#!/usr/bin/env python3
"""Conferência documental de L4 parcial. Somente leitura; não avalia equilíbrio em mesa."""
from pathlib import Path
import argparse,collections,hashlib,json,sys
ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--fontes',type=Path);ap.add_argument('--preparado',type=Path);a=ap.parse_args()
here=Path(__file__).absolute().parent;root=a.fontes or here.parents[1]
def path(rel):return a.preparado/rel if a.preparado and (a.preparado/rel).is_file() else root/rel
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
state=json.loads((here/'estado-inicial.json').read_text());data=json.loads((here/'cobertura-atualizada.json').read_text());before=json.loads(path(state['cobertura_anterior']).read_text());problems=[]
def check(ok,msg):
 if not ok:problems.append(msg)
reclassified=['M040','M043','M048','M049','M050']
check(len(data['pontos'])==len({r['id'] for r in data['pontos']})==130,'IDs M divergentes.')
check(len(data['competencias'])==len({r['id'] for r in data['competencias']})==20,'IDs P divergentes.')
for group in ['pontos','competencias']:
 prior={r['id']:r for r in before[group]}
 for r in data[group]:
  old=prior[r['id']]
  if r['id'] in reclassified:
   check(old['estado']=='P' and r['estado']=='E' and r['lote']=='—' and r['falta']=='—','Transição divergente: '+r['id'])
   excluded=['evidencias','estado','lote','falta','presente']
  elif r['id'] in ['M051','P20']:
   check(r['estado']==old['estado']=='P' and r['lote']==old['lote'],'Pendência indevidamente encerrada: '+r['id']);excluded=['evidencias','presente','restante','falta']
  else:excluded=['evidencias']
  check({k:v for k,v in r.items() if k not in excluded}=={k:v for k,v in old.items() if k not in excluded},'Escopo alterado: '+r['id'])
M=dict(collections.Counter(r['estado'] for r in data['pontos']));P=dict(collections.Counter(r['estado'] for r in data['competencias']))
check(M=={'E':113,'P':17} and data['totais_pontos']=={'E':113,'P':17,'L':0},'Contagens M divergentes.')
check(P==data['totais_competencias']=={'E':17,'P':3},'Contagens P divergentes.')
check([r['id'] for r in data['competencias'] if r['estado']=='P']==['P14','P15','P20'],'Competências restantes divergentes.')
check(all(not r['aprendizagem_observada'] for r in data['competencias']),'Aprendizagem indevidamente declarada.')
for b in data['lotes']:
 expected='entregue' if b['id'] in ['L1','L3','L2','L8'] else ('em andamento' if b['id']=='L4' else next(x['estado'] for x in before['lotes'] if x['id']==b['id']))
 check(b['estado']==expected,'Estado de lote divergente: '+b['id'])
checked=0
for r in data['pontos']+data['competencias']:
 for e in r['evidencias']:
  p=path(e['arquivo']);check(p.is_file(),'Fonte ausente: '+e['arquivo'])
  if not p.is_file():continue
  check(sha(p)==e['sha256'],'Fonte alterada: '+e['arquivo']);lines=p.read_text().splitlines();valid=1<=e['inicio']<=e['fim']<=len(lines);check(valid,'Trecho inválido: '+e['arquivo'])
  if valid:check(lines[e['inicio']-1].lstrip('# ').strip()==e['titulo'],'Título divergente: '+e['arquivo'])
  checked+=1
for field in ['fonte_R53','copia_R53']:check(sha(Path(state[field]))==state['R53_sha256'],'R53 alterada: '+field)
math=json.loads((here/'contas.json').read_text())
check(math['vida_rolada']==[9+2,9+4+2*2,9+4+10+2*3],'Vida rolada divergente.')
check(math['vida_fixa']==[12+2,12+2+7+2,12+2+2*(7+2)],'Vida fixa divergente.')
check(math['reparo']=={'maximo':41,'CD':12,'bonus':4,'primeiro':11,'repeticao':12,'recupera':20,'final':29,'classes':[20,20,20,13,10],'autonomo':12},'Reparo divergente.')
check(math['nilo']=={'PV':16,'PE':36,'defesa_escriba':13,'bloquear_constante':2,'vigor':3},'Nilo divergente.')
expected=[{'curtos':k,'excedente':36+9*k,'abundante':30+12*k,'condensada_cheia':42+7*k} for k in range(4)]
check(math['comparacao_cheia']==expected,'Comparação de menores divergente.')
check(math['estoque_por_longos']==[3,5,5,8],'Depósitos de G92 divergentes.')
check(math['ciclo_B']==[[30,12],[21,12],[27,6],[17,6],[24,6],[30,0],[8,0],[5,3],[30,3]],'Ciclo B divergente.')
check(math['escala']==[{'nivel':n,'essencia':e,'bastiao':4*n,'vanguarda':5*n,'emanador':6*n,'teto':4*e,'excedente':2*e} for n,e in [(1,3),(2,3),(5,3),(10,4),(20,5)]],'Escala divergente.')
check(math['usos_cadencias']==dict(inicial_um_curto=dict(condensada=22,excedente=17,abundante=11),avancada=[[170,162,168],[200,194,216]],saque_inicial=[8,6],apos_conjuracao_inicial=[5,6],saque_avancado=[18,10],apos_conjuracao_avancada=[9,10],cadencias=[dict(semanas=[1,2,3,4],estoque=[3,6,9,12]),dict(semanas=[4,8,12,16],estoque=[3,6,9,12])]),'Casos de ações/cadências divergentes.')
output=dict(etapa=85,contagens_M=data['totais_pontos'],contagens_P=P,evidencias_conferidas=checked,reclassificados=reclassified,pendentes_preservados=['M051','P20'],grupos_de_contas_conferidos=9,problemas=problems,limites='Integridade documental, contas explícitas e transições de cobertura. Não verifica compreensão humana ou equilíbrio de regras; Reserva não aprovada.')
print(json.dumps(output,ensure_ascii=False,indent=2));sys.exit(bool(problems))

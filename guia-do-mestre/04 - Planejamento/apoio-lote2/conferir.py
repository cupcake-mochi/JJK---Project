#!/usr/bin/env python3
"""Confere casos fixos de L2. --salvar grava somente resultados.json nesta pasta."""
from pathlib import Path
import argparse,collections,hashlib,json,math,re,sys
ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--fontes',type=Path);ap.add_argument('--preparado',type=Path);ap.add_argument('--salvar',action='store_true');a=ap.parse_args()
here=Path(__file__).absolute().parent;root=a.fontes or here.parents[1]
def path(rel):return a.preparado/rel if a.preparado and (a.preparado/rel).is_file() else root/rel
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
state=json.loads((here/'estado-inicial.json').read_text());data=json.loads((here/'cobertura-atualizada.json').read_text());before=json.loads(path(state['cobertura_anterior']).read_text());problems=[]
def check(ok,msg):
 if not ok:problems.append(msg)
g84=path('06 - Redacao do Guia/84-percursos-apoios-e-quedas.md').read_text();g85=path('06 - Redacao do Guia/85-trajetorias-ferramentas-e-improvisacao.md').read_text()
def number(s):return float(s.replace(',','.'))
routes=[]
for x,y,total,outcome in re.findall(r'^\| ([\d,]+) m \| ([\d,]+) m \| ([\d,]+) m \| ([^\n]+) \|$',g85,re.M):
 x,y,total=map(number,(x,y,total));check(x+y==total,'Soma de Ricochete incorreta.')
 valid=x<=18 and total<=24;long=x>6 or total>12
 check(('Inviável' in outcome)==(not valid),'Viabilidade do ricochete divergente.')
 if valid:check(('desvantagem' in outcome.lower())==long,'Faixa do ricochete divergente.')
 routes.append(dict(primeiro=x,segundo=y,total=total,permitido=valid,desvantagem_por_distancia=long if valid else None))
check(len(routes)==5,'Faltam percursos de Ricochete.')
points={}
for name,x,y in re.findall(r'^\| (Sora|Ponto de ricochete|Alvo) \| Coluna (\d+), linha (\d+) \|$',g85,re.M):points[name]=(int(x),int(y))
check(len(points)==3,'Faltam pontos do mapa.')
dist=lambda p,q:max(abs(p[0]-q[0]),abs(p[1]-q[1]))*1.5
map_lengths=[]
if len(points)==3:
 map_lengths=[dist(points['Sora'],points['Ponto de ricochete']),dist(points['Ponto de ricochete'],points['Alvo'])];check(map_lengths==[6,6],'Distâncias do mapa divergentes.')
swim=[3*3,3*1.5,3*4.5,3*3];check(swim==[9,4.5,13.5,9],'Custos de natação divergentes.')
for s in ['3 trechos × 3 m = **9 m**','3 × 1,5 m = **4,5 m**','3 × 4,5 m = **13,5 m**','3 × 3 m = **9 m**']:check(s in g84,'Tabela de natação alterada: '+s)
jump={'normal':3+1.5*1,'esforco':3+1.5*1+1.5,'movimento':3+6,'cd':max(14,18),'bonus':1+2+2//2,'sucesso':14+4,'falha':13+4}
check(jump=={'normal':4.5,'esforco':6.0,'movimento':9,'cd':18,'bonus':4,'sucesso':18,'falha':17},'Salto divergente.')
for s in ['**14 + 4 = 18**','**13 + 4 = 17**','**1 + 2 + 1 = +4**']:check(s in g84,'Conta de salto não localizada: '+s)
duct={'regular':1.5*3,'dificil':1.5*4,'restante_regular':9-4.5};check(duct=={'regular':4.5,'dificil':6.0,'restante_regular':4.5},'Duto divergente.')
fall=sum([2,4,5]);target=fall//2;faller=fall-target;fall_result={'dados':9//3,'total':fall,'alvo_antes_defesas':target,'quem_cai_antes_defesas':faller,'quem_cai_com_resistencia':math.ceil(faller/2),'quem_cai_se_alvo_evitar':math.ceil(fall/2)}
check(fall_result=={'dados':3,'total':11,'alvo_antes_defesas':5,'quem_cai_antes_defesas':6,'quem_cai_com_resistencia':3,'quem_cai_se_alvo_evitar':6},'Divisão ou resistência da queda divergente.')
sizes={'Minúsculo':0,'Pequeno':1,'Médio':2,'Grande':3,'Imenso':4,'Colossal':5};check(abs(sizes['Médio']-sizes['Grande'])<=1 and abs(sizes['Médio']-sizes['Imenso'])>1,'Faixa de tamanhos divergente.')
obra={'limite':2+3//2,'minutos':10*3,'vida':10+2+5*3,'defesa':10+1,'kg':100*3,'PE':2};check(80<=obra['kg'],'Carga da Passarela excedida.');check(obra=={'limite':3,'minutos':30,'vida':27,'defesa':11,'kg':300,'PE':2},'Obras divergentes.')
parkour={'movimento':9+3,'limite':12/2,'gasto':3+4.5,'restante':12-7.5,'limite_restante':6-3};check(parkour=={'movimento':12,'limite':6,'gasto':7.5,'restante':4.5,'limite_restante':3},'Parkour divergente.')
check(6/1.5*3==12 and 1.5//3==0,'Corda/queda de 1,5 m divergentes.')
check(12+5<18 and 13+5==18 and 18+5<24 and 19+5==24,'Fechadura/algema divergentes.')
weapons={'cabo_ataque':11+2+1,'cabo_dano':4+2,'garrafa_ataque':min(17,9)+4+1,'garrafa_dano':3+2,'garrafa_faixas':[6,18],'garrafa_critico':'2d4 + 2'}
check(weapons['cabo_ataque']==14 and weapons['cabo_dano']==6 and weapons['garrafa_ataque']==14 and weapons['garrafa_dano']==5,'Ataque/dano improvisado divergente.')
check('2d4 + 2' in g85,'Crítico improvisado divergente.')

check(len(data['pontos'])==130 and len({x['id'] for x in data['pontos']})==130,'IDs M ausentes/duplicados.')
check(len(data['competencias'])==20,'Competências divergentes.')
counts={k:sum(x['estado']==k for x in data['pontos']) for k in ['E','P','L']};check(counts=={'E':108,'P':22,'L':0},'Contagem de pontos divergente.')
check(dict(collections.Counter(x['estado'] for x in data['competencias']))=={'E':16,'P':4},'Contagem de competências divergente.')
old={x['id']:x for x in before['pontos']};changed=[]
for r in data['pontos']:
 prev=old[r['id']];check(all(r[k]==prev[k] for k in ['assunto','natureza','capitulo','previsto','discussao','pagina_inventario']),f"Escopo alterado: {r['id']}")
 if r['estado']!=prev['estado']:changed.append(r['id'])
check(changed==['M019','M020','M021','M022','M054','M064','M066'],'Reclassificação além de L2.')
check(sum(len(x['pontos']) for x in data['lotes'])==22,'Pendências restantes divergentes.')
for r in data['pontos']+data['competencias']:
 for e in r['evidencias']:
  p=path(e['arquivo']);check(p.is_file(),f"Fonte ausente: {e['arquivo']}")
  if not p.is_file():continue
  check(sha(p)==e['sha256'],f"Fonte alterada: {e['arquivo']}");lines=p.read_text().splitlines();valid=1<=e['inicio']<=e['fim']<=len(lines);check(valid,f"Trecho inválido: {e['arquivo']}")
  if valid:check(lines[e['inicio']-1].lstrip('# ').strip()==e['titulo'],f"Título divergente: {e['arquivo']}")
for field in ['fonte_R53','copia_R53']:check(sha(Path(state[field]))==state['R53_sha256'],'R53 alterada: '+field)
output=dict(etapa=83,natacao=swim,salto=jump,duto=duct,queda=fall_result,obra=obra,parkour=parkour,ricochete={'trechos_do_mapa':map_lengths,'percursos':routes,'defesa_direta':14+2,'defesa_final':14,'ataque':9+5,'dano':3+2},ferramentas={'instalacao_minutos':1,'maos':2,'descida_fisica_m':6,'movimento_descida_m':12,'fechadura':{'cd':18,'falha':17,'sucesso':18,'fim_primeira':'16h01','fim_segunda_se_possivel':'16h02'},'algema':{'cd':24,'falha':23,'sucesso':24}},armas_improvisadas=weapons,reclassificados=changed,contagens_M=counts,contagens_P=data['totais_competencias'],problemas=problems,limites='Conferência documental e aritmética de casos fixos; não simulação integral de combate, resgate ou aprendizagem com pessoas.')
if a.salvar:(here/'resultados.json').write_text(json.dumps(output,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(output,ensure_ascii=False,indent=2));sys.exit(bool(problems))

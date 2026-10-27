#!/usr/bin/env python3
"""Verificação documental de L8. Somente leitura; aceita um pacote preparado."""
from pathlib import Path
import argparse,collections,hashlib,json,sys
ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--fontes',type=Path);ap.add_argument('--preparado',type=Path);a=ap.parse_args()
here=Path(__file__).absolute().parent;root=a.fontes or here.parents[1]
def path(rel):return a.preparado/rel if a.preparado and (a.preparado/rel).is_file() else root/rel
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
state=json.loads((here/'estado-inicial.json').read_text());data=json.loads((here/'cobertura-atualizada.json').read_text());before=json.loads(path(state['cobertura_anterior']).read_text());problems=[]
def check(ok,msg):
 if not ok:problems.append(msg)
check(len(data['pontos'])==len({r['id'] for r in data['pontos']})==130,'IDs M divergentes.')
check(len(data['competencias'])==len({r['id'] for r in data['competencias']})==20,'IDs P divergentes.')
for group in ['pontos','competencias']:
 prior={r['id']:r for r in before[group]}
 for r in data[group]:
  old=prior[r['id']]
  if r['id']=='P02':check(old['estado']=='P' and r['estado']=='E' and r['lote']=='—','Transição de P02 divergente.')
  else:check({k:v for k,v in r.items() if k!='evidencias'}=={k:v for k,v in old.items() if k!='evidencias'},'Estado/escopo alterado fora de P02: '+r['id'])
M=dict(collections.Counter(r['estado'] for r in data['pontos']));P=dict(collections.Counter(r['estado'] for r in data['competencias']))
check(M=={'E':108,'P':22} and data['totais_pontos']=={'E':108,'P':22,'L':0},'Contagens M divergentes.')
check(P==data['totais_competencias']=={'E':17,'P':3},'Contagens P divergentes.')
check([r['id'] for r in data['competencias'] if r['estado']=='P']==['P14','P15','P20'],'Competências restantes divergentes.')
check(all(not r['aprendizagem_observada'] for r in data['competencias']),'Aprendizagem indevidamente declarada.')
for b in data['lotes']:check((b['estado']=='entregue')==(b['id'] in ['L1','L3','L2','L8']),'Estado de lote divergente: '+b['id'])
checked=0
for r in data['pontos']+data['competencias']:
 for e in r['evidencias']:
  p=path(e['arquivo']);check(p.is_file(),'Fonte ausente: '+e['arquivo'])
  if not p.is_file():continue
  check(sha(p)==e['sha256'],'Fonte alterada: '+e['arquivo']);lines=p.read_text().splitlines();valid=1<=e['inicio']<=e['fim']<=len(lines);check(valid,'Trecho inválido: '+e['arquivo'])
  if valid:check(lines[e['inicio']-1].lstrip('# ').strip()==e['titulo'],'Título divergente: '+e['arquivo'])
  checked+=1
for field in ['fonte_R53','copia_R53']:check(sha(Path(state[field]))==state['R53_sha256'],'R53 alterada: '+field)
output=dict(etapa=84,contagens_M=data['totais_pontos'],contagens_P=P,evidencias_conferidas=checked,reclassificados=['P02'],problemas=problems,limites='Integridade documental e transições de cobertura. Não verifica compreensão humana, cânone integral ou equilíbrio de regras.')
print(json.dumps(output,ensure_ascii=False,indent=2));sys.exit(bool(problems))

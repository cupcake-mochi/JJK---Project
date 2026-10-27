#!/usr/bin/env python3
"""Confere a correção de escopo, sem alterar arquivos."""
from pathlib import Path
import argparse,hashlib,json,collections,sys
ap=argparse.ArgumentParser();ap.add_argument('--fontes',type=Path);ap.add_argument('--preparado',type=Path);args=ap.parse_args();here=Path(__file__).absolute().parent;root=args.fontes or here.parents[1]
def source(rel):return args.preparado/rel if args.preparado and (args.preparado/rel).is_file() else root/rel
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
s=json.loads((here/'estado-inicial.json').read_text());a=json.loads((here/'cobertura-atualizada.json').read_text());b=json.loads(source(s['cobertura_anterior']).read_text());problems=[]
def ck(ok,msg):
 if not ok:problems.append(msg)
ck(a['totais_pontos']==b['totais_pontos']=={'E':113,'P':17,'L':0},'Totais M alterados.');ck(a['totais_competencias']==b['totais_competencias']=={'E':17,'P':3},'Totais P alterados.')
n=0
for group in ['pontos','competencias']:
 ck(len(a[group])==len(b[group]),'Número de entradas alterado.');prior={r['id']:r for r in b[group]}
 ck(len(prior)==len(b[group]) and {r['id'] for r in a[group]}==set(prior),'IDs alterados.')
 for r in a[group]:
  old=prior[r['id']];excluded={'evidencias'}|({'presente','falta'} if r['id']=='M051' else {'restante'} if r['id']=='P20' else set());ck({k:v for k,v in r.items() if k not in excluded}=={k:v for k,v in old.items() if k not in excluded},'Estado/escopo não autorizado: '+r['id'])
  for e in r['evidencias']:
   p=source(e['arquivo']);ck(p.is_file(),'Fonte ausente: '+e['arquivo'])
   if not p.is_file():continue
   lines=p.read_text().splitlines();ck(sha(p)==e['sha256'],'Hash divergente: '+e['arquivo']);valid=1<=e['inicio']<=e['fim']<=len(lines);ck(valid,'Trecho divergente: '+e['arquivo'])
   if valid:ck(lines[e['inicio']-1].lstrip('# ').strip()==e['titulo'],'Título divergente: '+e['arquivo'])
   n+=1
ck(a['lotes']==b['lotes'],'Estados de lote alterados.');ck(sha(Path(s['R53']))==s['R53_sha256'],'R53 alterada.')
g92=source('06 - Redacao do Guia/92-reserva-condensada-proposta-e-comparacao.md').read_text();ck('4 × Essência' not in g92 and '2 × Essência' not in g92 and 'acordo por personagem' in g92,'G92 ainda conserva o detalhamento numérico.');ck('descartou o detalhamento' in g92,'Decisão ausente de G92.')
print(json.dumps(dict(etapa=87,evidencias_conferidas=n,contagens_M=a['totais_pontos'],contagens_P=a['totais_competencias'],R53_intacta=not any('R53' in p for p in problems),decisao='Detalhamento descartado; habilidade existente mantida por enquanto.',problemas=problems),ensure_ascii=False,indent=2));sys.exit(bool(problems))

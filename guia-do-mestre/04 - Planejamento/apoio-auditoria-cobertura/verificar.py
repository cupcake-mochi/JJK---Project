#!/usr/bin/env python3
"""Conferência de cobertura, somente leitura. Nunca grava manifesto ou resultados."""
from pathlib import Path
import argparse,collections,hashlib,json,re,sys

ap=argparse.ArgumentParser(description=__doc__)
ap.add_argument('--fontes',type=Path,help='Raiz das fontes, para conferir uma cópia preparada antes da instalação.')
args=ap.parse_args()
here=Path(__file__).absolute().parent
root=args.fontes if args.fontes else here.parents[1]
audit=json.loads((here/'cobertura.json').read_text())
initial=json.loads((here/'estado-inicial.json').read_text())
errors=[]
def check(ok,message):
    if not ok: errors.append(message)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
points=audit['pontos'];comps=audit['competencias']
check(len(points)==130 and {x['id'] for x in points}=={f'M{i:03}' for i in range(1,131)},'Conjunto dos 130 IDs M divergente.')
check(len(comps)==20 and {x['id'] for x in comps}=={f'P{i:02}' for i in range(1,21)},'Conjunto dos 20 IDs P divergente.')
for group,key in [(points,'totais_pontos'),(comps,'totais_competencias')]:
    check(dict(collections.Counter(x['estado'] for x in group))==audit[key],f'Contagem divergente: {key}')
check(all(x['estado'] in {'E','P','L'} for x in points+comps),'Estado editorial inválido.')
check(all(x['aprendizagem_observada'] is False for x in comps),'Aprendizagem observada indevidamente declarada.')
check(collections.Counter(x['natureza'] for x in points)=={'R':49,'M':67,'G':11,'A':3},'Naturezas do inventário divergentes.')
inventory=(here/'inventario-extraido.txt').read_text()
ids=re.findall(r'(?m)^(M\d{3}) \|',inventory)
check(len(ids)==130 and set(ids)=={x['id'] for x in points},'Extração do inventário não corresponde aos IDs.')
batch={b['id']:b for b in audit['lotes']}
for row in points:
    if row['estado']=='E': check(row['falta']=='—' and row['lote']=='—',f"{row['id']}: complemento contraditório.")
    else:
        check(row['falta']!='—' and row['lote'] in batch,f"{row['id']}: lacuna sem destino.")
        if row['lote'] in batch: check(row['id'] in batch[row['lote']]['pontos'],f"{row['id']}: lote não inclui ponto.")
check(set(x for b in batch.values() for x in b['pontos'])=={x['id'] for x in points if x['estado']!='E'},'Distribuição de lacunas divergente.')
check(sum(len(b['pontos']) for b in batch.values())==37,'Lacuna duplicada ou omitida.')

cache={};evcount=0
for row in points+comps:
    check(bool(row['evidencias']),f"{row['id']}: sem evidência.")
    for ev in row['evidencias']:
        rel=ev['arquivo'];path=root/rel
        if rel not in cache:
            if not path.is_file():errors.append(f'Fonte ausente: {rel}');continue
            cache[rel]=(sha(path),path.read_text().splitlines())
        digest,lines=cache[rel]
        check(digest==ev['sha256'],f'Fonte alterada: {rel}')
        start,end=ev['inicio'],ev['fim']
        valid=1<=start<=end<=len(lines)
        check(valid,f'Trecho inválido: {rel} {start}:{end}')
        if valid:check(lines[start-1].lstrip('# ').strip()==ev['titulo'],f'Título de evidência divergente: {rel}:{start}')
        evcount+=1
for rel,digest in initial['secoes_numeradas'].items():
    check((root/rel).is_file() and sha(root/rel)==digest,f'Seção numerada alterada: {rel}')
for name,s in initial['fontes'].items():
    path=Path(s['caminho'])
    check(path.is_file() and sha(path)==s['sha256'],f'Fonte-base alterada: {name}')
report=dict(pontos=len(points),competencias=len(comps),contagens_pontos=audit['totais_pontos'],contagens_competencias=audit['totais_competencias'],lotes=len(batch),trechos_referenciados=evcount,arquivos_de_evidencia=len(cache),secoes_numeradas_preservadas=len(initial['secoes_numeradas']),problemas=errors,limites='Confere estrutura, fontes e localização da evidência; não avalia por algoritmo a suficiência editorial, o equilíbrio ou o aprendizado.')
print(json.dumps(report,ensure_ascii=False,indent=2))
sys.exit(bool(errors))

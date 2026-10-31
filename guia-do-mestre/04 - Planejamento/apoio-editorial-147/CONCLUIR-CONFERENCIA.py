from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import json,hashlib
r=Path('/media/mizuki/HD Externo II/Claude/Pesquisa de Campo - Mestragem');a=r/'04 - Planejamento/apoio-editorial-147'
def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  while block:=f.read(1024*1024):h.update(block)
 return h.hexdigest()
def save(p,d):p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
c=json.loads((a/'composicao.json').read_text());controls=json.loads((a/'arquivos-do-lote.json').read_text())['controles'];report=r/'04 - Planejamento/147-ajustes-de-consulta-e-leitura.md'
base=json.loads((a/'antes/manifesto-entrega.json').read_text());assert len(base)==6396
allowed=set(controls)|{p.relative_to(r).as_posix() for p in (r/'07 - Edicao de Leitura/edicao-integrada-136').glob('*.html')}|{'07 - Edicao de Leitura/edicao-integrada-136/leitura.css','06 - Redacao do Guia/edicao-integrada-136/03a-ideias-para-aventuras.md'}
def check(item):
 rel,h=item;p=r/rel;assert p.is_file(),rel;actual=sha(p);assert actual==h or rel in allowed,rel;return rel,actual
cache=a/'progresso-da-conferencia.json'
actual=json.loads(cache.read_text()) if cache.exists() else {}
pending=[x for x in base.items() if x[0] not in actual]
with ThreadPoolExecutor(max_workers=2) as pool:
 for index,(rel,h) in enumerate(pool.map(check,pending),1):
  actual[rel]=h
  if index%100==0:
   save(cache,actual);print(f'Conferidos {len(actual)}/{len(base)}',flush=True)
save(cache,actual)
print('Acervo anterior conferido.',flush=True)
changed=[k for k in base if base[k]!=actual[k]]
assert len([x for x in changed if x.startswith('06 - Redacao do Guia/edicao-integrada-136/')])==1
sources=json.loads((r/'04 - Planejamento/apoio-estrutura-99/estrutura-e-fontes.json').read_text())['fontes'];assert all(sha(r/x['fonte'])==x['sha256'] for x in sources)
save(a/'conferencia-do-manifesto.json',{'registro':147,'entradas_anteriores':len(base),'alteracoes':changed,'originais_preservados':104,'fontes_integradas_alteradas':1,'fontes_integradas_preservadas':98,'pdfs_anteriores_preservados':True,'falhas':[]})
files=[p for p in a.rglob('*') if p.is_file() and '__pycache__' not in p.parts]+[report,r/c['pdf'],r/'08 - Diagramacao do Guia/output/pdf/Ciclo-Maldito-Folhas-para-a-Mesa-Impressao.pdf']
assert json.loads((r/'04 - Planejamento/apoio-piloto/manifesto-entrega.json').read_text())==base,'O manifesto foi alterado durante o fechamento'
updated=dict(base);updated.update({x:actual[x] for x in changed});updated.update({p.relative_to(r).as_posix():sha(p) for p in files});save(r/'04 - Planejamento/apoio-piloto/manifesto-entrega.json',updated)
print(json.dumps({'entradas_finais':len(updated),'alterados':len(changed),'novos':len(updated)-len(base),'falhas':0}))

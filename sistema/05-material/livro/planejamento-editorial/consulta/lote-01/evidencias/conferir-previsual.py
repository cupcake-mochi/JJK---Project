from pathlib import Path
from collections import Counter
from fractions import Fraction
from itertools import product
import json,hashlib,re,unicodedata,sys
import pdfplumber
from pypdf import PdfReader
B=Path(sys.argv[1]).resolve()
P=next(p for p in B.parents if (p/'validacao-editorial/PROTOCOLO-COMPLETO.md').exists())
R=P.parents[3]
CONFIG=json.loads((B/'VALIDACAO.json').read_text());F=CONFIG['manuscrito'];PDF=CONFIG['pdf'];N=CONFIG['paginas']
checks=[]
def ck(n,a,b):checks.append({'verificacao':n,'obtido':a,'esperado':b,'ok':a==b})
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def words(s):return re.findall(r'\w+',unicodedata.normalize('NFKC',s).casefold())
md=(B/F).read_text();meta=json.loads((B/'ESTRUTURA.json').read_text());chunks=re.split(r'<!-- page:([^|]+)\|([^>]+) -->\s*',md);sections={chunks[i]:chunks[i+2] for i in range(1,len(chunks),3)}
r=PdfReader(B/'output/pdf'/PDF)
ck('Quantidade de páginas e seções',[len(r.pages),len(sections)],[N,N]);ck('Sequência',list(sections),meta['ordem'])
ck('Títulos correspondem ao mapa',all(s.splitlines()[0]=='# '+meta['titulos'][k] for k,s in sections.items()),True)
top=[o for o in r.outline if not isinstance(o,list)]
ck('Entradas principais',len(top),len(meta['grupos']))
ck('Grupos recolhidos',[o.get('/Count') for o in top if o.get('/Count')],[-len(keys) for _,keys in meta['grupos'] if len(keys)>1])
def flatten(nodes):
 for n in nodes:
  if isinstance(n,list):yield from flatten(n)
  else:yield n
ck('Destinos de marcadores válidos',all(0<=r.get_destination_page_number(o)<N for o in flatten(r.outline)),True)
ids={p.indirect_reference.idnum:i+1 for i,p in enumerate(r.pages)};geom=[]
with pdfplumber.open(B/'output/pdf'/PDF) as doc:
 for i,(p,(key,s)) in enumerate(zip(doc.pages,sections.items()),1):
  clean=re.sub(r'\[([^\]]+)\]\(#[^)]+\)',r'\1',s);t=p.extract_text(x_tolerance=1,y_tolerance=3)
  ck(f'p{i}: texto completo',dict(Counter(words(clean))-Counter(words(t))),{})
  cs=[c for c in p.chars if c['text'].strip()];body=[c for c in cs if 48<c['top']<785]
  ck(f'p{i}: texto dentro da página',all(0<=c['x0']<=c['x1']<=p.width and 0<=c['top']<=c['bottom']<=p.height for c in cs),True)
  ck(f'p{i}: corpo separado de rodapé',max(c['bottom'] for c in body)<785,True)
  embed=set()
  for f in r.pages[i-1]['/Resources']['/Font'].values():
   o=f.get_object();d=o.get('/FontDescriptor')
   if d and any(k in d.get_object() for k in ['/FontFile','/FontFile2','/FontFile3']):embed.add(str(o['/BaseFont']).lstrip('/'))
  ck(f'p{i}: fontes incorporadas',sorted({c['fontname'] for c in cs}-embed),[])
  ck(f'p{i}: sem imagem raster',len(p.images),0)
  refs=re.findall(r'\]\(#([^)]+)\)',s);ck(f'p{i}: remissões existentes',[x for x in refs if x not in meta['paginas']],[])
  targets=[]
  for ar in r.pages[i-1].get('/Annots',[]):
   a=ar.get_object()
   if a.get('/Subtype')=='/Link':
    d=a.get('/Dest');targets.append(ids.get(d[0].idnum) if d else None)
  ck(f'p{i}: links corretos',sorted(set(targets)),sorted({meta['paginas'][x] for x in refs}))
  for ref in set(refs):ck(f'p{i}: página citada {ref}',f"(p. {meta['paginas'][ref]})" in re.sub(r'\s+', ' ', t),True)
  geom.append({'pagina':i,'final_corpo':round(max(c['bottom'] for c in body),2)})
snap=json.loads((B/'evidencias/fontes-preservadas.json').read_text());ck('Fontes e versões anteriores preservadas',[n for n,h in snap.items() if sha(R/n)!=h],[])
inv=json.loads((R/'sistema/05-material/livro/planejamento-editorial/INVENTARIO-BASE.json').read_text());ck('Livro e exportações preservados',[x['arquivo'] for x in inv['fontes']+inv['artefatos_publicados'] if sha(R/x['arquivo'])!=x['sha256']],[])
rev=json.loads((B/'evidencias/REVISAO-EDITORIAL.json').read_text());ck('Revisão do texto atual',rev['sha256_texto'],sha(B/F));ck('Seções lidas',len(rev['secoes']),N)
import sys
sys.path.insert(0,str(P/'validacao-editorial'))
from conferir_editorial import check_file
ck('Bloqueio editorial e revisão contextual',check_file(B/F,True),[])

scenario=json.loads((B/'evidencias/regras-verificadas.json').read_text())
ck('Cenários mecânicos e interfaces',scenario['ok'],True)
ck('Cenários usam o manuscrito atual',scenario['sha256_texto'],sha(B/F))
if CONFIG.get('auditoria_numerica'):
 audit=json.loads((B/CONFIG['auditoria_numerica']).read_text())
 ck('Auditoria numérica concluída',audit['ok'],True)
 linked=audit.get('manuscritos_auditados',{})
 ck('Auditoria inclui este manuscrito',str((B/F).relative_to(R)) in linked,True)
 ck('Números vinculados a textos atuais',[n for n,h in linked.items() if sha(R/n)!=h],[])

res={'data':'2026-10-03','ok':all(c['ok'] for c in checks),'verificacoes':len(checks),'sha256_pdf':sha(B/'output/pdf'/PDF),'sha256_texto':sha(B/F),'checks':checks,'geometria':geom,'estado_visual':'pendente — não verificado por este script','limites':['Modelos e conferências documentais não substituem teste com leitores e jogadores.']}
(B/'evidencias/PRE-CONFERENCIA-PDF.json').write_text(json.dumps(res,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'unidade':B.name,'ok':res['ok'],'verificacoes':len(checks),'falhas':[c for c in checks if not c['ok']]},ensure_ascii=False))
raise SystemExit(0 if res['ok'] else 1)

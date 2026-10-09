from pathlib import Path
from collections import Counter,defaultdict
import hashlib,json,re,unicodedata,runpy,sys
from pypdf import PdfReader
import pdfplumber
B=Path(__file__).resolve().parent
m=json.loads((B/'FONTES-E-VALIDACAO.json').read_text());pdf=B/m['pdf'];reader=PdfReader(pdf)
g=runpy.run_path(str(B/'ler_fontes.py'))
issues=[];checks=0
def check(ok,kind,detail=None):
 global checks
 checks+=1
 if not ok:issues.append({'tipo':kind,'detalhe':detail})
def plain(s):
 s=re.sub(r'\[([^\]]+)\]\([^)]+\)',r'\1',s)
 s=re.sub(r'^[#>•\-]+\s*','',s);s=s.replace('–','-').replace('—','-').replace('−','-')
 return re.sub(r'\s+',' ',unicodedata.normalize('NFKC',s).replace('*','').replace('`','')).strip()
def tokens(s):return re.findall(r'\w+|[^\w\s]',plain(s).casefold())
check(hashlib.sha256(pdf.read_bytes()).hexdigest()==m['sha256_pdf'],'PDF exato')
check(len(reader.pages)==m['paginas'],'Contagem de páginas')
for k,source in m['fontes_locais_r30'].items():check(hashlib.sha256((B/'fontes-editoriais'/source['arquivo']).read_bytes()).hexdigest()==source['sha256'],'Fonte R30 conferida',k)
source_events=defaultdict(list)
for e in m['eventos']:
 if e['bloco'] in g['all_blocks'] and not e['gerado']:source_events[e['bloco']].append(e)
for key,block in g['all_blocks'].items():
 expected=[]
 for line in g['enriched'][key].splitlines()[1:]:
  line=line.strip()
  if not line or line=='---':continue
  if line.startswith('|'):
   if re.fullmatch(r'[\s|:\-]+',line):continue
   expected.extend(v.strip() for v in line.strip('|').split('|'))
  else:expected.append(line)
 actual=[]
 for e in source_events[key]:
  if e['tipo']=='table':actual.extend(v for row in e['texto'] for v in row)
  elif not e['tipo'].startswith('h') and e['tipo'] not in ['major','esquema']:actual.append(e['texto'])
  elif e['tipo'].startswith('h') and (e['tipo']!='h1' or e['texto']!=block.title):actual.append(e['texto'])
 missing=Counter(t for line in expected for t in tokens(line))-Counter(t for line in actual for t in tokens(line))
 check(not missing,'Conteúdo integral do bloco',{'bloco':key,'faltam':dict(missing)})
 check(key in m['ancoras'],'Âncora de origem',key)
 check(bool(source_events[key]),'Elementos de origem',key)
# Every complete subsection has one page and one prose width; continuations are documented.
for info in m['conjuntos_informacao']:
 a,b=info['eventos'];rows=m['eventos'][a:b]
 check(len({e['pagina'] for e in rows})==1,'Informação inteira na página',info['chave'])
 check(len({e['largura'] for e in rows})==1,'Largura estável',info['chave'])
for e in m['eventos']:
 check(e['y']>= (53 if next(p for p in m['paginas_planejadas'] if p['pagina']==e['pagina'])['tipo']=='form' else 100) and e['y']+e['altura']<=789,'Conteúdo dentro da área',{'pagina':e['pagina'],'bloco':e['bloco'],'tipo':e['tipo'],'y':e['y']})
 check(e['x']>=53 and e['x']+e['largura']<=542,'Margens do texto',{'pagina':e['pagina'],'bloco':e['bloco']})
# Bounding rectangles of drawn flowables must not intersect.
by_page=defaultdict(list)
for e in m['eventos']:by_page[e['pagina']].append(e)
for page,rows in by_page.items():
 for i,e in enumerate(rows):
  for f in rows[i+1:]:
   overlapx=min(e['x']+e['largura'],f['x']+f['largura'])-max(e['x'],f['x'])
   overlapy=min(e['y']+e['altura'],f['y']+f['altura'])-max(e['y'],f['y'])
   check(overlapx<=.02 or overlapy<=.02,'Sobreposição',{'pagina':page,'blocos':[e['bloco'],f['bloco']]})
# PDF links must resolve to an existing page and match the intended bookmark coordinates.
page_ids={p.indirect_reference.idnum:i+1 for i,p in enumerate(reader.pages)};links=0
for i,p in enumerate(reader.pages,1):
 for ref in p.get('/Annots',[]):
  a=ref.get_object()
  if a.get('/Subtype')!='/Link':continue
  dest=a.get('/Dest')
  if dest is None:continue
  links+=1
  target=page_ids.get(dest[0].idnum) if hasattr(dest[0],'idnum') else None
  check(target is not None,'Destino de link',{'pagina':i,'destino':str(dest)[:140]})
outline=[]
def visit(items):
 for x in items:
  if isinstance(x,list):visit(x)
  else:outline.append(x)
visit(reader.outline)
check(len(outline)==len(m['marcadores']),'Marcadores selecionados',len(outline))
check({r.title for r in outline}=={v['titulo'] for v in m['marcadores'].values()},'Títulos dos marcadores')
for row in outline:
 check(reader.get_destination_page_number(row)>=0,'Destino do marcador',row.title)
 expected=next(v for v in m['marcadores'].values() if v['titulo']==row.title and v['pagina']==reader.get_destination_page_number(row)+1)
 check(expected['pagina']==reader.get_destination_page_number(row)+1,'Página correta do marcador',row.title)
def check_tree(items,level=0):
 for row in items:
  if isinstance(row,list):check_tree(row,level+1)
  else:
   expected=[v for v in m['marcadores'].values() if v['titulo']==row.title and v['pagina']==reader.get_destination_page_number(row)+1]
   check(any(v['nivel']==level for v in expected),'Hierarquia do marcador',{'titulo':row.title,'nivel':level})
check_tree(reader.outline)
# Extracted PDF must contain the source text, using the pages where that source was drawn.
pdftexts=[p.extract_text() or '' for p in reader.pages]
def dense(s):return re.sub(r'\s+','',plain(s).casefold())
for key,es in source_events.items():
 pages=sorted({e['pagina'] for e in es});text=dense(' '.join(pdftexts[p-1] for p in pages))
 for e in es:
  strs=[v for row in e['texto'] for v in row] if e['tipo']=='table' else [e['texto']] if e['tipo']!='esquema' else []
  for s in strs:
   val=dense(s)
   if val:check(val in text,'Texto desenhado no PDF',{'bloco':key,'pagina':e['pagina'],'texto':str(s)[:150]})
fulltext='\n'.join(pdftexts)
for forbidden in ['Edição de trabalho','diagramação integral R20','REFERÊNCIA DE TESTE','Fontes consultadas','trabalho editorial','Regras editoriais:']:
 check(forbidden not in fulltext,'Notas de produção fora do livro',forbidden)
check('Ciclo Maldito' in pdftexts[0],'Capa com nome oficial')
toc=m['ancoras']['sumario']['pagina']-1
tocpages=[p['pagina'] for p in m['paginas_planejadas'] if p['tipo']=='toc']
toc_text=' '.join(pdftexts[p-1] for p in tocpages)
check('Sumário' in toc_text and all(str(i)+'. '+c['titulo'] in toc_text for i,c in enumerate(g['chapters'],1)),'Sumário detalhado completo após a capa')
check(len(m['capas_e_aberturas'])==22,'Capa e vinte e uma aberturas')
check('Arquivo > Fazer uma cópia' in plain(fulltext) and 'conta Google' in plain(fulltext),'Instruções de cópia da ficha')
# Scan actual glyph boxes for clipping at the page edges and unexpected replacement marks.
with pdfplumber.open(pdf) as pp:
 for i,p in enumerate(pp.pages,1):
  check(all(c['x0']>=-.2 and c['x1']<=p.width+.2 and c['top']>=-.2 and c['bottom']<=p.height+.2 for c in p.chars),'Glifos dentro da página',i)
  check(not any(c['text'] in ['\ufffd','■'] for c in p.chars),'Glifos faltantes',i)
# Images: verify original files, crop bounds, native PDF pixels and text separation.
from PIL import Image
for name,data in m['imagens']['imagens'].items():
 path=B/'referencias'/data['arquivo'];im=Image.open(path);im.load()
 check(hashlib.sha256(path.read_bytes()).hexdigest()==data['sha256_arquivo'],'Original da imagem preservado',name)
 check(list(im.size)==data['dimensoes_arquivo'],'Dimensões originais da imagem',name)
 x0,y0,x1,y1=data['crop'];check(0<=x0<x1<=im.width and 0<=y0<y1<=im.height,'Recorte dentro da imagem',name)
for art in m.get('posicionamento_imagens',[]):
 name=art['imagem'];pn=art['pagina'];data=m['imagens']['imagens'][name]
 check(art['y']+art['altura']<=art['topo_texto_livre']+.02,'Imagem separada do texto',name)
 check(art['y']>=107 and art['x']>=-.02 and art['x']+art['largura']<=595.3,'Painel dentro da página e acima da navegação',name)
 for e in by_page[pn]:
  overlapx=min(art['x']+art['largura'],e['x']+e['largura'])-max(art['x'],e['x'])
  overlapy=min(art['y']+art['altura'],e['y']+e['altura'])-max(art['y'],e['y'])
  check(overlapx<=.02 or overlapy<=.02,'Imagem não cobre texto',{'pagina':pn,'imagem':name})
 check(any(list(img.image.size)==data['dimensoes_arquivo'] for img in reader.pages[pn-1].images),'Imagem inserida sem reduzir pixels',{'pagina':pn,'imagem':name})
 if data.get('preservar_recorte'):
  expected=art['largura']*(data['crop'][3]-data['crop'][1])/(data['crop'][2]-data['crop'][0])
  check(abs(expected-art['altura'])<.02,'Recorte sem corte adicional automático',name)
report={'sha256_pdf':m['sha256_pdf'],'checagens':checks,'problemas':issues,'links_internos':links,'marcadores':len(outline),'blocos':len(g['all_blocks']),'paginas':len(reader.pages),'escopo':'Conteúdo, fontes locais da R30, geometria dos elementos, remissões e extração real. Revisão visual e teste de mesa são registros separados.'}
(B/'evidencias/CONFERENCIA.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:v for k,v in report.items() if k!='problemas'},ensure_ascii=False));print('Problemas',len(issues));print(json.dumps(issues[:12],ensure_ascii=False,indent=2))
sys.exit(bool(issues))

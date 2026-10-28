from pathlib import Path
from collections import Counter
import json,re,hashlib,unicodedata
import pymupdf as fitz
from pypdf import PdfReader
from PIL import Image,ImageDraw
H=Path(__file__).resolve().parent;B=H/'composicao';O=B/'output/pdf';V=H/'revisao';O.mkdir(parents=True,exist_ok=True);V.mkdir(exist_ok=True)
light=O/'Ciclo-Maldito-R58.pdf';dark=O/'Ciclo-Maldito-R58-Noturno.pdf'
m=json.loads((B/'FONTES-E-VALIDACAO.json').read_text());g=json.loads((B/'GEOMETRIA-CANDIDATA.json').read_text());source=(H/'LIVRO-CANDIDATA.md').read_text()
a=PdfReader(light);b=PdfReader(dark);checks=[]
def check(name,ok):checks.append({'verificacao':name,'aprovado':bool(ok)})
def norm(s):
 s=re.sub(r'\[([^\]]+)\]\([^)]*\)',r'\1',str(s));s=s.replace('−','-').replace('–','-').replace('—','-')
 return ''.join(x.lower() for x in unicodedata.normalize('NFKD',s) if x.isalnum())
check('Contagem das duas paletas corresponde ao manifesto.',len(a.pages)==len(b.pages)==m['paginas'])
# Ordem física dos blocos, além da presença do texto.
positions=m['ancoras'];hits=list(re.finditer(r'^## (\d+)\. .+$',source,re.M));order_errors=[]
for i,match in enumerate(hits):
 segment=source[match.end():hits[i+1].start() if i+1<len(hits) else len(source)]
 keys=re.findall(r'<!-- fonte:[^>]+-->\s*<a id="([^"]+)"></a>',segment)
 seq=[(positions[k]['pagina'],-positions[k]['y'],positions[k]['x']) for k in keys if k in positions]
 # Blocos em uma mesma página podem mudar de coluna; só a ordem entre páginas é comparada aqui.
 if [x[0] for x in seq]!=sorted(x[0] for x in seq):order_errors.append(match[1])
check('Blocos seguem a ordem editorial entre páginas.',not order_errors)
check('Regra Própria antecede o primeiro feitiço.',positions['fundamento-link-criar-regra-propria']['pagina']<positions['fundamento--primeiro']['pagina'])

check('Fonte da composição é idêntica à candidata.',(B/'LIVRO-COMPLETO.md').read_text()==source)
texta=[p.extract_text() or '' for p in a.pages];textb=[p.extract_text() or '' for p in b.pages]
check('Texto idêntico em todas as páginas entre paletas.',texta==textb)
alltext=norm(' '.join(texta));manifesttext=norm(' '.join(str(e['texto']) for e in m['eventos']))
missing=[]
for line in source.splitlines():
 l=line.strip()
 if re.fullmatch(r'### (?:Glossário: .+|Índice de assuntos)',l):continue
 if not l or l.startswith(('<!--','<a id=','# Ciclo Maldito','# Parte ','## ')) or l=='Livro de regras' or re.fullmatch(r'[|:\s-]+',l):continue
 values=[c.strip() for c in l.strip('|').split('|')] if l.startswith('|') else [re.sub(r'^[#>•\-]+\s*','',l)]
 for t in values:
  q=norm(t)
  if len(q)>2 and q not in alltext:missing.append({'texto':t[:240],'presente_no_manifesto':q in manifesttext})
check('Todas as linhas e células da candidata localizadas no PDF.',not missing)
check('Sem glifos de substituição ou âncoras brutas.',all('\ufffd' not in x and '\u25a0' not in x and '<a id=' not in x for x in texta))
# Geometria dos blocos reais, sem incluir arte e capas no limite do corpo.
margin=[];overlap=[]
for p in g['paginas']:
 if p['tipo'] in ['cover','art','credits']:continue
 rows=p['blocos']
 for i,x in enumerate(rows):
  if x['x']<g['limites']['esquerda']-.5 or x['x']+x['w']>g['limites']['direita']+.5 or x['y']<g['limites']['base']-.5 or x['y']+x['h']>g['limites']['topo']+.5:margin.append({'pagina':p['pagina'],'texto':x['texto'][:90]})
  for y in rows[i+1:]:
   ix=min(x['x']+x['w'],y['x']+y['w'])-max(x['x'],y['x']);iy=min(x['y']+x['h'],y['y']+y['h'])-max(x['y'],y['y'])
   if ix>.5 and iy>.5:overlap.append({'pagina':p['pagina'],'a':x['texto'][:90],'b':y['texto'][:90]})
check('Sem estouro de margem nos blocos de texto.',not margin)
check('Sem sobreposição entre blocos de texto.',not overlap)
refs={p.indirect_reference.idnum for p in a.pages};bad=[];links=Counter()
for n,p in enumerate(a.pages,1):
 for ref in p.get('/Annots',[]):
  ann=ref.get_object()
  if ann.get('/Subtype')!='/Link':continue
  ac=ann.get('/A')
  if ac and ac.get('/S')=='/URI':links['externos']+=1;continue
  z=ann.get('/Dest') or (ac.get('/D') if ac else None);z=z.get_object() if hasattr(z,'get_object') else z
  if not isinstance(z,list) or z[0].idnum not in refs:bad.append(n)
  links['internos']+=1
check('Todos os links internos chegam a páginas existentes.',not bad)
da=fitz.open(light);db=fitz.open(dark);diff=[]
for n,(pa,pb) in enumerate(zip(da,db),1):
 wa=pa.get_text('words');wb=pb.get_text('words')
 if len(wa)!=len(wb) or any(x[4]!=y[4] or max(abs(i-j) for i,j in zip(x[:4],y[:4]))>.01 for x,y in zip(wa,wb)):diff.append(n)
check('Texto ocupa as mesmas posições nas duas paletas.',not diff)
# Páginas para atenção na revisão visual: altura final em cada coluna.
occ=[]
for p in g['paginas']:
 if p['tipo']=='cover' or not p['blocos']:continue
 left=[x['y'] for x in p['blocos'] if x['x']<150 and x['w']<300];right=[x['y'] for x in p['blocos'] if x['x']>250 and x['w']<300]
 if left and right:
  cap=g['limites']['topo']-g['limites']['base'];lh=(g['limites']['topo']-min(left))/cap;rh=(g['limites']['topo']-min(right))/cap
  if max(lh,rh)-min(lh,rh)>.25 or max(lh,rh)<.67:occ.append({'pagina':p['pagina'],'ocupacao_esquerda':round(lh,2),'ocupacao_direita':round(rh,2),'tipo':p['tipo']})
report={'resultado':'aprovado' if all(x['aprovado'] for x in checks) else 'requer revisão','paginas':len(a.pages),'verificacoes':checks,'conteudo_ausente':missing,'margens':margin,'sobreposicoes':overlap,'links':dict(links),'links_invalidos':bad,'diferencas_geometria':diff,'paginas_para_atencao_visual':occ}
(V/'VALIDACAO.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n');(V/'TEXTO-EXTRAIDO.txt').write_text('\n\n'.join(f'PÁGINA {i+1}\n{x}' for i,x in enumerate(texta)))
print(json.dumps({k:report[k] for k in ['resultado','paginas','conteudo_ausente','margens','sobreposicoes','links','diferencas_geometria','paginas_para_atencao_visual']},ensure_ascii=False))
if '--render' in __import__('sys').argv:
 for palette,doc in [('claro',da),('noturno',db)]:
  folder=V/'visual'/palette;folder.mkdir(parents=True,exist_ok=True)
  for n,page in enumerate(doc,1):
   if n%80==0:print(palette,n,'páginas renderizadas',flush=True)
   path=folder/f'pagina-{n:03d}.png';page.get_pixmap(matrix=fitz.Matrix(1.25,1.25),alpha=False).save(path)
  for start in range(0,len(doc),8):
   sheet=Image.new('RGB',(1800,1320),'#777777');draw=ImageDraw.Draw(sheet)
   for j in range(min(8,len(doc)-start)):
    im=Image.open(folder/f'pagina-{start+j+1:03d}.png');im.thumbnail((440,625));x=(j%4)*450+(450-im.width)//2;y=(j//4)*660+24;sheet.paste(im,(x,y));draw.text((x,y-20),f'{palette} / {start+j+1}',fill='white')
   sheet.save(folder/f'contato-{start//8+1:03d}.jpg',quality=90)
 print('Todas as páginas renderizadas nas duas paletas.')

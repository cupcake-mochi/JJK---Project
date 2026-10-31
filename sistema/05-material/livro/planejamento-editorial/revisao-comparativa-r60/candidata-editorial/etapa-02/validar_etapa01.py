from pathlib import Path
import json,re,hashlib
import pymupdf as f
from PIL import Image,ImageDraw
H=Path(__file__).resolve().parent;B=H/'composicao';O=B/'output/pdf';V=H/'revisao';V.mkdir(exist_ok=True)
d=f.open(O/'Ciclo-Maldito-Livro-de-Regras.pdf');n=f.open(O/'Ciclo-Maldito-Livro-de-Regras-Noturno.pdf');m=json.loads((B/'FONTES-E-VALIDACAO.json').read_text());rows=json.loads((B/'NAVEGACAO-CANDIDATA.json').read_text());checks=[]
def check(t,v):checks.append({'verificacao':t,'aprovado':bool(v)})
check('Mesmo número de páginas e texto nas duas paletas',len(d)==len(n) and all(p.get_text()==q.get_text() for p,q in zip(d,n)))
seq=[]
for r in rows:
 a=m['ancoras'][r['destino']];seq.append((a['pagina'],0 if a['x']<290 else 1,-a['y']))
check('Sumário segue a sequência da leitura em Fundamento',seq==sorted(seq))
# Printed table of contents and digital outline share destination and title.
toc=[x for x in d.get_toc() if x[1] in {r['titulo'] for r in rows} and 240<x[2]<300]
check('Todos os assuntos no marcador digital',len(toc)==len(rows) and [x[1] for x in toc]==[r['titulo'] for r in rows])
log=json.loads((B/'revisao-r45/SUMARIO-PAGINADO.json').read_text());printed=[r for p in log for r in p['entradas'] if r['destino'] in {x['destino'] for x in rows}]
check('Sumário impresso usa a mesma ordem e destinos',[(x['titulo'],x['destino']) for x in printed]==[(x['titulo'],x['destino']) for x in rows])
check('Cabeçalhos antigos de Selo e Talentos removidos',not any('Selo e Talentos' in str(e.get('texto','')) for e in m['eventos'] if e.get('gerado') and e.get('capitulo')==10))
invalid=[]
for i,p in enumerate(d,1):
 for a in p.get_links():
  if a['kind']==1 and not 0<=a['page']<len(d):invalid.append(i)
check('Nenhum destino interno fora do livro',not invalid)
base=f.open(H.parents[3]/'Ciclo-Maldito-Livro-de-Regras.pdf');changed=[]
for i,(p,q) in enumerate(zip(base,d),1):
 if p.get_text()!=q.get_text():changed.append(i)
check('Mudanças de texto visual limitadas a sumário e Fundamento',len(d)==len(base) and all(2<=x<=5 or 248<=x<=286 for x in changed))
# Inspect TOC and every Fundamento page with altered generated context.
pages=sorted(set([2,3,4,5]+changed))
for i in pages:
 if i>5 and not 248<=i<=286:continue
 d[i-1].get_pixmap(matrix=f.Matrix(1,1)).save(V/f'claro-{i:03d}.png')
 n[i-1].get_pixmap(matrix=f.Matrix(1,1)).save(V/f'noturno-{i:03d}.png')
for palette in ['claro','noturno']:
 for start in range(0,len(pages),6):
  im=Image.new('RGB',(1800,1700),'#777');draw=ImageDraw.Draw(im)
  for j,num in enumerate(pages[start:start+6]):
   file=V/f'{palette}-{num:03d}.png'
   if not file.exists():continue
   q=Image.open(file);q.thumbnail((590,820));x=(j%3)*600;y=(j//3)*850;im.paste(q,(x,y+20));draw.text((x,y),str(num),fill='white')
  im.save(V/f'contato-{palette}-{start//6+1:02d}.jpg')
res={'resultado':'aprovado' if all(c['aprovado'] for c in checks) else 'revisar','paginas':len(d),'verificacoes':checks,'paginas_texto_visual_alterado':changed,'paginas_para_revisao':pages}
(V/'VALIDACAO-NAVEGACAO.json').write_text(json.dumps(res,ensure_ascii=False,indent=2)+'\n');print(json.dumps(res,ensure_ascii=False,indent=2))

from pathlib import Path
import json,hashlib
from pypdf import PdfReader
from pypdf.generic import ContentStream
B=Path(__file__).resolve().parent;R=B/'revisao-r55';P=json.loads((B/'PALETA-NOTURNA.json').read_text())
a=PdfReader(B/'output/pdf/Ciclo-Maldito-R55.pdf');path=B/'output/pdf/Ciclo-Maldito-R55-Noturno-Vinho-e-Pessego.pdf';b=PdfReader(path);checks=[]
def check(n,r):
 assert r,n
 checks.append(n)
check('Mesmo número de páginas',len(a.pages)==len(b.pages))
colors={b'rg',b'RG',b'g',b'G',b'k',b'K'}
def core(page,r):return [(v,o) for v,o in ContentStream(page.get_contents(),r).operations if o not in colors]
def annotations(r):
 refs={p.indirect_reference.idnum:i for i,p in enumerate(r.pages)};out=[]
 for pn,p in enumerate(r.pages):
  for obj in p.get('/Annots',[]):
   d=obj.get_object();t=d.get('/Dest');act=d.get('/A')
   if t is None and act:t=act.get('/D')
   if hasattr(t,'get_object'):t=t.get_object()
   target=[refs[t[0].idnum],*map(str,t[1:])] if isinstance(t,list) else str(t)
   out.append((pn,str(d.get('/Subtype')),list(d.get('/Rect',[])),target,str(act.get('/URI')) if act else None))
 return out
for i,(x,y) in enumerate(zip(a.pages,b.pages),1):
 check(f'{i}: texto idêntico',x.extract_text()==y.extract_text())
 check(f'{i}: geometria e operações preservadas',core(x,a)==core(y,b))
 check(f'{i}: formato preservado',list(x.mediabox)==list(y.mediabox))
 xo=x['/Resources'].get('/XObject',{});yo=y['/Resources'].get('/XObject',{})
 check(f'{i}: mesmas imagens',set(xo)==set(yo))
 for name in xo:
  u=xo[name].get_object();v=yo[name].get_object()
  check(f'{i}: pixels originais {name}',hashlib.sha256(u.get_data()).digest()==hashlib.sha256(v.get_data()).digest())
check('Navegação e URLs preservadas',annotations(a)==annotations(b))
def outline(r):
 def walk(items):
  return [walk(x) if isinstance(x,list) else (x.title,r.get_destination_page_number(x)) for x in items]
 return walk(r.outline)
check('Marcadores preservados',outline(a)==outline(b))
def lum(s):
 c=[int(s[i:i+2],16)/255 for i in [1,3,5]]
 c=[v/12.92 if v<=.04045 else ((v+.055)/1.055)**2.4 for v in c]
 return sum(v*w for v,w in zip(c,[.2126,.7152,.0722]))
def contrast(x,y):
 hi,lo=sorted([lum(x),lum(y)],reverse=True);return (hi+.05)/(lo+.05)
roles=['texto','texto_negrito','texto_tabela_cabecalho','texto_secundario','texto_metadados','titulo_secao','titulo_entrada','link']
pairs=[(r,s) for r in roles for s in ['fundo','faixa_tabela']]+[('texto_em_faixa','faixa_vinho')]
values=[{'texto':r,'fundo':s,'contraste':round(contrast(P[r],P[s]),2)} for r,s in pairs]
check('Texto com contraste pelo menos 4,5:1',all(contrast(P[r],P[s])>=4.5 for r,s in pairs))
check('Corpo acima de 7:1',all(contrast(P['texto'],P[s])>=7 for s in ['fundo','faixa_tabela']))
report={'resultado':'aprovado','paginas':len(b.pages),'verificacoes':checks,'sha256_pdf':hashlib.sha256(path.read_bytes()).hexdigest(),'contrastes':values,'limites':'As cores dos objetos vetoriais mudam; as imagens originais são preservadas. Preferência pessoal não é medida por contraste.'}
(R/'VALIDACAO-NOTURNO.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'resultado':'aprovado','paginas':len(b.pages),'verificacoes':len(checks),'contraste_minimo':min(c['contraste'] for c in values)},ensure_ascii=False))

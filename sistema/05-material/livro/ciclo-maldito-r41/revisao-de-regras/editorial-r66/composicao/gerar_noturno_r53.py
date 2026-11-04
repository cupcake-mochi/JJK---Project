"""Aplica a paleta D aprovada ao livro, conservando texto, imagens e geometria."""
from pathlib import Path
from collections import Counter
from pypdf import PdfReader,PdfWriter
from pypdf.generic import ContentStream,FloatObject,NameObject
import hashlib,json
B=Path(__file__).resolve().parent;R=B/'revisao-r53'
P=json.loads((B/'PALETA-NOTURNA.json').read_text())
source=B/'output/pdf/Ciclo-Maldito-R53.pdf';reader=PdfReader(source);writer=PdfWriter();writer.clone_document_from_reader(reader)
roles={'#FFFFFF':('texto_em_faixa','fundo'),'#9E2358':('titulo_secao','linha_destaque'),'#65545F':('texto_secundario','borda'),'#ECC3D6':('titulo_secao','linha'),'#251727':('texto','faixa_vinho'),'#927583':('texto_secundario','borda'),'#522039':('titulo_secao','faixa_vinho'),'#CFB8C2':('titulo_secao','linha_capitulo'),'#000000':('texto','fundo'),'#F2EFF0':('texto','faixa_tabela'),'#D8D1D4':('texto_secundario','linha_tabela'),'#F8F1F4':('texto','faixa_tabela'),'#2C2418':('texto','faixa_vinho'),'#BC2A6E':('link','linha_destaque')}
rgb=lambda code:tuple(int(code[i:i+2],16)/255 for i in [1,3,5])
key=lambda vals:tuple(round(v*255) for v in vals)
lookup={key(rgb(c)):v for c,v in roles.items()};counts=Counter()
def recolor(original,typ,font=None):
 k=key(original);assert k in lookup,(k,typ)
 role=lookup[k][0 if typ=='texto' else 1]
 if typ=='texto' and font:
  if k==(255,255,255):role='texto_em_faixa'
  elif 'IBMPlexMono' in font:role='texto_metadados'
  elif 'BreeSerif' in font:role='titulo_entrada'
  elif 'BarlowCondensed-Bold' in font:role='titulo_secao'
  elif 'BarlowCondensed-SemiBold' in font:role='texto_tabela_cabecalho' if k==(37,23,39) else 'texto_secundario'
  elif 'Spectral-SemiBold' in font:role='link' if k in {(158,35,88),(188,42,110)} else 'texto_negrito'
 counts[(typ,role)]+=1
 return [FloatObject(v) for v in rgb(P[role])]
for pn,page in enumerate(writer.pages,1):
 cs=ContentStream(page.get_contents(),writer);out=[];fill=stroke=(0.,0.,0.);font=None;mode=0;stack=[]
 for args,op in cs.operations:
  if op==b'q':stack.append((fill,stroke,font,mode))
  elif op==b'Q':fill,stroke,font,mode=stack.pop()
  elif op in [b'rg',b'RG',b'g',b'G']:
   val=tuple(float(v) for v in args)
   if op in [b'g',b'G']:val=(val[0],)*3
   if op in [b'rg',b'g']:fill=val
   else:stroke=val
   continue
  elif op in [b'k',b'K',b'cs',b'CS',b'sc',b'SC',b'scn',b'SCN',b'sh']:raise ValueError((pn,op))
  elif op==b'Tr':mode=int(args[0])
  elif op==b'Tf':font=str(page['/Resources']['/Font'][args[0]].get_object().get('/BaseFont'))
  if op in [b'Tj',b'TJ',b"'",b'"']:
   if mode in {0,2}:out.append((recolor(fill,'texto',font),b'rg'))
   if mode==1:out.append((recolor(stroke,'texto',font),b'RG'))
   elif mode==2:out.append((recolor(stroke,'linha'),b'RG'))
   else:assert mode in {0,3},('modo de texto inesperado',pn,mode)
   # Conserva o texto invisível e o contorno dos títulos das capas.
  elif op in [b'f',b'F',b'f*']:out.append((recolor(fill,'superficie'),b'rg'))
  elif op in [b'S',b's']:out.append((recolor(stroke,'linha'),b'RG'))
  elif op in [b'B',b'B*',b'b',b'b*']:
   out.append((recolor(fill,'superficie'),b'rg'));out.append((recolor(stroke,'linha'),b'RG'))
  out.append((args,op))
 assert not stack
 cs.operations=out;page[NameObject('/Contents')]=writer._add_object(cs);page.compress_content_streams()
writer.add_metadata({'/Title':'Ciclo Maldito | R53 | Vinho e pêssego','/Subject':'Versão noturna com texto, imagens, geometria e navegação preservados.'})
path=B/'output/pdf/Ciclo-Maldito-R53-Noturno-Vinho-e-Pessego.pdf';writer.write(path)
report={'pdf':str(path),'paginas':len(writer.pages),'sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'sha256_base':hashlib.sha256(source.read_bytes()).hexdigest(),'paleta':P,'pinturas':[{'tipo':t,'papel':r,'quantidade':v} for (t,r),v in sorted(counts.items())]}
(R/'GERACAO-NOTURNO.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'paginas':len(writer.pages),'bytes':path.stat().st_size},ensure_ascii=False))

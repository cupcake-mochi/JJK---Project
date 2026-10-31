from pathlib import Path
import pymupdf as fitz,json,hashlib
from PIL import Image,ImageDraw
H=Path(__file__).resolve().parent;old=H.parent/'consolidacao-final/composicao/output/pdf';new=H/'composicao/output/pdf';V=H/'revisao';V.mkdir(exist_ok=True)
result={'comparacao':'Texto, posições das palavras e imagem renderizada de todas as páginas frente à R59.','paletas':{},'revisao_visual':'pendente'}
for pal,suffix in [('claro',''),('noturno','-Noturno')]:
 name='Ciclo-Maldito-Livro-de-Regras'+suffix+'.pdf';a=fitz.open(old/name);b=fitz.open(new/name);assert len(a)==len(b)
 changes=[];textchanges=[]
 for i,(x,y) in enumerate(zip(a,b),1):
  if x.get_text()!=y.get_text():textchanges.append(i)
  if x.get_pixmap(matrix=fitz.Matrix(1,1)).samples!=y.get_pixmap(matrix=fitz.Matrix(1,1)).samples:changes.append(i)
 result['paletas'][pal]={'paginas':len(b),'paginas_com_texto_alterado':textchanges,'paginas_com_imagem_alterada':changes,'paginas_visualmente_identicas':len(a)-len(changes)}
 select=sorted({p for n in changes for p in [n-1,n,n+1] if 1<=p<=len(b)});result['paletas'][pal]['paginas_renderizadas_para_revisao']=select
 folder=V/pal;folder.mkdir(exist_ok=True)
 for n in select:b[n-1].get_pixmap(matrix=fitz.Matrix(1.3,1.3),alpha=False).save(folder/f'{n:03d}.png')
 for i in range(0,len(select),6):
  sheet=Image.new('RGB',(1500,1460),'#777777');draw=ImageDraw.Draw(sheet)
  for j,n in enumerate(select[i:i+6]):
   im=Image.open(folder/f'{n:03d}.png');im.thumbnail((490,690));x=(j%3)*500+(500-im.width)//2;y=(j//3)*730+25;sheet.paste(im,(x,y));draw.text((x,y-20),f'{pal} / {n}',fill='white')
  sheet.save(folder/f'contato-{i//6+1:02d}.jpg',quality=90)
 print(pal,changes,flush=True)
(V/'COMPARACAO-R59.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')

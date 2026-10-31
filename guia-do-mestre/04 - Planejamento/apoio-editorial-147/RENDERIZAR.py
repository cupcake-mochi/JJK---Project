"""Renderizar todas as páginas e gerar painéis numerados para inspeção."""
from pathlib import Path
from PIL import Image,ImageDraw
import json,hashlib
import pymupdf
A=Path(__file__).resolve().parent;R=A.parents[1];c=json.loads((A/'composicao.json').read_text());p=R/c['pdf'];d=pymupdf.open(p)
F=A/'revisao/paginas';S=A/'revisao/paineis';F.mkdir(parents=True,exist_ok=True);S.mkdir(parents=True,exist_ok=True)
rows=[]
for start in range(0,len(d),9):
 panel=Image.new('RGB',(1830,2640),'#ddd');draw=ImageDraw.Draw(panel)
 for j,i in enumerate(range(start,min(start+9,len(d)))):
  page=d[i];pix=page.get_pixmap(matrix=pymupdf.Matrix(1.35,1.35),alpha=False);file=F/f'pagina-{i+1:03}.png';pix.save(file)
  im=Image.frombytes('RGB',[pix.width,pix.height],pix.samples);im.thumbnail((595,842));x=(j%3)*610;y=(j//3)*880;panel.paste(im,(x+7,y+24));draw.text((x+10,y+5),f'PÁGINA {i+1}',fill='black')
 panelpath=S/f'painel-{start//9+1:02}.png';panel.save(panelpath)
 rows.append({'painel':panelpath.relative_to(A).as_posix(),'paginas':list(range(start+1,min(start+9,len(d))+1))})
 if start%90==0:print('Páginas renderizadas até',min(start+9,len(d)),flush=True)
(A/'renderizacao.json').write_text(json.dumps({'sha256_pdf':hashlib.sha256(p.read_bytes()).hexdigest(),'paginas':len(d),'painel':rows,'metodo':'Renderização offline das páginas em 97,2 dpi e painéis de nove páginas. Ampliações de página inteira disponíveis para os trechos selecionados.'},ensure_ascii=False,indent=2)+'\n')
print('Renderização concluída:',len(d),'páginas e',len(rows),'painéis.',flush=True)

from pathlib import Path
import json,subprocess
from PIL import Image,ImageOps,ImageDraw
B=Path(__file__).resolve().parents[1];R=B/'revisao-r47';D=R/'prova';D.mkdir(exist_ok=True);pages=json.loads((R/'PAGINAS-PROVA.json').read_text())
for p in pages:subprocess.run(['pdftoppm','-f',str(p),'-l',str(p),'-scale-to','1600','-singlefile','-png',str(B/'output/pdf/Ciclo-Maldito-R47.pdf'),str(D/f'p{p:03}')],check=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
for i in range(0,len(pages),4):
 canvas=Image.new('RGB',(1440,2080),'#dddddd');dr=ImageDraw.Draw(canvas)
 for j,p in enumerate(pages[i:i+4]):
  im=Image.open(D/f'p{p:03}.png');im.thumbnail((700,1000));x=(j%2)*720+10;y=(j//2)*1040+25;canvas.paste(im,(x,y));dr.text((x,y-18),f'R47 - pagina {p}',fill='black')
 canvas.save(D/f'contato-{i//4+1:02}.jpg',quality=92)
print(len(pages),'páginas renderizadas')

from pathlib import Path
from PIL import Image,ImageOps,ImageDraw
import json,sys
B=Path(__file__).resolve().parents[1];R=B/'revisao-r54';P=R/'paginas';O=R/'pranchas';O.mkdir(exist_ok=True)
files=sorted(P.glob('p-*.png'))
for start in range(0,len(files),24):
 canvas=Image.new('RGB',(1440,1420),'#aaa');draw=ImageDraw.Draw(canvas)
 for n,p in enumerate(files[start:start+24]):
  im=Image.open(p).convert('RGB');im.thumbnail((226,318));x=(n%6)*240+7;y=(n//6)*355+25
  canvas.paste(im,(x,y));draw.text((x,y-18),str(start+n+1),fill='black')
 canvas.save(O/f'geral-{start+1:03d}-{min(start+24,len(files)):03d}.jpg',quality=90)
print('pages',len(files),'sheets',(len(files)+23)//24)

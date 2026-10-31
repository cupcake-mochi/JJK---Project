from pathlib import Path
from PIL import Image,ImageDraw
import json
R=Path(__file__).resolve().parent;O=R/'alteradas';O.mkdir(exist_ok=True)
ps=json.loads((R/'PAGINAS-ALTERADAS.json').read_text())['paginas']
for i in range(0,len(ps),2):
 pair=ps[i:i+2];paths=[R/f'paginas/p-{p:03d}.png' for p in pair]
 if not all(p.exists() for p in paths):continue
 out=Image.new('RGB',(1200,875),'#aaa');draw=ImageDraw.Draw(out)
 for n,(p,fn) in enumerate(zip(pair,paths)):
  im=Image.open(fn).convert('RGB');out.paste(im,(n*600,25));draw.text((n*600+20,5),f'Pagina {p}',fill='black')
 out.save(O/f'{i//2+1:02d}.jpg',quality=94)

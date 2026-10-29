from pathlib import Path
from PIL import Image, ImageDraw
import sys
r=Path('/media/mizuki/HD Externo II/Claude/Pesquisa de Campo - Mestragem/04 - Planejamento/apoio-revisao-integral-94/visual-prova-2')
for start in range(int(sys.argv[1]),int(sys.argv[2])+1,4):
 nums=range(start,min(start+4,358));out=Image.new('RGB',(2220,3160),'#ddd');d=ImageDraw.Draw(out)
 for i,n in enumerate(nums):
  im=Image.open(r/f'p-{n:03}.png');x=(i%2)*1110;y=(i//2)*1580;out.paste(im,(x,y+20));d.text((x+8,y+3),f'PÁGINA {n}',fill='black')
 out.save(r/f'grupo-{start:03}.png')

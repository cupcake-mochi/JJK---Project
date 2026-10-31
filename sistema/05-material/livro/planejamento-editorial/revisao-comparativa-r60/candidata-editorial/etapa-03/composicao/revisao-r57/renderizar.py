from pathlib import Path
from PIL import Image,ImageDraw
from concurrent.futures import ThreadPoolExecutor
import subprocess,json,sys
B=Path('/home/mizuki/CHAT-GPT/RPG -JJK/entregas/livro-diagramado-r57');mode=sys.argv[1];R=B/'revisao-r57'/mode;R.mkdir(exist_ok=True)
count=json.loads((B/'FONTES-E-VALIDACAO.json').read_text())['paginas']
name='Ciclo-Maldito-R57.pdf' if mode=='visual-1' else 'Ciclo-Maldito-R57-Noturno-Vinho-e-Pessego.pdf'
def part(start):
 end=min(start+59,count);subprocess.run(['pdftoppm','-f',str(start),'-l',str(end),'-r','72','-jpeg','-jpegopt','quality=88',str(B/'output/pdf'/name),str(R/'p')],check=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
with ThreadPoolExecutor(max_workers=4) as pool:list(pool.map(part,range(1,count+1,60)))
for start in range(1,count+1,8):
 end=min(start+7,count);sheet=Image.new('RGB',(2400,1740),'#aaaaaa');d=ImageDraw.Draw(sheet)
 for i,p in enumerate(range(start,end+1)):
  im=Image.open(R/f'p-{p:03d}.jpg').convert('RGB');im.thumbnail((590,839));x=(i%4)*600;y=(i//4)*870;sheet.paste(im,(x,y+25));d.text((x+10,y+5),str(p),fill='black')
 sheet.save(R/f'prancha-{start:03d}-{end:03d}.jpg',quality=90)
print(mode,count,'páginas renderizadas')

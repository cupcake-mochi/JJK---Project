from pathlib import Path
import sys,subprocess,json,concurrent.futures
from PIL import Image,ImageDraw
B=Path(__file__).resolve().parents[1]; mode=sys.argv[1]; source=B.with_name('livro-diagramado-r47') if mode=='base' else B
m=json.loads((source/'FONTES-E-VALIDACAO.json').read_text()); D=B/'revisao-r48'/mode;D.mkdir(exist_ok=True)
pages=list(range(1,m['paginas']+1))
def render(p):
 path=D/f'p{p:03}.jpg'
 subprocess.run(['pdftoppm','-f',str(p),'-l',str(p),'-scale-to','1200','-singlefile','-jpeg','-jpegopt','quality=88',str(source/m['pdf']),str(path.with_suffix(''))],check=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:list(pool.map(render,pages))
for start in range(0,len(pages),8):
 canvas=Image.new('RGB',(1640,1200),'#dddddd');dr=ImageDraw.Draw(canvas)
 for j,p in enumerate(pages[start:start+8]):
  im=Image.open(D/f'p{p:03}.jpg');im.thumbnail((398,562));x=j%4*410+6;y=j//4*600+25;canvas.paste(im,(x,y));dr.text((x,y-18),f'{mode} p. {p}',fill='black')
 canvas.save(D/f'painel-{start//8+1:02}.jpg',quality=92)
print(mode,len(pages),'páginas renderizadas',flush=True)

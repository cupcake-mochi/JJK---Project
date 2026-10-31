from pathlib import Path
import json,sys,subprocess,concurrent.futures,shutil
from PIL import Image,ImageDraw
B=Path(__file__).resolve().parents[1];R=B/'revisao-r49';tag=sys.argv[1];D=R/tag;D.mkdir(exist_ok=True)
m=json.loads((B/'FONTES-E-VALIDACAO.json').read_text())
for f in ['FONTES-E-VALIDACAO.json','fluxo_continuo.py','gerar_livro.py','GERACAO-R49.log']:shutil.copy2(B/f,D/f)
shutil.copy2(B/m['pdf'],D/'ensaio.pdf')
ps=list(range(1,m['paginas']+1)) if len(sys.argv)<3 else sorted(set(int(x) for x in sys.argv[2].split(',')))
def render(p):
 subprocess.run(['pdftoppm','-f',str(p),'-l',str(p),'-scale-to','1400','-singlefile','-jpeg','-jpegopt','quality=90',str(D/'ensaio.pdf'),str(D/f'p{p:03}')],check=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:list(ex.map(render,ps))
for k in range(0,len(ps),8):
 im=Image.new('RGB',(1640,1200),'#ddd');draw=ImageDraw.Draw(im)
 for j,p in enumerate(ps[k:k+8]):
  sub=Image.open(D/f'p{p:03}.jpg');sub.thumbnail((398,562));x=j%4*410+6;y=j//4*600+25;im.paste(sub,(x,y));draw.text((x,y-18),f'{tag} p. {p}',fill='black')
 im.save(D/f'painel-{k//8+1:02}.jpg',quality=94)
(D/'PAGINAS-RENDERIZADAS.json').write_text(json.dumps(ps));print(tag,len(ps),'páginas renderizadas',flush=True)

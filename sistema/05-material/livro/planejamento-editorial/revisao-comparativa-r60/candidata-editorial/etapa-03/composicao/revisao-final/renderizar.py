from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import subprocess,json,hashlib
from PIL import Image,ImageDraw,ImageFont
B=Path(__file__).resolve().parent;ROOT=B.parent
m=json.loads((ROOT/'FONTES-E-VALIDACAO.json').read_text());pdf=ROOT/m['pdf']
assert hashlib.sha256(pdf.read_bytes()).hexdigest()==m['sha256_pdf']
P=B/'paginas';P.mkdir(exist_ok=True);D=B/'duplas';D.mkdir(exist_ok=True)
def render(n):
 subprocess.run(['pdftoppm','-f',str(n),'-l',str(n),'-singlefile','-r','120','-png',str(pdf),str(P/f'p{n:03}')],check=True,stdout=subprocess.DEVNULL,stderr=subprocess.PIPE)
 return n
with ThreadPoolExecutor(max_workers=6) as ex:
 for i,n in enumerate(ex.map(render,range(1,m['paginas']+1)),1):
  if i%25==0:print(f'{i}/{m["paginas"]} páginas renderizadas',flush=True)
font=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',16)
for n in range(1,m['paginas']+1,2):
 a=Image.open(P/f'p{n:03}.png').convert('RGB');w,h=a.size
 sheet=Image.new('RGB',(2*w+24,h+36),'#e9e5e8');d=ImageDraw.Draw(sheet)
 for j,pn in enumerate([n,n+1]):
  if pn>m['paginas']:continue
  im=Image.open(P/f'p{pn:03}.png');sheet.paste(im,(j*(w+24),30));d.text((j*(w+24)+12,5),f'R34 · Página {pn}',font=font,fill='#522039')
 sheet.save(D/f'p{n:03}-{min(n+1,m["paginas"]):03}.jpg',quality=94)
(B/'RENDERIZACAO.json').write_text(json.dumps({'sha256_pdf':m['sha256_pdf'],'paginas':m['paginas'],'resolucao_dpi':120,'paginas_individuais':'paginas/','duplas_para_inspecao':'duplas/','escala_das_duplas':'Cada página conserva os pixels da imagem individual; as duplas não reduzem a página.'},ensure_ascii=False,indent=2)+'\n')
print('Renderização concluída.',flush=True)

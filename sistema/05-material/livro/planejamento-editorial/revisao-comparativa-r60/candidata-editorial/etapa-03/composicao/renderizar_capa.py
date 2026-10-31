from pathlib import Path
import json,subprocess,concurrent.futures
from PIL import Image,ImageOps,ImageDraw
B=Path(__file__).resolve().parent
m=json.loads((B/'FONTES-E-VALIDACAO.json').read_text());out=B/'output/preview';out.mkdir(exist_ok=True)
coverpages=[a['pagina'] for a in m['capas_e_aberturas']]
nums=sorted(set(coverpages+[2,4,77,383,487,497,498]))
def render(n):
 p=out/f'pagina-{n:03d}'
 subprocess.run(['pdftoppm','-f',str(n),'-l',str(n),'-scale-to','1400','-png','-singlefile',str(B/m['pdf']),str(p)],check=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
 return n
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:list(pool.map(render,nums))
for group in range(4):
 sheet=Image.new('RGB',(1350,1320),'#eee9e4');d=ImageDraw.Draw(sheet)
 for cell,n in enumerate(coverpages[group*6:group*6+6]):
  im=Image.open(out/f'pagina-{n:03d}.png').convert('RGB');im.thumbnail((410,605))
  x=cell%3*450+(450-im.width)//2;y=cell//3*660+25
  sheet.paste(im,(x,y));d.text((cell%3*450+20,cell//3*660+635),f'Página {n}',fill='#221b18')
 sheet.save(out/f'aberturas-{group+1}.jpg',quality=94)
f=json.loads((B/'evidencias/FICHAS-SEPARADAS.json').read_text())
for n in [1,9]:
 subprocess.run(['pdftoppm','-f',str(n),'-l',str(n),'-scale-to','1400','-png','-singlefile',str(B/f['pdf']),str(out/f'caderno-{n:02d}')],check=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
(out/'PAGINAS-R28.json').write_text(json.dumps({'sha256_pdf':m['sha256_pdf'],'paginas_renderizadas':nums,'capas_e_aberturas':m['capas_e_aberturas'],'caderno_paginas':[1,9]},ensure_ascii=False,indent=2)+'\n')
print('Renderizadas',len(nums),'páginas e duas do caderno.')

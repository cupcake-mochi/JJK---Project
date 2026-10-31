import json, subprocess
from pathlib import Path
from PIL import Image,ImageOps,ImageDraw
root=Path(__file__).resolve().parent
pages=json.loads((root/'PAGINAS-PARA-REVISAO.json').read_text())['revisar']
out=root/'revisao-visual'
for p in pages:
    dest=out/f'p{p:03}'
    subprocess.run(['pdftoppm','-f',str(p),'-l',str(p),'-scale-to','1500','-singlefile','-png',str(root.parent/'output/pdf/Ciclo-Maldito-R44.pdf'),str(dest)],check=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
for i in range(0,len(pages),4):
    group=pages[i:i+4]
    sheet=Image.new('RGB',(1800,2580),'#ddd')
    d=ImageDraw.Draw(sheet)
    for j,p in enumerate(group):
        im=Image.open(out/f'p{p:03}.png');im.thumbnail((890,1250))
        x=(j%2)*900;y=(j//2)*1290
        d.text((x+15,y+5),f'Pagina PDF {p}',fill='black')
        sheet.paste(im,(x+(900-im.width)//2,y+25))
    sheet.save(out/f'folha-{i//4+1:02}.jpg',quality=90)
print(len(pages),'paginas renderizadas')

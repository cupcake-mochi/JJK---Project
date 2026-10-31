from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from PIL import Image, ImageDraw, ImageFont
import subprocess,json
R=Path(__file__).resolve().parent;B=R.parent
m=json.loads((B/'FONTES-E-VALIDACAO.json').read_text());total=m['paginas'];out=R/'paginas';out.mkdir(exist_ok=True)
def run(bounds):
    a,z=bounds
    subprocess.run(['pdftoppm','-f',str(a),'-l',str(z),'-r','110','-png',str(B/m['pdf']),str(out/'p')],check=True,stdout=subprocess.DEVNULL,stderr=subprocess.PIPE)
    print(a,z,flush=True)
with ThreadPoolExecutor(max_workers=4) as pool:list(pool.map(run,[(a,min(total,a+99)) for a in range(1,total+1,100)]))
nums=sorted({e['pagina'] for e in m['eventos'] if e.get('tratamento_hierarquia')});pairs=[]
font=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',18)
(R/'duplas').mkdir(exist_ok=True);(R/'painel').mkdir(exist_ok=True)
for i in range(0,len(nums),2):
    ns=nums[i:i+2];ims=[Image.open(out/f'p-{n:03}.png') for n in ns];w,h=ims[0].size
    im=Image.new('RGB',(w*2,h+30),'#eee9ec');d=ImageDraw.Draw(im)
    for col,(n,p) in enumerate(zip(ns,ims)):
        im.paste(p,(col*w,30));d.text((col*w+12,5),f'R35 · página {n}',font=font,fill='#522039')
    path=f'duplas/d-{i//2+1:03}.jpg';im.save(R/path,quality=93);pairs.append({'arquivo':path,'paginas':ns})
(R/'DUPLAS.json').write_text(json.dumps(pairs,ensure_ascii=False,indent=2)+'\n')
panels=[]
for i in range(0,total,12):
    im=Image.new('RGB',(1400,1530),'#eee9ec');d=ImageDraw.Draw(im);ns=list(range(i+1,min(i+13,total+1)))
    for j,n in enumerate(ns):
        p=Image.open(out/f'p-{n:03}.png');p.thumbnail((340,480));x=(j%4)*350;y=(j//4)*510
        im.paste(p,(x,y+25));d.text((x+10,y+3),str(n),font=font,fill='#522039')
    path=f'painel/g-{i//12+1:02}.jpg';im.save(R/path,quality=91);panels.append({'arquivo':path,'paginas':ns})
(R/'PAINEIS.json').write_text(json.dumps(panels,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'paginas':total,'com_titulos_novos':len(nums),'duplas':len(pairs),'paineis':len(panels)}),flush=True)

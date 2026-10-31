from pathlib import Path
from PIL import Image,ImageDraw,ImageFont
import json
B=Path(__file__).resolve().parents[1];R=B/'revisao-r53'
files=sorted((R/'paginas').glob('final-*.png'))
expected=json.loads((B/'FONTES-E-VALIDACAO.json').read_text())['paginas']
assert len(files)==expected,(len(files),expected)
font=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',14)
w=240;h=round(w*297/210);tile_h=h+24
for old in (R/'pranchas').glob('final-*.jpg'):old.unlink()
for start in range(0,len(files),16):
 group=files[start:start+16];rows=(len(group)+3)//4
 out=Image.new('RGB',(4*(w+10)+10,rows*tile_h+10),'#302B30');d=ImageDraw.Draw(out)
 for i,p in enumerate(group):
  x=10+(i%4)*(w+10);y=5+(i//4)*tile_h
  d.text((x,y),str(start+i+1),font=font,fill='#F0C0D5')
  im=Image.open(p).convert('RGB').resize((w,h),Image.Resampling.LANCZOS);out.paste(im,(x,y+19))
 out.save(R/'pranchas'/f'final-{start+1:03d}-{start+len(group):03d}.jpg',quality=94)
print('Pranchas',len(list((R/'pranchas').glob('final-*.jpg'))),'páginas',len(files))

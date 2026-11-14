from pathlib import Path
from PIL import Image,ImageDraw
import json,hashlib,subprocess
B=Path(__file__).resolve().parent;R=B/'revisao-r38';m=json.loads((B/'FONTES-E-VALIDACAO.json').read_text());N=m['paginas']
for name in ['paginas','duplas','visao-geral']:(R/name).mkdir(exist_ok=True)
subprocess.run(['pdftoppm','-r','100','-jpeg','-jpegopt','quality=86',str(B/m['pdf']),str(R/'paginas/p')],check=True)
for n in range(1,N+1,2):
 ims=[Image.open(R/'paginas'/f'p-{p:03}.jpg').convert('RGB') for p in range(n,min(n+2,N+1))];w,h=ims[0].size;out=Image.new('RGB',(w*2+12,h+25),'#ddd')
 for i,im in enumerate(ims):out.paste(im,(i*(w+12),25))
 ImageDraw.Draw(out).text((10,6),f'R38 | paginas {n} e {n+1}',fill='black');out.save(R/'duplas'/f'd-{(n+1)//2:03}.jpg',quality=87)
for n in range(1,N+1,8):
 out=Image.new('RGB',(1600,1172),'#ddd');d=ImageDraw.Draw(out)
 for i,p in enumerate(range(n,min(n+8,N+1))):
  im=Image.open(R/'paginas'/f'p-{p:03}.jpg');im.thumbnail((390,552));x=i%4*400;y=i//4*586;d.text((x+10,y+5),f'R38 | {p}',fill='black');out.paste(im,(x+5,y+24))
 out.save(R/'visao-geral'/f'v-{(n-1)//8+1:02}.jpg',quality=87)
old=json.loads((B.parent/'livro-diagramado-r37/FONTES-E-VALIDACAO.json').read_text())
requested=[5,7,79,82,203,212,214,242,284,321,332,357,24,52,63,70,92,94,97,99,111,117,122,126,128,130,148,162,193,215,217,237,246,250,303,306,317,324,329,335,362,374,377]
rows=[]
for p in requested:
 keys={e['bloco'] for e in old['eventos'] if e['pagina']==p and e['bloco']};dest=sorted({e['pagina'] for e in m['eventos'] if e['bloco'] in keys});rows.append({'pagina_r37':p,'blocos':sorted(keys),'paginas_r38':dest})
(R/'CORRESPONDENCIA-PAGINAS.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
(R/'PROVA-IMAGENS.json').write_text(json.dumps({'sha256_pdf':m['sha256_pdf'],'paginas':N,'imagens':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in (R/'paginas').glob('*.jpg') if int(p.stem[2:])<=N}},indent=2))
print(N,'páginas renderizadas e painéis gerados.')

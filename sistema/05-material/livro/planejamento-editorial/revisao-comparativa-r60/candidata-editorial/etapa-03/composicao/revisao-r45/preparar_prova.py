from pathlib import Path
import json,subprocess,hashlib
from PIL import Image,ImageOps,ImageDraw
B=Path(__file__).resolve().parents[1];R=B/'revisao-r45';P=R/'prova';P.mkdir(exist_ok=True)
m=json.loads((B/'FONTES-E-VALIDACAO.json').read_text());old=json.loads((B.parent/'livro-diagramado-r44/FONTES-E-VALIDACAO.json').read_text())
changed={r['bloco'] for r in json.loads((B/'ALTERACOES-R44-para-R45.json').read_text())}
pages={e['pagina'] for e in m['eventos'] if e['bloco'] in changed}
pages|={p['pagina'] for p in m['paginas_planejadas'] if p['capitulo'] in [0,21]}
# Detectar reflow por assinatura de texto/posição (ignora número da página).
def sigs(man):
 d={}
 for e in man['eventos']:
  if e['bloco'] in changed or e['capitulo'] in [0,21]:continue
  d.setdefault(e['pagina'],[]).append([e['bloco'],e['tipo'],e['texto'],*[round(e[k],2) for k in ['x','y','largura','altura']]])
 return {p:hashlib.sha256(json.dumps(v,sort_keys=True).encode()).hexdigest() for p,v in d.items()}
olds=set(sigs(old).values());new=sigs(m)
reflow=[p for p,h in new.items() if h not in olds];pages|=set(reflow)
pages=sorted(pages);(R/'PAGINAS-PARA-PROVA.json').write_text(json.dumps(dict(paginas=pages,refluxo_detectado=reflow,metodo='Eventos e posições, excluídos número de página e blocos alterados; prova visual separada.'),indent=2))
for p in pages:
 out=P/f'p{p:03}'
 subprocess.run(['pdftoppm','-f',str(p),'-l',str(p),'-scale-to','1400','-png','-singlefile',str(B/m['pdf']),str(out)],check=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
for i in range(0,len(pages),4):
 subset=pages[i:i+4];sheet=Image.new('RGB',(1440,2060),'#dddddd');d=ImageDraw.Draw(sheet)
 for j,p in enumerate(subset):
  im=Image.open(P/f'p{p:03}.png');im.thumbnail((700,990));x=(j%2)*720+10;y=(j//2)*1030+30;sheet.paste(im,(x,y));d.text((x,y-22),f'R45 — página {p}',fill='black')
 sheet.save(P/f'contato-{i//4+1:02}.jpg',quality=90)
print(len(pages),'páginas para inspeção visual:',pages,flush=True)

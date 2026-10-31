from pathlib import Path
import json,re
import pymupdf as f
from PIL import Image,ImageDraw
H=Path(__file__).resolve().parent;B=H/'composicao';O=B/'output/pdf';V=H/'revisao';V.mkdir(exist_ok=True)
m=json.loads((B/'FONTES-E-VALIDACAO.json').read_text());d=f.open(O/'Ciclo-Maldito-Livro-de-Regras.pdf');n=f.open(O/'Ciclo-Maldito-Livro-de-Regras-Noturno.pdf');old=json.loads((H.parent/'etapa-01/composicao/FONTES-E-VALIDACAO.json').read_text());pages=sorted(set(e['pagina'] for e in m['eventos'] if e.get('capitulo')==20));sel=[5]+pages+[pages[-1]+1,pages[-1]+2];checks=[]
def check(name,ok):checks.append({'verificacao':name,'aprovado':bool(ok)})
fields=['pagina','tipo','bloco','texto','x','y','largura','altura'];body=lambda j:[{k:e[k] for k in fields} for e in j['eventos'] if not e['gerado'] and e['capitulo'] in range(1,20)]
check('Texto e posição dos capítulos 1 a 19 preservados em relação à etapa 1',body(m)==body(old))
seq=[]
for r in json.loads((B/'NAVEGACAO-CANDIDATA.json').read_text()):
 a=m['ancoras'][r['destino']];seq.append((a['pagina'],0 if a['x']<290 else 1,-a['y']))
check('Navegação de Fundamento da etapa 1 preserva a ordem da leitura',seq==sorted(seq))
for alias,title in [('consulta-link-conjuracoes','Conjurações no turno'),('consulta-link-bloquear','Bloquear'),('consulta-link-morrendo','Morrendo e socorro')]:
 a=m['ancoras'][alias];check(title+' tem marcador digital na página correta',any(x[1]==title and x[2]==a['pagina'] for x in d.get_toc()))
check('Texto da Consulta rápida igual nas duas paletas',all(d[i-1].get_text()==n[i-1].get_text() for i in pages))
for palette,doc in [('claro',d),('noturno',n)]:
 for num in sel:doc[num-1].get_pixmap(matrix=f.Matrix(1.3,1.3)).save(V/f'{palette}-{num:03d}.png')
 for start in range(0,len(sel),4):
  im=Image.new('RGB',(1600,2200),'#777');draw=ImageDraw.Draw(im)
  for j,num in enumerate(sel[start:start+4]):
   a=Image.open(V/f'{palette}-{num:03d}.png');a.thumbnail((785,1070));x=j%2*800;y=j//2*1100;im.paste(a,(x,y+20));draw.text((x,y),str(num),fill='white')
  im.save(V/f'contato-{palette}-{start//4+1:02d}.jpg')
res={'resultado':'aprovado' if all(x['aprovado'] for x in checks) else 'revisar','paginas':len(d),'paginas_consulta':pages,'verificacoes':checks};(V/'VALIDACAO-ETAPA-02.json').write_text(json.dumps(res,ensure_ascii=False,indent=2)+'\n');print(json.dumps(res,ensure_ascii=False,indent=2))

# Mede, nas páginas que mudaram frente à R63, onde termina o texto de cada coluna e se a última
# linha da coluna é um título (título solto no pé). Faixa do corpo: 9,5% a 89% da altura.
import pymupdf as f,json,sys
from pathlib import Path
H0=Path(__file__).resolve().parent
c=json.load(open(H0/'revisao/COMPARACAO-R63.json'));ch=c['paletas']['claro']['paginas_com_imagem_alterada']
A=f.open(H0.parent/'reacao-r63/composicao/output/pdf/Ciclo-Maldito-Livro-de-Regras.pdf');B=f.open(H0/'composicao/output/pdf/Ciclo-Maldito-Livro-de-Regras.pdf')
def cols(p):
  W,H=p.rect.width,p.rect.height;r={0:[],1:[]}
  for b in p.get_text('dict')['blocks']:
    if b['type']!=0:continue
    for l in b['lines']:
      t=''.join(s['text'] for s in l['spans']).strip()
      if not t or l['bbox'][3]>H*0.89 or l['bbox'][1]<H*0.095:continue
      x=(l['bbox'][0]+l['bbox'][2])/2;r[0 if x<W/2 else 1].append((round(l['bbox'][3]/H,2),round(max(s['size'] for s in l['spans']),1),t[:35]))
  return [sorted(r[k])[-1] if r[k] else (0,0,'') for k in (0,1)]
res=[]
for n in ch:
  a,b=cols(A[n-1]),cols(B[n-1]);fl=[]
  for k in (0,1):
    if b[k][1]>10.8 and b[k][0]>0.75:fl.append(f'titulo no pe c{k}: {b[k][2]!r}')
    if abs(a[k][0]-b[k][0])>0.10:fl.append(f'c{k} {a[k][0]}->{b[k][0]}')
  res.append({'pagina':n,'r63':[x[0] for x in a],'r64':[x[0] for x in b],'sinais':fl})
  if fl:print(n,fl,'| r63',[x[0] for x in a],'r64',[x[0] for x in b])
if len(sys.argv)>1:Path(sys.argv[1]).write_text(json.dumps(res,ensure_ascii=False,indent=1))

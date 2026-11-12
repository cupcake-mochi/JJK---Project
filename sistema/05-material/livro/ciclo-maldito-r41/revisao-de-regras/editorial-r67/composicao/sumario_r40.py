"""Sumário detalhado em colunas de leitura contínua, com destinos compartilhados."""
import json,math
from functools import lru_cache
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle
from xml.sax.saxutils import escape

def construir(n):
 rows=json.loads((n['B']/'revisao-r45/NAVEGACAO.json').read_text())
 S=n['S'];styles={
 'parte':ParagraphStyle('toc-parte',parent=S['body'],fontName='Strong',fontSize=16,leading=19,textColor=n['ACC'],spaceBefore=12,spaceAfter=6),
 'capitulo':ParagraphStyle('toc-capitulo',parent=S['body'],fontName='Entry',fontSize=12,leading=15,spaceBefore=9,spaceAfter=4),
 'caminho':ParagraphStyle('toc-caminho',parent=S['body'],fontName='Bold',spaceBefore=4,spaceAfter=3),
 'secao':ParagraphStyle('toc-secao',parent=S['body'],spaceBefore=0,spaceAfter=3),
 }
 ch={'numero':0,'titulo':'Sumário','key':'sumario','parte':1}
 front=n['newpage'](ch,kind='cover');n['attach_key'](front,'capa');front['cover_title']=None
 items=[];last=None
 for c in n['chapters']:
  if c['parte']!=last:
   last=c['parte'];items.append(('parte',n['order']['partes'][last-1]['titulo'],None,0))
  items.append(('capitulo',f'{c["numero"]}. {c["titulo"]}',c['key'],0))
  items.extend(('caminho' if c['numero']==6 and r['nivel']==2 else 'secao',r['titulo'],r['destino'],r['nivel']-1) for r in rows if r['capitulo']==c['numero'])
 page=None;column=0;y=0;capacity=0;log=[]
 def measure(item):
  typ,txt,key,lv=item;inset=0 if typ not in {'secao','caminho'} else 10+(lv-1)*9
  st=styles[typ];w=n['CW']-inset-(27 if key else 0)
  f=Paragraph(f'<link href="#{key}" color="#251727">{escape(txt)}</link>' if key else escape(txt),st)
  h=f.wrap(w,n['H'])[1]
  return f,h+st.spaceBefore+st.spaceAfter,inset,w
 def fresh():
  nonlocal page,column,y,capacity
  page=n['newpage'](ch,kind='toc');column=0
  if not log:n['attach_key'](page,'sumario')
  part=n['Part']('major','Sumário',generated=True)
  h=n['put'](page,n['Unit']([part]),n['M'],n['TOP'],n['AW'],'uma-coluna')
  y=n['TOP']-h-16;capacity=y
  log.append({'pagina':page['numero'],'entradas':[]})
 fresh()
 # A unidade de consulta do sumário é o capítulo com suas entradas.
 # A parte acompanha o primeiro capítulo; nenhuma fonte ou entrelinha muda.
 groups=[];pending=[]
 for item in items:
  if item[0]=='parte':pending.append(item)
  elif item[0]=='capitulo':groups.append(pending+[item]);pending=[]
  else:groups[-1].append(item)
 assert not pending
 heights=[sum(measure(item)[1] for item in group) for group in groups]
 limit=capacity-n['BOTTOM']
 if max(heights)>limit:
  raise ValueError('Um capítulo do sumário excede uma coluna; revisar sua distribuição antes de gerar.')
 # Escolher o menor número de páginas que comporta capítulos inteiros e,
 # dentro dele, minimizar a diferença de ocupação entre todas as colunas.
 prefix=[0]
 for h in heights:prefix.append(prefix[-1]+h)
 for columns in range(2*math.ceil(prefix[-1]/(2*limit)),2*len(groups)+1,2):
  target=prefix[-1]/columns
  @lru_cache(None)
  def solve(start,left):
   if left==0:return (0,()) if start==len(groups) else (float('inf'),())
   best=(float('inf'),())
   for end in range(start+1,len(groups)-left+2):
    height=prefix[end]-prefix[start]
    if height>limit:break
    cost,tail=solve(end,left-1)
    candidate=((height-target)**2+cost,(end,)+tail)
    if candidate[0]<best[0]:best=candidate
   return best
  score,breaks=solve(0,columns)
  if math.isfinite(score):break
 else:raise ValueError('Não foi possível distribuir o sumário.')
 start=0
 for ci,end in enumerate(breaks):
  if ci and ci%2==0:fresh()
  column=ci%2;y=capacity
  for item in [item for group in groups[start:end] for item in group]:
   f,height,inset,w=measure(item)
   typ,txt,key,lv=item;st=styles[typ];x=n['M']+column*(n['CW']+n['G']);fh=height-st.spaceBefore-st.spaceAfter
   part=n['Part']('index',txt,generated=True);part.toc_target=key
   part.make=lambda width,f=f,st=st:(f,st.spaceBefore,st.spaceAfter)
   n['put'](page,n['Unit']([part]),x+inset,y,w,'duas-colunas')
   if key:page.setdefault('toc_rows',[]).append((key,x+n['CW'],y-st.spaceBefore-fh-4))
   log[-1]['entradas'].append({'titulo':txt,'destino':key,'nivel':lv,'coluna':column,'y':y,'altura':height})
   y-=height
  start=end
 (n['B']/'revisao-r45/SUMARIO-PAGINADO.json').write_text(json.dumps(log,ensure_ascii=False,indent=2)+'\n')

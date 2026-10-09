"""Sumário detalhado em colunas de leitura contínua, com destinos compartilhados."""
import json
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle
from xml.sax.saxutils import escape

def construir(n):
 rows=json.loads((n['B']/'revisao-r40/NAVEGACAO.json').read_text())
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
 page=None;column=0;y=0;capacity=0;floor=0;log=[];active_chapter=None;active_path=None
 def measure(item):
  typ,txt,key,lv=item;inset=0 if typ not in {'secao','caminho'} else 10+(lv-1)*9
  st=styles[typ];w=n['CW']-inset-(27 if key else 0)
  f=Paragraph(f'<link href="#{key}" color="#251727">{escape(txt)}</link>' if key else escape(txt),st)
  h=f.wrap(w,n['H'])[1]
  return f,h+st.spaceBefore+st.spaceAfter,inset,w
 def fresh(start=0):
  nonlocal page,column,y,capacity,floor
  page=n['newpage'](ch,kind='toc');column=0
  if not log:n['attach_key'](page,'sumario')
  title='Sumário' if not log else 'Sumário (continuação)'
  part=n['Part']('major',title,generated=True)
  h=n['put'](page,n['Unit']([part]),n['M'],n['TOP'],n['AW'],'uma-coluna')
  y=n['TOP']-h-16;capacity=y
  remaining=sum(measure(item)[1] for item in items[start:])
  floor=max(n['BOTTOM'],capacity-(remaining/2+35)) if remaining<=2*(capacity-n['BOTTOM'])-70 else n['BOTTOM']
  log.append({'pagina':page['numero'],'entradas':[]})
 fresh()
 for i,item in enumerate(items):
  f,height,inset,w=measure(item)
  # Uma parte/capítulo nunca fica sem ao menos a primeira entrada.
  stop=i+1
  if item[0] in {'parte','capitulo','caminho'}:
   while stop<len(items) and items[stop-1][0] in {'parte','capitulo','caminho'}:stop+=1
   stop=min(stop,len(items))
  needed=sum(measure(x)[1] for x in items[i:stop])
  if y-needed<floor:
   if column==0:column=1;y=capacity
   else:fresh(i)
   if item[0] in {'secao','caminho'} and active_chapter:
    context=active_chapter+((' / '+active_path) if active_path and item[3]>1 else '')+' (continuação)'
    q=n['Part']('small',context,generated=True)
    y-=n['put'](page,n['Unit']([q]),n['M']+column*(n['CW']+n['G']),y,n['CW'],'duas-colunas')+5
  if item[0]=='capitulo':active_chapter=item[1];active_path=None
  elif item[0] in {'secao','caminho'} and item[3]==1 and active_chapter and active_chapter.startswith('6.'):
   active_path=item[1]
  typ,txt,key,lv=item;st=styles[typ];x=n['M']+column*(n['CW']+n['G']);fh=height-st.spaceBefore-st.spaceAfter
  part=n['Part']('index',txt,generated=True);part.toc_target=key
  part.make=lambda width,f=f,st=st:(f,st.spaceBefore,st.spaceAfter)
  n['put'](page,n['Unit']([part]),x+inset,y,w,'duas-colunas')
  if key:page.setdefault('toc_rows',[]).append((key,x+n['CW'],y-st.spaceBefore-fh-4))
  log[-1]['entradas'].append({'titulo':txt,'destino':key,'nivel':lv,'coluna':column,'y':y,'altura':height})
  y-=height
 (n['B']/'revisao-r40/SUMARIO-PAGINADO.json').write_text(json.dumps(log,ensure_ascii=False,indent=2)+'\n')

#!/usr/bin/env python3
"""Diagrama o Guia em A4, com tipografia e medidas da R53. Fontes da edição HTML."""
from pathlib import Path
from dataclasses import dataclass,replace
from xml.sax.saxutils import escape
from urllib.parse import urlsplit,unquote
import argparse,json,re,hashlib,math,copy,unicodedata
from bs4 import BeautifulSoup,NavigableString,Tag
from reportlab import rl_config
rl_config.invariant=1
from reportlab.pdfgen.canvas import Canvas
from reportlab.platypus import Paragraph,Table,TableStyle,Flowable,Preformatted
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.colors import HexColor,white
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from PIL import Image
from MAPAS import Mapa
ap=argparse.ArgumentParser();ap.add_argument('--edicao',type=Path);ap.add_argument('--output',type=Path);opt=ap.parse_args()
B=Path(__file__).absolute().parent;E=opt.edicao or B.parent/'07 - Edicao de Leitura';OUT=opt.output or B/'output/pdf/Ciclo-Maldito-Guia-do-Mestre-Pre-1.0.pdf';OUT.parent.mkdir(parents=True,exist_ok=True)
for name,file in [('Body','Spectral-Regular.ttf'),('Bold','Spectral-SemiBold.ttf'),('Italic','Spectral-Italic.ttf'),('Head','BarlowCondensed-SemiBold.ttf'),('Strong','BarlowCondensed-Bold.ttf'),('Entry','BreeSerif.ttf'),('Meta','IBMPlexMono-Medium.ttf'),('Mono','DejaVuSansMono.ttf')]:pdfmetrics.registerFont(TTFont(name,str(B/'fontes'/file)))
pdfmetrics.registerFontFamily('Body',normal='Body',bold='Bold',italic='Italic',boldItalic='Bold')
W,H=A4;M=19*mm;AW=W-2*M;G=7*mm;CW=(AW-G)/2;TOP=H-23*mm;BOTTOM=33*mm
INK,ACC,PALE,RULE,MUTED=map(HexColor,['#251727','#9e2358','#f8f1f4','#ded4d9','#65545f'])
styles={}
for name,font,size,lead,color,before,after in [('body','Body',10.25,13.2,INK,0,2),('h1','Strong',23,26,ACC,9,8),('h2','Entry',15,18,INK,7,5),('h3','Head',13,16,ACC,5,4),('major','Strong',32,35,ACC,0,10),('note','Body',9.75,12.2,INK,3,6),('cell','Body',9.75,12.5,INK,0,0),('headcell','Head',10.5,12.5,ACC,0,0),('small','Head',9,11,MUTED,0,4),('toc','Body',10.25,14,INK,0,4)]:
 styles[name]=ParagraphStyle(name,fontName=font,fontSize=size,leading=lead,textColor=color,spaceBefore=before,spaceAfter=after,allowWidows=0,allowOrphans=0,splitLongWords=1)
styles['code']=ParagraphStyle('code',fontName='Mono',fontSize=8,leading=11,textColor=INK)
meta=json.loads((E/'mapa-editorial.json').read_text());sections={};chapters=meta['capitulos'];numbers={};targets={};source_titles={}
for ch in chapters:
 soup=BeautifulSoup((E/ch['pagina']).read_text(),'html.parser')
 for idx,sec in enumerate(soup.select('section.consulta'),1):
  k=sec['id'];sections[k]=sec;numbers[k]=(str(int(ch['codigo'][1:])) if ch['codigo'].startswith('C') and ch['codigo'][1:].isdigit() else {'FICHAS':'A','TERMOS':'B','PILOTO':'C','OBRA':'D'}[ch['codigo']])+'.'+str(idx)
  source_titles[k]=sec.h2.get_text(' ',strip=True)
  targets[k]=k
  for h in sec.find_all(attrs={'id':True}):targets[h['id']]=h['id']
PAGEMAP={};LOG=[];pageno_refs=True

def inline(node):
 if isinstance(node,NavigableString):return escape(re.sub(r'⌈(.*?)⌉',r'arredonde para cima (\1)',str(node)).replace('\u00a0',' ').replace('\u2011','-').replace('—','-').replace('–','-').replace('−','-'))
 if not isinstance(node,Tag):return ''
 content=''.join(inline(c) for c in node.children)
 if node.name in ['strong','b']:return '<b>'+content+'</b>'
 if node.name in ['em','i']:return '<i>'+content+'</i>'
 if node.name=='code':return '<b>'+content+'</b>'
 if node.name=='br':return '<br/>'
 if node.name=='a':
  href=node.get('href','');u=urlsplit(href);anchor=unquote(u.fragment)
  if anchor in targets:
   suffix=(' (p. '+str(PAGEMAP.get(anchor,'000'))+')') if pageno_refs else ''
   return '<link href="#'+anchor+'" color="#9e2358">'+content+suffix+'</link>'
  if href.startswith(('https://','http://','mailto:')):return '<link href="'+escape(href,{'"':'&quot;'})+'" color="#9e2358">'+content+'</link>'
  # production references remain traceable in companion source map, never absolute local paths in print.
  return content
 return content

@dataclass
class Item:
 f:object
 before:float=0
 after:float=3
 key:str=None
 kind:str='text'
 source:str=''
 text:str=''
 level:int=0
 original:object=None
 first:bool=True
 last:bool=True

def para(text,kind='body',key=None,source='',level=0):
 st=styles[kind];return Item(Paragraph(text,st),st.spaceBefore,st.spaceAfter,key,kind,source,re.sub('<[^>]+>','',text),level)

def table(node,source):
 rows=[]
 for tr in node.find_all('tr'):
  cs=tr.find_all(['td','th'],recursive=False)
  if cs:rows.append(cs)
 n=max(map(len,rows));assert all(len(r)==n for r in rows),(source,n)
 weights=[]
 for j in range(n):
  lengths=[len(r[j].get_text(' ',strip=True)) for r in rows]
  weights.append(max(7,math.sqrt(sum(lengths)/len(lengths))*2+max(len(w) for r in rows for w in (r[j].get_text(' ',strip=True).split() or ['']))*.35))
 if n==2:
  first=max(.24,min(.48,weights[0]/sum(weights)));fr=[first,1-first]
 else:fr=[x/sum(weights) for x in weights]
 data=[[Paragraph(inline(c),styles['headcell' if i==0 else 'cell']) for c in row] for i,row in enumerate(rows)]
 t=Table(data,colWidths=[AW*x for x in fr],repeatRows=1,hAlign='LEFT',splitByRow=1)
 t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),PALE),('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),6),('RIGHTPADDING',(0,0),(-1,-1),6),('TOPPADDING',(0,0),(-1,-1),4),('BOTTOMPADDING',(0,0),(-1,-1),4),('LINEBELOW',(0,0),(-1,0),.8,ACC),('LINEBELOW',(0,1),(-1,-2),.25,RULE),('LINEBELOW',(0,-1),(-1,-1),.5,ACC)]))
 return Item(t,6,9,None,'table',source,' | '.join(c.get_text(' ',strip=True) for c in rows[0]))

class Illustration(Flowable):
 def __init__(self,path,caption,width=AW,maxheight=220):
  super().__init__();self.path=path;self.width=width;im=Image.open(path);self.iw,self.ih=im.size;self.scale=min(width/self.iw,maxheight/self.ih);self.ww=self.iw*self.scale;self.hh=self.ih*self.scale
  self.caption=Paragraph(caption,styles['small']);self.ch=self.caption.wrap(width,H)[1];self.height=self.hh+8+self.ch
 def wrap(self,w,h):return self.width,self.height
 def draw(self):
  self.canv.drawImage(str(self.path),(self.width-self.ww)/2,self.ch+8,width=self.ww,height=self.hh,mask='auto');self.caption.drawOn(self.canv,0,0)

class Diagram(Flowable):
 def __init__(self,name):super().__init__();self.name=name;self.width=AW;self.height=145 if name!='socorro' else 160
 def wrap(self,w,h):return self.width,self.height
 def draw(self):
  c=self.canv;c.saveState();c.setFillColor(PALE);c.roundRect(0,0,AW,self.height,4,fill=1,stroke=0)
  if self.name=='ciclo':
   title='Dedicação: um saldo por ficha';nodes=[('ABERTURA','28 h novas + saldo válido'),('DURANTE','Use primeiro as horas antigas'),('FECHAMENTO','Só horas novas livres passam')];note='Sete dias administrativos. O trabalho também precisa caber no tempo da história.'
  elif self.name=='socorro':
   title='Socorro: acompanhe duas contas';nodes=[('QUEDA','Registre o máximo e a escolha'),('TRATAMENTO','Some apenas cura válida'),('JANELA','Conte tempo e dano posterior')];note='O tratamento completo encerra Morrendo; janela zero encerra a participação. Integridade a zero tem seu próprio desfecho.'
  else:
   title='Prepare uma situação, conduza escolhas';nodes=[('SITUAÇÃO','Objetivo, pessoas e informação'),('DECISÃO','Intenção, meios e resolução'),('CONSEQUÊNCIA','O que mudou e o que continua')];note='A resposta dos jogadores modifica o preparo. Não é uma sequência obrigatória de ações.'
  c.setFillColor(ACC);c.setFont('Head',16);c.drawString(12,self.height-24,title)
  box=(AW-44)/3
  for i,(head,body) in enumerate(nodes):
   x=12+i*(box+10);c.setFillColor(white);c.roundRect(x,48,box,55,3,fill=1,stroke=0)
   p=Paragraph('<b>'+head+'</b><br/>'+body,styles['note']);h=p.wrap(box-14,80)[1];p.drawOn(c,x+7,99-h)
  p=Paragraph(note,styles['small']);h=p.wrap(AW-24,50)[1];p.drawOn(c,12,12)
  c.restoreState()

# Only reader-directed trimming. All exact changes are logged and the source remains preserved.
def clean_section(sec,k):
 s=BeautifulSoup(str(sec),'html.parser').section
 for node in s.select('p.etiqueta'):node.decompose()
 for p in list(s.find_all('p',recursive=False)):
  text=p.get_text(' ',strip=True)
  if text.startswith(('Base de regras:','Base:','Fontes e alcance:','Referência de regras:','Referência principal:','Verificação realizada:','Revisão numérica do confronto:')):
   LOG.append({'consulta':k,'antes':text,'depois':'Fonte e alcance reunidos no mapa editorial e nas notas desta edição.','motivo':'Retira notas de produção da leitura contínua; mantém a fonte no registro.'});p.decompose()
 if k=='s087':
  p=s.select_one('blockquote p')
  if p:
   old=p.get_text(' ',strip=True)
   p.clear();p.append('Os casos usam referências até o volume 18 e as sinopses oficiais dos episódios 48–55. Para preparar sem revelações, use ')
   a=s.new_tag('a',href='../capitulos/c01.html#s086') if hasattr(s,'new_tag') and callable(s.new_tag) else BeautifulSoup('', 'html.parser').new_tag('a',href='../capitulos/c01.html#s086')
   a.string='A sociedade jujutsu';p.append(a);p.append('.')
   LOG.append({'consulta':k,'antes':old,'depois':p.get_text(' ',strip=True),'motivo':'O aviso de revelações e sua localização cronológica já aparecem na abertura do apêndice; evita repeti-los na seção.'})
 # Update stale title and repeated production-only references without altering content.
 if k=='x001':s.h2.string='As batidas no anexo: missão comentada'
 if k=='x002':s.h2.string='Três maldições para a missão'
 if k=='x003':
  s.h2.string='A entrega trocada'
  p=s.find('p',recursive=False)
  if p and p.get_text().startswith('21 de outubro'):
   old=p.get_text(' ',strip=True);p.string='Situação original de cotidiano. Aplica tarefas, testes, ofícios e reparos do Livro de Regras 1.0; não acrescenta benefícios de treinamento.'
   LOG.append({'consulta':k,'antes':old,'depois':p.string,'motivo':'Substitui a data e a nota de produção pela apresentação do exemplo; conserva seu alcance mecânico.'})
 return s

arts={a['consulta']:a for a in json.loads((B/'revisao/selecao-visual.json').read_text())['selecionadas']}

def section_items(k):
 sec=clean_section(sections[k],k);out=[]
 # source titles are consecutive inside each chapter, original number only in companion map.
 title=sec.h2.get_text(' ',strip=True);out.append(para(numbers[k]+' · '+escape(title),'h1',k,k,1))
 for node in list(sec.children):
  if not isinstance(node,Tag) or node is sec.h2:continue
  if node.name in ['h3','h4','h5','h6']:
   kind='h2' if node.name=='h3' else 'h3';out.append(para(inline(node),kind,node.get('id'),k,2));continue
  if node.name=='p':out.append(para(inline(node),source=k));continue
  if node.name in ['ul','ol']:
   for i,li in enumerate(node.find_all('li',recursive=False),1):
    prefix=(str(i)+'. ') if node.name=='ol' else '• '
    children=[c for c in li.children if not isinstance(c,Tag) or c.name not in ['ul','ol']]
    out.append(para(prefix+''.join(inline(c) for c in children),source=k))
    for nested in li.find_all(['ul','ol'],recursive=False):
     for nj,nli in enumerate(nested.find_all('li',recursive=False),1):out.append(para('    '+('– ' if nested.name=='ul' else str(nj)+'. ')+inline(nli),source=k))
   continue
  if node.name=='blockquote':
   for p in node.find_all(['p','li'],recursive=False):out.append(para(inline(p),'note',source=k))
   continue
  if node.name=='div' and node.find('table'):out.append(table(node.table,k));continue
  if node.name=='table':out.append(table(node,k));continue
  if node.name=='pre':
   raw=node.get_text().replace('—','-').replace('━','-').replace('→','>')
   out.append(Item(Mapa(k,AW),8,12,None,'map',k,raw))
   continue
  if node.name=='hr':continue
  if node.get_text(strip=True):out.append(para(inline(node),source=k))
 # Add one planned image after introduction, before first subsection; all captions contextual.
 if k in arts:
  a=arts[k];cap=a['legenda']+' Gege Akutami / Shueisha - Jujutsu Kaisen, cap. '+str(a['capitulo_manga'])+'.'
  pos=next((i for i,x in enumerate(out[1:],1) if x.kind=='h2'),min(3,len(out)))
  out.insert(pos,Item(Illustration(B/'imagens'/a['arquivo'],cap,maxheight=300 if k=='s087' else 260 if k=='s035' else 220),8,12,None,'image',k,cap))
 if k in ['s001','s022','s039']:
  name={'s001':'preparo','s022':'socorro','s039':'ciclo'}[k];pos=next((i for i,x in enumerate(out[1:],1) if x.kind=='h2'),min(3,len(out)));out.insert(pos,Item(Diagram(name),8,12,None,'diagram',k,name))
 return out

@dataclass
class Placement:
 item:Item
 x:float
 top:float
 w:float
 h:float
@dataclass
class Page:
 chapter:str
 title:str
 items:list
 kind:str='body'

pages=[];current=None;y=TOP;TAIL_WHOLE=False

def newpage(ch,title,kind='body'):
 global current,y
 current=Page(ch,title,[],kind);pages.append(current);y=TOP

def height(item,w):return item.f.wrap(w,H)[1]
def place(item,x,top,w):
 h=height(item,w);current.items.append(Placement(item,x,top,w,h));return h

def fill(items,w,capacity,split=True):
 q=list(items);placed=[];used=0
 while q:
  item=q[0];b=item.before if used else 0;h=height(item,w);needed=b+h+item.after
  if item.kind in ['h1','h2','h3'] and len(q)>1:
   # Keep a heading chain with the complete first paragraph, including its
   # trailing space; reserving only glyph height could orphan the heading.
   follow=0
   for nxt in q[1:]:
    follow+=nxt.before+height(nxt,w)+nxt.after
    if nxt.kind not in ['h1','h2','h3']:break
   if used+needed+follow>capacity+.01:break
  if used+needed<=capacity+.01:
   q.pop(0);placed.append((item,used+b,h));used+=needed;continue
  avail=capacity-used-b-item.after
  if split and item.kind not in ['h1','h2','h3','image','diagram'] and avail>=styles['body'].leading*2:
   bits=item.f.split(w,avail)
   if len(bits)>=2:
    first=replace(item,f=bits[0],original=item.original or item.f,last=False);h=height(first,w)
    if h<=avail+.01:
     placed.append((first,used+b,h));used+=b+h+item.after;q.pop(0)
     q=[replace(item,f=f,key=None,before=0,original=item.original or item.f,first=False,last=item.last and j==len(bits)-2) for j,f in enumerate(bits[1:])]+q
  break
 return placed,q,used

def normal(items,ch,title):
 global y
 q=list(items)
 while q:
  available=y-BOTTOM
  if available<42:newpage(ch,title);continue
  # A shallow band below a full-width element is read across the page.
  # It never creates two tiny columns joined in the middle of a sentence.
  if available<160:
   ps,rest,used=fill(q,AW,available,split=False)
   if not ps:newpage(ch,title);continue
   for item,offset,h in ps:current.items.append(Placement(item,M,y-offset,AW,h))
   y-=used;q=rest
   if q:newpage(ch,title)
   continue
  # Chapter 1 has been reviewed as complete teaching units. Keep its short
  # paragraphs whole even at ordinary column overflow, not just balancing.
  allow_split=not TAIL_WHOLE and ch!='C01'
  left,remain,lh=fill(q,CW,available,split=allow_split);right,rest,rh=fill(remain,CW,available,split=allow_split)
  if not left and not right:
   if abs(y-TOP)<.1:raise ValueError(('unplaceable',q[0].text,available))
   newpage(ch,title);continue
  if not rest:
   # Never split a paragraph merely to make the bottom edges even.
   # Normal full-height overflow may still split a long paragraph naturally.
   lo=0;hi=available;best=(left,right,lh,rh)
   whole_l,whole_rem,whole_lh=fill(q,CW,available,split=False)
   whole_r,whole_rest,whole_rh=fill(whole_rem,CW,available,split=False)
   can_balance=not whole_rest
   if can_balance:best=(whole_l,whole_r,whole_lh,whole_rh)
   for _ in range(14 if can_balance else 0):
    mid=(lo+hi)/2;l,r,lused=fill(q,CW,mid,split=False);rr,remain2,rused=fill(r,CW,mid,split=False)
    if not remain2:hi=mid;best=l,rr,lused,rused
    else:lo=mid
   left,right,lh,rh=best
  for col,ps in enumerate([left,right]):
   x=M+col*(CW+G)
   for item,offset,h in ps:current.items.append(Placement(item,x,y-offset,CW,h))
  y-=max(lh,rh);q=rest
  if q:newpage(ch,title)

def wide(item,ch,title):
 global y
 while True:
  h=height(item,AW);avail=y-BOTTOM-item.before-item.after
  if h<=avail+.01:
   y-=item.before;place(item,M,y,AW);y-=h+item.after;return
  if item.kind=='table' and h>180 and avail>60:
   bits=item.f.split(AW,avail)
   if len(bits)>1 and len(bits[0]._cellvalues)>=3:
    first=replace(item,f=bits[0],original=item.original or item.f,last=False);y-=item.before;place(first,M,y,AW);item=replace(item,f=bits[1],before=0,original=item.original or item.f,first=False);newpage(ch,title);continue
  if abs(y-TOP)<.1:raise ValueError(('wide too tall',item.kind,item.text,h))
  newpage(ch,title)

def lead_height(item):
 h=height(item,AW)
 # A split table must retain its header and two body rows. A fixed allowance
 # may fit the heading but not those rows, orphaning the heading on its page.
 if item.kind=='table' and h>180:
  return sum(item.f._rowHeights[:3])
 return h

def compose_items(items,ch,title):
 global y
 pending=[]
 for item in items:
  if item.kind not in ['table','image','diagram','map']:pending.append(item);continue
  # A heading immediately before a table belongs to the same band.
  held=[]
  while pending and pending[-1].kind in ['h1','h2','h3']:held.insert(0,pending.pop())
  if pending:
   # In the reviewed first chapter, bind a table's trailing heading and
   # sole lead paragraph to the table, even after a longer prose sequence.
   if ch=='C01' and item.kind=='table' and len(pending)>=2 and pending[-1].kind in ['body','note'] and pending[-2].key in ['s086--preparo-preenchido-o-deposito-vai-reabrir','s007--organize-as-sessoes-e-a-continuidade','s009--ligacoes-possiveis']:
    cut=len(pending)-2
    while cut and pending[cut-1].kind in ['h1','h2','h3']:cut-=1
    if cut:
     normal(pending[:cut],ch,title);pending=pending[cut:]
   # Keep an illustrated introduction together; preceding prose finishes first.
   if item.kind in ['image','diagram']:
    heads=[i for i,a in enumerate(pending) if a.kind=='h1']
    if heads:
     cut=heads[-1]
     if cut:normal(pending[:cut],ch,title)
     pending=pending[cut:]
     hs=[height(a,CW)+a.before+a.after for a in pending[1:]]
     band=min((max(sum(hs[:j]),sum(hs[j:])) for j in range(len(hs)+1)),default=0)
     if ch=='C01' and len(pending)==2 and pending[1].kind in ['body','note'] and height(pending[1],AW)+pending[1].before+pending[1].after<=140:
      band=height(pending[1],AW)+pending[1].before+pending[1].after
     need=height(pending[0],AW)+pending[0].before+pending[0].after+band+item.before+height(item,AW)+item.after
     if need<=TOP-BOTTOM and need>y-BOTTOM:newpage(ch,title)
     wide(pending.pop(0),ch,title)
   # A short heading and its sole lead paragraph use the figure/table width.
   shortlead=(pending and pending[-1].kind in ['body','note'] and
              all(a.kind in ['h1','h2','h3'] for a in pending[:-1]) and
              sum(height(a,AW)+a.before+a.after for a in pending)<=140)
   if shortlead:
    need=sum(height(a,AW)+a.before+a.after for a in pending)+lead_height(item)+item.before+item.after
    if need>y-BOTTOM:newpage(ch,title)
    for a in pending:wide(a,ch,title)
   elif pending:normal(pending,ch,title)
   pending=[]
  if held:
   need=sum(height(a,AW)+a.before+a.after for a in held)+lead_height(item)+item.before+item.after
   if y-BOTTOM<need:newpage(ch,title)
   for a in held:wide(a,ch,title)
  wide(item,ch,title)
 if pending:normal(pending,ch,title)

def rebalance_tail(ch,title,start_index):
 global pages,current,y,BOTTOM,TAIL_WHOLE
 if len(pages)-start_index<3:return
 base=BOTTOM
 last=pages[-1]
 area=sum(v.w*v.h for v in last.items)/(AW*(TOP-base))
 if area>=.45:return
 saved=list(pages[-2:]);prefix=list(pages[:-2]);raw=[v.item for pp in saved for v in pp.items];seq=[]
 # Reunite original paragraph pieces when all pieces lie inside this tail.
 i=0
 while i<len(raw):
  a=raw[i];j=i+1
  if a.original is not None and a.first:
   while j<len(raw) and raw[j].original is a.original:j+=1
   if raw[j-1].last:a=replace(a,f=a.original,original=None,first=True,last=True)
   else:j=i+1
  seq.append(a);i=j
 TAIL_WHOLE=True
 # First try to close the chapter on one page. Balancing two pages before
 # this test can preserve an avoidable near-empty ending.
 original_y=y
 pages=list(prefix);BOTTOM=base;newpage(ch,title)
 try:compose_items(seq,ch,title)
 except ValueError:pass
 else:
  if len(pages)-len(prefix)==1:
   TAIL_WHOLE=False;return
 pages=prefix+saved;current=pages[-1];y=original_y
 best=saved;best_y=y;lo=base;hi=TOP-220
 for _ in range(9):
  mid=(lo+hi)/2;pages=list(prefix);BOTTOM=mid;newpage(ch,title)
  try:compose_items(seq,ch,title)
  except ValueError:hi=mid;continue
  candidate=pages[len(prefix):]
  if len(candidate)<=2:best=candidate;best_y=y;lo=mid
  else:hi=mid
 BOTTOM=base;TAIL_WHOLE=False;pages=prefix+best;current=pages[-1];y=best_y

def front_items():
 return [
  para('Como usar este livro','major','inicio'),
  para('Pré-1.0 · edição de leitura · 28 de outubro de 2026','small'),
  para('Este livro ensina você a mestrar Ciclo Maldito: preparar uma missão, apresentar o mundo e acompanhar as escolhas dos jogadores. O sistema foi pensado principalmente para guildas, onde vários mestres e personagens compartilham a mesma história. Você também pode usar estas orientações numa campanha fechada.'),
  para('Não é preciso conhecer Jujutsu Kaisen. O primeiro capítulo apresenta o mundo e a vida de um feiticeiro. Se você já conhece a obra, pode seguir para os acordos do grupo. O apêndice D traz exemplos com revelações da trama; sua leitura é opcional.'),
  para('Como funciona uma sessão','h2'),
  para('Você descreve a situação e o que os personagens percebem. Os jogadores dizem o que querem fazer. Se o resultado for incerto e a falha fizer diferença, consulte a regra no Livro de Regras 1.0. Num teste comum, role um dado de vinte faces (d20) e some o bônus indicado. O teste tem sucesso se alcançar ou superar a Classe de Dificuldade (CD). Ataques e testes de resistência (TRs) seguem suas próprias regras.'),
  para('Depois, descreva o resultado e dê espaço à próxima escolha. Nem tudo exige dados: uma conversa pode resolver um problema. Num combate, use os turnos e as ações de cada participante. Consulte a ficha para saber quais capacidades, equipamentos e recursos cada personagem possui, como pontos de vida (PV) e pontos de energia (PE).'),
  para('Por onde começar','h2'),
  para('Para sua primeira missão, leia <link href="#s007" color="#9e2358">A sessão zero</link>, <link href="#s001" color="#9e2358">Preparar uma missão</link> e <link href="#s004" color="#9e2358">Conduzir uma sessão</link>. Depois, acompanhe <link href="#x001" color="#9e2358">As batidas no anexo</link>, no apêndice C. Durante o jogo, as fichas do apêndice A ajudam a consultar e anotar o que importa.'),
  para('Regras, dicas e exemplos','h2'),
  para('<b>Regras do jogo.</b> Estão no Livro de Regras 1.0. Este Guia mostra como usá-las em situações de jogo e onde consultá-las.<br/><b>Dicas para o mestre.</b> Ajudam a preparar e conduzir a sessão. Adapte-as ao seu grupo e avise quando uma mudança afetar os jogadores.<br/><b>Exemplos experimentais.</b> São inimigos, perigos e outras criações que ainda precisam ser avaliados em jogo. Seus avisos indicam o que está sendo proposto. Os exemplos não são regras obrigatórias para toda a guilda.'),
  para('Encontre o que precisa','h2'),
  para('O sumário, as referências e os botões no rodapé são clicáveis. As páginas indicadas levam a trechos deste PDF. O Livro de Regras 1.0 é um volume separado. Use o índice para procurar um assunto e leia os exemplos conforme sua necessidade.')]

def build():
 global pages,current,y,LOG
 pages=[];LOG=[]
 newpage('CAPA','Ciclo Maldito','cover')
 newpage('INÍCIO','Como usar este livro');compose_items(front_items(),'INÍCIO','Como usar este livro')
 newpage('SUMÁRIO','Sumário');toc=[para('Sumário','major','sumario')]
 for ch in chapters:
  label=(str(int(ch['codigo'][1:])) if ch['codigo'].startswith('C') and ch['codigo'][1:].isdigit() else {'FICHAS':'A','TERMOS':'B','PILOTO':'C','OBRA':'D'}[ch['codigo']])
  title=ch['titulo'].replace('—','-');key='ch-'+ch['codigo'];p=str(PAGEMAP.get(key,'000'))
  toc.append(para('<b><link href="#'+key+'" color="#9e2358">'+label+' · '+escape(title)+' · '+p+'</link></b>','h3'))
  text=' · '.join(escape(source_titles[k]) for k in ch['consultas'])
  # The chapter opening and index provide the complete section-level list.
  summaries={'C01':'Contexto, cotidiano e acordos do grupo.','C02':'Situações, investigação, facções e continuidade.','C03':'Testes, informação, espaço e improvisação.','C04':'Recursos, quedas, socorro e recuperação.','C05':'Criação, comparação e condução de ameaças.','C06':'Fichas, vínculos, Origens e cuidados.','C07':'Avaliação, montagem e poderes avançados.','C08':'Dedicação, projetos, equipamento e recompensas.','C09':'Trocas, aquisição e continuidade de entidades.','C10':'Ferramentas de registro e retomada.','FICHAS':'Folhas prontas para consultar e preencher.','TERMOS':'Vocabulário do mundo sem revelações.','PILOTO':'A entrega trocada, As batidas no anexo e fichas.','OBRA':'Aprofundamento opcional com revelações.'}
  toc.append(para(summaries[ch['codigo']],'small'))
 toc.append(para('<link href="#indice" color="#9e2358">Índice de assuntos</link> · '+str(PAGEMAP.get('indice','000')),'h3'))
 toc.append(para('<link href="#creditos" color="#9e2358">Créditos e notas da edição</link> · '+str(PAGEMAP.get('creditos','000')),'h3'));compose_items(toc,'SUMÁRIO','Sumário')
 for ch in chapters:
  code=ch['codigo'];title=ch['titulo'];chapter_start=len(pages);newpage(code,title)
  label=('CAPÍTULO '+str(int(code[1:]))) if code.startswith('C') and code[1:].isdigit() else 'APÊNDICE '+{'FICHAS':'A','TERMOS':'B','PILOTO':'C','OBRA':'D'}[code]
  head=[para(label,'small'),para(escape(title),'major','ch-'+code)]
  if code=='OBRA':head.append(para('<b>REVELAÇÕES IMPORTANTES.</b> Os casos a seguir discutem acontecimentos posteriores a Shibuya e o Jogo do Abate. Esta leitura é opcional; as orientações do Guia não exigem conhecer esses desfechos.','note'))
  desc=BeautifulSoup((E/ch['pagina']).read_text(),'html.parser').select_one('p.abertura').get_text()
  if code!='OBRA':head.append(para(escape(desc)))
  head.append(para('Neste capítulo: '+ ' · '.join('<link href="#'+k+'" color="#9e2358">'+numbers[k]+' '+escape(source_titles[k])+'</link>' for k in ch['consultas']),'small'))
  for item in head:wide(item,code,title)
  y-=9
  allitems=[]
  for k in ch['consultas']:allitems.extend(section_items(k))
  compose_items(allitems,code,title)
  rebalance_tail(code,title,chapter_start)
 newpage('ÍNDICE','Índice de assuntos');index=[para('Índice de assuntos','major','indice')]
 for k in sorted(sections,key=lambda k:unicodedata.normalize('NFKD',source_titles[k]).encode('ascii','ignore').decode().casefold()):
  index.append(para('<link href="#'+k+'" color="#9e2358">'+escape(source_titles[k])+'</link> · '+numbers[k]+' · '+str(PAGEMAP.get(k,'000')),'toc'))
 compose_items(index,'ÍNDICE','Índice de assuntos')
 newpage('NOTAS','Créditos e notas da edição');notes=[para('Créditos e notas da edição','major','creditos'),para('<b>Ciclo Maldito | Guia do Mestre</b><br/>Criação e coordenação: Mizuki_sama. Pré-1.0, 2026.'),para('Referência de regras','h2'),para('Ciclo Maldito — Livro de Regras 1.0. Este Guia distingue as regras do jogo, as orientações para a campanha e os exemplos experimentais. Os inimigos novos usam fichas próprias, preparadas a partir do livro de regras; seus números não vêm do Bestiário antigo.'),para('Obra e imagens','h2'),para('Ciclo Maldito é um RPG de fãs inspirado em Jujutsu Kaisen. É uma publicação independente. JUJUTSU KAISEN © 2018 by Gege Akutami / SHUEISHA Inc. Os quadros usados provêm do acervo do Livro de Regras 1.0; seus capítulos aparecem nas legendas. Não há autorização de reprodução registrada. Os créditos identificam a autoria e não constituem licença de reutilização.'),para('A base visual da capa foi fornecida por Mizuki_sama para o Livro de Regras 1.0. Esta edição aplica identificação própria em composição vetorial. Esquemas de consulta foram produzidos para o Guia e não representam páginas da obra.'),para('Tipografia e formato','h2'),para('Spectral (The Spectral Project Authors), Barlow Condensed (The Barlow Project Authors), Bree Serif e IBM Plex Mono. Fontes de licença aberta, conforme os arquivos que acompanham o projeto. Página A4, margens de 19 mm, duas colunas com intervalo de 7 mm. Texto principal: Spectral 10,25 pt, entrelinha 13,2 pt, conforme o formato do Livro de Regras 1.0.'),para('Alcance desta edição','h2'),para('A revisão simplifica a linguagem, organiza os títulos e confere as referências. As notas de pesquisa e produção ficam no acervo que acompanha o livro; os exemplos conservam suas hipóteses e limitações. O relatório de revisão identifica as conferências de texto e os controles de diagramação.'),para('Treinamentos específicos, atualização integral do Bestiário e uma eventual escala geral de dificuldade continuam sendo trabalhos próprios. Esta pré-1.0 recebe observações de leitores e de mesa antes de uma candidata à 1.0.'),para('Fontes e continuidade','h2'),para('O mapa editorial relaciona cada seção ao manuscrito numerado, ao histórico e às referências usadas. O texto editável e os registros permanecem nas pastas de redação e planejamento do projeto. Ao relatar uma dúvida, indique a página, o título, a passagem e a situação em que tentou usá-la.')]
 compose_items(notes,'NOTAS','Créditos e notas da edição')
 result={}
 for n,p in enumerate(pages,1):
  for v in p.items:
   if v.item.key:
    if v.item.key in result:raise ValueError(('duplicate',v.item.key))
    result[v.item.key]=n
 return result

# Page numbers in references affect wrapping. Iterate until all destinations stabilize.
for attempt in range(7):
 newmap=build();print('pass',attempt+1,'pages',len(pages),'anchors',len(newmap),flush=True)
 if newmap==PAGEMAP:break
 PAGEMAP=newmap
else:raise RuntimeError('Pagination did not converge')

c=Canvas(str(OUT),pagesize=A4,pageCompression=1,invariant=1);c.setTitle('Ciclo Maldito - Guia do Mestre - pré-1.0');c.setAuthor('Mizuki_sama');c.setSubject('Guia de preparação, condução e continuidade de mesas; referência Livro de Regras 1.0')
geometry=[];drawlog=[]
for num,p in enumerate(pages,1):
 if p.kind=='cover':
  c.drawImage(str(B/'imagens/capa-base.png'),0,0,width=W,height=H)
  # Existing chapter-cover asset: no bitmap edits. Cover labels are vector type.
  c.setFillColor(HexColor('#2c2418'));c.setFont('Bold',29)
  letters='CICLO MALDITO';yy=H-110
  for ch in letters:
   if ch==' ':yy-=15;continue
   c.drawCentredString(W*174/1024,yy,ch);yy-=38
  c.setFont('Head',12);c.drawCentredString(W*174/1024,H*0.279,'GUIA DO MESTRE')
  # The base artwork carries the rulebook's old version. A vector edition
  # label covers it without changing the supplied bitmap.
  c.setFillColor(HexColor('#352c25'));c.roundRect(W*.715,H*.045,W*.175,H*.060,5,fill=1,stroke=0)
  c.setFillColor(HexColor('#ded0b7'));c.setFont('Head',16)
  c.drawCentredString(W*.8025,H*.071,'PRÉ-1.0')
  c.setFont('Head',7);c.drawCentredString(W*.8025,H*.056,'EDIÇÃO DE LEITURA')
  c.showPage();continue
 c.setFillColor(ACC);c.setFont('Head',8.5);c.drawString(M,H-34,'CICLO MALDITO / GUIA DO MESTRE')
 short=p.title.upper()
 while pdfmetrics.stringWidth(short,'Head',8.5)>AW*.54:short=short[:-2]
 if short!=p.title.upper():short=short.rstrip()+'…'
 c.setFillColor(MUTED);c.drawRightString(W-M,H-34,short);c.setStrokeColor(RULE);c.setLineWidth(.5);c.line(M,H-42,W-M,H-42)
 for v in p.items:
  it=v.item
  if it.key:
   c.bookmarkHorizontalAbsolute(it.key,v.top)
   if it.key.startswith('ch-') or it.key in ['inicio','sumario','indice','creditos']:c.addOutlineEntry(it.text,it.key,0,False)
   elif re.fullmatch(r'[sx]\d{3}',it.key):c.addOutlineEntry(it.text,it.key,1,True)
  actual=it.f.wrap(v.w,H)[1]
  if abs(actual-v.h)>.1:raise ValueError(('changed geometry',num,it.text,actual,v.h))
  it.f.drawOn(c,v.x,v.top-v.h)
  if it.kind=='h2':c.setStrokeColor(ACC);c.setLineWidth(.65);c.line(v.x,v.top-v.h-1,v.x+35,v.top-v.h-1)
  geometry.append({'pagina':num,'tipo':it.kind,'consulta':it.source,'ancora':it.key,'x':round(v.x,2),'y_top':round(v.top,2),'largura':round(v.w,2),'altura':round(v.h,2),'texto':it.text[:120]})
 nav=[('Sumário','sumario'),('Capítulo','ch-'+p.chapter if 'ch-'+p.chapter in PAGEMAP else 'inicio'),('Fichas','ch-FICHAS'),('Índice','indice')]
 nw=AW/len(nav);ny=61
 for i,(label,dest) in enumerate(nav):
  x=M+i*nw;c.setStrokeColor(MUTED);c.setLineWidth(.4);c.rect(x,ny,nw,17,stroke=1,fill=0);c.setFillColor(MUTED);c.setFont('Head',9);c.drawCentredString(x+nw/2,ny+5,label);c.linkRect('',dest,(x,ny,x+nw,ny+17),relative=0,thickness=0)
 c.setFont('Head',8.5);c.setFillColor(MUTED);c.drawString(M,34,'PRÉ-1.0 · EDIÇÃO DE LEITURA');c.setFillColor(ACC);c.drawRightString(W-M,34,str(num));c.showPage()
c.save()
report={'paginas':len(pages),'ancoras':PAGEMAP,'secoes':{k:{'numero':numbers[k],'titulo':source_titles[k],'pagina':PAGEMAP[k]} for k in sections},'capitulos':[{'codigo':ch['codigo'],'titulo':ch['titulo'],'pagina':PAGEMAP['ch-'+ch['codigo']]} for ch in chapters],'fontes':meta['fontes'],'geometria':geometry,'notas_transferidas':LOG,'sha256_pdf':hashlib.sha256(OUT.read_bytes()).hexdigest(),'medidas':{'pagina':'A4','margem_mm':19,'intervalo_colunas_mm':7,'corpo_pt':10.25,'entrelinha_pt':13.2},'sem_teste_de_mesa':True}
(B/'revisao/composicao.json').write_text(json.dumps(report,ensure_ascii=False,indent=2))
print(OUT,OUT.stat().st_size)

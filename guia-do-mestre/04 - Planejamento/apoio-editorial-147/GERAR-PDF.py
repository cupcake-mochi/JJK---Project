"""Compor as 99 fontes revistas, com tipografia do Livro de Regras 1.0."""
from pathlib import Path
from dataclasses import dataclass,replace
from xml.sax.saxutils import escape
from urllib.parse import urlsplit,unquote
from io import BytesIO
import ast,json,re,hashlib,math,copy,unicodedata
from bs4 import BeautifulSoup,NavigableString,Tag,Comment
from reportlab import rl_config
rl_config.invariant=1
from reportlab.pdfgen.canvas import Canvas
from reportlab.platypus import Paragraph,Table,TableStyle,Flowable,Preformatted,Spacer
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.colors import HexColor,white
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.graphics import renderPDF
from svglib.svglib import svg2rlg
from PIL import Image
A=Path(__file__).resolve().parent;R=A.parents[1];B=R/'08 - Diagramacao do Guia';E=R/'07 - Edicao de Leitura/edicao-integrada-136'
OUT=B/'output/pdf/Ciclo-Maldito-Guia-do-Mestre-Pre-1.0-Editorial.pdf'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
for name,file in [('Body','Spectral-Regular.ttf'),('Bold','Spectral-SemiBold.ttf'),('Italic','Spectral-Italic.ttf'),('Head','BarlowCondensed-SemiBold.ttf'),('Strong','BarlowCondensed-Bold.ttf'),('Entry','BreeSerif.ttf'),('Meta','IBMPlexMono-Medium.ttf'),('Mono','DejaVuSansMono.ttf')]:pdfmetrics.registerFont(TTFont(name,str(B/'fontes'/file)))
pdfmetrics.registerFontFamily('Body',normal='Body',bold='Bold',italic='Italic',boldItalic='Bold')
W,H=A4;M=19*mm;AW=W-2*M;G=7*mm;CW=(AW-G)/2;TOP=H-23*mm;BOTTOM=33*mm
INK,ACC,PALE,RULE,MUTED=map(HexColor,['#251727','#9e2358','#f8f1f4','#ded4d9','#65545f'])
styles={}
for name,font,size,lead,color,before,after in [('body','Body',10.25,13.2,INK,0,3),('h1','Strong',23,26,ACC,10,8),('h2','Entry',15,18,INK,7,5),('h3','Head',13,16,ACC,5,4),('major','Strong',30,33,ACC,0,10),('note','Body',9.75,12.2,INK,3,6),('cell','Body',9.75,12.5,INK,0,0),('headcell','Head',10.5,12.5,ACC,0,0),('small','Head',9,11,MUTED,0,4),('toc','Body',10.25,14,INK,0,4)]:
 styles[name]=ParagraphStyle(name,fontName=font,fontSize=size,leading=lead,textColor=color,spaceBefore=before,spaceAfter=after,allowWidows=0,allowOrphans=0,splitLongWords=1)
for kind in ['decision','speech','technical']:
 styles[kind]=ParagraphStyle(kind,parent=styles['body'],leftIndent=7,rightIndent=4,spaceBefore=5,spaceAfter=6,backColor=PALE if kind!='speech' else None,borderPadding=2 if kind!='speech' else 0)
styles['code']=ParagraphStyle('code',fontName='Mono',fontSize=8,leading=11,textColor=INK)
# Reutilizar as medidas e o motor revisto, sem executar o antigo livro.
old=ast.parse((A/'base-GERAR-PDF.py').read_text());wanted={'Item','para','Illustration','Placement','Page','newpage','height','place','fill','normal','wide','lead_height','compose_items','rebalance_tail'}
for node in old.body:
 if isinstance(node,(ast.ClassDef,ast.FunctionDef)) and node.name in wanted:
  code=ast.get_source_segment((A/'base-GERAR-PDF.py').read_text(),node)
  if isinstance(node,ast.ClassDef) and node.decorator_list:code='@dataclass\n'+code
  if node.name=='fill':code=code.replace("if split and item.kind not in ['h1','h2','h3','image','diagram'] and avail>=styles['body'].leading*2:","if split and item.kind not in ['h1','h2','h3','image','diagram'] and h>(TOP-BOTTOM)*.85 and avail>=styles['body'].leading*3:")
  if node.name=='rebalance_tail':code=code.replace('if len(pages)-start_index<3:return','if len(pages)-start_index<2:return')
  if node.name=='compose_items':code=code.replace("pending[-1].kind in ['h1','h2','h3']","pending[-1].kind in ['h1','h2','h3','anchor']")
  exec(compile(code,str(A/'base-GERAR-PDF.py'),'exec'))
meta=json.loads((A/'fontes-para-compor.json').read_text());records=meta['ordem']
for r in records:assert sha(R/r['fonte'])==r['sha256'],r['fonte']
core=[r for r in records if r['pagina'].startswith('capitulo-')]
front=next(r for r in records if r['pagina']=='como-usar.html')
leaves=[r for r in records if r['parte']=='Apêndice A']
priority=['folhas.html','consulta-A1-preparar-a-missao.html','consulta-A1-exemplo-despedida.html','consulta-A2-conduzir-a-sessao.html','consulta-A4-retomar-a-missao.html','consulta-A4-exemplo-sala-de-conservacao.html']
leaves.sort(key=lambda r: priority.index(r['pagina']) if r['pagina'] in priority else len(priority)+records.index(r))
caseindex=next(r for r in records if r['pagina']=='casos.html')
cases=[r for r in records if r['parte']=='Apêndice B' and r!=caseindex]
C=next(r for r in records if r['pagina']=='apendice-c.html');D=next(r for r in records if r['pagina']=='apendice-d.html');refs=next(r for r in records if r['pagina']=='referencias.html')
order=[front]+core+leaves+[caseindex]+cases+[C,D,refs]
assert len(order)==98 and len({r['pagina'] for r in order})==98
DOCS={};ALIASES={};BOOKS={};DOC='';PAGEMAP={};EXTERNAL=[];FIGURES=[];SOURCE_LOG=[]
for i,r in enumerate(order):
 r['key']='d'+str(i).zfill(3);s=BeautifulSoup((E/r['pagina']).read_text(),'html.parser').article
 for nav in s.find_all('nav'):nav.decompose()
 DOCS[r['pagina']]=s;BOOKS[r['pagina']]=r['key']
 for tag in s.find_all(id=True):ALIASES[(r['pagina'],tag['id'])]=r['key'] if tag.name=='h1' else r['key']+'--'+tag['id']
ALIASES[('capitulo-03.html','ideias')]=BOOKS['capitulo-03.html']+'--ideias'
def normalized(s):return s.replace('\u00a0',' ').replace('\u2011','-').replace('—','-').replace('–','-').replace('−','-')
def inline(node):
 if isinstance(node,Comment):return ''
 if isinstance(node,NavigableString):return escape(normalized(str(node)))
 if not isinstance(node,Tag):return ''
 content=''.join(inline(c) for c in node.children)
 if node.name in ['strong','b']:return '<b>'+content+'</b>'
 if node.name in ['em','i']:return '<i>'+content+'</i>'
 if node.name=='code':return '<b>'+content+'</b>'
 if node.name=='br':return '<br/>'
 if node.name in ['sup','sub']:return '<'+node.name+'>'+content+'</'+node.name+'>'
 if node.name=='a':
  u=urlsplit(node.get('href',''));fragment=unquote(u.fragment)
  if u.scheme in ['https','http','mailto']:return '<link href="'+escape(node['href'],{'"':'&quot;'})+'" color="#9e2358">'+content+'</link>'
  target=Path(unquote(u.path)).name if u.path else DOC
  if target not in BOOKS:raise ValueError(('Destino sem documento',DOC,node.get('href')))
  key=ALIASES[(target,fragment)] if fragment else BOOKS[target]
  suffix=' (p. '+str(PAGEMAP.get(key,'000'))+')'
  return '<link href="#'+key+'" color="#9e2358">'+content+suffix+'</link>'
 return content
class Vector(Flowable):
 def __init__(self,path):
  super().__init__();raw=path.read_text().replace('Spectral','Body').replace('Barlow Condensed','Head').replace('BarlowCondensed','Head').replace('Bree Serif','Entry')
  self.drawing=svg2rlg(BytesIO(raw.encode()));self.width=AW;self.scale=min(AW/self.drawing.width,390/self.drawing.height);self.height=self.drawing.height*self.scale
 def wrap(self,w,h):return self.width,self.height
 def draw(self):
  self.canv.saveState();self.canv.translate((AW-self.drawing.width*self.scale)/2,0);self.canv.scale(self.scale,self.scale);renderPDF.draw(self.drawing,self.canv,0,0);self.canv.restoreState()
def table(node,source):
 rows=[tr.find_all(['td','th'],recursive=False) for tr in node.find_all('tr')];rows=[x for x in rows if x];n=max(map(len,rows));assert all(len(x)==n for x in rows)
 weights=[]
 for j in range(n):
  values=[r[j].get_text(' ',strip=True) for r in rows];weights.append(max(7,math.sqrt(sum(map(len,values))/len(values))*2+max(len(w) for s in values for w in (s.split() or ['']))*.35))
 if n==2:
  first=max(.24,min(.46,weights[0]/sum(weights)));fractions=[first,1-first]
 else:fractions=[x/sum(weights) for x in weights]
 data=[[Paragraph(inline(c),styles['headcell' if i==0 else 'cell']) for c in row] for i,row in enumerate(rows)]
 t=Table(data,colWidths=[AW*x for x in fractions],repeatRows=1,hAlign='LEFT',splitByRow=1,splitInRow=1)
 commands=[('BACKGROUND',(0,0),(-1,0),PALE),('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),6),('RIGHTPADDING',(0,0),(-1,-1),6),('TOPPADDING',(0,0),(-1,-1),4),('BOTTOMPADDING',(0,0),(-1,-1),4),('LINEBELOW',(0,0),(-1,0),.7,ACC),('LINEBELOW',(0,1),(-1,-2),.25,RULE),('LINEBELOW',(0,-1),(-1,-1),.5,ACC)]
 for i,row in enumerate(rows[1:],1):
  if not any(c.get_text(strip=True) for c in row):commands.extend([('TOPPADDING',(0,i),(-1,i),10),('BOTTOMPADDING',(0,i),(-1,i),10)])
 t.setStyle(TableStyle(commands));return Item(t,6,9,None,'table',source,' | '.join(c.get_text(' ',strip=True) for c in rows[0]))
# A seleção anterior foi reavaliada contra o texto atual: três cenas úteis; o pacto não ilustra os casos atuais do apêndice D.
arts={'capitulo-02.html':('ab-cap-1-p-40.jpg','Uma ameaça sobrenatural num lugar comum. Gege Akutami / Shueisha, Jujutsu Kaisen, cap. 1.'),'capitulo-03.html':('rotas-rota-marcial-cap-35-p-18.jpg','Prática e convivência também oferecem situações de jogo. Gege Akutami / Shueisha, Jujutsu Kaisen, cap. 35.'),'capitulo-08.html':('equip-cap-47-p-8.jpg','Posição e equipamento participam das decisões. Gege Akutami / Shueisha, Jujutsu Kaisen, cap. 47.')}
def items_for(r):
 global DOC
 DOC=r['pagina'];s=DOCS[DOC];out=[];raw=[]
 def visit(node):
  if isinstance(node,Comment):
   match=re.search(r'espaco:\s*(\d+)',str(node))
   if match:out.append(Item(Spacer(1,int(match[1])*12),0,2,None,'space',DOC,''))
   return
  if not isinstance(node,Tag):return
  key=ALIASES.get((DOC,node.get('id')))
  if node.name in ['h1','h2','h3','h4','h5','h6']:
   kind={'h1':'major' if DOC in [x['pagina'] for x in core]+[front['pagina'],caseindex['pagina'],'folhas.html','apendice-c.html','apendice-d.html','referencias.html'] else 'h1','h2':'h2','h3':'h3','h4':'h3','h5':'h3','h6':'h3'}[node.name]
   if node.name=='h1':key=BOOKS[DOC]
   out.append(para(inline(node),kind,key,DOC,int(node.name[1])));raw.append(node.get_text(' ',strip=True));return
  if key:out.append(Item(Spacer(0,0),0,0,key,'anchor',DOC,'',keep_next=True))
  if node.name=='p':
   for nested in node.find_all(id=True):
    nestedkey=ALIASES[(DOC,nested['id'])];out.append(Item(Spacer(0,0),0,0,nestedkey,'anchor',DOC,'',keep_next=True))
   img=node.find('img')
   if img:
    add_image(img)
    if node.get_text(strip=True):out.append(para(inline(node),source=DOC));raw.append(node.get_text(' ',strip=True))
   elif node.get_text(strip=True):
    cls=node.get('class',[])
    kind='decision' if 'decisao' in cls else 'speech' if 'fala' in cls else 'technical' if 'consulta-tecnica' in cls else 'body'
    out.append(para(inline(node),kind,source=DOC));raw.append(node.get_text(' ',strip=True))
   return
  if node.name=='table':out.append(table(node,DOC));raw.append(node.get_text(' ',strip=True));return
  if node.name in ['ul','ol']:
   for index,li in enumerate(node.find_all('li',recursive=False),1):
    children=[c for c in li.children if not isinstance(c,Tag) or c.name not in ['ul','ol']]
    text=''.join(inline(c) for c in children);source=' '.join(c.get_text(' ',strip=True) if isinstance(c,Tag) else str(c) for c in children)
    out.append(para((str(index)+'. ' if node.name=='ol' else '• ')+text,source=DOC));raw.append(source)
    for nested in li.find_all(['ul','ol'],recursive=False):visit(nested)
   return
  if node.name=='blockquote':
   for p in node.find_all('p',recursive=False):out.append(para(inline(p),'note',source=DOC));raw.append(p.get_text(' ',strip=True))
   return
  if node.name=='figure':
   for img in node.find_all('img'):add_image(img)
   for cap in node.find_all('figcaption'):out.append(para(inline(cap),'small',source=DOC));raw.append(cap.get_text(' ',strip=True))
   return
  if node.name=='pre':
   # Diagramas ASCII remanescentes ficam largos, legíveis e sem quebra de linha.
   text=normalized(node.get_text());out.append(Item(Preformatted(text,styles['code']),5,8,None,'map',DOC,text));raw.append(node.get_text(' ',strip=True));return
  if node.name in ['section','div']:
   for child in list(node.children):visit(child)
   return
  if node.name=='span' and not node.get_text(strip=True):return
  if node.name=='hr':return
  raise ValueError(('Elemento não tratado',DOC,node.name,str(node)[:160]))
 def add_image(img):
  p=(E/img['src']).resolve();assert p.is_file();obj=Vector(p) if p.suffix=='.svg' else Illustration(p,'',maxheight=300)
  out.append(Item(obj,8,10,None,'map' if p.suffix=='.svg' else 'image',DOC,img.get('alt','')))
 for child in list(s.children):visit(child)
 # A extração independente do DOM deve estar integralmente representada nos blocos.
 tokens=lambda t:re.findall(r'[^\W_]+',normalized(t),re.U)
 from collections import Counter
 expected=Counter(tokens(s.get_text(' ',strip=True)));actual=Counter(tokens(' '.join(raw)))
 assert expected==actual,(DOC,dict(expected-actual),dict(actual-expected))
 if DOC in arts:
  file,caption=arts[DOC];portrait=DOC=='capitulo-08.html';pos=next((i for i,x in enumerate(out) if x.kind in ['h2','h3']),len(out))
  if portrait:
   grade=next(i for i,x in enumerate(out) if x.kind=='table' and x.text.startswith('Equipamento | Acesso publicado'));pos=grade+1
  out.insert(pos,Item(Illustration(B/'imagens'/file,caption,width=CW if portrait else AW,maxheight=260 if portrait else 220),8,12,None,'colimage' if portrait else 'image',DOC,caption))
 return out
pages=[];current=None;y=TOP;TAIL_WHOLE=False;SOURCE_LOG=[]
MAIN_STARTS={r['pagina'] for r in core}|{front['pagina'],'folhas.html','casos.html','apendice-c.html','apendice-d.html','referencias.html'}
DOC_PAGE={}
def build():
 global pages,current,y,DOC,DOC_PAGE
 pages=[];DOC_PAGE={}
 newpage('CAPA','Ciclo Maldito','cover')
 newpage('SUMÁRIO','Sumário');toc=[para('Sumário','major','sumario')]
 groups=[front]+core+[next(r for r in leaves if r['pagina']=='folhas.html'),caseindex,C,D,refs]
 for r in groups:
  label=('A · ' if r['pagina']=='folhas.html' else 'B · ' if r==caseindex else 'C · ' if r==C else 'D · ' if r==D else '')+r['titulo']
  if r==D:label+=' (revelações da trama)'
  key=r['key'];toc.append(para('<link href="#'+key+'" color="#9e2358">'+escape(label)+' · '+str(PAGEMAP.get(key,'000'))+'</link>','toc'))
  if r in core:
   heads=DOCS[r['pagina']].find_all('h2',id=True)
   details=' · '.join('<link href="#'+ALIASES[(r['pagina'],h['id'])]+'" color="#65545f">'+escape(h.get_text(' ',strip=True))+'</link>' for h in heads)
   toc.append(para(details,'small'))
 for item in toc:wide(item,'SUMÁRIO','Sumário')
 for r in order:
  doc=r['pagina'];items=items_for(r)
  # Cada folha imprimível começa numa página; casos seguem em fluxo para evitar páginas vazias.
  if doc in MAIN_STARTS or r in leaves or current.chapter!=r['parte']:newpage(r['parte'],r['titulo'])
  else:current.title='Casos por assunto' if r in cases else r['titulo']
  if doc in {x['pagina'] for x in core}:
   n=next(i for i,x in enumerate(core,1) if x==r);wide(para('CAPÍTULO '+str(n),'small',source=doc),r['parte'],r['titulo'])
  elif doc=='folhas.html':wide(para('APÊNDICE A · FOLHAS PARA A MESA','small',source=doc),r['parte'],r['titulo'])
  elif doc=='casos.html':wide(para('APÊNDICE B · CASOS POR ASSUNTO','small',source=doc),r['parte'],r['titulo'])
  elif doc=='apendice-c.html':wide(para('APÊNDICE C · CONSULTA SEM REVELAÇÕES','small',source=doc),r['parte'],r['titulo'])
  elif doc=='apendice-d.html':wide(para('APÊNDICE D · REVELAÇÕES DA TRAMA','small',source=doc),r['parte'],r['titulo'])
  chapter_start=len(pages)-1
  # Título principal usa a largura inteira; o texto entra em duas colunas.
  if items and items[0].kind in ['major','h1']:
   need=height(items[0],AW)+items[0].before+items[0].after
   for follow in items[1:]:
    need+=follow.before+height(follow,CW)+follow.after
    if follow.kind not in ['h2','h3','anchor']:break
   if need>y-BOTTOM and y<TOP-1:newpage(r['parte'],r['titulo'])
   wide(items.pop(0),r['parte'],r['titulo'])
  if doc=='referencias.html':
   for it in items:wide(it,r['parte'],r['titulo'])
  else:compose_items(items,r['parte'],r['titulo'])
  rebalance_tail(r['parte'],r['titulo'],chapter_start)
 result={}
 for n,p in enumerate(pages,1):
  for v in p.items:
   if v.item.key:
    assert v.item.key not in result,('âncora duplicada',v.item.key);result[v.item.key]=n
 for alias,key in ALIASES.items():assert key in result,(alias,key)
 return result
for attempt in range(8):
 new=build();print('Composição',attempt+1,':',len(pages),'páginas;',len(new),'destinos',flush=True)
 if new==PAGEMAP:break
 PAGEMAP=new
else:raise RuntimeError('Paginação não estabilizou')
OUT.parent.mkdir(parents=True,exist_ok=True);c=Canvas(str(OUT),pagesize=A4,pageCompression=1,invariant=1);c.setTitle('Ciclo Maldito - Guia do Mestre - pré-1.0 revisada');c.setAuthor('Mizuki_sama');c.setSubject('Guia de mestragem; texto integrado revisado em 30/10/2026')
geometry=[];textlog=[]
for num,p in enumerate(pages,1):
 if p.kind=='cover':
  c.drawImage(str(B/'imagens/capa-base.png'),0,0,width=W,height=H);c.setFillColor(HexColor('#2c2418'));c.setFont('Bold',29);yy=H-110
  for ch in 'CICLO MALDITO':
   if ch==' ':yy-=15;continue
   c.drawCentredString(W*174/1024,yy,ch);yy-=38
  c.setFont('Head',12);c.drawCentredString(W*174/1024,H*.279,'GUIA DO MESTRE');c.showPage();continue
 c.setFillColor(ACC);c.setFont('Head',8.5);c.drawString(M,H-34,'CICLO MALDITO / GUIA DO MESTRE')
 short=p.title.upper()
 while pdfmetrics.stringWidth(short,'Head',8.5)>AW*.54:short=short[:-2]
 if short!=p.title.upper():short=short.rstrip()+'…'
 c.setFillColor(MUTED);c.drawRightString(W-M,H-34,short);c.setStrokeColor(RULE);c.setLineWidth(.5);c.line(M,H-42,W-M,H-42)
 for v in p.items:
  it=v.item
  if it.key:
   c.bookmarkHorizontalAbsolute(it.key,v.top)
   if it.key in BOOKS.values() or it.key=='sumario':c.addOutlineEntry(it.text,it.key,0 if it.kind=='major' or it.key=='sumario' else 1,False)
  assert abs(it.f.wrap(v.w,H)[1]-v.h)<.1,(num,it.text)
  it.f.drawOn(c,v.x,v.top-v.h)
  if it.kind=='h2':c.setStrokeColor(ACC);c.setLineWidth(.65);c.line(v.x,v.top-v.h-1,v.x+35,v.top-v.h-1)
  geometry.append({'pagina':num,'tipo':it.kind,'fonte_html':it.source,'ancora':it.key,'x':round(v.x,2),'y_top':round(v.top,2),'largura':round(v.w,2),'altura':round(v.h,2),'texto':it.text[:180]})
  if hasattr(it.f,'getPlainText'):textlog.append({'pagina':num,'fonte':it.source,'texto':it.f.getPlainText()})
 nav=[('Sumário','sumario'),('Começar',front['key']),('Folhas',BOOKS['folhas.html']),('Casos',caseindex['key'])];nw=AW/len(nav)
 for i,(label,dest) in enumerate(nav):
  x=M+i*nw;c.setStrokeColor(MUTED);c.setLineWidth(.4);c.rect(x,61,nw,17,stroke=1,fill=0);c.setFillColor(MUTED);c.setFont('Head',9);c.drawCentredString(x+nw/2,66,label);c.linkRect('',dest,(x,61,x+nw,78),relative=0,thickness=0)
 c.setFont('Head',8.5);c.setFillColor(MUTED);c.drawString(M,34,'PRÉ-1.0 · EDIÇÃO DE LEITURA');c.setFillColor(ACC);c.drawRightString(W-M,34,str(num));c.showPage()
c.save()
(A/'composicao.json').write_text(json.dumps({'registro':147,'pdf':OUT.relative_to(R).as_posix(),'sha256_pdf':sha(OUT),'paginas':len(pages),'destinos':PAGEMAP,'fontes':meta['ordem'],'complemento_incluido':meta['complemento_incluido'],'ordem_pdf':[{'pagina_html':r['pagina'],'titulo':r['titulo'],'pagina_pdf':PAGEMAP[r['key']]} for r in order],'geometria':geometry,'medidas':{'pagina':'A4','margem_mm':19,'intervalo_colunas_mm':7,'corpo_pt':10.25,'entrelinha_pt':13.2},'selecao_de_imagens':arts,'preservacao_do_dom':'Texto do DOM sem menus comparado integralmente aos blocos antes da composição, por documento.','limite':'Composição e geometria; inspeção visual é uma etapa separada.'},ensure_ascii=False,indent=2)+'\n')
(A/'texto-composto.json').write_text(json.dumps(textlog,ensure_ascii=False)+'\n')
print(OUT,OUT.stat().st_size,flush=True)

from pathlib import Path
from dataclasses import dataclass
from functools import lru_cache
from xml.sax.saxutils import escape
import runpy,types,sys,json,re,hashlib,math,time
from reportlab.pdfgen.canvas import Canvas
from reportlab.platypus import Paragraph,Table,TableStyle
from reportlab.lib.utils import ImageReader
from reportlab.lib.colors import white
from PIL import Image
B=Path(__file__).resolve().parent
g=runpy.run_path(str(B/'ler_fontes.py'))
chapters,all_blocks,enriched,order=g['chapters'],g['all_blocks'],g['enriched'],g['order']
hierarquia=g['hierarquia']
nav_r40=json.loads((B/'revisao-r40/NAVEGACAO.json').read_text())
index_specific=json.loads((B/'revisao-de-estrutura/DESTINOS-INDICE.json').read_text())
index_specific += [{'termo':r['titulo'],'titulo':r['cabecalho'],'bloco':r['bloco'],'alias':r['destino']} for r in nav_r40 if 'cabecalho' in r]
assert not g['link_issues']
def component(name):
 p=B/'componentes'/name/'componente.py';m=types.ModuleType('layout_'+name);m.__file__=str(p);sys.modules[m.__name__]=m
 m.__dict__['_texto_editorial_revisado']={doc:'\n\n'.join('<!-- page:'+b.anchor+'|'+b.title+' -->\n'+g['base_before_structure'][b.key] for b in blocks) for doc,blocks in g['blocks'].items() if doc in ['dano','geral']}
 exec(compile(p.read_text(),str(p),'exec'),m.__dict__)
 return m
d=component('dano');r=component('geral')
# Todos os diagramadores usam o mesmo texto editorial revisado.
for module in (d,r):
 for block in module.blocks:
  if block['key'] in enriched:
   block['md']=g['base_before_structure'][block['key']]
   block['title']=all_blocks[block['key']].title

S,W,H,M,AW,G,CW,TOP,BOTTOM,INK,ACC,PALE,RULE,MUTED,EDGE=(getattr(d,n) for n in ['S','W','H','M','AW','G','CW','TOP','BOTTOM','INK','ACC','PALE','RULE','MUTED','EDGE'])
mm=d.mm;CAP=TOP-BOTTOM
from reportlab.lib.styles import ParagraphStyle
S['compactmajor']=ParagraphStyle('compactmajor',parent=S['major'],spaceAfter=4)
S['cost']=S['body']
S['marker']=S['small']
from densidade_editorial import configurar
DENSITY=json.loads((B/'ESTUDO-DENSIDADE.json').read_text())
ACC,PALE=configurar(S,B,d,r,DENSITY)
keys=set(all_blocks)|{c['key'] for c in chapters}|{f'parte-{i}' for i in range(1,6)}|{'capa','sumario','creditos'}
keys.update(row['alias'] for row in index_specific)
pagemap={};append_page_numbers=False

def inline(s,doc=None):
 tokens=[]
 def link(m):
  label,target=m.groups();dest=target.lstrip('#')
  if doc and '--' not in dest and dest not in keys:dest=doc+'--'+dest
  if target.startswith('#') and dest in keys:
   suffix=f' (p. {pagemap[dest]})' if append_page_numbers and dest in pagemap else ''
   v=f'<link href="#{dest}" color="#BC2A6E">{escape(label)}{suffix}</link>'
  elif target.startswith(('http://','https://')):v=f'<link href="{escape(target)}" color="#BC2A6E">{escape(label)}</link>'
  else:v=escape(label)
  tokens.append(v);return f'ZZPROTECTEDLINK{len(tokens)-1}ZZ'
 s=re.sub(r'\[([^\]]+)\]\(([^)]+)\)',link,str(s));s=escape(s.replace('–','-').replace('—','-').replace('−','-'))
 s=re.sub(r'\*\*(.*?)\*\*',r'<b>\1</b>',s);s=re.sub(r'`([^`]+)`',r'<b>\1</b>',s)
 s=re.sub(r'(?<!\*)\*([^*]+)\*(?!\*)',r'<i>\1</i>',s)
 for i,v in enumerate(tokens):s=s.replace(f'ZZPROTECTEDLINK{i}ZZ',v)
 return s
r.inline=inline;d.inline=inline

def fractions(rows):
 n=len(rows[0]);h=rows[0]
 if n==7 and h[0]=='Arma':return [.19,.07,.14,.27,.075,.085,.17]
 if n>=7 and h[0] in ['Nível','Classe','Classe real','Classe da especial']:return [.14]+[.86/(n-1)]*(n-1)
 if n==2:
  if h[0]=='Nível':return [.12,.88]
  if h[0]=='Assunto':return [.34,.66]
  means=[sum(len(row[j]) for row in rows[1:])/max(1,len(rows)-1) for j in range(n)]
  left=max(.20,min(.44,means[0]/max(1,sum(means))))
  return [left,1-left]
 if n==3:
  if h[0]=='Integridade perdida':return [.23,.09,.68]
  if h[0]=='Momento':return [.44,.28,.28]
  if h[0]=='Degrau':return [.13,.63,.24]
  if h[0]=='Grau':return [.13,.64,.23]
  if h[0]=='TR':return [.16,.24,.60]
  if h[0]=='Melhoria':return [.25,.65,.10]
  if h[0]=='Porte e exemplo':return [.64,.18,.18]
  if h[0]=='Ofício':return [.20,.21,.59]
  return [.27,.34,.39]
 if n==4:
  if h[0]=='Item':return [.28,.43,.16,.13]
  if h[0]=='Arma e carga correspondente':return [.44,.21,.19,.16]
  if h[0]=='Nível':return [.14,.28,.30,.28]
  if h[0]=='Forma':return [.20,.22,.29,.29]
  return [.25]*4
 if n==5 and h[0]=='Item':return [.22,.23,.22,.18,.15]
 if n==6:return [.16,.20,.19,.15,.15,.15]
 return [1/n]*n

@dataclass
class Part:
 kind:str
 text:object
 key:str=None
 doc:str=None
 block:str=None
 generated:bool=False
 def make(self,w):
  if self.kind=='esquema':
   maker=d.Schematic if self.text=='janela' else r.Schematic
   return maker(self.text,w),8,10
  if self.kind in ['glossary','indexentry']:
   match=re.match(r'^\[([^\]]+)\]\(#([^)]+)\)(.*)$',self.text);assert match,self.text
   term,target,tail=match.groups()
   label='<link href="#'+target+'" color="#BC2A6E">'+escape(term)+'</link>'
   if self.kind=='glossary':
    return Paragraph('<b>'+label+'</b>'+inline(tail,self.doc),S['body']),0,5
   page=str(pagemap.get(target,'000'))
   t=Table([[Paragraph(label,S['index']),Paragraph('<link href="#'+target+'" color="#BC2A6E">'+page+'</link>',S['index'])]],colWidths=[w-27,27])
   t.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),0),('RIGHTPADDING',(0,0),(-1,-1),0),('TOPPADDING',(0,0),(-1,-1),1.8),('BOTTOMPADDING',(0,0),(-1,-1),1.8),('LINEBELOW',(0,0),(-1,-1),.25,RULE)]))
   return t,0,0
  if self.kind=='table':
   rows=self.text;n=len(rows[0]);commands=[]
   rendered=[]
   for i,row in enumerate(rows):
    category=i>0 and all(not s for s in row[1:])
    st=S['headcell' if i==0 else 'cell']
    if category:
     from reportlab.lib.styles import ParagraphStyle
     st=ParagraphStyle('category',parent=S['cell'],fontName='Head',textColor=white)
     commands.extend([('SPAN',(0,i),(-1,i)),('BACKGROUND',(0,i),(-1,i),MUTED)])
    rendered.append([Paragraph(inline(s,self.doc),st) for s in row])
   t=Table(rendered,colWidths=[w*v for v in fractions(rows)],repeatRows=1,hAlign='LEFT')
   t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),ACC),('ROWBACKGROUNDS',(0,1),(-1,-1),[white,PALE]),('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),6),('RIGHTPADDING',(0,0),(-1,-1),6),('TOPPADDING',(0,0),(-1,-1),4),('BOTTOMPADDING',(0,0),(-1,-1),4),('BOX',(0,0),(-1,-1),.65,EDGE),('INNERGRID',(0,0),(-1,-1),.25,EDGE)]+commands))
   return t,8,10
  if self.kind=='note':
   t=Table([[Paragraph(inline(self.text,self.doc),S['note'])]],colWidths=[w]);t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,-1),PALE),('BOX',(0,0),(-1,-1),.65,EDGE),('LEFTPADDING',(0,0),(-1,-1),9),('RIGHTPADDING',(0,0),(-1,-1),9),('TOPPADDING',(0,0),(-1,-1),8),('BOTTOMPADDING',(0,0),(-1,-1),8)]));return t,4,8
  st=S[self.kind];return Paragraph(inline(self.text,self.doc),st),st.spaceBefore,st.spaceAfter

@dataclass
class Unit:
 parts:list
 connected:bool=True
 def measure(self,w):
  h=0;out=[]
  for p in self.parts:
   f,b,a=p.make(w);fh=f.wrap(w,H)[1];out.append((p,f,b,fh,a));h+=b+fh+a
  return h,out

def parse(b):
 lines=enriched[b.key].splitlines();parts=[];i=0;sub=0;current_context=hierarquia.get(b.key,{}).get('contexto')
 while i<len(lines):
  l=lines[i].strip();i+=1
  if not l or l=='---':continue
  if l.startswith('|'):
   raw=[l]
   while i<len(lines) and lines[i].strip().startswith('|'):raw.append(lines[i].strip());i+=1
   rows=[[v.strip() for v in row.strip('|').split('|')] for row in raw if not re.fullmatch(r'[\s|:\-]+',row)]
   assert len({len(row) for row in rows})==1,b.key
   p=Part('table',rows,doc=b.doc,block=b.key)
  elif l.startswith('#'):
   level=len(l)-len(l.lstrip('#'));key=b.key if not parts else f'{b.key}-sub-{sub}';sub+=1
   p=Part('h'+str(min(level,3)),l[level:].strip(),key=key,doc=b.doc,block=b.key)
  else:
   kind='body'
   if l== '**'+str(hierarquia.get(b.key,{}).get('marcador'))+'**' or (b.key=='incursor--inc-continuacoes' and l=='**Continuações**'):kind='marker'
   if re.fullmatch(r'\*\*(Preço|Categoria de Efeito): .+\*\*',l):kind='cost'
   if re.fullmatch(r'\*\*Nível \d+\.\*\*',l):kind='cost'
   if b.doc in {'incursor','evocador'} and kind=='body' and re.fullmatch(r'\*\*[^*]+\*\*',l) and '=' not in l:kind='cost'
   if l.startswith('> '):kind='note';l=l[2:]
   if l.startswith('- '):l='• '+l[2:]
   p=Part(kind,l,doc=b.doc,block=b.key)
  if not parts and not p.key:p.key=b.key
  cfg=hierarquia.get(b.key,{})
  p.role=next((h['papel'] for h in cfg.get('titulos',[]) if h['titulo']==p.text), 'metadado' if p.kind=='cost' else 'texto')
  if p.kind.startswith('h'):current_context=cfg.get('contextos_por_titulo',{}).get(p.text,current_context)
  p.context=current_context
  p.aliases=[row['alias'] for row in index_specific if row['bloco']==b.key and row.get('titulo',row['termo'])==p.text and p.kind.startswith('h')]
  classificar_titulo(p)
  parts.append(p)
  if b.doc=='geral' and b.anchor=='defesa' and p.kind=='note' and 'Sousuke tem Defesa 15' in str(p.text):
   parts.append(Part('esquema','cobertura',doc=b.doc,block=b.key,generated=True))
 if b.doc=='geral' and b.anchor=='movimento':parts.append(Part('esquema','movimento',doc=b.doc,block=b.key,generated=True))
 if b.doc=='dano' and b.anchor=='zero':
  start=next((i for i,p in enumerate(parts) if p.text=='Janela de socorro'),None)
  if start is not None:
   end=next((i for i in range(start+1,len(parts)) if parts[i].kind in ['h1','h2','h3']),len(parts))
   parts.insert(end,Part('esquema','janela',doc=b.doc,block=b.key,generated=True))
 return parts

from densidade_editorial import instalar_partes
instalar_partes(Part,globals())
from tabelas_destaques import instalar as instalar_tabelas
instalar_tabelas(Part,globals())
from titulos_secao import instalar as instalar_secao
instalar_secao(Part,globals())

from titulos_intermediarios import instalar as instalar_intermediarios
instalar_intermediarios(Part,globals())

pages=[];events=[];positions={};information=[];changes=[{'tipo':'acesso_a_ficha','bloco':'ab--ab-criacao','motivo':'Link da ficha digital solicitado pelo autor durante a diagramação.'}]
def newpage(ch,group=None,kind='content'):
 p={'numero':len(pages)+1,'chapter':ch,'group':group or ch['titulo'],'kind':kind,'draws':[],'art':None};pages.append(p);return p

def put(page,unit,x,y,w,mode,band=None,info=None):
 h,measured=unit.measure(w);yy=y
 assert yy-h>=page.get('bottom',BOTTOM)-.05,(page['numero'],'overflow',yy-h,h,[p.text for p in unit.parts[:2]])
 start=len(events)
 for p,f,b,fh,a in measured:
  yy-=b;page['draws'].append((p,f,x,yy-fh,w,fh,mode))
  if p.key:
   assert p.key not in positions,p.key
   positions[p.key]=(page['numero'],x,yy)
  for alias in getattr(p,'aliases',[]):
   assert alias not in positions,alias
   positions[alias]=(page['numero'],x,yy)
  events.append({'pagina':page['numero'],'capitulo':page['chapter']['numero'],'bloco':p.block,'tipo':p.kind,'papel':getattr(p,'role',None),'tratamento_hierarquia':getattr(p,'editorial_style',None),'nivel_editorial':getattr(p,'editorial_level',None),'contexto':getattr(p,'context',None),'x':round(x,3),'y':round(yy-fh,3),'largura':round(w,3),'altura':round(fh,3),'modo':mode,'faixa':band,'gerado':p.generated,'texto':p.text})
  yy-=fh+a
 if info:information.append({'chave':info,'pagina':page['numero'],'largura':round(w,3),'eventos':[start,len(events)]})
 return h

def attach_key(page,key,x=M,y=TOP):
 assert key not in positions,key;positions[key]=(page['numero'],x,y)

# Consulta e esquemas preservados; o corpo segue o mesmo fluxo dos demais capítulos.
def approved(ch,module,doc):
 original_make=module.Part.make
 def consulta_make(part,w):
  if part.text=='Consulta' and part.kind in {'h1','h2'}:
   part.kind='h1'
   return Part('h1','Consulta',generated=True).make(w)
  return original_make(part,w)
 module.Part.make=consulta_make
 module.build_plan(pagemap)
 draws=[row for row in module.DRAW if row[0]==1]
 for number in sorted({row[0] for row in draws}):
  rows=[row for row in draws if row[0]==number];p=newpage(ch,' / '.join(dict.fromkeys(row[1] for row in rows)))
  if number==1:attach_key(p,ch['key'])
  for _,group,part,f,x,y,w,h,mode in rows:
   if number==1 and part.kind=='major':
    f=Paragraph(f'{ch["numero"]}. {ch["titulo"]}',S['major']);h=f.wrap(w,H)[1]
   elif number==1 and part.kind=='small':f=Paragraph('Consulta do capítulo',S['small']);h=f.wrap(w,H)[1]
   if part.key:attach_key(p,part.key,x,y+h)
   p['draws'].append((part,f,x,y,w,h,mode))
   events.append({'pagina':p['numero'],'capitulo':ch['numero'],'bloco':part.block,'tipo':part.kind,'x':round(x,3),'y':round(y,3),'largura':round(w,3),'altura':round(h,3),'modo':mode,'faixa':None,'gerado':number==1,'texto':part.text})
 ps=[part for group in ch['grupos'] for block in group['blocks'] for part in parse(block)]
 add_atoms(ch,atoms_for(ps,ch['titulo']))
 pnav=[(name,ch['key'] if dest=='consulta' else dest) for name,dest in module.nav]
 for p in pages:
  if p['chapter'] is ch:p['nav']=pnav

artdata=json.loads((B/'REFERENCIAS.json').read_text())
newart=json.loads((B/'ARTES-APLICADAS.json').read_text())
placements=[]
incmajors={'inc-caminho':'Incursor','inc-assassino':'Assassino','inc-pugilista':'Pugilista','inc-malabarista':'Malabarista'}

# Oversize tables split between whole rows with repeated headers.
def split_table(part,limit):
 rows=part.text;chunks=[];start=1
 while start<len(rows):
  end=start+1
  while end<len(rows) and Unit([Part('table',[rows[0]]+rows[start:end+1],doc=part.doc,block=part.block)]).measure(AW)[0]<=limit:end+=1
  if end<len(rows) and all(not v for v in rows[end-1][1:]) and end-1>start:end-=1
  subset=[rows[0]]+rows[start:end]
  q=Part('table',subset,doc=part.doc,block=part.block)
  assert Unit([q]).measure(AW)[0]<=limit,(part.block,'row too tall')
  chunks.append(q);start=end
 return chunks

def atoms_for(parts,group):
 sections=[];current=[]
 for p in parts:
  if current and p.kind in ['h1','h2','h3','major']:
   if all(x.kind in ['h1','h2','h3','major','small'] for x in current):current.append(p);continue
   sections.append(current);current=[]
  current.append(p)
 if current:sections.append(current)
 # A short introduction is kept with the following complete subsection.
 if len(sections)>1 and len(sections[0])<=3 and all(p.kind not in ['table','note'] for p in sections[0]) and Unit(sections[0]+sections[1]).measure(AW)[0]<=CAP:
  sections[:2]=[sections[0]+sections[1]]
 result=[]
 for section in sections:
  h=Unit(section).measure(AW)[0]
  chunks=[section]
  if h>CAP:
   chunks=[];chunk=[];lasthead=next((p.text for p in section if p.kind in ['h1','h2','h3','major']),group)
   for p in section:
    expansion=split_table(p,CAP-80) if p.kind=='table' and Unit([p]).measure(AW)[0]>CAP-80 else [p]
    for q in expansion:
     if chunk and Unit(chunk+[q]).measure(AW)[0]>CAP:
      # Keep any heading/short cost line with the following explanation.
      carry=[]
      while chunk and (chunk[-1].kind in ['h1','h2','h3','major'] or (chunk[-1].kind=='body' and len(str(chunk[-1].text))<80)):
       carry.insert(0,chunk.pop())
      assert chunk,(q.block,'oversize heading bundle')
      chunks.append(chunk)
      cont=Part('h3',lasthead+' (continuação)',doc=q.doc,block=q.block,generated=True)
      chunk=[cont]+carry
     chunk.append(q)
   if chunk:chunks.append(chunk)
   changes.append({'tipo':'continuidade','bloco':section[0].block,'titulo':lasthead,'altura_original':round(h,1),'segmentos':len(chunks),'motivo':'Seção maior que uma página. Divisão entre parágrafos/linhas inteiros, com cabeçalho de continuação.'})
  for chunk in chunks:
   u=Unit(chunk);ah=u.measure(AW)[0];cw=u.measure(CW)[0]
   assert ah<=CAP,(chunk[0].block,ah)
   result.append({'unit':u,'key':(next((p.key for p in chunk if p.key),chunk[0].block) or group)+f'--info-{len(result)}','group':group,'wide':any(p.kind in ['table','major'] for p in chunk) or any(p.generated for p in chunk),'aw':ah,'cw':cw})
 return result

def plan_atoms(atoms):
 N=len(atoms)
 if not N:return []
 options=[]
 for i,a in enumerate(atoms):
  opt=[{'i':i,'j':i+1,'cut':None,'height':a['aw']}]
  if not a['wide']:
   for j in range(i+2,min(N,i+6)+1):
    run=atoms[i:j]
    if any(x['wide'] for x in run) or len({x['group'] for x in run})!=1:break
    for cut in range(i+1,j):
     left=sum(x['cw'] for x in atoms[i:cut])+4*(cut-i-1);right=sum(x['cw'] for x in atoms[cut:j])+4*(j-cut-1);h=max(left,right)
     if h<=CAP and h<=sum(x['aw'] for x in run)+4*(len(run)-1) and abs(left-right)<=max(30,.25*h):opt.append({'i':i,'j':j,'cut':cut,'height':h})
  options.append(opt)
 def prune(states):
  v={}
  for h,bands in states:
   k=round(h,2)
   if k not in v or sum(b['cut'] is not None for b in bands)<sum(b['cut'] is not None for b in v[k][1]):v[k]=(h,bands)
  vals=list(v.values())
  if len(vals)<=12:return vals
  keep=sorted(vals,key=lambda x:x[0])[:5]+sorted(vals,key=lambda x:-x[0])[:5]+sorted(vals,key=lambda x:sum(b['cut'] is not None for b in x[1]))[:2]
  return list({round(h,2):(h,b) for h,b in keep}.values())
 best={N:((0,0,0),[])}
 for start in range(N-1,-1,-1):
  states={start:[(0,[])]};choices=[]
  for i in range(start,N):
   if i not in states:continue
   for height,bands in prune(states[i]):
    for band in options[i]:
     h=height+(4 if bands else 0)+band['height']
     if h<=CAP:states.setdefault(band['j'],[]).append((h,bands+[band]))
   if i>start:
    for h,bands in prune(states[i]):
     score,rest=best[i];narrow=sum(b['j']-b['i'] for b in bands if b['cut'] is not None)
     cost=(score[0]+1,score[1]+(CAP-h)**2-12000*narrow,score[2]+sum(b['cut'] is not None for b in bands))
     choices.append((cost,[{'height':h,'bands':bands}]+rest))
  for h,bands in prune(states.get(N,[])):
   narrow=sum(b['j']-b['i'] for b in bands if b['cut'] is not None)
   choices.append(((1,(CAP-h)**2-12000*narrow,sum(b['cut'] is not None for b in bands)),[{'height':h,'bands':bands}]))
  assert choices,('No page placement',atoms[start]['key']);best[start]=min(choices,key=lambda x:x[0])
 return best[0][1]

def add_atoms(ch,atoms):
 for plan in plan_atoms(atoms):
  p=newpage(ch,atoms[plan['bands'][0]['i']]['group']);y=TOP
  for bi,band in enumerate(plan['bands']):
   if bi:y-=4
   i,j,cut=band['i'],band['j'],band['cut'];bandno=f'{p["numero"]}-{bi}'
   if cut is None:y-=put(p,atoms[i]['unit'],M,y,AW,'uma-coluna',bandno,atoms[i]['key'])
   else:
    for start,end,x in [(i,cut,M),(cut,j,M+CW+G)]:
     yy=y
     for k in range(start,end):
      yy-=put(p,atoms[k]['unit'],x,yy,CW,'duas-colunas',bandno,atoms[k]['key'])
      if k+1<end:yy-=4
    y-=band['height']
  p['content_height']=plan['height']

from fluxo_continuo import Fluxo
fluxo=Fluxo(globals())
atoms_for=fluxo.atoms_for
add_atoms=fluxo.add_atoms

def add_compact(ch):
 # Fluxo alfabético em duas colunas. Cada verbete é uma unidade indivisível.
 entries=[]
 for group in ch['grupos']:
  for block in group['blocks']:
   first=True
   for line in enriched[block.key].splitlines()[1:]:
    if not line.strip():continue
    kind='glossary' if ch['numero']==19 else 'indexentry'
    part=Part(kind,line.strip(),key=block.key if first else None,doc=block.doc,block=block.key)
    first=False;entries.append(Unit([part]))
 heights=[u.measure(CW)[0] for u in entries];at=0;firstpage=True
 while at<len(entries):
  page=newpage(ch);y=TOP
  head=Part('compactmajor' if firstpage else 'h3',f'{ch["numero"]}. {ch["titulo"]}' if firstpage else ch['titulo'],key=ch['key'] if firstpage else None,generated=True)
  y-=put(page,Unit([head]),M,y,AW,'uma-coluna')
  cap=y-BOTTOM
  if sum(heights[at:])<=2*cap:
   # A última página conserva colunas com alturas próximas.
   cuts=[k for k in range(at+1,len(entries)+1) if sum(heights[at:k])<=cap and sum(heights[k:])<=cap]
   assert cuts,(ch['titulo'],at,cap)
   cut=min(cuts,key=lambda k:abs(sum(heights[at:k])-sum(heights[k:])))
   ends=[cut,len(entries)]
  else:
   ends=[];cursor=at
   for col in range(2):
    used=0
    while cursor<len(entries) and used+heights[cursor]<=cap:
     used+=heights[cursor];cursor+=1
    ends.append(cursor)
  start=at;bottoms=[]
  for col,end in enumerate(ends):
   yy=y;x=M+col*(CW+G)
   for k in range(start,end):
    yy-=put(page,entries[k],x,yy,CW,'duas-colunas',f'consulta-{page["numero"]}',f'{ch["key"]}-verbete-{k}')
   bottoms.append(yy);start=end
  assert start>at
  at=start;firstpage=False;page['content_height']=TOP-min(bottoms)

def illustrated_opening(ch,b,cfg,intro,rest):
 layout=cfg.get('composicao','rodape');data=artdata['imagens'][cfg['imagem']]
 page=newpage(ch,b.title,'art');w=data.get('largura_mm',210)*mm
 x0,y0,x1,y1=data['crop'];ih=w*(y1-y0)/(x1-x0);x=(W-w)/2
 # Each section remains complete. Image placement never changes its wording.
 heads=[];body=list(intro)
 while body and body[0].kind in ['major','h1']:
  heads.append(body.pop(0))
 y=TOP
 if layout=='rodape':
  y-=put(page,Unit(intro),M,y,AW,'uma-coluna',info=b.key+'--abertura')
  bottom=38*mm;credit=34*mm
 elif layout=='topo':
  if heads:y-=put(page,Unit(heads),M,y,AW,'uma-coluna')
  bottom=y-ih-8;credit=bottom-12;y=bottom-24
  y-=put(page,Unit(body),M,y,AW,'uma-coluna',info=b.key+'--abertura')
 elif layout.startswith('lateral'):
  if heads:y-=put(page,Unit(heads),M,y,AW,'uma-coluna')
  tw=AW-w-G;left=layout=='lateral-esquerda';x=M if left else W-M-w;tx=M+w+G if left else M
  th=put(page,Unit(body),tx,y,tw,'texto-ao-lado-da-imagem',info=b.key+'--abertura-lateral')
  offset=max(0,(th-ih)/2) if cfg.get('alinhamento_vertical')=='centro' else 0
  bottom=y-ih-offset;credit=bottom-12;y=min(y-th,credit-12)
 else:
  # A horizontal panel separates introductions from the following procedure/table.
  count=cfg.get('inserir_apos_corpo',999);at=0;seen=0
  for i,q in enumerate(intro):
   if q.kind=='body':seen+=1
   if seen>=count:at=i+1;break
  if not at:at=len(intro)
  y-=put(page,Unit(intro[:at]),M,y,AW,'uma-coluna',info=b.key+'--introducao')
  bottom=y-ih-8;credit=bottom-12;y=bottom-24
  if intro[at:]:y-=put(page,Unit(intro[at:]),M,y,AW,'uma-coluna',info=b.key+'--procedimento')
 assert bottom>=38*mm-.05,(b.key,'imagem invade rodapé',bottom,BOTTOM)
 assert bottom+ih<=TOP,(b.key,'imagem invade cabeçalho')
 page['art']={'name':cfg['imagem'],'top':y-12 if layout=='rodape' else bottom+ih,'data':data,'bottom':bottom,'panel_x':x,'panel_w':w,'credit_y':credit,'composicao':layout}
 if layout!='rodape':
  # Use remaining room only for an entire subsection, with one prose width.
  while rest:
   end=next((i for i,q in enumerate(rest[1:],1) if q.kind in ['h1','h2','h3','major']),len(rest))
   whole=rest[:end];height=Unit(whole).measure(AW)[0]
   if y-8-height<BOTTOM:break
   y-=8;y-=put(page,Unit(whole),M,y,AW,'uma-coluna',info=b.key+'--complemento-'+str(len(rest)));rest=rest[end:]
 page['content_height']=TOP-min(y,bottom)
 return rest

# R40: capítulos, seções e Trilhas com o mesmo mapa dos marcadores.
from sumario_r40 import construir as construir_sumario
construir_sumario(globals())

for ch in chapters:
 opening=newpage(ch,kind='cover');opening['cover_title']=ch['titulo'];opening['cover_number']=ch['numero'];attach_key(opening,'abertura-capitulo-'+str(ch['numero']))
 print('Planejando',ch['numero'],ch['titulo'],flush=True);before=len(pages)
 if ch['numero'] in [19,21]:add_compact(ch)
 elif ch['numero']==2:approved(ch,r,'geral')
 elif ch['numero']==3:approved(ch,d,'dano')
 else:
  first=True;pending_groups=[]
  for group in ch['grupos']:
   ps=[];atoms=[];groupname=ch['titulo']
   for bi,b in enumerate(group['blocks']):
    items=parse(b)
    if ch['numero']==20 and (b.anchor.startswith('consulta-ficha-') or b.anchor=='consulta-registro-missao'):
     if ps:atoms.extend(atoms_for(ps,groupname));ps=[]
     if pending_groups or atoms:add_atoms(ch,pending_groups+atoms);pending_groups=[];atoms=[]
     # Printable templates use the same type sizes, with the navigation strip omitted.
     # This frees vertical room for the complete form, without shrinking its fields.
     original_bottom,original_top,original_cap=BOTTOM,TOP,CAP
     BOTTOM=19*mm;TOP=H-19*mm;CAP=TOP-BOTTOM
     previous=len(pages)
     if Unit(items).measure(AW)[0]<=CAP:
      fp=newpage(ch,b.title,'form');fp['bottom']=BOTTOM
      put(fp,Unit(items),M,TOP,AW,'uma-coluna',info=b.key+'--modelo-completo')
     else:
      form_atoms=atoms_for(items,b.title);add_atoms(ch,form_atoms)
      for fp in pages[previous:]:fp['kind']='form';fp['bottom']=BOTTOM
     changes.append({'tipo':'modelo_imprimivel','bloco':b.key,'paginas':len(pages)-previous,'motivo':'Faixa de navegação omitida no modelo. Mesmas fontes e tabelas; mais área útil para preencher e imprimir.'})
     BOTTOM,TOP,CAP=original_bottom,original_top,original_cap
     continue
    if first:
     chapterpart=Part('major',f'{ch["numero"]}. {ch["titulo"]}',key=ch['key'],generated=True)
     if b.title.casefold()==ch['titulo'].casefold():
      items[0].key=b.key;chapterpart.key=ch['key'];items=items[1:]
      # Duplicate source title is represented by the chapter heading.
      alias=(b.key,ch['key'])
     else:alias=None
     ps.append(chapterpart);first=False
    if b.key in newart:
     cfg=newart[b.key];prefix=[]
     if ps and all(q.generated and q.kind=='major' for q in ps):prefix=ps;ps=[]
     if ps:atoms.extend(atoms_for(ps,groupname));ps=[]
     if pending_groups or atoms:add_atoms(ch,pending_groups+atoms);pending_groups=[];atoms=[]
     groupname=b.title
     if cfg.get('titulo_no_capitulo') and items and items[0].kind=='h1':items=items[1:]
     if items and items[0].kind=='h1':items[0].kind='major'
     limit=next((i for i,q in enumerate(items) if ((q.kind=='h2' and q.text==cfg['fim_abertura']) if cfg.get('fim_abertura') else (q.kind=='h2' or (cfg['corte_texto']=='lead' and q.kind=='table')))),len(items))
     intro,rest=prefix+items[:limit],items[limit:]
     rest=illustrated_opening(ch,b,cfg,intro,rest)
     if cfg.get('titulo_no_capitulo'):positions[b.key]=positions[ch['key']]
     ps.extend(rest)
     changes.append({'tipo':'abertura_ilustrada','bloco':b.key,'imagem':cfg['imagem'],'motivo':'Cena relacionada ao assunto. Introdução inteira, imagem no rodapé e regras preservadas.'})
     continue
    if group['caminho'] and bi==0:
     if ps:atoms.extend(atoms_for(ps,groupname));ps=[]
     groupname=b.title
     items[0].kind='major'
    if b.doc=='incursor' and b.anchor in incmajors:
     if ps:atoms.extend(atoms_for(ps,groupname));ps=[]
     if pending_groups or atoms:add_atoms(ch,pending_groups+atoms);pending_groups=[];atoms=[]
     groupname=incmajors[b.anchor];items[0].kind='major' if b.anchor=='inc-caminho' else 'h1'
     limit=next((i for i,q in enumerate(items) if q.kind=='h2' and (q.text.startswith('Progressão') if b.anchor=='inc-caminho' else not q.text.startswith('Progressão'))),len(items))
     intro,rest=items[:limit],items[limit:]
     ip=newpage(ch,groupname,'art');height=put(ip,Unit(intro),M,TOP,AW,'uma-coluna',info=b.key+'--abertura')
     ip['art']={'name':groupname,'top':TOP-height-12,'data':artdata['imagens'][groupname]}
     assert ip['art']['top']-38*mm>=45*mm,(b.key,'not enough room for art')
     ps.extend(rest)
    else:ps.extend(items)
   if ps:atoms.extend(atoms_for(ps,groupname))
   if atoms:pending_groups.extend(atoms)
   if ch['numero']!=6 and group is ch['grupos'][0] and 'alias' in locals() and alias:
    pass # Bound after the remaining chapter flow is emitted.
  if pending_groups:add_atoms(ch,pending_groups)
  if ch['numero']!=6 and 'alias' in locals() and alias and alias[0] not in positions:
   positions[alias[0]]=positions[alias[1]]
  if ch['key'] not in positions:attach_key(pages[before],ch['key'])
 # Part headings are bookmarks, not extra mostly empty separator sheets.
 pk='parte-'+str(ch['parte'])
 if pk not in positions:positions[pk]=positions[ch['key']]
 print(' ',len(pages)-before,'páginas',flush=True)

# Créditos ficam após o índice e não criam um capítulo de regras.
credits=json.loads((B/'CREDITOS.json').read_text())
credit_ch={'numero':0,'titulo':credits['titulo'],'key':'creditos','parte':5}
credit_page=newpage(credit_ch,kind='credits')
credit_parts=[Part(kind,text,key='creditos' if i==0 else None,generated=True) for i,(kind,text) in enumerate(credits['elementos'])]
credit_page['content_height']=put(credit_page,Unit(credit_parts),M,TOP,AW,'uma-coluna',info='creditos--pagina-completa')
changes.append({'tipo':'creditos_e_direitos','motivo':'Autoria informada pelo autor. Aviso verificado em fontes primárias, reunido após o índice para preservar a entrada do jogador no livro.'})

assert set(all_blocks)<=set(positions),('Missing source anchors',set(all_blocks)-set(positions))
pagemap={k:v[0] for k,v in positions.items()}
for page in pages:
 # Um cabeçalho não atribui a página inteira à primeira Família ou aptidão
 # quando a composição contém também outra categoria.
 contexts=list(dict.fromkeys((getattr(part,'context',None) or hierarquia[part.block]['contexto']) for part,_,_,_,_,_,_ in page['draws'] if part.block in hierarquia))
 if len(contexts)>1:
  if all(t.startswith('Família: ') for t in contexts):page['group']='Famílias: '+', '.join(t[9:] for t in contexts)
  elif len({t.split(' / ')[0] for t in contexts})==1:page['group']=contexts[0].split(' / ')[0]
  else:page['group']=page['chapter']['titulo']
 revised=[]
 for part,f,x,y,w,h,mode in page['draws']:
  if part.kind=='indexentry':
   f,_,_=part.make(w)
   assert abs(f.wrap(w,H)[1]-h)<.01,(part.text,'índice mudou de altura')
  revised.append((part,f,x,y,w,h,mode))
 page['draws']=revised

# Replace consultation index placeholders after the complete map exists.
for ch,mod,doc in [(chapters[1],r,'geral'),(chapters[2],d,'dano')]:
 mod.build_plan(pagemap)
 fresh=iter([z for z in mod.DRAW if z[0]==1 and z[2].kind=='index'])
 page=next(p for p in pages if p['chapter'] is ch and p['kind']!='cover')
 old=page['draws'];new=[]
 for part,f,x,y,w,h,mode in old:
  if part.kind=='index':
   z=next(fresh);f=z[3]
  new.append((part,f,x,y,w,h,mode))
 page['draws']=new

PDF=B/'output/pdf/Ciclo-Maldito-R42.pdf'
from titulos_capitulo import desenhar as desenhar_titulo_capitulo
estudo_capitulo=json.loads((B/'ESTUDO-CAPITULO.json').read_text())
titulos_capitulo_aplicados=[]
c=Canvas(str(PDF),pagesize=(W,H),pageCompression=1);c.setTitle('Ciclo Maldito | Livro de regras');c.setAuthor('Mizuki_sama');c.showOutline()
outline={'capa':('Ciclo Maldito',0)}
last_part=None
for ch in chapters:
 if ch['parte']!=last_part:
  last_part=ch['parte'];outline['parte-'+str(last_part)]=(order['partes'][last_part-1]['titulo'],0)
 outline[ch['key']]=(str(ch['numero'])+'. '+ch['titulo'],1)
 for row in nav_r40:
  if row['capitulo']==ch['numero']:
   assert row['destino'] in positions,row
   outline[row['destino']]=(row['titulo'],row['nivel'])

outline['creditos']=(credits['titulo'],0)

from capa_aberturas import draw_cover
cover_placements=[]
for page in pages:
 n=page['numero'];ch=page['chapter'];c.setFillColor(white);c.rect(0,0,W,H,fill=1,stroke=0)
 if page['kind']!='cover':
  c.setFillColor(ACC);c.setFont('Head',9);c.drawString(M,H-12*mm,'CICLO MALDITO')
  c.setFillColor(MUTED);header=ch['titulo'].upper()
  if page['group']!=ch['titulo']:header+=' / '+page['group'].upper()
  size=min(9,9*AW/max(AW,d.pdfmetrics.stringWidth(header,'Head',9)));c.setFont('Head',size);c.drawRightString(W-M,H-12*mm,header)
  c.setStrokeColor(RULE);c.setLineWidth(.5);c.line(M,H-15*mm,W-M,H-15*mm)
 for key,(pn,x,y) in positions.items():
  if pn==n:
   c.bookmarkHorizontalAbsolute(key,y,x)
   pass
 for key,(title,level) in outline.items():
  if positions[key][0]==n:c.addOutlineEntry(title,key,level,True)
 if page['kind']=='cover':
  cover=draw_cover(c,B,W,H,page.get('cover_title'),page.get('cover_number'),ch['key'] if page.get('cover_number') else 'sumario');cover['pagina']=n;cover_placements.append(cover)
 for part,f,x,y,w,h,mode in page['draws']:
  if page['kind']!='cover' and 1<=ch['numero']<=21 and part.kind in ['major','compactmajor'] and n==pagemap.get(ch.get('key')) and abs(y-(TOP-36))<.1:
   desenhar_titulo_capitulo(c,ch['numero'],ch['titulo'],x,y,w,estudo_capitulo['aprovado'])
   titulos_capitulo_aplicados.append({'numero':ch['numero'],'titulo':ch['titulo'],'pagina':n,'x':x,'y':y,'largura':w,'altura':h,'opcao':estudo_capitulo['aprovado']})
  else:f.drawOn(c,x,y)
 if page.get('art'):
  art=page['art'];data=art['data'];path=B/'referencias'/data['arquivo'];im=Image.open(path)
  x0,y0,x1,y1=data['crop'];iw,ih=im.size;panel_w=art.get('panel_w',data.get('largura_mm',210)*mm);panel_x=art.get('panel_x',(W-panel_w)/2);bottom=art.get('bottom',38*mm)
  wanted_h=panel_w*(y1-y0)/(x1-x0);available=art['top']-bottom
  if data.get('preservar_recorte'):
   assert wanted_h<=available+.1,(art['name'],'recorte não cabe',wanted_h,available)
   panel_h=wanted_h
  else:panel_h=min(available,wanted_h)
  scale=max(panel_w/(x1-x0),panel_h/(y1-y0));dx=panel_x-x0*scale;dy=bottom-(ih-y1)*scale+(panel_h-(y1-y0)*scale)/2
  c.saveState();clip=c.beginPath();clip.rect(panel_x,bottom,panel_w,panel_h);c.clipPath(clip,stroke=0)
  c.drawImage(ImageReader(im),dx,dy,width=iw*scale,height=ih*scale);c.restoreState()
  if data.get('borda',True):
   c.setStrokeColor(INK);c.setLineWidth(.65);c.rect(panel_x,bottom,panel_w,panel_h,stroke=1,fill=0)
  placements.append({'imagem':art['name'],'pagina':n,'x':round(panel_x,3),'y':round(bottom,3),'largura':round(panel_w,3),'altura':round(panel_h,3),'topo_texto_livre':round(art['top'],3),'crop':data['crop'],'pixels_recorte':[x1-x0,y1-y0],'dpi_efetivo':round(72/scale,1),'arquivo_original_preservado':True,'composicao':art.get('composicao','rodape'),'credito_x':round(panel_x if art.get('composicao','').startswith('lateral') else M,3),'credito_y':round(art.get('credit_y',34*mm),3)})
  c.setFont('Head',8.5);c.setFillColor(MUTED);c.drawString(panel_x if art.get('composicao','').startswith('lateral') else M,art.get('credit_y',34*mm),data['credito'])
 if page['kind']=='toc':
  c.setFont('Head',12);c.setFillColor(ACC)
  for key,right,y in page['toc_rows']:c.drawRightString(right,y+4,str(pagemap[key]))
 if page['kind']!='cover':
  nav=page.get('nav')
  if not nav:
   if ch['numero']==6:
    nav=[(group['blocks'][0].title,group['blocks'][0].key) for group in ch['grupos']]
    if any(getattr(part,'doc',None)=='incursor' for part,_,_,_,_,_,_ in page['draws']):nav=[('Caminho','incursor--inc-caminho'),('Assassino','incursor--inc-assassino'),('Pugilista','incursor--inc-pugilista'),('Malabarista','incursor--inc-malabarista')]
   else:nav=[('Sumário','sumario'),('Capítulo',ch['key']),('Índice','capitulo-21')]
  bw=AW/len(nav);ny=24*mm
  for j,(name,dest) in enumerate([] if page['kind']=='form' else nav):
   x=M+j*bw;active=name in page['group'];c.setFillColor(PALE if active else white);c.setStrokeColor(EDGE);c.setLineWidth(.65);c.rect(x,ny,bw,18,fill=1,stroke=1)
   size=min(10,10*(bw-8)/max(bw-8,d.pdfmetrics.stringWidth(name,'Head',10)));c.setFont('Head',size);c.setFillColor(ACC if active else MUTED);c.drawCentredString(x+bw/2,ny+5,name)
   c.linkRect('',dest,(x,ny,x+bw,ny+18),relative=0,thickness=0)
  c.setFont('Head',9);c.setFillColor(MUTED);c.drawString(M,14*mm,'CICLO MALDITO / LIVRO DE REGRAS')
  c.setFillColor(ACC);c.drawRightString(W-M,14*mm,str(n))
 c.showPage()
c.save()
manifest={'estudo_densidade':DENSITY,'pdf':str(PDF.relative_to(B)),'sha256_pdf':hashlib.sha256(PDF.read_bytes()).hexdigest(),'paginas':len(pages),'fontes':json.loads((B/'FONTES-REMOTAS.json').read_text()),'ancoras':{k:{'pagina':v[0],'x':v[1],'y':v[2]} for k,v in positions.items()},'capitulos':[{'numero':ch['numero'],'titulo':ch['titulo'],'pagina':pagemap[ch['key']]} for ch in chapters],'eventos':events,'conjuntos_informacao':information,'alteracoes_diagramacao':changes,'fontes_locais_r30':{k:{'arquivo':v,'sha256':g['source_hash'][k]} for k,v in g['order']['fontes'].items()},'alteracoes_regras':json.loads((B/'revisao-de-regras/ALTERACOES-REGRAS.json').read_text()),'creditos':{'pagina':pagemap['creditos'],'arquivo':'CREDITOS.json','autor':credits['autor']},'imagens':artdata,'posicionamento_imagens':placements,'capas_e_aberturas':cover_placements,'marcadores':{key:{'titulo':title,'nivel':level,'pagina':pagemap[key]} for key,(title,level) in outline.items()},'alteracoes_editoriais':g['publication_changes'],'paginas_planejadas':[{'pagina':p['numero'],'capitulo':p['chapter']['numero'],'tipo':p['kind'],'grupo':p['group'],'altura_conteudo':p.get('content_height')} for p in pages]}
manifest['revisao_r32']=json.loads((B/'revisao-de-compreensao/ESTADO-R32.json').read_text())
manifest['revisao_r37']={'base':'R36','etapa':'7C','registro':'correcoes-pente-fino/ALTERACOES-TEXTO.json','adicional':'Aberturas completas e primeira explicação útil, incluindo Muro'}
manifest['revisao_r36']={'base':'R35','origem':'Pente fino integral da R35 e respostas do autor em 08/10/2026','registro':'revisao-do-pente-fino/ALTERACOES.json','escopo':['PF011','PF014']}
manifest['revisao_r35']={'base':'R34','etapa':'6E','opcao':'B','classificacao':'revisao-de-hierarquia/CLASSIFICACAO.json','registro':'revisao-de-hierarquia/ALTERACOES-DIAGRAMACAO.json'}
manifest['revisao_r33']=json.loads((B/'revisao-de-continuidade/ESTADO-R33.json').read_text())
assert len(titulos_capitulo_aplicados)==21,titulos_capitulo_aplicados
manifest['revisao_r34']={'base':'R33','etapas':['6C.1','6D'],'estudo_capitulo':estudo_capitulo,'titulos_aplicados':titulos_capitulo_aplicados,'registro':'revisao-final/ALTERACOES-DIAGRAMACAO.json'}
(B/'FONTES-E-VALIDACAO.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
(B/'revisao-de-estrutura/FLUXO-COLUNAS.json').write_text(json.dumps(fluxo.flow_log,ensure_ascii=False,indent=2)+'\n')
(B/'revisao-de-continuidade/ABERTURAS.json').write_text(json.dumps(fluxo.opening_log,ensure_ascii=False,indent=2)+'\n')
manifest['revisao_estrutura']={'base':'R30','etapa':2,'fonte_corpo':S['body'].fontSize,'entrelinha_corpo':S['body'].leading,
 'blocos_transformados':len(g['structural_changes']),'hierarquia':'revisao-de-estrutura/HIERARQUIA.json',
 'registro_texto':'revisao-de-estrutura/ALTERACOES-ESTRUTURA.json','registro_diagramacao':'revisao-de-estrutura/ALTERACOES-DIAGRAMACAO.json',
 'criterio':'Colunas contínuas em cada região; estruturas largas separam regiões. Nomes, preços e regras preservados.'}
(B/'FONTES-E-VALIDACAO.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
print(PDF,len(pages),'páginas',len(events),'elementos',len(changes),'continuações necessárias',flush=True)

(B/'REGISTRO-TABELAS.json').write_text(json.dumps(list(registros_tabelas.values()),ensure_ascii=False,indent=2)+'\n')
(B/'REGISTRO-DESTAQUES.json').write_text(json.dumps(list(registros_destaques.values()),ensure_ascii=False,indent=2)+'\n')

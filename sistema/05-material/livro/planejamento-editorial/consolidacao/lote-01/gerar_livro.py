#!/usr/bin/env python3
"""Monta candidatas correntes sem editar suas fontes. Requer Python com ReportLab e pypdf.
Uso: python gerar_livro.py [--strict] [--passes 6]
Uma execução captura as fontes, cria Markdown único, converge páginas e registra cobertura.
"""
from pathlib import Path
from collections import Counter
from dataclasses import dataclass
from xml.sax.saxutils import escape
import argparse, hashlib, json, re, unicodedata, math, sys
from reportlab import rl_config
rl_config.invariant = 1
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle, KeepTogether
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.colors import HexColor, white
from reportlab.lib.enums import TA_LEFT, TA_RIGHT
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from pypdf import PdfReader
B=Path(__file__).resolve().parent; P=B.parents[1]; E=B/'evidencias'; OUT=B/'output/pdf'; E.mkdir(exist_ok=True);OUT.mkdir(parents=True,exist_ok=True)
args=argparse.ArgumentParser();args.add_argument('--strict',action='store_true');args.add_argument('--passes',type=int,default=6);opt=args.parse_args()
sha=lambda b:hashlib.sha256(b).hexdigest()
def save(n,data): (B/n).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
def norm(s):return re.sub(r'\s+',' ',unicodedata.normalize('NFKC',s)).strip().casefold()
order=json.loads((B/'ORDEM.json').read_text()); snapshots={k:(P/v).read_text() for k,v in order['fontes'].items()};source_hash={k:sha(t.encode()) for k,t in snapshots.items()}
paths={str(Path(v)):k for k,v in order['fontes'].items()}
@dataclass
class Block:
 doc:str
 anchor:str
 title:str
 text:str
 @property
 def key(self):return self.doc+'--'+self.anchor
blocks={};all_blocks={};link_issues=[]
for doc,text in snapshots.items():
 found=re.findall(r'<!-- page:([^|]+)\|([^>]+) -->\s*(.*?)(?=<!-- page:|\Z)',text,re.S)
 if not found:raise ValueError('Fonte sem blocos '+doc)
 blocks[doc]=[]
 for anchor,title,md in found:
  b=Block(doc,anchor.strip(),title.strip(),md.strip());assert b.key not in all_blocks,b.key
  assert b.text.splitlines()[0]=='# '+b.title,(doc,anchor,b.text[:100]);blocks[doc].append(b);all_blocks[b.key]=b

chapters=[];selection=[];part_rows=[]
for pi,part in enumerate(order['partes'],1):
 part_rows.append({'titulo':part['titulo'],'key':f'parte-{pi}'})
 for ch in part['capitulos']:
  ci=len(chapters)+1;entry={'titulo':ch['titulo'],'key':f'capitulo-{ci}','numero':ci,'parte':pi,'grupos':[]}
  for spec in ch['fontes']:
   doc=spec['documento'];want=spec.get('ancoras');omit=spec.get('excluir',[]);prefix=spec.get('prefixo');omit_prefixes=spec.get('excluir_prefixos',[])
   if want:
    unknown=set(want)-{b.anchor for b in blocks[doc]};assert not unknown,(doc,unknown)
   chosen=[b for b in blocks[doc] if (want is None or b.anchor in want) and b.anchor not in omit and (prefix is None or b.anchor.startswith(prefix)) and not any(b.anchor.startswith(p) for p in omit_prefixes)]
   assert chosen,(ch['titulo'],spec)
   entry['grupos'].append({'doc':doc,'blocks':chosen,'caminho':doc in ['bastiao','vanguarda','guia','emanador','evocador','incursor']})
   selection.extend(b.key for b in chosen)
  chapters.append(entry)
count=Counter(selection);assert len(count)==len(all_blocks) and set(count)==set(all_blocks),{'omitidos':list(set(all_blocks)-set(count)),'extras':list(set(count)-set(all_blocks))};assert all(v==1 for v in count.values()),'Blocos repetidos'

# R23 fornece destinos com identidade exata. Não inferir títulos nem usar páginas antigas.
mapfile=P/'consulta/lote-01/evidencias/DESTINOS.json';dest_snapshot=mapfile.read_text();dest_data=json.loads(dest_snapshot)
def destination(d,term):
 file=str(Path(d['arquivo']));doc=paths.get(file);key=(doc+'--'+d['ancora']) if doc else None
 if key not in all_blocks:
  link_issues.append({'origem':'DESTINOS.json','termo':term,'destino':d,'problema':'fonte/âncora não selecionada no livro'});return None
 # A raiz pode alterar títulos, mas identidade de arquivo/âncora é o contrato.
 return key
maps={kind:{row['termo']:{**row,'target':destination(row['destino'],row['termo'])} for row in dest_data.get(kind,[])} for kind in ['glossario','indice']}

def enrich(b):
 lines=b.text.splitlines();out=[]
 for line in lines:
  line=re.sub(r'\[([^\]]+)\]\(#([^)]+)\)',lambda m:'['+m[1]+'](#'+b.doc+'--'+m[2]+')',line)
  for target in re.findall(r'\]\(#([^)]+)\)',line):
   if target not in all_blocks:link_issues.append({'origem':b.key,'destino':target,'problema':'link interno sem bloco'})
  if b.doc=='consulta' and b.anchor.startswith('consulta-glossario-'):
   m=re.match(r'^\*\*(.*?)\.\*\*',line)
   if m:
    row=maps['glossario'].get(m[1])
    if row and row['target']:
     line=re.sub(r'(\*\*Consulta:\*\*\s*)(.*?)(\.)?$',lambda z:z[1]+'['+row['destino']['titulo']+'](#'+row['target']+').',line)
    elif not row:link_issues.append({'origem':b.key,'termo':m[1],'problema':'termo ausente no mapa de glossário'})
  if b.doc=='consulta' and b.anchor.startswith('consulta-indice-') and line.startswith('|'):
   cells=[x.strip() for x in line.strip('|').split('|')]
   if len(cells)==2 and cells[0] not in ['Assunto','---']:
    row=maps['indice'].get(cells[0])
    if row and row['target']:line='| '+cells[0]+' | ['+cells[1]+'](#'+row['target']+') |'
    elif not row:link_issues.append({'origem':b.key,'termo':cells[0],'problema':'termo ausente no mapa de índice'})
  out.append(line)
 return '\n'.join(out)
enriched={k:enrich(b) for k,b in all_blocks.items()};save('evidencias/DESTINOS-PENDENTES.json',link_issues)
if opt.strict and link_issues:raise ValueError(f'{len(link_issues)} destinos pendentes; consulte evidências')
(E/'fontes-capturadas').mkdir(exist_ok=True)
for key,text in snapshots.items(): (E/'fontes-capturadas'/f'{key}.md').write_text(text)

# Fonte única derivada: texto integral e destinos qualificados. Apenas hierarquia e remissões mudam.
md=['# Ciclo Maldito','', '> Candidata editorial reunida. Publicação v0.331 preservada.','']
map_chapter={};suppressed=[]
for ch in chapters:
 if ch['key']==next(c['key'] for c in chapters if c['parte']==ch['parte']):md.extend([f"<!-- parte:{ch['parte']} -->",f"# Parte {ch['parte']} — {part_rows[ch['parte']-1]['titulo']}",''])
 md.extend([f"<a id=\"{ch['key']}\"></a>",f"## {ch['numero']}. {ch['titulo']}",''])
 for gi,group in enumerate(ch['grupos']):
  for bi,b in enumerate(group['blocks']):
   map_chapter[b.key]={'parte':ch['parte'],'capitulo':ch['numero'],'titulo_capitulo':ch['titulo'],'fonte':order['fontes'][b.doc],'ancora_fonte':b.anchor,'titulo_bloco':b.title}
   md.extend([f'<!-- fonte:{order["fontes"][b.doc]}#{b.anchor} -->',f'<a id="{b.key}"></a>'])
   text=enriched[b.key]
   duplicate=(gi==0 and bi==0 and norm(b.title)==norm(ch['titulo']))
   if duplicate:suppressed.append(b.key);text='\n'.join(text.splitlines()[1:]).lstrip()
   text=re.sub(r'^(#{1,6}) ',lambda m:'#'*(len(m[1])+2)+' ',text,flags=re.M)
   md.extend([text,''])
(B/'LIVRO-COMPLETO.md').write_text('\n'.join(md)+'\n')

FONT=(B/'fontes-tipograficas')
for n,f in [('Body','Spectral-Regular.ttf'),('Body-Bold','Spectral-SemiBold.ttf'),('Body-Italic','Spectral-Italic.ttf'),('Head','BarlowCondensed-SemiBold.ttf')]:pdfmetrics.registerFont(TTFont(n,str(FONT/f)))
pdfmetrics.registerFontFamily('Body',normal='Body',bold='Body-Bold',italic='Body-Italic',boldItalic='Body-Bold')
W,H=A4;M=19*mm;AW=W-2*M;INK=HexColor('#251727');ACC=HexColor('#BC2A6E');PALE=HexColor('#FDF0F6');RULE=HexColor('#ECC3D6');MUTED=HexColor('#65545F')
ST={
 'body':ParagraphStyle('body',fontName='Body',fontSize=10.25,leading=14,textColor=INK,spaceAfter=5.8,allowWidows=0,allowOrphans=0),
 'chapter':ParagraphStyle('chapter',fontName='Head',fontSize=29,leading=32,textColor=INK,spaceAfter=13,keepWithNext=True),
 'part':ParagraphStyle('part',fontName='Head',fontSize=12,leading=15,textColor=ACC,spaceAfter=5,keepWithNext=True),
 'path':ParagraphStyle('path',fontName='Head',fontSize=27,leading=30,textColor=INK,spaceBefore=10,spaceAfter=11,keepWithNext=True),
 'section':ParagraphStyle('section',fontName='Head',fontSize=19,leading=22,textColor=INK,spaceBefore=13,spaceAfter=6,keepWithNext=True),
 'sub':ParagraphStyle('sub',fontName='Head',fontSize=14,leading=16,textColor=INK,spaceBefore=8,spaceAfter=4,keepWithNext=True),
 'note':ParagraphStyle('note',fontName='Body',fontSize=9.8,leading=13,textColor=INK,spaceAfter=0,allowWidows=0,allowOrphans=0),
 'list':ParagraphStyle('list',fontName='Body',fontSize=10.25,leading=14,textColor=INK,leftIndent=12,firstLineIndent=-12,spaceAfter=5,allowWidows=0,allowOrphans=0),
 'cell':ParagraphStyle('cell',fontName='Body',fontSize=9.2,leading=11.8,textColor=INK,spaceAfter=0),
 'headcell':ParagraphStyle('headcell',fontName='Head',fontSize=10.5,leading=12,textColor=white),
 'toc':ParagraphStyle('toc',fontName='Body',fontSize=10.2,leading=14,textColor=INK,spaceAfter=2),
 'tocpath':ParagraphStyle('tocpath',fontName='Body',fontSize=9.3,leading=12,textColor=MUTED,leftIndent=12),
 'tocpart':ParagraphStyle('tocpart',fontName='Head',fontSize=14,leading=17,textColor=ACC,spaceBefore=10,spaceAfter=4,keepWithNext=True),
 'cover':ParagraphStyle('cover',fontName='Head',fontSize=54,leading=57,textColor=INK,spaceAfter=20),
}

page_map={};events=[];page_context={};current_chapter='';current_part='';current_source='';current_block='';passno=0

def inline(s):
 # Markdown links are protected before emphasis, since their labels may be bold.
 tokens=[]
 def link(m):
  label,target=m.groups();num=page_map.get(target);suffix=f' (p. {num})' if num else ''
  val='<link href="#'+target+'" color="#BC2A6E">'+escape(label)+suffix+'</link>' if target in all_blocks else escape(label)
  tokens.append(val);return f'ZZLINK{len(tokens)-1}ZZ'
 s=re.sub(r'\[([^\]]+)\]\(#([^)]+)\)',link,s);s=escape(s)
 s=re.sub(r'\*\*(.+?)\*\*',r'<b>\1</b>',s);s=re.sub(r'`([^`]+)`',r'<b>\1</b>',s);s=re.sub(r'(?<!\*)\*([^*]+)\*(?!\*)',r'<i>\1</i>',s)
 for i,v in enumerate(tokens):s=s.replace(f'ZZLINK{i}ZZ',v)
 return s

class Book(SimpleDocTemplate):
 def afterFlowable(self,f):
  global current_chapter,current_part,current_source,current_block
  if hasattr(f,'keys'):
   for key in f.keys:
    y=min(H-21*mm,self.frame._y+getattr(f,'height',0)+f.getSpaceAfter()); self.canv.bookmarkHorizontalAbsolute(key,y);self.pages[key]=self.page
    events.append({'ancora':key,'pagina':self.page,'y':round(y,2)})
  if hasattr(f,'chapter_title'):current_chapter=f.chapter_title
  if hasattr(f,'part_title'):current_part=f.part_title
  if hasattr(f,'source_doc'):current_source=f.source_doc
  if hasattr(f,'block_key'):current_block=f.block_key
  if hasattr(f,'outline'):
   title,key,level=f.outline;self.canv.addOutlineEntry(title,key,level=level,closed=True)
  if current_block and isinstance(f,(Paragraph,Table)) and not hasattr(f,'part_title') and not (hasattr(f,'chapter_title') and not hasattr(f,'block_key')): self.block_pages.setdefault(current_block,set()).add(self.page)
 def afterPage(self): decorations(self.canv,self)

def decorations(c,doc):
 if doc.page==1:return
 c.saveState();c.setStrokeColor(RULE);c.setLineWidth(.5);c.line(M,H-14*mm,W-M,H-14*mm);c.line(M,16*mm,W-M,16*mm)
 c.setFillColor(ACC);c.setFont('Head',9);c.drawString(M,H-11*mm,'CICLO MALDITO')
 c.setFillColor(MUTED);c.setFont('Head',8);label=current_chapter.upper() if current_chapter else 'SUMÁRIO';c.drawRightString(W-M,H-11*mm,label)
 c.drawString(M,11*mm,'CANDIDATA EDITORIAL • BASE v0.331');c.setFillColor(ACC);c.setFont('Head',11);c.drawRightString(W-M,10.5*mm,str(doc.page));c.restoreState()

def widths(rows):
 n=len(rows[0]);head=rows[0]
 if head==['Arma','Mãos','Dano','Propriedades','Força','Volume','Preço (¥)']:w=[.19,.06,.14,.30,.06,.08,.17]
 elif head[0] in ('Nível','Classe','Classe real','Classe da especial') and n>=7:
  w=[.17]+[.83/(n-1)]*(n-1)
 elif n==2:
  # Index needs room for qualified destination, field sheets for writing.
  w=[.34,.66] if head[0]=='Assunto' else [.30,.70]
 elif n==3:
  if head[0].startswith('Classe d') and head[-1].startswith('Ajuste'):w=[.49,.35,.16]
  elif head[0]=='Grau':w=[.13,.64,.23]
  elif head[0]=='Ofício':w=[.20,.21,.59]
  elif head[0] in ['Melhoria']:w=[.25,.65,.10]
  elif head[0]=='TR':w=[.16,.24,.60]
  elif head[0]=='Porte e exemplo':w=[.64,.18,.18]
  else:w=[.31,.31,.38]
 elif n==4:
  if head[0]=='Item':w=[.28,.43,.16,.13]
  elif head[0]=='Arma e carga correspondente':w=[.44,.21,.19,.16]
  elif head[0]=='Nível':w=[.14,.28,.30,.28]
  elif head[0]=='Forma':w=[.20,.22,.29,.29]
  else:w=[.25]*4
 elif n==5:
  w=[.22,.23,.22,.18,.15] if head[0]=='Item' else [1/n]*n
 elif n==6:w=[.16,.20,.19,.15,.15,.15]
 else:w=[1/n]*n
 assert len(w)==n and abs(sum(w)-1)<1e-6,(head,w)
 return [AW*x for x in w]

class TabelaSemOrfa(Table):
 # Uma quebra de página não deixa só o cabeçalho e uma linha no pé, nem uma linha sozinha sob o cabeçalho repetido.
 MINIMO=2
 def split(self,availWidth,availHeight):
  r=Table.split(self,availWidth,availHeight)
  if len(r)!=2:return r
  h=self.repeatRows;a=len(r[0]._cellvalues)-h;b=len(r[1]._cellvalues)-h
  if a<self.MINIMO:return []
  if b<self.MINIMO:
   k=self.MINIMO-b
   if a-k<self.MINIMO:return []
   r=Table.split(self,availWidth,sum(self._rowHeights[:h+a-k+1])-0.01)
  return r

class GrupoComTabela(KeepTogether):
 # Título e linhas que apresentam uma tabela ou um parágrafo seguem com o começo dele: cabeçalho e duas linhas da tabela, ou duas linhas do texto. O resto pode quebrar.
 def split(self,aW,aH):
  t=self._content[-1]
  if not getattr(t,'apresentada',False):return KeepTogether.split(self,aW,aH)
  C=self._content;th=t.wrap(aW,H)[1]
  # Peça curta demais para quebrar sem deixar sobra de uma linha precisa caber inteira.
  m=TabelaSemOrfa.MINIMO
  if isinstance(t,TabelaSemOrfa):first=th if len(t._rowHeights)-t.repeatRows<2*m else sum(t._rowHeights[:t.repeatRows+m])
  elif isinstance(t,Paragraph):first=th if round(th/t.style.leading)<2*m else m*t.style.leading
  else:first=th
  # Mesma conta do quadro: alturas, e entre dois elementos o maior dos espaços que se encostam.
  need=sum(f.wrap(aW,H)[1] for f in C[:-1])+sum(max(C[i].getSpaceAfter(),C[i+1].getSpaceBefore()) for i in range(len(C)-1))+first
  if aH+0.01>=need:return C[:]
  return KeepTogether.split(self,aW,aH)

def make_table(lines):
 rows=[[v.strip() for v in line.strip().strip('|').split('|')] for line in lines];rows=[r for r in rows if not all(re.match(r'^:?-+:?$',v) for v in r)]
 n=len(rows[0]);assert all(len(r)==n for r in rows),(current_block,rows)
 ps=[[Paragraph(inline(v),ST['headcell' if j==0 else 'cell']) for v in r] for j,r in enumerate(rows)]
 t=TabelaSemOrfa(ps,colWidths=widths(rows),repeatRows=1,hAlign='LEFT',spaceBefore=3,spaceAfter=9,splitByRow=1)
 t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),INK),('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),4),('RIGHTPADDING',(0,0),(-1,-1),4),('TOPPADDING',(0,0),(-1,-1),4),('BOTTOMPADDING',(0,0),(-1,-1),4),('ROWBACKGROUNDS',(0,1),(-1,-1),[white,PALE]),('LINEBELOW',(0,1),(-1,-1),.35,RULE)]));return t

INTEIROS={'geral--energia-exemplo','guia--guia-emergencia-cuidado','emanador--ema-fluxo','consulta--consulta-entidades','incursor--inc-perfeita'}

def add_blocks(story,b,style='section',duplicate=False,outline=None):
 lines=enriched[b.key].splitlines();i=0;attached=False;start=len(story)
 compact=b.key=='consulta--consulta-ficha-repertorio'
 body_style=ParagraphStyle('ficha-body',parent=ST['body'],leading=13,spaceAfter=4) if compact else ST['body']
 sub_style=ParagraphStyle('ficha-sub',parent=ST['sub'],spaceBefore=6,spaceAfter=3) if compact else ST['sub']
 while i<len(lines):
  s=lines[i].strip();i+=1
  if not s or s=='---':continue
  if s.startswith('|'):
   group=[s]
   while i<len(lines) and lines[i].strip().startswith('|'):group.append(lines[i].strip());i+=1
   f=make_table(group)
   if compact:
    f.setStyle(TableStyle([('TOPPADDING',(0,0),(-1,-1),2.5),('BOTTOMPADDING',(0,0),(-1,-1),2.5)]));f.spaceAfter=6
   # Título seguido de até quatro linhas e da tabela: essas linhas vão junto, como o título já ia.
   if b.key not in INTEIROS:
    j=len(story);linhas=0
    while j-1>start and isinstance(story[j-1],Paragraph) and story[j-1].style.name in ('body','ficha-body','list'):
     linhas+=round(story[j-1].wrap(AW,H)[1]/story[j-1].style.leading);j-=1
    if j<len(story) and linhas<=4 and j-1>=start and isinstance(story[j-1],Paragraph) and getattr(story[j-1].style,'keepWithNext',0):
     for x in story[j:]:x.keepWithNext=True
     f.apresentada=True
  elif s.startswith('# '):
   if duplicate:continue
   f=Paragraph(inline(s[2:]),ST[style]);f.keys=[b.key];f.block_key=b.key;f.source_doc=b.doc;attached=True
   if outline:f.outline=(s[2:],b.key,outline)
  elif s.startswith('## '):f=Paragraph(inline(s[3:]),sub_style)
  elif s.startswith('> '):
   p=Paragraph(inline(s[2:]),ST['note']);f=Table([[p]],colWidths=[AW],hAlign='LEFT',spaceBefore=3,spaceAfter=9)
   f.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,-1),PALE),('LINEBEFORE',(0,0),(-1,-1),2,ACC),('LEFTPADDING',(0,0),(-1,-1),11),('RIGHTPADDING',(0,0),(-1,-1),10),('TOPPADDING',(0,0),(-1,-1),8),('BOTTOMPADDING',(0,0),(-1,-1),8)]))
  elif s.startswith('- '):f=Paragraph(inline('• '+s[2:]),ST['list'])
  elif re.match(r'^\d+\. ',s):f=Paragraph(inline(s),ST['list'])
  else:f=Paragraph(inline(s),body_style)
  # Keep short identifying lines with the actual rule or table they introduce.
  if (b.key=='incursor--inc-redirecionar' and s=='**Nível 27.**') or (b.key=='equip--eqa-tiro' and s=='Treino simples. Bestas de uma ou duas mãos.') or (b.key=='equip--eqf-acessorios' and s.startswith('**Roupa comum. Grau 3. Efeito: Perene.**')):
   f.keepWithNext=True
  # Título com uma linha só embaixo (como a linha de uso de uma habilidade): a linha segue com o começo do texto seguinte.
  if b.key not in INTEIROS and not getattr(f,'apresentada',False) and isinstance(f,(Paragraph,TabelaSemOrfa)) and len(story)-start>=2 and isinstance(story[-1],Paragraph) and story[-1].style.name in ('body','ficha-body','list') and isinstance(story[-2],Paragraph) and getattr(story[-2].style,'keepWithNext',0) and not getattr(story[-1],'keepWithNext',0) and round(story[-1].wrap(AW,H)[1]/story[-1].style.leading)<=1:
   story[-1].keepWithNext=True;f.apresentada=True
  f.source_block=b.key;story.append(f)
 assert attached or duplicate,b.key
 # Complete closing units replace isolated tails before a chapter/page break.
 if b.key in INTEIROS:
  story[start:]=[KeepTogether(story[start:])]

def toc_row(label,key,style='toc'):
 num=str(page_map.get(key,'—'));left=Paragraph('<link href="#'+key+'">'+escape(label)+'</link>',ST[style]);right=Paragraph('<link href="#'+key+'">'+num+'</link>',ParagraphStyle('tocnum',parent=ST[style],alignment=TA_RIGHT))
 tb=Table([[left,right]],colWidths=[AW-12*mm,12*mm],hAlign='LEFT');tb.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),0),('RIGHTPADDING',(0,0),(-1,-1),0),('TOPPADDING',(0,0),(-1,-1),1.3),('BOTTOMPADDING',(0,0),(-1,-1),1.3)]));return tb

def story():
 st=[Spacer(1,42*mm),Paragraph('CICLO MALDITO',ST['cover']),Paragraph('Livro de regras',ParagraphStyle('cover-sub',parent=ST['chapter'],fontSize=27,leading=30)),Spacer(1,8*mm),Paragraph('RPG de mesa no universo de Jujutsu Kaisen',ST['body']),Spacer(1,12*mm),Paragraph('Candidata editorial reunida',ST['part']),Paragraph('Texto em revisão • publicação v0.331 preservada',ST['body']),PageBreak(),Paragraph('Sumário',ST['chapter'])]
 for part in part_rows:
  p=Paragraph(escape(part['titulo']),ST['tocpart']);st.append(p)
  for ch in [c for c in chapters if part_rows[c['parte']-1]['key']==part['key']]:
   st.append(toc_row(f"{ch['numero']}. {ch['titulo']}",ch['key']))
   for g in ch['grupos']:
    if g['caminho']:st.append(toc_row(g['blocks'][0].title,g['blocks'][0].key,'tocpath'))
 previous_part=None
 for ch in chapters:
  st.append(PageBreak())
  if ch['parte']!=previous_part:
   pr=part_rows[ch['parte']-1];f=Paragraph(f"PARTE {ch['parte']} • "+escape(pr['titulo']).upper(),ST['part']);f.keys=[pr['key']];f.outline=(pr['titulo'],pr['key'],0);f.part_title=pr['titulo'];st.append(f);previous_part=ch['parte']
  f=Paragraph(f"{ch['numero']}. "+escape(ch['titulo']),ST['chapter']);f.keys=[ch['key']];f.outline=(f"{ch['numero']}. {ch['titulo']}",ch['key'],1);f.chapter_title=ch['titulo']
  first=ch['grupos'][0]['blocks'][0]
  if first.key in suppressed:f.keys.append(first.key);f.block_key=first.key;f.source_doc=first.doc
  st.append(f)
  for gi,g in enumerate(ch['grupos']):
   if g['caminho'] and gi>0:st.append(PageBreak())
   for bi,b in enumerate(g['blocks']):
    if b.doc=='consulta' and b.anchor.startswith('consulta-ficha-') and not (gi==0 and bi==0):st.append(PageBreak())
    add_blocks(st,b,style='path' if g['caminho'] and bi==0 else 'section',duplicate=b.key in suppressed,outline=2 if g['caminho'] and bi==0 else None)
 return st

pdf=OUT/'Projeto-M-Livro-Completo-Candidata.pdf';previous=None;pass_reports=[]
for passno in range(1,opt.passes+1):
 events=[];current_chapter='';current_part='';current_source='';current_block=''
 doc=Book(str(pdf),pagesize=A4,leftMargin=M,rightMargin=M,topMargin=21*mm,bottomMargin=21*mm,title='Ciclo Maldito — Livro de regras — candidata editorial',author='Ciclo Maldito',pageCompression=1)
 doc.pages={};doc.block_pages={};doc.keepTogetherClass=GrupoComTabela
 doc.build(story())
 fresh=doc.pages;pass_reports.append({'passagem':passno,'paginas':doc.page,'destinos':len(fresh),'mapa_estavel':fresh==page_map})
 print(json.dumps(pass_reports[-1],ensure_ascii=False),flush=True)
 if fresh==page_map:break
 page_map=fresh
else:raise RuntimeError('Paginação não convergiu no máximo de passagens')

mapped=[]
for k in selection:
 b=all_blocks[k];x={**map_chapter[k],'id_livro':k,'pagina':page_map[k],'paginas_conteudo':sorted(doc.block_pages.get(k,{page_map[k]})),'sha256_bloco_fonte':sha(b.text.encode()),'cabecalho_inicial_unificado':k in suppressed};mapped.append(x)
current_hash={k:sha((P/v).read_bytes()) for k,v in order['fontes'].items()};changed=[k for k in source_hash if source_hash[k]!=current_hash[k]]
report={'status':'primeira prova; não aprovada visualmente','sha256_gerador':sha(Path(__file__).read_bytes()),'sha256_ordem':sha((B/'ORDEM.json').read_bytes()),'fontes_tipograficas':{f.name:sha(f.read_bytes()) for f in FONT.glob('*.ttf') if f.name in ['Spectral-Regular.ttf','Spectral-SemiBold.ttf','Spectral-Italic.ttf','BarlowCondensed-SemiBold.ttf']},'fontes':{k:{'arquivo':v,'sha256_lido':source_hash[k],'sha256_no_fim':current_hash[k]} for k,v in order['fontes'].items()},'fontes_mudaram_durante_geracao':changed,'destinos_sha256':sha(dest_snapshot.encode()),'destinos_mudaram_durante_geracao':mapfile.read_text()!=dest_snapshot,'blocos_esperados':len(all_blocks),'blocos_incluidos':len(selection),'omitidos':[],'duplicados':[],'partes':len(part_rows),'capitulos':len(chapters),'caminhos':sum(g['caminho'] for c in chapters for g in c['grupos']),'paginas':doc.page,'passagens':pass_reports,'destinos_pendentes':len(link_issues),'sha256_manuscrito':sha((B/'LIVRO-COMPLETO.md').read_bytes()),'sha256_pdf':sha(pdf.read_bytes()),'V14':'não executado: requer inspeção visual de todas as páginas finais'}
save('evidencias/GERACAO.json',report);save('evidencias/MAPA-BLOCOS.json',mapped);save('evidencias/PAGINAS-DESTINOS.json',page_map);save('evidencias/EVENTOS-ANCORAS.json',events)
print(json.dumps({k:v for k,v in report.items() if k not in ['fontes','passagens']},ensure_ascii=False),flush=True)
if opt.strict and (changed or report['destinos_mudaram_durante_geracao']): raise RuntimeError('Fontes mudaram durante a captura; repetir a geração.')

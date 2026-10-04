from pathlib import Path
from xml.sax.saxutils import escape
import re, json
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle, KeepTogether
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.colors import HexColor, Color, white
from reportlab.lib.enums import TA_LEFT
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.graphics.shapes import Drawing, Line, Rect, String, Circle
from pypdf import PdfReader
B=Path(__file__).resolve().parent
F=Path('/home/mizuki/.local/share/fonts/manual')
for name,file in [('Body','Spectral-Regular.ttf'),('Body-Bold','Spectral-SemiBold.ttf'),('Body-Italic','Spectral-Italic.ttf'),('Head','BarlowCondensed-SemiBold.ttf')]:
 pdfmetrics.registerFont(TTFont(name,str(F/file)))
pdfmetrics.registerFontFamily('Body',normal='Body',bold='Body-Bold',italic='Body-Italic',boldItalic='Body-Bold')
INK=HexColor('#251727'); ACC=HexColor('#BC2A6E'); PALE=HexColor('#FDF0F6'); LINE=HexColor('#ECC3D6'); MUTED=HexColor('#65545F')
W,H=A4; M=20*mm; avail=W-2*M
styles={
'p':ParagraphStyle('Body',fontName='Body',fontSize=10.25,leading=13.7,textColor=INK,spaceAfter=5.8,allowWidows=0,allowOrphans=0),
'h1':ParagraphStyle('Title',fontName='Head',fontSize=28,leading=30.5,textColor=INK,spaceAfter=12,keepWithNext=True),
'h2':ParagraphStyle('Sub',fontName='Head',fontSize=16,leading=18,textColor=INK,spaceBefore=7,spaceAfter=4,keepWithNext=True),
'note':ParagraphStyle('Note',fontName='Body',fontSize=9.8,leading=13,textColor=INK,spaceAfter=0),
'cell':ParagraphStyle('Cell',fontName='Body',fontSize=9.25,leading=12,textColor=INK),
'headcell':ParagraphStyle('HeadCell',fontName='Head',fontSize=11,leading=12,textColor=white),
'num':ParagraphStyle('Num',fontName='Body',fontSize=10.25,leading=13.7,textColor=INK,leftIndent=13,firstLineIndent=-13,spaceAfter=6),
}
import sys
sys.path.insert(0,str(B.parents[1]/'validacao-editorial'))
from conferir_editorial import assert_exportable
assert_exportable(B/'MUNICAO.md')
META=json.loads((B/'ESTRUTURA.json').read_text())
PAGE=META['paginas']

def fmt(s):
 s=escape(s)
 s=re.sub(r'\*\*(.+?)\*\*',r'<b>\1</b>',s)
 s=re.sub(r'\[([^\]]+)\]\(#([^)]+)\)',lambda m: '<link href="#'+m[2]+'" color="#BC2A6E">'+m[1]+' (p. '+str(PAGE[m[2]])+')</link>',s)
 return s
class Doc(SimpleDocTemplate):
 def afterFlowable(self,flow):
  if isinstance(flow,Paragraph) and flow.style.name=='Title':
   key=flow.section_key; group=next((name,keys) for name,keys in META['grupos'] if key in keys)
   self.canv.bookmarkPage(key)
   if len(group[1])==1:self.canv.addOutlineEntry(flow.getPlainText(),key,level=0,closed=True)
   else:
    if key==group[1][0]:
     self.canv.bookmarkPage('grupo-'+key);self.canv.addOutlineEntry(group[0],'grupo-'+key,level=0,closed=True)
    self.canv.addOutlineEntry(flow.getPlainText(),key,level=1,closed=True)


def decorate(c,doc):
 c.saveState(); c.setStrokeColor(LINE); c.setLineWidth(.5)
 c.line(M,H-14*mm,W-M,H-14*mm)
 c.setFillColor(ACC);c.setFont('Head',9);c.drawString(M,H-11*mm,'PROJETO - M')
 c.setFillColor(MUTED);c.setFont('Head',8);c.drawRightString(W-M,H-11*mm,'MUNIÇÃO')
 c.line(M,16*mm,W-M,16*mm)
 c.setFont('Head',8);c.drawString(M,11*mm,'PROPOSTA EM DISCUSSÃO  |  BASE v0.331')
 c.setFillColor(ACC);c.setFont('Head',12);c.drawRightString(W-M,10.5*mm,str(doc.page))
 c.restoreState()

def table(lines):
 rows=[[v.strip() for v in line.strip().strip('|').split('|')] for line in lines]
 rows=[r for r in rows if not all(re.match(r'^:?-+:?$',s) for s in r)]
 cols=len(rows[0]); widths=([avail*.25,avail*.29,avail*.19,avail*.15,avail*.12] if cols==5 else [avail*.49,avail*.19,avail*.18,avail*.14])
 paras=[[Paragraph(fmt(s),styles['headcell' if n==0 else 'cell']) for s in row] for n,row in enumerate(rows)]
 t=Table(paras,colWidths=widths,repeatRows=1,hAlign='LEFT')
 t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),INK),('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),8),('RIGHTPADDING',(0,0),(-1,-1),8),('TOPPADDING',(0,0),(-1,-1),4),('BOTTOMPADDING',(0,0),(-1,-1),4),('ROWBACKGROUNDS',(0,1),(-1,-1),[white,PALE]),('LINEBELOW',(0,1),(-1,-1),.4,LINE)]))
 return t

src=(B/'MUNICAO.md').read_text()
parts=re.split(r'<!-- page:([^|]+)\|([^>]+) -->\s*',src)
story=[]
for pi in range(1,len(parts),3):
 key,label,md=parts[pi:pi+3]
 if pi>1:story.append(PageBreak())
 lines=md.splitlines();i=0
 while i<len(lines):
  s=lines[i].strip()
  if not s:i+=1;continue
  if s.startswith('|'):
   block=[]
   while i<len(lines) and lines[i].strip().startswith('|'):block.append(lines[i]);i+=1
   story += [Spacer(1,3),table(block),Spacer(1,9)];continue
  if s.startswith('# '):
   title=Paragraph(fmt(s[2:]),styles['h1']);title.section_key=key;story.append(title)
  elif s.startswith('## '):story.append(Paragraph(fmt(s[3:]),styles['h2']))
  elif s.startswith('> '):
   p=Paragraph(fmt(s[2:]),styles['note']);t=Table([[p]],colWidths=[avail]);t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,-1),PALE),('LINEBEFORE',(0,0),(-1,-1),2,ACC),('LEFTPADDING',(0,0),(-1,-1),11),('RIGHTPADDING',(0,0),(-1,-1),10),('TOPPADDING',(0,0),(-1,-1),8),('BOTTOMPADDING',(0,0),(-1,-1),8)]));story.extend([Spacer(1,3),t,Spacer(1,9)])
  elif re.match(r'^\d+\. ',s): story.append(Paragraph(fmt(s),styles['num']))
  else:story.append(Paragraph(fmt(s),styles['p']))
  i+=1
 while story and isinstance(story[-1],Spacer):story.pop()
out=B/'output/pdf/Projeto-M-Municao-Proposta-05.pdf'
Doc(str(out),pagesize=A4,leftMargin=M,rightMargin=M,topMargin=21*mm,bottomMargin=21*mm,title='Projeto - M | Munição, proposta 5',author='Projeto - M',pageCompression=1).build(story,onFirstPage=decorate,onLaterPages=decorate)
r=PdfReader(out)
def flatten_outline(nodes):
 for node in nodes:
  if isinstance(node,list):yield from flatten_outline(node)
  else:yield node
res={'paginas':len(r.pages),'marcadores_principais':len([x for x in r.outline if not isinstance(x,list)]),'marcadores_totais':len(list(flatten_outline(r.outline))),'grupos_recolhidos':1,'caracteres':[len(p.extract_text()) for p in r.pages]}
(B/'evidencias').mkdir(exist_ok=True)
(B/'evidencias/pdf-texto.txt').write_text('\n\n'.join(f'PÁGINA {i+1}\n'+p.extract_text() for i,p in enumerate(r.pages)))
(B/'evidencias/pdf-estrutura.json').write_text(json.dumps(res,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(res))

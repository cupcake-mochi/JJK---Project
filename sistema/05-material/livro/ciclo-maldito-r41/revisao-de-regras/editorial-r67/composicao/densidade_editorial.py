"""Hierarquia B+C aprovada e parâmetros isolados de densidade para simulações."""
from pathlib import Path
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import HexColor,white
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Flowable,Paragraph,Table,TableStyle

ACC=HexColor('#9e2358');PALE=HexColor('#f8f1f4');INK=HexColor('#251727')

def configurar(S,B,d,r,cfg):
    for name,file in [('Entry','/home/mizuki/.fonts/BreeSerif.ttf'),('Strong','/home/mizuki/.local/share/fonts/manual/BarlowCondensed-Bold.ttf'),('Meta','/home/mizuki/.local/share/fonts/manual/IBMPlexMono-Medium.ttf')]:
        pdfmetrics.registerFont(TTFont(name,file))
    def apply(styles):
        styles['body']=ParagraphStyle('density-body',parent=styles['body'],fontSize=cfg['body'],leading=cfg['leading'],spaceAfter=cfg['gap'])
        styles['note']=ParagraphStyle('density-note',parent=styles['note'],fontSize=cfg['note'],leading=cfg['note_leading'])
        for kind,font,size,lead,color in [('major','Strong',32,36,ACC),('h1','Strong',21,24,ACC),('h2','Entry',16,20,INK),('h3','Head',13,16,ACC)]:
            styles[kind]=ParagraphStyle('density-'+kind,parent=styles[kind],fontName=font,fontSize=size,leading=lead,textColor=color)
        styles['compactmajor']=ParagraphStyle('density-compactmajor',parent=styles['major'],spaceAfter=4)
        styles['cost']=ParagraphStyle('density-cost',parent=styles['body'],fontName='Meta',fontSize=9.3,leading=12,spaceAfter=3,textColor=ACC)
        styles['small']=ParagraphStyle('density-context',parent=styles['small'],fontName='Head',fontSize=9,leading=12,textColor=ACC)
        styles['marker']=styles['small']
        styles['headcell']=ParagraphStyle('density-headcell',parent=styles['headcell'],textColor=ACC)
    apply(S)
    if r.S is not S:apply(r.S)
    for m in [d,r]:m.ACC=ACC;m.PALE=PALE
    return ACC,PALE

class Titulo(Flowable):
    def __init__(self,part,width,ns):
        super().__init__();self.part=part;self.ns=ns;self.width=width
        kind=part.kind;self.family=kind=='h1' and getattr(part,'role',None)=='Família'
        text=str(part.text).upper() if self.family or kind in ['major','compactmajor'] else part.text
        self.p=Paragraph(ns['inline'](text,part.doc),ns['S'][kind])
    def wrap(self,w,h):
        self.width=w;_,self.height=self.p.wrap(w-3 if self.family else w,h)
        return self.width,self.height
    def draw(self):
        c=self.canv;c.saveState();w=self.width;h=self.height
        if self.family:
            c.setFillColor(PALE);c.rect(-5,-2,w+5,h+4,fill=1,stroke=0)
            c.setFillColor(ACC);c.rect(-5,-2,2,h+4,fill=1,stroke=0)
        self.p.drawOn(c,3 if self.family else 0,0)
        c.setStrokeColor(ACC)
        if self.part.kind=='h2':c.setLineWidth(.75);c.line(0,-1,min(w,44),-1)
        elif self.part.kind in ['major','compactmajor']:c.setLineWidth(1);c.line(0,-3,w,-3)
        c.restoreState()

def instalar_partes(Part,ns):
    original=Part.make
    def make(self,w):
        S=ns['S'];cfg=ns['DENSITY'];inline=ns['inline']
        if self.kind in ['major','compactmajor','h1','h2','h3']:
            st=S[self.kind];return Titulo(self,w,ns),st.spaceBefore,st.spaceAfter
        if self.kind=='table':
            rows=self.text;data=[];commands=[]
            for i,row in enumerate(rows):
                category=i>0 and all(not v for v in row[1:])
                st=S['headcell' if i==0 else 'cell']
                if category:
                    st=ParagraphStyle('density-category',parent=S['cell'],fontName='Head',textColor=ACC)
                    commands.extend([('SPAN',(0,i),(-1,i)),('BACKGROUND',(0,i),(-1,i),PALE)])
                data.append([Paragraph(inline(v,self.doc),st) for v in row])
            t=Table(data,colWidths=[w*f for f in ns['fractions'](rows)],repeatRows=1,hAlign='LEFT')
            t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),PALE),('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),6),('RIGHTPADDING',(0,0),(-1,-1),6),('TOPPADDING',(0,0),(-1,-1),4),('BOTTOMPADDING',(0,0),(-1,-1),4),('LINEBELOW',(0,0),(-1,0),.8,ACC),('LINEBELOW',(0,1),(-1,-2),.25,HexColor('#ded4d9')),('LINEBELOW',(0,-1),(-1,-1),.5,ACC)]+commands))
            return t,8,10
        if self.kind=='note':
            t=Table([[Paragraph(inline(self.text,self.doc),S['note'])]],colWidths=[w])
            t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,-1),PALE),('LINEBEFORE',(0,0),(0,0),2,ACC),('LEFTPADDING',(0,0),(-1,-1),9),('RIGHTPADDING',(0,0),(-1,-1),9),('TOPPADDING',(0,0),(-1,-1),8),('BOTTOMPADDING',(0,0),(-1,-1),8)]))
            return t,4,8
        return original(self,w)
    Part.make=make

"""Hierarquia intermediária B aprovada: grupo, subtópico e exemplo.

A classificação é explícita por bloco e título. Não altera Markdown, nomes,
parágrafos ou mecânicas; conserva o estilo de entrada para capacidades nomeadas.
"""
import json
from reportlab.platypus import Flowable, Paragraph
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.colors import HexColor

class TituloIntermediario(Flowable):
    def __init__(self, part, width, ns, role):
        super().__init__();self.part=part;self.width=width;self.role=role
        configs={
            'grupo':('Strong',16,19,11,7,'#522039'),
            'subtopico':('Strong',15,18,0,4,'#9e2358'),
            'exemplo':('Entry',13.5,16.5,0,2.5,'#251727'),
            'entrada':('Entry',16,20,0,0,'#251727'),
        }
        font,size,lead,self.inset,self.extra,color=configs[role]
        self.st=ParagraphStyle('hierarquia-'+role,parent=ns['S']['body'],fontName=font,fontSize=size,leading=lead,textColor=HexColor(color))
        text=str(part.text).strip('*') if part.kind=='marker' else part.text
        self.p=Paragraph(ns['inline'](text,part.doc),self.st)
    def wrap(self,w,h):
        self.width=w;_,ph=self.p.wrap(w-self.inset,h);self.height=ph+self.extra
        return w,self.height
    def draw(self):
        c=self.canv;c.saveState()
        if self.role=='grupo':
            c.setFillColor(HexColor('#522039'));c.rect(0,3,3,self.height-6,fill=1,stroke=0)
            self.p.drawOn(c,self.inset,4)
        elif self.role=='subtopico':
            c.setStrokeColor(HexColor('#9e2358'));c.setLineWidth(.7);c.line(0,1,28,1)
            self.p.drawOn(c,0,2)
        elif self.role=='exemplo':self.p.drawOn(c,0,1)
        else:
            self.p.drawOn(c,0,0);c.setStrokeColor(HexColor('#9e2358'));c.setLineWidth(.75);c.line(0,-1,min(self.width,44),-1)
        c.restoreState()

def instalar(Part,ns):
    rows=json.loads((ns['B']/'revisao-r41/CLASSIFICACAO.json').read_text())
    lookup={(r['bloco'],r['titulo']):r for r in rows}
    def classificar(p):
        if p.generated:return p
        row=lookup.get((p.block,str(p.text).strip('*')))
        if row and p.kind in {'h2','h3','marker'}:
            p.editorial_style=row['tratamento'];p.editorial_level=row['nivel_editorial']
        return p
    ns['classificar_titulo']=classificar
    original=Part.make
    def make(self,w):
        classificar(self)
        role=getattr(self,'editorial_style',None)
        if role:
            old=ns['S'][self.kind]
            before=old.spaceBefore+(6 if self.kind=='marker' else 0)
            return TituloIntermediario(self,w,ns,role),before,old.spaceAfter+2
        return original(self,w)
    Part.make=make

"""Provas adicionais para títulos de seção. Famílias e demais níveis preservados."""
from reportlab.platypus import Flowable,Paragraph
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.colors import HexColor,white

OPCOES={
 'A':{'nome':'Serifa e filete','font':'Bold','size':20.5,'inset':0,'color':'#251727'},
 'B':{'nome':'Cartela clara','font':'Bold','size':20.5,'inset':10,'color':'#251727'},
 'C':{'nome':'Faixa escura','font':'Strong','size':21,'inset':10,'color':'#ffffff'},
}
class Secao(Flowable):
 def __init__(self,part,width,ns,cfg):
  super().__init__();self.part=part;self.ns=ns;self.cfg=cfg;self.width=width
  self.st=ParagraphStyle('section-prototype',parent=ns['S']['h1'],fontName=cfg['font'],fontSize=cfg['size'],leading=24,textColor=HexColor(cfg['color']))
  self.p=Paragraph(ns['inline'](part.text,part.doc),self.st)
 def wrap(self,w,h):
  self.width=w;_,self.height=self.p.wrap(w-2*self.cfg['inset'],h);return w,self.height
 def draw(self):
  c=self.canv;w=self.width;h=self.height;v=self.cfg['id'];c.saveState();acc=HexColor('#9e2358');pale=HexColor('#f8f1f4')
  if v=='A':
   c.setStrokeColor(HexColor('#cfb8c2'));c.setLineWidth(.6);c.line(0,h+1,w,h+1);c.setStrokeColor(acc);c.setLineWidth(2);c.line(0,h+1,34,h+1)
  elif v=='B':
   c.setFillColor(pale);c.rect(0,-2,w,h+4,fill=1,stroke=0);c.setStrokeColor(acc);c.setLineWidth(.7);c.line(0,h+2,w,h+2);c.line(0,-2,w,-2)
  else:
   c.setFillColor(HexColor('#522039'));p=c.beginPath();p.moveTo(0,-2);p.lineTo(w-9,-2);p.lineTo(w,7);p.lineTo(w,h+2);p.lineTo(0,h+2);p.close();c.drawPath(p,fill=1,stroke=0)
  self.p.drawOn(c,self.cfg['inset'],0);c.restoreState()

def instalar(Part,ns):
 import json
 cfg=json.loads((ns['B']/'ESTUDO-SECAO.json').read_text());original=Part.make
 def make(self,w):
  if self.kind=='h1' and getattr(self,'role',None)!='Família' and not self.generated:
   st=ns['S']['h1'];return Secao(self,w,ns,cfg),st.spaceBefore,st.spaceAfter
  return original(self,w)
 Part.make=make

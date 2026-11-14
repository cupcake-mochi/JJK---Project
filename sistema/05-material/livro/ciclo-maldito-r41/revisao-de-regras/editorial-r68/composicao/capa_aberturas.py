"""Composição em PDF sobre a capa recebida. Não gera nem modifica bitmaps."""
from pathlib import Path
import hashlib,math
from PIL import Image
from reportlab.lib.utils import ImageReader
from reportlab.lib.colors import HexColor
from reportlab.pdfbase import pdfmetrics

def draw_cover(c,B,W,H,title=None,number=None,target=None):
 path=B/'capa/Ciclo-Maldito-Capa-Original.png';render_path=path if number is None else B/'capa/Ciclo-Maldito-Base-Aberturas.png';im=Image.open(render_path);iw,ih=im.size
 assert (iw,ih)==(1024,1536),(iw,ih)
 c.saveState();c.scale(W/iw,H/ih)
 image=ImageReader(im);c.drawImage(image,0,0,width=iw,height=ih,mask='auto')
 def region(src,dest):
  sx0,sy0,sx1,sy1=src;dx0,dy0,dx1,dy1=dest
  scalex=(dx1-dx0)/(sx1-sx0);scaley=(dy1-dy0)/(sy1-sy0)
  c.saveState();p=c.beginPath();p.rect(dx0,ih-dy1,dx1-dx0,dy1-dy0);c.clipPath(p,stroke=0)
  c.drawImage(image,dx0-sx0*scalex,ih-dy1-(ih-sy1)*scaley,width=iw*scalex,height=ih*scaley,mask='auto');c.restoreState()
 result={'tipo':'capa' if number is None else 'abertura','titulo':title or 'Ciclo Maldito','capitulo':number,'arquivo':'capa/Ciclo-Maldito-Capa-Original.png','dimensoes_originais':[iw,ih],'sha256_original':hashlib.sha256(path.read_bytes()).hexdigest(),'sem_geracao_ia':True}
 if number is not None:
  # Restored label derived only from the supplied artwork, without AI.
  words=title.upper().split();letters=sum(len(w) for w in words);gaps=len(words)-1
  font=min(79,840/(max(1,letters-1)*.94+gaps*.6+1));height=(max(1,letters-1)*.94+gaps*.6+1)*font
  y=145+(840-height)/2+font*.75;ys=[]
  c.setFillColor(HexColor('#2C2418'));c.setStrokeColor(HexColor('#2C2418'));c.setLineWidth(.35)
  for wi,word in enumerate(words):
   if wi:y+=font*.6
   for char in word:
    width=pdfmetrics.stringWidth(char,'Bold',font);assert width<143
    t=c.beginText();t.setTextOrigin(174-width/2,ih-y);t.setFont('Bold',font);t.setTextRenderMode(2);t.textOut(char);c.drawText(t)
    ys.append(y);y+=font*.94
  assert min(ys)-font>120 and max(ys)+font*.3<1018,(title,font,ys)
  c.setFont('Body',34);c.drawCentredString(174,ih-1088,'Capítulo')
  c.setFont('Bold',44);c.drawCentredString(174,ih-1130,str(number))
  # Keep the supplied symbols and edition stamp intact.
  result.update(fonte_titulo='Spectral SemiBold',tamanho_fonte_pixels=font,letras=letters,primeira_linha_y=ys[0],ultima_linha_y=ys[-1],subtitulo='Capítulo '+str(number),adaptacao='Texto vetorial sobre a faixa de papel restaurada por difusão convencional. Bordas, couro e símbolos preservados.',arquivo_base='capa/Ciclo-Maldito-Base-Aberturas.png',sha256_base=hashlib.sha256(render_path.read_bytes()).hexdigest())
 # Searchable descriptive text is invisible; the supplied front cover stays intact.
 t=c.beginText();t.setTextOrigin(8,12);t.setFont('Head',6);t.setTextRenderMode(3);t.textOut((title or 'Ciclo Maldito')+(' | Capítulo '+str(number) if number is not None else ' | Livro de Regras'));c.drawText(t)
 c.restoreState()
 if target:c.linkRect('',target,(W*104/iw,H*(ih-1240)/ih,W*252/iw,H*(ih-125)/ih),relative=0,thickness=0)
 return result

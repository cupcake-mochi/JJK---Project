from pathlib import Path
p=Path('/media/mizuki/HD Externo II/Claude/Pesquisa de Campo - Mestragem/08 - Diagramacao do Guia/GERAR-PDF.py');t=p.read_text()
a=''' TAIL_WHOLE=True
 best=saved;best_y=y;lo=base;hi=TOP-220'''
b=''' TAIL_WHOLE=True
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
 best=saved;best_y=y;lo=base;hi=TOP-220'''
assert a in t;t=t.replace(a,b)
a="  c.setFont('Head',12);c.drawCentredString(W*174/1024,H*0.279,'GUIA DO MESTRE')\n  c.showPage();continue"
b="""  c.setFont('Head',12);c.drawCentredString(W*174/1024,H*0.279,'GUIA DO MESTRE')
  # The base artwork carries the rulebook's old version. A vector edition
  # label covers it without changing the supplied bitmap.
  c.setFillColor(HexColor('#352c25'));c.roundRect(W*.715,H*.045,W*.175,H*.060,5,fill=1,stroke=0)
  c.setFillColor(HexColor('#ded0b7'));c.setFont('Head',16)
  c.drawCentredString(W*.8025,H*.071,'PRÉ-1.0')
  c.setFont('Head',7);c.drawCentredString(W*.8025,H*.056,'EDIÇÃO DE LEITURA')
  c.showPage();continue"""
assert a in t;t=t.replace(a,b);p.write_text(t)

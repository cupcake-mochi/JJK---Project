"""Tratamentos de capítulo; opção A aprovada, B e C guardadas para reversão."""
from reportlab.pdfbase import pdfmetrics
from reportlab.lib.colors import HexColor,white

def desenhar(c,numero,titulo,x,y,w,opcao='A'):
    c.saveState();c.translate(x,y)
    acc=HexColor('#9e2358');wine=HexColor('#522039');ink=HexColor('#251727');rule=HexColor('#cfb8c2')
    if opcao=='A':
        c.setFillColor(wine);p=c.beginPath();p.moveTo(0,0);p.lineTo(36,0);p.lineTo(44,8);p.lineTo(44,36);p.lineTo(0,36);p.close();c.drawPath(p,fill=1,stroke=0)
        c.setFillColor(white);c.setFont('Strong',30);c.drawCentredString(22,7,str(numero))
        c.setFillColor(acc);c.setFont('Strong',32);c.drawString(58,4,titulo.upper())
        c.setStrokeColor(rule);c.setLineWidth(.7);c.line(58,-3,w,-3)
    elif opcao=='B':
        c.setFillColor(HexColor('#f8f1f4'));c.rect(0,-1,w,37,fill=1,stroke=0)
        c.setFillColor(wine);c.rect(0,-1,4,37,fill=1,stroke=0)
        c.setFont('Strong',32);c.drawCentredString(33,4,str(numero))
        c.setStrokeColor(rule);c.setLineWidth(.6);c.line(62,5,62,30)
        c.setFillColor(ink);c.setFont('Strong',32);c.drawString(77,4,titulo.upper())
    elif opcao=='C':
        c.setFillColor(acc);c.setFont('Strong',46);c.drawCentredString(24,-1,str(numero))
        c.setStrokeColor(rule);c.setLineWidth(.7);c.line(60,1,60,32)
        c.setFillColor(ink);c.setFont('Entry',28);c.drawString(75,5,titulo)
        c.setStrokeColor(acc);c.setLineWidth(1.1);c.line(75,-3,w,-3)
    else:raise ValueError(opcao)
    font,size,offset=('Entry',28,75) if opcao=='C' else ('Strong',32,58 if opcao=='A' else 77)
    assert offset+pdfmetrics.stringWidth(titulo if opcao=='C' else titulo.upper(),font,size)<w,(numero,titulo,opcao)
    c.restoreState()

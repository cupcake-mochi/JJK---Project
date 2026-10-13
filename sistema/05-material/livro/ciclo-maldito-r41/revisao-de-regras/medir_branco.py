# -*- coding: utf-8 -*-
"""Branco no pé das colunas: para cada página de texto, a distância entre a última palavra de cada
coluna e a barra de navegação, como fração da altura útil. Não conta entrelinha nem espaço entre parágrafos."""
import re,sys
def mede(arq):
    t=open(arq,encoding="utf-8").read(); tot=0.0; n=0; vazias=[]; P=0; fora=0
    for i,pg in enumerate(re.findall(r'<page width="([\d.]+)" height="([\d.]+)">(.*?)</page>',t,flags=re.S),1):
        P+=1; W,H=float(pg[0]),float(pg[1])
        ws=[(float(a),float(b),float(c),float(d)) for a,b,c,d,w in re.findall(r'<word xMin="([\d.]+)" yMin="([\d.]+)" xMax="([\d.]+)" yMax="([\d.]+)">(.*?)</word>',pg[2])]
        rod=[r[1] for r in ws if r[1]>H*0.86]; topo=H*0.08
        if not rod: fora+=1; continue
        base=min(rod)-6
        corpo=[r for r in ws if topo<r[1]<base-2]
        if len(corpo)<40: fora+=1; continue
        n+=1; br=0.0
        for lado in (False,True):
            col=[r for r in corpo if ((r[0]+r[2])/2>=W/2)==lado]
            br+=max(0.0,base-max((r[3] for r in col),default=topo))/(base-topo)/2
        tot+=br
        if br>1/3: vazias.append(i)
    return P,n,fora,tot,vazias
for nome,arq in zip(sys.argv[1::2],sys.argv[2::2]):
    P,n,fora,tot,v=mede(arq)
    print(f"{nome}: {P} páginas, {n} medidas, {fora} fora (capa, arte, abertura) | branco no pé das colunas: {tot:.1f} páginas equivalentes = {tot/n*100:.1f}% da área de texto | páginas com mais de um terço em branco: {len(v)}")

from pathlib import Path
import sys,json
B=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(B))
s=(B/'gerar_livro.py').read_text()
s=s[:s.index('# Créditos ficam após o índice')]
s=s.replace('for ch in chapters:\n opening=',"for ch in [c for c in chapters if c['numero']==10]:\n opening=")
ns={'__file__':str(B/'gerar_livro.py'),'__name__':'__main__'}
exec(compile(s,str(B/'gerar_livro.py'),'exec'),ns)
from reportlab.pdfgen.canvas import Canvas
p=B/'tmp/pdfs/PROVA-FLUXO.pdf'
c=Canvas(str(p),pagesize=(ns['W'],ns['H']),pageCompression=1)
c.linkRect=lambda *a,**k:None
for page in ns['pages']:
 if page['chapter']['numero']!=10 or not page['draws']:continue
 for part,f,x,y,w,h,mode in page['draws']:f.drawOn(c,x,y)
 c.setFont('Head',9);c.drawString(54,25,str(page['numero']));c.showPage()
c.save()
report={'eventos':ns['events'],'fluxo':ns['fluxo'].flow_log,'paginas':[{'numero':p['numero'],'capitulo':p['chapter']['numero'],'desenhos':len(p['draws'])} for p in ns['pages']]}
(B/'revisao-r53/PROVA-FLUXO.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print('Prova de fluxo',p)

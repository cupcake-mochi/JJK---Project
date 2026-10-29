from pathlib import Path
from reportlab.pdfgen.canvas import Canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import json,hashlib,subprocess
A=Path(__file__).resolve().parent;R=A.parents[1];B=R/'08 - Diagramacao do Guia';G={};src=B/'MAPAS.py';exec(compile(src.read_text(),str(src),'exec'),G)
for name,file in [('Body','Spectral-Regular.ttf'),('Head','BarlowCondensed-SemiBold.ttf')]:pdfmetrics.registerFont(TTFont(name,str(B/'fontes'/file)))
(A/'imagens').mkdir(exist_ok=True);(A/'tmp/pdfs').mkdir(parents=True,exist_ok=True);rows=[]
for ident,name in [('s064','passarela'),('s066','portao')]:
 obj=G['Mapa'](ident,488);pdf=A/f'tmp/pdfs/{name}.pdf';c=Canvas(str(pdf),pagesize=(488,obj.height),invariant=1);obj.drawOn(c,0,0);c.showPage();c.save();svg=A/f'imagens/{name}.svg';subprocess.run(['pdftocairo','-svg',str(pdf),str(svg)],check=True);rows.append({'id':ident,'figura':str(svg.relative_to(R)),'sha256':hashlib.sha256(svg.read_bytes()).hexdigest(),'origem':str(src.relative_to(R)),'altura_pontos':obj.height})
data={'registro':121,'mapas':rows,'origem_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'criterios':['Conferidos os esquemas em caracteres e os mapas de referência da passarela, do portão e do Sineiro.','Escolhidos os desenhos vetoriais existentes da passarela e do portão, exportados com a altura do próprio desenho e sem a margem branca da página de referência.','Mapa do Sineiro reservado ao ensaio s073: contém posições de Rina, Mei e Akira não fixadas no caso s071. Não foi misturado a esta ficha.'],'limites':'Sem nova geometria, novo cenário ou edição de bitmap; reutilização das instruções vetoriais existentes.'}
(A/'mapas-selecionados.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n');print('Dois mapas vetoriais exportados')

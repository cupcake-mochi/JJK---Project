from pathlib import Path
import pymupdf as fitz,hashlib,json
r=Path('/media/mizuki/HD Externo II/Claude/Pesquisa de Campo - Mestragem');a=r/'04 - Planejamento/apoio-revisao-integral-94'
old=fitz.open(a/'visual-prova-2/prova-estavel.pdf');new=fitz.open(r/'08 - Diagramacao do Guia/output/pdf/Ciclo-Maldito-Guia-do-Mestre-Pre-1.0.pdf')
changed=[]
assert len(old)==len(new)
for i in range(len(new)):
 x=old[i].get_pixmap(matrix=fitz.Matrix(1,1)).samples;y=new[i].get_pixmap(matrix=fitz.Matrix(1,1)).samples
 if x!=y:changed.append(i+1)
result={'paginas':len(new),'mudaram':changed,'identicas':len(new)-len(changed),'metodo':'Comparação pixel a pixel, PyMuPDF, 72 dpi, entre a prova visual integral e o PDF final.'}
(a/'comparacao-final.json').write_text(json.dumps(result,ensure_ascii=False,indent=2));print(result)

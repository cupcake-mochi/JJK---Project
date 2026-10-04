from pathlib import Path
import re,json,hashlib
import markdown
from weasyprint import HTML
from pypdf import PdfReader
BASE=Path(__file__).resolve().parent
OUT=BASE/'output/pdf'
OUT.mkdir(parents=True,exist_ok=True)
src=(BASE/'PILOTO.md').read_text()
parts=re.split(r'<!-- page:([^|]+)\|([^>]+) -->\s*',src)
assert len(parts)==31,len(parts)
sections=[]
for i in range(1,len(parts),3):
    key,label,md=parts[i:i+3]
    body=markdown.markdown(md,extensions=['tables','md_in_html'])
    sections.append((key,label,body))
head='<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>Projeto - M | Piloto editorial 1</title><link rel="stylesheet" href="piloto.css"></head><body>'
html=head+''.join(f'<section class="page" id="{key}">{body}</section>' for key,label,body in sections)+'</body></html>'
(BASE/'PILOTO.html').write_text(html)
def render(text,name):
    doc=HTML(string=text,base_url=str(BASE)).render()
    out=OUT/name
    doc.write_pdf(out)
    boxes=[]
    for n,page in enumerate(doc.pages,1):
        for box in page._page_box.descendants():
            if getattr(box,'text',None):
                boxes.append({'pagina':n,'texto':box.text,'x':round(box.position_x,2),'y':round(box.position_y,2),'largura':round(box.width,2),'altura':round(box.height,2)})
    (BASE/'evidencias'/f'{out.stem}-caixas.json').write_text(json.dumps(boxes,ensure_ascii=False,indent=2))
    reader=PdfReader(out)
    pages=[p.extract_text() for p in reader.pages]
    (BASE/'evidencias'/f'{out.stem}-texto.txt').write_text('\n\n'.join(f'PÁGINA {i+1}\n{p}' for i,p in enumerate(pages)))
    print(json.dumps({'pdf':str(out),'paginas':len(doc.pages),'caracteres_por_pagina':[len(t) for t in pages],'links':sum(len(p.get('/Annots',[])) for p in reader.pages)},ensure_ascii=False))
    return out
render(html,'Projeto-M-Piloto-Editorial-01.pdf')
protecao=next(body for key,label,body in sections if key=='protecao')
# Both proofs use identical rule content; only column treatment changes.
inicio=protecao.index('<div class="ability">')
prefixo,regras=protecao[:inicio],protecao[inicio:]
comp=head+f'<section class="page" id="prova-uma"><div class="comparison-note">PROVA A · UMA COLUNA · MESMO TEXTO DA PROVA B</div>{protecao}</section><section class="page" id="prova-duas"><div class="comparison-note">PROVA B · DUAS COLUNAS · MESMO TEXTO DA PROVA A</div>{prefixo}<div class="columns">{regras}</div></section></body></html>'
comp=comp.replace('<link rel="stylesheet" href="piloto.css">','<link rel="stylesheet" href="piloto.css"><style>@page opening{background:white}section.page:first-child{page:auto}section.page{font-size:10.1pt;line-height:1.39}.ability{margin:3mm 0;padding:3mm 4mm 1mm}</style>')
(BASE/'COMPARACAO.html').write_text(comp)
render(comp,'Projeto-M-Prova-Protecao-1e2-colunas.pdf')

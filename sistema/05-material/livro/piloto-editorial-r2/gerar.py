from pathlib import Path
import re,json
import markdown
from weasyprint import HTML
from pypdf import PdfReader
BASE=Path(__file__).resolve().parent
OUT=BASE/'output/pdf'
OUT.mkdir(parents=True,exist_ok=True)
for source,name,kind in [('PILOTO','Projeto-M-Piloto-Editorial-02','reading'),('LOTE-TECNICO','Projeto-M-Amostras-Tecnicas-02','technical')]:
    src=(BASE/f'{source}.md').read_text()
    parts=re.split(r'<!-- page:([^|]+)\|([^>]+) -->\s*',src)
    assert (len(parts)-1)%3==0
    sections=[]
    for i in range(1,len(parts),3):
        key,label,md=parts[i:i+3]
        body=markdown.markdown(md,extensions=['tables','md_in_html'])
        sections.append(f'<section class="page {kind}" id="{key}">{body}</section>')
    html='<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>Projeto - M | Piloto editorial 2</title><link rel="stylesheet" href="piloto.css"></head><body>'+''.join(sections)+'</body></html>'
    (BASE/f'{source}.html').write_text(html)
    doc=HTML(string=html,base_url=str(BASE)).render()
    out=OUT/f'{name}.pdf';doc.write_pdf(out)
    boxes=[]
    for n,page in enumerate(doc.pages,1):
        for box in page._page_box.descendants():
            if getattr(box,'text',None):
                boxes.append({'pagina':n,'texto':box.text,'x':round(box.position_x,2),'y':round(box.position_y,2),'largura':round(box.width,2),'altura':round(box.height,2),'tag':box.element_tag})
    (BASE/'evidencias'/f'{name}-caixas.json').write_text(json.dumps(boxes,ensure_ascii=False,indent=2))
    pages=[p.extract_text() for p in PdfReader(out).pages]
    (BASE/'evidencias'/f'{name}-texto.txt').write_text('\n\n'.join(f'PÁGINA {i+1}\n{p}' for i,p in enumerate(pages)))
    print(json.dumps({'pdf':name,'paginas':len(doc.pages),'caracteres_por_pagina':[len(t) for t in pages]},ensure_ascii=False))

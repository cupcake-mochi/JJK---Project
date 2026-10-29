#!/usr/bin/env python3
"""Confere integridade, geometria e destinos. Não substitui a leitura das páginas."""
from pathlib import Path
import hashlib,json
import pymupdf as fitz
B=Path(__file__).resolve().parent
pdf=B/'output/pdf/Ciclo-Maldito-Guia-do-Mestre-Pre-1.0.pdf'
meta=json.loads((B/'revisao/composicao.json').read_text())
doc=fitz.open(pdf);issues=[];g=meta['geometria'];links=0
if hashlib.sha256(pdf.read_bytes()).hexdigest()!=meta['sha256_pdf']:issues.append('PDF difere da composição registrada.')
if len(doc)!=meta['paginas']:issues.append('Contagem de páginas divergente.')
for n,page in enumerate(doc,1):
 for link in page.get_links():
  links+=1
  if link['kind']==fitz.LINK_GOTO and not 0<=link['page']<len(doc):issues.append(f'Página {n}: destino interno inválido.')
 for block in page.get_text('dict')['blocks']:
  for line in block.get('lines',[]):
   for span in line['spans']:
    x0,y0,x1,y1=span['bbox']
    if '\ufffd' in span['text'] or '\x00' in span['text']:issues.append(f'Página {n}: caractere substituído.')
    if min(x0,y0)<-1 or x1>page.rect.width+1 or y1>page.rect.height+1:issues.append(f'Página {n}: texto fora da página.')
 items=[a for a in g if a['pagina']==n]
 for i,a in enumerate(items):
  if a['y_top']-a['altura']<93:issues.append(f'Página {n}: conteúdo abaixo da margem.')
  for b in items[i+1:]:
   ox=min(a['x']+a['largura'],b['x']+b['largura'])-max(a['x'],b['x'])
   oy=min(a['y_top'],b['y_top'])-max(a['y_top']-a['altura'],b['y_top']-b['altura'])
   if ox>1 and oy>1:issues.append(f'Página {n}: sobreposição de blocos.')
for a,b in zip(g,g[1:]):
 if a['consulta'] and a['tipo'] in ['h1','h2','h3']:
  if a['pagina']!=b['pagina'] or (a['largura']<300 and b['x']>a['x']+100):issues.append(f"Página {a['pagina']}: título separado do primeiro bloco.")
 if a['tipo']==b['tipo']=='table' and a['pagina']==b['pagina'] and a['texto']==b['texto']:issues.append(f"Página {a['pagina']}: tabela repartida na mesma página.")
print(json.dumps({'paginas':len(doc),'links':links,'problemas':issues,'nota':'Aprovação visual e clareza exigem inspeção das páginas.'},ensure_ascii=False,indent=2))
raise SystemExit(bool(issues))

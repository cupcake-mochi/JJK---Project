"""Conferência independente de texto, destinos, margens e geometria do PDF."""
from pathlib import Path
from collections import Counter,defaultdict
from bs4 import BeautifulSoup
import json,hashlib,re,unicodedata
import pymupdf
A=Path(__file__).resolve().parent;R=A.parents[1];E=R/'07 - Edicao de Leitura/edicao-integrada-136'
load=lambda p:json.loads(p.read_text());sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
c=load(A/'composicao.json');p=R/c['pdf'];assert sha(p)==c['sha256_pdf'];d=pymupdf.open(p)
assert len(d)==c['paginas'];fail=[];notes=[]
def tokens(t):return Counter(re.findall(r'[^\W_]+',unicodedata.normalize('NFKC',t).casefold(),re.U))
# Conferência por unidade, admitindo apenas páginas compartilhadas entre dois casos.
order=c['ordem_pdf'];content=[]
for i,r in enumerate(order):
 s=BeautifulSoup((E/r['pagina_html']).read_text(),'html.parser').article
 for nav in s.find_all('nav'):nav.decompose()
 expected=tokens(s.get_text(' ',strip=True));start=r['pagina_pdf']-1
 end=order[i+1]['pagina_pdf'] if i+1<len(order) else len(d)
 actual=tokens(' '.join(d[j].get_text() for j in range(start,end)))
 missing=expected-actual
 # Fragmentos separados na extração (ligações/itálico e quebras de palavra) são examinados, não ignorados.
 row={'pagina_html':r['pagina_html'],'intervalo_pdf':[start+1,end],'palavras_ausentes':dict(missing)};content.append(row)
 if missing:notes.append(row)
geometry=c['geometria'];bypage=defaultdict(list)
for g in geometry:
 bypage[g['pagina']].append(g)
 if g['x']<53 or g['x']+g['largura']>543 or g['y_top']>779 or g['y_top']-g['altura']<92:fail.append({'erro':'bloco fora da mancha','bloco':g})
collisions=[]
for page,items in bypage.items():
 for i,a in enumerate(items):
  if a['altura']<1:continue
  for b in items[i+1:]:
   if b['altura']<1:continue
   dx=min(a['x']+a['largura'],b['x']+b['largura'])-max(a['x'],b['x']);dy=min(a['y_top'],b['y_top'])-max(a['y_top']-a['altura'],b['y_top']-b['altura'])
   if dx>.8 and dy>.8:collisions.append({'pagina':page,'a':a['texto'],'b':b['texto'],'intersecao':[dx,dy]})
fail.extend(collisions)
links=0;external=0;outside=[];glyphs=[];pageinfo=[]
for i,page in enumerate(d,1):
 for link in page.get_links():
  links+=1
  if link['kind']==pymupdf.LINK_GOTO:
   if not 0<=link.get('page',-1)<len(d):fail.append({'pagina':i,'erro':'destino interno inválido','link':link})
  elif link['kind']==pymupdf.LINK_URI:
   external+=1
   if not link.get('uri','').startswith(('https://','http://','mailto:')):fail.append({'pagina':i,'erro':'ligação externa local','link':link})
  else:fail.append({'pagina':i,'erro':'tipo de ligação inesperado','link':link})
 for b in page.get_text('dict')['blocks']:
  for line in b.get('lines',[]):
   for span in line['spans']:
    rect=pymupdf.Rect(span['bbox'])
    if rect.x0<0 or rect.x1>page.rect.width+.5 or rect.y0<0 or rect.y1>page.rect.height+.5:outside.append([i,span['text'],list(rect)])
    if '\ufffd' in span['text'] or '\u25a0' in span['text']:glyphs.append([i,span['text']])
 area=sum(x['largura']*x['altura'] for x in bypage[i]);pageinfo.append({'pagina':i,'ocupacao_aproximada':round(area/(487.56*683.15),3),'caracteres_extraidos':len(page.get_text()),'titulo':next((x['texto'] for x in bypage[i] if x['tipo'] in ['major','h1','h2']),None)})
fail.extend({'erro':'texto fora da página','dados':x} for x in outside);fail.extend({'erro':'glifo ilegível','dados':x} for x in glyphs)
for row in load(R/'04 - Planejamento/apoio-leitura-144/cobertura-da-leitura-continua.json')['fontes']:assert sha(R/row['fonte'])==row['sha256_atual']
assert sha(R/'08 - Diagramacao do Guia/output/pdf/Ciclo-Maldito-Guia-do-Mestre-Pre-1.0.pdf')=='0050d7cf2426ce3eba555ab2010deaeb6d62e023a5dba67ec43f0495e79cbd3b'
report={'registro':145,'pdf':c['pdf'],'sha256_pdf':sha(p),'paginas':len(d),'fontes_textuais_preservadas':99,'ligacoes':links,'ligacoes_externas':external,'marcadores':len(d.get_toc()),'sobreposicoes_de_blocos':collisions,'texto_fora_da_pagina':outside,'glifos_ilegiveis':glyphs,'conferencia_por_unidade':content,'diferencas_de_extracao_a_examinar':notes,'paginas_para_revisao':pageinfo,'falhas':fail,'limite':'Controle automático de composição; inspeção visual registrada separadamente.'}
(A/'conferencia-do-pdf.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'paginas':len(d),'ligacoes':links,'marcadores':len(d.get_toc()),'unidades_com_diferencas_de_extracao':len(notes),'falhas':len(fail)},ensure_ascii=False))
assert not fail,fail[:5]

"""Conferir conteúdo e limites do PDF por extração independente da inspeção visual."""
from pathlib import Path
import subprocess,json,re,collections,xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
A=Path(__file__).resolve().parent
pdf=A/'output/pdf/Ciclo-Maldito-Apoios-da-Integracao.pdf'
subprocess.run(['pdftotext','-raw',str(pdf),str(A/'prova-dos-apoios.txt')],check=True)
subprocess.run(['pdftotext','-bbox',str(pdf),str(A/'coordenadas.html')],check=True)
s=BeautifulSoup((A/'prova-dos-apoios.html').read_text(),'html.parser').main.get_text(' ',strip=True)
t=(A/'prova-dos-apoios.txt').read_text()
for label in ['CICLO MALDITO / GUIA DO MESTRE','APOIOS REUNIDOS','PRÉ-1.0 · PROVA TEXTUAL PARCIAL']:t=t.replace(label,'')
t=re.sub(r'(?m)^[ \t]*\d+[ \t]*$','',t).replace('•','').replace('\x0c','\n')
t=re.sub(r'(?<=\w)[‐\-\u00ad]\s*\n\s*(?=\w)','',t)
def words(x):
 x=re.sub(r'(?<=\d)(?=(?:m|PE|PV)\b)',' ',x)
 return collections.Counter(re.findall(r'[^\W_]+(?:[-−+.,][^\W_]+)*',x,re.U))
a=words(s);b=words(t);pages=ET.parse(A/'coordenadas.html').findall('.//{*}page');bounds=[]
for i,p in enumerate(pages,1):
 for w in p.findall('.//{*}word'):
  if float(w.attrib['xMin'])<0 or float(w.attrib['yMin'])<0 or float(w.attrib['xMax'])>float(p.attrib['width']) or float(w.attrib['yMax'])>float(p.attrib['height']):bounds.append([i,w.text,w.attrib])
d={'registro':136,'paginas':len(pages),'palavras_ausentes':dict(a-b),'palavras_extras':dict(b-a),'fora_da_pagina':bounds,'metodo':'Poppler -raw e -bbox; cabeçalhos e números de página removidos, hifenização automática U+2010 normalizada. Comparação de palavras independente da ordem de leitura, além da inspeção direta das sete páginas.'}
(A/'conferencia-do-pdf.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
assert not d['palavras_ausentes'] and not d['palavras_extras'] and not bounds,d
print('PDF: sete páginas; palavras preservadas e limites conferidos.')

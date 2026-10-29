"""Conferir preservação editorial, referências e integridade da prova parcial."""
from pathlib import Path
from urllib.parse import urlsplit,unquote
from collections import Counter
from bs4 import BeautifulSoup
import hashlib,json,markdown,re,subprocess,unicodedata,xml.etree.ElementTree as ET
A=Path(__file__).resolve().parent;R=A.parents[1]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def load(p):return json.loads(p.read_text())
def soup(p):return BeautifulSoup(p.read_text() if p.suffix=='.html' else markdown.markdown(p.read_text(),extensions=['tables','toc']),'html.parser')
def tokens(t):
 t=unicodedata.normalize('NFKC',t).lower()
 t=re.sub(r'(?<=\w)[-‐‑]\s*(?=\w)','',t)
 return re.findall(r'[^\W_]+',t)
def main():
 d=load(A/'amostra.json');pdf=R/d['pdf'];doc=soup(R/d['html'])
 assert sha(pdf)==d['pdf_sha256'] and sha(R/d['html'])==d['html_sha256']
 preserved=[]
 for f in d['fontes']:
  p=R/f['fonte'];assert sha(p)==f['sha256']
  if p.name.startswith('00-'):continue
  old=soup(A/'antes'/f['fonte']);new=soup(p)
  assert re.findall(r'\d+(?:[.,]\d+)?',old.get_text())==re.findall(r'\d+(?:[.,]\d+)?',new.get_text()),p
  assert [x.get_text(' ',strip=True) for x in old.find_all('table')]==[x.get_text(' ',strip=True) for x in new.find_all('table')],p
  preserved.append({'fonte':f['fonte'],'numeros_na_mesma_ordem':True,'tabelas_iguais':True})
 cache={};links=[]
 targets=[R/f['fonte'] for f in d['fontes']]+[A/'prova-textual.html',A/'consulta-de-regras.html',R/'04 - Planejamento/112-revisao-textual-da-abertura-e-primeiros-capitulos.md']
 for p in targets:
  s=soup(p);ids=[x['id'] for x in s.find_all(id=True)];assert len(ids)==len(set(ids)),p
  for tag in s.find_all(['a','img']):
   attr='href' if tag.name=='a' else 'src';u=urlsplit(tag.get(attr,''))
   if u.scheme:continue
   target=(p.parent/unquote(u.path)).resolve() if u.path else p.resolve()
   assert target.is_file() or target in [A/'conferencias.json',A/'revisao-final.json'],(p,tag)
   if u.fragment:
    if target not in cache:cache[target]=soup(target)
    assert cache[target].find(id=unquote(u.fragment)),(p,tag)
   links.append({'origem':str(p.relative_to(R)),'destino':tag.get(attr,'')})
 text=subprocess.check_output(['pdftotext',str(pdf),'-'],text=True)
 for h in ['CICLO MALDITO / GUIA DO MESTRE','ABERTURA E CAPÍTULOS 1–3','PRÉ-1.0 · PROVA TEXTUAL PARCIAL']:text=text.replace(h,'')
 missing=Counter(tokens(doc.main.get_text(' ')))-Counter(tokens(text));assert not missing,missing
 subprocess.run(['pdftotext','-bbox',str(pdf),str(A/'limites.html')],check=True)
 tree=ET.parse(A/'limites.html');ns={'x':'http://www.w3.org/1999/xhtml'};outside=[];pages=[]
 for n,page in enumerate(tree.findall('.//x:page',ns),1):
  w=float(page.attrib['width']);h=float(page.attrib['height']);words=page.findall('x:word',ns)
  for word in words:
   x0,y0,x1,y1=[float(word.attrib[k]) for k in ['xMin','yMin','xMax','yMax']]
   if x0<0 or y0<0 or x1>w or y1>h:outside.append([n,word.text])
  pages.append({'pagina':n,'palavras':len(words)})
 assert len(pages)==len(d['paginas']) and not outside
 structure=load(R/'04 - Planejamento/apoio-estrutura-99/estrutura-e-fontes.json')
 for old in structure['fontes']:assert sha(R/old['fonte'])==old['sha256'],old['fonte']
 before=load(A/'antes/04 - Planejamento/apoio-piloto/manifesto-entrega.json')
 book='08 - Diagramacao do Guia/output/pdf/Ciclo-Maldito-Guia-do-Mestre-Pre-1.0.pdf';assert sha(R/book)==before[book]
 for a in ['apoio-primeira-missao-100','apoio-mundo-e-preparo-101','apoio-inspiracao-104']:
  for rel in before:
   if rel.startswith('04 - Planejamento/'+a+'/') and not '/antes/' in rel:assert sha(R/rel)==before[rel],rel
 states=load(R/'04 - Planejamento/apoio-conferencia-111/cobertura-e-destinos.json');assert len(states['pontos'])==130 and len(states['competencias'])==20
 base=R/'04 - Planejamento/apoio-carregador/fontes/LIVRO-COMPLETO-R53.md';assert sha(base)==before[str(base.relative_to(R))]
 result={'registro':112,'pdf_sha256':sha(pdf),'paginas':pages,'fontes_revisadas':preserved,'links_locais_conferidos':len(links),'links':links,'palavras_ausentes_no_pdf':dict(missing),'palavras_fora_da_pagina':outside,'fontes_antigas_preservadas':104,'pdf_integrado_preservado':True,'amostras_100_101_104_preservadas':True,'cobertura':'130 pontos e 20 competências documentais preservados; estados não promovidos.','base_de_regras_preservada':True,'limites':['Conferência de texto, números e arquivos; não é teste humano ou validação de equilíbrio.','Primeiro lote da etapa 6; revisão integral do livro ainda em andamento.']}
 (A/'conferencias.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
 print(json.dumps({k:v for k,v in result.items() if k not in ['links','paginas']},ensure_ascii=False,indent=2))
if __name__=='__main__':main()

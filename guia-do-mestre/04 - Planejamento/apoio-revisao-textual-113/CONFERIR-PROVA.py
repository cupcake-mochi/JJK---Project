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
 oldnav=A/'antes/04 - Planejamento/apoio-consultas-105'
 nav=R/'04 - Planejamento/apoio-consultas-105'
 oldcase=load(oldnav/'destinos-e-fontes.json');newcase=load(nav/'destinos-e-fontes.json')
 assert oldcase['casos']==newcase['casos'] and oldcase['fontes']==newcase['fontes']
 assert sum(len(items) for items in newcase['casos'].values())==59
 for name in ['casos-completos.html','folhas-para-a-mesa.html']:
  oldview=soup(oldnav/name);newview=soup(nav/name)
  assert oldview.get_text()==newview.get_text(),name
  assert [s.get_text() for s in oldview.find_all('style')]==[s.get_text() for s in newview.find_all('style')],name
 oldsheet=soup(oldnav/'folhas-para-a-mesa.html');newsheet=soup(nav/'folhas-para-a-mesa.html')
 assert str(oldsheet.main)==str(newsheet.main)
 sheet=load(nav/'amostra.json');assert sha(R/sheet['pdf'])==sheet['pdf_sha256']==load(oldnav/'amostra.json')['pdf_sha256']
 assert (nav/'conferencia-de-cobertura.json').read_bytes()==(oldnav/'conferencia-de-cobertura.json').read_bytes()
 cache={};links=[]
 targets=[R/f['fonte'] for f in d['fontes']]+[A/'prova-textual.html',A/'consulta-de-regras.html',R/'04 - Planejamento/113-revisao-textual-da-mesa-e-da-campanha.md']
 targets.extend([nav/'casos-completos.html',nav/'folhas-para-a-mesa.html',nav/'destinos-dos-casos.md',R/'06 - Redacao do Guia/revisao-98/LEIA-ME.md'])
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
 rule=soup(A/'consulta-de-regras.html')
 for group,folder in [('conducao','apoio-conducao-102'),('campanha','apoio-campanha-103')]:
  reference=soup(R/'04 - Planejamento'/folder/'consulta-de-regras.html')
  assert [s.get_text(' ',strip=True) for s in reference.find_all('section')]==[s.get_text(' ',strip=True) for s in rule.find(id=group).find_all('section')]
 raw=(R/'04 - Planejamento/apoio-carregador/fontes/LIVRO-COMPLETO-R53.md').read_text()
 assert 'uma pessoa estável que conclua um descanso curto' in raw
 assert 'um alvo estável que conclua um descanso curto' in (R/d['fontes'][0]['fonte']).read_text()
 text=subprocess.check_output(['pdftotext',str(pdf),'-'],text=True)
 for h in ['CICLO MALDITO / GUIA DO MESTRE','CAPÍTULOS 4 E 5','PRÉ-1.0 · PROVA TEXTUAL PARCIAL']:text=text.replace(h,'')
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
 for a in ['apoio-conducao-102','apoio-campanha-103','apoio-revisao-textual-112']:
  for rel in before:
   if rel.startswith('04 - Planejamento/'+a+'/') and not '/antes/' in rel:assert sha(R/rel)==before[rel],rel
 states=load(R/'04 - Planejamento/apoio-conferencia-111/cobertura-e-destinos.json');assert len(states['pontos'])==130 and len(states['competencias'])==20
 base=R/'04 - Planejamento/apoio-carregador/fontes/LIVRO-COMPLETO-R53.md';assert sha(base)==before[str(base.relative_to(R))]
 result={'registro':113,'pdf_sha256':sha(pdf),'paginas':pages,'fontes_revisadas':preserved,'links_locais_conferidos':len(links),'links':links,'palavras_ausentes_no_pdf':dict(missing),'palavras_fora_da_pagina':outside,'fontes_antigas_preservadas':104,'pdf_integrado_preservado':True,'amostras_102_103_e_prova_112_preservadas':True,'cobertura':'130 pontos e 20 competências documentais preservados; estados não promovidos.','base_de_regras_preservada':True,'casos_preservados':59,'texto_e_estilo_dos_indices_preservados':True,'corpo_e_pdf_das_folhas_preservados':True,'limites':['Conferência de texto, números e arquivos; não é teste humano ou validação de equilíbrio.','Segundo lote da etapa 6; revisão integral do livro ainda em andamento.']}
 (A/'conferencias.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
 print(json.dumps({k:v for k,v in result.items() if k not in ['links','paginas']},ensure_ascii=False,indent=2))
if __name__=='__main__':main()

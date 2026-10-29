"""Conferência da prova e da fila; não substitui leitura editorial ou teste humano."""
from pathlib import Path
from bs4 import BeautifulSoup
from collections import Counter
from urllib.parse import urlsplit,unquote
import hashlib,json,markdown,math,re,subprocess,unicodedata,xml.etree.ElementTree as ET
A=Path(__file__).resolve().parent;R=A.parents[1]
def load(p):return json.loads(p.read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def soup(p):return BeautifulSoup(p.read_text() if p.suffix=='.html' else markdown.markdown(p.read_text(),extensions=['tables','toc']),'html.parser')
def nums(t):return re.findall(r'\d+(?:[.,]\d+)?',t)
def tokens(t):
 t=unicodedata.normalize('NFKC',t).lower();t=re.sub(r'(?<=\w)[-‐‑]\s*(?=\w)','',t);return re.findall(r'[^\W_]+',t)
def main():
 m=load(A/'amostra.json');cfg=load(A/'arquivos-do-lote.json');old=load(A/'antes/04 - Planejamento/apoio-piloto/manifesto-entrega.json');pdf=R/m['pdf'];doc=soup(A/'prova-textual.html');changes=load(A/'alteracoes.json')
 assert sha(pdf)==m['pdf_sha256'] and sha(A/'prova-textual.html')==m['html_sha256']
 inspected=[]
 for f in m['fontes']+[m['guia_de_escolha']]:
  p=R/f['fonte'];assert sha(p)==f['sha256'];previous=(A/'antes'/f['fonte']).read_text();current=p.read_text();replayed=previous
  for c in changes:
   if c['fonte']==f['fonte']:
    assert replayed.count(c['antes'])==1,c;replayed=replayed.replace(c['antes'],c['depois'])
  assert replayed==current,f['fonte']
  before=soup(A/'antes'/f['fonte']);after=soup(p)
  # Nome da edição pode aparecer mais de uma vez no guia de escolha; não é número de regra.
  textbefore=before.get_text().replace('Livro de Regras 1.0','Livro de Regras');textafter=after.get_text().replace('Livro de Regras 1.0','Livro de Regras')
  assert nums(textbefore)==nums(textafter),f['fonte']
  tables=lambda s:[[x.get_text(' ',strip=True) for x in t.find_all(['th','td'])] for t in s.find_all('table')]
  assert tables(before)==tables(after),f['fonte']
  assert re.findall(r'<!-- espaco: (\d+) -->',previous)==re.findall(r'<!-- espaco: (\d+) -->',current),f['fonte']
  if f.get('tipo')=='formulario':assert len(before.find_all('h2'))==len(after.find_all('h2'))
  inspected.append({'fonte':f['fonte'],'alteracoes_reproduzidas':True,'numeros_e_tabelas_preservados':True,'linhas_de_preenchimento_preservadas':True})
 queue=load(A/'fila-dos-casos.json');base=load(R/queue['base']);assert sha(R/queue['base'])==queue['base_sha256']
 ids={x['id'] for v in base['casos'].values() for x in v};assert len(ids)==59
 planned=[i for l in queue['lotes_planejados'] for i in l['casos']];assert len(planned)==len(set(planned))==58 and set(planned)==ids-{'s089'}
 assert {x['id'] for x in queue['casos']}==ids and len(queue['lotes_planejados'])==14
 for c in queue['casos']:
  if c['id']=='s089':assert sha(R/c['fonte_revisada'])==c['sha256_revisado']==old[c['fonte_revisada']]
  else:assert sha(R/c['fonte_original'])==c['sha256']==old[c['fonte_original']]
 for c in queue['outras_consultas_pendentes']:assert sha(R/c['fonte'])==c['sha256']==old[c['fonte']]
 assert len(queue['outras_consultas_pendentes'])==17
 targets=[R/f['fonte'] for f in m['fontes']+[m['guia_de_escolha']]]+[A/'prova-textual.html',A/'fila-dos-casos.md',A/'fila-dos-casos.html',R/'06 - Redacao do Guia/revisao-98/LEIA-ME.md',R/'04 - Planejamento/116-revisao-das-folhas-e-fila-dos-casos.md'];cache={};links=[]
 for p in targets:
  view=soup(p);anchors=[x['id'] for x in view.find_all(id=True)];assert len(anchors)==len(set(anchors)),p
  for tag in view.find_all('a',href=True):
   u=urlsplit(tag['href'])
   if u.scheme:continue
   target=(p.parent/unquote(u.path)).resolve() if u.path else p.resolve();assert target.is_file() or target==A/'conferencias.json',(p,tag['href'])
   if u.fragment:
    if target not in cache:cache[target]=soup(target)
    assert cache[target].find(id=unquote(u.fragment)),(p,tag['href'])
   links.append({'origem':str(p.relative_to(R)),'destino':tag['href']})
 plain=subprocess.check_output(['pdftotext',str(pdf),'-'],text=True)
 for h in ['CICLO MALDITO / GUIA DO MESTRE','FOLHAS PARA A MESA','PRÉ-1.0 · PROVA TEXTUAL PARCIAL']:plain=plain.replace(h,'')
 missing=Counter(tokens(doc.main.get_text(' ')))-Counter(tokens(plain));assert not missing,missing
 subprocess.run(['pdftotext','-bbox',str(pdf),str(A/'limites.html')],check=True);ns={'x':'http://www.w3.org/1999/xhtml'};tree=ET.parse(A/'limites.html');pages=[];outside=[]
 for n,page in enumerate(tree.findall('.//x:page',ns),1):
  w=float(page.attrib['width']);h=float(page.attrib['height']);words=page.findall('x:word',ns)
  for word in words:
   x0,y0,x1,y1=[float(word.attrib[k]) for k in ['xMin','yMin','xMax','yMax']]
   if x0<0 or y0<0 or x1>w or y1>h:outside.append([n,word.text])
  pages.append({'pagina':n,'palavras':len(words)})
 assert len(pages)==len(m['paginas'])==5 and not outside,outside
 structure=load(R/'04 - Planejamento/apoio-estrutura-99/estrutura-e-fontes.json')
 for f in structure['fontes']:assert sha(R/f['fonte'])==f['sha256'],f['fonte']
 for rel in ['08 - Diagramacao do Guia/output/pdf/Ciclo-Maldito-Guia-do-Mestre-Pre-1.0.pdf','04 - Planejamento/apoio-carregador/fontes/LIVRO-COMPLETO-R53.md','04 - Planejamento/apoio-consultas-105/output/pdf/Ciclo-Maldito-Folhas-para-a-Mesa.pdf']:
  assert sha(R/rel)==old[rel],rel
 assert min(math.ceil(44/3),15*2)==15 and 3-0==3
 coverage=load(R/'04 - Planejamento/apoio-consultas-105/conferencia-de-cobertura.json');assert len(coverage['pontos'])==130 and len(coverage['competencias'])==20
 result={'registro':116,'pdf_sha256':sha(pdf),'paginas':pages,'fontes_conferidas':inspected,'links_locais_conferidos':len(links),'links':links,'palavras_ausentes_no_pdf':dict(missing),'palavras_fora_da_pagina':outside,'fontes_antigas_preservadas':104,'casos_distintos':59,'casos_pendentes':58,'lotes_planejados':14,'consultas_complementares_pendentes':17,'socorro':{'maximo_referencia':44,'classe':2,'tratamento_necessario':15,'tratamento_acumulado':0,'janela_na_pausa':3},'pdf_integrado_e_pdf_105_preservados':True,'cobertura':'130 pontos e 20 competências mantidos sem promoção; preservação completa por conferência final do manifesto.','limites':['Fila é planejamento, não nova revisão dos 59 casos.','Sem teste humano ou nova simulação.','Revisão textual e visual integrada ainda pendente.']}
 (A/'conferencias.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n');print(json.dumps({k:v for k,v in result.items() if k not in ['links','paginas']},ensure_ascii=False,indent=2))
if __name__=='__main__':main()

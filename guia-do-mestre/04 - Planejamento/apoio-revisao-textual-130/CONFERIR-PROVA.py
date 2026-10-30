"""Conferir cópias, números, tabelas e destinos sem alterar fontes históricas (registro 130)."""
from pathlib import Path
from bs4 import BeautifulSoup
from collections import Counter
from urllib.parse import urlsplit,unquote
import difflib,hashlib,json,markdown,re,subprocess,unicodedata,xml.etree.ElementTree as ET
A=Path(__file__).resolve().parent;R=A.parents[1]
def load(p):return json.loads(p.read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def soup(p):return BeautifulSoup(p.read_text() if p.suffix=='.html' else markdown.markdown(p.read_text(),extensions=['tables','toc']),'html.parser')
def nums(t):return re.findall(r'\d+(?:[.,]\d+)?',t)
def tokens(t):
 t=unicodedata.normalize('NFKC',t).lower();t=re.sub(r'(?<=\w)[-‐‑]\s*(?=\w)','',t);t=re.sub(r'(?<=\d)(?=[^\W\d_])|(?<=[^\W\d_])(?=\d)',' ',t);return re.findall(r'[^\W_]+',t)
def main():
 m=load(A/'amostra.json');cfg=load(A/'arquivos-do-lote.json');old=load(A/'antes/04 - Planejamento/apoio-piloto/manifesto-entrega.json');pdf=R/m['pdf'];doc=soup(A/'prova-textual.html');changes=load(A/'alteracoes.json');inspected=[];count=0
 assert sha(pdf)==m['pdf_sha256'] and sha(A/'prova-textual.html')==m['html_sha256']
 labels={}
 # Única mudança de número do lote, documentada em alteracoes.json (correcao_de_regra) e contas-conferidas.json.
 number_changes={'s054':[(('',),('6',))]};number_log={}
 for f in m['fontes']:
  p=R/f['fonte'];original=R/f['fonte_original'];assert sha(p)==f['sha256'] and sha(original)==f['sha256_original']==old[f['fonte_original']]
  previous=original.read_text();replayed=previous
  for c in changes:
   if c['fonte']==f['fonte']:
    assert replayed.count(c['antes'])==c.get('ocorrencias',1),c['fonte'];replayed=replayed.replace(c['antes'],c['depois'])
  assert replayed==p.read_text(),p
  before=soup(original);after=soup(p);nb,na=nums(before.get_text()),nums(after.get_text());ops=[(tuple(nb[i1:i2]),tuple(na[j1:j2])) for tag,i1,i2,j1,j2 in difflib.SequenceMatcher(None,nb,na,autojunk=False).get_opcodes() if tag!='equal'];allowed=[(tuple(x for x in a if x),tuple(b)) for a,b in number_changes.get(f['fonte_id'],[])];assert ops==allowed,(p,ops);number_log[f['fonte_id']]=[list(map(list,o)) for o in ops]
  tables=lambda s:[[x.get_text(' ',strip=True) for x in t.find_all(['th','td'])] for t in s.find_all('table')]
  def expected_cell(x):
   for old_text,new_text in labels.items():x=x.replace(old_text,new_text)
   return x
  expected=[[expected_cell(x) for x in t] for t in tables(before)]
  assert expected==tables(after),p;count+=len(expected)
  inspected.append({'id':f['fonte_id'],'fonte':f['fonte'],'numeros_preservados':not number_changes.get(f['fonte_id']),'mudancas_de_numero':number_log[f['fonte_id']],'tabelas':len(expected),'originais_preservados':True,'alteracoes_reproduzidas':True})
 source=load(A/'antes/04 - Planejamento/apoio-revisao-textual-129/destinos-e-fontes.json');current=load(A/'destinos-e-fontes.json');assert current['fontes']==source['fontes'];new={f['fonte_id']:f for f in m['fontes']};cases=0
 for group,entries in source['casos'].items():
  for before,after in zip(entries,current['casos'][group]):
   cases+=1
   if before['id'] in new:
    c=dict(after)
    for k in ['fonte_revisada','sha256_revisado','motivo']:c.pop(k)
    c['consulta_atual']=before['consulta_atual'];assert c==before,before['id']
    f=new[before['id']];assert after['consulta_atual']==m['html']+'#'+f['id'] and sha(R/after['fonte_revisada'])==after['sha256_revisado']
   else:assert before==after,before['id']
 assert cases==59 and sum(len(v) for v in current['casos'].values())==59
 q=load(A/'fila-dos-casos.json');assert q['casos_pendentes']==0 and q['lotes_pendentes']==0 and len(q['casos_ja_revistos'])==59
 assert len({c['id'] for c in q['casos']})==59 and len(q['lotes_planejados'])==14 and q['proximo_lote']=='consultas complementares'
 for f in q['casos']:
  if 'fonte_revisada' in f:assert sha(R/f['fonte_revisada'])==f['sha256_revisado']
  else:assert sha(R/f['fonte_original'])==f['sha256']
 targets=[R/f['fonte'] for f in m['fontes']]+[A/'prova-textual.html',A/'casos-completos.html',A/'guia-de-consulta.html',A/'destinos-dos-casos.md',A/'fila-dos-casos.md',R/'06 - Redacao do Guia/revisao-98/LEIA-ME.md',R/'06 - Redacao do Guia/revisao-98/consultas/LEIA-ME.md',R/'04 - Planejamento/130-revisao-de-doma-construcao-e-transporte.md'];cache={};links=[]
 for p in targets:
  view=soup(p);ids=[x['id'] for x in view.find_all(id=True)];assert len(ids)==len(set(ids)),p
  for tag in view.find_all('a',href=True):
   u=urlsplit(tag['href'])
   if u.scheme:continue
   target=(p.parent/unquote(u.path)).resolve() if u.path else p.resolve();assert target.is_file() or target==A/'conferencias.json',(p,tag['href'])
   if u.fragment:
    if target not in cache:cache[target]=soup(target)
    assert cache[target].find(id=unquote(u.fragment)),(p,tag['href'])
   links.append({'origem':str(p.relative_to(R)),'destino':tag['href']})
 plain=subprocess.check_output(['pdftotext',str(pdf),'-'],text=True)
 for h in ['CICLO MALDITO / GUIA DO MESTRE','DOMA, CONSTRUÇÃO E TRANSPORTE','PRÉ-1.0 · PROVA TEXTUAL PARCIAL']:plain=plain.replace(h,'')
 missing=Counter(tokens(doc.main.get_text(' ')))-Counter(tokens(plain));assert not missing,missing
 subprocess.run(['pdftotext','-bbox',str(pdf),str(A/'limites.html')],check=True);ns={'x':'http://www.w3.org/1999/xhtml'};tree=ET.parse(A/'limites.html');pages=[];outside=[]
 for i,page in enumerate(tree.findall('.//x:page',ns),1):
  w=float(page.attrib['width']);h=float(page.attrib['height']);words=page.findall('x:word',ns)
  for word in words:
   x0,y0,x1,y1=[float(word.attrib[k]) for k in ['xMin','yMin','xMax','yMax']]
   if x0<0 or y0<0 or x1>w or y1>h:outside.append([i,word.text])
  pages.append({'pagina':i,'palavras':len(words)})
 assert len(pages)==len(m['paginas']) and not outside,outside
 for f in load(R/'04 - Planejamento/apoio-estrutura-99/estrutura-e-fontes.json')['fontes']:assert sha(R/f['fonte'])==f['sha256'],f['fonte']
 # Contas dirigidas e comparação com resultados históricos, registradas à parte.
 math_checks=load(A/'contas-conferidas.json');assert math_checks['registro']==130 and not math_checks['novos_parametros']
 result={'registro':130,'pdf_sha256':sha(pdf),'paginas':pages,'casos_conferidos':inspected,'tabelas_conferidas':count,'rotulos_simplificados':labels,'links_locais_conferidos':len(links),'links':links,'normalizacao_da_extracao':'Separação equivalente de números e letras para unidades como 9m e 9 m.','palavras_ausentes_no_pdf':dict(missing),'palavras_fora_da_pagina':outside,'fontes_antigas_preservadas':104,'casos_no_indice':59,'casos_revistos':59,'casos_pendentes':0,'lotes_pendentes':0,'mudancas_de_numero':number_log,'contas_dos_exemplos':'Conferidas; mesmos dados e resultados. Nenhuma mudança de regra; o único número novo é o nível 6 citado na ressalva sobre Ren.','mapa':'Sem mapas: os casos não dependem de posições num mapa.','limites':['Conferência documental; preservação integral final pelo manifesto.','Sem teste humano, nova simulação ou equilíbrio demonstrado.','Revisão integral e diagramação integrada continuam pendentes.']}
 (A/'conferencias.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n');print(json.dumps({k:v for k,v in result.items() if k not in ['links','paginas']},ensure_ascii=False,indent=2))
if __name__=='__main__':main()

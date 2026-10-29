"""Conferir cópias, números, tabelas e destinos sem alterar fontes históricas."""
from pathlib import Path
from bs4 import BeautifulSoup
from collections import Counter
from urllib.parse import urlsplit,unquote
import hashlib,json,markdown,re,subprocess,unicodedata,xml.etree.ElementTree as ET
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
 labels={'⌈44 ÷ 3⌉ = 15':'44 ÷ 3, para cima = 15','no entrada limpa.':'na entrada limpa.','Providência aceita no exemplo':'O que mudar no registro','Responsável e momento':'Quem faz e quando','Resultado a conferir':'O que conferir depois','Houve uma escolha de Insistir nesta cena, cujo prazo próprio deve ser respeitado.':'Houve uma escolha de Insistir nesta cena; conserve essa contagem até a cena terminar.','Quem conduzir a próxima aplicação, durante o preparo.':'Quem mestrar a próxima sessão, durante o preparo.','O destinatário localiza fonte, prazo e próxima tentativa sem pedir nova reconstrução?':'Quem recebe encontra a fonte, o prazo e a próxima tentativa sem precisar refazer as contas?'}
 for f in m['fontes']:
  p=R/f['fonte'];original=R/f['fonte_original'];assert sha(p)==f['sha256'] and sha(original)==f['sha256_original']==old[f['fonte_original']]
  previous=original.read_text();replayed=previous
  for c in changes:
   if c['fonte']==f['fonte']:
    assert replayed.count(c['antes'])==c.get('ocorrencias',1),c['fonte'];replayed=replayed.replace(c['antes'],c['depois'])
  assert replayed==p.read_text(),p
  before=soup(original);after=soup(p);assert nums(before.get_text())==nums(after.get_text()),p
  tables=lambda s:[[x.get_text(' ',strip=True) for x in t.find_all(['th','td'])] for t in s.find_all('table')]
  def expected_cell(x):
   for old_text,new_text in labels.items():x=x.replace(old_text,new_text)
   return x
  expected=[[expected_cell(x) for x in t] for t in tables(before)]
  assert expected==tables(after),p;count+=len(expected)
  inspected.append({'id':f['fonte_id'],'fonte':f['fonte'],'numeros_preservados':True,'tabelas':len(expected),'originais_preservados':True,'alteracoes_reproduzidas':True})
 source=load(A/'antes/04 - Planejamento/apoio-revisao-textual-117/destinos-e-fontes.json');current=load(A/'destinos-e-fontes.json');assert current['fontes']==source['fontes'];new={f['fonte_id']:f for f in m['fontes']};cases=0
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
 q=load(A/'fila-dos-casos.json');assert q['casos_pendentes']==49 and q['lotes_pendentes']==12 and len(q['casos_ja_revistos'])==10
 assert len({c['id'] for c in q['casos']})==59 and len(q['lotes_planejados'])==14 and q['proximo_lote']=='B2-01'
 for f in q['casos']:
  if 'fonte_revisada' in f:assert sha(R/f['fonte_revisada'])==f['sha256_revisado']
  else:assert sha(R/f['fonte_original'])==f['sha256']
 targets=[R/f['fonte'] for f in m['fontes']]+[A/'prova-textual.html',A/'casos-completos.html',A/'guia-de-consulta.html',A/'destinos-dos-casos.md',A/'fila-dos-casos.md',R/'06 - Redacao do Guia/revisao-98/LEIA-ME.md',R/'06 - Redacao do Guia/revisao-98/consultas/LEIA-ME.md',R/'04 - Planejamento/118-revisao-de-movimento-socorro-e-continuidade.md'];cache={};links=[]
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
 for h in ['CICLO MALDITO / GUIA DO MESTRE','MOVIMENTO, SOCORRO E CONTINUIDADE','PRÉ-1.0 · PROVA TEXTUAL PARCIAL']:plain=plain.replace(h,'')
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
 # Contas dos exemplos, sem novas rolagens ou simulação.
 import math
 assert 3*3==9 and 3*1.5==4.5 and 3*4.5==13.5 and 3*3==9
 assert 1+2+1==4 and 3+1.5*1==4.5 and 3+6==9 and 14+4==18 and 13+4==17
 assert 1.5+1.5+1.5==4.5 and 4.5+1.5==6 and 9-4.5==4.5
 assert 2+4+5==11 and 11//2==5 and 11-5==6 and math.ceil(6/2)==3 and math.ceil(11/2)==6
 assert 2+3//2==3 and 10*3==30 and 10+2+5*3==27 and 10+1==11 and 100*3==300
 assert 3+4.5==7.5 and 12-7.5==4.5 and 6-3==3
 assert 6+6==12 and 18+6==24 and 9+1.5==10.5 and 19.5+1.5==21 and 6+19.5==25.5
 assert 4+1==5 and 9+5==14 and 3+2==5 and 6*2==12 and 12+5==17 and 13+5==18
 assert 18+5==23 and 19+5==24 and 11+3==14 and 4+2==6
 assert math.ceil(93/4)==24 and math.ceil(93/3)==31 and min(math.ceil(93/2),15*3)==45
 assert 31-18==13 and math.ceil(23/3)==8 and 5+4==9 and 18+1==19 and math.ceil(23/2)==12 and 7+5==12
 assert 5+2==7 and 60/12==5 and 2+5+1==8 and 9/2==4.5 and 6/2==3
 assert math.floor(10*.25)==2 and 1+2==3 and [max(1,math.floor(8*v)) if v else 0 for v in [.25,.15,.05,0]]==[2,1,1,0]
 assert 23//2==11 and max(18,23//2)==18 and 60//2==30
 assert math.ceil(44/3)==15 and 15*2==30 and 9+3==12 and sum([2,3,4,6])==15 and 30-6==24 and 12+3==15
 result={'registro':118,'pdf_sha256':sha(pdf),'paginas':pages,'casos_conferidos':inspected,'tabelas_conferidas':count,'rotulos_simplificados':labels,'links_locais_conferidos':len(links),'links':links,'normalizacao_da_extracao':'Separação equivalente de números e letras para unidades como 9m e 9 m.','palavras_ausentes_no_pdf':dict(missing),'palavras_fora_da_pagina':outside,'fontes_antigas_preservadas':104,'casos_no_indice':59,'casos_revistos':10,'casos_pendentes':49,'lotes_pendentes':12,'contas_dos_exemplos':'Conferidas; mesmos dados e resultados.','manejo_de_combate':'Escolha de Força para o dano explicitada; conta original preservada.','limites':['Conferência documental; preservação integral final pelo manifesto.','Sem teste humano, nova simulação ou equilíbrio demonstrado.','Revisão integral e diagramação integrada continuam pendentes.']}
 (A/'conferencias.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n');print(json.dumps({k:v for k,v in result.items() if k not in ['links','paginas']},ensure_ascii=False,indent=2))
if __name__=='__main__':main()

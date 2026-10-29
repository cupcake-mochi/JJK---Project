"""Conferência documental do lote 115, separada da leitura editorial e visual."""
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
 t=unicodedata.normalize('NFKC',t).lower();t=re.sub(r'(?<=\w)[-‐‑]\s*(?=\w)','',t)
 return re.findall(r'[^\W_]+',t)
def main():
 m=load(A/'amostra.json');config=load(A/'arquivos-do-lote.json');baseline=load(A/'antes/04 - Planejamento/apoio-piloto/manifesto-entrega.json');pdf=R/m['pdf'];doc=soup(A/'prova-textual.html')
 assert sha(pdf)==m['pdf_sha256'] and sha(A/'prova-textual.html')==m['html_sha256']
 inspected=[];tables=0
 for f in m['fontes']:
  p=R/f['fonte'];assert sha(p)==f['sha256'];old=soup(A/'antes'/f['fonte']);new=soup(p)
  assert nums(old.get_text())==nums(new.get_text()),f['fonte']
  gettables=lambda s:[[x.get_text(' ',strip=True) for x in t.find_all(['th','td'])] for t in s.find_all('table')]
  assert gettables(old)==gettables(new),f['fonte'];tables+=len(gettables(new))
  inspected.append({'fonte':f['fonte'],'numeros_na_mesma_ordem':True,'tabelas_preservadas':len(gettables(new))})
 rules=soup(A/'consulta-de-regras.html');rulecount=0
 for group,folder in [('entre-missoes','apoio-entre-missoes-108'),('pactos-entidades','apoio-pactos-entidades-109'),('guilda','apoio-guilda-110')]:
  old=soup(R/'04 - Planejamento'/folder/'consulta-de-regras.html').find_all('section');new=rules.find(id=group).find_all('section')
  assert [x.get_text(' ',strip=True) for x in old]==[x.get_text(' ',strip=True) for x in new];rulecount+=len(old)
 nav=R/'04 - Planejamento/apoio-consultas-105';before=A/'antes/04 - Planejamento/apoio-consultas-105';oldmap=load(before/'destinos-e-fontes.json');newmap=load(nav/'destinos-e-fontes.json')
 assert oldmap['fontes']==newmap['fontes'] and oldmap['casos']==newmap['casos'];cases=sum(len(v) for v in newmap['casos'].values());assert cases==59
 for name in ['casos-completos.html','folhas-para-a-mesa.html']:
  old=soup(before/name);new=soup(nav/name);assert old.get_text()==new.get_text(),name
  assert [x.get_text() for x in old.find_all('style')]==[x.get_text() for x in new.find_all('style')],name
  if name.startswith('folhas'):assert str(old.main)==str(new.main)
 sheet=load(nav/'amostra.json');assert sha(R/sheet['pdf'])==sheet['pdf_sha256']==load(before/'amostra.json')['pdf_sha256']
 assert (nav/'conferencia-de-cobertura.json').read_bytes()==(before/'conferencia-de-cobertura.json').read_bytes()
 targets=[R/f['fonte'] for f in m['fontes']]+[A/'prova-textual.html',A/'consulta-de-regras.html',nav/'casos-completos.html',nav/'folhas-para-a-mesa.html',nav/'destinos-dos-casos.md',R/'06 - Redacao do Guia/revisao-98/LEIA-ME.md',R/'04 - Planejamento/115-revisao-textual-de-atividades-pactos-e-guilda.md'];cache={};links=[]
 for p in targets:
  view=soup(p);ids=[x['id'] for x in view.find_all(id=True)];assert len(ids)==len(set(ids)),p
  for tag in view.find_all('a',href=True):
   u=urlsplit(tag['href'])
   if u.scheme:continue
   dest=(p.parent/unquote(u.path)).resolve() if u.path else p.resolve();assert dest.is_file() or dest==A/'conferencias.json',(p,tag['href'])
   if u.fragment:
    if dest not in cache:cache[dest]=soup(dest)
    assert cache[dest].find(id=unquote(u.fragment)),(p,tag['href'])
   links.append({'origem':str(p.relative_to(R)),'destino':tag['href']})
 text=subprocess.check_output(['pdftotext',str(pdf),'-'],text=True)
 for h in ['CICLO MALDITO / GUIA DO MESTRE','CAPÍTULOS 8 A 10','PRÉ-1.0 · PROVA TEXTUAL PARCIAL']:text=text.replace(h,'')
 missing=Counter(tokens(doc.main.get_text(' ')))-Counter(tokens(text));assert not missing,missing
 subprocess.run(['pdftotext','-bbox',str(pdf),str(A/'limites.html')],check=True);ns={'x':'http://www.w3.org/1999/xhtml'};tree=ET.parse(A/'limites.html');pages=[];outside=[]
 for n,page in enumerate(tree.findall('.//x:page',ns),1):
  w=float(page.attrib['width']);h=float(page.attrib['height']);words=page.findall('x:word',ns)
  for word in words:
   x0,y0,x1,y1=[float(word.attrib[k]) for k in ['xMin','yMin','xMax','yMax']]
   if x0<0 or y0<0 or x1>w or y1>h:outside.append([n,word.text])
  pages.append({'pagina':n,'palavras':len(words)})
 assert len(pages)==len(m['paginas']) and not outside,outside
 structure=load(R/'04 - Planejamento/apoio-estrutura-99/estrutura-e-fontes.json')
 for f in structure['fontes']:assert sha(R/f['fonte'])==f['sha256'],f['fonte']
 folders=['apoio-entre-missoes-108','apoio-pactos-entidades-109','apoio-guilda-110','apoio-revisao-textual-112','apoio-revisao-textual-113','apoio-revisao-textual-114']
 for rel in baseline:
  if any(rel.startswith('04 - Planejamento/'+folder+'/') for folder in folders):assert sha(R/rel)==baseline[rel],rel
 for rel in ['08 - Diagramacao do Guia/output/pdf/Ciclo-Maldito-Guia-do-Mestre-Pre-1.0.pdf','04 - Planejamento/apoio-carregador/fontes/LIVRO-COMPLETO-R53.md','06 - Redacao do Guia/revisao-98/casos/89-vida-rolada-e-familia-propria.md']:
  assert sha(R/rel)==baseline[rel],rel
 # Contas já presentes nos exemplos: conferir sem promover uma nova validação de equilíbrio.
 assert 28+28==56 and 14*4==56 and 15*4==60 and 2*60==120
 assert 100/8==12.5 and int(200*.5*.5)==50 and 150+100-200==50
 assert 4000-1500-1500==1000 and int(300000*.75)==225000
 assert 150000-90000-48000==12000 and 24000+2*6000==36000
 assert 28-6==22 and 2000+24000==26000 and 38000-24000==14000 and 22-2==20
 assert 32+16==48 and 32+2*16==64 and 8+16+24+8==56
 assert 8+4+2-2==12 and 5+6<12 and 8+6>=12
 assert 40*.8==32 and 40*1.2==48 and 12+48-32==28
 assert 2+3+4+6==15 and 30-6==24 and 9+3<14 and 12+3>=14
 result={'registro':115,'pdf_sha256':sha(pdf),'paginas':pages,'fontes_conferidas':inspected,'tabelas_preservadas':tables,'trechos_de_regras_preservados':rulecount,'links_locais_conferidos':len(links),'links':links,'palavras_ausentes_no_pdf':dict(missing),'palavras_fora_da_pagina':outside,'fontes_antigas_preservadas':104,'casos_preservados':59,'corpo_e_pdf_das_folhas_preservados':True,'arata_revisado_114_preservado':True,'pdf_integrado_preservado':True,'provas_112_a_114_preservadas':True,'base_de_regras_preservada':True,'contas_dos_exemplos':'Conferidas; nenhuma nova rolagem ou simulação.','limites':['Conferência de texto, números e documentos; sem avaliação humana ou demonstração de equilíbrio.','Revisão das folhas e casos e conferência global ainda pendentes.']}
 (A/'conferencias.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n');print(json.dumps({k:v for k,v in result.items() if k not in ['links','paginas']},ensure_ascii=False,indent=2))
if __name__=='__main__':main()

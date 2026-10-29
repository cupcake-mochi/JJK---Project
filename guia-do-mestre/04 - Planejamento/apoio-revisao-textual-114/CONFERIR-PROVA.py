"""Verificar preservação, correção local de CD e remissões da prova parcial."""
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
 labels={'Conduta':'Comportamento','Resolução':'Efeito','Intervenção':'Como agir','Ultrapassa a aquisição':'Não é permitido por essa opção'}
 for f in m['fontes']:
  p=R/f['fonte'];assert sha(p)==f['sha256'];oldpath=R/config['caso_original'] if f['id']=='arata' else A/'antes'/f['fonte'];old=soup(oldpath);new=soup(p)
  expected=nums(old.get_text())
  if f['id']=='arata':
   assert expected.count('16')==1;expected[expected.index('16')]='18'
  assert expected==nums(new.get_text()),f['fonte']
  oldtables=[]
  for table in old.find_all('table'):
   cells=[x.get_text(' ',strip=True) for x in table.find_all(['th','td'])]
   oldtables.append([labels.get(x,x) if f['id']!='arata' else x for x in cells])
  newtables=[[x.get_text(' ',strip=True) for x in table.find_all(['th','td'])] for table in new.find_all('table')]
  assert oldtables==newtables,f['fonte'];tables+=len(newtables)
  inspected.append({'fonte':f['fonte'],'numeros_preservados':f['id']!='arata','excecao':'História CD 16 → 18' if f['id']=='arata' else None,'tabelas':len(newtables)})
 arata=(R/config['caso_revisado']).read_text();assert 'História CD 16' not in arata and 'História CD 18, Muito Difícil na escala fixa' in arata
 assert '15 + 4 = 19' in arata and '9 + 4 = 13' in arata
 raw=(R/'04 - Planejamento/apoio-carregador/fontes/LIVRO-COMPLETO-R53.md').read_text();scale=raw.split('##### Dificuldade',1)[1].split('Quando a dificuldade',1)[0]
 fixed=[int(l.split('|')[2].strip()) for l in scale.splitlines() if l.startswith('| ') and l.split('|')[2].strip().isdigit()];assert fixed==[6,10,14,18,22,26]
 assert 19>=18 and 13<18
 rules=soup(A/'consulta-de-regras.html')
 for group,folder in [('inimigos','apoio-inimigos-106'),('personagens','apoio-personagens-107')]:
  reference=soup(R/'04 - Planejamento'/folder/'consulta-de-regras.html')
  assert [x.get_text(' ',strip=True) for x in reference.find_all('section')]==[x.get_text(' ',strip=True) for x in rules.find(id=group).find_all('section')]
 nav=R/'04 - Planejamento/apoio-consultas-105';before=A/'antes/04 - Planejamento/apoio-consultas-105';oldmap=load(before/'destinos-e-fontes.json');newmap=load(nav/'destinos-e-fontes.json')
 assert oldmap['fontes']==newmap['fontes'];cases=0
 for group in oldmap['casos']:
  oldrows=oldmap['casos'][group];newrows=newmap['casos'][group];assert len(oldrows)==len(newrows)
  for old,new in zip(oldrows,newrows):
   cases+=1
   if old['id']=='s089':
    copy=dict(new)
    for key in ['fonte_revisada','sha256_revisado','motivo']:copy.pop(key)
    copy['consulta_atual']=old['consulta_atual'];assert copy==old
    assert new['fonte_revisada']==config['caso_revisado'] and sha(R/new['fonte_revisada'])==new['sha256_revisado']
    assert new['consulta_atual']==m['html']+'#arata'
   else:assert new==old,old['id']
 assert cases==59
 oldsheet=soup(before/'folhas-para-a-mesa.html');newsheet=soup(nav/'folhas-para-a-mesa.html');assert str(oldsheet.main)==str(newsheet.main) and oldsheet.get_text()==newsheet.get_text()
 for name in ['casos-completos.html','folhas-para-a-mesa.html']:
  old=soup(before/name);new=soup(nav/name);assert [x.get_text() for x in old.find_all('style')]==[x.get_text() for x in new.find_all('style')]
  if name=='casos-completos.html':
   for notice in old.find_all('p',class_='pendencia'):notice.decompose()
   for group in oldmap['casos']:assert old.find(id=group).get_text()==new.find(id=group).get_text(),group
   assert not new.find('p',class_='pendencia')
 sheet=load(nav/'amostra.json');assert sha(R/sheet['pdf'])==sheet['pdf_sha256']==load(before/'amostra.json')['pdf_sha256']
 assert (nav/'conferencia-de-cobertura.json').read_bytes()==(before/'conferencia-de-cobertura.json').read_bytes()
 targets=[R/f['fonte'] for f in m['fontes']]+[A/'prova-textual.html',A/'consulta-de-regras.html',nav/'casos-completos.html',nav/'folhas-para-a-mesa.html',nav/'destinos-dos-casos.md',R/'06 - Redacao do Guia/revisao-98/LEIA-ME.md',R/'04 - Planejamento/114-revisao-textual-de-inimigos-e-personagens.md'];cache={};links=[]
 for p in targets:
  view=soup(p);ids=[x['id'] for x in view.find_all(id=True)];assert len(ids)==len(set(ids)),p
  for tag in view.find_all('a',href=True):
   u=urlsplit(tag['href'])
   if u.scheme:continue
   dest=(p.parent/unquote(u.path)).resolve() if u.path else p.resolve();assert dest.is_file() or dest in [A/'conferencias.json',A/'revisao-final.json'],(p,tag['href'])
   if u.fragment:
    if dest not in cache:cache[dest]=soup(dest)
    assert cache[dest].find(id=unquote(u.fragment)),(p,tag['href'])
   links.append({'origem':str(p.relative_to(R)),'destino':tag['href']})
 text=subprocess.check_output(['pdftotext',str(pdf),'-'],text=True)
 for heading in ['CICLO MALDITO / GUIA DO MESTRE','CAPÍTULOS 6 E 7 / CASO ARATA','PRÉ-1.0 · PROVA TEXTUAL PARCIAL']:text=text.replace(heading,'')
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
 for rel in baseline:
  if any(rel.startswith('04 - Planejamento/'+folder+'/') for folder in ['apoio-inimigos-106','apoio-personagens-107','apoio-revisao-textual-112','apoio-revisao-textual-113']):assert sha(R/rel)==baseline[rel],rel
 book='08 - Diagramacao do Guia/output/pdf/Ciclo-Maldito-Guia-do-Mestre-Pre-1.0.pdf';assert sha(R/book)==baseline[book]
 base='04 - Planejamento/apoio-carregador/fontes/LIVRO-COMPLETO-R53.md';assert sha(R/base)==baseline[base]
 result={'registro':114,'pdf_sha256':sha(pdf),'paginas':pages,'fontes_conferidas':inspected,'tabelas_conferidas':tables,'rotulos_de_tabelas_simplificados':labels,'correcao_arata':{'cd_anterior':16,'cd_atual':18,'escala_fixa':fixed,'total_preservado':19,'resultado':'sucesso','limite':'Muda a exigência desta tarefa em 2; não define a CD de toda leitura nem demonstra equilíbrio das menores.'},'links_locais_conferidos':len(links),'links':links,'palavras_ausentes_no_pdf':dict(missing),'palavras_fora_da_pagina':outside,'fontes_antigas_preservadas':104,'casos_preservados':59,'casos_com_destino_atualizado':['s089'],'corpo_e_pdf_das_folhas_preservados':True,'pdf_integrado_preservado':True,'provas_112_e_113_preservadas':True,'base_de_regras_preservada':True,'limites':['Conferência de texto, números e documentos; sem nova simulação ou avaliação humana.','Revisão integral do livro e avaliação de equilíbrio continuam pendentes.']}
 (A/'conferencias.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n');print(json.dumps({k:v for k,v in result.items() if k not in ['links','paginas']},ensure_ascii=False,indent=2))
if __name__=='__main__':main()

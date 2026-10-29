"""Prova parcial da etapa 6, com abertura e capítulos 1–3; originais anteriores preservados."""
from pathlib import Path
from bs4 import BeautifulSoup
from urllib.parse import urlsplit, unquote
import hashlib, importlib.util, json, markdown, os, re, shutil, sys, subprocess
from markdown.extensions.toc import slugify
from weasyprint import HTML, default_url_fetcher
sys.dont_write_bytecode=True
A=Path(__file__).resolve().parent
R=A.parents[1]
S=R/'06 - Redacao do Guia/revisao-98'
FILES=['00-como-usar-este-livro.md','01-sua-primeira-missao.md','02-o-mundo-dos-feiticeiros.md','03-preparar-aventuras.md','03a-ideias-para-aventuras.md']
IDS={name:'c'+name.split('-')[0] for name in FILES}
HEADERS=['ABERTURA','CAPÍTULO 1','CAPÍTULO 2','CAPÍTULO 3','IDEIAS PARA AVENTURAS']
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def offline(url,*args,**kwargs):
 if urlsplit(url).scheme not in ['file','data']:raise ValueError('Recurso externo não permitido: '+url)
 return default_url_fetcher(url,*args,**kwargs)
def main():
 spec=importlib.util.spec_from_file_location('primeira100',R/'04 - Planejamento/apoio-primeira-missao-100/GERAR-AMOSTRA.py')
 mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod);mod.APOIO=A
 first=BeautifulSoup(mod.preparar_html(),'html.parser')
 mod.regras_de_apoio()
 rules=A/'consulta-de-regras.html';rules.write_text(rules.read_text().replace('href="capitulo-1.html"','href="prova-textual.html#c01"'))
 css=BeautifulSoup((R/'04 - Planejamento/apoio-conducao-102/capitulo-4.html').read_text(),'html.parser').style.get_text()
 css=css.replace("content:'NA MESA DE JOGO'","content:'ABERTURA E CAPÍTULOS 1–3'").replace("content:'PRÉ-1.0 · AMOSTRA DE LEITURA'","content:'PRÉ-1.0 · PROVA TEXTUAL PARCIAL'")
 css+='''
 .numero{font:700 18px Barlow,sans-serif;color:#6f5867;letter-spacing:.06em;margin:0 0 8px}
 @media print{.numero{font-size:10pt;margin-bottom:7pt}.folha>header>h1{margin-bottom:12pt}.folha[data-capitulo="c03"]{break-after:auto}.folha>header{break-after:avoid}.colunas h2{font-size:17pt;margin:11pt 0 7pt}.colunas h3{font-size:12.5pt}table{font-size:9.2pt;line-height:11.5pt}.abertura .colunas{column-count:2}.abertura{break-after:page}.mapa-ideias{column-span:all;margin:9pt 0;break-inside:avoid}.mapa-ideias img{width:100%;max-height:85mm;object-fit:contain}.mapa-ideias figcaption{font-size:8.8pt;line-height:11pt;margin-top:5pt}.grupo-tabela{break-inside:avoid}.colunas p.comentario{break-inside:avoid!important}.registro-resumo{break-inside:avoid}}
 '''
 css+='''@media print{.ficha-cotidiano>header{border-top:.7pt solid #9e2358;padding-top:7pt;margin-top:8pt}.cartao{break-inside:avoid;margin:0 0 9pt}.cartao h3{margin-top:8pt}}'''
 articles=[];headings=[]
 for i,name in enumerate(FILES):
  source=S/name;key=IDS[name]
  if i==1:
   parts=list(first.main.find_all('article',recursive=False))
   for j,article in enumerate(parts):
    article['class']=list(article.get('class',[]))+['capitulo-um']
    if j==0: article['data-capitulo']=key
   container=BeautifulSoup(''.join(str(x) for x in parts),'html.parser')
  else:
   parts=source.read_text().split('<!-- folha: despedida -->')
   container=BeautifulSoup('','html.parser')
   for j,part in enumerate(parts):
    body=BeautifulSoup(markdown.markdown(part,extensions=['tables','sane_lists','toc']),'html.parser')
    title=body.find(['h1','h2']);titletext=title.get_text();title.extract()
    article=container.new_tag('article',attrs={'class':'folha '+('ficha-cotidiano' if j else ('abertura' if i==0 else ''))})
    if j==0:article['data-capitulo']=key
    header=container.new_tag('header');num=container.new_tag('p',attrs={'class':'numero'});num.string=HEADERS[i] if j==0 else 'PREPARO PREENCHIDO';header.append(num)
    h=container.new_tag('h1' if j==0 else 'h2');h.string=titletext;header.append(h);article.append(header)
    if i==4:
     group=''
     short=['Oito situações para começar','Seis pessoas para encontrar','Quatro lugares para usar','Seis complicações possíveis']
     for h in list(body.find_all(['h2','h3'],recursive=False)):
      if h.name=='h2':group=h.get_text();continue
      if group in short:
       p=h.find_next_sibling();card=body.new_tag('div',attrs={'class':'cartao'});h.insert_before(card);card.append(h.extract())
       if p and p.name=='p':card.append(p.extract())
     for img in body.find_all('img'):
      p=img.parent;caption=p.find_next_sibling('p');figure=body.new_tag('figure',attrs={'class':'mapa-ideias'})
      p.insert_before(figure);figure.append(p.extract())
      if caption and caption.find('em'):
       caption.name='figcaption';figure.append(caption.extract())
    col=container.new_tag('div',attrs={'class':'colunas'})
    for child in list(body.contents):col.append(child.extract())
    article.append(col);container.append(article)
  # Prefixos mantêm as âncoras de cada texto únicas na prova reunida.
  used=set()
  for tag in container.find_all(id=True):
   tag['id']=key+'--'+tag['id'];used.add(tag['id'])
  for h in container.find_all(['h1','h2','h3','h4']):
   if not h.get('id'):
    stem=key+'--'+slugify(h.get_text(),'-');candidate=stem;n=1
    while candidate in used:candidate=stem+'-'+str(n);n+=1
    h['id']=candidate;used.add(candidate)
  container.find(attrs={'data-capitulo':key})['id']=key
  # Links das fontes apontam para esta prova quando o capítulo está nela.
  for tag in container.find_all(['a','img']):
   attr='href' if tag.name=='a' else 'src';url=tag.get(attr,'');u=urlsplit(url)
   if u.scheme:continue
   if not u.path:
    if u.fragment:tag[attr]='#'+key+'--'+unquote(u.fragment)
    continue
   if tag.name=='img' and i==1:
    tag[attr]='planta-do-anexo.svg';continue
   dest=(source.parent/unquote(u.path)).resolve()
   if dest.parent==S and dest.name in IDS:
    tag[attr]='#'+IDS[dest.name]+('--'+unquote(u.fragment) if u.fragment else '')
   else:
    assert dest.is_file(),(name,url,dest)
    tag[attr]=os.path.relpath(dest,A)+('#'+u.fragment if u.fragment else '')
  headings.append({'id':key,'fonte':str(source.relative_to(R)),'titulo':container.find('h1').get_text(),'sha256':sha(source)})
  articles.append(str(container))
 menu=''.join(f'<a href="#{h["id"]}">{h["titulo"]}</a>' for h in headings)
 doc='<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Revisão textual: abertura e capítulos 1–3 | Ciclo Maldito</title><style>'+css+'</style></head><body><nav aria-label="Conteúdo">'+menu+'</nav><p class="aviso-edicao">Prova parcial da etapa 6: abertura e capítulos 1–3, incluindo Ideias para aventuras. Os exemplos de inimigos continuam experimentais. <a href="consulta-de-regras.html">Regras da primeira missão</a>. A edição integrada anterior permanece preservada.</p><main>'+''.join(articles)+'</main><p class="rodape-tela"><a href="../112-revisao-textual-da-abertura-e-primeiros-capitulos.md">Registro da revisão e próximos passos</a></p></body></html>'
 (A/'prova-textual.html').write_text(doc)
 (A/'capitulo-1.html').unlink()
 out=A/'output/pdf/Ciclo-Maldito-Abertura-e-Capitulos-1-a-3-Revisao-Textual.pdf';out.parent.mkdir(parents=True,exist_ok=True)
 HTML(string=doc,base_url=str(A),url_fetcher=offline).write_pdf(str(out),pdf_identifier=b'revisao-textual-112')
 extracted=subprocess.check_output(['pdftotext',str(out),'-'],text=True).split('\f')
 if not extracted[-1].strip():extracted.pop()
 pages=[];plain=[]
 for n,text in enumerate(extracted,1):
  plain.append(f'\n=== PÁGINA {n} ===\n'+text);pages.append({'pagina':n,'palavras':len(text.split())})
 (A/'prova-textual.txt').write_text(''.join(plain))
 d={'registro':112,'fontes':headings,'html':'04 - Planejamento/apoio-revisao-textual-112/prova-textual.html','html_sha256':sha(A/'prova-textual.html'),'pdf':str(out.relative_to(R)),'pdf_sha256':sha(out),'paginas':pages,'estilo_base':'04 - Planejamento/apoio-conducao-102/capitulo-4.html','estilo_base_sha256':sha(R/'04 - Planejamento/apoio-conducao-102/capitulo-4.html'),'limite':'Prova parcial da revisão textual; não substitui o PDF integrado nem conclui a etapa 6 ou 7.'}
 (A/'amostra.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n');print(json.dumps({'paginas':len(pages),'palavras':[p['palavras'] for p in pages]},ensure_ascii=False))
if __name__=='__main__':main()

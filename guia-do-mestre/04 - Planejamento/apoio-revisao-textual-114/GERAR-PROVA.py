"""Prova parcial dos capítulos 6–7 e do caso Arata, com fontes antigas preservadas."""
from pathlib import Path
from bs4 import BeautifulSoup
from urllib.parse import urlsplit,unquote
import hashlib,json,markdown,os,subprocess
from weasyprint import HTML,default_url_fetcher
A=Path(__file__).resolve().parent;R=A.parents[1];S=R/'06 - Redacao do Guia/revisao-98'
FILES=[('c06','06-inimigos-e-perigos.md','CAPÍTULO 6'),('c07','07-personagens-e-tecnicas.md','CAPÍTULO 7'),('arata','casos/89-vida-rolada-e-familia-propria.md','ESTUDO DE CASO')]
LOCAL={str((S/name).resolve()):key for key,name,_ in FILES}
OLD={str((R/f['fonte']).resolve()):f for f in json.loads((R/'07 - Edicao de Leitura/mapa-editorial.json').read_text())['fontes']}
FORMS={str((R/f['fonte']).resolve()):f['id'] for f in json.loads((R/'04 - Planejamento/apoio-consultas-105/amostra.json').read_text())['fontes']}
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def offline(url,*args,**kwargs):
 if urlsplit(url).scheme not in ['file','data']:raise ValueError('Recurso externo não permitido: '+url)
 return default_url_fetcher(url,*args,**kwargs)
def css():
 text=BeautifulSoup((R/'04 - Planejamento/apoio-conducao-102/capitulo-4.html').read_text(),'html.parser').style.get_text()
 text=text.replace("content:'NA MESA DE JOGO'","content:'CAPÍTULOS 6 E 7 / CASO ARATA'").replace("content:'PRÉ-1.0 · AMOSTRA DE LEITURA'","content:'PRÉ-1.0 · PROVA TEXTUAL PARCIAL'")
 return text+'''@media print{table{font-size:9.2pt;line-height:11.5pt}.colunas p.bloco-curto{break-inside:auto!important}.colunas li{break-inside:avoid}.golpes td:nth-child(n+2){white-space:nowrap}.golpes th:nth-child(1){width:40%}.golpes th:nth-child(2){width:14%}.golpes th:nth-child(3),.golpes th:nth-child(4){width:23%}.larga{column-span:all;break-inside:avoid;margin:8pt 0}.formula{white-space:nowrap}.abertura-secao{break-inside:avoid}.colunas p.estado-final,.colunas p.comparacao,.colunas p.exemplo-numerico{break-inside:avoid!important}}'''
def rules(style):
 parts=[];meta=[]
 for n,folder,group in [(6,'apoio-inimigos-106','inimigos'),(7,'apoio-personagens-107','personagens')]:
  src=R/'04 - Planejamento'/folder/'consulta-de-regras.html';body=BeautifulSoup(src.read_text(),'html.parser');blocks=body.find_all('section');doc=BeautifulSoup('','html.parser');article=doc.new_tag('article',id=group);h=doc.new_tag('h2');h.string='Inimigos e perigos' if n==6 else 'Personagens e técnicas';article.append(h)
  for block in blocks:
   for node in [block,*block.find_all(id=True)]:
    if node.get('id'):node['id']=f'r{n}--'+node['id']
   for link in block.find_all('a',href=True):
    u=urlsplit(link['href'])
    if u.scheme:continue
    if not u.path:link['href']=f'#r{n}--'+u.fragment
    else:link['href']=os.path.relpath((src.parent/unquote(u.path)).resolve(),A)+('#'+u.fragment if u.fragment else '')
   article.append(block.extract())
  doc.append(article);parts.append(str(doc));meta.append({'fonte':str(src.relative_to(R)),'sha256':sha(src),'secoes':len(blocks)})
 html='<!doctype html><html lang="pt-BR"><meta charset="utf-8"><title>Livro de Regras 1.0 | Consultas</title><style>'+style+'main{max-width:900px;padding:30px;background:white}section{border-top:1px solid #ded4d9;padding:15px 0}article{margin-bottom:30px}</style><main><p><a href="prova-textual.html">Voltar à prova</a></p><h1>Livro de Regras 1.0</h1><p>Trechos publicados, sem reescrita. Modelos e números experimentais permanecem identificados no Guia.</p>'+''.join(parts)+'</main></html>'
 (A/'consulta-de-regras.html').write_text(html);return meta

def main():
 style=css();consultas=rules(style);articles=[];meta=[]
 for key,name,label in FILES:
  path=S/name;body=BeautifulSoup(markdown.markdown(path.read_text(),extensions=['tables','sane_lists','toc']),'html.parser');title=body.h1.get_text();body.h1.extract()
  for table in body.find_all('table'):
   heads=[x.get_text() for x in table.find_all('th')]
   if heads==['Golpe','Ataque','Dano','Crítico']:table['class']='golpes'
   if heads[:1]==['Confira'] or (key=='arata' and heads[:1]==['Momento']):
    previous=table.find_previous_sibling();items=[table]
    if previous and previous.name=='h3':items.insert(0,previous)
    wrap=body.new_tag('div',attrs={'class':'larga'});items[0].insert_before(wrap)
    for item in items:wrap.append(item.extract())
  for strong in body.find_all('strong'):
   if len(strong.get_text())<=35 and any(x in strong.get_text() for x in ['=','×','÷','−','+']):strong['class']='formula'
  for h in list(body.find_all('h3')):
   if h.get_text() in ['Ao subir de nível','A outra voz do Receptáculo','O Encarnado e a vida recebida','Corpo Amaldiçoado: reparar e descansar']:
    p=h.find_next_sibling('p');wrap=body.new_tag('div',attrs={'class':'abertura-secao'});h.insert_before(wrap);wrap.append(h.extract());wrap.append(p.extract())
  if key=='arata':
   for p in body.find_all('p'):
    if p.get_text().startswith('Registro ao fim:'):p['class']='estado-final'
    if p.get_text().startswith('Comparação.'):p['class']='comparacao'
    if p.get_text().startswith('No último descanso longo,'):p['class']='exemplo-numerico'
  if key=='c07':
   for p in body.find_all('p'):
    if p.get_text().startswith(('Liberação:', 'Técnica Máxima:')):p['class']='exemplo-numerico'
   h=next(x for x in body.find_all('h3') if x.get_text()=='Exemplo completo: o golpe por Toque')
   following=[];node=h.find_next_sibling()
   while node and node.name not in ['h1','h2','h3']:
    following.append(node);node=node.find_next_sibling()
   wrapper=body.new_tag('div',attrs={'class':'abertura-secao exemplo-toque'});h.insert_before(wrapper);wrapper.append(h.extract())
   for node in following:wrapper.append(node.extract())
  for tag in body.find_all(id=True):tag['id']=key+'--'+tag['id']
  for tag in body.find_all('a',href=True):
   u=urlsplit(tag['href'])
   if u.scheme:continue
   if not u.path:tag['href']='#'+key+'--'+unquote(u.fragment);continue
   dest=(path.parent/unquote(u.path)).resolve();assert dest.is_file(),(path,tag['href'])
   if str(dest) in LOCAL:tag['href']='#'+LOCAL[str(dest)]+('--'+unquote(u.fragment) if u.fragment else '')
   elif dest.parent==S and dest.name[:2] in ['00','01','02','03','04','05']:
    part=dest.name.split('-')[0];folder='apoio-revisao-textual-112' if part not in ['04','05'] else 'apoio-revisao-textual-113';tag['href']='../'+folder+'/prova-textual.html#c'+part+('--'+unquote(u.fragment) if u.fragment else '')
   elif str(dest) in FORMS:tag['href']='../apoio-consultas-105/folhas-para-a-mesa.html#'+FORMS[str(dest)]+('--'+u.fragment if u.fragment else '')
   elif str(dest) in OLD:
    old=OLD[str(dest)];anchor=old['ancoras'].get(u.fragment,u.fragment) if u.fragment else old['id'];tag['href']=os.path.relpath(R/'07 - Edicao de Leitura'/old['pagina'],A)+'#'+anchor
   else:tag['href']=os.path.relpath(dest,A)+('#'+u.fragment if u.fragment else '')
  articles.append(f'<article class="folha" id="{key}"><header><p class="numero">{label}</p><h1>{title}</h1></header><div class="colunas">{body}</div></article>')
  meta.append({'id':key,'fonte':str(path.relative_to(R)),'titulo':title,'sha256':sha(path)})
 nav=''.join(f'<a href="#{f["id"]}">{f["titulo"]}</a>' for f in meta)
 doc='<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Inimigos, personagens e Arata | Revisão textual</title><style>'+style+'</style></head><body><nav>'+nav+'<a href="consulta-de-regras.html">Regras para consulta</a></nav><p class="aviso-edicao">Prova parcial da etapa 6: capítulos 6–7 e caso Arata revisado. Modelos próprios conservam o caráter experimental. <a href="../apoio-revisao-textual-113/prova-textual.html">Capítulos 4 e 5</a>.</p><main>'+''.join(articles)+'</main><p class="rodape-tela"><a href="../114-revisao-textual-de-inimigos-e-personagens.md">Registro da revisão</a></p></body></html>'
 (A/'prova-textual.html').write_text(doc);out=A/'output/pdf/Ciclo-Maldito-Capitulos-6-e-7-e-Arata-Revisao-Textual.pdf';out.parent.mkdir(parents=True,exist_ok=True)
 HTML(string=doc,base_url=str(A),url_fetcher=offline).write_pdf(str(out),pdf_identifier=b'revisao-textual-114')
 pages=subprocess.check_output(['pdftotext',str(out),'-'],text=True).split('\f')
 if not pages[-1].strip():pages.pop()
 (A/'prova-textual.txt').write_text(''.join(f'\n=== PÁGINA {i} ===\n{t}' for i,t in enumerate(pages,1)))
 data={'registro':114,'fontes':meta,'consultas':consultas,'html':str((A/'prova-textual.html').relative_to(R)),'html_sha256':sha(A/'prova-textual.html'),'pdf':str(out.relative_to(R)),'pdf_sha256':sha(out),'paginas':[{'pagina':i,'palavras':len(t.split())} for i,t in enumerate(pages,1)],'limite':'Prova parcial. Capítulos 8–10, consultas e conferência global ainda pendentes; fonte original de Arata preservada.'}
 (A/'amostra.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n');print(json.dumps({'paginas':len(pages),'palavras':[len(t.split()) for t in pages]},ensure_ascii=False))
if __name__=='__main__':main()

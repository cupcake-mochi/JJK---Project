"""Prova parcial dos capítulos 4 e 5, com consultas publicadas e sem alterar amostras antigas."""
from pathlib import Path
from bs4 import BeautifulSoup
from urllib.parse import urlsplit,unquote
import hashlib,json,markdown,os,subprocess
from weasyprint import HTML,default_url_fetcher
A=Path(__file__).resolve().parent;R=A.parents[1];S=R/'06 - Redacao do Guia/revisao-98'
FILES=['04-na-mesa-de-jogo.md','05-criar-uma-campanha.md']
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def offline(url,*args,**kwargs):
 if urlsplit(url).scheme not in ['file','data']:raise ValueError('Recurso externo não permitido: '+url)
 return default_url_fetcher(url,*args,**kwargs)
def stylesheet():
 css=BeautifulSoup((R/'04 - Planejamento/apoio-conducao-102/capitulo-4.html').read_text(),'html.parser').style.get_text()
 css=css.replace("content:'NA MESA DE JOGO'","content:'CAPÍTULOS 4 E 5'").replace("content:'PRÉ-1.0 · AMOSTRA DE LEITURA'","content:'PRÉ-1.0 · PROVA TEXTUAL PARCIAL'")
 return css+'''@media print{table{font-size:9.2pt;line-height:11.5pt}.colunas p.comentario{break-inside:avoid!important}.colunas li{break-inside:avoid}.colunas p.bloco-curto{break-inside:avoid!important}}'''
def rules(css):
 sections=[];metadata=[]
 for chapter,folder,group in [(4,'apoio-conducao-102','conducao'),(5,'apoio-campanha-103','campanha')]:
  src=R/'04 - Planejamento'/folder/'consulta-de-regras.html';s=BeautifulSoup(src.read_text(),'html.parser')
  blocks=s.find_all('section');container=BeautifulSoup('','html.parser');wrapper=container.new_tag('article',id=group)
  heading=container.new_tag('h2');heading.string='Condução' if chapter==4 else 'Campanha';wrapper.append(heading)
  for block in blocks:
   for item in [block,*block.find_all(id=True)]:
    if item.get('id'):item['id']='r'+str(chapter)+'--'+item['id']
   for link in block.find_all('a',href=True):
    u=urlsplit(link['href'])
    if u.scheme:continue
    if not u.path:link['href']='#r'+str(chapter)+'--'+u.fragment
    else:link['href']=os.path.relpath((src.parent/unquote(u.path)).resolve(),A)+('#'+u.fragment if u.fragment else '')
   wrapper.append(block.extract())
  container.append(wrapper);sections.append(str(container));metadata.append({'fonte':str(src.relative_to(R)),'sha256':sha(src),'secoes':len(blocks)})
 doc='<!doctype html><html lang="pt-BR"><meta charset="utf-8"><title>Livro de Regras 1.0 | Consultas</title><style>'+css+'main{max-width:900px;padding:30px;background:white}section{border-top:1px solid #ded4d9;padding:15px 0}article{margin-bottom:30px}</style><main><p><a href="prova-textual.html">Voltar aos capítulos 4 e 5</a></p><h1>Livro de Regras 1.0</h1><p>Trechos publicados preservados das consultas anteriores; exemplos e orientações do Guia estão na prova.</p>'+''.join(sections)+'</main></html>'
 (A/'consulta-de-regras.html').write_text(doc);return metadata

def main():
 css=stylesheet();consultas=rules(css);articles=[];sources=[]
 for n,name in enumerate(FILES,4):
  p=S/name;key=f'c0{n}';body=BeautifulSoup(markdown.markdown(p.read_text(),extensions=['tables','sane_lists','toc']),'html.parser');title=body.h1.get_text();body.h1.extract()
  for para in body.find_all('p'):
   if para.get_text().startswith('Na condução.'):para['class']=['comentario']
   first=next((c for c in para.contents if str(c).strip()),None)
   if getattr(first,'name',None)=='strong':para['class']=para.get('class',[])+['bloco-curto']
  for table in list(body.find_all('table')):
   prev=table.find_previous_sibling();items=[table]
   if prev and prev.name=='p':items.insert(0,prev);prev=prev.find_previous_sibling()
   if prev and prev.name in ['h2','h3']:items.insert(0,prev)
   wrapper=body.new_tag('div',attrs={'class':'grupo-tabela'});items[0].insert_before(wrapper)
   for item in items:wrapper.append(item.extract())
  for tag in body.find_all(id=True):tag['id']=key+'--'+tag['id']
  for tag in body.find_all('a',href=True):
   u=urlsplit(tag['href'])
   if u.scheme:continue
   if not u.path:
    tag['href']='#'+key+'--'+unquote(u.fragment);continue
   target=(p.parent/unquote(u.path)).resolve();assert target.is_file(),(p,tag['href'])
   if target.parent==S and target.name in FILES:tag['href']='#c0'+str(FILES.index(target.name)+4)+('--'+unquote(u.fragment) if u.fragment else '')
   elif target.parent==S and target.name in ['00-como-usar-este-livro.md','01-sua-primeira-missao.md','02-o-mundo-dos-feiticeiros.md','03-preparar-aventuras.md','03a-ideias-para-aventuras.md']:
    code='c'+target.name.split('-')[0];tag['href']='../apoio-revisao-textual-112/prova-textual.html#'+code+('--'+u.fragment if u.fragment else '')
   else:tag['href']=os.path.relpath(target,A)+('#'+u.fragment if u.fragment else '')
  articles.append(f'<article class="folha" id="{key}"><header><p class="numero">CAPÍTULO {n}</p><h1>{title}</h1></header><div class="colunas">{body}</div></article>')
  sources.append({'id':key,'fonte':str(p.relative_to(R)),'sha256':sha(p),'titulo':title})
 menu=''.join(f'<a href="#{f["id"]}">{f["titulo"]}</a>' for f in sources)
 doc='<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Na mesa e na campanha | Revisão textual</title><style>'+css+'</style></head><body><nav aria-label="Conteúdo">'+menu+'<a href="consulta-de-regras.html">Regras para consulta</a></nav><p class="aviso-edicao">Prova parcial da etapa 6: capítulos 4 e 5. A edição integrada anterior permanece preservada. <a href="../apoio-revisao-textual-112/prova-textual.html">Ler a abertura e os capítulos 1 a 3</a>.</p><main>'+''.join(articles)+'</main><p class="rodape-tela"><a href="../113-revisao-textual-da-mesa-e-da-campanha.md">Registro da revisão</a></p></body></html>'
 (A/'prova-textual.html').write_text(doc)
 out=A/'output/pdf/Ciclo-Maldito-Capitulos-4-e-5-Revisao-Textual.pdf';out.parent.mkdir(parents=True,exist_ok=True)
 HTML(string=doc,base_url=str(A),url_fetcher=offline).write_pdf(str(out),pdf_identifier=b'revisao-textual-113')
 extracted=subprocess.check_output(['pdftotext',str(out),'-'],text=True).split('\f')
 if not extracted[-1].strip():extracted.pop()
 (A/'prova-textual.txt').write_text(''.join(f'\n=== PÁGINA {i} ===\n{t}' for i,t in enumerate(extracted,1)))
 meta={'registro':113,'fontes':sources,'consultas':consultas,'html':str((A/'prova-textual.html').relative_to(R)),'html_sha256':sha(A/'prova-textual.html'),'pdf':str(out.relative_to(R)),'pdf_sha256':sha(out),'paginas':[{'pagina':i,'palavras':len(t.split())} for i,t in enumerate(extracted,1)],'limite':'Prova parcial; a etapa 6, a integração e a revisão visual integral continuam em andamento.'}
 (A/'amostra.json').write_text(json.dumps(meta,ensure_ascii=False,indent=2)+'\n');print(json.dumps({'paginas':len(extracted),'palavras':[len(t.split()) for t in extracted]}))
if __name__=='__main__':main()

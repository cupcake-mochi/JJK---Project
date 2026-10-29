"""Prova parcial dos capítulos 8–10, com fontes antigas preservadas."""
from pathlib import Path
from bs4 import BeautifulSoup
from urllib.parse import urlsplit,unquote
import hashlib,json,markdown,os,subprocess
from weasyprint import HTML,default_url_fetcher
A=Path(__file__).resolve().parent;R=A.parents[1];S=R/'06 - Redacao do Guia/revisao-98'
FILES=[('c08','08-entre-missoes.md','CAPÍTULO 8'),('c09','09-pactos-e-entidades.md','CAPÍTULO 9'),('c10','10-jogar-em-guilda.md','CAPÍTULO 10')]
LOCAL={str((S/name).resolve()):key for key,name,_ in FILES}
OLD={str((R/f['fonte']).resolve()):f for f in json.loads((R/'07 - Edicao de Leitura/mapa-editorial.json').read_text())['fontes']}
FORMS={str((R/f['fonte']).resolve()):f['id'] for f in json.loads((R/'04 - Planejamento/apoio-consultas-105/amostra.json').read_text())['fontes']}
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def offline(url,*args,**kwargs):
 if urlsplit(url).scheme not in ['file','data']:raise ValueError('Recurso externo não permitido: '+url)
 return default_url_fetcher(url,*args,**kwargs)
def css():
 text=BeautifulSoup((R/'04 - Planejamento/apoio-conducao-102/capitulo-4.html').read_text(),'html.parser').style.get_text()
 text=text.replace("content:'NA MESA DE JOGO'","content:'CAPÍTULOS 8 A 10'").replace("content:'PRÉ-1.0 · AMOSTRA DE LEITURA'","content:'PRÉ-1.0 · PROVA TEXTUAL PARCIAL'")
 return text+'''@media print{table{font-size:9.2pt;line-height:11.5pt}.colunas p.bloco-curto{break-inside:auto!important}.colunas li{break-inside:avoid}.golpes td:nth-child(n+2){white-space:nowrap}.golpes th:nth-child(1){width:40%}.golpes th:nth-child(2){width:14%}.golpes th:nth-child(3),.golpes th:nth-child(4){width:23%}.larga{column-span:all;break-inside:avoid;margin:8pt 0}.formula{white-space:nowrap}.abertura-secao{break-inside:avoid}.colunas p.estado-final,.colunas p.comparacao,.colunas p.exemplo-numerico{break-inside:avoid!important}#c10 .colunas p{margin-bottom:4.5pt}#c10 table th,#c10 table td{padding:3pt 4pt}#c10 .colunas h3{margin:8pt 0 5pt}#c10 .colunas h2{margin:10pt 0 6pt}#c10 .larga th:first-child{width:20%}#c10 .fechamento-exemplo{column-span:all;break-inside:avoid;margin:2pt 0 6pt}}'''
def rules(style):
 parts=[];meta=[]
 for n,folder,group in [(8,'apoio-entre-missoes-108','entre-missoes'),(9,'apoio-pactos-entidades-109','pactos-entidades'),(10,'apoio-guilda-110','guilda')]:
  src=R/'04 - Planejamento'/folder/'consulta-de-regras.html';body=BeautifulSoup(src.read_text(),'html.parser');blocks=body.find_all('section');doc=BeautifulSoup('','html.parser');article=doc.new_tag('article',id=group);h=doc.new_tag('h2');h.string={8:'Entre missões',9:'Pactos e entidades',10:'Jogar em guilda'}[n];article.append(h)
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
   if key=='c10' and heads[0] in ['O que continua','Ao fim do percurso']:
    wrap=body.new_tag('div',attrs={'class':'larga'});table.insert_before(wrap);wrap.append(table.extract())
  if key=='c10':
   p=next(p for p in body.find_all('p') if p.get_text().startswith('Nenhum descanso foi concluído.'));p['class']='fechamento-exemplo'
  for strong in body.find_all('strong'):
   if len(strong.get_text())<=35 and any(x in strong.get_text() for x in ['=','×','÷','−','+']):strong['class']='formula'
  for p in body.find_all('p'):
   if key=='c08' and p.get_text().startswith(('O reparo publicado','Rina trabalha','No caso de Kenji,','No Anel de Testemunho,','O projeto com uma falha','Com três exigidas,','Uma longa ocupa')):p['class']='exemplo-numerico'
   if key=='c09' and p.get_text().startswith(('Ren tem 6 PV','Overtime é','Com máximo 40','Rina, nível','O projeto local','Foram 48 horas','Uma operação de 32','É um teste por Classe')):p['class']='exemplo-numerico'
   if key=='c10' and p.get_text().startswith(('O registro da queda','De B0, Akira','Na fase 2,')):p['class']='exemplo-numerico'
  for h in list(body.find_all('h3')):
   if h.get_text() in ['O ciclo da guilda','O que passa para o ciclo seguinte','Criar o Vigia do depósito','A urgência de Mei','Uma retomada possível','Revelar a própria técnica']:
    p=h.find_next_sibling('p');wrap=body.new_tag('div',attrs={'class':'abertura-secao'});h.insert_before(wrap);wrap.append(h.extract());wrap.append(p.extract())
  for tag in body.find_all(id=True):tag['id']=key+'--'+tag['id']
  for tag in body.find_all('a',href=True):
   u=urlsplit(tag['href'])
   if u.scheme:continue
   if not u.path:tag['href']='#'+key+'--'+unquote(u.fragment);continue
   dest=(path.parent/unquote(u.path)).resolve();assert dest.is_file(),(path,tag['href'])
   rulegroups={'apoio-entre-missoes-108':'entre-missoes','apoio-pactos-entidades-109':'pactos-entidades','apoio-guilda-110':'guilda'}
   if dest.name=='consulta-de-regras.html' and dest.parent.name in rulegroups:tag['href']='consulta-de-regras.html#'+rulegroups[dest.parent.name]
   elif str(dest) in LOCAL:tag['href']='#'+LOCAL[str(dest)]+('--'+unquote(u.fragment) if u.fragment else '')
   elif dest.parent==S and dest.name[:2] in ['00','01','02','03','03a','04','05','06','07']:
    part=dest.name.split('-')[0];folder='apoio-revisao-textual-114' if part in ['06','07'] else ('apoio-revisao-textual-113' if part in ['04','05'] else 'apoio-revisao-textual-112');tag['href']='../'+folder+'/prova-textual.html#c'+part+('--'+unquote(u.fragment) if u.fragment else '')
   elif str(dest) in FORMS:tag['href']='../apoio-consultas-105/folhas-para-a-mesa.html#'+FORMS[str(dest)]+('--'+u.fragment if u.fragment else '')
   elif str(dest) in OLD:
    old=OLD[str(dest)];anchor=old['ancoras'].get(u.fragment,u.fragment) if u.fragment else old['id'];tag['href']=os.path.relpath(R/'07 - Edicao de Leitura'/old['pagina'],A)+'#'+anchor
   else:tag['href']=os.path.relpath(dest,A)+('#'+u.fragment if u.fragment else '')
  articles.append(f'<article class="folha" id="{key}"><header><p class="numero">{label}</p><h1>{title}</h1></header><div class="colunas">{body}</div></article>')
  meta.append({'id':key,'fonte':str(path.relative_to(R)),'titulo':title,'sha256':sha(path)})
 nav=''.join(f'<a href="#{f["id"]}">{f["titulo"]}</a>' for f in meta)
 doc='<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Entre missões, Pactos e guilda | Revisão textual</title><style>'+style+'</style></head><body><nav>'+nav+'<a href="consulta-de-regras.html">Regras para consulta</a></nav><p class="aviso-edicao">Prova parcial da etapa 6: capítulos 8–10. Modelos próprios conservam o caráter experimental. <a href="../apoio-revisao-textual-114/prova-textual.html">Capítulos 6 e 7</a>.</p><main>'+''.join(articles)+'</main><p class="rodape-tela"><a href="../115-revisao-textual-de-atividades-pactos-e-guilda.md">Registro da revisão</a></p></body></html>'
 (A/'prova-textual.html').write_text(doc);out=A/'output/pdf/Ciclo-Maldito-Capitulos-8-a-10-Revisao-Textual.pdf';out.parent.mkdir(parents=True,exist_ok=True)
 HTML(string=doc,base_url=str(A),url_fetcher=offline).write_pdf(str(out),pdf_identifier=b'revisao-textual-115')
 pages=subprocess.check_output(['pdftotext',str(out),'-'],text=True).split('\f')
 if not pages[-1].strip():pages.pop()
 (A/'prova-textual.txt').write_text(''.join(f'\n=== PÁGINA {i} ===\n{t}' for i,t in enumerate(pages,1)))
 data={'registro':115,'fontes':meta,'consultas':consultas,'html':str((A/'prova-textual.html').relative_to(R)),'html_sha256':sha(A/'prova-textual.html'),'pdf':str(out.relative_to(R)),'pdf_sha256':sha(out),'paginas':[{'pagina':i,'palavras':len(t.split())} for i,t in enumerate(pages,1)],'limite':'Prova parcial. Revisão das folhas e casos, conferência global e integração ainda pendentes. Fontes antigas preservadas.'}
 (A/'amostra.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n');print(json.dumps({'paginas':len(pages),'palavras':[len(t.split()) for t in pages]},ensure_ascii=False))
if __name__=='__main__':main()

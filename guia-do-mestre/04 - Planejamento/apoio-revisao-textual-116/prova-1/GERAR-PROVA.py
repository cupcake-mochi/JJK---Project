"""Prova das três folhas curtas e dos dois exemplos, preservando a edição 105."""
from pathlib import Path
from bs4 import BeautifulSoup,Comment
from urllib.parse import urlsplit,unquote
from weasyprint import HTML,default_url_fetcher
import hashlib,json,markdown,os,re,subprocess
A=Path(__file__).resolve().parent;R=A.parents[1];S=R/'06 - Redacao do Guia/revisao-98/consultas'
FILES=[('A1-preparar-a-missao.md','preparar','formulario'),('A2-conduzir-a-sessao.md','conduzir','consulta'),('A4-retomar-a-missao.md','retomar','formulario'),('A1-exemplo-despedida.md','exemplo-preparo','exemplo'),('A4-exemplo-sala-de-conservacao.md','exemplo-retomada','exemplo')]
LOCAL={str((S/name).resolve()):ident for name,ident,_ in FILES}
OLD={str((R/x['fonte']).resolve()):x for x in json.loads((R/'07 - Edicao de Leitura/mapa-editorial.json').read_text())['fontes']}
STAGED={}
for f in (S.parent).glob('*.md'):
 num=f.name.split('-')[0]
 if num.isdigit() or num=='03a':
  n=int(num[:2]);folder=112 if n<=3 else 113 if n<=5 else 114 if n<=7 else 115
  STAGED[str(f.resolve())]=(R/f'04 - Planejamento/apoio-revisao-textual-{folder}/prova-textual.html','c'+num)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def offline(url,*args,**kwargs):
 if urlsplit(url).scheme not in ['file','data']:raise ValueError(url)
 return default_url_fetcher(url,*args,**kwargs)
def convert(p,prefix):
 soup=BeautifulSoup(markdown.markdown(p.read_text(),extensions=['tables','sane_lists','toc']),'html.parser')
 for node in soup.find_all(id=True):node['id']=prefix+'--'+node['id']
 for c in list(soup.find_all(string=lambda x:isinstance(x,Comment))):
  if m:=re.search(r'espaco:\s*(\d+)',str(c)):
   b=soup.new_tag('div',attrs={'class':'linhas','aria-hidden':'true'})
   for _ in range(int(m[1])):b.append(soup.new_tag('span',attrs={'class':'linha'}))
   c.replace_with(b)
 for link in soup.find_all('a',href=True):
  u=urlsplit(link['href'])
  if u.scheme:continue
  if not u.path:
   if u.fragment:link['href']='#'+prefix+'--'+unquote(u.fragment)
   continue
  target=(p.parent/unquote(u.path)).resolve();assert target.is_file(),(p,link['href'])
  if str(target) in LOCAL:link['href']='#'+LOCAL[str(target)]+('--'+u.fragment if u.fragment else '')
  elif str(target) in STAGED:
   dest,key=STAGED[str(target)];link['href']=os.path.relpath(dest,A)+'#'+key+('--'+unquote(u.fragment) if u.fragment else '')
  elif str(target) in OLD:
   f=OLD[str(target)];anchor=f['ancoras'].get(u.fragment,u.fragment) if u.fragment else f['id'];link['href']=os.path.relpath(R/'07 - Edicao de Leitura'/f['pagina'],A)+'#'+anchor
  else:link['href']=os.path.relpath(target,A)+('#'+u.fragment if u.fragment else '')
 return soup
def main():
 css=BeautifulSoup((R/'04 - Planejamento/apoio-consultas-105/folhas-para-a-mesa.html').read_text(),'html.parser').style.get_text().replace("content:'PRÉ-1.0 · AMOSTRA DE LEITURA'","content:'PRÉ-1.0 · PROVA TEXTUAL PARCIAL'")
 css+='@media print{.exemplo-retomada .colunas p.estado-urgente{break-inside:avoid}.folha>h1{break-after:avoid}}'
 parts=[];sources=[]
 for name,key,kind in FILES:
  p=S/name;body=convert(p,key);title=body.h1.get_text();body.h1.extract()
  if key=='exemplo-retomada':
   for par in body.find_all('p'):
    if par.get_text().startswith(('Socorro de Mei:','Envenenado:','Conferência:')):par['class']='estado-urgente'
  parts.append(f'<article class="folha {kind} {key}" id="{key}"><h1>{title}</h1><div class="colunas">{body}</div></article>')
  sources.append({'fonte':str(p.relative_to(R)),'sha256':sha(p),'id':key,'tipo':kind,'titulo':title})
 guide=convert(S/'LEIA-ME.md','escolher');nav=''.join(f'<a href="#{x["id"]}">{x["titulo"]}</a>' for x in sources)
 doc='<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Folhas para a mesa | Revisão textual</title><style>'+css+'</style></head><body><nav>'+nav+'<a href="#escolher">Escolher uma folha</a><a href="fila-dos-casos.html">Fila de revisão dos casos</a></nav><p class="aviso-edicao">Revisão 116: três folhas curtas e dois exemplos. As linhas são para impressão; este PDF não tem campos interativos.</p><main>'+''.join(parts)+'</main><section id="escolher" class="indice">'+str(guide)+'</section><p class="rodape-tela"><a href="../116-revisao-das-folhas-e-fila-dos-casos.md">Registro da revisão</a></p></body></html>'
 (A/'prova-textual.html').write_text(doc);pdf=A/'output/pdf/Ciclo-Maldito-Folhas-para-a-Mesa-Revisao-Textual.pdf';pdf.parent.mkdir(parents=True,exist_ok=True)
 HTML(string=doc,base_url=str(A),url_fetcher=offline).write_pdf(str(pdf),pdf_identifier=b'revisao-textual-116')
 pages=subprocess.check_output(['pdftotext',str(pdf),'-'],text=True).split('\f')
 if not pages[-1].strip():pages.pop()
 (A/'prova-textual.txt').write_text(''.join(f'\n=== PÁGINA {i} ===\n{p}' for i,p in enumerate(pages,1)))
 data={'registro':116,'fontes':sources,'guia_de_escolha':{'fonte':str((S/'LEIA-ME.md').relative_to(R)),'sha256':sha(S/'LEIA-ME.md')},'html':str((A/'prova-textual.html').relative_to(R)),'html_sha256':sha(A/'prova-textual.html'),'pdf':str(pdf.relative_to(R)),'pdf_sha256':sha(pdf),'paginas':[{'pagina':i,'palavras':len(p.split())} for i,p in enumerate(pages,1)],'limite':'Cinco folhas revistas; casos extensos, demais consultas e conferência global ainda pendentes. Pacote 105 preservado como histórico.'}
 (A/'amostra.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n');print(json.dumps({'paginas':len(pages),'palavras':[len(p.split()) for p in pages]},ensure_ascii=False))
if __name__=='__main__':main()

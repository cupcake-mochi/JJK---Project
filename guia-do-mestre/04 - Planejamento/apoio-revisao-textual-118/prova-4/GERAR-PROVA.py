"""Prova dos cinco casos B1-02, com as fontes antigas preservadas."""
from pathlib import Path
from bs4 import BeautifulSoup
from urllib.parse import urlsplit,unquote
from weasyprint import HTML,default_url_fetcher
import hashlib,json,markdown,os,subprocess
A=Path(__file__).resolve().parent;R=A.parents[1];S=R/'06 - Redacao do Guia/revisao-98';CFG=json.loads((A/'arquivos-do-lote.json').read_text());FILES=CFG['casos']
LOCAL={str((R/f[k]).resolve()):f['id_prova'] for f in FILES for k in ['fonte_original','fonte_revisada']}
OLD={str((R/f['fonte']).resolve()):f for f in json.loads((R/'07 - Edicao de Leitura/mapa-editorial.json').read_text())['fontes']}
FORMS={str((R/f['fonte']).resolve()):f['id'] for f in json.loads((R/'04 - Planejamento/apoio-revisao-textual-116/amostra.json').read_text())['fontes']}
REVISED={str((R/f[k]).resolve()):f['consulta_atual'] for rows in json.loads((R/'04 - Planejamento/apoio-revisao-textual-117/destinos-e-fontes.json').read_text())['casos'].values() for f in rows for k in ['fonte','fonte_revisada'] if k in f and f.get('fonte_revisada')}
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def offline(url,*args,**kwargs):
 if urlsplit(url).scheme not in ['file','data']:raise ValueError(url)
 return default_url_fetcher(url,*args,**kwargs)
def main():
 css=BeautifulSoup((R/'04 - Planejamento/apoio-revisao-textual-115/prova-textual.html').read_text(),'html.parser').style.get_text().replace('CAPÍTULOS 8 A 10','MOVIMENTO, SOCORRO E CONTINUIDADE')
 css+='@media print{.larga th{white-space:normal}.colunas p.conta{break-inside:avoid}.colunas table{break-inside:avoid}.abertura-caso{break-inside:avoid}#socorro{break-after:auto}#recuperacao{padding-top:12pt}#recuperacao .colunas p{margin-bottom:5pt}#recuperacao table th,#recuperacao table td{padding:3pt 4pt}#recuperacao .colunas h2{margin:10pt 0 6pt}}'
 articles=[];meta=[]
 for f in FILES:
  key=f['id_prova'];p=R/f['fonte_revisada'];body=BeautifulSoup(markdown.markdown(p.read_text(),extensions=['tables','sane_lists','toc']),'html.parser');title=body.h1.get_text();body.h1.extract()
  for table in body.find_all('table'):
   heads=[x.get_text() for x in table.find_all('th')]
   if len(heads)>=3 or key=='passagem':
    items=[table];prev=table.find_previous_sibling()
    if prev and prev.name in ['h2','h3']:items.insert(0,prev)
    elif prev and prev.name=='p' and len(prev.get_text().split())<75:
     h=prev.find_previous_sibling()
     if h and h.name in ['h2','h3']:items=[h,prev,table]
    wrap=body.new_tag('div',attrs={'class':'larga'});items[0].insert_before(wrap)
    for node in items:wrap.append(node.extract())
  for strong in body.find_all('strong'):
   if len(strong.get_text())<=35 and any(x in strong.get_text() for x in ['=','×','÷','−','+']):strong['class']='formula'
  for par in body.find_all('p'):
   if par.get_text().startswith(('Aoi escolhe tentar.','Com dado 14, Haru','Os 3 m reais','Com dado 10 + 4','O alvo decide usar','Emi escolhe tentar.','Se Emi ainda tiver','Kaito é treinado','**Exemplo','Exemplo:','Exemplo de carga:','Comparação:','Quando Integridade e Exaustão')):par['class']='conta'
  for tag in body.find_all(id=True):tag['id']=key+'--'+tag['id']
  for tag in body.find_all('a',href=True):
   u=urlsplit(tag['href'])
   if u.scheme:continue
   if not u.path:tag['href']='#'+key+'--'+unquote(u.fragment);continue
   dest=(p.parent/unquote(u.path)).resolve();assert dest.is_file(),(p,tag['href'])
   if str(dest) in LOCAL:tag['href']='#'+LOCAL[str(dest)]+('--'+unquote(u.fragment) if u.fragment else '')
   elif str(dest) in REVISED:tag['href']=os.path.relpath(R/REVISED[str(dest)],A)
   elif str(dest) in FORMS:tag['href']='../apoio-revisao-textual-116/prova-textual.html#'+FORMS[str(dest)]+('--'+unquote(u.fragment) if u.fragment else '')
   elif dest.parent==S and dest.name[:2].isdigit():
    num=dest.name.split('-')[0];n=int(num[:2]);folder=112 if n<=3 else 113 if n<=5 else 114 if n<=7 else 115
    tag['href']=f'../apoio-revisao-textual-{folder}/prova-textual.html#c'+num+('--'+unquote(u.fragment) if u.fragment else '')
   elif str(dest) in OLD:
    o=OLD[str(dest)];anchor=o['ancoras'].get(u.fragment,u.fragment) if u.fragment else o['id'];tag['href']=os.path.relpath(R/'07 - Edicao de Leitura'/o['pagina'],A)+'#'+anchor
   else:tag['href']=os.path.relpath(dest,A)+('#'+u.fragment if u.fragment else '')
  articles.append(f'<article class="folha" id="{key}"><header><p class="numero">ESTUDO DE CASO</p><h1>{title}</h1></header><div class="colunas">{body}</div></article>')
  meta.append({'id':key,'fonte_id':f['id'],'fonte':f['fonte_revisada'],'fonte_original':f['fonte_original'],'titulo':title,'sha256':sha(p),'sha256_original':sha(R/f['fonte_original'])})
 nav=''.join(f'<a href="#{f["id"]}">{f["titulo"]}</a>' for f in meta)
 html='<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Movimento, socorro e continuidade | Revisão textual</title><style>'+css+'</style></head><body><nav>'+nav+'<a href="casos-completos.html">Casos por assunto</a><a href="guia-de-consulta.html">Folhas e capítulos</a></nav><p class="aviso-edicao">Prova parcial: lote B1-02. As fontes antigas e a edição integrada anterior continuam preservadas.</p><main>'+''.join(articles)+'</main><p class="rodape-tela"><a href="../118-revisao-de-movimento-socorro-e-continuidade.md">Registro da revisão</a></p></body></html>'
 (A/'prova-textual.html').write_text(html);pdf=A/'output/pdf/Ciclo-Maldito-Movimento-Socorro-e-Continuidade-Revisao-Textual.pdf';pdf.parent.mkdir(parents=True,exist_ok=True)
 HTML(string=html,base_url=str(A),url_fetcher=offline).write_pdf(str(pdf),pdf_identifier=b'revisao-textual-118')
 pages=subprocess.check_output(['pdftotext',str(pdf),'-'],text=True).split('\f')
 if not pages[-1].strip():pages.pop()
 (A/'prova-textual.txt').write_text(''.join(f'\n=== PÁGINA {i} ===\n{t}' for i,t in enumerate(pages,1)))
 data={'registro':118,'fontes':meta,'html':str((A/'prova-textual.html').relative_to(R)),'html_sha256':sha(A/'prova-textual.html'),'pdf':str(pdf.relative_to(R)),'pdf_sha256':sha(pdf),'paginas':[{'pagina':i,'palavras':len(t.split())} for i,t in enumerate(pages,1)],'limite':'Cinco casos revistos; demais lotes, consultas complementares, conferência global e integração continuam pendentes.'}
 (A/'amostra.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n');print(json.dumps({'paginas':len(pages),'palavras':[len(t.split()) for t in pages]},ensure_ascii=False))
if __name__=='__main__':main()

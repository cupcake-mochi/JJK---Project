"""Prova dos três apoios: quadros extensos largos e fichas curtas nas colunas."""
from pathlib import Path
from bs4 import BeautifulSoup
from weasyprint import HTML,default_url_fetcher
from urllib.parse import urlsplit
import markdown,re,json,hashlib

A=Path(__file__).resolve().parent;R=A.parents[1];T=R/'06 - Redacao do Guia/edicao-integrada-136'
def offline(url,*args,**kwargs):
 assert urlsplit(url).scheme in ['file','data'],url
 return default_url_fetcher(url,*args,**kwargs)

def main():
 old=BeautifulSoup((R/'04 - Planejamento/apoio-revisao-textual-121/prova-textual.html').read_text(),'html.parser')
 css=old.style.get_text().replace('TERRENO, SAÍDA E SINEIRO','APOIOS REUNIDOS')
 css+='\n.fonte-inicio{break-before:auto}#apoio-3{break-before:auto}.colunas{column-fill:balance;column-gap:9mm;hyphens:auto;overflow-wrap:break-word}.inteira{margin:6pt 0}.inteira h2{font-size:17pt;margin:5pt 0 7pt}.inteira table{margin-top:3pt}.quadro-inicio{break-inside:avoid}.colunas h2{break-after:avoid}.colunas h3{break-after:avoid}.formula{white-space:nowrap}.colunas p{orphans:3;widows:3}.colunas p.curto{break-inside:avoid!important}#apoio-3 h1{font-size:26pt;margin-bottom:8pt}#apoio-3 .colunas p{margin-bottom:4pt}#apoio-3 table{font-size:8.7pt;line-height:11pt}#apoio-3 td,#apoio-3 th{padding:4pt}#apoio-3 td:first-child{width:46%}.folha-registro table td,.folha-registro table th{padding:3pt 4pt}.registro-vazio td{height:23pt}'
 sources=['casos/27-convivencia-do-receptaculo.md','casos/14-tres-maldicoes-para-a-missao.md','consultas/92-reserva-condensada-proposta-e-comparacao.md']
 sections=[]
 for n,rel in enumerate(sources):
  soup=BeautifulSoup(markdown.markdown((T/rel).read_text(),extensions=['tables','toc']),'html.parser')
  # O destino do livro continua clicável; a prova parcial não inventa paginação do conjunto.
  for a in soup.find_all('a',href=True):
   u=urlsplit(a['href'])
   if not u.scheme and u.path:a['href']=(T/rel).parent.joinpath(u.path).resolve().as_uri()+('#'+u.fragment if u.fragment else '')
  for p in soup.find_all('p'):
   if len(p.get_text())<=240 or p.get_text().startswith(('Coexistência comporta discordância.','Pancada','Impacto concentrado','Estalo de farpas','Fundamento registrado')):p['class']=p.get('class',[])+['curto']
  blocks=[];column=[]
  def flush():
   if column:blocks.append('<div class="colunas">'+''.join(column)+'</div>');column.clear()
  for node in list(soup.children):
   if not getattr(node,'name',None):continue
   if node.name=='h1':
    flush();blocks.append(str(node));continue
   if node.name=='table':
    cols=len(node.find('tr').find_all(['th','td']))
    wide=not rel.startswith('consultas/')
    if wide:
     intro=[]
     if column and re.match(r'^<h[23]',column[-1]):intro.insert(0,column.pop())
     elif len(column)>=2 and re.match(r'^<p',column[-1]) and re.match(r'^<h[23]',column[-2]):intro=[column.pop(-2),column.pop()]
     extra=' folha-registro' if rel.startswith('consultas/') else ''
     if '____' in node.get_text():extra+=' registro-vazio'
     flush();blocks.append('<div class="inteira'+extra+'"><div class="quadro-inicio">'+''.join(intro)+str(node)+'</div></div>');continue
   column.append(str(node))
  flush();sections.append('<section class="fonte-inicio" id="apoio-'+str(n+1)+'">'+''.join(blocks)+'</section>')
 html='<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>Apoios reunidos | Ciclo Maldito</title><style>'+css+'</style></head><body><main>'+''.join(sections)+'</main></body></html>'
 (A/'prova-dos-apoios.html').write_text(html)
 pdf=A/'output/pdf/Ciclo-Maldito-Apoios-da-Integracao.pdf';pdf.parent.mkdir(parents=True,exist_ok=True)
 HTML(string=html,base_url=str(A),url_fetcher=offline).write_pdf(str(pdf),pdf_identifier=b'integracao-136-apoios')
 (A/'prova-dos-apoios.json').write_text(json.dumps({'registro':136,'pdf':pdf.relative_to(R).as_posix(),'pdf_sha256':hashlib.sha256(pdf.read_bytes()).hexdigest(),'fontes':[str((T/s).relative_to(R)) for s in sources],'limite':'Três apoios recuperados. Não é o PDF integrado completo nem comprovação de equilíbrio.'},ensure_ascii=False,indent=2)+'\n')
 print(pdf)

if __name__=='__main__':main()

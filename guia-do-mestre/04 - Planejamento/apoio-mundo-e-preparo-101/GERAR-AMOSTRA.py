"""Amostra dos capítulos 2 e 3; preserva a edição integrada e a amostra 100."""
from pathlib import Path
from bs4 import BeautifulSoup
from weasyprint import HTML
import markdown, json, hashlib, os, re
APOIO = Path(__file__).resolve().parent
RAIZ = APOIO.parents[1]
FONTES = [RAIZ/'06 - Redacao do Guia/revisao-98'/n for n in ['02-o-mundo-dos-feiticeiros.md','03-preparar-aventuras.md']]
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
    base = RAIZ/'04 - Planejamento/apoio-primeira-missao-100/capitulo-1.html'
    estilo = BeautifulSoup(base.read_text(),'html.parser').style.string
    estilo = estilo.replace("content:'SUA PRIMEIRA MISSÃO'", "content:'MUNDO E PREPARO'")
    estilo += """
    .folha>header>h1{margin-top:0}.numero{font:700 18px Barlow,sans-serif;letter-spacing:.08em;color:#6f5867;margin:0 0 8px}
    .colunas h2{margin-top:1.1em}ol{padding-left:1.4em}ol li{padding-left:.3em}.consulta{font-size:.9em;color:#6f5867}
    @media print{#capitulo-3{break-after:auto}.ficha-cotidiano{break-inside:avoid;margin-top:9pt;padding-top:9pt;border-top:.5pt solid #ded4d9}.numero{font-size:10pt;margin-bottom:7pt}.folha>header>h1{margin-bottom:12pt}.folha .colunas h2{font-size:17pt;margin:11pt 0 7pt}.colunas h3{font-size:12.5pt}.folha>header{break-after:avoid}.ficha-cotidiano .colunas{column-count:2}.ficha-cotidiano h2{font-size:25pt;margin-bottom:7pt}ol{margin:4pt 0 8pt;padding-left:14pt}a{text-decoration:none}p:has(>strong:first-child){break-inside:avoid}}
    """
    artigos=[]; links=[]
    for num,fonte in enumerate(FONTES,2):
        partes=fonte.read_text().split('<!-- folha: despedida -->')
        for j,raw in enumerate(partes):
            soup=BeautifulSoup(markdown.markdown(raw,extensions=['sane_lists','toc']),'html.parser')
            cab=soup.find(['h1','h2']); titulo=cab.get_text();cab.extract()
            for a in soup.find_all('a',href=True):
                href=a['href']
                if href=='03-preparar-aventuras.md': a['href']='#capitulo-3'
                elif href=='01-sua-primeira-missao.md': a['href']='../apoio-primeira-missao-100/capitulo-1.html'
                elif not re.match(r'^(https?:|#)',href):
                    path,sep,frag=href.partition('#'); destino=(fonte.parent/path).resolve()
                    assert destino.exists(),destino
                    a['href']=os.path.relpath(destino,APOIO)+(sep+frag if sep else '')
            chave=f'capitulo-{num}' if j==0 else 'folha-despedida'
            clas='folha' if j==0 else 'folha ficha-cotidiano'
            if j==0:
                header=f'<header><p class="numero">CAPÍTULO {num}</p><h1>{titulo}</h1></header>'
            else: header=f'<header><h2>{titulo}</h2></header>'
            artigos.append(f'<article class="{clas}" id="{chave}">{header}<div class="colunas">{soup}</div></article>')
            links.append(f'<a href="#{chave}">{titulo}</a>')
    doc=f'<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Mundo e preparo | Ciclo Maldito</title><style>{estilo}</style></head><body><nav aria-label="Conteúdo">'+''.join(links)+'</nav><p class="aviso-edicao">Amostra dos capítulos 2 e 3 da nova estrutura. <a href="../apoio-primeira-missao-100/capitulo-1.html">Ler a primeira missão</a>. A edição completa anterior continua preservada.</p><main>'+''.join(artigos)+'</main><p class="rodape-tela"><a href="../101-mundo-e-preparacao-de-aventuras.md">Registro de revisão</a></p></body></html>'
    saida=APOIO/'output/pdf/Ciclo-Maldito-Mundo-e-Preparo-Amostra.pdf'
    saida.parent.mkdir(parents=True,exist_ok=True)
    (APOIO/'capitulos-2-e-3.html').write_text(doc)
    HTML(string=doc,base_url=str(APOIO)).write_pdf(str(saida),pdf_identifier=b'mundo-e-preparo-101')
    dados={'registro':101,'fontes':[{'caminho':str(p.relative_to(RAIZ)),'sha256':sha(p),'palavras':len(p.read_text().split())} for p in FONTES],'estilo_base':str(base.relative_to(RAIZ)),'estilo_base_sha256':sha(base),'pdf':str(saida.relative_to(RAIZ)),'pdf_sha256':sha(saida),'estado':'amostra isolada; etapa 3 em andamento; não integrada às 357 páginas anteriores'}
    (APOIO/'amostra.json').write_text(json.dumps(dados,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(dados,ensure_ascii=False,indent=2))
if __name__=='__main__': main()

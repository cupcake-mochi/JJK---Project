"""Gera uma amostra isolada da nova entrada; não recompõe o livro de 357 páginas."""
from pathlib import Path
import hashlib
import html
import json
import re
import markdown
from bs4 import BeautifulSoup
from weasyprint import HTML

APOIO = Path(__file__).resolve().parent
RAIZ = APOIO.parents[1]
FONTE = RAIZ / '06 - Redacao do Guia/revisao-98/01-sua-primeira-missao.md'
BASE = RAIZ / '04 - Planejamento/apoio-carregador/fontes/LIVRO-COMPLETO-R53.md'

MAPA = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 800" role="img" aria-labelledby="titulo descricao">
<title id="titulo">Planta do anexo</title><desc id="descricao">O pátio de seis por seis metros leva à entrada principal do corredor. O corredor tem nove por três metros e uma entrada de serviço na ponta oposta. Uma única porta no meio de sua parede superior abre para o depósito de seis por seis metros. O Amontoado está a quatro metros e meio dessa porta.</desc>
<defs><marker id="seta" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto-start-reverse"><path d="M0,0 L8,4 L0,8" fill="none" stroke="#9e2358" stroke-width="1.2"/></marker></defs>
<style>text{font-family:Arial,sans-serif;fill:#251727;font-size:25px}.nome{font-size:29px;font-weight:bold}.dim{font-size:24px;fill:#6f5867}.parede{stroke:#251727;stroke-width:5;fill:none}.cota{stroke:#9e2358;stroke-width:2;fill:none}.porta{stroke:#9e2358;stroke-width:3;fill:none;stroke-dasharray:8 6}</style>
<rect width="1200" height="800" fill="white"/>
<rect x="40" y="340" width="360" height="360" fill="#f8f1f4" stroke="#bda5b2" stroke-width="2" stroke-dasharray="10 7"/>
<rect x="400" y="430" width="540" height="180" fill="#f8f1f4"/>
<rect x="490" y="70" width="360" height="360" fill="#fdfbfc"/>
<path class="parede" d="M490 430 V70 H850 V430 H715 M625 430 H400 V465 M400 555 V610 H940 V555 M940 465 V430 H850"/>
<path class="porta" d="M625 430 H715 M400 465 V555 M940 465 V555"/>
<g fill="#e8d7e0" stroke="#b99baa" stroke-width="2"><rect x="505" y="250" width="45" height="50"/><rect x="505" y="325" width="45" height="60"/><rect x="790" y="250" width="45" height="50"/><rect x="790" y="325" width="45" height="60"/><rect x="590" y="80" width="160" height="40"/></g>
<circle cx="670" cy="160" r="25" fill="#9e2358"/><text x="670" y="170" text-anchor="middle" fill="white" style="fill:white;font-weight:bold">A</text>
<text x="670" y="213" text-anchor="middle" class="nome">DEPÓSITO</text><text x="670" y="245" text-anchor="middle">6 m × 6 m</text>
<text x="220" y="468" text-anchor="middle" class="nome">PÁTIO</text><text x="220" y="506" text-anchor="middle">6 m × 6 m</text>
<text x="670" y="513" text-anchor="middle" class="nome">CORREDOR</text><text x="670" y="550" text-anchor="middle">9 m × 3 m</text>
<text x="386" y="392" text-anchor="middle"><tspan x="386">Entrada</tspan><tspan x="386" dy="28">principal</tspan></text>
<path class="cota" d="M950 510 H990" marker-end="url(#seta)"/><text x="1005" y="495">Entrada<tspan x="1005" dy="30">de serviço</tspan></text>
<path class="cota" d="M220 710 V740" marker-end="url(#seta)"/><text x="220" y="779" text-anchor="middle">Recepção (fora da planta)</text>
<path class="cota" d="M400 640 H670 M400 630 V650 M670 630 V650 M670 640 H940 M940 630 V650"/>
<text x="535" y="675" class="dim" text-anchor="middle">4,5 m</text><text x="805" y="675" class="dim" text-anchor="middle">4,5 m</text>
<path class="cota" d="M570 160 V430 M562 160 H578 M562 430 H578"/><text x="585" y="345" class="dim">4,5 m</text>
<text x="40" y="35" class="nome">UMA SALA, DOIS ACESSOS AO CORREDOR</text>
<text x="885" y="102" class="dim">Pilha ao fundo:<tspan x="885" dy="29">1,5 m de altura.</tspan></text>
<text x="885" y="169" class="dim">A: posição inicial<tspan x="885" dy="29">do Amontoado.</tspan></text>
<text x="885" y="261" class="dim">Traços rosa:<tspan x="885" dy="29">portas de 1,5 m.</tspan></text>
<text x="885" y="345" class="dim">Caixas baixas<tspan x="885" dy="29">nas laterais.</tspan></text>
</svg>'''


def css_fontes():
    pasta = RAIZ / '08 - Diagramacao do Guia/fontes'
    return '\n'.join(f'@font-face{{font-family:"{nome}";src:url("{(pasta/arquivo).as_uri()}");font-weight:{peso};font-style:{estilo};}}'
                     for nome, arquivo, peso, estilo in [
                         ('Spectral', 'Spectral-Regular.ttf', '400', 'normal'),
                         ('Spectral', 'Spectral-SemiBold.ttf', '600', 'normal'),
                         ('Spectral', 'Spectral-Italic.ttf', '400', 'italic'),
                         ('Bree', 'BreeSerif.ttf', '400', 'normal'),
                         ('Barlow', 'BarlowCondensed-Bold.ttf', '700', 'normal')])


def preparar_html():
    raw = FONTE.read_text()
    partes = re.split(r'<!-- pagina: ([a-z-]+) -->\s*', raw)[1:]
    paginas = []
    for chave, texto in zip(partes[::2], partes[1::2]):
        soup = BeautifulSoup(markdown.markdown(texto, extensions=['tables', 'sane_lists']), 'html.parser')
        for img in soup.find_all('img'):
            img['src'] = 'planta-do-anexo.svg'
        cabecalho = soup.find(['h1', 'h2', 'h3'])
        assert cabecalho is not None, chave
        titulo = str(cabecalho.extract())
        # As duas tabelas de números da criatura ficam juntas acima das colunas.
        topo = ''
        if chave == 'ficha':
            elementos = list(soup.contents)
            for item in elementos:
                if getattr(item, 'name', None) in ['p', 'table']:
                    topo += str(item.extract())
                    if getattr(item, 'name', None) == 'table' and 'Força' in item.get_text():
                        break
        conteudo = str(soup)
        for p in soup.find_all('p'):
            texto_p = p.get_text()
            if texto_p.startswith('Decisão do mestre.'):
                p['class'] = 'comentario'
            elif texto_p.startswith(('Jogador:', 'Jogadora:', 'Mestre:', 'Frente:')):
                p['class'] = 'fala'
        for h in list(soup.find_all(['h2','h3'])):
            primeiro=h.find_next_sibling()
            itens=[h]
            if primeiro and primeiro.name=='p':
                itens.append(primeiro)
                seguinte=primeiro.find_next_sibling()
            else:
                seguinte=primeiro
            if seguinte and seguinte.name=='table':
                itens.append(seguinte)
                grupo=soup.new_tag('div',attrs={'class':'grupo-tabela'})
                h.insert_before(grupo)
                for item in itens:grupo.append(item.extract())
        conteudo = str(soup)
        tipo = 'inteira' if chave in ['mapa', 'resumo'] else 'colunas'
        paginas.append((chave, titulo, f'{topo}<div class="{tipo}">{conteudo}</div>'))
    artigos = []
    sumario = []
    for chave, titulo, corpo in paginas:
        texto_titulo = BeautifulSoup(titulo, 'html.parser').get_text()
        sumario.append(f'<a href="#{chave}">{html.escape(texto_titulo)}</a>')
        artigos.append(f'<article class="folha" id="{chave}">{titulo}{corpo}</article>')
    # A condução e seus desfechos seguem o fluxo entre páginas. Isso aproveita o
    # espaço sem forçar uma página inteira para cada tópico da demonstração.
    inicio = next(i for i,p in enumerate(paginas) if p[0]=='investigacao')
    fim = next(i for i,p in enumerate(paginas) if p[0]=='fechamento')
    sequencia = []
    for i in range(inicio,fim+1):
        chave,titulo,corpo=paginas[i]
        bloco=BeautifulSoup(corpo,'html.parser')
        col=bloco.find('div',class_='colunas')
        miolo=''.join(str(c) for c in col.contents)
        sequencia.append((chave,titulo,miolo))
    cap = sequencia[0][1]
    miolo = sequencia[0][2] + ''.join(f'<section id="{k}">{t}{b}</section>' for k,t,b in sequencia[1:])
    artigos[inicio:fim+1] = [f'<article class="folha sessao" id="investigacao">{cap}<div class="colunas">{miolo}</div></article>']
    estilo = css_fontes() + '''
    :root{--ink:#251727;--accent:#9e2358;--pale:#f8f1f4;--rule:#ded4d9}
    *{box-sizing:border-box}body{margin:0;color:var(--ink);background:#eee9ed;font:18px/1.6 Spectral,serif}
    h1,h2,h3{break-after:avoid;line-height:1.15}h1{font:700 44px/1.1 Barlow,sans-serif;color:var(--accent)}
    h2{font:700 30px/1.15 Barlow,sans-serif;color:var(--accent)}h3{font:22px/1.2 Bree,serif}
    p{margin:.65em 0 .9em;orphans:3;widows:3}strong{font-weight:600}a{color:var(--accent)}
    nav{background:#251727;color:white;padding:18px 24px;font:15px/1.5 sans-serif}nav a{color:white;display:inline-block;margin:4px 14px 4px 0}
    .aviso-edicao{margin:0;padding:12px 24px;background:#f8f1f4;font:14px/1.5 sans-serif}
    main{max-width:1000px;margin:28px auto}.folha{background:white;padding:42px 48px;margin:24px 0;box-shadow:0 2px 10px #25172718;scroll-margin-top:15px}
    .folha>h1,.folha>h2,.folha>h3{margin-top:0}blockquote{background:var(--pale);border-left:3px solid var(--accent);margin:16px 0;padding:8px 16px;break-inside:avoid}
    .comentario{border-left:2px solid var(--accent);padding-left:12px;color:#59424f;break-inside:avoid}.fala{margin-bottom:.5em}p:has(>strong:first-child),.grupo-tabela{break-inside:avoid}
    table{width:100%;border-collapse:collapse;font-size:15px;line-height:1.4;margin:16px 0 20px;break-inside:avoid}th,td{padding:7px 9px;text-align:left;vertical-align:top;border-bottom:1px solid var(--rule)}th{background:var(--pale);font-weight:600}tr:nth-child(even) td{background:#fcf9fb}tr{break-inside:avoid}thead{display:table-header-group}img{max-width:100%;height:auto}li{margin:.35em 0}.rodape-tela{padding:12px 24px;font:14px/1.5 sans-serif}
    @page{size:A4;margin:19mm;@top-left{content:'CICLO MALDITO / GUIA DO MESTRE';font:700 8pt Barlow;color:#9e2358}@top-right{content:'SUA PRIMEIRA MISSÃO';font:700 8pt Barlow;color:#6f5867}@bottom-left{content:'PRÉ-1.0 · AMOSTRA DE LEITURA';font:700 8pt Barlow;color:#6f5867}@bottom-right{content:counter(page);font:700 9pt Barlow;color:#9e2358}}
    @media print{body{background:white;font-size:10.25pt;line-height:13.2pt}nav,.aviso-edicao,.rodape-tela{display:none}main{margin:0;max-width:none}.folha{padding:0;margin:0;box-shadow:none;break-after:page}.folha:last-child{break-after:auto}.colunas{column-count:2;column-gap:7mm;column-fill:balance}.inteira{column-count:1}h1{font-size:29pt;margin:0 0 10pt}h2{font-size:20pt;margin:0 0 10pt}h3{font-size:13pt;margin:9pt 0 6pt}.colunas h2{font-size:17pt;margin-top:10pt}p{margin:0 0 6pt}table{font-size:8.7pt;line-height:11pt;margin:5pt 0 9pt}th,td{padding:4pt 5pt}.comentario{padding-left:7pt;border-left-width:1pt}blockquote{margin:6pt 0 8pt;padding:6pt 9pt;border-left-width:2pt}li{margin:0 0 4pt}ul{padding-left:13pt;margin:4pt 0 8pt}img{display:block;width:100%;height:auto}.inteira table{font-size:9.1pt;line-height:11.5pt}#mapa img{max-height:111mm;object-fit:contain}#ficha>.colunas{margin-top:5pt}}
    @media(max-width:700px){main{margin:0}.folha{padding:26px 20px;margin:8px 0}h1{font-size:38px}table{font-size:13px}.folha table{display:table}}
    '''
    doc = f'''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Sua primeira missão | Ciclo Maldito</title><style>{estilo}</style></head><body>
    <nav aria-label="Conteúdo da amostra">{''.join(sumario)}</nav>
    <p class="aviso-edicao">Amostra da nova abertura do Guia. Capítulo em revisão; exemplos de inimigo experimentais. <a href="consulta-de-regras.html">Consultar as regras usadas</a>.</p>
    <main>{''.join(artigos)}</main><p class="rodape-tela"><a href="consulta-de-regras.html">Livro de Regras 1.0: trechos usados nesta missão</a>. <a href="../100-primeira-missao-reunida-e-comentada.md">Registro de preparação e revisão</a>.</p></body></html>'''
    (APOIO / 'planta-do-anexo.svg').write_text(MAPA)
    (APOIO / 'capitulo-1.html').write_text(doc)
    return doc


def regras_de_apoio():
    texto = BASE.read_text()
    # Seções por título, incluindo suas subseções até o próximo título do mesmo
    # nível ou superior. Não usar um resumo do assistente como texto da regra.
    titulos = ['Primeira sessão', 'Mundo jujutsu', 'Turnos',
               'Ataques', 'Estudar', 'Vida a zero', 'Janela de socorro',
               'Aguentar', 'Insistir', 'Socorro', 'Sequelas e Cicatrizes',
               'Derrota e morte', 'Dano na alma', 'Estágios de Integridade']
    linhas = texto.splitlines();secoes=[]
    for titulo in titulos:
        encontrados = [(i, re.match(r'^(#{2,5}) ', l).group(1)) for i,l in enumerate(linhas)
                       if re.match(r'^#{2,5} '+re.escape(titulo)+r'\s*$',l)]
        assert len(encontrados)==1,(titulo,encontrados)
        inicio,marcador=encontrados[0];nivel=len(marcador);fim=len(linhas)
        for j in range(inicio+1,len(linhas)):
            m=re.match(r'^(#{1,5}) ',linhas[j])
            if m and (len(m.group(1))<=nivel or (titulo=='Vida a zero' and len(m.group(1))==nivel+1)):
                fim=j;break
        bloco='\n'.join(linhas[inicio:fim])
        slug=re.sub(r'[^a-z0-9]+','-',titulo.lower()).strip('-')
        secoes.append((titulo,slug,bloco))
    lista=''.join(f'<li><a href="#{slug}">{html.escape(t)}</a></li>' for t,slug,_ in secoes)
    corpo=''.join(f'<section id="{slug}">{markdown.markdown(bloco,extensions=["tables","sane_lists"])}</section>' for _,slug,bloco in secoes)
    conversoes=(RAIZ/'04 - Planejamento/14-base-pequena-de-inimigos-r53.md').read_text().split('## Conversões conhecidas para maldições domadas',1)[1].split('## Uso e revisão',1)[0]
    corpo += '<section id="conversoes-domadas"><h2>Conversões para Doma</h2>'+markdown.markdown(conversoes,extensions=['tables','sane_lists'])+'</section>'
    lista += '<li><a href="#conversoes-domadas">Fichas convertidas para uma tentativa de Doma</a></li>'
    soup=BeautifulSoup(corpo,'html.parser')
    ids={x.get('id') for x in soup.find_all(id=True)}
    for a in soup.find_all('a'):
        href=a.get('href','')
        if href.startswith('#') and href[1:] not in ids:
            a['href']='../apoio-carregador/fontes/LIVRO-COMPLETO-R53.md'+href
    doc=f'''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Regras para consulta | Ciclo Maldito</title><style>{css_fontes()}body{{max-width:900px;margin:30px auto;padding:20px;font:18px/1.6 Spectral,serif;color:#251727}}h1,h2,h3,h4{{font-family:Bree,serif}}a{{color:#9e2358}}table{{width:100%;border-collapse:collapse;font-size:15px}}td,th{{padding:8px;border-bottom:1px solid #ded4d9;text-align:left}}blockquote{{border-left:3px solid #9e2358;padding-left:20px}}section{{border-top:1px solid #ded4d9;padding:20px 0;margin-top:20px}}</style></head><body><p><a href="capitulo-1.html">Voltar à primeira missão</a></p><h1>Livro de Regras 1.0</h1><p>Trechos usados para consultar esta missão, extraídos da referência do sistema sem reescrita. As conversões experimentais para Doma aparecem ao final, identificadas separadamente.</p><ul>{lista}</ul>{str(soup)}</body></html>'''
    (APOIO/'consulta-de-regras.html').write_text(doc)
    return [{'titulo':t,'ancora':slug} for t,slug,_ in secoes]


def main():
    APOIO.mkdir(parents=True,exist_ok=True)
    doc=preparar_html();regras=regras_de_apoio()
    saida=APOIO/'output/pdf';saida.mkdir(parents=True,exist_ok=True)
    pdf=saida/'Ciclo-Maldito-Sua-Primeira-Missao-Amostra.pdf'
    HTML(string=doc,base_url=str(APOIO)).write_pdf(str(pdf),pdf_identifier=b'primeira-missao-100')
    dados={'fonte':str(FONTE.relative_to(RAIZ)),'fonte_sha256':hashlib.sha256(FONTE.read_bytes()).hexdigest(),
           'base':str(BASE.relative_to(RAIZ)),'base_sha256':hashlib.sha256(BASE.read_bytes()).hexdigest(),
           'consultas_de_regras':regras,'pdf':str(pdf.relative_to(RAIZ)),
           'pdf_sha256':hashlib.sha256(pdf.read_bytes()).hexdigest(),
           'limite':'Amostra isolada; não altera o PDF integrado de 357 páginas.'}
    (APOIO/'amostra.json').write_text(json.dumps(dados,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(dados,ensure_ascii=False,indent=2))


if __name__=='__main__':
    main()

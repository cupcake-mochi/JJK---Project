"""Prova dos quatro casos B5-03, com as fontes antigas preservadas.

Adaptado do gerador do registro 121: mesmo padrão (A4, duas colunas, 19 mm, 7 mm,
Spectral 10,25/13,2, tabelas 9,2/11,5). Quadros largos ficam fora do bloco de colunas.
"""
from pathlib import Path
from bs4 import BeautifulSoup
from urllib.parse import urlsplit, unquote
from weasyprint import HTML, default_url_fetcher
import hashlib, json, markdown, os, subprocess

A = Path(__file__).resolve().parent
R = A.parents[1]
S = R / '06 - Redacao do Guia/revisao-98'
CFG = json.loads((A / 'arquivos-do-lote.json').read_text())
FILES = CFG['casos']
LOCAL = {str((R / f[k]).resolve()): f['id_prova'] for f in FILES for k in ['fonte_original', 'fonte_revisada']}
OLD = {str((R / f['fonte']).resolve()): f for f in json.loads((R / '07 - Edicao de Leitura/mapa-editorial.json').read_text())['fontes']}
FORMS = {str((R / f['fonte']).resolve()): f['id'] for f in json.loads((R / '04 - Planejamento/apoio-revisao-textual-116/amostra.json').read_text())['fontes']}
REVISED = {str((R / f[k]).resolve()): f['consulta_atual']
           for rows in json.loads((R / '04 - Planejamento/apoio-revisao-textual-129/destinos-e-fontes.json').read_text())['casos'].values()
           for f in rows for k in ['fonte', 'fonte_revisada'] if k in f and f.get('fonte_revisada')}
TITULO_PAGINA = 'DOMA, CONSTRUÇÃO E TRANSPORTE'
PDF_NOME = 'Ciclo-Maldito-Doma-Construcao-e-Transporte-Revisao-Textual.pdf'
WIDE_FIRST = ['Campo', 'Recurso ou estado', 'Escolha de condução', 'Compra', 'Uso', 'Nível da entidade', 'Nível do Vigia', 'O que a entidade leva', 'Origem', 'Momento', 'Campo de entrega']
CONTA = ('Exemplo:', 'Uso válido.', 'Uso impedido.', 'Avaliação:', 'Escolha visível:')
MAPAS = {}


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def offline(url, *args, **kwargs):
    if urlsplit(url).scheme not in ['file', 'data']:
        raise ValueError(url)
    return default_url_fetcher(url, *args, **kwargs)


def figure(body, key):
    box = body.new_tag('div', attrs={'class': 'bloco-mapa'})
    fig = body.new_tag('figure')
    fig.append(body.new_tag('img', src='imagens/' + key + '.svg', alt=MAPAS[key]))
    box.append(fig)
    return box


def main():
    css = BeautifulSoup((R / '04 - Planejamento/apoio-revisao-textual-115/prova-textual.html').read_text(), 'html.parser').style.get_text().replace('CAPÍTULOS 8 A 10', TITULO_PAGINA)
    css += ('@media print{.larga{column-span:none;break-inside:avoid;margin:8pt 0}.larga.fluida,.larga.fluida table{break-inside:auto}'
            '.larga th{white-space:normal}.larga>p{break-after:avoid}.colunas p.conta{break-inside:avoid}.numero-curto{white-space:nowrap}'
            '.bloco-mapa{break-inside:avoid;margin:8pt 0}.bloco-mapa figure{margin:0}.bloco-mapa img{display:block;width:100%;height:auto}'
            '.folha>header{break-inside:avoid;break-after:avoid}.folha>header .numero{break-after:avoid}.mapa-legenda{margin:5pt 0 8pt}#amontoado,#escriba,#mula{break-after:auto}#escriba,#mula,#vigia{padding-top:14pt;break-before:auto}.formula{white-space:nowrap}}')
    articles = []
    meta = []
    for f in FILES:
        key = f['id_prova']
        p = R / f['fonte_revisada']
        body = BeautifulSoup(markdown.markdown(p.read_text(), extensions=['tables', 'sane_lists', 'toc', 'fenced_code']), 'html.parser')
        title = body.h1.get_text()
        body.h1.extract()
        for table in body.find_all('table'):
            heads = [x.get_text() for x in table.find_all('th')]
            for cell in table.find_all('td'):
                val = cell.get_text(' ', strip=True)
                if len(val) <= 18 and val and any(c.isdigit() for c in val) and all(c in '0123456789.,%/ +−–' for c in val):
                    cell['class'] = 'numero-curto'
            if len(heads) >= 3 or heads[0] in WIDE_FIRST:
                items = [table]
                prev = table.find_previous_sibling()
                if prev and prev.name in ['h2', 'h3']:
                    items.insert(0, prev)
                elif prev and prev.name == 'p' and len(prev.get_text().split()) < 95:
                    h = prev.find_previous_sibling()
                    if h and h.name in ['h2', 'h3']:
                        items = [h, prev, table]
                wrap = body.new_tag('div', attrs={'class': 'larga fluida' if len(table.find_all('tr')) >= 5 else 'larga'})
                items[0].insert_before(wrap)
                for node in items:
                    wrap.append(node.extract())
        for strong in body.find_all('strong'):
            if len(strong.get_text()) <= 35 and any(x in strong.get_text() for x in ['=', '×', '÷', '−', '+', '–']):
                strong['class'] = 'formula'
        for par in body.find_all('p'):
            if par.get_text().startswith(CONTA):
                par['class'] = 'conta'
        for node in list(body.find_all(string=True)):
            if 'kg ÷ 12' in node:
                node.replace_with(str(node).replace('kg ÷ 12', 'kg ÷ 12'))
        for tag in body.find_all(id=True):
            tag['id'] = key + '--' + tag['id']
        for tag in body.find_all('a', href=True):
            u = urlsplit(tag['href'])
            if u.scheme:
                continue
            if not u.path:
                tag['href'] = '#' + key + '--' + unquote(u.fragment)
                continue
            dest = (p.parent / unquote(u.path)).resolve()
            assert dest.is_file(), (p, tag['href'])
            if str(dest) in LOCAL:
                tag['href'] = '#' + LOCAL[str(dest)] + ('--' + unquote(u.fragment) if u.fragment else '')
            elif str(dest) in REVISED:
                tag['href'] = os.path.relpath(R / REVISED[str(dest)].split('#')[0], A) + '#' + REVISED[str(dest)].split('#')[1]
            elif str(dest) in FORMS:
                tag['href'] = '../apoio-revisao-textual-116/prova-textual.html#' + FORMS[str(dest)] + ('--' + unquote(u.fragment) if u.fragment else '')
            elif dest.parent == S and dest.name[:2].isdigit():
                num = dest.name.split('-')[0]
                n = int(num[:2])
                folder = 112 if n <= 3 else 113 if n <= 5 else 114 if n <= 7 else 115
                tag['href'] = f'../apoio-revisao-textual-{folder}/prova-textual.html#c' + num + ('--' + unquote(u.fragment) if u.fragment else '')
            elif str(dest) in OLD:
                o = OLD[str(dest)]
                anchor = o['ancoras'].get(u.fragment, u.fragment) if u.fragment else o['id']
                tag['href'] = os.path.relpath(R / '07 - Edicao de Leitura' / o['pagina'], A) + '#' + anchor
            else:
                tag['href'] = os.path.relpath(dest, A) + ('#' + u.fragment if u.fragment else '')
        parts = []
        current = []

        def flush():
            if current:
                parts.append('<div class="colunas">' + ''.join(current) + '</div>')
                current.clear()
        for node in body.contents:
            if getattr(node, 'attrs', {}).get('class') and any(c in node['class'] for c in ['larga', 'bloco-mapa']):
                flush()
                parts.append(str(node))
            else:
                current.append(str(node))
        flush()
        articles.append(f'<article class="folha" id="{key}"><header><p class="numero">CONSULTA DO MESTRE</p><h1>{title}</h1></header>{"".join(parts)}</article>')
        meta.append({'id': key, 'fonte_id': f['id'], 'fonte': f['fonte_revisada'], 'fonte_original': f['fonte_original'], 'titulo': title,
                     'sha256': sha(p), 'sha256_original': sha(R / f['fonte_original'])})
    nav = ''.join(f'<a href="#{f["id"]}">{f["titulo"]}</a>' for f in meta)
    html = ('<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
            '<title>Doma, construção e transporte | Revisão textual</title><style>' + css + '</style></head><body><nav>' + nav +
            '<a href="casos-completos.html">Casos por assunto</a><a href="guia-de-consulta.html">Folhas e capítulos</a></nav>'
            '<p class="aviso-edicao">Prova parcial: lote B5-03. Fontes antigas e edição integrada anterior preservadas.</p><main>' + ''.join(articles) +
            '</main><p class="rodape-tela"><a href="../130-revisao-de-doma-construcao-e-transporte.md">Registro da revisão</a></p></body></html>')
    (A / 'prova-textual.html').write_text(html)
    pdf = A / 'output/pdf' / PDF_NOME
    pdf.parent.mkdir(parents=True, exist_ok=True)
    HTML(string=html, base_url=str(A), url_fetcher=offline).write_pdf(str(pdf), pdf_identifier=b'revisao-textual-130')
    pages = subprocess.check_output(['pdftotext', str(pdf), '-'], text=True).split('\f')
    if not pages[-1].strip():
        pages.pop()
    (A / 'prova-textual.txt').write_text(''.join(f'\n=== PÁGINA {i} ===\n{t}' for i, t in enumerate(pages, 1)))
    data = {'registro': 130, 'fontes': meta, 'html': str((A / 'prova-textual.html').relative_to(R)), 'html_sha256': sha(A / 'prova-textual.html'),
            'pdf': str(pdf.relative_to(R)), 'pdf_sha256': sha(pdf), 'paginas': [{'pagina': i, 'palavras': len(t.split())} for i, t in enumerate(pages, 1)],
            'limite': 'Quatro casos revistos; demais lotes, consultas, conferência global e integração continuam pendentes.'}
    (A / 'amostra.json').write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({'paginas': len(pages), 'palavras': [len(t.split()) for t in pages]}, ensure_ascii=False))


if __name__ == '__main__':
    main()

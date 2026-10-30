"""Prova da conferência do conjunto (registro 135): cada parágrafo que mudou de forma visível, com o texto
removido riscado e o acrescentado sublinhado. Trocas só de destino de link não aparecem no impresso e ficam
de fora. Mesma página e fonte das provas anteriores (A4, duas colunas, Spectral)."""
from pathlib import Path
from urllib.parse import urlsplit
import difflib, html, re
from bs4 import BeautifulSoup
from weasyprint import HTML, default_url_fetcher

A = Path(__file__).resolve().parent; R = A.parents[1]; S = R / '06 - Redacao do Guia/revisao-98'; ANTES = A / 'antes'
TITULO = 'CONFERÊNCIA DO CONJUNTO'


def offline(url, *a, **k):
    if urlsplit(url).scheme not in ['file', 'data']:
        raise ValueError(url)
    return default_url_fetcher(url, *a, **k)


def visivel(p):
    p = re.sub(r'!\[[^\]]*\]\([^)]*\)', '', p)
    p = re.sub(r'\[([^\]]*)\]\(<?[^)]*\)', r'\1', p)
    p = re.sub(r'<[^>]+>', '', p)
    p = re.sub(r'^\s*(#{1,6}|>)\s?', '', p, flags=re.M)
    return re.sub(r'\*\*|(?<!\w)\*(?!\s)|`', '', p).strip()


def blocos(t):
    return [visivel(b) for b in re.split(r'\n\s*\n', t) if visivel(b)]


def marca(a, d):
    wa, wd = re.findall(r'\S+|\s+', a), re.findall(r'\S+|\s+', d)
    out = []
    for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, wa, wd, autojunk=False).get_opcodes():
        if op == 'equal':
            out.append(html.escape(''.join(wa[i1:i2])))
        else:
            if i2 > i1: out.append('<del>' + html.escape(''.join(wa[i1:i2])) + '</del>')
            if j2 > j1: out.append('<ins>' + html.escape(''.join(wd[j1:j2])) + '</ins>')
    return ''.join(out)


def par(a, d):
    la, ld = a.splitlines(), d.splitlines()
    if len(la) > 1 or len(ld) > 1:  # tabela ou lista: só as linhas que mudaram
        linhas = []
        for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, la, ld, autojunk=False).get_opcodes():
            if op == 'equal': continue
            for k in range(max(i2 - i1, j2 - j1)):
                x = la[i1 + k] if i1 + k < i2 else ''; y = ld[j1 + k] if j1 + k < j2 else ''
                linhas.append(marca(x.strip('| ').replace(' | ', ' · '), y.strip('| ').replace(' | ', ' · ')))
        return ''.join(f'<p class="linha-tab">{l}</p>' for l in linhas)
    return f'<p>{marca(a, d)}</p>'


def main():
    css = BeautifulSoup((R / '04 - Planejamento/apoio-revisao-textual-115/prova-textual.html').read_text(), 'html.parser').style.get_text().replace('CAPÍTULOS 8 A 10', TITULO)
    css += ('del{color:#8a2b2b;text-decoration:line-through}ins{color:#1f5f3a;text-decoration:underline;text-decoration-thickness:.6pt}'
            '.arquivo{font-size:8pt;color:#6b5f66;margin:-4pt 0 6pt}.linha-tab{font-size:9.2pt;line-height:11.5pt;margin:2pt 0 4pt}'
            'h2{break-after:avoid}.arquivo{break-after:avoid}'
            '@media print{section.entrada:last-child h2{margin-bottom:6pt}'
            'section.entrada:last-child .arquivo{margin-bottom:2pt}'
            'section.entrada:last-child p:not(.arquivo){margin-bottom:2pt}'
            'section.entrada:last-child .linha-tab{margin-top:0;margin-bottom:1pt}}')
    corpo, total, arqs = [], 0, 0
    for p in sorted(ANTES.rglob('*.md'), key=lambda x: (x.parent.name != 'antes', str(x))):
        f = p.relative_to(ANTES); depois = (S / f).read_text()
        a, d = blocos(p.read_text()), blocos(depois)
        if f.as_posix() == 'consultas/LEIA-ME.md':
            # Na prova comparativa, mostrar só a frase de estado alterada.
            # O contexto idêntico permanece integralmente na fonte do livro.
            prefixo = 'O índice de casos por assunto reúne explicação, folhas e exemplos. '
            sufixo = ' Não trate um exemplo experimental como regra geral.'
            a = [b.removeprefix(prefixo).removesuffix(sufixo) if b.startswith(prefixo) else b for b in a]
            d = [b.removeprefix(prefixo).removesuffix(sufixo) if b.startswith(prefixo) else b for b in d]
        partes = []
        for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, a, d, autojunk=False).get_opcodes():
            if op == 'equal': continue
            for k in range(max(i2 - i1, j2 - j1)):
                partes.append(par(a[i1 + k] if i1 + k < i2 else '', d[j1 + k] if j1 + k < j2 else ''))
        if not partes: continue
        arqs += 1; total += len(partes)
        titulo = re.search(r'^#\s+(.+)$', depois, re.M).group(1)
        corpo.append(f'<section class="entrada"><h2>{html.escape(visivel(titulo))}</h2><p class="arquivo">{html.escape(str(f))}</p>{"".join(partes)}</section>')
    intro = (f'<h1>Conferência do conjunto</h1><p>Registro 135, 30 de outubro de 2026. Esta prova mostra os {total} trechos que mudaram de forma visível em {arqs} arquivos: '
             'nomes do elenco fixo, avisos que deixaram de ser necessários, títulos de remissão trocados pelo da seção nova e citações do Livro de Regras 1.0 que substituíram links de trabalho. '
             '<del>Riscado</del> sai; <ins>sublinhado</ins> entra. Remissões que só mudaram de destino não aparecem no impresso e não estão aqui.</p>')
    doc = f'<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>Conferência do conjunto</title><style>{css}</style></head><body><main>{intro}{"".join(corpo)}</main></body></html>'
    (A / 'prova-textual.html').write_text(doc)
    pdf = A / 'output/pdf/Ciclo-Maldito-Conferencia-do-Conjunto.pdf'; pdf.parent.mkdir(parents=True, exist_ok=True)
    HTML(string=doc, base_url=str(A), url_fetcher=offline).write_pdf(str(pdf), pdf_identifier=b'conferencia-135')
    print(arqs, 'arquivos', total, 'trechos', pdf)


main()

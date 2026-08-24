#!/usr/bin/env python3
"""Mede o livro contra os quatro manuais do hobby, nas marcas que decidem corte.

    python3 medir-voz.py

Os PDFs ficam FORA do repositorio, em "PDFs - Sistemas Extras/PDF_Sistemas/".
Se eles nao estiverem la, o script diz e sai — ele nao mede meio corpus.

A linha de base esta em METODO-passada-de-texto.md, e e' de la que sai a leitura
de cada numero. Aqui so' se produz o numero.
"""
import os, re, sys, glob, subprocess, statistics, tempfile

RAIZ = os.path.dirname(os.path.abspath(__file__))
PDFS = os.path.join(RAIZ, '..', '..', '..', 'PDFs - Sistemas Extras', 'PDF_Sistemas')
MANUAL = os.path.join(RAIZ, 'manual')

CORPORA = [
    ('PHB 2024',    'Player_Hand_Book_DnD_2024.pdf'),
    ('Tasha',       'dampd-5e---caldeirao-de-tasha-para-tudo.pdf'),
    ('Guia Mestre', 'dd-5e-guia-do-mestre-biblioteca-elfica.pdf'),
    ('GURPS 4e',    'gurps---gurps-4ed.---edicao-de-luxo.pdf'),
]

# So' o VERBO 'é'. A primeira versao destas duas casava [ée] e pegava a
# conjuncao "e" — ela inflou a equacao de 19,9 para 25,4 e a antitese de 0,3
# para 3,1, e quase rendeu 84 cortes errados. v0.137.
MARCAS = [
    ('% de frases SEM numero  (prosa)', None, '{:.0f}%'),
    ('palavras por frase (mediana)',    None, '{:.0f}'),
    ('"voce" por mil frases',           re.compile(r'\bvoc[êe]\b', re.I), '{:.0f}'),
    ('antitese  nao e X, e Y',  re.compile(r'(?<![\wà-ú])n[ãa]o\s+é\s+[^.;:]{3,60}[,;:]\s*é\s', re.I), '{:.1f}'),
    ('antitese  , e nao',       re.compile(r',\s*e\s+n[ãa]o\s', re.I), '{:.1f}'),
    ('antitese  em vez de',     re.compile(r'\bem\s+vez\s+de\b', re.I), '{:.1f}'),
    ('analogia  como se/quem',  re.compile(r'\bcomo\s+(se|quem)\b', re.I), '{:.1f}'),
    ('equacao   e o/a X que',   re.compile(r'(?<![\wà-ú])é\s+(o|a|um|uma)\s+\w+\s+que\b', re.I), '{:.1f}'),
]


def frases(t):
    return [f for f in re.split(r'(?<=[.!?])\s+(?=[A-ZÁÉÍÓÚÂÊÔÃÕÇ])', t) if len(f.split()) >= 4]


def do_pdf(caminho):
    with tempfile.NamedTemporaryFile(suffix='.txt', delete=False) as fh:
        tmp = fh.name
    try:
        subprocess.run(['pdftotext', caminho, tmp], check=True,
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        t = open(tmp, encoding='utf-8', errors='replace').read()
    finally:
        os.unlink(tmp)
    return re.sub(r'\s+', ' ', re.sub(r'-\n', '', t))


def do_livro():
    t = ' '.join(open(f, encoding='utf-8').read() for f in sorted(glob.glob(MANUAL + '/*.md')))
    t = re.sub(r'^\s*\|.*$', ' ', t, flags=re.M)   # fora tabelas
    t = re.sub(r'\{:[^}]*\}', ' ', t)
    t = re.sub(r'[`*_#>]', '', t)
    return re.sub(r'\s+', ' ', t)


def main():
    if not os.path.isdir(PDFS):
        sys.exit(f'  A pasta dos PDFs nao esta aqui:\n    {os.path.normpath(PDFS)}\n'
                 '  Ela fica FORA do repositorio, por ser material comercial de terceiro.\n'
                 '  Sem ela nao da para medir contra os quatro. Nada foi medido.')
    if not subprocess.run(['which', 'pdftotext'], capture_output=True).stdout:
        sys.exit('  Falta o pdftotext (pacote poppler-utils). Nada foi medido.')

    dados = []
    for nome, arq in CORPORA:
        p = os.path.join(PDFS, arq)
        if not os.path.exists(p):
            sys.exit(f'  Falta o corpus "{nome}" em {arq}. Nada foi medido — quatro ou nenhum.')
        fs = frases(do_pdf(p))
        # guarda de corpus vazio: a v0.137 teve um falso negativo por comparar
        # duas listas vazias e responder "nao sumiu nada".
        assert len(fs) > 1000, f'{nome} extraiu {len(fs)} frases — extracao falhou'
        dados.append((nome, fs))

    fs = frases(do_livro())
    assert len(fs) > 1000, f'o livro extraiu {len(fs)} frases — algo quebrou'
    dados.append(('NOSSO', fs))

    print(f"\n{'marca':34}" + ''.join(f'{n[:12]:>13}' for n, _ in dados))
    print('-' * (34 + 13 * len(dados)))
    for rot, rx, fmt in MARCAS:
        linha = f'{rot:34}'
        for _, f in dados:
            if rot.startswith('%'):
                v = 100 * sum(1 for x in f if not re.search(r'\d', x)) / len(f)
            elif rot.startswith('palavras'):
                v = statistics.median(len(x.split()) for x in f)
            else:
                v = 1000 * sum(1 for x in f if rx.search(x)) / len(f)
            linha += f'{fmt.format(v):>13}'
        print(linha)
    print('-' * (34 + 13 * len(dados)))
    print(f"{'frases medidas':34}" + ''.join(f'{len(f):>13,}' for _, f in dados))
    print('\n  A leitura de cada numero esta em METODO-passada-de-texto.md.')
    print('  Numero alto NAO e ordem de corte: tres das oito marcas ja estao')
    print('  na faixa dos quatro livros, e cortar nelas piora o texto.\n')


if __name__ == '__main__':
    main()

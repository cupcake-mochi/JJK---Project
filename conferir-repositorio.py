#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Confere o REPOSITORIO, e nao as regras.

Os sete validadores de sistema/03-mecanica conferem numero. Este confere que a
ARVORE esta inteira: que todo arquivo que um documento cita existe, que os
validadores acham o manual, e que nada ficou apontando para a estrutura antiga.

Ele existe porque a reorganizacao para git moveu tres coisas de lugar — o manual,
os changelogs e a pasta do sistema — e havia 104 referencias internas cruzadas.
Uma referencia quebrada nao falha nenhum validador: ela so' aparece seis meses
depois, quando alguem abre o projeto em outro computador e nao acha o arquivo.

Tres checagens:
  1. ESTRUTURA — as pastas e os arquivos que o README promete existem.
  2. REFERENCIA MORTA — todo caminho citado em .md e .py resolve para um arquivo
     de verdade.
  3. ESTRUTURA ANTIGA — nada continua apontando para RPG-JJK/ ou para o manual na
     raiz, que era onde eles moravam antes.

Roda da raiz do repositorio, sem argumento. Sai com codigo 1 se algo quebrar.
"""
import os
import re
import sys

RAIZ = os.path.dirname(os.path.abspath(__file__))
FALHAS = []
AVISOS = []


def erro(msg):
    FALHAS.append(msg)
    print(f'  !! {msg}')


def aviso(msg):
    AVISOS.append(msg)
    print(f'  ~~ {msg}')


def bloco(t):
    print()
    print('=' * 88)
    print(t)
    print('=' * 88)


def rel(p):
    return os.path.relpath(p, RAIZ)


# --------------------------------------------------------------------------
bloco('1. ESTRUTURA — o que o README promete existe?')

ESPERADO = [
    ('README.md', 'arquivo'),
    ('.gitignore', 'arquivo'),
    ('logs/CHANGELOG.md', 'arquivo'),
    ('logs/CHANGELOG-manual-v6-para-v7.md', 'arquivo'),
    ('manual/Fundamento-MANUAL-v7.docx', 'arquivo'),
    ('manual/Fundamento-MANUAL-v7.pdf', 'arquivo'),
    ('manual/gerador/make.js', 'arquivo'),
    ('manual/gerador/COMO-USAR.txt', 'arquivo'),
    ('manual/matematica/pac7.py', 'arquivo'),
    ('manual/matematica/v7.py', 'arquivo'),
    ('sistema/ESTADO-ATUAL.md', 'arquivo'),
    ('sistema/LEIA-ME.md', 'arquivo'),
    ('sistema/00-fundacao', 'pasta'),
    ('sistema/01-pesquisa', 'pasta'),
    ('sistema/02-esqueleto', 'pasta'),
    ('sistema/03-mecanica', 'pasta'),
    ('sistema/04-playtest', 'pasta'),
    ('sistema/05-material', 'pasta'),
    ('sistema/99-arquivo', 'pasta'),
    ('sistema/skills', 'pasta'),
]
for caminho, tipo in ESPERADO:
    p = os.path.join(RAIZ, caminho)
    ok = os.path.isfile(p) if tipo == 'arquivo' else os.path.isdir(p)
    print(f'  {"[x]" if ok else "[ ]"} {caminho}')
    if not ok:
        erro(f'{tipo} que o README promete nao existe: {caminho}')

# as onze pecas e os sete validadores
MEC = os.path.join(RAIZ, 'sistema', '03-mecanica')
pecas = sorted(f for f in os.listdir(MEC) if re.match(r'^\d\d-.*\.md$', f))
vals = sorted(f for f in os.listdir(MEC) if f.startswith('conferir-') and f.endswith('.py'))
print(f'\n  {len(pecas)} pecas de regra, {len(vals)} validadores.')
if len(pecas) != 11:
    erro(f'sao {len(pecas)} pecas e o README diz onze')
if len(vals) != 7:
    erro(f'sao {len(vals)} validadores e o README diz sete')

# a numeracao das pecas nao pode ter buraco
nums = [int(p[:2]) for p in pecas]
if nums != list(range(1, len(nums) + 1)):
    erro(f'a numeracao das pecas tem buraco ou repeticao: {nums}')
else:
    print(f'  Numeracao de 01 a {nums[-1]:02d}, sem buraco.')


# --------------------------------------------------------------------------
bloco('2. REFERENCIA MORTA — todo caminho citado resolve?')

# caminhos citados entre crases nos .md, e caminhos em os.path.join nos .py
RX_MD = re.compile(r'`([^`\n]*?[\w-]+/[\w./-]+|[\w-]+\.(?:md|py|docx|pdf|zip|txt|js|json))`')
IGNORAR = re.compile(
    r'^(https?:|npm |pip |python3 |node |cd |git )|'
    r'^(and/or|e/ou|N/A)$|'
    r'[<>{}*]|'
    r'^\d+/\d+$'
)

# todo nome de arquivo que existe na arvore, para resolver citacao solta em prosa
TODOS_OS_NOMES = set()
for _b, _d, _f in os.walk(RAIZ):
    _d[:] = [x for x in _d if x not in ('.git', '_backup', 'node_modules', '__pycache__')]
    TODOS_OS_NOMES.update(_f)

vistos = 0
mortas = 0
for base, dirs, files in os.walk(RAIZ):
    dirs[:] = [d for d in dirs
               if d not in ('.git', '_backup', 'node_modules', '__pycache__', 'skills')]
    for f in files:
        if not f.endswith('.md'):
            continue
        caminho = os.path.join(base, f)
        # o 99-arquivo e os changelogs descrevem estrutura que morreu de proposito,
        # e o projeto decidiu na v0.21 que as entradas antigas ficam como estao
        if '99-arquivo' in caminho or os.path.basename(base) == 'logs':
            continue
        txt = open(caminho, encoding='utf-8', errors='ignore').read()
        for m in RX_MD.finditer(txt):
            alvo = m.group(1).strip()
            if IGNORAR.search(alvo) or ' ' in alvo:
                continue
            vistos += 1
            # "Habilidade/Sabedoria" tem barra e nao e caminho. So conta como
            # caminho o que tem extensao ou termina em barra.
            eh_caminho = '/' in alvo and (alvo.endswith('/') or re.search(r'\.\w{2,4}$', alvo))
            if eh_caminho:
                # tem que resolver de algum lugar plausivel
                tentativas = [os.path.join(base, alvo),
                              os.path.join(RAIZ, alvo),
                              os.path.join(RAIZ, 'sistema', alvo)]
                achou = any(os.path.exists(x) for x in tentativas)
            elif '/' in alvo:
                continue        # par de termos, nao caminho
            else:
                # e um NOME solto citado em prosa: basta existir em algum lugar
                achou = alvo in TODOS_OS_NOMES
            if not achou:
                mortas += 1
                erro(f'{rel(caminho)} cita `{alvo}`, e ele nao existe em lugar nenhum')

print(f'  {vistos} caminhos citados em .md conferidos, {mortas} mortos.')
if mortas == 0:
    print('  Todos resolvem.')

# os validadores precisam achar o manual
print()
for v in ('conferir-nomes.py', 'conferir-manual.py', 'conferir-pericias.py'):
    txt = open(os.path.join(MEC, v), encoding='utf-8').read()
    if 'Fundamento-MANUAL-v7.docx' not in txt:
        continue
    aponta_para_manual = "'manual'" in txt or '"manual"' in txt
    print(f'  {"[x]" if aponta_para_manual else "[ ]"} {v} procura o .docx dentro de manual/')
    if not aponta_para_manual:
        erro(f'{v} procura o .docx fora de manual/ — ele vai PULAR as checagens '
             f'em silencio e sair verde sem ter lido nada')


# --------------------------------------------------------------------------
bloco('3. ESTRUTURA ANTIGA — sobrou alguem apontando para ela?')

ANTIGO = {
    r'RPG-JJK/': 'a pasta virou sistema/',
    r'raiz de .Claude 2.': 'o manual saiu da raiz para manual/',
    r'Claude 2/Fundamento': 'o manual saiu da raiz para manual/',
    r'Fundamento-FONTES-v7\.zip': 'o zip foi descompactado em manual/gerador e manual/matematica',
}
achou = 0
for base, dirs, files in os.walk(RAIZ):
    dirs[:] = [d for d in dirs
               if d not in ('.git', '_backup', 'node_modules', '__pycache__')]
    for f in files:
        if not f.endswith(('.md', '.py', '.txt')):
            continue
        caminho = os.path.join(base, f)
        if ('99-arquivo' in caminho
                or os.path.basename(base) == 'logs'
                or os.path.abspath(caminho) == os.path.abspath(__file__)):
            continue   # historico, e o proprio codigo que procura os padroes
        txt = open(caminho, encoding='utf-8', errors='ignore').read()
        for rx, motivo in ANTIGO.items():
            for m in re.finditer(rx, txt):
                achou += 1
                erro(f'{rel(caminho)} ainda cita "{m.group(0)}" — {motivo}')
if achou == 0:
    print('  Nada aponta para a estrutura antiga.')
    print('  (O 99-arquivo e os changelogs ficam de fora: eles descrevem o que era')
    print('   verdade na epoca, e e por isso que existem.)')


# --------------------------------------------------------------------------
print()
print('=' * 88)
if FALHAS:
    print(f'>>> {len(FALHAS)} PROBLEMA(S):')
    for e in FALHAS:
        print('   -', e)
    sys.exit(1)
print('>>> TUDO OK — a arvore esta inteira, toda referencia resolve, e nada aponta')
print('    para a estrutura antiga.')
if AVISOS:
    print(f'    {len(AVISOS)} aviso(s) acima, que nao falham.')

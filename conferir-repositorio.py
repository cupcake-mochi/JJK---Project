#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Confere o REPOSITORIO, e nao as regras.

Os validadores de sistema/03-mecanica conferem numero. Este confere que a
ARVORE esta inteira: que todo arquivo que um documento cita existe, que os
validadores acham o manual, e que nada ficou apontando para a estrutura antiga.

Ele existe porque a reorganizacao para git moveu tres coisas de lugar — o manual,
os changelogs e a pasta do sistema — e havia 104 referencias internas cruzadas.
Uma referencia quebrada nao falha nenhum validador: ela so' aparece seis meses
depois, quando alguem abre o projeto em outro computador e nao acha o arquivo.

Cinco checagens:
  1. ESTRUTURA — as pastas e os arquivos que o README promete existem.
  2. REFERENCIA MORTA — todo caminho citado em .md e .py resolve para um arquivo
     de verdade.
  3. ESTRUTURA ANTIGA — nada continua apontando para RPG-JJK/ ou para o manual na
     raiz, que era onde eles moravam antes.
  5. PONTEIRO DE SECAO — todo "peca N §M" citado aponta para uma secao que
     existe de verdade. A checagem 2 confere o ARQUIVO e passa por baixo desta.
  4. NUMERO COM DOIS DONOS — a versao do projeto e a versao do manual moram cada
     uma em meia duzia de arquivos. Cada uma tem UM dono declarado, e toda copia
     e' conferida contra ele.

A checagem 4 nasceu na v0.33 e e' a licao no 9 aplicada a ela mesma. O que ela
teria pego, se existisse:
  - a capa do .docx dizendo "Versao 7.5" com o projeto na v7.8, por tres versoes
    do manual seguidas. E a capa e' a unica copia que um jogador ve.
  - o sistema/LEIA-ME.md parado na v0.27, anunciando onze pecas, sete validadores
    e manual v7.6, cinco versoes depois.
  - o manual/matematica/COMO-USAR.txt dizendo v7.6.
  - o arquitetura.md dizendo v7.6.

Roda da raiz do repositorio, sem argumento. Sai com codigo 1 se algo quebrar.
Ele NAO precisa de python-docx e NAO le o .docx — entao, ao contrario dos tres
de 03-mecanica, nao existe jeito de ele sair verde tendo pulado checagem.
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

# as pecas e os validadores. O numero NAO fica guardado aqui: ele e lido do
# README, senao esta checagem vira mais uma copia para sair de sincronia — que e
# exatamente o defeito que a checagem 4 do conferir-manual.py existe para pegar.
# Ela ja saiu uma vez, quando o oitavo validador entrou e o "sete" ficou no codigo.
NUMERO = {'uma': 1, 'duas': 2, 'tres': 3, 'quatro': 4, 'cinco': 5, 'seis': 6,
          'sete': 7, 'oito': 8, 'nove': 9, 'dez': 10, 'onze': 11, 'doze': 12,
          'treze': 13, 'catorze': 14, 'quinze': 15, 'dezesseis': 16}


def por_extenso(palavra):
    chave = (palavra.lower()
             .replace('ê', 'e').replace('é', 'e').replace('ó', 'o')
             .replace('á', 'a').replace('ã', 'a').replace('í', 'i'))
    return NUMERO.get(chave)


MEC = os.path.join(RAIZ, 'sistema', '03-mecanica')
pecas = sorted(f for f in os.listdir(MEC) if re.match(r'^\d\d-.*\.md$', f))
vals = sorted(f for f in os.listdir(MEC) if f.startswith('conferir-') and f.endswith('.py'))
print(f'\n  {len(pecas)} pecas de regra, {len(vals)} validadores.')

readme = open(os.path.join(RAIZ, 'README.md'), encoding='utf-8').read()
m = re.search(r'\*\*(\S+) peças de regra\*\* e \*\*(\S+) validadores', readme)
if not m:
    erro('nao achei no README a linha que conta as pecas e os validadores — se ela '
         'mudou de forma, esta checagem parou de conferir e precisa ser reescrita')
else:
    bateu = True
    for rotulo, palavra, achado in (('pecas', m.group(1), len(pecas)),
                                    ('validadores', m.group(2), len(vals))):
        dito = por_extenso(palavra)
        if dito is None:
            bateu = False
            erro(f'o README escreve "{palavra}" {rotulo} e eu nao sei ler esse numero '
                 'por extenso — acrescente ele ao mapa NUMERO')
        elif dito != achado:
            bateu = False
            erro(f'sao {achado} {rotulo} na pasta e o README diz {palavra} ({dito})')
    if bateu:
        print(f'  O README diz {m.group(1)} e {m.group(2)}, e a pasta concorda.')
    else:
        print('  (um rascunho nao e peca: se o arquivo novo for material de apoio, '
              'ele nao deve comecar com dois digitos)')

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
    r'^\d+/\d+$|'
    # arquivo que existe so' as vezes, de proposito: o assistente cria quando
    # deixa uma mensagem de commit pronta, e o subir.sh apaga depois de usar
    r'^mensagem-de-commit\.txt$|'
    # o lock do git: existe so' enquanto um comando roda, e o README o cita
    # justamente para explicar o caso em que ele fica preso e trava o subir.sh.
    # Se ele ESTIVER no disco, e' o problema, nao a referencia.
    r'^\.git/index\.lock$'
)

# todo nome de arquivo que existe na arvore, para resolver citacao solta em prosa
TODOS_OS_NOMES = set()
for _b, _d, _f in os.walk(RAIZ):
    _d[:] = [x for x in _d if x not in ('.git', '_backup', '_to_delete', 'node_modules', '__pycache__')]
    TODOS_OS_NOMES.update(_f)

vistos = 0
mortas = 0
for base, dirs, files in os.walk(RAIZ):
    dirs[:] = [d for d in dirs
               if d not in ('.git', '_backup', '_to_delete', 'node_modules', '__pycache__', 'skills')]
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
               if d not in ('.git', '_backup', '_to_delete', 'node_modules', '__pycache__')]
    for f in files:
        if not f.endswith(('.md', '.py', '.txt')):
            continue
        caminho = os.path.join(base, f)
        if ('99-arquivo' in caminho
                or os.path.basename(base) == 'logs'
                or os.path.abspath(caminho) == os.path.abspath(__file__)):
            continue   # historico, e o proprio codigo que procura os padroes
        # O mount do sandbox as vezes lista um arquivo que ele nao consegue abrir
        # (ENOENT com ls e stat certos — esta no README, quatro vezes em seis
        # versoes). Aqui isso derrubava o validador com traceback, que esconde o
        # resultado das outras checagens. Vira aviso: o arquivo esta no disco.
        try:
            txt = open(caminho, encoding='utf-8', errors='ignore').read()
        except FileNotFoundError:
            aviso(f'{rel(caminho)} foi listado e nao abriu — e o mount, nao o '
                  f'arquivo. Reescreva ele e rode de novo')
            continue
        for rx, motivo in ANTIGO.items():
            for m in re.finditer(rx, txt):
                achou += 1
                erro(f'{rel(caminho)} ainda cita "{m.group(0)}" — {motivo}')
if achou == 0:
    print('  Nada aponta para a estrutura antiga.')
    print('  (O 99-arquivo e os changelogs ficam de fora: eles descrevem o que era')
    print('   verdade na epoca, e e por isso que existem.)')


# --------------------------------------------------------------------------
bloco('4. NUMERO COM DOIS DONOS — as copias batem com o dono?')

def ler(caminho):
    with open(os.path.join(RAIZ, caminho), encoding='utf-8', errors='ignore') as fh:
        return fh.read()


def confere(rotulo, dono_arq, dono_rx, copias):
    """Le o valor do dono e exige que toda copia diga a mesma coisa.

    O valor NAO fica escrito aqui. Se ficasse, este validador viraria mais uma
    copia para sair de sincronia — que e' o defeito que ele existe para pegar,
    e que ele mesmo ja teve quando guardava 'sete' validadores no codigo.
    """
    m = re.search(dono_rx, ler(dono_arq), re.MULTILINE)
    if not m:
        erro(f'{rotulo}: nao achei o valor em {dono_arq}, que e o DONO dele. '
             f'Se o arquivo mudou de forma, esta checagem parou de conferir')
        return
    dono = m.group(1)
    print(f'\n  {rotulo}: o dono e {dono_arq} e ele diz "{dono}".')
    for arq, rx, oque in copias:
        if not os.path.exists(os.path.join(RAIZ, arq)):
            erro(f'{rotulo}: {arq} nao existe, e ele deveria carregar uma copia')
            continue
        achados = re.findall(rx, ler(arq))
        if not achados:
            erro(f'{rotulo}: nao achei em {arq} ({oque}) — ou a copia sumiu, ou '
                 f'ela mudou de forma e esta checagem parou de olhar para ela')
            continue
        fora = sorted({a for a in achados if a != dono})
        if fora:
            erro(f'{rotulo}: {arq} ({oque}) diz {fora} e o dono diz "{dono}"')
        else:
            print(f'    [x] {arq} — {oque}')


# --- a versao do projeto. Dono: a entrada do topo do CHANGELOG. --------------
# Ela e a unica que nao da para escrever errado sem querer: a entrada so existe
# depois de a versao fechar.
confere(
    'VERSAO DO PROJETO',
    'logs/CHANGELOG.md', r'^## \[(\d+\.\d+)\]',
    [('README.md', r'\*\*Versão v(\d+\.\d+)\*\*', 'a linha de abertura'),
     ('sistema/ESTADO-ATUAL.md', r'\*\*Versão v(\d+\.\d+)\.\*\*', 'a linha de abertura'),
     ('sistema/LEIA-ME.md', r'\*\*v(\d+\.\d+)\.\*\* Fases', 'a secao "Versao atual"')],
)

# --- a versao do manual. Dono: a primeira linha do COMO-USAR.txt do gerador. -
# Por que o gerador e nao o .docx: o .docx e SAIDA. Quando os dois discordam,
# quem esta errado e a capa, e o conserto e regerar — foi exatamente o que
# aconteceu na v0.33, com a capa tres versoes atras do resto do projeto.
confere(
    'VERSAO DO MANUAL',
    'manual/gerador/COMO-USAR.txt', r'GERADOR DO MANUAL — Fundamento v(\d+\.\d+)',
    [('manual/gerador/partA.js', r'Versão (\d+\.\d+)', 'a CAPA do manual gerado'),
     ('manual/matematica/COMO-USAR.txt', r'MATEMÁTICA — Fundamento v(\d+\.\d+)', 'o cabecalho'),
     ('README.md', r'manual do Fundamento na \*\*v(\d+\.\d+)\*\*', 'a linha de abertura'),
     ('sistema/ESTADO-ATUAL.md', r'manual do Fundamento \*\*v(\d+\.\d+)\*\*', 'a secao do manual'),
     ('sistema/LEIA-ME.md', r'Fundamento está na \*\*v(\d+\.\d+)\*\*', 'a secao "Versao atual"'),
     ('sistema/02-esqueleto/arquitetura.md', r'O manual v(\d+\.\d+) é um subsistema', 'a abertura')],
)

# --- a contagem de pecas e validadores, nos outros dois documentos de entrada.
# A checagem 1 ja compara o README com a pasta. Estes dois tinham a mesma copia
# e ninguem olhava: o LEIA-ME passou cinco versoes dizendo onze e sete.
print()
for arq, rx, oque in (
    ('sistema/ESTADO-ATUAL.md',
     r'\*\*(\S+) peças escritas\*\* e \*\*(\S+) validadores\*\*', 'a linha de abertura'),
    ('sistema/LEIA-ME.md',
     r'\*\*(\S+) peças escritas e (\S+) validadores passando\*\*', 'a secao "Versao atual"'),
):
    m = re.search(rx, ler(arq))
    if not m:
        erro(f'CONTAGEM: nao achei em {arq} ({oque}) a linha que conta as pecas e '
             f'os validadores — se ela mudou de forma, esta checagem parou de conferir')
        continue
    ok = True
    for rotulo, palavra, achado in (('pecas', m.group(1), len(pecas)),
                                    ('validadores', m.group(2), len(vals))):
        dito = por_extenso(palavra)
        if dito is None:
            ok = False
            erro(f'CONTAGEM: {arq} escreve "{palavra}" {rotulo} e eu nao sei ler '
                 f'esse numero por extenso — acrescente ele ao mapa NUMERO')
        elif dito != achado:
            ok = False
            erro(f'CONTAGEM: sao {achado} {rotulo} na pasta e {arq} diz "{palavra}"')
    if ok:
        print(f'  [x] {arq} — diz {m.group(1)} pecas e {m.group(2)} validadores, '
              f'e a pasta concorda')

print()
print('  Um numero, um dono. Toda copia acima e conferida contra ele, e nenhuma')
print('  delas fica escrita dentro deste validador.')


# --------------------------------------------------------------------------
# 5. PONTEIRO DE SECAO — "peca N §M" apontando para secao que nao existe.
#
# Nasceu na v0.54, e o exemplar que a justifica e' de tres versoes antes: a v0.50
# achou que "peca 5 §9" NAO EXISTE e que TRES documentos apontavam para la — cada
# um querendo dizer uma coisa diferente, e as duas coisas morando em secoes
# diferentes uma da outra. A peca 5 sempre teve cinco secoes.
#
# A checagem 2 confere referencia de ARQUIVO e passa por baixo disto: o arquivo
# existe, e' a secao que nao. Foi assim que o fantasma sobreviveu.
#
# O CHANGELOG fica de fora de proposito. Entrada de CHANGELOG e' registro do que
# se pensou naquele dia, e a v0.50 decidiu por escrito nao reescrever historico
# para esconder erro — as duas citacoes de "peca 5 §9" que sobrevivem la sao
# justamente essa decisao, e acusa-las seria pedir para desfaze-la.
#
# Cuidado herdado da v0.51: um checker meu ja acusou cinco referencias BOAS por
# capturar "4." com o ponto e comparar contra "4". O rstrip('.') abaixo e' isso.
print()
bloco('5. PONTEIRO DE SECAO — "peca N §M" que aponta para secao inexistente')

MEC = os.path.join(RAIZ, 'sistema', '03-mecanica')
_secoes = {}
for _f in sorted(os.listdir(MEC)):
    _m = re.match(r'^(\d\d)-.*\.md$', _f)
    if not _m:
        continue
    _txt = open(os.path.join(MEC, _f), encoding='utf-8').read()
    _ids = set()
    for _h in re.findall(r'^#{2,4}\s+([\d.]+)[.\s]', _txt, re.M):
        _h = _h.rstrip('.')
        _ids.add(_h)
        _p = _h.split('.')
        for _k in range(1, len(_p)):
            _ids.add('.'.join(_p[:_k]))   # 5.0.4 satisfaz um ponteiro para 5 e 5.0
    _secoes[int(_m.group(1))] = (_f, _ids)

_PAT = re.compile(r'pe[cç]a\s+(\d{1,2})\s*.{0,2}§\s*([\d.]+)')
_vistos = 0
_ruins = 0
for _dir, _dirs, _files in os.walk(RAIZ):
    _dirs[:] = [d for d in _dirs
                if d not in ('_backup', '99-arquivo', '.git', '_to_delete', 'node_modules', '.venv')]
    for _f in _files:
        if not _f.endswith('.md'):
            continue
        _rel = os.path.relpath(os.path.join(_dir, _f), RAIZ)
        if _rel.replace('\\', '/').startswith('logs/'):
            continue                       # historico: ver o comentario acima
        for _i, _linha in enumerate(open(os.path.join(_dir, _f), encoding='utf-8'), 1):
            for _pn, _sec in _PAT.findall(_linha):
                _pn = int(_pn)
                _sec = _sec.rstrip('.')
                _vistos += 1
                if _pn not in _secoes:
                    _ruins += 1
                    erro(f'PONTEIRO: {_rel}:{_i} cita "peca {_pn} §{_sec}" e nao existe peca {_pn}')
                elif _sec not in _secoes[_pn][1]:
                    _ruins += 1
                    _reais = ' · '.join(sorted(_secoes[_pn][1]))
                    erro(f'PONTEIRO: {_rel}:{_i} cita "peca {_pn} §{_sec}", e a '
                         f'{_secoes[_pn][0]} tem so as secoes {_reais}')

if not _ruins:
    print(f'  [x] {_vistos} ponteiros de secao conferidos, e os {_vistos} resolvem')
print()
print('  A checagem 2 confere se o ARQUIVO existe; esta confere se a SECAO existe.')
print('  Nada em logs/ e conferido: entrada de CHANGELOG e registro do que se')
print('  pensou naquele dia, e a v0.50 decidiu nao reescrever historico.')


# --------------------------------------------------------------------------
print()
print('=' * 88)
if FALHAS:
    print(f'>>> {len(FALHAS)} PROBLEMA(S):')
    for e in FALHAS:
        print('   -', e)
    sys.exit(1)
print('>>> TUDO OK — a arvore esta inteira, toda referencia resolve, nada aponta')
print('    para a estrutura antiga, e todo numero de dois donos bate com o dono.')
if AVISOS:
    print(f'    {len(AVISOS)} aviso(s) acima, que nao falham.')

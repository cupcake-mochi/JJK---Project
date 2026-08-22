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

Nove checagens:
  1. ESTRUTURA — as pastas e os arquivos que o README promete existem.
  2. REFERENCIA MORTA — todo caminho citado em .md e .py resolve para um arquivo
     de verdade.
  3. ESTRUTURA ANTIGA — nada continua apontando para RPG-JJK/ ou para o manual na
     raiz, que era onde eles moravam antes.
  4. NUMERO COM DOIS DONOS — a versao do projeto e a versao do manual moram cada
     uma em meia duzia de arquivos. Cada uma tem UM dono declarado, e toda copia
     e' conferida contra ele.
  5. PONTEIRO DE SECAO — todo "peca N §M" citado aponta para uma secao que
     existe de verdade. A checagem 2 confere o ARQUIVO e passa por baixo desta.
  6. O MAPA — a tabela "Onde cada coisa esta" do ESTADO-ATUAL contra a pasta.
  7. A ENTREGA — o recorte de finalizado/ contra a fonte, byte a byte, e os
     ponteiros dele resolvidos contra a arvore DA ENTREGA.
  8. PENDENCIA MORTA — nenhum item de "Em aberto" pede coisa que ja existe.
  9. CONTAGEM DE CHECAGENS — o numero de checagens que cada validador tem e'
     lido do CODIGO, e todo documento que publica esse numero e' conferido
     contra ele. E a unica checagem em que o dono do numero e' o codigo.

O numero delas nao esta escrito em lugar nenhum alem desta linha: contagem
copiada envelhece na versao seguinte, e esta lista ja disse "cinco" com sete.
E a checagem 9 nao alcanca esta linha de proposito — ela le documento, e este
arquivo e' codigo.

A checagem 4 nasceu na v0.33 e e' a licao no 9 aplicada a ela mesma. O que ela
teria pego, se existisse:
  - a capa do .docx dizendo "Versao 7.5" com o projeto na v7.8, por tres versoes
    do manual seguidas. E a capa e' a unica copia que um jogador ve.
  - o sistema/LEIA-ME.md parado na v0.27, anunciando onze pecas, sete validadores
    e manual v7.6, cinco versoes depois.
  - o manual/matematica/COMO-USAR.txt dizendo v7.6.
  - o arquitetura.md dizendo v7.6.

Roda da raiz do repositorio, sem argumento. Sai com codigo 1 se algo quebrar.
Ele NAO precisa de python-docx e NAO le o .docx — entao, ao contrario dos CINCO
de 03-mecanica que leem, nao existe jeito de ele sair verde tendo pulado
checagem por falta da biblioteca. A checagem 7 pula quando finalizado/ nao
existe, e ela DIZ que pulou.
"""
import os
import re
import sys

RAIZ = os.path.dirname(os.path.abspath(__file__))
FALHAS = []
AVISOS = []
PULADAS = []


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
          'treze': 13, 'catorze': 14, 'quinze': 15, 'dezesseis': 16,
          'dezessete': 17, 'dezoito': 18, 'dezenove': 19, 'vinte': 20}


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
#
# `.claude` sai das quatro varreduras junto com `.git` e `node_modules`, e pelo
# mesmo motivo: o Claude Code abre worktree em
# sistema/05-material/livro/.claude/worktrees/<nome>/, e um worktree e' uma COPIA
# INTEIRA do repositorio dentro do repositorio. Sem esta linha o validador le a
# copia como se fosse material, e cada ponteiro morto do CHANGELOG e cada nome
# aposentado aparece DUAS vezes — uma pelo arquivo real, outra pelo espelho. Na
# v0.107 isso rendeu oito falsos, todos com `.claude/worktrees/` no caminho.
TODOS_OS_NOMES = set()
for _b, _d, _f in os.walk(RAIZ):
    _d[:] = [x for x in _d if x not in ('.git', '.claude', '_backup', '_to_delete', 'node_modules', '__pycache__')]
    TODOS_OS_NOMES.update(_f)

vistos = 0
mortas = 0
for base, dirs, files in os.walk(RAIZ):
    dirs[:] = [d for d in dirs
               if d not in ('.git', '.claude', '_backup', '_to_delete', 'node_modules', '__pycache__', 'skills')]
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
               if d not in ('.git', '.claude', '_backup', '_to_delete', 'node_modules', '__pycache__')]
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
                if d not in ('_backup', '99-arquivo', '.git', '.claude', '_to_delete', 'node_modules', '.venv')]
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


# --- checagem 6: o mapa do ESTADO-ATUAL contra a pasta. ----------------------
# Nasceu na v0.59. A tabela "Onde cada coisa esta" e uma COPIA da listagem da
# pasta, e ela nao tinha dono nem validador — que sao as duas saidas que a
# licao no 9 admite. Ela tinha divergido: faltavam as pecas 13 e 14 (as duas
# maiores do projeto) e SEIS validadores, e nada acusava.
#
# A checagem 1 conta quantas pecas existem. Esta confere quais estao NO MAPA,
# que e outra pergunta: um contador certo convive com um mapa furado.
print()
print('-' * 88)
print('  6. O MAPA — a tabela "Onde cada coisa esta" contra a pasta de verdade')
print('-' * 88)

_est_txt = open(os.path.join(RAIZ, 'sistema', 'ESTADO-ATUAL.md'), encoding='utf-8').read()
_pecas_disco = sorted(f for f in os.listdir(os.path.join(RAIZ, 'sistema', '03-mecanica'))
                      if re.match(r'^\d\d-.*\.md$', f))
_vals_disco = sorted(f for f in os.listdir(os.path.join(RAIZ, 'sistema', '03-mecanica'))
                     if re.match(r'^conferir-.*\.py$', f))
_fora_p = [f for f in _pecas_disco if f'`03-mecanica/{f}`' not in _est_txt]
_fora_v = [f for f in _vals_disco if f'`03-mecanica/{f}`' not in _est_txt]

print(f'  {len(_pecas_disco)} pecas e {len(_vals_disco)} validadores na pasta.')
if _fora_p:
    FALHAS.append('o mapa do ESTADO-ATUAL nao cita a(s) peca(s): ' + ', '.join(_fora_p))
else:
    print(f'  [x] as {len(_pecas_disco)} pecas aparecem no mapa')
if _fora_v:
    FALHAS.append('o mapa do ESTADO-ATUAL nao cita o(s) validador(es): ' + ', '.join(_fora_v))
else:
    print(f'  [x] os {len(_vals_disco)} validadores aparecem no mapa')

# e o caminho contrario: o mapa nao pode citar arquivo que nao existe mais.
# (a checagem 2 ja pega isso para o repositorio inteiro; aqui e so o contador)
_citados = set(re.findall(r'`03-mecanica/([^`]+)`', _est_txt))
_fantasma = sorted(c for c in _citados
                   if not os.path.exists(os.path.join(RAIZ, 'sistema', '03-mecanica', c)))
if _fantasma:
    FALHAS.append('o mapa cita arquivo que nao existe: ' + ', '.join(_fantasma))
else:
    print(f'  [x] os {len(_citados)} arquivos citados no mapa existem')

print()
print('  Um mapa furado nao quebra contagem nenhuma — por isso ele passou seis')
print('  versoes furado. Quem retoma em conversa nova le o mapa, nao a pasta.')


# --- checagem 7: a ENTREGA contra a fonte. -----------------------------------
# Nasceu na v0.98, e o defeito que ela existe para pegar e' de EIXO e nao de
# conteudo: a checagem 2 resolve nome de arquivo contra a arvore INTEIRA, entao
# uma peca copiada para finalizado/ herda os arquivos da fonte e todo ponteiro
# dela passa trivialmente. Com o recorte da v0.97 no disco, a checagem 2 via
# 472 caminhos e dizia "0 mortos" — e 95 deles nao resolviam de dentro da
# entrega, 19 apontando para material de mesa que nao estava la.
#
# A entrega e' ARTEFATO: nada nela e' editado a mao, com UMA excecao — o
# README.md dela, que nao existe na fonte e afirma numero. Ele era o unico
# arquivo do projeto que ninguem comparava com nada, e na v0.98 estava errado em
# seis lugares, o mais velho desde a v0.83.
#
# Se finalizado/ nao existir — ele e' ignorado pelo .gitignore, entao um clone
# limpo nao tem — esta checagem PULA e DIZ que pulou. Licao da v0.97: um verde
# que pulou checagem nao e' um verde.
print()
print('-' * 88)
print('  7. A ENTREGA — o recorte confere com a fonte?')
print('-' * 88)

ENT = os.path.join(RAIZ, 'finalizado')

if not os.path.isdir(ENT):
    PULADAS.append('7. a entrega — finalizado/ nao existe neste clone')
    print('  ~~ PULADA. finalizado/ nao existe aqui, e ele e ignorado pelo .gitignore,')
    print('     entao um clone limpo do repositorio de trabalho nao carrega o recorte.')
    print('     NADA da checagem 7 rodou.')
else:
    import hashlib

    def _md5(caminho):
        with open(caminho, 'rb') as fh:
            return hashlib.md5(fh.read()).hexdigest()

    # -- 7.1: toda copia bate byte a byte com a fonte. ------------------------
    # A entrega nao tem validador proprio e nenhum outro atravessa repositorio.
    # Ate aqui, a unica forma de saber se ela estava velha era md5 na mao.
    ESPERADO = [(os.path.join(MEC, f), os.path.join(ENT, 'regra', f)) for f in pecas]
    for f in sorted(os.listdir(RAIZ)):
        if re.match(r'^(DESENHO|LISTA)-.*\.md$', f):
            ESPERADO.append((os.path.join(RAIZ, f), os.path.join(ENT, 'desenho', f)))
    ESPERADO += [
        (os.path.join(RAIZ, 'sistema', '02-esqueleto', 'arquitetura.md'),
         os.path.join(ENT, 'desenho', 'arquitetura.md')),
        (os.path.join(MEC, 'RASCUNHO-bloqueio.md'),
         os.path.join(ENT, 'desenho', 'RASCUNHO-bloqueio.md')),
    ]
    for f in ('Fundamento-MANUAL-v7.docx', 'Fundamento-MANUAL-v7.pdf'):
        ESPERADO.append((os.path.join(RAIZ, 'manual', f), os.path.join(ENT, 'manual', f)))
    for f in ('ficha-em-branco.docx', 'ficha-exemplo-kaori.docx'):
        ESPERADO.append((os.path.join(RAIZ, 'sistema', '05-material', f),
                         os.path.join(ENT, 'ficha', f)))
    # O livro entrou no recorte na v0.114, e o motivo foi um defeito real: na
    # v0.112 o .pdf publicado estava TRES versoes atrasado — sem as condicoes
    # reescritas, sem o capitulo 11 reordenado, sem o vocabulario novo e sem a
    # regra de vida temporaria — e ninguem acusou, porque `livro/` nunca esteve
    # aqui. Ele so apareceu porque o build foi rodado para testar outra coisa.
    #
    # A fonte e' o que o build gera em 05-material/livro/, e nao o fonte .md:
    # o que a entrega carrega e' o artefato, e e' ele que envelhece calado.
    LIVRO = os.path.join(RAIZ, 'sistema', '05-material', 'livro')
    for f in ('Projeto-M-Manual-da-Guilda.pdf',
              'Projeto-M-Manual-da-Guilda-REVISAO.docx'):
        ESPERADO.append((os.path.join(LIVRO, f), os.path.join(ENT, 'livro', f)))

    # guarda de contagem: se o recorte encolher, ela acusa em vez de conferir
    # menos em silencio. Piso = 17 pecas + 4 desenhos + 2 avulsos + 2 do manual
    # + 2 fichas + 2 do livro, e ele so' cresce.
    PISO_RECORTE = 29
    if len(ESPERADO) < PISO_RECORTE:
        erro(f'7.1: o recorte deveria ter pelo menos {PISO_RECORTE} arquivos e eu montei '
             f'{len(ESPERADO)} — a lista mudou de forma e esta checagem parou de conferir')

    sumidos, velhos = [], []
    for orig, copia in ESPERADO:
        if not os.path.exists(orig):
            erro(f'7.1: a FONTE de {rel(copia)} sumiu — procurei em {rel(orig)}')
        elif not os.path.exists(copia):
            sumidos.append(rel(copia))
        elif _md5(orig) != _md5(copia):
            velhos.append(rel(copia))
    if sumidos:
        erro('7.1: a entrega nao tem copia de: ' + ', '.join(sumidos))
    if velhos:
        erro('7.1: a copia na entrega esta VELHA, nao bate com a fonte: ' + ', '.join(velhos))
    if not sumidos and not velhos:
        print(f'  [x] as {len(ESPERADO)} copias da entrega batem byte a byte com a fonte')

    # -- 7.2: ponteiro pendurado, resolvido contra a arvore DA ENTREGA. -------
    #
    # A lista branca e' DECLARADA e tem teto. O que entra nela sao as duas
    # familias que a entrega cita de proposito sem carregar: nome de validador
    # ("o conferir-X.py confere isto") e caminho de arquivo de trabalho. As duas
    # sao argumento de design, e o README da entrega ja avisa que as pecas sao
    # argumento e nao texto de mesa.
    #
    # O que NAO entra e' material de mesa: se uma peca da entrega manda o leitor
    # abrir um arquivo de regra, aquele arquivo tem que estar aqui.
    BRANCOS_RX = re.compile(
        r'^(conferir-[a-z-]+\.py'
        r'|subir\.sh|mensagem-de-commit\.txt'
        r'|ESTADO-ATUAL\.md|LEIA-ME\.md|CHANGELOG\.md|PROMPT-[A-Z-]+\.md'
        r'|pitch-de-design\.md|dossie-de-metodologia\.md'
        r'|dados\.js|ficha\.js|pac7\.py|v7\.py|bf2\.py|validador-feiticos\.py'
        r'|(?:sistema/)?\d\d-[a-z-]+/.*'      # caminho na arvore da FONTE
        r'|logs/.*|99-arquivo/.*|gerador-ficha/.*'
        r'|RASCUNHO-trilhas\.md'              # cortado do recorte por decisao
        r')$'
    )
    NOMES_ENT = set()
    for _b, _d, _f in os.walk(ENT):
        _d[:] = [x for x in _d if x != '.git']
        NOMES_ENT.update(_f)

    vistos_e, brancos, pendurados = 0, 0, []
    for base, dirs, arqs in os.walk(ENT):
        dirs[:] = [d for d in dirs if d != '.git']
        for f in sorted(arqs):
            if not f.endswith('.md'):
                continue
            caminho = os.path.join(base, f)
            txt = open(caminho, encoding='utf-8', errors='ignore').read()
            for m in RX_MD.finditer(txt):
                alvo = m.group(1).strip()
                if IGNORAR.search(alvo) or ' ' in alvo:
                    continue
                vistos_e += 1
                eh_caminho = '/' in alvo and (alvo.endswith('/') or re.search(r'\.\w{2,4}$', alvo))
                if eh_caminho:
                    achou = any(os.path.exists(x) for x in
                                (os.path.join(base, alvo), os.path.join(ENT, alvo)))
                elif '/' in alvo:
                    continue
                else:
                    achou = alvo in NOMES_ENT
                if achou:
                    continue
                if BRANCOS_RX.match(alvo):
                    brancos += 1
                    continue
                pendurados.append((rel(caminho), alvo))

    # guarda nos dois eixos: se as citacoes despencarem o extrator quebrou; se
    # os brancos crescerem, alguem alargou a lista sem dizer.
    # medido na v0.98: 161 citacoes, 85 delas brancas. O teto tem folga de cinco
    # e nao mais — quem precisar de mais que isso esta acrescentando familia nova
    # a lista, e ai o numero sobe junto com o motivo escrito.
    #
    # v0.99: 174 e 91. As seis novas sao a peca 18 citando os tres validadores
    # que leem a coluna de espacos dela e o caminho do arquitetura.md na arvore
    # da FONTE, mais duas da peca 2. Nenhuma familia nova — o teto vai a 96.
    #
    # v0.103: 99 brancas. As seis novas sao a peca 19 citando o conferir-dano.py
    # e o conferir-catalogo.py, mais as pecas que ganharam ponteiro para o
    # validador novo quando as condicoes mudaram de casa. TODAS sao "nome de
    # validador", que e' a primeira das duas familias ja declaradas — nenhuma
    # familia nova. O teto vai a 104, que e' a mesma folga de cinco.
    #
    # v0.117: 107 brancas. As oito novas saem das secoes que a v0.116 e a v0.117
    # escreveram — a peca 9 §8 citando o conferir-atributos.py, a peca 11 §6.8
    # citando o conferir-equipamento.py e caminhos da arvore da fonte, a peca 1
    # §5.0 e a peca 19 §2.2 apontando para os donos das constantes que se moveram.
    # Conferidas uma a uma: TODAS sao "nome de validador" ou "caminho de arquivo
    # de trabalho", que sao as duas familias declaradas la em cima — nenhuma
    # familia nova, e nenhuma delas e material de mesa. O teto vai a 112, que e'
    # a mesma folga de cinco.
    PISO_CITACOES, TETO_BRANCOS = 120, 112
    if vistos_e < PISO_CITACOES:
        erro(f'7.2: achei so {vistos_e} citacoes na entrega, e o piso e {PISO_CITACOES} — '
             f'o extrator mudou de forma e esta checagem parou de conferir')
    if brancos > TETO_BRANCOS:
        erro(f'7.2: {brancos} citacoes cairam na lista branca, e o teto e {TETO_BRANCOS} — '
             f'alguem alargou a lista; confira o que entrou nela')
    for arq, alvo in pendurados:
        erro(f'7.2: {arq} manda abrir `{alvo}`, e ele nao existe na entrega')
    if not pendurados:
        print(f'  [x] {vistos_e} citacoes conferidas contra a arvore DA ENTREGA, '
              f'{brancos} na lista branca declarada, 0 penduradas')

    # -- 7.3: o README da entrega afirma numero, e cada numero tem dono. ------
    _rme = open(os.path.join(ENT, 'README.md'), encoding='utf-8').read()

    def _entrega_confere(rotulo, rx_copia, dono_arq, rx_dono, extenso=False):
        m = re.search(rx_dono, ler(dono_arq), re.MULTILINE)
        if not m:
            erro(f'7.3: nao achei {rotulo} em {dono_arq}, que e o DONO dele — se o '
                 f'arquivo mudou de forma, esta checagem parou de conferir')
            return
        dono = por_extenso(m.group(1)) if extenso else m.group(1)
        if dono is None:
            erro(f'7.3: {dono_arq} escreve "{m.group(1)}" para {rotulo} e eu nao sei ler '
                 f'esse numero por extenso — acrescente ele ao mapa NUMERO')
            return
        achados = re.findall(rx_copia, _rme)
        if not achados:
            erro(f'7.3: nao achei {rotulo} no README da entrega — ou a frase sumiu, ou '
                 f'ela mudou de forma e esta checagem parou de olhar para ela')
            return
        lidos = [por_extenso(a) if extenso else a for a in achados]
        fora = sorted({str(a) for a in lidos if a != dono})
        if fora:
            erro(f'7.3: o README da entrega diz {fora} para {rotulo}, e o dono '
                 f'({dono_arq}) diz "{dono}"')
        else:
            print(f'    [x] {rotulo}: {len(achados)} ocorrencia(s), todas "{dono}"')

    print()
    print('  7.3 O README da entrega e o unico arquivo escrito a mao la.')
    _entrega_confere('a versao do recorte', r'\*\*Recorte da v(\d+\.\d+)\.\*\*',
                     'logs/CHANGELOG.md', r'^## \[(\d+\.\d+)\]')
    _entrega_confere('a versao do manual', r'\*\*v(\d+\.\d+)\*\*',
                     'manual/gerador/COMO-USAR.txt',
                     r'GERADOR DO MANUAL — Fundamento v(\d+\.\d+)')
    _entrega_confere('a contagem de pecas', r'as \*\*(\w+) peças\*\* de mecânica',
                     'README.md', r'\*\*(\S+) peças de regra\*\*', extenso=True)
    _entrega_confere('a contagem de condicoes', r'as (\w+) condições',
                     'sistema/03-mecanica/'
                     + next(p for p in pecas if 'condicoes' in p),
                     r'^## 3\. As (\w+) condições', extenso=True)
    _entrega_confere('o total de entradas do catalogo', r'das \*\*(\d+) entradas\*\*',
                     'sistema/03-mecanica/17-catalogo-de-entregas.md',
                     r'^\| \*\*total\*\* \| \*\*(\d+)\*\*')

    print()
    print('  A entrega e artefato e nao tem validador proprio. Esta checagem e a unica')
    print('  coisa do projeto que atravessa os dois repositorios.')


# --- checagem 8: a lista "Em aberto" contra o que ja existe. -----------------
# Nasceu na v0.100. As secoes "Em aberto" das dezoito pecas somavam 72 itens vivos
# e pelo menos onze deles ja tinham fechado — dois DENTRO da propria peca: a peca
# 11 §9 pedia as quatro anti-dominio que a §6.5 dela publica desde a v0.29, e a
# peca 13 §10 pedia um conserto que a §9 dela mesma tinha aplicado na v0.39.
#
# Nenhum validador lia essas secoes, e por isso elas nao envelheciam devagar:
# elas paravam. Uma lista de pendencia que mente e' pior que nenhuma, porque ela
# manda trabalhar no que ja esta feito e esconde o que falta no meio.
#
# A regra, em uma frase: UM ITEM DE PENDENCIA NAO PODE TER COMO ASSUNTO — nem
# esperar, nem pedir validador de — COISA QUE JA EXISTE NA PASTA.
#
# ESCOPO, e ele e' a metade dificil. A licao da v0.98 e' que uma checagem que
# resolve referencia contra uma arvore MAIOR que o objeto conferido passa de
# graca; aqui o risco e' o contrario — escopo estreito demais tambem passa de
# graca. As duas guardas embaixo sao contra isso: as dezoito pecas TEM de ter
# secao de pendencia, e o total de linhas vivas tem de ser maior que zero.
#
# O que NAO conta como item vivo, e cada exclusao tem motivo:
#   - linha com `~~`            : riscada e' fechada, e e' a convencao da casa
#   - o corpo de um item riscado: a tabela de especificacao segue o item dono
#   - linha comecando com `>`   : a v0.81 declarou `>` como historia
#   - linha que diz "fechad/fechou/resolvid" e nao diz "falta": ela se declara
#   - dentro de secao de FILA   : so linha de tabela; o resto e' argumento
print()
bloco('8. PENDENCIA MORTA — item de "Em aberto" apontando para coisa que existe')

import unicodedata as _ud


def _sa(t):
    t = _ud.normalize('NFD', t)
    return ''.join(c for c in t if _ud.category(c) != 'Mn').lower()


_STOP = set('a o e de da do das dos que em no na nos nas um uma uns umas ao aos '
            'as os por para com sem'.split())


def _pal(t):
    t = re.sub(r'[^a-z0-9 ]', ' ', re.sub(r'[`*_~\[\]()#|>]', ' ', _sa(t)))
    return {w for w in t.split() if w and w not in _STOP and len(w) > 1}


_CAB_PEND = re.compile(r'em aberto|o que fica para|destrava|o que nao existe|'
                       r'a fila|o que falta\b')
_SO_TABELA = re.compile(r'a fila')
_ITEM = re.compile(r'^\s{0,3}(?:[-*]|\d+\.)\s+\S')
_FECHADO = re.compile(r'fechad|fechou|fecharam|resolvid|respondid|escrito na v|corrigid')
_FALTA = re.compile(r'\bfalta\b|nao existe|precisa ter|precisa de|que sai junto|'
                    r'checagens que ele precisa')
_BLOQUEIO = re.compile(r'travad|ate a |ate o |enquanto|bloquead|depende de|espera|'
                       r'nao existe|falta')


def _secoes_pendencia(txt):
    out, atual, buf = [], None, []
    for l in txt.split('\n'):
        if re.match(r'^#{2,4} ', l):
            if atual:
                out.append((atual, buf))
            atual, buf = (l if _CAB_PEND.search(_sa(l)) else None), []
        elif atual is not None:
            buf.append(l)
    if atual:
        out.append((atual, buf))
    return out


def _linhas_vivas(linhas, solto, so_tabela):
    morto, saida = False, []
    for l in linhas:
        if _ITEM.match(l):
            morto = l.lstrip().lstrip('-*0123456789. ').startswith('~~')
        if morto or '~~' in l:
            continue
        if l.lstrip().startswith('>'):
            continue
        if re.match(r'^\s*\|\s*[-: ]+\|', l):
            continue
        tab = l.lstrip().startswith('|')
        _sl = _sa(l)
        # so' em TABELA: a celula de estado declara "fechado" e a linha inteira
        # e' registro. Em item de lista a convencao da casa e' o `~~`, e ler
        # "fechou" no meio da prosa de um item VIVO o apagaria em silencio.
        if tab and _FECHADO.search(_sl) and not _FALTA.search(_sl):
            continue
        if so_tabela and not tab:
            continue
        if solto:
            if l.strip() and not l.startswith('#'):
                saida.append(l)
        elif _ITEM.match(l) or tab:
            saida.append(l)
    return saida


def _assunto(l, solto=False):
    """O SUJEITO do item — e ele muda de forma com a forma da linha."""
    if solto:
        return l                                     # prosa: a frase inteira
    if l.lstrip().startswith('|'):
        for c in [c.strip() for c in l.strip().strip('|').split('|')]:
            if c and not re.fullmatch(r'~*\d+~*', c):
                return c                             # tabela: a 1a celula com texto
        return ''
    m = re.search(r'\*\*(.+?)\*\*', l)
    return m.group(1) if m else l                    # item: o primeiro negrito


_MEC8 = os.path.join(RAIZ, 'sistema', '03-mecanica')
_P8 = sorted(f for f in os.listdir(_MEC8) if re.match(r'^\d\d-.*\.md$', f))
_V8 = sorted(f for f in os.listdir(_MEC8) if re.match(r'^conferir-.*\.py$', f))
_SLUG8 = {f: _pal(f[3:-3].replace('-', ' ')) for f in _P8}
_TOPICO8 = {v: _sa(v[len('conferir-'):-3]) for v in _V8}


def _dono8(nome):
    """O validador dono de uma peca, DERIVADO do slug — sem tabela escrita."""
    if nome not in _SLUG8:
        return None
    partes = nome[3:-3].split('-')
    for i in range(len(partes), 0, -1):
        c = 'conferir-' + '-'.join(partes[:i]) + '.py'
        if c in _V8:
            return c
    for p in partes:
        c = f'conferir-{p}.py'
        if c in _V8:
            return c
    return None


_MANUAL8 = re.search(r'v(7\.\d+)', open(os.path.join(
    RAIZ, 'manual', 'gerador', 'COMO-USAR.txt'), encoding='utf-8').readline()).group(1)

_ALVOS8 = [('sistema/03-mecanica/' + p, p) for p in _P8] + \
          [('sistema/ESTADO-ATUAL.md', None), ('README.md', None)]

_mortas, _n_sec, _n_vivas, _sem_secao = [], 0, 0, []
for _rel8, _peca8 in _ALVOS8:
    _txt8 = open(os.path.join(RAIZ, _rel8), encoding='utf-8').read()
    _secs8 = _secoes_pendencia(_txt8)
    if _peca8 and not _secs8:
        _sem_secao.append(_peca8)
    for _tit8, _lins8 in _secs8:
        _n_sec += 1
        _solto8 = 'o que nao existe' in _sa(_tit8)
        for _l8 in _linhas_vivas(_lins8, _solto8, bool(_SO_TABELA.search(_sa(_tit8)))):
            _n_vivas += 1
            _sl8 = _sa(_l8)
            _suj8 = _assunto(_l8, _solto8)
            _w8 = _pal(_suj8)
            _corte = _l8.strip()[:70]
            # 8a — o item pede validador, e o validador existe
            if 'validador' in _sl8 and _FALTA.search(_sl8):
                _alvo8 = _dono8(_peca8) if _peca8 else None
                if not _alvo8:
                    for _v8, _t8 in _TOPICO8.items():
                        if re.search(r'\b' + re.escape(_t8), _sa(_suj8)):
                            _alvo8 = _v8
                            break
                if _alvo8:
                    _mortas.append((_rel8, '8a', f'o {_alvo8} existe', _corte))
            # 8b — o item esta travado por versao do manual que ja passou
            _m8 = re.search(r'manual v(7\.\d+)', _sl8)
            if _m8 and _BLOQUEIO.search(_sl8) and \
                    float(_m8.group(1)[2:]) <= float(_MANUAL8[2:]):
                _mortas.append((_rel8, '8b', f'o manual esta na v{_MANUAL8}', _corte))
            # 8c — o assunto do item e uma peca que ja existe
            for _pf8, _pw8 in _SLUG8.items():
                if _pf8 != _peca8 and _pw8 and _pw8 <= _w8:
                    _mortas.append((_rel8, '8c', f'a {_pf8} existe', _corte))
                    break
            # 8d — o item espera uma peca que ja existe
            for _esp8 in re.findall(r'espera[m]?\s+([^,;.|)]+)', _sl8):
                _we8 = _pal(_esp8)
                for _pf8, _pw8 in _SLUG8.items():
                    if _pf8 != _peca8 and _pw8 and _pw8 <= _we8:
                        _mortas.append((_rel8, '8d', f'a {_pf8} existe', _corte))
                        break

print(f'  {_n_sec} secoes de pendencia, {_n_vivas} linhas vivas, '
      f'manual na v{_MANUAL8}.')
if _sem_secao:
    erro(f'8: {len(_sem_secao)} peca(s) sem secao de pendencia nenhuma: '
         + ', '.join(_sem_secao)
         + ' — ou a peca perdeu a secao, ou o cabecalho mudou de forma e esta '
           'checagem parou de conferir')
elif _n_vivas < len(_P8):
    erro(f'8: so {_n_vivas} linha(s) viva(s) em {len(_P8)} pecas — o extrator '
         'mudou de forma e esta checagem parou de conferir')
else:
    print(f'  [x] as {len(_P8)} pecas tem secao de pendencia, e o extrator acha '
          'linha viva em todas')

if _mortas:
    for _r8, _q8, _pq8, _tx8 in _mortas:
        erro(f'PENDENCIA MORTA [{_q8}]: {_r8} — {_pq8}\n       {_tx8}')
else:
    print(f'  [x] nenhuma das {_n_vivas} linhas vivas pede coisa que ja existe')

print()
print('  8a pede validador que existe · 8b trava em versao do manual que passou ·')
print('  8c tem por assunto uma peca que existe · 8d espera uma peca que existe.')
print('  Riscar com ~~ fecha o item E o corpo dele — e' + " e' " + 'a convencao da casa.')


# --- checagem 9: a contagem de checagens de cada validador. ------------------
# Nasceu na v0.102, e ela e' a licao no 9 num eixo que nenhuma outra alcanca:
# aqui o DONO DO NUMERO E' O CODIGO. Ate agora o projeto tratava documento como
# dono e codigo como copia; esta e a direcao contraria.
#
# O que ela teria pego, e a v0.100 achou as tres na mao:
#   - o conferir-equipamento.py publicado como "dez checagens" tendo onze
#   - o conferir-catalogo.py publicado como "dez" no LEIA-ME, "nove" na peca 17
#     e "onze" no ESTADO-ATUAL — tres respostas para o mesmo numero
#   - o proprio conferir-repositorio.py com "Cinco checagens" na docstring
#     enquanto rodava sete
#
# A DEFINICAO, e ela precisa ser exata porque a checagem se mede contra ela:
# uma checagem e' UM BLOCO NUMERADO que o validador imprime — `bloco('N. ...')`
# ou `print('N. ...')`. Sub-bloco (`5.1`, `4d`) conta para o bloco pai. O bloco
# `0` conta, e o conferir-atributos.py e' o unico que tem um.
print()
bloco('9. CONTAGEM DE CHECAGENS — o codigo e o dono, e os documentos sao copia')

_RX_BLOCO = re.compile(r"""(?:^|\\n|['"])\s*(?:=|\s)*(\d+)[.)]\s+[A-ZÁÂÃÀÉÊÍÓÔÕÚÇ]""")


def _contar_blocos(caminho, repetidos=None):
    """Os numeros de bloco de um validador.

    v0.118: passou a devolver tambem os REPETIDOS, e o motivo e um defeito real.
    O `set()` come numero duplicado em silencio: um validador com dois blocos `6`
    conta 6 uma vez so, entao a checagem nova que alguem escreveu com um numero ja
    usado fica INVISIVEL na contagem — e a guarda de buraco nao pega, porque nao
    existe buraco. Aconteceu no conferir-aptidoes.py, que tinha dois `6` desde a
    v0.104 e ganhou um segundo `7` quando a checagem da Lapidacao foi escrita.
    """
    nums, vistos = set(), []
    for _l in open(caminho, encoding='utf-8'):
        if not re.match(r"^\s*(bloco|print)\(", _l):
            continue
        for _m in _RX_BLOCO.finditer(_l):
            _n = int(_m.group(1))
            if _n in nums and repetidos is not None:
                repetidos.append((os.path.basename(caminho), _n))
            nums.add(_n)
            vistos.append(_n)
    return nums


_VAL9, _REPETIDOS = {}, []
for _f9 in sorted(os.listdir(MEC)):
    if re.match(r'^conferir-.*\.py$', _f9):
        _VAL9[_f9] = _contar_blocos(os.path.join(MEC, _f9), _REPETIDOS)
_VAL9['conferir-repositorio.py'] = _contar_blocos(
    os.path.join(RAIZ, 'conferir-repositorio.py'), _REPETIDOS)

# guarda 0: numero de bloco REPETIDO. Ele nao abre buraco, entao a guarda 2 nao o
# pega — e ele faz a contagem MENTIR PARA BAIXO, escondendo a checagem mais nova.
if _REPETIDOS:
    erro('9: bloco numerado repetido em ' + ', '.join(
        f'{_v} (o {_n} duas vezes)' for _v, _n in _REPETIDOS)
        + ' — o `set()` da contagem come o segundo, entao a checagem mais nova '
          'fica invisivel no total. Renumere.')

# guarda 1: validador sem bloco numerado e' extrator quebrado, nao validador vazio
_mudos = sorted(v for v, n in _VAL9.items() if not n)
if _mudos:
    erro(f'9: {len(_mudos)} validador(es) sem bloco numerado nenhum: ' + ', '.join(_mudos)
         + ' — ou eles mudaram de forma, ou o extrator parou de achar bloco')

# guarda 2: a numeracao nao pode ter buraco. Um buraco quer dizer checagem
# removida sem renumerar, e a contagem passa a mentir mesmo estando "certa".
_furados = []
for _v9, _n9 in _VAL9.items():
    if not _n9:
        continue
    _lo = min(_n9)
    if _lo not in (0, 1) or sorted(_n9) != list(range(_lo, _lo + len(_n9))):
        _furados.append(f'{_v9} ({sorted(_n9)})')
if _furados:
    erro('9: a numeracao tem buraco em: ' + ' · '.join(_furados))

_PECAS9 = sorted(f for f in os.listdir(MEC) if re.match(r'^\d\d-.*\.md$', f))


def _dono9(nome):
    """o validador dono de uma peca, DERIVADO do slug — sem tabela escrita"""
    partes = nome[3:-3].split('-')
    for _i in range(len(partes), 0, -1):
        _c = 'conferir-' + '-'.join(partes[:_i]) + '.py'
        if _c in _VAL9:
            return _c
    for _p in partes:
        _c = f'conferir-{_p}.py'
        if _c in _VAL9:
            return _c
    return None


_DONO_PECA9 = {int(p[:2]): _dono9(p) for p in _PECAS9}

_NUM9 = {'uma': 1, 'um': 1, 'duas': 2, 'dois': 2, 'tres': 3, 'quatro': 4, 'cinco': 5,
         'seis': 6, 'sete': 7, 'oito': 8, 'nove': 9, 'dez': 10, 'onze': 11, 'doze': 12,
         'treze': 13, 'catorze': 14, 'quatorze': 14, 'quinze': 15, 'dezesseis': 16,
         'dezessete': 17, 'dezoito': 18, 'dezenove': 19, 'vinte': 20, 'trinta': 30}
_PAL9 = '|'.join(_NUM9)
_RX_QTD = re.compile(rf'(\*{{0,2}}(?:\d+|{_PAL9})\*{{0,2}})\s*\*{{0,2}}\s*'
                     r'(?:checagens?|blocos? de checagem)', re.I)
# afirmacao de INCREMENTO ou de ESPECIFICACAO nao e' contagem total
_RX_NAO9 = re.compile(r'\bnovas?\b|\ba mais\b|precisa ter|que ele precisa|'
                      r'que esta regua pede|nasceu a checagem|ganhou a checagem|'
                      r'checagens do §|checagens do rascunho')
_RX_VAL9 = re.compile(r'`(conferir-[a-z]+\.py)`')
_RX_PECA9 = re.compile(r'(?:checagens?|blocos? de checagem)\s+d[ao]\s+pe[cç]a\s+(\d{1,2})', re.I)

_ALVOS9 = ['README.md', 'sistema/ESTADO-ATUAL.md', 'sistema/LEIA-ME.md'] + \
          ['sistema/03-mecanica/' + p for p in _PECAS9]

_afirm, _ruins9 = 0, 0
for _rel9 in _ALVOS9:
    _basen = os.path.basename(_rel9)
    _peca_arq = int(_basen[:2]) if re.match(r'^\d\d-', _basen) else None
    for _i9, _l9 in enumerate(open(os.path.join(RAIZ, _rel9), encoding='utf-8'), 1):
        # `>` e' historia, e essa e' a convencao declarada na v0.81. Item RISCADO
        # NAO e' pulado aqui de proposito: `~~` fecha a pendencia, e nao a frase
        # ao lado dela — e foi justamente numa linha riscada que a v0.100 achou o
        # conferir-equipamento publicado como dez tendo onze.
        if _l9.lstrip().startswith('>'):
            continue
        _sl9 = _l9.lower()
        if _RX_NAO9.search(re.sub(r'[áàâãéêíóôõúç]', lambda m: 'aaaaeeiooouc'[
                'áàâãéêíóôõúç'.index(m.group(0))], _sl9)):
            continue
        for _m9 in _RX_QTD.finditer(_l9):
            _t9 = _m9.group(1).replace('*', '').strip().lower()
            _q9 = int(_t9) if _t9.isdigit() else _NUM9.get(
                re.sub(r'[áàâãéêíóôõúç]', lambda m: 'aaaaeeiooouc'[
                    'áàâãéêíóôõúç'.index(m.group(0))], _t9))
            if _q9 is None:
                continue
            _alvo9 = None
            _mp9 = _RX_PECA9.search(_l9)
            if _mp9 and int(_mp9.group(1)) in _DONO_PECA9:
                _alvo9 = _DONO_PECA9[int(_mp9.group(1))]
            if not _alvo9:
                _mv9 = _RX_VAL9.search(_l9)
                if _mv9 and _mv9.group(1) in _VAL9:
                    _alvo9 = _mv9.group(1)
            if not _alvo9 and _peca_arq:
                _alvo9 = _DONO_PECA9.get(_peca_arq)
            if not _alvo9:
                continue
            _afirm += 1
            _real9 = len(_VAL9[_alvo9])
            if _q9 != _real9:
                _ruins9 += 1
                erro(f'9: {_rel9}:{_i9} diz que o {_alvo9} tem {_q9} checagens, e o '
                     f'codigo tem {_real9}\n       {_l9.strip()[:90]}')

# guarda 3: se o extrator de afirmacao parar de casar, ele fica verde de graca
_PISO9 = 10
if _afirm < _PISO9:
    erro(f'9: so achei {_afirm} afirmacao(oes) de contagem e o piso e {_PISO9} — a '
         f'forma como os documentos escrevem isso mudou, e esta checagem parou de conferir')

print(f'  {len(_VAL9)} validadores, {sum(len(n) for n in _VAL9.values())} checagens no total.')
if not _mudos and not _furados:
    print('  [x] todo validador tem bloco numerado, e nenhuma numeracao tem buraco')
if not _ruins9:
    print(f'  [x] as {_afirm} afirmacoes de contagem batem com o codigo')
print()
print('  O DONO AQUI E O CODIGO, e e a unica checagem do projeto em que ele e.')
print('  Uma checagem = um bloco numerado. Sub-bloco conta para o bloco pai.')


# --------------------------------------------------------------------------
print()
print('=' * 88)
if FALHAS:
    print(f'>>> {len(FALHAS)} PROBLEMA(S):')
    for e in FALHAS:
        print('   -', e)
    sys.exit(1)
if PULADAS:
    print(f'>>> OK, mas {len(PULADAS)} checagem(ns) PULARAM:')
    for p in PULADAS:
        print('   -', p)
    print('    O que pulou NAO foi conferido. Um verde que pulou checagem nao e um verde.')
else:
    print('>>> TUDO OK — a arvore esta inteira, toda referencia resolve, nada aponta')
    print('    para a estrutura antiga, todo numero de dois donos bate com o dono, e o')
    print('    recorte da entrega confere com a fonte.')
if AVISOS:
    print(f'    {len(AVISOS)} aviso(s) acima, que nao falham.')

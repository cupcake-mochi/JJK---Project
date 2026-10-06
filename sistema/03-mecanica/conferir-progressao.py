#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Confere a peca 18 — a tabela de progressao — contra os donos de cada coluna.

Esta peca e' uma COPIA de proposito: ela junta num lugar so' o que se ganha em
cada nivel, e cada coluna tem dono em outro documento. A licao no 9 admite copia
com duas condicoes — dono declarado e validador em cima —, e este arquivo e' a
segunda.

NENHUM VALOR DA TABELA ESTA ESCRITO AQUI. As nove colunas sao reconstruidas
lendo os donos, e comparadas linha a linha. Se um dono mudar de forma, a
extracao falha ALTO em vez de conferir menos em silencio.

A decima coluna — o tamanho da lista de feiticos — nao tem outro dono: ela
NASCEU na peca 18, porque o manual devolveu essa contagem na v7.7 e ninguem
pegou. Ate a v0.99 a formula vivia escrita a mao dentro do conferir-aptidoes.py
e do conferir-expansao.py, que e' exatamente o que a regra do projeto proibe.
Os dois passam a ler a coluna daqui.

Desde a v0.337 o dono das colunas de Classe, Talento e Classe 0 e' o livro
reconstruido (capitulo de Progressao), lido pelo livro.py. O manual do Fundamento
v7 (.docx) foi para o arquivo, e este validador nao precisa mais do python-docx.
"""

import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))
ERROS = []
_PULADAS = []


def erro(msg):
    ERROS.append(msg)
    print(f'  !! {msg}')


def bloco(t):
    print()
    print('=' * 88)
    print(t)
    print('=' * 88)


def ler(caminho):
    with open(os.path.join(RAIZ, caminho), encoding='utf-8') as fh:
        return fh.read()


PECA = 'sistema/03-mecanica/18-progressao.md'
P01 = 'sistema/03-mecanica/01-atributos-acerto-defesa.md'
P02 = 'sistema/03-mecanica/02-economia-de-atributos.md'
P11 = 'sistema/03-mecanica/11-aptidoes-e-refino.md'
P12 = 'sistema/03-mecanica/12-experiencia-e-progressao.md'
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import livro


# --------------------------------------------------------------------------
bloco('1. A TABELA DA PECA — ela existe, tem 30 linhas e nao tem buraco?')
# --------------------------------------------------------------------------
# A extracao le a tabela de nove colunas. Se a peca ganhar outra tabela de nove
# colunas um dia, a guarda de contagem acusa em vez de misturar as duas.

COLS = ['nível', 'XP', 'maestria', 'espaços', 'refino', 'Classe', 'Talento',
        'Classe 0', 'o que acontece']

_txt = ler(PECA)
_linhas = [l.strip() for l in _txt.split('\n') if l.strip().startswith('|')]
_cab = [l for l in _linhas if all(c in l for c in COLS)]
if len(_cab) != 1:
    erro(f'esperava UM cabecalho de tabela com as colunas {COLS} na peca 18 e achei '
         f'{len(_cab)} — a peca mudou de forma e este validador parou de conferir')
    print('\n'.join(f'   - {e}' for e in ERROS))
    sys.exit(1)

_i = _linhas.index(_cab[0])
TABELA = {}
for l in _linhas[_i + 2:]:
    cel = [c.strip() for c in l.strip('|').split('|')]
    if len(cel) != 9:
        break
    nv = cel[0].strip('*')
    if not nv.isdigit():
        break
    TABELA[int(nv)] = cel

print(f'  {len(TABELA)} linhas lidas da tabela da peca 18.')
if sorted(TABELA) != list(range(1, 31)):
    erro(f'a tabela deveria ir do nivel 1 ao 30 e vai de {min(TABELA)} a {max(TABELA)} '
         f'com {len(TABELA)} linhas')
else:
    print('  [x] do nivel 1 ao 30, sem buraco e sem repeticao.')


def _num(nv, col):
    """Le uma celula numerica da tabela, sem negrito e sem separador de milhar."""
    return TABELA[nv][COLS.index(col)].replace('*', '').replace('.', '').strip()


def compara(rotulo, coluna, esperado_de):
    """esperado_de(nv) devolve str ou None (None = nao confere esta linha)."""
    fora = []
    conferidas = 0
    for nv in sorted(TABELA):
        esp = esperado_de(nv)
        if esp is None:
            continue
        conferidas += 1
        if _num(nv, coluna) != str(esp):
            fora.append(f'nv{nv}: a peca diz "{_num(nv, coluna)}" e o dono diz "{esp}"')
    if fora:
        erro(f'{rotulo}: {len(fora)} linha(s) fora — ' + '; '.join(fora[:6]))
    elif conferidas == 0:
        erro(f'{rotulo}: nenhuma linha foi conferida — a extracao do dono devolveu '
             f'vazio e esta checagem virou trivialmente verdadeira')
    else:
        print(f'  [x] {rotulo}: as {conferidas} linhas batem com o dono')


# --------------------------------------------------------------------------
bloco('2. XP — dono: a peca 12, secao 3')
# --------------------------------------------------------------------------
# Formato do dono:  | **2 a 4** | 1 missão | 100 |   e a ultima faixa e' | **29** |
FAIXAS = []
for m in re.finditer(r'^\| \*\*(\d+)(?: a (\d+))?\*\* \| [^|]+ \| ([\d.]+) \|', ler(P12), re.M):
    ini, fim, xp = int(m.group(1)), m.group(2), m.group(3).replace('.', '')
    FAIXAS.append((ini, int(fim) if fim else ini, int(xp)))
print(f'  {len(FAIXAS)} faixas de XP lidas da peca 12.')
# v0.196: a guarda era "pelo menos 10 faixas", e ela envelheceu no dia em que a
# curva foi represada — de 13 faixas para 9, sem nada de errado ter acontecido.
# Contar faixa e' contar a FORMA da tabela; o que esta checagem precisa garantir e'
# que a extracao COBRE todo nivel que ela vai conferir. Cobertura nao muda quando
# o Mizuki decide agrupar os niveis de outro jeito.
_cobertos = {n for ini, fim, _ in FAIXAS for n in range(ini, fim + 1)}
_faltam = sorted(set(range(2, 30)) - _cobertos)
if _faltam:
    erro(f'a extracao das faixas de XP da peca 12 nao cobre o(s) nivel(is) {_faltam} — '
         f'a tabela mudou de forma e esta checagem pararia de conferir essas linhas')
elif len(_cobertos - set(range(2, 30))) > 0:
    erro(f'a extracao pegou nivel fora do intervalo 2-29: '
         f'{sorted(_cobertos - set(range(2, 30)))}')
else:
    print(f'  [x] as faixas cobrem os niveis 2 a 29 sem buraco.')


def xp_de(nv):
    if nv == 30:
        return '—'
    for ini, fim, v in FAIXAS:
        if ini <= nv <= fim:
            return v
    return None    # o nivel 1 nao tem custo publicado


compara('XP', 'XP', xp_de)


# --------------------------------------------------------------------------
bloco('3. MAESTRIA — dono: a peca 1, secao 2')
# --------------------------------------------------------------------------
# Formato do dono, duas linhas:
#   | nível | 2–9 | 10–17 | 18–25 | 26–30 |
#   | maestria | 1 | 2 | 3 | 4 |
_p1 = ler(P01)
_mn = re.search(r'^\| nível \|((?: [\d–\-]+ \|)+)$', _p1, re.M)
_mv = re.search(r'^\| maestria \|((?: \d+ \|)+)$', _p1, re.M)
MAESTRIA = []
if not _mn or not _mv:
    erro('nao achei as duas linhas da tabela de maestria na peca 1 secao 2 — ela mudou '
         'de forma e esta checagem parou de conferir')
else:
    faixas = [c.strip() for c in _mn.group(1).strip().strip('|').split('|')]
    vals = [c.strip() for c in _mv.group(1).strip().strip('|').split('|')]
    if len(faixas) != len(vals):
        erro(f'a tabela de maestria tem {len(faixas)} faixas e {len(vals)} valores')
    for f, v in zip(faixas, vals):
        a, _, b = f.replace('–', '-').partition('-')
        MAESTRIA.append((int(a), int(b or a), int(v)))
    print(f'  {len(MAESTRIA)} degraus de maestria lidos da peca 1: '
          + ' · '.join(f'{a}-{b}={v}' for a, b, v in MAESTRIA))
    if len(MAESTRIA) != 4:
        erro(f'a maestria deveria ter 4 degraus e li {len(MAESTRIA)}')


def maestria_de(nv):
    for a, b, v in MAESTRIA:
        if a <= nv <= b:
            return v
    return MAESTRIA[0][2] if MAESTRIA and nv < MAESTRIA[0][0] else None


compara('maestria', 'maestria', maestria_de)


# --------------------------------------------------------------------------
bloco('4. MARCO E REFINO — dono: a peca 11, secao 3')
# --------------------------------------------------------------------------
_p11 = ler(P11)
_mm = re.search(r'A cada quatro níveis — \*\*([\d, e]+)\*\*', _p11)
MARCOS = []
if not _mm:
    erro('nao achei o calendario de marcos na peca 11 secao 3 — ela mudou de forma e '
         'esta checagem parou de conferir')
else:
    MARCOS = [int(x) for x in re.findall(r'\d+', _mm.group(1))]
    print(f'  marcos lidos da peca 11: {MARCOS}')
    if len(MARCOS) != 7:
        erro(f'o projeto tem 7 marcos e li {len(MARCOS)} na peca 11')

# o refino da tabela e' a LINHA PASSIVA: 1 no comeco, mais um por marco.
# O valor de partida vem da propria peca 11, que diz "mais o refino 1 do começo".
_r0 = re.search(r'mais o refino (\d+) com que toda ficha começa', _p11)
if not _r0:
    erro('nao achei na peca 11 a frase que diz com quanto refino a ficha comeca — '
         'ela mudou de forma e esta checagem parou de conferir')
REFINO_INICIAL = int(_r0.group(1)) if _r0 else None


def refino_de(nv):
    if REFINO_INICIAL is None or not MARCOS:
        return None
    return REFINO_INICIAL + sum(1 for m in MARCOS if nv >= m)


compara('refino (linha passiva)', 'refino', refino_de)

# a coluna "o que acontece" tem de marcar MARCO exatamente nos sete niveis
_marcados = sorted(nv for nv in TABELA if '**marco**' in TABELA[nv][8])
if MARCOS and _marcados != sorted(MARCOS):
    erro(f'a coluna "o que acontece" marca marco em {_marcados} e a peca 11 diz {MARCOS}')
elif MARCOS:
    print(f'  [x] os 7 marcos estao marcados na coluna de eventos, e so eles')


# --------------------------------------------------------------------------
bloco('5. ESPACOS DE FEITICO — dono: a propria peca 18, secao 4')
# --------------------------------------------------------------------------
# Esta e' a unica coluna que nasce na peca. A checagem faz duas coisas: confere
# que a coluna segue a formula que a secao 4 publica, e confere a formula contra
# a tabela da peca 11 que a usa — que e' quem acusaria se ela mudasse sozinha.
_f = re.search(r'Espaços de feitiço conhecido = `(\d+) \+ nível ÷ (\d+)`.*?'
               r'mais `(\d+)` por marco', _txt, re.S)
if not _f:
    erro('nao achei na secao 4 da peca 18 a linha que publica a formula dos espacos — '
         'ela mudou de forma e esta checagem parou de conferir')
else:
    BASE, DIV, PORMARCO = (int(_f.group(i)) for i in (1, 2, 3))
    print(f'  formula lida da peca 18: {BASE} + nivel/{DIV}, mais {PORMARCO} por marco.')

    def espacos_de(nv):
        if not MARCOS:
            return None
        return BASE + nv // DIV + PORMARCO * sum(1 for m in MARCOS if nv >= m)

    compara('espaços', 'espaços', espacos_de)

    # --- a regressao: a peca 11 usa esta formula, e publica quatro valores dela.
    # Formato do dono:  | só feitiço | 12 | 16 | 21 | 24 |
    # com o cabecalho   | montagem | nv14 | nv20 | nv26 | nv30 |
    _cab11 = re.search(r'^\| montagem \|((?: nv\d+ \|)+)$', _p11, re.M)
    _lin11 = re.search(r'^\| só feitiço \|((?: \*?\*?\d+\*?\*? \|)+)$', _p11, re.M)
    if not _cab11 or not _lin11:
        erro('nao achei na peca 11 a tabela de espacos por montagem — ela mudou de '
             'forma e a regressao dos espacos parou de rodar')
    else:
        nvs = [int(x) for x in re.findall(r'\d+', _cab11.group(1))]
        vals = [int(x) for x in re.findall(r'\d+', _lin11.group(1))]
        if len(nvs) != len(vals) or len(nvs) < 4:
            erro(f'a tabela de espacos da peca 11 tem {len(nvs)} niveis e {len(vals)} '
                 f'valores — ela mudou de forma')
        else:
            ruim = [(n, v, espacos_de(n)) for n, v in zip(nvs, vals) if espacos_de(n) != v]
            if ruim:
                erro('a formula dos espacos nao reproduz a tabela da peca 11: '
                     + '; '.join(f'nv{n}: ela diz {v}, a formula da {c}' for n, v, c in ruim))
            else:
                print(f'  [x] regressao: a formula reproduz os {len(nvs)} valores que a '
                      f'peca 11 publica ({", ".join(f"nv{n}={v}" for n, v in zip(nvs, vals))})')


# --------------------------------------------------------------------------
bloco('6. CAMINHO E TRILHA — dono: a colecao v0.4, em caminhos/')
# --------------------------------------------------------------------------
# v0.270: o dono do calendario mudou. Ate a v0.269 ele era a linha de orcamento
# do topo do DESENHO-caminhos.md, com o Caminho em quatro degraus (2, 7, 15, 30).
# A colecao v0.4 dos Caminhos, que o Mizuki mandou pôr no livro "exatamente" como
# ela e', deu aos quatro Caminhos um degrau no nivel 23, e ela passou a ser a dona
# do texto dos quatro — o DESENHO ficou como o registro com preco da colecao
# anterior. O calendario e' lido daqui, dos quadros de nivel dos seis arquivos,
# e os quatro tem de concordar entre si: se um Caminho ganhar um degrau que os
# outros nao tem, a tabela da peca 18 nao tem como dizer "degrau de Caminho".
#
# Nenhum numero mora aqui. O Caminho sai do PRIMEIRO quadro de nivel de cada
# arquivo (o do Caminho base), e a Trilha sai dos titulos `### Nivel N` de cada
# secao `## Trilha`, rota do Batedor incluida.
import glob as _glob
_V04 = os.path.join(RAIZ, 'caminhos', '05-Edicao-Integrada')
_cams, _tris = [], []
for _a in sorted(_glob.glob(os.path.join(_V04, '*-Caminho-e-Trilhas.md'))):
    _txt6 = open(_a, encoding='utf-8').read()
    _blocos = re.split(r'\n(?=### Trilha: )', _txt6)
    _mq = re.search(r'^\| (?:\*\*)?Nível(?:\*\*)? \|[^\n]*\n\|[- |]+\|\n((?:\|[^\n]*\n)+)', _blocos[0], re.M)
    _cams.append((os.path.basename(_a),
                  [int(x) for x in re.findall(r'^\| (\d+) \|', _mq.group(1), re.M)] if _mq else []))
    _reais6 = sorted({int(x) for x in re.findall(r'^(?:> \*\*)?(?:#{3,4} )?Nível (\d+)', _blocos[0], re.M)})
    if sorted(_cams[-1][1]) != _reais6:
        erro(f'{os.path.basename(_a)}: calendario da tabela {_cams[-1][1]} diverge das habilidades {_reais6}')
    for _b in _blocos[1:]:
        _tris.append((_b.split('\n')[0].replace('### Trilha: ', ''),
                      sorted({int(x) for x in re.findall(r'^(?:> \*\*)?(?:#{3,4} )?Nível (\d+)', _b, re.M)})))
_cal_cam = {tuple(n) for _, n in _cams}
_cal_tri = {tuple(n) for _, n in _tris}
if len(_cams) != 6 or len(_tris) != 18:
    erro(f'esperava os seis arquivos da colecao v0.4 e dezoito Trilhas, li {len(_cams)} e '
         f'{len(_tris)} — a pasta caminhos/ mudou e esta checagem parou de conferir')
elif len(_cal_cam) != 1 or not next(iter(_cal_cam)):
    erro(f'os seis Caminhos da v0.331 nao concordam no calendario: {_cams}')
elif len(_cal_tri) != 1 or not next(iter(_cal_tri)):
    erro(f'as dezoito Trilhas da v0.4 nao concordam no calendario: {_tris}')
else:
    CAMINHO = list(next(iter(_cal_cam)))
    TRILHA = list(next(iter(_cal_tri)))
    print(f'  Caminho em {CAMINHO} · Trilha em {TRILHA}  (os seis arquivos e as dezoito Trilhas concordam)')
    for rotulo, calendario, marca in (('Caminho', CAMINHO, 'degrau de **Caminho**'),
                                      ('Trilha', TRILHA, 'entrega de **Trilha**')):
        na_peca = sorted(nv for nv in TABELA if marca in TABELA[nv][8])
        if na_peca != sorted(calendario):
            erro(f'a coluna de eventos marca {rotulo} em {na_peca} e o dono diz {calendario}')
        else:
            print(f'  [x] {rotulo}: os {len(calendario)} niveis batem com o dono')


# --------------------------------------------------------------------------
bloco('7. CLASSE, TALENTO E CLASSE 0 — dono: o livro, capitulo de Progressao')
# --------------------------------------------------------------------------
# v0.337: ate a v0.336 o dono era a secao 9 do manual do Fundamento v7 (.docx), lida
# por frase ("Classe 2.", "libera Talento de Classe 2"). O .docx foi para o arquivo
# no passo 5 da migracao, e o livro reconstruido publica as tres colunas como coluna.
# As guardas de forma continuam: sete Classes, tres Categorias, tres ganhos de
# Classe 0 — se a extracao devolver outra coisa, o livro mudou de forma.
try:
    _prog = livro.texto('progressao')
    _lin = livro.tabelas_com(_prog, 'Nível', 'Classe máxima', 'Categoria de Efeito', 'Classe 0')
    LIVRO = {int(r['Nível']): r for r in _lin}
except (livro.LivroMudou, KeyError, ValueError, OSError) as e:
    LIVRO = None
    erro(f'7: nao consegui ler a tabela de Progressao do livro — {type(e).__name__}: {e}')

if LIVRO is not None:
    print(f'  {len(LIVRO)} niveis lidos do livro: {min(LIVRO)} a {max(LIVRO)}')
    if sorted(LIVRO) != list(range(1, 31)):
        erro(f'7: a tabela do livro deveria ir do 1 ao 30, sem buraco, e tem {sorted(LIVRO)}')
    else:
        _cl = sorted({int(r['Classe máxima']) for r in LIVRO.values()})
        _ce = sorted({int(r['Categoria de Efeito']) for r in LIVRO.values()})
        _c0 = [nv for nv in range(2, 31)
               if int(LIVRO[nv]['Classe 0']) > int(LIVRO[nv - 1]['Classe 0'])]
        print(f'  Classe maxima: {_cl} · Categoria de Efeito: {_ce} · Classe 0 sobe em {_c0}')
        if _cl != list(range(1, 8)):
            erro(f'7: o livro deveria abrir as Classes 1 a 7 e eu li {_cl}')
        if _ce != [1, 2, 3]:
            erro(f'7: o livro deveria abrir as Categorias de Efeito 1 a 3 e eu li {_ce}')
        if len(_c0) != 3:
            erro(f'7: esperava 3 niveis que dao Classe 0 a mais e li {len(_c0)}')

        for rotulo, col_peca, col_livro in (('Classe de feitiço', 'Classe', 'Classe máxima'),
                                            ('Categoria de Efeito de Talento', 'Talento', 'Categoria de Efeito'),
                                            ('Classe 0', 'Classe 0', 'Classe 0'),
                                            ('maestria', 'maestria', 'Maestria'),
                                            ('espaços', 'espaços', 'Espaços'),
                                            ('refino', 'refino', 'Refino básico')):
            compara(f'{rotulo} (livro)', col_peca, lambda nv, c=col_livro: LIVRO[nv][c])

    # os eventos que so o livro escreve: a prosa embaixo de cada metade da tabela
    _prosa = re.sub(r'\*', '', _prog)
    _lm1 = re.search(r'A primeira Liberação Máxima chega no (\d+)', _prosa)
    _tm = re.search(r'A Técnica Máxima chega no (\d+); as outras Liberações Máximas, no (\d+) e no (\d+)', _prosa)
    if not _lm1 or not _tm:
        erro('7: o livro parou de dizer em que nivel chegam a Tecnica Maxima e as '
             'Liberacoes Maximas — ele mudou de forma e esta checagem parou de conferir')
    else:
        for frase, marca, do_livro in (
                ('Liberação Máxima', 'Liberação Máxima',
                 sorted([int(_lm1.group(1)), int(_tm.group(2)), int(_tm.group(3))])),
                ('Técnica Máxima', '**Técnica Máxima**', [int(_tm.group(1))])):
            na_peca = sorted(nv for nv in TABELA if marca in TABELA[nv][8])
            if do_livro != na_peca:
                erro(f'{frase}: o livro diz {do_livro} e a peca 18 marca {na_peca}')
            else:
                print(f'  [x] {frase}: {do_livro} — bate com o livro')


# --------------------------------------------------------------------------
bloco('8. A TABELA DE TRES FICHAS DA PECA 2 — ela e copia, e ja saiu errada')
# --------------------------------------------------------------------------
# Nasceu na v0.99. A peca 2 secao 3 publica uma tabela de tres rotas com refino e
# aptidoes no nv14, nv22 e nv30, e ela NAO tinha validador nenhum: a linha de
# quem sempre escolhe Refino ficou nove versoes com os numeros de antes da v0.89,
# dizendo 5 aptidoes no nivel 22 e 7 no 30 quando sao 6 e 10.
#
# A regra da v0.89 mora na peca 11 secao 3 e e' lida de la, nao escrita aqui.
_teto = re.search(r'Teto do atributo: (\d+)\.\*?\*? Teto do refino: (\d+)', ler(P02))
_dobra = re.search(r'no teto, a escolha de Refino leva \*?\*?DUAS\*?\*? aptidões', _p11)
if not _teto:
    erro('8: nao achei os tetos de atributo e refino na peca 2 — ela mudou de forma')
elif not _dobra:
    erro('8: nao achei na peca 11 a decisao da v0.89 sobre a escolha no teto — ela '
         'mudou de forma e esta checagem parou de conferir')
elif not MARCOS or REFINO_INICIAL is None:
    erro('8: sem os marcos ou o refino inicial da peca 11 nao da para rodar a rota')
else:
    TETO_REFINO = int(_teto.group(2))
    ref, apt = REFINO_INICIAL, 0
    curva = {}
    for m in MARCOS:
        ref = min(TETO_REFINO, ref + 1)          # a linha passiva
        if ref < TETO_REFINO:
            ref += 1
            apt += 1
        else:
            apt += 2                              # a decisao da v0.89
        curva[m] = (ref, apt)
    print(f'  rota "sempre refino", rodada com a regra da peca 11 (teto {TETO_REFINO}):')
    print('   ' + ' · '.join(f'nv{m}: ref {r}, {a} apt' for m, (r, a) in curva.items()))

    _lin2 = re.search(r'^\| \*\*sempre refino\*\* \|(.+)\|$', ler(P02), re.M)
    if not _lin2:
        erro('8: nao achei a linha "sempre refino" na tabela da peca 2 secao 3 — ela '
             'mudou de forma e esta checagem parou de conferir')
    else:
        cels = [c.strip() for c in _lin2.group(1).split('|')]
        alvos = [14, 22, 30]
        if len(cels) != len(alvos):
            erro(f'8: a linha "sempre refino" tem {len(cels)} celulas e eu esperava '
                 f'{len(alvos)} (nv14, nv22, nv30)')
        else:
            for nv, cel in zip(alvos, cels):
                mr = re.search(r'ref (\d+)', cel)
                ma = re.search(r'(\d+) apt', cel)
                if not mr or not ma:
                    erro(f'8: nao consegui ler refino e aptidoes da celula de nv{nv}: '
                         f'"{cel}"')
                    continue
                r, a = curva[nv]
                if (int(mr.group(1)), int(ma.group(1))) != (r, a):
                    erro(f'8: a peca 2 diz nv{nv} com ref {mr.group(1)} e '
                         f'{ma.group(1)} aptidoes; a regra da peca 11 da ref {r} e {a}')
            if not any(m.startswith('8:') for m in ERROS):
                print('  [x] a linha "sempre refino" da peca 2 bate com a regra da peca 11')


# --------------------------------------------------------------------------
print()
print('=' * 88)
if ERROS:
    print(f'>>> {len(ERROS)} PROBLEMA(S):')
    for e in ERROS:
        print('   -', e)
    sys.exit(1)
if _PULADAS:
    print(f'>>> OK, mas {len(_PULADAS)} checagem(ns) PULARAM:')
    for p in _PULADAS:
        print('   -', p)
    print('    O que pulou NAO foi conferido.')
else:
    print('>>> TUDO OK — as nove colunas da tabela de progressao reconstroem a partir')
    print('    dos donos, a formula dos espacos reproduz a tabela da peca 11, e a copia')
    print('    de tres fichas da peca 2 bate com a regra do marco.')

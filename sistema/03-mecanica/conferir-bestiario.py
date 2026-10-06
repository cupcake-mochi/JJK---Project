#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Confere a peca 26 — o Bestiario na GRADE — contra os donos de cada numero.

v0.282, a fase 2 do bestiario. A categoria deixou de medir quantas pessoas o
inimigo exige e passou a ser a DIFICULDADE da luta, feita para N pessoas do nivel
(x1 a x6). A vida e rodadas x N x a saida de um personagem; o golpe e a pressao do
degrau x o golpe-base; o inimigo age N vezes; e o que ele carrega se paga na vida.
O validador da escada (v0.198 a v0.281) esta no historico do git; a peca daquela
escada, no arquivo morto.

NENHUM VALOR DE REGRA ESTA ESCRITO AQUI. A tabela de inimigo vem do manual, as
formulas da peca 1, a curva de refino da peca 11, a regua de condicao da peca 19,
o orcamento do Pathfinder 2e das notas da pesquisa e da propria peca, e as rodadas
da propria peca (decisao do Mizuki, 28/09/2026). A checagem 7 guarda essa promessa.

As checagens 3, 5 e 9 leem a tabela `Inimigos` do gerador do manual (partF.js),
de onde o .docx saia; desde a v0.337 o .docx nao e' lido. Se a tabela nao for
lida, elas PULAM e o rodape DIZ que pularam — e a leitura falha alto antes.

As checagens, na ordem:
  1   as ancoras da ficha, nos dois sentidos
  2   a tabela por nivel do §3.1 contra as formulas da peca 1; 2.1 o orcamento de
      atributo; 2.2 a troca do §3.2 (o desvio da tabela se paga na vida)
  3   a grade: os degraus, a pressao, a porta da Intervencao e as fichas prontas do
      §4.1 contra a tabela do manual; 3.3 o tamanho
  4   as acoes = N, e a regra do x1 e do x2 contra a regua da peca 19 §2.2;
      4.3 N corpos de x1; 4.4 o dado; 4.6 concentrando
  5   o Capanga: o esquadrao de 2N, a coluna do manual, o cambio e o chefe com
      capangas, pela simulacao; 5.2 a linha do manual e a regra das tres vezes
  6   o grau nao vira numero; 7 nenhum valor guardado aqui
  7.1 a Expansao divide a vida por 1,92, e os gates
  8   a resistencia divide a vida crua
  9   o catalogo do jogador: 9.1 o orcamento de feitico, 9.2 a aptidao, 9.3 as
      trocas ruins, 9.4 as portas, 9.5 as prontas, 9.6 a area natural, 9.7 a
      Recarga, 9.8 a corrente, 9.9 a parte destrutivel, 9.10 a Intervencao
  10  o papel: o Artilheiro por degrau, os de acao por N, e os dois da troca;
      10.1 o Emboscador ate Grande e o Reforco com companhia, na peca e no livro
  11  a ficha derivada do Sukuna contra o gerador da grade e os donos vigentes
"""

import math
import os
import subprocess
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))
ERROS = []
_PULADAS = []


def erro(msg):
    ERROS.append(msg)
    print(f'  !! {msg}')


def pulou(msg):
    _PULADAS.append(msg)
    print(f'  ~~ PULADA: {msg}')


def bloco(t):
    print()
    print('=' * 88)
    print(t)
    print('=' * 88)


def ler(caminho):
    with open(os.path.join(RAIZ, caminho), encoding='utf-8') as fh:
        return fh.read()


PECA = 'sistema/03-mecanica/26-bestiario.md'
P01 = 'sistema/03-mecanica/01-atributos-acerto-defesa.md'
P02 = 'sistema/03-mecanica/02-economia-de-atributos.md'
P03 = 'sistema/03-mecanica/03-economia-de-acao-e-iniciativa.md'
P05 = 'sistema/03-mecanica/05-caminho-e-combate-sem-feitico.md'
P07 = 'sistema/03-mecanica/07-pericias-e-oficios.md'
P11 = 'sistema/03-mecanica/11-aptidoes-e-refino.md'
P12 = 'sistema/03-mecanica/12-experiencia-e-progressao.md'
P18 = 'sistema/03-mecanica/18-progressao.md'
P19 = 'sistema/03-mecanica/19-dano-e-condicoes.md'
P22 = 'sistema/03-mecanica/22-pactos.md'
P24 = 'sistema/03-mecanica/24-dano-de-alma.md'
NOTAS = 'bestiario/09-fase-2/pesquisa/NOTAS-pesquisa-externa.md'
CAPANGA_DONO = 'bestiario/04-fase-1/fila/DECIDIDO-o-capanga.md'
PARTF = 'manual/gerador/partF.js'

TXT = ler(PECA)
_NUM_PT = {'um': 1, 'uma': 1, 'dois': 2, 'duas': 2, 'três': 3, 'quatro': 4, 'cinco': 5,
           'seis': 6, 'sete': 7, 'oito': 8, 'nove': 9, 'dez': 10}


def celulas(linha):
    return [c.replace('*', '').replace('`', '').strip() for c in linha.split('|')[1:-1]]


def tabela(texto, cabecalho):
    """As linhas de dado da primeira tabela que comeca com `cabecalho` (o `> ` sai antes)."""
    i = texto.find(cabecalho)
    if i < 0:
        return []
    t = texto[i:]
    t = t[:t.find('\n\n')] if '\n\n' in t else t
    linhas = [re.sub(r'^>\s*', '', l) for l in t.split('\n')[1:]]
    return [celulas(l) for l in linhas if l.startswith('|') and not l.startswith('|---')]


def _meio_baixo(x):
    """a regra do §4.1: meio para BAIXO, e so o meio exato — o resto arredonda normal"""
    return math.ceil(x - 0.5) if abs(x % 1 - 0.5) < 1e-9 else round(x)


def _f(s):
    return float(s.replace(',', '.'))


def _faixa_num(cel):
    """'`2,18×` a `2,43×`' -> (2.18, 2.43)"""
    xs = [_f(x) for x in re.findall(r'([\d]+,[\d]+)', cel)]
    return (xs[0], xs[-1]) if xs else None


# --------------------------------------------------------------------------
bloco('1. AS ANCORAS — cada linha da ficha aparece no dono dela')
# --------------------------------------------------------------------------
# A ficha e a tabela `linha | valor | dono` do §3. Este dicionario diz, para cada
# linha, o arquivo dono e um padrao que tem de casar la; a 1.1 compara as duas
# listas nos DOIS sentidos. Nenhum padrao carrega o VALOR que ele confere.
ANCORAS = {
    'nivel': (P12, r'[Nn]ível'),
    'categoria': (PECA, r'\*\*`Desastre`\*\*'),
    'n': (PECA, r'de `×1` a `×6`'),
    'vida': (PECA, r'A vida é `rodadas × N × a saída de um personagem`'),
    'integridade': (P24, r'Integridade de quem não é personagem jogador = '),
    'golpe': (PECA, r'O golpe é `a pressão × o golpe-base`'),
    'acoes': (PECA, r'Ele age `N` vezes por rodada'),
    'defesa': (P01, r'10 \+ Destreza \+ prote'),
    'acerto': (P01, r'atributo.{0,20}maestria'),
    'cd': (P01, r'8 \+ atributo'),
    'reacao': (PECA, r'volta no começo do turno dele'),
    'refino': (P11, r'\*\*meio a meio\*\*'),
    'tr': (P07, r'[Tt]este de Resistência'),
    'deslocamento': (P03, r'9 m'),
    'atributos': (P02, r'[Nn]ove pontos em cinco atributos'),
    'caracteristicas': (P11, r'catálogo de aptidões'),
    'pacto': (P22, r'metade da Essência'),
    'resistencia': (P19, r'\| \*\*Físicos\*\* \|'),
    'tamanho': (PECA, r'o tamanho não cobra nada'),
    'papel': (PECA, r'o que ele paga é o inverso do que ele ganha'),
}
MAPA_ANCORA = {
    'nível': ('nivel',), 'categoria': ('categoria',), 'N': ('n',), 'vida': ('vida',),
    'Integridade': ('integridade',), 'o golpe': ('golpe',),
    'ações por rodada': ('acoes',), 'Defesa': ('defesa',), 'acerto': ('acerto',),
    'CD': ('cd',), 'Reação': ('reacao',), 'refino': ('refino',),
    'Testes de Resistência': ('tr',), 'deslocamento': ('deslocamento',),
    'atributos': ('atributos',), 'características': ('caracteristicas',),
    'pacto': ('pacto',), 'resistência, vulnerabilidade e imunidade': ('resistencia',),
    'tamanho': ('tamanho',), 'papel': ('papel',),
}
_achadas = 0
for _rot, (_arq, _pad) in sorted(ANCORAS.items()):
    if re.search(_pad, ler(_arq)):
        _achadas += 1
    else:
        erro(f'1: a ancora "{_rot}" nao aparece em {_arq} — ou ela mudou de forma la, ou esta '
             'linha da ficha ficou sem chao')
print(f'  {_achadas} de {len(ANCORAS)} ancoras encontradas nos donos.')
_FICHA = [c for c in tabela(TXT, '| linha | valor | dono |') if len(c) == 3]
_rotulos = [c[0] for c in _FICHA]
_mn1 = re.search(r'\*\*(\w+) linhas\. Nenhum número novo nasce aqui\*\*', TXT)
if not _rotulos:
    erro('1.1: nao achei a tabela da ficha do §3')
else:
    _sem = [r for r in _rotulos if r not in MAPA_ANCORA]
    _sobra = [r for r in MAPA_ANCORA if r not in _rotulos]
    _reiv = {k for v in MAPA_ANCORA.values() for k in v}
    for _msg, _lista in (('linha(s) da ficha sem ancora nenhuma', _sem),
                         ('o mapa aponta para linha(s) que sairam da ficha', _sobra),
                         ('ancora(s) que nenhuma linha reivindica', sorted(set(ANCORAS) - _reiv)),
                         ('o mapa reivindica ancora(s) que nao existem', sorted(_reiv - set(ANCORAS)))):
        if _lista:
            erro(f'1.1: {_msg}: ' + ', '.join(_lista))
    _PAL1 = dict(_NUM_PT, dezenove=19, vinte=20, onze=11, doze=12)
    if not _mn1 or _PAL1.get(_mn1.group(1).lower()) != len(_rotulos):
        erro(f'1.1: a peca diz "{_mn1.group(1) if _mn1 else "?"} linhas" e a ficha tem {len(_rotulos)}')
    elif not (_sem or _sobra):
        print(f'  [x] as {len(_rotulos)} linhas da ficha e as {len(ANCORAS)} ancoras se cobrem nos dois '
              f'sentidos, e a contagem por extenso bate')


# --------------------------------------------------------------------------
bloco('2. A TABELA POR NIVEL — Defesa, acerto e CD contra as formulas da peca 1')
# --------------------------------------------------------------------------
# Desde a v0.282 a tabela do §3.1 e a DONA das tres (a ficha e propria, decisao do
# Mizuki de 28/09). As formulas da peca 1 continuam sendo a prova: a tabela tem de
# devolver, do lado do inimigo, os MESMOS numeros que a peca 1 §6 publica do lado
# do jogador.
def maestria(nv):
    return 1 + max(0, nv - 2) // 8


def investido(nv):
    return min(6, 3 + max(0, nv - 2) // 8)


_MEIO = {2: 1}
_lin = [c for c in tabela(ler(P11), '| | nv 6 | nv 10 | nv 14 | nv 18 | nv 22 | nv 26 | nv 30 |')
        if c and c[0].startswith('meio a meio')]
if not _lin or len(_lin[0]) < 8:
    erro('2: nao achei a linha do `meio a meio` na tabela de refino da peca 11 §3')
else:
    for _nv, _v in zip((6, 10, 14, 18, 22, 26, 30), _lin[0][1:8]):
        _MEIO[_nv] = int(_v)


def refino(nv):
    r = 1
    for m in (6, 10, 14, 18, 22, 26, 30):
        if nv >= m and m in _MEIO:
            r = _MEIO[m]
    return r


def protecao(ref):
    return ref // 3 + 1


def defesa(nv):
    return 10 + investido(nv) + protecao(refino(nv))


def acerto(nv):
    return investido(nv) + maestria(nv)


def cd(nv):
    return 8 + investido(nv) + maestria(nv)


def p(alvo, bonus):
    return max(0.05, min(0.95, (21 - (alvo - bonus)) / 20))


_NIVEIS = (5, 10, 15, 20, 25, 30)
_pub_der = {c[0]: c[1:] for c in tabela(TXT, '| nível do grupo | 5 | 10 | 15 | 20 | 25 | 30 |') if c}
_mau2 = 0
if not _pub_der:
    erro('2: nao achei a tabela do §3.1')
    _mau2 = 1
for _rot, _fn in (('Defesa', defesa), ('acerto', acerto), ('CD', cd), ('refino', refino)):
    if _rot not in _pub_der:
        if _pub_der:
            erro(f'2: a tabela do §3.1 nao publica a linha "{_rot}"')
            _mau2 += 1
        continue
    for _nv, _v in zip(_NIVEIS, _pub_der[_rot]):
        if int(_v.lstrip('+')) != _fn(_nv):
            erro(f'2: no nivel {_nv} a peca publica {_rot} {_v} e a formula da peca 1 da {_fn(_nv)}')
            _mau2 += 1
if not _mau2:
    print('  [x] as quatro linhas do §3.1 reconstroem das formulas dos donos')
_acertos = sorted({round(p(defesa(nv), acerto(nv)) * 100) for nv in _NIVEIS})
_falhas = sorted({round((1 - p(cd(nv), acerto(nv))) * 100) for nv in _NIVEIS})
_t01 = ler(P01)
_m01 = re.search(r'\|\s*\*\*treinado\*\*\s*\|((?:\s*\*{0,2}\d+%\*{0,2}\s*\|)+)', _t01)
_mb31 = re.search(r'ele acerta `(\d+)%` a `(\d+)%`, e o Teste de Resistência treinado dele falha `(\d+)%`', TXT)
if not (_m01 and _mb31):
    erro('2: faltou a linha do TR treinado da peca 1 §6 ou a frase do §3.1')
else:
    _res = sorted({int(x) for x in re.findall(r'(\d+)%', _m01.group(1))})
    if set(_falhas) != {100 - r for r in _res}:
        erro(f'2: a CD da tabela faz o TR treinado falhar {_falhas}%, e a peca 1 §6 publica {_res}%')
    elif (int(_mb31.group(1)), int(_mb31.group(2)), int(_mb31.group(3))) != (_acertos[0], _acertos[-1], _falhas[0]):
        erro(f'2: o §3.1 diz {_mb31.group(1)}% a {_mb31.group(2)}% e {_mb31.group(3)}%, e a conta da '
             f'{_acertos[0]}% a {_acertos[-1]}% e {_falhas}')
    else:
        print(f'  [x] ele acerta o alvo dificil em {_acertos[0]}% a {_acertos[-1]}%, e o TR treinado dele '
              f'falha {_falhas[0]}% — os numeros da peca 1 §6 do outro lado da rolagem')


# --------------------------------------------------------------------------
bloco('2.1 O ORCAMENTO DE ATRIBUTO — nove na criacao, e o marco no ritmo do meio a meio')
# --------------------------------------------------------------------------
_P02 = ler(P02); _P11 = ler(P11)
_nove = re.search(r'([Nn]ove) pontos em cinco atributos', _P02)
_p26 = re.search(r'O inimigo monta os cinco com (\w+) pontos na criação, teto `(\d+)` ali, e teto `(\d+)`', TXT)
_marc = re.search(r'\| \| nv 6 \|[^\n]*', _P11)
_mm = re.search(r'\| \*\*meio a meio\*\* \|[^\n]*', _P11)
_tab = TXT[TXT.find('| marco | nv 6 |'):]
_l_rf = re.search(r'\| refino do `meio a meio` \|([^\n]*)', _tab)
_l_es = re.search(r'\| escolhas gastas em refino, acumuladas \|([^\n]*)', _tab)
_l_pt = re.search(r'\| \*\*pontos de atributo\*\* \|([^\n]*)', _tab)
_l_ch = re.search(r'\| \*\*pontos de atributo do chefe\*\* \|([^\n]*)', _tab)
_dez = re.search(r'O chefe começa com (\w+) pontos na criação, e não (\w+)\.', TXT)
if not (_nove and _p26 and _marc and _mm and _l_rf and _l_es and _l_pt and _l_ch and _dez):
    erro('2.1: faltou dono — os nove pontos da peca 2, a regra do §3.2, a curva do meio a meio ou a tabela')
else:
    _ruins21 = []
    _base = _NUM_PT.get(_nove.group(1).lower())
    if _NUM_PT.get(_p26.group(1).lower()) != _base:
        _ruins21.append(f'a peca 26 diz {_p26.group(1)} pontos e a peca 2 diz {_nove.group(1)}')
    _curva = [int(x) for x in re.findall(r'`(\d+)`', _mm.group(0))]
    _pub = [[int(x) for x in re.findall(r'`(\d+)`', l.group(1))] for l in (_l_rf, _l_es, _l_pt)]
    _r, _esp = 0, ([], [], [])
    for _k, _c in enumerate(_curva, 1):
        _r = max(_r, _c - (1 + _k))
        _esp[0].append(_c); _esp[1].append(_r); _esp[2].append(_base + _k + (_k - _r))
    for _rot, _pp, _e in zip(('o refino', 'as escolhas gastas em refino', 'os pontos'), _pub, _esp):
        if _pp != _e:
            _ruins21.append(f'{_rot}: a peca publica {_pp}, e a conta da {_e}')
    _ch = [int(x) for x in re.findall(r'`(\d+)`', _l_ch.group(1))]
    _mais = _NUM_PT.get(_dez.group(1).lower(), -1) - _NUM_PT.get(_dez.group(2).lower(), -99)
    if _NUM_PT.get(_dez.group(2).lower()) != _base or _mais != 1 or _ch != [x + 1 for x in _esp[2]]:
        _ruins21.append(f'a linha do chefe publica {_ch}, e a do inimigo mais 1 da {[x + 1 for x in _esp[2]]}')
    if 'O ponto do chefe é a única coisa acima da tabela que não se paga na vida' not in TXT:
        _ruins21.append('a peca parou de declarar que o ponto do chefe nao se paga na vida (decisao da v0.233)')
    for _x in _ruins21:
        erro('2.1: ' + _x)
    if not _ruins21:
        print(f'  [x] {_base} na criacao e o orcamento por marco {_esp[2]}; o chefe comeca com {_base + 1}, '
              'e o ponto dele e a unica coisa acima da tabela que nao se paga na vida')


# --------------------------------------------------------------------------
bloco('2.2 A TROCA DO §3.2 — o que sai da tabela se paga na vida')
# --------------------------------------------------------------------------
# O dono do ponto e a peca 1 §5.2 (um ponto move 5pp), o personagem acerta o alvo
# dificil em 50% e o inimigo acerta o meio da banda do §3.1. A tabela do §3.2 e a
# conta desses tres, e o Brutamontes e o Baluarte do §3.4 tem de ser a linha de ±2.
_pp22 = re.search(r'um ponto de Defesa move `(\d+)` pontos percentuais, e o personagem acerta alvo difícil em `(\d+)%`', TXT)
_T22 = tabela(TXT, '| pontos em volta da tabela | a vida, pela Defesa | a vida, pelo acerto e pela CD |')
_frase22 = re.search(r'Um ponto de Defesa acima da tabela custa `(\d+)%` da vida, e um ponto de acerto e CD custa `(\d+),(\d)%`', TXT)
PP = PC = MEIO_INI = None
if not (_pp22 and _T22 and _frase22 and _mb31):
    erro('2.2: faltou a regra do ponto (§3.4), a tabela da troca do §3.2, a frase dela ou a banda do §3.1')
else:
    PP, PC = int(_pp22.group(1)), int(_pp22.group(2))
    MEIO_INI = (int(_mb31.group(1)) + int(_mb31.group(2))) / 2
    _vd = lambda k: (PC - PP * k) / PC
    _va = lambda k: MEIO_INI / (MEIO_INI + PP * k)
    _mau22 = []
    for _l in _T22:
        _k = int(_l[0].replace('−', '-').replace('+', ''))
        _pd, _pa = _f(_l[1].replace('×', '')), _f(_l[2].replace('×', ''))
        if abs(round(_vd(_k), 3) - _pd) > 1e-9 or abs(round(_va(_k), 3) - _pa) > 1e-9:
            _mau22.append(f'{_l[0]}: a peca publica {_l[1]} e {_l[2]}, e a conta da {_vd(_k):.3f} e {_va(_k):.3f}')
    if (int(_frase22.group(1)), _f(f'{_frase22.group(2)},{_frase22.group(3)}')) != (round(100 * (1 - _vd(1))), round(100 * (1 - _va(1)), 1)):
        _mau22.append(f'a frase diz {_frase22.group(1)}% e {_frase22.group(2)},{_frase22.group(3)}%, e a conta da '
                      f'{100 * (1 - _vd(1)):.0f}% e {100 * (1 - _va(1)):.1f}%')
    _bru = re.search(r'^\| `Brutamontes` \| vida crua `× ([\d,]+)` \| `Defesa −(\d)`', TXT, re.M)
    _bal = re.search(r'^\| `Baluarte` \| `Defesa \+(\d)`, que vale `× [\d,]+` \| vida crua `× ([\d,]+)` \|', TXT, re.M)
    if not (_bru and _bal):
        _mau22.append('nao achei o Brutamontes e o Baluarte no §3.4')
    elif abs(_f(_bru.group(1)) - round(_vd(-int(_bru.group(2))), 2)) > 1e-9 or abs(_f(_bal.group(2)) - round(_vd(int(_bal.group(1))), 2)) > 1e-9:
        _mau22.append('o Brutamontes ou o Baluarte do §3.4 nao sao a linha de ±2 da troca do §3.2')
    for _x in _mau22:
        erro('2.2: ' + _x)
    if not _mau22:
        print(f'  [x] as {len(_T22)} linhas da troca saem de {PP} pontos por ponto, do alvo dificil a {PC}% e do '
              f'inimigo a {MEIO_INI}%; o Brutamontes e o Baluarte sao a linha de ±2')


# --------------------------------------------------------------------------
bloco('3. A GRADE — os degraus, a pressao e as fichas prontas contra o manual')
# --------------------------------------------------------------------------
# A tabela de inimigo e do manual, e a grade parte dela: a saida de um personagem e
# o dano do grupo ÷ 4, e o golpe-base e o dano do chefe ÷ 4. O orcamento de cada
# degrau e o do Pathfinder 2e, lido da peca e conferido contra as notas da pesquisa.
_DEG = {}
for _c in tabela(TXT, '| categoria | rodadas | orçamento | pressão | o golpe, em % da vida de um personagem |'):
    if len(_c) >= 6 and re.match(r'[\d,]+$', _c[1]):
        _DEG[_c[0]] = dict(rod=_f(_c[1]), orc=_f(_c[2]), press=None if _c[3] == '—' else _f(_c[3]),
                           golpe_pct=_f(_c[4].rstrip('%')), interv=_c[5])
CATS = list(_DEG)
CHEFES = [c for c in CATS if c != 'Capanga']
_mb3 = re.search(r'trivial `(\d+)`, baixa `(\d+)`, moderada `(\d+)`, severa `(\d+)`, extrema `(\d+)`', TXT)
_mn3 = re.search(r'Trivial (\d+) ou menos \(ajuste \d+\), Low (\d+) \(\d+\), Moderate (\d+) \(\d+\), Severe (\d+) \(\d+\), Extreme (\d+) \(\d+\)', ler(NOTAS))
# v0.337: a tabela `Inimigos` e a prosa em volta dela saem do gerador do manual
# (partF.js), que era de onde o .docx saia. Ate a v0.336 esta leitura abria o .docx,
# que foi para o arquivo no passo 5 da migracao; o livro reconstruido nao publica a
# tabela. O dono definitivo dela e' decisao da v0.338.
_MANUAL = {}
_PROSA = []
_pf = ler(PARTF)
_mi = re.search(r"H2\('Inimigos'\)(.*?)(?=\n\s*H2\()", _pf, re.S)
if _mi:
    _PROSA = [x.replace("\\'", "'") for x in re.findall(r"\bP\('((?:[^'\\]|\\.)*)'\)", _mi.group(1))]
    _mt = re.search(r"TBL\(\[([^\]]*'Chefe: dano'[^\]]*)\],\s*\[(.*?)\n\s*\],", _mi.group(1), re.S)
    if _mt:
        def _n(x):
            try:
                return float(x)
            except ValueError:
                return None
        for _lin in re.findall(r"\[([^\[\]]*)\]", _mt.group(2)):
            _v = re.findall(r"'([^']*)'", _lin)
            if len(_v) == 6 and _v[0].isdigit():
                _vd_ = _v[2].split(' a ')
                _MANUAL[int(_v[0])] = (float(_v[1].replace('~', '')), (int(_vd_[0]) + int(_vd_[-1])) / 2,
                                       float(_v[3]), _n(_v[4]), _n(_v[5]))
if len(_MANUAL) < 5 or not _PROSA:
    erro(f'3: li {len(_MANUAL)} linha(s) e {len(_PROSA)} paragrafo(s) da secao `Inimigos` do partF.js — '
         'ela mudou de forma, e as checagens que dependem da tabela vao pular')
_mpct = re.search(r'O dano dele por rodada é (\d+)% da vida de um personagem', ' '.join(_PROSA))
PCT = int(_mpct.group(1)) / 100 if _mpct else None
R_DES = _DEG.get('Desastre', {}).get('rod')


def rod(c): return _DEG[c]['rod']
def press(c): return _DEG[c]['orc'] * R_DES / _DEG[c]['rod']
def s_de(nv): return _MANUAL[nv][0] / 4
def base_de(nv): return _MANUAL[nv][2] / 4
def vida_cel(nv, c, n): return _meio_baixo(rod(c) * n * s_de(nv))
def golpe_cel(nv, c): return _meio_baixo(base_de(nv) / 2) if c == 'Capanga' else _meio_baixo(press(c) * base_de(nv))
def interv_ok(c, n): return c != 'Capanga' and n * _DEG[c]['orc'] >= 4
def L_de(nv): return _MANUAL[nv][2] / PCT


if len(_DEG) != 5 or 'Capanga' not in _DEG or 'Desastre' not in _DEG:
    erro(f'3: achei {len(_DEG)} degrau(s) na tabela do §4, e a peca promete cinco com o Capanga e o Desastre')
elif not (_mb3 and _mn3):
    erro('3: nao li o orcamento do Pathfinder 2e na peca (§4) ou nas notas da pesquisa')
else:
    _ruins3 = []
    _orc = [int(x) for x in _mb3.groups()]
    if _orc != [int(x) for x in _mn3.groups()]:
        _ruins3.append(f'a peca cita o orcamento {_orc} e as notas da pesquisa dizem {list(_mn3.groups())}')
    _rods = [rod(c) for c in CATS]
    if _rods != sorted(_rods):
        _ruins3.append(f'as rodadas nao crescem com o degrau: {_rods}')
    for _c, _o in zip(CATS, _orc):
        if abs(_DEG[_c]['orc'] - round(_o / _orc[2], 2)) > 1e-9:
            _ruins3.append(f'`{_c}`: orcamento {_DEG[_c]["orc"]} e a conta da {_o / _orc[2]:.2f}')
        if _c != 'Capanga' and abs(_DEG[_c]['press'] - round(press(_c), 3)) > 1e-9:
            _ruins3.append(f'`{_c}`: pressao {_DEG[_c]["press"]} e orcamento × {R_DES} ÷ rodadas da {press(_c):.3f}')
        _ab = [n for n in range(1, 7) if interv_ok(_c, n)]
        _e_int = f'×{_ab[0]}' if _ab else '—'
        if _DEG[_c]['interv'] != _e_int:
            _ruins3.append(f'`{_c}`: a Intervencao abre em {_DEG[_c]["interv"]}, e N × orcamento ≥ 4 da {_e_int}')
        if PCT:
            _gp = round(100 * (0.5 if _c == 'Capanga' else press(_c)) * 0.25 * PCT, 1)
            if abs(_gp - _DEG[_c]['golpe_pct']) > 1e-9:
                _ruins3.append(f'`{_c}`: o golpe publica {_DEG[_c]["golpe_pct"]}% e a conta da {_gp}%')
    if 'Ele morreu na v0.282' not in TXT and 'Ela morreu na v0.282' not in TXT:
        _ruins3.append('a peca parou de registrar que a escada morreu na v0.282')
    if re.search(r'personagens = fator × \d', TXT.replace('`personagens = fator × 4`, e a `Calamidade` exigia oito', '')):
        _ruins3.append('a formula da escada (personagens = fator × 4) voltou como regra viva')
    for _x in _ruins3:
        erro('3: ' + _x)
    if not _ruins3:
        print(f'  [x] os cinco degraus: rodadas {_rods}, orcamento do PF2e {_orc} (o mesmo das notas), a '
              'pressao, o golpe em % e a porta da Intervencao reconstroem')

if not _MANUAL or PCT is None:
    pulou('3. as fichas prontas contra a tabela do manual — a tabela `Inimigos` do partF.js nao foi lida')
elif _DEG:
    print(f'  a tabela `Inimigos` do manual tem {len(_MANUAL)} linhas, de nv {min(_MANUAL)} a {max(_MANUAL)}.')
    _mau3b = 0
    for _nv in (10, 20, 30):
        _i = TXT.find(f'**Nível {_nv}**\n')
        _T = tabela(TXT[_i:], '| categoria | `×1` | `×2` | `×3` | `×4` | `×5` | `×6` |') if _i >= 0 else []
        if len(_T) != 5:
            erro(f'3: nao achei as cinco linhas da ficha pronta do nivel {_nv} no §4.1')
            _mau3b += 1
            continue
        for _l in _T:
            _c = _l[0]
            for _n, _cel in zip(range(1, 7), _l[1:7]):
                _nums = [int(x) for x in re.findall(r'\d+', _cel)]
                if _c == 'Capanga':
                    _esp = [2 * _n, math.floor(s_de(_nv)), golpe_cel(_nv, _c)]
                else:
                    _esp = [vida_cel(_nv, _c, _n), golpe_cel(_nv, _c)]
                if _nums != _esp:
                    erro(f'3: {_c} ×{_n} no nivel {_nv}: a peca publica {_cel} e a conta da {_esp}')
                    _mau3b += 1
    _d4 = (vida_cel(30, 'Desastre', 4), 4 * golpe_cel(30, 'Desastre'))
    if abs(_d4[0] - _MANUAL[30][1]) > 0.51 or abs(_d4[1] - _MANUAL[30][2]) > 2:
        erro(f'3: o Desastre ×4 do nivel 30 da {_d4} e a linha do manual e ({_MANUAL[30][1]:.0f}, {_MANUAL[30][2]:.0f})')
        _mau3b += 1
    if not _mau3b:
        print('  [x] as 90 celulas das fichas prontas do §4.1 reconstroem da tabela do manual, e o Desastre ×4 '
              f'e a linha do manual ({_d4[0]} de vida, {_d4[1]} por rodada contra {_MANUAL[30][2]:.0f})')


# 3.3 o tamanho. O alcance e o lado da grade vezes o quadrado, e do `Grande` para cima o
# golpe pega metade num vizinho.
_QUAD = None
_T33 = tabela(TXT, '| tamanho | ocupa na grade | alcance | o golpe pega |')
if len(_T33) != 4:
    erro(f'3.3: achei {len(_T33)} das 4 linhas da tabela de tamanho do §3.3')
else:
    _mau33 = 0
    for _l in _T33:
        _mg = re.match(r'(\d+)×(\d+)\s*\(([\d,]+) × ([\d,]+) m\)', _l[1])
        _ma = re.match(r'([\d,]+) m$', _l[2].strip())
        if not (_mg and _ma):
            erro(f'3.3: nao li a linha "{_l[0]}" da tabela de tamanho')
            _mau33 += 1
            continue
        _lado = int(_mg.group(1))
        _q = _f(_mg.group(3)) / _lado
        _QUAD = _QUAD or _q
        if abs(_q - _QUAD) > 1e-9 or abs(_f(_ma.group(1)) - _lado * _QUAD) > 1e-9:
            erro(f'3.3: "{_l[0]}" ocupa {_lado}×{_lado} e publica alcance {_l[2]}')
            _mau33 += 1
        if ('metade' in _l[3]) != (_lado >= 2):
            erro(f'3.3: "{_l[0]}" ocupa {_lado}×{_lado} e a coluna dos alvos diz "{_l[3]}"')
            _mau33 += 1
    if not _mau33:
        print('  [x] o alcance de cada tamanho e o lado da grade vezes o quadrado, e a metade no vizinho e de '
              'quem passa de um quadrado')


# --------------------------------------------------------------------------
bloco('4. AS ACOES — N, e o x1 e o x2 contra a regua da peca 19 §2.2')
# --------------------------------------------------------------------------
# A regua de condicao da peca 19 §2.2 publica o valor das quatro condicoes que
# tiram acao contra um inimigo de 1, 2 e 3 acoes. O x1 e o x2 da grade tem 1 e 2,
# e a regra do TR no comeco do turno e o que os devolve a regua. Um TR a mais
# multiplica o que a condicao nega pela chance de o inimigo FALHAR nele; a chance
# sai da peca 1 §6 (treinado e sem treino) e a desvantagem, do d20.
_T19 = ler(P19)
REGUA = {int(k): [_f(x) for x in re.findall(r'`([\d,]+)×`', l)]
         for k, l in re.findall(r'^\| (?:\*\*)?`([123])`(?:\*\*)? \|(.*)$', _T19, re.M)}
_mfil = re.search(r'filtro de dominância de `([\d,]+)×`', _T19)
_mtr = re.search(r'^\| \*\*treinado\*\* \| (\d+)% \| (\d+)% \| (\d+)% \| (\d+)% \| \*\*(\d+)%\*\* \|$', _t01, re.M)
_mst = re.search(r'^\| \*\*sem treino\*\* \| (\d+)% \| (\d+)% \| (\d+)% \| (\d+)% \| \*\*(\d+)%\*\* \|$', _t01, re.M)
_T4 = tabela(TXT, '| o que o inimigo tem | `×1` | `×2` |')
_m3a = re.search(r'o chefe de três ações fica em `([\d,]+)×` a `([\d,]+)×`, e o filtro de dominância é `([\d,]+)×`', TXT)
if sorted(REGUA) != [1, 2, 3] or not (_mfil and _mtr and _mst and len(_T4) == 4 and _m3a):
    erro('4: faltou a regua de 1, 2 e 3 acoes da peca 19 §2.2, o filtro, o TR da peca 1 §6, a tabela do §4.2 '
         'ou a frase do chefe de tres acoes')
else:
    _ruins4 = []
    FILTRO = _f(_mfil.group(1))
    pt = (100 - int(_mtr.group(5))) / 100
    ps = [(100 - int(x)) / 100 for x in _mst.groups()]
    pd = 1 - (1 - pt) ** 2
    rng = lambda v, ps_: (round(min(v) * min(ps_), 2), round(max(v) * max(ps_), 2))
    # a regra: no x1 o TR com a maestria; no x2 o mesmo TR com desvantagem
    _esp4 = {'nada': (rng(REGUA[1], [1]), rng(REGUA[2], [1])),
             'a regra': (rng(REGUA[1], [pt]), rng(REGUA[2], [pd])),
             'o Teste de Resistência normal, com a maestria': (rng(REGUA[1], [pt]), rng(REGUA[2], [pt])),
             'o Teste de Resistência normal, sem a maestria': (rng(REGUA[1], ps), rng(REGUA[2], ps))}
    for _l in _T4:
        _e = _esp4.get(_l[0])
        if _e is None:
            _ruins4.append(f'a linha "{_l[0]}" da tabela do §4.2 nao e uma das quatro que a conta conhece')
            continue
        for _cel, _ee, _n in zip(_l[1:3], _e, ('×1', '×2')):
            if _faixa_num(_cel) != _ee:
                _ruins4.append(f'{_l[0]}, {_n}: a peca publica {_cel} e a conta da {_ee[0]:.2f} a {_ee[1]:.2f}')
    _esp4['×1'] = [None, _esp4['a regra'][0]]; _esp4['×2'] = [None, _esp4['a regra'][1]]
    if (_f(_m3a.group(1)), _f(_m3a.group(2)), _f(_m3a.group(3))) != (min(REGUA[3]), max(REGUA[3]), FILTRO):
        _ruins4.append('o §4.2 cita o chefe de tres acoes ou o filtro diferente da peca 19 §2.2')
    if _esp4['×1'][1][1] > FILTRO or _esp4['×2'][1][1] > FILTRO:
        _ruins4.append('a regra do x1 ou do x2 deixa a condicao acima do filtro de dominancia')
    for _fr in ('No `×1`, a condição que tira ação dá ao inimigo um Teste de Resistência no começo do turno dele, sempre com a maestria.',
                'No `×2`, o mesmo Teste de Resistência, com desvantagem.', 'Ele age `N` vezes por rodada'):
        if _fr not in TXT:
            _ruins4.append(f'a peca parou de publicar "{_fr[:60]}"')
    if not re.search(r'regra do `×1` e do `×2` da peça 26 §4\.2', _T19):
        _ruins4.append('a peca 19 §2.2 parou de apontar para a regra do x1 e do x2 da peca 26 §4.2, que substituiu o piso de 3 acoes')
    for _x in _ruins4:
        erro('4: ' + _x)
    if not _ruins4:
        print(f'  [x] a regra devolve o x1 a {_esp4["×1"][1][0]:.2f}× a {_esp4["×1"][1][1]:.2f}× e o x2 a '
              f'{_esp4["×2"][1][0]:.2f}× a {_esp4["×2"][1][1]:.2f}×, abaixo do filtro de {FILTRO}×, com o TR '
              f'treinado falhando {pt:.0%} e a desvantagem {pd:.1%}')


# --- a simulacao, a mesma de toda a peca: os corpos vivos batem, e o grupo gasta a saida da
# rodada neles em ordem (os capangas primeiro, o chefe age primeiro) ---------------------------
def _simula(saida, corpos):
    vs = [list(c) for c in corpos]
    rod_, cobrado = 0, 0.0
    while vs and rod_ < 100:
        cobrado += sum(c[1] for c in vs)
        sobra = saida
        while sobra > 0 and vs:
            if vs[0][0] <= sobra:
                sobra -= vs.pop(0)[0]
            else:
                vs[0][0] -= sobra
                sobra = 0
        rod_ += 1
    return rod_, cobrado


def _corpo(nv, c, n):
    return (vida_cel(nv, c, n), n * golpe_cel(nv, c))


def _capangas(nv, k):
    return [(math.floor(s_de(nv)), golpe_cel(nv, 'Capanga'))] * k


if _MANUAL and PCT and _DEG:
    # 4.3 N corpos de x1 contra um de xN
    _T43 = tabela(TXT, '| categoria | `×2` | `×4` | `×6` |')
    _mau43 = 0
    if len(_T43) != 4:
        erro(f'4.3: a tabela do §4.3 tem {len(_T43)} linha(s), e sao quatro degraus de chefe')
        _mau43 += 1
    for _l in _T43:
        for _n, _cel in zip((2, 4, 6), _l[1:4]):
            _e = round(_simula(_n * s_de(30), [_corpo(30, _l[0], 1)] * _n)[1]
                       / _simula(_n * s_de(30), [_corpo(30, _l[0], _n)])[1], 2)
            if abs(_f(_cel) - _e) > 1e-9:
                erro(f'4.3: {_l[0]} ×{_n}: a peca publica {_cel} e a simulacao da {_e:.2f}')
                _mau43 += 1
    if not _mau43:
        print('  [x] 4.3: o que N corpos de x1 cobram contra um de xN reconstroi da simulacao, no nivel 30')
    # 4.6 concentrando
    _T46 = tabela(TXT, '| categoria, no nível 30 | rodadas | derruba um na rodada (`×4`) | derruba na luta |')
    _mau46 = 0
    if len(_T46) != 4:
        erro(f'4.6: a tabela do §4.6 tem {len(_T46)} linha(s)')
        _mau46 += 1
    for _l in _T46:
        _g = golpe_cel(30, _l[0])
        _e = (rod(_l[0]), round(L_de(30) / (4 * _g), 2), round(rod(_l[0]) * _g / L_de(30), 3))
        _pub = (_f(_l[1]), _f(_l[2]), _f(_l[3].split('×')[0]))
        if _pub != _e:
            erro(f'4.6: {_l[0]}: a peca publica {_pub} e a conta da {_e}')
            _mau46 += 1
    _m46 = re.search(r'derruba um personagem na rodada `([\d,]+)`\.\*\* \*No nível 30 ele entrega `(\d+)` de dano na luta contra `(\d+)` do alvo', TXT)
    _m46b = re.search(r'Numa luta de três rodadas ele derruba `([\d,]+)` pessoas se concentrar', TXT)
    _gd = golpe_cel(30, 'Desastre')
    if not (_m46 and _m46b) or (_f(_m46.group(1)), int(_m46.group(2)), int(_m46.group(3)), _f(_m46b.group(1))) != \
            (round(L_de(30) / (4 * _gd), 2), 3 * 4 * _gd, int(L_de(30)), round(3 * 4 * _gd / L_de(30), 2)):
        erro('4.6: a prosa do Desastre ×4 concentrando (a rodada, o dano da luta, a vida do alvo, as pessoas) nao e a conta')
        _mau46 += 1
    _m46c = re.search(r'a `Calamidade ×4` tira `(\d+)%` da vida do grupo em cinco rodadas', TXT)
    if not _m46c or int(_m46c.group(1)) != round(100 * rod('Calamidade') * golpe_cel(30, 'Calamidade') / L_de(30)):
        erro('4.6: a prosa da Calamidade ×4 (a vida do grupo que ela tira) nao e a conta')
        _mau46 += 1
    if not _mau46:
        print(f'  [x] 4.6: concentrando, o Desastre ×4 derruba um na rodada {L_de(30) / (4 * _gd):.2f} e '
              f'{3 * 4 * _gd / L_de(30):.2f} pessoas na luta; a tabela dos quatro degraus reconstroi')


# --------------------------------------------------------------------------
bloco('4.4 O DADO — o golpe de cada degrau, em dado, pela regra do §4.4')
# --------------------------------------------------------------------------
# A regra mora na peca (os dados, o teto na mao, o piso do numero seco), e a
# mesma funcao roda no gerador do bloco (make.js). O desempate e o do gerador.
_mdl = re.search(r'O tamanho do dado se escolhe entre ([^*]+?)\s*—', TXT)
_DL = [int(x) for x in re.findall(r'`d(\d+)`', _mdl.group(1))] if _mdl else []
_mteto = re.search(r'no máximo \*\*(\w+)\*\* dados', TXT)
_TETO_D = _NUM_PT.get(_mteto.group(1).lower()) if _mteto else None
_mseco = re.search(r'Abaixo de `(\d+)` o golpe fica em número seco', TXT)


def _jr(x):
    return math.floor(x + 0.5)            # o Math.round do gerador


def _dado(alvo):
    """a expressao do §4.4, na ordem de desempate do gerador"""
    if alvo < int(_mseco.group(1)):
        return str(_meio_baixo(alvo))
    meta, bom = alvo / 2, None
    for _d in _DL:
        med = (_d + 1) / 2
        n = max(1, _jr(meta / med))
        if n > _TETO_D:
            continue
        fixo = alvo - n * med
        if fixo < 0:
            continue
        inte = 0 if abs(fixo - _jr(fixo)) < 1e-9 else 1
        er = abs(n * med - meta)
        if (bom is None or inte < bom[0] or (inte == bom[0] and er < bom[1] - 1e-9)
                or (inte == bom[0] and abs(er - bom[1]) < 1e-9 and n < bom[2])):
            bom = (inte, er, n, _d, _jr(fixo))
    return f'{bom[2]}d{bom[3]} + {bom[4]}' if bom[4] > 0 else f'{bom[2]}d{bom[3]}'


def _media(e):
    m = re.match(r'^(\d+)d(\d+)(?:\s*\+\s*(\d+))?$', e.strip())
    return int(m.group(1)) * (1 + int(m.group(2))) / 2 + int(m.group(3) or 0) if m else float(e)


_T44 = tabela(TXT, '| categoria, no nível 26 a 30 | o golpe | em dado |')
if not (_DL and _TETO_D and _mseco):
    erro('4.4: nao achei na peca a regra do dado (os dados, o teto, o piso do seco)')
elif not _MANUAL:
    pulou('4.4. o dado de cada degrau — sem a tabela do manual')
elif len(_T44) != 5:
    erro(f'4.4: a tabela do dado tem {len(_T44)} linha(s), e sao cinco degraus')
else:
    _mau44 = 0
    for _l in _T44:
        _g = golpe_cel(30, _l[0])
        if int(_l[1]) != _g or _l[2] != _dado(_g):
            erro(f'4.4: {_l[0]}: a peca publica {_l[1]} e {_l[2]}, e a conta da {_g} e {_dado(_g)}')
            _mau44 += 1
    if not _mau44:
        print(f'  [x] os cinco golpes do nivel 30 e o dado deles saem da regra do §4.4 '
              f'(dados {_DL}, no maximo {_TETO_D} na mao, seco abaixo de {_mseco.group(1)})')


# --------------------------------------------------------------------------
bloco('5. O CAPANGA — o esquadrao de 2N, o cambio e o chefe com capangas, pela simulacao')
# --------------------------------------------------------------------------
# O Capanga xN sao 2N corpos que caem num golpe (a vida e a saida de um
# personagem, para baixo) e batem metade do golpe-base. A coluna do Capanga da
# tabela `Inimigos` do manual e a que o gerador copia, entao ela tem de ser esta.
_ruins5 = []
for _fr in ('A vida de um corpo é a saída de um personagem por rodada, para baixo.',
            'O golpe de um corpo é metade do golpe-base', 'os capangas primeiro'):
    if _fr not in TXT:
        _ruins5.append(f'a peca parou de publicar "{_fr}"')
if not _MANUAL:
    pulou('5. o Capanga contra o manual e a simulacao — sem a tabela do manual')
else:
    _fora5 = [f'nv{nv}: ({kv}, {kd}) contra ({math.floor(s_de(nv))}, {golpe_cel(nv, "Capanga")})'
              for nv, (_s, _cv, _cd, kv, kd) in sorted(_MANUAL.items())
              if (kv, kd) != (math.floor(s_de(nv)), golpe_cel(nv, 'Capanga'))]
    if _fora5:
        _ruins5.append('a coluna do Capanga do manual nao e a do §5 — ' + ' · '.join(_fora5[:3]))
    # o que o esquadrao cobra, contra a frase do §5
    _m5 = re.search(r'Com meio golpe o esquadrão cobra `([\d,]+)%` da vida do grupo em duas rodadas no nível 30', TXT)
    _cob5 = _simula(4 * s_de(30), _capangas(30, 8))
    if not _m5 or abs(_f(_m5.group(1)) - round(100 * _cob5[1] / (4 * L_de(30)), 1)) > 1e-9 or _cob5[0] != 2:
        _ruins5.append(f'o §5 diz que o esquadrao cobra {_m5.group(1) if _m5 else "?"}% e a simulacao da '
                       f'{100 * _cob5[1] / (4 * L_de(30)):.1f}% em {_cob5[0]} rodadas')
    # o cambio: quantos capangas cobram o que a celula cobra, nas faixas do manual
    _T5 = tabela(TXT, '| quantos capangas cobram o que a célula cobra | `×1` | `×2` | `×3` | `×4` | `×5` | `×6` |')

    def _cambio(nv, c, n):
        _, alvo = _simula(n * s_de(nv), [_corpo(nv, c, n)])
        return min(range(1, 80), key=lambda k: abs(_simula(n * s_de(nv), _capangas(nv, k))[1] - alvo))
    if len(_T5) != 4:
        _ruins5.append(f'a tabela do cambio tem {len(_T5)} linha(s), e sao quatro degraus de chefe')
    for _l in _T5:
        for _n, _cel in zip(range(1, 7), _l[1:7]):
            _ks = sorted({_cambio(nv, _l[0], _n) for nv in _MANUAL})
            _pub = [int(x) for x in re.findall(r'\d+', _cel)]
            if _pub != ([_ks[0]] if len(_ks) == 1 else [_ks[0], _ks[-1]]):
                _ruins5.append(f'o cambio de {_l[0]} ×{_n} publica {_cel} e a simulacao da {_ks}')
    _md = re.search(r'Um `Desastre ×N` vale `3N` capangas do mesmo nível', TXT)
    _des = next((l for l in _T5 if l[0] == 'Desastre'), None)
    _fixos = [(_n, int(c)) for _n, c in zip(range(1, 7), _des[1:7]) if re.fullmatch(r'\d+', c)] if _des else []
    if not _md or any(k != 3 * _n for _n, k in _fixos):
        _ruins5.append('a regra "um Desastre ×N vale 3N capangas" nao e a linha do Desastre da tabela do cambio')
    # 5.1 o chefe com capangas: cada capanga toma 1/(rodadas x N)
    _T51 = tabela(TXT, '| célula, no nível 30 | `1 ÷ (rodadas × N)` | com 1 capanga, o chefe fica com | com 2 | com 3 |')
    if len(_T51) < 4:
        _ruins5.append(f'a tabela do chefe com capangas do §4.5 tem {len(_T51)} linha(s)')
    for _l in _T51:
        _mc = re.match(r'(\w+) ×(\d)', _l[0])
        _c, _n = _mc.group(1), int(_mc.group(2))
        if abs(_f(_l[1].rstrip('%')) - round(100 / (rod(_c) * _n), 1)) > 1e-9:
            _ruins5.append(f'{_l[0]}: 1 ÷ (rodadas × N) publica {_l[1]} e a conta da {100 / (rod(_c) * _n):.1f}%')
        _, _alvo = _simula(_n * s_de(30), [_corpo(30, _c, _n)])
        _v, _d = _corpo(30, _c, _n)
        for _k, _cel in zip((1, 2, 3), _l[2:5]):
            _fr = min((x / 1000 for x in range(1, 1001)),
                      key=lambda f_: abs(_simula(_n * s_de(30), _capangas(30, _k) + [(_v * f_, _d * f_)])[1] - _alvo))
            if abs(_f(_cel.rstrip('%')) - round(100 * _fr, 1)) > 0.101:
                _ruins5.append(f'{_l[0]} com {_k} capanga(s): a peca publica {_cel} e a simulacao da {100 * _fr:.1f}%')
    for _x in _ruins5[:8]:
        erro('5: ' + _x)
    if not _ruins5:
        print(f'  [x] a coluna do Capanga do manual e a do §5 nas {len(_MANUAL)} faixas; o esquadrao cobra '
              f'{100 * _cob5[1] / (4 * L_de(30)):.1f}% em {_cob5[0]} rodadas no nivel 30')
        print('  [x] o cambio das quatro linhas e o chefe com capangas do §4.5 reconstroem da simulacao, com os '
              'capangas abatidos primeiro, e o Desastre ×N vale 3N')

    # -- 5.2: a linha do manual obedece a regra que a propria secao escreve ----
    # A prosa da secao `Inimigos` do manual diz que o chefe sozinho tem "cerca de tres
    # vezes o dano de rodada do grupo em vida, e e isso que faz a luta contra ele durar
    # tres rodadas". O Desastre x4 e essa linha, entao ela e o chao da grade inteira.
    _PAL = {'uma': 1, 'duas': 2, 'três': 3, 'tres': 3, 'quatro': 4, 'cinco': 5}
    _prosa = next((t for t in _PROSA if 'vezes o dano de rodada do grupo em vida' in t), None)
    _mmult = re.search(r'cerca de (\w+) vezes o dano de rodada do grupo em vida', _prosa or '')
    _mdur = re.search(r'durar (\w+) rodadas', _prosa or '')
    if not (_mmult and _mdur):
        erro('5.2: a prosa da secao `Inimigos` do manual mudou de forma, e esta checagem nao acha o '
             'multiplicador e a duracao nela')
    else:
        _MULT, _DUR = _PAL[_mmult.group(1).lower()], _PAL[_mdur.group(1).lower()]
        _fora52 = [f'nv{nv}' for nv, (_s, _cv, _cd, _kv, _kd) in sorted(_MANUAL.items())
                   if abs(_cv - _MULT * _s) > 0.51 or math.ceil(_cv / _s - 1e-9) != _DUR]
        if _fora52:
            erro('5.2: a tabela `Inimigos` desobedece a regra que a prosa dela escreve em ' + ', '.join(_fora52))
        elif _DUR != R_DES:
            erro(f'5.2: o manual promete a luta de {_DUR} rodadas e o Desastre da grade dura {R_DES}')
        else:
            print(f'  [x] as {len(_MANUAL)} linhas do manual tem {_MULT} × a saida do grupo em vida e saem em '
                  f'{_DUR} rodadas inteiras — a duracao do Desastre da grade')


# --------------------------------------------------------------------------
bloco('6. O GRAU NAO VIRA NUMERO — nem aqui nem na peca que decide isso')
# --------------------------------------------------------------------------
_LINHAS_GRAU = [l for l in TXT.split('\n')
                if re.search(r'\bgrau\b', l, re.I) and re.search(r'`\d', l) and not l.lstrip().startswith('>')]
if _LINHAS_GRAU:
    erro(f'6: {len(_LINHAS_GRAU)} linha(s) viva(s) falam de grau e carregam numero em crase: '
         + _LINHAS_GRAU[0].strip()[:90])
else:
    print('  [x] nenhuma linha viva desta peca pendura numero no grau')
if 'Grau é reconhecimento; nível é poder' not in ler(P12):
    erro('6: a peca 12 parou de publicar "Grau e reconhecimento; nivel e poder"')
else:
    print('  [x] a peca 12 continua sendo a dona de "Grau e reconhecimento; nivel e poder"')


# --------------------------------------------------------------------------
bloco('7. NENHUM VALOR DE REGRA GUARDADO AQUI DENTRO')
# --------------------------------------------------------------------------
_FONTE = open(__file__, encoding='utf-8').read()
_achou7 = False
for _pad, _que in ((r'^\s*(VIDA|DANO|CAMBIO|FATOR|ACOES|RODADAS|PRESSAO|GOLPE)_?\w*\s*=\s*[\d.]', 'valor de ficha'),
                   (r'^\s*(CHEFE|CAPANGA|ORCAMENTO)\s*=\s*[\d.]', 'o chefe, o capanga ou o orcamento')):
    if re.search(_pad, _FONTE, re.M):
        erro(f'7: tem {_que} escrito como constante neste arquivo — ele tem de sair do documento dono')
        _achou7 = True
if not _achou7:
    print('  [x] as rodadas, o orcamento, a vida, o golpe e o cambio saem dos donos, e nenhum esta escrito aqui')
if len(_MEIO) < 8:
    erro('7: a curva de refino nao foi lida da peca 11')
else:
    print('  [x] a curva do `meio a meio` foi lida da peca 11: ' + ' '.join(str(_MEIO[k]) for k in sorted(_MEIO)))


# --------------------------------------------------------------------------
bloco('7.1 A EXPANSAO — ela divide a vida por 1,92, e os gates sao os do jogador')
# --------------------------------------------------------------------------
# O Acerto do dominio para de rolar: a saida efetiva sobe por 1 ÷ o acerto do
# §3.1, e desde a v0.282 a vida crua paga isso (decisao do Mizuki de 28/09: o que
# o inimigo carrega se paga por dentro). A luta com Expansao dura rodadas ÷ 1,92.
_mexp = re.search(r'multiplica a saída efetiva dele por `1 ÷ ([\d,]+)`, que é `([\d,]+) ×`, e a vida crua dele se divide por `([\d,]+)`', TXT)
MULT_E = None
if not _mexp:
    erro('7.1: a peca nao publica o multiplicador da Expansao como "1 ÷ acerto", e que a vida se divide por ele')
else:
    _ruins71 = []
    _ac = _f(_mexp.group(1)); MULT_E = _f(_mexp.group(2))
    if abs(1 / _ac - MULT_E) > 0.01 or _f(_mexp.group(3)) != MULT_E:
        _ruins71.append(f'a peca publica {MULT_E} e 1 ÷ {_ac} da {1 / _ac:.2f}, ou a vida se divide por outro numero')
    if _mb31 and not (int(_mb31.group(1)) <= _ac * 100 <= int(_mb31.group(2))):
        _ruins71.append(f'a Expansao usa acerto {_ac:.0%} fora da banda do §3.1')
    _T71 = tabela(TXT, '| categoria | a luta sem Expansão | com Expansão completa |')
    if len(_T71) != 4:
        _ruins71.append(f'a tabela da luta com Expansao tem {len(_T71)} linha(s), e sao quatro degraus de chefe')
    for _l in _T71:
        if _l[0] not in _DEG or _f(_l[1]) != rod(_l[0]) or abs(_f(_l[2]) - round(rod(_l[0]) / MULT_E, 2)) > 1e-9:
            _ruins71.append(f'`{_l[0]}`: a peca publica {_l[1]} e {_l[2]}, e a conta da {rod(_l[0]) if _l[0] in _DEG else "?"} '
                            f'e {rod(_l[0]) / MULT_E:.2f}' if _l[0] in _DEG else f'`{_l[0]}` nao e degrau')
    _m71 = re.search(r'Um `Desastre ×4` com Expansão sai com `(\d+)` de vida no nível 30, e a luta dura `([\d,]+)` rodada', TXT)
    if _MANUAL and (not _m71 or int(_m71.group(1)) != _meio_baixo(vida_cel(30, 'Desastre', 4) / MULT_E)
                    or _f(_m71.group(2)) != round(R_DES / MULT_E, 2)):
        _ruins71.append('a prosa do Desastre ×4 com Expansao (a vida e a luta) nao e a conta')
    if re.search(r'Expansão de Domínio completa multiplica o fator|multiplica o fator do inimigo por', TXT):
        _ruins71.append('voltou a regra da escada: a Expansao multiplicando o fator')
    for _x in _ruins71:
        erro('7.1: ' + _x)
    if not _ruins71:
        print(f'  [x] a Expansao multiplica a saida efetiva por 1 ÷ {_ac} = {MULT_E}, a vida se divide por ele, e a '
              'luta com Expansao de cada degrau e as rodadas ÷ ele')

# 7.1b os gates e o desvio de refino da sem barreiras
PARTE = 'manual/gerador/partE.js'
_E = ler(PARTE)
_gc = re.search(r"\['Completa', '[^']*', 'nível (\d+) e refino (\d+)'", _E)
_gs = re.search(r"\['Sem Barreiras', '[^']*', 'refino (\d+)", _E)
_gp = re.search(r'A completa abre no nível `(\d+)` com refino `(\d+)`, e a Expansão sem Barreiras pede refino `(\d+)`', TXT)
_prot = re.search(r'a sua proteção é `1/(\d+) do refino \+ (\d+)`', _P11)
_db = re.search(r'o nível `(\d+)` dá refino `(\d+)` e `(\d+)` rodadas de domínio, contra a luta mais longa com Expansão, a da `(\w+)`, de `([\d,]+)`', TXT)
if not (_gc and _gs and _gp and _prot and _db and _marc and _mm and MULT_E and PP):
    erro('7.1b: faltou dono — os gates do manual (partE.js), os da peca, a protecao da peca 11, a duracao no gate, '
         'a curva ou o multiplicador')
else:
    _ruins = []
    if (int(_gp.group(1)), int(_gp.group(2)), int(_gp.group(3))) != (int(_gc.group(1)), int(_gc.group(2)), int(_gs.group(1))):
        _ruins.append(f'a peca publica os gates {_gp.groups()} e o manual diz {(_gc.group(1), _gc.group(2), _gs.group(1))}')
    NVS = [int(x) for x in re.findall(r'nv (\d+)', _marc.group(0))]
    CURVA = dict(zip(NVS, [int(x) for x in re.findall(r'`(\d+)`', _mm.group(0))]))
    NV_C, RF_C, RF_S = int(_gc.group(1)), int(_gc.group(2)), int(_gs.group(1))
    dur = lambda r: max(1, r // 2)
    _maior = max(CHEFES, key=rod)
    _lut = round(rod(_maior) / MULT_E, 2)
    if (int(_db.group(1)), int(_db.group(2)), int(_db.group(3)), _db.group(4), _f(_db.group(5))) != \
            (NV_C, CURVA.get(NV_C), dur(CURVA.get(NV_C, 0)), _maior, _lut):
        _ruins.append(f'no gate a peca diz {_db.groups()}, e a curva e a grade dao nivel {NV_C}, refino {CURVA.get(NV_C)}, '
                      f'{dur(CURVA.get(NV_C, 0))} rodadas, contra a {_maior} de {_lut}')
    _curtos = [n for n in NVS if n >= NV_C and CURVA[n] >= RF_C and dur(CURVA[n]) < _lut]
    if _curtos:
        _ruins.append(f'do gate para cima o dominio fica abaixo da luta mais longa com Expansao nos niveis {_curtos}')
    if not re.search(r'\*\*Ela divide a vida pelo mesmo `' + re.escape(f'{MULT_E:.2f}'.replace('.', ',')) + r'`\.\*\*', TXT):
        _ruins.append('a sem barreiras parou de dividir a vida pelo mesmo multiplicador da completa')
    _st = re.search(r'o inimigo só chega a refino `(\d+)` no nível `(\d+)`', TXT)
    _prim = min((n for n in NVS if CURVA[n] >= RF_S), default=None)
    if not _st or (int(_st.group(1)), int(_st.group(2))) != (RF_S, _prim):
        _ruins.append(f'a peca diz o refino {RF_S} num nivel diferente do {_prim} da curva')
    _linhas = re.findall(r'^\| nv `(\d+)` \| `(\d+)` \| `\+(\d+)` \| `× ([\d,]+)` \|$', TXT, re.M)
    _esperados = [n for n in NVS if n >= NV_C and CURVA[n] >= RF_C and CURVA[n] < RF_S]
    if [int(l[0]) for l in _linhas] != _esperados:
        _ruins.append(f'a tabela do desvio tem os marcos {[int(l[0]) for l in _linhas]} e devia ter {_esperados}')
    prot = lambda r: r // int(_prot.group(1)) + int(_prot.group(2))
    for _n, _r, _g, _v in _linhas:
        _n = int(_n)
        _ganho = prot(RF_S) - prot(CURVA.get(_n, 0))
        _vf = round((PC - PP * _ganho) / PC, 2)
        if (CURVA.get(_n), _ganho, _vf) != (int(_r), int(_g), _f(_v)):
            _ruins.append(f'no nv{_n} a tabela diz refino {_r}, Defesa +{_g}, vida × {_v}; a conta da refino '
                          f'{CURVA.get(_n)}, Defesa +{_ganho}, × {_vf:.2f}')
    for _r in _ruins:
        erro('7.1b: ' + _r)
    if not _ruins:
        print(f'  [x] os gates sao os do manual (nivel {NV_C} e refino {RF_C}; sem barreiras no refino {RF_S}), o dominio '
              f'cobre a luta mais longa com Expansao, e o desvio de refino se paga na vida pela troca do §3.2')


# --------------------------------------------------------------------------
bloco('8. A RESISTENCIA — isencao pontual e protecao ampla')
# --------------------------------------------------------------------------
_PESOS = {}
for _l in tabela(ler(P19), '| grupo | tipos | do dano recebido |'):
    if len(_l) >= 3 and _l[2].endswith('%'):
        _PESOS[_l[0]] = int(_l[2].rstrip('%')) / 100.0


def _efetiva(frac, modo):
    poupa = frac * 0.5 if modo == 'resistência' else (frac if modo == 'imunidade' else -frac)
    return 1.0 / (1.0 - poupa)


if not _PESOS:
    erro('8: nao achei a tabela dos tres grupos de dano na peca 19 §4')
else:
    _T8 = tabela(TXT, '| grupo | peso | resistência | imunidade | vulnerabilidade |')
    _mau8 = 0
    for _l in _T8:
        if len(_l) < 5 or not _l[1].endswith('%'):
            continue
        _peso = int(_l[1].rstrip('%')) / 100.0
        if _l[0] in _PESOS and abs(_PESOS[_l[0]] - _peso) > 1e-9:
            erro(f'8: a peca publica peso {_l[1]} para {_l[0]} e a peca 19 §4 diz {_PESOS[_l[0]]:.0%}')
            _mau8 += 1
        for _cel, _modo in zip(_l[2:5], ('resistência', 'imunidade', 'vulnerabilidade')):
            # A isencao pontual e decisao autoral; nao finge ausencia de efeito defensivo.
            _esperado8 = 1.0 if _l[0] == 'um tipo só' and _modo == 'resistência' else round(_efetiva(_peso, _modo), 2)
            if abs(_f(re.match(r'([\d,]+)', _cel).group(1)) - _esperado8) > 0.011:
                erro(f'8: {_l[0]}, {_modo}: a peca publica {_cel} e a regra pede {_esperado8:.2f}x')
                _mau8 += 1
    if not _T8:
        erro('8: nao achei a tabela de vida efetiva do §6.3')
        _mau8 += 1
    _mr = re.search(r'Resistência ao grupo `Físicos` divide a vida crua por `([\d,]+)`', TXT)
    _mi = re.search(r'Imunidade a `Físicos` divide a vida crua por `([\d,]+)`', TXT)
    _rf, _if = round(_efetiva(_PESOS.get('Físicos', 0), 'resistência'), 2), round(_efetiva(_PESOS.get('Físicos', 0), 'imunidade'), 2)
    if not (_mr and _mi) or (_f(_mr.group(1)), _f(_mi.group(1))) != (_rf, _if):
        erro('8: a peca nao declara que a resistencia divide a vida crua, ou declara um numero que nao e a conta')
        _mau8 += 1
    _mx8 = re.search(r'Um `Desastre ×4` imune a `Físicos` sai com `(\d+)` de vida no nível 30', TXT)
    if _MANUAL and (not _mx8 or int(_mx8.group(1)) != _meio_baixo(vida_cel(30, 'Desastre', 4) / _if)):
        erro('8: o exemplo do Desastre ×4 imune a Fisicos nao e a vida dele dividida pela imunidade')
        _mau8 += 1
    if re.search(r'multiplica o fator da categoria por|exige `10` personagens', TXT):
        erro('8: voltou a moeda da escada — a resistencia multiplicando o fator, ou o numero de pessoas')
        _mau8 += 1

    # A regra deve estar legivel no dono e nas duas publicacoes que o mestre usa.
    _regra8 = r'Resistência a até `(\d+)` tipos fixos, no total da criatura, não desconta PV\.'
    _lim8 = re.search(_regra8, TXT)
    if not _lim8:
        erro('8: falta a regra de isencao pontual com o limite total da criatura')
    for _rel8 in ('../../bestiario/08-livro/capitulos/50-o-bloco.md', '../05-material/gerador-inimigo/make.js'):
        _copia8 = ler(os.path.join(AQUI, _rel8))
        _m8 = re.search(_regra8, _copia8)
        if not _lim8 or not _m8 or _m8.group(1) != _lim8.group(1):
            erro(f'8: isencao pontual diverge ou sumiu em {_rel8}')
        for _trava8 in ('Um grupo completo continua pago, mesmo quando seus tipos são escritos separadamente.',
                        'Três ou mais tipos mistos que não completem um grupo continuam sem preço definido; não aplique a isenção a esse caso.'):
            if _trava8 not in TXT or _trava8 not in _copia8:
                erro(f'8: falta limite de cobertura da isencao no dono ou em {_rel8}')
    _um8 = [c for c in _T8 if c[0] == 'um tipo só']
    if len(_um8) != 1:
        erro('8: a linha de um tipo precisa existir uma unica vez')
    _fogo8 = re.search(r'O mesmo `Desastre ×4` resistente apenas a Fogo conserva `(\d+)` PV', TXT)
    if _MANUAL and (not _fogo8 or int(_fogo8.group(1)) != vida_cel(30, 'Desastre', 4)):
        erro('8: o exemplo resistente a Fogo nao conserva a vida da celula')
    if not _mau8:
        print(f'  [x] as {len(_T8)} linhas do §6.3 conferem, incluindo isencao pontual e pesos da peca 19 §4, '
              f'e a peca declara que a vida crua se divide: resistir {_rf}, ser imune {_if}')


# --------------------------------------------------------------------------
bloco('9. O CATALOGO DO JOGADOR NA FICHA DO INIMIGO — as portas e as moedas')
# --------------------------------------------------------------------------
# Tres portas e tres moedas: a tecnica paga no orcamento de feitico da acao; a
# aptidao paga na cota (os N golpes da rodada), pelo cambio de PE da peca 5 §4; e o
# que muda o encontro paga na vida. Os donos: o ponto de feitico e o piso da Classe 1
# (peca 19 §2.1), o cambio (peca 5 §4), a maior Classe (peca 18), o custo das
# anti-dominio (peca 11 §6.5).
_mp = re.search(r'vira `1d8` de dano — que são `([\d,]+)`', _T19)
_ESC19 = {}
for _l19 in tabela(_T19, '| Classe | `Leve` | `Média` | `Pesada` | Rotina |'):
    if len(_l19) >= 5 and _l19[0].isdigit():
        _ESC19[int(_l19[0])] = int(_l19[4])
_CL18 = {}
for _l18 in ler(P18).split('\n'):
    _m18 = re.match(r'\|\s*\*{0,2}(\d+)\*{0,2}\s*\|\s*[\d.—]+\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|'
                    r'\s*(\d+)\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|', _l18)
    if _m18:
        _CL18[int(_m18.group(1))] = int(_m18.group(5))
_mpe = re.search(r'recuperar `\+1` PE \| permanente \| `([\d,]+)`', ler(P05))
_PONTO = _f(_mp.group(1)) if _mp else None
_PISO19 = _ESC19[min(_ESC19)] if _ESC19 else None
_CAMBIO = _f(_mpe.group(1)) if _mpe else None
if not (_PONTO and _PISO19 and _CAMBIO and _CL18):
    erro('9: faltou dono — o ponto de feitico ou o piso da Classe 1 (peca 19 §2.1), o cambio (peca 5 §4) ou a '
         'maior Classe (peca 18)')
else:
    print(f'  um ponto de feitico vale {_PONTO}; o menor feitico custa {_PISO19} pontos; 1 PE por rodada vale '
          f'{_CAMBIO}; a maior Classe no nivel 30 e a {_CL18.get(30)}.')

    # -- 9.1: o orcamento de feitico, o golpe ÷ o ponto --------------------------
    _T91 = tabela(TXT, '| pontos por ação | `Capanga` | `Ameaça` | `Desastre` | `Catástrofe` | `Calamidade` |')
    if not _MANUAL:
        pulou('9.1. o orcamento de feitico — sem a tabela do manual')
    elif len(_T91) != len(_MANUAL):
        erro(f'9.1: a tabela de orcamento tem {len(_T91)} linha(s) e o manual tem {len(_MANUAL)} faixas')
    else:
        _mau91 = 0
        _cols91 = ['Capanga', 'Ameaça', 'Desastre', 'Catástrofe', 'Calamidade']
        for _l in _T91:
            _nv = int(re.search(r'\d+', _l[0]).group(0))
            for _cel, _c in zip(_l[1:], _cols91):
                _pts = _media(_dado(golpe_cel(_nv, _c))) / _PONTO
                if _pts < _PISO19 - 1e-9:
                    if _cel.lower() != 'seco':
                        erro(f'9.1: nv {_nv}, {_c}: {_pts:.2f} pontos, abaixo do piso de {_PISO19}, e a peca publica "{_cel}"')
                        _mau91 += 1
                elif _cel.lower() == 'seco' or abs(_f(_cel) - _pts) > 0.051:
                    erro(f'9.1: nv {_nv}, {_c}: a peca publica "{_cel}" e o golpe da {_pts:.2f} pontos')
                    _mau91 += 1
        _mx91 = re.search(r'A maior ação de inimigo do sistema é `([\d,]+)` pontos — a `(\w+)` do nível 30 —, e o teto do jogador naquele nível é `(\d+)`\.\*\* \*Uma ação de inimigo é `(\d+)%`', TXT)
        _top = max(_cols91, key=lambda c: golpe_cel(30, c))
        _pt30 = _media(_dado(golpe_cel(30, _top))) / _PONTO
        if not _mx91 or (_f(_mx91.group(1)), _mx91.group(2), int(_mx91.group(4))) != \
                (round(_pt30, 1), _top, round(100 * _pt30 / int(_mx91.group(3)))):
            erro(f'9.1: a prosa da maior acao nao e a conta: {_top} com {_pt30:.1f} pontos')
            _mau91 += 1
        _mc = re.search(r'numa ação de `(\d+),(\d)` pontos a Classe é a `(\d+)`, e uma `Leve` custa `(\d+)`', TXT)
        _cls = {int(x): int(y) for x, y in re.findall(r"H2\('Classe (\d+) · (\d+) pontos", ler('manual/gerador/partF.js'))}
        if not (_mc and _cls):
            erro('9.1: a peca parou de dizer que o preco da Melhoria usa a maior Classe que cabe (v0.230)')
            _mau91 += 1
        else:
            _pt = float(f'{_mc.group(1)}.{_mc.group(2)}')
            _c = max(c for c, pp_ in _cls.items() if pp_ <= _pt)
            if _c != int(_mc.group(3)) or -(-_c // 2) != int(_mc.group(4)):
                erro(f'9.1: com {_pt} pontos a maior Classe que cabe e a {_c}, e a Leve dela custa {-(-_c // 2)}')
                _mau91 += 1
        if not _mau91:
            print(f'  [x] 9.1: as {len(_T91) * 5} celulas do orcamento sao a media do dado ÷ {_PONTO}, o seco e o piso da '
                  f'Classe 1, e a maior acao e a {_top} do nivel 30, com {_pt30:.1f} pontos')

    # -- 9.2: a aptidao come a cota, e o custo sai da peca 11 -------------------
    _APT11 = {}
    for _l11 in tabela(ler(P11), '| | Classe · gate | abre em | o refino escala | PE por rodada |'):
        if len(_l11) >= 5:
            _mm_ = re.match(r'([\d,]+) × maior Classe', _l11[4].strip())
            _mf_ = re.match(r'(\d+) fixos?', _l11[4].strip())
            _APT11[_l11[0].strip()] = ('x', _f(_mm_.group(1))) if _mm_ else ('fixo', float(_mf_.group(1)) if _mf_ else 0.0)
    _mer = re.search(r'^\*\*E erguer custa a sua maior Classe em PE, toda vez que ela sobe\*\* — (.+)$', ler(P11), re.M)
    _ERG11 = set(re.findall(r'`([^`]+)`', _mer.group(1).split('*')[0])) if _mer else set()
    _i92 = TXT.find('| ligada a luta inteira, no nível 30 |')
    _cab92 = TXT[_i92:TXT.find('\n', _i92)] if _i92 >= 0 else ''
    _cols92 = [(m_.group(1), int(m_.group(2))) for m_ in re.finditer(r'`(\w+) ×(\d)`', _cab92)]
    _T92 = tabela(TXT, '| ligada a luta inteira, no nível 30 |')
    if not (_APT11 and _mer and _cols92 and _T92):
        erro('9.2: faltou a tabela das quatro anti-dominio da peca 11 §6.5, a frase de erguer, ou a tabela da aptidao do §6.5')
    elif 30 not in _MANUAL:
        pulou('9.2. a aptidao contra a cota — a linha do nivel 30 do manual nao foi lida')
    else:
        _mau92 = 0
        for _l in _T92:
            _nomes = [n_ for n_ in _APT11 if n_ in _l[0]]
            if len(_nomes) != 1:
                erro(f'9.2: a linha "{_l[0]}" nao nomeia uma aptidao que a peca 11 §6.5 preca')
                _mau92 += 1
                continue
            _fmt = _APT11[_nomes[0]]
            _erg = _nomes[0] in _ERG11
            if ('erguer' in _l[0]) != _erg:
                erro(f'9.2: a linha "{_l[0]}" diz erguer ao contrario da frase da peca 11')
                _mau92 += 1
            for _cel, (_c, _n) in zip(_l[1:], _cols92):
                _custo = ((math.ceil(_fmt[1] * _CL18[30] - 1e-9) if _fmt[0] == 'x' else _fmt[1])
                          + (_CL18[30] / rod(_c) if _erg else 0)) * _CAMBIO
                _esp = round(_custo / (_n * golpe_cel(30, _c)) * 100)
                if int(re.match(r'(\d+)%', _cel).group(1)) != _esp:
                    erro(f'9.2: {_nomes[0]} num {_c} ×{_n}: a peca publica {_cel} e a conta da {_esp}%')
                    _mau92 += 1
        _mx92 = re.search(r'No nível 30 um `Desastre ×1` não carrega a `Extensão de Domínio`: ela custa `(\d+)%` da cota dele', TXT)
        _ext = next((l for l in _T92 if 'Extensão' in l[0]), None)
        _ci = [i_ for i_, cn in enumerate(_cols92) if cn == ('Desastre', 1)]
        if not (_mx92 and _ext and _ci) or int(re.match(r'(\d+)', _ext[1 + _ci[0]]).group(1)) != int(_mx92.group(1)) or int(_mx92.group(1)) <= 100:
            erro('9.2: a prosa da Extensao no Desastre ×1 nao e a celula da tabela, ou ela cabe na cota')
            _mau92 += 1
        if not _mau92:
            print(f'  [x] 9.2: as {len(_T92)} linhas da aptidao reconstroem do custo da peca 11 §6.5, com erguer repartido '
                  f'pelas rodadas do degrau e a cota dos N golpes; a Extensao nao cabe no Desastre ×1')

    # -- 9.3: as duas trocas ruins ----------------------------------------------
    _mh = re.search(r'`([\d,]+) × H` no `Desastre` e `([\d,]+) × H` na `Calamidade`, no nível 30', TXT)
    _PAL93 = {'meia': 0.5, 'uma': 1.0, 'uma e meia': 1.5}
    _m93 = re.search(r'(meia|uma e meia|uma) ação é `Leve`, (meia|uma e meia|uma) é `Média`, (meia|uma e meia|uma) é `Pesada`', _T19)
    _m3 = re.search(r'metade de (\w+) ações é uma e meia', _T19)
    _T93 = re.findall(r'a `(Leve|Média|Pesada)` precisa de `(\d+)` alvos', TXT)
    _me93 = re.search(r'empata quando `alvos × ações negadas = (\d+) × ações gastas`', TXT)
    _ruins93 = []
    if not (_mh and _m93 and _m3 and len(_T93) == 3 and _me93):
        _ruins93.append('faltou a prosa das trocas ruins, a escada de acoes negadas da peca 19 ou as tres contas de alvo')
    elif 30 in _MANUAL:
        if (_f(_mh.group(1)), _f(_mh.group(2))) != (round(golpe_cel(30, 'Desastre') / s_de(30), 2),
                                                     round(golpe_cel(30, 'Calamidade') / s_de(30), 2)):
            _ruins93.append(f'H de cura vale golpe ÷ a saida de um personagem: '
                            f'{golpe_cel(30, "Desastre") / s_de(30):.2f} e {golpe_cel(30, "Calamidade") / s_de(30):.2f}')
        _acts_pc = _NUM_PT.get(_m3.group(1).lower())
        if int(_me93.group(1)) != _acts_pc:
            _ruins93.append(f'o empate da condicao usa {_me93.group(1)}, e a rodada do personagem tem {_acts_pc} acoes na peca 19')
        _esc93 = dict(zip(('Leve', 'Média', 'Pesada'), (_PAL93[_m93.group(i_)] for i_ in (1, 2, 3))))
        for _t, _a in _T93:
            if int(_a) != round(_acts_pc / _esc93[_t]):
                _ruins93.append(f'a `{_t}` precisa de {_acts_pc / _esc93[_t]:g} alvos, e a peca publica {_a}')
    for _x in _ruins93:
        erro('9.3: ' + _x)
    if not _ruins93:
        print('  [x] 9.3: H de cura vale golpe ÷ a saida de um personagem, e a condicao empata em alvos × acoes negadas '
              '= as acoes da rodada do personagem × acoes gastas, com a escada da peca 19')

    # -- 9.4: cada porta declara a moeda ----------------------------------------
    _MOEDAS = ('orçamento de feitiço', 'cota de dano por rodada', 'a vida')
    _T94 = tabela(TXT, '| o que ele carrega | onde ela se paga |')
    _faltam = [m_ for m_ in _MOEDAS if not any(m_ in l[1] for l in _T94)]
    if len(_T94) != len(_MOEDAS) or _faltam:
        erro(f'9.4: a tabela das portas tem {len(_T94)} linha(s), e faltam as moedas {_faltam}')
    else:
        print('  [x] 9.4: as tres portas do §6.5 declaram a moeda — o orcamento de feitico, a cota e a vida')


# =============================================================================
bloco('9.5 AS MALDICOES PRONTAS — as seis do gerador de inimigo, na grade')
# =============================================================================
# A ancora e o `dados.js` do gerador-inimigo. Cada pronta declara a categoria e o N;
# as Acoes Multiplas so existem em quem age mais de uma vez (N > 1); as Intervencoes
# so em quem a porta do §6.5 abre; o arranjo cabe na criacao; e nenhuma guarda numero
# de ficha. Os quatro `gerar-*.py` do livro rodam com `--conferir`.
_DJ = os.path.join(AQUI, '..', '05-material', 'gerador-inimigo', 'dados.js')
_BL = os.path.join(AQUI, '..', '05-material', 'bloco-de-inimigo.docx')
if not os.path.isfile(_DJ):
    erro('9.5: nao achei o `dados.js` do gerador-inimigo')
else:
    _dj = open(_DJ, encoding='utf-8').read()
    _i0 = _dj.find('const PRONTAS')
    _pb = _dj[_i0:_dj.find('\n];', _i0)] if _i0 >= 0 else ''
    _itens = re.split(r"\n\s*\{\s*nome:\s*'", _pb)[1:]
    _fx95 = set(re.findall(r"\['(\d+ a \d+)',", _dj))
    _mn95 = re.search(r'O inimigo com `Intervenção` carrega (\w+) por luta', TXT)
    _NINT = _NUM_PT.get(_mn95.group(1).lower()) if _mn95 else None
    _b95 = re.search(r'O inimigo monta os cinco com (\w+) pontos na criação, teto `(\d+)` ali', TXT)
    _BASE95 = _NUM_PT.get(_b95.group(1).lower()) if _b95 else None
    _TETO95 = int(_b95.group(2)) if _b95 else None
    _bd95 = re.search(r'A Defesa da tabela é `(\d+) \+ Destreza \+ proteção`', TXT)
    _DBASE95 = int(_bd95.group(1)) if _bd95 else None
    _pr95 = re.search(r'a sua proteção é `1/(\d+) do refino \+ (\d+)`', _P11)
    _DER95 = [(int(a_), int(b_), int(d_), int(r_), int(ac_)) for a_, b_, d_, ac_, r_ in
              re.findall(r"\['(\d+) a (\d+)',\s*(\d+),\s*(\d+),\s*\d+,\s*(\d+)\]", _dj)]
    _mq95 = re.search(r'^\| nível \| ([^\n]+)\|\n\|[-| ]+\|\n\| maestria \| ([^\n]+)\|', _t01, re.M)
    _MAE95 = []
    for _fx, _v in (zip(_mq95.group(1).split('|'), _mq95.group(2).split('|')) if _mq95 else []):
        _ab = re.match(r'\s*(\d+)[–-](\d+)\s*$', _fx)
        if _ab and _v.strip().isdigit():
            _MAE95.append((int(_ab.group(1)), int(_ab.group(2)), int(_v)))
    _mt95 = re.search(r'teto `\d+` ali, e teto `(\d+)`', TXT)
    _TETOC95 = int(_mt95.group(1)) if _mt95 else None
    _mo95 = re.search(r'^\| marco \|([^\n]+)\|\n\|[-| ]+\|\n(?:\|[^\n]*\n)*?\| \*\*pontos de atributo\*\* \|([^\n]+)\|\n'
                      r'\| \*\*pontos de atributo do chefe\*\* \|([^\n]+)\|', TXT, re.M)
    _ORC95 = {}
    if _mo95:
        _mks = [int(x) for x in re.findall(r'nv (\d+)', _mo95.group(1))]
        _pt_ = [int(x) for x in re.findall(r'`(\d+)`', _mo95.group(2))]
        _pc_ = [int(x) for x in re.findall(r'`(\d+)`', _mo95.group(3))]
        _ORC95 = {m_: (p_, c_) for m_, p_, c_ in zip(_mks, _pt_, _pc_)}
    _NOMES95 = ('Força', 'Destreza', 'Constituição', 'Inteligência', 'Essência')
    _fg95 = {c_ - p_ for p_, c_ in _ORC95.values()}
    _FOLGA95 = _fg95.pop() if len(_fg95) == 1 else None
    _ruins = []
    if None in (_NINT, _BASE95, _DBASE95, _TETOC95, _FOLGA95) or not (_pr95 and _DER95 and _MAE95 and _ORC95):
        _ruins.append('nao li na peca as Intervencoes por luta, os nove pontos, a base da Defesa, o teto ou o orcamento '
                      'por marco; ou a protecao da peca 11, as DERIVADAS do gerador ou a maestria da peca 1')
    if not _itens:
        _ruins.append('nao achei as PRONTAS no `dados.js`')

    def _pontos95(nv, chefe):
        _ms = [m_ for m_ in _ORC95 if m_ <= nv]
        return (_BASE95 + (1 if chefe else 0)) if not _ms else _ORC95[max(_ms)][1 if chefe else 0]
    for _it in (_itens if not _ruins else []):
        _nome = _it.split("'")[0]
        _fa = re.search(r"faixa:\s*'([^']+)'", _it)
        _ca = re.search(r"categoria:\s*'([^']+)'", _it)
        _nn = re.search(r"\bn:\s*(\d+)", _it)
        if not (_fa and _ca and _nn):
            _ruins.append(f'`{_nome}` sem faixa, categoria ou N')
            continue
        _c, _n = _ca.group(1), int(_nn.group(1))
        if _c not in _DEG or _c == 'Capanga':
            _ruins.append(f'`{_nome}` esta na categoria `{_c}`, que nao e degrau de chefe da grade')
            continue
        if not 1 <= _n <= 6:
            _ruins.append(f'`{_nome}` e ×{_n}, fora do ×1 a ×6 do §4')
        if _fa.group(1) not in _fx95:
            _ruins.append(f'`{_nome}` esta na faixa `{_fa.group(1)}`, que nao existe nas FAIXAS')
        _mm_ = re.search(r'acoes_multiplas:\s*(null|")', _it)
        if not _mm_ or ((_mm_.group(1) == 'null') != (_n == 1)):
            _ruins.append(f'`{_nome}` age {_n} vez(es), e a Acoes Multiplas dela nao bate')
        _mi = re.search(r'intervencoes:\s*\[(.*?)\]\s*[,}]', _it, re.S)
        _niv = len(re.findall(r'"nome"\s*:', _mi.group(1))) if _mi else -1
        _chefe = interv_ok(_c, _n)
        if _niv != (_NINT if _chefe else 0):
            _ruins.append(f'`{_nome}` carrega {_niv} Intervencao(oes), e `{_c} ×{_n}` pede {_NINT if _chefe else 0}')
        _ar = re.search(r"arranjo:\s*'([^']+)'", _it)
        _atq = re.search(r"ataque:\s*'([^']+)'", _it)
        if not _ar or not _atq or _atq.group(1) not in _NOMES95:
            _ruins.append(f'`{_nome}` sem arranjo ou sem atributo de ataque')
            continue
        _arr = [int(x) for x in _ar.group(1).split('·')]
        _tot = _BASE95 + (1 if _chefe else 0)
        if len(_arr) != 5 or max(_arr) > _TETO95 or sum(_arr) != _tot:
            _ruins.append(f'`{_nome}`: o arranjo {_ar.group(1)} nao e {_tot} pontos com teto {_TETO95}')
            continue
        _iat = _NOMES95.index(_atq.group(1))
        _mco = re.search(r'marcos:\s*\{([^}]*)\}', _it)
        _mc = []
        if _mco:
            for _k, _ls in re.findall(r'(\d+):\s*\[([^\]]*)\]', _mco.group(1)):
                _mc += [(int(_k), _a) for _a in re.findall(r"'([^']+)'", _ls)]
        _lo, _hi = map(int, _fa.group(1).split(' a '))
        for _nv in range(_lo, _hi + 1):
            _dv = next((d for d in _DER95 if d[0] <= _nv <= d[1]), None)
            _mae = next((v_ for a_, b_, v_ in _MAE95 if a_ <= _nv <= b_), None)
            if not _dv or _mae is None:
                _ruins.append(f'`{_nome}`: nenhuma linha de DERIVADAS, ou da maestria, cobre o nivel {_nv}')
                break
            _at = [_arr[i] + sum(1 for m, a in _mc if m <= _nv and a == _NOMES95[i]) for i in range(5)]
            if sum(1 for m, _a in _mc if m <= _nv) != _pontos95(_nv, _chefe) - _tot or max(_at) > _TETOC95:
                _ruins.append(f'`{_nome}` no nivel {_nv}: os pontos de marco nao somam o que o §3.2 da, ou passam do teto')
                break
            _exd = _at[1] - (_dv[2] - _DBASE95 - (_dv[3] // int(_pr95.group(1)) + int(_pr95.group(2))))
            _exa = _at[_iat] - (_dv[4] - _mae)
            if _exd < 0 or _exa < 0:
                _ruins.append(f'`{_nome}` no nivel {_nv}: a Destreza ou o atributo de ataque fica abaixo do que a tabela '
                              'do §3.1 pede — o desvio se paga na vida (§3.2), e a pronta nao declara isso')
                break
            if _exd + (0 if _iat == 1 else _exa) > (_FOLGA95 if _chefe else 0):
                _ruins.append(f'`{_nome}` no nivel {_nv}: acima da tabela mais do que o ponto do chefe')
                break
    _proibidos = [k for k in ('vida', 'dano', 'acoes', 'golpe', 'capanga', 'defesa') if re.search(r'\b' + k + r'\s*:', _pb)]
    if _proibidos:
        _ruins.append(f'as PRONTAS guardam {_proibidos} — esses numeros sao computados pelo make.js')
    if not os.path.isfile(_BL):
        _ruins.append('nao achei o `bloco-de-inimigo.docx`')
    _GLIV = os.path.join(RAIZ, 'bestiario', '08-livro', 'build')
    _geradores = sorted(f for f in os.listdir(_GLIV) if f.startswith('gerar-') and f.endswith('.py')) if os.path.isdir(_GLIV) else []
    if not _geradores:
        _ruins.append('nao achei os `gerar-*.py` do livro do Bestiario')
    for _g in _geradores:
        _r = subprocess.run([sys.executable, os.path.join(_GLIV, _g), '--conferir'], capture_output=True,
                            text=True, timeout=300, env=dict(os.environ, JJK_REPO=RAIZ))
        if _r.returncode != 0:
            _ruins.append(f'o livro do Bestiario nao e o que `{_g}` gera hoje: '
                          + ((_r.stderr.strip().splitlines() or _r.stdout.strip().splitlines() or ['sem saida'])[-1])[:160])
    for _m in _ruins[:6]:
        erro('9.5: ' + _m)
    if not _ruins:
        print(f'  [x] as {len(_itens)} prontas estao em celulas vivas (×1 a ×6), com Acoes Multiplas so em quem age mais de '
              'uma vez, Intervencoes so onde a porta abre, arranjos que cabem, e nenhuma guarda numero de ficha')
        print(f'  [x] os {len(_geradores)} geradores do livro do Bestiario devolvem os capitulos publicados ({", ".join(_geradores)})')


# 9.6 a area natural: os raios sao os primeiros degraus da escada de esfera do manual, a cobertura e o
# circulo em quadrados, e o cone e os retangulos cabem na tolerancia declarada.
bloco('9.6 A AREA NATURAL — a cobertura sai do nivel, e a forma e o jeito de gastar ela')
_T96 = tabela(TXT, '| nível | cobre | `Esfera` | `Cone` |')
_esc96 = re.search(r"\['Esfera \(raio\)', '([^']+)'\]", ler('manual/gerador/partC.js'))
_mtol = re.search(r'o pior erro de arredondamento nas doze células é `([\d,]+)%`', TXT)
if len(_T96) != 4 or not _esc96 or not _mtol or not _QUAD:
    erro('9.6: nao li a tabela da area natural, a escada de esfera do manual, a tolerancia ou o quadrado do §3.3')
else:
    _tol = _f(_mtol.group(1)) / 100
    _degraus = [_f(x) for x in re.findall(r'([\d,]+) m', _esc96.group(1))]
    _mau96, _raios, _fim = 0, [], 1
    for _l in _T96:
        _nv = [int(x) for x in re.findall(r'\d+', _l[0])]
        _cob = int(re.match(r'(\d+)', _l[1]).group(1))
        _r = _f(re.search(r'([\d,]+) m', _l[2]).group(1))
        _cone = _f(re.search(r'([\d,]+) m', _l[3]).group(1)) / _QUAD
        _rets = [(int(a), int(b)) for a, b in re.findall(r'(\d+)×(\d+)', _l[4])]
        _raios.append(_r)
        if _nv[0] != _fim + 1:
            erro(f'9.6: a faixa {_l[0]} nao comeca onde a anterior terminou')
            _mau96 += 1
        _fim = _nv[-1]
        if _cob != round(math.pi * (_r / _QUAD) ** 2):
            erro(f'9.6: raio {_r} m cobre {round(math.pi * (_r / _QUAD) ** 2)} quadrados, e a tabela publica {_cob}')
            _mau96 += 1
        for _rot, _area in [('o cone', _cone ** 2 / 2)] + [(f'o retangulo {a}×{b}', a * b) for a, b in _rets]:
            if abs(_area - _cob) / _cob > _tol + 1e-9:
                erro(f'9.6: na faixa {_l[0]}, {_rot} cobre {_area:g} contra {_cob}')
                _mau96 += 1
    if _raios != _degraus[:len(_raios)]:
        erro(f'9.6: os raios sao {_raios} e a escada de esfera do manual comeca em {_degraus[:len(_raios)]}')
        _mau96 += 1
    if 'E a trava conta por ESQUADRÃO' not in TXT:
        erro('9.6: a peca parou de dizer que a trava de area conta por esquadrao')
        _mau96 += 1
    if not _mau96:
        print(f'  [x] os {len(_raios)} raios sao os primeiros degraus da escada de esfera do manual, a cobertura e o circulo '
              f'em quadrados, e o cone e os retangulos cabem nos {_tol:.1%}')


# --------------------------------------------------------------------------
bloco('9.7 A RECARGA — ela come o turno, bate 2,5 golpes em cada alvo, e se paga na vida')
# --------------------------------------------------------------------------
_REC = TXT[TXT.find('#### A `Recarga`'):TXT.find('#### A área natural')]
_ruins97 = []
_k = re.search(r'cada alvo leva `([\d,]+) ×` o golpe na falha', _REC)
_dados = re.search(r'Ela rola em `d(\d+)`, com dois terços do dano em dado', _REC)
_ex = re.search(r'Um golpe de `(\d+)` vira `(\d+)`, que é `(\d+)d(\d+) \+ (\d+)`', _REC)
_banda_p = re.search(r'O golpe fica entre `(\d+)%` e `(\d+)%` da vida de um personagem do nível, então a `Recarga` tira de `(\d+)%` a `(\d+)%` dela', _REC)
_d6 = re.search(r'volta no começo do turno dele com `(\d)` ou `(\d)` no `d6`', _REC)
_disp = re.search(r'os disparos = 1 \+ \(rodadas − 1\) ÷ (\d)', _REC)
_raz = re.search(r'a rodada de `Recarga` vale `([\d,]+) × \(N ÷ 2\) ÷ N = ([\d,]+)` da rodada comum', _REC)
_T97 = re.search(r'^\| a vida se divide por \|((?: `× [\d,]+` \|)+)$', _REC, re.M)
_c97 = re.search(r'^\| categoria \|((?: `\w+` \|)+)$', _REC, re.M)
if not (_k and _dados and _ex and _banda_p and _d6 and _disp and _raz and _T97 and _c97):
    _ruins97.append('a secao da Recarga mudou de forma: o 2,5, os dados, o exemplo, a banda, o d6, os disparos, a razao '
                    'ou a tabela')
else:
    K = _f(_k.group(1)); _dN = int(_dados.group(1)); _g = int(_ex.group(1)); _tot = int(K * _g)
    _cands = [(abs(n * (_dN + 1) / 2 / _tot - 2 / 3), n) for n in range(1, 200)
              if _tot - n * (_dN + 1) / 2 >= 0 and abs((_tot - n * (_dN + 1) / 2) % 1) < 1e-9]
    _nd = min(_cands)[1]; _fx = int(_tot - _nd * (_dN + 1) / 2)
    if (int(_ex.group(2)), int(_ex.group(3)), int(_ex.group(4)), int(_ex.group(5))) != (_tot, _nd, _dN, _fx):
        _ruins97.append(f'o exemplo diz {_ex.group(2)} = {_ex.group(3)}d{_ex.group(4)} + {_ex.group(5)}, e a regra da '
                        f'{_tot} = {_nd}d{_dN} + {_fx}')
    _bd = re.search(r'A banda do `o golpe` vira \*\*`(\d+)%`–`(\d+)%`\*\*', ler(CAPANGA_DONO))
    if not _bd:
        _ruins97.append('nao achei a banda do golpe no DECIDIDO-o-capanga do Bestiario')
    else:
        b0, b1 = int(_bd.group(1)), int(_bd.group(2))
        if (int(_banda_p.group(1)), int(_banda_p.group(2))) != (b0, b1):
            _ruins97.append(f'a peca diz a banda {_banda_p.group(1)}–{_banda_p.group(2)}% e o Bestiario diz {b0}–{b1}%')
        if (int(_banda_p.group(3)), int(_banda_p.group(4))) != (int(K * b0), int(K * b1)):
            _ruins97.append(f'a Recarga tira {int(K * b0)}–{int(K * b1)}% pela banda, e a peca diz '
                            f'{_banda_p.group(3)}–{_banda_p.group(4)}%')
        if _DEG and _MANUAL:
            _gs = [100 * golpe_cel(nv, c) / L_de(nv) for nv in _MANUAL for c in CHEFES]
            if min(_gs) < b0 - 0.5 or max(_gs) > b1 + 0.5:
                _ruins97.append(f'o golpe dos chefes vai de {min(_gs):.1f}% a {max(_gs):.1f}% e a banda e {b0}–{b1}%')
    _p = (7 - int(_d6.group(1))) / 6
    if abs(_p - 1 / int(_disp.group(1))) > 1e-9:
        _ruins97.append(f'o d6 da {_p:.3f} por comeco de turno, e a formula dos disparos usa 1/{_disp.group(1)}')
    _rz = K * 0.5
    if abs(_f(_raz.group(1)) - K) > 1e-9 or abs(_f(_raz.group(2)) - _rz) > 1e-9:
        _ruins97.append(f'a razao da rodada de Recarga e {K} × metade das pessoas ÷ N = {_rz}, e a peca publica {_raz.group(2)}')
    _nomes97 = re.findall(r'`(\w+)`', _c97.group(1))
    _vals97 = [_f(x) for x in re.findall(r'`× ([\d,]+)`', _T97.group(1))]
    for _c, _v in zip(_nomes97, _vals97):
        if _c not in _DEG:
            _ruins97.append(f'a coluna `{_c}` da tabela da Recarga nao e degrau')
            continue
        _ds = 1 + (rod(_c) - 1) * _p
        _M = (_ds * _rz + (rod(_c) - _ds)) / rod(_c)
        if abs(round(_M, 2) - _v) > 1e-9:
            _ruins97.append(f'`{_c}`: a Recarga divide a vida por {_M:.2f}, e a peca publica {_v}')
    if len(_nomes97) != len(CHEFES):
        _ruins97.append(f'a tabela da Recarga tem {len(_nomes97)} degraus e sao {len(CHEFES)} de chefe')
    _med = ler('bestiario/04-fase-1/fila/MEDIDA-a-recarga-contra-a-vida.md')
    _cp = re.search(r'D&D 2024 no topo tira `(\d+)%`, a área limitada do Pathfinder 2e tira `(\d+)%` a `(\d+)%`, e a `Villain Action` do Draw Steel tira `(\d+)%`', _REC)
    _cm = [re.search(r'\| \*\*%s\*\* \|[^\n]*\| \*\*`(\d+)%%`\*\*' % s, _med) for s in ('D&D 2024', 'Draw Steel')]
    _pfm = re.findall(r'\| \*\*Pathfinder 2e\*\* \|[^\n]*\| \*\*`(\d+)%`\*\*', _med)
    if not (_cp and all(_cm) and len(_pfm) == 2) or tuple(int(x) for x in _cp.groups()) != \
            (int(_cm[0].group(1)), int(_pfm[0]), int(_pfm[1]), int(_cm[1].group(1))):
        _ruins97.append('a medicao de campo que a peca cita nao e a que a MEDIDA do Bestiario publica')
for _x in _ruins97:
    erro('9.7: ' + _x)
if not _ruins97:
    print(f'  [x] a Recarga bate {K} golpes, o exemplo sai da regra dos dois tercos em d{_dN}, a banda e a do Bestiario '
          f'(e os golpes dos chefes cabem nela), e a tabela divide a vida pelo multiplicador de cada degrau')


# --------------------------------------------------------------------------
bloco('9.8 A CORRENTE — a Regravacao na cota, a Energia Reversa e a Circulacao')
# --------------------------------------------------------------------------
_ruins98 = []
_t11_98 = _P11
_mt98 = re.search(r'sobe para `([\d,]+) × a sua maior Classe` de PE\*\*, arredondando para baixo', _t11_98)
_md98 = re.search(r'os dados de cura são `d(\d+)` em vez de', _t11_98)
_mf98 = re.search(r'Com `metade da sua (\w+) \+ metade da sua maestria` marcas', _t11_98)
_mcab = re.search(r'^\| a regravação no nível (\d+) · `(\d+)` PE = `([\d,]+)` \|((?: `[^`]+` \|)+)\n\|[-|]+\|\n'
                  r'\| da cota da rodada \|((?: `\d+%` \|)+)\n\| espalhada na luta \|((?: `[\d,]+%` \|)+)$', TXT, re.M)
_lcu = re.findall(r'^\| do nível (\d+) ao (\d+) · `(\d+)d(\d+)` \| `([\d,]+)` \|((?: `× [\d,]+` \|)+)$', TXT, re.M)
if not (_mt98 and _md98 and _mf98 and _mcab and _lcu and _CL18 and _CAMBIO):
    _ruins98.append('faltou o teto e o dado da Circulacao na peca 11, a formula das marcas, a tabela da regravacao ou a '
                    'da cura de Reacao')
elif not _MANUAL:
    pulou('9.8. a corrente contra a cota — sem a tabela do manual')
else:
    _nvc = int(_mcab.group(1))
    _pe = math.floor(_f(_mt98.group(1)) * _CL18[_nvc])
    _custo = _pe * _CAMBIO
    if int(_mcab.group(2)) != _pe or abs(_f(_mcab.group(3)) - round(_custo, 1)) > 1e-9:
        _ruins98.append(f'a regravacao no nivel {_nvc} gasta {_pe} PE = {_custo:.1f}, e a peca publica {_mcab.group(2)} = {_mcab.group(3)}')
    _cels = [(m_.group(1), int(m_.group(2))) for m_ in re.finditer(r'`(\w+) ×(\d)`', _mcab.group(4))]
    _rods = [int(x) for x in re.findall(r'`(\d+)%`', _mcab.group(5))]
    _dils = [_f(x) for x in re.findall(r'`([\d,]+)%`', _mcab.group(6))]
    for (_c, _n), _r, _d in zip(_cels, _rods, _dils):
        _cota = _n * golpe_cel(_nvc, _c)
        if (_r, _d) != (round(_custo / _cota * 100), round(_custo / _cota / rod(_c) * 100, 1)):
            _ruins98.append(f'{_c} ×{_n}: a regravacao custa {_custo / _cota * 100:.0f}% da rodada e '
                            f'{_custo / _cota / rod(_c) * 100:.1f}% na luta, e a peca publica {_r}% e {_d}%')
    for _lo, _hi, _nd_, _dd, _cu, _cs in _lcu:
        _hi = int(_hi)
        _teto = math.floor(_f(_mt98.group(1)) * _CL18[_hi])
        _cura = _teto * (int(_md98.group(1)) + 1) / 2
        if (int(_nd_), int(_dd)) != (_teto, int(_md98.group(1))) or abs(_f(_cu) - _cura) > 1e-9:
            _ruins98.append(f'do nivel {_lo} ao {_hi} a cura e {_teto}d{_md98.group(1)} = {_cura}, e a peca publica {_nd_}d{_dd} = {_cu}')
        _nvm = max(n_ for n_ in _MANUAL if n_ <= _hi)
        _vs = [_f(x) for x in re.findall(r'`× ([\d,]+)`', _cs)]
        for _n, _v in zip(range(1, 7), _vs):
            _mm_ = round(1 / (1 - _cura / (_n * s_de(_nvm))), 2)
            if abs(_mm_ - _v) > 1e-9:
                _ruins98.append(f'do nivel {_lo} ao {_hi}, ×{_n}: a cura de Reacao divide a vida por {_mm_}, e a peca publica {_v}')
    for _rot, _rx in (('a cura de acao da Energia Reversa no empate', r'os PV-base da célula ÷ as rodadas ÷ N, arredondando para baixo, no lugar de uma ação'),
                      ('a cura de Acao Bonus da Circulacao virando Reacao', r'A cura de Ação Bônus da `Circulação` vira Reação, quando ele sofre dano'),
                      ('o Rescaldo do inimigo', r'A cota fica, pelo §6\.2, e as ações dele viram golpes de corpo'),
                      ('o multiplicador que nao desconta a Reacao', r'O multiplicador não desconta a Reação de que ele abre mão'),
                      ('a corrente sem a regra de marco', r'Sem a regra de marco do §3\.2 ela fecharia no `\d+`')):
        if not re.search(_rx, TXT):
            _ruins98.append(f'a peca parou de publicar {_rot}')
    _mm98 = re.search(r'As marcas são as da peça 11, com a (\w+)\.', TXT)
    if not _mm98 or _mm98.group(1) != _mf98.group(1):
        _ruins98.append(f'as marcas leem a {_mm98.group(1) if _mm98 else "?"}, e a peca 11 le a {_mf98.group(1)}')
for _x in _ruins98:
    erro('9.8: ' + _x)
if not _ruins98 and _MANUAL:
    print(f'  [x] a regravacao no nivel {_nvc} gasta {_pe} PE = {_custo:.1f}, e a tabela reconstroi nas {len(_cels)} celulas; a '
          f'cura de Reacao divide a vida por 1 ÷ (1 − cura ÷ (N × a saida de um personagem)) nas {len(_lcu)} faixas')


# --------------------------------------------------------------------------
bloco('9.9 A PARTE DESTRUTIVEL — a vida dela e o empate: duas saidas de um personagem')
# --------------------------------------------------------------------------
_base99 = 'Para a cura de ação e as partes destrutíveis, use os PV-base da célula, antes dos ajustes de papel, atributos e recursos.'
_livro99 = ler('bestiario/08-livro/capitulos/50-o-bloco.md')
if _base99 not in TXT or _base99 not in _livro99:
    erro('9.9: cura e partes devem declarar PV-base antes dos ajustes na peca e no livro')
if 'mantenha as frações até arredondar o resultado para baixo' not in TXT or 'Arredonde para baixo somente no resultado' not in _livro99:
    erro('9.9: o arredondamento de cura e partes deve acontecer apenas no resultado')
_T99 = tabela(TXT, '| faixa | nível 2 | nível 5 |')
_f99 = 'A vida de uma parte destrutível é `os PV-base da célula ÷ as rodadas × 2 ÷ N`, arredondando para baixo'
if not _MANUAL:
    pulou('9.9. a parte destrutivel — sem a tabela do manual')
elif len(_T99) != 1 or _f99 not in TXT or 'O `×1` fica de fora por conta' not in TXT:
    erro('9.9: nao achei a tabela da parte destrutivel, a formula dela ou a frase do ×1 de fora')
else:
    _cab99 = [int(x) for x in re.findall(r'nível (\d+)', TXT[TXT.find('| faixa | nível 2 | nível 5 |'):].split('\n')[0])]
    _mau99 = [f'nv{nv}: {v} contra {math.floor(2 * s_de(nv))}' for nv, v in zip(_cab99, _T99[0][1:])
              if int(v) != math.floor(2 * s_de(nv))]
    # a formula da peca, rodada numa celula qualquer, da as duas saidas
    _v99 = math.floor(vida_cel(30, 'Desastre', 4) / rod('Desastre') * 2 / 4)
    if _v99 != math.floor(2 * s_de(30)):
        _mau99.append(f'a formula da {_v99} no Desastre ×4 do nivel 30, e duas saidas de um personagem sao {math.floor(2 * s_de(30))}')
    if _mau99:
        erro('9.9: ' + ' · '.join(_mau99))
    else:
        print(f'  [x] a vida da parte reconstroi nas {len(_cab99)} faixas: a vida ÷ as rodadas × 2 ÷ N, que e duas vezes a saida '
              'de um personagem, igual em todo degrau e todo N')


# --------------------------------------------------------------------------
bloco('9.10 A INTERVENCAO — a porta N × orcamento ≥ 4, e a vida paga 1 + 0,75 ÷ (rodadas × N)')
# --------------------------------------------------------------------------
_T910 = tabela(TXT, '| a vida se divide por | `×1` | `×2` | `×3` | `×4` | `×5` | `×6` |')
_m910 = re.search(r'`0,75` de ação extra por luta', TXT)
_f910 = re.search(r'`vida ÷ \(1 \+ ([\d,]+) ÷ \(rodadas × N\)\)`', TXT)
if len(_T910) != 4 or not (_m910 and _f910) or not _DEG:
    erro('9.10: nao achei a tabela da Intervencao, o 0,75 do Draw Steel ou a formula')
else:
    _x910 = _f(_f910.group(1))
    _mau910 = []
    for _l in _T910:
        for _n, _cel in zip(range(1, 7), _l[1:7]):
            _e = f'{1 + _x910 / (rod(_l[0]) * _n):.3f}'.replace('.', ',') if interv_ok(_l[0], _n) else '—'
            if _cel.replace('× ', '') != _e:
                _mau910.append(f'{_l[0]} ×{_n}: {_cel} contra {_e}')
    if _mau910:
        erro('9.10: ' + ' · '.join(_mau910[:4]))
    else:
        print(f'  [x] a tabela da Intervencao reconstroi: abre onde N × orcamento ≥ 4, e a vida se divide por 1 + {_x910} ÷ (rodadas × N)')


# --------------------------------------------------------------------------
bloco('10. O PAPEL — o Artilheiro por degrau, os de acao por N, e os dois da troca')
# --------------------------------------------------------------------------
_ruins10 = []
_T10a = tabela(TXT, '| categoria | `Capanga` | `Ameaça` | `Desastre` | `Catástrofe` | `Calamidade` |')
_T10n = tabela(TXT, '| papel | `×1` | `×2` | `×3` | `×4` | `×5` | `×6` |')
_mv10 = re.search(r'Em um ataque de `N`, o ganho é `\(N − 1 \+ ([\d,]+)\) ÷ N`', TXT)
_ma10 = re.search(r'`1 \+ ([\d,]+) ÷ rodadas`', TXT)
if len(_T10a) != 1 or len(_T10n) != 4 or not (_mv10 and _ma10) or not _DEG:
    _ruins10.append('nao achei a tabela do Artilheiro por degrau, a dos papeis de acao por N, o ganho da vantagem ou o do alcance')
else:
    _vant, _alc = _f(_mv10.group(1)), _f(_ma10.group(1))
    for _c, _cel in zip(CATS, _T10a[0][1:]):
        if abs(_f(_cel.replace('×', '')) - round(1 + _alc / rod(_c), 3)) > 1e-9:
            _ruins10.append(f'o Artilheiro no `{_c}` publica {_cel}, e 1 + {_alc} ÷ {rod(_c)} da {1 + _alc / rod(_c):.3f}')
    _fn = {'Emboscador ganha': lambda n: (n - 1 + _vant) / n,
           'Controlador e Reforço ganham': lambda n: 1 + 1 / n,
           'o esquadrão do Capanga, Emboscador': lambda n: (2 * n - 1 + _vant) / (2 * n),
           'o esquadrão do Capanga, Controlador e Reforço': lambda n: 1 + 1 / (2 * n)}
    for _l in _T10n:
        if _l[0] not in _fn:
            _ruins10.append(f'a linha "{_l[0]}" da tabela por N nao e uma das quatro')
            continue
        for _n, _cel in zip(range(1, 7), _l[1:7]):
            if abs(_f(_cel.replace('×', '')) - round(_fn[_l[0]](_n), 3)) > 1e-9:
                _ruins10.append(f'{_l[0]} ×{_n}: {_cel} contra {_fn[_l[0]](_n):.3f}')
    _m810 = re.search(r'um `Desastre ×4` de nível 30 sai com `(\d+)` de vida em vez de `(\d+)`', TXT)
    _m135 = re.search(r'explica os `(\d+)` que faltam', TXT)
    if _MANUAL:
        _cheia = vida_cel(30, 'Desastre', 4)
        _art = _meio_baixo(_cheia / round(1 + _alc / rod('Desastre'), 3))
        if not (_m810 and _m135) or (int(_m810.group(1)), int(_m810.group(2)), int(_m135.group(1))) != (_art, _cheia, _cheia - _art):
            _ruins10.append(f'a prosa do Artilheiro no Desastre ×4 nao e a conta: {_art} em vez de {_cheia}, faltando {_cheia - _art}')
    if 'O `Capanga` toma quatro dos seis:' not in TXT:
        _ruins10.append('a peca parou de dizer que o Capanga toma quatro dos seis papeis')

# 10.1 (v0.284): as duas regras de papel que moravam so no livro de inimigos (auditoria da
# fase 2, divergencia 3). O `Emboscador` nao sobe de `Grande`, por decisao da fase 1, e o
# `Reforco` so se paga com mais de um inimigo, porque o cambio dele vai para outro bloco. O
# livro dizia o mesmo do `Baluarte`, que na grade troca Defesa pela propria vida e serve
# sozinho: a frase velha nao volta, e nenhuma pronta e' `Emboscador` acima de `Grande` — a
# ordem dos tamanhos sai da tabela do §3.3, e nao daqui.
_L60 = os.path.join(RAIZ, 'bestiario', '08-livro', 'capitulos', '60-a-montagem.md')
_l60 = open(_L60, encoding='utf-8').read() if os.path.isfile(_L60) else ''
_RX_EMB = r'O `Emboscador` não sobe de `Grande`'
_RX_REF = r'`Reforço` só se paga com mais de um inimigo'
_RX_BAL = r'`Baluarte`[^.]*só se paga'
if not _l60:
    _ruins10.append('10.1: nao achei o capitulo 6 do livro de inimigos (60-a-montagem.md)')
else:
    for _onde, _t in (('a peca 26', TXT), ('o livro de inimigos, cap. 6', _l60)):
        if not re.search(_RX_EMB, _t):
            _ruins10.append(f'10.1: {_onde} parou de dizer que o `Emboscador` nao sobe de `Grande`')
        if not re.search(_RX_REF, _t):
            _ruins10.append(f'10.1: {_onde} parou de dizer que o `Reforco` so se paga com mais de um inimigo')
        if re.search(_RX_BAL, _t):
            _ruins10.append(f'10.1: {_onde} voltou a dizer que o `Baluarte` so se paga com mais de um inimigo — '
                            'na grade ele troca Defesa pela propria vida e serve sozinho')
_i33 = TXT.find('### 3.3 O tamanho')
_T33 = TXT[_i33:TXT.find('\n### ', _i33 + 5)] if _i33 >= 0 else ''
_TAM = [n_ for l_ in _T33.split('\n') if l_.startswith('| ') and not l_.startswith('|---')
        for n_ in re.findall(r'`(\w+)`', l_.split('|')[1])]
_DJ10 = os.path.join(AQUI, '..', '05-material', 'gerador-inimigo', 'dados.js')
_dj10 = open(_DJ10, encoding='utf-8').read() if os.path.isfile(_DJ10) else ''
# pronta por pronta, como a 9.5: a primeira forma pegava papel e tamanho numa regex so', e o
# `marcos: { ... }` da Hitotsume, entre os dois, a escondia — o arnes da v0.284 achou.
_i10 = _dj10.find('const PRONTAS')
_pb10 = _dj10[_i10:_dj10.find('\n];', _i10)] if _i10 >= 0 else ''
_emb, _sem_tam = [], []
for _it in re.split(r"\n\s*\{\s*nome:\s*'", _pb10)[1:]:
    _pp = re.search(r"papel:\s*'([^']+)'", _it)
    _tt = re.search(r"tamanho:\s*[\"']([^\"']+)[\"']", _it)
    if _pp and _pp.group(1) == 'Emboscador':
        (_emb.append((_it.split("'", 1)[0], _tt.group(1))) if _tt else _sem_tam.append(_it.split("'", 1)[0]))
for _n in _sem_tam:
    _ruins10.append(f'10.1: a pronta {_n} e `Emboscador` e nao declara tamanho no `dados.js`')
if 'Grande' not in _TAM or not _dj10:
    _ruins10.append('10.1: nao li a escada de tamanho do §3.3 ou o `dados.js` do gerador-inimigo')
else:
    _acima = set(_TAM[_TAM.index('Grande') + 1:])
    for _n, _tm in _emb:
        if _tm in _acima:
            _ruins10.append(f'10.1: a pronta {_n} e `Emboscador` e `{_tm}` — o Emboscador nao sobe de `Grande`')
    if not _emb:
        _ruins10.append('10.1: nao achei nenhuma pronta `Emboscador` no `dados.js` — a leitura da pronta mudou de forma')
for _x in _ruins10:
    erro('10: ' + _x)
if not _ruins10:
    print('  [x] o Artilheiro de cada degrau e 1 + meia rodada ÷ rodadas; os papeis de acao de cada N saem da vantagem e da '
          'acao negada, com o esquadrao do Capanga lendo 2N; e o Brutamontes e o Baluarte sao a troca do §3.2 (2.2)')
    print(f'  [x] 10.1: o Emboscador nao sobe de Grande e o Reforco so se paga com mais de um inimigo, na peca e no '
          f'livro; o Baluarte nao volta a precisar de companhia; e as {len(_emb)} prontas Emboscador cabem na escada')
    print()
    print('  O papel nao acrescenta encontro: ele move a base de um eixo para a vida, e o golpe fica onde estava.')


# Ficha concreta integrada: os números continuam nos donos, o bloco é derivado.
print('\n11. Sukuna — remontagem na grade atual (sem certificar equilíbrio)')
_suk = subprocess.run(['node', os.path.join(RAIZ, 'bestiario/05-sukuna/montar-sukuna-grade.js'), '--check'], capture_output=True, text=True)
if _suk.returncode:
    erro('11: a ficha derivada do Sukuna diverge: ' + (_suk.stderr or _suk.stdout)[-1800:])
else:
    print('  [x] ' + _suk.stdout.strip())


if ERROS:
    print(f'>>> {len(ERROS)} PROBLEMA(S):')
    for e in ERROS:
        print('   -', e)
    sys.exit(1)
if _PULADAS:
    print(f'>>> OK, mas {len(_PULADAS)} checagem(ns) PULARAM:')
    for pp in _PULADAS:
        print('   -', pp)
    print('    O que pulou NAO foi conferido. Um verde que pulou checagem nao e um verde.')
else:
    print('>>> TUDO OK — a tabela por nivel devolve o que a peca 1 publica do outro lado da mesa, a grade')
    print('    parte da tabela do manual, a regra do x1 e do x2 devolve a regua da peca 19, e o cambio,')
    print('    o chefe com capangas e o que o inimigo carrega foram medidos em vez de guardados.')

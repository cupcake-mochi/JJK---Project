#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Confere a peca 26 — o Bestiario — contra os donos de cada linha da ficha.

A peca 26 nao inventa numero: ela junta num lugar so' os que montar um inimigo
pede, e declara de onde cada um sai. Entao este validador quase nao mede regra
nova — ele mede DERIVACAO, que e' o que a peca promete.

NENHUM VALOR DE REGRA ESTA ESCRITO AQUI. A tabela de inimigo vem do manual, as
formulas vem da peca 1, a curva de refino vem da peca 11, as acoes do chefe vem
da peca 19 e os fatores de categoria vem da propria peca 26. A checagem 7 e' quem
guarda essa promessa.

As checagens 3, 5 e 9 leem o .docx do manual: sem o python-docx elas PULAM, e o
rodape DIZ que pularam. Um verde que pulou checagem nao e' um verde. A 9.4 nao
depende do manual e roda de qualquer jeito — ela le so' a declaracao da peca.
"""

import math
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
P03 = 'sistema/03-mecanica/03-economia-de-acao-e-iniciativa.md'
P07 = 'sistema/03-mecanica/07-pericias-e-oficios.md'
P11 = 'sistema/03-mecanica/11-aptidoes-e-refino.md'
P02 = 'sistema/03-mecanica/02-economia-de-atributos.md'
P12 = 'sistema/03-mecanica/12-experiencia-e-progressao.md'
P22 = 'sistema/03-mecanica/22-pactos.md'
P19 = 'sistema/03-mecanica/19-dano-e-condicoes.md'
P24 = 'sistema/03-mecanica/24-dano-de-alma.md'
DOCX = os.path.join(RAIZ, 'manual', 'Fundamento-MANUAL-v7.docx')

TXT = ler(PECA)


def celulas(linha):
    return [c.replace('*', '').replace('`', '').strip() for c in linha.split('|')[1:-1]]


def tabela(texto, cabecalho):
    """As linhas de dado da primeira tabela que comeca com `cabecalho`.

    ⚠ O `> ` de citacao sai antes de medir: a tabela dos tres grupos de dano da
    peca 19 §4 mora DENTRO de um bloco de citacao, e sem tirar o prefixo esta
    funcao nao acha ela — foi assim que a checagem 8 nasceu cega na v0.199.
    """
    i = texto.find(cabecalho)
    if i < 0:
        return []
    t = texto[i:]
    t = t[:t.find('\n\n')] if '\n\n' in t else t
    linhas = [re.sub(r'^>\s*', '', l) for l in t.split('\n')[1:]]
    return [celulas(l) for l in linhas
            if l.startswith('|') and not l.startswith('|---')]


# --------------------------------------------------------------------------
bloco('1. AS ANCORAS — cada linha da ficha aparece no dono dela')
# --------------------------------------------------------------------------
# A peca publica a ficha como uma tabela `linha | valor | dono` no §3. Este
# dicionario diz, para cada linha, o arquivo dono e um padrao que tem de casar
# la. A guarda 1.1 compara as duas listas nos DOIS sentidos: linha da peca sem
# ancora e' dono declarado que ninguem confere, e ancora sem linha e' o
# contrario. E' o mesmo defeito que a v0.198 achou no conferir-dano.py, e ele
# entra aqui ja fechado em vez de esperar alguem achar de novo.
#
# ⚠ Nenhum padrao carrega o VALOR que ele confere: ancora que carrega o valor
# some no dia em que o valor muda, que e' o dia em que ela precisa acender.
ANCORAS = {
    'nivel': (P12, r'[Nn]ível'),
    'categoria': (PECA, r'\*\*`Desastre`\*\*'),
    'vida': (PECA, r'a linha do manual vezes o fator'),
    # v0.228: a linha passou a ser da peca 24 §3.3, e a fracao e conferida no conferir-alma 13
    'integridade': (P24, r'Integridade de quem não é personagem jogador = '),
    'dano': (PECA, r'a linha do manual vezes o fator'),
    'acoes': (P19, r'O chefe age `\d+` vezes por rodada'),
    'defesa': (P01, r'10 \+ Destreza \+ prote'),
    'acerto': (P01, r'atributo.{0,20}maestria'),
    'cd': (P01, r'8 \+ atributo'),
    'reacao': (PECA, r'volta no começo do turno dele'),
    'refino': (P11, r'\*\*meio a meio\*\*'),
    'tr': (P07, r'[Tt]este de Resistência'),
    'deslocamento': (P03, r'9 m'),
    # v0.199: as quatro linhas que o Mizuki pediu. Nenhuma inventa economia —
    # as tres primeiras apontam para peca que ja existe, e a quarta e a regua
    # de tipo de dano da peca 19 §4 vista do lado do inimigo.
    'atributos': (P02, r'[Nn]ove pontos em cinco atributos'),
    'caracteristicas': (P11, r'catálogo de aptidões'),
    'pacto': (P22, r'metade da Essência'),
    'resistencia': (P19, r'\| \*\*Físicos\*\* \|'),
    'tamanho': (PECA, r'o tamanho não cobra nada'),
    'papel': (PECA, r'o que ele paga é o inverso do que ele ganha'),
}
MAPA_ANCORA = {
    'nível': ('nivel',), 'categoria': ('categoria',), 'vida': ('vida',),
    'Integridade': ('integridade',), 'dano por rodada': ('dano',),
    'ações por rodada': ('acoes',), 'Defesa': ('defesa',), 'acerto': ('acerto',),
    'CD': ('cd',), 'Reação': ('reacao',), 'refino': ('refino',),
    'Testes de Resistência': ('tr',), 'deslocamento': ('deslocamento',),
    'atributos': ('atributos',), 'características': ('caracteristicas',),
    'pacto': ('pacto',),
    'resistência, vulnerabilidade e imunidade': ('resistencia',),
    'tamanho': ('tamanho',),
    'papel': ('papel',),
}

_achadas = 0
for _rot, (_arq, _pad) in sorted(ANCORAS.items()):
    if re.search(_pad, ler(_arq)):
        _achadas += 1
    else:
        erro(f'1: a ancora "{_rot}" nao aparece em {_arq} — ou ela mudou de forma '
             f'la, ou esta linha da ficha ficou sem chao')
print(f'  {_achadas} de {len(ANCORAS)} ancoras encontradas nos donos.')

_FICHA = [c for c in tabela(TXT, '| linha | valor | dono |') if len(c) == 3]
_rotulos = [c[0] for c in _FICHA]
if not _rotulos:
    erro('1.1: nao achei a tabela da ficha do §3 — ela mudou de forma e a guarda '
         'que compara as duas listas parou de conferir')
else:
    _sem = [r for r in _rotulos if r not in MAPA_ANCORA]
    _sobra = [r for r in MAPA_ANCORA if r not in _rotulos]
    _reiv = {k for v in MAPA_ANCORA.values() for k in v}
    _orfas = sorted(set(ANCORAS) - _reiv)
    _fant = sorted(_reiv - set(ANCORAS))
    for _msg, _lista in (('linha(s) da ficha sem ancora nenhuma', _sem),
                         ('o mapa aponta para linha(s) que sairam da ficha', _sobra),
                         ('ancora(s) que nenhuma linha da ficha reivindica', _orfas),
                         ('o mapa reivindica ancora(s) que nao existem', _fant)):
        if _lista:
            erro(f'1.1: {_msg}: ' + ', '.join(_lista))
    if not (_sem or _sobra or _orfas or _fant):
        print(f'  [x] as {len(_rotulos)} linhas da ficha e as {len(ANCORAS)} ancoras '
              'se cobrem nos dois sentidos')


# --------------------------------------------------------------------------
bloco('2. AS TRES DERIVADAS — Defesa, acerto e CD saem das formulas da peca 1')
# --------------------------------------------------------------------------
# As tres nao tinham dono em documento nenhum ate a v0.198, e as tres derivam
# sem escolha. A prova de que a derivacao esta certa nao e' ela fechar sozinha:
# e' ela devolver, do lado do inimigo, os MESMOS numeros que a peca 1 §6 publica
# do lado do jogador. Se uma das duas se mover, esta acende.
def maestria(nv):
    return 1 + max(0, nv - 2) // 8


def investido(nv):
    return min(6, 3 + max(0, nv - 2) // 8)


_MEIO = {2: 1}
_lin = [c for c in tabela(ler(P11), '| | nv 6 | nv 10 | nv 14 | nv 18 | nv 22 | nv 26 | nv 30 |')
        if c and c[0].startswith('meio a meio')]
if not _lin or len(_lin[0]) < 8:
    erro('2: nao achei a linha do `meio a meio` na tabela de refino da peca 11 §3 — '
         'ela e a curva que o inimigo herda, e sem ela a Defesa dele nao reconstroi')
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
    return ref // 3 + 1          # peca 11 §6, arredonda pra baixo (peca 1 §5.4)


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
    erro('2: nao achei a tabela do §3.1 — as tres derivadas ficaram sem o outro lado')
    _mau2 = 1
for _rot, _f in (('Defesa', defesa), ('acerto', acerto), ('CD', cd), ('refino', refino)):
    if _rot not in _pub_der:
        if _pub_der:
            erro(f'2: a tabela do §3.1 nao publica a linha "{_rot}"')
            _mau2 += 1
        continue
    for _nv, _v in zip(_NIVEIS, _pub_der[_rot]):
        _esp = _f(_nv)
        if int(_v.lstrip('+')) != _esp:
            erro(f'2: no nivel {_nv} a peca publica {_rot} {_v} e a formula do dono '
                 f'da {_esp}')
            _mau2 += 1
if not _mau2:
    print('  [x] as quatro linhas do §3.1 reconstroem das formulas dos donos')

_acertos = sorted({round(p(defesa(nv), acerto(nv)) * 100) for nv in _NIVEIS})
_falhas = sorted({round((1 - p(cd(nv), acerto(nv))) * 100) for nv in _NIVEIS})
print(f'  ele acerta o alvo dificil em {_acertos[0]}% a {_acertos[-1]}%; '
      f'o TR treinado dele falha ' + ' a '.join(f'{x}%' for x in _falhas))
_t01 = ler(P01)
_m01 = re.search(r'\|\s*\*\*treinado\*\*\s*\|((?:\s*\d+%\s*\|)+)', _t01)
if not _m01:
    erro('2: a peca 1 §6 parou de publicar a linha do Teste de Resistencia treinado — '
         'a CD do inimigo se mede contra aquele numero')
else:
    _res = sorted({int(x) for x in re.findall(r'(\d+)%', _m01.group(1))})
    if _falhas != [100 - r for r in _res][::-1] and set(_falhas) != {100 - r for r in _res}:
        erro(f'2: a CD derivada faz o TR treinado falhar {_falhas}%, e a peca 1 §6 '
             f'publica que ele resiste {_res}% — os dois lados da mesma rolagem discordam')
    else:
        print(f'  [x] a CD do inimigo devolve exatamente os {_res[0]}% que a peca 1 §6 publica')

_m06 = re.findall(r'^\|\s*(?:corpo a corpo|à distância|conjuração)[^|]*\|((?:\s*\d+%\s*\|)+)',
                  _t01, re.M)
if not _m06:
    erro('2: nao achei as linhas de acerto da peca 1 §6 — a banda do inimigo se mede '
         'contra elas')
else:
    _pico = max(int(x) for l in _m06 for x in re.findall(r'(\d+)%', l))
    # ⚠ a tabela do §6 amostra os niveis de MARCO, que sao os picos da curva. O vale
    # nao aparece la — ele e' declarado ao lado, como oscilacao irredutivel. Ler so'
    # a tabela produziria uma banda de um ponto so', e o inimigo, amostrado em
    # niveis que nao sao marco, cairia fora dela sem nada estar errado.
    _mosc = re.search(r'oscilação de `(\d+)\s*pp`', _t01)
    if not _mosc:
        erro('2: a peca 1 §6 parou de declarar a oscilacao irredutivel do acerto — sem '
             'ela a tabela dela e so os picos, e a banda do inimigo fica sem chao')
    else:
        _piso = _pico - int(_mosc.group(1))
        if _acertos[0] < _piso or _acertos[-1] > _pico:
            erro(f'2: o inimigo acerta o alvo dificil em {_acertos[0]}% a {_acertos[-1]}%, '
                 f'e a peca 1 §6 publica pico de {_pico}% com oscilacao de '
                 f'{_mosc.group(1)}pp, que da a banda de {_piso}% a {_pico}%')
        else:
            print(f'  [x] o acerto dele cai na banda de {_piso}% a {_pico}% que a peca 1 '
                  '§6 publica — o pico da tabela e a oscilacao declarada')


# --------------------------------------------------------------------------
bloco('3. A CATEGORIA — vida e dano saem da linha do manual vezes o fator')
# --------------------------------------------------------------------------
# A tabela de inimigo e' do manual, e e' de la que a categoria reescala. Sem o
# python-docx esta checagem PULA, porque a alternativa seria guardar a tabela
# aqui dentro — que e' a licao no 9 no numero de que a peca inteira depende.
_CAT = []
_INT = {}
for _c in tabela(TXT, '| categoria | personagens | fator sobre a linha do manual | ações |'):
    if len(_c) < 5:
        continue
    _m = re.match(r'([\d,]+)', _c[2].replace('×', '').strip())
    if _m and _c[3].isdigit():
        # v0.221: o `Capanga` e' a unica categoria sem numero de personagens — a vida
        # dele sai do dano do grupo, e nao do fator. O travessao vira None.
        _pes = int(_c[1]) if _c[1].isdigit() else None
        _CAT.append((_c[0], _pes, float(_m.group(1).replace(',', '.')), int(_c[3])))
        _INT[_c[0]] = _c[4].strip().lower() == 'sim'
if len(_CAT) != 5:
    erro(f'3: achei {len(_CAT)} categoria(s) na tabela do §4 e a peca promete cinco — '
         'ela mudou de forma e esta checagem parou de conferir')
_CAPS = [c for c in _CAT if c[1] is None]
_CAPA = _CAPS[0] if len(_CAPS) == 1 else None
if _CAT and _CAPA is None:
    erro(f'3: esperava UMA categoria sem numero de personagens, o Capanga, e achei {len(_CAPS)}')
if 'Vida do capanga = o dano do grupo por rodada dividido por quatro, arredondado para baixo' not in TXT:
    erro('3: a peca parou de publicar de onde sai a vida do capanga — sem isso a linha dele '
         'no §4.1 e numero solto')

_FICHAS = tabela(TXT, '| categoria | nv 10 | nv 20 | nv 30 |')
_MANUAL = {}
try:
    import docx
except ImportError:
    docx = None

if docx is not None and os.path.isfile(DOCX):
    _doc = docx.Document(DOCX)
    for _t in _doc.tables:
        _cab = [c.text.strip() for c in _t.rows[0].cells]
        if _cab and _cab[0].startswith('Nível do grupo') and 'Chefe: dano' in _cab:
            for _r in _t.rows[1:]:
                _v = [c.text.strip() for c in _r.cells]
                _vd = _v[2].split(' a ')
                # ⚠ a celula pode vir com travessao, e o leitor devolve None.
                # Ate a v0.205 a faixa mais baixa vinha assim por decisao da v0.199;
                # a v0.206 abriu a coluna, e o travessao continua possivel porque
                # quem escreve a tabela pode fechar qualquer faixa de novo.
                def _n(x):
                    try:
                        return float(x)
                    except ValueError:
                        return None
                _MANUAL[int(_v[0])] = (float(_v[1].replace('~', '')),
                                       (int(_vd[0]) + int(_vd[-1])) / 2,
                                       float(_v[3]), _n(_v[4]), _n(_v[5]))
            break

if not _MANUAL:
    pulou('3. a categoria contra a tabela do manual — sem python-docx '
          '(pip install python-docx --break-system-packages)')
elif not _CAT or not _FICHAS:
    erro('3: sem as tabelas do §4 e do §4.1 lidas nao da para conferir a categoria')
else:
    print(f'  a tabela `Inimigos` do manual tem {len(_MANUAL)} linhas, '
          f'de nv {min(_MANUAL)} a {max(_MANUAL)}.')
    _mau3 = 0
    for _c in _FICHAS:
        if len(_c) < 4:
            continue
        _achou = [x for x in _CAT if x[0] == _c[0]]
        if not _achou:
            erro(f'3: o §4.1 publica a categoria "{_c[0]}", que nao esta na tabela do §4')
            _mau3 += 1
            continue
        _pes, _fator = _achou[0][1], _achou[0][2]
        if _pes is not None and abs(_fator - _pes / 4) > 1e-9:
            erro(f'3: a categoria {_c[0]} exige {_pes} personagem(ns) e publica fator '
                 f'{_fator}, e {_pes}/4 da {_pes / 4}')
            _mau3 += 1
        for _nv, _cel in zip((10, 20, 30), _c[1:4]):
            _nums = re.findall(r'(\d+)', _cel)
            if len(_nums) < 2:
                erro(f'3: nao consegui ler a celula "{_cel}" do §4.1')
                _mau3 += 1
                continue
            # ⚠ meio para BAIXO, pela regra declarada no §4.1 da peca. E a vida do
            # Capanga e' outra regra: o dano do grupo dividido por quatro, para baixo
            # por inteiro — um quarto de ponto poe o esquadrao vivo numa rodada a mais.
            if _pes is None:
                _ve = math.floor(_MANUAL[_nv][0] / 4)
            else:
                _ve = math.ceil(_MANUAL[_nv][1] * _fator - 0.5)
            _de = math.ceil(_MANUAL[_nv][2] * _fator - 0.5)
            if int(_nums[0]) != _ve or int(_nums[1]) != _de:
                erro(f'3: {_c[0]} no nv{_nv}: a peca publica {_nums[0]} vida e '
                     f'{_nums[1]} dano, e a linha do manual da {_ve} e {_de}')
                _mau3 += 1
    if not _mau3:
        print(f'  [x] as {len(_FICHAS)} categorias do §4.1 reconstroem da tabela do '
              'manual vezes o fator, e o Capanga do dano do grupo')
        print('  [x] os fatores reconstroem de personagens/4, onde ha personagens')


# 3.3 (v0.221): o tamanho. O alcance e' o lado da grade vezes o quadrado, e do
# `Grande` para cima o golpe pega metade num vizinho. O quadrado sai da propria
# tabela — a coluna da grade escreve os metros —, e nao daqui.
_QUAD = None
_T33 = tabela(TXT, '| tamanho | ocupa na grade | alcance | o golpe pega |')
if len(_T33) != 4:
    erro(f'3.3: achei {len(_T33)} das 4 linhas da tabela de tamanho do §3.3 — ela mudou de forma '
         'e esta checagem parou de conferir')
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
        _q = float(_mg.group(3).replace(',', '.')) / _lado
        _QUAD = _QUAD or _q
        if abs(_q - _QUAD) > 1e-9 or abs(float(_ma.group(1).replace(',', '.')) - _lado * _QUAD) > 1e-9:
            erro(f'3.3: "{_l[0]}" ocupa {_lado}×{_lado} e publica alcance {_l[2]} — o alcance e o '
                 'lado da grade vezes o quadrado')
            _mau33 += 1
        if ('metade' in _l[3]) != (_lado >= 2):
            erro(f'3.3: "{_l[0]}" ocupa {_lado}×{_lado} e a coluna dos alvos diz "{_l[3]}" — a '
                 'metade no vizinho e de quem passa de um quadrado')
            _mau33 += 1
    if 'o tamanho não cobra nada' not in TXT:
        erro('3.3: a peca parou de declarar que o tamanho nao cobra nada — sem isso ele vira '
             'preco escondido')
        _mau33 += 1
    if not _mau33:
        print('  [x] o alcance de cada tamanho e o lado da grade vezes o quadrado, e a metade no '
              'vizinho e de quem passa de um quadrado')


# --------------------------------------------------------------------------
bloco('4. AS ACOES — declaradas, e a categoria de fator 1,00 bate com o piso da peca 19')
# --------------------------------------------------------------------------
# Ate a v0.220 as acoes saiam de "personagens menos um, piso 1", e foi isso que
# quebrou a Dupla: a razao pessoas/(pessoas-1) explode embaixo. Desde a v0.221 elas
# sao DECLARADAS na tabela do §4. O que continua amarrado e' a categoria de fator
# 1,00, que e' a linha do manual sem tocar em nada: ela age o que a frase do manual
# diz, e a peca 19 §2.2 preca quatro condicoes dividindo por esse numero. Se aquele
# piso mudar, ESTA acende.
if not _CAT:
    erro('4: sem a tabela do §4 lida nao da para conferir as acoes')
else:
    _mau4 = [c[0] for c in _CAT if c[3] < 1]
    if _mau4:
        erro('4: categoria(s) que publicam menos de uma acao: ' + ', '.join(_mau4))
    _m19 = re.search(r'O chefe age `(\d+)` vezes por rodada', ler(P19))
    _um = [c for c in _CAT if c[1] is not None and abs(c[2] - 1.0) < 1e-9]
    if not _m19:
        erro('4: nao achei o piso das acoes do chefe na peca 19 §2.2 — ele e a metade '
             'de fora desta checagem, e sem ele ela so se compara com ela mesma')
    elif not _um:
        erro('4: nenhuma categoria desta peca tem fator 1,00 — a linha do manual ficou sem '
             'categoria, e a peca 19 e calibrada contra ela')
    elif _um[0][1] != 4:
        erro(f'4: a categoria de fator 1,00 exige {_um[0][1]} personagens, e a tabela do '
             'manual e a peca 19 sao calibradas para quatro')
    elif _um[0][3] != int(_m19.group(1)):
        erro(f'4: a categoria de fator 1,00 publica {_um[0][3]} acoes e a peca 19 §2.2 '
             f'publica {_m19.group(1)} — a regua de condicao daquela peca divide por esse '
             'numero, entao os dois nao podem discordar')
    elif not _mau4:
        print(f'  [x] as cinco categorias declaram ao menos uma acao, e a de fator 1,00 '
              f'({_um[0][0]}) age {_m19.group(1)} vezes, igual ao piso da peca 19 §2.2')


# --------------------------------------------------------------------------
bloco('5. O CAMBIO — medido aqui dentro, e nao guardado')
# --------------------------------------------------------------------------
# A peca publica "um chefe vale quatro capangas". O numero nao esta escrito neste
# arquivo: a simulacao de fogo concentrado roda aqui, com a vida, o dano e a
# saida do grupo lidos do manual, e o publicado tem de ser o que ela devolve.
import math as _math


def _meio_baixo(x):
    """a regra do §4.1: meio para BAIXO, e so' o meio exato — o resto arredonda normal"""
    return _math.ceil(x - 0.5) if abs(x % 1 - 0.5) < 1e-9 else round(x)


# A vida do grupo tem dono desde a v0.201, e o dono e' a ficha REAL: a media dos
# cinco Caminhos da peca 1 §5.1 com Constituicao 3, que e' a coluna em que aquela
# secao faz a propria calibragem. Ate a v0.200 a peca 26 usava DOIS modelos em
# secoes vizinhas — 243 no §4.6 e 252 no §5 e no §6.3 —, e nenhum dos dois estava
# declarado. Nada esta escrito aqui: a curva e' lida da peca 1.
_CAM = re.findall(r'\|\s*\*\*(\w+)\*\*\s*\|\s*d(\d+)\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|',
                  ler(os.path.join(AQUI, '01-atributos-acerto-defesa.md')))
if len(_CAM) != 5:
    erro('5.1: nao achei os cinco Caminhos na tabela de vida da peca 1 §5.1 — a vida do '
         'grupo sai dela e nao daqui')
    _V1 = _VN = 0.0
else:
    _V1 = sum(int(c[2]) for c in _CAM) / 5
    _VN = sum(int(c[3]) for c in _CAM) / 5
_CON_TIPICA = 3


def _VIDA_PC(nv):
    return _V1 + _VN * (nv - 1) + _CON_TIPICA * nv


# v0.221: com as formas femininas. A 9.5 le "carrega (\w+) `Intervenções`", e o arnes
# achou que "duas Intervenções" fazia a checagem dizer que nao tinha lido a peca.
_NUM_PT = {'um': 1, 'uma': 1, 'dois': 2, 'duas': 2, 'três': 3, 'quatro': 4, 'cinco': 5,
           'seis': 6, 'sete': 7, 'oito': 8, 'nove': 9, 'dez': 10}


def _simula(saida, corpos):
    vs = [list(c) for c in corpos]
    rod = 0
    cobrado = 0.0
    while vs and rod < 100:
        cobrado += sum(c[1] for c in vs)
        sobra = saida
        while sobra > 0 and vs:
            if vs[0][0] <= sobra:
                sobra -= vs.pop(0)[0]
            else:
                vs[0][0] -= sobra
                sobra = 0
        rod += 1
    return rod, cobrado


_m5 = re.search(r'vale (\w+) capangas', TXT)
if not _m5:
    erro('5: a peca nao publica o cambio como "vale N capangas" — a frase mudou de '
         'forma e esta checagem ficou sem o outro lado')
elif not _MANUAL:
    pulou('5. o cambio contra a simulacao — a tabela do manual nao foi lida')
elif _CAPA is None:
    erro('5: sem a linha do Capanga no §4 nao da para derivar o capanga')
else:
    _pub5 = _NUM_PT.get(_m5.group(1).lower())

    # v0.221: o capanga e' o da ESCADA — a vida e' o dano do grupo dividido por quatro,
    # para baixo, e o dano e' o do chefe vezes o fator da categoria dele. Ate a v0.220
    # ele era o da Alcateia (vida do chefe ÷ 4, dano ÷ 3), e esta checagem conferia
    # justamente aquilo. Nada aqui e' escrito: a saida do grupo e o chefe saem do
    # manual, e o fator sai da linha do Capanga no §4.
    def _capanga(nv):
        return (math.floor(_MANUAL[nv][0] / 4), _meio_baixo(_MANUAL[nv][2] * _CAPA[2]))

    _medidos = []
    for _nv, (_saida, _cv, _cd, _kv, _kd) in sorted(_MANUAL.items()):
        _r0, _t0 = _simula(_saida, [(_cv, _cd)])
        _k = _capanga(_nv)
        _melhor = min(range(1, 13),
                      key=lambda n: abs(_simula(_saida, [_k] * n)[1] - _t0))
        _medidos.append((_nv, _melhor))
    print('  cambio medido por nivel: ' + ' · '.join(f'nv{n}:{m}' for n, m in _medidos))
    _valores = sorted({m for _, m in _medidos})
    if _pub5 is None:
        erro(f'5: nao entendi "{_m5.group(1)}" como numero por extenso')
    elif _valores != [_pub5]:
        erro(f'5: a peca publica {_pub5} capangas por chefe, e a simulacao devolve '
             f'{_valores} nos {len(_medidos)} niveis da tabela do manual')
    else:
        print(f'  [x] a simulacao devolve {_pub5} em todos os niveis, e e o que a peca '
              'publica')

    # a declaracao que sobreviveu a decisao — a guarda da v0.206 continua: prosa que
    # diz que uma faixa nao tem capanga le-se como regra viva.
    if any(('não tem capanga' in _l or 'sem capanga' in _l) and not _l.lstrip().startswith('|')
           for _l in TXT.split('\n')):
        erro('5: a peca declara em prosa que uma faixa nao tem capanga — e o capanga da '
             'escada existe em todas, porque sai do dano do grupo')

    if not ('Vida do capanga = o dano do grupo por rodada dividido por quatro' in TXT
            and 'Dano do capanga = o dano do chefe vezes o fator da categoria' in TXT):
        erro('5: a peca nao publica as duas linhas da derivacao do capanga — sem elas '
             'a coluna volta a ser numero solto que ninguem reconstroi')

    # o capanga que a tabela `Inimigos` do MANUAL publica tem de ser este. E' a coluna
    # que o gerador do bloco copia, entao um capanga morto ali chega na mao do mestre.
    _fora, _sem = [], []
    for _nv, (_saida, _cv, _cd, _kv, _kd) in sorted(_MANUAL.items()):
        if _kv is None or _kd is None:
            _sem.append(_nv)
            continue
        _ev, _ed = _capanga(_nv)
        if (_kv, _kd) != (_ev, _ed):
            _fora.append(f'nv{_nv}: o manual da ({_kv:.0f}, {_kd:.0f}) e o capanga da '
                         f'escada e ({_ev}, {_ed})')
    if _sem:
        erro(f'5: a tabela do manual tem {len(_sem)} faixa(s) sem capanga, e o capanga da '
             'escada existe em todas')
    if _fora:
        erro('5: o capanga da tabela `Inimigos` do manual nao e o da escada — '
             + ' · '.join(_fora[:3]))
    elif not _sem:
        print(f'  [x] o capanga do manual e o da escada nas {len(_MANUAL)} faixas — o dano '
              'do grupo ÷ 4, para baixo, e o dano do chefe vezes o fator')

    # -- 5.1: a coluna da sub-categoria, recontada -----------------------------
    # Desde a v0.221 com uma casa decimal: meio ponto percentual na fracao do chefe
    # atravessa a borda de uma rodada. A ordem de abate continua declarada.
    _ordem_declarada = 'os capangas primeiro' in TXT
    _m51 = re.findall(r'\|\s*\*\*`(sozinho|com um apoio|com dois|bando)`\*\*\s*\|\s*'
                      r'`([\d,]+)%`\s*\|\s*`?([\d—]+)`?\s*\|\s*`([\d,]+)%`\s*\|', TXT)
    if not _ordem_declarada:
        erro('5.1: a peca publica a coluna da sub-categoria e nao declara em que ordem o '
             'grupo abate — a coluna muda com a ordem')
    elif len(_m51) != 4:
        erro(f'5.1: achei {len(_m51)} das 4 linhas da tabela de sub-categoria do §4.5 — '
             'ela mudou de forma e esta checagem parou de conferir')
    elif 30 not in _MANUAL:
        pulou('5.1. a sub-categoria — a linha do nivel 30 do manual nao foi lida')
    else:
        _saida, _cv, _cd, _kv, _kd = _MANUAL[30]
        _vg = 4 * _VIDA_PC(30)
        _k = _capanga(30)
        _mau51 = 0
        for _rot, _frac, _ncap, _pct in _m51:
            _f = float(_frac.replace(',', '.')) / 100.0
            _n = 0 if _ncap == '—' else int(_ncap)
            _r, _c = _simula(_saida, [_k] * _n + [(_cv * _f, _cd * _f)])
            _esp = _c / _vg * 100
            if abs(_esp - float(_pct.replace(',', '.'))) > 0.051:
                erro(f'5.1: a sub-categoria `{_rot}` publica {_pct}% da vida do grupo e a '
                     f'simulacao devolve {_esp:.1f}%')
                _mau51 += 1
        if not _mau51:
            print('  [x] as quatro formas da sub-categoria reconstroem da simulacao, com '
                  'os capangas abatidos primeiro e o Capanga da escada')

    # -- 5.2: a linha do manual obedece a regra que a propria secao escreve ----
    # v0.206, e ela nasceu porque a linha do nivel 2 estava um ponto fora e nada
    # olhava para isso. A secao `Inimigos` do manual escreve a regra em prosa —
    # o chefe tem "cerca de tres vezes o dano de rodada do grupo em vida, e e
    # isso que faz a luta contra ele durar tres rodadas" — e a tabela ao lado
    # dela publicava 115 onde a regra pede 114.
    #
    # UM PONTO DE VIDA custava uma rodada inteira: com 115 a luta dura 3,03
    # rodadas, rodada e' inteira na mesa, e o chefe agia quatro vezes. O encontro
    # cobrava 89% da vida do grupo contra os 68% das outras seis linhas.
    #
    # Os dois numeros — o multiplicador e a duracao — sao LIDOS da prosa do
    # manual, por extenso. Nenhum dos dois esta escrito aqui: trocar a prosa
    # move a checagem junto, que e' o que separa esta de uma constante.
    _PAL = {'uma': 1, 'duas': 2, 'três': 3, 'tres': 3, 'quatro': 4, 'cinco': 5}
    _prosa = None
    if docx is not None and os.path.isfile(DOCX):
        _txts = [_p.text for _p in docx.Document(DOCX).paragraphs]
        for _t in _txts:
            if 'vezes o dano de rodada do grupo em vida' in _t:
                _prosa = _t
                break
    _mmult = re.search(r'cerca de (\w+) vezes o dano de rodada do grupo em vida',
                       _prosa or '')
    _mdur = re.search(r'durar (\w+) rodadas', _prosa or '')
    if _prosa is None:
        pulou('5.2. a linha do manual contra a regra que ela escreve — a prosa da secao '
              '`Inimigos` nao foi lida')
    elif not _mmult or not _mdur:
        erro('5.2: a prosa da secao `Inimigos` do manual mudou de forma e esta checagem '
             f'parou de achar o multiplicador e a duracao nela: "{_prosa[:90]}"')
    elif _mmult.group(1).lower() not in _PAL or _mdur.group(1).lower() not in _PAL:
        erro(f'5.2: nao entendi "{_mmult.group(1)}" ou "{_mdur.group(1)}" como numero por '
             'extenso — a prosa do manual e a dona dos dois')
    else:
        _MULT = _PAL[_mmult.group(1).lower()]
        _DUR = _PAL[_mdur.group(1).lower()]
        _fora52 = []
        for _nv, (_s, _cv, _cd, _kv, _kd) in sorted(_MANUAL.items()):
            _esp = _MULT * _s
            _inteiras = math.ceil(_cv / _s - 1e-9)
            if abs(_cv - _esp) > 0.51 or _inteiras != _DUR:
                _fora52.append(f'nv{_nv}: o meio da faixa e {_cv:.0f}, a regra pede '
                               f'{_esp:.0f}, e a luta sai em {_inteiras} rodada(s) '
                               f'inteira(s) contra as {_DUR} que a prosa promete')
        if _fora52:
            erro(f'5.2: a tabela `Inimigos` desobedece a regra que a prosa dela escreve — '
                 + ' · '.join(_fora52))
        else:
            print(f'  [x] as {len(_MANUAL)} linhas do manual tem o meio da faixa em '
                  f'{_MULT} × a saida do grupo, e as {len(_MANUAL)} lutas saem em {_DUR} '
                  'rodadas inteiras — o numero e a duracao lidos da prosa da secao')


# --------------------------------------------------------------------------
bloco('6. O GRAU NAO VIRA NUMERO — nem aqui nem na peca que decide isso')
# --------------------------------------------------------------------------
# A decisao do §2 e' que o grau e' rotulo de ficcao. A checagem cobra os dois
# lados: nenhuma linha viva desta peca pode pendurar valor nele, e a peca 12, que
# e' a dona de "Grau e reconhecimento; nivel e poder", tem de continuar dizendo.
_LINHAS_GRAU = [l for l in TXT.split('\n')
                if re.search(r'\bgrau\b', l, re.I) and re.search(r'`\d', l)
                and not l.lstrip().startswith('>')]
if _LINHAS_GRAU:
    erro(f'6: {len(_LINHAS_GRAU)} linha(s) viva(s) desta peca falam de grau e carregam '
         'numero em crase — o §2 decide que ele e rotulo. Primeira: '
         + _LINHAS_GRAU[0].strip()[:90])
else:
    print('  [x] nenhuma linha viva desta peca pendura numero no grau')

if 'Grau é reconhecimento; nível é poder' not in ler(P12):
    erro('6: a peca 12 parou de publicar "Grau e reconhecimento; nivel e poder", que e '
         'a decisao em que o §2 desta peca se apoia — se ela caiu, esta peca precisa '
         'de outro argumento')
else:
    print('  [x] a peca 12 continua sendo a dona de "Grau e reconhecimento; nivel e poder"')


# --------------------------------------------------------------------------
bloco('7. NENHUM VALOR DE REGRA GUARDADO AQUI DENTRO')
# --------------------------------------------------------------------------
# A promessa do cabecalho. O que sobra de constante neste arquivo tem de ser
# FORMATO — a conversao de numero por extenso, os niveis que a tabela publica —
# e nunca valor de regra.
_FONTE = open(__file__, encoding='utf-8').read()
_achou7 = False
for _pad, _que in ((r'^\s*(VIDA|DANO|CAMBIO|FATOR|ACOES)_?\w*\s*=\s*[\d.]', 'valor de ficha'),
                   (r'^\s*CHEFE\s*=\s*[\d.]', 'o chefe'),
                   (r'^\s*CAPANGA\s*=\s*[\d.]', 'o capanga')):
    if re.search(_pad, _FONTE, re.M):
        erro(f'7: tem {_que} escrito como constante neste arquivo — ele tem de sair do '
             'documento dono')
        _achou7 = True
if not _achou7:
    print('  [x] a vida, o dano, o cambio e os fatores saem dos donos, e nenhum '
          'esta escrito aqui')
if len(_MEIO) < 8:
    erro('7: a curva de refino nao foi lida da peca 11 — ela rodou com o valor de '
         'formato deste arquivo')
else:
    print('  [x] a curva do `meio a meio` foi lida da peca 11: '
          + ' '.join(str(_MEIO[k]) for k in sorted(_MEIO)))


# --------------------------------------------------------------------------
# 7.1 (v0.204, reescrita na v0.205): a Expansao de Dominio do inimigo. Ela nao
# acrescenta dano — o §6.1 poe tudo na cota —, e o que ela faz e' o Acerto parar
# de rolar. O preco e' a razao entre acertar sempre e acertar 52%, e a categoria
# mede exatamente a coisa que essa razao move: quantos personagens ele exige.
#
# ⚠ A primeira forma desta checagem media so' para BAIXO e cobrava que a peca
# declarasse em que categorias a Expansao "nao cabe". Isso vinha de um erro da
# peca, achado pelo Mizuki: nao existir degrau abaixo da Calamidade nao proibe
# ela de ter dominio — so' quer dizer que o encontro fica maior, e o numero
# existe fora da escada porque a categoria mede PESSOAS.
_mexp = re.search(r'multiplica a saída efetiva dele por `1 ÷ ([\d,]+)`, que é `([\d,]+) ×`', TXT)
if not _mexp:
    erro('7.1: a peca nao publica o multiplicador da Expansao como "1 ÷ acerto" — sem '
         'isso ele vira numero solto, e ele e o preco inteiro da regra')
else:
    _ac = float(_mexp.group(1).replace(',', '.'))
    _mult_pub = float(_mexp.group(2).replace(',', '.'))
    if abs(1 / _ac - _mult_pub) > 0.01:
        erro(f'7.1: a peca publica {_mult_pub:.2f}x e 1 ÷ {_ac:.2f} da {1/_ac:.2f}')
    _mb = re.search(r'ele acerta `(\d+)%` a `(\d+)%`', TXT)
    if not _mb:
        erro('7.1: nao achei a banda de acerto do §3.1 — o multiplicador da Expansao se '
             'mede contra ela')
    elif not (int(_mb.group(1)) <= _ac * 100 <= int(_mb.group(2))):
        erro(f'7.1: a Expansao usa acerto {_ac:.0%} e o §3.1 publica a banda '
             f'{_mb.group(1)}% a {_mb.group(2)}%')
    else:
        print(f'  [x] o multiplicador da Expansao ({_mult_pub:.2f}x) e 1 ÷ o acerto do '
              f'§3.1, e o acerto cai dentro da banda publicada')

    # v0.221: a regra deixou de arredondar o multiplicador para "dobra". A moeda e' o
    # FATOR, que e' continuo, e a peca publica a regra e a tabela de pessoas. A tabela
    # tem de ser a coluna de personagens do §4 vezes o multiplicador, com uma casa.
    _mreg = re.search(r'Uma Expansão de Domínio completa multiplica o fator do inimigo por '
                      r'`([\d,]+)`', TXT)
    if not _mreg:
        erro('7.1: a peca parou de publicar a regra da Expansao como "multiplica o fator '
             'do inimigo por N" — sem ela a tabela vira numero solto')
    elif abs(float(_mreg.group(1).replace(',', '.')) - _mult_pub) > 1e-9:
        erro(f'7.1: a regra publica {_mreg.group(1)} e a conta do §6.4 da {_mult_pub:.2f}')
    else:
        _pes = {c[0]: c[1] for c in _CAT if c[1] is not None}
        _dob = {}
        for _l in TXT.split('\n'):
            _m = re.match(r'\|\s*\*\*`(\w+)`\*\*\s*\|\s*`(\d+)`\s*\|\s*`([\d,]+)`\s*\|\s*$', _l)
            if _m and _m.group(1) in _pes:
                _dob[_m.group(1)] = (int(_m.group(2)), float(_m.group(3).replace(',', '.')))
        if not _pes or len(_dob) != len(_pes):
            erro(f'7.1: li {len(_pes)} categorias com personagens no §4 e {len(_dob)} na '
                 'tabela do §6.4 — alguma mudou de forma')
        else:
            _mau = 0
            for _n, (_p, _c) in _dob.items():
                if _p != _pes[_n]:
                    erro(f'7.1: o §6.4 diz que a `{_n}` exige {_p} personagens e o §4 diz '
                         f'{_pes[_n]}')
                    _mau += 1
                elif abs(_c - round(_p * _mult_pub, 1)) > 1e-9:
                    erro(f'7.1: a `{_n}` exige {_p} e com Expansao o §6.4 publica {_c}, e '
                         f'{_p} × {_mult_pub:.2f} da {round(_p * _mult_pub, 1)}')
                    _mau += 1
            if not _mau:
                print(f'  [x] a tabela do §6.4 e a coluna de personagens do §4 vezes '
                      f'{_mult_pub:.2f}, nas {len(_dob)} categorias que tem personagens')


# --------------------------------------------------------------------------
# 7.1b (v0.229): os gates da Expansao de inimigo, e a Expansao sem Barreiras.
# Decisao do Mizuki: os gates sao os do jogador, e o refino acima da curva e'
# desvio com causa escrita, que se paga no fator pela Defesa. Tres coisas se
# conferem, e nenhum valor mora aqui:
#   a) os gates publicados sao os do manual (partE.js, a tabela dos tres degraus);
#   b) no nivel do gate da completa, a duracao pela curva do `meio a meio` (peca 11)
#      cobre a luta que a categoria promete, e o multiplicador abaixo dele e' o que
#      a peca publica; a sem barreiras usa o mesmo multiplicador da completa;
#   c) a tabela do desvio reconstroi: a Defesa ganha sai da protecao da peca 11, e
#      o fator sai do acerto do personagem e dos pontos por Defesa do §3.4.
PARTE = 'manual/gerador/partE.js'
_E, _P11 = ler(PARTE), ler(P11)
_gc = re.search(r"\['Completa', '[^']*', 'nível (\d+) e refino (\d+)'", _E)
_gs = re.search(r"\['Sem Barreiras', '[^']*', 'refino (\d+)", _E)
_gp = re.search(r'A completa abre no nível `(\d+)` com refino `(\d+)`, e a Expansão sem Barreiras pede refino `(\d+)`', TXT)
_marc = re.search(r'\| \| nv 6 \|[^\n]*', _P11)
_mm = re.search(r'\| \*\*meio a meio\*\* \|[^\n]*', _P11)
_prot = re.search(r'a sua proteção é `1/(\d+) do refino \+ (\d+)`', _P11)
_luta = re.search(r'contra as `(\d+),(\d+)` que a categoria promete', TXT)
_pp = re.search(r'um ponto de Defesa move `(\d+)` pontos percentuais, e o personagem acerta alvo difícil em `(\d+)%`', TXT)
_mx = re.search(r'multiplica a saída efetiva dele por `1 ÷ ([\d,]+)`, que é `([\d,]+) ×`', TXT)
if not (_gc and _gs):
    erro('7.1b: nao achei os gates na tabela dos tres degraus do manual (partE.js)')
elif not _gp:
    erro('7.1b: a peca parou de publicar os gates da Expansao de inimigo')
elif not (_marc and _mm and _prot and _luta and _pp and _mx):
    erro('7.1b: faltou dono — a curva do meio a meio, a protecao da peca 11, a luta, '
         'o acerto do personagem ou o multiplicador do §6.4')
else:
    _ruins = []
    if (int(_gp.group(1)), int(_gp.group(2)), int(_gp.group(3))) != (int(_gc.group(1)), int(_gc.group(2)), int(_gs.group(1))):
        _ruins.append(f'a peca publica os gates {_gp.groups()} e o manual diz {(_gc.group(1), _gc.group(2), _gs.group(1))}')
    NVS = [int(x) for x in re.findall(r'nv (\d+)', _marc.group(0))]
    RFS = [int(x) for x in re.findall(r'`(\d+)`', _mm.group(0))]
    CURVA = dict(zip(NVS, RFS))
    NV_C, RF_C, RF_S = int(_gc.group(1)), int(_gc.group(2)), int(_gs.group(1))
    DIV, SOMA = int(_prot.group(1)), int(_prot.group(2))
    LUTA = float(f'{_luta.group(1)}.{_luta.group(2)}')
    PP, PC = int(_pp.group(1)), int(_pp.group(2))
    MULT = 1 / float(_mx.group(1).replace(',', '.'))
    dur = lambda r: max(1, r // 2)
    # b) a duracao no gate e abaixo dele
    _db = re.search(r'o nível `(\d+)` dá refino `(\d+)` e `(\d+)` rodadas de domínio, contra a luta de `(\d+),(\d+)`', TXT)
    _ab = re.search(r'No nível `(\d+)` seriam `(\d+)` rodadas, e o multiplicador cairia para `(\d+),(\d+)`', TXT)
    if not (_db and _ab):
        erro('7.1b: a peca parou de publicar a duracao no gate e o multiplicador abaixo dele')
    else:
        _nv, _rf, _d = int(_db.group(1)), int(_db.group(2)), int(_db.group(3))
        if _nv != NV_C or CURVA.get(_nv) != _rf or dur(_rf) != _d:
            _ruins.append(f'no gate a peca diz nivel {_nv}, refino {_rf}, {_d} rodadas; a curva e o manual dao '
                          f'nivel {NV_C}, refino {CURVA.get(NV_C)}, {dur(CURVA.get(NV_C, 0))} rodadas')
        _curtos = [n for n in NVS if n >= NV_C and CURVA[n] >= RF_C and dur(CURVA[n]) < LUTA]
        if _curtos:
            _ruins.append(f'do gate para cima a duracao fica abaixo da luta de {LUTA} nos niveis {_curtos}')
        _na, _da = int(_ab.group(1)), int(_ab.group(2))
        _ma = float(f'{_ab.group(3)}.{_ab.group(4)}')
        _conta = round(1 + (MULT - 1) * min(1, dur(CURVA.get(_na, 0)) / LUTA), 2)
        if dur(CURVA.get(_na, 0)) != _da or abs(_conta - _ma) > 1e-9 or _na >= NV_C:
            _ruins.append(f'abaixo do gate a peca diz nivel {_na}, {_da} rodadas, x{_ma}; a conta da '
                          f'{dur(CURVA.get(_na, 0))} rodadas e x{_conta}')
    # b) a sem barreiras usa o mesmo multiplicador, e o nivel em que a curva chega ao teto
    _sm = re.search(r'\*\*Ela multiplica o fator pelo mesmo `([\d,]+)`\.\*\*', TXT)
    _st = re.search(r'o inimigo só chega a refino `(\d+)` no nível `(\d+)`', TXT)
    if not (_sm and _st):
        erro('7.1b: a peca parou de publicar o multiplicador da sem barreiras ou o nivel do teto na curva')
    else:
        if f'{MULT:.2f}'.replace('.', ',') != _sm.group(1):
            _ruins.append(f'a sem barreiras publica x{_sm.group(1)} e a completa e x{MULT:.2f}')
        _prim = min((n for n in NVS if CURVA[n] >= RF_S), default=None)
        if int(_st.group(1)) != RF_S or int(_st.group(2)) != _prim:
            _ruins.append(f'a peca diz refino {_st.group(1)} no nivel {_st.group(2)}; a curva chega a {RF_S} no nivel {_prim}')
    # c) a tabela do desvio
    _linhas = re.findall(r'^\| nv `(\d+)` \| `(\d+)` \| `\+(\d+)` \| `× (\d+),(\d+)` \|$', TXT, re.M)
    _esperados = [n for n in NVS if n >= NV_C and CURVA[n] >= RF_C and CURVA[n] < RF_S]
    if [int(l[0]) for l in _linhas] != _esperados:
        _ruins.append(f'a tabela do desvio tem os marcos {[int(l[0]) for l in _linhas]} e devia ter {_esperados} '
                      f'(do gate da completa ate a curva chegar ao refino {RF_S})')
    prot = lambda r: r // DIV + SOMA
    for _n, _r, _g, _a, _b in _linhas:
        _n, _r, _g = int(_n), int(_r), int(_g)
        _ganho = prot(RF_S) - prot(CURVA.get(_n, 0))
        _fat = round(PC / (PC - PP * _ganho), 2)
        if CURVA.get(_n) != _r or _ganho != _g or abs(_fat - float(f'{_a}.{_b}')) > 1e-9:
            _ruins.append(f'no nv{_n} a tabela diz refino {_r}, Defesa +{_g}, x{_a},{_b}; a conta da refino '
                          f'{CURVA.get(_n)}, Defesa +{_ganho}, x{_fat:.2f}')
    # v0.229: a Expansao aumenta o encontro e nao se compensa (decisao do Mizuki). O jeito
    # antigo de manter o tamanho dividia o golpe pelo multiplicador, e isso tirava o golpe
    # da banda do Bestiario — esta guarda impede ele de voltar.
    if re.search(r'[Dd]ivida o dano por rodada dele por|Quer manter o tamanho\?', TXT):
        _ruins.append('a peca voltou a oferecer manter o tamanho dividindo o dano pelo multiplicador da Expansao — '
                      'isso tira o golpe da banda do Bestiario, e saiu na v0.229')
    if _ruins:
        for _r in _ruins:
            erro('7.1b: ' + _r)
    else:
        print(f'  [x] os gates da peca sao os do manual: completa no nivel {NV_C} com refino {RF_C}, sem barreiras no refino {RF_S}')
        print(f'  [x] no gate a curva da {dur(CURVA[NV_C])} rodadas contra a luta de {LUTA}, e nenhum marco acima fica curto')
        print(f'  [x] a sem barreiras multiplica pelo mesmo x{MULT:.2f}, e a curva so chega ao refino {RF_S} no nivel {_prim}')
        print(f'  [x] a tabela do desvio reconstroi nos {len(_linhas)} marcos, com a protecao 1/{DIV} + {SOMA} e {PP} pontos por Defesa')


# --------------------------------------------------------------------------
bloco('8. RESISTENCIA E VIDA ESCONDIDA — e o fator da categoria e a moeda dela')
# --------------------------------------------------------------------------
# v0.199. A peca 19 §4 divide os catorze tipos em tres grupos com peso, e
# resistir corta pela metade o que entra por aquele grupo. Isso sobe a VIDA
# EFETIVA do inimigo, e a categoria nao sabia disso: um chefe de Alcateia imune
# a Fisicos joga uma luta de 9 rodadas onde a categoria promete 3,7.
#
# Nada esta escrito aqui: os pesos saem da peca 19, os fatores saem do §4 desta
# peca, e os multiplicadores sao recalculados. O mecanismo e o do Guia do Mestre
# de 2014, que tem tabela de Pontos de Vida Efetivos fazendo o mesmo.
_PESOS = {}
for _l in tabela(ler(P19), '| grupo | tipos | do dano recebido |'):
    if len(_l) >= 3 and _l[2].endswith('%'):
        _PESOS[_l[0]] = int(_l[2].rstrip('%')) / 100.0

if not _PESOS:
    erro('8: nao achei a tabela dos tres grupos de dano na peca 19 §4 — ela e a dona '
         'do peso, e sem ele nao da para dizer quanto uma resistencia vale')
else:
    print('  pesos lidos da peca 19 §4: '
          + ' · '.join(f'{k} {v:.0%}' for k, v in _PESOS.items()))

    def _efetiva(frac, modo):
        poupa = frac * 0.5 if modo == 'resistência' else (frac if modo == 'imunidade'
                                                          else -frac)
        return 1.0 / (1.0 - poupa)

    _T8 = tabela(TXT, '| grupo | peso | resistência | imunidade | vulnerabilidade |')
    _mau8 = 0
    for _l in _T8:
        if len(_l) < 5 or not _l[1].endswith('%'):
            continue
        _peso = int(_l[1].rstrip('%')) / 100.0
        if _l[0] in _PESOS and abs(_PESOS[_l[0]] - _peso) > 1e-9:
            erro(f'8: a peca publica peso {_l[1]} para o grupo {_l[0]} e a peca 19 §4 '
                 f'diz {_PESOS[_l[0]]:.0%}')
            _mau8 += 1
        for _cel, _modo in zip(_l[2:5], ('resistência', 'imunidade', 'vulnerabilidade')):
            _m = re.match(r'([\d,]+)', _cel)
            if not _m:
                erro(f'8: nao consegui ler "{_cel}" na linha {_l[0]}')
                _mau8 += 1
                continue
            _pub = float(_m.group(1).replace(',', '.'))
            _esp = round(_efetiva(_peso, _modo), 2)
            if abs(_pub - _esp) > 0.011:
                erro(f'8: {_l[0]}, {_modo}: a peca publica {_pub:.2f}x e a conta da '
                     f'{_esp:.2f}x')
                _mau8 += 1
    if not _T8:
        erro('8: nao achei a tabela de vida efetiva do §6.3 — ela mudou de forma e '
             'esta checagem parou de conferir')
    elif not _mau8:
        print(f'  [x] as {len(_T8)} linhas do §6.3 reconstroem de 1 ÷ (1 − o que se poupa)')

    # v0.221: a moeda deixou de ser o degrau de categoria — na escada viva ele vai de
    # 1,000x a 4,000x — e passou a ser o FATOR. A peca tem de declarar a moeda, e o
    # multiplicador que ela declara tem de ser o que a conta de cima devolve.
    if 'Físicos' in _PESOS:
        _res_fis = round(_efetiva(_PESOS['Físicos'], 'resistência'), 2)
        _imu_fis = round(_efetiva(_PESOS['Físicos'], 'imunidade'), 2)
        _mr = re.search(r'Resistência ao grupo `Físicos` multiplica o fator da categoria por '
                        r'`([\d,]+)`', TXT)
        _mi = re.search(r'Imunidade a `Físicos` multiplica o fator por `([\d,]+)`', TXT)
        if not _mr or not _mi:
            erro('8: a peca nao declara em que moeda a resistencia se paga — sem isso '
                 'ela e vida de graca, e a categoria passa a mentir sobre o encontro')
        elif (abs(float(_mr.group(1).replace(',', '.')) - _res_fis) > 0.011
              or abs(float(_mi.group(1).replace(',', '.')) - _imu_fis) > 0.011):
            erro(f'8: a peca declara que resistir aos Físicos multiplica o fator por '
                 f'{_mr.group(1)} e ser imune por {_mi.group(1)}, e a conta da '
                 f'{_res_fis:.2f} e {_imu_fis:.2f}')
        else:
            print(f'  [x] a peca declara a moeda, o fator, e os multiplicadores declarados '
                  f'sao os da conta: resistir {_res_fis:.2f}x, ser imune {_imu_fis:.2f}x')


# --------------------------------------------------------------------------
bloco('9. O CATALOGO DO JOGADOR NA FICHA DO INIMIGO — o cambio do §6.5')
# --------------------------------------------------------------------------
# v0.205. A peca deixou de prometer um catalogo de tracos proprio e passou a
# dizer o preco das entradas que o jogador ja tem — decisao do Mizuki, "da pra
# deixar ser que nem do sistema pra player, mas rebalancear".
#
# Sao TRES portas e tres moedas, e esta checagem confere as tres separadas,
# porque cada uma se mede contra um dono diferente:
#
#   a tecnica  -> o orcamento de feitico da acao, que sai do golpe do §4.4
#                 dividido pelo que um ponto de feitico vale (peca 19 §2.1)
#   a aptidao  -> a cota de dano por rodada, pelo cambio de PE da peca 5 §4
#   vida efetiva -> um degrau de categoria, e a checagem 8 ja e' dona disso
#
# NENHUM valor esta escrito aqui. O ponto de feitico, o piso da Classe 1, o
# cambio de PE, a maior Classe por nivel e o custo de cada aptidao sao todos
# lidos do documento dono, e a tabela da peca e' recontada contra eles.
P05 = 'sistema/03-mecanica/05-caminho-e-combate-sem-feitico.md'
P18 = 'sistema/03-mecanica/18-progressao.md'
_T19 = ler(P19)

# quanto vale um ponto de feitico em dano — a mesma frase que a peca 19 §2.1 le
# do manual, e a peca 26 §6.5 cita ao converter o golpe em orcamento.
_mp = re.search(r'vira `1d8` de dano — que são `([\d,]+)`', _T19)
# o piso: o menor feitico do manual, lido da tabela de preco do §2.1
_ESC19 = {}
for _l19 in tabela(_T19, '| Classe | `Leve` | `Média` | `Pesada` | Rotina |'):
    if len(_l19) >= 5 and _l19[0].isdigit():
        _ESC19[int(_l19[0])] = int(_l19[4])
# a maior Classe por nivel, da tabela de progressao da peca 18
_CL18 = {}
for _l18 in ler(P18).split('\n'):
    _m18 = re.match(r'\|\s*\*{0,2}(\d+)\*{0,2}\s*\|\s*[\d.—]+\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|'
                    r'\s*(\d+)\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|', _l18)
    if _m18:
        _CL18[int(_m18.group(1))] = int(_m18.group(5))
# o cambio de PE, do DONO dele: a linha de orcamento da peca 5 §4
_mpe = re.search(r'recuperar `\+1` PE \| permanente \| `([\d,]+)`', ler(P05))

if not _mp:
    erro('9: nao achei na peca 19 §2.1 quanto vale um ponto de feitico em dano — sem '
         'ele o orcamento do §6.5 nao reconstroi de nada')
elif not _ESC19:
    erro('9: nao achei a tabela de preco por Classe na peca 19 §2.1 — ela e a dona do '
         'piso, e sem ela nao da para dizer abaixo de que o inimigo nao conjura')
elif not _mpe:
    erro('9: nao achei o cambio de PE na peca 5 §4 — a linha `recuperar +1 PE` '
         'permanente e a dona dele, e o §6.5 se apoia nela')
elif not _CL18:
    erro('9: nao achei a tabela de progressao da peca 18 — a maior Classe por nivel '
         'sai dela, e sem ela a conta da aptidao nao fecha')
else:
    _PONTO = float(_mp.group(1).replace(',', '.'))
    _PISO19 = _ESC19[min(_ESC19)]
    _CAMBIO = float(_mpe.group(1).replace(',', '.'))
    print(f'  um ponto de feitico vale {_PONTO} de dano (peca 19 §2.1); o menor feitico '
          f'do manual custa {_PISO19} pontos.')
    print(f'  e 1 PE por rodada vale {_CAMBIO} de dano por rodada (peca 5 §4).')

    # -- 9.1: a tabela de orcamento de feitico do §6.5 -----------------------
    # Ela e' o golpe do §4.4 em outra unidade, e o golpe entra ja arredondado
    # pela regra do §4.1 — e' o numero que a ficha imprime. Sem isso a checagem
    # compararia contra um produto cru que o mestre nunca ve.
    # v0.221: o golpe entra como a ficha imprime ele — a MEDIA do dado do §4.4 — e
    # quem carrega `Intervencao` entra com o fator dela.
    # 11/09/2026: a conta era a rota A (o fator DEPOIS da media do golpe cru), e o
    # texto da peca descrevia a rota B. Medido em `medir-a-rota-do-orcamento.py`:
    # a rota B fecha com o texto, com o comentario daqui e com a regra do cap. 6 do
    # livro aplicada ao golpe que a mesa le. 9 das 35 celulas andaram 0,1. Nada mora aqui: a lista de
    # dados, o teto de dados na mao e o piso do numero seco saem do §4.4; o fator e
    # quem o carrega saem do §6.5 e da coluna `Intervencao` da tabela do §4.
    _T91 = tabela(TXT, '| pontos por ação | `Capanga` | `Ameaça` | `Desastre` | `Catástrofe` | `Calamidade` |')
    _mdl = re.search(r'O tamanho do dado se escolhe entre ([^*]+?)\s*—', TXT)
    _DL = [int(x) for x in re.findall(r'`d(\d+)`', _mdl.group(1))] if _mdl else []
    _mteto = re.search(r'no máximo \*\*(\w+)\*\* dados', TXT)
    _TETO_D = _NUM_PT.get(_mteto.group(1).lower()) if _mteto else None
    _mseco = re.search(r'Abaixo de `(\d+)` o golpe fica em número seco', TXT)
    _mfi = re.search(r'o fator de dano de quem carrega `Intervenção` é multiplicado por `([\d,]+)`', TXT)
    _FI = float(_mfi.group(1).replace(',', '.')) if _mfi else None

    def _jr(x):
        return math.floor(x + 0.5)            # o Math.round do gerador

    def _arr(x):
        return math.ceil(x - 0.5)             # o meio para baixo do §4.1

    def _media_do_dado(alvo):
        """a regra do §4.4, na mesma ordem de desempate do gerador do bloco"""
        if alvo < int(_mseco.group(1)):
            return float(_arr(alvo))
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
                bom = (inte, er, n, med, _jr(fixo))
        if bom is None:
            n = max(1, _jr(alvo / 9))
            return n * (8 + 1) / 2 + max(_arr(alvo - n * (8 + 1) / 2), 0)
        return bom[2] * bom[3] + max(bom[4], 0)

    if not (_DL and _TETO_D and _mseco and _FI):
        erro('9.1: nao achei na peca a regra do dado do §4.4 ou o fator da Intervencao do '
             '§6.5 — o orcamento de uma acao se mede contra os dois')
    elif not _CAT or not _MANUAL:
        pulou('9.1. o orcamento de feitico — sem a tabela do manual ou a do §4')
    elif len(_T91) != len(_MANUAL):
        erro(f'9.1: a tabela de orcamento do §6.5 tem {len(_T91)} linha(s) e a tabela de '
             f'inimigo do manual tem {len(_MANUAL)} — ela parou de cobrir as faixas')
    else:
        _mau91 = 0
        for _l91 in _T91:
            _mn = re.search(r'(\d+)', _l91[0])
            if not _mn or int(_mn.group(1)) not in _MANUAL:
                erro(f'9.1: nao reconheci o nivel na linha "{_l91[0]}" do §6.5')
                _mau91 += 1
                continue
            _nv91 = int(_mn.group(1))
            _cd91 = _MANUAL[_nv91][2]
            for _cel91, _c91 in zip(_l91[1:], _CAT):
                # rota B: o fator entra no dano de RODADA, antes do dado — e' o
                # golpe que a ficha imprime, que e' o que o texto do §6.5 descreve
                _rod91 = _arr(_cd91 * _c91[2])
                if _INT.get(_c91[0]):
                    _rod91 = _arr(_rod91 * _FI)
                _g91 = _media_do_dado(_rod91 / _c91[3])
                _pts = _g91 / _PONTO
                if _pts < _PISO19 - 1e-9:
                    if _cel91.strip().lower() != 'seco':
                        erro(f'9.1: nv {_nv91}, {_c91[0]}: o orcamento e {_pts:.2f} pontos, '
                             f'abaixo do piso de {_PISO19} que a Classe 1 do manual custa, '
                             f'e a peca publica "{_cel91}" em vez de seco')
                        _mau91 += 1
                    continue
                _mv = re.match(r'([\d,]+)$', _cel91.strip())
                if not _mv or abs(float(_mv.group(1).replace(',', '.')) - _pts) > 0.051:
                    erro(f'9.1: nv {_nv91}, {_c91[0]}: a peca publica "{_cel91}" e o golpe de '
                         f'{_g91:.2f} da {_pts:.2f} pontos')
                    _mau91 += 1
        if not _mau91:
            print(f'  [x] as {len(_T91) * len(_CAT)} celulas do orcamento de feitico saem '
                  f'da media do dado ÷ {_PONTO}, com o fator {_FI} de quem carrega '
                  'Intervencao, e o `seco` e o piso da Classe 1 do manual')

    # -- 9.2: a aptidao come a cota, e o custo sai da peca 11 ----------------
    # O multiplicador de cada aptidao NAO e' lido daqui: ele vem da tabela das
    # quatro anti-dominio da peca 11 §6.5, que e' a dona. Se ela repreçar, esta
    # acende — que e' a coisa que uma copia nao faz.
    _APT11 = {}
    for _l11 in tabela(ler(P11), '| | Classe · gate | abre em | o refino escala | PE por rodada |'):
        if len(_l11) >= 5:
            _mm = re.match(r'([\d,]+) × maior Classe', _l11[4].strip())
            if _mm:
                _APT11[_l11[0].strip()] = float(_mm.group(1).replace(',', '.'))
    _T92 = tabela(TXT, '| ligada a luta inteira, no nível 30 | da cota de uma `Ameaça` | de um `Desastre` |')
    if not _APT11:
        erro('9.2: nao achei o custo por rodada das anti-dominio na peca 11 §6.5 — ela e '
             'a dona, e sem ela o §6.5 daqui vira copia solta')
    elif 30 not in _MANUAL:
        pulou('9.2. a aptidao contra a cota — a linha do nivel 30 da tabela de inimigo '
              'nao foi lida, e a conta se mede contra o dano dela')
    elif not _T92:
        erro('9.2: nao achei a tabela da aptidao no §6.5 — ela mudou de forma e esta '
             'checagem parou de conferir')
    else:
        _cd92 = _MANUAL[30][2]
        _mau92 = 0
        for _l92 in _T92:
            _nomes = [_n for _n in _APT11 if _n in _l92[0]]
            if not _nomes:
                erro(f'9.2: a linha "{_l92[0]}" do §6.5 nao nomeia nenhuma aptidao que a '
                     'peca 11 §6.5 preca')
                _mau92 += 1
                continue
            _mm92 = re.search(r'([\d,]+) ×', _l92[0])
            _pub92 = float(_mm92.group(1).replace(',', '.')) if _mm92 else None
            _don92 = {_APT11[_n] for _n in _nomes}
            if len(_don92) != 1 or _pub92 is None or abs(_pub92 - _don92.pop()) > 1e-9:
                erro(f'9.2: a linha "{_l92[0]}" publica multiplicador {_pub92} e a peca 11 '
                     f'§6.5 da {[_APT11[_n] for _n in _nomes]}')
                _mau92 += 1
                continue
            _custo = _pub92 * _CL18[30] * _CAMBIO
            _COLS92 = [next(c for c in _CAT if c[0] == _r)
                       for _r in ('Ameaça', 'Desastre')]
            for _cel92, _c92 in zip(_l92[1:], _COLS92):
                # v0.221: a cota de quem carrega `Intervencao` leva o fator dela
                _cota92 = _meio_baixo(_cd92 * _c92[2]) * ((_FI or 1.0) if _INT.get(_c92[0]) else 1.0)
                _esp92 = round(_custo / _cota92 * 100)
                _mv92 = re.match(r'(\d+)%', _cel92.strip())
                if not _mv92 or int(_mv92.group(1)) != _esp92:
                    erro(f'9.2: {_nomes[0]} numa {_c92[0]}: a peca publica "{_cel92}" e a '
                         f'conta da {_esp92}% ({_custo:.2f} de '
                         f'{_meio_baixo(_cd92 * _c92[2])})')
                    _mau92 += 1
        if not _mau92:
            print(f'  [x] as {len(_T92)} linhas da aptidao reconstroem do custo da peca 11 '
                  f'§6.5 vezes a maior Classe da peca 18 vezes o cambio da peca 5 §4')

    # -- 9.3: as duas trocas ruins, e as duas sao a mesma conta --------------
    # A cura: H vale (dano ÷ saida) × H, entao o empate e' curar a SAIDA do
    # grupo — que e' a vida do chefe dividida pela duracao da luta.
    # A condicao: alvos × acoes negadas = 4 × acoes gastas, e o 4 e' o numero de
    # personagens da Alcateia, lido do §4 e nao escrito aqui.
    _mcura = re.search(r'empata em `(\d+)`, que é um terço da vida dele', TXT)
    if 30 not in _MANUAL:
        pulou('9.3. o empate da cura — a linha do nivel 30 da tabela de inimigo nao foi '
              'lida, e o empate E a saida do grupo que sai dela')
    elif not _mcura:
        erro('9.3: a peca nao publica o empate da cura do inimigo na forma que esta '
             'checagem le — sem ele a regua do §6.5 fica sem o numero que a fecha')
    else:
        _saida93, _cv93, _cd93 = _MANUAL[30][0], _MANUAL[30][1], _MANUAL[30][2]
        if abs(int(_mcura.group(1)) - _saida93) > 0.51:
            erro(f'9.3: a peca publica empate de cura em {_mcura.group(1)} e a saida do '
                 f'grupo no nivel 30 e {_saida93:.0f} — o empate E a saida, porque o que '
                 f'a cura compra e rodada de luta')
        elif abs(_cv93 / 3 - _saida93) > 0.51:
            erro(f'9.3: a vida do chefe ÷ 3 da {_cv93 / 3:.0f} e a saida do grupo e '
                 f'{_saida93:.0f} — "um terço da vida dele" deixou de ser verdade')
        else:
            print(f'  [x] o empate da cura e {_saida93:.0f}, que e a saida do grupo e e '
                  f'um terço da vida do chefe — a luta de 3 rodadas fecha os dois')

    _PALAVRA = {'meia': 0.5, 'uma': 1.0, 'uma e meia': 1.5}
    _m93 = re.search(r'(meia|uma e meia|uma) ação é `Leve`, (meia|uma e meia|uma) é '
                     r'`Média`, (meia|uma e meia|uma) é `Pesada`', _T19)
    _T93 = re.findall(r'a `(Leve|Média|Pesada)` precisa de `([\d,]+)` alvos', TXT)
    # o tamanho do grupo NAO esta escrito aqui: e' a categoria cujo fator sobre a
    # linha do manual e' exatamente 1, que e' a linha que o manual calibra.
    _alc = [c for c in _CAT if abs(c[2] - 1.0) < 1e-9]
    if not _m93:
        erro('9.3: nao achei na peca 19 a escada de acoes negadas por degrau — ela e a '
             'dona, e a conta de alvos do §6.5 se apoia nela')
    elif not _alc:
        erro('9.3: nao achei no §4 a categoria de fator 1,00 — ela e a linha que o '
             'manual calibra, e o tamanho do grupo sai dela')
    elif len(_T93) != 3:
        erro(f'9.3: achei {len(_T93)} das 3 contas de alvo do §6.5 — a frase mudou de '
             'forma e esta checagem parou de conferir')
    else:
        _ESCADA = {t: _PALAVRA[g] for t, g in zip(('Leve', 'Média', 'Pesada'),
                                                  (_m93.group(1), _m93.group(2),
                                                   _m93.group(3)))}
        _GRUPO = _alc[0][1]
        _mau93 = 0
        for _tier, _pub93 in _T93:
            _esp93 = _GRUPO / _ESCADA[_tier]
            if abs(float(_pub93.replace(',', '.')) - _esp93) > 0.011:
                erro(f'9.3: a peca diz que a `{_tier}` precisa de {_pub93} alvos e a conta '
                     f'da {_esp93:.2f} — ela e {_GRUPO} personagens ÷ '
                     f'{_ESCADA[_tier]:g} acao(oes) negada(s)')
                _mau93 += 1
        if not _mau93:
            print(f'  [x] as tres contas de alvo saem de {_GRUPO} ÷ acoes negadas, com a '
                  'escada lida da peca 19 e o grupo lido do §4')

    # -- 9.4: cada porta declara a moeda em que se paga ----------------------
    # E' o mesmo argumento da checagem 8: porta sem moeda declarada e' entrega de
    # graca, e a categoria passa a mentir sobre o encontro. A guarda cobra as
    # tres, e cobra que cada uma nomeie uma moeda que a peca ja tem.
    _MOEDAS = ('orçamento de feitiço', 'cota de dano por rodada', 'multiplica o fator')
    _T94 = tabela(TXT, '| o que ele carrega | onde ela se paga |')
    if len(_T94) != len(_MOEDAS):
        erro(f'9.4: a tabela das portas do §6.5 tem {len(_T94)} linha(s) e as moedas do '
             f'projeto sao {len(_MOEDAS)} — ou uma porta ficou sem moeda, ou a tabela '
             'mudou de forma e esta checagem parou de conferir')
    else:
        _faltam = [_m for _m in _MOEDAS
                   if not any(_m in _l94[1] for _l94 in _T94)]
        if _faltam:
            erro('9.4: nenhuma porta do §6.5 se paga em ' + ' nem em '.join(_faltam)
                 + ' — porta sem moeda declarada e entrega de graca, e a categoria '
                   'passa a mentir sobre o encontro')
        else:
            print(f'  [x] as {len(_T94)} portas do §6.5 declaram a moeda, e as tres moedas '
                  'sao as que a peca ja cobra')

# --------------------------------------------------------------------------
print()
print('=' * 88)
# =============================================================================
# 9.5 AS MALDICOES PRONTAS — as seis fichas de 05-material recomputadas
# =============================================================================
# Sub-bloco da 9, entao a contagem de checagens nao se move.
#
# A decisao da v0.161 era "maquina mais prontas", e a maquina fechou na v0.198.
# As prontas sairam na v0.213, do nivel 2 ao 6, com a ficcao no folclore japones
# — escolha do Mizuki, e ela e fiel a obra: maldicao de grau baixo e yokai com
# outro nome.
#
# Elas sao INSTANCIA, e instancia envelhece toda vez que a maquina mexe num
# numero. A peca 8 e o precedente e custou sete versoes: uma ficha publicada
# passou aquele tempo com a Defesa errada, com todos os validadores verdes.
#
# A ancora e o `dados.js` do gerador-inimigo, e nao o .docx: a tabela do manual
# so se le com python-docx, e uma checagem de INSTANCIA que pula e' pior que
# nenhuma. O `dados.js` ja e conferido contra a peca pelo bloco 7 do
# conferir-ficha.py, entao a cadeia fecha — prontas -> dados.js -> peca 26.
bloco('9.5 AS MALDICOES PRONTAS — as seis do gerador de inimigo')

_DJ = os.path.join(AQUI, '..', '05-material', 'gerador-inimigo', 'dados.js')
_BL = os.path.join(AQUI, '..', '05-material', 'bloco-de-inimigo.docx')
# v0.221: a derivacao do "seis" morreu com a escada — a Kitsune subiu de faixa
# e a coluna do Capanga ficou vazia, e isso e o preco declarado da decisao de
# 10/09. O que se confere agora e o que cada pronta promete: categoria viva que
# caiba na mesa padrao, faixa que exista, Acoes Multiplas so em quem age mais de
# uma vez, Intervencoes so em quem a categoria da — e nenhum numero guardado.
if not os.path.isfile(_DJ):
    erro('9.5: nao achei o `dados.js` do gerador-inimigo')
else:
    _dj = open(_DJ, encoding='utf-8').read()
    _i0 = _dj.find('const PRONTAS')
    _pb = _dj[_i0:_dj.find('\n];', _i0)] if _i0 >= 0 else ''
    _itens = re.split(r"\n\s*\{\s*nome:\s*'", _pb)[1:]
    _cats95 = {c[0]: c for c in _CAT}
    _fx95 = set(re.findall(r"\['(\d+ a \d+)',", _dj))
    _um95 = [c for c in _CAT if c[1] is not None and abs(c[2] - 1.0) < 1e-9]
    _MESA = _um95[0][1] if _um95 else None
    _mn95 = re.search(r'carrega (\w+) `Intervenções` por luta', TXT)
    _NINT = _NUM_PT.get(_mn95.group(1).lower()) if _mn95 else None
    _ruins = []
    if not _itens:
        _ruins.append('nao achei as PRONTAS no `dados.js` — a decisao da v0.161 pede maquina MAIS '
                      'prontas, e sem elas so existe a maquina')
    if _MESA is None or _NINT is None:
        _ruins.append('nao li na peca a mesa padrao (§4) ou quantas Intervencoes por luta (§6.5)')
    for _it in _itens:
        _nome = _it.split("'")[0]
        _fa = re.search(r"faixa:\s*'([^']+)'", _it)
        _ca = re.search(r"categoria:\s*'([^']+)'", _it)
        if not (_fa and _ca):
            _ruins.append(f'`{_nome}` sem faixa ou categoria')
            continue
        _c = _cats95.get(_ca.group(1))
        if _c is None:
            _ruins.append(f'`{_nome}` esta na categoria `{_ca.group(1)}`, que nao existe na escada do §4')
            continue
        if _fa.group(1) not in _fx95:
            _ruins.append(f'`{_nome}` esta na faixa `{_fa.group(1)}`, que nao existe nas FAIXAS')
        if _MESA and _c[1] is not None and _c[1] > _MESA:
            _ruins.append(f'`{_nome}` e `{_c[0]}`, que exige {_c[1]} personagens — uma pronta tem de '
                          f'caber na mesa padrao de {_MESA}')
        _mm = re.search(r'acoes_multiplas:\s*(null|")', _it)
        if not _mm or ((_mm.group(1) == 'null') != (_c[3] == 1)):
            _ruins.append(f'`{_nome}` age {_c[3]} vez(es), e a Acoes Multiplas dela nao bate — ela so '
                          'existe em quem age mais de uma vez')
        _mi = re.search(r'intervencoes:\s*\[(.*?)\]\s*[,}]', _it, re.S)
        _niv = len(re.findall(r'"nome"\s*:', _mi.group(1))) if _mi else -1
        _esp = (_NINT or 0) if _INT.get(_c[0]) else 0
        if _niv != _esp:
            _ruins.append(f'`{_nome}` carrega {_niv} Intervencao(oes), e a categoria `{_c[0]}` pede {_esp}')
    # a guarda que importa: PRONTAS nao pode guardar NUMERO de ficha. Vida, dano,
    # acoes, golpe e capanga sao COMPUTADOS pelo make.js das FAIXAS e CATEGORIAS —
    # escrever qualquer um deles aqui e a segunda fonte que a v0.213 ja pagou.
    _proibidos = [k for k in ('vida', 'dano', 'acoes', 'golpe', 'capanga', 'defesa')
                  if re.search(r'\b' + k + r'\s*:', _pb)]
    if _proibidos:
        _ruins.append(f'as PRONTAS guardam {_proibidos} — esses numeros sao computados de FAIXAS e '
                      'CATEGORIAS pelo make.js, e escrever eles aqui e a segunda fonte')
    if not os.path.isfile(_BL):
        _ruins.append('nao achei o `bloco-de-inimigo.docx` — as prontas so chegam ao mestre por ele')
    for _m in _ruins[:6]:
        erro('9.5: ' + _m)
    if not _ruins:
        print(f'  [x] as {len(_itens)} prontas estao em categorias vivas que cabem na mesa padrao, com '
              'Acoes Multiplas so em quem age mais de uma vez, Intervencoes so em quem a categoria da, '
              'e nenhuma guarda numero de ficha')


# 9.6 (v0.221): a area natural do inimigo — a cobertura sai do nivel, e cada forma
# gasta a mesma cobertura. Os raios tem de ser os primeiros degraus da escada de
# esfera do MANUAL (o partC.js e o dono dela), a cobertura tem de ser o circulo
# contado em quadrados, e o cone e cada retangulo tem de caber na tolerancia que
# a propria peca declara. As faixas cobrem do nivel 2 ao 30 sem buraco.
print()
bloco('9.6 A AREA NATURAL — a cobertura sai do nivel, e a forma e o jeito de gastar ela')
_T96 = tabela(TXT, '| nível | cobre | `Esfera` | `Cone` |')
_esc96 = re.search(r"\['Esfera \(raio\)', '([^']+)'\]",
                   open(os.path.join(RAIZ, 'manual', 'gerador', 'partC.js'), encoding='utf-8').read())
_mtol = re.search(r'o pior erro de arredondamento nas doze células é `([\d,]+)%`', TXT)
if len(_T96) != 4 or not _esc96 or not _mtol or not _QUAD:
    erro('9.6: nao li a tabela da area natural do §6.5, a escada de esfera do manual, a tolerancia '
         'declarada ou o quadrado do §3.3 — esta checagem parou de conferir')
else:
    _tol = float(_mtol.group(1).replace(',', '.')) / 100
    _degraus = [float(x.replace(',', '.')) for x in re.findall(r'([\d,]+) m', _esc96.group(1))]
    _mau96, _raios, _fim = 0, [], 1
    for _l in _T96:
        _nv = [int(x) for x in re.findall(r'\d+', _l[0])]
        _cob = int(re.match(r'(\d+)', _l[1]).group(1))
        _r = float(re.search(r'([\d,]+) m', _l[2]).group(1).replace(',', '.'))
        _cone = float(re.search(r'([\d,]+) m', _l[3]).group(1).replace(',', '.')) / _QUAD
        _rets = [(int(a), int(b)) for a, b in re.findall(r'(\d+)×(\d+)', _l[4])]
        _raios.append(_r)
        if _nv[0] != _fim + 1:
            erro(f'9.6: a faixa {_l[0]} nao comeca onde a anterior terminou')
            _mau96 += 1
        _fim = _nv[-1]
        if _cob != round(math.pi * (_r / _QUAD) ** 2):
            erro(f'9.6: raio {_r} m cobre {round(math.pi * (_r / _QUAD) ** 2)} quadrados, e a tabela '
                 f'publica {_cob}')
            _mau96 += 1
        for _rot, _area in [('o cone', _cone ** 2 / 2)] + [(f'o retangulo {a}×{b}', a * b) for a, b in _rets]:
            if abs(_area - _cob) / _cob > _tol + 1e-9:
                erro(f'9.6: na faixa {_l[0]}, {_rot} cobre {_area:g} contra {_cob} — passa dos '
                     f'{_tol:.1%} que a peca declara')
                _mau96 += 1
    if _raios != _degraus[:len(_raios)]:
        erro(f'9.6: os raios da area natural sao {_raios} e a escada de esfera do manual comeca em '
             f'{_degraus[:len(_raios)]}')
        _mau96 += 1
    if _fim != max(_MANUAL) if _MANUAL else False:
        erro(f'9.6: a area natural para no nivel {_fim}, e a tabela de inimigo vai ate o {max(_MANUAL)}')
        _mau96 += 1
    if not _mau96:
        print(f'  [x] os {len(_raios)} raios sao os primeiros degraus da escada de esfera do manual, a '
              f'cobertura e o circulo em quadrados, e o cone e os retangulos cabem nos {_tol:.1%}')


# --------------------------------------------------------------------------
bloco('9.7 A RECARGA — ela come o turno, bate 2,5 golpes em cada alvo, e se paga no fator')
# --------------------------------------------------------------------------
# v0.230. Ate a v0.229 a peca dizia que a Recarga "ocupa uma das acoes dele" — erro de
# travessia da decisao de 10/09, que dizia "come o turno" no sentido do D&D. O Mizuki
# decidiu em 14/09 que ela bate 2,5 golpes por alvo, e que se paga no fator pelo metodo
# do Guia do Mestre de 2014 (tres rodadas, a area conta 2 alvos numa mesa de 4).
# Nada de valor mora aqui: o multiplicador, a banda, o d6, a luta, a mesa do D&D, as
# pessoas e as acoes de cada categoria e a medicao de campo sao lidos dos donos.
_REC = TXT[TXT.find('#### A `Recarga` — ela come o turno'):TXT.find('#### A área natural')]
_ruins97 = []
if not _REC:
    erro('9.7: nao achei a subsecao da `Recarga` no §6.5')
else:
    _k = re.search(r'cada alvo leva `([\d,]+) ×` o golpe na falha', _REC)
    _come = re.search(r'Ela come as ações múltiplas do turno — não come a `Intervenção`, a Ação Bônus nem a Reação', _REC)
    _dados = re.search(r'Ela rola em `d(\d+)`, com dois terços do dano em dado e o resto fixo, sem o teto de oito dados do golpe', _REC)
    _ex = re.search(r'Um golpe de `(\d+)` vira `(\d+)`, que é `(\d+)d(\d+) \+ (\d+)`', _REC)
    _banda_p = re.search(r'O golpe fica entre `(\d+)%` e `(\d+)%` da vida.*?tira de `(\d+)%` a `(\d+)%` dela', _REC, re.S)
    _dnd = re.search(r'uma área conta como se pegasse `(\d+)` alvos numa mesa de `(\d+)`', _REC)
    _luta = re.search(r'Com a luta de `(\d+)` rodadas e `([\d,]+)` disparos', _REC)
    _d6 = re.search(r'volta no começo do turno dele com `(\d)` ou `(\d)` no `d6`', _REC)
    if not (_k and _come and _dados and _ex and _banda_p and _dnd and _luta and _d6):
        erro('9.7: a subsecao da `Recarga` perdeu uma das frases que esta checagem le — o multiplicador, '
             'o que ela come, os dados, a banda, a mesa do D&D, a luta ou o d6')
    else:
        K = float(_k.group(1).replace(',', '.'))
        # os dados: dois tercos em dN, o numero de dados que chega mais perto sem deixar fracao no fixo
        _f = int(_dados.group(1)); _g = int(_ex.group(1)); _tot = int(K * _g)
        _cands = [(abs(n * (_f + 1) / 2 / _tot - 2 / 3), n) for n in range(1, 200)
                  if _tot - n * (_f + 1) / 2 >= 0 and abs((_tot - n * (_f + 1) / 2) % 1) < 1e-9]
        if not _cands:
            _ruins97.append(f'nenhum numero de d{_f} fecha {_tot} sem fracao no fixo')
        else:
            _nd = min(_cands)[1]; _fx = int(_tot - _nd * (_f + 1) / 2)
            if (int(_ex.group(2)), int(_ex.group(3)), int(_ex.group(4)), int(_ex.group(5))) != (_tot, _nd, _f, _fx):
                _ruins97.append(f'o exemplo diz {_ex.group(2)} = {_ex.group(3)}d{_ex.group(4)} + {_ex.group(5)}, e a regra da '
                                f'{K} × {_g} = {_tot} = {_nd}d{_f} + {_fx}')
        # a banda do golpe e do Bestiario (DECIDIDO-o-capanga §1)
        try:
            _cap = open(os.path.join(RAIZ, 'bestiario/04-fase-1/fila/DECIDIDO-o-capanga.md'), encoding='utf-8').read()
            _bd = re.search(r'A banda do `o golpe` vira \*\*`(\d+)%`–`(\d+)%`\*\*', _cap)
        except OSError:
            _bd = None
        if not _bd:
            _ruins97.append('nao achei a banda do golpe no DECIDIDO-o-capanga do Bestiario')
        else:
            b0, b1 = int(_bd.group(1)), int(_bd.group(2))
            if (int(_banda_p.group(1)), int(_banda_p.group(2))) != (b0, b1):
                _ruins97.append(f'a peca diz a banda {_banda_p.group(1)}–{_banda_p.group(2)}% e o Bestiario diz {b0}–{b1}%')
            # para baixo: o que o inimigo tira e o que ele ganha, pela regra de arredondamento da peca 1 §5.4
            if (int(_banda_p.group(3)), int(_banda_p.group(4))) != (int(K * b0), int(K * b1)):
                _ruins97.append(f'a peca diz que a Recarga tira {_banda_p.group(3)}–{_banda_p.group(4)}%, e {K} × a banda da '
                                f'{int(K * b0)}–{int(K * b1)}%')
        # os disparos saem do d6 e da luta
        L = int(_luta.group(1))
        _p = (7 - int(_d6.group(1))) / 6
        _disp = 1 + (L - 1) * _p
        _luta_peca = re.search(r'contra as `(\d+),(\d+)` que a categoria promete', TXT)
        if _luta_peca and int(_luta_peca.group(1)) != L:
            _ruins97.append(f'a Recarga usa luta de {L} rodadas e o §6.3 promete {_luta_peca.group(1)}')
        if abs(round(_disp, 2) - float(_luta.group(2).replace(',', '.'))) > 1e-9:
            _ruins97.append(f'a peca publica {_luta.group(2)} disparos, e 1 + ({L} − 1) × {_p:.3f} da {_disp:.2f}')
        # a tabela do fator, contra as pessoas e as acoes do §4
        _meia = int(_dnd.group(1)) / int(_dnd.group(2))
        _cat = {}
        for _l in TXT.split('\n'):
            _m = re.match(r'^\| \*\*`(\w+)`\*\* \| (\d+) \| `× [\d,]+` \| `(\d+)` \| (?:sim|não) \|$', _l)
            if _m: _cat[_m.group(1)] = (int(_m.group(2)), int(_m.group(3)))
        _linhas = re.findall(r'^\| \*\*`(\w+)`\*\* \| `(\d+)` \| `(\d+)` \| `([\d,]+) ×`(?: a comum)? \| `× ([\d,]+)` \|$', _REC, re.M)
        if len(_linhas) != len(_cat) or not _cat:
            _ruins97.append(f'a tabela do fator tem {len(_linhas)} categorias e o §4 tem {len(_cat)} com personagens')
        for _n, _pe, _ac, _r, _f in _linhas:
            if _n not in _cat:
                _ruins97.append(f'a tabela do fator tem `{_n}`, que o §4 nao tem com personagens'); continue
            pe, ac = _cat[_n]
            r = K * pe * _meia / ac
            M = (_disp * r + (L - _disp)) / L
            if (int(_pe), int(_ac)) != (pe, ac):
                _ruins97.append(f'`{_n}`: a tabela diz {_pe} personagens e {_ac} acoes, e o §4 diz {pe} e {ac}')
            if abs(round(r, 2) - float(_r.replace(',', '.'))) > 1e-9 or abs(round(M, 2) - float(_f.replace(',', '.'))) > 1e-9:
                _ruins97.append(f'`{_n}`: a tabela diz rodada {_r}× e fator {_f}, e a conta da {r:.2f}× e {M:.2f}')
        # a medicao de campo, contra a MEDIDA do Bestiario
        try:
            _med = open(os.path.join(RAIZ, 'bestiario/04-fase-1/fila/MEDIDA-a-recarga-contra-a-vida.md'), encoding='utf-8').read()
        except OSError:
            _med = ''
        _campo_p = re.search(r'D&D 2024 no topo tira `(\d+)%`, a área limitada do Pathfinder 2e tira `(\d+)%` a `(\d+)%`, e a `Villain Action` do Draw Steel tira `(\d+)%`', _REC)
        _campo_m = [re.search(r'\| \*\*%s\*\* \|[^\n]*\| \*\*`(\d+)%%`\*\*' % s, _med) for s in ('D&D 2024', 'Draw Steel')]
        _pf_m = re.findall(r'\| \*\*Pathfinder 2e\*\* \|[^\n]*\| \*\*`(\d+)%`\*\*', _med)
        if not (_campo_p and all(_campo_m) and len(_pf_m) == 2):
            _ruins97.append('nao consegui ler a medicao de campo na peca ou na MEDIDA do Bestiario')
        elif (int(_campo_p.group(1)), int(_campo_p.group(2)), int(_campo_p.group(3)), int(_campo_p.group(4))) != \
                (int(_campo_m[0].group(1)), int(_pf_m[0]), int(_pf_m[1]), int(_campo_m[1].group(1))):
            _ruins97.append('a medicao de campo que a peca cita nao e a que a MEDIDA do Bestiario publica')
    # a guarda: o erro de travessia nao volta
    if re.search(r'ocupa uma das ações dele — não vem por cima|Cobrar a cota em cima seria cobrar duas vezes', TXT):
        _ruins97.append('voltou a frase de que a Recarga ocupa uma das acoes e ja se paga sozinha — saiu na v0.230')
    # e o preco da Melhoria na tecnica: a maior Classe que cabe
    _mc = re.search(r'o preço de cada Melhoria usa a maior Classe que cabe nesse orçamento\.\*\* \*Decisão do Mizuki, v0\.230: numa ação de `(\d+),(\d)` pontos a Classe é a `(\d+)`, e uma `Leve` custa `(\d+)`', TXT)
    try:
        _pf = open(os.path.join(RAIZ, 'manual/gerador/partF.js'), encoding='utf-8').read()
        _cls = {int(x): int(y) for x, y in re.findall(r"H2\('Classe (\d+) · (\d+) pontos", _pf)}
    except OSError:
        _cls = {}
    if not (_mc and _cls):
        _ruins97.append('a peca parou de dizer que o preco da Melhoria usa a maior Classe que cabe, ou o manual perdeu a escada de Classe')
    else:
        _pt = float(f'{_mc.group(1)}.{_mc.group(2)}')
        _c = max(c for c, p in _cls.items() if p <= _pt)
        if _c != int(_mc.group(3)) or -(-_c // 2) != int(_mc.group(4)):
            _ruins97.append(f'com {_pt} pontos a maior Classe que cabe e a {_c}, e a Leve dela custa {-(-_c // 2)}')
    if _ruins97:
        for _r in _ruins97:
            erro('9.7: ' + _r)
    else:
        print(f'  [x] a Recarga come o turno, bate {K} golpes por alvo, e o exemplo dos dados sai da regra dos dois tercos em d12')
        print(f'  [x] {K} × a banda do golpe do Bestiario da o que a peca publica, e a medicao de campo e a da MEDIDA')
        print(f'  [x] {_disp:.2f} disparos saem do d6 e da luta de {L}; a tabela do fator reconstroi nas {len(_linhas)} categorias')
        print(f'  [x] a frase do erro de travessia nao voltou, e o preco da Melhoria usa a maior Classe que cabe')


# --------------------------------------------------------------------------
bloco('10. O PAPEL — ele redistribui a base, e os seis fecham em 1,000')
# --------------------------------------------------------------------------
# O §3.4 publica duas tabelas: a dos seis papeis, com o que cada um ganha e
# paga, e a dos dois que variam com a categoria. Esta checagem faz tres coisas
# diferentes, e a ordem importa:
#
#   10.1  o INVARIANTE — ganha x paga = 1,000 em toda celula publicada. E' a
#         regra que a propria secao declara, e ela se confere sozinha.
#   10.2  a DERIVACAO — cada fator e' reconstruido do documento DONO dele, e
#         comparado com o publicado. Sem esta metade a 10.1 passaria com um par
#         de numeros inventados que por acaso se multiplicam em 1: o invariante
#         nao sabe se o 1,20 do `Brutamontes` e' o 1,20 certo.
#   10.3  as ACOES do §3.4 batem com as do §4.2, menos o `Capanga`, que no §3.4
#         se le por ESQUADRAO e no §4 por CORPO. A excecao e' declarada nos dois
#         lugares, e esta guarda existe pra ela nao virar erro silencioso.
#
# O `Artilheiro` so entra na 10.1: o fator de alcance dele e' decisao de sabor
# do projeto do Bestiario e nao tem dono neste repositorio. A peca diz isso na
# coluna `o dono`, e esta checagem nao finge que deriva o que nao deriva.

def _num(cel):
    """O primeiro numero decimal da celula, em ponto. Devolve None se nao tem."""
    m = re.search(r'(\d+),(\d+)', cel)
    return float(f'{m.group(1)}.{m.group(2)}') if m else None


_T34 = tabela(TXT, '| papel | o que ganha | o que paga | produto |')
_T34C = tabela(TXT, '| categoria | ações | `Emboscador` ganha | e paga | '
                    '`Controlador` e `Reforço` ganham | e pagam |')

if len(_T34) != 6:
    erro(f'10: achei {len(_T34)} das 6 linhas da tabela de papeis do §3.4 — ela mudou de '
         'forma e esta checagem parou de conferir')
elif len(_T34C) != 5:
    erro(f'10: achei {len(_T34C)} das 5 linhas da tabela por categoria do §3.4 — ela mudou '
         'de forma e esta checagem parou de conferir')
else:
    _PAPEIS = [c[0] for c in _T34]
    print(f'  os {len(_PAPEIS)} papeis do §3.4: ' + ' · '.join(_PAPEIS))

    # -- 10.1 o invariante, em toda celula que publica os dois lados ---------
    _mau101 = 0
    for _lin in _T34:
        _g, _p, _prod = _num(_lin[1]), _num(_lin[2]), _num(_lin[3])
        if _prod is None or abs(_prod - 1.0) > 0.0005:
            erro(f'10.1: `{_lin[0]}` publica produto `{_lin[3]}`, e a secao declara que '
                 f'os seis fecham em 1,000')
            _mau101 += 1
        if _g is not None and _p is not None and abs(_g * _p - 1.0) > 0.002:
            erro(f'10.1: `{_lin[0]}` ganha {_g} e paga {_p}, e o produto sai '
                 f'{_g * _p:.4f} em vez de 1,000')
            _mau101 += 1
    for _lin in _T34C:
        for _a, _b, _quem in ((2, 3, 'Emboscador'), (4, 5, 'Controlador e Reforço')):
            _g, _p = _num(_lin[_a]), _num(_lin[_b])
            if _g is None or _p is None:
                continue
            if abs(_g * _p - 1.0) > 0.002:
                erro(f'10.1: `{_quem}` na `{_lin[0]}` ganha {_g} e paga {_p}, e o produto '
                     f'sai {_g * _p:.4f} em vez de 1,000')
                _mau101 += 1
    if not _mau101:
        print(f'  [x] 10.1: o invariante fecha em 1,000 em toda celula que publica os dois lados')

    # -- 10.2 a derivacao, cada fator contra o dono dele ---------------------
    _PP_DADO = 1 / 20.0     # um ponto de Defesa num d20. Aritmetica do dado, nao design.

    _m_ac = re.search(r'Contra o alvo difícil, em que se acerta (\d+)%', ler(P01))
    _m_vant = re.search(r'vantagem e desvantagem \| `(\d+)` pontos percentuais', ler(P19))
    _m_banda = re.search(r'ele acerta `(\d+)%` a `(\d+)%`', TXT)

    if not (_m_ac and _m_vant and _m_banda):
        _faltou = [_nm for _nm, _m in (('o acerto do PC na peca 1', _m_ac),
                                       ('a vantagem em pp na peca 19', _m_vant),
                                       ('a banda de acerto do §3.1', _m_banda)) if not _m]
        erro('10.2: nao achei ' + ', '.join(_faltou) + ' — sem o dono esta metade nao '
             'deriva nada, e a 10.1 sozinha passa com numero inventado')
    else:
        _ac_pc = int(_m_ac.group(1)) / 100.0
        _pp_vant = int(_m_vant.group(1)) / 100.0
        _ac_ini = (int(_m_banda.group(1)) + int(_m_banda.group(2))) / 200.0
        _vant_mult = min(0.95, _ac_ini + _pp_vant) / _ac_ini
        print(f'  o PC acerta alvo dificil em {_ac_pc:.0%} (peca 1), a vantagem da '
              f'+{_pp_vant:.0%} (peca 19),')
        print(f'  e o inimigo acerta o meio da banda do §3.1, {_ac_ini:.1%} — '
              f'vantagem multiplica por {_vant_mult:.4f}')

        _ESPERADO = {}
        # Defesa <-> vida: o PC acerta menos contra Defesa maior, e a vida efetiva sobe
        _ESPERADO['Brutamontes'] = _ac_pc / (_ac_pc + 2 * _PP_DADO)   # ele PAGA Defesa -2
        _ESPERADO['Baluarte'] = _ac_pc / (_ac_pc - 2 * _PP_DADO)      # ele GANHA Defesa +2

        _mau102 = 0
        for _lin in _T34:
            _nome = _lin[0]
            if _nome not in _ESPERADO:
                continue
            _viu = _num(_lin[1]) if _nome == 'Baluarte' else _num(_lin[2])
            _quer = _ESPERADO[_nome]
            if _viu is None or abs(_viu - _quer) > 0.002:
                erro(f'10.2: `{_nome}` publica `{_viu}` para o cambio de Defesa, e a peca 1 '
                     f'dá {_quer:.3f} — 2 pontos de Defesa movem o acerto do PC de '
                     f'{_ac_pc:.0%} para {_ac_pc + (2 * _PP_DADO if _nome == "Brutamontes" else -2 * _PP_DADO):.0%}')
                _mau102 += 1

        # os dois que variam com a categoria, derivados das acoes
        for _lin in _T34C:
            _cat = _lin[0]
            _n = _num(_lin[1]) or (float(re.search(r'(\d+)', _lin[1]).group(1))
                                   if re.search(r'(\d+)', _lin[1]) else None)
            if not _n:
                erro(f'10.2: nao li as acoes da `{_cat}` no §3.4')
                _mau102 += 1
                continue
            _emb_viu = _num(_lin[2])
            if _emb_viu is not None:
                _emb_quer = (_n - 1 + _vant_mult) / _n
                if abs(_emb_viu - _emb_quer) > 0.002:
                    erro(f'10.2: `Emboscador` na `{_cat}` publica `{_emb_viu}`, e '
                         f'(N-1+{_vant_mult:.3f})/N com N={_n:.0f} dá {_emb_quer:.3f}')
                    _mau102 += 1
            _ctl_viu = _num(_lin[4])
            if _ctl_viu is not None:
                _ctl_quer = 1 + 1 / _n
                if abs(_ctl_viu - _ctl_quer) > 0.002:
                    erro(f'10.2: `Controlador` na `{_cat}` publica `{_ctl_viu}`, e 1+1/N '
                         f'com N={_n:.0f} dá {_ctl_quer:.3f} — a peca 19 §2.2 preca acao '
                         f'negada 1 pra 1')
                    _mau102 += 1

        if not _mau102:
            print('  [x] 10.2: os cinco fatores derivaveis reconstroem do dono — a Defesa '
                  'da peca 1, a vantagem e a acao negada da peca 19')
            print('      (o `Artilheiro` fica de fora: o alcance e decisao do projeto do '
                  'Bestiario, e a peca declara isso)')


    # -- 10.4 (v0.231) o alcance do Artilheiro e o dobro do deslocamento --------------
    # O metro sai de duas coisas: o deslocamento da peca 3 e a razao alcance ÷ deslocamento
    # da Artilharia do Draw Steel, medida no Bestiario. Nada de valor mora aqui.
    _ar = re.search(r'O ataque do `Artilheiro` alcança `(\d+) m`, em todo nível', TXT)
    _ds = re.search(r'mediana de alcance `(\d+)` contra deslocamento `(\d+)` do herói, nas `(\d+)` fichas', TXT)
    _desl = re.search(r'Deslocamento base: (\d+) metros', ler(P03))
    try:
        _md = open(os.path.join(RAIZ, 'bestiario/04-fase-1/papel/MEDIDA-o-alcance-do-artilheiro.md'), encoding='utf-8').read()
    except OSError:
        _md = ''
    _md_v = re.search(r'deslocamento de um herói \| `(\d+)` quadrados', _md)
    _md_a = re.search(r'mediana das `(\d+)` fichas \| \*\*`(\d+)`\*\* quadrados', _md)
    if not (_ar and _ds and _desl and _md_v and _md_a):
        erro('10.4: faltou dono — o alcance do Artilheiro na peca, o deslocamento da peca 3 ou a MEDIDA do Bestiario')
    else:
        _ruins104 = []
        _razao = int(_ds.group(1)) / int(_ds.group(2))
        if int(_ar.group(1)) != _razao * int(_desl.group(1)):
            _ruins104.append(f'o Artilheiro alcanca {_ar.group(1)} m, e {_razao:g} × o deslocamento de {_desl.group(1)} m da {_razao * int(_desl.group(1)):g}')
        if (int(_ds.group(1)), int(_ds.group(2)), int(_ds.group(3))) != (int(_md_a.group(2)), int(_md_v.group(1)), int(_md_a.group(1))):
            _ruins104.append('a medicao do Draw Steel que a peca cita nao e a da MEDIDA do Bestiario')
        for _r in _ruins104:
            erro('10.4: ' + _r)
        if not _ruins104:
            print(f'  [x] 10.4: o Artilheiro alcanca {_ar.group(1)} m = {_razao:g} × o deslocamento de {_desl.group(1)} m, e a razao e a da MEDIDA do Draw Steel')

    # -- 10.3 as acoes do §3.4 contra as do §4 ------------------------------
    _T4 = tabela(TXT, '| categoria | personagens | fator sobre a linha do manual | '
                      'ações | `Intervenção` |')
    _m_esq = re.search(r'esquadrão de `(\d+)` corpos', TXT)
    if not _T4 or not _m_esq:
        erro('10.3: nao achei a tabela do §4 ou o tamanho do esquadrao no §3 — sem os dois '
             'nao da para conferir se as duas leituras de acao do `Capanga` concordam')
    else:
        _ac4 = {}
        for _lin in _T4:
            _m = re.search(r'(\d+)', _lin[3])
            if _m:
                _ac4[_lin[0]] = int(_m.group(1))
        _esq = int(_m_esq.group(1))
        _mau103 = 0
        for _lin in _T34C:
            _cat = _lin[0]
            _m = re.search(r'(\d+)', _lin[1])
            if not _m:
                continue
            _n34 = int(_m.group(1))
            _quer = _esq if _cat == 'Capanga' else _ac4.get(_cat)
            if _quer is None:
                erro(f'10.3: a `{_cat}` esta no §3.4 e nao esta na tabela do §4')
                _mau103 += 1
            elif _n34 != _quer:
                _porq = (f'o `Capanga` se le por ESQUADRAO no §3.4, e o §3 diz {_esq} corpos'
                         if _cat == 'Capanga' else f'o §4 declara {_quer}')
                erro(f'10.3: a `{_cat}` tem {_n34} acao(oes) no §3.4 e {_porq}')
                _mau103 += 1
        if not _mau103:
            print(f'  [x] 10.3: as acoes do §3.4 batem com as do §4, e o `Capanga` usa o '
                  f'esquadrao de {_esq} corpos, que o §3 publica')

    print()
    print('  O papel nao acrescenta encontro: ele move a base de um eixo para outro.')
    print('  Nenhum dos seis sobe o dano por rodada — e e por isso que `o golpe` fica')
    print('  onde estava, e a banda que o modelo do Bestiario vigia nao entra no caminho.')


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
    print('>>> TUDO OK — as tres derivadas devolvem o que a peca 1 ja publicava do')
    print('    outro lado da mesa, a categoria reescala da tabela do manual, as acoes')
    print('    batem com o piso da peca 19, e o cambio foi medido em vez de guardado.')

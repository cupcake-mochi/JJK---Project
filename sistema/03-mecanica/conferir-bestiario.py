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
    'integridade': (PECA, r'igual à vida máxima'),
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


_NUM_PT = {'um': 1, 'dois': 2, 'três': 3, 'quatro': 4, 'cinco': 5, 'seis': 6,
           'sete': 7, 'oito': 8, 'nove': 9, 'dez': 10}


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
    # quem carrega `Intervencao` entra com o fator dela. Nada mora aqui: a lista de
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
                _g91 = (_media_do_dado(_arr(_cd91 * _c91[2]) / _c91[3])
                        * (_FI if _INT.get(_c91[0]) else 1.0))
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
if not os.path.isfile(_DJ):
    erro('9.5: nao achei o `dados.js` do gerador-inimigo')
else:
    _dj = open(_DJ, encoding='utf-8').read()
    _pb = _dj[_dj.index('const PRONTAS'):_dj.index('];', _dj.index('const PRONTAS'))] \
        if 'const PRONTAS' in _dj else ''
    _pr = re.findall(r"nome:\s*'([^']+)'[^}]*?faixa:\s*'([^']+)'[^}]*?categoria:\s*'([^']+)'",
                     _pb, re.S)
    _fx = re.findall(r"\['(\d+ a \d+)',", _dj)
    # ANCORADO no bloco CATEGORIAS: sem a ancora a regex pegava SUBCATEGORIAS
    # junto — `sozinho`, `bando` — e a checagem cobrava dez celulas onde ha seis.
    _cb = _dj[_dj.index('const CATEGORIAS'):_dj.index('];', _dj.index('const CATEGORIAS'))] \
        if 'const CATEGORIAS' in _dj else ''
    _ct = re.findall(r"\['(\w+)',\s*(\d+),\s*([\d.]+)\]", _cb)
    _ruins = []
    if not _pr:
        _ruins.append('nao achei as PRONTAS no `dados.js` — a decisao da v0.161 pede '
                      'maquina MAIS prontas, e sem elas so existe a maquina')
    else:
        # 1. o piso: seis celulas uteis, e a conta que produz o seis
        _uteis = [(f, c[0]) for f in _fx[:2] for c in _ct if c[0] != 'Calamidade']
        if len(_pr) != len(_uteis):
            _ruins.append(f'sao {len(_pr)} pronta(s) e a faixa do nivel 2 ao 6 tem '
                          f'{len(_uteis)} celulas uteis — duas linhas de FAIXAS vezes as '
                          'categorias, menos a Calamidade, que exige seis feiticeiros')
        _vistas = {(f, c) for _n, f, c in _pr}
        _falta = set(_uteis) - _vistas
        _sobra = _vistas - set(_uteis)
        if _falta:
            _ruins.append(f'celula(s) da faixa sem pronta: {sorted(_falta)}')
        if _sobra:
            _ruins.append(f'pronta(s) fora das duas linhas da faixa, ou Calamidade: '
                          f'{sorted(_sobra)}')
        if len(_vistas) != len(_pr):
            _ruins.append('duas prontas na mesma celula — com seis exemplos e seis celulas, '
                          'repetir e desperdicar exemplo')
        # 2. a guarda que importa: PRONTAS nao pode guardar NUMERO de ficha.
        # Vida, dano, acoes, golpe e capanga sao COMPUTADOS pelo make.js das
        # mesmas FAIXAS e CATEGORIAS que as tabelas da folha. Escrever qualquer
        # um deles aqui cria a segunda fonte — e foi exatamente isso que a v0.213
        # fez num .md a parte, com QUATRO dos seis golpes errados por um
        # arredondamento que o gerador faz e a copia nao fazia.
        _proibidos = [k for k in ('vida', 'dano', 'acoes', 'golpe', 'capanga', 'defesa')
                      if re.search(r'\b' + k + r'\s*:', _pb)]
        if _proibidos:
            _ruins.append(f'as PRONTAS guardam {_proibidos} — esses numeros sao computados '
                          'de FAIXAS e CATEGORIAS pelo make.js, e escrever eles aqui e a '
                          'segunda fonte que a v0.213 ja pagou uma vez')
    if not os.path.isfile(_BL):
        _ruins.append('nao achei o `bloco-de-inimigo.docx` — as prontas so chegam ao mestre '
                      'por ele')
    for _m in _ruins[:5]:
        erro('9.5: ' + _m)
    if not _ruins:
        print(f'  [x] as {len(_pr)} prontas cobrem as celulas uteis da faixa, nenhuma e '
              'Calamidade, e nenhuma guarda numero de ficha — todos saem da maquina.')


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

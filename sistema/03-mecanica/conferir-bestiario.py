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
    'categoria': (PECA, r'\*\*`Ronda`\*\*'),
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
for _c in tabela(TXT, '| categoria | personagens | fator sobre a linha do manual | ações |'):
    if len(_c) < 4:
        continue
    _m = re.match(r'([\d,]+)', _c[2].replace('×', '').strip())
    if _m:
        _CAT.append((_c[0], int(_c[1]), float(_m.group(1).replace(',', '.')), int(_c[3])))
if len(_CAT) != 4:
    erro(f'3: achei {len(_CAT)} categoria(s) na tabela do §4 e a peca promete quatro — '
         'ela mudou de forma e esta checagem parou de conferir')

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
                # ⚠ a faixa mais baixa nao tem capanga, e isso e decisao da v0.199:
                # com o corpo que a proporcao daria, DOIS deles cairiam na primeira
                # rodada de um grupo que causa 38 — ai ele e uma rolagem a mais e nao
                # um corpo. A celula vem com travessao, e quem le tem de saber disso.
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
        if abs(_fator - _pes / 4) > 1e-9:
            erro(f'3: a categoria {_c[0]} exige {_pes} personagem(ns) e publica fator '
                 f'{_fator}, e {_pes}/4 da {_pes / 4}')
            _mau3 += 1
        for _nv, _cel in zip((10, 20, 30), _c[1:4]):
            _nums = re.findall(r'(\d+)', _cel)
            if len(_nums) < 2:
                erro(f'3: nao consegui ler a celula "{_cel}" do §4.1')
                _mau3 += 1
                continue
            # ⚠ meio para BAIXO, pela regra declarada no §4.1 da peca. O round()
            # do Python arredonda para o PAR, e 19 das celulas desta escala caem
            # em ,5 — as duas convencoes divergem em nove delas.
            _ve = math.ceil(_MANUAL[_nv][1] * _fator - 0.5)
            _de = math.ceil(_MANUAL[_nv][2] * _fator - 0.5)
            if int(_nums[0]) != _ve or int(_nums[1]) != _de:
                erro(f'3: {_c[0]} no nv{_nv}: a peca publica {_nums[0]} vida e '
                     f'{_nums[1]} dano, e a linha do manual vezes {_fator} da '
                     f'{_ve} e {_de}')
                _mau3 += 1
    if not _mau3:
        print(f'  [x] as {len(_FICHAS)} categorias do §4.1 reconstroem da tabela do '
              'manual vezes o fator')
        print('  [x] os quatro fatores reconstroem de personagens/4')


# --------------------------------------------------------------------------
bloco('4. AS ACOES — personagens menos um, e a Alcateia bate com o piso da peca 19')
# --------------------------------------------------------------------------
# A regra sai da frase do manual — o chefe "perde a acao tres vezes por rodada"
# contra um grupo de quatro. E o valor da categoria de quatro nao e' livre: a
# peca 19 §2.2 preca quatro condicoes dividindo por ele, e com um a menos as
# quatro passam do teto do proprio tier. Se aquele piso mudar, ESTA acende.
if not _CAT:
    erro('4: sem a tabela do §4 lida nao da para conferir as acoes')
else:
    _mau4 = 0
    for _nome, _pes, _fat, _ac in _CAT:
        _esp = max(1, _pes - 1)
        if _ac != _esp:
            erro(f'4: a categoria {_nome} exige {_pes} personagem(ns) e publica {_ac} '
                 f'acao(oes), e "personagens menos um, piso 1" da {_esp}')
            _mau4 += 1
    if not _mau4:
        print('  [x] as quatro categorias seguem "personagens menos um, piso 1"')

    _m19 = re.search(r'O chefe age `(\d+)` vezes por rodada', ler(P19))
    if not _m19:
        erro('4: nao achei o piso das acoes do chefe na peca 19 §2.2 — ele e a metade '
             'de fora desta checagem, e sem ele ela so se compara com ela mesma')
    else:
        _piso = int(_m19.group(1))
        _quatro = [c for c in _CAT if c[1] == 4]
        if not _quatro:
            erro('4: nenhuma categoria desta peca exige quatro personagens, e a tabela '
                 'do manual e a peca 19 sao calibradas para quatro')
        elif _quatro[0][3] != _piso:
            erro(f'4: a categoria de quatro publica {_quatro[0][3]} acoes e a peca 19 '
                 f'§2.2 publica {_piso} — a regua de condicao daquela peca divide por '
                 'esse numero, entao os dois nao podem discordar')
        else:
            print(f'  [x] a categoria de quatro publica {_piso} acoes, igual ao piso '
                  'que a peca 19 §2.2 deriva da banda')


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
else:
    _pub5 = _NUM_PT.get(_m5.group(1).lower())
    _medidos, _sem_capanga = [], []
    for _nv, (_saida, _cv, _cd, _kv, _kd) in sorted(_MANUAL.items()):
        if _kv is None or _kd is None:
            _sem_capanga.append(_nv)
            continue
        _r0, _t0 = _simula(_saida, [(_cv, _cd)])
        _melhor = min(range(1, 13),
                      key=lambda n: abs(_simula(_saida, [(_kv, _kd)] * n)[1] - _t0))
        _medidos.append((_nv, _melhor))
    print('  cambio medido por nivel: ' + ' · '.join(f'nv{n}:{m}' for n, m in _medidos))
    # a faixa sem capanga nao entra na conta, e a peca tem de declarar o piso —
    # senao a coluna vazia fica lida como esquecimento em vez de decisao.
    if _sem_capanga:
        _decl = 'não tem capanga' in TXT or 'sem capanga' in TXT
        if not _decl:
            erro(f'5: a tabela do manual tem {len(_sem_capanga)} faixa(s) sem capanga '
                 f'— nivel {", ".join(str(x) for x in _sem_capanga)} — e esta peca nao '
                 'declara o piso. Coluna vazia sem motivo escrito le-se como esquecimento')
        else:
            print(f'  {len(_sem_capanga)} faixa(s) sem capanga (nv '
                  f'{", ".join(str(x) for x in _sem_capanga)}), e a peca declara o piso.')
    _valores = sorted({m for _, m in _medidos})
    if _pub5 is None:
        erro(f'5: nao entendi "{_m5.group(1)}" como numero por extenso')
    elif _valores != [_pub5]:
        erro(f'5: a peca publica {_pub5} capangas por chefe, e a simulacao devolve '
             f'{_valores} nos {len(_medidos)} niveis da tabela do manual')
    else:
        print(f'  [x] a simulacao devolve {_pub5} em todos os niveis, e e o que a peca '
              'publica')

    # v0.201: o capanga deixou de ser medido e passou a ser DERIVADO do chefe.
    # A peca publica a derivacao em palavras, e aqui ela e' cobrada contra a
    # tabela do manual — nos dois sentidos, porque uma derivacao que so' vale num
    # nivel nao e' derivacao.
    _diz_vida = 'vida do chefe dividida por quatro' in TXT
    _diz_dano = 'dano do chefe dividido por três' in TXT
    if not (_diz_vida and _diz_dano):
        erro('5: a peca nao publica as duas linhas da derivacao do capanga — sem elas '
             'a coluna volta a ser numero solto que ninguem reconstroi')
    else:
        _fora = []
        for _nv, (_saida, _cv, _cd, _kv, _kd) in sorted(_MANUAL.items()):
            if _kv is None:
                continue
            _evida, _edano = _meio_baixo(_cv / 4), _meio_baixo(_cd / 3)
            if (_kv, _kd) != (_evida, _edano):
                _fora.append(f'nv{_nv}: o manual da ({_kv}, {_kd}) e a derivacao da '
                             f'({_evida}, {_edano})')
        if _fora:
            erro('5: o capanga do manual nao e o que a derivacao da peca produz — '
                 + ' · '.join(_fora))
        else:
            print('  [x] o capanga do manual E a vida do chefe dividida por quatro e o '
                  'dano dele dividido por tres, nas seis faixas que tem capanga')

    # -- 5.1: a coluna da sub-categoria, recontada -----------------------------
    # Ela nunca teve validador ate a v0.201 e tinha divergido: o publicado subia
    # de 28% a 35% e a simulacao nao reproduzia nem a ordem. A ordem de abate
    # MUDA a resposta em ate 15 pontos, entao a peca tem de declarar qual e'.
    _ordem_declarada = 'os capangas primeiro' in TXT
    _m51 = re.findall(r'\|\s*\*\*`(sozinho|com um apoio|com dois|bando)`\*\*\s*\|\s*'
                      r'`(\d+)%`\s*\|\s*[`\d—]+\s*\|\s*`(\d+)%`\s*\|', TXT)
    if not _ordem_declarada:
        erro('5.1: a peca publica a coluna da sub-categoria e nao declara em que ordem o '
             'grupo abate — a coluna muda ate 15 pontos percentuais com a ordem')
    elif len(_m51) != 4:
        erro(f'5.1: achei {len(_m51)} das 4 linhas da tabela de sub-categoria do §4.5 — '
             'ela mudou de forma e esta checagem parou de conferir')
    elif not _MANUAL or 30 not in _MANUAL:
        pulou('5.1. a sub-categoria — a linha do nivel 30 do manual nao foi lida')
    else:
        _saida, _cv, _cd, _kv, _kd = _MANUAL[30]
        _vg = 4 * _VIDA_PC(30)
        _mau51 = 0
        for _rot, _frac, _pct in _m51:
            _f = int(_frac) / 100.0
            _cap = round((1 - _f) * 4)
            _r, _c = _simula(_saida, [(_kv, _kd)] * _cap + [(_cv * _f, _cd * _f)])
            _esp = round(_c / _vg * 100)
            if _esp != int(_pct):
                erro(f'5.1: a sub-categoria `{_rot}` publica {_pct}% da vida do grupo e a '
                     f'simulacao devolve {_esp}%')
                _mau51 += 1
        if not _mau51:
            print('  [x] as quatro formas da sub-categoria reconstroem da simulacao, com '
                  'os capangas abatidos primeiro')


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

    # a regra publicada e "dobra quantos personagens ele exige". O `dobra` so' vale
    # se o multiplicador arredondar para 2 — se ele sair dessa faixa, a frase da
    # peca deixa de ser verdade e esta checagem tem de acender.
    if not (1.75 <= _mult_pub <= 2.25):
        erro(f'7.1: a peca publica que a Expansao DOBRA a categoria, e o multiplicador '
             f'dela e {_mult_pub:.2f}x — fora da faixa que arredonda para dois')
    elif 'DOBRA quantos personagens o inimigo exige' not in TXT:
        erro('7.1: a peca parou de publicar a regra da Expansao como "dobra quantos '
             'personagens o inimigo exige" — sem ela a tabela vira numero solto')
    else:
        # e a tabela tem de ser o dobro da coluna de personagens do §4, linha a linha
        _pes = {}
        for _l in TXT.split('\n'):
            _m = re.match(r'\|\s*\*\*`(\w+)`\*\*\s*\|\s*(\d+)\s*\|\s*`× ([\d,]+)`', _l)
            if _m:
                _pes[_m.group(1)] = int(_m.group(2))
        _dob = {}
        for _l in TXT.split('\n'):
            _m = re.match(r'\|\s*\*\*`(\w+)`\*\*\s*\|\s*`(\d+)`\s*\|\s*\*?\*?`?(\d+)`?', _l)
            if _m and _m.group(1) in _pes:
                _dob[_m.group(1)] = (int(_m.group(2)), int(_m.group(3)))
        if len(_pes) != 4 or len(_dob) != 4:
            erro(f'7.1: li {len(_pes)} categorias no §4 e {len(_dob)} na tabela do §6.4, '
                 'e esperava 4 em cada — alguma mudou de forma')
        else:
            _mau = 0
            for _n, (_p, _c) in _dob.items():
                if _p != _pes[_n]:
                    erro(f'7.1: o §6.4 diz que a `{_n}` exige {_p} personagens e o §4 diz '
                         f'{_pes[_n]}')
                    _mau += 1
                elif _c != 2 * _p:
                    erro(f'7.1: a `{_n}` exige {_p} e com Expansao o §6.4 publica {_c}, e '
                         f'o dobro e {2 * _p}')
                    _mau += 1
            if not _mau:
                print('  [x] a tabela do §6.4 e o dobro da coluna de personagens do §4, '
                      'nas quatro categorias')


# --------------------------------------------------------------------------
bloco('8. RESISTENCIA E VIDA ESCONDIDA — e o degrau de categoria e a moeda dela')
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

    # e o degrau de categoria tem de ser a moeda: o maior multiplicador de
    # resistencia tem de caber no degrau que a escada do §4 vende.
    if _CAT and 'Físicos' in _PESOS:
        _degraus = sorted(c[2] for c in _CAT)
        _maior = max(_degraus[i + 1] / _degraus[i] for i in range(len(_degraus) - 1))
        _res_fis = _efetiva(_PESOS['Físicos'], 'resistência')
        _decl = 'custa um degrau de categoria' in TXT
        if not _decl:
            erro('8: a peca nao declara em que moeda a resistencia se paga — sem isso '
                 'ela e vida de graca, e a categoria passa a mentir sobre o encontro')
        elif _res_fis > max(_degraus) / min(d for d in _degraus if d >= 1.0) + 0.01:
            erro(f'8: resistir aos Físicos vale {_res_fis:.2f}x de vida efetiva e o maior '
                 f'degrau da escada do §4 vale {_maior:.2f}x — a moeda nao cobre o preco')
        else:
            print(f'  [x] resistir aos Físicos vale {_res_fis:.2f}x, e o degrau de '
                  f'categoria que a peca cobra vale {_maior:.2f}x')


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
    _T91 = tabela(TXT, '| pontos por ação | `Ronda` | `Dupla` | `Alcateia` | `Calamidade` |')
    if not _CAT or not _MANUAL:
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
                _dano = _meio_baixo(_cd91 * _c91[2])
                _pts = _dano / _c91[3] / _PONTO
                _seco = _pts < _PISO19 - 1e-9
                if _seco:
                    if _cel91.strip().lower() != 'seco':
                        erro(f'9.1: nv {_nv91}, {_c91[0]}: o orcamento e {_pts:.2f} pontos, '
                             f'abaixo do piso de {_PISO19} que a Classe 1 do manual custa, '
                             f'e a peca publica "{_cel91}" em vez de seco')
                        _mau91 += 1
                    continue
                _mv = re.match(r'([\d,]+)$', _cel91.strip())
                if not _mv:
                    erro(f'9.1: nv {_nv91}, {_c91[0]}: a peca publica "{_cel91}" e a conta '
                         f'da {_pts:.2f} pontos')
                    _mau91 += 1
                    continue
                if abs(float(_mv.group(1).replace(',', '.')) - _pts) > 0.051:
                    erro(f'9.1: nv {_nv91}, {_c91[0]}: a peca publica {_cel91} ponto(s) e o '
                         f'golpe de {_dano / _c91[3]:.2f} da {_pts:.2f}')
                    _mau91 += 1
        if not _mau91:
            print(f'  [x] as {len(_T91) * len(_CAT)} celulas do orcamento de feitico saem '
                  f'do golpe ÷ {_PONTO}, e o `seco` e o piso da Classe 1 do manual')

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
    _T92 = tabela(TXT, '| ligada a luta inteira, no nível 30 | da cota de uma `Ronda` | de uma `Alcateia` |')
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
                       for _r in ('Ronda', 'Alcateia')]
            for _cel92, _c92 in zip(_l92[1:], _COLS92):
                _esp92 = round(_custo / _meio_baixo(_cd92 * _c92[2]) * 100)
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
    _MOEDAS = ('orçamento de feitiço', 'cota de dano por rodada', 'degrau de categoria')
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

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Confere o eixo do controle: refino, aptidoes e o terceiro eixo do marco (peca 11).

A REGRA QUE GOVERNA ESTA PECA:
  O refino cresce +7 a +9 numa campanha; atributo e maestria crescem +3. Entao ele
  NAO pode aparecer de um lado de uma rolagem em que o outro lado nao cresce no
  ritmo dele. Isso proibe acerto, CD, defesa, Teste de Resistencia e dano — e
  permite refino contra refino, que e simetrico.

CONTRATO DE INVARIANTES:
  1. TRAVA DO REFINO. Tudo que o refino escala esta num eixo permitido: custo,
     frequencia, escopo, magnitude fora de disputa, ou disputa contra outro refino.
  2. COBRIR-SE nao deriva: 1/3 do refino cresce exatamente +3 na campanha, igual a
     um atributo. E a Reacao a 1,5 x refino fica com saldo POSITIVO em todo nivel.
  3. PROJETAR nao compete com feitico: o dano dela fica numa faixa estreita da
     coluna Rotina, e ela deriva para BAIXO.
  4. KOKUSEN e pequeno e nao espirala: a cascata nao toca a margem, e o que a
     FICHA consegue com as tres empilhadas, POR MARCO PAGO, fica abaixo de um
     quarto do que um ponto de atributo compra. A trava media so a entrada base
     ate a v0.90 — e a peca fala da ficha, nao da entrada.
  5. AS TRES ROTAS DO MARCO nao se dominam, e o orcamento de espaco cobre a
     montagem mais pesada que o manual permite.
  6. O TETO DE PASSIVAS: as pagas continuam sendo cinco. A gratis traz a propria vaga.
  7. OS GATES DE REFINO separam as rotas de verdade.
  8. E A SEGUNDA METADE DO 5, por outro eixo: em nenhum dos sete marcos uma
     das tres opcoes pode estar dominada. O 5 mede o FIM da campanha, e o fim
     esconde o meio — foi assim que a escolha de Refino passou tres marcos
     entregando metade do que promete, com o 5 verde o tempo todo.

Roda sem argumento. Sai com codigo 1 se algo quebrar.
"""
import os
import re
import math
import sys
import itertools

AQUI = os.path.dirname(os.path.abspath(__file__))

# a peca 11 e a dona das regras deste validador. Lida uma vez, aqui.
with open(os.path.join(AQUI, '11-aptidoes-e-refino.md'), encoding='utf-8') as _f:
    PECA11 = _f.read()

ERROS = []
AVISOS = []


import unicodedata


def sem_acento(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s)
                   if unicodedata.category(c) != 'Mn')


def erro(msg):
    ERROS.append(msg)
    print(f'  !! {msg}')


def aviso(msg):
    AVISOS.append(msg)
    print(f'  ~~ {msg}')


def bloco(t):
    print()
    print('=' * 90)
    print(t)
    print('=' * 90)


# --------------------------------------------------------------------------
MARCOS = [6, 10, 14, 18, 22, 26, 30]
NIVEIS = [2, 6, 10, 14, 18, 22, 26, 30]

# curvas de refino, do arquitetura.md secao 4.3
CURVA = {
    'especialista': [3, 5, 7, 9, 10, 10, 10],
    'meio a meio':  [3, 4, 6, 7, 9, 10, 10],
    'generalista':  [2, 3, 4, 5, 6, 7, 8],
}
TETO_REFINO = 10

# tabela de inimigo do manual — importada, e o conferir-manual.py vigia a copia
CHEFE = {5: 39, 10: 75, 15: 111, 20: 147, 25: 183, 30: 219}

# v0.201: a tabela de inimigo publica dano por RODADA, e o chefe age tres vezes.
# Toda regua defensiva desta peca — a RD da Reacao, o empate da Energia Reversa —
# compara com UM GOLPE, porque e' num golpe que a RD entra e e' um golpe que a
# cura repoe. Ate a v0.200 elas liam a rodada, e isso passou despercebido porque
# o chefe entregava 72 por rodada em golpes de 24: a rodada dele era, por
# coincidencia, o mesmo numero que o golpe do chefe de hoje. Com a linha nova os
# dois se separaram, e a leitura certa e' a do golpe.
#
# O numero de acoes NAO esta escrito aqui: ele e' lido da peca 19, que e' a dona.
_p19 = os.path.join(AQUI, '19-dano-e-condicoes.md')
try:
    _t19 = open(_p19, encoding='utf-8').read()
except OSError:
    _t19 = ''
_m19 = re.search(r'O chefe age `(\d+)` vezes por rodada', _t19)
if not _m19:
    print('  !! nao achei "O chefe age N vezes por rodada" na peca 19 — a regua '
          'defensiva desta peca se mede contra o golpe, e o golpe sai daquele numero')
    sys.exit(1)
CHEFE_ACOES = int(_m19.group(1))
ROTINA = {1: 13, 2: 31, 3: 45, 4: 63, 5: 76, 6: 94, 7: 108}
CLASSE_NO_NIVEL = {2: 1, 6: 2, 10: 3, 14: 4, 18: 5, 22: 6, 26: 7, 30: 7}
# Dano de um Classe 0, lido do MANUAL: a tabela "Seu nivel / Quantos voce tem /
# Dano" poe ele em 2d8 . 3d8 . 4d8 . 5d8 . 6d8 por faixa de nivel. Copia vigiada,
# no mesmo molde da ROTINA acima — o dono e o manual, e a checagem 4f do
# conferir-manual.py e quem vigia.
#
# Ate a v0.89 esta linha era `CLASSE_0 = 4.5`. Esse e o numero FANTASMA que a v0.80
# matou em todo o resto do projeto — ele nao aparece em lugar nenhum do manual — e
# ele sobreviveu aqui porque so era IMPRESSO, nunca conferido. Display errado
# ensina numero errado do mesmo jeito que checagem errada.
CLASSE_0_POR_FAIXA = [(1, 9), (5, 13), (11, 18), (17, 22), (25, 27)]


def classe_0(nv):
    v = CLASSE_0_POR_FAIXA[0][1]
    for piso, d in CLASSE_0_POR_FAIXA:
        if nv >= piso:
            v = d
    return v

ACERTO_DIFICIL = 0.50   # peca 1, secao 6


def refino_em(rota, nv):
    r = 1
    for i, m in enumerate(MARCOS):
        if nv >= m:
            r = CURVA[rota][i]
    return r


def dano_chefe(nv):
    ks = sorted(CHEFE)
    if nv <= ks[0]:
        return CHEFE[ks[0]] * nv / 5
    for a, b in zip(ks, ks[1:]):
        if a <= nv <= b:
            return CHEFE[a] + (CHEFE[b] - CHEFE[a]) * (nv - a) / (b - a)
    return CHEFE[30]


def golpe_chefe(nv):
    """o que UM golpe do chefe entrega — a linha do manual dividida pelas acoes"""
    return dano_chefe(nv) / CHEFE_ACOES


def piso(x):
    """Ganho arredonda para baixo — peca 1, secao 5.4."""
    return math.floor(x + 1e-9)


# --------------------------------------------------------------------------
bloco('1. A TRAVA DO REFINO — o que ele pode e nao pode escalar')
print('  O refino cresce muito mais rapido que o resto. Se ele aparecer de um lado')
print('  de uma rolagem disputada, a chance deriva.\n')
print(f"  {'o que cresce':<34}{'do nivel 2 ao 30':<20}{'cresce'}")
for rot, faixa, d in [('atributo investido', '3 -> 6', 3), ('maestria', '1 -> 4', 3),
                      ('refino, generalista', '1 -> 8', 7),
                      ('refino, especialista', '1 -> 10', 9)]:
    print(f'  {rot:<34}{faixa:<20}+{d}')
CRESCE_REFINO = TETO_REFINO - 1
if CRESCE_REFINO <= 3:
    erro('o refino deixou de crescer mais que um atributo — a trava perdeu o motivo')

# eixo -> (permitido?, por que)
EIXOS = {
    'custo em PE':                (True,  'nao ha outro lado; e economia'),
    'frequencia':                 (True,  'nao ha outro lado; e relogio'),
    'escopo (alcance, duracao)':  (True,  'nao ha outro lado; e alcance'),
    'magnitude fora de disputa':  (True,  'RD, protecao e dano que nao compete com feitico'),
    'disputa contra outro refino': (True, 'simetrico — os dois lados crescem +9'),
    'rolagem de acerto':          (False, 'do outro lado, a Defesa cresce +3'),
    'CD de feitico':              (False, 'do outro lado, o atributo do TR cresce +3'),
    'Defesa':                     (False, 'do outro lado, o ataque cresce +3'),
    'Teste de Resistencia':       (False, 'do outro lado, a CD cresce +3'),
    'dano que compete com feitico': (False, 'do outro lado, a vida de inimigo cresce'),
}
# o que cada aptidao escrita declara escalar
# v0.158: o `canalizar energia` deixou de ter uma linha so. O feitico de Toque
# continua com teto ZERO — ele vive dentro do orcamento do Fundamento —, e a outra
# metade dele, o DANO NA ARMA, escala com o refino de proposito. Ele entrou no
# livro na v0.147 e so ganhou peca na v0.158, na SS6.9; a checagem 10 mede ele
# contra as duas condicoes que a SS2 escreve para o eixo de dano.
ESCALA = {
    'cobrir-se, protecao':     'magnitude fora de disputa',
    'cobrir-se, RD da Reacao': 'magnitude fora de disputa',
    'canalizar, Toque':        None,
    'canalizar, dano na arma': 'magnitude fora de disputa',
    'estimulo, dano na arma':  'magnitude fora de disputa',
    'projetar energia':        'magnitude fora de disputa',
    'kokusen, a chance':       'frequencia',
    'kokusen melhorado':       'frequencia',
    'clash de expansao':       'disputa contra outro refino',
}
print(f"\n  {'aptidao':<28}{'eixo que ela escala':<32}{'passa?'}")
for apt, eixo in ESCALA.items():
    if eixo is None:
        print(f'  {apt:<28}{"nenhum — teto zero":<32}sim')
        continue
    ok, motivo = EIXOS[eixo]
    print(f'  {apt:<28}{eixo:<32}{"sim" if ok else "NAO"}')
    if not ok:
        erro(f'"{apt}" escala {eixo}, e {motivo}')
print('\n  Nenhuma aptidao escrita toca um eixo proibido.')


# --------------------------------------------------------------------------
bloco('2. COBRIR-SE — o 1/3 nao deriva, e a Reacao nao inverte de sinal')
DIVISOR = 3
prot = [piso(r / DIVISOR) + 1 for r in range(1, TETO_REFINO + 1)]
cresce = prot[-1] - prot[0]
print(f'  Protecao = 1/{DIVISOR} do refino + 1, arredondando para baixo.\n')
print(f"  {'refino':<9}" + ''.join(f'{r:<5}' for r in range(1, 11)))
print(f"  {'protecao':<9}" + ''.join(f'{p:<5}' for p in prot))
print(f'\n  Ela cresce +{cresce} na campanha. Um atributo investido cresce +3.')
if cresce != 3:
    erro(f'a protecao de cobrir-se cresce +{cresce}, e um atributo cresce +3 — '
         f'o divisor {DIVISOR} deixou de ser o que faz ela caber')
else:
    print('  Bate exatamente. Com 1/2 seriam +5, e com o refino cheio +9.')

# o caso que a trava evita, mostrado
print(f"\n  O que aconteceria sem o divisor, com protecao = refino:")
print(f"  {'nivel':<8}{'ataque':<9}{'Defesa com 1/3':<18}{'acerta':<10}{'Defesa com refino cheio':<26}{'acerta'}")
for nv in (2, 10, 22, 30):
    atk = min(6, 3 + max(0, nv - 2) // 8)
    ref = refino_em('especialista', nv)
    d3 = 10 + atk + piso(ref / DIVISOR) + 1
    dc = 10 + atk + ref
    p3 = max(0.0, min(1.0, (21 - (d3 - atk)) / 20))
    pc = max(0.0, min(1.0, (21 - (dc - atk)) / 20))
    print(f'  {nv:<8}{"d20+"+str(atk):<9}{d3:<18}{p3:<10.0%}{dc:<26}{pc:.0%}')
    if pc > 0.20:
        continue
if max(0.0, min(1.0, (21 - ((10 + 6 + 10) - 6)) / 20)) > 0.25:
    erro('o caso sem divisor deixou de ser catastrofico — a demonstracao perdeu o sentido')

# a Reacao
MULT_RD = 1.5
print(f'\n  A Reacao: Reducao de Dano de {MULT_RD} x refino, ao custo da protecao por um turno.\n')
print(f"  {'nivel':<8}{'refino':<9}{'RD':<7}{'golpe de chefe':<17}{'custo esperado':<17}{'saldo'}")
saldos = []
for nv in (6, 10, 14, 18, 22, 26, 30):
    r = refino_em('especialista', nv)
    rd = piso(MULT_RD * r)
    d = dano_chefe(nv)
    g = golpe_chefe(nv)
    perde = piso(r / DIVISOR) + 1
    custo = 0.05 * perde * g          # cada ponto de Defesa vale 5 pp de acerto
    saldo = rd - custo
    saldos.append(saldo)
    print(f'  {nv:<8}{r:<9}{rd:<7}{g:<17.0f}{custo:<17.1f}{saldo:+.1f}')
    if saldo <= 0:
        erro(f'nv{nv}: a Reacao de cobrir-se tem saldo {saldo:+.1f} — ela vira armadilha, '
             f'e quem a usar esta pagando para tomar mais dano')
if all(s > 0 for s in saldos):
    print('\n  Positiva em todo nivel, e o saldo ENCOLHE em vez de virar — forte quando')
    print('  voce nao tem outra resposta, e so mais uma opcao quando ja tem.')
if saldos[-1] >= saldos[0] * 2:
    aviso('o saldo da Reacao esta crescendo com o nivel em vez de encolher')


# --------------------------------------------------------------------------
bloco('3. PROJETAR — nao compete com feitico, e deriva para baixo')
print('  Dano = refino, sem PE. O arquitetura pede: "fixo e baixo, para quem ficou')
print('  sem PE, nao para competir com feitico".\n')
print(f"  {'nivel':<8}{'Rotina':<10}{'Classe 0':<12}{'projetar':<11}{'% da Rotina'}")
fracoes = []
for nv in NIVEIS:
    r = ROTINA[CLASSE_NO_NIVEL[nv]]
    proj = refino_em('especialista', nv)
    f = proj / r
    fracoes.append(f)
    print(f'  {nv:<8}{r:<10}{f"{classe_0(nv)/r:.0%}":<12}{proj:<11}{f:.0%}')
    if f > 0.30:
        erro(f'nv{nv}: projetar entrega {f:.0%} da Rotina — ela passou a competir com feitico')
print(f'\n  Faixa: de {min(fracoes):.0%} a {max(fracoes):.0%} da Rotina.')
if fracoes[-1] > fracoes[len(fracoes)//2]:
    erro('projetar esta derivando para CIMA — a vida de inimigo deveria crescer mais '
         'rapido que o refino')
else:
    print('  Ela deriva para BAIXO, que e o lado seguro para errar.')


# --------------------------------------------------------------------------
bloco('4. KOKUSEN — pequeno, e a cascata nao espirala')
MULT_KOK = 2       # d100 <= 2 x refino
BONUS_KOK = 0.50   # +50% no impacto, depois de tudo resolvido


def dpr(p_kok, margem=20):
    faces = (21 - margem) / 20
    normal = ACERTO_DIFICIL - faces
    crit = 2.0
    return normal * 1.0 + faces * ((1 - p_kok) * crit + p_kok * crit * (1 + BONUS_KOK))


BASE = dpr(0.0)
print(f'  Linha de base sem kokusen: {BASE:.4f} D por golpe.\n')
print(f"  {'refino':<9}{'chance no d100':<17}{'dano por rodada':<18}{'x um ponto de atributo'}")
VALE_ATRIBUTO = 0.10   # +1 no atributo de ataque vale ~+10% de dano por rodada
for r in (1, 5, 10):
    p = min(1.0, MULT_KOK * r / 100)
    ganho = dpr(p) / BASE - 1
    print(f'  {r:<9}{p:<17.0%}{f"+{ganho*100:.1f}%":<18}{ganho/VALE_ATRIBUTO:.2f}x')
teto_kok = dpr(min(1.0, MULT_KOK * TETO_REFINO / 100)) / BASE - 1
if teto_kok > VALE_ATRIBUTO / 4:
    erro(f'o kokusen chegou a {teto_kok:.1%} de dano por rodada — passou de um quarto '
         f'do que um ponto de atributo compra, e aí vale montar ficha em cima dele')
else:
    print(f'\n  Teto de {teto_kok:.1%}, menos de um quinto de um ponto de atributo.')
    print('  Ele existe pelo grito na mesa, e o texto precisa dizer isso.')

# --- 4.2 A PILHA, e nao so a entrada base ----------------------------------
# A trava acima mede a ENTRADA. A peca 11 diz "ninguem deve montar ficha em cima
# dele" — e isso e uma frase sobre a FICHA. Desde a v0.90 as tres empilham: a
# `Kokusen Constante` sobe a base para 3 x refino e a vantagem da `Melhorado`
# rola em cima dela. Medindo so a base, a trava nunca veria a pilha.
#
# A COMPARACAO E POR MARCO, e nao no total: a pilha inteira custa TRES marcos, e
# tres marcos de Corpo compram +3 de atributo. Medir a pilha contra UM ponto de
# atributo seria comparar tres marcos com um — o erro que a licao no 7 descreve.
#
# NADA DE VALOR ESCRITO AQUI: o multiplicador da Constante e o empilhamento saem
# da peca 11.
print()
_m = re.search(r'Kokusen Constante.{0,400}?base sobe para `(\d+) × refino`', PECA11, re.S)
MULT_CONST = int(_m.group(1)) if _m else None
if MULT_CONST is None:
    erro('nao achei na peca 11 quanto a `Kokusen Constante` poe na base do kokusen — '
         'a trava da pilha parou de conferir')
EMPILHAM = 'As três empilham' in PECA11
if not EMPILHAM:
    erro('a peca 11 parou de dizer que as tres de kokusen empilham — sem essa frase '
         'a mesa nao sabe se a vantagem rola sobre 2x ou sobre 3x, que e o buraco do '
         '`Mirar` outra vez (entrega escrita, interacao nao)')

# v0.202: o Kokusen BASE deixou de custar marco — ele e' regra de mundo, e a
# peca declara isso. Ate aqui este bloco tinha `MARCOS_DA_PILHA = 3` escrito no
# codigo, com o comentario "um marco cada", e era ele quem cobrava o marco que a
# prosa da peca dizia que ninguem pagava. O numero nao mora mais aqui: ele e' a
# contagem das aptidoes de kokusen que a peca declara como compraveis.
_regra_de_mundo = 'regra de mundo, e não entrada do catálogo' in PECA11

_mdom_apt = re.search(r'reprova a partir de `(\d+,\d+)×`', PECA11)
DOMINANCIA_APT = float(_mdom_apt.group(1).replace(',', '.')) if _mdom_apt else 3.00
if not _mdom_apt:
    erro('nao achei o filtro de dominancia na propria peca 11 — ele e o teto da '
         'checagem da `Circulação`, e ele nao pode morar neste arquivo')

# --------------------------------------------------------------------------
# v0.203: a `Circulação`. Duas metades com precos muito diferentes, e o `d4` da
# Acao Bonus e' o numero que traz a segunda para dentro do filtro. Nada esta
# escrito aqui: a formula do teto, os dois dados e o gate saem da peca, e a
# tabela nivel a nivel e' recomputada.
_mcirc = re.search(r'### Circulação · Classe Passiva 3 · exige a `Energia Reversa` e refino (\d+)',
                   PECA11)
if not _mcirc:
    erro('nao achei o titulo da `Circulação` na peca 11 — ela e a aptidao nova da '
         'v0.203 e o gate dela mora no titulo, como o das outras treze')
else:
    _gate_circ = int(_mcirc.group(1))
    _mult = re.search(r'teto por uso da sua `Energia Reversa` sobe para `([\d,]+) × a sua maior Classe`',
                      PECA11)
    _dados = re.search(r'os dados de cura são `d(\d+)` em vez de `d(\d+)`', PECA11)
    if not (_mult and _dados):
        erro('a `Circulação` parou de publicar o multiplicador do teto ou a troca de '
             'dado — os dois sao o preco dela, e sem eles a checagem nao tem o que medir')
    else:
        _M = float(_mult.group(1).replace(',', '.'))
        _dbonus, _dpadrao = int(_dados.group(1)), int(_dados.group(2))
        _med = lambda d: (d + 1) / 2.0
        print(f'  a `Circulação`: teto {_M:.1f}x a maior Classe · d{_dpadrao} na Padrao '
              f'e d{_dbonus} na Bonus · gate refino {_gate_circ}')
        # a tabela nivel a nivel da peca tem de reconstruir
        _linhas = re.findall(r'^\| (\d+|\d+ a \d+) \| (\d+) \| `(\d+)` PE \| `(\d+)` PE \| '
                             r'`([\d,]+)` \| `([\d,]+)` \|$', PECA11, re.M)
        if len(_linhas) != 3:
            erro(f'achei {len(_linhas)} das 3 linhas da tabela da `Circulação` — ela mudou '
                 'de forma e esta checagem parou de conferir')
        else:
            _mau = 0
            for _nv, _C, _ter, _tef, _pad, _bon in _linhas:
                C = int(_C)
                _eter, _etef = C, math.floor(_M * C)
                _epad, _ebon = _etef * _med(_dpadrao), _etef * _med(_dbonus)
                if (int(_ter), int(_tef)) != (_eter, _etef):
                    erro(f'a `Circulação` no nivel {_nv}: a peca publica teto {_ter}/{_tef} '
                         f'e a formula da {_eter}/{_etef}')
                    _mau += 1
                elif (abs(float(_pad.replace(',', '.')) - _epad) > 0.05
                      or abs(float(_bon.replace(',', '.')) - _ebon) > 0.05):
                    erro(f'a `Circulação` no nivel {_nv}: a peca publica {_pad} na Padrao e '
                         f'{_bon} na Bonus, e a conta da {_epad:.1f} e {_ebon:.1f}')
                    _mau += 1
            if not _mau:
                print('  [x] as 3 linhas da tabela da `Circulação` reconstroem da formula')

        # o `d4` e' o que segura a Acao Bonus dentro do filtro, e o `d8` nao seguraria.
        # Numa ficha que nao usa a Bonus para nada, curar ali sai de graca: o ganho e'
        # a cura inteira, toda rodada.
        _ROT = {5: 76.0, 6: 94.0, 7: 108.0}
        _VALE = 0.10
        _pior_b, _pior_p = 0.0, 0.0
        for C in (5, 6, 7):
            _teto = math.floor(_M * C)
            _pior_b = max(_pior_b, _teto * _med(_dbonus) / (_VALE * _ROT[C]))
            _pior_p = max(_pior_p, _teto * _med(_dpadrao) / (_VALE * _ROT[C]))
        print(f'  na Bonus, cura de graca por rodada: d{_dbonus} da {_pior_b:.2f}x um ponto '
              f'de atributo · d{_dpadrao} daria {_pior_p:.2f}x')
        if _pior_b > DOMINANCIA_APT + 1e-9:
            erro(f'a `Circulação` na Acao Bonus entrega {_pior_b:.2f}x o que um ponto de '
                 f'atributo compra, e o filtro reprova a partir de {DOMINANCIA_APT:.2f}x')
        elif _pior_p <= DOMINANCIA_APT + 1e-9:
            erro(f'o dado menor da Acao Bonus deixou de ser o que segura a aptidao: com '
                 f'd{_dpadrao} ela daria {_pior_p:.2f}x e ainda passaria no filtro. O `d{_dbonus}` '
                 'precisa ser a diferenca entre passar e reprovar, senao ele e enfeite')
        else:
            print(f'  [x] o d{_dbonus} segura a Acao Bonus dentro do filtro de '
                  f'{DOMINANCIA_APT:.2f}x, e o d{_dpadrao} nao seguraria')

        # o gate: refino 8 tem de ser alcancavel pelas TRES rotas, senao ele fecha
        # a porta para uma delas — que foi a alternativa recusada na v0.203.
        _fora = [r for r, cur in CURVA.items() if max(cur) < _gate_circ]
        if _fora:
            erro(f'o gate de refino {_gate_circ} da `Circulação` e inalcancavel para '
                 f'{", ".join(_fora)} — a v0.203 recusou o refino 9 por isso')
        else:
            print(f'  [x] o refino {_gate_circ} e alcancavel pelas tres rotas')


# --- o kokusen mora em DOIS documentos, e a v0.202 achou os tres jeitos de eles
# divergirem. O livro publicava um gatilho mais largo, um relogio que esta peca
# MEDIU E RECUSOU, e um requisito que esta peca nega com todas as letras. Nada
# disso tinha validador: a lição nº 9 com o documento que chega na mão do jogador.
_LIVRO_KOK = os.path.join(AQUI, '..', '05-material', 'livro', 'manual',
                          '45-aptidoes-e-refino.md')
try:
    _tl = open(_LIVRO_KOK, encoding='utf-8').read()
except OSError:
    _tl = None
    pulou_kok = True

if _tl is not None:
    # 1. o gatilho: corpo a corpo, e o feitico de Toque FICA DE FORA
    if 'Toque' in _tl.split('### Kokusen')[1].split('###')[0]:
        erro('o livro poe o feitico de Toque no gatilho do kokusen e a peca 11 §6.6 poe '
             'so o corpo a corpo — um Toque Classe 7 com kokusen entrega 2,62x a Rotina '
             'contra 0,54x do corpo a corpo, que e 4,8x mais')
    # 2. o relogio: descanso longo, e nao "por cena"
    _rel_peca = 'zera no descanso longo' in PECA11
    _rel_livro = 'zera no descanso longo' in _tl
    if not _rel_peca:
        erro('a peca 11 parou de declarar o relogio da protecao contra azar do kokusen')
    elif not _rel_livro:
        erro('o livro publica um relogio diferente do da peca 11 para a protecao contra '
             'azar do kokusen — a peca MEDIU "por cena" e recusou, porque o acumulo so '
             'comeca no segundo critico da mesma cena e isso acontece em 4,4% das vezes')
    # 3. nenhuma das duas de melhoria exige a outra nem o kokusen base
    if 'ter tirado um `Kokusen`' in _tl:
        erro('o livro poe "ter tirado um Kokusen" como requisito das de melhoria, e a '
             'peca 11 §6.6 diz que nenhuma delas exige a outra')
    if not (_rel_peca and 'Toque' not in _tl.split('### Kokusen')[1].split('###')[0]
            and 'ter tirado um `Kokusen`' not in _tl):
        pass
    else:
        print('  [x] o kokusen do livro bate com o da peca nos tres eixos: gatilho, '
              'relogio e requisito')
# --- GATE DE APTIDAO: quem exige outra aptidao mora no MESMO grupo dela no livro.
# A peca 11 SS5 chama isso de gate de aptidao e cobra que a exigida seja "a mesma
# coisa em tamanho menor" — entao as duas sao a mesma familia, e separar as duas em
# grupos diferentes do livro poe o leitor procurando a escada na prateleira errada.
# Nasceu na v0.208, quando o Mizuki achou a `Circulacao` publicada dentro de
# `Aptidoes de kokusen`: ela e' gate da `Energia Reversa`, que mora em `Energia
# crua`. Nenhum validador olhava agrupamento, e o proprio texto do grupo ja
# denunciava — ele dizia "as duas aptidoes que melhoram essa fonte" com tres
# secoes embaixo.
if _tl is not None:
    _pares = re.findall(r'^### ([^·\n]+?)\s*·[^\n]*?exige a `([^`]+)`', PECA11, re.M)
    _pares += re.findall(r'^### ([^·\n]+?)\s+exige a `([^`]+)`', PECA11, re.M)
    _grupo, _g = {}, None
    for _l in _tl.split('\n'):
        _m = re.match(r'^(#{2,3}) (.+)$', _l)
        if _m and len(_m.group(1)) == 2:
            _g = _m.group(2).strip()
        elif _m:
            _grupo[_m.group(2).strip('` ').strip()] = _g
    if not _pares:
        erro('a peca 11 nao declara nenhum gate de aptidao no formato '
             '"### <nome> ... exige a `<outra>`" — ou o formato mudou, ou o gate de '
             'aptidao sumiu, e nos dois casos esta checagem parou de conferir algo')
    else:
        _fora = []
        for _a, _b in _pares:
            _a, _b = _a.strip('` ').strip(), _b.strip('` ').strip()
            _ga, _gb = _grupo.get(_a), _grupo.get(_b)
            if _ga is None or _gb is None:
                _fora.append(f'`{_a}` ou `{_b}` nao tem secao propria no capitulo 12 do '
                             f'livro (achei {_ga!r} e {_gb!r})')
            elif _ga != _gb:
                _fora.append(f'`{_a}` exige a `{_b}` e as duas estao em grupos '
                             f'diferentes do livro: "{_ga}" contra "{_gb}"')
        for _m in _fora:
            erro(_m)
        if not _fora:
            print(f'  [x] os {len(_pares)} gates de aptidao moram no mesmo grupo do '
                  'livro que a aptidao que eles exigem')

if not _regra_de_mundo:
    erro('a peca 11 parou de declarar o `Kokusen` base como regra de mundo — se ele '
         'voltar a ser entrada de catalogo, a pilha volta a custar tres marcos e esta '
         'conta muda junto')

if MULT_CONST and EMPILHAM:
    # so as DUAS de melhoria custam marco
    MARCOS_DA_PILHA = 2
    p_base = min(1.0, MULT_KOK * TETO_REFINO / 100)
    p_const = min(1.0, MULT_CONST * TETO_REFINO / 100)
    p_pilha = 1 - (1 - p_const) ** 2      # vantagem rola sobre a base ja subida
    print(f"  {'a ficha tem':<38}{'chance no d100':<17}{'dano por rodada':<18}"
          f"{'marcos':<9}{'x atributo, POR marco'}")
    linhas = [('so o Kokusen (de graca)', p_base, 0),
              ('Kokusen + Constante', p_const, 1),
              ('Kokusen + Melhorado', 1 - (1 - p_base) ** 2, 1),
              ('as TRES empilhadas', p_pilha, MARCOS_DA_PILHA)]
    for nome, p, marcos in linhas:
        g = dpr(p) / BASE - 1
        # v0.202: a linha do Kokusen base custa ZERO marco, e "por marco" nao existe
        # para ela. O traco e' a leitura certa: ela nao entra na comparacao de preco
        # porque ela nao tem preco.
        _por = f'{g / marcos / VALE_ATRIBUTO:.2f}x' if marcos else '—  (de graca)'
        print(f'  {nome:<38}{p:<17.0%}{f"+{g*100:.2f}%":<18}{marcos:<9}{_por}')
    g_pilha = dpr(p_pilha) / BASE - 1
    por_marco = g_pilha / MARCOS_DA_PILHA
    if por_marco > VALE_ATRIBUTO / 4:
        erro(f'a pilha de kokusen rende {por_marco:.2%} de dano por rodada POR MARCO '
             f'pago, e passou de um quarto do que um ponto de atributo compra — vale '
             f'montar ficha em cima dela')
    else:
        print(f'\n  A pilha inteira rende +{g_pilha*100:.2f}% por {MARCOS_DA_PILHA} marcos.')
        print(f'  Os mesmos {MARCOS_DA_PILHA} marcos em Corpo comprariam '
              f'+{MARCOS_DA_PILHA*VALE_ATRIBUTO*100:.0f}% — '
              f'{MARCOS_DA_PILHA*VALE_ATRIBUTO/g_pilha:.1f}x mais.')
        print('  Continua sendo escolha pelo grito, e nao pela planilha.')

print('\n  A cascata mexe SO na chance. O que aconteceria mexendo na margem:\n')
print(f"  {'escada':<34}{'dano por golpe':<18}{'contra a base'}")
p5 = min(1.0, MULT_KOK * 5 / 100)
for nome, v in [('nada muda (refino 5)', dpr(p5)),
                ('dobra a chance', dpr(min(1.0, p5 * 2))),
                ('margem cai para 19', dpr(p5, 19)),
                ('margem cai para 18', dpr(p5, 18))]:
    print(f'  {nome:<34}{v:<18.4f}+{(v/BASE-1)*100:.1f}%')
so_dado = dpr(0.0, 19) / BASE - 1
print(f'\n  Dos +{(dpr(p5,19)/BASE-1)*100:.1f}% da margem 19, {so_dado*100:.1f} pontos vem do DADO A MAIS,')
print('  antes de o kokusen entrar. A margem carrega o critico inteiro junto.')
if so_dado < teto_kok:
    erro('mexer na margem passou a valer menos que o proprio kokusen — a demonstracao '
         'de por que a cascata nao toca a margem parou de valer')


# --------------------------------------------------------------------------
bloco('5. AS TRES ROTAS DO MARCO — nenhuma domina')


# --------------------------------------------------------------------------
# O tamanho da lista de feiticos NAO fica escrito aqui. Ate a v0.98 ficava — a
# mesma linha `2 + nv // 2` estava a mao neste arquivo e no vizinho, e em
# nenhum documento. A peca 18 virou a dona na v0.99, e esta funcao le a coluna
# `espacos` da tabela dela.
# --------------------------------------------------------------------------
def _espacos_da_peca18():
    caminho = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                           '18-progressao.md')
    with open(caminho, encoding='utf-8') as fh:
        linhas = [l.strip() for l in fh if l.strip().startswith('|')]
    cab = [l for l in linhas if 'nível' in l and 'espaços' in l and 'refino' in l]
    if len(cab) != 1:
        raise ValueError('a peca 18 nao tem UMA tabela com as colunas nivel/espacos/'
                         'refino — ela mudou de forma e este leitor parou de funcionar')
    col = [c.strip() for c in cab[0].strip('|').split('|')].index('espaços')
    tab = {}
    for l in linhas[linhas.index(cab[0]) + 2:]:
        cel = [c.strip() for c in l.strip('|').split('|')]
        if len(cel) < col + 1:
            break
        nv = cel[0].strip('*')
        if not nv.isdigit():
            break
        tab[int(nv)] = int(cel[col].strip('*'))
    if sorted(tab) != list(range(1, 31)):
        raise ValueError(f'a coluna de espacos da peca 18 tem {len(tab)} niveis e '
                         f'deveria ter 30 — a tabela mudou de forma')
    return tab


ESPACOS_POR_NIVEL = _espacos_da_peca18()


def espacos(nv):
    """Espacos de feitico conhecido. Dono: a peca 18, secao 4."""
    return ESPACOS_POR_NIVEL[nv]



ROTAS = {
    'sempre Corpo':  [0] * 7,
    'sempre Refino': [1] * 7,
    'sempre Leque':  [2] * 7,
    # Corpo=0, Refino=1, Leque=2. A colocacao NAO e livre: ela tem que
    # reproduzir a curva que a peca 11 §3 publica para o meio a meio, e a
    # checagem 11 falha se deixar de reproduzir. Ate a v0.160 esta linha
    # tinha 2 escolhas de Refino e a curva publicada tem 3 — o mesmo nome
    # descrevendo duas rotas, em tres documentos.
    'meio a meio':   [1, 0, 1, 2, 1, 0, 2],
}
# quanto cada escolha de Leque devolve em espaco de feitico. Se este numero mudar,
# a checagem abaixo tem que acender — foi por ela NAO olhar o eixo dos feiticos que
# uma proposta de subir o Leque para 2 passou verde na v0.28 sem acender nada.
LEQUE_DA_FEITICOS = 1

print(f"  {'rota':<18}{'atributo':<11}{'refino':<9}{'aptidoes':<11}{'Passivas':<11}"
      f"{'feiticos a mais':<18}{'espacos totais'}")
# Quantas aptidoes a escolha de Refino entrega quando o refino JA esta no teto.
# LIDO DA PECA 11, e nao escrito aqui: ela e a dona da regra.
_m = re.search(r'voce leva `(\d+)` aptid', PECA11) or re.search(
    r'voc[eê] leva `(\d+)` aptid', PECA11)
if not _m:
    erro('nao achei na peca 11 quantas aptidoes a escolha de Refino da no teto — '
         'esta checagem e a 6 pararam de conferir')
    APT_NO_TETO = None
else:
    APT_NO_TETO = int(_m.group(1))
    print(f'  regra lida da peca 11: no teto, a escolha de Refino da {APT_NO_TETO} '
          f'aptidoes\n')


def simular(esc):
    """Roda os sete marcos e devolve (totais, o que cada OPCAO daria em cada marco).

    O segundo valor e o que a checagem 6 mede: no marco, o jogador compara as tres
    opcoes entre si, e o que ele ja acumulou muda o que cada uma vale."""
    ref, atr, apt, pas, fei = 1, 7, 0, 5, 0
    por_marco = []
    for e in esc:
        ref = min(TETO_REFINO, ref + 1)        # a linha passiva do marco
        # o que CADA opcao daria a este jogador, agora. Componentes:
        #   (atributo, refino, escada de Classe Passiva, feitico)
        # aptidao e Passiva entram na MESMA componente porque a peca 11 SS3 diz que
        # elas vivem na mesma escada — e essa e a afirmacao que faz as tres se
        # equilibrarem. Separadas, a dominancia nunca aparece.
        ganho_ref = min(TETO_REFINO, ref + 1) - ref
        # se a regra nao foi lida, o erro ja esta registrado la em cima. Aqui
        # a simulacao segue com 0 em vez de estourar: um guarda que acusa e
        # depois quebra esconde TODAS as outras acusacoes da mesma rodada.
        n_apt = (APT_NO_TETO or 0) if ganho_ref == 0 else 1
        por_marco.append({
            'Corpo':  (1, 0, 0, 0),
            'Refino': (0, ganho_ref, n_apt, 0),
            'Leque':  (0, 0, 1, LEQUE_DA_FEITICOS),
        })
        if e == 0:
            atr += 1
        elif e == 1:
            ref = min(TETO_REFINO, ref + 1)
            apt += n_apt
        else:
            fei += LEQUE_DA_FEITICOS
            pas += 1
    return (atr, ref, apt, pas, fei), por_marco


res, marcos_de = {}, {}
for nome, esc in ROTAS.items():
    res[nome], marcos_de[nome] = simular(esc)
    atr, ref, apt, pas, lq = res[nome]
    print(f'  {nome:<18}{atr:<11}{ref:<9}{apt:<11}{pas:<11}{lq:<18}'
          f'{espacos(30) + lq}')

# Nenhuma rota pode ser fraca em TODOS os eixos ao mesmo tempo. Os eixos sao CINCO,
# e ate a v0.28 esta checagem olhava so tres — ela ignorava o refino e os feiticos,
# que e justamente o eixo em que o Leque lidera. Uma mexida na moeda de feitico
# passava invisivel, e invisivel e pior que errado.
EIXOS = [(0, 'atributo'), (1, 'refino'), (2, 'aptidoes'), (3, 'Passivas'), (4, 'feiticos')]
for nome, meu in res.items():
    if nome == 'meio a meio':
        continue
    outras = [v for k, v in res.items() if k not in (nome, 'meio a meio')]
    if all(all(meu[i] <= o[i] for i, _ in EIXOS) for o in outras):
        erro(f'a rota "{nome}" perde ou empata nos CINCO eixos — ela esta dominada')

# e a recproca: nenhuma pode LIDERAR em todos, senao ela domina as outras
for nome, meu in res.items():
    if nome == 'meio a meio':
        continue
    outras = [v for k, v in res.items() if k not in (nome, 'meio a meio')]
    if all(all(meu[i] >= o[i] for i, _ in EIXOS) for o in outras):
        erro(f'a rota "{nome}" ganha ou empata nos CINCO eixos — ela DOMINA as outras, '
             'e as tres deixaram de se auto-equilibrar')

print('\n  Onde cada rota lidera:')
for i, eixo in EIXOS:
    lider = max(res, key=lambda k: res[k][i])
    topo = res[lider][i]
    empatados = [k for k in res if res[k][i] == topo]
    print(f'    {eixo:<12}{", ".join(empatados)}  ({topo})')
print('\n  Cada rota lidera em pelo menos um dos cinco e perde nos outros.')
print('  Nenhuma esta dominada, e nenhuma domina.')

# A dominancia entre rotas NAO pega inflacao da moeda: se o Leque dobrasse o que
# devolve, as tres continuariam trocando vantagem entre si e a checagem passaria.
# O que pega e uma trava direta no tamanho da moeda.
print()
print('  A moeda de feitico, medida de frente:')
maior = max(espacos(30) + res[k][4] for k in res)
menor = min(espacos(30) + res[k][4] for k in res)
print(f'    lista mais longa (sempre Leque)   {maior}')
print(f'    lista mais curta (sem Leque)      {menor}')
print(f'    espalhamento                      +{maior - menor} espacos, '
      f'{(maior/menor - 1) * 100:.0f}%')
if LEQUE_DA_FEITICOS != 1:
    erro(f'cada escolha de Leque devolve {LEQUE_DA_FEITICOS} feiticos, e a regra '
         'escrita e UM. O eixo do marco compra "mais um feitico, que so pode ser '
         'feitico" — dois fazem a rota devolver mais espaco do que a linha passiva '
         'do proprio marco, e ai o Leque deixa de ser uma troca e vira desconto')
if maior - menor > len(MARCOS):
    erro(f'a rota de Leque termina com {maior - menor} espacos a mais que as outras, '
         f'e existem so {len(MARCOS)} marcos — alguem esta devolvendo mais de um '
         'feitico por escolha')
else:
    print(f'\n    A rota de Leque termina com no maximo UM feitico por marco a mais.')
    print('    Essa e a trava: a moeda nao infla sem que esta linha acenda.')

print('\n  E o que faz as tres se equilibrarem sem trava:')
print('    Passiva e aptidao vivem na MESMA escada de Classe, entao "+1 feitico e')
print('    1 Passiva" empata com "+1 refino e 1 aptidao". O que sobra dos dois lados')
print('    e "+1 feitico" contra "+1 refino" — e refino nao vale NADA para quem nao')
print('    tem aptidao. Quem escolhe Leque nao quer refino; quem escolhe refino nao')
print('    quer Passiva. Nenhuma compra o que a outra compra.')

print('\n  O orcamento de espaco cobre a montagem mais pesada que o manual permite?\n')
MONTAGENS = [('so feitico', 0), ('3 Passivas Classe 2', 6),
             ('3 Passivas Classe 2 + Expansao completa', 6 + 3),
             ('5 Passivas Classe 3 + Expansao completa', 15 + 3)]
print(f"  {'montagem':<44}" + ''.join(f'nv{n:<7}' for n in (14, 20, 26, 30)))
for nome, custo in MONTAGENS:
    print(f'  {nome:<44}' + ''.join(f'{max(0, espacos(nv)-custo):<9}' for nv in (14, 20, 26, 30)))
pesada = MONTAGENS[-1][1]
if espacos(30) < pesada:
    erro(f'a montagem mais pesada pede {pesada} espacos e a ficha de nivel 30 tem '
         f'{espacos(30)} — o teto de cinco Passivas pagas do manual continua letra morta')
else:
    cabe_em = next(nv for nv in range(2, 31) if espacos(nv) >= pesada)
    print(f'\n  A montagem mais pesada cabe a partir do nivel {cabe_em}. Antes da v0.27 ela')
    print('  nao cabia em nivel nenhum, e o teto do manual era letra morta.')


# --------------------------------------------------------------------------
bloco('5.2. MARCO A MARCO — nenhuma das tres opcoes fica dominada em nenhum marco')

# A checagem 5 mede o FIM da campanha e sai verde com o meio quebrado: ate a v0.88
# a escolha de Refino entregava so a aptidao nos marcos 22, 26 e 30, porque o teto
# de refino ja tinha sido alcancado — e nos totais ela continuava liderando o eixo
# do refino com 10 contra 8. Contagem nao e valor (licao no 3), e total nao e marco.
#
# O EIXO DESTA: no marco, o jogador compara as TRES entre si, com o que ele ja tem.
#
# As componentes sao QUATRO e nao cinco, e a fusao e a afirmacao da peca 11 SS3:
# aptidao e Passiva vivem na MESMA escada de Classe Passiva. Separadas, "1 aptidao"
# e "1 Passiva + 1 feitico" nunca se comparam e a dominancia nunca aparece — que e
# exatamente por que ninguem viu isso em dezessete versoes.
COMPONENTES = ['atributo', 'refino', 'escada de Classe Passiva', 'feitico']

if APT_NO_TETO is None:
    erro('sem a regra do teto lida da peca 11, a 5.2 nao tem o que simular')
else:
    print('  Em cada marco, o que CADA opcao daria ao jogador daquela rota.')
    print('  aptidao e Passiva entram na mesma componente, que e o que a peca 11 afirma.\n')
    print(f"  {'rota':<16}{'marco':<8}{'Corpo':<14}{'Refino':<16}{'Leque':<14}veredito")
    achou52 = False
    for nome, marcos in marcos_de.items():
        for i, opcoes in enumerate(marcos):
            dominadas = []
            for a, va in opcoes.items():
                for b, vb in opcoes.items():
                    if a == b:
                        continue
                    if all(y >= x for x, y in zip(va, vb)) and any(
                            y > x for x, y in zip(va, vb)):
                        dominadas.append((a, b, va, vb))
            fmt = lambda v: '/'.join(str(x) for x in v)
            if dominadas:
                a, b, va, vb = dominadas[0]
                ver = f'>> {b} DOMINA {a}'
                achou52 = True
            else:
                ver = 'nenhuma domina'
            print(f"  {nome:<16}nv{MARCOS[i]:<6}{fmt(opcoes['Corpo']):<14}"
                  f"{fmt(opcoes['Refino']):<16}{fmt(opcoes['Leque']):<14}{ver}")
            for a, b, va, vb in dominadas:
                erro(f'{nome}, marco nv{MARCOS[i]}: a opcao "{a}" entrega {fmt(va)} e a '
                     f'"{b}" entrega {fmt(vb)} nas mesmas componentes '
                     f'({" / ".join(COMPONENTES)}) — quem escolher "{a}" ali esta '
                     f'levando menos por nada')
    if not achou52:
        print(f'\n  [x] Nos {len(MARCOS)} marcos das {len(marcos_de)} rotas, nenhuma das')
        print('      tres opcoes fica atras das outras em todas as componentes.')
        print(f'      A regra do teto — no maximo, Refino da {APT_NO_TETO} aptidoes — e o')
        print('      que segura os tres ultimos marcos da rota que sempre escolhe Refino.')


# --------------------------------------------------------------------------
bloco('5.3. AS DUAS BARREIRAS — o relogio e o que tira as duas da luta')

# A REGRA APLICADA: levantar uma barreira tem de custar MAIS do que uma luta dura.
# O LIMITE DE DESIGN e outro, e fica declarado aqui e nao la: uma barreira que
# caiba numa luta vale mais que a Trilha inteira da ficha, porque dano evitado
# converte 1 pra 1 e ela evita a propria vida.
#
# NADA DE VALOR ESCRITO AQUI: a vida das duas e o tempo de levantar saem da peca
# 11 SS6.6; a duracao de uma luta sai da peca 1 SS8; a parede do manual sai da
# copia da peca 11, que o conferir-manual.py 4i vigia contra o .docx.
_s66 = PECA11.split('## 6.6.')[1].split('\n## 7.')[0] if '## 6.6.' in PECA11 else ''
if not _s66:
    erro('a secao 6.6 (as duas barreiras) sumiu da peca 11 — esta checagem parou de conferir')
else:
    _p1 = os.path.join(AQUI, '01-atributos-acerto-defesa.md')
    with open(_p1, encoding='utf-8') as _f:
        _t1 = _f.read()
    _m = re.search(r'previsão atual é ([\d,]+) a ([\d,]+) rodadas', _t1)
    LUTA = float(_m.group(2).replace(',', '.')) if _m else None
    if LUTA is None:
        erro('nao achei a duracao de uma luta na peca 1 — o relogio das barreiras nao '
             'tem contra o que ser medido, e esta checagem parou de conferir')

    _mm = re.search(r'`1 minuto` são \*\*(\w+) rodadas\*\*', _s66)
    _palavra = {'dez': 10, 'nove': 9, 'oito': 8, 'seis': 6, 'cinco': 5}
    MINUTO = _palavra.get(_mm.group(1)) if _mm else None
    if MINUTO is None:
        erro('nao achei na peca 11 SS6.6 quantas rodadas tem o minuto de levantar')

    _vidas = {}
    for _nome, _rx in (('Barreira Simples', r'`(\d+) × refino` de pontos de vida'),
                       ('Cortina', r'`(\d+) × refino` de pontos de vida')):
        pass
    _achadas = re.findall(r'`(\d+) × refino` de pontos de vida', _s66)
    if len(_achadas) != 2:
        erro(f'achei {len(_achadas)} vida(s) de barreira na secao 6.6 e sao duas — '
             f'esta checagem parou de conferir')
        _achadas = []
    _m_ant = re.search(r'`(\d+) × Classe` de vida', _s66)
    ANTEPARO = int(_m_ant.group(1)) if _m_ant else None
    if ANTEPARO is None:
        erro('a secao 6.6 parou de citar a parede do manual — a vida da `Barreira '
             'Simples` deixou de ter contra o que ser comparada')

    if LUTA and MINUTO and len(_achadas) == 2 and ANTEPARO:
        _b, _c = int(_achadas[0]), int(_achadas[1])
        print(f'  levantar custa {MINUTO} rodadas; uma luta dura no maximo {LUTA}.')
        # 5.3a — o relogio
        if MINUTO <= LUTA:
            erro(f'levantar uma barreira custa {MINUTO} rodadas e uma luta dura ate '
                 f'{LUTA} — ela CABE na luta, e ai ela evita a propria vida: '
                 f'{_c*TETO_REFINO} de dano, que sao '
                 f'{_c*TETO_REFINO/LUTA/5.08:.2f} fatias contra uma Trilha de 5,00')
        else:
            print(f'  [x] o minuto nao cabe numa luta: {MINUTO} contra {LUTA} rodadas.')
        # 5.3b — o que elas valeriam SE coubessem. Contra-prova do limite de design.
        print(f"\n  {'se coubesse numa luta':<28}{'evita':<14}{'por rodada':<14}{'em fatias'}")
        for _n, _k in (('Barreira Simples', _b), ('Cortina', _c)):
            _v = _k * TETO_REFINO
            print(f'  {_n:<28}{f"{_v} de dano":<14}{f"{_v/LUTA:.1f}":<14}'
                  f'{_v/LUTA/5.08:.2f}')
        print('  (uma Trilha inteira leva 5,00 fatias — e por isso que o relogio existe)')
        # 5.3c — a menor das duas fica abaixo da maior parede que um feitico monta
        CLASSE_MAX = 7
        if _b * TETO_REFINO >= ANTEPARO * CLASSE_MAX:
            erro(f'a `Barreira Simples` tem {_b*TETO_REFINO} de vida no teto e a maior '
                 f'parede do manual tem {ANTEPARO*CLASSE_MAX} — a que custa um marco e '
                 f'e permanente na ficha passou a que custa pontos e sai numa acao')
        else:
            print(f'\n  [x] a `Barreira Simples` tem {_b*TETO_REFINO} no teto, abaixo dos '
                  f'{ANTEPARO*CLASSE_MAX} da maior parede do manual.')
        # 5.3d — o quinto formato tem de estar DECLARADO na secao 5
        _s5 = PECA11.split('## 5. ')[1].split('\n## 6.')[0] if '## 5. ' in PECA11 else ''
        if 'gate de aptidão' not in _s5:
            erro('a `Cortina` usa um gate de aptidao e a secao 5 nao declara esse '
                 'formato — foi exatamente isso que a v0.65 derrubou: a dependencia '
                 'existindo sem ninguem ter escrito que ela podia')
        else:
            print('  [x] o quinto formato de gate esta declarado na secao 5.')

# --------------------------------------------------------------------------
bloco('5.4. APTIDAO PROPRIA — a unica entrada escrita NA MESA')

# Ela e a unica das catorze cujo conteudo nao esta no repositorio: o jogador e o
# mestre escrevem. Entao o que tem de ser conferido nao e o efeito — e a CERCA.
#
# NADA DE VALOR ESCRITO AQUI: a escada de frequencia sai da secao 6.7 da peca 11,
# que copiou do manual; o conferir-manual.py 4j vigia essa copia contra o .docx.
_s67 = PECA11.split('## 6.7.')[1].split('\n## 7.')[0] if '## 6.7.' in PECA11 else ''
if not _s67:
    erro('a secao 6.7 (Aptidao Propria) sumiu da peca 11 — esta checagem parou de conferir')
else:
    # 5.4a — o teto de Classe Passiva. Ele e a trava inteira: 3 e permanente.
    if not re.search(r'Classe Passiva 1 ou 2, nunca 3', _s67):
        erro('a secao 6.7 parou de dizer `Classe Passiva 1 ou 2, nunca 3` — sem esse '
             'teto a `Aptidao Propria` alcanca o permanente, e permanente e a unica '
             'coisa que ela nunca pode ser')
    else:
        print('  [x] o teto e `Classe Passiva 1 ou 2, nunca 3`.')

    # 5.4b — a escada de frequencia bate com os TRES degraus da secao 4
    _s4b = PECA11.split('## 4. ')[1].split('\n## 5.')[0] if '## 4. ' in PECA11 else ''
    _faixas = re.findall(r'\| \*\*(uma|metade|quase toda)\*\* \| (Leve|Média|Pesada) \| '
                         r'\*\*Classe Passiva (\d)\*\*', _s67)
    if len(_faixas) != 3:
        erro(f'achei {len(_faixas)} faixa(s) na escada de frequencia da 6.7 e sao tres — '
             f'a ponte entre a pergunta do manual e a escada da secao 4 se desfez')
    else:
        _esperado = [('uma', 'Leve', '1'), ('metade', 'Média', '2'), ('quase toda', 'Pesada', '3')]
        if _faixas != _esperado:
            erro(f'a escada de frequencia da 6.7 saiu {_faixas} e a ordem tem de ser '
                 f'{_esperado} — condicional dispara pouco, reativo dispara em parte, '
                 f'permanente dispara sempre')
        else:
            print('  [x] as tres faixas de frequencia caem nos tres degraus da secao 4.')
        # e os tres degraus citados existem mesmo na escada da secao 4
        for _n in ('1', '2', '3'):
            if f'**{_n}**' not in _s4b:
                erro(f'a 6.7 mapeia para a Classe Passiva {_n} e a escada da secao 4 nao '
                     f'tem esse degrau — as duas deixaram de falar da mesma escada')

    # 5.4c — os cinco requisitos. A cerca e o que sobra quando o conteudo e da mesa.
    _req = re.findall(r'^\d\. \*\*(.+?)\*\*', _s67, re.M)
    if len(_req) != 5:
        erro(f'a secao 6.7 lista {len(_req)} requisito(s) para a `Aptidao Propria` e sao '
             f'cinco — a cerca e a unica coisa que um segundo mestre tem para ler')
    else:
        print(f'  [x] os cinco requisitos estao escritos: {", ".join(_req)}.')

    # 5.4d — o desempate tem de reprovar, e nao aprovar
    if 'na dúvida, Pesada' not in _s67.lower().replace('na dúvida, pesada', 'na dúvida, Pesada'):
        if 'dúvida' not in _s67:
            erro('a secao 6.7 nao diz o que fazer na duvida — e o desempate e o unico '
                 'lugar do sistema em que "nao sei" precisa ter resposta escrita')
    if 'dúvida reprova' not in _s67:
        erro('a secao 6.7 parou de dizer que a duvida REPROVA a proposta — se o '
             'desempate aprovar, sete mesas aprovam sete coisas')
    else:
        print('  [x] na duvida a proposta e recusada, e nao aceita.')

# --------------------------------------------------------------------------
bloco('6. O TETO DE PASSIVAS — a gratis traz a propria vaga')
TETO_BASE = 5
print(f"  {'escolhas de Leque':<20}{'teto':<8}{'gratis':<9}{'pagas que sobram'}")
for n in range(0, 8):
    teto = TETO_BASE + n
    pagas = teto - n
    print(f'  {n:<20}{teto:<8}{n:<9}{pagas}')
    if pagas != TETO_BASE:
        erro(f'com {n} escolhas de Leque sobram {pagas} Passivas pagas, e deveriam ser '
             f'{TETO_BASE} — o teto esta crescendo de verdade em vez de abrir vaga')
print(f'\n  As pagas continuam sendo {TETO_BASE} em toda a escada. O teto nao cresce:')
print('  ele abre lugar para o que a rota concede.')


# --------------------------------------------------------------------------
bloco('7. OS GATES DE REFINO separam as rotas?')
GATE_REFINO = {1: 1, 2: 4, 3: 7}
GATE_NIVEL = {1: 1, 2: 7, 3: 13}
print(f"  {'gate':<28}{'especialista':<16}{'meio a meio':<16}{'generalista'}")
for cl in (1, 2, 3):
    linha = f'  Classe {cl} (refino {GATE_REFINO[cl]}, nivel {GATE_NIVEL[cl]}){"":<3}'
    abre = {}
    for rota in CURVA:
        nv = next((m for i, m in enumerate(MARCOS)
                   if CURVA[rota][i] >= GATE_REFINO[cl] and m >= GATE_NIVEL[cl]), None)
        abre[rota] = nv
        linha += f'{("nv " + str(nv)) if nv else "nunca":<16}'
    print(linha)
    if cl == 3:
        e, g = abre['especialista'], abre['generalista']
        if e is None:
            erro('nem o especialista alcanca a Classe 3 — o gate esta alto demais')
        elif g is not None and g - e < 8:
            erro(f'o gate de Classe 3 separa o especialista do generalista por so '
                 f'{g-e} niveis — refino deixou de significar acesso')
        else:
            print(f'\n  {(g or 31) - e} niveis entre quem investiu e quem nao investiu na Classe 3.')

# so nivel nao serve, e a checagem mostra por que
so_nivel = {}
for rota in CURVA:
    so_nivel[rota] = next((m for m in MARCOS if m >= GATE_NIVEL[3]), None)
if len(set(so_nivel.values())) == 1:
    print('  Com gate SO de nivel, as tres rotas abririam a Classe 3 no mesmo nivel '
          f'({so_nivel["especialista"]}) — e ai o refino nao compraria acesso nenhum.')
else:
    aviso('o gate so de nivel passou a separar as rotas — a justificativa do gate '
          'de refino precisa ser reescrita')


# =============================================================================
# N. A ESCADA DE FORMATO TEM NOME DE DUAS PALAVRAS, e nunca "Classe" solta
#
# Entrou na v0.64, e ela existe por um defeito medido na conversa e nao no codigo:
# o Mizuki leu a regua de Trilha inteira e parou em "Classe? para mim Classe e
# feiticо". Ele estava certo — o GLOSSARIO DO MANUAL diz "Classe: o tamanho do
# feitico, de 0 a 7", uma escala so'. O eixo de FORMATO desta peca (pequeno e
# condicional / reativo com limite / permanente) vivia pegando a palavra
# emprestada, e o leitor nao tinha como saber qual das duas estava lendo.
#
# O conserto e o idioma do proprio manual — ele ja escreve "Passiva de Classe 2"
# e "Classe de Passiva" quando precisa desambiguar. Feitio, Talhe, Lavra, Feicao
# e Formato sairam LIVRE na triagem e foram RECUSADOS: inventar palavra para o
# que o manual sabe dizer cria a segunda fonte da licao nº 9.
#
# NADA DE VALOR FICA ESCRITO AQUI: as tres alturas e o que cabe em cada uma saem
# da tabela da SS4. O que esta checagem afirma e a FORMA do nome, nao o conteudo.
#
# O QUE TEM DE ACENDER: o cabecalho da tabela voltar a "Classe"; a regra do nome
# sumir; qualquer altura sumir da tabela.
# CONTRA-TESTE: mexer no TEXTO do que cabe em cada altura nao pode acender — esta
# checagem e sobre o nome, e quem confere o conteudo sao as checagens de cima.
bloco('N. O NOME DA ESCADA DE FORMATO')

_p11 = os.path.join(AQUI, '11-aptidoes-e-refino.md')
_t11 = open(_p11, encoding='utf-8').read()
_s4 = _t11.split('## 4. ')[1].split('\n## 5.')[0] if '## 4. ' in _t11 else ''

if not _s4:
    erro('nao achei a secao 4 da peca 11 — a escada de formato mudou de lugar')
else:
    if 'Classe' not in _s4.split('\n')[0] or 'Passiva' not in _s4.split('\n')[0]:
        erro('o titulo da secao 4 nao diz "Classe Passiva" — o eixo de formato '
             'voltou a se chamar so "Classe", que e a palavra do TAMANHO DO '
             'FEITICO no glossario do manual')
    _regra = [l for l in _s4.split('\n')
              if 'nunca' in sem_acento(l).lower() and 'solta' in sem_acento(l).lower()]
    if not _regra:
        erro('a secao 4 nao declara mais que o nome nunca vem sozinho — sem essa '
             'linha nada impede a proxima peca de escrever "Classe 2" querendo '
             'dizer formato')
    else:
        print('  [x] a regra do nome esta escrita:',
              ' '.join(_regra[0].replace('>', '').replace('*', '').split())[:78])
    _cab = [l for l in _s4.split('\n') if l.strip().startswith('| Classe')]
    if not _cab:
        erro('a tabela da secao 4 nao tem cabecalho comecando por "Classe"')
    elif 'Classe Passiva' not in _cab[0]:
        erro(f'a tabela da secao 4 tem cabecalho "{_cab[0].strip()[:40]}" — ela precisa '
             'dizer "Classe Passiva", senao a coluna de alturas fica indistinguivel '
             'da Classe de feitico')
    else:
        _alturas = [l for l in _s4.split('\n')
                    if re.match(r'\|\s*\*\*[123]\*\*\s*\|', l.strip())]
        if len(_alturas) != 3:
            erro(f'a tabela da secao 4 tem {len(_alturas)} altura(s) e a escada tem tres')
        else:
            print(f'  [x] cabecalho "Classe Passiva" e as tres alturas na tabela.')
    # ARMADILHA Nº 4 DO PROJETO: esta secao contem o texto que a checagem procura
    # para reprovar, porque ela EXPLICA a ambiguidade citando o manual. Entao a
    # varredura pula a linha que esta citando o manual — e so' ela. Sem esta
    # excecao a checagem reprovaria a propria secao que existe para consertar o
    # problema, que e o modo de falha mais chato deste projeto.
    _soltas, _isentas = [], 0
    for _l in _s4.split('\n'):
        _achou = re.findall(r'(?<!Passiva )(?<!Passivas )\bClasse [123]\b', _l)
        if not _achou:
            continue
        if 'manual' in sem_acento(_l).lower():
            _isentas += 1
            continue
        _soltas += _achou
    if _soltas:
        erro(f'a secao 4 escreve "Classe N" solta {len(_soltas)}x '
             f'({sorted(set(_soltas))}) fora de citacao do manual — dentro da secao '
             'que existe para proibir isso')
    else:
        print(f'  [x] nenhuma "Classe N" solta na secao 4 fora das {_isentas} linha(s) '
              'que citam o manual.')

# --------------------------------------------------------------------------
# CONTRA-TESTE: cada checagem abaixo le o numero do DOCUMENTO, nunca do codigo.
# A cura no teto e a ancora da Recomposicao sao lidas do texto da secao 6; mexer
# em qualquer uma das duas move a comparacao, que e o que se quer.
bloco('N+1. A APTIDAO `Energia Reversa` — v0.78')

_s6 = _t11.split('### Energia Reversa')[1].split('\n## 6.5.')[0] \
      if '### Energia Reversa' in _t11 else ''

if not _s6:
    erro('nao achei a entrada `Energia Reversa` na secao 6 da peca 11 — ela fechou '
         'na v0.77 e a Trilha `Sutura` do Guia aponta para ela')
else:
    # 1. o gate esta no titulo, e ele e o mesmo da Extensao de Dominio
    _tit = _s6.split('\n')[0]
    _falta = [x for x in ('Classe Passiva 3', 'refino 7', 'nível 13') if x not in _tit]
    if _falta:
        erro(f'o titulo da `Energia Reversa` nao declara {_falta} — sem o gate escrito '
             'no titulo ela vira aptidao sem requisito, e a secao 5 diz que cada uma '
             'declara o proprio')
    else:
        print('  [x] gate no titulo: Classe Passiva 3, refino 7 e nivel 13.')

    # 2. o gate bate com o da Extensao de Dominio, que e a outra Classe Passiva 3
    _ext = _t11.split('### Extensão de Domínio')[1].split('\n')[0] \
           if '### Extensão de Domínio' in _t11 else ''
    if _ext and ('refino 7' in _ext) != ('refino 7' in _tit):
        erro('a `Energia Reversa` e a `Extensão de Domínio` sao as duas Classe Passiva 3 '
             'e os gates de refino divergiram — a secao 5 preca a ALTURA, nao a entrada')
    elif _ext:
        print('  [x] o gate bate com o da Extensão de Domínio, a outra Classe Passiva 3.')

    # 3. a cura no teto NAO pode passar a Passiva Recomposicao, que e a ancora
    #    declarada. Os dois numeros sao lidos do texto.
    # o [^`]* aceita formula suja (`1d8 + refino`) de proposito: sem ele, uma
    # perturbacao que enfia refino na formula acende a checagem ERRADA — a de
    # "nao consegui ler" em vez da de refino. Vermelho pelo motivo errado ensina
    # a procurar o defeito no lugar em que ele nao esta.
    _mdado = re.search(r'recupere `1d(\d+)[^`]*` de vida', _s6)
    _mrec  = re.search(r'`(\d+) × maior Classe`', _s6)
    if not _mdado or not _mrec:
        erro('nao consegui ler do texto o dado de cura e a ancora `N × maior Classe` — '
             'sem os dois a checagem viraria constante escrita no validador')
    else:
        _face = int(_mdado.group(1))
        _mult = int(_mrec.group(1))
        _classe_max = 7
        _teto_er  = _classe_max * (_face + 1) / 2
        _recomp   = _mult * _classe_max
        print(f'  [x] no nivel 30: Energia Reversa {_classe_max}d{_face} = {_teto_er:.1f} '
              f'de cura, Recomposicao = {_recomp}.')
        if _teto_er > _recomp:
            erro(f'a `Energia Reversa` cura {_teto_er:.1f} no teto contra os {_recomp} da '
                 f'Passiva `Recomposição` — a aptidao APRENDIDA passou a inata, e a '
                 f'secao 7 mandava medir uma contra a outra')

    # 4. o teto e' a `maior Classe` e nao o refino — MEDIDO, e nao procurado.
    #
    #    Ate a v0.170 esta sub-checagem so perguntava se a palavra `refino`
    #    aparecia na formula, e a mensagem de erro dizia "a secao 2 proibe".
    #    Duas coisas erradas na mesma linha: ela media o MARCADOR em vez do
    #    fenomeno, e o motivo que ela citava tinha morrido na v0.158, quando
    #    dano saiu da lista da §2. Cura e' `magnitude fora de disputa` — a §2
    #    nao proibe. Quem decide e' o EMPATE, e ele nunca tinha sido medido.
    #
    #    A regua: a rodada gasta curando cancela a rodada de apanhar. Cura sai
    #    do teto declarado no texto; o que voce toma sai do golpe de chefe da
    #    tabela de inimigo vezes o acerto da peca 1 §6. Nenhum dos dois esta
    #    escrito aqui.
    #
    #    BANDA_EMPATE e' LIMITE DE DESIGN, e por isso mora no codigo — a
    #    excecao que a licao no 8 abre. Ela existe para ser comparada com a
    #    regra aplicada, que e lida do texto.
    BANDA_EMPATE = (0.80, 1.10)
    NIVEIS_ER = (14, 18, 22, 26, 30)   # do gate (refino 7) ao teto de nivel

    _mregra = re.search(r'Gaste até `([^`]+)` de PE e recupere `1d(\d+)', _s6)
    if not _mregra:
        erro('nao consegui ler a LINHA DE REGRA da `Energia Reversa` — sem o teto e o '
             'dado, a banda do empate abaixo nao teria com que ser calculada, e esta '
             'sub-checagem sairia verde sem ter medido nada')
    else:
        _teto_txt, _face_er = _mregra.group(1), int(_mregra.group(2))
        _por_pe = (_face_er + 1) / 2

        def _teto_em(nv):
            t = sem_acento(_teto_txt).lower()
            if 'maior classe' in t:
                return CLASSE_NO_NIVEL[nv], 'maior Classe'
            if 'refino' in t:
                return refino_em('especialista', nv), 'refino'
            return None, _teto_txt

        _fora = []
        print(f"\n  {'nv':<5}{'teto':<7}{'cura':<9}{'a rodada tira':<16}{'cobre':<8}")
        for _nv in NIVEIS_ER:
            _t, _nome = _teto_em(_nv)
            if _t is None:
                erro(f'o teto da `Energia Reversa` virou "{_teto_txt}", e esta checagem '
                     f'so sabe medir `maior Classe` e `refino` — ensine o eixo novo a '
                     f'ela antes de publicar, senao ela para de medir em silencio')
                break
            _cura = _t * _por_pe
            _tira = golpe_chefe(_nv) * ACERTO_DIFICIL
            _cob = _cura / _tira
            print(f'  {_nv:<5}{_t:<7}{_cura:<9.1f}{_tira:<16.1f}{_cob:<8.0%}')
            if not BANDA_EMPATE[0] <= _cob <= BANDA_EMPATE[1]:
                _fora.append((_nv, _cob))
        else:
            if _fora:
                erro(f'com o teto em `{_nome}` a cura sai da banda do empate '
                     f'{BANDA_EMPATE[0]:.0%}-{BANDA_EMPATE[1]:.0%} em '
                     + ', '.join(f'nv{n} ({c:.0%})' for n, c in _fora)
                     + ' — a rodada de cura deixa de ser uma rodada COMPRADA e vira '
                       'uma rodada ganha')
            else:
                print(f'  [x] o teto em `{_nome}` empata a faixa inteira, dentro de '
                      f'{BANDA_EMPATE[0]:.0%}-{BANDA_EMPATE[1]:.0%}.')

        # 4.1 e a tabela publicada na peca e' recontada, celula a celula
        _pub = {}
        for _l in _s6.split('\n'):
            _m = re.match(r'\|\s*(\d+)\s*\|(.+)\|\s*$', _l)
            if not _m or int(_m.group(1)) not in NIVEIS_ER:
                continue
            _vals = re.findall(r'`([\d,]+)%?`', _m.group(2))
            if len(_vals) == 7:
                _pub[int(_m.group(1))] = [float(v.replace(',', '.')) for v in _vals]
        if len(_pub) != len(NIVEIS_ER):
            erro(f'a tabela do empate da `Energia Reversa` tem {len(_pub)} das '
                 f'{len(NIVEIS_ER)} linhas legiveis — extrator que para de achar '
                 f'sai verde calado')
        else:
            _ruins = []
            for _nv, _lido in _pub.items():
                _tira = golpe_chefe(_nv) * ACERTO_DIFICIL
                _cl, _rf = CLASSE_NO_NIVEL[_nv], refino_em('especialista', _nv)
                _alvo = [_tira,
                         _cl, _cl * _por_pe, round(_cl * _por_pe / _tira * 100),
                         _rf, _rf * _por_pe, round(_rf * _por_pe / _tira * 100)]
                if any(abs(a - b) > 0.06 for a, b in zip(_alvo, _lido)):
                    _ruins.append((_nv, _lido, [round(x, 1) for x in _alvo]))
            if _ruins:
                for _nv, _l, _a in _ruins:
                    erro(f'a linha do nivel {_nv} da tabela do empate publica {_l} e a '
                         f'conta da {_a}')
            else:
                print(f'  [x] as {len(_pub)} linhas publicadas da tabela do empate '
                      f'reconstroem da tabela de inimigo e da escada de Classe.')

    # 5. LIÇÃO Nº 9, GENERALIZADA na v0.90: o gate de cada aptidao mora no titulo
    #    da secao 6 ou 6.5 E na tabela do catalogo da secao 10. Dois donos para o
    #    mesmo numero, catorze vezes.
    #
    #    Ate a v0.90 esta checagem so olhava a `Energia Reversa`, escrita no braco.
    #    Perturbando o gate da `Kokusen Constante` no catalogo, ela saia VERDE —
    #    treze das catorze entradas nao tinham ninguem comparando as duas copias.
    #
    #    A direcao e de MAO UNICA, no molde da checagem 9 do conferir-catalogo:
    #    o titulo e o dono, e a tabela pode dizer mais (a `Aptidão Própria` carrega
    #    "uma vez na ficha", que nao e gate). Ela nao pode dizer MENOS nem OUTRO.
    def _gates(s):
        s = sem_acento(s).lower()
        g = set()
        for _mm in re.finditer(r'classe passiva (\d+)', s):
            g.add(f'Classe Passiva {_mm.group(1)}')
        _s2 = re.sub(r'classe passiva \d+', '', s)
        for _mm in re.finditer(r'classe (\d+)', _s2):
            g.add(f'Classe {_mm.group(1)}')
        for _mm in re.finditer(r'refino (\d+)', s):
            g.add(f'refino {_mm.group(1)}')
        for _mm in re.finditer(r'nivel (\d+)', s):
            g.add(f'nivel {_mm.group(1)}')
        if 'sem gate' in s:
            g.add('sem gate')
        if 'gratis' in s:
            g.add('gratis')
        # o QUINTO formato, da v0.91: "exige a `Barreira Simples`". Sem esta linha
        # o gate da `Cortina` nao produz token nenhum dos dois lados, e a
        # comparacao passa TRIVIALMENTE — um formato de gate inteiro sem ninguem
        # conferindo as duas copias dele.
        for _mm in re.finditer(r'exige a `([^`]+)`', s):
            g.add(f'exige {_mm.group(1)}')
        return g

    _titulos = {}
    for _l in _t11.split('\n'):
        if _l.startswith('### '):
            _corpo = _l[4:]
            _nome = _corpo.split('·')[0].strip()
            _titulos[sem_acento(_nome).lower().strip()] = (_corpo, _gates(_corpo))

    _cat = _t11.split('### O catálogo fechado')[1] if '### O catálogo fechado' in _t11 else ''
    if not _cat:
        erro('nao achei a tabela do catalogo na secao 10 — esta checagem parou de conferir')
    _pares, _divs = 0, 0
    for _l in _cat.split('\n'):
        _mm = re.match(r'\|\s*(\d+)\s*\|\s*\*\*(.+?)\*\*\s*\|\s*(.*?)\s*\|', _l)
        if not _mm:
            continue
        _nome, _cel = _mm.group(2), _mm.group(3)
        _k = sem_acento(_nome).lower().strip()
        if _k not in _titulos:
            continue          # ainda nao tem secao propria: e uma das que faltam
        if 'a definir' in _cel:
            erro(f'a tabela do catalogo diz "a definir" para `{_nome}`, e ela JA tem '
                 f'secao escrita na peca — e a licao nº 9 com a regra de um lado e '
                 f'a tabela de resumo do outro')
            _divs += 1
            continue
        _pares += 1
        _falta = _titulos[_k][1] - _gates(_cel)
        if _falta:
            erro(f'`{_nome}`: o titulo da secao pede {sorted(_falta)} e a linha do '
                 f'catalogo diz "{_cel[:50]}" — as duas copias do gate divergiram')
            _divs += 1
    # v0.202: o catalogo foi de catorze para treze quando o `Kokusen` base saiu da
    # lista e virou regra de mundo. O numero nao esta escrito aqui: ele e' contado
    # da tabela do §7 da propria peca, que e' a dona da lista. Guarda escrita a mao
    # envelhece na versao seguinte, e esta ja envelheceu uma vez.
    _mn = re.search(r'^\| (\d+) \| `Aptidão Própria`', PECA11, re.M)
    _esperadas = int(_mn.group(1)) if _mn else None
    if _esperadas is None:
        erro('nao achei a ultima linha numerada da tabela do §7 da peca 11 — e dela que '
             'sai quantas entradas o catalogo tem')
    elif _pares < _esperadas:
        erro(f'so {_pares} entrada(s) do catalogo tem secao para comparar, e a tabela do '
             f'§7 numera {_esperadas} — alguem mudou o formato do titulo e esta checagem '
             f'esta conferindo menos')
    elif not _divs:
        print(f'  [x] as {_pares} entradas com secao repetem o gate dela no catalogo.')

    # 6. e ela nao pode continuar na lista das que FALTAM
    _s7 = _t11.split('## 7. ')[1].split('\n## 8.')[0] if '## 7. ' in _t11 else ''
    _faltantes = [l for l in _s7.split('\n')
                  if l.strip().startswith('|') and '**' in l and 'aptidão' not in l
                  and '---' not in l]
    if any('Energia Reversa' in l for l in _faltantes):
        erro('a `Energia Reversa` continua na tabela das que faltam na secao 7, e ela '
             'esta escrita na secao 6 — decisao registrada nao e decisao aplicada')
    else:
        print(f'  [x] ela saiu da lista das que faltam: restam {len(_faltantes)}.')


# --------------------------------------------------------------------------
# A CLASSE PASSIVA NUNCA VEM SOZINHA — a regra da secao 4, aplicada a peca inteira.
#
# LIMITE DE DESIGN, declarado aqui a parte da regra aplicada: quantas ocorrencias na
# forma correta existiam quando esta checagem entrou. Se o numero CAIR, alguem
# reescreveu as Passivas e a checagem passou a conferir menos em silencio.
CLASSE_PASSIVA_MINIMO = 53

print()
print('=' * 90)
print('A CLASSE PASSIVA NUNCA VEM SOZINHA — a secao 4 conferida contra a peca inteira')
print('=' * 90)

_ini, _fim = PECA11.find('## 4. '), PECA11.find('## 5. ')
_S4 = set(PECA11[_ini:_fim].split('\n')) if _ini >= 0 else set()

# a escada le-se da tabela da propria secao 4 — o valor mora la, nao aqui
_degraus = sorted({int(d) for d in re.findall(r'^\|\s*\*\*([0-9])\*\*\s*\|',
                                             PECA11[_ini:_fim], re.M)})
if not _degraus:
    erro('nao consegui ler os degraus da escada de Classe Passiva da tabela da secao 4 — '
         'ela mudou de formato e esta checagem parou de conferir')
else:
    print(f'  a escada da secao 4 tem os degraus {_degraus}; fora deles, `Classe N` e feitico')
    _soltas, _boas = [], 0
    for _i, _l in enumerate(PECA11.split('\n'), 1):
        for _m in re.finditer(r'Classe\s+([0-7])\b', _l):
            if re.search(r'(Passivas?)\s*(de\s*)?$', _l[max(0, _m.start() - 30):_m.start()]):
                _boas += 1
                continue
            if int(_m.group(1)) not in _degraus:
                continue                      # Classe 0 e 4..7 nao existem como Passiva
            if _l in _S4:
                continue                      # a secao 4 e a que EXPLICA a ambiguidade
            _soltas.append((_i, _l[max(0, _m.start() - 55):_m.end() + 30].strip()))
    _boas += len(re.findall(r'Classe Passiva\s+([1-3])\b', PECA11))

    for _i, _ctx in _soltas:
        erro(f'peca 11 linha {_i}: `Classe` solta onde ela fala de Passiva, e a secao 4 '
             f'exige as duas palavras -> ... {_ctx} ...')
    print(f'  {_boas} ocorrencia(s) na forma correta, e {len(_soltas)} solta(s) fora da secao 4')
    if _boas < CLASSE_PASSIVA_MINIMO:
        erro(f'so {_boas} ocorrencia(s) na forma correta e o minimo declarado e '
             f'{CLASSE_PASSIVA_MINIMO} — alguem reescreveu as Passivas e esta checagem '
             f'passou a conferir menos do que conferia')
    if not _soltas:
        print('  [x] nenhuma Classe de Passiva aparece sem as duas palavras.')

# --------------------------------------------------------------------------
bloco('8. A CURVA DAS TRES ROTAS — ela cai da regra, e nao da tabela')
# --------------------------------------------------------------------------
# A curva veio do 02-esqueleto/arquitetura.md §4.3 para a peca 11 §3 na v0.104:
# ela era a ultima fonte de progressao do projeto fora de uma peca de regra.
# Aqui ela nao e' conferida contra copia nenhuma: e' RECONSTRUIDA da regra —
# refino comeca em 1, sobe +1 de graca em cada marco, a escolha pode somar mais
# +1, e o teto e 10. Se a tabela publicada divergir da regra, uma das duas esta
# errada, e a checagem nao decide qual: ela acusa.
MARCOS = [6, 10, 14, 18, 22, 26, 30]
TETO_REFINO = 10
def _curva(escolhe):
    r, saida = 1, []
    for _ in MARCOS:
        r = min(TETO_REFINO, r + 1 + (1 if escolhe else 0))
        saida.append(r)
    return saida
_ROTAS = [('especialista', _curva(True)), ('generalista', _curva(False))]
_sec = PECA11[PECA11.find('### A curva das três rotas, marco a marco'):]
_sec = _sec[:_sec.find('\n### ')] if '\n### ' in _sec else _sec
if not _sec:
    erro('6: nao achei a secao da curva das tres rotas na peca 11 — ou ela nao veio '
         'do arquitetura.md, ou mudou de titulo e esta checagem parou de conferir')
else:
    _pub = {}
    for _l in _sec.split('\n'):
        _m = re.match(r'^\|\s*\*\*(\w[\w ]*?)\*\*[^|]*\|(.+)\|\s*$', _l)
        if _m:
            _vals = re.findall(r'`?(\d+)`?', _m.group(2))
            if len(_vals) == len(MARCOS):
                _pub[_m.group(1).strip().lower()] = [int(x) for x in _vals]
    if len(_pub) != 3:
        erro(f'6: li {len(_pub)} rota(s) na tabela da curva e esperava 3 — ela mudou '
             'de forma e esta checagem parou de conferir')
    else:
        for _nome, _esp in _ROTAS:
            if _pub.get(_nome) != _esp:
                erro(f'6: a rota "{_nome}" publica {_pub.get(_nome)} e a regra '
                     f'reconstroi {_esp}')
        _mm = _pub.get('meio a meio')
        if _mm and not all(g <= m <= e for m, e, g in
                           zip(_mm, _ROTAS[0][1], _ROTAS[1][1])):
            erro(f'6: a rota "meio a meio" ({_mm}) sai da faixa entre o generalista '
                 f'e o especialista')
        if not ERROS:
            print(f'  marcos lidos da regra: {MARCOS}, teto {TETO_REFINO}')
            for _n, _v in _pub.items():
                print(f'     {_n:<14} {_v}')
            print('  [x] as duas rotas puras reconstroem da regra, e o meio a meio '
                  'fica entre elas')
        # o gate da secao 5 e' esta curva lida em coluna: o especialista alcanca
        # refino 7 no nivel 14 e o generalista so no 26.
        if _pub.get('especialista') and _pub.get('generalista'):
            _n14 = MARCOS[_pub['especialista'].index(
                next(v for v in _pub['especialista'] if v >= 7))]
            _n26 = MARCOS[_pub['generalista'].index(
                next(v for v in _pub['generalista'] if v >= 7))]
            if (_n14, _n26) != (14, 26):
                erro(f'6: o refino 7 cai no nivel {_n14} para o especialista e no '
                     f'{_n26} para o generalista, e a secao 5 publica 14 e 26')
            else:
                print('  [x] o refino 7 cai no nivel 14 e no 26, que e o gate que a '
                      'secao 5 publica')

# --------------------------------------------------------------------------
bloco('9. LAPIDACAO — a contraparte le os mesmos numeros do refino, ou diverge')
# A Lapidacao (peca 11 SS6.8) e o refino da rota sem energia amaldicoada. Ela NAO
# tem numero proprio: a peca escreve que ela e "a mesma maquina, com outra metrica"
# e que os degraus sao "os mesmos da peca 11 SS5".
#
# Isso e exatamente a licao no 9 esperando acontecer — um numero que mora em dois
# documentos vai divergir, e nao e "se", e "quando". Ate a v0.118 nada comparava
# os dois: mexer na curva do refino deixaria a Lapidacao para tras em silencio.
#
# A checagem NAO guarda valor nenhum. Ela le os dois lados do proprio texto e
# compara. Se a peca parar de escrever a Lapidacao, ela acusa que parou.
SEC68 = ''
_m = re.search(r'^## 6\.8\..*?(?=^## 7\.)', PECA11, re.S | re.M)
if _m:
    SEC68 = _m.group(0)
if not SEC68:
    erro('9: nao achei a secao 6.8 da peca 11 — a Lapidacao perdeu a casa dela, '
         'e esta checagem parou de conferir')
else:
    _lap_teto = re.search(r'tem teto `(\d+)`', SEC68) or re.search(
        r'Lapidação.{0,80}?teto `(\d+)`', SEC68, re.S)
    _lap_ini = re.search(r'Lapidação começa em `(\d+)`', SEC68)
    _lap_passo = re.search(r'sobe `\+(\d+)` de graça em cada marco', SEC68)
    # a peca 9 SS5 tambem publica a escada — e ela e a copia que a mesa le primeiro
    with open(os.path.join(AQUI, '09-origens.md'), encoding='utf-8') as _f:
        PECA09 = _f.read()
    _p9 = re.search(r'A Lapidação começa em `(\d+)`, sobe `\+(\d+)` de graça em cada '
                    r'marco, tem teto `(\d+)`', PECA09)

    achados = {}
    if _lap_ini:   achados['inicio'] = int(_lap_ini.group(1))
    if _lap_passo: achados['passo'] = int(_lap_passo.group(1))
    if _lap_teto:  achados['teto'] = int(_lap_teto.group(1))
    if _p9:
        achados.setdefault('inicio', int(_p9.group(1)))
        achados.setdefault('passo', int(_p9.group(2)))
        achados.setdefault('teto', int(_p9.group(3)))

    # o refino: o inicio e o passo saem da curva das tres rotas, e o teto do topo
    # dela. Nenhum dos tres esta escrito aqui — os tres sao derivados do CURVA.
    ref_ini = 1                      # toda ficha comeca no refino 1 (SS3 desta peca)
    ref_passo = 1                    # a linha de graca do marco sobe +1
    ref_teto = TETO_REFINO
    esperado = {'inicio': ref_ini, 'passo': ref_passo, 'teto': ref_teto}

    faltando = [k for k in esperado if k not in achados]
    if faltando:
        erro(f'9: a peca nao escreve mais {faltando} da Lapidacao — sem isso a '
             'contraparte deixa de ser conferivel contra o refino')
    else:
        print(f"  {'':<12}{'refino':<10}{'Lapidacao':<12}")
        for k in ('inicio', 'passo', 'teto'):
            bate = achados[k] == esperado[k]
            print(f'  {k:<12}{esperado[k]:<10}{achados[k]:<12}{"ok" if bate else "<<< DIVERGIU"}')
            if not bate:
                erro(f'9: a Lapidacao tem {k} = {achados[k]} e o refino tem '
                     f'{esperado[k]} — a peca 11 SS6.8 diz que ela e "a mesma '
                     'maquina, com outra metrica", e ela deixou de ser')

    # os gates: a SS6.8 promete "os mesmos degraus da peca 11 SS5"
    if 'mesmos da peça 11 §5' not in SEC68 and 'mesmos degraus' not in SEC68:
        erro('9: a secao 6.8 parou de dizer que os degraus da Lapidacao sao os '
             'mesmos do refino — se eles se separaram, cada um precisa do proprio '
             'argumento; se nao, a frase e o que segura a copia')
    else:
        # Os gates da Lapidacao NAO moram na 6.8 de proposito: a 6.8 aponta para o
        # SS5 em vez de copiar, e quem escreve os numeros e a peca 9 SS5, que e a
        # copia que a mesa le primeiro. E dela que a checagem le.
        _g = re.search(r'Classe Passiva 2 na Lapidação (\d+), Classe Passiva 3 na (\d+)',
                       PECA09)
        if not _g:
            erro('9: a peca 9 SS5 nao publica mais os degraus da Lapidacao — ela e a '
                 'copia que a mesa le primeiro, e sem ela nada compara os dois lados')
        if _g:
            g2, g3 = int(_g.group(1)), int(_g.group(2))
            # os do refino saem da SS5, lida do texto e nao escrita aqui
            _r = re.search(r'Classe Passiva 2 no refino (\d+)', PECA11)
            _r3 = re.search(r'Classe Passiva 3 no refino (\d+)', PECA11)
            if _r and _r3:
                if (g2, g3) != (int(_r.group(1)), int(_r3.group(1))):
                    erro(f'9: os gates da Lapidacao sao {g2} e {g3} e os do refino sao '
                         f'{_r.group(1)} e {_r3.group(1)} — os dois lados divergiram')
                else:
                    print(f'  gates       {_r.group(1)} e {_r3.group(1)}'
                          f'{"":<4}{g2} e {g3}{"":<7}ok')
        print('  Nenhum destes valores esta escrito dentro deste validador: os do')
        print('  refino sao derivados da CURVA e os da Lapidacao sao lidos do texto.')

# --------------------------------------------------------------------------
bloco('10. O DANO NA ARMA — a excecao da SS2, medida contra as duas condicoes')
# v0.158. O dano na arma entrou no LIVRO na v0.147 e passou onze versoes sem peca,
# sem validador e sem conta — o unico dado do sistema nessa situacao. A SS6.9 da
# peca 11 e o dono dele, e este bloco confere o que ela publica.
#
# Nada de valor de regra mora aqui dentro:
#   o passo e o dado ............. a linha de regra da SS6.9
#   a excecao do teto ............ a mesma linha
#   o teto de refino ............. TETO_REFINO, derivado da CURVA (SS3)
#   o dado do soco por nivel ..... peca 14 SS5.0.6
#   a Forca investida ............ peca 2 SS3 (3 na criacao, 6 no teto)
#   o nivel do ataque extra ...... peca 6 SS3.1
#   a Rotina e o Classe 0 ........ o manual, pelas tabelas importadas no topo
#   o filtro de dominancia ....... lido do texto, e A PARTE da regra aplicada
#
# A separacao do filtro e' de proposito e e' a licao no 8: uma checagem que se
# mede contra a propria constante sai VERDE quando alguem perturba a constante.
# Aqui a razao e RECONSTRUIDA da escada e comparada com a publicada; so depois
# ela e' comparada com o limite de design.
SEC69 = ''
_m69 = re.search(r'^## 6\.9\..*?(?=^## 7\.)', PECA11, re.S | re.M)
if _m69:
    SEC69 = _m69.group(0)

_reg69 = re.search(r'`1d(\d+)` de dano a mais a cada `(\d+)` pontos de refino', SEC69)
# A excecao e' lida como RELACAO: o refino em que ela dispara, as faces novas, e
# se ela acrescenta um dado. Ela nao guarda o `4d6`: o total sai de refino//passo
# mais o acrescimo. Assim o contra-teste coerente — voltar ao `3d6` mexendo em
# tudo que isso implica — sai verde, que e' o que prova que a checagem mede a
# relacao e nao a constante.
_exc69 = re.search(r'No refino `(\d+)` os dados viram `d(\d+)`'
                   r'(?: e entra (um) dado a mais)?', SEC69)

if not SEC69:
    erro('10: nao achei a secao 6.9 da peca 11 — o dano na arma perdeu o dono, e '
         'este bloco parou de conferir em vez de acusar')
elif not _reg69 or not _exc69:
    erro('10: a SS6.9 nao publica mais a regra do dano na arma em linha de regra — '
         'sem ela a escada nao tem de onde ser reconstruida')
else:
    FACE_BASE, PASSO_DANO = int(_reg69.group(1)), int(_reg69.group(2))
    TETO_TXT, FACE_TETO = int(_exc69.group(1)), int(_exc69.group(2))
    EXTRA_TETO = 1 if _exc69.group(3) else 0

    def escada(r):
        """(quantos dados, faces) no refino r — reconstruido da linha de regra."""
        n = r // PASSO_DANO
        if r >= TETO_TXT:
            return n + EXTRA_TETO, FACE_TETO
        return n, FACE_BASE

    def media_dados(n, f):
        return n * (f + 1) / 2.0

    def dano_na_arma(r):
        return media_dados(*escada(r))

    if TETO_TXT != TETO_REFINO:
        erro(f'10: a excecao da SS6.9 fala do refino {TETO_TXT} e o teto do refino e '
             f'{TETO_REFINO}, derivado da curva da SS3 — ou ela aponta para um refino '
             'que ninguem alcanca, ou o teto mudou e ela ficou para tras')

    # ---- a escada publicada, lida da tabela da SS6.9
    PUB = {}
    for _l in SEC69.splitlines():
        _mt = re.match(r'\|\s*\*{0,2}`(\d+)`\*{0,2}(?:\s*·\s*\*{0,2}`(\d+)`\*{0,2})?\s*\|'
                       r'\s*(?:—|\*{0,2}`(\d+)d(\d+)`\*{0,2})\s*\|'
                       r'\s*\*{0,2}`([\d,]+)`\*{0,2}\s*\|', _l)
        if not _mt:
            continue
        _v = float(_mt.group(5).replace(',', '.'))
        _n = int(_mt.group(3)) if _mt.group(3) else 0
        _f = int(_mt.group(4)) if _mt.group(4) else 0
        for _r in [int(_mt.group(1))] + ([int(_mt.group(2))] if _mt.group(2) else []):
            PUB[_r] = (_n, _f, _v)

    # guarda de reconhecedor: sem ela, renomear a tabela faz a checagem achar zero
    # linha, logo zero divergencia, e ela passa verde para sempre sem ter conferido
    # nada. E' a licao no 8 aplicada ao reconhecedor em vez de ao valor.
    if sorted(PUB) != list(range(1, TETO_REFINO + 1)):
        erro(f'10: a escada da SS6.9 cobre {sorted(PUB)} e o refino vai de 1 a '
             f'{TETO_REFINO} — a tabela mudou de forma, e a comparacao abaixo passaria '
             'verde sem conferir nada')
    else:
        print(f"  {'refino':<9}{'a peca publica':<18}{'a regra reconstroi':<22}")
        _mau = 0
        for _r in range(1, TETO_REFINO + 1):
            _n, _f, _v = PUB[_r]
            _en, _ef = escada(_r)
            _ev = media_dados(_en, _ef)
            _rot = f'{_en}d{_ef}' if _en else '—'
            _bate = (_n, _f) == ((_en, _ef) if _en else (0, 0)) and abs(_v - _ev) <= 0.01
            print(f'  {_r:<9}{(f"{_n}d{_f}" if _n else "—") + " = " + f"{_v:.1f}":<18}'
                  f'{_rot + " = " + f"{_ev:.1f}":<22}{"ok" if _bate else "<<< DIVERGIU"}')
            if not _bate:
                _mau += 1
        if _mau:
            erro(f'10: {_mau} degrau(s) da escada da SS6.9 nao reconstroem da propria '
                 f'linha de regra — `1d{FACE_BASE}` a cada {PASSO_DANO}, com o refino '
                 f'{TETO_TXT} virando d{FACE_TETO} com um dado a mais')
        else:
            print('  [x] os dez degraus reconstroem da linha de regra, e nenhum deles')
            print('      esta escrito dentro deste validador.')

    # ---- o golpe simples, dos donos
    with open(os.path.join(AQUI, '14-equipamento.md'), encoding='utf-8') as _f14:
        PECA14 = _f14.read()
    SOCO = []
    for _l in PECA14.splitlines():
        _ms = re.match(r'>?\s*\|\s*(\d)\s*\|\s*(\d+) a (\d+)\s*\|\s*\*\*d(\d+)\*\*\s*\|', _l)
        if _ms:
            SOCO.append((int(_ms.group(2)), int(_ms.group(3)), int(_ms.group(4))))
    with open(os.path.join(AQUI, '02-economia-de-atributos.md'), encoding='utf-8') as _f02:
        PECA02 = _f02.read()
    _matr = re.search(r'Atributo investido: \*\*(\d+) na criação, (\d+) no teto', PECA02)
    with open(os.path.join(AQUI, '06-caminhos-e-trilhas.md'), encoding='utf-8') as _f06:
        PECA06 = _f06.read()
    _mex = re.search(r'ganham ataque extra no nível (\d+)', PECA06)

    if len(SOCO) != 4 or not _matr or not _mex:
        erro('10: nao consegui ler o golpe simples dos donos — a escada do soco da '
             f'peca 14 SS5.0.6 devolveu {len(SOCO)} faixa(s), a Forca da peca 2 SS3 '
             f'{"veio" if _matr else "NAO veio"} e o nivel do ataque extra da peca 6 '
             f'SS3.1 {"veio" if _mex else "NAO veio"}')
    else:
        ATR_INI, ATR_TETO = int(_matr.group(1)), int(_matr.group(2))
        NV_EXTRA = int(_mex.group(1))

        def faixa_do_soco(nv):
            for _i, (_a, _b, _d) in enumerate(SOCO):
                if _a <= nv <= _b:
                    return _i, _d
            return None, None

        def golpe_simples(nv):
            """dado do soco (peca 14) + Forca investida (peca 2).

            A Forca sobe um por faixa do soco: as faixas da peca 14 SAO o ritmo da
            maestria, entao o `8` nao precisa estar escrito aqui.
            """
            _i, _d = faixa_do_soco(nv)
            return (_d + 1) / 2.0 + min(ATR_TETO, ATR_INI + _i)

        def classe_do_nivel(nv):
            _c = 1
            for _k in sorted(CLASSE_NO_NIVEL):
                if nv >= _k:
                    _c = CLASSE_NO_NIVEL[_k]
            return _c

        # ---- condicao 2 da SS2: a rodada em que o dano na arma cai fica ABAIXO da
        # Rotina do nivel. Medida nos 29 niveis, na rota que mais recebe.
        _pior_nv, _pior = None, -1.0
        _no30 = None
        for _nv in range(2, 31):
            _r = refino_em('especialista', _nv)
            _atk = (2 if _nv >= NV_EXTRA else 1) * (golpe_simples(_nv) + dano_na_arma(_r))
            _frac = 100.0 * _atk / ROTINA[classe_do_nivel(_nv)]
            if _frac > _pior:
                _pior_nv, _pior = _nv, _frac
            if _nv == 30:
                _no30 = _frac
        print(f'\n  A Acao de Atacar com o dano na arma inteiro, contra a Rotina:')
        print(f'  pior nivel {_pior_nv} com {_pior:.1f}% · nivel 30 com {_no30:.1f}%')
        if _pior >= 100.0:
            erro(f'10: no nivel {_pior_nv} a Acao de Atacar com o dano na arma chega a '
                 f'{_pior:.1f}% da Rotina — a segunda condicao da SS2 exige que ela '
                 'fique ABAIXO da regua, e o dano de refino deixou de caber')
        _mp = re.search(r'O pior nível é o `(\d+)`, com a Ação de Atacar em '
                        r'`([\d,]+)%` da Rotina', SEC69)
        _m30 = re.search(r'No nível 30 ela fica em `([\d,]+)%`', SEC69)
        if not _mp or not _m30:
            erro('10: a SS6.9 nao publica mais o pior nivel e a fracao dele — o '
                 'invariante da SS2 virou afirmacao sem numero ao lado')
        else:
            _pnv = int(_mp.group(1))
            _pfr = float(_mp.group(2).replace(',', '.'))
            _f30 = float(_m30.group(1).replace(',', '.'))
            if _pnv != _pior_nv or abs(_pfr - _pior) > 0.1 or abs(_f30 - _no30) > 0.1:
                erro(f'10: a SS6.9 publica o pior nivel em {_pnv} com {_pfr:.1f}% e o '
                     f'nivel 30 com {_f30:.1f}%, e a conta reconstroi nivel {_pior_nv} '
                     f'com {_pior:.1f}% e {_no30:.1f}%')
            else:
                print('  [x] o pior nivel e a fracao publicados reconstroem dos donos.')

        # ---- a dominancia dentro do Caminho, no nivel 30. A REGRA APLICADA e a
        # razao reconstruida; o LIMITE DE DESIGN e o filtro, lido a parte.
        _r_pior = refino_em('generalista', 30)
        _pior30 = 2 * (golpe_simples(30) + dano_na_arma(_r_pior))
        _melhor30 = 2 * (golpe_simples(30) + dano_na_arma(TETO_REFINO))
        _razao = _melhor30 / _pior30
        _md = re.search(r'\|\s*\*{0,2}com o `4d6`\*{0,2}\s*\|\s*`([\d,]+)`\s*\|'
                        r'\s*`([\d,]+)`\s*\|\s*\*{0,2}`([\d,]+)×`\*{0,2}\s*\|', SEC69)
        _mf = re.search(r'filtro do projeto reprova a partir de `([\d,]+)×`', SEC69)
        print(f'\n  Nivel 30: pior rota {_pior30:.2f} · melhor rota {_melhor30:.2f} · '
              f'razao {_razao:.2f}x')
        if not _md or not _mf:
            erro('10: a SS6.9 nao publica mais a linha da dominancia no nivel 30 ou o '
                 'filtro — sem os dois nada compara a razao com o limite de design')
        else:
            _p_pior = float(_md.group(1).replace(',', '.'))
            _p_melhor = float(_md.group(2).replace(',', '.'))
            _p_razao = float(_md.group(3).replace(',', '.'))
            _filtro = float(_mf.group(1).replace(',', '.'))
            if (abs(_p_pior - _pior30) > 0.01 or abs(_p_melhor - _melhor30) > 0.01
                    or abs(_p_razao - _razao) > 0.01):
                erro(f'10: a SS6.9 publica {_p_pior:.2f} / {_p_melhor:.2f} / '
                     f'{_p_razao:.2f}x no nivel 30, e a conta reconstroi '
                     f'{_pior30:.2f} / {_melhor30:.2f} / {_razao:.2f}x')
            elif _razao >= _filtro:
                erro(f'10: a razao entre a pior e a melhor rota no nivel 30 e '
                     f'{_razao:.2f}x, e o filtro declarado reprova a partir de '
                     f'{_filtro:.2f}x')
            else:
                print(f'  [x] a razao reconstroi, e ela cabe no filtro de {_filtro:.2f}x')

    # ---- a excecao declarada na SS2, e ela e' o que autoriza tudo acima
    SEC2 = ''
    _m2 = re.search(r'^## 2\. A trava.*?(?=^## 3\.)', PECA11, re.S | re.M)
    if _m2:
        SEC2 = _m2.group(0)
    _lista = re.search(r'Isso elimina de saída \*\*([^*]+)\*\*', SEC2)
    _cond = [_l for _l in SEC2.splitlines()
             if _l.lstrip().startswith('>') and 'PICO da rodada' in _l]
    _cond2 = [_l for _l in SEC2.splitlines()
              if _l.lstrip().startswith('>') and 'abaixo da Rotina do nível' in _l]
    if not SEC2 or not _lista:
        erro('10: nao achei a lista da trava na SS2 — sem ela nada diz o que o refino '
             'nao pode escalar, e a excecao do dano fica sem contra o que ser excecao')
    elif 'dano' in sem_acento(_lista.group(1)).lower():
        erro('10: a lista da trava da SS2 voltou a nomear `dano` junto dos quatro que '
             'tem rolagem disputada — a justificativa dela ("o outro lado cresce +3") '
             'nao alcanca dano, e a SS2 declara a excecao com o motivo desde a v0.158')
    elif not _cond or not _cond2:
        erro('10: a SS2 parou de escrever as DUAS condicoes da excecao de dano em '
             'linha de regra — sem elas a excecao vira permissao aberta')
    elif '§6.9' not in SEC2:
        erro('10: a SS2 declara a excecao de dano e nao aponta para a SS6.9, que e '
             'quem mede as duas condicoes')
    else:
        print('\n  [x] a SS2 tira `dano` da lista dos quatro, escreve as duas condicoes')
        print('      em linha de regra, e aponta para a SS6.9.')

    # ---- o incentivo: o degrau do teto e o unico que a linha de graca nao alcanca
    _sc = PECA11[PECA11.find('### A curva das três rotas, marco a marco'):]
    _sc = _sc[:_sc.find('\n### ')] if '\n### ' in _sc else _sc
    _pubc = {}
    for _l in _sc.split('\n'):
        _mc = re.match(r'^\|\s*\*\*(\w[\w ]*?)\*\*[^|]*\|(.+)\|\s*$', _l)
        if _mc:
            _vs = re.findall(r'`?(\d+)`?', _mc.group(2))
            if len(_vs) == len(MARCOS):
                _pubc[_mc.group(1).strip().lower()] = [int(x) for x in _vs]
    _alcanca = {}
    for _rota, _vals in _pubc.items():
        _nv = None
        for _i, _m in enumerate(MARCOS):
            if _vals[_i] >= TETO_REFINO:
                _nv = _m
                break
        _alcanca[_rota] = _nv
    if len(_pubc) != 3:
        erro(f'10: li {len(_pubc)} rota(s) na curva da SS3 e esperava 3 — sem ela nada '
             'diz quem alcanca o teto do refino, e o argumento do incentivo fica sem '
             'chao')
        _alcanca = {'generalista': None, 'especialista': -1, 'meio a meio': -1}
    _me = re.search(r'\*\*especialista\*\* — sempre Refino \|[^|]*\|\s*\*\*nível (\d+)\*\*', SEC69)
    _mm = re.search(r'\*\*meio a meio\*\* \|[^|]*\|\s*nível (\d+)', SEC69)
    _mg = re.search(r'\*\*generalista\*\* — nunca Refino \|[^|]*\|\s*\*\*nunca\*\*', SEC69)
    if not _me or not _mm or not _mg:
        erro('10: a SS6.9 parou de publicar em que nivel cada rota alcanca o teto do '
             'refino — e e nisso que o argumento do incentivo se apoia')
    elif _alcanca['generalista'] is not None:
        erro(f'10: a rota que nunca escolhe Refino passou a alcancar o teto no nivel '
             f'{_alcanca["generalista"]} — o degrau do teto deixou de ser exclusivo de '
             'quem escolhe, e o argumento de incentivo da SS6.9 cai junto')
    elif (int(_me.group(1)) != _alcanca['especialista']
          or int(_mm.group(1)) != _alcanca['meio a meio']):
        erro(f'10: a SS6.9 publica o teto chegando no nivel {_me.group(1)} para o '
             f'especialista e {_mm.group(1)} para o meio a meio, e a curva da SS3 da '
             f'{_alcanca["especialista"]} e {_alcanca["meio a meio"]}')
    else:
        print(f'  [x] o teto do refino chega no nivel {_alcanca["especialista"]} '
              f'(especialista) e {_alcanca["meio a meio"]} (meio a meio), e a rota que')
        print('      nunca escolhe Refino nao alcanca ele — o degrau e do eixo, nao da graca.')

    # ---- as duas copias no LIVRO. Copia sem comparacao diverge (licao no 9), e foi
    # exatamente isso que deixou o dano na arma onze versoes so no capitulo.
    _LIV = os.path.join(AQUI, '..', '05-material', 'livro', 'manual')
    _NT, _FT = escada(TETO_REFINO)
    for _arq, _metrica in (('45-aptidoes-e-refino.md', 'refino'),
                           ('47-bencaos-e-lapidacao.md', 'Lapidação')):
        _cam = os.path.join(_LIV, _arq)
        if not os.path.exists(_cam):
            aviso(f'10: nao achei {_arq} — a copia do livro nao foi conferida')
            continue
        _txt = open(_cam, encoding='utf-8').read()
        _ok_regra = re.search(rf'`1d{FACE_BASE}` de dano a mais a cada `{PASSO_DANO}` '
                              rf'pontos de {_metrica}', _txt)
        _ok_teto = re.search(rf'(?:refino|Lapidação) `{TETO_TXT}`[^\n]*`d{FACE_TETO}`'
                             rf'[^\n]*`{_NT}d{_FT}`', _txt)
        if not _ok_regra or not _ok_teto:
            erro(f'10: o livro, em {_arq}, nao publica o dano na arma como a SS6.9 '
                 f'escreve — `1d{FACE_BASE}` a cada `{PASSO_DANO}` de {_metrica}, e no '
                 f'`{TETO_TXT}` virando `{_NT}d{_FT}`')
        else:
            print(f'  [x] {_arq} publica a mesma escada que a SS6.9')

# --------------------------------------------------------------------------
bloco('11. AS CONTAGENS DE APTIDAO — a rota pura publica o que a regra produz')
# --------------------------------------------------------------------------
# A v0.89 trocou a MOEDA da escolha de Refino quando o refino ja esta no teto:
# ela passa a levar DUAS aptidoes em vez de uma. A regra mora na peca 11 §3 e os
# dois numeros dela sao LIDOS de la — nada de valor fica escrito aqui.
#
# O que faltava era comparacao. A curva de REFINO ja era reconstruida da regra
# (checagem 6), mas a contagem de APTIDAO nao era conferida em lugar nenhum, e o
# `7` de antes da v0.89 sobreviveu da v0.89 a v0.160 em quatro documentos — dois
# deles a poucas linhas da tabela que ja publicava o numero certo.
_A11 = os.path.join(AQUI, '11-aptidoes-e-refino.md')
_A02 = os.path.join(AQUI, '02-economia-de-atributos.md')
_AEST = os.path.join(AQUI, '..', 'ESTADO-ATUAL.md')
_ALIV = os.path.join(AQUI, '..', '05-material', 'livro', 'manual',
                     '45-aptidoes-e-refino.md')
_T11 = open(_A11, encoding='utf-8').read()
_T02 = open(_A02, encoding='utf-8').read()
_TEST = open(_AEST, encoding='utf-8').read()
_TLIV = open(_ALIV, encoding='utf-8').read() if os.path.exists(_ALIV) else ''

_NUM = {'zero': 0, 'uma': 1, 'duas': 2, 'três': 3, 'quatro': 4, 'cinco': 5,
        'seis': 6, 'sete': 7, 'oito': 8, 'nove': 9, 'dez': 10}


def _n(txt):
    """aceita algarismo ou numeral por extenso, que e como as pecas escrevem."""
    return int(txt) if txt.isdigit() else _NUM.get(txt.lower())


# ---- os dois valores da regra, lidos da peca 11 §3
_m_base = re.search(r'\*\*Refino\*\* — mais um de refino, e uma aptidão', _T11)
# o valor do teto ja foi lido da peca 11 la na checagem 5 (APT_NO_TETO). Ler de
# novo aqui criaria um segundo leitor do mesmo numero, que e a licao no 9 na
# forma de codigo.
_m_teto = APT_NO_TETO
if not _m_base or _m_teto is None:
    erro('11: nao achei a linha de regra da escolha de Refino na peca 11 §3 — a '
         'base ("mais um de refino, e uma aptidão") e a troca de moeda no teto '
         '("você leva `N` aptidões no lugar") sao de onde esta checagem tira os '
         'dois numeros, e sem elas ela conferiria contra valor escrito aqui')
else:
    APT_BASE, APT_TETO = 1, APT_NO_TETO

    def _sim(escolhas):
        """os sete marcos, na regra: passivo +1 de refino, e a escolha em cima.

        Devolve a curva de refino e as aptidoes acumuladas, marco a marco.
        """
        r, apt, cur, ac = 1, 0, [], []
        for e in escolhas:
            r = min(TETO_REFINO, r + 1)          # a linha de graca do marco
            if e:
                if r >= TETO_REFINO:
                    apt += APT_TETO              # a moeda trocada, v0.89
                else:
                    r += 1
                    apt += APT_BASE
            cur.append(r)
            ac.append(apt)
        return cur, ac

    # contra-prova de que este simulador e a MESMA regra da checagem 6: as duas
    # rotas puras tem de devolver a curva que o _curva() daquela reconstroi.
    _cur_esp, _apt_esp = _sim([True] * len(MARCOS))
    _cur_gen, _apt_gen = _sim([False] * len(MARCOS))
    if _cur_esp != _curva(True) or _cur_gen != _curva(False):
        erro(f'11: o simulador deste bloco devolve {_cur_esp} e {_cur_gen} para as '
             f'rotas puras, e o da checagem 6 devolve {_curva(True)} e '
             f'{_curva(False)} — as duas leem a mesma regra e discordam')
    else:
        PURA = _apt_esp[-1]
        print(f'  a regra: +{APT_BASE} aptidao por escolha de Refino, e +{APT_TETO} '
              f'quando o refino ja esta no teto')
        print(f'  aptidoes da rota pura, marco a marco: {_apt_esp}')
        print(f'  a rota que nunca escolhe Refino: {_apt_gen[-1]}')

        # ---- todo lugar que publica a contagem da rota pura.
        # Cada entrada e' (rotulo, texto, regex). O grupo 1 e' o numero.
        _PUBS = [
            ('peca 11 §3, a tabela das tres rotas puras', _T11,
             r'\|\s*sempre Refino\s*\|\s*\*{0,2}\d+\*{0,2}\s*\|'
             r'\s*\*{0,2}\d+\*{0,2}\s*\|\s*\*{0,2}(\d+)\*{0,2}\s*\|'),
            ('peca 11, o cardapio contra a rota pura', _T11,
             r'A rota pura passa a precisar de (\d+) aptidões'),
            ('peca 11, o argumento das tres nao se substituirem', _T11,
             r'Quem escolhe refino tem (\w+) aptidões'),
            ('peca 11, a troca escrita na cara do jogador', _T11,
             r'e (\w+) aptidões contra nenhuma'),
            ('peca 11, o preco da Vantagem no d100', _T11,
             r'numa campanha com no máximo (\w+) aptidões'),
            ('peca 2 §3, a tabela das tres fichas', _T02,
             r'\*\*sempre refino\*\*.*?\*{0,2}(\d+) apt\*{0,2}\s*\|\s*$'),
            ('peca 2 §3, a leitura embaixo da tabela', _T02,
             r'refino no teto e (\w+) aptidões'),
            ('o ESTADO-ATUAL, a tabela das quatro rotas', _TEST,
             r'\|\s*sempre refino\s*\|\s*\*{0,2}\d+\*{0,2}\s*\|'
             r'\s*\*{0,2}\d+\*{0,2}\s*\|\s*\*{0,2}(\d+)\*{0,2}\s*\|'),
        ]
        # O LIVRO saiu desta lista na v0.176. A frase que publicava a contagem
        # ali -- "troca dez aptidoes por sete pontos de atributo" -- foi cortada
        # na revisao do .docx, junto com as outras tabelas e frases que so
        # repetiam resultado. O livro deixou de ser publicacao desta conta de
        # proposito; as outras oito continuam sendo comparadas entre si.
        _cegos = [r for r, t, x in _PUBS if not re.search(x, t, re.M | re.S)]
        # guarda de reconhecedor: sem ela, uma frase reescrita faz a checagem
        # achar zero publicacao, logo zero divergencia, e ela passa verde para
        # sempre sem ter conferido nada. E' a licao no 8 no reconhecedor.
        if _cegos:
            erro(f'11: {len(_cegos)} publicacao(oes) da contagem da rota pura '
                 f'sumiram do reconhecedor: {"; ".join(_cegos)} — ou o texto mudou '
                 'de forma, ou o numero deixou de ser publicado ali, e nos dois '
                 'casos esta checagem parou de conferir aquele lugar')
        else:
            _mau = []
            print(f'\n  {"onde":<48}{"publica":<10}{"a regra"}')
            for _rot, _txt, _rx in _PUBS:
                _v = _n(re.search(_rx, _txt, re.M | re.S).group(1))
                _ok = _v == PURA
                print(f'  {_rot:<48}{str(_v):<10}{PURA}  {"ok" if _ok else "<<< DIVERGIU"}')
                if not _ok:
                    _mau.append(f'{_rot} diz {_v}')
            if _mau:
                erro(f'11: a rota pura leva {PURA} aptidoes pela regra da peca 11 §3, '
                     f'e {len(_mau)} lugar(es) publicam outro numero: '
                     + '; '.join(_mau))
            else:
                print(f'  [x] as {len(_PUBS)} publicacoes dizem {PURA}, e o numero nao')
                print('      esta escrito dentro deste validador.')

        # ---- a linha `meio a meio` do ESTADO-ATUAL: ela e' a unica que nao esta
        # na peca 11, e ate a v0.160 ela descrevia uma rota DIFERENTE com o mesmo
        # nome — 2 escolhas de Refino contra as 3 da curva da peca. O chefe herda
        # essa curva (o conferir-atributos.py deriva a Defesa do alvo dificil
        # dela), entao duas leituras do mesmo nome sao divergencia esperando data.
        _mmc = re.search(r'\|\s*\*\*meio a meio\*\*\s*\|((?:[^|]*\|){' +
                         str(len(MARCOS)) + r'})', _T11)
        _mme = re.search(r'\|\s*meio a meio\s*\|\s*\*{0,2}(\d+)\*{0,2}\s*\|'
                         r'\s*\*{0,2}(\d+)\*{0,2}\s*\|\s*\*{0,2}(\d+)\*{0,2}\s*\|'
                         r'\s*\*{0,2}(\d+)\*{0,2}\s*\|\s*\*{0,2}(\d+)\*{0,2}\s*\|',
                         _TEST)
        if not _mmc or not _mme:
            erro('11: nao achei a curva do "meio a meio" na peca 11 §3 ou a linha '
                 'dele na tabela do ESTADO-ATUAL — sem as duas nao da para provar '
                 'que o nome descreve uma rota so')
        else:
            _curva_mm = [int(x) for x in re.findall(r'`?(\d+)`?', _mmc.group(1))]
            _atr, _ref, _apt, _pas, _fei = (int(_mme.group(i)) for i in range(1, 6))
            # o orcamento de escolhas: o passivo da +1 atributo em cada marco, e o
            # que sobra no atributo foi comprado. Passiva paga e' o teto de sempre.
            _n_corpo = _atr - len(MARCOS)
            _n_leque = _fei
            _n_refino = len(MARCOS) - _n_corpo - _n_leque
            _cands = [c for c in itertools.combinations(range(len(MARCOS)), _n_refino)
                      if _sim([i in c for i in range(len(MARCOS))])[0] == _curva_mm] \
                if 0 <= _n_refino <= len(MARCOS) else []
            _apts = {_sim([i in c for i in range(len(MARCOS))])[1][-1] for c in _cands}
            print(f'\n  meio a meio: {_n_corpo} Corpo · {_n_refino} Refino · '
                  f'{_n_leque} Leque = {_n_corpo + _n_refino + _n_leque} escolhas, '
                  f'de {len(MARCOS)} marcos')
            if _n_corpo < 0 or _n_leque < 0 or _n_refino < 0:
                erro(f'11: a linha "meio a meio" do ESTADO-ATUAL pede {_n_corpo} '
                     f'Corpo, {_n_refino} Refino e {_n_leque} Leque, e escolha '
                     'negativa nao existe')
            elif not _cands:
                erro(f'11: nenhuma colocacao de {_n_refino} escolha(s) de Refino nos '
                     f'{len(MARCOS)} marcos reproduz a curva {_curva_mm} que a peca 11 '
                     f'§3 publica para o "meio a meio" — a tabela do ESTADO-ATUAL '
                     'descreve uma rota DIFERENTE com o mesmo nome')
            elif len(_apts) != 1:
                erro(f'11: as colocacoes que reproduzem a curva do "meio a meio" dao '
                     f'{sorted(_apts)} aptidoes, entao a contagem nao e derivavel da '
                     'curva e a linha precisa dizer qual delas e')
            elif _apt != _apts.pop():
                _e = _sim([i in _cands[0] for i in range(len(MARCOS))])[1][-1]
                erro(f'11: o "meio a meio" do ESTADO-ATUAL publica {_apt} aptidoes e '
                     f'a curva da peca 11 §3 ({_curva_mm}) produz {_e}')
            elif _ref != _curva_mm[-1]:
                erro(f'11: o "meio a meio" do ESTADO-ATUAL publica refino {_ref} no '
                     f'nivel 30 e a curva da peca 11 §3 termina em {_curva_mm[-1]}')
            elif tuple(i for i, v in enumerate(ROTAS['meio a meio'])
                       if v == 1) not in _cands:
                # a TERCEIRA copia do mesmo nome, e ela mora neste arquivo: a
                # colocacao da tabela ROTAS. Ela so aparece na saida da checagem
                # 5, e display que mente ensina numero errado igual a checagem
                # que mente.
                erro(f'11: a colocacao do "meio a meio" na tabela ROTAS deste '
                     f'validador ({ROTAS["meio a meio"]}) nao reproduz a curva '
                     f'{_curva_mm} que a peca 11 §3 publica — a checagem 5 estaria '
                     'imprimindo os totais de uma rota diferente com o mesmo nome')
            else:
                print(f'  [x] a curva {_curva_mm} da peca 11 e a linha do ESTADO-ATUAL '
                      f'({_apt} aptidoes,')
                print('      refino ' + str(_ref) + ') sao a MESMA rota — um nome, uma leitura.')

# ==========================================================================
# 12. O TETO DO QUE A `Extensao de Dominio` ANULA — v0.165
#
# A linha era "anula qualquer tecnica que encostar nela", sem teto. Decisao do
# Mizuki, levantada por um colega dele: ela passa a anular Classe Passiva, Regra
# Propria e feitico de Classe ate `1/3 do refino + 1` — "mas nao tudo".
#
# NENHUM VALOR MORA AQUI. A formula sai da secao da propria aptidao, o gate sai
# do titulo dela, o teto de refino e o mesmo que a peca 2 fixa, e a maior Classe
# sai da tabela importada do manual. O que se confere e a RELACAO que a frase
# "mas nao tudo" afirma: o teto nunca alcanca a maior Classe.
#
# E ela confere os dois lados: se o teto passar a alcancar tudo, o "mas nao
# tudo" virou mentira; se ele parar de crescer com refino, a aptidao deixou de
# usar a metrica das aptidoes, que e o que a §2 desta peca proibe.
print()
print('=' * 90)
print('12. O TETO DO QUE A `Extensao de Dominio` ANULA')
print('=' * 90)

_sec_ext = ''
if '### Extensão de Domínio' in _t11:
    _sec_ext = _t11.split('### Extensão de Domínio')[1].split('\n### ')[0]

# A formula sai da LINHA DE REGRA e nao da secao: a secao tem prosa que cita a
# mesma formula para explicar de onde ela vem, e ler a secao inteira faz apagar
# a REGRA sair verde por causa do COMENTARIO. Achado no arnes, e e a mesma
# familia do recorte de linha de regra que a v0.151 consertou no conferir-atributos.
_m_regra = re.search(r'^>\s*\*\*E o que encostar nela .*$', _sec_ext, re.M)
_linha_regra = _m_regra.group(0) if _m_regra else ''
_m_cap = re.search(r'`1/(\d+)\s+do refino\s*\+\s*(\d+)`', _linha_regra)
_m_gate = re.search(r'refino\s+(\d+)\s+e n[ií]vel\s+\d+', _sec_ext)

if not _sec_ext:
    erro('nao achei a secao da `Extensao de Dominio` na peca 11 — a checagem 12 '
         'passaria a conferir o vazio em vez de acusar')
elif not _m_cap:
    erro('a `Extensao de Dominio` nao declara mais o teto do que ela anula — sem '
         'ele a linha volta a ser "anula qualquer coisa", que foi o que a v0.165 '
         'saiu para tirar')
elif not _m_gate:
    erro('nao consegui ler o gate de refino da `Extensao de Dominio` no titulo dela')
else:
    _div, _mais = int(_m_cap.group(1)), int(_m_cap.group(2))
    _gate = int(_m_gate.group(1))
    _cap = lambda r: r // _div + _mais
    _maior_classe = max(CLASSE_NO_NIVEL.values())
    print(f'  teto declarado: 1/{_div} do refino + {_mais}')
    print(f'  no gate (refino {_gate}) ele para em {_cap(_gate)}; '
          f'no teto de refino ({TETO_REFINO}) ele chega em {_cap(TETO_REFINO)}')
    print(f'  a maior Classe do sistema e {_maior_classe}')

    # 12.1 — o "mas nao tudo": o teto NUNCA alcanca a maior Classe
    if _cap(TETO_REFINO) >= _maior_classe:
        erro(f'no refino {TETO_REFINO} a `Extensao de Dominio` anula ate Classe '
             f'{_cap(TETO_REFINO)}, e a maior Classe e {_maior_classe} — o teto '
             'alcancou tudo, e a linha voltou a ser "anula qualquer coisa" com '
             'uma formula na frente')
    else:
        print(f'  [x] 12.1 o teto para em {_cap(TETO_REFINO)} de {_maior_classe}: '
              'ha Classe que passa por ela em todo refino.')

    # 12.2 — ela tem de CRESCER com refino, senao nao e metrica de aptidao (§2)
    if _cap(TETO_REFINO) <= _cap(_gate):
        erro(f'o teto da `Extensao de Dominio` vale {_cap(_gate)} no gate e '
             f'{_cap(TETO_REFINO)} no teto de refino — ele nao cresce, e a §2 '
             'desta peca diz que o refino e a metrica das aptidoes')
    else:
        print(f'  [x] 12.2 o teto cresce de {_cap(_gate)} para {_cap(TETO_REFINO)} '
              'com o refino, que e a metrica das aptidoes.')

    # 12.3 — GUARDA: sem ela, apagar a frase do "mas nao tudo" sairia verde.
    # A afirmacao e do texto, e a checagem cobra que ela continue escrita.
    # A afirmacao mora na PROSA da §6.5 e nao numa celula: marca dentro da celula
    # quebra o extrator de gate do conferir-ferramenta.py, medido no arnes.
    if not re.search('n[ãa]o [ÉE] uma anti-dom[íi]nio', _t11):
        erro('a `Extensao de Dominio` voltou a ser contada como anti-dominio na '
             'peca 11 — ela serve como uma e nao e uma, e a §6.5 tem de dizer isso')
    elif not re.search('nunca alcan.a a maior Classe', _t11, re.I):
        erro('a peca 11 nao escreve mais o invariante do teto — a checagem 12 '
             'conferiria um numero que o documento nao afirma mais')
    else:
        print('  [x] 12.3 a peca declara o invariante e diz que ela nao e da categoria.')

# --------------------------------------------------------------------------
print()
print('=' * 90)
if ERROS:
    print(f'>>> {len(ERROS)} PROBLEMA(S):')
    for e in ERROS:
        print('   -', e)
    sys.exit(1)
print('>>> TUDO OK — o refino nao deriva onde nao pode, as tres rotas do marco nao se')
print('    dominam, e o orcamento de espaco cobre a montagem mais pesada.')
if AVISOS:
    print(f'    {len(AVISOS)} aviso(s) acima, que nao falham o validador.')

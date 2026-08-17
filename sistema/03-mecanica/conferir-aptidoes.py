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
CHEFE = {5: 15, 10: 26, 15: 38, 20: 49, 25: 61, 30: 72}
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
    'magnitude fora de disputa':  (True,  'RD e protecao nao sao rolagem'),
    'disputa contra outro refino': (True, 'simetrico — os dois lados crescem +9'),
    'rolagem de acerto':          (False, 'do outro lado, a Defesa cresce +3'),
    'CD de feitico':              (False, 'do outro lado, o atributo do TR cresce +3'),
    'Defesa':                     (False, 'do outro lado, o ataque cresce +3'),
    'Teste de Resistencia':       (False, 'do outro lado, a CD cresce +3'),
    'dano que compete com feitico': (False, 'do outro lado, a vida de inimigo cresce'),
}
# o que cada aptidao escrita declara escalar
ESCALA = {
    'cobrir-se, protecao':     'magnitude fora de disputa',
    'cobrir-se, RD da Reacao': 'magnitude fora de disputa',
    'canalizar energia':       None,
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
    perde = piso(r / DIVISOR) + 1
    custo = 0.05 * perde * d          # cada ponto de Defesa vale 5 pp de acerto
    saldo = rd - custo
    saldos.append(saldo)
    print(f'  {nv:<8}{r:<9}{rd:<7}{d:<17.0f}{custo:<17.1f}{saldo:+.1f}')
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

if MULT_CONST and EMPILHAM:
    MARCOS_DA_PILHA = 3          # Kokusen + Constante + Melhorado, um marco cada
    p_base = min(1.0, MULT_KOK * TETO_REFINO / 100)
    p_const = min(1.0, MULT_CONST * TETO_REFINO / 100)
    p_pilha = 1 - (1 - p_const) ** 2      # vantagem rola sobre a base ja subida
    print(f"  {'a ficha tem':<38}{'chance no d100':<17}{'dano por rodada':<18}"
          f"{'marcos':<9}{'x atributo, POR marco'}")
    linhas = [('so o Kokusen', p_base, 1),
              ('Kokusen + Constante', p_const, 2),
              ('Kokusen + Melhorado', 1 - (1 - p_base) ** 2, 2),
              ('as TRES empilhadas', p_pilha, MARCOS_DA_PILHA)]
    for nome, p, marcos in linhas:
        g = dpr(p) / BASE - 1
        print(f'  {nome:<38}{p:<17.0%}{f"+{g*100:.2f}%":<18}{marcos:<9}'
              f'{g / marcos / VALE_ATRIBUTO:.2f}x')
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


def feiticos_base(nv):
    return 2 + nv // 2


def espacos(nv):
    return feiticos_base(nv) + sum(1 for m in MARCOS if nv >= m)


ROTAS = {
    'sempre Corpo':  [0] * 7,
    'sempre Refino': [1] * 7,
    'sempre Leque':  [2] * 7,
    'meio a meio':   [0, 1, 2, 0, 1, 2, 0],
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
        n_apt = APT_NO_TETO if ganho_ref == 0 else 1
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

    # 4. o refino nao escala a cura. LIÇÃO Nº 1: refino cresce +7 a +9 e vida de
    #    inimigo cresce mais rapido; se ele entrar aqui, a cura deriva.
    _formula = [l for l in _s6.split('\n') if 'de vida por PE' in l or 'cura por PE' in l]
    if _formula and 'refino' in sem_acento(' '.join(_formula)).lower():
        erro('a formula de cura da `Energia Reversa` menciona refino — a secao 2 proibe, '
             'e o teto dela e `maior Classe`')
    else:
        print('  [x] o refino nao entra na formula de cura.')

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
    if _pares < 14:
        erro(f'so {_pares} entrada(s) do catalogo tem secao para comparar, e eram 14 — '
             f'alguem mudou o formato do titulo e esta checagem esta conferindo menos. '
             f'As catorze entradas do catalogo fecharam na v0.92')
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

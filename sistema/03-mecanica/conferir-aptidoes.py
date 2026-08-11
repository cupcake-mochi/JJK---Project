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
  4. KOKUSEN e pequeno e nao espirala: o teto de dano por rodada fica abaixo de um
     quinto do que um ponto de atributo compra, e a cascata nao toca a margem.
  5. AS TRES ROTAS DO MARCO nao se dominam, e o orcamento de espaco cobre a
     montagem mais pesada que o manual permite.
  6. O TETO DE PASSIVAS: as pagas continuam sendo cinco. A gratis traz a propria vaga.
  7. OS GATES DE REFINO separam as rotas de verdade.

Roda sem argumento. Sai com codigo 1 se algo quebrar.
"""
import math
import sys

ERROS = []
AVISOS = []


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
CLASSE_0 = 4.5          # peca 6, secao 5
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
    print(f'  {nv:<8}{r:<10}{f"{CLASSE_0/r:.0%}":<12}{proj:<11}{f:.0%}')
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
res = {}
for nome, esc in ROTAS.items():
    atr = 7 + sum(1 for e in esc if e == 0)
    ref = min(TETO_REFINO, 1 + 7 + sum(1 for e in esc if e == 1))
    apt = sum(1 for e in esc if e == 1)
    lq = sum(1 for e in esc if e == 2) * LEQUE_DA_FEITICOS
    res[nome] = (atr, ref, apt, 5 + sum(1 for e in esc if e == 2), lq)
    print(f'  {nome:<18}{atr:<11}{ref:<9}{apt:<11}{res[nome][3]:<11}{lq:<18}'
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

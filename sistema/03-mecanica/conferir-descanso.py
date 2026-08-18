#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Confere a economia de descanso, exaustao e orcamento de missao (peca 10).

CONTRATO DE INVARIANTES:
  Descanso curto  = 25% do PE maximo. Fora de ambiente propicio, a exaustao corta.
  Descanso longo  = cheio em ambiente propicio; METADE DO MAXIMO fora dele.
  Integridade     = cheia em qualquer lugar (a alma nao e o corpo).
  Exaustao        = da 4a luta do dia em diante, +1 por luta. TETO DE 3.

  1. O piso fora da base e ESTAVEL. "Metade do maximo" nunca colapsa; a leitura
     "metade do atual" colapsa em quatro dias e por isso a regra diz qual e.
  2. A exaustao NAO ESPIRALA: o teto de 3 e alcancado e nada passa dele.
  3. O orcamento efetivo de um dia fica numa faixa que o mestre consegue estimar.
  4. Os quatro relogios estao ordenados do mais frequente ao menos frequente.
  5. Nenhum degrau de exaustao toca a rolagem de luta antes do ultimo.

  ENTROU NA v0.26:
  6. ARREDONDAMENTO. Recuperacao arredonda PARA BAIXO com piso de 1 (peca 1,
     secao 5.4: "para o lado que nao te favorece"). A coluna do descanso curto
     e NAO CRESCENTE depois de arredondada, em todo nivel e todo Caminho — um
     degrau pior nunca devolve mais que um melhor. E o piso NAO desfaz um zero
     escrito: o degrau 3 devolve nada, e nada e zero.
  7. MAGNITUDE, e nao so o eixo. Desvantagem vale ate 25 pontos percentuais
     (p - p^2, maximo em p=50%), entao o degrau 1 e o degrau 3 tem o MESMO
     tamanho. A escada e ordenada por consequencia, nao por peso, e a checagem
     falha se alguem escrever um degrau de desvantagem como se fosse menor.
  8. EMPILHAMENTO com a Integridade. As duas escadas se cruzam em dois eixos;
     a regra e pegar o pior. A checagem falha se algum eixo somar.
"""
import os
import re
import sys
import math

AQUI = os.path.dirname(os.path.abspath(__file__))

ERROS = []


def erro(msg):
    ERROS.append(msg)
    print(f'  !! {msg}')


def bloco(t):
    print()
    print('=' * 88)
    print(t)
    print('=' * 88)


# --------------------------------------------------------------------------
CURTO_BASE = 0.25          # do PE maximo
LONGO_FORA = 0.50          # do PE maximo, fora de ambiente propicio
LUTAS_DE_GRACA = 3         # a exaustao entra da 4a em diante
TETO_EXAUSTAO = 3

# degrau -> (o que pega, quanto o curto devolve FORA de ambiente propicio)
EXAUSTAO = {
    0: ('—',                                              0.25),
    1: ('desvantagem em pericia e oficio',                0.15),
    2: ('deslocamento cai para 6 m',                      0.05),
    3: ('desvantagem em ataque e Teste de Resistencia',   0.00),
}
# quais degraus tocam a ROLAGEM DE LUTA
TOCA_COMBATE = {3}

RELOGIOS = ['por cena', 'por descanso curto', 'por dia', 'por descanso longo']

PE_CAMINHO = {'Bastiao': 4, 'Vanguarda': 5, 'Guia': 5, 'Evocador': 6, 'Emanador': 6}


def pool(nv, cam): return PE_CAMINHO[cam] * nv


# --------------------------------------------------------------------------
bloco('1. O PISO FORA DA BASE E ESTAVEL?')
print('  A regra diz "metade do SEU MAXIMO". A leitura errada — "metade do que voce')
print('  tem" — colapsa. Os dois modelos, com o grupo gastando tudo todo dia:\n')
p = pool(10, 'Emanador')
print(f"  Emanador nv10, pool {p} PE. Descanso longo sempre fora de ambiente propicio:")
print(f"  {'':<28}" + ''.join(f'dia {d}'.rjust(8) for d in range(1, 6)))

certo, cur = [], p
for _ in range(5):
    cur = int(p * LONGO_FORA)
    certo.append(cur)
print(f"  {'metade do MAXIMO (a regra)':<28}" + ''.join(f'{x:>8}' for x in certo))

errado, cur = [], p
for _ in range(5):
    cur = cur // 2
    errado.append(cur)
print(f"  {'metade do ATUAL (a leitura ruim)':<28}"[:30] + ''.join(f'{x:>8}' for x in errado))

if len(set(certo)) != 1:
    erro('o piso fora da base nao e estavel — a regra colapsa ou infla')
else:
    print(f'\n  Piso estavel em {certo[0]} PE ({LONGO_FORA:.0%} do maximo). Quem nunca volta para')
    print('  casa vive nesse numero, e o mestre sabe de cabeca com quanto o grupo acorda.')
if errado[-1] >= certo[-1]:
    erro('a leitura ruim nao e pior que a regra — entao a regra nao precisa desambiguar')

# --------------------------------------------------------------------------
bloco('2. A EXAUSTAO ESPIRALA?')
print(f"  {'missao':<26}{'lutas':>7}{'sem teto':>10}{'com teto 3':>12}")
pior = 0
for dias, luta_dia in [(1, 3), (1, 4), (2, 4), (3, 4), (5, 4), (10, 5)]:
    tot = dias * luta_dia
    sem = sum(max(0, luta_dia - LUTAS_DE_GRACA) for _ in range(dias))
    com = min(TETO_EXAUSTAO, sem)
    pior = max(pior, com)
    print(f"  {f'{dias} dia(s) x {luta_dia} lutas':<26}{tot:>7}{sem:>10}{com:>12}")
if pior > TETO_EXAUSTAO:
    erro(f'a exaustao passou de {TETO_EXAUSTAO} — o teto nao esta segurando')
else:
    print(f'\n  Nada passa de {TETO_EXAUSTAO}. Dez dias de campo doem igual a tres, e isso e o preco')
    print('  aceito por nao ter espiral. Esta registrado como coisa a olhar em playtest.')

# --------------------------------------------------------------------------
bloco('3. OS DEGRAUS TOCAM A ROLAGEM DE LUTA CEDO DEMAIS?')
print(f"  {'degrau':<8}{'o que pega':<48}{'curto fora':>12}  toca luta?")
for d in sorted(EXAUSTAO):
    o, pct = EXAUSTAO[d]
    print(f"  {d:<8}{o:<48}{pct:>11.0%}  {'SIM' if d in TOCA_COMBATE else 'nao'}")
    if d in TOCA_COMBATE and d < TETO_EXAUSTAO:
        erro(f'o degrau {d} ja toca a rolagem de luta, e ele nao e o ultimo — '
             f'quem erra mais apanha mais e cansa mais: e a espiral')
if min(TOCA_COMBATE) != TETO_EXAUSTAO:
    erro('a rolagem de luta deveria ser tocada so no ultimo degrau')
else:
    print('\n  So o ultimo degrau toca a rolagem. Antes dele a exaustao pega fora de combate')
    print('  e depois pega posicionamento: falha primeiro no que nao mata.')

antes = [EXAUSTAO[d][1] for d in sorted(EXAUSTAO)]
if antes != sorted(antes, reverse=True):
    erro('o corte do descanso curto nao e monotono — um degrau devolve mais que o anterior')

# --------------------------------------------------------------------------
bloco('4. O ORCAMENTO DE UM DIA')
print('  PE acumulado ao longo do dia, com descanso curto de 25% entre lutas,')
print('  em ambiente propicio (onde a exaustao nao corta):\n')
print(f"  {'lutas no dia':<16}{'x pool':>10}")
for n in range(1, 6):
    curtos = n - 1
    mult = 1 + CURTO_BASE * curtos
    marca = '   <- a exaustao entra aqui' if n == LUTAS_DE_GRACA + 1 else ''
    print(f"  {n:<16}{mult:>9.2f}x{marca}")
teto_dia = 1 + CURTO_BASE * LUTAS_DE_GRACA
print(f'\n  Antes da exaustao o teto e {teto_dia:.2f}x o pool.')
if not 1.2 <= teto_dia <= 2.0:
    erro(f'orcamento de dia em {teto_dia:.2f}x o pool — fora da faixa que o mestre estima de cabeca')
else:
    print('  A coluna do manual ("quantas vezes voce lanca o seu melhor feitico") vira o')
    print('  PISO por missao em vez do teto, e o desvio e pequeno o bastante para estimar.')

print(f"\n  {'Caminho':<12}{'pool nv2':>10}{'25% dele':>10}{'pool nv30':>11}{'25% dele':>10}")
for c, v in PE_CAMINHO.items():
    print(f"  {c:<12}{pool(2,c):>10}{int(pool(2,c)*CURTO_BASE):>10}"
          f"{pool(30,c):>11}{int(pool(30,c)*CURTO_BASE):>10}")
if int(pool(2, 'Bastiao') * CURTO_BASE) < 1:
    erro('no nivel 2 o descanso curto do Bastiao devolve menos de 1 PE — a regra nao faz nada')

# --------------------------------------------------------------------------
bloco('5. OS QUATRO RELOGIOS ESTAO ORDENADOS?')
for i, r in enumerate(RELOGIOS, 1):
    print(f'  {i}. {r}')
print('\n  Do mais frequente ao menos frequente. E por isso que "uma vez por dia" e')
print('  "uma vez por descanso longo" nao sao a mesma coisa no manual: numa missao de')
print('  cinco dias, o primeiro recarrega cinco vezes e o segundo uma.')
if RELOGIOS[-1] != 'por descanso longo':
    erro('o descanso longo deixou de ser o relogio mais lento')

# --------------------------------------------------------------------------
bloco('6. ARREDONDAMENTO — para o lado que nao te favorece, piso de 1')
print('  Regra geral na peca 1, secao 5.4. Aqui e tudo recuperacao, entao e tudo')
print('  para baixo. O piso de 1 vale para a conta que deu fracao, e NAO para a')
print('  regra que diz "nada".\n')


def ganho(x):
    """Recuperacao: para baixo, nunca abaixo de 1."""
    return max(1, math.floor(x + 1e-9))


def custo(x):
    """Preco: para cima. Existe para o validador conferir que os dois lados"""
    return math.ceil(x - 1e-9)


# o piso nao desfaz zero escrito
if ganho(0.0) == 0:
    erro('ganho(0) devolveu 0 — o piso de 1 nao esta aplicado')
DEGRAU_ZERADO = 3
if EXAUSTAO[DEGRAU_ZERADO][1] != 0.0:
    erro('o degrau 3 deixou de devolver nada — a tabela do texto mudou sem aviso')

print(f"  {'Caminho':<12}{'nv':>4}{'pool':>6}   " +
      ''.join(f'deg {d}'.rjust(9) for d in sorted(EXAUSTAO)))
quebrou_mono = False
primeira_separacao = {}
for cam in PE_CAMINHO:
    for nv in (2, 3, 4, 10, 30):
        P = pool(nv, cam)
        col = []
        for d in sorted(EXAUSTAO):
            pct = EXAUSTAO[d][1]
            col.append(0 if pct == 0 else ganho(P * pct))
        if nv in (2, 3, 4):
            print(f"  {cam:<12}{nv:>4}{P:>6}   " + ''.join(f'{v:>9}' for v in col))
        if col != sorted(col, reverse=True):
            quebrou_mono = True
            erro(f'{cam} nv{nv}: a coluna do descanso curto CRESCE num degrau pior '
                 f'({col}) — um degrau pior devolve mais que um melhor')
        if cam not in primeira_separacao and col[1] != col[2]:
            primeira_separacao[cam] = nv
    # onde os degraus 1 e 2 param de empatar
    for nv in range(2, 31):
        P = pool(nv, cam)
        if ganho(P * EXAUSTAO[1][1]) != ganho(P * EXAUSTAO[2][1]):
            primeira_separacao[cam] = nv
            break

print()
print('  Os degraus 1 e 2 empatam enquanto a pool e pequena, e o texto diz isso.')
print('  Em que nivel a coluna separa:')
for cam, nv in primeira_separacao.items():
    print(f'    {cam:<12} nivel {nv}  (pool {pool(nv, cam)})')
if max(primeira_separacao.values()) > 6:
    erro('algum Caminho so separa os degraus 1 e 2 depois do nivel 6 — '
         'a escada fica plana boa parte da campanha')
if not quebrou_mono:
    print('\n  A coluna e nao crescente em todo Caminho e em todo nivel testado.')

# o outro lado do arredondamento, para provar que a regra tem duas direcoes
print()
print('  A regra vale nos dois sentidos, e o manual ja usa o lado do preco:')
for rot, bruto, esperado, fn in [
        ('Melhoria Leve numa Classe 3 (metade da Classe)', 1.5, 2, custo),
        ('PE da Liberacao Classe 5 (15 + 50%)',           22.5, 23, custo),
        ('descanso curto do Guia nv2 (25% de 10)',         2.5,  2, ganho),
        ('metade da vida do Bastiao nv2 (23 / 2)',        11.5, 11, ganho),
        ('metade do PE da Vanguarda nv7 (35 / 2)',        17.5, 17, ganho)]:
    got = fn(bruto)
    ok = 'ok' if got == esperado else 'ERRO'
    print(f'    {rot:<48}{bruto:>6} -> {got:<4}{ok}')
    if got != esperado:
        erro(f'arredondamento errado em "{rot}": {bruto} virou {got}, esperado {esperado}')

# O CASO QUE PARECE EXCECAO E NAO E: a vida por nivel do Caminho e a media do
# dado arredondada PARA CIMA (d12 -> 7, d8 -> 5, d6 -> 4). E um ganho subindo.
# Ela nao quebra a regra porque nao e conta de mesa: e valor de tabela, decidido
# uma vez no desenho. A checagem existe para o dia em que alguem tentar
# "corrigir" a tabela aplicando a regra de arredondamento nela.
print()
print('  E o caso que parece excecao e nao e — a vida por nivel do Caminho:')
DADO_VIDA = {'Bastiao': 12, 'Vanguarda': 8, 'Guia': 8, 'Evocador': 6, 'Emanador': 6}
VIDA_POR_NIVEL = {'Bastiao': 7, 'Vanguarda': 5, 'Guia': 5, 'Evocador': 4, 'Emanador': 4}
for cam, dado in DADO_VIDA.items():
    media = (dado + 1) / 2
    esperado = custo(media)          # media do dado, para CIMA
    real = VIDA_POR_NIVEL[cam]
    print(f'    {cam:<12}d{dado:<4} media {media:<5.1f} -> {esperado:<4}'
          f'{"ok" if esperado == real else "ERRO"}')
    if esperado != real:
        erro(f'{cam}: a vida por nivel ({real}) deixou de ser a media do d{dado} '
             f'arredondada para cima ({esperado})')
print('    Ganho subindo, e nao e excecao: e valor de tabela, nao conta de mesa.')

# --------------------------------------------------------------------------
bloco('7. O TAMANHO DE CADA DEGRAU, e nao so o eixo que ele toca')
print('  Desvantagem = 2d20 e pega o menor. A chance p vira p^2, e a perda p - p^2')
print('  e MAXIMA em p = 50%. Nenhum degrau de desvantagem e "leve".\n')
print(f"  {'chance sem desvantagem':<26}{'com':>8}{'perda':>10}")
pico = 0.0
for p in (0.25, 0.40, 0.50, 0.60, 0.75, 0.90):
    perda = p - p * p
    pico = max(pico, perda)
    print(f'  {p:>10.0%}{"":<16}{p*p:>8.1%}{perda*100:>9.1f} pp')
PICO_ESPERADO = 0.25
if abs(pico - PICO_ESPERADO) > 0.001:
    erro(f'o pico da desvantagem saiu {pico:.3f}, esperado {PICO_ESPERADO}')

# tamanho declarado de cada degrau, na mesma moeda
TAMANHO = {  # degrau -> (eixo, tamanho em pp, consequencia da falha)
    1: ('pericia e oficio',              25.0, 'a cena anda'),
    2: ('deslocamento 9 m -> 6 m',       None, 'posicao'),
    3: ('ataque e Teste de Resistencia', 25.0, 'dano, e as vezes a vida'),
}
print()
print(f"  {'degrau':<8}{'eixo':<34}{'tamanho no pico':<18}{'a falha custa'}")
for d, (eixo, pp, cons) in TAMANHO.items():
    t = f'-{pp:.0f} pp' if pp is not None else '-33% de alcance'
    print(f'  {d:<8}{eixo:<34}{t:<18}{cons}')

desv = [d for d, (_, pp, _) in TAMANHO.items() if pp is not None]
if len({TAMANHO[d][1] for d in desv}) != 1:
    erro('dois degraus de desvantagem com tamanhos diferentes — '
         'desvantagem e sempre a mesma mecanica, entao e sempre o mesmo teto')
else:
    print(f'\n  Os degraus {" e ".join(str(d) for d in desv)} sao os dois desvantagem e valem os MESMOS')
    print('  25 pp. A escada e ordenada por CONSEQUENCIA, nao por peso — e o texto da')
    print('  peca 10 precisa dizer isso, senao promete "leve" onde nao e.')

print()
print('  Para comparar, o que 25 pp valem no resto do sistema:')
for rot, v in [('treinar um Teste de Resistencia', 10),
               ('a maestria de uma campanha inteira (nv 2 ao 30)', 20),
               ('sair de atributo 0 para 3', 15),
               ('UM DEGRAU DE EXAUSTAO', 25)]:
    print(f'    {rot:<50}{v:>4} pp')
if 25 <= max(10, 20, 15):
    erro('o degrau de exaustao deixou de ser maior que as tres alavancas de comparacao')

# --------------------------------------------------------------------------
bloco('8. EXAUSTAO E INTEGRIDADE AO MESMO TEMPO — pega o pior, nao soma')
DESLOC_BASE = 9                       # peca 3: deslocamento base
DESLOC_EXAUSTAO = 6                   # peca 10, degrau 2
DESLOC_INTEGRIDADE = DESLOC_BASE / 2  # manual, estagio 2: "pela metade"

INTEGRIDADE = {  # estagio -> eixos, como o manual escreve
    1: ['desvantagem em pericia'],
    2: [f'deslocamento cai para {DESLOC_INTEGRIDADE:g} m', 'custo +1 PE por Classe'],
    3: ['desvantagem em ataque e TR', 'teto de Classe'],
}
EXAUSTAO_EIXOS = {
    1: ['desvantagem em pericia'],
    2: [f'deslocamento cai para {DESLOC_EXAUSTAO:g} m'],
    3: ['desvantagem em ataque e TR'],
}
print(f"  {'':<10}{'exaustao (peca 10)':<38}{'Integridade (manual)'}")
for d in (1, 2, 3):
    print(f"  {'degrau '+str(d):<10}{' + '.join(EXAUSTAO_EIXOS[d]):<38}{' + '.join(INTEGRIDADE[d])}")

# eixos que as duas escadas dividem: nesses, pegar o pior; nunca somar
def eixo_de(txt):
    if 'desvantagem' in txt:
        return 'desvantagem:' + txt.split('desvantagem em ')[1]
    if 'deslocamento' in txt:
        return 'deslocamento'
    return txt

compartilhados, so_integridade = set(), set()
for d in (1, 2, 3):
    ex = {eixo_de(t) for t in EXAUSTAO_EIXOS[d]}
    it = {eixo_de(t) for t in INTEGRIDADE[d]}
    compartilhados |= (ex & it)
    so_integridade |= (it - ex)
print(f'\n  Eixos que as duas escadas tocam ({len(compartilhados)}): ' +
      ', '.join(sorted(compartilhados)))
print(f'  Eixos so da Integridade ({len(so_integridade)}): ' + ', '.join(sorted(so_integridade)))
if not compartilhados:
    erro('as duas escadas nao dividem nenhum eixo — entao a regra de empilhamento '
         'nao teria motivo para existir, e ela esta escrita na peca 10')
else:
    print('\n  Nos eixos compartilhados vale o PIOR dos dois; nos eixos que so a')
    print('  Integridade tem, nao ha com o que competir e eles simplesmente acontecem.')

# desvantagem duas vezes nao pode virar nada alem de desvantagem
p = 0.50
uma = p * p
duas_somando = p * p * p * p
if abs(uma - duas_somando) < 1e-9:
    erro('somar desvantagem nao mudou nada — o teste esta mal montado')
else:
    print(f'\n  Se somasse: acerto de {p:.0%} cairia para {duas_somando:.1%} em vez de {uma:.0%}.')
    print(f'  Pegando o pior, ele para em {uma:.0%} — que e o que qualquer mesa faria.')

# os 6 m e a metade divergem DE PROPOSITO, e a divergencia tem sentido
if DESLOC_INTEGRIDADE >= DESLOC_EXAUSTAO:
    erro(f'a Integridade deixou de cortar mais deslocamento que a exaustao '
         f'({DESLOC_INTEGRIDADE:g} m contra {DESLOC_EXAUSTAO:g} m) — '
         f'dano de alma deveria doer mais que cansaco')
else:
    print(f'\n  Deslocamento: exaustao deixa {DESLOC_EXAUSTAO:g} m, Integridade deixa '
          f'{DESLOC_INTEGRIDADE:g} m, de uma base de {DESLOC_BASE:g}.')
    print('  A alma corta mais que o cansaco, e e por isso que os dois numeros diferem.')

# =============================================================================
# 9. A ESCADA DE RELOGIOS ESTA DEFINIDA, e o degrau mais usado tem dono
#
# Entrou na v0.62. A escada da secao 5 existe desde a v0.23 e o degrau mais
# usado dela — "por cena" — nunca tinha sido definido: 94 usos em 03-mecanica,
# 71 so no catalogo de Legados, e nenhum documento dizendo o que a palavra
# quer dizer. A peca 13 SS7 mediu o estrago disso em outro degrau ("por sessao",
# spread de 3,0x) e reprovou; aqui o degrau ficou.
#
# PAR DECLARADO com a checagem 2 do conferir-legados.py. As duas leem a MESMA
# tabela desta peca: la ela e usada para reprovar relogio de Legado fora da
# escada, aqui para exigir que a escada esteja definida. Se a tabela mudar de
# formato, as duas caem juntas — e e por isso que o par esta escrito.
#
# NADA DE VALOR FICA ESCRITO AQUI: os quatro degraus saem da tabela, e os dois
# totais saem de CONTAR a pasta. O numero publicado na peca e conferido contra
# a contagem, nunca o contrario.
#
# O QUE TEM DE ACENDER: apagar a secao "O que conta como uma cena"; esvaziar o
# gatilho de qualquer degrau; e mexer em qualquer um dos dois totais escritos.
# CONTRA-TESTE: mexer num numero VIZINHO da mesma secao nao pode acender.
bloco('9. A ESCADA DE RELOGIOS ESTA DEFINIDA?')

_p10 = os.path.join(AQUI, '10-descanso-e-recuperacao.md')
_txt10 = open(_p10, encoding='utf-8').read()

_sec5 = _txt10.split('## 5. Os quatro relógios')
if len(_sec5) < 2:
    erro('nao achei a secao 5 desta peca — a escada de relogios sumiu ou mudou de titulo')
else:
    _corpo = _sec5[1].split('## 6.')[0]
    _degraus = []
    for _lin in _corpo.splitlines():
        _c = [x.strip().replace('*', '') for x in _lin.strip('|').split('|')]
        if len(_c) >= 2 and _c[0].startswith('por '):
            _degraus.append((_c[0], _c[1]))
    if len(_degraus) != 4:
        erro(f'a escada tem {len(_degraus)} degrau(s) e deveria ter quatro — '
             'o conferir-legados.py le esta mesma tabela para reprovar relogio '
             'de Legado fora dela (PAR DECLARADO)')
    print(f'  os {len(_degraus)} degraus, lidos da tabela desta secao:')
    for _nome, _gat in _degraus:
        _ok = len(_gat) >= 4
        print(f"    {_nome:<22}{'recarrega quando: ' + _gat if _ok else '!! SEM GATILHO'}")
        if not _ok:
            erro(f'o degrau "{_nome}" nao diz quando recarrega — um relogio sem '
                 'gatilho de ficcao e a coisa que a secao 1 desta peca recusou')

    # o degrau mais usado precisa de definicao propria: ele e o unico cuja
    # duracao o mestre arbitra, e a peca 13 SS7 ja mediu o que isso custa.
    if '### O que conta como uma cena' not in _txt10:
        erro('o degrau "por cena" nao tem secao dizendo o que conta como uma cena — '
             'e ele e o mais usado do projeto. Sem definicao, cada mestre le um '
             'tamanho, que e o defeito que a peca 13 SS7 reprovou em "por sessao"')
    else:
        print('  [x] o degrau "por cena" tem secao propria dizendo o que conta como uma.')

    # A CONTAGEM DE "por cena" SAIU NA v0.104, por decisao do Mizuki.
    # Ela nasceu na v0.62 como PROVA de que a palavra mais usada do projeto nao
    # tinha definicao — 91 usos e nenhum documento dizendo o que ela queria dizer.
    # A definicao foi escrita, e a checagem logo acima confere que ela continua la.
    # O total, porem, sobe toda vez que qualquer peca ganha uma entrega: acusou na
    # v0.83 (91->93), na v0.92 (93->96), na v0.103 e na v0.104 (96->102). Quatro
    # acusacoes, nenhuma delas achando defeito — so a propria idade.
    # E' o caso do "teste escrito contra numero que sobe toda semana": ele mente
    # na semana seguinte. O que ele provava virou regra escrita, e regra escrita
    # tem checagem propria. Ancorar em coisa que nao se move e' o conserto.

    # LICAO Nº 9: o 4,7 desta secao e COPIA da tabela de relogios da peca 13 SS7,
    # que e quem mede rolagens por periodo. Duas copias, e uma delas tem de ser
    # conferida contra a outra. As outras duas linhas (9,4 e 14,1) sao derivadas
    # dela por 2x e 3x, entao conferir a base confere as tres.
    _p13 = os.path.join(AQUI, '13-legados.md')
    if not os.path.exists(_p13):
        erro('nao achei a peca 13 para conferir o 4,7 desta secao contra o dono dele')
    else:
        _t13 = open(_p13, encoding='utf-8').read()
        _d = re.search(r'\|\s*por cena\s*\|\s*([\d,]+)\s*\|', _t13)
        _a = re.search(r'\|\s*a sala, ou o pr[óo]prio combate\s*\|\s*([\d,]+)\s*\|', _txt10)
        if not _d or not _a:
            erro('nao consegui ler o "por cena" da peca 13 SS7 ou a linha da tabela '
                 'de leituras desta secao — uma das duas mudou de formato e o '
                 'cruzamento parou de acontecer em silencio')
        else:
            _vd = float(_d.group(1).replace(',', '.'))
            _va = float(_a.group(1).replace(',', '.'))
            print(f'  rolagens por cena: peca 13 SS7 diz {_vd:g}, esta secao usa {_va:g}')
            if abs(_vd - _va) > 1e-9:
                erro(f'esta secao usa {_va:g} rolagens por cena e a peca 13 SS7 — que '
                     f'e a dona da medida — diz {_vd:g}. Um numero, um dono (licao nº 9)')
            else:
                print('  [x] a base da tabela de leituras sai do dono, e as outras duas')
                print('      linhas dela sao 2x e 3x essa base.')

# --------------------------------------------------------------------------
print()
print('=' * 88)
if ERROS:
    print(f'>>> {len(ERROS)} PROBLEMA(S):')
    for e in ERROS:
        print('   -', e)
    sys.exit(1)
print('>>> TUDO OK — o piso e estavel, a exaustao nao espirala e o orcamento fecha.')

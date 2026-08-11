#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Confere a Expansao de Dominio: gates, ordem, preco em espacos e fragilidade.

A Expansao NAO e aptidao e nao mora na peca 11. Ela mora no manual (v7.7), no
molde de uma Passiva, comprada trocando espacos de feitico conhecido, com gate
duplo de nivel e refino, em dois degraus. Este validador existe porque os dois
gates caem em cima da curva de refino do arquitetura.md 4.3 — a mesma que o
conferir-aptidoes.py usa —, e no nivel 10 as tres rotas estao COLADAS (5/4/3).
Um gate ali nao tem folga para todo mundo: so da para escolher quem raspa.

CONTRATO DE INVARIANTES:
  1. OS GATES SEPARAM o que dizem separar, e ninguem alem disso.
  2. A ORDEM NUNCA INVERTE. A completa exige a incompleta, entao nao pode existir
     ficha que alcance a completa antes de poder ter comprado a incompleta.
  3. BARRADO E ATRASADO, NAO TRANCADO. Toda rota chega aos dois degraus antes do
     nivel 30 — o gate compra tempo, nao exclusao permanente.
  4. O PRECO FECHA. Incompleta 2 espacos, completa 3 no total (+1 de upgrade), e
     as tres linhas de orcamento da peca 11 so fecham com esses numeros.
  5. A RESPOSTA CHEGA ANTES DA AMEACA. A completa acerta garantido, e isso so e
     jogavel porque o anti-dominio e barato: um unico marco de Refino, no nivel 6,
     compra a CESTA OCA DE VIME (Classe 1, sem gate) — antes de qualquer um poder
     comprar a incompleta. (Ate a v0.28 esta linha dizia Dominio Simples; a
     pesquisa na obra mostrou que a Cesta Oca e a predecessora que ele melhorou,
     e portanto a barata das duas.)
  6. FRAGILIDADE MEDIDA NAS DUAS DIRECOES. Um gate com folga zero quebra se a
     curva cair; um gate com folga quebra se a curva subir. O validador nao
     escolhe por voce — ele nomeia quem cai em cada direcao, para a escolha ser
     feita com o numero na frente e nao de memoria.
  7. AS QUATRO ANTI-DOMINIO. A mais barata alcanca as tres rotas antes da Expansao
     existir; o custo por rodada cabe no orcamento de lutas do dia sem evaporar; a
     Petala nunca anula o Acerto inteiro; e o raio do Dominio Simples nunca passa
     de um movimento, senao a defesa vira cerca.

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
# CONSTANTES. Mexeu aqui, o validador inteiro se move junto.
MARCOS = [6, 10, 14, 18, 22, 26, 30]
TETO_REFINO = 10

# curvas de refino, do arquitetura.md secao 4.3 — identicas as do conferir-aptidoes.py
CURVA = {
    'especialista': [3, 5, 7, 9, 10, 10, 10],
    'meio a meio':  [3, 4, 6, 7, 9, 10, 10],
    'generalista':  [2, 3, 4, 5, 6, 7, 8],
}

# (nivel minimo, refino minimo) — decididos na v0.28
GATE = {
    'incompleta': (10, 4),
    'completa':   (14, 5),
}

# em espacos de feitico conhecido. A completa e um upgrade: paga so a diferenca,
# no molde da Regra Propria do manual ("sobe pra Classe 2 e 3 pagando so a
# diferenca de espacos").
PRECO = {'incompleta': 2, 'completa': 3}

# custo de ABRIR, em multiplos da maior Classe. A regua e a Tecnica Maxima, que
# custa 5 x maior Classe: a Expansao tem que passar dela, porque ela custou espaco
# de lista e dois gates para existir, e a Maxima e dada de graca no nivel 17.
PE_ABRIR = {'incompleta': 6, 'completa': 8}
PE_TECNICA_MAXIMA = 5

# desconto de PE nos feiticos lancados LA DENTRO, como divisor do refino.
# 3 = um terco do refino, 2 = metade. Piso de 1 no desconto, e piso de 1 no custo
# final do feitico — sem ele, o refino 10 zera toda Classe baixa e o PE deixa de
# existir como recurso dentro do dominio.
DESCONTO_DIVISOR = {'incompleta': 3, 'completa': 2}
PISO_CUSTO_FEITICO = 1

# duracao em rodadas = refino // DURACAO_DIVISOR, minimo 1
DURACAO_DIVISOR = 2

# vida da barreira, por fora: BARREIRA_FATOR x (refino // 2). Por dentro nao quebra.
BARREIRA_FATOR = 50

# a coluna Rotina do manual — dano por rodada de um Classe da faixa. E a regua
# contra a qual a barreira e medida: quantas rodadas de saida cheia ela aguenta.
ROTINA = {1: 13, 2: 31, 3: 45, 4: 63, 5: 76, 6: 94, 7: 108}


def maior_classe(nv):
    for c, n in ((7, 26), (6, 21), (5, 17), (4, 13), (3, 9), (2, 5), (1, 1)):
        if nv >= n:
            return c
    return 1


def duracao(r):
    return max(1, r // DURACAO_DIVISOR)


def desconto(degrau, r):
    return max(1, r // DESCONTO_DIVISOR[degrau])

# quem o gate DEVE barrar no nivel do proprio gate. Isto e a intencao escrita,
# e a checagem 1 falha se a curva parar de produzi-la.
BARRA_ESPERADO = {
    'incompleta': {'generalista'},
    'completa':   {'generalista'},
}

DEGRAUS = ['incompleta', 'completa']


def refino_em(rota, nv):
    r = 1
    for i, m in enumerate(MARCOS):
        if nv >= m:
            r = CURVA[rota][i]
    return r


def abre_em(rota, degrau, curva=None):
    """Primeiro marco em que a rota satisfaz nivel E refino. None se nunca."""
    nvg, rg = GATE[degrau]
    for i, m in enumerate(MARCOS):
        r = (curva or CURVA)[rota][i]
        if m >= nvg and r >= rg:
            return m
    return None


def feiticos_base(nv):
    return 2 + nv // 2


def espacos(nv):
    """Espacos de feitico conhecido: 2 + nivel/2, mais um por marco."""
    return feiticos_base(nv) + sum(1 for m in MARCOS if nv >= m)


# --------------------------------------------------------------------------
bloco('1. OS GATES SEPARAM O QUE DIZEM SEPARAR?')

print('  A curva de refino, nos dois niveis que importam:\n')
print(f"  {'nivel':<9}" + ''.join(f'{r:<16}' for r in CURVA))
for nv in (10, 14):
    print(f'  {nv:<9}' + ''.join(f'{refino_em(r, nv):<16}' for r in CURVA))

for degrau in DEGRAUS:
    nvg, rg = GATE[degrau]
    print(f'\n  {degrau} — nivel {nvg} e refino {rg}')
    barrou = set()
    for rota in CURVA:
        val = refino_em(rota, nvg)
        folga = val - rg
        if folga < 0:
            barrou.add(rota)
        estado = 'passa' if folga >= 0 else 'BARRA'
        print(f'    {rota:<16}refino {val:<4}{estado:<8}folga {folga:+d}')
    if barrou != BARRA_ESPERADO[degrau]:
        erro(f'o gate da {degrau} barra {sorted(barrou) or "ninguem"}, e a intencao '
             f'escrita e barrar {sorted(BARRA_ESPERADO[degrau])}')

print('\n  No nivel 10 as tres rotas estao em 5 / 4 / 3 — coladas, sem buraco entre elas.')
print('  Logo, qualquer gate que barre o generalista pega o meio a meio com folga ZERO.')
print('  Isso nao e escolha de numero: e o formato da curva. So da para escolher quem raspa.')


# --------------------------------------------------------------------------
bloco('2. A ORDEM INVERTE EM ALGUM LUGAR?')

print('  A completa exige ter a incompleta. Entao nenhuma rota pode alcancar a')
print('  completa num marco anterior ao da incompleta.\n')
print(f"  {'rota':<18}{'incompleta':<16}{'completa':<16}{'distancia'}")
for rota in CURVA:
    a, b = abre_em(rota, 'incompleta'), abre_em(rota, 'completa')
    d = f'{b - a} niveis' if a is not None and b is not None else '—'
    print(f'  {rota:<18}nv {str(a):<13}nv {str(b):<13}{d}')
    if a is None:
        erro(f'a rota "{rota}" nunca alcanca a incompleta')
        continue
    if b is None:
        erro(f'a rota "{rota}" nunca alcanca a completa')
        continue
    if b < a:
        erro(f'a rota "{rota}" alcanca a completa no nv {b} e a incompleta so no '
             f'nv {a} — a exigencia de ter a incompleta vira letra morta')

# a inversao tambem pode nascer dos gates sozinhos, sem passar por rota nenhuma
if GATE['completa'][0] < GATE['incompleta'][0] or GATE['completa'][1] < GATE['incompleta'][1]:
    erro('o gate da completa e mais FROUXO que o da incompleta em algum eixo — '
         'quem alcanca a completa deveria automaticamente alcancar a incompleta')
else:
    print('\n  Os dois eixos do gate da completa sao >= os da incompleta, entao a')
    print('  inversao nao pode nascer nem dos gates nem da curva.')


# --------------------------------------------------------------------------
bloco('3. BARRADO E ATRASADO, OU TRANCADO?')

print('  "Generalista barrado" precisa querer dizer ATRASADO. Se alguma rota nao')
print('  chega antes do nivel 30, o gate deixou de comprar tempo e passou a excluir.\n')
for degrau in DEGRAUS:
    nvg, _ = GATE[degrau]
    esp = abre_em('especialista', degrau)
    print(f'  {degrau}:')
    for rota in CURVA:
        v = abre_em(rota, degrau)
        atraso = (v - esp) if (v is not None and esp is not None) else None
        marca = '' if not atraso else f'  ({atraso} niveis atras do especialista)'
        print(f'    {rota:<16}nv {v}{marca}')
        if v is None:
            erro(f'a rota "{rota}" nunca chega a {degrau} — isso e exclusao, nao atraso')
        elif v > 30:
            erro(f'a rota "{rota}" so chega a {degrau} depois do teto lendario')

atraso_gen = abre_em('generalista', 'completa') - abre_em('especialista', 'completa')
if atraso_gen < 4:
    erro(f'o generalista fica so {atraso_gen} niveis atras na completa — o gate de '
         'refino parou de comprar acesso')
elif atraso_gen > 12:
    aviso(f'o generalista fica {atraso_gen} niveis atras na completa; acima de doze '
          'a diferenca deixa de ser atraso e vira exclusao na pratica')
else:
    print(f'\n  O generalista chega a completa {atraso_gen} niveis depois do especialista.')
    print('  Ele nao e trancado fora dela: ele paga em tempo o que nao pagou em marco.')


# --------------------------------------------------------------------------
bloco('4. O PRECO EM ESPACOS FECHA COM AS TABELAS DA PECA 11?')

if PRECO['completa'] - PRECO['incompleta'] != 1:
    erro(f'a completa custa {PRECO["completa"]} e a incompleta {PRECO["incompleta"]}: '
         'a diferenca deixou de ser 1, e o molde da Regra Propria e "pagar so a diferenca"')

# as tres linhas que a peca 11, secao 3, publica
ESPERADO = {
    'so feitico':                       {14: 12, 20: 16, 26: 21, 30: 24},
    '3 Passivas C2':                    {14: 6,  20: 10, 26: 15, 30: 18},
    '3 Passivas C2 + completa':         {14: 3,  20: 7,  26: 12, 30: 15},
    '5 Passivas C3 + completa':         {14: 0,  20: 0,  26: 3,  30: 6},
}
CUSTO_MONTAGEM = {
    'so feitico': 0,
    '3 Passivas C2': 3 * 2,
    '3 Passivas C2 + completa': 3 * 2 + PRECO['completa'],
    '5 Passivas C3 + completa': 5 * 3 + PRECO['completa'],
}

print(f"  {'montagem':<28}" + ''.join(f'{f"nv{n}":<8}' for n in (14, 20, 26, 30)))
for nome, esperado in ESPERADO.items():
    linha = []
    for nv in (14, 20, 26, 30):
        calc = max(espacos(nv) - CUSTO_MONTAGEM[nome], 0)
        linha.append(calc)
        if calc != esperado[nv]:
            erro(f'"{nome}" no nv{nv}: a conta da {calc} e a peca 11 publica '
                 f'{esperado[nv]}')
    print(f'  {nome:<28}' + ''.join(f'{v:<8}' for v in linha))

print('\n  As quatro linhas so fecham com a incompleta a 2 espacos e a completa a 3.')
print('  O preco nao esta "a definir": ele ja esta travado por tabela publicada.')

# a montagem mais pesada que o manual permite
pesada = 5 * 3 + PRECO['completa']
cabe = next((nv for nv in range(2, 31) if espacos(nv) - pesada >= 0), None)
print(f'\n  A montagem mais pesada legal — cinco Passivas Classe 3 mais a completa —')
print(f'  pede {pesada} espacos, e cabe a partir do nivel {cabe}.')
if cabe is None or cabe > 26:
    erro(f'a montagem mais pesada que o manual permite so cabe no nivel {cabe} — o '
         'teto de cinco Passivas pagas voltou a ser letra morta')

print(f'\n  {"nivel":<9}{"espacos":<11}{"a incompleta e":<18}{"a completa e"}')
for nv in (10, 14, 18, 22, 26, 30):
    e = espacos(nv)
    print(f'  {nv:<9}{e:<11}{PRECO["incompleta"]/e:<18.0%}{PRECO["completa"]/e:.0%}')
peso10 = PRECO['completa'] / espacos(10)
if peso10 > 0.50:
    erro(f'no nivel 10 a completa come {peso10:.0%} da lista — o preco deixou de '
         'competir com as Passivas e passou a proibir')


# --------------------------------------------------------------------------
bloco('5. A RESPOSTA CHEGA ANTES DA AMEACA?')

print('  A completa acerta GARANTIDO. Isso so e jogavel porque a resposta e barata:')
print('  Dominio Simples nao tem gate de refino nem de nivel — custa uma escolha de')
print('  marco, e a primeira escolha de marco acontece no nivel 6.\n')

RESPOSTA_NIVEL = MARCOS[0]          # um marco de Refino, o mais cedo possivel
ameaca = min(v for v in (abre_em(r, 'incompleta') for r in CURVA) if v is not None)

print(f'  anti-dominio mais cedo (um marco de Refino, Dominio Simples)   nv {RESPOSTA_NIVEL}')
print(f'  Expansao mais cedo (incompleta, especialista ou meio a meio)   nv {ameaca}')
if RESPOSTA_NIVEL >= ameaca:
    erro(f'a resposta chega no nv {RESPOSTA_NIVEL} e a ameaca no nv {ameaca} — o '
         'acerto garantido existe antes de haver defesa contra ele')
else:
    print(f'\n  A resposta chega {ameaca - RESPOSTA_NIVEL} niveis antes da ameaca, e custa')
    print('  UM marco, uma vez. Nao e preciso ser do eixo do controle: e preciso gastar')
    print('  uma escolha nele, uma vez na campanha inteira.')

print('\n  Mas as duas rotas puras que nunca escolhem Refino — sempre Corpo e sempre')
print('  Leque — terminam com ZERO aptidoes, e portanto com zero resposta anti-dominio.')
print('  Isso e propriedade da rota e nao defeito do gate; o texto da peca 11 ja avisa')
print('  que quem nunca escolhe Refino termina sem aptidao nenhuma. Vale o playtest.')


# --------------------------------------------------------------------------
bloco('6. FRAGILIDADE — quem cai se a curva de refino se mexer?')

print('  Um gate com folga zero quebra se a curva CAIR; um gate com folga quebra se')
print('  ela SUBIR. Nenhum dos dois e seguro nas duas direcoes, e por isso a escolha')
print('  entre eles e sobre qual falha voce prefere ter.\n')


def curva_deslocada(passo):
    return {r: [min(TETO_REFINO, max(1, v + passo)) for v in vs] for r, vs in CURVA.items()}


for degrau in DEGRAUS:
    nvg, rg = GATE[degrau]
    print(f'  {degrau} (nv {nvg}, refino {rg}):')
    base = {r for r in CURVA if abre_em(r, degrau) == nvg}
    for passo, rotulo in ((-1, 'a curva cai 1'), (+1, 'a curva sobe 1')):
        c = curva_deslocada(passo)
        agora = {r for r in CURVA if abre_em(r, degrau, c) == nvg}
        saiu = sorted(base - agora)
        entrou = sorted(agora - base)
        partes = []
        if saiu:
            partes.append(f'PERDEM o degrau no nv{nvg}: {", ".join(saiu)}')
        if entrou:
            partes.append(f'passam a ter no nv{nvg}: {", ".join(entrou)}')
        print(f'    {rotulo:<16}{"; ".join(partes) if partes else "ninguem se move"}')
    raspam = sorted(r for r in CURVA if refino_em(r, nvg) - rg == 0)
    print(f'    quem raspa hoje  '
          f'{", ".join(raspam) + " (folga zero)" if raspam else "ninguem — todo mundo que passa tem folga"}')

print('\n  A leitura: a falha por curva que CAI e silenciosa — uma rota perde acesso e')
print('  ninguem percebe. A falha por curva que SOBE aparece na tabela da checagem 1,')
print('  que passa a acusar que o gate barra menos gente do que a intencao escrita.')
print('  Este validador torna as duas barulhentas, e e por isso que a escolha entre')
print('  refino 5 e refino 6 na completa deixou de ser aposta.')

alt = 6 if GATE['completa'][1] == 5 else 5
nvg = GATE['completa'][0]
barra_alt = {r for r in CURVA if refino_em(r, nvg) < alt}
if barra_alt == BARRA_ESPERADO['completa']:
    print(f'\n  Registrado: no nivel {nvg}, refino {GATE["completa"][1]} e refino {alt}')
    print('  separam EXATAMENTE as mesmas rotas. O escolhido nao compra separacao a')
    print('  mais que o outro — ele compra a direcao em que o gate falha.')


# --------------------------------------------------------------------------
bloco('7. O DESCONTO LA DENTRO PAGA A PROPRIA EXPANSAO?')

print('  A duracao e quantas rodadas o dominio fica de pe — e portanto quantos')
print('  feiticos saem la dentro. Se desconto x duracao alcancar o custo de abrir,')
print('  abrir o dominio fica de graca, e um preco que se paga sozinho nao e preco.\n')
for degrau in DEGRAUS:
    print(f'  {degrau} — abrir custa {PE_ABRIR[degrau]} x Classe, desconto '
          f'1/{DESCONTO_DIVISOR[degrau]} do refino')
    print(f"    {'nv':<6}{'Classe':<9}{'refino':<9}{'abrir':<9}{'duracao':<10}"
          f"{'economia':<11}{'saldo'}")
    for nv in (14, 18, 22, 26, 30):
        r = refino_em('especialista', nv)
        cl = maior_classe(nv)
        abrir = PE_ABRIR[degrau] * cl
        econ = desconto(degrau, r) * duracao(r)
        saldo = abrir - econ
        print(f'    {nv:<6}{cl:<9}{r:<9}{abrir:<9}{duracao(r):<10}{econ:<11}{saldo:+d}')
        if saldo <= 0:
            erro(f'{degrau} no nv{nv}: abrir custa {abrir} e o desconto devolve '
                 f'{econ} — a Expansao se paga sozinha, e o custo virou lucro')
        elif saldo < abrir * 0.25:
            aviso(f'{degrau} no nv{nv}: sobra so {saldo} de {abrir} depois do '
                  'desconto — o custo esta perto de evaporar')
    print()

if PE_ABRIR['completa'] <= PE_ABRIR['incompleta']:
    erro('a completa nao custa mais que a incompleta para abrir — o degrau de cima '
         'ficou mais barato que o de baixo')
if PE_ABRIR['incompleta'] <= PE_TECNICA_MAXIMA:
    erro(f'abrir a incompleta custa {PE_ABRIR["incompleta"]} x Classe e a Tecnica '
         f'Maxima custa {PE_TECNICA_MAXIMA} x — a Expansao ficou mais barata que o '
         'golpe que o nivel da de graca, e ela cobrou espaco de lista para existir')
else:
    print(f'  A escada de custo fecha: feitico do topo 3x < Tecnica Maxima '
          f'{PE_TECNICA_MAXIMA}x < incompleta {PE_ABRIR["incompleta"]}x '
          f'< completa {PE_ABRIR["completa"]}x.')


# --------------------------------------------------------------------------
bloco('8. O DESCONTO ZERA FEITICO?')

print('  Custo de um feitico = 3 x Classe. Com o desconto da completa no refino 10:\n')
print(f"  {'Classe':<9}{'custo':<9}" + ''.join(f'{"ref " + str(r):<11}' for r in (1, 5, 10)))
zerou = []
for cl in range(1, 8):
    custo = 3 * cl
    linha = []
    for r in (1, 5, 10):
        final = max(PISO_CUSTO_FEITICO, custo - desconto('completa', r))
        linha.append(final)
        if custo - desconto('completa', r) < PISO_CUSTO_FEITICO:
            zerou.append((cl, r))
    print(f'  {cl:<9}{custo:<9}' + ''.join(f'{v:<11}' for v in linha))

if PISO_CUSTO_FEITICO < 1:
    erro('nao ha piso no custo de feitico — no refino alto o desconto zera as '
         'Classes baixas e o PE deixa de existir como recurso dentro do dominio')
else:
    print(f'\n  O piso de {PISO_CUSTO_FEITICO} PE segura {len(zerou)} combinacao(oes) '
          'que ficariam em zero ou negativo.')
    print('  Sem ele, o dominio nao teria custo nenhum para quem investiu em refino.')


# --------------------------------------------------------------------------
bloco('9. A BARREIRA CAI DENTRO DA PROPRIA DURACAO?')

print('  A barreira so significa alguma coisa se der para derrubar antes de o tempo')
print('  acabar sozinho. Se ela aguentar mais do que a duracao, quem esta de fora')
print('  nao tem o que fazer, e a decisao de atacar ou esperar deixa de existir.\n')
print(f"  {'nv':<6}{'refino':<9}{'duracao':<10}{'Rotina':<9}{'barreira':<11}"
      f"{'aguenta':<12}{'da para derrubar?'}")
for nv in (14, 18, 22, 26, 30):
    r = refino_em('especialista', nv)
    dur = duracao(r)
    rot = ROTINA[maior_classe(nv)]
    vida = BARREIRA_FATOR * (r // 2)
    aguenta = vida / rot
    da = aguenta < dur
    print(f'  {nv:<6}{r:<9}{dur:<10}{rot:<9}{vida:<11}{aguenta:<12.1f}'
          f'{"sim" if da else "NAO — ela sobrevive ao proprio tempo"}')
    if not da:
        aviso(f'no nv{nv} a barreira aguenta {aguenta:.1f} rodadas contra uma duracao '
              f'de {dur} — de fora, ninguem consegue encurtar o dominio')

print('\n  Por dentro ela nao quebra, e isso e regra e nao numero.')
print('  E o mestre pode declarar que uma barreira cede fora desta conta — tres')
print('  dominios se atravessando, uma fraqueza ja estabelecida. Excecao declarada.')


# --------------------------------------------------------------------------
bloco('10. AS QUATRO ANTI-DOMINIO')

# Classe da aptidao -> (gate de refino, gate de nivel), da peca 11 secao 5
GATE_CLASSE_REFINO = {1: 1, 2: 4, 3: 7}
GATE_CLASSE_NIVEL = {1: 1, 2: 7, 3: 13}

# nome -> (Classe, multiplicador de PE por rodada sobre a maior Classe)
ANTIDOMINIO = {
    'Cesta Oca de Vime':   (1, 0.0),
    'Dominio Simples':     (2, 1.0),
    'Petala':              (2, 1.0),
    'Extensao de Dominio': (3, 1.5),
}
PE_POR_NIVEL_PISO = 4      # o Bastiao, que e o menor bolso do sistema
RODADAS_POR_LUTA = 3.5
LUTAS_DE_GRACA = 3         # a exaustao dispara da QUARTA (peca 10)


def abre_classe(rota, cl):
    for i, m in enumerate(MARCOS):
        if CURVA[rota][i] >= GATE_CLASSE_REFINO[cl] and m >= GATE_CLASSE_NIVEL[cl]:
            return m
    return None


print(f"  {'aptidao':<22}{'Classe':<8}{'especialista':<15}{'meio a meio':<15}"
      f"{'generalista':<15}{'PE/rodada'}")
for nome, (cl, mult) in ANTIDOMINIO.items():
    v = {r: abre_classe(r, cl) for r in CURVA}
    rot = 'nenhum' if mult == 0 else f'{mult:g} x Classe'
    print(f'  {nome:<22}{cl:<8}' + ''.join(f'nv {v[r]:<12}' for r in CURVA) + rot)

# --- a resposta chega antes da ameaca, para as TRES rotas
mais_barata = min(ANTIDOMINIO.values(), key=lambda x: x[0])[0]
pior_rota = max(abre_classe(r, mais_barata) for r in CURVA)
ameaca = min(v for v in (abre_em(r, 'incompleta') for r in CURVA) if v is not None)
print(f'\n  A anti-dominio mais barata e Classe {mais_barata}, e a rota mais lenta a')
print(f'  alcanca no nv {pior_rota}. A Expansao mais cedo aparece no nv {ameaca}.')
if pior_rota >= ameaca:
    erro(f'a anti-dominio mais barata so chega no nv {pior_rota} para alguma rota, e a '
         f'Expansao aparece no nv {ameaca} — a resposta deixou de chegar antes da ameaca')
else:
    print(f'  Folga de {ameaca - pior_rota} niveis, e ela vale para as tres rotas.')

# --- o upkeep cabe no orcamento de lutas do dia
# O multiplicador e LIDO da tabela acima, e nao escrito aqui. Uma primeira versao
# desta checagem tinha 1.0 na mao, e por isso nao enxergava mudanca na constante —
# o mesmo defeito que a checagem de dominancia do conferir-aptidoes.py tinha.
MULT_PADRAO = ANTIDOMINIO['Dominio Simples'][1]
print(f'\n  O custo por rodada ({MULT_PADRAO:g} x Classe), contra o dia de um Bastiao '
      '(o menor bolso):')
print(f"    {'nv':<6}{'Classe':<8}{'PE/rod':<9}{'uma luta':<11}{'% do dia':<11}{'lutas que cabem'}")
for nv in (10, 14, 20, 30):
    cl = maior_classe(nv)
    por = max(1, math.ceil(MULT_PADRAO * cl))
    luta = por * RODADAS_POR_LUTA
    dia = PE_POR_NIVEL_PISO * nv
    cabem = int(dia // luta)
    print(f'    {nv:<6}{cl:<8}{por:<9}{luta:<11.1f}{luta/dia:<11.0%}{cabem}')
    if cabem < LUTAS_DE_GRACA:
        erro(f'no nv{nv} o custo de {MULT_PADRAO:g} x Classe por rodada so cabe em '
             f'{cabem} luta(s), e o dia tem {LUTAS_DE_GRACA} de graca — segurar a '
             'defesa passou a custar o dia inteiro')
    if cabem > 2 * LUTAS_DE_GRACA:
        aviso(f'no nv{nv} o custo cabe em {cabem} lutas, mais que o dobro do dia — ele '
              'esta perto de evaporar')

# --- a Petala nao pode anular o Acerto inteiro
print('\n  A Petala devolve refino/2 Acertos, e a completa solta 1 + duracao:')
print(f"    {'refino':<9}{'Acertos que saem':<20}{'a Petala devolve':<20}{'sobra'}")
for r in (4, 6, 8, 10):
    saem = 1 + duracao(r)
    devolve = max(1, r // 2)
    print(f'    {r:<9}{saem:<20}{devolve:<20}{saem - devolve}')
    if devolve >= saem:
        erro(f'no refino {r} a Petala devolve {devolve} Acertos e a Expansao solta '
             f'{saem} — ela anula o Acerto inteiro, e o terceiro espaco da completa '
             'deixa de comprar alguma coisa')

# --- o raio do Dominio Simples nao pode virar cerca
MOVIMENTO = 9.0
print(f'\n  O raio do Dominio Simples (1,5 m + refino/2), contra o movimento de {MOVIMENTO:g} m:')
linha = []
for r in (1, 2, 4, 6, 8, 10):
    raio = 1.5 + r // 2
    linha.append(f'ref {r}: {raio:g} m')
    if raio > MOVIMENTO:
        erro(f'no refino {r} o raio e {raio:g} m e passa de um movimento ({MOVIMENTO:g} m) — '
             'quem esta dentro nao sai num turno, e a defesa virou cerca')
print('    ' + '  ·  '.join(linha))
print('    Nenhum passa de um movimento: ela e defesa, e nao prende ninguem.')

# --- a escada de upkeep segue a escada de Classe
ordem = sorted(ANTIDOMINIO.values())
if [m for _, m in ordem] != sorted(m for _, m in ordem):
    erro('o custo por rodada nao cresce junto com a Classe da aptidao — uma Classe '
         'menor esta custando mais PE que uma maior')
else:
    print('\n  O custo por rodada nao decresce com a Classe: 0 · 1 · 1 · 1,5.')
    print('  A Cesta Oca e a unica de graca em PE, e e a unica que cobra o TURNO')
    print('  inteiro — cobrar as duas seria cobrar duas vezes pela mesma escolha.')


# --------------------------------------------------------------------------
print()
print('=' * 90)
if ERROS:
    print(f'>>> {len(ERROS)} PROBLEMA(S):')
    for e in ERROS:
        print('   -', e)
    sys.exit(1)
print('>>> TUDO OK — os gates separam o que dizem, a ordem nao inverte, o preco fecha')
print('    com as tabelas publicadas e a resposta anti-dominio chega antes da ameaca.')
if AVISOS:
    print(f'    {len(AVISOS)} aviso(s) acima, que nao falham o validador.')

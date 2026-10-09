#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Confere a Expansao de Dominio: gates, ordem, preco em espacos e fragilidade.

A Expansao NAO e aptidao e nao mora na peca 11. Ela mora no manual (v7.18), no
molde de um Talento, comprada trocando espacos de feitico conhecido, com gate
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
     existir; erguer (a maior Classe, toda vez, desde a v0.272) mais o PE de rodada
     cabe no orcamento de lutas do dia; a Petala segue a Essencia em ordem, nunca
     deixa passar mais do que nao ter ela, e o contra-ataque dela custa o que vale
     pela regua da peca 5; e o raio do Dominio Simples nunca passa de um
     movimento, senao a defesa vira cerca.
  9. O DEGRAU SEM BARREIRAS (v0.226) exclui o generalista DE PROPOSITO, e so ele;
     o raio de todos sai de 1,5 m x refino; nada disso mora aqui dentro.
  8. A DISPUTA DE DOMINIOS SO TEM UM NUMERO, O DESEMPATE. Ela entrou na v0.173 e e'
     toda derivada: cascata de refino, tipo de Acerto, e corrida sobre estado que ja
     tinha dono. Desde a v0.351 os blocos 11 a 12 leem o capitulo de Poderes avancados
     do R41, que e' o dono; ate a v0.350 liam o gerador do manual v7 (partE.js) e o
     capitulo 9 do livro v0.331, e cobravam que os dois concordassem. A caixa REFINO,
     EM UMA LINHA do manual nao existe no R41 e saiu sem substituto.

Roda sem argumento. Sai com codigo 1 se algo quebrar.
"""
import os
import math
import re
import sys
# v0.333: o gerador do manual e o livro v0.331 ficam congelados com o nome antigo da
# família da `Passiva` até o passo 5; o que vem deles passa pelo renomes.py.
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import renomes

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
#
# v0.174: a completa desceu de 8 para 6, por retorno de mesa — "acharam muito caro".
# As duas passaram a abrir pelo MESMO PE, e isso e' decisao e nao descuido: o manual
# ja escrevia que a completa "paga so a diferenca — um espaco a mais, no molde da
# Regra Propria", e cobrar +2x de PE por cima era uma segunda cobranca que a regua
# invocada nao previa. O degrau de cima continua se pagando em ESPACO (+1) e em
# GATE (nivel 14 e refino 5, contra 10 e 4).
#
# E o valor deixou de morar aqui na mesma versao: ele e' LIDO do gerador do manual,
# que e' o dono. Ele era a quinta copia do mesmo numero, e a lição no 9 nao abre
# excecao para constante de validador.
# v0.351: o dono passou a ser o R41. Ate a v0.350 o valor era lido do gerador do manual v7
# (partE.js), que esta congelado desde a v0.337.
import livro as _livro_abrir
try:
    _TXT_E = _livro_abrir.texto('poderes')
except _livro_abrir.LivroMudou:
    _TXT_E = ''

PE_ABRIR = None
_mi_abrir = re.search(r'(?m)^\| Incompleta \| (\d+) × maior Classe em PE \|', _TXT_E)
_mc_abrir = re.search(r'(?m)^\| Completa ou fechado \| (\d+) × maior Classe em PE \|', _TXT_E)
if _mi_abrir and _mc_abrir:
    PE_ABRIR = {'incompleta': int(_mi_abrir.group(1)), 'completa': int(_mc_abrir.group(1))}

if PE_ABRIR is None:
    erro('nao consegui ler o custo de abrir a Expansao na tabela "Abrir e manter" do R41 — '
         'as linhas esperadas sao "| Incompleta | N × maior Classe em PE |" e '
         '"| Completa ou fechado | M × maior Classe em PE |"')
    PE_ABRIR = {'incompleta': 6, 'completa': 6}   # so para o resto do arquivo rodar

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
    '3 Talentos C2':                    {14: 6,  20: 10, 26: 15, 30: 18},
    '3 Talentos C2 + completa':         {14: 3,  20: 7,  26: 12, 30: 15},
    '5 Talentos C3 + completa':         {14: 0,  20: 0,  26: 3,  30: 6},
}
CUSTO_MONTAGEM = {
    'so feitico': 0,
    '3 Talentos C2': 3 * 2,
    '3 Talentos C2 + completa': 3 * 2 + PRECO['completa'],
    '5 Talentos C3 + completa': 5 * 3 + PRECO['completa'],
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
print(f'\n  A montagem mais pesada legal — cinco Talentos de Categoria de Efeito 3 mais a completa —')
print(f'  pede {pesada} espacos, e cabe a partir do nivel {cabe}.')
if cabe is None or cabe > 26:
    erro(f'a montagem mais pesada que o manual permite so cabe no nivel {cabe} — o '
         'teto de cinco Talentos pagos voltou a ser letra morta')

print(f'\n  {"nivel":<9}{"espacos":<11}{"a incompleta e":<18}{"a completa e"}')
for nv in (10, 14, 18, 22, 26, 30):
    e = espacos(nv)
    print(f'  {nv:<9}{e:<11}{PRECO["incompleta"]/e:<18.0%}{PRECO["completa"]/e:.0%}')
peso10 = PRECO['completa'] / espacos(10)
if peso10 > 0.50:
    erro(f'no nivel 10 a completa come {peso10:.0%} da lista — o preco deixou de '
         'competir com os Talentos e passou a proibir')


# --------------------------------------------------------------------------
bloco('5. A RESPOSTA CHEGA ANTES DA AMEACA?')

print('  A completa acerta GARANTIDO. Isso so e jogavel porque a resposta e barata:')
print('  a Cesta Oca nao tem gate de refino nem de nivel — custa uma escolha de')
print('  marco, e a primeira escolha de marco acontece no nivel 6.\n')

RESPOSTA_NIVEL = MARCOS[0]          # um marco de Refino, o mais cedo possivel
ameaca = min(v for v in (abre_em(r, 'incompleta') for r in CURVA) if v is not None)

print(f'  anti-dominio mais cedo (um marco de Refino, Cesta Oca)        nv {RESPOSTA_NIVEL}')
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

if PE_ABRIR['completa'] < PE_ABRIR['incompleta']:
    erro(f'a completa abre por {PE_ABRIR["completa"]} x Classe e a incompleta por '
         f'{PE_ABRIR["incompleta"]} x — o degrau de CIMA ficou mais barato que o de '
         'baixo, e aí a incompleta deixa de ter para que existir')
elif PE_ABRIR['completa'] == PE_ABRIR['incompleta']:
    print(f'  As duas abrem pelo mesmo PE ({PE_ABRIR["completa"]}x), e isso e '
          'decisao da v0.174 e nao descuido.')
    print('  O degrau de cima se paga em ESPACO (+1, de 2 para 3) e em GATE (nivel')
    print('  14 e refino 5, contra 10 e 4). O manual ja escrevia que a completa')
    print('  "paga so a diferenca — um espaco a mais, no molde da Regra Propria";')
    print('  cobrar PE por cima era a segunda cobranca pelo mesmo degrau.')
if PE_ABRIR['incompleta'] <= PE_TECNICA_MAXIMA:
    erro(f'abrir a incompleta custa {PE_ABRIR["incompleta"]} x Classe e a Tecnica '
         f'Maxima custa {PE_TECNICA_MAXIMA} x — a Expansao ficou mais barata que o '
         'golpe que o nivel da de graca, e ela cobrou espaco de lista para existir')
else:
    _lig = '<' if PE_ABRIR['completa'] > PE_ABRIR['incompleta'] else '='
    print(f'  A escada de custo fecha: feitico do topo 3x < Tecnica Maxima '
          f'{PE_TECNICA_MAXIMA}x < incompleta {PE_ABRIR["incompleta"]}x '
          f'{_lig} completa {PE_ABRIR["completa"]}x.')


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

# Classe da aptidao -> (gate de refino, gate de nivel), da peca 11 secao 5.
# v0.268: o de nivel estava em 7 e 13, que a v0.260 subiu para o marco (10 e 14). O
# resultado nao mudava — o marco manda —, mas a copia estava velha.
GATE_CLASSE_REFINO = {1: 1, 2: 4, 3: 7}
GATE_CLASSE_NIVEL = {1: 1, 2: 10, 3: 14}

# O CUSTO POR RODADA e' LIDO da tabela "As quatro, com numero" da peca 11 §6.5.
# Ate a v0.267 ele morava aqui escrito a mao, como multiplicador da maior Classe; na
# v0.268 o Dominio Simples passou a custar `2` PE FIXOS, por decisao do Mizuki, e uma
# copia a mao nao acenderia com a troca de formato. Tres formatos: nenhum · N fixos ·
# X × maior Classe.
_P11_10 = open(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                            '11-aptidoes-e-refino.md'), encoding='utf-8').read()
ANTIDOMINIO = {}          # nome -> (Classe, formato, valor)
for _m10 in re.finditer(r'^\| \*\*(.+?)\*\* \| (\d) · [^|]*\|[^|]*\|[^|]*\| ([^|]+?) \|$',
                        _P11_10, re.M):
    _c10 = _m10.group(3).replace('`', '').replace('*', '').strip()
    _mf = re.match(r'(\d+) fixos?$', _c10)
    _mx = re.match(r'([\d,]+) × maior Classe$', _c10)
    if _c10 == 'nenhum':
        ANTIDOMINIO[_m10.group(1)] = (int(_m10.group(2)), 'fixo', 0.0)
    elif _mf:
        ANTIDOMINIO[_m10.group(1)] = (int(_m10.group(2)), 'fixo', float(_mf.group(1)))
    elif _mx:
        ANTIDOMINIO[_m10.group(1)] = (int(_m10.group(2)), 'x', float(_mx.group(1).replace(',', '.')))
if len(ANTIDOMINIO) != 4:
    erro(f'li {len(ANTIDOMINIO)} anti-dominio na tabela da peca 11 §6.5 e sao quatro — a tabela '
         'mudou de forma e este bloco parou de conferir o custo')
PE_POR_NIVEL_PISO = 4      # o Bastiao, que e o menor bolso do sistema
RODADAS_POR_LUTA = 3.5
LUTAS_DE_GRACA = 3         # a exaustao dispara da QUARTA (peca 10)
RODADAS_POR_MINUTO = 10


def custo_rodada(nome, nv):
    cl, fmt, val = ANTIDOMINIO[nome]
    if fmt == 'fixo':
        return val
    return max(1, math.ceil(val * maior_classe(nv)))


def abre_classe(rota, cl):
    for i, m in enumerate(MARCOS):
        if CURVA[rota][i] >= GATE_CLASSE_REFINO[cl] and m >= GATE_CLASSE_NIVEL[cl]:
            return m
    return None


print(f"  {'aptidao':<22}{'Classe':<8}{'especialista':<15}{'meio a meio':<15}"
      f"{'generalista':<15}{'PE/rodada'}")
for nome, (cl, fmt, val) in ANTIDOMINIO.items():
    v = {r: abre_classe(r, cl) for r in CURVA}
    rot = ('nenhum' if val == 0 else f'{val:g} fixo' + ('s' if val != 1 else '')) if fmt == 'fixo' else f'{val:g} x Classe'
    print(f'  {nome:<22}{cl:<8}' + ''.join(f'nv {v[r]:<12}' for r in CURVA) + rot)

# --- a resposta chega antes da ameaca, para as TRES rotas
mais_barata = min(c for c, _, _ in ANTIDOMINIO.values()) if ANTIDOMINIO else 1
pior_rota = max(abre_classe(r, mais_barata) for r in CURVA)
ameaca = min(v for v in (abre_em(r, 'incompleta') for r in CURVA) if v is not None)
print(f'\n  A anti-dominio mais barata e Classe {mais_barata}, e a rota mais lenta a')
print(f'  alcanca no nv {pior_rota}. A Expansao mais cedo aparece no nv {ameaca}.')
if pior_rota >= ameaca:
    erro(f'a anti-dominio mais barata so chega no nv {pior_rota} para alguma rota, e a '
         f'Expansao aparece no nv {ameaca} — a resposta deixou de chegar antes da ameaca')
else:
    print(f'  Folga de {ameaca - pior_rota} niveis, e ela vale para as tres rotas.')

# --- ERGUER custa a maior Classe, toda vez (v0.272, decisao do Mizuki: "deveria custar
# Maior Classe em PE, pra todos eles"). Ate a v0.271 este bloco conferia o custo POR RODADA
# da Petala, 1 x maior Classe, contra o orcamento de lutas do dia; na v0.272 a Classe mudou
# de lugar e a Petala passou a 1 PE fixo. Quem ergue pagando e' LIDO da frase da peca 11
# §6.5; o que se confere e' a regra aplicada (uma vez por luta, mais o PE de rodada) contra
# o limite de design (as lutas de graca do dia, peca 10).
_mer = re.search(r'^\*\*E erguer custa a sua maior Classe em PE, toda vez que ela sobe\*\* — (.+)$',
                 _P11_10, re.M)
ERGUER = [n for n in re.findall(r'`([^`]+)`', _mer.group(1).split('*')[0])] if _mer else []
if not _mer:
    erro('nao achei na peca 11 §6.5 a frase "E erguer custa a sua maior Classe em PE, toda vez '
         'que ela sobe" — a regra de erguer sumiu ou mudou de forma, e este bloco parou de conferir')
elif any(n not in ANTIDOMINIO for n in ERGUER) or not ERGUER:
    erro(f'a frase de erguer da peca 11 nomeia {ERGUER}, e a tabela das quatro tem {list(ANTIDOMINIO)}')
else:
    # v0.273: a Extensao entrou no erguer, e ela e' a cara DE PROPOSITO ("ela sai cara por
    # isso") — a tabela da secao dela mede o dia. O limite de caber nas lutas de graca vale
    # para as de Categoria de Efeito 1 e 2; para ela, o que se confere e' continuar a mais cara.
    print(f'\n  Erguer custa a maior Classe, toda vez: {", ".join(ERGUER)}. Uma vez por luta, mais o PE')
    print('  de rodada numa luta de 3,5 rodadas, contra o dia de um Bastiao (o menor bolso):')
    print(f"    {'nv':<6}{'Classe':<8}" + ''.join(f'{n[:18]:<20}' for n in ERGUER))
    for nv in (6, 10, 14, 20, 26, 30):
        cl = maior_classe(nv)
        dia = PE_POR_NIVEL_PISO * nv
        cel = []
        lutas_nv = {}
        for nome in ERGUER:
            if abre_classe('especialista', ANTIDOMINIO[nome][0]) > nv:
                cel.append('—'); continue
            luta = cl + custo_rodada(nome, nv) * RODADAS_POR_LUTA
            lutas_nv[nome] = luta
            cabem = int(dia // luta)
            cel.append(f'{luta:g} PE, {cabem} lutas')
            if ANTIDOMINIO[nome][0] >= 3:
                continue
            if cabem < LUTAS_DE_GRACA:
                erro(f'no nv{nv} erguer {nome} e segurar uma luta custa {luta:g} PE, e o dia do '
                     f'Bastiao ({dia}) so tem {cabem} disso — menos que as {LUTAS_DE_GRACA} lutas de graca')
        print(f'    {nv:<6}{cl:<8}' + ''.join(f'{c:<20}' for c in cel))
        _c3 = [n for n in lutas_nv if ANTIDOMINIO[n][0] >= 3]
        _c12 = [lutas_nv[n] for n in lutas_nv if ANTIDOMINIO[n][0] < 3]
        for n in _c3:
            if _c12 and lutas_nv[n] <= max(_c12):
                erro(f'no nv{nv} {n} custa {lutas_nv[n]:g} PE por luta e outra anti-dominio custa '
                     f'{max(_c12):g} — a peca 11 diz que ela e a mais cara das quatro')
    if re.search(r'e é a mais cara das quatro', _P11_10):
        print('  A Extensao fica fora do limite do dia de proposito, e e a mais cara das quatro em todo nivel.')
    else:
        erro('a peca 11 parou de dizer que a Extensao e a mais cara das quatro — e esta checagem '
             'isenta ela do limite do dia por causa disso')

# --- o custo FIXO (v0.268, o Dominio Simples). Decisao do Mizuki: o PE dele "so pra
# impedir de ninguem abrir dominio simples fora de combate e ficar andando por ai com
# ele", e barato em luta — o preco dele e' o relogio contra a Expansao. Entao o aviso
# de "evaporar" nao vale para ele, de proposito. O que vale: ele nao pode ser ZERO (a
# porta que o PE existe para fechar) e tem de caber nas lutas do dia.
for nome, (cl, fmt, val) in ANTIDOMINIO.items():
    if fmt != 'fixo' or cl == 1:
        continue
    # o zero vem ANTES de qualquer divisao: a primeira forma deste bloco dividia pelo
    # custo e depois perguntava se ele era zero, e o arnes da v0.268 viu ela morrer de
    # ZeroDivisionError — vermelha pelo motivo errado.
    if val <= 0:
        erro(f'{nome} custa zero PE por rodada: ele fica de pe o dia inteiro fora de combate, '
             'que e o que o custo fixo existe para impedir')
        continue
    print(f'\n  {nome}: {val:g} PE fixo' + ('s' if val != 1 else '') + ' por rodada. Fora de combate, o dia inteiro do Bastiao o segura por:')
    for nv in (10, 30):
        dia = PE_POR_NIVEL_PISO * nv
        print(f'    nv {nv}: {dia / val / RODADAS_POR_MINUTO:.1f} min · uma luta custa {val * RODADAS_POR_LUTA:g} PE, '
              f'{val * RODADAS_POR_LUTA / dia:.0%} do dia')
        if int(dia // (val * RODADAS_POR_LUTA)) < LUTAS_DE_GRACA:
            erro(f'no nv{nv} os {val:g} PE fixos de {nome} so cabem em '
                 f'{int(dia // (val * RODADAS_POR_LUTA))} luta(s) — o custo fixo deixou de ser barato em luta')

# --- a Petala (v0.272). Ate a v0.271 este bloco cobrava que ela nunca anulasse o Acerto
# inteiro ("sempre sobra um", refino/2 por cena). A decisao do Mizuki trocou o contador pela
# Essencia contra a do dono, e com Essencia maior ela anula; o que fica sao tres coisas.
_ip = _P11_10.find('### Pétala · Categoria de Efeito 2')
_sp = _P11_10[_ip:_P11_10.find('\n### ', _ip + 5)] if _ip >= 0 else ''
_ml = re.search(r'^\| \*\*o dano do Acerto que toca, que você leva\*\* \| (.+?) \| (.+?) \| (.+?) \|$', _sp, re.M)
_PAL = {'nada': 0.0, 'metade': 0.5, 'tudo': 1.0}
def _fracao(c):
    c = c.replace('`', '').strip()
    if c in _PAL: return _PAL[c]
    m = re.match(r'(\d+)/(\d+)$', c)
    return int(m.group(1)) / int(m.group(2)) if m else None
if not _ml:
    erro('nao achei a tabela da Essencia na secao da Petala (peca 11 §6.5) — o dano que ela deixa '
         'passar parou de ser conferido')
else:
    LEVA = [_fracao(x) for x in _ml.groups()]      # maior, igual, menor
    print(f'\n  A Petala, pela Essencia contra a do dono (maior / igual / menor): voce leva '
          + ' / '.join(f'{x:g}' if x is not None else '?' for x in LEVA) + ' do dano do Acerto que toca')
    if None in LEVA:
        erro(f'uma celula da tabela da Petala nao e fracao que eu leio: {_ml.groups()}')
    elif not (LEVA[0] <= LEVA[1] <= LEVA[2] < 1):
        erro(f'a Petala nao segue a Essencia em ordem: {LEVA} — Essencia maior tem de proteger '
             'pelo menos o que a igual protege, e a menor tem de proteger alguma coisa')
    # usar e erguer de novo nunca deixa passar mais do que nao ter ela. O pior caso e' cair em
    # todo intervalo; com a queda NA HORA, cada queda soma um Acerto inteiro.
    # lido so da CAIXA (as linhas `> `), que e' onde a regra mora: a frase aparece de novo na
    # explicacao, e o arnes da v0.272 viu a primeira forma ficar verde com a caixa trocada.
    _caixa = '\n'.join(l for l in _sp.split('\n') if l.startswith('> '))
    _na_hora = not bool(re.search(r'Quando ela cai, a Expansão não te alcança na hora', _caixa))
    if None not in LEVA:
        _pior = [(r, 1 + duracao(r), x) for r in (4, 6, 8, 10) for x in LEVA
                 if (1 + duracao(r)) * x + ((1 + duracao(r)) - 1 if _na_hora else 0) > (1 + duracao(r))]
        if _pior:
            erro(f'com a queda na hora, a Petala deixa passar mais do que nao ter ela no pior caso: '
                 f'(refino, Acertos, fracao) = {_pior[:3]}')
        else:
            print('  Sem a queda na hora, usar e erguer de novo nunca deixa passar mais do que nao ter ela,')
            print('  nem no pior caso, em refino 4 a 10.')
# o contra-ataque custa o que vale, pela regua da peca 5 §4
_mca = re.search(r'Cada contra-ataque custa `(\d+)` PE', _sp)
_P05 = open(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                         '05-caminho-e-combate-sem-feitico.md'), encoding='utf-8').read()
_arma = {int(n): float(a + '.' + b) for n, _, a, b in
         re.findall(r'^\| (\d+) \| (\d+) \| (\d+),(\d) \| [\d,]+× \|$', _P05, re.M)}
_m1 = re.search(r'`\+1` no \*\*seu\*\* acerto \| permanente \| `(\d+),(\d+)`', _P05)
_map = re.search(r'uma ação padrão a mais \| permanente \| `(\d+),(\d+)`', _P05)
_mpe = re.search(r'recuperar `\+1` PE \| permanente \| `(\d+),(\d+)`', _P05)
if not _mca:
    erro('nao achei "Cada contra-ataque custa `N` PE" na secao da Petala')
elif not (_arma and _m1 and _map and _mpe):
    erro('nao achei a regua da peca 5 (a arma do §2, o acerto, a acao e o PE do §4) — o preco do '
         'contra-ataque parou de ser conferido')
else:
    _base = 0.05 / (float(_m1.group(1) + '.' + _m1.group(2)) / float(_map.group(1) + '.' + _map.group(2)))
    _vant = (1 - (1 - _base) ** 2) / _base
    _cam = float(_mpe.group(1) + '.' + _mpe.group(2))
    _por = {n: _arma[n] * _vant / _cam for n in sorted(_arma) if n >= 10}
    _media = sum(_por.values()) / len(_por)
    print(f'  O contra-ataque vale ' + ' · '.join(f'{v:.2f} PE no nv {n}' for n, v in _por.items())
          + f' (media {_media:.2f}); a peca cobra {_mca.group(1)}.')
    if int(_mca.group(1)) != round(_media):
        erro(f'a Petala cobra {_mca.group(1)} PE por contra-ataque e a regua da peca 5 da '
             f'{_media:.2f} em media do nivel 10 ao 30 — o preco saiu do que ele vale')

# --- a copia do livro (cap. 45): a tabela da Essencia e o preco do contra-ataque moram em dois
# documentos, e a peca 11 e' a dona (licao no 9). Uma copia sem comparacao diverge.
_L45 = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '05-material', 'livro',
                         'manual', '45-aptidoes-e-refino.md'), encoding='utf-8').read()
_L45 = renomes.traduz(_L45)
_ll = re.search(r'^\| o dano do Acerto que toca, que você leva \| (.+?) \| (.+?) \| (.+?) \|$', _L45, re.M)
_lca = re.search(r'Cada contra-ataque custa `(\d+)` PE', _L45)
if not (_ll and _lca):
    erro('nao achei no capitulo 45 do livro a tabela da Essencia da Petala ou o preco do contra-ataque '
         '— a copia que a mesa le parou de ser comparada com a peca 11')
elif _ml and _mca and ([_fracao(x) for x in _ll.groups()] != [_fracao(x) for x in _ml.groups()]
                       or _lca.group(1) != _mca.group(1)):
    erro(f'o livro diverge da peca 11 na Petala: tabela {_ll.groups()} contra {_ml.groups()}, '
         f'contra-ataque {_lca.group(1)} contra {_mca.group(1)} PE — a peca e a dona')
else:
    print('  O capitulo 45 do livro copia a tabela da Essencia e o preco do contra-ataque igual a peca 11.')

# --- a Extensao (v0.273): tres coisas moram em varios documentos, e a peca 11 e' a dona. A
# caixa do livro dizia nivel 18 enquanto a tabela do mesmo capitulo e a peca diziam 14, desde
# a v0.176 — nada comparava. Hoje o gate, o que passa acima do teto e o Corpo Amaldicoado.
_ie = _P11_10.find('### Extensão de Domínio · Categoria de Efeito 3')
_se = _P11_10[_ie:_P11_10.find('\n### ', _ie + 5)] if _ie >= 0 else ''
_i45 = _L45.find('### Extensão de Domínio\n')
_s45 = _L45[_i45:_L45.find('\n## ', _i45)] if _i45 >= 0 else ''
_P09 = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '09-origens.md'), encoding='utf-8').read()
_L25 = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '05-material', 'livro',
                         'manual', '25-origens.md'), encoding='utf-8').read()
_L25 = renomes.traduz(_L25)
_gates_e = {
    'peca 11, titulo': re.search(r'### Extensão de Domínio · Categoria de Efeito 3, refino (\d+) e nível (\d+)', _P11_10),
    'peca 11, as quatro com numero': re.search(r'^\| \*\*Extensão de Domínio\*\* \| 3 · refino (\d+), nível (\d+) \|', _P11_10, re.M),
    'peca 11, o catalogo fechado': re.search(r'^\| 7 \| \*\*Extensão de Domínio\*\* \| Categoria de Efeito 3 · refino (\d+), nível (\d+)', _P11_10, re.M),
    # so' a linha do Requisito: a primeira forma pendurava o gate na frase do Corpo Amaldicoado,
    # e o contra-teste da v0.273 (tirar o Corpo Amaldicoado dos quatro lugares) acendeu por ela
    'livro, a caixa': re.search(r'^> Requisito: [^\n]*?refino (\d+) e nível (\d+)\.', _s45, re.M),
    'livro, a tabela': re.search(r'^\| Extensão de Domínio \| [^|]*refino (\d+) e nível (\d+)', _L45, re.M),
}
_falta_e = [k for k, v in _gates_e.items() if not v]
_vals_e = {k: v.groups() for k, v in _gates_e.items() if v}
if _falta_e:
    erro(f'nao achei o gate da Extensao em {_falta_e} — a copia parou de ser comparada')
elif len(set(_vals_e.values())) != 1:
    erro(f'o gate da Extensao diverge entre as copias: {_vals_e} — a peca 11 e a dona')
_le = [re.search(r'Acima dele, ela reduz o dano em um quarto, e você leva `(\d)/(\d)`', x) for x in (_se, _s45)]
if not all(_le):
    erro('nao achei "Acima dele, ela reduz o dano em um quarto, e você leva `N/N`" na peca 11 e no livro')
elif {m.groups() for m in _le} != {('3', '4')}:
    erro(f'o que passa acima do teto da Extensao nao e 3/4 nas duas copias: {[m.groups() for m in _le]} — '
         '"reduz em um quarto" e "leva 3/4" sao a mesma conta')
# lido so' da CAIXA da peca 11 (as linhas `> `): a frase aparece de novo no paragrafo que explica,
# e o contra-teste da v0.273 ficou vermelho pela explicacao — o mesmo defeito da queda na hora.
_cxe = '\n'.join(l for l in _se.split('\n') if l.startswith('> '))
_ca = {'peca 11': 'O Corpo Amaldiçoado não compra' in _cxe, 'livro, cap. 45': 'O Corpo Amaldiçoado não compra' in _s45,
       'peca 9': 'A `Extensão de Domínio` ele não compra' in _P09,
       'livro, cap. 25': 'a `Extensão de Domínio` você não compra' in _L25}
if len(set(_ca.values())) != 1:
    erro(f'o Corpo Amaldicoado fora da Extensao nao esta nos quatro lugares: {_ca}')
# o `Manejo` tem de estar ESCRITO, e nao so' implicito — o problema de preco do Mizuki: sem ele o
# Sem Tecnica ergueria a Extensao sem perder nada. Ate a v0.275 o nome era o que fazia a regra
# alcancar o Sem Tecnica, porque o capitulo 43 so' mandava ler `Manejo` nos capitulos 8 e 9. Desde a
# v0.276 ele manda ler em qualquer capitulo, e o nome ficou por clareza: a decisao da v0.273 foi
# escrever com todas as letras, e e' ela que esta checagem guarda.
_mj = {'peca 11, a caixa': 'você não usa feitiço nem `Manejo`' in _cxe,
       'livro, a caixa': 'você não usa feitiço nem `Manejo`' in _s45,
       'peca 11, o que custa por fora': bool(re.search(
           r'^\| \*\*Extensão de Domínio\*\* \|[^\n]*nenhum feitiço nem `Manejo`', _P11_10, re.M)),
       'livro, a tabela das quatro': bool(re.search(
           r'^\| \*\*Extensão de Domínio\*\*[^\n]*nenhum feitiço nem `Manejo`', _L45, re.M))}
if not all(_mj.values()):
    erro(f'a Extensao parou de proibir o `Manejo` com todas as letras em '
         f'{[k for k, v in _mj.items() if not v]} — a v0.273 decidiu escrever o nome, e ele fica por clareza')
# a caixa nao diz o que continua (v0.283). Decisao do Mizuki: "se n ta citado, n precisa ficar
# deixando claro". Ate a v0.282 ela dizia "A Tecnica Marcial e as aptidoes continuam", e desde a
# v0.276 a `Kata` vale como feitico (capitulo 42): a frase brigava com a primeira linha da caixa.
# Lido so' das linhas da caixa, nos dois lados, e so' do que e' de quem ergue — a barreira que
# "continua te prendendo" e a Expansao ja aberta que "continua" sao regra, e ficam.
_RX_CONT = re.compile(r'(Técnica Marcial|aptidões|reversa)[^.\n]*\bcontinua')
_cx45 = '\n'.join(l for l in _s45.split('\n') if l.startswith('> '))
_cont = {k: [m.group(0) for m in _RX_CONT.finditer(v)]
         for k, v in (('peca 11, a caixa', _cxe), ('livro, a caixa', _cx45))}
if any(_cont.values()):
    erro(f'a caixa da Extensao voltou a dizer o que continua: {_cont} — desde a v0.283 ela so diz '
         f'o que para, e a `Kata` vale como feitico desde a v0.276')
if (not _falta_e and len(set(_vals_e.values())) == 1 and all(_le) and len(set(_ca.values())) == 1
        and all(_mj.values()) and not any(_cont.values())):
    print(f'  A Extensao: o gate (refino, nivel) = {next(iter(_vals_e.values()))} nas cinco copias, acima do teto '
          f'voce leva 3/4 na peca e no livro, o Corpo Amaldicoado fora dela nos quatro lugares, o `Manejo` '
          f'proibido pelo nome nos quatro, e a caixa sem lista do que continua.')

# --- a queda na hora (v0.274): quando a Cesta cai, ou o Simples cai pelo voto, a Expansao te alcanca
# na hora, e esse Acerto e' A MAIS — o do comeco do turno do dono continua vindo. Decisao do Mizuki:
# "e basicamente um extra, chegando no comeco do turno do inimigo vc vai receber novamente". O texto
# antigo lia dos dois jeitos, e com dois golpes por rodada as duas leituras davam numeros diferentes
# (sistema/01-pesquisa/anti-dominios/conta-as-quatro.py, secao 6). Lido so' das CAIXAS: a frase volta no
# paragrafo que explica, e o defeito da v0.272 e da v0.273 foi justamente ler a explicacao.
_EXTRA = 'com um Acerto a mais: o do começo do turno do dono continua vindo'
_ic = _P11_10.find('### Cesta Oca de Vime · Categoria de Efeito 1')
_cxc = '\n'.join(l for l in _P11_10[_ic:_P11_10.find('\n### ', _ic + 5)].split('\n') if l.startswith('> ')) if _ic >= 0 else ''
_ic45 = _L45.find('> **Cesta Oca de Vime** —')
_cxc45 = _L45[_ic45:_L45.find('\n\n', _L45.find('Se você soltar o símbolo', _ic45))] if _ic45 >= 0 else ''
_na = {'peca 11, a caixa da Cesta': 'a Expansão te alcança na hora, ' + _EXTRA in _cxc,
       'livro, a caixa da Cesta': 'Quando ela cai, a Expansão te alcança na hora, ' + _EXTRA in _cxc45,
       'livro, o Simples que cai pelo voto': 'Se ele cair pelo voto, no meio da rodada, a Expansão alcança na hora, ' + _EXTRA in _L45,
       'peca 11, a regra das quatro': bool(re.search(r'\*\*Quando uma delas cai e a Expansão te alcança na hora, esse Acerto é a mais:\*\*', _P11_10))}
if not all(_na.values()):
    erro(f'a queda na hora deixou de dizer que o Acerto e a mais em {[k for k, v in _na.items() if not v]} — '
         'sem a frase, o texto le dos dois jeitos, e com dois golpes por rodada as leituras divergem')
else:
    print('  A queda na hora: o Acerto e a mais, e o do comeco do turno do dono continua vindo — na caixa da Cesta')
    print('  na peca e no livro, no Simples que cai pelo voto e na regra das quatro.')

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

# --- a escada de upkeep segue a escada de Classe, NIVEL A NIVEL: o que a Classe menor
# cobra nunca passa do que a Classe maior cobra. v0.268: com o custo fixo, a comparacao
# por multiplicador deixou de dizer alguma coisa, e ela passou a ser feita em PE.
_ruim_escada = []
for nv in range(10, 31):
    por_cl = {}
    for nome in ANTIDOMINIO:
        por_cl.setdefault(ANTIDOMINIO[nome][0], []).append(custo_rodada(nome, nv))
    cls = sorted(por_cl)
    for a_, b_ in zip(cls, cls[1:]):
        if max(por_cl[a_]) > min(por_cl[b_]):
            _ruim_escada.append((nv, a_, b_))
if _ruim_escada:
    erro(f'o custo por rodada nao cresce junto com a Classe: nv, Classe menor, Classe maior = '
         f'{_ruim_escada[:4]} — uma Classe menor esta custando mais PE que uma maior')
else:
    print('\n  O custo por rodada nao decresce com a Classe, em nenhum nivel do 10 ao 30: ' +
          ' · '.join(f'{n} {custo_rodada(n, 30):g}' for n in ANTIDOMINIO) + ' no nivel 30.')
    print('  A Cesta Oca e a unica que nao custa PE de pe: desde a v0.267 o preco dela sao')
    print('  as maos presas no simbolo e a queda pelos golpes em quem segura, e desde a v0.272')
    print('  erguer custa a maior Classe, como nas outras duas.')


# --------------------------------------------------------------------------
bloco('11. A DISPUTA DE DOMINIOS — a cascata do R41, e o unico numero e o desempate')

# v0.351. Ate a v0.350 os blocos 11, 11.1, 11.2 e 12 liam o gerador do manual v7 (partE.js),
# que era o dono, e o capitulo 9 do livro v0.331, que era a copia, e cobravam que os dois
# concordassem. Os dois estao congelados desde a v0.337 e divergem do livro final nas regras
# que a revisao do Mizuki mudou; o dono da Expansao e' o R41, e e' ele que estes blocos leem.
# Saiu sem substituto, porque o R41 nao tem o que conferir: a caixa "REFINO, EM UMA LINHA" do
# manual, a comparacao manual x livro (hoje ha um documento so) e a tabela "Raio do dominio"
# do livro v0.331 (o R41 publica a formula, e nao a tabela).
import livro as _livro11
try:
    _POD = _livro11.texto('poderes')
except _livro11.LivroMudou as _e11:
    _POD = ''
    erro(f'11: nao li o capitulo de Poderes avancados do R41 — {_e11}')


def _pagina11(titulo):
    """O texto de uma pagina do capitulo: do titulo `# ` ate o proximo `# `."""
    m = re.search(r'^# ' + re.escape(titulo) + r'[ \t]*$', _POD, re.M)
    if not m:
        erro(f'11: o capitulo de Poderes avancados do R41 nao tem a pagina "{titulo}" — o '
             'titulo mudou, e o que este validador confere nela parou de ser conferido')
        return ''
    f = re.search(r'^# ', _POD[m.end():], re.M)
    return _POD[m.end(): m.end() + f.start()] if f else _POD[m.end():]


_DEGR = _pagina11('Expansão de Domínio')
_ABRE = _pagina11('Abrir e manter')
_SEMB = _pagina11('Expansão sem Barreiras')
_DISP = _pagina11('Disputa de domínios')
_MANT = _pagina11('Manter uma disputa')
_SOBR = _pagina11('Áreas sobrepostas')
_VARI = _pagina11('Vários domínios')

PALAVRA_N = {'um': 1, 'uma': 1, 'dois': 2, 'duas': 2, 'tres': 3, 'três': 3, 'quatro': 4}
FORMAS = [(r'\d+\s*d\s*\d+', 'notacao de dado'),
          (r'\d+\s*%', 'porcentagem'),
          (r'\d+\s*(?:rodadas?|PE|metros?)\b', 'custo ou prazo')]

if _DISP:
    # --- a cascata: contagem, numeracao, e quem decide cada degrau ---------------
    _linhas = re.findall(r'(?m)^\|\s*(\d)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*$', _DISP)
    print(f'  a cascata da disputa tem {len(_linhas)} pergunta(s)')
    # Nenhuma destas ancoras carrega o valor que confere: sao os nomes das quatro coisas
    # que decidem, na ordem. A linha tem de casar com a sua ancora e com nenhuma outra,
    # senao uma troca de ordem entre duas passaria calada.
    DEGRAU = [('o refino', r'Refino diferente'),
              ('o Acerto sem dano', r'Acerto sem dano'),
              ('o dado do desempate', r'\d+d\d+'),
              ('a corrida', r'disputa continua')]
    if len(_linhas) != len(DEGRAU):
        erro(f'11: a cascata da disputa rendeu {len(_linhas)} pergunta(s) e sao '
             f'{len(DEGRAU)} — extrator que para de achar nao confere nada')
    elif [n for n, _, _ in _linhas] != [str(i) for i in range(1, len(_linhas) + 1)]:
        erro(f'11: a numeracao da cascata tem buraco: {[n for n, _, _ in _linhas]}')
    else:
        _ruim = []
        for (_n, _p, _q), (_nome, _rx) in zip(_linhas, DEGRAU):
            _casou = [nm for nm, rx in DEGRAU if re.search(rx, f'{_p} {_q}')]
            if _casou != [_nome]:
                _ruim.append(f'a pergunta {_n} devia decidir por {_nome} e casa com '
                             f'{_casou or "nada"}')
        for _r in _ruim:
            erro(f'11: {_r}. A ordem da cascata e a regra')
        if not _ruim:
            print(f'  [x] a cascata esta numerada sem buraco, e os {len(DEGRAU)} degraus '
                  'decidem, na ordem, por: ' + ' · '.join(n for n, _ in DEGRAU) + '.')

    # --- o desempate: o dado, a margem, e a faixa que sobra para a corrida -------
    # Os valores NAO estao escritos aqui: sao lidos do R41. O que este bloco sabe e' a
    # forma, e que a pergunta 4 tem de cobrir exatamente o que a 3 nao decide.
    _dado = re.search(r'(\d+d\d+)', _DISP)
    _marg = re.search(r'diferença de (\d+) ou mais', _DISP)
    _faixa = re.search(r'Diferença de (\d+) a (\d+) no d\d+', _DISP)
    if not (_dado and _marg and _faixa):
        erro('11: nao achei o dado do desempate, a margem dele e a faixa da pergunta 4 na '
             'pagina da disputa — sem os tres a checagem abaixo passaria vazia')
    else:
        print(f'  o desempate publicado no R41: {_dado.group(1)}, margem {_marg.group(1)}; '
              f'a corrida cobre de {_faixa.group(1)} a {_faixa.group(2)}')
        if (int(_faixa.group(1)), int(_faixa.group(2))) != (0, int(_marg.group(1)) - 1):
            erro(f'11: a pergunta 3 decide com {_marg.group(1)} ou mais e a 4 cobre de '
                 f'{_faixa.group(1)} a {_faixa.group(2)} — entre as duas sobra buraco ou '
                 'sobreposicao')
        else:
            print('  [x] a pergunta 4 cobre exatamente o que a 3 nao decide.')

    # --- e a pagina tem esse numero, e so ele -----------------------------------
    _permitido = {_dado.group(1) if _dado else None}
    _achados = [f'{_nome}: "{_m2.group(0)}"'
                for _rx, _nome in FORMAS
                for _m2 in re.finditer(_rx, _DISP)
                if _m2.group(0).replace(' ', '') not in _permitido]
    if _achados:
        for _a in _achados:
            erro(f'11: a pagina da disputa escreveu numero que nao e o desempate — {_a}. '
                 'Fora do dado e da margem ela e toda derivada: cascata de refino, tipo de '
                 'Acerto e corrida sobre estado ja publicado')
    else:
        print('  [x] fora do desempate a pagina nao escreve dado, porcentagem nem prazo.')


# --------------------------------------------------------------------------
bloco('11.1. AS SAIDAS DA DISPUTA — as oito estao no R41')

# v0.200: este pedaco nasceu de uma falha real — a copia do livro levou a cascata e esqueceu
# a caixa dos tres dominios, e o bloco saiu verde porque so olhava a ordem das perguntas.
# v0.351: a comparacao entre duas copias acabou, e a pergunta ficou: o livro final traz as
# oito saidas que a regra tem? Nenhuma ancora carrega valor: sao os NOMES das saidas.
_DISPUTA_TODA = '\n'.join((_DISP, _MANT, _SOBR, _VARI))
SAIDAS = {
    'a sobreposicao':             r'sobrep',
    'os Acertos suspensos':       r'Acertos ficam suspensos',
    'a corrida':                  r'\*\*corrida\*\*',
    'o perdedor recebe':          r'Acerto do vencedor',
    'o Rescaldo dos donos':       r'entram em Rescaldo',
    'a incompleta que nao vence': r'não vence a disputa',
    'tres ou mais barreiras':     r'três ou mais',
    'a Concentracao fica livre':  r'não ocupam sua Concentração',
}
if _DISP and _MANT and _SOBR and _VARI:
    _falta11 = [n for n, rx in SAIDAS.items() if not re.search(rx, _DISPUTA_TODA)]
    for _n in _falta11:
        erro(f'11.1: o R41 nao escreve "{_n}" nas paginas da disputa — o jogador fica sem '
             'uma saida que a regra tem')
    if not _falta11:
        print(f'  [x] as {len(SAIDAS)} saidas da regra estao nas paginas da disputa.')


# --------------------------------------------------------------------------
bloco('11.2. O TESTE DE VIGOR NA CORRIDA — a regra no R41, e a tabela sai da conta')
# --------------------------------------------------------------------------
# v0.225. Decisao do Mizuki em 13/09: na corrida, quem mantem um dominio testa Vigor; o
# jogador testa a cada dano, o inimigo no maximo uma vez por jogador por rodada; as falhas
# acumulam, e o dominio cai quando elas chegam a uma fracao da Essencia. v0.253 (19/09): a CD
# e' a de quem feriu, e a frase antiga ("CD do dono do outro dominio") fica PROIBIDA.
# v0.351: a regra e' lida do R41, com a redacao dele.
#
# Tres coisas separadas, porque cada uma pode quebrar sozinha:
#   a) as oito pecas da regra estao na pagina "Manter uma disputa"
#   b) a FRACAO e o ARREDONDAMENTO sao os da peca 1 §5.4
#   c) a tabela sai da conta, celula a celula, e cobre a escala inteira de Essencia, com o
#      teto lido da peca 2
_AQ = os.path.dirname(os.path.abspath(__file__))
_P1 = open(os.path.join(_AQ, '01-atributos-acerto-defesa.md'), encoding='utf-8').read()
_P2 = open(os.path.join(_AQ, '02-economia-de-atributos.md'), encoding='utf-8').read()
_mant = _MANT.replace('**', '')

PECAS = {
    'o teste':                   r'TR de Vigor contra a CD de quem causou o dano',
    'a maior CD':                r'contra a maior CD entre eles',
    'a contagem de falhas':      r'ao atingir (metade|um terço|um quarto) da sua Essência em falhas',
    'o jogador, sem limite':     r'testa a cada aplicação de dano recebido, sem limite por rodada',
    'o inimigo, um por jogador': r'no máximo um teste por personagem de jogador que o acertou na rodada',
    'nao ocupa a Concentracao':  r'Esses testes não ocupam sua Concentração',
    'beneficio de Concentracao nao protege': r'Benefícios destinados apenas à Concentração não se aplicam',
    'a invocacao nao conta':     r'Dano de invocação reduz vida, mas não provoca esse teste',
}
if _MANT:
    _falta = [n for n, rx in PECAS.items() if not re.search(rx, _mant)]
    for _f in _falta:
        erro(f'11.2: "{_f}" nao esta na pagina "Manter uma disputa" do R41')
    if not _falta:
        print(f'  [x] as {len(PECAS)} pecas da regra estao no R41.')

    if re.search(r'CD do dono do outro domínio', _DISPUTA_TODA.replace('**', '')):
        erro('11.2: o R41 diz "CD do dono do outro dominio" — a decisao de 19/09/2026 passou '
             'a CD da corrida para a de quem te feriu (peca 3 §3)')
    else:
        print('  [x] a CD do dono do outro dominio nao aparece no R41.')

    # b) a fracao e o arredondamento
    FRAC = {'metade': 2, 'um terço': 3, 'um quarto': 4}
    _fm = re.search(PECAS['a contagem de falhas'] +
                    r', arredondada para (baixo|cima), no mínimo (\w+)', _mant)
    _regra_p1 = re.search(r'O que você \*\*ganha\*\* desce\. E o que você ganha nunca fica abaixo de (\d+)\.', _P1)
    _teto = re.search(r'\*\*Teto do atributo: (\d+)\.\*\*', _P2)
    if not (_fm and _regra_p1 and _teto) or _fm.group(3) not in PALAVRA_N:
        erro('11.2: nao li a fracao e o arredondamento no R41, a regra de arredondamento da '
             'peca 1 §5.4, ou o teto de atributo da peca 2 — sem os tres a tabela nao tem '
             'contra o que conferir')
    else:
        _div = FRAC[_fm.group(1)]
        _piso = int(_regra_p1.group(1))
        if _fm.group(2) != 'baixo':
            erro(f'11.2: o R41 arredonda as falhas para {_fm.group(2)}, e a peca 1 §5.4 manda '
                 'o que voce ganha descer')
        if PALAVRA_N[_fm.group(3)] != _piso:
            erro(f'11.2: o R41 escreve "no minimo {_fm.group(3)}" e a peca 1 §5.4 manda o '
                 f'ganho nunca ficar abaixo de {_piso}')
        print(f'  a fracao do R41: 1/{_div} da Essencia · o piso da peca 1: {_piso} '
              f'· o teto de atributo da peca 2: {_teto.group(1)}')

        # c) a tabela, celula a celula
        _mt = re.search(r'\| Essência \| Falhas que encerram o domínio \|\n\|[-| :]+\|\n((?:\|[^\n]*\|\n?)+)', _MANT)
        if not _mt:
            erro('11.2: o R41 perdeu a tabela "Falhas que encerram o dominio" — o jogador '
                 'fica sem a conta pronta')
        else:
            _vistos, _ruim = [], []
            for _c, _v in re.findall(r'\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|', _mt.group(1)):
                _r = re.fullmatch(r'(\d+)(?: (?:a|e|ou) (\d+))?', _c)
                if not _r or not _v.isdigit():
                    _ruim.append(f'a celula "{_c}" -> "{_v}" nao e lida como faixa de Essencia')
                    continue
                _a, _b = int(_r.group(1)), int(_r.group(2) or _r.group(1))
                for _e in range(_a, _b + 1):
                    _vistos.append(_e)
                    _quer = max(_piso, _e // _div)
                    if int(_v) != _quer:
                        _ruim.append(f'Essencia {_e}: o R41 publica {_v} falha(s) e a '
                                     f'conta da {_quer}')
            _esc = list(range(0, int(_teto.group(1)) + 1))
            if sorted(_vistos) != _esc:
                _ruim.append(f'a tabela cobre as Essencias {sorted(_vistos)} e a escala e {_esc}')
            for _r in _ruim:
                erro(f'11.2: {_r}')
            if not _ruim:
                print(f'  [x] a tabela do R41 cobre a Essencia de 0 a {_teto.group(1)} e cada '
                      f'celula e a conta: 1/{_div}, para baixo, nunca menos de {_piso}.')


# --------------------------------------------------------------------------
bloco('12. A EXPANSAO SEM BARREIRAS — o degrau de cima, e o raio de todos')
# --------------------------------------------------------------------------
# v0.226. O degrau entrou depois de tres rodadas com o Mizuki; o rascunho e' o
# RASCUNHO-expansao-sem-barreira.md, e a secao 9 dele e' a especificacao. Nenhum valor mora
# aqui: cada numero e' LIDO do R41 (v0.351; ate a v0.350, do manual v7 e do livro v0.331), e
# o que tem dono fora da Expansao (teto de refino, maestria por nivel, a pericia, o Dominio
# Simples) e' lido do dono.
#
# ⚠ ESTE DEGRAU QUEBRA O INVARIANTE 3 DE PROPOSITO. O generalista termina com refino 8 e
# nunca chega nele — "so dois conseguem, e eram outro patamar". A checagem 12.2 cobra que a
# exclusao seja EXATAMENTE a declarada: generalista fora, as outras duas rotas dentro.
_AQ12 = os.path.dirname(os.path.abspath(__file__))
_P2_12 = open(os.path.join(_AQ12, '02-economia-de-atributos.md'), encoding='utf-8').read()
_P7_12 = open(os.path.join(_AQ12, '07-pericias-e-oficios.md'), encoding='utf-8').read()
_P11_12 = open(os.path.join(_AQ12, '11-aptidoes-e-refino.md'), encoding='utf-8').read()
_P18_12 = open(os.path.join(_AQ12, '18-progressao.md'), encoding='utf-8').read()


def _dec12(s):
    return float(s.replace(',', '.'))


def _fmt_m(x):
    return (f'{x:.1f}'.rstrip('0').rstrip('.')).replace('.', ',') + ' m'


_ruim12 = []
if not (_DEGR and _ABRE and _SEMB):
    erro('12: sem as paginas dos degraus, de abrir e da Expansao sem Barreiras do R41, o '
         'degrau de cima nao foi conferido')
else:
    # 12.1 o preco em espacos ---------------------------------------------------
    _tot = {n: (int(e), req) for n, e, req in
            re.findall(r'(?m)^\| (Incompleta|Completa|Sem Barreiras) \| (\d+) \| ([^|]+?) \|', _DEGR)}
    _mais_c = re.search(r'gasta \*\*mais (\w+) espaço\*\* para adquirir Completa', _DEGR)
    _mais_s = re.search(r'gasta \*\*mais (\w+)\*\* para adquirir Sem Barreiras', _DEGR)
    _gs = re.search(r'Completa, refino (\d+) e especialização em (\w+)',
                    _tot.get('Sem Barreiras', (0, ''))[1])
    if len(_tot) != 3 or not (_mais_c and _mais_s and _gs) \
            or _mais_c.group(1) not in PALAVRA_N or _mais_s.group(1) not in PALAVRA_N:
        erro('12.1: nao li os tres degraus na tabela do R41, as duas frases de "mais N '
             'espacos" ou o requisito da Sem Barreiras')
        _gs = None
    else:
        tot_i, tot_c, tot_s = (_tot[n][0] for n in ('Incompleta', 'Completa', 'Sem Barreiras'))
        dif_c, dif_s = PALAVRA_N[_mais_c.group(1)], PALAVRA_N[_mais_s.group(1)]
        if tot_c - tot_i != dif_c:
            _ruim12.append(f'12.1: a Completa custa {tot_c} espacos, a Incompleta {tot_i}, e o '
                           f'texto diz "mais {_mais_c.group(1)}" — a diferenca escrita nao e a conta')
        if tot_s - tot_c != dif_s:
            _ruim12.append(f'12.1: a Sem Barreiras custa {tot_s} espacos, a Completa {tot_c}, e o '
                           f'texto diz "mais {_mais_s.group(1)}" — a diferenca escrita nao e a conta')
        print(f'  o degrau: {tot_s} espacos (+{dif_s} sobre a Completa de {tot_c}), refino '
              f'{_gs.group(1)} e especializacao em {_gs.group(2)}')

        # 12.2 o gate ---------------------------------------------------------
        _teto = re.search(r'\*\*Teto do atributo: \d+\.\*\* Teto do refino: (\d+)\.', _P2_12)
        _per = _gs.group(2)
        _cobre = re.search(r'^\*\*' + re.escape(_per) + r'\*\* — [^\n]*\bbarreiras\b', _P7_12, re.M)
        if not _teto:
            _ruim12.append('12.2: nao li o teto de refino na peca 2')
        elif int(_gs.group(1)) != int(_teto.group(1)):
            _ruim12.append(f'12.2: o degrau pede refino {_gs.group(1)} e o teto da peca 2 e '
                           f'{_teto.group(1)} — a decisao foi o refino no teto')
        if not _cobre:
            _ruim12.append(f'12.2: a pericia do gate e "{_per}", e a peca 7 nao diz que ela cobre '
                           f'barreiras — o gate e pericia de barreira, como na obra')
        if _teto:
            _rg = int(_teto.group(1))
            _chega = {rota: next((m for m, r in zip(MARCOS, CURVA[rota]) if r >= _rg), None)
                      for rota in CURVA}
            _fora = {r for r, v in _chega.items() if v is None}
            print('  refino ' + str(_rg) + ' chega em: ' +
                  ' · '.join(f'{r} nv{v}' if v else f'{r} NUNCA' for r, v in _chega.items()))
            if _fora != {'generalista'}:
                _ruim12.append(f'12.2: o gate deixa de fora {sorted(_fora) or "ninguem"}, e a exclusao '
                               f'declarada e so o generalista')

    # 12.3 o custo de abrir sem barreira, e o desconto -----------------------
    _ab = re.search(r'(?m)^\| Aberto \| (\d+) × maior Classe em PE \| ([\d,]+) m \| (\d+) × Maestria \|', _ABRE)
    _mae = {int(a): int(b) for a, b in re.findall(r'^\| \*{0,2}(\d+)\*{0,2} \| [\d.—]+ \| (\d+) \|', _P18_12, re.M)}
    if not _ab or len(_mae) != 30:
        erro('12.3: nao li a linha "Aberto" da tabela "Abrir e manter" do R41, ou a coluna de '
             'maestria da peca 18')
    else:
        k_abrir, k_desc = int(_ab.group(1)), int(_ab.group(3))
        if k_abrir <= PE_ABRIR['completa']:
            _ruim12.append(f'12.3: abrir sem barreira custa {k_abrir} x e a Completa {PE_ABRIR["completa"]} x '
                           f'— o degrau de cima ficou mais barato de abrir')
        dur = duracao(TETO_REFINO)
        print(f'  sem barreira: abrir {k_abrir} x a maior Classe, desconto {k_desc} x maestria, '
              f'{dur} rodadas no refino {TETO_REFINO}')
        for nv in (22, 26, 30):
            abrir = k_abrir * maior_classe(nv)
            poupa = dur * k_desc * _mae[nv]
            print(f'    nv{nv}: abrir {abrir} · o desconto devolve no maximo {poupa} · saldo {poupa - abrir:+d}')
            if poupa >= abrir:
                _ruim12.append(f'12.3: no nv{nv} o desconto devolve {poupa} e abrir custa {abrir} — '
                               f'abrir sem barreira virou lucro')
        # o exemplo da pagina e' a testemunha: ele da' o nivel, a Classe, a maestria e o
        # refino, e escreve as quatro contas. Cada uma e' refeita com os numeros da tabela.
        _ex = re.search(r'No nível (\d+), maior Classe (\d+), Maestria (\d+) e refino (\d+), abrir custa '
                        r'(\d+) PE\. Um feitiço de Classe \d+ custa \d+ − (\d+) = \*\*\d+ PE\*\*\. '
                        r'Escolhendo o modo fechado, a abertura custaria (\d+) PE e esse feitiço '
                        r'custaria \d+ − (\d+) = ', _SEMB)
        if not _ex:
            _ruim12.append('12.3: nao li o exemplo da pagina "Expansao sem Barreiras" do R41')
        else:
            _nv, _cl, _ma, _rf, _ca, _da, _cf, _df = (int(x) for x in _ex.groups())
            _quer = (maior_classe(_nv), _mae.get(_nv), k_abrir * _cl, k_desc * _ma,
                     PE_ABRIR['completa'] * _cl, _rf // DESCONTO_DIVISOR['completa'])
            _tem = (_cl, _ma, _ca, _da, _cf, _df)
            if _quer != _tem:
                _ruim12.append(f'12.3: o exemplo do R41 escreve (Classe, maestria, abrir aberto, '
                               f'desconto aberto, abrir fechado, desconto fechado) = {_tem} e a '
                               f'conta com as tabelas da {_quer}')
            else:
                print(f'  [x] o exemplo do R41 (nv{_nv}) sai das tabelas: abrir {_ca} e desconto '
                      f'{_da} no aberto; abrir {_cf} e desconto {_df} no fechado.')

    # 12.4 o raio do dominio fechado ------------------------------------------
    _ri = re.search(r'(?m)^\| Incompleta \| [^|]+\| ([\d,]+) m × refino, até ([\d,]+) m \|', _ABRE)
    _rc = re.search(r'(?m)^\| Completa ou fechado \| [^|]+\| ([\d,]+) m × refino \|', _ABRE)
    passo = None
    if not (_ri and _rc):
        erro('12.4: nao li o raio da Incompleta e o da Completa na tabela "Abrir e manter" do R41')
    else:
        passo, teto_inc = _dec12(_rc.group(1)), _dec12(_ri.group(2))
        if _dec12(_ri.group(1)) != passo:
            _ruim12.append(f'12.4: a Incompleta cresce {_ri.group(1)} m por refino e a Completa '
                           f'{_rc.group(1)} m — o passo do raio tem de ser um so')
        if teto_inc < passo * GATE['incompleta'][1]:
            _ruim12.append(f'12.4: a Incompleta para em {_fmt_m(teto_inc)}, abaixo do raio que ela '
                           f'ja tem no refino do gate ({_fmt_m(passo * GATE["incompleta"][1])})')
        print(f'  o raio: {_fmt_m(passo)} x refino, a incompleta ate {_fmt_m(teto_inc)}')
        _ds = re.search(r'raio `(\d+),(\d+) m \+ refino ÷ (\d+)`', _P11_12)
        if _ds:
            maior_ds = float(f'{_ds.group(1)}.{_ds.group(2)}') + TETO_REFINO / int(_ds.group(3))
            menor_c = passo * GATE['completa'][1]
            if maior_ds >= menor_c:
                aviso(f'12.4: o maior Dominio Simples ({_fmt_m(maior_ds)}) ja cobre a menor Completa '
                      f'({_fmt_m(menor_c)}) — a revisao dos anti-dominio precisa olhar isto')

    # 12.5 o raio sem barreira ------------------------------------------------
    _txt5 = re.search(r'área de \*\*([\d,]+) m de raio\*\*, com centro fixo no ponto da abertura', _SEMB)
    if not (_ab and _txt5):
        _ruim12.append('12.5: nao li o raio do modo aberto na tabela e no texto do R41')
    else:
        if _ab.group(2) != _txt5.group(1):
            _ruim12.append(f'12.5: o raio aberto e {_ab.group(2)} m na tabela e {_txt5.group(1)} m '
                           'no texto da pagina')
        if passo is not None and _dec12(_ab.group(2)) <= passo * TETO_REFINO:
            _ruim12.append('12.5: o raio sem barreira nao passa do maior dominio fechado')
        print(f'  o raio aberto: {_ab.group(2)} m, contra {_fmt_m((passo or 0) * TETO_REFINO)} do '
              'maior dominio fechado')

    # 12.6 as pecas de texto ----------------------------------------------------
    _tudo12 = '\n'.join((_DEGR, _SEMB, _SOBR, _VARI)).replace('**', '')
    PECAS12 = {
        'nao prende':                 r'Não há uma parede prendendo os ocupantes',
        'nao tem borda':              r'não tem uma barreira exterior que possa ser destruída',
        'quem nao tem energia':       r'alcança alguém sem energia amaldiçoada',
        'o Acerto continua fora':     r'O Acerto do modo aberto continua funcionando fora da área fechada',
        'bate na barreira por fora':  r'atinge a barreira rival pelo lado de fora',
        'o Acerto que nao fere':      r'Acerto sem dano não reduz a vida da barreira',
        'a incompleta so no raio':    r'suspende o Acerto garantido somente dentro do próprio raio',
        'fora dos tres ou mais':      r'Um domínio aberto e uma Incompleta não contam como barreiras',
        'fechar e a completa':        r'Abrir fechado conserva todas as regras da Completa',
    }
    for nome, rx in PECAS12.items():
        if not re.search(rx, _tudo12):
            _ruim12.append(f'12.6: "{nome}" nao esta no R41')
    try:
        _indice12 = _livro11.texto('consulta')
    except _livro11.LivroMudou:
        _indice12 = ''
    if '[Expansão sem Barreiras](#' not in _indice12:
        _ruim12.append('12.6: o indice de consulta do R41 nao tem a entrada "Expansao sem Barreiras"')

    for r in _ruim12:
        erro(r)
    if not _ruim12:
        print('  [x] o degrau, o gate, o custo, o exemplo, o raio dos dois lados e as pecas de '
              'texto batem entre o R41 e os donos.')

# --- 12.7: o R41 contra o modelo deste validador (v0.349) ------------------------
# Este arquivo mede a Expansao com constantes (GATE, PRECO, PE_ABRIR, os dois
# divisores, BARREIRA_FATOR) e confere o texto contra o gerador do manual v7 e o livro
# v0.331, que estao congelados. O livro principal desde a v0.341 e' o R41, e ate a
# v0.348 ninguem perguntava se ele publica os mesmos numeros que o modelo usa.
# Esta sub-checagem pergunta, e pergunta tambem pelas regras que a revisao do Mizuki
# de 07 a 09/10/2026 fechou no capitulo de Poderes avancados (itens 1 a 14, 152 e 153
# do MUDANCAS-DE-REGRA.md do R41). A Expansao nao tem peca: o dono e' o livro. Entao
# a testemunha de cada decisao e' a frase do R41, e a frase que a decisao TIROU nao
# pode voltar.
print()
print('  12.7: o R41 publica o que este validador mede, e as decisoes da revisao')
import livro as _livro127
try:
    _pod127 = _livro127.limpa(_livro127.texto('poderes'))
except _livro127.LivroMudou as _e127:
    _pod127 = ''
    erro(f'12.7: nao li o capitulo de Poderes avancados do R41 — {_e127}')
if _pod127:
    _antes127 = len(ERROS)
    # a) a tabela dos degraus: espacos e gate
    for _deg, _rot in (('incompleta', 'Incompleta'), ('completa', 'Completa')):
        _m = re.search(r'\| %s \| (\d+) \| [^|]*?[Nn]ível (\d+) e refino (\d+) \|' % _rot, _pod127)
        if not _m:
            erro(f'12.7: nao achei a linha "{_rot}" na tabela de degraus do R41')
        elif (int(_m.group(1)), (int(_m.group(2)), int(_m.group(3)))) != (PRECO[_deg], GATE[_deg]):
            erro(f'12.7: o R41 publica a {_rot} com {_m.group(1)} espacos, nivel {_m.group(2)} e '
                 f'refino {_m.group(3)}, e o modelo usa {PRECO[_deg]} espacos e o gate {GATE[_deg]}')
    # b) a tabela de abrir: PE, raio e desconto
    for _deg, _rot in (('incompleta', 'Incompleta'), ('completa', 'Completa ou fechado')):
        _m = re.search(r'\| %s \| (\d+) × maior Classe em PE \| 1,5 m × refino[^|]*\| Refino ÷ (\d+), para baixo \|' % _rot, _pod127)
        if not _m:
            erro(f'12.7: nao achei a linha "{_rot}" na tabela de abertura do R41')
        elif (int(_m.group(1)), int(_m.group(2))) != (PE_ABRIR[_deg], DESCONTO_DIVISOR[_deg]):
            erro(f'12.7: o R41 abre a {_rot} por {_m.group(1)} × a maior Classe e desconta refino ÷ '
                 f'{_m.group(2)}, e o modelo usa {PE_ABRIR[_deg]} × e ÷ {DESCONTO_DIVISOR[_deg]}')
    # c) a duracao e a barreira
    if DURACAO_DIVISOR != 2 or 'conte metade do refino, arredondada para baixo, em turnos seus' not in _pod127:
        erro('12.7: a duracao do R41 ("conte metade do refino... em turnos seus") e o divisor do '
             f'modelo ({DURACAO_DIVISOR}) deixaram de dizer a mesma coisa')
    _m = re.search(r'a barreira possui (\d+) × metade do refino em pontos de vida', _pod127)
    if not _m or int(_m.group(1)) != BARREIRA_FATOR:
        erro(f'12.7: o R41 da a barreira {_m.group(1) if _m else "?"} × metade do refino de vida, e o '
             f'modelo usa {BARREIRA_FATOR}')
    # d) as decisoes da revisao: a frase que vale, e a que saiu
    _VALE127 = [
        ('1, o Acerto de dano montado como feitico',
         'são 3 × sua maior Classe em pontos, menos o preço Médio dessa Melhoria'),
        ('2, poupar alguem do Acerto', 'Poupar alguém só é possível se o Efeito do domínio disser como'),
        ('3, a Incompleta por rolagem', 'O Acerto da Incompleta resolve por rolagem, como um feitiço'),
        ('4, o Acerto garantido contra as defesas',
         'O Acerto garantido ignora Redução de Dano, resistência e imunidade'),
        ('4, o Acerto garantido sem critico', 'o Acerto não produz crítico'),
        ('5, a regra de ambiente e o dono', 'Ela não vale contra você'),
        ('8, a barreira por dentro', 'Por dentro, a barreira não quebra'),
        ('11, o Rescaldo',
         'Quando seu domínio termina, você entra em Rescaldo pelo restante da cena. Não pode usar a Técnica Inata, salvo seus feitiços de Classe 0'),
        ('13, manter a disputa', 'contra a maior CD entre eles'),
        ('14, passar no TR', 'quem passa no TR recebe metade do resultado do dano'),
        ('152, tres ou mais barreiras',
         'Enquanto houver três ou mais barreiras, o refino não decide'),
        ('152, o intruso', 'Um intruso de nível menor entra sem derrubar nada'),
        ('153, duas barreiras e uma aberta', 'o domínio aberto ataca as duas por fora'),
        # o raio do modo aberto: 199,5 m e' decisao do Mizuki (133 quadrados de 1,5 m); o
        # gerador do manual v7 e o livro v0.331, congelados, dizem 200 m, e o bloco 12 os le
        ('178, o raio do modo aberto', '| Aberto | 7 × maior Classe em PE | 199,5 m | 2 × Maestria |'),
    ]
    _SAIU127 = [
        ('1, o valor fixo do Acerto', '2 × sua maior Classe em d8'),
        ('8, o dano por dentro dividido', 'dividido por quatro'),
        ('13, o primeiro total', 'Conserve o total obtido no primeiro teste'),
        ('153, o aberto disputando', 'O domínio aberto disputa com elas'),
    ]
    for _rot, _fr in _VALE127:
        if _fr not in _pod127:
            erro(f'12.7: o R41 nao escreve mais a decisao do item {_rot}: falta "{_fr}"')
    for _rot, _fr in _SAIU127:
        if _fr in _pod127:
            erro(f'12.7: o R41 voltou a trazer o que a revisao tirou (item {_rot}): "{_fr}"')
    if len(ERROS) == _antes127:
        print('  [x] degraus, custo de abrir, desconto, duracao e barreira do R41 sao os do modelo')
        print(f'  [x] as {len(_VALE127)} frases das decisoes estao no R41, e as {len(_SAIU127)} que '
              'sairam nao voltaram')

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

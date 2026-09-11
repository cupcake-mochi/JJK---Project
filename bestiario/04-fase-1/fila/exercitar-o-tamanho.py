#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
O EIXO DO `tamanho`, EXERCITADO — item 16 da fila.

O Sukuna e `Médio`, o unico degrau que nao carrega numero. `Grande`, `Imenso` e
`Colossal` nunca passaram pela maquina — e o `ACHADOS-o-teste-de-ponta-a-ponta`
registrou isso como o que o teste NAO achou.

A `MEDIDA-o-tamanho` fechou a troca com a Defesa do nivel 30 (`20` de base).
Este script roda os quatro degraus em TODOS os niveis, e cruza com a formula que
constroi a Defesa — `10 + Destreza + proteção`.

Nenhum numero mora aqui: cada ancora e lida do documento dono.
"""
import os
import re
import sys

BEST = os.environ.get('JJK_BEST', '/media/mizuki/HD Externo II/Claude/Claude 2/bestiario')

TABELA = '04-fase-1/TABELA.md'
TAMANHO = '04-fase-1/fila/MEDIDA-o-tamanho.md'
ANCORAS = '05-sukuna/ANCORAS-do-repositorio.md'
ACHADOS = '05-sukuna/ACHADOS-o-teste-de-ponta-a-ponta.md'
BLOCO = '03-bloco/RASCUNHO-5-o-bloco-em-branco.md'

_cache = {}


def ler(rel):
    if rel not in _cache:
        with open(os.path.join(BEST, rel), encoding='utf-8') as f:
            _cache[rel] = f.read()
    return _cache[rel]


def n(s):
    return float(s.replace('−', '-').replace(',', '.'))


def pega(rel, padrao, rotulo):
    m = re.search(padrao, ler(rel))
    if not m:
        print(f'\n  !! ANCORA PERDIDA: {rotulo}\n     nao casa em {rel}\n     padrao: {padrao}')
        sys.exit(1)
    return m


def bloco(t):
    print()
    print('=' * 96)
    print(t)
    print('=' * 96)


# ------------------------------------------------------------------ as ancoras
# a formula da Defesa
FORM = pega(ANCORAS, r'\| \*\*Defesa\*\* \| `10 \+ Destreza \+ proteção` \| (peça 1 §\d+) \|',
            'a fórmula da Defesa').group(1)
# o orcamento de atributo: piso 0, porque os pontos se COMPRAM
ORC = pega(ANCORAS, r'no mesmo orçamento de uma ficha\*\* — (nove) pontos na criação, teto `(\d)` '
                    r'ali, `\+1` por marco e teto `(\d)`', 'o orçamento de atributo')
TETO_CRIACAO, TETO_TOTAL = int(ORC.group(2)), int(ORC.group(3))
PISO_ATRIB = 0      # nao e ancora: e o piso de um orcamento que se COMPRA

# a tabela do tamanho
TAM = {}
for ln in ler(TAMANHO).split('\n'):
    m = re.match(r'\| \*\*`(\w+)`\*\* \| `([\d,]+) m` \| ([^|]+) \| `([\d,]+)×` \| '
                 r'`(\d+)` \*\(`([+−]\d+)`\)\* \| \*\*`([\d,]+)×`\*\* \|$', ln)
    if m:
        TAM[m.group(1)] = {'alcance': n(m.group(2)), 'pega': m.group(3).strip(),
                           'ganho': n(m.group(4)), 'defesa_ref': int(m.group(5)),
                           'delta': int(n(m.group(6))), 'produto': n(m.group(7))}
if len(TAM) < 4:
    print(f'  !! ANCORA PERDIDA: a tabela do tamanho — li {sorted(TAM)}')
    sys.exit(1)
ORDEM_T = ['Médio', 'Grande', 'Imenso', 'Colossal']

# a Defesa e a protecao, nivel a nivel — da linha do `Desastre`
DEF, PROT = {}, {}
dentro = False
for ln in ler(TABELA).split('\n'):
    if re.match(r'## `Desastre`', ln):
        dentro = True
        continue
    if dentro and re.match(r'## `', ln):
        break
    m = re.match(r'\| (\d+) \| `\d+` \| `\d+` \| `\d+` \| `[^`]+` \| `(\d+)` \| `\+\d+` \| '
                 r'`\d+` \| `\d+` \| `\+(\d+)` \|$', ln)
    if dentro and m:
        DEF[int(m.group(1))] = int(m.group(2))
        PROT[int(m.group(1))] = int(m.group(3))
if len(DEF) < 29:
    print(f'  !! ANCORA PERDIDA: a Defesa por nível — li {len(DEF)} linhas')
    sys.exit(1)
NIVEIS = sorted(DEF)

# o nivel de referencia que a MEDIDA usou
REF = [nv for nv in NIVEIS if DEF[nv] == TAM['Médio']['defesa_ref']]

bloco('AS ANCORAS')
print(f'  a fórmula da Defesa       10 + Destreza + proteção        {FORM}')
print(f'  o orçamento de atributo   9 na criação, teto {TETO_CRIACAO} · +1 por marco, teto {TETO_TOTAL}')
print(f'  o piso do atributo        {PISO_ATRIB}  — os pontos se COMPRAM, não se devem')
print()
print(f'  {"tamanho":<12}{"alcance":>10}{"ganho":>9}{"Defesa Δ":>10}{"produto":>10}   o golpe pega')
for t in ORDEM_T:
    d = TAM[t]
    print(f'  {t:<12}{d["alcance"]:>8.1f} m{d["ganho"]:>9.4f}{d["delta"]:>+10}{d["produto"]:>10.3f}   '
          f'{re.sub(r"[*`]", "", d["pega"])}')
print()
print(f'  ⚠ A `MEDIDA-o-tamanho` fechou a troca com Defesa base {TAM["Médio"]["defesa_ref"]},')
print(f'     que é o nível {REF[0]} a {REF[-1]}. **É o topo da tabela.**')


bloco('1. A DEFESA QUE O `tamanho` PEDE — contra o que a FÓRMULA consegue construir')
print()
print('  Defesa mínima construível = 10 + 0 + proteção. O atributo tem piso 0: os pontos')
print('  se compram, e ninguém deve ponto pro sistema.')
print()
print(f'  {"nv":>4}{"prot":>6}{"mín":>6}', end='')
for t in ORDEM_T:
    print(f'{t[:9]:>21}', end='')
print()
print(f'  {"":>4}{"":>6}{"":>6}', end='')
for t in ORDEM_T:
    print(f'{"pede":>11}{"consegue":>10}', end='')
print()
print('  ' + '-' * 100)
QUEBRA = {t: [] for t in ORDEM_T}
for nv in NIVEIS:
    minimo = 10 + PISO_ATRIB + PROT[nv]
    print(f'  {nv:>4}{PROT[nv]:>6}{minimo:>6}', end='')
    for t in ORDEM_T:
        pede = DEF[nv] + TAM[t]['delta']
        real = max(pede, minimo)
        if real > pede:
            QUEBRA[t].append((nv, pede, real))
        marca = '!' if real > pede else ' '
        print(f'{pede:>11}{str(real) + marca:>10}', end='')
    print()
print()
for t in ORDEM_T:
    q = QUEBRA[t]
    if q:
        print(f'  ⚠⚠ `{t}` é INCONSTRUÍVEL em {len(q)} de {len(NIVEIS)} níveis — '
              f'nv{q[0][0]} a nv{q[-1][0]}.')
        pior = max(q, key=lambda x: x[2] - x[1])
        print(f'      O pior é o nv{pior[0]}: a troca pede Defesa {pior[1]} e a fórmula '
              f'não desce de {pior[2]}.')
    else:
        print(f'  ✅ `{t}` é construível em todos os {len(NIVEIS)} níveis.')


bloco('2. QUANTOS PONTOS DE DEFESA ELE DEVE, E QUANTOS ELE PAGA — sem modelo nenhum')
print()
print('  Esta e' + ' a conta livre de modelo: a troca DEVE tantos pontos de Defesa, e a formula')
print('  so deixa pagar tantos. A diferenca e ganho puro, e ela nao depende de como se preca')
print('  um ponto de Defesa.')
print()
print(f'  {"tamanho":<12}{"deve":>7}', end='')
FAIXAS = [(2, 9), (10, 17), (18, 25), (26, 30)]
for a, b in FAIXAS:
    print(f'{f"nv{a}-{b}":>12}', end='')
print()
print('  ' + '-' * 68)
for t in ORDEM_T[1:]:
    deve = -TAM[t]['delta']
    print(f'  {t:<12}{deve:>7}', end='')
    for a, b in FAIXAS:
        nv = a
        minimo = 10 + PISO_ATRIB + PROT[nv]
        pago = DEF[nv] - max(DEF[nv] + TAM[t]['delta'], minimo)
        print(f'{f"{pago} de {deve}":>12}', end='')
    print()
print()
print('  >> o `Colossal` paga 3 dos 7 que deve na faixa de baixo. Isso e' + ' menos da METADE,')
print('     e nenhum modelo de preco muda esse numero.')

bloco('2b. E QUANTO ISSO VALE — ⚠ AQUI TEM MODELO, e ele e' + ' aproximacao')
print()
print('  ⚠ A `MEDIDA-o-tamanho` preca Defesa com custo CONVEXO ("1/x e' + ' convexo, cada ponto')
print('     custa mais que o anterior"). O modelo abaixo e' + ' LINEAR, entao os produtos nao')
print('     batem com os publicados. Use a ORDEM e o SINAL, nao o valor absoluto.')
print()
CUSTO_DEF = None
mcd = re.search(r'\| `−1` de Defesa \| \*\*custa `([\d,]+)%`\*\* \|', ler(TAMANHO))
if mcd:
    CUSTO_DEF = n(mcd.group(1)) / 100
else:
    mcd = pega(TAMANHO, r'`−1` de Defesa\*{0,2} \| \*\*custa `([\d,]+)%`\*\*', 'o custo de 1 Defesa')
    CUSTO_DEF = n(mcd.group(1)) / 100
print(f'  o custo de `−1` de Defesa, do câmbio que o papel construiu: {CUSTO_DEF:.1%}')
print()
print(f'  {"nv":>4}', end='')
for t in ORDEM_T[1:]:
    print(f'{t[:9]:>26}', end='')
print()
print(f'  {"":>4}', end='')
for t in ORDEM_T[1:]:
    print(f'{"Δ real":>9}{"produto":>9}{"folga":>8}', end='')
print()
print('  ' + '-' * 82)
FOLGA = {t: [] for t in ORDEM_T[1:]}
for nv in NIVEIS:
    minimo = 10 + PISO_ATRIB + PROT[nv]
    print(f'  {nv:>4}', end='')
    for t in ORDEM_T[1:]:
        pede = DEF[nv] + TAM[t]['delta']
        real = max(pede, minimo)
        delta_real = real - DEF[nv]          # negativo
        # o produto: ganho x (1 - custo por ponto de Defesa perdido)
        paga = (1 - CUSTO_DEF) ** (-delta_real)
        prod = TAM[t]['ganho'] * paga
        FOLGA[t].append((nv, prod))
        print(f'{delta_real:>+9}{prod:>9.3f}{prod - TAM[t]["produto"]:>+8.3f}', end='')
    print()
print()
for t in ORDEM_T[1:]:
    v = [p for _, p in FOLGA[t]]
    print(f'  `{t:<9}` produto de {min(v):.3f} a {max(v):.3f}   '
          f'(a MEDIDA publica {TAM[t]["produto"]:.3f})')


bloco('3. E O TAMANHO DEVOLVE PONTO DE ATRIBUTO — que o produto não vê')
print()
print('  A Defesa lê a Destreza. Se a Defesa cai, a Destreza obrigada cai junto — e os')
print('  pontos voltam pro orçamento.')
print()
m2 = re.search(r'\| o orçamento no nv20 \| \*\*`(\d+)`\*\* — `(\d+)` na criação \(teto `\d`\) \+ '
               r'`(\d+)` marcos', ler(ACHADOS))
if not m2:
    print('  !! ANCORA PERDIDA: o orçamento do nv20 no ACHADOS')
    sys.exit(1)
ORC20, CRIA20, MARCOS20 = int(m2.group(1)), int(m2.group(2)), int(m2.group(3))
print(f'  o orçamento no nv20: {ORC20} pontos — {CRIA20} na criação + {MARCOS20} marcos.')
print(f'  ⚠ e o achado `2` do teste do Sukuna: as derivadas comem {MARCOS20} de {MARCOS20} marcos,')
print(f'    e sobram 3 pontos de {ORC20} pra cor.')
print()
nv = 20
minimo = 10 + PISO_ATRIB + PROT[nv]
dex_base = DEF[nv] - 10 - PROT[nv]
print(f'  {"tamanho":<12}{"Defesa":>9}{"Destreza obrigada":>20}{"pontos devolvidos":>20}'
      f'{"sobra pra cor":>16}')
print('  ' + '-' * 78)
for t in ORDEM_T:
    pede = DEF[nv] + TAM[t]['delta']
    real = max(pede, minimo)
    dex = real - 10 - PROT[nv]
    devolve = dex_base - dex
    print(f'  {t:<12}{real:>9}{dex:>20}{devolve:>+20}{3 + devolve:>16}')
print()
print('  >> o `Colossal` no nv20 devolve pontos que valem MAIS que a sobra inteira de cor.')
print('     E isso nao esta no produto: o produto so conta alcance, alvos e Defesa.')


bloco('4. AS SAIDAS, COM O NUMERO DE CADA UMA')
print()
print('  O problema em uma linha: a Defesa tem PISO de formula e o tamanho pede abaixo dele.')
print('  As quatro saidas, e todas fecham o invariante — o que muda e o que se perde.')
print()

print('  A — o `Colossal` corta 2 vizinhos em vez de 3 (a MEDIDA ja ofereceu isso no §3)')
print('      ele vira o ganho do `Imenso` e fecha com Defesa −4.')
imenso_ok = [nv for nv in NIVEIS if DEF[nv] - 4 >= 10 + PISO_ATRIB + PROT[nv]]
print(f'      >> mas −4 so' + f' e construivel de nv{min(imenso_ok)} pra cima. Sobra o buraco do nv2 ao '
      f'nv{min(imenso_ok)-1}.')
print(f'      >> e o `Colossal` deixa de ter degrau proprio: ele VIRA o `Imenso`.')
print()

print('  B — cada degrau ganha um PISO DE NIVEL, e so existe onde a Defesa fecha')
print(f'      {"tamanho":<12}{"deve":>6}{"construível a partir de":>26}{"níveis perdidos":>18}')
print('      ' + '-' * 62)
for t in ORDEM_T[1:]:
    ok = [nv for nv in NIVEIS if DEF[nv] + TAM[t]['delta'] >= 10 + PISO_ATRIB + PROT[nv]]
    if ok:
        print(f'      {t:<12}{-TAM[t]["delta"]:>6}{f"nv{min(ok)}":>26}{len(NIVEIS)-len(ok):>18}')
    else:
        print(f'      {t:<12}{-TAM[t]["delta"]:>6}{"NUNCA":>26}{len(NIVEIS):>18}')
print(f'      >> o `Colossal` nao existe em nivel nenhum. A saida B mata ele.')
print()

print('  C — o `tamanho` para de pagar em DEFESA e passa a pagar em VIDA, como os papeis')
print('      a vida e continua e nao tem piso de formula. O invariante fecha em TODO nivel.')
print()
print(f'      {"tamanho":<12}{"ganho":>9}{"paga vida ×":>14}{"produto":>10}')
print('      ' + '-' * 46)
for t in ORDEM_T:
    g = TAM[t]['ganho']
    print(f'      {t:<12}{g:>9.4f}{1/g:>14.3f}{g*(1/g):>10.3f}')
print(f'      >> custa a FICCAO: um bicho de 6 m deixa de ser mais facil de acertar.')
print()

print('  D — hibrido: a Defesa cai o que a formula DEIXAR, e o resto vira vida')
print('      mantem a ficcao e fecha o invariante. Custa uma coluna por faixa de nivel.')
print()
print(f'      {"tamanho":<12}', end='')
for a, b in FAIXAS:
    print(f'{f"nv{a}-{b}":>18}', end='')
print()
print(f'      {"":<12}', end='')
for _ in FAIXAS:
    print(f'{"Defesa":>9}{"vida ×":>9}', end='')
print()
print('      ' + '-' * 84)
for t in ORDEM_T[1:]:
    print(f'      {t:<12}', end='')
    for a, b in FAIXAS:
        minimo = 10 + PISO_ATRIB + PROT[a]
        pago = DEF[a] - max(DEF[a] + TAM[t]['delta'], minimo)
        falta = (-TAM[t]['delta']) - pago
        # o que a Defesa nao pagou vira vida, no mesmo cambio linear
        resto = (1 - CUSTO_DEF) ** falta
        print(f'{-pago:>+9}{resto:>9.3f}', end='')
    print()
print(f'      >> onde a Defesa paga tudo, a vida fica em 1,000 e nada muda.')
print(f'      >> ⚠ os `vida ×` acima usam o cambio LINEAR — o numero final sai do convexo.')
print()
print('  E — a Defesa cai um valor FIXO que e' + ' sempre pagavel, e o resto vira vida FIXA')
print('      uma tabela so, quatro linhas, construivel em TODO nivel. Sem faixa.')
print()
MAX_PAGAVEL = min(DEF[nv] - (10 + PISO_ATRIB + PROT[nv]) for nv in NIVEIS)
print(f'      o maior corte de Defesa que fecha em TODOS os {len(NIVEIS)} niveis: −{MAX_PAGAVEL}')
print(f'      (o nivel que aperta e' + f' o nv{min(NIVEIS, key=lambda x: DEF[x]-(10+PISO_ATRIB+PROT[x]))}: '
      f'base {DEF[2]}, proteção {PROT[2]}, piso {10+PISO_ATRIB+PROT[2]})')
print()
print(f'      {"tamanho":<12}{"deve":>6}{"Defesa":>9}{"falta":>7}{"vida × (teto)":>16}')
print('      ' + '-' * 52)
for t in ORDEM_T:
    deve = -TAM[t]['delta']
    paga_def = min(deve, MAX_PAGAVEL)
    falta = deve - paga_def
    teto = (1 - CUSTO_DEF) ** falta
    print(f'      {t:<12}{deve:>6}{-paga_def:>+9}{falta:>7}'
          f'{(f"{teto:.3f}" if falta else "1,000  —"):>16}')
print()
print('      ⚠ O `vida ×` acima e' + ' TETO, nao valor final. Ele sai do cambio LINEAR, e a')
print('        `MEDIDA-o-tamanho` preca Defesa em cambio CONVEXO ("cada ponto custa mais que')
print('        o anterior"). Como os pontos que FALTAM sao os ULTIMOS — os mais caros —, o')
print('        convexo cobra mais que isso.')
print('      >> ENTAO: `Colossal` paga vida × 0,683 OU MENOS. O numero final tem de ser rodado')
print('         no cambio convexo da MEDIDA, que este script nao reconstroi.')
print()
print(f'      >> `Imenso` e `Colossal` ficam com a MESMA Defesa (−{MAX_PAGAVEL}), e se separam')
print(f'         em vida e em alvos. A ficcao "maior e' + ' mais facil de acertar" sobrevive')
print(f'         entre `Médio` e `Grande`, e empata do `Imenso` pra cima.')

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
O ESPALHAMENTO DAS FORMAS DE AREA — refeito, porque eu errei.

Ele, 10/09/2026: "Mas o da linha pega um alcance maior, ent ta justo, n?"

E ele esta certo, e a minha conta anterior estava errada. Eu publiquei "20x
entre o Cone e a Linha no d5". Errado: eu comparei os dois no MESMO INDICE DE
DEGRAU, e eles nao COMECAM no mesmo degrau.

  a escada compartilhada: 4,5 · 9 · 18 · 30 · 60 m
  o Cone  comeca em 4,5 m  -> degrau 1
  a Linha comeca em 18 m   -> degrau 3

Entao uma compra de `Maior` nao poe os dois no mesmo lugar. A comparacao certa
e: mesma CLASSE, mesma compra, quanto cada uma cobre — e quanto cada uma
ALCANCA, que e o que ele levantou.

E depois: o campo espalha quanto entre as formas dele, pelo mesmo preco?

Nenhum numero nasce aqui.
"""
import collections
import json
import math
import os
import re
import statistics
import sys

BEST = os.environ.get('JJK_BEST', '/media/mizuki/HD Externo II/Claude/Claude 2/bestiario')
REPO = os.environ.get('JJK_REPO', '/media/mizuki/HD Externo II/Claude/Claude 2')
FILA = os.path.join(BEST, '04-fase-1/fila')
DS = os.path.join(FILA, 'dados-recarga-area/data-md-main')
PARTC = 'manual/gerador/partC.js'
PARTD = 'manual/gerador/partD.js'
P19 = 'finalizado/regra/19-dano-e-condicoes.md'

QUAD = 1.5
AB = 1.0        # abertura do cone, decidida: a do D&D 2024

_cache = {}


def ler(rel, raiz=REPO):
    k = (rel, raiz)
    if k not in _cache:
        with open(os.path.join(raiz, rel), encoding='utf-8') as f:
            _cache[k] = f.read()
    return _cache[k]


def pega(rel, padrao, rotulo, raiz=REPO):
    m = re.search(padrao, ler(rel, raiz))
    if not m:
        print(f'\n  !! ANCORA PERDIDA: {rotulo}\n     nao casa em {rel}\n     padrao: {padrao}')
        sys.exit(1)
    return m


def n(s):
    return float(s.replace(',', '.'))


def bloco(t):
    print()
    print('=' * 96)
    print(t)
    print('=' * 96)


# ------------------------------------------------------------- 0 · as âncoras
bloco('0 · AS ÂNCORAS — a escada, as bases por Classe, e o teto de compra')

m = pega(PARTC, r"\['Cone e Linha', '([^']+)'\]", 'partC.js — a escada Cone e Linha')
ESCADA = [n(x) for x in re.findall(r'([\d,]+) m', m.group(1))]
m = pega(PARTC, r"\['Esfera \(raio\)', '([^']+)'\]", 'partC.js — a escada da Esfera')
ESF = [n(x) for x in re.findall(r'([\d,]+) m', m.group(1))]
print(f'  escada `Cone e Linha` : ' + ' → '.join(f'{v:g}' for v in ESCADA) + ' m')
print(f'  escada `Esfera (raio)`: ' + ' → '.join(f'{v:g}' for v in ESF) + ' m')

BASE = {}
m = pega(PARTC, r"\['Cone', '([\d,]+) m', '([\d,]+) m', '([\d,]+) m'\]",
         'partC.js — a base por Classe do Cone')
BASE['Cone'] = [n(m.group(i)) for i in (1, 2, 3)]
m = pega(PARTC, r"\['Linha', '([\d,]+) × ([\d,]+) m', '([\d,]+) × ([\d,]+) m', '([\d,]+) × ([\d,]+) m'\]",
         'partC.js — a base por Classe da Linha')
BASE['Linha'] = [(n(m.group(1)), n(m.group(2))), (n(m.group(3)), n(m.group(4))),
                 (n(m.group(5)), n(m.group(6)))]
m = pega(PARTC, r"\['Explosão', 'raio ([\d,]+) m, a [\d,]+ m', 'raio ([\d,]+) m, a [\d,]+ m', "
                r"'raio ([\d,]+) m, a [\d,]+ m'\]", 'partC.js — a base por Classe da Explosão')
BASE['Esfera'] = [n(m.group(i)) for i in (1, 2, 3)]

CLASSES = ['Classe 0', 'Classes 1–5', 'Classes 6–7']
print()
for i, c in enumerate(CLASSES):
    print(f'  {c:<14} Esfera raio {BASE["Esfera"][i]:>4g} m   Cone {BASE["Cone"][i]:>4g} m   '
          f'Linha {BASE["Linha"][i][0]:g} × {BASE["Linha"][i][1]:g} m')

m = pega(PARTD, r"\['Maior', '(\w+)', 'Sobe um degrau de tamanho de área\. Pode comprar (\w+) vezes\.'\]",
         'partD.js — a Melhoria Maior')
VEZES = {'duas': 2, 'três': 3}[m.group(2)]
m2 = pega(PARTD, r"\['Muito Maior', '(\w+)', 'Sobe (\w+) degraus de tamanho de uma vez\.'\]",
          'partD.js — a Melhoria Muito Maior')
MUITO = {'três': 3, 'dois': 2}[m2.group(2)]
print(f'\n  `Maior` sobe 1 degrau, pode comprar {VEZES}× ⟹ teto +{VEZES}')
print(f'  `Muito Maior` sobe {MUITO} degraus de uma vez ⟹ teto +{MUITO}')
TETO = max(VEZES, MUITO)
print(f'  ⟹ o teto de subida é +{TETO} degraus')

m = pega(P19, r'reprova a partir de `([\d,]+)×`', 'peça 19 §3.6 — o filtro de dominância')
FILTRO = n(m.group(1))
print(f'\n  peça 19 §3.6 · o filtro de dominância do projeto reprova a partir de {FILTRO:.2f}×')


# --------------------------------------------------- 1 · a comparação CERTA
bloco('1 · ⚠ A COMPARAÇÃO CERTA — mesma Classe, mesma compra')


def q_esf(r):
    return math.pi * r ** 2 / QUAD ** 2


def q_cone(L):
    return L * (L * AB) / 2 / QUAD ** 2


def q_lin(c, l):
    return c * l / QUAD ** 2


def sobe(escada, valor, degraus):
    i = escada.index(valor) if valor in escada else 0
    return escada[min(i + degraus, len(escada) - 1)]


print(f'  ⚠ O que eu tinha feito ERRADO: comparei `Cone` e `Linha` no mesmo ÍNDICE de degrau.')
print(f'     Mas o Cone começa no degrau 1 ({ESCADA[0]:g} m) e a Linha no degrau '
      f'{ESCADA.index(BASE["Linha"][1][0])+1} ({BASE["Linha"][1][0]:g} m).')
print(f'     Uma compra de `Maior` NÃO põe os dois no mesmo lugar.\n')

for ic, cl in enumerate(CLASSES):
    print(f'  {cl}')
    print(f'    {"compra":<16}{"Esfera":>22}{"Cone":>22}{"Linha":>26}')
    for d in range(0, TETO + 1):
        r = sobe(ESF, BASE['Esfera'][ic], d)
        c = sobe(ESCADA, BASE['Cone'][ic], d)
        lc, ll = BASE['Linha'][ic]
        lc = sobe(ESCADA, lc, d)
        qe, qc, ql = q_esf(r), q_cone(c), q_lin(lc, ll)
        rot = 'base' if d == 0 else f'+{d} degrau' + ('s' if d > 1 else '')
        print(f'    {rot:<16}{f"{r:g} m = {qe:.0f} q":>22}{f"{c:g} m = {qc:.0f} q":>22}'
              f'{f"{lc:g}×{ll:g} m = {ql:.0f} q":>26}')
    # espalhamento no teto e na base
    for d, rot in ((0, 'na base'), (TETO, f'no teto (+{TETO})')):
        r = sobe(ESF, BASE['Esfera'][ic], d)
        c = sobe(ESCADA, BASE['Cone'][ic], d)
        lc, ll = BASE['Linha'][ic]
        lc = sobe(ESCADA, lc, d)
        vals = [q_esf(r), q_cone(c), q_lin(lc, ll)]
        esp = max(vals) / min(vals)
        flag = '❌ REPROVA' if esp > FILTRO else '✅ passa'
        print(f'      espalhamento {rot:<16}{esp:5.2f}×   (filtro {FILTRO:.2f}×)  {flag}')
    print()

print('  ### ⟹ E ELE ESTÁ CERTO sobre o alcance — a Linha vai MAIS LONGE:')
ic = 1
for d in (0, TETO):
    c = sobe(ESCADA, BASE['Cone'][ic], d)
    lc, _ = BASE['Linha'][ic]
    lc = sobe(ESCADA, lc, d)
    print(f'    +{d} degrau: o `Cone` alcança {c:g} m, a `Linha` alcança {lc:g} m  '
          f'— a Linha vai {lc/c:.2f}× mais longe')


# ----------------------------------------- 2 · o campo espalha quanto?
bloco('2 · O CAMPO — quanto ELE espalha entre as formas, pelo mesmo preço?')

SRD = {}
for arq, rot in (('srd-2024.json', 'D&D 2024'), ('srd-2014.json', 'D&D 2014')):
    with open(os.path.join(FILA, arq), encoding='utf-8') as f:
        SRD[rot] = json.load(f)

PES = 0.3048   # pes -> metro


def cobertura_dnd(txt):
    """Devolve (forma, cobertura em quadrados de 1,5 m) das areas achadas no texto."""
    saida = []
    for m in re.finditer(r'(\d+)[- ]foot(?:-radius)?\s+(Cone|Line|Sphere|Cube|Emanation|Cylinder)',
                         txt, re.I):
        v = int(m.group(1)) * PES
        f = m.group(2).lower()
        if f == 'cone':
            a = v * v / 2
        elif f in ('sphere', 'emanation', 'cylinder'):
            a = math.pi * v * v
        elif f == 'cube':
            a = v * v
        elif f == 'line':
            a = v * 1.5      # o D&D publica so o comprimento; a largura padrao e 5 pes
        saida.append((f, a / QUAD ** 2))
    return saida


for rot, mons in SRD.items():
    por_forma = collections.defaultdict(list)
    for mo in mons:
        cr = mo.get('challenge_rating')
        if not cr:
            continue
        for a in (mo.get('actions') or []) + (mo.get('traits') or []):
            for f, q in cobertura_dnd(a.get('desc') or ''):
                por_forma[f].append(q)
    print(f'\n  {rot} — cobertura mediana por forma, em quadrados de 1,5 m')
    meds = {}
    for f, vs in sorted(por_forma.items(), key=lambda x: -len(x[1])):
        if len(vs) >= 3:
            meds[f] = statistics.median(vs)
            print(f'    {f:<12}{len(vs):>4} usos   mediana {meds[f]:>6.0f} q   '
                  f'(de {min(vs):.0f} a {max(vs):.0f})')
    if len(meds) >= 2:
        esp = max(meds.values()) / min(meds.values())
        maior = max(meds, key=meds.get)
        menor = min(meds, key=meds.get)
        print(f'    ⟹ espalhamento entre as formas: {esp:.2f}×   '
              f'({maior} {meds[maior]:.0f} q contra {menor} {meds[menor]:.0f} q)')

# Draw Steel — as formas dele sao em quadrado, direto
dstx = '\n'.join(open(os.path.join(r, a), encoding='utf-8').read()
                 for r, _, arqs in os.walk(os.path.join(DS, 'Bestiary'))
                 for a in arqs if a.endswith('.md'))
ds = collections.defaultdict(list)
for m in re.finditer(r'📏\s*([^|]+?)\s*\*\*', dstx):
    s = m.group(1).replace('**', '').strip()
    mb = re.match(r'(\d+)\s+burst', s, re.I)
    mc = re.match(r'(\d+)\s+cube', s, re.I)
    ml = re.match(r'(\d+)\s*[x×]\s*(\d+)\s+line', s, re.I)
    if mb:
        k = int(mb.group(1)); ds['burst'].append((2 * k + 1) ** 2)
    elif mc:
        k = int(mc.group(1)); ds['cube'].append(k * k)
    elif ml:
        ds['line'].append(int(ml.group(1)) * int(ml.group(2)))
print(f'\n  Draw Steel — cobertura mediana por forma, em quadrados')
meds = {}
for f, vs in sorted(ds.items(), key=lambda x: -len(x[1])):
    meds[f] = statistics.median(vs)
    print(f'    {f:<12}{len(vs):>4} usos   mediana {meds[f]:>6.0f} q   '
          f'(de {min(vs)} a {max(vs)})')
if len(meds) >= 2:
    esp = max(meds.values()) / min(meds.values())
    print(f'    ⟹ espalhamento entre as formas: {esp:.2f}×   '
          f'({max(meds, key=meds.get)} contra {min(meds, key=meds.get)})')

print(f'''
  ### ⟹ A PERGUNTA QUE ISSO RESPONDE:
      o campo TAMBEM deixa as formas cobrirem areas diferentes pelo mesmo preco?
      Se sim, o nosso espalhamento so e defeito se for MAIOR que o deles.''')

bloco('FIM')

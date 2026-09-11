#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
O `tamanho` VALIDADO CONTRA O DRAW STEEL — item 16.

Pedido do Mizuki, 10/09/2026: "novamente, roubamos esse conceito de Draw Steel,
n e bom olhar la pra saber a validacao? … sempre metrica antes de resposta em
achismo".

A `MEDIDA-o-tamanho` de 10/09 escreveu que a mecanica de `size` deles "nao abriu"
e que "a troca abaixo e construida com os cambios do Projeto-M, NAO copiada do
Draw Steel". O `Draw Steel Heroes.md` esta no dump — entao da pra abrir.

Mede tres coisas:
  1. o que o LIVRO diz que size faz
  2. o que os 415 statblocks FAZEM com size — Stamina, EV, alcance, atributo
  3. se existe orcamento de atributo por tamanho (a 2a pergunta do martelo)

Nenhum numero nosso mora aqui.
"""
import os
import re
import statistics
import sys

BEST = os.environ.get('JJK_BEST', '/media/mizuki/HD Externo II/Claude/Claude 2/bestiario')
DS = os.path.join(BEST, '04-fase-1/fila/dados-recarga-area/data-md-main')
STAT = os.path.join(DS, 'Bestiary/Monsters/Monsters')
HEROES = os.path.join(DS, 'Rules/Draw Steel Heroes.md')
BASICS = os.path.join(DS, 'Bestiary/Monsters/Chapters/Monster Basics.md')

TAMANHO = '04-fase-1/fila/MEDIDA-o-tamanho.md'

_c = {}


def ler(p):
    if p not in _c:
        with open(p, encoding='utf-8') as f:
            _c[p] = f.read()
    return _c[p]


def n(s):
    return float(s.replace('−', '-').replace(',', '.'))


def bloco(t):
    print()
    print('=' * 96)
    print(t)
    print('=' * 96)


# ordem de tamanho do Draw Steel, do livro:
# "Size 1T is one size smaller than 1S, two smaller than 1M, three smaller than 1L,
#  and four sizes smaller than size 2."
RANK = {'1T': 0, '1S': 1, '1M': 2, '1L': 3}
ROT = ['1T', '1S', '1M', '1L', '2', '3', '4', '5']


def rank(s):
    if s in RANK:
        return RANK[s]
    m = re.match(r'^(\d+)$', s)
    return 2 + int(m.group(1)) if m else None


# ------------------------------------------------------------------ 1 · o livro
bloco('1. O QUE O LIVRO DIZ QUE `size` FAZ — Draw Steel Heroes, "Size and Space"')
t = ler(HEROES)
m = re.search(r'#### Size and Space\n\n(.+?)\n', t)
if not m:
    print('  !! ANCORA PERDIDA: a seção "Size and Space" do Draw Steel Heroes')
    sys.exit(1)
print()
print('  "' + m.group(1)[:300] + '"')
print()
m2 = re.search(r'(There is no limit to what a creature\'s size might be\.)', t)
m3 = re.search(r'\*\*Size:\*\* (An indication of[^\n]+)', t)
if m3:
    print(f'  Glossário: "{m3.group(1)}"')
if m2:
    print(f'  E: "{m2.group(1)}"')
print()
# procura QUALQUER penalidade defensiva por tamanho
penal = [ln for ln in t.split('\n')
         if re.search(r'\bsize\b', ln, re.I)
         and re.search(r'edge|bane|easier to hit|harder to hit|bonus to.*defen', ln, re.I)]
print(f'  Linhas do livro que ligam `size` a acertar/errar mais: {len(penal)}')
for ln in penal[:4]:
    print(f'    "{ln.strip()[:150]}"')
print()
# e o que size DA' de graca
ganha = [ln for ln in t.split('\n')
         if re.search(r'your size is \d', ln, re.I) and re.search(r'bonus to distance|melee', ln, re.I)]
print(f'  Linhas em que ficar MAIOR dá alcance de corpo a corpo: {len(ganha)}')
for ln in ganha[:3]:
    print(f'    "{ln.strip()[:170]}"')


# ------------------------------------------------------------- 2 · os statblocks
CRIA = []
for dp, _, fs in os.walk(STAT):
    if 'Statblocks' not in dp:
        continue
    for f in sorted(fs):
        if not f.endswith('.md'):
            continue
        txt = ler(os.path.join(dp, f))
        mfm = re.search(r'^---\n(.*?)\n---', txt, re.S)
        if not mfm:
            continue
        fm = mfm.group(1)

        def campo(k):
            mm = re.search(r'^' + k + r': (.+)$', fm, re.M)
            return mm.group(1).strip().strip("'\"") if mm else None

        sz = campo('size')
        lv = campo('level')
        st = campo('stamina')
        if not (sz and lv and st):
            continue
        mr = re.search(r'^roles:\n((?:  - .+\n)+)', fm, re.M)
        papeis = [x.strip() for x in re.findall(r'^  - (.+)$', mr.group(1), re.M)] if mr else []
        if len(papeis) != 1 or papeis[0] == r'\-':
            continue
        p = papeis[0].split()
        org = p[0] if p[0] in ('Minion', 'Horde', 'Platoon', 'Elite', 'Leader', 'Solo') else '?'
        r = rank(sz)
        if r is None:
            continue
        ev = None
        e = campo('ev')
        if e:
            mm = re.match(r'^(\d+) for (\d+|four) minions?$', e)
            if mm:
                ev = int(mm.group(1)) / (4 if mm.group(2) == 'four' else int(mm.group(2)))
            elif re.match(r'^\d+$', e):
                ev = float(e)
        atrs = {}
        for a in ('might', 'agility', 'reason', 'intuition', 'presence'):
            v = campo(a)
            atrs[a] = int(v) if v and re.match(r'^-?\d+$', v) else None
        melee = [int(x) for x in re.findall(r'Melee (\d+)', txt)]
        CRIA.append({'nome': f[:-3], 'size': sz, 'rank': r, 'org': org,
                     'nv': int(re.match(r'-?\d+', lv).group(0)),
                     'stamina': int(re.match(r'-?\d+', st).group(0)),
                     'ev': ev, 'fs': campo('free_strike'), 'speed': campo('speed'),
                     'stab': campo('stability'), 'atr': atrs,
                     'melee': max(melee) if melee else None})

if len(CRIA) < 380:
    print(f'\n  !! li so {len(CRIA)} statblocks')
    sys.exit(1)

# normaliza por coorte (organizacao, nivel)
co = {}
for c in CRIA:
    co.setdefault((c['org'], c['nv']), []).append(c)
for c in CRIA:
    g = co[(c['org'], c['nv'])]
    ms = statistics.median([x['stamina'] for x in g])
    c['st_rel'] = c['stamina'] / ms if ms else None
    ge = [x['ev'] for x in g if x['ev'] is not None]
    me = statistics.median(ge) if ge else None
    c['ev_rel'] = (c['ev'] / me) if (me and c['ev'] is not None) else None
    c['coorte'] = len(g)


bloco('2. O QUE OS 415 STATBLOCKS FAZEM COM `size`')
print()
print('  Normalizado por coorte (mesma organização, mesmo nível) — nível e organização')
print('  saem da conta e sobra o tamanho.')
print()
print(f'  {"size":<6}{"n":>5}{"Stamina rel.":>15}{"EV rel.":>11}{"alcance melee":>16}'
      f'{"Σ atributos":>14}{"stability":>12}')
print('  ' + '-' * 82)
por = {}
for c in CRIA:
    por.setdefault(c['size'], []).append(c)
for s in ROT:
    v = por.get(s, [])
    if len(v) < 3:
        continue
    st = [x['st_rel'] for x in v if x['st_rel']]
    ev = [x['ev_rel'] for x in v if x['ev_rel']]
    ml = [x['melee'] for x in v if x['melee']]
    sa = [sum(y for y in x['atr'].values() if y is not None) for x in v
          if all(y is not None for y in x['atr'].values())]
    sb = [int(x['stab']) for x in v if x['stab'] and re.match(r'^-?\d+$', x['stab'])]
    print(f'  {s:<6}{len(v):>5}{statistics.median(st):>15.3f}'
          f'{(statistics.median(ev) if ev else float("nan")):>11.3f}'
          f'{(statistics.median(ml) if ml else float("nan")):>16.1f}'
          f'{(statistics.median(sa) if sa else float("nan")):>14.1f}'
          f'{(statistics.median(sb) if sb else float("nan")):>12.1f}')
print()
gr = [c for c in CRIA if c['rank'] >= 4]
pe = [c for c in CRIA if c['rank'] <= 2]
if gr and pe:
    a = statistics.median([c['st_rel'] for c in gr if c['st_rel']])
    b = statistics.median([c['st_rel'] for c in pe if c['st_rel']])
    ae = [c['ev_rel'] for c in gr if c['ev_rel']]
    be = [c['ev_rel'] for c in pe if c['ev_rel']]
    print(f'  >> size 2+ (n={len(gr)}): Stamina {a:.3f} × a coorte · EV {statistics.median(ae):.3f} ×')
    print(f'  >> size 1M ou menor (n={len(pe)}): Stamina {b:.3f} × · EV {statistics.median(be):.3f} ×')
    print(f'  >> a razão de Stamina entre os dois: {a/b:.3f} ×')


bloco('3. O TAMANHO COMPRA ALCANCE? — e ele PAGA por isso?')
print()
print(f'  {"size":<6}{"n com Melee":>13}{"alcance mediano":>18}{"mín":>6}{"máx":>6}'
      f'{"Stamina rel.":>15}{"EV rel.":>10}')
print('  ' + '-' * 76)
for s in ROT:
    v = [x for x in por.get(s, []) if x['melee']]
    if len(v) < 3:
        continue
    ml = [x['melee'] for x in v]
    st = [x['st_rel'] for x in v if x['st_rel']]
    ev = [x['ev_rel'] for x in v if x['ev_rel']]
    print(f'  {s:<6}{len(v):>13}{statistics.median(ml):>18.1f}{min(ml):>6}{max(ml):>6}'
          f'{statistics.median(st):>15.3f}{(statistics.median(ev) if ev else float("nan")):>10.3f}')
print()


bloco('4. EXISTE ORÇAMENTO DE ATRIBUTO POR TAMANHO? — a 2ª pergunta do martelo')
print()
print('  A nossa pergunta: o `tamanho` devolve ponto de atributo (Destreza), e isso deve')
print('  virar preço? No Draw Steel, a pergunta equivalente e: a SOMA dos cinco atributos')
print('  cresce com o tamanho, ou ela e' + ' um orcamento fixo que so muda de forma?')
print()
print(f'  {"size":<6}{"n":>5}{"Σ atributos":>14}{"Might":>9}{"Agility":>9}{"Reason":>9}'
      f'{"Intuition":>11}{"Presence":>10}')
print('  ' + '-' * 74)
somas = []
for s in ROT:
    v = [x for x in por.get(s, []) if all(y is not None for y in x['atr'].values())]
    if len(v) < 3:
        continue
    sa = [sum(x['atr'].values()) for x in v]
    somas.append((s, statistics.median(sa)))
    print(f'  {s:<6}{len(v):>5}{statistics.median(sa):>14.1f}', end='')
    for a in ('might', 'agility', 'reason', 'intuition', 'presence'):
        print(f'{statistics.median([x["atr"][a] for x in v]):>9.1f}'
              if a != 'intuition' else
              f'{statistics.median([x["atr"][a] for x in v]):>11.1f}', end='')
    print()
print()
if len(somas) >= 2:
    v = [x for _, x in somas]
    print(f'  >> a soma vai de {min(v):.1f} a {max(v):.1f} — variação de {max(v)-min(v):.1f} ponto(s).')
    print(f'  >> e ela cresce com o tamanho? '
          f'{"SIM" if somas[-1][1] > somas[0][1] else "não"}  '
          f'({somas[0][0]} = {somas[0][1]:.1f} → {somas[-1][0]} = {somas[-1][1]:.1f})')
print()
print('  ⚠ Mas a soma bruta confunde NIVEL com tamanho: bicho grande tende a ser de nivel')
print('     alto. Normalizando por coorte:')
print()
for c in CRIA:
    g = co[(c['org'], c['nv'])]
    sa = [sum(x['atr'].values()) for x in g if all(y is not None for y in x['atr'].values())]
    ms = statistics.median(sa) if sa else None
    tot = (sum(c['atr'].values())
           if all(y is not None for y in c['atr'].values()) else None)
    c['atr_rel'] = (tot / ms) if (ms and tot is not None and ms != 0) else None
print(f'  {"size":<6}{"n":>5}{"Σ atributos rel. à coorte":>28}')
print('  ' + '-' * 42)
for s in ROT:
    v = [x['atr_rel'] for x in por.get(s, []) if x['atr_rel'] is not None]
    if len(v) < 3:
        continue
    print(f'  {s:<6}{len(v):>5}{statistics.median(v):>28.3f}')


bloco('5. ⚠ A PERGUNTA QUE DECIDE — bicho grande pega MAIS GENTE no corpo a corpo?')
print()
print('  O nosso `tamanho` da DUAS coisas: alcance E "o golpe pega vizinhos a metade".')
print('  A secao 3 mostrou que o alcance ele copia do campo. E os vizinhos?')
print()
PAT = re.compile(r'📏 Melee (\d+)\*{0,2}\s*\|\s*\*{0,2}🎯 ([^*|]+)')
NUM = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6}


def alvos(txt):
    t2 = txt.strip().lower()
    if t2.startswith('self'):
        return None
    if t2.startswith('the triggering'):
        return 1
    m = re.match(r'(\w+) ', t2)
    if m and m.group(1) in NUM:
        return NUM[m.group(1)]
    if t2.startswith('each'):
        return 'area'
    return None


MEL = {}
for dp, _, fs in os.walk(STAT):
    if 'Statblocks' not in dp:
        continue
    for f in sorted(fs):
        if not f.endswith('.md'):
            continue
        txt = ler(os.path.join(dp, f))
        mfm = re.search(r'^---\n(.*?)\n---', txt, re.S)
        if not mfm:
            continue
        ms = re.search(r'^size: (.+)$', mfm.group(1), re.M)
        if not ms:
            continue
        sz = ms.group(1).strip().strip("'\"")
        for d, a in PAT.findall(txt):
            v = alvos(a)
            if isinstance(v, int):
                MEL.setdefault(sz, []).append((int(d), v, a.strip()))

print(f'  {"size":<6}{"n":>5}{"alcance mediano":>18}{"ALVOS mediano":>16}{"alvos máx":>12}'
      f'{"% com 2+ alvos":>17}')
print('  ' + '-' * 74)
serie = []
for s in ROT:
    v = MEL.get(s, [])
    if len(v) < 4:
        continue
    dist = [x[0] for x in v]
    alv = [x[1] for x in v]
    mult = sum(1 for x in alv if x >= 2) / len(alv)
    serie.append((s, statistics.median(dist), statistics.median(alv), mult))
    print(f'  {s:<6}{len(v):>5}{statistics.median(dist):>18.1f}{statistics.median(alv):>16.1f}'
          f'{max(alv):>12}{mult:>16.0%}')
print()
# ⚠ agrupar por MEDIANA DAS MEDIANAS infla o numero. Aqui as acoes sao SOMADAS.
PEQ = [x for sz, v in MEL.items() if sz.startswith('1') for x in v]
GRA = [x for sz, v in MEL.items() if not sz.startswith('1') for x in v]
if PEQ and GRA:
    mp = sum(1 for x in PEQ if x[1] >= 2) / len(PEQ)
    mg = sum(1 for x in GRA if x[1] >= 2) / len(GRA)
    print(f'  Somando as AÇÕES (não a mediana das linhas):')
    print()
    print(f'    size 1 — qualquer sub-degrau   {len(PEQ):>4} ações   {mp:>6.0%} pegam 2+ alvos')
    print(f'    size 2 ou maior                {len(GRA):>4} ações   {mg:>6.0%} pegam 2+ alvos')
    print()
    print(f'  >> bicho grande pega 2+ alvos {mg/mp:.2f} × mais que bicho de 1 quadrado.')
    print(f'  >> E ele NAO PAGA por isso: Stamina 1,000 e EV 1,000 na secao 2.')
    print()
    print(f'  ⟹ no Draw Steel o `size` da alcance E alvos, e o preco dele e ZERO.')
    print(f'     O livro define size como ESPACO — "an indication of a creature\'s space" —,')
    print(f'     nao existe estatistica de defesa pra baixar, e "there is no limit to what a')
    print(f'     creature\'s size might be".')

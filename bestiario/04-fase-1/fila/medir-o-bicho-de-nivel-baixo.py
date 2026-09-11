# -*- coding: utf-8 -*-
"""MEDIDA — item `21`: o bicho de nível BAIXO do campo tem quantos botões?

A máquina deu `1` botão pra `Ameaça` do nv2 ao nv8 (`golpe ÷ 4,5` < a `Classe 1`).
A pergunta é se isso é o formato do campo ou defeito nosso.

Corpora em disco: SRD 2024 (331) · SRD 2014 (325) · Draw Steel (437).
Âncoras do Projeto-M lidas do dono.
"""
import json, re, glob, os, sys, statistics as st
from collections import defaultdict, Counter

AQUI = os.path.dirname(os.path.abspath(__file__))
BEST = os.path.dirname(os.path.dirname(AQUI))
P26  = "/media/mizuki/HD Externo II/Claude/Claude 2/sistema/03-mecanica/26-bestiario.md"
TAB  = os.path.join(BEST, '04-fase-1', 'TABELA.md')
R5   = os.path.join(BEST, '03-bloco', 'RASCUNHO-5-o-bloco-em-branco.md')
ANC  = os.path.join(BEST, '05-sukuna', 'ANCORAS-do-repositorio.md')

def ler(p):
    if not os.path.exists(p): sys.exit('DONO SUMIU: %s' % p)
    return open(p, encoding='utf-8').read()
def exige(c, m):
    if not c: sys.exit('ÂNCORA PERDIDA: ' + m)
def num(s): return float(s.replace('−','-').replace(',','.'))
def med(e):
    m = re.match(r'(\d+)d(\d+)(?:\s*\+\s*(\d+))?$', e.strip())
    if m: return int(m.group(1))*(1+int(m.group(2)))/2 + int(m.group(3) or 0)
    return float(e) if re.match(r'^\d+$', e.strip()) else None

# ─────────────────────────────── âncoras nossas
DIV = num(re.search(r'O orçamento de feitiço de uma ação é o golpe dela dividido por `([\d,]+)`', ler(P26)).group(1))
m = re.search(r'\*\*Classe 1\*\*\s*\|\s*`(\d+)` pontos', ler(ANC))
exige(m, 'o custo da `Classe 1` sumiu do ANCORAS-do-repositorio')
CLASSE1 = int(m.group(1))
m = re.search(r'\|\s*bloco normal\s*\|\s*\*{0,2}`(\d+)`\*{0,2}\s*entradas', ler(R5))
exige(m, 'a linha de entradas nomeadas sumiu do RASCUNHO-5')
LINHA_NORMAL = int(m.group(1))

def tab(cat, nv):
    t = ler(TAB); corpo = t.split('## `%s`' % cat)[1].split('\n## ')[0]
    cab = None
    for ln in corpo.split('\n'):
        cels = [c.strip().strip('*').strip('`').strip('*') for c in ln.strip().strip('|').split('|')]
        if cels and cels[0] == 'nv': cab = cels
        elif cab and cels and cels[0] == str(nv): return dict(zip(cab, cels))
    return None

# ─────────────────────────────── o corpo do campo
def entradas_dnd(m):
    tr = [t for t in (m.get('traits') or []) if (t.get('name') or '').strip()]
    ac = [a for a in (m.get('actions') or []) if (a.get('name') or '').strip()]
    return len(tr), len(ac)

def faixa_cr(cr):
    if cr is None: return None
    if cr <= 1: return 'CR 0–1'
    if cr <= 4: return 'CR 2–4'
    if cr <= 10: return 'CR 5–10'
    if cr <= 16: return 'CR 11–16'
    return 'CR 17+'
ORD_CR = ['CR 0–1','CR 2–4','CR 5–10','CR 11–16','CR 17+']

def faixa_nv(nv):
    if nv is None: return None
    if nv <= 2: return 'nv 1–2'
    if nv <= 5: return 'nv 3–5'
    if nv <= 8: return 'nv 6–8'
    return 'nv 9+'
ORD_NV = ['nv 1–2','nv 3–5','nv 6–8','nv 9+']

print('=' * 84)
print('ÂNCORAS')
print('=' * 84)
print('  §6.5 divisor %.1f · `Classe 1` custa %d pontos ⟹ o piso `seco` é %.1f de golpe'
      % (DIV, CLASSE1, DIV * CLASSE1))
print('  a linha de entradas nomeadas do bloco normal: %d' % LINHA_NORMAL)
secos = []
for nv in range(2, 31):
    r = tab('Ameaça', nv)
    if not r: continue
    g = med(r['o golpe'])
    if g is not None and g / DIV < CLASSE1: secos.append(nv)
print('  a `Ameaça` fica SECA do nv%d ao nv%d — %d níveis' % (min(secos), max(secos), len(secos)))

print()
print('=' * 84)
print('O CAMPO — quantas ENTRADAS NOMEADAS um bicho de nível baixo tem?')
print('=' * 84)
for arq, rot in (('srd-2024.json','D&D SRD 2024'), ('srd-2014.json','D&D SRD 2014')):
    d = json.load(open(os.path.join(AQUI, arq), encoding='utf-8'))
    por = defaultdict(list); um_botao = defaultdict(int)
    for m_ in d:
        f = faixa_cr(m_.get('challenge_rating'))
        if not f: continue
        tr, ac = entradas_dnd(m_)
        por[f].append(tr + ac)
        if tr + ac <= 1: um_botao[f] += 1
    print('\n  %s' % rot)
    print('     %-10s %5s %8s %8s %s' % ('faixa','n','mediana','média','com 1 entrada ou menos'))
    for f in ORD_CR:
        if f not in por: continue
        v = por[f]
        print('     %-10s %5d %8.1f %8.2f %d de %d = %.1f%%'
              % (f, len(v), st.median(v), st.mean(v), um_botao[f], len(v), 100*um_botao[f]/len(v)))

# Draw Steel: conta as abilities (🗡/⭐️/🔳) por statblock
G = os.path.join(AQUI, 'dados-recarga-area/data-md-main/Bestiary/Monsters/**/Statblocks/*.md')
arqs = sorted(glob.glob(G, recursive=True))
exige(arqs, 'os statblocks do Draw Steel sumiram')
por = defaultdict(list); um = defaultdict(int)
for f in arqs:
    t = ler(f)
    fm = t.split('---')[1] if t.startswith('---') else ''
    mnv = re.search(r'^level:\s*(\d+)\s*$', fm, re.M)
    if not mnv: continue
    nv = int(mnv.group(1))
    n = len(re.findall(r'^>\s*[🗡⭐️🔳👤🔵]', t, re.M))
    fx = faixa_nv(nv)
    por[fx].append(n)
    if n <= 1: um[fx] += 1
print('\n  Draw Steel (conta 🗡 ⭐️ 🔳 por statblock)')
print('     %-10s %5s %8s %8s %s' % ('faixa','n','mediana','média','com 1 entrada ou menos'))
for f in ORD_NV:
    if f not in por: continue
    v = por[f]
    print('     %-10s %5d %8.1f %8.2f %d de %d = %.1f%%'
          % (f, len(v), st.median(v), st.mean(v), um[f], len(v), 100*um[f]/len(v)))

print()
print('=' * 84)
print('E O CORPO MAIS FRACO DE TODOS — o minion, que é o análogo do `Capanga`')
print('=' * 84)
mini = [ (os.path.basename(f)[:-3], len(re.findall(r'^>\s*[🗡⭐️🔳👤🔵]', ler(f), re.M)))
         for f in arqs if re.search(r'^\s*-\s*.*Minion', ler(f).split('---')[1] if ler(f).startswith('---') else '', re.M | re.I) ]
if mini:
    v = [n for _, n in mini]
    print('  Draw Steel, %d minions: mediana %.1f entradas, média %.2f, mínimo %d, máximo %d'
          % (len(v), st.median(v), st.mean(v), min(v), max(v)))
    print('  com 1 entrada ou menos: %d de %d = %.1f%%'
          % (sum(1 for x in v if x <= 1), len(v), 100*sum(1 for x in v if x <= 1)/len(v)))
    print('  exemplos: %s' % ', '.join('%s(%d)' % m_ for m_ in mini[:5]))

# -*- coding: utf-8 -*-
"""MEDIDA — item `15`, LADO DO INIMIGO: que tamanho de área o campo dá, por nível?

O Mizuki: "nem tudo e' fundamento e tecnica, tem ataques que sao NATURAIS do inimigo e
sao em area, eu queria olhar de ter metrica pra areas maiores, talvez baseado no nv".

Tudo e' convertido pra QUADRADO (1 quadrado = 1,5 m = 5 ft), e a metrica final e'
AREA COBERTA EM QUADRADOS, que e' a unica coisa comparavel entre cone, linha e esfera.

Corpora: SRD 2024 (331) · SRD 2014 (325) · Draw Steel (437 statblocks).
As ancoras do Projeto-M saem do manual (o dono das escadas de area).
"""
import json, re, glob, os, sys, math
import statistics as st
from collections import defaultdict, Counter

AQUI = os.path.dirname(os.path.abspath(__file__))
REPO = "/media/mizuki/HD Externo II/Claude/Claude 2"
GER  = REPO + "/manual/gerador/partC.js"

def ler(p):
    if not os.path.exists(p): sys.exit('DONO SUMIU: %s' % p)
    return open(p, encoding='utf-8').read()
def exige(c, m):
    if not c: sys.exit('ÂNCORA PERDIDA: ' + m)

PE_POR_QUAD = 5.0          # 5 ft = 1 quadrado
M_POR_QUAD  = 1.5          # 1,5 m = 1 quadrado

# ── área coberta, em quadrados, por forma ──────────────────────────────────
def area_cone(L):   return L * L / 2.0          # cone de comprimento L quadrados
def area_burst(R):  return math.pi * R * R      # esfera/emanação de raio R quadrados
def area_linha(L, W): return L * W
def area_cubo(N):   return N * N

FORMAS = [
    (r'(\d+)-foot[- ]long,?\s*(\d+)-foot[- ]wide [Ll]ine', 'linha',
     lambda g: area_linha(int(g[0])/PE_POR_QUAD, int(g[1])/PE_POR_QUAD)),
    (r'(\d+)-foot (?:\w+ )?[Cc]one', 'cone', lambda g: area_cone(int(g[0])/PE_POR_QUAD)),
    (r'(\d+)-foot [Ee]manation', 'emanação', lambda g: area_burst(int(g[0])/PE_POR_QUAD)),
    (r'(\d+)-foot[- ]radius', 'esfera', lambda g: area_burst(int(g[0])/PE_POR_QUAD)),
    (r'(\d+)-foot [Cc]ube', 'cubo', lambda g: area_cubo(int(g[0])/PE_POR_QUAD)),
]

def faixa(cr):
    if cr is None: return None
    if cr <= 1:  return 'CR 0–1'
    if cr <= 4:  return 'CR 2–4'
    if cr <= 10: return 'CR 5–10'
    if cr <= 16: return 'CR 11–16'
    return 'CR 17+'
ORD = ['CR 0–1', 'CR 2–4', 'CR 5–10', 'CR 11–16', 'CR 17+']

TETO_COMBATE = 500      # acima disso nao e' area de combate: e' presenca, covil ou aura de milha

def varre_dnd(arq):
    d = json.load(open(os.path.join(AQUI, arq), encoding='utf-8'))
    por, formas, fora = defaultdict(list), Counter(), []
    for m in d:
        f = faixa(m.get('challenge_rating'))
        if not f: continue
        for a in (m.get('actions') or []):
            t = a.get('desc') or ''
            achou = None
            for rx, nome, fn in FORMAS:
                mm = re.search(rx, t)
                if mm:
                    achou = (nome, fn(mm.groups())); break
            if achou and achou[1] <= TETO_COMBATE:
                por[f].append(achou[1]); formas[achou[0]] += 1
            elif achou:
                fora.append((m['name'], a['name'], achou[1]))
    return por, formas, fora

# ── Draw Steel: burst / cube / line / aura, já em quadrados ────────────────
DS = os.path.join(AQUI, 'dados-recarga-area/data-md-main/Bestiary/Monsters/**/Statblocks/*.md')
def varre_ds():
    arqs = sorted(glob.glob(DS, recursive=True))
    exige(arqs, 'os statblocks do Draw Steel sumiram')
    por, formas = defaultdict(list), Counter()
    for f in arqs:
        t = ler(f)
        fm = t.split('---')[1] if t.startswith('---') else ''
        mn = re.search(r'^level:\s*(\d+)\s*$', fm, re.M)
        if not mn: continue
        nv = int(mn.group(1))
        fx = 'nv 1–3' if nv <= 3 else ('nv 4–6' if nv <= 6 else 'nv 7+')
        for mm in re.finditer(r'📏\s*\**\s*([^*|\n]+)', t):
            d_ = mm.group(1).strip()
            a = None
            m1 = re.search(r'(\d+)\s*[x×]\s*(\d+)\s*(?:line|Line)', d_)
            m2 = re.search(r'[Bb]urst\s+(\d+)', d_)
            m3 = re.search(r'(\d+)\s*[Cc]ube', d_)
            m4 = re.search(r'[Aa]ura\s+(\d+)', d_)
            if   m1: a, k = area_linha(int(m1.group(1)), int(m1.group(2))), 'linha'
            elif m2: a, k = area_burst(int(m2.group(1))), 'burst'
            elif m3: a, k = area_cubo(int(m3.group(1))), 'cubo'
            elif m4: a, k = area_burst(int(m4.group(1))), 'aura'
            if a: por[fx].append(a); formas[k] += 1
    return por, formas

# ── as nossas escadas, lidas do manual ─────────────────────────────────────
def nossas():
    t = ler(GER)
    out = {}
    m = re.search(r'Explosão[^\n]{0,200}?raio\s*(?:de\s*)?(\d+(?:[.,]\d+)?)\s*m', t)
    if m: out['Explosão, raio base'] = float(m.group(1).replace(',', '.'))
    m = re.search(r'Cone[^\n]{0,200}?(\d+(?:[.,]\d+)?)\s*m', t)
    if m: out['Cone, base'] = float(m.group(1).replace(',', '.'))
    return out

# ══════════════════════════════════════════════════════════ saída
L = print
L('=' * 88)
L('A MÉTRICA — área coberta em QUADRADOS (1 quadrado = 1,5 m = 5 ft)')
L('=' * 88)
L('  cone de L quadrados .... L² ÷ 2')
L('  esfera de raio R ....... π R²')
L('  linha L × W ............ L × W')
L('  cubo de N .............. N²')

for arq, rot in (('srd-2024.json', 'D&D SRD 2024'), ('srd-2014.json', 'D&D SRD 2014')):
    por, formas, fora = varre_dnd(arq)
    n = sum(len(v) for v in por.values())
    L(); L('  %s — %d ações em área  (%s)' % (rot, n, ', '.join('%s %d' % x for x in formas.most_common())))
    if fora:
        L('     ⚠ %d fora da conta por passarem de %d quadrados (presença/covil): %s'
          % (len(fora), TETO_COMBATE, ', '.join('%s %.0f' % (x[1], x[2]) for x in sorted(fora, key=lambda y:-y[2])[:3])))
    L('     %-11s %5s %9s %9s %9s' % ('faixa', 'n', 'mediana', 'média', 'máximo'))
    for f in ORD:
        if f not in por: continue
        v = por[f]
        L('     %-11s %5d %9.1f %9.1f %9.1f' % (f, len(v), st.median(v), st.mean(v), max(v)))

por, formas = varre_ds()
n = sum(len(v) for v in por.values())
L(); L('  Draw Steel — %d áreas  (%s)' % (n, ', '.join('%s %d' % x for x in formas.most_common())))
L('     %-11s %5s %9s %9s %9s' % ('faixa', 'n', 'mediana', 'média', 'máximo'))
for f in ('nv 1–3', 'nv 4–6', 'nv 7+'):
    if f not in por: continue
    v = por[f]
    L('     %-11s %5d %9.1f %9.1f %9.1f' % (f, len(v), st.median(v), st.mean(v), max(v)))

L(); L('=' * 88)
L('E A NOSSA — a base que ele chamou de "3m é nada"')
L('=' * 88)
nos = nossas()
exige(nos, 'as escadas de área sumiram do manual/gerador/partC.js')
for k, v in nos.items():
    q = v / M_POR_QUAD
    a = area_burst(q) if 'raio' in k else area_cone(q)
    L('  %-22s %.1f m = %.1f quadrados  ⟹  cobre %.1f quadrados' % (k, v, q, a))


# ── a escada inteira, degrau a degrau ──────────────────────────────────────
L(); L('=' * 88)
L('A NOSSA ESCADA INTEIRA, em quadrados cobertos')
L('=' * 88)
t = ler(GER)
esc_e = re.search(r"'Esfera \(raio\)',\s*'([^']+)'", t)
esc_c = re.search(r"'Cone e Linha',\s*'([^']+)'", t)
def escada(txt):
    return [float(x.replace(',', '.')) for x in re.findall(r'([\d,]+)\s*m', txt)]
for rot, m_, fn in (('Explosão (raio)', esc_e, area_burst), ('Cone (comprimento)', esc_c, area_cone)):
    if not m_:
        L('  ⚠ a escada de %s não foi lida do partC.js' % rot); continue
    vals = escada(m_.group(1))
    L('  %s: %s m' % (rot, ' → '.join('%g' % v for v in vals)))
    L('     em quadrados cobertos: %s'
      % ' → '.join('%.0f' % fn(v / M_POR_QUAD) for v in vals))

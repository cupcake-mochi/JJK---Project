# -*- coding: utf-8 -*-
"""
MEDIR A RECARGA CONTRA A VIDA — quanto uma habilidade de área de uso limitado tira de
um personagem do mesmo nível, em três sistemas, e o que isso dá no Projeto-M.

Pedido do Mizuki, 14/09/2026: "Sukuna Nv30 está para enfrentar um grupo de nv30, pegue
uma média de vida ... e balanceie esse ataque ... Sempre pesquisar e validar ... drawn
steel ... pathfinder".

Corpora (já baixados, ver dados-recarga-area/COMO-RODAR.md):
  D&D 2024 (SRD 5.2) ... classificado-srd2024.json — as áreas com Recharge, dano na falha
  Pathfinder 2e ........ pf2e-habs2.json — as áreas com "again for 1d4 rounds"
  Draw Steel ........... ds-vas2.json — as Villain Actions que pegam mais de um, tier 12-16
Vida de personagem:
  D&D 2024 ... dado de vida das 12 classes do PHB 2024, máximo no 1º nível e média + 1 depois
  PF2e ....... 8 de ancestralidade + (HP da classe + Con) por nível, as 23 classes
  Draw Steel . vida inicial e por nível das 9 classes + bônus do kit por escalão
  Projeto-M .. peça 1 §5.1, os cinco Caminhos × Constituição 0 a 6
As suposições que NÃO saem de documento estão marcadas com SUPOSIÇÃO.
"""
import json, os, re, statistics as st, glob
AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.abspath(os.path.join(AQUI, '..', '..', '..'))
def q(xs, p):
    xs = sorted(xs); k = (len(xs) - 1) * p; i = int(k); j = min(i + 1, len(xs) - 1)
    return xs[i] + (xs[j] - xs[i]) * (k - i)
def resumo(rot, xs):
    if not xs: print(f'  {rot:<34} n=0'); return None
    print(f'  {rot:<34} n={len(xs):<4} mediana {st.median(xs):5.0%}   quartis {q(xs,.25):5.0%} a {q(xs,.75):5.0%}')
    return st.median(xs), q(xs, .25), q(xs, .75)

# ---------------------------------------------------------------- D&D 2024
DADO_2024 = {12: 1, 10: 3, 8: 6, 6: 2}          # Bárbaro · Guerreiro/Paladino/Patrulheiro · 6 d8 · Feiticeiro/Mago
def con_dnd(L): return 2 if L < 8 else 3        # SUPOSIÇÃO: Con +2, e +3 a partir do 8º
def vida_dnd(L):
    tot = sum(n for n in DADO_2024.values())
    return sum(n * (d + con_dnd(L) + (d // 2 + 1 + con_dnd(L)) * (L - 1)) for d, n in DADO_2024.items()) / tot
dnd = []
for x in json.load(open(os.path.join(AQUI, 'classificado-srd2024.json'))):
    if x['mao'] != 'AREA': continue
    m = re.search(r'Failure:\s*(\d+)\s*\(', x['desc'])
    if not m: continue
    L = max(1, min(20, round(x['cr'])))
    dnd.append((x['cr'], int(m.group(1)), vida_dnd(L)))

# ---------------------------------------------------------------- Pathfinder 2e
HP_CLASSE = [8, 12, 8, 10, 8, 8, 10, 8, 8, 8, 8, 8, 10, 8, 6, 10, 8, 6, 10, 10, 8, 6, 6]
def con_pf(L): return 2 if L < 5 else 3 if L < 10 else 4    # SUPOSIÇÃO: Con como atributo secundário
def vida_pf(L): return 8 + (st.mean(HP_CLASSE) + con_pf(L)) * L
def media_dado(txt):
    tot = 0
    for n, f, k in re.findall(r'(\d+)d(\d+)(?:\s*\+\s*(\d+))?', txt):
        tot += int(n) * (int(f) + 1) / 2 + (int(k) if k else 0)
    return tot
pf = []
for x in json.load(open(os.path.join(AQUI, 'pf2e-habs2.json'))):
    if x['cls'] != 'AREA': continue
    frase = re.search(r'deal(?:s|ing)?\s+((?:\d+d\d+(?:\s*\+\s*\d+)?\s*[a-z]*\s*(?:damage)?\s*(?:plus|and)?\s*)+)', x['bloco'])
    if not frase: continue
    dano = media_dado(re.split(r'persistent', frase.group(1))[0])
    if dano <= 0: continue
    pf.append((x['nv'], dano))

# ---------------------------------------------------------------- Draw Steel
CLASSES_DS = []
for f in glob.glob(os.path.join(AQUI, 'dados-recarga-area/data-md-main/Rules/Classes/*.md')):
    t = open(f, encoding='utf-8').read()
    a = re.search(r'Starting Stamina at 1st Level:\*\*\s*(\d+)', t); b = re.search(r'Stamina Gained at 2nd and Higher Levels:\*\*\s*(\d+)', t)
    if a and b: CLASSES_DS.append((int(a.group(1)), int(b.group(1))))
KITS = [int(x) for x in re.findall(r'\*\*Stamina Bonus:\*\*\s*\+(\d+) per echelon', open(os.path.join(AQUI, 'dados-recarga-area/data-md-main/Rules/Chapters/Kits.md'), encoding='utf-8').read())]
def escalao(L): return 1 if L <= 3 else 2 if L <= 6 else 3 if L <= 9 else 4
def vida_ds(L): return st.mean(s + p * (L - 1) for s, p in CLASSES_DS) + st.mean(KITS) * escalao(L)
NIVEL_DS = {}
for f in glob.glob(os.path.join(AQUI, 'dados-recarga-area/data-md-main/Bestiary/Monsters/Monsters/*/Statblocks/*.md')):
    t = open(f, encoding='utf-8').read()
    m = re.search(r'\|\s*Level (\d+)\s*\|', t)
    if m: NIVEL_DS[os.path.basename(f)[:-3]] = (int(m.group(1)), t)
ds = []
for x in json.load(open(os.path.join(AQUI, 'ds-vas2.json'))):
    if x['cls'] != 'MAIS_DE_UM': continue
    m = re.search(r'\*\*12-16:\*\*\s*(\d+)\s+\w*\s*damage', x['bloco'])
    if not m: continue
    nv = next((lv for nome, (lv, t) in NIVEL_DS.items() if x['nome'] in t), None)
    if nv is None: continue
    ds.append((nv, int(m.group(1))))

# ---------------------------------------------------------------- Projeto-M
P01 = open(os.path.join(RAIZ, 'sistema/03-mecanica/01-atributos-acerto-defesa.md'), encoding='utf-8').read()
CAMINHOS = [(n, int(a), int(b)) for n, a, b in re.findall(r'^\| \*\*(\w+)\*\* \| d\d+ \| (\d+) \| (\d+) \|', P01, re.M)]
def vida_m(ini, pn, con, L): return (ini + con) + (pn + con) * (L - 1)
GRADE30 = [vida_m(i, p, c, 30) for _, i, p, c in [(n, i, p, c) for n, i, p in CAMINHOS for c in range(0, 7)]]

print('=' * 96)
print('A RÉGUA DE CADA SISTEMA — dano por alvo na FALHA ÷ a vida média de um personagem do mesmo nível')
print('=' * 96)
print(f'  vida de referência: D&D nv20 {vida_dnd(20):.0f} · PF2e nv20 {vida_pf(20):.0f} · Draw Steel nv10 {vida_ds(10):.0f} '
      f'({len(CLASSES_DS)} classes, {len(KITS)} kits)')
print()
print('  D&D 2024 — áreas com Recharge')
r_d = resumo('   todos os níveis', [d / h for cr, d, h in dnd])
r_d_top = resumo('   o topo: nível de desafio 17+', [d / h for cr, d, h in dnd if cr >= 17])
print('  Pathfinder 2e — áreas com "1d4 rounds"')
resumo('   todos os níveis (criatura = grupo)', [d / vida_pf(min(20, nv)) for nv, d in pf if nv >= 1])
r_p_top = resumo('   o topo: nível 17+ (criatura = grupo)', [d / vida_pf(min(20, nv)) for nv, d in pf if nv >= 17])
r_p_boss = resumo('   o topo, chefe 2 níveis acima', [d / vida_pf(min(20, nv - 2)) for nv, d in pf if nv >= 17])
print('  Draw Steel — Villain Actions em área, resultado 12-16')
resumo('   todos os níveis', [d / vida_ds(min(10, nv)) for nv, d in ds])
r_s_top = resumo('   o topo: nível 8+', [d / vida_ds(min(10, nv)) for nv, d in ds if nv >= 8])
print()
print('=' * 96)
print('O PROJETO-M NO NÍVEL 30 — a vida dos personagens, peça 1 §5.1')
print('=' * 96)
print(f'  {len(CAMINHOS)} Caminhos × Constituição 0 a 6 = {len(GRADE30)} fichas · média {st.mean(GRADE30):.0f} · mediana {st.median(GRADE30):.0f} · '
      f'de {min(GRADE30)} a {max(GRADE30)}')
for n, i, p in CAMINHOS:
    print(f'   {n:<10} Con 0 {vida_m(i,p,0,30):>4} · Con 3 {vida_m(i,p,3,30):>4} · Con 6 {vida_m(i,p,6,30):>4}')
V = st.mean(GRADE30)
print()
print('  a Recarga por alvo que cada régua dá contra a vida média do nível 30:')
for rot, r in (('D&D 2024, topo', r_d_top), ('PF2e, topo', r_p_top), ('PF2e, chefe +2', r_p_boss), ('Draw Steel, topo', r_s_top)):
    if r: print(f'   {rot:<18} mediana {r[0]*V:5.0f}   quartis {r[1]*V:5.0f} a {r[2]*V:5.0f}')

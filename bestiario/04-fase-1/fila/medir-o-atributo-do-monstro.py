# -*- coding: utf-8 -*-
"""
MEDIR O ATRIBUTO DO MONSTRO — o monstro tem atributo maior que o personagem do mesmo nível?
Pergunta do Mizuki, 14/09/2026: "Inimigos em DnD normalmente tem mais atributos que player,
tem alguma metrica pra isso? vale apena a gente usar? os outros sistemas fazem isso tambem?"

Corpora (já baixados): srd-2024.json (D&D 2024, 331 criaturas) · pf2e-recarga.json (PF2e,
677 criaturas com habilidade de recarga — amostra enviesada para chefe) · o repositório do
Draw Steel (416 fichas).

O personagem de referência, e as regras que ele usa:
  D&D 2024 .. conjunto padrão 15·14·13·12·10·8, antecedente +2/+1, e todo aumento de atributo
              nos níveis 4, 8, 12 e 16 e a dádiva do 19 — o TETO do que um personagem chega.
  PF2e ...... atributo-chave +4 no 1, e o aumento parcial acima de +4 nos níveis 5·10·15·20:
              +5 no 10 e +6 no 20. Só o maior atributo (a soma depende demais da classe).
  Draw Steel  (Rules/Classes) dois principais em 2, 3 no 4º, +1 em todos até 4 no 7º, 5 no 10º;
              os outros três no arranjo 1·0·0.
SUPOSIÇÃO marcada onde o número não sai de documento.
"""
import glob, json, os, re, statistics as st
AQUI = os.path.dirname(os.path.abspath(__file__))
def mediana(xs): return st.median(xs) if xs else None

# ---------------------------------------------------------------- D&D 2024
def pc_dnd(L):
    s = [17, 15, 13, 12, 10, 8]                     # 15·14·13·12·10·8 + antecedente +2/+1
    for nv, (i, j) in ((4, (0, 0)), (8, (0, 1)), (12, (1, 1)), (16, (2, 2))):
        if L >= nv:
            s[i] = min(20, s[i] + 1); s[j] = min(20, s[j] + 1)
    if L >= 19: s[0] = min(30, s[0] + 1)
    mods = [(x - 10) // 2 for x in s]
    return max(mods), sum(mods)
dnd = {}
for c in json.load(open(os.path.join(AQUI, 'srd-2024.json'))):
    cr = float(c['challenge_rating']); mods = list(c['modifiers'].values())
    L = max(1, min(20, round(cr))) if cr >= 1 else 1
    dnd.setdefault(L, []).append((max(mods), sum(mods)))

# ---------------------------------------------------------------- PF2e
def pc_pf(L): return 4 if L < 10 else 5 if L < 20 else 6
pf = {}
for c in json.load(open(os.path.join(AQUI, 'pf2e-recarga.json'))):
    m = re.search(r'Str ([+−-]\d+),? Dex ([+−-]\d+),? Con ([+−-]\d+),? Int ([+−-]\d+),? Wis ([+−-]\d+),? Cha ([+−-]\d+)', c['text'])
    if not m or c.get('level') is None: continue
    mods = [int(x.replace('−', '-')) for x in m.groups()]
    pf.setdefault(c['level'], []).append((max(mods), sum(mods)))

# ---------------------------------------------------------------- Draw Steel
def pc_ds(L):
    p = 2 + (L >= 4) + (L >= 7) + (L >= 10)
    o = [1, 0, 0]
    if L >= 7: o = [min(4, x + 1) for x in o]
    return p, 2 * p + sum(o)
ds = {}
for f in glob.glob(os.path.join(AQUI, 'dados-recarga-area/data-md-main/Bestiary/Monsters/Monsters/*/Statblocks/*.md')):
    t = open(f, encoding='utf-8').read()
    lv = re.search(r'\|\s*Level (\d+)\s*\|', t)
    ch = re.findall(r'\*\*([+−-]\d+)\*\*<br/> (Might|Agility|Reason|Intuition|Presence)', t)
    if not lv or len(ch) < 5: continue
    mods = [int(v.replace('−', '-')) for v, _ in ch[:5]]
    ds.setdefault(int(lv.group(1)), []).append((max(mods), sum(mods)))

def faixa(dic, pc, niveis, rot, soma=True):
    print(f'\n{rot}')
    print(f'  {"nível":<8}{"n":>4}{"maior do monstro":>18}{"do personagem":>15}{"diferença":>11}' + (f'{"soma do monstro":>17}{"do personagem":>15}' if soma else ''))
    for a, b in niveis:
        xs = [x for L in range(a, b + 1) for x in dic.get(L, [])]
        if not xs: continue
        mm = mediana([x[0] for x in xs]); ms = mediana([x[1] for x in xs])
        pm, psum = pc(b)[0] if isinstance(pc(b), tuple) else pc(b), (pc(b)[1] if isinstance(pc(b), tuple) else None)
        linha = f'  {a:>2}–{b:<5}{len(xs):>4}{mm:>18g}{pm:>15g}{mm - pm:>+11g}'
        if soma and psum is not None: linha += f'{ms:>17g}{psum:>15g}'
        print(linha)
faixa(dnd, pc_dnd, [(1, 4), (5, 8), (9, 12), (13, 16), (17, 20)], 'D&D 2024 — nível de desafio contra personagem do mesmo nível (o personagem que põe tudo em atributo)')
faixa(pf, pc_pf, [(1, 4), (5, 9), (10, 14), (15, 19), (20, 25)], 'Pathfinder 2e — nível da criatura contra personagem do mesmo nível (só o maior atributo)', soma=False)
faixa(ds, pc_ds, [(1, 3), (4, 6), (7, 9), (10, 11)], 'Draw Steel — nível do monstro contra herói do mesmo nível')

# -*- coding: utf-8 -*-
"""
MEDIR O ALCANCE DO ARTILHEIRO — o alcance da Artilharia do Draw Steel contra o deslocamento
de um herói, para dar metro ao `Artilheiro` da peça 26 §3.4 (v0.231, 14/09/2026).
Corpus: ../fila/dados-recarga-area/data-md-main (o repositório do Draw Steel).
"""
import glob, os, re, statistics as st
AQUI = os.path.dirname(os.path.abspath(__file__))
DS = os.path.join(AQUI, '..', 'fila', 'dados-recarga-area', 'data-md-main')
anc = open(os.path.join(DS, 'Rules', 'Chapters', 'Ancestries.md'), encoding='utf-8').read()
VEL = int(re.search(r'has speed (\d+) and stability', anc).group(1))
rs = []
for f in glob.glob(os.path.join(DS, 'Bestiary', 'Monsters', 'Monsters', '*', 'Statblocks', '*.md')):
    t = open(f, encoding='utf-8').read()
    cab = re.search(r'\|[^\n]*Level (\d+)[^\n]*\|\s*([A-Za-z ]+?)\s*\|', t)
    if not cab or 'Artillery' not in cab.group(2):
        continue
    ds = [int(x) for x in re.findall(r'📏 (?:Melee \d+ or )?[Rr]anged (\d+)', t)]
    if ds:
        rs.append(max(ds))
rs.sort()
med = st.median(rs)
print(f'deslocamento de um herói: {VEL} quadrados')
print(f'Artilharia: n={len(rs)} · mediana {med:.0f} quadrados · quartis {rs[len(rs)//4]} a {rs[3*len(rs)//4]} · de {rs[0]} a {rs[-1]}')
print(f'razão mediana alcance ÷ deslocamento: {med / VEL:.1f}')

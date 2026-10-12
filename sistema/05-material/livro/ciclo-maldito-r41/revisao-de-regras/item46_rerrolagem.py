# -*- coding: utf-8 -*-
"""Item 46: Ritual de Rerrolagem comprado duas vezes. Uma compra: rerrola os d8 que caírem em 1, até Classe + 1 dados.
Segunda compra (proposta): passa a rerrolar também os que caírem em 2, e o limite dobra. Feitiço com 3 x Classe dados.
Ganho = dano esperado a mais, enumerado."""
from math import comb
from fractions import Fraction as F
MED = F(9, 2)
def ganho(n, faces_ruins, teto):
    """n dados; cada um cai numa face ruim com chance len/8; rerrola os piores primeiro, até o teto"""
    # distribuição conjunta de quantos 1 e quantos 2
    total = F(0)
    p1 = F(1, 8); p2 = F(1, 8) if 2 in faces_ruins else F(0); po = 1 - p1 - p2
    for a in range(n + 1):
        for b in range(n - a + 1):
            pr = comb(n, a) * comb(n - a, b) * p1 ** a * p2 ** b * po ** (n - a - b)
            if pr == 0: continue
            ra = min(a, teto); rb = min(b, teto - ra)
            total += pr * (ra * (MED - 1) + rb * (MED - 2))
    return total
print("Classe | dados | 1 compra (só o 1) | 2 compras (1 e 2, limite dobrado) | o que a 2ª acrescenta")
for c in range(1, 8):
    n = 3 * c
    g1 = ganho(n, {1}, c + 1); g2 = ganho(n, {1, 2}, 2 * (c + 1))
    print(f"   {c}   |  {n:>2}   |      +{float(g1):5.2f}        |            +{float(g2):5.2f}                |        +{float(g2 - g1):5.2f}")

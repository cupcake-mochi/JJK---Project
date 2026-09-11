# -*- coding: utf-8 -*-
"""Junta as tres contagens. Cada par (area, alvo unico) vem da saida do script daquele sistema."""
S = [
 # sistema, rotulos totais, area, alvo unico, sem alvo, precisao
 ("D&D 5e SRD 5.2",      86, 70,  12,  4, "exata"),
 ("Draw Steel (VA)",    156,119,   6, 31, "exata"),
 ("Pathfinder 2e",      663,595,  34, 34, "aproximada"),
]
print(f"{'sistema':22s}{'total':>7}{'area':>7}{'unico':>7}{'s/alvo':>8}{'% area*':>9}  precisao")
ta=tu=tt=0
for n,tot,a,u,s,p in S:
    assert a+u+s==tot, f"{n}: {a}+{u}+{s} != {tot}"
    ta+=a; tu+=u; tt+=tot
    print(f"{n:22s}{tot:>7}{a:>7}{u:>7}{s:>8}{100*a/(a+u):>8.1f}%  {p}")
print("-"*68)
mira=ta+tu
print(f"{'TOTAL':22s}{tt:>7}{ta:>7}{tu:>7}{tt-mira:>8}{100*ta/mira:>8.1f}%")
print(f"\n>> Somando os tres sistemas: {ta} de {mira} acoes de recarga que MIRAM ALGUEM sao de AREA")
print(f"   = {100*ta/mira:.1f}%.  Alvo unico: {tu} de {mira} = {100*tu/mira:.1f}%")
print(f"   (de um universo de {tt} rotulos de recarga levantados)")
print(f"\n>> 1 em cada {mira/tu:.0f} acoes de recarga e de alvo unico.")

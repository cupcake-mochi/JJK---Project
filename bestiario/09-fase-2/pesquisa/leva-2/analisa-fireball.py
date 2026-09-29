#!/usr/bin/env python3
"""Le fireball-combates.csv (saida de conta-fireball-rodadas.py) e imprime a distribuicao
de rodadas por combate, com filtros declarados, e as rodadas por numero de PJs e por
PV de monstro por PJ (um indicador grosseiro de dificuldade; nao ha ND nem nivel no dado).
"""
import csv
import os
import statistics as st
from collections import defaultdict

F = os.path.join(os.path.dirname(os.path.abspath(__file__)), "fireball-combates.csv")
rows = list(csv.DictReader(open(F)))
for r in rows:
    for k in ("max_round", "n_pc", "n_monsters", "monster_hp_total", "ended_event", "automation_runs", "state_updates"):
        r[k] = int(float(r[k] or 0))
    r["wallclock_s"] = float(r["wallclock_s"] or 0)


def resumo(nome, R):
    R = sorted(R)
    n = len(R)
    if not n:
        print(nome, "vazio")
        return
    q = lambda p: R[min(n - 1, int(p * n))]
    pct = lambda f: 100.0 * sum(1 for x in R if f(x)) / n
    print(f"{nome}: n={n} media={st.mean(R):.2f} mediana={st.median(R)} p25={q(.25)} p75={q(.75)} p90={q(.90)} "
          f"| 1:{pct(lambda x: x == 1):.0f}% 2:{pct(lambda x: x == 2):.0f}% 3:{pct(lambda x: x == 3):.0f}% "
          f"4:{pct(lambda x: x == 4):.0f}% 5:{pct(lambda x: x == 5):.0f}% >=6:{pct(lambda x: x >= 6):.0f}% "
          f">=8:{pct(lambda x: x >= 8):.0f}% >=10:{pct(lambda x: x >= 10):.0f}%")


print("total de combates:", len(rows))
resumo("F0 todos com rodada>=1", [r["max_round"] for r in rows if r["max_round"] >= 1])
F1 = [r for r in rows if r["max_round"] >= 1 and r["n_pc"] >= 1 and r["n_monsters"] >= 1 and r["automation_runs"] >= 3]
resumo("F1 PJ>=1, monstro>=1, >=3 acoes", [r["max_round"] for r in F1])
F2 = [r for r in F1 if r["ended_event"] == 1]
resumo("F2 = F1 + encerrado com combat_end", [r["max_round"] for r in F2])
F3 = [r for r in F2 if r["max_round"] <= 30]
resumo("F3 = F2 sem >30 rodadas", [r["max_round"] for r in F3])
print("F2 com >30 rodadas:", sum(1 for r in F2 if r["max_round"] > 30))

print("\nRodadas por numero de PJs (F3):")
by = defaultdict(list)
for r in F3:
    by[min(r["n_pc"], 8)].append(r["max_round"])
for k in sorted(by):
    v = by[k]
    print(f"  {k}{'+' if k == 8 else ''} PJs: n={len(v)} media={st.mean(v):.2f} mediana={st.median(v)} >=5:{100*sum(x>=5 for x in v)/len(v):.0f}%")

print("\nRodadas por numero de monstros (F3):")
by = defaultdict(list)
for r in F3:
    by[min(r["n_monsters"], 10)].append(r["max_round"])
for k in sorted(by):
    v = by[k]
    print(f"  {k}{'+' if k == 10 else ''} monstros: n={len(v)} media={st.mean(v):.2f} mediana={st.median(v)}")

print("\nRodadas por PV de monstro por PJ, em quintis (F3, so combates com PV>0):")
G = sorted([r for r in F3 if r["monster_hp_total"] > 0], key=lambda r: r["monster_hp_total"] / r["n_pc"])
n = len(G)
for i in range(5):
    parte = G[i * n // 5:(i + 1) * n // 5]
    hp = [r["monster_hp_total"] / r["n_pc"] for r in parte]
    v = [r["max_round"] for r in parte]
    print(f"  quintil {i+1}: PV/PJ {min(hp):.0f}-{max(hp):.0f} n={len(v)} media={st.mean(v):.2f} mediana={st.median(v)} >=5:{100*sum(x>=5 for x in v)/len(v):.0f}%")

print("\nMinutos de relogio por rodada (F3, mediana; inclui jogo por postagem):")
m = sorted(r["wallclock_s"] / 60 / r["max_round"] for r in F3 if r["wallclock_s"] > 0)
print(f"  mediana={st.median(m):.1f} p25={m[len(m)//4]:.1f} p75={m[3*len(m)//4]:.1f}")
curtos = [r for r in F3 if 0 < r["wallclock_s"] <= 6 * 3600]
resumo("F4 = F3 jogados em ate 6 h de relogio (mesa ao vivo, provavel)", [r["max_round"] for r in curtos])

print("\nCruzamento: rodadas (media / mediana / n) por numero de PJs x monstros por PJ (F3):")
def bpc(n):
    return "1" if n == 1 else "2" if n == 2 else "3-4" if n <= 4 else "5-6" if n <= 6 else "7+"
def bmr(r):
    x = r["n_monsters"] / r["n_pc"]
    return "<=0.5" if x <= 0.5 else "0.5-1" if x <= 1 else "1-2" if x <= 2 else ">2"
cols = ["<=0.5", "0.5-1", "1-2", ">2"]
tab = defaultdict(list)
for r in F3:
    tab[(bpc(r["n_pc"]), bmr(r))].append(r["max_round"])
print("  PJs   | " + " | ".join(f"monstros/PJ {c:>5}" for c in cols))
for p in ["1", "2", "3-4", "5-6", "7+"]:
    cel = []
    for c in cols:
        v = tab.get((p, c), [])
        cel.append(f"{st.mean(v):4.2f}/{st.median(v):>3}/{len(v):>5}" if len(v) >= 30 else f"{'(n<30)':>17}")
    print(f"  {p:>5} | " + " | ".join(cel))

print("\nMonstro unico contra 3+ PJs (F3), por PV do monstro ÷ PJs, em quartis:")
S = sorted([r for r in F3 if r["n_monsters"] == 1 and r["n_pc"] >= 3 and 0 < r["monster_hp_total"] < 100000],
           key=lambda r: r["monster_hp_total"] / r["n_pc"])
n = len(S)
print(f"  n total = {n}")
for i in range(4):
    parte = S[i * n // 4:(i + 1) * n // 4]
    hp = [r["monster_hp_total"] / r["n_pc"] for r in parte]
    v = [r["max_round"] for r in parte]
    print(f"  quartil {i+1}: PV/PJ {min(hp):.0f}-{max(hp):.0f} n={len(v)} media={st.mean(v):.2f} mediana={st.median(v)} >=5:{100*sum(x>=5 for x in v)/len(v):.0f}% >=8:{100*sum(x>=8 for x in v)/len(v):.0f}%")

print("\nCauda por faixa de mediana (F3): quando a mediana sobe, onde ficam p75 e p90?")
grupos = defaultdict(list)
for r in F3:
    grupos[(bpc(r["n_pc"]), bmr(r))].append(r["max_round"])
linhas = []
for k, v in grupos.items():
    if len(v) >= 100:
        v = sorted(v)
        n = len(v)
        linhas.append((st.median(v), v[int(.75 * n)], v[int(.9 * n)], round(st.mean(v), 2), n, k))
for l in sorted(linhas):
    print(f"  mediana {l[0]} | p75 {l[1]} | p90 {l[2]} | media {l[3]} | n {l[4]} | grupo {l[5]}")

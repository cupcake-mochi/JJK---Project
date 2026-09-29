# Conta: no D&D 2024 (SRD 5.2.1 p. 202-203), qual o MAIOR ND de UM monstro sozinho
# que cabe no orçamento de XP de um grupo de N personagens (1 a 6), por dificuldade.
# Fontes: tabela "XP Budget per Character" (SRD 5.2.1 p. 202) e XP por ND (blocos do SRD 5.2.1;
# ND 18 = 20.000 e ND 25-27 = 75.000/90.000/105.000 não aparecem em bloco do SRD e vêm da tabela da p. 256).
xp_nd = {0:10, 0.125:25, 0.25:50, 0.5:100, 1:200, 2:450, 3:700, 4:1100, 5:1800, 6:2300, 7:2900,
         8:3900, 9:5000, 10:5900, 11:7200, 12:8400, 13:10000, 14:11500, 15:13000, 16:15000,
         17:18000, 18:20000, 19:22000, 20:25000, 21:33000, 22:41000, 23:50000, 24:62000,
         25:75000, 26:90000, 27:105000, 28:120000, 29:135000, 30:155000}
budget = {1:(50,75,100), 2:(100,150,200), 3:(150,225,400), 4:(250,375,500), 5:(500,750,1100),
          6:(600,1000,1400), 7:(750,1300,1700), 8:(1000,1700,2100), 9:(1300,2000,2600),
          10:(1600,2300,3100), 11:(1900,2900,4100), 12:(2200,3700,4700), 13:(2600,4200,5400),
          14:(2900,4900,6200), 15:(3300,5400,7800), 16:(3800,6100,9800), 17:(4500,7200,11700),
          18:(5000,8700,14200), 19:(5500,10700,17200), 20:(6400,13200,22000)}
def maior_nd(orc):
    ok = [nd for nd, xp in xp_nd.items() if xp <= orc]
    return max(ok) if ok else None
def fmt(nd):
    return {0.125:'1/8', 0.25:'1/4', 0.5:'1/2'}.get(nd, str(nd))
print("nível | N PJs | baixa | moderada | alta   (maior ND de um monstro sozinho que cabe; ND - nível entre parênteses)")
for nivel in (5, 10, 15, 20):
    for n in range(1, 7):
        cel = []
        for i in range(3):
            nd = maior_nd(budget[nivel][i] * n)
            cel.append(f"ND {fmt(nd)} ({nd - nivel:+g})")
        print(f"{nivel:5d} | {n:5d} | " + " | ".join(cel))
# E o inverso: um monstro de ND = nível, que fração do orçamento ALTA ele consome, por N
print()
print("ND = nível: XP do monstro ÷ orçamento ALTO do grupo")
for nivel in (5, 10, 15, 20):
    linha = []
    for n in range(1, 7):
        linha.append(f"N={n}: {xp_nd[nivel] / (budget[nivel][2]*n):.2f}")
    print(nivel, " ".join(linha))

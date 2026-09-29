# Conta: no PF2e Remaster (GM Core p. 75, AoN Rules.aspx?ID=2716), qual o nível de UMA criatura
# sozinha (relativo ao grupo) que o orçamento de XP comporta, por tamanho de grupo N = 1..6.
# Orçamento = base (grupo de 4) + ajuste por personagem × (N - 4). XP por criatura: -4=10 ... +4=160.
base = {'trivial': (40, 10), 'baixa': (60, 20), 'moderada': (80, 20), 'severa': (120, 30), 'extrema': (160, 40)}
xp_nivel = {-4: 10, -3: 15, -2: 20, -1: 30, 0: 40, 1: 60, 2: 80, 3: 120, 4: 160}
def nivel_que_cabe(orc):
    ok = [d for d, xp in xp_nivel.items() if xp <= orc]
    return max(ok) if ok else None
print("N  | " + " | ".join(f"{k} (orç.)" for k in base))
for n in range(1, 7):
    cel = []
    for k, (b, adj) in base.items():
        orc = b + adj * (n - 4)
        d = nivel_que_cabe(orc)
        sobra = orc - xp_nivel[d] if d is not None else None
        cel.append(f"{'+' if d is not None and d >= 0 else ''}{d} ({orc}; sobra {sobra})")
    print(f"{n}  | " + " | ".join(cel))

# -*- coding: utf-8 -*-
"""Medida das Origens do R46. Tudo sai de conta exata (enumeração de dados), sem sorteio.

CONTRATO, lido do livro R46:
  Maestria: 1 nos níveis 1-9, 2 nos 10-17, 3 nos 18-25, 4 nos 26-30   (tabela de Progressão)
  Classe máxima: 1 (1-4), 2 (5-8), 3 (9-12), 4 (13-16), 5 (17-20), 6 (21-25), 7 (26-30)
  PE máximo = 5 x nível (Vanguarda, Guia) ou 6 x nível (Evocador, Incursor)
  Vida = (8+Con)+(5+Con)(n-1) ou (6+Con)+(4+Con)(n-1)
  Feitiço: custo 3 x Classe PE; pontos 3 x Classe; em dano, cada ponto de saldo vira 1d8
  Paridade: CD 8 + atributo + Maestria contra d20 + atributo + Maestria -> precisa de 8 no dado
  Bloquear = 2d10 + (Defesa - 11)
  Energia Reversa (aptidão, Refino 7 e nível 14): Padrão, 1d8 por PE; como Bônus, 1d4 por PE
"""
from fractions import Fraction as F
from itertools import product
NIVEIS = [2, 10, 18, 26]
def maestria(n): return 1 if n < 10 else 2 if n < 18 else 3 if n < 26 else 4
def classe(n): return 1 if n <= 4 else 2 if n <= 8 else 3 if n <= 12 else 4 if n <= 16 else 5 if n <= 20 else 6 if n <= 25 else 7
ESPACOS = {2: 3, 10: 9, 18: 15, 26: 21}          # coluna Espaços da tabela
CLASSE0 = {2: 2, 10: 3, 18: 5, 26: 5}            # coluna Classe 0
def pct(x): return f"{float(x)*100:5.1f}%"
def pp(x): return f"{float(x)*100:+5.1f}"
D20 = range(1, 21)
PAR = 8                                           # o dado que a paridade pede
def p_ge(k): return F(max(0, min(20, 21 - k)), 20)
base = p_ge(PAR)
print("=" * 78); print("0. A RÉGUA: teste de paridade do livro (precisa de %d no d20)" % PAR); print("=" * 78)
print(f"  chance sem nada: {pct(base)}")
vant = 1 - (1 - base) ** 2
print(f"  com vantagem, ou repetindo a falha: {pct(vant)}  (ganho {pp(vant - base)} pontos)")
for m in (1, 2, 3, 4): print(f"  somando Maestria {m}: {pct(p_ge(PAR - m))}  (ganho {pp(p_ge(PAR - m) - base)})")
d4 = sum(F(1, 20) * F(1, 4) for d in D20 for x in (1, 2, 3, 4) if d + x >= PAR) 
print(f"  somando 1d4: {pct(d4)}  (ganho {pp(d4 - base)})")
conv = sum(F(1, 4) for k in (1, 2, 3, 4) for x in (1, 2, 3, 4) if x >= k) / 4
print(f"     o d4 do Encarnado entra depois do dado: gasto só quando faltou de 1 a 4, ele salva {pct(conv)} dessas falhas")
print(f"  piso 10 (Certeza Momentânea) ou 10 fixo (Fundamento Incorporado): {pct(1)}  (ganho {pp(1 - base)})")

print(); print("=" * 78); print("1. LATENTE — Tentativa e Erro: PE poupados por uso, em média"); print("=" * 78)
for n in NIVEIS:
    m, c = maestria(n), classe(n); var = -(-c // 2); custo = 3 * c
    ruim = sum(F(1, 20) for d in D20 if d + m <= 9); bom = sum(F(1, 20) for d in D20 if d + m >= 14)
    esp = var * (bom - ruim)
    print(f"  nível {n:2d} (Maestria {m}, Classe {c}, feitiço de {custo} PE, variação {var}): desperdício {pct(ruim)}, controle {pct(bom)}, média {float(esp):+.2f} PE por uso = {pct(esp / custo)} do custo")
print("  níveis em que a média é zero:", [n for n in range(1, 31) if maestria(n) == 1][0], "a", [n for n in range(1, 31) if maestria(n) == 1][-1])

print(); print("=" * 78); print("2. RECEPTÁCULO"); print("=" * 78)
for n in NIVEIS:
    print(f"  nível {n:2d}: Coexistência dá 2 feitiços além dos {ESPACOS[n]} espaços (+{pct(F(2, ESPACOS[n])).strip()}); "
          f"Conflito recupera {max(1, n // 2) + 1} a {max(1, n // 2) + 3} PE por dia = {pct(F(max(1, n // 2) + 1, 6 * n)).strip()} a {pct(F(max(1, n // 2) + 3, 5 * n)).strip()} do máximo")

print(); print("=" * 78); print("3. DESCENDENTE — o que cada clã entrega por dia"); print("=" * 78)
p = base; top = sorted
dist = {}
for r in product(D20, repeat=3):
    a = sorted(r, reverse=True); dist[(a[0], a[1])] = dist.get((a[0], a[1]), 0) + F(1, 8000)
p1 = sum(v for (a, b), v in dist.items() if a >= PAR); p2 = sum(v for (a, b), v in dist.items() if b >= PAR)
m1 = sum(a * v for (a, b), v in dist.items()); m2 = sum(b * v for (a, b), v in dist.items())
print(f"  Kamo, Execução Ensaiada: os dois dados guardados valem em média {float(m1):.1f} e {float(m2):.1f}; passam na paridade {pct(p1)} e {pct(p2)}")
print(f"     soma dos dois ganhos sobre o teste comum: {pp((p1 - base) + (p2 - base))} pontos por dia, e você escolhe onde gastar sabendo o valor")
for n in NIVEIS:
    m = maestria(n)
    print(f"  nível {n:2d}: Zenin {m} vantagem(ns) em Atletismo/Acrobacia + 1 TR repetido + 1 Exaustão a menos | "
          f"Kamo 2 dados guardados + {m} acerto(s) repetido(s) | Gojo {m} vantagem(ns) em feitiço da lista + {m} TR(s) repetido(s) com a Reação")
print(f"  repetir depois de errar gasta o uso só quando errou; declarar vantagem antes gasta sempre: por uso gasto, a repetição rende {float(1 / (1 - base)):.1f} vez(es) a vantagem declarada")

print(); print("=" * 78); print("4. HÍBRIDO — Regeneração Orgânica contra a Energia Reversa do livro"); print("=" * 78)
for n in NIVEIS:
    c = classe(n); con = 3; usos = con // 2 + 1
    vida = (8 + con) + (5 + con) * (n - 1); vida2 = (6 + con) + (4 + con) * (n - 1)
    cura = F(7, 2) * c
    print(f"  nível {n:2d}: até {c} PE por uso, cura média {float(cura):4.1f}; com Constituição 3 são {usos} usos por cena = {float(cura * usos):4.1f} PV por {c * usos} PE; "
          f"isso é {pct(cura * usos / vida).strip()} a {pct(cura * usos / vida2).strip()} da vida máxima")
print(f"  por PE: Regeneração {3.5} PV (Ação Bônus, nível 1) | Energia Reversa como Bônus {2.5} PV | como Padrão {4.5} PV (as duas pedem nível 14 e Refino 7)")

print(); print("=" * 78); print("5. CORPO AMALDIÇOADO — reparo no descanso curto"); print("=" * 78)
print(f"  teste em paridade: {pct(base)} de recuperar metade da vida = {pct(base / 2)} da vida máxima por descanso curto, em média")
print(f"  com a repetição diária da Manutenção Precisa: {pct(vant)} = {pct(vant / 2)} da vida máxima")
print(f"  Reparo Autônomo (menor, 1 por dia, Ação Padrão): {pct(base)} de recuperar 30% = {pct(base * F(3, 10))} da vida máxima")

print(); print("=" * 78); print("6. SEM ENERGIA — Ataque sem Prenúncio (2 PE)"); print("=" * 78)
d2 = {}
for a, b in product(range(1, 11), repeat=2): d2[a + b] = d2.get(a + b, 0) + F(1, 100)
def acerto_bloq(need, desv):
    # ataque acerta se d20 - need >= 2d10 - 11 ; need = dado que acertaria a Defesa parada
    tot = F(0)
    for d in D20:
        if desv:
            for s1, q1 in d2.items():
                for s2, q2 in d2.items():
                    if d - need >= min(s1, s2) - 11: tot += F(1, 20) * q1 * q2
        else:
            for s, q in d2.items():
                if d - need >= s - 11: tot += F(1, 20) * q
    return tot
for need in (8, 10, 12):
    print(f"  ataque que acerta a Defesa com {need}+ ({pct(p_ge(need)).strip()}): contra Bloquear normal {pct(acerto_bloq(need, False)).strip()}, contra Bloquear com desvantagem {pct(acerto_bloq(need, True)).strip()}")
print("  (sem contar Aparar e Brecha, que são o duplo 10 e o duplo 1)")
for n in NIVEIS: print(f"  nível {n:2d}: os 2 PE são {pct(F(2, 5 * n)).strip()} a {pct(F(2, 6 * n)).strip()} do máximo", end=" |")
print()

print(); print("=" * 78); print("7. RESTRIÇÃO CORPORAL — Saída Elevada"); print("=" * 78)
for c in range(1, 8):
    extra = max(1, c // 2)
    print(f"  Classe {c}: +{extra} ponto(s) sobre {3 * c} = {pct(F(extra, 3 * c)).strip()} a mais de montagem (em dano, +{extra}d8 se o feitiço compra pelo menos {extra} ponto(s) de Melhoria)")
print(f"  o preço: Defesa 0, e o livro não tem erro automático no 1 natural. Um ataque que acertaria com 10+ ({pct(p_ge(10)).strip()}) passa a acertar {pct(F(1)).strip()} -> {float(1 / p_ge(10)):.2f} vez(es) os acertos")

print(); print("=" * 78); print("8. MENORES QUE AUMENTAM OS PE MÁXIMOS"); print("=" * 78)
MARCOS = [6, 10, 14, 18, 22, 26, 30]
for n, ess in ((2, 2), (10, 3), (18, 4), (26, 5), (30, 6)):
    marcos = sum(1 for x in MARCOS if x <= n)
    nucleo = ess + marcos * (ess // 2); exced = 2 * ess
    print(f"  nível {n:2d}, Essência {ess}: Reserva Excedente +{exced} PE ({pct(F(exced, 5 * n)).strip()} do máximo de 5 por nível) | Núcleo Dependente +{nucleo} PE ({pct(F(nucleo, 5 * n)).strip()})")

print(); print("=" * 78); print("9. PISO 10 uma vez por dia: Certeza Momentânea (Latente) x Fundamento Incorporado (Descendente)"); print("=" * 78)
for need in (6, 8, 10, 11, 13, 15):
    comum = p_ge(need); cert = F(1) if need <= 10 else p_ge(need); fund = F(1) if need <= 10 else F(0)
    print(f"  precisa de {need:2d}: comum {pct(comum)} | Certeza (menor que 10 vira 10) {pct(cert)} | Fundamento (o dado é 10) {pct(fund)}")

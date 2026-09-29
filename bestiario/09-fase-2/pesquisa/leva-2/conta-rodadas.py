#!/usr/bin/env python3
"""Leva 2, agente A — quantas rodadas dura uma luta, pela matemática de cada sistema.

rodadas  = vida do chefe / (N x dano esperado de um personagem por rodada, com a chance de acerto)
pressão  = dano esperado do chefe por rodada (com a chance de acerto dele) x rodadas / (N x vida de um personagem)
vida/rod = dano esperado do chefe por rodada / vida de um personagem (compara com a hipótese de 0,9)

Marcas: [C] texto de regra citado · [F] fonte oficial secundária · [I] conta própria/comunidade.
As notas com cada suposição estão em NOTAS-matematica.md, nesta pasta.
"""
import sys

NS = range(1, 7)


def fmt(x, casas=2):
    if x is None:
        return "  —  "
    return f"{x:.{casas}f}".replace(".", ",")


# ============================================================================================
# 1. PATHFINDER 2e (Remaster)
# ============================================================================================
# [C] GM Core Table 2-7 Hit Points, faixa Moderate — https://2e.aonprd.com/Rules.aspx?ID=2891
PF_HP_MOD = {-1: "8-7", 0: "16-14", 1: "21-19", 2: "32-28", 3: "48-42", 4: "63-57", 5: "78-72",
             6: "99-91", 7: "119-111", 8: "139-131", 9: "159-151", 10: "179-171", 11: "199-191",
             12: "219-211", 13: "239-231", 14: "259-251", 15: "279-271", 16: "299-291", 17: "319-311",
             18: "339-331", 19: "359-351", 20: "379-371", 21: "405-395", 22: "436-424", 23: "466-454",
             24: "508-492"}
# [C] GM Core Table 2-5 Armor Class, coluna High — https://2e.aonprd.com/Rules.aspx?ID=2888
PF_AC_HIGH = {-1: 15, 0: 16, 1: 16, 2: 18, 3: 19, 4: 21, 5: 22, 6: 24, 7: 25, 8: 27, 9: 28, 10: 30,
              11: 31, 12: 33, 13: 34, 14: 36, 15: 37, 16: 39, 17: 40, 18: 42, 19: 43, 20: 45, 21: 46,
              22: 48, 23: 49, 24: 51}
# [C] GM Core Table 2-9 Strike Attack Bonus, coluna High — https://2e.aonprd.com/Rules.aspx?ID=2896
PF_ATK_HIGH = {-1: 8, 0: 8, 1: 9, 2: 11, 3: 12, 4: 14, 5: 15, 6: 17, 7: 18, 8: 20, 9: 21, 10: 23,
               11: 24, 12: 26, 13: 27, 14: 29, 15: 30, 16: 32, 17: 33, 18: 35, 19: 36, 20: 38, 21: 39,
               22: 41, 23: 42, 24: 44}
# [C] GM Core Table 2-10 Strike Damage, coluna High (média entre parênteses) — https://2e.aonprd.com/Rules.aspx?ID=2897
PF_DMG_HIGH = {-1: 3, 0: 5, 1: 6, 2: 9, 3: 12, 4: 14, 5: 16, 6: 18, 7: 20, 8: 22, 9: 24, 10: 26,
               11: 28, 12: 30, 13: 32, 14: 34, 15: 36, 16: 37, 17: 38, 18: 40, 19: 42, 20: 44, 21: 46,
               22: 48, 23: 50, 24: 52}
# [C] GM Core p. 75-76 Tables 10-1/10-2 — https://2e.aonprd.com/Rules.aspx?ID=2716 (e 2717, 2719)
PF_ORC = {"trivial": (40, 10), "baixa": (60, 20), "moderada": (80, 20), "severa": (120, 30), "extrema": (160, 40)}
PF_XP = {-4: 10, -3: 15, -2: 20, -1: 30, 0: 40, 1: 60, 2: 80, 3: 120, 4: 160}
PF_NIVEIS = (3, 10, 20)


def pf_hp(n):
    a, b = PF_HP_MOD[n].split("-")
    return (int(a) + int(b)) / 2


def pf_graus(bonus, cd):
    """Probabilidades (falha crítica, falha, sucesso, crítico) de d20+bonus contra cd, regra do PF2e. [C]"""
    p = [0.0, 0.0, 0.0, 0.0]
    for d in range(1, 21):
        r = d + bonus
        g = 3 if r >= cd + 10 else 2 if r >= cd else 0 if r <= cd - 10 else 1
        if d == 20:
            g = min(3, g + 1)
        if d == 1:
            g = max(0, g - 1)
        p[g] += 1 / 20
    return p


def pf_dano_esperado(bonus, cd, dano, golpes=2, pam=5):
    """Dano esperado de `golpes` Strikes, cada um com -pam cumulativo; crítico dobra. [C] regra, [I] 2 golpes."""
    tot = 0.0
    for i in range(golpes):
        p = pf_graus(bonus - pam * i, cd)
        tot += p[2] * dano + p[3] * 2 * dano
    return tot


def pf_guerreiro(n):
    """Guerreiro de referência [I] sobre regras [C] (Classes.aspx?ID=35 e Rules.aspx?ID=2741)."""
    forca = 4 if n < 10 else 5 if n < 17 else 6 if n < 20 else 7
    con = 2 if n < 5 else 3 if n < 10 else 4 if n < 20 else 5
    prof_arma = 4 if n < 5 else 6 if n < 13 else 8
    potencia = 0 if n < 2 else 1 if n < 10 else 2 if n < 16 else 3
    dados = 1 if n < 4 else 2 if n < 12 else 3 if n < 19 else 4
    espec = 0 if n < 7 else (3 if n < 13 else 4) if n < 15 else (6 if n < 13 else 8)
    prof_arm = 2 if n < 11 else 4 if n < 17 else 6
    pot_ca = 0 if n < 5 else 1 if n < 11 else 2 if n < 18 else 3
    ataque = n + prof_arma + forca + potencia
    dano = dados * 6.5 + forca + espec
    ca = 10 + n + prof_arm + 6 + pot_ca
    pv = 8 + (10 + con) * n
    return dict(ataque=ataque, dano=dano, ca=ca, pv=pv)


def pf_criatura(n):
    return dict(pv=pf_hp(n), ca=PF_AC_HIGH[n], ataque=PF_ATK_HIGH[n], dano=PF_DMG_HIGH[n])


def pf_chefe_nivel(dif, N):
    base, aj = PF_ORC[dif]
    orc = base + aj * (N - 4)
    cabe = [d for d, xp in PF_XP.items() if xp <= orc]
    if not cabe or orc > 160:
        return None, orc
    return max(cabe), orc


def pf_luta(nivel_grupo, delta, N, k=1.0):
    """k criaturas de nível grupo+delta; k>1 = foco, uma de cada vez. Devolve rodadas, pressão, vida/rod."""
    pc = pf_guerreiro(nivel_grupo)
    cr = pf_criatura(nivel_grupo + delta)
    d_pc = pf_dano_esperado(pc["ataque"], cr["ca"], pc["dano"])
    d_cr = pf_dano_esperado(cr["ataque"], pc["ca"], cr["dano"])
    t1 = cr["pv"] / (N * d_pc)
    rodadas = k * t1
    dano_total = d_cr * t1 * k * (k + 1) / 2
    return rodadas, dano_total / (N * pc["pv"]), d_cr / pc["pv"], d_pc, d_cr


def pf_imprimir(out):
    out.append("\n## Pathfinder 2e — chefe sozinho (nível que cabe no orçamento) [C] tabelas, [I] conta")
    for nv in PF_NIVEIS:
        pc = pf_guerreiro(nv)
        out.append(f"\n### nível do grupo {nv} — guerreiro: ataque +{pc['ataque']}, dano/acerto {fmt(pc['dano'],1)}, CA {pc['ca']}, PV {pc['pv']}")
        out.append("dificuldade | " + " | ".join(f"N={N}" for N in NS))
        for dif in PF_ORC:
            cel = []
            for N in NS:
                d, orc = pf_chefe_nivel(dif, N)
                if d is None or nv + d < -1:
                    cel.append("não faz")
                    continue
                r, p, v, _, _ = pf_luta(nv, d, N)
                cel.append(f"{d:+d}: {fmt(r,1)} rod · pressão {fmt(p)} · {fmt(v)} vida/rod")
            out.append(f"{dif} | " + " | ".join(cel))
    out.append("\n## Pathfinder 2e — encontro padrão: orçamento/40 criaturas do nível do grupo, foco [I]")
    for nv in PF_NIVEIS:
        out.append(f"\n### nível do grupo {nv}")
        out.append("dificuldade | " + " | ".join(f"N={N}" for N in NS))
        for dif in PF_ORC:
            base, aj = PF_ORC[dif]
            cel = []
            for N in NS:
                k = (base + aj * (N - 4)) / 40
                if k <= 0:
                    cel.append("não faz")
                    continue
                r, p, v, _, _ = pf_luta(nv, 0, N, k)
                cel.append(f"{fmt(k,2)} cri.: {fmt(r,1)} rod · pressão {fmt(p)}")
            out.append(f"{dif} | " + " | ".join(cel))


def pf_linhas():
    """Linhas (sistema, nível, dificuldade, N, rodadas, pressão, vida/rod) para o resumo."""
    for nv in PF_NIVEIS:
        for dif in PF_ORC:
            for N in NS:
                d, orc = pf_chefe_nivel(dif, N)
                if d is None or nv + d < -1:
                    yield ("PF2e", nv, dif, N, None, None, None)
                    continue
                r, p, v, _, _ = pf_luta(nv, d, N)
                yield ("PF2e", nv, dif, N, r, p, v)



# ============================================================================================
# 2. D&D 2024 (SRD 5.2.1)
# ============================================================================================
# [C] XP Budget per Character, SRD 5.2.1 p. 202 — https://media.dndbeyond.com/compendium-images/srd/5.2/SRD_CC_v5.2.1.pdf
DND_ORC = {3: (150, 225, 400), 10: (1600, 2300, 3100), 17: (4500, 7200, 11700)}
DND_DIFS = ("baixa", "moderada", "alta")
# [F] XP por ND (blocos do SRD 5.2.1; ND 18 e 25-29 da tabela da p. 256 via leva 1)
DND_XP = {0.125: 25, 0.25: 50, 0.5: 100, 1: 200, 2: 450, 3: 700, 4: 1100, 5: 1800, 6: 2300, 7: 2900,
          8: 3900, 9: 5000, 10: 5900, 11: 7200, 12: 8400, 13: 10000, 14: 11500, 15: 13000, 16: 15000,
          17: 18000, 18: 20000, 19: 22000, 20: 25000, 21: 33000, 22: 41000, 23: 50000, 24: 62000,
          25: 75000, 26: 90000, 27: 105000, 28: 120000, 29: 135000, 30: 155000}
# [F] média dos blocos do SRD 5.2 por ND, lidos em https://api.open5e.com/v2/creatures/?document__key=srd-2024
# (331 blocos; conferido o Adult Red Dragon contra o PDF oficial). [I] a média e a rotina de ataque:
# Multiattack (ou o melhor ataque) + ações lendárias que fazem um ataque, 3 usos se sem trava; sem sopro/magia/área.
DND_ND = {  # ND: (n, PV, CA, ataque, dano bruto/rodada se tudo acerta, extra de crítico/rodada)
    0.125: (19, 8.9, 12.58, 3.68, 4.6, 3.5),
    0.25: (32, 14.1, 12.06, 4.09, 6.0, 4.4),
    0.5: (27, 20.9, 12.37, 4.04, 7.3, 5.4),
    1: (27, 28.1, 13.07, 4.56, 10.2, 7.4),
    2: (42, 49.0, 13.19, 5.17, 14.0, 10.3),
    3: (25, 64.1, 14.60, 5.12, 22.6, 17.9),
    4: (16, 79.1, 14.31, 5.94, 25.2, 18.7),
    5: (25, 103.1, 15.12, 7.12, 30.9, 22.1),
    6: (11, 114.9, 15.45, 7.00, 39.5, 29.3),
    7: (6, 133.5, 16.33, 7.67, 40.5, 30.6),
    8: (10, 131.2, 15.80, 7.60, 51.2, 39.0),
    9: (8, 161.6, 16.38, 9.75, 46.1, 33.6),
    10: (6, 181.8, 17.67, 9.17, 55.8, 41.4),
    11: (7, 201.4, 16.86, 9.86, 59.3, 45.8),
    12: (2, 174.0, 17.50, 8.50, 90.0, 74.0),
    13: (6, 200.3, 17.17, 10.83, 91.5, 70.0),
    14: (3, 202.3, 18.33, 10.67, 100.0, 73.5),
    15: (4, 213.2, 18.00, 11.50, 107.8, 81.1),
    16: (5, 232.4, 18.60, 11.40, 104.4, 78.0),
    17: (4, 263.5, 18.75, 13.25, 106.0, 71.1),
    19: (1, 287.0, 19.00, 14.00, 78.0, 63.5),
    20: (3, 334.0, 20.33, 14.00, 137.7, 95.2),
    21: (4, 336.5, 21.00, 14.25, 133.2, 101.5),
    22: (2, 423.0, 21.50, 15.50, 162.0, 112.5),
    23: (3, 476.7, 20.67, 16.67, 130.0, 85.3),
    24: (2, 526.5, 22.00, 17.00, 171.0, 112.5),
    30: (1, 697.0, 25.00, 19.00, 204.0, 134.0),
}
DND_NIVEIS = (3, 10, 17)


def dnd_monstro(nd):
    """Média do ND; com menos de 3 blocos, junta os ND vizinhos pesando por n. [I]"""
    nds = sorted(DND_ND)
    if nd in DND_ND and DND_ND[nd][0] >= 3:
        grupo = [nd]
    else:
        abaixo = [c for c in nds if c < nd][-1:]
        acima = [c for c in nds if c > nd][:1]
        grupo = abaixo + ([nd] if nd in DND_ND else []) + acima
    n = sum(DND_ND[c][0] for c in grupo)
    med = [sum(DND_ND[c][0] * DND_ND[c][i] for c in grupo) / n for i in range(1, 6)]
    return dict(pv=med[0], ca=med[1], ataque=med[2], bruto=med[3], crit=med[4], grupo=grupo)


def dnd_p_acerto(ataque, ca):
    """P(acertar) com d20: 1 natural erra, 20 natural acerta. [C]"""
    precisa = ca - ataque
    return min(0.95, max(0.05, (21 - precisa) / 20))


def dnd_dano_monstro(m, ca_pc):
    return dnd_p_acerto(m["ataque"], ca_pc) * m["bruto"] + 0.05 * m["crit"]


def dnd_guerreiro(n):
    """Guerreiro Campeão do SRD 5.2.1 [I] sobre regras [C]."""
    forca = 3 if n < 4 else 4 if n < 6 else 5
    prof = 2 + (n - 1) // 4
    ataques = 1 if n < 5 else 2 if n < 11 else 3 if n < 20 else 4
    crit_min = 20 if n < 3 else 19 if n < 15 else 18
    ca = (16 if n < 10 else 18) + 1        # cota de malha / placas, +1 do Defense
    pv = 10 + 2 + (n - 1) * (6 + 2)         # Con +2
    return dict(ataque=prof + forca, forca=forca, ataques=ataques, crit_min=crit_min, ca=ca, pv=pv,
                heroico=n >= 10, estudado=n >= 13)


def dnd_dist(ataque, ca, crit_min, vantagem):
    """(P crítico, P acerto sem crítico, P erro) de um ataque. [C]"""
    def um(d):
        if d == 1:
            return 2
        if d >= crit_min:
            return 0
        return 1 if d + ataque >= ca else 2
    p = [0.0, 0.0, 0.0]
    if vantagem:
        for a in range(1, 21):
            for b in range(1, 21):
                p[um(max(a, b))] += 1 / 400
    else:
        for d in range(1, 21):
            p[um(d)] += 1 / 20
    return p


def dnd_dano_guerreiro(pc, ca_alvo):
    """Dano esperado por rodada, com Graze, Studied Attacks e Heroic Inspiration (Markov entre turnos). [I]"""
    dmg = {0: 14 + pc["forca"], 1: 7 + pc["forca"], 2: pc["forca"]}   # crítico, acerto, erro (Graze)
    normal = dnd_dist(pc["ataque"], ca_alvo, pc["crit_min"], False)
    vant = dnd_dist(pc["ataque"], ca_alvo, pc["crit_min"], True)
    p_vant = 0.0            # probabilidade de começar o turno com vantagem (Studied Attacks)
    media = 0.0
    for turno in range(60):
        estados = {(True, pc["heroico"]): p_vant, (False, pc["heroico"]): 1 - p_vant}
        esperado = 0.0
        for _ in range(pc["ataques"]):
            novo = {}
            for (v, insp), pe in estados.items():
                if pe == 0:
                    continue
                for g, pg in enumerate(vant if v else normal):
                    if g == 2 and insp:          # errou e tem Heroic Inspiration: rola de novo
                        for g2, pg2 in enumerate(normal):
                            esperado += pe * pg * pg2 * dmg[g2]
                            k = (g2 == 2 and pc["estudado"], False)
                            novo[k] = novo.get(k, 0) + pe * pg * pg2
                    else:
                        esperado += pe * pg * dmg[g]
                        k = (g == 2 and pc["estudado"], insp)
                        novo[k] = novo.get(k, 0) + pe * pg
            estados = novo
        p_vant = sum(p for (v, _), p in estados.items() if v)
        if turno >= 30:
            media += esperado / 30
    return media


def dnd_chefe_nd(nivel, dif, N):
    orc = DND_ORC[nivel][DND_DIFS.index(dif)] * N
    cabe = [nd for nd, xp in DND_XP.items() if xp <= orc]
    return (max(cabe) if cabe else None), orc


def dnd_luta(nivel, nd, N, k=1.0):
    pc = dnd_guerreiro(nivel)
    m = dnd_monstro(nd)
    d_pc = dnd_dano_guerreiro(pc, m["ca"])
    d_m = dnd_dano_monstro(m, pc["ca"])
    t1 = m["pv"] / (N * d_pc)
    return k * t1, d_m * t1 * k * (k + 1) / 2 / (N * pc["pv"]), d_m / pc["pv"], d_pc, d_m


def dnd_imprimir(out):
    out.append("\n## D&D 2024 — chefe sozinho (maior ND que cabe no orçamento × N) [C] orçamento, [F] blocos, [I] conta")
    for nv in DND_NIVEIS:
        pc = dnd_guerreiro(nv)
        m0 = dnd_monstro(nv)
        out.append(f"\n### nível {nv} — guerreiro: ataque +{pc['ataque']}, {pc['ataques']} ataque(s), CA {pc['ca']}, PV {pc['pv']};"
                   f" contra ND {nv} (CA {fmt(m0['ca'],1)}): {fmt(dnd_dano_guerreiro(pc, m0['ca']),1)} por rodada")
        out.append("dificuldade | " + " | ".join(f"N={N}" for N in NS))
        for dif in DND_DIFS:
            cel = []
            for N in NS:
                nd, orc = dnd_chefe_nd(nv, dif, N)
                if nd is None:
                    cel.append("não faz")
                    continue
                r, p, v, _, _ = dnd_luta(nv, nd, N)
                cel.append(f"ND {nd:g}: {fmt(r,1)} rod · pressão {fmt(p)} · {fmt(v)} vida/rod")
            out.append(f"{dif} | " + " | ".join(cel))
    out.append("\n## D&D 2024 — encontro padrão: orçamento×N ÷ XP de ND = nível, foco [I]")
    for nv in DND_NIVEIS:
        out.append(f"\n### nível {nv}")
        out.append("dificuldade | " + " | ".join(f"N={N}" for N in NS))
        for dif in DND_DIFS:
            cel = []
            for N in NS:
                k = DND_ORC[nv][DND_DIFS.index(dif)] * N / DND_XP[nv]
                r, p, v, _, _ = dnd_luta(nv, nv, N, k)
                cel.append(f"{fmt(k,2)} mon.: {fmt(r,1)} rod · pressão {fmt(p)}")
            out.append(f"{dif} | " + " | ".join(cel))


def dnd_linhas():
    for nv in DND_NIVEIS:
        for dif in DND_DIFS:
            for N in NS:
                nd, orc = dnd_chefe_nd(nv, dif, N)
                if nd is None:
                    yield ("D&D 2024", nv, dif, N, None, None, None)
                    continue
                r, p, v, _, _ = dnd_luta(nv, nd, N)
                yield ("D&D 2024", nv, dif, N, r, p, v)


# ============================================================================================
# 3. DRAW STEEL (MCDM), via Steel Compendium (DRAW STEEL Creator License)
# ============================================================================================
# [C] Monster Basics, fórmulas l. 1297-1382 e hero slots l. 662-681 —
#     https://raw.githubusercontent.com/SteelCompendium/data-bestiary-md/main/Monsters/Chapters/Monster%20Basics.md
# [C] Fury, Kits, Classes — https://github.com/SteelCompendium/data-rules-md
import math

DS_TIER = (0.6, 1.1, 1.4)
DS_DIFS = ("trivial", "fácil", "padrão", "difícil", "extremo")
DS_NIVEIS = (1, 5, 10)
# [C] hero slots: ajuste por dificuldade (padrão +1 se ninguém acima; difícil +1 se nem todos acima)
# Solo = 6 espaços + 1 por nível acima; solo no máximo +1. [I] a leitura célula a célula:
DS_SOLO = {  # (dificuldade, N): níveis acima do grupo, ou None = não faz
    ("padrão", 5): 0, ("padrão", 6): 0,
    ("difícil", 3): 0, ("difícil", 4): 0, ("difícil", 5): 1,
    ("extremo", 1): 0, ("extremo", 2): 0, ("extremo", 3): 1,
}
DS_PELOTAO = {"trivial": -2, "fácil": -1, "padrão": 1, "difícil": 3, "extremo": 4}  # criaturas = N + isto


def ds_escalao(n):
    return 1 if n <= 3 else 2 if n <= 6 else 3 if n <= 9 else 4


def ds_tiers(bonus):
    """P(tier 1, 2, 3) de 2d10 + bonus; 19-20 natural sempre tier 3. [C]"""
    p = [0.0, 0.0, 0.0]
    for a in range(1, 11):
        for b in range(1, 11):
            s = a + b
            t = 2 if s >= 19 else (0 if s + bonus <= 11 else 1 if s + bonus <= 16 else 2)
            p[t] += 1 / 100
    return p


def ds_monstro(nivel, solo=True):
    """[C] fórmulas: Solo papel +30, org ×5 (Vigor), dano +2; pelotão [I] papel médio +20, dano +0."""
    car = min(5, 1 + ds_escalao(nivel) + (1 if solo else 0))
    mod = 2 if solo else 0
    dano = [math.ceil((4 + nivel + mod) * m) + car for m in DS_TIER]
    vigor = (10 * nivel + 30) * 5 if solo else (10 * nivel + 20)
    p = ds_tiers(car)
    por_alvo = sum(pi * di for pi, di in zip(p, dano))
    return dict(vigor=vigor, por_alvo=por_alvo, turnos=2 if solo else 1, alvos=2 if solo else 1)


def ds_furia(nivel):
    """Fúria de referência [I] sobre regras [C]."""
    M = 2 if nivel < 4 else 3 if nivel < 7 else 4 if nivel < 10 else 5
    kit = 2
    p = ds_tiers(M)
    assin = sum(pi * (b + M + kit) for pi, b in zip(p, (3, 6, 9)))            # Brutal Slam
    ferocidade = 2 if nivel < 7 else 3                                          # 1d3 (+1 do 7)
    if nivel < 4:
        heroica = sum(pi * (b + M + kit) for pi, b in zip(p, (7, 11, 16)))     # To the Uttermost End (5)
        extra = ferocidade / 5 * (heroica - assin)
    else:
        extra = min(3, ferocidade) * M                                          # Primordial Strike: surge = +M
    critico = 1 / (1 - 0.03)                                                    # 19-20 natural: ação principal extra
    vigor = 21 + 9 * (nivel - 1) + 6 * ds_escalao(nivel)
    return dict(dano=(assin + extra) * critico, vigor=vigor, M=M)


def ds_luta(nivel, acima, N, k=1.0, solo=True):
    her = ds_furia(nivel)
    m = ds_monstro(nivel + acima, solo)
    d_m = m["turnos"] * m["por_alvo"] * min(m["alvos"], N)
    t1 = m["vigor"] / (N * her["dano"])
    return k * t1, d_m * t1 * k * (k + 1) / 2 / (N * her["vigor"]), d_m / her["vigor"], her["dano"], d_m


def ds_imprimir(out):
    out.append("\n## Draw Steel — solo sozinho (hero slots) [C] fórmulas e espaços, [I] conta")
    for nv in DS_NIVEIS:
        h = ds_furia(nv)
        out.append(f"\n### nível {nv} — Fúria: Might {h['M']}, {fmt(h['dano'],1)} de dano por turno, Vigor {h['vigor']}")
        out.append("dificuldade | " + " | ".join(f"N={N}" for N in NS))
        for dif in DS_DIFS:
            cel = []
            for N in NS:
                a = DS_SOLO.get((dif, N))
                if a is None:
                    cel.append("não faz")
                    continue
                r, p, v, _, _ = ds_luta(nv, a, N)
                cel.append(f"solo {nv + a}: {fmt(r,1)} rod · pressão {fmt(p)} · {fmt(v)} vida/rod")
            out.append(f"{dif} | " + " | ".join(cel))
    out.append("\n## Draw Steel — encontro padrão: N + ajuste criaturas de pelotão do nível, foco [I]")
    for nv in DS_NIVEIS:
        out.append(f"\n### nível {nv}")
        out.append("dificuldade | " + " | ".join(f"N={N}" for N in NS))
        for dif in DS_DIFS:
            cel = []
            for N in NS:
                k = N + DS_PELOTAO[dif]
                if k <= 0:
                    cel.append("não faz")
                    continue
                r, p, v, _, _ = ds_luta(nv, 0, N, k, solo=False)
                cel.append(f"{k} cri.: {fmt(r,1)} rod · pressão {fmt(p)}")
            out.append(f"{dif} | " + " | ".join(cel))


def ds_linhas():
    for nv in DS_NIVEIS:
        for dif in DS_DIFS:
            for N in NS:
                a = DS_SOLO.get((dif, N))
                if a is None:
                    yield ("Draw Steel", nv, dif, N, None, None, None)
                    continue
                r, p, v, _, _ = ds_luta(nv, a, N)
                yield ("Draw Steel", nv, dif, N, r, p, v)


# ============================================================================================
# 4. 13th AGE (1ª edição, Archmage Engine SRD)
# ============================================================================================
# [F] Monster Creation — https://www.13thagesrd.com/monsters/monster-creation/
# nível: (ataque, dano de golpe, PV, CA) — normal, grande (double-strength) e enorme (triple-strength)
T13_NORMAL = {0: (5, 4, 20, 16), 1: (6, 5, 27, 17), 2: (7, 7, 36, 18), 3: (8, 10, 45, 19), 4: (9, 14, 54, 20),
              5: (10, 18, 72, 21), 6: (11, 21, 90, 22), 7: (12, 28, 108, 23), 8: (13, 38, 144, 24),
              9: (14, 50, 180, 25), 10: (15, 58, 216, 26), 11: (16, 70, 288, 27), 12: (17, 90, 360, 28),
              13: (18, 110, 432, 29), 14: (19, 135, 576, 30)}
T13_GRANDE = {0: (5, 9, 41, 16), 1: (6, 10, 54, 17), 2: (7, 14, 72, 18), 3: (8, 21, 90, 19), 4: (9, 28, 108, 20),
              5: (10, 36, 144, 21), 6: (11, 42, 180, 22), 7: (12, 56, 216, 23), 8: (13, 76, 288, 24),
              9: (14, 100, 360, 25), 10: (15, 116, 432, 26), 11: (16, 140, 576, 27), 12: (17, 180, 720, 28),
              13: (18, 220, 864, 29), 14: (19, 270, 1152, 30)}
T13_ENORME = {0: (5, 12, 60, 16), 1: (6, 15, 81, 17), 2: (7, 21, 108, 18), 3: (8, 30, 135, 19), 4: (9, 42, 162, 20),
              5: (10, 54, 216, 21), 6: (11, 63, 270, 22), 7: (12, 84, 324, 23), 8: (13, 114, 432, 24),
              9: (14, 150, 540, 25), 10: (15, 174, 648, 26), 11: (16, 210, 864, 27), 12: (17, 270, 1080, 28),
              13: (18, 330, 1296, 29), 14: (19, 405, 1728, 30)}
T13_TAB = {"normal": T13_NORMAL, "grande": T13_GRANDE, "enorme": T13_ENORME}
# [C] Running the Game, Monster Equivalents — https://www.13thagesrd.com/running-the-game/
# [I] chefe que vale N: (tamanho, níveis acima do "mesmo nível" do escalão)
T13_CHEFE = {1: ("normal", 0), 2: ("grande", 0), 3: ("enorme", 0), 4: ("enorme", 1), 5: ("enorme", 1), 6: ("enorme", 2)}
T13_NIVEIS = (1, 5, 10)


def t13_desloc(nivel):
    return 0 if nivel <= 4 else 1 if nivel <= 7 else 2


def t13_p(atk, ca):
    return min(0.95, max(0.05, (21 - (ca - atk)) / 20))


def t13_guerreiro(n):
    """[C] Fighter do SRD; [I] For +4 (1-6)/+5 (7-10), Con +2, meio +1, arma d10."""
    forca = 4 if n < 7 else 5
    mult_pv = {1: 3, 2: 4, 3: 5, 4: 6, 5: 8, 6: 10, 7: 12, 8: 16, 9: 20, 10: 24}[n]
    mult_atr = 1 if n <= 4 else 2 if n <= 7 else 3
    return dict(ataque=forca + n, acerto=n * 5.5 + forca * mult_atr, erro=n, ca=15 + 1 + n, pv=(8 + 2) * mult_pv)


def t13_dano_pc(pc, ca, rodada):
    esc = min(6, rodada - 1)                     # dado de escalada [C]
    p = t13_p(pc["ataque"] + esc, ca)
    return p * pc["acerto"] + 0.05 * pc["acerto"] + (1 - p) * pc["erro"]


def t13_tempo(alvo, N, pc, ca):
    """Rodada (fracionária) em que o dano somado de N guerreiros chega a `alvo`. [I]"""
    acum, r = 0.0, 0
    while True:
        r += 1
        d = N * t13_dano_pc(pc, ca, r)
        if acum + d >= alvo:
            return r - 1 + (alvo - acum) / d
        acum += d


def t13_luta(nivel, tamanho, acima, N, k=1):
    pc = t13_guerreiro(nivel)
    atk, dano, pv, ca = T13_TAB[tamanho][nivel + t13_desloc(nivel) + acima]
    d_m = t13_p(atk, pc["ca"]) * dano + 0.05 * dano
    tempos = [t13_tempo(i * pv, N, pc, ca) for i in range(1, k + 1)]
    return tempos[-1], d_m * sum(tempos) / (N * pc["pv"]), d_m / pc["pv"], t13_dano_pc(pc, ca, 1), d_m


def t13_imprimir(out):
    out.append("\n## 13th Age — batalha justa (N equivalentes), a única dificuldade do SRD [C] tabelas, [I] conta")
    for nv in T13_NIVEIS:
        pc = t13_guerreiro(nv)
        out.append(f"\n### nível {nv} — guerreiro: ataque +{pc['ataque']} (+ dado de escalada), acerto {fmt(pc['acerto'],1)}, erro {pc['erro']}, CA {pc['ca']}, PV {pc['pv']}")
        cel = []
        for N in NS:
            tam, a = T13_CHEFE[N]
            r, p, v, _, _ = t13_luta(nv, tam, a, N)
            cel.append(f"{tam} nv {nv + t13_desloc(nv) + a}: {fmt(r,1)} rod · pressão {fmt(p)} · {fmt(v)} vida/rod")
        out.append("chefe | " + " | ".join(cel))
        cel = []
        for N in NS:
            r, p, v, _, _ = t13_luta(nv, "normal", 0, N, k=N)
            cel.append(f"{N} normais: {fmt(r,1)} rod · pressão {fmt(p)}")
        out.append("encontro padrão | " + " | ".join(cel))


def t13_linhas():
    for nv in T13_NIVEIS:
        for N in NS:
            tam, a = T13_CHEFE[N]
            r, p, v, _, _ = t13_luta(nv, tam, a, N)
            yield ("13th Age", nv, "justa", N, r, p, v)


# ============================================================================================
# 5. RESUMO: as dificuldades dos sistemas nos cinco degraus do Mizuki [I]
# ============================================================================================
DEGRAUS = ("Capanga", "Ameaça", "Desastre", "Catástrofe", "Calamidade")
HIPOTESE = {"Capanga": 2, "Ameaça": 2.5, "Desastre": 3, "Catástrofe": 4, "Calamidade": 5}
MAPA = {  # [I] alinhamento por ordem de nome e pela descrição de risco de cada livro
    ("PF2e", "trivial"): "Capanga", ("PF2e", "baixa"): "Ameaça", ("PF2e", "moderada"): "Desastre",
    ("PF2e", "severa"): "Catástrofe", ("PF2e", "extrema"): "Calamidade",
    ("D&D 2024", "baixa"): "Ameaça", ("D&D 2024", "moderada"): "Desastre", ("D&D 2024", "alta"): "Catástrofe",
    ("Draw Steel", "trivial"): "Capanga", ("Draw Steel", "fácil"): "Ameaça", ("Draw Steel", "padrão"): "Desastre",
    ("Draw Steel", "difícil"): "Catástrofe", ("Draw Steel", "extremo"): "Calamidade",
    ("13th Age", "justa"): "Desastre",
}


def todas_linhas():
    for g in (pf_linhas, dnd_linhas, ds_linhas, t13_linhas):
        yield from g()


def faixa(v):
    v = [x for x in v if x is not None]
    if not v:
        return "—"
    return f"{fmt(min(v),1)}-{fmt(max(v),1)}"


def faixa2(v):
    v = [x for x in v if x is not None]
    return f"{fmt(min(v))}-{fmt(max(v))}" if v else "—"


def resumo_imprimir(out):
    L = list(todas_linhas())
    out.append("\n## RESUMO — rodadas do chefe sozinho por degrau (todos os níveis de referência) [I]")
    out.append("degrau | hipótese | sistema (dificuldade) | N=1 | N=2 | N=3 | N=4 | N=5 | N=6 | vida/rod em N=4 | pressão em N=4")
    for deg in DEGRAUS:
        for (sis, dif), d in MAPA.items():
            if d != deg:
                continue
            cel = [faixa([x[4] for x in L if x[0] == sis and x[2] == dif and x[3] == N]) for N in NS]
            vr = faixa2([x[6] for x in L if x[0] == sis and x[2] == dif and x[3] == 4])
            pr = faixa2([x[5] for x in L if x[0] == sis and x[2] == dif and x[3] == 4])
            out.append(f"{deg} | {fmt(HIPOTESE[deg],1)} | {sis} ({dif}) | " + " | ".join(cel) + f" | {vr} | {pr}")
    out.append("\n## RESUMO — faixa de rodadas por degrau, juntando os sistemas [I]")
    out.append("degrau | hipótese | N=4, todos os sistemas | N de 1 a 6, todos os sistemas | mediana N=4 | mediana 1-6")
    for deg in DEGRAUS:
        chaves = [k for k, d in MAPA.items() if d == deg]
        v4 = sorted(x[4] for x in L if (x[0], x[2]) in chaves and x[3] == 4 and x[4] is not None)
        vt = sorted(x[4] for x in L if (x[0], x[2]) in chaves and x[4] is not None)
        med = lambda v: (v[len(v) // 2] if len(v) % 2 else (v[len(v) // 2 - 1] + v[len(v) // 2]) / 2) if v else None
        out.append(f"{deg} | {fmt(HIPOTESE[deg],1)} | {faixa(v4)} | {faixa(vt)} | {fmt(med(v4),1)} | {fmt(med(vt),1)}")
    out.append("\n## RESUMO — o que o N faz: rodadas no menor e no maior N que o sistema monta, por nível [I]")
    out.append("sistema | dificuldade | nível | N menor → rodadas | N maior → rodadas | razão")
    for (sis, dif) in MAPA:
        for nv in sorted(set(x[1] for x in L if x[0] == sis)):
            v = [(x[3], x[4]) for x in L if x[0] == sis and x[2] == dif and x[1] == nv and x[4] is not None]
            if len(v) < 2:
                continue
            (n0, r0), (n1, r1) = v[0], v[-1]
            out.append(f"{sis} | {dif} | {nv} | N={n0} → {fmt(r0,1)} | N={n1} → {fmt(r1,1)} | {fmt(r1 / r0, 2)}")

if __name__ == "__main__":
    out = []
    pf_imprimir(out)
    dnd_imprimir(out)
    ds_imprimir(out)
    t13_imprimir(out)
    resumo_imprimir(out)
    print("\n".join(out))

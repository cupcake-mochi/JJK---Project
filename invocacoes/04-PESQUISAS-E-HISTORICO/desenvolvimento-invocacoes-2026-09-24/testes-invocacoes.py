#!/usr/bin/env python3
"""RASCUNHO: bancada determinística do protótipo v0.1; não é motor de combate."""
from copy import deepcopy
from fractions import Fraction
from hashlib import sha256
from pathlib import Path
import json
import shlex

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "02-RASCUNHO-prototipo.md"
SOURCE_HASH = sha256(SOURCE.read_bytes()).hexdigest()
CHECKS = []


def check(name, actual, expected):
    CHECKS.append({"teste": name, "esperado": deepcopy(expected), "obtido": deepcopy(actual),
                   "passou": actual == expected})


def rejected(name, operation):
    try:
        operation()
    except ValueError as exc:
        CHECKS.append({"teste": name, "passou": True, "rejeicao": str(exc)})
    else:
        CHECKS.append({"teste": name, "passou": False, "rejeicao": None})


def require(condition, message):
    if not condition:
        raise ValueError(message)


def spend(bank, *keys):
    # Validação atômica: uma resposta impossível não gasta metade do custo.
    require(all(bank[key] > 0 for key in keys), "recurso já gasto")
    for key in keys:
        bank[key] -= 1


FIXTURES = [
    ("Não-Evocador + 1", 3, [3], ["Guardião"], "isolado"),
    ("Singular", 6, [6], ["Guardião"], "isolado"),
    ("Parceria + 1", 3, [3], ["Predador"], "parceria"),
    ("Parceria + 2", 6, [3, 3], ["Predador", "Controlador"], "parceria"),
    ("Múltiplas + 2", 6, [3, 3], ["Guardião", "Predador"], "multiplas"),
    ("Múltiplas + 3", 6, [2, 2, 2], ["Guardião", "Predador", "Controlador"], "multiplas"),
    ("Múltiplas + 4", 6, [2, 2, 1, 1], ["Guardião", "Predador", "Controlador", "Batedor"], "multiplas"),
]


def state(fixture):
    name, capacity, weights, roles, mode = fixture
    creatures = [{"id": f"C{i + 1}", "papel": role, "peso": weight,
                  "pv": 12 * weight, "pv_max": 12 * weight,
                  "condicoes": {}, "usos": {"sonda": 1}, "ativo": True,
                  "fora_da_cena": False}
                 for i, (weight, role) in enumerate(zip(weights, roles))]
    return {"cenario": name, "capacidade": capacity, "modo": mode,
            "criaturas": creatures, "acoes": {"P": 1, "B": 1, "M": 1},
            "reacoes": {"usuario": 1, "coletiva": 1}, "pe": 20}


def body(s, identity):
    return next(c for c in s["criaturas"] if c["id"] == identity)


def armed(s, identity):
    return identity == "U" or (body(s, identity)["ativo"] and
                                body(s, identity)["papel"] in ("Guardião", "Predador"))


def attack(s, identities, joint=False, dice=None, extras=()):
    dice = dice or ([1, 6] if joint else [2, 6])
    require(not extras, "modo instrumental não concede Ataque Extra/Sequência/Kata")
    require(len(identities) == (2 if joint else 1), "número de ataques não autorizado")
    require(len(set(identities)) == len(identities), "corpos devem ser diferentes")
    require(all(armed(s, identity) for identity in identities), "corpo sem ataque elegível")
    require(dice == ([1, 6] if joint else [2, 6]), "dados instrumentais não podem ser substituídos")
    spend(s["acoes"], *("P", "B") if joint else ("P",))
    return {"corpos": identities, "d20": len(identities),
            "pools_dano_maximos": len(identities), "dados_por_pool": dice,
            "alvos_distintos_maximos": len(identities)}


def move(s, identities, resource="M"):
    require(len(identities) <= 2 and len(set(identities)) == len(identities),
            "cada Movimento reposiciona no máximo dois corpos diferentes")
    require(all(i == "U" or body(s, i)["ativo"] for i in identities), "corpo ausente")
    require(resource in ("M", "B", "P"), "conversão inválida")
    spend(s["acoes"], resource)
    return {"corpos": identities, "distancia_maxima_por_corpo_m": 9,
            "recurso_original": resource}


def manifest(s, identity):
    creature = body(s, identity)
    require(not creature["ativo"] and not creature["fora_da_cena"], "corpo indisponível")
    active = [c for c in s["criaturas"] if c["ativo"]]
    require(len(active) < 4 and sum(c["peso"] for c in active) + creature["peso"] <= s["capacidade"],
            "capacidade excedida")
    require(s["pe"] >= 2, "PE insuficiente")
    spend(s["acoes"], "P")
    s["pe"] -= 2
    creature["ativo"] = True


def retract(s, identity):
    creature = body(s, identity)
    require(creature["ativo"], "corpo ausente")
    require(not ({"Agarrado", "Impedido"} & creature["condicoes"].keys()), "impedimento pendente")
    spend(s["acoes"], "B")
    creature["ativo"] = False


def conserved(before, after):
    for old in before["criaturas"]:
        new = body(after, old["id"])
        for key in ("pv", "condicoes", "usos", "fora_da_cena"):
            require(new[key] == old[key], f"troca alterou {key}")
    require(before["reacoes"] == after["reacoes"], "troca renovou reserva de Reação")


def damage(creature, amount, immediate_heal=0):
    creature["pv"] = max(0, creature["pv"] - amount)
    if creature["pv"] == 0 and immediate_heal:
        # Gatilho já preparado é fornecido pela fixture; não cria uma cura.
        creature["pv"] = min(creature["pv_max"], immediate_heal)
    if creature["pv"] == 0:
        creature["ativo"] = False
        creature["fora_da_cena"] = True


def intercept(s, guardian, target="U", transferred=False):
    require(target == "U" and not transferred, "ataque não pode ser interceptado nesta origem")
    require(guardian["papel"] == "Guardião" and guardian["ativo"], "Guardião indisponível")
    spend(s["reacoes"], "coletiva")
    damage(guardian, 12)


def block(dice, defense=15, attacker_natural=10):
    outcome = "Aparar" if dice == [10, 10] and attacker_natural != 20 else "Brecha" if dice == [1, 1] else "Bloquear"
    return {"dados": dice, "defesa": defense, "resultado": sum(dice) + defense - 11, "evento": outcome}


def control(s, identity, natural):
    creature = body(s, identity)
    require(creature["ativo"] and creature["papel"] == "Controlador", "Controlador indisponível")
    require(s["pe"] >= 1, "PE insuficiente")
    spend(s["acoes"], "P")
    s["pe"] -= 1
    return {"TR_d20": 1, "TR_total": natural + 1, "CD": 12,
            "Derrubado": natural + 1 < 12, "ataques_d20": 0, "pools_dano": 0}


RESULTS = []
for fixture in FIXTURES:
    s = state(fixture)
    name, capacity, weights, roles, mode = fixture
    n = len(weights)
    check(name + ": capacidade", sum(weights), capacity)
    ids = ["C1"] if mode == "isolado" else (["U", "C1"] if mode == "parceria" else ["C1", "C2"])
    turn = attack(s, ids, joint=mode != "isolado")
    movement = move(s, ["U", "C1"])
    check(name + ": ataques", turn["d20"], 1 if mode == "isolado" else 2)
    check(name + ": movimento de dois corpos", len(movement["corpos"]), 2)
    check(name + ": Bônus restante", s["acoes"]["B"], 1 if mode == "isolado" else 0)
    rejected(name + ": terceiro ataque/Padrão adicional", lambda: attack(s, ["C1"]))

    # Inimigos acertam dois ataques não críticos contra C1; Bloquear não gasta Reação.
    s = state(fixture)
    reactions_before = deepcopy(s["reacoes"])
    blocks = [block([6, 6]) for _ in range(2)]
    check(name + ": dois Bloquear", [b["resultado"] for b in blocks], [16, 16])
    check(name + ": Bloquear preserva Reações", s["reacoes"], reactions_before)
    spend(s["reacoes"], "usuario")
    spend(s["reacoes"], "coletiva")
    check(name + ": duas reservas distintas", s["reacoes"], {"usuario": 0, "coletiva": 0})
    rejected(name + ": segunda Reação de criatura", lambda: spend(s["reacoes"], "coletiva"))

    s = state(fixture)
    spend(s["reacoes"], "usuario", "coletiva")  # Resposta Coordenada, elegibilidade fornecida.
    check(name + ": Guia orienta própria criatura", s["reacoes"], {"usuario": 0, "coletiva": 0})
    rejected(name + ": segunda Resposta Coordenada", lambda: spend(s["reacoes"], "usuario", "coletiva"))

    interception = None
    if "Guardião" in roles:
        s = state(fixture)
        guard = next(c for c in s["criaturas"] if c["papel"] == "Guardião")
        intercept(s, guard)
        interception = {"dano_usuario": 0, "dano_guardiao": 12, "novos_d20": 0,
                        "bloquear_transferencia": 0, "reacoes_restantes": deepcopy(s["reacoes"])}
        check(name + ": interceptar preserva Reação do usuário", s["reacoes"]["usuario"], 1)
        rejected(name + ": oportunidade após interceptar", lambda: spend(s["reacoes"], "coletiva"))
        rejected(name + ": resposta após interceptar", lambda: spend(s["reacoes"], "usuario", "coletiva"))
        check(name + ": resposta rejeitada não gasta Reação do Guia", s["reacoes"]["usuario"], 1)

    # Troca na mesma rodada: durações não avançam; relógio é entrada externa.
    s = state(fixture)
    first = body(s, "C1")
    first["pv"] -= 8
    first["condicoes"] = {"Derrubado": {"prazo": "até levantar"}, "Sonda temporal": {"rodadas": 2}}
    first["usos"]["sonda"] = 0
    reserve = deepcopy(first)
    reserve.update(id="R", ativo=False, pv=first["pv_max"], condicoes={}, usos={"sonda": 1})
    s["criaturas"].append(reserve)
    s["reacoes"]["coletiva"] = 0
    before = deepcopy(s)
    retract(s, "C1")
    manifest(s, "R")
    conserved(before, s)
    active_max = sum(c["pv_max"] for c in s["criaturas"] if c["ativo"])
    accessible_hp = sum(c["pv"] for c in s["criaturas"])
    check(name + ": troca preserva PV máximos simultâneos", active_max, 12 * capacity)
    check(name + ": reserva amplia PV acessíveis", accessible_hp, 12 * capacity - 8 + reserve["pv_max"])
    check(name + ": custo troca", [s["acoes"]["P"], s["acoes"]["B"], s["acoes"]["M"], before["pe"] - s["pe"]], [0, 0, 1, 2])
    for field, value in (("pv", first["pv_max"]), ("condicoes", {}), ("usos", {"sonda": 1})):
        bad = deepcopy(s)
        body(bad, "C1")[field] = value
        rejected(name + ": troca não altera " + field, lambda bad=bad: conserved(before, bad))
    bad = deepcopy(s)
    bad["reacoes"]["coletiva"] = 1
    rejected(name + ": troca não reseta Reação", lambda: conserved(before, bad))
    # Relógio externo: uma rodada passa com C1 recolhida e efeito periódico ativo.
    damage(body(s, "C1"), 3)
    body(s, "C1")["condicoes"]["Sonda temporal"]["rodadas"] -= 1
    check(name + ": recolhida continua sofrendo efeito", [body(s, "C1")["pv"], body(s, "C1")["condicoes"]["Sonda temporal"]["rodadas"]], [12 * weights[0] - 11, 1])
    s["acoes"] = {"P": 1, "B": 1, "M": 1}
    s["reacoes"] = {"usuario": 1, "coletiva": 1}  # único reset: próximo turno.
    before_return = deepcopy(s)
    retract(s, "R")
    manifest(s, "C1")
    conserved(before_return, s)
    check(name + ": remanifestar conserva ferida e duração", [body(s, "C1")["pv"], body(s, "C1")["condicoes"]["Sonda temporal"]["rodadas"]], [12 * weights[0] - 11, 1])

    focus = state(fixture)
    focus_log = []
    for hit in range(2):
        active = [c for c in focus["criaturas"] if c["ativo"]]
        if not active:
            focus_log.append({"golpe": hit + 1, "alvo": None})
            continue
        target = min(active, key=lambda c: c["pv"])
        damage(target, 15)
        focus_log.append({"golpe": hit + 1, "alvo": target["id"], "pv_final": target["pv"]})
    expected_focus = {1: [6], 2: [42], 3: [6], 4: [6, 36], 5: [6, 36], 6: [0, 24, 24], 7: [24, 24, 0, 0]}[len(RESULTS) + 1]
    check(name + ": foco 15 + 15", [c["pv"] for c in focus["criaturas"]], expected_focus)

    area = state(fixture)
    for creature in area["criaturas"]:
        damage(creature, 12)
    check(name + ": área 12 individual", [c["pv"] for c in area["criaturas"]], [12 * w - 12 for w in weights])
    for creature in area["criaturas"]:
        if creature["fora_da_cena"]:
            rejected(name + ": zero não volta " + creature["id"], lambda identity=creature["id"]: manifest(area, identity))

    # Entrada com campo vazio, uma Padrão por rodada, sem ataque de chegada.
    entry = state(fixture)
    for creature in entry["criaturas"]:
        creature["ativo"] = False
    for creature in entry["criaturas"]:
        entry["acoes"]["P"] = 1  # início da próxima rodada instrumental.
        manifest(entry, creature["id"])
    check(name + ": custo entrada", 20 - entry["pe"], 2 * n)
    RESULTS.append({"cenario": name, "pesos": weights, "pv_inicial": [12 * w for w in weights],
                    "turno": turn, "movimento": movement,
                    "resposta_inimiga": {"d20_inimigos": 2, "rolagens_bloquear": 2, "d10_bloquear": 4,
                                          "resultados_bloquear": [16, 16], "reacoes_gastas_por_bloquear": 0},
                    "guia": {"reacao_usuario": 1, "reacao_coletiva": 1, "ataques_concedidos": 1},
                    "interceptar": interception, "troca": {"P": 1, "B": 1, "PE": 2, "movimento_disponivel": True,
                    "pv_maximos_em_campo": active_max, "pv_reserva_nova": reserve["pv_max"],
                    "pv_restantes_acessiveis_na_cena": accessible_hp, "ferimento_inicial": 8},
                    "foco": {"eventos": focus_log, "pv_final": [c["pv"] for c in focus["criaturas"]]},
                    "area": {"TR_d20": n + 1, "dano_usuario": 12, "bloquear": 0,
                             "pv_final": [c["pv"] for c in area["criaturas"]]},
                    "entrada": {"Padroes": n, "PE": 2 * n, "ataques_de_chegada": 0}})

# Casos negativos de regra, construídos separadamente das execuções positivas.
for label, kwargs in [("terceiro corpo no conjunto", {"identities": ["U", "C1", "C2"]}),
                      ("arma substitui 1d6 por 2d6", {"dice": [2, 6]}),
                      ("Sequência não autorizada", {"extras": ["Sequência"]}),
                      ("Ataque Extra não autorizado", {"extras": ["Ataque Extra"]})]:
    fresh = state(FIXTURES[4])
    options = {"identities": ["U", "C1"], "joint": True, **kwargs}
    rejected(label, lambda fresh=fresh, options=options: attack(fresh, **options))

MOVEMENT = []
for count in (3, 4, 5):
    s = state(FIXTURES[6])
    identities = ["U", "C1", "C2", "C3", "C4"][:count]
    costs = ["M", "B", "P"][: (count + 1) // 2]
    events = [move(s, identities[i:i + 2], resource=costs[i // 2]) for i in range(0, count, 2)]
    check(f"reposicionar {count}: conversões", len(events), (count + 1) // 2)
    rejected(f"reposicionar {count}: sem Bônus para conjunto", lambda: attack(s, ["U", "C1"], joint=True))
    MOVEMENT.append({"corpos": count, "recursos": costs, "P_restante": s["acoes"]["P"], "eventos": events})
rejected("três corpos em um Movimento", lambda: move(state(FIXTURES[4]), ["U", "C1", "C2"]))
rejected("Batedor não ganha golpe no conjunto", lambda: attack(state(FIXTURES[6]), ["U", "C4"], joint=True))
for label, target, transferred in [("interceptar alvo originalmente criatura", "C2", False),
                                    ("interceptar ataque já transferido", "U", True)]:
    s = state(FIXTURES[4])
    rejected(label, lambda s=s, target=target, transferred=transferred: intercept(s, body(s, "C1"), target, transferred))
    check(label + ": rejeição preserva coletiva", s["reacoes"]["coletiva"], 1)
heal_test = state(FIXTURES[6])
damage(body(heal_test, "C4"), 15, immediate_heal=5)
check("cura imediata preparada evita retirada em zero", [body(heal_test, "C4")["pv"], body(heal_test, "C4")["ativo"], body(heal_test, "C4")["fora_da_cena"]], [5, True, False])

# Limites testados separadamente: quatro corpos, peso total e orçamento energético.
for label, fixture, capacity, reserve_weight, pe in [
    ("quinto corpo com peso ainda disponível", FIXTURES[6], 10, 1, 20),
    ("excesso de peso com só três corpos", FIXTURES[4], 6, 3, 20),
]:
    s = state(fixture)
    s["capacidade"] = capacity  # capacidade 10 é apenas sonda para isolar o teto de corpos.
    reserve = deepcopy(body(s, "C1"))
    reserve.update(id="R", ativo=False, peso=reserve_weight)
    s["criaturas"].append(reserve)
    before = deepcopy(s)
    rejected(label, lambda s=s: manifest(s, "R"))
    check(label + ": não consome recursos", [s["acoes"], s["pe"]], [before["acoes"], before["pe"]])
s = state(FIXTURES[0])
body(s, "C1")["ativo"] = False
s["pe"] = 1
before = deepcopy(s)
rejected("manifestar com só 1 PE", lambda: manifest(s, "C1"))
check("PE insuficiente não gasta Padrão", [s["acoes"], s["pe"]], [before["acoes"], 1])

CONTROLLERS = []
for fixture in FIXTURES:
    if "Controlador" not in fixture[3]:
        continue
    s = state(fixture)
    identity = next(c["id"] for c in s["criaturas"] if c["papel"] == "Controlador")
    result = control(s, identity, natural=10)  # 10 + 1 falha contra 12.
    check(fixture[0] + ": Controlador custa P + 1 PE", [s["acoes"], s["pe"]], [{"P": 0, "B": 1, "M": 1}, 19])
    check(fixture[0] + ": controla sem atacar", [result["TR_d20"], result["Derrubado"], result["ataques_d20"], result["pools_dano"]], [1, True, 0, 0])
    enemy_actions = {"P": 1, "B": 1, "M": 1}
    spend(enemy_actions, "M")
    check(fixture[0] + ": levantar não retira Padrão", enemy_actions, {"P": 1, "B": 1, "M": 0})
    CONTROLLERS.append({"cenario": fixture[0], "corpo": identity, "resolucao": result,
                        "acoes_alvo_depois_de_levantar": enemy_actions})
control_outcomes = [{"d20": die, "Derrubado": control(state(FIXTURES[3]), "C2", die)["Derrubado"]}
                    for die in range(1, 21)]
check("Controlador: falha 50% dos TR +1/CD12", sum(o["Derrubado"] for o in control_outcomes) / 20, 0.5)
s = state(FIXTURES[3])
s["pe"] = 0
before = deepcopy(s)
rejected("Controlador com 0 PE", lambda: control(s, "C2", 10))
check("Controlador sem PE não gasta Padrão", [s["acoes"], s["pe"]], [before["acoes"], 0])
s = state(FIXTURES[4])
spend(s["reacoes"], "usuario", "coletiva")
rejected("Guia nv30: segunda criatura sem coletiva mesmo dispensando Reação do Guia", lambda: spend(s["reacoes"], "coletiva"))

# Reações em cadeias forçadas; critérios de Aparar/Brecha recebidos na revisão.
bank = {"usuario": 1, "coletiva": 1}
spend(bank, "coletiva")  # primeiro duplo 10 de C1 permite contra-atacar.
rejected("segundo Aparar coletivo não contra-ataca", lambda: spend(bank, "coletiva"))
PARRY = {"ataques_inimigos": 2, "bloqueios": [[10, 10], [10, 10]],
         "criticos_naturais_inimigos": 0, "contra_ataques_criatura": 1,
         "total_d20": 3, "total_rolagens_bloquear": 2, "total_d10": 4,
         "pools_dano": 1, "pool_contra_ataque": "2d6 + 3", "inimigo_bloqueia_contra_ataque": False}
check("Aparar duplo 10: uma reação coletiva", bank, {"usuario": 1, "coletiva": 0})
check("duplo 10 contra crítico natural não Aparar", block([10, 10], attacker_natural=20)["evento"], "Bloquear")
check("duplo 1 abre Brecha", block([1, 1])["evento"], "Brecha")
chain = {"usuario": 1, "coletiva": 1, "inimigo": 1}
spend(chain, "inimigo")  # Brecha inicial permite ataque adicional do agressor.
spend(chain, "coletiva")  # segundo ataque é Aparado; criatura contra-ataca.
rejected("Brecha final não reabre cadeia: agressor sem coletiva", lambda: spend(chain, "coletiva"))
BREACH = {"sequencia": ["inimigo ataca C1; Bloquear [1,1]: Brecha",
                         "inimigo gasta sua Reação e ataca C1; Bloquear [10,10]: Aparar",
                         "C1 gasta coletiva e contra-ataca +3; inimigo Bloqueia [1,1]: Brecha",
                         "C1 já gastou coletiva: não ganha outro ataque"],
          "total_d20": 3, "total_rolagens_bloquear": 3, "total_d10": 6, "pools_dano": 2,
          "reacoes_finais": chain}

# Enumeração exata de todos os resultados do d20; expectativa dos d6 é analítica.
PROBABILITIES = []
for defense in (15, 17, 20):
    outcomes = [{"d20": die, "resultado": "critico" if die == 20 else "comum" if die + 4 >= defense else "erro"}
                for die in range(1, 21)]
    ordinary = sum(o["resultado"] == "comum" for o in outcomes)
    critical = sum(o["resultado"] == "critico" for o in outcomes)
    one = Fraction(ordinary, 20) * Fraction(7, 2) + Fraction(critical, 20) * 7
    two = sum(Fraction(14 if o["resultado"] == "critico" else 7 if o["resultado"] == "comum" else 0, 20)
              for o in outcomes)
    check(f"Defesa {defense}: E[2d6] = 2 E[1d6]", float(two), float(one + one))
    PROBABILITIES.append({"defesa": defense, "ataque": 4, "resultados": outcomes,
                          "p_acerto_comum": ordinary / 20, "p_critico": critical / 20,
                          "p_acerto_total": (ordinary + critical) / 20,
                          "E_1d6": float(one), "E_2d6": float(two), "E_dois_golpes_1d6": float(one + one)})
check("Defesa 15: valor exato 3,85", PROBABILITIES[0]["E_2d6"], 3.85)
check("expectativas para Defesas 15/17/20", [p["E_2d6"] for p in PROBABILITIES], [3.85, 3.15, 2.1])
check("probabilidades para Defesas 15/17/20", [p["p_acerto_total"] for p in PROBABILITIES], [0.5, 0.4, 0.25])

# Sonda espacial hipotética: três passagens independentes, sem voo/teleporte.
# Um corpo estacionado obstrui a passagem por premissa exclusiva desta sonda.
# C4 está numa área de espera fora das passagens; não fecha uma quarta rota.
PASSAGES = []
for count, expected_free in ((1, 2), (2, 1), (3, 0), (4, 0)):
    positions = dict(list({"C1": "A", "C2": "B", "C3": "C", "C4": "espera"}.items())[:count])
    free_before = sorted({"A", "B", "C"} - set(positions.values()))
    check(f"passagens: {count} corpos deixam rotas livres", len(free_before), expected_free)
    # Retira C1, ocupante único da passagem A.
    removed = "C1"
    remaining = {identity: route for identity, route in positions.items() if identity != removed}
    free_after = sorted({"A", "B", "C"} - set(remaining.values()))
    check(f"passagens: remover ocupante único com {count} corpos", len(free_after), expected_free + 1)
    passive_cost = {"acoes": 0, "reacoes": 0, "PE": 0}
    check(f"passagens: custo passivo imóvel com {count} corpos", passive_cost, {"acoes": 0, "reacoes": 0, "PE": 0})
    PASSAGES.append({"corpos": count, "passagens_largura_m": 1.5, "posicoes": positions,
                     "C4_em_area_de_espera": count == 4, "rotas_livres_antes": free_before,
                     "ocupante_removido": removed, "rotas_livres_depois": free_after,
                     "custo_passivo_enquanto_imovel": passive_cost})
check("integridade do protótipo durante a execução", sha256(SOURCE.read_bytes()).hexdigest(), SOURCE_HASH)

passed = sum(c["passou"] for c in CHECKS)
output = {"estado": "RASCUNHO", "prototipo_sha256": SOURCE_HASH, "comando": "python3 " + shlex.quote(str(Path(__file__).resolve())),
          "natureza": "bancada procedimental determinística; não motor completo nem certificação de balanceamento",
          "verificacoes": CHECKS, "total": len(CHECKS), "passaram": passed,
          "cenarios": RESULTS, "reposicionamento": MOVEMENT, "aparar": PARRY, "brecha": BREACH,
          "probabilidades": PROBABILITIES,
          "controlador": {"cenarios": CONTROLLERS, "enumeracao_TR": control_outcomes, "p_Derrubado": 0.5},
          "sonda_passagens": {"premissa": "corpo estacionado obstrui passagem; hipótese de ensaio, não traço universal",
                               "resultados": PASSAGES}}
(HERE / "resultados-testes.json").write_text(json.dumps(output, ensure_ascii=False, indent=2) + "\n")
print(json.dumps({"verificacoes": len(CHECKS), "passaram": passed, "falharam": len(CHECKS) - passed}, ensure_ascii=False))
raise SystemExit(0 if passed == len(CHECKS) else 1)

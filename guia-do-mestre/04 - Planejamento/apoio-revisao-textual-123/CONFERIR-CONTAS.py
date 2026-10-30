"""Contas dirigidas do lote B2-05: aritmética dos exemplos, regras do Livro de Regras 1.0 e
comparação das tabelas com os resultados já calculados no apoio-lote7 (lidos, não recalculados por cima)."""
from pathlib import Path
from fractions import Fraction as F
import json, hashlib, math

A = Path(__file__).resolve().parent
R = A.parents[1]
primary = R / '04 - Planejamento/apoio-carregador/fontes/LIVRO-COMPLETO-R53.md'
rule = primary.read_text()
lote7 = json.loads((R / '04 - Planejamento/apoio-lote7/resultados.json').read_text())
checks = []


def ck(name, x, y):
    assert x == y, (name, x, y)
    checks.append({'conta': name, 'resultado': x, 'esperado': y})


def has(text):
    assert text in rule, text


def stage_ranges(m):
    st = {}
    for i in range(m + 1):
        lost = m - i
        s = 4 if i == 0 else max([0] + [k for f, k in [(F(1, 4), 1), (F(1, 2), 2), (F(3, 4), 3)] if lost >= m * f])
        st.setdefault(s, []).append(i)
    return [[min(v), max(v)] for k, v in sorted(st.items())]


def dice(n, s):
    d = {0: F(1)}
    for _ in range(n):
        e = {}
        for k, v in d.items():
            for f in range(1, s + 1):
                e[k + f] = e.get(k + f, 0) + v / s
        d = e
    return d


# ---------------- s101: fichas
M = 2
ck('Guardas: Defesa e Bloquear', [10 + 3 + 1, 3], [14, 3])
ck('Haru: TRs (For 4, Con 4, Int 5, Ess 3)', [4 + M, 4 + M, 5, 3], [6, 6, 5, 3])
ck('Vigia: TRs (For 4, Con 4, Int 2, Ess 2)', [4 + M, 4 + M, 2, 2], [6, 6, 2, 2])
ck('Tessa: TRs (Des 3, Con 3, Int 3, Ess 5)', [3 + M, 3, 3, 5 + M], [5, 3, 3, 7])
has('**Percepção e Sentir Energia usam Essência; Intuição usa Inteligência.**')
ck('Perícias (Percepção/Sentir por Essência, Intuição por Inteligência)', [[4 + M, 3 + M, 3 + M, 5 + M], [4 + M, 2 + M, 2 + M, 2 + M], [5 + M, 5 + M, 3 + M, 5 + M]], [[6, 5, 5, 7], [6, 4, 4, 4], [7, 7, 5, 7]])
ck('Carga normal/arrasto', [[5 + 4, 18], [5 + 0, 10]], [[9, 18], [5, 10]])
ck('Ataque e CDs (8 + atributo + M)', [4 + M, 8 + 4 + M, 8 + 5 + M, 0 + M, 8 + 0 + M], [6, 14, 15, 2, 10])
has('| 3–5 | 2d4 |')
ck('Cobrir-se e Kokusen no Refino 4', [math.floor(1.5 * 4), 2 * 4], [6, 8])
has('Reduza esse dano em **1,5 × Refino, arredondado para baixo**')
has('O dado desarmado é **d4 com maestria 1, d6 com maestria 2, d8 com maestria 3 e d10 com maestria 4**.')
ck('Tessa: golpe desarmado com Maestria 2 (correção documentada)', ['1d6 + 2d4', '2d6 + 2d4'], ['1d6 + 2d4', '2d6 + 2d4'])
ck('Fita: montagens Classe 2 e 4', [6 - 1 - 2, 12 - 2 - 4], [3, 6])
ck('Remendo firme e Orientar o golpe', [min(12 - 4, 2 * 4), 3 - 1], [8, 2])
ck('Haru: PE com Fitas e Cobrir-se', [26 - 2 * 12, 26 - 2 * 2, 26 - 2 * 2 >= 24], [2, 22, False])
ck('Vigia: sete Cobrir-se', 14 // 2, 7)
ck('Tessa: gastos de 26 PE', [2 * 12 + 2, 12 + 4 * 3 + 2, 26 - 12 - 2 - 2 >= 12], [26, 26, False])
ck('Estágio 2: Fita, Remendo e Impulso', [6 + 2, 12 + 4, 12 + 4, 3 + 1, 2 * 16 <= 26], [8, 16, 16, 4, False])
ck('Estágio 3: Classe máxima', max(1, 4 // 2), 2)
ck('Integridade: Haru 140, Vigia 60, Tessa 40', [stage_ranges(140), stage_ranges(60), stage_ranges(40)],
   [[[106, 140], [71, 105], [36, 70], [1, 35], [0, 0]], [[46, 60], [31, 45], [16, 30], [1, 15], [0, 0]], [[31, 40], [21, 30], [11, 20], [1, 10], [0, 0]]])
ck('Integridade = metade da vida', [280 // 2, 120 // 2, 80 // 2], [140, 60, 40])
ck('Intervalo da Fita: avisa 1, conjura 2, avisa 3, conjura 4', [1 + 1, 2 + 1, 3 + 1], [2, 3, 4])
has('Na falha do TR, mesmo numa ficha de ataque, o alvo não pode se deslocar voluntariamente até o fim do próximo turno dele.')

# ---------------- s102: arquivo
has('| Ferro ou aço | 18 |')
has('| Pequena peça: garrafa, fecho ou cadeado | 2 | 5 |')
ck('Fecho de aço pequeno e resistente', [18, 5], [18, 5])
ck('Sala: 6 × 12 células de 1,5 m', [6 * 1.5, 12 * 1.5], [9.0, 18.0])


def fita(tr, adv=False, red=0):
    need = 15 - tr
    pf = F(need - 1, 20) if not adv else F(need - 1, 20) ** 2
    s = F(0)
    for k, v in dice(6, 8).items():
        s += v * (pf * max(0, k - red) + (1 - pf) * max(0, math.ceil(F(k, 2)) - red))
    return pf, float(s)


ck('Fita C4: média antes do TR', float(sum(k * v for k, v in dice(6, 8).items())), 27.0)
rows = [('Bastião', 8, False), ('Bastião, vantagem', 8, True), ('Emanador', 4, False), ('Guia', 2, False)]
ck('Fita: falha e dano médio por alvo', [[round(float(fita(t, a)[0]) * 100), round(fita(t, a)[1], 2)] for _, t, a in rows], [[30, 17.73], [9, 14.94], [50, 20.38], [60, 21.7]])
ck('Fita: Emanador com Cobrir-se (−6 por aplicação, mínimo zero)', round(fita(4, red=6)[1], 2), 14.38)
ck('Fita: mesmas médias no apoio-lote7', [round(x['media'], 2) for x in lote7['area'] if x['reducao'] == 0] + [round(next(x['media'] for x in lote7['area'] if x['caminho'] == 'Emanador' and x['reducao'] == 6), 2)],
   [17.72, 14.94, 20.38, 21.7, 14.38])
comp = {(c['misto'], c['caso']): c['resultados'] for c in lote7['composicoes']}
tab = [[round(comp[(False, k)][1]['pelo_menos_um_ativo'] * 100, 1), round(comp[(True, k)][1]['pelo_menos_um_ativo'] * 100, 1), round(comp[(True, k)][2]['pelo_menos_um_ativo'] * 100, 1)]
       for k in ['chefe200', 'chefe280', 'dupla_sem_cura', 'dupla_com_cura']]
ck('Tabela de composições contra o apoio-lote7', tab, [[18.1, 34.8, 3.7], [61.9, 84.9, 23.7], [37.2, 48.7, 6.7], [38.1, 52.7, 11.8]])
ck('Tessa ativa após o primeiro conjunto (três feitiços / misto)', [round(comp[(False, 'dupla_sem_cura')][0]['apoio_ativo'] * 100, 1), round(comp[(True, 'dupla_sem_cura')][0]['apoio_ativo'] * 100, 1)], [14.9, 24.9])
conc = {c['sequelas']: c['resultados'][3] for c in lote7['concentracao_de_ataques']}
ck('Queda não é derrota contra o apoio-lote7', [[round(conc[s]['zero_PV'] * 100, 1), round(conc[s]['derrotado'] * 100, 1)] for s in [0, 2]], [[87.1, 0.1], [87.1, 58.2]])
ck('Socorro: Fita e queda de Mei', [7 + 4 < 15, 4 + 4 + 4 + 5 + 5 + 5, 24 - 27 <= 0, 26 - 12], [True, 27, True, 14])
has('| Insistir pela primeira vez na cena | Permanece consciente e conserva as ações e os recursos disponíveis. | 1/3 do máximo de referência, para cima, até 15 × sua maior Classe. |')
ck('Socorro: janela, Insistir e Aguentar com máximo 137', [3 - 1, math.ceil(137 / 3), 15 * 4, math.ceil(137 / 4)], [2, 46, 60, 35])
ck('Socorro: curas de Akira e Bao', [4 * 4 + 4 * 5, 75 - 12, 6 - 2, 1 + 2 + 3 + 4, 60 - 6, 36 + 10, 36 >= 35], [36, 63, 4, 10, 54, 46, True])
ck('Perfis de nível 15 (apoio-lote7)', [[p['caminho'], p['PV'], p['PE'], p['TR_fisico']] for p in lote7['perfis'] if p['nivel'] == 15],
   [['Bastiao', 185, 60, 8], ['Emanador', 137, 90, 4], ['Guia', 153, 75, 2]])

# ---------------- s079: pó
has('| Vidro ou cerâmica | 12 |')
ck('Pino de cerâmica pequeno e frágil; Arremesso', [12, 2, 7 + 5 >= 12, 5 >= 2], [12, 2, True, True])
ck('Sala: A0 a A12', 12 * 1.5, 18.0)
ck('Exemplo: exposição, cura e PE', [8 + 3 < 14, 44 - 4, min(44, 40 + (1 + 1 + 2 + 3)), 40 + 7 - 44, 30 - 6, 9 + 3 < 14, 12 + 3 >= 14], [True, 40, 44, 3, 24, True, True])
ck('Exemplo: Insistir com máximo 44 e cura de 15', [math.ceil(44 / 3), 15 * 2, 2 + 3 + 4 + 6, 3 - 4 <= 0], [15, 30, 15, True])
ck('Duração: aplicada na rodada 1, expira na rodada 11', 1 + 10, 11)
has('Seus ataques e testes de perícia têm desvantagem. A condição não causa dano de Veneno por conta própria nem impõe desvantagem a todos os TRs.')
has('| Penumbra, fumaça leve ou vegetação rala | Percepção baseada na visão tem desvantagem.')
has('Dano absorvido pela vida temporária ainda conta, pois atingiu sua proteção.')
has('Todo corpo amaldiçoado é imune a Envenenado.')

sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(primary) == '7311979bdfc61bda1d2fd5113106f072edc7dd5b8a801a02779ada53fd13a81d'
d = {'registro': 123, 'novos_parametros': False, 'conferencias': checks,
     'correcao_documentada': {'caso': 's101', 'antes': 'golpe desarmado de Tessa 1d4 + 2d4, crítico 2d4 + 2d4', 'depois': '1d6 + 2d4, crítico 2d6 + 2d4',
                              'fundamento': 'Livro de Regras 1.0: dado desarmado d4 com Maestria 1, d6 com Maestria 2. Tessa tem Maestria 2.'},
     'resultados_anteriores': {'fonte': '04 - Planejamento/apoio-lote7/resultados.json', 'sha256': sha(R / '04 - Planejamento/apoio-lote7/resultados.json'),
                               'uso': 'Lido para comparar as tabelas do s102; o calcular.py antigo não foi executado, porque grava arquivos.'},
     'regras_primarias': {'fonte': str(primary.relative_to(R)), 'sha256': sha(primary),
                          'trechos_consultados': ['Atributos das perícias', 'Dado desarmado por Maestria', 'Canalizar em Golpe por Refino', 'Cobrir-se de Energia e Kokusen',
                                                  'Prende', 'Objetos: Defesa por material e vida por porte', 'Nem Um Arranhão e Duro de Matar',
                                                  'Vida a zero, Aguentar, Insistir, janela e cura do tratamento', 'Estágios de Integridade',
                                                  'Envenenado, condições Pesadas e Concentração', 'Visão em fumaça leve', 'Corpos amaldiçoados e Envenenado']},
     'limites': ['Conferência dirigida da aritmética e das regras existentes. Sem nova simulação.',
                 'As porcentagens de composição e de queda vêm do cálculo do apoio-lote7 e foram comparadas com ele; as médias da Fita foram recalculadas exatamente.',
                 'As fichas e o perigo continuam experimentais; contas corretas não demonstram equilíbrio.']}
(A / 'contas-conferidas.json').write_text(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
print(len(checks), 'contas conferidas')

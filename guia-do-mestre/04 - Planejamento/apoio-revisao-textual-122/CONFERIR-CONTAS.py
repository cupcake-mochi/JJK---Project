"""Contas dirigidas do lote B2-04: aritmética dos exemplos e regras do Livro de Regras 1.0.

Não cria parâmetros nem simula combates; só refaz as contas que o texto afirma.
"""
from pathlib import Path
from fractions import Fraction as F
import json, hashlib, math

A = Path(__file__).resolve().parent
R = A.parents[1]
primary = R / '04 - Planejamento/apoio-carregador/fontes/LIVRO-COMPLETO-R53.md'
rule = primary.read_text()
checks = []


def ck(name, x, y):
    assert x == y, (name, x, y)
    checks.append({'conta': name, 'resultado': x, 'esperado': y})


def has(text):
    assert text in rule, text
    return True


def col(c):
    return 'ABCDEFGH'.index(c)


def steps(a, b):
    """Passos de 1,5 m entre células, com diagonal custando 1,5 m."""
    return max(abs(col(a[0]) - col(b[0])), abs(int(a[1:]) - int(b[1:])))


def path(*cells):
    for a, b in zip(cells, cells[1:]):
        assert steps(a, b) == 1, (a, b)
    return (len(cells) - 1) * 1.5


def stage_ranges(m):
    st = {}
    for i in range(m + 1):
        lost = m - i
        s = 4 if i == 0 else max([0] + [k for f, k in [(F(1, 4), 1), (F(1, 2), 2), (F(3, 4), 3)] if lost >= m * f])
        st.setdefault(s, []).append(i)
    return [[min(v), max(v)] for k, v in sorted(st.items())]


# ---------------- s072: Doma
ck('Doma: vida e Integridade da construção', [5 + 3 + (3 + 3) * (6 - 1), (5 + 3 + (3 + 3) * (6 - 1)) // 2], [38, 19])
ck('Doma: destruição a partir de 5 PV (excedente 59/60)', [59 - 5, 60 - 5, 59 - 5 > 108 // 2, 60 - 5 > 108 // 2], [54, 55, False, True])
ck('Doma: ataque/CD com M = 1', [4 + 1, 12 + 1], [5, 13])
ck('Doma: estágio 2 sobre especial de Classe 2', 6 + 1 * 2, 8)
ck('Doma: Condução urgente, pontos sem uso', 4 - 2 + 1, 3)
ck('Doma: Dobrar o sino, dados', 4 - 1 - 1 + 1, 3)
ck('Doma: exemplo de condução (9 m a 3 m por passo + 6 m especial)', [9 / 3 * 1.5, 9 / 3 * 1.5 + 6], [4.5, 10.5])
has('O custo normal de entrada é a **maior Classe permitida pelo nível da entidade**')
has('Religar usa o retorno: dobro do PE da entrada, Bônus e metade da vida, onde o corpo está.')
ck('Doma: entrada nível 6 (Classe 2) e religar pelo dobro; metade da vida', [2, 2 * 2, 38 // 2], [2, 4, 19])
ck('Carregador (nível 2, Classe 1), para comparação: entrada e religar', [1, 2 * 1], [1, 2])
has('Fora do combate, a maldição derrotada faz **um TR Espírito contra sua CD de conjuração**')
has('O mestre pode permitir uma tentativa antes da derrota')

# ---------------- s073: Sineiro, retirada e socorro
ck('Ensaio: carga de Rina para o arrasto', round(72 / 12 + 1.3, 1), 7.3)
ck('Ensaio: C0 à caixa e percursos de 9 m', [path('C0', 'C1', 'C2', 'C3', 'C4', 'C5', 'C6'), path('F0', 'E1', 'D2', 'C3', 'C4', 'C5', 'C6'), path('D0', 'C1', 'C2', 'C3', 'C4', 'C5', 'C6')], [9.0, 9.0, 9.0])
ck('Ensaio: arrasto D6→D10 e retorno de Rina com Avançar', [path('D6', 'D7', 'D8', 'D9', 'D10'), path('C10', 'C9', 'C8')], [6.0, 3.0])
ck('Ensaio: separação após o Empurrão (C10 até E10)', steps('C10', 'E10') * 1.5, 3.0)
ck('Ensaio: Sineiro E10→D7 e Rina C8→C4', [path('E10', 'D9', 'D8', 'D7'), path('C8', 'C7', 'C6', 'C5', 'C4')], [4.5, 6.0])
ck('Ensaio: Mei D6 a 3 m de Rina em C4', steps('C4', 'D6') * 1.5, 3.0)


def dist_center_body(cell, body):
    # centro do corpo 2×2 (3 × 3 m) a partir do primeiro espaço da anotação
    bx = (col(body[0]) + 1) * 1.5
    by = (int(body[1:])) * 1.5
    cx = (col(cell[0]) + .5) * 1.5
    cy = (int(cell[1:]) - .5) * 1.5
    return math.hypot(cx - bx, cy - by)


ck('Ensaio: Rina em C10 dentro da zona de D10:E11', dist_center_body('C10', 'D10') <= 3, True)
ck('Ensaio: Mei em D6 dentro e Rina em C4 fora da zona de D7:E8', [dist_center_body('D6', 'D7') <= 3, dist_center_body('C4', 'D7') <= 3], [True, False])
ck('Ensaio: Mei em C11 dentro da zona de D10:E11', dist_center_body('C11', 'D10') <= 3, True)
ck('Ensaio 1: vida do Sineiro', [108 - 11, 97 - 22, 75 - 23], [97, 75, 52])
ck('Ensaio 1: Rina', [65 - math.ceil(12 / 2), 59 - math.ceil(11 / 2)], [59, 53])
ck('Ensaio 1: PE de Mei e Akira', [36 - 6, 30 - 7, 30 - 1 - 1], [30, 23, 28])
ck('Ensaio 1: dados', [5 + 4 + 2, 4 + 4 + 4, 3 + 4 + 4 + 5 + 6, 2 + 4 + 5 + 6 + 6, 3 + 4 + 4], [11, 12, 22, 23, 11])
ck('Ensaio 1: Bloquear 2d10 + 2 e ataque com desvantagem', [4 + 6 + 2, 9 + 5, 9 + 5 >= 12], [12, 14, True])
ck('Ensaio 1: saída de Mei e Rina', [path('D6', 'D5', 'D4', 'D3', 'D2'), path('D2', 'D1', 'D0', 'D-1', 'D-2', 'D-3', 'D-4'), path('C2', 'C1', 'C0', 'C-1')], [6.0, 9.0, 4.5])
ck('Ensaio 2: saída de Mei e Rina', [path('C11', 'C10', 'C9', 'C8', 'C7'), path('C7', 'C6', 'C5', 'C4', 'C3', 'C2', 'C1'), path('C1', 'C0', 'C-1', 'C-2', 'C-3', 'C-4', 'C-5'), path('C10', 'C9', 'C8', 'C7', 'C6', 'C5', 'C4'), path('C4', 'C3', 'C2', 'C1', 'C0', 'C-1', 'C-2')], [6.0, 9.0, 9.0, 9.0, 9.0])
ck('Ensaio 2: Mei C6→C11 com a Bônus convertida', path('C6', 'C7', 'C8', 'C9', 'C10', 'C11'), 7.5)
ck('Ensaio 2: impacto e Cobrir-se (Refino 2)', [6 * 5, math.floor(1.5 * 2), 30 - 3, 30 - 2], [30, 3, 27, 28])
has('Reduza esse dano em **1,5 × Refino, arredondado para baixo**')
ck('Ensaio 2: Insistir e Aguentar com máximo 44', [math.ceil(44 / 3), 15 * 2, math.ceil(44 / 4)], [15, 30, 11])
has('| Insistir pela primeira vez na cena | Permanece consciente e conserva as ações e os recursos disponíveis. | 1/3 do máximo de referência, para cima, até 15 × sua maior Classe. |')
has('| Aguentar | Fica Inconsciente e espera socorro. | 1/4 do máximo de referência, para cima, sem teto. |')
has('A janela começa com **3 rodadas, menos 1 por Sequela que você já tenha**.')
ck('Ensaio 2: PE de Mei e vida do Sineiro', [28 - 7, 97 - 23], [21, 74])
ck('Ensaio 2: distâncias de socorro (C0–C−5 e C0–C11)', [5 * 1.5, 11 * 1.5], [7.5, 16.5])
ck('Ensaio 2: curas e tratamento', [1 + 2 + 3 + 4, 1 + 1 + 2 + 4, 10 + 8, 10 + 8 >= 15, 0 + 18], [10, 8, 18, True, 18])
ck('Ensaio 2: PE de Akira', [30 - 1 - 6, 30 - 1 - 6 - 6], [23, 17])
has('O requisito não é um custo subtraído dessa quantidade.')

# ---------------- s075: Ren e Sora
ck('Dupla: Defesa e Bloquear', [10 + 2 + 1, 2], [13, 2])
ck('Dupla: TRs de Ren (For 4, Con 3, Int 1, Ess 1, M 1)', [4 + 1, 3 + 1, 1, 1], [5, 4, 1, 1])
ck('Dupla: TRs de Sora (Des 2, Con 3, Int 2, Ess 4, M 1)', [2 + 1, 3, 2, 4 + 1], [3, 3, 2, 5])
has('**Percepção e Sentir Energia usam Essência; Intuição usa Inteligência.**')
ck('Dupla: perícias (Percepção/Sentir por Essência, Intuição por Inteligência)', [[4 + 1, 1 + 1, 1 + 1, 1 + 1], [4 + 1, 4 + 1, 2 + 1, 4 + 1]], [[5, 2, 2, 2], [5, 5, 3, 5]])
ck('Dupla: carga normal/arrasto', [[5 + 4, (5 + 4) * 2], [5 + 0, 5 * 2]], [[9, 18], [5, 10]])
ck('Dupla: CD de manobra (8 + Força + M)', [8 + 4 + 1, 8 + 0 + 1], [13, 9])
ck('Dupla: montagens (Fenda, Remendo)', [3 - 1, 6 - 2], [2, 4])
ck('Dupla: Kokusen, limite 2 × Refino', 2 * 2, 4)
ck('Dupla: gastos de Ren (8 PE)', [3 + 3 + 2, 8 - (3 + 2 + 2), 8 - (2 + 2 + 3)], [8, 1, 1])
ck('Dupla: gastos de Sora (12 PE)', [4 * 3, 2 * 6, 2 * 3 + 6, 3 + 2 + 6, 12 - 11], [12, 12, 12, 11, 1])
ck('Dupla: estágio 2 (+1 PE por Classe)', [3 + 1, 3 + 1, 6 + 2], [4, 4, 8])
ck('Dupla: Classe máxima no estágio 3', max(1, 2 // 2), 1)
ck('Dupla: estágios de Integridade, Ren 36', stage_ranges(36), [[28, 36], [19, 27], [10, 18], [1, 9], [0, 0]])
ck('Dupla: estágios de Integridade, Sora 24', stage_ranges(24), [[19, 24], [13, 18], [7, 12], [1, 6], [0, 0]])

# ---------------- s076: confronto
ck('Confronto: Sora F8 a Ren D5', steps('F8', 'D5') * 1.5, 4.5)
ck('Confronto: Empurrão F8→H12 e distância até Ren', [path('F8', 'G9', 'H10', 'H11', 'H12'), steps('H12', 'D5') * 1.5], [6.0, 10.5])
ck('Confronto: Akira F0→F6 e F6–H12', [6 * 1.5, steps('F6', 'H12') * 1.5], [9.0, 9.0])
ck('Confronto: Mei D4 a Sora F8 e Rina C4 a Mei D4', [steps('D4', 'F8') * 1.5, steps('C4', 'D4') * 1.5], [6.0, 1.5])
ck('Confronto: Passo de Ren e retorno de Sora', [path('D5', 'E6', 'F7'), path('H12', 'G11', 'F10', 'F9', 'F8')], [3.0, 6.0])
ck('Confronto: Rina C4→D6 e saída de Ren', [path('C4', 'D5', 'D6'), path('F7', 'G6', 'G5', 'G4', 'F3', 'F2', 'F1'), 2 * 1.5], [3.0, 9.0, 3.0])
ck('Confronto: Akira F6→G12', path('F6', 'G7', 'G8', 'G9', 'G10', 'G11', 'G12'), 9.0)
ck('Confronto: Ren (vida e PE)', [72 - ((11 - 3) - 3), 67 - (11 - 3), 59 - 13, 8 - 2 - 2 - 3], [67, 59, 46, 1])
ck('Confronto: Sora (vida e PE)', [48 - (29 - 3), 22 + 18, 40 - 24, 16 - 21 <= 0, 12 - 3 - 2 - 6], [22, 40, 16, True, 1])
ck('Confronto: Rina', [65 - math.ceil(13 / 2), 58 - math.ceil(11 / 2)], [58, 52])
ck('Confronto: dados', [5 + 4 + 2, 6 + 4 + 3, 6 + 6 + 5 + 6 + 6, 3 + 4 + 5 + 6, 4 + 4 + 3, 5 + 6, 4 + 4 + 5 + 5 + 6, 2 + 3 + 3 + 4 + 4 + 5, 6 + 4 + 3], [11, 13, 29, 18, 11, 11, 24, 21, 13])
ck('Confronto: PE gastos', [(6 + 6) + (6 + 1 + 6 + 1), (2 + 2 + 3) + (3 + 2 + 6)], [26, 18])
ck('Confronto: PE finais de Mei e Akira', [36 - 12, 30 - 14], [24, 16])


def dice(n, s):
    d = {0: F(1)}
    for _ in range(n):
        e = {}
        for k, v in d.items():
            for f in range(1, s + 1):
                e[k + f] = e.get(k + f, 0) + v / s
        d = e
    return d


def spell(n):
    out = {0: F(7, 20)}
    for k, v in dice(n, 8).items():
        out[k] = out.get(k, 0) + v * F(12, 20)
    for k, v in dice(2 * n, 8).items():
        out[k] = out.get(k, 0) + v * F(1, 20)
    return out


def kill(hp):
    p = F(0)
    for a, pa in spell(5).items():
        for b, pb in spell(6).items():
            if a > 0:
                tot = max(0, a - 3) + b
            elif b > 0:
                tot = max(0, b - 3)
            else:
                tot = 0
            if tot >= hp:
                p += pa * pb
    return p


ck('Confronto: chance de derrotar Sora (48) e Ren (67), em %', [round(float(kill(48)) * 100, 1), round(float(kill(67)) * 100, 1)], [23.9, 4.5])


def melee(n8, flat, adv, half, n4=1, nd=8, hit_on=8):
    miss = F(hit_on - 1, 20)
    if adv:
        pmiss = miss ** 2
        pcrit = 1 - F(19, 20) ** 2
    else:
        pmiss, pcrit = miss, F(1, 20)
    phit = 1 - pmiss - pcrit

    def comb(k):
        d = {}
        for a, va in dice(k, nd).items():
            for b, vb in dice(n4, 4).items():
                d[a + b + flat] = d.get(a + b + flat, 0) + va * vb
        return d

    def ev(d, crit):
        s = F(0)
        for k, v in d.items():
            x = math.ceil(F(k, 2)) if half else k
            s += v * ((F(96, 100) * x + F(4, 100) * math.ceil(F(3, 2) * x)) if crit else x)
        return s
    return float(phit * ev(comb(n8), False) + pcrit * ev(comb(2 * n8), True))


ck('Confronto: acerto da espada sem e com vantagem, em %', [65.0, round((1 - (7 / 20) ** 2) * 100, 2)], [65.0, 87.75])
ck('Confronto: dano médio da espada (comum / Impulso / Alicerce / Alicerce e Impulso)',
   [round(melee(1, 4, False, False), 2), round(melee(1, 4, True, False), 2), round(melee(1, 4, False, True), 2), round(melee(1, 4, True, True), 2)],
   [7.39, 10.12, 3.86, 5.28])
ck('Confronto: dano médio desarmado de Sora (+1, 1d4 + 1d4)', round(melee(1, 0, False, False, nd=4, hit_on=12), 2), 2.38)
has('Se tirar **2 × Refino ou menos**, ocorre um Kokusen.')
has('O Kokusen acrescenta **50% ao dano final**.')

sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(primary) == '7311979bdfc61bda1d2fd5113106f072edc7dd5b8a801a02779ada53fd13a81d'
d = {'registro': 122, 'novos_parametros': False, 'conferencias': checks,
     'correcao_documentada': {'caso': 's072', 'antes': 'religar custa Bônus e 2 PE', 'depois': 'religar custa Bônus e 4 PE, o dobro do PE da entrada',
                              'fundamento': 'Livro de Regras 1.0: entrada = maior Classe permitida pelo nível da entidade (nível 6 → 2 PE); retorno e religar = dobro do PE da entrada.'},
     'regras_primarias': {'fonte': str(primary.relative_to(R)), 'sha256': sha(primary),
                          'trechos_consultados': ['Recursos do turno, conversão de ações, Correr, Desengajar e movimento que não provoca', 'Provocar e Olhos Em Mim (provocação inicial e área de 6 m)',
                                                  'Vida a zero, Aguentar, Insistir, janela de socorro e cura do tratamento', 'Estágios de Integridade', 'Cobrir-se de Energia, Canalizar e Kokusen',
                                                  'Abrir Caminho: Executar e Resguardar', 'Atributos de Percepção, Sentir Energia e Intuição',
                                                  'Invocações em campo: entrada, retorno, religar, ciclo e Reação coletiva', 'Domar uma maldição: submissão e tentativa durante o combate',
                                                  'Carregar, Recuo e Escolher']},
     'limites': ['Conferência dirigida da aritmética, das distâncias e das regras existentes. Sem simulação de combate.',
                 'As probabilidades do s076 foram recalculadas por convolução exata, nas mesmas condições declaradas pelo texto; não medem dificuldade.',
                 'As fichas do Sineiro, da domada, de Ren e de Sora continuam experimentais; contas corretas não demonstram equilíbrio.']}
(A / 'contas-conferidas.json').write_text(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
print(len(checks), 'contas conferidas')

"""Contas dirigidas do lote B5-03: Amontoado domado, Escriba, Mula de dobra e Vigia do depósito,
conferidos contra o texto do Livro de Regras 1.0 (R53)."""
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


vida = lambda con, n: 5 + con + (3 + con) * (n - 1)          # entidade comum
vida_corpo = lambda con, n: 5 + con + (4 + con) * (n - 1)    # corpo de criação
desc_livre = {1: 1, 2: 1, 3: 1, 4: 2, 5: 2, 6: 3, 7: 3}
pontos_esp = {1: 2, 2: 4, 3: 6, 4: 9}
leve, media = (lambda c: math.ceil(c / 2)), (lambda c: c)
livre = lambda preco, c: max(1, preco - desc_livre[c])
vagas = lambda n: math.floor((2 + n / 2) / 2)


def destroi(vmax, v, dano):
    return dano >= vmax or (dano - v) > F(vmax, 2)


has('> Com Constituição 2, uma entidade comum de nível 5 tem **7 + 5 × 4 = 27 de vida**. Um corpo de criação do mesmo nível tem **7 + 6 × 4 = 31**.')
has('| Desconto da Família Livre | 1 | 1 | 1 | 2 | 2 | 3 | 3 |')
has('**Reserva máxima = nível da entidade × (1 + um terço da Essência dela, arredondado para baixo).**')
has('O descanso curto recupera um quarto do máximo, arredondado para baixo, com mínimo de 1 PE e sem ultrapassar o máximo.')
has('Para uma especial, divida o custo ao meio. A parcela ímpar fica com você.')
has('A entidade ganha **um no nível 1** e outro nos níveis **6, 10, 14, 18, 22, 26 e 30**.')
has('A entidade conhece **uma básica até o nível 10** e **duas a partir do nível 11**.')
has('| 1–4 | 1 | 1d6 | 2 |')
has('| 13–16 | 4 | 2d6 | 9 |')
has('| Espaços de especiais | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |')
ck('Fórmulas de vida conferem com o exemplo do livro', [vida(2, 5), vida_corpo(2, 5)], [27, 31])
ck('Vagas de especial pela fórmula do Guia = tabela do livro', [vagas(n) for n in [1, 4, 5, 8, 9, 12]], [1, 2, 2, 3, 3, 4])

# ---------------- s052: Amontoado
ck('Amontoado domado: vida, Integridade, reserva', [vida(3, 2), vida(3, 2) // 2, 2 * (1 + 1 // 3)], [14, 7, 2])
ck('Amontoado domado: Defesa e Bloquear (Essência 3 de Nara)', [10 + 1 + 3 // 2, 12 - 11], [12, 1])
ck('Nara: CD e corpos mantidos', [8 + 3 + 1, 3 + 2], [12, 5])
ck('Destruição a partir de 8 PV (máximo 48)', [[d - 8, destroi(48, 8, d)] for d in [12, 32, 33, 48]], [[4, False], [24, False], [25, True], [40, True]])
ck('Depois da doma: +4 direto no corpo Desligado', [4 + 4, 4 + 4 > F(14, 2)], [8, True])
ck('Submissão (Espírito +1 contra CD 12)', [10 + 1 < 12, 11 + 1 < 12], [True, False])
ck('Retorno e especial com reserva vazia', [1 * 2, 14 // 2, math.ceil(3 / 2), 3 // 2, 5 - 2, 3 - 3], [2, 7, 2, 1, 3, 0])
ck('Descanso curto da reserva de 2', max(1, 2 // 4), 1)

# ---------------- s053: Escriba
ck('Escriba nível 5: atributos, vida, Integridade', [0 + 2 + 2 + 3 + 2, vida(2, 5), vida(2, 5) // 2], [9, 27, 13])
ck('Escriba: Defesa, Bloquear, ataque, CD, perícias', [10 + 2 + 4 // 2, 14 - 11, 3 + 1, 8 + 3 + 1, 4 + 3 // 2], [14, 3, 4, 12, 5])
ck('Agulha guiada C1 e C2', [pontos_esp[1] - livre(leve(1), 1), pontos_esp[2] - livre(leve(2), 2)], [1, 3])
ck('Agulha perfurante C2: dados e RD ignorada', [pontos_esp[2] - livre(leve(2), 2) - livre(media(2), 2), 2 * max(1, 2 - 1)], [2, 2])
ck('Pedido de Longe: saldo e alternativa', [4 - 1 - 1 - leve(2), 4 - 1 - leve(2)], [1, 2])
ck('Turno do Escriba', [10 + 6 >= 15, 5 + 4, 9 - max(0, 3 - 2), 8 - 6], [True, 9, 8, 2])
ck('Escriba níveis 6, 8 e 9', [vida(3, 6), vida(3, 6) // 2, vida(3, 8), vida(3, 8) // 2, vida(3, 9), vida(3, 9) // 2], [38, 19, 50, 25, 56, 28])
ck('Agulhas em Classe 3', [pontos_esp[3] - livre(leve(3), 3), pontos_esp[3] - livre(leve(3), 3) - livre(media(3), 3), 2 * (3 - 1)], [5, 3, 4])

# ---------------- s054: Mula
ck('Mula: vida, Integridade, Defesa, capacidade', [vida(3, 2), 7, 10 + 1 + 2 // 2, 5 + 3], [14, 7, 12, 8])
ck('Mula: perícias (4 treinos)', [4 + 1 // 2, 3 + 1, 1 + 1, 1 + 1, 1 + 1], [4, 4, 2, 2, 2])
ck('Passageiro de 72 e 84 kg', [72 // 12 + 1 + 1, 84 // 12 + 1 + 1], [8, 9])
has('**Montar ou desmontar** uma criatura a até 1,5 m custa movimento igual à metade do seu deslocamento, arredondado para baixo em múltiplos de 1,5 m.')
has('o cavaleiro faz **TR Físico CD 10**')
ck('Montar com deslocamento 9 e queda de 6 m', [math.floor(9 / 2 / 1.5) * 1.5, 6 // 3], [4.5, 2])

# ---------------- s055: Vigia
ck('Vigia nível 9', [vida(3, 9), 28, 10 + 2 + 4 // 2, 3 + 1, 8 + 3 + 1, 4 + 3 // 2], [56, 28, 14, 4, 12, 5])
ck('Agulha precisa C3 e C4', [pontos_esp[3] - livre(leve(3), 3), pontos_esp[4] - livre(leve(4), 4), 3 * 4], [5, 8, 12])
ck('Vigia: vida nos níveis 10 a 13', [vida(4, 10), vida(4, 11), vida(4, 12), vida(4, 13)], [72, 79, 86, 93])
ck('Vigia: Integridade nos níveis 10 a 13', [vida(4, n) // 2 for n in [10, 11, 12, 13]], [36, 39, 43, 46])
ck('Vigia nível 10 (Maestria 2): ataque, CD, Intelecto, Agulha precisa', [3 + 2, 8 + 3 + 2, 3 + 2, 3 + 2 + 2], [5, 13, 5, 7])
ck('Talentos: dois CE1 no nível 9, terceiro (até CE2) no 10', [len([x for x in [1, 6, 10] if x <= 9]), len([x for x in [1, 6, 10] if x <= 10])], [2, 3])
has('| 2 ou 3 | 1 PE | 1 ou 2 PE |')
has('| 4 ou 5 | 2 PE | 2 ou 3 PE |')
ck('Carga do talismã nas Classes 3 e 4', [3 - 1, 4 - 2], [2, 2])
ck('Projetos do Vigia', [32 + 16, 24000 + 6000 * 2, 24 + 12, 12000 + 3000 * 2, 4 + 2, 2000 * 2], [48, 36000, 36, 18000, 6, 4000])
ck('Transferência a Mei: Defesa e Bloquear', [10 + 2 + 2 // 2, 13 - 11], [13, 2])
ck('Corpo de criação: vida e corpos mantidos', [vida_corpo(3, 9), vida_corpo(3, 9) // 2, vida_corpo(4, 13), vida_corpo(4, 13) // 2, 4 + 2], [64, 32, 105, 52, 6])

sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(primary) == '7311979bdfc61bda1d2fd5113106f072edc7dd5b8a801a02779ada53fd13a81d'
d = {'registro': 130, 'novos_parametros': False, 'conferencias': checks,
     'regras_primarias': {'fonte': str(primary.relative_to(R)), 'sha256': sha(primary),
                          'trechos_consultados': ['Vida de entidade comum e de corpo de criação', 'Progressão da entidade (básica, pontos da especial, espaços)', 'Talentos da entidade',
                                                  'Desconto de Família Livre das entidades', 'Reserva própria, divisão de custo e descanso curto', 'Queda, destruição e retorno',
                                                  'Carga de talismã', 'Combate montado', 'Domar uma maldição']},
     'limites': ['Conferência dirigida da aritmética e da presença literal das regras citadas. Sem simulação.',
                 'Amontoado domado, Escriba, Mula e Vigia continuam exemplos experimentais; Retrato de referência e Albarda de papel são propostas de talento.']}
(A / 'contas-conferidas.json').write_text(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
print(len(checks), 'contas conferidas')

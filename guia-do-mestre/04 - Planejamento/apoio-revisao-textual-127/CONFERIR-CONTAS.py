"""Contas dirigidas do lote B4-01: Ofícios, ferramentas, Anel de Testemunho, Cofre e venda,
Pastilha e Limiar, conferidas contra o texto do Livro de Regras 1.0 (R53)."""
from pathlib import Path
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


# ---------------- s034
has('> **Exemplo:** Rina é treinada em Arrombamento, tem Destreza 4, Inteligência 2 e Maestria 1. Numa tranca mecânica, seu bônus é **+5**.')
has('exige tecido e fechos de **¥3.000**, ferramentas e **4 horas de trabalho**')
ck('Ofícios: bônus de Rina e alvo contra CD 14', [4 + 1, 2 + 1, 14 - 5, 14 - 3], [5, 3, 9, 11])
ck('Etiquetas: bônus, tentativas e tempo', [3 + 1, 9 + 4 >= 14, 12 + 4 >= 14, 2 + 0.5], [4, False, True, 2.5])
ck('Traje de Rina: horas restantes', 4 - 2, 2)

# ---------------- s036
has('| 2 | Uma opção de combate ou exploração com limites definidos | 7 |')
has('| 1 | Uma capacidade que muda o uso habitual do equipamento | 13 |')
has('| 3 | 1 |')
has('| 1 ou especial | 3 |')
has('Depois de resolver um arremesso com esta arma no seu turno, ela volta para a mão que a lançou, se essa mão estiver livre.')
ck('Desgaste grau 2: missões A, B e C', [2 - 1, 2 - 1 - 0, 2 - 1 - 0 - 1], [1, 1, 0])

# ---------------- s096
ck('Anel: orçamento inicial e total', [4000 + 6000 + 2000 + 18000, 30000 + 8000, 40000 - 38000], [30000, 38000, 2000])
ck('Anel: segundo lote (resina e consumíveis)', 6000 + 2000, 8000)
ck('Anel: testes de Aya (Destreza 3, Maestria 2)', [3 + 2, 7 + 5 >= 14, 12 + 5 >= 14], [5, False, True])
ck('Anel: horas e dedicação de Kenji', [3 + 3, 8 + 4, 28 - 6], [6, 12, 22])

# ---------------- s097
has('Receba **uma ferramenta amaldiçoada emprestada por vez**, de grau igual ou inferior à sua patente reconhecida, até grau 1.')
has('**Uma vez por descanso longo**, após falhar em Persuasão numa negociação viável, ofereça sua palavra e reputação como garantia.')
has('| Kunai (lâmina de arremesso) | 1 | 1d6 Perfurante | Longo Alcance 6/18 m · Oculta · Leve | — | 0,2 | 8.000 |')
ck('Venda: Persuasão e diferença', [8 + 4 >= 14, 38000 - 24000, 2000 + 24000, 22 - 2], [False, 14000, 26000, 20])

# ---------------- s098
has('Você não ouve e falha automaticamente em testes que precisem de audição. Recebe **-2 na iniciativa**.')
ck('Pastilha: Volume, selo e prazos', [round(0.1 + 0.4, 1), 9 + 8, 17 - 1, 16 - 15.5, 8 + 3 >= 14, 14 * 60 + 10 - (14 * 60 + 2)], [0.5, 17, 16, 0.5, False, 8])

# ---------------- s099
has('| Levantar alguém que estava a zero de vida. | O socorro devolveu a capacidade de agir pelas regras de queda. |')
has('| 20–22 | 1.500 |')
has('salvo o XP guardado até cumprir o feito do Limiar do nível 20.')
has('As **duas primeiras missões da semana** pagam a recompensa inteira. A partir da terceira, cada posição paga metade da anterior.')
has('| Aguentar | Fica Inconsciente e espera socorro. | 1/4 do máximo de referência, para cima, sem teto. |')
ck('Limiar: janela, tratamento e cura', [3 - 1, math.ceil(84 / 4), 6 - 2, 2 * 2, 6 + 5 + 5 + 6, 22 >= 21, 12 - 6], [2, 21, 4, 4, 22, True, 6])
ck('Limiar: XP e níveis', [100 // 2, 3950 + 50, 4000 - 1500, 2500 - 1500, 1000 >= 1500], [50, 4000, 2500, 1000, False])

sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(primary) == '7311979bdfc61bda1d2fd5113106f072edc7dd5b8a801a02779ada53fd13a81d'
d = {'registro': 127, 'novos_parametros': False, 'conferencias': checks,
     'regras_primarias': {'fonte': str(primary.relative_to(R)), 'sha256': sha(primary),
                          'trechos_consultados': ['Ofícios e exemplo de Arrombamento', 'Reparo do Traje de Rina', 'Graus das ferramentas, nível mínimo e Desgaste', 'Kunai Fiel e Kunai',
                                                  'Cofre da Família e Palavra Empenhada', 'Surdo', 'Limiar do nível 20, progressão, XP e experiência semanal', 'Aguentar e tratamento']},
     'limites': ['Conferência dirigida da aritmética e da presença literal das regras citadas. Sem simulação.',
                 'Anel de Testemunho, Pastilha e os valores de projeto são exemplos experimentais; contas corretas não os aprovam como regra geral.']}
(A / 'contas-conferidas.json').write_text(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
print(len(checks), 'contas conferidas')

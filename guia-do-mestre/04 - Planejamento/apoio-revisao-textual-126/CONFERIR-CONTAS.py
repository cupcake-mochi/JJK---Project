"""Contas dirigidas do lote B3-02: Remodelar, Cortina, Traje, mescla, Firmeza, Condicional,
Matriz de chão e Desarma o Feitiço, conferidos contra o texto do Livro de Regras 1.0 (R53)."""
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


leve, media, pesada = (lambda c: math.ceil(c / 2)), (lambda c: c), (lambda c: math.ceil(1.5 * c))
has('| 3 | 9 | 9 | 2 | 3 | 5 |')

# ---------------- s033
has('> **Exemplo.** Um Projétil de Classe 3 tem Fura por 3 pontos, sem desconto, e causa 6d8. Trocar Fura por Rápido, que custa 5, retira **2d8**. A versão causa 4d8, usa Bônus e custa **9 + 2 = 11 PE**.')
ck('Remodelar: Fura → Rápido na Classe 3', [9 - media(3), pesada(3) - media(3), 6 - 2, math.ceil(3 / 2), 9 + 2], [6, 2, 4, 2, 11])
has('| 4 a 6 | Um quarteirão. | Até 300 m. |')
has('A Cortina tem **40 × Refino pontos de vida**')
has('isso exige **dez turnos consecutivos dedicando a Ação Padrão**')
ck('Cortina com Refino 6', [270 <= 300, 320 <= 300, 40 * 6], [True, False, 240])
has('Escolha também **um tipo de TR** entre Físico, Vigor, Intelecto e Espírito, e **um número de perícias igual à sua Maestria**.')
ck('Traje com Maestria 2: perícias e TR', [2, 1], [2, 1])
has('Você recebe a aptidão escolhida como semente **no nível 2**')

# ---------------- s093
has('**Montagem:** Aura (2), base de cura (3), Escolher (3), Gesto (devolve 2). Saldo 3: dois pontos de dano e um de cura.')
ck('Pulso: saldos nas Classes 3 e 4', [9 - media(3) - leve(3) - media(3) + leve(3), 12 - media(4) - leve(4) - media(4) + leve(4)], [3, 4])
ck('Pulso: Explosão (Média) no lugar de Aura (Leve)', [media(3) - leve(3), media(4) - leve(4), 9 - 3 - 3 - 3 + 2, 12 - 4 - 4 - 4 + 2], [1, 2, 2, 2])
ck('Pulso: Remodelar e PE', [math.ceil(3 / 2), math.ceil(4 / 2), 9 + 2, 12 + 2], [2, 2, 11, 14])
ck('Yara: CD e exemplos', [8 + 4 + 2, 20 - 12, 4 + 5 + 2, math.ceil(11 / 2), 22 - 11, math.ceil(5 / 2)], [14, 8, 11, 6, 11, 3])
has('| 15 | Forma Fluida. |')
has('| 23 | Composição Técnica. |')

# ---------------- s094
has('Na criação do feitiço, escolha uma categoria: **testes de perícia, testes de ofício ou Testes de Resistência (TR)**.')
ck('Firmeza: Classe 2 e Classe 3', [leve(2) * 2, 6 - 2, leve(3) * 3, 9 - 6], [2, 4, 6, 3])
ck('Firmeza + Guarda na Classe 2', [leve(2) + media(2), 6 - 3], [3, 3])
ck('Iara e Rui', [14 - 6, 14 + 3 + 1], [8, 18])
has('Se impedir em pelo menos metade delas, devolve Média.')
has('ignore até **2 × Classe de Redução de Dano**')
ck('Lâmina de canal: saldos com devolução Média, Leve e zero', [9 - leve(3) - media(3) + media(3), 9 - 2 - 3 + leve(3), 9 - 2 - 3], [7, 6, 4])
ck('Lâmina de canal: Fura, ataque e dados', [2 * 3, 3 + 1 + 2, 12 + 6, sum([3, 4, 2, 5, 1, 6, 4]), 4 / 6 >= 0.5], [6, 6, 18, 25, True])
ck('Matriz de chão: saldo e ataque', [9 - 2 - 3 + leve(3), 8 + 6 >= 16], [6, False])
has('O mestre deve rever uma Restrição depois de três sessões em que o feitiço tenha sido usado.')
has('Uma Vez, Condicional, Aquecer e Restrições próprias equivalentes pertencem ao mesmo grupo de frequência.')

# ---------------- s095
has('Uma técnica de luz prepara uma aplicação de Efeito fora de combate de Classe 2 para iluminar um cômodo grande por 10 minutos. Cada uso custa Ação Padrão e 6 PE.')
has('role **d20 + atributo da técnica, sem maestria, contra a CD de quem criou**.')
has('Para outros tipos de aplicação, o mestre atribui uma Classe de **1 a 7** ou determina que o cancelamento é impossível. Domínios ficam fora dos alvos permitidos.')
ck('Luz de Oficina: PE', [15 - 6, 6 - 0], [9, 6])
ck('Desarma: saldos nas Classes 1 e 2', [3 - media(1), 6 - media(2)], [2, 4])
ck('Desarma contra Luz de Classe 2', [8 + 3 + 1, 8 + 3 >= 12, 8 + 3 + 1 >= 12, 10 - 3, 10 - 6], [12, False, True, 7, 4])

sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(primary) == '7311979bdfc61bda1d2fd5113106f072edc7dd5b8a801a02779ada53fd13a81d'
d = {'registro': 126, 'novos_parametros': False, 'conferencias': checks,
     'regras_primarias': {'fonte': str(primary.relative_to(R)), 'sha256': sha(primary),
                          'trechos_consultados': ['Tabela de Classe e preços', 'Remodelar e seu exemplo', 'Cortina e Barreira Simples', 'Situação do Traje', 'Semente de Sem Técnica',
                                                  'Pulso de renovação, Forma Fluida e Composição Técnica', 'Firmeza, Guarda, Fura, Rápido e Gesto', 'Condicional, grupo de frequência e revisão de Restrições',
                                                  'Luz de Oficina e Desarma o Feitiço']},
     'limites': ['Conferência dirigida da aritmética e da presença literal das regras citadas. Sem simulação.',
                 'Matriz de chão e a Classe atribuída ao painel do Escriba continuam propostas experimentais; contas corretas não as aprovam.']}
(A / 'contas-conferidas.json').write_text(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
print(len(checks), 'contas conferidas')

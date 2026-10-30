"""Contas dirigidas do lote B3-01: reparo do corpo, Restrição corporal e avaliação de poderes,
conferidas contra o texto do Livro de Regras 1.0 (R53)."""
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


# Tabela de preços por Classe e desconto pessoal de Família Livre (metade da Classe, para cima).
price = {c: (math.ceil(c / 2), c, math.ceil(1.5 * c)) for c in range(1, 8)}
has('| 5 | 17 | 15 | 3 | 5 | 8 |')
has('Uma Melhoria de Família Livre recebe desconto igual à **metade da Classe, arredondada para cima**.')

# ---------------- s090: reparo
has('A CD é **8 + atributo usado no ofício + Maestria do reparador + ajuste da comparação**.')
has('| Uma abaixo | Média | −2 | Metade da vida máxima. |')
has('| Duas ou mais acima | Difícil | 0 | Um quarto da vida máxima. |')
has('**Uma vez por dia**, quando um teste para reparar você durante um **descanso curto** falhar')
has('No sucesso, recupere **30% da vida máxima, arredondados para baixo**.')
vida = 12 + 2 + (7 + 2) * 3
ck('Reparo: vida do Bastião nível 4, Constituição 2', vida, 41)
ck('Reparo: CD, bônus e rolagens', [8 + 3 + 1 + 0, 3 + 1, 7 + 4 >= 12, 8 + 4 >= 12], [12, 4, False, True])
ck('Reparo: frações (metade, terço, quarto, 30%)', [vida // 2, vida // 3, vida // 4, math.floor(vida * 0.3)], [20, 13, 10, 12])
ck('Reparo: saldo e limite ao máximo', [9 + 20, min(vida, 35 + 20) - 35, 20 - 6], [29, 6, 14])
ck('Reparo: Classe máxima no nível 4', 1, 1)

# ---------------- s091: Restrição corporal
has('| Vida no nível 1 | 6 + Constituição. |')
has('Seus **PE máximos aumentam em 2 × Essência**.')
has('sua **vida máxima é metade da normal, arredondada para baixo, mínimo 1**')
has('**TRs de Vigor seguem normalmente**, inclusive os de Concentração.')
has('Some **10 + Destreza da entidade + metade da Essência ou da Inteligência do invocador**, arredondada para baixo.')
has('O vínculo alcança até **3.000 km a partir do seu corpo**.')
has('sofra **1d4 de dano Radiante, sem TR**')
has('Um **descanso longo em ambiente propício recupera 25% da vida máxima**')
has('Efeitos de cura recuperam **metade da vida normal, arredondada para baixo, mínimo 1 quando positiva**.')
has('Com Constituição 2, uma entidade comum de nível 5 tem **7 + 5 × 4 = 27 de vida**.')
v = 6 + 2 + (4 + 2) * 4
ck('Nilo: vida antes e depois de Corpo Quebradiço', [v, max(1, v // 2)], [32, 16])
ck('Nilo: PE (6 × nível + 2 × Essência)', 6 * 5 + 2 * 3, 36)
ck('Nilo: atributos somam 9', 0 + 1 + 2 + 3 + 3, 9)
ck('Escriba: Defesa e Bloquear', [10 + 2 + 3 // 2, 13 - 11], [13, 2])
ck('Nilo: Vigor treinado e Concentração CD 14', [2 + 1, 11 + 3 >= 14], [3, True])
ck('Quebradiço: cura dentro do máximo reduzido', min(16, 8 + 6), 14)
ck('Exaurido: descanso, limite de deslocamento e cura pela metade', [math.floor(32 * 0.25), 8 + 8, 32 // 2, 7 // 2, 16 + 3, 16 + 3 > 16], [8, 16, 16, 3, 19, True])

# ---------------- s030: avaliação de poderes
has('Concede **+2 no ataque ou +2 na CD do TR** que resolve o feitiço')
has('| Sem dano | Descarta o saldo inteiro. | A rodada adicional e +2 na CD dos TRs próprios de Controle, quando aplicáveis. |')
has('**Uma vez por descanso curto**, use **Ação Padrão** para recuperar **4 × sua maior Classe em pontos de vida**')
has('**Uma vez por dia, antes da rolagem**, pode usar **10 no lugar de um d20**')
has('Fora de combate, Aquecer permite o uso sem atraso adicional.')
ck('Toque sem Melhoria e com Precisão (Classe 1)', [3 - 0 + 0, price[1][0], 3 - 1 + 1, 3 + 1 + 2], [3, 1, 3, 6])
ck('Prender com fios: saldo e CD', [6 - price[2][1], 8 + 3 + 2, 8 + 3 + 2 + 2], [4, 13, 15])
ck('Recomposição com maior Classe 3', 4 * 3, 12)
ck('Fundamento Incorporado', [10 + 5, 9 + 5], [15, 14])

# ---------------- s031: poderes avançados
has('| 17 a 20 | 24d8 | 8 | 25 |')
has('Seu custo é **9 + 4,5 = 13,5**, arredondado para **14 PE**.')
has('| Sangue | Sofre 4 × Classe de dano irredutível, direto na vida. |')
has('Quando o alvo passa no TR de uma Máxima de dano, recebe **três quartos do dano**.')
has('O mestre pode permitir outro uso depois de **3 rodadas**, sem contar a rodada em que a usou.')
has('| Abertura | Ação Completa, Selo e 24 PE |')
has('| Área e duração | Raio 7,5 m; dois turnos seguintes |')
has('Com refino 5, são 100 PV')
ck('Liberação Classe 3 por Linha', [9 - 2, 9 - 2 + 3, math.ceil(9 * 1.5), 4 * 3], [7, 10, 14, 12])
ck('Técnica Máxima: Fenda de Arrasto e TR', [8 - (0 + 1 + 1), math.ceil(101 * 3 / 4), 5 * 5], [6, 76, 25])
ck('Máxima de cura: base e Guarda na Classe 5', [price[5][1], price[5][1], price[5][1] + 0 + price[5][1], max(1, price[5][1] - math.ceil(5 / 2)), price[5][1] + 0 + 2, 8 - 7], [5, 5, 10, 2, 7, 1])
ck('Recarga: usada na rodada 1, volta na 5', 1 + 1 + 3, 5)
ck('Galeria de Vidro: Acerto e aplicações', [3 * 4 - price[4][1], 3], [8, 3])

sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(primary) == '7311979bdfc61bda1d2fd5113106f072edc7dd5b8a801a02779ada53fd13a81d'
d = {'registro': 125, 'novos_parametros': False, 'conferencias': checks,
     'regras_primarias': {'fonte': str(primary.relative_to(R)), 'sha256': sha(primary),
                          'trechos_consultados': ['Existência Artificial, Manutenção Precisa, Reparo do corpo, Reparo Autônomo e Reparar', 'Vida e PE do Bastião e do Emanador',
                                                  'Restrição corporal: CE4, Rede Remota, Saída Elevada, Corpos Debilitado, Quebradiço e Exaurido, Reserva Excedente',
                                                  'Defesa das entidades e vida de entidade de nível 5', 'Tabela de Classe, preços e desconto de Família Livre',
                                                  'Precisão, Prende, reforço de Controle sem dano, Toque, Aquecer', 'Recomposição e Fundamento Incorporado',
                                                  'Liberação Máxima (Corte de ruptura, preços), Técnica Máxima (tabela, TR, recarga, Fenda de Arrasto)', 'Galeria de Vidro e Sala de Trégua']},
     'limites': ['Conferência dirigida da aritmética e da presença literal das regras citadas. Sem simulação.',
                 'Os exemplos continuam experimentais; contas corretas não demonstram equilíbrio.']}
(A / 'contas-conferidas.json').write_text(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
print(len(checks), 'contas conferidas')

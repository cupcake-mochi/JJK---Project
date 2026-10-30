"""Contas dirigidas do lote B5-02: aquisição, criação, reconstrução, transferência e a prova do Cão de sombra,
conferidas contra o texto do Livro de Regras 1.0 (R53)."""
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


def destroi(vida_max, vida, dano):
    return dano >= vida_max or (dano - vida) > F(vida_max, 2)


# ---------------- s043
has('**Um dano direto destrói a entidade quando uma única ocorrência alcança sua vida máxima ou quando o excedente além de zero supera metade da vida máxima.**')
has('Reconstruir usa o mesmo teste de criação, comparando a **nova Classe** com a de quem reconstrói, e reduz a dificuldade em um degrau: Igual vira **Média (−2)**; Uma abaixo vira **Fácil (−4)**')
has('As Classes comparadas são 4 e 3: a dificuldade é Média. A CD fica **8 + 4 + 2 − 2 = 12**.')
has('Cada talismã ocupa **0,5 de Volume**')
has('Fora dele, use o limite comum de duas.')
ck('Destruição (52 PV, 8 atuais): 30 e 35 de dano direto', [30 - 8, destroi(52, 8, 30), 35 - 8, destroi(52, 8, 35)], [22, False, 27, True])
ck('Calígrafa: CD, bônus, falha e nova tentativa', [8 + 4 + 2 - 2, 4 + 2, 5 + 6 >= 12, 8 + 6 >= 12], [12, 6, False, True])
ck('Reconstrução e criação na Classe 4; transferência', [8 + 4 + 2 - 2, 8 + 4 + 2, 8 + 4 + 2 - 2, 8 + 4 + 2], [12, 14, 12, 14])
ck('Doma: CD 12', [11 < 12, 12 < 12], [True, False])

# ---------------- s045 / s046 (referências do Guia)
cria = {1: 8, 2: 16, 3: 32, 4: 48, 5: 72, 6: 96, 7: 128}
ck('Reconstrução = metade da criação da nova Classe', [cria[c] // 2 for c in range(2, 8)], [8, 16, 24, 36, 48, 64])
ck('Retomada da reconstrução', [math.ceil(cria[c] / 2 / 2) for c in range(2, 8)], [4, 8, 12, 18, 24, 32])
tr = {c: max(2, math.ceil(cria[c] / 8)) for c in cria}
ck('Transferência = 1/8, mínimo 2', [tr[c] for c in range(1, 8)], [2, 2, 4, 6, 9, 12, 16])
ck('Retomada da transferência', [max(1, math.ceil(tr[c] / 2)) for c in range(1, 8)], [1, 1, 2, 3, 5, 6, 8])
ck('Criação do Vigia: horas e materiais', [20 + 12, 32 // 2, 32 + 16, 24000 + 6000 + 6000, 5 + 6 >= 12, 8 + 6 >= 12], [32, 16, 48, 36000, False, True])
ck('Ciclos do Vigia', [20, 12 + 8, 8, 20 + 20 + 8], [20, 20, 8, 48])
ck('Reconstrução para Classe 4: horas e materiais', [24 + 12, 12000 + 3000 + 3000, 28 - 24, 12 - 4], [36, 18000, 4, 8])
ck('Classes 1 → 4: trabalho-base e com uma falha na segunda', [8 + 16 + 24, 8 + 16 + 8 + 24], [48, 56])
ck('Transferência do Vigia', [32 // 8, 2 + 6 >= 12, 9 + 6 >= 12, 4 + 2, 2000 * 2], [4, False, True, 6, 4000])

# ---------------- s051
has('A entidade tem treino em **4 + metade da Inteligência**, arredondada para baixo, perícias.')
has('Quem tem energia amaldiçoada começa com **Cobrir-se de Energia** e **Canalizar Energia**, sem gastar uma escolha.')
has('| 1–2 | 1d4 |')
has('Some **10 + Destreza da entidade + metade da Essência ou da Inteligência do invocador**, arredondada para baixo.')
vida = 5 + 2 + (3 + 2) * (2 - 1)
ck('Cão: vida, Integridade, Defesa, Bloquear', [vida, vida // 2, 10 + 2 + 2 // 2, 13 - 11], [12, 6, 13, 2])
ck('Cão: ataque, CD, TRs e perícias', [3 + 1, 8 + 3 + 1, 3 + 1, 2, 1, 1, 3 + 1, 2 + 1, 1 + 1, 1 + 1, 4 + 1 // 2], [4, 12, 4, 2, 1, 1, 4, 3, 2, 2, 4])
ck('Cão: Mordida precisa', 2 - 1 + 1, 2)
ck('Cão: estágios de Integridade (máximo 6)', [math.ceil(6 / 4), math.ceil(6 / 2), math.ceil(6 * 3 / 4)], [2, 3, 5])
ck('Kaito (correção): golpe desarmado com Canalizar, mínimo e máximo', [1 + 3 + 1, 4 + 3 + 4], [5, 11])
ck('Kaito: primeiro e segundo golpes', [10 + 4 >= 13, 1 + 3 + 2, 12 - 6, 6 - 6, destroi(12, 6, 6)], [True, 6, 6, 0, False])
ck('Kaito: golpe máximo a 1 PV destrói; golpe de 12 destrói', [11 - 1, destroi(12, 1, 11), destroi(12, 6, 12)], [10, True, True])
ck('Golpe máximo de Kaito nunca alcança 12 sozinho', 11 >= 12, False)
ck('Retorno do cão e PE de Kaito', [1, 2 * 1, 12 // 2, 8 - 1, 7 - 2], [1, 2, 6, 7, 5])

sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(primary) == '7311979bdfc61bda1d2fd5113106f072edc7dd5b8a801a02779ada53fd13a81d'
d = {'registro': 129, 'novos_parametros': False, 'conferencias': checks,
     'correcao_documentada': {'caso': 's051', 'antes': 'ataque desarmado de Kaito: 1d4 + 3, sem outro modificador; d4 mostra 3 → 6',
                              'depois': '1d4 + 3 + 1d4 (Canalizar Energia); d4 mostram 1 e 2 → 6; aviso de que o golpe máximo de 11 destrói o cão a 1 PV',
                              'fundamento': 'Livro de Regras 1.0: quem tem energia amaldiçoada recebe Canalizar Energia sem escolha; Canalizar em Golpe soma 1d4 no Refino 1–2 a cada ataque desarmado que acerta.'},
     'regras_primarias': {'fonte': str(primary.relative_to(R)), 'sha256': sha(primary),
                          'trechos_consultados': ['Queda e destruição de entidades', 'Domar uma maldição', 'Criação, vantagem, reconstrução e transferência', 'Talismã de 0,5 Volume e limite de duas ativas',
                                                  'Perícias e Defesa de entidades', 'Canalizar Energia e Canalizar em Golpe', 'Retorno e entrada']},
     'limites': ['Conferência dirigida da aritmética e da presença literal das regras citadas. Sem simulação.',
                 'Os prazos de criação, reconstrução e transferência são referências do Guia; a prova do Cão de sombra é proposta experimental.']}
(A / 'contas-conferidas.json').write_text(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
print(len(checks), 'contas conferidas')

"""Contas dirigidas do lote B5-01: Pactos e Promessa, conferidos contra o texto do Livro de Regras 1.0 (R53)."""
from pathlib import Path
from datetime import datetime, timedelta
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


# ---------------- s047
for ideia in ['Fragmentação', 'Liberação irregular', 'Energia alternada', 'Pacifismo impraticável', 'Magnetismo energético', 'Despertar do corpo', 'Reserva vital']:
    has('| ' + ideia + ' |')
ck('Sete ideias do Livro de Regras 1.0', 7, 7)
has('Quando houver uma quantidade, ela é uma **porcentagem da energia máxima, combinada com o mestre**, nunca um número fixo.')
has('Pactos não concedem bônus numérico a ataques, Defesa ou perícias.')
has('**Pacto não concede Estilo.**')

# ---------------- s048
has('Cada pacto ocupa uma vaga **enquanto existir**.')
ck('Fio de Corte: Classe 1, Projétil, sem peças', [3 - 0, 3], [3, 3])
ck('Condução pela matéria: ataque e dano na porta', [3 + 1, 10 + 4 >= 14, 7 + 4 >= 14, 3 + 4 + 5, 20 - 12], [4, True, False, 12, 8])
t0 = datetime(2026, 10, 22, 18)
j1 = t0 + timedelta(days=30)
ck('Pacifismo: calendário das janelas', [j1.strftime('%d/%m %H'), (j1 + timedelta(days=3)).strftime('%d/%m %H'), (j1 + timedelta(days=30)).strftime('%d/%m %H')],
   ['21/11 18', '24/11 18', '21/12 18'])

# ---------------- s049
has('Recupere **25% dos PE máximos**, sem ultrapassar o máximo.')
has('Seu custo é **9 + 4,5 = 13,5**, arredondado para **14 PE**.')
teto = lambda m, p: 0 if p == 0 else max(1, math.floor(m * p))
ck('Liberação: tetos com máximo 40', [teto(40, x) for x in [0, .25, .5, .75, 1]], [0, 10, 20, 30, 40])
ck('Liberação: exemplo do feitiço de Classe 3', [24 - 9, 10 - 9, 1 >= 2], [15, 1, False])
ck('Liberação: Refluxo com saldo 6', [math.floor(40 * .25), 6 + 10, 14], [10, 16, 14])
ck('Liberação: manutenção, Refluxo e feitiços', [6 - 3, 10 - 3, 3 + 10, 13 - 6, 7 - 6, 9 <= 7 - 6], [3, 7, 13, 7, 1, False])
ck('Liberação: mudanças de máximo (50%, gasto 12)', [teto(40, .5) - 12, teto(60, .5) - 12, max(0, teto(20, .5) - 12), teto(40, .5) - 12], [8, 18, 0, 8])

# ---------------- s050
has('Quebrar uma Promessa **custa a energia amaldiçoada de quem quebra e pode custar a vida**.')
has('Promessas e pactos temporários não entram nesse limite.')
has('Ela é consumida primeiro e normalmente desaparece no fim da cena.')
ck('Promessa: descanso curto de Akira (máximo 40)', math.floor(40 * .25), 10)
ck('Promessa: duração do bloqueio (Dia 2 18h → Dia 3 10h)', (datetime(2026, 1, 3, 10) - datetime(2026, 1, 2, 18)).seconds // 3600, 16)
ck('Promessa: perda total e máximo', [14 - 14, 4 - 4, 40], [0, 0, 40])

sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(primary) == '7311979bdfc61bda1d2fd5113106f072edc7dd5b8a801a02779ada53fd13a81d'
d = {'registro': 128, 'novos_parametros': False, 'conferencias': checks,
     'regras_primarias': {'fonte': str(primary.relative_to(R)), 'sha256': sha(primary),
                          'trechos_consultados': ['Pacto permanente, vagas e benefícios', 'Pacto de energia como porcentagem', 'Ideias para desenvolver (sete)',
                                                  'Promessa e quebra', 'Descanso curto (25% dos PE)', 'Energia temporária consumida primeiro', 'Liberação Máxima de Classe 3 (14 PE)', 'Núcleo Dependente']},
     'limites': ['Conferência dirigida da aritmética e da presença literal das regras citadas. Sem simulação.',
                 'Pacifismo impraticável, Liberação irregular e a Promessa do arquivo continuam modelos experimentais; contas corretas não os aprovam.']}
(A / 'contas-conferidas.json').write_text(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
print(len(checks), 'contas conferidas')

"""Contas e regras dirigidas do lote C-03 (personagens, entidades e inimigos), conferidas contra o Livro de Regras 1.0 (R53)
e, para a dedicação, contra o padrão recomendado do guia (28 horas por ficha a cada sete dias)."""
from pathlib import Path
import json, hashlib, math
A = Path(__file__).resolve().parent
R = A.parents[1]
primary = R / '04 - Planejamento/apoio-carregador/fontes/LIVRO-COMPLETO-R53.md'
rule = primary.read_text()
C = R / '06 - Redacao do Guia/revisao-98/consultas'
guia = (R / '06 - Redacao do Guia/revisao-98/08-entre-missoes.md').read_text()
checks = []
def ck(name, x, y):
    assert x == y, (name, x, y); checks.append({'conta': name, 'resultado': x, 'esperado': y})
def has(t, src=None):
    assert t in (rule if src is None else src), t

# s040 — dedicação: 28 horas novas; gaste primeiro as antigas; só a parte livre das novas passa
has('O padrão recomendado é **28 horas novas por ficha a cada ciclo comum de sete dias**.', guia)
def ciclo(antigo, executado, novas=28):
    usa_antigo = min(antigo, executado); usa_novo = executado - usa_antigo
    return usa_antigo, usa_novo, antigo - usa_antigo, novas - usa_novo
tabela = {('Rina', 1): (0, 18), ('Mei', 1): (0, 28), ('Rina', 2): (10, 20), ('Mei', 2): (0, 8), ('Rina', 3): (18, 12), ('Mei', 3): (20, 0)}
publicado = {('Rina', 1): (0, 18, 0, 10), ('Mei', 1): (0, 28, 0, 0), ('Rina', 2): (10, 10, 0, 18), ('Mei', 2): (0, 8, 0, 20), ('Rina', 3): (12, 0, 6, 28), ('Mei', 3): (0, 0, 20, 28)}
for k, (antigo, ex) in tabela.items():
    ck(f'Dedicação {k[0]}, ciclo {k[1]}: antigas usadas, novas usadas, antigas que expiram, novas que passam', ciclo(antigo, ex), publicado[k])
# o saldo de cada ciclo é o que passou do anterior
ck('Saldo de Rina no ciclo 2 = novas que passaram do 1', publicado[('Rina', 1)][3], tabela[('Rina', 2)][0])
ck('Saldo de Rina no ciclo 3 = novas que passaram do 2', publicado[('Rina', 2)][3], tabela[('Rina', 3)][0])
ck('Saldo de Mei no ciclo 3 = novas que passaram do 2', publicado[('Mei', 2)][3], tabela[('Mei', 3)][0])
ck('Abertura do ciclo 2: Rina 10 + 28, Mei 0 + 28', [10 + 28, 0 + 28], [38, 28])
ck('Abertura do ciclo 4: 28 novas + 28 que passaram', 28 + 28, 56)
ck('Entrada no quinto dia: dias 5, 6 e 7 a 28 ÷ 7 horas', 3 * (28 // 7), 12)
ck('Conferência pendente: 10 confirmadas + 8 reservadas + 10 livres', 10 + 8 + 10, 28)
ck('Abertura seguinte: 10 livres + 28 novas', 10 + 28, 38)

# s042 — Overtime: 2,5% por hora, 8 horas = 20%; máximo 40 → 32 e 48; diferença 16; 12 + 16
has('O percentual é **2,5% por hora**: 4 horas dão 10%; 8 horas, a jornada normal, dão 20%')
has('Com PE máximo 40 e jornada de 8 horas, seu máximo é **32 durante a jornada** e **48 na hora extra**. Ao passar de um para o outro, você recebe **16 PE**')
ck('Overtime: 40 com 20% a menos e a mais', [math.floor(40 * 0.8), math.floor(40 * 1.2)], [32, 48])
ck('Overtime: PE depois da passagem, 12 + (48 − 32)', 12 + (48 - 32), 28)
has('Você pode manter **metade da Essência em pactos**, arredondada para baixo')
ck('Vagas com Essência 4', 4 // 2, 2)

# s044 — calígrafa: CD 8 + 4 + 2 − 2 = 12; d20 + 6, um 6 basta; talismã 0,5 Volume
has('A CD fica **8 + 4 + 2 − 2 = 12**. Seu teste é d20 + 6; um 6 no dado basta.')
ck('Calígrafa: CD', 8 + 4 + 2 - 2, 12)
ck('Calígrafa: Destreza 4 + Maestria 2; dado 6', [4 + 2, 6 + 6 >= 12], [6, True])
has('Rolagem | d20 + 6; resultado 6 no dado totaliza 12 e tem sucesso.', (C / '44-registro-de-aquisicao-e-estado-de-entidade.md').read_text())

# s061 — Agarrar do Carregador: CD 8 + Força 3 + maestria 1; Escapar com a mesma CD; estágio 2 só pesa em feitiço
has('O alvo faz um **TR Físico contra CD 8 + sua Força + sua maestria**.')
has('Rina tem Força 3 e maestria 1: sua CD é 12.')
ck('Carregador: CD de Agarrar', 8 + 3 + 1, 12)
has('No seu turno, gaste uma **Ação Padrão** e faça um **TR Físico contra a CD da contenção**.')
has('| Pelo menos 1/2 | 2 | Deslocamento pela metade. Cada feitiço custa +1 PE por Classe. |')
has('| Pelo menos 3/4 | 3 | Desvantagem em ataques e TRs.')
has('A manobra substitui o dano: não há rolagem de ataque, crítico nem adicionais de dano de ataque.')

sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(primary) == '7311979bdfc61bda1d2fd5113106f072edc7dd5b8a801a02779ada53fd13a81d'
d = {'registro': 133, 'novos_parametros': False, 'conferencias': checks,
     'regras_primarias': {'fonte': str(primary.relative_to(R)), 'sha256': sha(primary),
                          'trechos_consultados': ['Nanami: Overtime', 'Vagas de pacto', 'Teste de criação (calígrafa)', 'Agarrar, derrubar e empurrar', 'Escapar de uma contenção', 'Estágios de Integridade']},
     'padrao_do_guia': 'Dedicação de 28 horas por ficha a cada sete dias: recomendação do guia (Entre missões, 8.2), não regra do Livro de Regras 1.0.',
     'limites': ['A ficha de inimigo e encontro não tem contas; foi conferida na leitura.']}
(A / 'contas-conferidas.json').write_text(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
print(len(checks), 'contas conferidas')

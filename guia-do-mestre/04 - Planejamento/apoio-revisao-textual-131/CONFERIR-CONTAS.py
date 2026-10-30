"""Contas e regras dirigidas do lote C-01 (fichas de mesa), conferidas contra o Livro de Regras 1.0 (R53)."""
from pathlib import Path
import json, hashlib, math
A = Path(__file__).resolve().parent
R = A.parents[1]
primary = R / '04 - Planejamento/apoio-carregador/fontes/LIVRO-COMPLETO-R53.md'
rule = primary.read_text()
checks = []
def ck(name, x, y):
    assert x == y, (name, x, y); checks.append({'conta': name, 'resultado': x, 'esperado': y})
def has(t):
    assert t in rule, t
has('**Pelo menos metade precisa passar** para o grupo conseguir. Num grupo de cinco, são necessários três sucessos.')
ck('Teste em grupo: metade, para cima', [math.ceil(4 / 2), math.ceil(5 / 2)], [2, 3])
has('Em empate, age primeiro quem tiver maior Destreza. Se ela também empatar entre jogador e inimigo, o jogador age primeiro.')
has('Bloquear é gratuito, **não gasta Reação**')
has('Se não houver nada a informar, não gaste a ação nem o uso.')
has('Havendo esforço e risco juntos, role uma vez contra a maior CD.')
has('**Ela não volta na passagem de uma rodada para outra.**')
ck('Regras citadas conferidas', 6, 6)
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(primary) == '7311979bdfc61bda1d2fd5113106f072edc7dd5b8a801a02779ada53fd13a81d'
d = {'registro': 131, 'novos_parametros': False, 'conferencias': checks,
     'regras_primarias': {'fonte': str(primary.relative_to(R)), 'sha256': sha(primary),
                          'trechos_consultados': ['Teste em grupo', 'Empate de iniciativa', 'Bloquear', 'Ler o Ambiente', 'Salto com esforço e risco', 'Reação']},
     'limites': ['Formulários quase sem contas; conferência das regras que a folha de condução resume.']}
(A / 'contas-conferidas.json').write_text(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
print(len(checks), 'contas conferidas')

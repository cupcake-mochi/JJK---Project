"""Contas dirigidas do lote B2-06: calendário da febre, valores da ficha preenchida contra as
consultas revistas da dupla e contas do chefe contra as fichas revistas do Carregador e do portão."""
from pathlib import Path
from fractions import Fraction as F
import json, hashlib, math, re

A = Path(__file__).resolve().parent
R = A.parents[1]
C = R / '06 - Redacao do Guia/revisao-98/casos'
primary = R / '04 - Planejamento/apoio-carregador/fontes/LIVRO-COMPLETO-R53.md'
rule = primary.read_text()
checks = []


def ck(name, x, y):
    assert x == y, (name, x, y)
    checks.append({'conta': name, 'resultado': x, 'esperado': y})


def has(text, where=None):
    assert text in (where if where is not None else rule), text


def stage_ranges(m):
    st = {}
    for i in range(m + 1):
        lost = m - i
        s = 4 if i == 0 else max([0] + [k for f, k in [(F(1, 4), 1), (F(1, 2), 2), (F(3, 4), 3)] if lost >= m * f])
        st.setdefault(s, []).append(i)
    return [[min(v), max(v)] for k, v in sorted(st.items())]


# ---------------- s103: calendário em horas a partir do dia 1, 00h
h = lambda dia, hora: (dia - 1) * 24 + hora
contato = h(1, 8)
crises = [contato + 6 * k for k in range(1, 9)]
ck('Febre: crises a cada seis horas', crises[:4], [h(1, 14), h(1, 20), h(2, 2), h(2, 8)])
ck('Febre: término máximo 48 h após o contato (dia 3, 08h)', contato + 48, h(3, 8))
ck('Febre: TRs do exemplo contra CD 14', [8 + 3 >= 14, 7 + 3 >= 14, 12 + 3 >= 14, 13 + 3 >= 14], [False, False, True, True])
ck('Febre: dano da crise e vida', [3 + 4, 40 - 7], [7, 33])
ck('Febre: tratamento (falha, espera e nova tentativa)', [6 + 5 >= 14, h(1, 17) + 6, h(1, 23) + 2, 10 + 5 >= 14], [False, h(1, 23), h(2, 1), True])
ck('Febre: a doença termina antes da crise das 02h', h(2, 1) < crises[2], True)
ck('Febre: horas do profissional', 2 + 2, 4)
ck('Febre: primeira crise e chegada à enfermaria (1 h de percurso depois de conter às 08h10)', [h(1, 8) + 10 / 60 + 1 <= h(1, 15)], [True])
has('Seus ataques e testes de perícia têm desvantagem. A condição não causa dano de Veneno por conta própria nem impõe desvantagem a todos os TRs.')
has('Dano absorvido pela vida temporária ainda conta, pois atingiu sua proteção.')

# ---------------- s077: valores iguais aos das consultas revistas 75 e 76
f75 = (C / '75-ren-e-sora-atacante-e-apoio.md').read_text()
f76 = (C / '76-confronto-de-ren-e-sora.md').read_text()
f73 = (C / '73-ensaio-guiado-do-sineiro.md').read_text()
for t in ['**72 PV / 36**', '**48 PV / 24**', '**8 / 8**', '**12 / 12**', '**13 / 2d10 + 2**', '| TR Físico | **+5**, Força treinada | **+3**, Destreza treinada |',
          '| Carga normal / arrasto máximo | 9 / 18 Volume | 5 / 10 Volume |', 'Ren pesa 72 kg; Sora, 60 kg.']:
    has(t, f75)
ck('Ficha: valores da dupla presentes na consulta 75', True, True)
ck('Ficha: perfis de nível 6 (vida/PE/Integridade)', [[65, 24, 50], [44, 36, 55], [51, 30, 65]],
   [[int(x) for x in re.search(r'\| ' + n + r' \|[^|]*\|[^|]*\| (\d+) \| (\d+) \| (\d+) \|', f73).groups()] for n in ['Rina', 'Mei', 'Akira']])
final76 = {n: re.search(r'\| ' + n + r' \| ([^|]+) \| ([^|]+) \| ([^|]+) \|', f76[f76.index('Estado ao encerrar a oposição'):]).groups() for n in ['Rina', 'Mei', 'Akira', 'Ren', 'Sora']}
ck('Ficha: estado final igual ao do confronto revisto', {k: [x.strip() for x in v] for k, v in final76.items()},
   {'Rina': ['52/65', '24/24', '50/50'], 'Mei': ['44/44', '24/36', '55/55'], 'Akira': ['51/51', '16/30', '65/65'], 'Ren': ['46/72', '1/8', '36/36'], 'Sora': ['0/48', '1/12', '24/24']})
ck('Ficha: PE gastos (grupo / dupla)', [(36 - 24) + (30 - 16), (8 - 1) + (12 - 1)], [26, 18])
ck('Ficha: Fio (montagem e estágio 2)', [3 - 1 - 1, 3 + 1, max(1, 2 // 2) >= 1], [1, 4, True])
ck('Ficha: soma de vida da dupla', 72 + 48, 120)
ck('Ficha: iniciativas (natural + Destreza 2)', [x + 2 for x in [16, 14, 12, 10, 8]], [18, 16, 14, 12, 10])

# ---------------- s068: Carregador e portão
f63 = (C / '63-carregador-consulta-e-doma.md').read_text()
f66 = (C / '66-o-carregador-e-a-saida-que-fecha.md').read_text()
has('| Vida | **32/32 PV**, total experimental escolhido para o encontro. |', f63)
has('| Integridade | **16/16**, metade da vida máxima. |', f63)
has('Com 8 PV ou menos, solta a contenção e tenta se afastar no próprio turno.', f63)
has('de 8 a 5, estágio 2', f63)
ck('Chefe: Integridade do Carregador', stage_ranges(16), [[13, 16], [9, 12], [5, 8], [1, 4], [0, 0]])
ck('Chefe: dois corpos somados', [32 * 2, 16 * 2], [64, 32])
ck('Chefe: limiar de retirada (10 → 7 PV)', [10 > 8, 7 <= 8], [True, True])
has('| A → Q → P, para operar a parada | 12 m |', f66)
has('| C → P, para operar a parada | 6 m |', f66)
ck('Chefe: Mei de A a P e sobra', [9 + 9 - 12, 12], [6, 12])
ck('Chefe: Preparar desloca até 9 m; C→P 6 m', [9 >= 6], [True])
ck('Chefe: estágio 2 (metade do deslocamento) e espaço a 1,5 m de P', [9 / 2, 6 - 1.5, 9 / 2 >= 6 - 1.5, 9 / 2 >= 6], [4.5, 4.5, True, False])
has('**Preparar** | Escolher uma resposta a um evento perceptível, pagando Reação quando a executar.')
has('| Pelo menos 1/2 | 2 | Deslocamento pela metade. Cada feitiço custa +1 PE por Classe. |')
ck('Chefe: nome da criatura nas fontes revistas (sem "Carregador de Sinos")',
   sorted({p.name for p in C.glob('*.md') if 'Carregador de Sinos' in p.read_text()}), [])

sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(primary) == '7311979bdfc61bda1d2fd5113106f072edc7dd5b8a801a02779ada53fd13a81d'
d = {'registro': 124, 'novos_parametros': False, 'conferencias': checks,
     'correcao_documentada': {'caso': 's068', 'antes': 'Carregador de Sinos', 'depois': 'Carregador',
                              'fundamento': 'Nome usado em todas as outras fontes; "de Sinos" misturava a criatura com o Sineiro. Sem mudança de regra ou número.'},
     'regras_primarias': {'fonte': str(primary.relative_to(R)), 'sha256': sha(primary),
                          'trechos_consultados': ['Envenenado', 'Concentração e vida temporária', 'Preparar', 'Estágios de Integridade', 'Vida a zero e socorro']},
     'fontes_cruzadas': ['revisao-98/casos/63, 66, 73, 75 e 76: valores conferidos por texto literal.'],
     'limites': ['Conferência dirigida do calendário, dos valores e das regras existentes. Sem simulação.',
                 'A doença, a dupla e o Carregador continuam experimentais; contas corretas não demonstram equilíbrio.']}
(A / 'contas-conferidas.json').write_text(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
print(len(checks), 'contas conferidas')

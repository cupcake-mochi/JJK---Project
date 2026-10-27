"""Conferência somente de leitura. Não gera nem substitui manifestos.

Uso: python3 conferir.py
As contas não simulam combate nem escolhas humanas. A saída pode ser salva
em resultados.json pela etapa de produção depois de inspecionada.
"""
from pathlib import Path
from fractions import Fraction as F
import hashlib, heapq, json
H = Path(__file__).resolve().parent
R = H.parent.parent
D = json.loads((H / 'dados-comparacao.json').read_text(encoding='utf-8'))
original = json.loads((H / D['fonte_inimigo']).read_text(encoding='utf-8'))
source = R / '04 - Planejamento/apoio-carregador/fontes/LIVRO-COMPLETO-R53.md'
source_hash = hashlib.sha256(source.read_bytes()).hexdigest()
assert source_hash == '7311979bdfc61bda1d2fd5113106f072edc7dd5b8a801a02779ada53fd13a81d'
cases = []
def check(label, actual, expected):
    assert actual == expected, (label, actual, expected)
    cases.append({'caso': label, 'resultado': actual, 'esperado': expected})
def route(start, end, closed=False, dragging=False):
    edges = {n: [] for n in D['nos']}
    blocked = set(D['aresta_bloqueada_por_portao'])
    for a, b, length in D['arestas_regulares_m']:
        if closed and {a, b} == blocked: continue
        cost = length * (2 if dragging else 1)
        edges[a].append((b, cost)); edges[b].append((a, cost))
    queue = [(0, start)]; seen = set()
    while queue:
        cost, at = heapq.heappop(queue)
        if at == end: return cost
        if at in seen: continue
        seen.add(at)
        for nxt, step in edges[at]:
            if nxt not in seen: heapq.heappush(queue, (cost + step, nxt))
    return None

def turns(costs, budget):
    count = 0; index = 0; spent = []
    while index < len(costs):
        count += 1; use = F(0)
        assert costs[index] <= budget
        while index < len(costs) and use + costs[index] <= budget:
            use += costs[index]; index += 1
        spent.append(float(use))
    return {'turnos': count, 'gastos': spent}

# Modelo explícito apenas dos estados ambientais, sem personagens simulados.
def gate(rounds):
    marker = 0; motor = True; closed = False; leaf = True; closures = []
    for n, frame in enumerate(rounds, 1):
        if frame.get('parar'): motor = False
        if frame.get('romper_folha'): leaf = False; closed = False
        if motor and leaf and not closed:
            marker = min(3, marker + 1)
            if marker == 3 and not frame.get('ocupada', False):
                closed = True; closures.append(n)
    return {'marcador': marker, 'motor': motor, 'fechado': closed, 'fechamentos': closures, 'folha_integra': leaf}

check('base do Carregador conservada', [original['inimigo']['vida'], original['inimigo']['integridade'], original['inimigo']['pe'], original['inimigo']['ataques']], [32, 16, 0, 1])
for closed, walk, drag in [(False, 6, 12), (True, 18, 36)]:
    check('rota C-A andando; fechado=' + str(closed), route('C', 'A', closed), walk)
    check('rota C-A arrastando; fechado=' + str(closed), route('C', 'A', closed, True), drag)
    check('retorno A-C continua acessível; fechado=' + str(closed), route('A', 'C', closed), walk)
check('pátio até parada', route('A', 'P'), 12)
check('pátio até parada após fechamento', route('A', 'P', True), 12)
check('trabalho até parada', route('C', 'P'), 6)
check('intervir com dois Movimentos e Padrão', 2 * 9 - route('A', 'P'), 6)
check('retorno a C após parada sem outra ação Padrão', route('P', 'C') <= 6, True)
check('transporte total sem arredondamento', D['socorrista']['itens_proprios_volume'] + D['transportado']['massa_kg'] / 12 + D['transportado']['itens_volume'], 9)
check('teto de arrasto da socorrista', 2 * (5 + D['socorrista']['forca']), 14)
check('transporte dentro do teto', 9 <= 14, True)
check('andar no atalho com um Movimento', turns([F('1.5')] * 4, F(9)), {'turnos': 1, 'gastos': [6.0]})
check('andar no serviço com um Movimento por turno', turns([F('1.5')] * 12, F(9)), {'turnos': 2, 'gastos': [9.0, 9.0]})
check('andar no serviço com Movimento e Bônus', turns([F('1.5')] * 12, F(18)), {'turnos': 1, 'gastos': [18.0]})
check('arrastar pelo atalho preservando Padrão', turns([F(3)] * 4, F(18)), {'turnos': 1, 'gastos': [12.0]})
check('arrastar pelo serviço preservando Padrão', turns([F(3)] * 12, F(18)), {'turnos': 2, 'gastos': [18.0, 18.0]})
check('arrastar pelo serviço com Correr', turns([F(3)] * 12, F(27)), {'turnos': 2, 'gastos': [27.0, 9.0]})
check('estágio2, dois Movimentos, atalho arrastando', turns([F(3)] * 4, F(9)), {'turnos': 2, 'gastos': [9.0, 3.0]})
check('estágio2, dois Movimentos, serviço arrastando', turns([F(3)] * 12, F(9)), {'turnos': 4, 'gastos': [9.0, 9.0, 9.0, 9.0]})
# Recorte desde o recuo: preserva os segmentos difíceis e não guarda sobras.
recess = [F(3)] * 4 + [F('4.5')] * 4 + [F(3)] * 4
check('recuo até pátio pelo atalho; custo agregado', float(sum(recess + [F(3)] * 4)), 54.0)
check('54 metros não cabem em três orçamentos18', turns(recess + [F(3)] * 4, F(18)), {'turnos': 4, 'gastos': [16.5, 16.5, 18.0, 3.0]})
check('recuo até pátio pelo serviço', turns(recess + [F(3)] * 12, F(18)), {'turnos': 5, 'gastos': [16.5, 16.5, 18.0, 18.0, 9.0]})
check('fechamento único na terceira rodada', gate([{}] * 6)['fechamentos'], [3])
check('parada rodada1 mantém zero', gate([{'parar': True}] + [{}] * 4)['marcador'], 0)
check('parada rodada3 antes da fase mantém aberto', gate([{}, {}, {'parar': True}])['fechado'], False)
check('parada depois não reabre', gate([{}, {}, {}, {'parar': True}])['fechado'], True)
check('ocupação no terceiro aguarda', gate([{}, {}, {'ocupada': True}])['fechado'], False)
check('saída da faixa só fecha na fase seguinte', gate([{}, {}, {'ocupada': True}, {}])['fechamentos'], [4])
check('ocupação persistente não fecha', gate([{'ocupada': True}] * 6)['fechamentos'], [])
check('parada durante espera mantém aberto', gate([{}, {}, {'ocupada': True}, {'parar': True}])['fechado'], False)
check('romper folha antes impede fechamento', gate([{'romper_folha': True}] + [{}] * 5)['fechamentos'], [])
check('romper folha depois libera', gate([{}, {}, {}, {'romper_folha': True}])['fechado'], False)
check('dano acumulado encerra comando', max(0, D['comando']['pv'] - 4 - 6), 0)
check('dano acumulado rompe folha', max(0, D['portao']['pv'] - 15 - 25), 0)
check('dano insuficiente conserva bloqueio', max(0, D['portao']['pv'] - 39), 1)
check('resposta preparada alcança atalho aberto', route('C', 'A') <= 9, True)
check('resposta depois do fechamento não alcança saída com9', route('C', 'A', True) <= 9, False)
print(json.dumps({'data': '2026-10-25', 'tipo': 'contas de percursos e estados condicionais; sem combate simulado', 'casos_conferidos': len(cases), 'r53_sha256': source_hash, 'casos': cases, 'teste_humano': False, 'equilibrio_validado': False}, ensure_ascii=False, indent=2))

"""Disponibilidade e estados; não simula um encontro ou valida equilíbrio."""
from pathlib import Path
from fractions import Fraction
import hashlib
import json

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
SOURCE = ROOT / '04 - Planejamento/apoio-piloto/base-inimigos.json'
BOOK = Path('/home/mizuki/CHAT-GPT/RPG -JJK/entregas/livro-diagramado-r53/LIVRO-COMPLETO.md')


def sequence(kind, turns, cost=3):
    balance = 2 if kind == 'U' else 6
    ready = 1
    result = []
    for turn in range(1, turns + 1):
        price = 1 if kind == 'U' else (0 if kind == 'I' else cost)
        if turn >= ready and balance >= price:
            result.append('H')
            balance -= price
            ready = turn + (2 if kind in ('I', 'M') else 1)
        else:
            result.append('B')
    return {'sequencia': result, 'impactos': result.count('H'),
            'saldo': None if kind == 'I' else balance,
            'unidade_saldo': None if kind == 'I' else ('usos' if kind == 'U' else 'PE')}


def combinations(kind, turns, cost=3):
    """Um H ou B por turno; até uma proteção após essa ação por turno.

    Supõe ocasião válida para cada proteção e sobrevivência. Guarda pares de
    quantidades atingíveis, não trajetórias de dano. Não restaura recursos.
    """
    initial = 2 if kind == 'U' else 6
    states = {(initial, 1, 0, 0)}
    for turn in range(1, turns + 1):
        following = set()
        for balance, ready, hits, guards in states:
            for hit in (0, 1):
                if hit and turn < ready:
                    continue
                for guard in (0, 1):
                    price = hit * (1 if kind == 'U' else cost)
                    price += guard * (1 if kind == 'U' else 2)
                    if balance < price:
                        continue
                    next_ready = turn + 2 if hit and kind == 'M' else ready
                    following.add((balance - price, next_ready, hits + hit, guards + guard))
        states = following
    pairs = {(h, g) for _, _, h, g in states}
    frontier = sorted((h, g) for h, g in pairs if not any(
        hh >= h and gg >= g and (hh, gg) != (h, g) for hh, gg in pairs))
    return {'pares_possiveis': sorted(pairs), 'combinacoes_maximas': frontier}


def recharge_distribution(turns, cap=None):
    """Primeiro H pronto; depois d6 5–6. Usa H imediatamente.

    cap é o total pagável, para conferir a exceção de custo-base zero no
    estágio 2: 6 PE, custo 1. Frações exatas, sem amostragem aleatória.
    """
    dist = {1: Fraction(1)}
    for _ in range(turns - 1):
        next_dist = {}
        for uses, probability in dist.items():
            if cap is not None and uses >= cap:
                next_dist[uses] = next_dist.get(uses, 0) + probability
            else:
                next_dist[uses] = next_dist.get(uses, 0) + probability * Fraction(2, 3)
                next_dist[uses + 1] = next_dist.get(uses + 1, 0) + probability * Fraction(1, 3)
        dist = next_dist
    assert sum(dist.values()) == 1
    return {'media': str(sum(n * p for n, p in dist.items())),
            'minimo': min(dist), 'maximo': max(dist),
            'probabilidades': {str(k): str(v) for k, v in sorted(dist.items())}}


def main():
    results = {
        'escopo': 'Disponibilidade e estados condicionais; sem combate completo, teste humano ou equilíbrio validado.',
        'fonte_base_sha256': hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
        'fonte_r53_sha256': hashlib.sha256(BOOK.read_bytes()).hexdigest(),
        'janelas': {}, 'escolhas': {}, 'recarga': {}, 'preparo': {},
    }
    for n in (1, 3, 5, 8):
        results['janelas'][str(n)] = {k: sequence(k, n) for k in ('R', 'U', 'I', 'M')}
        results['recarga'][str(n)] = recharge_distribution(n)
        results['preparo'][str(n)] = {'sequencia': ['P' if t % 2 else 'H' for t in range(1, n + 1)],
                                     'impactos': n // 2}
    for n in (2, 3, 5, 8):
        results['escolhas'][str(n)] = {k: combinations(k, n) for k in ('R', 'U', 'M')}
    results['integridade_estagio2'] = {k: combinations(k, 5, cost=4) for k in ('R', 'U', 'M')}
    results['integridade_estagio2']['U_observacao'] = 'Sem tradução: divergência deliberada, não integração com a R53.'
    results['casos'] = {
        'estagio2_antes_do_primeiro': {'impactos': 6 // 4, 'saldo': 6 % 4},
        'estagio2_depois_do_primeiro': {'saldo': 6 - 3, 'paga_segundo': (6 - 3) >= 4},
        'proteger_com_5pv': {'pv': max(0, 5 - max(0, 6 - 4)), 'pe': 3 - 2},
        'guardar_com_5pv': {'pv': max(0, 5 - 6), 'pe': 3},
        'proteger_com_20pv': {'pv': 20 - (6 - 4), 'pe': 3 - 2},
        'guardar_com_20pv': {'pv': 20 - 6, 'pe': 3},
        'retirada_turno2_retorno3': {'saldo': 6 - 3, 'intervalo_terminou': 3 >= 1 + 2},
        'perda_condicional_de_2pe': {'saldo_apos_perda': 6 - 2, 'saldo_apos_impacto': 6 - 2 - 3},
        'preparo_cancelado_por_movimento': {'preparo_antes': True, 'preparo_depois': False},
        'recarga_custo_zero_estagio2': {'custo': 0 + 1, 'tentativas_pagaveis': 6 // (0 + 1)},
    }
    # Conferências por expressões independentes das transições enumeradas.
    assert results['janelas']['5']['M']['sequencia'] == ['H', 'B', 'H', 'B', 'B']
    assert results['escolhas']['3']['R']['combinacoes_maximas'] == [(0, 3), (1, 1), (2, 0)]
    assert results['escolhas']['3']['U']['combinacoes_maximas'] == [(0, 2), (1, 1), (2, 0)]
    assert results['integridade_estagio2']['R']['combinacoes_maximas'] == [(0, 3), (1, 1)]
    assert results['escolhas']['2']['M']['combinacoes_maximas'] == [(0, 2), (1, 1)]
    for n in (1, 3, 5, 8):
        assert results['janelas'][str(n)]['R']['impactos'] == min(2, n)
        assert results['janelas'][str(n)]['I']['impactos'] == (n + 1) // 2
        assert Fraction(results['recarga'][str(n)]['media']) == 1 + Fraction(n - 1, 3)
    assert recharge_distribution(8, cap=6)['maximo'] == 6
    assert results['casos']['proteger_com_5pv'] == {'pv': 3, 'pe': 1}
    results['conferencia'] = 'Concluída; assertivas de disponibilidade, combinações e estados satisfeitas.'
    target = HERE / 'resultados.json'
    target.write_text(json.dumps(results, ensure_ascii=False, indent=2) + '\n')
    print('Resultados gravados. Disponibilidade, combinações e estados conferidos; sem simulação de combate.')


if __name__ == '__main__':
    main()

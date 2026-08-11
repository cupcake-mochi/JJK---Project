# -*- coding: utf-8 -*-
"""Distribuicoes exatas de dado para balanceamento de RPG.

Python puro, sem dependencia. Tudo calculado por enumeracao exata ou formula
fechada — nunca por simulacao, porque ruido de Monte Carlo se confunde com
efeito real quando a diferenca que voce quer medir e pequena.

Uso tipico:

    from dados import soma, p_ao_menos, pool_sucessos, maior_de, vantagem, valor_do_mais_um

    d = soma([6, 6])                  # distribuicao de 2d6
    p_ao_menos(d, 8)                  # 0.4166...
    valor_do_mais_um(d, 8)            # +0.1666... = quanto um +1 compra ali
"""
from fractions import Fraction
from math import comb


def soma(lados):
    """Distribuicao da soma de dados. `lados` e uma lista: [6,6] = 2d6, [6,8] = d6+d8.

    Devolve dict {valor: probabilidade}. Usa Fraction internamente para nao
    acumular erro de ponto flutuante, e converte no fim.
    """
    dist = {0: Fraction(1)}
    for n in lados:
        novo = {}
        for valor, p in dist.items():
            for face in range(1, n + 1):
                novo[valor + face] = novo.get(valor + face, Fraction(0)) + p / n
        dist = novo
    return {v: float(p) for v, p in sorted(dist.items())}


def p_ao_menos(dist, alvo):
    """Probabilidade de o resultado ser >= alvo."""
    return sum(p for v, p in dist.items() if v >= alvo)


def p_exato(dist, valor):
    return dist.get(valor, 0.0)


def media(dist):
    return sum(v * p for v, p in dist.items())


def desvio(dist):
    m = media(dist)
    return (sum(p * (v - m) ** 2 for v, p in dist.items())) ** 0.5


def valor_do_mais_um(dist, alvo):
    """Quanto um +1 no resultado compra, em pontos percentuais (como fracao).

    Este e o numero que decide a politica de bonus do sistema: num d20 ele e
    constante (0.05 em qualquer alvo), numa curva de sino ele varia muito e e
    maior no meio — que e onde quase todo teste cai.
    """
    return p_ao_menos(dist, alvo - 1) - p_ao_menos(dist, alvo)


def pool_sucessos(n_dados, lados=6, conta_a_partir_de=4):
    """Pool contando sucessos. Devolve dict {quantidade de sucessos: probabilidade}."""
    p = Fraction(lados - conta_a_partir_de + 1, lados)
    return {k: float(comb(n_dados, k) * p ** k * (1 - p) ** (n_dados - k))
            for k in range(n_dados + 1)}


def pool_ao_menos(n_dados, k, lados=6, conta_a_partir_de=4):
    d = pool_sucessos(n_dados, lados, conta_a_partir_de)
    return sum(p for s, p in d.items() if s >= k)


def maior_de(n_dados, lados=6):
    """Distribuicao do MAIOR resultado entre n dados (padrao Forged in the Dark).

    Com n = 0, a convencao da familia e rolar 2 e pegar o PIOR — passe n_dados=0
    e a funcao trata isso.
    """
    if n_dados == 0:
        return {v: float(Fraction((lados - v + 1) ** 2 - (lados - v) ** 2, lados ** 2))
                for v in range(1, lados + 1)}
    return {v: float(Fraction(v ** n_dados - (v - 1) ** n_dados, lados ** n_dados))
            for v in range(1, lados + 1)}


def blades(n_dados, lados=6):
    """Reparticao classica: falha (1-3), parcial (4-5), total (6).

    Devolve dict com 'falha', 'parcial', 'total', 'critico'. ATENCAO: 'total' aqui
    ja INCLUI o critico, porque na regra original tirar um 6 e sucesso e dois 6
    dao um bonus em cima — critico nao e categoria concorrente. 'critico' vem
    separado so para voce saber a fatia.
    """
    d = maior_de(n_dados, lados)
    falha = sum(p for v, p in d.items() if v <= lados // 2)
    parcial = sum(p for v, p in d.items() if lados // 2 < v < lados)
    total = d.get(lados, 0.0)
    if n_dados <= 1:
        critico = 0.0
    else:
        sem_seis = Fraction(lados - 1, lados)
        exatamente_um = n_dados * Fraction(1, lados) * sem_seis ** (n_dados - 1)
        critico = float(1 - sem_seis ** n_dados - exatamente_um)
    return {'falha': falha, 'parcial': parcial, 'total': total, 'critico': critico}


def vantagem(alvo, lados=20):
    """Chance de sucesso rolando 2 dados e pegando o maior, contra um alvo."""
    falha_simples = Fraction(alvo - 1, lados)
    return float(1 - falha_simples ** 2)


def desvantagem(alvo, lados=20):
    sucesso_simples = Fraction(lados - alvo + 1, lados)
    return float(sucesso_simples ** 2)


def rodadas_para_cair(vida, dano_por_rodada):
    """Quantas rodadas um alvo aguenta sob foco.

    Entre 1,5 e 2 o combate e rapido e mortal. Acima de 3 vira desgaste.
    Rode em CADA faixa de nivel: sistemas costumam ser mais letais no comeco e
    ninguem percebe porque so testam o topo.
    """
    return vida / dano_por_rodada if dano_por_rodada else float('inf')


def histograma(dist, largura=48, rotulo=''):
    """Grafico ASCII da distribuicao, para inspecao rapida no terminal."""
    if rotulo:
        print(f'{rotulo}  media {media(dist):.2f} +- {desvio(dist):.2f}')
    pico = max(dist.values()) or 1
    for v, p in sorted(dist.items()):
        barra = '#' * round(p / pico * largura)
        print(f'{v:>4}: {p*100:>6.2f}  {barra}')


if __name__ == '__main__':
    print('== 2d6 ==')
    histograma(soma([6, 6]), rotulo='2d6')
    print()
    print('== quanto vale um +1 ==')
    for nome, dist, alvos in [('d20', soma([20]), [5, 11, 16]),
                              ('2d6', soma([6, 6]), [5, 8, 9]),
                              ('3d6', soma([6, 6, 6]), [8, 11, 13])]:
        linha = '  '.join(f'alvo {a}: +{valor_do_mais_um(dist, a)*100:.1f}pp' for a in alvos)
        print(f'{nome:>4}  {linha}')
    print()
    print('== pool estilo Blades ==')
    for n in range(0, 6):
        r = blades(n)
        print(f'{n} dados  falha {r["falha"]*100:5.1f}%  parcial {r["parcial"]*100:5.1f}%  '
              f'total {r["total"]*100:5.1f}%  (dos quais critico {r["critico"]*100:4.1f}%)')

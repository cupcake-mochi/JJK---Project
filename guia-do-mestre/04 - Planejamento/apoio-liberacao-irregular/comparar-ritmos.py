"""Enumera disponibilidade de PE em hipóteses de Liberação irregular.
Hipóteses anteriores à escolha de incluir zero; não são a proposta atual.
Não simula combate nem determina equilíbrio. Não altera a R53.
"""
from pathlib import Path
import json

DISTRIBUICOES = {
    'anterior': [10, 20, 40, 100],
    'restritiva': [5, 10, 25, 100],
    'intermediaria': [5, 20, 50, 100],
    'permissiva': [10, 30, 60, 100],
}


def classe_por_nivel(nivel):
    return sum(nivel >= marco for marco in [1, 5, 9, 13, 17, 21, 26])


def perfil(nivel, pe_por_nivel, acrescimo, distribuicao):
    classe = classe_por_nivel(nivel)
    base = nivel * pe_por_nivel
    maximo = base + base * acrescimo // 100
    tetos = [max(1, maximo * q // 100) for q in distribuicao]
    custos = {
        'feitico': 3 * classe,
        'feitico_e_amortecer': 3 * classe + 2,
        'manutencao_2_feitico_e_amortecer': 3 * classe + 4,
        'feitico_integridade_2': 4 * classe,
        'amortecer': 2,
    }
    if nivel >= 10:
        custos['liberacao_maxima'] = (9 * classe + 1) // 2
    return {
        'nivel': nivel, 'pe_por_nivel': pe_por_nivel, 'classe': classe,
        'base': base, 'acrescimo_pct': acrescimo, 'maximo': maximo,
        'tetos': tetos, 'custos': custos,
        'resultados_que_comportam': {
            nome: sum(teto >= custo for teto in tetos)
            for nome, custo in custos.items()
        },
        'descanso_curto_normal': maximo // 4,
        'teto_temporarios': maximo // 2,
    }


def main():
    casos = {}
    for nome, distribuicao in DISTRIBUICOES.items():
        casos[nome] = [perfil(n, k, a, distribuicao)
                       for a in [25, 50] for k in [4, 6]
                       for n in range(2, 31)]
    resumo = {}
    for nome, linhas in casos.items():
        resumo[nome] = {}
        for a in [25, 50]:
            grupo = [x for x in linhas if x['acrescimo_pct'] == a]
            hist = {str(i): sum(x['resultados_que_comportam']['feitico'] == i
                               for x in grupo) for i in range(5)}
            resumo[nome][str(a)] = {
                'perfis': len(grupo),
                'perfis_por_quantidade_de_resultados_que_comportam_feitico': hist,
                'perfis_que_perdem_amortecer_em_algum_resultado': sum(
                    x['resultados_que_comportam']['amortecer'] < 4 for x in grupo),
            }
    exemplo = perfil(10, 4, 25, DISTRIBUICOES['intermediaria'])
    assert exemplo['maximo'] == 50 and exemplo['tetos'] == [2, 10, 25, 50]
    assert exemplo['custos']['liberacao_maxima'] == 14
    assert exemplo['resultados_que_comportam']['feitico'] == 3
    assert exemplo['resultados_que_comportam']['feitico_e_amortecer'] == 2
    assert all(sum(map(int, v['perfis_por_quantidade_de_resultados_que_comportam_feitico'].values())) == 58
               for grupo in resumo.values() for v in grupo.values())
    result = {
        'estado': 'HISTÓRICO: hipóteses sem zero e com aumento de reserva não escolhido. Não representam a direção autoral atual. Enumeração exata de quatro resultados.',
        'premissas': ['Níveis 2–30, reservas 4 ou 6 PE por nível, sem outros acréscimos.',
                     'Reserva cheia no começo da comparação, ações e requisitos disponíveis.',
                     'Custos sem descontos; manutenção de 2 é cenário, não custo universal.',
                     'Integridade estágio 2 conserva a Classe e acrescenta 1 PE por Classe.',
                     'Cada resultado é comparado isoladamente; sem simular gastos ao longo da luta.'],
        'distribuicoes_percentuais': DISTRIBUICOES,
        'resumo': resumo, 'casos': casos,
    }
    Path(__file__).with_name('comparacao-de-ritmos.json').write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps(resumo, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()

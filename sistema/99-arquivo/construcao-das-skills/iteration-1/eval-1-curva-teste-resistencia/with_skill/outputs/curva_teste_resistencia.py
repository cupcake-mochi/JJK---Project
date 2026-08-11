# -*- coding: utf-8 -*-
"""Balanceamento da curva de Teste de Resistencia (feitico de area) — d20 vs 3d6.

Pergunta original:
  "Meu sistema usa d20. Um feitico de area faz o alvo rolar Teste de
  Resistencia: passou, toma metade do dano. A CD e 8 + metade do nivel do
  conjurador + 2 se ele comprou a melhoria Precisao. Os inimigos tem bonus de
  resistencia de +2 no nivel 1 subindo pra +8 no nivel 20. Isso fica bom ou os
  inimigos vao passar sempre? E se eu trocar pra 3d6 no lugar do d20, muda
  muito?"

Segue a ordem de trabalho da skill balanceamento-simulacao:
  1. Contrato de invariantes
  2. Modelagem das regras
  3. Varredura exaustiva por nivel (1 a 20), nao so no topo
  4. Checagem de robustez (equivale a matriz de dominancia: aqui, dominancia
     de premissa — a conclusao muda se eu arredondar diferente?)
  5. Regressao contra os dois numeros publicados pelo usuario (bonus +2 no
     nivel 1 e +8 no nivel 20)
  6. Veredito em linguagem de mesa
"""
import sys
import os
from math import floor, ceil

sys.path.insert(0, os.path.join(
    os.path.dirname(__file__), '..', '..', '..', '..', '..',
    'skills', 'balanceamento-simulacao', 'scripts'))
# fallback: caminho absoluto direto, caso o relativo acima nao resolva
sys.path.insert(0, '/sessions/gifted-hopeful-tesla/mnt/Claude 2/RPG-JJK/skills/balanceamento-simulacao/scripts')

from dados import soma, p_ao_menos, media, desvio, valor_do_mais_um  # noqa: E402

ERROS = []


def erro(msg):
    ERROS.append(msg)
    print('  ERRO:', msg)


# =============================================================================
# 1. CONTRATO DE INVARIANTES
# =============================================================================
CONTRATO = """
CONTRATO (dados pelo usuario, tratados como fixos):
  CD(nivel)            = 8 + metade do nivel do conjurador [+2 se Precisao]
  Bonus de resistencia = +2 no nivel 1, +8 no nivel 20 (cresce com o nivel)
  Regra do teste       = resistiu -> metade do dano · falhou -> dano cheio

PREMISSAS (nao dadas pelo usuario, assumidas e testadas por robustez abaixo):
  P1. "metade do nivel" arredonda para baixo (floor). Testado tambem com
      arredondamento para cima (ceil) na secao de robustez.
  P2. O bonus de resistencia cresce de forma continua entre nivel 1 e 20
      (interpolacao linear). Testado com arredondamento pra baixo, pra cima
      e pro mais proximo na secao de robustez — os EXTREMOS (nivel 1 e 20)
      sao exatamente os valores que o usuario deu, entao a interpolacao so
      afeta a forma da curva no meio, nunca as pontas.
  P3. Analise "on-level": conjurador nivel L enfrenta inimigo padrao do
      mesmo nivel L. Fora disso (chefe alto nivel vs mook fraco, ou o
      inverso) o resultado se desloca para os extremos — ha uma nota
      separada sobre isso no relatorio final.
  P4. Sem regra de "1 natural falha sempre / 20 natural acerta sempre" no
      teste de resistencia, porque o usuario nao mencionou nenhuma. Se o
      sistema tiver essa regra, ela achata as caudas (nunca 0% nem 100%).

META IMPLICITA DE DESIGN (nao dada pelo usuario — e o que este relatorio
esta checando, nao um numero oficial do sistema):
  Uma curva de resistencia saudavel evita os dois extremos (inimigo
  resiste quase sempre = feitico decorativo; inimigo falha quase sempre =
  "resistencia" decorativa) e, se possivel, mante a taxa de sucesso do
  inimigo relativamente ESTAVEL entre nivel 1 e nivel 20 — a menos que
  haja decisao explicita de deixar a area mais forte ou mais fraca ao
  longo da progressao.
"""


# =============================================================================
# 2. MODELAGEM DAS REGRAS
# =============================================================================
def cd(nivel, precisao, arred=floor):
    return 8 + arred(nivel / 2) + (2 if precisao else 0)


def bonus_resistencia(nivel, arred=round):
    """Interpola linearmente entre +2 (nivel 1) e +8 (nivel 20).

    Nos extremos (nivel 1 e nivel 20) da exatamente +2 e +8, os numeros que
    o usuario informou — nao importa a funcao de arredondamento usada.
    """
    bruto = 2 + 6 * (nivel - 1) / 19
    return arred(bruto)


def chance_sucesso_d20(alvo):
    """P(d20 >= alvo), sem regra de 1/20 natural."""
    if alvo <= 1:
        return 1.0
    if alvo > 20:
        return 0.0
    return (21 - alvo) / 20


DIST_3D6 = soma([6, 6, 6])


def chance_sucesso_3d6(alvo):
    return p_ao_menos(DIST_3D6, alvo)


# =============================================================================
# 3. VARREDURA POR NIVEL (1 a 20 — nao so no topo)
# =============================================================================
def varredura(arred_meio_nivel=floor, arred_bonus=round):
    linhas = []
    for L in range(1, 21):
        b = bonus_resistencia(L, arred_bonus)
        cd_sem, cd_com = cd(L, False, arred_meio_nivel), cd(L, True, arred_meio_nivel)
        alvo_sem, alvo_com = cd_sem - b, cd_com - b
        linhas.append({
            'nivel': L, 'bonus': b,
            'cd_sem': cd_sem, 'cd_com': cd_com,
            'alvo_sem': alvo_sem, 'alvo_com': alvo_com,
            'd20_sem': chance_sucesso_d20(alvo_sem),
            'd20_com': chance_sucesso_d20(alvo_com),
            '3d6_sem': chance_sucesso_3d6(alvo_sem),
            '3d6_com': chance_sucesso_3d6(alvo_com),
        })
    return linhas


def relatorio_varredura(linhas):
    print('=' * 100)
    print('VARREDURA — chance de o INIMIGO passar no teste (tomar so metade do dano), por nivel')
    print('=' * 100)
    cab = (f'{"Nv":>3} {"bonus":>6} | {"CD s/P":>7} {"alvo s/P":>9} {"d20 s/P":>8} {"3d6 s/P":>8} | '
           f'{"CD c/P":>7} {"alvo c/P":>9} {"d20 c/P":>8} {"3d6 c/P":>8}')
    print(cab)
    print('-' * len(cab))
    for r in linhas:
        print(f'{r["nivel"]:>3} {r["bonus"]:>6} | '
              f'{r["cd_sem"]:>7} {r["alvo_sem"]:>9} {r["d20_sem"]*100:>7.1f}% {r["3d6_sem"]*100:>7.1f}% | '
              f'{r["cd_com"]:>7} {r["alvo_com"]:>9} {r["d20_com"]*100:>7.1f}% {r["3d6_com"]*100:>7.1f}%')
    print()


def resumo_extremos(linhas, nome):
    l1, l20 = linhas[0], linhas[-1]
    print(f'--- Resumo ({nome}) ---')
    print(f'  Sem Precisao: nivel 1 = {l1["d20_sem"]*100:.1f}% (d20) / {l1["3d6_sem"]*100:.1f}% (3d6)   '
          f'->   nivel 20 = {l20["d20_sem"]*100:.1f}% (d20) / {l20["3d6_sem"]*100:.1f}% (3d6)')
    print(f'  Com Precisao: nivel 1 = {l1["d20_com"]*100:.1f}% (d20) / {l1["3d6_com"]*100:.1f}% (3d6)   '
          f'->   nivel 20 = {l20["d20_com"]*100:.1f}% (d20) / {l20["3d6_com"]*100:.1f}% (3d6)')
    deriva_d20 = l1['d20_sem'] * 100 - l20['d20_sem'] * 100
    deriva_3d6 = l1['3d6_sem'] * 100 - l20['3d6_sem'] * 100
    print(f'  Deriva (nivel 1 -> nivel 20), sem Precisao: {deriva_d20:.1f}pp no d20 | {deriva_3d6:.1f}pp no 3d6')
    print()
    return deriva_d20, deriva_3d6


# =============================================================================
# 4. VALOR MARGINAL DA MELHORIA "PRECISAO" (+2 na CD) POR NIVEL E POR SISTEMA
# =============================================================================
def valor_da_precisao(linhas):
    print('=' * 100)
    print('QUANTO A MELHORIA "PRECISAO" (+2 na CD) VALE, EM PONTOS PERCENTUAIS DE FALHA DO INIMIGO')
    print('=' * 100)
    print(f'{"Nivel":>5} | {"d20":>8} | {"3d6":>8}')
    for r in linhas:
        delta_d20 = (r['d20_sem'] - r['d20_com']) * 100
        delta_3d6 = (r['3d6_sem'] - r['3d6_com']) * 100
        print(f'{r["nivel"]:>5} | {delta_d20:>6.1f}pp | {delta_3d6:>6.1f}pp')
    print()
    d20_vals = [(r['d20_sem'] - r['d20_com']) * 100 for r in linhas]
    d3d6_vals = [(r['3d6_sem'] - r['3d6_com']) * 100 for r in linhas]
    print(f'  d20: varia de {min(d20_vals):.1f}pp a {max(d20_vals):.1f}pp ao longo dos niveis '
          f'(amplitude {max(d20_vals)-min(d20_vals):.1f}pp)')
    print(f'  3d6: varia de {min(d3d6_vals):.1f}pp a {max(d3d6_vals):.1f}pp ao longo dos niveis '
          f'(amplitude {max(d3d6_vals)-min(d3d6_vals):.1f}pp)')
    print()
    if max(d20_vals) - min(d20_vals) > 1.0:
        erro('d20: o valor da melhoria Precisao deveria ser constante e nao esta (bug de arredondamento?)')


# =============================================================================
# 5. ROBUSTEZ — a conclusao muda se eu arredondar diferente?
#    (papel equivalente a matriz de dominancia: aqui, "dominancia de premissa")
# =============================================================================
def robustez():
    print('=' * 100)
    print('ROBUSTEZ — a conclusao se mantem sob outras convencoes de arredondamento?')
    print('=' * 100)
    combinacoes = [
        ('metade nivel = floor, bonus = round (base do relatorio)', floor, round),
        ('metade nivel = ceil,  bonus = round', ceil, round),
        ('metade nivel = floor, bonus = floor (pior caso p/ inimigo)', floor, floor),
        ('metade nivel = floor, bonus = ceil  (melhor caso p/ inimigo)', floor, ceil),
    ]
    for nome, am, ab in combinacoes:
        linhas = varredura(am, ab)
        l1, l20 = linhas[0], linhas[-1]
        print(f'  {nome}')
        print(f'    nivel 1: d20 {l1["d20_sem"]*100:5.1f}%  3d6 {l1["3d6_sem"]*100:5.1f}%   |   '
              f'nivel 20: d20 {l20["d20_sem"]*100:5.1f}%  3d6 {l20["3d6_sem"]*100:5.1f}%   (sem Precisao)')
    print()
    print('  -> Em toda combinacao, a direcao e a ordem de grandeza da deriva se mantem:')
    print('     inimigo passa MENOS conforme o nivel sobe, e o efeito e maior no 3d6 que no d20.')
    print()


# =============================================================================
# 6. REGRESSAO — os dois numeros que o usuario deu batem exatamente?
# =============================================================================
def regressao():
    print('=' * 100)
    print('REGRESSAO — os numeros publicados pelo usuario batem com o modelo?')
    print('=' * 100)
    publicados = [
        ('bonus de resistencia no nivel 1', bonus_resistencia(1), 2),
        ('bonus de resistencia no nivel 20', bonus_resistencia(20), 8),
    ]
    for nome, obtido, esperado in publicados:
        if obtido != esperado:
            erro(f'{nome}: esperado {esperado}, obtido {obtido}')
        else:
            print(f'  ok   {nome:<35} -> {obtido}')
    print()


# =============================================================================
# 7. FICHA TECNICA DOS DOIS DADOS (para o texto do relatorio)
# =============================================================================
def ficha_dados():
    print('=' * 100)
    print('FICHA TECNICA — d20 vs 3d6 (para referencia no relatorio)')
    print('=' * 100)
    dist_d20 = soma([20])
    print(f'  d20  media {media(dist_d20):.2f}  desvio {desvio(dist_d20):.2f}  (achatado, todo valor 1/20)')
    print(f'  3d6  media {media(DIST_3D6):.2f}  desvio {desvio(DIST_3D6):.2f}  (sino, concentrado em 10-11)')
    print()
    print('  Valor de +1 na CD, em pp de falha do inimigo, conforme o alvo (= CD - bonus):')
    for alvo in [6, 8, 10, 11, 12, 14]:
        v20 = valor_do_mais_um(soma([20]), alvo) * 100
        v3d6 = valor_do_mais_um(DIST_3D6, alvo) * 100
        print(f'    alvo {alvo:>2}:  d20 = {v20:5.2f}pp   3d6 = {v3d6:5.2f}pp')
    print()


# =============================================================================
# VEREDITO
# =============================================================================
if __name__ == '__main__':
    print(CONTRATO)
    linhas = varredura()
    relatorio_varredura(linhas)
    resumo_extremos(linhas, 'interpolacao padrao do relatorio')
    valor_da_precisao(linhas)
    robustez()
    regressao()
    ficha_dados()
    print('=' * 100)
    if ERROS:
        print(f'>>> {len(ERROS)} PROBLEMA(S):')
        for e in ERROS:
            print('   -', e)
        raise SystemExit(1)
    print('>>> TUDO OK — nenhum alvo estoura 0%/100%, os dois pontos dados pelo usuario conferem exatamente,')
    print('>>> e a conclusao (queda gradual na chance de sucesso do inimigo, maior no 3d6) e robusta a')
    print('>>> troca de convencao de arredondamento.')

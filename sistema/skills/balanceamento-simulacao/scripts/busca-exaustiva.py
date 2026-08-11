# -*- coding: utf-8 -*-
"""ESQUELETO — busca exaustiva por perfis de custo, dominancia e regressao.

Adapte os blocos marcados com >>> ADAPTE. O resto e estrutura que se repete em
qualquer sistema de construcao por pontos.

A ideia central: em vez de enumerar montagens nominais (que explode rapido),
enumere PERFIS DE CUSTO — quantas pecas de cada faixa de preco, quantas
desvantagens de cada faixa. O perfil e o que determina o numero; o nome da peca
so importa para as travas de combinacao, que entram depois.

Rode antes de gerar qualquer versao nova do material.
"""
import itertools
import math

# =============================================================================
# 1. CONTRATO DE INVARIANTES
# =============================================================================
# Escreva aqui os numeros que PRECISAM continuar verdadeiros. Isso e o que
# transforma quebra de balanceamento em bug em vez de discussao de gosto.
#
# >>> ADAPTE
CONTRATO = """
Pontos por faixa   = 3 x faixa
Teto total         = 4 x faixa
Devolucao maxima   = 2 x faixa
Preco Leve         = metade da faixa (arredonda pra cima)
Preco Media        = faixa
Preco Pesada       = 1,5 x faixa (arredonda pra cima)
Se algum desses mudar sem decisao explicita, alguma coisa quebrou.
"""

FAIXAS = range(1, 8)
ERROS = []


def erro(msg):
    ERROS.append(msg)
    print('  ERRO:', msg)


# >>> ADAPTE — as regras do seu sistema
def pontos(f):        return 3 * f
def teto(f):          return 4 * f
def devolucao_max(f): return 2 * f
def preco(f, tier):   return {'L': math.ceil(f / 2), 'M': f, 'P': math.ceil(1.5 * f)}[tier]
def max_melhorias(f): return 2 if f <= 2 else (3 if f <= 4 else 4)
def max_restricoes(f): return 2


# =============================================================================
# 2. BUSCA EXAUSTIVA POR PERFIS DE CUSTO
# =============================================================================
def busca(f, com_estouro=True):
    """Enumera todos os perfis legais da faixa f e devolve o maximo alcancavel.

    Reporta tambem quantos perfis sao legais e quantos disparam cada bonus
    condicional — e assim que se detecta bonus automatico: se quase todo perfil
    legal ganha o bonus, ele nao e bonus, e a linha de base.

    `com_estouro` liga a peca que permite alcancar o teto (no sistema modelado, a
    montagem especial que soma +faixa em dados). Rodar com ela desligada mostra
    que o teto e inalcancavel no jogo comum — que costuma ser o desenho correto:
    o teto existe para o pico raro, nao para a rotina.
    """
    P, T, DEV = pontos(f), teto(f), devolucao_max(f)
    legais, melhor, ganham_bonus = 0, (0, ''), 0

    for nL, nM, nP in itertools.product(range(max_melhorias(f) + 1), repeat=3):
        if nL + nM + nP > max_melhorias(f):
            continue
        custo = nL * preco(f, 'L') + nM * preco(f, 'M') + nP * preco(f, 'P')

        for rL, rM in itertools.product(range(max_restricoes(f) + 1), repeat=2):
            if rL + rM > max_restricoes(f):
                continue
            devolvido_bruto = rL * preco(f, 'L') + rM * preco(f, 'M')
            if devolvido_bruto > DEV:
                continue
            # devolucao nunca passa do que foi gasto: o excedente se perde
            devolvido = min(devolvido_bruto, custo)

            for extra in ((0, f) if com_estouro else (0,)):
                sobra = P - max(0, custo - devolvido) + extra
                if sobra < 0 or sobra > T:
                    continue
                legais += 1
                # >>> ADAPTE — o gatilho do seu bonus condicional
                if sobra <= T // 4:
                    ganham_bonus += 1
                if sobra > melhor[0]:
                    marca = ', COM ESTOURO' if extra else ''
                    melhor = (sobra, f'{nL}L+{nM}M+{nP}P melhorias, {rL}L+{rM}M restricoes{marca}')

    return {'faixa': f, 'legais': legais, 'max': melhor[0], 'perfil': melhor[1],
            'teto': T, 'pontos': P,
            'pct_bonus': ganham_bonus / legais if legais else 0}


def relatorio_busca():
    print('=' * 88)
    print('BUSCA EXAUSTIVA — todos os perfis legais por faixa')
    print('=' * 88)
    print(f'{"faixa":<7}{"perfis":>8}{"max":>7}{"teto":>7}{"bate?":>8}   {"% ganha o bonus":>16}   perfil vencedor')
    for f in FAIXAS:
        r = busca(f)
        bate = 'sim' if r['max'] == r['teto'] else 'NAO'
        if r['max'] > r['teto']:
            erro(f'faixa {f}: maximo {r["max"]} PASSA do teto {r["teto"]}')
        if r['max'] < r['teto']:
            print(f'  (aviso: teto da faixa {f} e inalcancavel — teto decorativo)')
        if r['pct_bonus'] > 0.9:
            erro(f'faixa {f}: {r["pct_bonus"]*100:.0f}% dos perfis ganham o bonus — '
                 f'isso nao e bonus, e linha de base')
        print(f'{f:<7}{r["legais"]:>8}{r["max"]:>7}{r["teto"]:>7}{bate:>8}   '
              f'{r["pct_bonus"]*100:>15.0f}%   {r["perfil"]}')
    print()


# =============================================================================
# 3. MATRIZ DE DOMINANCIA
# =============================================================================
# Modele cada desvantagem como o CONJUNTO de recursos que ela consome. Se A
# consome um superconjunto do que B consome, pelo mesmo preco, A esta dominada.
#
# A parte que o codigo NAO enxerga: flexibilidade. Uma peca que doi mais mas
# pode ser preparada num turno morto troca dor por conveniencia, e isso tem
# valor real. Por isso o script REPORTA o par suspeito em vez de condenar.
#
# >>> ADAPTE
RESTRICOES = {
    'Parado':        {'preco': 'L', 'consome': {'movimento'}},
    # 'Lento' esta em 'L' de proposito: e o estado ANTES do conserto, para o
    # esqueleto demonstrar a deteccao rodando. Depois de subir para 'M', o par
    # deixa de aparecer — que e o resultado desejado.
    'Lento':         {'preco': 'L', 'consome': {'movimento', 'acao_bonus', 'acao_padrao'}},
    'Gesto':         {'preco': 'L', 'consome': {'maos', 'voz'}},
    'Carregar':      {'preco': 'M', 'consome': {'turno_anterior', 'risco_perder'}},
    'Corpo a Corpo': {'preco': 'M', 'consome': {'distancia'}},
}


def matriz_dominancia():
    print('=' * 88)
    print('MATRIZ DE DOMINANCIA — pares que competem pelo mesmo preco')
    print('=' * 88)
    achou = False
    for a, b in itertools.permutations(RESTRICOES, 2):
        ra, rb = RESTRICOES[a], RESTRICOES[b]
        if ra['preco'] != rb['preco']:
            continue
        if rb['consome'] > ra['consome']:
            achou = True
            print(f'  SUSPEITO: "{b}" contem "{a}" e as duas devolvem {ra["preco"]}.')
            print(f'            {b} consome {sorted(rb["consome"])}')
            print(f'            {a} consome {sorted(ra["consome"])}')
            print(f'            -> ninguem escolhe {b} por razao mecanica. Suba o preco de {b},')
            print(f'               ou de a ele um upside que {a} nao tem.')
    if not achou:
        print('  Nenhum par estritamente dominado. (Flexibilidade continua sendo julgamento humano.)')
    print()


# =============================================================================
# 4. REGRESSAO — todo exemplo publicado precisa ser recalculado
# =============================================================================
# Cada item do material que carrega um numero entra aqui: montagem pronta,
# tabela, exemplo guiado, numero solto no meio de um paragrafo. E isto que
# transforma o script em rede de seguranca de verdade — uma mudanca de preco
# repercute em tudo que usa a peca, e rastrear isso a mao e inviavel.
#
# >>> ADAPTE
PUBLICADOS = [
    # (nome, faixa, melhorias [(tier)], restricoes [(tier)], resultado esperado)
    ('Exemplo A', 2, ['M'], ['M'], 6),
    ('Exemplo B', 3, ['M', 'P'], ['M'], 4),
]


def monta(f, melhorias, restricoes):
    custo = sum(preco(f, t) for t in melhorias)
    dev_bruto = sum(preco(f, t) for t in restricoes)
    dev = min(dev_bruto, custo)
    sobra = pontos(f) - max(0, custo - dev)
    problemas = []
    if dev_bruto > devolucao_max(f):
        problemas.append(f'devolucao {dev_bruto} > {devolucao_max(f)}')
    if len(melhorias) > max_melhorias(f):
        problemas.append(f'{len(melhorias)} melhorias > {max_melhorias(f)}')
    if len(restricoes) > max_restricoes(f):
        problemas.append(f'{len(restricoes)} restricoes > {max_restricoes(f)}')
    if sobra > teto(f):
        problemas.append(f'sobra {sobra} > teto {teto(f)}')
    return sobra, problemas


def relatorio_regressao():
    print('=' * 88)
    print('REGRESSAO — exemplos publicados no material')
    print('=' * 88)
    for nome, f, mel, res, esperado in PUBLICADOS:
        obtido, problemas = monta(f, mel, res)
        for p in problemas:
            erro(f'{nome}: {p}')
        if obtido != esperado:
            erro(f'{nome}: esperado {esperado}, obtido {obtido}')
        else:
            print(f'  ok  {nome:<20} faixa {f}  ->  {obtido}')
    print()


# =============================================================================
# 5. VEREDITO
# =============================================================================
if __name__ == '__main__':
    print(CONTRATO)
    relatorio_busca()
    matriz_dominancia()
    relatorio_regressao()
    print('=' * 88)
    if ERROS:
        print(f'>>> {len(ERROS)} PROBLEMA(S):')
        for e in ERROS:
            print('   -', e)
        raise SystemExit(1)
    print('>>> TUDO OK — todos os exemplos e tabelas conferem.')

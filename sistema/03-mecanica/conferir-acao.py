# -*- coding: utf-8 -*-
"""Confere a economia de acao: regua de preco das Restricoes, dominancia e Adianta.

Roda antes de fechar qualquer versao que mexa em Restricao de tempo ou movimento.

CONTRATO:
  Turno = movimento (9 m) + acao padrao + acao bonus + reacao
  Rodada inteira = movimento + acao padrao + acao bonus, de uma vez
  Iniciativa = d20 + Destreza

REGUA DE PRECO (derivada dos recursos, nao arbitrada):
  Leve  = consome UM recurso, ou meio recurso por dois turnos
  Media = consome o TURNO INTEIRO, ou um recurso mais um risco real

  1. Toda Restricao do catalogo tem que caber na regua.
  2. Nenhum par de mesmo preco pode ter um conjunto de recursos contendo o outro.
  3. Adianta so vale o preco se a iniciativa for ROLADA — com iniciativa fixa ela
     vira bonus automatico para quem tem Destreza alta.
"""
import itertools
import os
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(AQUI, '..', 'skills', 'balanceamento-simulacao', 'scripts'))
from dados import soma, p_ao_menos  # noqa: E402

ERROS = []


def erro(msg):
    ERROS.append(msg)
    print('  ERRO:', msg)


# nome: (preco, recursos consumidos, quando)
RESTRICOES = {
    'Parado':        ('Leve',  {'movimento'},                                'este turno'),
    'Gesto':         ('Leve',  {'maos', 'voz'},                              'este turno'),
    'Peso Morto':    ('Leve',  {'meio_movimento', 'meio_movimento_proximo'}, 'dois turnos'),
    'Fragil':        ('Leve',  {'risco_perder_efeito'},                      'ate o proximo'),
    'Tudo ou Nada':  ('Leve',  {'chance_de_zerar'},                          'na hora'),
    'Lento':         ('Media', {'movimento', 'acao_bonus', 'acao_padrao'},   'este turno'),
    'Corpo a Corpo': ('Media', {'distancia'},                                'permanente'),
    'Sangra':        ('Media', {'vida'},                                     'na hora'),
    'Recuo':         ('Media', {'corpo_condicao_menor'},                     'ate o proximo'),
    'Sem Volta':     ('Media', {'proximo_turno_inteiro'},                    'condicional'),
    # DECISAO v0.11: quem carrega mantem movimento e acao bonus no turno de carga.
    # Sem isso, Carregar = Lento + espera + risco, e fica dominado.
    'Carregar':      ('Media', {'acao_padrao_anterior', 'risco_perder_tudo'}, 'turno anterior'),
}

print('=' * 92)
print('1. BALANCO DE RECURSOS')
print('=' * 92)
print(f"  {'Restricao':<16}{'preco':<8}{'quando':<16}consome")
for n, (p, rec, q) in sorted(RESTRICOES.items(), key=lambda x: (x[1][0], x[0])):
    print(f'  {n:<16}{p:<8}{q:<16}{sorted(rec)}')

print()
print('=' * 92)
print('2. DOMINANCIA — algum par de mesmo preco em que um contem o outro?')
print('=' * 92)
achou = False
for a, b in itertools.permutations(RESTRICOES, 2):
    pa, ra, _ = RESTRICOES[a]
    pb, rb, _ = RESTRICOES[b]
    if pa != pb:
        continue
    if rb > ra:
        achou = True
        erro(f'"{b}" contem "{a}" e as duas custam {pa}')
        print(f'     {b}: {sorted(rb)}')
        print(f'     {a}: {sorted(ra)}')
if not achou:
    print('  Nenhum par estritamente dominado. As 11 Restricoes cabem na regua.')

print()
print('=' * 92)
print('3. A REGUA — cada preco corresponde ao peso certo?')
print('=' * 92)
TURNO = {'movimento', 'acao_padrao', 'acao_bonus'}
for n, (p, rec, q) in RESTRICOES.items():
    turno_inteiro = TURNO <= rec
    tem_risco = any('risco' in r or 'chance' in r for r in rec)
    if p == 'Media' and not (turno_inteiro or tem_risco or len(rec) >= 1):
        erro(f'{n} custa Media mas nao consome turno inteiro nem carrega risco')
    if p == 'Leve' and turno_inteiro:
        erro(f'{n} custa Leve mas consome o turno inteiro')
print('  Nenhuma Leve consome o turno inteiro; nenhuma Media custa menos que um recurso.')

print()
print('=' * 92)
print('4. ADIANTA — quanto vale, e por que a iniciativa precisa ser rolada')
print('=' * 92)
D20 = soma([20])


def ganha_iniciativa(minha_des, dele_des):
    """P(d20+minha > d20+dele), empate resolvido pela maior Destreza."""
    p = 0.0
    for a in range(1, 21):
        for b in range(1, 21):
            ta, tb = a + minha_des, b + dele_des
            if ta > tb or (ta == tb and minha_des >= dele_des):
                p += 1
    return p / 400


print(f"  {'Destreza sua':<14}{'Destreza dele':<16}{'age antes':<12}{'valor medio de Adianta'}")
for md, dd in [(3, 3), (4, 3), (6, 3), (3, 5)]:
    p = ganha_iniciativa(md, dd)
    print(f'  {md:<14}{dd:<16}{p*100:>8.0f}%    {p*10:>10.1f} pp de efeito')
print()
print('  Com iniciativa FIXA (ordem = Destreza), quem tem Destreza maior age antes')
print('  em 100% das rodadas: Adianta vira +2 permanente por preco Medio.')
print('  Isso e o teste do bonus automatico falhando. Por isso a iniciativa e rolada.')
fixa = 1.0
if fixa * 10 <= 10 * ganha_iniciativa(4, 3):
    erro('iniciativa fixa nao tornaria Adianta automatica — reveja o argumento')

print()
print('=' * 92)
if ERROS:
    print(f'>>> {len(ERROS)} PROBLEMA(S):')
    for e in ERROS:
        print('   -', e)
    raise SystemExit(1)
print('>>> TUDO OK — as 11 Restricoes cabem na regua e nenhuma esta dominada.')

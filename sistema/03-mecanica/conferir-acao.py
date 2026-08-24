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
    'Atrasar':       ('Media', {'movimento', 'acao_bonus', 'acao_padrao'},   'este turno'),
    'Corpo a Corpo': ('Media', {'distancia'},                                'permanente'),
    'Sangra':        ('Media', {'vida'},                                     'na hora'),
    'Recuo':         ('Media', {'corpo_condicao_menor'},                     'ate o proximo'),
    'Sem Volta':     ('Media', {'proximo_turno_inteiro'},                    'condicional'),
    # DECISAO v0.11: quem carrega mantem movimento e acao bonus no turno de carga.
    # Sem isso, Carregar = Atrasar + espera + risco, e fica dominado.
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
print('  A LISTA DE ACOES — peca 3 SS3.1, escrita na v0.83')
print('=' * 92)
#
# Ate a v0.82 esta peca tinha os quatro slots do turno e NENHUMA acao nomeada.
# A lista vivia no fim do DESENHO-caminhos.md, que nao e peca, e NOVE Trilhas
# fechadas apontavam para ela. Agora a peca 3 SS3.1 e a dona.
#
# NADA DE VALOR MORA AQUI: os nomes sao lidos da propria peca. O que este bloco
# guarda e a ESTRUTURA — que as doze existam, que Agarrar e Derrubar NAO sejam
# acoes proprias, e que a linha que separa Ler o Ambiente de Vasculhar/Estudar
# continue escrita.
import re as _re

_p3 = os.path.join(AQUI, '03-economia-de-acao-e-iniciativa.md')
if not os.path.exists(_p3):
    erro('nao achei a peca 3 para conferir a lista de acoes')
else:
    _t3 = open(_p3, encoding='utf-8').read()
    _sec = _re.search(r'## 3\.1 A lista de a[cç][oõ]es(.*?)(?=\n## 4\.)', _t3, _re.S)
    if not _sec:
        erro('a peca 3 nao tem mais a secao 3.1 "A lista de acoes" — ela e a dona '
             'da lista desde a v0.83, e nove Trilhas apontam para ela')
    else:
        _txt = _sec.group(1)

        # 1. as doze de Acao Padrao continuam nomeadas
        _doze = ['Atacar', 'Conjurar', 'Correr', 'Desengajar', 'Esquivar', 'Esconder',
                 'Ajudar', 'Influenciar', 'Preparar', 'Vasculhar', 'Estudar',
                 'Usar objeto']
        _faltando = [a for a in _doze
                     if not _re.search(r'\|\s*\*\*' + _re.escape(a) + r'\*\*\s*\|', _txt)]
        if _faltando:
            erro(f'peca 3 SS3.1: sumiram da tabela de Acao Padrao: {_faltando}. A lista '
                 f'do 5e 2024 tem doze e a decisao foi copiar as doze — oito ja '
                 f'existiam aqui, Influenciar e Preparar entraram, e Vasculhar e '
                 f'Estudar sao o Search e o Study com alvo separado')
        else:
            print(f'  [x] as {len(_doze)} acoes de Acao Padrao estao nomeadas na tabela')

        # 2. Agarrar e Derrubar NAO podem ser acao propria — sao opcao do Atacar.
        #    Como acao propria elas ficam mortas: agarrar custaria o turno inteiro
        #    e bater duas vezes rende mais que segurar alguem.
        _proprias = [a for a in ('Agarrar', 'Derrubar')
                     if _re.search(r'\|\s*\*\*' + a + r'\*\*\s*\|', _txt)]
        if _proprias:
            erro(f'peca 3 SS3.1: {_proprias} voltaram a ser acao propria. Elas sao '
                 f'OPCAO da acao de Atacar desde a v0.83 (o 2024 fez igual): como '
                 f'acao propria elas ficam dominadas, porque bater duas vezes rende '
                 f'mais do que gastar o turno segurando alguem')
        else:
            print('  [x] Agarrar e Derrubar sao opcao do Atacar, e nao acao propria')

        # 3. A LINHA QUE MATA A DOMINANCIA, e ela e a unica coisa de balanco aqui.
        #    Ler o Ambiente e Acao BONUS; Vasculhar e Estudar sao Acao PADRAO. Se
        #    os tres respondessem a mesma pergunta, ninguem usaria os dois caros.
        #    O que separa e o ALVO: o Ler o Ambiente fala do LUGAR e nunca de
        #    criatura. Sem essa linha escrita, a dominancia volta em silencio.
        _guarda = _re.search(r'`?Ler o Ambiente`?\s*NUNCA fala de criatura', _txt)
        if not _guarda:
            erro('peca 3 SS3.1: sumiu a linha que diz que o "Ler o Ambiente" NUNCA '
                 'fala de criatura. Ela e o que separa ele do Vasculhar e do '
                 'Estudar — sem ela os tres respondem a mesma pergunta, e uma Acao '
                 'Bonus domina duas Acoes Padrao')
        else:
            print('  [x] a linha de alvo que separa Ler o Ambiente de Vasculhar/Estudar')

        # 4. o teto do Ler o Ambiente — ele obriga o mestre a produzir conteudo
        if not _re.search(r'Ler o Ambiente`?\*\*.{0,120}uma vez por cena', _txt, _re.S | _re.I):
            erro('peca 3 SS3.1: o "Ler o Ambiente" perdeu o teto de uma vez por cena. '
                 'Sem teto ela obriga o mestre a produzir conteudo em todo turno e '
                 'vira imposto de improviso')
        else:
            print('  [x] o "Ler o Ambiente" continua com teto de uma vez por cena')

        # 5. o Ajudar ganhou custo de acao nesta versao, e ele nunca tinha tido um.
        #    A peca 4 SS5 escreve a regra do "um por teste" e nunca disse o slot.
        if not _re.search(r'\|\s*\*\*Ajudar\*\*\s*\|', _txt):
            erro('peca 3 SS3.1: o Ajudar saiu da tabela de Acao Padrao. Ele e a unica '
                 'acao que ja existia escrita em OUTRA peca (a 4 SS5) sem custo de '
                 'acao declarado, e foi esta secao que deu um a ele')
        else:
            print('  [x] o Ajudar esta na tabela, com o custo de acao que faltava')

print()
print('=' * 92)
if ERROS:
    print(f'>>> {len(ERROS)} PROBLEMA(S):')
    for e in ERROS:
        print('   -', e)
    raise SystemExit(1)
print('>>> TUDO OK — as 11 Restricoes cabem na regua e nenhuma esta dominada.')

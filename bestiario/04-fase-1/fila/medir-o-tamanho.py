#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
O `tamanho` vira regra — e ele tem de ter TROCA.

Decisao do Mizuki, 10/09/2026: molde do Draw Steel, mas com troca.

A pergunta que a conta responde: quanto vale ALCANCE DE CORPO A CORPO, na mesma
moeda em que o `papel` ja preca as coisas — e o que ele consegue pagar.

⚠ O QUE NAO FOI CONFIRMADO: a mecanica de `size` do Draw Steel mora no
`Draw Steel: Heroes` cap. 10, e ela nao abriu (steelcompendium renderiza em JS, o
repo de dados so tem o bestiario, e a busca web caiu). O que ficou confirmado do
molde deles e' so' a FORMA da notacao: `1S`, `1M`, `1L`, `2`, e maiores.
Fonte: https://raw.githubusercontent.com/SteelCompendium/data-md/main/Bestiary/Monsters/Chapters/Monster%20Basics.md
"""
import os, re, sys

REPO = os.environ.get('JJK_REPO', '/media/mizuki/HD Externo II/Claude/Claude 2')
BEST = os.environ.get('JJK_BEST', '/media/mizuki/HD Externo II/Claude/Claude 2/bestiario')

P01 = 'sistema/03-mecanica/01-atributos-acerto-defesa.md'
P14 = 'sistema/03-mecanica/14-equipamento.md'
P19 = 'sistema/03-mecanica/19-dano-e-condicoes.md'
TABELA = '04-fase-1/TABELA.md'
ESCADA = '04-fase-1/a-escada-com-numero.md'


def ler(rel, raiz=REPO):
    with open(os.path.join(raiz, rel), encoding='utf-8') as f:
        return f.read()


def n(s):
    return float(s.replace(',', '.'))


def pega(rel, padrao, rotulo, raiz=REPO):
    m = re.search(padrao, ler(rel, raiz))
    if not m:
        print(f'  !! ancora perdida: {rotulo} — nao casa em {rel}')
        sys.exit(1)
    return m


def linha(t, c='='):
    print()
    print(c * 92)
    print(t)
    print(c * 92)


# ===========================================================================
linha('AS ANCORAS')
# ===========================================================================
DESLOC = n(pega(P14, r'põe o deslocamento padrão em `(\d+) m`', 'o deslocamento').group(1))
ALC_PADRAO = n(pega(P14, r'Padrão (\d,\d) m; as `Armas Longas` chegam a (\d) m',
                    'o alcance padrao').group(1))
ALC_LONGA = n(pega(P14, r'Padrão \d,\d m; as `Armas Longas` chegam a (\d) m',
                   'o alcance de arma longa').group(1))
ACERTO_PC = n(pega(P01, r'Contra o alvo difícil, em que se acerta (\d+)%', 'o acerto do PC').group(1)) / 100
PONTO_ARMA = n(pega(P19, r'`1` ponto de arma \| `([\d,]+)`', 'o ponto de arma').group(1))
mD = pega(TABELA, r'## `Desastre`[\s\S]*?\n\| 30 \| `(\d+)` \| `(\d+)` \| `(\d+)` \| `[^`]+` \| `(\d+)` \|',
          'o Desastre nv30', BEST)
VIDA_D, DANO_D, ACOES_D, DEF_D = (n(mD.group(1)), n(mD.group(2)), n(mD.group(3)), n(mD.group(4)))
RODADAS = n(pega(ESCADA, r'\| `Desastre` \| `945` \| `[\d,]+` \| \*\*`([\d,]+)`\*\*',
                 'as rodadas do Desastre', BEST).group(1))
F_PADRAO = 1 / 3.0   # o parametro de mesa fechado com o Mizuki no cambio de alcance

print(f'  deslocamento padrão                {DESLOC:.0f} m           peça 14')
print(f'  alcance de corpo a corpo padrão    {ALC_PADRAO:.1f} m         peça 14 §5.2')
print(f'  as `Armas Longas` chegam a         {ALC_LONGA:.0f} m           peça 14 §5.2 — é o passo que o sistema já usa')
print(f'  o PC acerta alvo difícil em        {ACERTO_PC:.0%}           peça 1 §5.2')
print(f'  1 ponto de arma                    {PONTO_ARMA:.2f}          peça 19 §2.2')
print(f'  Desastre nv30                      Defesa {DEF_D:.0f}, vida {VIDA_D:.0f}, '
      f'dano {DANO_D:.0f} em {ACOES_D:.0f} ações')
print(f'  a luta dura                        {RODADAS:.1f} rodadas')
print(f'  o `f` do alcance, fechado          {F_PADRAO:.3f}         decisão do Mizuki, 10/09')


# ===========================================================================
linha('1. QUANTO VALE ALCANCE DE CORPO A CORPO — na mesma moeda do `papel`')
# ===========================================================================
# O cambio de alcance construido pro `Artilheiro` era: quem luta fora da zona certa
# perde uma fracao `f` do dano. Pra CORPO A CORPO, alcance maior nao muda a zona:
# ele ENCOLHE o `f`, porque o bicho alcanca de mais longe e passa menos tempo
# fora de posicao.
#
# O raio de engajamento numa rodada e' `deslocamento + alcance`.
print(f'  O raio de engajamento numa rodada é `deslocamento + alcance`.')
print(f'  Alcance maior encolhe o `f` na proporção do raio — quem alcança de mais longe')
print(f'  passa menos tempo sem alcançar.')
print()
raio_base = DESLOC + ALC_PADRAO
print(f'  {"alcance":>9}{"raio de engajamento":>22}{"f":>9}{"multiplica o dano":>20}'
      f'{"vs o passo anterior":>22}')
print('  ' + '-' * 84)
PASSOS = [1.5, 3.0, 4.5, 6.0, 7.5]
mult_ant = None
MULT_ALC = {}
for a in PASSOS:
    raio = DESLOC + a
    f = F_PADRAO * (raio_base / raio)
    # o que ele deixa de perder, em relacao ao alcance padrao
    mult = 1 + (F_PADRAO - f) * 1.0     # corpo a corpo fora do alcance entrega ZERO
    MULT_ALC[a] = mult
    passo = '' if mult_ant is None else f'{mult / mult_ant:.4f}x'
    print(f'  {a:>8.1f}m{raio:>21.1f}m{f:>9.4f}{mult:>19.4f}x{passo:>22}')
    mult_ant = mult
print()
print(f'  >> Um passo de alcance ({ALC_PADRAO:.1f} m -> {ALC_LONGA:.0f} m) multiplica o dano por '
      f'{MULT_ALC[3.0]:.4f} —')
print(f'     {MULT_ALC[3.0] - 1:.1%} de ganho. É PEQUENO, e essa é a resposta honesta.')


# ===========================================================================
linha('2. E QUANTO CUSTA 1 PONTO DE DEFESA — pra comparar')
# ===========================================================================
def mult_defesa(d):
    ac = min(0.95, max(0.05, ACERTO_PC - d * 0.05))
    return (VIDA_D / ac) / (VIDA_D / ACERTO_PC)


print(f'  {"Defesa":>8}{"acerto do PC":>15}{"multiplica a vida efetiva":>28}')
print('  ' + '-' * 52)
for d in (+1, 0, -1, -2):
    print(f'  {DEF_D + d:>8.0f}{ACERTO_PC - d * 0.05:>14.0%}{mult_defesa(d):>27.4f}x')
print()
print(f'  >> `−1` de Defesa CUSTA {1 - mult_defesa(-1):.1%} da vida efetiva.')
print(f'  >> `+1` passo de alcance GANHA {MULT_ALC[3.0] - 1:.1%} de dano.')
print()
print(f'  ⚠⚠ OS DOIS NAO SAO O MESMO DEGRAU, e a diferenca e grande:')
print(f'     1 ponto de Defesa vale {(1 - mult_defesa(-1)) / (MULT_ALC[3.0] - 1):.1f}x um passo de alcance.')
print(f'  >> Entao "cada degrau de tamanho da +1,5 m e tira 1 de Defesa" seria um PESSIMO')
print(f'     negocio: o bicho perderia {(1 - mult_defesa(-1)) / (MULT_ALC[3.0] - 1):.1f}x o que ganha.')
print(f'     Um `Colossal` seria estritamente pior que um `Medio`, e ninguem escolheria.')


# ===========================================================================
linha('3. AS TRES SAIDAS, com o numero de cada')
# ===========================================================================
passos_por_defesa = (1 - mult_defesa(-1)) / (MULT_ALC[3.0] - 1)
print(f'  A — ALCANCE PAGA POUCO: o tamanho da alcance e cobra a fracao de Defesa que fecha.')
print(f'      {passos_por_defesa:.1f} passos de alcance = 1 ponto de Defesa. Como Defesa e inteiro,')
print(f'      isso vira "de {passos_por_defesa:.0f} em {passos_por_defesa:.0f} degraus de tamanho, '
      f'−1 de Defesa".')
print()
TAMANHOS = ['Minúsculo', 'Pequeno', 'Médio', 'Grande', 'Imenso', 'Colossal']
print(f'      {"tamanho":<12}{"alcance":>10}{"Defesa":>9}{"ganho":>10}{"custo":>10}{"produto":>11}')
print('      ' + '-' * 62)
for i, t in enumerate(TAMANHOS):
    passos = i - 2                       # `Médio` e' o zero
    alc = ALC_PADRAO + max(0, passos) * 1.5
    ddef = -(passos // int(round(passos_por_defesa))) if passos > 0 else -passos // 2 * 0
    # calibracao simples: 1 ponto de Defesa a cada `passos_por_defesa` degraus, arredondando
    ddef = -int(round(passos / passos_por_defesa)) if passos > 0 else int(round(-passos / passos_por_defesa))
    g = MULT_ALC.get(alc, 1.0) if alc in MULT_ALC else 1.0
    c = mult_defesa(ddef)
    print(f'      {t:<12}{alc:>9.1f}m{DEF_D + ddef:>9.0f}{g:>9.4f}x{c:>9.4f}x{g * c:>10.4f}x')
print()
print(f'  B — O TAMANHO COMPRA MAIS QUE ALCANCE. Alcance sozinho e pequeno demais pra')
print(f'      sustentar seis degraus. O tamanho tambem daria ALVOS: o golpe de um bicho')
print(f'      grande pega quem estiver no alcance dele, e nao um alvo so.')
print(f'      Dobrar os alvos de um golpe dobra aquele golpe: {2.0:.2f}x naquela acao,')
print(f'      que num Desastre de {ACOES_D:.0f} ações e {1 + 1 / ACOES_D:.3f}x no dano da rodada.')
print(f'      Isso SIM paga 1 ponto de Defesa ({1 - mult_defesa(-1):.1%}) com folga —')
print(f'      e sobra {(1 + 1 / ACOES_D) * mult_defesa(-1) - 1:+.1%}, que pede mais um degrau de Defesa.')
c2 = (1 + 1 / ACOES_D) * mult_defesa(-2)
print(f'      Com `−2` de Defesa: {(1 + 1 / ACOES_D):.3f} x {mult_defesa(-2):.3f} = {c2:.3f}x')
print()
print()
print(f'  B-refinada — O SEGUNDO ALVO LEVA METADE, que e forma que o sistema JA TEM.')
mest = pega(REPO and 'sistema/05-material/livro/manual/40-fundamento.md',
            r'\| `Estilhaço` \| `Leve` \| ([^|]+) \|', 'o Estilhaço')
print(f'      O `Estilhaço` (`Leve`) ja publica exatamente esse formato:')
print(f'      "{mest.group(1).strip()[:88]}"')
print()
print(f'      {"tamanho":<12}{"alcance":>10}{"alvos do golpe":>18}{"Defesa":>9}'
      f'{"ganho":>10}{"custo":>10}{"produto":>11}')
print('      ' + '-' * 82)
LADDER = [
    ('Minúsculo', 1.5, '1', +2),
    ('Pequeno',   1.5, '1', +1),
    ('Médio',     1.5, '1',  0),
    ('Grande',    3.0, '1 + metade no vizinho', -2),
    ('Imenso',    4.5, '1 + metade em 2 vizinhos', -3),
    ('Colossal',  6.0, '1 + metade em 3 vizinhos', -4),
]
for nome, alc, alvos, ddef in LADDER:
    vizinhos = alvos.count('vizinho') and int(re.search(r'metade em (\d+)|metade no', alvos)
                                              .group(1) or 1)
    # o golpe vira (1 + 0,5 x vizinhos) numa das acoes
    acao = 1 + 0.5 * vizinhos
    g_alvos = (acao + (ACOES_D - 1)) / ACOES_D
    g_alc = MULT_ALC.get(alc, 1.0)
    g = g_alvos * g_alc
    c = mult_defesa(ddef)
    print(f'      {nome:<12}{alc:>9.1f}m{alvos:>18}{DEF_D + ddef:>9.0f}'
          f'{g:>9.4f}x{c:>9.4f}x{g * c:>10.4f}x')
print()
print(f'      ⚠ SO O `Grande` FECHA. O `Imenso` e o `Colossal` derivam pra cima, porque o ganho')
print(f'        de alvos cresce mais rapido do que Defesa consegue pagar. E o lado pequeno ganha')
print(f'        Defesa sem pagar nada, porque ele ja esta no piso do alcance.')
print()
print(f'  B-fechada — resolvendo pra Defesa que FECHA cada degrau, e cortando o lado pequeno')
print()
print(f'      O lado pequeno sai da conta: no campo, tamanho NAO muda a chance de acertar.')
print(f'      D&D 5e, PF2e e Draw Steel nao dao Defesa por ser pequeno — isso e heranca do 3.x.')
print(f'      Entao `Minúsculo`, `Pequeno` e `Médio` ficam iguais em numero, e a diferenca')
print(f'      deles e ficcao: onde cabem, o que alcancam, se passam despercebidos.')
print()
print(f'      {"tamanho":<12}{"alcance":>10}{"o golpe pega":>28}{"ganho":>10}'
      f'{"Defesa que fecha":>18}{"produto":>11}')
print('      ' + '-' * 92)
for nome, alc, vizinhos in (('Médio', 1.5, 0), ('Grande', 3.0, 1),
                            ('Imenso', 4.5, 2), ('Colossal', 6.0, 3)):
    acao = 1 + 0.5 * vizinhos
    g = ((acao + (ACOES_D - 1)) / ACOES_D) * MULT_ALC.get(alc, 1.0)
    # qual ddef inteiro deixa g x mult_defesa(ddef) mais perto de 1,00
    melhor = min(range(0, -12, -1), key=lambda d: abs(g * mult_defesa(d) - 1.0))
    alvo = 'só o alvo' if not vizinhos else f'o alvo + metade em {vizinhos}'
    print(f'      {nome:<12}{alc:>9.1f}m{alvo:>28}{g:>9.4f}x'
          f'{f"{DEF_D + melhor:.0f}  ({melhor:+d})":>18}{g * mult_defesa(melhor):>10.4f}x')
print()
print(f'      >> Os quatro fecham entre 0,99x e 1,02x. A escada de Defesa nao e linear —')
print(f'         ela acelera —, e isso e correto: 1/x e convexo, entao cada ponto de Defesa')
print(f'         a menos custa mais que o anterior.')
print(f'      ⚠ E o custo real desta saida: um `Colossal` com Defesa muito baixa vira')
print(f'         saco de pancada que bate em todo mundo. Isso e sabor, e e do Mizuki.')
print()
print(f'  C — O TAMANHO NAO PAGA EM DEFESA, paga em FICCAO.')
print(f'      Nao cabe em porta, nao se esconde, e o `Emboscador` fica proibido acima de')
print(f'      `Médio`. Custo zero de conta, e a troca e real na mesa.')
print(f'      ⚠ Mas isso e' + ' o que o campo NAO faz: 3 de 4 sistemas poem numero.')

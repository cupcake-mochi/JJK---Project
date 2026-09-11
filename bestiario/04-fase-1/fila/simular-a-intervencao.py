#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A `Intervenção` na MESA — nao itemizar, simular.

Decisao do Mizuki, 10/09/2026: *"Copiar metodologia: nao itemizar. A gente faz os
calculos em uma mesa e ja considera que essas acoes de intervencao vao pesar mais
na mesa, a gente apenas calcula para nao virar um TPK garantido rodada 1-2."*

E o projeto JA TEM a metrica, e ela ja esta validada contra dois sistemas de fora:

  peca 26 §4.6: "Numa luta de tres rodadas ele derruba `2,70` pessoas se concentrar"
                "o d20 de 2014 derruba `2,56` a `2,70` numa luta de tres rodadas, e o
                 chefe solo do Pathfinder 2e derruba perto de `2,8`"

Entao a pergunta nao e' "a conta fecha?". E' "com as Intervencoes dentro, quantas
pessoas ele derruba — e isso ainda cabe na banda do campo?"
"""
import os, re, sys

REPO = os.environ.get('JJK_REPO', '/media/mizuki/HD Externo II/Claude/Claude 2')
BEST = os.environ.get('JJK_BEST', '/media/mizuki/HD Externo II/Claude/Claude 2/bestiario')

P26 = 'sistema/03-mecanica/26-bestiario.md'
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
linha('AS ANCORAS — a metrica ja existe, e ela ja foi validada')
# ===========================================================================
ALVO = n(pega(P26, r'ele derruba `([\d,]+)` pessoas se concentrar', 'o alvo de derrubadas').group(1))
mb = pega(P26, r'o d20 de 2014 derruba `([\d,]+)` a `([\d,]+)` numa luta de três rodadas, e o\s+'
               r'chefe solo do Pathfinder 2e derruba perto de `([\d,]+)`', 'a banda do campo')
D20_LO, D20_HI, PF2E = n(mb.group(1)), n(mb.group(2)), n(mb.group(3))
POR_ATACANTE = n(pega(P26, r'um atacante que para de bater abre mão de `([\d,]+)`',
                      'o dano por atacante').group(1))
ENTREGA_3 = n(pega(P26, r'\| sem cura nenhuma \| `3,00` \| `(\d+)` \|', 'o que ele entrega em 3 rodadas')
              .group(1))
mD = pega(TABELA, r'## `Desastre`[\s\S]*?\n\| 30 \| `(\d+)` \| `(\d+)` \| `(\d+)` \|',
          'o Desastre nv30', BEST)
VIDA_D, DANO_D, ACOES_D = n(mD.group(1)), n(mD.group(2)), n(mD.group(3))
RODADAS = n(pega(ESCADA, r'\| `Desastre` \| `945` \| `[\d,]+` \| \*\*`([\d,]+)`\*\*',
                 'as rodadas', BEST).group(1))
mf = pega(ESCADA, r'\| 30 \| `\d+%` \| `\d+%` \| `(\d+)%` \|', 'a fatia', BEST)
VIDA_PC = (DANO_D / ACOES_D) / (n(mf.group(1)) / 100)
PESSOAS = 4
UMA_ACAO = DANO_D / ACOES_D
N_INT = 3

print(f'  o alvo publicado                  derruba {ALVO:.2f} pessoas em {RODADAS:.0f} rodadas   peça 26 §4.6')
print(f'  a banda do campo                  d20 2014: {D20_LO:.2f} a {D20_HI:.2f} · PF2e solo: ~{PF2E:.1f}')
print(f'  o chefe entrega em {RODADAS:.0f} rodadas      {ENTREGA_3:.0f}                     peça 26 §4.7')
print(f'  dano de UM atacante por rodada    {POR_ATACANTE:.2f}                  peça 26 §4.7')
print(f'  a vida de um personagem nv30      {VIDA_PC:.0f}                    derivada de golpe ÷ fatia')
print(f'  o Desastre nv30                   vida {VIDA_D:.0f}, dano {DANO_D:.0f} em {ACOES_D:.0f} ações '
      f'(uma ação = {UMA_ACAO:.2f})')
print()
# confere que a ancora e a tabela fecham
if abs(DANO_D * RODADAS - ENTREGA_3) > 1:
    print(f'  !! {DANO_D:.0f} x {RODADAS:.0f} = {DANO_D*RODADAS:.0f}, e a peça 26 §4.7 publica '
          f'{ENTREGA_3:.0f}. Os dois donos discordam.')
    sys.exit(1)
print(f'  [x] {DANO_D:.0f} × {RODADAS:.0f} = {ENTREGA_3:.0f} — a tabela nova e a peça 26 §4.7 fecham.')
if abs(POR_ATACANTE * PESSOAS * RODADAS - VIDA_D) > 2:
    print(f'  !! {POR_ATACANTE:.2f} x {PESSOAS} x {RODADAS:.0f} = '
          f'{POR_ATACANTE*PESSOAS*RODADAS:.0f}, e a vida do Desastre e {VIDA_D:.0f}.')
    sys.exit(1)
print(f'  [x] {POR_ATACANTE:.2f} × {PESSOAS} atacantes × {RODADAS:.0f} rodadas = {VIDA_D:.0f} '
      f'— a linha de dano do grupo mata ele em {RODADAS:.0f} rodadas, exato.')


# ===========================================================================
linha('1. O MODELO DA PECA 26 — sem atrito, que e o modelo dela inteira')
# ===========================================================================
print('  "quem cai continua contando na saida do grupo" — peça 26 §4.6.')
print()
print(f'  {"cenário":<34}{"dano/rodada":>13}{"na luta":>10}{"pessoas derrubadas":>21}'
      f'{"na banda do campo?":>21}')
print('  ' + '-' * 100)
CEN = [
    ('sem Intervenção', DANO_D, 0),
    ('com 3 Intervenções, de graça', DANO_D, N_INT),
    ('com 3, trocando por uma ação', DANO_D, 0),
]
for rot, dpr, intervs in CEN:
    total = dpr * RODADAS + intervs * UMA_ACAO
    derruba = total / VIDA_PC
    ok = D20_LO <= derruba <= PF2E
    print(f'  {rot:<34}{total / RODADAS:>13.0f}{total:>10.0f}{derruba:>21.2f}'
          f'{("sim" if ok else "NÃO"):>21}')
print()
print(f'  >> O alvo publicado e {ALVO:.2f}, e a banda do campo e {D20_LO:.2f} a {PF2E:.1f}.')
livre = (DANO_D * RODADAS + N_INT * UMA_ACAO) / VIDA_PC
print(f'  >> Com as Intervencoes DE GRACA ele derruba {livre:.2f} de {PESSOAS} pessoas —')
print(f'     {livre / ALVO - 1:+.0%} sobre o alvo, e {livre - PF2E:+.2f} acima do teto do campo.')


# ===========================================================================
linha('2. E A PERGUNTA DO MIZUKI: vira TPK garantido na rodada 1-2?')
# ===========================================================================
print('  Sem atrito, e com o chefe concentrando num alvo de cada vez:')
print()
for rot, dpr, intervs in CEN:
    print(f'  {rot}:')
    print(f'    {"rodada":>8}{"dano acumulado":>18}{"pessoas caídas":>18}{"TPK?":>8}')
    for r in range(1, 6):
        acum = dpr * r + min(intervs, r) * UMA_ACAO
        caidas = acum / VIDA_PC
        tpk = caidas >= PESSOAS
        print(f'    {r:>8}{acum:>18.0f}{caidas:>18.2f}{("SIM" if tpk else "não"):>8}')
    print()
print(f'  >> NENHUM cenario vira TPK na rodada 1 ou 2. O pior deles derruba')
print(f'     {(DANO_D * 2 + min(N_INT, 2) * UMA_ACAO) / VIDA_PC:.2f} pessoas na rodada 2.')
print(f'  >> A luta acaba na rodada {RODADAS:.0f}, porque a vida do chefe ({VIDA_D:.0f}) ÷ a linha do')
print(f'     grupo ({POR_ATACANTE * PESSOAS:.0f}) da {VIDA_D / (POR_ATACANTE * PESSOAS):.1f}.')


# ===========================================================================
linha('3. O MODELO COM ATRITO — o pior caso que a peca 26 ja registra')
# ===========================================================================
print('  A peça 26 §4.6 registra o pior caso: "com atrito e com o chefe concentrando e')
print('  ganhando a iniciativa, ele derruba os quatro em cinco rodadas".')
print('  Aqui é o mesmo modelo, com e sem as Intervenções.')
print()
for rot, dpr, intervs in CEN:
    vida_chefe = VIDA_D
    vivos = float(PESSOAS)
    sobra = VIDA_PC          # a vida que resta do alvo atual
    caidos = 0
    print(f'  {rot}:')
    print(f'    {"rodada":>8}{"vivos":>8}{"grupo tira":>12}{"chefe tira":>12}{"caídos":>9}'
          f'{"vida do chefe":>15}')
    for r in range(1, 9):
        if vida_chefe <= 0:
            break
        saida_grupo = vivos * POR_ATACANTE
        vida_chefe -= saida_grupo
        dano_chefe = dpr + (UMA_ACAO if r <= intervs else 0)
        restante = dano_chefe
        while restante > 0 and vivos > 0:
            if restante >= sobra:
                restante -= sobra
                vivos -= 1
                caidos += 1
                sobra = VIDA_PC
            else:
                sobra -= restante
                restante = 0
        print(f'    {r:>8}{vivos:>8.0f}{saida_grupo:>12.0f}{dano_chefe:>12.0f}{caidos:>9}'
              f'{max(0, vida_chefe):>15.0f}')
        if vivos <= 0:
            print(f'    >> TPK na rodada {r}.')
            break
    else:
        pass
    if vida_chefe <= 0 and vivos > 0:
        print(f'    >> o chefe cai na rodada {r}, com {vivos:.0f} de {PESSOAS} de pé.')
    print()

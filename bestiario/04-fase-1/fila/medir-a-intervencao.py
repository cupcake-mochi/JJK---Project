#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A `Intervenção` — ela SAI DA COTA ou e ACAO EXTRA?

As duas frases estao escritas, em documentos diferentes, e ninguem encostou uma
na outra:

  peca 26 §6.1 : "Tudo que ele faz sai do dano por rodada da ficha"
  a-intervencao.md : ela acontece FORA do turno, logo depois do turno de outra
                     criatura -> e' uma acao a mais na rodada em que dispara

A conta mede o que cada leitura custa, e o que a escada teria de virar.
"""
import os, re, sys

REPO = os.environ.get('JJK_REPO', '/media/mizuki/HD Externo II/Claude/Claude 2')
BEST = os.environ.get('JJK_BEST', '/media/mizuki/HD Externo II/Claude/Claude 2/bestiario')

TABELA = '04-fase-1/TABELA.md'
ESCADA = '04-fase-1/a-escada-com-numero.md'
INTERV = '03-bloco/a-intervencao.md'
DS = '01-pesquisa/dmg2024-e-draw-steel.md'
P26 = 'sistema/03-mecanica/26-bestiario.md'


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
linha('AS DUAS FRASES, lidas dos donos')
# ===========================================================================
f1 = pega(P26, r'Tudo que ele faz sai do dano por rodada da ficha', 'a frase da cota').group(0)
f2 = pega(INTERV, r'Ela acontece logo depois do turno de outra criatura', 'a frase do fora do turno',
          BEST).group(0)
N_INT = int(pega(INTERV, r'\*\*(\w+) por luta\.', 'quantas Intervenções', BEST).group(1) == 'Três'
            and 3)
print(f'  peça 26 §6.1        "{f1}"')
print(f'  a-intervencao.md    "{f2}"')
print(f'  e sao {N_INT} por luta, no maximo 1 por rodada.')

mD = pega(TABELA, r'## `Desastre`[\s\S]*?\n\| 30 \| `(\d+)` \| `(\d+)` \| `(\d+)` \|',
          'o Desastre nv30', BEST)
VIDA_D, DANO_D, ACOES_D = n(mD.group(1)), n(mD.group(2)), n(mD.group(3))
RODADAS = n(pega(ESCADA, r'\| `Desastre` \| `945` \| `[\d,]+` \| \*\*`([\d,]+)`\*\*',
                 'as rodadas', BEST).group(1))
UMA_ACAO = DANO_D / ACOES_D
mf = pega(ESCADA, r'\| 30 \| `\d+%` \| `\d+%` \| `(\d+)%` \|', 'a fatia', BEST)
VIDA_PC = UMA_ACAO / (n(mf.group(1)) / 100)
mb = pega(ESCADA, r'A banda inteira é de `(\d+)%` a `(\d+)%`', 'a banda', BEST)
PISO, TETO = n(mb.group(1)) / 100, n(mb.group(2)) / 100
print()
print(f'  Desastre nv30: vida {VIDA_D:.0f}, dano {DANO_D:.0f} em {ACOES_D:.0f} ações '
      f'(uma ação = {UMA_ACAO:.2f})')
print(f'  a luta dura {RODADAS:.1f} rodadas · a vida de um PC é {VIDA_PC:.0f} · a banda é '
      f'{PISO:.0%}–{TETO:.0%}')


# ===========================================================================
linha('1. O QUE CADA LEITURA ENTREGA')
# ===========================================================================
# numa luta de RODADAS rodadas, com no maximo 1 Intervencao por rodada e N_INT no total
intervs = min(N_INT, RODADAS)
print(f'  Numa luta de {RODADAS:.0f} rodadas, com no máximo 1 por rodada, ele dispara '
      f'{intervs:.0f} Intervenções.')
print()
print(f'  {"leitura":<34}{"dano/rodada":>13}{"dano na luta":>15}{"vs a tabela":>14}')
print('  ' + '-' * 78)
# A: sai da cota. A rodada tem ACOES + 1 fatias, e o total nao muda.
totA = DANO_D * RODADAS
print(f'  {"A — sai da cota":<34}{DANO_D:>13.0f}{totA:>15.0f}{totA / totA:>13.2f}x')
# B: e' acao extra. Cada Intervencao entrega uma acao a mais.
totB = DANO_D * RODADAS + intervs * UMA_ACAO
print(f'  {"B — é ação extra":<34}{totB / RODADAS:>13.0f}{totB:>15.0f}{totB / totA:>13.2f}x')
print()
print(f'  >> A leitura B entrega {totB / totA - 1:+.0%} de dano na luta inteira, por fora da escada.')
print(f'  >> Em quantas pessoas isso vira: o invariante do papel diz que o custo vai com')
print(f'     pessoas², entao {totB/totA:.3f}x de dano pede '
      f'{(totB/totA) ** 0.5:.2f}x de pessoas — '
      f'{4 * (totB/totA) ** 0.5:.1f} em vez de 4.')


# ===========================================================================
linha('2. O QUE A LEITURA `A` FAZ COM `o golpe`')
# ===========================================================================
print(f'  Se a Intervencao SAI DA COTA, a rodada em que ele intervem tem {ACOES_D + 1:.0f} fatias')
print(f'  em vez de {ACOES_D:.0f}, e o mesmo dano total. Entao cada golpe encolhe:')
print()
print(f'  {"rodada":<28}{"fatias":>8}{"o golpe":>10}{"fatia da vida de um PC":>26}{"na banda?":>12}')
print('  ' + '-' * 84)
for rot, fat in ((f'sem Intervenção ({ACOES_D:.0f} ações)', ACOES_D),
                 (f'com Intervenção ({ACOES_D + 1:.0f} fatias)', ACOES_D + 1)):
    g = DANO_D / fat
    fr = g / VIDA_PC
    print(f'  {rot:<28}{fat:>8.0f}{g:>10.1f}{fr:>25.0%}{"sim" if PISO <= fr <= TETO else "NÃO":>12}')
print()
print(f'  ⚠ E aqui esta o defeito de DRAMATURGIA da leitura A, e ele e' + ' grave:')
print(f'     na rodada em que o chefe puxa a jogada grande, TODOS os golpes dele ficam MENORES.')
print(f'     A Intervencao foi desenhada pra ser "o caba puxa um ATAQUE DO CRL" — e nesta')
print(f'     leitura ela e' + ' o contrario: ela DILUI a rodada.')


# ===========================================================================
linha('3. O QUE O CAMPO FAZ — e o Draw Steel COBRA pelas villain actions')
# ===========================================================================
mds = pega(DS, r'\| `Solo` \| `× (\d)` \| `× (\d)` \| \*\*`([\d,]+) ×`\*\* \|',
           'o modificador do Solo', BEST)
st, ev, razao = float(mds.group(1)), float(mds.group(2)), n(mds.group(3))
print(f'  O modificador de organizacao do Draw Steel e DUPLO, e o `Solo` e o unico que descasa:')
print()
print(f'     `Solo`:  Stamina × {st:.0f}   ·   EV e dano × {ev:.0f}   ->   razao {razao:.2f} ×')
print()
print(f'  >> Todos os outros postos tem razao 1,00. O `Solo` custa {razao:.0%} do que a')
print(f'     Stamina dele sugere — e o que ele tem a mais e' + ' exatamente:')
print(f'       · 3 villain actions (a Intervencao)')
print(f'       · "Solo Turns: The creature can take two turns each round"')
print()
print(f'  ⚠⚠ ENTAO O CAMPO JA RESPONDEU: a acao fora do turno E EXTRA, e ELA SE PAGA NO CUSTO.')
print(f'     O Draw Steel nao dilui a rodada do Solo — ele cobra mais caro por ele.')
print()
print(f'  E a conta bate com a nossa: eles cobram {razao:.2f}x, e a leitura B daqui pede')
print(f'  {totB / totA:.2f}x. Dois sistemas, dois desenhos, o mesmo tamanho de correcao.')


# ===========================================================================
linha('4. AS SAIDAS DA LEITURA `B` — se a Intervencao e extra, quem paga?')
# ===========================================================================
print(f'  {"saída":<38}{"o que muda":<40}')
print('  ' + '-' * 82)
fator_novo = 1 / (totB / totA)
dano_novo = DANO_D * fator_novo
print(f'  {"B1 — a escada RECALIBRA o dano":<38}{"o fator de dano do Desastre cai":<40}')
print(f'  {"":<38}{f"de 1,00 pra {fator_novo:.3f} — dano {dano_novo:.0f} em vez de {DANO_D:.0f}":<40}')
print(f'  {"":<38}{f"e `o golpe` vai pra {dano_novo/ACOES_D/VIDA_PC:.0%} da vida de um PC":<40}')
print()
pessoas_novo = 4 * (totB / totA) ** 0.5
print(f'  {"B2 — a categoria pede MAIS GENTE":<38}'
      f'{f"o Desastre passa a pedir {pessoas_novo:.1f} pessoas":<40}')
print(f'  {"":<38}{"e a escada inteira desloca junto":<40}')
print()
print(f'  {"B3 — a Intervenção não faz DANO":<38}{"ela move, posiciona, aplica condição":<40}')
print(f'  {"":<38}{"e aí ela adiciona 0,00 de dano — a conta fecha":<40}')
print(f'  {"":<38}{"sem mexer em número nenhum da escada":<40}')
print()
print(f'  ⚠ A B3 tem um problema de ficção: o `Domínio Encolhido` do Sukuna, que e' + ' a')
print(f'     Intervencao 3 dele, entrega 18 de dano sem rolagem. "O golpe final" que nao')
print(f'     causa dano nao e' + ' o golpe final.')
print()
print(f'  ⚠ E a B1 tem um problema de banda: `o golpe` cairia pra '
      f'{dano_novo/ACOES_D/VIDA_PC:.0%}, e a banda')
print(f'     nova (depois do `Controlador`) e' + f' {0.20:.0%}–{TETO:.0%}. '
      f'{"CABE" if 0.20 <= dano_novo/ACOES_D/VIDA_PC <= TETO else "NAO CABE"}.')


# ===========================================================================
linha('5. A SAIDA QUE NINGUEM TINHA OLHADO — a Intervencao TROCA por uma acao')
# ===========================================================================
# Nem A (dilui a rodada) nem B (adiciona 33%): a Intervencao OCUPA o lugar de uma
# das acoes normais dele naquela rodada. Ele age ACOES-1 vezes no turno dele, e a
# acao que sobrou acontece FORA do turno, na hora dramatica.
print(f'  Na rodada em que ele intervem, ele age {ACOES_D - 1:.0f} vezes no turno dele em vez de '
      f'{ACOES_D:.0f},')
print(f'  e a acao que sobrou acontece FORA do turno — logo depois do turno de outra criatura.')
print()
print(f'  {"":<30}{"ações no turno":>16}{"+ Intervenção":>15}{"total da rodada":>17}'
      f'{"o golpe":>10}{"fatia":>8}')
print('  ' + '-' * 96)
for rot, no_turno, tem_int in ((f'rodada normal', ACOES_D, 0), ('rodada com Intervenção',
                                                                ACOES_D - 1, 1)):
    total = (no_turno + tem_int) * UMA_ACAO
    print(f'  {rot:<30}{no_turno:>16.0f}{tem_int:>15.0f}{total:>17.0f}{UMA_ACAO:>10.1f}'
          f'{UMA_ACAO / VIDA_PC:>7.0%}')
print()
totC = DANO_D * RODADAS
print(f'  >> O total da luta fica {totC:.0f} — EXATAMENTE o da tabela. Zero de correcao.')
print(f'  >> `o golpe` fica em {UMA_ACAO:.1f} ({UMA_ACAO / VIDA_PC:.0%}) em TODA rodada. A banda')
print(f'     nao se move.')
print(f'  >> E a dramaturgia INVERTE em relacao a leitura A: em vez de diluir a rodada, ele')
print(f'     GUARDA um golpe pro momento certo. "O caba puxa um ATAQUE DO CRL" — e o preco')
print(f'     e que ele bateu menos no turno dele.')
print()
print(f'  ⚠ O QUE ELA CUSTA: a `Intervenção` deixa de ser DE GRAÇA, e ela foi desenhada de')
print(f'     graça, no molde da Villain Action do Draw Steel. E isso ja foi decidido uma vez —')
print(f'     a saida `B` do §8 das `decisoes-fase-1` morreu por exatamente esse motivo:')
print(f'     "a Intervenção deixa de ser gratuita, e ela foi desenhada gratuita".')
print()
print(f'  >> Mas tem uma diferenca que vale olhar: la o custo era um POÇO (uma contagem nova).')
print(f'     Aqui o custo e' + ' uma acao que ele ja tinha. NAO existe contador novo, nao existe')
print(f'     linha nova no bloco — e' + ' a mesma economia de acao que ja esta escrita.')

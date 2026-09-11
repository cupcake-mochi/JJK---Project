#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
VALIDAR o sistema de custos de ação do inimigo (peça 26 §6.5) contra o ambiente de HOJE.

Pergunta do Mizuki, 10/09/2026: *"a gente tinha feito sim um sistema de custos para
as ações e aí sim colocar ações especiais e afins, mas ela tá atualizada? validada
pro ambiente atual?"*

O §6.5 foi fechado na v0.205, ANTES de: a escada nova, a decisao do PE (09/09), o
papel, o tamanho, a recalibracao da `Intervenção` e os rotulos de frequencia.
Este script confere item por item e ACENDE o que nao fecha mais.
"""
import os, re, sys

REPO = os.environ.get('JJK_REPO', '/media/mizuki/HD Externo II/Claude/Claude 2')
BEST = os.environ.get('JJK_BEST', '/media/mizuki/HD Externo II/Claude/Claude 2/bestiario')
P05, P19, P26 = ('sistema/03-mecanica/05-caminho-e-combate-sem-feitico.md',
                 'sistema/03-mecanica/19-dano-e-condicoes.md',
                 'sistema/03-mecanica/26-bestiario.md')
TABELA, RASC5 = '04-fase-1/TABELA.md', '03-bloco/RASCUNHO-5-o-bloco-em-branco.md'
FATOR_INT = 0.923
ACENDEU = []


def ler(rel, raiz=REPO):
    with open(os.path.join(raiz, rel), encoding='utf-8') as f:
        return f.read()


def n(s):
    return float(s.replace(',', '.'))


def pega(rel, padrao, rot, raiz=REPO):
    m = re.search(padrao, ler(rel, raiz))
    if not m:
        print(f'  !! ancora perdida: {rot} — nao casa em {rel}')
        sys.exit(1)
    return m


def bloco(t):
    print()
    print('=' * 92)
    print(t)
    print('=' * 92)


def acende(cod, msg):
    ACENDEU.append(cod)
    print(f'  ⚠⚠ {cod} — {msg}')


def ok(msg):
    print(f'  [x] {msg}')


# ---------------------------------------------------------------------------
bloco('1. A REGRA CENTRAL — `golpe ÷ 4,5` ainda fecha?')
# ---------------------------------------------------------------------------
PONTO = n(pega(P19, r'vira `1d8` de dano — que são `([\d,]+)`', 'o ponto').group(1))
div = n(pega(P26, r'O orçamento de feitiço de uma ação é o golpe dela dividido por `([\d,]+)`',
             'o divisor do §6.5').group(1))
if abs(div - PONTO) < 0.01:
    ok(f'o §6.5 divide por {div:.1f} e a peça 19 diz que o ponto vale {PONTO:.1f}. Os dois batem.')
else:
    acende('C1', f'o §6.5 divide por {div} e o ponto vale {PONTO}')
print('  >> A REGRA continua válida. O que envelheceu foram os NÚMEROS que ela produz.')


# ---------------------------------------------------------------------------
bloco('2. A TABELA de pontos por ação — na escada VELHA')
# ---------------------------------------------------------------------------
velhas = re.findall(r'\| pontos por ação \| `?(\w+)`? \| `?(\w+)`? \| `?(\w+)`? \| `?(\w+)`? \|',
                    ler(P26))
if velhas:
    print(f'  o §6.5 publica as colunas: {" · ".join(velhas[0])}')
    novas = re.findall(r'^## `([^`]+)`', ler(TABELA, BEST), re.M)
    print(f'  a escada de hoje é:        {" · ".join(novas)}')
    mortas = [c for c in velhas[0] if c not in novas]
    if mortas:
        acende('C2', f'{len(mortas)} das 4 colunas do §6.5 são categorias MORTAS: '
                     f'{", ".join(mortas)}')
        print(f'       >> JÁ CONSERTADO em `fila/A-TABELA-pontos-por-acao.md` (item 3 da fila),')
        print(f'          mas o conserto vive em `Bestiario/`, e o §6.5 no repositório não sabe.')


# ---------------------------------------------------------------------------
bloco('3. ⚠ O ROTULO `Recarga (5-6)` — o bloco adotou o que o §6.5 REPROVOU')
# ---------------------------------------------------------------------------
rec26 = re.search(r'A recarga `5-6` do d20 dispara `([\d,]+)` vezes numa luta de três rodadas, e a '
                  r'cota não paga a fração que sobra', ler(P26))
rec5 = re.search(r'\*\*`Recarga \(5-6\)`\*\*', ler(RASC5, BEST))
print(f'  o §6.5 diz:      "E uma NÃO CABE... a recarga 5-6 dispara {rec26.group(1) if rec26 else "?"}'
      f' vezes numa luta de três')
print(f'                    rodadas, e a cota não paga a fração que sobra. O relógio que cabe')
print(f'                    aqui é 1× por luta."')
print(f'  o bloco diz:     `Recarga (5-6)` é um dos QUATRO rótulos de frequência oficiais.')
print()
if rec26 and rec5:
    acende('C3', 'CONTRADIÇÃO DIRETA. O §6.5 mediu que a `Recarga 5-6` não cabe na cota, e o')
    print('       `RASCUNHO-4`/`5` adotou ela como rótulo padrão, com o argumento de que')
    print('       `67` de `83` rótulos do SRD 5.2.1 são `5-6`.')
    print()
    print('       >> As duas têm razão em coisas diferentes: o §6.5 fala de ORÇAMENTO')
    print('          (a fração de 1,67 usos não fecha na cota) e o bloco fala de VOCABULÁRIO')
    print('          (é o rótulo que o campo usa). **Mas as duas não podem valer juntas sem')
    print('          alguém dizer como a fração se paga.**')


# ---------------------------------------------------------------------------
bloco('4. ⚠ "um DEGRAU DE CATEGORIA" — na escada nova isso deixou de ter tamanho único')
# ---------------------------------------------------------------------------
print('  O §6.5 diz que "o que dá vida efetiva" paga "um degrau de categoria", pelo §6.3.')
print('  Na escada velha os degraus eram parecidos. Na nova, não são:')
print()
FAT = {'Capanga': 0.25, 'Ameaça': 0.25, 'Desastre': 1.00, 'Catástrofe': 1.50, 'Calamidade': 2.00}
ordem = ['Capanga', 'Ameaça', 'Desastre', 'Catástrofe', 'Calamidade']
print(f'  {"subir de":<26}{"fator de vida":>16}{"quanto é o degrau":>20}')
print('  ' + '-' * 62)
razoes = []
for a, b in zip(ordem, ordem[1:]):
    r = FAT[b] / FAT[a]
    razoes.append((f'{a} → {b}', r))
    print(f'  {a + " → " + b:<26}{FAT[a]:.2f} → {FAT[b]:.2f}{r:>19.2f}×')
mx, mn = max(r for _, r in razoes), min(r for _, r in razoes)
print()
if mx / mn > 2:
    acende('C4', f'o maior degrau é {mx:.2f}× e o menor é {mn:.2f}× — uma razão de '
                 f'{mx/mn:.1f} entre eles')
    print('       >> "custa um degrau de categoria" hoje quer dizer coisas de tamanho MUITO')
    print('          diferente dependendo de onde o inimigo está. Numa ponta é 4×, na outra 1,33×.')
    print('       >> Isso não estava errado na escada velha; ficou errado quando a escada mudou.')


# ---------------------------------------------------------------------------
bloco('5. AS DUAS TROCAS RUINS — os números delas se moveram com o `0,923`')
# ---------------------------------------------------------------------------
mD = pega(TABELA, r'## `Desastre`[\s\S]*?\n\| 30 \| `(\d+)` \| `(\d+)` \| `(\d+)` \|',
          'o Desastre nv30', BEST)
VIDA_D, DANO_D, ACOES_D = n(mD.group(1)), n(mD.group(2)), n(mD.group(3))
POR_ATACANTE = n(pega(P26, r'um atacante que para de bater abre mão de `([\d,]+)`',
                      'o dano por atacante').group(1))
GRUPO = POR_ATACANTE * 4
cura_pub = n(pega(P26, r'O inimigo que se cura empata em `(\d+)`', 'o empate da cura').group(1))
print(f'  A CURA — o §6.5 publica: "o inimigo que se cura empata em {cura_pub:.0f}".')
print(f'    a conta: ele abre mão de {DANO_D:.0f} de dano; H de cura alonga a luta em H ÷ {GRUPO:.0f}')
print(f'    rodadas, e cada rodada entrega {DANO_D:.0f}. Então H de cura vale '
      f'{DANO_D/GRUPO:.2f} × H de dano.')
if abs(cura_pub - GRUPO) < 1:
    ok(f'o empate publicado ({cura_pub:.0f}) É a saída do grupo ({GRUPO:.0f}). Fecha.')
print()
novo_dano = DANO_D * FATOR_INT
print(f'  ⚠ MAS com o fator da `Intervenção`, o dano do `Desastre` vira {novo_dano:.0f}, e a razão')
print(f'    da cura passa de {DANO_D/GRUPO:.2f}× para {novo_dano/GRUPO:.2f}×.')
acende('C5', f'a frase publicada "curar vale 0,70 × H de dano" vira '
             f'{novo_dano/GRUPO:.2f} × H — mudou {abs(novo_dano/GRUPO - 0.70)/0.70:.0%}')
print('       >> Não muda a CONCLUSÃO (curar continua troca ruim). Muda o número impresso.')


# ---------------------------------------------------------------------------
bloco('O VEREDITO')
# ---------------------------------------------------------------------------
print(f'  A REGRA do §6.5 sobrevive inteira: `golpe ÷ 4,5`, e o Fundamento faz o resto.')
print(f'  O que envelheceu foram os NÚMEROS e DUAS FRASES.')
print()
print(f'  acenderam {len(ACENDEU)}: {", ".join(ACENDEU)}')
print()
print('   C2  a tabela de pontos — JÁ CONSERTADA aqui, falta trocar no repositório')
print('   C3  ⚠ CONTRADIÇÃO: `Recarga (5-6)` — o §6.5 reprova, o bloco adota')
print('   C4  ⚠ "um degrau de categoria" perdeu tamanho único na escada nova')
print('   C5  o número da cura mudou com o `0,923` (a conclusão não)')
print()
print('  E fica de fora daqui, porque já estava mapeado:')
print('   ·  a frase "as ações fora do turno... NUNCA POR CIMA" contradiz a decisão de 10/09')
print('      — é o item 4 da fila.')

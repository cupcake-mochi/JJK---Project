#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A `Recarga` — dimensionada, e a contradicao C3 resolvida.

Enquadramento do Mizuki, 10/09/2026: *"o recarga era pra ser aquela ACAO PESADA DA
RODADA que muda o combate no turno do inimigo, normalmente pro lado do dano... o
5-6 n é regra, era exemplo... seria aí onde entrariam tecnicas máximas, liberações
máximas e afins (o nome é flavor, n precisa de calculo a parte)."*

⚠ E isso DISSOLVE a objecao do §6.5. Ele dizia que "a cota nao paga a fracao que
sobra" — mas isso so' e' problema se a Recarga vier POR CIMA. Se ela OCUPA um slot
de acao, nada vem por cima: a fracao nao precisa ser paga, precisa ser DIMENSIONADA.
"""
import os, re, sys

REPO = os.environ.get('JJK_REPO', '/media/mizuki/HD Externo II/Claude/Claude 2')
BEST = os.environ.get('JJK_BEST', '/media/mizuki/HD Externo II/Claude/Claude 2/bestiario')
FATOR_INT = 0.923


def n(s): return float(s.replace(',', '.'))
def ler(rel, raiz=REPO):
    with open(os.path.join(raiz, rel), encoding='utf-8') as f: return f.read()
def pega(rel, pat, rot, raiz=REPO):
    m = re.search(pat, ler(rel, raiz))
    if not m: print(f'  !! ancora perdida: {rot}'); sys.exit(1)
    return m
def bloco(t): print(); print('=' * 88); print(t); print('=' * 88)


mD = pega('04-fase-1/TABELA.md',
          r'## `Desastre`[\s\S]*?\n\| 30 \| `\d+` \| `(\d+)` \| `(\d+)` \| `([^`]+)` \|',
          'o Desastre nv30', BEST)
DANO, ACOES = n(mD.group(1)), n(mD.group(2))
RODADAS = n(pega('04-fase-1/a-escada-com-numero.md',
                 r'\| `Desastre` \| `945` \| `[\d,]+` \| \*\*`([\d,]+)`\*\*', 'as rodadas',
                 BEST).group(1))
GOLPE = DANO * FATOR_INT / ACOES
SLOTS = ACOES * RODADAS
USOS = n(pega('03-bloco/RASCUNHO-5-o-bloco-em-branco.md',
              r'`Recarga \(5-6\)` dispara `([\d,]+)` vezes', 'os usos da Recarga', BEST).group(1))

bloco('AS ANCORAS')
print(f'  `Desastre` nv30 · {ACOES:.0f} ações · luta de {RODADAS:.0f} rodadas')
print(f'  o golpe normal, já com o × {FATOR_INT}      {GOLPE:.1f}')
print(f'  slots de ação na luta inteira        {SLOTS:.0f}')
print(f'  a `Recarga (5-6)` dispara            {USOS:.2f} vezes')

bloco('1. A CONTA — a Recarga OCUPA um slot, e os outros encolhem pra pagar')
print('  total da luta = usos × (k × golpe novo) + (slots − usos) × golpe novo')
print('  e ele tem de continuar igual a slots × golpe de hoje.')
print()
print(f'  {"a Recarga é":<18}{"golpe normal":>15}{"a Recarga":>13}{"quanto ela é":>16}'
      f'{"do golpe de hoje":>20}')
print('  ' + '-' * 82)
for k in (1.5, 2.0, 2.5, 3.0, 4.0):
    gl = SLOTS * GOLPE / (USOS * k + SLOTS - USOS)
    print(f'  {f"{k:.1f}× uma ação":<18}{gl:>15.1f}{gl*k:>13.1f}{gl*k/GOLPE:>15.2f}×'
          f'{gl/GOLPE:>19.2f}×')
print()
print('  >> Ler a tabela: quanto MAIOR a Recarga, MENORES os golpes normais. O total nao muda.')
print(f'  >> E `o golpe` que a ficha imprime passa a ser o NORMAL — o da coluna 2.')

bloco('2. O CONTRA-TESTE — o Sukuna que o projeto ja tinha escrito')
_s1 = ler('03-bloco/RASCUNHO-1-o-bloco.md', BEST)
mf = re.search(r'\*\*\*Fuga \(recarrega no `5–6`\)\.\*\*\*[\s\S]*?`(\d+) \(', _s1)
mc = re.search(r'\*\*\*Corte\.\*\*\*[\s\S]*?`(\d+) \(', _s1)
if mf and mc:
    fuga, corte = float(mf.group(1)), float(mc.group(1))
    print(f'  o `RASCUNHO-1` escreve, sem nenhuma conta por tras:')
    print(f'    `Corte` (a ação normal)          {corte:.0f}')
    print(f'    `Fuga (recarrega no 5–6)`        {fuga:.0f}')
    print(f'    >> a Recarga dele é {fuga/corte:.2f}× a ação normal.')
    print()
    gl = SLOTS * GOLPE / (USOS * (fuga/corte) + SLOTS - USOS)
    print(f'  >> Nessa razão ({fuga/corte:.2f}×), o golpe normal cairia pra {gl:.1f} '
          f'({gl/GOLPE:.2f}× o de hoje)')
    print(f'     e a Recarga bateria {gl*fuga/corte:.1f}.')
    print(f'  ⚠ Entao a intuicao dele quando escreveu o Sukuna JA ERA {fuga/corte:.1f}x — e a')
    print(f'     conta so diz o preco disso: os golpes normais ficam '
          f'{(1-gl/GOLPE)*100:.0f}% menores.')

bloco('3. E O QUE ISSO FAZ COM A OBJECAO DO §6.5')
print('  O §6.5 dizia: "a recarga 5-6 dispara 1,67 vezes... e a cota nao paga a fracao que sobra".')
print()
print('  ⚠ Isso so e problema se a Recarga vier POR CIMA das acoes dele.')
print('  >> No enquadramento do Mizuki ela OCUPA uma acao. Entao nao ha fracao a pagar:')
print('     ha uma fracao a DIMENSIONAR, e a conta acima dimensiona.')
print()
print('  >> E a `1× por luta` do §6.5 continua valendo — ela e o caso `usos = 1`.')
gl1 = SLOTS * GOLPE / (1 * 2.0 + SLOTS - 1)
print(f'     Com `1× por luta` e a habilidade valendo 2,0× uma acao, o golpe normal fica em')
print(f'     {gl1:.1f} ({gl1/GOLPE:.2f}×) — encolhe MENOS que com a Recarga, porque dispara menos.')

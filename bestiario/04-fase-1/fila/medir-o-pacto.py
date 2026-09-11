#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
O `pacto` no bloco — item 1 da fila.

A pergunta: uma coisa que so' ALGUNS blocos tem precisa de linha declarada, ou
ela cabe na lista variavel de `Traços`?

Conta tracos por bloco nos dois sistemas em disco. Se muitos blocos tem ZERO,
a lista variavel ja' resolve "opcional" sozinha — e nao precisa de celula.
"""
import collections
import json
import os
import re
import statistics
import sys

BEST = os.environ.get('JJK_BEST', '/media/mizuki/HD Externo II/Claude/Claude 2/bestiario')
SRD = os.path.join(BEST, '04-fase-1/fila/srd-2024.json')
DS = os.path.join(BEST, '04-fase-1/fila/dados-recarga-area/data-md-main'
                        '/Bestiary/Monsters/Monsters')
ANCORAS = os.path.join(BEST, '05-sukuna/ANCORAS-do-repositorio.md')


def bloco(t):
    print()
    print('=' * 90)
    print(t)
    print('=' * 90)


# ---------------------------------------------- 1 · o pacto e' derivavel?
bloco('1. QUANTOS PACTOS — a conta que decide se ele ganha celula')
txt = open(ANCORAS, encoding='utf-8').read()
m = re.search(r'\*\*Você fecha, em toda a campanha, um número de pactos permanentes igual a '
              r'(metade da sua Essência), arredondando para baixo\.\*\*', txt)
if not m:
    print('  !! ANCORA PERDIDA: a regra de quantos pactos, peça 22 §3.1')
    sys.exit(1)
print()
print(f'  peça 22 §3.1: "um número de pactos permanentes igual a {m.group(1)},')
print('                 arredondando para baixo."')
print()
mt = re.search(r'\| \*\*pactos permanentes\*\* \| ((?:\d+ \| ?)+)', txt)
if mt:
    v = re.findall(r'\d+', mt.group(1))
    print('  Essência  ' + '  '.join(f'{i}' for i in range(len(v))))
    print('  pactos    ' + '  '.join(v))
print()
print('  >> a Essência JA esta no bloco, na linha de atributos.')
print('  >> e o bloco ja cortou `Iniciativa` e `Reação 1 por rodada` pela mesma regra:')
print('     "numero derivavel nao ganha celula".')


# ------------------------------------- 2 · lista variavel resolve opcional?
bloco('2. O CONTEÚDO — lista variável resolve "opcional"? contado nos dois sistemas')
d = json.load(open(SRD, encoding='utf-8'))
c = collections.Counter(len(mm.get('traits') or []) for mm in d)
tot = len(d)
n = [len(mm.get('traits') or []) for mm in d]
if tot < 300:
    print(f'  !! li so {tot} monstros do SRD')
    sys.exit(1)
print()
print(f'  D&D 2024 SRD — {tot} monstros')
for k in sorted(c):
    print(f'    {k:>2} traços: {c[k]:>4}  ({c[k]/tot:>4.0%})')
print(f'    mediana {statistics.median(n):.0f} · média {statistics.mean(n):.1f} · máx {max(n)}')
print(f'    >> {c[0]/tot:.0%} têm ZERO traços — a seção some quando não tem nada.')

cc = collections.Counter()
m2 = 0
for dp, _, fs in os.walk(DS):
    if 'Statblocks' not in dp:
        continue
    for f in sorted(fs):
        if not f.endswith('.md'):
            continue
        t = open(os.path.join(dp, f), encoding='utf-8').read()
        if not re.match(r'^---\n', t):
            continue
        m2 += 1
        cc[len(re.findall(r'\n> ⭐️ \*\*', t))] += 1
if m2 < 380:
    print(f'  !! li so {m2} statblocks do Draw Steel')
    sys.exit(1)
print()
print(f'  Draw Steel — {m2} statblocks')
for k in sorted(cc):
    print(f'    {k:>2} traços: {cc[k]:>4}  ({cc[k]/m2:>4.0%})')
print(f'    >> {cc[0]/m2:.0%} têm ZERO.')
print()
print('  >> nenhum dos dois cria CELULA FIXA pra coisa opcional. Os dois usam lista')
print('     variavel, e ela some sozinha quando esta vazia.')


bloco('⟹ AS DUAS PORTAS QUE JÁ EXISTEM')
print()
print('  o voto restringe UMA ação      -> parêntese de pré-requisito no nome dela')
print('                                    (item 13, fechado em 10/09)')
print('  o voto restringe o INIMIGO     -> um `Traço`')
print()
print('  E o numero de pactos nao vai a lugar nenhum: ele e' + ' Essencia ÷ 2.')

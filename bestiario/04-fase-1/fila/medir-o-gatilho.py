#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
O GATILHO DA `Chama Divina` — item 13 da fila.

A pergunta: "so' depois de `Desmembrar` e `Clivar`" nao e' nenhum dos quatro
rotulos de frequencia (a vontade · 1x/rodada · 1x/luta · Recarga 5-6).
E' QUINTO ROTULO, ou TEXTO DA ACAO?

O `ESTADO` ja registrou que "8 de 9 sistemas usam rotulo de frequencia OU
GATILHO — o gatilho so' ficou fora da nossa lista". Este script mede COMO os
tres sistemas em disco escrevem isso.

Amostras: D&D 2024 SRD 989 acoes · Draw Steel 544 blocos · PF2e 677 habilidades
"""
import collections
import json
import os
import re
import statistics
import sys

BEST = os.environ.get('JJK_BEST', '/media/mizuki/HD Externo II/Claude/Claude 2/bestiario')
FILA = os.path.join(BEST, '04-fase-1/fila')
DSMON = os.path.join(FILA, 'dados-recarga-area/data-md-main/Bestiary/Monsters/Monsters')
BLOCO = os.path.join(BEST, '03-bloco/RASCUNHO-5-o-bloco-em-branco.md')


def bloco(t):
    print()
    print('=' * 96)
    print(t)
    print('=' * 96)


# ------------------------------------------------- os nossos quatro rotulos
txt = open(BLOCO, encoding='utf-8').read()
ROT = re.findall(r'^\| \*\*`([^`]+)`\*\* \| ', txt, re.M)
ROT = [r for r in ROT if re.search(r'\d|vontade|Recarga', r)]
mab = re.search(r'`‹ nome › \*\*\(Ação Bônus\)\.\*\*`', txt) or re.search(r'\(Ação Bônus\)', txt)

bloco('AS NOSSAS QUATRO — e a quinta que já existe sem ser rótulo')
print()
msil = re.search(r'\| \*\*‹ sem rótulo ›\*\* \| \*\*(à vontade)', txt)
print(f'  Os rótulos de frequência do `RASCUNHO-5` — são {len(ROT) + (1 if msil else 0)}:')
if msil:
    print(f'    ‹ sem rótulo › = {msil.group(1)}  — o quarto é o SILÊNCIO, e é o padrão')
for r in ROT:
    print(f'    `{r}`')
print()
print('  E JÁ existe um parêntese que NÃO é frequência, e ninguém chamou de quinto rótulo:')
print(f'    `(Ação Bônus)` — {"achado no bloco" if mab else "NAO ACHADO"}')
print('    O `ESTADO` registra: "não vira célula: vira linha no capítulo de combate')
print('    + rótulo `(Ação Bônus)`". Ele divide o SLOT com os quatro e é OUTRO EIXO.')


# ------------------------------------------------------------- D&D 2024 SRD
DND = json.load(open(os.path.join(FILA, 'srd-2024.json'), encoding='utf-8'))
ul, lf, at = collections.Counter(), [], collections.Counter()
n_acoes = 0
for m in DND:
    for a in (m.get('actions') or []):
        n_acoes += 1
        u = a.get('usage_limits')
        ul[(u or {}).get('type') or '(sem limite)'] += 1
        at[a.get('action_type')] += 1
        if a.get('limited_to_form'):
            lf.append((a['name'], a['limited_to_form']))
if n_acoes < 900:
    print(f'\n  !! li so {n_acoes} acoes do SRD')
    sys.exit(1)

bloco('1. D&D 2024 SRD — DOIS campos separados, e o de pré-requisito existe')
print()
print(f'  {n_acoes} ações em 331 monstros.')
print()
print('  `usage_limits` — o campo de FREQUÊNCIA:')
for k, v in ul.most_common():
    if k != '(sem limite)':
        print(f'    {v:>4}  {k}')
print(f'    {ul["(sem limite)"]:>4}  (sem limite)')
freq = sum(v for k, v in ul.items() if k != '(sem limite)')
print(f'    ⟹ {freq} de {n_acoes} ações ({freq/n_acoes:.0%}) carregam limite de frequência.')
print()
print('  `limited_to_form` — o campo de PRÉ-REQUISITO, e ele é OUTRO:')
for nome, cond in lf:
    print(f'    {nome} ({cond})')
print(f'    ⟹ {len(lf)} de {n_acoes} ações ({len(lf)/n_acoes:.1%}).')
print()
print('  >> O SRD tem DOIS campos, e o pre-requisito NAO entra na lista de frequencia.')
print('  >> E os dois saem impressos no MESMO lugar: parentese depois do nome.')
print()
comp = [len(c) for _, c in lf]
print(f'  ⚠ E o pré-requisito deles é CURTO: mediana {statistics.median(comp):.0f} caracteres, '
      f'de {min(comp)} a {max(comp)}.')
NOSSO = 'depois de `Desmembrar` e `Clivar`'
print(f'     O nosso — "{NOSSO}" — tem {len(NOSSO)} caracteres. Mesma faixa.')


# ---------------------------------------------------------------- Draw Steel
hab = trig = pre = 0
for dp, _, fs in os.walk(DSMON):
    if 'Statblocks' not in dp:
        continue
    for f in sorted(fs):
        if not f.endswith('.md'):
            continue
        t = open(os.path.join(dp, f), encoding='utf-8').read()
        for b in re.split(r'\n> [🗡⭐️💥🌟]', t):
            if 'Power Roll' in b or 'Effect:' in b:
                hab += 1
                if re.search(r'\*\*Trigger:\*\*', b):
                    trig += 1
                if re.search(r'only (if|when|while)|can only|must (be|have)', b, re.I):
                    pre += 1

bloco('2. Draw Steel — `Trigger:` é campo NOMEADO, não parêntese')
print()
print(f'  {hab} blocos de habilidade em 416 statblocks.')
print()
print(f'  {"com **Trigger:** — campo nomeado":<40}{trig:>6}{trig/hab:>8.0%}')
print(f'  {"com pré-requisito em PROSA":<40}{pre:>6}{pre/hab:>8.0%}')
print()
print('  >> `Trigger:` e' + ' uma LINHA dentro do bloco da habilidade, e ela e' + ' 4,8x mais')
print('     comum que condicao solta em prosa.')


# ---------------------------------------------------------------- PF2e
PF = json.load(open(os.path.join(FILA, 'pf2e-recarga.json'), encoding='utf-8'))
c = collections.Counter()
for a in PF:
    t = a.get('text') or ''
    for campo in ('Trigger', 'Requirements', 'Frequency', 'Prerequisites', 'Effect'):
        if re.search(r'\b' + campo + r'\b', t):
            c[campo] += 1

bloco('3. Pathfinder 2e — QUATRO campos nomeados, e eles são eixos diferentes')
print()
print(f'  {len(PF)} habilidades.')
print(f'  ⚠ AMOSTRA ENVIESADA: ela veio de uma busca por RECARGA ("again for 1d4 rounds"),')
print(f'     entao ela superestima quem tem Frequency e Trigger. Use a EXISTENCIA dos')
print(f'     campos, nao a proporcao.')
print()
for k in ('Effect', 'Trigger', 'Frequency', 'Requirements', 'Prerequisites'):
    print(f'  {k:<16}{c[k]:>6}{c[k]/len(PF):>8.0%}')
print()
print('  >> o PF2e separa em quatro: `Frequency` (quantas vezes), `Trigger` (o que dispara),')
print('     `Requirements` (o que precisa estar valendo) e `Effect` (o que acontece).')
print('  >> `Frequency` e `Requirements` sao campos DIFERENTES, e os dois existem.')


bloco('⟹ O VEREDITO')
print()
print('  Nos TRES sistemas, pre-requisito e frequencia sao EIXOS SEPARADOS.')
print('  Nenhum dos tres enfia pre-requisito na lista de rotulos de frequencia.')
print()
print(f'  {"sistema":<16}{"frequência":<22}{"pré-requisito":<26}{"onde sai impresso":<22}')
print('  ' + '-' * 88)
print(f'  {"D&D 2024":<16}{"usage_limits":<22}{"limited_to_form":<26}{"parêntese após o nome":<22}')
print(f'  {"Draw Steel":<16}{"palavra-chave":<22}{"prosa / **Trigger:**":<26}{"linha no bloco":<22}')
print(f'  {"Pathfinder 2e":<16}{"Frequency":<22}{"Requirements":<26}{"linha no bloco":<22}')
print(f'  {"— o nosso —":<16}{"4 rótulos":<22}{"NÃO EXISTE":<26}{"—":<22}')
print()
print('  E o nosso ja tem a FORMA pronta e usada: o `(Ação Bônus)` e' + ' um parentese que')
print('  divide o slot com os quatro rotulos e nao e' + ' frequencia. E' + ' o mesmo desenho do')
print('  `limited_to_form` do D&D 2024.')

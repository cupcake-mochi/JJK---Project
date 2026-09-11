#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
QUANTO DANO UMA VILLAIN ACTION FAZ, comparada a uma acao normal do MESMO bicho.

Pedido do Mizuki, 10/09/2026: *"Como outros sistemas fazem? principalmente drawn
steel. Sempre q me perguntar algo que pode ser pesquisado e validado, pesquisa
primeiro."*

⚠ OS NUMEROS DESTE BLOCO SAO EXTERNOS. Eles vem dos statblocks oficiais do
Draw Steel, no repositorio de dados do Steel Compendium:
  https://raw.githubusercontent.com/SteelCompendium/data-md/main/Bestiary/Monsters/Monsters/<...>

Todos os valores sao do TIER 2, que e' o resultado normal da rolagem
(modificador x1,1, contra x0,6 do tier 1 e x1,4 do tier 3).
"""
import statistics

# nome, nivel, organizacao, dano do SIGNATURE/acao principal no tier 2, [VA1, VA2, VA3] no tier 2
BLOCOS = [
    ('Thorn Dragon', 2, 'Solo', 9,
     [('Briar Bindings', 9), ('Thorned Armor', 0), ('Malign Thicket', 0)],
     'Virulent Breath (Signature)'),
    ('Ajax the Invincible', 11, 'Solo', 22,
     [('Phoenix Wing King', 17), ("I've Learned Their Tricks", 0), ('Awe of the Iron Crown', 0)],
     'Blade of the Gol King'),
    ('Count Rhodar von Glauer', 10, 'Solo', 18,
     [('Red Tide', 13), ('Sanguine Mist', 13), ('Fires of Dracul', 16)],
     'Spear of the Damned (Signature)'),
]

print('=' * 92)
print('AS VILLAIN ACTIONS DO DRAW STEEL, medidas contra a acao normal do mesmo bicho')
print('=' * 92)
print()
print('  Tudo no TIER 2 — o resultado normal da rolagem.')
print()
todas = []
for nome, nv, org, base, vas, rot_base in BLOCOS:
    print(f'  {nome}  ·  nível {nv}  ·  {org}')
    print(f'    {"a ação normal":<32}{rot_base:<34}{base:>6}')
    for rot, dano in vas:
        r = dano / base
        todas.append(r)
        print(f'    {"villain action":<32}{rot:<34}{dano:>6}   {r:>6.0%} da ação normal')
    print()

print('  ' + '-' * 88)
print(f'  {len(todas)} villain actions medidas, em {len(BLOCOS)} criaturas `Solo`.')
print()
print(f'  a MAIOR delas          {max(todas):.0%} da ação normal')
print(f'  a MENOR                {min(todas):.0%}')
print(f'  a MÉDIA                {statistics.mean(todas):.0%}')
print(f'  a MEDIANA              {statistics.median(todas):.0%}')
zeros = sum(1 for r in todas if r == 0)
print(f'  quantas fazem ZERO     {zeros} de {len(todas)}')
print()
print('  >> ACHADO 1: NENHUMA villain action bate mais forte que uma acao normal do bicho.')
print(f'     O teto medido e {max(todas):.0%}.')
print(f'  >> ACHADO 2: {zeros} das {len(todas)} nao causam dano NENHUM — elas sao controle,')
print('     terreno, reposicionamento ou setup pro golpe seguinte.')
print('  >> ACHADO 3: em 2 das 3 criaturas, as villain actions 2 e 3 sao as que nao causam dano.')
print('     A 1 abre com dano; as outras duas mudam o campo.')

print()
print('=' * 92)
print('O QUE ISSO FAZ COM A RECALIBRACAO DO PROJETO-M')
print('=' * 92)
# ancoras do Projeto-M
DANO_D, ACOES_D, RODADAS, N_INT = 219.0, 3.0, 3.0, 3
VIDA_PC = 243.0
UMA_ACAO = DANO_D / ACOES_D
print(f'  o `Desastre` nv30: dano {DANO_D:.0f} em {ACOES_D:.0f} ações, uma ação = {UMA_ACAO:.2f},')
print(f'  luta de {RODADAS:.0f} rodadas, {N_INT} Intervenções.')
print()
print(f'  {"se a Intervenção valer":<38}{"ações extras na luta":>22}{"fator":>9}'
      f'{"dano novo":>12}{"o golpe":>10}{"fatia":>8}')
print('  ' + '-' * 90)
CENARIOS = [
    ('uma AÇÃO INTEIRA (o que eu supus)', 1.00),
    (f'a MÉDIA medida do Draw Steel ({statistics.mean(todas):.0%})', statistics.mean(todas)),
    ('a FORMA do campo: 1 com dano, 2 sem', 0.75 / 3),
]
for rot, peso in CENARIOS:
    extras = N_INT * peso
    fator = RODADAS / (RODADAS + extras / ACOES_D)
    dano_novo = DANO_D * fator
    golpe = dano_novo / ACOES_D
    print(f'  {rot:<38}{extras:>22.2f}{fator:>9.3f}{dano_novo:>12.1f}{golpe:>10.1f}'
          f'{golpe / VIDA_PC:>7.0%}')
print()
print('  ⚠ E o meu palpite era o CENARIO DE CIMA — o mais pesado dos tres, e o unico que o')
print('     campo NAO faz. A recalibracao que eu ia propor cortava 25% do dano de todo')
print('     inimigo, e a medida diz que o corte honesto e' + ' menor.')
print()
print('  >> E o mais fiel ao campo e' + ' a linha de baixo: a `Intervenção 1` bate (um pouco menos')
print('     que uma acao normal), e a `2` e a `3` MUDAM O CAMPO em vez de causar dano.')
print('     Nessa forma o dano extra e' + f' {N_INT * 0.75/3:.2f} de uma acao na luta inteira, e o')
print(f'     fator fica em {RODADAS / (RODADAS + (N_INT * 0.75/3) / ACOES_D):.3f} — quase nada.')

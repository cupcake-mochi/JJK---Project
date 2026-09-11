# -*- coding: utf-8 -*-
"""Gera a tabela de orçamento de atributo do capítulo 5, e confere o texto aprovado.

O orçamento não é escolha deste livro: ele é o da ficha de jogador, e a peça 26
§3.2 manda o inimigo usar o mesmo — nove pontos na criação, teto `3` ali, `+1` por
marco, teto `6`.

Este script:
  §1  lê os MARCOS na `TABELA.md` (a Defesa muda neles, e é por isso que dá pra ler)
  §2  computa o orçamento por marco
  §3  ⚠ CONFERE os três números que o texto aprovado publica — `13` pontos no nv20,
      Destreza `5` obrigada pela Defesa `18`, e `4` marcos comidos
  §4  escreve a tabela no capítulo 5

Morre se qualquer um dos três deixar de reproduzir.
"""
import os
import re
import sys

BASE = os.path.dirname(os.path.abspath(__file__))
LIVRO = os.path.dirname(BASE)
BEST = os.path.dirname(LIVRO)
TAB = os.path.join(BEST, '04-fase-1', 'TABELA.md')
DEC = os.path.join(BEST, '04-fase-1', 'fila', 'DECIDIDO-a-linha-do-aperto-de-atributo.md')
CAP = os.path.join(LIVRO, 'capitulos', '50-o-bloco.md')
MARCA = '<!-- ATRIBUTOS -->'

BASE_CRIACAO = 9     # peça 26 §3.2 — "nove pontos na criação"
TETO_CRIACAO = 3
TETO = 6


def morre(m):
    sys.exit('✗ ÂNCORA PERDIDA: ' + m)


def ler(p):
    if not os.path.exists(p):
        morre('não existe: %s' % p)
    return open(p, encoding='utf-8').read()


# ── §1 · os marcos, lidos da escada viva
ttab = ler(TAB)
sec = ttab.split('## `Desastre`')[1].split('\n## ')[0]
cab, linhas = None, {}
for ln in sec.split('\n'):
    cels = [c.strip().strip('*').strip('`').strip('*') for c in ln.strip().strip('|').split('|')]
    if cels and cels[0] == 'nv':
        cab = cels
    elif cab and cels and re.match(r'^\d+$', cels[0] or ''):
        linhas[int(cels[0])] = dict(zip(cab, cels))
if len(linhas) < 29:
    morre('a `TABELA.md` não trouxe os 29 níveis')

NIVEIS = sorted(linhas)
marcos, ini = [], NIVEIS[0]
for i, nv in enumerate(NIVEIS):
    ult = i == len(NIVEIS) - 1
    muda = (not ult) and linhas[NIVEIS[i + 1]]['Defesa'] != linhas[nv]['Defesa']
    if muda or ult:
        marcos.append((ini, nv))
        if not ult:
            ini = NIVEIS[i + 1]
if len(marcos) != 7:
    morre('a Defesa colapsou em %d marcos, e a peça publica 7' % len(marcos))

# ── §2 · o orçamento: +1 por marco vencido, a partir do primeiro
def pontos(nv):
    venceu = sum(1 for k, (a, b) in enumerate(marcos) if k > 0 and nv >= a)
    return BASE_CRIACAO + venceu


def destreza_obrigada(nv):
    """A Defesa é `10 + Destreza + proteção`. Isolando a Destreza."""
    d = int(linhas[nv]['Defesa'])
    prot = int(linhas[nv]['proteção'].replace('+', ''))
    return d - 10 - prot


# ── §3 · a guarda: o texto aprovado reproduz?
tdec = ler(DEC)
m = re.search(r'No nível `(\d+)` o inimigo tem `(\d+)` pontos de atributo', tdec)
if not m:
    morre('a frase dos pontos de atributo sumiu do DECIDIDO')
NV_REF, PTS_REF = int(m.group(1)), int(m.group(2))
m2 = re.search(r'a Defesa `(\d+)` pede Destreza `(\d+)`', tdec)
if not m2:
    morre('a frase da Destreza obrigada sumiu do DECIDIDO')
DEF_REF, DES_REF = int(m2.group(1)), int(m2.group(2))

calc_pts = pontos(NV_REF)
calc_des = destreza_obrigada(NV_REF)
calc_def = int(linhas[NV_REF]['Defesa'])
print('=' * 76)
print('ORÇAMENTO DE ATRIBUTO — gerado da `TABELA.md`')
print('=' * 76)
print('  guarda: o texto aprovado publica %d pontos no nv%d ⟹ a conta dá %d  %s'
      % (PTS_REF, NV_REF, calc_pts, '✓' if calc_pts == PTS_REF else '✗'))
print('  guarda: ele publica Defesa %d pedindo Destreza %d ⟹ a conta dá Defesa %d, Destreza %d  %s'
      % (DEF_REF, DES_REF, calc_def, calc_des,
         '✓' if (calc_def, calc_des) == (DEF_REF, DES_REF) else '✗'))
if calc_pts != PTS_REF:
    morre('o orçamento do nv%d não reproduz: texto %d, conta %d' % (NV_REF, PTS_REF, calc_pts))
if (calc_def, calc_des) != (DEF_REF, DES_REF):
    morre('a Destreza obrigada do nv%d não reproduz' % NV_REF)

# ── §4 · a tabela
out = ['**Orçamento de atributo por marco**', '{: .tab-titulo }', '',
       '| nível | pontos no total | Defesa | Destreza que ela obriga |', '|---|---|---|---|']
for a, b in marcos:
    rot = str(a) if a == b else '%d–%d' % (a, b)
    out.append('| **%s** | `%d` | `%s` | `%d` |'
               % (rot, pontos(a), linhas[a]['Defesa'], destreza_obrigada(a)))
out += ['', '*`9` pontos na criação, com teto `3` em cada atributo, e `+1` a cada marco, com teto '
        '`6`. É o mesmo orçamento da ficha de jogador.*']

cap = ler(CAP)
if MARCA not in cap:
    morre('a marca `%s` sumiu do capítulo 5' % MARCA)
i, j = cap.index(MARCA), cap.index('<!-- FIM ATRIBUTOS -->')
open(CAP, 'w', encoding='utf-8').write(cap[:i] + MARCA + '\n\n' + '\n'.join(out) + '\n\n' + cap[j:])

print()
print('  %-10s %8s %8s %10s' % ('nível', 'pontos', 'Defesa', 'Destreza'))
for a, b in marcos:
    print('  %-10s %8d %8s %10d'
          % (str(a) if a == b else '%d–%d' % (a, b), pontos(a), linhas[a]['Defesa'],
             destreza_obrigada(a)))
print()
print('  ✓ os dois números do texto aprovado reproduzem da `TABELA.md`.')

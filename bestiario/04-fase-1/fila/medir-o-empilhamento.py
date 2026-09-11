#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
O TETO DE EMPILHAMENTO DO `Capanga` — item 19 da fila.

Achado em 10/09 medindo o `Controlador` contra o Draw Steel: o nosso `Capanga`
nao tem trava nenhuma pra quantos corpos batem na MESMA pessoa. Oito corpos batem
oito golpes cheios em quem o mestre quiser.

O Draw Steel tem a trava escrita, e ela tem duas partes:
  - teto DURO: no maximo 2 ou 3 corpos no mesmo alvo
  - desconto: cada corpo alem do primeiro entrega FREE STRIKE, nao a assinatura

Este script mede o desconto (free strike / dano esperado da assinatura) nos
minions do Draw Steel, e traduz a trava pra nossa escada.

Nenhum numero nosso mora aqui: cada ancora e lida do documento dono.
"""
import os
import re
import statistics
import sys

BEST = os.environ.get('JJK_BEST', '/media/mizuki/HD Externo II/Claude/Claude 2/bestiario')
DS = os.path.join(BEST, '04-fase-1/fila/dados-recarga-area/data-md-main')
STAT = os.path.join(DS, 'Bestiary/Monsters/Monsters')
BASICS = os.path.join(DS, 'Bestiary/Monsters/Chapters/Monster Basics.md')
HEROES = os.path.join(DS, 'Rules/Draw Steel Heroes.md')

TABELA = '04-fase-1/TABELA.md'
ESCADA = '04-fase-1/a-escada-com-numero.md'
ANCORAS = '05-sukuna/ANCORAS-do-repositorio.md'
TAMDEC = '04-fase-1/fila/DECIDIDO-o-tamanho.md'

_c = {}


def ler(p, raiz=None):
    q = os.path.join(raiz, p) if raiz else p
    if q not in _c:
        with open(q, encoding='utf-8') as f:
            _c[q] = f.read()
    return _c[q]


def n(s):
    return float(s.replace('−', '-').replace(',', '.'))


def pega(p, padrao, rotulo, raiz=BEST):
    m = re.search(padrao, ler(p, raiz))
    if not m:
        print(f'\n  !! ANCORA PERDIDA: {rotulo}\n     nao casa em {p}')
        sys.exit(1)
    return m


def bloco(t):
    print()
    print('=' * 96)
    print(t)
    print('=' * 96)


def media_dado(e):
    e = e.strip()
    m = re.match(r'(\d+)d(\d+)(?:\s*\+\s*(\d+))?$', e)
    if m:
        return int(m.group(1)) * (1 + int(m.group(2))) / 2 + int(m.group(3) or 0)
    return float(e) if re.match(r'^\d+$', e) else None


# ---------------------------------------------------------------- a regra deles
bloco('1. A TRAVA DO DRAW STEEL, colada')
t = ler(BASICS)
q1 = re.search(r'(Each target of a minion\'s signature ability is affected by only one instance.+?)\n', t)
q2 = re.search(r'(Because a minion\'s free strike value is typically lower.+?)\n', t)
if not q1 or not q2:
    print('  !! ANCORA PERDIDA: a regra de squad attack')
    sys.exit(1)
print()
print('  "' + q1.group(1) + '"')
print()
print('  "' + q2.group(1) + '"')
print()
mteto = re.search(r'when (two or three) \(at maximum\)', q1.group(1))
print(f'  >> teto DURO: {mteto.group(1)} corpos no mesmo alvo.')
print(f'  >> e do 2o em diante o corpo entrega FREE STRIKE, nao a assinatura.')


# ------------------------------------------------------- o desconto, medido
def esperado(bonus, t1, t2, t3):
    """dano esperado de um power roll 2d10+bonus com as tres faixas.
    natural 19 ou 20 (o 2d10 cru) sempre da tier 3."""
    tot = 0.0
    for a in range(1, 11):
        for b in range(1, 11):
            cru = a + b
            if cru >= 19:
                tot += t3
                continue
            v = cru + bonus
            tot += t1 if v <= 11 else (t2 if v <= 16 else t3)
    return tot / 100.0


MIN = []
for dp, _, fs in os.walk(STAT):
    if 'Statblocks' not in dp:
        continue
    for f in sorted(fs):
        if not f.endswith('.md'):
            continue
        txt = ler(os.path.join(dp, f))
        mfm = re.search(r'^---\n(.*?)\n---', txt, re.S)
        if not mfm:
            continue
        fm = mfm.group(1)
        mr = re.search(r'^roles:\n((?:  - .+\n)+)', fm, re.M)
        if not mr or 'Minion' not in mr.group(1):
            continue
        mfs = re.search(r'^free_strike: (\d+)$', fm, re.M)
        mlv = re.search(r'^level: (\d+)$', fm, re.M)
        if not (mfs and mlv):
            continue
        # a assinatura: "Power Roll + N:" seguido das tres faixas
        ma = re.search(r'\*\*Power Roll \+ (\d+):\*\*[\s>]*\n'
                       r'[>\s]*- \*\*≤11:\*\* (\d+)[^\n]*\n'
                       r'[>\s]*- \*\*12-16:\*\* (\d+)[^\n]*\n'
                       r'[>\s]*- \*\*17\+:\*\* (\d+)', txt)
        if not ma:
            continue
        b, t1, t2, t3 = (int(ma.group(i)) for i in range(1, 5))
        MIN.append({'nome': f[:-3], 'nv': int(mlv.group(1)), 'fs': int(mfs.group(1)),
                    'assin': esperado(b, t1, t2, t3)})

if len(MIN) < 60:
    print(f'\n  !! li so {len(MIN)} minions com assinatura parseavel')
    sys.exit(1)

bloco('2. O DESCONTO, MEDIDO — free strike contra o dano esperado da assinatura')
print()
print(f'  {len(MIN)} minions com assinatura parseável. Power roll = 2d10 + bônus,')
print(f'  faixas ≤11 / 12-16 / 17+, e natural 19-20 sempre dá tier 3.')
print()
raz = [m['fs'] / m['assin'] for m in MIN if m['assin'] > 0]
print(f'  {"":<22}{"mediana":>10}{"média":>10}{"mín":>8}{"máx":>8}')
print('  ' + '-' * 58)
print(f'  {"free strike":<22}{statistics.median([m["fs"] for m in MIN]):>10.2f}'
      f'{statistics.mean([m["fs"] for m in MIN]):>10.2f}'
      f'{min(m["fs"] for m in MIN):>8}{max(m["fs"] for m in MIN):>8}')
print(f'  {"assinatura esperada":<22}{statistics.median([m["assin"] for m in MIN]):>10.2f}'
      f'{statistics.mean([m["assin"] for m in MIN]):>10.2f}'
      f'{min(m["assin"] for m in MIN):>8.1f}{max(m["assin"] for m in MIN):>8.1f}')
print(f'  {"RAZÃO fs / assinatura":<22}{statistics.median(raz):>10.3f}'
      f'{statistics.mean(raz):>10.3f}{min(raz):>8.2f}{max(raz):>8.2f}')
R = statistics.median(raz)
print()
print(f'  >> o corpo empilhado entrega {R:.1%} do que ele entregaria batendo em outro alvo.')
print(f'  >> e o livro diz isso em palavras: "typically lower than the average damage".')


bloco('3. O QUE A TRAVA FAZ — empilhar contra espalhar, na conta deles')
print()
for teto in (2, 3):
    stack = 1 + (teto - 1) * R
    spread = teto
    print(f'  {teto} corpos no MESMO alvo:  1 assinatura + {teto-1} free strike = {stack:.3f} assinaturas')
    print(f'  {teto} corpos ESPALHADOS:     {spread} assinaturas')
    print(f'    >> empilhar entrega {stack/spread:.1%} do que espalhar entrega. '
          f'Perde {1-stack/spread:.1%}.')
    print()
print('  >> a trava tem DUAS partes, e as duas importam:')
print('     o teto DURO (3) impede a alfinetada de 8; o DESCONTO tira a vontade de usar o teto.')


# --------------------------------------------------------- traduzindo pro nosso
bloco('4. O NOSSO `Capanga` — o buraco, com número')
CORPOS = int(pega(ESCADA, r'\| \*\*`Capanga`\*\* \| — \| `dano do grupo ÷ 4` \| `[\d,]+` \| `1` \| `(\d+)`',
                  'os corpos do `Capanga`').group(1))
CATS, atual = {}, None
for ln in ler(TABELA, BEST).split('\n'):
    m = re.match(r'## `([^`]+)`', ln)
    if m:
        atual = m.group(1)
        CATS.setdefault(atual, {})
        continue
    m = re.match(r'\| (\d+) \| `(\d+)` \| \*\*`(\d+)`\*\* \| `([^`]+)` \|', ln)
    if m and atual == 'Capanga':
        CATS['Capanga'][int(m.group(1))] = {'vida': int(m.group(2)), 'golpe': media_dado(m.group(4))}
    m = re.match(r'\| (\d+) \| `(\d+)` \| `(\d+)` \| `(\d+)` \| `([^`]+)` \|', ln)
    if m and atual == 'Desastre':
        CATS['Desastre'][int(m.group(1))] = {'vida': int(m.group(2)), 'golpe': media_dado(m.group(5))}
GRUPO = {}
for ln in ler(ANCORAS, BEST).split('\n'):
    m = re.match(r'\| \*{0,2}(\d+)\*{0,2} \| \*{0,2}~(\d+)\*{0,2} \| \*{0,2}\d+ a \d+', ln)
    if m:
        GRUPO[int(m.group(1))] = float(m.group(2))
mf = pega(ESCADA, r'\| 20 \| `[\d,]+%` \| `[\d,]+%` \| `([\d,]+)%` \|', 'a fatia do Desastre nv20')
VIDA_PC20 = CATS['Desastre'][20]['golpe'] / (n(mf.group(1)) / 100)

print()
print(f'  nv20: o capanga bate {CATS["Capanga"][20]["golpe"]:.0f} · são {CORPOS} corpos · '
      f'o personagem tem {VIDA_PC20:.0f} de vida')
print()
print(f'  {"quantos batem no mesmo alvo":<32}{"dano":>9}{"% da vida de 1 PC":>20}{"mata?":>9}')
print('  ' + '-' * 72)
g = CATS['Capanga'][20]['golpe']
for k in (1, 2, 3, 4, CORPOS):
    d = k * g
    print(f'  {k:<32}{d:>9.0f}{d/VIDA_PC20:>19.0%}{("SIM" if d >= VIDA_PC20 else "não"):>9}')
print()
lim = VIDA_PC20 / g
print(f'  >> {CORPOS} corpos entregam {CORPOS*g/VIDA_PC20:.0%} da vida de um personagem NUMA RODADA.')
print(f'  >> bastam {lim:.1f} corpos pra derrubar alguém. Hoje nada na regra impede os {CORPOS}.')


bloco('5. A TRAVA TRADUZIDA — o que cada forma entrega')
print()
print('  Traduzindo a regra deles: teto DURO de N corpos, e do 2o em diante o corpo')
print(f'  entrega uma fração do golpe. A fração medida no campo e {R:.3f}.')
print()
MEIO = 0.5   # o `Estilhaço` ja publica "metade dos dados respinga" — e a fracao que o sistema tem
print(f'  {"forma":<38}{"máx num alvo":>14}{"% da vida do PC":>18}{"mata?":>9}')
print('  ' + '-' * 80)
opts = [('sem trava — hoje', CORPOS, 1.0),
        (f'teto 3, extras a {R:.2f} (o do campo)', 3, R),
        ('teto 3, extras a metade (o `Estilhaço`)', 3, MEIO),
        ('teto 2, extras a metade', 2, MEIO),
        ('teto 3, sem desconto', 3, 1.0),
        ('teto 2, sem desconto', 2, 1.0)]
for rot, teto, frac in opts:
    d = g * (1 + (teto - 1) * frac)
    print(f'  {rot:<38}{d:>14.0f}{d/VIDA_PC20:>17.0%}{("SIM" if d >= VIDA_PC20 else "não"):>9}')
print()
print('  >> e o efeito no ENXAME inteiro: com teto 3 e 4 personagens, os 8 corpos ainda')
print('     entregam tudo — eles so nao podem CONCENTRAR. O dano total do enxame nao muda')
print('     enquanto houver alvo pra todo mundo.')


bloco('6. ⚠ E O `tamanho` PIOROU ISSO EM 10/09')
mtam = [ln for ln in ler(TAMDEC, BEST).split('\n')
        if re.match(r'\| \*\*`Grande`\*\* \| `[\d,]+ m` \|', ln)]
print()
print('  A saída `F` do item 16 deu ao `Grande` "o alvo + metade em 1 vizinho", de graça.')
print(f'  {mtam[0].strip() if mtam else "(linha do Grande)"}')
print()
print(f'  {"":<34}{"alvos atingidos":>17}{"dano total":>13}{"vs 1 PC":>10}')
print('  ' + '-' * 76)
for rot, teto, frac, viz in (('8 capangas Médio, sem trava', CORPOS, 1.0, 0),
                             ('8 capangas Grande, sem trava', CORPOS, 1.0, 1),
                             ('8 capangas Grande, teto 3 + metade', 3, MEIO, 1)):
    corpos_ef = min(teto, CORPOS)
    dano_alvo = g * (1 + (corpos_ef - 1) * frac)
    respingo = g * 0.5 * viz * corpos_ef
    print(f'  {rot:<34}{corpos_ef*(1+viz):>17}{dano_alvo+respingo:>13.0f}'
          f'{(dano_alvo+respingo)/VIDA_PC20:>9.0%}')
print()
print('  >> um `Capanga` `Grande` sem trava e' + ' o pior caso do bestiario inteiro.')

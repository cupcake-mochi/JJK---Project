#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
O `Capanga` NA VARREDURA DA BANDA — item 17 da fila.

Ele ficou de fora de tres varreduras seguidas porque a tabela dele na `TABELA.md`
tem outro formato de coluna (`vida de um` / `pool dos 8` / `golpe de um`, sem
`dano/rod` e sem `ações`). "Nao e passou: e nao medido."

Este script le a tabela dele no formato dele, poe ele lado a lado com as outras
quatro, e roda tres coisas que nunca foram rodadas:

  1. a fatia do `o golpe` dele contra a banda — e contra a fatia PUBLICADA na escada
  2. de onde vem o topo `32%` da banda
  3. os seis papeis no `Capanga`, contra a trava que define ele: cai num golpe
  4. a luta inteira com fogo concentrado, papel a papel

Nenhum numero mora aqui dentro: cada ancora e lida do documento dono, e o script
morre se o dono mudar.
"""
import math
import os
import re
import sys

BEST = os.environ.get('JJK_BEST', '/media/mizuki/HD Externo II/Claude/Claude 2/bestiario')

TABELA = '04-fase-1/TABELA.md'
ESCADA = '04-fase-1/a-escada-com-numero.md'
BARATA = '04-fase-1/fila/DECIDIDO-o-capanga.md'   # a banda mudou de dono em 10/09
INTERV = '04-fase-1/fila/MEDIDA-a-intervencao.md'
BLOCO = '03-bloco/RASCUNHO-5-o-bloco-em-branco.md'
CAPANGA = '04-fase-1/o-capanga-contra-os-outros-sistemas.md'
CONTROL = '04-fase-1/papel/DECIDIDO-o-controlador-por-categoria.md'
ANCORAS = '05-sukuna/ANCORAS-do-repositorio.md'

_cache = {}


def ler(rel):
    if rel not in _cache:
        with open(os.path.join(BEST, rel), encoding='utf-8') as f:
            _cache[rel] = f.read()
    return _cache[rel]


def n(s):
    return float(s.replace('−', '-').replace(',', '.'))


def pega(rel, padrao, rotulo):
    m = re.search(padrao, ler(rel))
    if not m:
        print(f'\n  !! ANCORA PERDIDA: {rotulo}\n     nao casa em {rel}\n     padrao: {padrao}')
        sys.exit(1)
    return m


def media_dado(e):
    e = e.strip()
    m = re.match(r'(\d+)d(\d+)(?:\s*\+\s*(\d+))?$', e)
    if m:
        return int(m.group(1)) * (1 + int(m.group(2))) / 2 + int(m.group(3) or 0)
    return float(e) if re.match(r'^\d+$', e) else None


def bloco(t):
    print()
    print('=' * 96)
    print(t)
    print('=' * 96)


NIVEIS = [2, 10, 20, 30]
ORDEM = ['Capanga', 'Ameaça', 'Desastre', 'Catástrofe', 'Calamidade']

# ---------------------------------------------------------------- as ancoras
FATOR_INT = n(pega(INTERV, r'o fator de dano de quem tem `Intervenção` é \*\*`([\d,]+)`\*\*',
                   'o fator da `Intervenção`').group(1))
mb = pega(BARATA, r'A banda do `o golpe` vira \*\*`([\d,]+)%`–`([\d,]+)%`\*\*', 'a banda NOVA — dono: DECIDIDO-o-capanga §1')
PISO, TETO = n(mb.group(1)) / 100, n(mb.group(2)) / 100
mv = pega(ESCADA, r'A banda inteira é de `([\d,]+)%` a `([\d,]+)%`', 'a banda VELHA da escada')
PISO_V, TETO_V = n(mv.group(1)) / 100, n(mv.group(2)) / 100

# o fator de dano do `Capanga` — ele aparece DUAS vezes na escada, e diferente
FAT_MORTO = n(pega(ESCADA, r'\| \*\*`Capanga`\*\* \| — \| `0,25` \| `([\d,]+)` \| `1` \|',
                   'o fator de dano da tabela MORTA').group(1))
FAT_VIVO = n(pega(ESCADA,
                  r'\| \*\*`Capanga`\*\* \| — \| `dano do grupo ÷ 4` \| `([\d,]+)` \| `1` \| `(\d+)`',
                  'o fator de dano da escada FECHADA').group(1))
CORPOS = int(pega(ESCADA,
                  r'\| \*\*`Capanga`\*\* \| — \| `dano do grupo ÷ 4` \| `[\d,]+` \| `1` \| `(\d+)`',
                  'os corpos').group(1))
TRAVA = pega(CAPANGA, r'\*\*Trava:\*\* \*o `Capanga` (cai num golpe de um jogador)\.\*',
             'a trava do um-golpe').group(1)
RAZAO_PUB = {}
for _ln in ler(CAPANGA).split('\n'):
    _m = re.match(r'\| (\d+) \| `\d+` \| `\d+` \| `\d+` \| `([\d,]+) ×` \| `(\d+)` \|', _ln)
    if _m:
        RAZAO_PUB[int(_m.group(1))] = (n(_m.group(2)), int(_m.group(3)))
if len(RAZAO_PUB) < 4:
    print(f'  !! ANCORA PERDIDA: a razao publicada por nivel — li {sorted(RAZAO_PUB)}')
    sys.exit(1)

# quem tem `Intervenção`, lido do bloco
TEM_INT = {}
for ln in ler(BLOCO).split('\n'):
    m = re.match(r'\| \*{0,2}`(\w+)`\*{0,2} \| .* \| \*{0,2}(sim|não)\*{0,2} \|$', ln)
    if m:
        TEM_INT[m.group(1)] = (m.group(2) == 'sim')

# os seis papeis, lidos do bloco: quanto cada um mexe na VIDA
PAPEIS = {}
for ln in ler(BLOCO).split('\n'):
    m = re.match(r'\| \*\*`(\w+)`\*\* \| (.+?) \| (.+?) \| `1,000` \|$', ln)
    if not m:
        continue
    nome, ganha, paga = m.group(1), m.group(2), m.group(3)
    mv2 = re.search(r'vida × ([\d,]+)', ganha + ' | ' + paga)
    md = re.search(r'dano `× ([\d,]+)`', ganha + ' | ' + paga)
    PAPEIS[nome] = {'vida': n(mv2.group(1)) if mv2 else 1.0,
                    'dano': n(md.group(1)) if md else 1.0,
                    'ganha': ganha, 'paga': paga}
if len(PAPEIS) != 6:
    print(f'  !! ANCORA PERDIDA: os seis papeis — li {len(PAPEIS)} em {BLOCO}')
    sys.exit(1)

# o `Controlador` forma B numa categoria de UMA acao
mc = pega(CONTROL, r'\| `Ameaça` \| `1` \| `([\d,]+)×` \| \*\*`× ([\d,]+)`\*\*', 'a forma B em 1 ação')
CTRL_GANHA, CTRL_PAGA = n(mc.group(1)), n(mc.group(2))

# as quatro categorias de corpo unico
CATS, atual = {}, None
for ln in ler(TABELA).split('\n'):
    m = re.match(r'## `([^`]+)`', ln)
    if m:
        atual = m.group(1)
        CATS.setdefault(atual, {})
        continue
    if not atual:
        continue
    m = re.match(r'\| (\d+) \| `([^`]+)` \| `([^`]+)` \| `(\d+)` \| `([^`]+)` \|', ln)
    if m and atual != 'Capanga':
        CATS[atual][int(m.group(1))] = {
            'vida': n(m.group(2)), 'dano': n(m.group(3)),
            'acoes': int(m.group(4)), 'golpe': media_dado(m.group(5))}
    # o `Capanga` — OUTRO formato: nv | vida de um | **pool** | golpe de um | ...
    m = re.match(r'\| (\d+) \| `(\d+)` \| \*\*`(\d+)`\*\* \| `([^`]+)` \|', ln)
    if m and atual == 'Capanga':
        CATS['Capanga'][int(m.group(1))] = {
            'vida': n(m.group(2)), 'pool': n(m.group(3)),
            'acoes': 1, 'golpe': media_dado(m.group(4))}
for c in ORDEM:
    if len(CATS.get(c, {})) < 29:
        print(f'  !! ANCORA PERDIDA: a tabela do `{c}` — li {len(CATS.get(c, {}))} linhas')
        sys.exit(1)

# a fatia PUBLICADA, por nivel — e a vida de um personagem, derivada dela
cab = pega(ESCADA, r'\| nv \| (`[^\n]+)', 'o cabeçalho da tabela de fatia')
ORDEM_FATIA = re.findall(r'`([^`]+)`', cab.group(1))
FATIA_PUB, VIDA_PC = {}, {}
for nv in NIVEIS:
    mf = pega(ESCADA, r'\| ' + str(nv) + r' \| ((?:`[\d,]+%` \| ?)+)', f'a fatia do nv{nv}')
    FATIA_PUB[nv] = {c: n(v) / 100 for c, v in
                     zip(ORDEM_FATIA, re.findall(r'`([\d,]+)%`', mf.group(1)))}
    VIDA_PC[nv] = CATS['Desastre'][nv]['golpe'] / FATIA_PUB[nv]['Desastre']

# o dano do grupo por rodada — o manual, colado nas ANCORAS
GRUPO = {}
for ln in ler(ANCORAS).split('\n'):
    m = re.match(r'\| \*{0,2}(\d+)\*{0,2} \| \*{0,2}~(\d+)\*{0,2} \| \*{0,2}\d+ a \d+', ln)
    if m:
        GRUPO[int(m.group(1))] = float(m.group(2))
if not all(nv in GRUPO for nv in NIVEIS):
    print(f'  !! ANCORA PERDIDA: o dano do grupo por rodada — li {sorted(GRUPO)}')
    sys.exit(1)


bloco('AS ANCORAS — todas lidas do dono')
print(f'  a banda NOVA                    {PISO:.0%} – {TETO:.0%}           DECIDIDO-o-capanga §1')
print(f'  a banda VELHA da escada         {PISO_V:.0%} – {TETO_V:.0%}           a-escada-com-numero')
print(f'  o fator da `Intervenção`        × {FATOR_INT:.3f}            MEDIDA-a-intervencao §12')
print(f'  o fator de dano do `Capanga`    × {FAT_MORTO:.2f}  na tabela do TOPO da escada')
print(f'                                  × {FAT_VIVO:.2f}  na escada FECHADA, embaixo')
print(f'  corpos                          {CORPOS}')
print(f'  a trava que define ele          "{TRAVA}"')
print('  a razão publicada do enxame     ' +
      ' · '.join(f'nv{k} {v[0]:.2f}×' for k, v in sorted(RAZAO_PUB.items())) +
      '   o-capanga-contra-os-outros-sistemas')
print(f'  o `Controlador` forma B em 1 ação   ganha {CTRL_GANHA:.3f}× · paga vida × {CTRL_PAGA:.3f}')
print()
print(f'  {"nv":>4}{"vida de 1 PC":>16}{"dano do grupo/rod":>21}{"vida de 1 capanga":>20}'
      f'{"pool dos "+str(CORPOS):>14}')
for nv in NIVEIS:
    c = CATS['Capanga'][nv]
    print(f'  {nv:>4}{VIDA_PC[nv]:>16.1f}{GRUPO[nv]:>21.0f}{c["vida"]:>20.0f}{c["pool"]:>14.0f}')


# =============================================================== 1
bloco('1. A FATIA DO `Capanga` — a recomputada contra a PUBLICADA')
print()
print('  A fatia = `o golpe` de UM corpo dividido pela vida de UM personagem. E a mesma metrica')
print('  das outras quatro, e e a que a banda vigia.')
print()
print(f'  {"nv":>4}{"golpe de 1":>13}{"fatia recomputada":>21}{"fatia PUBLICADA":>19}'
      f'{"bate?":>9}{"na banda "+f"{PISO:.0%}–{TETO:.0%}":>19}')
print('  ' + '-' * 86)
desvios = []
for nv in NIVEIS:
    c = CATS['Capanga'][nv]
    f = c['golpe'] / VIDA_PC[nv]
    pub = FATIA_PUB[nv]['Capanga']
    bate = abs(f - pub) < 0.01
    if not bate:
        desvios.append((nv, f, pub))
    dentro = PISO <= f <= TETO
    print(f'  {nv:>4}{c["golpe"]:>13.1f}{f:>20.1%}{pub:>19.0%}{("sim" if bate else "NAO"):>9}'
          f'{("sim" if dentro else "NAO"):>19}')
print()
if desvios:
    r = desvios[-1][2] / desvios[-1][1]
    print(f'  >> A tabela do `Capanga` e a fatia publicada dele NAO batem. A razao entre as duas')
    print(f'     e {r:.3f} — e {FAT_MORTO:.2f} / {FAT_VIVO:.2f} = {FAT_MORTO/FAT_VIVO:.3f}.')
    print()
    print(f'  >> A fatia publicada foi calculada com o fator de dano `{FAT_MORTO:.2f}`, que e o da')
    print(f'     tabela do TOPO da escada — a que a propria escada substituiu embaixo por `{FAT_VIVO:.2f}`.')
    print(f'     A `TABELA.md` implementa o `{FAT_VIVO:.2f}`. A linha de fatia ficou na versao morta.')
else:
    print('  >> a fatia publicada bate com a tabela. Nada a corrigir.')


# =============================================================== 2
bloco('2. DE ONDE VEM O TOPO DA BANDA')
print()
print('  A banda e o intervalo em que `o golpe` de todas as categorias cai. Quem esta no topo?')
print()
print(f'  nv20, com o fator da `Intervenção` aplicado em quem tem:')
print()
print(f'  {"categoria":<14}{"golpe cru":>11}{"tem Int?":>10}{"golpe efetivo":>15}{"fatia":>10}')
print('  ' + '-' * 60)
tab = []
for c in ORDEM:
    b = CATS[c][20]
    g = b['golpe'] * (FATOR_INT if TEM_INT.get(c) else 1.0)
    tab.append((c, g / VIDA_PC[20]))
    print(f'  {c:<14}{b["golpe"]:>11.1f}{("sim" if TEM_INT.get(c) else "não"):>10}'
          f'{g:>15.1f}{g/VIDA_PC[20]:>10.1%}')
alto = max(tab, key=lambda x: x[1])
baixo = min(tab, key=lambda x: x[1])
print()
print(f'  >> o TOPO real e o `{alto[0]}`, em {alto[1]:.1%}. O PISO real e o `{baixo[0]}`, em {baixo[1]:.1%}.')
print(f'  >> a banda publicada e {PISO:.0%}–{TETO:.0%}. Sobra {TETO-alto[1]:.1%} de teto que ninguem alcanca.')
print()
print(f'  E o `{TETO_V:.0%}` da banda velha? nv2, com a fatia publicada de cada um:')
print('   ', '  '.join(f'{c} {FATIA_PUB[2][c]:.0%}' for c in ORDEM))
topo_pub = max(FATIA_PUB[2], key=lambda c: FATIA_PUB[2][c])
print(f'  >> o topo `{TETO_V:.0%}` e o `{topo_pub}` no nv2 — e ele foi calculado com o fator MORTO.')
print(f'     Recomputado com o `{FAT_VIVO:.2f}` que a `TABELA.md` implementa, o `Capanga` nv2 da '
      f'{CATS["Capanga"][2]["golpe"]/VIDA_PC[2]:.1%}.')


# =============================================================== 3
bloco('3. OS SEIS PAPEIS NO `Capanga` — contra a trava que define ele')
print()
print(f'  A trava: o `Capanga` "{TRAVA}". A vida dele NAO e um fator da vida do chefe —')
print(f'  ela e `dano do grupo ÷ 4`, que e exatamente o que UM jogador entrega numa rodada.')
print()
print('  Entao vida x m com m > 1,0 quer dizer: ele para de cair num golpe.')
print()
print(f'  nv20 — a vida de um capanga e {CATS["Capanga"][20]["vida"]:.0f} e um jogador entrega '
      f'{GRUPO[20]/4:.0f} por rodada.')
print()
print(f'  {"papel":<14}{"vida ×":>9}{"vida de 1":>11}{"golpes p/ cair":>16}{"a trava":>12}   o que ele paga')
print('  ' + '-' * 96)
ordem_p = ['Brutamontes', 'Guardião', 'Artilheiro', 'Emboscador', 'Controlador', 'Apoio']
um_pc = GRUPO[20] / 4
for p in ordem_p:
    d = PAPEIS[p]
    m = d['vida']
    if p == 'Controlador':
        m = CTRL_PAGA   # a forma B: em 1 acao ele paga vida, nao dano
    v = CATS['Capanga'][20]['vida'] * m
    golpes = v / um_pc
    ok = 'INTEIRA' if golpes <= 1.0001 else 'QUEBRA'
    nota = d['paga'] if 'vida' in d['paga'] else d['ganha']
    if p == 'Controlador':
        nota = f'forma B em 1 ação: vida × {CTRL_PAGA:.3f}'
    print(f'  {p:<14}{m:>9.3f}{v:>11.1f}{golpes:>16.2f}{ok:>12}   {re.sub(r"[`*]", "", nota)[:44]}')
print()
print('  >> A moeda dos seis papeis e VIDA. Num corpo unico ela e continua: 20% a mais de vida e')
print('     20% mais de luta. No `Capanga` ela e um DEGRAU: abaixo de um golpe nao muda nada,')
print('     acima de um golpe DOBRA o corpo.')


# =============================================================== 4
bloco('4. A LUTA INTEIRA, COM FOGO CONCENTRADO — papel a papel')


def simular(nv, mult_vida=1.0, mult_dano=1.0, corpos=CORPOS):
    """O enxame em pool contra 4 jogadores que concentram fogo. Devolve
    (dano total do enxame, rodadas)."""
    c = CATS['Capanga'][nv]
    # a escada define a vida como `dano do grupo ÷ 4`. A `TABELA.md` IMPRIME ela
    # arredondada; o sim usa a formula, senao um resto de 2 pontos inventa uma rodada.
    vida_um = (GRUPO[nv] / 4) * mult_vida
    pool = corpos * vida_um
    golpe = c['golpe'] * mult_dano
    d, total, rod = GRUPO[nv], 0.0, 0
    while pool > 0 and rod < 20:
        rod += 1
        vivos = min(corpos, math.ceil(pool / vida_um))
        total += vivos * golpe
        pool -= d
    return total, rod


def chefe(nv):
    b = CATS['Desastre'][nv]
    rod = b['vida'] / GRUPO[nv]
    return b['dano'] * rod, rod


print()
print('  Primeiro: o modelo reproduz o numero publicado?')
print()
print(f'  {"nv":>4}{"enxame":>10}{"chefe":>10}{"razão":>9}{"publicado":>12}'
      f'{"rodadas":>10}{"pub":>6}{"vida impressa":>16}{"a fórmula":>12}')
print('  ' + '-' * 92)
bateu = 0
for nv in NIVEIS:
    e, r = simular(nv)
    ch, rc = chefe(nv)
    pr, prod = RAZAO_PUB[nv]
    ok = abs(e / ch - pr) <= 0.015 and r == prod
    bateu += ok
    print(f'  {nv:>4}{e:>10.0f}{ch:>10.0f}{e/ch:>9.2f}{pr:>12.2f}{r:>10.0f}{prod:>6}'
          f'{CATS["Capanga"][nv]["vida"]:>16.0f}{GRUPO[nv]/4:>12.2f}')
print()
print(f'  >> o modelo reproduz {bateu} de {len(NIVEIS)} niveis, razao E rodadas.')
print(f'  >> e ele so reproduz usando a FORMULA `dano do grupo ÷ 4`. Com a vida IMPRESSA na')
print(f'     `TABELA.md` o nv30 inventa uma terceira rodada, porque `79` arredonda `78,75`')
print(f'     pra cima e sobram 2 pontos de pool que mantem um corpo vivo.')
print()
print('  Agora os seis papeis, no nv20. O papel mexe na vida de cada corpo — e a vida de um')
print('  enxame E a duracao dele, e a duracao multiplica TUDO que ele entrega.')
print()
print(f'  {"papel":<14}{"vida ×":>9}{"dano do enxame":>17}{"razão vs chefe":>17}'
      f'{"rodadas":>10}{"desvio":>10}')
print('  ' + '-' * 78)
base, _ = simular(20)
ch20, _ = chefe(20)
print(f'  {"— sem papel —":<14}{1.0:>9.3f}{base:>17.0f}{base/ch20:>17.2f}{simular(20)[1]:>10.0f}'
      f'{0.0:>10.1%}')
for p in ordem_p:
    d = PAPEIS[p]
    mv3 = CTRL_PAGA if p == 'Controlador' else d['vida']
    md3 = 1.0 if p == 'Controlador' else d['dano']
    e, r = simular(20, mult_vida=mv3, mult_dano=md3)
    print(f'  {p:<14}{mv3:>9.3f}{e:>17.0f}{e/ch20:>17.2f}{r:>10.0f}{e/base-1:>10.1%}')
print()
print('  >> O invariante dos seis papeis e `produto 1,000` — cada um devolve em vida o que')
print('     leva em outro eixo. Num corpo unico isso fecha. Num enxame de', CORPOS, 'nao:')
print('     a vida entra DUAS vezes, uma no corpo e outra na duracao.')


# =============================================================== 5
bloco('5. O `Controlador` NO ESQUADRAO — `ações` de quem?')
print()
print('  A forma B preca o `Controlador` assim: negar 1 acao do grupo vale 1 acao DELE, entao')
print(f'  ele ganha (1 + 1/ações) e paga vida x 1/(1 + 1/ações).')
print()
print(f'  A escada publica `ações = 1` pro `Capanga`. Mas isso e por CORPO, e ele vem em {CORPOS}.')
print()
acoes_corpo = CATS['Capanga'][20]['acoes']
acoes_esq = acoes_corpo * CORPOS
print(f'  {"leitura":<28}{"ações":>7}{"ganha":>10}{"paga vida":>12}{"produto":>10}'
      f'{"dano do enxame":>17}{"razão":>9}')
print('  ' + '-' * 94)
for rot, a in ((f'por CORPO — `ações = {acoes_corpo}`', acoes_corpo),
               (f'por ESQUADRÃO — {CORPOS} corpos', acoes_esq)):
    ganha, paga = 1 + 1 / a, 1 / (1 + 1 / a)
    e, r = simular(20, mult_vida=paga)
    print(f'  {rot:<28}{a:>7}{ganha:>10.3f}{paga:>12.3f}{ganha*paga:>10.3f}{e:>17.0f}{e/ch20:>9.2f}')
print()
ganha1, paga1 = 1 + 1 / acoes_corpo, 1 / (1 + 1 / acoes_corpo)
print(f'  >> As duas fecham em 1,000 no invariante. Mas a leitura por CORPO manda o esquadrao')
print(f'     pra {simular(20, mult_vida=paga1)[0]/ch20:.2f} x do chefe, e a por ESQUADRAO deixa em '
      f'{simular(20, mult_vida=1/(1+1/acoes_esq))[0]/ch20:.2f} x.')
print(f'  >> E a conta de "quantas acoes o grupo perde" e a mesma nos dois: UMA. O que muda e')
print(f'     quanto isso vale — 1 de {acoes_corpo} ou 1 de {acoes_esq}.')


# =============================================================== 6
bloco('6. A BANDA REAL — varrida nos 29 níveis das CINCO categorias')
print()
print('  A varredura que fechou a banda olhou 3 niveis e 4 categorias, e o `Capanga` ficou de fora.')
print('  Esta olha 29 x 5, com o fator da `Intervenção` aplicado em quem tem.')
print()
TODOS = sorted(CATS['Desastre'])
# a vida do PC so tem ancora nos 4 niveis publicados; interpolo pela razao golpe/fatia do Desastre
VPC = dict(VIDA_PC)
for nv in TODOS:
    if nv in VPC:
        continue
    ref = min(NIVEIS, key=lambda k: abs(k - nv))
    VPC[nv] = CATS['Desastre'][nv]['golpe'] / FATIA_PUB[ref]['Desastre']
todas = []
for c in ORDEM:
    for nv in TODOS:
        g = CATS[c][nv]['golpe'] * (FATOR_INT if TEM_INT.get(c) else 1.0)
        todas.append((g / VPC[nv], c, nv))
todas.sort()
print(f'  {"categoria":<14}{"mínimo":>10}{"onde":>8}{"máximo":>10}{"onde":>8}')
print('  ' + '-' * 52)
for c in ORDEM:
    so = [t for t in todas if t[1] == c]
    print(f'  {c:<14}{so[0][0]:>10.1%}{"nv"+str(so[0][2]):>8}{so[-1][0]:>10.1%}{"nv"+str(so[-1][2]):>8}')
print('  ' + '-' * 52)
print(f'  {"TODAS":<14}{todas[0][0]:>10.1%}{"nv"+str(todas[0][2]):>8}'
      f'{todas[-1][0]:>10.1%}{"nv"+str(todas[-1][2]):>8}')
print(f'  {"":<14}{"("+todas[0][1]+")":>10}{"":>8}{"("+todas[-1][1]+")":>10}')
print()
print(f'  >> a banda MEDIDA e {todas[0][0]:.1%} – {todas[-1][0]:.1%}.')
print(f'  >> a publicada e {PISO:.0%} – {TETO:.0%}. Ela sobra {todas[0][0]-PISO:.1%} embaixo e '
      f'{TETO-todas[-1][0]:.1%} em cima.')
print()
print(f'  E arredondando pra numero redondo, como a escada faz: **{math.floor(todas[0][0]*100):.0f}% '
      f'– {math.ceil(todas[-1][0]*100):.0f}%**.')


# =============================================================== 7
bloco('7. E SE O PAPEL PAGASSE EM CORPOS, E NAO EM VIDA?')
print()
print('  A moeda dos seis e VIDA. Num enxame vida e duracao, e duracao multiplica tudo o que')
print('  ele entrega. CORPOS seria a moeda natural do enxame — e ela nao encosta no "cai num')
print('  golpe" que DEFINE o `Capanga`. Ela serve?')
print()
alvo = base / ch20
print(f'  {"corpos":>8}{"vs os "+str(CORPOS):>10}{"dano do enxame":>17}{"razão":>9}'
      f'{"vs sem papel":>15}{"rodadas":>10}')
print('  ' + '-' * 70)
for k in range(4, 13):
    e, r = simular(20, corpos=k)
    print(f'  {k:>8}{k/CORPOS-1:>10.1%}{e:>17.0f}{e/ch20:>9.2f}{e/base-1:>15.1%}{r:>10.0f}')
print()
e9 = simular(20, corpos=CORPOS + 1)[0]
print(f'  >> UM corpo a mais e {1/CORPOS:+.1%} de corpos e {e9/base-1:+.1%} de encontro.')
print(f'     A moeda dobra no caminho, pela mesma razao que a vida dobra: mais corpo e mais')
print(f'     rodada, e mais rodada e mais tudo.')
print()
pedidos = sorted(abs(1 - (CTRL_PAGA if pp == 'Controlador' else PAPEIS[pp]['vida']))
                 for pp in ordem_p if abs((CTRL_PAGA if pp == 'Controlador' else PAPEIS[pp]['vida']) - 1) > 1e-9)
print(f'  >> e os seis papeis pedem ajustes de {min(pedidos):.1%} a {max(pedidos):.1%}. O MENOR')
print(f'     degrau que corpos sabe fazer e {e9/base-1:.1%}.')
print(f'  >> Entao pagar em corpos nao resolve: a moeda e grossa demais, e ela erra pro mesmo')
print(f'     lado que a vida erra.')


bloco('O VEREDITO')
print()
n_fora = sum(1 for nv in NIVEIS if not (PISO <= CATS['Capanga'][nv]['golpe'] / VIDA_PC[nv] <= TETO))
print(f'  1. `o golpe` do `Capanga` esta DENTRO da banda em {len(NIVEIS)-n_fora} de {len(NIVEIS)} niveis.')
print(f'     Ele nao era o problema. O problema e que a fatia PUBLICADA dele esta errada.')
print()
print(f'  2. O topo `{TETO_V:.0%}` da banda velha e o `Capanga` no nv2, calculado com o fator MORTO')
print(f'     de `{FAT_MORTO:.2f}`. Com o `{FAT_VIVO:.2f}` que a `TABELA.md` implementa, ninguem')
print(f'     encosta em {TETO:.0%}: o topo real e {alto[1]:.1%}.')
print()
print('  3. Os papeis que pagam em VIDA nao sao neutros no `Capanga`, e o desvio esta acima.')
print()
print(f'  4. E o item 17 da `A-FILA.md` cita o fator MORTO: "ele tem fator de dano proprio')
print(f'     (`0,33` contra `0,25` de vida)". A escada fechada diz `{FAT_VIVO:.2f}`, e a')
print(f'     `TABELA.md` implementa `{FAT_VIVO:.2f}`. O `Capanga` E uma `Ameaça` com outra vida.')

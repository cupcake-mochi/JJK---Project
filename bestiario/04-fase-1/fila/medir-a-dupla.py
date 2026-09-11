# -*- coding: utf-8 -*-
"""MEDIDA — o remapeamento das SEIS PRONTAS, e o martelo da `Dupla`.

O `medir-as-seis-prontas.py` (o 26º) mediu que `6` de `6` estão na escada MORTA.
Este mede a coisa seguinte: PARA ONDE cada uma vai, e o que fazer com a `Dupla`.

O `ESTADO-onde-paramos.md` publica a leitura "`Ronda` ⟹ `Ameaça` e `Alcateia` ⟹
`Capanga` saem sozinhos". Este script NÃO supõe isso: ele lê as duas escadas nos
documentos DONOS e cruza por IDENTIDADE — pessoas, fator e ações —, e depois
confere célula a célula contra a `TABELA.md` nos 29 níveis.

  §0  as âncoras, todas lidas do dono
  §1  o cruzamento por identidade — quem herda quem
  §2  a conferência célula a célula, 29 níveis × 4 colunas
  §3  ⚠ a leitura publicada `Alcateia ⟹ Capanga`, medida
  §4  ⚠ a armadilha do nome `Calamidade`
  §5  a `Dupla` — as saídas, com o simulador de encontro generalizado
  §6  ⚠ a BANDA do `o golpe` — a métrica que a escada diz ter pegado a `Dupla`
  §7  ⚠ o orçamento de feitiço, e a `Kitsune` que conjura
  §8  a grade que produziu o número SEIS, rodada na escada viva
  §9  a varredura do `gerador-inimigo/` — quantas linhas falam a escada morta

O simulador do §5 é o do item `9`, generalizado pra N corpos. Antes de qualquer
conclusão ele reproduz DUAS âncoras que não calibrou — o `68%` do §4.5 e o
`0,75×`–`0,77×` do §4.3 — e morre se não reproduzir.

⚠ Este script NÃO escreve nada no `Claude 2`. Ele só LÊ.

Nenhum número mora aqui dentro: cada âncora é lida do documento dono, e o script
morre se o dono mudar.
"""
import math
import os
import re
import statistics as st
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
BEST = os.path.dirname(os.path.dirname(AQUI))
REPO = os.environ.get('JJK_REPO', '/media/mizuki/HD Externo II/Claude/Claude 2')

P26 = os.path.join(REPO, 'sistema/03-mecanica/26-bestiario.md')
DADOS = os.path.join(REPO, 'sistema/05-material/gerador-inimigo/dados.js')
TAB = os.path.join(BEST, '04-fase-1', 'TABELA.md')
R5 = os.path.join(BEST, '03-bloco', 'RASCUNHO-5-o-bloco-em-branco.md')
DEG = os.path.join(BEST, '04-fase-1', 'fila', 'DECIDIDO-o-degrau.md')
CAPU = os.path.join(BEST, '04-fase-1', 'fila', 'DECIDIDO-o-capanga-unico.md')
CAPD = os.path.join(BEST, '04-fase-1', 'fila', 'DECIDIDO-o-capanga.md')
ESC = os.path.join(BEST, '04-fase-1', 'a-escada-com-numero.md')
# ⚠ A escada MORTA saiu da peça 26 na v0.221 e não vive em documento nenhum do
# repositório. Este laudo mede a TRANSIÇÃO, então ele lê a peça velha do museu —
# cópia byte a byte do commit `fc1cb79`, o último antes da troca. Só a escada morta
# e as duas tabelas dela (§4.1 e §4.4) saem dali; a VIVA sai dos donos de sempre.
P26_MORTA = os.path.join(BEST, '04-fase-1', 'museu', 'a-peca-26.v0.220.md')


def ler(p):
    if not os.path.exists(p):
        sys.exit('DONO SUMIU: %s' % p)
    return open(p, encoding='utf-8').read()


def exige(c, m):
    if not c:
        sys.exit('✗ ÂNCORA PERDIDA: ' + m)


def num(s):
    return float(s.replace('−', '-').replace(',', '.'))


# ═══════════════════════════════════════════ as fórmulas do `make.js`, portadas
# ⚠ meio para BAIXO — peça 26 §4.1 declara a regra porque 22 de 56 células caem
#   exatamente em ,5. `Math.ceil(x - 0.5)` é o que o gerador roda.
def arred(x):
    return math.ceil(x - 0.5)


def acoes(pes):
    return max(1, pes - 1)


DADOS_LADOS = [4, 6, 8, 10, 12]


def dado(alvo):
    """A tradução de dano em dado — peça 26 §4.4, v0.216 (d4 a d12, teto 8 dados)."""
    if alvo < 5:
        return str(arred(alvo))
    meta = alvo / 2
    bom = None
    for d in DADOS_LADOS:
        med_ = (d + 1) / 2
        n = max(1, round(meta / med_))
        if n > 8:
            continue
        fixo = alvo - n * med_
        if fixo < 0:
            continue
        inteiro = 0 if abs(fixo - round(fixo)) < 1e-9 else 1
        erro = abs(n * med_ - meta)
        if (bom is None or inteiro < bom['inteiro']
                or (inteiro == bom['inteiro'] and erro < bom['erro'] - 1e-9)
                or (inteiro == bom['inteiro'] and abs(erro - bom['erro']) < 1e-9
                    and n < bom['n'])):
            bom = {'inteiro': inteiro, 'erro': erro, 'n': n, 'd': d,
                   'fixo': round(fixo)}
    if bom is None:
        n = max(1, round(alvo / 9))
        m = arred(alvo - 4.5 * n)
        return '%dd8 + %d' % (n, m) if m > 0 else '%dd8' % n
    return ('%dd%d + %d' % (bom['n'], bom['d'], bom['fixo'])
            if bom['fixo'] > 0 else '%dd%d' % (bom['n'], bom['d']))


def golpe(dano_rodada, fator, pes):
    return dado(arred(dano_rodada * fator) / acoes(pes))


def media_dado(e):
    m = re.match(r'(\d+)d(\d+)(?:\s*\+\s*(\d+))?$', e.strip())
    if m:
        return int(m.group(1)) * (1 + int(m.group(2))) / 2 + int(m.group(3) or 0)
    return float(e) if re.match(r'^\d+$', e.strip()) else None


# ═══════════════════════════════════════════ §0 · AS ÂNCORAS
print('=' * 92)
print('§0 · AS ÂNCORAS — todas lidas do documento DONO')
print('=' * 92)

t26 = ler(P26)

t26morta = ler(P26_MORTA)
exige('| **`Dupla`** | 2 | `× 0,50` | `1` |' in t26morta,
      'a cópia de museu da peça 26 não traz mais a escada morta — regere do git '
      '(`git show fc1cb79:sistema/03-mecanica/26-bestiario.md`)')

# a escada MORTA, no §4 da peça 26 da v0.220 (museu)
MORTA = {}
for ln in t26morta.split('\n'):
    m = re.match(r'\|\s*\*{0,2}`(\w+)`\*{0,2}\s*\|\s*(\d+)\s*\|\s*`× ([\d,]+)`\s*\|\s*`(\d+)`\s*\|', ln)
    if m:
        MORTA[m.group(1)] = dict(pessoas=int(m.group(2)), fator=num(m.group(3)),
                                 acoes=int(m.group(4)))
exige(len(MORTA) == 4, 'a tabela do §4 da peça 26 mudou de forma (li %d linhas)' % len(MORTA))
print('  escada MORTA (peça 26 §4, museu da v0.220): ' + ' · '.join(
    '%s %dp %.2f %da' % (k, v['pessoas'], v['fator'], v['acoes']) for k, v in MORTA.items()))

# a escada VIVA, no RASCUNHO-5 Passo 1
t5 = ler(R5)
VIVA = {}
for ln in t5.split('\n'):
    m = re.match(r'\|\s*\*{0,2}`(\w+)`\*{0,2}\s*\|\s*([^|]*?)\s*\|[^|]*\|\s*`?([\d,]+)`?\s*\|'
                 r'\s*`?(\d+)`?\s*\|\s*`?(\d+)`?', ln)
    if m and m.group(1) in ('Capanga', 'Ameaça', 'Desastre', 'Catástrofe', 'Calamidade'):
        pes = m.group(2).strip().strip('*').strip('`')
        mp = re.match(r'^`?(\d+)`?', pes)          # "`4` — a mesa padrão" ⟹ 4
        pes = int(mp.group(1)) if mp else None
        VIVA[m.group(1)] = dict(pessoas=pes, fator=num(m.group(3)),
                                acoes=int(m.group(4)), corpos=int(m.group(5)))
exige(len(VIVA) == 5, 'a escada do Passo 1 do RASCUNHO-5 mudou de forma (li %d)' % len(VIVA))
print('  escada VIVA  (RASCUNHO-5 P1): ' + ' · '.join(
    '%s %s %.2f %da %dc' % (k, ('%dp' % v['pessoas']) if v['pessoas'] else '—',
                            v['fator'], v['acoes'], v['corpos']) for k, v in VIVA.items()))

# a ficha pronta do §4.1 e o golpe do §4.4 — as duas tabelas da peça MORTA
F41 = {}
for ln in t26morta.split('\n'):
    m = re.match(r'\|\s*`(\w+)`\s*\|\s*`(\d+)`(?: vida)? · `(\d+)`(?: dano)?\s*\|'
                 r'\s*`(\d+)` · `(\d+)`\s*\|\s*`(\d+)` · `(\d+)`\s*\|', ln)
    if m and m.group(1) in MORTA:
        F41[m.group(1)] = {10: (int(m.group(2)), int(m.group(3))),
                           20: (int(m.group(4)), int(m.group(5))),
                           30: (int(m.group(6)), int(m.group(7)))}
exige(len(F41) == 4, 'a tabela §4.1 da peça 26 sumiu (li %d linhas)' % len(F41))

F44 = {}
for ln in t26morta.split('\n'):
    m = re.match(r'\|\s*`(\w+)`\s*\|\s*`(\d+)`\s*\|\s*`(\d+)`\s*\|\s*`([\dd + ]+)`\s*\|', ln)
    if m and m.group(1) in MORTA:
        F44[m.group(1)] = (int(m.group(2)), int(m.group(3)), m.group(4).strip())
exige(len(F44) == 4, 'a tabela §4.4 da peça 26 sumiu (li %d linhas)' % len(F44))
print('  §4.1 e §4.4 da peça 26 da v0.220 lidas — %d + %d linhas' % (len(F41), len(F44)))

# as FAIXAS do gerador (o dono das seis)
tj = ler(DADOS)
FAIXAS = []
for m in re.finditer(r"\['([\d ea]+)',\s*(\d+),\s*(\d+),\s*(\d+),\s*(\d+),\s*(\d+),\s*(\d+),"
                     r"\s*(\d+),\s*(\d+)\]", tj):
    FAIXAS.append(dict(rot=m.group(1), de=int(m.group(2)), ate=int(m.group(3)),
                       classe=int(m.group(4)), grupo=int(m.group(5)),
                       chefe_vida=int(m.group(6)), chefe_dano=int(m.group(7)),
                       cap_vida=int(m.group(8)), cap_dano=int(m.group(9))))
exige(len(FAIXAS) == 7, 'as FAIXAS do `dados.js` mudaram de forma (li %d)' % len(FAIXAS))

SEIS = re.findall(r"\{\s*nome:\s*'([^']+)'\s*,\s*faixa:\s*'([^']+)'\s*,\s*categoria:\s*'([^']+)'", tj)
exige(len(SEIS) == 6, 'as PRONTAS do `dados.js` mudaram de forma (li %d)' % len(SEIS))
print('  `dados.js`: %d faixas · %d prontas' % (len(FAIXAS), len(SEIS)))

# as âncoras de encontro
VEZES = num(re.search(r'tem `(\d+) ×` o dano de rodada do grupo em vida', t26).group(1))
PCT = num(re.search(r'O chefe entrega `(\d+)%` da vida de um personagem por rodada',
                    t26).group(1)) / 100
# a escada viva trocou os nomes na v0.221: `Ronda` virou `Ameaça` e `Alcateia`,
# `Desastre` — e o §4.3 diz que o modelo do Bestiário refez a razão e deu o mesmo
m = re.search(r'\*\*Quatro `Ameaça` não valem um `Desastre`: elas cobram `([\d,]+) ×` a `([\d,]+) ×`', t26)
exige(m, 'o `0,75×`–`0,77×` do §4.3 sumiu da peça 26')
AMEACA_4 = (num(m.group(1)), num(m.group(2)))
# a fração do §4.5 passou a sair com UMA CASA na v0.221 — `67,6%`, e não `68%`:
# a própria peça diz que meio ponto percentual atravessa a borda de uma rodada
m = re.search(r'\|\s*\*\*`sozinho`\*\*\s*\|\s*`100%`\s*\|\s*—\s*\|\s*`([\d,]+)%`', t26)
exige(m, 'a linha `sozinho` do §4.5 sumiu da peça 26')
COBRA = num(m.group(1)) / 100
MESA = VIVA['Desastre']['pessoas']
print('  peça 26: chefe = %.0f× o dano do grupo em vida · entrega %.0f%% da vida de um PJ/rodada'
      % (VEZES, 100 * PCT))
print('  §4.3: quatro `Ronda` cobram %.2f×–%.2f× uma `Alcateia`  ·  §4.5: sozinho cobra %.0f%%'
      % (AMEACA_4[0], AMEACA_4[1], 100 * COBRA))

# a régua do encontro misturado, e o fator contínuo
m = re.search(r'`fator do encontro = fator do chefe \+ \(capangas × `([\d,]+)`\)`', ler(CAPU))
exige(m, 'a régua `0,083` sumiu do DECIDIDO-o-capanga-unico')
CAMBIO_CAP = num(m.group(1))
tdeg = ler(DEG)
exige('eles passam a ser RÓTULOS num contínuo' in tdeg,
      'a frase do fator contínuo sumiu do DECIDIDO-o-degrau')
exige('personagens = fator × 4' in tdeg or 'personagens = fator × 4' in t5,
      'a identidade `personagens = fator × 4` sumiu')
print('  régua do encontro: fator do chefe + capangas × %.3f  ·  fator é CONTÍNUO (item 5)'
      % CAMBIO_CAP)

# a TABELA viva, célula a célula
def secao(cat):
    t = ler(TAB)
    exige('## `%s`' % cat in t, 'a seção `%s` sumiu da TABELA' % cat)
    return t.split('## `%s`' % cat)[1].split('\n## ')[0]


def linhas(cat):
    cab, out = None, {}
    for ln in secao(cat).split('\n'):
        cels = [c.strip().strip('*').strip('`').strip('*') for c in ln.strip().strip('|').split('|')]
        if cels and cels[0] == 'nv':
            cab = cels
        elif cab and cels and re.match(r'^\d+$', cels[0] or ''):
            out[int(cels[0])] = dict(zip(cab, cels))
    return out


T = {c: linhas(c) for c in ('Ameaça', 'Desastre', 'Catástrofe', 'Calamidade', 'Capanga')}
exige(all(len(v) >= 29 for v in T.values()), 'a TABELA.md não tem os 29 níveis nas cinco seções')
NIVEIS = sorted(T['Desastre'])
print('  `TABELA.md`: %d níveis × %d categorias' % (len(NIVEIS), len(T)))


# ═══════════════════════════════════════════ §1 · O CRUZAMENTO POR IDENTIDADE
print()
print('=' * 92)
print('§1 · O CRUZAMENTO — quem herda quem, por IDENTIDADE (pessoas · fator · ações)')
print('=' * 92)
print('  %-14s %22s   %-14s %22s  %s' % ('MORTA', '(pessoas fator ações)', 'HERDEIRO',
                                         '(pessoas fator ações)', 'distância'))
HERDA = {}
for nome, d in MORTA.items():
    achou = None
    for vn, vd in VIVA.items():
        if (vd['pessoas'] == d['pessoas'] and abs(vd['fator'] - d['fator']) < 1e-9
                and vd['acoes'] == d['acoes'] and vd['corpos'] == 1):
            achou = vn
            break
    HERDA[nome] = achou
    if achou:
        v = VIVA[achou]
        print('  %-14s %8dp %6.2f %4da   ⟹ %-12s %8dp %6.2f %4da  %s'
              % (nome, d['pessoas'], d['fator'], d['acoes'], achou,
                 v['pessoas'], v['fator'], v['acoes'], 'EXATO'))
    else:
        print('  %-14s %8dp %6.2f %4da   ⟹ %-12s %22s  %s'
              % (nome, d['pessoas'], d['fator'], d['acoes'], '— ÓRFÃ —', '', '⚠ SEM HERDEIRO'))

orfas = [k for k, v in HERDA.items() if v is None]
print()
print('  ⟹ %d de %d degraus da escada morta têm herdeiro EXATO nos três eixos.'
      % (len(MORTA) - len(orfas), len(MORTA)))
if orfas:
    print('    órfã(s): ' + ', '.join('`%s`' % o for o in orfas))


# ═══════════════════════════════════════════ §2 · CÉLULA A CÉLULA
print()
print('=' * 92)
print('§2 · A CONFERÊNCIA CÉLULA A CÉLULA — 29 níveis × 4 colunas, gerador contra `TABELA.md`')
print('=' * 92)
print('  Recomputo cada degrau morto com as fórmulas do `make.js` e comparo com a coluna viva.')
print()


def faixa_de(nv):
    for f in FAIXAS:
        if f['de'] <= nv <= f['ate']:
            return f
    return None


print('  %-12s %-12s %8s %8s %8s %8s %9s' % ('morta', 'herdeiro', 'vida', 'dano/rod',
                                             'ações', 'golpe', 'bate?'))
for nome, d in MORTA.items():
    her = HERDA[nome]
    if not her:
        print('  %-12s %-12s %8s %8s %8s %8s %9s'
              % (nome, '— órfã —', '—', '—', '—', '—', '—'))
        continue
    ok = dict(vida=0, dano=0, acoes=0, golpe=0)
    for nv in NIVEIS:
        f = faixa_de(nv)
        if not f:
            continue
        v_calc = arred(f['chefe_vida'] * d['fator'])
        dn_calc = arred(f['chefe_dano'] * d['fator'])
        ac_calc = acoes(d['pessoas'])
        g_calc = golpe(f['chefe_dano'], d['fator'], d['pessoas'])
        linha = T[her][nv]
        ok['vida'] += (int(linha['vida']) == v_calc)
        ok['dano'] += (int(linha['dano/rod']) == dn_calc)
        ok['acoes'] += (int(linha['ações']) == ac_calc)
        ok['golpe'] += (linha['o golpe'].strip() == g_calc)
    n = len(NIVEIS)
    todos = all(v == n for v in ok.values())
    print('  %-12s %-12s %6d/%-2d %6d/%-2d %6d/%-2d %6d/%-2d %9s'
          % (nome, her, ok['vida'], n, ok['dano'], n, ok['acoes'], n, ok['golpe'], n,
             '✓ IDÊNTICO' if todos else '⚠ DIVERGE'))

print()
print('  E as duas tabelas PUBLICADAS da peça 26, conferidas contra a `TABELA.md`:')
print('  %-12s %-12s %-30s %-30s' % ('morta', 'herdeiro', '§4.1 (vida · dano, nv10/20/30)',
                                     '§4.4 (por rodada · ações · golpe, nv30)'))
for nome, d in MORTA.items():
    her = HERDA[nome]
    a41 = F41.get(nome, {})
    a44 = F44.get(nome)
    if not her:
        print('  %-12s %-12s %-30s %-30s'
              % (nome, '— órfã —',
                 ' / '.join('%d·%d' % a41[k] for k in (10, 20, 30)),
                 '%d · %da · %s' % a44 if a44 else '—'))
        continue
    bate41 = all(int(T[her][k]['vida']) == a41[k][0] and int(T[her][k]['dano/rod']) == a41[k][1]
                 for k in (10, 20, 30))
    bate44 = (int(T[her][30]['dano/rod']) == a44[0] and int(T[her][30]['ações']) == a44[1]
              and T[her][30]['o golpe'].strip() == a44[2])
    print('  %-12s %-12s %-30s %-30s'
          % (nome, her, '✓ bate nos três' if bate41 else '⚠ DIVERGE',
             '✓ bate' if bate44 else '⚠ DIVERGE'))


# ═══════════════════════════════════════════ §3 · A LEITURA PUBLICADA
print()
print('=' * 92)
print('§3 · ⚠ A LEITURA PUBLICADA `Alcateia ⟹ Capanga`, MEDIDA')
print('=' * 92)
print('  O `ESTADO-onde-paramos.md` e a `MEDIDA-as-seis-prontas.md` §4 publicam:')
print('    "`Ronda` era `1` personagem ⟹ `Ameaça`; `Alcateia` era o esquadrão ⟹ `Capanga`"')
print()
alc = MORTA['Alcateia']
cap = VIVA['Capanga']
print('  %-34s %10s %10s %10s' % ('', 'Alcateia', 'Capanga', 'Desastre'))
print('  %-34s %10.2f %10.2f %10.2f' % ('fator', alc['fator'], cap['fator'],
                                        VIVA['Desastre']['fator']))
print('  %-34s %10d %10d %10d' % ('ações', alc['acoes'], cap['acoes'],
                                  VIVA['Desastre']['acoes']))
print('  %-34s %10s %10d %10d' % ('corpos', '1', cap['corpos'], VIVA['Desastre']['corpos']))
for nv in (10, 20, 30):
    f = faixa_de(nv)
    print('  %-34s %10d %10s %10s'
          % ('vida no nv%d' % nv, arred(f['chefe_vida'] * alc['fator']),
             T['Capanga'][nv]['vida de um'], T['Desastre'][nv]['vida']))
razao_v = arred(faixa_de(20)['chefe_vida'] * alc['fator']) / float(T['Capanga'][20]['vida de um'])
print()
print('  ⟹ `Alcateia` ÷ `Capanga` em vida, no nv20: %.2f×.  `Alcateia` ÷ `Desastre`: %.2f×.'
      % (razao_v, arred(faixa_de(20)['chefe_vida'] * alc['fator']) / float(T['Desastre'][20]['vida'])))
print('  ⟹ fator: `Alcateia` %.2f · `Capanga` %.2f (%.0f× de distância) · `Desastre` %.2f (exato)'
      % (alc['fator'], cap['fator'], alc['fator'] / cap['fator'], VIVA['Desastre']['fator']))
print()
print('  E a própria peça 26 §4.3 já separa os dois, palavra por palavra:')
# a frase fala da escada MORTA, então ela mora na peça velha — a de hoje não tem `Ronda`
m = re.search(r'\*\*É por isso que o capanga do manual não é uma `Ronda`\.\*\*(.{0,220})',
              t26morta, re.S)
exige(m, 'a frase "o capanga do manual não é uma `Ronda`" sumiu do §4.3')
print('    "É por isso que o capanga do manual não é uma `Ronda`."')
print('    ⟹ o capanga do manual era EIXO SEPARADO da escada, não um degrau dela.')


# ═══════════════════════════════════════════ §4 · A ARMADILHA DO NOME
print()
print('=' * 92)
print('§4 · ⚠⚠ A ARMADILHA — o nome `Calamidade` sobrevive e o SIGNIFICADO não')
print('=' * 92)
cm, cv = MORTA['Calamidade'], VIVA['Calamidade']
her_cal = HERDA['Calamidade']
print('  %-28s %12s %12s' % ('', '`Calamidade`', '`Calamidade`'))
print('  %-28s %12s %12s' % ('', 'MORTA', 'VIVA'))
print('  %-28s %12d %12s' % ('personagens', cm['pessoas'],
                             cv['pessoas'] if cv['pessoas'] else '> 6'))
print('  %-28s %12.2f %12.2f' % ('fator', cm['fator'], cv['fator']))
print('  %-28s %12d %12d' % ('ações', cm['acoes'], cv['acoes']))
print()
print('  ⟹ O MESMO NOME vale %.2f× mais na escada viva. E o herdeiro real da morta é `%s`.'
      % (cv['fator'] / cm['fator'], her_cal))
print('  ⚠ Renomear as seis e deixar o `Calamidade` quieto NÃO é seguro: o `make.js` imprime')
print('    a escada INTEIRA em duas tabelas do `.docx`, não só as seis fichas.')
usa_cal = [n for n, _f, c in SEIS if c == 'Calamidade']
print('    Das seis prontas, %s usa `Calamidade` — mas a COLUNA dela vai pro livro do mesmo jeito.'
      % (', '.join(usa_cal) if usa_cal else 'nenhuma'))


# ═══════════════════════════════════════════ §5 · A DUPLA
print()
print('=' * 92)
print('§5 · A `Dupla` — a órfã, e as saídas medidas')
print('=' * 92)
dup = MORTA['Dupla']
dela = [n for n, _f, c in SEIS if c == 'Dupla']
print('  `Dupla`: %d personagens · fator %.2f · %d ação.  Fichas dela: %s'
      % (dup['pessoas'], dup['fator'], dup['acoes'], ', '.join(dela)))
print('  Entre `Ameaça` (%.2f) e `Desastre` (%.2f) a escada viva não tem degrau.'
      % (VIVA['Ameaça']['fator'], VIVA['Desastre']['fator']))
print()


def mundo(nv):
    d = T['Desastre'][nv]
    vida_chefe = float(d['vida'])
    dano_chefe = float(d['dano/rod'])
    saida = vida_chefe / VEZES
    vida_pj = dano_chefe / PCT
    return dict(nv=nv, vida_chefe=vida_chefe, dano_chefe=dano_chefe, saida=saida,
                vida_pj=vida_pj, vida_cap=saida / 4,
                golpe_cap=media_dado(T['Capanga'][nv]['golpe de um']))


def luta(corpos, saida, max_rod=60):
    """`corpos` = lista de (vida, dano por rodada). Fogo concentrado, do mais
    fraco pro mais forte — a mesma ordem que o §4.5 declara. Devolve o dano
    TOTAL que os inimigos entregam na luta."""
    corpos = sorted(corpos, key=lambda c: c[0])
    hp = [c[0] for c in corpos]
    dn = [c[1] for c in corpos]
    total, rod = 0.0, 0
    while any(h > 0 for h in hp) and rod < max_rod:
        rod += 1
        total += sum(d for h, d in zip(hp, dn) if h > 0)
        resto = saida
        for i in range(len(hp)):
            if resto <= 0:
                break
            if hp[i] <= 0:
                continue
            g = min(hp[i], resto)
            hp[i] -= g
            resto -= g
    return total, rod


def monta(w, especie, mesa):
    """Devolve a lista de corpos de um encontro, escalada por nada — a ficha é
    a ficha; quem escala com a mesa é a SAÍDA do grupo."""
    out = []
    for (fator, n) in especie:
        for _ in range(n):
            out.append((w['vida_chefe'] * fator, w['dano_chefe'] * fator))
    return out


def pessoas_que_exige(especie, capangas=0):
    """Acha a mesa N em que o encontro cobra os mesmos %% que o chefe sozinho."""
    lo, hi = 0.4, 40.0
    for _ in range(70):
        mid = (lo + hi) / 2
        ps = []
        for nv in NIVEIS:
            w = mundo(nv)
            corpos = monta(w, especie, mid)
            corpos += [(w['vida_cap'], w['golpe_cap'])] * capangas
            d, _ = luta(corpos, w['saida'] * mid / MESA)
            ps.append(d / (mid * w['vida_pj']))
        lo, hi = (mid, hi) if st.mean(ps) > COBRA else (lo, mid)
    return (lo + hi) / 2


def cobra(especie, capangas=0):
    """Quanto da vida da mesa PADRÃO o encontro leva embora. É a unidade em que
    a peça 26 §4.3 e o §4.5 publicam — `68%`, `0,75×`–`0,77×`."""
    ps = []
    for nv in NIVEIS:
        w = mundo(nv)
        corpos = monta(w, especie, MESA)
        corpos += [(w['vida_cap'], w['golpe_cap'])] * capangas
        d, _ = luta(corpos, w['saida'])
        ps.append(d / (MESA * w['vida_pj']))
    return st.mean(ps)


# — a guarda: o modelo reproduz DOIS números que ele não calibrou?
print('  GUARDA — o modelo reproduz o que já está publicado?')
c_des = cobra([(VIVA['Desastre']['fator'], 1)])
print('    `1 Desastre` sozinho cobra %.1f%% da vida do grupo — o §4.5 publica %.0f%%.'
      % (100 * c_des, 100 * COBRA))
exige(abs(c_des - COBRA) <= 0.03, 'o modelo NÃO reproduz o `%.0f%%` do §4.5' % (100 * COBRA))
n_des = pessoas_que_exige([(VIVA['Desastre']['fator'], 1)])
print('    e ele exige %.2f pessoas — a peça publica %d.' % (n_des, MESA))
exige(abs(n_des - MESA) <= 0.15, 'o modelo NÃO reproduz a mesa padrão — não dá pra confiar nele')
razao_r = cobra([(MORTA['Ronda']['fator'], 4)]) / c_des
print('    `4 Ronda` contra `1 Alcateia`: %.2f× — a peça 26 §4.3 publica %.2f×–%.2f×.'
      % (razao_r, AMEACA_4[0], AMEACA_4[1]))
ok_r = AMEACA_4[0] - 0.04 <= razao_r <= AMEACA_4[1] + 0.04
print('    ⟹ %s' % ('✓ o modelo reproduz uma âncora que ele NÃO calibrou.' if ok_r
                    else '⚠ FORA da banda publicada — leia com desconfiança.'))
exige(ok_r, 'o modelo não reproduz o `0,75×`–`0,77×` do §4.3')
print()

# — as saídas
print('  AS SAÍDAS, medidas nos %d níveis. ⚠ A unidade PRINCIPAL é `cobra da mesa padrão`,' % len(NIVEIS))
print('    que é a mesma em que a peça 26 §4.3 e §4.5 publicam — e é onde o modelo validou.')
print()
alvo_c = cobra([(dup['fator'], 1)])
alvo_n = pessoas_que_exige([(dup['fator'], 1)])
print('  %-38s %10s %11s %9s %8s %7s' % ('a saída', 'cobra', 'vs `Dupla`', 'pessoas',
                                         'fator', 'corpos'))
print('  %-38s %9.1f%% %11s %9.2f %8.3f %7d'
      % ('a `Dupla` de hoje (o que está no livro)', 100 * alvo_c, '—', alvo_n,
         alvo_n / MESA, 1))
print('  ' + '-' * 88)

saidas = [
    ('A · duas `Ameaça` (dois corpos)', [(VIVA['Ameaça']['fator'], 2)], 0, 2),
    ('B · `Ameaça` + 3 `Capanga` (a régua)', [(VIVA['Ameaça']['fator'], 1)], 3, 4),
    ('C · promover a `Desastre`', [(VIVA['Desastre']['fator'], 1)], 0, 1),
    ('D · rebaixar a `Ameaça`', [(VIVA['Ameaça']['fator'], 1)], 0, 1),
    ('E · um corpo, fator `0,50`, sem degrau', [(dup['fator'], 1)], 0, 1),
]
for rot, esp, cap, corpos in saidas:
    c = cobra(esp, cap)
    n = pessoas_que_exige(esp, cap)
    print('  %-38s %9.1f%% %10.1f%% %9.2f %8.3f %7d'
          % (rot, 100 * c, 100 * (c / alvo_c - 1), n, n / MESA, corpos))

print()
print('  ⟹ `vs Dupla` é quanto o encontro CRESCE ou ENCOLHE contra o que as duas fichas')
print('    publicadas cobram hoje. `0,0%` é a saída que não mexe na mesa de ninguém.')
print()
print('  ⚠⚠ E A COLUNA `pessoas` NÃO SERVE PRA DECIDIR AQUI — ela está sentada num DEGRAU.')
for mesa in (1.90, 2.00):
    ps = {}
    for rot, esp, cap in (('Dupla', [(dup['fator'], 1)], 0),
                          ('2 Ameaça', [(VIVA['Ameaça']['fator'], 2)], 0)):
        vals = []
        for nv in NIVEIS:
            w = mundo(nv)
            corpos = monta(w, esp, mesa) + [(w['vida_cap'], w['golpe_cap'])] * cap
            d, _ = luta(corpos, w['saida'] * mesa / MESA)
            vals.append(d / (mesa * w['vida_pj']))
        ps[rot] = st.mean(vals)
    print('    numa mesa de %.2f pessoas: `Dupla` cobra %.1f%% · duas `Ameaça` cobram %.1f%%'
          % (mesa, 100 * ps['Dupla'], 100 * ps['2 Ameaça']))
print('    ⟹ de %.2f pra %.2f a cobrança despenca, porque a luta perde uma RODADA inteira.'
      % (1.90, 2.00))
print('    A busca binária cai dentro desse degrau e devolve `2,00` pras duas.')
print('    ⚠ É o mesmo defeito que o `DECIDIDO-o-capanga-unico` §2 já registrou:')
print('      "o chefe a `91,5%` cobra `67,4%`; a `92%` cobra `80,3%`" — meio ponto move 13.')
print('    ⟹ Leia a coluna `cobra`. A coluna `pessoas` fica pra conferência, não pra decisão.')
print()
print('  E a razão de duas `Ameaça` contra uma `Dupla` é a MESMA que o §4.3 já publicou:')
print('    quatro `Ronda` contra uma `Alcateia` : %.3f×  (a peça publica %.2f×–%.2f×)'
      % (cobra([(MORTA['Ronda']['fator'], 4)]) / cobra([(MORTA['Alcateia']['fator'], 1)]),
         AMEACA_4[0], AMEACA_4[1]))
print('    duas  `Ameaça` contra uma `Dupla`   : %.3f×  ⟹ mesma propriedade, mesmo número'
      % (cobra([(VIVA['Ameaça']['fator'], 2)]) / alvo_c))
print('    *eles morrem em fila e a saída deles despenca* — §4.3, palavra por palavra.')

# — o golpe de cada saída, que é o que o mestre lê em voz alta
print()
print('  E O GOLPE, que é o que muda na MÃO do mestre (nv 26–30, a faixa mais gorda):')
f30 = faixa_de(30)
print('    `Dupla` publicada        : %5d por rodada · %d ação · %s'
      % (arred(f30['chefe_dano'] * dup['fator']), dup['acoes'],
         golpe(f30['chefe_dano'], dup['fator'], dup['pessoas'])))
for nome_v in ('Ameaça', 'Desastre'):
    v = VIVA[nome_v]
    print('    `%-22s`: %5s por rodada · %s ação(ões) · %s'
          % (nome_v, T[nome_v][30]['dano/rod'], T[nome_v][30]['ações'],
             T[nome_v][30]['o golpe']))
print('    duas `Ameaça` juntas    : %5d por rodada · 1 ação cada · %s + %s'
      % (2 * int(T['Ameaça'][30]['dano/rod']), T['Ameaça'][30]['o golpe'],
         T['Ameaça'][30]['o golpe']))

# — as duas fichas, uma a uma
print()
print('  E AS DUAS FICHAS, uma a uma — porque a ficção delas não é a mesma:')
tj_txt = tj
for nome_f in dela:
    m = re.search(r"\{\s*nome:\s*'%s'.*?linha:\s*'([^']*)'.*?notas:\s*'([^']*)'" % nome_f,
                  tj_txt, re.S)
    exige(m, 'a ficção da `%s` sumiu do dados.js' % nome_f)
    corpos = 'DOIS corpos' if 'Duas ' in m.group(2) or 'dupla' in m.group(1).lower() else 'UM corpo?'
    print('    `%s` — %s' % (nome_f, m.group(1)))
    print('      ⟹ a ficção descreve: %s' % corpos)


# ═══════════════════════════════════════════ §6 · A BANDA — a métrica que PEGOU a Dupla
print()
print('=' * 92)
print('§6 · ⚠⚠ A BANDA DO `o golpe` — e a escada viva já escreveu que a `Dupla` era o DEFEITO')
print('=' * 92)

tesc = ler(ESC)
m = re.search(r'\*\*Foi isso que quebrou a `Dupla`\*\*', tesc)
exige(m, 'a frase "Foi isso que quebrou a `Dupla`" sumiu da `a-escada-com-numero.md`')
m2 = re.search(r'A do bestiário antigo era de `(\d+)%` a `(\d+)%`, vinte e dois pontos, '
               r'e o topo dela era a `Dupla`', tesc)
exige(m2, 'a frase "o topo dela era a `Dupla`" sumiu da `a-escada-com-numero.md`')
BANDA_VELHA = (int(m2.group(1)) / 100, int(m2.group(2)) / 100)
exige('E `Ações` é número DECLARADO' in tesc,
      'a seção "Ações é número DECLARADO" sumiu da `a-escada-com-numero.md`')

tcap = ler(CAPD)
m3 = re.search(r'A banda do `o golpe` vira \*\*`(\d+)%`–`(\d+)%`\*\*', tcap)
exige(m3, 'a âncora da banda sumiu do `DECIDIDO-o-capanga.md` §1')
BANDA = (int(m3.group(1)) / 100, int(m3.group(2)) / 100)

print('  O `a-escada-com-numero.md` publica, sobre a escada viva, palavra por palavra:')
print('    · "No bestiário antigo ele saía de `personagens − 1`… **Foi isso que quebrou a `Dupla`**,')
print('       que levava o dobro do orçamento pela mesma porta."')
print('    · "A do bestiário antigo era de `%d%%` a `%d%%`… e **o topo dela era a `Dupla`**."'
      % (100 * BANDA_VELHA[0], 100 * BANDA_VELHA[1]))
print('    · "E `Ações` é número **DECLARADO**." ⟹ a regra `personagens − 1` está MORTA.')
print()
print('  ⟹ A `Dupla` não ficou órfã por descuido. Ela É o defeito que a escada nova removeu.')
print('    A âncora da banda viva é o `DECIDIDO-o-capanga.md` §1: `%d%%`–`%d%%`.'
      % (100 * BANDA[0], 100 * BANDA[1]))
print()


# ⚠ a vida de UM personagem sai da MESMA âncora que o `medir-o-capanga.py` usa —
#   a fatia PUBLICADA do `Desastre` na `a-escada-com-numero.md`, e não de `dano ÷ PCT`.
#   Sem isso a varredura devolve `21,2%` onde a banda publica `21,8%`, e a comparação
#   deixa de ser com a régua do dono.
m4 = re.search(r'\| nv \| `Capanga` \| `Ameaça` \| `Desastre` \| `Catástrofe` \| `Calamidade` \|',
               tesc)
exige(m4, 'a tabela de fatia da `a-escada-com-numero.md` mudou de forma')
FATIA_PUB = {}
for ln in tesc.split('\n'):
    mm = re.match(r'\|\s*(\d+)\s*\|\s*`(\d+)%`\s*\|\s*`(\d+)%`\s*\|\s*`(\d+)%`\s*\|'
                  r'\s*`(\d+)%`\s*\|\s*`(\d+)%`\s*\|', ln)
    if mm:
        FATIA_PUB[int(mm.group(1))] = int(mm.group(4)) / 100      # a coluna `Desastre`
exige(len(FATIA_PUB) == 4, 'a fatia publicada do `Desastre` sumiu (li %d níveis)' % len(FATIA_PUB))
m5 = re.search(r'fator de dano de quem tem `Intervenção` é multiplicado por `([\d,]+)`', t5)
exige(m5, 'o fator `0,923` da Intervenção sumiu do RASCUNHO-5')
FATOR_INT = num(m5.group(1))
TEM_INT = {'Desastre', 'Catástrofe', 'Calamidade'}
print('  âncoras desta varredura: fatia publicada do `Desastre` = %.0f%% · Intervenção `%.3f`'
      % (100 * list(FATIA_PUB.values())[0], FATOR_INT))
print()


def vida_de_um_pj(nv):
    """A mesma derivação do `medir-o-capanga.py` §6: o golpe do `Desastre` daquele
    nível dividido pela fatia PUBLICADA dele."""
    ref = min(FATIA_PUB, key=lambda k: abs(k - nv))
    return media_dado(T['Desastre'][nv]['o golpe']) / FATIA_PUB[ref]


def fatia(nv, fator, n_acoes, tem_int=False):
    """Que fração da vida de UM personagem um golpe leva. É a métrica que a
    `a-escada-com-numero.md` chama de "a que pegou a `Dupla`"."""
    f = faixa_de(nv)
    alvo = arred(f['chefe_dano'] * fator) / n_acoes
    g = media_dado(dado(alvo))
    return g * (FATOR_INT if tem_int else 1.0) / vida_de_um_pj(nv)


print('  %-42s %9s %9s %9s %9s' % ('', 'nv2', 'nv10', 'nv20', 'nv30'))
CANDS = [
    ('a `Dupla` publicada — fator 0,50 · 1 ação', dup['fator'], 1, False),
    ('`Ameaça` (o piso da banda viva)', VIVA['Ameaça']['fator'], VIVA['Ameaça']['acoes'], False),
    ('`Desastre` (a âncora, com a Intervenção)', VIVA['Desastre']['fator'],
     VIVA['Desastre']['acoes'], True),
    ('⟹ um corpo fator 0,50 com **2 ações**', dup['fator'], 2, False),
]
res_banda = {}
for rot, fat, nac, ti in CANDS:
    linha, fora = [], 0
    for nv in NIVEIS:
        v = fatia(nv, fat, nac, ti)
        linha.append(v)
        fora += not (BANDA[0] - 0.005 <= v <= BANDA[1] + 0.005)
    res_banda[rot] = (linha, fora)
    idx = {nv: i for i, nv in enumerate(NIVEIS)}
    print('  %-42s %8.1f%% %8.1f%% %8.1f%% %8.1f%%'
          % (rot, 100 * linha[idx[2]], 100 * linha[idx[10]], 100 * linha[idx[20]],
             100 * linha[idx[30]]))
print()
print('  %-42s %12s %12s' % ('', 'níveis FORA', 'de'))
for rot, (linha, fora) in res_banda.items():
    print('  %-42s %12d %12d  %s' % (rot, fora, len(NIVEIS),
                                     '⚠ FURA A BANDA' if fora else '✓ dentro'))
print()
d_lin, d_fora = res_banda['a `Dupla` publicada — fator 0,50 · 1 ação']
print('  ⟹ A `Dupla` publicada entrega %.0f%% da vida de um personagem NUM GOLPE SÓ,'
      % (100 * max(d_lin)))
print('    contra um teto vivo de %d%%. É %.2f× o topo da banda, em %d de %d níveis.'
      % (100 * BANDA[1], max(d_lin) / BANDA[1], d_fora, len(NIVEIS)))
print('    E as DUAS fichas do livro — `%s` — carregam isso.' % '` e `'.join(dela))
print()
b_lin, b_fora = res_banda['⟹ um corpo fator 0,50 com **2 ações**']
print('  ⟹ E a saída sai de graça, porque `Ações` virou número DECLARADO:')
print('    o MESMO fator `0,50`, com `2` ações em vez de `1`, cai pra %.1f%%–%.1f%% — DENTRO.'
      % (100 * min(b_lin), 100 * max(b_lin)))
print('    Vida e dano por rodada não se movem ⟹ o encontro é o mesmo (a saída `E` do §5, `0,0%`).')
print('    ⚠ O que muda na mão do mestre: o golpe do nv30 sai de `%s` para `%s`.'
      % (golpe(faixa_de(30)['chefe_dano'], dup['fator'], 2),
         dado(arred(faixa_de(30)['chefe_dano'] * dup['fator']) / 2)))


# ═══════════════════════════════════════════ §7 · O ORÇAMENTO DE FEITIÇO
print()
print('=' * 92)
print('§7 · ⚠⚠⚠ E A COISA QUE NENHUMA DAS SAÍDAS RESOLVE — a `Kitsune` CONJURA')
print('=' * 92)
m6 = re.search(r'dividido por `([\d,]+)` dá menos que os `(\d+)` pontos da `Classe 1`', t5)
exige(m6, 'o piso `seco` sumiu do RASCUNHO-5')
DIV, PISO_SECO = num(m6.group(1)), int(m6.group(2))
print('  O `RASCUNHO-5` publica o piso: golpe da ação ÷ `%.1f` < `%d` pontos ⟹ ela NÃO monta feitiço.'
      % (DIV, PISO_SECO))
# O commit `C` da v0.221 tirou o campo `caracteristicas` das `PRONTAS` do `dados.js`:
# o feitiço da `Kitsune` passou a ser COMPUTADO (`⌊golpe ÷ 4,5⌋d8`, o marcador
# `{tecnica_dano}`), e o `4,2` deixou de morar lá. O dono do número passou a ser o
# martelo que o fixou — o `DECIDIDO-as-seis-prontas.md` §2.
DEC_SEIS = os.path.join(BEST, '04-fase-1', 'fila', 'DECIDIDO-as-seis-prontas.md')
tdec_seis = ler(DEC_SEIS)
m7 = re.search(r'uma técnica de `Classe 1` no orçamento de `([\d,]+)` pontos', tdec_seis)
exige(m7, 'o orçamento publicado da `Kitsune` sumiu do `DECIDIDO-as-seis-prontas.md` §2')
KITSUNE_PTS = num(m7.group(1))
print('  E o `DECIDIDO-as-seis-prontas.md` §2 publica, da ficha da `Kitsune`:')
print('    "uma técnica de `Classe 1` no orçamento de `%.1f` pontos da ação."'
      % KITSUNE_PTS)
print('    A linha dela é: "a única da faixa que conjura."')
print()


def pontos(faixa_rot, fator, n_acoes):
    f = [x for x in FAIXAS if x['rot'] == faixa_rot][0]
    return (arred(f['chefe_dano'] * fator) / n_acoes) / DIV


kit_faixa = [f for n, f, c in SEIS if n == 'Kitsune'][0]
print('  A `Kitsune` está na faixa `%s`. Quantos pontos a ação dela tem em cada saída:' % kit_faixa)
print()
print('  %-46s %10s %10s' % ('a saída', 'pontos', 'conjura?'))
SAIDAS_PTS = [
    ('a `Dupla` de hoje — fator 0,50 · 1 ação', dup['fator'], 1),
    ('A · duas `Ameaça` (cada corpo)', VIVA['Ameaça']['fator'], VIVA['Ameaça']['acoes']),
    ('B · `Ameaça` + 3 `Capanga` (o corpo do chefe)', VIVA['Ameaça']['fator'],
     VIVA['Ameaça']['acoes']),
    ('C · promover a `Desastre`', VIVA['Desastre']['fator'], VIVA['Desastre']['acoes']),
    ('D · rebaixar a `Ameaça`', VIVA['Ameaça']['fator'], VIVA['Ameaça']['acoes']),
    ('E · fator 0,50 com **2 ações** (a saída do §6)', dup['fator'], 2),
    ('o TOPO da escada viva na mesma faixa: `Calamidade`', VIVA['Calamidade']['fator'],
     VIVA['Calamidade']['acoes']),
]
for rot, fat, nac in SAIDAS_PTS:
    p = pontos(kit_faixa, fat, nac)
    print('  %-46s %10.1f %10s' % (rot, p, '✓ sim' if p >= PISO_SECO else '❌ SECO'))
print()
vivas_conjuram = [rot for rot, fat, nac in SAIDAS_PTS[1:]
                  if pontos(kit_faixa, fat, nac) >= PISO_SECO]
print('  ⟹ %d de %d saídas da escada VIVA deixam a `Kitsune` conjurar NESTA FAIXA.'
      % (len(vivas_conjuram), len(SAIDAS_PTS) - 1))
print('    ⚠ Nem o TOPO da escada viva conjura aqui — e isso não é defeito, é o piso `seco`,')
print('      fechado por ele no item `21` em 10/09: "`1` entrada é o que `25%` do D&D 2024 imprime".')
print()
print('  ⟹⟹ O ACHADO: a única coisa que faz a `Kitsune` ser a `Kitsune` só existe na escada MORTA.')
print('     Ela conjura porque a `Dupla` concentrava `2` pessoas de orçamento numa ação só —')
print('     que é EXATAMENTE o defeito que a escada nova removeu de propósito.')
print('     Consertar a categoria dela apaga a ficha. Manter a ficha ressuscita o defeito.')
print()

# — a saída F: subir de faixa
print('  ⚡ MAS EXISTE UMA SAÍDA QUE NINGUÉM TINHA OLHADO — mudar a FAIXA em vez da categoria.')
print()
print('  %-30s %10s %10s %12s' % ('a `Ameaça`, por faixa', 'pontos', 'conjura?', 'vs os %.1f dela'
                                  % KITSUNE_PTS))
achou_f = None
for f in FAIXAS:
    p = pontos(f['rot'], VIVA['Ameaça']['fator'], VIVA['Ameaça']['acoes'])
    marca = '✓ sim' if p >= PISO_SECO else '❌ SECO'
    dist = '%+.1f%%' % (100 * (p / KITSUNE_PTS - 1))
    if p >= PISO_SECO and achou_f is None:
        achou_f = (f['rot'], p)
    print('  %-30s %10.1f %10s %12s' % ('nv ' + f['rot'], p, marca, dist))
print()
exige(achou_f, 'nenhuma faixa da `Ameaça` sai do `seco` — a escada mudou')
print('  ⟹ SAÍDA `F` · a `Kitsune` sobe de faixa: `%s` ⟹ `%s`, e vira `Ameaça`.'
      % (kit_faixa, achou_f[0]))
print('    Ela fica com `%.1f` pontos — %s os `%.1f` que a ficha publicada já declara.'
      % (achou_f[1], 'EXATAMENTE' if abs(achou_f[1] - KITSUNE_PTS) < 0.05 else 'perto d',
         KITSUNE_PTS))
print('    ⟹ a característica dela — "no orçamento de `%.1f` pontos da ação" — NÃO MUDA UMA LETRA.'
      % KITSUNE_PTS)
print('    ⚠ O preço: as seis deixam de cobrir `nv 2 ao 6` e passam a cobrir `nv 2 ao 12`.')
print()

print('  E a `Kamaitachi` NÃO tem esse problema — a característica dela é:')
# mesma história da `Kitsune`: o campo `caracteristicas` morreu no commit `C`. A
# ficção de dois corpos passou a viver em dois campos melhores — o traço `Par` e o
# `corpos_na_mesa`, que é NÚMERO e o gerador imprime.
m8 = re.search(r"\{\s*nome:\s*'Kamaitachi'.*?corpos_na_mesa:\s*(\d+).*?"
               r'"nome": "Par", "texto": "([^"]*)"', tj, re.S)
exige(m8, 'o traço `Par` ou o `corpos_na_mesa` da `Kamaitachi` sumiu do `dados.js`')
exige(int(m8.group(1)) == 2, 'a `Kamaitachi` deixou de ser DOIS corpos no `dados.js`')
print('    `corpos_na_mesa: %s` · traço `Par`: "%s"' % (m8.group(1), m8.group(2)))
print('    ⟹ a ficção dela JÁ É dois corpos. A saída `A` (duas `Ameaça`) escreve a ficção dela')
print('      sem mudar uma palavra.')


# ═══════════════════════════════════════════ §8 · A GRADE — ainda dá SEIS?
print()
print('=' * 92)
print('§8 · E A GRADE QUE PRODUZIU AS SEIS — ela ainda dá seis na escada VIVA?')
print('=' * 92)
# Até a v0.220 o `dados.js` DERIVAVA o seis ("a faixa do nível 2 ao 6 cruza DUAS
# linhas de FAIXAS com as QUATRO categorias"). O commit `C` da v0.221 trocou o
# comentário: a derivação morreu junto com a escada, e o seis passou a ser escolha
# declarada. O §8 deixou de perguntar "ainda dá seis?" e passou a CONFERIR o registro.
m9 = re.search(r'Sao seis porque sao seis: a derivacao antiga \(duas faixas vezes as quatro\s*'
               r'\n?//?\s*categorias, menos a Calamidade\) morreu com a escada', tj)
exige(m9, 'o comentário do número SEIS sumiu do `dados.js` — nem a derivação velha, '
      'nem o registro de que ela morreu')
print('  O `dados.js` NÃO deriva mais o seis, e diz isso:')
print('    "São seis porque são seis: a derivação antiga (duas faixas vezes as quatro')
print('     categorias, menos a Calamidade) morreu com a escada."')
print('  ⟹ o número virou escolha declarada. A grade abaixo fica como REGISTRO do que')
print('    a derivação daria hoje, e não como dona do número.')
print()
FAIXAS_BAIXAS = [f for f in FAIXAS if f['de'] <= 6]
print('  Rodando a MESMA derivação na escada viva:')
print('    faixas que cobrem o nv 2 ao 6 : %d  (%s)'
      % (len(FAIXAS_BAIXAS), ', '.join(f['rot'] for f in FAIXAS_BAIXAS)))
cabe, nao_cabe = [], []
for nome in ('Capanga', 'Ameaça', 'Desastre', 'Catástrofe', 'Calamidade'):
    v = VIVA[nome]
    pes = v['pessoas'] if v['pessoas'] else round(v['fator'] * MESA)
    (cabe if pes <= MESA else nao_cabe).append((nome, pes))
print('    categorias que uma mesa de %d aguenta : %d  (%s)'
      % (MESA, len(cabe), ', '.join('%s %s' % (n, ('%dp' % p) if n != 'Capanga' else '—')
                                    for n, p in cabe)))
print('    categorias que ela NÃO tem gente pra : %d  (%s)'
      % (len(nao_cabe), ', '.join('%s %dp' % (n, p) for n, p in nao_cabe)))
print()
print('  ⟹ %d faixas × %d categorias = **%d células**.'
      % (len(FAIXAS_BAIXAS), len(cabe), len(FAIXAS_BAIXAS) * len(cabe)))
if len(FAIXAS_BAIXAS) * len(cabe) == len(SEIS):
    print('    ⚡ A grade viva dá o MESMO número: %d. As seis continuam sendo seis.' % len(SEIS))
    print('    O que muda é a COMPOSIÇÃO: sai `Ronda`·`Dupla`·`Alcateia`, entra')
    print('    `Capanga`·`Ameaça`·`Desastre` — e a vaga da `Dupla` vira vaga de `Capanga`.')
else:
    print('    ⟹ a grade viva daria %d células, e as prontas são %d — e está tudo bem:'
          % (len(FAIXAS_BAIXAS) * len(cabe), len(SEIS)))
    print('      o `dados.js` parou de derivar o número, e declara a escolha.')
print()
print('  E o que a vaga da `Dupla` passa a custar, se ela virar `Capanga`:')
for n in (2, 3, VIVA['Capanga']['corpos']):
    cn = cobra([], capangas=n)
    print('    %d `Capanga` sozinhos: cobram %5.1f%% da mesa padrão, contra %.1f%% da `Dupla` — %+.1f%%.'
          % (n, 100 * cn, 100 * alvo_c, 100 * (cn / alvo_c - 1)))
print('    ⚠ e o `Capanga` NÃO tem vida derivada do chefe: ela é `dano do grupo ÷ 4`.')
print('      ⟹ é o único degrau vivo cuja ficha não sai de multiplicar a linha do manual.')



# ═══════════════════════════════════════════ §9 · A VARREDURA DO GERADOR
print()
print('=' * 92)
print('§9 · A VARREDURA — quantos pontos do `gerador-inimigo/` falam a escada MORTA')
print('=' * 92)
MAKE = os.path.join(REPO, 'sistema/05-material/gerador-inimigo/make.js')
tm = ler(MAKE)
MORTOS = tuple(MORTA)          # os quatro nomes, lidos da peça 26

# ⚠ CAIXA DE CORREÇÃO — a primeira versão deste §9 varria SÓ o `dados.js` e o
#   `make.js`, e publicou "24 linhas" como se fosse o repositório inteiro.
#   Era o total dos dois arquivos que eu tinha escolhido olhar, e a escolha era
#   minha. A varredura de verdade anda o repositório todo.
IGNORA = ('.claude/worktrees', '_backup', '_to_delete', '__pycache__')
EXT = ('.md', '.py', '.js', '.txt')
# o CHANGELOG é registro histórico: ele DEVE falar a escada morta.
# e `finalizado/` é ESPELHO — outro repo git, recortado byte a byte da fonte, e a
# checagem 7 do `conferir-repositorio.py` é a dona dessa comparação. Não é edição
# a mais; é um push a mais.
HISTORICO = ('logs/CHANGELOG.md',)


def espelho(rel):
    return rel.startswith('finalizado/')

alvos = []
for raiz, dirs, arqs in os.walk(REPO):
    dirs[:] = [d for d in dirs if not any(x in os.path.join(raiz, d) for x in IGNORA)]
    for a in arqs:
        if a.endswith(EXT):
            alvos.append(os.path.join(raiz, a))
alvos.sort()
exige(len(alvos) > 50, 'a varredura achou só %d arquivos — o REPO está no lugar certo?'
      % len(alvos))

achado_por_arq, total, n_hist = {}, 0, 0
for caminho in alvos:
    rel = os.path.relpath(caminho, REPO)
    try:
        txt = open(caminho, encoding='utf-8').read()
    except (UnicodeDecodeError, OSError):
        continue
    linhas = []
    for i, ln in enumerate(txt.split('\n'), 1):
        quais = [c for c in MORTOS if re.search(r'\b%s\b' % c, ln)]
        if quais:
            linhas.append((i, quais, ln.strip()))
    if not linhas:
        continue
    achado_por_arq[rel] = linhas
    if rel in HISTORICO or espelho(rel):
        n_hist += len(linhas)
    else:
        total += len(linhas)

print()
print('  Varridos %d arquivos do repositório (fora de worktree, backup e cache).' % len(alvos))
print()
print('  %-52s %8s %s' % ('arquivo', 'linhas', 'o que é'))
QUEM = {
    'sistema/03-mecanica/26-bestiario.md': 'peça VIVA — já na MEXIDAS',
    'sistema/03-mecanica/conferir-bestiario.py': 'validador — já na MEXIDAS',
    'sistema/03-mecanica/conferir-ficha.py': 'validador — bloco 7',
    'sistema/03-mecanica/15-invocacoes.md': '⚠⚠ peça VIVA — FORA DE TODA LISTA',
    'sistema/05-material/gerador-inimigo/dados.js': 'gerador — item 30c',
    'sistema/05-material/gerador-inimigo/make.js': 'gerador — item 30c',
    'sistema/05-material/gerador-inimigo/COMO-USAR.txt': '⚠ gerador — eu tinha PULADO',
    'sistema/04-playtest/mesa-01-grupo-01.md': '⚠ registro de mesa real',
    'sistema/ESTADO-ATUAL.md': '⚠ estado do repo',
    'logs/CHANGELOG.md': 'histórico — DEVE falar a morta',
    'finalizado/regra/26-bestiario.md': 'ESPELHO byte a byte — checagem 7',
    'finalizado/regra/15-invocacoes.md': 'ESPELHO byte a byte — checagem 7',
}
for rel, linhas in sorted(achado_por_arq.items(), key=lambda kv: -len(kv[1])):
    print('  %-52s %8d %s' % (rel, len(linhas), QUEM.get(rel, '?')))
print()
fontes = [r for r in achado_por_arq if r not in HISTORICO and not espelho(r)]
print('  ⟹ %d linhas em %d arquivos-FONTE que citam a escada morta.' % (total, len(fontes)))
print('    (+ %d em espelho e histórico, que não são edição a mais.)' % n_hist)
print('    ⚠ "linha que cita" NÃO é "mexida": a `MEXIDAS-no-repositorio.md` conta mudança')
print('      SEMÂNTICA, e uma tabela inteira trocada é uma mexida com dez linhas dentro.')
print('      Este número é a SUPERFÍCIE, e serve pra achar arquivo esquecido — não pra estimar.')
print()
novos = [r for r in fontes
         if 'gerador-inimigo/dados.js' not in r and 'gerador-inimigo/make.js' not in r
         and '26-bestiario' not in r and 'conferir-bestiario' not in r
         and 'conferir-ficha' not in r]
print('  ⚠⚠ E %d arquivo(s) NÃO estavam em lista nenhuma — nem na `MEXIDAS`, nem no item `30`:'
      % len(novos))
for r in sorted(novos):
    print('    · %-50s %d linha(s)' % (r, len(achado_por_arq[r])))
print()
print('  ⟹ a `15-invocacoes.md` é PEÇA DE REGRA VIVA, e ela calibra a morte do')
print('    shikigami contra o golpe da `Dupla`. Conta em `medir-a-peca-15.py` (o 28º).')
print()
tm_ = tm
print('  E o detalhe linha a linha dos dois arquivos do gerador:')
for rot, txt in (('dados.js', tj), ('make.js', tm_)):
    rel = 'sistema/05-material/gerador-inimigo/' + rot
    print()
    print('  `%s` — %d linha(s):' % (rot, len(achado_por_arq.get(rel, []))))
    for i, quais, ln in achado_por_arq.get(rel, []):
        corte = ln if len(ln) <= 78 else ln[:75] + '...'
        print('    L%-4d %-34s %s' % (i, '·'.join(quais), corte))
print()
print('  ⚠ E DUAS delas repetem frases que o item `5` já matou por medição:')
for pat, quem in ((r'não existe degrau acima da `Calamidade`', 'o item `5`'),
                  (r'vale \*\*\$\{X\.CAMBIO\} capangas\*\*', 'o item `9` — o câmbio é `8`')):
    m_ = re.search(pat, tm)
    print('    %s  %s' % ('ACHADA ' if m_ else 'sumiu  ', quem))
print()
print('  ⚠⚠ E o `make.js` L318 declara a `Calamidade` fora da faixa "porque exige SEIS feiticeiros".')
print('     Na escada viva quem exige seis é a `Catástrofe`; a `Calamidade` exige %d.'
      % round(VIVA['Calamidade']['fator'] * MESA))
print('     ⟹ a frase continua verdadeira e passa a apontar pro bicho ERRADO.')



# ═══════════════════════════════════════════ §10 · A DECISÃO, CONFERIDA
print()
print('=' * 92)
print('§10 · A DECISÃO DE 10/09 (noite), conferida contra a escada viva')
print('=' * 92)
DEC = os.path.join(BEST, '04-fase-1', 'fila', 'DECIDIDO-as-seis-prontas.md')
tdec = ler(DEC)


def limpa(c):
    return c.replace('###', '').replace('**', '').replace('`', '').strip()


DECIDIDO = []
for ln in tdec.split('\n'):
    cels = [limpa(c) for c in ln.strip().strip('|').split('|')]
    if len(cels) >= 5 and cels[0] in [n for n, _f, _c in SEIS]:
        DECIDIDO.append(dict(nome=cels[0], faixa=cels[1], de=cels[2], para=cels[3],
                             corpos=int(cels[4])))
exige(len(DECIDIDO) == len(SEIS),
      'a tabela §1 do `DECIDIDO-as-seis-prontas.md` mudou de forma (li %d de %d)'
      % (len(DECIDIDO), len(SEIS)))

print('  %-12s %-10s %-12s %-12s %7s %9s %9s %9s'
      % ('ficha', 'faixa', 'de', 'para', 'corpos', 'pontos', 'fatia', 'na banda?'))
mudou_faixa, fora_banda = [], []
for d in DECIDIDO:
    orig = [f for n, f, _c in SEIS if n == d['nome']][0]
    if d['faixa'] != orig:
        mudou_faixa.append((d['nome'], orig, d['faixa']))
    exige(d['para'] in VIVA, 'a ficha `%s` foi mandada pra `%s`, que não está na escada viva'
          % (d['nome'], d['para']))
    v = VIVA[d['para']]
    p = pontos(d['faixa'], v['fator'], v['acoes'])
    nv_ref = [f for f in FAIXAS if f['rot'] == d['faixa']][0]['de']
    fa = fatia(nv_ref, v['fator'], v['acoes'], d['para'] in TEM_INT)
    ok = BANDA[0] - 0.005 <= fa <= BANDA[1] + 0.005
    if not ok:
        fora_banda.append(d['nome'])
    print('  %-12s %-10s %-12s %-12s %7d %9.1f %8.1f%% %9s'
          % (d['nome'], d['faixa'], d['de'], d['para'], d['corpos'], p, 100 * fa,
             '✓' if ok else '⚠ NÃO'))
print()
exige(not fora_banda, 'a decisão põe %s fora da banda' % ', '.join(fora_banda))
print('  ✓ %d de %d fichas caem DENTRO da banda `%d%%`–`%d%%`.'
      % (len(DECIDIDO), len(DECIDIDO), 100 * BANDA[0], 100 * BANDA[1]))
for nome, de, para in mudou_faixa:
    print('  ⚡ `%s` mudou de FAIXA: `%s` ⟹ `%s`.' % (nome, de, para))

# a Kitsune: o número dela ainda é o publicado?
kit = [d for d in DECIDIDO if d['nome'] == 'Kitsune'][0]
p_kit = pontos(kit['faixa'], VIVA[kit['para']]['fator'], VIVA[kit['para']]['acoes'])
print('  ⚡ `Kitsune` na faixa `%s`: %.1f pontos, contra os %.1f que a ficha publica — %+.1f%%.'
      % (kit['faixa'], p_kit, KITSUNE_PTS, 100 * (p_kit / KITSUNE_PTS - 1)))
exige(p_kit >= PISO_SECO, 'a `Kitsune` decidida ficou SECA — a decisão não fecha')
exige(abs(p_kit / KITSUNE_PTS - 1) <= 0.02,
      'a `Kitsune` decidida não bate os `%.1f` pontos publicados' % KITSUNE_PTS)
print('     ✓ ela conjura, e a característica publicada dela não muda uma letra.')

# a Kamaitachi: o custo do encontro
kam = [d for d in DECIDIDO if d['nome'] == 'Kamaitachi'][0]
c_kam = cobra([(VIVA[kam['para']]['fator'], kam['corpos'])])
print('  ⚡ `Kamaitachi` — %d × `%s`: cobra %.1f%% contra %.1f%% da `Dupla` que ela era (%+.1f%%).'
      % (kam['corpos'], kam['para'], 100 * c_kam, 100 * alvo_c, 100 * (c_kam / alvo_c - 1)))

# a grade que sobra
print()
print('  E A GRADE QUE SOBRA — o preço declarado da decisão:')
faixas_usadas = sorted({d['faixa'] for d in DECIDIDO},
                       key=lambda r: [f['de'] for f in FAIXAS if f['rot'] == r][0])
COLS = ('Capanga', 'Ameaça', 'Desastre')
print('  %-10s %-26s %-26s %-26s' % ('faixa', *COLS))
vazias = 0
for fx in faixas_usadas:
    linha = [fx]
    for c in COLS:
        aqui = ['%s%s' % (d['nome'], ' ×%d' % d['corpos'] if d['corpos'] > 1 else '')
                for d in DECIDIDO if d['faixa'] == fx and d['para'] == c]
        if not aqui and fx in [f['rot'] for f in FAIXAS if f['de'] <= 8]:
            vazias += 1
            linha.append('⚠ vazio')
        else:
            linha.append(' · '.join(aqui) if aqui else '—')
    print('  %-10s %-26s %-26s %-26s' % tuple(linha))
print()
print('  ⟹ %d célula(s) da grade do nv `2` ao `8` ficam vazias, e todas são de `Capanga`.' % vazias)
print('    ⚠ Está DECLARADO no `DECIDIDO-as-seis-prontas.md` §5. Não é pendência, é o preço da `F`.')


print()
print('=' * 92)
print('✓ todas as âncoras de pé.')
print('=' * 92)

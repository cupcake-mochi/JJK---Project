# -*- coding: utf-8 -*-
"""MEDIDA — a peça 15 calibra a morte do shikigami contra o golpe da `Dupla`.

Achado em 10/09 (noite) respondendo "o que falta?" DE NOVO, depois que as seis
prontas fecharam.

A peça 15 §"A morte em definitivo" publica a régua do shikigami: ele morre de vez
se UM GOLPE causar a vida máxima do corpo. E ela não escolheu esse teto — ela o
MEDIU contra a tabela de golpe da peça 26, pelo MÁXIMO da rolagem.

  "Nenhum golpe comum destrói em definitivo […] Precisa do crítico da maior
   categoria da tabela."

A maior categoria da tabela dela é a `Dupla`. E a `Dupla` está morta.

  §0  as âncoras, todas lidas do dono
  §1  o teto da tabela — o que era, o que é
  §2  a tabela do §"morte em definitivo", recomputada na escada VIVA
  §3  a CONCLUSÃO da peça ainda vale?
  §4  a tabela do corpo já machucado, recomputada
  §5  ⚠ a frase "`Alcateia`, que é também o capanga"

⚠ Este script NÃO escreve nada no `Claude 2`. Ele só LÊ.
⚠ E ele NÃO é dono de nada: a peça 15 é do repositório, e este projeto só mede.

Nenhum número mora aqui dentro: cada âncora é lida do documento dono, e o script
morre se o dono mudar.
"""
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
BEST = os.path.dirname(os.path.dirname(AQUI))
REPO = os.environ.get('JJK_REPO', '/media/mizuki/HD Externo II/Claude/Claude 2')

P15 = os.path.join(REPO, 'sistema/03-mecanica/15-invocacoes.md')
TAB = os.path.join(BEST, '04-fase-1', 'TABELA.md')
DEC = os.path.join(BEST, '04-fase-1', 'fila', 'DECIDIDO-as-seis-prontas.md')


def ler(p):
    if not os.path.exists(p):
        sys.exit('DONO SUMIU: %s' % p)
    return open(p, encoding='utf-8').read()


def exige(c, m):
    if not c:
        sys.exit('✗ ÂNCORA PERDIDA: ' + m)


# ═══════════════════════════════════════════ o dado
def parse(e):
    m = re.match(r'(\d+)d(\d+)(?:\s*\+\s*(\d+))?$', e.strip())
    exige(m, 'expressão de dado que não sei ler: %r' % e)
    return int(m.group(1)), int(m.group(2)), int(m.group(3) or 0)


def maximo(e):
    n, d, mod = parse(e)
    return n * d + mod


def critico(e):
    """O crítico da peça 26: DOBRA os dados, o fixo não dobra — é a forma que a
    própria peça 15 imprime (`8d12 + 57` ⟹ `16d12 + 57`)."""
    n, d, mod = parse(e)
    return '%dd%d + %d' % (2 * n, d, mod) if mod else '%dd%d' % (2 * n, d)


def distribuicao(n, d):
    """Distribuição exata da soma de n dados de d lados."""
    dist = {0: 1.0}
    for _ in range(n):
        novo = {}
        for s, p in dist.items():
            for f in range(1, d + 1):
                novo[s + f] = novo.get(s + f, 0.0) + p / d
        dist = novo
    return dist


def p_alcanca(e, alvo):
    """Probabilidade de UMA rolagem de `e` alcançar `alvo`."""
    n, d, mod = parse(e)
    dist = distribuicao(n, d)
    return sum(p for s, p in dist.items() if s + mod >= alvo)


# ═══════════════════════════════════════════ §0 · AS ÂNCORAS
print('=' * 94)
print('§0 · AS ÂNCORAS — todas lidas do documento DONO')
print('=' * 94)

t15 = ler(P15)

# a régua, palavra por palavra
exige('A régua da morte é a vida máxima daquele corpo' in t15,
      'a régua da morte sumiu da peça 15')
exige('Ela morre de vez se um único golpe causar a régua inteira' in t15
      or 'morre de vez se **um único golpe** causar a régua inteira' in t15,
      'o gatilho de um golpe sumiu da peça 15')
print('  peça 15: "A régua da morte é a vida máxima daquele corpo."')
print('           "…morre de vez se UM ÚNICO GOLPE causar a régua inteira."')

# a tabela do §"morte em definitivo"
def celulas(ln):
    ln = ln.strip()
    if not ln.startswith('|'):
        return []
    return [c.strip() for c in ln.strip('|').split('|')]


def limpo(c):
    return c.replace('**', '').replace('`', '').strip()


T15 = []
for ln in t15.split('\n'):
    cels = celulas(ln)
    if len(cels) == 5 and re.match(r'^`\d+d\d+', cels[1]) and re.match(r'^`\d+`$', cels[2]):
        T15.append(dict(rot=limpo(cels[0]), exp=limpo(cels[1]),
                        maxi=int(limpo(cels[2])), coro=limpo(cels[3]), forte=limpo(cels[4])))
# Na v0.221 a tabela passou a AGRUPAR categorias de mesmo golpe (`Capanga` e `Ameaça`
# numa linha, `Desastre` e `Calamidade` noutra), e foi de 5 linhas para 4. O número de
# linhas não é âncora: quem manda é a escada, e o §1 confere linha a linha contra ela.
exige(len(T15) >= 2, 'a tabela da morte em definitivo sumiu ou mudou de forma (li %d linhas)'
      % len(T15))

m = re.search(r'Os corpos valem `(\d+)` e `(\d+)`', t15)
exige(m, 'os valores dos dois corpos sumiram da peça 15')
CORO, FORTE = int(m.group(1)), int(m.group(2))
print('  peça 15: os dois corpos do nv30 valem `%d` (Coro, Con 1) e `%d` (forte)' % (CORO, FORTE))

exige('Nenhum golpe comum destrói em definitivo' in t15,
      'a conclusão "nenhum golpe comum destrói" sumiu da peça 15')
# v0.221: a frase era "Precisa do crítico da maior categoria da tabela". Com a escada
# viva o crítico do topo NÃO alcança mais o corpo forte, e a peça passou a dizer o que
# ele alcança e o que não alcança, em vez de uma exigência só.
m = re.search(r'O crítico da maior categoria da tabela destrói o corpo do `Coro` e não '
              r'destrói o corpo forte', t15)
exige(m, 'a frase da conclusão do crítico sumiu da peça 15')
print('  peça 15: "Nenhum golpe comum destrói em definitivo […] O crítico da maior')
print('            categoria destrói o corpo do `Coro` e NÃO destrói o corpo forte."')

# a tabela do corpo já machucado
MACHUCADO = []
for ln in t15.split('\n'):
    cels = celulas(ln)
    if len(cels) == 3 and limpo(cels[0]) in ('cheio', 'na metade', 'em um quarto',
                                             'a um ponto de cair'):
        MACHUCADO.append((limpo(cels[0]), int(limpo(cels[1])), limpo(cels[2])))
exige(len(MACHUCADO) == 4, 'a tabela do corpo machucado mudou de forma (li %d)' % len(MACHUCADO))
print('  peça 15: a tabela do corpo já machucado — %d linhas' % len(MACHUCADO))

# a escada VIVA, na TABELA.md
ttab = ler(TAB)
VIVAS = {}
for cat in ('Capanga', 'Ameaça', 'Desastre', 'Catástrofe', 'Calamidade'):
    exige('## `%s`' % cat in ttab, 'a seção `%s` sumiu da TABELA' % cat)
    sec = ttab.split('## `%s`' % cat)[1].split('\n## ')[0]
    col = 'golpe de um' if cat == 'Capanga' else 'o golpe'
    cab, achou = None, None
    for ln in sec.split('\n'):
        cels = [c.strip().strip('*').strip('`').strip('*') for c in ln.strip().strip('|').split('|')]
        if cels and cels[0] == 'nv':
            cab = cels
        elif cab and cels and cels[0] == '30':
            achou = dict(zip(cab, cels))[col].strip()
    exige(achou, 'não achei o golpe do nv30 de `%s`' % cat)
    VIVAS[cat] = achou
print('  `TABELA.md` nv30: ' + ' · '.join('%s `%s`' % (k, v) for k, v in VIVAS.items()))

# e a decisão de hoje, pra saber que a `Dupla` está morta mesmo
tdec = ler(DEC)
exige('DECIDIDO — o item `30`' in tdec, 'o `DECIDIDO-as-seis-prontas.md` mudou de forma')
exige('Dupla' in tdec, 'a `Dupla` sumiu do DECIDIDO')
print('  `DECIDIDO-as-seis-prontas.md`: a `Dupla` saiu da escada em 10/09 (noite).')

# ── a virada: até a v0.220 a peça 15 publicava a escada MORTA e este script PREVIA a
# viva. Desde a v0.221 ela publica a viva — então dá pra CONFERIR em vez de prever.
PUB_COMUNS = sorted({r['exp'] for r in T15 if 'crítico' not in r['rot']}, key=maximo)
EXP_VIVAS = sorted(set(VIVAS.values()), key=maximo)
exige(PUB_COMUNS == EXP_VIVAS,
      'as linhas comuns da peça 15 não são as da escada viva: ela publica %s e a '
      'TABELA dá %s' % (PUB_COMUNS, EXP_VIVAS))
print('  ✓ as %d expressões comuns da peça 15 são exatamente as da escada viva no nv30.'
      % len(PUB_COMUNS))


# ═══════════════════════════════════════════ §1 · O TETO DA TABELA
print()
print('=' * 94)
print('§1 · O TETO DA TABELA — o que a peça 15 mediu, e o que existe hoje')
print('=' * 94)
comuns = [r for r in T15 if 'crítico' not in r['rot']]
topo_pub = max(comuns, key=lambda r: r['maxi'])
print('  A tabela da peça 15, como está publicada (nv30):')
print('  %-38s %-14s %8s %10s %10s' % ('linha', 'expressão', 'máximo', 'Coro', 'forte'))
for r in T15:
    marca = ' ← o TETO' if r is topo_pub else ''
    print('  %-38s %-14s %8d %10s %10s%s'
          % (r['rot'], r['exp'], r['maxi'], r['coro'], r['forte'], marca))
    exige(maximo(r['exp']) == r['maxi'],
          'o máximo publicado de `%s` (%d) não bate com a expressão (%d)'
          % (r['exp'], r['maxi'], maximo(r['exp'])))
print()
print('  ✓ os %d máximos publicados batem com as expressões. A tabela é consistente por dentro.'
      % len(T15))
print()
topo_vivo_cat = max(VIVAS, key=lambda c: maximo(VIVAS[c]))
TOPO_VIVO = VIVAS[topo_vivo_cat]
print('  E o teto da escada VIVA, no mesmo nível:')
for c, e in sorted(VIVAS.items(), key=lambda kv: -maximo(kv[1])):
    print('    %-12s `%-10s` máximo %3d%s' % (c, e, maximo(e),
                                              '  ← o TETO VIVO' if e == TOPO_VIVO else ''))
print()
exige(topo_pub['exp'] == TOPO_VIVO,
      'o teto publicado na peça 15 (`%s`) não é o teto da escada viva (`%s`)'
      % (topo_pub['exp'], TOPO_VIVO))
print('  ⟹ o teto publicado é `%s` (%d), e é o MESMO da escada viva.'
      % (topo_pub['exp'], topo_pub['maxi']))
print('    A linha que a peça chama de "o maior golpe da tabela" é a `%s`.' % topo_pub['rot'])
print('    ⚠ Até a v0.220 aqui estava a `Dupla`, com máximo `153` — 1,51× o teto de hoje.')


# ═══════════════════════════════════════════ §2 · A TABELA RECOMPUTADA
print()
print('=' * 94)
print('§2 · A TABELA DA MORTE, RECOMPUTADA NA ESCADA VIVA')
print('=' * 94)
print('  A régua: um golpe destrói se o MÁXIMO da rolagem alcança a vida do corpo.')
print('  Corpos: `Coro` Con 1 = %d · forte = %d.' % (CORO, FORTE))
print()
print('  %-32s %-14s %8s %12s %12s' % ('a linha viva', 'expressão', 'máximo',
                                       'Coro (%d)' % CORO, 'forte (%d)' % FORTE))
LINHAS_VIVAS = []
for c, e in sorted(VIVAS.items(), key=lambda kv: maximo(kv[1])):
    LINHAS_VIVAS.append((c, e))
crit_vivo = critico(TOPO_VIVO)
for c, e in LINHAS_VIVAS:
    print('  %-32s %-14s %8d %12s %12s'
          % ('`%s`' % c, e, maximo(e),
             'destrói' if maximo(e) >= CORO else 'cai',
             'destrói' if maximo(e) >= FORTE else 'cai'))
print('  %-32s %-14s %8d %12s %12s'
      % ('**crítico do topo (`%s`)**' % topo_vivo_cat, crit_vivo, maximo(crit_vivo),
         'DESTRÓI' if maximo(crit_vivo) >= CORO else 'cai',
         'DESTRÓI' if maximo(crit_vivo) >= FORTE else '⚠ CAI'))
print()
crit_pub = [r for r in T15 if 'crítico' in r['rot']][0]
print('  E a linha de crítico que a peça publica, pra CONFERIR:')
print('  %-32s %-14s %8d %12s %12s'
      % (crit_pub['rot'], crit_pub['exp'], crit_pub['maxi'],
         crit_pub['coro'], crit_pub['forte']))
exige(crit_pub['exp'] == crit_vivo,
      'o crítico publicado (`%s`) não é o crítico do topo vivo (`%s`)'
      % (crit_pub['exp'], crit_vivo))
for r in T15:
    esperado = (('destrói' if maximo(r['exp']) >= CORO else 'cai'),
                ('destrói' if maximo(r['exp']) >= FORTE else 'cai'))
    exige((r['coro'].lower(), r['forte'].lower()) == esperado,
          'a linha `%s` publica %s/%s e a conta devolve %s/%s'
          % (r['rot'], r['coro'], r['forte'], esperado[0], esperado[1]))
print('  ✓ o crítico publicado é o do topo vivo, e os %d veredictos da tabela reproduzem.'
      % len(T15))


# ═══════════════════════════════════════════ §3 · A CONCLUSÃO AINDA VALE?
print()
print('=' * 94)
print('§3 · A CONCLUSÃO DA PEÇA — a conta devolve o que ela publica?')
print('=' * 94)
print('  A peça 15 conclui, palavra por palavra:')
print('    "Nenhum golpe comum destrói em definitivo, e a razão vale em todo nível."')
print('    "O crítico da maior categoria da tabela destrói o corpo do `Coro` e não')
print('     destrói o corpo forte — com a escada viva da peça 26, nenhum golpe único')
print('     destrói o corpo forte."')
print()
comum_max = max(maximo(e) for e in VIVAS.values())
metade_1 = comum_max < CORO
metade_2 = comum_max < FORTE
print('  metade `1` — "nenhum golpe COMUM destrói":')
print('    o maior golpe comum vivo é %d; o Coro vale %d e o forte %d.' % (comum_max, CORO, FORTE))
print('    ⟹ %s' % ('✅ CONTINUA VALENDO, e com mais folga que antes.'
                    if (metade_1 and metade_2) else '⚠ NÃO vale mais.'))
print()
print('  metade `2` — o que o crítico da maior categoria alcança:')
ok_coro = maximo(crit_vivo) >= CORO
ok_forte = maximo(crit_vivo) >= FORTE
print('    o crítico do topo vivo (`%s`) alcança %d.' % (crit_vivo, maximo(crit_vivo)))
print('    contra o `Coro` (%d): %s' % (CORO, '✅ destrói' if ok_coro else '❌ NÃO destrói'))
print('    contra o corpo forte (%d): %s' % (FORTE, '✅ destrói' if ok_forte else '❌ NÃO DESTRÓI'))
print()
# v0.221: era aqui que este script ACENDIA — a peça publicava que o crítico da `Dupla`
# destruía OS DOIS corpos. O Mizuki escolheu REGISTRAR a régua frouxa em vez de encolher
# o corpo forte, e a peça passou a dizer isso. Agora o script confere o registro.
exige(ok_coro and not ok_forte,
      'a conta mudou: o crítico do topo %s o `Coro` e %s o corpo forte — a peça 15 '
      'publica destrói/cai' % ('destrói' if ok_coro else 'NÃO destrói',
                               'destrói' if ok_forte else 'não destrói'))
exige('nenhum golpe único destrói o corpo forte' in t15,
      'a peça 15 parou de registrar que nenhum golpe único destrói o corpo forte')
print('  ### ⟹ ✅ A CONCLUSÃO PUBLICADA REPRODUZ, e a régua frouxa está REGISTRADA.')
print('    Nada no jogo destrói um corpo forte com um golpe único — nem o crítico do topo.')
print('    Decisão do Mizuki na v0.221: registrar, em vez de encolher o corpo forte.')
print()
print('    ⟹ a morte definitiva do corpo forte virou coisa quase só do gatilho do')
print('      excedente, com o corpo já machucado — e o §4 mede ele.')


# ═══════════════════════════════════════════ §4 · O CORPO MACHUCADO
print()
print('=' * 94)
print('§4 · A TABELA DO CORPO JÁ MACHUCADO, RECOMPUTADA')
print('=' * 94)
print('  A peça publica esta tabela pro `Coro` de Con `1` no nv30 (vida %d):' % CORO)
print()
print('  %-24s %14s %26s' % ('o corpo', 'precisa de',
                             'o topo (`%s`) alcança?' % TOPO_VIVO))
mudou = []
for rot, precisa, publicado in MACHUCADO:
    p_morto = p_alcanca(topo_pub['exp'], precisa)
    p_vivo = p_alcanca(TOPO_VIVO, precisa)
    lido_morto = ('não' if p_morto == 0 else
                  'sempre' if p_morto >= 0.9995 else '%.0f%% das rolagens' % (100 * p_morto))
    lido_vivo = ('não' if p_vivo == 0 else
                 'sempre' if p_vivo >= 0.9995 else '%.0f%% das rolagens' % (100 * p_vivo))
    if lido_morto != lido_vivo:
        mudou.append((rot, publicado, lido_vivo))
    print('  %-24s %14d %26s' % (rot, precisa, lido_vivo))
    exige(lido_morto.startswith(publicado.split()[0][:3]) or publicado.startswith(lido_morto[:3]),
          'a linha `%s` da peça publica %r e a conta devolve %r — o dono mudou'
          % (rot, publicado, lido_morto))
print()
print('  ✓ as %d linhas publicadas reproduzem com o topo vivo `%s`.'
      % (len(MACHUCADO), TOPO_VIVO))
print('    ⟹ a tabela FOI recalculada na escada viva. Não é coincidência de leitura.')
print()
if mudou:
    print('  ⚠ E %d de %d linhas MUDAM na escada viva:' % (len(mudou), len(MACHUCADO)))
    for rot, antes, depois in mudou:
        print('    · `%s`: publicado "%s" ⟹ medido "%s"' % (rot, antes, depois))


# ═══════════════════════════════════════════ §5 · A FRASE
print()
print('=' * 94)
print('§5 · A frase `Alcateia, que é também o capanga` — ela saiu da peça?')
print('=' * 94)
m = re.search(r'\|\s*`Alcateia`, que é também o capanga\s*\|', t15)
if m:
    print('  A peça 15 imprime, na tabela da morte:')
    print('      "`Alcateia`, que é também o capanga"')
    print()
    print('  ⚠ E a peça 26 §4.3 diz o contrário, com todas as letras:')
    print('      "É por isso que o capanga do manual NÃO É uma `Ronda`."')
    print('    A `Alcateia` é fator `1,00` e o capanga do manual é `chefe ÷ 4` / `chefe ÷ 3`.')
    print('    ⟹ é a MESMA confusão que a `MEDIDA-o-remapeamento-das-seis.md` corrigiu hoje,')
    print('      e aqui ela está numa PEÇA DE REGRA, não num arquivo de estado.')
else:
    print('  a frase "`Alcateia`, que é também o capanga" não está mais lá.')

print()
print('=' * 94)
print('✓ todas as âncoras de pé.')
print('=' * 94)

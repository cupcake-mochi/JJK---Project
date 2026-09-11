# ROTA B — o orcamento de feitico de uma acao sai do golpe IMPRESSO pela ficha.
#
# A peca 26 §6.5 escreve embaixo da tabela: "O golpe entra aqui como a ficha imprime
# ele — a media do dado do §4.4 —, e quem carrega `Intervencao` entra ja com o fator
# dela." A tabela publicada, e a checagem 9.1, faziam a conta A (o fator DEPOIS da
# media do golpe cru). Medido em 11/09/2026 — `04-fase-1/fila/medir-a-rota-do-orcamento.py`,
# saida em `SAIDA-a-rota-do-orcamento.txt` — e a rota B e a validada.
#
# Este script NAO digita numero: ele reabre os donos, refaz as 35 celulas pela rota B
# e reescreve os tres lugares que publicam a conta. Morre se uma ancora sumir.
#
#   dono da linha de dano       manual/gerador/partF.js, tabela `Inimigos`
#   dono da categoria           peca 26 §4 (fator, acoes, carrega Intervencao)
#   dono do fator 0,923         peca 26 §6.5
#   dono do piso da Classe 1    peca 26 §6.5
#   dono do dado()              gerador-inimigo/make.js (DADOS, piso, teto, e a ORDEM)
import re, math, sys
from decimal import Decimal, ROUND_HALF_UP

R = '/media/mizuki/HD Externo II/Claude/Claude 2'
B = '/media/mizuki/HD Externo II/Claude/Claude 2/bestiario'
P26 = f'{R}/sistema/03-mecanica/26-bestiario.md'
PVAL = f'{R}/sistema/03-mecanica/conferir-bestiario.py'
P60 = f'{B}/08-livro/capitulos/60-a-montagem.md'

def ler(p): return open(p, encoding='utf-8').read()
def morre(m): sys.exit('✗ ÂNCORA PERDIDA: ' + m)

pf = ler(f'{R}/manual/gerador/partF.js'); t26 = ler(P26)
mk = ler(f'{R}/sistema/05-material/gerador-inimigo/make.js')

LIN = {int(n): int(cd) for n, cd in re.findall(r"\['(\d+)', '~\d+', '\d+ a \d+', '(\d+)', '\d+', '\d+'\]", pf)}
if len(LIN) != 7: morre('tabela Inimigos do partF.js (%d linhas)' % len(LIN))
CAT = []
for nome, pes, fat, ac, it in re.findall(r"\| \*\*`(\w+)`\*\* \| (—|\d+) \| `× ([\d,]+)` \| `(\d+)` \| (sim|não) \|", t26):
    CAT.append((nome, float(fat.replace(',', '.')), int(ac), it == 'sim'))
if len(CAT) != 5: morre('tabela de categorias do §4 (%d)' % len(CAT))
m = re.search(r'é multiplicado por `([\d,]+)`', t26) or morre('o fator da Intervenção')
F = float(m.group(1).replace(',', '.'))
m = re.search(r'custa `(\d+)` pontos\*\*, que são `([\d,]+)` de dano', t26) or morre('o piso da Classe 1')
PISO_PT = int(m.group(1)); PT = float(m.group(2).replace(',', '.')) / PISO_PT
DADOS = [int(x) for x in re.search(r'const DADOS = \[([\d,\s]+)\]', mk).group(1).split(',')]
PISO_D = int(re.search(r'if \(alvo < (\d+)\) return String\(arred\(alvo\)\)', mk).group(1))
TETO = int(re.search(r'if \(n > (\d+)\) continue', mk).group(1))
if 'return c[4] ? arred(r * X.FATOR_INTERVENCAO) : r;' not in mk:
    morre('a ORDEM da conta do golpe no make.js — a rota B depende dela')

arred = lambda x: math.ceil(x - 0.5)
jsr = lambda x: math.floor(x + 0.5)

def dado(alvo):
    if alvo < PISO_D: return str(arred(alvo))
    meta, bom = alvo / 2, None
    for d in DADOS:
        med = (d + 1) / 2; n = max(1, jsr(meta / med))
        if n > TETO: continue
        fixo = alvo - n * med
        if fixo < 0: continue
        inteiro = 0 if abs(fixo - jsr(fixo)) < 1e-9 else 1; er = abs(n * med - meta)
        if bom is None or inteiro < bom[0] or (inteiro == bom[0] and er < bom[1] - 1e-9) \
           or (inteiro == bom[0] and abs(er - bom[1]) < 1e-9 and n < bom[2]):
            bom = (inteiro, er, n, d, jsr(fixo))
    if bom is None:
        n = max(1, jsr(alvo / 9)); r = arred(alvo - 4.5 * n)
        return f'{n}d8 + {r}' if r > 0 else f'{n}d8'
    return f'{bom[2]}d{bom[3]} + {bom[4]}' if bom[4] > 0 else f'{bom[2]}d{bom[3]}'

def media(e):
    m = re.match(r'(\d+)d(\d+)(?: \+ (\d+))?$', e)
    return int(m.group(1)) * (int(m.group(2)) + 1) / 2 + int(m.group(3) or 0) if m else float(e)

def fmt(p):
    if p < PISO_PT - 1e-9: return 'seco'
    return str(Decimal(repr(p)).quantize(Decimal('0.1'), ROUND_HALF_UP)).replace('.', ',')

# ── as 35 celulas pela rota B
CEL, PTS = {}, {}
for nv in sorted(LIN):
    CEL[nv], PTS[nv] = [], []
    for nome, fat, ac, it in CAT:
        rod = arred(LIN[nv] * fat)
        imp = dado(arred(rod * F) / ac) if it else dado(rod / ac)
        p = media(imp) / PT
        CEL[nv].append(fmt(p)); PTS[nv].append(p)

topo = max(PTS[30]); i_topo = [i for i, p in enumerate(PTS[30]) if abs(p - topo) < 1e-9]
TOPO = fmt(topo)
NOMES_TOPO = [CAT[i][0] for i in i_topo]

# o teto do jogador sai da propria frase da peca
m = re.search(r'o teto do jogador naquele nível é `(\d+)`', t26) or morre('o teto do jogador na frase do §6.5')
TETO_J = int(m.group(1))
PCT = int(Decimal(repr(topo / TETO_J * 100)).quantize(Decimal('1'), ROUND_HALF_UP))

def fmt_num(x):
    return str(Decimal(repr(x)).quantize(Decimal('0.1'), ROUND_HALF_UP)).replace('.', ',')

def cels_md(nv, cru):
    return ' | '.join(c if c == 'seco' else f'`{c}`' for c in CEL[nv])

def troca(t, old, new, onde):
    if t.count(old) != 1: morre('%s — %d ocorrência(s): %r' % (onde, t.count(old), old[:80]))
    return t.replace(old, new)

# ── 1 · a tabela e a frase do topo, na peca 26
t = t26
for nv in sorted(LIN):
    velho = re.search(r'\| nível %d \|(?:[^\n|]*\|){5}' % nv, t)
    if not velho: morre('linha "nível %d" da tabela do §6.5' % nv)
    t = troca(t, velho.group(0), '| nível %d | %s |' % (nv, cels_md(nv, 0)), 'tabela §6.5 nv %d' % nv)

velha = re.search(r'\*\*A maior ação de inimigo do sistema é `[\d,]+` pontos — [^*]*?—, e o teto do jogador naquele nível é `\d+`\.\*\* \*Uma ação de inimigo é `\d+%`', t)
if not velha: morre('a frase da maior ação do §6.5')
lista = ' e '.join('`%s`' % n for n in NOMES_TOPO)
nova = ('**A maior ação de inimigo do sistema é `%s` pontos — o %s do nível 30 —, e o teto do '
        'jogador naquele nível é `%d`.** *Uma ação de inimigo é `%d%%`' % (TOPO, lista, TETO_J, PCT))
t = t.replace(velha.group(0), nova)
open(P26, 'w', encoding='utf-8').write(t)

# ── 2 · a mesma tabela no capitulo 6 do livro
t60 = ler(P60)
for nv in sorted(LIN):
    velho = re.search(r'\| `%d` \|(?:[^\n|]*\|){5}' % nv, t60)
    if not velho: morre('linha `%d` da tabela do capítulo 6' % nv)
    t60 = troca(t60, velho.group(0), '| `%d` | %s |' % (nv, cels_md(nv, 0)), 'tabela cap 6 nv %d' % nv)
# a `Condição na maior ação`: o topo menos o preço de cada Classe da peça 19 §2.1
P19 = f'{R}/sistema/03-mecanica/19-dano-e-condicoes.md'
t19 = ler(P19)
mcl = re.search(r'\n\| 7 \| (\d+) \| (\d+) \| (\d+) \|', t19)
if not mcl: morre('a linha da Classe 7 da tabela de preço de condição, peça 19 §2.1')
CUSTO = dict(zip(('Leve', 'Média', 'Pesada'), (int(x) for x in mcl.groups())))

velho = re.search(r'O que cabe n[^\n]*maior do sistema[^\n]*:', t60)
if not velho: morre('a frase que abre a `Condição na maior ação` no capítulo 6')
t60 = t60.replace(velho.group(0),
                  'O que cabe na maior ação do sistema, a de `%s` pontos:' % TOPO)
for cl in ('Leve', 'Média', 'Pesada'):
    velho = re.search(r'\| uma condição `%s` \| `\d+` \| `[\d,]+` \|' % cl, t60)
    if not velho: morre('a linha `%s` da `Condição na maior ação`' % cl)
    sobra = fmt_num(topo - CUSTO[cl])
    t60 = t60.replace(velho.group(0),
                      '| uma condição `%s` | `%d` | `%s` |' % (cl, CUSTO[cl], sobra))

open(P60, 'w', encoding='utf-8').write(t60)

# ── 3 · a checagem 9.1 passa a fazer a rota B
tv = ler(PVAL)
velho = ("                _g91 = (_media_do_dado(_arr(_cd91 * _c91[2]) / _c91[3])\n"
         "                        * (_FI if _INT.get(_c91[0]) else 1.0))\n")
novo = ("                # rota B: o fator entra no dano de RODADA, antes do dado — e' o\n"
        "                # golpe que a ficha imprime, que e' o que o texto do §6.5 descreve\n"
        "                _rod91 = _arr(_cd91 * _c91[2])\n"
        "                if _INT.get(_c91[0]):\n"
        "                    _rod91 = _arr(_rod91 * _FI)\n"
        "                _g91 = _media_do_dado(_rod91 / _c91[3])\n")
tv = tv if novo in tv else troca(tv, velho, novo, 'a conta da checagem 9.1')
velho2 = ("    # v0.221: o golpe entra como a ficha imprime ele — a MEDIA do dado do §4.4 — e\n"
          "    # quem carrega `Intervencao` entra com o fator dela.")
novo2 = ("    # v0.221: o golpe entra como a ficha imprime ele — a MEDIA do dado do §4.4 — e\n"
         "    # quem carrega `Intervencao` entra com o fator dela.\n"
         "    # 11/09/2026: a conta era a rota A (o fator DEPOIS da media do golpe cru), e o\n"
         "    # texto da peca descrevia a rota B. Medido em `medir-a-rota-do-orcamento.py`:\n"
         "    # a rota B fecha com o texto, com o comentario daqui e com a regra do cap. 6 do\n"
         "    # livro aplicada ao golpe que a mesa le. 9 das 35 celulas andaram 0,1.")
tv = tv if novo2 in tv else troca(tv, velho2, novo2, 'o comentario da 9.1')
open(PVAL, 'w', encoding='utf-8').write(tv)

print('fator %s · 1 ponto = %s de dano · piso %d pontos' % (F, PT, PISO_PT))
print('%-4s %s' % ('nv', ' '.join('%-11s' % c[0] for c in CAT)))
for nv in sorted(LIN):
    print('%-4d %s' % (nv, ' '.join('%-11s' % c for c in CEL[nv])))
print('\n✓ peça 26 §6.5, capítulo 6 do livro e a checagem 9.1 reescritos pela rota B')
print('✓ a maior ação: %s pontos (%s), %d%% do teto de %d do jogador' % (TOPO, lista, PCT, TETO_J))

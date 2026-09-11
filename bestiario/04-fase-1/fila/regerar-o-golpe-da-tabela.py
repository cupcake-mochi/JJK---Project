# A coluna `o golpe` da TABELA.md sai do dado() do make.js, e nao do round() do Python.
#
# Achado do agente dos blocos (11/09/2026): tres celulas da `Catastrofe` divergiam do
# gerador. A causa e o meio-ponto: `Math.round` do JS sobe (2,5 -> 3) e o `round` do
# Python vai pro PAR (2,5 -> 2). O dono do golpe e o make.js — e o gerador de bloco, o
# `gerar-as-seis.py` e a checagem 9.1 ja fazem a conta dele.
#
# Sem `--escrever` ele so' CONFERE e morre se divergir. Este script refaz a coluna inteira das 5 categorias x 29 niveis a partir de
# `dano/rod` e `acoes` da propria TABELA, com o dado() portado do make.js, e reescreve
# so' o que diverge. Morre se uma ancora sumir.
import os, re, math, sys

BEST = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
REPO = os.environ.get('JJK_REPO', '/media/mizuki/HD Externo II/Claude/Claude 2')
TAB = os.path.join(BEST, '04-fase-1', 'TABELA.md')
MAKE = os.path.join(REPO, 'sistema/05-material/gerador-inimigo/make.js')

def morre(m): sys.exit('✗ ÂNCORA PERDIDA: ' + m)
def ler(p):
    if not os.path.exists(p): morre('não existe: %s' % p)
    return open(p, encoding='utf-8').read()

mk = ler(MAKE)
_m = re.search(r'const DADOS = \[([\d,\s]+)\]', mk) or morre('o DADOS do make.js')
DADOS = [int(x) for x in _m.group(1).split(',')]
_m = re.search(r'if \(alvo < (\d+)\) return String\(arred\(alvo\)\)', mk) or morre('o piso do dado no make.js')
PISO = int(_m.group(1))
_m = re.search(r'if \(n > (\d+)\) continue', mk) or morre('o teto de dados no make.js')
TETO = int(_m.group(1))
if 'Math.round' not in mk:
    morre('o make.js parou de usar Math.round — o meio-ponto deste script vem de lá')

arred = lambda x: math.ceil(x - 0.5)
jsr = lambda x: math.floor(x + 0.5)          # Math.round do JS: o meio SOBE

def dado(alvo):
    if alvo < PISO: return str(arred(alvo))
    meta, bom = alvo / 2, None
    for d in DADOS:
        med = (d + 1) / 2
        n = max(1, jsr(meta / med))
        if n > TETO: continue
        fixo = alvo - n * med
        if fixo < 0: continue
        inteiro = 0 if abs(fixo - jsr(fixo)) < 1e-9 else 1
        er = abs(n * med - meta)
        if bom is None or inteiro < bom[0] or (inteiro == bom[0] and er < bom[1] - 1e-9) \
           or (inteiro == bom[0] and abs(er - bom[1]) < 1e-9 and n < bom[2]):
            bom = (inteiro, er, n, d, jsr(fixo))
    if bom is None:
        n = max(1, jsr(alvo / 9)); r = arred(alvo - 4.5 * n)
        return '%dd8 + %d' % (n, r) if r > 0 else '%dd8' % n
    return ('%dd%d + %d' % bom[2:]) if bom[4] > 0 else '%dd%d' % (bom[2], bom[3])

t = ler(TAB)
LINHA = re.compile(r'^\| (\d+) \| `(\d+)` \| `(\d+)` \| `(\d+)` \| `([^`]+)` \|', re.M)
cat, mudou, conferidas = None, [], 0
saida = []
for ln in t.split('\n'):
    mc = re.match(r'^## `(\w+)`', ln)
    if mc: cat = mc.group(1)
    m = LINHA.match(ln)
    if not m:
        saida.append(ln); continue
    nv, vida, rod, ac, velho = m.group(1), m.group(2), int(m.group(3)), int(m.group(4)), m.group(5)
    novo = dado(rod / ac)
    conferidas += 1
    if novo != velho:
        mudou.append((cat, int(nv), velho, novo))
        ln = ln.replace('| `%s` |' % velho, '| `%s` |' % novo, 1)
    saida.append(ln)

if not conferidas: morre('não reconheci nenhuma linha de faixa na TABELA.md')

# A fila e' de MEDIDA: rodar ela nunca mexe num dono. Sem `--escrever` este script
# so' confere, e morre se divergir — que e' o que a rodada da fila quer saber.
ESCREVE = '--escrever' in sys.argv

print('dados %s · seco abaixo de %d · teto %d dados · meio-ponto PRA CIMA (Math.round)'
      % (DADOS, PISO, TETO))
print('%d célula(s) conferida(s) contra o dado() do make.js' % conferidas)
if not mudou:
    print('✓ nenhuma diverge — a TABELA já publica o golpe do gerador')
elif ESCREVE:
    open(TAB, 'w', encoding='utf-8').write('\n'.join(saida))
    for c, nv, v, n in mudou:
        print('  ⟹ %-11s nv %-2d  %-12s ⟹ %s' % (c, nv, v, n))
    print('✓ %d célula(s) reescrita(s)' % len(mudou))
else:
    for c, nv, v, n in mudou:
        print('  ⚠ %-11s nv %-2d  TABELA %-12s make.js %s' % (c, nv, v, n))
    morre('%d célula(s) da TABELA não são o golpe do gerador. '
          'Rode com `--escrever` pra acertar.' % len(mudou))

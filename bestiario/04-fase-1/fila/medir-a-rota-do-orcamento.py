# As duas contas do orcamento de feitico de uma acao, nas 35 celulas da peca 26 §6.5.
#   A: media do golpe CRU x 0,923 / 4,5      (o fator depois da media)
#   B: media do golpe IMPRESSO / 4,5         (o fator antes do dado, como o make.js imprime)
# Toda ancora lida do dono: partF.js (a tabela Inimigos), peca 26 (§4, §6.5, o piso da Classe 1)
# e o make.js (DADOS, piso e teto do dado). Morre se uma ancora sumir.
import re, math, sys
from decimal import Decimal, ROUND_HALF_UP
R = '/media/mizuki/HD Externo II/Claude/Claude 2'
def ler(p): return open(f'{R}/{p}', encoding='utf-8').read()
def morre(m): sys.exit('ANCORA PERDIDA: ' + m)
pf = ler('manual/gerador/partF.js'); t26 = ler('sistema/03-mecanica/26-bestiario.md'); mk = ler('sistema/05-material/gerador-inimigo/make.js')
LIN = {int(n): int(cd) for n, cd in re.findall(r"\['(\d+)', '~\d+', '\d+ a \d+', '(\d+)', '\d+', '\d+'\]", pf)}
if len(LIN) != 7: morre('tabela Inimigos do partF.js (%d linhas)' % len(LIN))
CAT = []
for nome, pes, fat, ac, it in re.findall(r"\| \*\*`(\w+)`\*\* \| (—|\d+) \| `× ([\d,]+)` \| `(\d+)` \| (sim|não) \|", t26):
    CAT.append((nome, float(fat.replace(',', '.')), int(ac), it == 'sim'))
if len(CAT) != 5: morre('tabela de categorias do §4 (%d)' % len(CAT))
m = re.search(r'é multiplicado por `([\d,]+)`', t26) or morre('o fator da Intervencao')
F = float(m.group(1).replace(',', '.'))
m = re.search(r'custa `(\d+)` pontos\*\*, que são `([\d,]+)` de dano', t26) or morre('o piso da Classe 1')
PISO_PT = int(m.group(1)); PT = float(m.group(2).replace(',', '.')) / PISO_PT
DADOS = [int(x) for x in re.search(r'const DADOS = \[([\d,\s]+)\]', mk).group(1).split(',')]
PISO_D = int(re.search(r'if \(alvo < (\d+)\) return String\(arred\(alvo\)\)', mk).group(1))
TETO = int(re.search(r'if \(n > (\d+)\) continue', mk).group(1))
if 'return c[4] ? arred(r * X.FATOR_INTERVENCAO) : r;' not in mk: morre('a ordem da conta do golpe no make.js')
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
        inteiro = 0 if abs(fixo - jsr(fixo)) < 1e-9 else 1; erro = abs(n * med - meta)
        if bom is None or inteiro < bom[0] or (inteiro == bom[0] and erro < bom[1] - 1e-9) or (inteiro == bom[0] and abs(erro - bom[1]) < 1e-9 and n < bom[2]):
            bom = (inteiro, erro, n, d, jsr(fixo))
    if bom is None:
        n = max(1, jsr(alvo / 9)); r = arred(alvo - 4.5 * n); return f'{n}d8 + {r}' if r > 0 else f'{n}d8'
    return f'{bom[2]}d{bom[3]} + {bom[4]}' if bom[4] > 0 else f'{bom[2]}d{bom[3]}'
def media(e):
    m = re.match(r'(\d+)d(\d+)(?: \+ (\d+))?$', e)
    return int(m.group(1)) * (int(m.group(2)) + 1) / 2 + int(m.group(3) or 0) if m else float(e)
def fmt(p):
    if p < PISO_PT - 1e-9: return 'seco'
    return str(Decimal(repr(p)).quantize(Decimal('0.1'), ROUND_HALF_UP)).replace('.', ',')
# a tabela publicada no §6.5
PUB = {}
for nv, *cels in re.findall(r"\| nível (\d+) \| (seco|`[\d,]+`) \| (seco|`[\d,]+`) \| (seco|`[\d,]+`) \| (seco|`[\d,]+`) \| (seco|`[\d,]+`) \|", t26):
    PUB[int(nv)] = [c.strip('`') for c in cels]
if len(PUB) != 7: morre('a tabela do §6.5 (%d linhas)' % len(PUB))
# guarda do porte: o golpe cru do nivel 30 tem de ser o do §4.4
t44 = {c: g for c, g in re.findall(r"\| `(\w+)` \| `\d+` \| `\d+` \| `([^`]+)` \|", t26)}
difA = difB = 0; linhas = []
for nv in sorted(PUB):
    for k, (nome, fat, ac, it) in enumerate(CAT):
        rod = arred(LIN[nv] * fat)
        cru = dado(rod / ac)
        imp = dado(arred(rod * F) / ac) if it else cru
        if nv == 30 and t44.get(nome) and t44[nome] != cru: morre(f'o porte do dado nao refaz o §4.4: {nome} {cru} x {t44[nome]}')
        A = media(cru) * (F if it else 1) / PT
        B = media(imp) / PT
        pub = PUB[nv][k]
        volta_A = (float(fmt(A).replace(',', '.')) * PT if fmt(A) != 'seco' else None)
        volta_B = (float(fmt(B).replace(',', '.')) * PT if fmt(B) != 'seco' else None)
        a_ok, b_ok = fmt(A) == pub, fmt(B) == pub
        difA += not a_ok; difB += not b_ok
        linhas.append((nv, nome, pub, fmt(A), fmt(B), cru, imp, media(imp), volta_A, volta_B))
print(f'fator {F} · 1 ponto = {PT} de dano · piso {PISO_PT} pontos · dados {DADOS}, seco abaixo de {PISO_D}, teto {TETO}')
print(f'{"nv":>3} {"categoria":<11} {"publicado":>9} {"rota A":>7} {"rota B":>7}  {"golpe cru":<11} {"golpe impresso":<14} {"media imp.":>10}  {"A x 4,5":>8} {"B x 4,5":>8}')
for nv, nome, pub, a, b, cru, imp, mi, va, vb in linhas:
    marca = '' if a == b else '  <-- as rotas divergem'
    print(f'{nv:>3} {nome:<11} {pub:>9} {a:>7} {b:>7}  {cru:<11} {imp:<14} {mi:>10.2f}  {("—" if va is None else f"{va:.2f}"):>8} {("—" if vb is None else f"{vb:.2f}"):>8}{marca}')
print(f'\ncelulas em que o publicado difere: rota A {difA} de 35 · rota B {difB} de 35')
erros = lambda idx: [abs(l[idx] - l[7]) for l in linhas if l[idx] is not None]
eA, eB = erros(8), erros(9)
print(f'volta (pontos x 4,5 contra a media do golpe impresso): rota A erro max {max(eA):.2f} medio {sum(eA)/len(eA):.3f} · rota B erro max {max(eB):.2f} medio {sum(eB)/len(eB):.3f}')

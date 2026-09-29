# -*- coding: utf-8 -*-
"""Gera as tabelas do capítulo 6 na GRADE da fase 2 (v0.282).

Nenhum número é digitado à mão neste livro. As fontes:
  · as faixas da tabela de inimigo do manual, pelo `dados.js` do gerador de inimigo
    (o bloco 7 do conferir-ficha.py confere o dados.js contra a peça 26);
  · os degraus, o pagamento do papel e a regra do orçamento, pela peça 26;
  · o dado do golpe, pela função `dado()` do conta.js do gerador, portada com as constantes de lá;
  · as derivadas por marco, pela `04-fase-1/TABELA.md` (a grade não mexeu nelas);
  · o preço das condições, pela peça 19 §3.

Regiões que ele escreve no capítulo: DEGRAUS, CAPANGAS, PAGAMENTO, TABELAS e ORCAMENTO.
Com `--conferir` ele compara sem escrever, e o conferir-bestiario.py (9.5) roda assim.
"""
import math
import os
import re
import sys

BASE = os.path.dirname(os.path.abspath(__file__))
LIVRO = os.path.dirname(BASE)
BEST = os.path.dirname(LIVRO)
REPO = os.environ.get('JJK_REPO', os.path.dirname(BEST))
TAB = os.path.join(BEST, '04-fase-1', 'TABELA.md')
CAP = os.path.join(LIVRO, 'capitulos', '60-a-montagem.md')
DJ = os.path.join(REPO, 'sistema/05-material/gerador-inimigo/dados.js')
MAKE = os.path.join(REPO, 'sistema/05-material/gerador-inimigo/conta.js')
P26 = os.path.join(REPO, 'sistema/03-mecanica/26-bestiario.md')
P19 = os.path.join(REPO, 'sistema/03-mecanica/19-dano-e-condicoes.md')


def morre(m):
    sys.exit('✗ ÂNCORA PERDIDA: ' + m)


def ler(p):
    if not os.path.exists(p):
        morre('não existe: %s' % p)
    return open(p, encoding='utf-8').read()


def vg(x, casas=1):
    return ('%.*f' % (casas, x)).replace('.', ',')


def arred(x):                       # make.js: Math.ceil(x - 0.5), o meio para baixo
    return math.ceil(x - 0.5)


def jsround(x):                     # Math.round do JS
    return math.floor(x + 0.5)


# ── o dado() do conta.js, portado com as constantes lidas de lá
tm = ler(MAKE)
_md = re.search(r'const DADOS = \[([\d,\s]+)\]', tm)
_mp = re.search(r'if \(alvo < (\d+)\) return String\(arred\(alvo\)\)', tm)
_mt = re.search(r'if \(n > (\d+)\) continue', tm)
if not (_md and _mp and _mt):
    morre('a função `dado()` do conta.js mudou de forma')
DADOS_MK = [int(x) for x in _md.group(1).split(',')]
PISO, TETO_N = int(_mp.group(1)), int(_mt.group(1))


def dado(alvo):
    if alvo < PISO:
        return str(arred(alvo))
    meta, bom = alvo / 2, None
    for d in DADOS_MK:
        med = (d + 1) / 2
        n = max(1, jsround(meta / med))
        if n > TETO_N:
            continue
        fixo = alvo - n * med
        if fixo < 0:
            continue
        inteiro = 0 if abs(fixo - jsround(fixo)) < 1e-9 else 1
        erro = abs(n * med - meta)
        if (bom is None or inteiro < bom[0] or (inteiro == bom[0] and erro < bom[1] - 1e-9)
                or (inteiro == bom[0] and abs(erro - bom[1]) < 1e-9 and n < bom[2])):
            bom = (inteiro, erro, n, d, jsround(fixo))
    return ('%dd%d + %d' % bom[2:]) if bom[4] > 0 else '%dd%d' % (bom[2], bom[3])


def media(e):
    m = re.match(r'(\d+)d(\d+)(?:\s*\+\s*(\d+))?$', e.strip())
    return int(m.group(1)) * (1 + int(m.group(2))) / 2 + int(m.group(3) or 0) if m else float(e)


# ── as faixas, pelo dados.js: rotulo, de, ate, Classe, grupo, chefe vida, chefe dano, capanga vida, capanga dano
FX = [(r, int(a), int(b), int(g), int(cd), int(kv), int(kd)) for r, a, b, _, g, _, cd, kv, kd in
      re.findall(r"\['(\d+ a \d+)',\s*(\d+),\s*(\d+),\s*(\d+),\s*(\d+),\s*(\d+),\s*(\d+),\s*(\d+),\s*(\d+)\]", ler(DJ))]
if len(FX) != 7:
    morre('o dados.js não traz as sete faixas da tabela de inimigo')

# ── os degraus, pela peça 26 §4
t26 = ler(P26)
DEG = []
for ln in t26.split('| categoria | rodadas | orçamento | pressão |')[1].split('\n')[2:] if '| categoria | rodadas | orçamento | pressão |' in t26 else []:
    if not ln.startswith('|'):
        break
    c = [x.replace('*', '').replace('`', '').strip() for x in ln.split('|')[1:-1]]
    DEG.append((c[0], float(c[1].replace(',', '.')), float(c[2].replace(',', '.')), c[5]))
if [d[0] for d in DEG] != ['Capanga', 'Ameaça', 'Desastre', 'Catástrofe', 'Calamidade']:
    morre('a tabela dos degraus da peça 26 §4 mudou de forma (li %s)' % [d[0] for d in DEG])
m = re.search(r'trivial `\d+`, baixa `\d+`, moderada `\d+`, severa `\d+`, extrema `\d+`', t26)
if not m:
    morre('os nomes das dificuldades do Pathfinder 2e sumiram da peça 26 §4')
NOMES_DIF = re.findall(r'(\w+) `\d+`', m.group(0))
R_DES = dict((d[0], d[1]) for d in DEG)['Desastre']
NS = range(1, 7)


def pressao(d):
    return d[2] * R_DES / d[1]


def vida(f, d, n):
    return arred(d[1] * n * f[3] / 4)


def golpe(f, d):
    return dado(arred(f[4] / 8)) if d[0] == 'Capanga' else dado(arred(pressao(d) * f[4] / 4))


def rot(f):
    return f[0].replace(' a ', '–')


# ── DEGRAUS
deg = ['**Categorias**', '{: .tab-titulo }', '',
       '| categoria | a luta | dura | o golpe | tem `Intervenção`? |', '|---|---|---|---|---|']
for d, nome in zip(DEG, NOMES_DIF):
    gp = 'metade do golpe-base' if d[0] == 'Capanga' else ('o golpe-base' if abs(pressao(d) - 1) < 1e-9 else '`%s` × o golpe-base' % vg(pressao(d), 3))
    luta = nome + (' — o chefe do manual' if d[0] == 'Desastre' else '')
    it = 'não' if d[3] == '—' else ('só no `%s`' % d[3] if d[3] == '×6' else 'do `%s` em diante' % d[3])
    deg.append('| **`%s`** | %s | `%s` rodadas | %s | %s |' % (d[0], luta, vg(d[1], 1).replace(',0', ''), gp, it))
degraus = '\n'.join(deg)

# ── CAPANGAS: cada capanga tira 1 ÷ (rodadas × N) do chefe
cap = ['**Chefe com capangas**', '{: .tab-titulo }', '',
       '| cada capanga tira | ' + ' | '.join('`×%d`' % n for n in NS) + ' |', '|---' * 7 + '|']
for d in DEG[2:]:
    cap.append('| `%s` | ' % d[0] + ' | '.join('`%s%%`' % vg(100 / (d[1] * n), 1) for n in NS) + ' |')
capangas = '\n'.join(cap)

# ── PAGAMENTO: o Artilheiro pela categoria, e os tres de acao pelo N, lidos da peça 26 §3.4
_ma = t26.split('| categoria | `Capanga` | `Ameaça` | `Desastre` | `Catástrofe` | `Calamidade` |')
_mn = t26.split('| papel | `×1` | `×2` | `×3` | `×4` | `×5` | `×6` |')
if len(_ma) < 2 or len(_mn) < 2:
    morre('as tabelas do pagamento do papel sumiram da peça 26 §3.4')
art = [x.strip().strip('`').replace('× ', '') for x in _ma[1].split('\n')[2].split('|')[2:-1]]
porN = {}
for ln in _mn[1].split('\n')[2:]:
    if not ln.startswith('|'):
        break
    c = [x.replace('`', '').replace('× ', '').strip() for x in ln.split('|')[1:-1]]
    porN[c[0]] = c[1:]
inv = lambda s: vg(1 / float(s.replace(',', '.')), 3)
pag = ['**Vida do `Artilheiro`, por categoria**', '{: .tab-titulo }', '',
       '| | ' + ' | '.join('`%s`' % d[0] for d in DEG) + ' |', '|---' * 6 + '|',
       '| a vida | ' + ' | '.join('`× %s`' % inv(x) for x in art) + ' |', '',
       '**Vida do papel, pelo N**', '{: .tab-titulo }', '',
       '| papel | ' + ' | '.join('`×%d`' % n for n in NS) + ' |', '|---' * 7 + '|']
for k, rotulo in (('Emboscador ganha', '`Emboscador`'), ('Controlador e Reforço ganham', '`Controlador` e `Reforço`'),
                  ('o esquadrão do Capanga, Emboscador', 'o esquadrão do `Capanga`, `Emboscador`'),
                  ('o esquadrão do Capanga, Controlador e Reforço', 'o esquadrão do `Capanga`, `Controlador` e `Reforço`')):
    if k not in porN:
        morre('a linha "%s" do pagamento por N sumiu da peça 26 §3.4' % k)
    pag.append('| %s | ' % rotulo + ' | '.join('`× %s`' % inv(x) for x in porN[k]) + ' |')
pag += ['', '*O esquadrão do `Capanga` tem dois corpos por personagem, e age `2N` vezes.*']
pagamento = '\n'.join(pag)

# ── TABELAS
out = []
for d in DEG[1:]:
    out += ['**Vida por faixa · `%s`**' % d[0], '{: .tab-titulo }', '',
            '| nível | ' + ' | '.join('`×%d`' % n for n in NS) + ' |', '|---' * 7 + '|']
    out += ['| **%s** | ' % rot(f) + ' | '.join(str(vida(f, d, n)) for n in NS) + ' |' for f in FX]
    out.append('')
out += ['**Golpe por faixa**', '{: .tab-titulo }', '',
        '| nível | ' + ' | '.join('`%s`' % d[0] for d in DEG) + ' |', '|---' * 6 + '|']
out += ['| **%s** | ' % rot(f) + ' | '.join(golpe(f, d) for d in DEG) + ' |' for f in FX]
out += ['', '*O golpe de uma ação. Ele sai N vezes por rodada, e não muda com o N.*', '']
out += ['**Capanga por faixa**', '{: .tab-titulo }', '',
        '| nível | vida de um corpo | o golpe dele |', '|---|---|---|']
out += ['| **%s** | %d | %s |' % (rot(f), f[5], golpe(f, DEG[0])) for f in FX]
out += ['', '*O esquadrão tem dois corpos por personagem, com a vida num pool só.*', '']
# as derivadas por marco, da TABELA.md (a grade não mexeu nelas)
ttab = ler(TAB)
sec = ttab.split('## `Desastre`')[1].split('\n## ')[0] if '## `Desastre`' in ttab else morre('a seção `Desastre` sumiu da TABELA.md')
cab, T = None, {}
for ln in sec.split('\n'):
    c = [x.strip().strip('*').strip('`').strip('*') for x in ln.strip().strip('|').split('|')]
    if c and c[0] == 'nv':
        cab = c
    elif cab and c and re.match(r'^\d+$', c[0] or ''):
        T[int(c[0])] = dict(zip(cab, c))
CAMPOS = ['Defesa', 'acerto', 'CD', 'refino', 'proteção']
niveis = sorted(T)
marcos, ini = [], niveis[0]
for i, nv in enumerate(niveis):
    ult = i == len(niveis) - 1
    if ult or any(T[niveis[i + 1]][c] != T[nv][c] for c in CAMPOS):
        marcos.append((ini, nv))
        if not ult:
            ini = niveis[i + 1]
if len(marcos) != 7:
    morre('as derivadas colapsaram em %d marcos, e a peça publica 7' % len(marcos))
out += ['**Defesa, acerto, CD e refino por marco**', '{: .tab-titulo }', '',
        '| nível | Defesa | acerto | CD | refino | proteção |', '|---|---|---|---|---|---|']
for a, b in marcos:
    x = T[a]
    out.append('| **%s** | %s | %s | %s | %s | %s |' % ('%d–%d' % (a, b), x['Defesa'], x['acerto'], x['CD'], x['refino'], x['proteção']))
out += ['', '*Estas cinco valem para toda célula. Elas sobem em marco de nível, e a vida e o golpe sobem em faixa de Classe.*']
tabelas = '\n'.join(out)

# ── ORCAMENTO: o golpe ÷ 4,5, e o que cabe na maior ação
m = re.search(r'O orçamento de feitiço de uma ação é o golpe dela dividido por `([\d,]+)`', t26)
m2 = re.search(r'o menor feitiço do manual é a `Classe 1` e custa `(\d+)` pontos', t26)
if not (m and m2):
    morre('a regra do orçamento ou o piso da `Classe 1` sumiram do §6.5 da peça 26')
MED_D8, PISO_PTS = float(m.group(1).replace(',', '.')), int(m2.group(1))
t19 = ler(P19)
CUSTO = {}
for pt, nv_ in re.findall(r'\| `(\d+)` \| `[\d,]+×` \| `(Leve|Média|Pesada)` \|', t19):
    CUSTO.setdefault(nv_, int(pt))
if sorted(CUSTO) != ['Leve', 'Média', 'Pesada']:
    morre('não li os três níveis de condição na peça 19 §3')
orc = ['**Orçamento de uma ação, por categoria**', '{: .tab-titulo }', '',
       '| nível | ' + ' | '.join('`%s`' % d[0] for d in DEG) + ' |', '|---' * 6 + '|']
maior = 0.0
for f in FX:
    nv = {2: 2, 5: 5, 9: 10, 13: 15, 17: 20, 21: 25, 26: 30}.get(f[1])
    cel = []
    for d in DEG:
        v = media(golpe(f, d)) / MED_D8
        maior = max(maior, v)
        cel.append('seco' if v < PISO_PTS else '`%s`' % vg(v, 1))
    orc.append('| `%d` | %s |' % (nv, ' | '.join(cel)))
orc += ['', 'O que cabe na maior ação do sistema, a de `%s` pontos:' % vg(maior, 1), '',
        '**Condição na maior ação**', '{: .tab-titulo }', '',
        '| se ele comprar | custa | sobra para dado |', '|---|---|---|']
for nv_ in ('Leve', 'Média', 'Pesada'):
    orc.append('| uma condição `%s` | `%d` | `%s` |' % (nv_, CUSTO[nv_], vg(maior - CUSTO[nv_], 1)))
orcamento = '\n'.join(orc)

# ── escreve as regiões
capt = ler(CAP)
novo = capt
for nome, conteudo in (('DEGRAUS', degraus), ('CAPANGAS', capangas), ('PAGAMENTO', pagamento),
                       ('TABELAS', tabelas), ('ORCAMENTO', orcamento)):
    ini_, fim_ = '<!-- %s -->' % nome, '<!-- FIM %s -->' % nome
    if ini_ not in novo or fim_ not in novo:
        morre('a marca `%s` sumiu do capítulo 6' % nome)
    i, j = novo.index(ini_), novo.index(fim_)
    novo = novo[:i] + ini_ + '\n\n' + conteudo + '\n\n' + novo[j:]
if '--conferir' in sys.argv:
    sys.exit(0 if novo == capt else '✗ DESATUALIZADO: o capítulo não é o que build/gerar-tabelas.py gera hoje — rode ele')
open(CAP, 'w', encoding='utf-8').write(novo)
print('✓ capítulo 6: os cinco degraus, o chefe com capangas, o pagamento do papel, as tabelas de nível e o orçamento, '
      'da peça 26, do dados.js e do make.js; a maior ação tem %s pontos.' % vg(maior, 1))

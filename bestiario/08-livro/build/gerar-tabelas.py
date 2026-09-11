# -*- coding: utf-8 -*-
"""Gera as tabelas do capítulo 6 a partir da `04-fase-1/TABELA.md`.

Nenhum número é digitado à mão neste livro. Este script lê a escada viva no
documento DONO, confere que ela colapsa em faixa (senão a tabela impressa seria
mentira) e escreve o markdown do capítulo.

  · vida, dano por rodada, ações e golpe mudam em FAIXA de Classe
  · Defesa, acerto, CD, refino e proteção mudam em MARCO de nível

As duas escadas não coincidem, e é por isso que saem duas tabelas.

O script morre se a `TABELA.md` mudar de forma, ou se algum valor deixar de ser
constante dentro da faixa dele.
"""
import math
import os
import re
import sys

BASE = os.path.dirname(os.path.abspath(__file__))
LIVRO = os.path.dirname(BASE)
BEST = os.path.dirname(LIVRO)

TAB = os.path.join(BEST, '04-fase-1', 'TABELA.md')
CAP = os.path.join(LIVRO, 'capitulos', '60-a-montagem.md')
MARCA = '<!-- TABELAS -->'
MARCA_ORC = '<!-- ORCAMENTO -->'

CATS = ('Capanga', 'Ameaça', 'Desastre', 'Catástrofe', 'Calamidade')


def morre(m):
    sys.exit('✗ ÂNCORA PERDIDA: ' + m)


def ler(p):
    if not os.path.exists(p):
        morre('não existe: %s' % p)
    return open(p, encoding='utf-8').read()


def linhas(txt, cat):
    if '## `%s`' % cat not in txt:
        morre('a seção `%s` sumiu da TABELA.md' % cat)
    sec = txt.split('## `%s`' % cat)[1].split('\n## ')[0]
    cab, out = None, {}
    for ln in sec.split('\n'):
        cels = [c.strip().strip('*').strip('`').strip('*')
                for c in ln.strip().strip('|').split('|')]
        if cels and cels[0] == 'nv':
            cab = cels
        elif cab and cels and re.match(r'^\d+$', cels[0] or ''):
            out[int(cels[0])] = dict(zip(cab, cels))
    if len(out) < 29:
        morre('a seção `%s` tem %d níveis, e a escada é de 29' % (cat, len(out)))
    return out


def blocos(niveis, dados, campos):
    """Colapsa os níveis em faixas onde TODOS os campos ficam constantes."""
    faixas, ini = [], niveis[0]
    for i, nv in enumerate(niveis):
        ult = i == len(niveis) - 1
        muda = (not ult) and any(dados[niveis[i + 1]][c] != dados[nv][c] for c in campos)
        if muda or ult:
            faixas.append((ini, nv))
            if not ult:
                ini = niveis[i + 1]
    return faixas


def rot(a, b):
    return str(a) if a == b else '%d–%d' % (a, b)


txt = ler(TAB)
T = {c: linhas(txt, c) for c in CATS}
NIVEIS = sorted(T['Desastre'])

# ── o golpe de quem carrega `Intervenção` sai impresso já com o fator, pela conta do
#    make.js: dado(arred(dano/rod × fator) ÷ ações). O fator é lido do RASCUNHO-5, e o
#    dado() é portado do make.js com as constantes lidas de lá.
R5 = os.path.join(BEST, '03-bloco', 'RASCUNHO-5-o-bloco-em-branco.md')
REPO = os.environ.get('JJK_REPO', '/media/mizuki/HD Externo II/Claude/Claude 2')
MAKE = os.path.join(REPO, 'sistema/05-material/gerador-inimigo/make.js')
COM_INT = ('Desastre', 'Catástrofe', 'Calamidade')
m = re.search(r'fator de dano de quem tem `Intervenção` é multiplicado por `([\d,]+)`', ler(R5))
if not m:
    morre('o fator da Intervenção sumiu do RASCUNHO-5')
FAT_INT = float(m.group(1).replace(',', '.'))
tm = ler(MAKE)
_md = re.search(r'const DADOS = \[([\d,\s]+)\]', tm)
_mp = re.search(r'if \(alvo < (\d+)\) return String\(arred\(alvo\)\)', tm)
_mt = re.search(r'if \(n > (\d+)\) continue', tm)
if not (_md and _mp and _mt):
    morre('a função `dado()` do make.js mudou de forma')
DADOS_MK = [int(x) for x in _md.group(1).split(',')]
PISO, TETO_N = int(_mp.group(1)), int(_mt.group(1))


def arred(x):                       # make.js: Math.ceil(x - 0.5)
    return math.ceil(x - 0.5)


def jsround(x):                     # Math.round do JS
    return math.floor(x + 0.5)


def dado(alvo, rnd=None):
    """`rnd` só existe para a conferência: `round` do Python arredonda o meio para o par."""
    R = rnd or jsround
    if alvo < PISO:
        return str(arred(alvo))
    meta, bom = alvo / 2, None
    for d in DADOS_MK:
        med = (d + 1) / 2
        n = max(1, R(meta / med))
        if n > TETO_N:
            continue
        fixo = alvo - n * med
        if fixo < 0:
            continue
        inteiro = 0 if abs(fixo - R(fixo)) < 1e-9 else 1
        erro = abs(n * med - meta)
        if (bom is None or inteiro < bom[0]
                or (inteiro == bom[0] and erro < bom[1] - 1e-9)
                or (inteiro == bom[0] and abs(erro - bom[1]) < 1e-9 and n < bom[2])):
            bom = (inteiro, erro, n, d, R(fixo))
    if bom is None:
        n = max(1, R(alvo / 9))
        r = arred(alvo - 4.5 * n)
        return '%dd8 + %d' % (n, r) if r > 0 else '%dd8' % n
    return ('%dd%d + %d' % bom[2:]) if bom[4] > 0 else '%dd%d' % (bom[2], bom[3])


# o porte tem de refazer o golpe cru publicado. A única folga aceita é a célula em
# que a TABELA arredondou o meio-ponto para o par; ela é listada no fim, nunca calada.
MEIO = []
for c in CATS[1:]:
    for nv, d in T[c].items():
        x = int(d['dano/rod']) / int(d['ações'])
        if dado(x) != d['o golpe']:
            if dado(x, round) != d['o golpe']:
                morre('o dado() portado não refaz o golpe de `%s` nv %d' % (c, nv))
            MEIO.append('%s nv %d: TABELA %s, make.js %s' % (c, nv, d['o golpe'], dado(x)))


def golpe_int(d):
    return dado(arred(int(d['dano/rod']) * FAT_INT) / int(d['ações']))

# ── as colunas de cada seção
COL_VIDA = {c: ('vida de um' if c == 'Capanga' else 'vida') for c in CATS}
COL_GOLPE = {c: ('golpe de um' if c == 'Capanga' else 'o golpe') for c in CATS}

# ── 1. a tabela de vida e golpe, por faixa
campos_cat = {}
for c in CATS:
    cs = [COL_VIDA[c], COL_GOLPE[c]]
    if c != 'Capanga':
        cs += ['dano/rod', 'ações']
    if c == 'Capanga':
        cs += ['pool dos 8']
    campos_cat[c] = cs

faixas = None
for c in CATS:
    f = blocos(NIVEIS, T[c], campos_cat[c])
    if faixas is None:
        faixas = f
    elif f != faixas:
        morre('a categoria `%s` não colapsa nas mesmas faixas das outras — '
              'a tabela impressa por faixa seria mentira' % c)
if len(faixas) != 7:
    morre('a escada colapsou em %d faixas, e a tabela do manual publica 7' % len(faixas))

out = []
out.append('**Vida e golpe por faixa**')
out.append('{: .tab-titulo }')
out.append('')
out.append('| nível | `Capanga` (cada um) | `Ameaça` | `Desastre` | `Catástrofe` | `Calamidade` |')
out.append('|---|---|---|---|---|---|')
for a, b in faixas:
    cel = []
    for c in CATS:
        d = T[c][a]
        g = golpe_int(d) if c in COM_INT else d[COL_GOLPE[c]]
        cel.append('%s · %s' % (d[COL_VIDA[c]], g))
    out.append('| **%s** | %s |' % (rot(a, b), ' | '.join(cel)))
out.append('')
out.append('*Vida · golpe de uma ação. O golpe sai uma vez por ação, e o número de ações está '
           'na tabela do Passo 1. Em `%s` o golpe já vem com o `%s` da `Intervenção`.*'
           % ('`, `'.join(COM_INT[:-1]) + '` e `' + COM_INT[-1], ('%.3f' % FAT_INT).replace('.', ',')))
out.append('')

# ── 2. o pool do Capanga
out.append('**Pool do esquadrão de `Capanga`**')
out.append('{: .tab-titulo }')
out.append('')
out.append('| nível | vida de um | pool dos oito |')
out.append('|---|---|---|')
for a, b in faixas:
    d = T['Capanga'][a]
    out.append('| **%s** | %s | **%s** |' % (rot(a, b), d['vida de um'], d['pool dos 8']))
out.append('')

# ── 3. as derivadas, por marco
CAMPOS_DER = ['Defesa', 'acerto', 'CD', 'refino', 'proteção']
marcos = blocos(NIVEIS, T['Desastre'], CAMPOS_DER)
for c in CATS:
    if c == 'Capanga':
        continue
    if blocos(NIVEIS, T[c], CAMPOS_DER) != marcos:
        morre('as derivadas de `%s` não batem com as das outras categorias' % c)
if len(marcos) != 7:
    morre('as derivadas colapsaram em %d marcos, e a peça publica 7' % len(marcos))
if marcos == faixas:
    morre('faixa e marco colapsaram iguais — o texto do capítulo diz que eles NÃO coincidem')

out.append('**Defesa, acerto, CD e refino por marco**')
out.append('{: .tab-titulo }')
out.append('')
out.append('| nível | Defesa | acerto | CD | refino | proteção |')
out.append('|---|---|---|---|---|---|')
for a, b in marcos:
    d = T['Desastre'][a]
    out.append('| **%s** | %s | %s | %s | %s | %s |'
               % (rot(a, b), d['Defesa'], d['acerto'], d['CD'], d['refino'], d['proteção']))
out.append('')
out.append('*Estas cinco valem para toda categoria. Elas sobem em marco de nível, e as duas '
           'escadas não coincidem.*')

tabelas = '\n'.join(out)

# ── 4. o orçamento de uma ação, por categoria
#
# ⚠ Até 11/09/2026 esta tabela era ESTÁTICA no capítulo — 35 números digitados à mão,
#   fora de região gerada. A rota `B` do orçamento moveu 9 deles e alguém digitou certo;
#   na vez seguinte ninguém garantia. Agora ela sai da mesma conta do golpe impresso.
P26 = os.path.join(REPO, 'sistema/03-mecanica/26-bestiario.md')
P19 = os.path.join(REPO, 'sistema/03-mecanica/19-dano-e-condicoes.md')
t26, t19 = ler(P26), ler(P19)
m = re.search(r'O orçamento de feitiço de uma ação é o golpe dela dividido por `([\d,]+)`', t26)
if not m:
    morre('a regra do orçamento sumiu do §6.5 da peça 26')
MED_D8 = float(m.group(1).replace(',', '.'))
m = re.search(r'o menor feitiço do manual é a `Classe 1` e custa `(\d+)` pontos', t26)
if not m:
    morre('o piso da `Classe 1` sumiu do §6.5 da peça 26')
PISO_PTS = int(m.group(1))

# os três níveis de condição, com o preço em ponto — peça 19 §3
CUSTO = {}
for pt, nv_ in re.findall(r'\| `(\d+)` \| `[\d,]+×` \| `(Leve|Média|Pesada)` \|', t19):
    CUSTO.setdefault(nv_, int(pt))
    if CUSTO[nv_] != int(pt):
        morre('a peça 19 §3 dá dois preços para a condição `%s`' % nv_)
if sorted(CUSTO) != ['Leve', 'Média', 'Pesada']:
    morre('não li os três níveis de condição na peça 19 §3 (li %s)' % sorted(CUSTO))


def media_e(e):
    e = e.strip()
    mm = re.match(r'(\d+)d(\d+)(?:\s*\+\s*(\d+))?$', e)
    if mm:
        return int(mm.group(1)) * (1 + int(mm.group(2))) / 2 + int(mm.group(3) or 0)
    if re.match(r'^\d+$', e):
        return float(e)
    morre('não sei ler a expressão de golpe %r' % e)


def pts_de(c, nv):
    d = T[c][nv]
    g = golpe_int(d) if c in COM_INT else d[COL_GOLPE[c]]
    return media_e(g) / MED_D8


orc = []
orc.append('**Orçamento de uma ação, por categoria**')
orc.append('{: .tab-titulo }')
orc.append('')
orc.append('| nível | `Capanga` | `Ameaça` | `Desastre` | `Catástrofe` | `Calamidade` |')
orc.append('|---|---|---|---|---|---|')
NV_ORC = [2, 5, 10, 15, 20, 25, 30]
maior = 0.0
for nv in NV_ORC:
    if nv not in T['Desastre']:
        morre('o nível %d sumiu da TABELA' % nv)
    cel = []
    for c in CATS:
        v = pts_de(c, nv)
        maior = max(maior, v)
        cel.append('seco' if v < PISO_PTS else '`%s`' % ('%.1f' % v).replace('.', ','))
    orc.append('| `%d` | %s |' % (nv, ' | '.join(cel)))
orc.append('')
orc.append('*As colunas de quem tem `Intervenção` já levam o `%s`.*'
           % ('%.3f' % FAT_INT).replace('.', ','))
orc.append('')
mai = ('%.1f' % maior).replace('.', ',')
orc.append('O que cabe na maior ação do sistema, a de `%s` pontos:' % mai)
orc.append('')
orc.append('**Condição na maior ação**')
orc.append('{: .tab-titulo }')
orc.append('')
orc.append('| se ele comprar | custa | sobra para dado |')
orc.append('|---|---|---|')
for nv_ in ('Leve', 'Média', 'Pesada'):
    sobra = maior - CUSTO[nv_]
    orc.append('| uma condição `%s` | `%d` | `%s` |'
               % (nv_, CUSTO[nv_], ('%.1f' % sobra).replace('.', ',')))
orcamento = '\n'.join(orc)

cap = ler(CAP)
for mk in (MARCA, '<!-- FIM TABELAS -->', MARCA_ORC, '<!-- FIM ORCAMENTO -->'):
    if mk not in cap:
        morre('a marca `%s` sumiu do capítulo 6' % mk)
inicio = cap.index(MARCA)
fim = cap.index('<!-- FIM TABELAS -->')
novo = cap[:inicio] + MARCA + '\n\n' + tabelas + '\n\n' + cap[fim:]
i2 = novo.index(MARCA_ORC)
f2 = novo.index('<!-- FIM ORCAMENTO -->')
novo = novo[:i2] + MARCA_ORC + '\n\n' + orcamento + '\n\n' + novo[f2:]
open(CAP, 'w', encoding='utf-8').write(novo)

print('=' * 70)
print('TABELAS DO CAPÍTULO 6 — geradas da `04-fase-1/TABELA.md`')
print('=' * 70)
print('  %d faixas de Classe  ·  %d marcos de nível  ·  %d categorias'
      % (len(faixas), len(marcos), len(CATS)))
print('  faixas : ' + ' · '.join(rot(a, b) for a, b in faixas))
print('  marcos : ' + ' · '.join(rot(a, b) for a, b in marcos))
print('✓ a escada colapsa, e as duas não coincidem.')
print('✓ golpe de %s impresso com o fator %.3f, pela conta do make.js.'
      % (' · '.join(COM_INT), FAT_INT))
for x in MEIO:
    print('  ⚠ meio-ponto arredondado para o par na TABELA — ' + x)

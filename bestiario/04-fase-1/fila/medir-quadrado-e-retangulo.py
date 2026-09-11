#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
"Quadrado e retangular" — as DUAS leituras, medidas.

Pergunta do Mizuki, 10/09/2026: "E se a gente adicionasse tamanhos no formato
quadrado e retangular? meio q a gente n boto mas e uma metrica padrao,
acredito eu, tanto pra inimigo quanto pra player"

Ela le de dois jeitos, e os dois sao mediveis:

  LEITURA A · a FORMA DA AREA — hoje o sistema tem Esfera, Cone e Linha.
             Entra `Cubo`/`Quadrado`? Entra `Retangulo`?

  LEITURA B · o CORPO NA GRADE — hoje o `tamanho` so da alcance em metro, e
             nao diz quantos quadrados o bicho ocupa.

E medindo isso apareceram DUAS coisas que a pergunta nao pedia:
  · o Cone NAO TEM LARGURA DEFINIDA em lugar nenhum do manual
  · Cone e Linha dividem UMA escada e UM preco, e no topo dela o Cone
    cobre 20x o que a Linha cobre

Nenhum numero nosso mora aqui: as ancoras sao lidas dos donos.
"""
import collections
import json
import math
import os
import re
import statistics
import sys

BEST = os.environ.get('JJK_BEST', '/media/mizuki/HD Externo II/Claude/Claude 2/bestiario')
REPO = os.environ.get('JJK_REPO', '/media/mizuki/HD Externo II/Claude/Claude 2')
FILA = os.path.join(BEST, '04-fase-1/fila')
DS = os.path.join(FILA, 'dados-recarga-area/data-md-main')

BLOCO = '03-bloco/RASCUNHO-5-o-bloco-em-branco.md'
PARTC = 'manual/gerador/partC.js'
QUAD = 1.5          # o lado do quadrado da grade — lido abaixo, do dono

_cache = {}


def ler(rel, raiz=BEST):
    k = (rel, raiz)
    if k not in _cache:
        with open(os.path.join(raiz, rel), encoding='utf-8') as f:
            _cache[k] = f.read()
    return _cache[k]


def pega(rel, padrao, rotulo, raiz=BEST, flags=0):
    m = re.search(padrao, ler(rel, raiz), flags)
    if not m:
        print(f'\n  !! ANCORA PERDIDA: {rotulo}\n     nao casa em {rel}\n     padrao: {padrao}')
        sys.exit(1)
    return m


def num(s):
    return float(s.replace('−', '-').replace(',', '.'))


def bloco(t):
    print()
    print('=' * 96)
    print(t)
    print('=' * 96)


def pct(x, tot):
    return f'{100.0*x/tot:5.1f}%' if tot else '   —  '


# ------------------------------------------------------------ 0 · o que temos
bloco('0 · AS FORMAS QUE O SISTEMA TEM — lidas do partC.js')

FORMA = {}
for nome in ('Explosão', 'Aura', 'Cone', 'Linha'):
    m = pega(PARTC, r"\['" + nome + r"', '(\w+)', '([^']+)'", f'partC.js — a Forma {nome}', REPO)
    FORMA[nome] = {'custa': m.group(1), 'texto': m.group(2)}
    print(f"  {nome:<10} custa {m.group(1):<6} — {m.group(2)[:70]}")

precos = set(f['custa'] for f in FORMA.values())
print(f'\n  ⟹ as {len(FORMA)} Formas de área custam: {precos}  '
      + ('### TODAS O MESMO DEGRAU' if len(precos) == 1 else '(preços diferentes)'))

print('\n  as formas que NAO existem no gerador:')
tx = ler(PARTC, REPO)
for nome in ('Cubo', 'Quadrado', 'Retângulo', 'Cilindro', 'Muro', 'Emanação'):
    n = len(re.findall(r'\b' + nome + r'\b', tx))
    print(f'    {nome:<12}{n:>4} menções' + ('   <<< NAO EXISTE' if not n else ''))

# a Linha JA e um retangulo
# a mexida `29b` da v0.221 emendou a frase da Linha ("… Maior passa a subir a largura"),
# e a aspa que fechava a string deixou de vir logo depois do `1,5 m`
mL = pega(PARTC, r"\['Linha', '\w+', '([\d,]+) m por ([\d,]+) m", 'partC.js — a Linha', REPO)
LIN_C, LIN_L = num(mL.group(1)), num(mL.group(2))
print(f'\n  ⚠ a nossa `Linha` JÁ É um retângulo: {mL.group(1)} m por {mL.group(2)} m '
      f'— razão {LIN_C/LIN_L:.1f}:1')

# as escadas
ESC = {}
for rot, chave in (('Esfera', r'Esfera \(raio\)'), ('Cone e Linha', r'Cone e Linha')):
    m = pega(PARTC, r"\['" + chave + r"', '([^']+)'\]", f'partC.js — a escada {rot}', REPO)
    ESC[rot] = [num(x) for x in re.findall(r'([\d,]+) m', m.group(1))]
    print(f'\n  escada `{rot}`: ' + ' → '.join(f'{v:g} m' for v in ESC[rot]))

# o Cone tem largura definida?
tem_larg = re.search(r'[Cc]one[^\n]{0,120}?(?:largura|ângulo|graus|por [\d,]+ m|abre)', tx)
print(f'\n  ⚠⚠ o `Cone` tem LARGURA ou ÂNGULO definido no gerador? '
      + ('SIM' if tem_larg else '### NÃO — só o comprimento'))
print(f'     a `Esfera` diz raio ({FORMA["Explosão"]["texto"][:22]}…) — 1 número, e ele basta')
print(f'     a `Linha` diz {LIN_C:g} m por {LIN_L:g} m — 2 números')
print(f'     o `Cone` diz "{FORMA["Cone"]["texto"]}" — 1 número, e ele NAO basta')

# a grade
m = pega(BLOCO, r'largura na grade', 'RASCUNHO-5 — a coluna de grade')
m2 = pega(BLOCO, r'\| `2`–`8` \| \*\*`([\d,]+) m`\*\* \| `(\d+)` quadrados \| `(\d+)` quadrados \|',
          'RASCUNHO-5 — a linha nv2-8 da área natural')
r_base, cob_base, larg_base = num(m2.group(1)), int(m2.group(2)), int(m2.group(3))
QUAD = 2 * r_base / larg_base
print(f'\n  RASCUNHO-5 · raio {r_base:g} m cobre {cob_base} quadrados, largura {larg_base} '
      f'⟹ o quadrado da grade é {QUAD:g} m')
conf = math.pi * r_base ** 2 / QUAD ** 2
print(f'  conferindo: π·{r_base:g}² ÷ {QUAD:g}² = {conf:.2f} → {round(conf)} quadrados   '
      + ('✅ bate' if round(conf) == cob_base else '⚠ NAO BATE'))


# --------------------------------- § A CONTA QUE DECIDE — cobertura por forma
bloco('§ QUANTO CADA FORMA COBRE — mesma escada, mesmo preço')


def q_esfera(r):
    return math.pi * r ** 2 / QUAD ** 2


def q_linha(comp, larg=None):
    return comp * (larg if larg else LIN_L) / QUAD ** 2


def q_cone(comp, abertura):
    """abertura = largura da boca ÷ comprimento. O D&D usa 1,0 (boca = comprimento)."""
    return comp * (comp * abertura) / 2 / QUAD ** 2


def q_quadrado(lado):
    return lado ** 2 / QUAD ** 2


print(f'''
  ⚠ O `Cone` nao tem abertura definida, entao ele sai em TRES hipoteses:
    · 1,00  — a do D&D 2024 ("a largura em qualquer ponto é igual à distância")
    · 0,58  — cone de 60 graus, o do Pathfinder 1e e de varios VTT
    · 1,73  — cone de 120 graus, o mais aberto que costuma aparecer
''')

print(f'  em quadrados de {QUAD:g} m:\n')
print(f'    {"degrau":<8}{"Esfera":>10}{"Linha":>10}{"Cone 0,58":>12}{"Cone 1,00":>12}{"Cone 1,73":>12}')
linhas = []
for i in range(5):
    r = ESC['Esfera'][i]
    c = ESC['Cone e Linha'][i]
    e, li = q_esfera(r), q_linha(c)
    co = [q_cone(c, a) for a in (0.58, 1.00, 1.73)]
    linhas.append((e, li, co[1]))
    print(f'    d{i+1:<7}{e:10.0f}{li:10.0f}{co[0]:12.0f}{co[1]:12.0f}{co[2]:12.0f}')

print(f'\n    {"crescimento d1→d5":<22}'
      f'{linhas[-1][0]/linhas[0][0]:8.1f}×{linhas[-1][1]/linhas[0][1]:9.1f}×'
      f'{"":12}{linhas[-1][2]/linhas[0][2]:11.1f}×')

print(f'''
  ⟹ As tres tem o MESMO preco (`{list(precos)[0]}`) e as duas ultimas dividem a MESMA escada.''')
for i in (0, 4):
    e, li, co = linhas[i]
    pior, melhor = min(e, li, co), max(e, li, co)
    print(f'    no d{i+1}: Esfera {e:.0f} · Linha {li:.0f} · Cone {co:.0f} quadrados '
          f'— o maior é {melhor/pior:.1f}× o menor')

print(f'''
  ### E o Cone e a Linha estao na MESMA LINHA da tabela de escadas.
      No d5 os dois estao no MESMO degrau ({ESC["Cone e Linha"][4]:g} m) e cobrem '''
      f'{linhas[-1][2]:.0f} contra {linhas[-1][1]:.0f} quadrados — '
      f'{linhas[-1][2]/linhas[-1][1]:.1f}× de diferenca.')

# o quadrado que empataria
print('\n  § E um `Quadrado` de que lado empataria com cada uma?\n')
print(f'    {"degrau":<8}{"= à Esfera":>14}{"= à Linha":>14}{"= ao Cone 1,00":>16}')
for i in range(5):
    e, li, co = linhas[i]
    print(f'    d{i+1:<7}{math.sqrt(e)*QUAD:11.1f} m{math.sqrt(li)*QUAD:11.1f} m'
          f'{math.sqrt(co)*QUAD:13.1f} m')


# ------------------------------------------------- LEITURA A · forma de area
bloco('LEITURA A · QUEM NO CAMPO TEM QUADRADO / CUBO / RETÂNGULO?')

SRD = {}
for arq, rot in (('srd-2024.json', 'D&D 2024'), ('srd-2014.json', 'D&D 2014')):
    with open(os.path.join(FILA, arq), encoding='utf-8') as f:
        SRD[rot] = json.load(f)

FORMA_DND = {'Cone': r'\bcone\b', 'Linha': r'\bline\b', 'Esfera / raio': r'\bsphere\b|\bradius\b',
             'CUBO': r'\bcube\b', 'Cilindro': r'\bcylinder\b', 'Emanação': r'\bemanation\b',
             'QUADRADO (forma)': r'\b\d+-foot square\b'}
for rot, mons in SRD.items():
    textos = [a.get('desc') or '' for m in mons for a in (m.get('actions') or [])]
    textos += [t.get('desc') or '' for m in mons for t in (m.get('traits') or [])]
    conta = {k: sum(1 for t in textos if re.search(p, t, re.I)) for k, p in FORMA_DND.items()}
    tot = sum(conta.values())
    print(f'\n  {rot} — {len(textos)} textos de ação/traço, {tot} menções de forma')
    for k, v in sorted(conta.items(), key=lambda x: -x[1]):
        print(f'    {k:<20}{v:>5} {pct(v, tot)}' + ('   <<< ZERO' if v == 0 else ''))

with open(os.path.join(FILA, 'pf2e-habs2.json'), encoding='utf-8') as f:
    pf = json.load(f)
FORMA_PF = {'Cone': r'\bcone\b', 'Linha': r'\bline\b', 'Burst (esfera)': r'\bburst\b',
            'Emanação': r'\bemanation\b', 'CUBO': r'\bcube\b', 'Cilindro': r'\bcylinder\b',
            'QUADRADO (forma)': r'\b\d+-foot square\b'}
textos = [h.get('bloco') or '' for h in pf]
conta = {k: sum(1 for t in textos if re.search(p, t, re.I)) for k, p in FORMA_PF.items()}
tot = sum(conta.values())
print(f'\n  Pathfinder 2e — {len(textos)} habilidades, {tot} menções de forma')
for k, v in sorted(conta.items(), key=lambda x: -x[1]):
    print(f'    {k:<20}{v:>5} {pct(v, tot)}' + ('   <<< ZERO' if v == 0 else ''))

# Draw Steel: a declaracao de area e marcada com 📏
dstx = '\n'.join(open(os.path.join(r, a), encoding='utf-8').read()
                 for r, _, arqs in os.walk(os.path.join(DS, 'Bestiary'))
                 for a in arqs if a.endswith('.md'))
spec = [s.replace('**', '').strip() for s in re.findall(r'📏\s*([^|]+?)\s*\*\*', dstx)]
c = collections.Counter()
for s in spec:
    for w in ('burst', 'cube', 'line', 'aura', 'wall', 'cone', 'sphere'):
        if re.search(r'\b' + w + r'\b', s, re.I):
            c[w] += 1
            break
tot = sum(c.values())
print(f'\n  Draw Steel — {len(spec)} declarações de distância lidas, {tot} são ÁREA')
for w in ('burst', 'cube', 'line', 'aura', 'wall', 'cone', 'sphere'):
    print(f'    {w:<20}{c[w]:>5} {pct(c[w], tot)}' + ('   <<< ZERO' if not c[w] else ''))

larg = re.findall(r'(\d+)\s*[x×]\s*(\d+)\s*line', dstx, re.I)
ws = collections.Counter(int(b) for a, b in larg)
raz = [int(a) / int(b) for a, b in larg]
print(f'\n  ⚠ e a `line` DELES carrega LARGURA como parâmetro — "A x B line", {len(larg)} delas:')
print(f'    larguras: ' + '  '.join(f'{k}→{v}' for k, v in sorted(ws.items())))
print(f'    razão comprimento/largura: mediana {statistics.median(raz):.1f}:1   '
      f'a NOSSA Linha é {LIN_C/LIN_L:.0f}:1, fixa')

cub = collections.Counter(int(x) for x in re.findall(r'(\d+)\s*cube', dstx, re.I))
print(f'\n  os cubos deles: lados ' + '  '.join(f'{k}→{v}' for k, v in sorted(cub.items()))
      + f'   (mediana {statistics.median([k for k, v in cub.items() for _ in range(v)]):.0f} quadrados de lado)')


# --------------------------------------------- LEITURA B · o corpo na grade
bloco('LEITURA B · O CORPO NA GRADE — o footprint é quadrado em todo lugar?')

for rot, mons in SRD.items():
    cc = collections.Counter((m.get('size') or {}).get('name') for m in mons)
    print(f'\n  {rot} — {len(mons)} blocos, {len(cc)} tamanhos, e o tamanho é UMA palavra')
    print('    ' + '  ·  '.join(f'{k} {v}' for k, v in cc.most_common()))

with open(os.path.join(FILA, 'pf2e-tamanho.json'), encoding='utf-8') as f:
    pf2 = json.load(f)


def achatar(v):
    if isinstance(v, list):
        return v[0] if v else '?'
    return v or '?'


cc = collections.Counter(achatar(x.get('size')) for x in pf2)
print(f'\n  Pathfinder 2e — {len(pf2)} criaturas, {len(cc)} tamanhos')
print('    ' + '  ·  '.join(f'{k} {v}' for k, v in cc.most_common()))

TAM = re.compile(r'\*\*([\dTSML]+)\*\*<br/>\s*Size')
tds = collections.Counter(TAM.findall(dstx))
print(f'\n  Draw Steel — {sum(tds.values())} statblocks, {len(tds)} tamanhos, '
      f'e o tamanho é UM número (mais uma letra no 1)')
print('    ' + '  ·  '.join(f'{k} {v}' for k, v in tds.most_common()))

print('\n  ⚠ procurando footprint RETANGULAR de CORPO nos três:')
PAD = r'\b\d+\s*(?:feet|foot|ft\.?|squares?)?\s*(?:by|[x×])\s*\d+\s*(?:feet|foot|ft\.?|squares?)\b'
CORPO = r'(?:space|occupies|footprint|takes up)'
for rot, t in (('D&D 2024', ' '.join((a.get('desc') or '') for m in SRD['D&D 2024']
                                     for a in (m.get('actions') or []))),
               ('Draw Steel', dstx),
               ('PF2e', ' '.join(h.get('bloco') or '' for h in pf))):
    tot_ret = len(re.findall(PAD, t, re.I))
    de_corpo = len(re.findall(CORPO + r'[^.]{0,60}' + PAD, t, re.I))
    print(f'    {rot:<14}{tot_ret:>5} expressões "A por B" no total, '
          f'{de_corpo:>3} delas descrevendo o ESPAÇO de um corpo')

print('''
  ⟹ LEITURA B: nos TRES sistemas o corpo ocupa um QUADRADO, e o tamanho e UM
     numero (ou uma palavra). As expressoes "A por B" que aparecem sao todas
     AREA — linha e muro —, nunca o espaco de um corpo.
     Footprint retangular nao existe no campo.''')

bloco('FIM')

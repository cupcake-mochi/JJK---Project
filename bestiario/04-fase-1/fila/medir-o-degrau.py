# -*- coding: utf-8 -*-
"""MEDIDA — item `5`: "um degrau de categoria" perdeu tamanho único.

Tres secoes da peca 26 cobram em "degrau":
  §6.3  resistencia   -> "resistencia a `Fisicos` custa UM DEGRAU"
  §6.4  a Expansao    -> "ela custa um degrau... os dois degraus de baixo valem 2,00×"
  §6.5  vida efetiva  -> "o que da' vida efetiva paga em degrau"

Mas na escada NOVA os degraus nao tem o mesmo tamanho. Este script mede quanto
cada um vale, confere se os precos das tres secoes cabem em algum, e pergunta ao
campo se "um degrau da escada de dificuldade" e' unidade em algum lugar.
"""
import json, re, glob, os, sys, statistics as st
from collections import defaultdict

AQUI = os.path.dirname(os.path.abspath(__file__))
BEST = os.path.dirname(os.path.dirname(AQUI))
P26  = "/media/mizuki/HD Externo II/Claude/Claude 2/sistema/03-mecanica/26-bestiario.md"
R5   = os.path.join(BEST, '03-bloco', 'RASCUNHO-5-o-bloco-em-branco.md')

def ler(p):
    if not os.path.exists(p): sys.exit('DONO SUMIU: %s' % p)
    return open(p, encoding='utf-8').read()
def exige(c, m):
    if not c: sys.exit('ÂNCORA PERDIDA: ' + m)
def num(s): return float(s.replace('−','-').replace(',','.'))

# ─────────────────────────── a escada NOVA, lida do Passo 1 do RASCUNHO-5
ESCADA = []
for ln in ler(R5).split('\n'):
    m = re.match(r'\|\s*\*{0,2}`(\w+)`\*{0,2}\s*\|\s*([^|]*?)\s*\|\s*([^|]*?)\s*\|\s*\*{0,2}`?([\d,]+)`?\*{0,2}\s*\|\s*\*{0,2}`?(\d+)`?\*{0,2}\s*\|', ln)
    if m and m.group(1) in ('Capanga','Ameaça','Desastre','Catástrofe','Calamidade'):
        ESCADA.append((m.group(1), num(m.group(4)), int(m.group(5)), m.group(2).strip()))
exige(len(ESCADA) == 5, 'a escada do Passo 1 do RASCUNHO-5 mudou de forma (achei %d)' % len(ESCADA))

# ─────────────────────────── os preços que as três seções cobram
t26 = ler(P26)
PRECOS = {}
m = re.search(r'\|\s*`Físicos`\s*\|\s*`60%`\s*\|\s*\*{0,2}`([\d,]+)×`\*{0,2}\s*\|\s*\*{0,2}`([\d,]+)×`\*{0,2}', t26)
exige(m, 'a linha `Físicos` do §6.3 mudou de forma')
PRECOS['§6.3 · resistir a `Físicos`'] = num(m.group(1))
PRECOS['§6.3 · ser IMUNE a `Físicos`'] = num(m.group(2))
m = re.search(r'\|\s*`Elementais`\s*\|\s*`30%`\s*\|\s*`([\d,]+)×`', t26)
exige(m, 'a linha `Elementais` do §6.3 mudou de forma')
PRECOS['§6.3 · resistir a `Elementais`'] = num(m.group(1))
m = re.search(r'a Expansão completa multiplica a saída efetiva dele por `1 ÷ [\d,]+`, que é `([\d,]+) ×`', t26)
exige(m, 'o `1,92×` da Expansão do §6.4 mudou de forma')
PRECOS['§6.4 · a Expansão de Domínio'] = num(m.group(1))

print('=' * 84)
print('A ESCADA NOVA, e o tamanho de cada degrau')
print('=' * 84)
print('  %-12s %8s %7s   %s' % ('categoria','fator','ações','pede'))
for nome, fat, ac, pede in ESCADA:
    print('  %-12s %8.2f %7d   %s' % (nome, fat, ac, pede))
print()
print('  %-28s %10s' % ('o degrau', 'vale'))
degraus = []
for i in range(len(ESCADA) - 1):
    a, b = ESCADA[i], ESCADA[i+1]
    r = b[1] / a[1]
    degraus.append((f'{a[0]} → {b[0]}', r))
    print('  %-28s %9.3f×' % (f'{a[0]} → {b[0]}', r))
vals = [r for _, r in degraus]
print()
print('  ⟹ o menor degrau é %.3f× e o maior é %.3f× — espalha %.2f× entre eles.'
      % (min(vals), max(vals), max(vals)/min(vals)))

print()
print('=' * 84)
print('AS TRÊS SEÇÕES COBRAM EM "DEGRAU". Algum degrau serve?')
print('=' * 84)
print('  %-34s %9s   %s' % ('o que a peça cobra', 'vale', 'cabe em que degrau?'))
for rot, v in PRECOS.items():
    cabe = [(n, abs(r/v - 1)) for n, r in degraus]
    n_best, err = min(cabe, key=lambda x: x[1])
    veredito = ('%s (erra %.1f%%)' % (n_best, 100*err)) if err <= 0.10 else \
               ('⚠ NENHUM — o mais perto é %s, e erra %.1f%%' % (n_best, 100*err))
    print('  %-34s %8.3f×   %s' % (rot, v, veredito))

print()
print('  ⚠ E a frase do §6.4 fala de "os dois degraus de baixo da escada valem 2,00×".')
dois_de_baixo = [r for _, r in degraus[:2]]
print('    Na escada NOVA os dois de baixo valem %s — a frase é da escada MORTA.'
      % ' e '.join('%.3f×' % r for r in dois_de_baixo))

print()
print('=' * 84)
print('E "DOBRAR A CATEGORIA" (a regra do §6.4) — ela ainda pousa em alguma?')
print('=' * 84)
fatores = {n: f for n, f, _, _ in ESCADA}
for nome, fat, _, _ in ESCADA:
    alvo = fat * 2
    pouso = [n for n, f in fatores.items() if abs(f - alvo) < 1e-9]
    print('  %-12s %.2f × 2 = %.2f  ⟹  %s'
          % (nome, fat, alvo, pouso[0] if pouso else '⚠ não existe categoria com esse fator'))

print()
print('=' * 84)
print('O CAMPO — "um degrau da escada de dificuldade" é unidade em algum lugar?')
print('=' * 84)
def passo(pares, rot, chave):
    por = defaultdict(list)
    for k, v in pares: por[k].append(v)
    ks = sorted(por)
    passos = []
    for i in range(len(ks) - 1):
        a, b = st.median(por[ks[i]]), st.median(por[ks[i+1]])
        if a > 0: passos.append(b / a)
    if not passos: return
    print('  %-16s %s: %d degraus, de %.3f× a %.3f× — espalha %.2f×'
          % (rot, chave, len(passos), min(passos), max(passos), max(passos)/min(passos)))
for arq, rot in (('srd-2024.json','D&D SRD 2024'), ('srd-2014.json','D&D SRD 2014')):
    d = json.load(open(os.path.join(AQUI, arq), encoding='utf-8'))
    passo([(m_['challenge_rating'], m_['hit_points']) for m_ in d
           if m_.get('challenge_rating') is not None and m_.get('hit_points')], rot, 'HP por CR')
d = json.load(open(os.path.join(AQUI, 'pf2e-tamanho.json'), encoding='utf-8'))
passo([(m_['level'], m_['hp']) for m_ in d if m_.get('level') is not None and m_.get('hp')],
      'Pathfinder 2e', 'HP por nível')
arqs = sorted(glob.glob(os.path.join(AQUI, 'dados-recarga-area/data-md-main/Bestiary/Monsters/**/Statblocks/*.md'), recursive=True))
ds = []
for f in arqs:
    t = ler(f); fm = t.split('---')[1] if t.startswith('---') else ''
    mn = re.search(r'^level:\s*(\d+)\s*$', fm, re.M); ms = re.search(r"^stamina:\s*'?(\d+)'?\s*$", fm, re.M)
    if mn and ms: ds.append((int(mn.group(1)), int(ms.group(1))))
passo(ds, 'Draw Steel', 'Stamina por nível')

print()
print('  ⟹ Se o degrau do CAMPO também espalha, "um degrau" não é unidade em lugar nenhum,')
print('    e a moeda tem de ser o MULTIPLICADOR — que é o que o `Guia do Mestre` de 2014 já usa')
print('    na tabela de `Pontos de Vida Efetivos`, citada pelo próprio §6.3.')

# -*- coding: utf-8 -*-
"""MEDIDA — item `9`: quanto custa `1 Desastre + N Capangas`?

Somar os fatores nao serve, e a propria peca 26 §4.3 ja' mediu por que:
"Quatro `Ronda` nao valem uma `Alcateia`: elas cobram 0,75× a 0,77× o que ela cobra…
 eles morrem em fila e a saida deles despenca."

Este script simula a luta inteira com fogo concentrado — a mesma maquina que escolheu a
forma do `Capanga` — e devolve o FATOR EFETIVO do encontro misturado.

Toda ancora e' lida do dono.
"""
import re, os, sys, math
import statistics as st

AQUI = os.path.dirname(os.path.abspath(__file__))
BEST = os.path.dirname(os.path.dirname(AQUI))
P26  = "/media/mizuki/HD Externo II/Claude/Claude 2/sistema/03-mecanica/26-bestiario.md"
TAB  = os.path.join(BEST, '04-fase-1', 'TABELA.md')
R5   = os.path.join(BEST, '03-bloco', 'RASCUNHO-5-o-bloco-em-branco.md')

def ler(p):
    if not os.path.exists(p): sys.exit('DONO SUMIU: %s' % p)
    return open(p, encoding='utf-8').read()
def exige(c, m):
    if not c: sys.exit('ÂNCORA PERDIDA: ' + m)
def num(s): return float(s.replace('−','-').replace(',','.'))
def med(e):
    m = re.match(r'(\d+)d(\d+)(?:\s*\+\s*(\d+))?$', e.strip())
    if m: return int(m.group(1))*(1+int(m.group(2)))/2 + int(m.group(3) or 0)
    return float(e) if re.match(r'^\d+$', e.strip()) else None

# ───────────────────────────────── a TABELA
def secao(cat):
    t = ler(TAB)
    exige('## `%s`' % cat in t, 'a seção `%s` sumiu da TABELA' % cat)
    return t.split('## `%s`' % cat)[1].split('\n## ')[0]
def linhas(cat):
    cab, out = None, {}
    for ln in secao(cat).split('\n'):
        cels = [c.strip().strip('*').strip('`').strip('*') for c in ln.strip().strip('|').split('|')]
        if cels and cels[0] == 'nv': cab = cels
        elif cab and cels and re.match(r'^\d+$', cels[0] or ''):
            out[int(cels[0])] = dict(zip(cab, cels))
    return out
DES, CAPA = linhas('Desastre'), linhas('Capanga')
exige(DES and CAPA, 'as tabelas de `Desastre` e `Capanga` não foram lidas')

# ───────────────────────────────── as âncoras de regra
t26 = ler(P26)
VEZES = num(re.search(r'tem `(\d+) ×` o dano de rodada do grupo em vida', t26).group(1))
PCT   = num(re.search(r'O chefe entrega `(\d+)%` da vida de um personagem por rodada', t26).group(1)) / 100
# `Ronda` virou `Ameaça` e `Alcateia` virou `Desastre` na escada viva (v0.221)
m = re.search(r'\*\*Quatro `Ameaça` não valem um `Desastre`: elas cobram `([\d,]+) ×` a `([\d,]+) ×`', t26)
exige(m, 'o `0,75×`–`0,77×` do §4.3 sumiu da peça 26')
AMEACA = (num(m.group(1)), num(m.group(2)))
# a fração do §4.5 passou a sair com UMA CASA na v0.221 — `67,6%`, e não `68%`
m = re.search(r'\|\s*\*\*`sozinho`\*\*\s*\|\s*`100%`\s*\|\s*—\s*\|\s*`([\d,]+)%`', t26)
exige(m, 'a linha `sozinho` do §4.5 sumiu da peça 26')
COBRA_SOZINHO = num(m.group(1)) / 100
MESA = int(re.search(r'\|\s*\*\*`Desastre`\*\*\s*\|\s*`(\d+)` — a mesa padrão', ler(R5)).group(1))
FAT = {}
for ln in ler(R5).split('\n'):
    mm = re.match(r'\|\s*\*{0,2}`(\w+)`\*{0,2}\s*\|[^|]*\|[^|]*\|\s*\*{0,2}`?([\d,]+)`?\*{0,2}\s*\|', ln)
    if mm and mm.group(1) in ('Capanga','Ameaça','Desastre','Catástrofe','Calamidade'):
        FAT[mm.group(1)] = num(mm.group(2))
exige(len(FAT) == 5, 'a escada de fatores do Passo 1 do RASCUNHO-5 mudou de forma')
mt = re.search(r'No máximo `(\d+)` corpos do mesmo esquadrão atacam o mesmo alvo por rodada', ler(R5))
exige(mt, 'o teto de empilhamento sumiu do RASCUNHO-5')
TETO_PILHA = int(mt.group(1))

NIVEIS = sorted(set(DES) & set(CAPA))

# ───────────────────────────────── o motor
def mundo(nv):
    d = DES[nv]
    vida_chefe = float(d['vida']); dano_chefe = float(d['dano/rod'])
    saida_grupo = vida_chefe / VEZES
    vida_pj = dano_chefe / PCT
    vida_capanga = saida_grupo / 4          # a escada: "dano do grupo ÷ 4"
    golpe_capanga = med(CAPA[nv]['golpe de um'])
    return dict(nv=nv, vida_chefe=vida_chefe, dano_chefe=dano_chefe, saida=saida_grupo,
                vida_pj=vida_pj, vida_cap=vida_capanga, golpe_cap=golpe_capanga,
                grupo_hp=MESA * vida_pj)

def luta(w, f_chefe, n_cap, mesa=None):
    """Fogo concentrado, capangas primeiro (ordem declarada no §4.5).
    `mesa` muda o tamanho do grupo: a saída é proporcional ao número de gente.
    Devolve o dano TOTAL que os inimigos entregam na luta."""
    mesa = mesa or MESA
    saida = w['saida'] * mesa / MESA
    vc = w['vida_chefe'] * f_chefe
    dc = w['dano_chefe'] * f_chefe
    pool_cap = n_cap * w['vida_cap']
    total, rod = 0.0, 0
    while (pool_cap > 0 or vc > 0) and rod < 60:
        rod += 1
        vivos = min(n_cap, math.ceil(pool_cap / w['vida_cap'])) if pool_cap > 0 else 0
        total += vivos * w['golpe_cap'] + (dc if vc > 0 else 0)
        if pool_cap > 0:
            gasto = min(pool_cap, saida)
            pool_cap -= gasto
            vc -= (saida - gasto)               # a sobra vai pro chefe na mesma rodada
        else:
            vc -= saida
    return total, rod

def fator_equivalente(w, dano_total):
    """Que chefe SOZINHO cobraria isso? A cobrança de um solo cresce com F²."""
    unidade = w['dano_chefe'] * w['vida_chefe'] / w['saida']    # a cobrança de F = 1
    return math.sqrt(dano_total / unidade)

# ───────────────────────────────── saída
print('=' * 92)
print('ÂNCORAS')
print('=' * 92)
print('  peça 26: chefe tem %.0f× o dano do grupo em vida · entrega %.0f%% da vida de um PJ por rodada'
      % (VEZES, 100*PCT))
print('  §4.3: quatro `Ameaça` cobram %.2f×–%.2f× um `Desastre`' % AMEACA)
print('  §4.5: o chefe `sozinho` cobra %.0f%% da vida do grupo' % (100*COBRA_SOZINHO))
print('  escada: ' + ' · '.join('%s %.2f' % (k, v) for k, v in FAT.items()))
print('  mesa padrão %d · teto de empilhamento %d corpos' % (MESA, TETO_PILHA))

w0 = mundo(NIVEIS[len(NIVEIS)//2])
print()
print('=' * 92)
print('PRIMEIRO: o modelo reproduz o `%.0f%%` publicado do chefe sozinho?' % (100*COBRA_SOZINHO))
print('=' * 92)
print('  %4s %10s %10s %8s' % ('nv', 'cobra', 'publicado', 'bate?'))
bate = 0
for nv in NIVEIS:
    w = mundo(nv)
    d, _ = luta(w, FAT['Desastre'], 0)
    p = d / w['grupo_hp']
    ok = abs(p - COBRA_SOZINHO) <= 0.02
    bate += ok
    if nv in (NIVEIS[0], 7, 20, NIVEIS[-1]):
        print('  %4d %9.1f%% %9.0f%% %8s' % (nv, 100*p, 100*COBRA_SOZINHO, 'sim' if ok else 'NÃO'))
print('  ⟹ bate em %d de %d níveis.' % (bate, len(NIVEIS)))
exige(bate >= len(NIVEIS) * 0.8, 'o modelo NÃO reproduz o número publicado — não dá pra confiar nele')

print()
print('=' * 92)
print('A CONTA — `1 Desastre` + N `Capanga`, e quanto ela custa DE VERDADE')
print('=' * 92)
print('  %-26s %9s %11s %11s %9s' % ('o encontro', 'cobra', 'soma ingênua', 'fator real', 'a soma erra'))
res = {}
for n_cap in range(0, 9):
    ps, fs = [], []
    for nv in NIVEIS:
        w = mundo(nv)
        d, _ = luta(w, FAT['Desastre'], n_cap)
        ps.append(d / w['grupo_hp'])
        fs.append(fator_equivalente(w, d))
    ingenua = FAT['Desastre'] + n_cap * FAT['Capanga']
    real = st.mean(fs)
    res[n_cap] = (st.mean(ps), ingenua, real)
    rot = '1 Desastre' + (' + %d Capanga%s' % (n_cap, 's' if n_cap > 1 else '') if n_cap else ' sozinho')
    print('  %-26s %8.1f%% %11.2f %11.2f %8.1f%%'
          % (rot, 100*st.mean(ps), ingenua, real, 100*(ingenua/real - 1)))

print()
print('=' * 92)
print('A RÉGUA — o capanga vale quanto, quando ele é ACRESCENTADO a um chefe inteiro?')
print('=' * 92)
base = res[0][2]
print('  %-14s %12s %12s %12s' % ('N capangas', 'fator real', 'o que ele somou', 'por capanga'))
for n in range(1, 9):
    real = res[n][2]
    somou = real - base
    print('  %-14d %12.3f %12.3f %12.3f' % (n, real, somou, somou / n))
por = [(res[n][2] - base) / n for n in range(1, 9)]
print()
print('  ⟹ cada capanga acrescentado vale de %.3f a %.3f de fator, média %.3f.'
      % (min(por), max(por), st.mean(por)))
print('    A tabela vende ele por %.3f ⟹ a soma ingênua paga %.1f%% A MAIS do que ele entrega.'
      % (FAT['Capanga'], 100*(FAT['Capanga']/st.mean(por) - 1)))
print()
print('  E isso é a MESMA propriedade que o §4.3 já mediu:')
print('    lá, quatro corpos de 1/4 cobram %.2f×–%.2f× um corpo inteiro.' % AMEACA)
razao_4 = (res[4][2] - base) / (4 * FAT['Capanga'])
print('    aqui, quatro capangas somados cobram %.3f× o que os fatores deles prometem.' % razao_4)


# ═══════════════════════════════════════════ validação contra o §4.5
print()
print('=' * 92)
print('VALIDAÇÃO — o modelo reproduz as OUTRAS TRÊS linhas do §4.5?')
print('=' * 92)
SUB = {}
for ln in t26.split('\n'):
    # v0.221: as duas frações passaram a sair com UMA CASA — `91,5%` e `67,5%`.
    # A própria peça declara por quê: meio ponto percentual atravessa a borda de uma rodada.
    mm = re.match(r'\|\s*\*{0,2}`(\w+[\w ]*)`\*{0,2}\s*\|\s*`([\d,]+)%`\s*\|\s*`?([—\d]+)`?\s*\|\s*`([\d,]+)%`\s*\|', ln)
    if mm: SUB[mm.group(1)] = (num(mm.group(2))/100, 0 if mm.group(3)=='—' else int(mm.group(3)), num(mm.group(4))/100)
exige(len(SUB) >= 4, 'a tabela do §4.5 não foi lida (achei %d linhas)' % len(SUB))
print('  %-16s %8s %8s %10s %10s %s' % ('sub-categoria','chefe','capangas','publicado','medido','bate?'))
ok_all = 0
for nome, (frac, ncap, pub) in SUB.items():
    ps = [luta(mundo(nv), FAT['Desastre']*frac, ncap)[0] / mundo(nv)['grupo_hp'] for nv in NIVEIS]
    m_ = st.mean(ps); ok = abs(m_ - pub) <= 0.03
    ok_all += ok
    print('  %-16s %7.0f%% %8d %9.0f%% %9.1f%% %s' % (nome, 100*frac, ncap, 100*pub, 100*m_, 'sim' if ok else '⚠ NÃO'))
print('  ⟹ %d de %d linhas do §4.5 reproduzem.' % (ok_all, len(SUB)))

# ═══════════════════════════════════════════ a leitura que a peça usa: PESSOAS
print()
print('=' * 92)
print('E AGORA PELA DEFINIÇÃO DA PEÇA — "a categoria é quantos personagens ele exige"')
print('=' * 92)
print('  Um `Desastre` sozinho cobra %.0f%% de uma mesa de %d. A pergunta certa é:' % (100*COBRA_SOZINHO, MESA))
print('  de que tamanho a mesa precisa ser pra o encontro misturado cobrar os MESMOS %.0f%%?' % (100*COBRA_SOZINHO))
print()
def pessoas_que_ele_exige(n_cap, f_chefe=1.0):
    """acha a mesa N em que o encontro cobra COBRA_SOZINHO da vida dela."""
    lo, hi = 1.0, 40.0
    for _ in range(60):
        mid = (lo + hi) / 2
        ps = []
        for nv in NIVEIS:
            w = mundo(nv)
            d, _ = luta(w, f_chefe, n_cap, mesa=mid)
            ps.append(d / (mid * w['vida_pj']))
        (lo, hi) = (mid, hi) if st.mean(ps) > COBRA_SOZINHO else (lo, mid)
    return (lo + hi) / 2

print('  %-26s %12s %12s %12s %10s' % ('o encontro','pessoas','fator = /4','soma ingênua','a soma erra'))
tab = {}
for n_cap in range(0, 9):
    N = pessoas_que_ele_exige(n_cap)
    f = N / MESA
    ing = FAT['Desastre'] + n_cap * FAT['Capanga']
    tab[n_cap] = (N, f, ing)
    rot = '1 Desastre' + (' + %d Capanga%s' % (n_cap, 's' if n_cap>1 else '') if n_cap else ' sozinho')
    print('  %-26s %12.2f %12.3f %12.2f %9.1f%%' % (rot, N, f, ing, 100*(ing/f - 1)))

print()
base_f = tab[0][1]
por = [(tab[n][1] - base_f) / n for n in range(1, 9)]
print('  ⟹ cada capanga ACRESCENTADO a um chefe inteiro vale %.3f a %.3f de fator (média %.3f).'
      % (min(por), max(por), st.mean(por)))
print('    A escada vende ele por %.3f — ou seja, ela cobra %.2f× o que ele entrega quando é somado.'
      % (FAT['Capanga'], FAT['Capanga'] / st.mean(por)))
print()
print('  E o `%d Capangas` sozinhos, sem chefe, pra comparar com o §4.3:' % MESA)
for n in (4, 8):
    N = pessoas_que_ele_exige(n, f_chefe=0.0)
    print('    %d capangas sem chefe: exige %.2f pessoas ⟹ fator %.3f, contra %.2f de soma ingênua'
          % (n, N, N/MESA, n*FAT['Capanga']))

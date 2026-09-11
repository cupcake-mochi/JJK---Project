#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
O `tamanho` NOS TRES SISTEMAS — Draw Steel, D&D 2024 e Pathfinder 2e.

Pedido do Mizuki, 10/09/2026: "Valida com os outros exemplos q temos, Draw Steel,
D&D e Pathfinder, deve ter auxilios nas versoes atualizadas para que sirva como
calculo e media pra gente."

Duas perguntas:
  1. o tamanho MEXE na defesa? (a nossa troca cobra em Defesa)
  2. o tamanho ADICIONA orcamento de atributo, ou so' muda a forma dele?

E uma terceira, que fecha a saida `F`:
  3. quanto o tamanho GANHA no campo? (pra saber ate' onde encolher o nosso)

Amostras:  Draw Steel 415 statblocks · D&D 2024 SRD 331 · PF2e 4791
"""
import json
import os
import re
import statistics
import sys

BEST = os.environ.get('JJK_BEST', '/media/mizuki/HD Externo II/Claude/Claude 2/bestiario')
FILA = os.path.join(BEST, '04-fase-1/fila')
DS = os.path.join(FILA, 'dados-recarga-area/data-md-main')
STAT = os.path.join(DS, 'Bestiary/Monsters/Monsters')

ATRIB = ('strength', 'dexterity', 'constitution', 'intelligence', 'wisdom', 'charisma')
ORDEM6 = ['Tiny', 'Small', 'Medium', 'Large', 'Huge', 'Gargantuan']
ORDEM_DS = ['1T', '1S', '1M', '1L', '2', '3', '4', '5']
# como os seis degraus do campo mapeiam nos nossos
NOSSO = {'Tiny': 'Minúsculo', 'Small': 'Pequeno', 'Medium': 'Médio',
         'Large': 'Grande', 'Huge': 'Imenso', 'Gargantuan': 'Colossal'}


def bloco(t):
    print()
    print('=' * 98)
    print(t)
    print('=' * 98)


def med(xs):
    return statistics.median(xs) if xs else None


def normaliza(itens, chave_coorte, campo):
    """Devolve {valor_do_campo: mediana da razao contra a mediana da coorte}."""
    co = {}
    for it in itens:
        co.setdefault(chave_coorte(it), []).append(it)
    out = {}
    for it in itens:
        g = [x[campo] for x in co[chave_coorte(it)] if x.get(campo) is not None]
        m = med(g)
        if m and it.get(campo) is not None:
            out.setdefault(it['sz'], []).append(it[campo] / m)
    return {k: (med(v), len(v)) for k, v in out.items()}


# ============================================================ D&D 2024 SRD
DND = []
for m in json.load(open(os.path.join(FILA, 'srd-2024.json'), encoding='utf-8')):
    sz = (m.get('size') or {}).get('name')
    a = m.get('ability_scores') or {}
    if not sz or m.get('challenge_rating') is None:
        continue
    DND.append({'nome': m['name'], 'sz': sz, 'cr': m['challenge_rating'],
                'ac': m.get('armor_class'), 'hp': m.get('hit_points'),
                'dex': a.get('dexterity'),
                'soma': sum(a[k] for k in ATRIB) if all(k in a for k in ATRIB) else None})

# ============================================================ Pathfinder 2e
PF = []
for m in json.load(open(os.path.join(FILA, 'pf2e-tamanho.json'), encoding='utf-8')):
    s = m.get('size')
    sz = (s[0] if isinstance(s, list) and s else s)
    if not sz or m.get('level') is None or m.get('ac') is None:
        continue
    tem = all(isinstance(m.get(k), (int, float)) for k in ATRIB)
    PF.append({'nome': m.get('name'), 'sz': sz, 'nv': m['level'],
               'ac': m.get('ac'), 'hp': m.get('hp'), 'dex': m.get('dexterity'),
               'soma': sum(m[k] for k in ATRIB) if tem else None})

# ============================================================ Draw Steel
DSC, MEL = [], {}
PAT = re.compile(r'📏 Melee (\d+)\*{0,2}\s*\|\s*\*{0,2}🎯 ([^*|]+)')
NUM = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6}
for dp, _, fs in os.walk(STAT):
    if 'Statblocks' not in dp:
        continue
    for f in sorted(fs):
        if not f.endswith('.md'):
            continue
        txt = open(os.path.join(dp, f), encoding='utf-8').read()
        mfm = re.search(r'^---\n(.*?)\n---', txt, re.S)
        if not mfm:
            continue
        fm = mfm.group(1)

        def c(k):
            mm = re.search(r'^' + k + r': (.+)$', fm, re.M)
            return mm.group(1).strip().strip("'\"") if mm else None

        sz, lv, st = c('size'), c('level'), c('stamina')
        if not (sz and lv and st):
            continue
        mr = re.search(r'^roles:\n((?:  - .+\n)+)', fm, re.M)
        ps = [x.strip() for x in re.findall(r'^  - (.+)$', mr.group(1), re.M)] if mr else []
        org = ps[0].split()[0] if ps and ps[0].split()[0] in (
            'Minion', 'Horde', 'Platoon', 'Elite', 'Leader', 'Solo') else '?'
        at = {}
        for a in ('might', 'agility', 'reason', 'intuition', 'presence'):
            v = c(a)
            at[a] = int(v) if v and re.match(r'^-?\d+$', v) else None
        DSC.append({'nome': f[:-3], 'sz': sz, 'org': org,
                    'nv': int(re.match(r'-?\d+', lv).group(0)),
                    'stamina': int(re.match(r'-?\d+', st).group(0)),
                    'soma': sum(at.values()) if all(v is not None for v in at.values()) else None})
        for d, a in PAT.findall(txt):
            t2 = a.strip().lower()
            if t2.startswith('self'):
                continue
            k = 1 if t2.startswith('the triggering') else NUM.get(t2.split()[0])
            if k:
                MEL.setdefault(sz, []).append((int(d), k))

if len(DND) < 300 or len(PF) < 4000 or len(DSC) < 380:
    print(f'  !! amostra curta: D&D {len(DND)} · PF2e {len(PF)} · Draw Steel {len(DSC)}')
    sys.exit(1)


bloco('AS AMOSTRAS')
print(f'  Draw Steel      {len(DSC):>5} statblocks   (sem estatística de defesa — power roll)')
print(f'  D&D 2024 SRD    {len(DND):>5} monstros     size · CR · AC · HP · 6 atributos')
print(f'  Pathfinder 2e   {len(PF):>5} criaturas    size · nível · AC · HP · 6 atributos')


bloco('1. O TAMANHO MEXE NA DEFESA? — a pergunta que o nosso `tamanho` responde com `−7`')
print()
print('  Normalizado por coorte de desafio (CR no D&D, nível no PF2e).')
print()
ac_dnd = normaliza(DND, lambda x: x['cr'], 'ac')
ac_pf = normaliza(PF, lambda x: x['nv'], 'ac')
print(f'  {"tamanho":<12}{"o nosso":<12}{"D&D 2024: AC rel.":>22}{"n":>6}'
      f'{"PF2e: AC rel.":>18}{"n":>7}')
print('  ' + '-' * 80)
for s in ORDEM6:
    a, na = ac_dnd.get(s, (None, 0))
    b, nb = ac_pf.get(s, (None, 0))
    print(f'  {s:<12}{NOSSO[s]:<12}'
          f'{(f"{a:.3f}" if a else "—"):>22}{na:>6}{(f"{b:.3f}" if b else "—"):>18}{nb:>7}')
print()
va = [v for s in ORDEM6 if (v := ac_dnd.get(s, (None,))[0])]
vb = [v for s in ORDEM6 if (v := ac_pf.get(s, (None,))[0])]
print(f'  >> D&D 2024: a AC vai de {min(va):.3f} a {max(va):.3f} — espalha {max(va)/min(va):.3f} ×')
print(f'  >> PF2e:     a AC vai de {min(vb):.3f} a {max(vb):.3f} — espalha {max(vb)/min(vb):.3f} ×')
print(f'  >> Draw Steel: NAO TEM defesa. Ataque e' + ' power roll contra faixa.')
print()
print(f'  E o NOSSO: `Colossal` pede Defesa {7} pontos abaixo do `Médio`.')
print(f'  Num nv20 isso e' + ' 18 -> 11, uma razao de {:.3f} ×.'.format(11/18))


bloco('2. E O DEX? — porque a NOSSA Defesa lê a Destreza')
print()
dx_dnd = normaliza(DND, lambda x: x['cr'], 'dex')
dx_pf = normaliza(PF, lambda x: x['nv'], 'dex')
print(f'  {"tamanho":<12}{"D&D: Dex rel.":>18}{"n":>6}{"PF2e: Dex rel.":>18}{"n":>7}')
print('  ' + '-' * 62)
for s in ORDEM6:
    a, na = dx_dnd.get(s, (None, 0))
    b, nb = dx_pf.get(s, (None, 0))
    print(f'  {s:<12}{(f"{a:.3f}" if a is not None else "—"):>18}{na:>6}'
          f'{(f"{b:.3f}" if b is not None else "—"):>18}{nb:>7}')
print()
gd = dx_dnd.get('Gargantuan', (None, 0))
gp = dx_pf.get('Gargantuan', (None, 0))
md_ = dx_dnd.get('Medium', (None, 0))[0]
mp_ = dx_pf.get('Medium', (None, 0))[0]
print(f'  >> D&D 2024: Gargantuan {gd[0]:.3f} contra Medium {md_:.3f}  (n={gd[1]} — amostra pequena)')
print(f'  >> PF2e:     Gargantuan {gp[0]:.3f} contra Medium {mp_:.3f}  (n={gp[1]})')
if gp[0] < 0.98 and gd[0] >= 0.98:
    print('  >> So' + ' o PF2e mostra bicho gigante com menos Destreza, e por ' +
          f'{1-gp[0]:.1%}. O D&D nao mostra —')
    print('     mas o n de Gargantuan no SRD e' + f' {gd[1]}, pequeno demais pra afirmar.')
print('  >> A pergunta que importa e' + ' se ele GANHA os pontos de volta. E' + ' a secao 3.')


bloco('3. ⚠ O TAMANHO ADICIONA ORÇAMENTO DE ATRIBUTO? — a 2ª pergunta do martelo')
print()
sm_dnd = normaliza(DND, lambda x: x['cr'], 'soma')
sm_pf = normaliza(PF, lambda x: x['nv'], 'soma')
co_ds = {}
for x in DSC:
    co_ds.setdefault((x['org'], x['nv']), []).append(x)
sm_ds = {}
for x in DSC:
    g = [y['soma'] for y in co_ds[(x['org'], x['nv'])] if y['soma'] is not None]
    m = med(g)
    if m and x['soma'] is not None and m != 0:
        sm_ds.setdefault(x['sz'], []).append(x['soma'] / m)
sm_ds = {k: (med(v), len(v)) for k, v in sm_ds.items()}

print(f'  {"tamanho":<12}{"D&D 2024":>14}{"n":>6}{"PF2e":>12}{"n":>7}')
print('  ' + '-' * 54)
for s in ORDEM6:
    a, na = sm_dnd.get(s, (None, 0))
    b, nb = sm_pf.get(s, (None, 0))
    print(f'  {s:<12}{(f"{a:.3f}" if a else "—"):>14}{na:>6}{(f"{b:.3f}" if b else "—"):>12}{nb:>7}')
print()
print('  Draw Steel (Σ dos cinco, normalizado por organização + nível):')
print('   ', '  '.join(f'{s} {sm_ds[s][0]:.3f}' for s in ORDEM_DS if s in sm_ds and sm_ds[s][1] >= 3))
print()
for rot, tab in (('D&D 2024', sm_dnd), ('PF2e', sm_pf)):
    v = [x for s in ORDEM6 if (x := tab.get(s, (None,))[0])]
    if len(v) >= 4:
        peq = tab.get('Medium', (None,))[0]
        gra = tab.get('Gargantuan', (None,))[0] or tab.get('Huge', (None,))[0]
        print(f'  >> {rot}: Medium {peq:.3f} → o maior {gra:.3f}   '
              f'({"CRESCE " + f"{gra/peq:.2f} ×" if gra > peq * 1.02 else "não cresce"})')
v = [sm_ds[s][0] for s in ORDEM_DS if s in sm_ds and sm_ds[s][1] >= 3]
print(f'  >> Draw Steel: de {min(v):.3f} a {max(v):.3f} — espalha {max(v)/min(v):.3f} ×')


bloco('4. QUANTO O TAMANHO GANHA NO CAMPO? — o número que a saída `F` precisa')
print()
print('  A saida `F` e' + ' "nao cobra, e encolhe o ganho ate' + ' o tamanho do campo".')
print('  Entao: quanto o tamanho ganha la, medido em ALVOS por acao de corpo a corpo?')
print()
print(f'  {"size":<6}{"ações":>8}{"alvos esperados":>18}{"vs size 1M":>13}   o nosso equivalente')
print('  ' + '-' * 78)
base = None
NOSSO_GANHO = {'1M': ('Médio', 1.0000), '2': ('Grande', 1.2153),
               '3': ('Imenso', 1.4321), '4': ('Colossal', 1.6500)}
for s in ORDEM_DS:
    v = MEL.get(s, [])
    if len(v) < 4:
        continue
    esp = statistics.mean([x[1] for x in v])
    if s == '1M':
        base = esp
    rel = esp / base if base else float('nan')
    eq = NOSSO_GANHO.get(s)
    extra = f'{eq[0]} = {eq[1]:.4f} ×' if eq else ''
    print(f'  {s:<6}{len(v):>8}{esp:>18.3f}{rel:>13.3f}   {extra}')
print()
gr = [x[1] for s, v in MEL.items() if not s.startswith('1') for x in v]
pq = [x[1] for s, v in MEL.items() if s.startswith('1') for x in v]
if gr and pq:
    g, p = statistics.mean(gr), statistics.mean(pq)
    print(f'  >> juntando: size 1 entrega {p:.3f} alvos por ação · size 2+ entrega {g:.3f}')
    print(f'  >> o ganho de tamanho no campo e' + f' {g/p:.3f} ×, do menor pro maior degrau.')
    print()
    print(f'  ⚠ E o NOSSO topo e' + ' 1,650 × — {:.2f} × o do campo.'.format(1.65 / (g / p)))

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
O `Controlador` no ESQUADRAO — validado contra o Draw Steel.

Pedido do Mizuki, 10/09/2026: "valide em comparacao ao Draw Steel, foi de la q
pegamos a ideia, ent deve ter uma metrica q podemos roubar e adaptar".

A pergunta: a forma `B` preca o `Controlador` com `(1 + 1/ações)`. No `Capanga`,
`ações` e 1 (por corpo) ou 8 (por esquadrao)? As duas fecham em 1,000 no
invariante e dao 0,67x contra 1,01x de encontro.

O Draw Steel tem `Minion Controller` — 6 deles — e tem `Controller` em toda
organizacao. Entao da pra medir se o Controller DELES paga em Stamina, e quanto.

Nenhum numero nosso mora aqui: as ancoras sao lidas dos documentos donos.
"""
import os
import re
import statistics
import sys

BEST = os.environ.get('JJK_BEST', '/media/mizuki/HD Externo II/Claude/Claude 2/bestiario')
DS = os.path.join(BEST, '04-fase-1/fila/dados-recarga-area/data-md-main')
STAT = os.path.join(DS, 'Bestiary/Monsters/Monsters')
BASICS = os.path.join(DS, 'Bestiary/Monsters/Chapters/Monster Basics.md')

CONTROL = '04-fase-1/papel/DECIDIDO-o-controlador-por-categoria.md'
ESCADA = '04-fase-1/a-escada-com-numero.md'
BLOCO = '03-bloco/RASCUNHO-5-o-bloco-em-branco.md'

_cache = {}


def ler(rel, raiz=BEST):
    k = (rel, raiz)
    if k not in _cache:
        with open(os.path.join(raiz, rel), encoding='utf-8') as f:
            _cache[k] = f.read()
    return _cache[k]


def n(s):
    return float(s.replace('−', '-').replace(',', '.'))


def pega(rel, padrao, rotulo, raiz=BEST):
    m = re.search(padrao, ler(rel, raiz))
    if not m:
        print(f'\n  !! ANCORA PERDIDA: {rotulo}\n     nao casa em {rel}\n     padrao: {padrao}')
        sys.exit(1)
    return m


def bloco(t):
    print()
    print('=' * 96)
    print(t)
    print('=' * 96)


# ------------------------------------------------------------- as nossas ancoras
CORPOS = int(pega(ESCADA,
                  r'\| \*\*`Capanga`\*\* \| — \| `dano do grupo ÷ 4` \| `[\d,]+` \| `1` \| `(\d+)`',
                  'os corpos do `Capanga`').group(1))
mc = pega(CONTROL, r'\| `Ameaça` \| `1` \| `([\d,]+)×` \| \*\*`× ([\d,]+)`\*\*',
          'a forma B em 1 ação')
POR_CORPO_GANHA, POR_CORPO_PAGA = n(mc.group(1)), n(mc.group(2))
POR_ESQ_GANHA = 1 + 1 / CORPOS
POR_ESQ_PAGA = 1 / POR_ESQ_GANHA

# ------------------------------------------------------------- o Draw Steel
def num(s):
    s = s.strip().strip("'\"")
    m = re.match(r'^-?\d+', s)
    return int(m.group(0)) if m else None


CRIA = []
for dp, _, fs in os.walk(STAT):
    if 'Statblocks' not in dp:
        continue
    for f in sorted(fs):
        if not f.endswith('.md'):
            continue
        t = ler(os.path.join(dp, f), raiz='/')
        m = re.search(r'^---\n(.*?)\n---', t, re.S)
        if not m:
            continue
        fm = m.group(1)
        mr = re.search(r'^roles:\n((?:  - .+\n)+)', fm, re.M)
        if not mr:
            continue
        papeis = [x.strip() for x in re.findall(r'^  - (.+)$', mr.group(1), re.M)]
        if len(papeis) != 1 or papeis[0] == r'\-':
            continue
        p = papeis[0].split()
        org = p[0] if p[0] in ('Minion', 'Horde', 'Platoon', 'Elite', 'Leader', 'Solo') else '(sem)'
        rol = ' '.join(p[1:]) if org != '(sem)' else papeis[0]
        rol = rol or org           # Leader e Solo nao tem papel
        lv = num(re.search(r'^level: (.+)$', fm, re.M).group(1)) if re.search(r'^level: ', fm, re.M) else None
        st = num(re.search(r'^stamina: (.+)$', fm, re.M).group(1)) if re.search(r'^stamina: ', fm, re.M) else None
        fs_ = num(re.search(r'^free_strike: (.+)$', fm, re.M).group(1)) if re.search(r'^free_strike: ', fm, re.M) else None
        mev = re.search(r'^ev: (.+)$', fm, re.M)
        ev = None
        if mev:
            e = mev.group(1).strip().strip("'\"")
            mm = re.match(r'^(\d+) for (\d+|four) minions?$', e)
            if mm:
                q = 4 if mm.group(2) == 'four' else int(mm.group(2))
                ev = int(mm.group(1)) / q          # EV POR CORPO
            elif re.match(r'^\d+$', e):
                ev = float(e)
        if lv is None or st is None:
            continue
        CRIA.append({'nome': f[:-3], 'org': org, 'papel': rol, 'nv': lv,
                     'stamina': st, 'ev': ev, 'fs': fs_})

if len(CRIA) < 380:
    print(f'  !! li so {len(CRIA)} statblocks — o dump mudou?')
    sys.exit(1)


bloco('AS ANCORAS')
print(f'  os corpos do `Capanga`                  {CORPOS}                      a escada fechada')
print(f'  a forma B por CORPO   (`ações` = 1)     ganha {POR_CORPO_GANHA:.3f}× · paga vida × {POR_CORPO_PAGA:.3f}')
print(f'  a forma B por ESQUADRÃO (`ações` = {CORPOS})   ganha {POR_ESQ_GANHA:.3f}× · paga vida × {POR_ESQ_PAGA:.3f}')
print(f'  statblocks do Draw Steel lidos          {len(CRIA)}')


bloco('1. O `Controller` EXISTE em minion? E o que o livro DIZ dele?')
mm = re.search(r'##### Controller\n\n(.+?)\n', ler(BASICS, raiz='/'))
md = re.search(r'##### Defender\n\n(.+?)\n', ler(BASICS, raiz='/'))
mrole = re.search(r'#### Creature Roles\n\n(.+?)\n', ler(BASICS, raiz='/'))
print()
print('  O que o livro escreve sobre PAPEL:')
print(f'    "{mrole.group(1)[:180]}..."')
print()
print('  O que ele escreve sobre o Controller:')
print(f'    "{mm.group(1)}"')
print()
print('  E sobre o Defender, que e o oposto dele:')
print(f'    "{md.group(1)}"')
print()
por_org = {}
for c in CRIA:
    por_org.setdefault(c['org'], {}).setdefault(c['papel'], []).append(c)
print(f'  {"organização":<12}{"quantos":>9}{"tem Controller?":>18}{"quantos":>9}')
print('  ' + '-' * 50)
for o in ('Minion', 'Horde', 'Platoon', 'Elite', 'Leader', 'Solo'):
    if o not in por_org:
        continue
    tot = sum(len(v) for v in por_org[o].values())
    ctrl = len(por_org[o].get('Controller', []))
    print(f'  {o:<12}{tot:>9}{("sim" if ctrl else "NÃO"):>18}{ctrl:>9}')
print()
print('  >> `Leader` e `Solo` NAO tem papel — o livro escreve isso com todas as letras.')
print('     E o `Minion` TEM. E a mesma linha que a gente desenhou: papel no cabecalho,')
print('     de `Capanga` a `Calamidade`, menos onde a organizacao ja e o papel.')


bloco('2. O `Controller` PAGA em Stamina? — normalizado por nível e organização')
print()
print('  Cada criatura vira uma razao contra a MEDIANA da coorte (mesma organizacao, mesmo')
print('  nivel). Assim nivel e organizacao saem da conta e sobra o papel.')
print()
coorte = {}
for c in CRIA:
    coorte.setdefault((c['org'], c['nv']), []).append(c)
for c in CRIA:
    grupo = [x['stamina'] for x in coorte[(c['org'], c['nv'])]]
    med = statistics.median(grupo)
    c['rel'] = c['stamina'] / med if med else None
    c['coorte'] = len(grupo)

print(f'  {"papel":<12}{"n":>5}{"stamina rel. à mediana":>26}{"mediana":>10}{"leitura":>26}')
print('  ' + '-' * 80)
por_papel = {}
for c in CRIA:
    if c['rel'] is None or c['coorte'] < 3:
        continue
    por_papel.setdefault(c['papel'], []).append(c['rel'])
for p, v in sorted(por_papel.items(), key=lambda kv: statistics.median(kv[1])):
    if len(v) < 5:
        continue
    m = statistics.median(v)
    leitura = 'mais duro' if m > 1.02 else ('mais mole' if m < 0.98 else 'na mediana')
    print(f'  {p:<12}{len(v):>5}{m:>26.3f}{m:>10.2f}×{leitura:>26}')
print()
ctrl_all = [c['rel'] for c in CRIA if c['papel'] == 'Controller' and c['rel'] and c['coorte'] >= 3]
def_all = [c['rel'] for c in CRIA if c['papel'] == 'Defender' and c['rel'] and c['coorte'] >= 3]
if ctrl_all and def_all:
    print(f'  >> Controller: mediana {statistics.median(ctrl_all):.3f} × a coorte  (n={len(ctrl_all)})')
    print(f'  >> Defender:   mediana {statistics.median(def_all):.3f} × a coorte  (n={len(def_all)})')
    print(f'  >> a distancia entre os dois e {statistics.median(def_all)/statistics.median(ctrl_all):.3f} ×.')


bloco('3. E SO ENTRE OS MINIONS — o caso do `Capanga`')
print()
mins = [c for c in CRIA if c['org'] == 'Minion']
mctrl = [c for c in mins if c['papel'] == 'Controller']
moutros = [c for c in mins if c['papel'] != 'Controller']
print(f'  {"":<26}{"n":>5}{"stamina mediana":>18}{"EV/corpo mediano":>20}{"free strike":>14}')
print('  ' + '-' * 84)


def resume(rot, xs):
    if not xs:
        return
    ev = [x['ev'] for x in xs if x['ev'] is not None]
    fs_ = [x['fs'] for x in xs if x['fs'] is not None]
    print(f'  {rot:<26}{len(xs):>5}{statistics.median([x["stamina"] for x in xs]):>18.1f}'
          f'{(statistics.median(ev) if ev else float("nan")):>20.2f}'
          f'{(statistics.median(fs_) if fs_ else float("nan")):>14.1f}')


resume('Minion Controller', mctrl)
resume('Minion — os outros', moutros)
print()
print('  E os 6 `Minion Controller`, um a um, contra a coorte deles:')
print()
print(f'  {"nome":<30}{"nv":>4}{"stamina":>9}{"mediana do nv":>15}{"razão":>9}{"EV/corpo":>10}')
print('  ' + '-' * 78)
razoes = []
for c in sorted(mctrl, key=lambda x: x['nv']):
    grupo = [x['stamina'] for x in mins if x['nv'] == c['nv']]
    med = statistics.median(grupo)
    r = c['stamina'] / med
    razoes.append(r)
    print(f'  {c["nome"][:29]:<30}{c["nv"]:>4}{c["stamina"]:>9}{med:>15.1f}{r:>9.3f}'
          f'{(c["ev"] if c["ev"] is not None else float("nan")):>10.2f}')
print()
if razoes:
    print(f'  >> mediana das razoes: {statistics.median(razoes):.3f} ×   '
          f'(media {statistics.mean(razoes):.3f} ×)')


bloco('4. O PAPEL CUSTA EV? — normalizado por nível E organização, como a Stamina')
print()
print('  ⚠ O EV cru esta confundido com o NIVEL: um `Minion Controller` nv10 tem EV/corpo 3,00')
print('     e um nv1 tem 0,75. E os 6 controllers de minion pendem pra nivel alto.')
print('     Entao aqui cada criatura vira razao contra a MEDIANA DE EV da coorte dela.')
print()
for c in CRIA:
    grupo = [x['ev'] for x in coorte[(c['org'], c['nv'])] if x['ev'] is not None]
    med = statistics.median(grupo) if grupo else None
    c['evrel'] = (c['ev'] / med) if (med and c['ev'] is not None) else None

print(f'  {"papel":<12}{"n":>5}{"EV rel. à coorte":>20}{"stamina rel.":>16}{"leitura":>28}')
print('  ' + '-' * 82)
linhas = []
for p2 in sorted(set(c['papel'] for c in CRIA)):
    ev = [c['evrel'] for c in CRIA if c['papel'] == p2 and c['evrel'] is not None and c['coorte'] >= 3]
    st = [c['rel'] for c in CRIA if c['papel'] == p2 and c['rel'] is not None and c['coorte'] >= 3]
    if len(ev) < 5:
        continue
    linhas.append((statistics.median(ev), p2, len(ev), statistics.median(st) if st else float('nan')))
for m, p2, k, sm in sorted(linhas):
    if m > 1.02:
        leitura = 'CUSTA mais no encontro'
    elif m < 0.98:
        leitura = 'custa menos'
    else:
        leitura = 'de graça'
    print(f'  {p2:<12}{k:>5}{m:>20.3f}{sm:>16.3f}{leitura:>28}')
print()
todos_ev = [c['evrel'] for c in CRIA if c['evrel'] is not None and c['coorte'] >= 3]
espalha = max(l[0] for l in linhas) / min(l[0] for l in linhas)
print(f'  >> o EV normalizado espalha {min(l[0] for l in linhas):.2f}× a {max(l[0] for l in linhas):.2f}×'
      f' — um fator de {espalha:.2f}× entre o papel mais barato e o mais caro.')
print()
if espalha > 1.15:
    print('  >> ENTAO O PAPEL DO DRAW STEEL NAO E DE GRACA. O livro diz "roles are descriptive",')
    print('     mas o PRECO dele existe — so que ele mora FORA do bloco, no EV do encontro.')
    print('     A gente cobra DENTRO do bloco, redistribuindo. Sao dois desenhos diferentes.')
else:
    print('  >> o papel do Draw Steel e de graca no EV: ele e so descritivo mesmo.')
print()
print('  E so entre os MINIONS, que e o caso do `Capanga`:')
print()
print(f'  {"papel":<12}{"n":>5}{"EV rel.":>11}{"stamina rel.":>15}')
print('  ' + '-' * 45)
for p2 in sorted(set(c['papel'] for c in CRIA if c['org'] == 'Minion')):
    ev = [c['evrel'] for c in CRIA if c['org'] == 'Minion' and c['papel'] == p2 and c['evrel'] is not None]
    st = [c['rel'] for c in CRIA if c['org'] == 'Minion' and c['papel'] == p2 and c['rel'] is not None]
    if not ev:
        continue
    print(f'  {p2:<12}{len(ev):>5}{statistics.median(ev):>11.3f}'
          f'{(statistics.median(st) if st else float("nan")):>15.3f}')
print()


bloco('5. A METRICA QUE DA PRA ROUBAR — o teto de empilhamento')
t = ler(BASICS, raiz='/')
m1 = re.search(r'(Each target of a minion\'s signature ability is affected by only one instance[^\n]+)', t)
m2 = re.search(r'(When minions act, each minion in the squad uses their main action[^\n]+)', t)
m3 = re.search(r'(Minion turns are meant to be short[^\n]+)', t)
print()
print('  Sobre quantas ACOES um esquadrao tem:')
print(f'    "{m2.group(1)}"')
print(f'    "{m3.group(1)}"')
print()
print('  >> cada corpo tem a acao DELE. O esquadrao age junto, mas as acoes sao', CORPOS, 'e nao 1.')
print()
print('  E o teto de empilhar num alvo so:')
print(f'    "{m1.group(1)[:300]}"')
print()
mais = re.search(r'(Because a minion\'s free strike value is typically lower[^\n]+)', t)
print(f'    "{mais.group(1)}"')

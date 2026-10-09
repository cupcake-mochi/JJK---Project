# -*- coding: utf-8 -*-
"""As tabelas da peca 26 na grade nova (fase 2, 28/09/2026). Nenhuma sai escrita a mao.

    python3 bestiario/09-fase-2/gerar-grade.py            imprime as tabelas em markdown

Os donos: a tabela `Inimigos` do manual (partF.js: a saida do grupo e o dano do chefe por faixa),
as rodadas e as decisoes do Mizuki (decisoes-fase-2.md §5, §10 e §11), o orcamento do PF2e (as notas
da leva 1), a peca 11 §6.5 (o custo das quatro anti-dominio), a peca 18 (a maior Classe por nivel) e a
peca 5 §4 (1 PE = 5,14 de dano). A conta de cada preco e a de conta-esqueleto.py, cortes 2 a 4.
"""
import re, os, sys, math
R = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) + os.sep
def ler(c): return open(R + c, encoding='utf-8').read()
def perdida(o): print('ANCORA PERDIDA:', o); sys.exit(1)
def pega(txt, rx, nome, fl=re.M):
    m = re.search(rx, txt, fl)
    if not m: perdida(nome)
    return m
def baixo(x): return int(x) if x - int(x) <= 0.5 else int(x) + 1          # meio para BAIXO
def virg(x, c=2): return f'{x:.{c}f}'.replace('.', ',')

pf = ler('sistema/99-arquivo/manual-fundamento-v7/gerador/partF.js')
i = pf.find("H2('Inimigos')")
FAIXA = {int(n): (int(g), int(d)) for n, g, d in
         re.findall(r"\['(\d+)', '~(\d+)', '[\d a]+', '(\d+)', '\d+', '\d+'\]", pf[i:i + 900])}
if len(FAIXA) != 7: perdida('a tabela Inimigos do manual')
PCT = int(pega(pf, r'O dano dele por rodada é (\d+)% da vida de um personagem', 'os 90%').group(1)) / 100
dec = ler('bestiario/09-fase-2/decisoes-fase-2.md')
ROD_TXT = pega(dec, r'As rodadas dele \(`([\d,]+) · ([\d,]+) · ([\d,]+) · ([\d,]+) · ([\d,]+)`\)', 'as rodadas dele').groups()
DEGRAUS = ('Capanga', 'Ameaça', 'Desastre', 'Catástrofe', 'Calamidade')
ROD = {c: float(x.replace(',', '.')) for c, x in zip(DEGRAUS, ROD_TXT)}
pes = ler('bestiario/09-fase-2/pesquisa/NOTAS-pesquisa-externa.md')
m = pega(pes, r'Trivial (\d+) ou menos \(ajuste \d+\), Low (\d+) \(\d+\), Moderate (\d+) \(\d+\), Severe (\d+) \(\d+\), Extreme (\d+) \(\d+\)', 'o orcamento do PF2e')
ORC = {c: int(x) / int(m.group(3)) for c, x in zip(DEGRAUS, m.groups())}
PRESS = {c: ORC[c] * ROD['Desastre'] / ROD[c] for c in DEGRAUS}
p11 = ler('sistema/03-mecanica/11-aptidoes-e-refino.md')
p18 = ler('sistema/03-mecanica/18-progressao.md')
p05 = ler('sistema/03-mecanica/05-caminho-e-combate-sem-feitico.md')

def s_de(nv): return FAIXA[nv][0] / 4                   # a saida de UM personagem por rodada
def base_de(nv): return FAIXA[nv][1] / 4                # o golpe-base: o dano do chefe ÷ 4
def vida(nv, c, n): return baixo(ROD[c] * n * s_de(nv))
def golpe(nv, c): return baixo(PRESS[c] * base_de(nv)) if c != 'Capanga' else baixo(base_de(nv) / 2)
def interv_ok(c, n): return c != 'Capanga' and n * ORC[c] >= 4

# o dado do golpe, a regra da peca 26 §4.4 (a mesma funcao do make.js)
def dado(alvo):
    if alvo < 5: return str(baixo(alvo))
    meta = alvo / 2; bom = None
    for d in (4, 6, 8, 10, 12):
        med = (d + 1) / 2; n = max(1, round(meta / med))
        if n > 8: continue
        fixo = alvo - n * med
        if fixo < 0: continue
        inteiro = 0 if abs(fixo - round(fixo)) < 1e-9 else 1
        erro = abs(n * med - meta)
        if bom is None or inteiro < bom[0] or (inteiro == bom[0] and erro < bom[1] - 1e-9) or \
           (inteiro == bom[0] and abs(erro - bom[1]) < 1e-9 and n < bom[2]):
            bom = (inteiro, erro, n, d, round(fixo))
    return f'{bom[2]}d{bom[3]} + {bom[4]}' if bom[4] > 0 else f'{bom[2]}d{bom[3]}'

def f_interv(c, n): return 1 + 0.75 / (ROD[c] * n)
def f_recarga(c):
    disparos = 1 + (ROD[c] - 1) / 3
    return (disparos * 1.25 + (ROD[c] - disparos)) / ROD[c]

out = []
def T(*linhas): out.extend(linhas); out.append('')

T('## os degraus',
  '| categoria | rodadas | orçamento | pressão | o golpe, em % da vida de um personagem | `Intervenção` a partir de |',
  '|---|---|---|---|---|---|',
  *[f'| **`{c}`** | `{virg(ROD[c], 1).replace(",0", "")}` | `{virg(ORC[c])}` | `{virg(PRESS[c], 3) if c != "Capanga" else "—"}` | '
    f'`{virg(100 * (PRESS[c] if c != "Capanga" else 0.5) * 0.25 * PCT, 1)}%` | '
    f'{("`×" + str(min(n for n in range(1, 7) if interv_ok(c, n))) + "`") if any(interv_ok(c, n) for n in range(1, 7)) else "—"} |'
    for c in DEGRAUS])

for nv in (10, 20, 30):
    T(f'## fichas prontas, nivel {nv} (vida · golpe)',
      '| categoria | `×1` | `×2` | `×3` | `×4` | `×5` | `×6` |', '|---|---|---|---|---|---|---|',
      *[f'| `{c}` | ' + ' | '.join((f'`{2 * n}` × `{math.floor(s_de(nv))}` · `{golpe(nv, c)}`' if c == 'Capanga'
                                    else f'`{vida(nv, c, n)}` · `{golpe(nv, c)}`') for n in range(1, 7)) + ' |'
        for c in DEGRAUS])

T('## o golpe em dado, nivel 26 a 30',
  '| categoria | o golpe | em dado |', '|---|---|---|',
  *[f'| `{c}` | `{golpe(30, c)}` | `{dado(golpe(30, c))}` |' for c in DEGRAUS])

T('## pontos de feitico por acao (o golpe ÷ 4,5; seco abaixo de 3 pontos)',
  '| pontos por ação | ' + ' | '.join(f'`{c}`' for c in DEGRAUS) + ' |', '|---' * 6 + '|',
  *[f'| nível {nv} | ' + ' | '.join(('seco' if golpe(nv, c) / 4.5 < 3 else f'`{virg(golpe(nv, c) / 4.5, 1)}`') for c in DEGRAUS) + ' |'
    for nv in sorted(FAIXA)])

T('## o papel por N (o preco e uma acao; o Capanga le 2N acoes)',
  '| papel | ' + ' | '.join(f'`×{n}`' for n in range(1, 7)) + ' |', '|---' * 7 + '|',
  '| `Emboscador` ganha | ' + ' | '.join(f'`× {virg((n - 1 + 1.476) / n, 3)}`' for n in range(1, 7)) + ' |',
  '| `Controlador` e `Reforço` ganham | ' + ' | '.join(f'`× {virg(1 + 1 / n, 3)}`' for n in range(1, 7)) + ' |',
  '| o esquadrão do `Capanga`, `Emboscador` | ' + ' | '.join(f'`× {virg((2 * n - 1 + 1.476) / (2 * n), 3)}`' for n in range(1, 7)) + ' |',
  '| o esquadrão do `Capanga`, `Controlador` | ' + ' | '.join(f'`× {virg(1 + 1 / (2 * n), 3)}`' for n in range(1, 7)) + ' |')

T('## o Artilheiro e a Recarga, por degrau',
  '| categoria | `Artilheiro` ganha | a `Recarga` multiplica a pressão por |', '|---|---|---|',
  *[f'| `{c}` | `× {virg(1 + 0.5 / ROD[c], 3)}` | ' + (f'`× {virg(f_recarga(c))}`' if c != 'Capanga' else '—') + ' |' for c in DEGRAUS])

T('## a Intervencao (vida ÷ isto), onde N x peso >= 4',
  '| categoria | ' + ' | '.join(f'`×{n}`' for n in range(1, 7)) + ' |', '|---' * 7 + '|',
  *[f'| `{c}` | ' + ' | '.join((f'`× {virg(f_interv(c, n), 3)}`' if interv_ok(c, n) else '—') for n in range(1, 7)) + ' |'
    for c in DEGRAUS[1:]])

T('## a parte destrutivel: a vida dela e 2 x a saida de um personagem',
  '| faixa | ' + ' | '.join(f'nível {nv}' for nv in sorted(FAIXA)) + ' |', '|---' * 8 + '|',
  '| a vida de uma parte | ' + ' | '.join(f'`{math.floor(2 * s_de(nv))}`' for nv in sorted(FAIXA)) + ' |')

# a Circulacao: a Reacao cura por rodada; a luta de L rodadas vira L ÷ (1 − L × cura ÷ vida). Com a vida
# = L × N × s, o L sai da conta: o multiplicador e 1 ÷ (1 − cura ÷ (N × s)), igual em todo degrau.
T('## a Circulacao: vida ÷ isto (igual em todo degrau)',
  '| a Reação, uma vez por rodada | cura | ' + ' | '.join(f'`×{n}`' for n in range(1, 7)) + ' |', '|---' * 8 + '|',
  *[f'| do nível {de} ao {ate} · `{dd}d4` | `{virg(dd * 2.5, 1)}` | ' +
    ' | '.join(f'`× {virg(1 / (1 - dd * 2.5 / (n * s_de(nvl))), 2)}`' for n in range(1, 7)) + ' |'
    for de, ate, dd, nvl in ((22, 25, 9, 25), (26, 30, 10, 30))])

# as quatro anti-dominio na cota, nivel 30 — o custo por rodada em dano ÷ a cota (N golpes)
CL18 = {int(m_.group(1)): int(m_.group(5)) for m_ in (re.match(r'\|\s*\*{0,2}(\d+)\*{0,2}\s*\|\s*[\d.—]+\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|'
        r'\s*(\d+)\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|', l) for l in p18.split('\n')) if m_}
if 30 not in CL18: perdida('a maior Classe por nivel (peca 18, a leitura do conferir-bestiario 9)')
mx = CL18[30]
CAMBIO = float(pega(p05, r'recuperar `\+1` PE \| permanente \| `([\d,]+)`', 'o cambio da peca 5 §4').group(1).replace(',', '.'))
# o custo por rodada de cada uma e o formato dele saem da tabela das quatro da peca 11 §6.5, e quem paga
# erguer, da frase de erguer — a mesma leitura da checagem 9.2 do conferir-bestiario.py
def _celulas(l): return [c.replace('*', '').replace('`', '').strip() for c in l.split('|')[1:-1]]
_i11 = p11.find('| | Classe · gate | abre em | o refino escala | PE por rodada |')
if _i11 < 0: perdida('a tabela das quatro anti-dominio da peca 11 §6.5')
apt = []
for l in p11[_i11:].split('\n\n')[0].split('\n')[2:]:
    c = _celulas(l)
    mm = re.match(r'([\d,]+) × maior Classe', c[4]); mf = re.match(r'(\d+) fixos?', c[4])
    apt.append((c[0], ('x', float(mm.group(1).replace(',', '.'))) if mm else ('fixo', float(mf.group(1)) if mf else 0.0)))
_erg = pega(p11, r'^\*\*E erguer custa a sua maior Classe em PE, toda vez que ela sobe\*\* — (.+)$', 'a frase de erguer da peca 11')
ERG = set(re.findall(r'`([^`]+)`', _erg.group(1).split('*')[0]))
def custo_rodada(nome, fmt, c):
    return ((math.ceil(fmt[1] * mx - 1e-9) if fmt[0] == 'x' else fmt[1]) + (mx / ROD[c] if nome in ERG else 0)) * CAMBIO
T(f'## as quatro anti-dominio ligadas a luta inteira, nivel 30 (maior Classe {mx}, 1 PE = {virg(CAMBIO)})',
  '| ligada a luta inteira, no nível 30 | `Desastre ×1` | `Desastre ×4` | `Calamidade ×1` | `Calamidade ×4` |', '|---|---|---|---|---|',
  *[f'| `{nome}` | ' + ' | '.join(f'`{round(custo_rodada(nome, fmt, c) / (n * golpe(30, c)) * 100)}%`'
                                   for c, n in (('Desastre', 1), ('Desastre', 4), ('Calamidade', 1), ('Calamidade', 4))) + ' |'
    for nome, fmt in apt])

# --- as simulacoes: a do conferir-bestiario.py (checagens 5 e 5.1), o chefe age primeiro ---------------
def simula(saida, corpos):
    vs = [list(c) for c in corpos]; rod = 0; cobrado = 0.0
    while vs and rod < 100:
        cobrado += sum(c[1] for c in vs); sobra = saida
        while sobra > 0 and vs:
            if vs[0][0] <= sobra: sobra -= vs.pop(0)[0]
            else: vs[0][0] -= sobra; sobra = 0
        rod += 1
    return rod, cobrado
def corpo(nv, c, n): return (vida(nv, c, n), n * golpe(nv, c))
def capangas(nv, k): return [(math.floor(s_de(nv)), golpe(nv, 'Capanga'))] * k
def cambio(nv, c, n):
    _, alvo = simula(n * s_de(nv), [corpo(nv, c, n)])
    return min(range(1, 80), key=lambda k: abs(simula(n * s_de(nv), capangas(nv, k))[1] - alvo))
T('## o cambio: quantos capangas cobram o que a celula cobra (todas as faixas)',
  '| categoria | ' + ' | '.join(f'`×{n}`' for n in range(1, 7)) + ' |', '|---' * 7 + '|',
  *[f'| `{c}` | ' + ' | '.join(
      (lambda ks: f'`{ks[0]}`' if len(set(ks)) == 1 else f'`{min(ks)}`–`{max(ks)}`')([cambio(nv, c, n) for nv in sorted(FAIXA)])
      for n in range(1, 7)) + ' |' for c in DEGRAUS[1:]])
def fracao(nv, c, n, k):
    _, alvo = simula(n * s_de(nv), [corpo(nv, c, n)])
    v, d = corpo(nv, c, n)
    return min((x / 1000 for x in range(1, 1001)),
               key=lambda f: abs(simula(n * s_de(nv), capangas(nv, k) + [(v * f, d * f)])[1] - alvo))
T('## o chefe com capangas, nivel 30: a fracao do chefe que devolve o que ele cobra sozinho',
  '| célula | `1/(rodadas × N)` | 1 capanga | 2 | 3 |', '|---|---|---|---|---|',
  *[f'| `{c} ×{n}` | `{virg(100 / (ROD[c] * n), 1)}%` | ' + ' | '.join(f'`{virg(100 * fracao(30, c, n, k), 1)}%`' for k in (1, 2, 3)) + ' |'
    for c in ('Desastre', 'Calamidade') for n in (2, 4, 6)])
T('## N corpos de x1 contra um corpo de xN, do mesmo degrau: o que cobram (nivel 30)',
  '| categoria | `×2` | `×4` | `×6` |', '|---|---|---|---|',
  *[f'| `{c}` | ' + ' | '.join(
      f'`{virg(simula(n * s_de(30), [corpo(30, c, 1)] * n)[1] / simula(n * s_de(30), [corpo(30, c, n)])[1], 2)}`'
      for n in (2, 4, 6)) + ' |' for c in DEGRAUS[1:]])
L30 = FAIXA[30][1] / PCT
T('## concentrando, nivel 30: em que rodada ele derruba um, e quantos derruba na luta (xN)',
  '| categoria | rodadas | derruba um na rodada | derruba na luta |', '|---|---|---|---|',
  *[f'| `{c}` | `{virg(ROD[c], 1)}` | `{virg(L30 / (4 * golpe(30, c)), 2)}` (×4) | `{virg(ROD[c] * golpe(30, c) / L30, 3)} × N` |' for c in DEGRAUS[1:]])
T('## a Regravacao no nivel 30 (10 PE = 51,4): da cota da rodada, e espalhada na luta',
  '| | `Desastre ×1` | `Desastre ×4` | `Calamidade ×1` | `Calamidade ×4` |', '|---|---|---|---|---|',
  '| da cota da rodada | ' + ' | '.join(f'`{round(10 * CAMBIO / (n * golpe(30, c)) * 100)}%`' for c, n in (('Desastre', 1), ('Desastre', 4), ('Calamidade', 1), ('Calamidade', 4))) + ' |',
  '| espalhada na luta | ' + ' | '.join(f'`{virg(10 * CAMBIO / (n * golpe(30, c)) / ROD[c] * 100, 1)}%`' for c, n in (('Desastre', 1), ('Desastre', 4), ('Calamidade', 1), ('Calamidade', 4))) + ' |')

print('\n'.join(out))

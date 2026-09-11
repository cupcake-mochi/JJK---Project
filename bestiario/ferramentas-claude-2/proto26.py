# Prototipo: todo numero que a peca 26 vai publicar na escada viva, lido dos donos.
import re, os, math, docx
R = '/media/mizuki/HD Externo II/Claude/Claude 2'
B = '/media/mizuki/HD Externo II/Claude/Claude 2/bestiario'
def ler(p): return open(os.path.join(R, p), encoding='utf-8').read()
def mb(x): return math.ceil(x - 0.5) if abs(x % 1 - 0.5) < 1e-9 else round(x)
def arred(x): return math.ceil(x - 0.5)
def jr(x): return math.floor(x + 0.5)
MAN = {}
for t in docx.Document(os.path.join(R, 'manual/Fundamento-MANUAL-v7.docx')).tables:
    cab = [c.text.strip() for c in t.rows[0].cells]
    if cab and cab[0].startswith('Nível do grupo') and 'Chefe: dano' in cab:
        for r in t.rows[1:]:
            v = [c.text.strip() for c in r.cells]; vd = v[2].split(' a ')
            MAN[int(v[0])] = (float(v[1].replace('~', '')), (int(vd[0]) + int(vd[-1])) / 2, float(v[3]), float(v[4]), float(v[5]))
        break
CAM = re.findall(r'\|\s*\*\*(\w+)\*\*\s*\|\s*d(\d+)\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|', ler('sistema/03-mecanica/01-atributos-acerto-defesa.md'))
V1 = sum(int(c[2]) for c in CAM) / 5; VN = sum(int(c[3]) for c in CAM) / 5
def VPC(nv): return V1 + VN * (nv - 1) + 3 * nv
def simula(saida, corpos):
    vs = [list(c) for c in corpos]; rod = 0; cob = 0.0
    while vs and rod < 100:
        cob += sum(c[1] for c in vs); sobra = saida
        while sobra > 0 and vs:
            if vs[0][0] <= sobra: sobra -= vs.pop(0)[0]
            else: vs[0][0] -= sobra; sobra = 0
        rod += 1
    return rod, cob
DADOS = [4, 6, 8, 10, 12]
def dado(alvo):
    if alvo < 5: return str(arred(alvo)), float(arred(alvo))
    meta = alvo / 2; bom = None
    for d in DADOS:
        med = (d + 1) / 2; n = max(1, jr(meta / med))
        if n > 8: continue
        fixo = alvo - n * med
        if fixo < 0: continue
        inte = 0 if abs(fixo - jr(fixo)) < 1e-9 else 1
        er = abs(n * med - meta)
        if bom is None or inte < bom[0] or (inte == bom[0] and er < bom[1] - 1e-9) or (inte == bom[0] and abs(er - bom[1]) < 1e-9 and n < bom[2]):
            bom = (inte, er, n, d, jr(fixo))
    if bom is None:
        n = max(1, jr(alvo / 9)); m = arred(alvo - 4.5 * n)
        return (f'{n}d8 + {m}' if m > 0 else f'{n}d8'), n * 4.5 + max(m, 0)
    _, _, n, d, fx = bom
    return (f'{n}d{d} + {fx}' if fx > 0 else f'{n}d{d}'), n * (d + 1) / 2 + max(fx, 0)
CATS = [('Capanga', None, 0.25, 1, False), ('Ameaça', 1, 0.25, 1, False), ('Desastre', 4, 1.0, 3, True),
        ('Catástrofe', 6, 1.5, 5, True), ('Calamidade', 8, 2.0, 6, True)]
FI = 0.923
print('MANUAL', {k: v[:3] for k, v in MAN.items()}); print('VPC30', VPC(30), 'grupo', 4 * VPC(30))
print('\n§4.1  vida · dano (nv10 | nv20 | nv30)')
for nome, p, f, a, i in CATS:
    out = []
    for nv in (10, 20, 30):
        s, cv, cd, _, _ = MAN[nv]
        v = math.floor(s / 4) if nome == 'Capanga' else mb(cv * f)
        out.append(f'{v} · {mb(cd * f)}')
    print(f'  {nome:<11}', ' | '.join(out))
meios = tot = 0
for nv, (s, cv, cd, _, _) in MAN.items():
    for nome, p, f, a, i in CATS:
        for x in ([cd * f] if nome == 'Capanga' else [cv * f, cd * f]):
            tot += 1; meios += abs(x % 1 - 0.5) < 1e-9
print(f'  celulas em ,5 exato: {meios} de {tot}')
print('\n§4.4  nv26-30: por rodada · acoes · golpe')
for nome, p, f, a, i in CATS:
    s, cv, cd, _, _ = MAN[30]; dr = mb(cd * f)
    print(f'  {nome:<11} {dr:>4} {a} {dado(arred(cd * f) / a)[0]}')
print('\n§5  cambio com o Capanga da escada (vida = saida/4 pra baixo, dano = cd x 0,25)')
for nv, (s, cv, cd, _, _) in sorted(MAN.items()):
    kv, kd = math.floor(s / 4), mb(cd * 0.25)
    r0, t0 = simula(s, [(cv, cd)])
    melhor = min(range(1, 13), key=lambda n: abs(simula(s, [(kv, kd)] * n)[1] - t0))
    r8, t8 = simula(s, [(kv, kd)] * 8)
    print(f'  nv{nv:<3} saida {s:>4.0f} capanga {kv}/{kd}  chefe {t0:.0f} em {r0}  8 capangas {t8:.0f} em {r8}  melhor n={melhor}')
print('\n§4.5  sub-categoria no nv30 (capangas primeiro)')
s, cv, cd, _, _ = MAN[30]; kv, kd = math.floor(s / 4), mb(cd * 0.25); vg = 4 * VPC(30)
for rot, f, n in (('sozinho', 1.0, 0), ('com um apoio', 0.915, 1), ('com dois', 0.83, 2), ('bando', 0.745, 3)):
    r, c = simula(s, [(kv, kd)] * n + [(cv * f, cd * f)])
    print(f'  {rot:<13} {f:.3f} n={n}  rodadas {r}  cobra {c / vg * 100:.1f}%')
print('\n§6.5 pontos por acao (metodo A-TABELA: media do dado x 0,923 / 4,5; seco < 3)')
t19 = ler('sistema/03-mecanica/19-dano-e-condicoes.md')
PONTO = float(re.search(r'vira `1d8` de dano — que são `([\d,]+)`', t19).group(1).replace(',', '.'))
atab = open(os.path.join(B, '04-fase-1/fila/A-TABELA-pontos-por-acao.md'), encoding='utf-8').read()
pub = {}
for ln in atab.split('\n'):
    m = re.match(r'\|\s*`(\d+)`\s*\|(.*)\|\s*$', ln)
    if m: pub[int(m.group(1))] = [c.strip().strip('*').strip('`').strip('*') for c in m.group(2).split('|')]
dif = 0
for nv in sorted(MAN):
    s, cv, cd, _, _ = MAN[nv]; row = []
    for nome, p, f, a, i in CATS:
        g = dado(arred(cd * f) / a)[1] * (FI if i else 1.0); pts = g / PONTO
        row.append('seco' if pts < 3 - 1e-9 else f'{pts:.1f}'.replace('.', ','))
    ok = row == pub.get(nv)
    dif += not ok
    print(f'  nv{nv:<3}', ' '.join(f'{x:>5}' for x in row), '' if ok else f'  <- A-TABELA: {pub.get(nv)}')
print(f'  linhas que nao batem com a A-TABELA: {dif}')
print('\n§6.5 aptidao (nv30): % da cota')
t11 = ler('sistema/03-mecanica/11-aptidoes-e-refino.md'); t18 = ler('sistema/03-mecanica/18-progressao.md')
CL18 = {}
for l in t18.split('\n'):
    m = re.match(r'\|\s*\*{0,2}(\d+)\*{0,2}\s*\|\s*[\d.—]+\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|', l)
    if m: CL18[int(m.group(1))] = int(m.group(5))
CAMB = float(re.search(r'recuperar `\+1` PE \| permanente \| `([\d,]+)`', ler('sistema/03-mecanica/05-caminho-e-combate-sem-feitico.md')).group(1).replace(',', '.'))
for mult, rot in ((1.0, 'Dominio Simples/Petala 1x'), (1.5, 'Extensao 1,5x')):
    for nv in (30, 2):
        c = mult * CL18[nv] * CAMB; s, cv, cd, _, _ = MAN[nv]
        am = mb(cd * 0.25); de = mb(cd * 1.0); de9 = de * FI
        print(f'  nv{nv} {rot}: custo {c:.2f}  Ameaça {c / am * 100:.0f}%  Desastre cru {c / de * 100:.0f}%  Desastre x0,923 {c / de9 * 100:.1f}%')
c1 = 1.0 * CL18[30] * CAMB / 3
print(f'  Dominio Simples uma rodada de tres: {c1:.2f} = {c1 / (219 * FI) * 100:.1f}% de um Desastre, {c1 / 55 * 100:.0f}% de uma Ameaça')
print(f'  cura: 219 x 0,923 = {219 * FI:.1f};  / 315 = {219 * FI / 315:.3f}')
print('\n§6.4 personagens x 1,92:', [(n, p, round(p * 1.92, 1)) for n, p, f, a, i in CATS if p])

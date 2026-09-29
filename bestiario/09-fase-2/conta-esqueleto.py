# -*- coding: utf-8 -*-
"""Fase 2, corte 1: o esqueleto categoria x pessoas, com as tres respostas do Mizuki de 28/09/2026.

O que o corte supoe, e nada mais:
  - O N (x1 a x6) poe a vida e as acoes: o inimigo age N vezes, e cada golpe e a pressao de UMA pessoa
    (o golpe do Campeao do Fabula Ultima nao cresce com o N; os turnos, sim).
  - A categoria e a dificuldade, pelo degrau do Pathfinder 2e (baixa, moderada, severa, extrema); ela
    mexe na DURACAO da luta, e o resto da forca dela vem de recurso, e nao do golpe (resposta "A+B").
  - A Intervencao e liberada pela regra N x peso >= 4, que reproduz os dois exemplos dele: a Ameaca so no
    x6, e o Desastre ja no x4.

O CONTRATO: a regressao reproduz antes a linha do manual e a escada da peca 26 nas celulas que o
esqueleto novo mantem; todo numero sai do dono.
"""
import re, sys, os
R = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) + os.sep
def ler(c): return open(R + c, encoding='utf-8').read()
pf = ler('manual/gerador/partF.js')
p26 = ler('sistema/03-mecanica/26-bestiario.md')
cap = ler('bestiario/04-fase-1/fila/DECIDIDO-o-capanga.md')
pes = ler('bestiario/09-fase-2/pesquisa/NOTAS-pesquisa-externa.md')
falhas = []
def confere(nome, obtido, esperado):
    ok = obtido == esperado
    print(f'  [{"x" if ok else "!"}] {nome}: {obtido}' + ('' if ok else f'  (esperado {esperado})'))
    if not ok: falhas.append(nome)
def perdida(o): print('ANCORA PERDIDA:', o); sys.exit(1)
def pega(txt, rx, nome, fl=re.M):
    m = re.search(rx, txt, fl)
    if not m: perdida(nome)
    return m
def baixo(x): return int(x) if x - int(x) <= 0.5 else int(x) + 1     # meio para BAIXO, peca 26 §4.1

# --- os donos -----------------------------------------------------------------------------------
i = pf.find("H2('Inimigos')")
LINHA = {int(n): (float(g), int(d)) for n, g, d in re.findall(r"\['(\d+)', '~(\d+)', '[\d a]+', '(\d+)', '\d+', '\d+'\]", pf[i:i + 900])}
if len(LINHA) != 7: perdida('a tabela Inimigos do manual (partF.js)')
QUATRO = 'quatro' if re.search(r'A conta supõe quatro personagens', pf) else perdida('a mesa de 4 do manual')
PCT = int(pega(pf, r'O dano dele por rodada é (\d+)% da vida de um personagem', 'os 90% do manual').group(1)) / 100
RODADAS = 3 if re.search(r'cerca de três vezes o dano de rodada do grupo em vida', pf) else perdida('as 3 rodadas do manual')
m = pega(cap, r'A banda do `o golpe` vira \*\*`(\d+)%`–`(\d+)%`\*\*', 'a banda do golpe')
BANDA = (int(m.group(1)) / 100, int(m.group(2)) / 100)
m = pega(pes, r'Low (\d+) \(\d+\), Moderate (\d+) \(\d+\), Severe (\d+) \(\d+\), Extreme (\d+) \(\d+\)', 'a Table 10-1 do PF2e nas notas')
PF2E = [int(x) for x in m.groups()]
PESO = {c: x / PF2E[1] for c, x in zip(('Ameaça', 'Desastre', 'Catástrofe', 'Calamidade'), PF2E)}
T41 = {c: (int(v), int(d)) for c, v, d in re.findall(r'^\| `(Ameaça|Desastre|Catástrofe|Calamidade)` \|[^|]+\|[^|]+\| `(\d+)` · `(\d+)` \|$', p26, re.M)}
if len(T41) != 4: perdida('a tabela §4.1 da peca 26 no nivel 30')

def celula(nv, cat, n):
    grupo, chefe = LINHA[nv]
    s = grupo / 4                              # a saida de UM personagem: o manual calibra para quatro
    L = chefe / PCT                            # a vida de um personagem: o dano do chefe e 90% dela
    rod = RODADAS * PESO[cat]
    golpe = chefe / 4                          # a pressao de uma pessoa por rodada
    return dict(vida=baixo(rod * n * s), acoes=n, golpe=baixo(golpe), dano=baixo(n * golpe), rodadas=rod,
                pct=golpe / L, grupo=rod * golpe / L, derruba=rod * n * golpe / L,
                interv=n * PESO[cat] >= 4)

print('REGRESSAO — as celulas que o esqueleto novo mantem da escada de hoje (nivel 30)')
confere('a mesa de 4, os 90% e as 3 rodadas do manual', (QUATRO, PCT, RODADAS), ('quatro', 0.9, 3))
confere('a banda do golpe (DECIDIDO-o-capanga)', BANDA, (0.21, 0.28))
confere('o degrau do PF2e: baixa, moderada, severa, extrema', PF2E, [60, 80, 120, 160])
confere('Desastre x4 = o Desastre de hoje (vida, dano)', (celula(30, 'Desastre', 4)['vida'], celula(30, 'Desastre', 4)['dano']), T41['Desastre'])
confere('Desastre x1 = a Ameaca de hoje, de 1 pessoa (vida, dano)', (celula(30, 'Desastre', 1)['vida'], celula(30, 'Desastre', 1)['dano']), T41['Ameaça'])
confere('Catastrofe x4 tem a vida da Catastrofe de hoje, de 6 pessoas', celula(30, 'Catástrofe', 4)['vida'], T41['Catástrofe'][0])
confere('Calamidade x4 tem a vida da Calamidade de hoje, de 8 pessoas', celula(30, 'Calamidade', 4)['vida'], T41['Calamidade'][0])
if falhas: print('\n>>> A REGRESSAO FALHOU — nada abaixo vale.'); sys.exit(1)
print('>>> TUDO OK.\n')

CATS = ('Ameaça', 'Desastre', 'Catástrofe', 'Calamidade')
for nv in (10, 30):
    print(f'NIVEL {nv} — vida do inimigo (acoes = N; golpe {celula(nv, "Desastre", 1)["golpe"]}, '
          f'{100 * celula(nv, "Desastre", 1)["pct"]:.1f}% da vida de um personagem, dentro da banda '
          f'{100 * BANDA[0]:.0f}-{100 * BANDA[1]:.0f}%)')
    print('  categoria    rodadas  ' + '  '.join(f'   x{n}' for n in range(1, 7)))
    for c in CATS:
        print(f'  {c:<12} {celula(nv, c, 1)["rodadas"]:>5.2f}  ' + '  '.join(f'{celula(nv, c, n)["vida"]:>5}' for n in range(1, 7)))
    print()
print('O QUE A LUTA COBRA (igual em todo nivel e todo N, sem cura e sem atrito):')
print('  categoria    peso   vida do grupo que ela tira   derruba se concentrar (x1 .. x6)')
for c in CATS:
    k = celula(30, c, 1)
    print(f'  {c:<12} {PESO[c]:.2f}   {100 * k["grupo"]:>5.1f}%                       '
          + ' '.join(f'{celula(30, c, n)["derruba"]:>4.1f}' for n in range(1, 7)))
print('\nINTERVENCAO (N x peso >= 4):')
for c in CATS:
    print(f'  {c:<12} ' + ' '.join(('  x%d:sim' if celula(30, c, n)['interv'] else '  x%d: - ') % n for n in range(1, 7)))
fora = [(c, n) for c in CATS for n in range(1, 7) if not (BANDA[0] <= celula(30, c, n)['pct'] <= BANDA[1])]
print(f'\nGolpes fora da banda: {len(fora)} de 24 celulas.')
m = pega(p26, r'o `Desastre` não pode descer de `(\d)`', 'o piso de acoes da peca 19, citado na peca 26')
piso = int(m.group(1))
abaixo = [n for n in range(1, 7) if n < piso]
print(f'Celulas com menos acoes que o piso {piso} da regua de condicao da peca 19: as de x{abaixo[0]} a x{abaixo[-1]}, nas quatro categorias.')

# --- corte 2: a hipotese dele de 28/09 ("B"; "eu penso em ser 2-2.5-3-4-5 rodadas, lembrando q tem a
# categoria faltando") — cinco degraus, como os cinco do PF2e (trivial a extrema). O orcamento de cada
# degrau e o do PF2e; as rodadas sao as dele; o que sobra do orcamento depois da duracao vira pressao por
# rodada, e o que passa de N acoes vem de recurso (Intervencao, Recarga), e nao de golpe maior.
# A que faltava e o Capanga (resposta dele de 28/09: "Capanga, ele pode sim ser usado contra players em
# multiplas quantidades ou junto de um chefe").
m = pega(pes, r'Trivial (\d+) ou menos \(ajuste \d+\), Low (\d+) \(\d+\), Moderate (\d+)', 'o degrau trivial do PF2e nas notas')
TRIVIAL = int(m.group(1)) / int(m.group(3))
RODADAS_DELE = (2, 2.5, 3, 4, 5)
DEGRAUS = (('Capanga', TRIVIAL),) + tuple((c, PESO[c]) for c in CATS)
_, chefe30 = LINHA[30]
print('\nCORTE 2 — as rodadas dele, com o orcamento do PF2e (x4, nivel 30; o Desastre x4 de hoje bate', chefe30, 'por rodada)')
print('  degrau          orcamento  rodadas  pressao  dano/rodada  acao a mais por rodada, de recurso  vida do grupo que tira')
for (nome, peso), rod in zip(DEGRAUS, RODADAS_DELE):
    press = peso * RODADAS / rod
    extra = max(0.0, (press - 1) * 4)
    print(f'  {nome:<15} {peso:>8.2f}  {rod:>7.1f}  {press:>6.2f}x  {baixo(chefe30 * press):>11}  {extra:>34.1f}  '
          f'{100 * RODADAS * peso * PCT / 4:>21.1f}%')

# --- corte 2, a ficha: tres contas que nao dependem das rodadas -----------------------------------
# (1) o preco de um ponto de atributo, (2) o Capanga no degrau de 2 rodadas, (3) o preco de sair da
# condicao no x1 e no x2. Todo numero sai de dono; a regressao confere antes o que ja esta publicado.
print('\nCORTE 2, A FICHA')
m = pega(p26, r'um ponto de Defesa move `(\d+)` pontos percentuais, e o personagem acerta alvo difícil em `(\d+)%`', 'o ponto de Defesa (peca 26 §3.4, dono peca 1 §5.2)')
PP, BASE_PJ = int(m.group(1)), int(m.group(2))          # 5 pp por ponto; o personagem acerta 50%
m = pega(p26, r'`\+(\d+)` pontos percentuais sobre o acerto, e o inimigo acerta o meio da banda', 'a vantagem do Emboscador')
BANDA_INI = re.search(r'Contra um personagem que investiu em defesa ele acerta `(\d+)%` a `(\d+)%`', p26)
BASE_INI = (int(BANDA_INI.group(1)) + int(BANDA_INI.group(2))) / 2   # o inimigo acerta 52,5%
PAPEL = {n: float(v.replace(',', '.')) for n, v in re.findall(r'^\| `(Brutamontes|Baluarte)` \|[^|]*?vida crua `× ([\d,]+)`', p26, re.M)}
PAPEL.update({n: float(v.replace(',', '.')) for n, v in re.findall(r'^\| `(Baluarte)` \|[^|]+\| vida crua `× ([\d,]+)`', p26, re.M)})
def vida_por_defesa(k): return (BASE_PJ - PP * k) / BASE_PJ          # Defesa +k: o personagem acerta menos
def vida_por_acerto(k): return BASE_INI / (BASE_INI + PP * k)        # acerto +k: ele entrega mais
print('  regressao: a troca reproduz o papel de hoje')
confere('Brutamontes = Defesa -2 pago em vida', round(vida_por_defesa(-2), 3), PAPEL['Brutamontes'])
confere('Baluarte = Defesa +2 pago em vida', round(vida_por_defesa(2), 3), PAPEL['Baluarte'])
if falhas: print('>>> A REGRESSAO DA FICHA FALHOU'); sys.exit(1)
print('  o que a vida paga (ou recebe) por ponto acima (ou abaixo) da tabela:')
print('    pontos   Defesa   acerto e CD')
for k in (-2, -1, 1, 2):
    print(f'    {k:+d}       x{vida_por_defesa(k):.3f}   x{vida_por_acerto(k):.3f}')

# (2) o Capanga: esquadrao de corpos de um golpe (a vida e o que UM personagem derruba por rodada), o
# esquadrao age antes (o "8 + 4" da peca 26 §5), e o grupo mata em ordem. Quanto da vida do grupo ele tira.
def esquadrao(n, corpos, golpes_para_cair, fracao_golpe):
    vivos = [golpes_para_cair] * corpos; batidas = 0; rod = 0
    while vivos:
        rod += 1; batidas += len(vivos)
        for _ in range(n):                                      # cada personagem da um golpe, no primeiro vivo
            if vivos:
                vivos[0] -= 1
                if vivos[0] == 0: vivos.pop(0)
    _, chefe = LINHA[30]; L = chefe / PCT; golpe = chefe / 4
    return rod, batidas * golpe * fracao_golpe / (n * L)
print('\n  o Capanga contra N (o alvo do degrau de 2 rodadas e o trivial do PF2e, '
      f'{100 * RODADAS * TRIVIAL * PCT / 4:.1f}% da vida do grupo):')
print('    forma                                     ' + '  '.join(f'   x{n}     ' for n in range(1, 7)))
for nome, f in (('a) 2N corpos de um golpe, golpe inteiro', lambda n: esquadrao(n, 2 * n, 1, 1)),
                ('b) 2N corpos de um golpe, meio golpe', lambda n: esquadrao(n, 2 * n, 1, 0.5)),
                ('c) N corpos de dois golpes, golpe inteiro', lambda n: esquadrao(n, n, 2, 1))):
    print(f'    {nome:<42}' + '  '.join(f'{f(n)[0]}r {100 * f(n)[1]:>5.1f}%' for n in range(1, 7)))
confere('a forma a) no x4 e o esquadrao de 8 de hoje, que cobra o Desastre', round(esquadrao(4, 8, 1, 1)[1], 3), round(celula(30, 'Desastre', 4)['grupo'], 3))

# (3) sair da condicao no x1 e no x2: a condicao dura uma rodada (manual, a Melhoria Condicao) e o inimigo
# age num turno so (livro de inimigos, Acoes Multiplas), entao pagar no FIM do turno so serve para a que
# dura mais (Concentrada, Duradoura, a Pesada com TR). O preco neutro e a fatia da luta que ela tiraria.
for cat, rod in zip(('Capanga',) + CATS, RODADAS_DELE):
    if cat == 'Capanga': continue
    print(f'    {cat:<11} x1: uma acao negada = {100 / rod:.0f}% da vida dele;  x2: uma = {100 / (2 * rod):.0f}%, a Pesada (1,5) = {150 / (2 * rod):.0f}%')
s30 = LINHA[30][0] / 4
print(f'  preco neutro = o dano de UM personagem por rodada, por acao negada: {s30:.0f} no nivel 30 '
      f'(a vida do Capanga de hoje, {T41["Capanga"][0] if "Capanga" in T41 else "78"})')

# --- corte 3: as celulas com as rodadas fechadas, e o recurso pago no golpe -------------------------
# Rodadas 2 · 2,5 · 3 · 4 · 5 (ele, 28/09; "C": nenhum mecanismo de cauda). A pressao de cada degrau e o
# orcamento do PF2e dividido pela duracao. Resposta "B" dos tracos: o recurso se paga por DENTRO — a
# pressao da celula fica, e o golpe fecha a conta. A banda e o limite de quanto recurso cabe.
print('\nCORTE 3 — o recurso pago no golpe')
m = pega(p26, r'`([\d,]+)` de ação extra numa luta de três rodadas', 'a Intervencao: 0,75 de acao extra')
INTERV = float(m.group(1).replace(',', '.'))
F_INT = float(pega(p26, r'multiplicado por `([\d,]+)`', 'o 0,923 da Intervencao').group(1).replace(',', '.'))
TAB_REC = {c: float(f.replace(',', '.')) for c, f in re.findall(r'^\| \*\*`(Ameaça|Desastre|Catástrofe|Calamidade)`\*\* \| `\d` \| `\d` \| `[\d,]+ ×`[^|]*\| `× ([\d,]+)` \|$', p26, re.M)}
ANT = {'Ameaça': (1, 1), 'Desastre': (4, 3), 'Catástrofe': (6, 5), 'Calamidade': (8, 6)}   # personagens, acoes de hoje
def f_interv(rod, acoes): return 1 + INTERV / (rod * acoes)
def f_recarga(rod, pessoas, acoes):
    razao = 2.5 * (pessoas / 2) / acoes
    disparos = 1 + (rod - 1) / 3                 # sai na primeira, volta com 1/3 em cada comeco de turno
    return (disparos * razao + (rod - disparos)) / rod
print('  regressao: os precos de hoje, pela peca 26 §6.5')
confere('Intervencao do Desastre de hoje (3 acoes, 3 rodadas)', round(1 / f_interv(3, 3), 3), F_INT)
confere('Recarga das quatro de hoje', {c: round(f_recarga(3, *ANT[c]), 2) for c in TAB_REC}, TAB_REC)
if falhas: print('>>> A REGRESSAO DO CORTE 3 FALHOU'); sys.exit(1)
ROD = dict(zip(('Capanga',) + CATS, RODADAS_DELE))
PES = dict([('Capanga', TRIVIAL)] + [(c, PESO[c]) for c in CATS])
L30 = LINHA[30][1] / PCT
def golpe_pct(cat, n, interv=False, recarga=False):
    rod = ROD[cat]; press = PES[cat] * RODADAS / rod
    f = (f_interv(rod, n) if interv else 1) * (f_recarga(rod, n, n) if recarga else 1)
    return 100 * press * (LINHA[30][1] / 4) / f / L30
print(f'  o golpe em % da vida de um personagem (banda {100*BANDA[0]:.0f}-{100*BANDA[1]:.0f}%); * = fora da banda; '
      'Intervencao so onde N x peso >= 4')
print('  degrau      rodadas pressao  recurso              ' + ''.join(f'   x{n} ' for n in range(1, 7)))
for cat in CATS:
    rod = ROD[cat]
    for nome, kw in (('nenhum', {}), ('Intervencao', {'interv': True}), ('Recarga', {'recarga': True}),
                     ('as duas', {'interv': True, 'recarga': True})):
        cel = []
        for n in range(1, 7):
            if kw.get('interv') and n * PES[cat] < 4: cel.append('    - '); continue
            g = golpe_pct(cat, n, **kw)
            cel.append(f'{g:5.1f}' + ('*' if not BANDA[0] * 100 - 1e-9 <= g <= BANDA[1] * 100 + 1e-9 else ' '))
        print(f'  {cat:<11} {rod:>5.1f}  {PES[cat] * RODADAS / rod:>6.3f}  {nome:<20} ' + ' '.join(cel))
print('  o preco de cada recurso na grada nova (multiplica a pressao, e o golpe divide por ele):')
for cat in CATS:
    rod = ROD[cat]
    print(f'    {cat:<11} Intervencao x{f_interv(rod, 1):.3f} (x1) a x{f_interv(rod, 6):.3f} (x6);  Recarga x{f_recarga(rod, 4, 4):.3f} em todo N')

# --- corte 3, as respostas de 28/09: (a) a condicao no x1 e no x2, sem garantia ------------------------
# Ele: "n ser garantido seria melhor. Talvez uma habilidade pra rerolar o TR, rolar no comeco do turno
# dnv ao inves do final". Um TR a mais antes do turno multiplica o que a condicao nega pela chance de
# ele FALHAR nesse TR. A regua da peca 19 §2.2 da o valor com 1, 2 e 3 acoes; o filtro e 3,00x.
print('\nCORTE 3 — a condicao no x1 e no x2 com um TR no comeco do turno')
p19 = ler('sistema/03-mecanica/19-dano-e-condicoes.md')
p01 = ler('sistema/03-mecanica/01-atributos-acerto-defesa.md')
REGUA = {int(k): [float(x.replace(',', '.')) for x in re.findall(r'`([\d,]+)×`', l)]
         for k, l in re.findall(r'^\| (?:\*\*)?`([123])`(?:\*\*)? \|(.*)$', p19, re.M)}
if sorted(REGUA) != [1, 2, 3] or any(len(v) != 4 for v in REGUA.values()): perdida('a regua de 1, 2 e 3 acoes da peca 19 §2.2')
FILTRO = float(pega(p19, r'filtro de dominância de `([\d,]+)×`', 'o filtro de 3,00x').group(1).replace(',', '.'))
TREINO = [100 - int(x) for x in re.search(r'^\| \*\*treinado\*\* \| (\d+)% \| (\d+)% \| (\d+)% \| (\d+)% \| \*\*(\d+)%\*\* \|$', p01, re.M).groups()]
SEM = [100 - int(x) for x in re.search(r'^\| \*\*sem treino\*\* \| (\d+)% \| (\d+)% \| (\d+)% \| (\d+)% \| \*\*(\d+)%\*\* \|$', p01, re.M).groups()]
confere('o TR treinado do inimigo falha 35% (peca 26 §3.1 = peca 1 §6)', TREINO[-1], 35)
print(f'  a regua com 3 acoes (o chefe de hoje): {min(REGUA[3]):.2f}x a {max(REGUA[3]):.2f}x; filtro {FILTRO:.2f}x')
print('  (Lento, Calado, Enfeitiçado, Atordoado; o TR sem treino falha de %d%% no nivel 2 a %d%% no 30)' % (SEM[0], SEM[-1]))
def faixa(v, ps): return f'{min(v) * min(ps) / 100:.2f}x a {max(v) * max(ps) / 100:.2f}x'
for nome, acoes, ps in (('x1, sem nada', 1, [100]), ('x2, sem nada', 2, [100]),
                        ('x1, TR treinado no comeco do turno', 1, [TREINO[-1]]),
                        ('x1, TR sem treino no comeco do turno', 1, SEM),
                        ('x2, TR treinado no comeco do turno', 2, [TREINO[-1]]),
                        ('x2, TR sem treino no comeco do turno', 2, SEM),
                        ('x2, TR treinado com desvantagem', 2, [100 - (100 - TREINO[-1]) ** 2 / 100])):
    v = REGUA[acoes]; hi = max(v) * max(ps) / 100
    print(f'    {nome:<38} {faixa(v, ps):<16} ' + ('passa do filtro' if hi > FILTRO else ''))

# --- a grade inteira com o que esta decidido (28/09) -------------------------------------------------
# Rodadas 2 · 2,5 · 3 · 4 · 5; pressao = orcamento do PF2e / duracao; o golpe carrega a pressao (o
# recurso se paga na vida e nao entrega pressao a mais); acoes = N; o Capanga xN e 2N corpos de um golpe,
# com meio golpe (resposta "B"), e a vida do corpo arredonda para baixo, por inteiro (peca 26 §4.1).
print('\nA GRADE — vida · golpe (acoes = N; o Capanga: corpos x vida de um · meio golpe)')
for nv in (10, 20, 30):
    grupo, chefe = LINHA[nv]; s = grupo / 4; base = chefe / 4
    print(f'  nivel {nv}  (golpe-base {base:.2f}; vida de um personagem {chefe / PCT:.0f})')
    print(f'    {"Capanga":<11} ' + '  '.join(f'x{n}: {2 * n}x{int(s)}·{baixo(base / 2)}' for n in range(1, 7)))
    for cat in CATS:
        rod = ROD[cat]; press = PES[cat] * RODADAS / rod
        print(f'    {cat:<11} ' + '  '.join(f'x{n}: {baixo(rod * n * s)}·{baixo(press * base)}' for n in range(1, 7)))

# --- corte 4: o que dependia de "quatro pessoas e tres rodadas", refeito na grade ------------------
# A simulacao e a do conferir-bestiario.py (checagens 5 e 5.1): os corpos vivos batem, e o grupo gasta a
# saida da rodada neles em ordem. A regressao reproduz antes o que a peca 26 publica com a escada de hoje.
print('\nCORTE 4 — o que dependia de 4 pessoas e 3 rodadas')
def simula(saida, corpos):
    vs = [list(c) for c in corpos]; rod = 0; cobrado = 0.0
    while vs and rod < 100:
        cobrado += sum(c[1] for c in vs); sobra = saida
        while sobra > 0 and vs:
            if vs[0][0] <= sobra: sobra -= vs.pop(0)[0]
            else: vs[0][0] -= sobra; sobra = 0
        rod += 1
    return rod, cobrado
g30, c30 = LINHA[30]
m = pega(p26, r'\| \*\*`sozinho`\*\* \| `100%` \| — \| `([\d,]+)%` \|', 'a linha sozinho do §4.5')
m2 = pega(p26, r'\| \*\*`com um apoio`\*\* \| `([\d,]+)%` \| `1` \| `([\d,]+)%` \|', 'a linha com um apoio do §4.5')
f1 = float(m2.group(1).replace(',', '.')) / 100
_, so = simula(g30, [(945, 219)]); _, um = simula(g30, [(78, 55)] + [(945 * f1, 219 * f1)])
pub = float(m2.group(2).replace(',', '.')) / float(m.group(1).replace(',', '.'))   # 67,5% / 67,6%
confere('§4.5 de hoje: o chefe a 91,5% com um capanga cobra o que a peca publica, relativo a sozinho', round(um / so, 3), round(pub, 3))
_, oito = simula(g30, [(78, 55)] * 8)
confere('§5 de hoje: oito capangas cobram o que o Desastre cobra (a menos de um golpe de capanga)', abs(oito - so) < 55, True)
if falhas: print('>>> A REGRESSAO DO CORTE 4 FALHOU'); sys.exit(1)

def celula4(nv, cat, n):
    grupo, chefe = LINHA[nv]; s = grupo / 4; rod = ROD[cat]; press = PES[cat] * RODADAS / rod
    return dict(s=s, saida=n * s, vida=rod * n * s, golpe=press * chefe / 4, acoes=n, rod=rod)
def capangas(nv, n, k):
    grupo, chefe = LINHA[nv]
    return [(math.floor(grupo / 4), (chefe / 4) / 2)] * k
import math
print('  o cambio: quantos capangas (de meio golpe) cobram o que a celula cobra, no nivel 30')
for cat in CATS:
    linha = []
    for n in (1, 4, 6):
        c = celula4(30, cat, n); _, alvo = simula(c['saida'], [(c['vida'], c['golpe'] * n)])
        k = min(range(1, 80), key=lambda k: abs(simula(c['saida'], capangas(30, n, k))[1] - alvo))
        linha.append(f'x{n}: {k} ({k / n:.2f} por pessoa)')
    print(f'    {cat:<11} ' + '   '.join(linha))
print('  o chefe com capangas: a fracao do chefe que devolve o que ele cobra sozinho (nivel 30)')
for cat in ('Desastre', 'Calamidade'):
    for n in (2, 4, 6):
        c = celula4(30, cat, n); _, alvo = simula(c['saida'], [(c['vida'], c['golpe'] * n)])
        fr = []
        for k in (1, 2, 3):
            f = min((x / 1000 for x in range(300, 1001)),
                    key=lambda f: abs(simula(c['saida'], capangas(30, n, k) + [(c['vida'] * f, c['golpe'] * n * f)])[1] - alvo))
            fr.append(f'{k}: {100 * f:.1f}%')
        print(f'    {cat:<11} x{n}  ' + '  '.join(fr))
print('  N corpos de x1 contra um corpo de xN, do mesmo degrau (o que cobram, nivel 30):')
for cat in CATS:
    rs = []
    for n in (2, 4, 6):
        c1 = celula4(30, cat, 1); cn = celula4(30, cat, n)
        _, um_n = simula(cn['saida'], [(cn['vida'], cn['golpe'] * n)])
        _, n_um = simula(cn['saida'], [(c1['vida'], c1['golpe'])] * n)
        rs.append(f'x{n}: {n_um / um_n:.2f}')
    print(f'    {cat:<11} ' + '  '.join(rs))
print('  os precos que liam 4 e 3, por degrau (o papel e as curas):')
print('    degrau      Artilheiro  cura que empata  H de cura vale   ER por acao (xN: vida / (rod x N))')
for cat in CATS:
    c = celula4(30, cat, 4)
    print(f'    {cat:<11} x{1 + 0.5 / c["rod"]:.3f}      vida / {c["rod"]:<4}      {c["golpe"] / c["s"]:.2f} x H        1/{c["rod"] * 4:.0f} da vida no x4')
print('    papel por N: ' + '  '.join(f'x{n}: Emboscador x{(n - 1 + 1.476) / n:.3f}, Controlador x{1 + 1 / n:.3f}' for n in (1, 2, 4, 6)))
print('    a condicao que o inimigo poe empata quando alvos x acoes negadas = 3 x acoes gastas, em todo N')

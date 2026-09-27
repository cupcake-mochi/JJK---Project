# -*- coding: utf-8 -*-
"""Rodada 3 da revisao dos anti-dominio: a comparacao das quatro (27/09/2026).

Irmao do conta-cesta-oca.py, do conta-dominio-simples.py, do conta-petala.py e do conta-extensao.py,
com o mesmo contrato: a regressao reproduz o que ja esta publicado ANTES de medir coisa nova, a
probabilidade e exata (distribuicao de estados, nada de Monte Carlo), e todo numero que tem dono e
lido do dono. O modelo de cada uma e o do script dela, copiado aqui e conferido contra a peca.

O pedido do Mizuki: nao comparar as quatro antes das tres serem revistas; quando a Extensao fechar,
"a matriz lado a lado — quem cai por que, quanto segura, o que custa, e se alguma ficou dominada".

REGRESSAO
  R1. A tabela medida da Cesta na peca 11 §6.5 (Acertos segurados, sem erguer de novo)
  R2. A tabela medida do Dominio Simples na peca 11 §6.5
  R3. "Paga mais quem cai mais" (peca 11 §6.5): 13% / 17% / 28% do dia, e 32% da Cesta com Essencia 2
  R4. A tabela da Extensao na peca 11 §6.5, com o PE por rodada arredondado para cima (peca 1 §5.4)
  R5. A tabela da Essencia da Petala (o que voce leva: nada, 1/4, metade)
  R6. O PE por rodada das quatro, lido da tabela "As quatro, com numero" — e e dela que o modelo tira
  R7. A regua das maos: a arma 1d10 + Forca da peca 5 §2 e o dado do soco da peca 14 §5.0.6
  R8. O cambio (1 PE por rodada = 5,14 de dano por rodada, peca 5 §4) e a Rotina do manual
  R9. O QUE A v0.274 PUBLICOU (peca 11 §6.5, "As quatro lado a lado") sai deste modelo — conferido no
      fim do script, depois de medir

AS DECISOES DO MIZUKI (27/09/2026): "Pode fazer" (a comparacao); e a queda na hora — "Nos casos aonde o
'ataque do acerto garantido vem imediatamente' e basicamente um extra, chegando no comeco do turno do
inimigo vc vai receber novamente". E a leitura A da secao 6, e e a que as tabelas 1 e 2 usam.
"""
import re, sys, os, math
from math import comb
from functools import lru_cache
R = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))) + os.sep
def ler(c): return open(R + c, encoding='utf-8').read()
pa, p18, p11 = ler('manual/gerador/partA.js'), ler('sistema/03-mecanica/18-progressao.md'), ler('sistema/03-mecanica/11-aptidoes-e-refino.md')
p06, p05, p14, pF = (ler('sistema/03-mecanica/06-caminhos-e-trilhas.md'), ler('sistema/03-mecanica/05-caminho-e-combate-sem-feitico.md'),
                     ler('sistema/03-mecanica/14-equipamento.md'), ler('manual/gerador/partF.js'))
falhas = []
def confere(nome, obtido, esperado):
    ok = obtido == esperado
    print(f'  [{"x" if ok else "!"}] {nome}: {obtido}' + ('' if ok else f'  (esperado {esperado})'))
    if not ok: falhas.append(nome)
def perdida(o): print('ANCORA PERDIDA:', o); sys.exit(1)

# --- os donos -----------------------------------------------------------------------------------
i0 = pa.find("TBL(['Classe', 'Nível', 'Pontos e PE', 'Leve', 'Média', 'Pesada'")
if i0 < 0: perdida('a tabela de Classe do partA')
CL = {int(c): (int(p), int(m)) for c, p, m in re.findall(r"\['(\d)', '\d+', '(\d+)', '\d+', '(\d+)', '\d+'", pa[i0:pa.find('),', i0)])}
def dano(classe): p, m = CL[classe]; return (p - m) * 4.5                 # o Acerto da Expansao, Classe do dono
NV = {int(m.group(1)): dict(mae=int(m.group(2)), ref=int(m.group(4)), cls=int(m.group(5)))
      for m in re.finditer(r'^\| \*\*(\d+)\*\* \| [^|]*\| (\d+) \| (\d+) \| (\d+) \| (\d+) \|', p18, re.M)}
if not NV: perdida('a tabela da peca 18')
def nivel(n): return NV[max(x for x in NV if x <= n)]
m_b = re.search(r'PE por nível: 6 no Emanador[^.]*\. 5 na Vanguarda e no Guia\. (\d+) no Bastião', p06)
if not m_b: perdida('o PE por nivel do Bastiao na peca 6')
BOLSO = int(m_b.group(1))
m_pe = re.search(r'recuperar `\+1` PE \| permanente \| `(\d+),(\d+)`', p05)
if not m_pe: perdida('o cambio da peca 5 §4')
CAMBIO = float(m_pe.group(1) + '.' + m_pe.group(2))
ARMA = {int(n): float(a + '.' + b) for n, _, a, b in re.findall(r'^\| (\d+) \| (\d+) \| (\d+),(\d) \| [\d,]+× \|$', p05, re.M)}
if len(ARMA) != 4: perdida('a arma da peca 5 §2')
i_s = p14.find('### 5.0.6 O soco')
SOCO = {(int(a), int(b)): int(d) for a, b, d in re.findall(r"^> \| \d \| (\d+) a (\d+) \| \*\*d(\d+)\*\* \|$", p14[i_s:i_s + 3000], re.M)}
if len(SOCO) != 4: perdida('o dado do soco na peca 14 §5.0.6')
mrot = re.findall(r"\['(\d+) a (\d+)', '(\d)', '[^']*= (\d+)'", pF)
if not mrot: perdida('a Rotina do manual (partF)')
ROT = {int(c): int(r) for _, _, c, r in mrot}

acertos = lambda ref: ref // 2 + 1                # a Expansao: ao abrir e no comeco de cada turno do dono
dur = lambda ref: max(1, ref // 2)
def pf(bonus, cd): return 1 - max(0, min(20, 21 - (cd - bonus))) / 20
def cd_dono(nv): return 8 + 6 + nivel(nv)['mae']
def binom_menor(n, p, T): return sum(comb(n, f) * p**f * (1 - p)**(n - f) for f in range(min(T, n + 1)))
def metade(e): return max(1, e // 2)
def tr(atrib, treino, nv): return atrib + (nivel(nv)['mae'] if treino else 0)
CENARIOS = ((14, 5), (20, 7), (26, 10))           # (nivel, refino do dono da Expansao) — o dos outros scripts
RODADAS = {'maior': 4, 'igual': 3, 'menor': 2}    # o Simples (peca 11 §6.5) — conferido em R2
LEVA = {'maior': 0.0, 'igual': 0.25, 'menor': 0.5}  # a Petala — conferido em R5

# --- os modelos, um de cada script ---------------------------------------------------------------
def seg_cesta(nv, ref, bonus, T, h=1):            # conta-cesta-oca.py: Acertos segurados, sem erguer de novo
    p = pf(bonus, cd_dono(nv))
    return sum(binom_menor((j - 1) * h, p, T) for j in range(1, acertos(ref) + 1))
def queda(A, p, T, h=1, na_hora=True, leva=0.0, de_novo=True, um_so=False):
    """(Acertos que te alcancam, vezes que ergue de novo) — a Cesta (na_hora=True, leva=0) e a Petala
    (na_hora=False, leva=a fracao da Essencia). As duas caem pelo mesmo teste: h golpes entre um Acerto e o
    seguinte, cada um com falha p, e T falhas derrubam. A Petala caindo so deixa de rebater. Erguer de novo
    custa a Acao Bonus, e ela e uma por rodada: caiu de novo na mesma rodada, fica caida, e volta com a Acao
    Bonus da rodada seguinte.
    A Cesta caindo te expoe na hora, e o texto dela le de dois jeitos:
      um_so=False (leitura A): a queda e um Acerto a mais, e o da rodada ainda vem se ela estiver caida;
      um_so=True  (leitura B): a queda traz o Acerto da rodada antes, e e um so — como o Simples escreve.
    Com h=1 as duas dao o mesmo, e e o modelo dos scripts da Cesta e da Petala."""
    est = {(0, True, False): 1.0}; alc = de = 0.0          # (falhas, de pe, o Acerto desta rodada ja veio)
    for t in range(A):
        e2 = {}
        for (f, up, veio), pr in est.items():
            if not (um_so and veio): alc += pr * (leva if up else 1.0)
            e2[(f, up)] = e2.get((f, up), 0) + pr
        if t == A - 1: break
        rod = {}                                            # (falhas, de pe, Acao Bonus gasta, ja veio)
        for (f, up), pr in e2.items():
            k = (0, True, True, False) if (not up and de_novo) else (f, up, False, False)
            if not up and de_novo: de += pr
            rod[k] = rod.get(k, 0) + pr
        for _ in range(h):
            novo = {}
            for (f, up, ab, veio), pr in rod.items():
                if not up: novo[(f, up, ab, veio)] = novo.get((f, up, ab, veio), 0) + pr; continue
                novo[(f, up, ab, veio)] = novo.get((f, up, ab, veio), 0) + pr * (1 - p)
                if f + 1 < T: k = (f + 1, up, ab, veio)
                else:
                    if na_hora and not (um_so and veio): alc += pr * p
                    v2 = veio or (na_hora and um_so)
                    if de_novo and not ab: de += pr * p; k = (0, True, True, v2)
                    else: k = (f, False, ab, v2)
                novo[k] = novo.get(k, 0) + pr * p
            rod = novo
        est = {}
        for (f, up, ab, veio), pr in rod.items(): est[(f, up, veio)] = est.get((f, up, veio), 0) + pr
    return alc, de
def cesta(A, p, T, h=1, de_novo=True, um_so=False): return queda(A, p, T, h, True, 0.0, de_novo, um_so)
def petala(A, leva, p, T, h=1, de_novo=True): return queda(A, p, T, h, False, leva, de_novo)
def simples_seg(nv, ref, ess, treino, comp):      # conta-dominio-simples.py: segurados, sem erguer de novo
    A = acertos(ref); p = pf(tr(ess, treino, nv), cd_dono(nv)); piso = metade(ess)
    @lru_cache(None)
    def V(t, h, d):
        if t == A or h >= d: return 0.0
        return 1 + (1 - p) * V(t + 1, h + 1, d) + p * V(t + 1, h + 1, max(min(d, piso), d - 1))
    return V(0, 0, RODADAS[comp])
def simples(nv, ref, ess, treino, comp):
    """(Acertos que alcancam, vezes que ergue de novo) — erguendo de novo com a Acao Padrao e metade das
    rodadas sempre que cai. O Acerto que o derruba passa. Golpe em quem segura nao conta."""
    A = acertos(ref); p = pf(tr(ess, treino, nv), cd_dono(nv)); piso = metade(ess); base = RODADAS[comp]
    @lru_cache(None)
    def V(t, h, d):
        if t == A: return (0.0, 0.0)
        if h < d:
            ok, ruim = V(t + 1, h + 1, d), V(t + 1, h + 1, max(min(d, piso), d - 1))
            return ((1 - p) * ok[0] + p * ruim[0], (1 - p) * ok[1] + p * ruim[1])
        if t == A - 1: return (1.0, 0.0)
        r = V(t + 1, 0, max(1, base // 2))
        return (1 + r[0], 1 + r[1])
    return V(0, 0, base)

print('REGRESSAO — o modelo reproduz o que ja esta publicado antes de medir coisa nova')
PERF_C = (('Espírito treinado, Essência `6`', 6, True), ('Espírito treinado, Essência `4`', 4, True), ('sem treino, Essência `2`', 2, False))
pubc = {r: [float(v.replace(',', '.')) for v in vs] for r, *vs in re.findall(
    r'^\| (' + '|'.join(re.escape(x[0]) for x in PERF_C) + r') \| `([\d,]+)` \| `([\d,]+)` \| `([\d,]+)` \|$', p11, re.M)}
if len(pubc) != 3: perdida('a tabela medida da Cesta')
for rot, ess, t in PERF_C:
    confere('R1 a Cesta, ' + rot.replace('`', ''), pubc[rot],
            [round(seg_cesta(nv, ref, tr(ess, t, nv), metade(ess)), 1) for nv, ref in CENARIOS])
LIN_S = {'Essência `6`, maior que a do dono, Espírito treinado': (6, True, 'maior'),
         'Essência `6`, igual à do dono, com ou sem treino': (6, True, 'igual'),
         'Essência `4`, igual à do dono, Espírito treinado': (4, True, 'igual'),
         'Essência `2`, menor que a do dono, sem treino': (2, False, 'menor')}
pubs = {r: [float(x.replace(',', '.')) for x in v[:3]] for r, *v in re.findall(
    r'^\| (' + '|'.join(re.escape(k) for k in LIN_S) + r') \| `([\d,]+)` \| `([\d,]+)` \| `([\d,]+)` \| `([\d,]+)` \|$', p11, re.M)}
if len(pubs) != 4: perdida('a tabela medida do Dominio Simples')
for rot, (ess, t, comp) in LIN_S.items():
    confere('R2 o Simples, ' + rot.replace('`', ''), pubs[rot], [round(simples_seg(nv, ref, ess, t, comp), 1) for nv, ref in CENARIOS])
ic = p11.find('### Por que erguer custa a maior Classe')
cus = p11[ic:p11.find('\n## ', ic)] if ic >= 0 else ''
mp = re.search(r'a média gasta `(\d+)%` do dia na Cesta, `(\d+)%` na Pétala e `(\d+)%` no Simples\. Com Essência `2` e sem treino, a Cesta sobe e cai quase quatro vezes, e chega a `(\d+)%`', cus)
def _pct(nome, ess, t, cmp):
    nv, r = 26, 10; cls = nivel(nv)['cls']; p = pf(tr(ess, t, nv), cd_dono(nv))
    ronda, de = {'Cesta': (0, lambda: cesta(acertos(r), p, metade(ess))[1]),
                 'Petala': (1, lambda: petala(acertos(r), LEVA[cmp], p, metade(ess))[1]),
                 'Simples': (2, lambda: simples(nv, r, ess, t, cmp)[1])}[nome]
    return round(100 * (ronda * dur(r) + cls * (1 + de())) / (BOLSO * nv))
confere('R3 "Paga mais quem cai mais" (Cesta, Petala, Simples com Essencia 4 igual; a Cesta com Essencia 2)',
        [int(x) for x in mp.groups()] if mp else None,
        [_pct('Cesta', 4, True, 'igual'), _pct('Petala', 4, True, 'igual'), _pct('Simples', 4, True, 'igual'), _pct('Cesta', 2, False, 'menor')])
pe_ext = lambda nv: math.ceil(1.5 * nivel(nv)['cls'])      # peca 1 §5.4: o que voce paga sobe
tab = [tuple(int(x) for x in t) for t in re.findall(r'^\| (\d+) \| (\d+) \| (\d+) \| (\d+) \| (\d+) \| \**(\d+)%\** \|$', p11, re.M)]
confere('R4 a tabela da Extensao (nv, refino, duracao, PE, erguer e ate o fim, % do dia)', tab,
        [(n, r, r, pe_ext(n), nivel(n)['cls'] + pe_ext(n) * r, round(100 * (nivel(n)['cls'] + pe_ext(n) * r) / (BOLSO * n))) for n, r, *_ in tab])
ip = p11.find('### Pétala · Classe Passiva 2')
mL = re.search(r'^\| \*\*o dano do Acerto que toca, que você leva\*\* \| (.+?) \| (.+?) \| (.+?) \|$', p11[ip:], re.M)
_fr = lambda c: {'nada': 0.0, 'metade': 0.5}.get(c.strip('` '), None) if c.strip('` ') in ('nada', 'metade') else (lambda a, b: a / b)(*map(int, c.strip('` ').split('/')))
confere('R5 o que a Petala deixa passar (maior, igual, menor)', [_fr(x) for x in mL.groups()] if mL else None, [LEVA['maior'], LEVA['igual'], LEVA['menor']])
iq = p11.find('### As quatro, com número')
q4 = {n: c for n, c in re.findall(r'^\| \*\*(Cesta Oca de Vime|Domínio Simples|Pétala|Extensão de Domínio)\*\* \|[^|]*\|[^|]*\|[^|]*\| (.+?) \|$', p11[iq:iq + 2500], re.M)}
def _ronda(c):
    c = c.replace('*', '').replace('`', '').strip()
    if c == 'nenhum': return lambda nv: 0
    m = re.fullmatch(r'(\d+) fixos?', c)
    if m: return (lambda k: lambda nv: k)(int(m.group(1)))
    if c == '1,5 × maior Classe': return pe_ext
    perdida('o PE por rodada "' + c + '" na tabela das quatro')
confere('R6 o PE por rodada das quatro, da tabela da peca (nv 26)', {k: _ronda(v)(26) for k, v in q4.items()},
        {'Cesta Oca de Vime': 0, 'Domínio Simples': 2, 'Pétala': 1, 'Extensão de Domínio': 11})
RONDA = {'Cesta': _ronda(q4['Cesta Oca de Vime']), 'Simples': _ronda(q4['Domínio Simples']),
         'Petala': _ronda(q4['Pétala']), 'Extensao': _ronda(q4['Extensão de Domínio'])}
confere('R7 a arma 1d10 + Forca (nv 2/10/20/30) e o dado do soco por faixa', ([ARMA[n] for n in (2, 10, 20, 30)], sorted(SOCO.values())),
        ([8.5, 9.5, 10.5, 11.5], [4, 6, 8, 10]))
confere('R8 o cambio e a Rotina de Classe 4 / 7', (CAMBIO, ROT[4], ROT[7]), (5.14, 63, 108))
if falhas: print('\n>>> A REGRESSAO FALHOU — nada abaixo vale.'); sys.exit(1)
print('>>> TUDO OK — o modelo reproduz os numeros publicados.\n')

# --- a medida ------------------------------------------------------------------------------------
PERFIS = (('Essencia 6, maior que a do dono, treinado', 6, True, 'maior'),
          ('Essencia 6, igual a do dono, treinado', 6, True, 'igual'),
          ('Essencia 4, igual a do dono, treinado', 4, True, 'igual'),
          ('Essencia 2, menor que a do dono, sem treino', 2, False, 'menor'))
NOMES = ('Cesta', 'Simples', 'Petala', 'Extensao')
def medida(nome, nv, ref, ess, t, cmp, h=1, toca=True, um_so=False):
    """(Acertos que te alcancam, vezes que ergue de novo, PE gasto na Expansao inteira, ergueu de novo?).
    Na Cesta e na Petala a ficha escolhe o que deixa passar menos: erguer de novo sempre que cai, ou nunca."""
    A = acertos(ref); p = pf(tr(ess, t, nv), cd_dono(nv)); cls = nivel(nv)['cls']; sobe = True
    if nome in ('Cesta', 'Petala'):
        f = (lambda dn: cesta(A, p, metade(ess), h, dn, um_so)) if nome == 'Cesta' else \
            (lambda dn: petala(A, LEVA[cmp], p, metade(ess), h, dn))
        (alc, de), (alc_n, de_n) = f(True), f(False)
        if alc_n < alc - 1e-9: alc, de, sobe = alc_n, 0.0, False
        if nome == 'Petala' and not toca: alc = A              # o Acerto que nao encosta passa por ela
    if nome == 'Simples':  alc, de = simples(nv, ref, ess, t, cmp)
    if nome == 'Extensao': alc, de = 0.0, 0.0
    return alc, de, cls * (1 + de) + RONDA[nome](nv) * dur(ref), sobe

def tabela(titulo, h=1, toca=True):
    print('=' * 112); print(titulo); print('=' * 112)
    print(f'  {"":46s}' + ''.join(f'{f"nv {nv} ({acertos(r)} Acertos)":>22s}' for nv, r in CENARIOS))
    for rot, ess, t, cmp in PERFIS:
        print(f'  {rot}')
        for n in NOMES:
            cel = []
            for nv, r in CENARIOS:
                a, de, pe, sobe = medida(n, nv, r, ess, t, cmp, h, toca)
                cel.append(f'{a:.1f}{" " if sobe else "*"}· {pe:.0f} PE')
            print(f'    {n:44s}' + ''.join(f'{c:>22s}' for c in cel))
    print()
tabela('1 · ACERTOS QUE TE ALCANCAM numa Expansao inteira, e o PE gasto nela (erguer, erguer de novo e o PE por\n'
       '    rodada). 1 golpe por rodada em quem segura; erguendo de novo quando cai, com * onde nao erguer de novo\n'
       '    deixa passar menos. A Cesta pela leitura A (a queda e um Acerto a mais). Sem nada: todos.')
tabela('2 · A MESMA CENA com 2 golpes por rodada em quem segura (o Simples e a Extensao nao caem por golpe)', h=2)

print('=' * 112)
print('3 · A PETALA CONTRA A CESTA, que cai pelo mesmo teste e ergue de novo pela mesma acao. A diferenca e so')
print('    o que passa: a Cesta deixa passar o Acerto da queda; a Petala, a fracao da Essencia em todo Acerto que toca.')
print('=' * 112)
for rot, ess, t, cmp in PERFIS:
    cel = []
    for nv, r in CENARIOS:
        c = medida('Cesta', nv, r, ess, t, cmp); pt = medida('Petala', nv, r, ess, t, cmp)
        cel.append(f'nv {nv}: {c[0]:.1f} x {pt[0]:.1f}, {c[2]:.0f} x {pt[2]:.0f} PE')
    print(f'  {rot:44s} ' + ' | '.join(cel))
print('  (Cesta x Petala: Acertos que alcancam, e PE. Mesmo numero de quedas nas duas — o teste e o mesmo.)')
print()

print('=' * 112)
print('4 · O PRECO QUE NAO E PE, em PE por rodada ligada (1 PE por rodada = 5,14 de dano por rodada)')
print('=' * 112)
def soco(nv): return next(d for (a, b), d in SOCO.items() if a <= nv <= b)
def maos(nv):                                      # a Cesta a quem luta de arma: chute no lugar da arma
    arma = ARMA[max(k for k in ARMA if k <= nv)]; forca = arma - 5.5
    return (arma - ((soco(nv) + 1) / 2 + forca)) * (2 if nv >= 7 else 1) / CAMBIO   # dois golpes do 7 (peca 6 §3.1)
def feitico(nv): return (ROT[nivel(nv)['cls']] - ARMA[max(k for k in ARMA if k <= nv)] * 2) / CAMBIO
for nv in (6, 7, 10, 14, 18, 20, 26, 30):
    print(f'  nv {nv}: a Cesta, quem luta de arma: chute d{soco(nv)} no lugar da arma = {maos(nv):.1f} PE por rodada'
          + (f' · a Extensao, quem conjura: {feitico(nv):.1f} PE por rodada' if nv >= 14 else ''))
print('  (a Cesta tambem tira o escudo e o feitico com Gesto; quem conjura com Gesto perde esses feiticos inteiros)')
print()

print('=' * 112)
print('5 · DOMINANCIA — X domina Y se, em todos os perfis, niveis e cenas (1 e 2 golpes; o Acerto toca ou nao),')
print('    ninguem leva mais Acertos com X, X nao custa mais PE, e X chega no mesmo nivel ou antes. So os numeros:')
print('    o que cada uma cobre (raio, Efeito) e o que cada uma tira (maos, feitico) esta abaixo, fora da conta.')
print('=' * 112)
GATE = {'Cesta': 6, 'Simples': 10, 'Petala': 10, 'Extensao': 18}   # o primeiro nivel de compra, da tabela das quatro
ig = re.findall(r'^\| \*\*(Cesta Oca de Vime|Domínio Simples|Pétala|Extensão de Domínio)\*\* \|[^|]*\| nv (\d+)', p11[iq:iq + 2500], re.M)
confere('o primeiro nivel de compra, da tabela das quatro', {k: int(v) for k, v in ig},
        {'Cesta Oca de Vime': 6, 'Domínio Simples': 10, 'Pétala': 10, 'Extensão de Domínio': 18})
if falhas: sys.exit(1)
CENAS = [(h, toca) for h in (1, 2) for toca in (True, False)]
for x in NOMES:
    for y in NOMES:
        if x == y: continue
        pior_a = pior_pe = 0; melhor = False
        for rot, ess, t, cmp in PERFIS:
            for nv, r in CENARIOS:
                for h, toca in CENAS:
                    ax, _, px, _ = medida(x, nv, r, ess, t, cmp, h, toca); ay, _, py, _ = medida(y, nv, r, ess, t, cmp, h, toca)
                    pior_a = max(pior_a, ax - ay); pior_pe = max(pior_pe, px - py)
                    melhor |= (ax < ay - 1e-9 or px < py - 1e-9)
        dom = pior_a <= 1e-9 and pior_pe <= 1e-9 and GATE[x] <= GATE[y] and melhor
        if dom: print(f'  {x} DOMINA {y} nos numeros')
        elif pior_a <= 1e-9 and GATE[x] <= GATE[y]:
            print(f'  {x} protege sempre pelo menos o que {y} protege, e chega antes ou junto — mas custa ate {pior_pe:.0f} PE a mais')
print('  (nenhuma linha acima = nenhum par em que uma protege sempre pelo menos o mesmo que a outra, chegando antes ou junto;\n'
      '   o que cada uma cobre e o que cada uma tira esta na peca 11 §6.5, em "As quatro lado a lado")')
print()

print('=' * 112)
print('6 · A QUEDA DA CESTA, NAS DUAS LEITURAS — "quando ela cai, a Expansao te alcanca na hora". A: e um Acerto a mais,')
print('    e o da rodada ainda vem se ela estiver caida. B: e o Acerto da rodada que chega antes, e e um so (o Simples')
print('    escreve assim: "e um Acerto so, e nao um na hora da queda e outro depois"). Acertos que alcancam,')
print('    erguendo de novo sempre que cai / nunca; e sem Cesta nenhuma.')
print('=' * 112)
for rot, ess, t, cmp in PERFIS[1:]:
    for h in (1, 2):
        cel = []
        for nv, r in CENARIOS:
            A = acertos(r); p = pf(tr(ess, t, nv), cd_dono(nv)); T = metade(ess)
            a1, an = cesta(A, p, T, h, True)[0], cesta(A, p, T, h, False)[0]
            b1, bn = cesta(A, p, T, h, True, True)[0], cesta(A, p, T, h, False, True)[0]
            cel.append(f'nv {nv}: A {a1:.1f}/{an:.1f} · B {b1:.1f}/{bn:.1f} · nada {A}')
        print(f'  {rot:44s} {h} golpe{"s" if h > 1 else " "}: ' + ' | '.join(cel))
print('  Pela A, com Essencia 2 e 2 golpes por rodada, erguer de novo deixa passar mais do que nao ter Cesta nenhuma.')
print('  Pela B, a Cesta nunca deixa passar mais do que nada, e erguer de novo nunca piora.')
print()

print('=' * 112)
print('7 · O GRUPO NO RAIO — o Simples cobre quem estiver nele; a Cesta, a Petala e a Extensao sao de uma pessoa so.')
print('    Quatro pessoas com a mesma ficha, 1 golpe por rodada em cada uma; o Simples erguido por uma delas.')
print('    Acertos que alcancam somados nas quatro, e o PE somado de quem ergueu.')
print('=' * 112)
for rot, ess, t, cmp in PERFIS:
    cel = []
    for nv, r in CENARIOS:
        s_ = medida('Simples', nv, r, ess, t, cmp); c_ = medida('Cesta', nv, r, ess, t, cmp)
        cel.append(f'nv {nv}: Simples {4 * s_[0]:.1f} · {s_[2]:.0f} PE, quatro Cestas {4 * c_[0]:.1f} · {4 * c_[2]:.0f} PE')
    print(f'  {rot:44s} ' + ' | '.join(cel))
print()

print('=' * 112)
print('8 · O ARREDONDAMENTO DA EXTENSAO — a peca 11 cobra 1,5 x maior Classe arredondado para cima (peca 1 §5.4: "o que')
print('    voce paga sobe"); a peca 26 §6.5 entrava com 1,5 x Classe sem arredondar. No inimigo, erguer repartido')
print('    pelas 3 rodadas da luta, como a peca 26 escreve.')
print('=' * 112)
p26 = ler('sistema/03-mecanica/26-bestiario.md')
m_fi = re.search(r'multiplicado por `(\d),(\d+)`', p26)
if not m_fi: perdida('o fator da Intervencao na peca 26')
FI = float(m_fi.group(1) + '.' + m_fi.group(2))
i0 = pF.find("TBL(['Nível do grupo', 'Dano do grupo por rodada', 'Chefe sozinho: vida', 'Chefe: dano'")
CHEFE = {int(n): int(d) for n, d in re.findall(r"\['(\d+)', '~\d+', '[\d a]+', '(\d+)'", pF[i0:pF.find(')', pF.find('],\n    [', i0))])}
def meio_baixo(x): return math.ceil(x - 0.5)      # o arredondamento da cota na 9.2 do conferir-bestiario
for nv in (2, 30):
    cls = nivel(nv)['cls']
    cota = {'Ameaça': meio_baixo(CHEFE[nv] * 0.25), 'Desastre': meio_baixo(CHEFE[nv] * 1) * FI}
    for nome, pe in (('hoje, sem arredondar', 1.5 * cls), ('arredondando para cima', pe_ext(nv))):
        c = (pe + cls / 3) * CAMBIO
        print(f'  nv {nv} (Classe {cls}), {nome:24s} {pe:g} PE por rodada: ' + ' · '.join(f'{k} {c / v:.0%}' for k, v in cota.items()))

# --- R9: o que a v0.274 publicou (peca 11 §6.5, "As quatro lado a lado") sai deste modelo ----------
print()
print('REGRESSAO DO QUE A v0.274 PUBLICOU (peca 11 §6.5, "As quatro lado a lado")')
il = p11.find('### As quatro lado a lado')
lado = p11[il:p11.find('\n## ', il)] if il >= 0 else ''
if not lado: perdida('a secao "As quatro lado a lado" na peca 11')
_n = lambda x: float(x.replace(',', '.'))
LIN9 = {'Essência `6`, maior que a do dono, treinado': (6, True, 'maior', 1),
        'Essência `4`, igual à do dono, treinado': (4, True, 'igual', 1),
        'Essência `2`, menor, sem treino': (2, False, 'menor', 1),
        'a mesma, com dois golpes por rodada': (2, False, 'menor', 2)}
for rot, (ess, t, cmp, h) in LIN9.items():
    m = re.search(r'^\| ' + re.escape(rot) + r' \|' + r' `([\d,]+)` · `(\d+)` PE \|' * 4 + r'$', lado, re.M)
    pub = [(_n(m.group(2 * i + 1)), int(m.group(2 * i + 2))) for i in range(4)] if m else None
    conta = [(round(a, 1), round(pe)) for a, _, pe, _ in (medida(n, 26, 10, ess, t, cmp, h) for n in NOMES)]
    confere('R9 a linha "' + rot.replace('`', '') + '" (Cesta, Simples, Petala, Extensao)', pub, conta)
def _faixa(rx):
    m = re.search(rx, lado)
    return tuple(_n(x) for x in m.groups()) if m else None
cest = [medida(x, nv, r, e, t, c) for nv, r in CENARIOS for (_, e, t, c) in PERFIS if c == 'maior' for x in ('Cesta', 'Petala')]
dif = [cest[i + 1][2] - cest[i][2] for i in range(0, len(cest), 2)]
confere('R9 a Petala com Essencia maior custa "de 2 a 5 PE a mais que a Cesta"', _faixa(r'custa de `(\d+)` a `(\d+)` PE a mais que a Cesta'),
        (min(dif), max(dif)))
confere('R9 ... e nao deixa passar nada, nem com tres golpes por rodada',
        max(medida('Petala', nv, r, e, t, c, h)[0] for nv, r in CENARIOS for (_, e, t, c) in PERFIS if c == 'maior' for h in (1, 2, 3)), 0.0)
rat = [medida('Extensao', nv, r, e, t, c)[2] / medida(x, nv, r, e, t, c)[2]
       for nv, r in CENARIOS for (_, e, t, c) in PERFIS for x in ('Cesta', 'Simples', 'Petala')]
confere('R9 a Extensao custa "de 1,4 a 7,2 vezes" o PE das outras', _faixa(r'Custa de `([\d,]+)` a `([\d,]+)` vezes o PE das outras'),
        (round(min(rat), 1), round(max(rat), 1)))
FEIT = [feitico(nv) for nv in (18, 20, 26, 30)]
confere('R9 o feitico que quem conjura deixa de lancar, do gate (nv 18) ao 30', _faixa(r'de `([\d,]+)` a `([\d,]+)` PE por rodada, em dano'),
        (round(min(FEIT), 1), round(max(FEIT), 1)))
_s = medida('Simples', 26, 10, 2, False, 'menor'); _c = medida('Cesta', 26, 10, 2, False, 'menor')
confere('R9 o grupo no raio (Simples: Acertos, PE; quatro Cestas: Acertos, PE)',
        _faixa(r'deixam passar `(\d+)` Acertos somados por `(\d+)` PE, contra `(\d+)` Acertos e `(\d+)` PE de quatro Cestas'),
        (round(4 * _s[0]), round(_s[2]), round(4 * _c[0]), round(4 * _c[2])))
MAOS = {nv: maos(nv) for nv in range(6, 31)}
m = re.search(r'no máximo `([\d,]+)` PE por rodada, no nível (\d+), e zero do nível (\d+) em diante', lado)
_top = max(MAOS, key=MAOS.get); _zero = min(nv for nv in MAOS if all(MAOS[k] <= 1e-9 for k in range(nv, 31)))
confere('R9 as maos da Cesta a quem luta de arma (o teto, onde, e desde quando e zero)',
        (_n(m.group(1)), int(m.group(2)), int(m.group(3))) if m else None, (round(MAOS[_top], 1), _top, _zero))
_pior = max(cesta(acertos(10), pf(tr(2, False, 26), cd_dono(26)), 1, 2, True)[0] - acertos(10), 0)
confere('R9 com Essencia 2 e dois golpes, erguer a Cesta de novo deixa passar mais do que nada', _pior > 0,
        'erguer de novo deixa passar mais do que não ter Cesta nenhuma' in lado)
if falhas: print('\n>>> A REGRESSAO DA v0.274 FALHOU — a peca publica o que este modelo nao da.'); sys.exit(1)
print('>>> TUDO OK — a comparacao publicada na v0.274 sai deste modelo.')

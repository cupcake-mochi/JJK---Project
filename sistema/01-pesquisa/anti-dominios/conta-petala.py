# -*- coding: utf-8 -*-
"""Rodada 3 da revisao dos anti-dominio: a Petala (26/09/2026).

Irmao do conta-cesta-oca.py e do conta-dominio-simples.py, com o mesmo contrato: a regressao
reproduz o que ja esta publicado ANTES de medir coisa nova, a probabilidade e exata (binomial e
distribuicao de estados, nada de Monte Carlo), e todo numero que tem dono e lido do dono.

REGRESSAO
  R1. Acerto da Expansao = (pontos - Media) d8, 4,5 por dado                        (partA)
  R2. A tabela da Petala na peca 11 §6.5 ate a v0.271 (refino, Acertos que a Expansao solta, quantos
      ela devolvia) — registro: a v0.272 tirou a tabela, e os valores ficam aqui escritos como historia
  R10. A REGRA PUBLICADA NA v0.272 (peca 11 §6.5 e livro cap. 45): a tabela da Essencia, o preco do
       contra-ataque, a tabela de erguer e os numeros da secao "Por que erguer custa a maior Classe"
       e da Petala saem deste modelo — conferidos no fim do script, depois de medir
  R3. As tres curvas de refino da peca 11 §3
  R4. A tabela medida da Cesta na peca 11 (o mesmo cenario: 1 golpe por rodada, teste do Carregar)
  R5. A tabela medida do Dominio Simples na peca 11 (v0.269)
  R6. 'Por que o custo por rodada e 1 x maior Classe': 20% a 26% do dia do Bastiao por luta de 3,5
      rodadas, 3 a 4 lutas, nos marcos do nivel 10 ao 30                               (peca 11 §6.5)
  R7. O PE por nivel do Bastiao (peca 6)
  R8. A Concentracao e Vigor contra a CD de quem feriu, um teste por golpe; o Carregar e Espirito,
      e Espirito e Essencia                                                           (pecas 3 e 1)
  R9. A regua do contra-ataque: a arma do §2 e o soco extra do §4 da peca 5

AS DECISOES DO MIZUKI (26/09/2026, rodada 3), em tres voltas sobre esta conta:
  1a volta: "um teste de carregar a cada golpe, sendo contra qualquer um" · levanta como as outras,
  e "acao bonus pra levantar na segunda vez, por ser um pouco mais fraco que dom simples" · "so o
  que a energia tiver toque, contato" · "Se a essencia for maior que do inimigo, anula. Se for igual,
  reduz a 1/4 e se for menor reduz pela metade. E anula efeitos que exigem contato, independente da
  essencia" · "Refino 4 e o mesmo requisito narrativo de antes" · rebate "no sentido de contra
  atacar ... energia contra energia, n devolve dano", e o ataque de oportunidade com vantagem ·
  "caso o jogador tenha uma arma corpo a corpo, ele ganha a possibilidade acima".
  2a volta: sem a queda na hora (a secao 6 mediu que ela deixava a Essencia baixa pior que nada) ·
  o soco nao conta · o contra-ataque dispara no golpe corpo a corpo que acerta · o que ela anula e'
  o que a Expansao traz por contato, "n precisa ser o acerto garantido" · 1 PE por rodada e 3 por
  contra-ataque · e erguer: "deveria custar Maior Classe em PE, pra todos eles".
  3a volta: erguer paga toda vez.
  As leituras que apliquei, para ele vetar: "reduz a 1/4" = leva 1/4 · o contador de refino / 2
  saiu · a Essencia e' a do dono da Expansao · metade da Essencia em falhas derruba · o teste nao
  ocupa a Concentracao e a Mao Firme nao protege · contra a incompleta ela nao faz nada.
"""
import re, sys, os
from math import comb
from itertools import product
from functools import lru_cache
R = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))) + os.sep
def ler(c): return open(R + c, encoding='utf-8').read()
pa, p18, p11 = ler('manual/gerador/partA.js'), ler('sistema/03-mecanica/18-progressao.md'), ler('sistema/03-mecanica/11-aptidoes-e-refino.md')
p06, p03, p01 = ler('sistema/03-mecanica/06-caminhos-e-trilhas.md'), ler('sistema/03-mecanica/03-economia-de-acao-e-iniciativa.md'), ler('sistema/03-mecanica/01-atributos-acerto-defesa.md')

falhas = []
def confere(nome, obtido, esperado):
    ok = obtido == esperado
    print(f'  [{"x" if ok else "!"}] {nome}: {obtido}' + ('' if ok else f'  (esperado {esperado})'))
    if not ok: falhas.append(nome)
def perdida(o_que): print('ANCORA PERDIDA:', o_que); sys.exit(1)

# --- Classe -> dano do Acerto (partA) ------------------------------------------------------
i0 = pa.find("TBL(['Classe', 'Nível', 'Pontos e PE', 'Leve', 'Média', 'Pesada'")
if i0 < 0: perdida('tabela de Classe do partA')
CL = {int(c): (int(p), int(m)) for c, p, m in re.findall(r"\['(\d)', '\d+', '(\d+)', '\d+', '(\d+)', '\d+'", pa[i0:pa.find('),', i0)])}
def dano(classe): p, m = CL[classe]; return (p - m) * 4.5

# --- nivel -> maestria, refino, Classe (peca 18) --------------------------------------------
NV = {int(m.group(1)): dict(mae=int(m.group(2)), ref=int(m.group(4)), cls=int(m.group(5)))
      for m in re.finditer(r'^\| \*\*(\d+)\*\* \| [^|]*\| (\d+) \| (\d+) \| (\d+) \| (\d+) \|', p18, re.M)}
if not NV: perdida('tabela da peca 18')
def nivel(n): return NV[max(x for x in NV if x <= n)]

# --- curvas de refino (peca 11 §3) ------------------------------------------------------------
cab = re.search(r'^\| \| (nv \d+(?: \| nv \d+)+) \|$', p11, re.M)
if not cab: perdida('cabecalho da curva das tres rotas na peca 11 §3')
MARCOS = [int(x) for x in re.findall(r'nv (\d+)', cab.group(1))]
CURVA = {}
for rot in ('especialista', 'meio a meio', 'generalista'):
    m = re.search(r'^\| \*\*' + rot + r'\*\*[^|]*\|(.*)\|$', p11, re.M)
    if not m: perdida('linha ' + rot + ' da curva')
    CURVA[rot] = [int(x) for x in re.findall(r'`(\d+)`', m.group(1))]
def refino_rota(rot, nv): return CURVA[rot][max(i for i, mc in enumerate(MARCOS) if mc <= nv)]

# --- a Petala na peca 11 --------------------------------------------------------------------
ip = p11.find('### Pétala · Classe Passiva 2')
if ip < 0: perdida('a secao da Petala na peca 11')
sec = p11[ip:p11.find('\n### ', ip + 5)]
TAB_PET = [(4, 3, 2), (6, 4, 3), (8, 5, 4), (10, 6, 5)]     # a tabela da peca 11 ate a v0.271 (registro, sem dono vivo)
m_bolso = re.search(r'PE por nível: 6 no Emanador[^.]*\. 5 na Vanguarda e no Guia\. (\d+) no Bastião', p06)
if not m_bolso: perdida('o PE por nivel do Bastiao na peca 6')
BOLSO = int(m_bolso.group(1))

acertos = lambda ref: ref // 2 + 1                # a Expansao: ao abrir e no comeco de cada turno do dono
dur = lambda ref: max(1, ref // 2)
devolve = lambda ref: ref // 2                    # a Petala hoje: refino / 2 por cena
def pf(bonus, cd): return 1 - max(0, min(20, 21 - (cd - bonus))) / 20      # falha, igual as outras duas
def cd_dono(nv): return 8 + 6 + nivel(nv)['mae']
def binom_menor(n, p, T): return sum(comb(n, f) * p**f * (1 - p)**(n - f) for f in range(min(T, n + 1)))
def metade(e): return max(1, e // 2)
def tr(atrib, treino, nv): return atrib + (nivel(nv)['mae'] if treino else 0)
CENARIOS = ((14, 5), (20, 7), (26, 10))           # (nivel, refino do dono da Expansao) — o das outras duas

print('REGRESSAO — o modelo reproduz o que ja esta publicado antes de medir coisa nova')
confere('R1 Acerto Classe 6 / 7', (dano(6), dano(7)), (54.0, 63.0))
confere('R2 a tabela da Petala ate a v0.271 (refino, a Expansao solta, a Petala devolvia)', TAB_PET, [(r, acertos(r), devolve(r)) for r, _, _ in TAB_PET])
confere('R3 as tres curvas no nv 14 / 20 / 26 (esp, meio, gen)',
        [[refino_rota(r, nv) for r in CURVA] for nv in (14, 20, 26)], [[7, 6, 4], [9, 7, 5], [10, 10, 7]])
# R4 — a Cesta publicada
def seg_cesta(nv, ref, bonus, T, h=1):
    p = pf(bonus, cd_dono(nv))
    return sum(binom_menor((j - 1) * h, p, T) for j in range(1, acertos(ref) + 1))
PERF_C = (('Espírito treinado, Essência `6`', 6, True), ('Espírito treinado, Essência `4`', 4, True), ('sem treino, Essência `2`', 2, False))
pubc = {r: [float(v.replace(',', '.')) for v in vs] for r, *vs in re.findall(
    r'^\| (' + '|'.join(re.escape(x[0]) for x in PERF_C) + r') \| `([\d,]+)` \| `([\d,]+)` \| `([\d,]+)` \|$', p11, re.M)}
if len(pubc) != 3: perdida('a tabela medida da Cesta na peca 11')
for rot, ess, t in PERF_C:
    confere('R4 a Cesta publicada, ' + rot.replace('`', ''), pubc[rot],
            [round(seg_cesta(nv, ref, tr(ess, t, nv), metade(ess)), 1) for nv, ref in CENARIOS])
# R5 — o Simples publicado (o mesmo modelo do conta-dominio-simples.py)
RODADAS = {'maior': 4, 'igual': 3, 'menor': 2}
def simples(nv, ref, ess, treino, comp):
    A = acertos(ref); p = pf(tr(ess, treino, nv), cd_dono(nv)); piso = metade(ess)
    @lru_cache(None)
    def V(t, h, d):
        if t == A or h >= d: return 0.0
        return 1 + (1 - p) * V(t + 1, h + 1, d) + p * V(t + 1, h + 1, max(min(d, piso), d - 1))
    return V(0, 0, RODADAS[comp])
LIN_S = {'Essência `6`, maior que a do dono, Espírito treinado': (6, True, 'maior'),
         'Essência `6`, igual à do dono, com ou sem treino': (6, True, 'igual'),
         'Essência `4`, igual à do dono, Espírito treinado': (4, True, 'igual'),
         'Essência `2`, menor que a do dono, sem treino': (2, False, 'menor')}
pubs = {r: [float(x.replace(',', '.')) for x in v[:3]] for r, *v in re.findall(
    r'^\| (' + '|'.join(re.escape(k) for k in LIN_S) + r') \| `([\d,]+)` \| `([\d,]+)` \| `([\d,]+)` \| `([\d,]+)` \|$', p11, re.M)}
if len(pubs) != 4: perdida('a tabela medida do Dominio Simples na peca 11')
for rot, (ess, t, comp) in LIN_S.items():
    confere('R5 o Simples publicado, ' + rot.replace('`', ''), pubs[rot], [round(simples(nv, ref, ess, t, comp), 1) for nv, ref in CENARIOS])
# R6 — o custo 1 x Classe
MARCOS10 = [m for m in MARCOS if m >= 10]
fr = [nivel(nv)['cls'] * 3.5 / (BOLSO * nv) for nv in MARCOS10]
confere('R6 1 x Classe: do dia, por luta (min, max) e lutas que cabem (min, max)',
        (round(100 * min(fr)), round(100 * max(fr)), int(1 / max(fr)), int(1 / min(fr))), (20, 26, 3, 4))
confere('R7 PE por nivel do Bastiao', BOLSO, 4)
confere('R8 Concentracao e Vigor contra a CD de quem feriu, um teste por golpe; Carregar e Espirito; Espirito e Essencia',
        (bool(re.search(r'\*\*Concentração\*\* \| o efeito que já está no ar \| \*\*Vigor\*\*', p03)),
         bool(re.search(r'É um teste por golpe que te acerta', p03)),
         bool(re.search(r'^\| \*\*Carregar\*\* \| [^|]*\| \*\*Espírito\*\* \|', p03, re.M)),
         bool(re.search(r'^\| \*\*Espírito\*\* \| Essência \|', p01, re.M))), (True, True, True, True))
if falhas: print('\n>>> A REGRESSAO FALHOU — nada abaixo vale.'); sys.exit(1)
print('>>> TUDO OK — o modelo reproduz os numeros publicados.\n')

def petala(A, P, p, T, h=1, de_novo=False):
    """(Acertos que ela para, Acertos que te alcancam, Acoes Bonus gastas), em media.
    A Acertos da Expansao; ela para os primeiros P (o contador e por cena, e ela dispara sozinha).
    h golpes em voce entre um Acerto e o seguinte; cada um e um teste com falha p; T falhas a derrubam.
    de_novo=False: caida, fica caida.  de_novo=True: como a Cesta — a Expansao te alcanca NA HORA, e
    voce ergue de novo antes do Acerto seguinte (Acao Bonus), com as falhas zeradas; o contador segue."""
    est = {(0, 0, True): 1.0}; para = alc = ab = 0.0
    for t in range(A):
        novo = {}
        for (u, f, up), pr in est.items():
            if up and u < P: para += pr; k = (u + 1, f, up)
            else: alc += pr; k = (u, f, up)
            novo[k] = novo.get(k, 0) + pr
        est = novo
        if t == A - 1: break
        for _ in range(h):
            novo = {}
            for (u, f, up), pr in est.items():
                if not up or u >= P: novo[(u, f, up)] = novo.get((u, f, up), 0) + pr; continue
                k = (u, f, True); novo[k] = novo.get(k, 0) + pr * (1 - p)
                if f + 1 < T: k = (u, f + 1, True); novo[k] = novo.get(k, 0) + pr * p
                elif de_novo:
                    alc += pr * p; ab += pr * p; k = (u, 0, True); novo[k] = novo.get(k, 0) + pr * p
                else:
                    k = (u, f, False); novo[k] = novo.get(k, 0) + pr * p
            est = novo
    return para, alc, ab

ROT_CURTA = {'especialista': 'esp', 'meio a meio': 'meio', 'generalista': 'gen'}
print('=' * 110)
print('1 · QUANTO ELA SEGURA HOJE, sem cair nunca — o contador de refino / 2 por cena, pela rota de quem usa')
print('    (a Expansao com o refino tipico de cada nivel, o mesmo cenario das tabelas da Cesta e do Simples)')
print('=' * 110)
for nv, r in CENARIOS:
    A = acertos(r)
    cel = []
    for rot in CURVA:
        rd = refino_rota(rot, nv)
        cel.append(f'{ROT_CURTA[rot]} (refino {rd}): {min(devolve(rd), A) if rd >= 4 else 0}' + ('' if rd >= 4 else ' — sem o gate'))
    print(f'  nv {nv}, Expansao de refino {r}, {A} Acertos · ' + ' · '.join(cel))
print('  "Sempre sobra um" so vale com refino igual: quem tem refino 2 acima do dono da Expansao para todos.')
viol = [(rd, rx) for rd in range(4, 11) for rx in range(1, 11) if devolve(rd) >= acertos(rx)]
print(f'  pares (refino da Petala, refino da Expansao) em que ela para TODOS: {len(viol)} de {7 * 10}; o menor salto e '
      f'{min(rd - rx for rd, rx in viol)} de refino')
print()

PERFS = (('forte: Ess 6 / Con 6, treinado', 6, 6, True), ('medio: Ess 4 / Con 3, treinado', 4, 3, True),
         ('fraco: Ess 2 / Con 0, sem treino', 2, 0, False))
def linha(nome, fn):
    print(f'  {nome:52s}' + ''.join(f'{fn(nv, r):>12s}' for nv, r in CENARIOS))
print('=' * 110)
print('2 · COMO CAI — Acertos que ela PARA, em media, com 1 golpe por rodada em quem a usa (o cenario da Cesta).')
print('    O refino da Petala e o da rota meio a meio. Entre parenteses, a Cesta e o Simples na mesma cena.')
print('=' * 110)
print(f'  {"":52s}' + ''.join(f'{f"nv {nv} ({acertos(r)})":>12s}' for nv, r in CENARIOS))
for rot, ess, con, t in PERFS:
    print(f'  {rot}')
    P = lambda nv: devolve(refino_rota('meio a meio', nv))
    linha('   D · nao cai por golpe (so o contador)', lambda nv, r: f'{petala(acertos(r), P(nv), 0, 1)[0]:.1f}')
    linha('   A · hoje: Concentracao, Vigor, 1 falha derruba', lambda nv, r: f'{petala(acertos(r), P(nv), pf(tr(con, t, nv), cd_dono(nv)), 1)[0]:.1f}')
    linha('   B · como a Cesta: Carregar, metade da Essencia', lambda nv, r: f'{petala(acertos(r), P(nv), pf(tr(ess, t, nv), cd_dono(nv)), metade(ess))[0]:.1f}')
    linha('   (a Cesta, mesma cena)', lambda nv, r: f'({seg_cesta(nv, r, tr(ess, t, nv), metade(ess)):.1f})')
    comp = 'maior' if ess == 6 else ('igual' if ess == 4 else 'menor')
    linha(f'   (o Simples, Essencia {comp} que a do dono)', lambda nv, r: f'({simples(nv, r, ess, t, comp):.1f})')
print()
print('  Com 2 golpes por rodada:')
for rot, ess, con, t in PERFS:
    P = lambda nv: devolve(refino_rota('meio a meio', nv))
    linha(f'   {rot.split(":")[0]} · A (Vigor, 1 falha)', lambda nv, r: f'{petala(acertos(r), P(nv), pf(tr(con, t, nv), cd_dono(nv)), 1, 2)[0]:.1f}')
    linha(f'   {rot.split(":")[0]} · B (Carregar, metade Ess)', lambda nv, r: f'{petala(acertos(r), P(nv), pf(tr(ess, t, nv), cd_dono(nv)), metade(ess), 2)[0]:.1f}')
print()
print('  B com erguer de novo como a Cesta (a queda te expoe na hora; Acao Bonus para voltar; contador segue):')
print('  Acertos que te ALCANCAM por Expansao — sem erguer de novo → erguendo de novo (Acoes Bonus gastas)')
for rot, ess, con, t in PERFS:
    P = lambda nv: devolve(refino_rota('meio a meio', nv))
    def cel(nv, r):
        p = pf(tr(ess, t, nv), cd_dono(nv))
        a = petala(acertos(r), P(nv), p, metade(ess)); b = petala(acertos(r), P(nv), p, metade(ess), 1, True)
        return f'{a[1]:.1f}→{b[1]:.1f} ({b[2]:.1f})'
    linha(f'   {rot.split(":")[0]}', cel)
print()

print('=' * 110)
print('3 · O QUE CUSTA — PE por Expansao que ela aguenta, e por luta de 3,5 rodadas, em % do dia do Bastiao')
print('    (ligada quando a Expansao abre e desligada quando ela acaba; a Expansao dura metade do refino do dono)')
print('=' * 110)
CUSTOS = (('hoje: 1 x maior Classe por rodada', lambda nv, rod, par: nivel(nv)['cls'] * rod),
          ('2 PE fixos por rodada (o do Simples)', lambda nv, rod, par: 2 * rod),
          ('1 x maior Classe por Acerto que ela PARA', lambda nv, rod, par: nivel(nv)['cls'] * par),
          ('metade da maior Classe por rodada', lambda nv, rod, par: max(1, nivel(nv)['cls'] // 2) * rod))
for nome, f in CUSTOS:
    cel = []
    for nv, r in CENARIOS:
        par = min(devolve(refino_rota('meio a meio', nv)), acertos(r)); dia = BOLSO * nv
        c = f(nv, dur(r), par); cl = f(nv, 3.5, par)
        cel.append(f'nv {nv}: {c:g} PE = {c / dia:4.0%}')
    print(f'  {nome:44s}' + ' · '.join(cel))
print(f'  (no Simples, pela mesma conta: ' + ' · '.join(f'nv {nv}: {2 * dur(r)} PE = {2 * dur(r) / (BOLSO * nv):.0%}' for nv, r in CENARIOS)
      + '; a Cesta nao custa PE)')
print(f'  O dano que ela evita (Acertos que ela para x o Acerto de Classe do dono): ' + ' · '.join(
      f'nv {nv}: {min(devolve(refino_rota("meio a meio", nv)), acertos(r))} x {dano(nivel(nv)["cls"]):.0f} = '
      f'{min(devolve(refino_rota("meio a meio", nv)), acertos(r)) * dano(nivel(nv)["cls"]):.0f}' for nv, r in CENARIOS))
print()

print('=' * 110)
print('4 · O GATE — refino 4 e nivel 10 (a peca) contra refino 2 e nivel 10 (o livro, v0.176)')
print('=' * 110)
def primeiro_marco(seq, gate_ref, gate_nv):
    ref = 1
    for mc, e in zip(MARCOS, seq):
        ref = min(10, ref + 1)
        if e == 'R':
            ref = min(10, ref + 1)
            if mc >= gate_nv and ref >= gate_ref: return mc
    return None
todas = list(product('CRL', repeat=len(MARCOS)))
dif = [s for s in todas if primeiro_marco(s, 2, 10) != primeiro_marco(s, 4, 10)]
print(f'  Em {len(dif)} das {len(todas)} sequencias de marco o marco em que da para comprar a Petala muda.')
n10 = 1 + len([m for m in MARCOS if m <= 10])
print(f'  Motivo: a linha passiva sozinha da refino {n10} no nivel 10, e a aptidao se compra num marco de Refino,')
print(f'  que soma 1. Quem compra a partir do nivel 10 tem refino {n10 + 1} ou mais — os dois gates passam juntos.')
print()

# --- 5. O que o cap. 227 abre: reduzir em vez de anular ---------------------------------------
# Na obra (227, tres transcricoes: neet-life, eiga-manga, manga-games) o Gojo ergue a Petala ja sendo
# cortado, e o Sukuna nota que as feridas sairam RASAS; o Choso: "nao sai ileso; nao e tecnica que encare
# a saida de um dominio"; o Kusakabe: "nao e arrancada como o Simples". Contra o Dagon (108) ela segurou
# ate o soco. Nenhuma fonte da contador nem relogio.
def petala_frac(A, P, f_cont, f_depois, p, T, h=1):
    """Acertos evitados em media, somando fracao: enquanto de pe, os P primeiros Acertos evitam f_cont
    do dano e os seguintes f_depois. Cai pelo teste (p, T), como a Cesta, sem erguer de novo."""
    est = {(0, 0, True): 1.0}; ev = 0.0
    for t in range(A):
        novo = {}
        for (u, f, up), pr in est.items():
            if up: ev += pr * (f_cont if u < P else f_depois)
            k = (u + 1, f, up); novo[k] = novo.get(k, 0) + pr
        est = novo
        if t == A - 1: break
        for _ in range(h):
            novo = {}
            for (u, f, up), pr in est.items():
                if not up: novo[(u, f, up)] = novo.get((u, f, up), 0) + pr; continue
                k = (u, f, True); novo[k] = novo.get(k, 0) + pr * (1 - p)
                k = (u, f + 1, True) if f + 1 < T else (u, f, False); novo[k] = novo.get(k, 0) + pr * p
            est = novo
    return ev
INF = 99
OPC = (('i   hoje: anula refino / 2 por cena', lambda nv, cmp: (devolve(refino_rota('meio a meio', nv)), 1.0, 0.0)),
       ('ii  reduz a metade todo Acerto, sem contador', lambda nv, cmp: (INF, 0.5, 0.5)),
       ('iii anula se a sua Essencia >= a do dono; se menor, metade', lambda nv, cmp: (INF, 0.5 if cmp == 'menor' else 1.0, 0.0)),
       ('iv  anula refino / 2, e depois reduz a metade', lambda nv, cmp: (devolve(refino_rota('meio a meio', nv)), 1.0, 0.5)))
print('=' * 110)
print('5 · ANULAR OU REDUZIR — Acertos evitados em media (meio Acerto evitado conta 0,5), caindo como a Cesta,')
print('    1 golpe por rodada. Rota meio a meio. Entre parenteses, sem cair nunca.')
print('=' * 110)
print(f'  {"":62s}' + ''.join(f'{f"nv {nv} ({acertos(r)})":>16s}' for nv, r in CENARIOS))
for rot, ess, con, t in PERFS:
    cmp = 'maior' if ess == 6 else ('igual' if ess == 4 else 'menor')
    print(f'  {rot} — Essencia {cmp} que a do dono')
    for nome, f in OPC:
        cel = []
        for nv, r in CENARIOS:
            P, a, b = f(nv, cmp); p = pf(tr(ess, t, nv), cd_dono(nv))
            cel.append(f'{petala_frac(acertos(r), P, a, b, p, metade(ess)):.1f} ({petala_frac(acertos(r), P, a, b, 0, 1):.1f})')
        print(f'    {nome:60s}' + ''.join(f'{c:>16s}' for c in cel))
    print(f'    {"(a Cesta, mesma cena)":60s}' + ''.join(f'{f"({seg_cesta(nv, r, tr(ess, t, nv), metade(ess)):.1f})":>16s}' for nv, r in CENARIOS))
    print(f'    {f"(o Simples, Essencia {cmp})":60s}' + ''.join(f'{f"({simples(nv, r, ess, t, cmp):.1f})":>16s}' for nv, r in CENARIOS))
print()

# --- 6. A REGRA DO MIZUKI (26/09/2026, rodada 3) e o custo dela ------------------------------
# 1 - teste do Carregar a cada golpe, de qualquer um (T = metade da Essencia, como a Cesta)
# 2 - levanta como as outras (Reacao quando a Expansao abre, ou Acao Bonus); erguer de novo: Acao Bonus
# 3 - so o Acerto que toca
# 4 - Essencia maior que a do dono: anula; igual: voce leva 1/4; menor: voce leva metade.
#     "reduz a 1/4" lido como "leva 1/4": a outra leitura (leva 3/4) poria o 'igual' abaixo do 'menor'.
# 7/8 - com arma corpo a corpo, quando algo encosta na energia: Reacao, ataque de oportunidade com
#     vantagem contra quem encostou, se estiver ao alcance.
print('=' * 110)
print('6 · A REGRA DO MIZUKI — Acertos que te ALCANCAM por Expansao (em Acertos inteiros de dano), 1 golpe por')
print('    rodada em quem segura; ao cair, a Expansao alcanca na hora e voce ergue de novo com Acao Bonus.')
print('    Entre parenteses, as Acoes Bonus gastas erguendo de novo.')
print('=' * 110)
LEVA = {'maior': 0.0, 'igual': 0.25, 'menor': 0.5}
def petala_regra(A, leva, p, T, h=1):
    est = {0: 1.0}; alc = ab = 0.0                      # estado: falhas (ela sempre volta antes do Acerto seguinte)
    for t in range(A):
        alc += leva                                      # de pe em todo Acerto
        if t == A - 1: break
        for _ in range(h):
            novo = {}
            for f, pr in est.items():
                novo[f] = novo.get(f, 0) + pr * (1 - p)
                if f + 1 < T: novo[f + 1] = novo.get(f + 1, 0) + pr * p
                else: alc += pr * p; ab += pr * p; novo[0] = novo.get(0, 0) + pr * p
            est = novo
    return alc, ab
def cesta_nova(A, p, T, h=1):                            # a Cesta publicada, com a queda na hora e erguer de novo
    est = {0: 1.0}; alc = ab = 0.0
    for t in range(A):
        if t == A - 1: break
        for _ in range(h):
            novo = {}
            for f, pr in est.items():
                novo[f] = novo.get(f, 0) + pr * (1 - p)
                if f + 1 < T: novo[f + 1] = novo.get(f + 1, 0) + pr * p
                else: alc += pr * p; ab += pr * p; novo[0] = novo.get(0, 0) + pr * p
            est = novo
    return alc, ab
print(f'  {"":44s}' + ''.join(f'{f"nv {nv} ({acertos(r)})":>18s}' for nv, r in CENARIOS))
for rot, ess, con, t in PERFS:
    cmp = 'maior' if ess == 6 else ('igual' if ess == 4 else 'menor')
    print(f'  {rot} — Essencia {cmp} que a do dono')
    def c_pet(nv, r):
        a, b = petala_regra(acertos(r), LEVA[cmp], pf(tr(ess, t, nv), cd_dono(nv)), metade(ess)); return f'{a:.1f} ({b:.1f})'
    def c_ces(nv, r):
        a, b = cesta_nova(acertos(r), pf(tr(ess, t, nv), cd_dono(nv)), metade(ess)); return f'{a:.1f} ({b:.1f})'
    def c_sim(nv, r):
        return f'{acertos(r) - simples(nv, r, ess, t, cmp):.1f}'
    print(f'    {"a Petala, pela regra dele":42s}' + ''.join(f'{c_pet(nv, r):>18s}' for nv, r in CENARIOS))
    print(f'    {"a Cesta, erguendo de novo":42s}' + ''.join(f'{c_ces(nv, r):>18s}' for nv, r in CENARIOS))
    print(f'    {"o Simples, sem erguer de novo":42s}' + ''.join(f'{c_sim(nv, r):>18s}' for nv, r in CENARIOS))
print('  (a Petala leva, alem das quedas, a fracao de cada Acerto: 0 com Essencia maior, 1/4 igual, 1/2 menor)')
print()

# --- o contra-ataque, pela regua da peca 5 §4 --------------------------------------------------
m_arma = re.findall(r'^\| (\d+) \| (\d+) \| (\d+),(\d) \| [\d,]+× \|$', p05 := ler('sistema/03-mecanica/05-caminho-e-combate-sem-feitico.md'), re.M)
ARMA = {int(n): float(a + '.' + b) for n, _, a, b in m_arma}
m_soco = re.search(r'o soco no nível 30 — `d10 \+ Força 6` \| permanente \| `(\d+),(\d+)`', p05)
m_eng = re.search(r'disparado por \*"quando você acerta"\*, com dois ataques \| `(\d+)%` \| `(\d+),(\d+)`', p05)
m_ac = re.search(r'`\+1` no \*\*seu\*\* acerto \| permanente \| `(\d+),(\d+)`', p05)
m_ap = re.search(r'uma ação padrão a mais \| permanente \| `(\d+),(\d+)`', p05)
m_pe = re.search(r'recuperar `\+1` PE \| permanente \| `(\d+),(\d+)`', p05)
if not (len(ARMA) == 4 and m_soco and m_eng and m_ac and m_ap and m_pe): perdida('a regua da peca 5 (§2 e §4)')
SOCO30 = float(m_soco.group(1) + '.' + m_soco.group(2)); FREQ_ENG = int(m_eng.group(1)) / 100
ENG = float(m_eng.group(2) + '.' + m_eng.group(3)); AC1 = float(m_ac.group(1) + '.' + m_ac.group(2))
AP = float(m_ap.group(1) + '.' + m_ap.group(2)); PE_DANO = float(m_pe.group(1) + '.' + m_pe.group(2))
print('REGRESSAO DA REGUA DO CONTRA-ATAQUE (peca 5 §2 e §4)')
confere('R9 arma 1d10 + Forca nos niveis 2/10/20/30', [ARMA[n] for n in (2, 10, 20, 30)], [8.5, 9.5, 10.5, 11.5])
confere('R9 o soco extra do Engate = dano cru x frequencia (11,50 x 75%)', int(SOCO30 * FREQ_ENG * 100) / 100, ENG)
BASE = round(0.05 / (AC1 / AP), 2)      # +1 no acerto = +5 pontos no d20, e vale 10,80 de 108 (+10%): base de 50%
confere('R9 a base de acerto que a regua supoe (+1 = 10,80 de 108)', BASE, 0.5)
if falhas: print('\n>>> A REGRESSAO FALHOU.'); sys.exit(1)
VANT = (1 - (1 - BASE) ** 2) / BASE
print(f'  vantagem, pela mesma base: acerta {1 - (1 - BASE) ** 2:.0%} em vez de {BASE:.0%}, fator {VANT:.2f}')
print()
print('=' * 110)
print('7 · O CONTRA-ATAQUE — quanto ele vale e quanto PE paga ele (1 PE por rodada = 5,14 de dano por rodada, peca 5 §4)')
print('=' * 110)
for n in (10, 20, 30):
    uso = ARMA[n] * VANT
    print(f'  nv {n}: arma 1d10 + Forca = {ARMA[n]:.1f}; com vantagem vale {uso:.2f} por uso = {uso / PE_DANO:.2f} PE por uso;'
          f' por rodada, disparando em 50% / 75% / 100% das rodadas: ' + ' / '.join(f'{uso * f / PE_DANO:.1f}' for f in (0.5, 0.75, 1.0)) + ' PE')
print(f'  (uma Trilha inteira sao 5 fatias; o contra-ataque em 75% das rodadas no nv 30 vale {ARMA[30] * VANT * 0.75:.1f} de dano por rodada)')

print()
print('  A queda na hora, com Essencia menor: erguer de novo pode sair PIOR que deixar caida (Acertos que alcancam):')
def petala_sem_erguer(A, leva, p, T, h=1):
    est = {(0, True): 1.0}; alc = 0.0
    for t in range(A):
        for (f, up), pr in est.items(): alc += pr * (leva if up else 1.0)
        if t == A - 1: break
        for _ in range(h):
            novo = {}
            for (f, up), pr in est.items():
                if not up: novo[(f, up)] = novo.get((f, up), 0) + pr; continue
                novo[(f, True)] = novo.get((f, True), 0) + pr * (1 - p)
                if f + 1 < T: novo[(f + 1, True)] = novo.get((f + 1, True), 0) + pr * p
                else: alc += pr * p; novo[(f, False)] = novo.get((f, False), 0) + pr * p
            est = novo
    return alc
for rot, ess, con, t in PERFS:
    cmp = 'maior' if ess == 6 else ('igual' if ess == 4 else 'menor')
    cel = [f'nv {nv}: erguendo {petala_regra(acertos(r), LEVA[cmp], pf(tr(ess, t, nv), cd_dono(nv)), metade(ess))[0]:.1f}'
           f' · deixando caida {petala_sem_erguer(acertos(r), LEVA[cmp], pf(tr(ess, t, nv), cd_dono(nv)), metade(ess)):.1f}'
           f' · sem Petala {acertos(r)}' for nv, r in CENARIOS]
    print(f'    {rot.split(":")[0]:6s} ' + ' | '.join(cel))
print()
print('  O conserto medido: a queda da Petala SEM o "na hora" — ela so deixa de rebater, e o Acerto seguinte a pega')
print('  inteira se ela nao voltar antes. Erguendo de novo (Acao Bonus) antes do Acerto seguinte:')
def petala_sem_na_hora(A, leva, p, T, h=1):
    est = {0: 1.0}; alc = ab = 0.0
    for t in range(A):
        alc += leva
        if t == A - 1: break
        for _ in range(h):
            novo = {}
            for f, pr in est.items():
                novo[f] = novo.get(f, 0) + pr * (1 - p)
                if f + 1 < T: novo[f + 1] = novo.get(f + 1, 0) + pr * p
                else: ab += pr * p; novo[0] = novo.get(0, 0) + pr * p
            est = novo
    return alc, ab
for rot, ess, con, t in PERFS:
    cmp = 'maior' if ess == 6 else ('igual' if ess == 4 else 'menor')
    cel = []
    for nv, r in CENARIOS:
        a, b = petala_sem_na_hora(acertos(r), LEVA[cmp], pf(tr(ess, t, nv), cd_dono(nv)), metade(ess))
        c = cesta_nova(acertos(r), pf(tr(ess, t, nv), cd_dono(nv)), metade(ess))[0]
        cel.append(f'nv {nv}: {a:.1f} ({b:.1f} AB) · Cesta {c:.1f}')
    print(f'    {rot.split(":")[0]:6s} ' + ' | '.join(cel))
print()

# --- 8. PE PARA ERGUER = maior Classe, nas quatro (pergunta do Mizuki, 26/09) -------------------
# Hoje nenhuma cobra para erguer: so por rodada (Cesta 0, Simples 2, Petala 1 pela decisao desta rodada,
# Extensao 1,5 x maior Classe arredondado para cima). A proposta: erguer custa a maior Classe em PE.
def simples_sobe(nv, ref, ess, treino, comp):
    """(Acertos segurados, vezes que ergue de novo) — o modelo publicado do conta-dominio-simples.py."""
    A = acertos(ref); p = pf(tr(ess, treino, nv), cd_dono(nv)); piso = metade(ess); base = RODADAS[comp]
    @lru_cache(None)
    def V(t, h, d):
        if t == A: return (0.0, 0.0)
        if h < d:
            ok, ruim = V(t + 1, h + 1, d), V(t + 1, h + 1, max(min(d, piso), d - 1))
            return (1 + (1 - p) * ok[0] + p * ruim[0], (1 - p) * ok[1] + p * ruim[1])
        if t == A - 1: return (0.0, 0.0)
        r = V(t + 1, 0, max(1, base // 2))
        return (r[0], 1 + r[1])
    return V(0, 0, base)
import math
print('=' * 110)
print('8 · ERGUER CUSTANDO A MAIOR CLASSE — PE por Expansao que ela segura, e em % do dia do Bastiao (4 PE por nivel).')
print('    Perfil medio (Essencia 4, igual a do dono, treinado), 1 golpe por rodada; erguendo de novo sempre que cai.')
print('    "hoje" = so o PE por rodada; "+ erguer (1a vez)" = a Classe so na primeira; "+ erguer (toda vez)" = a cada vez.')
print('=' * 110)
ess, t, cmp = 4, True, 'igual'
print(f'  {"":14s}' + ''.join(f'{f"nv {nv} (Classe {nivel(nv)[chr(99)+chr(108)+chr(115)]}, {dur(r)} rod.)":>32s}' for nv, r in CENARIOS))
for nome in ('Cesta', 'Simples', 'Petala', 'Extensao'):
    lin = {'hoje': [], '+ erguer (1a vez)': [], '+ erguer (toda vez)': []}
    for nv, r in CENARIOS:
        cls = nivel(nv)['cls']; rod = dur(r); dia = BOLSO * nv; p = pf(tr(ess, t, nv), cd_dono(nv))
        if nome == 'Cesta':    ronda, de_novo = 0, cesta_nova(acertos(r), p, metade(ess))[1]
        if nome == 'Simples':  ronda, de_novo = 2, simples_sobe(nv, r, ess, t, cmp)[1]
        if nome == 'Petala':   ronda, de_novo = 1, petala_sem_na_hora(acertos(r), LEVA[cmp], p, metade(ess))[1]
        if nome == 'Extensao': ronda, de_novo = math.ceil(1.5 * cls), 0.0
        base = ronda * rod
        for k, extra in (('hoje', 0), ('+ erguer (1a vez)', cls), ('+ erguer (toda vez)', cls * (1 + de_novo))):
            v = base + extra; lin[k].append(f'{v:5.1f} PE = {v / dia:4.0%}')
    for k, cel in lin.items():
        print(f'  {nome if k == "hoje" else "":9s}{k:22s}' + ''.join(f'{c:>24s}' for c in cel))
print(f'  (a Extensao nas mesmas rodadas da Expansao; se o gate dela ainda nao chegou, a linha e teorica)')

print()

# --- R10: a regra publicada na v0.272 sai deste modelo ------------------------------------------
print('REGRESSAO DO QUE A v0.272 PUBLICOU (peca 11 §6.5 e livro cap. 45)')
p45 = ler('sistema/05-material/livro/manual/45-aptidoes-e-refino.md')
def _fr(c):
    c = c.replace('`', '').strip()
    return {'nada': 0.0, 'metade': 0.5}.get(c) if c in ('nada', 'metade') else (lambda a, b: a / b)(*map(int, c.split('/')))
for nome, txt, rx in (('peca 11', sec, r'^\| \*\*o dano do Acerto que toca, que você leva\*\* \| (.+?) \| (.+?) \| (.+?) \|$'),
                      ('livro cap. 45', p45, r'^\| o dano do Acerto que toca, que você leva \| (.+?) \| (.+?) \| (.+?) \|$')):
    m = re.search(rx, txt, re.M)
    confere(f'R10 a tabela da Essencia, {nome} (maior, igual, menor)', [_fr(x) for x in m.groups()] if m else None,
            [LEVA['maior'], LEVA['igual'], LEVA['menor']])
m = re.search(r'Cada contra-ataque custa `(\d+)` PE', sec)
confere('R10 o contra-ataque: o preco publicado e o meio da regua (nv 10, 20, 30)',
        int(m.group(1)) if m else None, round(sum(ARMA[n] * VANT / PE_DANO for n in (10, 20, 30)) / 3))
confere('R10 o contra-ataque: 2,8 e 3,4 PE no nivel 10 e 30, como a peca escreve',
        [round(ARMA[n] * VANT / PE_DANO, 1) for n in (10, 30)],
        [float(x.replace(',', '.')) for x in re.search(r'vale `([\d,]+)` PE no nível 10 e `([\d,]+)` no nível 30', sec).groups()])
ic = p11.find('### Por que erguer custa a maior Classe')
cus = p11[ic:p11.find('\n## ', ic)] if ic >= 0 else ''
tab = [(int(a), int(b), int(c)) for a, b, c in re.findall(r'^\| (\d+) \| (\d) \| (\d+)% \|$', cus, re.M)]
confere('R10 erguer uma vez, em % do dia do Bastiao (nv, Classe, %)', tab,
        [(n, nivel(n)['cls'], round(100 * nivel(n)['cls'] / (BOLSO * n))) for n, _, _ in tab] if tab else ['a tabela'])
def _pct(nome, ess, t, cmp):
    nv, r = 26, 10; cls = nivel(nv)['cls']; p = pf(tr(ess, t, nv), cd_dono(nv)); dia = BOLSO * nv
    if nome == 'Cesta': ronda, dn = 0, cesta_nova(acertos(r), p, metade(ess))[1]
    if nome == 'Petala': ronda, dn = 1, petala_sem_na_hora(acertos(r), LEVA[cmp], p, metade(ess))[1]
    if nome == 'Simples': ronda, dn = 2, simples_sobe(nv, r, ess, t, cmp)[1]
    return round(100 * (ronda * dur(r) + cls * (1 + dn)) / dia)
mp = re.search(r'a média gasta `(\d+)%` do dia na Cesta, `(\d+)%` na Pétala e `(\d+)%` no Simples\. Com Essência `2` e sem treino, a Cesta sobe e cai quase quatro vezes, e chega a `(\d+)%`', cus)
confere('R10 "Paga mais quem cai mais": Cesta, Petala, Simples (Ess 4 igual), e a Cesta com Ess 2',
        [int(x) for x in mp.groups()] if mp else None,
        [_pct('Cesta', 4, True, 'igual'), _pct('Petala', 4, True, 'igual'), _pct('Simples', 4, True, 'igual'), _pct('Cesta', 2, False, 'menor')])
mh = re.search(r'passariam `([\d,]+)` a `([\d,]+)` Acertos contra os `(\d+)` de não ter Pétala nenhuma\.\* Sem a queda na hora, passam `([\d,]+)`', sec)
_p = pf(tr(2, False, 26), cd_dono(26)); _A = acertos(10)
confere('R10 a queda na hora (Ess 2 menor, sem treino, nv 26): deixando caida, erguendo, sem Petala, e sem a queda na hora',
        [float(mh.group(1).replace(',', '.')), float(mh.group(2).replace(',', '.')), int(mh.group(3)), float(mh.group(4).replace(',', '.'))] if mh else None,
        [round(petala_sem_erguer(_A, LEVA['menor'], _p, metade(2)), 1), round(petala_regra(_A, LEVA['menor'], _p, metade(2))[0], 1), _A,
         round(petala_sem_na_hora(_A, LEVA['menor'], _p, metade(2))[0], 1)])
if falhas: print('\n>>> A REGRESSAO DA v0.272 FALHOU — a peca publica o que este modelo nao da.'); sys.exit(1)
print('>>> TUDO OK — a regra publicada na v0.272 sai deste modelo.')

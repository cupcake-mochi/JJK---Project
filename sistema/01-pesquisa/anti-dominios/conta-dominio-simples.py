# -*- coding: utf-8 -*-
"""Rodada 3 da revisao dos anti-dominio: o Dominio Simples (24/09/2026).

Irmao do conta-cesta-oca.py, com o mesmo contrato: a regressao reproduz o que ja esta
publicado ANTES de medir coisa nova, a probabilidade e exata (binomial e programacao
dinamica, nada de Monte Carlo), e todo numero que tem dono e lido do dono.

REGRESSAO
  R1. Acerto da Expansao = (pontos - Media) d8, 4,5 por dado                      (partA)
  R2. A Expansao solta refino//2 + 1 Acertos em metade do refino rodadas          (peca 11 §6.5)
  R3. O Dominio Simples de hoje: nv22 30 PE e 324 evitados; nv26 35 PE e 378     (rascunho 8.4)
  R4. A saida do rascunho 'um teste a cada Acerto, contra a CD do dono': 1,9 / 1,0 / 0,2 com
      bonus +10 / +7 / +0 — reproduzida pela media SEM teto, s/(1-s), contra a CD do nv 26.
      Com o teto de 6 Acertos do refino 10 o +10 da menos, e o script imprime os dois.
  R5. A tabela medida da Cesta na peca 11 (v0.267), que e a base da rodada 3
  R6. As tres curvas de refino da peca 11 §3, e a linha passiva da peca 18
  R7. O texto do Dominio Simples na peca 11: o raio, o custo e os pes
  R8. O cambio de PE (peca 5 §4) e o preco do deslocamento (DESENHO-trilhas)
  R9. As rotas nomeadas reproduzem as curvas da peca 11 §3
  R10. A REGRA PUBLICADA NA v0.268 (peca 11 §6.5 e livro cap. 45): o texto da caixa, a tabela de
       rodadas por Essencia e a tabela medida saem do modelo abaixo — e a copia do livro bate

AS DECISOES DO MIZUKI (24/09/2026, rodada 3), em duas voltas sobre esta conta:
  1a volta: refino contra refino · o Acerto de abrir nao conta · sobe com Reacao a uma Expansao,
  ou Acao Bonus no turno · sem recarga, subir de novo gasta a acao, e a Expansao alcanca na hora
  quem estava protegido (a Cesta tambem) · o gate com o voto do iniciante.
  2a volta: "ele aguenta uma quantidade de rodadas igual a metade da essencia + 1 (min 1),
  reduzindo em 1 para cada 1 ponto de diferenca no refino do oponente contra o seu" — e a regra
  publicada; as saidas (b1) e (b2) da secao 1 ficam como o registro do que foi medido antes dela ·
  "remova o requisito de nivel" · "vai 2 de PE fixo".
"""
import re, sys, os
from math import comb, ceil
from itertools import product
R = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))) + os.sep
def ler(c): return open(R + c, encoding='utf-8').read()
pa, p18, p11 = ler('manual/gerador/partA.js'), ler('sistema/03-mecanica/18-progressao.md'), ler('sistema/03-mecanica/11-aptidoes-e-refino.md')
p05, dtr = ler('sistema/03-mecanica/05-caminho-e-combate-sem-feitico.md'), ler('DESENHO-trilhas.md')

falhas = []
def confere(nome, obtido, esperado):
    ok = obtido == esperado
    print(f'  [{"x" if ok else "!"}] {nome}: {obtido}' + ('' if ok else f'  (esperado {esperado})'))
    if not ok: falhas.append(nome)
def perdida(o_que): print('ANCORA PERDIDA:', o_que); sys.exit(1)

# --- tabela de Classe (partA) -> dano do Acerto -------------------------------------------
i0 = pa.find("TBL(['Classe', 'Nível', 'Pontos e PE', 'Leve', 'Média', 'Pesada'")
if i0 < 0: perdida('tabela de Classe do partA')
CL = {int(c): (int(p), int(m)) for c, p, m in re.findall(r"\['(\d)', '\d+', '(\d+)', '\d+', '(\d+)', '\d+'", pa[i0:pa.find('),', i0)])}
def dano(classe): p, m = CL[classe]; return (p - m) * 4.5

# --- nivel -> maestria, refino passivo, Classe (peca 18) ---------------------------------
NV = {int(m.group(1)): dict(mae=int(m.group(2)), ref=int(m.group(4)), cls=int(m.group(5)))
      for m in re.finditer(r'^\| \*\*(\d+)\*\* \| [^|]*\| (\d+) \| (\d+) \| (\d+) \| (\d+) \|', p18, re.M)}
if not NV: perdida('tabela da peca 18')
def nivel(n): return NV[max(x for x in NV if x <= n)]

# --- as tres curvas de refino (peca 11 §3) -----------------------------------------------
cab = re.search(r'^\| \| (nv \d+(?: \| nv \d+)+) \|$', p11, re.M)
if not cab: perdida('cabecalho da curva das tres rotas na peca 11 §3')
MARCOS = [int(x) for x in re.findall(r'nv (\d+)', cab.group(1))]
CURVA = {}
for rot in ('especialista', 'meio a meio', 'generalista'):
    m = re.search(r'^\| \*\*' + rot + r'\*\*[^|]*\|(.*)\|$', p11, re.M)
    if not m: perdida('linha ' + rot + ' da curva')
    CURVA[rot] = [int(x) for x in re.findall(r'`(\d+)`', m.group(1))]
def refino_rota(rot, nv): return CURVA[rot][max(i for i, mc in enumerate(MARCOS) if mc <= nv)]

# --- o Dominio Simples na peca 11 (v0.268) ----------------------------------------------
# O custo de ATE a v0.267 (1 × maior Classe) nao mora mais em lugar nenhum vivo: ele e' o
# ponto de partida historico do rascunho 8.4, e a regressao R3 o reconstroi com MULT_PE = 1.
ds = re.search(r'raio `(\d+),(\d+) m \+ refino ÷ (\d+)`, que cobre quem estiver nele\. '
               r'Lá dentro a Expansão não alcança ninguém.*?custa `(\d+)` PE por rodada\.\*\*', p11)
if not ds: perdida('a caixa do Dominio Simples na peca 11 (raio e custo)')
RAIO0, DIV_RAIO, PE_FIXO = float(ds.group(1) + '.' + ds.group(2)), int(ds.group(3)), int(ds.group(4))
MULT_PE = 1                               # o de ate a v0.267, so para a regressao R3
for frase in ('Ele aguenta a Expansão por metade da sua Essência (no mínimo 1) mais uma rodada',
              'cada ponto de refino que o dono dela tem acima do seu tira uma rodada; ele sempre aguenta pelo menos uma',
              'O Acerto de quando ela abre não conta. Quando ele cai, a Expansão alcança na hora quem ele protegia',
              'Com refino 4, só com o voto do iniciante'):
    if frase not in p11: perdida('a regra do Dominio Simples na peca 11: ' + frase)

# --- o cambio: 1 PE por rodada e o deslocamento de 9 m, em dano por rodada ----------------
m_pe = re.search(r'recuperar `\+1` PE \| permanente \| `(\d+),(\d+)`', p05)
m_mv = re.search(r'abrir mão do deslocamento de `9 m` \| `−(\d+),(\d+)`', dtr)
if not (m_pe and m_mv): perdida('o cambio de PE (peca 5 §4) ou o preco do deslocamento (DESENHO-trilhas)')
PE_EM_DANO = float(m_pe.group(1) + '.' + m_pe.group(2)); DESLOC = float(m_mv.group(1) + '.' + m_mv.group(2))

acertos = lambda ref: ref // 2 + 1
dur = lambda ref: max(1, ref // 2)
def pf(bonus, cd): return 1 - max(0, min(20, 21 - (cd - bonus))) / 20      # falha, igual a Cesta
def cd_dono(nv): return 8 + 6 + nivel(nv)['mae']
def binom_menor(n, p, T): return sum(comb(n, f) * p**f * (1 - p)**(n - f) for f in range(min(T, n + 1)))
def metade_ess(e): return max(1, e // 2)

print('REGRESSAO — o modelo reproduz o que ja esta publicado antes de medir coisa nova')
confere('R1 Acerto Classe 6 / 7', (dano(6), dano(7)), (54.0, 63.0))
confere('R2 Acertos que a Expansao solta, refino 4/6/8/10', [acertos(r) for r in (4, 6, 8, 10)], [3, 4, 5, 6])
confere('R3 Dominio Simples ate a v0.267, nv22 (PE, evitado)', (MULT_PE * nivel(22)['cls'] * dur(10), acertos(10) * dano(nivel(22)['cls'])), (30, 324.0))
confere('R3 Dominio Simples ate a v0.267, nv26 (PE, evitado)', (MULT_PE * nivel(26)['cls'] * dur(10), acertos(10) * dano(nivel(26)['cls'])), (35, 378.0))
s = [1 - pf(b, cd_dono(26)) for b in (10, 7, 0)]
confere('R4 o rascunho sem teto, s/(1-s), bonus +10/+7/+0 contra a CD do nv26', [round(x / (1 - x), 1) for x in s], [1.9, 1.0, 0.2])
com_teto = [round(sum(x**j for j in range(1, acertos(10) + 1)), 1) for x in s]
print(f'      (com o teto de {acertos(10)} Acertos do refino 10, a mesma conta da {com_teto} — o rascunho nao tinha o teto)')
def seg_cesta(nv, ref, bonus, T):     # a Cesta publicada: um golpe por rodada, T = metade da Essencia
    p = pf(bonus, cd_dono(nv))
    return sum(binom_menor(j - 1, p, T) for j in range(1, acertos(ref) + 1))
PERF = (('Vigor treinado, Constituição `6`, Essência `6`', 6, True, 3),
        ('Vigor treinado, Constituição `3`, Essência `4`', 3, True, 2),
        ('sem treino, Constituição `0`, Essência até `3`', 0, False, 1))
CENARIOS = ((14, 5), (20, 7), (26, 10))    # os mesmos da tabela da Cesta: (nivel, refino do dono da Expansao)
pub = {r: [float(v.replace(',', '.')) for v in vs] for r, *vs in re.findall(
    r'^\| (' + '|'.join(re.escape(x[0]) for x in PERF) + r') \| `([\d,]+)` \| `([\d,]+)` \| `([\d,]+)` \|$', p11, re.M)}
if len(pub) != 3: perdida('a tabela medida da Cesta na peca 11')
for rot, con, tr, T in PERF:
    calc = [round(seg_cesta(nv, ref, con + (nivel(nv)['mae'] if tr else 0), T), 1) for nv, ref in CENARIOS]
    confere('R5 a Cesta publicada, ' + rot.split(',')[0] + f' Con {con}', pub[rot], calc)
confere('R6 as tres curvas no nv 14 / 20 / 26 (esp, meio, gen)',
        [[refino_rota(r, nv) for r in CURVA] for nv in (14, 20, 26)], [[7, 6, 4], [9, 7, 5], [10, 10, 7]])
confere('R7 o raio no refino 4 e 10', (RAIO0 + 4 // DIV_RAIO, RAIO0 + 10 // DIV_RAIO), (3.5, 6.5))
confere('R8 o cambio de PE e o deslocamento, em dano por rodada', (PE_EM_DANO, DESLOC), (5.14, 5.40))

# --- A REGRA PUBLICADA (v0.268), e a conferencia dela ------------------------------------
def rodadas_ds(ess, r_def, r_dono):
    """metade da Essencia (minimo 1) mais uma rodada; cada ponto de refino que o dono tem
    acima do seu tira uma; ele sempre aguenta pelo menos uma. Mais refino nao da rodada a mais."""
    return max(1, metade_ess(ess) + 1 - max(0, r_dono - r_def))
def segura_regra(A, N, levanta=False):
    """o Acerto de abrir nao conta; depois dele, N rodadas (um Acerto cada); o seguinte o
    derruba e passa. levanta=True: sobe de novo sem espera, e a conta recomeca no Acerto seguinte."""
    seg, t_, cap = 1, 1, N
    while t_ < A:
        if cap > 0: seg += 1; cap -= 1
        elif levanta: cap = N
        else: break
        t_ += 1
    return seg
ROTAS = {'especialista (Refino em todo marco)': 'R' * 7, 'Refino no 6 e no 10': 'RRCCCCC',
         'meio a meio (Refino no 6, 14 e 22)': 'RCRCRCC',
         'um Refino só, no marco 10': 'CRCCCCC', 'um Refino só, no marco 14': 'CCRCCCC'}
def _curva(seq):
    ref, out = 1, []
    for e in seq: ref = min(10, ref + 1 + (e == 'R')); out.append(ref)
    return out
confere('R9 as rotas nomeadas reproduzem as curvas da peca 11 §3',
        (_curva('R' * 7), _curva('RCRCRCC')), (CURVA['especialista'], CURVA['meio a meio']))

_rod = re.search(r'^\| \*\*rodadas que ele aguenta\*\*, com refino igual ou maior que o do dono \| `(\d+)` \| `(\d+)` \| `(\d+)` \|$', p11, re.M)
if not _rod: perdida('a tabela de rodadas do Dominio Simples na peca 11')
confere('R10 rodadas por Essencia (0-3, 4-5, 6), na peca 11', [int(x) for x in _rod.groups()],
        [rodadas_ds(e, 10, 10) for e in (3, 5, 6)])
if [rodadas_ds(e, 10, 10) for e in (0, 3)] != [rodadas_ds(3, 10, 10)] * 2 or rodadas_ds(4, 10, 10) != rodadas_ds(5, 10, 10):
    falhas.append('R10 as faixas de Essencia da tabela nao sao faixas da regra')
p45 = ler('sistema/05-material/livro/manual/45-aptidoes-e-refino.md')
_rodl = re.search(r'^\| com refino igual ou maior que o do dono da Expansão \| `(\d+)` \| `(\d+)` \| `(\d+)` \|$', p45, re.M)
confere('R10 a mesma tabela, no capitulo 45 do livro', [int(x) for x in _rodl.groups()] if _rodl else None,
        [int(x) for x in _rod.groups()])
_LIN = {'refino igual ou maior que o do dono, Essência `6`': (6, 0), 'o mesmo, Essência `4` ou `5`': (4, 0),
        'o mesmo, Essência até `3`': (3, 0), '`3` pontos de refino abaixo do dono, qualquer Essência': (None, 3)}
_med = dict((r, [int(x) for x in v]) for r, *v in re.findall(
    r'^\| (' + '|'.join(re.escape(k) for k in _LIN) + r') \| `(\d+)` \| `(\d+)` \| `(\d+)` \|$', p11, re.M))
if len(_med) != len(_LIN): perdida('a tabela medida do Dominio Simples na peca 11')
for rot, (ess, d) in _LIN.items():
    esss = (0, 1, 2, 3, 4, 5, 6) if ess is None else (ess,)
    calc = sorted({tuple(segura_regra(acertos(r), rodadas_ds(e, r - d, r)) for nv, r in CENARIOS) for e in esss})
    confere('R10 medido, ' + rot.replace('`', ''), [tuple(_med[rot])], calc)
if falhas: print('\n>>> A REGRESSAO FALHOU — nada abaixo vale.'); sys.exit(1)
print('>>> TUDO OK — o modelo reproduz os numeros publicados.\n')

# =========================================================================================
# O MODELO. A Expansao abre (Acerto 0) e dispara de novo no comeco de cada turno do dono:
# Acertos 0..D. O Dominio Simples sobe com Reacao quando ela abre, e segura o Acerto 0 de graca
# (decisao 2). Depois dele, cada Acerto pesa. Golpe no dono NAO derruba (obra, H §2).
# X = quantos Acertos ele aguenta depois do de abrir; o seguinte passa e ele cai.
# =========================================================================================
def X_refino(r_def, r_dono):
    """(b1) so refino: com refino igual, cai no ultimo Acerto; um ponto acima, segura tudo;
    cada ponto abaixo, um Acerto a menos. = seu refino - metade do refino do dono, para cima, menos o de abrir."""
    return max(0, r_def - ceil(r_dono / 2) - 1)
def X_corrida(r_def, r_dono, ess):
    """(b2) a metrica da corrida: cada Acerto depois do de abrir e uma falha, e ele cai com
    metade da Essencia + (seu refino - refino do dono) falhas, no minimo 1."""
    return max(1, metade_ess(ess) + r_def - r_dono) - 1
def segura(A, X, levanta=False):
    """Acertos segurados. levanta=True: sobe de novo no turno seguinte (Acao Bonus, sem recarga),
    com a conta zerada; o Acerto que o derrubou ja passou, e depois de subir de novo ele aguenta X."""
    seg, t = 1, 1
    cap = X
    while t < A:
        if cap > 0: seg += 1; cap -= 1
        elif levanta: cap = X
        else: break
        t += 1
    return seg

print('=' * 106)
print('1 · COMO CAI — refino contra refino. Acertos segurados de quantos a Expansao solta, sem subir de novo.')
print('    (b1) so refino · (b2) a metrica da corrida: metade da Essencia, mais a diferenca de refino')
print('=' * 106)
ESS = (6, 4, 2)
print(f'  {"quem defende":34s}{"":6s}' + ''.join(f'{f"nv {nv}: dono refino {r} ({acertos(r)})":>22s}' for nv, r in CENARIOS))
for rot in ('especialista', 'meio a meio', 'generalista'):
    rot_n = 'Sem Técnica sem escolher Refino' if rot == 'generalista' else rot
    linha = f'  {rot_n:34s}{"(b1)":6s}'
    for nv, r in CENARIOS:
        rd = refino_rota(rot, nv); A = acertos(r)
        linha += f'{f"{segura(A, X_refino(rd, r))}/{A} (refino {rd})":>22s}'
    print(linha)
    linha = f'  {"":34s}{"(b2)":6s}'
    for nv, r in CENARIOS:
        rd = refino_rota(rot, nv); A = acertos(r)
        linha += f'{"Ess 6/4/2: " + "/".join(str(segura(A, X_corrida(rd, r, e))) for e in ESS):>22s}'
    print(linha)
print()
print()
print('  (regra publicada) metade da Essencia (min. 1) mais uma rodada, menos um por ponto de refino do dono acima do seu:')
for rot in ('especialista', 'meio a meio', 'generalista'):
    rot_n = 'Sem Técnica sem escolher Refino' if rot == 'generalista' else rot
    linha = f'  {rot_n:34s}{"":6s}'
    for nv, r in CENARIOS:
        rd = refino_rota(rot, nv); A = acertos(r)
        linha += f'{"Ess 6/4/2: " + "/".join(str(segura_regra(A, rodadas_ds(e, rd, r))) for e in ESS):>22s}'
    print(linha)
print()
print('  Refino igual ao do dono, de ponta a ponta (b1): ' +
      ' · '.join(f'refino {r}: {segura(acertos(r), X_refino(r, r))}/{acertos(r)}' for r in range(4, 11)))
print('  O mesmo com a metade do dono para BAIXO (a formula da primeira conta): ' +
      ' · '.join(f'{r}: {min(acertos(r), max(1, r - r // 2))}/{acertos(r)}' for r in range(4, 11)))
print()
print('  O papel oposto — o inimigo (curva do meio a meio, peca 26 §3) com Simples contra o jogador especialista:')
for nv in (14, 20, 26):
    rj, ri = refino_rota('especialista', nv), refino_rota('meio a meio', nv); A = acertos(rj)
    print(f'    nv {nv}: Expansao de refino {rj} ({A} Acertos), Simples de refino {ri}: (b1) {segura(A, X_refino(ri, rj))}/{A}'
          f' · (b2) Ess 6/4/2: ' + '/'.join(str(segura(A, X_corrida(ri, rj, e))) for e in ESS)
          + ' · (regra) Ess 6/4/2: ' + '/'.join(str(segura_regra(A, rodadas_ds(e, ri, rj))) for e in ESS))
print()

print('=' * 106)
print('2 · A QUEBRA — sem recarga: sobe de novo no turno seguinte gastando a acao, e na hora da quebra a Expansao')
print('    alcanca quem ele protegia. Quantos Acertos ALCANCAM quem estava no raio, por Expansao.')
print('=' * 106)
for rot in ('especialista', 'generalista'):
    rot_n = 'Sem Técnica sem escolher Refino' if rot == 'generalista' else rot
    for nv, r in CENARIOS:
        rd = refino_rota(rot, nv); A = acertos(r)
        rg = [(A - segura_regra(A, rodadas_ds(e, rd, r)), A - segura_regra(A, rodadas_ds(e, rd, r), True)) for e in ESS]
        print(f'  {rot_n:32s} nv {nv} ({A}): Acertos que alcancam, sem subir de novo → subindo, Ess 6/4/2: '
              + ' · '.join(f'{a}→{b}' for a, b in rg))
print()
print('  A CESTA na mesma regra (um golpe por rodada em quem segura): Acertos que te alcancam, por Expansao')
def cesta_alcanca(A, p, T, regra, h=1):
    """regra 'v0.267': cai e fica caida metade da Essencia em rodadas (T), e os Acertos dessa janela passam.
    regra 'nova': na quebra a Expansao te alcanca NA HORA (um Acerto a mais), e voce sobe de novo antes
    do Acerto seguinte, com as falhas zeradas. h golpes entre um Acerto e o seguinte."""
    est = {(0, -1): 1.0}; alc = 0.0         # (falhas, ate que Acerto fica caida)
    for t in range(A):
        novo = {}
        for (f, caida), pr in est.items():
            if t <= caida:                   # caida: o Acerto t passa
                alc += pr; ch = (0, caida) if t < caida else (0, -1)
                novo[ch] = novo.get(ch, 0) + pr; continue
            novo[(f, -1)] = novo.get((f, -1), 0) + pr     # de pe: segura o Acerto t
        est = novo
        if t == A - 1: break
        for _ in range(h):                   # golpes antes do proximo Acerto
            novo = {}
            for (f, caida), pr in est.items():
                if caida != -1: novo[(f, caida)] = novo.get((f, caida), 0) + pr; continue
                ok, ruim = pr * (1 - p), pr * p
                novo[(f, -1)] = novo.get((f, -1), 0) + ok
                if f + 1 < T: novo[(f + 1, -1)] = novo.get((f + 1, -1), 0) + ruim
                elif regra == 'nova':                 # na hora; sobe de novo no seu turno, antes do Acerto seguinte
                    alc += ruim; novo[(0, t)] = novo.get((0, t), 0) + ruim     # caida pelo resto desta rodada
                else:
                    novo[(0, t + T)] = novo.get((0, t + T), 0) + ruim              # cai: Acertos t+1..t+T passam
            est = novo
    return alc
for rot, con, tr, T in PERF:
    cel = []
    for nv, r in CENARIOS:
        A = acertos(r); p = pf(con + (nivel(nv)['mae'] if tr else 0), cd_dono(nv))
        cel.append(f'nv {nv}: {cesta_alcanca(A, p, T, "v0.267"):.1f} → {cesta_alcanca(A, p, T, "nova"):.1f}'
                   f' (2 golpes: {cesta_alcanca(A, p, T, "v0.267", 2):.1f} → {cesta_alcanca(A, p, T, "nova", 2):.1f})')
    print(f'  {rot.replace("`", ""):48s} ' + ' · '.join(cel))
print()

print('=' * 106)
print('3 · O PE — um valor so. Quanto custa numa luta de 3,5 rodadas, e quantos minutos ele fica de pe fora')
print('    de combate com o dia inteiro de PE (10 rodadas por minuto). O Bastiao e o menor bolso (4 PE por nivel).')
print('=' * 106)
BOLSO = {'Bastião': 4, 'Emanador': 6}
CANDS = (('ate a v0.267: 1 × maior Classe', lambda nv: MULT_PE * nivel(nv)['cls']),
         (f'{PE_FIXO} PE, fixo (a decisao, v0.268)', lambda nv: PE_FIXO),
         ('metade da maior Classe (mín. 1)', lambda nv: max(1, nivel(nv)['cls'] // 2)),
         ('maestria', lambda nv: nivel(nv)['mae']),
         ('1 PE, fixo', lambda nv: 1))
print(f'  {"PE por rodada":34s}' + ''.join(f'{f"nv {nv}":>26s}' for nv in (10, 14, 20, 30)))
for nome, f in CANDS:
    cel = []
    for nv in (10, 14, 20, 30):
        c = f(nv); dia = BOLSO['Bastião'] * nv
        cel.append(f'{c} · luta {c * 3.5 / dia:4.0%} · {dia / c / 10:4.1f} min')
    print(f'  {nome:34s}' + ''.join(f'{x:>26s}' for x in cel))
print(f'  (o Emanador tem {BOLSO["Emanador"]} PE por nivel: os minutos dele sao {BOLSO["Emanador"] / BOLSO["Bastião"]:.1f}x os do Bastiao)')
print(f'  Na regua do projeto, 1 PE por rodada vale {PE_EM_DANO:.2f} de dano por rodada, e o deslocamento de 9 m, {DESLOC:.2f}.')
print(f'  No inimigo (peca 26 §6.5) a aptidao come a cota a {PE_EM_DANO:.2f} por PE por rodada ligada.')
print()

print('=' * 106)
print('4 · O GATE, com o voto do iniciante — o marco mais cedo em que cada rota compra o Dominio Simples')
print('=' * 106)
def primeiro_marco(seq, gate_ref, gate_nv):
    ref = 1
    for mc, e in zip(MARCOS, seq):
        ref = min(10, ref + 1)
        if e == 'R':
            ref = min(10, ref + 1)
            if mc >= gate_nv and ref >= gate_ref: return mc
    return None
GATES = (('ate a v0.267: refino 4, nível 10', 4, 10), ('refino 5, sem nível', 5, 0),
         ('com o voto: refino 4, sem nível', 4, 0), ('refino 5, nível 14', 5, 14))
print(f'  {"":38s}' + ''.join(f'{g[0]:>32s}' for g in GATES))
for nome, seq in ROTAS.items():
    print(f'  {nome:38s}' + ''.join(f'{(("nv " + str(m)) if (m := primeiro_marco(seq, gr, gn)) else "nunca, com essas escolhas"):>32s}' for _, gr, gn in GATES))
dif = sum(1 for seq in product('CRL', repeat=len(MARCOS)) if primeiro_marco(seq, 3, 10) != primeiro_marco(seq, 4, 10))
print(f'  Refino 3 contra 4 no nivel 10: em {dif} das {3 ** len(MARCOS)} sequencias de marco o marco de compra muda.')
dif5 = sum(1 for seq in product('CRL', repeat=len(MARCOS)) if primeiro_marco(seq, 4, 10) != primeiro_marco(seq, 5, 10))
print(f'  Refino 4 contra 5 no nivel 10: em {dif5} das {3 ** len(MARCOS)} ele muda.')
sem_niv = sum(1 for seq in product('CRL', repeat=len(MARCOS)) for g in (4, 5)
              if primeiro_marco(seq, g, 0) != primeiro_marco(seq, g, 10))
print(f'  Tirar o nivel 10 (decisao da v0.268): muda o marco de compra em {sem_niv} das {2 * 3 ** len(MARCOS)} combinacoes'
      f' de sequencia e gate (refino 4 e 5) — refino 4 so se alcanca no marco 10.')
print(f'  O Sem Técnica ganha o Simples na criacao, sem gate; sem escolher Refino, o refino dele chega a 5 no nivel '
      f'{min(mc for mc, v in zip(MARCOS, CURVA["generalista"]) if v >= 5)}.')

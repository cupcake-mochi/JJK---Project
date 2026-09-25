# -*- coding: utf-8 -*-
"""Rodada 2 da revisao dos anti-dominio: a Cesta Oca, opcoes 2 e 3 (24/09/2026).

CONTRATO (o que precisa continuar verdadeiro, e o script confere antes de medir):
  R1. Acerto da Expansao = Inescapavel = (pontos - Media) d8, media 4,5 por dado  (partA, partD)
  R2. A Expansao solta refino//2 + 1 Acertos: ao abrir e no comeco de cada turno do dono,
      por metade do refino em rodadas                                             (livro cap. 40)
  R3. Petala devolve refino//2 e sempre sobra um: 4->3/2, 6->4/3, 8->5/4, 10->6/5   (peca 11 §6.5)
  R4. Dominio Simples ate a v0.267: nv22 30 PE e 324 evitados; nv26 35 PE e 378  (rascunho 8.4)
  R5. Cesta ate a v0.266: 1/2/3 rodadas = 29%/57%/86% dos turnos numa luta de 3,5 (so aritmetica: a v0.267 tirou)
  R8. A tabela 'O que isso faz, medido' da Cesta, na peca 11 §6.5, sai desta conta (na v0.269 o
      teste virou o do Carregar, Espirito = Essencia; ate a v0.268 era Vigor, e a linha de Vigor
      com Constituicao 6 e Essencia 6 da o mesmo numero que a de hoje com Essencia 6)
  R6. Extensao: nv14 42 PE, nv20 72, nv26 110 para segurar ate o fim              (peca 11 §6.5)
  R7. Perfis da corrida no nv26: falha 35% / 50% / 85%                             (casca-sem-barreira)
Nada de numero digitado quando existe dono: tudo que tem ancora e lido do repositorio.
"""
import re, sys, math, os
from math import comb
R = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))) + os.sep
pa = open(R + 'manual/gerador/partA.js', encoding='utf-8').read()
p18 = open(R + 'sistema/03-mecanica/18-progressao.md', encoding='utf-8').read()
p11 = open(R + 'sistema/03-mecanica/11-aptidoes-e-refino.md', encoding='utf-8').read()

falhas = []
def confere(nome, obtido, esperado):
    ok = obtido == esperado
    print(f'  [{"x" if ok else "!"}] {nome}: {obtido}' + ('' if ok else f'  (esperado {esperado})'))
    if not ok: falhas.append(nome)

# --- tabela de Classe (partA) -----------------------------------------------------------
i0 = pa.find("TBL(['Classe', 'Nível', 'Pontos e PE', 'Leve', 'Média', 'Pesada'")
bloco = pa[i0:pa.find('),', i0)]
CL = {int(c): (int(pts), int(med)) for c, pts, med in re.findall(r"\['(\d)', '\d+', '(\d+)', '\d+', '(\d+)', '\d+'", bloco)}
def acerto_dano(classe):
    pts, med = CL[classe]
    return (pts - med) * 4.5

# --- nivel -> maestria, refino, Classe (peca 18) ----------------------------------------
NV = {}
for m in re.finditer(r'^\| \*\*(\d+)\*\* \| [^|]*\| (\d+) \| (\d+) \| (\d+) \| (\d+) \|', p18, re.M):
    NV[int(m.group(1))] = dict(mae=int(m.group(2)), esp=int(m.group(3)), ref=int(m.group(4)), cls=int(m.group(5)))
if not NV: print('ANCORA PERDIDA: tabela da peca 18'); sys.exit(1)
def nivel(n):
    k = max(x for x in NV if x <= n)
    return NV[k]

# --- ancoras de texto da peca 11 --------------------------------------------------------
for frase in ('Ela cai pelos golpes em você, e não pela Expansão', 'Soltar o símbolo não a desfaz',
              'Sempre sobra um', '`refino ÷ 2` vezes por cena', 'ela cai se você perder a concentração'):
    if frase not in p11: print('ANCORA PERDIDA na peca 11:', frase); sys.exit(1)

print('REGRESSAO — o modelo reproduz o que ja esta publicado antes de medir coisa nova')
acertos = lambda ref: ref // 2 + 1
dur = lambda ref: max(1, ref // 2)
confere('R1 Acerto Classe 6 / 7', (acerto_dano(6), acerto_dano(7)), (54.0, 63.0))
confere('R3 Petala (solta, devolve) refino 4/6/8/10',
        [(acertos(r), r // 2) for r in (4, 6, 8, 10)], [(3, 2), (4, 3), (5, 4), (6, 5)])
confere('R4 Dominio Simples nv22 (PE, evitado)', (nivel(22)['cls'] * dur(10), acertos(10) * acerto_dano(nivel(22)['cls'])), (30, 324.0))
confere('R4 Dominio Simples nv26 (PE, evitado)', (nivel(26)['cls'] * dur(10), acertos(10) * acerto_dano(nivel(26)['cls'])), (35, 378.0))
confere('R5 Cesta, turnos gastos 1/2/3 rodadas', [round(100 * r / 3.5) for r in (1, 2, 3)], [29, 57, 86])
ext = lambda nv, ref: math.ceil(1.5 * nivel(nv)['cls']) * ref
confere('R6 Extensao nv14 r7 / nv20 r9 / nv26 r10', (ext(14, 7), ext(20, 9), ext(26, 10)), (42, 72, 110))
def pf(bonus, cd):                      # igual ao casca-sem-barreira.py
    return 1 - max(0, min(20, 21 - (cd - bonus))) / 20
cd26 = 8 + 6 + nivel(26)['mae']
confere('R7 perfis nv26 (Con6 tr, Con3 tr, Con0)', tuple(round(pf(b, cd26), 2) for b in (6 + nivel(26)['mae'], 3 + nivel(26)['mae'], 0)), (0.35, 0.5, 0.85))
# R8 — a tabela da peca 11 (v0.269): golpe no dono, 1 golpe por rodada, T = metade da Essencia,
# o teste do Carregar (Espirito, que e Essencia + maestria se treinado)
def _seg(nv, ref, bonus, T):
    A = ref // 2 + 1; cd = 8 + 6 + nivel(nv)['mae']; p = pf(bonus, cd)
    return round(sum(sum(comb((j - 1), f) * p**f * (1 - p)**((j - 1) - f) for f in range(min(T, j))) for j in range(1, A + 1)), 1)
_pub = re.findall(r'^\| (Espírito treinado, Essência `6`|Espírito treinado, Essência `4`|sem treino, Essência `2`) \| `([\d,]+)` \| `([\d,]+)` \| `([\d,]+)` \|$', p11, re.M)
if len(_pub) != 3: print('ANCORA PERDIDA: a tabela medida da Cesta na peca 11'); sys.exit(1)
_perf = {'Espírito treinado, Essência `6`': (6, True, 3), 'Espírito treinado, Essência `4`': (4, True, 2), 'sem treino, Essência `2`': (2, False, 1)}
for rot, *vals in _pub:
    ess, tr, T = _perf[rot]
    calc = [_seg(nv, ref, ess + (nivel(nv)['mae'] if tr else 0), T) for nv, ref in ((14, 5), (20, 7), (26, 10))]
    confere(f'R8 peca 11, {rot.split(",")[0]} Ess {ess} (T={T})', [float(v.replace(',', '.')) for v in vals], calc)
if falhas:
    print('\n>>> A REGRESSAO FALHOU — nada abaixo vale.'); sys.exit(1)
print('>>> TUDO OK — o modelo reproduz os numeros publicados, e a tabela da Cesta na peca 11.\n')

# --- o cenario ---------------------------------------------------------------------------
# a Expansao abre (Acerto 1) e dispara de novo no comeco de cada turno do dono, por dur rodadas.
# entre um Acerto e o seguinte, quem segura a Cesta toma h golpes (0, 1 ou 2 por rodada).
CENARIOS = ((14, 5), (20, 7), (26, 10))     # (nivel, refino do dono da Expansao)
def perfis(nv):
    m = nivel(nv)['mae']
    return (('Con 6 treinado', 6 + m), ('Con 3 treinado', 3 + m), ('Con 0 sem treino', 0))
def limite(ess): return max(1, ess // 2)   # a mesma regra da corrida (peca 1 §5.4)

def binom_menor(n, p, T):               # P(falhas em n testes < T)
    return sum(comb(n, f) * p**f * (1 - p)**(n - f) for f in range(min(T, n + 1)))

def seguros(A, p, T, h, pelo_acerto, fixo=None):
    """Acertos que a Cesta segura, em media, e a chance de segurar todos.
    h golpes no dono entre um Acerto e o seguinte (golpe no dono, obra 266);
    pelo_acerto: cada Acerto segurado tambem pede um teste (pressao do dominio, obra 266 'um dia sempre perde');
    a falha de numero T desfaz a Cesta, e o Acerto daquela hora passa."""
    if fixo is not None:
        return min(fixo, A), 1.0 if fixo >= A else 0.0
    tot, ult = 0.0, 0.0
    for j in range(1, A + 1):           # antes do Acerto j: (j-1)*h testes de golpe; no Acerto j: 1 teste se pelo_acerto
        n = (j - 1) * h + (j if pelo_acerto else 0)
        pr = binom_menor(n, p, T)
        tot += pr; ult = pr
    return tot, ult

print('=' * 100)
print('COMO ESTAVAM ANTES DA REVISAO — a Cesta ate a v0.266, o Simples ate a v0.267: como caiam, quanto duravam')
print('=' * 100)
for nv, ref in CENARIOS:
    A, D, cls, dmg = acertos(ref), dur(ref), nivel(nv)['cls'], acerto_dano(nivel(nv)['cls'])
    rf = nivel(nv)['ref']
    print(f'nv {nv}: Expansao de refino {ref} solta {A} Acertos de {dmg:.0f} ({A*dmg:.0f} no total) em {D} rodada(s); quem defende tem refino ~{rf}, Classe {cls}')
    print(f'  Cesta Oca     segura {A}/{A} · nao cai · custa {D} rodada(s) de turno = {min(100, round(100*D/3.5))}% da luta · 0 PE')
    print(f'  Dom. Simples  segura {A}/{A} no raio, pra todo mundo · cai se os pes sairem do chao · {cls*D} PE')
    pet = min(rf // 2, A - 1) if rf >= 4 else 0
    print(f'  Petala        segura {pet}/{A} (refino {rf} -> {rf//2}, sempre sobra um) · cai na 1a falha de concentracao · {cls*D} PE')
    print(f'  Extensao      segura {A}/{A} · dura {rf} rodadas · {math.ceil(1.5*cls)*D} PE e sem tecnica enquanto de pe' + ('' if rf >= 7 else ' · (gate refino 7: ainda nao tem)'))
print()

print('=' * 100)
print('OPCAO 3 — a Cesta que CAI: quantos Acertos ela segura, em media (e a chance de segurar todos)')
print('  A = a obra 266, golpe no dono: cada golpe que ele toma e um teste de Vigor; T falhas desfazem')
print('  B = a obra 266, pressao: cada Acerto segurado e um teste de Vigor contra a CD do dono da Expansao')
print('  T = falhas que desfazem: 1 (como a concentracao) ou metade da Essencia (como a corrida)')
print('=' * 100)
for nv, ref in CENARIOS:
    A = acertos(ref); cd = 8 + 6 + nivel(nv)['mae']
    print(f'\nnv {nv} · Expansao refino {ref} · {A} Acertos · CD do dono {cd}')
    print(f'  {"perfil":18s} {"":10s}' + ''.join(f'{c:>16s}' for c in ('A, 1 golpe/rod', 'A, 2 golpes/rod', 'B, so pressao', 'A+B, 1 golpe')))
    for rot, b in perfis(nv):
        p = pf(b, cd)
        for T, tr in ((1, 'T=1'), (2, 'T=2 (Ess 4)'), (3, 'T=3 (Ess 6)')):
            cel = []
            for h, pa_ in ((1, False), (2, False), (0, True), (1, True)):
                m, tudo = seguros(A, p, T, h, pa_)
                cel.append(f'{m:4.1f}/{A} ({tudo:4.0%})')
            print(f'  {rot:18s} {tr:10s}' + ''.join(f'{c:>16s}' for c in cel))
    print(f'  {"fixo, segura 2":29s}' + f'{min(2,A):>11d}/{A}' + f'   · fixo, segura 3: {min(3,A)}/{A}')
print()
print('(o primeiro Acerto sempre sai ao abrir, antes de qualquer golpe; por isso "A" nunca desce de 1)')

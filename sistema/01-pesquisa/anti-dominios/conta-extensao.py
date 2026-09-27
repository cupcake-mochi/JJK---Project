# -*- coding: utf-8 -*-
"""Rodada 3 da revisao dos anti-dominio: a Extensao de Dominio (26/09/2026).

Irmao do conta-cesta-oca.py, do conta-dominio-simples.py e do conta-petala.py, com o mesmo
contrato: a regressao reproduz o que ja esta publicado ANTES de medir coisa nova, e todo
numero que tem dono e lido do dono.

REGRESSAO
  R1. A tabela da Extensao na peca 11 §6.5 (nv, refino, duracao, PE/rodada, erguer e segurar ate o
      fim, do dia de um Bastiao), com o PE por rodada = 1,5 x maior Classe arredondado para cima e,
      desde a v0.273, erguer = a maior Classe (ate a v0.272 a coluna nao tinha erguer: 42/72/110)
  R2. O teto do que encosta: 1/3 do refino + 1 — 3 no gate (refino 7) e 4 no refino 10
  R3. A linha da Extensao na peca 26 §6.5 no nivel 30 (ali o 1,5 x Classe entra sem arredondar, e
      erguer entra repartido pelas 3 rodadas da luta) — ate a v0.272, sem erguer, eram 98% e 27%
  R4. O dano do chefe por rodada (manual, a tabela Inimigos) e as tres acoes dele (peca 19)

AS DECISOES DO MIZUKI (26/09/2026, rodada 3): erguer custa a maior Classe, toda vez; contra o acerto
garantido ela anula sempre, e "uma pessoa que utilizar uma extensao de dominio e imune a todos os
efeitos da expansao", em qualquer degrau ("imune a efeitos de expansao incompleta e sem barreiras
tambem"); a tecnica acima do teto "reduzindo 1/4 do dano tomado, sobrando 3/4" (o "voce leva 1/4"
de uma volta antes era da Petala); nao cai por golpe ("so sai cara mesmo"); levanta como as outras;
nivel 18, e o requisito "ver alguem usando ou estudando (alguem ensinando serve tambem)".
"""
import re, sys, os, math
R = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))) + os.sep
def ler(c): return open(R + c, encoding='utf-8').read()
p11, p18, p26 = ler('sistema/03-mecanica/11-aptidoes-e-refino.md'), ler('sistema/03-mecanica/18-progressao.md'), ler('sistema/03-mecanica/26-bestiario.md')
pF, p05, pA = ler('manual/gerador/partF.js'), ler('sistema/03-mecanica/05-caminho-e-combate-sem-feitico.md'), ler('manual/gerador/partA.js')
falhas = []
def confere(nome, obtido, esperado):
    ok = obtido == esperado
    print(f'  [{"x" if ok else "!"}] {nome}: {obtido}' + ('' if ok else f'  (esperado {esperado})'))
    if not ok: falhas.append(nome)
def perdida(o): print('ANCORA PERDIDA:', o); sys.exit(1)

NV = {int(m.group(1)): dict(mae=int(m.group(2)), ref=int(m.group(4)), cls=int(m.group(5)))
      for m in re.finditer(r'^\| \*\*(\d+)\*\* \| [^|]*\| (\d+) \| (\d+) \| (\d+) \| (\d+) \|', p18, re.M)}
def nivel(n): return NV[max(x for x in NV if x <= n)]
BOLSO = 4                                              # o Bastiao (peca 6), o mesmo dos outros scripts
m_pe = re.search(r'recuperar `\+1` PE \| permanente \| `(\d+),(\d+)`', p05)
if not m_pe: perdida('o cambio de PE da peca 5 §4')
CAMBIO = float(m_pe.group(1) + '.' + m_pe.group(2))
i0 = pF.find("TBL(['Nível do grupo', 'Dano do grupo por rodada', 'Chefe sozinho: vida', 'Chefe: dano'")
if i0 < 0: perdida('a tabela Inimigos do manual')
CHEFE = {int(n): int(d) for n, d in re.findall(r"\['(\d+)', '~\d+', '[\d a]+', '(\d+)'", pF[i0:pF.find(')', pF.find('],\n    [', i0))])}
i1 = pA.find("TBL(['Classe', 'Nível', 'Pontos e PE', 'Leve', 'Média', 'Pesada'")
CL = {int(c): (int(p), int(m)) for c, p, m in re.findall(r"\['(\d)', '\d+', '(\d+)', '\d+', '(\d+)', '\d+'", pA[i1:pA.find('),', i1)])}

print('REGRESSAO — o modelo reproduz o que ja esta publicado antes de medir coisa nova')
pe_rod = lambda nv: math.ceil(1.5 * nivel(nv)['cls'])
tab = [tuple(int(x) for x in t) for t in re.findall(r'^\| (\d+) \| (\d+) \| (\d+) \| (\d+) \| (\d+) \| \**(\d+)%\** \|$', p11, re.M)]
confere('R1 a tabela da Extensao na peca 11 (nv, refino, duracao, PE, erguer e ate o fim, % do dia)', tab,
        [(n, r, r, pe_rod(n), nivel(n)['cls'] + pe_rod(n) * r, round(100 * (nivel(n)['cls'] + pe_rod(n) * r) / (BOLSO * n)))
         for n, r, *_ in tab] if tab else ['a tabela'])
confere('R2 o teto do que encosta no refino 7 e 10', (7 // 3 + 1, 10 // 3 + 1), (3, 4))
m26 = re.search(r'^\| `Extensão de Domínio` · erguer, e `1,5 ×` maior Classe \| `(\d+)%` \| `(\d+)%` \|$', p26, re.M)
m_fi = re.search(r'multiplicado por `(\d),(\d+)`', p26)
if not m_fi: perdida('o fator da Intervencao na peca 26')
FI = float(m_fi.group(1) + '.' + m_fi.group(2))
COTA = {'Ameaça': 55, 'Desastre': 219 * FI}             # a cota do nivel 30 como a 9.2 le: o Desastre carrega Intervencao
confere('R3 a Extensao na peca 26 (Ameaca, Desastre), nv 30', tuple(int(x) for x in m26.groups()) if m26 else None,
        tuple(round(100 * (1.5 * nivel(30)['cls'] + nivel(30)['cls'] / 3) * CAMBIO / COTA[c]) for c in ('Ameaça', 'Desastre')))
confere('R4 o dano do chefe por rodada nos niveis 10/20/30', [CHEFE[n] for n in (10, 20, 30)], [75, 147, 219])
if falhas: print('\n>>> A REGRESSAO FALHOU — nada abaixo vale.'); sys.exit(1)
print('>>> TUDO OK — o modelo reproduz os numeros publicados.\n')

print('=' * 104)
print('1 · ERGUER CUSTANDO A MAIOR CLASSE — segurar ate o fim (erguer uma vez + refino rodadas), no dia do Bastiao')
print('=' * 104)
for n, r, *_ in tab:
    hoje = pe_rod(n) * r; novo = hoje + nivel(n)['cls']
    print(f'  nv {n}: refino {r}, {pe_rod(n)} PE/rodada · hoje {hoje} PE = {hoje / (BOLSO * n):.0%} · erguendo {novo} PE = {novo / (BOLSO * n):.0%}'
          f' · uma luta de 3,5 rodadas: {nivel(n)["cls"] + pe_rod(n) * 3.5:g} PE = {(nivel(n)["cls"] + pe_rod(n) * 3.5) / (BOLSO * n):.0%}')
print()
print('=' * 104)
print('2 · O QUE O "REDUZ 1/4" DA — o chefe bate por feiticos acima do teto; quanto dano a Extensao evita por')
print('    rodada em quem a usa, e quanto isso vale em PE (1 PE por rodada = 5,14 de dano por rodada, peca 5 §4)')
print('=' * 104)
for n in (14, 20, 26, 30):
    ch = CHEFE[max(k for k in CHEFE if k <= n)]
    for quem, frac in (('um alvo de quatro', 0.25), ('o alvo que o chefe escolheu', 1.0)):
        chega = ch * frac; evita = chega * 0.25
        print(f'  nv {n}: {quem:28s} leva {chega:5.1f} por rodada; a Extensao evita {evita:5.1f} = {evita / CAMBIO:4.1f} PE por rodada'
              f' (ela custa {pe_rod(n)})')
print('  (abaixo do teto ela anula tudo; o golpe de arma do chefe, que nao e tecnica, passa inteiro)')
print('  Registro — se acima do teto ela deixasse voce levar so 1/4 (a leitura que o Mizuki corrigiu), com o chefe')
print('  batendo so nela: ' + ' · '.join(f'nv {n}: {CHEFE[max(k for k in CHEFE if k <= n)] * 0.75 / CAMBIO:.1f} PE (custa {pe_rod(n)})' for n in (14, 20, 26, 30)))
print()
print('=' * 104)
print('3 · NO INIMIGO (peca 26 §6.5): a Extensao com erguer, na cota do nivel 30 — a Classe repartida pelas 3 rodadas')
print('=' * 104)
for nome, custo in (('hoje, 1,5 x Classe', 1.5 * nivel(30)['cls']), ('com erguer', 1.5 * nivel(30)['cls'] + nivel(30)['cls'] / 3)):
    print(f'  {nome:20s} ' + ' · '.join(f'{c} {custo * CAMBIO / COTA[c]:.0%}' for c in COTA))
print()
print('=' * 104)
print('4 · QUEM A EXTENSAO CUSTA MAIS — o dano por rodada que a ficha perde enquanto ela esta de pe. Quem conjura')
print('    (Fundamento, e o Sem Tecnica com o Manejo, que "e o feitico com outro nome") cai para o golpe de arma; o')
print('    Corpo Amaldicoado, com a Tecnica Marcial liberada, nao perde nada. Em PE por rodada, a 5,14.')
print('=' * 104)
ARMA = {int(n): float(a + '.' + b) for n, _, a, b in re.findall(r'^\| (\d+) \| (\d+) \| (\d+),(\d) \| [\d,]+× \|$', p05, re.M)}
ROT = {1: 13, 2: 31, 3: 45, 4: 63, 5: 76, 6: 94, 7: 108}
mrot = re.findall(r"\['(\d+) a (\d+)', '(\d)', '[^']*= (\d+)'", pF)
if mrot: ROT = {int(c): int(r) for _, _, c, r in mrot}
for n in (14, 20, 30):
    arma = ARMA[max(k for k in ARMA if k <= n)] * 2        # dois golpes do nivel 7 em diante (peca 6 §3.1)
    perde = ROT[nivel(n)['cls']] - arma
    print(f'  nv {n}: a Rotina e {ROT[nivel(n)["cls"]]}, dois golpes de arma dao {arma:g} — quem conjura perde {perde:g} por rodada'
          f' = {perde / CAMBIO:.1f} PE, alem dos {pe_rod(n)} que ela custa; o Corpo Amaldicoado perde 0')

print()
print('=' * 104)
print('5 · O NIVEL 18 — em quantas ordens de marco a compra muda, contra o nivel 14 da Classe Passiva 3 (peca 11 §5)')
print('=' * 104)
from itertools import product
cab = re.search(r'^\| \| (nv \d+(?: \| nv \d+)+) \|$', p11, re.M)
MARCOS = [int(x) for x in re.findall(r'nv (\d+)', cab.group(1))]
def primeiro_marco(seq, gr, gn):
    ref = 1
    for mc, e in zip(MARCOS, seq):
        ref = min(10, ref + 1)
        if e == 'R':
            ref = min(10, ref + 1)
            if mc >= gn and ref >= gr: return mc
    return None
todas = list(product('CRL', repeat=len(MARCOS)))
muda = [s_ for s_ in todas if primeiro_marco(s_, 7, 14) != primeiro_marco(s_, 7, 18)]
nunca = [s_ for s_ in muda if primeiro_marco(s_, 7, 18) is None]
print(f'  a compra muda em {len(muda)} das {len(todas)} ordens, e em {len(nunca)} delas a pessoa nunca chega a comprar')

# --- R5: o que a v0.273 publicou sai deste modelo -----------------------------------------------
print()
print('REGRESSAO DO QUE A v0.273 PUBLICOU (peca 11 §6.5 e peca 26 §6.5)')
m = re.search(r'Numa luta normal de 3,5 rodadas, erguendo uma vez, ela custa de `(\d+)%` a `(\d+)%` do dia', p11)
lutas = [(nivel(n)['cls'] + pe_rod(n) * 3.5) / (BOLSO * n) for n, *_ in tab]
confere('R5 uma luta de 3,5 rodadas, erguendo uma vez (min, max do dia)', tuple(int(x) for x in m.groups()) if m else None,
        (round(100 * min(lutas)), round(100 * max(lutas))))
m = re.search(r'quem conjura perde de `([\d,]+)` a `([\d,]+)` PE por rodada em dano', p11)
perde = [(ROT[nivel(n)['cls']] - ARMA[max(k for k in ARMA if k <= n)] * 2) / CAMBIO for n in (14, 20, 30)]
confere('R5 o que quem conjura perde com ela de pe (nv 14 e 30)', tuple(float(x.replace(',', '.')) for x in m.groups()) if m else None,
        (round(perde[0], 1), round(perde[-1], 1)))
m = re.search(r'em `(\d+)` das `([\d.]+)` ordens de marco a compra atrasa, e em `(\d+)` delas', p11)
confere('R5 o nivel 18 (muda, de quantas, nunca)', (int(m.group(1)), int(m.group(2).replace('.', '')), int(m.group(3))) if m else None,
        (len(muda), len(todas), len(nunca)))
foco = [(CHEFE[max(k for k in CHEFE if k <= n)] * 0.25 / CAMBIO, pe_rod(n)) for n in (14, 20, 26, 30)]
confere('R5 "a reducao vale no maximo o PE que ela custa por rodada", com o chefe batendo so nela',
        all(v <= c for v, c in foco), True)
m = re.search(r'custa `(\d+)%` da cota de uma `Ameaça`, e por isso uma maldição daquele nível que a carregue tem de ser pelo menos um `Desastre`\*\* — \*lá ela cai para `(\d+)%`', p26)
c2 = (1.5 * 1 + 1 / 3) * CAMBIO
def meio_baixo(x): return math.ceil(x - 0.5)      # o arredondamento da cota na 9.2 do conferir-bestiario
confere('R5 a Extensao no nivel 2, com erguer (Ameaca, Desastre)', tuple(int(x) for x in m.groups()) if m else None,
        (round(100 * c2 / meio_baixo(CHEFE[2] * 0.25)), round(100 * c2 / (meio_baixo(CHEFE[2] * 1) * FI))))
if falhas: print('\n>>> A REGRESSAO DA v0.273 FALHOU.'); sys.exit(1)
print('>>> TUDO OK — a regra publicada na v0.273 sai deste modelo.')

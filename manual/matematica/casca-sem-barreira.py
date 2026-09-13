# -*- coding: utf-8 -*-
"""Rascunho da Expansao sem Barreiras, secao 7.4 (12/09/2026).

A corrida da casca contra a corrida da concentracao. Nenhum numero digitado.
"""
# A corrida da casca contra a corrida da concentração. Donos: manual partA (pontos e Média por
# Classe), partD (Inescapável = Média, sem outra peça), livro cap. 40 (casca por fora = 50 × metade
# do refino; Acerto ao abrir e no começo de cada turno), peça 3 (concentração = TR Vigor), peça 1
# (CD = 8 + atributo + maestria), peça 18 (maestria e maior Classe por nível).
import re, math, sys
import os
R = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) + os.sep
pa = open(R + 'manual/gerador/partA.js', encoding='utf-8').read()
pd = open(R + 'manual/gerador/partD.js', encoding='utf-8').read()
lv = open(R + 'sistema/05-material/livro/manual/40-fundamento.md', encoding='utf-8').read()
def anc(p, t, o):
    m = re.search(p, t, re.M)
    if not m: print('ANCORA PERDIDA:', o); sys.exit(1)
    return m
i0 = pa.find("TBL(['Classe', 'Nível', 'Pontos e PE', 'Leve', 'Média', 'Pesada'")
if i0 < 0: print('ANCORA PERDIDA: a tabela de Classe no partA'); sys.exit(1)
bloco = pa[i0:pa.find('),', i0)]
CL = {int(c): (int(pts), int(med)) for c, pts, med in re.findall(r"\['(\d)', '\d+', '(\d+)', '\d+', '(\d+)', '\d+'", bloco)}
if sorted(CL) != [1, 2, 3, 4, 5, 6, 7] or CL[7] != (21, 7): print('A TABELA DE CLASSE NAO BATE:', CL); sys.exit(1)
anc(r"\['Inescapável', 'Média', 'Sem acerto e sem Teste de Resistência", pd, 'Inescapável no partD')
m = anc(r'Por fora ela tem (\d+) × metade do refino de vida', lv, 'a casca no livro')
K = int(m.group(1))
anc(r'O Acerto acontece no momento em que você abre\*\*, e de novo no começo de cada turno seu', lv, 'o ritmo do Acerto no livro')

print('O ACERTO LETAL, pela régua do Inescapável (pontos − Média, o resto vira d8 de 4,5)')
for c in (5, 6, 7):
    pts, med = CL[c]
    d = pts - med
    print(f'  Classe {c}: {pts} pontos − {med} da Média = {d}d8, média {d*4.5:.0f} por Acerto')
print()
print(f'A CASCA POR FORA: {K} × metade do refino')
for ref in (5, 7, 10):
    print(f'  refino {ref}: {K*(ref//2)} de vida')
print()
print('QUANTOS ACERTOS a casca aguenta (o primeiro sai ao abrir, os outros no começo de cada turno do dono)')
print(f'  {"":22s}' + ''.join(f'refino {r:<5d}' for r in (5, 7, 10)))
for c in (6, 7):
    dmg = (CL[c][0] - CL[c][1]) * 4.5
    print(f'  Acerto de Classe {c} ({dmg:.0f}) ' + ''.join(f'{math.ceil(K*(r//2)/dmg):<12d}' for r in (5, 7, 10)))
print('  -> "1" quer dizer que cai ao abrir; "4" quer dizer abrir e mais três turnos do dono')
print()
print('A CONCENTRAÇÃO: cada golpe no dono durante a corrida é um TR de Vigor contra a CD do rival')
def pf(bonus, cd):
    return 1 - max(0, min(20, 21 - (cd - bonus))) / 20
for nv, mae in ((22, 3), (26, 4)):
    cd = 8 + 6 + mae
    print(f'  nível {nv}, CD do rival {cd}:')
    for rot, b in (('Con 6, treinado', 6 + mae), ('Con 3, treinado', 3 + mae), ('Con 0, sem treino', 0)):
        f = pf(b, cd)
        print(f'    {rot:18s} falha {f:4.0%} por golpe · segura a rodada contra 1 golpe {1-f:4.0%}, contra 3 golpes {(1-f)**3:4.0%}'
              f' · golpes até cair, em média {1/f:.1f}')

# ---------------------------------------------------------------------------
# 13/09/2026 — a regra do Mizuki para a concentração na corrida (rascunho §7.5):
#   o jogador na corrida testa a cada dano, sem limite; o inimigo, no máximo um
#   teste por jogador que ataca ele; as falhas acumulam, e a expansão cai quando
#   elas chegam a metade da Essência.
# ---------------------------------------------------------------------------
from math import comb
p1 = open(R + 'sistema/03-mecanica/01-atributos-acerto-defesa.md', encoding='utf-8').read()
p26 = open(R + 'sistema/03-mecanica/26-bestiario.md', encoding='utf-8').read()
anc(r'O que você \*\*ganha\*\* desce\. E o que você ganha nunca fica abaixo de 1\.', p1, 'o arredondamento da peça 1 §5.4')
anc(r'\*\*Dura metade do refino em rodadas\*\*, no mínimo uma', lv, 'a duração no livro')
anc(r'no máximo uma por rodada, logo depois do turno de outra criatura', p26, 'as Intervenções, uma por rodada, peça 26')
CAT = {}
for nome, pes, ac in re.findall(r'^\| \*\*`(Desastre|Catástrofe|Calamidade)`\*\* \| (\d+) \| `× [\d,]+` \| `(\d+)` \|', p26, re.M):
    CAT[nome] = (int(pes), int(ac))
if len(CAT) != 3: print('ANCORA PERDIDA: a tabela de categorias da peça 26 §4', CAT); sys.exit(1)

def limite(ess):                      # o que o dono ganha desce, e nunca fica abaixo de 1
    return max(1, ess // 2)

def de_pe(testes, p, T):              # chance de ainda estar de pé depois de `testes` testes
    return sum(comb(testes, f) * p**f * (1-p)**(testes-f) for f in range(min(T, testes + 1)))

DUR = 10 // 2
PERFIS = (('Con 6, treinado', 0.35), ('Con 3, treinado', 0.50), ('Con 0, sem treino', 0.85))

print()
print('=' * 92)
print('A REGRA DE 13/09: falhas acumulam até metade da Essência (arredonda para baixo, mínimo 1)')
print('=' * 92)
print('Essência -> falhas que derrubam: ' + '  '.join(f'{e}->{limite(e)}' for e in range(7)))
print(f'duração da corrida com refino 10: {DUR} rodadas · a casca de refino 10 cai no 4º Acerto letal')
print()

def tabela(titulo, testes_por_rodada, cap_total=None):
    print(titulo)
    print(f'  {"":20s}' + ''.join(f'Ess {e} ({limite(e)} falha{"s" if limite(e)>1 else ""})'.ljust(22) for e in (2, 4, 6)))
    for rot, p in PERFIS:
        cel = []
        for e in (2, 4, 6):
            T = limite(e)
            vivo = [de_pe(min(testes_por_rodada * r, cap_total) if cap_total else testes_por_rodada * r, p, T) for r in range(1, DUR + 1)]
            cai = next((r for r, v in zip(range(1, DUR + 1), vivo) if v < 0.5), None)
            cel.append((f'cai na rodada {cai}' if cai else 'aguenta as 5') + f' ({vivo[-1]:.0%} no fim)')
        print(f'  {rot:20s}' + ''.join(c.ljust(22) for c in cel))
    print()

for nome, (pes, ac) in CAT.items():
    print(f'--- {nome}: {pes} jogadores, {ac} ações do inimigo por rodada, mais 1 Intervenção por rodada ---')
    tabela(f'  JOGADOR dono do domínio, levando todas as {ac + 1} ações na rodada (um teste por dano, sem limite):', ac + 1)
    tabela(f'  INIMIGO dono, UM teste por jogador POR RODADA ({pes} testes por rodada):', pes)
    tabela(f'  INIMIGO dono, UM teste por jogador NA CORRIDA INTEIRA (no máximo {pes} testes):', pes, cap_total=pes)

print('=' * 92)
print('SENSIBILIDADE: o jogador dono, se o chefe NÃO concentra tudo nele (1 e 2 danos por rodada)')
print('=' * 92)
print('chance de o domínio ainda estar de pé no fim de cada rodada, Essência 6 (3 falhas)')
print(f'  {"":24s}{"r1":>6s}{"r2":>6s}{"r3":>6s}{"r4":>6s}{"r5":>6s}')
for danos in (1, 2):
    for rot, p in PERFIS:
        print(f'  {danos} dano/rodada, {rot:17s}' + ''.join(f'{de_pe(danos*r, p, 3):6.0%}' for r in range(1, DUR + 1)))
print()
print('a mesma coisa com Essência 2 (1 falha — igual à regra antiga de uma falha só)')
for danos in (1, 2):
    for rot, p in PERFIS:
        print(f'  {danos} dano/rodada, {rot:17s}' + ''.join(f'{de_pe(danos*r, p, 1):6.0%}' for r in range(1, DUR + 1)))

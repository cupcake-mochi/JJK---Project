# -*- coding: utf-8 -*-
"""Piloto da medicao da colecao v0.4 (item 12 da fila): o Bastiao, entrega por entrega, em fatias.

Pedido do Mizuki em 27/09/2026 ("2 - A"): um piloto com o Bastiao, sem agente, que traz o metodo, os
numeros e as duas pendencias que a propria v0.4 deixou (o Oportunista e o Contra a Parede) medidas.

O CONTRATO dos scripts de conta do projeto: a regressao reproduz o que ja esta publicado antes de medir,
e todo numero que tem dono e lido do dono. Aqui os donos sao a peca 5 §4 (a fatia, a regua de conversao),
o manual (a tabela de Classe e a do Classe 0), o DESENHO-trilhas.md (as linhas de preco da colecao
anterior que as entregas novas repetem) e a peca 1 (acerto e falha de TR de hoje).

O QUE E CONVENCAO NOVA, e esta escrito como tal: o piloto precisa de numeros que nenhum documento tem —
quantos golpes o Bastiao assume por Olhos Em Mim numa rodada, quanto tempo ele passa com metade da vida ou
menos, quantos inimigos cabem na area dele. Cada um entra com um valor BAIXO e um ALTO, e a tabela sai em
faixa. As convencoes sao do Mizuki para decidir; este script nao escolhe.

AS RESPOSTAS DELE, na v0.280, depois do piloto: o Contra a Parede nao custa PE, o feitiço e de metade da
maior Classe arredondada para baixo, se paga normalmente, vem depois do primeiro golpe e nao crita (a
linha "pagando o PE" daqui, e nao a "de graca" que a tabela das Trilhas soma); o Oportunista vale um
ataque ou um alvo, ate o fim do proximo turno;
e o Combatente Amaldicoado fica como esta: "N acho q os valores atuais estao corretos, sendo franco, voce
esta calculando cogitando muitas coisas, n precisa tanto". Os numeros abaixo ficam como o registro do
piloto, e nenhum numero publicado saiu daqui.
"""
import re, sys, os
R = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))) + os.sep
def ler(c): return open(R + c, encoding='utf-8').read()
p05, dtr, pa = ler('sistema/03-mecanica/05-caminho-e-combate-sem-feitico.md'), ler('DESENHO-trilhas.md'), ler('manual/gerador/partA.js')
p19, dca = ler('sistema/03-mecanica/19-dano-e-condicoes.md'), ler('DESENHO-caminhos.md')
v04 = ler('caminhos/01-Caminhos-e-Trilhas/01-Bastiao-Caminho-e-Trilhas.md')
falhas = []
def confere(nome, obtido, esperado):
    ok = obtido == esperado
    print(f'  [{"x" if ok else "!"}] {nome}: {obtido}' + ('' if ok else f'  (esperado {esperado})'))
    if not ok: falhas.append(nome)
def perdida(o): print('ANCORA PERDIDA:', o); sys.exit(1)
def n(s): return float(s.replace(',', '.'))
def pega(txt, rx, nome):
    m = re.search(rx, txt, re.M)
    if not m: perdida(nome)
    return m

# --- os donos -------------------------------------------------------------------------------------
FATIA = n(pega(p05, r'A fatia é `(\d+,\d+)` de dano por rodada', 'a fatia na peca 5 §4').group(1))
m = pega(p05, r'o soco no nível 30 — `d10 \+ Força 6` \| permanente \| `(\d+,\d+)`', 'o soco da peca 5 §4'); SOCO = n(m.group(1))
m = pega(p05, r'mover-se `\+1,5 m` \| permanente \| `(\d+,\d+)`', 'posicionamento +1,5 m'); POS15 = n(m.group(1))
m = pega(p05, r'`\+1` de Defesa \| permanente \| `(\d+,\d+)`', '+1 de Defesa permanente'); DEF1 = n(m.group(1))
m = pega(p05, r'recuperar `\+1` PE \| permanente \| `(\d+,\d+)`', 'recuperar +1 PE'); PE = n(m.group(1))
m = pega(dtr, r'Com o acerto em `(\d+)%`, dois ataques dão `(\d+,\d+)%`; e a falha de TR virou `(\d+)%`', 'o acerto e a falha de TR de hoje (v0.119)')
ACERTO, DOIS, FALHA_TR = int(m.group(1)) / 100, n(m.group(2)) / 100, int(m.group(3)) / 100
DERRUBADO = n(pega(p19, r'^\| \*\*`Derrubado`\*\* \| `(\d+,\d+)` \|', 'o Derrubado da peca 19').group(1))
TIPOS = {int(q): n(v) for q, v in re.findall(r'^\| \**(\d)\** \| \d+% \| \**(\d+,\d+)\** \|$', dtr, re.M)}
i0 = pa.find("TBL(['Classe', 'Nível', 'Pontos e PE', 'Leve', 'Média', 'Pesada'")
CLASSE = {int(c): int(d) for c, d in re.findall(r"\['(\d)', '\d+', '\d+', '\d+', '\d+', '\d+', '\d+', '\+\d', '\d+', '\d+d8 = (\d+)'\]", pa[i0:pa.find('),', i0)])}
m0 = pega(pa, r"\['Dano', '2d8', '3d8', '4d8', '5d8', '(\d)d8'\]", 'o dano do Classe 0 no nivel 25 em diante')
CLASSE0 = int(m0.group(1)) * 4.5
PE_POR_CLASSE = int(pega(pa, r'Conjurar um feitiço custa \*\*(\d) × Classe\*\* de PE', 'o custo de conjurar').group(1))
m = pega(dtr, r'O Bastião tem `(\d+)` de PE no nível 30 e um Classe 7 custa `(\d+)`: são `(\d+,\d+)` conjurações num dia de `(\d+)` rodadas', 'o dia de conjuracao do Bastiao')
PE_DIA, CONJ_DIA, DIA_RODADAS = int(m.group(1)), n(m.group(3)), int(m.group(4))
DIA_ABSORVER = n(pega(dca, r'O dia tem `(\d+,\d+)` rodadas de luta', 'o dia de luta do DESENHO-caminhos').group(1))
VANT = (1 - (1 - ACERTO) ** 2) - ACERTO           # o ganho da vantagem, no acerto de hoje

print('REGRESSAO — as linhas da colecao anterior que as entregas novas repetem')
confere('a fatia (peca 5 §4)', FATIA, 5.08)
confere('o soco no nivel 30, e disparado por "quando voce acerta" com dois ataques a 75% (o Engate, 1,70)',
        (SOCO, round(SOCO * 0.75 / FATIA, 2)), (11.5, 1.7))
confere('o Derrubado do Encontrao na v0.103: 8,45 x 75% x 45% (0,56)', round(DERRUBADO * 0.75 * 0.45 / FATIA, 2), 0.56)
confere('resistencia a 2 e a 4 tipos (o Alicerce e a Cupula)', (TIPOS.get(2), TIPOS.get(4)), (1.33, 2.17))
confere('o Classe 0 no nivel 30, e as Classes 3, 4 e 7 (manual)', (CLASSE0, CLASSE[3], CLASSE[4], CLASSE[7]), (27.0, 40, 54, 94))
confere('o acerto, dois ataques e a falha de TR de hoje (v0.119)', (ACERTO, DOIS, FALHA_TR), (0.55, 0.7975, 0.35))
confere('o dia do Bastiao: 120 PE, 5,7 conjuracoes em 13 rodadas; e o dia de luta de 10,5', (PE_DIA, CONJ_DIA, DIA_RODADAS, DIA_ABSORVER), (120, 5.7, 13, 10.5))
if falhas: print('\n>>> A REGRESSAO FALHOU — nada abaixo vale.'); sys.exit(1)
print('>>> TUDO OK.\n')

# --- as convencoes novas: (baixo, alto) ------------------------------------------------------------
CONV = {
    'T':   ('golpes que o Bastiao assume por Olhos Em Mim, por rodada', 0.5, 1.0),
    'Al':  ('o atacante ao alcance do contra-golpe', 0.5, 1.0),
    'G':   ('golpes que o Bastiao recebe por rodada (Bloquear)', 1, 2),
    'H':   ('rodadas com metade da vida ou menos', 0.25, 0.5),
    'C':   ('rodadas em que o Guarda-Costas vale (atacante junto de voce, ou a distancia)', 0.5, 0.75),
    'TRF': ('Testes de Resistencia Fisicos por rodada', 0.25, 0.5),
    'Nx':  ('rodadas com quatro inimigos na area do Arrastao', 0.0, 0.5),
}
def val(c, lado): return CONV[c][1 if lado == 'b' else 2]
def p_algum(g, p): return 1 - (1 - p) ** g        # pelo menos um de g
F = lambda d: d / FATIA

def bastiao(lado):
    T, Al, G, H, C, TRF, Nx = (val(k, lado) for k in ('T', 'Al', 'G', 'H', 'C', 'TRF', 'Nx'))
    blq_ok = p_algum(G, 1 - ACERTO)                  # pelo menos um Bloquear que deu certo
    blq_falha = p_algum(G, ACERTO)                   # pelo menos um golpe que entrou mesmo Bloqueando
    feit = CONJ_DIA / DIA_RODADAS                    # rodadas com feitiço de Classe acima de 0
    e = {}
    # Muro
    e[('Muro', 2, 'Alicerce')] = TIPOS[2] * FATIA
    e[('Muro', 11, 'Guarda-Costas')] = 2 * DEF1 * C
    e[('Muro', 19, 'Casca Grossa')] = (10 + 6) * T
    e[('Muro', 27, 'Inabalável')] = (TIPOS[4] - TIPOS[2]) * FATIA
    # Punho
    e[('Punho', 2, 'Trocação Franca')] = SOCO * DOIS + SOCO * T * Al
    e[('Punho', 11, 'Mão Pesada')] = 3 * POS15 + DERRUBADO * DOIS * FALHA_TR
    e[('Punho', 19, 'Minha Vez')] = (SOCO - 2 * PE) * blq_ok * Al
    e[('Punho', 27, 'Arrastão')] = (4 - 2) * SOCO * Nx
    # Combatente Amaldicoado
    e[('Combatente Amaldiçoado', 2, 'Retaliação')] = CLASSE0 * T + (6 / (DIA_RODADAS if lado == 'b' else DIA_ABSORVER)) * PE
    e[('Combatente Amaldiçoado', 11, 'Embalo')] = (2 * 0.05 + TRF * (1 - FALHA_TR)) * 4 * PE
    e[('Combatente Amaldiçoado', 19, 'Oportunista')] = CLASSE[7] * VANT * feit * blq_ok
    e[('Combatente Amaldiçoado', 27, 'Contra a Parede')] = CLASSE[3] * H          # leitura A: metade para baixo, de graca
    return e

B, A = bastiao('b'), bastiao('a')
print('=' * 104)
print('1 · AS TRES TRILHAS, em fatias (5,08 de dano por rodada no nivel 30); orcamento 5,00, banda 4,50 a 5,00')
print('=' * 104)
for tri in ('Muro', 'Punho', 'Combatente Amaldiçoado'):
    tb = ta = 0
    for (t, nv, nome), vb in B.items():
        if t != tri: continue
        va = A[(t, nv, nome)]; tb += F(vb); ta += F(va)
        print(f'  {tri[:22]:22s} nv {nv:2d}  {nome:18s} {F(vb):5.2f} a {F(va):5.2f}')
    print(f'  {"":22s} {"TOTAL":24s} {tb:5.2f} a {ta:5.2f}\n')

print('=' * 104)
print('2 · AS DUAS PENDENCIAS DA v0.4, medidas nas leituras possiveis (nivel 30, maior Classe 7)')
print('=' * 104)
H_b, H_a = CONV['H'][1], CONV['H'][2]
print('  Contra a Parede — a metade da maior Classe, e o custo da conjuracao:')
for arred, cl in (('para baixo (Classe 3)', 3), ('para cima (Classe 4)', 4)):
    for custo, pe in (('de graca', 0), ('pagando o PE', PE_POR_CLASSE * cl)):
        liq = CLASSE[cl] - pe * PE
        print(f'    {arred:22s} {custo:13s} por uso: {CLASSE[cl]} de dano − {pe:2d} PE ({pe * PE:5.1f}) = {liq:6.1f} · '
              f'na rodada: {F(liq * H_b):5.2f} a {F(liq * H_a):5.2f} fatias')
print('  Oportunista — um alvo contra todos os alvos de um feitico de area (tres), no prazo do proximo turno:')
feit = CONJ_DIA / DIA_RODADAS
for alc, mult in (('um ataque ou um alvo', 1), ('todos os alvos (tres)', 3)):
    vb = CLASSE[7] * VANT * feit * p_algum(1, 1 - ACERTO) * mult; va = CLASSE[7] * VANT * feit * p_algum(2, 1 - ACERTO) * mult
    print(f'    {alc:24s} {F(vb):5.2f} a {F(va):5.2f} fatias')

print()
print('=' * 104)
print('3 · O CAMINHO BASE — o que a regua mede e o que nao tem conversao (o Caminho tinha 3,00 fatias)')
print('=' * 104)
G_b, G_a = CONV['G'][1], CONV['G'][2]
ainda = (4.5 + 15) / 3.3
duro_b, duro_a = (11 + 6) * p_algum(G_b, ACERTO), (11 + 6) * p_algum(G_a, ACERTO)
print(f'  nv 7  Ainda de Pé    cura 1d8 + 15 uma vez por cena, numa luta de 3,3 rodadas: {F(ainda):4.2f} fatia')
print(f'  nv 15 Duro de Matar  2d10 + Constituicao 6 no golpe que entrou, uma vez por rodada: {F(duro_b):4.2f} a {F(duro_a):4.2f} fatias')
print(f'  as duas somam {F(ainda + duro_b):4.2f} a {F(ainda + duro_a):4.2f} — acima das 3,00 do Caminho, sem contar o resto')
print('  nv 2  Olhos Em Mim   a transferencia de golpe e a Provocacao em area: SEM conversao na regua')
print('  nv 7  Ataque Extra   correcao de base, de graca pela peca 6 §3.1; Nem Um Arranhao: depende de quantos efeitos de TR Fisico')
print('  nv 23 Chega Mais     a area em 9 m e a Provocacao de quem entra: SEM conversao (e a mesma lacuna do nv 2)')
print('  nv 30 Passa Pra Mim  "a queda nao aconteceu": SEM conversao — e a lacuna do Ninguem Cai, registrada desde a v0.77')

print()
print('CONVENCOES USADAS (baixo · alto) — nenhuma tem dono no projeto:')
for k, (txt, b, a) in CONV.items(): print(f'  {k:4s} {txt}: {b} · {a}')
print('>>> O piloto nao certifica nada: ele mostra onde as tres Trilhas caem com as convencoes escritas.')

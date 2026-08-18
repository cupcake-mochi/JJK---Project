# -*- coding: utf-8 -*-
"""Confere maestria, atributos, acerto, defesa, Testes de Resistencia e pericias.

Roda antes de fechar qualquer versao que mexa nesses numeros.

A REGRA QUE GOVERNA TUDO:
  Numa rolagem disputada, os dois lados precisam crescer no MESMO RITMO. Nao basta
  os dois crescerem — se um cresce mais rapido, a chance deriva ao longo da campanha,
  e nenhum valor fixo conserta isso.

    atributo investido, campanha inteira ... 3 -> 6   (+3)
    maestria a cada 4 niveis ............... 1 -> 8   (+7)   RAPIDO DEMAIS
    maestria a cada 8 niveis ............... 1 -> 4   (+3)   casa com o atributo

CONTRATO DE INVARIANTES:
  Maestria             = 1, +1 a cada 8 niveis
  Ataque corpo a corpo = d20 + Forca
  Ataque a distancia   = d20 + Destreza
  Ataque de conjuracao = d20 + 2 + maestria
  Defesa               = 10 + Destreza + protecao
  CD de feitico        = 10 + 2 + maestria
  Teste de Resistencia = d20 + atributo do TR (+2 se treinado)
  Pericia              = d20 + atributo + maestria (maestria so entra se treinado)
  Pontos de vida       = (inicial do Caminho + Con) + (por nivel do Caminho + Con) x (nivel-1)
  Integridade          = 20 + 8 x (nivel - 1)   — plana, sem Caminho e sem Constituicao

  1. Acerto NAO deriva na campanha — nem fisico nem de conjuracao.
  2. Teste de Resistencia NAO deriva — nem treinado nem sem treino.
  3. Ser treinado vale exatamente 10 pontos percentuais.
  4. Pericia DEVE derivar para cima: e o unico lugar onde crescer e o ponto.
  5. Nenhum termo aparece dos dois lados da mesma rolagem.
  6. Constituicao compra sobrevivencia na MESMA FAIXA que a Destreza ja compra
     pela Defesa. Nao e o numero do manual que decide isso — e o outro atributo
     que ja mexe em sobrevivencia.
  7. Integridade NAO leva Caminho nem Constituicao: dano de alma ignora o corpo.
  8. MEDIA DOS DADOS + CONSTITUICAO TIPICA (3) ~= 8, que e o que o manual supoe.
     ATENCAO: nao e a media dos dados sozinha. O 8 do manual e a vida TOTAL por
     nivel, sem atributo nenhum — ele foi escrito antes de existir Constituicao.
     Conferir a media dos dados contra o 8 foi o erro da v0.18: dava ao grupo 38%
     de vida a mais do que a tabela de encontro supoe.

PONTO CEGO CORRIGIDO EM 06/08:
  A versao anterior testava invariancia mantendo os atributos FIXOS. Isso verifica
  se o nivel cancela, mas nao se a CAMPANHA cancela — o defensor investe em Destreza
  e vai de 3 a 6. Todo teste aqui agora varia o atributo junto com o nivel.
"""
import os
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(AQUI, '..', 'skills', 'balanceamento-simulacao', 'scripts'))
from dados import soma, p_ao_menos  # noqa: E402

D20 = soma([20])
NIVEIS = [2, 6, 10, 14, 18, 22, 26, 30]
FIXO = 2
ERROS = []
_PULADAS = []


def maestria(nv):   return 1 + max(0, nv - 2) // 8
def investido(nv):  return min(6, 3 + max(0, nv - 2) // 8)   # o atributo de quem investe
def conjuracao(nv): return FIXO + maestria(nv)
def defesa(nv, des, prot): return 10 + des + prot
def cd(nv, prec=0): return 10 + conjuracao(nv) + 2 * prec
# Caminho: (dado, vida no nivel 1, vida por nivel, PE por nivel)
CAMINHO = {
    'Bastiao':   (12, 12, 7, 4),
    'Vanguarda': (8,   8, 5, 5),
    'Guia':      (8,   8, 5, 5),
    'Evocador':  (6,   6, 4, 6),
    'Emanador':  (6,   6, 4, 6),
}
BASE_MANUAL = 8   # vida por nivel que o manual usa para calibrar chefe e capanga
CON_TIPICA = 3    # o que uma ficha comum carrega em Constituicao

# Dano de chefe por rodada, tabela do manual (linhas 1598-1637 do .docx)
CHEFE = {5: 15, 10: 26, 15: 38, 20: 49, 25: 61, 30: 72}


def dano_chefe(nv):
    if nv <= 5:
        return 15 * nv / 5
    ks = sorted(CHEFE)
    for a, b in zip(ks, ks[1:]):
        if a <= nv <= b:
            return CHEFE[a] + (CHEFE[b] - CHEFE[a]) * (nv - a) / (b - a)
    return CHEFE[30]


def vida(nv, con, cam='Guia'):
    _, ini, porniv, _ = CAMINHO[cam]
    return (ini + con) + (porniv + con) * (nv - 1)


def integridade(nv): return 20 + 8 * (nv - 1)
def vida_manual(nv): return 20 + 8 * (nv - 1)


def pe_maximo(nv, cam):
    """PE por nivel do Caminho x nivel. Escrito na v0.26 (peca 1, secao 5.3)."""
    return CAMINHO[cam][3] * nv


# A tabela do manual "quantas vezes voce lanca o seu melhor feitico" e calculada
# em cima de um conjurador de 6 PE por nivel. Ela E a formula, e e por isso que
# a formula nao e escolha nossa.
PE_MANUAL = {1: 6, 5: 30, 9: 54, 13: 78, 17: 102, 20: 120}


def pct(alvo): return p_ao_menos(D20, alvo) * 100


def erro(msg):
    ERROS.append(msg)
    print('  ERRO:', msg)


def sem_deriva(nome, valores, tolerancia=0):
    d = max(valores) - min(valores)
    if d > tolerancia:
        erro(f'{nome}: deriva de {d:.0f}pp na campanha (tolerancia {tolerancia})')
    return d


print('=' * 88)
print('0. RITMOS — o que cresce, e quanto')
print('=' * 88)
print('  ' + '  '.join(f'nv{nv}: M{maestria(nv)}/atr{investido(nv)}' for nv in NIVEIS))
print(f'  maestria cresce +{maestria(30)-maestria(2)} · atributo investido cresce +{investido(30)-investido(2)}')
if maestria(30) - maestria(2) != investido(30) - investido(2):
    erro('maestria e atributo investido crescem em ritmos diferentes')

print()
print('=' * 88)
print('1. ACERTO — contra alvo que INVESTE em Destreza (3 -> 6) com protecao 1')
print('=' * 88)
print(f"  {'quem ataca':<38}" + ''.join(f'nv{nv:<4}' for nv in NIVEIS) + '  deriva')
for nome, bonus in [
    ('corpo a corpo (Forca investida)', investido),
    ('a distancia (Destreza investida)', investido),
    ('conjuracao (2 + maestria)', conjuracao),
]:
    vals = [pct(defesa(nv, investido(nv), 1) - bonus(nv)) for nv in NIVEIS]
    print(f'  {nome:<38}' + ''.join(f'{v:3.0f}%  ' for v in vals) + f'  {sem_deriva(nome, vals):.0f}pp')

print()
print('=' * 88)
print('2. TESTE DE RESISTENCIA — o resistente tambem investe (3 -> 6)')
print('=' * 88)
print(f"  {'estado':<38}" + ''.join(f'nv{nv:<4}' for nv in NIVEIS) + '  deriva')
res = {}
for tre in (False, True):
    vals = [pct(cd(nv) - (investido(nv) + (2 if tre else 0))) for nv in NIVEIS]
    rot = 'treinado (+2)' if tre else 'sem treino'
    res[tre] = vals
    print(f'  {rot:<38}' + ''.join(f'{v:3.0f}%  ' for v in vals) + f'  {sem_deriva(rot, vals):.0f}pp')
for i, nv in enumerate(NIVEIS):
    d = res[True][i] - res[False][i]
    if abs(d - 10) > 1e-9:
        erro(f'nivel {nv}: treino vale {d:.0f}pp, esperado 10pp')
print('  treinar vale 10pp em todos os niveis.')

print()
print('=' * 88)
print('3. PRECISAO (+2 na CD) — 10 pontos percentuais em todo nivel?')
print('=' * 88)
ok = True
for nv in NIVEIS:
    for tre in (False, True):
        b = investido(nv) + (2 if tre else 0)
        d = pct(cd(nv) - b) - pct(cd(nv, prec=1) - b)
        if abs(d - 10) > 1e-9:
            erro(f'nv {nv}, treinado={tre}: Precisao vale {d:.0f}pp')
            ok = False
if ok:
    print('  Conferido em todos os niveis e estados de treino: 10 pp sempre.')

print()
print('=' * 88)
print('4. PERICIA — aqui a deriva para CIMA e o objetivo')
print('=' * 88)
print(f"  {'dificuldade':<38}" + ''.join(f'nv{nv:<4}' for nv in NIVEIS) + '  ganho')
for cdf, rot in [(10, 'rotina'), (14, 'facil'), (18, 'media'), (22, 'dificil'), (26, 'quase impossivel')]:
    vals = [pct(cdf - (investido(nv) + maestria(nv))) for nv in NIVEIS]
    ganho = vals[-1] - vals[0]
    print(f'  {"CD "+str(cdf)+" ("+rot+")":<38}' + ''.join(f'{v:3.0f}%  ' for v in vals) + f'  {ganho:+.0f}pp')
    if ganho <= 0:
        erro(f'pericia CD {cdf} nao melhora com a campanha — perde o unico proposito da maestria')

print()
print('=' * 88)
print('5. NENHUM TERMO DOS DOIS LADOS DA MESMA ROLAGEM')
print('=' * 88)
lados = {
    'acerto de conjuracao': ({'2 fixo', 'maestria'}, {'Destreza', 'protecao'}),
    'Teste de Resistencia': ({'2 fixo', 'maestria'}, {'atributo do TR', 'treino +2'}),
    'pericia':              ({'CD da dificuldade'}, {'atributo', 'maestria'}),
}
for nome, (a, b) in lados.items():
    comum = a & b
    print(f'  {nome:<24} ataque {sorted(a)}  vs  defesa {sorted(b)}'
          + ('   <<< TERMO REPETIDO' if comum else '   ok'))
    if comum:
        erro(f'{nome}: {comum} aparece dos dois lados')

print()
print('=' * 88)
print('6. VIDA — Constituicao compra o mesmo tanto de sobrevivencia que a Destreza?')
print('=' * 88)
print('  A referencia NAO e a tabela do manual, que nao tem atributo nenhum.')
print('  E o outro atributo que ja compra sobrevivencia: Destreza, pela Defesa.\n')
print(f"  {'nivel':<8}{'Des 1->6 (erra mais)':>22}{'Con 1->6 (aguenta mais)':>26}{'razao':>9}")
for nv in NIVEIS:
    a1 = p_ao_menos(D20, defesa(nv, 1, 0) - conjuracao(nv))
    a6 = p_ao_menos(D20, defesa(nv, 6, 0) - conjuracao(nv))
    g_des = a1 / a6 - 1
    g_con = vida(nv, 6) / vida(nv, 1) - 1
    razao = (1 + g_con) / (1 + g_des)
    print(f'  nv{nv:<6}{g_des:>21.0%}{g_con:>26.0%}{razao:>9.2f}')
    if not 0.60 <= razao <= 1.40:
        erro(f'nv{nv}: Constituicao compra {razao:.2f}x o que a Destreza compra — '
             f'fora da faixa, um dos dois domina a sobrevivencia')
print('\n  Razao 1,00 = os dois compram igual. As duas correm em sentidos opostos:')
print('  Destreza protege mais cedo (a Defesa nao cresce), Constituicao mais tarde')
print('  (a vida cresce). E por isso que uma nao domina a outra a campanha inteira.')

print()
print('=' * 88)
print('7. VIDA POR CAMINHO')
print('=' * 88)
print(f"  {'Caminho':<12}{'dado':>6}{'nv1':>6}{'/nivel':>8}{'PE':>5}{'  vida+PE':>10}"
      + ''.join(f'nv{n}'.rjust(9) for n in [2, 10, 30]))
for nome, (dado, ini, porniv, pe) in CAMINHO.items():
    print(f'  {nome:<12}d{dado:<5}{ini:>6}{porniv:>8}{pe:>5}{porniv + pe:>10}'
          + ''.join(f'{vida(n, CON_TIPICA, nome):>9}' for n in [2, 10, 30]))

# a vida inicial e o maximo do dado; a de nivel e a metade arredondando pra cima
for nome, (dado, ini, porniv, _) in CAMINHO.items():
    if ini != dado:
        erro(f'{nome}: vida inicial {ini} nao e o maximo do d{dado}')
    if porniv != dado // 2 + 1:
        erro(f'{nome}: vida por nivel {porniv} nao e a metade do d{dado} arredondando '
             f'pra cima ({dado // 2 + 1}) — o dado e o fixo deixam de ser equivalentes')

media_dados = sum(c[2] for c in CAMINHO.values()) / len(CAMINHO)
efetiva = media_dados + CON_TIPICA
print(f'\n  media dos dados = {media_dados:.1f}   + Constituicao tipica ({CON_TIPICA}) = {efetiva:.1f}'
      f'   (o manual supoe {BASE_MANUAL})')
if abs(efetiva - BASE_MANUAL) > 1.0:
    erro(f'media dos dados + Constituicao tipica da {efetiva:.1f}, e o manual supoe '
         f'{BASE_MANUAL} — a tabela de encontro dele deixa de valer para um grupo tipico')
print('  NAO conferir a media dos dados sozinha contra o 8: o 8 do manual e a vida TOTAL')
print('  por nivel, escrita antes de existir Constituicao. Foi o erro da v0.18.')

print(f"\n  rodadas para cair sob foco (o manual calibra tudo em 3,5):")
print(f"  {'':<14}" + ''.join(f'nv{n}'.rjust(9) for n in [2, 5, 10, 20, 30]))
for nome in CAMINHO:
    print(f'  {nome:<14}' + ''.join(f'{vida(n, CON_TIPICA, nome) / dano_chefe(n):>9.1f}'
                                    for n in [2, 5, 10, 20, 30]))
med = [sum(vida(n, CON_TIPICA, c) for c in CAMINHO) / 5 / dano_chefe(n) for n in [2, 5, 10, 20, 30]]
print(f'  {"MEDIA":<14}' + ''.join(f'{m:>9.1f}' for m in med))
if not 2.5 <= sum(med) / len(med) <= 4.5:
    erro(f'grupo tipico cai em {sum(med)/len(med):.1f} rodadas — longe das 3,5 do manual')

hi_c = max(CAMINHO, key=lambda c: CAMINHO[c][2])
lo_c = min(CAMINHO, key=lambda c: CAMINHO[c][2])
espalha = vida(30, 6, hi_c) / vida(30, 0, lo_c)
print(f'\n  espalhamento no nv30: {vida(30, 0, lo_c)} ({lo_c} Con 0) a '
      f'{vida(30, 6, hi_c)} ({hi_c} Con 6)  ->  {espalha:.1f}x')
print(f'  ({vida(30, 0, lo_c) / dano_chefe(30):.1f} rodadas contra '
      f'{vida(30, 6, hi_c) / dano_chefe(30):.1f})')
if espalha > 3.5:
    erro(f'espalhamento de vida em {espalha:.1f}x — o mestre perde a nocao de quanto '
         f'dano derruba quem, e a tabela de encontro vira chute')
else:
    print('  Largo de proposito: a Constituicao entra ja no nivel 1, entao ela multiplica')
    print('  por NIVEL em vez de (nivel-1). Teto do validador em 3,5x por causa disso.')

somas = [c[2] + c[3] for c in CAMINHO.values()]
print(f'\n  soma vida+PE por Caminho: {min(somas)} a {max(somas)}')
if max(somas) - min(somas) > 2:
    erro(f'a soma vida+PE varia {max(somas)-min(somas)} entre Caminhos — a troca '
         f'"couro contra combustivel" virou degrau de poder em vez de sabor')
else:
    print('  Parelha: a troca couro-contra-combustivel e sabor, nao degrau de poder.')

print(f"\n  as tres alavancas de sobrevivencia, no nv10, do menor valor ao maior:")
b = conjuracao(10)
g_cam = vida(10, CON_TIPICA, hi_c) / vida(10, CON_TIPICA, lo_c) - 1
g_con = vida(10, 6) / vida(10, 0) - 1
g_des = p_ao_menos(D20, defesa(10, 1, 0) - b) / p_ao_menos(D20, defesa(10, 6, 0) - b) - 1
print(f'    Caminho  {g_cam:>6.0%}     Constituicao  {g_con:>6.0%}     Destreza  {g_des:>6.0%}')
if max(g_cam, g_con, g_des) / min(g_cam, g_con, g_des) > 2.5:
    erro('uma das tres alavancas de sobrevivencia domina as outras duas')

print()
print('=' * 88)
print('8. INTEGRIDADE NAO LEVA CAMINHO NEM CONSTITUICAO')
print('=' * 88)
print(f"  {'nivel':<8}{'Integridade':>13}{'Emanador Con3':>16}{'Bastiao Con3':>15}   quem acaba primeiro")
for nv in [2, 10, 18, 30]:
    i = integridade(nv)
    frag, duro = vida(nv, CON_TIPICA, lo_c), vida(nv, CON_TIPICA, hi_c)
    quem = 'o corpo, nos dois' if duro < i else f'a alma do {hi_c}, so ele'
    print(f'  nv{nv:<6}{i:>13}{frag:>16}{duro:>15}   {quem}')
    if integridade(nv) != vida_manual(nv):
        erro(f'nv{nv}: Integridade saiu da formula original do manual — a tabela de '
             f'estagios de dano de alma precisaria ser refeita')
print('\n  A Integridade e exatamente a formula que o manual ja tem, e nao muda nenhuma')
print('  tabela: os quatro estagios continuam valendo.')
print('\n  ATENCAO, efeito colateral da vida menor: a alma virou a reserva MAIOR em quatro')
print('  dos cinco Caminhos. Quem nao e Bastiao cai pelo corpo antes de a alma acabar,')
print('  entao o estagio 4 de dano de alma quase nunca dispara. Isso muda quando a')
print('  Essencia entrar na Integridade.')
print('\n  PENDENTE E JA DECIDIDO: a Integridade vai escalar com Essencia, virando uma')
print('  segunda vida de verdade. Entra junto com a peca de dano de alma.')

# --------------------------------------------------------------------------
print()
print('=' * 88)
print('PONTOS DE ENERGIA — a formula que estava no manual e ninguem tinha lido')
print('=' * 88)
print('  Escrita na v0.26. Ate ali so existia a instancia do nivel 2 na peca 8, e ela')
print('  nao da para generalizar sozinha: a vida ao lado dela multiplica por (nivel-1)')
print('  e ainda soma atributo, entao as duas leituras obvias eram plausiveis.\n')
print(f"  {'nivel':<8}{'PE do manual':<16}{'6 x nivel':<12}bate?")
for nv in sorted(PE_MANUAL):
    calc = 6 * nv
    ok = PE_MANUAL[nv] == calc
    print(f'  {nv:<8}{PE_MANUAL[nv]:<16}{calc:<12}{"sim" if ok else "NAO"}')
    if not ok:
        erro(f'nv{nv}: a tabela de PE do manual ({PE_MANUAL[nv]}) nao e 6 x nivel ({calc}) — '
             f'a formula do projeto nao pode mais dizer que veio de la')

# a instancia da peca 8 precisa continuar caindo na formula geral
for cam in CAMINHO:
    pe_nivel = CAMINHO[cam][3]
    if pe_maximo(2, cam) != pe_nivel * 2:
        erro(f'{cam}: a formula geral discorda da instancia de nivel 2 da peca 8')

# e ela NAO pode levar atributo — a decisao da peca 1, secao 9
print('\n  Sem atributo dentro, e isso e decisao: um atributo na conta de PE viraria o')
print('  atributo obrigatorio de todo conjurador pela porta dos fundos.\n')
print(f"  {'Caminho':<12}" + ''.join(f'nv{n}'.rjust(7) for n in NIVEIS))
for cam in CAMINHO:
    print(f'  {cam:<12}' + ''.join(f'{pe_maximo(n, cam):>7}' for n in NIVEIS))

# a soma vida+PE por nivel e o que faz a troca ser sabor, e ela ja e conferida
# acima; aqui so garantimos que o PE cresce LINEAR, sem degrau escondido
for cam in CAMINHO:
    passos = {pe_maximo(n + 1, cam) - pe_maximo(n, cam) for n in range(2, 30)}
    if len(passos) != 1:
        erro(f'{cam}: o PE nao cresce em passo constante ({sorted(passos)}) — '
             f'a formula deixou de ser linear no nivel')
print('\n  O passo e constante em todos os cinco: o PE e a unica reserva do sistema que')
print('  cresce em linha reta desde o nivel 1, e e por isso que a ficha de nivel 2 ja')
print('  tem combustivel para uma missao sem ter couro para ela.')

print()
print('=' * 88)
print('9. INCONSCIENTE — a maquina de estado de 0 de vida (secao 5.5)')
print('=' * 88)

import re as _re
import math as _math

# Nada aqui fica escrito na mao: os numeros sao LIDOS da peca, e o limite de
# design fica declarado A PARTE da regra aplicada. Licao no 8: uma checagem nao
# pode se medir contra a propria constante.
PECA = os.path.join(AQUI, '01-atributos-acerto-defesa.md')
try:
    TXT = open(PECA, encoding='utf-8').read()
except OSError as _e:
    erro(f'nao consegui abrir a peca 1 para conferir o Inconsciente ({_e})')
    TXT = ''

sec = TXT.split('## 5.5')[1].split('## 6.')[0] if '## 5.5' in TXT else ''
if not sec:
    erro('a secao 5.5 (Inconsciente) sumiu da peca 1 — esta checagem parou de conferir')

# o ritmo de combate mora na secao 8 desta mesma peca, e e de la que ele vem
_m = _re.search(r'previsão atual é ([\d,]+) a ([\d,]+) rodadas', TXT)
if _m:
    RODADAS_MIN = float(_m.group(1).replace(',', '.'))
    RODADAS_MAX = float(_m.group(2).replace(',', '.'))
else:
    RODADAS_MIN = RODADAS_MAX = None
    erro('nao achei o ritmo de combate na secao 8 — a janela do Inconsciente nao tem contra o que '
         'ser medida, e esta checagem parou de conferir')
RODADAS_MED = (RODADAS_MIN + RODADAS_MAX) / 2 if RODADAS_MIN else 0

# --- o que a REGRA diz, lido do texto ---------------------------------------
m = _re.search(r'janela de \*\*(\d+) rodadas\*\*', sec)
JANELA = int(m.group(1)) if m else None
if JANELA is None:
    erro('nao achei a janela do Aguentar no texto da secao 5.5')

m = _re.search(r'\*\*1/(\d+), depois 1/(\d+), depois 1/(\d+)\*\*', sec)
ESCADA = [1/int(x) for x in m.groups()] if m else None
if ESCADA is None:
    erro('nao achei a escada de custo do Insistir no texto da secao 5.5')

m = _re.search(r'\*\*Na (segunda|terceira|quarta) queda', sec)
ORDINAL = {'segunda': 2, 'terceira': 3, 'quarta': 4}
CICATRIZ_NA = ORDINAL.get(m.group(1)) if m else None
if CICATRIZ_NA is None:
    erro('nao achei em que queda a Cicatriz entra no texto da secao 5.5')

# --- os LIMITES DE DESIGN, declarados aqui e nao lidos de la ----------------
JANELA_MINIMA_DE_DESIGN = 2      # abaixo disso o socorro nunca chega a tempo
JANELA_MAXIMA_DE_DESIGN = 3      # acima disso socorrer deixa de custar decisao
CUSTO_TOTAL_MAXIMO = 1.0         # Insistir nao pode zerar a maxima antes da 3a
QUEDAS_PLAUSIVEIS_POR_MISSAO = 2 # medido abaixo; a Cicatriz tem que caber nisso

# --- 9.1 a janela cabe no combate -------------------------------------------
if JANELA is not None:
    if not (JANELA_MINIMA_DE_DESIGN <= JANELA <= JANELA_MAXIMA_DE_DESIGN):
        erro(f'a janela do Aguentar e {JANELA} rodadas, fora da faixa de design '
             f'{JANELA_MINIMA_DE_DESIGN}-{JANELA_MAXIMA_DE_DESIGN} — abaixo dela o socorro '
             f'nunca chega, acima dela socorrer deixa de custar o turno de alguem')
    if RODADAS_MAX is not None and JANELA > RODADAS_MAX:
        erro(f'a janela ({JANELA}) passa do combate inteiro ({RODADAS_MAX} rodadas): '
             f'quem cai nunca correria risco nenhum')
    print(f'  janela do Aguentar: {JANELA} rodadas, num combate de '
          f'{RODADAS_MIN} a {RODADAS_MAX}.')

# --- 9.2 a escada do Insistir da o mesmo numero de rodadas para TODOS -------
if ESCADA:
    total = sum(ESCADA)
    if total >= CUSTO_TOTAL_MAXIMO:
        erro(f'a escada do Insistir soma {total:.3f} da vida maxima, que e >= 1 — '
             f'ela zera a maxima antes de a terceira rodada terminar')
    janelas = set()
    for cam in CAMINHO:
        for con in (0, 3, 6):
            for nv in NIVEIS:
                vmax = vida(nv, con, cam)
                restante, rodadas = vmax, 0
                for frac in ESCADA:
                    custo = _math.ceil(vmax * frac)   # arredondamento da 5.4: custo sobe
                    if custo > restante:
                        break
                    restante -= custo
                    rodadas += 1
                janelas.add(rodadas)
    if len(janelas) != 1:
        erro(f'o Insistir NAO da a mesma janela para todo mundo: {sorted(janelas)} rodadas '
             f'conforme Caminho, Constituicao e nivel. Era esse o motivo de cobrar fracao '
             f'em vez do dano que entra — a vida maxima espalha 3,2x entre os Caminhos')
    else:
        print(f'  Insistir: {total:.3f} da maxima no total, e {janelas.pop()} rodadas para os '
              f'{len(CAMINHO)} Caminhos x 3 Constituicoes x {len(NIVEIS)} niveis.')

# --- 9.3 o contra-teste: o dano que entra NAO daria janela igual ------------
# se esta perturbacao deixar de acender, a checagem 9.2 virou decoracao
janelas_dano = set()
for cam in CAMINHO:
    for con in (0, 3, 6):
        janelas_dano.add(round(vida(14, con, cam) / (dano_chefe(14) * 0.5)))
if len(janelas_dano) == 1:
    erro('contra-teste falhou: cobrar o dano que entra daria a MESMA janela para todos, '
         'entao a checagem 9.2 nao esta provando nada')
else:
    print(f'  contra-teste: cobrar o dano que entra daria {min(janelas_dano)} a '
          f'{max(janelas_dano)} rodadas conforme o corpo. Por isso a escada e fracao.')

# --- 9.4 a Cicatriz entra numa queda que acontece de verdade ---------------
LUTAS_POR_MISSAO, ACERTO, GRUPO = 4, 0.5, 4
pior = 0.0
for nv in NIVEIS:
    dano_missao = dano_chefe(nv) * ACERTO * RODADAS_MED / GRUPO * LUTAS_POR_MISSAO
    for cam in CAMINHO:
        pior = max(pior, dano_missao / vida(nv, 0, cam))
if CICATRIZ_NA is not None:
    if CICATRIZ_NA > QUEDAS_PLAUSIVEIS_POR_MISSAO:
        erro(f'a Cicatriz entra na {CICATRIZ_NA}a queda, e o perfil mais fragil cai '
             f'{pior:.2f} vez(es) por missao — uma regra cujos dentes so aparecem la '
             f'nunca morde')
    print(f'  Cicatriz na {CICATRIZ_NA}a queda; o perfil mais fragil cai {pior:.2f} '
          f'vez(es) por missao padrao.')

# --- 9.5 a Sequela nao pode virar espiral de competencia -------------------
PROIBIDO = ('desvantagem', 'penalidade em ataque', '-1 em', 'menos 1 em')
achado = [p for p in PROIBIDO
          if _re.search(r'Sequela[^.]{0,160}' + _re.escape(p), sec, _re.I)
          or _re.search(_re.escape(p) + r'[^.]{0,160}Sequela', sec, _re.I)]
if achado:
    erro(f'a Sequela encostou em rolagem ({achado}) — isso e espiral de COMPETENCIA, '
         f'que a v0.8 consertou e a peca 10 limitou. Ela so pode encurtar a janela')
else:
    print('  a Sequela so encurta a janela: espiral de letalidade, nunca de competencia.')

# --- 9.6 Aguentar e Insistir nao se dominam (teste de conjunto da peca 3) ---
AGUENTAR = ({'janela de 3 rodadas', 'acorda com 1 de cura'},
            {'fora da luta desde ja', 'uma Sequela'})
INSISTIR = ({'age por 3 rodadas'},
            {'7/8 da vida maxima', 'uma Sequela', 'so acorda com metade da maxima'})
for (na, a), (nb, b) in ((('Aguentar', AGUENTAR), ('Insistir', INSISTIR)),
                         (('Insistir', INSISTIR), ('Aguentar', AGUENTAR))):
    if a[0] >= b[0] and a[1] <= b[1] and (a[0] > b[0] or a[1] < b[1]):
        erro(f'{na} domina {nb}: mesmo preco, e um dos dois nunca teria motivo de ser escolhido')
print('  Aguentar e Insistir: nenhum contem o outro. A escolha existe nos dois sentidos.')


print('=' * 88)
if ERROS:
    print(f'>>> {len(ERROS)} PROBLEMA(S):')
    for e in ERROS:
        print('   -', e)
    raise SystemExit(1)
if _PULADAS:
    print(f'>>> OK, mas {len(_PULADAS)} checagem(ns) PULARAM: ' + '; '.join(_PULADAS))
    print('    um verde que pulou checagem nao prova nada.')
else:
    print('>>> TUDO OK — nada deriva onde nao deve, e a pericia deriva onde deve.')

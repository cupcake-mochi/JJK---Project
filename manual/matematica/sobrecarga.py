#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Quanto vale a `Sobrecarga`, somada, em cada um dos dois degraus.

A divergencia: `Leve` no manual/gerador/partD.js e no .docx, `Pesada` no
sistema/05-material/livro/manual/40-fundamento.md.

Nenhum numero mora aqui dentro: cada um e' lido do documento dono, no mesmo
lugar de onde o conferir-dano.py le. A regua e a da peca 19 §2.2.
"""
import os, re, sys, math

# a raiz sai do __file__, no molde dos validadores da casa: este arquivo mora em
# manual/matematica/, entao sao dois niveis acima.
# O JJK_RAIZ existe so' para o arnes rodar a conta contra uma copia perturbada.
RAIZ = os.environ.get(
    'JJK_RAIZ',
    os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                 '..', '..')))

def ler(rel):
    with open(os.path.join(RAIZ, rel), encoding='utf-8') as f:
        return f.read()

def num(s):
    return float(s.replace(',', '.'))

def pega(rel, padrao, rotulo):
    m = re.search(padrao, ler(rel))
    if not m:
        print(f'  !! ancora perdida: {rotulo} — nao casa em {rel}')
        sys.exit(1)
    return m

P01  = 'sistema/03-mecanica/01-atributos-acerto-defesa.md'
P05  = 'sistema/03-mecanica/05-caminho-e-combate-sem-feitico.md'
P19  = 'sistema/03-mecanica/19-dano-e-condicoes.md'
P26  = 'sistema/03-mecanica/26-bestiario.md'
DTRI = 'DESENHO-trilhas.md'
PARTA = 'manual/gerador/partA.js'
PARTD = 'manual/gerador/partD.js'
FUND  = 'sistema/05-material/livro/manual/40-fundamento.md'

print('=' * 86)
print('AS ANCORAS — lidas do dono, nenhuma escrita aqui')
print('=' * 86)

CHEFE = float(pega(DTRI, r'chefe (?:do nível 30 )?em `?(\d+)`? de dano por rodada',
                   'o chefe').group(1))
CAPANGA = float(pega(DTRI, r'o capanga em `(\d+)`', 'o capanga').group(1))
ACOES = float(pega(P19, r'O chefe age `(\d+)` vezes por rodada', 'acoes do chefe').group(1))
ROTINA = float(pega(P19, r'a Rotina em `(\d+)`', 'a Rotina no nv30').group(1))
PONTO  = float(pega(P19, r'cada ponto que não vira Melhoria vira `1d8` de dano — que são `([\d,]+)`',
                    'o ponto de feitico').group(1).replace(',', '.'))
FILTRO = float(pega(P19, r'filtro de `([\d,]+)×`', 'o filtro de dominancia').group(1).replace(',', '.'))
PE_CAMBIO = float(pega(P05, r'recuperar `\+1` PE \| permanente \| `([\d,]+)`',
                       'o cambio de PE').group(1).replace(',', '.'))
# a taxa de resistencia de quem TREINOU, no nivel 30 (peca 1 §6)
RESISTE = float(pega(P01, r'\*\*treinado\*\* \| 65% \| 65% \| 65% \| 65% \| \*\*(\d+)%\*\*',
                     'o TR treinado').group(1)) / 100.0
RESISTE_SEM = float(pega(P01, r'\*\*sem treino\*\* \| 60% \| 55% \| 50% \| 45% \| \*\*(\d+)%\*\*',
                         'o TR sem treino').group(1)) / 100.0
CUSTO_PE = pega(PARTA, r'custa \*\*3 × Classe\*\* de PE', 'o custo em PE').group(0)
CLASSE0_GRATIS = pega(PARTA, r'Classe 0 é grátis', 'o Classe 0 gratis').group(0)
CLASSE0_METADE = pega(PARTA, r'gasta PE em cerca de \*\*metade das rodadas de luta do dia\*\*',
                      'metade das rodadas').group(0)
SEM_PE = pega(P26, r'O inimigo não conta PE', 'o inimigo sem PE').group(0)
# a Melhoria que o manual preca em exatamente +2 de CD
PRECISAO = pega(PARTD, r"\['Precisão', '(\w+)', '\+2 na rolagem de acerto, ou \+2 na CD",
                'a Precisao').group(1)
# a Melhoria que o manual preca em exatamente -2 num teste de resistencia
ABREFERIDA = pega(PARTD, r"\['Abre Ferida', '(\w+)'", 'a Abre Ferida').group(1)
# TR bem-sucedido = metade do dano
METADE = pega(PARTD, r'O alvo ainda faz o Teste de Resistência pra metade', 'a metade').group(0)

print(f'  chefe nv30                 {CHEFE:.0f} de dano por rodada, em {ACOES:.0f} acoes')
print(f'  capanga nv30               {CAPANGA:.0f} de dano por rodada')
print(f'  Rotina nv30                {ROTINA:.0f}')
print(f'  1 ponto de feitico         {PONTO:.1f} de dano')
print(f'  filtro de dominancia       {FILTRO:.2f}x')
print(f'  TR no nv30                 treinado resiste {RESISTE:.0%}, sem treino {RESISTE_SEM:.0%}')
print(f'  TR bem-sucedido            metade do dano  (Certeiro, manual)')
print(f'  custo de um feitico        3 x Classe de PE; Classe 0 e gratis')
print(f'  +1 PE permanente           {PE_CAMBIO:.2f} de dano por rodada')
print(f'  `Precisao` (+2 na CD)      o manual preca em {PRECISAO}')
print(f'  `Abre Ferida` (-2 no TR)   o manual preca em {ABREFERIDA}')
print(f'  o inimigo                  nao conta PE (peca 26 §6.1)')

print()
print('=' * 86)
print('A REGUA DA CD — quanto vale mover 2 pontos num d20 de resistencia')
print('=' * 86)
# 2 pontos num d20 = 10 pontos percentuais. Um TR bem-sucedido corta o dano pela
# metade, entao a fracao do dano que chega e' (1 - R) * 1 + R * 0,5 = 1 - R/2.
PP_POR_PONTO = 1 / 20.0
DELTA_PP = 2 * PP_POR_PONTO
def chega(r):
    return 1 - r / 2.0
for rot, r in (('treinado', RESISTE), ('sem treino', RESISTE_SEM)):
    antes, depois = chega(r), chega(min(1.0, r + DELTA_PP))
    print(f'  {rot:<11} resiste {r:.0%} -> {r + DELTA_PP:.0%} | do dano chega '
          f'{antes:.1%} -> {depois:.1%} | negado {antes - depois:.2%}')
NEGA_CD = DELTA_PP / 2.0
print(f'\n  >> -2 na CD nega SEMPRE {NEGA_CD:.1%} do dano daquele feitico.')
print('     Nao depende da taxa de resistencia: metade da massa que se desloca')
print('     troca dano cheio por metade, e 10 pp / 2 = 5 pp. E o mesmo tamanho')
print(f'     que o manual ja preca DUAS vezes em `{PRECISAO}` — a `Precisao` e a `Abre Ferida`.')

print()
print('=' * 86)
print('O QUE A `Sobrecarga` ENTREGA — as duas metades, medidas separadas')
print('=' * 86)
print('  "Ate o fim do proximo turno do alvo, o feitico dele custa o dobro de')
print('   energia e sai com a CD 2 menor."')
print()
print('  METADE 1 — o dobro de energia')
print(f'   jogador -> inimigo   {0.0:>7.2f}   o inimigo nao conta PE (peca 26 §6.1).')
print( '                                  Nao existe alvo no bestiario inteiro.')
POR_ACAO = CHEFE / ACOES
# o outro lado: um inimigo poe Sobrecarga num jogador
DIA = float(pega('sistema/03-mecanica/06-caminhos-e-trilhas.md',
                 r'`([\d,]+)` rodadas de luta por dia', 'as rodadas por dia').group(1).replace(',', '.'))
for C in (7,):
    pe_extra = 3 * C
    # um feitico de Classe C custa 3C PE; pagar 3C a mais e' um feitico daquela
    # Classe a menos no dia. O dano cheio dele e' 3C dados de d8.
    dano_cheio = 3 * C * 4.5
    por_rodada = dano_cheio / DIA
    print(f'   inimigo -> jogador   {por_rodada:>7.2f}   se ele PAGAR: +{pe_extra} PE e' 
          f' um Classe {C} a menos')
    print(f'                                  no dia ({dano_cheio:.0f} de dano / {DIA:.1f} rodadas).')
    print(f'   inimigo -> jogador   {0.0:>7.2f}   se ele conjurar um Classe 0: o dobro de zero')
    print( '                                  e zero. O manual diz que ele ja passa METADE')
    print( '                                  das rodadas no Classe 0 — e chama o Classe 0 de')
    print( '                                  "o golpe de todo turno em que o PE precisa ser')
    print( '                                  poupado". E o buraco que a v0.217 fechou na `Divida`.')
print()
print('  METADE 2 — a CD 2 menor')
print(f'   a janela e UM turno do alvo. O chefe age {ACOES:.0f} vezes nele.')
janela_alta = CHEFE * NEGA_CD
janela_baixa = POR_ACAO * NEGA_CD
cap = CAPANGA * NEGA_CD
print(f'   teto  (as {ACOES:.0f} acoes pedem TR)  {janela_alta:>7.2f} de dano por rodada')
print(f'   piso  (1 acao pede TR)      {janela_baixa:>7.2f}')
print(f'   num capanga                 {cap:>7.2f}')

print()
print('=' * 86)
print('O QUE ELA CUSTA — somada, nos dois degraus, em todas as sete Classes')
print('=' * 86)
def leve(C):   return math.ceil(C / 2)
def media(C):  return C
def pesada(C): return math.ceil(C * 1.5)
print(f'  {"Classe":<7}{"PE":>5}{"Leve":>7}{"Pesada":>8}   {"Leve em dano":>13}{"Pesada em dano":>16}'
      f'{"a mais":>9}')
for C in range(1, 8):
    l, p = leve(C), pesada(C)
    print(f'  {C:<7}{3*C:>5}{l:>7}{p:>8}   {l*PONTO:>13.1f}{p*PONTO:>16.1f}{(p-l)*PONTO:>9.1f}')
print()
print(f'  Na Classe 7, que e a do nivel 30: `Leve` custa {leve(7)} pontos ({leve(7)*PONTO:.1f} de dano)')
print(f'  e `Pesada` custa {pesada(7)} ({pesada(7)*PONTO:.1f}). A diferenca entre os dois degraus e')
print(f'  {(pesada(7)-leve(7))*PONTO:.1f} de dano por feitico — {(pesada(7)-leve(7))*PONTO/POR_ACAO:.2f} acoes de chefe.')

print()
print('=' * 86)
print('A DOMINANCIA — o que ela entrega dividido pelo que aqueles pontos dariam')
print('=' * 86)
print(f'  {"":<34}{"Leve":>10}{"Pesada":>10}      contra o filtro de {FILTRO:.2f}x')
for rot, val in (('teto: as 3 acoes pedem TR', janela_alta),
                 ('piso: 1 acao pede TR', janela_baixa),
                 ('num capanga', cap)):
    dl = val / (leve(7) * PONTO)
    dp = val / (pesada(7) * PONTO)
    print(f'  {rot:<34}{dl:>9.2f}x{dp:>9.2f}x')
print()
print('  A banda em que as treze condicoes ja publicadas vivem (peca 19 §2.2):')
band = re.findall(r'\| \*\*`([^`]+)`\*\* \| `[\d,]+` \| [^|]*\| `(\d+)` \| `([\d,]+)×` \| `(\w+)` \|',
                  ler(P19))
if len(band) != 13:
    print(f'  !! li {len(band)} linhas da tabela das treze, e sao 13. A forma mudou.')
    sys.exit(1)
for nome, pts, dom, tier in band:
    print(f'    {nome:<14} {tier:<7} {dom}x')

print()
print('=' * 86)
print('O VEREDITO DA MEDIDA')
print('=' * 86)
alvo_pesada = [num(d) for _, _, d, t in band if t == 'Pesada']
alvo_leve   = [num(d) for _, _, d, t in band if t == 'Leve']
print(f'  As `Pesada` ja publicadas entregam de {min(alvo_pesada):.2f}x a {max(alvo_pesada):.2f}x.')
print(f'  As `Leve`   ja publicadas entregam de {min(alvo_leve):.2f}x a {max(alvo_leve):.2f}x.')
print()
precisa = min(alvo_pesada) * pesada(7) * PONTO
print(f'  Para a `Sobrecarga` sentar no PIOR degrau `Pesada` que existe ({min(alvo_pesada):.2f}x)')
print(f'  ela teria de negar {precisa:.1f} de dano por rodada. Ela nega {janela_alta:.2f} no teto.')
print(f'  Falta um fator de {precisa/janela_alta:.0f}x. Isso nao se alcanca ajustando numero:')
print(f'  seria outra Melhoria.')
print()
print(f'  No degrau `Leve` ela cai em {janela_baixa/(leve(7)*PONTO):.2f}x a {janela_alta/(leve(7)*PONTO):.2f}x,')
print(f'  dentro da banda das `Leve` publicadas, entre o `Incapacitado` e o `Derrubado`.')

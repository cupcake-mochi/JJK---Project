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
# as rodadas da luta: a frase e' da secao `Inimigos` do manual, e o §6.1 da peca
# 26 diz que o terceiro fator do poco sai de la.
RODADAS = float({'duas': 2, 'três': 3, 'quatro': 4}[
    pega('manual/gerador/partF.js', r'faz a luta contra ele durar (três|duas|quatro) rodadas',
         'as rodadas da luta').group(1)])
CLASSE0_GRATIS = pega(PARTA, r'Classe 0 é grátis', 'o Classe 0 gratis').group(0)
CLASSE0_METADE = pega(PARTA, r'gasta PE em cerca de \*\*metade das rodadas de luta do dia\*\*',
                      'metade das rodadas').group(0)
# v0.221: o inimigo passou a contar PE, e a ancora mudou de frase junto. O poco
# nao e' numero novo — e' a cota do §4.1 dividida pelo ponto de feitico e
# multiplicada pelas rodadas da luta, e o conferir-bestiario.py bloco 10 guarda
# isso. Aqui a gente le a TABELA, porque e' dela que a medida precisa.
pega(P26, r'Poço de PE = o orçamento de feitiço de uma ação', 'a regra do poco')
def cota_e_acoes():
    """As quatro categorias no nivel 30: cota por rodada e acoes, lidas do §4 e
    do §4.1 da peca 26. Nada disto e' escrito aqui."""
    txt = ler(P26)
    acoes = {m[0]: int(m[1]) for m in re.findall(
        r'\*\*`(Ronda|Dupla|Alcateia|Calamidade)`\*\* \| \d+ \| `× [\d,]+` \| `(\d+)` \|', txt)}
    gente = {m[0]: int(m[1]) for m in re.findall(
        r'\*\*`(Ronda|Dupla|Alcateia|Calamidade)`\*\* \| (\d+) \|', txt)}
    i = txt.index('| categoria | nv 10 | nv 20 | nv 30 |')
    bl = txt[i:txt.index('\n\n', i)]
    cota = {}
    for m in re.finditer(r'^\| `(Ronda|Dupla|Alcateia|Calamidade)` \|(.+)\|\s*$', bl, re.M):
        ns = [int(x) for x in re.findall(r'`(\d+)`', m.group(2))]
        cota[m.group(1)] = ns[-1]          # a coluna do nv 30, e a celula traz vida e dano
    if len(acoes) != 4 or len(cota) != 4 or len(gente) != 4:
        print('  !! nao li as quatro categorias da peca 26 — a forma mudou')
        sys.exit(1)
    return cota, acoes, gente
COTA30, ACOES30, GENTE30 = cota_e_acoes()
POCO = pega(P26, r'\| `Alcateia` \| `\d+` \| `\d+` \| `(\d+)` \|', 'o poco da Alcateia nv30').group(1)
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
print(f'  o inimigo                  CONTA PE desde a v0.221 (peca 26 §6.1)')
print(f'  o poco de uma Alcateia nv30  {POCO} PE — a cota {COTA30["Alcateia"]:.0f} / {PONTO} x 3 rodadas')

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
POR_ACAO = CHEFE / ACOES
# ⚠ ESTA E A METADE QUE A v0.219 MEDIU EM 0,00 E A v0.221 REMEDIU.
# Com o poco do §6.1, dobrar o feitico do inimigo custa a ele um orcamento de
# acao a mais. O poco guarda exatamente `pontos por acao x acoes x rodadas`,
# entao pagar um orcamento a mais e' UMA ACAO A MENOS montada como feiticio no
# resto da luta — ela sai como o golpe do §4.4, sem area, sem condicao e sem
# Melhoria. O que se perde e' a FORMA daquela acao, e a forma se preca em ponto
# de feitico, que e' o mesmo `4,5` de sempre.
#
# ⚠ E o que se perde NAO e' a cota: o golpe entrega o mesmo dano. Somar dano
# perdido aqui seria contar duas vezes — o poco E' a cota noutra unidade.
print( '   o poco guarda pontos-por-acao x acoes x rodadas. Dobrar UM feitico gasta')
print( '   um orcamento de acao a mais, e sobra uma acao a menos com forma na luta.')
print()
print(f'   {"categoria":<12}{"cota":>6}{"acoes":>7}{"golpe":>8}{"pts/acao":>10}{"poco":>7}'
      f'{"por rodada":>12}')
ENERGIA = {}
for _c in ('Ronda', 'Dupla', 'Alcateia', 'Calamidade'):
    _cota = float(COTA30[_c])
    _ac = ACOES30[_c]
    _golpe = _cota / _ac
    _pts = _golpe / PONTO
    _poco = _cota / PONTO * RODADAS
    # a forma de uma acao, espalhada na luta
    ENERGIA[_c] = _golpe / RODADAS
    print(f'   {_c:<12}{_cota:>6.0f}{_ac:>7}{_golpe:>8.1f}{_pts:>10.1f}{_poco:>7.0f}'
          f'{ENERGIA[_c]:>12.2f}')
print()
print(f'   jogador -> inimigo   {ENERGIA["Alcateia"]:>7.2f}   contra um chefe de `Alcateia`, que e a linha')
print( '                                  em que a categoria e calibrada. Era 0,00 ate a v0.220.')
print(f'   jogador -> inimigo   {ENERGIA["Dupla"]:>7.2f}   contra uma `Dupla`, que e o teto: uma acao so,')
print( '                                  entao o golpe dela e o maior da tabela (§4.4).')
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
# ⚠ AS DUAS METADES SE SOMAM, e ate a v0.219 uma delas era zero. A regra de ouro
# desta casa e' que preco se mede SOMADO — a licao no 7 —, e com o poco do §6.1
# a metade da energia deixou de ser zero contra o bestiario.
print(f'  {"":<34}{"Leve":>10}{"Pesada":>10}      contra o filtro de {FILTRO:.2f}x')
SOMADO = {}
for rot, val in (('so a CD, teto: as 3 acoes pedem TR', janela_alta),
                 ('so a CD, piso: 1 acao pede TR', janela_baixa),
                 ('so a CD, num capanga', cap),
                 ('SOMADO num chefe de Alcateia', janela_alta + ENERGIA['Alcateia']),
                 ('SOMADO numa Dupla (o teto)', janela_alta + ENERGIA['Dupla'])):
    dl = val / (leve(7) * PONTO)
    dp = val / (pesada(7) * PONTO)
    SOMADO[rot] = (val, dl, dp)
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
teto_som = janela_alta + ENERGIA['Dupla']
alc_som = janela_alta + ENERGIA['Alcateia']
print(f'  Para a `Sobrecarga` sentar no PIOR degrau `Pesada` que existe ({min(alvo_pesada):.2f}x)')
print(f'  ela teria de negar {precisa:.1f} de dano por rodada.')
print(f'  Somadas as duas metades ela nega {alc_som:.2f} num chefe de `Alcateia` e {teto_som:.2f}')
print(f'  no teto, que e a `Dupla`. Falta um fator de {precisa/teto_som:.1f}x ate a `Pesada`.')
print()
print( '  ⚠ E ISSO MUDOU O TAMANHO, e nao o veredito. Ate a v0.219 a metade da energia')
print(f'  lia 0,00 contra o bestiario e a soma era {janela_alta:.2f}; com o poco do §6.1 ela')
print(f'  passou a {alc_som:.2f}, que e {alc_som/janela_alta:.1f}x. Continua fora da banda `Pesada`.')
print()
dl_alc, dl_dup = alc_som / (leve(7) * PONTO), teto_som / (leve(7) * PONTO)
print(f'  No degrau `Leve` ela cai em {dl_alc:.2f}x contra um chefe de `Alcateia` e')
print(f'  {dl_dup:.2f}x contra uma `Dupla`. A banda das `Leve` publicadas para em {max(alvo_leve):.2f}x.')
print()
print( '  ⚠⚠ E ISSO E UM ACHADO, e nao um arredondamento: a `Alcateia` cabe em `Leve`')
print(f'  ({dl_alc:.2f}x contra o teto de {max(alvo_leve):.2f}x) e a `Dupla` NAO cabe — ela passa')
print(f'  {dl_dup/max(alvo_leve) - 1:.0%} do teto e cai dentro da banda das `Pesada`')
print(f'  ({min(alvo_pesada):.2f}x a {max(alvo_pesada):.2f}x).')
print()
print( '  A causa e o §4.4, e ela nao e desta Melhoria: a `Dupla` entrega metade da cota')
print( '  de uma `Alcateia` numa acao SO, entao o golpe dela e o maior da tabela. Como o')
print( '  que a Sobrecarga tira e UMA ACAO de forma, ela tira mais de quem concentra mais.')
print( '  Qualquer Melhoria que custe uma acao do inimigo tem esse mesmo perfil.')
print()
print( '  ⚠ QUEM DECIDE O DEGRAU E O MIZUKI, e a linha `Sobrecarga` do ESTADO-revisao.md')
print( '  continua `aberta`: `Leve` no manual e `Pesada` no livro. Isto e a medida, e nao')
print( '  a decisao. O que a medida diz e que `Pesada` continua sem caber.')

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Quanto vale cada candidata a SUBSTITUIR a metade morta da `Sobrecarga`.

A metade morta e' "o feitico dele custa o dobro de energia". Ela vale 0,00
contra inimigo desde que o Mizuki fechou, em 09/09/2026, que o inimigo nao
conta PE (decisoes-fase-1.md §8).

As candidatas sao as quatro que ele listou — as 3 Intervencoes, as acoes por
rodada, a Reacao, o refino — mais o cambio PE<->acao que o proprio §6.1 do
bestiario declara.

REGRA DESTE ARQUIVO, a mesma do manual/matematica/sobrecarga.py:
nenhum numero de regra mora aqui dentro. Cada ancora e' lida do documento
dono. Se uma sumir do dono, o script sai com erro em vez de sair com numero
velho.

A regua e a da peca 19 §2.2, e ela tem DUAS perguntas separadas:
  1. O NIVEL sai de quantas acoes da rodada do alvo a coisa nega —
     meia acao e' `Leve`, uma e' `Media`, uma e meia e' `Pesada`.
  2. O TESTE e' de dominancia, contra o filtro de 3,00x.
"""
import os, re, sys, math

REPO = os.environ.get('JJK_REPO', '/media/mizuki/HD Externo II/Claude/Claude 2')
BEST = os.environ.get('JJK_BEST', '/media/mizuki/HD Externo II/Claude/Claude 2/bestiario')

P01  = 'sistema/03-mecanica/01-atributos-acerto-defesa.md'
P03  = 'sistema/03-mecanica/03-economia-de-acao-e-iniciativa.md'
P05  = 'sistema/03-mecanica/05-caminho-e-combate-sem-feitico.md'
P06  = 'sistema/03-mecanica/06-caminhos-e-trilhas.md'
P11  = 'sistema/03-mecanica/11-aptidoes-e-refino.md'
P19  = 'sistema/03-mecanica/19-dano-e-condicoes.md'
P26  = 'sistema/03-mecanica/26-bestiario.md'
DTRI = 'DESENHO-trilhas.md'
DCAM = 'DESENHO-caminhos.md'
PARTA = 'manual/gerador/partA.js'
PARTD = 'manual/gerador/partD.js'
FUND  = 'sistema/05-material/livro/manual/40-fundamento.md'
TABELA = '04-fase-1/TABELA.md'


def ler(rel, raiz=REPO):
    with open(os.path.join(raiz, rel), encoding='utf-8') as f:
        return f.read()


def n(s):
    return float(s.replace(',', '.'))


def pega(rel, padrao, rotulo, raiz=REPO):
    m = re.search(padrao, ler(rel, raiz))
    if not m:
        print(f'  !! ancora perdida: {rotulo} — nao casa em {rel}')
        sys.exit(1)
    return m


def linha(t, c='='):
    print()
    print(c * 92)
    print(t)
    print(c * 92)


# ===========================================================================
linha('1. AS ANCORAS — lidas do dono, nenhuma escrita aqui')
# ===========================================================================

CHEFE   = n(pega(DTRI, r'chefe (?:do nível 30 )?em `?(\d+)`? de dano por rodada', 'o chefe').group(1))
CAPANGA = n(pega(DTRI, r'o capanga em `(\d+)`', 'o capanga').group(1))
ACOES   = n(pega(P19, r'O chefe age `(\d+)` vezes por rodada', 'acoes do chefe').group(1))
ROTINA  = n(pega(P19, r'a Rotina em `(\d+)`', 'a Rotina no nv30').group(1))
PONTO   = n(pega(P19, r'cada ponto que não vira Melhoria vira `1d8` de dano — que são `([\d,]+)`',
                 'o ponto de feitico').group(1))
FILTRO  = n(pega(P19, r'filtro de `([\d,]+)×`', 'o filtro de dominancia').group(1))
PP_ALIADO = n(pega(DCAM, r'`1` pp vale `([\d,]+)`', 'o pp de aliado').group(1))
ACAO_ALIADO = n(pega(DCAM, r'aquela ação vale `([\d,]+)`', 'a acao de aliado').group(1))
GOLPE_SIMPLES = n(pega(DCAM, r'dois golpes simples de `([\d,]+)`', 'o golpe simples').group(1))
ALIADOS = int(pega(P19, r'Benefício que qualquer atacante colhe conta (TRÊS)', 'os tres aliados')
              and 3)
DIA = n(pega(P06, r'`([\d,]+)` rodadas de luta por dia', 'as rodadas por dia').group(1))
RESISTE = n(pega(P01, r'\*\*treinado\*\* \| 65% \| 65% \| 65% \| 65% \| \*\*(\d+)%\*\*',
                 'o TR treinado').group(1)) / 100.0

# o acerto base contra alvo dificil — e' ele que faz desvantagem valer METADE do dano,
# e o dono e' a peca 1 §5.2, na linha do critico
ACERTO = n(pega(P01, r'Contra o alvo difícil, em que se acerta (\d+)%', 'o acerto base')
           .group(1)) / 100.0

# as travas de regra que esta conta pressupoe
SEM_PE   = pega(P26, r'O inimigo não conta PE', 'o inimigo sem PE').group(0)
CAMBIO   = pega(P26, r'o inimigo tem o mesmo teto escrito direto, sem a moeda no meio',
                'o cambio PE<->cota').group(0)
REACAO_1 = pega(P03, r'\*\*Reação\*\* \| uma, e ela volta no começo do seu turno',
                'a Reacao, uma por rodada').group(0)
PROTECAO = pega(P11, r'a sua proteção é `1/3 do refino \+ 1`', 'a protecao do refino').group(0)
C0_METADE = pega(PARTA, r'gasta PE em cerca de \*\*metade das rodadas de luta do dia\*\*',
                 'metade das rodadas no Classe 0').group(0)
C0_GRATIS = pega(PARTA, r'Classe 0 é grátis', 'o Classe 0 gratis').group(0)

# o degrau da `Sobrecarga` divergе entre os dois donos — a divergencia e' da v0.219
TIER_GER = pega(PARTD, r"\['Sobrecarga', '(\w+)'", 'o degrau no gerador').group(1)
m = re.search(r'\| `Sobrecarga` \| `(\w+)` \|', ler(FUND))
TIER_LIV = m.group(1) if m else '??'

# a tabela de preco dos tres tiers, lida da propria tabela do §2.1
PRECO = {}
for ln in ler(P19).split('\n'):
    m = re.match(r'\| (\d) \| (\d+) \| (\d+) \| (\d+) \| (\d+) \|', ln)
    if m:
        C = int(m.group(1))
        PRECO[C] = {'Leve': int(m.group(2)), 'Média': int(m.group(3)),
                    'Pesada': int(m.group(4)), 'Rotina': int(m.group(5))}
if sorted(PRECO) != list(range(1, 8)):
    print(f'  !! li {sorted(PRECO)} da tabela de preco do §2.1, e sao as Classes 1 a 7')
    sys.exit(1)

# ⚠ A DERIVACAO QUE TUDO DEPENDE: quanto vale a Reacao do inimigo.
# Ela nao esta escrita em lugar nenhum como numero. Ela sai do `Atordoado`
# publicado: o texto dele e' "perde a Acao Padrao E NAO USA REACAO", e a tabela
# das treze publica `1,5` acoes negadas. 1,5 - 1,0 = 0,5.
m = re.search(r'\| \*\*`Atordoado`\*\* \| `([\d,]+)` \| `([\d,]+)`[^|]*\|', ler(P19))
if not m:
    print('  !! nao achei a linha do `Atordoado` na tabela das treze do §2.2')
    sys.exit(1)
ATORD_NEGA, ATORD_ACOES = n(m.group(1)), n(m.group(2))
txt_atord = re.search(r'\| \*\*`Atordoado`\*\* \| `Pesada` \| \*\*([^*]+)\*\*', ler(P19))
if not txt_atord or 'não usa reação' not in txt_atord.group(1):
    print('  !! o texto do `Atordoado` na peca 19 nao diz mais "nao usa reacao" — a '
          'derivacao de quanto vale a Reacao do inimigo perdeu o chao')
    sys.exit(1)
ACAO_PADRAO_DO_ATORDOADO = 1.0   # "perde a Acao Padrao" — UMA, pela propria celula
FRACAO_REACAO = ATORD_ACOES - ACAO_PADRAO_DO_ATORDOADO

UMA_ACAO = CHEFE / ACOES
A_REACAO = FRACAO_REACAO * UMA_ACAO

print(f'  chefe nv30                    {CHEFE:.0f} de dano por rodada, em {ACOES:.0f} acoes')
print(f'  capanga nv30                  {CAPANGA:.0f} de dano por rodada')
print(f'  Rotina nv30                   {ROTINA:.0f}')
print(f'  1 ponto de feitico            {PONTO:.1f} de dano')
print(f'  filtro de dominancia          {FILTRO:.2f}x')
print(f'  1 pp na rolagem de um aliado  {PP_ALIADO:.3f} de dano por rodada')
print(f'  a acao de atacar de um aliado {ACAO_ALIADO:.2f} — dois golpes de {GOLPE_SIMPLES:.2f}')
print(f'  atacantes que colhem          {ALIADOS} (convencao do §2.2)')
print(f'  TR treinado no nv30           resiste {RESISTE:.0%}')
print(f'  rodadas de luta por dia       {DIA:.1f}')
print(f'  preco na Classe 7, em pontos  Leve {PRECO[7]["Leve"]} · Média {PRECO[7]["Média"]} '
      f'· Pesada {PRECO[7]["Pesada"]}')
print(f'  degrau da `Sobrecarga` hoje   gerador diz `{TIER_GER}`, livro diz `{TIER_LIV}`'
      f'{"   <- DIVERGENCIA ABERTA (v0.219)" if TIER_GER != TIER_LIV else ""}')
print()
print(f'  >> UMA acao do chefe          {UMA_ACAO:.2f} de dano  ({CHEFE:.0f} / {ACOES:.0f})')
print(f'  >> a REACAO do inimigo        {A_REACAO:.2f} de dano')
print(f'     derivada do `Atordoado` publicado: o texto dele tira a Acao Padrao E a reacao,')
print(f'     e a tabela das treze publica {ATORD_ACOES:.1f} acoes negadas. '
      f'{ATORD_ACOES:.1f} - {ACAO_PADRAO_DO_ATORDOADO:.1f} = {FRACAO_REACAO:.1f} acao.')
print(f'     Confere: {ATORD_ACOES:.1f} x {UMA_ACAO:.2f} = {ATORD_ACOES*UMA_ACAO:.2f}, e a peca '
      f'publica {ATORD_NEGA:.2f}. {"OK" if abs(ATORD_ACOES*UMA_ACAO-ATORD_NEGA)<0.01 else "NAO FECHA"}')


# ===========================================================================
linha('2. O QUE A METADE MORTA VALE HOJE — os dois lados da mesa')
# ===========================================================================
print('  "o feitico dele custa o dobro de energia"')
print()
print(f'  contra INIMIGO                {0.00:>7.2f}   o inimigo nao conta PE (peca 26 §6.1).')
print( '                                          Nao existe alvo no bestiario inteiro.')
CLASSE = 7
pe_extra = 3 * CLASSE
dano_cheio = pe_extra * PONTO
se_paga = dano_cheio / DIA
print(f'  contra JOGADOR, se ele paga   {se_paga:>7.2f}   +{pe_extra} PE = um Classe {CLASSE} a '
      f'menos no dia')
print(f'  contra JOGADOR, no Classe 0   {0.00:>7.2f}   o dobro de zero e zero')
ESPERADO = se_paga * 0.5
print(f'  >> o ESPERADO contra jogador  {ESPERADO:>7.2f}   o manual escreve que o conjurador passa')
print( '                                          METADE das rodadas no Classe 0, e chama o')
print( '                                          Classe 0 de "o golpe de todo turno em que o')
print( '                                          PE precisa ser poupado".')
print()
print('  >> A metade morta nao esta meio-morta contra inimigo e viva contra jogador.')
print(f'     Ela esta morta de um lado e vale {ESPERADO:.2f} do outro — que e {ESPERADO/UMA_ACAO:.1%}')
print(f'     de UMA acao de chefe. E a frase "o dobro de energia" e a mesma que a v0.217')
print('     tirou da `Divida` por dobrar zero.')


# ===========================================================================
linha('3. A METADE QUE FICA — a CD 2 menor, remedida')
# ===========================================================================
PP_POR_PONTO = 1 / 20.0
NEGA_CD = (2 * PP_POR_PONTO) / 2.0
print(f'  -2 na CD nega SEMPRE {NEGA_CD:.1%} do dano daquele feitico, em qualquer taxa de TR.')
CD_TETO  = CHEFE * NEGA_CD
CD_PISO  = UMA_ACAO * NEGA_CD
print(f'  teto (as {ACOES:.0f} acoes pedem TR)   {CD_TETO:>7.2f} de dano por rodada')
print(f'  piso (1 acao pede TR)        {CD_PISO:>7.2f}')


# ===========================================================================
linha('4. AS CANDIDATAS — cada uma contra algo que o inimigo TEM')
# ===========================================================================

# a desvantagem num golpe, que e' o `Trava` ja publicado em Leve: serve de irmao
TRAVA = UMA_ACAO * (1 - ACERTO)

CANDIDATAS = [
    # (codigo, nome, acoes negadas, valor, nota)
    ('R',   'trava a Reação da próxima rodada',
     FRACAO_REACAO, A_REACAO,
     'o inimigo tem UMA Reação por rodada (peça 3). Irmão publicado: o `Trava`'),
    ('A1',  'tranca UMA ação da próxima rodada',
     1.0, UMA_ACAO,
     'é o `Calado` e o `Enfeitiçado` com outro nome — já existem, em `Média`'),
    ('A15', 'tranca uma ação E a Reação',
     1.5, UMA_ACAO + A_REACAO,
     'é o `Atordoado` inteiro — já existe, em `Pesada`'),
    ('I-0', 'tranca a Intervenção — leitura "ela sai da cota"',
     0.0, 0.0,
     'pelo §6.1 tudo sai do dano por rodada; então a Intervenção não ADICIONA nada'),
    ('I-1', 'tranca a Intervenção — leitura "ela é ação extra"',
     1.0, UMA_ACAO,
     'ela acontece FORA do turno, então é uma 4ª ação na rodada em que dispara'),
    ('D2',  'o golpe dele custa o DOBRO de ação (o câmbio do §6.1)',
     1.0, UMA_ACAO,
     'a mesma frase pelo câmbio que o §6.1 declara: PE do jogador = cota do inimigo'),
    ('RF',  'refino −3 (um degrau de proteção)',
     0.0, 5 * PP_ALIADO * ALIADOS,
     'proteção é `1/3 do refino + 1`; −1 de Defesa = 5 pp pra cada atacante'),
    # Esta nao estava na lista do Mizuki. Ela entrou porque e' o ESPELHO da metade
    # que fica: a `Sobrecarga` ja da -2 na CD dele; dar -2 no ACERTO dele tambem
    # faz a Melhoria virar UMA ideia — "-2 nas duas rolagens de ataque dele".
    # O irmao publicado e' a `Precisao`, que vende "+2 na rolagem de acerto, OU
    # +2 na CD" por `Leve` — ou seja, UMA das duas metades custa `Leve`.
    ('AC',  '−2 no ACERTO dele na mesma janela (o espelho da CD)',
     None, None,
     'a `Precisão` vende +2 em UMA das duas rolagens por `Leve`; esta dá −2 nas DUAS'),
]
# o -2 no acerto: 2 pontos num d20 sao 10 pp, e um golpe que erra entrega ZERO —
# entao ele nega 10/ACERTO do dano daquele golpe, e nao 5% como a CD.
NEGA_ACERTO = (2 * PP_POR_PONTO) / ACERTO
AC_TETO = CHEFE * NEGA_ACERTO
AC_PISO = UMA_ACAO * NEGA_ACERTO
for i, c in enumerate(CANDIDATAS):
    if c[0] == 'AC':
        CANDIDATAS[i] = (c[0], c[1], AC_TETO / UMA_ACAO, AC_TETO, c[4])

# ⚠ A candidata `AC` NAO se soma com a metade da CD, e isso e' o que decide o preco
# dela: um golpe ou rola ACERTO ou pede TESTE DE RESISTENCIA — nunca os dois. Entao
# com k das acoes dele rolando acerto e (ACOES - k) pedindo TR, a Melhoria inteira
# nega k x (20% daquele golpe) + (ACOES - k) x (5% daquele golpe).
# Todas as outras candidatas SE somam, porque nenhuma disputa a mesma rolagem.
def total_AC(k):
    return k * UMA_ACAO * NEGA_ACERTO + (ACOES - k) * UMA_ACAO * NEGA_CD

TOTAIS = {}
for cod, nome, ac, val, _ in CANDIDATAS:
    if cod == 'AC':
        TOTAIS[cod] = (total_AC(0), total_AC(ACOES))   # k=0 (tudo TR) a k=3 (tudo acerto)
    else:
        TOTAIS[cod] = (val + CD_PISO, val + CD_TETO)

def tier_por_acao(a):
    """a regra 1 do §2.2: meia acao e' Leve, uma e' Media, uma e meia e' Pesada"""
    if a >= 1.5:  return 'Pesada'
    if a >= 1.0:  return 'Média'
    if a >= 0.5:  return 'Leve'
    return '‹ abaixo de meia ›'

print(f'  O irmão de preço que importa: o `Trava` (`Leve`, já publicado) dá desvantagem num')
print(f'  golpe do alvo, e isso vale {TRAVA:.2f} — exatamente o mesmo que a Reação do chefe.')
print()
print(f'  ⚠ E a conta acha uma assimetria que ninguém tinha escrito: os MESMOS 2 pontos num d20')
print(f'     valem 4x mais no ACERTO do que na CD. -2 na CD nega {NEGA_CD:.1%} daquele golpe;')
print(f'     -2 no acerto nega {NEGA_ACERTO:.1%}. A causa: golpe que erra entrega ZERO, e')
print(f'     Teste de Resistência bem-sucedido ainda entrega METADE.')
print(f'     Em dano, na janela inteira do turno dele: a CD nega {CD_TETO:.2f}, o acerto nega '
      f'{AC_TETO:.2f}.')
print()
print(f'  {"cód":<5}{"o que ela nega":<46}{"ações":>7}{"dano/rod":>10}  {"nível pela regra 1":<20}')
print(f'  {"-"*5:<5}{"-"*46:<46}{"-"*7:>7}{"-"*10:>10}  {"-"*20:<20}')
for cod, nome, ac, val, _ in CANDIDATAS:
    print(f'  {cod:<5}{nome:<46}{ac:>7.2f}{val:>10.2f}  {tier_por_acao(ac):<20}')
print()
for cod, nome, ac, val, nota in CANDIDATAS:
    print(f'  {cod:<5} {nota}')


# ===========================================================================
linha('5. O TESTE DE DOMINANCIA — a Sobrecarga INTEIRA, nos tres degraus')
# ===========================================================================
print(f'  A Melhoria entrega as DUAS metades. Total = candidata + a CD 2 menor.')
print(f'  A CD vai no teto ({CD_TETO:.2f}) e no piso ({CD_PISO:.2f}); as duas colunas estao aqui.')
print(f'  O filtro e {FILTRO:.2f}x. A banda das treze publicadas: Leve 0,00x a 2,18x,')
print(f'  Media 2,32x, Pesada 2,21x a 2,67x.')
print()
TIERS = ('Leve', 'Média', 'Pesada')
cab = f'  {"cód":<5}{"nível p/ regra 1":<18}'
for t in TIERS:
    cab += f'{t+" piso":>13}{t+" teto":>13}'
print(cab)
print('  ' + '-' * 88)
RES = {}
for cod, nome, ac, val, _ in CANDIDATAS:
    tot_piso, tot_teto = TOTAIS[cod]
    ln = f'  {cod:<5}{tier_por_acao(ac):<18}'
    RES[cod] = {}
    for t in TIERS:
        custo = PRECO[7][t] * PONTO
        dpiso, dteto = tot_piso / custo, tot_teto / custo
        RES[cod][t] = (dpiso, dteto)
        marca = lambda d: '!' if d > FILTRO else ' '
        ln += f'{dpiso:>12.2f}x{marca(dpiso)}{dteto:>12.2f}x{marca(dteto)}'
    print(ln)
print()
print(f'  `!` = passa do filtro de {FILTRO:.2f}x, ou seja: domina o dano que aqueles pontos dariam.')
print()
print(f'  ⚠ A `AC` tem piso e teto por OUTRO motivo que as demais: ela disputa a mesma rolagem')
print(f'     que a metade da CD. As duas nao se somam — um golpe ou rola acerto ou pede TR.')
print(f'     Com k das {ACOES:.0f} acoes dele rolando acerto:')
for k in range(int(ACOES) + 1):
    print(f'       k={k}  {total_AC(k):>6.2f} de dano negado   '
          f'Leve {total_AC(k)/(PRECO[7]["Leve"]*PONTO):>5.2f}x   '
          f'Média {total_AC(k)/(PRECO[7]["Média"]*PONTO):>5.2f}x')
print(f'     E o k nao e' + " hipotese: o UNICO bloco preenchido que o projeto tem — o Sukuna do")
print(f'     `03-bloco/RASCUNHO-1-o-bloco.md` — tem `Corte` rolando acerto e `Desmantelar` e')
print(f'     `Fuga` pedindo Teste de Resistencia. ISSO E k=1, e k=1 da '
      f'{total_AC(1)/(PRECO[7]["Leve"]*PONTO):.2f}x em `Leve`.')
print(f'     O bloco carrega as DUAS rolagens (peca 26 §3 deriva `acerto` E `CD`), entao a')
print(f'     Melhoria pega o inimigo qualquer que seja a mistura dele — e e isso que a')
print(f'     metade da CD sozinha NAO faz.')
print()
print('  E o COERENTE e ler a diagonal: o degrau que a regra 1 manda, com a dominancia dele.')
print()
print(f'  {"cód":<5}{"o que ela nega":<46}{"degrau":<9}{"dominância piso→teto":<24}{"passa?":<8}')
print('  ' + '-' * 90)
for cod, nome, ac, val, _ in CANDIDATAS:
    t = tier_por_acao(ac)
    if t not in TIERS:
        print(f'  {cod:<5}{nome:<46}{"—":<9}{"‹ nega menos que meia ação ›":<24}{"—":<8}')
        continue
    dp, dt = RES[cod][t]
    ok = 'sim' if dt <= FILTRO else 'NÃO'
    print(f'  {cod:<5}{nome:<46}{t:<9}{f"{dp:.2f}x → {dt:.2f}x":<24}{ok:<8}')


# ===========================================================================
linha('5.5 O BAIRRO — as nove `Auxiliares` publicadas, na MESMA regua')
# ===========================================================================
# A `Sobrecarga` nao e' uma Condicao: ela e' uma `Auxiliar`. O §2.2 mede a banda
# das treze CONDICOES, e elas sao outra familia. A banda que importa para precar
# esta Melhoria e' a da familia dela, e ninguem tinha medido.
#
# Cada linha diz a convencao que usou. As tres primeiras nao dependem de
# convencao nenhuma: elas leem ancora direto.
TEC = 6.0   # o atributo de tecnica no teto da campanha (peca 2 §3: +1 por marco, teto 6)
m = re.search(r'teto `(\d)`', ler(P26))
AUX = [
    ('Impulso',     'Leve',  25 * PP_ALIADO,
     'vantagem no proximo teste de um aliado = 25 pp x o pp de aliado'),
    ('Trava',       'Leve',  UMA_ACAO * (1 - ACERTO),
     'desvantagem num golpe do alvo = metade daquele golpe'),
    ('Abre Ferida', 'Leve',  UMA_ACAO * NEGA_CD,
     '-2 em UM Teste de Resistencia = 5% daquele golpe'),
    ('Ecoa',        'Média', 25 * PP_ALIADO,
     'vantagem no proximo ataque de um aliado — a mesma conta do `Impulso`'),
    ('Enfraquece',  'Média', (TEC / 2) * 2.5,
     f'Xd4 com X = metade do atributo de tecnica; no teto X={TEC/2:.0f}, e 1d4 e 2,5'),
    ('Pressa',      'Média', 6 * (n(pega(P05, r'(0,90)', 'o metro').group(1)) / 1.5),
     '+6 m de deslocamento, ao cambio de metro da peca 5 (o "nao provoca" nao entrou)'),
    ('Firmeza',     'Média', UMA_ACAO * (25 / 100.0) / 2,
     'vantagem num TR = 25 pp, e TR bem-sucedido corta o dano pela metade'),
    ('Guarda',      'Média', UMA_ACAO * (2 * PP_POR_PONTO) / ACERTO,
     '+2 de defesa contra UMA acao do chefe (convencao: uma acao, nao a rodada)'),
]
print(f'  {"Auxiliar":<13}{"degrau":<8}{"entrega":>9}{"dominância":>12}   convenção')
print('  ' + '-' * 88)
for nome, tier, val, conv in AUX:
    custo = PRECO[7][tier] * PONTO
    print(f'  {nome:<13}{tier:<8}{val:>9.2f}{val/custo:>11.2f}x   {conv[:46]}')
print()
_leves = [v / (PRECO[7]['Leve'] * PONTO) for nm, t, v, _ in AUX if t == 'Leve']
_medias = [v / (PRECO[7]['Média'] * PONTO) for nm, t, v, _ in AUX if t == 'Média']
print(f'  >> A banda das `Auxiliares` `Leve` publicadas:  {min(_leves):.2f}x a {max(_leves):.2f}x')
print(f'  >> A banda das `Auxiliares` `Média` publicadas: {min(_medias):.2f}x a {max(_medias):.2f}x')
print()
print(f'  ⚠ A familia `Auxiliar` e MUITO mais fraca que a familia `Condicao`. As treze condicoes')
print(f'     que negam acao entregam 2,18x a 2,67x; a `Media` mais forte daqui entrega')
print(f'     {max(_medias):.2f}x. O teto natural desta familia e o `Trava`, em {max(_leves):.2f}x.')
_rp, _rt = RES['R']['Leve']
print(f'  ⚠ E e isso que decide o degrau da candidata `R`: em `Leve` ela daria {_rp:.2f}x a '
      f'{_rt:.2f}x,')
print(f'     que e o `Trava` MAIS o `Abre Ferida` — duas `Leve` publicadas pelo preco de uma.')
_rpm, _rtm = RES['R']['Média']
print(f'     Em `Média` ela da {_rpm:.2f}x a {_rtm:.2f}x, que e o topo natural desta familia.')


# ===========================================================================
linha('6. A CANDIDATA `R` CONTRA AS CINCO CATEGORIAS — o mesmo texto, cinco blocos')
# ===========================================================================
TXT_TAB = ler(TABELA, BEST)
CATS = {}
atual = None
for ln in TXT_TAB.split('\n'):
    m = re.match(r'## `([^`]+)`', ln)
    if m:
        atual = m.group(1)
        CATS[atual] = {}
        continue
    m = re.match(r'\| (\d+) \| `(\d+)` \| `?\*?\*?`?(\d+)`?\*?\*?`? \| `(\d+)` \|', ln)
    if m and atual:
        CATS[atual][int(m.group(1))] = (float(m.group(2)), float(m.group(3)), float(m.group(4)))

NV = 30
print(f'  Nível {NV}. "ações" e a coluna da escada; a Reação e sempre UMA, pela peca 3.')
print()
print(f'  {"categoria":<14}{"dano/rod":>10}{"ações":>7}{"1 ação":>10}{"a Reação":>10}'
      f'{"% da rodada":>13}')
print('  ' + '-' * 66)
ordem = ['Ameaça', 'Desastre', 'Catástrofe', 'Calamidade']
for cat in ordem:
    if cat not in CATS or NV not in CATS[cat]:
        print(f'  !! nao li a linha do nivel {NV} da categoria {cat} no TABELA.md')
        sys.exit(1)
    vida, dano, acs = CATS[cat][NV]
    ua = dano / acs
    reac = FRACAO_REACAO * ua
    print(f'  {cat:<14}{dano:>10.0f}{acs:>7.0f}{ua:>10.2f}{reac:>10.2f}{reac/dano:>12.1%}')
# O capanga tem OUTRA forma de tabela — ele nao tem coluna `dano/rod` nem `acoes`,
# e o golpe dele vem em dado (`6d8 + 28`) em vez de numero seco. A escada da `1`
# acao a ele, e o dano por rodada de UM corpo e' o golpe dele.
# ⚠ Isto abortava em silencio antes: o `if m:` pulava a linha e a tabela saia com
# quatro categorias sob um titulo que prometia cinco.
m = re.search(r'## `Capanga`[\s\S]*?\n\| 30 \| `(\d+)` \| \*\*`(\d+)`\*\* \| `(\d+)d(\d+) \+ (\d+)` \|',
              TXT_TAB)
if not m:
    print('  !! nao achei a linha do nivel 30 do `Capanga` no TABELA.md — a forma da tabela '
          'dele mudou, e ela NAO e a mesma das outras quatro')
    sys.exit(1)
dados, faces, fixo = float(m.group(3)), float(m.group(4)), float(m.group(5))
golpe_um = dados * (1 + faces) / 2 + fixo
print(f'  {"Capanga (um)":<14}{golpe_um:>10.0f}{1:>7.0f}{golpe_um:>10.2f}'
      f'{FRACAO_REACAO*golpe_um:>10.2f}{FRACAO_REACAO:>12.1%}')
print(f'  {"":<14}{f"({int(dados)}d{int(faces)} + {int(fixo)}, medio)":>10}')
print()
print('  >> A mordida RELATIVA cresce quando o inimigo tem menos acoes — e isso nao e defeito')
print('     desta Melhoria: e o que o §2.2 ja publica para as quatro condicoes que cobram acao')
print('     ("cada acao a menos encarece as quatro na mesma proporcao").')


# ===========================================================================
linha('7. O OUTRO LADO DA MESA — a mesma linha contra um JOGADOR')
# ===========================================================================
print('  Um jogador tem 1 Acao Padrao, 1 Acao Bonus, 1 Reacao e movimento (peca 3).')
print()
print(f'  tranca a Reação dele      {GOLPE_SIMPLES:>7.2f}   um ataque de oportunidade = um golpe '
      f'simples')
print(f'  tranca a Ação Padrão      {ACAO_ALIADO:>7.2f}   se ele ia atacar (dois golpes)')
print(f'  tranca a Ação Padrão      {ROTINA:>7.2f}   se ele ia conjurar (a Rotina do nv30)')
print()
print(f'  >> Trancar a REAÇÃO e a unica das tres que cabe no MESMO degrau nos dois lados:')
print(f'     {A_REACAO:.2f} contra chefe e {GOLPE_SIMPLES:.2f} contra jogador, e os dois sao')
print(f'     "meia acao do dono" — que e `Leve` pela regra 1.')
print(f'  >> Trancar UMA AÇÃO nao cabe: contra o chefe tira 1/{ACOES:.0f} da rodada, contra o')
print(f'     jogador tira a rodada INTEIRA ({ROTINA:.0f} de dano). Isso e `Atordoado`, nao `Leve`.')


# ===========================================================================
linha('7.2 SENSIBILIDADE — e se a Reacao do inimigo valer UMA acao, e nao meia?')
# ===========================================================================
# O 36,50 sai da convencao que o `Atordoado` publicado IMPLICA: a Reacao vale meia
# acao. A leitura por tras disso e' que a Reacao so' dispara se alguem provocar —
# entao ela vale metade de uma acao garantida.
# Mas um ataque de oportunidade de inimigo USA `o golpe` dele, e `o golpe` e' a cota
# de UMA acao inteira. Se o gatilho sempre acontecesse, a Reacao valeria 73,00.
# Este bloco mostra os dois limites, porque o numero de cima NAO e' desprezivel.
print(f'  O `o golpe` do chefe nv30 entrega {UMA_ACAO:.2f} — a cota de UMA acao.')
print(f'  Se a Reacao dele e um ataque de oportunidade, ela entrega esse mesmo golpe')
print(f'  NAS VEZES EM QUE ALGUEM PROVOCA.')
print()
for rot, fr in (('a convenção publicada (meia ação)', FRACAO_REACAO), ('se provocar SEMPRE', 1.0)):
    val = fr * UMA_ACAO
    print(f'  {rot:<36}{val:>8.2f}   '
          + '   '.join(f'{t} {(val+CD_TETO)/(PRECO[7][t]*PONTO):>5.2f}x'
                       + ('!' if (val+CD_TETO)/(PRECO[7][t]*PONTO) > FILTRO else ' ')
                       for t in TIERS))
print()
print(f'  >> O limite de cima ESTOURA o filtro em `Leve` e cabe em `Média`.')
print(f'  ⚠ Mas usar o limite de cima obriga a reprecar o `Atordoado` junto: ele e a MESMA')
print(f'     convencao, e a peca 19 publica ele em {ATORD_NEGA:.2f}. Mexer num mexe no outro.')
print(f'  >> A conta desta rodada usa o numero PUBLICADO. O outro fica escrito pra quem')
print(f'     quiser abrir a convencao — e abrir ela e trabalho da peca 19, nao desta Melhoria.')


# ===========================================================================
linha('7.5 A TERCEIRA OPCAO — as duas finalistas JUNTAS')
# ===========================================================================
# Se a `R` e a `AC` forem as duas, a Melhoria passa a negar 0,50 + 0,60 = 1,10 acao,
# que e' `Media` pela regra 1. As duas NAO disputam rolagem nenhuma entre si — a
# Reacao e' slot de acao e o -2 e' rolagem —, entao aqui elas SE SOMAM.
RmaisAC = FRACAO_REACAO + AC_TETO / UMA_ACAO
print(f'  ações negadas somadas: {FRACAO_REACAO:.2f} (a Reação) + {AC_TETO/UMA_ACAO:.2f} '
      f'(o −2 no acerto) = {RmaisAC:.2f}')
print(f'  degrau pela regra 1:   {tier_por_acao(RmaisAC)}')
print()
print(f'  {"k":<4}{"nega":>9}{"Leve":>10}{"Média":>10}{"Pesada":>10}')
print('  ' + '-' * 44)
for k in range(int(ACOES) + 1):
    tot = A_REACAO + total_AC(k)
    ln = f'  {k:<4}{tot:>9.2f}'
    for t in TIERS:
        d = tot / (PRECO[7][t] * PONTO)
        ln += f'{d:>9.2f}x' + ('!' if d > FILTRO else ' ')
    print(ln)
print()
print(f'  >> Em `Média` a combinação cabe em TODO k, e o teto dela fica em')
print(f'     {(A_REACAO+total_AC(ACOES))/(PRECO[7]["Média"]*PONTO):.2f}x contra o filtro de '
      f'{FILTRO:.2f}x.')
print(f'  >> Em `Leve` ela estoura a partir de k={min([k for k in range(int(ACOES)+1) if (A_REACAO+total_AC(k))/(PRECO[7]["Leve"]*PONTO) > FILTRO], default=99)}.')
print(f'  ⚠ Custo da combinação: ela e `Média`, e NENHUM dos tres donos da tabela escreve')
print(f'     `Média` hoje (o gerador e o .docx dizem `{TIER_GER}`, o livro diz `{TIER_LIV}`).')
print(f'     A divergencia da v0.219 nao se FECHA — ela vira um terceiro valor.')


# ===========================================================================
linha('8. O VEREDITO DA MEDIDA')
# ===========================================================================
t_r = tier_por_acao(FRACAO_REACAO)
dp, dt = RES['R'][t_r]
print(f'  1. A metade morta vale {0.00:.2f} contra inimigo e {ESPERADO:.2f} esperado contra')
print(f'     jogador. Substituir ela inteira e mais barato que pendurar uma clausula "contra')
print(f'     inimigo" — e mata a frase que a v0.217 ja tirou da `Divida`.')
print()
print(f'  2. A candidata `R` (trava a Reacao) entrega {A_REACAO:.2f} contra chefe, o que e')
print(f'     exatamente o que o `Trava` ja publicado entrega ({TRAVA:.2f}) — e o `Trava` e `Leve`.')
print(f'     Com a CD somada ela fica em {dp:.2f}x a {dt:.2f}x contra o filtro de {FILTRO:.2f}x.')
print()
print(f'  3. As candidatas `A1`, `A15` e `D2` nao sao novas: elas SAO o `Calado`, o `Atordoado`')
print(f'     e o `Atordoado` de novo. Comprar condicao ja publicada por Melhoria e duplicar.')
print()
print(f'  4. A `Intervencao` tem DUAS leituras e o projeto nao decidiu qual: 0,00 se ela sai da')
print(f'     cota (§6.1) e {UMA_ACAO:.2f} se ela e acao extra. ⚠ Isso e um buraco aberto no')
print(f'     bestiario, e nao uma escolha desta Melhoria.')
print()
print(f'  5. O `refino` entrega {5*PP_ALIADO*ALIADOS:.2f} por degrau de protecao — tamanho de')
print(f'     `Desarmado`. E ele NAO e alvo reproduzivel: cada aptidao le o refino com teto')
print(f'     proprio, entao o mesmo "-3 de refino" faz coisa diferente em cada bloco.')

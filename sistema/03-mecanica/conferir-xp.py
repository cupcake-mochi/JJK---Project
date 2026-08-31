#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Confere a tabela de XP (peca 12) — a trava numero 1 de mundo compartilhado.

O QUE ELA TEM DE DIFERENTE DE TODA PECA ANTERIOR:

  Ela e a primeira escrita a partir de DADO DE GENTE REAL — catorze opinioes da
  Guilda sobre quanto tempo a subida deve levar. Entao este validador tem uma
  checagem que nenhum outro do projeto tem: ele confere que a regra escrita ainda
  produz o TEMPO que as pessoas pediram. Se alguem mexer na curva ou no tamanho
  das missoes, ele diz de quanto o alvo saiu.

CONTRATO DE INVARIANTES:
  1. A CURVA CRESCE, E E ISSO QUE FECHA O ABISMO. Cada nivel custa mais que o
     anterior, entao a mesma missao vale uma fatia menor para quem esta na frente.
     E a propriedade que faz XP fixo funcionar numa guilda.
  2. O ATRASADO ALCANCA. Simulado: dois personagens, um perde dez sessoes, e a
     distancia entre eles tem que FECHAR antes do teto de nivel — e nunca crescer.
  3. OS TRES PERFIS BATEM O ALVO. joga pouco, mediano e joga muito chegam ao nivel
     20 dentro da faixa que a Guilda pediu.
  4. O RETORNO DECRESCENTE NAO ZERA NINGUEM. Nenhuma missao da semana pode pagar
     zero — foi por isso que ele e decrescente em vez de teto duro.
  5. A FAIXA LENDARIA E MAIS CURTA EM TEMPO, apesar de custar mais XP. Foi o unico
     ponto em que as catorze opinioes concordaram.
  6. A CONVERSAO DE MESTRAGEM RECONSTROI DOS DOIS DONOS. O `20` do SS6.2 nao esta
     escrito em lugar nenhum como escolha: ele e a taxa mais pesada do levantamento
     dividida pela fatia do mundano do SS6.1. A tabela de ritmo e recontada dele, e
     a marca tem de continuar mais rara que o marco da peca 2.
  7. A LISTA DE FEITOS DO LIMIAR E FECHADA E ANCORADA. Oito entradas, a contagem
     batida contra o titulo, toda entrada citando o documento em que o fato mora, e
     toda peca citada existindo. E' o que separa lista fechada de lista de exemplo:
     a peca 10 exige fato do mundo, e fato do mundo tem dono.

  Os blocos 6 e 7 sao os unicos que LEEM documento — o resto deste validador
  carrega a regra no codigo, do jeito que a v0.32 escreveu.

Roda de sistema/03-mecanica/, sem argumento. Sai com codigo 1 se algo quebrar.
"""
import os
import re
import sys

ERROS = []
AVISOS = []


def erro(msg):
    ERROS.append(msg)
    print(f'  !! {msg}')


def aviso(msg):
    AVISOS.append(msg)
    print(f'  ~~ {msg}')


def bloco(t):
    print()
    print('=' * 88)
    print(t)
    print('=' * 88)


# --------------------------------------------------------------------------
# A REGRA
#
# O custo de um nivel e sempre um numero INTEIRO de missoes padrao, e ele sobe um
# degrau a cada tres niveis. Isso vem do jogo organizado: a Adventurers League usa
# 4 e 8 checkpoints por nivel, e a Pathfinder Society usa 12 XP por nivel com o
# cenario pagando 4 — "tres cenarios por nivel", legivel sem tabela.
#
# A v0.31 usava uma reta (100 + 30 x (nivel-2)), e ela produzia custo quebrado em
# quase todo nivel (1,3 missao, 1,6 missao) e deixava uma missao grande entregar
# DOIS niveis de uma vez nos primeiros. A AL abandonou XP em 2018 por esse mesmo
# defeito, com o caso documentado: "uma aventura de quatro horas levava um
# personagem novo do nivel 1 ao 3".
MISSAO_PADRAO = 100
NIVEIS_POR_DEGRAU = 3  # a cada tres niveis, o custo sobe uma missao
TETO_NIVEIS_POR_MISSAO = 1
NIVEL_INICIAL = 2
NIVEL_LIMIAR = 20      # aqui o XP para de bastar: precisa de feito
NIVEL_TETO = 30

TAMANHO = {'curta': 50, 'padrao': 100, 'longa': 200, 'final de arco': 300}

# retorno decrescente: as N primeiras missoes da semana pagam cheio, e da
# seguinte em diante o valor cai pela metade a cada uma
MISSOES_CHEIAS = 2
DECAIMENTO = 0.5

SEMANAS_POR_MES = 4.33

# a mistura tipica de missao em cada faixa, de onde sai a missao media
MEDIA_MUNDANA = 106    # padrao, com uma longa a cada quatro
MEDIA_LENDARIA = 240   # longa e final de arco

# o que a Guilda pediu — catorze opinioes, em meses ate o nivel 20
# (perfil, mesas por semana, alvo, tolerancia)
PERFIS = [
    ('joga pouco', 1.0, 14.0, 2.0),
    ('mediano',    1.5,  9.0, 1.5),
    ('joga muito', 4.0,  6.5, 2.0),
]


def missoes_do_nivel(nivel):
    """Quantas missoes padrao custa sair de `nivel`. Sempre inteiro."""
    return 1 + (nivel - NIVEL_INICIAL) // NIVEIS_POR_DEGRAU


def preciso(nivel):
    """XP para sair de `nivel` para o proximo."""
    return MISSAO_PADRAO * missoes_do_nivel(nivel)


def acumulado(ate):
    return sum(preciso(n) for n in range(NIVEL_INICIAL, ate))


def equiv_semana(mesas):
    """Quantas missoes-cheias valem `mesas` missoes numa semana."""
    total = 0.0
    i = 1
    resto = float(mesas)
    while resto > 1e-9:
        parte = min(1.0, resto)
        peso = 1.0 if i <= MISSOES_CHEIAS else DECAIMENTO ** (i - MISSOES_CHEIAS)
        total += parte * peso
        resto -= parte
        i += 1
    return total


# --------------------------------------------------------------------------
bloco('1. A CURVA CRESCE?')

print('  E o que faz XP fixo funcionar: se cada nivel custa mais, a mesma missao')
print('  vale uma fatia menor para quem esta na frente.\n')
print(f"  {'nivel':<8}{'XP para o proximo':<22}{'em missoes padrao':<22}{'acumulado'}")
for n in (2, 5, 8, 11, 14, 17, 19, 20, 24, 29):
    p = preciso(n)
    print(f'  {n:<8}{p:<22}{p / TAMANHO["padrao"]:<22.1f}{acumulado(n + 1)}')

anterior = 0
for n in range(NIVEL_INICIAL, NIVEL_TETO):
    p = preciso(n)
    if p < anterior:
        erro(f'no nivel {n} o custo ({p}) e MENOR que o do nivel anterior '
             f'({anterior}) — a curva desceu, e sem crescer o atrasado nunca alcanca')
    anterior = p
if preciso(NIVEL_TETO - 1) <= preciso(NIVEL_INICIAL):
    erro('a curva termina custando o mesmo que comeca — ela e plana, e curva plana '
         'nao fecha abismo nenhum: todo mundo sobe no mesmo ritmo para sempre')
else:
    print(f'\n  A curva sobe de {preciso(NIVEL_INICIAL)} para '
          f'{preciso(NIVEL_TETO - 1)} XP, em degraus de '
          f'{NIVEIS_POR_DEGRAU} niveis.')

# --- o custo tem que ser numero inteiro de missoes, que e a licao do jogo organizado
quebrados = [n for n in range(NIVEL_INICIAL, NIVEL_TETO)
             if preciso(n) % MISSAO_PADRAO != 0]
if quebrados:
    erro(f'{len(quebrados)} nivel(is) custam um numero quebrado de missoes padrao '
         f'(o primeiro e o {quebrados[0]}) — a Adventurers League e a Pathfinder '
         'Society convergem em custo inteiro justamente porque ele se le sem tabela')
else:
    print('  E todo nivel custa um numero INTEIRO de missoes padrao: '
          + ' · '.join(f'nv{n}={missoes_do_nivel(n)}' for n in (2, 5, 8, 11, 14, 17, 20)))

fatia_2 = TAMANHO['padrao'] / preciso(2)
fatia_19 = TAMANHO['padrao'] / preciso(19)
print(f'  Uma missao padrao vale {fatia_2:.0%} de um nivel no nv2 e {fatia_19:.0%} no nv19.')
if fatia_19 > fatia_2 / 2:
    aviso(f'a fatia so caiu de {fatia_2:.0%} para {fatia_19:.0%} — a curva cresce devagar '
          'demais para fechar abismo em tempo util')


# --------------------------------------------------------------------------
bloco('2. O ATRASADO ALCANCA?')

print('  Dois personagens comecam juntos. Um perde dez sessoes e depois joga tudo')
print('  junto com o outro. A distancia entre eles tem que FECHAR — e nunca crescer.\n')


def simula(escalado, n_sessoes, atraso=10, valor=TAMANHO['padrao']):
    def sobe(nv, xp):
        while nv < NIVEL_TETO and xp >= preciso(nv):
            xp -= preciso(nv)
            nv += 1
        return nv, xp

    A = [NIVEL_INICIAL, 0]
    B = [NIVEL_INICIAL, 0]
    for s in range(n_sessoes):
        for quem, ativo in ((A, True), (B, s >= atraso)):
            if not ativo:
                continue
            ganho = valor * (quem[0] / 8) if escalado else valor
            quem[1] += ganho
            quem[0], quem[1] = sobe(*quem)
    return A[0], B[0]


print(f"  {'sessoes':<12}{'XP fixo: distancia':<26}{'XP escalado: distancia'}")
dist_fixo = []
for n in (20, 40, 60, 90, 120):
    a1, b1 = simula(False, n)
    a2, b2 = simula(True, n)
    dist_fixo.append(a1 - b1)
    print(f'  {n:<12}{a1 - b1:<26}{a2 - b2}')

# O invariante NAO e "chega a zero em 120 sessoes" — 120 sessoes nao alcancam o
# teto de nivel, entao exigir zero ali era criterio arbitrario meu. O que importa
# e a distancia ENCOLHER sempre e terminar pequena: e isso que garante que o
# atrasado volta a caber na mesa, mesmo que nunca empate no papel.
TETO_DISTANCIA_FINAL = 1

if any(dist_fixo[i] < dist_fixo[i + 1] for i in range(len(dist_fixo) - 1)):
    erro('com XP fixo a distancia CRESCEU em algum ponto — a propriedade que '
         'justifica o XP fixo parou de valer')
elif dist_fixo[-1] > TETO_DISTANCIA_FINAL:
    erro(f'com XP fixo a distancia ainda e de {dist_fixo[-1]} niveis no fim da '
         f'campanha, acima do teto de {TETO_DISTANCIA_FINAL} — quem perdeu dez '
         'sessoes nao volta a caber na mesa')
else:
    print(f'\n  Com XP fixo a distancia so encolhe: '
          f'{" -> ".join(str(d) for d in dist_fixo)}.')
    print('  E aritmetica pura: ninguem recebe nada de especial, o atrasado so')
    print('  precisa de menos XP porque o nivel dele e mais barato.')
    # onde ela zera de verdade, se zerar
    for n in range(130, 400, 10):
        a, b = simula(False, n)
        if a == b:
            print(f'  Ela chega a zero em {n} sessoes — depois do fim de uma campanha,')
            print('  o que quer dizer que na pratica ela termina em um nivel de folga.')
            break


# --------------------------------------------------------------------------
bloco('3. OS TRES PERFIS BATEM O QUE A GUILDA PEDIU?')

missoes_20 = acumulado(NIVEL_LIMIAR) / MEDIA_MUNDANA
missoes_30 = (acumulado(NIVEL_TETO) - acumulado(NIVEL_LIMIAR)) / MEDIA_LENDARIA
print(f'  2 -> 20: {acumulado(NIVEL_LIMIAR)} XP em missoes de {MEDIA_MUNDANA} = '
      f'{missoes_20:.0f} missoes')
print(f'  20 -> 30: {acumulado(NIVEL_TETO) - acumulado(NIVEL_LIMIAR)} XP em missoes de '
      f'{MEDIA_LENDARIA} = {missoes_30:.0f} missoes\n')
print(f"  {'perfil':<14}{'mesas/sem':<12}{'equivalente':<14}{'2->20':<12}{'alvo':<10}{'20->30'}")
for nome, freq, alvo, tol in PERFIS:
    e = equiv_semana(freq)
    m20 = missoes_20 / (e * SEMANAS_POR_MES)
    m30 = missoes_30 / (e * SEMANAS_POR_MES)
    fora = abs(m20 - alvo) > tol
    print(f'  {nome:<14}{freq:<12}{e:<14.2f}{m20:<12.1f}{alvo:<10}{m30:.1f}'
          f'{"   <<< fora da faixa" if fora else ""}')
    if fora:
        erro(f'o perfil "{nome}" chega ao nivel {NIVEL_LIMIAR} em {m20:.1f} meses, e a '
             f'Guilda pediu {alvo} (tolerancia {tol}) — a regra saiu do que as '
             'pessoas aceitaram')

print('\n  A tolerancia existe porque isto e opiniao, e nao medida. O que ela impede')
print('  e a regra derivar longe do pedido sem ninguem perceber.')


# --------------------------------------------------------------------------
bloco('3b. UMA MISSAO PODE ENTREGAR MAIS DE UM NIVEL?')

print('  E o defeito que derrubou o XP na Adventurers League: "uma aventura de')
print('  quatro horas levava um personagem novo do nivel 1 ao 3". Subir tres niveis')
print('  de uma vez e decisao de ficha demais para digerir numa sessao.\n')


def sobe_uma_missao(nivel, xp_ganho, teto=TETO_NIVEIS_POR_MISSAO):
    """Quantos niveis uma unica missao entrega, e o que sobra acumulado."""
    sobra = xp_ganho
    subiu = 0
    n = nivel
    while n < NIVEL_TETO and sobra >= preciso(n) and (teto is None or subiu < teto):
        sobra -= preciso(n)
        n += 1
        subiu += 1
    return subiu, sobra


print(f"  {'no nivel':<12}" + ''.join(f'{k:<16}' for k in TAMANHO))
for nv in (2, 3, 5, 8, 12, 18, 25):
    linha = []
    for k, v in TAMANHO.items():
        s, resto = sobe_uma_missao(nv, v)
        linha.append(f'{s} niv, +{resto:.0f}')
    print(f'  {nv:<12}' + ''.join(f'{x:<16}' for x in linha))

sem_teto_max = 0
for nv in range(NIVEL_INICIAL, NIVEL_TETO):
    for v in TAMANHO.values():
        s, _ = sobe_uma_missao(nv, v, teto=None)
        sem_teto_max = max(sem_teto_max, s)
print(f'\n  Sem o teto, a pior combinacao entregaria {sem_teto_max} niveis de uma vez.')

# O LIMITE DE DESIGN, que e coisa diferente do teto aplicado. Comparar o resultado
# contra TETO_NIVEIS_POR_MISSAO seria auto-referencia: subir a constante subiria a
# regua junto, e a perturbacao passaria verde. E o mesmo defeito que a checagem de
# dominancia (v0.28) e a do upkeep (v0.30) tiveram — a terceira vez na mesma semana.
MAXIMO_DE_DESIGN = 1

if TETO_NIVEIS_POR_MISSAO > MAXIMO_DE_DESIGN:
    erro(f'o teto aplicado e {TETO_NIVEIS_POR_MISSAO} nivel(is) por missao, e o '
         f'limite de design e {MAXIMO_DE_DESIGN} — subir tres niveis numa sessao e '
         'decisao de ficha demais, e foi por isso que a Adventurers League largou XP')

achou = False
for nv in range(NIVEL_INICIAL, NIVEL_TETO):
    for nome, v in TAMANHO.items():
        s, _ = sobe_uma_missao(nv, v)
        if s > MAXIMO_DE_DESIGN:
            achou = True
            erro(f'no nivel {nv} uma missao "{nome}" entrega {s} niveis de uma vez, '
                 f'acima do limite de design de {MAXIMO_DE_DESIGN}')
if not achou:
    print(f'  Com o teto de {TETO_NIVEIS_POR_MISSAO}, nenhuma combinacao de nivel e '
          'tamanho passa do limite de design.')
    print('  E o excedente NAO some: ele fica no acumulado e sai na missao seguinte.')


# --------------------------------------------------------------------------
bloco('4. O RETORNO DECRESCENTE ZERA ALGUEM?')

print('  Ele e decrescente em vez de teto duro por um motivo de mesa: seis horas de')
print('  sessao que terminam em zero fazem a pessoa nao voltar.\n')
print(f"  {'missao da semana':<20}{'paga'}")
for i in range(1, 7):
    peso = 1.0 if i <= MISSOES_CHEIAS else DECAIMENTO ** (i - MISSOES_CHEIAS)
    print(f'  {i}a{"":<18}{peso:.0%}')
    if peso <= 0:
        erro(f'a {i}a missao da semana paga zero — o retorno decrescente virou teto '
             'duro, e a regra vira motivo de briga em vez de ritmo')

if not 0 < DECAIMENTO < 1:
    erro(f'o decaimento e {DECAIMENTO} — fora do intervalo aberto (0, 1) ele deixa de '
         'ser retorno decrescente')

sem_teto = missoes_20 / (4.0 * SEMANAS_POR_MES)
com_teto = missoes_20 / (equiv_semana(4.0) * SEMANAS_POR_MES)
print(f'\n  Sem o decrescente, quem joga 4x por semana chega ao nivel 20 em '
      f'{sem_teto:.1f} meses.')
print(f'  Com ele, em {com_teto:.1f}. E ele tambem e o que faz moer mesa parar de '
      'compensar sozinho.')
if com_teto <= sem_teto * 1.2:
    aviso('o retorno decrescente quase nao muda o ritmo de quem joga muito — ele '
          'esta frouxo demais para fazer o trabalho que justifica existir')


# --------------------------------------------------------------------------
bloco('5. A FAIXA LENDARIA E MAIS CURTA EM TEMPO?')

xp_mundano = acumulado(NIVEL_LIMIAR)
xp_lendario = acumulado(NIVEL_TETO) - acumulado(NIVEL_LIMIAR)
print(f'  mundana  (2 -> 20, 18 niveis): {xp_mundano} XP, ~{missoes_20:.0f} missoes')
print(f'  lendaria (20 -> 30, 10 niveis): {xp_lendario} XP, ~{missoes_30:.0f} missoes')
print(f'\n  A lendaria custa MAIS XP ({xp_lendario} contra {xp_mundano}) em MENOS niveis,')
print('  e mesmo assim leva menos missoes — porque as missoes de la sao maiores.')

if xp_lendario <= xp_mundano:
    aviso(f'a faixa lendaria custa menos XP que a mundana — dez niveis de topo '
          'ficaram mais baratos que dezoito de base')
if missoes_30 >= missoes_20:
    erro(f'a faixa lendaria leva {missoes_30:.0f} missoes contra {missoes_20:.0f} da '
         'mundana — as catorze opinioes concordaram que ela e mais curta em tempo, '
         'e a regra parou de entregar isso')
else:
    print(f'\n  Razao: {missoes_30 / missoes_20:.2f} — a Guilda pediu entre 0,45 e 0,61.')
    if not 0.35 <= missoes_30 / missoes_20 <= 0.75:
        aviso(f'a razao {missoes_30 / missoes_20:.2f} saiu da faixa que o levantamento '
              'produziu (0,45 a 0,61, com folga ate 0,35 e 0,75)')


# --------------------------------------------------------------------------
# v0.172. Daqui para baixo NADA esta escrito no codigo: os dois numeros novos
# saem do documento dono. O `20` da conversao e' uma divisao de dois donos —
# a taxa mais pesada do levantamento e a fatia do mundano do SS6.1 — e a lista
# de feitos e' recontada da tabela do SS7.1.
AQUI = os.path.dirname(os.path.abspath(__file__))


def _ler(nome, subdir='.'):
    try:
        with open(os.path.join(AQUI, subdir, nome), encoding='utf-8') as fh:
            return fh.read()
    except OSError:
        return ''


def _sec(texto, abre, fecha):
    """Recorta de um titulo ate o proximo. Fecha em `##` E em `###` — a v0.153
    pagou por fechar so na `###` e deixar o corpo vazar tres secoes adiante."""
    i = texto.find(abre)
    if i < 0:
        return ''
    j = texto.find(fecha, i + len(abre))
    return texto[i:j if j > 0 else len(texto)]


def _num(s):
    return float(s.replace('.', '').replace(',', '.'))


PALAVRA = {'dez': 10, 'doze': 12, 'quinze': 15, 'dezoito': 18, 'vinte': 20,
           'vinte e cinco': 25, 'trinta': 30, 'quarenta': 40, 'cinquenta': 50,
           'quatro': 4, 'cinco': 5, 'seis': 6, 'sete': 7, 'oito': 8, 'nove': 9}

P12 = _ler('12-experiencia-e-progressao.md')
P02 = _ler('02-economia-de-atributos.md')
LEV = _ler('levantamento-ritmo-de-progressao.md', '../01-pesquisa')

bloco('6. A CONVERSAO DE MESTRAGEM RECONSTROI? (peca 12 SS6.2)')

# --- o `20` da LINHA DE REGRA, e nao da secao -----------------------------
# Licao no 1: prosa SOBRE a regra nao e' a regra. Licao no 2: janela de N
# caracteres morre num ponto final — por isso o recorte sai da LINHA do bloco
# `>` que carrega a regra, e nao de uma janela em volta da palavra.
_s62 = _sec(P12, '## 6.2 ', '## 7.')
if not _s62:
    erro('6: nao achei o SS6.2 da peca 12 — a secao da conversao de mestragem '
         'sumiu, e esta checagem sairia verde sem ter lido regra nenhuma')
else:
    _regra = [l for l in _s62.splitlines()
              if l.startswith('>') and 'mesas mestradas' in l]
    if len(_regra) != 1:
        erro(f'6: achei {len(_regra)} linha(s) de regra com "mesas mestradas" no '
             f'bloco > do SS6.2, e tem de ser uma — tirar a regra do bloco de '
             f'citacao ou duplica-la faz esta checagem medir a coisa errada')
    else:
        _l = _regra[0]
        _p = re.search(r'A cada (\w+) mesas mestradas', _l)
        N_PUB = PALAVRA.get(_p.group(1)) if _p else None
        if N_PUB is None:
            erro(f'6: a linha de regra do SS6.2 nao diz "A cada <numero> mesas '
                 f'mestradas", ou o numeral nao esta no dicionario: {_l[:90]}')
        if 'mensalidade' not in _l or 'seu Grau' not in _l:
            erro('6: a linha de regra do SS6.2 parou de pagar "uma mensalidade do '
                 'seu Grau" — se o valor virar numero proprio, ele deixa de ser a '
                 'linha da peca 12 SS6.1 e vira a segunda copia dela (licao no 9)')

        # --- os dois donos da divisao -------------------------------------
        _f = re.search(r'o mundano inteiro cabe em `(\d+)%`', P12)
        FATIA = int(_f.group(1)) / 100 if _f else None
        if FATIA is None:
            erro('6: nao achei a fatia do mundano no SS6.1 da peca 12 ("o mundano '
                 'inteiro cabe em `N%` dela") — ela e um dos dois donos do 20')
        _t = re.search(r'mestra (\d+)-(\d+) mesas por m[êe]s', LEV)
        TAXA_MAX = int(_t.group(2)) if _t else None
        if TAXA_MAX is None:
            erro('6: nao achei "mestra N-M mesas por mes" no levantamento — ele e '
                 'o outro dono do 20, e sem ele a divisao nao reproduz')

        if None not in (N_PUB, FATIA, TAXA_MAX):
            N_DER = TAXA_MAX / FATIA
            print(f'  regra publica: uma marca a cada {N_PUB} mesas mestradas')
            print(f'  derivado: {TAXA_MAX} mesas/mes (levantamento) / {FATIA:.0%} '
                  f'(SS6.1) = {N_DER:.1f}')
            if abs(N_PUB - N_DER) > 0.5:
                erro(f'6: a regra publica {N_PUB} mesas por marca e a divisao dos '
                     f'dois donos da {N_DER:.1f}. O SS6.2 afirma que nenhum dos '
                     f'dois numeros foi escolhido — se o 20 deixa de reproduzir, '
                     f'a afirmacao e' + chr(39) + ' falsa')
            else:
                print('  [x] o 20 nao foi escolhido: ele e a divisao dos dois donos.')

            # --- 6.1: o livro publica a FORMA, e a peca publica o VALOR ----
            # v0.195. A regra de voz do livro ganhou uma linha nova: o livro
            # recomenda o que e de cada servidor e nao decide por ele — quanto se
            # paga por mesa mestrada e decisao de guilda, e um servidor pode
            # escolher nao pagar em dinheiro nenhum. O livro trocou o numero por
            # `X`; a peca ficou dona da derivacao.
            #
            # E na primeira aplicacao os dois divergiram em silencio: o livro
            # passou a dizer `X` e esta peca continuou publicando "vinte" como
            # REGRA, sem dizer que tinha deixado de ser. Nenhum validador olhava
            # os dois lados.
            #
            # A checagem guarda a RELACAO, nos dois sentidos: enquanto o livro
            # publicar a forma, a peca tem de declarar que aquilo virou
            # recomendacao; se o livro voltar a publicar um numero, a declaracao
            # perde o objeto e isso acende.
            _CAP = os.path.join(AQUI, '..', '05-material', 'livro', 'manual',
                                '80-experiencia-e-progressao.md')
            _FORMA = re.compile(r'a cada `X` mesas mestradas', re.I)
            _NUM_LIV = re.compile(r'a cada (?:`)?(\d+|vinte|dez|quinze)(?:`)? mesas mestradas', re.I)
            _DECLARA = re.compile(r'DEIXOU DE SER REGRA', re.I)
            if not os.path.isfile(_CAP):
                erro('6.1: nao achei o capitulo de XP do livro — e ele e o outro lado '
                     'da relacao que esta checagem guarda')
            else:
                _liv = open(_CAP, encoding='utf-8').read()
                _tem_forma = bool(_FORMA.search(_liv))
                _tem_num = bool(_NUM_LIV.search(_liv))
                _declara = bool(_DECLARA.search(_s62))
                if _tem_forma and not _declara:
                    erro('6.1: o livro publica a FORMA ("a cada `X` mesas mestradas") e o '
                         'SS6.2 desta peca nao declara que o numero deixou de ser regra — '
                         'a peca continua lendo como lei o que o livro entrega ao servidor')
                elif _tem_num and _declara:
                    erro('6.1: o livro voltou a publicar um NUMERO de mesas mestradas, e o '
                         'SS6.2 continua declarando que aquilo virou recomendacao — as duas '
                         'nao podem ser verdade juntas')
                elif not _tem_forma and not _tem_num:
                    erro('6.1: o capitulo de XP do livro nao publica nem a forma nem o '
                         'numero da conversao de mestragem — a regra sumiu de la, e esta '
                         'checagem sairia verde sem ter comparado nada')
                else:
                    print('  [x] o livro publica a forma, e a peca declara que o numero '
                          'virou recomendacao.')

            # --- a tabela do SS6.2.1 e RECONTADA -------------------------
            _linhas = []
            for _l in _s62.splitlines():
                m = re.match(r'\|\s*\*\*(\w+)\*\*[^|]*\|\s*`(\d+)`\s*\|\s*`([\d,]+)`'
                             r'\s*meses\s*\|\s*\**`([\d,]+)%`\**\s*\|', _l)
                if m:
                    _linhas.append((m.group(1), int(m.group(2)),
                                    _num(m.group(3)), _num(m.group(4))))
            if len(_linhas) != 3:
                erro(f'6: a tabela de ritmo do SS6.2.1 rendeu {len(_linhas)} linha(s) '
                     f'e sao tres — extrator que para de achar recontaria nada e '
                     f'sairia verde calado')
            else:
                _ruins = []
                for _nome, _taxa, _meses, _pct in _linhas:
                    _m_esp = round(N_PUB / _taxa, 1)
                    _p_esp = round(_taxa / N_PUB * 100, 1)
                    if abs(_meses - _m_esp) > 0.15:
                        _ruins.append(f'"{_nome}" publica {_meses} meses e '
                                      f'{N_PUB}/{_taxa} da {_m_esp}')
                    if abs(_pct - _p_esp) > 0.6:
                        _ruins.append(f'"{_nome}" publica {_pct}% e {_taxa}/{N_PUB} '
                                      f'da {_p_esp}%')
                for _r in _ruins:
                    erro(f'6: a tabela do SS6.2.1 nao reconta: {_r}')
                if not _ruins:
                    print(f'  [x] as tres linhas da tabela reconstroem de N={N_PUB}.')
                _tx = [t for _, t, _, _ in _linhas]
                if max(_tx) != TAXA_MAX:
                    erro(f'6: a tabela do SS6.2.1 chama {max(_tx)} de teto relatado e '
                         f'o levantamento diz {TAXA_MAX} — a linha de cima da tabela '
                         f'e a que ancora a trava, e ela virou copia divergente')

            # --- a marca e' mais rara que o marco ------------------------
            # Nao e' auto-referencia: os marcos vem da peca 2 e o 9,7 do SS5.
            _mm = re.search(r'\|\s*mediano\s*\|[^|]*\|[^|]*\|\s*\*\*([\d,]+) meses',
                            P12)
            _mc = re.search(r'n[íi]veis \*\*([\d, e]+)\*\*, sete marcos', P02)
            if not _mm or not _mc:
                erro('6: nao achei o perfil mediano do SS5 ou os sete marcos da peca 2 '
                     '— sem os dois a comparacao de raridade nao tem contra o que medir')
            else:
                _meses20 = _num(_mm.group(1))
                _marcos = [int(x) for x in re.findall(r'\d+', _mc.group(1))]
                _ate20 = len([m for m in _marcos if m <= NIVEL_LIMIAR])
                _marcas = _meses20 * TAXA_MAX / N_PUB
                print(f'  ate o nivel 20 ({_meses20} meses do mediano): '
                      f'{_marcas:.1f} marca(s) contra {_ate20} marcos')
                if _marcas >= _ate20:
                    erro(f'6: o mestre mais pesado fecha {_marcas:.1f} marcas ate o '
                         f'nivel 20 e a ficha atravessa {_ate20} marcos — o SS6.2.1 '
                         f'afirma que a marca e MENOS frequente que o marco, e ela '
                         f'deixou de ser')
                else:
                    print('  [x] a marca e mais rara que o marco, como o SS6.2.1 diz.')

bloco('7. A LISTA DE FEITOS E FECHADA E ANCORADA? (peca 12 SS7.1)')

_s71 = _sec(P12, '### 7.1 ', '### 7.2')
if not _s71:
    erro('7: nao achei o SS7.1 da peca 12 — a lista de feitos do limiar sumiu')
else:
    _feitos = []
    for _l in _s71.splitlines():
        m = re.match(r'\|\s*\*\*(\d+)\*\*\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|', _l)
        if m:
            _feitos.append((int(m.group(1)), m.group(2), m.group(3)))
    _p = re.search(r'### 7\.1 As (\w+)', _s71)
    N_PROSA = PALAVRA.get(_p.group(1)) if _p else None
    print(f'  {len(_feitos)} entrada(s) na tabela; o titulo do SS7.1 diz {N_PROSA}')
    if N_PROSA is None:
        erro('7: o titulo do SS7.1 nao diz "As <numero>" — sem ele a contagem da '
             'tabela nao tem segunda copia para bater, e a licao no 9 fica sem guarda')
    elif len(_feitos) != N_PROSA:
        erro(f'7: a tabela do SS7.1 tem {len(_feitos)} entradas e o titulo diz '
             f'{N_PROSA} — um numero, dois donos, e eles divergiram')
    elif len(_feitos) < 4:
        erro(f'7: so {len(_feitos)} entrada(s) legiveis — o extrator parou de achar '
             f'e as checagens abaixo passariam trivialmente')
    else:
        if [n for n, _, _ in _feitos] != list(range(1, len(_feitos) + 1)):
            erro(f'7: a numeracao das entradas do SS7.1 tem buraco: '
                 f'{[n for n, _, _ in _feitos]}')

        # --- toda entrada aponta para onde o fato mora --------------------
        # E' o que separa lista FECHADA de lista de exemplo: a peca 10 exige que
        # a entrada cite fato do mundo, e fato do mundo tem documento dono.
        _sem = []
        for _n, _feito, _confere in _feitos:
            if not re.search(r'pe[çc]a \d+|manual|se[çc][ãa]o \d+', _confere):
                _sem.append(f'{_n} ("{_feito[:40]}")')
        if _sem:
            for _s in _sem:
                erro(f'7: a entrada {_s} nao diz em que documento o fato mora — '
                     f'sem dono, conferir vira julgamento e a lista deixa de '
                     f'atravessar sete mesas')
        else:
            print('  [x] as oito entradas apontam para o documento que carrega o fato.')

        # --- e a peca citada existe --------------------------------------
        _arquivos = {int(f[:2]): f for f in os.listdir(AQUI)
                     if re.match(r'\d\d-.*\.md$', f)}
        _mortas = sorted({int(p) for _, _, c in _feitos
                          for p in re.findall(r'pe[çc]a (\d+)', c)}
                         - set(_arquivos))
        if _mortas:
            erro(f'7: a lista aponta para peca(s) que nao existem: {_mortas}')
        else:
            print(f'  [x] toda peca citada nas entradas existe em 03-mecanica/.')

        # --- a lista continua FECHADA ------------------------------------
        if 'palavra final' not in _s71:
            erro('7: o SS7.1 parou de dizer que a palavra final do mestre e sobre SE '
                 'o feito aconteceu, e nao sobre QUAIS sao — e essa frase e a '
                 'diferenca inteira entre lista fechada e lista de exemplo')

# --------------------------------------------------------------------------
print()
print('=' * 88)
if ERROS:
    print(f'>>> {len(ERROS)} PROBLEMA(S):')
    for e in ERROS:
        print('   -', e)
    sys.exit(1)
print('>>> TUDO OK — a curva cresce, o atrasado alcanca, os tres perfis batem o que')
print('    a Guilda pediu, ninguem sai com zero, e a faixa lendaria e mais curta.')
if AVISOS:
    print(f'    {len(AVISOS)} aviso(s) acima, que nao falham o validador.')

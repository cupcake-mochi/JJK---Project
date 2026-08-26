#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Confere o ORCAMENTO SOMADO — todos os drenos de PE ao mesmo tempo.

POR QUE ELE EXISTE, e vale ler antes de mexer:

  Ate a v0.29 todo validador do projeto media UMA peca contra a regua DELA. O
  conferir-aptidoes olhava a aptidao, o conferir-expansao olhava a Expansao, o
  conferir-descanso olhava o descanso. Nenhum somava.

  E uma ficha de verdade gasta tudo ao mesmo tempo: ela conjura, segura uma
  anti-dominio, leva dano de alma que encarece feitico, e ainda tem Reacao. Tres
  versoes seguidas precificaram peca nova medindo o custo dela SOZINHO contra o
  bolso inteiro — o que descreve um personagem que so faz aquilo e mais nada.

  O erro nao era de conta: era de modelo. Este validador existe para tornar essa
  classe inteira visivel, e ele e o unico que responde "cabe TUDO junto?".

CONTRATO DE INVARIANTES:
  1. A LINHA DE BASE CABE. Um personagem que so conjura consegue atravessar o dia
     de tres lutas sem ficar mudo — e a taxa de conjuracao dele e a regua contra a
     qual todo compromisso novo e medido.
  2. UM COMPROMISSO NAO PODE CALAR O PERSONAGEM. Segurar uma anti-dominio durante
     um dominio inimigo tem que deixar PE para as outras lutas do dia.
  3. PRE-LIGAR NAO PODE COMPENSAR. Andar com a aptidao ligada "por via das duvidas"
     tem que esvaziar o bolso rapido o bastante para nao virar rotina.
  4. O DANO DE ALMA EMPILHA POR BAIXO. A Integridade no degrau 2 encarece todo
     feitico em +1 PE por Classe, e ela chega justamente quando voce mais precisa
     da defesa. O somatorio tem que continuar cabendo com ela ligada.
  5. TODO PRECO TEM NUMERO. Um custo escrito como "gasta PE" sem quantidade nao e
     preco: e um buraco que cada mesa preenche diferente.

Roda de sistema/03-mecanica/, sem argumento. Sai com codigo 1 se algo quebrar.
"""
import math
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
    print('=' * 90)
    print(t)
    print('=' * 90)


# --------------------------------------------------------------------------
# O MUNDO. Estes numeros vem de outras pecas e sao copias declaradas — se
# divergirem de la, este validador passa a mentir junto.
MARCOS = [6, 10, 14, 18, 22, 26, 30]

# PE por nivel de cada Caminho (peca 1). O Bastiao e o PISO do sistema, e e por
# ele que toda checagem daqui e medida: se cabe nele, cabe em todo mundo.
PE_POR_NIVEL = {'Bastiao': 4, 'Vanguarda': 5, 'Guia': 5, 'Evocador': 6, 'Emanador': 6}
PISO = 'Bastiao'

LUTAS_DE_GRACA = 3      # a exaustao dispara da QUARTA (peca 10)
RODADAS_POR_LUTA = 3.5  # a trava de vida da peca 1
RODADAS_POR_MINUTO = 6  # rodada de 10 segundos

# curva de refino do especialista (arquitetura.md 4.3) — quem mais segura aptidao
CURVA_ESP = [3, 5, 7, 9, 10, 10, 10]

# --- os precos das anti-dominio que estao em avaliacao ---------------------
# (nome, custo de ATIVAR em x maior Classe, UPKEEP por rodada em x maior Classe)
CANDIDATOS = [
    ('A  0x ativar · 1,00x upkeep', 0, 1.00),
    ('B  0x ativar · 0,50x upkeep', 0, 0.50),
    ('C  2x ativar · 0,50x upkeep', 2, 0.50),
    ('D  3x ativar · 0,25x upkeep', 3, 0.25),
    ('E  2x ativar · 0,75x upkeep', 2, 0.75),
    ('F  1x ativar · 1,00x upkeep', 1, 1.00),
]
# O escolhido na v0.30. Os seis ficam na lista porque a comparacao entre eles e
# metade do valor desta checagem: mostrar QUE OUTRO preco falharia, e por onde.
# A v0.30 chegou a escolher o C e voltou para o A depois que este validador
# mostrou que os dois passam igual — e que o estouro que motivou a mudanca era
# vicio do cenario que eu tinha montado, e nao do preco.
ESCOLHIDO = 'A  0x ativar · 1,00x upkeep'

# quanto tempo pre-ligado o projeto aceita antes de considerar rotina
TETO_PRE_LIGADO_MIN = 6.0


def maior_classe(nv):
    for c, n in ((7, 26), (6, 21), (5, 17), (4, 13), (3, 9), (2, 5), (1, 1)):
        if nv >= n:
            return c
    return 1


def refino(nv):
    r = 1
    for i, m in enumerate(MARCOS):
        if nv >= m:
            r = CURVA_ESP[i]
    return r


def bolso(caminho, nv):
    return PE_POR_NIVEL[caminho] * nv


def custo_feitico(nv, integridade2=False):
    c = maior_classe(nv)
    return 3 * c + (c if integridade2 else 0)


def duracao_dominio(nv):
    return max(1, refino(nv) // 2)


def rodadas_do_dia():
    return LUTAS_DE_GRACA * RODADAS_POR_LUTA


NIVEIS = [10, 14, 18, 22, 26, 30]


# --------------------------------------------------------------------------
bloco('1. A LINHA DE BASE — quanto do dia um personagem consegue conjurar?')

print('  Um dia normal tem 3 lutas de graca (a exaustao dispara da quarta) e cada')
print(f'  luta dura ~{RODADAS_POR_LUTA} rodadas: {rodadas_do_dia():g} rodadas de luta por dia.')
print('  Ninguem conjura em todas — o resto vai para Classe 0, golpe simples e')
print('  projetar energia, que nao custam PE. A pergunta e QUANTAS cabem.\n')

print(f"  {'nv':<5}{'Classe':<8}{'feitico':<9}" +
      ''.join(f'{k[:9]:<16}' for k in ('Bastiao', 'Emanador')))
base_taxa = {}
for nv in NIVEIS:
    c = maior_classe(nv)
    f = custo_feitico(nv)
    linha = []
    for k in ('Bastiao', 'Emanador'):
        n = bolso(k, nv) // f
        taxa = n / rodadas_do_dia()
        if k == PISO:
            base_taxa[nv] = taxa
        linha.append(f'{n}x = {taxa:.0%}')
    print(f'  {nv:<5}{c:<8}{f:<9}' + ''.join(f'{v:<16}' for v in linha))

pior = min(base_taxa.values())
print(f'\n  A taxa de conjuracao do {PISO} fica entre {pior:.0%} e '
      f'{max(base_taxa.values()):.0%} das rodadas do dia.')
if pior < 0.25:
    erro(f'a linha de base caiu para {pior:.0%} das rodadas — sem compromisso nenhum, '
         'o personagem ja passa o dia sem poder conjurar')
elif pior > 0.90:
    aviso(f'a linha de base chegou a {pior:.0%} — o PE parou de ser recurso escasso')
else:
    print('  Isso e a regua. Todo compromisso abaixo e medido contra ela.')


# --------------------------------------------------------------------------
bloco('2. O CANDIDATO ESCOLHIDO CABE, SOMANDO TUDO?')

print('  Cenario: um inimigo abre Expansao. Voce ativa a anti-dominio, segura pela')
print('  duracao dela, e conjura o que sobrar. Depois ainda tem duas lutas no dia.\n')


def gasto_dominio(nv, ativar, upkeep):
    c = maior_classe(nv)
    d = duracao_dominio(nv)
    ca = ativar * c
    cu = max(1, math.ceil(upkeep * c)) if upkeep > 0 else 0
    return ca + cu * d, ca, cu, d


print(f"  {'candidato':<30}{'nv':<5}{'ativar':<8}{'upkeep':<8}{'um dominio':<12}"
      f"{'% do dia':<11}{'feiticos que sobram no dia'}")
for nome, at, up in CANDIDATOS:
    marca = ' <<<' if nome == ESCOLHIDO else ''
    for nv in (14, 22, 30):
        tot, ca, cu, d = gasto_dominio(nv, at, up)
        pool = bolso(PISO, nv)
        sobra = pool - tot
        n_feiticos = max(0, sobra) // custo_feitico(nv)
        rot = nome if nv == 14 else ''
        print(f'  {rot:<30}{nv:<5}{ca:<8}{cu:<8}{tot:<12}{tot/pool:<11.0%}'
              f'{n_feiticos}{marca if nv == 14 else ""}')
    print()

# a checagem de verdade, so no escolhido
at_e, up_e = next((a, u) for n, a, u in CANDIDATOS if n == ESCOLHIDO)
print(f'  Invariante: depois da luta de dominio, tem que sobrar PE para conjurar')
print(f'  pelo menos uma vez em cada uma das outras {LUTAS_DE_GRACA - 1} lutas do dia.\n')
for nv in NIVEIS:
    tot, ca, cu, d = gasto_dominio(nv, at_e, up_e)
    pool = bolso(PISO, nv)
    sobra = pool - tot
    n = max(0, sobra) // custo_feitico(nv)
    ok = n >= (LUTAS_DE_GRACA - 1)
    print(f'    nv{nv:<4} gasta {tot:<4} de {pool:<4} e sobra para {n} feitico(s)  '
          f'{"ok" if ok else "NAO CABE"}')
    if not ok:
        erro(f'no nv{nv} o candidato escolhido deixa so {n} feitico(s) para as outras '
             f'{LUTAS_DE_GRACA - 1} lutas do dia — segurar a defesa uma vez cala o '
             'personagem pelo resto do dia')


# --------------------------------------------------------------------------
bloco('3. PRE-LIGAR COMPENSA?')

print('  Se der para andar com a aptidao ligada, ela deixa de ser decisao e vira')
print(f'  rotina. Uma rodada e {60 // RODADAS_POR_MINUTO}s, entao '
      f'{RODADAS_POR_MINUTO} rodadas por minuto.\n')
print(f"  {'candidato':<30}" + ''.join(f'{"nv"+str(n):<12}' for n in (14, 22, 30)))
for nome, at, up in CANDIDATOS:
    linha = []
    for nv in (14, 22, 30):
        c = maior_classe(nv)
        cu = max(1, math.ceil(up * c)) if up > 0 else 0
        pool = bolso(PISO, nv) - at * c
        minutos = (pool / cu / RODADAS_POR_MINUTO) if cu else float('inf')
        linha.append(f'{minutos:.1f} min')
    marca = ' <<<' if nome == ESCOLHIDO else ''
    print(f'  {nome:<30}' + ''.join(f'{v:<12}' for v in linha) + marca)

print()
for nv in NIVEIS:
    c = maior_classe(nv)
    cu = max(1, math.ceil(up_e * c)) if up_e > 0 else 0
    if cu == 0:
        erro('o candidato escolhido nao tem upkeep nenhum — nada limita quanto tempo '
             'a aptidao fica ligada, e pre-ligar passa a ser sempre certo')
        break
    pool = bolso(PISO, nv) - at_e * c
    minutos = pool / cu / RODADAS_POR_MINUTO
    if minutos > TETO_PRE_LIGADO_MIN:
        erro(f'no nv{nv} da para segurar {minutos:.1f} min pre-ligado, acima do teto de '
             f'{TETO_PRE_LIGADO_MIN:g} min — andar com ela ligada virou rotina')
else:
    print(f'  O escolhido segura no maximo {TETO_PRE_LIGADO_MIN:g} min pre-ligado em todo nivel.')
    print('  Curto o bastante para ser decisao tatica, e nao estado permanente.')

print('\n  E note as DUAS travas, que fazem coisas diferentes:')
print('    o custo de ATIVAR pune ligar sem precisar — e afundado, some se a luta nao vem')
print('    o UPKEEP limita quanto tempo voce segura — quanto menor, mais tempo ligado')
print('  Baixar so o upkeep ALARGA a janela de pre-ligamento. Foi o que a v0.30 achou.')


# --------------------------------------------------------------------------
bloco('4. O DANO DE ALMA EMPILHA POR BAIXO')

print('  A Integridade no degrau 2 faz todo feitico custar +1 PE por Classe. E ela')
print('  chega justamente por dano de alma — que e o que uma Expansao entrega.')
print('  Ou seja: no momento em que voce mais precisa da defesa, conjurar encarece.\n')
# A pergunta NAO e "da para conjurar toda rodada com tudo ligado" — a linha de
# base do bloco 1 ja responde que nao, e nunca deu. A pergunta e se uma rodada de
# compromisso total ainda cabe no dia, ou se ela sozinha ja quebra o personagem.
TETO_RODADA_CHEIA = 0.50   # uma rodada com tudo ligado nao pode passar disto do dia

print(f"  {'nv':<5}{'feitico':<10}{'com Integr.2':<15}{'+ upkeep':<11}"
      f"{'a rodada cheia e':<18}{'conjura na luta'}")
for nv in NIVEIS:
    c = maior_classe(nv)
    f = custo_feitico(nv)
    fi = custo_feitico(nv, integridade2=True)
    cu = max(1, math.ceil(up_e * c))
    por = fi + cu
    pool = bolso(PISO, nv)
    fatia = por / pool
    # quantas vezes ele consegue conjurar DENTRO da luta de dominio
    na_luta = min(int(RODADAS_POR_LUTA), int(pool // por))
    print(f'  {nv:<5}{f:<10}{fi:<15}{por:<11}{fatia:<18.0%}{na_luta}x')
    if fatia > TETO_RODADA_CHEIA:
        erro(f'no nv{nv} uma unica rodada com tudo ligado custa {fatia:.0%} do dia — '
             'uma rodada nao pode falir o personagem')
    if na_luta < 1:
        erro(f'no nv{nv}, com dano de alma e a defesa de pe, o {PISO} nao consegue '
             'conjurar nenhuma vez na luta — o compromisso o calou por completo')

print('\n  A leitura: uma rodada de compromisso total custa cerca de um terco do dia,')
print('  e o personagem ainda conjura 3 vezes dentro da luta de dominio. Isso e caro')
print('  e jogavel — que e o formato certo.')
print('\n  E note o que esta checagem NAO pergunta: se da para conjurar toda rodada.')
print('  Nunca deu, e supor que dava foi o vicio que produziu esta peca inteira.')


# --------------------------------------------------------------------------
bloco('5. TODO PRECO TEM NUMERO?')

AQUI = os.path.dirname(os.path.abspath(__file__))

# "PE" tem que ser a sigla e nao o comeco de outra palavra — sem o \b, "custa
# Pesada" casava com "custa PE" e a checagem acusava preco de Melhoria como se
# fosse preco em energia. Foi o primeiro falso positivo dela.
RX_SEM_NUMERO = re.compile(r'(gastando|gasta|custa|custam)\s+PE\b(?![^.]{0,40}\d)',
                           re.IGNORECASE)
# negacao nao e preco: "ela NAO gasta PE" esta dizendo que e de graca
RX_NEGADO = re.compile(r'\b(nao|não|sem)\b[^.]{0,25}$', re.IGNORECASE)
# CARACTERIZACAO nao e preco, e este e o terceiro falso positivo desta checagem
# — os dois primeiros estao logo abaixo. Uma frase da forma "uma acao QUE gasta
# PE ... E' o Fundamento" nao cobra de coisa nenhuma: o sujeito e' indefinido, e
# o que a frase afirma nao e' o custo, e' a identidade que vem depois. Preco de
# verdade se pendura em coisa NOMEADA — "a `Redoma` gasta PE" ainda acende.
# A peca 25 §7 usa essa forma para DERIVAR que a maquina tem de gastar PE, e
# esta checagem estava lendo o argumento como se fosse a linha de regra: e' a
# mesma familia da licao no 1 da v0.168, extrator lendo prosa onde ha regra.
RX_CARACTERIZA = re.compile(
    r'\b(uma?|toda?s?|todos?|qualquer)\b[^.]{0,80}\bque\b[^.]{0,80}$', re.IGNORECASE)
RX_IDENTIDADE = re.compile(r'\b[Éé]\b')

# entradas ainda nao escritas declaram o que VAO cobrar, e isso e legitimo.
# Elas saem da checagem enquanto estiverem na lista das que faltam.
NAO_ESCRITAS = ('Energia Reversa', 'Barreira Simples', 'Cortina', 'Aptidão Própria')

achados = []
for f in sorted(os.listdir(AQUI)):
    if not f.endswith('.md') or f.startswith('RASCUNHO'):
        continue
    txt = open(os.path.join(AQUI, f), encoding='utf-8').read()
    for m in RX_SEM_NUMERO.finditer(txt):
        antes = txt[max(0, m.start() - 40):m.start()]
        if RX_NEGADO.search(antes):
            continue
        # citacao nao e regra: uma nota que EXPLICA o preco antigo precisa poder
        # escrever como ele era. Se o trecho esta entre aspas, ele esta sendo
        # mencionado e nao aplicado. Foi o segundo falso positivo desta checagem.
        if txt[max(0, m.start() - 1):m.start()] == '"' and txt[m.end():m.end() + 1] == '"':
            continue
        # a frase em volta do match, cortada no ponto e na quebra de linha
        frase_ini = max(txt.rfind('.', 0, m.start()), txt.rfind('\n', 0, m.start())) + 1
        # o predicado tem de ser o IMEDIATO — corta na virgula tambem. Sem isso
        # qualquer "..., e e' por isso que..." adiante na frase satisfazia a
        # guarda, e ai ela nao separava nada: `e'` esta em toda frase daqui.
        resto = txt[m.end():]
        _fim = re.search(r'[.,\n]', resto)
        if RX_CARACTERIZA.search(txt[frase_ini:m.start()]) and \
                RX_IDENTIDADE.search(resto[:_fim.start()] if _fim else resto):
            continue
        linha_ini = txt.rfind('\n', 0, m.start()) + 1
        linha = txt[linha_ini:txt.find('\n', m.end())]
        if any(n in linha for n in NAO_ESCRITAS):
            continue
        ini = max(0, m.start() - 90)
        achados.append((f, txt[ini:m.end() + 50].replace('\n', ' ')))

if achados:
    for f, trecho in achados:
        erro(f'{f} anuncia custo em PE sem quantidade: "...{trecho.strip()}..."')
    print('\n  Um custo escrito como "gasta PE" sem numero nao e preco — e um buraco')
    print('  que cada mesa preenche diferente, e o filtro multi-mestre existe para isso.')
else:
    print('  Nenhuma peca de 03-mecanica anuncia custo em PE sem dizer quanto.')


# --------------------------------------------------------------------------
print()
print('=' * 90)
if ERROS:
    print(f'>>> {len(ERROS)} PROBLEMA(S):')
    for e in ERROS:
        print('   -', e)
    sys.exit(1)
print('>>> TUDO OK — a linha de base cabe, o compromisso nao cala o personagem,')
print('    pre-ligar nao compensa, o dano de alma empilha sem quebrar, e todo')
print('    preco em PE tem numero.')
if AVISOS:
    print(f'    {len(AVISOS)} aviso(s) acima, que nao falham o validador.')

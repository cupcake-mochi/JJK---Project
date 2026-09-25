#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Confere o quadro de pericias e oficios da peca 07.

  Pericia = d20 + atributo dela + maestria (maestria so entra se treinado)
  Oficio  = d20 + atributo que a situacao pede + maestria (idem)

O que este validador garante:
  1. contagem por atributo bate com o documento
  2. nenhum nome aparece duas vezes, nem como pericia e oficio ao mesmo tempo
  3. as fixas de cada Caminho existem no quadro e nenhuma se repete dentro do Caminho
  4. a fracao treinada fica na faixa que a peca 6 pediu (30% a 40%)
  5. toda pericia e alcancavel por alguem
  6. nenhum nome colide com termo definido do Fundamento nem com termo interno do
     projeto — e as colisoes ACEITAS de proposito estao declaradas aqui, com o motivo

Roda sem argumento. Sai com codigo 1 se algo quebrar.
"""

import os
import glob
import re
import sys
import unicodedata

FALHAS = []
# Checagem que nao rodou — ver o comentario igual no conferir-nomes.py. Sem
# python-docx este validador dizia TUDO OK sem ter aberto o manual uma vez.
PULADAS = []


def erro(msg):
    FALHAS.append(msg)
    print(f'  !! {msg}')


def norma(s):
    s = unicodedata.normalize('NFD', s.lower())
    return ''.join(c for c in s if unicodedata.category(c) != 'Mn')


# --------------------------------------------------------------------------
# O QUADRO
# --------------------------------------------------------------------------
# v0.16: "Inteligencia SABE, Essencia PERCEBE". Sentir Energia e Percepcao
# moraram em Inteligencia da v0.8 ate a v0.15 e mudaram de casa aqui.

PERICIAS = {
    'Forca':        ['Atletismo'],
    'Destreza':     ['Acrobacia', 'Furtividade', 'Pontaria', 'Prestidigitacao'],
    'Inteligencia': ['Intuicao', 'Investigacao', 'Ocultismo', 'Religiao', 'Historia',
                     'Hierarquia', 'Medicina', 'Sobrevivencia', 'Natureza',
                     'Lidar com Animais', 'Tecnologia'],
    'Essencia':     ['Sentir Energia', 'Percepcao', 'Persuasao', 'Enganacao',
                     'Intimidacao', 'Atuacao', 'Provocar'],
    'Constituicao': [],
}

# v0.42: a lista de oficios saiu daqui e passou a ser LIDA da peca 7.
# Ela morava em tres lugares — a peca, este validador e o dados.js da ficha —
# e so dois eram comparados (o conferir-ficha.py cruza a peca com o dados.js).
# Este arquivo era a terceira copia, sem ninguem conferindo. Licao no 9.
_P7 = open(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '07-pericias-e-oficios.md'), encoding='utf-8').read()
_SEC = re.search(r'## 5\. Os \w+ of[ií]cios(.*?)(?=\n## )', _P7, re.S)
OFICIOS = [norma(n).capitalize() for n in re.findall(r'\*\*([^*]+)\*\* — ', _SEC.group(1))] if _SEC else []

# Quantos a peca DECLARA, lido do titulo dela — separado da lista aplicada,
# que e a licao no 8: a checagem nao pode se medir contra a propria constante.
_NUM = {'nove': 9, 'dez': 10, 'onze': 11, 'doze': 12, 'treze': 13, 'catorze': 14}
_m = re.search(r'## 5\. Os (\w+) of[ií]cios', _P7)
OFICIOS_DECLARADOS = _NUM.get(_m.group(1).lower()) if _m else None

# Cada Caminho fixa duas pericias. Oficio o Caminho NAO trava: os dois que ele
# entrega sao livres (v0.105).
CAMINHOS = {
    'Bastiao':   {'pericias': ['Atletismo', 'Provocar']},   # Provocar desde a v0.271, pela colecao v0.4
    'Vanguarda': {'pericias': ['Acrobacia', 'Percepcao']},
    'Guia':      {'pericias': ['Persuasao', 'Medicina']},
    'Emanador':  {'pericias': ['Ocultismo', 'Investigacao']},
    'Evocador':  {'pericias': ['Religiao', 'Lidar com Animais']},
}
# Sentir Energia NAO e fixa de ninguem, de proposito: ela e a mais rolada da mesa,
# e fixa-la em um Caminho daria a ele uma escolha livre a mais na pratica. Livre
# para todos, ela vira decisao — e o feiticeiro ruim de sentir energia passa a caber.

# v0.212: as livres do Caminho passaram de 4 para 5 e o extra da Origem acabou;
# v0.216: os dois oficios foram do Caminho para a Origem. As contagens sao LIDAS
# do §6 da peca 7, que e a dona. (Este comentario dizia "v0.211" e "a Origem
# parou de dar oficio" ate a v0.263.)
_mF = re.search(r'duas perícias fixas e mais (\w+) à sua escolha', _P7)
CAM_FIXAS = 2
CAM_LIVRES = {'quatro': 4, 'cinco': 5, 'seis': 6}.get(_mF.group(1).lower()) if _mF else None
ORI_PERICIAS = 2                   # uma da lista da Origem + uma livre

# Quantos oficios existem, de QUEM eles sao e por quantas pericias eles se
# trocam, tudo LIDO do §6 da peca 7. Ate a v0.171 os numeros eram literais, e a
# peca 8 passou sessenta e cinco versoes com a atribuicao trocada.
#
# v0.263: este bloco lia "A Origem nao da oficio" para concluir que o extra
# dela valia zero, e contava os dois oficios como do Caminho. A frase era o
# texto da v0.212 que a v0.216 esqueceu na peca; o total fechava igual (dois
# de onze), entao nada acendia. E com o extra zerado as duas rotas impressas
# eram a MESMA -- a de trocar os oficios por pericia nunca tinha sido medida.
_S6 = re.search(r'\n## 6\. De onde vem o treino(.*?)(?=\n## )', _P7, re.S)
_S6t = _S6.group(1) if _S6 else ''
_PN = {'um': 1, 'uma': 1, 'dois': 2, 'duas': 2, 'três': 3, 'quatro': 4}
_mL = re.search(r'Mais (\w+) ofícios?\b', _S6t)
OFI_N = _PN.get(_mL.group(1).lower()) if _mL else None
_dO = bool(re.search(r'\*\*O Caminho não dá ofício, e quem dá é a Origem\.\*\*', _S6t))
_dC = bool(re.search(r'\*\*A Origem não dá ofício\.?\*\*', _S6t))
OFI_DONO = 'Origem' if (_dO and not _dC) else ('Caminho' if (_dC and not _dO) else None)
_mT = re.search(r'os dois se trocam por mais (\w+) perícias? livres?', _S6t)
OFI_TROCA = _PN.get(_mT.group(1).lower()) if _mT else None
# A faixa de pericia treinada e' da peca 7 §7, e e' LIDA de la. Ate a v0.263 ela
# morava so aqui, escrita na v0.27, antes das duas trocas do §6 existirem.
_mFx = re.search(r'A faixa é de `(\d+)%` a `(\d+)%` de perícias treinadas, e ela vale para a rota de base', _P7)
FAIXA_TREINADA = (int(_mFx.group(1)) / 100, int(_mFx.group(2)) / 100) if _mFx else None

TODAS = [p for grupo in PERICIAS.values() for p in grupo]

# Cada Origem oferece quatro pericias e voce treina uma (peca 09).
#
# v0.129: esta lista saiu daqui e passou a ser LIDA da peca 09, pelo mesmo motivo
# que a de oficios saiu na v0.42 — ela morava em tres lugares (a peca, este
# validador e o livro) e nenhum par era comparado. Licao no 9.
# A Restricao Celestial e a primeira Origem com lista por RAMO: a celula dela traz
# as duas separadas por <br>, cada uma com o nome do ramo em italico na frente.
_P9 = open(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '09-origens.md'), encoding='utf-8').read()
_POR_NORMA = {norma(p): p for p in TODAS}


def _le_origens(texto):
    """{nome da Origem, ou 'Origem · ramo': [as quatro pericias]}, lido da peca 09."""
    saida, atual = {}, None
    for linha in texto.splitlines():
        cab = re.match(r'#{3,4}\s+(.+?)\s*$', linha)
        if cab:
            atual = cab.group(1).strip()
            continue
        if atual is None or '**Perícias**' not in linha or linha.count('|') < 3:
            continue
        for pedaco in linha.split('|')[2].split('<br>'):
            pedaco = pedaco.strip()
            if not pedaco:
                continue
            ramo = re.match(r'\*([^*]+?):\*\s*(.+)$', pedaco)
            chave = f'{atual} · {ramo.group(1).strip()}' if ramo else atual
            corpo = ramo.group(2) if ramo else pedaco
            # A peca e a fonte da LISTA; o quadro acima e a fonte da GRAFIA.
            saida[chave] = [_POR_NORMA.get(norma(p.strip()), p.strip())
                            for p in corpo.split('·') if p.strip()]
    return saida


ORIGENS = _le_origens(_P9)
# Guarda de contagem: extrator que para de achar sai VERDE em silencio, e isso e a
# licao no 8 por outra porta. Cinco principais + Corpo Amaldicoado + os DOIS ramos
# da Restricao Celestial.
ORIGENS_ESPERADAS = 8

# Termos que ja significam outra coisa dentro do projeto.
INTERNOS = {
    'Muro', 'Punho', 'Brasa', 'Estocada', 'Alcance', 'Oficio', 'Elo', 'Folego',
    'Regua', 'Torrente', 'Explosivo', 'Arremate', 'Sombra', 'Enxame', 'Coro',
    'Bastiao', 'Vanguarda', 'Guia', 'Emanador', 'Evocador', 'Vigor', 'Intelecto',
    'Espirito', 'Maestria', 'Classe', 'Refino', 'Caminho', 'Trilha', 'Origem',
    'Pacto', 'Grau', 'Selo', 'Barreira', 'Dominio', 'Familia', 'Melhoria',
    'Restricao', 'Passiva', 'Forma', 'Integridade', 'Aptidao', 'Defesa',
}

# Colisoes conhecidas e ACEITAS de proposito. Nao falham o validador, mas
# aparecem no relatorio para nao serem confundidas com descuido depois.
COLISOES_ACEITAS = {
    'Provocar': 'o manual usa "sem provocar ataque de oportunidade" 3x. Decidido na '
                'v0.16 que a frase e comum demais para confundir na mesa.',
    'Natureza': 'o manual tem a Passiva "Segunda Natureza". Duas palavras contra uma, '
                'e a Passiva e rara. Colisao fraca, aceita.',
    'Historia': 'aparece 1x no manual em prosa solta. Pela nota de metodo da v0.6, '
                'prosa solta nao e colisao.',
    'Ocultismo': 'v0.226: o manual cita a PERICIA de proposito, como requisito da '
                 'Expansao sem Barreiras (especializacao em Ocultismo). E o nome da '
                 'pericia usado como pericia, e nao um termo do Fundamento que colide.',
}


def bloco(titulo):
    print()
    print('=' * 88)
    print(titulo)
    print('=' * 88)


# --------------------------------------------------------------------------
bloco('1. CONTAGEM POR ATRIBUTO')

total = len(TODAS)
for atr, lista in PERICIAS.items():
    n = len(lista)
    print(f'  {atr:<16} {n:>2} pericias  {n/total:>5.0%}   ' + ' · '.join(lista))
print(f'\n  total: {total} pericias, {len(OFICIOS)} oficios')

if not 21 <= total <= 25:
    erro(f'{total} pericias — a peca 07 declara 23')
if not OFICIOS:
    erro('nao consegui ler a lista de oficios da peca 07 (o titulo do §5 mudou?)')
if OFICIOS_DECLARADOS is None:
    erro('o titulo do §5 da peca 07 nao diz quantos oficios sao, por extenso')
elif len(OFICIOS) != OFICIOS_DECLARADOS:
    erro(f'a peca 07 lista {len(OFICIOS)} oficios e o titulo dela declara '
         f'{OFICIOS_DECLARADOS}')
if PERICIAS['Constituicao']:
    erro('Constituicao ganhou pericia — a peca 4 decidiu que ela nao tem nenhuma')

# --------------------------------------------------------------------------
bloco('2. PESO DE MESA — contagem nao e a mesma coisa que valor')

# Quantas vezes cada pericia e rolada numa campanha tipica, em peso relativo.
# Serve para responder "qual atributo vale mais fora de combate", que a contagem
# crua responde errado: uma Sentir Energia vale por quatro pericias de nicho.
PESO = {'Sentir Energia': 4, 'Percepcao': 3, 'Intuicao': 2, 'Investigacao': 2,
        'Atletismo': 2, 'Furtividade': 2, 'Persuasao': 2, 'Acrobacia': 1.5,
        'Ocultismo': 1.5, 'Intimidacao': 1.5, 'Medicina': 1, 'Enganacao': 1}

peso_total = sum(PESO.get(p, 1) for p in TODAS)
print(f"  {'atributo':<16} {'pericias':>9} {'contagem':>9} {'peso de mesa':>13}")
pesos = {}
for atr, lista in PERICIAS.items():
    w = sum(PESO.get(p, 1) for p in lista) / peso_total
    pesos[atr] = w
    print(f'  {atr:<16} {len(lista):>9} {len(lista)/total:>8.0%} {w:>12.0%}')

print('\n  Antes da v0.16, com Sentir Energia e Percepcao em Inteligencia:')
print('    Inteligencia 56% de peso, Essencia 21%.')
print('  A troca nao mudou a contagem para melhor — mudou o peso, que e o que importa.')

lider = max(pesos, key=pesos.get)
if pesos[lider] > 0.50:
    erro(f'{lider} concentra {pesos[lider]:.0%} do valor de mesa — vira atributo obrigatorio')

# --------------------------------------------------------------------------
bloco('3. NENHUM NOME REPETIDO, E NENHUM EM DUAS LISTAS')

vistos = {}
for atr, lista in PERICIAS.items():
    for p in lista:
        if norma(p) in vistos:
            erro(f'"{p}" aparece em {vistos[norma(p)]} e em {atr}')
        vistos[norma(p)] = atr
for o in OFICIOS:
    if norma(o) in vistos:
        erro(f'"{o}" e pericia ({vistos[norma(o)]}) e oficio ao mesmo tempo')
    vistos[norma(o)] = 'oficio'
print(f'  {len(vistos)} nomes, todos unicos entre pericias e oficios.')

# --------------------------------------------------------------------------
bloco('4. AS FIXAS DE CADA CAMINHO')

print(f"  {'Caminho':<12} {'pericias fixas':<34} atributos")
for nome, d in CAMINHOS.items():
    fora = [p for p in d['pericias'] if p not in TODAS]
    atrs = [vistos[norma(p)] for p in d['pericias'] if norma(p) in vistos]
    print(f"  {nome:<12} {' · '.join(d['pericias']):<34} {' + '.join(a[:3] for a in atrs)}")
    if len(d['pericias']) != CAM_FIXAS:
        erro(f'{nome} fixa {len(d["pericias"])} pericias, deveria fixar {CAM_FIXAS}')
    if fora:
        erro(f'{nome} fixa o que nao existe no quadro: {", ".join(fora)}')
    if len(set(map(norma, d['pericias']))) != len(d['pericias']):
        erro(f'{nome} repete uma pericia nas proprias fixas')

# -- 4.1: a tabela da peca 7 e a dona, e as copias dela ----------------------
# v0.271. A perícia fixa do Bastiao trocou de `Intimidacao` para `Provocar`, e a
# troca foi em NOVE lugares — e nenhum validador comparava a tabela da peca 7 com
# a lista acima, nem as fixas que a Kaori declara com as do Caminho dela. O
# conferir-ficha.py cruzava so a peca 8 com o dados.js. Esta sub-checagem le a
# peca 7 como dona e cobra: a lista deste arquivo, a tabela da peca 8, as tabelas
# dos capitulos 3, 6 e 8 do livro, e a frase "Do Caminho, fixas: X e Y" da Kaori
# na peca 8 e no capitulo 6. O livro nao traz o Evocador desde a v0.270, e o que
# ele traz tem de bater.
def _par41(cel):
    return tuple(sorted(norma(x.strip(' `*')) for x in re.split(r'\s*·\s*| e ', cel.strip()) if x.strip(' `*')))
_m41 = re.search(r'As duas fixas são a assinatura do Caminho.*?\n\n((?:\|[^\n]*\n)+)', _P7, re.S)
DONO41 = {}
if _m41:
    for _l in _m41.group(1).split('\n')[2:]:
        _mm = re.match(r'\|\s*\*\*([^*]+)\*\*\s*\|\s*([^|]+?)\s*\|', _l)
        if _mm:
            DONO41[norma(_mm.group(1))] = _par41(_mm.group(2))
if len(DONO41) != len(CAMINHOS):
    erro(f'4.1: li {len(DONO41)} Caminho(s) na tabela de fixas da peca 7 e esta lista tem '
         f'{len(CAMINHOS)} — a tabela dona sumiu ou mudou de forma')
else:
    _aqui = {norma(n): _par41(' · '.join(d['pericias'])) for n, d in CAMINHOS.items()}
    for _n, _v in _aqui.items():
        if DONO41.get(_n) != _v:
            erro(f'4.1: este validador fixa {_v} no {_n}, e a peca 7 diz {DONO41.get(_n)}')
    _AQ = os.path.dirname(os.path.abspath(__file__))
    _LIV41 = os.path.join(_AQ, '..', '05-material', 'livro', 'manual')
    def _abre41(p):
        return open(p, encoding='utf-8').read() if os.path.isfile(p) else ''
    _P8t = _abre41(os.path.join(_AQ, '08-criacao-de-personagem.md'))
    _C12 = _abre41(os.path.join(_LIV41, '12-pericias-e-oficios.md'))
    _C20 = _abre41(os.path.join(_LIV41, '20-criacao-de-personagem.md'))
    _C35 = _abre41(os.path.join(_LIV41, '35-caminhos-e-trilhas.md'))
    _copias41 = []
    for _rot, _txt, _rx in (
            ('peca 8', _P8t, r'^\|\s*\*\*([^*]+)\*\*\s*\|\s*\d+ \(d\d+\)\s*\|\s*\d+\s*\|\s*\d+\s*\|\s*([^|]+?)\s*\|'),
            ('livro, capitulo 6', _C20, r'^\|\s*\*\*([^*]+)\*\*\s*\|\s*\d+ \(d\d+\)\s*\|\s*\d+\s*\|\s*\d+\s*\|\s*([^|]+?)\s*\|'),
            ('livro, capitulo 3', _C12.split('**Perícias fixas por Caminho**')[-1].split('\n\n', 2)[1] if '**Perícias fixas por Caminho**' in _C12 else '',
             r'^\|\s*\*\*([^*]+)\*\*\s*\|\s*([^|]+?)\s*\|\s*$')):
        _lidos = {norma(m.group(1)): _par41(m.group(2)) for m in re.finditer(_rx, _txt, re.M)}
        _copias41.append((_rot, _lidos))
    _cap35 = {}
    for _m in re.finditer(r'^## (\S+)\n(.*?)(?=^## |\Z)', _C35, re.S | re.M):
        _mf = re.search(r'\|\s*\*\*Perícias fixas\*\*\s*\|\s*([^|]+?)\s*\|', _m.group(2))
        if _mf:
            _cap35[norma(_m.group(1))] = _par41(_mf.group(1))
    _copias41.append(('livro, capitulo 8', _cap35))
    for _rot, _lidos in _copias41:
        if len(_lidos) < 4:
            erro(f'4.1: li {len(_lidos)} Caminho(s) nas fixas da copia `{_rot}` — a leitura quebrou')
        for _n, _v in _lidos.items():
            if DONO41.get(_n) != _v:
                erro(f'4.1: a copia `{_rot}` fixa {_v} no {_n}, e a peca 7 diz {DONO41.get(_n)}')
    # a Kaori: o Caminho dela e as fixas que ela declara
    for _rot, _txt, _rxc in (('peca 8', _P8t, r'\*\*Caminho\.\*\*\s*(\w+)'),
                             ('livro, capitulo 6', _C20, r'### Caminho e Trilha\s*\n\s*\*\*(\w+)\*\*')):
        _mc, _mk = re.search(_rxc, _txt), re.search(r'Do Caminho, fixas: ([^.]+)\.', _txt)
        if not (_mc and _mk):
            erro(f'4.1: nao achei o Caminho ou as fixas da Kaori na copia `{_rot}`')
        elif DONO41.get(norma(_mc.group(1))) != _par41(_mk.group(1)):
            erro(f'4.1: a Kaori da copia `{_rot}` e {_mc.group(1)} e declara as fixas '
                 f'{_par41(_mk.group(1))}, e a peca 7 da {DONO41.get(norma(_mc.group(1)))}')
    print(f'  4.1: a peca 7 e a dona; conferidas a lista daqui, {len(_copias41)} copias de tabela e a Kaori em duas')

repetidas = [p for p in TODAS
             if sum(1 for d in CAMINHOS.values() if p in d['pericias']) > 1]
print(f"\n  fixada por mais de um Caminho: {', '.join(repetidas) if repetidas else '—'}")
print('  As fixas sao a assinatura do Caminho. Repetir demais apaga a diferenca entre eles.')

# Quanto cada Caminho ganha de graca. Se um ganha muito mais que outro, ele leva
# na pratica uma escolha livre a mais. Informativo: o peso abaixo e estimado.
print(f"\n  {'Caminho':<12} {'peso das duas fixas':>20}")
cargas = {}
for nome, d in CAMINHOS.items():
    c = sum(PESO.get(p, 1) for p in d['pericias'])
    cargas[nome] = c
    print(f'  {nome:<12} {c:>20.1f}')
lo, hi = min(cargas.values()), max(cargas.values())
print(f'\n  faixa: {lo:.1f} a {hi:.1f}. Diferenca de {hi - lo:.1f} sobre 8 pericias treinadas.')
if hi - lo > 3.0:
    erro(f'as fixas de {max(cargas, key=cargas.get)} valem {hi/lo:.1f}x as de '
         f'{min(cargas, key=cargas.get)} — o Caminho mais bem servido ganha uma escolha livre disfarcada')
else:
    print('  Dentro do ruido: as 4 escolhas livres corrigem sozinhas essa diferenca.')

# --------------------------------------------------------------------------
bloco('5. FRACAO TREINADA')

if FAIXA_TREINADA is None:
    erro('nao achei a faixa de pericia treinada na peca 7 §7 — sem ela a fracao '
         'abaixo nao tem contra o que ser julgada')
    FAIXA_TREINADA = (0.0, 1.0)
if OFI_N is None or OFI_DONO is None or OFI_TROCA is None:
    erro('nao consegui ler do §6 da peca 07 quantos oficios existem, de quem eles '
         'sao (uma declaracao so) ou por quantas pericias eles se trocam — extrator '
         'que para de achar sai verde calado, e a fracao abaixo nao teria com que '
         'ser calculada')
    OFI_N = OFI_N or 0
    OFI_TROCA = OFI_TROCA or 0

base_p = CAM_FIXAS + CAM_LIVRES + ORI_PERICIAS
# As rotas que a peca 7 §6 publica. Decisao do Mizuki na v0.263: a faixa julga so
# a de BASE — o que a regra da antes de qualquer troca. As trocas sao do jogador,
# tem preco escrito, e aqui sao impressas sem julgamento.
_mA = re.search(r'(\w+) das cinco à sua escolha se trocam por treino em UMA arma', _S6t)
POR_ARMA = _PN.get(_mA.group(1).lower()) if _mA else None
if POR_ARMA is None:
    erro('nao achei no §6 da peca 7 quantas pericias uma arma custa — as rotas com '
         'arma nao teriam como ser impressas')
    POR_ARMA = 0
rotas = []
for _armas in (0, 1, 2):
    for _troca in (False, True):
        rotas.append((f'{_armas} arma(s)' + (', troca os oficios' if _troca else ''),
                      base_p - _armas * POR_ARMA + (OFI_TROCA if _troca else 0),
                      0 if _troca else OFI_N,
                      _armas == 0 and not _troca))
print(f'  {CAM_FIXAS} fixas + {CAM_LIVRES} livres do Caminho + {ORI_PERICIAS} da Origem, e os '
      f'{OFI_N} oficios da {OFI_DONO}; os dois se trocam por {OFI_TROCA} pericia, e '
      f'{POR_ARMA} pericias por uma arma:\n')
print(f"  {'rota':<30}{'pericias':>16}{'oficios':>16}")
for nome, p, o, base in rotas:
    marca = 'BASE, julgada' if base else 'troca, so impressa'
    print(f'  {nome:<30}{f"{p} de {total} = {p/total:.0%}":>16}'
          f'{f"{o} de {len(OFICIOS)} = {o/len(OFICIOS):.0%}":>16}   {marca}')
    if not base:
        continue
    if not FAIXA_TREINADA[0] <= p / total <= FAIXA_TREINADA[1]:
        erro(f'a rota de base da {p/total:.0%} de pericia, fora da faixa '
             f'{FAIXA_TREINADA[0]:.0%}-{FAIXA_TREINADA[1]:.0%} da peca 7 §7')
    if o / len(OFICIOS) > 0.35:
        erro(f'a rota de base da {o/len(OFICIOS):.0%} de oficio — oficio precisa ser raro para virar cena')
print(f'\n  faixa da peca 7 §7, para a rota de base: {FAIXA_TREINADA[0]:.0%} a {FAIXA_TREINADA[1]:.0%}')
print('  Abaixo disso a ficha esvazia. Acima, "ser treinado" para de significar algo.')
print('  As trocas sao do jogador e tem preco escrito: elas saem da faixa de proposito.')

# --------------------------------------------------------------------------
bloco('5.1 AS LISTAS DE ORIGEM')
print(f'  lidas da peca 09: {len(ORIGENS)} (esperadas {ORIGENS_ESPERADAS})')
if len(ORIGENS) != ORIGENS_ESPERADAS:
    erro(f'o extrator achou {len(ORIGENS)} listas de Origem na peca 09 e '
         f'esperava {ORIGENS_ESPERADAS} — extrator que para de achar sai verde calado')
print(f"\n  {'Origem':<34}{'oferece':>9}   pericias")
for nome, lista in ORIGENS.items():
    fora = [p for p in lista if p not in TODAS]
    print(f"  {nome:<34}{len(lista):>9}   {' · '.join(lista)}")
    if len(lista) != 4:
        erro(f'{nome} oferece {len(lista)} pericias, e a peca 09 diz quatro')
    if fora:
        erro(f'{nome} oferece o que nao existe no quadro: {", ".join(fora)}')
    if len(set(map(norma, lista))) != len(lista):
        erro(f'{nome} repete uma pericia na propria lista')

# 5.1.1 — o que a propria peca 09 NEGA aquela Origem nao pode voltar pela lista.
# Ela nasceu do arnes da v0.129: o ramo sem energia diz "sem Sentir Energia" com
# todas as letras, e o poco de Destreza+Forca a excluia POR ACASO. Perturbar a
# lista pondo Sentir Energia nela saia VERDE — ninguem estava conferindo.
# A negacao e LIDA da peca, e nao escrita aqui: licao no 9.
print('\n  o que a peca 09 nega a uma Origem, conferido contra a lista dela:')
_NEGA = {}
_atual = None
for _l in _P9.splitlines():
    _c = re.match(r'#{3,4}\s+(.+?)\s*$', _l)
    if _c:
        _atual = _c.group(1).strip()
        continue
    if _atual is None or '**O que muda**' not in _l or _l.count('|') < 3:
        continue
    for _p in _l.split('|')[2].split('<br>'):
        _r = re.match(r'\*([^*]+?):\*\s*(.+)$', _p.strip())
        _k = f'{_atual} · {_r.group(1).strip()}' if _r else _atual
        _corpo = _r.group(2) if _r else _p
        _achados = [m.strip() for m in re.findall(r'sem ([A-ZÀ-Ü][\wÀ-ÿ ]*)', _corpo)]
        _NEGA[_k] = [_POR_NORMA[norma(m)] for m in _achados if norma(m) in _POR_NORMA]

_negadas = 0
for nome, proibidas in _NEGA.items():
    if not proibidas:
        continue
    _negadas += 1
    print(f'    {nome:<40} nega {", ".join(proibidas)}')
    for p in proibidas:
        if norma(p) in {norma(x) for x in ORIGENS.get(nome, [])}:
            erro(f'{nome} oferece {p} na lista de perícia, e o texto dela nega {p}')
if _negadas == 0:
    erro('nenhuma negacao "sem <Pericia>" foi lida da peca 09 — o extrator parou de achar')

print('\n  Origem cuja lista o Caminho ja fixa por inteiro (a escolha da Origem morreria):')
achou = False
for o_nome, o_lista in ORIGENS.items():
    for c_nome, c in CAMINHOS.items():
        if set(o_lista) <= set(c['pericias']):
            erro(f'{o_nome} tem as quatro pericias ja fixadas por {c_nome}')
            achou = True
if not achou:
    print('    nenhuma. Sobreposicao parcial e esperada — quem cair nela escolhe outra da lista.')

usadas = {p for l in ORIGENS.values() for p in l}
print(f'\n  as {len(ORIGENS)} listas tocam {len(usadas)} das {total} pericias')

# --------------------------------------------------------------------------
bloco('5.2 O TREINO TEM DOIS GRAUS — e nenhuma linha viva diz que ele e binario')
# --------------------------------------------------------------------------
# v0.263. A peca 4 §7 listava "se treino em pericia tem graus... binario por ora"
# como pergunta aberta, e a peca 2 §6 dizia "o treino e binario". A especializacao
# da peca 11 §3 — metade da maestria de novo, do nivel 10 em diante — e o segundo
# grau desde a v0.212: cinquenta e uma versoes com as pecas discordando, e nenhuma
# checagem comparava. A RASCUNHO da Expansao sem Barreiras anotou o achado e ele
# ficou la.
#
# A regra e lida, nao escrita: se a peca 11 publica a especializacao, nenhuma
# linha VIVA das pecas nem do livro pode chamar o treino de binario. Linha viva
# e o que sobra sem os trechos riscados (~~), e que nao registra um FECHADO.
# A citacao ('>') NAO e historia neste projeto: a regra da especializacao mora
# numa citacao da peca 11, e as caixas de regra do livro tambem sao '>' — a
# primeira versao desta checagem pulava citacao e nao achava a propria regra.
# Se a especializacao sair da peca 11, dizer "binario" volta a ser permitido —
# e esse e o contra-teste.
_AQ52 = os.path.dirname(os.path.abspath(__file__))
_P11 = open(os.path.join(_AQ52, '11-aptidoes-e-refino.md'), encoding='utf-8').read()
_espec = [l for l in _P11.splitlines()
          if re.search(r'\*\*especializar\*\* um que já treina', l)
          and 'metade da maestria' in l]
_LIV52 = os.path.join(_AQ52, '..', '05-material', 'livro', 'manual')
_arqs52 = sorted(glob.glob(os.path.join(_AQ52, '*.md'))) + \
          sorted(glob.glob(os.path.join(_LIV52, '*.md')))
_vivas = []
for _a in _arqs52:
    for _n, _l in enumerate(open(_a, encoding='utf-8').read().splitlines(), 1):
        _v = re.sub(r'~~.*?~~', '', _l)
        if re.search(r'fechad', _v, re.I):
            continue
        if re.search(r'trein', _v, re.I) and re.search(r'bin[aá]ri', _v, re.I):
            _vivas.append(f'{os.path.basename(_a)}:{_n}')
if len(_arqs52) < 20:
    erro(f'5.2: li {len(_arqs52)} arquivo(s) entre pecas e livro — a varredura '
         'parou de achar o que ela confere, e passaria verde a toa')
elif not _espec:
    print('  a peca 11 nao publica a especializacao: o treino e de um grau so, e '
          'chamar ele de binario e permitido')
elif _vivas:
    erro(f'5.2: a peca 11 publica a especializacao (o segundo grau do treino), e '
         f'{len(_vivas)} linha(s) viva(s) ainda chamam o treino de binario: '
         f'{" · ".join(_vivas)}')
else:
    print(f'  [x] a peca 11 publica a especializacao, e nenhuma linha viva das '
          f'{len(_arqs52)} pecas e capitulos chama o treino de binario')

bloco('6. TODA PERICIA E ALCANCAVEL')

print('  Com 4 pericias e 1 oficio de escolha livre em todo o quadro, qualquer nome')
print('  e alcancavel por qualquer Caminho. Nao existe pericia orfa desde a v0.16 —')
print('  antes, Prestidigitacao e Jogatina so vinham da Origem.')
nunca_fixa = [p for p in TODAS if not any(p in d['pericias'] for d in CAMINHOS.values())]
print(f'\n  pericias que nenhum Caminho fixa ({len(nunca_fixa)} de {total}): {", ".join(nunca_fixa)}')
print('  Isso e esperado: so 10 das pericias sao assinatura de alguem.')

# --------------------------------------------------------------------------
bloco('7. COLISAO DE TERMO — contra o Fundamento e contra o proprio projeto')

AQUI = os.path.dirname(os.path.abspath(__file__))
DOCX = os.path.join(AQUI, '..', '..', 'manual', 'Fundamento-MANUAL-v7.docx')

texto_manual = None
try:
    import docx  # python-docx
    doc = docx.Document(DOCX)
    partes = [p.text for p in doc.paragraphs]
    for t in doc.tables:
        for r in t.rows:
            for c in r.cells:
                partes.append(c.text)
    texto_manual = '\n'.join(partes)
except Exception as e:
    print(f'  (manual nao lido: {e})')
    print('  A checagem contra o Fundamento foi PULADA. Rode com python-docx instalado')
    print('  e o manual em manual/Fundamento-MANUAL-v7.docx antes de fechar versao.')

nomes = TODAS + OFICIOS
internos_norm = {norma(x) for x in INTERNOS}
achados = []

for n in nomes:
    if norma(n) in internos_norm:
        erro(f'"{n}" ja e termo interno do projeto — colisao para dentro')
    if texto_manual:
        pat = re.compile(r'\b' + re.escape(norma(n)) + r'\b')
        linhas = [l.strip() for l in texto_manual.split('\n')
                  if l.strip() and pat.search(norma(l))]
        if linhas:
            achados.append((n, len(linhas), linhas[0][:58]))

if texto_manual:
    print('  Nota de metodo da v0.6: separar TERMO DEFINIDO de PROSA SOLTA.\n')
    for n, q, amostra in achados:
        if n in COLISOES_ACEITAS:
            print(f'  ACEITA  {n:<18} {q}x no manual')
            print(f'          motivo: {COLISOES_ACEITAS[n]}')
        else:
            erro(f'"{n}" aparece {q}x no manual e nao esta na lista de aceitas: "{amostra}..."')
    nao_apareceram = [n for n in COLISOES_ACEITAS if n not in [a[0] for a in achados]]
    for n in nao_apareceram:
        if n in nomes:
            print(f'  (declarada aceita mas nao aparece mais no manual: {n} — pode sair da lista)')
    if not achados:
        print('  Nenhum dos nomes aparece no manual.')
else:
    PULADAS.append('7. colisao de termo contra o Fundamento (sem o manual)')
    print('  PULADA — nenhum nome foi batido contra o manual.')

# --------------------------------------------------------------------------
bloco('8. A ESCADA DE DIFICULDADE — a peca 4 §2 e a dona, e as copias batem')

# Esta secao tinha os cinco degraus escritos aqui dentro e so IMPRIMIA uma
# tabela: nao conferia nada. A escada esta republicada em QUATRO lugares -- a
# peca 4, a peca 1, a peca 11 e o capitulo 10 do livro -- e o numero dentro do
# validador era a quinta copia, sem ninguem comparando. Licao no 9, na variante
# que este projeto ja pagou tres vezes: checagem que se mede contra a propria
# constante sai verde quando se perturba a constante.


def maestria(nv):
    return 1 + (nv - 2) // 8


def investido(nv):
    return min(6, 3 + (nv - 2) // 8)


def chance(cd, nv, treinado=True):
    """o modelo do projeto: d20 + atributo investido + maestria, se treinado"""
    alvo = cd - (investido(nv) + (maestria(nv) if treinado else 0))
    return max(0, min(100, (21 - alvo) * 5))


def _tabela(texto, titulo):
    """as linhas de tabela que vem DEPOIS de um titulo, ate a tabela acabar"""
    i = texto.find(titulo)
    if i < 0:
        return []
    linhas, comecou = [], False
    for lin in texto[i:].split('\n')[1:]:
        t = lin.strip()
        if t.startswith('|'):
            comecou = True
            if set(t) <= set('|-: '):          # a linha de tracos
                continue
            linhas.append([c.strip() for c in t.strip('|').split('|')])
            continue
        if comecou:                            # a tabela acabou
            break
    return linhas


_AQUI = os.path.dirname(os.path.abspath(__file__))
_P4 = open(os.path.join(_AQUI, '04-pericias-e-testes.md'), encoding='utf-8').read()

# A escada sai da dona. O cabecalho dela diz QUAIS niveis ela publica, entao
# uma coluna nova na peca entra aqui sozinha.
_linhas = _tabela(_P4, '### 2.1 A escada fixa')
_cab = _linhas[0] if _linhas else []
NIVEIS = [int(m.group(1)) for c in _cab
          for m in [re.search(r'n[ií]vel\s+(\d+)', c)] if m]
_lim = lambda c: c.strip().strip('*').strip()
ESCADA = [(int(_lim(cs[0])), _lim(cs[1]), [_lim(c).rstrip('%').strip() for c in cs[2:]])
          for cs in _linhas[1:] if cs and _lim(cs[0]).isdigit()]

if not ESCADA or not NIVEIS:
    erro('nao consegui ler a escada da peca 4 §2 — o formato da tabela mudou, e '
         'formato que nao casa faz esta secao virar decoracao')
else:
    print(f'  a peca 4 publica {len(ESCADA)} degraus, nos niveis {NIVEIS}')
    print(f"  {'dificuldade':<26}" + ''.join(f'nv{nv:<6}' for nv in NIVEIS)
          + f'   sem treino no nv{NIVEIS[-1]}')
    for cd, rot, _ in ESCADA:
        linha = f'  {"CD " + str(cd) + " (" + rot + ")":<26}'
        for nv in NIVEIS:
            linha += f'{chance(cd, nv):>4}%   '
        print(linha + f'{chance(cd, NIVEIS[-1], treinado=False):>10}%')

    # 8.1 cada porcentagem publicada e a que o modelo da
    _erradas = [f'CD {cd} no nv{nv}: a peca diz {pub}%, o modelo da {chance(cd, nv)}%'
                for cd, _, pcts in ESCADA
                for nv, pub in zip(NIVEIS, pcts)
                if not pub.isdigit() or int(pub) != chance(cd, nv)]
    for e in _erradas:
        erro(e)
    if not _erradas:
        print(f'  [x] as {len(ESCADA) * len(NIVEIS)} porcentagens publicadas batem '
              f'com d20 + atributo investido + maestria')

    # 8.2 as duas propriedades que a peca declara de proposito. Elas nao estao
    # escritas como numero aqui: saem da escada lida, e o que se confere e que
    # a prosa que as justifica continua na peca.
    _baixa, _alta = ESCADA[0][0], ESCADA[-1][0]
    # v0.261: a promessa da ponta de baixo MUDOU. A escada antiga prometia que o
    # degrau mais baixo so virava automatico no FIM; a nova ancora o `fácil` em
    # CD 6 de proposito, e ele vira automatico cedo. Decisao do Mizuki: "um cara
    # com atributo bom, treinado, passa com seus 50% no começo do jogo. Isso n
    # e facil". O que a peca promete agora e' outra coisa, e e' isso que se
    # confere: ele NAO pode ser automatico ja no primeiro nivel, senao nao havia
    # por que rolar; e quem nao investiu nem treinou tem de falhar ali as vezes.
    if chance(_baixa, NIVEIS[0]) == 100:
        erro(f'o degrau mais baixo (CD {_baixa}) ja e 100% no nv{NIVEIS[0]} para quem '
             f'investiu e treinou — um degrau que nunca falha nao precisa de rolagem')
    elif chance(_baixa, NIVEIS[-1]) != 100:
        erro(f'o degrau mais baixo (CD {_baixa}) nao chega a 100% no nv{NIVEIS[-1]}, '
             f'e a peca promete que ele vira automatico ao longo da campanha')
    elif chance(_baixa, NIVEIS[0], treinado=False) == 100:
        erro(f'o degrau mais baixo (CD {_baixa}) ja e automatico no nv{NIVEIS[0]} para '
             f'quem NAO treinou — a peca diz que ele ainda falha ali')
    else:
        print(f'  [x] CD {_baixa} e {chance(_baixa, NIVEIS[0])}% no nv{NIVEIS[0]} e automatica '
              f'no nv{NIVEIS[-1]}; sem treino ainda falha '
              f'{100-chance(_baixa, NIVEIS[0], treinado=False)}% no comeco')

    if chance(_alta, NIVEIS[0]) != 0:
        erro(f'o degrau mais alto (CD {_alta}) da {chance(_alta, NIVEIS[0])}% no '
             f'nv{NIVEIS[0]}, e a peca reserva ele para o que "deveria ser impossivel"')
    elif chance(_alta, NIVEIS[-1]) > 50:
        erro(f'o degrau mais alto (CD {_alta}) chega a {chance(_alta, NIVEIS[-1])}% '
             f'no nv{NIVEIS[-1]}, e a peca diz que ele "nunca vira confortavel"')
    else:
        print(f'  [x] CD {_alta} e impossivel no nv{NIVEIS[0]} e ainda incomoda no '
              f'nv{NIVEIS[-1]} ({chance(_alta, NIVEIS[-1])}%)')

    for _frase in ('é quase automático, e isso é escolha', 'ainda é um quarto de chance'):
        if _frase not in _P4:
            erro(f'a peca 4 perdeu a frase que justifica a ponta: "{_frase}"')

    # 8.3 as copias. Elas republicam a escada e nenhuma era conferida.
    _DONA = {cd: norma(rot) for cd, rot, _ in ESCADA}
    _SIST = os.path.dirname(_AQUI)          # .../sistema
    _COPIAS = [
        ('peca 1 §Pericias', os.path.join(_AQUI, '01-atributos-acerto-defesa.md'),
         r'\|\s*CD (\d+) \(([^)]+)\)\s*\|'),
        ('peca 11 §Esteio', os.path.join(_AQUI, '11-aptidoes-e-refino.md'),
         r'\|\s*CD (\d+) — ([^|]+?)\s*\|'),
        ('capitulo 10 do livro',
         os.path.join(_SIST, '05-material', 'livro', 'manual', '10-como-jogar.md'),
         r'^\|\s*(\d+)\s*\|\s*([^|]+?)\s*\|'),
    ]
    for _nome, _cam, _pad in _COPIAS:
        if not os.path.exists(_cam):
            PULADAS.append(f'8.3 a copia da escada em {_nome} (arquivo nao existe)')
            print(f'  PULADA — {_nome} nao existe em {_cam}')
            continue
        _txt = open(_cam, encoding='utf-8').read()
        _achado = {}
        for _m2 in re.finditer(_pad, _txt, re.M):
            _cd, _rot = int(_m2.group(1)), norma(_m2.group(2))
            if _rot in _DONA.values():
                _achado[_cd] = _rot
        if not _achado:
            erro(f'{_nome}: nao achei a escada republicada — o formato mudou, e um '
                 f'formato que nao casa faz esta checagem virar decoracao')
        elif not set(_achado.items()) <= set(_DONA.items()):
            _fora = {k: v for k, v in _achado.items() if _DONA.get(k) != v}
            erro(f'{_nome} discorda da peca 4: a copia publica {_fora}, e a dona '
                 f'tem {_DONA}')
        else:
            _quantos = len(_achado)
            print(f'  [x] {_nome} republica {_quantos} degrau(s), todos iguais a peca 4')

# --------------------------------------------------------------------------
print('\n' + '=' * 88)
print('O ATRIBUTO PADRAO DE CADA OFICIO — v0.104')
print('=' * 88)
# Os onze oficios ganharam atributo padrao. A checagem confere que TODOS tem um,
# que ele e' um dos cinco atributos que a peca 8 governa, e que a distribuicao
# publicada na prosa bate com a tabela — sao duas copias do mesmo numero.
_ATRIB = ['Força', 'Destreza', 'Constituição', 'Inteligência', 'Essência']
_sec = _P7[_P7.find('### O atributo padrão de cada ofício'):]
_sec = _sec[:_sec.find('\n### ')] if '\n### ' in _sec else _sec
_pad = {}
for _l in _sec.split('\n'):
    _m = re.match(r'^\|\s*\*\*([^*]+)\*\*\s*\|\s*([A-ZÀ-Ú][a-zçãêéíóú]+)\s*\|', _l)
    if _m:
        _pad[norma(_m.group(1)).capitalize()] = _m.group(2)
_semp = [o for o in OFICIOS if o not in _pad]
_sobra = [o for o in _pad if o not in OFICIOS]
if not _sec:
    FALHAS.append('a peca 07 nao tem mais a secao do atributo padrao de oficio')
elif _semp:
    FALHAS.append('oficio sem atributo padrao na peca 07: ' + ', '.join(_semp))
elif _sobra:
    FALHAS.append('a tabela de atributo padrao tem oficio que nao existe: '
                  + ', '.join(_sobra))
else:
    _mau = [f'{o} ({a})' for o, a in _pad.items() if a not in _ATRIB]
    if _mau:
        FALHAS.append('atributo padrao que nao e um dos cinco: ' + ', '.join(_mau))
    else:
        _c = {a: sum(1 for v in _pad.values() if v == a) for a in _ATRIB}
        print('  ' + ' · '.join(f'{a} {_c[a]}' for a in _ATRIB))
        _m2 = re.search(r'\*\*(\w+) em Destreza, (\w+) em Inteligência, (\w+) em '
                        r'Essência, (\w+) em Força — e nenhuma em Constituição\.\*\*', _sec)
        _EXT = {'uma': 1, 'duas': 2, 'três': 3, 'quatro': 4, 'cinco': 5, 'seis': 6}
        if not _m2:
            FALHAS.append('a peca 07 nao publica mais a distribuicao dos atributos '
                          'padrao em prosa, no formato que esta checagem le')
        else:
            _esc = [_EXT.get(x.lower()) for x in _m2.groups()]
            if _esc != [_c['Destreza'], _c['Inteligência'], _c['Essência'], _c['Força']] \
                    or _c['Constituição'] != 0:
                FALHAS.append(f'a prosa da peca 07 diz {_esc} (Des/Int/Ess/For) e a '
                              f'tabela tem {[_c["Destreza"], _c["Inteligência"], _c["Essência"], _c["Força"]]}')
            else:
                print(f'  [x] os {len(_pad)} oficios tem atributo padrao, e a prosa bate com a tabela')
        if 'antes da rolagem' not in _sec:
            FALHAS.append('a peca 07 nao exige mais que o mestre diga o atributo ANTES '
                          'da rolagem — sem isso o padrao nao tira julgamento nenhum')
        else:
            print('  [x] o mestre diz o atributo antes da rolagem, e a peca cobra isso')

# --------------------------------------------------------------------------
print()
print('=' * 88)
if FALHAS:
    print(f'>>> {len(FALHAS)} PROBLEMA(S):')
    for f in FALHAS:
        print(f'    - {f}')
    sys.exit(1)
if PULADAS:
    print(f'>>> OK, mas {len(PULADAS)} checagem(ns) PULARAM:')
    for p in PULADAS:
        print(f'    - {p}')
    print('    O que pulou NAO foi conferido. Um verde que pulou checagem nao e')
    print('    um verde. Instale: pip install python-docx --break-system-packages')
else:
    print('>>> TUDO OK — o quadro fecha, a fracao esta na faixa, e as colisoes que existem')
    print('    estao declaradas com motivo em vez de esquecidas.')

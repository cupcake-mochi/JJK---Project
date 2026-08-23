#!/usr/bin/env python3
"""conferir-pactos.py — o validador dono da peca 22, `Pactos`.

Pacto e' a QUARTA economia de poder do sistema, e a unica das quatro formas
que precisa de numero e' a permanente. Entao este validador confere duas
coisas de naturezas diferentes: que as quatro formas continuam declaradas e
separadas, e que o unico teto que existe continua DERIVADO dos donos.

NENHUM VALOR FICA ESCRITO AQUI DENTRO:
  a fatia .................. DESENHO-trilhas.md, na raiz
  o Classe 0 no nivel 30 ... DESENHO-trilhas.md
  o teto de atributo ....... peca 2 §1
  o golpe simples .......... peca 6 §3, o vao entre as duas colunas da tabela
  o cambio de PE ........... peca 5 §4, a tabela de familia de entrega
  o piso do arredondamento . peca 1 §5.4
  as quatro travas ......... peca 8, Passo 8
  a lista de pecas ......... a pasta

O PAR DECLARADO desta peca e' a checagem 2, e ela mede RELACAO e nao
constante. O `0,50` nao esta escrito aqui: ele e' recalculado como
`camada / (teto de atributo / 2)`. Perturbar a camada sozinha acende;
perturbar o teto de atributo sozinho acende; e mudar os dois de forma
coerente fica VERDE de proposito — e' esse contra-teste que prova que ela
nao esta se medindo contra a propria constante (licao no 8).

Roda de 03-mecanica/, sem argumento. Sai com codigo 1 se algo quebrar.
Ele NAO le o .docx e NAO precisa de python-docx: nao existe jeito de ele
sair verde tendo pulado checagem por falta de biblioteca.
"""
import os
import re
import sys

MEC = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(MEC))
FALHAS = []


def erro(n, msg):
    FALHAS.append(f'{n}: {msg}')
    print(f'  !! {n}: {msg}')


def bloco(t):
    print()
    print('=' * 88)
    print(t)
    print('=' * 88)


def ler(nome, base=MEC):
    with open(os.path.join(base, nome), encoding='utf-8') as fh:
        return fh.read()


def limpo(s):
    return re.sub(r'[`*]', '', s).strip()


def celulas(linha):
    return [c.strip() for c in linha.strip().strip('|').split('|')]


def separador(linha):
    return set(linha.replace('|', '').strip()) <= set('-: ')


def num(s):
    """`1,50` -> 1.50. Devolve None se nao for numero."""
    m = re.search(r'(\d+(?:[,.]\d+)?)', s.replace('`', ''))
    return float(m.group(1).replace(',', '.')) if m else None


def tabela(texto, rx_cabecalho, ncols=None):
    """Le a tabela cujo CABECALHO casa com rx_cabecalho. Le a tabela pelo
    cabecalho, e nao pela posicao: tabela que muda de lugar continua sendo
    achada, e tabela que muda de forma acende em vez de sair verde vazia."""
    linhas, dentro = [], False
    for l in texto.split('\n'):
        if not dentro:
            if l.startswith('|') and rx_cabecalho.search(l):
                dentro = True
            continue
        if not l.startswith('|'):
            break
        if separador(l):
            continue
        c = celulas(l)
        if ncols is None or len(c) == ncols:
            linhas.append(c)
    return linhas


PECAS = sorted(f for f in os.listdir(MEC) if re.match(r'^\d\d-.*\.md$', f))
POR_NUM = {int(p[:2]): p for p in PECAS}

ALVO = '22-pactos.md'
if ALVO not in PECAS:
    print(f'  !! SETUP: {ALVO} nao esta na pasta — nao ha o que conferir')
    sys.exit(1)

P22 = ler(ALVO)
P22_L = P22.split('\n')
_p1 = ler(POR_NUM[1])
_p2 = ler(POR_NUM[2])
_p5 = ler(POR_NUM[5])
_p6 = ler(POR_NUM[6])
_p8 = ler(POR_NUM[8])
_TRILHAS = ler('DESENHO-trilhas.md', RAIZ)

print('=' * 88)
print('conferir-pactos.py — peca 22, Pactos')
print('=' * 88)
print(f'  pecas na pasta           : {len(PECAS)}')
print(f'  linhas da peca 22        : {len(P22_L)}')


# ---------------------------------------------------------------- 1 ---------
bloco('1. AS QUATRO FORMAS — declaradas, e cada uma diz se tem teto')

FORMAS = tabela(P22, re.compile(r'\|\s*forma\s*\|\s*quando se fecha\s*\|'), 4)
NOMES_FORMA = [limpo(c[0]) for c in FORMAS]
TETO_DE = {limpo(c[0]): limpo(c[2]) for c in FORMAS}

FORMAS_ESPERADAS = 4
print(f'  formas lidas do §1       : {len(FORMAS)}  (tem de ser {FORMAS_ESPERADAS})')
for _c in FORMAS:
    print(f'      {limpo(_c[0]):<14} teto: {limpo(_c[2])}')

if len(FORMAS) != FORMAS_ESPERADAS:
    erro('1', f'a tabela do §1 tem {len(FORMAS)} forma(s) e a peca fala de '
              f'{FORMAS_ESPERADAS} — ou a tabela mudou de forma, ou uma sumiu')
else:
    _mudas = [n for n, t in TETO_DE.items() if not t]
    if _mudas:
        erro('1', f'{len(_mudas)} forma(s) sem a coluna de teto preenchida: {_mudas}')
    else:
        print(f'  [x] as {len(FORMAS)} formas estao declaradas, e todas dizem se '
              'tem teto.')


# ---------------------------------------------------------------- 2 ---------
bloco('2. O TETO POR PACTO — camada / pior caso, e ele NAO esta escrito aqui')

_m2 = re.search(r'=\s*(\d+,\d+)\s*÷\s*(\d+)\s*\n\s*=\s*(\d+,\d+)\s*fatia', P22)
_m_esc = re.search(r'Escala de (\d+) a (\d+)', _p2)

if not _m2:
    erro('2', 'nao achei a derivacao do teto no §3.2 da peca 22 — o bloco '
              '`camada ÷ pior caso = teto` sumiu, e esta checagem parou de conferir')
elif not _m_esc:
    erro('2', 'nao achei a escala de atributo na peca 2 §1 — o teto do pior caso '
              'nao tem de onde sair, e esta checagem parou de conferir')
else:
    CAMADA = float(_m2.group(1).replace(',', '.'))
    PIOR_ESCRITO = int(_m2.group(2))
    POR_PACTO = float(_m2.group(3).replace(',', '.'))
    TETO_ATRIB = int(_m_esc.group(2))
    PIOR_CASO = TETO_ATRIB // 2
    ESPERADO = round(CAMADA / PIOR_CASO, 2) if PIOR_CASO else None

    print(f'  camada, lida da peca 22  : {CAMADA:.2f} fatia')
    print(f'  teto de atributo, peca 2 : {TETO_ATRIB}  ->  pior caso = {PIOR_CASO} pactos')
    print(f'  pior caso escrito no §3.2: {PIOR_ESCRITO}')
    print(f'  teto por pacto escrito   : {POR_PACTO:.2f}')
    print(f'  teto por pacto derivado  : {ESPERADO:.2f}' if ESPERADO is not None else '')

    if PIOR_ESCRITO != PIOR_CASO:
        erro('2', f'o §3.2 divide por {PIOR_ESCRITO} e o pior caso derivado da peca 2 '
                  f'e {PIOR_CASO} (metade do teto de atributo {TETO_ATRIB})')
    elif ESPERADO is None:
        erro('2', 'o pior caso deu zero — o teto de atributo da peca 2 nao produz '
                  'pacto nenhum')
    elif abs(POR_PACTO - ESPERADO) > 0.005:
        erro('2', f'o §3.2 escreve {POR_PACTO:.2f} fatia por pacto e a camada de '
                  f'{CAMADA:.2f} dividida por {PIOR_CASO} da {ESPERADO:.2f} — o teto '
                  'parou de ser derivado')
    else:
        print(f'  [x] o teto de {POR_PACTO:.2f} e a camada de {CAMADA:.2f} dividida '
              f'pelos {PIOR_CASO} pactos do pior caso.')


# ---------------------------------------------------------------- 3 ---------
bloco('3. QUANTIDADE — a tabela reconstroi `metade da Essencia` na escala inteira')

_q = tabela(P22, re.compile(r'\|\s*Ess[êe]ncia\s*\|\s*0\s*\|'))
_linha_q = next((c for c in _q if 'pactos' in limpo(c[0]).lower()), None)

if not _m_esc:
    erro('3', 'sem a escala da peca 2 nao ha contra o que reconstruir')
elif _linha_q is None:
    erro('3', 'nao achei a linha `pactos permanentes` na tabela do §3.1 — o '
              'extrator quebrou e esta checagem parou de conferir')
else:
    _lo, _hi = int(_m_esc.group(1)), int(_m_esc.group(2))
    _valores = [limpo(x) for x in _linha_q[1:]]
    _esperados = [str(e // 2) for e in range(_lo, _hi + 1)]
    print(f'  escala da peca 2         : {_lo} a {_hi}')
    print(f'  escrito no §3.1          : {" ".join(_valores)}')
    print(f'  derivado (metade, baixo) : {" ".join(_esperados)}')
    if len(_valores) != len(_esperados):
        erro('3', f'a tabela do §3.1 tem {len(_valores)} coluna(s) de Essencia e a '
                  f'escala da peca 2 vai de {_lo} a {_hi}, que sao {len(_esperados)}')
    elif _valores != _esperados:
        _diff = [f'Ess {_lo+i}: escrito {a}, derivado {b}'
                 for i, (a, b) in enumerate(zip(_valores, _esperados)) if a != b]
        erro('3', 'a tabela do §3.1 nao reconstroi metade da Essencia: ' + ' · '.join(_diff))
    else:
        print(f'  [x] as {len(_valores)} celulas reconstroem `metade da Essencia`, '
              'arredondando para baixo.')


# ---------------------------------------------------------------- 4 ---------
bloco('4. SO O PERMANENTE TEM TETO — e as outras tres dizem que nao tem')

_t4 = tabela(P22, re.compile(r'\|\s*forma\s*\|\s*vai para a ficha\?\s*\|'), 4)
print(f'  linhas do §1.1 lidas     : {len(_t4)}  (tem de ser {FORMAS_ESPERADAS})')

if len(_t4) != FORMAS_ESPERADAS:
    erro('4', f'a tabela do §1.1 tem {len(_t4)} linha(s) e as formas sao '
              f'{FORMAS_ESPERADAS}')
elif not FORMAS:
    erro('4', 'sem a tabela do §1 nao ha contra o que comparar')
else:
    _com_teto = []
    for _c in _t4:
        _nome, _precisa = limpo(_c[0]), limpo(_c[3]).lower()
        print(f'      {_nome:<14} precisa de teto: {_precisa}')
        if _nome not in NOMES_FORMA:
            erro('4', f'o §1.1 fala da forma `{_nome}` e o §1 nao a declara')
        if _precisa.startswith('sim'):
            _com_teto.append(_nome)
    if not [f for f in FALHAS if f.startswith('4:')]:
        if _com_teto != ['permanente']:
            erro('4', f'as formas com teto sao {_com_teto} — so o permanente '
                      'atravessa mesa, e so ele precisa de teto')
        else:
            _sem = [n for n in NOMES_FORMA if n != 'permanente' and
                    not re.match(r'n[ãa]o', TETO_DE.get(n, ''), re.I)]
            if _sem:
                erro('4', f'{_sem} nao dizem no §1 que nao tem teto — o §1 e o §1.1 '
                          'discordam')
            else:
                print('  [x] so o permanente tem teto, nas duas tabelas.')


# ---------------------------------------------------------------- 5 ---------
bloco('5. DANO POR RODADA — teto x fatia, com a fatia lida do DESENHO-trilhas')

_m_fatia = re.search(r'A fatia é `(\d+,\d+)`', _TRILHAS)
_moedas = tabela(P22, re.compile(r'\|\s*o teto de um pacto vale\s*\|'), 3)
_dpr = next((num(c[1]) for c in _moedas if 'dano por rodada' in limpo(c[0]).lower()), None)

if not _m_fatia:
    erro('5', 'nao achei `A fatia é ...` no DESENHO-trilhas.md — a regua de Trilhas '
              'e a dona da fatia, e esta checagem parou de conferir')
elif _dpr is None:
    erro('5', 'nao achei a linha `dano por rodada` na tabela de moedas do §3.2')
elif 'POR_PACTO' not in dir():
    erro('5', 'sem o teto por pacto da checagem 2 nao ha o que multiplicar')
else:
    FATIA = float(_m_fatia.group(1).replace(',', '.'))
    _esp5 = round(POR_PACTO * FATIA, 2)
    print(f'  fatia, do DESENHO-trilhas: {FATIA}')
    print(f'  {POR_PACTO:.2f} x {FATIA} = {_esp5:.2f}   (a peca 22 escreve {_dpr:.2f})')
    if abs(_dpr - _esp5) > 0.02:
        erro('5', f'a peca 22 escreve {_dpr:.2f} de dano por rodada e '
                  f'{POR_PACTO:.2f} fatia x {FATIA} da {_esp5:.2f}')
    else:
        print('  [x] o dano por rodada do teto reconstroi da fatia.')


# ---------------------------------------------------------------- 6 ---------
bloco('6. O GOLPE SIMPLES — o vao da peca 6 §3, e a % que a peca 22 publica')

_t6 = tabela(_p6, re.compile(r'\|\s*n[íi]vel\s*\|\s*Rotina\s*\|.*conjurador'), 4)
_l30 = next((c for c in _t6 if limpo(c[0]) == '30'), None)
_pct = next((num(c[1]) for c in _moedas if 'golpe simples' in limpo(c[0]).lower()), None)
_citado = re.search(r'o golpe simples é `(\d+)` no n[íi]vel 30', P22)

if _l30 is None:
    erro('6', 'nao achei a linha do nivel 30 na tabela da peca 6 §3 — o vao nao '
              'tem de onde sair, e esta checagem parou de conferir')
elif _pct is None or not _citado:
    erro('6', 'a peca 22 nao publica a % de um golpe simples ou nao diz de quanto '
              'e o golpe simples no nivel 30')
elif _dpr is None:
    erro('6', 'sem o dano por rodada da checagem 5 nao ha o que dividir')
else:
    _conj, _fis = num(_l30[2]), num(_l30[3])
    _vao = _fis - _conj
    _golpe = int(_citado.group(1))
    _esp6 = round(_dpr / _vao * 100)
    print(f'  peca 6 §3, nivel 30      : conjurador {_conj:.0f} · fisico {_fis:.0f}')
    print(f'  o vao (o golpe simples)  : {_vao:.0f}   (a peca 22 cita {_golpe})')
    print(f'  {_dpr:.2f} / {_vao:.0f} = {_esp6}%   (a peca 22 escreve {_pct:.0f}%)')
    if _golpe != _vao:
        erro('6', f'a peca 22 diz que o golpe simples e {_golpe} no nivel 30 e o vao '
                  f'entre as duas colunas da peca 6 §3 da {_vao:.0f}')
    elif abs(_pct - _esp6) > 1:
        erro('6', f'a peca 22 escreve {_pct:.0f}% de um golpe simples e a conta da '
                  f'{_esp6}%')
    else:
        print('  [x] a % de um golpe simples reconstroi do vao da peca 6.')


# ---------------------------------------------------------------- 7 ---------
bloco('7. O CAMBIO DE PE — o que a peca 22 cita e o que a peca 5 §4 publica')

_t7 = tabela(_p5, re.compile(r'\|\s*fam[íi]lia\s*\|\s*exemplo\s*\|\s*janela\s*\|'), 6)
_row_pe = next((c for c in _t7 if 'recuperar' in c[1] and 'PE' in c[1]
                and limpo(c[2]) == 'permanente'), None)
_row_ac = next((c for c in _t7 if 'acerto' in c[1] and 'seu' in c[1]
                and limpo(c[2]) == 'permanente'), None)

if _row_pe is None or _row_ac is None:
    erro('7', 'nao achei a linha de `+1 PE permanente` ou a de `+1 no seu acerto` '
              'na tabela da peca 5 §4 — o cambio nao tem de onde sair')
else:
    _pe_dano, _pe_fatia = num(_row_pe[3]), num(_row_pe[4])
    _ac_fatia = num(_row_ac[4])
    print(f'  peca 5: 1 PE/rodada      : {_pe_dano} de dano = {_pe_fatia} fatia')
    print(f'  peca 5: +1 no acerto     : {_ac_fatia} fatias')
    _cita_pe = re.search(r'`(\d+,\d+)` de dano, pelo câmbio da peça 5', P22)
    _cita_pe2 = re.search(r'`1` PE por rodada vale `(\d+,\d+)` fatia', P22)
    _cita_ac = re.search(r'que é `(\d+,\d+)` fatias', P22)
    _ruins = []
    if not _cita_pe or abs(num(_cita_pe.group(1)) - _pe_dano) > 0.005:
        _ruins.append(f'o dano do cambio (peca 5 diz {_pe_dano})')
    if not _cita_pe2 or abs(num(_cita_pe2.group(1)) - _pe_fatia) > 0.005:
        _ruins.append(f'a fatia do cambio (peca 5 diz {_pe_fatia})')
    if not _cita_ac or abs(num(_cita_ac.group(1)) - _ac_fatia) > 0.005:
        _ruins.append(f'o preco de +1 no acerto (peca 5 diz {_ac_fatia})')
    if _ruins:
        erro('7', 'a peca 22 diverge da peca 5 em: ' + ' · '.join(_ruins))
    else:
        print('  [x] os tres numeros que a peca 22 importa da peca 5 batem com ela.')


# ---------------------------------------------------------------- 8 ---------
bloco('8. A EXCECAO AO PISO — declarada, e ela nomeia a peca 1 §5.4')

_piso_vivo = re.search(r'nunca fica abaixo de 1', _p1)
_declara = re.search(r'exce[çc][ãa]o ao arredondamento da peça 1 §5\.4', P22, re.I)
_zero_escrito = re.search(r'zero escrito', P22)

print(f'  peca 1 ainda tem o piso  : {"sim" if _piso_vivo else "NAO"}')
print(f'  peca 22 declara a excecao: {"sim" if _declara else "NAO"}')
if not _piso_vivo:
    erro('8', 'a peca 1 §5.4 nao diz mais que o que se ganha nunca fica abaixo de 1 '
              '— a excecao da peca 22 passou a apontar para regra que nao existe')
elif not _declara:
    erro('8', 'a peca 22 nao declara a excecao ao arredondamento da peca 1 §5.4 — '
              'Essencia 1 arredonda para 0 e o piso daquela peca levaria para 1')
elif not _zero_escrito:
    erro('8', 'a peca 22 declara a excecao e nao separa a Essencia 0 da Essencia 1 '
              '— a peca 1 §5.4 ja diz que o piso nao desfaz zero escrito, entao a '
              'excecao e de UMA linha e nao de duas')
else:
    print('  [x] a excecao esta declarada, aponta para a peca 1 §5.4, e separa o '
          'zero escrito do zero arredondado.')


# ---------------------------------------------------------------- 9 ---------
bloco('9. ROLAGEM — a peca 22 nao CONCEDE numero em acerto, Defesa nem pericia')

# ATENCAO ao que esta checagem mede. A primeira versao perguntava se as palavras
# `acerto`, `Defesa` e `pericia` APARECEM numa linha de proibicao — e elas
# aparecem, porque o §3.4 e' literalmente essa linha. Escrever uma entrega que
# desse `+1` de Defesa noutra secao saia VERDE. Medir o marcador em vez do
# fenomeno, que e' a armadilha que este projeto ja pagou varias vezes.
# Hoje ela procura a PROMESSA e nao a proibicao, em dois eixos.
PROIBIDOS = ['acerto', 'defesa', 'perícia', 'pericia']
_bene = tabela(P22, re.compile(r'\|\s*o que o pacto dá\s*\|\s*quem alcança\s*\|'), 4)

print(f'  linhas de beneficio (§3.3): {len(_bene)}')
if not _bene:
    erro('9', 'nao achei a tabela de beneficio do §3.3 — o extrator quebrou e esta '
              'checagem parou de conferir')
else:
    # 9a — o FENOMENO: a lista do que o pacto da' nao pode nomear os tres.
    _sujas = [limpo(c[0]) for c in _bene
              if any(p in limpo(c[0]).lower() for p in PROIBIDOS)]
    if _sujas:
        erro('9', f'a tabela do §3.3 lista {_sujas} como coisa que o pacto entrega — '
                  'pacto nao mexe em valor numerico de rolagem')
    else:
        print(f'  [x] 9a: nenhuma das {len(_bene)} linhas de beneficio nomeia '
              'acerto, Defesa ou pericia.')

    # 9b — qualquer linha que junte numero com sinal a um dos tres tem de
    # carregar negacao. O regex e' conferido contra uma TESTEMUNHA da pasta:
    # se ele parar de acender onde o sistema realmente concede, ele quebrou.
    _RX_CONC = re.compile(r'[+−-]\s*`?\d+`?[^.\n]{0,40}?(' + '|'.join(PROIBIDOS) + r')'
                          r'|(' + '|'.join(PROIBIDOS) + r')[^.\n]{0,24}?[+−-]\s*`?\d+',
                          re.I)
    _RX_NEG = re.compile(r'\bn[ãa]o\b|\bnunca\b|\bnem\b|\bsem\b|de fora|fora d|'
                         r'proíb|proib|reprova|estour', re.I)
    _testemunha9 = '\n'.join(ler(p) for p in PECAS if p != ALVO)
    _acende_fora = len(_RX_CONC.findall(_testemunha9))
    _PISO9 = 5
    print(f'  o regex de concessao acende {_acende_fora}x na testemunha (piso {_PISO9})')
    if _acende_fora < _PISO9:
        erro('9', f'o regex de concessao so acende {_acende_fora}x nas outras pecas '
                  f'e o piso e {_PISO9} — ele quebrou, e a peca 22 esta passando por '
                  'falta de medida e nao por estar limpa')
    else:
        _nuas = [(i, l) for i, l in enumerate(P22_L, 1)
                 if _RX_CONC.search(l) and not _RX_NEG.search(l)]
        if _nuas:
            for _i, _l in _nuas:
                erro('9', f'linha {_i} junta numero a acerto/Defesa/pericia sem '
                          f'negacao: "{_l.strip()[:96]}"')
        else:
            print('  [x] 9b: toda linha que junta numero aos tres carrega negacao.')


# --------------------------------------------------------------- 10 ---------
bloco('10. DONO DE CADA BENEFICIO — ou a peca existe, ou a falta esta declarada')

if not _bene:
    erro('10', 'sem a tabela do §3.3 nao ha beneficio para conferir')
else:
    _RX_SEM = re.compile(r'n[ãa]o (?:tem|pode|existe)|não existe|inexistente|'
                         r'a peça não existe', re.I)
    _orfaos = []
    for _c in _bene:
        _nome, _resto = limpo(_c[0]), ' '.join(_c[1:])
        _pecas_citadas = [int(m.group(1)) for m in re.finditer(r'pe[çc]a (\d+)', _resto)]
        _quebradas = [n for n in _pecas_citadas if n not in POR_NUM]
        _declara_falta = bool(_RX_SEM.search(_resto))
        _ok = (_pecas_citadas and not _quebradas) or _declara_falta
        _mostra = ','.join(str(n) for n in _pecas_citadas) or '—'
        print(f'      {_nome:<22} pecas: {_mostra:<8} '
              f'declara falta: {"sim" if _declara_falta else "nao"}')
        if _quebradas:
            _orfaos.append(f'`{_nome}` aponta para peca {_quebradas} que nao existe')
        elif not _ok:
            _orfaos.append(f'`{_nome}` nao nomeia dono nem declara que nao tem preco')
    if _orfaos:
        for _o in _orfaos:
            erro('10', _o)
    else:
        print(f'  [x] os {len(_bene)} beneficios tem dono existente ou falta '
              'declarada.')


# --------------------------------------------------------------- 11 ---------
bloco('11. AS QUATRO TRAVAS — moram na peca 8, e esta peca aponta em vez de copiar')

_TRAVAS = re.findall(r'^\*\*(\d)\.\s+(.{20,90}?)\*\*', _p8, re.M)
_TRAVAS = [(int(n), t.strip()) for n, t in _TRAVAS]
print(f'  travas achadas na peca 8 : {len(_TRAVAS)}')
for _n, _t in _TRAVAS:
    print(f'      {_n}. {_t[:74]}')

_PISO11 = 4
if len(_TRAVAS) < _PISO11:
    erro('11', f'so achei {len(_TRAVAS)} trava(s) no Passo 8 da peca 8 e o piso e '
               f'{_PISO11} — elas sao a fundacao desta peca, e esta checagem parou '
               'de conferir')
else:
    _copiadas = [f'trava {n}' for n, t in _TRAVAS if t in P22]
    _aponta = len(re.findall(r'trava n[ºo°]?\s*\d', P22))
    print(f'  a peca 22 aponta por numero: {_aponta}x')
    if _copiadas:
        erro('11', f'a peca 22 copia o texto de {_copiadas} em vez de apontar — '
                   'uma frase em dois documentos e a licao no 9')
    elif _aponta < 2:
        erro('11', f'a peca 22 so aponta para trava {_aponta}x — ela apoia o §3.3 e '
                   'o §6 nelas, e sem o ponteiro ninguem acha o argumento')
    else:
        print(f'  [x] as {len(_TRAVAS)} travas ficaram na peca 8, e a peca 22 aponta '
              f'para elas {_aponta}x sem copiar.')


# --------------------------------------------------------------- 12 ---------
bloco('12. PECA 8 — ela nao diz mais que a quarta forma nao tem regra')

_RX_MORTA = re.compile(
    r'pacto entre personagens n[ãa]o tem regra|'
    r'o que n[ãa]o existe ainda é a régua|'
    r'\|\s*\*?\*?ningu[ée]m\*?\*?\s*\|\s*—\s*\|', re.I)
_mortas = [(i, l) for i, l in enumerate(_p8.split('\n'), 1)
           if _RX_MORTA.search(l) and '~~' not in l]
_aponta12 = re.search(r'pe[çc]a 22', _p8)

print(f'  linhas mortas na peca 8  : {len(_mortas)}')
if _mortas:
    for _i, _l in _mortas:
        erro('12', f'peca 8 linha {_i} ainda diz que a quarta forma nao tem regra: '
                   f'"{_l.strip()[:88]}"')
elif not _aponta12:
    erro('12', 'a peca 8 nao cita a peca 22 em lugar nenhum — o Passo 8 dela e quem '
               'prometia a regra desde a v0.21, e ele tem de nomear quem pagou')
else:
    print('  [x] a peca 8 aponta para a peca 22 e nao anuncia mais a quarta forma '
          'como sem regra.')


# --------------------------------------------------------------- 13 ---------
bloco('13. CATALOGO — todo exemplar da obra declara qual das quatro formas ele e')

_ex = tabela(P22, re.compile(r'\|\s*exemplar\s*\|\s*forma\s*\|'), 3)
_PISO13 = 5
print(f'  exemplares lidos do §7.1 : {len(_ex)}  (piso {_PISO13})')
if len(_ex) < _PISO13:
    erro('13', f'so achei {len(_ex)} exemplar(es) no §7.1 e o piso e {_PISO13} — o '
               'extrator quebrou e esta checagem parou de conferir')
elif not NOMES_FORMA:
    erro('13', 'sem a tabela do §1 nao ha forma contra o que comparar')
else:
    _fora = []
    for _c in _ex:
        _f = limpo(_c[1])
        if _f not in NOMES_FORMA:
            _fora.append(f'`{limpo(_c[0])}` diz ser `{_f}`')
    _usadas = sorted({limpo(c[1]) for c in _ex})
    print(f'  formas usadas no catalogo: {_usadas}')
    if _fora:
        for _o in _fora:
            erro('13', _o + f' — e as formas declaradas no §1 sao {NOMES_FORMA}')
    else:
        print(f'  [x] os {len(_ex)} exemplares usam so as formas que o §1 declara.')


# --------------------------------------------------------------- 14 ---------
bloco('14. PONTEIRO PENDURADO — todo termo em crase da peca 22 tem destino')

_RX_CRASE = re.compile(r'`([A-ZÁÂÃÀÉÊÍÓÔÕÚÇ][^`\n]{1,28})`')
_termos = sorted({m.group(1).strip() for m in _RX_CRASE.finditer(P22)})
_outras = '\n'.join(ler(p) for p in PECAS if p != ALVO)

_pendurados = []
for _t in _termos:
    _definido = re.search(r'\*\*`?' + re.escape(_t) + r'`?\*\*', P22) is not None
    if not _definido and _t not in _outras:
        _pendurados.append(_t)

_PISO14 = 5
print(f'  termos em crase na peca  : {len(_termos)}')
print(f'      {_termos}')
if len(_termos) < _PISO14:
    erro('14', f'so achei {len(_termos)} termo(s) em crase e o piso e {_PISO14} — o '
               'extrator quebrou e esta checagem parou de conferir')
elif _pendurados:
    erro('14', f'{len(_pendurados)} termo(s) em crase sem destino: {_pendurados} — '
               'nem definidos aqui, nem existentes em outra peca')
else:
    print(f'  [x] os {len(_termos)} termos em crase tem destino.')


print()
print('=' * 88)
if FALHAS:
    print(f'>>> {len(FALHAS)} PROBLEMA(S):')
    for _e in FALHAS:
        print('   -', _e)
    sys.exit(1)
print('>>> TUDO OK — as quatro formas estao separadas, o unico teto que existe e')
print('    derivado dos donos, e nenhum numero desta peca esta escrito no validador.')
sys.exit(0)

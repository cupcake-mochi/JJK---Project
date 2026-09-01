#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Confere a peca 26 — o Bestiario — contra os donos de cada linha da ficha.

A peca 26 nao inventa numero: ela junta num lugar so' os que montar um inimigo
pede, e declara de onde cada um sai. Entao este validador quase nao mede regra
nova — ele mede DERIVACAO, que e' o que a peca promete.

NENHUM VALOR DE REGRA ESTA ESCRITO AQUI. A tabela de inimigo vem do manual, as
formulas vem da peca 1, a curva de refino vem da peca 11, as acoes do chefe vem
da peca 19 e os fatores de categoria vem da propria peca 26. A checagem 7 e' quem
guarda essa promessa.

As checagens 3 e 5 leem o .docx do manual: sem o python-docx elas PULAM, e o
rodape DIZ que pularam. Um verde que pulou checagem nao e' um verde.
"""

import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))
ERROS = []
_PULADAS = []


def erro(msg):
    ERROS.append(msg)
    print(f'  !! {msg}')


def pulou(msg):
    _PULADAS.append(msg)
    print(f'  ~~ PULADA: {msg}')


def bloco(t):
    print()
    print('=' * 88)
    print(t)
    print('=' * 88)


def ler(caminho):
    with open(os.path.join(RAIZ, caminho), encoding='utf-8') as fh:
        return fh.read()


PECA = 'sistema/03-mecanica/26-bestiario.md'
P01 = 'sistema/03-mecanica/01-atributos-acerto-defesa.md'
P03 = 'sistema/03-mecanica/03-economia-de-acao-e-iniciativa.md'
P07 = 'sistema/03-mecanica/07-pericias-e-oficios.md'
P11 = 'sistema/03-mecanica/11-aptidoes-e-refino.md'
P12 = 'sistema/03-mecanica/12-experiencia-e-progressao.md'
P19 = 'sistema/03-mecanica/19-dano-e-condicoes.md'
DOCX = os.path.join(RAIZ, 'manual', 'Fundamento-MANUAL-v7.docx')

TXT = ler(PECA)


def celulas(linha):
    return [c.replace('*', '').replace('`', '').strip() for c in linha.split('|')[1:-1]]


def tabela(texto, cabecalho):
    """As linhas de dado da primeira tabela que comeca com `cabecalho`."""
    i = texto.find(cabecalho)
    if i < 0:
        return []
    t = texto[i:]
    t = t[:t.find('\n\n')] if '\n\n' in t else t
    return [celulas(l) for l in t.split('\n')[1:]
            if l.startswith('|') and not l.startswith('|---')]


# --------------------------------------------------------------------------
bloco('1. AS ANCORAS — cada linha da ficha aparece no dono dela')
# --------------------------------------------------------------------------
# A peca publica a ficha como uma tabela `linha | valor | dono` no §3. Este
# dicionario diz, para cada linha, o arquivo dono e um padrao que tem de casar
# la. A guarda 1.1 compara as duas listas nos DOIS sentidos: linha da peca sem
# ancora e' dono declarado que ninguem confere, e ancora sem linha e' o
# contrario. E' o mesmo defeito que a v0.198 achou no conferir-dano.py, e ele
# entra aqui ja fechado em vez de esperar alguem achar de novo.
#
# ⚠ Nenhum padrao carrega o VALOR que ele confere: ancora que carrega o valor
# some no dia em que o valor muda, que e' o dia em que ela precisa acender.
ANCORAS = {
    'nivel': (P12, r'[Nn]ível'),
    'categoria': (PECA, r'\*\*`Ronda`\*\*'),
    'vida': (PECA, r'a linha do manual vezes o fator'),
    'integridade': (PECA, r'igual à vida máxima'),
    'dano': (PECA, r'a linha do manual vezes o fator'),
    'acoes': (P19, r'O chefe age `\d+` vezes por rodada'),
    'defesa': (P01, r'10 \+ Destreza \+ prote'),
    'acerto': (P01, r'atributo.{0,20}maestria'),
    'cd': (P01, r'8 \+ atributo'),
    'reacao': (PECA, r'volta no começo do turno dele'),
    'refino': (P11, r'\*\*meio a meio\*\*'),
    'tr': (P07, r'[Tt]este de Resistência'),
    'deslocamento': (P03, r'9 m'),
}
MAPA_ANCORA = {
    'nível': ('nivel',), 'categoria': ('categoria',), 'vida': ('vida',),
    'Integridade': ('integridade',), 'dano por rodada': ('dano',),
    'ações por rodada': ('acoes',), 'Defesa': ('defesa',), 'acerto': ('acerto',),
    'CD': ('cd',), 'Reação': ('reacao',), 'refino': ('refino',),
    'Testes de Resistência': ('tr',), 'deslocamento': ('deslocamento',),
}

_achadas = 0
for _rot, (_arq, _pad) in sorted(ANCORAS.items()):
    if re.search(_pad, ler(_arq)):
        _achadas += 1
    else:
        erro(f'1: a ancora "{_rot}" nao aparece em {_arq} — ou ela mudou de forma '
             f'la, ou esta linha da ficha ficou sem chao')
print(f'  {_achadas} de {len(ANCORAS)} ancoras encontradas nos donos.')

_FICHA = [c for c in tabela(TXT, '| linha | valor | dono |') if len(c) == 3]
_rotulos = [c[0] for c in _FICHA]
if not _rotulos:
    erro('1.1: nao achei a tabela da ficha do §3 — ela mudou de forma e a guarda '
         'que compara as duas listas parou de conferir')
else:
    _sem = [r for r in _rotulos if r not in MAPA_ANCORA]
    _sobra = [r for r in MAPA_ANCORA if r not in _rotulos]
    _reiv = {k for v in MAPA_ANCORA.values() for k in v}
    _orfas = sorted(set(ANCORAS) - _reiv)
    _fant = sorted(_reiv - set(ANCORAS))
    for _msg, _lista in (('linha(s) da ficha sem ancora nenhuma', _sem),
                         ('o mapa aponta para linha(s) que sairam da ficha', _sobra),
                         ('ancora(s) que nenhuma linha da ficha reivindica', _orfas),
                         ('o mapa reivindica ancora(s) que nao existem', _fant)):
        if _lista:
            erro(f'1.1: {_msg}: ' + ', '.join(_lista))
    if not (_sem or _sobra or _orfas or _fant):
        print(f'  [x] as {len(_rotulos)} linhas da ficha e as {len(ANCORAS)} ancoras '
              'se cobrem nos dois sentidos')


# --------------------------------------------------------------------------
bloco('2. AS TRES DERIVADAS — Defesa, acerto e CD saem das formulas da peca 1')
# --------------------------------------------------------------------------
# As tres nao tinham dono em documento nenhum ate a v0.198, e as tres derivam
# sem escolha. A prova de que a derivacao esta certa nao e' ela fechar sozinha:
# e' ela devolver, do lado do inimigo, os MESMOS numeros que a peca 1 §6 publica
# do lado do jogador. Se uma das duas se mover, esta acende.
def maestria(nv):
    return 1 + max(0, nv - 2) // 8


def investido(nv):
    return min(6, 3 + max(0, nv - 2) // 8)


_MEIO = {2: 1}
_lin = [c for c in tabela(ler(P11), '| | nv 6 | nv 10 | nv 14 | nv 18 | nv 22 | nv 26 | nv 30 |')
        if c and c[0].startswith('meio a meio')]
if not _lin or len(_lin[0]) < 8:
    erro('2: nao achei a linha do `meio a meio` na tabela de refino da peca 11 §3 — '
         'ela e a curva que o inimigo herda, e sem ela a Defesa dele nao reconstroi')
else:
    for _nv, _v in zip((6, 10, 14, 18, 22, 26, 30), _lin[0][1:8]):
        _MEIO[_nv] = int(_v)


def refino(nv):
    r = 1
    for m in (6, 10, 14, 18, 22, 26, 30):
        if nv >= m and m in _MEIO:
            r = _MEIO[m]
    return r


def protecao(ref):
    return ref // 3 + 1          # peca 11 §6, arredonda pra baixo (peca 1 §5.4)


def defesa(nv):
    return 10 + investido(nv) + protecao(refino(nv))


def acerto(nv):
    return investido(nv) + maestria(nv)


def cd(nv):
    return 8 + investido(nv) + maestria(nv)


def p(alvo, bonus):
    return max(0.05, min(0.95, (21 - (alvo - bonus)) / 20))


_NIVEIS = (5, 10, 15, 20, 25, 30)
_pub_der = {c[0]: c[1:] for c in tabela(TXT, '| nível do grupo | 5 | 10 | 15 | 20 | 25 | 30 |') if c}
_mau2 = 0
if not _pub_der:
    erro('2: nao achei a tabela do §3.1 — as tres derivadas ficaram sem o outro lado')
    _mau2 = 1
for _rot, _f in (('Defesa', defesa), ('acerto', acerto), ('CD', cd), ('refino', refino)):
    if _rot not in _pub_der:
        if _pub_der:
            erro(f'2: a tabela do §3.1 nao publica a linha "{_rot}"')
            _mau2 += 1
        continue
    for _nv, _v in zip(_NIVEIS, _pub_der[_rot]):
        _esp = _f(_nv)
        if int(_v.lstrip('+')) != _esp:
            erro(f'2: no nivel {_nv} a peca publica {_rot} {_v} e a formula do dono '
                 f'da {_esp}')
            _mau2 += 1
if not _mau2:
    print('  [x] as quatro linhas do §3.1 reconstroem das formulas dos donos')

_acertos = sorted({round(p(defesa(nv), acerto(nv)) * 100) for nv in _NIVEIS})
_falhas = sorted({round((1 - p(cd(nv), acerto(nv))) * 100) for nv in _NIVEIS})
print(f'  ele acerta o alvo dificil em {_acertos[0]}% a {_acertos[-1]}%; '
      f'o TR treinado dele falha ' + ' a '.join(f'{x}%' for x in _falhas))
_t01 = ler(P01)
_m01 = re.search(r'\|\s*\*\*treinado\*\*\s*\|((?:\s*\d+%\s*\|)+)', _t01)
if not _m01:
    erro('2: a peca 1 §6 parou de publicar a linha do Teste de Resistencia treinado — '
         'a CD do inimigo se mede contra aquele numero')
else:
    _res = sorted({int(x) for x in re.findall(r'(\d+)%', _m01.group(1))})
    if _falhas != [100 - r for r in _res][::-1] and set(_falhas) != {100 - r for r in _res}:
        erro(f'2: a CD derivada faz o TR treinado falhar {_falhas}%, e a peca 1 §6 '
             f'publica que ele resiste {_res}% — os dois lados da mesma rolagem discordam')
    else:
        print(f'  [x] a CD do inimigo devolve exatamente os {_res[0]}% que a peca 1 §6 publica')

_m06 = re.findall(r'^\|\s*(?:corpo a corpo|à distância|conjuração)[^|]*\|((?:\s*\d+%\s*\|)+)',
                  _t01, re.M)
if not _m06:
    erro('2: nao achei as linhas de acerto da peca 1 §6 — a banda do inimigo se mede '
         'contra elas')
else:
    _pico = max(int(x) for l in _m06 for x in re.findall(r'(\d+)%', l))
    # ⚠ a tabela do §6 amostra os niveis de MARCO, que sao os picos da curva. O vale
    # nao aparece la — ele e' declarado ao lado, como oscilacao irredutivel. Ler so'
    # a tabela produziria uma banda de um ponto so', e o inimigo, amostrado em
    # niveis que nao sao marco, cairia fora dela sem nada estar errado.
    _mosc = re.search(r'oscilação de `(\d+)\s*pp`', _t01)
    if not _mosc:
        erro('2: a peca 1 §6 parou de declarar a oscilacao irredutivel do acerto — sem '
             'ela a tabela dela e so os picos, e a banda do inimigo fica sem chao')
    else:
        _piso = _pico - int(_mosc.group(1))
        if _acertos[0] < _piso or _acertos[-1] > _pico:
            erro(f'2: o inimigo acerta o alvo dificil em {_acertos[0]}% a {_acertos[-1]}%, '
                 f'e a peca 1 §6 publica pico de {_pico}% com oscilacao de '
                 f'{_mosc.group(1)}pp, que da a banda de {_piso}% a {_pico}%')
        else:
            print(f'  [x] o acerto dele cai na banda de {_piso}% a {_pico}% que a peca 1 '
                  '§6 publica — o pico da tabela e a oscilacao declarada')


# --------------------------------------------------------------------------
bloco('3. A CATEGORIA — vida e dano saem da linha do manual vezes o fator')
# --------------------------------------------------------------------------
# A tabela de inimigo e' do manual, e e' de la que a categoria reescala. Sem o
# python-docx esta checagem PULA, porque a alternativa seria guardar a tabela
# aqui dentro — que e' a licao no 9 no numero de que a peca inteira depende.
_CAT = []
for _c in tabela(TXT, '| categoria | personagens | fator sobre a linha do manual | ações |'):
    if len(_c) < 4:
        continue
    _m = re.match(r'([\d,]+)', _c[2].replace('×', '').strip())
    if _m:
        _CAT.append((_c[0], int(_c[1]), float(_m.group(1).replace(',', '.')), int(_c[3])))
if len(_CAT) != 4:
    erro(f'3: achei {len(_CAT)} categoria(s) na tabela do §4 e a peca promete quatro — '
         'ela mudou de forma e esta checagem parou de conferir')

_FICHAS = tabela(TXT, '| categoria | nv 10 | nv 20 | nv 30 |')
_MANUAL = {}
try:
    import docx
except ImportError:
    docx = None

if docx is not None and os.path.isfile(DOCX):
    _doc = docx.Document(DOCX)
    for _t in _doc.tables:
        _cab = [c.text.strip() for c in _t.rows[0].cells]
        if _cab and _cab[0].startswith('Nível do grupo') and 'Chefe: dano' in _cab:
            for _r in _t.rows[1:]:
                _v = [c.text.strip() for c in _r.cells]
                _vd = _v[2].split(' a ')
                _MANUAL[int(_v[0])] = (float(_v[1].replace('~', '')),
                                       (int(_vd[0]) + int(_vd[-1])) / 2,
                                       float(_v[3]), float(_v[4]), float(_v[5]))
            break

if not _MANUAL:
    pulou('3. a categoria contra a tabela do manual — sem python-docx '
          '(pip install python-docx --break-system-packages)')
elif not _CAT or not _FICHAS:
    erro('3: sem as tabelas do §4 e do §4.1 lidas nao da para conferir a categoria')
else:
    print(f'  a tabela `Inimigos` do manual tem {len(_MANUAL)} linhas, '
          f'de nv {min(_MANUAL)} a {max(_MANUAL)}.')
    _mau3 = 0
    for _c in _FICHAS:
        if len(_c) < 4:
            continue
        _achou = [x for x in _CAT if x[0] == _c[0]]
        if not _achou:
            erro(f'3: o §4.1 publica a categoria "{_c[0]}", que nao esta na tabela do §4')
            _mau3 += 1
            continue
        _pes, _fator = _achou[0][1], _achou[0][2]
        if abs(_fator - _pes / 4) > 1e-9:
            erro(f'3: a categoria {_c[0]} exige {_pes} personagem(ns) e publica fator '
                 f'{_fator}, e {_pes}/4 da {_pes / 4}')
            _mau3 += 1
        for _nv, _cel in zip((10, 20, 30), _c[1:4]):
            _nums = re.findall(r'(\d+)', _cel)
            if len(_nums) < 2:
                erro(f'3: nao consegui ler a celula "{_cel}" do §4.1')
                _mau3 += 1
                continue
            _ve, _de = round(_MANUAL[_nv][1] * _fator), round(_MANUAL[_nv][2] * _fator)
            if int(_nums[0]) != _ve or int(_nums[1]) != _de:
                erro(f'3: {_c[0]} no nv{_nv}: a peca publica {_nums[0]} vida e '
                     f'{_nums[1]} dano, e a linha do manual vezes {_fator} da '
                     f'{_ve} e {_de}')
                _mau3 += 1
    if not _mau3:
        print(f'  [x] as {len(_FICHAS)} categorias do §4.1 reconstroem da tabela do '
              'manual vezes o fator')
        print('  [x] os quatro fatores reconstroem de personagens/4')


# --------------------------------------------------------------------------
bloco('4. AS ACOES — personagens menos um, e a Alcateia bate com o piso da peca 19')
# --------------------------------------------------------------------------
# A regra sai da frase do manual — o chefe "perde a acao tres vezes por rodada"
# contra um grupo de quatro. E o valor da categoria de quatro nao e' livre: a
# peca 19 §2.2 preca quatro condicoes dividindo por ele, e com um a menos as
# quatro passam do teto do proprio tier. Se aquele piso mudar, ESTA acende.
if not _CAT:
    erro('4: sem a tabela do §4 lida nao da para conferir as acoes')
else:
    _mau4 = 0
    for _nome, _pes, _fat, _ac in _CAT:
        _esp = max(1, _pes - 1)
        if _ac != _esp:
            erro(f'4: a categoria {_nome} exige {_pes} personagem(ns) e publica {_ac} '
                 f'acao(oes), e "personagens menos um, piso 1" da {_esp}')
            _mau4 += 1
    if not _mau4:
        print('  [x] as quatro categorias seguem "personagens menos um, piso 1"')

    _m19 = re.search(r'O chefe age `(\d+)` vezes por rodada', ler(P19))
    if not _m19:
        erro('4: nao achei o piso das acoes do chefe na peca 19 §2.2 — ele e a metade '
             'de fora desta checagem, e sem ele ela so se compara com ela mesma')
    else:
        _piso = int(_m19.group(1))
        _quatro = [c for c in _CAT if c[1] == 4]
        if not _quatro:
            erro('4: nenhuma categoria desta peca exige quatro personagens, e a tabela '
                 'do manual e a peca 19 sao calibradas para quatro')
        elif _quatro[0][3] != _piso:
            erro(f'4: a categoria de quatro publica {_quatro[0][3]} acoes e a peca 19 '
                 f'§2.2 publica {_piso} — a regua de condicao daquela peca divide por '
                 'esse numero, entao os dois nao podem discordar')
        else:
            print(f'  [x] a categoria de quatro publica {_piso} acoes, igual ao piso '
                  'que a peca 19 §2.2 deriva da banda')


# --------------------------------------------------------------------------
bloco('5. O CAMBIO — medido aqui dentro, e nao guardado')
# --------------------------------------------------------------------------
# A peca publica "um chefe vale quatro capangas". O numero nao esta escrito neste
# arquivo: a simulacao de fogo concentrado roda aqui, com a vida, o dano e a
# saida do grupo lidos do manual, e o publicado tem de ser o que ela devolve.
_NUM_PT = {'um': 1, 'dois': 2, 'três': 3, 'quatro': 4, 'cinco': 5, 'seis': 6,
           'sete': 7, 'oito': 8, 'nove': 9, 'dez': 10}


def _simula(saida, corpos):
    vs = [list(c) for c in corpos]
    rod = 0
    cobrado = 0.0
    while vs and rod < 100:
        cobrado += sum(c[1] for c in vs)
        sobra = saida
        while sobra > 0 and vs:
            if vs[0][0] <= sobra:
                sobra -= vs.pop(0)[0]
            else:
                vs[0][0] -= sobra
                sobra = 0
        rod += 1
    return rod, cobrado


_m5 = re.search(r'vale (\w+) capangas', TXT)
if not _m5:
    erro('5: a peca nao publica o cambio como "vale N capangas" — a frase mudou de '
         'forma e esta checagem ficou sem o outro lado')
elif not _MANUAL:
    pulou('5. o cambio contra a simulacao — a tabela do manual nao foi lida')
else:
    _pub5 = _NUM_PT.get(_m5.group(1).lower())
    _medidos = []
    for _nv, (_saida, _cv, _cd, _kv, _kd) in sorted(_MANUAL.items()):
        _r0, _t0 = _simula(_saida, [(_cv, _cd)])
        _melhor = min(range(1, 13),
                      key=lambda n: abs(_simula(_saida, [(_kv, _kd)] * n)[1] - _t0))
        _medidos.append((_nv, _melhor))
    print('  cambio medido por nivel: ' + ' · '.join(f'nv{n}:{m}' for n, m in _medidos))
    _valores = sorted({m for _, m in _medidos})
    if _pub5 is None:
        erro(f'5: nao entendi "{_m5.group(1)}" como numero por extenso')
    elif _valores != [_pub5]:
        erro(f'5: a peca publica {_pub5} capangas por chefe, e a simulacao devolve '
             f'{_valores} nos {len(_medidos)} niveis da tabela do manual')
    else:
        print(f'  [x] a simulacao devolve {_pub5} em todos os niveis, e e o que a peca '
              'publica')


# --------------------------------------------------------------------------
bloco('6. O GRAU NAO VIRA NUMERO — nem aqui nem na peca que decide isso')
# --------------------------------------------------------------------------
# A decisao do §2 e' que o grau e' rotulo de ficcao. A checagem cobra os dois
# lados: nenhuma linha viva desta peca pode pendurar valor nele, e a peca 12, que
# e' a dona de "Grau e reconhecimento; nivel e poder", tem de continuar dizendo.
_LINHAS_GRAU = [l for l in TXT.split('\n')
                if re.search(r'\bgrau\b', l, re.I) and re.search(r'`\d', l)
                and not l.lstrip().startswith('>')]
if _LINHAS_GRAU:
    erro(f'6: {len(_LINHAS_GRAU)} linha(s) viva(s) desta peca falam de grau e carregam '
         'numero em crase — o §2 decide que ele e rotulo. Primeira: '
         + _LINHAS_GRAU[0].strip()[:90])
else:
    print('  [x] nenhuma linha viva desta peca pendura numero no grau')

if 'Grau é reconhecimento; nível é poder' not in ler(P12):
    erro('6: a peca 12 parou de publicar "Grau e reconhecimento; nivel e poder", que e '
         'a decisao em que o §2 desta peca se apoia — se ela caiu, esta peca precisa '
         'de outro argumento')
else:
    print('  [x] a peca 12 continua sendo a dona de "Grau e reconhecimento; nivel e poder"')


# --------------------------------------------------------------------------
bloco('7. NENHUM VALOR DE REGRA GUARDADO AQUI DENTRO')
# --------------------------------------------------------------------------
# A promessa do cabecalho. O que sobra de constante neste arquivo tem de ser
# FORMATO — a conversao de numero por extenso, os niveis que a tabela publica —
# e nunca valor de regra.
_FONTE = open(__file__, encoding='utf-8').read()
_achou7 = False
for _pad, _que in ((r'^\s*(VIDA|DANO|CAMBIO|FATOR|ACOES)_?\w*\s*=\s*[\d.]', 'valor de ficha'),
                   (r'^\s*CHEFE\s*=\s*[\d.]', 'o chefe'),
                   (r'^\s*CAPANGA\s*=\s*[\d.]', 'o capanga')):
    if re.search(_pad, _FONTE, re.M):
        erro(f'7: tem {_que} escrito como constante neste arquivo — ele tem de sair do '
             'documento dono')
        _achou7 = True
if not _achou7:
    print('  [x] a vida, o dano, o cambio e os fatores saem dos donos, e nenhum '
          'esta escrito aqui')
if len(_MEIO) < 8:
    erro('7: a curva de refino nao foi lida da peca 11 — ela rodou com o valor de '
         'formato deste arquivo')
else:
    print('  [x] a curva do `meio a meio` foi lida da peca 11: '
          + ' '.join(str(_MEIO[k]) for k in sorted(_MEIO)))


# --------------------------------------------------------------------------
print()
print('=' * 88)
if ERROS:
    print(f'>>> {len(ERROS)} PROBLEMA(S):')
    for e in ERROS:
        print('   -', e)
    sys.exit(1)
if _PULADAS:
    print(f'>>> OK, mas {len(_PULADAS)} checagem(ns) PULARAM:')
    for pp in _PULADAS:
        print('   -', pp)
    print('    O que pulou NAO foi conferido. Um verde que pulou checagem nao e um verde.')
else:
    print('>>> TUDO OK — as tres derivadas devolvem o que a peca 1 ja publicava do')
    print('    outro lado da mesa, a categoria reescala da tabela do manual, as acoes')
    print('    batem com o piso da peca 19, e o cambio foi medido em vez de guardado.')

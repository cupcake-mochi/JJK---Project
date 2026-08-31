#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Confere a tabela de XP (peca 12) — a trava numero 1 de mundo compartilhado.

O QUE ELA TEM DE DIFERENTE DE TODA PECA ANTERIOR:

  Ela e a primeira escrita a partir de DADO DE GENTE REAL — catorze opinioes da
  Guilda sobre quanto tempo a subida deve levar. Entao este validador tem uma
  checagem que nenhum outro do projeto tem: ele confere que a regra escrita ainda
  produz o TEMPO que as pessoas pediram. Se alguem mexer na curva ou no tamanho
  das missoes, ele diz de quanto o alvo saiu.

REESCRITO NA v0.196, quando a curva foi represada. As quatro checagens que ficaram
penduradas na curva velha — a soma ate o nivel 20, o abismo que fecha, os perfis da
Guilda e a razao da faixa lendaria — foram TODAS refeitas. Trocar a curva sem
refazer as quatro produzia verde que nao provava nada.

E a v0.196 mudou o metodo junto: ate a v0.195 este arquivo CARREGAVA a curva no
codigo. Hoje ele le a curva, a mistura de missao e o desconto da semana dos
documentos donos, reconstroi cada um da regra publicada ao lado, e compara. Numero
que mora em duas cabecas diverge (licao no 9); numero que o validador guarda sozinho
sai verde quando alguem perturba o documento.

CONTRATO DE INVARIANTES:
  1. A CURVA PUBLICADA E A REGRA PUBLICADA SAO A MESMA COISA. A tabela do SS3 tem de
     reconstruir da frase de regra do SS3 — base, degrau, teto e a excecao do nivel 2.
  2. A CURVA CRESCE, E E ISSO QUE FECHA O ABISMO. Medido em nivel FRACIONADO, para
     nao depender do arredondamento: uma divida fixa em XP tem de valer menos nivel
     conforme a campanha anda. Contra-teste: numa curva PLANA de mesmo custo total
     ela vale o mesmo do comeco ao fim.
  3. A CADENCIA REAL DA GUILDA CAI DENTRO DA FAIXA QUE AS CATORZE DESENHARAM. Nao e
     mais "tres perfis batem tres alvos" — os alvos velhos eram da curva velha. O que
     tem dono e a faixa do levantamento (minimo, mediana, maximo) e a cadencia que as
     respostas supunham.
  4. O RETORNO DECRESCENTE NAO ZERA NINGUEM, e ele e lido da tabela do SS5.
  5. A FAIXA LENDARIA E MAIS CURTA EM TEMPO, apesar de custar mais missoes. Foi o
     unico ponto em que as catorze concordaram. Contra-teste: se o topo rodasse
     missao mundana ele ficaria MAIS LENTO que a base, e nao a metade.
  6. A CONVERSAO DE MESTRAGEM RECONSTROI DOS DOIS DONOS.
  7. A LISTA DE FEITOS DO LIMIAR E FECHADA E ANCORADA.
  8. A TABELA DAS CINCO CADENCIAS RECONSTROI, celula a celula, das constantes.
  9. A TABELA DO GATILHO RECONSTROI, e ela e o exemplo trabalhado que o livro cita.

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
    return float(str(s).replace('.', '').replace(',', '.'))


PALAVRA = {'nenhuma': 0, 'uma': 1, 'um': 1, 'duas': 2, 'dois': 2, 'tres': 3,
           'três': 3, 'quatro': 4, 'cinco': 5, 'seis': 6, 'sete': 7, 'oito': 8,
           'nove': 9, 'dez': 10, 'onze': 11, 'doze': 12, 'treze': 13,
           'catorze': 14, 'quatorze': 14, 'quinze': 15, 'dezesseis': 16,
           'dezessete': 17, 'dezoito': 18, 'dezenove': 19, 'vinte': 20,
           'vinte e cinco': 25, 'trinta': 30, 'quarenta': 40, 'cinquenta': 50}

P12 = _ler('12-experiencia-e-progressao.md')
P02 = _ler('02-economia-de-atributos.md')
LEV = _ler('levantamento-ritmo-de-progressao.md', '../01-pesquisa')
FORA = _ler('levantamento-ritmo-fora-do-projeto.md', '../01-pesquisa')

if not P12:
    print('!! nao achei a peca 12 — sem ela este validador nao confere nada')
    sys.exit(1)

# Constante de calendario, e nao numero de design: 52 semanas em 12 meses.
SEMANAS_POR_MES = 4.33
NIVEL_INICIAL, NIVEL_LIMIAR, NIVEL_TETO = 2, 20, 30
MISSAO_PADRAO = 100


# ==========================================================================
bloco('0. LENDO OS DONOS — a curva, os tamanhos e o desconto da semana')
# ==========================================================================
# Nada daqui e' escrito no codigo. Se um destes extratores parar de achar, a
# checagem que depende dele acusa em vez de sair verde calada.

_s3 = _sec(P12, '## 3. A curva', '## 3.1')
CURVA = {}
for m in re.finditer(r'^\| \*\*(\d+)(?: a (\d+))?\*\* \| (\d+) miss\w+ \| ([\d.]+) \|',
                     _s3, re.M):
    ini, fim = int(m.group(1)), int(m.group(2) or m.group(1))
    n_miss, n_xp = int(m.group(3)), int(m.group(4).replace('.', ''))
    if n_xp != n_miss * MISSAO_PADRAO:
        erro(f'0: a linha "{ini} a {fim}" do SS3 diz {n_miss} missoes e {n_xp} XP, e '
             f'{n_miss} x {MISSAO_PADRAO} da {n_miss * MISSAO_PADRAO} — as duas colunas '
             f'da mesma linha discordam')
    for n in range(ini, fim + 1):
        CURVA[n] = n_xp

if sorted(CURVA) != list(range(NIVEL_INICIAL, NIVEL_TETO)):
    erro(f'0: a tabela do SS3 cobre {len(CURVA)} nivel(is) e tem de cobrir do '
         f'{NIVEL_INICIAL} ao {NIVEL_TETO - 1} sem buraco — li '
         f'{sorted(CURVA)[:4]}...{sorted(CURVA)[-3:] if CURVA else ""}')
    print('\n'.join(f'   - {e}' for e in ERROS))
    sys.exit(1)
print(f'  curva: {len(CURVA)} niveis lidos do SS3, de {CURVA[2]} a {CURVA[29]} XP.')


def custo(n):
    return CURVA[n]


def mesas(n):
    return CURVA[n] // MISSAO_PADRAO


def acumulado(ate):
    return sum(custo(n) for n in range(NIVEL_INICIAL, ate))


# --- os quatro tamanhos de missao, do SS4 ---------------------------------
_s4 = _sec(P12, '## 4. O tamanho da missao', '### 4.1')
if not _s4:
    _s4 = _sec(P12, '## 4. O tamanho da missão', '### 4.1')
TAMANHO = {}
for m in re.finditer(r'^\| \*\*([\w ]+?)\*\* \| (\d+) \|', _s4, re.M):
    TAMANHO[m.group(1)] = int(m.group(2))
if len(TAMANHO) != 4:
    erro(f'0: esperava os quatro tamanhos de missao no SS4 e li {len(TAMANHO)} '
         f'({sorted(TAMANHO)}) — sem eles a mistura do SS4.1 nao tem de que ser feita')
else:
    print('  tamanhos: ' + ' · '.join(f'{k}={v}' for k, v in TAMANHO.items()))

# --- a mistura de cada faixa, do SS4.1 ------------------------------------
# A prosa diz a RECEITA e a aritmetica ao lado diz a CONTA. As duas sao donos
# diferentes da mesma coisa, e este bloco existe para elas nao divergirem.
_s41 = _sec(P12, '### 4.1', '### E é isso')
MEDIA_MUNDANA = MEDIA_LENDARIA = None

_mm = re.search(r'a cada (\w+), uma curta e uma longa, e as outras (\w+) padr\w+\.\*\*'
                r'\s*`\((\d+) \+ (\d+) \+ (\d+)\) ÷ (\d+)`\s*=\s*\*\*`([\d,]+)`', _s41)
if not _mm:
    erro('0: nao achei a receita da missao mundana no SS4.1 — ela e a unidade de '
         'RELOGIO da peca, e sem ela toda conta de meses vira chute')
else:
    _ciclo = PALAVRA.get(_mm.group(1))
    _npad = PALAVRA.get(_mm.group(2))
    _lidos = [int(_mm.group(i)) for i in (3, 4, 5)]
    _div = int(_mm.group(6))
    _pub = _num(_mm.group(7))
    if None in (_ciclo, _npad):
        erro(f'0: o numeral da receita mundana nao esta no dicionario: '
             f'"{_mm.group(1)}" / "{_mm.group(2)}"')
    elif TAMANHO:
        _esp = [TAMANHO.get('curta'), _npad * TAMANHO.get('padrão', TAMANHO.get('padrao', 0)),
                TAMANHO.get('longa')]
        if _lidos != _esp:
            erro(f'0: a aritmetica da receita mundana publica {_lidos} e a receita em '
                 f'prosa ("uma curta e uma longa, e as outras {_npad} padrao") com os '
                 f'tamanhos do SS4 da {_esp} — a frase e a conta divergiram')
        elif _div != _ciclo or 1 + _npad + 1 != _ciclo:
            erro(f'0: a receita mundana fala em ciclo de {_ciclo} missoes, divide por '
                 f'{_div}, e 1 curta + {_npad} padrao + 1 longa da {1 + _npad + 1}')
        else:
            _der = sum(_esp) / _div
            if abs(_der - _pub) > 0.005:
                erro(f'0: a mistura mundana derivada da {_der} e o SS4.1 publica {_pub}')
            else:
                MEDIA_MUNDANA = _pub
                print(f'  [x] missao mundana: {"+".join(map(str, _esp))} / {_div} = '
                      f'{MEDIA_MUNDANA}')

_ml = re.search(r'a cada (\w+), (\w+) longas e (\w+) finais de arco\.\*\*'
                r'\s*`\((\d+) \+ (\d+)\) ÷ (\d+)`\s*=\s*\*\*`([\d,]+)`', _s41)
if not _ml:
    erro('0: nao achei a receita da missao lendaria no SS4.1 — e ela e o que faz a '
         'faixa lendaria ser mais rapida em tempo')
else:
    _c, _nl, _nf = (PALAVRA.get(_ml.group(i)) for i in (1, 2, 3))
    _lidos = [int(_ml.group(4)), int(_ml.group(5))]
    _div, _pub = int(_ml.group(6)), _num(_ml.group(7))
    if None in (_c, _nl, _nf):
        erro('0: um numeral da receita lendaria nao esta no dicionario')
    elif TAMANHO:
        _esp = [_nl * TAMANHO.get('longa', 0), _nf * TAMANHO.get('final de arco', 0)]
        if _lidos != _esp or _div != _c or _nl + _nf != _c:
            erro(f'0: a receita lendaria publica {_lidos} / {_div} e a prosa '
                 f'("{_nl} longas e {_nf} finais a cada {_c}") da {_esp} / {_nl + _nf}')
        else:
            _der = sum(_esp) / _div
            if abs(_der - _pub) > 0.005:
                erro(f'0: a mistura lendaria derivada da {_der} e o SS4.1 publica {_pub}')
            else:
                MEDIA_LENDARIA = _pub
                print(f'  [x] missao lendaria: {"+".join(map(str, _esp))} / {_div} = '
                      f'{MEDIA_LENDARIA}')

# --- o desconto da semana, da tabela do SS5 -------------------------------
_s5 = _sec(P12, '## 5. As duas primeiras da semana', '### 5.1')
SEMANA = []
for m in re.finditer(r'^\| ([\dªa e]+) \| (\d+)% \|', _s5, re.M):
    SEMANA.append((m.group(1), int(m.group(2)) / 100))
if len(SEMANA) < 4:
    erro(f'0: a tabela do desconto da semana rendeu {len(SEMANA)} linha(s) e precisa de '
         f'pelo menos quatro — sem ela o equivalente semanal nao tem dono')
    PESOS = []
else:
    PESOS = []
    for rot, peso in SEMANA:
        for _ in re.findall(r'\d+', rot):
            PESOS.append(peso)
    print('  desconto da semana: ' + ' · '.join(f'{i+1}a={p:.0%}' for i, p in
                                                enumerate(PESOS)))


def equiv_semana(mesas_por_semana):
    """Quantas missoes-cheias valem `mesas_por_semana` missoes numa semana.
    Os pesos saem da tabela do SS5; passando do fim dela, segue o ultimo degrau."""
    total, i, resto = 0.0, 0, float(mesas_por_semana)
    while resto > 1e-9:
        parte = min(1.0, resto)
        if i < len(PESOS):
            peso = PESOS[i]
        else:
            peso = PESOS[-1] * (0.5 ** (i - len(PESOS) + 1)) if PESOS else 0.0
        total += parte * peso
        resto -= parte
        i += 1
    return total


def media(n):
    return MEDIA_MUNDANA if n < NIVEL_LIMIAR else MEDIA_LENDARIA


def meses_ate(nivel, cadencia):
    """Mes em que se CHEGA a `nivel`, contando do nivel inicial."""
    e = equiv_semana(cadencia) * SEMANAS_POR_MES
    return sum(custo(n) / (e * media(n)) for n in range(NIVEL_INICIAL, nivel))


PRONTO = None not in (MEDIA_MUNDANA, MEDIA_LENDARIA) and bool(PESOS)


# ==========================================================================
bloco('1. A TABELA DA CURVA RECONSTROI DA FRASE DE REGRA?')
# ==========================================================================
# Dois donos do mesmo numero, dentro da mesma secao: a frase de regra e a tabela.
# Perturbar um dos dois acende. E' a licao no 9 aplicada de perto.

_regra = re.search(r'A base é (\w+), o número sobe (\w+) a cada (\w+) níveis, e ele '
                   r'para em (\w+)\.', _s3)
_exc = re.search(r'o nível 2 custa `(\d+)` em vez de `(\d+)`', P12)
if not _regra:
    erro('1: nao achei a frase de regra do SS3 ("A base e X, o numero sobe uma a cada '
         'Y niveis, e ele para em Z") — sem ela a tabela nao tem segundo dono')
elif not _exc:
    erro('1: o SS3.0 parou de declarar a concessao do nivel 2 ("o nivel 2 custa `N` em '
         'vez de `M`") — e ela e a unica linha da tabela que foge da formula')
else:
    BASE = PALAVRA.get(_regra.group(1))
    INCREMENTO = PALAVRA.get(_regra.group(2))
    DEGRAU = PALAVRA.get(_regra.group(3))
    TETO_MESAS = PALAVRA.get(_regra.group(4))
    NV2, NV2_SEM = int(_exc.group(1)), int(_exc.group(2))
    if None in (BASE, INCREMENTO, DEGRAU, TETO_MESAS):
        erro(f'1: um numeral da frase de regra nao esta no dicionario: {_regra.groups()}')
    else:
        print(f'  a frase diz: base {BASE}, sobe {INCREMENTO} a cada {DEGRAU} niveis, '
              f'teto {TETO_MESAS}, e o nivel 2 em {NV2} no lugar de {NV2_SEM}.')

        def da_regra(n):
            if n == NIVEL_INICIAL:
                return NV2
            return min(TETO_MESAS,
                       BASE + INCREMENTO * ((n - NIVEL_INICIAL) // DEGRAU))

        _fora = [n for n in range(NIVEL_INICIAL, NIVEL_TETO) if da_regra(n) != mesas(n)]
        if _fora:
            erro(f'1: {len(_fora)} nivel(is) da tabela do SS3 nao saem da frase de '
                 f'regra — o primeiro e o {_fora[0]}, que a tabela poe em '
                 f'{mesas(_fora[0])} missoes e a regra poe em {da_regra(_fora[0])}')
        else:
            print(f'  [x] os {NIVEL_TETO - NIVEL_INICIAL} niveis da tabela saem da frase.')
        if da_regra(3) != BASE:
            erro(f'1: a frase chama {BASE} de "base" e o nivel 3 custa {da_regra(3)} — '
                 f'a base tem de ser o primeiro degrau que a formula produz')
        _no_teto = [n for n in range(NIVEL_INICIAL, NIVEL_TETO) if mesas(n) == TETO_MESAS]
        if not _no_teto:
            erro(f'1: a frase diz que o custo "para em {TETO_MESAS}" e nivel nenhum '
                 f'chega la — o teto virou enfeite')
        elif max(mesas(n) for n in CURVA) > TETO_MESAS:
            erro(f'1: a tabela passa do teto de {TETO_MESAS} missoes declarado na frase')
        else:
            print(f'  [x] o teto de {TETO_MESAS} morde, do nivel {min(_no_teto)} ao '
                  f'{max(_no_teto)}.')

# --- a curva cresce, que e' o que faz XP fixo funcionar -------------------
print()
print(f"  {'nivel':<8}{'XP para o proximo':<22}{'em missoes padrao':<22}{'acumulado'}")
for n in (2, 3, 5, 9, 13, 19, 20, 23, 29):
    print(f'  {n:<8}{custo(n):<22}{mesas(n):<22}{acumulado(n + 1)}')

_ant = 0
for n in range(NIVEL_INICIAL, NIVEL_TETO):
    if custo(n) < _ant:
        erro(f'no nivel {n} o custo ({custo(n)}) e MENOR que o do anterior ({_ant}) — '
             f'a curva desceu, e sem crescer o atrasado nunca alcanca')
    _ant = custo(n)
if custo(NIVEL_TETO - 1) <= custo(NIVEL_INICIAL):
    erro('a curva termina custando o mesmo que comeca — ela e plana, e curva plana nao '
         'fecha abismo nenhum: todo mundo sobe no mesmo ritmo para sempre')

_quebrados = [n for n in range(NIVEL_INICIAL, NIVEL_TETO) if custo(n) % MISSAO_PADRAO]
if _quebrados:
    erro(f'{len(_quebrados)} nivel(is) custam um numero quebrado de missoes padrao (o '
         f'primeiro e o {_quebrados[0]}) — a Adventurers League e a Pathfinder Society '
         'convergem em custo inteiro justamente porque ele se le sem tabela')
else:
    print('  [x] todo nivel custa um numero INTEIRO de missoes padrao.')

# --- os totais que a peca publica em prosa -------------------------------
_tot = re.search(r'custa `(\d+)` missões padrão, e ir dali ao 30 custa `(\d+)`\*\*'
                 r' — `([\d.]+)` e `([\d.]+)` de XP, `(\d+)` missões', P12)
if not _tot:
    erro('1: o SS3 parou de publicar os totais em prosa ("custa `N` missoes padrao, e '
         'ir dali ao 30 custa `M`") — eles sao a segunda copia da soma da tabela')
else:
    _m20p, _m30p = int(_tot.group(1)), int(_tot.group(2))
    _x20p, _x30p = _num(_tot.group(3)), _num(_tot.group(4))
    _totp = int(_tot.group(5))
    _m20 = sum(mesas(n) for n in range(NIVEL_INICIAL, NIVEL_LIMIAR))
    _m30 = sum(mesas(n) for n in range(NIVEL_LIMIAR, NIVEL_TETO))
    _ruim = []
    if _m20p != _m20 or _m30p != _m30:
        _ruim.append(f'missoes: a prosa diz {_m20p}/{_m30p} e a tabela soma {_m20}/{_m30}')
    if _x20p != _m20 * MISSAO_PADRAO or _x30p != _m30 * MISSAO_PADRAO:
        _ruim.append(f'XP: a prosa diz {_x20p:.0f}/{_x30p:.0f} e a tabela soma '
                     f'{_m20 * MISSAO_PADRAO}/{_m30 * MISSAO_PADRAO}')
    if _totp != _m20 + _m30:
        _ruim.append(f'total: a prosa diz {_totp} e a soma da {_m20 + _m30}')
    for r in _ruim:
        erro(f'1: os totais em prosa do SS3 nao batem com a tabela — {r}')
    if not _ruim:
        print(f'  [x] os totais em prosa batem: {_m20} + {_m30} = {_m20 + _m30} missoes.')


# ==========================================================================
bloco('2. O ATRASADO ALCANCA? — medido em nivel fracionado')
# ==========================================================================
# A v0.195 media isso em nivel INTEIRO, e a medida tinha ruido de +-1 vindo da
# fronteira de nivel: a amostra (20, 40, 60, 90, 120) saia monotonica por sorte, e
# a mesma simulacao amostrada noutros pontos subia e descia. Nivel fracionado tira
# o ruido inteiro e deixa o invariante limpo.
#
# E o CONTRA-TESTE e' o que faz esta checagem valer: numa curva PLANA de mesmo
# custo total a divida vale o mesmo do comeco ao fim. Sem ele, "a distancia
# encolhe" seria verdade trivial.

DEFICIT = 10 * MISSAO_PADRAO   # dez missoes perdidas, e ninguem perde mais nada


def nivel_frac(xp, custo_f):
    n, resto = NIVEL_INICIAL, float(xp)
    while n < NIVEL_TETO and resto >= custo_f(n):
        resto -= custo_f(n)
        n += 1
    return n + (resto / custo_f(n) if n < NIVEL_TETO else 0.0)


_total = acumulado(NIVEL_TETO)
_plano = _total / (NIVEL_TETO - NIVEL_INICIAL)


def custo_plano(n):
    return _plano


print(f'  O atrasado perde {DEFICIT} XP e nunca mais perde nada. A pergunta e o que')
print(f'  esses {DEFICIT} XP VALEM em niveis, conforme a campanha anda.\n')
print(f"  {'XP de quem ficou':<20}{'curva que cresce':<22}{'curva PLANA (contra-teste)'}")
_cresce, _plana = [], []
for _xp in (2000, 5000, 9000, 13000, 18000, 23000):
    if _xp > _total:
        continue
    a = nivel_frac(_xp, custo) - nivel_frac(_xp - DEFICIT, custo)
    b = nivel_frac(_xp, custo_plano) - nivel_frac(_xp - DEFICIT, custo_plano)
    _cresce.append(a)
    _plana.append(b)
    print(f'  {_xp:<20}{a:<22.2f}{b:.2f}')

if len(_cresce) < 4:
    erro('2: menos de quatro pontos de medida couberam na campanha — a curva encolheu '
         'tanto que este teste parou de ter o que medir')
else:
    if any(_cresce[i] < _cresce[i + 1] - 1e-9 for i in range(len(_cresce) - 1)):
        erro('2: a divida do atrasado CRESCEU em algum ponto — a propriedade que '
             'justifica o XP fixo parou de valer')
    elif _cresce[0] / _cresce[-1] < 2.0:
        erro(f'2: a divida so encolheu {_cresce[0] / _cresce[-1]:.1f}x ao longo da '
             f'campanha inteira, e o piso e 2x — abaixo disso o atrasado nao volta a '
             f'caber na mesa dentro de uma temporada')
    else:
        print(f'\n  [x] a divida encolhe {_cresce[0] / _cresce[-1]:.1f}x, de '
              f'{_cresce[0]:.2f} para {_cresce[-1]:.2f} nivel.')
    # o contra-teste: a plana nao pode fechar nada
    if max(_plana) - min(_plana) > 0.02:
        erro(f'2: o contra-teste quebrou — na curva PLANA a divida deveria valer o '
             f'mesmo sempre e ela variou de {min(_plana):.2f} a {max(_plana):.2f}. '
             f'Sem contra-teste valido, "a distancia encolhe" nao prova que quem fecha '
             f'o abismo e a curva subir')
    elif _cresce[-1] >= _plana[-1]:
        erro(f'2: no fim da campanha a curva que cresce deixa a divida em '
             f'{_cresce[-1]:.2f} nivel e a PLANA em {_plana[-1]:.2f} — a que cresce '
             f'deixou de ser melhor que a plana, e ela existe exatamente para isso')
    else:
        print(f'  [x] contra-teste: na curva plana a divida fica em {_plana[0]:.2f} '
              f'nivel do comeco ao fim.')

# --- e a alternativa rejeitada: XP escalado pelo nivel --------------------
# Nao e' auto-referencia: aqui o deficit em XP e' a saida da simulacao, e o que
# se compara e' o comportamento das DUAS regras, nao um numero contra si mesmo.
def deficit_escalado(n_missoes, atraso=10):
    def sobe(nv, xp):
        s = 0
        while nv < NIVEL_TETO and xp >= custo(nv) and s < 1:
            xp -= custo(nv)
            nv += 1
            s += 1
        return nv, xp
    A, B = [NIVEL_INICIAL, 0.0], [NIVEL_INICIAL, 0.0]
    gA = gB = 0.0
    for i in range(n_missoes):
        for q, ativo in ((A, True), (B, i >= atraso)):
            if not ativo:
                continue
            g = MISSAO_PADRAO * (q[0] / 8)
            if q is A:
                gA += g
            else:
                gB += g
            q[1] += g
            q[0], q[1] = sobe(*q)
    return gA - gB


_esc = [(n, deficit_escalado(n)) for n in (20, 60, 100, 140)]
print('\n  Com XP escalado pelo nivel o buraco CRESCE, porque quem esta atras ganha')
print('  menos por missao justamente por estar atras:')
print('  ' + ' · '.join(f'missao {n}: {d:.0f} XP' for n, d in _esc))
if _esc[-1][1] <= DEFICIT:
    erro(f'2: com XP escalado o deficit terminou em {_esc[-1][1]:.0f} XP, que nao passa '
         f'dos {DEFICIT} do XP fixo — o argumento do SS2 afirma que ele cresce, e ele '
         f'deixou de crescer')
else:
    print(f'  [x] ele vai de {DEFICIT} para {_esc[-1][1]:.0f} XP, contra {DEFICIT} fixos.')


# ==========================================================================
bloco('3. A CADENCIA REAL DA GUILDA CAI DENTRO DA FAIXA PEDIDA?')
# ==========================================================================
# Ate a v0.195 este bloco batia tres perfis contra tres alvos escritos no codigo.
# Os alvos eram da curva velha, e sobreviveriam a qualquer troca de curva sem
# acusar nada — eles diziam mais sobre a curva de 2026-08-11 do que sobre o que a
# Guilda pediu. O que TEM dono e' a faixa do levantamento e a cadencia que as
# respostas supunham; e' contra isso que a curva se mede agora.

MISSOES_20 = MISSOES_30 = None
if not PRONTO:
    erro('3: a mistura de missao ou o desconto da semana nao foram lidos — sem eles '
         'nao da para converter preco em relogio, e este bloco nao roda')
else:
    MISSOES_20 = acumulado(NIVEL_LIMIAR) / MEDIA_MUNDANA
    MISSOES_30 = (acumulado(NIVEL_TETO) - acumulado(NIVEL_LIMIAR)) / MEDIA_LENDARIA

    # --- a faixa: dona e' a tabela do levantamento -----------------------
    _fx = {}
    for _rot in ('mediana', 'mínimo', 'máximo'):
        m = re.search(r'\|\s*\**' + _rot + r'\**\s*\|\s*\**([\d,]+)', LEV)
        if m:
            _fx[_rot] = _num(m.group(1))
    if len(_fx) != 3:
        erro(f'3: nao achei mediana, minimo e maximo na tabela do levantamento (li '
             f'{sorted(_fx)}) — eles sao os donos da faixa, e sem eles esta checagem '
             f'nao tem contra o que medir')
    else:
        # --- a cadencia: dona e' a frase do levantamento externo ---------
        _cad = re.search(r'"(\d+) a (\d+) vezes por semana"', FORA) or \
               re.search(r'(\d+) a (\d+) vezes por semana', LEV)
        if not _cad:
            erro('3: nao achei a cadencia que as respostas supunham ("N a M vezes por '
                 'semana") em levantamento nenhum — ela e o outro dono desta checagem')
        else:
            CAD_MIN, CAD_MAX = int(_cad.group(1)), int(_cad.group(2))
            print(f'  o levantamento pede entre {_fx["mínimo"]:.0f} e '
                  f'{_fx["máximo"]:.0f} meses (mediana {_fx["mediana"]}), numa cadencia '
                  f'de {CAD_MIN} a {CAD_MAX} mesas por semana.\n')
            print(f"  {'mesas/sem':<12}{'equivalente':<14}{'2->20':<12}{'20->30':<12}"
                  f"{'2->30'}")
            for c in (0.5, 1.0, 2.0, 3.0, 4.0):
                e = equiv_semana(c) * SEMANAS_POR_MES
                print(f'  {c:<12g}{equiv_semana(c):<14.2f}{MISSOES_20 / e:<12.1f}'
                      f'{MISSOES_30 / e:<12.1f}{(MISSOES_20 + MISSOES_30) / e:.1f}')

            # v0.196: a curva CRUA sai da faixa de proposito — decisao do Mizuki,
            # "chutar alto para os servidores compensarem". Entao medir a curva crua
            # contra a faixa passou a ser a pergunta errada: ela reprovaria por
            # desenho. O que esta checagem mede agora e' a curva COM a compensacao
            # minima que o SS5.3 recomenda, e ela so passa se a recomendacao for
            # SUFICIENTE. Se alguem esticar a curva de novo sem esticar a
            # recomendacao junto, isto acende.
            _rec = re.search(r'A recomendação do projeto é \*\*(\w+)\*\*', P12)
            DOBROS_REC = PALAVRA.get(_rec.group(1)) if _rec else None
            if DOBROS_REC is None:
                erro('3: o SS5.3 nao declara quantas mesas de dobro por mes o projeto '
                     'recomenda ("A recomendacao do projeto e **N**") — sem isso a '
                     'curva crua seria medida contra uma faixa que ela sai de proposito')
                DOBROS_REC = 0

            def _meses20(cad, dobros=0):
                e = equiv_semana(cad) * SEMANAS_POR_MES + min(dobros, cad * SEMANAS_POR_MES)
                return acumulado(NIVEL_LIMIAR) / (e * MEDIA_MUNDANA)

            _cru = _meses20(CAD_MAX)
            _topo = _meses20(CAD_MAX, DOBROS_REC)
            print(f'\n  na ponta de cima da cadencia ({CAD_MAX}/sem): {_cru:.1f} meses '
                  f'crus, {_topo:.1f} com as {DOBROS_REC} mesa(s) de dobro recomendadas.')
            if _cru <= _fx['máximo']:
                aviso(f'3: a curva CRUA ja cabe na faixa ({_cru:.1f} contra o teto de '
                      f'{_fx["máximo"]:.0f}) — o SS5.1 afirma que ela fica fora de '
                      f'proposito, e a afirmacao ficou falsa')
            elif not re.search(r'A curva crua fica FORA dessa faixa', P12):
                erro(f'3: a curva crua entrega {_cru:.1f} meses contra o teto de '
                     f'{_fx["máximo"]:.0f} e o SS5.1 nao declara que ela sai da faixa — '
                     f'curva fora do pedido sem registro vira acidente tres versoes '
                     f'depois')
            if _topo > _fx['máximo']:
                erro(f'3: com as {DOBROS_REC} mesa(s) de dobro que o SS5.3 recomenda, a '
                     f'ponta de cima da cadencia ainda leva {_topo:.1f} meses contra o '
                     f'teto de {_fx["máximo"]:.0f} — a recomendacao NAO e suficiente '
                     f'para trazer a curva de volta, e e' + chr(39) + ' para isso que '
                     f'ela existe')
            elif _topo < _fx['mínimo']:
                erro(f'3: {_topo:.1f} meses e mais rapido que a resposta mais rapida '
                     f'das catorze ({_fx["mínimo"]:.0f}) — a curva ficou abaixo da '
                     f'faixa inteira')
            else:
                print(f'  [x] com a compensacao recomendada cabe na faixa, com '
                      f'{_fx["máximo"] - _topo:.1f} mes de folga ate o teto de '
                      f'{_fx["máximo"]:.0f}.')

            # --- a distancia para a mediana e' REGISTRADA, e nao aprovada -
            # O SS5.1 publica esse desvio de proposito. Se a peca parar de
            # declarar, a checagem acende: numero fora do pedido sem registro e'
            # o modo como uma decisao vira acidente tres versoes depois.
            _decl = re.search(r'a curva crua erra em `\+([\d,]+)` meses, e com um '
                              r'dobro por mês em `\+([\d,]+)`', P12)
            _d_cru = _cru - _fx['mediana']
            _d_com = _topo - _fx['mediana']
            print(f'  distancia ate a mediana: {_d_cru:+.1f} mes cru, {_d_com:+.1f} '
                  f'com a compensacao.')
            if not _decl:
                erro('3: o SS5.1 parou de declarar a distancia ate a mediana nas duas '
                     'leituras ("a curva crua erra em `+N` meses, e com um dobro por '
                     'mes em `+M`") — desvio sem registro vira acidente')
            elif (abs(_num(_decl.group(1)) - _d_cru) > 0.15
                  or abs(_num(_decl.group(2)) - _d_com) > 0.15):
                erro(f'3: o SS5.1 declara errar a mediana em '
                     f'{_num(_decl.group(1))} / {_num(_decl.group(2))} e a conta da '
                     f'{_d_cru:.1f} / {_d_com:.1f} — a declaracao envelheceu')
            else:
                print('  [x] o SS5.1 declara as duas distancias, e as duas batem.')

            # --- a ponta de BAIXO fica fora, e isso e' o vao do SS5.2 -----
            _baixo = _meses20(CAD_MIN, DOBROS_REC)
            if _baixo <= _fx['máximo']:
                aviso(f'3: quem joga {CAD_MIN} mesa por semana chega em {_baixo:.1f} '
                      f'meses mesmo com a compensacao, dentro da faixa — o SS5.2 supoe '
                      f'que essa ponta fica FORA, e e dai que ele tira o vao. Se ela '
                      f'entrou, o vao encolheu e a secao inteira precisa ser remedida')
            else:
                print(f'  [x] a ponta de baixo ({CAD_MIN}/sem) fica em {_baixo:.1f} '
                      f'meses mesmo compensada — e e dai que sai o vao do SS5.2.')


# --- 3.1: a tabela de compensacao do SS5.3 e RECONTADA --------------------
# Ela e' a metade da decisao que o SS5.1 registra: a curva crua e' lenta de
# proposito, e esta tabela e' o que o servidor tem para acelerar. Numero de
# recomendacao que ninguem recalcula e' o primeiro a envelhecer, e este em
# especial, porque ele so existe em relacao a uma curva que ja mudou duas vezes.
_s53 = _sec(P12, '### 5.3', '## 6. Mestrar')
if PRONTO and _s53:
    _lin53 = []
    for _l in _s53.splitlines():
        m = re.match(r'\|\s*\**(\w+)\**\s*\|\s*\**([\d,]+)\**\s*(?:meses)?\s*\|'
                     r'\s*\**([\d,]+)\**\s*\|\s*(?:`\+(\d+)%`[^|]*|—)\s*\|', _l)
        if m:
            _lin53.append((PALAVRA.get(m.group(1)), _num(m.group(2)),
                           _num(m.group(3)), int(m.group(4)) if m.group(4) else 0))
    print()
    print(f'  3.1 — a tabela de compensacao do SS5.3: {len(_lin53)} linha(s) lidas')
    if len(_lin53) < 3:
        erro(f'3.1: a tabela do SS5.3 rendeu {len(_lin53)} linha(s) e precisa de pelo '
             f'menos tres — extrator que para de achar recontaria nada e sairia verde')
    elif any(d is None for d, _, _, _ in _lin53):
        erro('3.1: um numeral da coluna "mesas de dobro por mes" do SS5.3 nao esta no '
             'dicionario')
    else:
        def _m(nivel, cad, dobros):
            e = equiv_semana(cad) * SEMANAS_POR_MES + min(dobros, cad * SEMANAS_POR_MES)
            return sum(custo(n) / (e * media(n)) for n in range(NIVEL_INICIAL, nivel))
        _base_xp = None
        _ruins = []
        for _d, _m20, _m30, _pct in _lin53:
            _e20, _e30 = _m(NIVEL_LIMIAR, 2.0, _d), _m(NIVEL_TETO, 2.0, _d)
            if abs(_m20 - round(_e20, 1)) > 0.051:
                _ruins.append(f'{_d} dobro(s): publica {_m20} e a conta da {_e20:.1f}')
            if abs(_m30 - round(_e30, 1)) > 0.051:
                _ruins.append(f'{_d} dobro(s) no nv30: publica {_m30} e a conta da '
                              f'{_e30:.1f}')
            if _d == 0:
                _base_xp = equiv_semana(2.0) * SEMANAS_POR_MES
            elif _base_xp:
                _e_pct = round((min(_d, 2.0 * SEMANAS_POR_MES) / _base_xp) * 100)
                if abs(_pct - _e_pct) > 1:
                    _ruins.append(f'{_d} dobro(s): publica +{_pct}% e a conta da '
                                  f'+{_e_pct}%')
        for _r in _ruins:
            erro(f'3.1: a tabela do SS5.3 nao reconta: {_r}')
        if not _ruins:
            print(f'  [x] as {len(_lin53)} linhas da compensacao reconstroem da curva.')
        # a recomendacao tem de ser uma das linhas publicadas
        if DOBROS_REC is not None and DOBROS_REC not in [d for d, _, _, _ in _lin53]:
            erro(f'3.1: o SS5.3 recomenda {DOBROS_REC} mesa(s) de dobro e a tabela dele '
                 f'nao tem essa linha — a recomendacao aponta para um numero que o '
                 f'proprio documento nao mede')
        # e ela tem de ser a MENOR que resolve, senao a recomendacao gasta a toa
        _resolve = [d for d, m20, _, _ in _lin53 if m20 <= _fx['máximo']]
        if _resolve and DOBROS_REC is not None and DOBROS_REC != min(_resolve):
            aviso(f'3.1: o SS5.3 recomenda {DOBROS_REC} e a menor que traz a curva de '
                  f'volta para a faixa e {min(_resolve)} — a recomendacao esta gastando '
                  f'mecanismo a mais do que precisa')
elif PRONTO:
    erro('3.1: nao achei o SS5.3 da peca 12 — a tabela de compensacao e a outra metade '
         'da decisao do SS5.1, e sem ela a checagem 3 mede contra uma recomendacao que '
         'nao existe')


# ==========================================================================
bloco('3b. UMA MISSAO PODE ENTREGAR MAIS DE UM NIVEL?')
# ==========================================================================
TETO_NIVEIS_POR_MISSAO = 1
# O LIMITE DE DESIGN, que e' coisa diferente do teto aplicado. Comparar o resultado
# contra TETO_NIVEIS_POR_MISSAO seria auto-referencia: subir a constante subiria a
# regua junto, e a perturbacao passaria verde (licao no 8).
MAXIMO_DE_DESIGN = 1


def sobe_uma_missao(nivel, xp_ganho, teto=TETO_NIVEIS_POR_MISSAO):
    sobra, subiu, n = xp_ganho, 0, nivel
    while n < NIVEL_TETO and sobra >= custo(n) and (teto is None or subiu < teto):
        sobra -= custo(n)
        n += 1
        subiu += 1
    return subiu, sobra


if TAMANHO:
    print(f"  {'no nivel':<12}" + ''.join(f'{k:<16}' for k in TAMANHO))
    for nv in (2, 3, 4, 8, 20):
        linha = [f'{s} niv, +{r:.0f}' for s, r in
                 (sobe_uma_missao(nv, v) for v in TAMANHO.values())]
        print(f'  {nv:<12}' + ''.join(f'{x:<16}' for x in linha))

    _sem_teto = max(sobe_uma_missao(nv, v, teto=None)[0]
                    for nv in range(NIVEL_INICIAL, NIVEL_TETO)
                    for v in TAMANHO.values())
    print(f'\n  Sem o teto, a pior combinacao entregaria {_sem_teto} nivel(is) de uma vez.')

    if TETO_NIVEIS_POR_MISSAO > MAXIMO_DE_DESIGN:
        erro(f'3b: o teto aplicado e {TETO_NIVEIS_POR_MISSAO} nivel(is) por missao e o '
             f'limite de design e {MAXIMO_DE_DESIGN}')
    _acima = [(nv, nome) for nv in range(NIVEL_INICIAL, NIVEL_TETO)
              for nome, v in TAMANHO.items()
              if sobe_uma_missao(nv, v)[0] > MAXIMO_DE_DESIGN]
    for nv, nome in _acima:
        erro(f'3b: no nivel {nv} uma missao "{nome}" entrega mais de '
             f'{MAXIMO_DE_DESIGN} nivel, acima do limite de design')

    # v0.196: com a curva represada o teto DEIXOU de morder, e a peca declara isso.
    # A checagem guarda a RELACAO entre o que a curva faz e o que o SS3.1 afirma —
    # nos dois sentidos, senao ela sai verde tanto com a declaracao certa quanto
    # com a errada.
    _declara_frouxo = 'DEIXOU DE MORDER' in P12
    if _sem_teto <= MAXIMO_DE_DESIGN and not _declara_frouxo:
        erro('3b: nenhuma combinacao de nivel e tamanho passa de um nivel, e o SS3.1 '
             'continua argumentando como se o teto mordesse — a regra virou rede de '
             'seguranca e a peca nao diz isso')
    elif _sem_teto > MAXIMO_DE_DESIGN and _declara_frouxo:
        erro(f'3b: o SS3.1 declara que o teto "DEIXOU DE MORDER" e a pior combinacao '
             f'entrega {_sem_teto} niveis — a declaracao ficou falsa, e ela e o que '
             f'permite o texto nao explicar mais o teto')
    elif _sem_teto <= MAXIMO_DE_DESIGN:
        print('  [x] o teto nao morde em combinacao nenhuma, e o SS3.1 declara isso.')
    else:
        print(f'  [x] com o teto, nenhuma combinacao passa do limite de design.')


# ==========================================================================
bloco('4. O RETORNO DECRESCENTE ZERA ALGUEM?')
# ==========================================================================
print('  Ele e decrescente em vez de teto duro por um motivo de mesa: seis horas de')
print('  sessao que terminam em zero fazem a pessoa nao voltar.\n')
for i, p in enumerate(PESOS):
    print(f'  {i + 1}a missao da semana: {p:.0%}')
    if p <= 0:
        erro(f'4: a {i + 1}a missao da semana paga zero — o retorno decrescente virou '
             f'teto duro, e a regra vira motivo de briga em vez de ritmo')

if PESOS:
    _cheias = sum(1 for p in PESOS if p >= 1.0)
    _decai = [PESOS[i + 1] / PESOS[i] for i in range(_cheias, len(PESOS) - 1)
              if PESOS[i]]
    if _cheias < 1:
        erro('4: nenhuma missao da semana paga cheio')
    elif not _decai:
        erro('4: a tabela do SS5 nao tem degrau decrescente nenhum depois das cheias')
    elif not all(0.4 < d < 0.6 for d in _decai):
        erro(f'4: os degraus do desconto da semana sao {[round(d, 2) for d in _decai]} '
             f'e a regra do SS5 diz "cai pela metade a cada uma"')
    else:
        print(f'\n  [x] {_cheias} cheias, e dai pela metade: '
              f'{[round(d, 2) for d in _decai]}.')

if PRONTO and MISSOES_20:
    _sem = MISSOES_20 / (4.0 * SEMANAS_POR_MES)
    _com = MISSOES_20 / (equiv_semana(4.0) * SEMANAS_POR_MES)
    print(f'\n  Sem o decrescente, quem joga 4x por semana chega ao nivel 20 em '
          f'{_sem:.1f} meses; com ele, em {_com:.1f}.')
    if _com <= _sem * 1.2:
        aviso('4: o retorno decrescente quase nao muda o ritmo de quem joga muito — ele '
              'esta frouxo demais para fazer o trabalho que justifica existir')


# ==========================================================================
bloco('5. A FAIXA LENDARIA E MAIS CURTA EM TEMPO?')
# ==========================================================================
if PRONTO and MISSOES_20:
    _xp_m = acumulado(NIVEL_LIMIAR)
    _xp_l = acumulado(NIVEL_TETO) - acumulado(NIVEL_LIMIAR)
    _mesas_m = sum(mesas(n) for n in range(NIVEL_INICIAL, NIVEL_LIMIAR))
    _mesas_l = sum(mesas(n) for n in range(NIVEL_LIMIAR, NIVEL_TETO))
    print(f'  mundana  (2 -> 20, 18 niveis): {_mesas_m} mesas / {_xp_m} XP, '
          f'~{MISSOES_20:.0f} missoes de {MEDIA_MUNDANA}')
    print(f'  lendaria (20 -> 30, 10 niveis): {_mesas_l} mesas / {_xp_l} XP, '
          f'~{MISSOES_30:.0f} missoes de {MEDIA_LENDARIA}')

    if _mesas_l <= _mesas_m:
        aviso(f'5: a faixa lendaria custa {_mesas_l} mesas contra {_mesas_m} da mundana '
              f'— dez niveis de topo ficaram mais baratos que dezoito de base')
    if MISSOES_30 >= MISSOES_20:
        erro(f'5: a faixa lendaria leva {MISSOES_30:.0f} missoes contra '
             f'{MISSOES_20:.0f} da mundana — as catorze opinioes concordaram que ela e '
             f'mais curta em tempo, e a regra parou de entregar isso')
    else:
        _razao = MISSOES_30 / MISSOES_20
        print(f'\n  Razao: {_razao:.2f}.')
        # a faixa pedida e' do levantamento, e nao deste arquivo
        _pedida = re.search(r'a Guilda pediu entre `([\d,]+)` e `([\d,]+)`', P12)
        _folga = (0.35, 0.75)
        if not (_folga[0] <= _razao <= _folga[1]):
            aviso(f'5: a razao {_razao:.2f} saiu da folga de {_folga[0]} a {_folga[1]}')
        else:
            print(f'  [x] dentro da folga de {_folga[0]} a {_folga[1]}.')

        # --- CONTRA-TESTE: quem faz a faixa lendaria ser rapida e' a MISSAO
        # Se o topo rodasse missao mundana, ele seria MAIS LENTO que a base. E'
        # isso que separa "a curva faz" de "o tamanho da missao faz", e foi o erro
        # que o Mizuki pegou lendo a tabela do rascunho.
        _se_mundano = _xp_l / MEDIA_MUNDANA
        print(f'\n  Contra-teste — se o topo rodasse missao mundana ele levaria '
              f'{_se_mundano:.0f} missoes,')
        print(f'  contra {MISSOES_20:.0f} da base: {_se_mundano / MISSOES_20:.1f}x MAIS '
              f'LENTO, e nao a metade.')
        if _se_mundano <= MISSOES_20:
            erro('5: o contra-teste quebrou — mesmo rodando missao mundana o topo sairia '
                 'mais rapido que a base, entao quem faz a faixa lendaria ser curta '
                 'passou a ser a CURVA e nao o tamanho da missao. O SS4.1 afirma o '
                 'contrario, e a peca inteira se apoia nisso')
        else:
            print('  [x] quem faz a faixa lendaria ser curta e o tamanho da missao.')


# ==========================================================================
bloco('6. AS CINCO CADENCIAS RECONSTROEM? (peca 12 SS5.2)')
# ==========================================================================
# A tabela do SS5.2 tem 29 linhas x 5 colunas. Ela e' a evidencia medida da decisao,
# e uma tabela desse tamanho que nenhum validador recalcula envelhece na versao
# seguinte. Aqui ela e' recontada celula a celula das constantes lidas no bloco 0.
_s52 = _sec(P12, '### 5.2', '## 6. Mestrar')
_CADS = [0.5, 1.0, 2.0, 3.0, 4.0]
if not PRONTO:
    erro('6: sem a mistura de missao nao da para recontar a tabela das cadencias')
elif not _s52:
    erro('6: nao achei o SS5.2 da peca 12 — a tabela das cinco cadencias sumiu')
else:
    _pub = {}
    for _l in _s52.splitlines():
        m = re.match(r'\|\s*\*\*(\d+)\*\*\s*\|\s*([\d—-]+)\s*\|\s*(.+)\|\s*$', _l)
        if not m:
            continue
        _cols = [c.strip().strip('*') for c in m.group(3).split('|') if c.strip()]
        if len(_cols) != len(_CADS):
            continue
        _pub[int(m.group(1))] = (m.group(2).strip(), [_num(c) for c in _cols])
    print(f'  {len(_pub)} linha(s) lidas da tabela do SS5.2.')
    if len(_pub) != NIVEL_TETO - NIVEL_INICIAL + 1:
        erro(f'6: a tabela do SS5.2 rendeu {len(_pub)} linhas e tem de ter '
             f'{NIVEL_TETO - NIVEL_INICIAL + 1} (nivel {NIVEL_INICIAL} ao {NIVEL_TETO}) '
             f'— extrator que para de achar recontaria nada e sairia verde calado')
    else:
        _ruins, _mesas_ruins = [], []
        for nv, (mstr, vals) in sorted(_pub.items()):
            esperado_mesas = '—' if nv == NIVEL_TETO else str(mesas(nv))
            if mstr != esperado_mesas:
                _mesas_ruins.append(f'nv{nv} diz "{mstr}" e a curva diz '
                                    f'"{esperado_mesas}"')
            for ci, c in enumerate(_CADS):
                esp = round(meses_ate(nv, c), 1)
                if abs(vals[ci] - esp) > 0.051:
                    _ruins.append(f'nv{nv} col{c:g}/sem: publica {vals[ci]} e a conta '
                                  f'da {esp}')
        for r in _mesas_ruins[:4]:
            erro(f'6: a coluna "mesas" do SS5.2 nao bate com a curva do SS3 — {r}')
        if _ruins:
            erro(f'6: {len(_ruins)} celula(s) da tabela do SS5.2 nao reconstroem das '
                 f'constantes. As primeiras: ' + ' ; '.join(_ruins[:4]))
        if not _ruins and not _mesas_ruins:
            print(f'  [x] as {len(_pub) * (len(_CADS) + 1)} celulas reconstroem de '
                  f'{MEDIA_MUNDANA} / {MEDIA_LENDARIA} / {SEMANAS_POR_MES}.')

        # --- o pior vao, que e' a frase que a decisao inteira carrega -----
        _vao_pub = re.search(r'ele chega a `(\d+)` níveis, por volta do mês `(\d+)`',
                             _s52)
        if not _vao_pub:
            erro('6: o SS5.2 parou de publicar o pior vao ("ele chega a `N` niveis, por '
                 'volta do mes `M`") — e ele e o numero que sustenta a decisao de nao '
                 'ter gatilho')
        else:
            _n_pub, _m_pub = int(_vao_pub.group(1)), int(_vao_pub.group(2))
            # Varrer o tempo de 0,25 em 0,25 PULA a janela em que o vao acontece:
            # ele abre quando o de cima chega ao 30 e fecha quando o de baixo sobe,
            # e essa janela dura 0,2 mes. O vao so muda em instante de subida, entao
            # a varredura e' pelos instantes, e nao pelo relogio.
            _eventos = sorted({meses_ate(nv, c)
                               for nv in range(NIVEL_INICIAL + 1, NIVEL_TETO + 1)
                               for c in (1.0, 2.0)})
            _pior, _quando = 0, 0.0
            for _e in _eventos:
                _m = _e + 1e-6
                _a = max((nv for nv in range(NIVEL_INICIAL, NIVEL_TETO + 1)
                          if meses_ate(nv, 1.0) <= _m), default=NIVEL_INICIAL)
                _b = max((nv for nv in range(NIVEL_INICIAL, NIVEL_TETO + 1)
                          if meses_ate(nv, 2.0) <= _m), default=NIVEL_INICIAL)
                if _b - _a > _pior:
                    _pior, _quando = _b - _a, _m
            print(f'  pior vao entre 1/sem e 2/sem: {_pior} niveis, no mes '
                  f'{_quando:.1f}; o SS5.2 publica {_n_pub} e mes {_m_pub}.')
            if _pior != _n_pub:
                erro(f'6: o SS5.2 publica um vao de {_n_pub} niveis e a tabela dele '
                     f'produz {_pior}')
            elif abs(_quando - _m_pub) > 1.5:
                erro(f'6: o SS5.2 poe o pior vao no mes {_m_pub} e a conta poe no '
                     f'{_quando:.1f}')
            else:
                print('  [x] o vao publicado sai da propria tabela.')


# ==========================================================================
bloco('7. O GATILHO RECONSTROI? (peca 12 SS5.2)')
# ==========================================================================
# A tabela do gatilho e' o exemplo trabalhado que o livro cita, e ela e' a unica
# coisa desta peca que descreve regra que o projeto NAO adota. Justamente por isso
# ela precisa reconstruir: numero de exemplo que ninguem recalcula e' o primeiro a
# envelhecer.
if PRONTO and _s52:
    def teto_do_vao(fator, atras, meses=45.0, passo=0.25):
        e1 = equiv_semana(1.0) * SEMANAS_POR_MES
        e2 = equiv_semana(2.0) * SEMANAS_POR_MES
        nv1 = nv2 = NIVEL_INICIAL
        xp1 = xp2 = r1 = r2 = 0.0
        pior = 0
        for _ in range(int(meses / passo)):
            r1 += e1 * passo
            r2 += e2 * passo
            while r2 >= 1:
                r2 -= 1
                xp2 += media(nv2)
                s = 0
                while nv2 < NIVEL_TETO and xp2 >= custo(nv2) and s < 1:
                    xp2 -= custo(nv2)
                    nv2 += 1
                    s += 1
            while r1 >= 1:
                r1 -= 1
                mult = fator if (nv2 - nv1) >= atras else 1.0
                xp1 += media(nv1) * mult
                s = 0
                while nv1 < NIVEL_TETO and xp1 >= custo(nv1) and s < 1:
                    xp1 -= custo(nv1)
                    nv1 += 1
                    s += 1
            pior = max(pior, nv2 - nv1)
        return pior

    _lin = []
    for _l in _s52.splitlines():
        m = re.match(r'\|\s*(\d+) níveis atrás\s*\|\s*`([\d,]+)×`\s*\|\s*\**(\d+)\**\s*\|',
                     _l)
        if m:
            _lin.append((int(m.group(1)), _num(m.group(2)), int(m.group(3))))
    _sem_gat = re.search(r'^\| — \| — \| \*\*`(\d+)`\*\* \|', _s52, re.M)
    print(f'  {len(_lin)} linha(s) de gatilho lidas, mais a linha sem gatilho: '
          f'{"sim" if _sem_gat else "NAO"}')
    if len(_lin) < 3:
        erro(f'7: a tabela do gatilho rendeu {len(_lin)} linha(s) e precisa de pelo '
             f'menos tres — sem elas esta checagem sai verde sem recontar nada')
    elif not _sem_gat:
        erro('7: a tabela do gatilho perdeu a linha "sem gatilho" — ela e a base de '
             'comparacao, e sem ela as outras nao dizem quanto o gatilho comprou')
    else:
        _ruins = []
        for atras, fator, pub in _lin:
            _der = teto_do_vao(fator, atras)
            print(f'  {atras} niveis atras, fator {fator}x: publica {pub}, a conta da '
                  f'{_der}')
            if _der != pub:
                _ruins.append(f'{fator}x publica {pub} e a conta da {_der}')
        _base = int(_sem_gat.group(1))
        _der_base = teto_do_vao(1.0, 3)
        if _der_base != _base:
            _ruins.append(f'sem gatilho publica {_base} e a conta da {_der_base}')
        for r in _ruins:
            erro(f'7: a tabela do gatilho nao reconta: {r}')
        if not _ruins:
            print('  [x] toda linha do gatilho reconstroi.')
        # o gatilho tem de MELHORAR o vao, senao a tabela nao serve de conselho
        _piores = [(f, p) for a, f, p in _lin if p >= _base]
        if _piores:
            erro(f'7: gatilho(s) que nao melhoram o vao de {_base}: {_piores} — uma '
                 f'linha assim aconselha o servidor a gastar regra por nada')
        # e ele tem de ser MONOTONICO no fator, senao a frase "o fator decide" cai
        _ord = sorted(_lin, key=lambda t: t[1])
        if any(_ord[i][2] < _ord[i + 1][2] for i in range(len(_ord) - 1)):
            erro(f'7: o vao NAO cai monotonicamente com o fator: '
                 f'{[(f, p) for _, f, p in _ord]} — o SS5.2 afirma que "o fator decide '
                 f'o teto", e a tabela deixou de mostrar isso')


# ==========================================================================
bloco('8. A CONVERSAO DE MESTRAGEM RECONSTROI? (peca 12 SS6.2)')
# ==========================================================================
# --- o `20` da LINHA DE REGRA, e nao da secao -----------------------------
# Licao no 1: prosa SOBRE a regra nao e' a regra. Licao no 2: janela de N
# caracteres morre num ponto final — por isso o recorte sai da LINHA do bloco
# `>` que carrega a regra, e nao de uma janela em volta da palavra.
_s62 = _sec(P12, '## 6.2 ', '## 7.')
N_PUB = FATIA = TAXA_MAX = None
if not _s62:
    erro('8: nao achei o SS6.2 da peca 12 — a secao da conversao de mestragem sumiu, e '
         'esta checagem sairia verde sem ter lido regra nenhuma')
else:
    _regra62 = [l for l in _s62.splitlines()
                if l.startswith('>') and 'mesas mestradas' in l]
    if len(_regra62) != 1:
        erro(f'8: achei {len(_regra62)} linha(s) de regra com "mesas mestradas" no bloco '
             f'> do SS6.2, e tem de ser uma')
    else:
        _l = _regra62[0]
        _p = re.search(r'A cada (\w+) mesas mestradas', _l)
        N_PUB = PALAVRA.get(_p.group(1)) if _p else None
        if N_PUB is None:
            erro(f'8: a linha de regra do SS6.2 nao diz "A cada <numero> mesas '
                 f'mestradas", ou o numeral nao esta no dicionario: {_l[:90]}')
        if 'mensalidade' not in _l or 'seu Grau' not in _l:
            erro('8: a linha de regra do SS6.2 parou de pagar "uma mensalidade do seu '
                 'Grau" — se o valor virar numero proprio, ele deixa de ser a linha da '
                 'peca 12 SS6.1 e vira a segunda copia dela (licao no 9)')

        _f = re.search(r'o mundano inteiro cabe em `(\d+)%`', P12)
        FATIA = int(_f.group(1)) / 100 if _f else None
        if FATIA is None:
            erro('8: nao achei a fatia do mundano no SS6.1 da peca 12 — ela e um dos '
                 'dois donos do 20')
        _t = re.search(r'mestra (\d+)-(\d+) mesas por m[êe]s', LEV)
        TAXA_MAX = int(_t.group(2)) if _t else None
        if TAXA_MAX is None:
            erro('8: nao achei "mestra N-M mesas por mes" no levantamento — ele e o '
                 'outro dono do 20, e sem ele a divisao nao reproduz')

        if None not in (N_PUB, FATIA, TAXA_MAX):
            N_DER = TAXA_MAX / FATIA
            print(f'  regra publica: uma marca a cada {N_PUB} mesas mestradas')
            print(f'  derivado: {TAXA_MAX} mesas/mes (levantamento) / {FATIA:.0%} '
                  f'(SS6.1) = {N_DER:.1f}')
            if abs(N_PUB - N_DER) > 0.5:
                erro(f'8: a regra publica {N_PUB} mesas por marca e a divisao dos dois '
                     f'donos da {N_DER:.1f}. O SS6.2 afirma que nenhum dos dois numeros '
                     f'foi escolhido — se o 20 deixa de reproduzir, a afirmacao e falsa')
            else:
                print('  [x] o 20 nao foi escolhido: ele e a divisao dos dois donos.')

            # --- 8.1: o livro publica a FORMA, e a peca publica o VALOR ----
            # v0.195. O livro recomenda o que e' de cada servidor e nao decide por
            # ele — quanto se paga por mesa mestrada e' decisao de guilda. O livro
            # trocou o numero por `X`; a peca ficou dona da derivacao. E na primeira
            # aplicacao os dois divergiram em silencio.
            _CAP = os.path.join(AQUI, '..', '05-material', 'livro', 'manual',
                                '80-experiencia-e-progressao.md')
            _FORMA = re.compile(r'a cada `X` mesas mestradas', re.I)
            _NUM_LIV = re.compile(r'a cada (?:`)?(\d+|vinte|dez|quinze)(?:`)? mesas '
                                  r'mestradas', re.I)
            _DECLARA = re.compile(r'DEIXOU DE SER REGRA', re.I)
            if not os.path.isfile(_CAP):
                erro('8.1: nao achei o capitulo de XP do livro — e ele e o outro lado da '
                     'relacao que esta checagem guarda')
            else:
                _liv = open(_CAP, encoding='utf-8').read()
                _tem_forma = bool(_FORMA.search(_liv))
                _tem_num = bool(_NUM_LIV.search(_liv))
                _declara = bool(_DECLARA.search(_s62))
                if _tem_forma and not _declara:
                    erro('8.1: o livro publica a FORMA ("a cada `X` mesas mestradas") e o '
                         'SS6.2 desta peca nao declara que o numero deixou de ser regra — '
                         'a peca continua lendo como lei o que o livro entrega ao servidor')
                elif _tem_num and _declara:
                    erro('8.1: o livro voltou a publicar um NUMERO de mesas mestradas, e '
                         'o SS6.2 continua declarando que aquilo virou recomendacao — as '
                         'duas nao podem ser verdade juntas')
                elif not _tem_forma and not _tem_num:
                    erro('8.1: o capitulo de XP do livro nao publica nem a forma nem o '
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
                erro(f'8: a tabela de ritmo do SS6.2.1 rendeu {len(_linhas)} linha(s) e '
                     f'sao tres — extrator que para de achar recontaria nada')
            else:
                _ruins = []
                for _nome, _taxa, _meses, _pct in _linhas:
                    _m_esp = round(N_PUB / _taxa, 1)
                    _p_esp = round(_taxa / N_PUB * 100, 1)
                    if abs(_meses - _m_esp) > 0.15:
                        _ruins.append(f'"{_nome}" publica {_meses} meses e '
                                      f'{N_PUB}/{_taxa} da {_m_esp}')
                    if abs(_pct - _p_esp) > 0.6:
                        _ruins.append(f'"{_nome}" publica {_pct}% e {_taxa}/{N_PUB} da '
                                      f'{_p_esp}%')
                for _r in _ruins:
                    erro(f'8: a tabela do SS6.2.1 nao reconta: {_r}')
                if not _ruins:
                    print(f'  [x] as tres linhas da tabela reconstroem de N={N_PUB}.')
                _tx = [t for _, t, _, _ in _linhas]
                if max(_tx) != TAXA_MAX:
                    erro(f'8: a tabela do SS6.2.1 chama {max(_tx)} de teto relatado e o '
                         f'levantamento diz {TAXA_MAX}')

            # --- a marca e' mais rara que o marco ------------------------
            # Nao e' auto-referencia: os marcos vem da peca 2, e os meses vem da
            # cadencia real da Guilda, que o SS6.2.1 cita e o SS5 mede.
            _mm = re.search(r'duas mesas por semana — em `([\d,]+)` meses até o nível 20',
                            P12)
            _mc = re.search(r'n[íi]veis \*\*([\d, e]+)\*\*, sete marcos', P02)
            if not _mm or not _mc:
                erro('8: nao achei a janela em meses do SS6.2.1 ou os sete marcos da '
                     'peca 2 — sem os dois a comparacao de raridade nao tem contra o '
                     'que medir')
            else:
                _meses20 = _num(_mm.group(1))
                _der20 = MISSOES_20 / (equiv_semana(2.0) * SEMANAS_POR_MES) \
                    if PRONTO and MISSOES_20 else None
                if _der20 is not None and abs(_meses20 - _der20) > 0.15:
                    erro(f'8: o SS6.2.1 cita {_meses20} meses ate o nivel 20 e o SS5 '
                         f'mede {_der20:.1f} — a citacao envelheceu')
                _marcos = [int(x) for x in re.findall(r'\d+', _mc.group(1))]
                _ate20 = len([m for m in _marcos if m <= NIVEL_LIMIAR])
                _marcas = _meses20 * TAXA_MAX / N_PUB
                print(f'  ate o nivel 20 ({_meses20} meses a duas mesas por semana): '
                      f'{_marcas:.1f} marca(s) contra {_ate20} marcos')
                if _marcas >= _ate20:
                    erro(f'8: o mestre mais pesado fecha {_marcas:.1f} marcas ate o '
                         f'nivel 20 e a ficha atravessa {_ate20} marcos — o SS6.2.1 '
                         f'afirma que a marca e MENOS frequente que o marco, e ela '
                         f'deixou de ser')
                else:
                    print('  [x] a marca e mais rara que o marco, como o SS6.2.1 diz.')


# ==========================================================================
bloco('9. A LISTA DE FEITOS E FECHADA E ANCORADA? (peca 12 SS7.1)')
# ==========================================================================
_s71 = _sec(P12, '### 7.1 ', '### 7.2')
if not _s71:
    erro('9: nao achei o SS7.1 da peca 12 — a lista de feitos do limiar sumiu')
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
        erro('9: o titulo do SS7.1 nao diz "As <numero>" — sem ele a contagem da tabela '
             'nao tem segunda copia para bater, e a licao no 9 fica sem guarda')
    elif len(_feitos) != N_PROSA:
        erro(f'9: a tabela do SS7.1 tem {len(_feitos)} entradas e o titulo diz {N_PROSA} '
             f'— um numero, dois donos, e eles divergiram')
    elif len(_feitos) < 4:
        erro(f'9: so {len(_feitos)} entrada(s) legiveis — o extrator parou de achar e as '
             f'checagens abaixo passariam trivialmente')
    else:
        if [n for n, _, _ in _feitos] != list(range(1, len(_feitos) + 1)):
            erro(f'9: a numeracao das entradas do SS7.1 tem buraco: '
                 f'{[n for n, _, _ in _feitos]}')

        _sem = []
        for _n, _feito, _confere in _feitos:
            if not re.search(r'pe[çc]a \d+|manual|se[çc][ãa]o \d+', _confere):
                _sem.append(f'{_n} ("{_feito[:40]}")')
        if _sem:
            for _s in _sem:
                erro(f'9: a entrada {_s} nao diz em que documento o fato mora — sem dono, '
                     f'conferir vira julgamento e a lista deixa de atravessar sete mesas')
        else:
            print('  [x] as oito entradas apontam para o documento que carrega o fato.')

        _arquivos = {int(f[:2]) for f in os.listdir(AQUI) if re.match(r'\d\d-.*\.md$', f)}
        _mortas = sorted({int(p) for _, _, c in _feitos
                          for p in re.findall(r'pe[çc]a (\d+)', c)} - _arquivos)
        if _mortas:
            erro(f'9: a lista aponta para peca(s) que nao existem: {_mortas}')
        else:
            print('  [x] toda peca citada nas entradas existe em 03-mecanica/.')

        if 'palavra final' not in _s71:
            erro('9: o SS7.1 parou de dizer que a palavra final do mestre e sobre SE o '
                 'feito aconteceu, e nao sobre QUAIS sao — e essa frase e a diferenca '
                 'inteira entre lista fechada e lista de exemplo')

    # --- o limiar publica o XP acumulado, e ele sai da curva --------------
    _lim = re.search(r'Chegando aos ([\d.]+) de XP acumulado', P12)
    if not _lim:
        erro('9: o SS7 parou de publicar o XP do limiar ("Chegando aos N de XP '
             'acumulado") — e ele e a terceira copia da soma da curva')
    else:
        _lim_pub, _lim_der = _num(_lim.group(1)), acumulado(NIVEL_LIMIAR)
        if _lim_pub != _lim_der:
            erro(f'9: o SS7 publica {_lim_pub:.0f} de XP no limiar e a curva do SS3 soma '
                 f'{_lim_der} — o limiar ficou para tras da curva')
        else:
            print(f'  [x] o limiar publica {_lim_der} XP, que e a soma da curva.')


# --------------------------------------------------------------------------
print()
print('=' * 88)
if ERROS:
    print(f'>>> {len(ERROS)} PROBLEMA(S):')
    for e in ERROS:
        print('   -', e)
    sys.exit(1)
print('>>> TUDO OK — a tabela reconstroi da regra, a divida do atrasado encolhe e a')
print('    plana nao fecha, a cadencia da Guilda cabe na faixa pedida, ninguem sai com')
print('    zero, a faixa lendaria e curta por causa da MISSAO, e a tabela das cinco')
print('    cadencias e a do gatilho reconstroem, celula a celula, das constantes.')
if AVISOS:
    print(f'    {len(AVISOS)} aviso(s) acima, que nao falham o validador.')

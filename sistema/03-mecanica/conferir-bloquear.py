#!/usr/bin/env python3
"""conferir-bloquear.py — o validador dono da peca 23, `Bloquear`.

O Bloquear e' a unica rolagem do sistema que NAO usa d20, e a razao inteira
de ele existir e' aritmetica: `E[d20] = 10,5` contra uma base de Defesa `10`
da +2,5 pontos percentuais de graca. `2d10-1` tem media `10` exata.

Entao este validador confere uma coisa acima de todas as outras: QUE A
NEUTRALIDADE CONTINUA EXATA. Ela nao e' um numero publicado que da para
conferir contra si mesmo — ela e' recalculada por enumeracao das 2.000
combinacoes de `d20 x 2d10`, e comparada com a Defesa estatica.

NENHUM VALOR FICA ESCRITO AQUI DENTRO:
  a formula da Defesa .......... peca 1, a secao 5
  a formula do Bloquear ........ peca 23, a secao 3
  o dado do Bloquear ........... peca 23, a tabela da secao 2
  os dois multiplicadores ...... peca 23, a secao 3
  o bonus do Aparar ............ peca 23, a secao 3
  a folga do nivel 22 .......... peca 23, a secao 3.2
  o teto do liquido ............ peca 23, a secao 3.3
  as treze condicoes ........... peca 19, a secao 3
  a propriedade `Talha` ........ peca 14, a secao 5.2

A CHECAGEM 1 E' A UNICA DESTE PROJETO QUE EXISTE PARA SUSTENTAR UM NUMERO DE
OUTRA PECA. A peca 19 publica o `Incapacitado` em 11,00 porque a metade
"voce nao pode Bloquear" vale zero — e ela vale zero PORQUE o Bloquear e'
neutro. Se a neutralidade quebrar, aquele preco fica errado e ninguem mais
estaria olhando.

Roda de 03-mecanica/, sem argumento. Sai com codigo 1 se algo quebrar.
Ele NAO le o .docx e NAO precisa de python-docx: nao existe jeito de ele
sair verde tendo pulado checagem por falta de biblioteca.
"""
import os
import re
import sys
from itertools import product

MEC = os.path.dirname(os.path.abspath(__file__))
FALHAS = []

P01 = '01-atributos-acerto-defesa.md'
P14 = '14-equipamento.md'
P19 = '19-dano-e-condicoes.md'
P23 = '23-bloquear.md'


def erro(n, msg):
    FALHAS.append(f'{n}: {msg}')
    print(f'  !! {n}: {msg}')


def bloco(t):
    print()
    print('=' * 88)
    print(t)
    print('=' * 88)


def ler(nome):
    with open(os.path.join(MEC, nome), encoding='utf-8') as fh:
        return fh.read()


def num(s):
    m = re.search(r'(\d+(?:[,.]\d+)?)', str(s).replace('`', ''))
    return float(m.group(1).replace(',', '.')) if m else None


def celula_nome(linha):
    """o nome na primeira celula de uma linha de tabela, sem crase nem negrito"""
    return re.sub(r'[`*]', '', linha.strip().strip('|').split('|')[0]).strip()


T23 = ler(P23)
T19 = ler(P19)
T14 = ler(P14)
T01 = ler(P01)


# ==========================================================================
bloco('1. A NEUTRALIDADE — recalculada, e nao conferida contra si mesma')
# ==========================================================================
# O dado sai da tabela do SS2 da peca: a linha marcada em negrito e' a
# escolhida. Se alguem trocar o dado la, tudo abaixo se move junto.
_m = re.search(r'\|\s*\*\*`(\d+)d(\d+)([+−-]\d+)`\*\*\s*\|', T23)
if not _m:
    erro(1, 'nao achei o dado escolhido em negrito na tabela do SS2 da peca 23 — '
            'sem ele esta checagem nao tem o que enumerar')
    print('\n>>> FALHOU'); sys.exit(1)
QTD, FACES = int(_m.group(1)), int(_m.group(2))
AJUSTE = int(_m.group(3).replace('\u2212', '-'))
print(f'  o dado lido da peca: {QTD}d{FACES}{AJUSTE:+d}')

# a base da Defesa sai da peca 1, e a formula do Bloquear sai da peca 23
_m = re.search(r'Defesa\s*=\s*(\d+)\s*\+\s*Destreza\s*\+\s*proteção', T01)
if not _m:
    erro(1, 'nao achei `Defesa = N + Destreza + protecao` na peca 1 — a base da '
            'Defesa e o chao da neutralidade')
    print('\n>>> FALHOU'); sys.exit(1)
BASE_DEFESA = int(_m.group(1))

_m = re.search(r'`(\d+)d(\d+)\s*\+\s*\(a sua Defesa\s*[−-]\s*(\d+)\)`', T23)
if not _m:
    erro(1, 'nao achei a formula `NdM + (a sua Defesa - K)` no SS3 da peca 23')
    print('\n>>> FALHOU'); sys.exit(1)
OFFSET = int(_m.group(3))
print(f'  a base da Defesa, lida da peca 1: {BASE_DEFESA}')
print(f'  o offset escrito na regra da peca 23: {OFFSET}')

# --- 1.1 (v0.151): o valor do `Incapacitado` mora na peca 19 e esta peca o CITA.
# A v0.151 repreçou aquela condicao de 11,00 para 4,95, os 24 validadores sairam
# verdes, e esta peca continuou publicando 11,00 e 11,02 — porque ninguem comparava
# as duas copias. Licao no 9, no numero que esta peca existe para sustentar.
_m19 = re.search(r'\|\s*\*\*`Incapacitado`\*\*\s*\|\s*`([\d,]+)`\s*\|', T19)
if not _m19:
    erro(1, 'nao achei a linha do `Incapacitado` na tabela do SS2.2 da peca 19 — '
            'esta peca cita o valor dela e ficou sem o dono para comparar')
else:
    _v19 = float(_m19.group(1).replace(',', '.'))
    # ⚠ Nao existe lista de formas de citar: a primeira versao desta sub-checagem
    # casava "iria para" e "em", e o §5.1 citava o numero numa TERCEIRA forma —
    # que sobreviveu ao repreco com a checagem verde. Hoje ela pega TODO `N,NN`
    # que apareça a menos de 200 caracteres da palavra `Incapacitado`, e a peca 23
    # e' obrigada a nao guardar numeral historico: o valor velho fica em discurso
    # indireto, que e' a convencao que a v0.143 pagou para escrever.
    _achou = []
    for _mi in re.finditer(r'Incapacitado', T23):
        _jan = T23[max(0, _mi.start() - 200): _mi.end() + 200]
        _achou += re.findall(r'`(\d+,\d{2})`', _jan)
    _aqui = sorted({float(x.replace(',', '.')) for x in _achou})
    # guarda de contagem: sem ela, a peca parar de citar o valor deixa esta
    # sub-checagem VERDE e calada — que e' a licao no 8 por outra porta. Sao DOIS
    # valores distintos hoje: o da peca 19 e ele mais o `+0,02` da metade.
    if len(_aqui) < 2:
        erro(1, f'a peca 23 cita {len(_aqui)} valor(es) do `Incapacitado` e eu '
                'esperava 2 — ela parou de citar, ou mudou de forma, e esta '
                'sub-checagem deixaria de comparar as duas copias em silencio')
    else:
        # o `+0,02` da metade do Bloquear e' o unico desvio legal
        _fora = [v for v in _aqui if abs(v - _v19) > 0.05 and abs(v - _v19 - 0.02) > 0.005]
        if _fora:
            erro(1, f'a peca 23 publica o `Incapacitado` em {_fora} e a peca 19, que '
                    f'e a dona, publica {_v19:.2f} — as duas copias divergiram')
        else:
            print(f'  [x] o `Incapacitado` citado aqui bate com a peca 19: '
                  f'{_v19:.2f} de dano por rodada, em {len(_aqui)} citacao(oes)')

MEDIA_DADO = QTD * (FACES + 1) / 2.0
CASOS = list(product(range(1, 21), *[range(1, FACES + 1)] * QTD))
N = float(len(CASOS))
MAX_DADO = QTD * FACES
MIN_DADO = QTD


def multiplicador(alvo, trava_20, com_bloquear=True):
    """dano por ataque com golpe = 1. O crito dobra os dados: conta 2."""
    if not com_bloquear:
        return sum(2.0 if r == 20 else 1.0 for r in range(1, 21) if r >= alvo) / 20.0
    t = 0.0
    for caso in CASOS:
        r, dados = caso[0], caso[1:]
        s = sum(dados)
        if s == MAX_DADO:                      # Aparar: o ataque nao acerta
            if trava_20 and r == 20:           # ...a nao ser que a trava exista
                t += 2.0
            continue
        if r >= s + alvo - OFFSET:
            t += 2.0 if r == 20 else 1.0
    return t / N

# o alvo do d20 que produz o acerto de referencia: base + 1 e' o que a
# neutralidade exige, e e' isso que estamos testando — nao supondo.
ALVO = OFFSET
EST = multiplicador(ALVO, False, com_bloquear=False)
COM = multiplicador(ALVO, True)
SEM = multiplicador(ALVO, False)

print(f'  Defesa estatica ................ {EST:.4f}')
print(f'  Bloquear COM a trava do 20 nat . {COM:.4f}')
print(f'  Bloquear SEM a trava ........... {SEM:.4f}')

# 1a — a RELACAO: media do dado = base da Defesa + 1, e o offset = a media
if abs(MEDIA_DADO - (BASE_DEFESA + 1)) > 1e-9:
    erro('1a', f'a media de {QTD}d{FACES} e {MEDIA_DADO:g} e a base da Defesa e '
                f'{BASE_DEFESA}: para ser neutro o dado precisa de media '
                f'{BASE_DEFESA + 1:g}. O ajuste escrito ({AJUSTE:+d}) nao fecha '
                f'esse vao, e a regra ganhou vies de '
                f'{(MEDIA_DADO - BASE_DEFESA - 1) * 5:+.1f} pontos percentuais')
else:
    print(f'  [x] media({QTD}d{FACES}) = {MEDIA_DADO:g} = base da Defesa + 1. '
          f'O ajuste {AJUSTE:+d} fecha o meio ponto que dado unico nunca fecha.')

if OFFSET != int(MEDIA_DADO):
    erro('1b', f'a regra escreve `Defesa - {OFFSET}` e a media do dado e '
                f'{MEDIA_DADO:g} — os dois tem de ser o mesmo numero, senao a '
                f'troca deixa de ser neutra')
else:
    print(f'  [x] o offset da regra ({OFFSET}) e a media do dado ({MEDIA_DADO:g}) '
          f'sao o mesmo numero')

# 1c — a NEUTRALIDADE medida, e nao suposta
if abs(COM - EST) > 5e-4:
    erro('1c', f'o Bloquear rende {COM:.4f} contra {EST:.4f} da Defesa estatica — '
                f'vies de {(COM - EST) * 100:+.2f} pontos percentuais. A peca 19 '
                f'publica o `Incapacitado` em 11,00 SUPONDO que este vies e zero')
else:
    print(f'  [x] o Bloquear e neutro: {COM:.4f} dos dois lados, ao ponto flutuante')

# 1d — a trava do 20 natural PAGA a neutralidade, em vez de custar
if not (SEM < COM):
    erro('1d', f'sem a trava do 20 natural o multiplicador deveria ser MENOR que '
                f'com ela ({SEM:.4f} contra {COM:.4f}) — a trava existe porque ela '
                f'devolve o pedaco que o Aparar tirava do critico')
else:
    print(f'  [x] a trava do 20 natural paga a neutralidade: {SEM:.4f} -> {COM:.4f}')

# 1e — os dois multiplicadores publicados batem com os recalculados
_pub = re.search(r'de `(\d,\d{4})` para \*\*`(\d,\d{4})` exato\*\*', T23)
if not _pub:
    erro('1e', 'nao achei os dois multiplicadores publicados no SS3 da peca 23')
else:
    p_sem, p_com = num(_pub.group(1)), num(_pub.group(2))
    if abs(p_sem - SEM) > 5e-4 or abs(p_com - COM) > 5e-4:
        erro('1e', f'a peca publica {p_sem:.4f} -> {p_com:.4f} e a enumeracao da '
                    f'{SEM:.4f} -> {COM:.4f}')
    else:
        print(f'  [x] os dois numeros publicados batem com a enumeracao das '
              f'{int(N):,} combinacoes'.replace(',', '.'))


# ==========================================================================
bloco('2. O MODIFICADOR E A MESMA EXPRESSAO — nao dois valores que calham')
# ==========================================================================
# A forma mais forte possivel de "a mesma expressao" e a que a peca usa: o
# Bloquear e escrito EM FUNCAO da Defesa, e nao repetindo os termos dela.
# Esta checagem falha se alguem reescrever a regra somando os termos a mao,
# porque a partir dali as duas copias podem divergir (licao no 9).
_soma_a_mao = re.search(r'`\d+d\d+\s*[+-]\s*\d+\s*\+\s*Destreza\s*\+\s*proteção`', T23)
_em_funcao = re.search(r'`\d+d\d+\s*\+\s*\(a sua Defesa\s*[−-]\s*\d+\)`', T23)
if not _em_funcao:
    erro(2, 'a regra do SS3 nao escreve o Bloquear em funcao da Defesa — enquanto '
            'ela for escrita assim, nada pode subir um lado sem subir o outro')
else:
    print('  [x] a regra escreve o Bloquear EM FUNCAO da Defesa, e nao repetindo '
          'os termos dela')
if _soma_a_mao:
    print('  .. o SS2.3 mostra a forma expandida como equivalencia — e' + " ok, "
          'porque a REGRA do SS3 continua em funcao da Defesa')

# 2a — nenhuma outra peca da bonus a um lado so
# O menos deste projeto e' U+2212 e nao o hifen ASCII, e o negrito do markdown
# entra no meio: `**−1 no `Bloquear` de quem se defende**`. Ja errei as duas
# coisas nesta mesma versao — a checagem saia VERDE achando ZERO lugares, com a
# `Talha` escrita na peca 14 na frente dela.
_alvo = re.compile(r'([+−-]\s*\d+)[^\n]{0,20}?\bno\s+\**`?Bloquear`?', re.I)
_suspeitas = []
for _arq in sorted(f for f in os.listdir(MEC) if re.match(r'\d\d-.*\.md$', f)):
    if _arq == P23:
        continue
    for _l in ler(_arq).split('\n'):
        if _alvo.search(_l):
            _suspeitas.append((_arq, _l.strip()[:90]))
_TALHA_DECLARADA = 'Talha' in T23 and 'do **atacante**' in T23 or 'é do atacante' in T23
_fora = [s for s in _suspeitas if 'Talha' not in s[1]]
if _fora:
    for a, l in _fora:
        erro('2a', f'{a} mexe no numero do Bloquear e nao e a `Talha`: "{l}" — '
                   f'o invariante do SS4 diz que nada sobe um lado sem subir o outro')
else:
    print(f'  [x] {len(_suspeitas)} lugar(es) mexem no numero do Bloquear, e '
          f'{"todos sao a `Talha`" if _suspeitas else "nenhum e de outra peca"}')


# ==========================================================================
bloco('3. O LIQUIDO DO PACOTE DE EXTREMOS — recalculado dos donos')
# ==========================================================================
# Aparar e Brecha sao os dois unicos lugares onde o Bloquear deixa de ser
# neutro. Os dois valem ~1% cada, e a assimetria e o bonus do Aparar.
# As duas NAO tem a mesma probabilidade, e a diferenca e a trava do SS3:
# "o Aparar nao anula um 20 natural" tira 1/20 dos duplos-10, e nada tira nada
# da Brecha. O rascunho da v0.43 usava 1% dos dois lados, e por isso publicava
# um liquido 3% menor do que o real.
P_APARAR = sum(1 for c in CASOS if sum(c[1:]) == MAX_DADO and c[0] != 20) / N
P_BRECHA = sum(1 for c in CASOS if sum(c[1:]) == MIN_DADO) / N
print(f'  Aparar (soma maxima, MENOS o 20 natural) . {P_APARAR * 100:.2f}%')
print(f'  Brecha (soma minima, nada cancela) ....... {P_BRECHA * 100:.2f}%')

# o trafego: quantas vezes o dado muda o resultado em relacao a Defesa parada.
# E' a medida que o SS7.1 manda perguntar no playtest, e ela e simetrica.
_salvou = _traiu = 0
for _c in CASOS:
    _r, _s = _c[0], sum(_c[1:])
    _est = _r >= ALVO
    _blo = (_r == 20) if _s == MAX_DADO else (_r >= _s + ALVO - OFFSET)
    _salvou += _est and not _blo
    _traiu += _blo and not _est
TRAFEGO = (_salvou + _traiu) / N
print(f'  trafego: {TRAFEGO * 100:.1f}% — salvou {_salvou / N * 100:.1f}%, '
      f'traiu {_traiu / N * 100:.1f}%')
if abs(_salvou - _traiu) > 1:
    erro('3s', f'o trafego deixou de ser simetrico: salvou {_salvou / N * 100:.1f}% '
               f'e traiu {_traiu / N * 100:.1f}% — a assimetria E o vies que a peca '
               f'existe para nao ter')

_m = re.search(r'\|\s*\*\*`?\+(\d+)`? fixo\*\*\s*\|\s*`([\d,]+)`\s*\|', T23)
if not _m:
    erro(3, 'nao achei a linha do bonus fixo na tabela do SS3.2 da peca 23')
    BONUS = AO_BONIF = None
else:
    BONUS, AO_BONIF = int(_m.group(1)), num(_m.group(2))
    print(f'  o bonus do Aparar, lido da peca: +{BONUS} '
          f'(o seu ataque de oportunidade vale {AO_BONIF:.2f})')

_m = re.search(r'\|\s*chefe sozinho, qualquer nível\s*\|\s*`([\d,]+)`\s*\|', T23)
AO_BASE = num(_m.group(1)) if _m else None
_m = re.search(r'a Reação vale `([\d,]+)` contra os `([\d,]+)` do ataque de '
               r'oportunidade base, e a folga é `([\d,]+)` de dano esperado', T23)
if not _m:
    erro(3, 'nao achei a frase da folga do nivel 22 no SS3.2 — ela e o limite de '
            'design que separa o `+3` aplicado do teto derivado')
    REACAO_22 = AO_22 = FOLGA_PUB = None
else:
    REACAO_22, AO_22, FOLGA_PUB = (num(_m.group(1)), num(_m.group(2)),
                                   num(_m.group(3)))

# 3a — o liquido, recalculado. O chefe e o golpe saem da peca 19 SS2.1.
_m = re.search(r'\|\s*chefe e capanga no nível 30\s*\|\s*`(\d+)` e `(\d+)`', T19)
_m2 = re.search(r'\|\s*ações do chefe por rodada\s*\|\s*`(\d+)`', T19)
if not (_m and _m2):
    erro('3a', 'nao achei o chefe do nivel 30 nem as acoes dele na peca 19 SS2.1')
else:
    CHEFE, ACOES = float(_m.group(1)), float(_m2.group(1))
    GOLPE_CHEFE = CHEFE / ACOES
    if AO_BONIF is not None:
        liquido = P_APARAR * AO_BONIF - P_BRECHA * GOLPE_CHEFE
        print(f'  o golpe do chefe no nv30: {CHEFE:.0f} / {ACOES:.0f} acoes = '
              f'{GOLPE_CHEFE:.2f}')
        print(f'  liquido = {P_APARAR * 100:.2f}% x {AO_BONIF:.2f} - '
              f'{P_BRECHA * 100:.2f}% x {GOLPE_CHEFE:.2f} = {liquido:+.4f} por golpe')
        _pub = re.search(r'\|\s*\*\*com Aparar e Brecha, a `\+\d+`\*\*\s*\|\s*'
                         r'`−([\d,]+)`', T23)
        if not _pub:
            erro('3a', 'nao achei o liquido publicado na tabela do SS3.3')
        elif abs(abs(liquido) - num(_pub.group(1))) > 0.002:
            erro('3a', f'a peca publica {num(_pub.group(1)):.3f} de liquido e a '
                       f'conta dos donos da {abs(liquido):.3f}')
        else:
            print(f'  [x] o liquido publicado ({num(_pub.group(1)):.3f}) sai dos '
                  f'donos, e nao de uma constante escrita aqui')
        # 3b — o teto de 1% do golpe
        # O DENOMINADOR E' DECLARADO, e ate a v0.142 ele nao era: o rascunho
        # publicava "0,43% do golpe" sem dizer de que golpe, e a conta so fecha
        # com um 36 que nao tem dono em documento nenhum. Aqui e o golpe do
        # chefe, que a peca 19 SS2.1 publica.
        _pct = abs(liquido) / GOLPE_CHEFE
        _pubpct = re.search(r'`([\d,]+)%` do golpe do chefe', T23)
        if _pct >= 0.01:
            erro('3b', f'o liquido e {_pct * 100:.2f}% do golpe do chefe '
                       f'({GOLPE_CHEFE:.2f}), e o SS3.3 promete abaixo de 1%')
        elif not _pubpct:
            erro('3b', 'o SS3.3 nao declara a porcentagem contra o golpe do chefe — '
                       'porcentagem sem denominador escrito nao tem dono')
        elif abs(num(_pubpct.group(1)) / 100 - _pct) > 0.0002:
            erro('3b', f'o SS3.3 publica {num(_pubpct.group(1)):.2f}% e a conta da '
                       f'{_pct * 100:.2f}% do golpe do chefe')
        else:
            print(f'  [x] o liquido e {_pct * 100:.2f}% do golpe do chefe '
                  f'({GOLPE_CHEFE:.2f}), abaixo do teto de 1%, e o denominador '
                  f'esta declarado na peca')


# ==========================================================================
bloco('4. O `+3` DO APARAR E O MAIOR QUE CABE — a regra contra o limite')
# ==========================================================================
# Licao no 8: a regra aplicada (+3) e o limite de design (a folga do nv22)
# sao coisas separadas, e as duas sao conferidas. Perturbar o `+3` sozinho
# acende; perturbar a folga sozinha acende; mudar os dois de forma coerente
# fica VERDE de proposito, e e isso que prova que ela nao se mede contra si.
if None in (BONUS, AO_BASE, REACAO_22, AO_22, FOLGA_PUB):
    erro(4, 'faltou um dos quatro numeros do SS3.2 para derivar o teto do bonus')
else:
    # A v0.143 achou que o rascunho chamava de "folga" DOIS numeros diferentes:
    # 9,00 - 6,88 = 2,12 e' a folga em DANO ESPERADO, e 3,85 e' o teto do bonus
    # em DANO CRU — o mesmo 2,12 dividido pela taxa de acerto. O texto publicava
    # `3,86` como se fosse a subtracao, e a subtracao nao da isso.
    folga = REACAO_22 - AO_22
    if abs(folga - FOLGA_PUB) > 0.02:
        erro('4a', f'a peca escreve folga de {FOLGA_PUB:.2f} em dano esperado e '
                   f'{REACAO_22:.2f} - {AO_22:.2f} da {folga:.2f}')
    else:
        print(f'  [x] a folga do nivel 22, em dano esperado: {REACAO_22:.2f} - '
              f'{AO_22:.2f} = {folga:.2f}')
    # o acerto sai da propria enumeracao: e o multiplicador da Defesa estatica
    ganho_por_ponto = EST
    teto_bonus = folga / ganho_por_ponto
    print(f'  cada ponto de bonus rende {ganho_por_ponto:.4f} de dano esperado, '
          f'entao o teto em dano CRU e {teto_bonus:.2f}')
    _pubteto = re.search(r'teto do bônus é `([\d,]+)` de dano cru', T23)
    if not _pubteto:
        erro('4d', 'o SS3.2 nao publica o teto em dano cru com essas palavras — ele '
                   'e o limite de design, e sem ele a checagem 4 se mede contra o '
                   'proprio `+3`')
    elif abs(num(_pubteto.group(1)) - teto_bonus) > 0.02:
        erro('4d', f'o SS3.2 publica teto de {num(_pubteto.group(1)):.2f} de dano '
                   f'cru e a derivacao da {teto_bonus:.2f}')
    else:
        print(f'  [x] o teto publicado ({num(_pubteto.group(1)):.2f}) sai de '
              f'`folga / acerto`, e nao de uma constante')
    if BONUS > teto_bonus:
        erro('4b', f'o bonus publicado (+{BONUS}) passa do teto derivado '
                   f'({teto_bonus:.2f}) — a decisao do nivel 22 morre')
    elif BONUS + 1 <= teto_bonus:
        erro('4c', f'+{BONUS + 1} tambem caberia no teto ({teto_bonus:.2f}) — ou o '
                   f'bonus esta baixo demais, ou a folga foi medida errado. O SS3.2 '
                   f'promete que +{BONUS} e o MAIOR que cabe')
    else:
        print(f'  [x] +{BONUS} cabe com {teto_bonus - BONUS:.2f} de margem e '
              f'+{BONUS + 1} estoura: e o maior que cabe')


# ==========================================================================
bloco('5. SO O `Incapacitado` DESLIGA O BLOQUEAR — lido da peca 19')
# ==========================================================================
# Ela existe porque a proxima pessoa que ler o rascunho antigo vai querer
# acrescentar `Derrubado` ou `Agarrado`, e isso repreca duas condicoes que
# ja tem numero publicado na regua das treze.
_cond = {}
for _l in T19.split('\n'):
    _m = re.match(r'\|\s*\*\*`([A-Za-zçãíéóÇ]+)`\*\*\s*\|\s*`(Leve|Média|Pesada)`'
                  r'\s*\|\s*(.+?)\s*\|\s*$', _l)
    if _m:
        _cond[_m.group(1)] = _m.group(3)
if len(_cond) != 13:
    erro(5, f'li {len(_cond)} condicao(oes) no SS3 da peca 19 e esperava 13 — a '
            f'tabela mudou de forma e esta checagem parou de conferir')
else:
    _citam = sorted(n for n, t in _cond.items() if re.search(r'\bBloquear\b', t))
    if _citam != ['Incapacitado']:
        erro(5, f'as condicoes que citam Bloquear sao {_citam}, e o SS5 da peca 23 '
                f'diz que so o `Incapacitado` desliga — cada uma a mais e um '
                f'repreco na regua das treze, e nao uma regra nova')
    else:
        print(f'  [x] das 13 condicoes, so o `Incapacitado` cita Bloquear')
    _m = re.search(r'\|\s*\*\*`Incapacitado`\*\*\s*\|\s*`([\d,]+)`\s*\|\s*'
                   r'`([\d,]+)`\s*\|\s*`(Leve|Média|Pesada)`', T19)
    if not _m:
        erro('5a', 'nao achei a linha do `Incapacitado` na tabela de preco do SS2.2')
    else:
        print(f'  .. e ele continua em {num(_m.group(1)):.2f} de dano por rodada, '
              f'{num(_m.group(2)):.2f} fatias, nivel {_m.group(3)} — o preco que a '
              f'checagem 1 sustenta')


# ==========================================================================
bloco('6. A `Talha` E DO ATACANTE, e e a unica que encosta no Bloquear')
# ==========================================================================
_m = re.search(r'\|\s*\*\*`Talha`\*\*\s*\|\s*(\d+)\s*\|\s*(.+?)\s*\|', T14)
if not _m:
    erro(6, 'nao achei a `Talha` na tabela de propriedades da peca 14')
else:
    _custo, _texto = int(_m.group(1)), _m.group(2)
    _m2 = re.search(r'([−-]\s*\d+)\s*no\s*`Bloquear`\s*de\s*quem\s*se\s*defende',
                    _texto)
    if not _m2:
        erro('6a', f'a `Talha` deixou de dizer "-N no Bloquear de quem se defende": '
                   f'"{_texto}" — quem paga por ela precisa saber o que recebe')
    else:
        print(f'  [x] a `Talha` custa {_custo} ponto e da {_m2.group(1).strip()} no '
              f'Bloquear de quem se defende')
    # 6d: a CONTAGEM e a LISTA escritas na peca contra o catalogo de verdade.
    # A v0.143 achou o bilhete da v0.45 dizendo `sete` com nove no catalogo, e
    # o capitulo 13 do livro ja publicava nove. Contagem em prosa nao tem dono.
    _armas = sorted(celula_nome(l) for l in T14.split('\n')
                    if re.match(r'\|\s*[A-ZÀ-Ú]', l) and 'Talha' in l)
    print(f'  .. {len(_armas)} arma(s) do catalogo carregam a `Talha`')
    _EXT = {'uma': 1, 'duas': 2, 'três': 3, 'quatro': 4, 'cinco': 5, 'seis': 6,
            'sete': 7, 'oito': 8, 'nove': 9, 'dez': 10, 'onze': 11, 'doze': 12}
    _m3 = re.search(r'As \*\*(\w+)\*\* armas que carregam a propriedade', T14)
    if not _m3:
        erro('6d', 'a peca 14 nao escreve quantas armas carregam a `Talha` na forma '
                   '"As **N** armas que carregam a propriedade"')
    elif _EXT.get(_m3.group(1).lower()) != len(_armas):
        erro('6d', f'a peca 14 escreve `{_m3.group(1)}` armas com `Talha` e o '
                   f'catalogo tem {len(_armas)}: {", ".join(_armas)}')
    else:
        print(f'  [x] a contagem escrita na peca 14 (`{_m3.group(1)}`) bate com o '
              f'catalogo')
        _escritas = set(re.findall(r'`([A-ZÀ-Ú][^`]*)`',
                                   T14.split('em toda mesa:')[1].split('\n')[0]))
        _faltam = set(_armas) - _escritas
        _sobram = _escritas - set(_armas)
        if _faltam or _sobram:
            erro('6e', f'a lista nomeada na peca 14 nao bate com o catalogo — '
                       f'faltam {sorted(_faltam)}, sobram {sorted(_sobram)}')
        else:
            print(f'  [x] as {len(_armas)} nomeadas na peca 14 sao exatamente as do '
                  f'catalogo')
    # A primeira versao aceitava `é do atacante` solto, e a peca diz isso em DOIS
    # lugares — entao trocar a frase do SS4 saia VERDE porque a do SS6 segurava.
    # Agora ela cobra a declaracao do SS4, que e' onde mora o invariante.
    if not re.search(r'a `Talha` é do atacante e não toca em modificador nenhum '
                     r'do defensor', T23):
        erro('6b', 'a peca 23 parou de declarar que a `Talha` e do ATACANTE — sem '
                   'essa linha ela parece violar o invariante do SS4')
    else:
        print('  [x] a peca 23 declara que a `Talha` e do atacante, e por isso ela '
              'nao viola o invariante do modificador unico')
    # A primeira versao desta checagem olhava os 400 caracteres antes da frase
    # e procurava `Talha` dentro deles. A palavra caia fora da janela, entao ela
    # saia VERDE com a frase morta escrita na peca. Hoje ela procura as frases
    # diretamente: a divida da `Talha` foi paga na v0.143, e cada uma destas
    # afirma que ela nao foi.
    _mortas = [
        'é regra opcional',
        'Numa mesa que não a use',
        'onde a mesa usa a Defesa estática',
        'a sua mesa pode usar no lugar da Defesa',
    ]
    # CONVENCAO, e ela e' consequencia do metodo: esta checagem procura texto,
    # e texto nao distingue citacao historica de afirmacao viva. Entao frase
    # morta NAO volta entre aspas — a peca 14 registra o bilhete velho em
    # discurso indireto, e diz isso no proprio paragrafo. Tentar ensinar a
    # checagem a reconhecer "isto e' citacao" seria medir o marcador de novo.
    _vivas = [f for f in _mortas if f.lower() in T14.lower()]
    if _vivas:
        for _f in _vivas:
            erro('6c', f'a peca 14 ainda diz "{_f}" — o Bloquear deixou de ser '
                       f'opcional na v0.143, e a divida da `Talha` foi paga junto')
    else:
        print(f'  [x] nenhuma das {len(_mortas)} frases de opcionalidade sobreviveu '
              f'na peca 14')


# ==========================================================================
bloco('7. O BLOQUEAR E A UNICA ROLAGEM NAO-d20 DE UM NUMERO DISPUTADO')
# ==========================================================================
# Um segundo dado nao-d20 numa rolagem disputada seria uma familia nova de
# aritmetica, e a neutralidade teria de ser reprovada para ela tambem.
_padrao = re.compile(r'(?<![\w])(\d*d(?:4|6|8|10|12|100))\b')
_disputa = re.compile(r'no lugar da (?:sua )?Defesa|contra a Defesa|se defender', re.I)
_achados = []
for _arq in sorted(f for f in os.listdir(MEC) if re.match(r'\d\d-.*\.md$', f)):
    for _i, _l in enumerate(ler(_arq).split('\n'), 1):
        if not _disputa.search(_l):
            continue
        for _d in _padrao.findall(_l):
            if _d.lower() not in (f'{QTD}d{FACES}', 'd20', '1d20'):
                _achados.append((_arq, _i, _d, _l.strip()[:70]))
if _achados:
    for a, i, d, l in _achados:
        erro(7, f'{a}:{i} usa `{d}` numa rolagem que substitui a Defesa: "{l}" — '
                f'so o `{QTD}d{FACES}` do Bloquear pode, e a neutralidade dele foi '
                f'provada na checagem 1')
else:
    print(f'  [x] nenhuma rolagem que substitui a Defesa usa dado fora do '
          f'`{QTD}d{FACES}` e do `d20`')


# ==========================================================================
print()
print('=' * 88)
if FALHAS:
    print(f'>>> {len(FALHAS)} PROBLEMA(S)')
    for f in FALHAS:
        print('   -', f)
    sys.exit(1)
print('>>> TUDO OK — a neutralidade e exata e recalculada, o modificador e a mesma')
print('    expressao dos dois lados, o liquido dos extremos sai dos donos e cabe no')
print('    teto, o `+3` e o maior que cabe, so o `Incapacitado` desliga, e a `Talha`')
print('    e do atacante.')

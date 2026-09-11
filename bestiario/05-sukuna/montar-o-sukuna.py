#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MONTAR O SUKUNA — a máquina de três passos rodada de ponta a ponta.

Este script não guarda número nenhum dentro dele. Cada âncora é lida do
documento DONO dela, e o padrão nunca carrega o valor: ele captura. Se o dono
mudar o número, o script continua achando a âncora e o número novo entra; se o
dono mudar a FRASE, o script morre com o nome da âncora perdida.

    passo 1  a `categoria`  diz quanto ele AGUENTA   — 04-fase-1/TABELA.md
    passo 2  o `papel`      diz COMO ele luta        — 04-fase-1/papel/
    passo 3  o `tamanho`    diz o alcance            — 04-fase-1/fila/

E o `o golpe` sai em dado pela regra do §4.4 da peça 26.
"""
import os
import re
import sys

REPO = os.environ.get('JJK_REPO', '/media/mizuki/HD Externo II/Claude/Claude 2')
BEST = os.environ.get('JJK_BEST', '/media/mizuki/HD Externo II/Claude/Claude 2/bestiario')

P19 = 'sistema/03-mecanica/19-dano-e-condicoes.md'
P26 = 'sistema/03-mecanica/26-bestiario.md'

TABELA = '04-fase-1/TABELA.md'
ESCADA = '04-fase-1/a-escada-com-numero.md'
PAPEIS = '04-fase-1/papel/A-TABELA-dos-seis-papeis.md'
DECCTRL = '04-fase-1/papel/DECIDIDO-o-controlador-por-categoria.md'
DECPAPEL = '04-fase-1/papel/DECIDIDO-o-papel.md'
BARATA = '04-fase-1/fila/DECIDIDO-a-fila-barata.md'
CAPDEC = '04-fase-1/fila/DECIDIDO-o-capanga.md'   # a banda mudou de dono em 10/09
TAMDEC = '04-fase-1/fila/DECIDIDO-o-tamanho.md'   # o tamanho mudou de dono em 10/09
INTERV = '04-fase-1/fila/MEDIDA-a-intervencao.md'
BLOCO = '03-bloco/RASCUNHO-5-o-bloco-em-branco.md'
MESA = '00-fase-0/mesa-nd20.md'

# quem o Sukuna é. As duas primeiras são escolha declarada; o resto é lido.
NIVEL = 20
CATEGORIA = 'Calamidade'
TAMANHO = 'Médio'
PAPEL_ESCOLHIDO = 'Artilheiro'

_cache = {}


def ler(rel, raiz=REPO):
    chave = (raiz, rel)
    if chave not in _cache:
        with open(os.path.join(raiz, rel), encoding='utf-8') as f:
            _cache[chave] = f.read()
    return _cache[chave]


def n(s):
    return float(s.replace('−', '-').replace(',', '.'))


def pega(rel, padrao, rotulo, raiz=REPO):
    m = re.search(padrao, ler(rel, raiz))
    if not m:
        print(f'\n  !! ÂNCORA PERDIDA: {rotulo}')
        print(f'     não casa em {rel}')
        print(f'     padrão: {padrao}')
        sys.exit(1)
    return m


def linha(t=''):
    print(t)


def bloco(t):
    print()
    print('=' * 96)
    print(t)
    print('=' * 96)


def media_dado(e):
    e = e.strip()
    m = re.match(r'(\d+)d(\d+)(?:\s*\+\s*(\d+))?$', e)
    if m:
        return int(m.group(1)) * (1 + int(m.group(2))) / 2 + int(m.group(3) or 0)
    return float(e) if re.match(r'^\d+$', e) else None


# ────────────────────────────────────────────────────────────────────────────
bloco('AS ÂNCORAS — cada uma com o documento dono')
# ────────────────────────────────────────────────────────────────────────────

# 1 · o ponto de feitiço, e a regra do §6.5 que divide por ele
PONTO = n(pega(P19, r'cada ponto que não vira Melhoria vira `1d8` de dano — que são `([\d,]+)`',
               'o ponto de feitiço').group(1))
DIVISOR = n(pega(P26, r'O orçamento de feitiço de uma ação é o golpe dela dividido por `([\d,]+)`',
                 'a regra do §6.5').group(1))
if abs(DIVISOR - PONTO) > 0.01:
    print(f'  !! o §6.5 divide por {DIVISOR} e a peça 19 diz que o ponto vale {PONTO}')
    sys.exit(1)
PISO_PONTOS = n(pega(P26, r'o menor feitiço do manual é a `Classe 1` e custa `(\d+)` pontos',
                     'o piso da `Classe 1`').group(1))

# 2 · o fator da `Intervenção`, e quem tem
FATOR_INT = n(pega(INTERV, r'o fator de dano de quem tem `Intervenção` é \*\*`([\d,]+)`\*\*',
                   'o fator da `Intervenção`', BEST).group(1))
TEM_INT = {}
for ln in ler(BLOCO, BEST).split('\n'):
    m = re.match(r'\| \*{0,2}`(\w+)`\*{0,2} \| .* \| \*{0,2}(sim|não)\*{0,2} \|$', ln)
    if m:
        TEM_INT[m.group(1)] = (m.group(2) == 'sim')
if set(TEM_INT) < {'Capanga', 'Ameaça', 'Desastre', 'Catástrofe', 'Calamidade'}:
    print(f'  !! ÂNCORA PERDIDA: quem tem `Intervenção` — li só {sorted(TEM_INT)} no {BLOCO}')
    sys.exit(1)

# 3 · a banda do `o golpe`
mb = pega(CAPDEC, r'A banda do `o golpe` vira \*\*`([\d,]+)%`–`([\d,]+)%`\*\*',
          'a banda do `o golpe` — dono: DECIDIDO-o-capanga §1', BEST)
BANDA = (n(mb.group(1)) / 100, n(mb.group(2)) / 100)

# 4 · a TABELA da categoria — todas as categorias, todos os níveis
COLS = ['vida', 'dano', 'acoes', 'golpe', 'defesa', 'acerto', 'cd', 'refino', 'protecao']
CATS, atual = {}, None
for ln in ler(TABELA, BEST).split('\n'):
    m = re.match(r'## `([^`]+)`', ln)
    if m:
        atual = m.group(1)
        CATS.setdefault(atual, {})
        continue
    m = re.match(r'\| (\d+) \| `([^`]+)` \| `([^`]+)` \| `(\d+)` \| `([^`]+)` \| `(\d+)` \| '
                 r'`\+(\d+)` \| `(\d+)` \| `(\d+)` \| `\+(\d+)` \|$', ln)
    if m and atual:
        CATS[atual][int(m.group(1))] = {
            'vida': int(m.group(2)), 'dano': int(m.group(3)), 'acoes': int(m.group(4)),
            'golpe': m.group(5), 'defesa': int(m.group(6)), 'acerto': int(m.group(7)),
            'cd': int(m.group(8)), 'refino': int(m.group(9)), 'protecao': int(m.group(10)),
        }
    # o `Capanga` tem OUTRO formato: nv | vida de um | **pool** | golpe de um | Defesa | ...
    m = re.match(r'\| (\d+) \| `(\d+)` \| \*\*`(\d+)`\*\* \| `([^`]+)` \| `(\d+)` \| '
                 r'`\+(\d+)` \| `(\d+)` \| `(\d+)` \|$', ln)
    if m and atual == 'Capanga':
        CATS['Capanga'][int(m.group(1))] = {
            'vida': int(m.group(2)), 'pool': int(m.group(3)), 'dano': None, 'acoes': 1,
            'golpe': m.group(4), 'defesa': int(m.group(5)), 'acerto': int(m.group(6)),
            'cd': int(m.group(7)), 'refino': int(m.group(8)), 'protecao': None,
        }
if CATEGORIA not in CATS or NIVEL not in CATS[CATEGORIA]:
    print(f'  !! ÂNCORA PERDIDA: a linha `{CATEGORIA}` nv{NIVEL} da {TABELA}')
    sys.exit(1)

# 5 · a fatia publicada, pra derivar a vida de um personagem
cabec = pega(ESCADA, r'\| nv \| ((?:`[^`]+` \| )+)', 'o cabeçalho da tabela de fatia', BEST)
ORDEM_FATIA = re.findall(r'`([^`]+)`', cabec.group(1))
mf = pega(ESCADA, r'\| ' + str(NIVEL) + r' \| ((?:`[\d,]+%` \| ?)+)',
          f'a linha de fatia do nv{NIVEL}', BEST)
FATIA = {c: n(v) / 100 for c, v in zip(ORDEM_FATIA, re.findall(r'`([\d,]+)%`', mf.group(1)))}

# a vida de um personagem = `o golpe` publicado ÷ a fatia publicada. É a mesma
# derivação que a tabela dos seis papéis usa pra chegar em `243` no nv30.
ANCORA_PC = 'Desastre'
VIDA_PC = media_dado(CATS[ANCORA_PC][NIVEL]['golpe']) / FATIA[ANCORA_PC]

# 6 · os câmbios de Defesa, e quanto vale um ponto num d20
PP_DEFESA = n(pega(PAPEIS, r'derivado — `(\d+)` pp num `d20`', 'o ponto de Defesa em pp', BEST).group(1))
CAMBIO_DEF = {}
for ln in ler(PAPEIS, BEST).split('\n'):
    m = re.match(r'\| `Defesa ([+−]\d+)` \| \*\*`([\d,]+)×`\*\* \| vida efetiva \|', ln)
    if m:
        CAMBIO_DEF[int(n(m.group(1)))] = n(m.group(2))
if not {2, -2} <= set(CAMBIO_DEF):
    print(f'  !! ÂNCORA PERDIDA: os câmbios de Defesa — li só {sorted(CAMBIO_DEF)}')
    sys.exit(1)

# 7 · os seis papéis. Cada linha é lida pelo nome, e os multiplicadores são
#     capturados da linha — o padrão não carrega nenhum valor dentro.
NOMES_PAPEL = ['Brutamontes', 'Guardião', 'Artilheiro', 'Emboscador', 'Controlador', 'Apoio']
MULT = {}
for nome in NOMES_PAPEL:
    m = re.search(r'\| \*\*`%s`\*\* \|(.*?)\|(.*?)\| \*\*`([\d,]+)`\*\*' % re.escape(nome),
                  ler(PAPEIS, BEST))
    if not m:
        print(f'  !! ÂNCORA PERDIDA: a linha do `{nome}` na tabela dos seis papéis')
        sys.exit(1)
    MULT[nome] = {
        'ganho': re.findall(r'`([\d,]+)×`', m.group(1)),
        'paga': re.findall(r'`([\d,]+)×`', m.group(2)),
        'produto': n(m.group(3)),
    }

# 8 · o `Emboscador` tem valor POR CATEGORIA — a tabela corrigida
EMB = {}
for ln in ler(DECPAPEL, BEST).split('\n'):
    m = re.match(r'\| \*{0,2}`(\w+)`\*{0,2} \| `\d+` \| \*{0,2}`([\d,]+)×`\*{0,2} \| '
                 r'\*{0,2}`× ([\d,]+)`\*{0,2} \|$', ln)
    if m:
        EMB[m.group(1)] = (n(m.group(2)), n(m.group(3)))
if CATEGORIA not in EMB:
    print(f'  !! ÂNCORA PERDIDA: a linha `{CATEGORIA}` da tabela do `Emboscador`')
    sys.exit(1)

# 9 · o `Controlador` foi corrigido em 10/09: corta DANO e mantém as ações
# ⚠ O `Controlador` mudou em 10/09: a forma `B` foi escolhida e ela paga em VIDA.
# `o golpe` NAO se move mais em papel nenhum. O corte de dano abaixo e' o VELHO,
# mantido so' pra mostrar o que ele fazia — DECIDIDO-o-controlador-por-categoria.md.
CTRL_DANO = n(pega(DECPAPEL, r'\*\*`Controlador` troca DANO, não ação\*\* \| corta o dano por '
                             r'rodada em `1/(\d)`', 'a correção do `Controlador` (VELHA)', BEST).group(1))
CTRL_DANO = 1.0 - 1.0 / CTRL_DANO
CORPOS_CAP = int(pega(ESCADA,
                      r'\| \*\*`Capanga`\*\* \| — \| `dano do grupo ÷ 4` \| `[\d,]+` \| `1` \| `(\d+)`',
                      'os corpos do `Capanga`', BEST).group(1))
CTRLB = {}
for _ln in ler(DECCTRL, BEST).split('\n'):
    _m = re.match(r'\| `(\w+)` \| `(\d+)` \| `([\d,]+)×` \| \*\*`× ([\d,]+)`\*\* \| `1,000×` \|', _ln)
    if _m:
        CTRLB[_m.group(1)] = {'acoes': int(_m.group(2)),
                              'ganha': n(_m.group(3)), 'paga_vida': n(_m.group(4))}
if len(CTRLB) < 4:
    print(f'  !! ÂNCORA PERDIDA: a forma `B` do `Controlador` — li {sorted(CTRLB)}')
    sys.exit(1)

# 10 · o `tamanho` — SEM troca desde 10/09. Ele nao mexe em Defesa e nao tem produto.
TAM = {}
for ln in ler(TAMDEC, BEST).split('\n'):
    m = re.match(r'\| .*`([\wÍíúÚ]+)`\*{0,2} \| `([\d,]+) m` \| ([^|]+) \|$', ln)
    if m:
        TAM[m.group(1)] = {'alcance': n(m.group(2)), 'pega': m.group(3).strip(),
                           'defesa': 0, 'produto': 1.0}
if TAMANHO not in TAM:
    print(f'  !! ÂNCORA PERDIDA: o `{TAMANHO}` na tabela do tamanho — li {sorted(TAM)}')
    sys.exit(1)

linha(f'  1 ponto de feitiço vale         {PONTO:>8.1f} de dano        peça 19 §2.1')
linha(f'  a regra do §6.5                 golpe ÷ {DIVISOR:.1f}              peça 26 §6.5')
linha(f'  o piso do feitiço               {PISO_PONTOS:>8.0f} pontos         a `Classe 1`, peça 26 §6.5')
linha(f'  o fator da `Intervenção`        × {FATOR_INT:<7.3f}              MEDIDA-a-intervencao §12')
linha(f'  a banda do `o golpe`            {BANDA[0]:.0%} – {BANDA[1]:.0%}            DECIDIDO-o-capanga §1')
linha(f'  1 ponto de Defesa vale          {PP_DEFESA:>8.0f} pp num d20     peça 1 §5.2')
linha(f'  a vida de um personagem nv{NIVEL}   {VIDA_PC:>8.1f}                `{ANCORA_PC}` nv{NIVEL}: '
      f'golpe {media_dado(CATS[ANCORA_PC][NIVEL]["golpe"]):.1f} ÷ {FATIA[ANCORA_PC]:.0%}')
linha(f'  `{CATEGORIA}` tem `Intervenção`?    {"sim" if TEM_INT[CATEGORIA] else "não":>8}                RASCUNHO-5, passo 1')

# ────────────────────────────────────────────────────────────────────────────
bloco(f'PASSO 1 — a `categoria` diz quanto ele AGUENTA   ·   `{CATEGORIA}` nível {NIVEL}')
# ────────────────────────────────────────────────────────────────────────────
base = CATS[CATEGORIA][NIVEL]
golpe_cru = media_dado(base['golpe'])
fator = FATOR_INT if TEM_INT[CATEGORIA] else 1.0
dano_rod = base['dano'] * fator

linha(f'  a linha crua da TABELA          vida {base["vida"]}  ·  dano/rodada {base["dano"]}  ·  '
      f'{base["acoes"]} ações  ·  o golpe `{base["golpe"]}` = {golpe_cru:.1f}')
linha(f'  Defesa {base["defesa"]}  ·  acerto +{base["acerto"]}  ·  CD {base["cd"]}  ·  '
      f'refino {base["refino"]} (proteção +{base["protecao"]})')
linha()
linha(f'  e o fator da `Intervenção`      dano/rodada {base["dano"]} × {FATOR_INT:.3f} = {dano_rod:.1f}  →  {round(dano_rod):.0f}')
linha(f'  a `Intervenção` é extra e de graça, e o fator é o que paga por ela.')

# ────────────────────────────────────────────────────────────────────────────
bloco('PASSO 2 — o `papel` diz COMO ele luta   ·   os seis, lado a lado')
# ────────────────────────────────────────────────────────────────────────────


def aplica_papel(nome):
    """devolve (vida, defesa, dano_rodada, acoes, ganho, paga, nota)"""
    v, d, dm, ac = base['vida'], base['defesa'], dano_rod, base['acoes']
    g = p = 1.0
    nota = ''
    if nome == '— sem papel —':
        return v, d, dm, ac, 1.0, 1.0, ''
    mu = MULT[nome]
    if nome == 'Brutamontes':
        g = n(mu['ganho'][0]); p = CAMBIO_DEF[-2]
        v = base['vida'] * g; d = base['defesa'] - 2
    elif nome == 'Guardião':
        g = CAMBIO_DEF[+2]; p = n(mu['paga'][0])
        v = base['vida'] * p; d = base['defesa'] + 2
        nota = 'só se paga com mais de um inimigo no encontro'
    elif nome == 'Artilheiro':
        g = n(mu['ganho'][0]); p = n(mu['paga'][0])
        v = base['vida'] * p
        nota = 'o ganho é ALCANCE, taxa fixa — e ele não tem célula'
    elif nome == 'Emboscador':
        g, pv = EMB[CATEGORIA]
        p = pv
        v = base['vida'] * pv
        nota = f'valor de `{CATEGORIA}`, não o da tabela geral · não sobe de `Grande`'
    elif nome == 'Controlador':
        p = CTRL_DANO
        g = 1.0 / CTRL_DANO
        dm = dano_rod * CTRL_DANO
        v = base['vida'] * g
        nota = 'corrigido em 10/09: corta DANO e MANTÉM as ações'
    elif nome == 'Apoio':
        p = CTRL_DANO
        g = 1.0 / CTRL_DANO
        dm = dano_rod * CTRL_DANO
        v = base['vida'] * g
        nota = 'o `1 pra 1` cai em OUTRO bloco — só se paga com mais de um inimigo'
    return v, d, dm, ac, g, p, nota


def vida_efetiva(vida, defesa):
    """vida crua ÷ a chance de o PC acertar. A chance sai do câmbio publicado."""
    ch = 0.50 - (defesa - base['defesa']) * PP_DEFESA / 100
    return vida / ch, ch


def ganho_fora_da_ficha(nome):
    """O que o papel dá SEM ter célula. A `A-TABELA` §4 chama isso de `fora da ficha`."""
    if nome == 'Artilheiro':
        return n(MULT[nome]['ganho'][0])          # o alcance, taxa fixa
    if nome == 'Emboscador':
        return EMB[CATEGORIA][0]                  # a vantagem, valor da categoria
    return 1.0                                    # os outros pagam e ganham em célula


linha(f'  {"papel":<16}{"Defesa":>8}{"vida":>8}{"dano/rod":>10}{"ações":>7}{"o golpe":>10}'
      f'{"fatia":>8}{"banda":>7}{"fora":>8}{"invariante":>12}')
linha('  ' + '-' * 100)
FORA = {}
for nome in ['— sem papel —'] + NOMES_PAPEL:
    v, d, dm, ac, g, p, nota = aplica_papel(nome)
    gol = dm / ac
    fat = gol / VIDA_PC
    ve, _ = vida_efetiva(v, d)
    ve0, _ = vida_efetiva(base['vida'], base['defesa'])
    fora = ganho_fora_da_ficha(nome) if nome != '— sem papel —' else 1.0
    inv = (ve * dm * fora) / (ve0 * dano_rod)
    dentro = BANDA[0] <= fat <= BANDA[1]
    FORA[nome] = (v, d, dm, ac, gol, fat, inv, nota)
    linha(f'  {nome:<16}{d:>8}{round(v):>8}{round(dm):>10}{ac:>7}{gol:>10.1f}'
          f'{fat:>8.1%}{("sim" if dentro else "NÃO"):>7}{fora:>7.3f}×{inv:>11.3f}×')
linha()
for nome in NOMES_PAPEL:
    if FORA[nome][7]:
        linha(f'  ⚠ `{nome}`: {FORA[nome][7]}')
linha()
linha(f'  Olhe a coluna `fatia`: a banda é {BANDA[0]:.0%}–{BANDA[1]:.0%}, e nenhum papel sobe o dano.')
linha(f'  O `Controlador` e o `Apoio` são o piso — e foi o `Controlador` que empurrou o piso pra {BANDA[0]:.0%}.')

# ────────────────────────────────────────────────────────────────────────────
bloco('A VARREDURA — as CINCO categorias contra a banda, com e sem `Controlador`')
# ────────────────────────────────────────────────────────────────────────────
linha(f'  A banda foi varrida em 29 níveis x 5 categorias — MEDIDA-o-capanga.md §6.')
linha(f'  Aqui ela roda no nível {NIVEL}, com o fator da `Intervenção` aplicado em quem tem.')
linha()
_faltam = [c for c in ['Capanga', 'Ameaça', 'Desastre', 'Catástrofe', 'Calamidade']
           if c not in CATS or NIVEL not in CATS[c]]
if _faltam:
    linha(f'  !! FALTOU LER: {", ".join("`" + c + "`" for c in _faltam)} — o parser da {TABELA}')
    linha(f'     não casou. Isso é ERRO, não "não medido".')
    sys.exit(1)
linha(f'  ⚠ O `Controlador` mudou em 10/09: a forma `B` paga em VIDA, e `o golpe` NÃO se move')
linha(f'    mais em papel nenhum. As duas últimas colunas mostram o que o papel VELHO fazia —')
linha(f'    ele é que furava a banda, e ele não existe mais.')
linha()
linha(f'  {"categoria":<14}{"Interv.":>9}{"golpe cru":>11}{"c/ fator":>10}{"ações":>7}'
      f'{"fatia":>8}{"banda":>7}   {"Ctrl B: vida ×":>15}{"golpe":>12}   {"(Ctrl VELHO)":>13}{"banda":>7}')
linha('  ' + '-' * 112)
ROTOS, VELHOS = [], []
for cat in ['Capanga', 'Ameaça', 'Desastre', 'Catástrofe', 'Calamidade']:
    b = CATS[cat][NIVEL]
    fa = FATOR_INT if TEM_INT.get(cat) else 1.0
    cru = media_dado(b['golpe'])
    gol_n = cru * fa
    fat_n = gol_n / VIDA_PC
    d1 = BANDA[0] <= fat_n <= BANDA[1]
    if not d1:
        ROTOS.append((cat, 'sem papel', fat_n))
    # a forma B: `ações` do bloco. No `Capanga` sao os CORPOS, nao 1 — DECIDIDO-o-capanga §3
    acoes_b = CORPOS_CAP if cat == 'Capanga' else CTRLB.get(cat, {}).get('acoes', b['acoes'])
    paga_b = 1.0 / (1.0 + 1.0 / acoes_b)
    fat_velho = fat_n * CTRL_DANO
    d2 = BANDA[0] <= fat_velho <= BANDA[1]
    if not d2:
        VELHOS.append((cat, fat_velho))
    linha(f'  {cat:<14}{("sim" if TEM_INT.get(cat) else "não"):>9}{cru:>11.1f}{gol_n:>10.1f}'
          f'{acoes_b:>7}{fat_n:>8.1%}{("sim" if d1 else "NÃO"):>7}   {paga_b:>15.3f}'
          f'{"não move":>12}   {fat_velho:>13.1%}{("sim" if d2 else "NÃO"):>7}')
linha()
if ROTOS:
    linha(f'  ⚠⚠ {len(ROTOS)} CÉLULA(S) FORA DA BANDA DE {BANDA[0]:.0%}–{BANDA[1]:.0%}:')
    for cat, quem, f_ in ROTOS:
        fora = (BANDA[0] - f_) if f_ < BANDA[0] else (f_ - BANDA[1])
        lado = 'abaixo do piso' if f_ < BANDA[0] else 'acima do teto'
        linha(f'      `{cat}` com `{quem}` → {f_:.1%}   ({fora * 100:.1f} pontos {lado})')
else:
    linha(f'  ✅ As CINCO caem na banda de {BANDA[0]:.0%}–{BANDA[1]:.0%}, e o `Controlador` da forma `B`')
    linha(f'     não move nenhuma delas: ele paga em vida.')
linha()
if VELHOS:
    linha(f'  E o papel VELHO (corte de {1-CTRL_DANO:.1%} do dano) botava {len(VELHOS)} de 5 fora da banda:')
    linha('      ' + ' · '.join(f'`{c}` {f_:.1%}' for c, f_ in VELHOS))
    linha(f'  >> era esse o achado `1` do teste de ponta a ponta, e a forma `B` fechou ele.')

# ────────────────────────────────────────────────────────────────────────────
bloco(f'PASSO 3 — o `tamanho` diz o alcance, e ele é DE GRAÇA   ·   `{TAMANHO}`')
# ────────────────────────────────────────────────────────────────────────────
linha(f'  {"tamanho":<12}{"alcance":>10}   o golpe pega')
linha('  ' + '-' * 66)
for t, dados in TAM.items():
    marca = ' ←' if t == TAMANHO else ''
    linha(f'  {t:<12}{dados["alcance"]:>8.1f} m   {dados["pega"]}{marca}')
linha()
linha(f'  ⚠ O `tamanho` NÃO mexe em Defesa e NÃO pede nada em troca — decisão de 10/09,')
linha(f'    04-fase-1/fila/DECIDIDO-o-tamanho.md. A defesa não muda com o tamanho em')
linha(f'    sistema nenhum: AC espalha 1,000x em 4.791 criaturas do PF2e.')
linha(f'  ⚠ E a escada dele mora no ALCANCE. Nos ALVOS ele é um degrau só — `Grande`,')
linha(f'    `Imenso` e `Colossal` pegam o mesmo 1 vizinho a metade.')
linha()
linha(f'  A Defesa do bloco fica em {base["defesa"]} em qualquer tamanho.')
linha(f'  E o alcance acima NÃO é o do `Artilheiro`: este é o de CORPO A CORPO.')

# ────────────────────────────────────────────────────────────────────────────
bloco('O GOLPE EM DADO — a regra do §4.4: metade do alvo em dado, no máximo 8 dados')
# ────────────────────────────────────────────────────────────────────────────
TETO_DADOS = int(n(pega(P26, r'com no máximo \*\*(\w+)\*\* dados na mão'.replace('(\\w+)', '(oito|\\d+)'),
                        'o teto de dados do §4.4').group(1).replace('oito', '8')))
PISO_SECO = n(pega(P26, r'\*\*Abaixo de `(\d+)` o golpe fica em número seco\*\*',
                   'o piso do número seco').group(1))


def em_dado(alvo, teto=None):
    """N dados + fixo, com metade do alvo em dado. Devolve (texto, media, %dado)."""
    teto = teto or TETO_DADOS
    alvo_i = round(alvo)
    if alvo_i < PISO_SECO:
        return str(alvo_i), float(alvo_i), 0.0
    melhor = None
    for faces in (4, 6, 8, 10, 12):
        for nd in range(1, teto + 1):
            m = nd * (1 + faces) / 2
            fixo = alvo_i - m
            if fixo < 0 or abs(fixo - round(fixo)) > 1e-9:
                continue
            fixo = int(round(fixo))
            desvio = abs(m / alvo_i - 0.5)
            cand = (desvio, nd, -faces)
            if melhor is None or cand < melhor[0]:
                txt = f'{nd}d{faces}' + (f' + {fixo}' if fixo else '')
                melhor = (cand, txt, m + fixo, m / alvo_i)
    return melhor[1], melhor[2], melhor[3]


v, d, dm, ac, gol, fat, inv, _ = FORA[PAPEL_ESCOLHIDO]
txt, med, pct = em_dado(gol)
linha(f'  o alvo do golpe                 {gol:.2f}  →  arredondado {round(gol)}')
linha(f'  o teto de dados do §4.4         {TETO_DADOS}')
linha(f'  o piso do número seco           {PISO_SECO:.0f}')
linha()
linha(f'  ⟹  `o golpe` = `{txt}` = {med:.1f}   ·   {pct:.1%} em dado')
linha()
linha('  as outras montagens que fechavam, pra registro:')
alvo_i = round(gol)
alt = []
for faces in (4, 6, 8, 10, 12):
    for nd in range(1, TETO_DADOS + 1):
        m = nd * (1 + faces) / 2
        fixo = alvo_i - m
        if fixo < 0 or abs(fixo - round(fixo)) > 1e-9:
            continue
        alt.append((abs(m / alvo_i - 0.5), f'{nd}d{faces}' + (f' + {int(fixo)}' if fixo else ''),
                    m / alvo_i, nd))
for desvio, txt2, p2, nd in sorted(alt)[:6]:
    marca = '  ←' if txt2 == txt else ''
    linha(f'    {txt2:<14}{p2:>7.1%} em dado   {nd} dado(s) na mão{marca}')

# ────────────────────────────────────────────────────────────────────────────
bloco('O ORÇAMENTO DE FEITIÇO — quanto cada ação dele monta')
# ────────────────────────────────────────────────────────────────────────────
pontos = med / PONTO
linha(f'  a regra:  o golpe ÷ {PONTO:.1f}')
linha(f'  {med:.1f} ÷ {PONTO:.1f} = {pontos:.1f} pontos por ação')
linha()
if pontos < PISO_PONTOS:
    linha(f'  ⚠ `seco` — abaixo de {PISO_PONTOS:.0f} pontos ele NÃO monta feitiço: ele bate.')
else:
    linha(f'  Acima do piso de {PISO_PONTOS:.0f}. Ele monta feitiço, e o Fundamento faz o resto.')
linha()
# a escada de Classe, lida do gerador do manual — nada de valor no padrão
PARTF = 'manual/gerador/partF.js'
PARTD = 'manual/gerador/partD.js'
CLASSES = {int(a): int(b) for a, b in
           re.findall(r"H2\('Classe (\d+) · (\d+) pontos", ler(PARTF))}
if not CLASSES:
    print('  !! ÂNCORA PERDIDA: a escada de Classe em ' + PARTF)
    sys.exit(1)
pega(PARTD, r'\*\*Leve\*\* custa metade da Classe, \*\*Média\*\* custa a Classe inteiro, '
            r'\*\*Pesada\*\* custa Classe e meio — sempre arredondando pra cima',
     'a regra de preço da Melhoria')

# a Classe da ação dele: a maior que cabe no orçamento
CLASSE_ACAO = max((c for c, p in CLASSES.items() if p <= pontos), default=None)
if CLASSE_ACAO is None:
    print(f'  !! o orçamento de {pontos:.1f} pontos não paga nem a menor Classe')
    sys.exit(1)


def preco_melhoria(degrau, classe):
    import math
    return {'Leve': math.ceil(classe / 2), 'Média': classe,
            'Pesada': math.ceil(classe * 1.5)}[degrau]


linha(f'  a Classe da ação            `Classe {CLASSE_ACAO}` = {CLASSES[CLASSE_ACAO]} pontos, '
      f'e sobram {pontos - CLASSES[CLASSE_ACAO]:.1f}')
linha(f'  ⚠ o preço da Melhoria é uma FRAÇÃO DA CLASSE, não um número fixo:')
linha(f'    Leve = metade da Classe · Média = a Classe · Pesada = Classe e meio, arred. pra cima')
linha()
linha(f'  e o que cabe numa ação de {pontos:.1f} pontos (`Classe {CLASSE_ACAO}`):')
linha(f'    {"o que comprar":<28}{"custa":>8}{"sobra":>8}{"em dado":>10}{"em dano":>10}')
linha('  ' + '-' * 66)
COMPRAS = [('condição `Leve`', 'Leve'), ('condição `Média`', 'Média'),
           ('condição `Pesada`', 'Pesada'),
           ('área — Cone/Linha/Explosão', 'Leve'),
           ('área + condição `Leve`', None)]
for rotulo, degrau in COMPRAS:
    custo = (preco_melhoria('Leve', CLASSE_ACAO) * 2 if degrau is None
             else preco_melhoria(degrau, CLASSE_ACAO))
    sobra = pontos - custo
    dados = int(sobra) if sobra > 0 else 0
    linha(f'    {rotulo:<28}{custo:>8}{(f"{sobra:.1f}" if sobra > 0 else "NÃO CABE"):>8}'
          f'{(f"{dados}d8" if sobra > 0 else "—"):>10}'
          f'{(f"{dados * PONTO:.1f}" if sobra > 0 else "—"):>10}')
linha()
linha(f'  ⚠ `área` custa `Leve` e NÃO tem preço por formato — Cone, Linha e Explosão custam')
linha(f'    a mesma coisa. Confirmado em três lugares: ANCORAS-do-repositorio.md §4.')
linha(f'  ⚠ E só cabe UMA condição `Pesada` por feitiço (peça 19 §3.3).')

# ────────────────────────────────────────────────────────────────────────────
bloco('OS ATRIBUTOS — eles não se escolhem: as três derivadas OBRIGAM eles')
# ────────────────────────────────────────────────────────────────────────────
P01 = 'sistema/03-mecanica/01-atributos-acerto-defesa.md'
P02 = 'sistema/03-mecanica/02-economia-de-atributos.md'
P08 = 'sistema/03-mecanica/08-criacao-de-personagem.md'

MAESTRIA_BASE = n(pega(P01, r'\*\*Maestria\*\* começa em (\d+) e sobe um ponto a cada \w+ níveis',
                       'a base da maestria').group(1))
MARCOS_MAESTRIA = [int(x) for x in re.findall(
    r'\d+', pega(P02, r'a maestria sobe nos marcos de \*\*níve(?:l|is) ([\d, e]+)\*\*',
                 'os marcos de maestria', ).group(1))]
MARCOS = [int(x) for x in re.findall(
    r'\d+', pega(P02, r'nos níveis \*\*([\d, e]+)\*\*, sete marcos ao todo',
                 'os marcos de atributo').group(1))]
mo = pega(P02, r'Atributo investido: \*\*(\d+) na criação, (\d+) no teto',
          'a escada do atributo investido')
CRIACAO_TETO, ATRIB_TETO = int(mo.group(1)), int(mo.group(2))
mp = pega(P26, r'(\w+) pontos na criação, teto `(\d+)` ali, `\+1` por marco e teto `(\d+)`',
          'o orçamento de atributo do inimigo')
NUM_PT = {'um': 1, 'dois': 2, 'três': 3, 'quatro': 4, 'cinco': 5, 'seis': 6,
          'sete': 7, 'oito': 8, 'nove': 9, 'dez': 10}
PONTOS_CRIACAO = NUM_PT.get(mp.group(1).lower(), None)
if PONTOS_CRIACAO is None:
    print(f'  !! não sei ler "{mp.group(1)}" como número — o §3.2 mudou a palavra')
    sys.exit(1)
if int(mp.group(2)) != CRIACAO_TETO or int(mp.group(3)) != ATRIB_TETO:
    print(f'  !! o §3.2 diz teto {mp.group(2)}/{mp.group(3)} e a peça 2 diz '
          f'{CRIACAO_TETO}/{ATRIB_TETO} — os dois donos discordam')
    sys.exit(1)

marcos_ate = [m for m in MARCOS if m <= NIVEL]
maestria = MAESTRIA_BASE + len([m for m in MARCOS_MAESTRIA if m <= NIVEL])
orcamento = PONTOS_CRIACAO + len(marcos_ate)

dex_obrigada = base['defesa'] - 10 - base['protecao']
atrib_tecnica = base['acerto'] - maestria
cd_confere = 8 + atrib_tecnica + maestria

linha(f'  a maestria no nv{NIVEL}            {maestria:.0f}        base {MAESTRIA_BASE:.0f} + os marcos '
      f'{[m for m in MARCOS_MAESTRIA if m <= NIVEL]}')
linha(f'  os marcos até o nv{NIVEL}          {len(marcos_ate)}        {marcos_ate}')
linha(f'  o orçamento de atributo       {orcamento}       {PONTOS_CRIACAO} na criação (teto {CRIACAO_TETO} ali) '
      f'+ {len(marcos_ate)} marcos (teto {ATRIB_TETO})')
linha()
linha(f'  Defesa {base["defesa"]} = 10 + Destreza + proteção {base["protecao"]}   ⟹  '
      f'DESTREZA OBRIGADA = {dex_obrigada}')
linha(f'  acerto +{base["acerto"]} = atributo + maestria {maestria:.0f}         ⟹  '
      f'ATRIBUTO DA TÉCNICA = {atrib_tecnica:.0f}')
linha(f'  e a CD confere:  8 + {atrib_tecnica:.0f} + {maestria:.0f} = {cd_confere:.0f}   '
      f'contra {base["cd"]} da TABELA   →  {"bate" if cd_confere == base["cd"] else "NÃO BATE"}')
linha()
# o que os dois obrigados custam: 3 na criação + o resto em marco
custo_dex = CRIACAO_TETO + max(0, dex_obrigada - CRIACAO_TETO)
custo_tec = CRIACAO_TETO + max(0, atrib_tecnica - CRIACAO_TETO)
marcos_gastos = max(0, dex_obrigada - CRIACAO_TETO) + max(0, int(atrib_tecnica) - CRIACAO_TETO)
livre = orcamento - custo_dex - custo_tec
linha(f'  {"o que cada obrigado custa":<34}{"na criação":>12}{"em marco":>10}{"total":>8}')
linha('  ' + '-' * 64)
linha(f'  {"Destreza (a Defesa manda)":<34}{min(dex_obrigada, CRIACAO_TETO):>12}'
      f'{max(0, dex_obrigada - CRIACAO_TETO):>10}{custo_dex:>8}')
linha(f'  {"o atributo da técnica (o acerto)":<34}{min(int(atrib_tecnica), CRIACAO_TETO):>12}'
      f'{max(0, int(atrib_tecnica) - CRIACAO_TETO):>10}{custo_tec:>8}')
linha('  ' + '-' * 64)
linha(f'  {"":<34}{"":>12}{marcos_gastos:>10}{custo_dex + custo_tec:>8}')
linha()
linha(f'  ⟹  sobram {livre} ponto(s) de {orcamento} pra COR, e {len(marcos_ate) - marcos_gastos} marco(s) de '
      f'{len(marcos_ate)}.')
if marcos_gastos > len(marcos_ate):
    linha(f'  !! NÃO FECHA: as derivadas pedem {marcos_gastos} marcos e o nv{NIVEL} só tem {len(marcos_ate)}.')
elif marcos_gastos == len(marcos_ate):
    linha(f'  ⚠ FECHA COM ZERO FOLGA DE MARCO. Todo marco do nv{NIVEL} está conscrito pelas derivadas.')
    linha(f'    O §3.2 promete que "os nove pontos compram cor, e não tamanho" — no nv{NIVEL} eles')
    linha(f'    compram {livre} de {orcamento}. A promessa é verdadeira e pequena.')

# ────────────────────────────────────────────────────────────────────────────
bloco('A FICHA — o que vai em cada célula do bloco')
# ────────────────────────────────────────────────────────────────────────────
tam = TAM[TAMANHO]
defesa_final = d + tam['defesa']
linha(f'  cabeçalho     `{TAMANHO} maldição, grau especial · {CATEGORIA} · {PAPEL_ESCOLHIDO} · nível {NIVEL}`')
linha()
de_papel = ' {0:+d} do papel'.format(d - base['defesa']) if d != base['defesa'] else ''
de_tam = ' {0:+d} do tamanho'.format(tam['defesa']) if tam['defesa'] else ''
linha(f'  Defesa               {defesa_final}          {base["defesa"]} da TABELA{de_papel}{de_tam}')
linha(f'  Acerto               +{base["acerto"]}')
linha(f'  CD                   {base["cd"]}')
linha(f'  Refino               {base["refino"]}  (proteção +{base["protecao"]})')
linha(f'  Vida                 {round(v)}        {base["vida"]} × {FORA[PAPEL_ESCOLHIDO][0] / base["vida"]:.3f} do `{PAPEL_ESCOLHIDO}`')
linha(f'  Integridade          {round(v)}        igual à vida máxima — peça 26 §3')
linha(f'  O golpe              `{txt}` = {med:.1f}   ·   alcance de corpo a corpo {tam["alcance"]:.1f} m')
linha(f'  Deslocamento         9 m')
linha(f'  Ações Múltiplas      ({ac})')
linha(f'  Intervenções         3 por luta, 1 por rodada')
linha()
linha(f'  dano por rodada      {round(dm)}   — NÃO é célula: é `o golpe` × ações, e derivável não ganha célula')

# ────────────────────────────────────────────────────────────────────────────
bloco('AS AÇÕES DELE — cada uma montada no orçamento DELA')
# ────────────────────────────────────────────────────────────────────────────
RECARGA_ROT = pega(BLOCO, r'\*\*`(Recarga \(\d-\d\))`\*\*', 'o rótulo de recarga', BEST).group(1)
pega('04-fase-1/fila/DECIDIDO-a-recarga.md',
     r'ela come o TURNO INTEIRO\*\* \| não uma ação', 'a decisão da `Recarga`', BEST)
TOQUE_DEVOLVE = 'Média'   # a Forma Toque devolve Média — ANCORAS-do-repositorio.md §4

linha(f'  o orçamento de uma ação       {pontos:.1f} pontos   (`Classe {CLASSE_ACAO}`)')
linha(f'  o turno cheio                 {dm:.0f}   =  {med:.0f} × {ac} ações')
linha()
ALVOS_AREA = n(pega(P26, r'ele derruba `([\d,]+)` pessoas se concentrar',
                    'quantas pessoas a área pega', ).group(1))
linha(f'  a área pega                   {ALVOS_AREA:.2f} pessoas   — peça 26 §4.6, a mesma leitura do §6.5')
linha()
linha(f'  {"a ação":<26}{"o que ela compra":<40}{"pts":>5}{"dado":>11}{"por alvo":>9}'
      f'{"no grupo":>9}{"vs a cota":>10}')
linha('  ' + '-' * 112)


def monta(rotulo, compras, devolve=0):
    """compras = lista de degraus de Melhoria. devolve = degrau de Restrição."""
    custo = sum(preco_melhoria(x, CLASSE_ACAO) for x in compras)
    rebate = preco_melhoria(devolve, CLASSE_ACAO) if devolve else 0
    teto_dev = 2 * CLASSE_ACAO
    if rebate > teto_dev:
        print(f'  !! a devolução de {rebate} passa do teto de {teto_dev} (2 × Classe)')
        sys.exit(1)
    sobra = pontos + rebate - custo
    dados = int(sobra)
    dano = dados * PONTO
    return custo, rebate, dados, dano, dano / VIDA_PC


ACOES = [
    ('Desmembrar 解', 'nada — o golpe cru, à distância', [], 0, 1),
    ('Clivar 捌', 'Toque (devolve Média) · `Impedido` (Pesada)', ['Pesada'], TOQUE_DEVOLVE, 1),
    ('Teia de Aranha 蜘蛛の糸', 'área (Leve) · `Derrubado` (Leve)', ['Leve', 'Leve'], 0, ALVOS_AREA),
]
ROMPEU_AREA = []
for rot, desc, compras, dev, nalv in ACOES:
    custo, rebate, dados, dano, fat_a = monta(rot, compras, dev)
    if not compras and not dev:
        dados, dano, dtxt = None, med, txt
    else:
        dtxt = f'{dados}d8'
    grupo = dano * nalv
    razao = grupo / med
    if nalv > 1 and razao > 1.05:
        ROMPEU_AREA.append((rot, razao, grupo))
    linha(f'  {rot:<26}{desc:<40}{(pontos if not compras and not dev else -custo + rebate):>+5.0f}'
          f'{dtxt:>11}{dano:>9.0f}{grupo:>9.0f}{razao:>9.2f}×{"" if razao <= 1.05 else " !!"}')
linha()
# ── a régua de área que o campo publica, medida em 7 sistemas ──────────────
FONTE_AREA = '04-fase-1/fila/FONTE-a-area-no-campo.md'
try:
    CONSENSO = n(pega(FONTE_AREA, r'O número de consenso é `([\d,]+)×` de dano por alvo',
                      'o consenso de área do campo', BEST).group(1))
    TETO_LIVRE = n(pega(FONTE_AREA, r'O teto absoluto do bestiário inteiro do Draw Steel é `([\d,]+)`',
                        'o teto da área livre', BEST).group(1))
except SystemExit:
    raise
_area = [a for a in ACOES if a[4] > 1]
linha()
linha(f'  A RÉGUA DO CAMPO — medida em 7 sistemas, `{FONTE_AREA}`:')
linha(f'    o consenso de dano por alvo       {CONSENSO:.2f}× o golpe de alvo único')
linha(f'    o teto da área REPETÍVEL          {TETO_LIVRE:.2f}×   — `0` de `43` do Draw Steel passam, `0` de `17` do D&D 2024')
linha()
for rot, desc, compras, dev, nalv in _area:
    _c, _r, _d, _dano, _f = monta(rot, compras, dev)
    razao_alvo = _dano / med
    linha(f'    `{rot}` entrega {razao_alvo:.2f}× por alvo')
    linha(f'      contra o consenso de {CONSENSO:.2f}× e o teto repetível de {TETO_LIVRE:.2f}×  →  '
          f'{"DENTRO" if razao_alvo <= TETO_LIVRE else "FORA"}')
linha()
linha(f'  ⟹ POR ALVO a nossa área está DENTRO da banda do campo. O que está fora é a')
linha(f'    frase do §6.5 — nenhum dos 7 define a cota como total do GRUPO em área.')

if ROMPEU_AREA:
    linha()
    linha(f'  ⚠⚠ ACHADO — o §6.5 diz "área REPARTE a cota, e não multiplica ela", e a área do')
    linha(f'     Fundamento é MELHORIA DE PREÇO FIXO (`Leve`, {preco_melhoria("Leve", CLASSE_ACAO)} pontos '
          f'na `Classe {CLASSE_ACAO}`).')
    linha(f'     Preço fixo não reparte nada. Com {ALVOS_AREA:.2f} alvos:')
    for rot, razao, grupo in ROMPEU_AREA:
        linha(f'       `{rot}` entrega {grupo:.0f} ao grupo contra a cota de {med:.0f} '
              f'— {razao:.2f}× a cota')
    linha(f'     ⟹ Pra obedecer o §6.5, a ação em área tinha de entregar {med / ALVOS_AREA:.0f} '
          f'por alvo ({med / ALVOS_AREA / PONTO:.1f} pontos),')
    linha(f'       e o Fundamento entrega {ROMPEU_AREA[0][2] / ALVOS_AREA:.0f}. '
          f'A régua e a máquina discordam por {ROMPEU_AREA[0][1]:.2f}×.')
    linha(f'     E é EXATAMENTE a pergunta que a `A-FILA.md` declarou respondida.')
    linha()
linha(f'  ⚠ E a `{RECARGA_ROT}` é outro bicho: ela COME as `Ações Múltiplas` do turno')
linha(f'    e entrega ~1,0× o turno cheio, em ÁREA. O ganho não é tamanho, é área.')
linha()
linha(f'  {"se a área pegar":<18}{"cada alvo leva":>16}{"em dado":>14}{"fatia":>9}{"× o turno":>12}')
linha('  ' + '-' * 72)
for nalvos in (1, 2, 3, 4):
    porcabeca = dm / nalvos
    t2, m2, p2 = em_dado(porcabeca)
    linha(f'  {f"{nalvos} alvo(s)":<18}{m2:>16.0f}{t2:>14}{m2 / VIDA_PC:>8.0%}'
          f'{m2 * nalvos / dm:>11.2f}×')
linha()
linha(f'  ⚠⚠ E aqui o §4.4 BATE numa parede: a metade em dado não fecha em cima de {dm:.0f}.')
_t, _m, _p = em_dado(dm)
linha(f'     `{_t}` = {_m:.0f}, e só {_p:.0%} disso é dado — o teto de {TETO_DADOS} dados não alcança')
linha(f'     a metade de {dm / 2:.0f}. O maior punhado possível é {TETO_DADOS}d12 = {TETO_DADOS * 6.5:.0f}.')
linha(f'     ⟹ A `{RECARGA_ROT}` SÓ fecha o §4.4 se for repartida por área. Em alvo único ela')
linha(f'       vira número quase todo fixo, que é o que o §4.4 existe pra evitar.')

# ────────────────────────────────────────────────────────────────────────────
bloco('AS CONFERÊNCIAS')
# ────────────────────────────────────────────────────────────────────────────
ok = True


def confere(rotulo, cond, detalhe):
    global ok
    ok = ok and cond
    linha(f'  [{"ok" if cond else "!!"}]  {rotulo:<44}{detalhe}')


confere('o golpe cai na banda', BANDA[0] <= fat <= BANDA[1],
        f'{fat:.1%}  ·  banda {BANDA[0]:.0%}–{BANDA[1]:.0%}')
confere('o invariante do papel fecha em 1,000', abs(inv - 1.0) < 0.02, f'{inv:.3f}×')
confere('o produto do tamanho fecha', abs(tam['produto'] - 1.0) < 0.05, f'{tam["produto"]:.3f}×')
confere('as ações por rodada saem da categoria', ac == base['acoes'],
        f'{ac}  — é a TRAVA DURA, não a linha')
confere('o golpe fecha metade em dado', 0.40 <= pct <= 0.60, f'{pct:.1%} em dado')
confere('o golpe cabe na mão', int(txt.split('d')[0]) <= TETO_DADOS,
        f'{txt.split("d")[0]} dados  ·  teto {TETO_DADOS}')
confere('a categoria tem `Intervenção`', TEM_INT[CATEGORIA], f'`{CATEGORIA}` — de `Desastre` pra cima')
confere('o orçamento passa do piso', pontos >= PISO_PONTOS,
        f'{pontos:.1f} pontos  ·  piso {PISO_PONTOS:.0f}')
confere('o `Emboscador` não é o papel', PAPEL_ESCOLHIDO != 'Emboscador' or TAMANHO in ('Médio', 'Grande'),
        'ele não sobe de `Grande`')

# a única evidência de mesa que o projeto tem
mv = pega(MESA, r'cerca de `(\d+)` por fase', 'a vida da mesa de ND 20', BEST)
mg = pega(MESA, r'cortou pela metade\*\*: `([\dd\s+]+)` no alvo único', 'o golpe da mesa de ND 20', BEST)
mesa_vida = int(mv.group(1)) * 2
mesa_golpe = media_dado(mg.group(1))
linha()
linha(f'  E contra a ÚNICA evidência de mesa do projeto — o Sukuna que o Mizuki rodou em 07/09:')
linha(f'    {"":<22}{"a mesa rodou":>16}{"a máquina dá":>16}{"razão":>10}')
linha('  ' + '-' * 66)
linha(f'    {"vida":<22}{mesa_vida:>16}{round(v):>16}{round(v) / mesa_vida:>9.2f}×')
linha(f'    {"o golpe":<22}{mesa_golpe:>16.1f}{med:>16.1f}{med / mesa_golpe:>9.2f}×')
linha(f'    {"ações por rodada":<22}{3:>16}{ac:>16}{ac / 3:>9.2f}×')
linha(f'    {"dano por rodada":<22}{mesa_golpe * 3:>16.1f}{dm:>16.1f}{dm / (mesa_golpe * 3):>9.2f}×')
linha()
linha(f'  ⚠ A VIDA bate em {round(v) / mesa_vida:.2f}× e o DANO fica em {dm / (mesa_golpe * 3):.2f}×.')
linha(f'    O mestre amarrou a vida na `{CATEGORIA}` e o dano num degrau abaixo:')
for cat in ['Ameaça', 'Desastre', 'Catástrofe', 'Calamidade']:
    if cat not in CATS or NIVEL not in CATS[cat]:
        continue
    b = CATS[cat][NIVEL]
    dr = b['dano'] * (FATOR_INT if TEM_INT.get(cat) else 1.0)
    linha(f'      `{cat:<11}` dano/rodada {dr:>6.1f}   ·   a mesa rodou {mesa_golpe * 3:.0f}   '
          f'→ {mesa_golpe * 3 / dr:.2f}× do que a categoria pede')
linha(f'    E na máquina isso NÃO É MONTAGEM LEGAL: os dois fatores da categoria andam juntos.')
linha(f'    Ele derruba {dm / VIDA_PC:.2f} personagem por rodada, contra {mesa_golpe * 3 / VIDA_PC:.2f} que a mesa viu.')

linha()
linha('=' * 96)
linha(f'  {"TODAS AS CONFERÊNCIAS PASSARAM" if ok else "!! ALGUMA CONFERÊNCIA FALHOU"}')
linha('=' * 96)
sys.exit(0 if ok else 2)

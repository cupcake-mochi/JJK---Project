#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Confere a FICHA de 05-material contra as pecas de 03-mecanica.

Por que ele existe
------------------
A ficha imprime catalogo: 23 pericias, os oficios, 5 Caminhos, 15 Trilhas, os
4 Testes de Resistencia, e as constantes do nivel 2. Cada um desses e' uma
COPIA de uma peca — e este projeto ja sabe o que acontece com copia sem dono:
a peca 8 passou sete versoes com a Defesa errada porque ninguem comparava.

Uma ficha e' pior que um documento nesse aspecto, porque ela e' o que vai para
a mao do jogador. Um erro aqui nao fica num .md que ninguem abre: ele vira
personagem, em sete mesas ao mesmo tempo.

Entao a regra e a mesma de sempre: um numero, um dono. O dono e' a peca; o
gerador-ficha/dados.js e' copia; e este validador falha quando os dois
discordam.

Seis checagens
--------------
  1. PERICIAS — as 23 da ficha sao as 23 da peca 7, com o mesmo atributo.
  2. OFICIOS — os da ficha sao os da peca 7 (a contagem sai da peca).
  3. CAMINHOS — nome, vida inicial, vida por nivel e PE por nivel batem com a
     peca 8, e as pericias fixas batem com a peca 7.
  4. TRILHAS — as 15 da ficha existem na peca 6, no Caminho certo.
  5. AS CONSTANTES DO NIVEL 2 — maestria, refino, protecao, Classe, feiticos
     conhecidos, Classe 0, Integridade, XP do proximo nivel e os pontos de
     atributo batem com as pecas donas.
  6. OS ARQUIVOS EXISTEM — o .docx gerado esta em 05-material, e o gerador
     tambem.

Roda de sistema/03-mecanica. Nao le o .docx e nao precisa de python-docx.
"""
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
MAT = os.path.join(AQUI, '..', '05-material')
GER = os.path.join(MAT, 'gerador-ficha')
FALHAS = []


def erro(msg):
    FALHAS.append(msg)
    print(f'  !! {msg}')


def bloco(t):
    print()
    print('=' * 88)
    print(t)
    print('=' * 88)


def ler(caminho, rotulo):
    try:
        with open(caminho, encoding='utf-8') as fh:
            return fh.read()
    except FileNotFoundError:
        erro(f'{rotulo} nao abriu ({caminho}). Se o ls mostra ele, e o mount — '
             f'reescreva e rode de novo')
        return ''


P6 = ler(os.path.join(AQUI, '06-caminhos-e-trilhas.md'), 'peca 6')
P7 = ler(os.path.join(AQUI, '07-pericias-e-oficios.md'), 'peca 7')
P8 = ler(os.path.join(AQUI, '08-criacao-de-personagem.md'), 'peca 8')

# v0.143: a peca 23 SS2.3 poe a linha do Bloquear como OBRIGACAO da ficha —
# e' ela que faz o `-11` nunca aparecer na mesa. Aqui mora a impressao; a
# matematica mora no conferir-bloquear.py.
_P23 = ler(os.path.join(AQUI, '23-bloquear.md'), 'peca 23')
_m = re.search(r'`(\d+d\d+)\s*\+\s*\(a sua Defesa\s*[−-]\s*(\d+)\)`', _P23)
if not _m:
    erro('nao achei a formula do Bloquear na peca 23 — sem ela nao da para conferir '
         'a linha da ficha')
    DADO_BLO, OFF_BLO = None, None
else:
    DADO_BLO, OFF_BLO = _m.group(1), int(_m.group(2))

P11 = ler(os.path.join(AQUI, '11-aptidoes-e-refino.md'), 'peca 11')
P12 = ler(os.path.join(AQUI, '12-experiencia-e-progressao.md'), 'peca 12')
DADOS = ler(os.path.join(GER, 'dados.js'), 'o dados.js do gerador da ficha')


def lista_js(nome):
    """le um array de strings simples do dados.js"""
    m = re.search(nome + r'\s*=\s*\[(.*?)\];', DADOS, re.S)
    if not m:
        return None
    return re.findall(r"'([^']+)'", m.group(1))


def const_js(nome):
    m = re.search(r'const ' + nome + r'\s*=\s*([^;]+);', DADOS)
    if not m:
        return None
    expr = m.group(1).strip()
    try:
        return int(expr)
    except ValueError:
        pass
    # expressoes simples usadas no dados.js. O ctx leva TODA constante inteira
    # do arquivo — antes ele levava quatro escritas a mao, e uma constante nova
    # que se apoiasse noutra devolvia None em silencio (v0.145).
    ctx = {k: int(x) for k, x in re.findall(r'const (\w+)\s*=\s*(\d+);', DADOS)}

    def val(tok):
        return int(tok) if tok.isdigit() else ctx.get(tok)
    e = expr.replace('Math.floor', '//INT//')
    try:
        if '//INT//' in e:
            m2 = re.match(r'//INT//\((\w+) / (\d+)\) \+ (\d+)', e)
            if m2:
                return ctx.get(m2.group(1), 0) // int(m2.group(2)) + int(m2.group(3))
            m2 = re.match(r'(\d+) \+ //INT//\((\w+) / (\d+)\)', e)
            if m2:
                return int(m2.group(1)) + ctx.get(m2.group(2), 0) // int(m2.group(3))
        m2 = re.match(r'(\d+) \* (\w+)', e)
        if m2:
            return int(m2.group(1)) * ctx.get(m2.group(2), 0)
        # `A + B * (NIVEL - 1)`, com A e B numero OU nome de outra constante
        m2 = re.match(r'(\w+) \+ (\w+) \* \((\w+) - (\d+)\)', e)
        if m2:
            a, b, nv = val(m2.group(1)), val(m2.group(2)), ctx.get(m2.group(3))
            if None not in (a, b, nv):
                return a + b * (nv - int(m2.group(4)))
    except Exception:
        return None
    return None


def const_js_simples(nome):
    m = re.search(r'const ' + nome + r'\s*=\s*(\d+);', DADOS)
    return int(m.group(1)) if m else None


# ==========================================================================
bloco('1. PERICIAS — as 23 da ficha sao as 23 da peca 7?')

# o quadro da peca 7: | **Atributo** | Pericia · Pericia | n |
peca_per = {}
for linha in P7.splitlines():
    m = re.match(r'\|\s*\*\*(\w+)\*\*\s*\|\s*(.+?)\s*\|\s*(\d+)\s*\|', linha)
    if m and m.group(2) != '—':
        peca_per[m.group(1)] = [p.strip().replace('**', '')
                                for p in m.group(2).split('·')]

# o dados.js: ['Atributo', ['Pericia', ...]]
ficha_per = {}
m = re.search(r'const PERICIAS\s*=\s*\[(.*?)\n\];', DADOS, re.S)
if not m:
    erro('nao achei o array PERICIAS no dados.js do gerador')
else:
    for bl in re.finditer(r"\['([^']+)',\s*\[(.*?)\]\]", m.group(1), re.S):
        ficha_per[bl.group(1)] = re.findall(r"'([^']+)'", bl.group(2))

if peca_per and ficha_per:
    total_peca = sum(len(v) for v in peca_per.values())
    total_ficha = sum(len(v) for v in ficha_per.values())
    print(f'  peca 7: {total_peca} pericias em {len(peca_per)} atributos')
    print(f'  ficha:  {total_ficha} pericias em {len(ficha_per)} atributos')
    if total_peca != total_ficha:
        erro(f'a peca 7 tem {total_peca} pericias e a ficha imprime {total_ficha}')
    for attr in sorted(set(peca_per) | set(ficha_per)):
        a, b = set(peca_per.get(attr, [])), set(ficha_per.get(attr, []))
        if a != b:
            if b - a:
                erro(f'{attr}: a ficha imprime {sorted(b - a)} e a peca 7 nao tem')
            if a - b:
                erro(f'{attr}: a peca 7 tem {sorted(a - b)} e a ficha nao imprime')
        else:
            print(f'    [x] {attr:<14} {len(a)} pericias, iguais')

# ==========================================================================
bloco('2. OFICIOS — os da ficha sao os da peca 7?')

peca_of = re.findall(r'^\*\*(\w+)\*\* — ', P7, re.M)
# v0.42: era '## 5. Os dez ofícios' literal, e mudar o titulo da peca 7
# quebrava este validador em vez de acusar o que mudou.
secao = re.search(r'## 5\. Os \w+ of[ií]cios(.*?)(?=\n## )', P7, re.S)
if secao:
    peca_of = re.findall(r'\*\*([^*]+)\*\* — ', secao.group(1))
ficha_of = lista_js('const OFICIOS')
if ficha_of is None:
    erro('nao achei OFICIOS no dados.js')
elif peca_of:
    print(f'  peca 7: {len(peca_of)} oficios · ficha: {len(ficha_of)}')
    a, b = set(peca_of), set(ficha_of)
    if a != b:
        if b - a:
            erro(f'a ficha imprime oficios que a peca 7 nao tem: {sorted(b - a)}')
        if a - b:
            erro(f'a peca 7 tem oficios que a ficha nao imprime: {sorted(a - b)}')
    else:
        print(f'    [x] os {len(a)} batem: {", ".join(sorted(a))}')
else:
    erro('nao consegui ler a lista de oficios da peca 7')

# ==========================================================================
bloco('3. CAMINHOS — vida, PE e pericias fixas')

# peca 8: | **Nome** | 12 (d12) | 7 | 4 | Pericia · Pericia |
# CINCO colunas desde a v0.105, quando o Caminho parou de travar oficio: a coluna
# de oficio fixo saiu da peca, e com ela saiu o que havia para comparar aqui.
peca_cam = {}
for linha in P8.splitlines():
    m = re.match(r'\|\s*\*\*(\w+)\*\*\s*\|\s*(\d+)\s*\((d\d+)\)\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|'
                 r'\s*([^|]+?)\s*\|', linha)
    if m:
        peca_cam[m.group(1)] = dict(vida1=int(m.group(2)), dado=m.group(3),
                                    vidaNv=int(m.group(4)), peNv=int(m.group(5)),
                                    pericias=[p.strip() for p in m.group(6).split('·')])

# cada entrada e um bloco { ... } dentro de const CAMINHOS. Le campo por campo,
# em vez de um regex unico com a formatacao inteira dentro: o dados.js alinha os
# valores com espacos, e um regex que depende disso quebra quando alguem realinha.
ficha_cam = {}
_blocoCam = re.search(r'const CAMINHOS\s*=\s*\[(.*?)\n\];', DADOS, re.S)
if _blocoCam:
    for bl in re.finditer(r'\{(.*?)\}', _blocoCam.group(1), re.S):
        b = bl.group(1)
        def _s(campo):
            mm = re.search(campo + r"\s*:\s*'([^']*)'", b)
            return mm.group(1) if mm else None
        def _i(campo):
            mm = re.search(campo + r'\s*:\s*(\d+)', b)
            return int(mm.group(1)) if mm else None
        def _l(campo):
            mm = re.search(campo + r'\s*:\s*\[([^\]]*)\]', b, re.S)
            return re.findall(r"'([^']+)'", mm.group(1)) if mm else []
        nome = _s('nome')
        if nome:
            ficha_cam[nome] = dict(dado=_s('dado'), vida1=_i('vida1'),
                                   vidaNv=_i('vidaNv'), peNv=_i('peNv'),
                                   pericias=_l('pericias'),
                                   trilhas=_l('trilhas'))

if not peca_cam:
    erro('nao consegui ler a tabela de Caminhos da peca 8')
elif not ficha_cam:
    erro('nao consegui ler os CAMINHOS do dados.js')
else:
    if set(peca_cam) != set(ficha_cam):
        erro(f'Caminhos diferentes — peca 8: {sorted(peca_cam)} · ficha: {sorted(ficha_cam)}')
    for nome in sorted(set(peca_cam) & set(ficha_cam)):
        p, f = peca_cam[nome], ficha_cam[nome]
        ok = True
        for k in ('vida1', 'vidaNv', 'peNv', 'dado'):
            if p[k] != f[k]:
                ok = False
                erro(f'{nome}: a peca 8 diz {k}={p[k]} e a ficha imprime {f[k]}')
        if set(p['pericias']) != set(f['pericias']):
            ok = False
            erro(f'{nome}: pericias fixas divergem — peca 8 {p["pericias"]} · ficha {f["pericias"]}')
        if ok:
            print(f'    [x] {nome:<11} vida {p["vida1"]}/{p["vidaNv"]} · PE {p["peNv"]} · '
                  f'{", ".join(p["pericias"])}')
    # a soma vida+PE, que e a trava do sabor-e-nao-degrau
    somas = {n: c['vidaNv'] + c['peNv'] for n, c in ficha_cam.items()}
    if max(somas.values()) - min(somas.values()) > 1:
        erro(f'a soma vida+PE por nivel abriu demais entre os Caminhos: {somas} — '
             f'ela deve ficar em 10 ou 11, senao a escolha vira degrau de poder')
    else:
        print(f'    [x] soma vida+PE por nivel: {sorted(set(somas.values()))} — '
              f'a troca continua sendo sabor')

# ==========================================================================
bloco('4. TRILHAS — as 15 da ficha existem na peca 6?')

total_tr = 0
for nome, c in sorted(ficha_cam.items()):
    faltando = [t for t in c['trilhas'] if not re.search(r'\|\s*\*\*' + re.escape(t) + r'\*\*\s*\|', P6)]
    total_tr += len(c['trilhas'])
    if faltando:
        erro(f'{nome}: Trilhas que a ficha imprime e a peca 6 nao tem: {faltando}')
    else:
        print(f'    [x] {nome:<11} {", ".join(c["trilhas"])}')
if total_tr:
    print(f'  {total_tr} Trilhas ao todo, tres por Caminho.')
if total_tr != 15:
    erro(f'esperava 15 Trilhas (3 x 5 Caminhos) e a ficha imprime {total_tr}')

# ==========================================================================
bloco('5. AS CONSTANTES DO NIVEL 2')

NIVEL = const_js_simples('NIVEL')
checagens = []

# maestria e refino, da peca 8
for nome_js, rx, rotulo in (
    ('MAESTRIA', r'Maestria\s*=\s*(\d+)', 'peca 8, passo 7'),
    ('REFINO', r'Refino\s*=\s*(\d+)', 'peca 8, passo 7'),
):
    m = re.search(rx, P8)
    checagens.append((nome_js, const_js_simples(nome_js),
                      int(m.group(1)) if m else None, rotulo))

# protecao, da peca 11 (a dona da formula)
m = re.search(r'a sua proteção é `1/3 do refino \+ (\d+)`', P11)
refino = const_js_simples('REFINO')
checagens.append(('PROTECAO', const_js('PROTECAO'),
                  (refino // 3 + int(m.group(1))) if (m and refino is not None) else None,
                  'peca 11, cobrir-se de energia'))

# feiticos conhecidos e Classe 0, da peca 8
m = re.search(r'\*\*(\w+) feitiços conhecidos\*\*', P8)
PALAVRA = {'dois': 2, 'três': 3, 'tres': 3, 'quatro': 4}
checagens.append(('CONHECIDOS', const_js('CONHECIDOS'),
                  PALAVRA.get(m.group(1).lower()) if m else None, 'peca 8, passo 5'))
checagens.append(('CLASSE_0', const_js_simples('CLASSE_0'),
                  2 if re.search(r'dois feitiços de \*\*Classe 0\*\*', P8) else None,
                  'peca 8, passo 5'))
checagens.append(('CLASSE', const_js_simples('CLASSE'),
                  1 if re.search(r'No nível 2 você tem \*\*Classe 1\*\*', P8) else None,
                  'peca 8, passo 5'))

# integridade, da peca 8
# O modificador impresso na ficha de exemplo tem de ser a SUBTRACAO refeita, e
# nao um numero que hoje calha de bater — licao no 9. Se a Defesa da Kaori mudar
# e o Bloquear nao mudar junto, isto acende.
_mk = ler(os.path.join(MAT, 'gerador-ficha', 'make.js'), 'make.js da ficha')
_d = re.search(r"defesa:\s*'(\d+)'", _mk)
_b = re.search(r"bloquear:\s*'(\d+d\d+)\s*\+\s*(\d+)'", _mk)
if not (_d and _b):
    erro('nao achei `defesa` e/ou `bloquear` nos numeros da ficha de exemplo do '
         'make.js — a linha do Bloquear e obrigacao da peca 23 SS2.3')
elif OFF_BLO is not None:
    _esperado = int(_d.group(1)) - OFF_BLO
    if _b.group(1) != DADO_BLO:
        erro(f'a ficha de exemplo imprime `{_b.group(1)}` e a peca 23 diz '
             f'`{DADO_BLO}`')
    elif int(_b.group(2)) != _esperado:
        erro(f'a ficha de exemplo imprime Bloquear +{_b.group(2)} e a Defesa dela e '
             f'{_d.group(1)}: {_d.group(1)} - {OFF_BLO} = {_esperado}. O modificador '
             f'do Bloquear e o da Defesa tem de ser a MESMA expressao (peca 23 SS4)')
    else:
        print(f'  [x] a linha do Bloquear da ficha de exemplo e derivada: '
              f'Defesa {_d.group(1)} - {OFF_BLO} = +{_esperado}')

# v0.145: a Integridade deixou de ser constante — ela leva Essencia (peca 24 SS2).
# O que o gerador guarda e' a BASE do nivel 2, e o passo 7 imprime `N + Essencia`.
m = re.search(r'Integridade\s*=\s*(\d+) \+ Essência', P8)
checagens.append(('INTEGRIDADE_NV', const_js('INTEGRIDADE_NV'),
                  int(m.group(1)) if m else None, 'peca 8, passo 7'))

# xp do proximo nivel, da peca 12
# v0.196: a ancora era a FAIXA ("2 a 4") e a contagem ("1 missao"), e as duas
# carregavam o valor da curva velha — entao ela sumiu no dia em que a curva mudou,
# que e' exatamente o dia em que ela precisava acender. Hoje o recorte e' pelo
# NIVEL: qualquer faixa que cubra o nivel 2 serve, e o custo sai da linha dela.
def _xp_do_nivel(txt, nivel):
    for m in re.finditer(r'^\| \*\*(\d+)(?: a (\d+))?\*\* \| (\d+) miss\w+ \| ([\d.]+) \|',
                         txt, re.M):
        ini, fim = int(m.group(1)), int(m.group(2) or m.group(1))
        if ini <= nivel <= fim:
            return int(m.group(4).replace('.', '')), int(m.group(3))
    return None, None

_xp2, _miss2 = _xp_do_nivel(P12, 2)
checagens.append(('XP_PROXIMO', const_js_simples('XP_PROXIMO'),
                  _xp2, 'peca 12, a faixa da curva que cobre o nivel 2'))

# pontos de atributo e teto, da peca 8
m = re.search(r'\*\*(\w+) pontos entre os cinco\. Nenhum acima de (\d+)\.\*\*', P8)
if m:
    checagens.append(('PONTOS_ATRIBUTO', const_js_simples('PONTOS_ATRIBUTO'),
                      PALAVRA.get(m.group(1).lower()) or
                      {'nove': 9, 'oito': 8, 'dez': 10}.get(m.group(1).lower()),
                      'peca 8, passo 4'))
    checagens.append(('TETO_ATRIBUTO', const_js_simples('TETO_ATRIBUTO'),
                      int(m.group(2)), 'peca 8, passo 4'))

print(f'  {"constante":<18}{"na ficha":>10}{"na peca":>10}   dono')
for nome, na_ficha, na_peca, dono in checagens:
    if na_peca is None:
        erro(f'{nome}: nao consegui ler o valor em {dono} — se o texto mudou de '
             f'forma, esta checagem parou de conferir')
        continue
    if na_ficha is None:
        erro(f'{nome}: nao consegui ler o valor no dados.js do gerador')
        continue
    bate = na_ficha == na_peca
    print(f'  {nome:<18}{na_ficha:>10}{na_peca:>10}   {dono}   {"" if bate else "<<< NAO BATE"}')
    if not bate:
        erro(f'{nome}: a ficha imprime {na_ficha} e {dono} diz {na_peca}')

# ==========================================================================
bloco('6. OS ARQUIVOS EXISTEM')

for rel, oque in (
    ('ficha-em-branco.docx', 'a ficha em branco'),
    ('ficha-exemplo-kaori.docx', 'o exemplo preenchido'),
    ('gerador-ficha/make.js', 'o gerador'),
    ('gerador-ficha/dados.js', 'os catalogos'),
    ('gerador-ficha/ficha.js', 'o layout das tres paginas'),
    ('gerador-ficha/helpers.js', 'os helpers'),
    ('gerador-ficha/COMO-USAR.txt', 'as instrucoes'),
):
    p = os.path.join(MAT, rel)
    ok = os.path.isfile(p)
    print(f'  {"[x]" if ok else "[ ]"} 05-material/{rel} — {oque}')
    if not ok:
        erro(f'05-material/{rel} nao existe, e a ficha depende dele')

# O .docx publicado tem que ter sido gerado do codigo ATUAL. A primeira versao
# desta checagem comparava mtime — e ela nao acendia na perturbacao, porque o
# mount carimba data de arquivo de um jeito que nao da para confiar. Checagem
# que nao pode acender e pior que checagem nenhuma (licao no 8), entao ela
# passou a ler o CONTEUDO.
#
# Um .docx e um zip com word/document.xml dentro, e zipfile e biblioteca padrao
# — nao ha dependencia para faltar, nem caminho por onde isto pule em silencio.
import zipfile

def texto_do_docx(caminho):
    with zipfile.ZipFile(caminho) as z:
        xml = z.read('word/document.xml').decode('utf-8', 'ignore')
    return re.sub(r'<[^>]+>', '', xml)

esperados = [
    (f'10 + Des + {const_js("PROTECAO")}', 'a formula da Defesa com a protecao atual'),
    (f"{const_js('INTEGRIDADE_NV')} + Essência",
     'a CONTA da Integridade, e nao um numero — ela depende da Essencia'),
    (str(const_js_simples('XP_PROXIMO')), 'o XP do proximo nivel'),
]
if DADO_BLO:
    esperados.append((f'{DADO_BLO} + (Defesa − {OFF_BLO})',
                      'a formula do Bloquear, na linha colada na Defesa'))
for arq in ('ficha-em-branco.docx', 'ficha-exemplo-kaori.docx'):
    p = os.path.join(MAT, arq)
    if not os.path.isfile(p):
        continue
    try:
        txt = texto_do_docx(p)
    except Exception as exc:
        erro(f'{arq} nao abriu como .docx ({exc}) — ele pode estar corrompido')
        continue
    faltando = [oque for alvo, oque in esperados if alvo and alvo not in txt]
    if faltando:
        erro(f'{arq} nao traz {faltando} — ele foi gerado de uma versao antiga do '
             f'codigo. Rode "node make.js" em gerador-ficha e copie para 05-material')
    else:
        print(f'  [x] {arq} foi gerado do codigo atual')

# ==========================================================================
print()
print('=' * 88)
print('7. O BLOCO DE INIMIGO — o material contra a peca 26')
print('=' * 88)
# v0.199. O `gerador-inimigo/dados.js` guarda a tabela de faixas, as quatro
# categorias e a regua de resistencia. NENHUM valor dali e autoridade — a
# autoridade e a peca 26 e a tabela `Inimigos` do manual. Esta checagem e quem
# compara os dois, no mesmo molde que as seis de cima fazem com a ficha.
import math as _math
import re as _re

_GER = os.path.join(MAT, 'gerador-inimigo', 'dados.js')
_P26 = os.path.join(AQUI, '26-bestiario.md')

if not os.path.isfile(_GER):
    erro('7: nao achei o gerador-inimigo/dados.js — o bloco de inimigo depende dele')
elif not os.path.isfile(_P26):
    erro('7: nao achei a peca 26, que e a dona do que o bloco imprime')
else:
    _js = open(_GER, encoding='utf-8').read()
    _md = open(_P26, encoding='utf-8').read()

    # 7a — as quatro categorias: nome, personagens e fator
    _cat_js = _re.findall(r"\['(\w+)',\s*(\d+),\s*([\d.]+)\]", _js)
    _cat_md = []
    _i = _md.find('| categoria | personagens | fator sobre a linha do manual | ações |')
    if _i >= 0:
        _bloco = _md[_i:]
        _bloco = _bloco[:_bloco.find('\n\n')] if '\n\n' in _bloco else _bloco
        for _l in _bloco.split('\n')[2:]:
            _c = [x.replace('*', '').replace('`', '').strip() for x in _l.split('|')[1:-1]]
            if len(_c) == 4 and _c[1].isdigit():
                _cat_md.append((_c[0], int(_c[1]),
                                float(_c[2].replace('×', '').replace(',', '.').strip())))
    if not _cat_md:
        erro('7: nao achei a tabela de categorias na peca 26 §4')
    elif len(_cat_js) != len(_cat_md):
        erro(f'7: o dados.js tem {len(_cat_js)} categoria(s) e a peca 26 publica '
             f'{len(_cat_md)}')
    else:
        _mau = [f'{a[0]}' for a, b in zip(_cat_js, _cat_md)
                if a[0] != b[0] or int(a[1]) != b[1] or abs(float(a[2]) - b[2]) > 1e-9]
        if _mau:
            erro('7: categoria(s) do dados.js que nao batem com a peca 26 §4: '
                 + ', '.join(_mau))
        else:
            print(f'  [x] as {len(_cat_md)} categorias do dados.js batem com a peca 26 §4')

    # 7b — as sete faixas do dados.js contra a tabela do §4.1 da peca.
    # ⚠ A comparacao e' contra a PECA e nao contra o .docx de proposito: quem
    # compara a peca com o manual e' a checagem 3 do conferir-bestiario.py, e
    # duplicar essa leitura aqui poria um segundo caminho entre o mesmo par de
    # documentos — e faria este validador precisar do python-docx, que ele nao
    # precisa hoje. Um elo por checagem.
    _fx = _re.findall(r"\['(\d+ a \d+)',\s*\d+,\s*\d+,\s*\d+,\s*(\d+),\s*(\d+),"
                      r"\s*(\d+),\s*(null|\d+),\s*(null|\d+)\]", _js)
    if len(_fx) != 7:
        erro(f'7: achei {len(_fx)} faixa(s) no dados.js e a tabela do manual tem sete')
    else:
        _por_cat = {}
        _i = _md.find('| categoria | nv 10 | nv 20 | nv 30 |')
        if _i >= 0:
            _b = _md[_i:]
            _b = _b[:_b.find('\n\n')] if '\n\n' in _b else _b
            for _l in _b.split('\n')[2:]:
                _c = [x.replace('*', '').replace('`', '').strip() for x in _l.split('|')[1:-1]]
                if len(_c) == 4:
                    _por_cat[_c[0]] = [tuple(int(x) for x in _re.findall(r'(\d+)', y))
                                       for y in _c[1:]]
        if not _por_cat:
            erro('7: nao achei a tabela do §4.1 da peca 26 — ela e o outro lado desta '
                 'comparacao')
        else:
            _alvo = {'2 a 4': None, '9 a 12': 0, '17 a 20': 1, '26 a 30': 2}
            _mau = []
            for _f in _fx:
                _k = _alvo.get(_f[0])
                if _k is None:
                    continue
                for _nome, _pes, _fat in [(c[0], int(c[1]), float(c[2])) for c in _cat_js]:
                    if _nome not in _por_cat:
                        _mau.append(f'{_nome} nao esta no §4.1')
                        continue
                    _v = _math.ceil(int(_f[2]) * _fat - 0.5)
                    _d = _math.ceil(int(_f[3]) * _fat - 0.5)
                    if (_v, _d) != _por_cat[_nome][_k]:
                        _mau.append(f'{_nome} na faixa {_f[0]}: dados.js da ({_v}, {_d}) '
                                    f'e o §4.1 publica {_por_cat[_nome][_k]}')
            if _mau:
                erro('7: ' + ' · '.join(_mau[:3]))
            else:
                print('  [x] as faixas do dados.js reproduzem a tabela do §4.1, celula '
                      'a celula, com o arredondamento meio para baixo')

    # 7c — o cambio, e a regra de arredondamento que os tres lugares seguem
    _mc = _re.search(r'const CAMBIO = (\d+)', _js)
    _mp = _re.search(r'vale (\w+) capangas', _md)
    _PT = {'um': 1, 'dois': 2, 'três': 3, 'quatro': 4, 'cinco': 5, 'seis': 6}
    if not _mc or not _mp:
        erro('7: nao achei o cambio no dados.js ou na peca 26 §5')
    elif int(_mc.group(1)) != _PT.get(_mp.group(1).lower()):
        erro(f'7: o dados.js diz cambio {_mc.group(1)} e a peca 26 §5 diz '
             f'"{_mp.group(1)}"')
    else:
        print(f'  [x] o cambio do dados.js e o da peca 26 §5 dizem o mesmo: '
              f'{_mc.group(1)}')

    # 7c-bis — a sub-categoria: a fracao sai do CAMBIO, e nao de escolha.
    _sub = _re.search(r'const SUBCATEGORIAS = \[(.*?)\];', _js, _re.S)
    _t45 = []
    _i45 = _md.find('| sub-categoria | o chefe fica com | capangas | cobra do grupo |')
    if _i45 >= 0:
        _b = _md[_i45:]
        _b = _b[:_b.find('\n\n')] if '\n\n' in _b else _b
        for _l in _b.split('\n')[2:]:
            _c = [x.replace('*', '').replace('`', '').strip() for x in _l.split('|')[1:-1]]
            if len(_c) == 4:
                _t45.append((_c[0], int(_c[1].rstrip('%')), 0 if _c[2] == '—' else int(_c[2])))
    if not _sub or not _t45:
        erro('7: nao achei a sub-categoria no dados.js ou a tabela do §4.5 da peca 26')
    else:
        _pares = _re.findall(r"\['([^']+)',\s*(\d+)\]", _sub.group(1))
        _mau = []
        if len(_pares) != len(_t45):
            _mau.append(f'o dados.js tem {len(_pares)} e a peca publica {len(_t45)}')
        for (_n1, _c1), (_n2, _frac, _c2) in zip(_pares, _t45):
            _esp = round((1 - int(_c1) / int(_mc.group(1))) * 100)
            if _n1 != _n2 or int(_c1) != _c2:
                _mau.append(f'{_n1} contra {_n2}')
            elif _esp != _frac:
                _mau.append(f'{_n1}: a peca publica {_frac}% e o cambio da {_esp}%')
        if _mau:
            erro('7: a sub-categoria nao fecha com o cambio: ' + ' · '.join(_mau[:3]))
        else:
            print(f'  [x] as {len(_t45)} sub-categorias saem do cambio — 1 menos '
                  'capangas sobre ele, e nao de escolha')

    # 7d — a regra do dado: o gerador tem de seguir o §4.4, e a peca tem de
    # publicar a tabela de exemplo que ela promete.
    _mk = open(os.path.join(MAT, 'gerador-inimigo', 'make.js'), encoding='utf-8').read()
    if 'Math.round(alvo / 9)' not in _mk:
        erro('7: o gerador parou de montar o golpe como `N d8 + fixo` com N saindo do '
             'alvo dividido por nove, e a peca 26 §4.4 e a dona dessa regra')
    elif 'N d8 + fixo' not in _md:
        erro('7: a peca 26 parou de publicar a regra do golpe em dado, e o gerador '
             'continua imprimindo dado — a folha teria regra que peca nenhuma tem')
    else:
        # v0.201: esta linha carregava o VALOR (`| `Ronda` | `18` |`) e por isso
        # sumiu no dia em que a tabela de inimigo mudou — que e' exatamente o dia
        # em que ela precisava acender. Hoje ela casa a FORMA da linha, e o valor
        # e' lido dela.
        _tab44 = re.findall(r'^\| `Ronda` \| `(\d+)` \| `(\d+)` \| `?([^|`]+)`? \|$',
                            _md, re.M)
        if not _tab44:
            erro('7: a tabela de exemplo do §4.4 mudou de forma')
        else:
            _r44, _a44, _g44 = _tab44[0]
            print(f'  [x] o golpe em dado segue a regra do §4.4, e a peca publica ela '
                  f'(`Ronda` {_r44} por rodada em {_a44} acao -> {_g44.strip()})')

    if 'Math.ceil(x - 0.5)' not in open(
            os.path.join(MAT, 'gerador-inimigo', 'make.js'), encoding='utf-8').read():
        erro('7: o gerador do bloco parou de arredondar meio para BAIXO, e a peca 26 '
             '§4.1 declara essa regra — vinte e duas das celulas caem em ,5, entao as duas '
             'convencoes divergem em nove delas')
    elif 'meio para BAIXO' not in _md:
        erro('7: a peca 26 parou de declarar a regra de arredondamento, e sem ela os '
             'tres lugares que calculam a escala divergem em silencio')
    else:
        print('  [x] a peca declara o arredondamento meio para baixo, e o gerador segue')


# ==========================================================================
print()
print('=' * 88)
if FALHAS:
    print(f'>>> {len(FALHAS)} PROBLEMA(S):')
    for e in FALHAS:
        print('   -', e)
    sys.exit(1)
print('>>> TUDO OK — a ficha imprime o mesmo catalogo que as pecas decidiram, e as')
print('    constantes do nivel 2 batem com os donos delas.')

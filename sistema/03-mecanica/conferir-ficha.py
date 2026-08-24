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
    # expressoes simples usadas no dados.js
    ctx = {}
    for k in ('NIVEL', 'MAESTRIA', 'REFINO', 'CLASSE'):
        v = const_js_simples(k)
        if v is not None:
            ctx[k] = v
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
        m2 = re.match(r'(\d+) \+ (\d+) \* \((\w+) - (\d+)\)', e)
        if m2:
            return int(m2.group(1)) + int(m2.group(2)) * (ctx.get(m2.group(3), 0) - int(m2.group(4)))
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

m = re.search(r'Integridade\s*=\s*(\d+)', P8)
checagens.append(('INTEGRIDADE', const_js('INTEGRIDADE'),
                  int(m.group(1)) if m else None, 'peca 8, passo 7'))

# xp do proximo nivel, da peca 12
m = re.search(r'\|\s*\*\*2 a 4\*\*\s*\|\s*1 missão\s*\|\s*(\d+)\s*\|', P12)
checagens.append(('XP_PROXIMO', const_js_simples('XP_PROXIMO'),
                  int(m.group(1)) if m else None, 'peca 12, faixa 2 a 4'))

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
    (str(const_js('INTEGRIDADE')), 'a Integridade do nivel 2'),
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
if FALHAS:
    print(f'>>> {len(FALHAS)} PROBLEMA(S):')
    for e in FALHAS:
        print('   -', e)
    sys.exit(1)
print('>>> TUDO OK — a ficha imprime o mesmo catalogo que as pecas decidiram, e as')
print('    constantes do nivel 2 batem com os donos delas.')

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

Dez checagens
-------------
  1. PERICIAS — as 23 da ficha sao as 23 da peca 7, com o mesmo atributo.
  2. OFICIOS — os da ficha sao os da peca 7 (a contagem sai da peca).
  3. CAMINHOS — nome, vida inicial, vida por nivel e PE por nivel batem com a
     peca 8, e as pericias fixas batem com a peca 7.
  4. TRILHAS — as 18 da ficha existem na peca 6, no Caminho certo.
  5. AS CONSTANTES DO NIVEL 2 — maestria, refino, protecao, Classe, feiticos
     conhecidos, Classe 0, Integridade, XP do proximo nivel e os pontos de
     atributo batem com as pecas donas.
  6. OS ARQUIVOS EXISTEM — o .docx gerado esta em 05-material, e o gerador
     tambem.
  7. O BLOCO DE INIMIGO — o gerador do bloco contra a peca 26.
  8. FAMILIAS — as da ficha sao as da tabela do manual, as da Kaori sao as da
     peca 8, e as duas fichas publicadas trazem as do manual.
  9. A TIRA DE REFERENCIA E AS NOTAS — o que a pagina 3 resume, e as notas da
     pagina 2, contra as pecas e o livro, e nenhuma mecanica morta.
  10. OS TESTES DE RESISTENCIA — o que a tabela e a nota dela somam no treinado,
      contra o termo da peca 1, no ficha.js e nas duas fichas publicadas.

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
bloco('4. TRILHAS — as 18 da ficha existem na peca 6?')

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
if total_tr != 3 * len(peca_cam):
    erro(f'esperava tres Trilhas por Caminho e a ficha imprime {total_tr}')

# ==========================================================================
# v0.331: tabelas do livro tambem devem mostrar os seis Caminhos.
_raiz331 = os.path.dirname(os.path.dirname(AQUI))
for _file331, _cols331 in [('10-como-jogar.md',5),('12-pericias-e-oficios.md',2)]:
    _path331 = os.path.join(_raiz331, 'sistema', '05-material', 'livro', 'manual', _file331)
    _txt331 = open(_path331, encoding='utf-8').read()
    _rows331 = {}
    for _line331 in _txt331.splitlines():
        _mat331 = re.match(r'^\| \*\*([^*]+)\*\* \| (.+)$', _line331)
        if _mat331 and _mat331[1] in peca_cam:
            _rows331[_mat331[1]] = [x.strip() for x in _mat331[2].strip('|').split('|')]
    if set(_rows331) != set(peca_cam):
        erro(f'{_file331}: tabela do livro omite Caminho atual')
    for _name331, _values331 in _rows331.items():
        _p331 = peca_cam[_name331]
        _expected331 = ([_p331['dado'],str(_p331['vida1']),str(_p331['vidaNv']),str(_p331['peNv'])]
                       if _cols331 == 5 else [' · '.join(_p331['pericias'])])
        if _values331 != _expected331:
            erro(f'{_file331}: {_name331} diverge da base mecanica')

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

    # v0.282: a GRADE da fase 2 do bestiario. O dados.js guarda os degraus (rodadas e
    # orcamento), as faixas do manual, os papeis e as constantes; a peca 26 e a dona de
    # todos, e esta checagem compara as copias com ela, celula a celula.
    def _n7(s):
        return float(str(s).replace(',', '.'))

    def _tab7(cab):
        _i7 = _md.find(cab)
        if _i7 < 0:
            return []
        _b7 = _md[_i7:]
        _b7 = _b7[:_b7.find('\n\n')] if '\n\n' in _b7 else _b7
        return [[x.replace('*', '').replace('`', '').strip() for x in _l.split('|')[1:-1]]
                for _l in _b7.split('\n')[2:] if _l.startswith('|')]

    def _mbaixo(x):
        return _math.ceil(x - 0.5) if abs(x % 1 - 0.5) < 1e-9 else round(x)

    # 7a — os degraus: nome, rodadas e orcamento
    _bl_dg = _re.search(r'const DEGRAUS = \[(.*?)\];', _js, _re.S)
    _dg_js = [(n, float(r), float(o)) for n, r, o in _re.findall(
        r"\['([^']+)',\s*([\d.]+),\s*([\d.]+)\]", _bl_dg.group(1) if _bl_dg else '')]
    _dg_md = [(c[0], _n7(c[1]), _n7(c[2])) for c in
              _tab7('| categoria | rodadas | orçamento | pressão | o golpe, em % da vida de um personagem |') if len(c) >= 3]
    _nmax = _re.search(r'const N_MAXIMO = (\d+);', _js)
    _nmd = _re.search(r'de `×1` a `×(\d+)`', _md)
    if not _dg_md:
        erro('7a: nao achei a tabela dos degraus na peca 26 §4')
    elif _dg_js != _dg_md:
        erro(f'7a: os degraus do dados.js {_dg_js} nao sao os da peca 26 §4 {_dg_md}')
    elif not (_nmax and _nmd) or _nmax.group(1) != _nmd.group(1):
        erro('7a: o N maximo do dados.js nao e o da peca 26 §4')
    else:
        print(f'  [x] os {len(_dg_md)} degraus do dados.js sao os da peca 26 §4 — rodadas e orcamento —, de ×1 a ×{_nmax.group(1)}')
    _DG = {n: (r, o) for n, r, o in _dg_js}
    _RD = _DG.get('Desastre', (3, 1))[0]

    # 7b — as faixas: a coluna do Capanga e as tres tabelas do §4.1, celula a celula
    _fx = _re.findall(r"\['(\d+ a \d+)',\s*\d+,\s*\d+,\s*\d+,\s*(\d+),\s*(\d+),"
                      r"\s*(\d+),\s*(null|\d+),\s*(null|\d+)\]", _js)
    if len(_fx) != 7:
        erro(f'7b: achei {len(_fx)} faixa(s) no dados.js e a tabela do manual tem sete')
    else:
        _mau = []
        for _f in _fx:
            _s, _cd = int(_f[1]) / 4, int(_f[3])
            if (_f[4], _f[5]) == ('null', 'null') or (int(_f[4]), int(_f[5])) != (_math.floor(_s), _mbaixo(_cd / 8)):
                _mau.append(f'{_f[0]}: o capanga do dados.js e ({_f[4]}, {_f[5]}) e o da grade e ({_math.floor(_s)}, {_mbaixo(_cd / 8)})')
        _alvo = {'9 a 12': 10, '17 a 20': 20, '26 a 30': 30}
        for _f in _fx:
            _nv = _alvo.get(_f[0])
            if _nv is None:
                continue
            _k = _md.find(f'**Nível {_nv}**\n')
            _sub = _md[_k:] if _k >= 0 else ''
            _i41 = _sub.find('| categoria | `×1` |')
            _b41 = _sub[_i41:_sub.find('\n\n', _i41)] if _i41 >= 0 else ''
            _linhas = [[x.replace('`', '').strip() for x in _l.split('|')[1:-1]] for _l in _b41.split('\n')[2:] if _l.startswith('|')]
            if len(_linhas) != 5:
                _mau.append(f'nao achei a ficha pronta do nivel {_nv} no §4.1')
                continue
            _s, _cd = int(_f[1]) / 4, int(_f[3])
            for _l in _linhas:
                _nome = _l[0]
                if _nome not in _DG:
                    _mau.append(f'{_nome} nao e degrau do dados.js')
                    continue
                _r, _o = _DG[_nome]
                for _n, _cel in zip(range(1, 7), _l[1:7]):
                    _nums = [int(x) for x in _re.findall(r'\d+', _cel)]
                    if _nome == 'Capanga':
                        _e = [2 * _n, _math.floor(_s), _mbaixo(_cd / 8)]
                    else:
                        _e = [_mbaixo(_r * _n * _s), _mbaixo(_o * _RD / _r * _cd / 4)]
                    if _nums != _e:
                        _mau.append(f'{_nome} ×{_n} na faixa {_f[0]}: o dados.js da {_e} e o §4.1 publica {_nums}')
        if _mau:
            erro('7b: ' + ' · '.join(_mau[:3]))
        else:
            print('  [x] as sete faixas do dados.js tem o capanga da grade, e as tres que o §4.1 publica reproduzem as '
                  'noventa celulas')

    # 7c — os papeis contra a peca 26 §3.4
    _pap_js = _re.findall(r"\['([^']+)',\s*(null|[\d.]+),\s*([+-]?\d+),\s*(null|'[a-z]+')\]",
                          (_re.search(r'const PAPEIS = \[(.*?)\];', _js, _re.S).group(1)
                           if _re.search(r'const PAPEIS = \[(.*?)\];', _js, _re.S) else ''))
    _pap_md = _tab7('| papel | o que ganha | o que paga |')
    _mau_p = []
    if not _pap_js or len(_pap_js) != len(_pap_md):
        _mau_p.append(f'o dados.js tem {len(_pap_js)} papel(eis) e a peca 26 §3.4 publica {len(_pap_md)}')
    else:
        for (_nj, _vj, _dj_, _tj), _lm in zip(_pap_js, _pap_md):
            if _nj != _lm[0]:
                _mau_p.append(f'o dados.js diz `{_nj}` onde a peca diz `{_lm[0]}`')
                continue
            _cv = _re.search(r'vida crua × (\d+),(\d+)', _lm[1] + ' ' + _lm[2])
            _quer = float(f'{_cv.group(1)}.{_cv.group(2)}') if _cv else None
            if (_vj == 'null') != (_quer is None) or (_quer is not None and abs(float(_vj) - _quer) > 0.001):
                _mau_p.append(f'`{_nj}`: o dados.js diz vida {_vj} e a peca diz {_quer}')
            _mdf = _re.search(r'Defesa ([−+-])\s*(\d+)', _lm[1] + ' ' + _lm[2])
            _qd = int(_mdf.group(2)) * (-1 if _mdf.group(1) in '−-' else 1) if _mdf else 0
            if int(_dj_) != _qd:
                _mau_p.append(f'`{_nj}`: o dados.js move a Defesa em {_dj_} e a peca diz {_qd:+d}')
            _fonte = {'alcance': 'degrau', 'vantagem': 'N', 'acao': 'N'}.get(_tj.strip("'"), None) if _tj != 'null' else None
            if _fonte and _fonte not in _lm[1] + " " + _lm[2]:
                _mau_p.append(f'`{_nj}`: o dados.js tira o fator por {_tj} e a peca paga "{_lm[2]}"')
    for _rot, _rj, _rp in (('a vantagem', r'const MULT_VANTAGEM = ([\d.]+);', r'\(N − 1 \+ ([\d,]+)\) ÷ N'),
                           ('o alcance', r'const GANHO_ALCANCE = ([\d.]+);', r'`1 \+ ([\d,]+) ÷ rodadas`')):
        _a7, _b7 = _re.search(_rj, _js), _re.search(_rp, _md)
        if not (_a7 and _b7) or abs(_n7(_a7.group(1)) - _n7(_b7.group(1))) > 0.001:
            _mau_p.append(f'{_rot}: o dados.js e a formula do §3.4 nao batem')
    _fora_js = sorted(_re.findall(r"'([^']+)'", (_re.search(r'const PAPEIS_FORA_DO_CAPANGA = \[(.*?)\];', _js) or
                                                 _re.match('', '')).group(1) if _re.search(r'const PAPEIS_FORA_DO_CAPANGA = \[(.*?)\];', _js) else ''))
    _mf = _re.search(r'\*\*`(\w+)` e `(\w+)` ficam fora:\*\*', _md)
    if not _mf or _fora_js != sorted([_mf.group(1), _mf.group(2)]):
        _mau_p.append('quem o Capanga recusa nao bate entre o dados.js e o §3.4')
    if _mau_p:
        erro('7c: ' + ' · '.join(_mau_p[:4]))
    else:
        print(f'  [x] os {len(_pap_js)} papeis do dados.js batem com a peca 26 §3.4 — os fatores fixos, a Defesa, de onde sai '
              'o variavel, a vantagem, o alcance e quem o Capanga recusa')

    # 7c-ter — os numeros que o gerador COPIA, contra o dono
    _pc = open(os.path.join(os.path.dirname(os.path.dirname(AQUI)), 'manual', 'gerador', 'partC.js'), encoding='utf-8').read()
    _PT = {'um': 1, 'uma': 1, 'dois': 2, 'duas': 2, 'três': 3, 'quatro': 4, 'cinco': 5, 'seis': 6}
    _pares7 = (
        ('quantas Intervencoes por luta', r'const INTERVENCOES = (\d+)', _js, r'O inimigo com `Intervenção` carrega (\w+) por luta', _md,
         lambda s: int(s) if str(s).isdigit() else _PT.get(s, s)),
        ('a porta da Intervencao', r'const PORTA_INTERVENCAO = (\d+)', _js, r'Ela abre quando `N × orçamento ≥ (\d+)`', _md, _n7),
        ('a acao extra da Intervencao', r'const INTERVENCAO_EXTRA = ([\d.]+)', _js, r'`vida ÷ \(1 \+ ([\d,]+) ÷ \(rodadas × N\)\)`', _md, _n7),
        ('os corpos por pessoa do Capanga', r'const CORPOS_POR_PESSOA = (\d+)', _js, r'é um esquadrão de `(\d)N` corpos', _md, _n7),
        ('o cambio por pessoa', r'const CAMBIO_POR_PESSOA = (\d+)', _js, r'Um `Desastre ×N` vale `(\d)N` capangas', _md, _n7),
        ('o teto de empilhamento', r'const TETO_EMPILHAMENTO = (\d+)', _js, r'no máximo `(\d+)` corpos do mesmo esquadrão', _md, _n7),
        ('o deslocamento', r"const DESLOCAMENTO = '([^']+)'", _js, r'\| deslocamento \| `([^`]+)` \|', _md, str),
        ('o alcance do Projetil nas Classes 1 a 5', r"const ALCANCE_PROJETIL = '([^']+)'", _js,
         r"\['Projétil e Toque\*', '[^']+', '([^']+)'", _pc, str),
    )
    _mau7 = []
    for _rot, _rj, _tj, _rp, _tp, _cv in _pares7:
        _a, _b7 = _re.search(_rj, _tj), _re.search(_rp, _tp)
        if not (_a and _b7):
            _mau7.append(f'{_rot}: nao achei no dados.js ou no dono')
        elif _cv(_a.group(1)) != _cv(_b7.group(1)):
            _mau7.append(f'{_rot}: o dados.js diz {_a.group(1)} e o dono diz {_b7.group(1)}')
    _cc = _re.search(r'const CORPOS_CONTRA_UM = \[([\d.]+),\s*([\d.]+)\]', _js)
    _t43 = [_n7(x) for c in _tab7('| categoria | `×2` | `×4` | `×6` |') for x in c[1:4]]
    if not (_cc and _t43) or (float(_cc.group(1)), float(_cc.group(2))) != (min(_t43), max(_t43)):
        _mau7.append('a faixa de N corpos de ×1 contra um ×N nao bate com a tabela do §4.3')
    _rs = _re.findall(r"\['([^']+)',\s*'(\d+%)',\s*'([\d,]+×)',\s*'([\d,]+×)',\s*'([\d,]+×)'\]",
                      (_re.search(r'const RESISTENCIA = \[(.*?)\];', _js, _re.S) or _re.match('', '')).group(1)
                      if _re.search(r'const RESISTENCIA = \[(.*?)\];', _js, _re.S) else '')
    _rsm = [tuple(c[:5]) for c in _tab7('| grupo | peso | resistência | imunidade | vulnerabilidade |')]
    if not _rs or [tuple(x) for x in _rs] != _rsm:
        _mau7.append('a regua de resistencia do dados.js nao e a do §6.3')
    _tb = _re.search(r'const TAMANHOS = \[(.*?)\];', _js, _re.S)
    _tam_js = {n: (int(l), v == 'true') for n, l, v in _re.findall(r"\['([^']+)',\s*(\d+),\s*(true|false)\]", _tb.group(1) if _tb else '')}
    _tam_md = {}
    for _c in _tab7('| tamanho | ocupa na grade | alcance | o golpe pega |'):
        _lado = _re.search(r'(\d+)×', _c[1])
        for _nm in [x.strip() for x in _c[0].split('·')]:
            _tam_md[_nm] = (int(_lado.group(1)) if _lado else 0, 'metade' in _c[3])
    if not _tam_js or _tam_js != _tam_md:
        _mau7.append(f'o tamanho do dados.js {_tam_js} nao e o do §3.3 da peca 26 {_tam_md}')
    _ab = _re.search(r'const AREA_NATURAL = \[(.*?)\n\];', _js, _re.S)
    _area_js = [(int(a), int(b), int(q), r, c, [x.strip().strip("'") for x in rt.split(',')])
                for a, b, q, r, c, rt in _re.findall(r"\[\s*(\d+),\s*(\d+),\s*(\d+),\s*'([^']+)',\s*'([^']+)',\s*\[([^\]]*)\]\]",
                                                     _ab.group(1) if _ab else '')]
    _area_md = []
    for _c in _tab7('| nível | cobre | `Esfera` | `Cone` |'):
        if len(_c) == 5:
            _nv = [int(x) for x in _re.findall(r'\d+', _c[0])]
            _area_md.append((_nv[0], _nv[-1], int(_re.match(r'(\d+)', _c[1]).group(1)), _c[2].replace('raio ', ''), _c[3],
                             [x.strip() for x in _c[4].split('·')]))
    if not _area_js or _area_js != _area_md:
        _mau7.append('a area natural do dados.js nao e a do §6.5 da peca 26')
    if _mau7:
        erro('7: ' + ' · '.join(_mau7[:4]))
    else:
        print('  [x] as Intervencoes (tres, a porta, a acao extra), o esquadrao, o cambio, o teto de empilhamento, o '
              'deslocamento, o alcance do Projetil, o §4.3, a resistencia, o tamanho e a area natural batem com os donos')

    # 7d — a regra do dado e as guardas do make.js
    # v0.282: a conta mora no conta.js, e o make.js monta o .docx em cima dela; as guardas leem os dois
    _mk = (open(os.path.join(MAT, 'gerador-inimigo', 'conta.js'), encoding='utf-8').read() + '\n'
           + open(os.path.join(MAT, 'gerador-inimigo', 'make.js'), encoding='utf-8').read())
    _dg = re.findall(r'\d+', (re.search(r'const DADOS = \[([^\]]+)\]', _mk) or
                              type('', (), {'group': lambda s, n: ''})()).group(1))
    _mr = re.search(r'O tamanho do dado se escolhe entre ([^*]+?)\s*—', _md)
    _dp = re.findall(r'`d(\d+)`', _mr.group(1)) if _mr else []
    _teto_g = re.search(r'if \(n > (\d+)\) continue', _mk)
    _teto_p = re.search(r'no máximo \*\*(\w+)\*\* dados', _md)
    _PALNUM = {'quatro': 4, 'cinco': 5, 'seis': 6, 'sete': 7, 'oito': 8, 'nove': 9, 'dez': 10}
    _tab44 = re.findall(r'^\| `Desastre` \| `(\d+)` \| `([^`]+)` \|$', _md, re.M)
    if not _dg or not _dp or _dg != _dp:
        erro(f'7d: o gerador escolhe entre d{_dg} e a peca 26 §4.4 escreve d{_dp}')
    elif not (_teto_g and _teto_p and int(_teto_g.group(1)) == _PALNUM.get(_teto_p.group(1).lower())):
        erro('7d: o teto de dados na mao nao bate entre o gerador e a peca 26 §4.4')
    elif not _tab44:
        erro('7d: a tabela do dado do §4.4 mudou de forma')
    else:
        print(f'  [x] o golpe em dado segue a regra do §4.4 (o `Desastre` do nivel 30: {_tab44[0][0]} -> {_tab44[0][1]})')
    _faltam = [g for g in ('X.DEGRAUS', 'temIntervencao', 'vidaCel', 'X.CAMBIO_POR_PESSOA', 'X.CORPOS_POR_PESSOA') if g not in _mk]
    if _faltam:
        erro(f'7d: o conta.js e o make.js pararam de ler a grade do dados.js ({_faltam}) — se voltarem a guardar numero inline, '
             'ninguem compara com a peca de novo')
    elif re.search(r'FATOR_INTERVENCAO|SUBCATEGORIAS|X\.CATEGORIAS', _mk):
        erro('7d: o make.js voltou a ler a escada (o fator da Intervencao, a sub-categoria ou as categorias de antes)')
    else:
        print('  [x] o conta.js e o make.js leem os degraus, a porta da Intervencao, a vida da celula, o cambio e o esquadrao do dados.js')
    if 'Math.ceil(x - 0.5)' not in _mk or 'meio para BAIXO' not in _md:
        erro('7d: o gerador ou a peca 26 pararam de arredondar meio para BAIXO')
    else:
        print('  [x] a peca declara o arredondamento meio para baixo, e o gerador segue')

# ==========================================================================
print()
print('=' * 88)
print('8. FAMILIAS — as da ficha sao as do manual, e as da Kaori sao as da peca 8')
print('=' * 88)
# v0.239, o B4 do repositorio da ficha. A ficha imprimia `Ataque`, `Corpo`,
# `Movimento` e `Percepção`, que o manual nao tem, e nao imprimia `Alcance`,
# `Mira`, `Tempo` e `Marca`, que juntas sao boa parte das Melhorias. Passou
# porque as checagens de cima cobrem pericia, oficio, Caminho, Trilha e
# constante, e a lista de Familias era a unica copia da ficha sem dono.
#
# O DONO e' a tabela `Famílias` do gerador do manual do Fundamento: nenhuma peca
# de 03-mecanica declara a lista. Se uma passar a declarar, a fonte muda para ela.
# Nenhum nome de Familia e nenhuma contagem estao escritos aqui.
_EXT8 = {'sete': 7, 'oito': 8, 'nove': 9, 'dez': 10, 'onze': 11, 'doze': 12,
         'duas': 2, 'dois': 2, 'três': 3, 'tres': 3}
_PARTB = ler(os.path.join(AQUI, '..', '..', 'manual', 'gerador', 'partB.js'),
             'o partB.js do gerador do manual') or ''
_mfam = re.search(r"H2\('Famílias'\).*?TBL\(\[[^\]]*\],\s*\[(.*?)\n\s*\],", _PARTB, re.S)
_mqtd = re.search(r"divididas em (\w+) Famílias", _PARTB)
_fam_ficha = lista_js('FAMILIAS')
if not _mfam or not _mqtd:
    erro('8: nao achei a tabela de Familias no partB.js, ou a frase que diz quantas '
         'sao — se o gerador do manual mudou de forma, esta checagem parou de conferir')
elif _fam_ficha is None:
    erro('8: nao achei FAMILIAS no dados.js da ficha')
else:
    _fam_manual = re.findall(r"\['([^']+)',", _mfam.group(1))
    _qtd = _EXT8.get(_mqtd.group(1).lower())
    if _qtd is None or len(_fam_manual) != _qtd:
        erro(f'8: li {len(_fam_manual)} Familias na tabela do partB.js, e a frase dele diz '
             f'"{_mqtd.group(1)}" — a leitura esta errada, conserte ela antes de confiar')
    else:
        _sobra = [f for f in _fam_ficha if f not in _fam_manual]
        _falta = [f for f in _fam_manual if f not in _fam_ficha]
        if _sobra:
            erro(f'8: a ficha imprime Familia que o manual nao tem: {_sobra}. Nenhuma '
                 f'Melhoria pertence a ela, e o jogador marca um quadrado vazio')
        if _falta:
            erro(f'8: a ficha nao imprime Familia que o manual tem: {_falta}. O jogador '
                 f'nao tem onde marcar ela como Livre ou Fechada')
        if len(set(_fam_ficha)) != len(_fam_ficha):
            erro(f'8: a ficha imprime Familia repetida: {_fam_ficha}')
        if not _sobra and not _falta and len(set(_fam_ficha)) == len(_fam_ficha):
            print(f'  [x] as {len(_fam_manual)} Familias da ficha sao as {len(_fam_manual)} '
                  f'da tabela do manual')

        # a Kaori: as dela no make.js tem de existir, e tem de ser as da peca 8
        _MAKE = ler(os.path.join(GER, 'make.js'), 'o make.js do gerador da ficha') or ''
        _FJS = ler(os.path.join(GER, 'ficha.js'), 'o ficha.js do gerador da ficha') or ''
        _P08 = ler(os.path.join(AQUI, '08-criacao-de-personagem.md'), 'a peca 8') or ''
        _mk = re.search(r"livres: \[([^\]]*)\],\s*fechadas: \[([^\]]*)\]", _MAKE)
        _mp = re.search(r"\*Famílias Livres:\* ([^.]+)\. \*Fechadas:\* ([^—]+?) —", _P08)
        _mf = re.search(r"Famílias — (\w+) Livres, (\w+) Fechadas", _FJS)

        def _nomes(s):
            return [x.strip().strip("'") for x in re.split(r',| e ', s) if x.strip()]
        if not _mk or not _mp or not _mf:
            erro('8: nao achei as Familias da Kaori no make.js, a frase dela na peca 8, '
                 'ou o rotulo de quantas Livres e Fechadas no ficha.js')
        else:
            _kl, _kf = _nomes(_mk.group(1)), _nomes(_mk.group(2))
            _pl, _pf = _nomes(_mp.group(1)), _nomes(_mp.group(2))
            _ql, _qf = _EXT8.get(_mf.group(1)), _EXT8.get(_mf.group(2))
            _mau8 = []
            _fora = [f for f in _kl + _kf if f not in _fam_manual]
            if _fora:
                _mau8.append(f'a Kaori marca Familia que o manual nao tem: {_fora}')
            if (sorted(_kl), sorted(_kf)) != (sorted(_pl), sorted(_pf)):
                _mau8.append(f'o make.js da {_kl} Livres e {_kf} Fechadas, e a peca 8 diz '
                             f'{_pl} e {_pf}')
            if (len(_kl), len(_kf)) != (_ql, _qf):
                _mau8.append(f'a Kaori tem {len(_kl)} Livres e {len(_kf)} Fechadas, e a ficha '
                             f'imprime "{_mf.group(1)} Livres, {_mf.group(2)} Fechadas"')
            for _r in _mau8:
                erro(f'8: {_r}')
            if not _mau8:
                print(f'  [x] as {len(_kl)} Livres e as {len(_kf)} Fechadas da Kaori existem no '
                      f'manual e sao as da peca 8')

        # e os dois .docx publicados tem de trazer as Familias do manual
        for _arq8 in ('ficha-em-branco.docx', 'ficha-exemplo-kaori.docx'):
            _p8 = os.path.join(MAT, _arq8)
            if not os.path.isfile(_p8):
                continue
            try:
                _tx8 = texto_do_docx(_p8)
            except Exception as _exc8:
                erro(f'8: {_arq8} nao abriu como .docx ({_exc8})')
                continue
            _sem8 = [f for f in _fam_manual if f not in _tx8]
            if _sem8:
                erro(f'8: {_arq8} nao traz {_sem8} — ele foi gerado de uma versao antiga do '
                     f'dados.js. Rode "node make.js" em gerador-ficha e copie para 05-material')
            else:
                print(f'  [x] {_arq8} traz as {len(_fam_manual)} Familias do manual')

# ==========================================================================
print()
print('=' * 88)
print('9. A TIRA DE REFERENCIA E AS NOTAS — o que a ficha resume bate com o dono')
print('=' * 88)
# v0.239. A tira de referencia da pagina 3 dizia "canalizado = os dados da Classe e nada
# mais", mecanica que a peca 5 declara morta desde a v0.81; mandava o jogador para a
# quick-start, abandonada na v0.102; e dava os 25% do descanso curto "em ambiente
# propicio", quando eles valem em qualquer lugar. A nota do pacto dizia que pacto entre
# personagens nao tinha regra. Nenhum validador lia a tira nem as notas, porque o que elas
# resumem mora em outro documento. Cada linha aqui le o dono e cobra a copia.
_FJ9 = ler(os.path.join(GER, 'ficha.js'), 'o ficha.js do gerador da ficha') or ''
_LV9 = os.path.join(AQUI, '..', '05-material', 'livro')
_P01 = ler(os.path.join(AQUI, '01-atributos-acerto-defesa.md'), 'peca 1') or ''
_P03 = ler(os.path.join(AQUI, '03-economia-de-acao-e-iniciativa.md'), 'peca 3') or ''
_P05 = ler(os.path.join(AQUI, '05-caminho-e-combate-sem-feitico.md'), 'peca 5') or ''
_P10 = ler(os.path.join(AQUI, '10-descanso-e-recuperacao.md'), 'peca 10') or ''
_RLV = ler(os.path.join(_LV9, 'README.md'), 'o README do livro') or ''
_L20 = ler(os.path.join(_LV9, 'manual', '20-criacao-de-personagem.md'), 'o capitulo de criacao do livro') or ''
_L40 = ler(os.path.join(_LV9, 'manual', '40-fundamento.md'), 'o capitulo do Fundamento do livro') or ''
_L45 = ler(os.path.join(_LV9, 'manual', '45-aptidoes-e-refino.md'), 'o capitulo de aptidoes do livro') or ''
_mau9 = []

# as mortas: o dono declara a morte, e a ficha nao pode citar
for _rot, _morte, _dono, _termo in (
        ('o golpe canalizado', 'golpe canalizado" nunca existiu', _P05, 'canaliz'),
        ('a quick-start', 'quick-start abandonado', _RLV, 'quick-start')):
    if _morte not in _dono:
        _mau9.append(f'o dono parou de declarar a morte d{_rot[0]} {_rot[2:]} — reveja se ela voltou')
    elif _termo in _FJ9.lower():
        _mau9.append(f'a ficha ainda cita {_rot}, que o dono declara morta')

# os numeros e as frases da tira e das notas, contra quem manda neles
_CONF9 = [
    ('o deslocamento do turno', r'Deslocamento base: (\d+) metros', _P03, r"movimento (\d+) m \+ ação padrão", _FJ9),
    ('o descanso curto', r'\| \*\*PE\*\* \| \*\*(\d+)% do seu máximo\*\* \|', _P10, r'curto devolve (\d+)% do PE máximo', _FJ9),
    ('o crítico', r'> \*\*(\d+) natural numa rolagem de acerto é crítico', _P01, r"\['Crítico', '(\d+) natural", _FJ9),
    ('a primeira Liberação Máxima', r'\| \*\*(\d+)\*\* \| A primeira Liberação Máxima\.', _L40, r'A Liberação Máxima chega no nível (\d+)', _FJ9),
    ('a Técnica Máxima', r'\| \*\*(\d+)\*\* \| Classe \d+\. Técnica Máxima\.', _L40, r'e a Técnica Máxima no (\d+)', _FJ9),
]
for _rot, _rxd, _dono, _rxf, _copia in _CONF9:
    _md, _mf = re.search(_rxd, _dono), re.search(_rxf, _copia)
    if not _md or not _mf:
        _mau9.append(f'{_rot}: nao achei {"o dono" if not _md else "a copia na ficha"}')
    elif _md.group(1) != _mf.group(1):
        _mau9.append(f'{_rot}: o dono diz {_md.group(1)} e a ficha diz {_mf.group(1)}')

_FRASES9 = [
    ('o descanso longo', '| **PE** | **cheio** | **metade do seu máximo** |', _P10,
     'longo devolve tudo em ambiente propício, e metade fora dele'),
    ('o arredondamento', 'Arredonde sempre para o lado que não te favorece', _P01,
     'sempre para o lado que não te favorece'),
    ('o pacto na criação', 'só o pacto de restrição entra na criação', _L20,
     'Na criação só entra o pacto de restrição'),
    ('a Classe 0', 'Cabe uma Melhoria `Leve` e uma Restrição `Leve` numa Classe 0', _L40,
     'Cabe uma Melhoria Leve e uma Restrição Leve'),
    # v0.246: a nota dizia que o escudo desligava a protecao, e o escudo soma desde a
    # v0.42 (peca 14). A frase errada estava nas duas fichas publicadas.
    ('o escudo na protecao', 'sem Traje e sem Revestimento, a sua proteção é `1/3 do refino + 1`. Escudo soma com ela.', _L45,
     'Escudo soma por cima'),
]
for _rot, _fd, _dono, _ff in _FRASES9:
    if _fd not in _dono:
        _mau9.append(f'{_rot}: o dono parou de dizer "{_fd}" — a nota da ficha precisa ser relida')
    elif _ff not in _FJ9:
        _mau9.append(f'{_rot}: a ficha nao diz mais "{_ff}", e o dono continua dizendo')

# e a ficha em branco publicada tem de ter sido gerada deste ficha.js
_pb9 = os.path.join(MAT, 'ficha-em-branco.docx')
if os.path.isfile(_pb9):
    try:
        _tx9 = texto_do_docx(_pb9)
        if 'canaliz' in _tx9 or 'curto devolve' not in _tx9 or 'Escudo soma por cima' not in _tx9:
            _mau9.append('ficha-em-branco.docx nao traz a tira de hoje — rode "node make.js" em '
                         'gerador-ficha e copie para 05-material')
    except Exception as _e9:
        _mau9.append(f'ficha-em-branco.docx nao abriu ({_e9})')

for _r in _mau9:
    erro('9: ' + _r)
if not _mau9:
    print(f'  [x] as {len(_CONF9)} contas e as {len(_FRASES9)} frases da tira e das notas batem com os donos,')
    print('      nenhuma mecanica morta aparece, e a ficha publicada e a deste ficha.js')

# ==========================================================================
print()
print('=' * 88)
print('10. OS TESTES DE RESISTENCIA — o treinado soma o que a peca 1 manda')
print('=' * 88)
# v0.240, o B14 do repositorio da ficha. A tabela de TRs imprimia `d20 + atr + 2` no
# treinado, e a peca 1 §4 soma a maestria desde a v0.117. Passou pelas nove de cima porque
# nenhuma lia a coluna `total` dessa tabela. O termo sai da formula da peca 1, e nao daqui.
_P01_10 = ler(os.path.join(AQUI, '01-atributos-acerto-defesa.md'), 'peca 1') or ''
_FJ10 = ler(os.path.join(GER, 'ficha.js'), 'o ficha.js do gerador da ficha') or ''
_mau10 = []
_mp10 = re.search(r'Teste de Resistência = d20 \+ atributo do TR \+ (\w+)\s+'
                  r'\(a (\w+) só entra se treinado\)', _P01_10)
_mf10 = re.search(r"trTreinados\.includes\(nome\) \? 'd20 \+ atr \+ ([^']+)' : 'd20 \+ atr'", _FJ10)
_mn10 = re.search(r"NOTA\('Treinado: `d20 \+ atributo \+ (\w+)`\. Sem treino: `d20 \+ atributo`\.'\)", _FJ10)
if not _mp10 or _mp10.group(1) != _mp10.group(2):
    _mau10.append('nao achei na peca 1 a formula do TR, com o termo que so entra se treinado')
elif not _mf10:
    _mau10.append('nao achei no ficha.js o que a tabela de TRs soma no treinado')
elif _mf10.group(1) != _mp10.group(1):
    _mau10.append(f'a ficha soma "{_mf10.group(1)}" no treinado, e a peca 1 soma "{_mp10.group(1)}"')
elif not _mn10 or _mn10.group(1) != _mp10.group(1):
    _mau10.append(f'a nota da tabela de TRs soma "{_mn10.group(1) if _mn10 else "?"}" no treinado, '
                  f'e a peca 1 soma "{_mp10.group(1)}"')
else:
    # a tabela da Kaori marca os treinados; a em branco nao marca nenhum, e a nota e o que diz a conta
    for _arq10, _alvo10 in (('ficha-exemplo-kaori.docx', f'd20 + atr + {_mp10.group(1)}'),
                            ('ficha-em-branco.docx', f'Treinado: d20 + atributo + {_mp10.group(1)}')):
        _p10 = os.path.join(MAT, _arq10)
        if not os.path.isfile(_p10):
            continue
        try:
            if _alvo10 not in texto_do_docx(_p10):
                _mau10.append(f'{_arq10} nao traz "{_alvo10}" — rode "node make.js" em gerador-ficha '
                              'e copie para 05-material')
        except Exception as _e10:
            _mau10.append(f'{_arq10} nao abriu ({_e10})')
for _r in _mau10:
    erro('10: ' + _r)
if not _mau10:
    print(f'  [x] o TR treinado soma a {_mp10.group(1)}, como na peca 1, na tabela, na nota e nas duas fichas')

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

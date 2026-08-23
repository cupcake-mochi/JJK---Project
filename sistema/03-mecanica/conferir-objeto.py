#!/usr/bin/env python3
"""conferir-objeto.py — o validador dono da peca 21, `Objeto amaldicoado`.

Ela e' peca de VOCABULARIO: nao cria numero, nao cria moeda e nao muda ficha
nenhuma. Um validador de peca assim confere coisa diferente das outras vinte —
a pergunta aqui nao e' "a formula deriva certo?", e sim "cada palavra tem UMA
dona, e ela e' a dona certa?".

NENHUM VALOR FICA ESCRITO AQUI DENTRO. A escada de grau sai da peca 16, as
Origens saem da peca 9, o Legado sai da peca 13 e a lista de pecas sai da pasta.

O par declarado desta peca sao as checagens 3 e 8, e elas medem por eixos
OPOSTOS. A 3 confere que esta peca NAO ESCREVE o que ja tem dono; a 8 confere
que ela E' A UNICA a escrever o que e' dela. Uma peca de vocabulario falha dos
dois lados — por repetir o que e' de outra, e por deixar o que ela criou sem
dono — e cada uma sozinha sai verde por motivo que a outra derrubaria.

Roda de 03-mecanica/, sem argumento. Sai com codigo 1 se algo quebrar.
Ele NAO le o .docx e NAO precisa de python-docx: nao existe jeito de ele sair
verde tendo pulado checagem por falta de biblioteca.
"""
import os
import re
import sys

MEC = os.path.dirname(os.path.abspath(__file__))
FALHAS = []


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


def celulas(linha):
    return [c.strip() for c in linha.strip().strip('|').split('|')]


def separador(linha):
    return set(linha.replace('|', '').strip()) <= set('-: ')


PECAS = sorted(f for f in os.listdir(MEC) if re.match(r'^\d\d-.*\.md$', f))
POR_NUM = {int(p[:2]): p for p in PECAS}

ALVO = '21-objeto-amaldicoado.md'
if ALVO not in PECAS:
    print(f'  !! SETUP: {ALVO} nao esta na pasta — nao ha o que conferir')
    sys.exit(1)

P21 = ler(ALVO)
P21_L = P21.split('\n')
_p13 = ler(POR_NUM[13])
_p16 = ler(POR_NUM[16])

print('=' * 88)
print('conferir-objeto.py — peca 21, Objeto amaldicoado')
print('=' * 88)
print(f'  pecas na pasta           : {len(PECAS)}')
print(f'  linhas da peca 21        : {len(P21_L)}')


bloco('1. A FAMILIA — as quatro estao declaradas, e cada uma nomeia a dona')

_fam = []
_dentro = False
for _l in P21_L:
    if re.match(r'^\|.*dona da regra', _l):
        _dentro = True
        continue
    if _dentro:
        if not _l.startswith('|'):
            break
        if separador(_l):
            continue
        _c = celulas(_l)
        if len(_c) == 3:
            _fam.append(_c)

FAMILIA_ESPERADA = 4
print(f'  linhas de familia lidas  : {len(_fam)}')
for _c in _fam:
    print(f'      {_c[0][:46]:<48} dona: {_c[2]}')

if len(_fam) != FAMILIA_ESPERADA:
    erro('1', f'a tabela da familia tem {len(_fam)} linha(s) e a peca fala de '
              f'{FAMILIA_ESPERADA} coisas — ou a tabela mudou de forma, ou uma '
              'das quatro sumiu')
else:
    _mudas = [_c[0] for _c in _fam if not _c[2].strip()]
    if _mudas:
        erro('1', f'{len(_mudas)} linha(s) da familia sem dona declarada: {_mudas}')
    else:
        print(f'  [x] as {len(_fam)} coisas da familia estao declaradas, e todas '
              'nomeiam uma dona.')


bloco('2. PONTEIRO DE DONA — toda peca nomeada como dona existe na pasta')

_apontadas, _quebradas = set(), []
for _c in _fam:
    for _m in re.finditer(r'pe[çc]a (\d+)', _c[2]):
        _n = int(_m.group(1))
        _apontadas.add(_n)
        if _n not in POR_NUM:
            _quebradas.append((_c[0], _n))

if not _apontadas and not any('esta peça' in _c[2] for _c in _fam):
    erro('2', 'nenhuma linha da familia aponta para peca nenhuma — o extrator '
              'da coluna de dona parou de extrair')
elif _quebradas:
    for _o, _n in _quebradas:
        erro('2', f'a familia diz que `{_o}` e da peca {_n}, e ela nao existe na pasta')
else:
    print(f'  [x] as {len(_apontadas)} pecas nomeadas como dona existem: '
          + ' · '.join(f'peca {n}' for n in sorted(_apontadas)))


bloco('3. ESCADA DE GRAU — ela e da peca 16, e NAO se republica aqui')

_p16 = ler(POR_NUM[16])
_RX_CLASSE = re.compile(r'Classe [123]\b')
_n16 = len(_RX_CLASSE.findall(_p16))
_n21 = len(_RX_CLASSE.findall(P21))

_PISO16 = 3
print(f'  `Classe N` na peca 16    : {_n16}   (piso {_PISO16})')
print(f'  `Classe N` na peca 21    : {_n21}   (tem de ser 0)')

if _n16 < _PISO16:
    erro('3', f'a peca 16 so publica {_n16} `Classe N` e o piso e {_PISO16} — a '
              'escada de grau saiu de la, e esta checagem parou de conferir')
elif _n21:
    erro('3', f'a peca 21 escreve `Classe N` {_n21} vez(es) — a escada de grau e '
              'da peca 16 §3, e a segunda copia e a licao no 9')
else:
    print('  [x] a peca 21 aponta para a escada da peca 16 sem republicar nenhum '
          'degrau dela.')


bloco('4. SEM NUMERO DE REGRA — peca de vocabulario nao preca nada')

_RX_NUM = [
    ('dado',      re.compile(r'\b\d*d(?:4|6|8|10|12|20|100)\b')),
    ('PE',        re.compile(r'\b\d+\s*(?:de\s+)?PE\b')),
    ('fatia',     re.compile(r'\b\d+[,.]\d+\s*fatia')),
    ('distancia', re.compile(r'\b\d+\s*m\b')),
]
# A testemunha do contra-teste e' a PASTA, e nao uma peca escolhida a dedo:
# nenhuma peca sozinha usa as quatro notacoes, entao exigir isso de uma so'
# fazia o arnes falhar por si mesmo em vez de medir o texto.
_TESTEMUNHA = [p for p in PECAS if p != ALVO]
_pt = '\n'.join(ler(p) for p in _TESTEMUNHA)

_achados, _cego = [], []
for _rot, _rx in _RX_NUM:
    _n = _rx.findall(P21)
    if _n:
        _achados.append((_rot, _n[:4]))
    if not _rx.search(_pt):
        _cego.append(_rot)

print(f'  testemunha do contra-teste: as outras {len(_TESTEMUNHA)} pecas da pasta')
if _cego:
    erro('4', 'os regex de ' + ', '.join(_cego) + ' nao acendem em peca nenhuma '
         'da pasta — eles quebraram, e a peca 21 esta passando por falta de '
         'medida e nao por estar limpa')
elif _achados:
    for _rot, _ex in _achados:
        erro('4', f'a peca 21 escreve numero de {_rot}: {_ex} — ela e peca de '
                  'vocabulario e nao pode precar')
else:
    print(f'  [x] a peca 21 nao escreve dado, PE, fatia nem distancia, e os '
          f'{len(_RX_NUM)} regex acendem na testemunha.')


bloco('5. CADAVER AMALDICOADO — os tres rotulos, declarados como a mesma coisa')

# ATENCAO ao que esta checagem mede. A primeira versao dela perguntava se cada
# rotulo APARECE na peca 21 — e os tres aparecem tambem na tabela da familia do
# §2, entao apagar a tabela do §2.1 inteira saia VERDE. Medir o marcador em vez
# do fenomeno, que e' a armadilha que este projeto ja pagou dez vezes.
# Hoje ela le a tabela do §2.1 pelo cabecalho e exige as tres LINHAS.
_DONOS5 = {
    'Corpo Amaldiçoado':   POR_NUM[9],
    'corpo amaldiçoado':   POR_NUM[15],
    'cadáver amaldiçoado': POR_NUM[16],
}
_rot5 = []
_dentro = False
for _l in P21_L:
    if re.match(r'^\|\s*onde\s*\|\s*como aparece\s*\|', _l):
        _dentro = True
        continue
    if _dentro:
        if not _l.startswith('|'):
            break
        if separador(_l):
            continue
        _c = celulas(_l)
        if len(_c) == 3:
            _rot5.append((_c[0], re.sub(r'[`*]', '', _c[1]).strip()))

print(f'  linhas do §2.1 lidas     : {len(_rot5)}  (tem de ser {len(_DONOS5)})')
for _onde, _rot in _rot5:
    print(f'      {_rot:<22} visto de: {_onde}')

if len(_rot5) != len(_DONOS5):
    erro('5', f'a tabela do §2.1 tem {len(_rot5)} linha(s) e os rotulos de cadaver '
              f'amaldicoado sao {len(_DONOS5)} — sem os tres JUNTOS numa tabela so, '
              'ninguem descobre que sao a mesma coisa')
else:
    _vistos5 = {r for _, r in _rot5}
    _faltam5 = [r for r in _DONOS5 if r not in _vistos5]
    if _faltam5:
        erro('5', f'o §2.1 nao declara {_faltam5} — declara {sorted(_vistos5)}')
    else:
        _orfaos5 = []
        for _rot, _dona in _DONOS5.items():
            _a, _b = _rot.lower().split()
            _txt = ler(_dona).lower()
            if not re.search(re.escape(_a[:-1]) + r'\w*\s+' + re.escape(_b[:-1]) + r'\w*',
                             _txt):
                _orfaos5.append(f'`{_rot}` nao aparece em {_dona}, em forma nenhuma')
        if _orfaos5:
            for _o in _orfaos5:
                erro('5', _o + ' — a peca 21 afirma um rotulo que a dona nao usa')
        else:
            print(f'  [x] os {len(_rot5)} rotulos estao na mesma tabela e existem '
                  'nas donas.')


bloco('6. ENCARNACAO — as tres Origens citadas existem na peca 9')

_p9 = ler(POR_NUM[9])
_BLOCOS_P9 = re.split(r'^###\s+', _p9, flags=re.M)[1:]
ORIGENS_P9 = [b.split('\n', 1)[0].strip() for b in _BLOCOS_P9
              if re.search(r'^\|\s*\*\*Legados\*\*\s*\|', b, re.M)]

_enc = []
_dentro = False
for _l in P21_L:
    if re.match(r'^\|.*\|\s*Origem\s*\|', _l):
        _dentro = True
        continue
    if _dentro:
        if not _l.startswith('|'):
            break
        if separador(_l):
            continue
        _c = celulas(_l)
        if _c:
            _enc.append(re.sub(r'\*', '', _c[-1]).strip())

print(f'  Origens lidas da peca 9  : {len(ORIGENS_P9)}')
print(f'  rotas de encarnacao      : {len(_enc)}  {_enc}')

ROTAS_ESPERADAS = 3
if not ORIGENS_P9:
    erro('6', 'nenhuma Origem lida da peca 9 — o extrator quebrou')
elif len(_enc) != ROTAS_ESPERADAS:
    erro('6', f'a tabela de encarnacao tem {len(_enc)} rota(s) e a peca fala de '
              f'{ROTAS_ESPERADAS}')
else:
    _fora6 = [o for o in _enc if o not in ORIGENS_P9]
    if _fora6:
        erro('6', f'a peca 21 cita Origem que a peca 9 nao tem: {_fora6}')
    else:
        print(f'  [x] as {len(_enc)} Origens de encarnacao existem na peca 9.')



# --- a tabela do §6 da peca 21: qual Legado, que formato, que Origem, o que
# desliga. Ela e' a ponte entre esta peca e a peca 13, e e' de onde as
# checagens 7 e 9 leem os NOMES — nunca de constante escrita aqui.
LIGACOES = []
_dentro = False
for _l in P21_L:
    if re.match(r'^\|\s*Legado\s*\|\s*formato\s*\|', _l):
        _dentro = True
        continue
    if _dentro:
        if not _l.startswith('|'):
            break
        if separador(_l):
            continue
        _c = celulas(_l)
        if len(_c) == 4:
            LIGACOES.append({
                'legado':  re.sub(r'[`*]', '', _c[0]).strip(),
                'formato': re.sub(r'[`*]', '', _c[1]).strip(),
                'origem':  re.sub(r'[`*]', '', _c[2]).strip(),
                'desliga': re.sub(r'[`*]', '', _c[3]).strip(),
            })


def formatos_na_peca13(legado):
    """Em que tabela(s) de formato da peca 13 este Legado aparece."""
    achados, secao, origem = set(), None, None
    for _l in _p13.split('\n'):
        _mo = re.match(r'^###\s+(.+?)(?:\s+—|$)', _l.strip())
        if _mo:
            origem = _mo.group(1).strip()
        _m = re.match(r'^\*\*(Destranca|Ajusta|Desliga)\b', _l.strip())
        if _m:
            secao = _m.group(1)
            continue
        if _l.startswith('|') and secao:
            _c = celulas(_l)
            if _c and re.sub(r'[`*]', '', _c[0]).strip() == legado:
                achados.add((secao, origem, _c[1] if len(_c) > 1 else ''))
    return achados


bloco('7. LIGACOES — todo Legado citado no §6 bate de formato e de Origem')

_PISO7 = 2
print(f'  ligacoes declaradas      : {len(LIGACOES)}  (piso {_PISO7})')
if len(LIGACOES) < _PISO7:
    erro('7', f'a tabela de ligacoes tem {len(LIGACOES)} linha(s) e o piso e '
              f'{_PISO7} — o extrator quebrou e esta checagem parou de conferir')
else:
    for _lg in LIGACOES:
        _ach = formatos_na_peca13(_lg['legado'])
        _fmts = {a[0] for a in _ach}
        _orgs = {a[1] for a in _ach}
        print(f"      {_lg['legado']:<14} peca 21 diz {_lg['formato']:<10} "
              f"{_lg['origem']:<14} | peca 13 diz {sorted(_fmts) or '—'} "
              f"{sorted(_orgs) or '—'}")
        if not _ach:
            erro('7', f"a peca 21 cita o `{_lg['legado']}` e ele nao aparece em "
                      'tabela de formato nenhuma da peca 13')
        elif _fmts != {_lg['formato']}:
            erro('7', f"a peca 21 diz que o `{_lg['legado']}` e {_lg['formato']} "
                      f'e a peca 13 lista ele como {sorted(_fmts)}')
        elif _lg['origem'] not in _orgs:
            erro('7', f"a peca 21 poe o `{_lg['legado']}` no {_lg['origem']} e a "
                      f'peca 13 poe ele em {sorted(_orgs)}')
    if not [f for f in FALHAS if f.startswith('7:')]:
        print(f'  [x] as {len(LIGACOES)} ligacoes batem de formato e de Origem '
              'com a peca 13.')


bloco('8. A ATRACAO — declarada aqui, e em nenhuma outra peca')

_RX_DECL = re.compile(r'sem selo puxa maldi[çc][ãa]o', re.I)
_donas8 = [p for p in PECAS if _RX_DECL.search(ler(p))]

print(f'  pecas que declaram       : {_donas8 or "nenhuma"}')
if not _donas8:
    erro('8', 'nenhuma peca declara a atracao — ela e a UNICA coisa nomeada que '
              'a peca 21 cria, e o `Conhecido` da peca 13 desliga ela')
elif _donas8 != [ALVO]:
    erro('8', f'a atracao esta declarada em {len(_donas8)} pecas: {_donas8} — '
              'uma coisa nomeada tem uma dona so')
else:
    print('  [x] a atracao tem uma dona so, e ela e a peca 21.')


bloco('9. A VAGA FECHADA — o Desliga do §6 aponta para a atracao nas duas pecas')

_desligas = [l for l in LIGACOES if l['formato'] == 'Desliga']
if len(_desligas) != 1:
    erro('9', f'o §6 declara {len(_desligas)} Legado(s) de formato Desliga, e a '
              'peca fecha UMA vaga — nem zero, nem duas')
else:
    _lg = _desligas[0]
    _ach = formatos_na_peca13(_lg['legado'])
    _apaga = next((a[2] for a in _ach if a[0] == 'Desliga'), None)
    print(f"  o Legado da vaga         : `{_lg['legado']}`, no {_lg['origem']}")
    print(f"  peca 21 diz que desliga  : {_lg['desliga']}")
    print(f"  peca 13 diz que apaga    : {_apaga or 'nao encontrado'}")
    if _apaga is None:
        erro('9', f"o `{_lg['legado']}` nao e Desliga na peca 13")
    elif 'atra' not in _apaga.lower() or 'atra' not in _lg['desliga'].lower():
        erro('9', f"as duas pecas discordam do que o `{_lg['legado']}` desliga: "
                  f'peca 21 diz "{_lg["desliga"]}", peca 13 diz "{_apaga}"')
    else:
        print(f"  [x] o `{_lg['legado']}` desliga a atracao nos dois documentos.")


bloco('10. VAGA MORTA — a peca 13 nao diz mais que a vaga espera esta peca')

_RX_MORTA = re.compile(r'espera a pe[çc]a de objeto amaldi[çc]oado', re.I)
_mortas10 = [(i, l) for i, l in enumerate(_p13.split('\n'), 1)
             if _RX_MORTA.search(l)]
if _mortas10:
    for _i, _l in _mortas10:
        erro('10', f'peca 13 linha {_i} ainda diz que a vaga espera objeto '
                   'amaldicoado, e ele e a peca 21')
else:
    print('  [x] nenhuma linha da peca 13 diz que a vaga espera esta peca.')


bloco('11. PONTEIRO PENDURADO — todo termo em crase da peca 21 tem destino')

_RX_CRASE = re.compile(r'`([A-ZÁÂÃÀÉÊÍÓÔÕÚÇ][^`\n]{1,28})`')
_termos11 = sorted({m.group(1).strip() for m in _RX_CRASE.finditer(P21)})
_outras11 = '\n'.join(ler(p) for p in PECAS if p != ALVO)

_pendurados = []
for _t in _termos11:
    _definido = re.search(r'\*\*`?' + re.escape(_t) + r'`?\*\*', P21) is not None
    if not _definido and _t not in _outras11:
        _pendurados.append(_t)

_PISO11 = 3
print(f'  termos em crase na peca  : {len(_termos11)}  {_termos11}')
if len(_termos11) < _PISO11:
    erro('11', f'so achei {len(_termos11)} termo(s) em crase e o piso e {_PISO11} '
               '— o extrator quebrou e esta checagem parou de conferir')
elif _pendurados:
    erro('11', f'{len(_pendurados)} termo(s) em crase sem destino: {_pendurados} '
               '— nem definidos aqui, nem existentes em outra peca')
else:
    print(f'  [x] os {len(_termos11)} termos em crase tem destino.')


bloco('12. PECA 16 — ela aponta para esta peca, e nao a anuncia como pendente')

_RX_PEND12 = re.compile(r'objeto amaldi[çc]oado.{0,80}?'
                        r'(?:e outra pe[çc]a|est[áa] sendo escrit|'
                        r'n[ãa]o tem pe[çc]a dona)', re.I | re.S)
_pend12 = [i for i, l in enumerate(_p16.split('\n'), 1)
           if _RX_PEND12.search(l) and not l.lstrip().startswith('>')
           and '~~' not in l]
_aponta12 = re.search(r'pe[çc]a 21', _p16)

if _pend12:
    for _i in _pend12:
        erro('12', f'peca 16 linha {_i} ainda anuncia objeto amaldicoado como '
                   'pendente, e ele e a peca 21')
elif not _aponta12:
    erro('12', 'a peca 16 nao cita a peca 21 em lugar nenhum — o §9 dela e quem '
               'declarava que objeto amaldicoado era outra peca, e ele tem de '
               'nomear qual')
else:
    print('  [x] a peca 16 aponta para a peca 21 e nao a anuncia como pendente.')


print()
print('=' * 88)
if FALHAS:
    print(f'>>> {len(FALHAS)} PROBLEMA(S):')
    for _e in FALHAS:
        print('   -', _e)
    sys.exit(1)
print('>>> TUDO OK — a familia tem quatro donas, a peca 21 nao republica numero')
print('    de ninguem, e a unica coisa que ela cria tem uma dona so.')
sys.exit(0)

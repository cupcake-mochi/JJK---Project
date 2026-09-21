#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Confere o MANUAL contra o PROJETO. E a direcao que faltava.

O conferir-nomes.py olha projeto -> manual: "esse nome que eu batizei ja significa
alguma coisa la?". Ninguem olhava o contrario: "o manual usa alguma palavra que
este sistema nao tem?".

E por isso que o "Bonus de Treinamento" da Passiva Reforco sobreviveu ate a v0.25
e o "Habilidade / Sabedoria" da Restricao Fraqueza sobreviveu ate a v0.26. Os dois
sao vocabulario de outro sistema vivo dentro do manual, e nenhum dos cinco
validadores olhava para la: o pac7.py e o v7.py conferem NUMERO, e o conferir-nomes
confere a outra direcao.

Oito checagens (as quatro primeiras sao as originais; 5 a 8 vieram
depois, e cada uma tem o motivo escrito no bloco dela):
  1. VOCABULARIO ORFAO — palavra de outro sistema que este aqui nao tem. Sabedoria
     e Carisma fundiram em Essencia; o nosso bonus de treino se chama Maestria;
     "Habilidade" aqui e atributo; "Grau" e patente e nao tamanho de feitico.
     Tolerancia zero: se aparecer, alguem escreveu texto novo sem olhar o lado de ca.
  2. OS CINCO ATRIBUTOS — nenhum outro nome de atributo pode aparecer no manual.
  3. TERMO MECANICO SEM DEFINICAO — palavra que o manual usa como se fosse termo
     definido e nunca explica. As que ja existem estao declaradas aqui com motivo,
     no mesmo padrao do conferir-pericias; uma nova FALHA.
  4. OS NUMEROS COMPARTILHADOS, COM DONO DECLARADO — a tabela de PE, a de inimigo
     e a curva de Rotina aparecem nos dois lados. Se divergirem, o projeto mente em
     silencio.
     ATENCAO AO QUE ESTA CHECAGEM *NAO* DIZ. Ela nao diz que o manual esta certo.
     Os limitadores e exemplos dele foram calibrados quando o sistema em volta era
     outro; eles servem de continuidade, nao de lei. Divergencia aqui e' um pedido
     de DECISAO — qual dos dois lados muda —, e nao um veredito de que o projeto
     errou. Por isso cada numero carrega um dono declarado logo abaixo.

Roda sem argumento. Sai com codigo 1 se algo quebrar.
Sem python-docx, as oito checagens sao PULADAS com aviso, em vez de falhar.
"""

import os
import re
import sys

FALHAS = []
AVISOS = []


def erro(msg):
    FALHAS.append(msg)
    print(f'  !! {msg}')


def aviso(msg):
    AVISOS.append(msg)
    print(f'  ~~ {msg}')


def bloco(t):
    print()
    print('=' * 88)
    print(t)
    print('=' * 88)


# --------------------------------------------------------------------------
AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.abspath(os.path.join(AQUI, '..', '..'))
DOCX = os.path.join(RAIZ, 'manual', 'Fundamento-MANUAL-v7.docx')

try:
    import docx  # noqa: F401
except ImportError:
    print('~~ python-docx nao instalado. As oito checagens foram PULADAS.')
    print('   pip install python-docx --break-system-packages')
    sys.exit(0)

if not os.path.exists(DOCX):
    print(f'~~ manual nao encontrado em {DOCX}. As oito checagens foram PULADAS.')
    sys.exit(0)

import docx as _docx
_D = _docx.Document(DOCX)

LINHAS = []          # (origem, texto)
for i, p in enumerate(_D.paragraphs):
    if p.text.strip():
        LINHAS.append((f'paragrafo {i}', p.text))
for ti, t in enumerate(_D.tables):
    for ri, r in enumerate(t.rows):
        txt = ' | '.join(c.text for c in r.cells)
        if txt.strip():
            LINHAS.append((f'tabela {ti}, linha {ri}', txt))

TUDO = '\n'.join(t for _, t in LINHAS)

print(f'Manual lido: {len(_D.paragraphs)} paragrafos, {len(_D.tables)} tabelas, '
      f'{len(LINHAS)} linhas com texto.')


# --------------------------------------------------------------------------
bloco('1. VOCABULARIO ORFAO — palavra de outro sistema viva no manual')

# termo -> (o que este sistema usa no lugar, por que a troca aconteceu)
ORFAOS = {
    r'\bSabedoria\b':            ('Essencia', 'Sabedoria e Carisma fundiram em Essencia'),
    r'\bCarisma\b':              ('Essencia', 'Sabedoria e Carisma fundiram em Essencia'),
    r'\bHabilidade\b':           ('atributo', 'aqui os cinco se chamam atributos'),
    r'B[oô]nus de Treinamento':  ('Maestria', 'o nosso numero de treino e a Maestria'),
    r'Classe de Armadura':       ('Defesa', 'Defesa = 10 + Destreza + protecao'),
    r'Percep[çc][aã]o Passiva':  ('a pericia Percepcao', 'nao existe valor passivo aqui'),
    r'Profici[êe]ncia':          ('Maestria', 'o treino e binario e o numero e a Maestria'),
    r'\bGrau\b':                 ('Classe', 'Grau e a patente do feiticeiro desde a v0.20'),
    r'\bEscala\b':               ('Classe', 'nome de rascunho do tamanho do feitico'),
    r'\bPot[êe]ncia\b':          ('Classe', 'nome de rascunho do tamanho do feitico'),
    r'\btruque\b':               ('feitico de Classe 0', 'vocabulario de outro sistema'),
    r'\bcantrip\b':              ('feitico de Classe 0', 'vocabulario de outro sistema'),
    r'\bn[ií]vel de conjurador\b': ('nivel', 'aqui existe um nivel so'),
}

achou_orfao = False
for rx, (subst, motivo) in ORFAOS.items():
    hits = [(o, t) for o, t in LINHAS if re.search(rx, t)]
    if hits:
        achou_orfao = True
        nome = rx.replace(r'\b', '').replace('[oô]', 'o').replace('[êe]', 'e') \
                 .replace('[çc]', 'c').replace('[aã]', 'a').replace('[ií]', 'i')
        erro(f'"{nome}" aparece {len(hits)}x no manual. Aqui isso e "{subst}" — {motivo}')
        for o, t in hits[:3]:
            print(f'        {o}: {t[:150]}')
if not achou_orfao:
    print(f'  Nenhum dos {len(ORFAOS)} termos de outro sistema aparece no manual.')
    print('  Esta e a checagem que teria pego o Bonus de Treinamento na v0.24 e o')
    print('  Habilidade/Sabedoria da Fraqueza tres versoes antes de a v0.26 achar.')


# --------------------------------------------------------------------------
bloco('2. TESTE NOMEADO PELO ATRIBUTO, EM VEZ DO TESTE DE RESISTENCIA')

TRS = ['Fisico', 'Vigor', 'Intelecto', 'Espirito']
ATRIBUTOS = ['Forca', 'Destreza', 'Constituicao', 'Inteligencia', 'Essencia']
print('  Aqui existem quatro Testes de Resistencia — ' + ' · '.join(TRS) + ' — e cada um')
print('  tem um atributo por baixo. O manual nao pode chamar um teste pelo ATRIBUTO:')
print('  "teste de Constituicao" nao diz se e o TR Vigor ou outra coisa, e o TR Fisico')
print('  usa Forca OU Destreza, entao a traducao nem e um para um.\n')

# "teste de X" / "Teste de Resistencia de X", onde X e' nome de atributo
RX_TESTE = (r'[Tt]este(?:s)? (?:de Resist[êe]ncia )?de (?:uma )?'
            r'(For[çc]a|Destreza|Constitui[çc][aã]o|Intelig[êe]ncia|Ess[êe]ncia|'
            r'Sabedoria|Carisma|Habilidade)')
achou_teste = False
for o, t in LINHAS:
    for m in re.finditer(RX_TESTE, t):
        achou_teste = True
        erro(f'{o}: teste nomeado pelo atributo — "{m.group(0)}". '
             f'Aqui os testes se chamam {", ".join(TRS)}')
        print(f'        {t[:170]}')
if not achou_teste:
    print('  Nenhum teste do manual e nomeado pelo atributo.')

# uma regra de preco que liste atributos so pode listar os cinco daqui
DE_FORA = ['Sabedoria', 'Carisma', 'Astucia', 'Aparencia', 'Percepcao Passiva']
fora = [x for x in DE_FORA
        if re.search(r'\b' + x.replace('c', '[çc]').replace('e', '[êe]') + r'\b', TUDO)]
if fora:
    erro(f'atributo que nao existe neste sistema citado no manual: {", ".join(fora)}')
else:
    print('\n  E nenhum atributo de fora aparece. Uma regra de preco que cite atributo')
    print('  (como a Restricao Fraqueza) so pode citar os cinco daqui.')

print('\n  Contagem, so para leitura — a palavra tambem aparece como Tema e como prosa:')
for nome, rx in zip(ATRIBUTOS, [r'For[çc]a', r'Destreza', r'Constitui[çc][aã]o',
                                r'Intelig[êe]ncia', r'Ess[êe]ncia']):
    print(f'    {nome:<16}{len(re.findall(rx, TUDO)):>3}x')
print('    (Vontade e Forca aparecem tambem como Tema, nos grupos "Mente e alma" e')
print('     "Forca e movimento". Tema nao e atributo, e por isso a checagem olha para')
print('     a frase "teste de X" em vez de para a palavra solta.)')


# --------------------------------------------------------------------------
bloco('3. TERMO MECANICO USADO E NUNCA DEFINIDO')

# termo -> (regex, motivo pelo qual ele esta declarado aqui em vez de falhar)
INDEFINIDOS_ACEITOS = {
    'inimigo fraco': (
        r'[Ii]nimigos? fracos?',
        'a Passiva Peso da Presenca so pega inimigo fraco. Depende do bestiario, '
        'que sai da matematica de inimigo do proprio manual.'),
}

# Termos que o manual IMPORTA do projeto, de proposito. Eles sao a direcao
# contraria do problema que este validador existe para pegar: em vez de vocabulario
# de outro sistema vazando para dentro, e vocabulario DESTE sistema entrando porque
# uma peca precisou dele. Cada um so entra aqui com o lugar onde o manual o define.
#
# O teste generico de "esta definido" (a constante DEFINE) aceita qualquer frase
# que contenha a palavra "e" — e quase toda frase em portugues contem. Isso basta
# para os termos da checagem acima, que sao raros e aparecem poucas vezes. NAO
# basta aqui: um termo importado aparece em varias linhas, e uma delas vai casar
# por acidente. Entao cada importado declara o PROPRIO padrao de definicao.
IMPORTADOS_DO_PROJETO = {
    'refino': (
        r'\brefino\b',
        r'[Oo] \*?\*?refino\*?\*? é',
        'a Expansao de Dominio (v7.7) tem gate de refino, desconto de refino e '
        'duracao por refino. O manual define o termo na caixa "REFINO, EM UMA LINHA" '
        'da secao 7 e nao usa ele em mais lugar nenhum.'),
}

# termos que EXIGEM definicao no manual: se aparecerem sem uma linha que os
# explique, e sem estarem declarados acima, falha
EXIGEM_DEFINICAO = {
    'dano fisico':  r'dano f[ií]sico',
    'resistencia':  r'resist[êe]ncia (ao|a) (seu )?tipo de dano|sem resist[êe]ncia',
    # entra aqui para que a isencao dele em INDEFINIDOS_ACEITOS seja um caminho
    # VIVO. Ate a v0.161 as duas listas nao tinham um termo em comum, entao o
    # `elif nome in INDEFINIDOS_ACEITOS` nunca era alcancado — a lista parecia
    # excecao de checagem e nao isentava nada. Quando o Bestiario definir o
    # termo, a isencao sai e esta linha passa a cobrar de verdade.
    'inimigo fraco': r'[Ii]nimigos? fracos?',
}

DEFINE = r'\b[ée]\b|significa|quer dizer|considera-se|chamamos|:\s*metade|metade do dano'

for nome, rx in EXIGEM_DEFINICAO.items():
    usos = [(o, t) for o, t in LINHAS if re.search(rx, t)]
    if not usos:
        print(f'  {nome:<16} 0 usos — nao esta no manual')
        continue
    defs = [t for _, t in usos if re.search(DEFINE, t)]
    if defs:
        print(f'  {nome:<16} {len(usos)} uso(s), definido')
    elif nome in INDEFINIDOS_ACEITOS:
        print(f'  {nome:<16} {len(usos)} uso(s), indefinido — ACEITO')
    else:
        erro(f'"{nome}" e usado {len(usos)}x no manual e nunca definido. '
             f'Dois mestres leem diferente, e o preco da peca que o usa depende disso')
        for o, t in usos[:3]:
            print(f'        {o}: {t[:150]}')

print()
print('  Termos IMPORTADOS do projeto — o manual usa, e tem que definir:')
for nome, (rx, rx_def, motivo) in IMPORTADOS_DO_PROJETO.items():
    usos = [(o, t) for o, t in LINHAS if re.search(rx, t)]
    if not usos:
        aviso(f'"{nome}" esta declarado como termo importado e nao aparece mais no '
              'manual — a declaracao virou peso morto')
        continue
    defs = [t for _, t in usos if re.search(rx_def, t)]
    if not defs:
        erro(f'"{nome}" e termo do PROJETO, aparece {len(usos)}x no manual e nunca e '
             'definido la. Quem le so o manual nao sabe o que ele e, e o gate que '
             'depende dele vira numero sem unidade')
    else:
        print(f'    {nome} ({len(usos)}x, definido no manual)')
        print(f'      motivo: {motivo}')

print()
print('  Indefinidos ACEITOS, com motivo declarado:')
for nome, (rx, motivo) in INDEFINIDOS_ACEITOS.items():
    n = len([1 for _, t in LINHAS if re.search(rx, t)])
    if n == 0:
        aviso(f'"{nome}" esta declarado como indefinido aceito e nao aparece mais '
              f'no manual — a declaracao virou peso morto')
    else:
        print(f'    {nome} ({n}x)')
        print(f'      motivo: {motivo}')


# --------------------------------------------------------------------------
bloco('4. OS NUMEROS COMPARTILHADOS, E QUEM MANDA EM CADA UM')
print('  Estes numeros aparecem nos DOIS lados. Se divergirem, o projeto mente em')
print('  silencio — mas divergir nao quer dizer que o projeto errou. Os limitadores')
print('  do manual foram calibrados quando o sistema em volta era outro: eles servem')
print('  de continuidade, e nao de lei.\n')
DONO = {
    'PE': ('o PROJETO', 'nada exige que o Emanador tenha 6 de PE por nivel. O que exige e '
           'que a coluna "quantas vezes voce lanca" diga a verdade sobre a ficha. Mudou o '
           '6? Regere a coluna. O numero e nosso; a coluna e a consequencia'),
    'inimigo': ('o PLAYTEST', 'esta e a unica das tres que afirma alguma coisa sobre o '
                'mundo: que um combate dura ~3,5 rodadas. A trava de vida inteira da peca 1 '
                'foi calibrada contra ela. Ninguem e dono ate alguem jogar'),
    'Classe 0': ('o MANUAL', 'ele tem tabela propria — 2d8 . 3d8 . 4d8 . 5d8 . 6d8 por '
                 'faixa de nivel — e ate a v0.79 nenhum documento do projeto e nenhum '
                 'validador abriam ela. A peca 6 precava ele em 4,50 fixo, que nao existe '
                 'no manual. Ele e a QUARTA tabela compartilhada, e era a unica sem dono'),
    'Rotina': ('o MANUAL', 'ela nao e uma medida, e a DEFINICAO de "quanto dano por rodada '
               'e normal". Nao ha verdade fora dela — o projeto compara tudo contra ela, '
               'inclusive ela mesma. Mudar a Rotina e mudar a regua, e reprecifica tudo'),
}
for k, (quem, motivo) in DONO.items():
    print(f'  {k:<10} dono: {quem}')
    print(f'             {motivo}')
print()

# (rotulo, o que o projeto assume, funcao que extrai do .docx)
def _tabela_com(cabecalho_contem):
    for t in _D.tables:
        hdr = ' | '.join(c.text.strip() for c in t.rows[0].cells)
        if all(k in hdr for k in cabecalho_contem):
            return t
    return None


ok_num = True

# 4a. PE por nivel do conjurador — a peca 1 secao 5.3 diz que a formula veio daqui
t = _tabela_com(['PE total'])
if t is None:
    erro('nao achei a tabela de PE total no manual — a peca 1, secao 5.3 diz que a '
         'formula do PE maximo vem dela')
    ok_num = False
else:
    print(f"  {'nivel':<8}{'PE do manual':<16}{'6 x nivel':<12}bate?")
    for r in t.rows[1:]:
        cel = [c.text.strip() for c in r.cells]
        try:
            nv, pe = int(cel[0]), int(cel[1])
        except ValueError:
            continue
        bate = pe == 6 * nv
        print(f'  {nv:<8}{pe:<16}{6*nv:<12}{"sim" if bate else "NAO"}')
        if not bate:
            ok_num = False
            erro(f'PE: o manual diz {pe} no nivel {nv} e a formula do projeto da {6*nv}. '
                 f'DONO: {DONO["PE"][0]} — entao o normal e regerar a coluna do manual, '
                 f'e nao mudar a peca 1. Se a decisao for a outra, mude os dois')

# 4b. dano de chefe e capanga — o conferir-atributos.py tem essa tabela dentro
CHEFE_NO_PROJETO = {2: 17, 5: 39, 10: 75, 15: 111, 20: 147, 25: 183, 30: 219}
t = _tabela_com(['Chefe', 'Capanga'])
if t is None:
    erro('nao achei a tabela de inimigos no manual — o conferir-atributos.py copia '
         'o dano de chefe dela para medir rodadas sob foco')
    ok_num = False
else:
    print(f"\n  {'nivel':<8}{'chefe no manual':<18}{'no projeto':<14}bate?")
    for r in t.rows[1:]:
        cel = [c.text.strip() for c in r.cells]
        try:
            nv, dano = int(cel[0]), int(cel[3])
        except (ValueError, IndexError):
            continue
        esperado = CHEFE_NO_PROJETO.get(nv)
        bate = esperado == dano
        print(f'  {nv:<8}{dano:<18}{str(esperado):<14}{"sim" if bate else "NAO"}')
        if not bate:
            ok_num = False
            erro(f'inimigo: o manual diz {dano} de dano de chefe no nivel {nv} e o '
                 f'conferir-atributos.py assume {esperado}. DONO: {DONO["inimigo"][0]} — '
                 f'esta e a tabela que promete ~3,5 rodadas, e mexer nela move a trava '
                 f'de vida inteira da peca 1')

# 4c. a coluna Rotina — a peca 6 usa ela para aprovar ataque extra e invocacao
ROTINA_NO_PROJETO = {1: 13, 2: 31, 3: 45, 4: 63, 5: 76, 6: 94, 7: 108}
t = _tabela_com(['Rotina'])
if t is None:
    erro('nao achei a coluna Rotina no manual — a peca 6 pendura nela o ataque '
         'extra e o orcamento de invocacao')
    ok_num = False
else:
    print(f"\n  {'Classe':<8}{'Rotina no manual':<20}{'no projeto':<14}bate?")
    for r in t.rows[1:]:
        cel = [c.text.strip() for c in r.cells]
        try:
            cl = int(cel[1])
        except (ValueError, IndexError):
            continue
        m = re.search(r'=\s*(\d+)', cel[2])
        if not m:
            continue
        dano = int(m.group(1))
        esperado = ROTINA_NO_PROJETO.get(cl)
        bate = esperado == dano
        print(f'  {cl:<8}{dano:<20}{str(esperado):<14}{"sim" if bate else "NAO"}')
        if not bate:
            ok_num = False
            erro(f'Rotina da Classe {cl}: o manual diz {dano} e a peca 6 assume '
                 f'{esperado}. DONO: {DONO["Rotina"][0]} — ela e a regua, nao uma medida. '
                 f'Mudar a Rotina reprecifica o golpe canalizado, o ataque extra e a '
                 f'invocacao de uma vez')

if ok_num:
    print('\n  Os tres conjuntos batem. Enquanto baterem, nenhuma das dez decisoes do')
    print('  projeto penduradas neles precisa ser reaberta.')


# --------------------------------------------------------------------------
# 4d. A ROTINA POR NIVEL DA PECA 6 SS3 CONTRA A COLUNA DO MANUAL
#
# Escrita na v0.60, e ela existe por um vao que a 4c acima NAO cobre.
#
# A 4c confere a coluna Rotina do .docx contra um dicionario escrito aqui. Ela sai
# VERDE com a peca 6 publicando qualquer coisa, porque ela nunca abre a peca 6. Foi
# por esse vao que o 81 e o 126 sobreviveram catorze versoes: os dois moram na MESMA
# tabela do manual, em OUTRAS colunas — 'Feitico num alvo' da Classe 6 e 'Somando
# alvos' da Classe 7. Numero que veio da coluna errada da tabela certa passa por
# qualquer varredura que so procure se o numero existe no manual.
#
# NADA DE VALOR FICA ESCRITO AQUI, e isso vale para o mapa tambem: a faixa de nivel
# de cada Classe sai da coluna 'Nivel' da PROPRIA tabela do manual. Se o manual
# reagrupar as faixas, esta checagem acompanha sozinha.
#
# O QUE TEM DE ACENDER: trocar qualquer Rotina de qualquer tabela da peca 6 por
# outro numero da mesma linha do manual. Contra-teste: trocar pela Rotina certa de
# OUTRO nivel tambem tem de acender, senao a checagem so confere "existe no manual".
print()
print('  4d. a Rotina por NIVEL da peca 6 SS3 contra a coluna do manual')

_p6 = os.path.join(AQUI, '06-caminhos-e-trilhas.md')
_t = _tabela_com(['Rotina'])
if not os.path.exists(_p6):
    erro('nao achei a peca 6 para conferir a Rotina por nivel')
elif _t is None:
    erro('nao achei a coluna Rotina no manual para conferir a peca 6 SS3')
else:
    _i_rot = [n for n, c in enumerate(_t.rows[0].cells)
              if c.text.strip() == 'Rotina']
    _faixas = []
    for _r in _t.rows[1:]:
        _cel = [c.text.strip() for c in _r.cells]
        _n = re.findall(r'\d+', _cel[0])
        _m = re.search(r'=\s*(\d+)', _cel[_i_rot[0]]) if _i_rot else None
        if len(_n) >= 2 and _m:
            _faixas.append((int(_n[0]), int(_n[1]), int(_m.group(1))))

    def _rotina_do_nivel(nv):
        for _a, _b, _v in _faixas:
            if _a <= nv <= _b:
                return _v
        return None

    _txt = open(_p6, encoding='utf-8').read()
    # varre TABELA por TABELA, e so as que declaram Rotina no cabecalho
    _achados, _cab, _col = [], None, None
    for _lin in _txt.splitlines():
        _s = _lin.strip()
        if not _s.startswith('|'):
            _cab, _col = None, None
            continue
        _cel = [x.strip() for x in _s.strip('|').split('|')]
        if _cab is None:
            _r = [n for n, c in enumerate(_cel) if 'Rotina' in c]
            if _r:
                _cab, _col = _cel, _r[0]
            continue
        if not _cel or not _cel[0].isdigit():
            continue
        _m = re.match(r'\**\s*(\d+)', _cel[_col]) if _col < len(_cel) else None
        if _m:
            _achados.append((int(_cel[0]), int(_m.group(1))))

    if not _achados:
        erro('a peca 6 nao publica Rotina por nivel em tabela nenhuma — ou o '
             'formato mudou, e esta checagem parou de conferir em silencio')
    else:
        print(f"    {'nivel':<8}{'peca 6 diz':<13}{'manual, pela faixa':<21}bate?")
        _vistos = set()
        for _nv, _val in _achados:
            _esp = _rotina_do_nivel(_nv)
            _bate = _esp == _val
            if (_nv, _val) not in _vistos:
                _vistos.add((_nv, _val))
                print(f'    {_nv:<8}{_val:<13}{str(_esp):<21}'
                      f'{"sim" if _bate else "NAO"}')
            if not _bate:
                _onde = []
                for _r in _t.rows[1:]:
                    _c = [x.text.strip() for x in _r.cells]
                    for _j, _x in enumerate(_c):
                        if _j >= 2 and re.search(rf'=\s*{_val}$', _x):
                            _onde.append(f'Classe {_c[1]} · coluna "'
                                         f'{_t.rows[0].cells[_j].text.strip()}"')
                erro(f'peca 6: no nivel {_nv} ela publica Rotina {_val} e o manual '
                     f'diz {_esp}. DONO: {DONO["Rotina"][0]}. '
                     + (f'O {_val} existe no manual, mas em ' + ' e '.join(_onde)
                        + ('. Coluna certa, LINHA errada.'
                           if all('"Rotina"' in _o for _o in _onde)
                           else ' — coluna errada da tabela certa.')
                        if _onde else
                        f'O {_val} nao existe em coluna nenhuma daquela tabela.'))
        if all(_rotina_do_nivel(n) == v for n, v in _achados):
            print(f'    As {len(_vistos)} linhas de Rotina da peca 6 saem da coluna '
                  f'certa do manual,')
            print('    e a faixa de cada Classe foi lida do .docx em vez de escrita aqui.')


# --------------------------------------------------------------------------
# 4e. A ROTINA RECONSTROI DO PROPRIO MANUAL — e ela NUNCA foi "feitico + Classe 0"
#
# Escrita na v0.80. Ela existe porque a peca 6 SS3 passou de v0.14 ate aqui
# explicando a coluna Rotina com uma frase que nao reconstroi de nada:
# "a coluna Rotina do Fundamento ja e feitico + Classe 0". Ela nao e.
#
# A Rotina e o MEIO EXATO entre as duas colunas vizinhas da mesma tabela:
#     Feitico num alvo = 3 x Classe dados   (regra de ouro no 2: "para nos pontos")
#     Somando alvos    = 4 x Classe dados   (o teto)
#     Rotina           = floor(3,5 x Classe) dados
# Bate nas SETE Classes, com zero parametro livre.
#
# NADA DE VALOR ESCRITO AQUI: as tres contagens de dados de cada linha saem do .docx.
#
# O QUE TEM DE ACENDER: mexer na contagem de dados de qualquer Rotina do manual.
# CONTRA-TESTE: a leitura velha — "num alvo + Classe 0" — tem de dar DIFERENTE da
# Rotina em pelo menos uma Classe. Se ela desse igual, esta checagem estaria
# aprovando as duas leituras ao mesmo tempo e nao provaria nada.
print()
print('  4e. a Rotina reconstroi como o meio entre "num alvo" e "somando alvos"')

def _dados(txt):
    """soma todos os NdX de uma celula: '21d8 + 3d8 = 108' -> 24"""
    return sum(int(n) for n in re.findall(r'(\d+)d\d+', txt))

_tr = _tabela_com(['Rotina', 'Feitico num alvo']) or _tabela_com(['Rotina', 'Feitiço num alvo'])
_t0 = None
for _t in _D.tables:
    _l = [[c.text.strip() for c in r.cells] for r in _t.rows]
    if _l and _l[0][0].startswith('Seu n') and any(r[0] == 'Dano' for r in _l):
        _t0 = _l
        break

if _tr is None:
    erro('nao achei a tabela da curva no manual — a Rotina e a regua de tudo')
elif _t0 is None:
    erro('nao achei a tabela de dano do Classe 0 no manual. DONO: o MANUAL. '
         'Sem ela nao da para conferir a leitura velha da Rotina')
else:
    _cab = [c.text.strip() for c in _tr.rows[0].cells]
    _ir = next(n for n, c in enumerate(_cab) if c == 'Rotina')
    _ia = next(n for n, c in enumerate(_cab) if 'num alvo' in c)
    _is = next(n for n, c in enumerate(_cab) if 'Somando' in c)

    # o Classe 0 por FAIXA DE NIVEL, lido do .docx
    _nv0 = [int(x) for x in _t0[0][1:]]
    _dd0 = [int(re.match(r'(\d+)', x).group(1)) for x in _t0[2][1:]]

    def _c0_dados(nv):
        _v = _dd0[0]
        for _n, _x in zip(_nv0, _dd0):
            if nv >= _n:
                _v = _x
        return _v

    print(f"    {'Classe':<8}{'num alvo':<11}{'somando':<10}{'o meio':<9}"
          f"{'Rotina':<9}{'bate?':<7}{'num alvo + C0'}")
    _velha_bate_sempre = True
    for _r in _tr.rows[1:]:
        _cel = [c.text.strip() for c in _r.cells]
        if not _cel[1].isdigit():
            continue
        _cl = int(_cel[1])
        _da, _ds, _drot = _dados(_cel[_ia]), _dados(_cel[_is]), _dados(_cel[_ir])
        _meio = (_da + _ds) // 2
        _niv_da_classe = int(re.findall(r'\d+', _cel[0])[0])
        _velha = _da + _c0_dados(_niv_da_classe)
        if _velha != _drot:
            _velha_bate_sempre = False
        _bate = (_meio == _drot) and (_drot == 3 * _cl + _cl // 2)
        print(f'    {_cl:<8}{str(_da)+"d8":<11}{str(_ds)+"d8":<10}'
              f'{str(_meio)+"d8":<9}{str(_drot)+"d8":<9}'
              f'{"sim" if _bate else "NAO":<7}{str(_velha)+"d8"}')
        if not _bate:
            erro(f'Rotina da Classe {_cl}: o manual publica {_drot}d8, e o meio entre '
                 f'"num alvo" ({_da}d8) e "somando alvos" ({_ds}d8) da {_meio}d8 '
                 f'(= floor(3,5 x Classe) = {3*_cl + _cl//2}d8). DONO: '
                 f'{DONO["Rotina"][0]}. A Rotina e a regua: mudar ela reprecifica o '
                 f'golpe canalizado, o ataque extra, a invocacao e as quinze Trilhas')

    if _velha_bate_sempre:
        erro('CONTRA-TESTE FALHOU: "num alvo + Classe 0" deu igual a Rotina em TODAS '
             'as Classes. Entao esta checagem nao separa a leitura certa da leitura '
             'que viveu de v0.14 a v0.79, e ela nao esta provando nada')
    else:
        print('    Contra-teste: "num alvo + Classe 0" NAO reproduz a Rotina. A frase')
        print('    "a Rotina ja e feitico + Classe 0" morreu na v0.80, e esta linha e')
        print('    o que impede ela de voltar.')


# --------------------------------------------------------------------------
# 4f. O CLASSE 0 TEM DONO, E A PECA 6 PAROU DE INVENTAR UM
#
# Escrita na v0.80. O manual publica o dano de um Classe 0 numa tabela propria —
# 2d8 . 3d8 . 4d8 . 5d8 . 6d8 por faixa de nivel — e ate a v0.79 NENHUM documento
# do projeto e NENHUM validador abriam ela. A peca 6 SS3 precava o Classe 0 em 4,50
# em todo nivel, que e um numero que nao aparece em lugar nenhum do manual.
#
# O estrago: a coluna "conjurador" da peca 6 saia 5 pontos alta em todo nivel, e o
# vao "fisico - conjurador" — que paga o degrau do nivel 7 dos cinco Caminhos, o
# nivel 2 do Arremate e o empate em +6% — saia 4/5/6/7 quando ele e 9/10/11/12.
#
# A REGRA APLICADA, e ela e separada do limite de design de proposito:
#     a coluna "conjurador" da peca 6 e o feitico SOZINHO ("Feitico num alvo"),
#     porque um Classe 0 gasta a Acao Padrao e nao cabe junto do feitico grande.
# O LIMITE DE DESIGN e outro: o vao tem de ser positivo e crescer com o nivel,
#     porque ele e um golpe simples.
#
# NADA DE VALOR ESCRITO AQUI: o feitico por Classe e a faixa de cada Classe saem
# do .docx; os niveis publicados saem da peca 6.
#
# O QUE TEM DE ACENDER: somar qualquer coisa de volta na coluna conjurador.
print()
print('  4f. a coluna "conjurador" da peca 6 contra o feitico sozinho do manual')

if not os.path.exists(_p6):
    erro('nao achei a peca 6 para conferir a linha de base do SS3')
elif _tr is None:
    erro('nao achei a tabela da curva no manual para conferir a peca 6')
else:
    _faixa_cl = []
    _feitico = {}
    for _r in _tr.rows[1:]:
        _cel = [c.text.strip() for c in _r.cells]
        if not _cel[1].isdigit():
            continue
        _n = re.findall(r'\d+', _cel[0])
        _cl = int(_cel[1])
        _feitico[_cl] = int(re.search(r'=\s*(\d+)', _cel[_ia]).group(1))
        if len(_n) >= 2:
            _faixa_cl.append((int(_n[0]), int(_n[1]), _cl))

    def _classe_do_nivel(nv):
        for _a, _b, _c in _faixa_cl:
            if _a <= nv <= _b:
                return _c
        return None

    # a tabela de base do SS3: nivel | Rotina | conjurador | fisico
    _linhas_base, _dentro = [], False
    for _lin in open(_p6, encoding='utf-8').read().splitlines():
        _s = _lin.strip()
        if not _s.startswith('|'):
            _dentro = False
            continue
        _cel = [x.strip() for x in _s.strip('|').split('|')]
        if not _dentro:
            if len(_cel) == 4 and 'Rotina' in _cel[1] and 'conjurador' in _cel[2]:
                _dentro = True
            continue
        if len(_cel) == 4 and _cel[0].isdigit():
            try:
                _linhas_base.append(tuple(int(re.match(r'\**\s*(-?\d+)', x).group(1))
                                          for x in _cel))
            except AttributeError:
                pass

    if not _linhas_base:
        erro('a peca 6 nao publica mais a tabela "nivel | Rotina | conjurador | '
             'fisico" — ou o formato mudou, e esta checagem parou em silencio')
    else:
        print(f"    {'nv':<5}{'conjurador':<12}{'feitico sozinho':<17}"
              f"{'fisico':<9}{'vao':<7}bate?")
        _vao_ant = None
        for _nv, _rot, _cj, _fi in _linhas_base:
            _cl = _classe_do_nivel(_nv)
            _esp = _feitico.get(_cl)
            _vao = _fi - _cj
            _bate = _esp == _cj
            print(f'    {_nv:<5}{_cj:<12}{str(_esp):<17}{_fi:<9}{_vao:<7}'
                  f'{"sim" if _bate else "NAO"}')
            if not _bate:
                erro(f'peca 6 SS3: no nivel {_nv} ela publica conjurador {_cj} e o '
                     f'feitico sozinho da Classe {_cl} e {_esp}. DONO do Classe 0: '
                     f'o MANUAL, na tabela de dano do Classe 0. A diferenca de '
                     f'{_cj - _esp} e o Classe 0 fantasma de 4,50 que viveu de v0.14 '
                     f'a v0.79 — um Classe 0 gasta a Acao Padrao e nao cabe junto do '
                     f'feitico grande')
            if _vao <= 0:
                erro(f'peca 6 SS3: o vao no nivel {_nv} deu {_vao}. Ele e um golpe '
                     f'simples, entao ele e positivo — e ele paga o degrau do nivel 7 '
                     f'dos cinco Caminhos')
            if _vao_ant is not None and _vao < _vao_ant:
                erro(f'peca 6 SS3: o vao encolheu do nivel anterior para o {_nv} '
                     f'({_vao_ant} -> {_vao}). Ele e um golpe simples e o golpe '
                     f'simples so cresce')
            _vao_ant = _vao

    # A frase morta, guardada POR LINHA e nao pelo arquivo inteiro.
    # Linha de citacao (">") e nota em italico ("*texto*") sao historia e podem
    # conter a frase — o projeto guarda o erro em vez de apagar.
    #
    # v0.81: o teste de historia estava ERRADO e deixava passar linha viva.
    # Ele aceitava qualquer linha comecando com "*", e "**negrito**" comeca com "*"
    # — e negrito no comeco da linha e o estilo dominante da prosa deste projeto.
    # Toda afirmacao viva em negrito era lida como nota historica.
    # Agora: ">" e historia, "*" sozinho e historia, "**" e AFIRMACAO VIVA.
    def _e_historica(_l):
        _s = _l.lstrip()
        if _s.startswith('>'):
            return True
        return _s.startswith('*') and not _s.startswith('**')

    _vivas, _historicas = [], 0
    for _n, _lin in enumerate(open(_p6, encoding='utf-8').read().splitlines(), 1):
        if 'feitiço + Classe 0' not in _lin:
            continue
        if _e_historica(_lin):
            _historicas += 1
        else:
            _vivas.append(_n)
    for _n in _vivas:
        erro(f'peca 6, linha {_n}: ela afirma que a Rotina e "feitico + Classe 0". '
             f'A checagem 4e prova que nao e — a Rotina e o meio entre bater num '
             f'alvo e espalhar, e o Classe 0 tem tabela propria no manual. Se for '
             f'nota historica, ela vai num bloco de citacao')
    if not _vivas:
        print(f'    A frase morta nao aparece viva em nenhuma linha '
              f'({_historicas} em nota historica, que e onde ela deve ficar).')

    # 4g. O NUMERO morto, e nao so a frase.
    # A frase morta era "a Rotina ja e feitico + Classe 0". O numero que ela
    # produzia era 4,50 de dano por Classe 0, e ele sobreviveu a v0.80 na SS5,
    # onde argumentava o PE do Bastiao — sem a frase, so o numero.
    # Guarda: nenhuma linha VIVA pode preçar um Classe 0 em 4,5 ou 4,50.
    # O dono do dano de um Classe 0 e o manual, e a tabela dele esta acima.
    _num, _num_hist = [], 0
    for _n, _lin in enumerate(open(_p6, encoding='utf-8').read().splitlines(), 1):
        if 'Classe 0' not in _lin:
            continue
        if not re.search(r'4,50?(?![0-9])', _lin):
            continue
        if _e_historica(_lin):
            _num_hist += 1
        else:
            _num.append(_n)
    print()
    print('  4g. o NUMERO morto do Classe 0 (4,50), e nao so a frase morta')
    for _n in _num:
        erro(f'peca 6, linha {_n}: ela preca um Classe 0 em 4,50. Esse numero nao '
             f'existe no manual — ele e o dano de UM d8, que e a regua de montar '
             f'feitico. O dano de um Classe 0 tem tabela propria no manual, e a '
             f'checagem 4f a le. Se for nota historica, ela vai num bloco de citacao')
    if not _num:
        print(f'    Nenhuma linha viva preca Classe 0 em 4,50 '
              f'({_num_hist} em nota historica).')


# --------------------------------------------------------------------------
# 4h. A FORMA DO ATAQUE EXTRA — e nao so o numero dele
#
# Escrita na v0.82 para guardar a forma "golpe SOLTO"; INVERTIDA na v0.147, quando
# o Mizuki reverteu aquela decisao. O motivo da inversao esta na peca 6 SS3.1 e ele
# e concreto: com o golpe solto, o `Bote` — nivel 19 da `Estocada` — comprava por
# 2,46 fatias uma coisa que ja acontecia sozinha. Entrega preçada valendo zero.
#
# O QUE ELA GUARDA AGORA, e sao TRES metades independentes de proposito:
#   (a) a peca 6 declara que o ataque extra EXIGE a Acao de Atacar;
#   (b) nenhuma linha VIVA da peca 6 afirma o contrario — a forma velha nao pode
#       voltar por descuido, e a tabela historica dela mora num bloco de citacao;
#   (c) a VALVULA continua escrita: "a nao ser que uma habilidade diga o contrario".
#       Sem ela o `Bote` morre de novo, e a inversao inteira perde o motivo.
#
# A (c) e a que importa mais, e ela e nova. As duas primeiras guardam a forma; a
# terceira guarda o que a forma existe para permitir.
#
# O PRECO DESTA FORMA ESTA MEDIDO E ACEITO: dois golpes rendem 23 no nivel 30
# contra 27 de um Classe 0 gratis, entao a Acao de Atacar fica dominada pelo botao
# que toda ficha tem. A v0.82 recusou a forma por isso; a v0.147 a escolhe sabendo.
print()
print('  4h. a FORMA do ataque extra na peca 6 — exige a Acao de Atacar, com valvula')

if not os.path.exists(_p6):
    erro('nao achei a peca 6 para conferir a forma do ataque extra')
else:
    _txt6 = open(_p6, encoding='utf-8').read()

    def _historica_h(_l):
        _s = _l.lstrip()
        if _s.startswith('>'):
            return True
        return _s.startswith('*') and not _s.startswith('**')

    # (a) a declaracao afirmativa existe — e ela e a LINHA DE REGRA, nao o titulo
    #     da secao. O arnes pegou a primeira versao desta checagem passando no
    #     proprio titulo "O ataque extra EXIGE a Acao de Atacar": apagar a regra
    #     saia VERDE. Mesmo defeito da checagem 2 do conferir-alma.py.
    _regra6 = [l for l in _txt6.splitlines()
               if re.search(r'ganha um golpe simples por rodada', l, re.I)]
    _regra6 = _regra6[0] if _regra6 else ''
    _decl = _regra6 and re.search(r'exige a A[cç][aã]o de Atacar', _regra6, re.I)
    if not _decl:
        erro('peca 6: a forma do ataque extra nao esta declarada. Ela precisa dizer '
             'que ele EXIGE a Acao de Atacar — foi a inversao da v0.147, e o que ela '
             'existe para consertar e o `Bote` da `Estocada` valer zero')
    else:
        print('    [x] a peca 6 declara que o ataque extra exige a Acao de Atacar')

    # (b) a forma velha nao pode voltar viva
    _contra = []
    for _n, _lin in enumerate(_txt6.splitlines(), 1):
        if not re.search(r'ataque extra|golpe simples', _lin, re.I):
            continue
        if not re.search(r'n[aã]o exige a A[cç][aã]o de Atacar|golpe\s+SOLTO|'
                         r'golpe simples solto', _lin, re.I):
            continue
        if _historica_h(_lin):
            continue
        _contra.append(_n)
    for _n in _contra:
        erro(f'peca 6, linha {_n}: a forma VELHA do ataque extra voltou — golpe solto, '
             f'sem exigir a Acao de Atacar. Ela foi invertida na v0.147, e com ela o '
             f'`Bote` da `Estocada` volta a valer zero com preco de 2,46 fatias. Se for '
             f'nota historica, ela vai num bloco de citacao')
    if not _contra:
        print('    [x] a forma velha so aparece em nota historica')

    # (c) A VALVULA — e ela e o motivo de a inversao caber.
    #     Tambem na LINHA DE REGRA: o paragrafo que explica a valvula carrega uma
    #     segunda copia dela, e o arnes mostrou que apagar a valvula da regra saia
    #     verde por causa dessa copia.
    if not re.search(r'a n[aã]o ser que uma habilidade diga o contr[aá]rio', _regra6, re.I):
        erro('peca 6: sumiu a valvula "a nao ser que uma habilidade diga o contrario". '
             'Sem ela nenhuma entrega de Trilha consegue comprar a excecao, e o `Bote` '
             'volta a ser letra morta — que e exatamente o defeito que a v0.147 saiu '
             'para consertar')
    else:
        print('    [x] a valvula continua escrita: habilidade pode dizer o contrario')

    # (c) o gate do golpe do Arremate e do Coro continua escrito — a outra metade
    #     da forma que a propria peca disse que nenhum validador guardava
    if not re.search(r'A[cç][aã]o B[oô]nus.{0,200}A[cç][aã]o Padr[aã]o', _txt6, re.S):
        erro('peca 6: sumiu o gate do golpe do Arremate e do Coro — ele e Acao '
             'Bonus e so existe se a Acao Padrao daquele turno foi gasta no que a '
             'Trilha e. Sem o gate, uma Padrao solta conjura, golpeia e ainda '
             'sobra a Bonus')
    else:
        print('    [x] o gate do golpe do Arremate e do Coro continua escrito')


# --------------------------------------------------------------------------
# 4i. A PAREDE DO MANUAL, que a peca 11 SS6.6 copiou
#
# Escrita na v0.91. A peca 11 preca a vida da `Barreira Simples` comparando com a
# Melhoria `Anteparo` do manual — "uma parede com 10 x Classe de vida" — e essa
# frase virou a SEGUNDA copia do numero. Sem esta checagem, o manual podia mudar
# a Melhoria e a peca continuaria preçando contra o valor velho.
#
# NADA ESCRITO AQUI: os dois lados sao lidos, um do .docx e o outro da peca 11.
print()
print('  4i. a parede da Melhoria `Anteparo` contra a copia da peca 11')

_ant_manual = None
for _t in _D.tables:
    for _r in _t.rows:
        _cel = [c.text.strip() for c in _r.cells]
        if _cel and _cel[0].strip() == 'Anteparo':
            _mm = re.search(r'(\d+)\s*[×x]\s*Classe', ' | '.join(_cel))
            if _mm:
                _ant_manual = int(_mm.group(1))
if _ant_manual is None:
    erro('nao achei a Melhoria `Anteparo` no .docx — a peca 11 preca a `Barreira '
         'Simples` contra ela e a comparacao ficou sem dono')
else:
    _p11m = os.path.join(AQUI, '11-aptidoes-e-refino.md')
    with open(_p11m, encoding='utf-8') as _f:
        _t11m = _f.read()
    _mm = re.search(r'`(\d+) × Classe` de vida', _t11m)
    _ant_peca = int(_mm.group(1)) if _mm else None
    if _ant_peca is None:
        erro('a peca 11 parou de citar a parede do `Anteparo` — a vida da `Barreira '
             'Simples` deixou de ter contra o que ser comparada')
    elif _ant_peca != _ant_manual:
        erro(f'o manual diz que o `Anteparo` da {_ant_manual} x Classe de vida e a peca '
             f'11 copiou {_ant_peca} x Classe — as duas copias divergiram, e a peca '
             f'preca a `Barreira Simples` contra a copia dela')
    else:
        print(f'    [x] as duas dizem {_ant_manual} x Classe. No Classe 7 sao '
              f'{_ant_manual*7} de vida.')


# --------------------------------------------------------------------------
# 4j. A ESCADA DE FREQUENCIA DO EFEITO PROPRIO, que a peca 11 SS6.7 copiou
#
# Escrita na v0.92. A peca 11 listou "falta a regua do Efeito Proprio" por sessenta
# versoes, e o manual publica ela numa tabela: "Em quantas cenas por arco isso vai
# importar? Uma cena: Leve. Metade: Media. Quase toda: Pesada. Na duvida, Pesada."
#
# A peca 6.7 usa essa escada para dizer em que degrau de Classe Passiva uma
# `Aptidao Propria` cai — entao ela virou a segunda copia das tres faixas.
print()
print('  4j. a escada de frequencia do `Efeito Proprio` contra a copia da peca 11')

_freq = None
for _t in _D.tables:
    for _r in _t.rows:
        _cel = ' | '.join(c.text.strip() for c in _r.cells)
        if 'Em quantas cenas por arco' in _cel:
            _freq = _cel
if _freq is None:
    erro('nao achei no .docx a pergunta do `Efeito Proprio` — a peca 11 SS6.7 preca a '
         '`Aptidao Propria` contra ela e a escada ficou sem dono')
else:
    _tres = [(k, v) for k, v in (('Uma cena', 'Leve'), ('Metade', 'Média'),
                                 ('Quase toda', 'Pesada'))
             if f'{k}: {v}' in _freq]
    if len(_tres) != 3:
        erro(f'a escada do `Efeito Proprio` no .docx nao tem as tres faixas na ordem '
             f'esperada — achei {len(_tres)}. A peca 11 SS6.7 mapeia as tres para os '
             f'tres degraus de Classe Passiva, e o mapa quebrou')
    elif 'Na dúvida, Pesada' not in _freq:
        erro('o manual parou de dizer "Na duvida, Pesada" na escada do `Efeito '
             'Proprio` — e o desempate e o que faz a peca 11 SS6.7 RECUSAR a proposta '
             'em vez de aceitar')
    else:
        _p11f = os.path.join(AQUI, '11-aptidoes-e-refino.md')
        with open(_p11f, encoding='utf-8') as _f:
            _t11f = _f.read()
        _copia = re.findall(r'\| \*\*(uma|metade|quase toda)\*\* \| (Leve|Média|Pesada) \|',
                            _t11f)
        _esp = [('uma', 'Leve'), ('metade', 'Média'), ('quase toda', 'Pesada')]
        if _copia != _esp:
            erro(f'a peca 11 SS6.7 copiou a escada do `Efeito Proprio` como {_copia} e o '
                 f'manual diz {_esp} — as duas copias divergiram')
        else:
            print('    [x] as tres faixas batem: uma/Leve, metade/Media, quase toda/Pesada.')
            print('    [x] o desempate "Na duvida, Pesada" continua nos dois.')


# --------------------------------------------------------------------------
# 4k. A LISTA DE PASSIVAS POR CLASSE PASSIVA, que a peca 11 SS4 copiou
#
# Escrita na v0.107, e ela nasceu de uma divergencia achada a olho na revisao do
# livro: a peca 11 publicava `—` na linha da Classe Passiva 3 — NENHUMA Passiva —
# enquanto o manual lista tres ali (`Escama`, `Afinidade`, `Reserva Profunda`).
# A linha da 2 tambem estava curta: cinco de sete.
#
# A coluna existe como PROVA de que a escada de formato foi lida do manual e nao
# inventada na peca. Uma prova que diverge do que ela cita prova o contrario.
#
# `Regra Propria` e `Passiva Propria` sao `1 a 3` e ficam de fora dos dois lados:
# elas nao moram numa altura so.
#
# NADA ESCRITO AQUI: as tres linhas saem do .docx, e as tres saem da peca 11.
print()
print('  4k. as Passivas por Classe Passiva no .docx contra a copia da peca 11 SS4')

_pv_manual = {'1': [], '2': [], '3': []}
for _t in _D.tables:
    _cab = [c.text.strip() for c in _t.rows[0].cells] if _t.rows else []
    if _cab[:3] != ['Passiva', 'Classe', 'O que faz']:
        continue
    for _r in _t.rows[1:]:
        _cel = [c.text.strip() for c in _r.cells]
        if len(_cel) >= 2 and _cel[1] in _pv_manual:
            _pv_manual[_cel[1]].append(_cel[0])

if not all(_pv_manual.values()):
    erro('nao achei a lista de Passivas do .docx com as tres alturas preenchidas — '
         'achei ' + repr({k: len(v) for k, v in _pv_manual.items()}) + '. A peca 11 SS4 '
         'copia essa lista como prova da escada, e a comparacao ficou sem dono')
else:
    _p11p = os.path.join(AQUI, '11-aptidoes-e-refino.md')
    with open(_p11p, encoding='utf-8') as _f:
        _t11p = _f.read()
    _pv_peca = {}
    for _lin in _t11p.splitlines():
        _m = re.match(r'\|\s*\*\*([123])\*\*\s*\|[^|]*\|\s*([^|]+?)\s*\|\s*$', _lin)
        if _m:
            _pv_peca[_m.group(1)] = [x.strip(' `') for x in _m.group(2).split('·')]
    if set(_pv_peca) != {'1', '2', '3'}:
        erro('nao consegui ler as tres linhas da tabela de Classe Passiva da peca 11 SS4 '
             f'— achei {sorted(_pv_peca)}. Se a tabela mudou de forma, esta checagem '
             'parou de conferir')
    else:
        _ruim = False
        for _cl in ('1', '2', '3'):
            if _pv_peca[_cl] != _pv_manual[_cl]:
                _ruim = True
                erro(f'Classe Passiva {_cl}: o manual lista {_pv_manual[_cl]} e a peca 11 '
                     f'SS4 copiou {_pv_peca[_cl]} — as duas copias divergiram, e a coluna '
                     f'da peca existe justamente para provar que a escada saiu do manual')
        if not _ruim:
            print('    [x] ' + ' · '.join(f'Classe Passiva {c}: {len(_pv_manual[c])}'
                                          for c in ('1', '2', '3')) +
                  ' — as tres linhas batem, nome por nome e na mesma ordem.')

# guarda: `Regra Propria` e `Passiva Propria` sao `1 a 3` e nao podem aparecer em
# nenhuma das tres linhas dos dois lados. Se o manual passar a dar altura fixa a
# uma delas, a comparacao acima muda de forma e esta guarda acusa primeiro.
_flex = [_c[0] for _t in _D.tables for _c in
         ([[x.text.strip() for x in _r.cells] for _r in _t.rows])
         if len(_c) >= 2 and _c[1] == '1 a 3']
if sorted(_flex) != ['Passiva Própria', 'Regra Própria']:
    erro(f'as Passivas de altura flexivel do .docx mudaram: achei {sorted(_flex)} e '
         f'esperava a `Regra Própria` e a `Passiva Própria`. A checagem 4k deixa as '
         f'duas de fora das tres linhas, e essa exclusao deixou de valer')
else:
    print('    [x] a `Regra Própria` e a `Passiva Própria` continuam `1 a 3`, fora das tres.')


# --------------------------------------------------------------------------
# 4l. v0.252: a Regra Propria de Classe 1 vem de graca na criacao (opcao X do Mizuki,
# 19/09/2026). Ate a v0.251 ela era a unica Passiva "comprada em Classe 1 desde o nivel
# 1" — frase que ja contradizia a tabela, que abre a Classe 1 para todas — e o teto
# dela na criacao nao estava escrito. Os numeros da regra NAO ficam aqui: o custo da
# subida sai da coluna `Custa` do .docx (Classe 3 menos Classe 1, Classe 2 menos Classe
# 1), e o teto na criacao sai da coluna `Libera no nivel` contra o nivel em que a ficha
# comeca, que e da peca 1. Se alguem abrir a Classe 2 no nivel 2, o teto derivado muda
# e a frase "Classe 1 e o teto" acende.
print()
print('  4l. a Regra Propria gratis na criacao: a subida, o teto e as cinco copias')

_custa, _libera = {}, {}
for _t in _D.tables:
    _cab = [c.text.strip() for c in _t.rows[0].cells] if _t.rows else []
    if _cab[:3] != ['Classe', 'Custa', 'Libera no nível']:
        continue
    for _r in _t.rows[1:]:
        _cel = [c.text.strip() for c in _r.cells]
        _m = re.match(r'(\d+) espaço', _cel[1])
        if _cel[0] in ('1', '2', '3') and _m and re.fullmatch(r'\d+', _cel[2]):
            _custa[int(_cel[0])] = int(_m.group(1))
            _libera[int(_cel[0])] = int(_cel[2])
_p1t = open(os.path.join(AQUI, '01-atributos-acerto-defesa.md'), encoding='utf-8').read()
_mn = re.search(r'A ficha começa no \*{0,2}nível (\d+)', _p1t)
if sorted(_custa) != [1, 2, 3] or not _mn:
    erro(f'4l: nao li o custo das tres Classes Passivas no .docx ({_custa}) ou o nivel em que a '
         f'ficha comeca na peca 1 ({bool(_mn)}) — sem os dois a regra da Regra Propria gratis '
         'nao tem de onde derivar')
else:
    _nv0 = int(_mn.group(1))
    _teto = max(c for c in (1, 2, 3) if _libera[c] <= _nv0)
    _d2, _d3 = _custa[2] - _custa[1], _custa[3] - _custa[1]
    _esp = lambda n: 'espaço' if n == 1 else 'espaços'
    _texto_docx = '\n'.join([p.text for p in _D.paragraphs] +
                            [c.text for t_ in _D.tables for r_ in t_.rows for c in r_.cells])
    _livro = os.path.join(AQUI, '..', '05-material', 'livro', 'manual')
    _l9 = open(os.path.join(_livro, '40-fundamento.md'), encoding='utf-8').read()
    _l6 = open(os.path.join(_livro, '20-criacao-de-personagem.md'), encoding='utf-8').read()
    _p8 = open(os.path.join(AQUI, '08-criacao-de-personagem.md'), encoding='utf-8').read()
    _ok4l = True

    def _quer(onde, texto, frase):
        global _ok4l
        if frase not in texto:
            _ok4l = False
            erro(f'4l: {onde} nao diz "{frase}"')

    def _proibe(onde, texto, frase):
        global _ok4l
        if frase in texto:
            _ok4l = False
            erro(f'4l: {onde} ainda diz "{frase}" — a frase que a decisao de 19/09/2026 tirou')

    # o .docx, que e o dono
    _quer('o .docx', _texto_docx, f'Na criação, a Regra Própria vem de graça em Classe {_teto}: ela não gasta espaço de feitiço')
    _quer('o .docx', _texto_docx, f'a Classe {_teto} é o teto dela até os níveis liberarem as maiores')
    _quer('o .docx', _texto_docx, f'pagando só a diferença pra Classe 1: {_d2} {_esp(_d2)} pra Classe 2, e {_d3} pra Classe 3')
    _quer('o .docx', _texto_docx, 'A Passiva Livre e a Regra Própria não contam')
    _quer('o .docx', _texto_docx, f'uma Regra Própria, de graça, em Classe {_teto}')
    _proibe('o .docx', _texto_docx, 'única Passiva que pode ser comprada em Classe 1')
    # a copia do livro (capitulo 9) e as duas listas de criacao (capitulo 6 e peca 8)
    _quer('o capitulo 9 do livro', _l9, f'Na criação, a `Regra Própria` vem de graça em Classe Passiva {_teto}: ela não gasta espaço de feitiço')
    _quer('o capitulo 9 do livro', _l9, f'pagando só a diferença para a Classe Passiva 1: {_d2} {_esp(_d2)} para a Classe Passiva 2, e {_d3} para a 3')
    _quer('o capitulo 9 do livro', _l9, 'A Passiva Livre e a `Regra Própria` não contam.')
    _quer('o capitulo 9 do livro', _l9, f'uma `Regra Própria`, de graça, em Classe Passiva {_teto}')
    _proibe('o capitulo 9 do livro', _l9, 'Só a `Regra Própria` pode ser comprada em Classe Passiva 1')
    _quer('o capitulo 6 do livro', _l6, f'a `Regra Própria` de Classe Passiva {_teto} vem junto, também de graça')
    _quer('a peca 8', _p8, f'a **Regra Própria** de Classe {_teto} vem junto, também de graça')
    if _ok4l:
        print(f'    [x] a Regra Propria vem gratis em Classe {_teto} (a mais alta aberta no nivel {_nv0}); '
              f'subir custa {_d2} e {_d3} {_esp(_d3)} (a diferenca para a Classe 1, lida da coluna Custa); '
              'as cinco copias dizem o mesmo e a frase antiga sumiu.')


# --------------------------------------------------------------------------
# 4m. v0.253: a Concentracao rola Vigor contra a CD de QUEM FERIU, e nao mais contra
# `10` ou metade do dano (decisao do Mizuki, 19/09/2026; a peca 3 §3, subsecao `A CD de
# quem te feriu`, e' a dona da regra e o conferir-acao.py, checagem 7, deriva as tabelas
# dela). Esta checagem guarda as COPIAS: o `Carregar` (usa a mesma CD, com teste de
# Espirito), a corrida de dominios (que passou a ser a mesma rolagem, so com a contagem
# trocada), o capitulo 2 e o glossario. Nenhum numero e' escrito aqui: o `10` da Mao Firme
# sai da Passiva no .docx (o dono) e tem de ser o mesmo nas outras tres copias.
print()
print('  4m. a Concentracao contra a CD de quem te feriu: as copias, a frase antiga e a Mao Firme')

_livro_m = os.path.join(AQUI, '..', '05-material', 'livro')


def _le_m(*partes):
    _c = os.path.join(_livro_m, *partes)
    return open(_c, encoding='utf-8').read() if os.path.isfile(_c) else None


_sem_md = lambda t: t.replace('**', '').replace('`', '')
_docx_m = '\n'.join([p.text for p in _D.paragraphs] +
                    [c.text for t_ in _D.tables for r_ in t_.rows for c in r_.cells])
_c2m = _sem_md(_le_m('manual', '11-o-turno.md') or '')
_c9m = _sem_md(_le_m('manual', '40-fundamento.md') or '')
_glm = _sem_md(_le_m('manual', '07-glossario.md') or '')
_p3m = _sem_md(open(os.path.join(AQUI, '03-economia-de-acao-e-iniciativa.md'), encoding='utf-8').read())
_txm = _le_m('Projeto-M-Manual-da-Guilda-TEXTO.md')
_txm = _sem_md(_txm) if _txm else None
_ok4m = True


def _quer_m(onde, texto, frase):
    global _ok4m
    if frase not in texto:
        _ok4m = False
        erro(f'4m: {onde} nao diz "{frase}"')


def _proibe_m(onde, texto, frase):
    global _ok4m
    if frase in texto:
        _ok4m = False
        erro(f'4m: {onde} ainda diz "{frase}" — a regra que a decisao de 19/09/2026 tirou')


_CARREGAR = 'faz um Teste de Resistência de Espírito contra a CD de quem te feriu para manter'
_CORRIDA = 'Teste de Resistência de Vigor contra a CD de quem te feriu, a mesma rolagem da Concentração'
_MAIOR = 'e contra a maior CD entre eles'
_VELHAS = ('ou metade do dano, o que for maior', 'ou metade do dano que você tomou',
           'CD do dono do outro domínio', 'com a CD e a contagem trocadas')

# o .docx (dono) e o capitulo 9 (copia)
for _onde, _t in (('o .docx', _docx_m), ('o capitulo 9 do livro', _c9m)):
    _quer_m(_onde, _t, _CARREGAR)
    _quer_m(_onde, _t, _CORRIDA)
    _quer_m(_onde, _t, _MAIOR)
# o capitulo 2 e o glossario
_quer_m('o capitulo 2 do livro', _c2m, 'faça um Teste de Resistência de Vigor contra a CD de quem te feriu. Se falhar, o efeito cai.')
_quer_m('o capitulo 2 do livro', _c2m, 'Cada golpe que te acerta é um teste')
_quer_m('o capitulo 2 do livro', _c2m, 'a rolagem é a mesma, com a contagem trocada')
_quer_m('o capitulo 9 do livro', _c9m, 'a mesma rolagem de Vigor da Concentração, com a contagem trocada')
_quer_m('o glossario do livro', _glm, 'tomar dano pede Teste de Resistência de Vigor contra a CD de quem te feriu')
_quer_m('a peca 3', _p3m, 'Cada golpe que acerta quem concentra pede um teste')
# a frase antiga, em todo lugar que publica a regra
for _onde, _t in (('o .docx', _docx_m), ('o capitulo 2 do livro', _c2m), ('o capitulo 9 do livro', _c9m),
                  ('o glossario do livro', _glm), ('o texto compilado do livro', _txm)):
    if _t is None:
        continue
    for _v in _VELHAS:
        _proibe_m(_onde, _t, _v)
if _txm is not None:
    _quer_m('o texto compilado do livro', _txm, _CARREGAR)
    _quer_m('o texto compilado do livro', _txm, _CORRIDA)
    _quer_m('o texto compilado do livro', _txm, 'faça um Teste de Resistência de Vigor contra a CD de quem te feriu. Se falhar, o efeito cai.')
else:
    print('    ~~ o texto compilado do livro nao existe: as copias dele nao foram conferidas')

# a Mao Firme: o dono e o .docx; as outras tres copias tem de dizer o mesmo numero
_mf = re.search(r'não perde concentração nem carga por dano de (\d+) ou menos', _docx_m)
if not _mf:
    _ok4m = False
    erro('4m: a Passiva `Mão Firme` saiu do .docx, ou parou de dizer "por dano de N ou menos" — '
         'sem ela nao ha de onde ler o numero que as copias repetem')
else:
    _nmf = _mf.group(1)
    for _onde, _t, _rx in (
            ('o capitulo 9 do livro', _c9m, r'não perde concentração nem carga por dano de (\d+) ou menos'),
            ('o capitulo 2 do livro', _c2m, r'Dano de (\d+) ou menos não pede o teste'),
            ('a peca 3', _p3m, r'dano de (\d+) ou menos não pede o teste')):
        _mx = re.search(_rx, _t)
        if not _mx:
            _ok4m = False
            erro(f'4m: {_onde} nao diz a regra da Mao Firme ({_rx})')
        elif _mx.group(1) != _nmf:
            _ok4m = False
            erro(f'4m: {_onde} diz "dano de {_mx.group(1)} ou menos" e a Passiva do .docx diz {_nmf}')
if _ok4m:
    print('    [x] o Carregar, a corrida, o capitulo 2, o glossario e a peca 3 dizem a CD de quem te feriu; '
          'nenhuma copia guarda a regra antiga; a Mao Firme diz o mesmo numero nas quatro.')


# --------------------------------------------------------------------------
# 4n. v0.254: a Concentrada e a Duradoura (as duas Melhorias de duracao, na Familia Tempo).
# O .docx e' o dono do custo e do texto delas; a peca 3 §3 e' dona da regra, e o
# conferir-acao.py (checagem 8) deriva o preco por Classe e confere a tabela de duracao contra
# o .docx. Esta checagem guarda as COPIAS: o capitulo 9 do livro, o texto compilado, o glossario,
# o capitulo 2, as duas frases da Condicao, e o numero de Melhorias escrito por extenso.
print()
print('  4n. a Concentrada e a Duradoura: as copias, e a contagem de Melhorias por extenso')

_ok4n = True


def _erro_n(msg):
    global _ok4n
    _ok4n = False
    erro(f'4n: {msg}')


_semmd = lambda t: t.replace('**', '').replace('`', '').strip()

# --- o dono: as duas linhas e a tabela de duracao do .docx ---
_linhas_d, _dur_d, _n_melhorias = {}, [], 0
for _t in _D.tables:
    _cab = [c.text.strip() for c in _t.rows[0].cells] if _t.rows else []
    if _cab[:3] == ['Melhoria', 'Custo', 'O que faz']:
        _n_melhorias += len(_t.rows) - 1
        for _r in _t.rows[1:]:
            _v = [c.text.strip() for c in _r.cells]
            if _v[0] in ('Concentrada', 'Duradoura'):
                _linhas_d[_v[0]] = (_v[1], _v[2])
    elif _cab[:3] == ['O que o efeito faz', 'Concentrada', 'Duradoura']:
        _dur_d = [[c.text.strip() for c in _r.cells] for _r in _t.rows[1:]]
if set(_linhas_d) != {'Concentrada', 'Duradoura'} or not _dur_d:
    _erro_n(f'nao achei no .docx as duas Melhorias ({sorted(_linhas_d)}) ou a tabela de duracao ({len(_dur_d)} linhas)')
else:
    # --- o livro (cap. 9) e o texto compilado: linha a linha ---
    for _onde, _t in (('o capitulo 9 do livro', _le_m('manual', '40-fundamento.md')),
                      ('o texto compilado do livro', _le_m('Projeto-M-Manual-da-Guilda-TEXTO.md'))):
        if _t is None:
            print(f'    ~~ {_onde} nao existe: as copias dele nao foram conferidas')
            continue
        _lin = {}
        for _l in _t.split('\n'):
            _m = re.match(r'^\|\s*`(Concentrada|Duradoura)`\s*\|\s*`?([^|`]+?)`?\s*\|\s*(.*?)\s*\|\s*$', _l)
            if _m:
                _lin[_m.group(1)] = (_m.group(2).strip(), _semmd(_m.group(3)))
        for _nome, (_custo, _texto) in _linhas_d.items():
            if _nome not in _lin:
                _erro_n(f'{_onde} nao tem a linha da `{_nome}`')
            elif _lin[_nome] != (_custo, _texto):
                _erro_n(f'{_onde}: a linha da `{_nome}` difere do .docx: {_lin[_nome]} contra {(_custo, _texto)}')
        # a tabela de duracao
        _rows = []
        _ini = _t.find('| O que o efeito faz | Concentrada | Duradoura |')
        if _ini >= 0:
            for _l in _t[_ini:].split('\n')[2:]:
                if not _l.startswith('|'):
                    break
                _rows.append([_semmd(c) for c in _l.strip().strip('|').split('|')])
        if _rows != [[_semmd(x) for x in _r] for _r in _dur_d]:
            _erro_n(f'{_onde}: a tabela de duracao difere da do .docx: {_rows} contra {_dur_d}')
    # --- a Condicao diz que a duracao de uma rodada pode ser trocada ---
    _frase = 'a não ser que o feitiço tenha a Concentrada ou a Duradoura'
    for _onde, _t in (('o .docx', _docx_m), ('o capitulo 9 do livro', _c9m)):
        if _t.count(_frase) < 2:
            _erro_n(f'{_onde} diz "{_frase}" {_t.count(_frase)} vez(es) e a Condicao pede 2 (a linha do catalogo e a frase das condicoes)')
    # --- o capitulo 2 e o glossario ---
    if 'A Duradoura faz o mesmo sem pedir concentração.' not in _c2m:
        _erro_n('o capitulo 2 do livro nao diz "A Duradoura faz o mesmo sem pedir concentracao."')
    for _nome_gl in ('Concentrada', 'Duradoura'):
        _gl = re.search(r'\|\s*\*\*`' + _nome_gl + r'`\*\*\s*\|[^|]+\|\s*(\d+)\s*\|', _le_m('manual', '07-glossario.md') or '')
        if not _gl or _gl.group(1) != '9':
            _erro_n(f'o glossario nao tem a entrada da `{_nome_gl}` apontando para o capitulo 9')
    # --- a contagem por extenso ---
    _U = {'um': 1, 'uma': 1, 'dois': 2, 'duas': 2, 'três': 3, 'quatro': 4, 'cinco': 5, 'seis': 6, 'sete': 7, 'oito': 8, 'nove': 9,
          'dez': 10, 'onze': 11, 'doze': 12, 'treze': 13, 'catorze': 14, 'quinze': 15, 'dezesseis': 16, 'dezessete': 17,
          'dezoito': 18, 'dezenove': 19}
    _Z = {'vinte': 20, 'trinta': 30, 'quarenta': 40, 'cinquenta': 50, 'sessenta': 60, 'setenta': 70, 'oitenta': 80, 'noventa': 90}
    _mc = re.search(r'([A-Za-zçãéêíóú]+(?: e [a-zçãéêíóú]+)?) Melhorias, em nove Famílias', _docx_m)
    if not _mc:
        _erro_n('o .docx parou de escrever por extenso "N Melhorias, em nove Famílias"')
    else:
        _pal = _mc.group(1).lower().split(' e ')
        _val = (_Z.get(_pal[0], 0) + _U.get(_pal[1], 0)) if len(_pal) == 2 else (_U.get(_pal[0]) or _Z.get(_pal[0]))
        if _val != _n_melhorias:
            _erro_n(f'o .docx escreve "{_mc.group(1)}" ({_val}) Melhorias e as tabelas do catalogo tem {_n_melhorias} linhas')
if _ok4n:
    print(f'    [x] as duas linhas e a tabela de duracao do .docx estao no capitulo 9 e no texto compilado; a Condicao diz que a '
          f'duracao pode ser trocada; o capitulo 2 e o glossario falam delas; "{_mc.group(1) if _mc else "?"} Melhorias" '
          f'e o que as tabelas contam ({_n_melhorias}).')


# 4o. v0.255: o `Alvo de Caça` (a Melhoria de buff de dano, na Familia `Marca`), a frase que
# faltava no `Efeito Próprio` e a regra do combo. O .docx e' o dono da linha e do texto; a peca 3
# e' dona da regra, e o conferir-acao.py (checagem 9) deriva o preco e as tabelas. Esta checagem
# guarda as COPIAS: o capitulo 9 do livro, o texto compilado, o glossario, as tres copias da frase
# do `Efeito Próprio` e o paragrafo do combo. A contagem de Melhorias por extenso ja e' da 4n.
print()
print('  4o. o `Alvo de Caça`, o `Efeito Próprio` que conta, e a regra do combo')

_ok4o = True


def _erro_o(msg):
    global _ok4o
    _ok4o = False
    erro(f'4o: {msg}')


# --- o dono: a linha do `Alvo de Caça` e a tabela em que ela mora ---
_adc_d, _fam_d = None, None
for _t in _D.tables:
    _cab = [c.text.strip() for c in _t.rows[0].cells] if _t.rows else []
    if _cab[:3] == ['Melhoria', 'Custo', 'O que faz']:
        _nomes = [_r.cells[0].text.strip() for _r in _t.rows]
        for _r in _t.rows[1:]:
            _v = [c.text.strip() for c in _r.cells]
            if _v[0] == 'Alvo de Caça':
                _adc_d, _fam_d = (_v[1], _v[2]), _nomes
if _adc_d is None:
    _erro_o('nao achei a linha do `Alvo de Caça` no .docx — ela e a dona de tudo que vem abaixo')
elif 'Marca' not in _fam_d:
    _erro_o(f'a linha do `Alvo de Caça` nao esta na tabela da Familia `Marca`: {_fam_d}')
else:
    # --- as copias da linha: cap. 9 e texto compilado ---
    for _onde, _t in (('o capitulo 9 do livro', _le_m('manual', '40-fundamento.md')),
                      ('o texto compilado do livro', _le_m('Projeto-M-Manual-da-Guilda-TEXTO.md'))):
        if _t is None:
            print(f'    ~~ {_onde} nao existe: as copias dele nao foram conferidas')
            continue
        _achou = None
        for _l in _t.split('\n'):
            _m = re.match(r'^\|\s*`Alvo de Caça`\s*\|\s*`?([^|`]+?)`?\s*\|\s*(.*?)\s*\|\s*$', _l)
            if _m:
                _achou = (_m.group(1).strip(), _semmd(_m.group(2)))
        if _achou is None:
            _erro_o(f'{_onde} nao tem a linha do `Alvo de Caça`')
        elif _achou != (_adc_d[0], _semmd(_adc_d[1])):
            _erro_o(f'{_onde}: a linha do `Alvo de Caça` difere do .docx: {_achou} contra '
                    f'{(_adc_d[0], _semmd(_adc_d[1]))}')
    # --- o glossario aponta para o capitulo 9 ---
    _glo = re.search(r'\|\s*\*\*`Alvo de Caça`\*\*\s*\|[^|]+\|\s*(\d+)\s*\|',
                     _le_m('manual', '07-glossario.md') or '')
    if not _glo or _glo.group(1) != '9':
        _erro_o('o glossario nao tem a entrada do `Alvo de Caça` apontando para o capitulo 9')

# --- o `Efeito Próprio` conta como Melhoria: as TRES copias, nos dois documentos ---
_FRASE_EP = 'conta como uma Melhoria'
_COPIAS_EP = (
    ('a linha do catalogo', 'Um por feitiço'),
    ('a frase depois da tabela de limite', 'A Forma não conta como Melhoria.'),
    ('a regra de ouro 3', 'Restrições: até 2.'),
)
for _onde, _txt in (('o .docx', _docx_m), ('o capitulo 9 do livro', _c9m)):
    for _rot, _anc in _COPIAS_EP:
        _linhas = [_l for _l in _txt.split('\n') if _anc in _l]
        if not _linhas:
            _erro_o(f'{_onde}: nao achei {_rot} (a ancora "{_anc}" sumiu)')
        elif not any(_FRASE_EP in _l or 'o Efeito Próprio conta' in _l for _l in _linhas):
            _erro_o(f'{_onde}: {_rot} nao diz que o `Efeito Próprio` conta como Melhoria')
    # a frase antiga: "Um por feitiço" sem dizer que conta e' a redacao que a v0.255 tirou
    for _l in _txt.split('\n'):
        if 'Um por feitiço' in _l and _FRASE_EP not in _l:
            _erro_o(f'{_onde} ainda tem "Um por feitiço" sem "{_FRASE_EP}": {_l.strip()[:90]}')

# --- o paragrafo do combo, com as tres frases-chave ---
_CHAVES = ('duas Melhorias escritas como uma', 'soma dos preços', 'por conta e risco', 'não recomenda')
for _onde, _txt in (('o .docx', _docx_m), ('o capitulo 9 do livro', _c9m)):
    _par = [_l for _l in _txt.split('\n') if 'Duas Melhorias escritas como uma' in _l]
    if not _par:
        _erro_o(f'{_onde} nao tem o paragrafo do combo ("Duas Melhorias escritas como uma")')
        continue
    for _k in _CHAVES[1:]:
        if not any(_k in _l for _l in _par):
            _erro_o(f'{_onde}: o paragrafo do combo nao diz "{_k}"')

if _ok4o:
    print(f'    [x] a linha do `Alvo de Caça` ({_adc_d[0]}) esta na tabela da `Marca` do .docx, no '
          f'capitulo 9 e no texto compilado, e o glossario aponta para o 9; o `Efeito Próprio` diz '
          f'que conta nas tres copias dos dois documentos; o paragrafo do combo tem as frases-chave.')


# --------------------------------------------------------------------------
bloco('5. O PORTAO DAS LINHAS DE CONTROLE — quem prende o alvo diz como solta')
# --------------------------------------------------------------------------
# v0.151. O `Cerca` passou nove versoes sendo a UNICA linha de Controle que
# prendia um alvo e nao dizia como aquilo acaba: o `Prende` cobra acao mais Teste
# de Resistencia, o `Anteparo` tem pontos de vida, o `Desarma o Feitico` tem
# portao de Classe, e as condicoes `Pesada` dao Teste de Resistencia no fim de
# cada turno. Ele nao tinha nada, e custava metade do `Prende`.
#
# ⚠ A classificacao NAO esta escrita aqui dentro. Quem escolhe as linhas que
# precisam de portao e' o texto do proprio manual: a linha fala do ALVO, e ela
# dura alem do instante. `Terreno` e `Anteparo` falam da area e da parede;
# `Puxa` e `Desarma o Feitico` acontecem e acabam. Nenhum dos quatro entra, e
# nenhum deles esta nomeado neste arquivo.

_tc = _tabela_com(['Melhoria', 'O que faz'])
_ctrl = []
if _tc is None:
    erro('5: nao achei a tabela de Melhorias no .docx — a checagem do portao de '
         'Controle ficou sem chao')
else:
    # o catalogo tem uma tabela por Familia, todas com o mesmo cabecalho: a de
    # Controle e' a que carrega a Melhoria `Condicao`.
    for _t5 in _D.tables:
        _h5 = ' | '.join(c.text.strip() for c in _t5.rows[0].cells)
        if 'Melhoria' not in _h5 or 'O que faz' not in _h5:
            continue
        _linhas5 = [[c.text.strip() for c in r.cells] for r in _t5.rows[1:]]
        if any(l and l[0] == 'Condição' for l in _linhas5):
            _ctrl = _linhas5
            break

if not _ctrl:
    erro('5: nao achei a tabela de Controle no .docx (a que carrega a Melhoria '
         '`Condição`) — ou o catalogo mudou de forma, ou a extracao parou de achar')
elif len(_ctrl) != 7:
    erro(f'5: a tabela de Controle tem {len(_ctrl)} linha(s) e eu esperava 7 — a '
         'familia mudou de tamanho e esta checagem parou de cobrir ela')
else:
    _DURA = (r'até o fim do próximo turno', r'por uma rodada', r'por 1 minuto',
             r'Dura uma rodada')
    _SAI = (r'Teste de Resistência', r'pontos de vida', r'Acaba', r'se soltar')
    _presos, _sem = [], []
    for _nome5, _custo5, _txt5 in _ctrl:
        _fala_do_alvo = re.search(r'\bO alvo\b|\bAplica uma\b', _txt5)
        _dura = any(re.search(_d, _txt5) for _d in _DURA)
        if not (_fala_do_alvo and _dura):
            continue
        _presos.append(_nome5)
        if not any(re.search(_s, _txt5) for _s in _SAI):
            _sem.append(_nome5)
    if len(_presos) < 3:
        erro(f'5: so {len(_presos)} linha(s) de Controle prendem um alvo por mais de '
             'um instante, e eu esperava pelo menos 3 (`Condição`, `Prende` e '
             '`Cerca`) — a selecao perdeu o chao e esta checagem parou de cobrir')
    elif _sem:
        erro('5: ' + ', '.join(f'`{n}`' for n in _sem) + ' prende(m) o alvo por mais '
             'de um instante e nao diz(em) como aquilo acaba — toda linha de Controle '
             'que segura alguem tem de nomear a saida, senao ela e um portao a menos '
             'pelo mesmo preco')
    else:
        print(f'  {len(_presos)} linha(s) de Controle seguram o alvo alem do instante: '
              + ', '.join(_presos))
        print('  e as ' + str(len(_presos)) + ' nomeiam a saida.')
        _fora = [n for n, _, _ in _ctrl if n not in _presos]
        print('  fora da selecao, por nao segurarem alvo nenhum: ' + ', '.join(_fora))


# --------------------------------------------------------------------------
# 6: os cinco degraus de nivel 7, comparados entre si.
#
# v0.155. O degrau do nivel 7 existe para que os cinco Caminhos recebam a mesma
# coisa, e ate aqui nada conferia isso — a regra dizia "vale exatamente o vao" e
# o vao deixou de ser um numero quando a v0.147 devolveu o ataque extra a Acao
# de Atacar. Hoje a peca 6 §3.1 publica os tres totais e declara a diferenca.
#
# Nenhum numero mora aqui: os tres saem da tabela da peca, e o teto da diferenca
# sai da frase que o declara.
# v0.158: este rotulo era `print('  6. os cinco degraus ...')`, em minuscula e
# fora do `bloco()`. O extrator da checagem 9 do conferir-repositorio.py exige
# LETRA MAIUSCULA depois do numero, entao ele nao via este bloco: a contagem do
# projeto publicava 258 e o codigo tinha 257, desde a v0.155. A guarda daquela
# checagem procura BURACO e REPETICAO, e nenhuma das duas abre aqui — o bloco
# simplesmente nao existia para ela.
bloco('6. OS CINCO DEGRAUS DE NIVEL 7 — a diferenca declarada')

_t6 = open(_p6, encoding='utf-8').read() if os.path.exists(_p6) else ''
_tot = {}
for _l in _t6.split('\n'):
    _m = re.match(r'>?\s*\|\s*\*\*(Bastião|Vanguarda)\*\*\s*\|[^|]*\|'
                  r'\s*`([\d,]+)`\s*\|\s*`([\d,]+)`\s*\|\s*\*\*`([\d,]+)`\*\*\s*\|', _l)
    if _m:
        _tot[_m.group(1)] = float(_m.group(4).replace(',', '.'))
_mg = re.search(r'Guia · Emanador · Evocador \| o degrau grande \| — \| — \| `([\d,]+)` \|', _t6)
_grande = float(_mg.group(1).replace(',', '.')) if _mg else None
_md = re.search(r'Bastião `−([\d,]+)` e Vanguarda `−([\d,]+)` contra o degrau grande', _t6)

if len(_tot) != 2 or _grande is None or not _md:
    erro('6: nao consegui ler os tres totais do nivel 7 na peca 6 §3.1 — a tabela '
         'ou a linha da diferenca declarada mudou de forma, e esta checagem parou '
         'de conferir em vez de acusar')
else:
    _db = float(_md.group(1).replace(',', '.'))
    _dv = float(_md.group(2).replace(',', '.'))
    print(f"     Bastiao {_tot['Bastião']:.2f} · Vanguarda {_tot['Vanguarda']:.2f} · "
          f"os outros tres {_grande:.2f}")
    _erro_b = abs((_grande - _tot['Bastião']) - _db)
    _erro_v = abs((_grande - _tot['Vanguarda']) - _dv)
    if _erro_b > 0.005 or _erro_v > 0.005:
        erro(f'6: a peca declara a diferenca em -{_db:.2f} e -{_dv:.2f}, e os totais '
             f'dao -{_grande-_tot["Bastião"]:.2f} e -{_grande-_tot["Vanguarda"]:.2f} '
             f'— a tabela e a frase divergiram')
    elif max(_db, _dv) > 0.50:
        erro(f'6: a diferenca declarada chegou a {max(_db,_dv):.2f} fatia, e o degrau '
             f'do nivel 7 existe para os cinco receberem a mesma coisa — acima de '
             f'0,50 ela deixa de ser residuo e vira degrau desigual')
    else:
        print('     [x] os totais batem com a diferenca declarada, e ela cabe no teto.')


# --------------------------------------------------------------------------
bloco('7. A COBERTURA — o manual cita o grau, e a escala e da peca 19 §5')
# --------------------------------------------------------------------------
# v0.162. Duas entradas PRECADAS do manual compravam "furar cobertura" contra
# graus que este sistema nao tem: a Melhoria `Sem Cobertura` (`Leve`) dizia
# "cobertura leve e meia cobertura", e a Passiva `Afinidade` (Classe 3) dizia
# "cobertura leve". Rastreados nos PDFs de referencia: `cobertura leve` e' do
# GURPS 4e, onde nem grau e' — la e' um -2 de tiro —, e `meia cobertura` e' o
# half cover do D&D 2014. A escala DESTE sistema e a do D&D 2024, renomeada:
# `Parcial` . `Boa` . `Total`, na peca 19 §5.
#
# ⚠ A escala NAO esta escrita aqui: ela e lida da peca. O que este bloco proibe
# e' o manual nomear um grau que a peca nao tem — e proibe tambem o contrario,
# o manual COPIAR os bonus. Copia sem comparacao diverge (licao no 9), e o
# molde de "apontar e nao copiar" e o da v0.159 com a Integridade.
_p19 = os.path.join(AQUI, '19-dano-e-condicoes.md')
if not os.path.exists(_p19):
    erro('7: nao achei a peca 19 — a escala de cobertura ficou sem dono e esta '
         'checagem nao tem contra o que comparar')
else:
    _t19 = open(_p19, encoding='utf-8').read()
    _sec = _t19[_t19.find('\n## 5. Cobertura'):]
    _sec = _sec[:_sec.find('\n## ', 1)] if '\n## ' in _sec[1:] else _sec
    _GRAUS, _BONUS = [], []
    for _l in _sec.splitlines():
        _m = re.match(r'\|\s*\*\*([A-Za-zÀ-ÿ]+)\*\*\s*\|\s*\*\*(.+?)\*\*\s*\|', _l)
        if _m:
            _GRAUS.append(_m.group(1))
            _BONUS += re.findall(r'\+(\d+)', _m.group(2))
    # guarda de reconhecedor: sem ela, renomear a secao faz esta checagem achar
    # zero grau, logo zero divergencia, e ela passa verde para sempre.
    if len(_GRAUS) < 3 or not _BONUS:
        erro(f'7: li {len(_GRAUS)} grau(s) e {len(set(_BONUS))} bonus na §5 da peca 19 '
             'e esperava tres graus com bonus — a tabela mudou de forma, e a '
             'comparacao abaixo passaria verde sem conferir nada')
    else:
        print(f'  a escala, lida da peca 19 §5: {" · ".join(_GRAUS)}')
        # palavras que podem encostar em "cobertura" sem serem grau
        _LIGACAO = {
            'e', 'ou', 'de', 'do', 'da', 'em', 'no', 'na', 'que', 'se', 'a', 'o',
            'as', 'os', 'ao', 'à', 'nao', 'não', 'nem', 'para', 'por', 'com',
            'contra', 'alem', 'além', 'sem', 'um', 'uma', 'ignora', 'ignoram',
            'fura', 'furam', 'atrapalha', 'atrapalham', 'continua', 'tem', 'ha',
            'há', 'sua', 'seu', 'esta', 'está', 'dele', 'dela', 'mais', 'toda',
        }
        _norm = {g.lower() for g in _GRAUS}
        _maus, _copias, _vistos = [], [], 0
        for _onde, _txt in LINHAS:
            if not re.search(r'[Cc]obertura', _txt):
                continue
            _vistos += 1
            _viz = (re.findall(r'[Cc]obertura\s+([A-Za-zÀ-ÿ]+)', _txt)
                    + re.findall(r'([A-Za-zÀ-ÿ]+)\s+[Cc]obertura', _txt))
            for _w in _viz:
                if _w.lower() in _LIGACAO or _w.lower() in _norm:
                    continue
                _maus.append((_onde, _w, _txt.strip()[:110]))
            for _b in set(_BONUS):
                if re.search(rf'\+{_b}\s+(de\s+)?(Defesa|CA)', _txt):
                    _copias.append((_onde, _b, _txt.strip()[:110]))
        if _vistos == 0:
            erro('7: a palavra "cobertura" sumiu do manual inteiro — ou o texto '
                 'mudou, ou esta checagem parou de achar o que confere')
        elif _maus:
            for _onde, _w, _txt in _maus:
                print(f'     {_onde}: grau "{_w}" — {_txt}')
            erro(f'7: o manual nomeia {len(_maus)} grau(s) de cobertura que a peca 19 '
                 f'§5 nao tem. A escala e {" · ".join(_GRAUS)}, e dois mestres nao '
                 'chegam ao mesmo lugar lendo um grau que a regra nao define — '
                 'as duas entradas que fazem isso sao PRECADAS')
        elif _copias:
            for _onde, _b, _txt in _copias:
                print(f'     {_onde}: copia o +{_b} — {_txt}')
            erro(f'7: o manual COPIA {len(_copias)} bonus de cobertura que a peca 19 §5 '
                 'e dona. Ele deve apontar o grau pelo nome e nao repetir o numero, '
                 'no molde da Integridade na v0.159 — copia sem comparacao diverge')
        else:
            print(f'  [x] as {_vistos} linhas do manual que falam de cobertura citam '
                  f'so os graus da peca,')
            print(f'      e nenhuma repete os bonus ({" · ".join("+" + b for b in dict.fromkeys(_BONUS))}) '
                  'que sao dela.')

# --------------------------------------------------------------------------
bloco('8. A CURA COMECA NA CLASSE 1 — e a Classe 0 nao pode ter uma')
# --------------------------------------------------------------------------
# v0.166. Achado do Mizuki: a regra da Classe 0 diz "nao se montam: escolha uma
# Forma e pronto", e `Cura` E uma Forma. A coluna `Custa` da tabela de Formas
# (`Cura` = Media, `Onda` = Pesada) nunca era aplicada, porque uma Classe 0 nao
# tem orcamento de onde pagar. Entao um Classe 0 com Forma `Cura` entregava
# 6d8 = 27 de cura POR RODADA, de graca, EM ALIADO, no nivel 30 — 5,31 fatias,
# que e 1,06 Trilha inteira. E a peca 11 §6 escreve que curar terceiro e o degrau
# RARO do material, pago pela Trilha `Sutura` no nivel 11 dela.
#
# ⚠ Nao era mudanca de regra: era CONTRADICAO DENTRO DO MANUAL. A tabela de cura
# dele comeca na Classe 1 — nunca houve cura de Classe 0 precada. Quem abria o
# buraco era a tabela `Base por Classe`, que juntava `Cura, Apoio e Onda` numa
# linha so e dava a ela uma coluna `Classe 0`; o `Apoio` custa `—` e pertence
# ali, as outras duas nao.
#
# NADA DA DECISAO MORA AQUI. Esta checagem le da tabela de cura DO PROPRIO MANUAL
# quais Classes curam, e cobra que a `Base por Classe` concorde. Ela falha nas
# DUAS direcoes: coluna `Classe 0` viva numa Forma de cura acende, e cura de
# Classe 0 precada sem a coluna correspondente tambem. Mudar os dois de forma
# coerente sai VERDE de proposito — e' esse o contra-teste.
#
# E o que ela NAO cobra, declarado: a FRASE do texto. Apagar o paragrafo
# "Classe 0 nao cura" sai verde, e e de proposito — exigir frase literal e' a
# armadilha da "frase morta EXIGIDA por um validador", que nunca mais sai.
# Quem manda aqui e a TABELA; o paragrafo e placa, e placa nao e dono.
# Arnes da v0.166: 10 perturbacoes, 8 acendendo e 2 contra-testes verdes.
def _tabela_com_rotulo(rotulo):
    # ⚠ o `if not r.cells` nao e paranoia: sem ele esta funcao ESTOURA numa tabela
    # com linha vazia, e o arnes pegou isso. Guarda que acusa e estoura logo
    # depois e' o defeito da v0.161 — a checagem morre antes de dizer o que viu.
    for t in _D.tables:
        for r in t.rows[1:]:
            if not r.cells:
                continue
            if r.cells[0].text.strip().startswith(rotulo):
                return t
    return None


_tc = _tabela_com_rotulo('Cura cheia')
_tb = _tabela_com(['Forma', 'Classe 0'])
if _tc is None or _tb is None:
    erro('8: nao achei a tabela de cura ("Cura cheia") ou a "Base por Classe" no '
         'manual — sem as duas esta checagem nao tem o que comparar, e passaria '
         'verde sem conferir nada')
else:
    # 8a. quais Classes o manual preca cura, lido do cabecalho da tabela de cura
    _CL_CURA = []
    for _c in _tc.rows[0].cells[1:]:
        _m = re.fullmatch(r'\s*(\d+)\s*', _c.text)
        if _m:
            _CL_CURA.append(int(_m.group(1)))
    # as Formas que aquela tabela governa saem dos ROTULOS dela, e nao de lista minha
    _FORMAS_CURA = []
    for _r in _tc.rows[1:]:
        _rot = _r.cells[0].text.strip()
        _m = re.match(r'([A-Za-zÀ-ÿ]+)', _rot)
        if _m and 'Dano' not in _rot:
            _FORMAS_CURA.append(_m.group(1))
    # guarda de reconhecedor
    if not _CL_CURA or len(_FORMAS_CURA) < 2:
        erro(f'8: li {len(_CL_CURA)} Classe(s) e {len(_FORMAS_CURA)} Forma(s) na tabela '
             'de cura do manual, e esperava pelo menos uma Classe e duas Formas — '
             'a tabela mudou de forma, e a comparacao abaixo nao provaria nada')
    else:
        _CURA_NA_0 = 0 in _CL_CURA
        print(f'  a tabela de cura do manual preca as Classes: '
              f'{" · ".join(str(c) for c in _CL_CURA)}')
        print(f'  e as Formas que ela governa, lidas dos rotulos dela: '
              f'{" · ".join(_FORMAS_CURA)}')
        print(f'  => cura de Classe 0 e {"PRECADA" if _CURA_NA_0 else "inexistente"} '
              'no manual')
        # 8b. a `Base por Classe` tem de concordar com isso
        _hdr = [c.text.strip() for c in _tb.rows[0].cells]
        try:
            _col0 = next(i for i, h in enumerate(_hdr) if re.fullmatch(r'Classe\s*0', h))
        except StopIteration:
            _col0 = None
        if _col0 is None:
            erro('8: a tabela "Base por Classe" perdeu a coluna `Classe 0` — sem ela '
                 'nao da para conferir se uma Forma de cura tem alcance ali')
        else:
            _vazio = re.compile(r'^\s*(—|-|–|n/?a|\.)?\s*$', re.I)
            _acusa, _conferidas = [], 0
            for _r in _tb.rows[1:]:
                _rot = _r.cells[0].text.strip()
                _quais = [f for f in _FORMAS_CURA
                          if re.search(rf'\b{re.escape(f)}\b', _rot)]
                if not _quais:
                    continue
                _conferidas += 1
                _cel = _r.cells[_col0].text.strip()
                _tem = not _vazio.match(_cel)
                if _tem != _CURA_NA_0:
                    _acusa.append((_rot, _quais, _cel or '(vazio)'))
            if _conferidas == 0:
                erro('8: nenhuma linha da "Base por Classe" nomeia uma Forma de cura. '
                     'Ou a tabela foi renomeada, ou esta checagem parou de achar o '
                     'que ela confere — nos dois casos ela passaria verde a toa')
            elif _acusa:
                for _rot, _quais, _cel in _acusa:
                    print(f'     linha "{_rot}" ({" · ".join(_quais)}): '
                          f'Classe 0 = {_cel}')
                if _CURA_NA_0:
                    erro(f'8: o manual preca cura de Classe 0 na tabela de cura, e a '
                         f'"Base por Classe" nao da alcance de Classe 0 para '
                         f'{len(_acusa)} Forma(s) de cura. As duas tem de dizer a '
                         'mesma coisa')
                else:
                    erro(f'8: a tabela de cura do manual comeca na Classe '
                         f'{min(_CL_CURA)}, mas a "Base por Classe" da alcance de '
                         f'Classe 0 para {len(_acusa)} Forma(s) de cura. Um Classe 0 '
                         'com Forma de cura sai de graca e toda rodada, EM ALIADO — '
                         'e curar terceiro e o degrau que a Trilha `Sutura` paga uma '
                         'Trilha inteira por, no nivel 11 dela (peca 11 §6)')
            else:
                print(f'  [x] as {_conferidas} linha(s) da "Base por Classe" que nomeiam '
                      f'Forma de cura concordam')
                print(f'      com a tabela de cura: alcance de Classe 0 '
                      f'{"existe" if _CURA_NA_0 else "nao existe"} nos dois lugares.')

# --------------------------------------------------------------------------
bloco('8.1 A BASE POR CLASSE COBRE AS FORMAS — e a do Corpo a Corpo herda o raio')
# --------------------------------------------------------------------------
# v0.263. A tabela tinha seis linhas e a Aura, uma das dez Formas, nao estava em
# nenhuma: a descricao dela diz "raio 3 m", que e o valor das Classes 1 a 5, e
# nas Classes 6 e 7 ninguem sabia se ela ia a 4,5 m como a Explosao. Decisao do
# Mizuki em 21/09/2026: acompanha a Explosao. E o raio nao e escolha — a Aura e
# "Explosao com Corpo a Corpo embutida", e o Corpo a Corpo muda ONDE a esfera
# nasce, nao o tamanho dela. Com raio fixo, a mesma Explosao com a Restricao
# comprada teria dois tamanhos conforme o caminho da montagem.
#
# Tres coisas, e nenhuma lista de Forma escrita aqui:
#  (a) toda Forma que mede alguma coisa em metros na tabela de Formas tem linha
#      na Base por Classe. A que nao mede — a Efeito, fora de combate — fica de
#      fora sozinha, sem estar nomeada neste arquivo.
#  (b) a Forma que e "<X> com [a Restricao] Corpo a Corpo embutida" tem, em cada
#      coluna, o mesmo RAIO que X. Se X nao tem raio (o Projetil), nao ha o que
#      herdar, e ela e conferida so por (a). Guarda: pelo menos uma heranca tem
#      de ser conferida, senao (b) passaria verde a toa.
#  (c) a tabela do capitulo 9 do livro diz o mesmo que a do manual, linha a
#      linha. Copia sem comparacao diverge — licao no 9.
_tf = _tabela_com(['Forma', 'Custa', 'O que é'])
if _tb is None or _tf is None:
    erro('8.1: nao achei a "Base por Classe" ou a tabela de Formas no manual — '
         'sem as duas nao ha o que comparar')
else:
    def _limpa81(s):
        return re.sub(r'[`*]', '', s).strip()

    _formas81 = {}
    for _r in _tf.rows[1:]:
        _c = [c.text.strip() for c in _r.cells]
        if _c and _c[0]:
            _formas81[_c[0]] = _c[2] if len(_c) > 2 else ''
    _base81 = {}
    for _r in _tb.rows[1:]:
        _c = [c.text.strip() for c in _r.cells]
        if _c and _c[0]:
            _base81[_limpa81(_c[0])] = [_limpa81(x) for x in _c[1:]]

    def _linha81(forma):
        return next((r for r in _base81
                     if re.search(rf'(?<![\wÀ-ÿ]){re.escape(forma)}(?![\wÀ-ÿ])', r)), None)

    # (a)
    _medem = [f for f, d in _formas81.items() if re.search(r'\d\s*m\b', d)]
    _sem = [f for f in _medem if _linha81(f) is None]
    if len(_formas81) < 8 or not _medem:
        erro(f'8.1: li {len(_formas81)} Forma(s), {len(_medem)} com medida — a tabela '
             'de Formas mudou de forma e (a) nao provaria nada')
    elif _sem:
        erro(f'8.1: {len(_sem)} Forma(s) medem alguma coisa na tabela de Formas e nao '
             f'tem linha na "Base por Classe": {" · ".join(_sem)}')
    else:
        _fora = [f for f in _formas81 if f not in _medem]
        print(f'  [x] as {len(_medem)} Formas que medem alguma coisa tem linha na '
              f'"Base por Classe"; fora dela, por nao medir: {" · ".join(_fora) or "nenhuma"}')

    # (b)
    _raio = lambda cels: [re.findall(r'raio\s+([\d,]+)\s*m', c) for c in cels]
    _herdadas = 0
    for f, d in _formas81.items():
        m = re.search(r'([A-Za-zÀ-ÿ]+) com (?:a Restrição )?Corpo a Corpo embutida', d)
        if not m:
            continue
        x = m.group(1)
        lf, lx = _linha81(f), _linha81(x)
        if lx is None:
            erro(f'8.1: a {f} e "{x} com Corpo a Corpo", e a {x} nao tem linha na '
                 '"Base por Classe"')
            continue
        rx = _raio(_base81[lx])
        if not any(rx):
            print(f'   - a {f} e {x} com Corpo a Corpo, e a {x} nao tem raio: nada a herdar')
            continue
        if lf is None or lf == lx:
            erro(f'8.1: a {f} e {x} com Corpo a Corpo e nao tem linha propria na '
                 '"Base por Classe" — o raio dela nas Classes 6 e 7 fica sem dono')
            continue
        rf81 = _raio(_base81[lf])
        _herdadas += 1
        if rf81 != rx:
            erro(f'8.1: a {f} tem raio {rf81} por coluna e a {x} tem {rx} — o Corpo a '
                 'Corpo muda onde a esfera nasce, e nao o tamanho dela')
        else:
            print(f'  [x] a {f} tem o raio da {x} em toda coluna: '
                  f'{" · ".join("/".join(r) + " m" for r in rf81)}')
    if _herdadas == 0:
        erro('8.1: nenhuma Forma com raio herdado foi conferida — a frase "com Corpo '
             'a Corpo embutida" mudou ou a Forma sumiu, e (b) passaria verde a toa')

    # (c) a copia do livro
    _l9 = ''
    try:
        _l9 = open(os.path.join(AQUI, '..', '05-material', 'livro', 'manual',
                                '40-fundamento.md'), encoding='utf-8').read()
    except FileNotFoundError:
        pass
    _i = _l9.find('**Base por Classe**')
    _tab9 = []
    if _i >= 0:
        for _ln in _l9[_i:].splitlines()[1:]:
            if _ln.startswith('|'):
                _tab9.append(_ln)
            elif _tab9:
                break
    if len(_tab9) < 3:
        erro('8.1: nao achei a "Base por Classe" no capitulo 9 do livro')
    else:
        _liv81 = {}
        for _ln in _tab9[2:]:
            _c = [x.strip() for x in _ln.strip().strip('|').split('|')]
            _liv81[_limpa81(_c[0])] = [_limpa81(x) for x in _c[1:]]
        _so_man = [k for k in _base81 if k not in _liv81]
        _so_liv = [k for k in _liv81 if k not in _base81]
        _dif = [k for k in _base81 if k in _liv81 and _base81[k] != _liv81[k]]
        if _so_man or _so_liv or _dif:
            erro(f'8.1: a "Base por Classe" do livro e a do manual discordam — so no '
                 f'manual: {_so_man}; so no livro: {_so_liv}; linhas diferentes: {_dif}')
        else:
            print(f'  [x] a tabela do capitulo 9 do livro e a do manual batem nas '
                  f'{len(_base81)} linhas')

# --------------------------------------------------------------------------
print()
print('=' * 88)
if FALHAS:
    print(f'>>> {len(FALHAS)} PROBLEMA(S):')
    for e in FALHAS:
        print('   -', e)
    sys.exit(1)
print('>>> TUDO OK — nenhum vocabulario de outro sistema no manual, nenhum termo')
print('    mecanico indefinido sem motivo, e os numeros importados continuam batendo.')
if AVISOS:
    print(f'    {len(AVISOS)} aviso(s) acima, que nao falham o validador.')

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

Quatro checagens:
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
Sem python-docx, as quatro checagens sao PULADAS com aviso, em vez de falhar.
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
    print('~~ python-docx nao instalado. As quatro checagens foram PULADAS.')
    print('   pip install python-docx --break-system-packages')
    sys.exit(0)

if not os.path.exists(DOCX):
    print(f'~~ manual nao encontrado em {DOCX}. As quatro checagens foram PULADAS.')
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
    'cobertura leve': (
        r'cobertura leve',
        'a Passiva Afinidade fura cobertura leve. Cobertura e conceito de tabuleiro '
        'e mora na peca de equipamento, que ainda nao existe. Reavaliar quando ela sair.'),
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
CHEFE_NO_PROJETO = {5: 15, 10: 26, 15: 38, 20: 49, 25: 61, 30: 72}
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

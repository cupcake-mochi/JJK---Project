# -*- coding: utf-8 -*-
"""
conferir-invocacoes.py — o validador da peca 15 (Invocacoes).

NADA DE VALOR FICA ESCRITO AQUI. O teto da Rotina somada e a cota por corpo saem
da PECA 6 SS4; a Rotina por nivel sai da PECA 6 SS3; os marcos e os tetos saem da
PECA 2; a formula de vida, o PE por nivel e a maestria saem da PECA 1; a amarra
sai da PECA 3 SS3 (o alcance base de Projetil); o ritmo do refino sai da PECA 11
SS2; o ponto de arma sai da PECA 14 SS5; o PISO do bolso sai do
conferir-orcamento.py, que e quem ja sabe medir isso. O catalogo, a regua e o
orcamento saem da propria peca 15.

O unico bloco com valor na mao e o LIMITES DE DESIGN, declarado a parte da regra
aplicada — licao no 8: uma checagem nao pode se medir contra a propria constante.

Trinta checagens, na ordem do SS5 da peca:
   1. TETO-ROTINA   — o teto somado vem da peca 6 SS4 e nunca de constante.
   2. DOMINANCIA    — a matriz entre as tres Trilhas, por quantidade de corpos.
   3. SOMATORIO     — invocar cabe no bolso junto do resto que drena PE.
   4. TEMPO-DE-MESA — a tabela de rolagens fecha, e o numero esperado esta escrito.
   5. TRIAGEM       — todo nome que a peca cria aparece no argumento, e nenhum
                      esta na lista de OCUPADO que a propria peca levantou.
   6. REGUA         — toda entrada cai no degrau que a regua da criacao manda.
   7. ILEGAIS       — nenhuma entrada com dado de dano, refino ou deslocamento +.
   8. DESLOCAMENTO  — nenhuma linha da ficha sobe acima do numero do dono.
   9. ORCAMENTO     — derivado dos marcos da peca 2, nunca lido de constante.
  10. DUAS-MOEDAS   — ponto de arma e ponto de ficha nao se convertem.
  11. AREA          — o multiplicador sai do documento, e o pool nao se apaga.
  12. MORTE         — os dois gatilhos, e nenhum golpe de rotina dispara.
  13. PRECO         — o preco de invocar medido contra o BASTIAO, nao o Evocador.
  14. ECONOMIA      — o teto cai da economia de acao, e nao de decreto.
  15. CORO          — a excecao medida somada nao passa de uma Rotina.
  16. BUSCA         — todas as montagens legais: gasto exato e zero dominadas.
  17. INSTANCIAS    — as montagens publicadas conferidas contra a maquina.
  18. RITMO         — nenhuma linha derivada cresce fora do +3.
  19. VIDA          — a formula no molde da peca 1, e a tabela recalculada.
  20. POOL          — a invariante da Q2: ninguem ganha barra de vida propria.
  21. COTA          — 1/n lido da peca 6 SS4, com n = corpos no campo.
  22. CRITICO       — 22,6% de chance e 5% de Rotina; o pacote unico salta a 23%.
  23. INICIATIVA    — a invariante da Q1: ninguem ganha casa separada.
  24. AMARRA        — os 18 m lidos da peca 3 SS3, nunca de constante.
  25. FAIXAS        — "na cena" e "fora da cena" nao ganham metro.
  26. GATE          — o gate do Remoto e o unico do catalogo.
  27. NAO-COMPRA    — nenhuma entrada compra linha que ja e deslocamento.
  28. CONTAGEM      — o catalogo recontado bate com o que o documento afirma.
  29. BUSCA-DEGRAU  — a busca por degrau bate com o numero escrito antes.
  30. PISO-DA-VENDA — vender deslocamento nao precisa de piso, e isso e medido.

Roda de sistema/03-mecanica/. NAO le o .docx e NAO precisa de python-docx —
entao nao existe caminho por onde ele saia verde tendo pulado checagem.
"""
import os, re, sys, unicodedata
from itertools import combinations

AQUI = os.path.dirname(os.path.abspath(__file__))


def ler(nome):
    with open(os.path.join(AQUI, nome), encoding='utf-8') as f:
        return f.read()


def sem_acento(t):
    return ''.join(c for c in unicodedata.normalize('NFD', t)
                   if unicodedata.category(c) != 'Mn').lower()


def num(t):
    """'38,5' -> 38.5 ; '1,40x' -> 1.4 ; devolve None se nao houver numero."""
    m = re.search(r'-?\d+(?:[.,]\d+)?', t.replace('−', '-'))
    return float(m.group(0).replace(',', '.')) if m else None


ERROS, AVISOS = [], []


def erro(c, m):
    ERROS.append(f'[{c}] {m}')


def aviso(m):
    AVISOS.append(m)


def bloco(t):
    print('\n' + '=' * 88 + f'\n{t}\n' + '=' * 88)


def limpo(x):
    """tira negrito e crase de UMA celula. Nao se usa na celula inteira quando ela
    carrega uma lista de nomes entre crases — foi assim que a primeira versao
    desta funcao comeu o ultimo nome de cada degrau da regua."""
    return x.strip().strip('*').strip('`').strip()


def linhas_de_tabela(txt):
    """Devolve as linhas de tabela de um trecho, ja quebradas em celulas.
    Tira negrito, e NAO tira crase — quem precisa chama limpo()."""
    out = []
    for l in txt.split('\n'):
        s = l.strip()
        if not s.startswith('|'):
            continue
        c = [x.strip().strip('*').strip() for x in s.strip('|').split('|')]
        if c and set(''.join(c)) <= set('-: '):
            continue
        out.append(c)
    return out


def trecho(txt, ini, fim=None, nome=''):
    try:
        a = txt.index(ini)
    except ValueError:
        erro('SETUP', f'nao achei o trecho "{ini}" {nome}')
        return ''
    if fim is None:
        return txt[a:]
    try:
        b = txt.index(fim, a)
    except ValueError:
        return txt[a:]
    return txt[a:b]


PECA = ler('15-invocacoes.md')
P1 = ler('01-atributos-acerto-defesa.md')
P2 = ler('02-economia-de-atributos.md')
P3 = ler('03-economia-de-acao-e-iniciativa.md')
P6 = ler('06-caminhos-e-trilhas.md')
P11 = ler('11-aptidoes-e-refino.md')
P14 = ler('14-equipamento.md')
ORC = ler('conferir-orcamento.py')

# ---------------------------------------------------------------- LIMITES DE DESIGN
# Declarados aqui, a parte da regra aplicada. Sao DECISOES REGISTRADAS, cada uma
# com o lugar onde o argumento dela mora. Perturbar qualquer um deles tem de
# acender a checagem correspondente — e nunca a mesma que le o valor do documento.
TRILHAS = ('Servo', 'Matilha', 'Coro')          # peca 6 SS2, ja batizadas
CORPOS_ESPERADOS = {'Servo': 1, 'Coro': 1, 'Matilha': 5}   # peca 6 SS4, so o formato
# O SS3.6 e o SS4 da peca levantaram estes como OCUPADOS na triagem. Nenhum nome
# do catalogo pode ser um deles. A lista e o resultado do conferir-nomes.py, nao
# uma opiniao — e quem confere nome contra o .docx e aquele validador, nao este.
OCUPADO_NA_TRIAGEM = {'Passiva', 'Natureza', 'Forma', 'Molde', 'Instinto',
                      'Enxame', 'Sombra', 'Provocar', 'Vinculo', 'Invocacao'}
# As tres coisas que a criacao nao compra a preco nenhum (SS3.7), com o dono de cada.
ILEGAL_DONO = {'dado de dano': 'peca 6 SS4',
               'refino': 'peca 11 SS2',
               'deslocamento positivo': 'SS3.6'}
CON_DA_TABELA = 0        # a tabela de vida do SS3.6 e impressa com Constituicao 0
# A Q6 FECHOU NA v0.63, e por isso este conjunto esta VAZIO.
# Ate a v0.62 ele carregava ('Matilha','Servo') e ('Coro','Servo') — as duas
# apontando para o Servo, porque "um corpo forte" nao tinha numero e ele nao
# ficava na frente em EIXO NENHUM. O conserto nao foi um numero: foi uma coluna
# nova na matriz. A Trilha concede orcamento e vida ao corpo, e as duas colunas
# saem da tabela "O que cada Trilha concede" do SS3.7 — nunca daqui.
# Se alguma dominancia voltar, a checagem 2 falha em vez de aceitar calada.
DOMINANCIA_PENDENTE_Q6 = set()
# Quantos pontos de deslocamento a ficha pode vender de uma vez, no pior caso
# medido no SS3.7. E um CENARIO de teste, nao uma regra: a peca nao poe teto.
VENDA_MEDIDA = 5
RODADAS_POR_LUTA = (10 / 3, 4.0)   # a banda que o SS3.2 usa por combate

# =============================================================================
# OS DONOS — tudo lido, nada escrito
# =============================================================================

# --- peca 6 SS4: o teto somado, e as cotas por Trilha ------------------------
S6_4 = trecho(P6, '## 4. Invocação: não passa como está', '## 5. Energia', 'peca 6 SS4')
m = re.search(r'\*\*Você e todas as suas invocações somados entregam \*?\*?(uma|duas|três) '
              r'Rotina', S6_4)
TETO_SOMADO = {'uma': 1, 'duas': 2, 'três': 3}[m.group(1)] if m else None
if TETO_SOMADO is None:
    erro('SETUP', 'peca 6 SS4: nao achei a frase do teto somado')

COTA = {}
for ln in S6_4.split('\n'):
    mm = re.match(r'- \*\*(Servo|Matilha|Coro)\*\* (.+)', ln)
    if not mm:
        continue
    nome, resto = mm.group(1), mm.group(2)
    mc = re.search(r'(metade|um quinto|um quarto|um terço) da Rotina em cada', resto)
    mn = re.search(r'(\d+|um|dois|três|quatro|cinco|seis|sete|oito|nove|dez) '
                   r'corpos? (?:a mais )?no campo', resto)
    fr = {'metade': 2, 'um terço': 3, 'um quarto': 4, 'um quinto': 5}
    esc = {'um': 1, 'dois': 2, 'três': 3, 'quatro': 4, 'cinco': 5,
           'seis': 6, 'sete': 7, 'oito': 8, 'nove': 9, 'dez': 10}
    corpos = None
    if mn:
        g = mn.group(1)
        corpos = esc[g] if g in esc else (int(g) if g.isdigit() else None)
        if corpos is None:
            erro('SETUP', f'peca 6 SS4: nao entendi "{g} corpos no campo" na linha do {nome}')
    COTA[nome] = dict(divisor=fr.get(mc.group(1)) if mc else None,
                      corpos=corpos, texto=resto)
for t in TRILHAS:
    if t not in COTA:
        erro('SETUP', f'peca 6 SS4: nao achei a linha da Trilha {t}')

# --- peca 6 SS3: a Rotina por nivel ------------------------------------------
ROTINA_NV = {}
for c in linhas_de_tabela(trecho(P6, '## 3. Ataque extra', '## 3.1 Quem ganha')):
    if len(c) >= 3 and re.fullmatch(r'\d+', limpo(c[0])) and re.fullmatch(r'\d+', limpo(c[1])):
        ROTINA_NV[int(limpo(c[0]))] = int(limpo(c[1]))
if len(ROTINA_NV) < 4:
    erro('SETUP', f'peca 6 SS3: esperava a coluna Rotina por nivel, achei {ROTINA_NV}')

# --- peca 2: marcos e tetos --------------------------------------------------
m = re.search(r'nos níveis \*\*([\d, e]+)\*\*, sete marcos', P2)
MARCOS = sorted(int(x) for x in re.findall(r'\d+', m.group(1))) if m else []
if len(MARCOS) != 7:
    erro('SETUP', f'peca 2: esperava sete marcos, achei {MARCOS}')
m = re.search(r'\*\*Teto do atributo: (\d+)\.\*\* Teto do refino: (\d+)\.', P2)
TETO_ATR, TETO_REF = (int(m.group(1)), int(m.group(2))) if m else (None, None)
if TETO_ATR is None:
    erro('SETUP', 'peca 2: nao achei os tetos de atributo e de refino')

# --- peca 1: vida, PE por nivel, maestria ------------------------------------
CAMINHOS = {}
for c in linhas_de_tabela(trecho(P1, '## 5.1 Pontos de vida', '## 5.2', 'peca 1 SS5.1')):
    if len(c) >= 5 and limpo(c[1]).startswith('d') and limpo(c[2]).isdigit():
        CAMINHOS[limpo(c[0])] = dict(vida1=int(limpo(c[2])), por_nivel=int(limpo(c[3])),
                                     pe=int(limpo(c[4])))
if len(CAMINHOS) != 5:
    erro('SETUP', f'peca 1 SS5.1: esperava os cinco Caminhos, achei {list(CAMINHOS)}')
m = re.search(r'\*\*Maestria\*\* começa em (\d+) e sobe um ponto a cada (\w+) níveis', P1)
MAESTRIA_INI = int(m.group(1)) if m else None
MAESTRIA_PASSO = {'oito': 8, 'quatro': 4, 'seis': 6}.get(m.group(2)) if m else None
if MAESTRIA_INI is None:
    erro('SETUP', 'peca 1 SS2: nao achei a regra da maestria')
# v0.117: o ataque de conjuracao deixou de ter fixo. Ele e `atributo + maestria`,
# e o atributo cresce +3 na campanha como qualquer atributo investido — que e
# exatamente o que a checagem 18 precisa saber para medir o ritmo do dono.
if not re.search(r'Ataque de conjuração\s*=\s*d20 \+ atributo da técnica \+ maestria', P1):
    erro('SETUP', 'peca 1: o ataque de conjuracao nao e mais `atributo da tecnica + '
                  'maestria` — a checagem 18 mede o ritmo do dono a partir dele')

# --- peca 3 SS3: o alcance base de Projetil, que e a amarra ------------------
m = re.search(r'O alcance base de Projétil é (\d+) m', P3)
PROJETIL = int(m.group(1)) if m else None
if PROJETIL is None:
    erro('SETUP', 'peca 3 SS3: nao achei o alcance base de Projetil')
m = re.search(r'\*\*Deslocamento base: (\d+) metros\.\*\*', P3)
DESLOC_BASE = int(m.group(1)) if m else None

# --- peca 11 SS2: o ritmo do refino ------------------------------------------
RITMO_REFINO = []
for c in linhas_de_tabela(trecho(P11, '## 2. A trava', '## 3. O marco', 'peca 11 SS2')):
    if len(c) >= 2 and 'refino' in c[0]:
        v = re.search(r'\+(\d+)', limpo(c[1]))
        if v:
            RITMO_REFINO.append(int(v.group(1)))
if not RITMO_REFINO:
    erro('SETUP', 'peca 11 SS2: nao achei o ritmo do refino')

# --- peca 14 SS5: o ponto de arma --------------------------------------------
m = re.search(r'1 ponto\s*=\s*([\d,]+) por rodada', P14)
PONTO_DE_ARMA = num(m.group(1)) if m else None
if PONTO_DE_ARMA is None:
    erro('SETUP', 'peca 14 SS5: nao achei o valor do ponto de arma')

# --- conferir-orcamento.py: o PISO e a escada de Classe ----------------------
m = re.search(r"^PISO\s*=\s*'(\w+)'", ORC, re.M)
PISO = m.group(1) if m else None
if PISO is None:
    erro('SETUP', 'conferir-orcamento.py: nao achei a declaracao do PISO')
ESCADA_CLASSE = [(int(a), int(b)) for a, b in
                 re.findall(r'\((\d+),\s*(\d+)\)', trecho(ORC, 'def maior_classe', 'def refino'))]
m = re.search(r'return (\d+) \* c', ORC)
MULT_FEITICO = int(m.group(1)) if m else None
if not ESCADA_CLASSE or MULT_FEITICO is None:
    erro('SETUP', 'conferir-orcamento.py: nao achei a escada de Classe ou o custo do feitico')


def maior_classe(nv):
    for c, n in ESCADA_CLASSE:
        if nv >= n:
            return c
    return 1


def bolso_piso(nv):
    nome = [k for k in CAMINHOS if sem_acento(k) == sem_acento(PISO)]
    if not nome:
        erro('SETUP', f'o PISO "{PISO}" nao existe na tabela de Caminhos da peca 1')
        return 0
    return CAMINHOS[nome[0]]['pe'] * nv


def pv(caminho, nv, con):
    c = CAMINHOS[caminho]
    return (c['vida1'] + con) + (c['por_nivel'] + con) * (nv - 1)


def teto(x):
    """o arredondamento da peca 1 SS5.4: o que voce PAGA sobe."""
    import math
    return math.ceil(x - 1e-9)


if ERROS:
    print('\n>>> FALHOU no SETUP: nao consegui ler os donos. Nada abaixo vale.')
    for e in ERROS:
        print(f'    - {e}')
    sys.exit(1)

# =============================================================================
# A PECA — catalogo, regua, orcamento
# =============================================================================
S37 = trecho(PECA, '## 3.7 O catálogo', nome='peca 15 SS3.7')
S36 = trecho(PECA, '## 3.6 Os números da Q3', '## 3.7 O catálogo', 'peca 15 SS3.6')
S35 = trecho(PECA, '## 3.5 A Q5', '## 3.6 Os números', 'peca 15 SS3.5')
S34 = trecho(PECA, '## 3.4 A Q4', '## 3.5 A Q5', 'peca 15 SS3.4')
S33 = trecho(PECA, '## 3.3 A Q3', '## 3.4 A Q4', 'peca 15 SS3.3')
S32 = trecho(PECA, '## 3.2 A Q2', '## 3.3 A Q3', 'peca 15 SS3.2')
S31 = trecho(PECA, '## 3.1 A Q1', '## 3.2 A Q2', 'peca 15 SS3.1')

CATALOGO = []      # (camada, pontos, nome, efeito, fonte)
for camada, ini, fim in (
        ('Traço', '### `Traço` — o que a invocação é', '### `Comando` — o que ela faz'),
        ('Comando', '### `Comando` — o que ela faz', '### Criar o seu')):
    for c in linhas_de_tabela(trecho(S37, ini, fim, f'catalogo de {camada}')):
        if len(c) < 3 or not re.fullmatch(r'\d+', limpo(c[0])):
            continue
        CATALOGO.append(dict(camada=camada, pts=int(limpo(c[0])), nome=limpo(c[1]),
                             efeito=c[2], fonte=c[3] if len(c) > 3 else ''))
COMPRAVEIS = [e for e in CATALOGO if e['pts'] > 0]
GRATIS = [e for e in CATALOGO if e['pts'] == 0]
if not CATALOGO:
    erro('SETUP', 'nao consegui ler o catalogo do SS3.7')

# a regua: os nomes que cada degrau declara
REGUA = {}
for camada, ini, fim in (('Traço', '| pontos | `Traço` — o que separa', '| pontos | `Comando` — o que separa'),
                         ('Comando', '| pontos | `Comando` — o que separa', '### E três coisas que a criação')):
    for c in linhas_de_tabela(trecho(S37, ini, fim, f'regua de {camada}')):
        if len(c) < 2 or not re.fullmatch(r'\d+', limpo(c[0])):
            continue
        nomes = {limpo(n) for n in re.findall(r'`([^`]+)`', c[1])}
        REGUA[(camada, int(limpo(c[0])))] = dict(criterio=c[1].split('.')[0], nomes=nomes)

# o orcamento por nivel
ORCAMENTO = {}
for c in linhas_de_tabela(trecho(S36, '### O orçamento cresce', '### Quanto vale um ponto')):
    if len(c) >= 3 and re.fullmatch(r'\d+', c[0]) and re.fullmatch(r'\d+', c[2]):
        ORCAMENTO[int(c[0])] = dict(marcos=int(c[1]), pts=int(c[2]))

# =============================================================================
# 1. TETO-ROTINA
# =============================================================================
bloco('1. TETO-ROTINA — o teto somado vem da peca 6 SS4, nunca de constante')
citacoes = re.findall(r'somados entregam \*?\*?(uma|duas|três) Rotina', PECA)
print(f'  peca 6 SS4 e dona: o dono e todas as invocacoes somados entregam '
      f'{TETO_SOMADO} Rotina. A peca 15 cita a frase {len(citacoes)}x.')
if not citacoes:
    erro('TETO-ROTINA', 'a peca 15 nao cita o teto somado da peca 6 SS4 em lugar nenhum')
for c in citacoes:
    if {'uma': 1, 'duas': 2, 'três': 3}[c] != TETO_SOMADO:
        erro('TETO-ROTINA', f'a peca 15 cita "{c} Rotina" e a peca 6 SS4 diz '
                            f'{TETO_SOMADO} — o teto tem UM dono, e nao e este documento')
# a soma das cotas de cada Trilha tem de dar exatamente o teto
for t in TRILHAS:
    d = COTA[t]['divisor']
    if d is None:
        continue
    n_corpos = d                      # 1/n em cada, com n corpos entregando
    if abs(n_corpos * (1.0 / d) - TETO_SOMADO) > 1e-9:
        erro('TETO-ROTINA', f'{t}: {n_corpos} x 1/{d} nao fecha {TETO_SOMADO} Rotina')
    print(f'  {t:<9} {n_corpos} x 1/{d} = {n_corpos * (1.0 / d):.2f} Rotina')

# =============================================================================
# 2. DOMINANCIA entre as tres Trilhas
# =============================================================================
bloco('2. DOMINANCIA — a matriz entre as tres Trilhas, por quantidade de corpos')
# quem ataca E comanda sai da tabela do SS3.4, e nao de constante aqui dentro
ACAO = {}
for c in linhas_de_tabela(trecho(S34, '| Trilha | na peça 6 §2 | aqui |', '*As três passam a diferir')):
    if len(c) >= 3 and limpo(c[0]) in TRILHAS:
        ACAO[limpo(c[0])] = 1 if 'ataca e comanda' in sem_acento(c[2]) else 0
if set(ACAO) != set(TRILHAS):
    erro('DOMINANCIA', f'SS3.4: a tabela de economia de acao por Trilha nao lista as tres '
                       f'({sorted(ACAO)}) — sem ela a excecao do Coro vira constante escrita '
                       'dentro do validador')
# Os dois eixos que a Q6 acrescentou saem da tabela do SS3.7. Sem eles a matriz
# volta a acusar as duas dominancias que aquela pergunta existia para matar, e e
# por isso que a leitura falha alto em vez de cair para um valor de reserva.
CONCEDE = {}
for c in linhas_de_tabela(trecho(S37, '| Trilha | o que ela concede |',
                                 '**A vida do `Servo`')):
    if len(c) < 4:
        continue
    nome = limpo(c[0])
    if nome not in TRILHAS:
        continue
    _o = sem_acento(c[2])
    _v = sem_acento(c[3])
    CONCEDE[nome] = dict(orc=2 if 'mais metade' in _o else 1,
                         vida=5 if '5' in _v.replace('x', ' ') else 1)
if set(CONCEDE) != set(TRILHAS):
    erro('DOMINANCIA', 'SS3.7: a tabela "O que cada Trilha concede" nao lista as tres '
                       f'({sorted(CONCEDE)}) — sem ela os dois eixos que a Q6 abriu '
                       'virariam constante escrita dentro deste arquivo, e a matriz '
                       'voltaria a acusar as duas dominancias que ela fechou')
perfil = {}
for t in TRILHAS:
    corpos = COTA[t]['corpos'] if COTA[t]['corpos'] else CORPOS_ESPERADOS[t]
    perfil[t] = dict(saida=TETO_SOMADO,
                     corpos=int(corpos),
                     acao=ACAO.get(t, 0),
                     orc=CONCEDE.get(t, {}).get('orc', 1),
                     vida=CONCEDE.get(t, {}).get('vida', 1))
    print(f'  {t:<9} saida {perfil[t]["saida"]} Rotina · {perfil[t]["corpos"]} corpo(s) '
          f'· {"ataca e comanda" if perfil[t]["acao"] else "comanda, nao ataca"} '
          f'· orcamento {"x1,5" if perfil[t]["orc"] > 1 else "da ficha"} '
          f'· vida {"5h" if perfil[t]["vida"] > 1 else "h"}')
EIXOS = ('saida', 'corpos', 'acao', 'orc', 'vida')
achadas = set()
for a in TRILHAS:
    for b in TRILHAS:
        if a == b:
            continue
        if all(perfil[a][e] >= perfil[b][e] for e in EIXOS) and \
           any(perfil[a][e] > perfil[b][e] for e in EIXOS):
            achadas.add((a, b))
        if all(perfil[a][e] == perfil[b][e] for e in EIXOS) and a < b:
            erro('DOMINANCIA', f'{a} e {b} sao identicas nos tres eixos — duas Trilhas '
                               'com o mesmo perfil nao sao duas escolhas')
novas = achadas - DOMINANCIA_PENDENTE_Q6
sumidas = DOMINANCIA_PENDENTE_Q6 - achadas
print(f'  {len(TRILHAS) * (len(TRILHAS) - 1)} pares, {len(achadas)} dominancia(s), '
      f'{len(achadas & DOMINANCIA_PENDENTE_Q6)} declarada(s) como pendente da Q6.')
for a, b in sorted(novas):
    erro('DOMINANCIA', f'{a} domina {b} nos tres eixos e nao esta declarada')
if not achadas and not DOMINANCIA_PENDENTE_Q6:
    print('  nenhuma dominancia entre as tres, e nenhuma declarada — a Q6 fechou '
          'os dois pares que apontavam para o Servo.')

# A VIDA NAO E EIXO DE DOMINANCIA, e por isso ela precisa de checagem propria.
# Medido: so o orcamento ja zera a matriz, entao tirar o 5h do Servo sairia VERDE
# aqui e desfaria em silencio a metade da Q6 que a matriz nao mede — a de "perder
# o corpo acaba o kit". A regra do SS3.5 le a VIDA MAXIMA para decidir morte em
# definitivo, e com h o gatilho do Servo era 1/5 do da Matilha para a MESMA Rotina
# entregue. O invariante e esse, e nao o numero 5.
if set(CONCEDE) == set(TRILHAS):
    _vs, _vm = CONCEDE['Servo']['vida'], CONCEDE['Matilha']['vida']
    if _vs < _vm:
        erro('DOMINANCIA', f'SS3.7: a vida do corpo do Servo ({_vs}h) e menor que a da '
                           f'Matilha ({_vm}h) e as duas entregam a mesma Rotina — pela '
                           'regra de morte do SS3.5 o Servo sai da luta por um golpe '
                           f'{_vm / max(_vs, 1):.0f}x menor, e ele e a Trilha de UM corpo '
                           'so. A matriz de dominancia nao mede isto e sai verde.')
    else:
        print(f'  [x] o corpo do Servo ({_vs}h) nao sai da luta por golpe menor que o '
              f'da Matilha ({_vm}h) — as duas entregam a mesma Rotina.')
alvos = {b for _, b in achadas & DOMINANCIA_PENDENTE_Q6}
if len(alvos) == 1:
    print(f'  as {len(achadas & DOMINANCIA_PENDENTE_Q6)} pendentes apontam todas para o '
          f'{alvos.pop()} — que e a unica das tres cuja concessao ainda nao tem numero.')
for a, b in sorted(sumidas):
    erro('DOMINANCIA', f'{a} > {b} esta declarada como pendente da Q6 e nao aparece mais — '
                       'se a Q6 fechou e deu numero ao corpo forte, tire a declaracao '
                       'em vez de deixar ela mentindo')

# =============================================================================
# 3. SOMATORIO — invocar dentro do bolso, junto do resto
# =============================================================================
bloco('3. SOMATORIO — invocar contra o bolso, sem apagar o dia de feitico')
tab_preco = [c for c in linhas_de_tabela(trecho(S34, '### O `1 ×` escolhido', '### A ação sozinha'))
             if len(c) >= 5 and re.fullmatch(r'\d+', limpo(c[0]))]
if not tab_preco:
    erro('SOMATORIO', 'SS3.4: nao achei a tabela do "1 x escolhido"')
print(f"  {'nv':<5}{'bolso':<8}{'invocar x3':<12}{'feiticos no dia':<18}{'o doc diz':<12}")
for c in tab_preco:
    nv = int(limpo(c[0]))
    unit, tres = int(limpo(c[1])), int(limpo(c[2]))
    esperado_unit = teto(1 * maior_classe(nv))
    bolso = bolso_piso(nv)
    feitico = MULT_FEITICO * maior_classe(nv)
    no_dia = bolso // feitico
    diz = limpo(c[4])
    m = re.match(r'(\d+) de (\d+)', diz)
    print(f'  {nv:<5}{bolso:<8}{tres:<12}{no_dia:<18}{diz:<12}')
    if unit != esperado_unit:
        erro('SOMATORIO', f'nv{nv}: o doc diz {unit} PE por invocacao e '
                          f'1 x Classe {maior_classe(nv)} da {esperado_unit}')
    if tres != 3 * unit:
        erro('SOMATORIO', f'nv{nv}: tres lutas dao {3 * unit} PE e o doc escreve {tres}')
    if m and int(m.group(2)) != no_dia:
        erro('SOMATORIO', f'nv{nv}: o doc diz "{diz}" e o bolso do {PISO} ({bolso} PE) '
                          f'paga {no_dia} feiticos de {feitico} PE')
    if m and tres != int(m.group(1)) * feitico:
        erro('SOMATORIO', f'nv{nv}: invocar tres vezes custa {tres} PE e o doc diz que '
                          f'isso e {m.group(1)} feitico(s) de {feitico} PE')
    if tres > bolso:
        erro('SOMATORIO', f'nv{nv}: invocar tres vezes ({tres} PE) nao cabe no bolso do '
                          f'{PISO} ({bolso} PE) nem sozinho')

# =============================================================================
# 4. TEMPO-DE-MESA — nao e checagem de codigo, e numero escrito ANTES da sessao
# =============================================================================
bloco('4. TEMPO-DE-MESA — a tabela de rolagens fecha, e o numero esperado esta escrito')
rol = [c for c in linhas_de_tabela(trecho(S32, '### O tempo de mesa', '### A forma do dano'))
       if len(c) >= 3 and num(c[1]) is not None and re.search(r'\d+\s*[–-]\s*\d+', c[2])]
if len(rol) < 4:
    erro('TEMPO-DE-MESA', f'SS3.2: esperava a tabela de rolagens por rodada, achei {len(rol)} linha(s)')
por_rodada = {}
for c in rol:
    quem = limpo(c[0])
    pr = num(c[1])
    a, b = (int(x) for x in re.findall(r'\d+', c[2].replace('–', '-'))[:2])
    por_rodada[quem] = pr
    lo, hi = RODADAS_POR_LUTA
    if not (pr * lo - 1 <= a <= pr * lo + 1) or not (pr * hi - 1 <= b <= pr * hi + 1):
        erro('TEMPO-DE-MESA', f'"{quem}": {pr} por rodada dao {pr * lo:.0f}-{pr * hi:.0f} '
                              f'por combate, e a tabela escreve {a}-{b}')
    print(f'  {quem[:44]:<46}{pr:>5} por rodada   {a}-{b} por combate')
m = re.search(r'\*\*A Matilha custa ([\d,]+)×', S32)
if not m:
    erro('TEMPO-DE-MESA', 'SS3.2: o multiplo da Matilha nao esta escrito — o numero '
                          'esperado da sessao de playtest tem de estar no papel ANTES dela')
else:
    escrito = num(m.group(1))
    alvo = [v for k, v in por_rodada.items() if 'Matilha' in k]
    base = [v for k, v in por_rodada.items() if 'nv6' in k or 'nível 6' in k or 'dois golpes' in k]
    if alvo and base:
        calc = alvo[0] / base[0]
        print(f'  a Matilha custa {calc:.1f}x o personagem de nivel 6 — e o doc escreve {escrito:g}x')
        if abs(calc - escrito) > 0.05:
            erro('TEMPO-DE-MESA', f'o doc escreve {escrito:g}x e a tabela dele mesmo da {calc:.2f}x')

# =============================================================================
# 5. TRIAGEM
# =============================================================================
bloco('5. TRIAGEM — todo nome que a peca cria, contra a propria triagem dela')
PECA_SA = sem_acento(PECA)
for e in CATALOGO:
    n_sa = sem_acento(e['nome'])
    if n_sa in {sem_acento(x) for x in OCUPADO_NA_TRIAGEM}:
        erro('TRIAGEM', f'"{e["nome"]}" esta na lista de OCUPADO que a propria peca '
                        'levantou, e mesmo assim foi para o catalogo')
    if PECA_SA.count(n_sa) < 2:
        erro('TRIAGEM', f'"{e["nome"]}" aparece uma vez so na peca — ele esta no catalogo '
                        'e em lugar nenhum do argumento')
print(f'  {len(CATALOGO)} nomes de catalogo conferidos contra a lista de OCUPADO '
      f'({len(OCUPADO_NA_TRIAGEM)} nomes) e contra o corpo do documento.')
print('  (quem confere nome contra o .docx e o conferir-nomes.py, e nao este.)')

# =============================================================================
# 6. REGUA — toda entrada cai no degrau que a regua manda
# =============================================================================
bloco('6. REGUA — toda entrada cai no degrau que a regua da criacao manda')
if not REGUA:
    erro('REGUA', 'SS3.7: nao achei as tabelas da regua de criacao')
por_nome = {}
for (camada, pts), d in REGUA.items():
    for n in d['nomes']:
        por_nome[(camada, n)] = pts
for e in CATALOGO:
    chave = (e['camada'], e['nome'])
    if chave not in por_nome:
        erro('REGUA', f'{e["camada"]} "{e["nome"]}" esta no catalogo e em degrau nenhum '
                      'da regua — entrada que a regua nao classifica e entrada que a '
                      'mesa vai precificar por imitacao')
    elif por_nome[chave] != e['pts']:
        erro('REGUA', f'{e["camada"]} "{e["nome"]}" custa {e["pts"]} no catalogo e a regua '
                      f'o poe no degrau de {por_nome[chave]}')
for (camada, n), pts in por_nome.items():
    if not any(x['camada'] == camada and x['nome'] == n for x in CATALOGO):
        erro('REGUA', f'a regua do {camada} de {pts} ponto(s) lista "{n}", que nao esta '
                      'no catalogo')
for (camada, pts), d in sorted(REGUA.items()):
    print(f'  {camada:<8} degrau {pts}: {len(d["nomes"])} entrada(s) — {d["criterio"][:52]}')

# =============================================================================
# 7. ILEGAIS
# =============================================================================
bloco('7. ILEGAIS — dado de dano, refino e deslocamento positivo nao tem preco')
S_ILEGAL = trecho(S37, '### E três coisas que a criação', '### Os outros três tipos')
for chave, dono in ILEGAL_DONO.items():
    if sem_acento(chave) not in sem_acento(S_ILEGAL):
        erro('ILEGAIS', f'a peca nao declara "{chave}" como ilegal na criacao')
    elif sem_acento(dono).replace('ss', '§') not in sem_acento(S_ILEGAL).replace('ss', '§'):
        aviso(f'a proibicao de "{chave}" nao nomeia o dono ({dono}) ao lado dela')
sujo = 0
for e in CATALOGO:
    texto = f'{e["efeito"]} {e["fonte"]}'
    if re.search(r'\b\d*d\d+\b', texto):
        erro('ILEGAIS', f'"{e["nome"]}" tem dado de dano no texto — {ILEGAL_DONO["dado de dano"]} '
                        'governa a saida, e um dado a mais nao e caro, e inexistente')
        sujo += 1
    if 'refino' in sem_acento(texto):
        erro('ILEGAIS', f'"{e["nome"]}" usa refino — ele cresce +{max(RITMO_REFINO)} contra +3, '
                        f'e {ILEGAL_DONO["refino"]} proibe')
        sujo += 1
    if re.search(r'\+\s*\d', texto):
        erro('ILEGAIS', f'"{e["nome"]}" concede um valor positivo no texto — deslocamento '
                        f'positivo e proibido por {ILEGAL_DONO["deslocamento positivo"]}')
        sujo += 1
print(f'  {len(CATALOGO)} entradas varridas, {sujo} com dado, refino ou valor positivo.')

# =============================================================================
# 8. DESLOCAMENTO — nada sobe acima do numero do dono
# =============================================================================
bloco('8. DESLOCAMENTO — a invocacao comeca no numero do dono e so pode descer')
S_DESL = trecho(S36, '### "Invocações raramente passam', '### A amarra')
tab = [c for c in linhas_de_tabela(S_DESL) if len(c) >= 3]
achou_proibido, subiu = False, []
for c in tab:
    faz, custa = limpo(c[0]), limpo(c[1])
    if re.search(r'^\+\s*\d', faz.replace('**', '')):
        achou_proibido = True
        if 'proibido' not in sem_acento(custa):
            erro('DESLOCAMENTO', f'a linha "{faz}" nao esta marcada como proibida — '
                                 'a invocacao passaria do portador')
    if re.match(r'^-|^−', faz) and 'devolve' not in sem_acento(custa):
        subiu.append(faz)
if not achou_proibido:
    erro('DESLOCAMENTO', 'SS3.6: a tabela nao tem a linha do deslocamento POSITIVO marcada '
                         'como proibida — sem ela a regra vira orientacao')
for f in subiu:
    erro('DESLOCAMENTO', f'a linha "{f}" desce e nao devolve ponto — descer sem devolver '
                         'nao e escolha, e castigo')
m = re.search(r'\*\*A invocação começa no número do dono e só pode descer\.\*\*', S36)
if not m:
    erro('DESLOCAMENTO', 'SS3.6: a regra "comeca no numero do dono e so pode descer" nao '
                         'esta escrita como regra')
# --- o TAMANHO da devolucao, que ate a v0.68 ninguem media -------------------
# A checagem acima confere a FORMA da venda (descer devolve, subir e proibido).
# Ela sai verde com qualquer numero, e foi por isso que a v0.67 multiplicou o
# catalogo e o orcamento por quatro e deixou a devolucao em 1 sem ninguem ver.
dev = None
for c in tab:
    m_d = re.search(r'devolve\s*(\d+)', limpo(c[1]))
    if not m_d:
        continue
    v = int(m_d.group(1))
    if dev is None:
        dev = v
    elif dev != v:
        erro('DESLOCAMENTO', f'as linhas de venda devolvem valores diferentes ({dev} e '
                             f'{v}) — acerto e Defesa se vendem pelo mesmo preco')
if dev is None:
    erro('DESLOCAMENTO', 'SS3.6: nao achei quanto a venda devolve — sem isso o tamanho '
                         'dela nao tem contra o que ser medido')
else:
    # A REGRA APLICADA: vender tem de comprar alguma coisa.
    barato = min(e['pts'] for e in COMPRAVEIS)
    if dev < barato:
        erro('DESLOCAMENTO', f'a venda devolve {dev} e a entrada mais barata do catalogo '
                             f'custa {barato} — sozinha ela nao compra nada. Descer sem '
                             'poder comprar e castigo, nao escolha')
    # O LIMITE DE DESIGN, separado da regra e lido do dono: a devolucao e um ponto
    # da escala velha, que e a mesma coisa que o marco passou a dar.
    m_p = re.search(r'\*\*Cada marco dá `(\d+)` pontos', S36)
    if not m_p:
        erro('DESLOCAMENTO', 'SS3.6: nao achei quanto cada marco da, e sem isso a '
                             'devolucao viraria constante escrita neste arquivo')
    elif dev != int(m_p.group(1)):
        erro('DESLOCAMENTO', f'a venda devolve {dev} e cada marco da {m_p.group(1)} — os '
                             'dois SAO um ponto da escala velha e andam juntos. Separar '
                             'os dois e decisao a escrever, nao numero a ajustar')
    else:
        print(f'  a venda devolve {dev}: compra a entrada mais barata ({barato}) e bate '
              f'com o passo do marco.')
print(f'  {len(tab)} linha(s) de deslocamento, com a positiva declarada proibida.')

# =============================================================================
# 9. ORCAMENTO — derivado dos marcos da peca 2
# =============================================================================
bloco('9. ORCAMENTO — derivado dos marcos da peca 2, nunca lido de constante')
if 2 not in ORCAMENTO:
    erro('ORCAMENTO', 'SS3.6: a tabela do orcamento nao tem a linha do nivel 2')
else:
    # o passo do marco e a base sao DECLARADOS no SS3.6 e lidos de la.
    # Ate a v0.66 o passo era 1 e estava implicito; a v0.67 quebrou o ponto em
    # quatro e o passo virou 4. Passo implicito nao acende quando muda.
    m_passo = re.search(r'\*\*Cada marco dá `(\d+)` pontos, e a base no nível 2 '
                        r'é `(\d+)`\.\*\*', S36)
    if not m_passo:
        erro('ORCAMENTO', 'SS3.6: nao achei a linha que declara quanto cada marco da e '
                          'qual a base do nivel 2 — sem ela o passo viraria constante '
                          'escrita dentro deste arquivo')
        PASSO_ORC, BASE_DECL = 1, None
    else:
        PASSO_ORC, BASE_DECL = int(m_passo.group(1)), int(m_passo.group(2))
    BASE_ORC = ORCAMENTO[2]['pts'] - PASSO_ORC * sum(1 for m_ in MARCOS if 2 >= m_)
    if BASE_DECL is not None and BASE_DECL != BASE_ORC:
        erro('ORCAMENTO', f'o SS3.6 declara base {BASE_DECL} e a tabela dele deriva '
                          f'{BASE_ORC} — as duas copias do mesmo numero divergiram')
    print(f'  marcos da peca 2: {MARCOS}   base no nivel 2: {BASE_ORC}   '
          f'cada marco da: {PASSO_ORC}')
    print(f"  {'nv':<5}{'marcos ate ali':<17}{'derivado':<11}{'no doc':<8}")
    for nv in sorted(ORCAMENTO):
        n_marcos = sum(1 for m_ in MARCOS if nv >= m_)
        deriv = BASE_ORC + PASSO_ORC * n_marcos
        d = ORCAMENTO[nv]
        print(f'  {nv:<5}{n_marcos:<17}{deriv:<11}{d["pts"]:<8}')
        if d['marcos'] != n_marcos:
            erro('ORCAMENTO', f'nv{nv}: o doc conta {d["marcos"]} marcos e a peca 2 da '
                              f'{n_marcos}')
        if d['pts'] != deriv:
            erro('ORCAMENTO', f'nv{nv}: o doc da orcamento {d["pts"]} e os marcos da peca 2 '
                              f'derivam {deriv} — o orcamento tem de cair dos marcos, nao '
                              'ser escrito ao lado deles')
    # o resumo do topo da peca e COPIA do orcamento, e nada comparava as duas.
    # Ele passou a v0.67 inteira publicando a escala velha, verde.
    m_res = re.search(r'O orçamento é `(\d+)` no nível 2 e sobe `\+(\d+)` por marco, '
                      r'até `(\d+)` no 30', PECA)
    if not m_res:
        erro('ORCAMENTO', 'o resumo do topo da peca nao publica mais o orcamento — se a '
                          'linha saiu de proposito, esta checagem sai com ela')
    else:
        r_base, r_passo, r_topo = (int(x) for x in m_res.groups())
        topo = ORCAMENTO[max(ORCAMENTO)]['pts']
        if (r_base, r_passo, r_topo) != (BASE_ORC, PASSO_ORC, topo):
            erro('ORCAMENTO', f'o resumo do topo diz base {r_base}, passo {r_passo} e teto '
                              f'{r_topo}, e o SS3.6 da {BASE_ORC}, {PASSO_ORC} e {topo} — '
                              'duas copias do mesmo numero, divergindo')
        else:
            print(f'  o resumo do topo bate com o dono: {r_base} de base, {r_passo} por '
                  f'marco, {r_topo} no 30.')
    # a tabela do orcamento do SERVO e DERIVADA: ficha x1,5 com o arredondamento
    # da peca 1 SS5.4 (ganho desce). Ate a v0.68 ela publicava a escala velha nas
    # duas colunas e a escala nova no cabecalho, meio convertida, verde.
    tab_servo = [c for c in linhas_de_tabela(
                     trecho(S37, '| nv | orçamento da ficha | do `Servo` |',
                            '**A `Matilha` compra menos'))
                 if len(c) >= 4 and re.fullmatch(r'\d+', limpo(c[0]))]
    m_cat = re.search(r'do catálogo inteiro \((\d+) pontos\)', S37)
    soma_cat = sum(e['pts'] for e in CATALOGO)
    if not tab_servo:
        erro('ORCAMENTO', 'SS3.7: nao achei a tabela do orcamento do Servo')
    elif not m_cat:
        erro('ORCAMENTO', 'SS3.7: a tabela do Servo nao declara o total do catalogo')
    else:
        if int(m_cat.group(1)) != soma_cat:
            erro('ORCAMENTO', f'SS3.7: a tabela do Servo diz que o catalogo tem '
                              f'{m_cat.group(1)} pontos e ele soma {soma_cat}')
        for c in tab_servo:
            nv, ficha, servo = int(limpo(c[0])), int(limpo(c[1])), int(limpo(c[2]))
            pct = limpo(c[3])
            esp_ficha = BASE_ORC + PASSO_ORC * sum(1 for m_ in MARCOS if nv >= m_)
            esp_servo = (esp_ficha * 3) // 2          # "mais metade", ganho desce
            esp_pct = round(100.0 * esp_servo / soma_cat) if soma_cat else 0
            if ficha != esp_ficha:
                erro('ORCAMENTO', f'SS3.7 nv{nv}: a tabela do Servo diz que a ficha tem '
                                  f'{ficha} e os marcos derivam {esp_ficha}')
            if servo != esp_servo:
                erro('ORCAMENTO', f'SS3.7 nv{nv}: o Servo esta com {servo} e "a ficha mais '
                                  f'metade, ganho desce" da {esp_servo}')
            if pct != f'{esp_pct}%':
                erro('ORCAMENTO', f'SS3.7 nv{nv}: a tabela publica {pct} do catalogo e o '
                                  f'recontado da {esp_pct}%')
        print(f'  a tabela do Servo: {len(tab_servo)} linhas derivadas da ficha x1,5, '
              f'contra um catalogo de {soma_cat} pontos recontado.')
    faixa = re.search(r'\*\*De (\d+) a (\d+),', S36)
    if faixa:
        lo, hi = int(faixa.group(1)), int(faixa.group(2))
        real = (min(v['pts'] for v in ORCAMENTO.values()), max(v['pts'] for v in ORCAMENTO.values()))
        if (lo, hi) != real:
            erro('ORCAMENTO', f'a prosa escreve "de {lo} a {hi}" e a tabela dela da {real}')

# =============================================================================
# 10. DUAS-MOEDAS
# =============================================================================
bloco('10. DUAS-MOEDAS — ponto de arma e ponto de ficha nao se convertem')
m = re.search(r'esta ficha[^|]*\|\s*\*\*±(\d+)% do que a invocação entrega\*\*', S36)
PONTO_DE_FICHA = int(m.group(1)) if m else None
if PONTO_DE_FICHA is None:
    erro('DUAS-MOEDAS', 'SS3.6: nao achei quanto vale um ponto de ficha')
else:
    print(f'  ponto de arma  (peca 14 SS5): {PONTO_DE_ARMA:g} de dano por rodada')
    print(f'  ponto de ficha (SS3.6)      : +-{PONTO_DE_FICHA}% do que a invocacao entrega')
    if not re.search(r'não pode acontecer é as duas moedas caírem no mesmo saco', S36):
        erro('DUAS-MOEDAS', 'SS3.6: a peca nao declara que as duas moedas nao se misturam')
    for e in CATALOGO:
        if re.search(r'0[.,]33|ponto de arma', sem_acento(f'{e["efeito"]} {e["fonte"]}')):
            erro('DUAS-MOEDAS', f'"{e["nome"]}" preca em moeda de arma dentro do catalogo '
                                'da ficha — as duas cairam no mesmo saco')
    if re.search(r'\d\s*ponto de ficha\s*=\s*[\d,]+\s*ponto de arma', PECA) or \
       re.search(r'ponto de arma\s*=\s*[\d,]+\s*ponto de ficha', PECA):
        erro('DUAS-MOEDAS', 'existe taxa de conversao escrita entre as duas moedas')
    # A razao entre as duas moedas, RECALCULADA dos donos. Ate a v0.68 a peca
    # publicava "o ponto de arma e cerca de quatro vezes menor", sem nada guardando
    # — e a v0.67 dividiu o lado da ficha por quatro sem que a frase se mexesse.
    m_raz = re.search(r'o ponto de ficha vale \*\*([\d,]+)× o de arma no nível 2 e '
                      r'([\d,]+)× no nível 30\*\*', S36)
    if not m_raz:
        erro('DUAS-MOEDAS', 'SS3.6: nao achei a razao publicada entre as duas moedas')
    elif dev is None:
        erro('DUAS-MOEDAS', 'sem a devolucao lida na checagem 8 a razao nao tem como ser '
                            'recalculada')
    else:
        # 1 ponto de acerto vale PONTO_DE_FICHA% do que a invocacao entrega, e ela
        # entrega AREA por alvo; vender 1 ponto devolve `dev` pontos de orcamento.
        AREA = 1.0 / COTA['Servo']['divisor']
        for nv, publicado in ((2, num(m_raz.group(1))), (30, num(m_raz.group(2)))):
            if nv not in ROTINA_NV:
                erro('DUAS-MOEDAS', f'peca 6 SS3: sem a Rotina do nv{nv} a razao nao fecha')
                continue
            calc = (PONTO_DE_FICHA / 100.0 * AREA * ROTINA_NV[nv] / dev) / PONTO_DE_ARMA
            print(f'  nv{nv}: 1 ponto de ficha = {calc:.2f}x o ponto de arma '
                  f'(publicado: {publicado:g}x)')
            if abs(calc - publicado) > 0.05:
                erro('DUAS-MOEDAS', f'nv{nv}: a peca publica {publicado:g}x e os donos dao '
                                    f'{calc:.2f}x — a razao entre as duas moedas envelheceu')
    print('  Nenhuma taxa de conversao escrita, e nenhuma entrada precada em moeda de arma.')

# =============================================================================
# 11. AREA
# =============================================================================
bloco('11. AREA — o multiplicador sai do documento, e o pool nao se apaga')
m = re.search(r'\*\*×(\d+) — vulnerável\*\*', S35) or re.search(r'×(\d+) — vulnerável', S35)
MULT_AREA = int(m.group(1)) if m else None
if MULT_AREA is None:
    erro('AREA', 'SS3.5: nao achei o multiplicador da area')
CORPOS_MATILHA = int(COTA['Matilha']['corpos'])
tab_area = [c for c in linhas_de_tabela(trecho(S35, '| como a área entra', '**Contra-teste'))
            if len(c) >= 4 and num(c[1]) is not None]
if not tab_area:
    erro('AREA', 'SS3.5: nao achei a tabela de como a area entra')
AREA_ROTINA = 1.0 / COTA['Servo']['divisor']      # "area de rotina" = meia Rotina por alvo
POOL_R = CORPOS_MATILHA * AREA_ROTINA             # o pool em Rotinas: 5 x meia Rotina
print(f'  pool da Matilha = {CORPOS_MATILHA} x {AREA_ROTINA:g} = {POOL_R:g} Rotina(s); '
      f'area de rotina = {AREA_ROTINA:g} Rotina por alvo')
print(f"  {'como entra':<24}{'no pool':<10}{'% do pool':<12}{'corpos':<9}{'doc':<18}")
for c in tab_area:
    rot_doc, pct_doc, corp_doc = num(c[1]), num(c[2]), num(c[3])
    rotulo = limpo(c[0])
    mm = re.search(r'×([\d,]+)', rotulo)
    if 'por corpo' in rotulo:
        mult = CORPOS_MATILHA
    elif 'uma vez, sem' in rotulo:
        mult = 1.0
    elif mm:
        mult = num(mm.group(1))
    else:
        continue
    calc = AREA_ROTINA * mult
    pct = calc / POOL_R
    corpos = calc / AREA_ROTINA
    print(f'  {rotulo[:22]:<24}{calc:<10.2f}{pct:<12.0%}{corpos:<9.1f}'
          f'{rot_doc:g} R · {pct_doc:g}% · {corp_doc:g}')
    if abs(calc - rot_doc) > 0.01 or abs(pct * 100 - pct_doc) > 0.6 or abs(corpos - corp_doc) > 0.05:
        erro('AREA', f'a linha "{rotulo}" nao reproduz: a conta da {calc:.2f} R / {pct:.0%} / '
                     f'{corpos:.1f} corpos e o doc escreve {rot_doc:g} / {pct_doc:g}% / {corp_doc:g}')
if MULT_AREA:
    dano_escolhido = AREA_ROTINA * MULT_AREA
    caem = dano_escolhido / AREA_ROTINA
    print(f'  com o x{MULT_AREA} escolhido, um feitico de area de rotina tira '
          f'{caem:.0f} dos {CORPOS_MATILHA} corpos.')
    if dano_escolhido >= POOL_R - 1e-9:
        erro('AREA', f'com x{MULT_AREA} um feitico de area de ROTINA leva {dano_escolhido:g} R '
                     f'ao pool de {POOL_R:g} R — ele apaga a Matilha inteira, e a jogada '
                     'certa vira jogada automatica')

# =============================================================================
# 12. MORTE — os dois gatilhos
# =============================================================================
bloco('12. MORTE — os dois gatilhos, e nenhum golpe de rotina dispara')
m = re.search(r'se o excedente passar de \*?\*?(metade|um terço|um quarto) da vida máxima, ou '
              r'se um único golpe causar a vida máxima inteira', S35)
FRACAO = {'metade': 2, 'um terço': 3, 'um quarto': 4}[m.group(1)] if m else None
if FRACAO is None:
    erro('MORTE', 'SS3.5: nao achei a regra dos dois gatilhos de morte em definitivo')
else:
    GAT_A = POOL_R / FRACAO
    GAT_B = POOL_R
    print(f'  vida maxima do pool = {POOL_R:g} R · gatilho A (excedente) > {GAT_A:g} R · '
          f'gatilho B (golpe unico) >= {GAT_B:g} R')
    tab_morte = [c for c in linhas_de_tabela(trecho(S35, '| de onde vem o golpe', '### Reconseguir'))
                 if len(c) >= 4 and num(c[1]) is not None]
    if not tab_morte:
        erro('MORTE', 'SS3.5: nao achei a tabela dos gatilhos')
    rotina_limpa = True
    for c in tab_morte:
        origem, dano = limpo(c[0]), num(c[1])
        a_doc = 'sim' in sem_acento(c[2])
        b_doc = 'sim' in sem_acento(c[3])
        a_calc, b_calc = dano > GAT_A + 1e-9, dano >= GAT_B - 1e-9
        marca = 'ok' if (a_calc == a_doc and b_calc == b_doc) else 'DIVERGE'
        print(f'  {origem[:44]:<46}{dano:>5.2f} R  A={"sim" if a_calc else "nao"}/'
              f'{"sim" if a_doc else "nao"}  B={"sim" if b_calc else "nao"}/'
              f'{"sim" if b_doc else "nao"}  {marca}')
        if a_calc != a_doc or b_calc != b_doc:
            erro('MORTE', f'"{origem}": {dano:g} R da A={a_calc} B={b_calc} contra os '
                          f'dois gatilhos, e a tabela escreve A={a_doc} B={b_doc}')
        de_rotina = 'rotina' in sem_acento(origem) or 'golpe' in sem_acento(origem)
        if de_rotina and 'grande' not in sem_acento(origem) and (a_calc or b_calc):
            rotina_limpa = False
            erro('MORTE', f'"{origem}" e golpe de rotina e dispara morte em definitivo — '
                          'a regra tem de disparar onde a ficcao dispara, e area grande e '
                          'Expansao sao as duas coisas que na obra destroem shikigami de vez')
    if rotina_limpa:
        print('  Nenhum golpe de rotina dispara nenhum dos dois gatilhos.')

# =============================================================================
# 13. PRECO — contra o bolso do PISO
# =============================================================================
bloco(f'13. PRECO — o preco de invocar medido contra o {PISO}, nunca contra o Evocador')
S_PRECO = trecho(S34, '### E o arredondamento do projeto', '### Por que "nada" não cabia')
tab_reg = [c for c in linhas_de_tabela(S_PRECO) if len(c) >= 5 and '×' in c[0]]
if not tab_reg:
    erro('PRECO', 'SS3.4: nao achei a tabela das reguas de preco')
niveis = [int(x) for x in re.findall(r'nv(\d+)', S_PRECO)][:4]
if len(niveis) < 4:
    niveis = sorted(ORCAMENTO)[:4]
print(f"  bolso do {PISO}: " + ' · '.join(f'nv{n} {bolso_piso(n)} PE' for n in niveis))
zera = []
for c in tab_reg:
    mult = num(c[0])
    print(f'  regua {c[0]:<22}', end='')
    for i, nv in enumerate(niveis, start=1):
        if i >= len(c):
            break
        pe_doc, pct_doc = num(c[i]), num(c[i].split('·')[-1]) if '·' in c[i] else None
        pe_calc = 3 * teto(mult * maior_classe(nv))
        bolso = bolso_piso(nv)
        pct_calc = 100.0 * pe_calc / bolso
        print(f'{pe_calc:>3} PE {pct_calc:>3.0f}% ', end='')
        if pe_doc is not None and abs(pe_calc - pe_doc) > 0.01:
            erro('PRECO', f'regua {c[0]}, nv{nv}: a conta da {pe_calc} PE em tres lutas e o '
                          f'doc escreve {pe_doc:g}')
        if pct_doc is not None and abs(pct_calc - pct_doc) > 0.6:
            erro('PRECO', f'regua {c[0]}, nv{nv}: a conta da {pct_calc:.0f}% do dia e o doc '
                          f'escreve {pct_doc:g}%')
    nv0 = min(niveis)
    sobra = bolso_piso(nv0) - 3 * teto(mult * maior_classe(nv0))
    feiticos = max(0, sobra) // (MULT_FEITICO * maior_classe(nv0))
    print(f'   -> nv{nv0} sobra {sobra} PE = {feiticos} feitico(s)')
    if feiticos == 0:
        zera.append(c[0])
ESCOLHIDA = re.search(r'\*\*Invocar custa `(\d+(?:,\d+)?) × a sua maior Classe`', PECA)
if not ESCOLHIDA:
    erro('PRECO', 'nao achei a regra do custo de invocar na peca')
else:
    mult_esc = num(ESCOLHIDA.group(1))
    nv0 = min(niveis)
    sobra = bolso_piso(nv0) - 3 * teto(mult_esc * maior_classe(nv0))
    feiticos = max(0, sobra) // (MULT_FEITICO * maior_classe(nv0))
    print(f'  a regua ESCOLHIDA e {mult_esc:g}x, e no nv{nv0} ela deixa {feiticos} feitico(s) '
          f'no dia do {PISO}.')
    if feiticos < 1:
        erro('PRECO', f'a regua escolhida ({mult_esc:g}x) deixa o {PISO} de nivel {nv0} com '
                      'zero feiticos no dia — e o nivel em que toda ficha nasce')
    if not zera:
        erro('PRECO', 'nenhuma regua da tabela zera o dia do PISO no nivel 2 — a tabela '
                      'perdeu o degrau que justifica a escolha, e a escolha vira gosto')
    else:
        print(f'  reguas que zerariam o dia no nv{nv0}: {", ".join(zera)}')

# =============================================================================
# 14. ECONOMIA — o teto cai da economia de acao
# =============================================================================
bloco('14. ECONOMIA — o teto cai da economia de acao, e nao de decreto')
if not re.search(r'\*\*Comandar a invocação, a cada rodada, custa a sua ação padrão\.\*\*', PECA):
    erro('ECONOMIA', 'a peca nao escreve que comandar custa a acao padrao — sem isso o teto '
                     'de uma Rotina volta a ser decreto e precisa de mestre policiando')
tab_eco = [c for c in linhas_de_tabela(trecho(S34, '| | ação livre | comandar custa a padrão',
                                              '> **O teto deixa de ser')) if len(c) >= 3]
soma_ok = False
for c in tab_eco:
    if sem_acento(limpo(c[0])).startswith('soma'):
        v = num(c[2])
        soma_ok = v is not None and abs(v - TETO_SOMADO) < 1e-9
print(f'  comandar custa a acao padrao: dono e invocacao ficam mutuamente exclusivos, '
      f'e a soma fica em {TETO_SOMADO} Rotina.')
if not soma_ok:
    erro('ECONOMIA', 'SS3.4: a tabela da economia de acao nao fecha a soma em '
                     f'{TETO_SOMADO} Rotina na coluna de "comandar custa a padrao"')

# =============================================================================
# 15. CORO — a excecao medida somada
# =============================================================================
bloco('15. CORO — a excecao medida somada nao passa de uma Rotina')
saida_coro = COTA['Coro']
if 'somam a mesma Rotina' not in saida_coro['texto']:
    erro('CORO', 'peca 6 SS4: a linha do Coro nao diz mais que dono e invocacao somam a '
                 'MESMA Rotina — se ela passar a somar duas, a excecao vira ação a mais')
ataque_dono = 1.0 / COTA['Servo']['divisor']
ataque_invoc = 1.0 - ataque_dono
total = ataque_dono + ataque_invoc
print(f'  Coro: o dono entrega {ataque_dono:g} e a invocacao {ataque_invoc:g} — '
      f'somados, {total:g} Rotina.')
if total > TETO_SOMADO + 1e-9:
    erro('CORO', f'o Coro entrega {total:g} Rotina somada e o teto e {TETO_SOMADO}')
if ACAO.get('Coro') != 1:
    erro('CORO', 'o SS3.4 deixou de dar ao Coro a excecao de atacar E comandar — sem ela '
                 'as tres Trilhas passam a diferir so em quantidade de corpos')
if sum(ACAO.values()) != 1:
    erro('CORO', f'{sum(ACAO.values())} Trilhas atacam e comandam na mesma rodada — a peca 5 '
                 'SS4 autoriza UMA excecao estreita, e duas nao sao estreitas')
if not re.search(r'exceção estreita e paga na economia de ação', PECA):
    erro('CORO', 'a peca nao ancora a excecao do Coro na frase da peca 5 SS4 — uma excecao '
                 'sem dono declarado vira precedente para a proxima')

# =============================================================================
# 16. BUSCA — todas as montagens legais
# =============================================================================
bloco('16. BUSCA — todas as montagens legais: gasto exato e zero dominadas')


def montagens(pts):
    """todos os conjuntos de entradas que gastam EXATAMENTE pts."""
    itens = [(e['camada'], e['nome'], e['pts']) for e in COMPRAVEIS]
    out = []
    n = len(itens)

    def anda(i, resto, acc):
        if resto == 0:
            out.append(frozenset(acc))
            return
        if i >= n or resto < 0:
            return
        anda(i + 1, resto - itens[i][2], acc + [itens[i][:2]])
        anda(i + 1, resto, acc)
    anda(0, pts, [])
    return out


CACHE = {}
print(f"  {'nv':<5}{'orcamento':<12}{'montagens cheias':<20}{'maior':<8}{'% do catalogo':<15}")
for nv in sorted(ORCAMENTO):
    pts = ORCAMENTO[nv]['pts']
    ms = CACHE.setdefault(pts, montagens(pts))
    maior = max((len(x) for x in ms), default=0)
    print(f'  {nv:<5}{pts:<12}{len(ms):<20}{maior:<8}{maior / len(COMPRAVEIS):<15.0%}')
    if not ms:
        erro('BUSCA', f'nv{nv}: nenhuma montagem gasta o orcamento {pts} exato')
    if len(ms) != len(set(ms)):
        erro('BUSCA', f'nv{nv}: duas montagens com a mesma assinatura')
custos = {e['pts'] for e in COMPRAVEIS}
if min(custos) <= 0:
    erro('BUSCA', 'existe entrada compravel de custo zero — com ela uma montagem pode ser '
                  'superconjunto estrito de outra gastando o mesmo, e a dominancia volta')
else:
    print(f'  toda entrada compravel custa >= {min(custos)}, e toda montagem gasta o '
          'orcamento EXATO —')
    print('  logo nenhuma montagem e superconjunto estrito de outra: zero dominadas, por '
          'construcao.')
topo = max(ORCAMENTO, key=lambda k: ORCAMENTO[k]['pts'])
usadas = set()
for x in CACHE[ORCAMENTO[topo]['pts']]:
    usadas |= x
mortas = [e['nome'] for e in COMPRAVEIS if (e['camada'], e['nome']) not in usadas]
for n in mortas:
    erro('BUSCA', f'"{n}" nao aparece em nenhuma montagem cheia do topo — entrada morta, '
                  'que e o defeito que Equipamento chama de propriedade morta')
if not mortas:
    print(f'  as {len(COMPRAVEIS)} entradas aparecem em alguma montagem cheia do topo.')

# =============================================================================
# 17. INSTANCIAS — as montagens publicadas contra a maquina
# =============================================================================
bloco('17. INSTANCIAS — as montagens publicadas conferidas contra a maquina')
preco = {e['nome']: e['pts'] for e in CATALOGO}
tab_inst = [c for c in linhas_de_tabela(trecho(S37, '### E montar os shikigami', '> **Mas o Coelho'))
            if len(c) >= 4 and num(c[2]) is not None]
if not tab_inst:
    erro('INSTANCIAS', 'SS3.7: nao achei a tabela das montagens publicadas')
print(f"  {'montagem':<20}{'entradas':<32}{'pts':<7}{'doc':<6}{'cabe no nv':<12}{'doc':<6}")
for c in tab_inst:
    nome = limpo(c[0])
    partes = [limpo(x) for x in re.findall(r'`([^`]+)`', c[1])]
    pts_doc, nv_doc = num(c[2]), num(c[3])
    if not partes:
        continue
    faltando = [p for p in partes if p not in preco]
    if faltando:
        erro('INSTANCIAS', f'{nome}: usa {faltando}, que nao esta(o) no catalogo')
        continue
    pts = sum(preco[p] for p in partes)
    cabe = min([nv for nv in sorted(ORCAMENTO) if ORCAMENTO[nv]['pts'] >= pts] or [0])
    print(f'  {nome[:18]:<20}{" + ".join(partes)[:30]:<32}{pts:<7}{pts_doc:<6.0f}'
          f'{cabe:<12}{nv_doc:<6.0f}')
    if pts != pts_doc:
        erro('INSTANCIAS', f'{nome}: as entradas somam {pts} pontos pelo catalogo e a tabela '
                           f'escreve {pts_doc:g}')
    if cabe != nv_doc:
        erro('INSTANCIAS', f'{nome}: {pts} pontos cabem primeiro no nivel {cabe} pelo '
                           f'orcamento, e a tabela escreve {nv_doc:g}')
if not re.search(r'três montagens prontas|três invocações já montadas', PECA):
    aviso('a peca nao publica as tres montagens prontas por Trilha — elas dependem da Q6, '
          'que e da peca de Trilhas. Quando entrarem, esta checagem passa a confere-las.')

# =============================================================================
# 18. RITMO — nada cresce fora do +3
# =============================================================================
bloco('18. RITMO — nenhuma linha derivada cresce fora do ritmo do dono')


def maestria(nv):
    return MAESTRIA_INI + (nv - 1) // MAESTRIA_PASSO


def atributo_investido(nv):
    """peca 2 SS3: comeca em 3 na criacao e vai ate o teto 6, no passo da maestria."""
    return min(6, 3 + (nv - 1) // MAESTRIA_PASSO)


def acerto_dono(nv):
    return atributo_investido(nv) + maestria(nv)


nvs = sorted(ORCAMENTO)
lo, hi = min(nvs), max(nvs)
base_cresce = acerto_dono(hi) - acerto_dono(lo)
print(f"  {'linha':<28}{'nv' + str(lo):<8}{'nv' + str(hi):<8}{'cresce':<9}")
print(f'  {"acerto derivado do dono":<28}{acerto_dono(lo):<8}{acerto_dono(hi):<8}'
      f'+{base_cresce:<9}')
for desl in (0, -1, -2):
    c = (acerto_dono(hi) + desl) - (acerto_dono(lo) + desl)
    print(f'  {"...com deslocamento " + f"{desl:+d}":<28}{acerto_dono(lo) + desl:<8}'
          f'{acerto_dono(hi) + desl:<8}+{c:<9}')
    if c != base_cresce:
        erro('RITMO', f'o deslocamento {desl:+d} muda o RITMO da linha ({c} contra '
                      f'{base_cresce}) — deslocamento fixo nao pode derivar')
# O ALVO do acerto e a DEFESA, e ela tambem tem dois termos que crescem: a Destreza
# do alvo (teto da peca 2) e a protecao de cobrir-se (peca 11 SS6, `1/3 do refino + 1`,
# com o refino topando em 10 pela peca 11 SS3). Ate a v0.116 esta checagem comparava o
# acerto contra UM atributo, porque o acerto tinha um termo so. Com a base da v0.117 ele
# tem dois, e o alvo dele sempre teve dois — a comparacao certa e contra a Defesa.
ATRIBUTO_CRESCE = TETO_ATR - 3
PROTECAO_CRESCE = (TETO_REF // 3 + 1) - (1 // 3 + 1)
DEFESA_CRESCE = ATRIBUTO_CRESCE + PROTECAO_CRESCE
print(f'  {"a Defesa do alvo cresce":<28}{"":<8}{"":<8}+{DEFESA_CRESCE:<9}'
      f'(Destreza +{ATRIBUTO_CRESCE}, protecao +{PROTECAO_CRESCE})')
if base_cresce != DEFESA_CRESCE:
    erro('RITMO', f'o acerto derivado cresce +{base_cresce} e a Defesa do alvo cresce '
                  f'+{DEFESA_CRESCE} (Destreza +{ATRIBUTO_CRESCE} da peca 2, protecao '
                  f'+{PROTECAO_CRESCE} da peca 11) — os dois lados da rolagem deixaram '
                  'de crescer no mesmo ritmo')
else:
    print(f'  contra-teste: os dois lados sao lidos de PECAS DIFERENTES — o acerto da peca 1'
          f' e a Defesa das pecas 2 e 11.')
    print(f'  Perturbar a maestria, o teto de atributo ou o teto de refino desencaixa '
          'a igualdade, e nenhum dos tres mora aqui dentro.')

# =============================================================================
# 19. VIDA — a formula no molde da peca 1
# =============================================================================
bloco('19. VIDA — a formula no molde da peca 1, e a tabela recalculada')
m = re.search(r'\*\*`vida = base do tipo \+ \((\d+) \+ a Constituição dela\) × nível do dono`\*\*', S36)
POR_NIVEL = int(m.group(1)) if m else None
if POR_NIVEL is None:
    erro('VIDA', 'SS3.6: nao achei a formula de vida com o termo de tipo preenchido')
else:
    ok_molde = all(k in PECA for k in ('inicial do Caminho', 'por nível do Caminho')) or \
        re.search(r'peça 1:\s*\(inicial do Caminho', PECA)
    if not ok_molde:
        erro('VIDA', 'a peca nao mostra a formula lado a lado com a da peca 1 — a formula de '
                     'vida tem UM molde, e ele e o do Caminho')
    tab_vida = [c for c in linhas_de_tabela(trecho(S36, '### A fórmula de vida', '### O que a Q3 devia'))
                if len(c) >= 6]
    niveis_vida = []
    for c in tab_vida:
        if sem_acento(limpo(c[0])) in ('tipo',):
            niveis_vida = [int(x) for x in re.findall(r'nv(\d+)', ' '.join(c))]
    if not niveis_vida:
        erro('VIDA', 'SS3.6: nao achei o cabecalho de niveis da tabela de vida')
    print(f"  formula: base do tipo + ({POR_NIVEL} + Con) x nivel do dono, "
          f"impressa com Con {CON_DA_TABELA}")
    print(f"  {'tipo':<34}{'base':<7}" + ''.join(f'nv{n:<7}' for n in niveis_vida))
    for c in tab_vida:
        rotulo = limpo(c[0])
        if 'alvo' in sem_acento(rotulo):
            print(f'  {"alvo — meia Rotina":<34}{"":<7}', end='')
            for i, nv in enumerate(niveis_vida, start=2):
                v = num(c[i]) if i < len(c) else None
                alvo = ROTINA_NV.get(nv)
                if alvo is None:
                    aviso(f'a peca 6 SS3 nao publica Rotina no nivel {nv}; a linha do alvo '
                          'nao pode ser conferida ali')
                    print(f'{"—":<9}', end='')
                    continue
                print(f'{alvo / 2:<9.1f}', end='')
                if v is None or abs(v - alvo / 2) > 0.05:
                    erro('VIDA', f'a linha do alvo escreve {v} no nv{nv} e meia Rotina da '
                                 f'peca 6 SS3 e {alvo / 2:g} (Rotina {alvo}) — a Rotina tem '
                                 'UM dono, e a linha do alvo pegou o valor de outro lugar')
            print()
            continue
        base = num(c[1]) if len(c) > 1 else None
        if base is None:
            continue
        print(f'  {rotulo[:32]:<34}{base:<7.0f}', end='')
        for i, nv in enumerate(niveis_vida, start=2):
            v = num(c[i]) if i < len(c) else None
            calc = base + (POR_NIVEL + CON_DA_TABELA) * nv
            print(f'{calc:<9.0f}', end='')
            if v is None or abs(v - calc) > 0.01:
                erro('VIDA', f'"{rotulo}" no nv{nv}: a formula da {calc:g} e a tabela '
                             f'escreve {v}')
        print()
    bases = [num(c[1]) for c in tab_vida
             if len(c) > 1 and num(c[1]) is not None and 'alvo' not in sem_acento(limpo(c[0]))]
    if len(set(bases)) < 2:
        erro('VIDA', 'todos os tipos tem a mesma base — o termo de tipo voltou a ser um '
                     'numero so, e a formula perdeu o motivo de ter um termo')

# =============================================================================
# 20. POOL — a invariante da Q2
# =============================================================================
bloco('20. POOL — a invariante da Q2: ninguem ganha barra de vida propria')
if not re.search(r'Uma barra de vida só, e o dano que passa de um corpo \*\*cascateia\*\*', PECA):
    erro('POOL', 'a peca nao escreve a barra unica com cascata — sem ela o limiar D = h do '
                 'SS3.2 deixa de valer e a Matilha vira cinco fichas')
suspeitas = []
for ln in PECA.split('\n'):
    s = sem_acento(ln)
    if re.search(r'barra(s)? (de vida )?(propria|separada|por corpo|cada)', s) and \
       'nenhuma' not in s and 'nao' not in s and 'sem ' not in s and 'voltaram' not in s and \
       'desfaz' not in s:
        suspeitas.append(ln.strip()[:100])
for s in suspeitas:
    erro('POOL', f'a peca da barra de vida separada em algum lugar: "{s}..."')
print(f'  barra unica com cascata declarada; {len(suspeitas)} frase(s) concedendo barra '
      'separada.')
print('  (uma Trilha ou aptidao que devolva barras separadas desfaz a conta do limiar '
      'D = h do SS3.2.)')

# =============================================================================
# 21. COTA — 1/n lido da peca 6 SS4
# =============================================================================
bloco('21. COTA — 1/n lido da peca 6 SS4, com n = corpos no campo')
for t in TRILHAS:
    d, corp = COTA[t]['divisor'], COTA[t]['corpos']
    if d is None:
        print(f'  {t:<9} sem cota por corpo (a excecao da economia de acao)')
        continue
    n = int(corp) + (1 if 'a mais' in COTA[t]['texto'] else 0)
    print(f'  {t:<9} 1/{d} em cada, {corp} corpo(s) no campo -> n = {n}')
    if n != d:
        erro('COTA', f'{t}: a peca 6 SS4 divide por {d} e poe {corp} corpo(s) no campo — '
                     f'com o dono contando como um deles isso da n = {n}, e 1/{d} nao fecha')
    if CORPOS_ESPERADOS[t] != int(corp):
        erro('COTA', f'{t}: a peca 6 SS4 mudou para {corp} corpos e este validador declara '
                     f'{CORPOS_ESPERADOS[t]} — atualize a declaracao junto, ou ela mente')

# =============================================================================
# 22. CRITICO
# =============================================================================
bloco('22. CRITICO — o ganho de critico da Matilha, e o salto do pacote unico')
n = CORPOS_MATILHA
P20 = 1 / 20.0
chance = 1 - (1 - P20) ** n
somando = n * P20 * (1.0 / n)          # cada 20 dobra os dados do PROPRIO corpo
pacote = chance * 1.0                  # um 20 dobraria o pacote inteiro
print(f'  {n} d20: P(pelo menos um 20) = {chance:.1%}')
print(f'  somando  — cada 20 dobra os dados do proprio corpo: ganho medio {somando:.0%} da Rotina')
print(f'  pacote   — um 20 dobra o pacote inteiro:            ganho medio {pacote:.0%} da Rotina')
S_CRIT = trecho(S32, '**O 20 natural fecha.**', '### Uma hipótese')
m = re.search(r'`P\(pelo menos um 20\) = ([\d,]+)%`', S_CRIT)
if not m:
    erro('CRITICO', 'SS3.2: a chance de 20 natural em pool nao esta escrita')
elif abs(num(m.group(1)) - chance * 100) > 0.1:
    erro('CRITICO', f'o doc escreve {m.group(1)}% e {n} d20 dao {chance:.1%}')
vals = [num(c[1]) for c in linhas_de_tabela(S_CRIT) if len(c) >= 2 and num(c[1]) is not None]
if len(vals) >= 2:
    if abs(vals[0] - somando * 100) > 0.6:
        erro('CRITICO', f'o ganho da forma SOMADA e {somando:.0%} e o doc escreve {vals[0]:g}%')
    if abs(vals[1] - pacote * 100) > 0.6:
        erro('CRITICO', f'o ganho do PACOTE UNICO e {pacote:.0%} e o doc escreve {vals[1]:g}%')
else:
    erro('CRITICO', 'SS3.2: nao achei a tabela dos dois ganhos de critico')
if pacote <= somando:
    erro('CRITICO', 'o pacote unico deixou de ser pior que a soma — o argumento que escolheu '
                    'a forma somada caiu junto')

# =============================================================================
# 23. INICIATIVA — a invariante da Q1
# =============================================================================
bloco('23. INICIATIVA — a invariante da Q1: ninguem ganha casa separada')
if not re.search(r'compartilha o número de iniciativa do dono e age logo depois', PECA):
    erro('INICIATIVA', 'a peca nao escreve a regra da Q1 como regra — sem ela a tabela do '
                       'SS3.1 volta inteira')
concessoes = []
for e in CATALOGO:
    if re.search(r'iniciativa|age sozinh|age por conta|turno próprio|turno proprio',
                 sem_acento(e['efeito'])):
        concessoes.append(e['nome'])
for nome_ in concessoes:
    erro('INICIATIVA', f'"{nome_}" concede acao fora da casa do dono — uma entrada, uma '
                       'Trilha ou um Legado que faca isso reabre os 97,6% da tabela do SS3.1')
m = re.search(r'\*\*([\d,]+)%\*\*\s*\|\s*52,5%', S31)
if m:
    print(f'  o que a Q1 comprou: com casa por corpo, "um corpo meu age antes do inimigo" '
          f'ia a {m.group(1)}%; na casa do dono fica em 52,5%, com um corpo ou com cinco.')
print(f'  {len(CATALOGO)} entradas varridas, {len(concessoes)} concedendo casa separada.')
print('  E invariante de TEXTO e nao de numero, no molde do teto de Defesa de Equipamento.')

# =============================================================================
# 24. AMARRA
# =============================================================================
bloco('24. AMARRA — os 18 m lidos da peca 3 SS3, nunca de constante')
m = re.search(r'\*\*A invocação tem de ficar a até (\d+) metros do dono\.\*\*', PECA)
AMARRA = int(m.group(1)) if m else None
if AMARRA is None:
    erro('AMARRA', 'a peca nao escreve a amarra como regra')
else:
    print(f'  peca 3 SS3: o alcance base de Projetil e {PROJETIL} m '
          f'(deslocamento base {DESLOC_BASE} m).')
    print(f'  peca 15   : a amarra e {AMARRA} m — {AMARRA / DESLOC_BASE:g} turnos de movimento.')
    if AMARRA != PROJETIL:
        erro('AMARRA', f'a amarra e {AMARRA} m e o alcance base de Projetil da peca 3 SS3 e '
                       f'{PROJETIL} m — o numero tem UM dono, e nao e esta peca. Perturbar '
                       'o Projetil tem de fazer a amarra andar junto, e nao divergir')
    if not re.search(r'não pode ser comandada', PECA):
        erro('AMARRA', 'a peca nao diz o que acontece fora da amarra — foi essa falta que '
                       'a Q4 transformou em pergunta de toda rodada')
    if re.search(r'fora da amarra ela some|além disso ela some', sem_acento(PECA)):
        erro('AMARRA', 'a peca faz a invocacao SUMIR fora da amarra — ai um empurrao apaga '
                       'o preco de invocar de graca')

# =============================================================================
# 25. FAIXAS — nenhuma ganha metro
# =============================================================================
bloco('25. FAIXAS — "na cena" e "fora da cena" nao ganham metro')
S_FAIXA = trecho(S36, '### As três faixas', '### O orçamento cresce')
achou = 0
for c in linhas_de_tabela(S_FAIXA):
    if len(c) < 2:
        continue
    faixa, oque = limpo(c[0]), c[1]
    if 'no combate' in sem_acento(faixa):
        achou += 1
        if str(PROJETIL) not in oque:
            erro('FAIXAS', f'a faixa "no combate" deixou de ser os {PROJETIL} m da amarra')
        continue
    if 'cena' not in sem_acento(faixa):
        continue
    achou += 1
    fora_parenteses = re.sub(r'\([^)]*\)', '', oque)
    if re.search(r'\d+\s*(m\b|metro|km|quilômetro)', fora_parenteses):
        erro('FAIXAS', f'a faixa "{faixa}" ganhou metragem fora dos parenteses: '
                       f'"{oque.strip()}" — medir em metro uma coisa que ninguem vai medir '
                       'e precisao falsa, e vira teste de fita metrica na mesa')
    print(f'  {faixa:<16} {oque.strip()[:58]}')
if achou < 3:
    erro('FAIXAS', f'SS3.6: esperava as tres faixas de alcance, achei {achou}')

# =============================================================================
# 26. GATE — o do Remoto e o unico
# =============================================================================
bloco('26. GATE — o gate de Origem do Remoto e o unico do catalogo')
com_gate = [e['nome'] for e in CATALOGO if 'gate' in sem_acento(f'{e["efeito"]} {e["fonte"]}')
            or 'requisito' in sem_acento(f'{e["efeito"]} {e["fonte"]}')]
print(f'  entradas com requisito declarado: {com_gate or "nenhuma"}')
if len(com_gate) != 1:
    erro('GATE', f'{len(com_gate)} entrada(s) com gate: {com_gate}. A peca 11 SS5 manda cada '
                 'aptidao declarar o gate dela e permite nenhum, so nivel, so refino, ou os '
                 'dois; o de Origem e um QUARTO formato. Um segundo gate no catalogo quer '
                 'dizer que a regua de degrau do SS3.7 parou de precificar sozinha, e isso '
                 'tem de ser decisao e nao descuido')
elif not re.search(r'quarto formato', PECA):
    erro('GATE', 'o gate do Remoto e de Origem, que e um quarto formato ao lado dos tres da '
                 'peca 11 SS5, e a peca nao o declara como tal')

# =============================================================================
# 27. NAO-COMPRA — nenhuma entrada compra linha que ja e deslocamento
# =============================================================================
bloco('27. NAO-COMPRA — nenhuma entrada compra linha que ja e deslocamento')
MOEDA_DO_DESLOCAMENTO = ('defesa', 'acerto', 'vida', 'constituicao')
sujas = []
for e in CATALOGO:
    t = sem_acento(e['efeito'])
    for palavra in MOEDA_DO_DESLOCAMENTO:
        if re.search(rf'\b{palavra}\b', t):
            sujas.append((e['nome'], palavra))
for nome_, palavra in sujas:
    erro('NAO-COMPRA', f'"{nome_}" encosta em {palavra}, que ja e a moeda do deslocamento do '
                       'SS3.6 — dois precos pela mesma coisa e a licao no 2 na forma em que '
                       'ela reincide aqui')
print(f'  {len(CATALOGO)} entradas varridas contra {MOEDA_DO_DESLOCAMENTO}: '
      f'{len(sujas)} encostando.')

# =============================================================================
# 28. CONTAGEM — o catalogo recontado
# =============================================================================
bloco('28. CONTAGEM — o catalogo recontado bate com o que o documento afirma')
n_tr = sum(1 for e in COMPRAVEIS if e['camada'] == 'Traço')
n_cm = sum(1 for e in COMPRAVEIS if e['camada'] == 'Comando')
print(f'  contado na tabela: {len(COMPRAVEIS)} compraveis — {n_tr} Traco e {n_cm} Comando, '
      f'mais {len(GRATIS)} a custo 0 ({", ".join(e["nome"] for e in GRATIS)}).')
afirma = re.findall(r'(\d+)\s*(?:entradas\s+)?compráveis', PECA)
vals = {int(a) for a in afirma}
print(f'  o documento afirma a contagem {len(afirma)}x, dizendo {sorted(vals)}.')
if not vals:
    erro('CONTAGEM', 'a peca nao afirma em lugar nenhum quantas entradas compraveis o '
                     'catalogo tem — e a contagem que envelhece dentro do proprio arquivo')
for v in vals:
    if v != len(COMPRAVEIS):
        erro('CONTAGEM', f'a peca escreve "{v} compraveis" e a tabela dela tem '
                         f'{len(COMPRAVEIS)}')
m = re.search(r'(\d+) `Traço` e (\d+) `Comando`', PECA)
if m:
    if (int(m.group(1)), int(m.group(2))) != (n_tr, n_cm):
        erro('CONTAGEM', f'a peca escreve {m.group(1)} Traco e {m.group(2)} Comando, e a '
                         f'tabela tem {n_tr} e {n_cm}')
else:
    erro('CONTAGEM', 'a peca nao quebra a contagem por camada — foi assim que as contas do '
                     'rascunho da peca 13 envelheceram duas vezes dentro do proprio arquivo')

# =============================================================================
# 29. BUSCA-DEGRAU — o numero escrito ANTES
# =============================================================================
bloco('29. BUSCA-DEGRAU — a busca por degrau bate com o numero escrito antes')
topo_pts = ORCAMENTO[topo]['pts']
ms = CACHE[topo_pts]
maior = max(len(x) for x in ms)
frac = maior / len(COMPRAVEIS)
print(f'  no nv{topo}, orcamento {topo_pts}, gasto exato: {len(ms)} montagens cheias; '
      f'a maior usa {maior} das {len(COMPRAVEIS)} entradas ({frac:.0%}).')
m = re.search(r'entrega \*\*([\d.]+) montagens cheias\*\*', PECA)
if not m:
    erro('BUSCA-DEGRAU', 'o numero esperado da busca nao esta escrito na peca — "escrito '
                         'antes" e a metade que faz a checagem valer alguma coisa')
elif int(m.group(1).replace('.', '')) != len(ms):
    erro('BUSCA-DEGRAU', f'a peca escreve {m.group(1)} montagens e a busca da {len(ms)}')
m = re.search(r'usa \*\*(\d+) das (\d+) entradas — (\d+)%\*\*', PECA)
if not m:
    erro('BUSCA-DEGRAU', 'a peca nao escreve quanto do catalogo a maior montagem consome')
else:
    if (int(m.group(1)), int(m.group(2))) != (maior, len(COMPRAVEIS)):
        erro('BUSCA-DEGRAU', f'a peca escreve "{m.group(1)} das {m.group(2)}" e a busca da '
                             f'{maior} das {len(COMPRAVEIS)}')
    if abs(int(m.group(3)) - frac * 100) > 0.6:
        erro('BUSCA-DEGRAU', f'a peca escreve {m.group(3)}% e a conta da {frac:.0%}')

# =============================================================================
# 30. PISO-DA-VENDA
# =============================================================================
bloco('30. PISO-DA-VENDA — vender deslocamento nao precisa de piso, e isso e medido')
m = re.search(r'\|\s*−1 na Defesa\s*\|[^|]*\|\s*−(\d+)% de vida efetiva\s*\|', S33)
PERDA_POR_PONTO = int(m.group(1)) / 100.0 if m else None
if PERDA_POR_PONTO is None:
    erro('PISO-DA-VENDA', 'SS3.3: nao achei o cambio de −1 de Defesa em vida efetiva')
m = re.search(r'\*\*De (\d+)% a (\d+)% da Rotina', P14)
BANDA_TRILHA = (int(m.group(1)) / 100.0, int(m.group(2)) / 100.0) if m else None
if BANDA_TRILHA is None:
    erro('PISO-DA-VENDA', 'peca 14 SS4: nao achei a banda do que uma Trilha inteira vale')
if PERDA_POR_PONTO and BANDA_TRILHA:
    presenca = POOL_R * (1 - PERDA_POR_PONTO) ** VENDA_MEDIDA
    print(f'  pool cheio: {POOL_R:g} Rotina(s) de presenca em campo.')
    print(f'  vendendo −{VENDA_MEDIDA} de Defesa, a {PERDA_POR_PONTO:.0%} de vida efetiva por '
          f'ponto: {presenca:.2f} Rotina(s).')
    print(f'  uma Trilha inteira vale {BANDA_TRILHA[0]:.0%} a {BANDA_TRILHA[1]:.0%} da Rotina '
          f'(peca 14 SS4) = {BANDA_TRILHA[0]:.2f} a {BANDA_TRILHA[1]:.2f}.')
    print(f'  a venda no fundo do poco ainda entrega {presenca / BANDA_TRILHA[1]:.0f}x o que '
          'uma Trilha inteira vale.')
    if presenca <= BANDA_TRILHA[1]:
        erro('PISO-DA-VENDA', f'vendendo −{VENDA_MEDIDA} de Defesa a presenca cai para '
                              f'{presenca:.2f} Rotina, que e menos que a banda de uma Trilha '
                              f'({BANDA_TRILHA[1]:.2f}) — a venda deixou de se limitar sozinha '
                              'no valor, e agora ela PRECISA de piso. Isso e decisao a tomar, '
                              'nao numero a ajustar')
    else:
        print('  Ela se limita sozinha no valor: nenhum piso e necessario, e isso e medido '
              'em vez de suposto.')

# =============================================================================
# VEREDITO
# =============================================================================
print('\n' + '=' * 88)
for a in AVISOS:
    print(f'  aviso: {a}')
if AVISOS:
    print(f'  {len(AVISOS)} aviso(s), que nao falham o validador.\n')
if ERROS:
    print(f'>>> {len(ERROS)} PROBLEMA(S):')
    for e in ERROS:
        print(f'    - {e}')
    print('=' * 88)
    sys.exit(1)
print('>>> TUDO OK — o teto somado e a cota saem da peca 6, o orcamento sai dos marcos')
print('    da peca 2, a amarra sai da peca 3, a vida sai do molde da peca 1, e as 30')
print('    checagens do SS5 fecham sem nenhum valor escrito dentro deste arquivo.')
print('=' * 88)

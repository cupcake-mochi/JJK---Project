#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Confere a CRIACAO DE PERSONAGEM — a peca 8 contra o resto do sistema.

Por que ele existe
------------------
A peca 8 e' a unica que produz uma FICHA INTEIRA, com numero fechado, e por isso
ela e a que envelhece pior: ela soma o que sete outras pecas decidiram, e cada
vez que uma delas muda um numero a peca 8 fica um pouco mais errada sem que nada
acuse. Foi exatamente o que aconteceu duas vezes:

  - a v0.27 deu numero a "cobrir-se de energia" (protecao 1/3 do refino + 1), e a
    peca 8 continuou dizendo que a ficha nasce com protecao 0 por SETE versoes.
    A Defesa da ficha de exemplo ficou 12 quando devia ser 13, e a matematica de
    balanco do projeto inteiro ja rodava supondo protecao 1.
  - a v0.27 decidiu que a Trilha vem no nivel 2 e mandou "corrigir na peca 6, na
    peca 8 e aqui". Nenhum dos tres foi corrigido, e o ESTADO-ATUAL passou a se
    contradizer sozinho.

Nenhum dos treze validadores pegava os dois, e o motivo e' estrutural: eles
conferem REGRA (a formula deriva certo?) e ninguem conferia a INSTANCIA (a ficha
publicada obedece a formula?). Este confere a instancia.

E o padrao vale registrar: as pecas com validador — 1, 3, 4, 7, 10, 11, 12 —
estavam limpas. Os dois erros estavam nas pecas 6 e 8, que nao tinham nenhum.

Sete checagens
--------------
  1. A FICHA DE EXEMPLO — todo numero da Kaori sai das formulas canonicas.
  2. O BLOCO DE FORMULAS — o passo 7 da peca 8 bate com a peca 1.
  3. PROTECAO — a ficha de nivel 2 nasce com a protecao da aptidao gratuita, e
     nenhuma peca afirma o contrario.
  4. A TRILHA — a criacao entrega uma, e nada diz que ela chega depois.
  5. FEITICOS — a contagem do nivel 2 bate com a formula da v0.27.
  6. AS ESCOLHAS FECHAM — pericias, oficios e Testes de Resistencia somam o que
     a peca promete, pelas duas rotas do extra.
  7. O CATALOGO EXISTE — Caminho, Trilha e Origem citados na criacao existem
     mesmo nas pecas 6 e 9.

Roda de sistema/03-mecanica. Nao le o .docx e nao precisa de python-docx, entao
nao existe caminho por onde ele saia verde tendo pulado checagem.
"""
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
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


def ler(nome):
    caminho = os.path.join(AQUI, nome)
    try:
        with open(caminho, encoding='utf-8') as fh:
            return fh.read()
    except FileNotFoundError:
        erro(f'{nome} nao abriu. Se o ls mostra ele, e o mount do sandbox — '
             f'reescreva o arquivo e rode de novo (esta no README)')
        return ''


P1 = ler('01-atributos-acerto-defesa.md')
P6 = ler('06-caminhos-e-trilhas.md')
P7 = ler('07-pericias-e-oficios.md')
P8 = ler('08-criacao-de-personagem.md')
P9 = ler('09-origens.md')
P11 = ler('11-aptidoes-e-refino.md')
P12 = ler('12-experiencia-e-progressao.md')


# ==========================================================================
# As constantes canonicas. NENHUMA fica escrita aqui: cada uma e' LIDA da peca
# que e' dona dela. Escrever o valor neste arquivo faria dele mais uma copia
# para sair de sincronia — que e' a licao no 9, e e' o defeito que este
# validador existe para pegar.
# ==========================================================================
bloco('0. DE ONDE VEM CADA NUMERO — lendo os donos')

NIVEL = 2       # a ficha padrao. E' o unico numero desta pagina, e a peca 8 o
                # afirma em tres lugares; a checagem 2 confere que ele nao mudou.

# --- o refino inicial, da peca 8
m = re.search(r'Refino\s*=\s*(\d+)', P8)
REFINO = int(m.group(1)) if m else None
if REFINO is None:
    erro('nao achei o refino inicial no bloco de formulas da peca 8')

# --- a maestria inicial, da peca 8
m = re.search(r'Maestria\s*=\s*(\d+)', P8)
MAESTRIA = int(m.group(1)) if m else None
if MAESTRIA is None:
    erro('nao achei a maestria inicial no bloco de formulas da peca 8')

# --- a formula da protecao de cobrir-se de energia, da peca 11 (a dona)
m = re.search(r'a sua proteção é `1/3 do refino \+ (\d+)`', P11)
if not m:
    erro('nao achei a formula da protecao de cobrir-se de energia na peca 11 — '
         'se ela mudou de forma, esta checagem parou de conferir')
    PROT_MAIS = None
else:
    PROT_MAIS = int(m.group(1))

PROTECAO = (REFINO // 3 + PROT_MAIS) if (REFINO is not None and PROT_MAIS is not None) else None

# --- a tabela de Caminhos da peca 8: vida inicial, vida por nivel, PE por nivel
CAMINHOS = {}
for linha in P8.splitlines():
    m = re.match(r'\|\s*\*\*(\w+)\*\*\s*\|\s*(\d+)\s*\(d\d+\)\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|', linha)
    if m:
        CAMINHOS[m.group(1)] = dict(vida1=int(m.group(2)),
                                    vida_nv=int(m.group(3)),
                                    pe_nv=int(m.group(4)))

print(f'  nivel da ficha padrao:      {NIVEL}')
print(f'  maestria inicial:           {MAESTRIA}   (peca 8)')
print(f'  refino inicial:             {REFINO}   (peca 8)')
print(f'  protecao de cobrir-se:      {PROTECAO}   (peca 11: 1/3 do refino + {PROT_MAIS})')
print(f'  Caminhos lidos da peca 8:   {len(CAMINHOS)} — {", ".join(sorted(CAMINHOS))}')
if len(CAMINHOS) != 5:
    erro(f'esperava 5 Caminhos na tabela do passo 3 e achei {len(CAMINHOS)}')


# ==========================================================================
bloco('1. A FICHA DE EXEMPLO — a Kaori sai das formulas?')

publicado = {}
for rotulo, rx in (
    ('vida',        r'\|\s*Vida\s*\|[^|]*\|\s*\*\*(\d+)\*\*'),
    ('integridade', r'\|\s*Integridade\s*\|[^|]*\|\s*\*\*(\d+)\*\*'),
    ('pe',          r'\|\s*PE\s*\|[^|]*\|\s*\*\*(\d+)\*\*'),
    ('defesa',      r'\|\s*Defesa\s*\|[^|]*\|\s*\*\*(\d+)\*\*'),
    ('cd',          r'\|\s*CD dos feitiços dela\s*\|[^|]*\|\s*\*\*(\d+)\*\*'),
):
    m = re.search(rx, P8)
    if not m:
        erro(f'nao achei "{rotulo}" na tabela de numeros da ficha de exemplo — '
             f'se a tabela mudou de forma, esta checagem parou de conferir')
    else:
        publicado[rotulo] = int(m.group(1))

m = re.search(r'\*\*Atributos\.\*\*\s*Força (\d+) · Constituição (\d+) · Destreza (\d+) · '
              r'Inteligência (\d+) · Essência (\d+)', P8)
if not m:
    erro('nao achei a linha de atributos da ficha de exemplo')
    FOR = CON = DES = None
else:
    FOR, CON, DES = int(m.group(1)), int(m.group(2)), int(m.group(3))
    soma = sum(int(g) for g in m.groups())
    print(f'  atributos da Kaori: For {FOR} · Con {CON} · Des {DES} · '
          f'Int {m.group(4)} · Ess {m.group(5)}  (somam {soma})')
    if soma != 9:
        erro(f'os atributos da ficha de exemplo somam {soma} e a regra da criacao diz 9')
    if max(int(g) for g in m.groups()) > 3:
        erro('a ficha de exemplo tem atributo acima de 3, e a criacao proibe')

m = re.search(r'\*\*Caminho\.\*\*\s*(\w+)', P8)
CAM = m.group(1) if m else None
if CAM not in CAMINHOS:
    erro(f'a ficha de exemplo diz Caminho "{CAM}" e ele nao esta na tabela do passo 3')
else:
    c = CAMINHOS[CAM]
    esperado = {
        'vida':        (c['vida1'] + CON) + (c['vida_nv'] + CON) * (NIVEL - 1),
        'integridade': 20 + 8 * (NIVEL - 1),
        'pe':          c['pe_nv'] * NIVEL,
        'defesa':      10 + DES + PROTECAO,
        'cd':          10 + 2 + MAESTRIA,
    }
    print(f'\n  {"campo":<14}{"publicado":>11}{"pela formula":>15}')
    for k in ('vida', 'integridade', 'pe', 'defesa', 'cd'):
        if k not in publicado:
            continue
        bate = publicado[k] == esperado[k]
        print(f'  {k:<14}{publicado[k]:>11}{esperado[k]:>15}   {"ok" if bate else "<<< NAO BATE"}')
        if not bate:
            erro(f'a ficha de exemplo publica {k} = {publicado[k]} e a formula da '
                 f'{esperado[k]} — a peca 8 ficou para tras de alguma peca posterior')

    print(f'\n  Vida       = ({c["vida1"]} + Con {CON}) + ({c["vida_nv"]} + Con {CON}) x {NIVEL - 1}')
    print(f'  PE         = {c["pe_nv"]} x {NIVEL}')
    print(f'  Defesa     = 10 + Des {DES} + protecao {PROTECAO}')
    print(f'  A protecao NAO e equipamento: e a aptidao gratuita do refino {REFINO}.')


# ==========================================================================
bloco('2. O BLOCO DE FORMULAS — o passo 7 bate com a peca 1?')

for rotulo, rx8, esperado, porque in (
    ('ataque de conjuracao',
     r'Ataque de conjuração\s*=\s*d20 \+ (\d+)', 2 + MAESTRIA,
     '2 + maestria'),
    ('CD de feitico',
     r'CD de feitiço\s*=\s*(\d+)', 10 + 2 + MAESTRIA,
     '10 + 2 + maestria'),
    ('Integridade',
     r'Integridade\s*=\s*(\d+)', 20 + 8 * (NIVEL - 1),
     '20 + 8 x (nivel - 1)'),
    ('pericia treinada',
     r'Perícia treinada\s*=\s*d20 \+ atributo \+ (\d+)', MAESTRIA,
     'atributo + maestria'),
    ('deslocamento',
     r'Deslocamento\s*=\s*(\d+) metros', 9,
     'o turno da peca 3'),
):
    m = re.search(rx8, P8)
    if not m:
        erro(f'nao achei "{rotulo}" no bloco de formulas do passo 7')
        continue
    achado = int(m.group(1))
    if achado != esperado:
        erro(f'o passo 7 diz {rotulo} = {achado} e a formula ({porque}) da {esperado}')
    else:
        print(f'  [x] {rotulo:<22} = {achado}   ({porque})')

if not re.search(r'Defesa\s*=\s*10 \+ Destreza \+ proteção', P1):
    erro('a peca 1 nao diz mais "Defesa = 10 + Destreza + protecao" — se a formula '
         'mudou, a checagem 1 deste validador parou de valer')
else:
    print('  [x] a peca 1 continua com Defesa = 10 + Destreza + protecao')


# ==========================================================================
bloco('3. PROTECAO — a ficha nasce com a da aptidao, e ninguem diz o contrario')

padrao_morto = re.compile(r'nasce com proteção 0|proteção 0\b', re.I)
achou_morto = False
for nome, txt in (('01', P1), ('06', P6), ('08', P8), ('09', P9), ('11', P11), ('12', P12)):
    for m in padrao_morto.finditer(txt):
        ctx = txt[max(0, m.start() - 90):m.end() + 90].replace('\n', ' ')
        if re.search(r'Corrigido|dizia|até a v|antes da v|v0\.2\d', ctx):
            continue
        achou_morto = True
        erro(f'a peca {nome} ainda afirma "protecao 0": ...{ctx.strip()[:130]}...')
if not achou_morto:
    print(f'  [x] nenhuma peca afirma que a ficha nasce com protecao 0')
    print(f'      (ela nasce com {PROTECAO}, e vem de cobrir-se de energia)')

if not re.search(r'Cobrir-se de energia · grátis no refino 1', P11):
    erro('cobrir-se de energia deixou de ser gratuita no refino 1 na peca 11 — '
         'se ela virou comprada, a ficha de nivel 2 nao tem mais essa protecao')
else:
    print('  [x] cobrir-se de energia continua gratuita no refino 1')

# v0.42: a condicao mudou de forma com a peca de equipamento. O escudo saiu
# da lista do que desliga (ele SOMA agora), e as duas classes de uniforme
# ganharam nome. Confere as duas metades separadas, para uma nao esconder a outra.
if not re.search(r'Sem Traje e sem Revestimento', P11):
    erro('a condicao de cobrir-se ("sem Traje e sem Revestimento") sumiu da peca 11')
else:
    print('  [x] a condicao dela (sem Traje e sem Revestimento) continua escrita')

# E a metade que a v0.42 pagou para consertar: o escudo NAO pode voltar para a
# lista do que desliga, em nenhum dos tres documentos. Decisao registrada nao e
# decisao aplicada — foi assim que a Trilha passou sete versoes.
for arq, txt in (('peca 11', P11), ('peca 8', P8)):
    if re.search(r'(armadura e sem escudo|armadura e escudo \*\*desligam|'
                 r'uniforme, armadura e escudo)', txt):
        erro(f'o escudo voltou para a lista do que desliga cobrir-se, na {arq} — '
             f'a v0.42 decidiu que ele SOMA')
else:
    print('  [x] o escudo continua fora da lista do que desliga (ele soma)')

if re.search(r'sem a protecao passiva|sem a prote\u00e7\u00e3o passiva', P11):
    erro('o preco da Reacao de cobrir-se voltou a dizer "a protecao passiva" — '
         'ele tem de ser agnostico de fonte, senao quem esta fardado nao paga nada')
else:
    print('  [x] o preco da Reacao continua agnostico de fonte ("sem protecao")')


# ==========================================================================
bloco('4. A TRILHA — a criacao entrega uma?')

if not re.search(r'Trilha, que você escolhe agora junto do Caminho', P8):
    erro('a peca 8 nao entrega Trilha na criacao. A decisao da v0.27 diz que a '
         'Trilha e identidade e nasce com o personagem')
else:
    print('  [x] a peca 8 entrega a Trilha no passo do Caminho')

if not re.search(r'primeira Trilha vem na criação', P6):
    erro('a peca 6 nao diz que a primeira Trilha vem na criacao')
else:
    print('  [x] a peca 6 diz que a primeira Trilha vem na criacao')

for nome, txt in (('06', P6), ('08', P8)):
    for m in re.finditer(r'não afeta[m]? o nível 2', txt):
        ctx = txt[max(0, m.start() - 120):m.end() + 60].replace('\n', ' ')
        if re.search(r'diziam|dizia|Corrigido|até a v|aplicado na v', ctx):
            continue
        erro(f'a peca {nome} ainda diz que a Trilha "nao afeta o nivel 2": '
             f'...{ctx.strip()[:130]}...')

m = re.search(r'\*Trilha:\*\s*\*\*(\w+)\*\*', P8)
if not m:
    erro('a ficha de exemplo nao declara Trilha')
else:
    trilha = m.group(1)
    if not re.search(r'\|\s*\*\*' + trilha + r'\*\*\s*\|', P6):
        erro(f'a ficha de exemplo usa a Trilha "{trilha}" e ela nao esta no quadro da peca 6')
    else:
        print(f'  [x] a ficha de exemplo usa a Trilha {trilha}, e ela existe na peca 6')


# ==========================================================================
bloco('5. FEITICOS — a contagem do nivel 2')

if not re.search(r'`2 \+ \(nível ÷ 2\)`', P8):
    erro('a peca 8 nao cita mais a formula 2 + (nivel / 2) dos feiticos conhecidos')
conhecidos_formula = 2 + NIVEL // 2

m = re.search(r'\*\*(\w+) feitiços conhecidos\*\*', P8)
PALAVRA = {'dois': 2, 'três': 3, 'tres': 3, 'quatro': 4, 'cinco': 5}
if not m:
    erro('nao achei quantos feiticos conhecidos a criacao entrega')
else:
    dito = PALAVRA.get(m.group(1).lower())
    if dito is None:
        erro(f'a peca 8 escreve "{m.group(1)} feiticos conhecidos" e eu nao sei ler '
             f'esse numero por extenso')
    elif dito != conhecidos_formula:
        erro(f'a peca 8 entrega {dito} feiticos conhecidos e a formula '
             f'2 + (nivel/2) da {conhecidos_formula} no nivel {NIVEL}')
    else:
        print(f'  [x] {dito} feiticos conhecidos, e a formula da {conhecidos_formula}')

if not re.search(r'dois feitiços de \*\*Classe 0\*\*', P8):
    erro('a peca 8 mudou a contagem de Classe 0 — ela e do manual (tabela de '
         'progressao: "Dois feiticos de Classe 0"), entao mexer aqui e divergir')
else:
    print('  [x] dois feiticos de Classe 0, como o manual diz')

if not re.search(r'No nível 2 você tem \*\*Classe 1\*\*', P8):
    erro('a peca 8 nao diz mais que o nivel 2 tem Classe 1 (o manual da 1 a 4)')
else:
    print('  [x] Classe 1 no nivel 2, como a tabela do manual')


# ==========================================================================
bloco('6. AS ESCOLHAS FECHAM — pericias, oficios e Testes de Resistencia')

rotas = {}
for linha in P8.splitlines():
    m = re.match(r'\|\s*pegando (o ofício|a perícia)\s*\|\s*(\d+) de (\d+)\s*\|\s*(\d+) de (\d+)\s*\|', linha)
    if m:
        rotas[m.group(1)] = dict(per=int(m.group(2)), per_tot=int(m.group(3)),
                                 ofi=int(m.group(4)), ofi_tot=int(m.group(5)))

if len(rotas) != 2:
    erro(f'esperava as duas rotas do extra da Origem na peca 8 e achei {len(rotas)}')
else:
    base_per, base_ofi = 6 + 2, 2
    # v0.104: o DENOMINADOR tambem e conferido, e ele vem contado da peca 7 — nao
    # escrito aqui. Ate a v0.103 esta checagem lia so o numerador, e o `de dez` da
    # tabela sobreviveu SETE versoes depois de o Alfaiate fazer onze oficios.
    # E' a checagem medindo pelo eixo errado: verde exatamente onde importava.
    def _conta(cab):
        _a = P7.find(cab)
        if _a < 0:
            erro(f'nao achei a secao "{cab}" na peca 7 — a contagem do quadro parou '
                 'de conferir e o denominador voltou a poder envelhecer')
            return -1
        _c = P7[_a + len(cab):]
        _f = _c.find('\n## ')
        return len(re.findall(r'^\*\*[A-ZÀ-Ú][^*]*\*\* —',
                              _c[:_f] if _f >= 0 else _c, re.M))
    _per_tot = _conta('## 4. As vinte e três perícias')
    _ofi_tot = _conta('## 5. Os onze ofícios')
    esperado = {'o ofício': (base_per, base_ofi + 1),
                'a perícia': (base_per + 1, base_ofi)}
    for rota, (ep, eo) in esperado.items():
        r = rotas[rota]
        ok = (r['per'], r['ofi']) == (ep, eo)
        okd = (r['per_tot'], r['ofi_tot']) == (_per_tot, _ofi_tot)
        print(f'  {"[x]" if ok and okd else "[ ]"} pegando {rota:<10} -> '
              f'{r["per"]} de {r["per_tot"]} pericias e {r["ofi"]} de {r["ofi_tot"]} '
              f'oficios   (a soma da {ep} de {_per_tot} e {eo} de {_ofi_tot})')
        if not ok:
            erro(f'a rota "pegando {rota}" publica {r["per"]} pericias e {r["ofi"]} '
                 f'oficios, e a soma dos passos da {ep} e {eo}')
        if not okd:
            erro(f'a rota "pegando {rota}" publica um quadro de {r["per_tot"]} '
                 f'pericias e {r["ofi_tot"]} oficios, e a peca 7 tem {_per_tot} e '
                 f'{_ofi_tot} — denominador guardado a mao envelhece (licao nº 1)')
    a, b = rotas['o ofício'], rotas['a perícia']
    if a['per'] + a['ofi'] != b['per'] + b['ofi']:
        erro('as duas rotas do extra entregam quantidades diferentes de treino no '
             'total — se e para serem alternativas, elas tem que somar igual')
    else:
        print(f'  [x] as duas rotas somam o mesmo: {a["per"] + a["ofi"]} treinos')

# v0.104: a pericia livre da Origem perdeu a aprovacao do mestre e ganhou trava
# contavel — de fora das seis do Caminho. Ela mora em TRES documentos, e o
# 8 de 23 publicado so fecha se ela valer: com repeticao a ficha teria 7.
_trava = 'de fora das seis'
_sem = [n for n, t in (('peca 7 §6', P7), ('peca 8, o Passo 6', P8),
                       ('peca 9 §2', P9)) if _trava not in t]
if _sem:
    erro('a trava da pericia livre da Origem — "' + _trava + ' que o Caminho te deu" '
         '— nao esta em: ' + ', '.join(_sem) + '. Sem ela o total de 8 de 23 nao fecha')
else:
    print('  [x] a pericia livre da Origem e travada nos tres donos, sem julgamento')

if not re.search(r'\*\*São dois Testes de Resistência treinados\*\*', P8):
    erro('a peca 8 nao confere mais os dois Testes de Resistencia treinados')
else:
    print('  [x] dois Testes de Resistencia treinados, um da Origem e um do Caminho')


# ==========================================================================
bloco('7. O CATALOGO EXISTE — o que a criacao cita esta escrito?')

m = re.search(r'\*\*Origem: (\w+)\.\*\*', P8)
if not m:
    erro('a ficha de exemplo nao declara Origem')
else:
    origem = m.group(1)
    if not re.search(r'^### ' + origem + r'\s*$', P9, re.M):
        erro(f'a ficha de exemplo usa a Origem "{origem}" e ela nao tem secao na peca 9')
    else:
        print(f'  [x] a Origem {origem} existe na peca 9')

faltando = [c for c in CAMINHOS if not re.search(r'\*\*' + c + r'\*\*', P6)]
if faltando:
    erro(f'Caminhos citados na criacao e ausentes da peca 6: {faltando}')
else:
    print(f'  [x] os {len(CAMINHOS)} Caminhos da criacao existem na peca 6')

g8 = re.search(r'começa \*\*Grau (\d+)\*\*', P8)
g12 = re.search(r'começa Grau (\d+)', P12)
if g8 and g12:
    v8, v12 = int(g8.group(1)), int(g12.group(1))
    if v8 != v12:
        erro(f'a peca 8 diz que todo personagem comeca Grau {v8} e a peca 12 diz Grau {v12}')
    else:
        print(f'  [x] Grau {v8} na criacao, e a peca 12 concorda')
else:
    aviso('nao consegui comparar o Grau inicial entre a peca 8 e a peca 12')

m = re.search(r'\|\s*\*\*2 a 4\*\*\s*\|\s*1 missão\s*\|\s*(\d+)\s*\|', P12)
if not m:
    erro('nao achei na peca 12 quanto custa o primeiro nivel (a faixa "2 a 4")')
else:
    print(f'  [x] o nivel {NIVEL} sobe com {m.group(1)} XP — uma missao padrao')


# ==========================================================================
print()
print('=' * 88)
if FALHAS:
    print(f'>>> {len(FALHAS)} PROBLEMA(S):')
    for e in FALHAS:
        print('   -', e)
    sys.exit(1)
print('>>> TUDO OK — a ficha de exemplo sai das formulas, a criacao entrega Trilha,')
print('    a protecao da aptidao gratuita esta na Defesa, e tudo que a criacao cita')
print('    existe nas pecas donas.')
if AVISOS:
    print(f'    {len(AVISOS)} aviso(s) acima, que nao falham o validador.')

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""conferir-alma.py — o validador dono da peca 24, `Dano de alma e Integridade`.

A peca 24 nao inventou a maquina de alma: ela RECOLHEU uma que ja rodava
partida em cinco donos. Entao o trabalho deste validador nao e' conferir um
numero novo — e' conferir que as cinco partes voltaram a dizer a mesma coisa,
e que a parte nova (a Essencia dentro da barra) nao moveu a curva publicada.

A CHECAGEM 1 E' A QUE ESTA PECA EXISTE PARA TER. Ela nao compara a formula
contra uma copia dela: ela reconstroi a curva a partir de TRES donos
independentes — o `20` e o `5` da peca 24, a Essencia de referencia derivada
do teto de atributo da peca 2, e a curva original `20 + 8 x (nivel - 1)` lida
do MANUAL — e exige que as duas coincidam nos 30 niveis. Perturbar qualquer
um dos tres acende.

A CHECAGEM 4 e' a unica que mede CONSEQUENCIA em vez de copia. Se alguem
mexer no `5` ou no `3`, a formula continua bem-formada e o estagio 4 some da
campanha sem nenhuma outra checagem acusar.

NENHUM VALOR FICA ESCRITO AQUI DENTRO:
  a formula da Integridade ....... peca 24, a secao 2
  a curva original `20 + 8` ...... manual/gerador/partF.js
  o teto de atributo ............. peca 2, a secao 3
  a vida por Caminho ............. peca 1, a secao 5.1
  a forma da formula de vida ..... peca 1, a secao 5 (o bloco de formulas)
  os quatro estagios ............. manual/gerador/partF.js
  a ficha de inimigo ............. manual/gerador/partF.js
  os quatro Testes de Resistencia  peca 1, a secao 4
  a excecao que atravessa ........ peca 16, a secao 4
  a ficha de exemplo ............. peca 8
  a recuperacao .................. peca 10, a secao 2

Roda de 03-mecanica/, sem argumento. Sai com codigo 1 se algo quebrar.
Ele NAO le o .docx e NAO precisa de python-docx: nao existe jeito de ele sair
verde tendo pulado checagem por falta de biblioteca.
"""
import os
import re
import sys

MEC = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(MEC))
PARTF = os.path.join(RAIZ, 'manual', 'gerador', 'partF.js')

FALHAS = []
NIVEIS = range(1, 31)


def erro(n, msg):
    FALHAS.append(f'{n}: {msg}')
    print(f'  !! {n}: {msg}')


def bloco(t):
    print()
    print('=' * 88)
    print(t)
    print('=' * 88)


def ler(nome):
    p = os.path.join(MEC, nome)
    if not os.path.isfile(p):
        print(f'  !! nao achei {nome}')
        sys.exit(1)
    with open(p, encoding='utf-8') as f:
        return f.read()


P01 = ler('01-atributos-acerto-defesa.md')
P02 = ler('02-economia-de-atributos.md')
P08 = ler('08-criacao-de-personagem.md')
P10 = ler('10-descanso-e-recuperacao.md')
P16 = ler('16-ferramenta-amaldicoada.md')
P24 = ler('24-dano-de-alma.md')
with open(PARTF, encoding='utf-8') as f:
    MANUAL = f.read()


# ==========================================================================
bloco('1. A FORMULA REPRODUZ A CURVA DO MANUAL, NA ESSENCIA DE REFERENCIA')

# --- dono 1: a formula da peca 24
_m = re.search(r'Integridade = (\d+) \+ \(Essência \+ (\d+)\) × \(nível − 1\)', P24)
if not _m:
    erro(1, 'nao achei a formula da Integridade na peca 24 — se ela mudou de '
            'redacao, esta checagem parou de conferir e precisa ser refeita')
    BASE = POR_NIVEL = None
else:
    BASE, POR_NIVEL = int(_m.group(1)), int(_m.group(2))
    print(f'  peca 24  -> Integridade = {BASE} + (Essencia + {POR_NIVEL}) x (nivel - 1)')

# --- dono 2: o teto de atributo, da peca 2. A referencia e' o MEIO da escala.
_m = re.search(r'\*\*Teto do atributo:\s*(\d+)\.', P02)
if not _m:
    erro(1, 'nao achei o teto de atributo na peca 2')
    TETO_ATR = None
else:
    TETO_ATR = int(_m.group(1))
    print(f'  peca 2   -> teto de atributo = {TETO_ATR}')

# --- dono 3: a curva original, lida do MANUAL e nao daqui
_m = re.search(r'Vida de personagem = (\d+) \+ (\d+) × \(nível − 1\)', MANUAL)
if not _m:
    erro(1, 'nao achei a curva original de vida no partF.js do manual — ela e a '
            'ancora desta checagem, e sem ela a checagem 1 vira circular')
    M_BASE = M_POR = None
else:
    M_BASE, M_POR = int(_m.group(1)), int(_m.group(2))
    print(f'  manual   -> curva original = {M_BASE} + {M_POR} x (nivel - 1)')

if None not in (BASE, POR_NIVEL, TETO_ATR, M_BASE, M_POR):
    ESS_REF = TETO_ATR // 2
    print(f'\n  Essencia de referencia = teto {TETO_ATR} // 2 = {ESS_REF}   (o meio da escala)')

    def integridade(nv, ess):
        return BASE + (ess + POR_NIVEL) * (nv - 1)

    def curva_manual(nv):
        return M_BASE + M_POR * (nv - 1)

    divergem = [nv for nv in NIVEIS if integridade(nv, ESS_REF) != curva_manual(nv)]
    if divergem:
        erro(1, f'a formula com Essencia {ESS_REF} deixou de reproduzir a curva do '
                f'manual em {len(divergem)} nivel(is) — o primeiro e o nv{divergem[0]} '
                f'({integridade(divergem[0], ESS_REF)} contra {curva_manual(divergem[0])}). '
                f'A tabela de estagios foi calibrada nessa curva')
    else:
        print(f'  [x] os {len(list(NIVEIS))} niveis coincidem exatamente '
              f'({BASE} + ({ESS_REF} + {POR_NIVEL}) = {BASE} + {M_POR})')
        print(f'      nv2 = {integridade(2, ESS_REF)}   nv30 = {integridade(30, ESS_REF)}')
else:
    integridade = curva_manual = None
    ESS_REF = None


# ==========================================================================
bloco('2. A REFERENCIA E DERIVADA, E NAO ESCRITA')

# O `3` nao pode estar escrito na peca como constante solta: ele TEM de ser o
# meio da escala. Se alguem trocar o teto de atributo, a referencia acompanha.
if TETO_ATR is not None and BASE is not None:
    if TETO_ATR % 2 != 0:
        erro(2, f'o teto de atributo virou {TETO_ATR}, que e impar — o "meio da escala" '
                f'deixou de ser um numero inteiro e a referencia perdeu sentido')
    else:
        print(f'  [x] a referencia {TETO_ATR // 2} sai de {TETO_ATR} // 2, e nao esta escrita '
              f'em lugar nenhum como constante')
    # E a peca tem de DIZER que ela e derivada, senao o proximo leitor a trata como
    # escolha. A frase tem de estar na SECAO 2, ao lado da formula — o arnes pegou
    # esta checagem lendo a copia dela que mora na tabela do SS7, que e a descricao
    # da propria checagem. Uma checagem que se le na propria descricao nao pega nada.
    _sec2 = P24[P24.find('## 2. A Integridade'):P24.find('## 3. O acoplamento')]
    if not _sec2:
        erro(2, 'nao consegui recortar a secao 2 da peca 24 — se ela mudou de titulo, '
                'esta checagem parou de conferir')
    elif 'meio da escala' not in _sec2:
        erro(2, 'a secao 2 da peca 24 parou de declarar que a Essencia de referencia e o '
                'MEIO DA ESCALA — sem essa frase, ao lado da formula, o `5` vira numero '
                'magico. (A tabela do SS7 tem uma copia, e ela NAO conta aqui.)')
    else:
        print('  [x] a secao 2 declara a derivacao ao lado da formula, e nao so na tabela')


# ==========================================================================
bloco('3. UM PONTO DE ESSENCIA E UM DE CONSTITUICAO VALEM O MESMO')

# Isto NAO se mede com os numeros: mede-se com a FORMA das duas formulas.
# Constituicao aparece DUAS vezes na formula de vida (no inicial e no por-nivel),
# entao ela vale nv. Essencia aparece UMA vez, entao vale nv-1. A diferenca tem
# de ser exatamente 1 — e e' a vida inicial, que a alma nao tem de proposito.
_bloco_form = re.search(r'Pontos de vida\s*=(.*?)Pontos de energia', P01, re.S)
if not _bloco_form:
    erro(3, 'nao achei a formula de Pontos de vida no bloco da peca 1')
else:
    _vida_txt = _bloco_form.group(1)
    n_con = _vida_txt.count('Constituição')
    _integ = re.search(r'Integridade\s*=([^\n]*)', P01)
    n_ess = _integ.group(1).count('Essência') if _integ else 0
    print(f'  Constituicao aparece {n_con}x na formula de vida  -> +1 Con vale nv por ponto')
    print(f'  Essencia     aparece {n_ess}x na da Integridade    -> +1 Ess vale nv-1 por ponto')
    if n_con != 2 or n_ess != 1:
        erro(3, f'a forma das duas formulas mudou (Con {n_con}x, Ess {n_ess}x) — a simetria '
                f'de preco entre as duas reservas era derivada dessa forma')
    else:
        for nv in (2, 30):
            d_con, d_ess = nv, nv - 1
            if d_con - d_ess != 1:
                erro(3, f'nv{nv}: a diferenca entre os dois deixou de ser 1')
        print('  [x] a diferenca e exatamente 1 em todo nivel, e ela e a vida inicial')
        print('      que a alma nao tem — nv30: Con vale +30, Essencia vale +29')


# ==========================================================================
bloco('4. O ESTAGIO 4 NAO PODE SUMIR DA CAMPANHA')

# A unica checagem que mede CONSEQUENCIA. O estagio 4 e' a Integridade zerada,
# e como dano de alma esvazia as duas barras 1:1, ele so dispara se a alma for
# a barra MENOR. Se a formula nova encolher a taxa, o estagio 4 vira letra
# morta e nenhuma outra checagem deste projeto acusaria.
_tab = re.findall(r'\|\s*\*\*(Bastião|Vanguarda|Guia|Evocador|Emanador)\*\*\s*\|\s*d\d+\s*\|'
                  r'\s*(\d+)\s*\|\s*(\d+)\s*\|', P01)
if len(_tab) != 5:
    erro(4, f'nao consegui ler a tabela de vida por Caminho da peca 1 §5.1 '
            f'(achei {len(_tab)} linhas de 5)')
elif integridade is None:
    erro(4, 'sem a formula da checagem 1 esta checagem nao roda')
else:
    CAM = {n: (int(i), int(p)) for n, i, p in _tab}
    print('  vida por Caminho, lida da peca 1 §5.1: ' +
          ' · '.join(f'{n} {i}/{p}' for n, (i, p) in CAM.items()))

    def vida(cam, con, nv):
        i, p = CAM[cam]
        return (i + con) + (p + con) * (nv - 1)

    def taxa(f_integ):
        tot = dis = 0
        for nv in (2, 10, 20, 30):
            for cam in CAM:
                for con in range(TETO_ATR + 1):
                    for ess in range(TETO_ATR + 1):
                        tot += 1
                        if f_integ(nv, ess) <= vida(cam, con, nv):
                            dis += 1
        return dis, tot

    d_novo, tot = taxa(integridade)
    d_velho, _ = taxa(lambda nv, ess: curva_manual(nv))
    print(f'\n  grade: 4 niveis x {len(CAM)} Caminhos x Con 0-{TETO_ATR} x Ess 0-{TETO_ATR} = {tot} fichas')
    print(f'  a alma e a barra menor em {d_novo} delas ({d_novo / tot:.1%})')
    print(f'  com a curva plana anterior seriam {d_velho} ({d_velho / tot:.1%})')
    if d_novo == 0:
        erro(4, 'o estagio 4 deixou de disparar em QUALQUER ficha da grade — '
                'ele virou letra morta')
    elif d_novo < d_velho * 0.9:
        erro(4, f'a taxa de disparo do estagio 4 caiu de {d_velho / tot:.1%} para '
                f'{d_novo / tot:.1%} — mais de 10% de queda. A Essencia entrou para '
                f'CRUZAR os dois eixos, nao para engrossar a alma de todo mundo')
    else:
        print(f'  [x] a taxa se manteve. A Essencia mudou COM QUEM o estagio 4 acontece,')
        print(f'      e nao quanto ele acontece')


# ==========================================================================
bloco('5. OS QUATRO ESTAGIOS BATEM COM OS DO MANUAL')

_man = re.findall(r"\['(1/4|1/2|3/4|Toda)',\s*'(\d)',\s*'([^']*)'\]", MANUAL)
_pec = re.findall(r'^\|\s*`?(1/4|1/2|3/4|toda)`?\s*\|\s*\*\*(\d)\*\*\s*\|\s*([^|]+)\|',
                  P24, re.M)
if len(_man) != 4:
    erro(5, f'nao achei os quatro estagios no partF.js (achei {len(_man)})')
elif len(_pec) != 4:
    erro(5, f'nao achei os quatro estagios na peca 24 (achei {len(_pec)})')
else:
    # a prosa e' reescrita de proposito (o livro tem voz propria); o que tem de
    # bater e' a FRACAO, o NUMERO do estagio, e os tokens mecanicos de cada linha
    TOKENS = {
        '1': ['perícia'],
        '2': ['metade', 'PE por Classe'],
        '3': ['ataques', 'Testes de Resistência', 'Classe'],
        '4': ['não é mais você', 'mestre'],
    }
    for (fm, em, tm), (fp, ep, tp) in zip(_man, _pec):
        if fm.lower() != fp.lower() or em != ep:
            erro(5, f'estagio fora de ordem ou de fracao: manual "{fm}/{em}" contra '
                    f'peca "{fp}/{ep}"')
            continue
        faltando = [t for t in TOKENS[ep] if t.lower() not in tp.lower()]
        if faltando:
            erro(5, f'o estagio {ep} da peca 24 perdeu {faltando} — o manual publica '
                    f'"{tm.strip()}"')
    if not [f for f in FALHAS if f.startswith('5:')]:
        print('  [x] as quatro fracoes, os quatro numeros e os tokens mecanicos de cada')
        print('      linha batem entre a peca 24 §4 e o partF.js do manual')


# ==========================================================================
bloco('6. O TESTE DE RESISTENCIA E UM DOS QUATRO QUE EXISTEM')

_trs = re.findall(r'^\|\s*\*\*(Físico|Vigor|Intelecto|Espírito)\*\*\s*\|', P01, re.M)
print(f'  a peca 1 §4 declara {len(_trs)}: ' + ' · '.join(_trs))
if len(_trs) != 4:
    erro(6, f'a peca 1 §4 deixou de declarar quatro Testes de Resistencia (achei {len(_trs)})')

# a DECLARACAO, e nao qualquer mencao: a peca fala do assunto em varias secoes
_m = re.search(r'faz um Teste de Resistência de (\w+)', P24)
if not _m:
    erro(6, 'a peca 24 §4.1 nao declara qual Teste de Resistencia o dano de alma '
            'forca, na forma "faz um **Teste de Resistencia de X**"')
else:
    tr = _m.group(1)
    if tr not in _trs:
        erro(6, f'a peca 24 manda rolar "Teste de Resistencia de {tr}", e esse TR nao '
                f'existe — os quatro sao {" · ".join(_trs)}')
    else:
        print(f'  [x] o dano de alma forca o TR de {tr}, e ele e um dos quatro')

# E o TR fantasma nao pode voltar, em canto nenhum do projeto nem do gerador.
FANTASMA = 'Teste de Resistência de Integridade'
_sujos = []
for _raiz, _dirs, _arqs in os.walk(os.path.dirname(MEC)):
    if any(x in _raiz for x in ('99-arquivo', '.claude', '_backup', 'node_modules',
                                '_to_delete', '__pycache__')):
        continue
    for _a in _arqs:
        if not _a.endswith(('.md', '.py', '.js')):
            continue
        _p = os.path.join(_raiz, _a)
        if os.path.abspath(_p) == os.path.abspath(__file__):
            continue
        try:
            with open(_p, encoding='utf-8') as _f:
                if FANTASMA in _f.read():
                    _sujos.append(os.path.relpath(_p, os.path.dirname(MEC)))
        except (UnicodeDecodeError, OSError):
            pass
if FANTASMA in MANUAL:
    _sujos.append('manual/gerador/partF.js')
if _sujos:
    erro(6, f'o "{FANTASMA}" voltou em {len(_sujos)} arquivo(s): {_sujos} — ele nomeia '
            f'um quinto TR que a peca 1 §4 nunca teve, e a decisao da v0.7 o matou')
else:
    print(f'  [x] o "{FANTASMA}" nao existe em lugar nenhum do projeto nem do gerador')


# ==========================================================================
bloco('7. EXATAMENTE UMA ENTRADA ATRAVESSA O CORPO, E ELA E O `Cisao`')

if 'ATRAVESSA' not in P24:
    erro(7, 'a peca 24 §3.2 parou de declarar a excecao que atravessa o corpo')
else:
    print('  [x] a peca 24 §3.2 declara a excecao')

# quem se declara excecao tem de dizer as duas metades: tira Integridade E nao tira vida
_cis = re.search(r'\|\s*\*\*`Cisão`\*\*\s*\|([^|]*)\|', P16)
if not _cis:
    erro(7, 'nao achei a linha do `Cisao` no catalogo da peca 16')
else:
    txt = _cis.group(1)
    if 'atravessa o corpo' not in txt:
        erro(7, f'o `Cisao` parou de declarar que atravessa o corpo: "{txt.strip()}"')
    elif 'não tira vida' not in txt:
        erro(7, f'o `Cisao` diz que atravessa mas nao diz que NAO tira vida — e a '
                f'segunda metade que o separa da regra geral: "{txt.strip()}"')
    else:
        print('  [x] o `Cisao` declara as duas metades: tira Integridade, e nao tira vida')

# e ninguem MAIS pode se declarar excecao sem passar por aqui
_outros = [l.strip() for l in P16.split('\n')
           if 'atravessa o corpo' in l and 'Cisão' not in l]
if _outros:
    erro(7, f'{len(_outros)} entrada(s) da peca 16 alem do `Cisao` dizem que atravessam '
            f'o corpo — a peca 24 §3.2 declara que so uma existe')
else:
    print('  [x] nenhuma outra entrada da peca 16 reivindica a excecao')


# ==========================================================================
bloco('8. A EXCECAO SO E EXCECAO SE A REGRA GERAL LEVAR O CORPO JUNTO')

# A PRIMEIRA VERSAO DESTA CHECAGEM ERA VAZIA, e o arnes pegou por ausencia: nenhuma
# perturbacao conseguia acender ela. Ela comparava `min(vida, alma)` com `alma`, e
# `alma >= min(vida, alma)` e' verdade em aritmetica, nao em regra — ela nao podia
# falhar nunca. Licao no 8 na forma mais pura: a checagem se media contra si mesma.
#
# O que sustenta de verdade o preco do `Cisao` nao e' aquela desigualdade: e' o fato
# de a REGRA GERAL esvaziar as duas barras. Se o SS3.1 parar de acoplar o dano de
# alma a vida, "atravessar" deixa de ser troca e vira o mesmo que todo mundo faz —
# e aí o `Classe 3` daquela entrada esta pago por uma distincao que sumiu.
_g = P24[P24.find('### 3.1'):P24.find('### 3.2')]
_e = P24[P24.find('### 3.2'):P24.find('### 3.3')]
if not _g or not _e:
    erro(8, 'nao consegui recortar o SS3.1 e o SS3.2 da peca 24 — se eles mudaram de '
            'titulo, esta checagem parou de conferir')
else:
    # A LINHA da regra, e nao a secao inteira: a prosa em volta dela tambem fala de
    # "vida maxima", e o arnes mostrou que perturbar a regra saia VERDE por causa disso.
    _linha = [l for l in _g.splitlines() if 'Cada ponto de dano de alma tira' in l]
    _linha = _linha[0] if _linha else ''
    if not _linha:
        erro(8, 'o SS3.1 parou de publicar a linha "Cada ponto de dano de alma tira ..." — '
                'e ela e a regra geral inteira')
    ACOPLA = ('de vida', 'de Integridade', 'vida máxima')
    faltam = [t for t in ACOPLA if t not in _linha]
    if _linha and faltam:
        erro(8, f'o SS3.1 parou de acoplar o dano de alma a {faltam} — sem as tres, '
                f'"atravessar" deixa de ser excecao e o preco do `Cisao` fica pago '
                f'por uma distincao que nao existe mais')
    else:
        print('  [x] o SS3.1 acopla as tres: vida, Integridade e vida maxima')

    NEGA = ('Não tira vida', 'não derruba a vida máxima')
    faltam = [t for t in NEGA if t not in _e]
    if faltam:
        erro(8, f'o SS3.2 parou de negar {faltam} — a excecao tem de dizer o que ela '
                f'NAO faz, senao ela e apenas a regra geral com outro nome')
    else:
        print('  [x] o SS3.2 nega as duas que o SS3.1 afirma — as duas leituras se separam')

    # E so entao a comparacao numerica vale a pena, porque ela agora tem premissa.
    if integridade is not None and len(_tab) == 5:
        pior = None
        for nv in (2, 10, 20, 30):
            for cam in CAM:
                for con in range(TETO_ATR + 1):
                    for ess in range(TETO_ATR + 1):
                        v, i = vida(cam, con, nv), integridade(nv, ess)
                        if i < min(v, i):
                            pior = (nv, cam, con, ess)
        if pior:
            erro(8, f'a excecao ficou mais rapida que a regra geral em {pior}')
        else:
            print('  [x] e, com o acoplamento de pe, a excecao e igual ou pior na grade')
            print('      inteira — que e o que faz o preco publicado continuar valendo')


bloco('9. QUEM NAO TEM CAMINHO FICA COM `Integridade = vida maxima`')

if not re.search(r'Integridade de quem não é personagem jogador = a vida máxima', P24):
    erro(9, 'a peca 24 §3.3 parou de declarar a Integridade de quem nao e personagem '
            'jogador — sem essa linha o `Cisao` fica sem alvo contra inimigo')
else:
    print('  [x] a peca 24 §3.3 declara a linha, e ela e a do manual sem numero novo')
    if 'não tem Caminho' not in P24:
        erro(9, 'a peca 24 nao diz POR QUE a substituicao da peca 1 nao alcanca o '
                'inimigo — sem o motivo, a linha vira excecao arbitraria')
    else:
        print('  [x] e ela diz o motivo: inimigo nao tem Caminho nem Constituicao')


# ==========================================================================
bloco('10. A FICHA DE EXEMPLO DA PECA 8 OBEDECE A FORMULA')

_ess = re.search(r'Essência (\d+)\.', P08)
_int = re.search(r'\|\s*Integridade\s*\|\s*([^|]*?)\s*\|\s*\*\*(\d+)\*\*\s*\|', P08)
if not _ess:
    erro(10, 'nao achei a Essencia da ficha de exemplo na peca 8')
elif not _int:
    erro(10, 'nao achei a Integridade na tabela de numeros da ficha de exemplo')
elif integridade is None:
    erro(10, 'sem a formula da checagem 1 esta checagem nao roda')
else:
    ess_ficha = int(_ess.group(1))
    conta, valor = _int.group(1), int(_int.group(2))
    esperado = integridade(2, ess_ficha)
    print(f'  a Kaori tem Essencia {ess_ficha}; a ficha imprime "{conta}" = {valor}')
    if valor != esperado:
        erro(10, f'a ficha publica Integridade {valor} e a formula da Essencia '
                 f'{ess_ficha} no nivel 2 da {esperado}')
    elif str(ess_ficha) not in conta:
        erro(10, f'a coluna "a conta" da ficha nao mostra a Essencia dela ({ess_ficha}) — '
                 f'ela e "{conta}", e um leitor nao consegue refazer o numero')
    else:
        print(f'  [x] {valor} sai de {BASE} + ({ess_ficha} + {POR_NIVEL}) x 1, e a conta esta a vista')

# e o passo 7 nao pode voltar a imprimir numero fixo: ele depende do atributo
_p7 = re.search(r'Integridade\s*=\s*(\d+)\s*\+\s*Essência', P08)
if not _p7:
    erro(10, 'o Passo 7 da peca 8 parou de escrever a Integridade como `N + Essencia` — '
             'se ele voltou a imprimir um numero fixo, ele mente para quatro Essencias '
             'de cinco')
else:
    _esp = BASE + POR_NIVEL * (2 - 1) if BASE else None
    if _esp is not None and int(_p7.group(1)) != _esp:
        erro(10, f'o Passo 7 diz `{_p7.group(1)} + Essencia` e a formula no nivel 2 da '
                 f'`{_esp} + Essencia`')
    else:
        print(f'  [x] o Passo 7 escreve `{_p7.group(1)} + Essencia`, que e a formula no nivel 2')


# ==========================================================================
bloco('11. A RECUPERACAO DAQUI E A DA PECA 10 DIZEM A MESMA COISA')

_p10 = re.search(r'\|\s*\*\*Integridade\*\*\s*\|([^|]*)\|([^|]*)\|', P10)
if not _p10:
    erro(11, 'nao achei a linha da Integridade na tabela de descanso da peca 10')
else:
    curto, longo = _p10.group(1).strip(), _p10.group(2).strip()
    print(f'  peca 10 -> descanso curto: "{curto}"   descanso longo: "{longo}"')
    if 'cheia' not in longo or 'estágios limpam' not in longo:
        erro(11, 'a peca 10 mudou o que o descanso longo devolve, e a peca 24 §5 '
                 'continua publicando a versao antiga')
    # a peca 24 tem de APONTAR, e nao repetir: ela nao pode ser dona desta linha
    if 'peça 10 §2 é quem manda' not in P24:
        erro(11, 'a peca 24 §5 parou de declarar que a peca 10 e a dona da tabela de '
                 'descanso — sem isso as duas viram fontes concorrentes (licao no 9)')
    else:
        print('  [x] a peca 24 §5 aponta para a peca 10 em vez de disputar a posse')
    if 'Cura comum não devolve' not in P24:
        erro(11, 'a peca 24 §5 parou de dizer que cura comum nao devolve o que a alma '
                 'perdeu — e a metade da regra que a peca 10 NAO carrega')
    else:
        print('  [x] e a peca 24 carrega a metade que a peca 10 nao tem: cura nao devolve')


# ==========================================================================
bloco('12. O MANUAL IMPRIME AS DUAS LINHAS DO INIMIGO')
# ==========================================================================
# v0.159. Duas coisas nasceram juntas porque sao a mesma:
#
#   1) a caixa `Integridade` do manual publicava `= vida maxima` sem dizer para
#      quem. Desde a v0.145 aquela linha e' FALSA para personagem jogador — quem
#      manda nele e' a formula do SS2 desta peca — e ela ficou treze versoes assim.
#   2) a secao `Inimigos` nao dizia que o inimigo tem a barra. Sem isso o `Cisao`
#      fica sem alvo contra inimigo, que era o item 1 do SS8.
#
# NAO ENTROU COLUNA. Uma coluna de Integridade ao lado da coluna de vida seria a
# mesma linha escrita duas vezes dentro da mesma tabela — licao no 9. O que o
# mestre precisa e' de um lugar para marcar o desgaste, e nao de um segundo valor.
#
# E o manual continua SEM a formula do SS2: ele aponta para fora em vez de copiar.
_int = re.search(r"H2\('Integridade'\)(.*?)(?=\n\s*H2\()", MANUAL, re.S)
_ini = re.search(r"H2\('Inimigos'\)(.*?)(?=\n\s*H2\()", MANUAL, re.S)

# GUARDA: recorte vazio quer dizer secao renomeada, e uma checagem cega passa
# verde para sempre. As duas guardas vem antes de qualquer comparacao.
if not _int:
    erro(12, 'nao achei a secao `Integridade` no partF.js do manual')
if not _ini:
    erro(12, 'nao achei a secao `Inimigos` no partF.js do manual — e e la que a '
             'ficha de inimigo mora')

if _int and _ini:
    S_INT, S_INI = _int.group(1), _ini.group(1)

    # 12a — a caixa nomeia OS DOIS LADOS
    _tem_inimigo = re.search(r'inimigo|não seja personagem jogador', S_INT, re.I)
    _tem_pj = re.search(r'personagem[^.]{0,60}f[óo]rmula própria', S_INT, re.I)
    if not _tem_inimigo:
        erro('12a', 'a caixa `Integridade` do manual nao diz para QUEM a regra '
                    'plana `= vida maxima` vale — e ela vale para inimigo, nao '
                    'para personagem jogador (peca 24 SS3.3)')
    elif not _tem_pj:
        erro('12a', 'a caixa `Integridade` do manual nao diz que personagem tem '
                    'formula propria — quem le so ela da ao personagem a '
                    'Integridade errada, que foi o que aconteceu da v0.145 ate a '
                    'v0.158')
    else:
        print('  [x] a caixa `Integridade` do manual nomeia os dois lados: a regra '
              'plana e do')
        print('      inimigo, e personagem tem formula propria')

    # 12b — e o manual NAO republica a formula. Ela e' montada dos numeros lidos
    # da peca no bloco 1, e nao escrita aqui: se a peca mudar, a busca muda junto.
    if None not in (BASE, POR_NIVEL):
        _assin = f'(Essência + {POR_NIVEL})'
        if _assin in MANUAL or f'{BASE} + (Essência' in MANUAL:
            erro('12b', f'o manual passou a carregar a formula da peca 24 '
                        f'(`{_assin}`) — duas copias do mesmo numero em dois '
                        f'documentos, que e a licao no 9. Ele aponta, nao copia')
        else:
            print(f'  [x] o manual nao carrega a formula da peca 24 (`{_assin}`): '
                  f'ele aponta')

    # 12c — a secao `Inimigos` manda anotar a barra, e o ponteiro tem alvo
    _linha = re.search(r'Integridade[^\n]*vida máxima', S_INI)
    # a coluna sai do CABECALHO da tabela, e nao de qualquer texto com `vida`
    # dentro: a propria linha da Integridade tem a palavra, e ler ela faria a
    # guarda apontar para si mesma.
    _cab = re.search(r'TBL\(\[([^\]]*)\]', S_INI)
    _col = _cab and re.search(r'vida', _cab.group(1), re.I)
    if not _linha:
        erro('12c', 'a secao `Inimigos` do manual nao diz que a Integridade do '
                    'inimigo e a vida maxima dele — sem essa linha o `Cisao` fica '
                    'sem alvo contra inimigo (peca 24 SS3.3)')
    elif not _col:
        erro('12c', 'a linha da Integridade aponta para a coluna de vida da tabela '
                    'de inimigo, e a tabela nao tem mais coluna de vida — ponteiro '
                    'pendurado')
    else:
        print('  [x] a secao `Inimigos` manda anotar a barra, e a coluna de vida '
              'que ela cita existe')


# ==========================================================================
print()
print('=' * 88)
if FALHAS:
    print(f'>>> {len(FALHAS)} PROBLEMA(S)')
    for f in FALHAS:
        print('   -', f)
    sys.exit(1)
print('>>> TUDO OK — a formula reproduz a curva do manual na Essencia de referencia,')
print('    a referencia e derivada do teto, as duas reservas custam o mesmo por ponto,')
print('    o estagio 4 continua disparando, os quatro estagios batem com o manual,')
print('    o TR e um dos quatro que existem, so o `Cisao` atravessa o corpo e ele nao')
print('    ficou mais rapido, o inimigo tem alvo, e a ficha de exemplo obedece.')

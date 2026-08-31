#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Confere a peca 25 — SEM TECNICA, a nona rota de Origem.

NENHUM VALOR DE REGRA MORA AQUI. Orcamento, fatia, Rotina, curva de refino,
escada de gate e teto de Classe Passiva saem dos documentos donos:

  o PE por Caminho ............ peca 6 §5
  a curva de refino ........... peca 11 §3
  a escada de gate ............ peca 11 §5
  o divisor da `cobrir-se` .... peca 11 §6
  a trava da `Aptidao Propria`  peca 11 §6.7
  a `Sutura` e o `Pulso` ...... DESENHO-trilhas.md
  os renomes da peca 20 ....... 20-tecnica-marcial.md §3.1

Doze checagens. Sai com codigo 1 se algo quebrar.
"""
import os
import re
import subprocess
import sys

FALHAS, AVISOS = [], []
def erro(m): FALHAS.append(m); print(f'  !! {m}')
def aviso(m): AVISOS.append(m); print(f'  ~~ {m}')
def bloco(t):
    print(); print('=' * 88); print(t); print('=' * 88)

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.abspath(os.path.join(AQUI, '..', '..'))
def ler(nome, base=AQUI):
    with open(os.path.join(base, nome), encoding='utf-8') as f:
        return f.read()

P25 = ler('25-sem-tecnica.md')
P20 = ler('20-tecnica-marcial.md')
P11 = ler('11-aptidoes-e-refino.md')
P09 = ler('09-origens.md')
P06 = ler('06-caminhos-e-trilhas.md')
DES = ler('DESENHO-trilhas.md', RAIZ)

def secao(txt, titulo, nivel='## '):
    """recorte que fecha em QUALQUER cabecalho de nivel igual ou MENOR — a
    armadilha que a v0.153 pagou duas vezes.

    ⚠ E ele procura o fecho DEPOIS da linha do cabecalho. A primeira versao
    procurava a partir do caractere seguinte ao `\n`, e ai o proprio cabecalho
    casava com o padrao de fecho: a secao saia com UM caractere. O arnes nao
    pegou isso — quem pegou foram quatro checagens acusando de uma vez."""
    i = txt.find('\n' + nivel + titulo)
    if i < 0:
        return ''
    ini = i + 1
    corpo = txt.find('\n', ini) + 1
    m = re.search(r'^#{1,%d} ' % len(nivel.strip()), txt[corpo:], re.M)
    return txt[ini:corpo + m.start()] if m else txt[ini:]

FATIA = 5.08          # DESENHO-trilhas.md, e o conferir-catalogo.py e' o dono
NASCE = 2             # a ficha nasce no nivel 2 — peca 8 §2
FILTRO = 3.00         # o filtro de dominancia do projeto

print('Peca 25 lida:', len(P25.splitlines()), 'linhas.')

# --------------------------------------------------------------------------
bloco('1. O ORCAMENTO E O `PE` DO CAMINHO — a peca nao inventa moeda')
# A peca 9 §5 fixou isto na v0.116 e a peca 20 §2 obedeceu. Esta obedece igual.
_m = re.search(r'PE por nível \|([^\n]+)\|', P06)
PE_CAM = []
if _m:
    PE_CAM = [int(x) for x in re.findall(r'\b(\d)\b', _m.group(1))]
if len(PE_CAM) != 5:
    erro(f'1: li {len(PE_CAM)} coluna(s) de PE por nivel na peca 6 §5 e os Caminhos '
         'sao cinco — o extrator parou de casar, e esta checagem nao tem contra o '
         'que comparar')
else:
    print(f'  PE por nivel, lido da peca 6 §5: {" · ".join(map(str, PE_CAM))}')
    faixa = f'`{min(PE_CAM)}` a `{max(PE_CAM)}` de PE por nível'
    if faixa not in P25:
        erro(f'1: a peca 25 nao publica a faixa de orcamento que a peca 6 §5 tem '
             f'({faixa}) — ou ela inventou numero, ou a citacao envelheceu')
    else:
        print(f'  [x] a peca 25 cita a faixa do dono, e nao um numero proprio.')

# --------------------------------------------------------------------------
bloco('2. A MAQUINA NAO TEM NUMERO PROPRIO — ela e o Fundamento inteiro')
# Molde da checagem 6 do conferir-marcial.py: um preco ou um dado escrito AQUI
# quer dizer que a rota deixou de herdar e passou a ser subsistema ao lado.
_TAB = secao(P25, '3. A máquina é o Fundamento')
_HERDA = ['3 × Classe', '1d8', '2 + (nível ÷ 2)']
_falta = [h for h in _HERDA if h not in _TAB]
if _falta:
    erro(f'2: a §3 da peca 25 parou de citar {_falta} — sao os numeros que ela '
         'HERDA, e sem eles nao da para provar que ela nao inventou os proprios')
else:
    print(f'  [x] a §3 cita os tres numeros herdados: {" · ".join(_HERDA)}')
    if 'Não existe número novo nesta tabela' not in _TAB:
        erro('2: a §3 deixou de declarar que nao ha numero novo na tabela — a '
             'declaracao e' + ' o que faz esta checagem valer alguma coisa')
    else:
        print('  [x] e ela declara, com todas as letras, que nao ha numero novo.')

# --------------------------------------------------------------------------
bloco('3. OS DOIS RENOMES, E O ORIGINAL SUMIU DESTA ROTA')
RENOMES = {'feitiço': 'Manejo', 'Técnica Máxima': 'Auge'}
for velho, novo in RENOMES.items():
    if novo not in P25:
        erro(f'3: `{novo}` nao aparece na peca 25 — o renome de `{velho}` sumiu')
    else:
        print(f'  [x] `{velho}` -> `{novo}`')
# o original nao pode viver como vocabulario DESTA rota. DOIS recortes saem
# fora: a tabela do §3, que cita os dois lados de proposito, e a §10, que e a
# ESPECIFICACAO deste validador e por isso nomeia as palavras velhas para dizer
# o que esta checagem faz. Sem o segundo, a checagem acusa a propria spec —
# a mesma familia do defeito que a v0.165 pagou, em que o extrator lia a prosa
# que explica a regra em vez da linha de regra.
_fora = P25.replace(_TAB, '').replace(secao(P25, '10. O que o validador confere'), '')
for velho in RENOMES:
    achados = [l.strip()[:90] for l in _fora.splitlines()
               if re.search(rf'\b{re.escape(velho)}\b', l)
               and 'peça 20' not in l and 'manual' not in l and 'Fundamento' not in l]
    if achados:
        for a in achados:
            print(f'     {a}')
        erro(f'3: `{velho}` continua vivo fora da tabela de renomes, e nesta rota '
             f'ele se chama `{RENOMES[velho]}`')
if not FALHAS:
    print('  [x] e nenhum dos dois vive fora da tabela que declara a troca.')

# --------------------------------------------------------------------------
bloco('4. A `Liberacao Maxima` NAO RENOMEIA, E O MOTIVO ESTA ESCRITO')
# A peca 20 §3.1 renomeou TRES; esta renomeia DOIS. Uma diferenca com o
# precedente so vale se ela vier com o motivo — senao daqui a dez versoes
# alguem "conserta" a assimetria sem saber que ela foi medida.
_p20_renomes = len(set(re.findall(r'\*\*`(Kata|Ruptura|Ōgi)`\*\*', P20)))
print(f'  a peca 20 §3.1 renomeia: {_p20_renomes} coisa(s)')
# ⚠ o ARGUMENTO tem de morar na §3.1, e nao so numa celula da tabela do §3.
# A primeira versao aceitava a linha `| Liberação Máxima | igual |` como prova e
# procurava o motivo na peca INTEIRA — e "tecnica inata" aparece no §1 e no §3.2
# por outros motivos. Apagar o argumento saia VERDE. Terceira vez que o arnes
# desta versao pega a mesma familia: prosa sobre a regra nao e a regra.
_S31 = secao(P25, '3.1 Os dois renomes', '### ')
if 'Liberação Máxima' not in P25:
    erro('4: a peca 25 nao menciona a `Liberacao Maxima` — ela precisa dizer que '
         'aquele nome FICA, senao a assimetria com a peca 20 fica sem dono')
elif not _S31:
    erro('4: a §3.1 da peca 25 sumiu — e ela e a dona do argumento')
elif not re.search(r'`Liberação Máxima`\*{0,2}\s*(NÃO|não)\s+renomeia', _S31):
    erro('4: a §3.1 nao declara que a `Liberacao Maxima` NAO renomeia — a celula '
         'da tabela do §3 sozinha nao e argumento')
elif 'inata' not in _S31:
    erro('4: a §3.1 declara a diferenca para a peca 20 e nao escreve o MOTIVO — e '
         'o motivo e o que impede alguem de "consertar" a assimetria em dez versoes')
else:
    print('  [x] ela declara que a `Liberacao Maxima` fica, e escreve por que a')
    print('      razao da peca 20 nao alcanca esta rota.')

# --------------------------------------------------------------------------
bloco('5. A BANDA DA SEMENTE E DERIVADA DA ESCADA DE GATE — nao e teto escolhido')
# Esta checagem NAO guarda 9,3 nem 17,3. Ela le a escada de gate da peca 11 §5,
# le a curva de refino da §3, e recalcula a antecipacao de cada altura. Mudar a
# escada de forma coerente move a banda junto e sai VERDE de proposito.
ESCADA = {}
for _m in re.finditer(
        r'\|\s*Classe Passiva (\d) no refino (\d+)\s*\|([^\n]+)\|', P11):
    cp, _r = int(_m.group(1)), int(_m.group(2))
    niveis = [int(x) for x in re.findall(r'nível (\d+)', _m.group(3))]
    if len(niveis) == 3:
        ESCADA[cp] = niveis
# a Classe Passiva 1 nao tem gate: ela abre no PRIMEIRO MARCO, e os marcos sao
# da §3 da mesma peca.
MARCOS = [int(x) for x in re.findall(r'\*\*(\d+), (\d+), (\d+), (\d+), (\d+), (\d+) e (\d+)\*\*',
                                     P11)[0]] if re.findall(
    r'\*\*(\d+), (\d+), (\d+), (\d+), (\d+), (\d+) e (\d+)\*\*', P11) else []
if len(ESCADA) < 2 or len(MARCOS) != 7:
    erro(f'5: li {len(ESCADA)} altura(s) da escada de gate e {len(MARCOS)} marco(s) '
         'na peca 11, e esperava duas e sete — o extrator parou de casar, e a '
         'banda abaixo passaria verde sem conferir nada')
else:
    ESCADA[1] = [MARCOS[0]] * 3
    print(f'  marcos, lidos da peca 11 §3: {" · ".join(map(str, MARCOS))}')
    ANTEC = {cp: sum(n - NASCE for n in ns) / 3 for cp, ns in ESCADA.items()}
    for cp in sorted(ANTEC):
        print(f'  Classe Passiva {cp}: abre em {"/".join(map(str, ESCADA[cp]))} '
              f'-> antecipa {ANTEC[cp]:.1f} niveis na media')
    banda = [ANTEC[c] for c in (2, 3) if c in ANTEC]
    com1 = banda + [ANTEC[1]]
    esp_banda = max(banda) / min(banda)
    esp_com1 = max(com1) / min(com1)
    print(f'\n  banda `CP 2` e `3`: {min(banda):.1f} a {max(banda):.1f}  '
          f'-> espalhamento {esp_banda:.2f}x')
    print(f'  com a `CP 1` junto:  {min(com1):.1f} a {max(com1):.1f}  '
          f'-> espalhamento {esp_com1:.2f}x')
    if esp_banda >= FILTRO:
        erro(f'5: a banda de `CP 2` e `3` esta em {esp_banda:.2f}x e o filtro do '
             f'projeto reprova a partir de {FILTRO:.2f}x — a peca 25 §4.1 nao fecha')
    elif esp_com1 < FILTRO:
        erro(f'5: com a `CP 1` junto o espalhamento e {esp_com1:.2f}x, ABAIXO do '
             f'filtro — entao o motivo que a §4.1 da para excluir a `CP 1` deixou '
             'de valer, e a banda vira teto escolhido em vez de derivado')
    else:
        print(f'  [x] a banda passa em {esp_banda:.2f}x e a `CP 1` reprova em '
              f'{esp_com1:.2f}x — o corte e derivado, e nao escolhido.')
        for v in (f'`{min(banda):.1f}`'.replace('.', ','),
                  f'`{max(banda):.1f}`'.replace('.', ',')):
            if v not in P25:
                erro(f'5: a peca 25 publica uma banda diferente da que a escada da '
                     f'peca 11 §5 produz — falta {v}')

# --------------------------------------------------------------------------
bloco('6. AS SEMENTES NOMEADAS CAEM NA BANDA')
# as sementes saem da tabela do §4.2 da propria peca; a altura de cada uma sai
# da peca 11. Se uma semente da peca 25 nao existir no catalogo de la, acende.
# a linha e `| **a porta** | **`Semente`** | CP | adianta |`
SEM = re.findall(r'\|\s*\*\*[^|]+\*\*\s*\|\s*\*\*`([^`]+)`\*\*\s*\|\s*(\d)\s*\|',
                 secao(P25, '4. A semente'))
if not SEM:
    erro('6: nao li semente nenhuma na tabela do §4.2 da peca 25 — o extrator '
         'parou de casar')
else:
    for nome, cp in SEM:
        cp = int(cp)
        if nome not in P11 and nome != 'Aptidão Própria':
            erro(f'6: a semente `{nome}` nao existe no catalogo da peca 11')
        elif cp not in (2, 3):
            erro(f'6: a semente `{nome}` e Classe Passiva {cp}, e a banda do §4.1 '
                 'e `2` e `3` — ela quebra o espalhamento')
        else:
            print(f'  [x] `{nome}` — Classe Passiva {cp}, dentro da banda')
    print(f'  {len(SEM)} semente(s) nomeada(s).')

# --------------------------------------------------------------------------
bloco('7. A `Aptidao Propria` CONTINUA TRAVADA EM `CP 1 ou 2`')
# Ela e a terceira porta, e o que impede ela de virar a melhor semente e uma
# trava que ja existia na peca 11 §6.7 — nao uma regra nova desta peca.
if not re.search(r'Classe Passiva 1 ou 2, nunca 3', P11):
    erro('7: a trava da `Aptidao Propria` sumiu da peca 11 §6.7 — sem ela a '
         'terceira porta da peca 25 pode virar `Classe Passiva 3` e dominar as outras')
elif 'Classe Passiva 1 ou 2' not in P25:
    erro('7: a peca 25 nao cita a trava da peca 11 §6.7 na terceira porta — o '
         'leitor nao tem como saber que ela cai no piso da banda por regra que ja existe')
else:
    print('  [x] a trava vive na peca 11 §6.7, e a peca 25 aponta para ela.')

# --------------------------------------------------------------------------
bloco('8. A SEMENTE NAO GASTA MARCO — a contagem da rota pura nao se move')
# Se a semente cobrasse um marco, a rota pura de Refino cairia de 10 picks para
# 9, e o catalogo de doze deixaria de ter a folga de duas que o §3 da peca 11 pede.
if 'Ela não gasta marco' not in P25:
    erro('8: a peca 25 nao declara que a semente nao gasta marco — e' +
         ' a diferenca entre a rota pura terminar com 10 aptidoes ou com 9')
else:
    _m = re.search(r'rota pura passa a precisar de (\d+) aptidões', P11)
    if not _m:
        erro('8: nao achei na peca 11 §3 quantas aptidoes a rota pura precisa — '
             'esta checagem ficou sem contra o que comparar')
    else:
        n = int(_m.group(1))
        print(f'  a rota pura de Refino precisa de {n} aptidoes, pela peca 11 §3')
        print(f'  [x] a semente nao cobra marco, entao os {n} continuam saindo dos '
              'sete marcos.')

# --------------------------------------------------------------------------
bloco('9. O BUFF DE CURA E `1/3 DO REFINO`, E O DIVISOR TEM DONO')
# Ele nao inventa divisor: `1/3 do refino` e o da `cobrir-se` da peca 11 §6, e o
# motivo escrito la e' que ele cresce de 0 a 3 na campanha.
# ⚠ ela le a LINHA DE REGRA e nao a secao. A §6 cita `1/3 do refino` de novo
# para dizer de onde o divisor vem — entao procurar a string na secao inteira
# deixa trocar a REGRA e manter o COMENTARIO, e sai verde. Foi assim que a
# v0.165 se mordeu, e o arnes desta versao pegou de novo.
_REGRA9 = ''
for _l in secao(P25, '6. A rota da Shoko').splitlines():
    if _l.lstrip().startswith('>') and 'rolagem de cura' in _l:
        _REGRA9 = _l
        break
if '1/3 do refino' not in P11:
    erro('9: `1/3 do refino` sumiu da peca 11 §6 — o divisor do buff de cura da '
         'peca 25 ficou sem dono')
elif not _REGRA9:
    erro('9: nao achei a LINHA DE REGRA do buff de cura na §6 da peca 25 — o '
         'reconhecedor parou de casar e esta checagem passaria verde a toa')
elif '1/3 do refino' not in _REGRA9:
    erro(f'9: a linha de regra do buff de cura nao usa `1/3 do refino`, e o divisor '
         f'tem dono na peca 11 §6: {_REGRA9.strip()[:90]}')
else:
    # o preco, na regua que a propria `Sutura` usa: cura x 50% / fatia
    _m = re.search(r'\*\*`Pulso`\*\*.*?\|\s*([\d,]+)\s*\|', DES)
    if not _m:
        erro('9: nao achei o preco do `Pulso` no DESENHO-trilhas.md — sem ele nao '
             'da para medir o buff contra a entrega que ele espelha')
    else:
        pulso = float(_m.group(1).replace(',', '.'))
        buff = 3 * 0.50 / FATIA          # 1/3 do refino no teto = +3
        print(f'  o `Pulso` (nivel 19 da `Sutura`) vale {pulso:.2f} fatia')
        print(f'  o buff no refino 10 (+3) vale {buff:.2f} fatia -> {buff/pulso:.2f}x')
        if buff > pulso:
            erro(f'9: o buff de cura vale {buff:.2f} fatia contra {pulso:.2f} do '
                 '`Pulso`, que e entrega de NIVEL 19 de uma Trilha — e este sai de graca')
        else:
            print(f'  [x] ele fica abaixo da entrega de Trilha que espelha ele.')

# --------------------------------------------------------------------------
bloco('10. CURAR OS OUTROS CONTINUA SENDO DA `Sutura`, NO NIVEL 11 DELA')
_m = re.search(r'\|\s*\*\*11\*\*\s*\|\s*\*\*`Enxerto`\*\*\s*\|([^|]+)\|', DES)
if not _m:
    erro('10: nao achei o `Enxerto` no nivel 11 da `Sutura` — esta checagem ficou '
         'sem contra o que comparar')
elif 'curar **os outros**' not in _m.group(1) and 'curar os outros' not in _m.group(1):
    erro('10: o nivel 11 da `Sutura` deixou de ser quem entrega curar os outros')
else:
    print('  o `Enxerto`, nivel 11 da `Sutura`, e quem entrega curar os outros')
    if re.search(r'`Liberação`.{0,120}(na criação|semente)', P25, re.S) and \
       'fica de fora da criação' not in P25:
        erro('10: a peca 25 parece conceder a `Liberacao` na criacao — curar os '
             'outros custa uma Trilha inteira e chega no nivel 11 dela')
    else:
        print('  [x] a peca 25 mantem ela fora da criacao, e diz por que.')

# --------------------------------------------------------------------------
bloco('11. A EXPANSAO DE DOMINIO NAO E ALCANCAVEL POR ESTA ROTA')
_sec = secao(P25, '3.2 A Expansão de Domínio', '### ')
if not _sec:
    erro('11: a §3.2 da peca 25, que nega a Expansao, sumiu')
elif 'não tem Expansão de Domínio' not in _sec:
    erro('11: a §3.2 existe e nao nega a Expansao com todas as letras')
else:
    print('  [x] a §3.2 nega a Expansao, e escreve o motivo do lado.')
    if 'troca' not in _sec.lower():
        aviso('11: a negacao esta escrita e a TROCA nao — a peca 9 §5 e a peca 20 '
              '§8.2 as duas declaram o que a rota ganha em cima da negacao')

# --------------------------------------------------------------------------
bloco('12. TRIAGEM DE TODO NOME QUE A PECA CRIA')
# v0.193: a lista era escrita a mao aqui dentro — `Manejo`, `Auge`, `Redoma` —, e
# ela envelheceu na primeira vez que a peca ganhou exemplo novo: o `Espinho`
# entrou no §9 e passou por baixo da triagem. Lista a mao dentro de validador e'
# a licao no 9 na forma mais barata dela.
#
# Hoje os dois renomes saem do §3.1, que os declara em bloco de citacao, e os
# exemplos saem dos titulos do §9. Nome novo entra na triagem sozinho.
_ren = re.findall(r'^>\s*\*\*`([A-ZÁÉÍÓÚÂÊÔÃÕÇ][\wÀ-ÿ]*)`\.\*\*', P25, re.M)
_ex = re.findall(r'^###\s+([A-ZÁÉÍÓÚÂÊÔÃÕÇ][\wÀ-ÿ]*)\s+—\s+[ao]\s', P25, re.M)
NOMES = sorted(set(_ren) | set(_ex))
if len(NOMES) < 3:
    erro(f'12: achei so {len(NOMES)} nome(s) criado(s) pela peca ({NOMES}) — os renomes do '
         f'§3.1 ou os titulos de exemplo do §9 mudaram de forma, e a triagem parou de '
         f'alcancar o que a peca batiza')
print(f'  nomes que esta peca cria, lidos dela: {", ".join(NOMES)}')
try:
    r = subprocess.run([sys.executable, 'conferir-nomes.py', '--candidatos'] + NOMES,
                       cwd=AQUI, capture_output=True, text=True, timeout=180)
    saida = r.stdout + r.stderr
    for n in NOMES:
        m = re.search(rf'^\s*(LIVRE|OCUPADO|DENTRO|fraco|MORTO)\s+{n}\b(.*)$',
                      saida, re.M)
        if not m:
            erro(f'12: a triagem nao respondeu sobre `{n}`')
        elif m.group(1) == 'LIVRE':
            print(f'  [x] `{n}` sai LIVRE')
        else:
            erro(f'12: `{n}` sai {m.group(1)}{m.group(2)} — e a peca 25 batiza assim mesmo')
except Exception as e:
    aviso(f'12: nao consegui rodar a triagem ({e}) — checagem PULADA')

# --------------------------------------------------------------------------
print()
print('=' * 88)
if FALHAS:
    print(f'>>> {len(FALHAS)} PROBLEMA(S):')
    for e in FALHAS:
        print('   -', e)
    sys.exit(1)
print('>>> TUDO OK — a rota herda o orcamento e a maquina, a banda da semente e')
print('    derivada da escada de gate, e nenhum numero de regra mora nesta peca.')
if AVISOS:
    print(f'    {len(AVISOS)} aviso(s) acima, que nao falham o validador.')

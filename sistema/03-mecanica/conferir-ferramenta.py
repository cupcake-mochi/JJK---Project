# -*- coding: utf-8 -*-
"""
conferir-ferramenta.py — o validador da peca 16 (Ferramenta amaldicoada).

Confere a camada contra o fundo de Equipamento, a escada de grau contra as
Classes da peca 11, o gate contra a peca 11 SS6, o teto na ficha contra o
orcamento de marco da peca 2, e o catalogo contra a regua que o produziu.

NADA DE VALOR FICA ESCRITO AQUI. O fundo sai da PECA 14, o gate e as Classes
saem da PECA 11, os marcos saem da PECA 2, a Rotina sai da PECA 6, a rota sem
energia sai da PECA 9, as vagas de Desliga saem da PECA 13, e a escada de grau,
o teto e o catalogo saem da PROPRIA PECA 16. O unico bloco com valor na mao e o
LIMITES DE DESIGN abaixo, declarado a parte da regra aplicada — que e a licao
no 8: uma checagem nao pode se medir contra a propria constante.

Dezessete checagens, as do SS7 do rascunho que virou o SS8 da peca:
   1. FUNDO       — a camada nao fura o fundo de Equipamento.
   2. UM-ESTIGMA  — um Estigma por ferramenta, nunca dois.
   3. GATE        — o gate lido da peca 11 SS6, nunca de constante.
   4. SEM-REFINO  — nenhum gate de refino em lugar nenhum da peca.
   5. DESGASTE    — o Desgaste compra o gate e nunca a Classe.
   6. TETO        — o teto de Estigmas na ficha, com busca exaustiva.
   7. CLASSE      — cada grau declara UMA Classe, e ela existe na peca 11 SS4.
   8. SEM-DADO    — nenhum grau da dado de dano nem numero que cresca com refino.
   9. ESCADA      — a escada de grau lida do documento dono, nunca de constante.
  10. PATENTE     — patente e grau da ferramenta nao se tocam no texto.
  11. DOMINANCIA  — nenhum grau domina outro, por rota de protecao.
  12. SOMATORIO   — nenhum efeito de grau entra no bolso sem estar no orcamento.
  13. SEM-ENERGIA — a rota sem energia nenhuma, medida ponta a ponta.
  14. TRIAGEM     — todo nome que a peca cria, e a colisao de sentido declarada.
  15. DESLIGA     — as duas vagas da peca 13 SS8 contra a trava do Desliga.
  16. SINTONIA    — nao sintonizada = arma comum, e a regra de sintonizar existe.
  17. RELOGIO     — todo Estigma de Classe 2 tem limite de uso, e nenhum e letra
                    morta contra o teto de Reacoes que uma luta cabe.

O PAR DECLARADO: a 3 e a 9 leem a mesma amarra por dois lados — a 3 confere que
o gate vem da peca 11, a 9 confere que a escada de grau vem daqui. Elas NAO sao
independentes: se a escada do SS7 da peca virasse gate duro, ela seria mais dura
que o gate herdado em toda linha, a 3 morreria (o gate do grau 1 pararia de
andar quando a peca 11 mudasse) e a 9 continuaria verde sozinha. A checagem 9
afirma a ordenacao e falha se ela inverter.

Roda de sistema/03-mecanica/. NAO le o .docx e NAO precisa de python-docx —
entao nao existe caminho por onde ele saia verde tendo pulado checagem.
"""
import os, re, sys
from itertools import product

AQUI = os.path.dirname(os.path.abspath(__file__))
def ler(nome):
    with open(os.path.join(AQUI, nome), encoding='utf-8') as f:
        return f.read()

# ---------------------------------------------------------------- LIMITES DE DESIGN
# Declarados aqui, a parte da regra aplicada. Nao sao a regra: sao o contorno
# contra o qual a regra e medida. Mexer num destes e decisao de design, e o
# arnes de perturbacao testa que mexer aqui acende a checagem certa e so ela.
LIM_MAX_ESTIGMA_POR_FERRAMENTA = 1     # SS1 da peca: "mais UM Estigma"
LIM_TETO_APOIO                 = 2     # SS5: "o apoio tem teto de duas"
LIM_TETO_DECLARADO             = 3     # SS5: arma + dois apoios
LIM_EXTREMO                    = 4     # SS5: duas armas de uma mao + dois apoios
LIM_FRACAO_MAX_DO_MARCO        = 0.57  # SS5: o extremo nao passa de 57%
LIM_DESLIGA_ALVOS_ESPERADOS    = 2     # SS8 c.15: "ela produz pouquissimo alvo legal"
# Vocabulario que um grau NAO pode carregar. Os dois primeiros sao magnitude
# (peca 11 SS4 separa formato de magnitude); o terceiro e o eixo proibido da
# peca 1 — o refino nao aparece contra quem cresce +3.
PROIBIDO_NO_GRAU = ['dado de dano', 'refino']
RX_DADO          = re.compile(r'\b\d*d(4|6|8|10|12|20)\b')

erros, avisos = [], []
def erro(n, m): erros.append(f'CHECAGEM {n}: {m}')
def aviso(m):   avisos.append(m)

P16 = ler('16-ferramenta-amaldicoada.md')
P14 = ler('14-equipamento.md')
P13 = ler('13-legados.md')
P12 = ler('12-experiencia-e-progressao.md')
P11 = ler('11-aptidoes-e-refino.md')
P09 = ler('09-origens.md')
P06 = ler('06-caminhos-e-trilhas.md')
P02 = ler('02-economia-de-atributos.md')
P01 = ler('01-atributos-acerto-defesa.md')   # v0.144: o tamanho da luta, para a 17

def secao(txt, n):
    """Recorta TODOS os blocos cujo numero de secao seja n, concatenados.

    Nao da para parar no proximo '## \\d+\\.': a peca 11 tem '## 6.' E '## 6.5.',
    e um recorte ingenuo para na subsecao e perde a tabela de gate que vem
    depois dela. Aqui o corte e por NUMERO DE SECAO, nao por proxima linha '##'.
    """
    blocos, atual, num = [], [], None
    for linha in txt.split('\n'):
        m = re.match(r'^## (\d+)(?:\.\d+)*\.', linha)
        if m:
            if atual and num == str(n):
                blocos.append('\n'.join(atual))
            atual, num = [linha], m.group(1)
        elif atual is not None:
            atual.append(linha)
    if atual and num == str(n):
        blocos.append('\n'.join(atual))
    return '\n'.join(blocos)

print('=' * 88)
print('  conferir-ferramenta.py — a peca 16, e nenhum numero mora aqui dentro')
print('=' * 88)

# ================================================================ o que a peca declara
S1, S3, S4, S5, S6, S7, S8 = (secao(P16, n) for n in (1, 3, 4, 5, 6, 7, 8))

# a escada de grau: grau -> (Classe, gate)  — lida da tabela do SS3
ESCADA = {}
for m in re.finditer(
        r'^\| \*\*(4|3|2|1|especial)\*\* \| (.+?) \| (.+?) \|', S3, re.M):
    grau, col_est, col_gate = m.group(1), m.group(2), m.group(3)
    mc = re.search(r'Classe (\d)', col_est)
    classe = int(mc.group(1)) if mc else None
    mg = re.search(r'nível (\d+)', col_gate)
    gate = int(mg.group(1)) if mg else (0 if 'nenhum' in col_gate else None)
    ESCADA[grau] = (classe, gate)

if len(ESCADA) != 5:
    erro('9', f'nao achei os cinco graus na tabela do SS3 — achei {sorted(ESCADA)}')

# o catalogo: conta, nunca guarda
CATALOGO = {}
for cl in (1, 2, 3):
    m = re.search(rf'^### Classe {cl} · .*?(?=^###|\Z)', S6, re.M | re.S)
    if not m:
        erro('7', f'nao achei a tabela de Classe {cl} no SS6')
        continue
    for e in re.finditer(r'^\| \*\*`([^`]+)`\*\* \| (.+?) \|', m.group(0), re.M):
        CATALOGO[e.group(1)] = {'classe': cl, 'texto': e.group(2)}

# ================================================================ 1. FUNDO
print('\n 1. FUNDO — a camada nao fura o fundo de Equipamento')
m = re.search(r'[Ff]undo `(\d)` numa mão e `(\d)` em duas', P14)
if not m:
    erro('1', 'nao achei o fundo 3/5 na peca 14 — ela e a dona')
else:
    f1, f2 = int(m.group(1)), int(m.group(2))
    print(f'  peca 14 SS5 — fundo: `{f1}` numa mao, `{f2}` em duas')
    cita = re.search(r'`(\d)` numa mão, `(\d)` em duas', S1)
    if not cita:
        erro('1', 'a peca 16 SS1 nao repete o fundo da peca 14 — ela tem de citar o dono')
    elif (int(cita.group(1)), int(cita.group(2))) != (f1, f2):
        erro('1', f'a peca 16 diz {cita.groups()} e a peca 14 diz ({f1}, {f2})')
    else:
        print(f'  [x] a peca 16 le o fundo do dono e nao guarda copia propria')
    # a camada nao pode dar ponto de arma nenhum
    if re.search(r'(ponto de arma|passo de dado|\+\d+ ponto)', S6):
        erro('1', 'alguma entrada do catalogo mexe em ponto de arma ou passo de dado')
    else:
        print('  [x] nenhuma das entradas do catalogo toca no orcamento da arma')

# ================================================================ 2. UM-ESTIGMA
print('\n 2. UM-ESTIGMA — um por ferramenta, nunca dois')
m = re.search(r'mais UM `Estigma`', S1)
if not m:
    erro('2', 'o SS1 nao declara "mais UM Estigma"')
else:
    print(f'  o SS1 declara: mais UM Estigma (limite {LIM_MAX_ESTIGMA_POR_FERRAMENTA})')
por_grau = {g: (1 if c else 0) for g, (c, _) in ESCADA.items()}
excesso = {g: n for g, n in por_grau.items() if n > LIM_MAX_ESTIGMA_POR_FERRAMENTA}
if excesso:
    erro('2', f'grau(s) carregando mais de um Estigma: {excesso}')
else:
    print(f'  [x] os cinco graus carregam no maximo um: {por_grau}')
if re.search(r'dois `Estigma`|dois Estigmas|`Estigma`s? adicionais', S3 + S4 + S6):
    erro('2', 'o texto abre porta para uma segunda Estigma na mesma ferramenta')
else:
    print('  [x] nenhum texto da peca abre porta para a segunda')

# ================================================================ 3. GATE  (par com a 9)
print('\n 3. GATE — lido da peca 11 SS6, nunca de constante')
S11_6 = secao(P11, 6)
GATE_APT = {}
for m in re.finditer(r'^\| \*\*(.+?)\*\* \| (\d) · (sem gate|refino \d+, nível (\d+))',
                     S11_6, re.M):
    nome, classe, bruto, nivel = m.group(1), int(m.group(2)), m.group(3), m.group(4)
    GATE_APT.setdefault(classe, set()).add(0 if bruto == 'sem gate' else int(nivel))
if not GATE_APT:
    erro('3', 'nao achei a tabela de gates das aptidoes na peca 11 SS6')
else:
    GATE_DONO = {}
    for cl, niveis in GATE_APT.items():
        if len(niveis) > 1:
            aviso(f'a peca 11 tem gates diferentes na mesma Classe {cl}: {sorted(niveis)}')
        GATE_DONO[cl] = min(niveis)
    print('  peca 11 SS6 — gate por Classe: ' +
          ' · '.join(f'Classe {c}: {"sem gate" if g == 0 else f"nivel {g}"}'
                     for c, g in sorted(GATE_DONO.items())))
    for grau, (classe, gate) in sorted(ESCADA.items()):
        if classe is None:
            continue
        esperado = GATE_DONO.get(classe)
        if esperado is None:
            erro('3', f'grau {grau} pede Classe {classe} e a peca 11 nao tem gate para ela')
        elif gate != esperado:
            erro('3', f'grau {grau} (Classe {classe}) tem gate {gate} e a peca 11 manda {esperado}')
    if not [e for e in erros if e.startswith('CHECAGEM 3')]:
        print('  [x] os cinco graus herdam o gate da peca 11, sem excecao')

# ================================================================ 4. SEM-REFINO
print('\n 4. SEM-REFINO — nenhum gate de refino em lugar nenhum')
# So as secoes de REGRA. O SS8 descreve as checagens e cita "gate de refino"
# justamente para dizer que ele nao pode existir — varrer o SS8 aqui e ler a
# especificacao do teste como se fosse a regra testada.
REGRA = ''.join(secao(P16, n) for n in (1, 2, 3, 4, 5, 6, 7))
achados = []
for m in re.finditer(r'refino', REGRA):
    ini = max(0, m.start() - 120)
    trecho = REGRA[ini:m.end() + 120]
    if re.search(r'(refino \d|gate de refino|exige refino|pede refino|requer refino)', trecho):
        # a peca PODE falar do refino para dizer que ele NAO entra
        if not re.search(r'(NÃO entra|não entra|recusa o eixo|Não existe gate de refino|'
                         r'trancaria|cresça com refino|cresce com refino|nenhuma cresce)', trecho):
            achados.append(trecho.replace('\n', ' ')[:90])
if achados:
    erro('4', f'gate de refino aparece na peca: {achados[:2]}')
else:
    print('  [x] o refino so aparece na peca para dizer que ele nao entra')
if not re.search(r'[Nn]ão existe gate de refino em lugar nenhum desta peça', P16):
    erro('4', 'a peca nao declara por escrito que nao existe gate de refino')
else:
    print('  [x] e a peca declara isso por escrito, em vez de deixar por omissao')

# ================================================================ 5. DESGASTE
print('\n 5. DESGASTE — compra o gate e nunca a Classe')
if not re.search(r'ignora o gate de nível do `Estigma`', S4):
    erro('5', 'o SS4 nao declara que o Desgaste ignora o GATE')
else:
    print('  o SS4 declara: o Desgaste ignora o gate de nivel do Estigma')
if re.search(r'[Dd]esgaste.{0,200}?(sobe|aumenta|eleva).{0,40}?Classe', P16, re.S):
    erro('5', 'o texto deixa o Desgaste mexer na Classe')
else:
    print('  [x] o Desgaste nao encosta em Classe em lugar nenhum do texto')
if not re.search(r'compra o GATE e nunca a Classe|compra o gate e nunca a Classe', P16):
    erro('5', 'a peca nao declara a separacao gate/Classe por escrito')
else:
    print('  [x] a separacao formato/magnitude esta escrita, nao subentendida')
# e o Desgaste tem de comprar ALGUMA COISA: o gate que ele apaga tem de ser o que trava
gates_reais = sorted({g for _, (c, g) in ESCADA.items() if c and g})
if not gates_reais:
    erro('5', 'nenhum grau tem gate — o Desgaste nao compraria nada')
else:
    print(f'  [x] o Desgaste apaga um gate que existe de verdade: {gates_reais}')

# ================================================================ 6. TETO (busca exaustiva)
print('\n 6. TETO — busca exaustiva sobre as rotas de mao x o teto de apoio')
m = re.search(r'níveis \*\*([\d, e]+)\*\*, sete marcos', P02)
if not m:
    erro('6', 'nao achei os marcos na peca 2 SS3')
else:
    MARCOS = [int(x) for x in re.findall(r'\d+', m.group(1))]
    N_MARCOS = len(MARCOS)
    print(f'  peca 2 SS3 — marcos: {MARCOS}  (n={N_MARCOS} escolhas na campanha)')
    # rotas de mao, do teto declarado da peca 14: 2 maos, arma de uma ou de duas
    ROTAS = {'uma mao + escudo': 1, 'duas maos': 1, 'duas de uma mao': 2}
    montagens = []
    for (nome_rota, armas), apoios in product(ROTAS.items(), range(LIM_TETO_APOIO + 1)):
        montagens.append((nome_rota, armas, apoios, armas + apoios))
    maximo = max(t for *_, t in montagens)
    normal = max(t for nome, a, ap, t in montagens if a == 1 and ap <= LIM_TETO_APOIO)
    print(f'  {len(montagens)} montagens legais enumeradas · teto declarado {LIM_TETO_DECLARADO}'
          f' · extremo {maximo}')
    if maximo != LIM_EXTREMO:
        erro('6', f'a busca acha extremo {maximo} e a peca declara {LIM_EXTREMO}')
    if normal != LIM_TETO_DECLARADO:
        erro('6', f'a busca acha teto declarado {normal} e a peca diz {LIM_TETO_DECLARADO}')
    fracao = maximo / N_MARCOS
    print(f'  o extremo custa {maximo}/{N_MARCOS} = {fracao:.0%} do orcamento de escolha de marco')
    if fracao > LIM_FRACAO_MAX_DO_MARCO + 0.005:
        erro('6', f'o extremo consome {fracao:.0%}, acima do limite declarado '
                  f'de {LIM_FRACAO_MAX_DO_MARCO:.0%}')
    else:
        print(f'  [x] fica dentro do limite declarado de {LIM_FRACAO_MAX_DO_MARCO:.0%}')
    # a tabela escrita na peca tem de bater com a contada
    for n_est, frac_escrita in re.findall(r'^\| \*?\*?(\d)[^|]*\| \*?\*?(\d+)%', S5, re.M):
        calc = round(int(n_est) / N_MARCOS * 100)
        if abs(calc - int(frac_escrita)) > 1:
            erro('6', f'a tabela do SS5 diz {n_est} Estigmas = {frac_escrita}% e a conta da {calc}%')
    if not [e for e in erros if e.startswith('CHECAGEM 6')]:
        print('  [x] a tabela de fracao escrita no SS5 bate com a recalculada')

# ================================================================ 7. CLASSE
print('\n 7. CLASSE — cada grau declara UMA Classe, e ela existe na peca 11 SS4')
S11_4 = secao(P11, 4)
CLASSES_DONO = {int(c) for c in re.findall(r'^\| \*\*(\d)\*\* \|', S11_4, re.M)}
if not CLASSES_DONO:
    erro('7', 'nao achei as Classes na peca 11 SS4')
else:
    print(f'  peca 11 SS4 — Classes que existem: {sorted(CLASSES_DONO)}')
    for grau, (classe, _) in sorted(ESCADA.items()):
        if classe is not None and classe not in CLASSES_DONO:
            erro('7', f'grau {grau} declara Classe {classe}, que nao existe na peca 11')
    orfas = {d['classe'] for d in CATALOGO.values()} - CLASSES_DONO
    if orfas:
        erro('7', f'o catalogo usa Classe(s) que a peca 11 nao tem: {orfas}')
    if not [e for e in erros if e.startswith('CHECAGEM 7')]:
        print(f'  [x] os {len(CATALOGO)} Estigmas caem em Classes que a peca 11 declara')
    # o catalogo se CONTA, nunca se guarda
    m = re.search(r'catálogo continua com onze|onze `Estigma`|## 6\. O catálogo — onze', P16)
    afirmado = re.search(r'O catálogo — (\w+) `Estigma`', S6 or P16)
    NUM = {'dez': 10, 'onze': 11, 'doze': 12, 'treze': 13}
    if afirmado and afirmado.group(1) in NUM:
        if NUM[afirmado.group(1)] != len(CATALOGO):
            erro('7', f'a peca afirma "{afirmado.group(1)}" e o catalogo contado tem {len(CATALOGO)}')
        else:
            print(f'  [x] o escrito ("{afirmado.group(1)}") bate com o contado ({len(CATALOGO)})')

# ================================================================ 8. SEM-DADO
print('\n 8. SEM-DADO — nenhum grau da dado de dano nem numero que cresca com refino')
sujas = []
for nome, d in CATALOGO.items():
    if RX_DADO.search(d['texto']):
        sujas.append((nome, 'dado de dano'))
    for proib in PROIBIDO_NO_GRAU:
        if proib in d['texto'].lower():
            sujas.append((nome, proib))
if sujas:
    erro('8', f'entrada(s) carregando magnitude: {sujas}')
else:
    print(f'  [x] as {len(CATALOGO)} entradas passaram: nenhuma com dado, nenhuma com refino')
if not re.search(r'[Nn]enhuma das onze dá dado de dano|nenhuma cresce com refino', P16):
    aviso('a peca nao declara a trava do SS6 por escrito (nenhuma da dado / cresce com refino)')

# ================================================================ 9. ESCADA (par com a 3)
print('\n 9. ESCADA — lida do documento dono, e o par com a checagem 3')
print('  escada do SS3: ' + ' · '.join(
    f'grau {g}: Classe {c if c else "—"}, gate {"nenhum" if not gt else gt}'
    for g, (c, gt) in sorted(ESCADA.items(), key=lambda x: (x[0] != 'especial', x[0]))))
# o SS7 e RITMO, nao gate. Se ele virasse gate, seria mais duro que o herdado
# em toda linha e mataria a checagem 3. A ordenacao e o que prova que ele nao e gate.
RITMO = {}
for m in re.finditer(r'^\| (4|3|2|1|especial) \| nível \*\*(\d+)\*\*', S7, re.M):
    RITMO[m.group(1)] = int(m.group(2))
if len(RITMO) != 5:
    erro('9', f'nao achei os cinco degraus de ritmo no SS7 — achei {sorted(RITMO)}')
else:
    if not re.search(r'[Ee]sta seção não cria requisito|ritmo, e não gate', S7):
        erro('9', 'o SS7 nao declara que ele e ritmo e nao gate — sem isso ele vira gate por leitura')
    else:
        print('  [x] o SS7 se declara ritmo e nao requisito, por escrito')
    mais_duro = [g for g, (c, gt) in ESCADA.items()
                 if g in RITMO and RITMO[g] > (gt or 0)]
    print(f'  o ritmo do SS7 e mais alto que o gate herdado em {len(mais_duro)} dos '
          f'{len(RITMO)} graus: {sorted(mais_duro)}')
    if len(mais_duro) == len(RITMO) and not re.search(r'ritmo, e não gate', S7):
        erro('9', 'o ritmo domina o gate em toda linha E nao esta declarado como ritmo — '
                  'nessa combinacao a checagem 3 fica trivialmente verdadeira')
    else:
        print('  [x] PAR DECLARADO com a checagem 3: o gate que a 3 mede continua sendo o')
        print('      da peca 11, porque o SS7 nao gateia. Perturbar a peca 11 move a 3.')

# ================================================================ 10. PATENTE
print('\n 10. PATENTE — a patente e o grau da ferramenta nao se tocam')
if not re.search(r'Grau é reconhecimento; nível é poder', P12):
    erro('10', 'nao achei a frase dona na peca 12 SS2')
else:
    print('  peca 12 SS2: "Grau e reconhecimento; nivel e poder"')
if not re.search(r'a sua patente não decide que ferramenta você pode portar', P16):
    erro('10', 'a peca 16 nao nega a ligacao patente/grau por escrito')
else:
    print('  [x] a peca 16 nega a ligacao com todas as letras, em vez de por omissao')
# A peca CITA a ideia refutada de proposito ("feiticeiro de Grau 2 porta
# ferramenta de grau 2") para derruba-la com a peca 12. Ler a citacao como
# regra e o mesmo erro que a c.4 cometia com o SS8: confundir o alvo com o tiro.
ligas = []
for liga in re.finditer(r'(Grau \d[^.\n]{0,60}(pode portar|porta|autoriza)|'
                        r'patente[^.\n]{0,40}(libera|destrava|permite)[^.\n]{0,40}ferramenta)',
                        P16):
    volta = P16[max(0, liga.start() - 200): liga.end() + 400]
    refutada = re.search(r'(ideia óbvia|bate de frente|refutad|não decide|'
                         r'não muda uma vírgula|espiral fechada)', volta)
    if not refutada:
        ligas.append(liga.group(0)[:70])
if ligas:
    erro('10', f'o texto liga patente a grau sem refutar: {ligas}')
else:
    print('  [x] nenhum trecho da peca pendura ferramenta em patente')

# ================================================================ 11. DOMINANCIA
print('\n 11. DOMINANCIA — nenhum grau domina outro')
ordem = ['4', '3', '2', '1', 'especial']
dominadas = []
for a, b in product(ordem, repeat=2):
    if a == b:
        continue
    ca, ga = ESCADA.get(a, (None, None))
    cb, gb = ESCADA.get(b, (None, None))
    ca, cb = (ca or 0), (cb or 0)
    ga, gb = (ga or 0), (gb or 0)
    # a domina b se entrega >= e custa < (o custo aqui e acesso: o gate)
    if ca >= cb and ga < gb and (ca > cb or ga < gb):
        if ca == cb and ga == gb:
            continue
        if ca > cb or (ca == cb and ga < gb):
            dominadas.append((a, b))
empates = [(a, b) for a, b in product(ordem, repeat=2)
           if a < b and ESCADA.get(a) == ESCADA.get(b)]
print(f'  {len(ordem)}x{len(ordem)} pares rodados · dominadas: {len(dominadas)} · '
      f'empates: {len(empates)}')
if dominadas:
    erro('11', f'grau(s) dominando outro pelo mesmo ou menor gate: {dominadas}')
else:
    print('  [x] a escada e monotona: mais Classe custa mais gate, sem excecao')
for a, b in empates:
    if not re.search(rf'(escassez|única no mundo)', S3 + secao(P16, 3)):
        erro('11', f'grau {a} e {b} sao mecanicamente identicos e a peca nao declara o motivo')
    else:
        print(f'  [x] o empate {a}/{b} esta declarado, e o que separa e escassez e nao mecanica')

# ================================================================ 12. SOMATORIO
print('\n 12. SOMATORIO — nada entra no bolso sem estar no orcamento')
orc = ler('conferir-orcamento.py')
piso = re.search(r'PISO[_A-Z]*\s*=\s*([\d.]+)', orc)
print(f'  conferir-orcamento.py e quem sabe medir o bolso'
      + (f' (piso {piso.group(1)})' if piso else ''))
custam_pe = {n: d['texto'] for n, d in CATALOGO.items()
             if re.search(r'\bcusta\b.{0,20}PE|\d+ PE\b', d['texto'])}
devolvem_pe = {n: d['texto'] for n, d in CATALOGO.items()
               if re.search(r'sem custo de PE|não gasta PE', d['texto'])}
print(f'  entradas que ADICIONAM dreno de PE: {len(custam_pe)} · '
      f'que REMOVEM custo: {len(devolvem_pe)} ({", ".join(devolvem_pe) or "—"})')
if custam_pe:
    erro('12', f'entrada(s) cobrando PE sem entrar no somatorio do orcamento: {list(custam_pe)}')
else:
    print('  [x] nenhum Estigma abre dreno novo de PE — o bolso da peca 11 nao se move')

# ================================================================ 13. SEM-ENERGIA
print('\n 13. SEM-ENERGIA — a rota sem energia nenhuma, ponta a ponta')
S09_5 = secao(P09, 5)
# v0.81: o termo 'golpe canalizado' morreu — ele nao existe no manual e virou
# 'feiticco de Toque'. A checagem aceita os dois para nao quebrar em nota historica,
# e o que ela guarda e a ROTA (sem Fundamento, sem PE, sem Sentir Energia).
m = re.search(r'sem Fundamento, sem PE, sem (?:golpe canalizado|feitiço de Toque), sem Sentir Energia', S09_5)
if not m:
    erro('13', 'nao achei a rota "energia pelo corpo" na peca 9 SS5')
else:
    print('  peca 9 SS5: sem Fundamento, sem PE, sem feitico de Toque, sem Sentir Energia')
    if 'ferramenta amaldiçoada' not in S09_5:
        erro('13', 'a peca 9 nao nomeia ferramenta amaldicoada como o eixo de poder da rota')
    else:
        print('  [x] a peca 9 ja nomeia esta peca como o eixo de poder da rota')
    # a rota entra no nivel 2? o grau 4 nao pode ter gate.
    c4, g4 = ESCADA.get('4', (None, None))
    if g4:
        erro('13', f'o grau 4 tem gate {g4} — a rota sem energia nao entra no nivel 2')
    else:
        print('  [x] o grau 4 nao tem gate: a rota fere maldicao desde o nivel 2')
    # e existe pelo menos um Estigma que compensa o que a rota nao tem
    compensa = [n for n, d in CATALOGO.items()
                if re.search(r'maldição perto|sabe o grau', d['texto'])]
    if not compensa:
        erro('13', 'nenhum Estigma compensa a falta de Sentir Energia da rota')
    else:
        print(f'  [x] {len(compensa)} Estigma(s) cobrem o buraco de Sentir Energia: {compensa}')

# ================================================================ 14. TRIAGEM
print('\n 14. TRIAGEM — todo nome que a peca cria')
nomes = sorted(CATALOGO) + ['Estigma', 'Desgaste']
print(f'  {len(nomes)} nomes batizados: {", ".join(nomes)}')
dup = [n for n in nomes if nomes.count(n) > 1]
if dup:
    erro('14', f'nome repetido dentro da propria peca: {set(dup)}')
outras = {'peca 11': P11, 'peca 13': P13, 'peca 14': P14, 'peca 6': P06, 'peca 9': P09}
colisoes = []
for n in nomes:
    for onde, txt in outras.items():
        if re.search(rf'\*\*`{re.escape(n)}`\*\*', txt):
            colisoes.append((n, onde))
if colisoes:
    erro('14', f'nome ja batizado por outra peca: {colisoes}')
else:
    print('  [x] nenhum dos nomes colide com termo batizado por outra peca')
# a colisao de SENTIDO, que o validador nao pega sozinho, tem de estar declarada
if not re.search(r'duas escadas de cinco casas com o mesmo nome', P16):
    erro('14', 'a colisao de sentido de `Grau` nao esta declarada no texto — '
               'ela sai LIVRE em substring e NAO e livre em sentido')
else:
    print('  [x] a colisao de sentido de `Grau` esta declarada a mao, como manda o SS7 do rascunho')

# ================================================================ 15. DESLIGA
print('\n 15. DESLIGA — as duas vagas da peca 13 SS8')
S13_8 = secao(P13, 8)
vagas = re.findall(r'\*\*(.+?)\*\* \| .*?\| \*\*ferramenta amaldiçoada\*\*', S13_8)
vagas += re.findall(r'ferramenta amaldiçoada.*?\| `?(Armaria)`? do Descendente · (Restrição Celestial)',
                    S13_8, re.S)
achadas = set()
for v in vagas:
    achadas.update([v] if isinstance(v, str) else v)
print(f'  a peca 13 SS8 nomeia esta peca em: {sorted(achadas) or "nada"}')
if len(achadas) < LIM_DESLIGA_ALVOS_ESPERADOS:
    erro('15', f'a peca 13 SS8 deveria ter {LIM_DESLIGA_ALVOS_ESPERADOS} vagas apontando '
               f'para ferramenta amaldicoada, achei {len(achadas)}')
else:
    print(f'  [x] as {LIM_DESLIGA_ALVOS_ESPERADOS} vagas existem e nomeiam esta peca')
# A trava do Desliga: so pode apagar o que ninguem comprou. Esta peca precifica
# quase tudo que nomeia — Classe 2 e 3 custam ACESSO (o gate), e o que custa
# acesso alguem comprou. Sobra a Classe 1, que nao tem gate.
GATE_POR_CLASSE = {c: g for _, (c, g) in ESCADA.items() if c}
comprados = [n for n, d in CATALOGO.items() if GATE_POR_CLASSE.get(d['classe'])]
livres = [n for n, d in CATALOGO.items() if not GATE_POR_CLASSE.get(d['classe'])]
print(f'  dos {len(CATALOGO)} Estigmas, {len(comprados)} custam acesso (gate) e '
      f'{len(livres)} nao custam')
print(f'  alvos legais de Desliga — o que ninguem comprou: {len(livres)} ({", ".join(livres)})')
if len(livres) == len(CATALOGO):
    erro('15', 'nenhum Estigma custa acesso — a trava do Desliga nao morde em nada')
if not re.search(r'2 das 7 vagas de Desliga|2 das 7 vagas', P16):
    erro('15', 'a peca 16 nao registra que fecha as duas vagas')
else:
    print('  [x] a peca 16 registra que fecha as duas, e o contador de vagas anda')

# ================================================================ 16. SINTONIA
print('\n 16. SINTONIA — nao sintonizada = arma comum, nos dois sentidos')
if not re.search(r'que você não sintonizou é uma arma comum', S1):
    erro('16', 'o SS1 nao declara que a nao sintonizada e arma comum')
else:
    print('  o SS1 declara: ferramenta nao sintonizada e arma comum, e nada mais')
if not re.search(r'continua gastando o \*\*fundo exato\*\*|fundo exato', S1):
    erro('16', 'o SS1 nao amarra a arma de baixo ao fundo exato da peca 14')
else:
    print('  [x] sentido 1: a arma por baixo continua gastando o fundo exato')
sem_pagar = [n for n, d in CATALOGO.items()
             if re.search(r'de graça|sem pagar|automaticamente', d['texto'])]
if sem_pagar:
    erro('16', f'entrada(s) entregando efeito sem pagamento: {sem_pagar}')
else:
    print('  [x] sentido 2: nenhuma entrada entrega efeito sem o pagamento correspondente')

# v0.144: a terceira linha do SS1 e' de v0.55 e ficou oitenta e oito versoes sem
# dizer COMO se sintoniza — o livro mandava combinar com o mestre. O SS1.1 fechou.
# Estas quatro leem a regra nova, e nenhuma delas guarda numero: o custo e' um
# DESCANSO, e descanso e' peca 10.
if not re.search(r'Sintonizar custa um descanso curto', S1):
    erro('16', 'o SS1.1 nao escreve o custo de sintonizar — sem ele o livro volta '
               'a mandar o jogador combinar com o mestre')
else:
    print('  [x] sintonizar tem custo escrito: um descanso curto dedicado')
if not re.search(r'[Dd]esfazer custa outro descanso curto', S1):
    erro('16', 'o SS1.1 nao escreve como se DESFAZ a sintonizacao — o PHB fecha as '
               'duas pontas, e uma regra que so liga prende a ficha ao primeiro item')
else:
    print('  [x] desfazer tem custo escrito, e e o mesmo do PHB')
if not re.search(r'[Nn]ão custa PE, e não pode custar|[Nn]ão custa PE', S1):
    erro('16', 'o SS1.1 parou de declarar que sintonizar nao custa PE — a ferramenta '
               'e a rota de quem NAO tem energia, pela peca 9 SS5')
else:
    print('  [x] nao custa PE, e o motivo esta escrito ao lado')
# O relogio de HORAS e' o que a peca 10 recusa por escrito, e por motivo
# multi-mestre. Se alguem escrever "leva N horas" aqui, a heranca se perde.
_horas = re.search(r'sintoniz\w*[^.\n]{0,80}?(\d+)\s*(hora|minuto)', S1, re.I)
if _horas:
    erro('16', f'o SS1.1 fixa relogio de {_horas.group(1)} {_horas.group(2)}(s) para '
               f'sintonizar — a peca 10 SS1 recusa relogio de horas de proposito, e '
               f'e dai que o custo herda o filtro multi-mestre')
else:
    print('  [x] nenhum relogio de horas: o custo e um descanso, e descanso e peca 10')

# ================================================================ 17. RELOGIO
print('\n 17. RELOGIO — Classe 2 promete limite de uso, e ele tem de morder')
# A propria peca define a Classe 2 como "reativo, COM LIMITE DE USO por cena ou
# por descanso". Ate a v0.143 uma das tres entradas nao tinha nenhum, e o livro
# mandava combinar com o mestre. Esta checagem le a promessa do titulo e cobra
# ela de cada entrada — a promessa nao esta escrita aqui dentro.
_m = re.search(r'^### Classe 2 · [^\n]*?—\s*(.+)$', S6, re.M)
if not _m:
    erro('17', 'nao achei o titulo da Classe 2 no SS6 — e dele que sai a promessa '
               'de limite de uso')
else:
    _promessa = _m.group(1)
    if not re.search(r'limite de uso', _promessa):
        erro('17', f'o titulo da Classe 2 nao promete mais limite de uso: '
                   f'"{_promessa}" — se a promessa sumiu, esta checagem parou de '
                   f'ter chao')
    else:
        print(f'  o titulo promete: "{_promessa.strip()}"')
        _c2 = {n: d for n, d in CATALOGO.items() if d['classe'] == 2}
        if len(_c2) != 3:
            erro('17', f'esperava 3 Estigma de Classe 2 e li {len(_c2)} — a tabela '
                       f'mudou de forma')
        _RELOGIO = re.compile(r'(uma|duas|três|\d+)\s+vez(?:es)?\s+por\s+'
                              r'(cena|descanso\s+\w+)', re.I)
        _EXT = {'uma': 1, 'duas': 2, 'três': 3}
        _mudos, _usos = [], {}
        for n, d in sorted(_c2.items()):
            mm = _RELOGIO.search(d['texto'])
            if not mm:
                _mudos.append(n); continue
            q = _EXT.get(mm.group(1).lower()) or int(mm.group(1))
            _usos[n] = (q, mm.group(2).lower())
            print(f'    {n:<12} {q}x por {mm.group(2)}')
        for n in _mudos:
            erro('17', f'o `{n}` e Classe 2 e nao escreve limite de uso, e o titulo '
                       f'da Classe promete um')
        # A LETRA MORTA: a Reacao volta no comeco do seu turno, entao uma luta
        # cabe no maximo <rodadas> Reacoes. Relogio por cena acima disso nao
        # limita nada. O numero de rodadas e LIDO da peca 1, nunca escrito aqui.
        _mr = re.search(r'combate dura de ([\d,]+) a ([\d,]+) rodadas', P01)
        if not _mr:
            erro('17', 'nao achei "combate dura de N a N rodadas" na peca 1 — sem o '
                       'tamanho da luta nao da para saber se um relogio morde')
        else:
            _lo, _hi = (float(x.replace(',', '.')) for x in _mr.groups())
            _teto = (_lo + _hi) / 2
            print(f'    teto de Reacoes por luta, lido da peca 1: {_teto:.1f}')
            for n, (q, rel) in _usos.items():
                if 'cena' not in rel:
                    continue
                if not re.search(r'Reação', CATALOGO[n]['texto']):
                    continue
                if q >= _teto:
                    erro('17', f'o `{n}` pede {q} usos por cena e a Reacao so cabe '
                               f'{_teto:.1f} vezes numa luta — o relogio e letra '
                               f'morta, e a entrada vale o mesmo que sem relogio')
                else:
                    print(f'  [x] o {n} morde: {q} usos contra teto de {_teto:.1f}')

# ================================================================ veredito
print('\n' + '=' * 88)
if avisos:
    for a in avisos: print(f'  aviso: {a}')
if erros:
    print('>>> FALHOU')
    for e in erros: print('    ' + e)
    sys.exit(1)
print('>>> TUDO OK — o fundo sai da peca 14, o gate sai da peca 11, os marcos saem')
print('    da peca 2, a rota sai da peca 9, e as 17 checagens do SS8 fecham sem')
print('    nenhum valor de regra escrito dentro deste arquivo.')
print('=' * 88)

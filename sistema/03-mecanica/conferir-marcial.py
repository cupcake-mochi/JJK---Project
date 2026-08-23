#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
conferir-marcial.py — as treze checagens da peca 20, Tecnica Marcial.

NENHUM VALOR DE REGRA MORA AQUI. Orcamento, fatia, Rotina, condicao, escada de
grau e catalogo de arma saem dos documentos donos. O unico bloco com numero na
mao e o LIMITES DE DESIGN, declarado a parte da regra aplicada — que e a licao
no 8 do README: uma checagem nao pode se medir contra a propria constante.

A peca 20 e' quase toda HERANCA: ela nao inventa numero, ela promete que os
numeros de outras oito pecas continuam valendo. Entao quase toda checagem daqui
tem a forma "o dono continua dizendo X, e a peca 20 continua repetindo X".
"""
import os, re, sys, io, unicodedata

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.abspath(os.path.join(AQUI, '..', '..'))

erros, avisos, pulou = [], [], []
def erro(c, m):  erros.append(f'[{c}] {m}')
def aviso(m):    avisos.append(m)
def pular(c, m): pulou.append(f'[{c}] {m}')

def bloco(t):
    print('\n' + '=' * 88); print(t); print('=' * 88)

def ler(rel):
    p = rel if os.path.isabs(rel) else os.path.join(AQUI, rel)
    if not os.path.exists(p):
        p = os.path.join(RAIZ, rel)
    return io.open(p, encoding='utf-8').read()

def sa(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s)
                   if unicodedata.category(c) != 'Mn')

def num(s):
    return float(s.replace('.', '').replace(',', '.'))

P20 = ler('20-tecnica-marcial.md')
P6  = ler('06-caminhos-e-trilhas.md')
P9  = ler('09-origens.md')
P11 = ler('11-aptidoes-e-refino.md')
P13 = ler('13-legados.md')
P14 = ler('14-equipamento.md')
P16 = ler('16-ferramenta-amaldicoada.md')
P19 = ler('19-dano-e-condicoes.md')
P3  = ler('03-economia-de-acao-e-iniciativa.md')
EST = ler(os.path.join(RAIZ, 'sistema', 'ESTADO-ATUAL.md'))
MAN = ler(os.path.join(RAIZ, 'DESENHO-manhas.md'))

# ------------------------------------------------------------ LIMITES DE DESIGN
# Escritos a mao DE PROPOSITO e separados da regra aplicada. Perturbar um destes
# tem de acender; perturbar a regra la em cima tambem. Se so um dos dois acender,
# a checagem esta se medindo contra a propria constante.
TOLERANCIA_SOMA   = 2      # peca 6 SS5: o espalhamento de vida+PE que o projeto aceita
FILTRO_DOMINANCIA = 3.00   # o projeto reprova a partir daqui
GRUPOS_MINIMOS    = 2      # abaixo disto o `Desarmado` apaga a ficha — SS7 da peca 20
CATEGORIAS_ARMA   = 13     # quantas categorias a peca 14 SS5.1.2 tem


# ============================================================ 1
bloco('1. O ORCAMENTO E O PE DO CAMINHO, e esta peca nao escreve numero proprio')

mt = re.search(r'\|\s*PE por n[ií]vel\s*\|((?:\s*\*{0,2}\d+\*{0,2}\s*\|)+)', P6)
if not mt:
    erro(1, 'nao consegui ler a linha de PE por nivel da peca 6 SS5')
    PE_CAMINHO = []
else:
    PE_CAMINHO = [int(x) for x in re.findall(r'\d+', mt.group(1))]
    print(f'  peca 6 SS5 · PE por nivel, lido do dono: {PE_CAMINHO}')

mv = re.search(r'\|\s*vida por n[ií]vel\s*\|((?:\s*\*{0,2}\d+\*{0,2}\s*\|)+)', P6)
VIDA_CAMINHO = [int(x) for x in re.findall(r'\d+', mv.group(1))] if mv else []

if PE_CAMINHO:
    faixa = f'`{min(PE_CAMINHO)}` a `{max(PE_CAMINHO)}`'
    if faixa.replace('`', '') not in sa(P20).replace('`', ''):
        aviso(f'a peca 20 nao repete a faixa {faixa} do PE por nivel')
    else:
        print(f'  [x] a peca 20 cita a faixa {faixa}, e ela sai da peca 6')

# a peca 20 nao pode publicar uma coluna de PE por nivel propria
propria = re.findall(r'PE por n[ií]vel[^\n|]{0,20}[:=]\s*`?(\d+)`?', P20)
if propria:
    erro(1, f'a peca 20 publica PE por nivel proprio ({propria}) — o dono e a peca 6 SS5')
else:
    print('  [x] a peca 20 nao publica coluna de PE propria: ela cita o dono')

if 'Pontos de Esfor' not in P20 and 'Pontos de Esfor' in P9:
    aviso('a peca 9 SS5 fixou `Pontos de Esforco` e a peca 20 nao cita a leitura')
elif 'Pontos de Esfor' in P20:
    print('  [x] a peca 20 usa a sigla `PE` com a leitura que a v0.120 fixou')


# ============================================================ 2
bloco('2. A SOMA vida+PE CONTINUA PARELHA com esta peca em cima')

if PE_CAMINHO and VIDA_CAMINHO and len(PE_CAMINHO) == len(VIDA_CAMINHO):
    somas = [v + p for v, p in zip(VIDA_CAMINHO, PE_CAMINHO)]
    espalha = max(somas) - min(somas)
    print(f'  somas por Caminho, recontadas: {somas}   espalhamento {espalha}')
    if espalha > TOLERANCIA_SOMA:
        erro(2, f'a soma vida+PE espalha {espalha}, e o limite de design e {TOLERANCIA_SOMA}')
    else:
        print(f'  [x] espalhamento {espalha} <= {TOLERANCIA_SOMA}: a troca continua sabor')
    # CONTRA-TESTE embutido: e' esta peca que impede a coluna de valer zero
    sem = [v for v in VIDA_CAMINHO]
    esp0 = max(sem) - min(sem)
    if esp0 <= TOLERANCIA_SOMA:
        erro(2, f'com a coluna de PE valendo zero o espalhamento seria {esp0}, que passa — '
                'entao esta peca nao esta segurando nada e a checagem e trivial')
    else:
        print(f'  [x] contra-teste: com a coluna valendo zero o espalhamento seria {esp0}, '
              f'que reprova. E por isso que o orcamento e herdado')
else:
    erro(2, 'nao consegui reconstruir a tabela de vida+PE da peca 6 SS5')


# ============================================================ 3
bloco('3. TRES GRUPOS, DIFERENTES ENTRE SI, e nenhuma Manha junto')

manhas = re.findall(r'^\|\s*\*\*(.+?)\*\*\s*\|\s*`(.+?)`\s*\|.*?\|\s*\*\*([\d,]+)\*\*\s*\|$',
                    MAN, re.M)
if not manhas:
    erro(3, 'nao consegui ler a tabela das treze Manhas do DESENHO-manhas.md')
else:
    vals = [num(f) for _, _, f in manhas]
    media = sum(vals) / len(vals)
    print(f'  {len(manhas)} Manhas lidas do dono · media {media:.2f} fatia · '
          f'min {min(vals):.2f} · max {max(vals):.2f}')
    if len(manhas) != CATEGORIAS_ARMA:
        erro(3, f'li {len(manhas)} Manhas e o limite de design diz {CATEGORIAS_ARMA} '
                'categorias: o extrator ou a tabela mudou')

    mc = re.search(r'o Caminho leva \*{0,2}`?(\d+)`?\*{0,2} fatias', EST)
    if not mc:
        erro(3, 'nao achei o orcamento de Caminho em fatias no ESTADO-ATUAL')
    else:
        cam = float(mc.group(1))
        tres = 3 * media
        print(f'  tres Manhas medias = {tres:.2f} fatias contra um Caminho de {cam:.2f}')
        if tres < cam * 0.5:
            erro(3, f'tres Manhas dariam so {tres:.2f} de {cam:.2f} fatias — a proibicao do '
                    'SS4.1 deixou de ter motivo, e o texto dela virou regra sem conta')
        else:
            print(f'  [x] tres Manhas seriam {tres/cam*100:.1f}% de um Caminho inteiro: '
                  'e por isso que os grupos nao dao Manha')

if not re.search(r'Manha nenhuma', P20):
    erro(3, 'a peca 20 nao diz, com todas as letras, que os tres grupos nao dao Manha')
else:
    print('  [x] a peca 20 escreve `Manha nenhuma`')

SEC41 = P20[P20.find('### 4.1'):P20.find('### 4.2')]
if not re.search(r'diferentes entre si', SEC41):
    erro(3, 'o SS4.1 da peca 20 nao exige que os tres grupos sejam diferentes entre si — '
            'sem isso a resposta do SS7 ao `Desarmado` cai. (Procurado NA SECAO, e nao no '
            'arquivo: uma copia da frase em outro lugar nao e a regra.)')
else:
    print('  [x] o SS4.1 exige tres grupos diferentes entre si')


# ============================================================ 4
bloco('4. OS GRUPOS ACERTAM PELO ATRIBUTO DECLARADO')

cats = re.findall(r'^\|\s*\*\*(.+?)\*\*\s*\((\d+)\)\s*\|', P14, re.M)
CATS = [c.strip() for c, _ in cats]
print(f'  categorias lidas da peca 14 SS5.1.2: {len(CATS)}')
if len(CATS) != CATEGORIAS_ARMA:
    erro(4, f'li {len(CATS)} categorias de arma na peca 14 e o limite de design diz '
            f'{CATEGORIAS_ARMA}')

# a tabela da peca 20 SS5 tem de cobrir as treze, e so com Forca ou Destreza
sec5 = P20[P20.find('## 5.'):P20.find('## 6.')]
linhas = re.findall(r'^\|\s*\*\*(For[cç]a|Destreza)\*\*\s*\|\s*\*\*(\d+)\*\*\s*\|\s*(.+?)\s*\|$',
                    sec5, re.M)
if not linhas:
    erro(4, 'nao consegui ler a tabela de atributo por grupo da peca 20 SS5')
else:
    cobertas = set()
    for atr, qtd, lista in linhas:
        nomes = [sa(n.strip()) for n in lista.split('·')]
        if len(nomes) != int(qtd):
            erro(4, f'a peca 20 diz {qtd} grupos em {atr} e lista {len(nomes)}')
        cobertas |= set(nomes)
        print(f'  {atr}: {qtd} grupos, e a lista tem {len(nomes)}')
    faltando = {sa(c) for c in CATS} - cobertas
    if faltando:
        erro(4, f'categorias da peca 14 que a tabela da peca 20 nao classifica: '
                f'{sorted(faltando)}')
    else:
        print(f'  [x] as {len(CATS)} categorias da peca 14 estao todas classificadas')


# ============================================================ 5
bloco('5. NENHUM GRUPO DE ARMA ACERTA POR INTELIGENCIA, ESSENCIA OU CONSTITUICAO')

MENTAIS = ['Inteligencia', 'Essencia', 'Constituicao']
achados = [m for m in MENTAIS
           if re.search(rf'^\|\s*\*\*{m}\*\*\s*\|', sa(sec5), re.M)]
if achados:
    erro(5, f'a tabela da peca 20 SS5 poe grupo de arma em {achados} — a peca 1 so tem '
            'Forca no corpo a corpo e Destreza a distancia')
else:
    print('  [x] a tabela de grupos so tem Forca e Destreza')

if not re.search(r'nenhum grupo de arma acerta por Intelig', sa(P20), re.I):
    erro(5, 'a peca 20 nao declara que a rota de arma e sempre Forca ou Destreza')
else:
    print('  [x] a peca 20 declara o fechamento, com todas as letras')

if 'rota de ferramenta' not in P20 or not re.search(r'qualquer um dos cinco', P20):
    erro(5, 'a peca 20 fecha a rota de arma nos atributos mentais e nao abre a de '
            'ferramenta para os cinco: o restringido de Inteligencia fica sem rota')
else:
    print('  [x] e a rota de ferramenta declara qualquer um dos cinco: a saida existe')


# ============================================================ 6
bloco('6. A MAQUINA NAO TEM NUMERO PROPRIO — os de montagem batem com o dono')

# os tres numeros que a peca 20 repete, e quem e dono de cada um
ALVOS = [
    ('pontos por Classe',  r'[Pp]ontos s[aã]o `?3 [x×] Classe',       P20, r'3 × Classe'),
    ('custo em PE',        r'custo em PE [eé] o mesmo n[uú]mero',      P20, None),
    ('espacos de feitico', r'2 \+ \(n[ií]vel [÷/] 2\)',               P20, None),
]
for rot, rx, txt, _ in ALVOS:
    if re.search(rx, txt):
        print(f'  [x] a peca 20 cita `{rot}`')
    else:
        erro(6, f'a peca 20 parou de citar `{rot}`, que e a heranca que ela promete')

# a formula dos espacos tem dono no ESTADO-ATUAL / peca 11: as duas tem de bater
mest = re.search(r'`?2 \+ \(n[ií]vel [÷/] 2\)`?', EST)
if not mest:
    erro(6, 'nao achei a formula de espacos de feitico no ESTADO-ATUAL para comparar')
else:
    print('  [x] a formula de espacos bate com a do ESTADO-ATUAL, que e o dono dela')

# e ela NAO pode publicar dado de dano proprio
dados = re.findall(r'(?<![\w`])(\d*d\d+)(?![\w`])', P20)
maus = [d for d in dados if d not in ('d8', 'd12', 'd10', 'd20', '1d8')]
if maus:
    erro(6, f'a peca 20 publica dado que nao e do Fundamento nem da peca 14: {sorted(set(maus))}')
else:
    print(f'  [x] os dados citados sao os do Fundamento e da peca 14: {sorted(set(dados))}')


# ============================================================ 7
bloco('7. OS TRES RENOMES EXISTEM, e cada um continua sendo o que era')

RENOMES = {
    'Kata':    r'Libera|feiti[cç]o',
    'Ruptura': r'passa do limite de dano|limite de dano contra um alvo',
    'Ogi':     r'dano fixo',
}
tab = P20[P20.find('## 3.'):P20.find('## 4.')]
for novo, prova in RENOMES.items():
    if not re.search(rf'\*\*`?{novo}`?', sa(tab)):
        erro(7, f'o renome `{novo}` nao aparece na tabela do SS3 da peca 20')
    elif not re.search(prova, sa(tab), re.I):
        erro(7, f'`{novo}` aparece sem a frase que diz o que ele continua sendo')
    else:
        print(f'  [x] `{novo}` esta declarado, e o texto diz o que ele continua sendo')

# os tres originais tem de aparecer SO como origem do renome, nunca como regra viva
for velho in ('Libera[cç][aã]o M[aá]xima', 'T[eé]cnica M[aá]xima'):
    fora = [l for l in P20.split('\n')
            if re.search(velho, l) and not re.search(r'Ruptura|Ogi|Ōgi|renome|manual|Fundamento', l)]
    if fora:
        erro(7, f'`{velho}` aparece na peca 20 fora do contexto de renome: {fora[0][:70]}')
    else:
        print(f'  [x] `{velho}` so aparece como o nome que foi trocado')


# ============================================================ 8
bloco('8. A EXPANSAO DE DOMINIO NAO E ALCANCAVEL POR ESTA ROTA')

if not re.search(r'quem n[aã]o tem energia nunca tem Expans[aã]o', P9, re.I):
    erro(8, 'a peca 9 SS5 parou de negar a Expansao a quem nao tem energia')
else:
    print('  [x] a peca 9 SS5 continua negando, e ela e a dona')

if not re.search(r'\*\*n[aã]o existe nesta pe[cç]a\*\*', P20):
    erro(8, 'a peca 20 nao nega a Expansao na tabela do SS3')
elif not re.search(r'a Tecnica Marcial nao tem Expansao de Dominio', sa(P20)):
    erro(8, 'a peca 20 nega a Expansao so citando a peca 9, e aquela frase fala de quem '
            'NAO tem energia — o Corpo Amaldicoado TEM, entao ela nao alcanca ele')
else:
    print('  [x] a peca 20 nega por conta propria, e nao so pela Origem sem energia')

# o argumento velho nao pode continuar de pe em lugar nenhum, porque ele virou falso
velho_arg = r'n[aã]o tem lista de feiti[cç]o para gastar'
vivos = []
for rel, txt in (('09-origens.md', P9), ('11-aptidoes-e-refino.md', P11)):
    for i, l in enumerate(txt.split('\n'), 1):
        if re.search(velho_arg, l) and not re.search(r'v0\.12[2-9]|virou falso|deixou de|'
                                                     r'era verdade|hist[oó]ric', l):
            vivos.append(f'{rel}:{i}')
if vivos:
    erro(8, 'o argumento "esta rota nao tem lista de feitico para gastar" continua vivo em '
            + ', '.join(vivos) + ' — a peca 20 deu lista a ela, entao ele e falso agora')
else:
    print('  [x] o argumento antigo da negacao foi reescrito onde ele morava')


# ============================================================ 9
bloco('9. O `Desarmado` NAO PASSA DO FILTRO DE DOMINANCIA contra esta rota')

md = re.search(r'\|\s*\*\*`Desarmado`\*\*\s*\|\s*`([\d,]+)`\s*\|\s*`([\d,]+)`\s*\|\s*`(\w+)`', P19)
if not md:
    erro(9, 'nao consegui ler o `Desarmado` da peca 19')
else:
    des_dano, des_fatia, des_nivel = num(md.group(1)), num(md.group(2)), md.group(3)
    print(f'  `Desarmado` lido da peca 19: nivel {des_nivel} · {des_dano} de dano por '
          f'rodada · {des_fatia} fatia')
    # a Kata cheia da maior Classe, lida do proprio SS7 da peca 20 (que a le do manual)
    mk = re.search(r'\|\s*\*\*17 a 30\*\*\s*\|\s*\*\*5\*\*\s*\|\s*\*\*(\d+)\*\*', P20)
    if not mk:
        erro(9, 'nao achei a linha da maior Classe na tabela do SS7 da peca 20')
    else:
        kata = float(mk.group(1))
        razao = kata / des_dano
        print(f'  Kata cheia de Classe 5 = {kata:.0f} · razao contra o preco = {razao:.1f}x '
              f'· filtro {FILTRO_DOMINANCIA:.2f}x')
        if razao <= FILTRO_DOMINANCIA:
            erro(9, f'a razao caiu para {razao:.1f}x, abaixo do filtro — entao o SS7 deixou '
                    'de descrever um problema e a resposta dele virou decoracao')
        else:
            print(f'  [x] {razao:.1f}x reprova em {FILTRO_DOMINANCIA:.2f}x, e e por isso '
                  'que a rota precisa de mais de um grupo')

mg = re.search(r'Escolha (uma?|tr[eê]s|dois|quatro) das treze categorias', P20)
PAL = {'um': 1, 'uma': 1, 'dois': 2, 'tres': 3, 'quatro': 4}
n_gr = PAL.get(sa(mg.group(1))) if mg else None
if n_gr is None:
    erro(9, 'nao consegui ler quantos grupos a peca 20 SS4.1 entrega')
elif n_gr < GRUPOS_MINIMOS:
    erro(9, f'a peca 20 entrega {n_gr} grupo(s), e o minimo de design e {GRUPOS_MINIMOS}: '
            'com menos que isso o `Desarmado` apaga a ficha inteira')
else:
    print(f'  [x] a peca 20 entrega {n_gr} grupos, contra um minimo de {GRUPOS_MINIMOS}')

if not re.search(r'n[aã]o alcan[cç]a ele', P20):
    erro(9, 'a peca 20 nao diz que o `Desarmado` nao alcanca o objeto de apoio — sem isso '
            'a rota de ferramenta fica sem resposta nenhuma')
else:
    print('  [x] e a rota de ferramenta tem a resposta dela escrita')


# ============================================================ 10
bloco('10. FERIR MALDICAO CONTINUA SENDO DA FERRAMENTA')

if not re.search(r'ferramenta amaldi[cç]oada\*{0,2}\s*\|\s*\*{0,2}ferir maldi[cç][aã]o', P16):
    erro(10, 'a peca 16 SS2 parou de declarar que ferir maldicao e dela')
else:
    print('  [x] a peca 16 SS2 continua sendo a dona da porta')

if not re.search(r'grau 4', P20):
    erro(10, 'a peca 20 entrega equipamento sem dizer o grau, e o grau e o que decide '
             'se ele fere maldicao')
else:
    print('  [x] a peca 20 entrega grau 4, que e o degrau que fere e nao da Estigma')

# a peca 20 nao pode dar a porta sozinha, sem ferramenta no meio
if re.search(r'as suas Katas ferem maldi[cç][aã]o sem', P20):
    erro(10, 'a peca 20 concede ferir maldicao sem ferramenta — isso e da peca 16')
else:
    print('  [x] a peca 20 concede a porta pelo equipamento, e nunca sozinha')


# ============================================================ 11
bloco('11. O TETO DE `Estigma` NA FICHA NAO SE MOVEU')

mt16 = re.search(r'\|\s*\*\*teto declarado\*\*.*?\|\s*\*\*(\d+)\*\*\s*\|', P16)
if not mt16:
    erro(11, 'nao consegui ler o teto de Estigma da peca 16 SS5')
else:
    teto = int(mt16.group(1))
    print(f'  teto de `Estigma` na ficha, lido da peca 16 SS5: {teto}')
    _s41 = P20[P20.find('### 4.1'):P20.find('### 4.2')]
    if not re.search(r'teto de `Estigma` na ficha n[aã]o se move', _s41):
        erro(11, 'o SS4.1 entrega tres armas e nao declara, ali mesmo, que o teto de '
                 '`Estigma` nao se move — um mestre vai ler tres armas como tres Estigma')
    else:
        print('  [x] o SS4.1 declara o teto junto da entrega das tres armas')
    if not re.search(r'pelas m[aã]os e n[aã]o pela mochila', P20):
        erro(11, 'a peca 20 nao diz POR QUE o teto nao se move, e o motivo e o que '
                 'impede a leitura errada')
    else:
        print('  [x] e diz o motivo: o teto conta pelas maos, nao pela mochila')


# ============================================================ 12
bloco('12. TRIAGEM DE TODO NOME QUE A PECA CRIA')

CRIADOS = ['Kata', 'Ruptura', 'Ogi', 'Fisga', 'Bancada']
try:
    import subprocess
    out = subprocess.run([sys.executable, os.path.join(AQUI, 'conferir-nomes.py'),
                          '--candidatos'] + CRIADOS,
                         capture_output=True, text=True, timeout=180).stdout
    vered = {n: v for v, n in
             re.findall(r'^\s+(LIVRE|OCUPADO|DENTRO|MORTO|fraco)\s+(\S+)', out, re.M)}
    if not vered:
        pular(12, 'a triagem nao devolveu veredito nenhum (conferir-nomes.py pulou?)')
    # Depois de batizado, o proprio nome sai OCUPADO — como TERMO DE SISTEMA DO
    # PROJETO, que e' ele mesmo. O que reprova e' colidir com OUTRA coisa: com o
    # manual, com uma entrega de catalogo, com um Legado. Exigir LIVRE aqui daria
    # uma checagem que so passa ANTES do batismo, e que falha no dia seguinte.
    motivo = dict(re.findall(r'^\s+(?:OCUPADO|DENTRO)\s+(\S+)\s+(.*?)\s*$', out, re.M))
    for n in CRIADOS:
        v, m = vered.get(n, '?'), motivo.get(n, '')
        proprio = 'termo de sistema no projeto' in m
        if v == 'LIVRE':
            print(f'  [x] `{n}` sai LIVRE')
        elif v in ('OCUPADO', 'DENTRO') and proprio:
            print(f'  [x] `{n}` sai OCUPADO como ele mesmo — batizado e protegido')
        elif v in ('OCUPADO', 'DENTRO'):
            erro(12, f'`{n}` sai {v} por OUTRO motivo — {m} — e a peca 20 batiza assim mesmo')
        elif v == '?':
            aviso(f'a triagem nao respondeu sobre `{n}`')
        else:
            print(f'  [x] `{n}` sai {v}')
    # CONTRA-TESTE: se nenhum dos batizados estiver protegido, o vocabulario do
    # conferir-nomes.py nao recebeu esta peca e a triagem deixa rebatizar amanha.
    protegidos = sum(1 for n in ('Kata', 'Ruptura', 'Ogi')
                     if 'termo de sistema no projeto' in motivo.get(n, ''))
    if protegidos < 3:
        erro(12, f'so {protegidos} dos tres renomes estao no vocabulario do '
                 'conferir-nomes.py — os outros podem ser rebatizados sem ninguem acusar')
    else:
        print('  [x] os tres renomes estao protegidos contra rebatismo')
except Exception as e:
    pular(12, f'nao consegui rodar a triagem: {e}')



# ============================================================ 13
bloco('13. O `Bocado` NAO INVENTA O SAQUE DOBRADO — a peca 3 SS3.2 e a dona')

# A metade do saque desta Passiva nao e' numero desta peca: a peca 3 SS3.2 ja
# decidiu, na v0.122, que "uma Passiva ou aptidao pode dizer que o segundo saque
# sai de graca, e ela cabe na Classe Passiva 1". Esta checagem confere que as
# DUAS pontas continuam de acordo — a peca 3 permitindo e a peca 20 aplicando.
#
# Ela le o numero de itens dos DOIS lados em vez de guardar `2` aqui dentro:
# a peca 3 diz quantos saem de graca hoje (UM), e a peca 20 diz quantos o
# `Bocado` entrega (DOIS). O que se confere e' a RELACAO — o `Bocado` entrega
# exatamente um a mais que a regra de base, que e' o que "o segundo saque sai
# de graca" quer dizer. Perturbar qualquer um dos dois lados acende; mudar os
# dois de forma coerente fica verde, e e' assim que tem de ser.
_m_base = re.search(r'Sacar ou guardar (UM|DOIS|TRES) item', P3)
_m_pass = re.search(r'saca ou guarda \*{0,2}(UM|DOIS|TRES)\*{0,2} itens? de graça',
                    P20, re.I)
_m_perm = re.search(r'uma Passiva ou aptid[ãa]o pode dizer que o segundo saque sai de graça',
                    P3)
_PALAVRA = {'um': 1, 'dois': 2, 'tres': 3}

if not _m_base:
    pular(13, 'nao achei a regra de base de sacar na peca 3 SS3.2')
elif not _m_pass:
    erro(13, 'a peca 20 nao diz quantos itens o `Bocado` saca de graca por turno — '
             'a Passiva ficou sem a metade que a peca 3 SS3.2 preca')
elif not _m_perm:
    erro(13, 'a peca 3 SS3.2 nao permite mais que uma Passiva compre o segundo saque, '
             'e o `Bocado` da peca 20 continua comprando — as duas pecas discordam')
else:
    _base = _PALAVRA[sa(_m_base.group(1)).lower()]
    _pass = _PALAVRA[sa(_m_pass.group(1)).lower()]
    print(f'  peca 3 SS3.2: de graca por turno .. {_base}')
    print(f'  peca 20: o `Bocado` entrega ...... {_pass}')
    if _pass != _base + 1:
        erro(13, f'o `Bocado` entrega {_pass} saque(s) de graca e a base da peca 3 e '
                 f'{_base} — a peca 3 preca "o SEGUNDO saque", que e exatamente '
                 f'{_base + 1}, e nao {_pass}')
    else:
        print(f'  [x] o `Bocado` entrega um a mais que a base, que e o degrau que a '
              f'peca 3 SS3.2 preca em Classe Passiva 1.')


# ------------------------------------------------------------------ RODAPE
print('\n' + '=' * 88)
for a in avisos:
    print(f'  aviso: {a}')
if pulou:
    print('\n  ⚠ CHECAGENS QUE PULARAM — e um verde que pulou nao e um verde:')
    for p in pulou:
        print(f'    {p}')
if erros:
    print(f'\n>>> {len(erros)} PROBLEMA(S):')
    for e in erros:
        print(f'   - {e}')
    sys.exit(1)
print('>>> TUDO OK — o orcamento e herdado, a soma continua parelha, os tres grupos')
print('    nao entregam Manha, o atributo fecha os dois lados da rolagem, e o')
print('    `Desarmado` volta a valer o preco de tabela.')
if pulou:
    print(f'    OK, mas {len(pulou)} checagem(ns) PULARAM.')
print('=' * 88)

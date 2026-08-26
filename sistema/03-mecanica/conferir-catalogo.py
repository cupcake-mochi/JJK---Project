# -*- coding: utf-8 -*-
"""
conferir-catalogo.py — o validador da peca 17 (Catalogo de entregas).

A peca 17 e um INDICE: ela sabe quantas entradas existem, como cada uma se chama
e onde o texto dela mora. Ela nao guarda preco e nao guarda texto de mesa — os
dois sao dos DESENHO-*.md, que sao os donos.

Este validador e a primeira coisa do projeto que ALCANCA os DESENHO-*.md. Ate a
v0.84 nenhum lia aqueles arquivos, e foi por isso que o nivel 27 da Estocada
passou tres versoes com a tabela de preco dizendo "se o feitico acertou" e o
bloco de regra dizendo "carrega SEMPRE" — 1,33 fatia contra 5,31, numa Trilha
cujo orcamento inteiro e 5,00. A mesa le o bloco.

NADA DE VALOR FICA ESCRITO AQUI. Os nomes saem das tabelas da peca 17, os textos
saem dos DESENHO-*.md, e as contagens saem da propria pasta. O unico bloco com
valor na mao e o LIMITES DE DESIGN abaixo, declarado a parte da regra aplicada,
que e a licao no 8: uma checagem nao pode se medir contra a propria constante.

Doze checagens:
  1. TOTAIS    — a tabela de totais bate com o contado das tabelas de cima.
  2. SOMAS     — as duas somas do total fecham por caminhos diferentes.
  3. INDICE    — todo nome do indice existe no DESENHO dono dele.
  4. VOLTA     — todo nome batizado num degrau do DESENHO esta no indice.
  5. BLOCO     — toda entrega de Trilha com nome tem bloco de regra escrito.
  6. GATE      — bloco de regra nao contradiz o gate da linha de preco.
  7. CONTAGEM  — a pasta tem 23 pecas e 23 validadores.
  8. COPIAS    — todo documento que cita o total concorda com o contado.
  9. VALOR     — toda Classe que a linha de preco cobra aparece no bloco de regra.
 10. CALENDARIO — o degrau de Caminho publicado sai do DESENHO-caminhos.md, que
                  e o dono, e o calendario aposentado nao sobrou vivo.
 11. CAPITALIZACAO — todo nome batizado do indice comeca com maiuscula.
 12. PRECO     — toda entrega de Trilha tem fatia legivel, e o total do cabecalho
                 cai dentro do que as linhas somam.

Roda de sistema/03-mecanica/. NAO le o .docx e NAO precisa de python-docx —
entao nao existe caminho por onde ele saia verde tendo pulado checagem.
"""
import os, re, sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))

def ler(caminho):
    with open(caminho, encoding='utf-8') as f:
        return f.read()

# ---------------------------------------------------------------- LIMITES DE DESIGN
# Declarados aqui, a parte da regra aplicada. Sao FORMA e nao valor: os niveis em
# que uma Trilha entrega, e as palavras que denunciam a contradicao da Estocada.
# A regra aplicada le das tabelas; o limite esta aqui e nao la.
NIVEIS_DE_TRILHA = ['2', '11', '19', '27']
PALAVRA_DE_PERMANENCIA = 'sempre'
PALAVRAS_DE_GATE = ['quando', 'se o ', 'se a ', 'se voce', 'se você', 'condicional']
PECAS_ESPERADAS = 24   # 19 ate a v0.121; a peca 20 entrou na v0.122, a 21 na v0.132,
                       # a 22, Pactos, na v0.134, a 23, Bloquear, na v0.143, e a 24,
                       # Dano de alma e Integridade, na v0.145

PECA  = ler(os.path.join(AQUI, '17-catalogo-de-entregas.md'))
TRI   = ler(os.path.join(RAIZ, 'DESENHO-trilhas.md')).split('\n')
CAM   = ler(os.path.join(RAIZ, 'DESENHO-caminhos.md'))
MAN   = ler(os.path.join(RAIZ, 'DESENHO-manhas.md'))

erros, avisos = [], []
def erro(n, msg): erros.append(f'[{n}] {msg}')

print('=' * 88)
print('CONFERIR-CATALOGO — a peca 17 contra os tres DESENHO')
print('=' * 88)

# ================================================================ leitura do indice
def celulas(linha):
    return [c.strip() for c in linha.strip().strip('|').split('|')]

def desmarcar(s):
    return s.replace('*', '').strip()

def nomes_da_celula(cel):
    """Os nomes batizados de uma celula. Vazio se a celula e travessao ou vaga."""
    limpo = desmarcar(cel)
    if limpo in ('—', '-', '') or 'vaga' in limpo.lower():
        return []
    achados = re.findall(r'`([^`]+)`', cel)
    return achados if achados else [limpo]

def estado_da_celula(cel):
    limpo = desmarcar(cel).lower()
    if limpo in ('—', '-', ''): return 'sem nome'
    if 'vaga' in limpo:         return 'vaga'
    return 'com nome'

# secoes 3, 4 e 5 da peca
def fatia_da_peca(inicio, fim):
    a = PECA.find(inicio)
    b = PECA.find(fim) if fim else len(PECA)
    return PECA[a:b] if a >= 0 else ''

# Os ancoras sao o NUMERO DA SECAO e nao o titulo inteiro: a v0.147 acrescentou a
# `Versado` e o titulo virou "As 14 Manhas". Com o titulo antigo escrito aqui, as
# duas fatias vizinhas se abriram uma dentro da outra e o extrator devolveu 24
# degraus e 0 Manhas — numeros que nao existem, vindos de ancora vencida e nao de
# conteudo errado. Contagem no ancora e a licao no 9 pela porta do parser.
S3 = fatia_da_peca('## 3. As ', '## 4. Os ')
S4 = fatia_da_peca('## 4. Os ', '## 5. As ')
S5 = fatia_da_peca('## 5. As ', '## 6. Os totais')
S6 = fatia_da_peca('## 6. Os totais', '## 7. O que')

def linhas_de_catalogo(secao):
    """Linhas de tabela cujo primeiro campo e um dono em negrito, com 5 campos."""
    saida = []
    for l in secao.split('\n'):
        if not l.startswith('|'): continue
        c = celulas(l)
        if len(c) != 5: continue
        if not c[0].startswith('**'): continue
        if set(desmarcar(c[0])) <= set('-: '): continue
        saida.append(c)
    return saida

TRILHAS_IDX, CAMINHOS_IDX = linhas_de_catalogo(S3), linhas_de_catalogo(S4)
MANHAS_IDX = []
for l in S5.split('\n'):
    if l.count('`') >= 20:
        MANHAS_IDX = re.findall(r'`([^`]+)`', l); break

n_trilha  = len(TRILHAS_IDX) * 4
n_caminho = len(CAMINHOS_IDX) * 4
n_manha   = len(MANHAS_IDX)

estados = []
for c in TRILHAS_IDX + CAMINHOS_IDX:
    estados += [estado_da_celula(x) for x in c[1:]]
com_nome  = estados.count('com nome') + n_manha
sem_nome  = estados.count('sem nome')
vagas     = estados.count('vaga')
total     = n_trilha + n_caminho + n_manha

# ================================================================ 1. TOTAIS
print('\n' + '=' * 88)
print('1. TOTAIS — a tabela de totais contra o contado das tabelas de cima')
print('=' * 88)
print(f'  contado: Trilha {n_trilha} · Caminho {n_caminho} · Manha {n_manha} = {total}')
print(f'           com nome {com_nome} · sem nome {sem_nome} · vaga {vagas}')

def linha_de_total(rotulo):
    for l in S6.split('\n'):
        if not l.startswith('|'): continue
        c = celulas(l)
        if c and rotulo in desmarcar(c[0]).lower():
            return [desmarcar(x) for x in c]
    return None

esperado = {
    'entregas de trilha': (n_trilha, ),
    'degraus de caminho': (n_caminho, ),
    'manhas':             (n_manha, ),
}
ok1 = True
for rot, (qtd, ) in esperado.items():
    lin = linha_de_total(rot)
    if not lin:
        erro('1', f'nao achei a linha de total de "{rot}"'); ok1 = False; continue
    try: escrito = int(re.sub(r'\D', '', lin[1]))
    except ValueError:
        erro('1', f'o total de "{rot}" nao e numero'); ok1 = False; continue
    if escrito != qtd:
        erro('1', f'"{rot}": a tabela diz {escrito} e a pasta tem {qtd}'); ok1 = False

lin_tot = linha_de_total('total')
if not lin_tot:
    erro('1', 'nao achei a linha "total" da tabela de totais'); ok1 = False
else:
    nums = [int(re.sub(r'\D', '', x)) for x in lin_tot[1:5]]
    if nums != [total, com_nome, sem_nome, vagas]:
        erro('1', f'a linha total diz {nums} e o contado e {[total, com_nome, sem_nome, vagas]}')
        ok1 = False
if ok1:
    print('  [x] todo total escrito foi recontado da propria peca. Nenhum foi digitado a mao.')

# ================================================================ 2. SOMAS
print('\n' + '=' * 88)
print('2. SOMAS — o total fecha por dois caminhos diferentes')
print('=' * 88)
por_familia = n_trilha + n_caminho + n_manha
por_estado  = com_nome + sem_nome + vagas
print(f'  por familia: {n_trilha} + {n_caminho} + {n_manha} = {por_familia}')
print(f'  por estado : {com_nome} + {sem_nome} + {vagas} = {por_estado}')
if por_familia != por_estado:
    erro('2', f'as duas somas discordam: {por_familia} contra {por_estado}')
else:
    print('  [x] as duas fecham no mesmo numero. Uma entrada sem estado nao passa por aqui.')

# ================================================================ 3. INDICE -> DESENHO
print('\n' + '=' * 88)
print('3. INDICE — todo nome do indice existe no DESENHO dono dele')
print('=' * 88)
TEXTO_TRI = '\n'.join(TRI)
alvos = []
for c in TRILHAS_IDX:
    for cel in c[1:]: alvos += [(n, 'DESENHO-trilhas.md',  TEXTO_TRI) for n in nomes_da_celula(cel)]
for c in CAMINHOS_IDX:
    for cel in c[1:]: alvos += [(n, 'DESENHO-caminhos.md', CAM) for n in nomes_da_celula(cel)]
for n in MANHAS_IDX:  alvos.append((n, 'DESENHO-manhas.md', MAN))
faltando = [(n, arq) for (n, arq, txt) in alvos if n not in txt]
print(f'  {len(alvos)} nomes no indice, conferidos contra os tres arquivos')
for n, arq in faltando:
    erro('3', f'o nome `{n}` esta no indice e nao aparece em {arq}')
if not faltando:
    print('  [x] nenhum nome do indice esta orfao. Renomear de um lado so falha aqui.')

# ================================================================ secoes do DESENHO
CABECA = [(i, len(m.group(1)), m.group(2))
          for i, l in enumerate(TRI) if (m := re.match(r'^(#+)\s+(.*)$', l))]

def tem_tabela_de_preco(ln):
    for j in range(ln + 1, min(ln + 16, len(TRI))):
        if re.match(r'^\|\s*nv\s*\|', TRI[j], re.I) and 'fatias' in TRI[j].lower():
            for k in range(j + 1, min(j + 4, len(TRI))):
                if re.match(r'^\|\s*\*\*2\*\*\s*\|', TRI[k]): return True
    return False

donos = []
for c in TRILHAS_IDX:
    rotulo = desmarcar(c[0])
    donos.append((rotulo, re.findall(r'`([^`]+)`', c[0])[-1]))

comeco = {}
for rotulo, chave in donos:
    cands = sorted((lv, ln) for (ln, lv, t) in CABECA if chave in t and tem_tabela_de_preco(ln))
    if cands: comeco[rotulo] = (cands[0][1], cands[0][0])

ordem = sorted(comeco.items(), key=lambda kv: kv[1][0])
SECAO = {}
for i, (rotulo, (ln, lv)) in enumerate(ordem):
    fim = ordem[i + 1][1][0] if i + 1 < len(ordem) else len(TRI)
    for (ln2, lv2, _) in CABECA:
        if ln2 > ln and lv2 <= lv: fim = min(fim, ln2); break
    SECAO[rotulo] = (ln, fim)

for rotulo, _ in donos:
    if rotulo not in SECAO:
        erro('3', f'nao achei a secao mecanica de {rotulo} no DESENHO-trilhas.md')

# ================================================================ 4. VOLTA
print('\n' + '=' * 88)
print('4. VOLTA — todo nome batizado num degrau do DESENHO esta no indice')
print('=' * 88)
no_indice = {n for c in TRILHAS_IDX for cel in c[1:] for n in nomes_da_celula(cel)}
achados, sobrando = 0, []
for rotulo, (a, b) in SECAO.items():
    for l in TRI[a:b]:
        if not re.match(r'^\|\s*\*\*(2|11|19|27)\*\*\s*\|', l): continue
        # so o PRIMEIRO nome em negrito+crase e a coluna de nome; o resto da
        # linha carrega numero e unidade no mesmo formato (`9 m`, `+1`, `a Classe`)
        m_nome = re.search(r'\*\*`([^`]+)`\*\*', l)
        if not m_nome: continue
        nome = m_nome.group(1)
        achados += 1
        if nome not in no_indice: sobrando.append((rotulo, nome))
print(f'  {achados} nomes batizados em linha de preco, conferidos contra o indice')
for rotulo, nome in sobrando:
    erro('4', f'`{nome}` esta batizado em {rotulo} e nao aparece no indice da peca 17')
if not sobrando:
    print('  [x] nenhuma entrega batizada ficou fora do indice.')

# ================================================================ 5. BLOCO / 6. GATE
print('\n' + '=' * 88)
print('5. BLOCO — toda entrega de Trilha com nome tem bloco de regra escrito')
print('=' * 88)
precos, blocos = {}, {}
for rotulo, (a, b) in SECAO.items():
    for l in TRI[a:b]:
        m = re.match(r'^\|\s*\*\*(2|11|19|27)\*\*\s*\|', l)
        if m and (rotulo, m.group(1)) not in precos: precos[(rotulo, m.group(1))] = l
        m2 = re.match(r'^>\s*\*\*N[íi]vel\s+(2|11|19|27)\b', l)
        if m2 and (rotulo, m2.group(1)) not in blocos: blocos[(rotulo, m2.group(1))] = l

nomeadas = []
for c in TRILHAS_IDX:
    rotulo = desmarcar(c[0])
    for i, cel in enumerate(c[1:]):
        if estado_da_celula(cel) == 'com nome': nomeadas.append((rotulo, NIVEIS_DE_TRILHA[i]))
sem_bloco = [k for k in nomeadas if k not in blocos]
print(f'  {len(nomeadas)} entregas com nome, {len(blocos)} blocos de regra achados')
for rotulo, nv in sem_bloco:
    erro('5', f'{rotulo} nivel {nv} tem nome e nao tem bloco de regra')
if not sem_bloco:
    print('  [x] toda entrega batizada tem texto que o mestre le na mesa.')

print('\n' + '=' * 88)
print('6. GATE — o bloco de regra nao contradiz o gate da linha de preco')
print('=' * 88)
print('  Esta e a checagem que a Estocada nv27 custou: a linha de preco dizia')
print('  "se o feitico acertou" e o bloco dizia "carrega SEMPRE".')
conferidos, contradizem = 0, []
for chave, linha_preco in precos.items():
    bloco = blocos.get(chave)
    if not bloco: continue
    conferidos += 1
    preco_tem_gate = any(p in linha_preco.lower() for p in PALAVRAS_DE_GATE)
    bloco_diz_sempre = PALAVRA_DE_PERMANENCIA in bloco.lower()
    if preco_tem_gate and bloco_diz_sempre:
        contradizem.append(chave)
print(f'  {conferidos} pares (linha de preco, bloco de regra) conferidos')
for rotulo, nv in contradizem:
    erro('6', f'{rotulo} nivel {nv}: a linha de preco declara gate e o bloco diz "sempre"')
if not contradizem:
    print('  [x] nenhum bloco promete permanencia onde o preco cobrou condicao.')

# ================================================================ 7. CONTAGEM
print('\n' + '=' * 88)
print(f'7. CONTAGEM — a pasta tem {PECAS_ESPERADAS} pecas e {PECAS_ESPERADAS} validadores')
print('=' * 88)
pecas = sorted(f for f in os.listdir(AQUI) if re.match(r'^\d\d-.*\.md$', f))
vals  = sorted(f for f in os.listdir(AQUI) if re.match(r'^conferir-.*\.py$', f))
print(f'  pecas na pasta      : {len(pecas)}')
print(f'  validadores na pasta: {len(vals)}')
if len(pecas) != PECAS_ESPERADAS:
    erro('7', f'a pasta tem {len(pecas)} pecas e o limite de design diz {PECAS_ESPERADAS}')
if len(vals) != PECAS_ESPERADAS:
    erro('7', f'a pasta tem {len(vals)} validadores e o limite de design diz {PECAS_ESPERADAS}')
if len(pecas) == len(vals) == PECAS_ESPERADAS:
    print('  [x] peca e validador andam em par, e o par bate com o numero declarado.')

# ================================================================ 8. COPIAS
print('\n' + '=' * 88)
print('8. COPIAS — todo documento que cita o total concorda com o contado')
print('=' * 88)
print('  A peca 17 e a DONA de "quantas entradas existem". Todo outro documento')
print('  que repete o numero e copia, e copia sem dono vira a licao no 9.')

# Os documentos VIVOS que repetem o total. O CHANGELOG fica de fora de
# proposito: ele e registro historico e diz o que se pensou naquele dia — a
# entrada da v0.84 tem de continuar dizendo 81 sem falhar nada.
DERIVADOS = [
    'README.md',
    os.path.join('sistema', 'ESTADO-ATUAL.md'),
    os.path.join('sistema', 'LEIA-ME.md'),
    os.path.join('finalizado', 'README.md'),
]
# A frase e estreita de proposito. "NN entradas" solto pega o catalogo de 19 da
# peca 15 e o de 81 da peca 13, que sao outros catalogos e outros numeros —
# a checagem tem de achar a copia DESTE total, e nao qualquer numero parecido.
FRASE = r'[íi]ndice d(?:as|e)\s+\**`?(\d+)`?\**\s+entradas'

conferidas, divergiram, sem_citacao = 0, [], []
for rel in DERIVADOS:
    caminho = os.path.join(RAIZ, rel)
    if not os.path.isfile(caminho): continue
    doc = ler(caminho)
    achou = False
    for m in re.finditer(FRASE, doc):
        conferidas += 1; achou = True
        if int(m.group(1)) != total:
            divergiram.append((rel, m.group(1)))
    if not achou: sem_citacao.append(rel)
print(f'  {conferidas} citacoes de "indice das NN entradas" conferidas contra o dono')
for rel in sem_citacao:
    avisos.append(f'{rel} nao cita o total do catalogo — nada a conferir ali')
for rel, achado in divergiram:
    erro('8', f'{rel} diz "indice das {achado} entradas" e o contado e {total}')
if not divergiram:
    print(f'  [x] as {conferidas} copias do total dizem {total}, que e o que a pasta tem.')

# ================================================================ 9. VALOR
print('\n' + '=' * 88)
print('9. VALOR — toda Classe que a linha de preco cobra aparece no bloco de regra')
print('=' * 88)
print('  A checagem 6 pega gate contra "sempre". Esta pega VALOR contra valor, que')
print('  foi o que deixou o nivel 19 da Brasa publicar Classe 2 por tres versoes')
print('  enquanto a tabela e o argumento diziam Classe 3, e Classe 4 do nivel 21.')

def classes_de(texto):
    return set(int(x) for x in re.findall(r'Classe\s+(\d)', texto))

def bloco_inteiro(a, b, inicio):
    """Do '> **Nivel N' ate o proximo, sem as notas em italico, que sao historia."""
    corpo = []
    for j in range(inicio, b):
        if j > inicio and re.match(r'^>\s*\*\*N[íi]vel\s', TRI[j]): break
        if not TRI[j].startswith('>'): break
        if re.match(r'^>\s*\*[^*]', TRI[j]): continue
        corpo.append(TRI[j])
    return '\n'.join(corpo)

inteiros = {}
for rotulo, (a, b) in SECAO.items():
    vistos = set()
    for i in range(a, b):
        m = re.match(r'^>\s*\*\*N[íi]vel\s+(2|11|19|27)\b', TRI[i])
        if m and m.group(1) not in vistos:
            vistos.add(m.group(1))
            inteiros[(rotulo, m.group(1))] = bloco_inteiro(a, b, i)

pares, faltando = 0, []
for chave, linha_preco in precos.items():
    corpo = inteiros.get(chave)
    if corpo is None: continue
    pares += 1
    falta = classes_de(linha_preco) - classes_de(corpo)
    if falta: faltando.append((chave, sorted(falta)))
print(f'  {pares} pares conferidos, na direcao preco -> bloco')
print('  (o bloco PODE citar Classe a mais: exemplo de custo nao e promessa)')
for (rotulo, nv), falta in faltando:
    erro('9', f'{rotulo} nivel {nv}: o preco cobra Classe {falta} e o bloco nao entrega')
if not faltando:
    print('  [x] nenhum bloco entrega Classe menor do que a que foi paga.')

# ================================================================ 10. CALENDARIO
print()
print('=' * 88)
print('10. CALENDARIO — o degrau de Caminho publicado sai do dono')
print('=' * 88)

# O dono do calendario e o DESENHO-caminhos.md. A peca 6 e a peca 17 sao copia,
# e a copia da peca 6 passou DEZOITO versoes publicando o calendario aposentado
# como fato fechado — de v0.70 ate v0.88. Nenhum validador alcancava.
#
# Duas checagens por EIXOS DIFERENTES, que e a regra do arnes desde a v0.63:
#   10a pergunta "o que esta publicado bate com o dono?"
#   10b pergunta "o valor morto sumiu?"
# Reescrever a frase sem o numero apaga a 10a e deixa a 10b; trocar o numero
# sem mexer na frase acende a 10a. Uma checagem so cobriria metade.
import glob as _glob

_m = re.search(r'\*\*Or[cç]amento:\*\*\s*Caminho em `([^`]+)`', CAM)
CAL_DONO = _m.group(1).strip() if _m else None
if CAL_DONO is None:
    erro('10', 'nao achei a linha de orcamento do DESENHO-caminhos.md — o dono do '
               'calendario de Caminho sumiu e esta checagem parou de conferir')
else:
    print(f'  dono: DESENHO-caminhos.md diz `{CAL_DONO}`')

# O calendario que MORREU na v0.70. Fica escrito aqui de proposito, no molde da
# checagem 4g do conferir-manual.py: guardar so o valor VIVO nao pega a copia
# velha que nao usa a mesma frase.
CAL_MORTO = '7 · 15 · 23 · 29'

# Quantas copias vivas existem. Se cair, alguem reescreveu a frase e a 10a
# parou de conferir em silencio — que e o modo de falha da licao no 8.
COPIAS_ESPERADAS = 3

PUB = re.compile(r'[Cc]aminhos?[^`\n]{0,45}?(?:em|para) `(\d+(?: · \d+){3})`')
HIST = re.compile(r'(at[ée] a v0|era `|foi `|superad|antigo|mudou na v0|antes da v0|contra o)')

VIVOS = sorted(_glob.glob(os.path.join(AQUI, '[0-9][0-9]-*.md')))
VIVOS += [os.path.join(RAIZ, 'ESTADO-ATUAL.md'),
          os.path.join(RAIZ, '..', 'README.md'),
          os.path.join(RAIZ, 'LEIA-ME.md'),
          os.path.join(RAIZ, '..', 'DESENHO-trilhas.md'),
          os.path.join(RAIZ, '..', 'DESENHO-manhas.md')]

def _hist(l):
    return l.lstrip().startswith('>') or '~~' in l or bool(HIST.search(l))

copias = 0
for _cam in VIVOS:
    if not os.path.exists(_cam):
        continue
    _rel = os.path.basename(_cam)
    for _i, _l in enumerate(ler(_cam).split('\n'), 1):
        if CAL_DONO:
            for _pub in PUB.findall(_l):
                copias += 1
                if _pub.strip() != CAL_DONO:
                    erro('10', f'{_rel}:{_i} publica o degrau de Caminho em `{_pub}` e o '
                               f'dono (DESENHO-caminhos.md) diz `{CAL_DONO}`')
        if CAL_MORTO in _l and not _hist(_l):
            erro('10', f'{_rel}:{_i} carrega o calendario aposentado `{CAL_MORTO}` '
                       f'fora de nota historica')

print(f'  {copias} copia(s) viva(s) do calendario conferida(s) contra o dono')
if copias < COPIAS_ESPERADAS:
    erro('10', f'so {copias} copia(s) do calendario de Caminho foram encontradas e '
               f'eram {COPIAS_ESPERADAS} — alguem reescreveu a frase e a 10a esta '
               f'conferindo menos do que conferia')
if not [e for e in erros if e.startswith('[10]')]:
    print('  [x] toda copia viva bate com o dono, e o calendario aposentado nao sobrou.')


# ================================================================ 11. CAPITALIZACAO
print('\n' + '=' * 88)
print('11. CAPITALIZACAO — todo nome batizado do indice comeca com maiuscula')
print('=' * 88)

_conf, _minusculos = 0, []
for _c in TRILHAS_IDX + CAMINHOS_IDX:
    _dono = desmarcar(_c[0])
    for _cel in _c[1:]:
        for _n in nomes_da_celula(_cel):
            _n = _n.strip()
            if not _n or not _n[0].isalpha():
                continue
            _conf += 1
            if _n[0].islower():
                _minusculos.append(f'{_dono} -> `{_n}`')
for _n in MANHAS_IDX:
    _n = _n.strip()
    if _n and _n[0].isalpha():
        _conf += 1
        if _n[0].islower():
            _minusculos.append(f'Manha -> `{_n}`')

print(f'  {_conf} nome(s) batizado(s) em {com_nome} celula(s) com nome '
      f'(uma celula de Caminho carrega duas entregas, por isso {_conf} > {com_nome})')
for _m in _minusculos:
    erro('11', f'nome de entrega em minuscula, e o indice capitaliza todos os outros: {_m}')
if _conf < com_nome:
    erro('11', f'so {_conf} nome(s) chegaram ao extrator e a peca conta {com_nome} com '
               f'nome — a 11a esta conferindo menos do que existe, em vez de acusar')
if not [e for e in erros if e.startswith('[11]')]:
    print('  [x] nenhuma das entradas batizadas do indice tem nome em minuscula.')

# ================================================================ 12. PRECO
# Nasceu na v0.131, e ela e a licao no 9 numa direcao que nenhuma outra alcanca
# neste validador: aqui o buraco nao era um numero divergindo de outro, era um
# numero que NAO EXISTIA. A linha do nivel 2 da Torrente publicava `(a base)` na
# coluna de fatias — texto onde as outras 59 linhas tem numero — e com isso uma
# entrega de 2,87 fatias ficou cinquenta versoes fora da conta da Trilha dela.
#
# O `(a base)` aparecia UMA vez no arquivo inteiro. Uma celula que nao le como
# numero e o unico jeito de uma entrega escapar do total sem que nada acuse:
# somar quatro linhas e comparar com o cabecalho da verde, porque a linha muda
# nao entra em nenhum dos dois lados.
#
# 12.1 — toda linha de preco tem fatia legivel como numero.
# 12.2 — o total do cabecalho cai dentro da faixa que as linhas somam.
#
# Zero declarado NAO reprova: `0,00` e um preco, e o nivel 27 do Arremate esta
# vago com `0,00` de proposito. O que reprova e a AUSENCIA de preco.
print('\n' + '=' * 88)
print('12. PRECO — toda entrega de Trilha tem fatia legivel, e o total bate com as linhas')
print('=' * 88)

# LIMITE DE DESIGN, declarado a parte da regra aplicada (licao no 8):
# a tolerancia existe porque o documento arredonda cada linha em centavo, entao
# quatro linhas podem somar 0,01 longe do total. Ela nao e a regra; a regra le.
TOL_POR_LINHA = 0.02

def _fatias_da_celula(cel):
    """Os numeros de fatia de uma celula. Faixa `a a b` volta com os dois."""
    limpo = re.sub(r'[*`]', '', cel)
    return [float(x.replace(',', '.')) for x in re.findall(r'\d+,\d{2}', limpo)]

def _coluna_de_fatias(linha_cab):
    cels = [c.strip().lower() for c in linha_cab.strip().strip('|').split('|')]
    for i, c in enumerate(cels):
        if c == 'fatias':
            return i
    return None

_lidas, _sem_preco, _totais_conferidos, _fora = 0, [], 0, []
for _rot, (_a, _b) in sorted(SECAO.items(), key=lambda kv: kv[1][0]):
    _cab_i = None
    for _j in range(_a, _b):
        if re.match(r'^\|\s*nv\s*\|', TRI[_j], re.I) and 'fatias' in TRI[_j].lower():
            _cab_i = _j
            break
    if _cab_i is None:
        continue
    # _col nunca volta None aqui: o SECAO so guarda secao cuja tabela ja tem
    # `fatias` no cabecalho. Renomear essa coluna faz a Trilha SUMIR do SECAO, e
    # quem acusa isso e a checagem 3 — conferido no arnes da v0.131.
    _col = _coluna_de_fatias(TRI[_cab_i])
    _lo, _hi, _linhas = 0.0, 0.0, 0
    for _k in range(_cab_i + 1, _b):
        if not re.match(r'^\|\s*\*\*(2|11|19|27)\*\*\s*\|', TRI[_k]):
            if _linhas and not TRI[_k].startswith('|'):
                break
            continue
        _cels = [c.strip() for c in TRI[_k].strip().strip('|').split('|')]
        if _col >= len(_cels):
            erro('12', f'{_rot}: linha de preco com menos colunas que o cabecalho: '
                       f'{TRI[_k].strip()[:70]}')
            continue
        _lidas += 1
        _linhas += 1
        _vals = _fatias_da_celula(_cels[_col])
        if not _vals:
            _sem_preco.append((_rot, TRI[_k].strip()[:80], _cels[_col]))
            continue
        _lo += min(_vals)
        _hi += max(_vals)
    # 12.2 — o total do cabecalho, quando ele publica um
    _mt = re.search(r'((?:\d+,\d{2}(?:\s+a\s+)?)+)[`\s*]*de[`\s*]*\s*\d+,\d{2}',
                    re.sub(r'[`*]', '', TRI[_a]))
    if _mt and _linhas:
        _pub = [float(x.replace(',', '.')) for x in re.findall(r'\d+,\d{2}', _mt.group(1))]
        _tol = TOL_POR_LINHA * _linhas
        for _p in _pub:
            _totais_conferidos += 1
            if not (_lo - _tol <= _p <= _hi + _tol):
                _fora.append((_rot, _p, _lo, _hi))

print(f'  {_lidas} linha(s) de preco lida(s) em {len(SECAO)} Trilha(s); '
      f'{_totais_conferidos} total(is) de cabecalho recontado(s)')

for _rot, _linha, _cel in _sem_preco:
    erro('12', f'{_rot}: a coluna de fatias diz "{_cel}" e nao tem numero — uma entrega '
               f'sem preco nao entra no total da Trilha, e nada mais acusa isso\n'
               f'       {_linha}')
for _rot, _p, _lo, _hi in _fora:
    _faixa = f'{_lo:.2f}' if abs(_hi - _lo) < 0.005 else f'{_lo:.2f} a {_hi:.2f}'
    erro('12', f'{_rot}: o cabecalho publica {_p:.2f} e as linhas somam {_faixa}')

# guarda: se o extrator parar de casar, esta checagem fica verde de graca. O piso
# e derivado — quatro linhas por Trilha achada —, e nao um numero escrito aqui.
_PISO12 = 4 * len(SECAO)
if _lidas < _PISO12:
    erro('12', f'so li {_lidas} linha(s) de preco e as {len(SECAO)} Trilhas achadas dao '
               f'{_PISO12} — o extrator parou de casar, e a checagem passou a conferir '
               f'menos do que existe em vez de acusar')
if not [e for e in erros if e.startswith('[12]')]:
    print('  [x] nenhuma entrega de Trilha esta sem preco, e todo total de cabecalho')
    print('      recontado cai dentro do que as linhas dele somam.')

# ================================================================ 13
# v0.154: a BANDA das Manhas. O catalogo delas tem preco por entrada e um
# filtro de dominancia declarado, e ate aqui nada comparava os dois — a leva
# daquela versao mexeu em cinco entradas e tres delas mudaram de preco.
#
# Nenhum numero mora aqui: as fatias saem da tabela do DESENHO-manhas.md, o
# filtro sai da frase que o declara, e a banda publicada sai da linha que a
# publica. A checagem so' compara.
print()
print('=' * 88)
print('13. A BANDA DAS MANHAS — o catalogo contra o filtro de dominancia')
print('=' * 88)

_fatias = {}
for _l in MAN.split('\n'):
    _m = re.match(r'\|\s*\*\*[^|]+\*\*\s*\|\s*`([^`]+)`\s*\|.*\|\s*\*\*(\d+,\d+)\*\*\s*\|\s*$', _l)
    if _m:
        _fatias[_m.group(1)] = float(_m.group(2).replace(',', '.'))

_filtro = re.search(r'o filtro do projeto reprova em `(\d+,\d+)×`', MAN)
_pub = re.search(r'A menor é [^.]*?em `(\d+,\d+)`, a maior é [^.]*?em `(\d+,\d+)`', MAN)
_pubdom = re.search(r'Dominância entre a maior e a menor: `(\d+,\d+)×`', MAN)

if len(_fatias) < 10:
    erro('13', f'so li {len(_fatias)} preco(s) na tabela do DESENHO-manhas.md — o '
               f'extrator parou de casar e a banda passou a ser medida sobre um '
               f'pedaco do catalogo')
elif not (_filtro and _pub and _pubdom):
    erro('13', 'o DESENHO-manhas.md nao publica a banda, a dominancia ou o filtro — '
               'sem os tres esta checagem nao tem contra o que comparar')
else:
    _lo, _hi = min(_fatias.values()), max(_fatias.values())
    _dom = _hi / _lo
    _f = float(_filtro.group(1).replace(',', '.'))
    _plo = float(_pub.group(1).replace(',', '.'))
    _phi = float(_pub.group(2).replace(',', '.'))
    _pd = float(_pubdom.group(1).replace(',', '.'))
    print(f'  {len(_fatias)} Manhas com preco; banda medida {_lo:.2f} a {_hi:.2f}, '
          f'dominancia {_dom:.2f}x')
    print(f'  o documento publica {_plo:.2f} a {_phi:.2f}, dominancia {_pd:.2f}x, '
          f'filtro {_f:.2f}x')
    if abs(_lo - _plo) > 0.005 or abs(_hi - _phi) > 0.005:
        erro('13', f'a banda publicada e {_plo:.2f}-{_phi:.2f} e a tabela da '
                   f'{_lo:.2f}-{_hi:.2f} — o texto e a tabela divergiram')
    elif abs(_dom - _pd) > 0.01:
        erro('13', f'a dominancia publicada e {_pd:.2f}x e a recontada da {_dom:.2f}x')
    elif _dom >= _f:
        erro('13', f'a dominancia das Manhas e {_dom:.2f}x e o filtro reprova em '
                   f'{_f:.2f}x — o catalogo saiu da banda')
    else:
        print('  [x] a banda recontada bate com a publicada, e ela passa no filtro.')

# --- 13.1 --------------------------------------------------------------
# v0.158: a MESMA banda no mundo de UM ataque por rodada. A Vanguarda tem um
# golpe do nivel 2 ao 6 — o ataque extra e' o degrau de Caminho do nivel 7 —,
# e as Manhas foram todas precadas supondo dois.
#
# A v0.154 registrou isso em prosa e nomeou quatro entradas de cabeca. Medida
# entrada por entrada na v0.158, a lista estava errada em dois pontos e faltavam
# duas. O conserto nao foi de preco: foi dar DONO ao numero, no molde da tabela
# de derivacao das travas da checagem 14.
#
# Nada aqui esta escrito neste arquivo: a tabela `Com um ataque por rodada` do
# DESENHO-manhas diz quem escala e quanto vale, e a banda daquele mundo e'
# RECONTADA dela. O filtro e' o mesmo da 13, lido do documento, e comparado
# DEPOIS da reconta — regra aplicada e limite de design separados (licao no 8).
print()
print('  13.1 a mesma banda com UM ataque por rodada — os niveis 2 a 6')

_um = {}
_escala = {}
for _l in MAN.split('\n'):
    _m = re.match(r'\|\s*`([^`]+)`\s*\|\s*(sim|não)\s*\|\s*`(\d+,\d+)`\s*\|\s*$', _l)
    if _m:
        _um[_m.group(1)] = float(_m.group(3).replace(',', '.'))
        _escala[_m.group(1)] = _m.group(2) == 'sim'

_pub1 = re.search(r'A banda daquele mundo é `(\d+,\d+)`–`(\d+,\d+)`, a dominância é '
                  r'`(\d+,\d+)×` e a média é `(\d+,\d+)`', MAN)

if not _fatias or len(_fatias) < 10:
    erro('13', '13.1: sem a tabela de precos da 13 nao ha contra o que comparar o '
               'mundo de um ataque')
elif len(_um) != len(_fatias):
    erro('13', f'13.1: a tabela `Com um ataque por rodada` tem {len(_um)} linha(s) e o '
               f'catalogo tem {len(_fatias)} Manha(s) — Manha nova sem essa linha faz '
               'a banda daquele mundo ser medida sobre um pedaco do catalogo')
elif sorted(_um) != sorted(_fatias):
    _fora = sorted(set(_um) ^ set(_fatias))
    erro('13', f'13.1: os nomes das duas tabelas nao batem — {_fora}')
elif not _pub1:
    erro('13', '13.1: o DESENHO-manhas nao publica mais a banda, a dominancia e a '
               'media do mundo de um ataque — sem elas a reconta nao tem par')
else:
    # coerencia da propria declaracao: quem NAO escala tem de valer o mesmo preco
    _incoerente = [n for n in _um
                   if not _escala[n] and abs(_um[n] - _fatias[n]) > 0.005]
    _parada = [n for n in _um if _escala[n] and abs(_um[n] - _fatias[n]) <= 0.005]
    _lo1, _hi1 = min(_um.values()), max(_um.values())
    _dom1 = _hi1 / _lo1
    _med1 = sum(_um.values()) / len(_um)
    _plo1 = float(_pub1.group(1).replace(',', '.'))
    _phi1 = float(_pub1.group(2).replace(',', '.'))
    _pd1 = float(_pub1.group(3).replace(',', '.'))
    _pm1 = float(_pub1.group(4).replace(',', '.'))
    print(f'       {len(_um)} Manhas declaradas; {sum(_escala.values())} escalam com o '
          f'numero de golpes')
    print(f'       banda recontada {_lo1:.2f} a {_hi1:.2f}, dominancia {_dom1:.2f}x, '
          f'media {_med1:.2f}')
    if _incoerente:
        erro('13', f'13.1: {_incoerente} esta(o) declarada(s) como NAO escalando e o '
                   'valor com um golpe difere do preco do catalogo — a declaracao '
                   'contradiz a propria tabela')
    elif _parada:
        erro('13', f'13.1: {_parada} esta(o) declarada(s) como escalando e o valor com '
                   'um golpe e igual ao do catalogo — ou ela nao escala, ou o numero '
                   'ficou para tras')
    elif (abs(_lo1 - _plo1) > 0.005 or abs(_hi1 - _phi1) > 0.005
          or abs(_dom1 - _pd1) > 0.01 or abs(_med1 - _pm1) > 0.005):
        erro('13', f'13.1: o documento publica {_plo1:.2f}-{_phi1:.2f}, {_pd1:.2f}x e '
                   f'media {_pm1:.2f} para o mundo de um ataque, e a tabela reconta '
                   f'{_lo1:.2f}-{_hi1:.2f}, {_dom1:.2f}x e {_med1:.2f}')
    elif _dom1 >= _f:
        erro('13', f'13.1: com um ataque a dominancia e {_dom1:.2f}x e o filtro reprova '
                   f'em {_f:.2f}x — o catalogo sai da banda nos niveis 2 a 6, que e '
                   'exatamente onde a Vanguarda comeca')
    else:
        print('       [x] a banda de um ataque reconta da tabela dona e passa no filtro.')

# ================================================================ 14
# v0.156: toda trava do catalogo de Manhas tem de apontar para a familia de onde
# ela sai. A coluna teve quatro fontes por quatro versoes e nenhuma escrita — e
# foi assim que o TR de tres entradas ficou fora do preco sem ninguem ver.
#
# Esta checagem NAO confere preco. Ela confere que toda Manha esta na tabela de
# derivacao, que a familia dela e uma das declaradas, e que a tabela de familias
# nao encolheu. O preco continua sendo decisao registrada.
print()
print('=' * 88)
print('14. A DERIVACAO DAS TRAVAS — toda Manha diz de onde a trava dela sai')
print('=' * 88)

_cat, _der = [], {}
for _l in MAN.split('\n'):
    _m = re.match(r'\|\s*\*\*[^|]+\*\*\s*\|\s*`([^`]+)`\s*\|.*\|\s*\*\*[\d,]+\*\*\s*\|\s*$', _l)
    if _m:
        _cat.append(_m.group(1))
    _d = re.match(r'\|\s*`([^`]+)`\s*\|\s*`?([^|`]+?)`?\s*\|\s*(acerto|Teste de Resistência|cenário|sem portão)\s*\|', _l)
    if _d:
        _der[_d.group(1)] = _d.group(3)

_fam = set(re.findall(r'^\|\s*\*\*(portão de acerto|portão de Teste de Resistência|'
                      r'taxa de cenário|sem portão)\*\*\s*\|', MAN, re.M))

if len(_fam) != 4:
    erro('14', f'a tabela de familias de trava tem {len(_fam)} linha(s) e devem ser 4 — '
               f'ela encolheu, e a checagem passaria a aceitar trava sem fonte')
elif len(_cat) < 10:
    erro('14', f'so li {len(_cat)} Manha(s) no catalogo — o extrator parou de casar')
else:
    _fora = [m for m in _cat if m not in _der]
    print(f'  {len(_cat)} Manhas no catalogo, {len(_der)} na tabela de derivacao, '
          f'{len(_fam)} familias declaradas')
    if _fora:
        erro('14', f'sem derivacao escrita: {", ".join(_fora)} — toda trava tem de '
                   f'dizer de que familia ela sai, senao a proxima medida diverge')
    else:
        _por = {}
        for _m2, _f in _der.items():
            _por[_f] = _por.get(_f, 0) + 1
        print('     ' + ' · '.join(f'{k}: {v}' for k, v in sorted(_por.items())))
        print('  [x] toda Manha do catalogo aponta para a familia de onde a trava dela sai.')

# ================================================================ veredito
print('\n' + '=' * 88)
if avisos:
    for a in avisos: print(f'  aviso: {a}')
if erros:
    print('>>> FALHOU')
    for e in erros: print('    ' + e)
    sys.exit(1)
print('>>> TUDO OK — o indice bate com os tres DESENHO nas duas direcoes, todo')
print('    total foi recontado, e nenhum bloco de regra contradiz o preco dele.')

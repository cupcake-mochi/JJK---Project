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

Nove checagens:
  1. TOTAIS    — a tabela de totais bate com o contado das tabelas de cima.
  2. SOMAS     — as duas somas do total fecham por caminhos diferentes.
  3. INDICE    — todo nome do indice existe no DESENHO dono dele.
  4. VOLTA     — todo nome batizado num degrau do DESENHO esta no indice.
  5. BLOCO     — toda entrega de Trilha com nome tem bloco de regra escrito.
  6. GATE      — bloco de regra nao contradiz o gate da linha de preco.
  7. CONTAGEM  — a pasta tem 17 pecas e 17 validadores.
  8. COPIAS    — todo documento que cita o total concorda com o contado.
  9. VALOR     — toda Classe que a linha de preco cobra aparece no bloco de regra.

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
PECAS_ESPERADAS = 17

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

S3 = fatia_da_peca('## 3. As 56 entregas de Trilha', '## 4. Os 20 degraus')
S4 = fatia_da_peca('## 4. Os 20 degraus', '## 5. As 13 Manhas')
S5 = fatia_da_peca('## 5. As 13 Manhas', '## 6. Os totais')
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
print('7. CONTAGEM — a pasta tem 17 pecas e 17 validadores')
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

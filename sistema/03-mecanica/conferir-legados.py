# -*- coding: utf-8 -*-
"""
conferir-legados.py — o validador da peca 13 (Legados).

Confere a regua de magnitude contra o catalogo, e o catalogo contra as pecas donas.

NADA DE VALOR FICA ESCRITO AQUI. Os quatro degraus de relogio saem da PECA 10,
as Origens saem da PECA 9, e as contagens saem da propria pasta. O unico bloco
com valor na mao e o LIMITES DE DESIGN abaixo, declarado a parte da regra
aplicada — que e a licao no 8: uma checagem nao pode se medir contra a propria
constante.

Onze checagens:
  1. FORMATO      — todo Legado esta sob um dos tres formatos.
  2. RELOGIO      — todo relogio e degrau da escada da peca 10.
  3. LARGURA      — categoria inteira nao fica em degrau rapido.
  4. DESLIGA/DANO — nenhum Desliga encosta em dano, imunidade, resistencia ou condicao.
  5. DESLIGA/TROCA— todo Desliga escreve o que custa em troca.
  6. COTA         — toda Origem soma DOIS Desliga entre escritos e reservados,
                    e toda vaga nomeia a peca que ela espera.
  7. ORIGENS      — as Origens do catalogo existem na peca 9, e nenhuma falta.
  8. SEM TECNICA  — aparece uma vez, e nao esta nas duas Origens especiais.
  9. CONTA        — a tabela de totais bate com o que a pasta tem de verdade.
 10. TRES FORMATOS— os doze exemplos da tabela do SS4 existem no catalogo.
 11. GLOSA        — a peca e o livro descrevem o Desliga pelas MESMAS duas
                   direcoes. A glosa estreita fez a v0.176 abrir uma pergunta
                   de formato que nao existia, e ela mora em dois lugares.

*Este cabecalho dizia NOVE ate a v0.179, e o codigo tinha DEZ desde que o bloco
da tabela dos tres formatos entrou. Contagem escrita a mao dentro do proprio
arquivo envelhece igual a de qualquer documento — a checagem 9 do
conferir-repositorio.py le do CODIGO, e por isso ela nunca acusou este.*

Roda de sistema/03-mecanica/. NAO le o .docx e NAO precisa de python-docx —
entao nao existe caminho por onde ele saia verde tendo pulado checagem.
"""
import os, re, sys

AQUI = os.path.dirname(os.path.abspath(__file__))
def ler(nome):
    with open(os.path.join(AQUI, nome), encoding='utf-8') as f:
        return f.read()

# ---------------------------------------------------------------- LIMITES DE DESIGN
# Declarados aqui, a parte da regra aplicada. Sao VOCABULARIO DO MANUAL: os quatro
# conceitos que ja tem preco pago em algum lugar, e que por isso um Desliga nao
# pode apagar de graca. Conferir no .docx antes de mexer.
PROIBIDO_NO_DESLIGA = ['imunidade', 'imune', 'resistencia', 'resistência', 'dano']
# A licao no 8 exige que o limite (acima) e a regra (abaixo) nao sejam a mesma
# fonte. A regra aplicada le do catalogo; o limite esta aqui e nao la.
ESPECIAIS_SEM_SUBORIGEM = ['Corpo Amaldiçoado', 'Restrição Celestial']
COTA_DESLIGA = 2

PECA  = ler('13-legados.md')
P9    = ler('09-origens.md')
P10   = ler('10-descanso-e-recuperacao.md')

erros, avisos = [], []
def erro(c, m): erros.append(f'[{c}] {m}')
def aviso(m):   avisos.append(m)

# ---------------------------------------------------------------- os donos
# degraus: da tabela "Os quatro relogios" da peca 10
sec10 = P10.split('## 5. Os quatro relógios')[1] if '## 5. Os quatro relógios' in P10 else ''
DEGRAUS = []
for ln in sec10.split('\n'):
    if not ln.startswith('|'): 
        if DEGRAUS: break
        continue
    cels = [c.strip() for c in ln.strip('|').split('|')]
    if len(cels) == 3 and cels[0].startswith('**'):
        DEGRAUS.append(cels[0].strip('*').strip())
if len(DEGRAUS) != 4:
    erro('SETUP', f'esperava 4 degraus na peca 10, achei {len(DEGRAUS)}: {DEGRAUS}')

# Origens: dos titulos de nivel 3 da peca 9 que tem bloco de Legados.
#
# Ate a v0.116 isto era `re.findall('^### ')` menos UM titulo excluido pelo nome
# ('Legado tem teto'). O comentario dizia "que tem bloco de Legados" e o codigo
# nao conferia isso — ele so conhecia a excecao que existia em 2026-08. Bastou a
# peca 9 ganhar tres subsecoes novas para as tres virarem "Origem sem lista no
# catalogo". Agora o filtro faz o que a frase diz: e Origem o titulo cujo bloco
# carrega a LINHA de Legados da tabela, que as sete tem e mais ninguem tem.
_BLOCOS_P9 = re.split(r'^### ', P9, flags=re.M)[1:]
ORIGENS_P9 = [b.split('\n', 1)[0].strip() for b in _BLOCOS_P9
              if re.search(r'^\|\s*\*\*Legados\*\*\s*\|', b, re.M)]
if not ORIGENS_P9:
    erro('SETUP', 'nenhum titulo de nivel 3 da peca 9 tem linha de Legados — '
                  'o extrator de Origem parou de extrair')

# ---------------------------------------------------------------- parse do catalogo
CAT = PECA.split('## 9. O catálogo')[1] if '## 9. O catálogo' in PECA else PECA
linhas = CAT.split('\n')
NOMES_DE_LISTA = ORIGENS_P9 + ['Sem Técnica']
origem_atual, formato_atual, pendente, em_tabela = None, None, None, False
entradas = []           # (origem, formato, nome, alcanca, relogio)
vagas    = []           # (origem, texto)
corpos   = {}           # nome -> paragrafo de citacao

for ln in linhas:
    m = re.match(r'^### (?:[\d.]+ · )?(.+?)(?: — |$)', ln)
    if m:
        titulo = m.group(1).strip()
        origem_atual = titulo if titulo in NOMES_DE_LISTA else None
        formato_atual, pendente, em_tabela = None, None, False
        continue
    if ln.startswith('#'):
        formato_atual, pendente, em_tabela = None, None, False
        continue
    # marcador de formato: linha em negrito que ABRE uma tabela de Legado
    mm = re.match(r'^\*\*(?:.*?— )?(Destranca|Ajusta|Desliga)\b', ln)
    if mm and not ln.startswith('|'):
        pendente, em_tabela = mm.group(1), False
        continue
    if not ln.startswith('|'):
        # rotulo de sub-tabela (**Ninhada**, **Gemeos**...) mantem o formato aberto
        if em_tabela:
            em_tabela = False
            pendente = formato_atual
        elif formato_atual and pendente is None:
            pendente = formato_atual
        continue
    # daqui pra baixo, e linha de tabela
    if pendente and not em_tabela:
        formato_atual, em_tabela = pendente, True
        pendente = None
    if not em_tabela or origem_atual is None or formato_atual is None:
        continue
    cels = [c.strip() for c in ln.strip('|').split('|')]
    if not cels or cels[0].startswith('---') or cels[0] in ('Legado', ''):
        continue
    if 'vaga reservada' in cels[0]:
        vagas.append((origem_atual, ' '.join(cels)))
        continue
    nome = cels[0].strip('*').strip()
    if not nome or nome.startswith('—'):
        continue
    alc = cels[1] if len(cels) > 1 else ''
    rel = cels[-1] if len(cels) > 2 else ''
    entradas.append((origem_atual, formato_atual, nome, alc, rel))

for m in re.finditer(r'^> \*\*(.+?)\*\* — (.+?)(?=\n>?\s*\n|\n> \*\*)', CAT, re.M | re.S):
    corpos[m.group(1).strip()] = m.group(2)

print('=' * 88)
print('CONFERIR LEGADOS — a peca 13 contra as pecas donas')
print('=' * 88)
print(f'  degraus lidos da peca 10 : {DEGRAUS}')
print(f'  Origens lidas da peca 9  : {len(ORIGENS_P9)}')
print(f'  entradas no catalogo     : {len(entradas)}  ({len(vagas)} vaga(s) reservada(s))')

# ---------------------------------------------------------------- 1. FORMATO
print('\n' + '=' * 88 + '\n1. FORMATO — todo Legado esta sob um dos tres\n' + '=' * 88)
FORMATOS = ['Ajusta', 'Desliga', 'Destranca']
ruins = [e for e in entradas if e[1] not in FORMATOS]
if ruins: erro('1', f'{len(ruins)} entrada(s) fora dos tres formatos')
else:     print(f'  [x] as {len(entradas)} entradas estao sob Ajusta, Desliga ou Destranca.')

# ---------------------------------------------------------------- 2. RELOGIO
print('\n' + '=' * 88 + '\n2. RELOGIO — todo relogio e degrau da escada da peca 10\n' + '=' * 88)
LIVRES = ['sempre', '—', '-', '']
mau = []
for org, fmt, nome, alc, rel in entradas:
    if fmt == 'Destranca' and rel in LIVRES + ['sem relógio']:
        continue
    r = rel.lower().strip()
    if r in [x.lower() for x in LIVRES] or r == 'sem relógio':
        continue
    if not any(d.lower() == r for d in DEGRAUS):
        mau.append(f'{org} · {nome} → "{rel}"')
if mau:
    erro('2', 'relogio fora da escada da peca 10:')
    for x in mau: erro('2', f'    {x}')
else:
    print(f'  [x] todo relogio usado e um dos quatro degraus da peca 10.')
    usados = sorted({e[4] for e in entradas if e[4] and e[4] not in LIVRES}, key=str)
    print(f'      em uso: {usados}')

# ---------------------------------------------------------------- 3. LARGURA
print('\n' + '=' * 88 + '\n3. LARGURA — categoria inteira nao fica em degrau rapido\n' + '=' * 88)
RAPIDOS = [d.lower() for d in DEGRAUS[:2]]      # por cena, por descanso curto
largos = []
for org, fmt, nome, alc, rel in entradas:
    if fmt != 'Ajusta': continue
    a = alc.lower()
    eh_largo = 'qualquer' in a and not re.search(r'\((\d+)\)', a)
    if eh_largo and rel.lower() in RAPIDOS:
        largos.append(f'{org} · {nome} → "{alc}" em "{rel}"')
if largos:
    erro('3', 'gatilho de categoria inteira em degrau rapido:')
    for x in largos: erro('3', f'    {x}')
else:
    n = sum(1 for e in entradas if e[1] == 'Ajusta')
    print(f'  [x] os {n} Ajusta respeitam a trava: categoria inteira desce de degrau.')

# ---------------------------------------------------------------- 4. DESLIGA / DANO
print('\n' + '=' * 88 + '\n4. DESLIGA — nenhum encosta em dano, e o de condicao carrega o relogio do nivel\n' + '=' * 88)
enc = []
for org, fmt, nome, alc, rel in entradas:
    if fmt != 'Desliga': continue
    txt = (alc + ' ' + corpos.get(nome, '')).lower()
    for p in PROIBIDO_NO_DESLIGA:
        if p in txt:
            enc.append(f'{org} · {nome} → usa "{p}"')
if enc:
    erro('4', 'Desliga encostando em coisa que tem preco:')
    for x in enc: erro('4', f'    {x}')
else:
    n = sum(1 for e in entradas if e[1] == 'Desliga')
    print(f'  [x] os {n} Desliga escritos so apagam o que ninguem comprou.')

# v0.104: a trava do Desliga foi relaxada — ele pode ENFRAQUECER o que alguem
# comprou, e "enfraquecer" quer dizer apagar UMA VEZ, com relogio. A trava so
# vale se o degrau do relogio sair do NIVEL da condicao, e nao do gosto de quem
# escreve. Os niveis vem da peca 19; a tabela de degrau por nivel vem da peca 13.
# Nada disso esta escrito aqui dentro.
P19 = ler('19-dano-e-condicoes.md')
NIVEL_DA_CONDICAO = {}
for _l in P19.split('\n'):
    _m = re.match(r'^\|\s*\*\*`([A-Za-zÀ-ú]+)`\*\*\s*\|\s*`(Leve|Média|Pesada)`\s*\|', _l)
    if _m:
        NIVEL_DA_CONDICAO[_m.group(1)] = _m.group(2)
_secT = PECA[PECA.find('> **E o degrau do relógio sai do nível da condição**'):]
_secT = _secT[:_secT.find('\n')]
DEGRAU_POR_NIVEL = {}
for _n, _d in re.findall(r'`(Leve|Média|Pesada)` → \*\*([^*]+)\*\*', _secT):
    DEGRAU_POR_NIVEL[_n] = _d.strip()
if len(NIVEL_DA_CONDICAO) != 13:
    erro('4', f'li {len(NIVEL_DA_CONDICAO)} condicao(oes) com nivel na peca 19 e '
              'esperava 13 — a extracao quebrou e a trava do relogio nao vale')
elif len(DEGRAU_POR_NIVEL) != 3:
    erro('4', 'a peca 13 nao publica mais os tres degraus de relogio por nivel de '
              'condicao, no formato que esta checagem le')
else:
    _fora = []
    for org, fmt, nome, alc, rel in entradas:
        if fmt != 'Desliga':
            continue
        _cond = [c for c in NIVEL_DA_CONDICAO if f'`{c}`' in alc]
        if not _cond:
            continue
        if len(_cond) > 1:
            _fora.append(f'{org} · {nome} → nomeia mais de uma condicao: {_cond}')
            continue
        _niv = NIVEL_DA_CONDICAO[_cond[0]]
        _esp = DEGRAU_POR_NIVEL[_niv]
        if rel.strip() != _esp:
            _fora.append(f'{org} · {nome} → apaga `{_cond[0]}` ({_niv}) com relogio '
                         f'"{rel.strip()}" e o nivel pede "{_esp}"')
    if _fora:
        erro('4', 'Desliga de condicao com o relogio errado:')
        for x in _fora:
            erro('4', f'    {x}')
    else:
        _q = sum(1 for o, f, n, a, r in entradas if f == 'Desliga'
                 and any(f'`{c}`' in a for c in NIVEL_DA_CONDICAO))
        print(f'  [x] os {_q} Desliga que nomeiam condicao carregam o relogio que o '
              'nivel dela pede')

# ---------------------------------------------------------------- 5. DESLIGA / TROCA
print('\n' + '=' * 88 + '\n5. DESLIGA — todo um escreve o que custa em troca\n' + '=' * 88)
sem = [f'{o} · {n}' for o, f, n, a, r in entradas
       if f == 'Desliga' and 'em troca' not in corpos.get(n, '').lower()]
if sem:
    erro('5', 'Desliga sem clausula de troca: ' + ', '.join(sem))
else:
    print('  [x] todo Desliga escreve o que custa em troca, no proprio texto.')

# ---------------------------------------------------------------- 6. COTA
print('\n' + '=' * 88 + f'\n6. COTA — toda Origem soma {COTA_DESLIGA} Desliga, e toda vaga nomeia a peca\n' + '=' * 88)
origens_cat = sorted({e[0] for e in entradas})
for org in origens_cat:
    escritos = sum(1 for e in entradas if e[0] == org and e[1] == 'Desliga')
    reserv   = sum(1 for v in vagas if v[0] == org)
    tot = escritos + reserv
    marca = '[x]' if tot == COTA_DESLIGA else '[ ]'
    print(f'  {marca} {org:<22} {escritos} escrito(s) + {reserv} reservada(s) = {tot}')
    if tot != COTA_DESLIGA:
        erro('6', f'{org} soma {tot} Desliga, e a cota e {COTA_DESLIGA}')
# Uma vaga reservada tem de dizer o que ela esta esperando, e desde a v0.103 as
# duas respostas legais sao DIFERENTES: ou ela ainda espera uma peca que nao
# existe, ou a peca ja saiu e a vaga esta DESTRAVADA de ORIGEM. Aceitar so' a
# primeira forma obrigaria a vaga a mentir depois que a peca nascesse — foi o
# que a peca 19 fez com tres delas naquela versao.
#
# v0.188: a celula da vaga destravada dizia "e por escrever", e essa era a
# promessa falsa que a 6.1 existe para proibir — as duas checagens do mesmo
# arquivo pediam coisas opostas, e a peca sentava no meio. Agora a celula
# declara o ESTADO DO ALVO, que e a segunda metade da destrava, e a ancora sai
# da prosa e vai para a tabela.
mudas = [v for v in vagas
         if 'espera' not in v[1].lower() and 'destravada' not in v[1].lower()]
if mudas:
    erro('6', f'{len(mudas)} vaga(s) reservada(s) sem dizer o que estao esperando '
              f'nem declarar que ja destravaram')
else:
    import collections
    esperando = [v for v in vagas if 'destravada' not in v[1].lower()]
    destrav = [v for v in vagas if 'destravada' in v[1].lower()]
    print(f'  [x] as {len(vagas)} vagas dizem o que esperam: '
          f'{len(esperando)} esperando peca, {len(destrav)} destravada(s) de Origem.')
    quem = collections.Counter()
    for _, txt in esperando:
        m = re.search(r'espera a pe[cç]a de ([^*|]+)', txt)
        quem[m.group(1).strip() if m else '?'] += 1
    for k, v in sorted(quem.items()):
        print(f'      {v} espera(m) a peca de {k}')
    quem2 = collections.Counter()
    _ALVO = re.compile(r'travada de alvo|sem alvo livre|com alvo livre', re.I)
    _sem_alvo = []
    for _, txt in destrav:
        m = re.search(r'destravada pela pe[cç]a (\d+)', txt)
        quem2[m.group(1) if m else '?'] += 1
        if not _ALVO.search(txt):
            _sem_alvo.append(txt.strip())
    for k, v in sorted(quem2.items()):
        print(f'      {v} destravada(s) de Origem pela peca {k}')
    if '?' in quem2:
        erro('6', f'{quem2["?"]} vaga(s) dizem "destravada" sem nomear a peca que '
                  f'destravou — vaga que nao nomeia e cheque em branco do mesmo jeito')
    if _sem_alvo:
        erro('6', f'{len(_sem_alvo)} vaga(s) declaram destrava de ORIGEM e nao declaram o '
                  f'estado do ALVO — destravar a Origem nao destrava o alvo, e uma celula '
                  f'que cala sobre isso volta a ler como "so falta escrever". '
                  f'Primeira: "{_sem_alvo[0][:70]}"')
    else:
        print('  [x] toda vaga destravada declara na tabela se o alvo esta livre ou travado.')

# -- 6.1: destravada de ORIGEM nao e destravada de ALVO -----------------------
# v0.187: a peca dizia as DUAS coisas sobre a mesma vaga, na mesma secao. Num
# lugar: "ela nao espera peca nenhuma, e o que falta ali e escrita". No fim da
# mesma secao: "o alvo livre acabou — daqui para a frente todo Desliga novo
# depende de peca nova criar coisa nomeada". As duas nao podem ser verdade
# juntas, e a fila herdou a primeira: o item passou versoes descrito como se
# bastasse sentar e escrever, quando o que falta e ALVO.
#
# A checagem guarda a RELACAO e nao a decisao. Enquanto a enumeracao estiver
# esgotada, nenhuma linha pode prometer que so falta escrita. E ela NAO passa
# por ausencia: se a declaracao da enumeracao sumir, isso tambem acende — senao
# apagar a frase viraria o conserto barato para a divergencia.
#
# v0.188: o reconhecedor da promessa nasceu ancorado em quatro frases inteiras,
# e uma delas foi copiada SEM a virgula que a peca tem. Com isso a 6.1 saiu
# verde na propria linha que ela existia para pegar — "O que falta nela e
# escrita, e nao peca" ficou de pe na secao 8 enquanto o §10 dizia o contrario.
# Frase inteira e ancora de prosa: qualquer virgula a derruba. O reconhecedor
# passou a ser FAMILIA de promessa, com cada membro provado no arnes, e a
# ancora dura mudou de casa — a celula da tabela declara o estado do alvo, e a
# checagem 6 cobra ela.
#
# E a checagem aceita as DUAS declaracoes, e nao so' a de esgotada. Sem a
# oposta ela seria satisfeita de um jeito so, que e o outro nome de checagem
# trivialmente verdadeira — e o contra-teste dela nao teria como existir:
# trocar a declaracao para "sobrou alvo livre" E abrir a vaga junto tem de
# ficar VERDE, porque aquilo e uma peca coerente com outra decisao.
_ESGOTADA = re.compile(r'alvo livre acabou|zero alvo livre|zero livres|'
                       r'depende de peça nova (?:nomear|criar) coisa', re.I)
_TEM_ALVO = re.compile(r'sobrou alvo livre|ainda há alvo livre|'
                       r'a enumeração da seção 8 tem alvo livre', re.I)
_SO_ESCRITA = re.compile(r'não espera peça nenhuma|não depende de peça nenhuma|'
                         r'falta (?:ali|nela|nele|aqui) é escrita|'
                         r'o que falta é escrita|'
                         r'e por escrever|'
                         r'(?:só falta|basta) sentar', re.I)
# `bastasse` e `bastava` ficam FORA de proposito: as duas so' aparecem em nota
# historica contando o defeito antigo, e por em recognizer o tempo passado da
# promessa e plantar armadilha em toda nota de correcao que este arquivo
# escrever daqui para a frente. O reconhecedor le AFIRMACAO no presente — a
# mesma regra que ja tira as frases entre aspas.
if not _ESGOTADA.search(PECA) and not _TEM_ALVO.search(PECA):
    erro('6', 'a peca parou de declarar o estado da enumeracao de alvos da secao 8 — sem '
              'essa declaracao, uma vaga pode voltar a prometer que so falta escrita e '
              'nada contradiz')
elif not _ESGOTADA.search(PECA):
    print('  [x] a peca declara que ainda sobra alvo livre — a promessa de escrita e legitima.')
else:
    _contra = [l for l in PECA.split('\n') if _SO_ESCRITA.search(l)]
    # a celula da tabela entra na mesma relacao: com a enumeracao esgotada,
    # nenhuma vaga pode declarar `com alvo livre`. Mudar as duas metades de
    # forma coerente — tirar a declaracao de esgotada E abrir o alvo — fica
    # verde de proposito, e e o contra-teste desta checagem.
    _contra += [t for _, t in vagas if re.search(r'com alvo livre', t, re.I)]
    if _contra:
        erro('6', f'{len(_contra)} linha(s) dizem que a vaga so espera escrita, e a peca '
                  'declara que a enumeracao de alvos esta esgotada — destravada de ORIGEM '
                  'nao e destravada de ALVO. Primeira: "' + _contra[0].strip()[:90] + '"')
    else:
        print('  [x] a enumeracao esta declarada esgotada, e nenhuma linha promete que a '
              'vaga so espera escrita.')

# -- 6.2: destino de Legado morto nao pode ser coisa que outra regra proibe ---
# v0.188. O `Nao Sou Gente` saiu do catalogo na v0.38 por ser imunidade a dano, e
# a v0.39 escreveu o destino dele: "vira Passiva paga com espaco de feitico". Ela
# citou a caixa IMUNIDADE do manual — "nenhuma Melhoria fura imunidade; quem
# quiser isso monta uma Passiva de Regra Propria" —, e aquela caixa e do lado do
# ATAQUE: `Melhoria` e peca de feitico, e furar e atravessar a imunidade DE
# OUTRO. Quem decide o lado da defesa e a lista `Limites` do capitulo 9 do livro,
# que poe "imunidade completa a um tipo de dano ou condicao" entre o que nenhuma
# Passiva paga pode fazer.
#
# Resultado: a decisao ficou 149 versoes como tomada-e-nao-aplicada, e ela nunca
# podia ser aplicada. E a licao no 6 na forma dela: antes de aceitar um destino,
# va ler a regra pendurada nele.
#
# A checagem guarda a RELACAO e nao a decisao, no mesmo molde da 6.1: enquanto o
# livro publicar a proibicao, nenhuma linha viva desta peca pode prometer a
# Passiva. E ela aceita o estado OPOSTO — se um dia o livro deixar de proibir, a
# peca declara isso com todas as letras e a promessa volta a ser legal. Sem esse
# lado, a checagem so podia ser satisfeita de um jeito e o contra-teste dela nao
# teria como existir.
#
# E ela NAO passa por ausencia nos dois eixos: capitulo que sumiu acende, e
# proibicao que sumiu SEM a declaracao no lugar acende tambem — senao apagar a
# linha do livro viraria o conserto barato para a divergencia.
_LIM = os.path.join(AQUI, '..', '05-material', 'livro', 'manual', '40-fundamento.md')
_PROIBE = re.compile(r'[Ii]munidade completa a um tipo de dano ou condição')
_LIBEROU = re.compile(r'o livro deixou de proibir Passiva paga de dar imunidade', re.I)
_PROMETE = re.compile(r'vir(?:a|ou) Passiva paga|virar Passiva|'
                      r'vira Passiva de Regra Própria|'
                      r'foi para a Passiva|nome inteiro foi para a Passiva')
_prom = [l for l in PECA.split('\n')
         if _PROMETE.search(re.sub(r'~~.*?~~|"[^"]*"|“[^”]*”', ' ', l))]
if not os.path.isfile(_LIM):
    erro('6', 'nao achei o capitulo do Fundamento no livro — a 6.2 le dali a lista '
              '`Limites`, que e quem decide se um Legado morto pode virar Passiva paga')
elif _PROIBE.search(ler(_LIM)):
    if _prom:
        erro('6', f'{len(_prom)} linha(s) mandam um Legado morto virar Passiva paga, e o '
                  f'capitulo 9 do livro proibe Passiva paga de dar imunidade completa. '
                  f'Primeira: "' + _prom[0].strip()[:90] + '"')
    else:
        print('  [x] o livro proibe Passiva paga de dar imunidade completa, e nenhuma '
              'linha desta')
        print('      peca manda um Legado morto virar Passiva paga.')
elif not _LIBEROU.search(PECA):
    erro('6', 'o capitulo 9 do livro parou de publicar "imunidade completa a um tipo de '
              'dano ou condicao" entre os `Limites`, e esta peca nao declara que isso '
              'mudou — a proibicao nao pode sumir em silencio, senao apaga-la vira o '
              'conserto barato para a divergencia')
else:
    print('  [x] a peca declara que o livro deixou de proibir — a promessa de Passiva paga')
    print('      voltou a ser legal, e a 6.2 sai de cena de proposito.')

# ---------------------------------------------------------------- 7. ORIGENS
print('\n' + '=' * 88 + '\n7. ORIGENS — as do catalogo existem na peca 9, e nenhuma falta\n' + '=' * 88)
faltando = [o for o in ORIGENS_P9 if o not in origens_cat]
sobrando = [o for o in origens_cat if o not in ORIGENS_P9]
if faltando: erro('7', f'Origem da peca 9 sem lista no catalogo: {faltando}')
if sobrando: erro('7', f'lista no catalogo sem Origem na peca 9: {sobrando}')
if not faltando and not sobrando:
    print(f'  [x] as {len(ORIGENS_P9)} Origens da peca 9 tem lista, e nao existe lista orfa.')

# ---------------------------------------------------------------- 8. SEM TECNICA
print('\n' + '=' * 88 + '\n8. SEM TECNICA — nas cinco que aceitam, em nenhuma das duas especiais\n' + '=' * 88)
if '### Sem Técnica' not in PECA:
    erro('8', 'a secao do Sem Tecnica nao existe na peca')
else:
    st = PECA.split('### Sem Técnica')[1].split('\n### ')[0]
    # as cinco que aceitam sao as da peca 9 menos as duas especiais — lido, nao escrito
    ELEGIVEIS = [o for o in ORIGENS_P9 if o not in ESPECIAIS_SEM_SUBORIGEM]
    faltam_eleg = [o for o in ELEGIVEIS if o not in st]
    excluidas   = [e for e in ESPECIAIS_SEM_SUBORIGEM if e in st]
    if faltam_eleg:
        erro('8', f'Origem que aceita Sem Tecnica nao esta listada na secao: {faltam_eleg}')
    elif len(excluidas) != len(ESPECIAIS_SEM_SUBORIGEM):
        erro('8', 'a secao nao nomeia as duas Origens especiais para exclui-las')
    elif not re.search(r'especiais\s+n[aã]o', st):
        erro('8', 'a secao nomeia as especiais mas nao diz que elas NAO aceitam')
    else:
        print(f'  [x] o Sem Tecnica lista as {len(ELEGIVEIS)} elegiveis e exclui as 2 especiais.')
        print('      (escrito uma vez e referenciado: cinco copias seriam a licao no 9)')

# ---------------------------------------------------------------- 9. CONTA
print('\n' + '=' * 88 + '\n9. CONTA — a tabela de totais bate com o catalogo de verdade\n' + '=' * 88)
tot_tab = re.search(r'^\|\s*\|\s*\*\*(\d+)\*\*\s*\|\s*\*\*(\d+)\*\*\s*\|\s*\*\*(\d+)\*\*\s*\|\s*\*\*(\d+)\*\*\s*\|\s*\*\*(\d+)\*\*\s*\|', PECA, re.M)
real = {f: sum(1 for e in entradas if e[1] == f) for f in FORMATOS}
real_total = len(entradas)
print(f'  contado na pasta : Destranca {real["Destranca"]} · Ajusta {real["Ajusta"]} · Desliga {real["Desliga"]} = {real_total}')
if not tot_tab:
    erro('9', 'nao achei a linha de totais da tabela de conta')
else:
    d, a, de, rv, tt = (int(x) for x in tot_tab.groups())
    print(f'  escrito na tabela: Destranca {d} · Ajusta {a} · Desliga {de} (+{rv} reservadas) = {tt}')
    if (d, a, de, tt) != (real['Destranca'], real['Ajusta'], real['Desliga'], real_total):
        erro('9', 'a tabela de conta nao bate com o catalogo — reconte antes de fechar versao')
    elif rv != len(vagas):
        erro('9', f'a tabela diz {rv} vagas reservadas e o catalogo tem {len(vagas)}')
    else:
        print('  [x] a conta escrita bate com a contada. Nenhum total foi digitado a mao sem conferir.')

# ==========================================================================
print('\n' + '=' * 88 + '\n10. A TABELA DOS TRES FORMATOS — os doze exemplos dela existem?\n' + '=' * 88)
# A tabela do §4 e a PORTA DE ENTRADA da peca: e a primeira coisa que a mesa le
# sobre o que cada formato faz. Ela e ILUSTRACAO, nao regra, e por isso nenhum
# validador a alcancava — e ela ficou errada em TRES das doze entradas da v0.39
# ate a v0.104: `Treino de Berco` virou Destranca, `Corpo Emprestado` virou
# Ajusta, e `Nao Sou Gente` saiu do catalogo. Os tres foram convertidos pela
# propria v0.39, que nao voltou nas tabelas que os citavam de exemplo.
# O formato de cada exemplo vem DO CATALOGO, e nao de lista escrita aqui.
_real = {}
for _o, _f, _n, _a, _r in entradas:
    _real.setdefault(_n, set()).add(_f)
_i = PECA.find('| **Ajusta** | mexe num número de uma rolagem |')
if _i < 0:
    erro('10', 'nao achei a tabela dos tres formatos no §4 — ela mudou de forma e '
                'esta checagem parou de conferir')
else:
    _bloco = PECA[_i:PECA.find('\n\n', _i)]
    _n_ex, _maus = 0, []
    for _ln in _bloco.split('\n'):
        _m = re.match(r'^\|\s*\*\*(\w+)\*\*\s*\|[^|]*\|\s*(.+?)\s*\|$', _ln)
        if not _m:
            continue
        _f = _m.group(1)
        for _e in (x.strip() for x in _m.group(2).split('·')):
            _n_ex += 1
            if _e not in _real:
                _maus.append(f'{_e} (citado como {_f}) nao esta no catalogo')
            elif _f not in _real[_e]:
                _maus.append(f'{_e} e citado como {_f} e no catalogo e '
                             + '/'.join(sorted(_real[_e])))
    if _n_ex != 12:
        erro('10', f'a tabela do §4 traz {_n_ex} exemplos e eu esperava 12 — ela '
                    'mudou de forma e esta checagem parou de conferir')
    if _maus:
        erro('10', 'exemplo da tabela dos tres formatos divergindo do catalogo: '
                   + '; '.join(_maus))
    elif _n_ex == 12:
        print('  [x] os 12 exemplos do §4 existem no catalogo e estao no formato certo')

# ------------------------------------------------- 11. GLOSA DO DESLIGA, NO LIVRO
# A regua do SS5 e' "apaga o que ninguem comprou", e ela nunca teve problema. O que
# tinha era a GLOSA ao lado dela — "o que o mundo faz com voce" —, que descrevia um
# catalogo mais estreito que o real: o `Ferro Velho` e o `Sangue que Nao e Sangue`
# apagam coisa que o mundo COBRA e nao coisa que chega, e o segundo diz isso no
# proprio texto. A glosa estreita fez a v0.176 abrir uma pergunta de formato sobre
# o `Conhecimento Antigo` que nao existia. Ela mora em DOIS lugares — esta peca e o
# capitulo 7 do livro — e ninguem comparava os dois, que e a licao no 9 em prosa.
print('\n' + '=' * 88)
print('11. GLOSA DO DESLIGA — a peca e o livro contam a mesma historia?')
print('=' * 88)
_CAP = os.path.join(AQUI, '..', '05-material', 'livro', 'manual', '25-origens.md')
if not os.path.isfile(_CAP):
    erro('GLOSA', 'nao achei o capitulo de Origens do livro — a glosa do Desliga tem duas '
                  'publicacoes e so uma seria conferida')
else:
    # RECORTE, e ele e' o que faz a checagem valer: lendo o documento inteiro ela
    # passava por causa de uma frase VIZINHA — apagar a direcao da glosa do §5 saia
    # verde porque o exemplo do `Sangue que Nao e Sangue`, tres linhas abaixo, tem a
    # palavra "precisar". Achado no arnes da v0.179.
    def _bloco(txt, ini, fim):
        i = txt.find(ini)
        if i < 0:
            return ''
        j = txt.find(fim, i + len(ini))
        return txt[i:j if j > 0 else len(txt)]

    _liv = _bloco(open(_CAP, encoding='utf-8').read(), '### Como ler um Desliga', '\n### ')
    _pec = _bloco(ler('13-legados.md'), '### Desliga —', '\n### ')
    if not _liv or not _pec:
        erro('GLOSA', 'nao achei a secao que explica o Desliga num dos dois documentos — '
                      'sem o recorte a checagem le o arquivo inteiro e passa por vizinhanca')
    # as duas direcoes que o catalogo realmente usa, cada uma com um exemplar vivo
    # A alternativa `precisar ` era frouxa: ela casava com o EXEMPLO do `Sangue que
    # Nao e Sangue`, que mora dentro do mesmo recorte, entao apagar a direcao da
    # glosa saia verde por vizinhanca de novo. A frase tem de dizer as duas com as
    # palavras dela, e nao por acidente de exemplo.
    _dirs = (('chega em você', r'chega em voc[êe]'), ('teria de fazer', r'teria de fazer'))
    # o negrito parte a frase no meio ("uma coisa que **chega** em voce"), entao a
    # comparacao normaliza os `*` antes de casar — senao a checagem acusa formatacao
    # em vez de conteudo, que e o pior tipo de falso positivo.
    for _onde, _txt in (('a peca 13 §5', _pec), ('o capitulo 7 do livro', _liv)):
        _n = _txt.replace('*', '')
        _falta = [n for n, rx in _dirs if not re.search(rx, _n, re.I)]
        if _falta:
            erro('GLOSA', f'{_onde} descreve o Desliga so por uma direcao — falta "{_falta[0]}". '
                          'O catalogo tem exemplar vivo das DUAS, e uma glosa que nomeia so '
                          'uma faz a proxima entrada ser medida contra a regua errada')
        else:
            print(f'  [x] {_onde}: nomeia as duas direcoes do Desliga.')
    # e o exemplar que prova que a direcao larga nao e teorica
    if 'não é uma coisa que acontece com você' not in ler('13-legados.md'):
        erro('GLOSA', 'o `Ferro Velho` deixou de dizer que "cansaco nao e uma coisa que '
                      'acontece com voce" — era ele que provava, dentro do proprio catalogo, '
                      'que a glosa estreita estava errada')
    else:
        print('  [x] o `Ferro Velho` continua sendo o contra-exemplo escrito da glosa estreita.')

# ---------------------------------------------------------------- 12
# O que a Origem entrega em oficio e Teste de Resistencia mora em DOIS lugares do
# capitulo 7: a tabela `Caracteristicas da Origem`, no topo, e o bloco `Efeito na
# ficha` de cada uma. Ate a v0.209 morava so na tabela, e a mesa perguntava — o
# leitor que abre numa Origem via so a lista de pericias e concluia que o oficio e
# o TR daquela Origem tinham faltado. Sao SETE copias do mesmo paragrafo agora, e
# copia sem comparacao diverge (licao no 9).
print('\n' + '=' * 88)
print('12. O TR NA ORIGEM — as sete copias, e nenhuma promete oficio')
print('=' * 88)
if not os.path.isfile(_CAP):
    erro('ORIGEM-EXTRA', 'nao achei o capitulo de Origens do livro')
else:
    _t = open(_CAP, encoding='utf-8').read()
    _origens = re.findall(r'^## ([^\n]+)\n(.*?)(?=^## |\Z)', _t, re.S | re.M)
    _com_pericia = [(n, c) for n, c in _origens if '#### Perícias' in c]
    _blocos = {}
    for _n, _c in _com_pericia:
        _m = re.search(r'#### Teste de Resistência\n(.*?)(?=^#### |\Z)', _c, re.S | re.M)
        _blocos[_n.strip()] = _m.group(1).strip() if _m else None
    _faltam = [n for n, b in _blocos.items() if b is None]
    if not _com_pericia:
        erro('ORIGEM-EXTRA', 'nao achei nenhuma Origem com `#### Perícias` no capitulo 7 — '
                             'ou o formato do bloco `Efeito na ficha` mudou')
    elif _faltam:
        erro('ORIGEM-EXTRA', f'{len(_faltam)} Origem(ns) publicam a lista de pericias e nao '
                             f'dizem do Teste de Resistencia: {sorted(_faltam)}. '
                             'A mesa perguntou justamente por isso: sem a linha, o leitor '
                             'conclui que os dois faltaram naquela Origem')
    else:
        _uniq = set(_blocos.values())
        if len(_uniq) > 1:
            erro('ORIGEM-EXTRA', f'as {len(_blocos)} copias do bloco de oficio e TR '
                                 f'divergiram: {len(_uniq)} redacoes diferentes. Nenhuma '
                                 'Origem muda esses dois, entao a divergencia e erro')
        else:
            # e a copia tem de dizer o que a tabela do topo do capitulo diz
            _tab = _bloco(_t, '| O que você anota | Detalhe |', '\n### ')
            _quer = [
                ('escolha entre os quatro Testes de Resistencia',
                 r'qualquer um dos quatro', r'quatro'),
                ('o outro TR vem do Caminho', r'o outro vem do Caminho', r'Caminho'),
            ]
            _texto = next(iter(_uniq))
            # v0.211: a Origem parou de dar oficio. A negacao e' cobrada nos DOIS
            # documentos, e nos dois sentidos: a tabela do topo nao pode voltar a
            # oferecer, e o bloco tem de dizer com todas as letras que nao ha —
            # senao o leitor conclui de novo que o oficio daquela Origem faltou.
            if re.search(r'ofício livre', _tab):
                erro('ORIGEM-EXTRA', 'a tabela `Caracteristicas da Origem` voltou a '
                                     'oferecer oficio, e desde a v0.211 quem da oficio '
                                     'e o Caminho')
            if not re.search(r'A Origem não dá ofício', _texto):
                erro('ORIGEM-EXTRA', 'o bloco das sete Origens parou de declarar que a '
                                     'Origem nao da oficio — foi essa falta que a mesa '
                                     'perguntou, e a ausencia da linha nao se le')
            _erra = [rot for rot, na_tab, no_bloco in _quer
                     if not (re.search(na_tab, _tab) and re.search(no_bloco, _texto))]
            if not _tab:
                erro('ORIGEM-EXTRA', 'nao achei a tabela `Caracteristicas da Origem` — ela e '
                                     'a dona do que a Origem entrega, e sem ela as sete '
                                     'copias nao tem contra o que ser medidas')
            elif _erra:
                erro('ORIGEM-EXTRA', 'o bloco publicado nas sete Origens perdeu o que a '
                                     f'tabela do topo declara: {_erra}')
            else:
                print(f'  [x] as {len(_blocos)} Origens com lista de pericia publicam o mesmo '
                      'bloco de oficio e TR, e ele bate com a tabela do topo do capitulo.')

# ---------------------------------------------------------------- veredito
print('\n' + '=' * 88)
if avisos:
    for a in avisos: print(f'  aviso: {a}')
if erros:
    print('>>> FALHOU')
    for e in erros: print('    ' + e)
    sys.exit(1)
print('>>> TUDO OK — a regua fecha, o catalogo obedece a ela, e todo numero')
print('    conferido aqui foi lido do documento dono.')

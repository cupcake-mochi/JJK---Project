# -*- coding: utf-8 -*-
"""
conferir-legados.py — o validador da peca 13 (Legados).

Confere a regua de magnitude contra o catalogo, e o catalogo contra as pecas donas.

NADA DE VALOR FICA ESCRITO AQUI. Os quatro degraus de relogio saem da PECA 10,
as Origens saem da PECA 9, e as contagens saem da propria pasta. O unico bloco
com valor na mao e o LIMITES DE DESIGN abaixo, declarado a parte da regra
aplicada — que e a licao no 8: uma checagem nao pode se medir contra a propria
constante.

Nove checagens:
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

# Origens: dos titulos de nivel 3 da peca 9 que tem bloco de Legados
ORIGENS_P9 = [t.strip() for t in re.findall(r'^### (.+)$', P9, re.M)
              if 'Legado tem teto' not in t]

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
if len(NIVEL_DA_CONDICAO) != 14:
    erro('4', f'li {len(NIVEL_DA_CONDICAO)} condicao(oes) com nivel na peca 19 e '
              'esperava 14 — a extracao quebrou e a trava do relogio nao vale')
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
# existe, ou a peca ja saiu e a vaga esta DESTRAVADA e por escrever. Aceitar so'
# a primeira forma obrigaria a vaga a mentir depois que a peca nascesse — foi o
# que a peca 19 fez com tres delas nesta versao.
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
          f'{len(esperando)} esperando peca, {len(destrav)} destravada(s) e por escrever.')
    quem = collections.Counter()
    for _, txt in esperando:
        m = re.search(r'espera a pe[cç]a de ([^*|]+)', txt)
        quem[m.group(1).strip() if m else '?'] += 1
    for k, v in sorted(quem.items()):
        print(f'      {v} espera(m) a peca de {k}')
    quem2 = collections.Counter()
    for _, txt in destrav:
        m = re.search(r'destravada pela pe[cç]a (\d+)', txt)
        quem2[m.group(1) if m else '?'] += 1
    for k, v in sorted(quem2.items()):
        print(f'      {v} destravada(s) pela peca {k}, e por escrever')
    if '?' in quem2:
        erro('6', f'{quem2["?"]} vaga(s) dizem "destravada" sem nomear a peca que '
                  f'destravou — vaga que nao nomeia e cheque em branco do mesmo jeito')

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

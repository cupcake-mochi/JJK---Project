# -*- coding: utf-8 -*-
"""
conferir-equipamento.py — o validador da peca de Equipamento.

NADA DE VALOR FICA ESCRITO AQUI. O fundo sai do SS5.0.1 e do SS5.0.5, o catalogo
sai do SS5.3, o corte simples/marcial sai do SS5.4.1, o 10 da Defesa sai da PECA 1,
os tetos de atributo e de refino saem da PECA 2 e a formula de cobrir-se sai da
PECA 11. O unico bloco com valor na mao e o LIMITES DE DESIGN, declarado a parte
da regra aplicada — licao no 8: uma checagem nao pode se medir contra a propria
constante.

Onze checagens:
  1. ORCAMENTO   — toda arma gasta o fundo exato. Nem sobra, nem estoura.
  2. DOMINANCIA  — a matriz sobre ARMA (nao sobre classe), uma vez por escada.
  3. PROPRIEDADE — toda propriedade usada no catalogo tem texto no SS5.2.
  4. FORCA       — o requisito pega os dois degraus de cima de cada escada, e
                   nenhum passa do teto da criacao da PECA 2.
  5. TETO        — o teto de Defesa e DERIVADO de tres donos e nunca lido de uma
                   constante, com busca exaustiva provando o invariante da peca.
  6. BALDES      — os dois baldes de treino tem as duas maos e o mesmo teto, e o
                   simples sobrevive ao requisito de Forca.
  7. TALHA       — nenhuma arma depende so da Talha, que e regra opcional.
  8. VERSATIL    — so as armas declaradas carregam o passo de graca.
  9. DESLIGA     — a frase do desligamento nao cita escudo em nenhum dos tres.
 10. TRIAGEM     — todo nome do catalogo aparece no documento que o define.
 11. SOCO        — o punho vazio do SS5.0.6 nunca passa do fundo de uma mao, fecha
                   EXATO no topo da maestria, e nao entra na contagem das 52.

Roda de sistema/03-mecanica/. NAO le o .docx e NAO precisa de python-docx —
entao nao existe caminho por onde ele saia verde tendo pulado checagem.
"""
import os, re, sys
from itertools import permutations

AQUI = os.path.dirname(os.path.abspath(__file__))
def ler(nome):
    with open(os.path.join(AQUI, nome), encoding='utf-8') as f:
        return f.read()

def sem_acento(t):
    import unicodedata
    return ''.join(c for c in unicodedata.normalize('NFD', t)
                   if unicodedata.category(c) != 'Mn').lower()

ERROS = []
AVISOS = []
def aviso(msg): AVISOS.append(msg)
def erro(msg): ERROS.append(msg)
def bloco(t): print('\n' + '=' * 88 + f'\n{t}\n' + '=' * 88)

EQ = ler('14-equipamento.md')
P1 = ler('01-atributos-acerto-defesa.md')
P2 = ler('02-economia-de-atributos.md')
P8 = ler('08-criacao-de-personagem.md')
P11 = ler('11-aptidoes-e-refino.md')

# ------------------------------------------------------------ LIMITES DE DESIGN
# Declarados aqui, a parte da regra aplicada. Sao DECISOES REGISTRADAS, cada uma
# com o lugar onde o argumento dela mora. Perturbar qualquer um deles tem de
# acender a checagem correspondente — e nunca a mesma que le o valor do documento.
DOMINANCIA_ACEITA = {              # SS5.2: Versatil a custo zero, 0,1 ponto no nv2
    ('Espada Longa', 'Machete'),
    ('Espada Longa', 'Machado'),
    # v0.335: ('Taco', 'Wakizashi') saiu. O Taco trocou `Oculta` por `Discreta` e a
    # Wakizashi ganhou `Leve`, e nenhuma das duas cobre mais a outra (SS5.2).
}
VERSATIL_DECLARADAS = {'Katana', 'Espada Longa', 'Taco', 'Bastão'}   # SS8 item 17
# SS5.2: a divida da v0.45 manda o validador acusar quem depender so da Talha.
# Estas duas sao DECISAO DO MIZUKI na v0.48, com argumento escrito no SS5.2: a maca
# e o kanabo SAO as armas anti-guarda, entao a Talha nelas e identidade e nao enfeite.
# Uma TERCEIRA arma que dependa so dela falha.
#
# v0.143 — A PERGUNTA DESTA CHECAGEM MUDOU, e ela nao morreu junto com a divida.
# Ela nasceu perguntando "alguma arma depende so de uma regra que a mesa pode
# desligar?". O Bloquear virou a peca 23 e deixou de ser opcional, entao essa
# pergunta acabou. A que fica e' a que sempre importou por baixo dela: uma arma
# cuja identidade paga inteira e' `-1` num numero alheio e' uma arma sem
# identidade propria — e isso vale com o Bloquear ligado do mesmo jeito.
# A geometria do Bloquear e' do `conferir-bloquear.py`; aqui so mora o
# orcamento de arma.
SO_TALHA_ACEITA = {'Maça', 'Kanabō'}
MEDIA_DADO = {'d4': 2.5, 'd6': 3.5, 'd8': 4.5, 'd10': 5.5, 'd12': 6.5,
              '1d8': 4.5, '1d10': 5.5, '2d6': 7.0, '2d8': 9.0, '2d10': 11.0}
PISO_MELEE = 2.5     # o d4, SS5.0
FORCA_MELEE = 6.0    # a Forca que o corpo a corpo soma, SS5.2
RESTRICOES = {'volumosa', 'embainhada', 'comprida'}
GRATIS = {'municao', 'versatil', 'leve'}   # SS5.2: Versatil custa 0, Municao e textura;
# v0.335: Leve e' marca de manejo da candidata, e o preco mora no Caminho que a pede

# ------------------------------------------------------------------ LEITURA
def fundo_corpo():
    m = re.search(r'\*\*uma mão\*\* \(fundo (\d+)\).*?\*\*duas mãos\*\* \(fundo (\d+)\)', EQ)
    if not m: erro('SS5.0.1: nao achei o fundo do corpo a corpo na tabela'); return None
    return int(m.group(1)), int(m.group(2))

def fundo_tiro():
    m = re.search(r'fundo:\s*(\d+) numa mão,\s*(\d+) em duas', EQ)
    if not m: erro('SS5.0.5: nao achei o fundo do tiro'); return None
    return int(m.group(1)), int(m.group(2))

def escada_tiro():
    m = re.search(r'(1d10 · 2d6 · 2d8 · 2d10)\s*=\s*([\d · ]+)', EQ)
    if not m: erro('SS5.0.5: nao achei a escada do tiro'); return None
    dados = [d.strip() for d in m.group(1).split('·')]
    custos = [int(c.strip()) for c in m.group(2).split('·')]
    return dict(zip(dados, custos))

def catalogo():
    ini = EQ.index('## 5.3 As 52 armas'); fim = EQ.index('## 5.4 Treino de arma')
    armas, cat, modo = [], None, 'corpo'
    for linha in EQ[ini:fim].split('\n'):
        s = linha.strip()
        m = re.fullmatch(r'\*\*(.+?)\*\*', s)
        if m and 'assinatura' not in m.group(1) and 'Zero' not in m.group(1):
            if m.group(1).startswith('As de tiro'): modo = 'tiro'
            else: cat = m.group(1)
            continue
        if s.startswith('**As de tiro'): modo = 'tiro'; continue
        if not s.startswith('|'): continue
        c = [x.strip() for x in s.strip('|').split('|')]
        if not c or c[0] in ('arma', '') or set(c[0]) <= set('-: '): continue
        if modo == 'corpo' and len(c) >= 5:
            armas.append(dict(nome=c[0], categoria=cat, maos=int(c[1]),
                              dado=c[2].strip('* '), atributo='Forca',
                              props=[p.strip(' `') for p in c[3].split('·')]))
        elif modo == 'tiro' and len(c) >= 6:
            armas.append(dict(nome=c[0], categoria=c[1], maos=int(c[2]),
                              dado=c[3].strip('* '), atributo=c[4],
                              props=[p.strip(' `') for p in c[5].split('·')]))
    return armas

FC, FT, ESC_T, ARMAS = fundo_corpo(), fundo_tiro(), escada_tiro(), catalogo()
if not all([FC, FT, ESC_T]) or not ARMAS:
    print('\n>>> FALHOU: nao consegui ler a regua do documento. Nada abaixo vale.')
    sys.exit(1)
CORPO = [a for a in ARMAS if a['atributo'] == 'Forca']
TIRO = [a for a in ARMAS if a['atributo'] != 'Forca']

def pagas(a):
    return [p for p in a['props']
            if sem_acento(p) not in RESTRICOES and sem_acento(p) not in GRATIS]
def restr(a): return [p for p in a['props'] if sem_acento(p) in RESTRICOES]
def custo_dado(a):
    if a['atributo'] == 'Forca':
        return MEDIA_DADO[a['dado']] - PISO_MELEE
    if a['atributo'] == 'Destreza':
        return max(0.0, MEDIA_DADO[a['dado']] + FORCA_MELEE - PISO_MELEE - FORCA_MELEE)
    return float(ESC_T[a['dado']])
def gasto(a): return custo_dado(a) + len(pagas(a)) - len(restr(a))
def fundo(a):
    f = FC if a['atributo'] == 'Forca' else FT
    return f[0] if a['maos'] == 1 else f[1]

# -------------------------------------------------------------- 1. ORCAMENTO
bloco('1. ORCAMENTO — toda arma gasta o fundo exato')
fora = [(a['nome'], gasto(a), fundo(a)) for a in ARMAS if abs(gasto(a) - fundo(a)) > 0.01]
for n, g, f in fora:
    erro(f'{n} gasta {g:g} de um fundo {f} — ' +
         ('vaga vazia e dominancia estrita' if g < f else 'estoura o orcamento'))
print(f'  {len(ARMAS)} armas, {len(CORPO)} de corpo a corpo (fundo {FC[0]}/{FC[1]}) '
      f'e {len(TIRO)} de tiro (fundo {FT[0]}/{FT[1]}).')
print(f'  {len(ARMAS)-len(fora)} fecham exato.' if not fora else f'  {len(fora)} fora do fundo.')

# ------------------------------------------------------------- 2. DOMINANCIA
bloco('2. DOMINANCIA — a matriz sobre arma, uma vez por escada')
def domina(x, y):
    if x['maos'] != y['maos'] or x['atributo'] != y['atributo']: return False
    if MEDIA_DADO[x['dado']] < MEDIA_DADO[y['dado']]: return False
    px = {sem_acento(p) for p in x['props']} - RESTRICOES
    py = {sem_acento(p) for p in y['props']} - RESTRICOES
    rx = {sem_acento(p) for p in restr(x)}; ry = {sem_acento(p) for p in restr(y)}
    if not px >= py or not rx <= ry: return False
    return (MEDIA_DADO[x['dado']] > MEDIA_DADO[y['dado']] or px > py or rx < ry)
for grupo, nome in ((CORPO, 'corpo a corpo'), (TIRO, 'tiro')):
    achadas = {(x['nome'], y['nome']) for x, y in permutations(grupo, 2) if domina(x, y)}
    novas = achadas - DOMINANCIA_ACEITA
    sumidas = (DOMINANCIA_ACEITA & {(x['nome'], y['nome'])
               for x, y in permutations(grupo, 2)}) - achadas
    pares = len(grupo) * (len(grupo) - 1)
    print(f'  {nome}: {pares} pares, {len(achadas)} dominancia(s), '
          f'{len(achadas & DOMINANCIA_ACEITA)} declarada(s) como ACEITA.')
    for x, y in sorted(novas):
        erro(f'dominancia NOVA no {nome}: {x} domina {y}, e ela nao esta declarada')
    for x, y in sorted(sumidas):
        erro(f'a dominancia ACEITA {x} > {y} sumiu — se ela foi consertada, '
             'tire-a do bloco LIMITES DE DESIGN em vez de deixar a declaracao mentindo')

# ------------------------------------------------------------ 3. PROPRIEDADE
bloco('3. PROPRIEDADE — toda propriedade usada tem texto no SS5.2')
# as propriedades pagas moram no SS5.2; as restricoes moram no SS5.0.4
texto_def = (EQ[EQ.index('### 5.0.4 A restrição devolve'):EQ.index('## 5.1 A categoria')]
             + EQ[EQ.index('## 5.2 As propriedades'):EQ.index('## 5.3 As 52 armas')])
alvo = sem_acento(texto_def)
usadas = sorted({p for a in ARMAS for p in a['props']})
sem_texto = [p for p in usadas
             if not re.search(r'\*\*`?' + re.escape(sem_acento(p)) + r'`?\*\*|`'
                              + re.escape(sem_acento(p)) + r'`', alvo)]
print(f'  {len(usadas)} propriedades em uso no catalogo.')
for p in sem_texto:
    erro(f'a propriedade "{p}" e usada no SS5.3 e nao tem texto no SS5.2 — '
         'propriedade sem numero faz a matriz sair INCONCLUSIVO em silencio')
if not sem_texto: print('  Todas com texto.')

# ------------------------------------------------------------------ 4. FORCA
bloco('4. FORCA — o requisito pega os dois degraus de cima de cada escada')
m = re.search(r'\| 3 \| bom, e é o teto da criação \|', P2)
if not m: erro('PECA 2: nao achei a linha que declara o teto da criacao')
TETO_CRIACAO = 3
m = re.search(r'`Força (\d+)` para os dois degraus de cima', EQ)
REQ = int(m.group(1)) if m else erro('SS5.5: nao achei o requisito de Forca')
if REQ and REQ > TETO_CRIACAO:
    erro(f'o requisito de arma pede Forca {REQ} e o teto da criacao e {TETO_CRIACAO} — '
         'isso deixa de ser acesso e vira preco em ponto de marco, sem decisao escrita')
def escada_de(grupo):
    return sorted({a['dado'] for a in grupo}, key=lambda d: MEDIA_DADO[d])
# tres familias de preco, nao duas: quem soma Forca, quem soma Destreza, quem nao soma
FAM = {'Forca': [a for a in CORPO],
       'Destreza': [a for a in TIRO if a['atributo'] == 'Destreza'],
       'nenhuma': [a for a in TIRO if a['atributo'] == 'nenhuma']}
gate = set()
for nome_fam, grupo in FAM.items():
    if not grupo: continue
    esc = escada_de(grupo)
    topo = set(esc[-2:]) if nome_fam != 'Destreza' else set()
    print(f'  familia {nome_fam:9s}: {" · ".join(esc)}' +
          (f' — gate em {sorted(topo)}' if topo else ' — sem gate: paga em Destreza'))
    gate |= {a['nome'] for a in grupo if a['dado'] in topo}
    topo_c = set(escada_de(CORPO)[-2:])
print(f'  o requisito pega {len(gate)} de {len(ARMAS)} armas.')
dex_gate = [a['nome'] for a in ARMAS if a['nome'] in gate and
            ('fineza' in {sem_acento(p) for p in a['props']} or a['atributo'] == 'Destreza')]
for n in dex_gate:
    erro(f'{n} paga em Destreza e cai no requisito de Forca — o gate estaria cobrando '
         'Forca de quem trocou Forca por Destreza')
if not dex_gate:
    print('  Nenhuma arma de Destreza cai no requisito, nas tres familias.')
m = re.search(r'\*\*Dezesseis de 52\.\*\*|Dezesseis de 52', EQ)
if m and len(gate) != 16:
    erro(f'o SS5.5 escreve "Dezesseis de 52" e o catalogo gateia {len(gate)} — '
         'um numero se moveu debaixo da frase')
# v0.335: a Espingarda e o Rifle pedem Forca 1 desde a v0.176 (revisao do Word), e a
# peca so' acompanhou na migracao da candidata. O degrau de cada arma sai da coluna
# "Força" da candidata, e as duas excecoes tem de estar NOMEADAS na nota do SS5.5 —
# assim a regra da peca e a tabela do livro nao se desencontram de novo em silencio.
_s55 = EQ[EQ.index('## 5.5 O requisito de Força'):EQ.index('### Por que o tiro entra')]
_mx = re.search(r'pede[mn]? `Força (\d+)`', _s55)
# v0.346: o capitulo de Equipamento e' lido do R41, pelo livro.py, como os outros. Ate a
# v0.345 esta checagem e a 15 abriam o manuscrito da candidata direto.
import livro as _livro_eq
_forca = {}
try:
    _ct = _livro_eq.texto('equipamento')
except _livro_eq.LivroMudou:
    _ct = ''
if _ct:
    for _l in _ct[_ct.index('# Lâminas'):_ct.index('# Itens comuns')].splitlines():
        _c = [x.strip() for x in _l.strip().strip('|').split('|')] if _l.startswith('|') else []
        if len(_c) == 7 and _c[0] != 'Arma' and not set(_c[0]) <= set('-: '):
            _forca[re.sub(r'\s*\(.*\)', '', _c[0]).strip()] = _c[4]
if len(_forca) != 52:
    erro(f'5.5: li {len(_forca)} linhas de Forca na candidata, e sao 52')
elif not _mx:
    erro('5.5: a nota da v0.335 nao diz mais qual Forca as excecoes pedem')
else:
    _f3 = {n for n, v in _forca.items() if v == '3'}
    _fx = {n for n, v in _forca.items() if v == _mx.group(1)}
    _excecao = gate - _f3
    if _excecao != _fx:
        erro(f'5.5: a regra da peca menos a coluna da candidata da {sorted(_excecao)}, e a '
             f'candidata pede Forca {_mx.group(1)} de {sorted(_fx)}')
    elif _f3 - gate:
        erro(f'5.5: a candidata pede Forca 3 de {sorted(_f3 - gate)}, que a regra nao gateia')
    else:
        _nao_nomeada = [n for n in sorted(_excecao) if f'**{n}**' not in _s55 and f'a {n}' not in _s55
                        and f'o {n}' not in _s55]
        if _nao_nomeada:
            erro(f'5.5: a excecao {_nao_nomeada} nao esta nomeada na nota da v0.335')
        _m14 = re.search(r'pega hoje (\d+) de 52', _s55)
        if not _m14 or int(_m14.group(1)) != len(_f3):
            erro(f'5.5: a nota publica {_m14.group(1) if _m14 else "?"} de 52 no Forca 3, '
                 f'e a candidata tem {len(_f3)}')
        else:
            print(f'  [x] Forca 3 em {len(_f3)} de 52; {sorted(_excecao)} em Forca {_mx.group(1)}, '
                  'como a candidata publica.')

# ------------------------------------------------------------------- 5. TETO
bloco('5. TETO DE DEFESA — derivado de tres donos, nunca lido de constante')
m = re.search(r'Defesa\s*=\s*(\d+) \+ Destreza \+ proteção', P1)
BASE = int(m.group(1)) if m else erro('PECA 1: nao achei a formula da Defesa')
m = re.search(r'\*\*Teto do atributo: (\d+)\.\*\* Teto do refino: (\d+)\.', P2)
TETO_ATR, TETO_REF = (int(m.group(1)), int(m.group(2))) if m else (None, None)
if TETO_ATR is None: erro('PECA 2: nao achei os tetos de atributo e de refino')
m = re.search(r'a sua proteção é `1/(\d+) do refino \+ (\d+)`', P11)
DIV, MAIS = (int(m.group(1)), int(m.group(2))) if m else (None, None)
if DIV is None: erro('PECA 11: nao achei a formula de cobrir-se')
if None not in (BASE, TETO_ATR, TETO_REF, DIV, MAIS):
    cobrir = lambda r: r // DIV + MAIS
    TETO_LIVRE = BASE + TETO_ATR + cobrir(TETO_REF)
    print(f'  {BASE} (peca 1) + {TETO_ATR} (peca 2) + {cobrir(TETO_REF)} '
          f'(peca 11: 1/{DIV} de {TETO_REF} + {MAIS}) = {TETO_LIVRE}')
    if re.search(r'teto de Defesa (?:é|e) \*?\*?%d' % TETO_LIVRE, EQ):
        erro(f'o numero {TETO_LIVRE} esta ESCRITO no rascunho — ele e derivado e '
             'escreve-lo cria a segunda fonte, que e a licao no 9')
    def tabela(sec_ini, sec_fim, ncols):
        ini = EQ.index(sec_ini); fim = EQ.index(sec_fim)
        out = []
        for l in EQ[ini:fim].split('\n'):
            c = [x.strip(' *`') for x in l.strip().strip('|').split('|')]
            if len(c) >= ncols and re.fullmatch(r'\d', c[0]): out.append(c)
        return out
    unis = tabela('## 3. A escada', '### A coluna de Força', 7)
    escs = tabela('### Então: proteção, com requisito de Força e teto de Destreza',
                  '### O que isso NÃO conserta', 5)
    def num(x): return None if x in ('—', '-', '') else int(re.sub(r'\D', '', x) or 0)
    rotas = [('cobrir-se', cobrir(TETO_REF), None)]
    for c in unis:
        rotas.append((f'Traje {c[0]}', num(c[1]), num(c[2])))
        rotas.append((f'Revestimento {c[0]}', num(c[4]), num(c[5])))
    escudos = [('sem escudo', 0, None)] + [(f'escudo {c[0]}', num(c[1]), num(c[2])) for c in escs]
    print(f'  busca exaustiva: {len(rotas)} rotas de protecao x {len(escudos)} escudos '
          f'x {TETO_ATR+1} Destrezas = {len(rotas)*len(escudos)*(TETO_ATR+1)} montagens')
    pico, quem = 0, None
    for rn, rp, rt in rotas:
        for en, ep, et in escudos:
            tetos = [t for t in (rt, et) if t is not None]
            for dex in range(TETO_ATR + 1):
                d = BASE + min([dex] + tetos) + (rp or 0) + (ep or 0)
                if d > pico: pico, quem = d, f'{rn} + {en}, Destreza {dex}'
                if rn != 'cobrir-se' and d > TETO_LIVRE:
                    erro(f'{rn} + {en} com Destreza {dex} da Defesa {d}, acima dos '
                         f'{TETO_LIVRE} que a rota sem equipamento alcanca — '
                         'quebra o invariante que esta peca e dona')
    print(f'  pico da busca: {pico} ({quem}) — e o teto derivado e {TETO_LIVRE}.')
    if pico > TETO_LIVRE:
        erro(f'alguma montagem chega a {pico} e o teto derivado e {TETO_LIVRE}')

# ----------------------------------------------------------------- 6. BALDES
bloco('6. BALDES — os dois lados do treino de arma')
m = re.search(r'\*\*Simples — \d+ armas, \d+ categorias:\*\* (.+)', EQ)
n = re.search(r'\*\*Marciais — \d+ armas, \d+ categorias:\*\* (.+)', EQ)
if not (m and n):
    erro('SS5.4.1: nao achei os dois baldes')
else:
    simples = {x.strip(' `') for x in m.group(1).split('·')}
    marcial = {x.strip(' `') for x in n.group(1).split('·')}
    simples = {sem_acento(x) for x in simples}
    marcial = {sem_acento(x) for x in marcial}
    cats = {sem_acento(a['categoria']) for a in CORPO}
    falta = cats - simples - marcial
    for c in falta: erro(f'a categoria "{c}" nao esta em nenhum dos dois baldes')
    sm = [a for a in CORPO if sem_acento(a['categoria']) in simples]
    mc = [a for a in CORPO if sem_acento(a['categoria']) in marcial]
    def teto1(g): return max([MEDIA_DADO[a['dado']] for a in g if a['maos'] == 1] or [0])
    def teto2(g):
        v = [MEDIA_DADO[a['dado']] for a in g if a['maos'] == 2]
        v += [MEDIA_DADO[a['dado']] + 1.0 for a in g if a['maos'] == 1 and 'versatil' in {sem_acento(p) for p in a['props']}]
        return max(v or [0])
    print(f'  simples {len(sm)} armas / marcial {len(mc)} armas')
    for g, nm in ((sm, 'simples'), (mc, 'marcial')):
        if not any(a['maos'] == 1 for a in g): erro(f'o balde {nm} nao tem arma de uma mao')
        if not any(a['maos'] == 2 for a in g): erro(f'o balde {nm} nao tem arma de duas maos')
    if teto1(sm) != teto1(mc):
        erro(f'os baldes nao empatam numa mao: simples {teto1(sm)} contra marcial {teto1(mc)} '
             '— a divisao passou a restringir PODER e nao identidade')
    if teto2(sm) != teto2(mc):
        erro(f'os baldes nao empatam em duas maos: simples {teto2(sm)} contra marcial {teto2(mc)}')
    print(f'  teto: 1 mao {teto1(sm)} = {teto1(mc)} | 2 maos {teto2(sm)} = {teto2(mc)}')
    livres2 = [a for a in sm if a['maos'] == 2 and a['dado'] not in topo_c]
    if not livres2:
        erro('sob o requisito de Forca o balde simples fica sem arma de duas maos — '
             'os dois gates se multiplicam e o Caminho nao-marcial perde uma economia de mao')
    print(f'  sob o requisito de Forca, o simples mantem {len(livres2)} arma(s) de duas maos.')

# ------------------------------------------------------------------ 7. TALHA
bloco('7. TALHA — ela nao pode ser a unica identidade paga de uma arma')
so_talha = {a['nome'] for a in ARMAS if [sem_acento(x) for x in pagas(a)] == ['talha']}
for n in sorted(so_talha - SO_TALHA_ACEITA):
    erro(f'{n} tem a Talha como unica propriedade paga e nao esta declarada — a '
         'identidade inteira dela seria -1 no Bloquear de outra pessoa, e isso nao '
         'e identidade de arma (v0.143: o motivo antigo era o Bloquear ser opcional, '
         'e ele deixou de ser)')
for n in sorted(SO_TALHA_ACEITA - so_talha):
    erro(f'{n} esta declarada como so-Talha e nao e mais — tire da declaracao')
n_talha = sum(1 for a in ARMAS if 'talha' in {sem_acento(p) for p in a['props']})
print(f'  {n_talha} armas com Talha, {len(so_talha)} dependendo so dela '
      f'({len(SO_TALHA_ACEITA)} declarada(s)).')

# --------------------------------------------------------------- 8. VERSATIL
bloco('8. VERSATIL — o passo de graca so nas armas declaradas')
tem = {a['nome'] for a in ARMAS if 'versatil' in {sem_acento(p) for p in a['props']}}
for n in sorted(tem - VERSATIL_DECLARADAS):
    erro(f'{n} carrega Versatil e nao esta declarada — a propriedade custa zero, '
         'entao quem a carrega e estritamente melhor que a arma identica sem ela. '
         'A condicao que segura isso e de ficcao e ainda nao esta escrita (SS8 item 17)')
for n in sorted(VERSATIL_DECLARADAS - tem):
    erro(f'{n} esta declarada com Versatil e nao a tem mais no catalogo')
print(f'  {len(tem)} armas com Versatil, todas declaradas.' if not (tem ^ VERSATIL_DECLARADAS)
      else f'  {len(tem)} no catalogo contra {len(VERSATIL_DECLARADAS)} declaradas.')

# --------------------------------------------------------------- 9. DESLIGA
bloco('9. DESLIGA — a frase do desligamento nao cita escudo')
for nome, txt in (('peca 8', P8), ('peca 11', P11)):
    for m2 in re.finditer(r'[^.\n]*deslig[^.\n]*', txt):
        f = m2.group(0)
        if 'escudo' in f.lower() and 'sa' not in f.lower()[:f.lower().find('escudo')][-4:] \
           and 'soma' not in f.lower() and 'saiu' not in f.lower():
            erro(f'{nome}: a frase do desligamento ainda cita escudo — '
                 f'"{f.strip()[:90]}..."')
print('  peca 8 e peca 11 conferidas.')

# --------------------------------------------------------------- 10. TRIAGEM
bloco('10. TRIAGEM — todo nome do catalogo aparece no documento que o define')
EQ_SA = sem_acento(EQ)
for a in ARMAS:
    n_sa = sem_acento(a['nome'])
    if EQ_SA.count(n_sa) < 2:
        erro(f'a arma "{a["nome"]}" aparece uma vez so no rascunho — '
             'ela esta no catalogo e em lugar nenhum do argumento')
    elif EQ.count(a['nome']) < 2:
        erro(f'"{a["nome"]}" e escrita de um jeito na tabela do SS5.3 e de outro na prosa — '
             'o conferir-nomes.py compara literal e nao veria uma colisao neste nome')
print(f'  {len(ARMAS)} nomes de arma conferidos contra o corpo do documento.')

# ------------------------------------------------------------------- 11. SOCO
bloco('11. SOCO — o punho vazio nunca passa do fundo, e fecha exato no topo')
#
# Entrou na v0.74. O soco e a unica entrada do sistema sem categoria e sem
# propriedade, e o que o segura NAO e' uma constante escrita aqui: e' a mesma
# conta do bloco 1, com zero propriedade. O dado sai da tabela do SS5.0.6, o
# custo de cada dado sai do MEDIA_DADO/PISO_MELEE que o SS5.0 ja definia, e as
# faixas de maestria saem da PECA 1. Nada e' guardado.
#
# AS DUAS METADES, e elas TEM de ser conferidas separadas (licao no 8):
#   a) nenhuma maestria passa do fundo   -> perturbar d10 para d12 acende
#   b) a ULTIMA maestria fecha EXATO     -> perturbar d10 para d8 acende
# So a (a) sairia verde com o soco parado no d4 a campanha inteira, que e' o
# desenho que esta secao existe para nao deixar acontecer.
try:
    _sec = EQ[EQ.index('### 5.0.6 O soco'):EQ.index('## 5.1 A categoria')]
except ValueError:
    _sec = ''
    erro('SS5.0.6: a secao do soco sumiu da peca 14 — esta checagem parou de conferir')

if _sec:
    ESCADA_SOCO = {int(m.group(1)): 'd' + m.group(2)
                   for m in re.finditer(r'\|\s*(\d)\s*\|\s*\d+ a \d+\s*\|\s*\*\*d(\d+)\*\*\s*\|', _sec)}
    # as faixas de maestria sao da PECA 1, e o soco nao pode inventar as proprias
    FAIXAS_P1 = re.search(r'\| nível \| ([\d–\-–]+) \| ([\d–\-–]+) \| ([\d–\-–]+) \| ([\d–\-–]+) \|', P1)
    n_maestrias = len(FAIXAS_P1.groups()) if FAIXAS_P1 else 0
    if not FAIXAS_P1:
        erro('PECA 1: nao achei a tabela de faixas de maestria — o soco ficaria sem ancora')
    elif len(ESCADA_SOCO) != n_maestrias:
        erro(f'o soco declara {len(ESCADA_SOCO)} degraus e a PECA 1 tem {n_maestrias} '
             f'faixas de maestria — um degrau sem faixa e uma faixa sem dado')
    if not ESCADA_SOCO:
        erro('SS5.0.6: nao consegui ler a tabela de maestria -> dado do soco')

    FUNDO_1MAO = FC[0]
    print(f'  fundo de uma mao: {FUNDO_1MAO} (lido do SS5.0.1) · zero propriedade custa 0')
    print(f"  {'maestria':<10}{'dado':<7}{'gasta':<8}{'fundo':<8}sobra")
    topo_exato = None
    for m in sorted(ESCADA_SOCO):
        d = ESCADA_SOCO[m]
        if d not in MEDIA_DADO:
            erro(f'o soco usa o dado {d} na maestria {m}, e ele nao esta na escada do SS5.0')
            continue
        g = MEDIA_DADO[d] - PISO_MELEE          # zero propriedade paga, zero restricao
        sobra = FUNDO_1MAO - g
        print(f'  {m:<10}{d:<7}{g:<8g}{FUNDO_1MAO:<8}{sobra:+g}')
        if g > FUNDO_1MAO + 0.01:
            erro(f'o soco na maestria {m} gasta {g:g} de um fundo {FUNDO_1MAO} — ele passa a '
                 f'dominar arma de uma mao sem pagar propriedade nenhuma, e nao existe '
                 f'segunda mao para ele vender')
        topo_exato = abs(sobra) < 0.01
    if ESCADA_SOCO and topo_exato is False:
        erro(f'o soco no topo da maestria gasta {MEDIA_DADO[ESCADA_SOCO[max(ESCADA_SOCO)]] - PISO_MELEE:g} '
             f'de um fundo {FUNDO_1MAO} — ele nunca chega a paridade, e ai socar e sempre a '
             f'escolha ruim. A metade (a) desta checagem sairia VERDE assim')
    elif ESCADA_SOCO:
        print('  O topo fecha exato: o soco chega a paridade com arma de uma mao e nao passa.')

    # e ele nao pode estar no catalogo, senao a contagem das 52 anda sozinha
    if any(sem_acento(a['nome']) in ('soco', 'punho', 'desarmado') for a in ARMAS):
        erro('o soco entrou no catalogo do SS5.3 — ele nao e uma das 52, e por na tabela '
             'move a contagem que tres documentos publicam')
    else:
        print(f'  E ele esta FORA do SS5.3: as {len(ARMAS)} do catalogo nao se moveram.')

    # a isencao do requisito de Forca tem de estar escrita, senao o SS5.5 pega o d10
    if 'isento' not in sem_acento(_sec):
        erro('SS5.0.6: o soco chega ao dado que o requisito de Forca gateia e a isencao '
             'nao esta escrita — o SS5.5 le o dado impresso e pegaria ele no nivel 26')
    else:
        print('  A isencao do requisito de Forca esta escrita.')

# --------------------------------------------------- 12. TREINO POR CAMINHO
bloco('12. TREINO POR CAMINHO — quem alcanca qual balde, lido da peca 6')
#
# Entrou na v0.130. A regra existia desde a v0.106 e morava SO no PDF do livro,
# que e' artefato: a peca 14 SS5.4 ja dizia que o eixo de acesso e' o Caminho, e
# QUAL Caminho pega o que nao estava escrito em peca nenhuma.
#
# NADA e' guardado aqui: os nomes de Caminho saem da peca 6 SS1, a tabela de
# treino sai da peca 6 SS8.0, e cada categoria nomeada e' conferida contra a
# peca 14, que e' a dona do catalogo.
#
# AS DUAS METADES, conferidas separadas (licao no 8):
#   a) toda categoria nomeada EXISTE na peca 14
#   b) os CINCO Caminhos aparecem na tabela
# So a (a) sairia verde com um Caminho faltando; so a (b) sairia verde com uma
# categoria inventada.
P6 = ler('06-caminhos-e-trilhas.md')
CAMINHOS_5 = ['Bastião', 'Vanguarda', 'Guia', 'Emanador', 'Evocador', 'Incursor']

try:
    _s8 = P6[P6.index('### 8.0 Qual Caminho treina'):P6.index('### 8.1')]
except ValueError:
    _s8 = ''
    erro('PECA 6 SS8.0: a secao de treino por Caminho sumiu — esta checagem parou de conferir')

if _s8:
    _linhas = [l for l in _s8.splitlines()
               if l.startswith('|') and '---' not in l and 'treina' not in l]
    if not _linhas:
        erro('PECA 6 SS8.0: a tabela de treino sumiu da secao — extrator sem nada para ler')

    _vistos, _cats = [], []
    for _l in _linhas:
        _c = [x.strip() for x in _l.strip().strip('|').split('|')]
        if len(_c) < 3:
            continue
        _quem = [x for x in CAMINHOS_5 if x in _c[0]]
        _vistos += _quem
        # categoria nomeada = o que vem entre crases na ultima coluna
        _n = re.findall(r'`([^`]+)`', _c[2])
        _cats += _n
        _quanto = 'as treze' if 'treze' in _c[1] else (', '.join(_n) or _c[1])
        print(f'  {" · ".join(_quem):<24} {_quanto}')

    # (a) toda categoria nomeada existe na peca 14
    for _n in sorted(set(_cats)):
        if _n not in EQ:
            erro(f'PECA 6 SS8.0: o treino cita a categoria "{_n}", que nao existe na peca 14')
    if _cats:
        print(f'  {len(set(_cats))} categoria(s) nomeada(s), todas conferidas contra a peca 14.')

    # (b) os cinco estao cobertos
    _faltam = [c for c in CAMINHOS_5 if c not in _vistos]
    if _faltam:
        erro(f'PECA 6 SS8.0: {", ".join(_faltam)} nao aparece na tabela de treino — '
             'Caminho sem balde declarado e o buraco que esta secao existe para fechar')
    else:
        print(f'  Os {len(CAMINHOS_5)} Caminhos aparecem na tabela.')

    # a porta da Trilha, senao o conjurador fica trancado fora do marcial
    # v0.270: a porta mudou de Trilha com a colecao v0.4 — era a `Empunhadura` do
    # `Arremate`, e hoje e' a `Arma Condutora` do Condutor Armado, com o mesmo efeito.
    # A checagem segue a porta viva, e o livro tem de nomear a mesma.
    if 'Arma Condutora' not in _s8:
        erro('PECA 6 SS8.0: a porta da Trilha nao esta escrita — sem ela o conjurador '
             'que quer arma marcial nao tem rota nenhuma')
    else:
        print('  A porta da Trilha (`Arma Condutora` do Condutor Armado) esta escrita.')

    # o livro e COPIA desta regra, e copia sem comparacao diverge (licao no 9)
    _LIVRO = os.path.join(AQUI, '..', '05-material', 'livro', 'manual',
                          '35-caminhos-e-trilhas.md')
    if os.path.exists(_LIVRO):
        # compara SEM crase: a peca marca categoria com `` e o livro nem sempre.
        # A regra e' a mesma; a notacao e' que difere, e comparar literal daria
        # falso positivo — foi o que aconteceu ao escrever esta checagem.
        _lv = re.sub(r'`', '', open(_LIVRO, encoding='utf-8').read())
        _bateu = 0
        for _frase, _que in (('treinam as treze categorias', 'os dois marciais'),
                             ('treinam Arma de Fogo e Balestra', 'os conjuradores'),
                             ('Arma Condutora', 'a porta da Trilha')):
            if _frase in _lv:
                _bateu += 1
            else:
                erro(f'LIVRO cap. 8: a linha de treino de {_que} nao bate com a peca 6 SS8.0')
        if _bateu == 3:
            print('  O livro repete a mesma regra, conferido nas tres linhas.')
    else:
        aviso('nao achei o capitulo 8 do livro — a copia dele nao foi conferida')


# --------------------------------------------------------------- 13. O DINHEIRO
# O capitulo de equipamento tambem precisa incluir todo o catalogo atual.
# Cada frase de treino deve citar os Caminhos do balde correspondente na peca 6.
_eq_livro = os.path.join(AQUI, '../05-material/livro/manual/50-equipamento.md')
if os.path.exists(_eq_livro):
    _eq_texto = open(_eq_livro, encoding='utf-8').read()
    _frases = re.findall(r'(?m)^> \*\*([^*]+treinam[^*]+)\*\*', _eq_texto)
    for _linha in _s8.splitlines():
        if not _linha.startswith('| '):
            continue
        _cel = [c.strip().replace('**', '') for c in _linha.strip('|').split('|')]
        if len(_cel) < 3:
            continue
        _quem = [c for c in CAMINHOS_5 if c in _cel[0]]
        _grupo = 'treze categorias' if 'treze' in _cel[1] else 'Arma de Fogo e Balestra'
        for _nome in _quem:
            if not any(_nome in _frase and _grupo in _frase for _frase in _frases):
                erro(f'LIVRO cap. 15: a frase de treino omite {_nome} ou seu grupo de armas')

# -- 12.1: o ponteiro para o catalogo, no comeco de cada Caminho. ------------
# A tabela `Caracteristicas de <X>` diz em que armas o Caminho treina, e nao diz
# que a arma se COMPRA. O capitulo 6 ja escrevia a frase certa — "o Caminho te
# treina numa lista de armas; ele nao te da a arma" — e ela morava so la, longe
# de quem abre o livro num Caminho. Mesmo defeito da v0.209 nas Origens, mesma
# forma de conserto: a linha entra no ponto de uso.
#
# O ponteiro NAO repete o fundo da criacao. O `¥150.000` ja mora no capitulo 6 e
# no 14, e uma terceira copia seria a licao no 9 de graca — a linha aponta e o
# numero fica com quem ja e dono dele. O numero do capitulo citado e conferido
# pela checagem 10.3 do conferir-repositorio.py, que le a lista do build.py.
bloco('12.1 PONTEIRO DE EQUIPAMENTO — os Caminhos da edicao jogavel mandam o leitor comprar')
if not os.path.exists(_LIVRO):
    erro('12.1: nao achei o capitulo de Caminhos do livro')
else:
    _tc = open(_LIVRO, encoding='utf-8').read()
    _caminhos = re.findall(r'^## ([^\n]+)\n(.*?)(?=^## |\Z)', _tc, re.S | re.M)
    _com_tab = [(n, c) for n, c in _caminhos if 'Características do' in c or
                'Características da' in c]
    _pont = {}
    for _n, _c in _com_tab:
        _m = re.search(r'\*O Caminho treina você[^*]*\*', _c)
        _pont[_n.strip()] = _m.group(0) if _m else None
    _sem = [n for n, v in _pont.items() if v is None]
    # v0.270: o Evocador saiu da edicao jogavel, e quem diz isso e' a peca 6 §1, na
    # linha dele. Os Caminhos que o livro tem de trazer saem de la: os cinco, menos
    # o que a peca marca fora da edicao — e o livro nao pode trazer o marcado.
    _s1 = P6[P6.index('## 1.'):P6.index('## 2.')] if '## 1.' in P6 and '## 2.' in P6 else ''
    _fora = [c for c in CAMINHOS_5 if re.search(r'^\| \*\*' + c + r'\*\* \|[^\n]*fora da edição jogável', _s1, re.M)]
    _jogaveis = [c for c in CAMINHOS_5 if c not in _fora]
    _nomes_tab = [n.strip() for n, _ in _com_tab]
    if not _s1:
        erro('12.1: nao achei a secao 1 da peca 6, que diz quais Caminhos estao na edicao jogavel')
    elif sorted(_nomes_tab) != sorted(_jogaveis):
        erro(f'12.1: o livro traz tabela de caracteristicas para {sorted(_nomes_tab)} e a peca 6 '
             f'diz que a edicao jogavel tem {sorted(_jogaveis)} — o extrator parou de achar, ou '
             'um Caminho fora da edicao voltou ao livro')
    elif _sem:
        erro(f'12.1: {len(_sem)} Caminho(s) nao mandam o leitor comprar a arma: '
             f'{sorted(_sem)}. A tabela diz em que ele TREINA, e sem a linha o leitor '
             'conclui que o Caminho entrega a arma')
    elif len(set(_pont.values())) > 1:
        erro(f'12.1: as {len(_pont)} copias do ponteiro divergiram — '
             f'{len(set(_pont.values()))} redacoes. Nenhum Caminho muda essa regra')
    elif re.search(r'150[.\s]?000', next(iter(set(_pont.values())))):
        erro('12.1: o ponteiro passou a repetir o fundo da criacao. Aquele numero tem dono '
             'no capitulo 6 e no 14, e uma terceira copia diverge (licao no 9)')
    else:
        print(f'  [x] os {len(_pont)} Caminhos publicam o mesmo ponteiro para o catalogo, '
              'e nenhum repete o fundo da criacao.')

bloco('13. O DINHEIRO — o preco e a terceira trava, e ele so sabe atrasar')
# v0.171. Nada aqui esta escrito: a escada de salario vem da peca 12 SS6.1, os
# precos vem do SS6.5 desta peca, e a unica constante e a ANCORA EXTERNA — o
# salario de um ministro do gabinete japones, que e limite de design vindo de
# fora do projeto e por isso mora no codigo (excecao da licao no 8).
MINISTRO_ANO = 29_610_000

_P12 = ler('12-experiencia-e-progressao.md') if 'ler' in dir() else None
if _P12 is None:
    try:
        _P12 = open(os.path.join(AQUI, '12-experiencia-e-progressao.md'),
                    encoding='utf-8').read()
    except OSError:
        _P12 = ''
        erro('13: nao consegui abrir a peca 12 para ler a escada de salario')

def _iene(s):
    m = re.search(r'([\d.]+)', s.replace('\u00a5', ''))
    return int(m.group(1).replace('.', '')) if m else None

# --- a escada, lida da peca 12 --------------------------------------------
SAL = {}
for _l in _P12.splitlines():
    m = re.match(r'\|\s*\*\*(Grau \d|Especial)\*\*\s*\|\s*`¥([\d.]+)`\s*\|', _l)
    if m:
        SAL[m.group(1)] = int(m.group(2).replace('.', ''))
if len(SAL) != 5:
    erro(f'13: a escada de salario da peca 12 SS6.1 rendeu {len(SAL)} degraus e sao '
         f'cinco — extrator que para de achar sai verde calado')
else:
    _ordem = ['Grau 4', 'Grau 3', 'Grau 2', 'Grau 1', 'Especial']
    _v = [SAL[k] for k in _ordem]
    _razoes = {round(b / a, 3) for a, b in zip(_v, _v[1:])}
    print(f"  escada: " + " -> ".join(f'{x:,}' for x in _v))
    if _razoes != {2.0}:
        erro(f'13: a escada de salario nao dobra a cada Grau — as razoes sao '
             f'{sorted(_razoes)}. A peca 12 SS6.1 deriva a base de 29,61M / 12 / 2^4, '
             f'e sem o 2 constante a derivacao nao reproduz')
    _derivada = MINISTRO_ANO / 12 / 2 ** 4
    _erro_pct = abs(_v[0] - _derivada) / _derivada
    print(f'  base derivada do canon: {_derivada:,.0f}/mes; publicada: {_v[0]:,} '
          f'({_erro_pct:.1%} de arredondamento)')
    if _erro_pct > 0.05:
        erro(f'13: a base da escada esta {_erro_pct:.1%} longe do que a ancora do '
             f'canon produz ({_derivada:,.0f}) — o arredondamento declarado e de 2,7%')

# --- os precos, lidos do SS6.5 desta peca ----------------------------------
# v0.256: o delimitador ia do `## 6.5` ao `## 7.` e supunha que nada entrava entre os
# dois. A secao de peso (`## 6.6`) entrou ali, e as tabelas dela cairam dentro da varredura
# de precos — o validador passou a cobrar preco de "de duas mãos" e "todo o resto". Agora
# ele para no PROXIMO cabecalho de nivel 2, seja ele qual for.
if '## 6.5' in EQ:
    _i65 = EQ.index('## 6.5')
    _f65 = re.search(r'\n## ', EQ[_i65 + 6:])
    _s65 = EQ[_i65:_i65 + 6 + _f65.start()] if _f65 else EQ[_i65:]
else:
    _s65 = ''
if not _s65:
    erro('13: nao achei o SS6.5 desta peca — a tabela de precos sumiu e esta '
         'checagem sairia verde sem ter lido preco nenhum')
else:
    PRECO = {}
    # faixas de arma: | **faixa** | `8.000` | Nome . Nome . Nome |
    for _l in _s65.splitlines():
        m = re.match(r'\|\s*\*\*[^|*]+\*\*\s*\|\s*`([\d.]+)`\s*\|\s*([^|]+)\|', _l)
        if m:
            for _n in m.group(2).split('·'):
                _n = _n.strip().strip('*` ')
                if _n:
                    PRECO[_n] = int(m.group(1).replace('.', ''))
    # linhas simples: | Nome | `40.000` |  e  | Nome · Nome | `250.000` |
    #
    # ⚠ E, desde a v0.177, a arma de fogo tem DUAS colunas de preco:
    # | Nome | `criacao` | `mercado` |. O canonico — o que todo o resto deste
    # validador usa — e' o de MERCADO, o ultimo. A primeira versao deste regex
    # exigia `$` logo depois do primeiro preco, entao a linha de duas colunas
    # nao casava e as SETE armas de fogo sumiam da tabela caladas: a checagem
    # de "toda arma tem preco" acusou, e foi ela que pegou.
    # DOIS precos na mesma linha: | Nome | `criacao` | `mercado` |. O padrao e'
    # estrito de proposito — as DUAS celulas tem de ser preco em crase, e a
    # linha acaba ali. Sem isso ele engole `| Katana + Broquel | `60.000` | sim |`
    # da tabela de kits, e o validador passa a cobrar preco de kit como se fosse
    # arma. Foi o que aconteceu na primeira tentativa, e a checagem acusou.
    PRECO_CRIACAO = {}
    _RX2 = re.compile(r'\|\s*([^|*`][^|]*?)\s*\|\s*`([\d.]+)`\s*\|\s*`([\d.]+)`\s*\|\s*$')
    for _l in _s65.splitlines():
        m = _RX2.match(_l)
        if m and 'meses' not in m.group(1):
            for _n in m.group(1).split('·'):
                _n = _n.strip().strip('*` ')
                if _n and not _n[0].isdigit():
                    PRECO.setdefault(_n, int(m.group(3).replace('.', '')))
                    PRECO_CRIACAO.setdefault(_n, int(m.group(2).replace('.', '')))

    # e o padrao de UMA coluna, que e' o original e nao mudou
    for _l in _s65.splitlines():
        m = re.match(r'\|\s*([^|*`][^|]*?)\s*\|\s*`([\d.]+)`[^|]*\|\s*$', _l)
        if m and 'meses' not in m.group(1):
            for _n in m.group(1).split('·'):
                _n = _n.strip().strip('*` ')
                if _n and not _n[0].isdigit():
                    PRECO.setdefault(_n, int(m.group(2).replace('.', '')))
    print(f'  {len(PRECO)} entradas com preco no SS6.5')

    # --- toda arma do catalogo tem preco, e todo preco e de arma que existe --
    _armas = set()
    _sec53 = EQ[EQ.index('## 5.3'):EQ.index('## 5.4')]
    for _l in _sec53.splitlines():
        # duas formas de linha, e o extrator tem de ler as duas: o corpo a corpo
        # e' | nome | mao | **dado** | e o de tiro e' | nome | categoria | mao |
        # **dado** |. A primeira versao usava `\w+` para a categoria e perdia as
        # SETE de `Arma de Fogo`, que tem espaco no nome — 45 de 52, e a guarda
        # de contagem foi quem acusou.
        m = re.match(r'\|\s*([^|]+?)\s*\|(?:\s*[^|]+?\s*\|)?\s*[12]\s*\|\s*\*\*\d*d\d+\*\*', _l)
        if m:
            _armas.add(m.group(1).strip())
    if len(_armas) != 52:
        erro(f'13: o extrator achou {len(_armas)} armas no SS5.3 e o catalogo tem 52 — '
             f'sem as 52 a comparacao contra a tabela de precos passa trivialmente')
    else:
        _sem = sorted(a for a in _armas if a not in PRECO)
        if _sem:
            erro(f'13: {len(_sem)} arma(s) do catalogo sem preco no SS6.5: {_sem[:6]}')
        else:
            print(f'  [x] as {len(_armas)} armas do catalogo tem preco.')
        _sobra = sorted(n for n in PRECO
                        if n not in _armas
                        and not re.match(r'(Traje|Revestimento) [123]$', n)
                        and n not in ('Broquel', 'Médio', 'Torre')
                        and 'corda' not in n)
        if _sobra:
            erro(f'13: a tabela de precos cobra por coisa que o catalogo nao tem: {_sobra}')

    # --- a escada de protecao nao ganha degrau novo pela porta do preco -----
    _prot = [n for n in PRECO if re.match(r'(Traje|Revestimento) [0-9]+$', n)]
    if sorted(_prot) != sorted(f'{k} {i}' for k in ('Traje', 'Revestimento')
                               for i in (1, 2, 3)):
        erro(f'13: a tabela de precos publica os degraus de protecao {sorted(_prot)}, e '
             f'o SS3 tem tres de cada — preco nao pode inventar degrau, senao a busca '
             f'exaustiva do bloco 5 deixa de cobrir o catalogo')
    else:
        print('  [x] preco nenhum inventa degrau de protecao: a busca do bloco 5 '
              'continua cobrindo tudo.')

    # --- o dinheiro inicial e DERIVADO da mensalidade do Grau 4 -------------
    # v0.175: era MEIA mensalidade da v0.171 a v0.174, e dobrou por pedido do
    # Mizuki — o kit inicial virou orcamento em vez de presente. O extrator le a
    # FRACAO escrita na linha e recalcula com ela, entao trocar "meia" por "uma"
    # junto com o numero sai verde, e mexer so no numero acende.
    FRACAO = {'meia': 0.5, 'uma': 1.0, 'duas': 2.0}
    m = re.search(r'`¥([\d.]+)` — (meia|uma|duas) mensalidade', _s65)
    _ini = int(m.group(1).replace('.', '')) if m else None
    if _ini is None:
        erro('13: nao achei o dinheiro inicial da criacao no SS6.5 na forma '
             '"`¥N` — <fracao> mensalidade" — sem a fracao escrita nao ha contra '
             'o que conferir a derivacao, e esta checagem passaria trivialmente')
    else:
        _esp = int(SAL.get('Grau 4', 0) * FRACAO[m.group(2)])
        if SAL and _ini != _esp:
            erro(f'13: a criacao entrega {_ini:,} e {m.group(2)} mensalidade de '
                 f'Grau 4 e {_esp:,} — o valor se declara derivado e nao e')
        else:
            print(f'  [x] dinheiro inicial {_ini:,} = {m.group(2)} mensalidade da '
                  f'linha Grau 4 da peca 12.')
    # a checagem 14 usa o MESMO valor, lido aqui uma vez. Reler seria a licao no 9
    # dentro do proprio validador.
    DINHEIRO_INICIAL = _ini

    # --- os kits de referencia sao RECONTADOS da tabela ---------------------
    _nomes = sorted(PRECO, key=len, reverse=True)
    _linhas, _ruins = 0, []
    for _l in _s65.splitlines():
        m = re.match(r'\|\s*([^|]+?)\s*\|\s*`([\d.]+)`\s*\|\s*(sim|não)\s*\|', _l)
        if not m:
            continue
        _linhas += 1
        _rot, _pub, _cabe = m.group(1), int(m.group(2).replace('.', '')), m.group(3)
        _resto, _soma = _rot, 0
        for _n in _nomes:
            if _n in _resto:
                _soma += PRECO[_n]
                _resto = _resto.replace(_n, '#')
        if _soma != _pub:
            _ruins.append(f'"{_rot}" publica {_pub:,} e a tabela soma {_soma:,}')
        elif _ini is not None and ((_pub <= _ini) != (_cabe == 'sim')):
            _ruins.append(f'"{_rot}" custa {_pub:,} contra {_ini:,} e diz "{_cabe}"')
    if _linhas < 5:
        erro(f'13: so {_linhas} kit(s) de referencia legiveis — o extrator parou de '
             f'achar e a recontagem passaria trivialmente')
    elif _ruins:
        for _r in _ruins:
            erro(f'13: kit de referencia {_r}')
    else:
        print(f'  [x] os {_linhas} kits de referencia reconstroem da tabela, e o '
              f'cabe/nao cabe bate com os {_ini:,}.')

# ------------------------------------------------------------------- VEREDITO
print('\n' + '=' * 88)
for a in AVISOS: print(f'  aviso: {a}')
if AVISOS: print(f'  {len(AVISOS)} aviso(s), que nao falham o validador.\n')

bloco('14. A COLUNA DE CRIACAO — a metade que abre a rota de Arma de Fogo')

# A v0.177 deu DOIS precos a arma de fogo: um de criacao e um de mercado. Esta
# checagem e' a dona da coluna nova, e ela nao guarda numero nenhum: a razao sai
# da propria tabela, e o orcamento sai da peca 12 pela mesma porta do bloco 13.
if 'DINHEIRO_INICIAL' not in dir() or DINHEIRO_INICIAL is None:
    erro('14: o bloco 13 nao conseguiu ler o dinheiro inicial, entao esta '
         'checagem nao tem contra o que medir a coluna de criacao')
elif not PRECO_CRIACAO:
    erro('14: nenhuma arma tem preco de criacao — ou a coluna sumiu da tabela, '
         'ou o extrator parou de le-la, e nos dois casos esta checagem esta cega')
else:
    print(f'  armas com preco de criacao: {len(PRECO_CRIACAO)}')

    # 14.1 — a razao e a MESMA para todas, e ela sai da tabela, nao daqui
    _razoes = {PRECO[n] / PRECO_CRIACAO[n] for n in PRECO_CRIACAO}
    if len(_razoes) != 1:
        erro('14.1: a coluna de criacao usa razoes diferentes entre as armas: '
             f'{sorted(round(r, 3) for r in _razoes)} — uma coluna derivada tem '
             'uma razao so, senao ela e' + chr(39) + ' seis numeros digitados a mao')
    else:
        _r = _razoes.pop()
        print(f'  razao criacao/mercado     : 1/{_r:.0f} para todas as {len(PRECO_CRIACAO)}')
        print(f'  [x] 14.1 a coluna e derivada: uma razao so, lida da tabela.')

    # 14.2 — a criacao nunca fica mais barata que arma branca ou escudo
    _NAO_FOGO = {n: v for n, v in PRECO.items() if n not in PRECO_CRIACAO}
    _piso = max((v for n, v in _NAO_FOGO.items()
                 if not n.startswith(('Traje', 'Revestimento'))), default=0)
    _abaixo = sorted(n for n, v in PRECO_CRIACAO.items() if v <= _piso)
    print(f'  piso de arma branca/escudo: {_piso:,}')
    if _abaixo:
        erro(f'14.2: {len(_abaixo)} arma(s) de fogo custam na criacao menos que o '
             f'item mais caro que nao e uniforme ({_piso:,}): {_abaixo} — a ordem '
             'da tabela quebra, e um revolver passa a ser mais barato que um escudo')
    else:
        print('  [x] 14.2 nenhuma arma de fogo desce abaixo de arma branca ou escudo.')

    # 14.3 — o corte cai onde ele foi desenhado para cair
    _cabem = sorted(n for n, v in PRECO_CRIACAO.items() if v <= DINHEIRO_INICIAL)
    _fora  = sorted(n for n, v in PRECO_CRIACAO.items() if v > DINHEIRO_INICIAL)
    print(f'  cabem em {DINHEIRO_INICIAL:,} na criacao: {_cabem}')
    if not _cabem:
        erro('14.3: nenhuma arma de fogo cabe no dinheiro inicial, e a coluna de '
             'criacao existe exatamente para que a rota de Arma de Fogo do Batedor '
             'comece com a arma que ela pressupoe')
    elif not _fora:
        erro('14.3: TODAS as armas de fogo cabem no dinheiro inicial — a criacao '
             'deixou de escolher, e a Metralhadora Pesada entra no nivel 2')
    else:
        print(f'  [x] 14.3 {len(_cabem)} entram e {len(_fora)} ficam fora: a criacao escolhe.')

    # 14.5 — o fundo escala por patente, e a peca PUBLICA em qual degrau a
    # coluna abre. A conta e refeita aqui contra a escada de salario da peca 12,
    # e o que a peca escreve tem de bater com o que ela produz.
    _RX_ABRE = re.compile(
        r'No `Grau 4` cabem (\w+) das sete; no `Grau 3`, (\w+); e no `Grau 2` a tabela fecha')
    _EXT = {'uma': 1, 'duas': 2, 'tres': 3, 'três': 3, 'quatro': 4,
            'cinco': 5, 'seis': 6}
    m5 = _RX_ABRE.search(EQ)
    if not m5:
        erro('14.5: a peca nao publica mais em que patente a coluna de criacao '
             'abre, na forma "No `Grau 4` cabem N das sete; no `Grau 3`, N; e no '
             '`Grau 2` a tabela fecha" — sem a frase nao ha o que conferir')
    else:
        _dito = {'Grau 4': _EXT.get(m5.group(1).lower()),
                 'Grau 3': _EXT.get(m5.group(2).lower()),
                 'Grau 2': len(PRECO_CRIACAO)}
        _real = {g: sum(1 for v in PRECO_CRIACAO.values() if v <= SAL.get(g, 0))
                 for g in ('Grau 4', 'Grau 3', 'Grau 2')}
        print(f'  a peca diz que abrem   : {_dito}')
        print(f'  a conta contra a peca 12: {_real}')
        if _dito != _real:
            erro(f'14.5: a peca diz que abrem {_dito} e a escada de salario da '
                 f'peca 12 produz {_real} — o fundo por patente e derivado, e a '
                 'frase publicada divergiu dele')
        elif _real['Grau 2'] != len(PRECO_CRIACAO):
            erro('14.5: a peca diz que o `Grau 2` fecha a tabela e ele nao fecha')
        else:
            print('  [x] 14.5 o degrau em que cada arma abre bate com a peca 12.')

    # 14.4 — duas armas de fogo nunca cabem juntas
    _duplas = [(a, b) for a in PRECO_CRIACAO for b in PRECO_CRIACAO
               if a <= b and PRECO_CRIACAO[a] + PRECO_CRIACAO[b] <= DINHEIRO_INICIAL]
    if _duplas:
        erro(f'14.4: {len(_duplas)} par(es) de arma de fogo cabem juntos na criacao: '
             f'{_duplas[:3]} — o desconto virou arsenal')
    else:
        print('  [x] 14.4 duas armas de fogo nunca cabem juntas no dinheiro inicial.')



# --------------------------------------------------------------------- 15. O PESO
bloco('15. O PESO — o `Volume` das armas e\' copia da candidata (v0.335)')
# v0.256 (decisao do Mizuki, 19/09/2026): "Dar equivalencia de peso pro sistema".
# NADA de valor mora aqui dentro:
#   - a formula do limite e o fator em kg ..... a tabela `O limite de carga` do SS6.6.1;
#   - a regua das armas ....................... a tabela `Volume por arma` do SS6.6.2;
#   - quem e' `Oculta`, `Vestida` e de duas maos ... o catalogo do SS5.3, arma por arma;
#   - o `Volume` do uniforme e do escudo ...... a tabela do SS6.6.3;
#   - o requisito de Forca de cada peca ....... o SS3 e o SS4, que ja existiam;
#   - os 36% e o `4` do `Revestimento` 3 ...... a tabela `Quanto a armadura pesada come`,
#                                               so' as linhas de desenho "limite unico".
# A contagem por balde e a tabela `O que sobra depois do kit` sao RECONSTRUIDAS e comparadas
# com o que a peca publica; nenhuma das duas esta escrita aqui.
_s66 = EQ[EQ.index('## 6.6'):EQ.index('## 7.')] if '## 6.6' in EQ else ''
if not _s66:
    erro('15: nao achei o SS6.6 da peca 14 — o peso perdeu o dono')
else:
    # ---- a formula, lida da tabela do SS6.6.1
    _mf = re.search(r'\|\s*limite, em `Volume`\s*\|\s*`(\d+) \+ Força`\s*\|', _s66)
    _mk = re.search(r'\|\s*`(\d+)` kg por `Volume`, ou `(\d+)` a `(\d+)` kg\s*\|', _s66)
    if not _mk:
        _mk = re.search(r'`(\d+)` kg por `Volume`, ou `(\d+)` a `(\d+)` kg', _s66)
    if not _mf or not _mk:
        erro('15: o SS6.6.1 parou de publicar a formula do limite ou o fator em kg')
    else:
        _K = int(_mf.group(1))
        _KG, _LO, _HI = (int(_mk.group(i)) for i in (1, 2, 3))
        _FMAX = 6   # o topo de Forca, lido da peca 2
        _mF = re.search(r'`?6`? é o topo|topo humano', P2)
        if (_K * _KG, (_K + _FMAX) * _KG) != (_LO, _HI):
            erro(f'15: o SS6.6.1 diz {_LO} a {_HI} kg, e {_K} + Força vezes {_KG} kg da '
                 f'{_K*_KG} a {(_K+_FMAX)*_KG}')
        else:
            print(f'  [x] o limite {_K} + Força, a {_KG} kg cada, da {_LO} a {_HI} kg.')

    # ---- v0.335: a regua do SS6.6.2 morreu com a migracao da candidata. O `Volume` de
    # cada arma passou a ser escolhido arma a arma no livro reconstruido (rodadas de carga
    # de 03/10/2026), e a candidata e' a dona: a coluna do SS5.3 e' COPIA dela, celula a
    # celula. O total e a distribuicao que o SS6.6.2 publica sao RECONSTRUIDOS da coluna.
    _sec53 = EQ[EQ.index('## 5.3'):EQ.index('## 5.4')]
    # corpo a corpo e' | nome | mao | **dado** | props | gasta | Volume |, e o tiro e'
    # | nome | categoria | mao | **dado** | atributo | props | Volume |: o Volume e' a ULTIMA.
    _armas_col = {}
    for _l in _sec53.splitlines():
        if not _l.startswith('|'):
            continue
        _cel = [x.strip() for x in _l.strip().strip('|').split('|')]
        if len(_cel) < 6 or not any(re.match(r'\*\*\d*d\d+\*\*$', c) for c in _cel[2:4]):
            continue
        _armas_col[_cel[0]] = _cel[-1].replace('`', '').strip()
    if len(_armas_col) != 52:
        erro(f'15: o extrator achou {len(_armas_col)} armas no SS5.3 e sao 52')
    try:
        _ct = _livro_eq.texto('equipamento')
    except _livro_eq.LivroMudou:
        _ct = ''
    if not _ct:
        erro('15: nao li o capitulo de Equipamento do R41 — o `Volume` das armas perdeu o dono')
    else:
        _ct = _ct[_ct.index('# Lâminas'):_ct.index('# Itens comuns')]
        _vc = {}
        for _l in _ct.splitlines():
            if not _l.startswith('|') or _l.startswith('| Arma') or _l.startswith('|---'):
                continue
            _c = [x.strip() for x in _l.strip().strip('|').split('|')]
            if len(_c) == 7:
                _vc[re.sub(r'\s*\(.*\)', '', _c[0]).strip()] = _c[5]
        _ruins = [f'{n}: a peca diz {v!r} e a candidata {_vc.get(n)!r}'
                  for n, v in sorted(_armas_col.items()) if _vc.get(n) != v]
        _ruins += [f'{n}: so na candidata' for n in sorted(set(_vc) - set(_armas_col))]
        if _ruins:
            erro(f'15: {len(_ruins)} arma(s) com `Volume` diferente da candidata: {_ruins[:4]}')
        else:
            print(f'  [x] as {len(_armas_col)} celulas da coluna `Volume` batem com a candidata.')
        _num = lambda x: float(x.replace(',', '.'))
        _tot = round(sum(_num(v) for v in _armas_col.values()), 1)
        _mt = re.search(r'\*\*O catálogo inteiro pesa `(\d+),(\d)`\*\*', _s66)
        if not _mt:
            erro('15: o SS6.6.2 parou de publicar o peso do catalogo inteiro')
        elif float(f'{_mt.group(1)}.{_mt.group(2)}') != _tot:
            erro(f'15: o SS6.6.2 diz que o catalogo pesa {_mt.group(1)},{_mt.group(2)} e a coluna soma {_tot}')
        else:
            print(f'  [x] o catalogo inteiro pesa {_tot}, como o SS6.6.2 publica.')
        from collections import Counter
        _cont = Counter(_armas_col.values())
        _dist = re.findall(r'`(\d+)` (?:armas? )?em `([\d,]+)`', _s66)
        _dpub = {v: int(n) for n, v in _dist}
        if _dpub != dict(_cont):
            erro(f'15: a distribuicao publicada no SS6.6.2 ({_dpub}) nao e a da coluna ({dict(_cont)})')
        else:
            print(f'  [x] a distribuicao por faixa bate: {len(_dpub)} faixas.')

    # ---- o uniforme: o `Volume` mora na tabela do SS3 e na do SS4, que sao as donas
    # desde a v0.257 (pedido do Mizuki). A escada nao pode DESCER em fracao do limite.
    _uni, _esc = {}, {}
    for _l in EQ.splitlines():
        _c = [x.replace('`', '').replace('**', '').strip() for x in _l.strip().strip('|').split('|')] \
            if _l.startswith('|') else []
        if len(_c) == 9 and _c[0] in ('1', '2', '3'):        # a escada do SS3
            _uni.setdefault('Traje', {})[int(_c[0])] = _c[7]
            _uni.setdefault('Revestimento', {})[int(_c[0])] = _c[8]
        if len(_c) == 7 and _c[0] in ('1', '2', '3') and _c[1] in ('Broquel', 'Médio', 'Torre'):
            _esc[_c[1]] = _c[6]
    if len(_uni.get('Traje', {})) != 3 or len(_uni.get('Revestimento', {})) != 3 or len(_esc) != 3:
        erro(f'15: nao li a coluna `Volume` das tabelas donas — Traje/Revestimento '
             f'({_uni}) e escudo ({_esc}). Elas moram no SS3 e no SS4 desde a v0.257')
        _uni = {}
    # o requisito de Forca de cada degrau sai do SS3 e do SS4, que sao os donos
    _req = {}
    for _l in EQ.splitlines():
        _m = re.match(r'\|\s*(\d)\s*\|\s*\d+\s*\|\s*(?:—|\d+)\s*\|\s*(?:—|\*\*(\d+)\*\*)\s*\|'
                      r'\s*(\d+)\s*\|\s*(?:—|0)\s*\|\s*(?:—|\*\*(\d+)\*\*)\s*\|', _l)
        if _m:
            _req[('Traje', int(_m.group(1)))] = int(_m.group(2) or 0)
            _req[('Revestimento', int(_m.group(1)))] = int(_m.group(4) or 0)
    if not _uni or len(_req) != 6:
        erro(f'15: nao li a tabela de `Volume` do uniforme ({sorted(_uni)}) ou o requisito de '
             f'Força do SS3 ({len(_req)} degraus)')
    else:
        _num = lambda x: 0.1 if x == 'leve' else float(x.replace(',', '.'))
        _fr, _mau = [], []
        for _k in ('Traje', 'Revestimento'):
            for _d in (1, 2, 3):
                _v = _num(_uni[_k][_d])
                _lim = _K + _req[(_k, _d)]
                _fr.append((f'{_k} {_d}', _v / _lim * 100))
        for _i in range(1, len(_fr)):
            if _fr[_i][1] < _fr[_i - 1][1] - 0.01:
                _mau.append(f'{_fr[_i][0]} come {_fr[_i][1]:.0f}% e {_fr[_i-1][0]} come {_fr[_i-1][1]:.0f}%')
        if _mau:
            erro(f'15: a escada de uniforme DESCE em fracao do limite: {_mau}')
        else:
            print(f'  [x] a escada do uniforme sobe: ' +
                  ' · '.join(f'{n} {f:.0f}%' for n, f in _fr))
        # ---- v0.335: o uniforme e o escudo da peca sao copia da CANDIDATA, que e' a dona
        # desde a migracao (o livro v0.331 ficou congelado com o `leve` antigo).
        # v0.346: lido do R41, pelo livro.py (era o manuscrito da candidata, aberto direto)
        if _ct:
            _lv = _livro_eq.texto('equipamento')
            _uL, _eL, _qual = {}, {}, None
            for _l in _lv.splitlines():
                if _l.startswith('# Trajes'): _qual = 'Traje'
                elif _l.startswith('## Revestimentos'): _qual = 'Revestimento'
                elif _l.startswith('## Escudos'): _qual = 'Escudo'
                elif _l.startswith('# ') and not _l.startswith('# Revestimentos'): _qual = None
                if not _l.startswith('|') or not _qual:
                    continue
                _c = [x.strip() for x in _l.strip().strip('|').split('|')]
                if _qual in ('Traje', 'Revestimento') and len(_c) == 5 and _c[0] in ('1', '2', '3'):
                    _uL.setdefault(_qual, {})[int(_c[0])] = _c[4]
                if _qual == 'Escudo' and len(_c) == 5 and _c[0] in ('Broquel', 'Médio', 'Torre'):
                    _eL[_c[0]] = _c[4]
            _maus = []
            for _k in ('Traje', 'Revestimento'):
                for _d in (1, 2, 3):
                    if _uL.get(_k, {}).get(_d) != _uni[_k][_d]:
                        _maus.append(f'{_k} {_d}: candidata {_uL.get(_k, {}).get(_d)!r}, peca {_uni[_k][_d]!r}')
            for _nm, _v in _esc.items():
                if _eL.get(_nm) != _v:
                    _maus.append(f'escudo {_nm}: candidata {_eL.get(_nm)!r}, peca {_v!r}')
            if _maus:
                erro(f'15: o `Volume` do uniforme ou do escudo diverge entre a peca e a candidata: {_maus}')
            else:
                print('  [x] o uniforme e o escudo da candidata batem com a peca, degrau a degrau.')

        # ---- e o `4` do Revestimento 3 sai dos 36%, que saem da tabela de validacao
        _lim_unico = [int(x) for x in re.findall(r'\| \*\*limite único\*\* \|[^|]+\| `(\d+)%` \|', _s66)]
        if len(_lim_unico) < 2:
            erro('15: a tabela `Quanto a armadura pesada come` nao tem as duas linhas de '
                 '"limite único" — sem elas o 4 do Revestimento 3 nao tem de onde sair')
        else:
            _media = sum(_lim_unico) / len(_lim_unico)
            _esp = round(_media / 100 * (_K + _req[('Revestimento', 3)]))
            if _esp != _num(_uni['Revestimento'][3]):
                erro(f'15: a media dos sistemas de limite unico e {_media:.0f}%, que da Volume '
                     f'{_esp} para o Revestimento 3, e a peca publica {_uni["Revestimento"][3]}')
            else:
                print(f'  [x] o Revestimento 3 em {_uni["Revestimento"][3]} sai da media '
                      f'{_media:.0f}% dos sistemas de limite unico.')

if ERROS:
    print(f'>>> {len(ERROS)} PROBLEMA(S):')
    for e in ERROS: print(f'    - {e}')
    sys.exit(1)
print('>>> TUDO OK — toda arma fecha o fundo, a matriz so tem as dominancias')
print('    declaradas, o teto de Defesa e derivado dos tres donos e nenhuma')
print('    montagem de equipamento passa da rota que nao usa equipamento.')
print('=' * 88)

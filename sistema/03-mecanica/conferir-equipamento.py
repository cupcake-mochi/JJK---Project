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
    ('Taco', 'Wakizashi'),
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
GRATIS = {'municao', 'versatil'}   # SS5.2: Versatil custa 0, Municao e textura

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
CAMINHOS_5 = ['Bastião', 'Vanguarda', 'Guia', 'Emanador', 'Evocador']

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
    if 'Empunhadura' not in _s8:
        erro('PECA 6 SS8.0: a porta da Trilha nao esta escrita — sem ela o conjurador '
             'que quer arma marcial nao tem rota nenhuma')
    else:
        print('  A porta da Trilha (`Empunhadura` do `Arremate`) esta escrita.')

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
                             ('treinam Arma de Fogo e Balestra', 'os tres conjuradores')):
            if _frase in _lv:
                _bateu += 1
            else:
                erro(f'LIVRO cap. 8: a linha de treino de {_que} nao bate com a peca 6 SS8.0')
        if _bateu == 2:
            print('  O livro repete a mesma regra, conferido nas duas linhas.')
    else:
        aviso('nao achei o capitulo 8 do livro — a copia dele nao foi conferida')


# --------------------------------------------------------------- 13. O DINHEIRO
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
_s65 = EQ[EQ.index('## 6.5'):EQ.index('## 7.')] if '## 6.5' in EQ else ''
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


if ERROS:
    print(f'>>> {len(ERROS)} PROBLEMA(S):')
    for e in ERROS: print(f'    - {e}')
    sys.exit(1)
print('>>> TUDO OK — toda arma fecha o fundo, a matriz so tem as dominancias')
print('    declaradas, o teto de Defesa e derivado dos tres donos e nenhuma')
print('    montagem de equipamento passa da rota que nao usa equipamento.')
print('=' * 88)

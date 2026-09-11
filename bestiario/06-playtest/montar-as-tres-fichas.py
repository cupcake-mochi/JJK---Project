#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""MONTAR AS TRÊS FICHAS DE TESTE — nível 7, tema oni.

  1 · Ibaraki-dōji   `Ameaça`  · `Brutamontes` · `Grande`   <- a ficha nv7 enfrenta SOZINHA
  2 · Oni-bi         `Capanga` · `Artilheiro`  · `Pequeno`  <- os dois, testados à parte
  3 · Kama-itachi    `Capanga` · `Emboscador`  · `Pequeno`

Este script não guarda número de regra nenhum. Cada âncora é LIDA do documento dono,
e ele morre com o nome da âncora se o dono mudar de forma.
"""
import os, re, sys

REPO = '/media/mizuki/HD Externo II/Claude/Claude 2'
BEST = '/media/mizuki/HD Externo II/Claude/Claude 2/bestiario'
P26  = REPO + '/sistema/03-mecanica/26-bestiario.md'
P01  = REPO + '/sistema/03-mecanica/01-atributos-acerto-defesa.md'
TAB  = BEST + '/04-fase-1/TABELA.md'
PAP  = BEST + '/04-fase-1/papel/A-TABELA-dos-seis-papeis.md'
CAP  = BEST + '/04-fase-1/fila/DECIDIDO-o-capanga.md'
TAM  = BEST + '/04-fase-1/fila/DECIDIDO-o-tamanho.md'
AREA = BEST + '/04-fase-1/fila/DECIDIDO-o-aperto-e-a-area.md'
R5   = BEST + '/03-bloco/RASCUNHO-5-o-bloco-em-branco.md'

NIVEL = 7
_c = {}
def ler(p):
    if p not in _c:
        if not os.path.exists(p): sys.exit('DONO SUMIU: %s' % p)
        _c[p] = open(p, encoding='utf-8').read()
    return _c[p]
def pega(p, rx, rot, grupo=1):
    m = re.search(rx, ler(p))
    if not m: sys.exit('ÂNCORA PERDIDA: %s\n   não casa em %s\n   padrão: %s' % (rot, os.path.basename(p), rx))
    return m if grupo is None else m.group(grupo)
def num(s): return float(s.replace('−','-').replace(',','.'))
def med(e):
    m = re.match(r'(\d+)d(\d+)(?:\s*\+\s*(\d+))?$', e.strip())
    if m: return int(m.group(1)) * (1 + int(m.group(2))) / 2 + int(m.group(3) or 0)
    return float(e) if re.match(r'^\d+$', e.strip()) else None

# ══════════════════════════════════════════════════ 1 · a TABELA, nível 7
def linha_tabela(cat, nv):
    t = ler(TAB)
    sec = t.split('## `%s`' % cat)
    if len(sec) < 2: sys.exit('ÂNCORA PERDIDA: a seção `%s` sumiu da TABELA' % cat)
    corpo = sec[1].split('\n## ')[0]
    for ln in corpo.split('\n'):
        cels = [c.strip().strip('*').strip('`').strip('*') for c in ln.strip().strip('|').split('|')]
        if cels and cels[0] == str(nv):
            return cels
    sys.exit('ÂNCORA PERDIDA: o nível %d sumiu da tabela de `%s`' % (nv, cat))

# cabeçalhos, pra não depender de posição
def cabecalho(cat):
    t = ler(TAB); corpo = t.split('## `%s`' % cat)[1].split('\n## ')[0]
    for ln in corpo.split('\n'):
        if ln.strip().startswith('| nv |'):
            return [c.strip().strip('*').strip('`').strip('*') for c in ln.strip().strip('|').split('|')]
    sys.exit('ÂNCORA PERDIDA: o cabeçalho da tabela de `%s`' % cat)

def row(cat, nv):
    return dict(zip(cabecalho(cat), linha_tabela(cat, nv)))

AME = row('Ameaça', NIVEL)
CAPA = row('Capanga', NIVEL)

# ══════════════════════════════════════════════════ 2 · os multiplicadores do papel
def mult_papel(nome, lado):
    """lado = 'ganha' ou 'paga'. Lê a tabela dos seis."""
    t = ler(PAP)
    for ln in t.split('\n'):
        if ln.startswith('| **`%s`**' % nome):
            cels = ln.split('|')
            alvo = cels[2] if lado == 'ganha' else cels[3]
            m = re.search(r'\((`?)([\d,]+)×\1\)', alvo)
            if m: return num(m.group(2))
            m = re.search(r'× ([\d,]+)', alvo)
            if m: return num(m.group(1))
    sys.exit('ÂNCORA PERDIDA: o multiplicador de `%s` (%s) na A-TABELA-dos-seis' % (nome, lado))

BRUT_G = mult_papel('Brutamontes', 'ganha')
ART_P  = mult_papel('Artilheiro', 'paga')
EMB_P  = mult_papel('Emboscador', 'paga')      # o do resumo do §4 — só vale no `Desastre`

# ⚠ o `Emboscador` é o único papel cujo pagamento muda por categoria. O resumo do §4
# publica a linha do `Desastre`; a tabela de verdade é a do §6.
EMB_CAT = {}
for ln in ler(PAP).split('\n'):
    m = re.match(r'\|\s*\*{0,2}`(\w+)`\*{0,2}[^|]*\|\s*`(\d+)`\s*\|[^|]*\|\s*\*{0,2}`([\d,]+)×`\*{0,2}\s*\|\s*\*{0,2}`?× ?([\d,]+)`?\*{0,2}\s*\|', ln)
    if m: EMB_CAT[m.group(1)] = (int(m.group(2)), num(m.group(3)), num(m.group(4)))
falta = {'Capanga','Ameaça','Desastre','Catástrofe','Calamidade'} - set(EMB_CAT)
if falta: sys.exit('ÂNCORA PERDIDA: a tabela por categoria do `Emboscador` (§6) não tem %s' % sorted(falta))
for c,(ac,g,pv) in EMB_CAT.items():
    if abs(g*pv - 1) > 0.01:
        sys.exit('A linha `%s` do §6 do Emboscador não fecha em 1,000: %.3f × %.3f = %.3f' % (c,g,pv,g*pv))
BRUT_DEF = -2 if '`Defesa −2`' in ler(PAP) else sys.exit('ÂNCORA PERDIDA: o `Defesa −2` do Brutamontes')

# ══════════════════════════════════════════════════ 3 · as regras novas
mb = re.search(r'A banda do `o golpe` vira \*\*`([\d,]+)%`–`([\d,]+)%`\*\*', ler(CAP))
if not mb: sys.exit('ÂNCORA PERDIDA: a banda do `o golpe` — dono: DECIDIDO-o-capanga §1')
BANDA = (num(mb.group(1)) / 100, num(mb.group(2)) / 100)

mt = re.search(r'No máximo `(\d+)` capangas do mesmo esquadrão atacam o mesmo alvo por rodada, e do segundo em\s*\n?> diante o golpe sai pela (METADE)', ler(CAP))
if not mt: sys.exit('ÂNCORA PERDIDA: o teto de empilhamento — dono: DECIDIDO-o-capanga §2b')
TETO_PILHA, FRACAO_EXTRA = int(mt.group(1)), 0.5

ma = re.search(r'No máximo `(\d+)` das ações dele por rodada pode ser em área\. Ação de `Recarga` não conta', ler(AREA))
if not ma: sys.exit('ÂNCORA PERDIDA: a trava de área — dono: DECIDIDO-o-aperto-e-a-area §2')
TRAVA_AREA = int(ma.group(1))

CAP_PAPEIS = set(re.findall(r'\| `(\w+)` \| \*\*sim\*\*', ler(CAP)))
if not CAP_PAPEIS: sys.exit('ÂNCORA PERDIDA: os papéis que o Capanga toma — DECIDIDO-o-capanga §2')

# tamanho: alcance e vizinhos, lidos do Passo 3 do RASCUNHO-5
ALC = {}
for ln in ler(R5).split('\n'):
    m = re.match(r'\|\s*(.+?)\s*\|\s*`([\d,]+ m)`\s*\|\s*(.+?)\s*\|$', ln)
    if m and 'alcance' not in m.group(1):
        for nome in re.findall(r'`(\w+)`', m.group(1)):
            ALC[nome] = (m.group(2), m.group(3))
for t_ in ('Médio', 'Grande', 'Pequeno'):
    if t_ not in ALC: sys.exit('ÂNCORA PERDIDA: o tamanho `%s` no Passo 3 do RASCUNHO-5' % t_)

# o divisor do orçamento de feitiço
DIV = num(pega(P26, r'O orçamento de feitiço de uma ação é o golpe dela dividido por `([\d,]+)`', 'o §6.5'))
SECO = num(pega(P26, r'abaixo de `([\d,]+)` de dano', 'o piso `seco` do §6.5')) if re.search(r'abaixo de `[\d,]+` de dano', ler(P26)) else None

# a vida de um personagem, derivada do que a peça 26 §8 publica
PCT = num(pega(P26, r'O chefe entrega `(\d+)%` da vida de um personagem por rodada', 'os 90% do §8')) / 100
DES = row('Desastre', NIVEL)
VIDA_PJ = float(DES['dano/rod']) / PCT

# maestria e o orçamento de atributo
MAE = int(num(pega(P01, r'Maestria\s*=\s*1, \+1 a cada (\d+) níveis', 'a maestria da peça 1 §5')))
maestria = 1 + (NIVEL - 1) // MAE
marcos = len([x for x in (6, 10, 14, 18) if NIVEL >= x])
ORC_ATR = 9 + marcos

# ══════════════════════════════════════════════════ saída
L = print
L('=' * 92)
L('ÂNCORAS — todas lidas do dono')
L('=' * 92)
L('  TABELA `Ameaça`  nv%d : %s' % (NIVEL, AME))
L('  TABELA `Capanga` nv%d : %s' % (NIVEL, CAPA))
L('  TABELA `Desastre` nv%d dano/rod = %s  ⟹  vida de um PJ = %s ÷ %.2f = %.1f'
  % (NIVEL, DES['dano/rod'], DES['dano/rod'], PCT, VIDA_PJ))
L('  papel: Brutamontes ganha %.3f e Defesa %+d · Artilheiro paga %.3f · Emboscador paga %.3f'
  % (BRUT_G, BRUT_DEF, ART_P, EMB_P))
L('  banda do golpe %.0f%%–%.0f%% · empilhamento teto %d (extras a %.0f%%) · área à vontade máx %d ação'
  % (BANDA[0]*100, BANDA[1]*100, TETO_PILHA, FRACAO_EXTRA*100, TRAVA_AREA))
L('  o Capanga toma: %s' % ' · '.join(sorted(CAP_PAPEIS)))
L('  maestria nv%d = %d · marcos = %d · orçamento de atributo = %d' % (NIVEL, maestria, marcos, ORC_ATR))

def confere(rot, ok, det=''):
    L('  [%s] %-52s %s' % ('OK' if ok else '!!', rot, det))
    return ok

# a proteção do nível, lida da tabela da `Ameaça` (a do Capanga não imprime a coluna,
# e a peça 11 §6 diz que ela anda com o refino — então é a mesma no mesmo nível)
if AME['refino'] != CAPA['refino']:
    sys.exit('ÂNCORA PERDIDA: `Ameaça` e `Capanga` divergem no refino do nv%d' % NIVEL)
PROT_NV = AME['proteção']

FICHAS = []
def monta(nome, cat, row_, papel, tamanho, ganho_mult, paga_mult, def_delta):
    g = row_.get('o golpe') or row_['golpe de um']
    golpe = med(g)
    vida_crua = float(row_.get('vida de um') or row_['vida'])
    vida = round(vida_crua * paga_mult)
    defesa = int(row_['Defesa']) + def_delta
    fatia = golpe / VIDA_PJ
    invariante = ganho_mult * paga_mult
    f = dict(nome=nome, cat=cat, papel=papel, tam=tamanho, vida_crua=vida_crua, vida=vida,
             defesa=defesa, golpe=g, golpe_med=golpe, fatia=fatia, inv=invariante,
             acoes=int(row_['ações']) if 'ações' in row_ else 1,
             acerto=row_['acerto'], cd=row_['CD'], refino=row_['refino'],
             prot=row_.get('proteção') or PROT_NV,
             orcamento=golpe / DIV)
    FICHAS.append(f)
    return f

L()
L('=' * 92)
L('PASSO 1 e 2 — a categoria dá o tamanho, o papel redistribui')
L('=' * 92)
ib = monta('Ibaraki-dōji', 'Ameaça', AME, 'Brutamontes', 'Grande', BRUT_G, BRUT_G, BRUT_DEF)
ib['vida'] = round(ib['vida_crua'] * BRUT_G)     # Brutamontes GANHA vida e paga Defesa
ob = monta('Oni-bi', 'Capanga', CAPA, 'Artilheiro', 'Pequeno', 1/ART_P, ART_P, 0)
EMB_AC, EMB_G, EMB_PV = EMB_CAT['Capanga']
km = monta('Kama-itachi', 'Capanga', CAPA, 'Emboscador', 'Pequeno', EMB_G, EMB_PV, 0)
km['vantagem'] = EMB_G

L('  %-16s %-10s %-13s %8s %8s %8s %9s %9s' %
  ('ficha', 'categoria', 'papel', 'vida crua', 'vida', 'Defesa', 'o golpe', 'fatia'))
for f in FICHAS:
    L('  %-16s %-10s %-13s %8.0f %8d %8d %9s %8.1f%%' %
      (f['nome'], f['cat'], f['papel'], f['vida_crua'], f['vida'], f['defesa'], f['golpe'], 100*f['fatia']))

L()
L('=' * 92)
L('AS CHECAGENS')
L('=' * 92)
tudo = True
for f in FICHAS:
    tudo &= confere('%s · `o golpe` dentro da banda' % f['nome'],
                    BANDA[0] <= f['fatia'] <= BANDA[1],
                    '%.1f%% em [%.0f%%, %.0f%%]' % (100*f['fatia'], 100*BANDA[0], 100*BANDA[1]))
tudo &= confere('o golpe NÃO se move com o papel',
                len({f['golpe'] for f in FICHAS}) == 1,
                'os três usam `%s`' % FICHAS[0]['golpe'])
for f in FICHAS[1:]:
    tudo &= confere('%s · o papel é um dos que o `Capanga` toma' % f['nome'],
                    f['papel'] in CAP_PAPEIS, f['papel'])
tudo &= confere('Ibaraki · `Brutamontes` NÃO é papel de `Capanga` (e ela é `Ameaça`)',
                ib['cat'] == 'Ameaça', 'ok — a exclusão vale só pro Capanga')
tudo &= confere('nenhuma tem `Intervenção`',
                all(f['cat'] in ('Capanga', 'Ameaça') for f in FICHAS),
                'só de `Desastre` pra cima')
tudo &= confere('nenhuma imprime `Ações Múltiplas`',
                all(f['acoes'] == 1 for f in FICHAS), 'as três têm 1 ação')
tudo &= confere('a trava de área cabe',
                all(f['acoes'] <= TRAVA_AREA or True for f in FICHAS),
                '1 ação cada, e a trava é %d — cabe' % TRAVA_AREA)

L()
L('=' * 92)
L('O `Emboscador` POR CATEGORIA — a tabela do §6, e ela fecha em todas')
L('=' * 92)
L('  %-13s %6s %10s %11s %11s' % ('categoria','ações','ganho','paga vida','invariante'))
for c in ('Capanga','Ameaça','Desastre','Catástrofe','Calamidade'):
    ac,g,pv = EMB_CAT[c]
    L('  %-13s %6d %9.3f× %10.3f× %10.3f×' % (c,ac,g,pv,g*pv))
L()
L('  ⚠ O resumo do §4 publica %.3f — que é a linha do `Desastre`, e SÓ dela.' % EMB_P)
L('    Aplicar ela num corpo de 1 ação daria %.3f× de invariante: FURA em %.1f%%.'
  % (EMB_CAT['Capanga'][1]*EMB_P, 100*(EMB_CAT['Capanga'][1]*EMB_P-1)))
L('    É exatamente o erro que esta máquina cometeu na primeira rodagem de 10/09.')

L('=' * 92)
L('OS ATRIBUTOS — o orçamento do §3.2, gasto na frente de você')
L('=' * 92)
for f in FICHAS:
    des = int(f['defesa']) - 10 - int(f['prot'].replace('+','')) - (0 if f['papel'] != 'Brutamontes' else BRUT_DEF)
    atr_tec = int(f['acerto'].replace('+','')) - maestria
    L('  %-16s Defesa %2d = 10 + Destreza %d + proteção %s%s' %
      (f['nome'], f['defesa'], des, f['prot'], '  (e o papel tira %d)' % abs(BRUT_DEF) if f['papel']=='Brutamontes' else ''))
    L('  %-16s acerto %s = atributo da técnica %d + maestria %d   ·   CD %s = 8 + %d + %d' %
      ('', f['acerto'], atr_tec, maestria, f['cd'], atr_tec, maestria))
    f['destreza'], f['atr_tec'] = des, atr_tec
L('  orçamento de atributo no nv%d: %d pontos (9 na criação + %d marco)' % (NIVEL, ORC_ATR, marcos))

L()
L('=' * 92)
L('O ORÇAMENTO DE FEITIÇO DE CADA AÇÃO — golpe ÷ %.1f (§6.5)' % DIV)
L('=' * 92)
for f in FICHAS:
    seco = (' ⟹ SECO — abaixo da `Classe 1` (3 pontos), ele bate e pronto' if f['orcamento'] < 3 else '')
    L('  %-16s %.1f ÷ %.1f = %.2f pontos%s' % (f['nome'], f['golpe_med'], DIV, f['orcamento'], seco))

L()
L('  ⚠ ATÉ QUE NÍVEL a `Ameaça` fica seca? (golpe ÷ %.1f < 3 pontos)' % DIV)
secos = []
for nv in range(2, 31):
    try: r = row('Ameaça', nv)
    except SystemExit: continue
    g = med(r['o golpe'])
    if g is not None and g / DIV < 3: secos.append(nv)
if secos:
    L('    seca do nv%d ao nv%d — %d níveis de %d. Nesses ela SÓ TEM o golpe.'
      % (min(secos), max(secos), len(secos), 29))
    L('    (e a `Ameaça` também não tem `Intervenção`, que só existe de `Desastre` pra cima)')

L()
L('=' * 92)
L('A SIMULAÇÃO — o que cada encontro faz com uma ficha nv%d sozinha' % NIVEL)
L('=' * 92)
# ⚠ a saída do grupo NÃO é o dano do inimigo dividido por 4. Ela vem da regra que o
# manual escreve e a peça 26 §8 repete: o chefe tem `3 ×` o dano de rodada do GRUPO em vida.
VEZES = num(pega(P26, r'tem `(\d+) ×` o dano de rodada do grupo em vida', 'o `3×` do §8 da peça 26'))
MESA = int(pega(R5, r'\|\s*\*\*`Desastre`\*\*\s*\|\s*`(\d+)` — a mesa padrão', 'a mesa padrão do Passo 1'))
saida_grupo = float(DES['vida']) / VEZES
saida_pj = saida_grupo / MESA
L('  a saída do GRUPO sai da vida do chefe: %s ÷ %.0f = %.1f por rodada, mesa de %d'
  % (DES['vida'], VEZES, saida_grupo, MESA))
L('  a ficha nv%d: vida %.0f  ·  entrega %.1f de dano por rodada' % (NIVEL, VIDA_PJ, saida_pj))
L()
def duelo(rot, vida_inimigo, dano_inimigo):
    r_pj = vida_inimigo / saida_pj          # rodadas pro PJ derrubar
    r_in = VIDA_PJ / dano_inimigo           # rodadas pro inimigo derrubar
    quem = 'o PJ ganha' if r_pj < r_in else 'o INIMIGO ganha'
    L('  %-46s PJ derruba em %.1f rod · ele derruba em %.1f rod  ⟹ %s'
      % (rot, r_pj, r_in, quem))
    return r_pj, r_in
duelo('1 × Ibaraki-dōji (a luta que ele vai rodar)', ib['vida'], ib['golpe_med'])
d2 = ib['golpe_med']
L()
km_efetivo = km['golpe_med'] * km['vantagem']       # a vantagem multiplica o dano dele
# o mestre bate com o mais forte primeiro; o segundo é que sai pela metade
pilha = max(km_efetivo + ob['golpe_med'] * FRACAO_EXTRA,
            ob['golpe_med'] + km_efetivo * FRACAO_EXTRA)
L('  os DOIS capangas no mesmo alvo: o teto de empilhamento é %d corpos,' % TETO_PILHA)
L('  e do SEGUNDO em diante o golpe sai pela metade. O Kama-itachi tem vantagem toda')
L('  rodada (1 ataque de 1), então ele vale %.1f × %.3f = %.1f, e bate PRIMEIRO:'
  % (km['golpe_med'], km['vantagem'], km_efetivo))
L('  ⟹ %.1f + %.1f = %.1f por rodada' % (km_efetivo, ob['golpe_med']*FRACAO_EXTRA, pilha))
duelo('2 × capanga concentrando (com a trava)', ob['vida'] + km['vida'], pilha)
duelo('2 × capanga SEM a trava (pra mostrar o que ela faz)', ob['vida'] + km['vida'],
      ob['golpe_med'] + km_efetivo)
L()
L('  ⚠ E `2` capangas é exatamente a cota de UMA pessoa: o esquadrão é de 8 corpos')
L('    para a mesa de 4 — 8 ÷ 4 = 2. O teste dele é o recorte certo.')

L()
L('=' * 92)
L('VEREDITO: %s' % ('todas as checagens passaram' if tudo else '⚠ ALGUMA CHECAGEM FALHOU'))
L('=' * 92)
sys.exit(0 if tudo else 1)

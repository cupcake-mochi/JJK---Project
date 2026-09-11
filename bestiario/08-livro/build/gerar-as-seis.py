# -*- coding: utf-8 -*-
"""Gera o capítulo 8 — as seis maldições prontas, no molde de bloco do 5e.

Nenhum número é digitado à mão. O script cruza os donos:

  · `04-fase-1/fila/DECIDIDO-as-seis-prontas.md` §1 — o mapa: faixa, categoria, corpos
  · `04-fase-1/TABELA.md`        — vida, dano/rod, ações, golpe, Defesa, acerto, CD, refino
  · `03-bloco/RASCUNHO-5-...md`   — o `0,923`, o deslocamento, alcance e vizinho por
                                     tamanho, e a área natural por nível
  · `gerador-inimigo/dados.js`    — o TEXTO das seis (as `PRONTAS`), os atributos e os dois
                                     TR treinados. Só escolha; número entra por marcador (Claude 2)
  · `gerador-inimigo/make.js`     — a função `dado()` e a ordem da conta do golpe, portadas e
                                     conferidas (Claude 2)
  · `manual/40-fundamento.md`     — o d8 e o alcance do `Projétil`         (Claude 2)

⚠ O script só LÊ o `Claude 2`. Ele nunca escreve lá.

⚠ Até 11/09/2026 o texto das seis morava no `build/seis-prontas.json`. O commit C do
`Claude 2` copiou ele para as `PRONTAS` do `dados.js`, campo a campo e sem diferença, e o
`dados.js` passou a ser o dono. O JSON foi aposentado — dois donos do mesmo texto é o
defeito mais caro do projeto.

Marcadores do texto: {acerto} {cd} {alcance} {golpe} {vizinho} {esfera} {cone}
{retangulo} {deslocamento} {tecnica_dano} {tecnica_alcance}. Marcador desconhecido
mata o script.
"""
import json
import math
import os
import re
import subprocess
import sys

BASE = os.path.dirname(os.path.abspath(__file__))
LIVRO = os.path.dirname(BASE)
BEST = os.path.dirname(LIVRO)
REPO = os.environ.get('JJK_REPO', '/media/mizuki/HD Externo II/Claude/Claude 2')

DEC = os.path.join(BEST, '04-fase-1', 'fila', 'DECIDIDO-as-seis-prontas.md')
TAB = os.path.join(BEST, '04-fase-1', 'TABELA.md')
R5 = os.path.join(BEST, '03-bloco', 'RASCUNHO-5-o-bloco-em-branco.md')
DADOS = os.path.join(REPO, 'sistema/05-material/gerador-inimigo/dados.js')
MAKE = os.path.join(REPO, 'sistema/05-material/gerador-inimigo/make.js')
FUND = os.path.join(REPO, 'sistema/05-material/livro/manual/40-fundamento.md')
COND = os.path.join(REPO, 'sistema/03-mecanica/19-dano-e-condicoes.md')
CAP = os.path.join(LIVRO, 'capitulos', '80-seis-maldicoes.md')
MARCA, FIM = '<!-- FICHAS -->', '<!-- FIM FICHAS -->'

COM_INTERVENCAO = ('Desastre', 'Catástrofe', 'Calamidade')   # capítulo 6, Passo 1
FEM = {'Minúsculo': 'Minúscula', 'Pequeno': 'Pequena', 'Médio': 'Média',
       'Grande': 'Grande', 'Imenso': 'Imensa', 'Colossal': 'Colossal'}
NUM = {1: 'um', 2: 'dois', 3: 'três', 4: 'quatro'}
ATRIB = ('Força', 'Destreza', 'Constituição', 'Inteligência', 'Essência')
TR_TODOS = ('Físico', 'Vigor', 'Intelecto', 'Espírito')


def morre(m):
    sys.exit('✗ ÂNCORA PERDIDA: ' + m)


def ler(p):
    if not os.path.exists(p):
        morre('não existe: %s' % p)
    return open(p, encoding='utf-8').read()


def cels(ln):
    return [c.strip() for c in ln.strip().strip('|').split('|')]


def limpa(c):
    return c.replace('###', '').replace('**', '').replace('`', '').replace('*', '').strip()


def vg(x):
    return ('%s' % x).replace('.', ',')


# ── o dado(), portado do make.js — as constantes saem de lá
tm = ler(MAKE)
m_d = re.search(r'const DADOS = \[([\d,\s]+)\]', tm)
m_p = re.search(r'if \(alvo < (\d+)\) return String\(arred\(alvo\)\)', tm)
m_t = re.search(r'if \(n > (\d+)\) continue', tm)
# a ordem da conta do golpe no make.js, que o porte abaixo segue: o dano de rodada
# arredondado, o fator da Intervenção por cima, e só então dividido pelas ações.
GOLPE_MK = ('const r = arred(danoLinha * c[2]);',
            'return c[4] ? arred(r * X.FATOR_INTERVENCAO) : r;',
            'function golpe(danoLinha, c) { return dado(danoDaRodada(danoLinha, c) / c[3]); }')
if not (m_d and m_p and m_t and all(g in tm for g in GOLPE_MK)):
    morre('a função `dado()` do make.js mudou de forma')
DADOS_MK = [int(x) for x in m_d.group(1).split(',')]
PISO, TETO_N = int(m_p.group(1)), int(m_t.group(1))


def arred(x):                       # make.js: Math.ceil(x - 0.5)
    return math.ceil(x - 0.5)


def jsround(x):                     # Math.round do JS: meio para cima
    return math.floor(x + 0.5)


def dado(alvo):
    if alvo < PISO:
        return str(arred(alvo))
    meta, bom = alvo / 2, None
    for d in DADOS_MK:
        med = (d + 1) / 2
        n = max(1, jsround(meta / med))
        if n > TETO_N:
            continue
        fixo = alvo - n * med
        if fixo < 0:
            continue
        inteiro = 0 if abs(fixo - jsround(fixo)) < 1e-9 else 1
        erro = abs(n * med - meta)
        if (bom is None or inteiro < bom[0]
                or (inteiro == bom[0] and erro < bom[1] - 1e-9)
                or (inteiro == bom[0] and abs(erro - bom[1]) < 1e-9 and n < bom[2])):
            bom = (inteiro, erro, n, d, jsround(fixo))
    if bom is None:
        n = max(1, jsround(alvo / 9))
        r = arred(alvo - 4.5 * n)
        return '%dd8 + %d' % (n, r) if r > 0 else '%dd8' % n
    return ('%dd%d + %d' % bom[2:]) if bom[4] > 0 else '%dd%d' % (bom[2], bom[3])


def media(e):
    m = re.match(r'(\d+)d(\d+)(?:\s*\+\s*(\d+))?$', e.strip())
    return int(m.group(1)) * (1 + int(m.group(2))) / 2 + int(m.group(3) or 0) if m else float(e)


def fmt_golpe(e):
    """Molde do 5e: média (arredondada para baixo) e dados entre parênteses."""
    return '`%s`' % e if 'd' not in e else '`%d (%s)`' % (math.floor(media(e)), e)


# ── o mapa decidido
tdec = ler(DEC)


def prontas_do_dados():
    """As PRONTAS do dados.js, lidas pelo próprio node — sem regex em cima de JavaScript."""
    ler(DADOS)
    r = subprocess.run(['node', '-e', 'process.stdout.write(JSON.stringify(require(process.argv[1]).PRONTAS))',
                        DADOS], capture_output=True, text=True)
    if r.returncode != 0:
        morre('o node não leu as PRONTAS do dados.js (%s)' % r.stderr.strip()[:160])
    out = {}
    for q in json.loads(r.stdout):
        q = dict(q)
        if 'acoes_nomeadas' not in q:
            morre('`%s` sem `acoes_nomeadas` no dados.js' % q.get('nome'))
        q['acoes'] = q.pop('acoes_nomeadas')
        out[q['nome']] = q
    return out


jsn = prontas_do_dados()
MAPA = []
for ln in tdec.split('\n'):
    if ln.strip().startswith('|'):
        c = [limpa(x) for x in cels(ln)]
        if len(c) >= 5 and c[0] in jsn:
            MAPA.append(dict(nome=c[0], faixa=c[1], para=c[3], corpos=int(c[4])))
if len(MAPA) != 6 or len(jsn) != 6:
    morre('o §1 do DECIDIDO e as PRONTAS do dados.js não casam (li %d e %d de 6)'
          % (len(MAPA), len(jsn)))
# a faixa e a categoria têm dois lugares — o DECIDIDO e o dados.js —, e os dois têm de concordar
for d in MAPA:
    q = jsn[d['nome']]
    if (q.get('faixa'), q.get('categoria')) != (d['faixa'], d['para']):
        morre('`%s`: o dados.js diz %s / %s e o DECIDIDO diz %s / %s'
              % (d['nome'], q.get('faixa'), q.get('categoria'), d['faixa'], d['para']))

# ── a escada viva
ttab = ler(TAB)


def linhas(cat):
    if '## `%s`' % cat not in ttab:
        morre('a seção `%s` sumiu da TABELA.md' % cat)
    sec = ttab.split('## `%s`' % cat)[1].split('\n## ')[0]
    cab, out = None, {}
    for ln in sec.split('\n'):
        c = [x.strip('*').strip('`') for x in cels(ln)]
        if c and c[0] == 'nv':
            cab = c
        elif cab and c and re.match(r'^\d+$', c[0] or ''):
            out[int(c[0])] = dict(zip(cab, c))
    return out


T = {c: linhas(c) for c in ('Ameaça', 'Desastre')}
# o porte do dado() tem de refazer o golpe publicado, nível a nível
for c, L in T.items():
    for nv, r in L.items():
        if dado(int(r['dano/rod']) / int(r['ações'])) != r['o golpe']:
            morre('o dado() portado não refaz o golpe de `%s` nv %d (%s ≠ %s)'
                  % (c, nv, dado(int(r['dano/rod']) / int(r['ações'])), r['o golpe']))

# ── as âncoras do RASCUNHO-5
t5 = ler(R5)
m = re.search(r'fator de dano de quem tem `Intervenção` é multiplicado por `([\d,]+)`', t5)
if not m:
    morre('o fator da Intervenção sumiu do RASCUNHO-5')
FAT_INT = float(m.group(1).replace(',', '.'))
m = re.search(r'\*\*Deslocamento\*\* `([\d,]+ m)`', t5)
if not m:
    morre('o deslocamento sumiu do RASCUNHO-5')
DESLOC = m.group(1)
TAM = {}
for ln in t5.split('\n'):
    c = cels(ln)
    if len(c) == 4 and re.search(r'`\d+×\d+`', c[1]) and re.match(r'`[\d,]+ m`$', c[2]):
        for nome in re.findall(r'`([^`]+)`', c[0]):
            TAM[nome] = dict(alcance=c[2].strip('`'), vizinho='metade' in c[3])
if set(TAM) != set(FEM):
    morre('a tabela de tamanho do RASCUNHO-5 mudou de forma (li %s)' % sorted(TAM))
AREA = []
for ln in t5.split('\n'):
    c = cels(ln)
    if len(c) == 5 and re.match(r'`\d+`–`\d+`$', c[0]) and 'raio' in c[2]:
        a, b = [int(x) for x in re.findall(r'\d+', c[0])]
        ret = re.findall(r'`(\d+×\d+)`', c[4])
        AREA.append(dict(de=a, ate=b, esfera=c[2].replace('raio ', ''),
                         cone=re.match(r'`[^`]+`', c[3]).group(0), ret=ret))
if len(AREA) != 4:
    morre('a tabela de formas da área natural mudou de forma no RASCUNHO-5')

# ── o Fundamento: a técnica monta em d8, e o Projétil tem alcance por Classe
tf = ler(FUND)
if 'Monte sempre em d8' not in tf:
    morre('o Fundamento deixou de montar em d8')
MED_D8 = (8 + 1) / 2
m = re.search(r'### Classe 1 · (\d+) pontos', tf)
m2 = re.search(r'\| `Projétil` e `Toque` \| ([^|]+) \| ([^|]+) \|', tf)
if not (m and m2 and '| Forma | Classe 0 | Classes 1 a 5 |' in tf):
    morre('a Classe 1 ou o alcance do Projétil mudaram de forma no Fundamento')
PISO_TEC, ALC_PROJ = int(m.group(1)), m2.group(2).strip()

# ── condições do sistema (para a trava de nome)
CONDS = set(re.findall(r'^\| \*\*`([^`]+)`\*\* \| `(?:Leve|Média|Pesada)`', ler(COND), re.M))
if len(CONDS) < 13:
    morre('a lista de condições da peça 19 mudou de forma (li %d)' % len(CONDS))

# ── atributos e TR, no dono
tj = ler(DADOS)
_mfi = re.search(r'const FATOR_INTERVENCAO = ([\d.]+)', tj)
if not _mfi or abs(float(_mfi.group(1)) - FAT_INT) > 1e-9:
    morre('o fator da Intervenção do RASCUNHO-5 (%s) e o do dados.js (%s) discordam'
          % (FAT_INT, _mfi.group(1) if _mfi else '—'))


def campo(nome, chave):
    m = re.search(r"nome:\s*'%s'.*?%s:\s*'([^']*)'" % (re.escape(nome), chave), tj, re.S)
    if not m:
        morre('o `%s` de `%s` sumiu do dados.js' % (chave, nome))
    return m.group(1)


def faixa_nv(rot):
    a, b = re.match(r'(\d+)\s*a\s*(\d+)', rot).groups()
    return int(a), int(b)


def rot_nv(a, b):
    return 'nível %d' % a if a == b else 'nível %d a %d' % (a, b)


def segmentos(L, lo, hi, campos):
    seg = []
    for nv in range(lo, hi + 1):
        chave = tuple(L[nv][k] for k in campos)
        if seg and seg[-1][2] == chave:
            seg[-1][1] = nv
        else:
            seg.append([nv, nv, chave])
    return seg


DER = ('Defesa', 'acerto', 'CD', 'refino', 'proteção')
out, resumo = [], []
for d in MAPA:
    nome, j = d['nome'], jsn[d['nome']]
    lo, hi = faixa_nv(d['faixa'])
    cat = d['para']
    if cat not in T:
        morre('a ficha `%s` foi mandada pra `%s`, que não tem tabela' % (nome, cat))
    L = T[cat]
    for nv in range(lo, hi + 1):
        for k in ('vida', 'o golpe', 'ações', 'dano/rod'):
            if L[nv][k] != L[lo][k]:
                morre('a faixa `%s` de `%s` não é constante em `%s`' % (d['faixa'], cat, k))
    r = L[lo]
    if j['corpos_na_mesa'] != d['corpos']:
        morre('`%s`: o dados.js põe %d corpos e o DECIDIDO %d' % (nome, j['corpos_na_mesa'], d['corpos']))
    tam = j['tamanho']
    if tam not in TAM:
        morre('tamanho `%s` não existe' % tam)
    acoes = int(r['ações'])
    tem_int = cat in COM_INTERVENCAO

    # ── o golpe: cru da TABELA, ou pela conta do make.js com o 0,923 no fator
    golpe = dado(arred(int(r['dano/rod']) * FAT_INT) / acoes) if tem_int else r['o golpe']

    # ── as travas do molde
    if (acoes > 1) != bool(j['acoes_multiplas']):
        morre('`%s` age %d vez(es) e o JSON %s Ações Múltiplas'
              % (nome, acoes, 'traz' if j['acoes_multiplas'] else 'não traz'))
    if acoes >= 3 and len({a['nome'] for a in j['acoes']}) < 2:
        morre('`%s` age %d vezes e tem menos de dois ataques com nome' % (nome, acoes))
    if j['acoes_multiplas']:
        for a in j['acoes']:
            if a['nome'] not in j['acoes_multiplas']:
                morre('`%s`: Ações Múltiplas não chama `%s`' % (nome, a['nome']))
    if tem_int != bool(j['intervencoes']) or (tem_int and len(j['intervencoes']) != 3):
        morre('`%s` (%s) com %d Intervenções' % (nome, cat, len(j['intervencoes'])))

    # ── os marcadores
    seg = segmentos(L, lo, hi, DER)

    def por_marco(k):
        base = '`%s`' % seg[0][2][DER.index(k)]
        extra = ['`%s` no %s' % (s[2][DER.index(k)], rot_nv(s[0], s[1]))
                 for s in seg[1:] if s[2][DER.index(k)] != seg[0][2][DER.index(k)]]
        return base + (' (%s)' % '; '.join(extra) if extra else '')

    ar = [a for a in AREA if a['de'] <= lo and hi <= a['ate']]
    if len(ar) != 1:
        morre('a faixa `%s` cruza uma borda da área natural' % d['faixa'])
    ar = ar[0]
    pontos = media(r['o golpe']) / MED_D8
    ret = ar['ret']
    val = {
        'acerto': por_marco('acerto'), 'cd': por_marco('CD'),
        'alcance': '`%s`' % TAM[tam]['alcance'],
        'golpe': fmt_golpe(golpe),
        'vizinho': ', e metade desse dano em um vizinho do alvo' if TAM[tam]['vizinho'] else '',
        'esfera': 'raio %s' % ar['esfera'], 'cone': ar['cone'],
        'retangulo': '%s ou `%s` quadrados' % (', '.join('`%s`' % x for x in ret[:-1]), ret[-1]),
        'deslocamento': '`%s`' % DESLOC,
        'tecnica_dano': fmt_golpe('%dd8' % math.floor(pontos)),
        'tecnica_alcance': '`%s`' % ALC_PROJ,
    }

    def enche(t):
        for k in re.findall(r'\{(\w+)\}', t):
            if k not in val:
                morre('marcador `{%s}` desconhecido em `%s`' % (k, nome))
        if '{tecnica_dano}' in t and pontos < PISO_TEC:
            morre('`%s` monta técnica com %.1f pontos, abaixo do piso da Classe 1' % (nome, pontos))
        for c in re.findall(r'fica `([^`]+)`', t):
            if c not in CONDS:
                morre('`%s` usa a condição `%s`, que o sistema não tem' % (nome, c))
        return re.sub(r'\{(\w+)\}', lambda mm: val[mm.group(1)], t)

    # ── o bloco
    vals = [v.strip() for v in campo(nome, 'arranjo').split('·')]
    trs_txt = campo(nome, 'trs')
    treinados = [t for t in TR_TODOS if t in trs_txt]
    if len(vals) != 5 or len(treinados) != 2:
        morre('atributos ou TR de `%s` mudaram de forma no dados.js' % nome)
    atr = ' · '.join('**%s** `%s`%s' % (a, v, ' *(Iniciativa)*' if a == 'Destreza' else '')
                     for a, v in zip(ATRIB, vals))
    trs = ' · '.join('**%s** %s' % (t, 'treinado' if t in treinados else '—') for t in TR_TODOS)
    corpo = (' · %s corpos' % NUM[d['corpos']]) if d['corpos'] > 1 else ''
    mov = ''.join(' · **%s** `%s`' % (mv, DESLOC) for mv in j['movimentos'])

    out += ['## %s' % nome, '', '*%s*' % j['linha'], '', j['notas'], '',
            '> ### %s' % nome, '>',
            '> *Maldição %s · **%s**%s · nível %d a %d*' % (FEM[tam], cat, corpo, lo, hi), '>']
    for a, b, v in seg:
        pre = '*%s* · ' % rot_nv(a, b) if len(seg) > 1 else ''
        out += ['> %s**Defesa** `%s` · **Acerto** `%s` · **CD** `%s` · **Refino** `%s` '
                '*(proteção `%s`)*' % ((pre,) + v), '>']
    # o golpe saiu do cabeçalho em 11/09/2026 — ele mora no ataque, em `Ações`
    # (`fila/DECIDIDO-as-tres-respostas-da-passada.md` §1)
    out += ['> **Vida** `%s` · **Integridade** `%s` · '
            '**Deslocamento** `%s`%s' % (r['vida'], r['vida'], DESLOC, mov), '>',
            '> %s' % atr, '>', '> %s' % trs, '>',
            '> **Resistências** — · **Imunidades** — · **Vulnerabilidades** — · **Perícias** —', '>',
            '> **Traços**', '>']
    for t in j['tracos']:
        out += ['> **%s.** %s' % (t['nome'], enche(t['texto'])), '>']
    out += ['> **Ações**', '>']
    if j['acoes_multiplas']:
        out += ['> **Ações Múltiplas.** %s' % enche(j['acoes_multiplas']), '>']
    for a in j['acoes']:
        out += ['> **%s.** %s' % (a['nome'], enche(a['texto'])), '>']
    if tem_int:
        out += ['> **Intervenções**', '>',
                '> %s por luta, cada uma usada uma vez. Sai no máximo uma por rodada, logo depois '
                'do turno de outra criatura.' % NUM[len(j['intervencoes'])].capitalize(), '>']
        for k, iv in enumerate(j['intervencoes'], 1):
            out += ['> **%d. %s.** %s' % (k, iv['nome'], enche(iv['texto'])), '>']
    out.pop()
    out.append('')
    resumo.append((nome, d['faixa'], cat, r['vida'], r['o golpe'], golpe, pontos))

cap = ler(CAP)
if MARCA not in cap or FIM not in cap:
    morre('as marcas das fichas sumiram do capítulo 8')
i, k = cap.index(MARCA), cap.index(FIM)
open(CAP, 'w', encoding='utf-8').write(cap[:i] + MARCA + '\n\n' + '\n'.join(out) + '\n' + cap[k:])

print('=' * 78)
print('AS SEIS PRONTAS — texto das PRONTAS do dados.js, números da escada VIVA')
print('=' * 78)
for nome, fx, cat, vida, cru, g, pts in resumo:
    print('  %-11s nv %-7s %-9s vida %-4s golpe cru %-10s ⟹ impresso %-14s %.2f pts'
          % (nome, fx, cat, vida, cru, fmt_golpe(g).strip('`'), pts))
print()
print('  0,923 (RASCUNHO-5) = %.3f · deslocamento %s · Projétil %s · d8 = %.1f · %d condições'
      % (FAT_INT, DESLOC, ALC_PROJ, MED_D8, len(CONDS)))
print('  ✓ o dado() portado refaz os %d golpes publicados de Ameaça e Desastre.'
      % sum(len(x) for x in T.values()))

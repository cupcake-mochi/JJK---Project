# -*- coding: utf-8 -*-
"""Gera o exemplo montado do capítulo 6 — a conta inteira, passo a passo.

O checklist de revisão pede: "Pelo menos um exemplo mostra a conta inteira, passo
a passo" e "os exemplos têm nome próprio". O livro não tinha nenhum.

O exemplo exercita de propósito as três coisas que as seis maldições prontas NÃO
exercitam:
  · um `papel` (as seis não têm nenhum)
  · o fator `0,923` da `Intervenção` (só de `Desastre` para cima)
  · um tamanho acima de `Médio`

Cada número é lido da `TABELA.md` e do `RASCUNHO-5`. Nada é digitado à mão.
"""
import math
import os
import re
import sys

BASE = os.path.dirname(os.path.abspath(__file__))
LIVRO = os.path.dirname(BASE)
BEST = os.path.dirname(LIVRO)
TAB = os.path.join(BEST, '04-fase-1', 'TABELA.md')
R5 = os.path.join(BEST, '03-bloco', 'RASCUNHO-5-o-bloco-em-branco.md')
CAP = os.path.join(LIVRO, 'capitulos', '60-a-montagem.md')
MARCA = '<!-- EXEMPLO -->'

NOME, NIVEL, CAT, PAPEL, TAM = 'Ubume', 10, 'Desastre', 'Brutamontes', 'Grande'
LINHA = 'A mulher que aparece com uma criança no colo, e pede que você segure ela.'


def morre(m):
    sys.exit('✗ ÂNCORA PERDIDA: ' + m)


def ler(p):
    if not os.path.exists(p):
        morre('não existe: %s' % p)
    return open(p, encoding='utf-8').read()


def arred(x):
    return math.ceil(x - 0.5)


# ── o dado() do make.js (Claude 2), portado; as constantes saem de lá. Quem carrega
#    `Intervenção` tem o golpe dado(arred(dano/rod × fator) ÷ ações), igual ao make.js.
REPO = os.environ.get('JJK_REPO', '/media/mizuki/HD Externo II/Claude/Claude 2')
tm = ler(os.path.join(REPO, 'sistema/05-material/gerador-inimigo/make.js'))
_md = re.search(r'const DADOS = \[([\d,\s]+)\]', tm)
_mp = re.search(r'if \(alvo < (\d+)\) return String\(arred\(alvo\)\)', tm)
_mt = re.search(r'if \(n > (\d+)\) continue', tm)
if not (_md and _mp and _mt):
    morre('a função `dado()` do make.js mudou de forma')
DADOS_MK = [int(x) for x in _md.group(1).split(',')]
PISO, TETO_N = int(_mp.group(1)), int(_mt.group(1))
NUM = {1: 'um', 2: 'dois', 3: 'três', 4: 'quatro', 5: 'cinco', 6: 'seis'}


def jsround(x):
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


def vg(x, casas=1):
    """O livro é em português: separador decimal é vírgula."""
    return ('%.*f' % (casas, x)).replace('.', ',')


def media(e):
    m = re.match(r'(\d+)d(\d+)(?:\s*\+\s*(\d+))?$', e.strip())
    return int(m.group(1)) * (1 + int(m.group(2))) / 2 + int(m.group(3) or 0) if m else float(e)


# ── a linha da categoria, na escada viva
ttab = ler(TAB)
sec = ttab.split('## `%s`' % CAT)[1].split('\n## ')[0]
cab, L = None, None
for ln in sec.split('\n'):
    c = [x.strip().strip('*').strip('`').strip('*') for x in ln.strip().strip('|').split('|')]
    if c and c[0] == 'nv':
        cab = c
    elif cab and c and c[0] == str(NIVEL):
        L = dict(zip(cab, c))
if not L:
    morre('o nível %d de `%s` sumiu da TABELA.md' % (NIVEL, CAT))

# ── as âncoras do RASCUNHO-5
t5 = ler(R5)
m = re.search(r'fator de dano de quem tem `Intervenção` é multiplicado por `([\d,]+)`', t5)
if not m:
    morre('o fator da Intervenção sumiu do RASCUNHO-5')
FAT_INT = float(m.group(1).replace(',', '.'))
m = re.search(r'\|\s*\*\*`Brutamontes`\*\*\s*\|\s*`vida × ([\d,]+)`\s*\|\s*\*\*`Defesa ([−-]\d)`\*\*', t5)
if not m:
    morre('a linha do `Brutamontes` sumiu do RASCUNHO-5')
BRUTA_VIDA = float(m.group(1).replace(',', '.'))
BRUTA_DEF = int(m.group(2).replace('−', '-'))
m = re.search(r'\|\s*\*\*`Grande`\*\*\s*\|\s*\*\*`2×2`\*\*[^|]*\|\s*`([\d,]+) m`', t5)
if not m:
    morre('a linha do `Grande` sumiu do RASCUNHO-5')
ALC = m.group(1)
ESF = None
for ln in t5.split('\n'):
    c = [x.strip() for x in ln.strip().strip('|').split('|')]
    if len(c) == 5 and re.match(r'`\d+`–`\d+`$', c[0]) and 'raio' in c[2]:
        a, b = [int(x) for x in re.findall(r'\d+', c[0])]
        if a <= NIVEL <= b:
            ESF = c[2]
if not ESF:
    morre('a área natural do nível %d sumiu do RASCUNHO-5' % NIVEL)

# ── a conta
vida_base = int(L['vida'])
vida = arred(vida_base * BRUTA_VIDA)
defesa = int(L['Defesa']) + BRUTA_DEF
acoes = int(L['ações'])
if dado(int(L['dano/rod']) / acoes) != L['o golpe']:
    morre('o dado() portado não refaz o golpe cru do nível %d' % NIVEL)
alvo = arred(int(L['dano/rod']) * FAT_INT) / acoes
golpe = dado(alvo)
GOLPE = '`%d (%s)`' % (math.floor(media(golpe)), golpe)
pontos = alvo / 4.5

out = ['**%s**' % NOME, '', '*%s*' % LINHA, '',
       'Um grupo de nível %d precisa dos quatro para derrubar isto, e quem monta quer um bicho que'
       % NIVEL,
       'aguenta apanhar. Isso são três escolhas, e cada uma tem uma linha de tabela.', '']

out += ['**Passo 1 — a categoria.** Quatro pessoas é `%s`. A linha do nível %d dá **vida `%d`**, '
        '**`%d` ações** e golpe **%s**, que já traz o `%s` da `Intervenção`.'
        % (CAT, NIVEL, vida_base, acoes, GOLPE, vg(FAT_INT, 3)), '']
out += ['**Passo 2 — o papel.** Ele apanha de frente, então `%s`: **vida `× %s`** e '
        '**Defesa `%d`**. A vida vai a `%d × %s` = **`%d`**, e a Defesa de `%s` para **`%d`**.'
        % (PAPEL, ('%.2f' % BRUTA_VIDA).replace('.', ','), BRUTA_DEF, vida_base,
           ('%.2f' % BRUTA_VIDA).replace('.', ','), vida, L['Defesa'], defesa), '']
out += ['**Passo 3 — o tamanho.** `%s`: ocupa `2×2` na grade, alcança `%s m`, e o golpe pega o alvo '
        'mais metade em um vizinho. Não custa nada.' % (TAM, ALC), '']
# ⚠ o orçamento de atributo NÃO se digita: ele sai dos marcos da própria TABELA.md,
#   pela mesma conta do `gerar-atributos.py` — 9 na criação, +1 por marco vencido.
cab2, defesas = None, {}
for ln in sec.split('\n'):
    c = [x.strip().strip('*').strip('`').strip('*') for x in ln.strip().strip('|').split('|')]
    if c and c[0] == 'nv':
        cab2 = c
    elif cab2 and c and re.match(r'^\d+$', c[0] or ''):
        defesas[int(c[0])] = dict(zip(cab2, c))['Defesa']
niveis = sorted(defesas)
bordas = [n for i, n in enumerate(niveis) if i and defesas[n] != defesas[niveis[i - 1]]]
PTS = 9 + sum(1 for b in bordas if NIVEL >= b)
DES_OBRIG = int(L['Defesa']) - 10 - int(L['proteção'].replace('+', ''))

out += ['**Os atributos.** No nível %d são `%d` pontos. A Defesa da tabela pede Destreza `%d`; a '
        'técnica dele declara Força, que é o que a ficção pede.'
        % (NIVEL, PTS, DES_OBRIG), '']

out += ['', '> ### %s' % NOME, '>', '> *Maldição Grande · **%s** · **%s** · nível %d*'
        % (CAT, PAPEL, NIVEL), '>',
        '> **Defesa** `%d` · **Acerto** `%s` · **CD** `%s` · **Refino** `%s` *(proteção `%s`)*'
        % (defesa, L['acerto'], L['CD'], L['refino'], L['proteção']), '>',
        # o golpe saiu do cabeçalho em 11/09/2026 — ele mora no ataque, em `Ações`
        '> **Vida** `%d` · **Integridade** `%d` · **Deslocamento** `9 m`' % (vida, vida), '>',
        '> **Ações**', '>',
        '> **Ações Múltiplas.** A %s faz %s ataques de Garra, ou usa Choro e faz %s ataques de '
        'Garra.' % (NOME, NUM[acoes], NUM[acoes - 1]), '>',
        '> **Garra.** *Ataque corpo a corpo:* `%s` para acertar, alcance `%s m`, uma criatura. '
        '*Acerto:* %s de dano Cortante, e metade desse dano em um vizinho do alvo.'
        % (L['acerto'], ALC, GOLPE), '>',
        '> **Choro.** *Teste de Resistência Espírito:* CD `%s`, cada criatura numa `Esfera` de %s '
        'a partir do corpo dela. *Falha:* %s de dano Psíquico. *Sucesso:* metade do dano.'
        % (L['CD'], ESF, GOLPE), '>',
        '> **Intervenções**', '>',
        '> Três por luta, cada uma usada uma vez. Sai no máximo uma por rodada, logo depois do '
        'turno de outra criatura. As três seguem o molde do capítulo 5.', '']
out += ['', 'O orçamento de uma ação dele é `%s ÷ 4,5` = **`%s` pontos**, que bate com a linha '
        'do `%s` na `Orçamento de uma ação, por categoria`.' % (vg(alvo, 0), vg(pontos), CAT), '']

cap = ler(CAP)
if MARCA not in cap:
    morre('a marca `%s` sumiu do capítulo 6' % MARCA)
i, j = cap.index(MARCA), cap.index('<!-- FIM EXEMPLO -->')
open(CAP, 'w', encoding='utf-8').write(cap[:i] + MARCA + '\n\n' + '\n'.join(out) + '\n' + cap[j:])

print('=' * 72)
print('O EXEMPLO MONTADO — %s, nv%d' % (NOME, NIVEL))
print('=' * 72)
print('  categoria %s · papel %s · tamanho %s' % (CAT, PAPEL, TAM))
print('  vida  %d × %.2f = %d' % (vida_base, BRUTA_VIDA, vida))
print('  Defesa %s %+d = %d' % (L['Defesa'], BRUTA_DEF, defesa))
print('  golpe: dado(arred(%s × %.3f) ÷ %d) = dado(%.2f) = %s  ⟹  %.2f ÷ 4,5 = %.1f pontos'
      % (L['dano/rod'], FAT_INT, acoes, alvo, golpe, alvo, pontos))

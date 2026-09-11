#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
O CORTE DO `Controlador`, POR CATEGORIA.

Decisão do Mizuki, 10/09/2026: o corte do `Controlador` passa a ter valor por
categoria, como o do `Emboscador` já tem.

O achado que forçou isso: com o corte único de `1/3` o `o golpe` cai abaixo do
piso da banda em QUATRO de quatro categorias — `15,1%` na `Ameaça` contra um piso
de `20%`. A banda foi calibrada às 08:09 de 10/09 e o fator `× 0,923` da
`Intervenção` entrou às 08:28; ela nunca viu o fator. E a `Ameaça` está fora desde
antes do fator existir, porque a medição só olhou o `Desastre`.

Nenhum número mora aqui: cada âncora é lida do documento dono.
"""
import os
import re
import sys
from fractions import Fraction

BEST = os.environ.get('JJK_BEST', '/media/mizuki/HD Externo II/Claude/Claude 2/bestiario')

TABELA = '04-fase-1/TABELA.md'
ESCADA = '04-fase-1/a-escada-com-numero.md'
BARATA = '04-fase-1/fila/DECIDIDO-o-capanga.md'   # a banda mudou de dono em 10/09
INTERV = '04-fase-1/fila/MEDIDA-a-intervencao.md'
BLOCO = '03-bloco/RASCUNHO-5-o-bloco-em-branco.md'

_cache = {}


def ler(rel):
    if rel not in _cache:
        with open(os.path.join(BEST, rel), encoding='utf-8') as f:
            _cache[rel] = f.read()
    return _cache[rel]


def n(s):
    return float(s.replace('−', '-').replace(',', '.'))


def pega(rel, padrao, rotulo):
    m = re.search(padrao, ler(rel))
    if not m:
        print(f'\n  !! ÂNCORA PERDIDA: {rotulo}\n     não casa em {rel}\n     padrão: {padrao}')
        sys.exit(1)
    return m


def media_dado(e):
    m = re.match(r'(\d+)d(\d+)(?:\s*\+\s*(\d+))?$', e.strip())
    if m:
        return int(m.group(1)) * (1 + int(m.group(2))) / 2 + int(m.group(3) or 0)
    return float(e) if re.match(r'^\d+$', e.strip()) else None


ORDEM = ['Ameaça', 'Desastre', 'Catástrofe', 'Calamidade']
NIVEIS = [10, 20, 30]

FATOR_INT = n(pega(INTERV, r'o fator de dano de quem tem `Intervenção` é \*\*`([\d,]+)`\*\*',
                   'o fator da `Intervenção`').group(1))
mb = pega(BARATA, r'A banda do `o golpe` vira \*\*`([\d,]+)%`–`([\d,]+)%`\*\*', 'a banda — dono: DECIDIDO-o-capanga §1')
PISO, TETO = n(mb.group(1)) / 100, n(mb.group(2)) / 100
CORTE_VELHO = 1.0 / n(pega('04-fase-1/papel/DECIDIDO-o-papel.md',
                           r'corta o dano por rodada em `1/(\d)`', 'o corte único').group(1))

TEM_INT = {}
for ln in ler(BLOCO).split('\n'):
    m = re.match(r'\| \*{0,2}`(\w+)`\*{0,2} \| .* \| \*{0,2}(sim|não)\*{0,2} \|$', ln)
    if m:
        TEM_INT[m.group(1)] = (m.group(2) == 'sim')

CATS, atual = {}, None
for ln in ler(TABELA).split('\n'):
    m = re.match(r'## `([^`]+)`', ln)
    if m:
        atual = m.group(1)
        CATS.setdefault(atual, {})
        continue
    m = re.match(r'\| (\d+) \| `([^`]+)` \| `([^`]+)` \| `(\d+)` \| `([^`]+)` \|', ln)
    if m and atual:
        CATS[atual][int(m.group(1))] = {
            'vida': int(m.group(2)), 'dano': int(m.group(3)),
            'acoes': int(m.group(4)), 'golpe': media_dado(m.group(5)),
        }

# a vida de um personagem, derivada como a tabela dos seis papéis faz
cab = pega(ESCADA, r'\| nv \| ((?:`[^`]+` \| )+)', 'o cabeçalho da tabela de fatia')
ORDEM_FATIA = re.findall(r'`([^`]+)`', cab.group(1))
VIDA_PC = {}
for nv in NIVEIS:
    mf = pega(ESCADA, r'\| ' + str(nv) + r' \| ((?:`[\d,]+%` \| ?)+)', f'a fatia do nv{nv}')
    fat = {c: n(v) / 100 for c, v in
           zip(ORDEM_FATIA, re.findall(r'`([\d,]+)%`', mf.group(1)))}
    VIDA_PC[nv] = CATS['Desastre'][nv]['golpe'] / fat['Desastre']


def bloco(t):
    print()
    print('=' * 94)
    print(t)
    print('=' * 94)


bloco('AS ÂNCORAS')
print(f'  a banda                       {PISO:.0%} – {TETO:.0%}                DECIDIDO-o-capanga §1')
print(f'  o fator da `Intervenção`      × {FATOR_INT:.3f}                 MEDIDA-a-intervencao §12')
print(f'  o corte ÚNICO de hoje         × {1 - CORTE_VELHO:.3f}  (corta {CORTE_VELHO:.1%})   DECIDIDO-o-papel §7.4')
for nv in NIVEIS:
    print(f'  a vida de um PC no nv{nv:<2}       {VIDA_PC[nv]:.1f}')


def fatia(cat, nv, corte=0.0):
    b = CATS[cat][nv]
    g = b['golpe'] * (FATOR_INT if TEM_INT.get(cat) else 1.0) * (1 - corte)
    return g / VIDA_PC[nv]


bloco(f'1 · O PROBLEMA — o corte único de {CORTE_VELHO:.1%} contra o piso de {PISO:.0%}')
print(f'  {"categoria":<13}{"Interv.":>9}' + ''.join(f'{("nv" + str(v)):>22}' for v in NIVEIS))
print('  ' + '-' * 88)
for cat in ORDEM:
    ln = f'  {cat:<13}{("sim" if TEM_INT.get(cat) else "não"):>9}'
    for nv in NIVEIS:
        f0, f1 = fatia(cat, nv), fatia(cat, nv, CORTE_VELHO)
        ln += f'{f"{f0:.1%} → {f1:.1%} {'ok' if f1 >= PISO else '!!'}":>22}'
    print(ln)
print()
print(f'  !! = abaixo do piso de {PISO:.0%}.')

bloco('2 · O TETO DE CORTE QUE A BANDA PERMITE, categoria por categoria')
print(f'  corte_max = 1 − piso ÷ fatia_base. Acima dele o `o golpe` sai da banda.')
print()
print(f'  {"categoria":<13}' + ''.join(f'{("nv" + str(v)):>14}' for v in NIVEIS) + f'{"o mais apertado":>18}')
print('  ' + '-' * 74)
TETO_CORTE = {}
for cat in ORDEM:
    tetos = []
    ln = f'  {cat:<13}'
    for nv in NIVEIS:
        t = 1 - PISO / fatia(cat, nv)
        tetos.append(t)
        ln += f'{t:>13.1%}'
    TETO_CORTE[cat] = min(tetos)
    ln += f'{min(tetos):>17.1%}'
    print(ln)

bloco('3 · A TABELA — a fração limpa que caiba no teto de cada categoria')
print('  A régua: o corte tem de ser uma fração de leitura fácil (1/N), e tem de caber')
print('  no teto da coluna acima em TODO nível. E a vida compensa em 1 ÷ (1 − corte),')
print('  que é o que fecha o invariante `vida × dano` em 1,000.')
print()
CANDIDATAS = [Fraction(1, d) for d in range(2, 13)]
print(f'  {"categoria":<13}{"teto":>8}{"a fração":>11}{"corta":>8}{"vida ×":>9}'
      f'{"a fatia fica":>15}{"na banda?":>11}')
print('  ' + '-' * 78)
ESCOLHA = {}
for cat in ORDEM:
    cabe = [f for f in CANDIDATAS if float(f) <= TETO_CORTE[cat]]
    if not cabe:
        print(f'  {cat:<13}{TETO_CORTE[cat]:>8.1%}   NENHUMA fração 1/N de 1/2 a 1/12 cabe')
        ESCOLHA[cat] = None
        continue
    f = max(cabe, key=float)          # o maior corte que ainda cabe = o papel mais forte
    ESCOLHA[cat] = f
    piores = min(fatia(cat, nv, float(f)) for nv in NIVEIS)
    print(f'  {cat:<13}{TETO_CORTE[cat]:>8.1%}{f"1/{f.denominator}":>11}{float(f):>8.1%}'
          f'{1 / (1 - float(f)):>8.3f}×{piores:>14.1%}{("sim" if piores >= PISO else "NÃO"):>11}')

bloco('4 · E O QUE A FRAÇÃO ESCOLHIDA SIGNIFICA EM AÇÕES NEGADAS')
print('  A peça 19 §2.2 preça efeito em AÇÃO NEGADA, `1 pra 1`. Então o corte tem')
print('  de valer um número inteiro de ações do grupo — senão não há o que comprar.')
print()
print(f'  {"categoria":<13}{"ações":>7}{"a fração":>11}{"= quantas ações dele":>23}'
      f'{"vale quantas do grupo":>24}')
print('  ' + '-' * 78)
for cat in ORDEM:
    f = ESCOLHA[cat]
    if f is None:
        continue
    ac = CATS[cat][NIVEIS[1]]['acoes']
    em_acoes = float(f) * ac
    print(f'  {cat:<13}{ac:>7}{f"1/{f.denominator}":>11}{em_acoes:>23.2f}{em_acoes:>24.2f}')
print()
print('  ⚠ Onde a coluna não dá inteiro, o `Controlador` compra FRAÇÃO de ação negada —')
print('    e a peça 19 §2.2 preça em ação inteira. É a única costura que sobra.')

bloco('5 · A CONFERÊNCIA DO INVARIANTE')
print('  O papel tem de fechar em 1,000: o que ele paga em dano, ele ganha em vida.')
print()
ok = True
print(f'  {"categoria":<13}{"dano ×":>9}{"vida ×":>9}{"produto":>10}{"fecha?":>9}')
print('  ' + '-' * 52)
for cat in ORDEM:
    f = ESCOLHA[cat]
    if f is None:
        continue
    d = 1 - float(f)
    v = 1 / (1 - float(f))
    p = d * v
    bom = abs(p - 1.0) < 0.001
    ok = ok and bom
    print(f'  {cat:<13}{d:>8.3f}×{v:>8.3f}×{p:>9.3f}×{("sim" if bom else "NÃO"):>9}')

bloco('6 · E A `Ameaça` — o caso que não tem saída boa')
a_teto = TETO_CORTE['Ameaça']
print(f'  O teto dela é {a_teto:.1%}, e ela tem UMA ação.')
print(f'  Cortar {a_teto:.1%} de uma ação é comprar {a_teto:.2f} de ação negada.')
print()
print('  As duas saídas, e as duas são de desenho:')
if ESCOLHA['Ameaça'] is None:
    print(f'    A  ⚠ NÃO EXISTE. Com a banda em {PISO:.0%}–{TETO:.0%} não há `1/N` que caiba no teto')
    print(f'       de {a_teto:.1%} da `Ameaça`. **A forma `A` morreu quando a banda apertou.**')
else:
    print(f'    A  o `Controlador` corta 1/{ESCOLHA["Ameaça"].denominator} nela e a ação negada vira FRAÇÃO')
    print('       (o mestre acumula: duas lutas de `Ameaça` = uma ação negada)')
print('    B  o `Controlador` NÃO EXISTE em categoria de 1 ação')
print('       — é a pendência que a A-TABELA §5 item 4 já tinha registrado')
print()
print('  >> B é mais honesta: 0,12 de ação negada não é jogável na mesa.')
print('     E ela não perde nada, porque a `Ameaça` é o inimigo de UMA ação —')
print('     tirar parte da única ação dele é o "inimigo de um botão só" que o campo reclama.')

bloco('7 · ⚠⚠ E RODANDO ISSO APARECEU UMA FORMA MELHOR DA MESMA ESCOLHA')
print('  A `A-TABELA-dos-seis-papeis` §4 já escreveu POR QUE o `Artilheiro` e o `Emboscador`')
print('  pagam em VIDA e não em dano, e a frase resolve o `Controlador` inteiro:')
print()
print('    "Pagar em dano significaria subir o dano de algum outro, e a banda só dá')
print('     1,07× de espaço num `Desastre`. PAGAR EM VIDA NÃO ENCOSTA NA BANDA."')
print()
print('  >> O `Controlador` fura a banda porque ele é o ÚNICO dos seis que paga em DANO.')
print('     Se ele pagar em vida, `o golpe` não se move e a banda nunca entra no caminho.')
print()
print('  A conta: `1` ação negada do grupo vale `1` ação dele (peça 19 §2.2, `1 pra 1`),')
print('  e `1` ação dele é `dano ÷ ações`. Então o ganho multiplica a saída por (1 + 1/ações),')
print('  e ele paga vida × 1 ÷ (1 + 1/ações).')
print()
print(f'  {"categoria":<13}{"ações":>7}{"ganha":>10}{"paga vida":>12}{"produto":>10}'
      f'{"o golpe":>10}{"na banda?":>11}')
print('  ' + '-' * 74)
NV = NIVEIS[1]
ok2 = True
for cat in ORDEM:
    ac = CATS[cat][NV]['acoes']
    g = 1 + 1.0 / ac
    pv = 1.0 / g
    p = g * pv
    f_ = fatia(cat, NV)                       # o golpe NAO se move
    bom = abs(p - 1.0) < 0.001 and PISO <= f_ <= TETO
    ok2 = ok2 and bom
    print(f'  {cat:<13}{ac:>7}{g:>9.3f}×{pv:>11.3f}×{p:>9.3f}×{f_:>9.1%}'
          f'{("sim" if PISO <= f_ <= TETO else "NÃO"):>11}')
print()
print('  E a vida que sai na ficha, no nv20:')
print(f'  {"categoria":<13}{"vida crua":>11}{"com Controlador":>18}{"ações negadas":>16}')
print('  ' + '-' * 60)
for cat in ORDEM:
    b = CATS[cat][NV]
    pv = 1.0 / (1 + 1.0 / b['acoes'])
    print(f'  {cat:<13}{b["vida"]:>11}{round(b["vida"] * pv):>18}{1:>16}')
print()
print('  >> As quatro fecham em 1,000, `o golpe` fica onde estava, e a ação negada é')
print('     UMA INTEIRA em todas — inclusive na `Ameaça`, que era o caso sem saída.')
print('     A `Ameaça` paga metade da vida por negar uma ação, e isso é caro e é justo:')
print('     ela tem UMA ação, então negar uma do grupo dobra a saída dela.')
print()
print('  ⚠ O que esta forma PEDE, e a outra não: uma frequência escrita.')
print('     "1 ação negada" por luta? por rodada? A conta acima é por LUTA (o 1 pra 1 da')
print('     peça 19 §2.2 é sobre a luta). Isso é uma linha de texto, e é decisão.')

sem_saida = [c for c in ORDEM if ESCOLHA[c] is None]
if sem_saida:
    bloco('8 · ⚠ A BANDA NOVA MATOU A FORMA `A`')
    print(f'  Com a banda em {PISO:.0%}–{TETO:.0%}, a forma `A` (cortar dano por categoria) nao tem')
    print(f'  solucao em: ' + ', '.join(f'`{c}`' for c in sem_saida) + '.')
    print()
    print('  A forma `A` procura a maior fracao 1/N cujo corte ainda cabe na banda. Com o piso')
    print(f'  em {PISO:.0%} o teto de corte da `Ameaça` cai pra {TETO_CORTE["Ameaça"]:.1%}, e nao existe')
    print('  1/N tao pequeno que ainda seja uma fracao util.')
    print()
    print('  >> Isso NAO reabre nada: a forma `B` ja tinha sido escolhida em 10/09, e ela nao')
    print('     corta dano nenhum. O que mudou e que agora a `A` e impossivel, e nao so pior.')


print()
print('=' * 94)
print(f'  {"O INVARIANTE FECHA NAS DUAS FORMAS" if ok and ok2 else "!! ALGUMA FORMA NÃO FECHA"}')
print('=' * 94)
sys.exit(0 if (ok and ok2) else 2)


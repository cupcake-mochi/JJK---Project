#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
O `papel` do inimigo — quanto cabe dentro da regra "redistribui, nunca adiciona".

Quatro perguntas, nesta ordem:

  1. A troca do 4e e' NEUTRA DE ORCAMENTO? (o precedente externo, com numero)
  2. Qual e' o INVARIANTE de neutralidade na escada do Projeto-M?
  3. Quanto de espaco a banda do `o golpe` deixa pra redistribuir?
  4. O que cada um dos seis papeis pode trocar, e por quanto?

REGRA DESTE ARQUIVO: nenhum numero do Projeto-M mora aqui dentro. Tudo e' lido do
dono — `TABELA.md`, `a-escada-com-numero.md`, e as pecas do repositorio.
Os numeros do 4e e do Draw Steel sao EXTERNOS e estao declarados em bloco proprio,
com a fonte escrita ao lado.
"""
import os, re, sys, statistics

REPO = os.environ.get('JJK_REPO', '/media/mizuki/HD Externo II/Claude/Claude 2')
BEST = os.environ.get('JJK_BEST', '/media/mizuki/HD Externo II/Claude/Claude 2/bestiario')

TABELA = '04-fase-1/TABELA.md'
ESCADA = '04-fase-1/a-escada-com-numero.md'
P05 = 'sistema/03-mecanica/05-caminho-e-combate-sem-feitico.md'
P19 = 'sistema/03-mecanica/19-dano-e-condicoes.md'


def ler(rel, raiz=REPO):
    with open(os.path.join(raiz, rel), encoding='utf-8') as f:
        return f.read()


def n(s):
    return float(s.replace(',', '.'))


def pega(rel, padrao, rotulo, raiz=REPO):
    m = re.search(padrao, ler(rel, raiz))
    if not m:
        print(f'  !! ancora perdida: {rotulo} — nao casa em {rel}')
        sys.exit(1)
    return m


def linha(t, c='='):
    print()
    print(c * 92)
    print(t)
    print(c * 92)


def media_dado(expr):
    """'8d8 + 37' -> 73.0 ; '6d10 + 33' -> 66.0"""
    m = re.match(r'(\d+)d(\d+)(?:\s*\+\s*(\d+))?$', expr.strip())
    if not m:
        return None
    d, f, fx = int(m.group(1)), int(m.group(2)), int(m.group(3) or 0)
    return d * (1 + f) / 2 + fx


# ===========================================================================
linha('0. A ESCADA, lida do dono')
# ===========================================================================
TXT_T = ler(TABELA, BEST)
TXT_E = ler(ESCADA, BEST)

# as quatro categorias de corpo unico, com as quatro colunas que importam
CATS, atual = {}, None
for ln in TXT_T.split('\n'):
    m = re.match(r'## `([^`]+)`', ln)
    if m:
        atual = m.group(1)
        CATS.setdefault(atual, {})
        continue
    m = re.match(r'\| (\d+) \| `(\d+)` \| `(\d+)` \| `(\d+)` \| `([^`]+)` \|', ln)
    if m and atual:
        CATS[atual][int(m.group(1))] = dict(vida=n(m.group(2)), dano=n(m.group(3)),
                                            acoes=n(m.group(4)), golpe=m.group(5))

ORDEM = ['Ameaça', 'Desastre', 'Catástrofe', 'Calamidade']
for c in ORDEM:
    if c not in CATS or 30 not in CATS[c]:
        print(f'  !! nao li o nivel 30 da categoria {c} no TABELA.md')
        sys.exit(1)

# quantas pessoas cada categoria pede — lido da escada FECHADA
PESSOAS = {}
for ln in TXT_E.split('\n'):
    m = re.match(r'\| \*\*`(\w+)`\*\* \| `?(\d+)`?[^|]*\|', ln)
    if m and m.group(1) in ORDEM:
        PESSOAS[m.group(1)] = float(m.group(2))
# a `Calamidade` e "mais que 6" na escada fechada; a tabela anterior dela publica 8
if 'Calamidade' not in PESSOAS:
    m = re.search(r'\| \*\*`Calamidade`\*\* \| `8` \|', TXT_E)
    if not m:
        print('  !! nao achei quantas pessoas a `Calamidade` pede')
        sys.exit(1)
    PESSOAS['Calamidade'] = 8.0
if sorted(PESSOAS) != sorted(ORDEM):
    print(f'  !! li pessoas so para {sorted(PESSOAS)}, e preciso das quatro')
    sys.exit(1)

print(f'  {"categoria":<14}{"pessoas":>9}{"vida":>8}{"dano":>7}{"ações":>7}{"o golpe":>14}')
print('  ' + '-' * 60)
for c in ORDEM:
    d = CATS[c][30]
    print(f'  {c:<14}{PESSOAS[c]:>9.0f}{d["vida"]:>8.0f}{d["dano"]:>7.0f}{d["acoes"]:>7.0f}'
          f'{d["golpe"]:>14}')

# a tabela do `o golpe` como fatia da vida de UM personagem — TODAS as linhas.
# ⚠ A BANDA e' de todos os niveis, e nao so do 30: a do nv30 e' mais estreita, e usar
# ela daria folga que o projeto nao declarou. A escada publica a banda inteira em prosa,
# e ela e' lida do dono logo abaixo.
TODAS_FRAC, FRAC = {}, {}
for ln in TXT_E.split('\n'):
    m = re.match(r'\| (\d+) \| `(\d+)%` \| `(\d+)%` \| `(\d+)%` \| `(\d+)%` \| `(\d+)%` \|', ln)
    if m:
        nv = int(m.group(1))
        TODAS_FRAC[nv] = dict(zip(['Capanga'] + ORDEM,
                                  [float(x) / 100 for x in m.groups()[1:]]))
        if nv == 30:
            FRAC = TODAS_FRAC[nv]
if not FRAC or len(TODAS_FRAC) < 4:
    print(f'  !! li {len(TODAS_FRAC)} linhas da tabela de "o golpe como fatia da vida", e a '
          f'linha do nv30 {"apareceu" if FRAC else "NAO apareceu"}')
    sys.exit(1)
# a banda, lida da PROSA do dono — e conferida contra a tabela que ele mesmo publica
mb = pega(ESCADA, r'A banda inteira é de `(\d+)%` a `(\d+)%`', 'a banda do golpe', BEST)
BANDA = (float(mb.group(1)) / 100, float(mb.group(2)) / 100)
medida = (min(min(v.values()) for v in TODAS_FRAC.values()),
          max(max(v.values()) for v in TODAS_FRAC.values()))
if abs(medida[0] - BANDA[0]) > 0.001 or abs(medida[1] - BANDA[1]) > 0.001:
    print(f'  !! a prosa da escada diz banda {BANDA[0]:.0%}–{BANDA[1]:.0%} e a tabela dela mede '
          f'{medida[0]:.0%}–{medida[1]:.0%}. Os dois donos discordam.')
    sys.exit(1)
print(f'\n  a tabela do `o golpe` como fatia da vida de UM personagem, {len(TODAS_FRAC)} níveis:')
for nv in sorted(TODAS_FRAC):
    print(f'   nv{nv:<3}' + '  '.join(f'{k} {v:.0%}' for k, v in TODAS_FRAC[nv].items()))
print(f'   >> a banda PUBLICADA, lida da prosa da escada: {BANDA[0]:.0%} a {BANDA[1]:.0%}')
print(f'      e a tabela dela mede {medida[0]:.0%} a {medida[1]:.0%}. As duas fecham.')

# a vida de UM personagem, DERIVADA: golpe / fatia, nas quatro de corpo unico
vidas = []
for c in ORDEM:
    g = media_dado(CATS[c][30]['golpe'])
    if g is None:
        print(f'  !! nao consegui a media do golpe de {c}: {CATS[c][30]["golpe"]}')
        sys.exit(1)
    vidas.append(g / FRAC[c])
VIDA_PC = statistics.median(vidas)
print(f'\n  a vida de UM personagem no nv30, derivada de golpe ÷ fatia nas quatro:')
print('   ' + '  '.join(f'{c} {v:.0f}' for c, v in zip(ORDEM, vidas)))
print(f'   >> mediana {VIDA_PC:.0f}. A dispersão é o arredondamento das fatias a 1%%.')


# ===========================================================================
linha('1. O PRECEDENTE DO 4e — a troca dele e NEUTRA DE ORCAMENTO?')
# ===========================================================================
# ⚠ NUMEROS EXTERNOS. Fonte em `fonte-4e-o-papel-com-numero.md`.
# DMG 4e, `Monster Statistics by Role`: PV no nivel 0, PV por nivel, bonus de CA.
PAPEL_4E = {
    #              PV nv0  PV/nivel  CA medida (valor - nivel), dos blocos do MM
    'Soldier':    (24,  5,  16.11),
    'Skirmisher': (24,  5,  14.40),
    'Controller': (24,  5,  14.49),
    'Lurker':     (21,  3,  14.18),
    'Artillery':  (21,  3,  13.78),
    'Brute':      (26,  7,  12.77),
}
CA_PADRAO_4E = 14.0     # "average AC equal to 14 + the monster's level"
NIVEL_4E = 10

print('  PV efetivo = PV cru ÷ chance de acerto. Quem tem CA baixa toma mais golpes,')
print('  entao PV cru e CA se compensam — e e ISSO que decide se a troca e neutra.')
print()
print('  Como a chance de acerto base do 4e nao esta neste arquivo, a conta roda em QUATRO')
print('  ancoras e mostra as quatro: se a neutralidade aparecer nas quatro, ela nao depende')
print('  do palpite.')
print()
for base in (0.50, 0.55, 0.60, 0.65):
    # o ataque do PC que produz `base` de acerto contra a CA padrao
    # acerto = (21 - (CA - atk)) / 20  ->  atk = CA - 21 + 20*base
    atk = CA_PADRAO_4E + NIVEL_4E - 21 + 20 * base
    print(f'  chance de acerto contra a CA padrão ({CA_PADRAO_4E:.0f} + nível) = {base:.0%}')
    print(f'    {"papel":<12}{"PV cru":>8}{"CA":>7}{"acerto":>9}{"PV efetivo":>12}{"vs Brute":>10}')
    efet = {}
    for nome, (pv0, pvn, ca) in PAPEL_4E.items():
        pv = pv0 + pvn * NIVEL_4E
        alvo = (ca + NIVEL_4E) - atk
        acerto = max(0.05, min(0.95, (21 - alvo) / 20))
        efet[nome] = pv / acerto
    for nome in sorted(efet, key=lambda k: -efet[k]):
        pv0, pvn, ca = PAPEL_4E[nome]
        pv = pv0 + pvn * NIVEL_4E
        alvo = (ca + NIVEL_4E) - atk
        acerto = max(0.05, min(0.95, (21 - alvo) / 20))
        print(f'    {nome:<12}{pv:>8.0f}{ca + NIVEL_4E:>7.1f}{acerto:>8.1%}{efet[nome]:>12.1f}'
              f'{efet[nome] / efet["Brute"]:>9.2f}x')
    dif = abs(efet['Soldier'] - efet['Brute']) / efet['Brute']
    print(f'    >> `Soldier` contra `Brute`: {dif:.1%} de diferença em PV efetivo.')
    print(f'    >> `Artillery` contra `Brute`: {efet["Artillery"] / efet["Brute"]:.0%} '
          f'— ele paga {1 - efet["Artillery"] / efet["Brute"]:.0%} da durabilidade')
    print()
print('  >> O par `Brute` / `Soldier` fica dentro de 10% em TODA a faixa, e aperta quanto mais')
print('     alto o acerto: 9,7% em 50%, 3,1% em 60%, 0,7% em 65%. O alvo de desenho do 4e')
print('     era o PC acertando monstro padrao em torno de 55% a 60% — e ali a diferenca e de')
print('     3% a 6%. ISSO e redistribuicao de verdade: o `Brute` compra PV cru com CA.')
print('  ⚠ A neutralidade NAO e exata, e ela depende da ancora. O que e robusto e a DIRECAO')
print('     e a ordem de grandeza, nao o empate no centavo.')
print('  >> E o `Artillery` paga 42% a 43% da durabilidade em TODAS as quatro ancoras — esse')
print('     numero nao se move. O que ele compra com isso esta no TEXTO da habilidade')
print('     (alcance), nao na tabela.')
print('  ⚠ E o 4e NAO COBRA por nada disso: o XP e funcao do nivel e do qualificador')
print('     (Minion 1/4, Elite 2x, Solo 5x). O papel nao entra no XP.')


# ===========================================================================
linha('2. O INVARIANTE da escada do Projeto-M — o que tem de ficar constante')
# ===========================================================================
print('  O que um inimigo custa num encontro e quanto dano ele entrega na luta inteira:')
print()
print('    dano total = dano por rodada x rodadas     e     rodadas = vida ÷ dano do grupo')
print('    entao  dano total ∝ VIDA x DANO.')
print()
print('  Se isso esta certo, o produto `vida x dano` tem de crescer com o QUADRADO das')
print('  pessoas que a categoria pede — porque dobrar as pessoas dobra o dano delas E')
print('  obriga o inimigo a durar o dobro.')
print()
base_c = 'Desastre'
print(f'  {"categoria":<14}{"pessoas":>9}{"vida x dano":>14}{"produto ÷ Desastre":>20}'
      f'{"(pessoas ÷ 4)²":>16}')
print('  ' + '-' * 74)
prod_base = CATS[base_c][30]['vida'] * CATS[base_c][30]['dano']
ok2 = True
for c in ORDEM:
    d = CATS[c][30]
    prod = d['vida'] * d['dano']
    razao = prod / prod_base
    esperado = (PESSOAS[c] / PESSOAS[base_c]) ** 2
    erro = abs(razao - esperado) / esperado
    if erro > 0.12:
        ok2 = False
    print(f'  {c:<14}{PESSOAS[c]:>9.0f}{prod:>14.0f}{razao:>19.2f}x{esperado:>15.2f}x'
          f'   {"ok" if erro <= 0.12 else f"ERRO {erro:.0%}"}')
print()
if ok2:
    print('  >> FECHA. O invariante de neutralidade e `vida x dano`, e ele vai com pessoas².')
    print('     Entao um papel que multiplica a vida por `m` e divide o dano por `m` NAO muda')
    print('     quantas pessoas o inimigo pede. Isso e a regra "redistribui" com conta.')
else:
    print('  !! NAO FECHA. O invariante `vida x dano` nao reproduz pessoas² — a regra de')
    print('     redistribuicao precisa de outro eixo.')


# ===========================================================================
linha('3. QUANTO ESPACO A BANDA DO `o golpe` DEIXA — e ela e apertada')
# ===========================================================================
print('  Subir o dano sobe `o golpe`, e a escada mede `o golpe` como fatia da vida de UM')
print(f'  personagem. A banda publicada e {BANDA[0]:.0%} a {BANDA[1]:.0%}, e foi passar dela que')
print('  matou a `Dupla` (ela chegou a 45%).')
print()
print(f'  {"categoria":<14}{"fatia hoje":>12}{"teto da banda":>15}{"dano pode subir":>18}')
print('  ' + '-' * 60)
TETO_DANO = {}
for c in ORDEM:
    f = FRAC[c]
    cresce = BANDA[1] / f
    TETO_DANO[c] = cresce
    print(f'  {c:<14}{f:>11.0%}{BANDA[1]:>14.0%}{cresce:>17.2f}x')
print()
print(f'  >> O `Desastre` e a `Calamidade` ja sentam no teto da banda ({FRAC["Desastre"]:.0%}).')
print(f'     Elas tem {TETO_DANO["Desastre"]:.2f}x de espaco — que e quase nada.')
print(f'  >> A `Ameaça` tem {TETO_DANO["Ameaça"]:.2f}x, porque ela senta em {FRAC["Ameaça"]:.0%}.')
print()
print('  ⚠ ISSO E O ACHADO QUE MANDA NO DESENHO: o eixo do DANO esta praticamente fechado')
print('     pra cima, e o espaco e DIFERENTE em cada categoria. Um papel que sobe o dano')
print('     quebraria a banda na categoria mais usada e caberia na menos usada.')
print('  >> A direcao que SOBRA e a de baixo: papel que DESCE o dano e sobe a vida cabe')
print('     sempre, porque `o golpe` sai da banda por baixo e o piso dela e 21%.')


# ===========================================================================
linha('3.5 O EIXO QUE O 4e USA, E QUE A BANDA NAO ALCANCA — `vida` contra `Defesa`')
# ===========================================================================
# O 4e NAO troca PV por dano. Ele troca PV por CA. E a banda do `o golpe` nao encosta
# nesse eixo, porque ele nao toca no dano.
ACERTO_PC = n(pega('sistema/03-mecanica/01-atributos-acerto-defesa.md',
                   r'Contra o alvo difícil, em que se acerta (\d+)%',
                   'o acerto contra alvo dificil').group(1)) / 100.0
DEF30 = None
for ln in TXT_T.split('\n'):
    m = re.match(r'\| 30 \| `\d+` \| `\d+` \| `\d+` \| `[^`]+` \| `(\d+)` \|', ln)
    if m:
        DEF30 = float(m.group(1))
        break
if DEF30 is None:
    print('  !! nao achei a Defesa do nivel 30 no TABELA.md')
    sys.exit(1)

print(f'  A Defesa do inimigo no nv30 e {DEF30:.0f}, e o personagem acerta alvo difícil em '
      f'{ACERTO_PC:.0%} (peça 1 §5.2).')
print(f'  1 ponto de Defesa move 5 pontos percentuais num d20.')
print()
print(f'  vida EFETIVA = vida ÷ chance de acerto. Entao mexer na Defesa e mexer na vida')
print(f'  efetiva SEM TOCAR NO DANO — e e por isso que a banda do `o golpe` nao alcança')
print(f'  este eixo. É o eixo que o 4e usa.')
print()
print(f'  {"Defesa":>8}{"acerto do PC":>15}{"vida efetiva":>15}{"vida crua precisa ser":>24}')
print('  ' + '-' * 64)
CAMBIO_DEF = {}
ef_base = 1.0 / ACERTO_PC
for dd in (-3, -2, -1, 0, +1, +2, +3):
    ac = min(0.95, max(0.05, ACERTO_PC - dd * 0.05))
    ef = 1.0 / ac
    fator = ef_base / ef
    CAMBIO_DEF[dd] = fator
    print(f'  {DEF30 + dd:>8.0f}{ac:>14.0%}{ef:>14.2f}x{fator:>23.2f}x')
print()
print(f'  >> O câmbio: `−1` de Defesa pede `×{CAMBIO_DEF[-1]:.2f}` de vida crua pra ficar neutro.')
print(f'     `−2` de Defesa pede `×{CAMBIO_DEF[-2]:.2f}`. `+2` de Defesa devolve '
      f'`×{CAMBIO_DEF[2]:.2f}`.')
print(f'  >> E isso E o `Brute` do 4e, traduzido: CA mais baixa, PV mais altos, durabilidade igual.')
print(f'  ⚠ E aqui NAO tem banda nenhuma no caminho: o dano nao se move, entao `o golpe` fica')
print(f'     exatamente onde a escada pôs ele.')
print()
print(f'  O `Brutamontes` e o `Guardião` medidos neste eixo, num Desastre nv30:')
print(f'    {"papel":<14}{"Defesa":>8}{"vida":>8}{"dano":>7}{"o golpe":>10}{"fatia":>8}'
      f'{"vida efetiva":>14}')
print('    ' + '-' * 70)
dd30 = CATS['Desastre'][30]
g_base = media_dado(dd30['golpe'])
for nome, dd in (('‹ sem papel ›', 0), ('Brutamontes', -2), ('Guardião', +2)):
    vida = dd30['vida'] * CAMBIO_DEF[dd]
    ac = min(0.95, max(0.05, ACERTO_PC - dd * 0.05))
    print(f'    {nome:<14}{DEF30 + dd:>8.0f}{vida:>8.0f}{dd30["dano"]:>7.0f}{g_base:>10.0f}'
          f'{g_base / VIDA_PC:>7.0%}{vida / ac:>14.0f}')
print()
print(f'  >> A vida efetiva fica IGUAL nos tres, e `o golpe` nao se move. Isso e')
print(f'     redistribuicao de verdade, com um numero que sai de conta e nao de gosto.')


# ===========================================================================
linha('4. OS SEIS PAPEIS — o que cada um pode trocar, medido')
# ===========================================================================
# o cambio de metro, lido do dono (peca 5 §4): mover 1,5 m vale 0,90
METRO = n(pega(P19, r'mover `1,5 m` \| `([\d,]+)`', 'o metro').group(1)) / 1.5
# a regua de condicao (peca 19 §2.2): uma acao do chefe
PONTO = n(pega(P19, r'vira `1d8` de dano — que são `([\d,]+)`', 'o ponto de feitico').group(1))
print(f'  câmbios lidos do dono:  1 m = {METRO:.2f} de dano por rodada (peça 19 §2.2, da peça 5 §4)')
print(f'                          dano evitado converte 1 pra 1 (peça 19 §2.2)')
print()
d30 = CATS['Desastre'][30]
UMA_ACAO = d30['dano'] / d30['acoes']
print(f'  e o Desastre nv30, que e a mesa padrao: vida {d30["vida"]:.0f}, dano {d30["dano"]:.0f}'
      f' em {d30["acoes"]:.0f} ações, uma ação = {UMA_ACAO:.2f}')
print()

# quanto vale ALCANCE, pelo cambio de metro do proprio sistema
ALC_CORPO, ALC_LONGE = 1.5, 18.0
VALE_ALCANCE = (ALC_LONGE - ALC_CORPO) * METRO
print(f'  ⚠ ALCANCE nao tem preco publicado. O unico cambio de metro que o sistema tem e o de')
print(f'     DESLOCAMENTO. Usando ele como convenção: sair de {ALC_CORPO:.1f} m pra {ALC_LONGE:.0f} m')
print(f'     vale {VALE_ALCANCE:.2f} de dano por rodada — {VALE_ALCANCE / d30["dano"]:.1%} da cota de '
      f'um Desastre.')
print(f'  >> Em vida, ao câmbio 1 pra 1 de dano evitado, isso é {VALE_ALCANCE:.0f} de vida por rodada')
print(f'     de luta. Numa luta de 3 rodadas, {VALE_ALCANCE * 3:.0f} de vida — '
      f'{VALE_ALCANCE * 3 / d30["vida"]:.1%} da vida dele.')
print()

PAPEIS = [
    ('Brutamontes', 'vida ↑, dano ↓', 'vida', 'dano',
     'desce `o golpe` — sai da banda por BAIXO, e o piso é 21%. CABE SEMPRE'),
    ('Artilheiro', 'vida ↓, alcance ↑', 'dano', 'vida',
     'NÃO sobe o dano: o espaço da banda é quase zero. Ele paga vida e ganha alcance'),
    ('Emboscador', 'mesmo dano/rodada, em MENOS ações', '—', '—',
     'concentra: sobe `o golpe` na proporção das ações cortadas. É o eixo PROIBIDO'),
    ('Controlador', 'dano ↓ → efeito', 'efeito', 'dano',
     'a régua da peça 19 §2.2 já converte: N ações negadas por M pontos'),
    ('Guardião', 'dano ↓ → dano negado no aliado', 'negação', 'dano',
     'dano evitado converte 1 pra 1 (peça 19 §2.2). Câmbio direto, sem conta nova'),
    ('Apoio', 'o próprio orçamento → o dos aliados', 'aliado', 'dano',
     'o mesmo 1 pra 1, só que o destino é outro bloco'),
]
print(f'  {"papel":<13}{"a troca":<36}{"cabe?":<8}')
print('  ' + '-' * 88)
for nome, troca, ganha, paga, nota in PAPEIS:
    print(f'  {nome:<13}{troca:<36}')
    print(f'  {"":<13}{nota}')
print()

# o Emboscador, medido: concentrar o mesmo dano em menos acoes
print('  O `Emboscador` medido — o unico dos seis que a banda REPROVA:')
print()
print(f'    {"ações":<8}{"o golpe":>10}{"fatia da vida de um PC":>26}{"dentro da banda?":>20}')
print('    ' + '-' * 62)
for acs in (3, 2, 1):
    golpe = d30['dano'] / acs
    frac = golpe / VIDA_PC
    dentro = BANDA[0] <= frac <= BANDA[1]
    print(f'    {acs:<8}{golpe:>10.2f}{frac:>25.0%}{"sim" if dentro else "NÃO":>20}')
print()
print(f'    >> Cortar de {d30["acoes"]:.0f} pra 2 ações joga `o golpe` em '
      f'{d30["dano"] / 2 / VIDA_PC:.0%} da vida de um personagem.')
print(f'    >> Cortar pra 1 joga em {d30["dano"] / 1 / VIDA_PC:.0%} — '
      f'que é MAIS que a `Dupla` que morreu (45%).')
print('    >> Então o `Emboscador` não pode concentrar o dano. Ele troca no eixo de')
print('       MOBILIDADE e de ESCONDER, que é onde o 4e põe o `Lurker`.')


# ===========================================================================
linha('5. E SE O PROJETO IMPORTASSE OS MODIFICADORES DO DRAW STEEL DIRETO')
# ===========================================================================
# ⚠ NUMEROS EXTERNOS. Fonte: `01-pesquisa/dmg2024-e-draw-steel.md`, secao
# `Adjusting Monster Levels`, e `fonte-4e-o-papel-com-numero.md` §3.
DS = {'Brute': (30, 1), 'Defender': (30, 0), 'Ambusher': (20, 1),
      'Harrier': (20, 0), 'Support': (20, 0), 'Artillery': (10, 1),
      'Controller': (10, 0), 'Hexer': (10, 0)}
NV_DS, ORG_DS, TIER_DS = 5, 1.0, 1.1
print(f'  Draw Steel, nível {NV_DS}, organização `Platoon` (×{ORG_DS:.0f}), tier {TIER_DS}:')
print(f'  Stamina = ((10 × nível) + mod. papel) × org    ·    dano = (4 + nível + mod. dano) × tier')
print(f'  E o EV — o custo — é ((2 × nível) + 4) × org = {((2 * NV_DS) + 4) * ORG_DS:.0f} '
      f'pra TODOS eles.')
print()
print(f'  {"papel":<12}{"Stamina":>9}{"dano":>7}{"EV":>6}{"Stamina ÷ Controller":>22}')
print('  ' + '-' * 58)
st_ctrl = ((10 * NV_DS) + DS['Controller'][0]) * ORG_DS
for nome in sorted(DS, key=lambda k: -DS[k][0]):
    mp, md = DS[nome]
    st = ((10 * NV_DS) + mp) * ORG_DS
    dn = (4 + NV_DS + md) * TIER_DS
    ev = ((2 * NV_DS) + 4) * ORG_DS
    print(f'  {nome:<12}{st:>9.0f}{dn:>7.1f}{ev:>6.0f}{st / st_ctrl:>21.2f}x')
print()
print('  >> O `Brute` tem 1,33x a Stamina do `Controller` e o MESMO EV.')
print('  >> O `Brute` e o `Artillery` tem o MESMO modificador de dano (+1) e o `Brute` tem')
print('     +20 de Stamina. O `Brute` e compra estritamente melhor, pelo mesmo preco.')
print('  ⚠ Isso NAO e neutro de orcamento. Importar esses modificadores direto traz de volta')
print('     o defeito que matou a `Dupla`: dois donos no mesmo numero.')


# ===========================================================================
linha('5.5 O `Líder` — se a categoria ganhar um degrau, que numero ele tem')
# ===========================================================================
# O `PAPEL-do-inimigo-base.md` propoe um `Lider` na categoria, "entre `Ameaca` e
# `Desastre`". A escada e' medida em PESSOAS, entao esse degrau pede 2 ou 3.
# E o invariante do §2 da o resto: vida x dano = (pessoas ÷ 4)² do Desastre.
print(f'  A escada mede em PESSOAS, e o invariante do §2 e `vida × dano ∝ pessoas²`.')
print(f'  Entao um degrau novo entre `Ameaça` (1) e `Desastre` (4) tem o numero determinado')
print(f'  pela escolha de quantas pessoas ele pede — e so sobra escolher as AÇÕES.')
print()
print(f'  {"pessoas":>8}{"fator":>8}{"vida":>8}{"dano":>7}{"ações":>7}{"o golpe":>10}'
      f'{"fatia da vida de um PC":>25}{"na banda?":>12}')
print('  ' + '-' * 86)
d_base = CATS['Desastre'][30]
for pes in (2, 3):
    fator = pes / PESSOAS['Desastre']       # o fator de vida E de dano, os dois iguais
    vida = d_base['vida'] * fator
    dano = d_base['dano'] * fator
    for acs in (1, 2, 3):
        golpe = dano / acs
        frac = golpe / VIDA_PC
        dentro = BANDA[0] <= frac <= BANDA[1]
        print(f'  {pes:>8}{fator:>8.2f}{vida:>8.0f}{dano:>7.0f}{acs:>7}{golpe:>10.1f}'
              f'{frac:>24.0%}{"sim" if dentro else "NÃO":>12}')
print()
print(f'  >> Com 2 pessoas, `1` ação joga `o golpe` em '
      f'{d_base["dano"] * (2 / PESSOAS["Desastre"]) / VIDA_PC:.0%} — fora da banda.')
print(f'     Com 2 pessoas e `2` ações ele cai em '
      f'{d_base["dano"] * (2 / PESSOAS["Desastre"]) / 2 / VIDA_PC:.0%}, dentro.')
print(f'  >> Com 3 pessoas e `2` ações da '
      f'{d_base["dano"] * (3 / PESSOAS["Desastre"]) / 2 / VIDA_PC:.0%}, dentro; com `3` ações da '
      f'{d_base["dano"] * (3 / PESSOAS["Desastre"]) / 3 / VIDA_PC:.0%}, dentro.')
print()
print(f'  ⚠ E o problema do `Líder` NAO e o numero — e o NOME.')
print(f'     O papel `Apoio` ja e "fortalece os outros, o proprio orcamento vira o dos aliados".')
print(f'     Um degrau de categoria chamado `Líder` que "melhora os outros" e a MESMA ideia')
print(f'     em dois eixos. Dois nomes pra uma coisa e o defeito que a skill de redacao chama')
print(f'     de "uma coisa por nome".')
print(f'  >> A saida limpa: o degrau de categoria e sobre TAMANHO (quantas pessoas), e o que')
print(f'     ele faz com os aliados e o PAPEL `Apoio` pendurado nele. `Desastre Apoio` ja diz.')


# ===========================================================================
linha('6. O VEREDITO')
# ===========================================================================
print(f'  1. O invariante de neutralidade e `vida x dano`, e ele reproduz pessoas² nas quatro')
print(f'     categorias. Um papel que faz vida x m e dano ÷ m nao muda o encontro.')
print()
print(f'  2. Mas a banda do `o golpe` ({BANDA[0]:.0%} a {BANDA[1]:.0%}) fecha o eixo do dano PRA CIMA:')
print(f'     o `Desastre` tem {TETO_DANO["Desastre"]:.2f}x de espaco e a `Ameaça` tem '
      f'{TETO_DANO["Ameaça"]:.2f}x.')
print(f'     O espaco e DIFERENTE por categoria, entao um `m` unico nao serve pros dois sentidos.')
print()
print(f'  3. A direcao de BAIXO cabe sempre. `Brutamontes` (vida ↑, dano ↓) e legal em qualquer')
print(f'     categoria; `Artilheiro` (dano ↑) nao e.')
print()
print(f'  4. Entao o `Artilheiro` tem de pagar de outro jeito: vida ↓ em troca de ALCANCE.')
print(f'     Pelo cambio de metro do proprio sistema, {ALC_LONGE:.0f} m valem '
      f'{VALE_ALCANCE:.2f} por rodada —')
print(f'     {VALE_ALCANCE * 3 / d30["vida"]:.0%} da vida dele numa luta de 3 rodadas. É pequeno.')
print()
print(f'  5. O `Emboscador` NAO pode concentrar dano: 2 acoes joga `o golpe` em '
      f'{d30["dano"] / 2 / VIDA_PC:.0%} da')
print(f'     vida de um personagem, e 1 acao em {d30["dano"] / VIDA_PC:.0%} — pior que a `Dupla`.')
print()
print(f'  6. `Controlador`, `Guardião` e `Apoio` sao os TRES FACEIS: a peca 19 §2.2 ja tem a')
print(f'     regua de converter dano em efeito, e `dano evitado converte 1 pra 1`.')
print()
print(f'  7. O precedente e o 4e, nao o Draw Steel. O 4e redistribui com numero e nao cobra')
print(f'     (o XP ignora o papel); o Draw Steel ADICIONA e tambem nao cobra, e por isso o')
print(f'     `Brute` dele e compra melhor que o `Artillery` pelo mesmo EV.')

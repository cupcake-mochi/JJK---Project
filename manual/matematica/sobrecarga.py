#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Quanto vale a `Sobrecarga`, somada — a da v0.221.

  `Sobrecarga` · `Leve` · Ate o fim do proximo turno do alvo, ele nao usa Reacao,
  e o feitico dele sai com a CD 2 menor.

Ate a v0.220 esta conta media outra Melhoria: "o feitico dele custa o dobro de
energia". Aquela metade valia ZERO contra inimigo (ele nao conta PE, peca 26
§6.1) e dobrava zero contra quem conjura Classe 0 — o mesmo buraco que a v0.217
fechou na `Divida`. Ela saiu por decisao do Mizuki em 09/09, e a metade que
entrou no lugar e' a Reacao. A secao `METADE 1` antiga deixou de existir.

Nenhum numero mora aqui dentro: cada um e' lido do documento dono, e o script
sai com erro se uma ancora sumir. A regua e' a da peca 19 §2.2, com as duas
perguntas separadas: o NIVEL sai de quantas acoes da rodada do alvo a coisa
nega, e o TESTE e' de dominancia contra o filtro.
"""
import os, re, sys

# a raiz sai do __file__, no molde dos validadores da casa: este arquivo mora em
# manual/matematica/, entao sao dois niveis acima.
# O JJK_RAIZ existe so' para o arnes rodar a conta contra uma copia perturbada.
RAIZ = os.environ.get(
    'JJK_RAIZ',
    os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                 '..', '..')))


def ler(rel):
    with open(os.path.join(RAIZ, rel), encoding='utf-8') as f:
        return f.read()


def num(s):
    return float(s.replace(',', '.'))


def pega(rel, padrao, rotulo, flags=0):
    m = re.search(padrao, ler(rel), flags)
    if not m:
        print(f'  !! ancora perdida: {rotulo} — nao casa em {rel}')
        sys.exit(1)
    return m


P03  = 'sistema/03-mecanica/03-economia-de-acao-e-iniciativa.md'
P19  = 'sistema/03-mecanica/19-dano-e-condicoes.md'
P26  = 'sistema/03-mecanica/26-bestiario.md'
DTRI = 'DESENHO-trilhas.md'
PARTD = 'manual/gerador/partD.js'
FUND  = 'sistema/05-material/livro/manual/40-fundamento.md'

print('=' * 86)
print('AS ANCORAS — lidas do dono, nenhuma escrita aqui')
print('=' * 86)

CHEFE = num(pega(DTRI, r'chefe (?:do nível 30 )?em `?(\d+)`? de dano por rodada', 'o chefe').group(1))
ACOES = num(pega(P19, r'O chefe age `(\d+)` vezes por rodada', 'acoes do chefe').group(1))
PONTO = num(pega(P19, r'cada ponto que não vira Melhoria vira `1d8` de dano — que são `([\d,]+)`',
                 'o ponto de feitico').group(1))
FILTRO = num(pega(P19, r'filtro de `([\d,]+)×`', 'o filtro de dominancia').group(1))
pega(P26, r'O inimigo não conta PE', 'o inimigo sem PE')
pega(P03, r'\*\*Reação\*\* \| uma, e ela volta no começo do seu turno', 'a Reacao, uma por rodada')
METADE = pega(PARTD, r'O alvo ainda faz o Teste de Resistência pra metade', 'a metade').group(0)

# a regra 1 do §2.2: quantas acoes negadas fazem cada degrau, lida por extenso
_PAL = {'meia': 0.5, 'uma': 1.0, 'uma e meia': 1.5}
m = pega(P19, r'(meia|uma e meia|uma) ação é `Leve`, (meia|uma e meia|uma) é `Média`, '
              r'(meia|uma e meia|uma) é `Pesada`', 'a escada de acoes negadas por degrau')
DEGRAU_ACOES = {'Leve': _PAL[m.group(1)], 'Média': _PAL[m.group(2)], 'Pesada': _PAL[m.group(3)]}

# o preco dos tres degraus por Classe, da tabela do §2.1
PRECO = {}
_t19 = ler(P19)
_i = _t19.find('| Classe | `Leve` | `Média` | `Pesada` | Rotina |')
if _i < 0:
    print('  !! ancora perdida: a tabela de preco por Classe da peca 19 §2.1')
    sys.exit(1)
for _ln in _t19[_i:].split('\n')[2:]:
    _c = [x.strip().strip('`') for x in _ln.strip().strip('|').split('|')]
    if len(_c) < 5 or not _c[0].isdigit():
        break
    PRECO[int(_c[0])] = {'Leve': int(_c[1]), 'Média': int(_c[2]), 'Pesada': int(_c[3])}
C_MAX = max(PRECO)

# ⚠ A DERIVACAO DE QUE A CONTA INTEIRA DEPENDE: quanto vale a Reacao do inimigo.
# Ela nao esta escrita como numero em lugar nenhum — sai do `Atordoado` publicado.
# O texto dele e' "perde a Acao Padrao E NAO USA REACAO", e a tabela das treze
# publica as acoes negadas dele. Tira a Acao Padrao (UMA, pela propria celula) e
# o que sobra e' a Reacao.
m = pega(P19, r'\| \*\*`Atordoado`\*\* \| `([\d,]+)` \| `([\d,]+)`', 'a linha do `Atordoado` na tabela das treze')
ATORD_NEGA, ATORD_ACOES = num(m.group(1)), num(m.group(2))
m = pega(P19, r'\| \*\*`Atordoado`\*\* \| `Pesada` \| \*\*([^*]+)\*\*', 'o texto do `Atordoado`')
if 'não usa reação' not in m.group(1) or 'perde a Ação Padrão' not in m.group(1):
    print('  !! o texto do `Atordoado` parou de dizer que tira a Acao Padrao E a reacao — a '
          'derivacao do preco da Reacao perdeu o chao')
    sys.exit(1)
UMA_ACAO = CHEFE / ACOES
FRACAO_REACAO = ATORD_ACOES - 1.0
A_REACAO = FRACAO_REACAO * UMA_ACAO
if abs(ATORD_ACOES * UMA_ACAO - ATORD_NEGA) > 0.01:
    print(f'  !! {ATORD_ACOES} x {UMA_ACAO:.2f} nao da os {ATORD_NEGA} que a peca 19 publica pro '
          '`Atordoado` — a acao do chefe mudou de um lado so')
    sys.exit(1)

# a Sobrecarga, nos dois donos do texto: o degrau e o texto tem de ser o mesmo
m_ger = pega(PARTD, r"\['Sobrecarga', '(\w+)', '([^']+)'\]", 'a `Sobrecarga` no gerador')
m_liv = pega(FUND, r'^\| `Sobrecarga` \| `(\w+)` \| ([^|]+?) \|\s*$', 'a `Sobrecarga` no livro', re.M)
TIER, TEXTO = m_ger.group(1), m_ger.group(2)
if (m_liv.group(1), m_liv.group(2).strip()) != (TIER, TEXTO):
    print(f'  !! a `Sobrecarga` diverge: `{TIER}` no gerador e `{m_liv.group(1)}` no livro, ou o '
          'texto nao e o mesmo — a v0.221 fechou essa divergencia')
    sys.exit(1)
if 'dobro de energia' in TEXTO or 'não usa Reação' not in TEXTO:
    print(f'  !! o texto da `Sobrecarga` nao e o da v0.221: "{TEXTO}"')
    sys.exit(1)
DELTA_CD = int(pega(PARTD, r"\['Sobrecarga', '\w+', '[^']*CD (\d+) menor", 'o tamanho da CD').group(1))

print(f'  chefe nv30                 {CHEFE:.0f} de dano por rodada, em {ACOES:.0f} acoes')
print(f'  1 ponto de feitico         {PONTO:.1f} de dano')
print(f'  filtro de dominancia       {FILTRO:.2f}x')
print(f'  acoes negadas por degrau   Leve {DEGRAU_ACOES["Leve"]} · Média {DEGRAU_ACOES["Média"]} '
      f'· Pesada {DEGRAU_ACOES["Pesada"]}')
print(f'  a `Sobrecarga`             `{TIER}` nos dois donos: "{TEXTO}"')
print()
print(f'  >> UMA acao do chefe       {UMA_ACAO:.2f} de dano')
print(f'  >> a REACAO do inimigo     {A_REACAO:.2f} de dano  ({FRACAO_REACAO:.1f} acao)')
print(f'     derivada do `Atordoado`: ele tira a Acao Padrao e a reacao, e a peca 19 publica')
print(f'     {ATORD_ACOES:.1f} acoes negadas. {ATORD_ACOES:.1f} - 1 = {FRACAO_REACAO:.1f}. '
      f'Confere: {ATORD_ACOES:.1f} x {UMA_ACAO:.2f} = {ATORD_NEGA:.2f}.')

print()
print('=' * 86)
print('O QUE ELA ENTREGA — as duas metades')
print('=' * 86)
print(f'  METADE 1 — ele nao usa Reacao        {A_REACAO:>7.2f} de dano por rodada')
print( '    a Reacao volta no comeco do turno dele (peca 3 §2) e cai na trava de novo;')
print( '    a janela e a mesma do `Atordoado`, e nao precisa de regra nova.')
# 2 pontos num d20 sao 10 pontos percentuais, e um TR bem-sucedido corta o dano
# pela metade — entao a massa que se desloca troca dano cheio por metade.
NEGA_CD = (DELTA_CD / 20.0) / 2.0
CD_TETO = CHEFE * NEGA_CD
CD_PISO = UMA_ACAO * NEGA_CD
print(f'  METADE 2 — a CD {DELTA_CD} menor               nega {NEGA_CD:.1%} de cada golpe que pede TR')
print(f'    teto (as {ACOES:.0f} acoes pedem TR)          {CD_TETO:>7.2f}')
print(f'    piso (1 acao pede TR)               {CD_PISO:>7.2f}')
TOT_PISO, TOT_TETO = A_REACAO + CD_PISO, A_REACAO + CD_TETO
print(f'  SOMADA                                {TOT_PISO:>7.2f} a {TOT_TETO:.2f}')

print()
print('=' * 86)
print('O VEREDITO — o degrau pela regra 1, e a dominancia nele')
print('=' * 86)


def degrau(acoes):
    for t in ('Pesada', 'Média', 'Leve'):
        if acoes >= DEGRAU_ACOES[t] - 1e-9:
            return t
    return None


PELA_REGRA = degrau(FRACAO_REACAO)
CUSTO = PRECO[C_MAX][TIER] * PONTO
D_PISO, D_TETO = TOT_PISO / CUSTO, TOT_TETO / CUSTO
band = re.findall(r'\| \*\*`([^`]+)`\*\* \| `[\d,]+` \| [^|]*\| `(\d+)` \| `([\d,]+)×` \| `(\w+)` \|', _t19)
if len(band) != 13:
    print(f'  !! li {len(band)} linhas da tabela das treze, e sao 13. A forma mudou.')
    sys.exit(1)
faixa = sorted(num(d) for _, _, d, t in band if t == TIER)
print(f'  a Reacao nega {FRACAO_REACAO:.1f} acao  ⟹ pela regra 1 o degrau e `{PELA_REGRA}`, '
      f'e os dois donos publicam `{TIER}`.')
print(f'  na Classe {C_MAX}, `{TIER}` custa {PRECO[C_MAX][TIER]} pontos = {CUSTO:.1f} de dano.')
print(f'  dominancia: {D_PISO:.2f}x a {D_TETO:.2f}x, contra o filtro de {FILTRO:.2f}x.')
print(f'  as condicoes `{TIER}` ja publicadas vivem de {faixa[0]:.2f}x a {faixa[-1]:.2f}x.')
ruim = []
if PELA_REGRA != TIER:
    ruim.append(f'a regra 1 manda `{PELA_REGRA}` e os donos publicam `{TIER}`')
if D_TETO > FILTRO:
    ruim.append(f'o teto de {D_TETO:.2f}x passa do filtro de {FILTRO:.2f}x')
print()
if ruim:
    for r in ruim:
        print(f'  !! {r}')
    sys.exit(1)
print(f'  >> PASSA: `{TIER}` e o degrau que a regra 1 manda, e a Melhoria inteira fica abaixo')
print(f'     do filtro em qualquer mistura de acerto e TR.')

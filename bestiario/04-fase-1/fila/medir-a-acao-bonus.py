#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
O inimigo tem AÇÃO BÔNUS?

Pergunta do Mizuki, 10/09/2026: *"Eu notei q falta, a gente coloca ação bonus?"*

⚠ E a resposta nao e' decisao nova: o sistema JA PRECA a Acao Bonus do inimigo, e
ela ja esta dentro de uma condicao publicada. So' o bloco nao imprime a linha.

A prova esta no `Lento`.
"""
import os, re, sys

REPO = os.environ.get('JJK_REPO', '/media/mizuki/HD Externo II/Claude/Claude 2')
BEST = os.environ.get('JJK_BEST', '/media/mizuki/HD Externo II/Claude/Claude 2/bestiario')

P19 = 'sistema/03-mecanica/19-dano-e-condicoes.md'
P03 = 'sistema/03-mecanica/03-economia-de-acao-e-iniciativa.md'
P26 = 'sistema/03-mecanica/26-bestiario.md'
FUND = 'sistema/05-material/livro/manual/40-fundamento.md'
TABELA = '04-fase-1/TABELA.md'


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


# ===========================================================================
linha('1. O QUE O BLOCO DECLARA HOJE — e o que ele NAO declara')
# ===========================================================================
print('  A peça 26 §3 lista dezessete linhas da ficha. Sobre economia de ação ela diz:')
a1 = pega(P26, r'\| ações por rodada \| ([^|]+) \|', 'as ações por rodada').group(1).strip()
a2 = pega(P26, r'\| Reação \| ([^|]+) \|', 'a Reação').group(1).strip()
print(f'    ações por rodada   {a1}')
print(f'    Reação             {a2}')
print()
tem_bonus = re.search(r'\| [Aa]ção [Bb]ônus \|', ler(P26))
print(f'    Ação Bônus         {"declarada" if tem_bonus else "⚠ NAO APARECE EM LUGAR NENHUM"}')
print()
print('  E o jogador tem as quatro, pela peça 3:')
m3 = pega(P03, r'\| \*\*Reação\*\* \| ([^|]+) \|', 'a Reação do jogador')
print(f'    Ação Padrão · Ação Bônus · Reação · movimento')


# ===========================================================================
linha('2. MAS O CATALOGO DO INIMIGO E O MESMO DO JOGADOR — e ele TEM Ação Bônus')
# ===========================================================================
cat = pega(P26, r'refino, aptidão, Passiva e técnica saem do mesmo catálogo',
           'o catalogo compartilhado').group(0)
print(f'  peça 26 §6: "{cat}"')
print()
print('  E o catálogo tem coisa que custa Ação Bônus:')
ACHADOS = [
    ('`Rápido`', 'Melhoria `Pesada`', 'Custa Ação Bônus em vez de Ação Padrão'),
    ('`Ímpeto`', 'Classe Passiva 2', 'Como Ação Bônus, você se move até o seu deslocamento'),
    ('`Campo`', 'Classe Passiva 1', 'A ação `Estudar` custa a sua Ação Bônus'),
    ('`Energia Reversa`', 'aptidão', 'pode ser usada como Ação Bônus, com `d4` em vez de `d8`'),
]
for nome, onde, txt in ACHADOS:
    print(f'    {nome:<20}{onde:<20}{txt}')
print()
print('  ⚠ Então uma aptidão que custa Ação Bônus NAO TEM ONDE CABER na ficha do inimigo.')


# ===========================================================================
linha('3. A PROVA — o `Lento` ja preca a Acao Bonus DO INIMIGO')
# ===========================================================================
mL = pega(FUND, r'\| `Lento` \| ([^|]+) \|', 'o texto do Lento')
print(f'  O texto do `Lento`, no manual: "{mL.group(1).strip()}"')
print()
print('  E a peça 19 §2.2 publica o valor dele CONTRA O CHEFE:')
mrow = pega(P19, r'\| \*\*`Lento`\*\* \| `([\d,]+)` \| `([\d,]+)`[^|]*\|', 'a linha do Lento')
LENTO_NEGA, LENTO_ACOES = n(mrow.group(1)), n(mrow.group(2))
print(f'    nega {LENTO_NEGA:.2f} de dano por rodada · {LENTO_ACOES:.1f} ações negadas')
print()
# as ancoras que reconstroem o Lento
METRO = n(pega(P19, r'mover `1,5 m` \| `([\d,]+)`', 'o metro').group(1)) / 1.5
mD = pega(TABELA, r'## `Desastre`[\s\S]*?\n\| 30 \| `\d+` \| `(\d+)` \| `(\d+)` \|',
          'o Desastre nv30', BEST)
DANO_D, ACOES_D = n(mD.group(1)), n(mD.group(2))
UMA_ACAO = DANO_D / ACOES_D
MEIO_DESLOC = 4.5      # metade de 9 m
print(f'  Reconstruindo ele das ancoras:')
print(f'    metade do deslocamento    {MEIO_DESLOC:.1f} m × {METRO:.2f} = {MEIO_DESLOC*METRO:.2f}')
print(f'    a AÇÃO BÔNUS              {LENTO_ACOES:.1f} × {UMA_ACAO:.2f} = {LENTO_ACOES*UMA_ACAO:.2f}')
total = MEIO_DESLOC * METRO + LENTO_ACOES * UMA_ACAO
print(f'    {"":<26}{"—":>22}')
print(f'    total                     {total:.2f}')
print()
if abs(total - LENTO_NEGA) > 0.01:
    print(f'  !! reconstruí {total:.2f} e a peça publica {LENTO_NEGA:.2f}. A decomposição está errada.')
    sys.exit(1)
print(f'  [x] FECHA EXATO: {total:.2f} = os {LENTO_NEGA:.2f} publicados.')
print()
print('  >> O `Lento` tira DUAS coisas: metade do deslocamento e a Ação Bônus.')
print(f'  >> A metade do deslocamento vale {MEIO_DESLOC*METRO:.2f}. Todo o resto — '
      f'{LENTO_ACOES*UMA_ACAO:.2f} — é a AÇÃO BÔNUS.')
print()
print('  ⚠⚠ ENTAO O SISTEMA JA DECIDIU: o inimigo TEM Ação Bônus, e ela vale')
print(f'     {LENTO_ACOES:.1f} ação = {LENTO_ACOES*UMA_ACAO:.2f} de dano por rodada.')
print('     O `Lento` cobra por tirar ela. Se o inimigo nao tivesse, o `Lento` estaria')
print(f'     sobreprecado em {LENTO_ACOES*UMA_ACAO/LENTO_NEGA:.0%} contra inimigo — e ele e uma das treze')
print('     condicoes publicadas, com validador em cima.')


# ===========================================================================
linha('4. E E O MESMO TAMANHO DA REACAO — as duas valem meia acao')
# ===========================================================================
mA = pega(P19, r'\| \*\*`Atordoado`\*\* \| `([\d,]+)` \| `([\d,]+)`[^|]*\|', 'o Atordoado')
AT_ACOES = n(mA.group(2))
print(f'  a `Reação`      derivada do `Atordoado`: {AT_ACOES:.1f} − 1,0 = '
      f'{AT_ACOES-1:.1f} ação = {(AT_ACOES-1)*UMA_ACAO:.2f}')
print(f'  a `Ação Bônus`  derivada do `Lento`:     {LENTO_ACOES:.1f} ação = '
      f'{LENTO_ACOES*UMA_ACAO:.2f}')
print()
print('  >> As duas valem MEIA AÇÃO, e as duas foram derivadas de condicoes publicadas')
print('     diferentes, sem se falarem. Duas rotas, o mesmo numero.')


# ===========================================================================
linha('5. O QUE FALTA FAZER — e nao e' + ' recalibrar')
# ===========================================================================
print('  A Ação Bônus do inimigo JA ESTA no orçamento — ela foi preçada quando o `Lento`')
print('  foi preçado. O que falta é o bloco DIZER que ela existe.')
print()
print('  E ela nao muda a cota de dano, pelo mesmo motivo que a Intervencao 2 e 3 nao mudam:')
print('  o que se faz com Acao Bonus no catalogo do jogador quase nunca e dano —')
print('  `Ímpeto` move, `Campo` estuda, `Energia Reversa` cura. So o `Rápido` conjura.')
print()
print(f'  {"cenário":<44}{"soma na cota?":>16}')
print('  ' + '-' * 62)
print(f'  {"Ação Bônus usada pra mover / posicionar":<44}{"não":>16}')
print(f'  {"Ação Bônus usada pra curar aliado":<44}{"não":>16}')
print(f'  {"Ação Bônus com `Rápido` — conjura":<44}{"SIM":>16}')
print()
print('  >> Entao a linha do bloco tem de existir, e o que ela CARREGA e escolha:')
print('     ou "1 por rodada, e o que couber nela", ou "1 por rodada, e ela nao causa dano".')

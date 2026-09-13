# -*- coding: utf-8 -*-
"""Quanto do PE do dia o degrau sem barreira come, a 6x e a 8x a maior Classe.

Rascunho da Expansao sem barreira (sistema/03-mecanica/RASCUNHO-expansao-sem-barreira.md),
rodada 1, 12/09/2026. Nenhum numero digitado: cada um sai do documento dono.

  PE por nivel          peca 6, a tabela "PE por nivel" dos cinco Caminhos
  maior Classe          peca 18, a coluna Classe da tabela de progressao
  refino por rota       peca 11, a tabela especialista / meio a meio / generalista
  desconto e duracao    o livro, capitulo 40: metade do refino, nas duas coisas
"""
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
M = os.path.join(RAIZ, 'sistema', '03-mecanica')


def ler(*partes):
    with open(os.path.join(*partes), encoding='utf-8') as fh:
        return fh.read()


def ancora(padrao, texto, onde):
    m = re.search(padrao, texto, re.M)
    if not m:
        print(f'ANCORA PERDIDA: {onde}')
        sys.exit(1)
    return m


p6 = ler(M, '06-caminhos-e-trilhas.md')
cab = ancora(r'^\| \| (Bastião \| .*?) \|$', p6, 'o cabecalho dos Caminhos na peca 6').group(1).split(' | ')
pe = [int(x) for x in ancora(r'^\| PE por nível \| (.*?) \|$', p6, 'PE por nivel na peca 6').group(1).split(' | ')]
PE = dict(zip(cab, pe))

p18 = ler(M, '18-progressao.md')
CL = {int(a): int(b) for a, b in re.findall(
    r'^\| \*\*(\d+)\*\* \| [\d.—]+ \| \d+ \| \d+ \| \d+ \| (\d+) \|', p18, re.M)}
if not all(n in CL for n in (22, 26, 30)):
    print('ANCORA PERDIDA: a coluna Classe da peca 18 nos niveis 22, 26 e 30')
    sys.exit(1)

p11 = ler(M, '11-aptidoes-e-refino.md')
NIV = [int(x) for x in re.findall(r'nv (\d+)', ancora(
    r'^\| \| nv 6 \| nv 10 \| nv 14 \| nv 18 \| nv 22 \| nv 26 \| nv 30 \|$', p11,
    'o cabecalho da tabela de refino na peca 11').group(0))]
ROTA = {}
for nome in ('especialista', 'meio a meio', 'generalista'):
    linha = ancora(r'^\| \*\*' + nome + r'\*\*[^|]*\|(.*)$', p11, f'a linha {nome} na peca 11').group(1)
    ROTA[nome] = [int(x) for x in re.findall(r'`(\d+)`', linha)]

livro = ler(RAIZ, 'sistema', '05-material', 'livro', 'manual', '40-fundamento.md')
ancora(r'\*\*−metade do refino\*\* na completa', livro, 'o desconto da completa no livro')
ancora(r'\*\*Dura metade do refino em rodadas\*\*', livro, 'a duracao no livro')
ancora(r'as duas cobram \*\*6 × a sua maior Classe\*\* de PE', livro, 'o custo de abrir no livro')

print('REFINO 10 CHEGA EM (peca 11):')
for nome, v in ROTA.items():
    n = next((NIV[i] for i, r in enumerate(v) if r >= 10), None)
    print(f'  {nome:13s} nivel {n if n else "NUNCA"}')
print()
print(f'{"nivel":7s}{"Classe":8s}{"6x":6s}{"8x":6s}{"Bastiao":16s}Emanador')
for n in (22, 26, 30):
    c = CL[n]
    b, e = PE['Bastião'] * n, PE['Emanador'] * n
    print(f'{n:<7d}{c:<8d}{6*c:<6d}{8*c:<6d}{100*6*c/b:3.0f}% -> {100*8*c/b:3.0f}%    '
          f'{100*6*c/e:3.0f}% -> {100*8*c/e:3.0f}%')
print()
poupa = (10 // 2) * (10 // 2)
print(f'refino 10: desconto de {10//2} PE por feitico, {10//2} rodadas -> no maximo {poupa} PE poupados')
for n in (22, 26, 30):
    c = CL[n]
    print(f'  nivel {n}: abrir 6x = {6*c} (saldo {poupa-6*c:+d}) · abrir 8x = {8*c} (saldo {poupa-8*c:+d})')

# ---------------------------------------------------------------------------
# RODADA 1, segunda parte (12/09/2026): a proposta do Mizuki para o degrau
#   abrir a 7 x a maior Classe · desconto de dentro = maestria x 2, minimo 1 PE
#   por feitico · 4 ou 5 espacos, "valide"
# ---------------------------------------------------------------------------
print()
print('=' * 78)
print('A PROPOSTA DA RODADA 1: 7x, desconto de maestria x 2, e 4 ou 5 espacos')
print('=' * 78)

LIN = {}
for m in re.finditer(r'^\| \*{0,2}(\d+)\*{0,2} \| [\d.—]+ \| (\d+) \| (\d+) \| (\d+) \| (\d+) \|', p18, re.M):
    LIN[int(m.group(1))] = {'maestria': int(m.group(2)), 'espacos': int(m.group(3)), 'classe': int(m.group(5))}
if not all(n in LIN for n in (10, 14, 22, 26, 30)):
    print('ANCORA PERDIDA: as linhas 10, 14, 22, 26 e 30 da tabela de progressao da peca 18')
    sys.exit(1)

m_inc = ancora(r'\| \*\*Incompleta\*\* \| (\d+) espaços \| nível (\d+) e refino (\d+) \|', livro, 'o degrau Incompleta no livro')
m_com = ancora(r'\| \*\*Completa\*\* \| (\d+) espaços \(\+1\) \| nível (\d+) e refino (\d+) \|', livro, 'o degrau Completa no livro')
m_uma = ancora(r'regra de ouro nº 6:\*{0,2} \*feitiço em Ação Bônus ou Reação só permite mais um de Classe 0 no turno', livro,
               'a regra de ouro no 6 no livro — um feitico pago por turno')
m_st = ancora(r'cinco Passivas de Classe 3 mais Expansão completa eram impossíveis em qualquer nível — dezoito espaços numa ficha de dezesseis',
              p18, 'o teste de carga dos espacos na peca 18')
PASSIVA3 = (18 - int(m_com.group(1))) // 5      # dezoito = cinco Passivas de Classe 3 + a Completa

print()
print('custo liquido de abrir, com um feitico pago por turno durante a duracao inteira (regra de ouro no 6)')
print('(a duracao continua metade do refino; refino 10 -> 5 rodadas; so conta feitico que custa mais que o desconto)')
print(f'{"nivel":7s}{"degrau":30s}{"abrir":7s}{"desconto":10s}{"poupa":7s}{"saldo":7s}Bastiao')
for n in (22, 26, 30):
    L = LIN[n]
    c, mae = L['classe'], L['maestria']
    b = PE['Bastião'] * n
    dur = 10 // 2
    for nome, abrir, desc in (('Completa (6x, metade do refino)', 6 * c, 10 // 2),
                              ('sem barreira (7x, maestria x 2)', 7 * c, 2 * mae)):
        poupa = dur * desc
        print(f'{n:<7d}{nome:30s}{abrir:<7d}{desc:<10d}{poupa:<7d}{poupa-abrir:<+7d}{100*abrir/b:3.0f}%')
print('  -> saldo negativo nos dois: abrir continua sendo preco, e o bloco 7 do conferir-expansao nao quebra')

print()
print('a fatia da lista de feitico que cada degrau come NO NIVEL EM QUE ABRE')
inc_e, inc_n = int(m_inc.group(1)), int(m_inc.group(2))
com_e, com_n = int(m_com.group(1)), int(m_com.group(2))
print(f'  Incompleta   {inc_e} de {LIN[inc_n]["espacos"]:2d} no nivel {inc_n}  = {100*inc_e/LIN[inc_n]["espacos"]:3.0f}%')
print(f'  Completa     {com_e} de {LIN[com_n]["espacos"]:2d} no nivel {com_n}  = {100*com_e/LIN[com_n]["espacos"]:3.0f}%')
for n in (22, 26):
    for e in (4, 5):
        print(f'  sem barreira {e} de {LIN[n]["espacos"]:2d} no nivel {n}  = {100*e/LIN[n]["espacos"]:3.0f}%')

print()
print(f'o teste de carga da peca 18: cinco Passivas de Classe 3 = {5*PASSIVA3} espacos, mais o degrau')
for n in (22, 26, 30):
    tot = LIN[n]['espacos']
    for e in (4, 5):
        sobra = tot - 5 * PASSIVA3 - e
        print(f'  nivel {n} ({tot} espacos), degrau a {e}: sobram {sobra:+d} para feitico'
              + ('   <- NAO CABE' if sobra < 0 else ''))

# ---------------------------------------------------------------------------
# RODADA 1, quarta parte (12/09/2026): pedido do Mizuki — "mostre quantos feiticos
# a pessoa tem no nv22 e 26, simule caso ela gaste em feiticos tambem, e explique
# por que uma pessoa nv22 conseguiria pegar com refino 10 e especializacao"
# ---------------------------------------------------------------------------
print()
print('=' * 78)
print('QUEM CHEGA NO NIVEL 22 COM REFINO 10 E ESPECIALIZACAO — e o que sobra de feitico')
print('=' * 78)

m_pas = ancora(r'cada \*\*Passiva\*\* paga custa de (\d) a (\d) espaços, e a \*\*Expansão de Domínio\*\* custa (\d) ou (\d)',
               livro, 'o custo em espaco de Passiva e Expansao no livro')
ancora(r'^Máximo de cinco Passivas pagas\. A Passiva Livre não conta\.$', livro, 'o teto de cinco Passivas pagas no livro')
ancora(r'Do nível 10 em diante, no lugar da perícia ou do ofício novo', p11, 'a especializacao no eixo Corpo, peca 11')
ancora(r'passa a levar duas aptidões', p11, 'a escolha de Refino levando duas aptidoes no marco 22, peca 11')
m_cl0 = {int(a): int(b) for a, b in re.findall(
    r'^\| \*{0,2}(\d+)\*{0,2} \| [\d.—]+ \| \d+ \| \d+ \| \d+ \| \d+ \| \d+ \| (\d+) \|', p18, re.M)}
p7 = ler(M, '07-pericias-e-oficios.md')
ancora(r'^\*\*Ocultismo\*\* — maldições, técnicas conhecidas, barreiras', p7, 'o que o Ocultismo cobre, peca 7')

print()
print('A ROTA QUE SEMPRE ESCOLHE REFINO, marco a marco (peca 11):')
print('  o refino sobe +1 de graca em todo marco, e +1 se voce escolher Refino, ate o teto 10')
ref = 1
print(f'  {"marco":7s}{"escolha":34s}{"refino":8s}')
for mc in (6, 10, 14, 18, 22):
    if mc < 22:
        ref = min(10, ref + 2)
        esc = 'Refino (+1 refino e 1 aptidao)'
    else:
        ref = min(10, ref + 1)
        esc = 'Corpo (+1 atributo e especializa)'
    print(f'  {mc:<7d}{esc:34s}{ref:<8d}')
print('  -> no marco 22 o +1 de graca ja leva o refino de 9 a 10. Escolher Refino ali')
print('     nao sobe mais refino: vira duas aptidoes. Entao o marco 22 fica livre pra')
print('     Corpo, e o Corpo especializa o Ocultismo (que ela ja treinava).')
print('  -> o preco real de especializar no 22 e abrir mao de DUAS APTIDOES, e nao de refino.')

print()
print('ESPACOS: quanto sobra pra feitico montado depois das Passivas e da Expansao')
print(f'  (Passiva paga come espaco igual a Classe dela, de {m_pas.group(1)} a {m_pas.group(2)}; no maximo cinco;')
print('   feitico de Classe 0 nao ocupa espaco e vem por fora)')
CARGAS = [
    ('nenhuma Passiva paga',              []),
    ('2 Passivas de Classe 3',            [3, 3]),
    ('5 Passivas: Classe 3,3,2,2,1',      [3, 3, 2, 2, 1]),
    ('5 Passivas de Classe 3 (carga max)', [3, 3, 3, 3, 3]),
]
for n in (22, 26):
    tot = LIN[n]['espacos']
    print()
    print(f'  NIVEL {n}: {tot} espacos, mais {m_cl0[n]} feiticos de Classe 0 de graca')
    print(f'  {"as Passivas":36s}{"com a Completa (3)":22s}{"com o degrau (5)":18s}')
    for nome, cls in CARGAS:
        s3 = tot - sum(cls) - 3
        s5 = tot - sum(cls) - 5
        f = lambda s: (f'{s:2d} feiticos' if s >= 0 else f'falta {-s}  <- NAO CABE')
        print(f'  {nome:36s}{f(s3):22s}{f(s5):18s}')

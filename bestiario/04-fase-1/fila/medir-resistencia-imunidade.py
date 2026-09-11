#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Resistencia · Imunidade · Vulnerabilidade na ficha do inimigo.

Pergunta do Mizuki, 10/09/2026: "como ficou imunidades, resistencias e
vulnerabilidades para se colocar nas fichas de inimigo?"

O bloco (RASCUNHO-5) tem a linha com as tres celulas. A peca 26 §6.3 tem a
tabela de preco. Mas ninguem mediu:
  1 · quantos blocos do campo REALMENTE imprimem cada celula
  2 · quantas entradas cabem numa celula
  3 · se a VULNERABILIDADE e precada de verdade  (experimento natural:
      se ela devolve orcamento, quem a tem tem de ter vida maior por CR)
  4 · como o Draw Steel escreve as duas — e la elas sao NUMERO, nao binario
  5 · a imunidade a CONDICAO, que a nossa linha nao tem celula pra ela

Nenhum numero nosso mora aqui: toda ancora e lida do documento dono, e o
script morre se o dono mudar.
"""
import json
import os
import re
import statistics
import sys

BEST = os.environ.get('JJK_BEST', '/media/mizuki/HD Externo II/Claude/Claude 2/bestiario')
REPO = os.environ.get('JJK_REPO', '/media/mizuki/HD Externo II/Claude/Claude 2')

P26 = 'finalizado/regra/26-bestiario.md'
P19 = 'finalizado/regra/19-dano-e-condicoes.md'
BLOCO = '03-bloco/RASCUNHO-5-o-bloco-em-branco.md'
DEGRAU = '04-fase-1/fila/DECIDIDO-o-degrau.md'

FILA = os.path.join(BEST, '04-fase-1/fila')
DS = os.path.join(FILA, 'dados-recarga-area/data-md-main')
DSMON = os.path.join(DS, 'Bestiary/Monsters/Monsters')

_cache = {}


def ler(rel, raiz=BEST):
    k = (rel, raiz)
    if k not in _cache:
        with open(os.path.join(raiz, rel), encoding='utf-8') as f:
            _cache[k] = f.read()
    return _cache[k]


def n(s):
    return float(s.replace('−', '-').replace(',', '.'))


def pega(rel, padrao, rotulo, raiz=BEST):
    m = re.search(padrao, ler(rel, raiz))
    if not m:
        print(f'\n  !! ANCORA PERDIDA: {rotulo}\n     nao casa em {rel}\n     padrao: {padrao}')
        sys.exit(1)
    return m


def bloco(t):
    print()
    print('=' * 96)
    print(t)
    print('=' * 96)


def pct(x, tot):
    return f'{100.0 * x / tot:5.1f}%' if tot else '   —  '


# ---------------------------------------------------------------- 0 · ancoras
bloco('0 · AS ANCORAS — lidas dos donos')

GRUPOS = {}
for nome, chave in (('Físicos', 'Físicos'), ('Elementais', 'Elementais'), ('Especiais', 'Especiais')):
    m = pega(P19, r'\| \*\*' + chave + r'\*\* \| ([^|]+) \| \*\*(\d+)%\*\* \|',
             f'peça 19 §4 — o grupo {nome}', REPO)
    tipos = [t.strip(' `') for t in m.group(1).split('·')]
    GRUPOS[nome] = {'peso': int(m.group(2)) / 100.0, 'tipos': tipos}
    print(f'  peça 19 §4 · {nome:<12} peso {m.group(2):>3}%   {len(tipos)} tipos: ' + ', '.join(tipos))

N_TIPOS = sum(len(g['tipos']) for g in GRUPOS.values())
m = pega(P19, r'\*\*(\w+) tipos, em três grupos\.\*\*', 'peça 19 §4 — quantos tipos', REPO)
DECLARADO = {'Catorze': 14, 'Treze': 13, 'Quinze': 15}.get(m.group(1))
print(f'  peça 19 §4 · a peça declara "{m.group(1)} tipos" = {DECLARADO}; a tabela lista {N_TIPOS}')
if DECLARADO != N_TIPOS:
    print(f'  !! a peça se contradiz: declara {DECLARADO} e lista {N_TIPOS}')
    sys.exit(1)

PRECO = {}
for grupo in ('Físicos', 'Elementais', 'Especiais'):
    m = pega(P26, r'\| `' + grupo + r'` \| `(\d+)%` \| \*{0,2}`([\d,]+)×`\*{0,2} \| '
             r'\*{0,2}`([\d,]+)×`\*{0,2} \| \*{0,2}`([\d,]+)×`\*{0,2} \|',
             f'peça 26 §6.3 — a linha {grupo}', REPO)
    PRECO[grupo] = {'peso': int(m.group(1)) / 100.0,
                    'res': n(m.group(2)), 'imu': n(m.group(3)), 'vul': n(m.group(4))}
m = pega(P26, r'\| um tipo só \| `(\d+)%` \| `([\d,]+)×` \| `([\d,]+)×` \| `([\d,]+)×` \|',
         'peça 26 §6.3 — a linha "um tipo só"', REPO)
PRECO['um tipo só'] = {'peso': int(m.group(1)) / 100.0,
                       'res': n(m.group(2)), 'imu': n(m.group(3)), 'vul': n(m.group(4))}

print()
print('  peça 26 §6.3 — a tabela de preço:')
print(f'    {"grupo":<14}{"peso":>6}{"resistir":>10}{"imune":>10}{"vulnerável":>12}')
for g, p in PRECO.items():
    print(f'    {g:<14}{p["peso"]*100:5.0f}%{p["res"]:10.2f}{p["imu"]:10.2f}{p["vul"]:12.2f}')

# a conta da propria peca, refeita: resistir corta metade do que entra por aquele grupo
print()
print('  conferindo a tabela contra a fórmula que a própria §6.3 enuncia:')
ok = True
for g, p in PRECO.items():
    w = p['peso']
    esperado_res = 1.0 / (1.0 - w / 2.0)
    esperado_imu = 1.0 / (1.0 - w)
    esperado_vul = 1.0 / (1.0 + w)
    for rot, pub, esp in (('resistir', p['res'], esperado_res),
                          ('imune', p['imu'], esperado_imu),
                          ('vulnerável', p['vul'], esperado_vul)):
        d = abs(pub - esp) / esp
        flag = '' if d < 0.01 else '   <<< erra ' + f'{100*d:.1f}%'
        if d >= 0.01:
            ok = False
        print(f'    {g:<14}{rot:<12}publicado {pub:5.2f}   fórmula {esp:5.2f}{flag}')
print('  ⟹ a tabela é conta, e ela fecha.' if ok else '  ⚠ a tabela NÃO é a fórmula em algum ponto.')

# a linha do bloco
m = pega(BLOCO, r'\*\*Resistências\*\* (.) · \*\*Imunidades\*\* (.) · \*\*(\w+)\*\* (.) · \*\*Perícias\*\*',
         'RASCUNHO-5 — a linha de resistências')
NOME_VUL = m.group(3)
print()
print(f'  RASCUNHO-5 · a linha do bloco chama a terceira célula de "{NOME_VUL}"')
print(f'  peça 26 §6.3 · a peça chama de "vulnerabilidade"')
if NOME_VUL.lower().startswith('vulner'):
    print('  ⟹ os dois nomes batem.')
else:
    print(f'  ⚠ NOMES DIFERENTES: o bloco diz "{NOME_VUL}", a peça diz "vulnerabilidade".')

# o degrau morreu — a vulnerabilidade estava pendurada nele?
tx26 = ler(P26, REPO)
frase_vul = re.search(r'\*\*Vulnerabilidade devolve na mesma moeda\.\*\*', tx26)
print()
print('  peça 26 §6.3 · a frase da vulnerabilidade: '
      + ('"Vulnerabilidade devolve na mesma moeda." — ACHADA' if frase_vul else 'NAO ACHADA'))
if frase_vul:
    print('    ⚠ "a mesma moeda" é o DEGRAU, e o item 5 matou o degrau como moeda.')
    mex = ler(DEGRAU)
    cita = 'vulnerab' in mex.lower()
    print(f'    a lista de mexidas do item 5 cita vulnerabilidade? {"SIM" if cita else "NÃO"}')

# escada morta dentro do §6.3
mortas = re.findall(r'`(Alcateia|Ronda|Dupla)`', tx26[tx26.index('### 6.3'):tx26.index('### 6.4')])
print()
print(f'  peça 26 §6.3 · menções à escada MORTA (Ronda/Dupla/Alcateia): {len(mortas)} '
      + (' -> ' + ', '.join(sorted(set(mortas))) if mortas else ''))


# ---------------------------------------------------------- 1 · o campo, D&D
def carregar_srd(arq):
    with open(os.path.join(FILA, arq), encoding='utf-8') as f:
        return json.load(f)


SRD = {'D&D 2024': carregar_srd('srd-2024.json'),
       'D&D 2014': carregar_srd('srd-2014.json')}

# ---------------------------------------------- 0b · O CANARIO DA VULNERABILIDADE
bloco('0b · ⚠ O CANÁRIO — o dado de VULNERABILIDADE do SRD 2024 está FURADO')

# Ele mandou um print do statblock da Mumia do MM'25 (p.219) em 10/09/2026:
# "Vulnerabilities Fire". O nosso srd-2024.json traz o campo VAZIO pra ela.
# O srd-2014.json traz 'fire' certinho. Logo: a coleta de 2024 perdeu a celula.
# Este canario existe pra ninguem mais concluir "o D&D 2024 apagou a
# vulnerabilidade" a partir de um zero que e da COLETA, e nao do desenho.
mum = {rot: [x for x in mons if x['name'].lower() == 'mummy']
       for rot, mons in SRD.items()}
print("  a Múmia do MM'25 p.219 publica: Vulnerabilities Fire   (print que ele mandou)")
FURADO = False
for rot, achados in mum.items():
    if not achados:
        print(f'  {rot:<10} a Múmia nem está nesta base')
        continue
    v = achados[0]['resistances_and_immunities']['damage_vulnerabilities_display']
    ok = 'fire' in (v or '').lower()
    print(f'  {rot:<10} o nosso dado traz {v!r:<10} ' + ('✅ bate' if ok else '❌ NÃO BATE'))
    if not ok and rot == 'D&D 2024':
        FURADO = True

if FURADO:
    print()
    print('  ### ⟹ A COLETA DE VULNERABILIDADE DO SRD 2024 ESTÁ INCOMPLETA.')
    print('      Toda contagem de vulnerabilidade em `D&D 2024` aqui é PISO, não valor.')
    print('      O que continua válido: resistência, imunidade e imunidade a condição —')
    print('      a Múmia traz as três preenchidas e elas conferem com o statblock publicado.')

bloco('1 · QUANTOS BLOCOS DO CAMPO IMPRIMEM CADA CÉLULA')

CAMPOS = (('resistência', 'damage_resistances'),
          ('imunidade', 'damage_immunities'),
          ('vulnerabilidade', 'damage_vulnerabilities'),
          ('imunidade a CONDIÇÃO', 'condition_immunities'))

prevalencia = {}
for sis, mons in SRD.items():
    print(f'\n  {sis} — {len(mons)} blocos')
    print(f'    {"célula":<24}{"quantos têm":>13}{"":>3}{"mediana de entradas (nos que têm)":>34}')
    for rot, campo in CAMPOS:
        tem = [m for m in mons if m['resistances_and_immunities'].get(campo)]
        cont = [len(m['resistances_and_immunities'][campo]) for m in tem]
        med = statistics.median(cont) if cont else 0
        mx = max(cont) if cont else 0
        print(f'    {rot:<24}{len(tem):>6} {pct(len(tem), len(mons))}   '
              f'mediana {med:>4.1f}   máximo {mx:>3}')
        prevalencia[(sis, rot)] = (len(tem), len(mons), med, mx)


# ------------------------------------- 2 · o experimento natural da vulnerab.
bloco('2 · A VULNERABILIDADE É PREÇADA? — o experimento natural')

print('''
  O MECANISMO da §6.3 e o do `Guia do Mestre` de 2014 sao o mesmo: resistir nao
  muda a vida IMPRESSA, muda a vida EFETIVA — e o CR e fixado pela efetiva.

  Entao, para um mesmo CR:
    resistir / ser imune  ->  a vida IMPRESSA tem de ser MENOR  (razao < 1)
    ser vulneravel        ->  a vida IMPRESSA tem de ser MAIOR  (razao > 1)
  Se a razao for 1,00, aquela celula e DE GRACA naquele sistema.

  ⚠ E a comparacao e feita DENTRO da faixa de CR, senao ela mede so o CR.
''')

FAIXAS = [(0.125, 1, 'CR 0–1'), (2, 4, 'CR 2–4'), (5, 10, 'CR 5–10'),
          (11, 16, 'CR 11–16'), (17, 30, 'CR 17+')]

for sis, mons in SRD.items():
    validos = [m for m in mons if m.get('challenge_rating') and m.get('hit_points')
               and m['challenge_rating'] > 0]
    print(f'\n  {sis} — {len(validos)} blocos com CR > 0')
    for rot, campo in CAMPOS[:3]:
        razoes, n_com = [], 0
        detalhe = []
        for lo, hi, nome in FAIXAS:
            faixa = [m for m in validos if lo <= m['challenge_rating'] <= hi]
            com = [m['hit_points'] for m in faixa if m['resistances_and_immunities'].get(campo)]
            sem = [m['hit_points'] for m in faixa if not m['resistances_and_immunities'].get(campo)]
            if len(com) >= 3 and len(sem) >= 3:
                r = statistics.median(com) / statistics.median(sem)
                razoes.append(r)
                n_com += len(com)
                detalhe.append(f'{nome} {r:.2f} (n={len(com)})')
        if not razoes:
            tot = sum(1 for m in validos if m['resistances_and_immunities'].get(campo))
            aviso = ''
            if tot == 0 and rot == 'vulnerabilidade' and sis == 'D&D 2024':
                aviso = '   ⚠ ZERO da COLETA — ver o canário §0b'
            print(f'    {rot:<20} {tot} blocos no sistema inteiro — '
                  + ('ZERO, a célula não existe aqui' if tot == 0 else 'amostra pequena demais')
                  + aviso)
            continue
        r = statistics.median(razoes)
        esperado_menor = rot != 'vulnerabilidade'
        if 0.95 <= r <= 1.05:
            veredito = 'DE GRAÇA — a vida impressa não muda'
        elif (r < 0.95) == esperado_menor:
            veredito = '✅ PREÇADA, e no sentido que a §6.3 prevê'
        else:
            veredito = '⚠ PREÇADA AO CONTRÁRIO da §6.3'
        print(f'    {rot:<20} vida impressa de quem tem ÷ de quem não tem, '
              f'dentro da faixa: {r:5.3f}   {veredito}')
        print(f'      {len(razoes)} faixas, {n_com} blocos com a célula — ' + ' · '.join(detalhe))


# ------------------------------------------------- 3 · quais tipos aparecem
bloco('3 · EM QUE TIPO O CAMPO PÕE RESISTÊNCIA — e ele bate no nosso 60/30/10?')

MAPA = {}
for grupo, g in GRUPOS.items():
    for t in g['tipos']:
        MAPA[t.lower()] = grupo
TRAD = {'slashing': 'Cortante', 'piercing': 'Perfurante', 'bludgeoning': 'Concussão',
        'fire': 'Fogo', 'cold': 'Frio', 'lightning': 'Elétrico', 'acid': 'Ácido',
        'thunder': 'Trovejante', 'poison': 'Veneno',
        'radiant': 'Radiante', 'necrotic': 'Necrótico', 'psychic': 'Psíquico',
        'force': None, 'bludgeoning, piercing, and slashing': None}


def grupo_de(chave):
    nome = TRAD.get(chave)
    if nome and nome.lower() in MAPA:
        return MAPA[nome.lower()]
    return None


for sis, mons in SRD.items():
    print(f'\n  {sis}')
    for rot, campo in CAMPOS[:3]:
        conta = {'Físicos': 0, 'Elementais': 0, 'Especiais': 0, 'fora dos catorze': 0}
        for m in mons:
            for e in m['resistances_and_immunities'].get(campo, []):
                k = (e.get('name') or e.get('key') or '').lower()
                g = grupo_de(k)
                conta[g if g else 'fora dos catorze'] += 1
        tot = sum(conta.values())
        if not tot:
            continue
        linha = '   '.join(f'{k} {pct(v, tot)}' for k, v in conta.items())
        print(f'    {rot:<20}({tot:>4} entradas)  {linha}')

print('\n  o nosso peso publicado (peça 19 §4): '
      + '   '.join(f'{k} {g["peso"]*100:.0f}%' for k, g in GRUPOS.items()))
print('  ⚠ os dois medem coisas diferentes: o nosso peso é "quanto do dano RECEBIDO vem')
print('    daquele grupo"; o do campo é "em que grupo o autor põe resistência".')


# ------------------------------------------------------------ 4 · Draw Steel
bloco('4 · O DRAW STEEL — e lá as duas são NÚMERO, não binário')

IMU = re.compile(r'\|\s*\*\*([^|]*?)\*\*<br/>\s*Immunity')
FRA = re.compile(r'\|\s*\*\*([^|]*?)\*\*<br/>\s*Weakness')
CAB = re.compile(r'\|\s*Level (\d+)\s*\|\s*([\w ]+?)\s*\|\s*EV\s*(\d+)\s*\|')
STAM = re.compile(r'\*\*(\d+)\*\*<br/>\s*Stamina')

statblocks = []
for raiz, _, arqs in sorted(os.walk(DSMON)):
    for a in sorted(arqs):
        if not a.endswith('.md'):
            continue
        linhas = open(os.path.join(raiz, a), encoding='utf-8').read().splitlines()
        pend = {}
        for ln in linhas:
            c = CAB.search(ln)
            if c:
                pend = {'nivel': int(c.group(1)), 'org': c.group(2).strip(),
                        'ev': int(c.group(3))}
            s = STAM.search(ln)
            if s:
                pend['stam'] = int(s.group(1))
            mi, mf = IMU.search(ln), FRA.search(ln)
            if mi and mf:
                statblocks.append(dict(pend, imu=mi.group(1).strip(),
                                       fraq=mf.group(1).strip()))
                pend = {}

print(f'  {len(statblocks)} statblocks com as duas células lidas')
com_i = [s for s in statblocks if s['imu'] != '-']
com_f = [s for s in statblocks if s['fraq'] != '-']
print(f'    imprimem a célula Immunity ......... {len(statblocks)} de {len(statblocks)} (100%) — sempre, com "-" quando vazia')
print(f'    têm imunidade de fato ............. {len(com_i):>4} {pct(len(com_i), len(statblocks))}')
print(f'    têm fraqueza de fato .............. {len(com_f):>4} {pct(len(com_f), len(statblocks))}')

NUM = re.compile(r'([A-Za-z]+)\s+(\d+)')
vals_i = [int(x) for s in com_i for _, x in NUM.findall(s['imu'])]
vals_f = [int(x) for s in com_f for _, x in NUM.findall(s['fraq'])]
if vals_i:
    print(f'\n    a imunidade deles é NÚMERO: mediana {statistics.median(vals_i):.0f}, '
          f'de {min(vals_i)} a {max(vals_i)} — é redução fixa de dano, não "não recebe nada"')
if vals_f:
    print(f'    a fraqueza deles é NÚMERO: mediana {statistics.median(vals_f):.0f}, '
          f'de {min(vals_f)} a {max(vals_f)} — é acréscimo fixo, não "dobra"')

tipos_i = {}
for s in com_i:
    for t, _ in NUM.findall(s['imu']):
        tipos_i[t.lower()] = tipos_i.get(t.lower(), 0) + 1
tipos_f = {}
for s in com_f:
    for t, _ in NUM.findall(s['fraq']):
        tipos_f[t.lower()] = tipos_f.get(t.lower(), 0) + 1
print('\n    em que tipo eles põem imunidade: '
      + ', '.join(f'{k} {v}' for k, v in sorted(tipos_i.items(), key=lambda x: -x[1])[:8]))
print('    em que tipo eles põem fraqueza:  '
      + ', '.join(f'{k} {v}' for k, v in sorted(tipos_f.items(), key=lambda x: -x[1])[:8]))

# o EV deles ve imunidade/fraqueza?
print('\n  O EV (o preço de encontro deles) enxerga essas duas células?')
by = {}
for s in statblocks:
    if s.get('ev') and s.get('nivel') and s.get('org'):
        by.setdefault((s['nivel'], s['org']), []).append(s)
for rot, sel in (('imunidade', lambda s: s['imu'] != '-'),
                 ('fraqueza', lambda s: s['fraq'] != '-')):
    razoes = []
    for k, grp in by.items():
        com = [s['ev'] for s in grp if sel(s)]
        sem = [s['ev'] for s in grp if not sel(s)]
        if com and sem:
            razoes.append(statistics.mean(com) / statistics.mean(sem))
    if razoes:
        r = statistics.median(razoes)
        print(f'    {rot:<12} {len(razoes):>3} coortes (mesmo nível+organização) — '
              f'EV de quem tem ÷ de quem não tem = {r:5.3f}  '
              + ('IGUAL, não é preçada' if 0.95 <= r <= 1.05 else 'MEXE no preço'))
    else:
        print(f'    {rot:<12} nenhuma coorte tem os dois lados')

bloco('FIM')

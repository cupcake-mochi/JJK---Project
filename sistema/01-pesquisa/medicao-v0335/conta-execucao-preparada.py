# -*- coding: utf-8 -*-
"""O preco da Execucao Preparada (Vanguarda, nivel 7), pela regua do degrau da peca 06.

Pedido do PLANO da migracao (sexta passada, D42): "meca a parcela dela pela mesma regua e confira se o
degrau continua abaixo do Guia, do Emanador e do Evocador (2,36)". A Execucao Preparada entrou no lugar da
Nao Pega, que valia 1,18 fatia; o ataque extra (0,92) nao muda.

A REGUA, lida da peca 06 (o degrau do nivel 7): tudo vira dano equivalente por rodada no nivel 30 e e
dividido pela fatia. A Nao Pega reproduz assim: 12,00 evitados x 50% das rodadas / 5,08 = 1,18.

A ENTREGA, lida da candidata (VANGUARDA.md): "Uma vez por Sequencia, ao Concluir depois de duas ou mais
Conducoes acertadas, imponha -1 a um TR adicional da Conclusao." Num d20, -1 no TR do alvo e um ponto a
mais de falha: 5 pontos percentuais. O valor de uma falha e o da condicao que a Conclusao aplica, por uma
rodada, na tabela das treze da peca 19.

O CONTRATO dos scripts de conta: a regressao reproduz o publicado antes de medir, e todo numero com dono e
lido do dono. O que e CONVENCAO NOVA (quantas Sequencias chegam a Conclusao, que Conclusao, quantas rodadas
a Vanguarda passa atacando) entra com um valor BAIXO e um ALTO, e a resposta sai em faixa.
"""
import re, sys, os
R = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))) + os.sep
def ler(c): return open(R + c, encoding='utf-8').read()
def n(s): return float(s.replace(',', '.'))
def pega(txt, rx, nome):
    m = re.search(rx, txt, re.M)
    if not m: print('ANCORA PERDIDA:', nome); sys.exit(1)
    return m
p05 = ler('sistema/03-mecanica/05-caminho-e-combate-sem-feitico.md')
p06 = ler('sistema/03-mecanica/06-caminhos-e-trilhas.md')
p19 = ler('sistema/03-mecanica/19-dano-e-condicoes.md')
dtr = ler('DESENHO-trilhas.md')
cand = ler('sistema/05-material/livro/planejamento-editorial/caminhos/vanguarda/lote-01/VANGUARDA.md')

# --- os donos -------------------------------------------------------------------------------------
FATIA = n(pega(p05, r'A fatia é `(\d+,\d+)` de dano por rodada', 'a fatia, peca 5 §4').group(1))
m = pega(dtr, r'Com o acerto em `(\d+)%`, dois ataques dão `(\d+,\d+)%`; e a falha de TR virou `(\d+)%`', 'acerto e falha de TR')
ACERTO, FALHA_TR = int(m.group(1)) / 100, int(m.group(3)) / 100
m = pega(p06, r'`(\d+)` lutas × `(\d+,\d+)` rodadas = `(\d+,\d+)` rodadas de luta por dia', 'o dia de luta, peca 06')
RODADAS_LUTA = n(m.group(2))
m = pega(p06, r'Bastião conjura `(\d+)%` das rodadas no nível 30, Vanguarda `(\d+)%`', 'a taxa de conjuracao, peca 06')
VANG_CONJURA = int(m.group(2)) / 100
m = pega(p06, r'\| \*\*Vanguarda\*\* \| ataque extra \+ `Não Pega` \| `(\d+,\d+)` \| `(\d+,\d+)` \| \*\*`(\d+,\d+)`\*\* \|', 'a linha da Vanguarda, peca 06')
EXTRA, NAO_PEGA, TOTAL_VELHO = n(m.group(1)), n(m.group(2)), n(m.group(3))
GRANDE = n(pega(p06, r'\| Guia · Emanador · Evocador \| o degrau grande \| — \| — \| `(\d+,\d+)` \|', 'o degrau grande').group(1))
m = pega(p06, r'Um efeito de TR-para-metade custa `(\d+,\d+)` esperados; ela derruba para `(\d+,\d+)`, evitando `(\d+,\d+)`', 'a Nao Pega')
EVITA = n(m.group(3))
TAXA_NP = int(pega(p06, r'Taxa declarada: `(\d+)%`', 'a taxa da Nao Pega').group(1)) / 100
COND = {c: n(v) for c, v in re.findall(r'^\| \*\*`([^`]+)`\*\* \| `(\d+,\d+)` \|', p19, re.M)}
# o que a candidata diz da entrega e das Conclusoes com TR
pega(cand, r'Uma vez por Sequência, ao Concluir depois de \*\*duas ou mais Conduções acertadas\*\*, imponha \*\*−1 a um TR adicional', 'a Execucao Preparada na candidata')
CONCL = {  # Conclusao -> condicao aplicada na falha, lidas do texto da candidata
    'Rasteira': ('Derrubado', r'\*\*Rasteira\.\*\*[^\n]*\*\*Derrubado\*\*'),
    'Desarme': ('Desarmado', r'\*\*Desarme\.\*\*[^\n]*sai da empunhadura'),
    'Quebrar o Ritmo': ('Lento', r'\*\*Quebrar o Ritmo\.\*\*[^\n]*\*\*Lento'),
    'Fixar o Alvo': ('Impedido', r'\*\*Fixar o Alvo\.\*\*[^\n]*\*\*Impedido'),
}
for k, (c, rx) in CONCL.items(): pega(cand, rx, f'a Conclusao {k} na candidata')
m = pega(cand, r'\*\*Nível 23: Persistência\.\*\*', 'a Persistencia na candidata')

falhas = []
def confere(nome, obtido, esperado):
    ok = obtido == esperado
    print(f'  [{"x" if ok else "!"}] {nome}: {obtido}' + ('' if ok else f'  (esperado {esperado})'))
    if not ok: falhas.append(nome)
print('REGRESSAO — o que ja esta publicado')
confere('a fatia', FATIA, 5.08)
confere('acerto e falha de TR', (ACERTO, FALHA_TR), (0.55, 0.35))
confere('a Nao Pega: 12,00 evitados x 50% / 5,08', round(EVITA * TAXA_NP / FATIA, 2), NAO_PEGA)
confere('a linha da Vanguarda fecha', round(EXTRA + NAO_PEGA, 2), TOTAL_VELHO)
confere('as quatro condicoes, peca 19', tuple(COND[c] for c in ('Derrubado', 'Desarmado', 'Lento', 'Impedido')), (8.45, 3.45, 40.37, 135.65))
if falhas: print('\n>>> A REGRESSAO FALHOU — nada abaixo vale.'); sys.exit(1)
print('>>> TUDO OK.\n')

# --- a entrega ------------------------------------------------------------------------------------
DELTA = 0.05                       # -1 num d20: um ponto de falha a mais, sem bater no 1 ou no 20 (falha 35%)
assert 0.05 < FALHA_TR + DELTA < 0.95
# Uma Sequencia que chega a Conclusao qualificada: Golpe Inicial e Conducao no 1o turno (ataque extra),
# a 2a Conducao no 2o, a Conclusao no 3o. Uma por luta, no maximo: tres turnos de uma luta de 3,5.
# BAIXO: sem Persistencia, e so nas rodadas em que a Vanguarda ataca em vez de conjurar.
# ALTO, um teto generoso: as duas Conducoes acertam sempre e a Vanguarda ataca em toda rodada. Nem a
# Persistencia chega nisso: ela mantem a Sequencia, mas a Conducao salva nao conta como acertada.
def por_rodada(p_chega, cond):
    return p_chega * ACERTO * DELTA * COND[cond] / RODADAS_LUTA
CONV = {
    'baixo': ACERTO ** 3 * (1 - VANG_CONJURA),
    'alto':  ACERTO * 1.0 * 1.0,
}
print('A EXECUCAO PREPARADA, em fatias (BAIXO a ALTO de frequencia), por Conclusao:')
res = {}
for k, (c, _) in CONCL.items():
    lo = por_rodada(CONV['baixo'], c) / FATIA
    hi = por_rodada(CONV['alto'], c) / FATIA
    res[k] = (lo, hi)
    print(f'  {k:<16} ({c:<9}, {COND[c]:6.2f}): {lo:.3f} a {hi:.3f}')
teto = max(h for _, h in res.values())
print(f'\nO teto, com a Conclusao mais cara e a frequencia mais alta: {teto:.2f} fatia.')
print(f'A linha da Vanguarda: ataque extra {EXTRA:.2f} + Execucao Preparada ate {teto:.2f} = ate {EXTRA + teto:.2f},'
      f' contra {TOTAL_VELHO:.2f} com a Nao Pega e {GRANDE:.2f} do degrau grande.')
print(f'A diferenca contra o degrau grande fica entre {EXTRA + teto - GRANDE:+.2f} e {EXTRA - GRANDE:+.2f}'
      f' (era {TOTAL_VELHO - GRANDE:+.2f}).')

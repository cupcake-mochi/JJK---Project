# -*- coding: utf-8 -*-
"""MEDIDA — o pacote de `tipo` cabe DENTRO do bloco?

Duas contas, e as duas leem a ancora do dono:
  A) os NUCLEOS do `corpo amaldicoado` como multiplicador de vida — quanto custa na escada?
  B) o pacote de `tipo` impresso como TRACO — quanto ele come da linha de entradas nomeadas?

Nenhum numero digitado aqui. Sai com erro se o dono mudar.
"""
import re, sys, os
BEST = "/media/mizuki/HD Externo II/Claude/Claude 2/bestiario"
R5   = BEST + "/03-bloco/RASCUNHO-5-o-bloco-em-branco.md"
PESQ = BEST + "/04-fase-1/fila/PESQUISA-pendente-o-pacote-de-tipo.md"

def ler(p):
    if not os.path.exists(p): sys.exit("DONO SUMIU: %s" % p)
    return open(p, encoding='utf-8').read()
def exige(c, m):
    if not c: sys.exit("ANCORA PERDIDA: " + m)

t = ler(R5)

# --- ancora 1: a escada de vida do Passo 1 --------------------------------------
escada = []
for lin in t.splitlines():
    m = re.match(r'\|\s*\*{0,2}`(\w+)`\*{0,2}\s*\|[^|]*\|\s*\*{0,2}`?([\d,]+|dano do grupo ÷ 4)`?\*{0,2}\s*\|', lin)
    if m and m.group(1) in ('Capanga','Ameaça','Desastre','Catástrofe','Calamidade'):
        v = m.group(2)
        escada.append((m.group(1), None if '÷' in v else float(v.replace(',', '.'))))
exige(len(escada) == 5, "a escada de 5 categorias do Passo 1 do RASCUNHO-5 mudou de forma (achei %d)" % len(escada))

# --- ancora 2: a linha de entradas nomeadas -------------------------------------
m = re.search(r'\|\s*bloco normal\s*\|\s*\*{0,2}`(\d+)`\*{0,2}\s*entradas\s*\|', t)
exige(m, "a linha de entradas nomeadas do bloco normal sumiu do RASCUNHO-5")
TETO_NORMAL = int(m.group(1))
m = re.search(r'\|\s*chefe de fim de arco\s*\|\s*\*{0,2}`(\d+)`\*{0,2}\s*\|', t)
exige(m, "a linha de entradas nomeadas do chefe sumiu do RASCUNHO-5")
TETO_CHEFE = int(m.group(1))

# --- ancora 3: quantas linhas cada tipo tem, lidas da tabela final da PESQUISA ---
tp = ler(PESQ)
bloco = tp[tp.index('| tipo | linhas que o repositório tinha |'):]
tipos = {}
for lin in bloco.splitlines():
    m = re.match(r'\|\s*[`*]*([`\w çãéóúâê]+?)[`*]*\s*\|\s*[`*]*(\d+)[`*]*\s*\|\s*[^|]*?[`*]{2}([\d]+)[`*]{2}', lin)
    if m:
        nome = m.group(1).replace('`','').strip()
        tipos[nome] = (int(m.group(2)), int(m.group(3)))
exige(len(tipos) >= 6, "a tabela do saldo da PESQUISA mudou de forma (achei %d tipos)" % len(tipos))

print("=" * 78)
print("ANCORAS LIDAS")
print("=" * 78)
print("  escada de vida (RASCUNHO-5 Passo 1): " +
      " · ".join("%s %s" % (n, '—' if v is None else ('%.2f' % v)) for n, v in escada))
print("  entradas nomeadas: bloco normal %d · chefe %d" % (TETO_NORMAL, TETO_CHEFE))
print("  pacote de tipo (PESQUISA, tabela do saldo):")
for k, (a, b) in tipos.items():
    print("     %-20s repositório %d + obra %d = %d linhas" % (k, a, b, a + b))

# ================================================================= conta A
print()
print("=" * 78)
print("CONTA A — os NUCLEOS como MULTIPLICADOR de vida")
print("=" * 78)
viv = [(n, v) for n, v in escada if v]
base = dict(viv)
print("  Se 'destruir os nucleos' quer dizer N vidas cheias, a vida efetiva e' N x.")
print("  E a escada da categoria e' a unica moeda que o §6.3 aceita pra vida efetiva.")
print()
print("  %-13s %-8s %s" % ('partindo de', 'fator', 'com N nucleos o fator efetivo fica'))
for n, v in viv:
    linha = "  %-13s %-8.2f " % (n, v)
    for N in (2, 3):
        ef = v * N
        topo = max(x for _, x in viv)
        cabe = "cabe na escada" if ef <= topo else "FORA DA ESCADA"
        linha += " | N=%d -> %.2f (%s)" % (N, ef, cabe)
    print(linha)
topo = max(x for _, x in viv)
print()
print("  O TOPO da escada e' %.2f (a `Calamidade`)." % topo)
print("  ⟹ Um `Desastre` (%.2f) com 2 nucleos ja' vale %.2f = a `Calamidade`," %
      (base['Desastre'], base['Desastre'] * 2))
print("    e com 3 nucleos vale %.2f — a escada NAO TEM o que vender." % (base['Desastre'] * 3))
print("  ⟹ E' o mesmo beco da imunidade a `Fisicos` (2,50x) que o §6.3 ja' declara sem saida.")
print()
print("  A forma que custa 1,00x: os nucleos PARTEM a vida que ele ja' tem,")
print("  em vez de multiplicar. Vida total identica, e o que muda e' o CAMINHO ate' o zero.")

# ================================================================= conta B
print()
print("=" * 78)
print("CONTA B — o pacote de `tipo` impresso como TRACO NOMEADO")
print("=" * 78)
print("  %-20s %-8s %-14s %s" % ('tipo', 'linhas', 'do teto normal', 'do teto de chefe'))
piores = []
for k, (a, b) in sorted(tipos.items(), key=lambda x: -(x[1][0] + x[1][1])):
    tot = a + b
    pn, pc = 100.0 * tot / TETO_NORMAL, 100.0 * tot / TETO_CHEFE
    piores.append((k, tot, pn))
    print("  %-20s %-8d %5.1f%%          %5.1f%%" % (k, tot, pn, pc))
mx = max(piores, key=lambda x: x[1])
mn = min(piores, key=lambda x: x[1])
print()
print("  ⟹ O pacote come de %.1f%% a %.1f%% da linha de entradas nomeadas do bloco normal." %
      (mn[2], mx[2]))
print("    E o texto e' IDENTICO em todo bloco do mesmo tipo — o `Reação 1 por rodada`")
print("    e a `Iniciativa` duplicada sairam do bloco por esse mesmo motivo.")

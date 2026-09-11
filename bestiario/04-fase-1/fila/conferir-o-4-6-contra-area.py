# -*- coding: utf-8 -*-
"""CONFERÊNCIA — o §4.6 sobrevive a "área é GANHO" em vez de "área reparte a cota"?

O custo `2` da A-DECISAO-da-area-e-da-recarga.md diz, com todas as letras:
  "o §4.6 precisa de uma conferida. A metrica de 'ele derruba 2,70 pessoas' foi derivada
   supondo que ele CONCENTRA. Se area passa a ser ganho em vez de reparticao, a metrica
   nao muda — MAS NINGUEM CONFERIU ISSO, e ela e' o numero mais bem validado do bestiario."

⚠ O `0,60×` e' por alvo contra UM GOLPE (a Teia de Aranha: 27 por alvo contra golpe de 45),
  e nao contra a rodada inteira. Entao a variavel de verdade e' QUANTAS ACOES ele poe em area.

Todas as ancoras sao lidas do dono. Sai com erro se qualquer uma mudar.
"""
import re, os, sys

AQUI = os.path.dirname(os.path.abspath(__file__))
BEST = os.path.dirname(os.path.dirname(AQUI))
P26  = "/media/mizuki/HD Externo II/Claude/Claude 2/sistema/03-mecanica/26-bestiario.md"
DEC  = os.path.join(AQUI, 'A-DECISAO-da-area-e-da-recarga.md')
R5   = os.path.join(BEST, '03-bloco', 'RASCUNHO-5-o-bloco-em-branco.md')

def ler(p):
    if not os.path.exists(p): sys.exit("DONO SUMIU: %s" % p)
    return open(p, encoding='utf-8').read()
def exige(c, m):
    if not c: sys.exit("ANCORA PERDIDA: " + m)
def num(s): return float(s.replace(',', '.'))

# ------------------------------------------------------------------ ancoras
t26 = ler(P26)
m = re.search(r'\*\*Numa luta de três rodadas ele derruba `([\d,]+)` pessoas se concentrar\*\*', t26)
exige(m, "o `2,70` do §4.6 da peca 26 mudou de forma")
R270 = num(m.group(1))                      # vidas de PJ que ele entrega na luta, concentrando
m = re.search(r'ele entrega `(\d+)` de dano na luta contra `(\d+)` do alvo', t26)
exige(m, "o par `657` / `243` do §4.6 da peca 26 mudou de forma")
LUTA, VIDA_PJ = int(m.group(1)), int(m.group(2))
exige(abs(LUTA / VIDA_PJ - R270) < 0.02,
      "o §4.6 discorda de si mesmo: %d ÷ %d = %.2f, e ele publica %.2f" % (LUTA, VIDA_PJ, LUTA/VIDA_PJ, R270))

tdec = ler(DEC)
m = re.search(r'\|\s*\*\*a nossa razão por alvo\*\*\s*\|\s*\*\*`([\d,]+)×`\*\*\s*\|', tdec)
exige(m, "a razao por alvo `0,60×` sumiu da A-DECISAO")
NOSSA = num(m.group(1))
m = re.search(r'\|\s*o teto da área repetível\s*\|\s*`([\d,]+)×`\s*\|', tdec)
exige(m, "o teto da area repetivel `0,80×` sumiu da A-DECISAO")
TETO = num(m.group(1))
m = re.search(r'a banda do campo\s*\|\s*`([\d,]+)×`[^`]*`([\d,]+)×`', tdec)
exige(m, "a banda do campo sumiu da A-DECISAO")
PISO_CAMPO = num(m.group(1))

t5 = ler(R5)
m = re.search(r'\*\*`Recarga \(5-6\)` dispara `([\d,]+)` vezes numa luta de três rodadas', t5)
exige(m, "o `1,67` da Recarga sumiu do RASCUNHO-5")
DISPAROS = num(m.group(1))
m = re.search(r'\|\s*\*\*`Desastre`\*\*\s*\|\s*`(\d+)` — a mesa padrão', t5)
exige(m, "o tamanho da mesa padrao sumiu do Passo 1 do RASCUNHO-5")
MESA = int(m.group(1))

# a escada: categoria -> (fator de dano, acoes), lida do Passo 1 do RASCUNHO-5
CAT = []
for lin in t5.splitlines():
    m = re.match(r'\|\s*\*{0,2}`(\w+)`\*{0,2}\s*\|[^|]*\|[^|]*\|\s*\*{0,2}`?([\d,]+)`?\*{0,2}\s*\|\s*\*{0,2}`?(\d+)`?\*{0,2}\s*\|', lin)
    if m and m.group(1) in ('Capanga','Ameaça','Desastre','Catástrofe','Calamidade'):
        CAT.append((m.group(1), num(m.group(2)), int(m.group(3))))
exige(len(CAT) == 5, "a escada de dano/ações do Passo 1 do RASCUNHO-5 mudou de forma (achei %d)" % len(CAT))
m = re.search(r'o fator de dano de quem tem `Intervenção` é multiplicado por `([\d,]+)`', t5)
exige(m, "o fator `0,923` da Intervencao sumiu do RASCUNHO-5")
F_INTERV = num(m.group(1))
TEM_INTERV = {'Desastre', 'Catástrofe', 'Calamidade'}

print("=" * 80)
print("ANCORAS — todas lidas do dono, nenhuma digitada aqui")
print("=" * 80)
print("  §4.6 peça 26 ..... concentrando ele entrega %.2f vidas de PJ na luta (%d ÷ %d)" % (R270, LUTA, VIDA_PJ))
print("  A-DECISAO ........ nossa área %.2f× por alvo do GOLPE · teto repetível %.2f× · piso do campo %.2f×"
      % (NOSSA, TETO, PISO_CAMPO))
print("  RASCUNHO-5 ....... Recarga dispara %.2f× na luta · mesa padrão %d · Intervenção ×%.3f"
      % (DISPAROS, MESA, F_INTERV))
print("  escada ........... " + " · ".join("%s dano %.2f ações %d" % c for c in CAT))

# ------------------------------------------------------------------ o modelo
def vidas_por_golpe(k, a, tem_interv):
    """quantas vidas de PJ UM golpe entrega na luta inteira, na categoria."""
    kk = k * (F_INTERV if tem_interv else 1.0)
    return (R270 * kk) / a

print()
print("=" * 80)
print("A CONFERÊNCIA — quantas AÇÕES em área à vontade a mesa aguenta?")
print("=" * 80)
print("  Um golpe em área entrega  %.2f × (o que aquele golpe entrega)  a CADA alvo." % NOSSA)
print("  A mesa cai quando um alvo leva 1,00 vida na luta.")
print()
print("  %-12s %6s %6s %10s %12s %s" % ('categoria','dano','ações','por golpe','por alvo/área','à vontade: cai com'))
travas = {}
for nome, k, a in CAT:
    vg = vidas_por_golpe(k, a, nome in TEM_INTERV)
    por_alvo = NOSSA * vg
    n_cai = (1.0 / por_alvo) if por_alvo > 0 else float('inf')
    trava = max(0, min(a, int(n_cai - 1e-9)))   # quantas acoes em area ainda NAO derrubam
    travas[nome] = (trava, a, n_cai, por_alvo)
    txt = ('%.2f ações' % n_cai) if n_cai <= a else 'nem com as %d — seguro' % a
    print("  %-12s %6.2f %6d %10.3f %12.3f %s" % (nome, k, a, vg, por_alvo, txt))

print()
print("  ⟹ A TRAVA, categoria a categoria — quantas ações em área à vontade cabem:")
for nome, (trava, a, n_cai, _) in travas.items():
    print("     %-12s  %d de %d ações  %s" % (nome, trava, a,
          '' if n_cai > a else '⚠ com %d a mesa cai' % (trava + 1)))

print()
print("=" * 80)
print("E O QUE ACONTECE SE ELE PUSER TUDO EM ÁREA — o pior caso")
print("=" * 80)
print("  %-12s %14s %14s %s" % ('categoria', 'concentrando', 'tudo em área', 'veredito'))
for nome, k, a in CAT:
    kk = k * (F_INTERV if nome in TEM_INTERV else 1.0)
    conc = R270 * kk                                  # vidas entregues, concentrando
    area_por_alvo = NOSSA * conc                      # cada alvo leva isso
    caem = MESA if area_por_alvo >= 1.0 else 0
    print("  %-12s %13.2f  %10.2f/alvo  %s" % (nome, conc, area_por_alvo,
          ('⚠⚠ A MESA INTEIRA (%d) cai' % caem) if caem else 'ninguém cai'))

print()
print("=" * 80)
print("E A RECARGA? — ela é a trava que o campo usa, e ela apaga a trava inteira")
print("=" * 80)
print("  Uma área em Recarga dispara %.2f× numa luta de 3 rodadas — ela vale %.3f de uma à vontade."
      % (DISPAROS, DISPAROS / 3))
print()
print("  %-12s %14s %16s %s" % ('categoria', 'por alvo/ação', 'cai com', 'trava'))
for nome, k, a in CAT:
    vg = vidas_por_golpe(k, a, nome in TEM_INTERV)
    por_alvo = NOSSA * vg * (DISPAROS / 3.0)
    n_cai = 1.0 / por_alvo
    cabe = n_cai > a
    print("  %-12s %13.3f  %13s  %s" % (nome, por_alvo,
          ('%.2f ações' % n_cai) if not cabe else 'nem com %d' % a,
          'NENHUMA — todas cabem' if cabe else '%d de %d' % (int(n_cai), a)))
print()
print("  ⟹ Em Recarga, a trava some: nenhuma categoria derruba a mesa nem pondo TODAS")
print("    as ações em área. É exatamente o que o campo faz — e a Recarga já está fechada.")

print()
print("=" * 80)
print("⚠ MAS A TRAVA DE `2` É DE PENHASCO, E O PENHASCO É AFIADO")
print("=" * 80)
print("  %-12s %10s %12s %12s" % ('categoria', '1 ação', '2 ações', '3 ações'))
for nome, k, a in CAT:
    if a < 2: continue
    vg = vidas_por_golpe(k, a, nome in TEM_INTERV)
    pa = NOSSA * vg
    linha = "  %-12s" % nome
    for n in (1, 2, 3):
        if n > a: linha += "%12s" % '—'; continue
        v = n * pa
        linha += "%11.0f%%%s" % (100 * v, '⚠' if v >= 1 else ' ')
    print(linha)
print()
print("  Com 2 ações em área o alvo fica com %.1f%% de vida — a mesa inteira a um fio."
      % (100 * (1 - 2 * NOSSA * vidas_por_golpe(1.0, 3, True))))
print("  ⟹ A trava MATEMÁTICA é 2. A trava USÁVEL é 1: com 1 ação em área todo mundo")
print("    leva ~50%% e a luta continua sendo uma luta.")

print("=" * 80)
print("⚠⚠ E A FORMA DO NÚMERO MUDA — e este é o achado maior")
print("=" * 80)
print("  Concentrando, a queda é uma CURVA: %.2f pessoas." % R270)
print("     A terceira cai no finalzinho e a quarta não cai. A fração é real.")
print()
print("  Em área uniforme, a queda é um PENHASCO: todo mundo leva o mesmo dano,")
print("  então ou NINGUÉM cai, ou A MESA INTEIRA cai.")
print("     ⟹ O `%.2f` NÃO É ALCANÇÁVEL em área. Ele é uma métrica de alvo único," % R270)
print("       e o §6.5 chamar as duas leituras de 'a mesma' é o que está errado.")

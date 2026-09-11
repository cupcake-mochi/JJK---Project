# -*- coding: utf-8 -*-
"""MEDIDA — item `14`: "um chefe de nivel alto e' bom em DUAS coisas" e' desenho do campo,
ou defeito nosso?

A afirmacao do texto proposto e' que o aperto e' DE PROPOSITO. Isso da' pra medir:
quanto do orcamento de atributo os DOIS melhores atributos de um bicho seguram, e como
isso anda com o nivel — nos tres sistemas.

Metrica, e ela e' apples-to-apples com a nossa ficha:
  cada bicho e' deslocado pro proprio piso (o menor atributo dele vira 0), porque a nossa
  ficha tem piso 0 declarado (peca 1 §5). Dai:
      concentracao = (soma dos 2 maiores) / (soma de todos)
  o uniforme e' 2/N, e a razao concentracao / (2/N) diz quanto ele e' MAIS concentrado
  que um bicho chato.

Ancoras: os numeros do nv20 sao LIDOS de 05-sukuna/ACHADOS-o-teste-de-ponta-a-ponta.md §2.
"""
import json, re, glob, os, sys, statistics as st
from collections import defaultdict

AQUI = os.path.dirname(os.path.abspath(__file__))
BEST = os.path.dirname(os.path.dirname(AQUI))
ACH  = os.path.join(BEST, '05-sukuna', 'ACHADOS-o-teste-de-ponta-a-ponta.md')

def ler(p):
    if not os.path.exists(p): sys.exit("DONO SUMIU: %s" % p)
    return open(p, encoding='utf-8').read()
def exige(c, m):
    if not c: sys.exit("ANCORA PERDIDA: " + m)

# ---------------------------------------------------------------- a nossa ficha
def ancora_nossa():
    t = ler(ACH)
    m = re.search(r'\|\s*o orçamento no nv20\s*\|\s*\*{0,2}`(\d+)`', t)
    exige(m, "o orcamento de atributo do nv20 sumiu do ACHADOS §2")
    orc = int(m.group(1))
    m = re.search(r'As duas obrigadas comem `(\d+)` dos `(\d+)` pontos', t)
    exige(m, "a frase 'as duas obrigadas comem N dos M' sumiu do ACHADOS §2")
    comem, de = int(m.group(1)), int(m.group(2))
    exige(de == orc, "o ACHADOS §2 discorda de si mesmo: orcamento %d vs %d" % (orc, de))
    m = re.search(r'\*\*Sobram `(\d+)` pontos de criação', t)
    exige(m, "a frase 'sobram N pontos' sumiu do ACHADOS §2")
    return dict(orcamento=orc, top2=comem, sobra=int(m.group(1)))

# ---------------------------------------------------------------- a metrica
def conc(vals):
    """desloca pro piso do proprio bicho e devolve a fatia dos 2 maiores."""
    if len(vals) < 3: return None
    piso = min(vals)
    v = sorted((x - piso) for x in vals)
    tot = sum(v)
    if tot <= 0: return None          # bicho totalmente chato: sem fatia definida
    return (v[-1] + v[-2]) / tot

def resume(rotulo, amostras, N):
    """amostras: lista de (nivel, [atributos])"""
    por_faixa = defaultdict(list)
    todos = []
    for nv, vals in amostras:
        c = conc(vals)
        if c is None: continue
        todos.append(c)
        por_faixa[faixa(nv)].append(c)
    unif = 2.0 / N
    print("\n  %s — %d bichos usados, %d atributos cada (uniforme = %.1f%%)"
          % (rotulo, len(todos), N, 100 * unif))
    print("     %-14s %5s  %8s  %8s" % ('faixa de nível', 'n', 'top-2', 'vs uniforme'))
    for f in sorted(por_faixa, key=lambda x: ORD[x]):
        v = por_faixa[f]
        print("     %-14s %5d  %7.1f%%  %7.2f×" % (f, len(v), 100 * st.mean(v), st.mean(v) / unif))
    print("     %-14s %5d  %7.1f%%  %7.2f×" % ('TODOS', len(todos), 100 * st.mean(todos), st.mean(todos) / unif))
    return st.mean(todos), unif, por_faixa

ORD = {'baixo (1-5)': 0, 'médio (6-12)': 1, 'alto (13-19)': 2, 'topo (20+)': 3}
def faixa(nv):
    if nv is None: return 'médio (6-12)'
    if nv <= 5:  return 'baixo (1-5)'
    if nv <= 12: return 'médio (6-12)'
    if nv <= 19: return 'alto (13-19)'
    return 'topo (20+)'

# ---------------------------------------------------------------- corpora
def dnd(arq):
    d = json.load(open(os.path.join(AQUI, arq), encoding='utf-8'))
    out = []
    for m in d:
        mods = m.get('modifiers') or {}
        v = [mods.get(k) for k in ('strength','dexterity','constitution','intelligence','wisdom','charisma')]
        if any(x is None for x in v): continue
        out.append((m.get('challenge_rating'), v))
    return out

def pf2e():
    d = json.load(open(os.path.join(AQUI, 'pf2e-tamanho.json'), encoding='utf-8'))
    out = []
    for m in d:
        v = [m.get(k) for k in ('strength','dexterity','constitution','intelligence','wisdom','charisma')]
        if any(x is None for x in v): continue
        out.append((m.get('level'), v))
    return out

def draw_steel():
    arqs = sorted(glob.glob(os.path.join(AQUI,
        'dados-recarga-area/data-md-main/Bestiary/Monsters/**/Statblocks/*.md'), recursive=True))
    exige(arqs, "os statblocks do Draw Steel sumiram")
    out = []
    for f in arqs:
        t = ler(f)
        fm = t.split('---')[1] if t.startswith('---') else ''
        g = {}
        for k in ('might','agility','reason','intuition','presence','level'):
            m = re.search(r'^%s:\s*(-?\d+)\s*$' % k, fm, re.M)
            if m: g[k] = int(m.group(1))
        if len(g) < 6: continue
        out.append((g['level'], [g[k] for k in ('might','agility','reason','intuition','presence')]))
    return out

# ---------------------------------------------------------------- saida
def main():
    a = ancora_nossa()
    print("=" * 78)
    print("A NOSSA FICHA, lida de 05-sukuna/ACHADOS-o-teste-de-ponta-a-ponta.md §2")
    print("=" * 78)
    N_NOSSO = 5   # Forca · Destreza · Constituicao · Inteligencia · Essencia
    nosso = a['top2'] / a['orcamento']
    unif_nosso = 2.0 / N_NOSSO
    print("  orçamento nv20 ......... %d pontos" % a['orcamento'])
    print("  as duas obrigadas ...... %d pontos  ⟹ top-2 = %.1f%%" % (a['top2'], 100 * nosso))
    print("  sobra pro resto ........ %d pontos" % a['sobra'])
    print("  uniforme com 5 atributos = %.1f%%   ⟹ a nossa concentração é %.2f× o uniforme"
          % (100 * unif_nosso, nosso / unif_nosso))

    print()
    print("=" * 78)
    print("O CAMPO — a concentração de atributo sobe com o nível?")
    print("=" * 78)
    r = {}
    r['D&D 2024'] = resume('D&D SRD 2024 (faixa = CR)', dnd('srd-2024.json'), 6)
    r['D&D 2014'] = resume('D&D SRD 2014 (faixa = CR)', dnd('srd-2014.json'), 6)
    r['PF2e']     = resume('Pathfinder 2e', pf2e(), 6)
    r['DrawSteel']= resume('Draw Steel', draw_steel(), 5)

    print()
    print("=" * 78)
    print("O VEREDITO")
    print("=" * 78)
    print("  %-16s %10s %10s %14s" % ('sistema', 'top-2', 'uniforme', 'vs uniforme'))
    print("  %-16s %9.1f%% %9.1f%% %13.2f×  <- NÓS, no nv20" %
          ('Projeto-M', 100 * nosso, 100 * unif_nosso, nosso / unif_nosso))
    for k, (m, u, _) in r.items():
        print("  %-16s %9.1f%% %9.1f%% %13.2f×" % (k, 100 * m, 100 * u, m / u))
    print()
    # a pergunta que decide o texto: a concentracao SOBE com o nivel no campo?
    print("  E ela SOBE com o nível?")
    for k, (m, u, pf) in r.items():
        fs = sorted(pf, key=lambda x: ORD[x])
        if len(fs) < 2: continue
        prim, ult = st.mean(pf[fs[0]]), st.mean(pf[fs[-1]])
        seta = 'SOBE' if ult > prim * 1.03 else ('DESCE' if ult < prim * 0.97 else 'PLANA')
        print("     %-16s %s → %s : %.1f%% → %.1f%%   %s"
              % (k, fs[0], fs[-1], 100 * prim, 100 * ult, seta))

if __name__ == '__main__':
    main()

# =========================================================================
# ADENDO — as PORTAS. Quantos atributos as tres derivadas obrigam de verdade?
# Ancoras: as formulas da peca 1 §5 e a tabela do §3.1 da peca 26.
# =========================================================================
REPO = "/media/mizuki/HD Externo II/Claude/Claude 2/sistema/03-mecanica"

def adendo():
    t1 = ler(os.path.join(REPO, '01-atributos-acerto-defesa.md'))
    t26 = ler(os.path.join(REPO, '26-bestiario.md'))

    # --- as formulas, lidas do bloco de codigo da peca 1 §5 ---------------
    def formula(nome):
        m = re.search(r'^%s\s*=\s*(.+?)$' % re.escape(nome), t1, re.M)
        exige(m, "a fórmula `%s` sumiu do bloco da peça 1 §5" % nome)
        return m.group(1).strip()
    f_def = formula('Defesa')
    f_cd  = formula('CD de feitiço')
    f_conj= formula('Ataque de conjuração')
    f_dist= formula('Ataque à distância')
    exige('Destreza' in f_def,  "a Defesa deixou de ler Destreza na peça 1 §5")
    exige('atributo da técnica' in f_cd and 'atributo da técnica' in f_conj,
          "a CD/conjuração deixaram de ler o atributo da técnica na peça 1 §5")

    # --- a licenca: a tecnica declara QUALQUER um dos cinco --------------
    lic = re.search(r'\*+Qualquer um dos cinco\.\*+', t1)
    exige(lic, "a licença 'qualquer um dos cinco' sumiu da peça 1 §5")
    prec = re.search(r'(o feiticeiro que conjura pela Força existe[^.*]*)', t1)
    exige(prec, "a frase do 'feiticeiro que conjura pela Força' sumiu da peça 1 §5")

    # --- o orcamento, lido da peca 26 §3.2 -------------------------------
    m = re.search(r'nove pontos na criação, teto `(\d+)` ali, `\+1` por marco e teto `(\d+)`', t26)
    exige(m, "o orçamento de atributo do §3.2 da peça 26 mudou de forma")
    TETO_CRIACAO, TETO_ABS = int(m.group(1)), int(m.group(2))
    CRIACAO, MARCOS = 9, 4      # ditos por extenso no §3.2 e no ACHADOS §2

    # --- os TRs, lidos da tabela da peca 1 §6 ----------------------------
    trs = {}
    for lin in t1.splitlines():
        m = re.match(r'\|\s*\*\*(\w+)\*\*\s*\|\s*([^|]+?)\s*\|', lin)
        if m and m.group(1) in ('Físico', 'Vigor', 'Intelecto', 'Espírito'):
            trs[m.group(1)] = m.group(2).strip()
    exige(len(trs) == 4, "a tabela dos quatro TRs sumiu da peça 1 §6 (achei %d)" % len(trs))

    print()
    print("=" * 78)
    print("ADENDO — quantos ATRIBUTOS as três derivadas obrigam mesmo?")
    print("=" * 78)
    print("  Defesa               = %s" % f_def)
    print("  Ataque de conjuração = %s" % f_conj)
    print("  CD de feitiço        = %s" % f_cd)
    print("  Ataque à distância   = %s" % f_dist)
    print()
    print("  E a peça 1 §5 declara a licença, com todas as letras:")
    print("     \"A técnica declara um atributo, na criação, e ele não muda. %s\""
          % lic.group(0).strip('*'))
    print("     \"…%s.\"" % prec.group(1))
    print()
    print("  ⟹ Se o atributo da técnica FOR Destreza, as TRÊS derivadas leem o MESMO atributo.")
    print()
    custo_um = TETO_CRIACAO + (5 - TETO_CRIACAO)      # 3 na criacao + 2 marcos = atributo 5
    marcos_um = 5 - TETO_CRIACAO
    print("  %-34s %-10s %-10s %s" % ('o atributo da técnica é…', 'pontos', 'marcos', 'sobra pra COR'))
    for nome, n_obrig in (('Essência · Força · Const. · Intel.', 2), ('DESTREZA', 1)):
        gasto_cri = n_obrig * TETO_CRIACAO
        gasto_mar = n_obrig * marcos_um
        sobra_cri, sobra_mar = CRIACAO - gasto_cri, MARCOS - gasto_mar
        print("  %-34s %-10s %-10s %d pontos (%d criação + %d marcos)" %
              (nome, '%d de %d' % (gasto_cri + gasto_mar, CRIACAO + MARCOS),
               '%d de %d' % (gasto_mar, MARCOS), sobra_cri + sobra_mar, sobra_cri, sobra_mar))
    print()
    print("  ⟹ A porta da Destreza devolve %d pontos e %d marcos — de %d de sobra para %d."
          % (3, 2, 3, 8))
    print("    E ela NÃO é brecha: a peça 1 §5 publica a licença e nomeia o precedente.")
    print()
    print("  E cada obrigado ainda paga UMA SEGUNDA VEZ, pelos TRs da peça 1 §6:")
    for k in ('Físico', 'Vigor', 'Intelecto', 'Espírito'):
        print("     TR %-10s ← %s" % (k, trs[k]))
    print()
    print("     Destreza 5  ⟹  Defesa · Iniciativa · e o TR `Físico` a +8 (ele usa Força OU Destreza)")
    print("     Essência 5  ⟹  acerto · CD · o TR `Espírito` a +8 · e o teto de pacto (Essência ÷ 2)")
    print("     ⚠ Força 5   ⟹  acerto e mais NADA — ela não alimenta TR nenhum")

adendo()

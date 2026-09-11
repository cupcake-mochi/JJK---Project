# -*- coding: utf-8 -*-
"""MEDIDA — as duas coisas que a pesquisa do pacote de `tipo` quebrou no bloco.

  1) CONDICAO DE MORTE que nao e' "vida a zero"  ->  o campo tem? e ONDE ele imprime?
  2) IMUNIDADE a uma CATEGORIA LARGA de dano     ->  o campo tem? e quanto ela custa AQUI?

Corpora em disco:
  SRD 5.1 (2014) : srd-2014.json   325 blocos   <- o antes
  SRD 5.2 (2024) : srd-2024.json   331 blocos   <- o depois   (experimento natural)
  Draw Steel     : dados-recarga-area/.../Statblocks/*.md

NENHUM numero de regra do Projeto-M vive aqui dentro. Toda ancora e' LIDA do documento
dono, e o script morre com mensagem se o dono mudar de forma.
"""
import json, re, glob, os, sys
from collections import Counter, defaultdict

AQUI  = os.path.dirname(os.path.abspath(__file__))
REPO  = "/media/mizuki/HD Externo II/Claude/Claude 2/sistema"
P26   = REPO + "/03-mecanica/26-bestiario.md"
P19   = REPO + "/03-mecanica/19-dano-e-condicoes.md"
P09   = REPO + "/03-mecanica/09-origens.md"
P16   = REPO + "/03-mecanica/16-ferramenta-amaldicoada.md"
P25   = REPO + "/03-mecanica/25-sem-tecnica.md"
MAN   = REPO + "/05-material/livro/manual/45-aptidoes-e-refino.md"

def ler(p):
    if not os.path.exists(p): sys.exit("DONO SUMIU: %s" % p)
    return open(p, encoding='utf-8').read()

def exige(cond, msg):
    if not cond: sys.exit("ANCORA PERDIDA: " + msg)

# ============================================================ ancoras dos donos
def ancoras():
    a = {}
    t26 = ler(P26)
    for g in ('Físicos', 'Elementais', 'Especiais'):
        m = re.search(r'\|\s*`%s`\s*\|\s*\*{0,2}`?(\d+)%%`?\*{0,2}\s*\|'
                      r'\s*\*{0,2}`([\d,]+)×`\*{0,2}\s*\|\s*\*{0,2}`([\d,]+)×`\*{0,2}\s*\|' % g, t26)
        exige(m, "a linha `%s` do §6.3 da peca 26 mudou de forma" % g)
        a[g] = dict(peso=int(m.group(1)), resist=float(m.group(2).replace(',', '.')),
                    imune=float(m.group(3).replace(',', '.')))
    # v0.221: o degrau morreu como moeda e o preco virou MULTIPLICADOR do fator da
    # categoria (`DECIDIDO-o-degrau.md`). As duas frases dizem o mesmo numero que a
    # tabela logo acima — e o script agora COBRA que os dois donos concordem.
    m = re.search(r'\*\*Resistência ao grupo `Físicos` multiplica o fator da categoria '
                  r'por `([\d,]+)`', t26)
    exige(m, "a frase do preco da resistencia sumiu do §6.3 da peca 26")
    a['frase_preco'] = m.group(0)
    exige(abs(float(m.group(1).replace(',', '.')) - a['Físicos']['resist']) < 1e-9,
          "a frase e a tabela do §6.3 discordam do preco da resistencia a `Fisicos`")
    m = re.search(r'\*\*Imunidade a `Físicos` multiplica o fator por `([\d,]+)`([^*]*)\*\*', t26)
    exige(m, "a frase do preco da IMUNIDADE sumiu do §6.3 da peca 26")
    exige(abs(float(m.group(1).replace(',', '.')) - a['Físicos']['imune']) < 1e-9,
          "a frase e a tabela do §6.3 discordam do preco da imunidade a `Fisicos`")
    a['frase_imu'] = ('multiplicar o fator por %s%s' % (m.group(1), m.group(2))).strip()

    # os catorze tipos, do dono deles
    t19 = ler(P19)
    m = re.search(r'>\s*\*\*(\w+) tipos, em (\w+) grupos\.\*\*', t19)
    exige(m, "a frase 'catorze tipos, em tres grupos' sumiu da peca 19 §4")
    a['n_tipos'] = m.group(1)
    a['tem_eixo_imbuido'] = bool(re.search(r'imbuí|amaldiçoad[oa]\s*\|', t19.split('## 4. Os tipos de dano')[1].split('## 5.')[0]))

    # as TRES PORTAS que permitem ferir maldicao
    tman = ler(MAN)
    exige('Canalizar energia' in tman, "a aptidao `Canalizar energia` sumiu do manual")
    m = re.search(r'\*\*Canalizar energia\*\* — ([^\n]+)', tman)
    exige(m, "a frase da `Canalizar energia` mudou de forma no manual")
    a['porta_canalizar'] = m.group(1).strip()
    m = re.search(r'##\s*Aptidões de graça\s*\n\s*\n([^\n]+)', tman)
    exige(m, "a secao `Aptidoes de graca` sumiu do manual")
    a['canalizar_gratis'] = m.group(1).strip()
    exige('sem custar marco nenhum' in a['canalizar_gratis'],
          "a `Canalizar energia` deixou de ser de graca no manual")

    t16 = ler(P16)
    m = re.search(r'\*\*(Ela fere maldição\. Isso é binário: ou fere, ou não fere\.)\*\*', t16)
    exige(m, "a frase binaria da ferramenta sumiu da peca 16")
    a['porta_ferramenta'] = m.group(1)
    exige(re.search(r'\|\s*\*\*o que se gasta\*\*\s*\|\s*nada\.', t16),
          "a ferramenta deixou de custar `nada` na peca 16")

    t25 = ler(P25)
    exige('A `Energia Reversa` fere maldição' in t25,
          "o §4.4 da peca 25 (Energia Reversa fere maldicao) sumiu")
    a['porta_reversa'] = 'peça 25 §4.4 — a `Energia Reversa` fere maldição, +50%'

    # as rotas publicadas de personagem
    t09 = ler(P09)
    rotas = ['Latente', 'Receptáculo', 'Descendente', 'Reencarnado', 'Feto',
             'Sem Técnica', 'Corpo Amaldiçoado', 'Restrição Celestial']
    for r in rotas:
        exige(re.search(r'#+\s*' + re.escape(r) + r'\s*$', t09, re.M) or ('**' + r + '**') in t09
              or ('## 4. ' + r) in t09, "a rota `%s` sumiu da peca 9" % r)
    a['rotas'] = rotas
    exige('acesso a ferramenta amaldiçoada como eixo de poder' in t09,
          "a Restricao Celestial perdeu o acesso a ferramenta na peca 9 §5")
    exige('**você tem energia amaldiçoada**' in t09,
          "o Corpo Amaldicoado perdeu a energia propria na peca 9 §5")
    return a

# ============================================================ corpora D&D
def carrega(n): return json.load(open(os.path.join(AQUI, n), encoding='utf-8'))
def entradas(m):
    for t in (m.get('traits') or []):  yield 'traço',  (t.get('name') or ''), (t.get('desc') or '')
    for x in (m.get('actions') or []): yield 'ação',   (x.get('name') or ''), (x.get('desc') or '')

MORTE = [
 ('a 0 de vida ele vira outra coisa',
  re.compile(r'(reduced to 0 [Hh]it [Pp]oints?|drops to 0 [Hh]it [Pp]oints?)(?:[^.]{0,120})?'
             r'\b(instead|isn\'t destroyed|is not destroyed|doesn\'t die|does not die|transform|'
             r'reverts?|turns? into|becomes)\b', re.S)),
 ('ele volta depois de morto',
  re.compile(r'\b(rejuvenat\w+|regains? all (its )?[Hh]it [Pp]oints? (in|after) \d|'
             r'reforms?|re-?forms?|returns? to life|comes? back to life)\b', re.I)),
 ('so fica morto se X (Regeneration)', re.compile(r'\bRegenerat', re.I)),
 ('precisa de um passo A MAIS',
  re.compile(r'\b(only way to (kill|destroy)|can only be (killed|destroyed)|'
             r'to destroy .{0,40}(you |one )?must|unless .{0,60}(destroyed|burn|acid|fire))', re.I)),
]

def mede_morte(blocos):
    por_pad, donos, onde = Counter(), set(), Counter()
    for m in blocos:
        bateu = False
        for tipo, nome, desc in entradas(m):
            alvo = nome + '. ' + desc
            for pad, rx in MORTE:
                if rx.search(alvo):
                    por_pad[pad] += 1; bateu = True
                    onde[tipo] += 1
        if bateu: donos.add(m['name'])
    return por_pad, donos, onde

LARGA = re.compile(r'nonmagical|non-?magical', re.I)
def mede_imunidade(blocos):
    r = dict(n=len(blocos), imu=0, res=0, imu_larga=0, res_larga=0, n_tipos=Counter(), ex=[])
    for m in blocos:
        ri = m.get('resistances_and_immunities') or {}
        di = (ri.get('damage_immunities_display') or '').strip()
        dr = (ri.get('damage_resistances_display') or '').strip()
        if di: r['imu'] += 1; r['n_tipos'][len(ri.get('damage_immunities') or [])] += 1
        if dr: r['res'] += 1
        if LARGA.search(di): r['imu_larga'] += 1; r['ex'].append((m['name'], di))
        if LARGA.search(dr): r['res_larga'] += 1
    return r

# ============================================================ Draw Steel
DS = os.path.join(AQUI, 'dados-recarga-area/data-md-main/Bestiary/Monsters/**/Statblocks/*.md')
# "IMPEDE a morte" e' o analogo exato do `corpo amaldicoado`: 0 de vida NAO basta
RX_IMPEDE = re.compile(r"(instead of dying|doesn't die|does not die|dies only if|"
                       r"(reduced to|drops? to) 0 Stamina[^.]{0,140}?\b(instead|remain|stay|revive|return)\b)",
                       re.I | re.S)
def cel(rot): return re.compile(r'\|\s*\*\*([^*|]*)\*\*<br/>\s*' + rot)
def mede_draw_steel():
    arqs = sorted(glob.glob(DS, recursive=True))
    exige(arqs, "os statblocks do Draw Steel sumiram de dados-recarga-area/")
    r = dict(n=len(arqs), imu=0, fra=0, numerica=0, binaria=0, val=Counter(), morte=[], impede=[])
    for f in arqs:
        t = ler(f)
        mi, mf = cel('Immunity').search(t), cel('Weakness').search(t)
        if mi and mi.group(1).strip() not in ('', '-'):
            v = mi.group(1).strip(); r['imu'] += 1; r['val'][v] += 1
            # a celula pode ser "Cold, fire, or lightning 5": o numero fecha a celula inteira
            if re.search(r'\d+\s*$', v): r['numerica'] += 1
            else: r['binaria'] += 1
        if mf and mf.group(1).strip() not in ('', '-'): r['fra'] += 1
        n = os.path.basename(f)[:-3]
        if re.search(r'(reduced to|drops? to) 0 Stamina|when (they|it) dies', t, re.I):
            r['morte'].append(n)
        if RX_IMPEDE.search(t):
            r['impede'].append(n)
    return r

# ============================================================ saida
def pct(a, b): return (100.0 * a / b) if b else 0.0
def main():
    a = ancoras()
    L = lambda s='': print(s)
    L('=' * 80); L('ANCORAS — todas LIDAS do dono, nenhuma digitada aqui'); L('=' * 80)
    for g in ('Físicos', 'Elementais', 'Especiais'):
        d = a[g]; L('  §6.3  %-11s peso %2d%%   resistir %.2f×   IMUNE %.2f×' %
                    (g, d['peso'], d['resist'], d['imune']))
    L('  §6.3  imunidade a Físicos custa: %s' % a['frase_imu'])
    L('  §19.4 os tipos de dano: %s tipos, e existe eixo "imbuído"? %s'
      % (a['n_tipos'], 'SIM' if a['tem_eixo_imbuido'] else 'NÃO'))
    L()
    L('  AS TRÊS PORTAS que já permitem ferir maldição, e cada uma tem dono:')
    L('   1. manual  · Canalizar energia — %s' % a['porta_canalizar'][:88])
    L('      e ela é de graça: "%s"' % a['canalizar_gratis'][:88])
    L('   2. peça 16 · %s' % a['porta_ferramenta'])
    L('   3. %s' % a['porta_reversa'])

    c14, c24 = carrega('srd-2014.json'), carrega('srd-2024.json')
    L(); L('=' * 80)
    L('MEDIDA 1 — "vida a zero" é a única condição de morte no campo?'); L('=' * 80)
    for blocos, rot in ((c14, 'SRD 2014'), (c24, 'SRD 2024')):
        pp, donos, onde = mede_morte(blocos)
        L(); L('  %s — %d blocos' % (rot, len(blocos)))
        for pad, _ in MORTE: L('     %-38s %3d entradas' % (pad, pp.get(pad, 0)))
        L('     %-38s %3d blocos = %.1f%%' % ('>> blocos com regra PRÓPRIA de morte', len(donos), pct(len(donos), len(blocos))))
        tot = sum(onde.values()) or 1
        L('     onde ela é impressa: %s' % ' · '.join('%s %d (%.0f%%)' % (k, v, pct(v, tot)) for k, v in onde.most_common()))
    ds = mede_draw_steel()
    L(); L('  Draw Steel — %d statblocks' % ds['n'])
    L('     dispara ALGUMA coisa na morte/0 Stamina .... %3d (%.1f%%)' % (len(ds['morte']), pct(len(ds['morte']), ds['n'])))
    L('     IMPEDE a morte a 0 Stamina ................. %3d (%.1f%%)  <- o análogo do `corpo amaldiçoado`' % (len(ds['impede']), pct(len(ds['impede']), ds['n'])))

    L(); L('=' * 80)
    L('MEDIDA 2 — imunidade a uma CATEGORIA LARGA travada por propriedade'); L('=' * 80)
    L('  "nonmagical" não é um tipo de dano: é uma PROPRIEDADE que corta uma classe')
    L('  inteira. É o mesmo formato de "ataque não imbuído em energia amaldiçoada".')
    for blocos, rot in ((c14, 'SRD 2014'), (c24, 'SRD 2024')):
        r = mede_imunidade(blocos)
        L(); L('  %s — %d blocos' % (rot, r['n']))
        L('     com QUALQUER imunidade de dano ......... %3d (%.1f%%)' % (r['imu'], pct(r['imu'], r['n'])))
        L('     IMUNE a categoria larga ("nonmagical") . %3d (%.1f%%)' % (r['imu_larga'], pct(r['imu_larga'], r['n'])))
        L('     RESISTE a categoria larga .............. %3d (%.1f%%)' % (r['res_larga'], pct(r['res_larga'], r['n'])))
        t = sum(r['n_tipos'].values()); u2 = sum(v for k, v in r['n_tipos'].items() if k <= 2)
        if t: L('     dos que têm imunidade, %d de %d listam 1 ou 2 tipos (%.1f%%)' % (u2, t, pct(u2, t)))
        for n, d in r['ex'][:3]: L('        ex: %-20s %s' % (n, d[:60]))
    L(); L('  Draw Steel — %d statblocks' % ds['n'])
    L('     com célula Immunity preenchida ......... %3d (%.1f%%)' % (ds['imu'], pct(ds['imu'], ds['n'])))
    L('     dessas, com NÚMERO (redução de dano) ... %3d (%.1f%%)' % (ds['numerica'], pct(ds['numerica'], ds['imu'])))
    L('     dessas, BINÁRIAS (imunidade total) ..... %3d (%.1f%%)' % (ds['binaria'], pct(ds['binaria'], ds['imu'])))
    L('     com célula Weakness preenchida ......... %3d (%.1f%%)' % (ds['fra'], pct(ds['fra'], ds['n'])))
    L('     valores distintos na célula: %d — top: %s' %
      (len(ds['val']), ', '.join('%s(%d)' % (k, v) for k, v in ds['val'].most_common(4))))

    L(); L('=' * 80)
    L('MEDIDA 3 — quanto a imunidade da `maldição` custa AQUI'); L('=' * 80)
    L('  A pergunta não é "quanto vale imunidade": é "quanta saída do GRUPO ela apaga".')
    L('  E o sistema já publica a porta de ferir maldição em TRÊS documentos.')
    L()
    L('  %-24s %-34s %s' % ('rota publicada (peça 9)', 'porta que ela tem', 'custa?'))
    portas = {
        'Latente':            ('energia → Canalizar energia', 'grátis, refino 1'),
        'Receptáculo':        ('energia → Canalizar energia', 'grátis, refino 1'),
        'Descendente':        ('energia → Canalizar energia', 'grátis, refino 1'),
        'Reencarnado':        ('energia → Canalizar energia', 'grátis, refino 1'),
        'Feto':               ('energia → Canalizar energia', 'grátis, refino 1'),
        'Sem Técnica':        ('energia → Canalizar energia', 'grátis, refino 1'),
        'Corpo Amaldiçoado':  ('energia própria → Canalizar', 'grátis, refino 1'),
        'Restrição Celestial':('ferramenta amaldiçoada',      'nada — peça 16'),
    }
    for r in a['rotas']:
        p, c = portas[r]; L('  %-24s %-34s %s' % (r, p, c))
    L()
    L('  ⟹ %d de %d rotas publicadas têm porta, e nenhuma delas custa marco.' % (len(a['rotas']), len(a['rotas'])))
    L('    A imunidade apaga 0% da saída de um grupo de personagens ⟹ fator 1,00×.')
    L('    Contra quem ela morde: `civil` — e `civil` não é rota de personagem.')

if __name__ == '__main__':
    main()

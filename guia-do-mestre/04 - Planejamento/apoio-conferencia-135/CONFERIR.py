"""Confere a aplicação do registro 135 contra antes/: links e âncoras, números visíveis, células de tabela,
nomes que deviam sumir e o que continua apontando para fora do livro."""
from pathlib import Path
import json, re, sys, unicodedata, difflib
from urllib.parse import unquote
A = Path(__file__).resolve().parent; R = A.parents[1]; G = R / '06 - Redacao do Guia'; S = G / 'revisao-98'
ANTES = A / 'antes'
files = sorted(str(p.relative_to(ANTES)) for p in ANTES.rglob('*.md'))
falhas, out = [], {}

def slug(h):
    h = re.sub(r'<[^>]+>|[*_`]', '', h).strip().lower()
    h = ''.join(c for c in unicodedata.normalize('NFKD', h) if not unicodedata.combining(c))
    return re.sub(r'[\s]+', '-', re.sub(r'[^\w\s-]', '', h)).strip('-')
def ancoras(p):
    t = p.read_text(); s = {slug(h) for h in re.findall(r'^#{1,6}\s+(.+)$', t, re.M)}
    return s | set(re.findall(r'id="([^"]+)"', t))
def links(base, t):
    ruins = []
    for txt, alvo, frag in re.findall(r'\[([^\]]*)\]\(<?([^)>#]*)(#[^)>]*)?>?\)', t):
        if not alvo or alvo.startswith('http'):
            continue
        d = (base / unquote(alvo)).resolve()
        if not d.exists(): ruins.append(('arquivo', alvo)); continue
        if frag and d.suffix == '.md' and frag[1:] not in ancoras(d): ruins.append(('ancora', alvo + frag))
    return ruins
nums = lambda t: re.findall(r'\d+(?:[.,]\d+)?', re.sub(r'\]\(<?[^)]*\)|<[^>]+>', ']', t))
cells = lambda t: [c.strip() for l in t.splitlines() if l.lstrip().startswith('|') for c in l.strip().strip('|').split('|')]
alt = json.loads((A / 'alteracoes.json').read_text())
nomes_de = lambda f: [(e['antes'], e['depois']) for e in alt if e['motivo'].startswith('Nome: elenco') and e['arquivo'] == f]
titulos = [(re.match(r'\[([^\]]+)\]', e['antes']).group(1), re.match(r'\[([^\]]+)\]', e['depois']).group(1))
           for e in alt if e['antes'].startswith('[') and e['depois'].startswith('[')]
# números que a edição tira ou põe, declarados um a um
NUM_SAI = {'casos/72-sineiro-consulta-e-doma.md': ['73'], 'casos/77-ficha-preenchida-ren-e-sora.md': ['76'],
           'casos/54-transporte-e-continuidade-das-entidades.md': ['6']}
NUM_ENTRA = {f: ['1.0'] for f in ['04-na-mesa-de-jogo.md', '06-inimigos-e-perigos.md', '07-personagens-e-tecnicas.md',
             '08-entre-missoes.md', '09-pactos-e-entidades.md', '10-jogar-em-guilda.md']}
ruins_antes = ruins_depois = 0
for f in files:
    a, d = (ANTES / f).read_text(), (S / f).read_text()
    base = (S / f).parent
    ra = links(base, a); rd = links(base, d)
    ruins_antes += len(ra); ruins_depois += len(rd)
    if rd: falhas.append(f'{f}: links ruins {rd}')
    na, nd = nums(a), nums(d)
    if na != nd:
        sai, entra = [], []
        for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, na, nd, autojunk=False).get_opcodes():
            if op != 'equal': sai += na[i1:i2]; entra += nd[j1:j2]
        if sorted(sai) != sorted(NUM_SAI.get(f, [])) or sorted(entra) != sorted(NUM_ENTRA.get(f, [])):
            falhas.append(f'{f}: números mudaram: saem {sai}, entram {entra}')
    ca, cd = cells(a), cells(d)
    if len(ca) != len(cd): falhas.append(f'{f}: número de células mudou')
    else:
        for x, y in zip(ca, cd):
            if x == y: continue
            z = re.sub(r'\]\(<?[^)]*\)', ']()', x); w = re.sub(r'\]\(<?[^)]*\)', ']()', y)
            for v, n in nomes_de(f) + titulos: z = re.sub(r'(?<![\w-])' + re.escape(v) + r'(?![\w-])', n, z)
            if z != w: falhas.append(f'{f}: célula mudou além de nome/link: {x[:60]!r} -> {y[:60]!r}')
# nomes que deviam sumir de cada arquivo
for e in alt:
    if e['motivo'].startswith('Nome: elenco'):
        t = re.sub(r'\]\(<?[^)]*\)', ']', (S / e['arquivo']).read_text())
        if re.search(r'(?<![\w-])' + e['antes'] + r'(?![\w-])', t): falhas.append(f"{e['arquivo']}: ainda tem {e['antes']}")
fora = {}
for f in files:
    for alvo in re.findall(r'\]\(<?([^)>#]+)', (S / f).read_text()):
        if alvo.startswith('/home') or 'Planejamento' in alvo or (((S / f).parent / alvo).resolve().parent == G.resolve()):
            fora.setdefault(f, []).append(alvo.split('/')[-1])
out = {'arquivos': len(files), 'alteracoes': len(alt), 'links_ruins_antes': ruins_antes, 'links_ruins_depois': ruins_depois,
       'ainda_fora_do_livro': fora, 'falhas': falhas}
(A / 'conferencia.json').write_text(json.dumps(out, ensure_ascii=False, indent=1) + '\n')
print(json.dumps({k: v for k, v in out.items() if k != 'ainda_fora_do_livro'}, ensure_ascii=False, indent=1))
for k, v in fora.items(): print(' fora:', k, v)
sys.exit(1 if falhas else 0)

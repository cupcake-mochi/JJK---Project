"""Integra a R67 no texto: só os blocos da Técnica Máxima mudam.

Os PDFs continuam os da R66 (EDICAO-ATUAL.json não muda). A composição da R67
fica para outra rodada; até lá o texto corrente está à frente do PDF, como já
aconteceu na v0.361 (texto R47, PDF R46).
Roda uma vez, sobre a R66 intacta, e recusa rodar de novo.
"""
from pathlib import Path
import hashlib, json, sys
E = Path(__file__).resolve().parent
RAIZ = E.parents[5]
B = RAIZ/'sistema/05-material/livro/ciclo-maldito-r41'
sys.path.insert(0, str(E))
from trocas_r67 import TROCAS, MOTIVO

def ler(p): return p.read_text(encoding='utf-8')
def gravar(p, t): p.parent.mkdir(parents=True, exist_ok=True); p.write_text(t, encoding='utf-8')
def dump(p, v): gravar(p, json.dumps(v, ensure_ascii=False, indent=2) + '\n')
def editar(p, a, b):
    t = ler(p); assert t.count(a) == 1, (str(p), a, t.count(a)); gravar(p, t.replace(a, b, 1))

livro = B/'LIVRO-COMPLETO.md'
r66 = B/'revisao-de-regras/editorial-r66'
texto = ler(livro)
assert texto == ler(r66/'LIVRO-COMPLETO-R66.md'), 'LIVRO-COMPLETO.md não é a R66 intacta'
snap = json.loads(ler(r66/'BLOCOS-R66.json'))
ops = []
for k, antes, depois in TROCAS:
    assert texto.count(antes) == 1 and snap[k].count(antes) == 1, k
    texto = texto.replace(antes, depois, 1)
    snap[k] = snap[k].replace(antes, depois, 1)
    ops.append({'id': f'R67-{len(ops)+1:02}', 'bloco': k, 'antes': antes, 'depois': depois, 'motivo': MOTIVO})

gravar(livro, texto)
gravar(E/'LIVRO-COMPLETO-R67.md', texto)
dump(E/'BLOCOS-R67.json', snap)
dump(B/'revisao-de-regras/alteracoes/R66-para-R67.json', ops)
dump(E/'FONTE-PUBLICADA.json', {
    'revisao': 'R67',
    'sha256_texto': hashlib.sha256(livro.read_bytes()).hexdigest(),
    'blocos': len(snap),
    'registros': len(ops),
    'pdf': 'pendente: os PDFs publicados e o EDICAO-ATUAL.json continuam os da R66',
    'tipo': 'Regra: Técnica Máxima com Forma e função pagas nos dados, decidida pelo autor em 12/11/2026.'})

# Ponteiros da fonte corrente, no mesmo molde da integração da R66.
p = RAIZ/'conferir-repositorio.py'
t = ler(p); ini = t.index("bloco('12. FONTE R66"); fim = t.index('# ----', ini)
parte = t[ini:fim].replace('R66', 'R67').replace("'editorial-r66'", "'editorial-r67'").replace('range(54, 67)', 'range(54, 68)')
assert parte != t[ini:fim]
gravar(p, t[:ini] + parte + t[fim:])
for nome in ['editorial-r57', 'fundamento-r53']:
    editar(B/f'revisao-de-regras/{nome}/testar-integridade.py', "bloco('12. FONTE R66", "bloco('12. FONTE R67")
editar(B/'revisao-de-regras/editorial-r57/testar-integridade.py', 'R65-para-R66.json', 'R66-para-R67.json')
editar(B/'revisao-de-regras/fundamento-r53/testar-integridade.py', 'fonte corrente R66', 'fonte corrente R67')
editar(RAIZ/'sistema/03-mecanica/conferir-fundamento.py', 'editorial-r66/BLOCOS-R66.json', 'editorial-r67/BLOCOS-R67.json')
editar(RAIZ/'sistema/03-mecanica/livro.py', 'edição atual, R66', 'edição atual, R67')
print('Integrada R67:', len(ops), 'trocas em', len({o['bloco'] for o in ops}), 'blocos.')

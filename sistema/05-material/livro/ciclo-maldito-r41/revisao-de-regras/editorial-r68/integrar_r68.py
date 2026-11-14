"""Integra a R68 no texto: duas frases das seções de Controle, no molde do integrar_r67.py.

Os PDFs entram depois, por integrar_pdf_r68.py. Roda uma vez, sobre a R67 intacta,
e recusa rodar de novo.
"""
from pathlib import Path
import hashlib, json, sys
E = Path(__file__).resolve().parent
RAIZ = E.parents[5]
B = RAIZ/'sistema/05-material/livro/ciclo-maldito-r41'
sys.path.insert(0, str(E))
from trocas_r68 import TROCAS, MOTIVO

def ler(p): return p.read_text(encoding='utf-8')
def gravar(p, t): p.parent.mkdir(parents=True, exist_ok=True); p.write_bytes(t.encode('utf-8'))
def dump(p, v): gravar(p, json.dumps(v, ensure_ascii=False, indent=2) + '\n')
def editar(p, a, b):
    t = ler(p); assert t.count(a) == 1, (str(p), a, t.count(a)); gravar(p, t.replace(a, b, 1))

livro = B/'LIVRO-COMPLETO.md'
r67 = B/'revisao-de-regras/editorial-r67'
texto = ler(livro)
assert texto == ler(r67/'LIVRO-COMPLETO-R67.md'), 'LIVRO-COMPLETO.md não é a R67 intacta'
snap = json.loads(ler(r67/'BLOCOS-R67.json'))
ops = []
for k, antes, depois in TROCAS:
    assert texto.count(antes) == 1 and snap[k].count(antes) == 1, k
    texto = texto.replace(antes, depois, 1)
    snap[k] = snap[k].replace(antes, depois, 1)
    ops.append({'id': f'R68-{len(ops)+1:02}', 'bloco': k, 'antes': antes, 'depois': depois, 'motivo': MOTIVO})

gravar(livro, texto)
gravar(E/'LIVRO-COMPLETO-R68.md', texto)
dump(E/'BLOCOS-R68.json', snap)
dump(B/'revisao-de-regras/alteracoes/R67-para-R68.json', ops)
dump(E/'FONTE-PUBLICADA.json', {
    'revisao': 'R68',
    'sha256_texto': hashlib.sha256(livro.read_bytes()).hexdigest(),
    'blocos': len(snap),
    'registros': len(ops),
    'pdf': 'pendente: integrar_pdf_r68.py',
    'tipo': 'Correção: reforço de Controle da Máxima sem dano nas seções de Controle, consequência da R67.'})

p = RAIZ/'conferir-repositorio.py'
t = ler(p); ini = t.index("bloco('12. FONTE R67"); fim = t.index('# ----', ini)
parte = t[ini:fim].replace('R67', 'R68').replace("'editorial-r67'", "'editorial-r68'").replace('range(54, 68)', 'range(54, 69)')
assert parte != t[ini:fim]
gravar(p, t[:ini] + parte + t[fim:])
for nome in ['editorial-r57', 'fundamento-r53']:
    editar(B/f'revisao-de-regras/{nome}/testar-integridade.py', "bloco('12. FONTE R67", "bloco('12. FONTE R68")
editar(B/'revisao-de-regras/editorial-r57/testar-integridade.py', 'R66-para-R67.json', 'R67-para-R68.json')
editar(B/'revisao-de-regras/fundamento-r53/testar-integridade.py', 'fonte corrente R67', 'fonte corrente R68')
editar(RAIZ/'sistema/03-mecanica/conferir-fundamento.py', 'editorial-r67/BLOCOS-R67.json', 'editorial-r68/BLOCOS-R68.json')
editar(RAIZ/'sistema/03-mecanica/livro.py', 'edição atual, R67', 'edição atual, R68')
print('Integrada R68:', len(ops), 'trocas em', len({o['bloco'] for o in ops}), 'blocos.')

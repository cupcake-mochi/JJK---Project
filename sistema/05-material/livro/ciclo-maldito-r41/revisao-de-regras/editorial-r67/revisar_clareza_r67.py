"""Refaz o texto da R67 depois da revisão de clareza feita na composição (12/11/2026).

Seis ajustes de redação nas trocas, sem mudar número nem regra: a linha coletiva da
tabela nova, "Nenhuma" no lugar de "0", "o da base da função", a conta completa do
exemplo, "até Pesada" e o encaminhamento da vida temporária em Aplicação sem dano.
Parte da R66 intacta, aplica trocas_r67.py e confere que só esses trechos mudaram.
Os ponteiros que o integrar_r67.py trocou continuam valendo e não são tocados aqui.
"""
from pathlib import Path
import difflib, hashlib, json, sys
E = Path(__file__).resolve().parent
B = E.parents[1]
sys.path.insert(0, str(E))
from trocas_r67 import TROCAS, MOTIVO

def ler(p): return p.read_text(encoding='utf-8')
def gravar(p, t): p.write_text(t, encoding='utf-8')
def dump(p, v): gravar(p, json.dumps(v, ensure_ascii=False, indent=2) + '\n')

r66 = B/'revisao-de-regras/editorial-r66'
texto = ler(r66/'LIVRO-COMPLETO-R66.md'); snap = json.loads(ler(r66/'BLOCOS-R66.json'))
anterior = ler(E/'LIVRO-COMPLETO-R67.md')
assert ler(B/'LIVRO-COMPLETO.md') == anterior, 'LIVRO-COMPLETO.md não é a R67 antes da revisão'
ops = []
for k, antes, depois in TROCAS:
    assert texto.count(antes) == 1 and snap[k].count(antes) == 1, k
    texto = texto.replace(antes, depois, 1); snap[k] = snap[k].replace(antes, depois, 1)
    ops.append({'id': f'R67-{len(ops)+1:02}', 'bloco': k, 'antes': antes, 'depois': depois, 'motivo': MOTIVO})
mudou = [l for l in difflib.unified_diff(anterior.splitlines(), texto.splitlines(), lineterm='', n=0) if l[:1] in '+-' and l[:3] not in ('+++', '---')]
assert len(mudou) == 12, mudou   # 6 linhas da R67 saem e 6 entram
gravar(B/'LIVRO-COMPLETO.md', texto); gravar(E/'LIVRO-COMPLETO-R67.md', texto)
dump(E/'BLOCOS-R67.json', snap)
dump(B/'revisao-de-regras/alteracoes/R66-para-R67.json', ops)
f = json.loads(ler(E/'FONTE-PUBLICADA.json'))
f.update(sha256_texto=hashlib.sha256((B/'LIVRO-COMPLETO.md').read_bytes()).hexdigest(), blocos=len(snap), registros=len(ops))
dump(E/'FONTE-PUBLICADA.json', f)
print('R67 revista:', len(ops), 'trocas;', len(mudou) // 2, 'linhas de texto ajustadas.')
for l in mudou: print(l[:230])

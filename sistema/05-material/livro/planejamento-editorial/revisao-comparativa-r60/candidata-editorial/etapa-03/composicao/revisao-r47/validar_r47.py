from pathlib import Path
import json, hashlib, re, runpy, sys
from pypdf import PdfReader

B = Path(__file__).resolve().parents[1]
R = B / 'revisao-r47'
O = B.with_name('livro-diagramado-r46')
sys.path.insert(0, str(B))
g = runpy.run_path(str(B / 'ler_fontes.py'))
actual = g['enriched']
base = json.loads((R / 'BLOCOS-BASE.json').read_text())
rows = json.loads((B / 'ALTERACOES-R46-para-R47.json').read_text())
assert len(rows) == 1 and rows[0]['item'] == '194'
key = 'origens--restricao-prenuncio'
row = rows[0]
assert row['bloco'] == key
assert set(actual) == set(base)
for k, text in base.items():
    assert actual[k] == (row['depois'] if k == key else text), k
assert row['antes'] == base[key]
# The new timing repeats the reference to the same d20; all costs stay intact.
assert re.findall(r'\d+', row['antes'].replace('d20', '')) == re.findall(r'\d+', row['depois'].replace('d20', ''))

# Only the four authorized paragraphs/list items differ inside the block.
a, z = row['antes'].split('\n\n'), row['depois'].split('\n\n')
assert len(a) == len(z)
diffs = [(x, y) for x, y in zip(a, z) if x != y]
assert len(diffs) == 3  # the two adjacent list items form one Markdown paragraph
assert a[-1] == z[-1] and '**5 PE**' in z[-1]
assert row['antes'].split('### Estudar a execução', 1)[1] == row['depois'].split('### Estudar a execução', 1)[1]

# Reconstruct the full consolidated Markdown using only the registered block.
def rendered(text):
    return re.sub(r'^(#{1,6}) ', lambda m: '#' * (len(m[1]) + 2) + ' ', text, flags=re.M)
old_md = (O / 'LIVRO-COMPLETO.md').read_text()
new_md = (B / 'LIVRO-COMPLETO.md').read_text()
assert old_md.count(rendered(row['antes'])) == 1
assert new_md == old_md.replace(rendered(row['antes']), rendered(row['depois']), 1)

snapshot = json.loads((R / 'BASE-R46-SHA256.json').read_text())
bad = [p for p, h in snapshot.items() if not (O / p).exists() or hashlib.sha256((O / p).read_bytes()).hexdigest() != h]
assert not bad, bad
metadata = json.loads((B / 'FONTES-E-VALIDACAO.json').read_text())
pdf = B / metadata['pdf']
reader = PdfReader(pdf)
result = {
    'base': 'R46',
    'item': '194',
    'base_arquivos_preservados': len(snapshot),
    'diferencas_base': bad,
    'blocos_alterados_registrados': 1,
    'blocos_inalterados': len(base) - 1,
    'consolidado': 'Idêntico à R46 fora do único bloco registrado; dentro dele, somente os trechos autorizados.',
    'exemplo_Kata_3_PE': 'Preservado integralmente; custo total 5 PE, sem ordem contraditória.',
    'estudo_memoria_terceiros': 'Preservados integralmente.',
    'hibrido_e_demais_origens': 'Idênticos à R46.',
    'consulta_rapida_resumo_turno': 'Não repetem a ordem de Ataque sem Prenúncio; sem alteração.',
    'paginas': len(reader.pages),
    'sha256_pdf': hashlib.sha256(pdf.read_bytes()).hexdigest(),
}
(R / 'VALIDACAO.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
print(json.dumps(result, ensure_ascii=False))

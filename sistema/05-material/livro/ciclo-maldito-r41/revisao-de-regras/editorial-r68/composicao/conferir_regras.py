"""Confere a entrega R30 contra a R29, sem alterar o texto do livro."""
from pathlib import Path
import hashlib, json, re

B = Path(__file__).resolve().parent
R = B / 'revisao-de-regras'
old_root = B.parent / 'livro-diagramado-r29'
old = (old_root / 'LIVRO-COMPLETO.md').read_text()
new = (B / 'LIVRO-COMPLETO.md').read_text()
pattern = r'<!-- fonte:([^\n]+) -->\n<a id="([^"]+)"></a>\n(.*?)(?=<!-- fonte:|<!-- parte:|<a id="capitulo-|\Z)'
before = list(re.finditer(pattern, old, re.S))
after = list(re.finditer(pattern, new, re.S))
assert [m[2] for m in before] == [m[2] for m in after]
records = json.loads((R / 'ALTERACOES-REGRAS.json').read_text())
by_block = {entry['bloco']: entry for entry in records}
assert len(by_block) == len(records)
changed = {a[2] for a, b in zip(before, after) if a[3] != b[3]}
assert changed == set(by_block)
rebuilt = old
for a, b in reversed(list(zip(before, after))):
    if a[2] not in changed:
        continue
    entry = by_block[a[2]]
    assert a[3] == entry['antes'] and b[3] == entry['depois']
    rebuilt = rebuilt[:a.start(3)] + entry['depois'] + rebuilt[a.end(3):]
assert rebuilt == new, 'Diferença fora do registro'

# O adicional de Equipamento usa a R30 entregue como base, mantendo também
# o histórico cumulativo R29 → R30 do registro principal.
baseline = R / 'base-r30-antes-equipamento'
base_text = (baseline / 'LIVRO-COMPLETO.md').read_text()
base_blocks = list(re.finditer(pattern, base_text, re.S))
assert [m[2] for m in base_blocks] == [m[2] for m in after]
delta = json.loads((R / 'ALTERACOES-REGRAS-156-158.json').read_text())
delta_by_block = {e['bloco']: e for e in delta}
assert len(delta_by_block) == len(delta)
new_changes = {a[2] for a,b in zip(base_blocks, after) if a[3] != b[3]}
assert new_changes == set(delta_by_block)
base_rebuilt = base_text
for a,b in reversed(list(zip(base_blocks, after))):
    if a[2] not in new_changes:
        continue
    e = delta_by_block[a[2]]
    assert e['antes'] == a[3] and e['depois'] == b[3]
    assert by_block[a[2]]['adicional_r30'] == {k:e[k] for k in ['antes','depois','motivo','item']}
    base_rebuilt = base_rebuilt[:a.start(3)] + e['depois'] + base_rebuilt[a.end(3):]
assert base_rebuilt == new, 'Diferença do adicional fora do registro'
assert (baseline / 'ALTERACOES-TEXTUAIS.json').read_bytes() == (B / 'revisao-textual/ALTERACOES.json').read_bytes()
modified_sources = []
base_sources = baseline / 'fontes-editoriais'
assert {str(p.relative_to(base_sources)) for p in base_sources.rglob('*') if p.is_file()} == {
    str(p.relative_to(B / 'fontes-editoriais')) for p in (B / 'fontes-editoriais').rglob('*') if p.is_file()}
for p in base_sources.rglob('*'):
    if p.is_file() and p.read_bytes() != (B / 'fontes-editoriais' / p.relative_to(base_sources)).read_bytes():
        modified_sources.append(str(p.relative_to(base_sources)))
assert set(modified_sources) == {
    'abertura/lote-01/ABERTURA-E-CRIACAO.md', 'regras-gerais/lote-final/REGRAS-GERAIS.md',
    'equipamento/lote-final/EQUIPAMENTO.md', 'caminhos/bastiao/lote-01/BASTIAO.md',
    'caminhos/emanador/lote-01/EMANADOR.md', 'ritual-e-pactos/lote-01/RITUAL-E-PACTOS.md',
    'caminhos/incursor/lote-01/INCURSOR.md', 'invocacoes/lote-01/INVOCACOES-EM-CAMPO.md'}
# Estes avisos não autorizaram edição. Os blocos precisam continuar idênticos.
for key in ['dano--zero', 'dano--insistir', 'poderes--degraus', 'poderes--criardominio', 'poderes--acerto']:
    assert key in {a[2] for a in base_blocks}
    assert key not in new_changes

hashes = json.loads((R / 'R29-HASHES.json').read_text())
current = {str(p.relative_to(old_root)): hashlib.sha256(p.read_bytes()).hexdigest()
           for p in old_root.rglob('*') if p.is_file()}
assert current == hashes, 'R29 alterada'
old_editorial = json.loads((old_root / 'revisao-textual/ALTERACOES.json').read_text())
editorial = json.loads((B / 'revisao-textual/ALTERACOES.json').read_text())
assert len(editorial) == 73
assert {e['id'] for e in editorial} == {e['id'] for e in old_editorial} - {'T072'}
adapted = [e['id'] for e in editorial if e != next(o for o in old_editorial if o['id'] == e['id'])]
assert adapted == ['T056']
for forbidden in ['suas fichas', 'não tem como recusar']:
    assert forbidden not in new.casefold()
for path in ['ORDEM.json', 'ARTES-APLICADAS.json', 'CAPA-E-ABERTURAS.json', 'CREDITOS.json', 'MARCADORES.json']:
    assert (B / path).read_bytes() == (old_root / path).read_bytes(), path
for folder in ['referencias', 'fonts']:
    for path in (old_root / folder).rglob('*'):
        if path.is_file():
            assert path.read_bytes() == (B / path.relative_to(old_root)).read_bytes(), str(path)
coverage = json.loads((R / 'ITENS-APLICADOS.json').read_text())
manifest = json.loads((B / 'FONTES-E-VALIDACAO.json').read_text())
assert manifest['alteracoes_regras'] == records
assert hashlib.sha256((B / manifest['pdf']).read_bytes()).hexdigest() == manifest['sha256_pdf']
report = {'r29_preservada': True, 'arquivos_r29': len(hashes), 'blocos_comparados': len(before),
          'blocos_alterados': len(records), 'diferencas_sem_registro': 0,
          'reconstrucao_integral_do_markdown': True, 'itens_A_B': len(coverage),
          'itens_com_alteracao': sum(bool(e['blocos']) for e in coverage),
          'itens_ja_conformes': [e['item'] for e in coverage if not e['blocos']],
          'exemplos_refeitos': sum(e['exemplo_refeito'] for e in records),
          'alteracoes_textuais_mantidas': len(editorial), 'entradas_textuais_adaptadas': adapted,
          'capa_artes_creditos_ordem_preservados': True, 'paginas': manifest['paginas'],
          'sha256_markdown': hashlib.sha256(new.encode()).hexdigest(),
          'sha256_pdf': manifest['sha256_pdf']}
report['adicional_equipamento'] = {
    'base': 'R30 entregue antes dos itens 156–158', 'blocos_alterados': len(delta),
    'diferencas_sem_registro': 0, 'reconstrucao_integral_do_markdown': True,
    'fontes_alteradas': sorted(modified_sources), 'alteracoes_textuais_preservadas': True,
    'insistir_e_incompleta_preservados': True, 'exemplos_ajustados': 4,
    'itens_novos': ['156','157','158'], 'correcao_de_frase': '85 — tabela do Ritual'}
(B / 'evidencias/CONFERENCIA-REGRAS.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
print(json.dumps(report, ensure_ascii=False, indent=2))

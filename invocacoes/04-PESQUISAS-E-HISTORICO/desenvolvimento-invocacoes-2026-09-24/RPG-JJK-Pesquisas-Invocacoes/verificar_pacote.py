"""Confere a integridade desta exportação. Não valida regras de jogo ou fontes externas."""
from pathlib import Path
import hashlib
import json


def main() -> None:
    root = Path(__file__).resolve().parent
    manifest = json.loads((root / 'MANIFESTO.json').read_text(encoding='utf-8'))
    failures = []
    for entry in manifest['files']:
        path = root / entry['path']
        if not path.is_file():
            failures.append(f"Ausente: {entry['path']}")
            continue
        actual = hashlib.sha256(path.read_bytes()).hexdigest()
        if actual != entry['sha256']:
            failures.append(f"Alterado: {entry['path']}")
    for report in manifest['reports']:
        source = (root / report['original_report']).read_text(encoding='utf-8')
        converted = (root / report['exported_report']).read_text(encoding='utf-8')
        body = converted.split('\n\n---\n\n## Referências da pesquisa original — exportadas', 1)[0]
        refs = json.loads((root / report['references_file']).read_text(encoding='utf-8'))
        for ref in refs['references']:
            body = body.replace(f"[^{ref['label']}]", ref['original_marker'])
        if body != source:
            failures.append(f"Texto não preservado: {report['title']}")
    if failures:
        raise SystemExit('\n'.join(failures))
    print(f"Integridade confirmada: {len(manifest['files'])} arquivos e dois relatórios integrais.")
    print('Esta conferência não verifica fatos externos, regras ou balanceamento.')


if __name__ == '__main__':
    main()

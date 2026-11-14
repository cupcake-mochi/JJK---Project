"""Confere a publicação da R68: baixa as duas URLs públicas inteiras e compara o SHA-256
com o EDICAO-ATUAL.json. No molde do editorial-r67/verificar_publicacao.py.
A Vercel publica do repositório JJK---PDF---RPG, não deste: o merge aqui não publica."""
from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo
import urllib.request, hashlib, json, concurrent.futures, subprocess
P = Path(__file__).resolve().parent; R = P.parents[5]; Q = Path(r'E:\Claude\Claude 2\.claude\worktrees\pdf-r68')
meta = json.loads((R/'sistema/05-material/livro/EDICAO-ATUAL.json').read_text(encoding='utf-8'))
assert meta == json.loads((Q/'livro/EDICAO-ATUAL.json').read_text(encoding='utf-8')), 'EDICAO-ATUAL difere entre os dois repositórios'
def fetch(pal):
    url = meta[pal]['url']
    req = urllib.request.Request(url, headers={'Cache-Control': 'no-cache', 'User-Agent': 'Ciclo-Maldito-publication-check'})
    with urllib.request.urlopen(req, timeout=60) as r:
        h = hashlib.sha256(); size = 0
        while chunk := r.read(1024*1024): h.update(chunk); size += len(chunk)
        res = {'url': url, 'url_final': r.url, 'status': r.status, 'tipo': r.headers.get('Content-Type'), 'sha256': h.hexdigest(), 'bytes': size}
    res['identico_ao_aprovado'] = res['sha256'] == meta[pal]['sha256']
    return pal, res
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as ex: results = dict(ex.map(fetch, ['claro', 'noturno']))
good = all(x['identico_ao_aprovado'] and x['status'] == 200 for x in results.values())
rev = lambda d: subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=d, text=True).strip()
record = {'estado': 'publicada e verificada' if good else 'aguardando atualização pública', 'revisao': meta['revisao'], 'paginas': meta['paginas'],
          'commit_sistema': rev(R), 'commit_pdf': rev(Q), 'verificado_em': datetime.now(ZoneInfo('America/Sao_Paulo')).isoformat(),
          'verificacao': 'Download integral das duas URLs públicas e comparação SHA-256 com os PDFs aprovados na composição da R68.', **results}
(P/'PUBLICACAO.json').write_bytes((json.dumps(record, ensure_ascii=False, indent=2) + '\n').encode('utf-8'))
print(json.dumps(record, ensure_ascii=False, indent=1))
raise SystemExit(0 if good else 1)

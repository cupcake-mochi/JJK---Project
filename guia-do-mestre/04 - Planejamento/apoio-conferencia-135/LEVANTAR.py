"""Levantamento automático do conjunto revisto (capítulos, casos, consultas): remissões a originais já revistos,
remissões a capítulos antigos, nomes de exemplo repetidos, frases duplicadas entre arquivos e termos de processo.
Só aponta onde ler; não substitui a leitura."""
from pathlib import Path
from collections import defaultdict, Counter
import json, re
A = Path(__file__).resolve().parent; R = A.parents[1]; G = R / '06 - Redacao do Guia'; S = G / 'revisao-98'
est = json.loads((R / '04 - Planejamento/apoio-estrutura-99/estrutura-e-fontes.json').read_text())
files = sorted([p for p in S.glob('*.md') if p.name != 'LEIA-ME.md'] + list((S / 'casos').glob('*.md')) + [p for p in (S / 'consultas').glob('*.md') if p.name != 'LEIA-ME.md'])
revised = {p.name: p for p in list((S / 'casos').glob('*.md')) + list((S / 'consultas').glob('*.md'))}
chapter_src = {f['fonte'].split('/')[-1] for f in est['fontes']} - set(revised)
link = re.compile(r'\[([^\]]+)\]\(<?([^)>#]+\.md)(#[^)>]*)?>?\)')
stale, oldchap, broken = defaultdict(list), defaultdict(list), defaultdict(list)
for p in files:
    for txt, tgt, frag in link.findall(p.read_text()):
        dest = (p.parent / tgt).resolve()
        if not dest.exists(): broken[str(p.relative_to(S))].append(tgt); continue
        if dest.parent == G and dest.name in revised: stale[str(p.relative_to(S))].append(dest.name)
        elif dest.parent == G and dest.name in chapter_src: oldchap[str(p.relative_to(S))].append(dest.name)
# nomes de exemplo
names = ['Haru', 'Rui', 'Rina', 'Mei', 'Akira', 'Ren', 'Sora', 'Kaori', 'Mina', 'Emi', 'Nara', 'Davi', 'Ana', 'Tessa', 'Maia', 'Taru', 'Aline', 'Nao', 'Arata', 'Yuki', 'Kenji', 'Hana', 'Aoi', 'Daichi', 'Riku', 'Sana', 'Toma', 'Leo', 'Iris']
where = {n: sorted({str(p.relative_to(S)) for p in files if re.search(r'\b' + n + r'\b', p.read_text())}) for n in names}
# frases longas repetidas entre arquivos
sent = defaultdict(set)
for p in files:
    for s in re.split(r'(?<=[.!?])\s+', re.sub(r'\s+', ' ', re.sub(r'[*_`>|#\[\]]|\(<?[^)]*\.md[^)]*\)', ' ', p.read_text()))):
        s = s.strip()
        if len(s.split()) >= 14: sent[s].add(str(p.relative_to(S)))
dup = sorted(((s, sorted(f)) for s, f in sent.items() if len(f) >= 2), key=lambda x: -len(x[1]))
# termos de processo no texto ao leitor
proc = re.compile(r'\b(registro \d{2,3}|lote [A-C]\d|R5\d|Codex|pré-1\.0|Pré-1\.0|livro-base|GPT|Claude)\b')
procs = {str(p.relative_to(S)): sorted(set(proc.findall(p.read_text()))) for p in files if proc.search(p.read_text())}
out = {'arquivos': len(files), 'palavras': sum(len(p.read_text().split()) for p in files),
       'remissoes_a_original_ja_revisto': {k: dict(Counter(v)) for k, v in stale.items()},
       'remissoes_a_capitulo_antigo': {k: dict(Counter(v)) for k, v in oldchap.items()},
       'links_quebrados': dict(broken), 'nomes': {n: w for n, w in where.items() if len(w) >= 2},
       'frases_repetidas': [{'frase': s, 'arquivos': f} for s, f in dup], 'termos_de_processo': procs}
(A / 'levantamento.json').write_text(json.dumps(out, ensure_ascii=False, indent=2) + '\n')
print('arquivos', out['arquivos'], 'palavras', out['palavras'])
print('remissões a original já revisto:', sum(len(v) for v in stale.values()), 'em', len(stale), 'arquivos')
print('remissões a capítulo antigo:', sum(len(v) for v in oldchap.values()), 'em', len(oldchap), 'arquivos')
print('links quebrados:', sum(len(v) for v in broken.values()))
print('frases longas repetidas entre arquivos:', len(dup))
print('arquivos com termo de processo:', len(procs))
for n, w in out['nomes'].items(): print(f'  {n}: {len(w)} arquivos')

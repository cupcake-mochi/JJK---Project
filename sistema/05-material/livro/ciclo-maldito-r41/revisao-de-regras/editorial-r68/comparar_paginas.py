"""Compara R67 e R68 página a página: texto extraído e pixels renderizados, nas duas paletas.
Uso: comparar_paginas.py <pasta R67 com os 2 PDFs> <pasta R68 com os 2 PDFs> <saída>"""
import sys, json, hashlib
from pathlib import Path
import pymupdf
a, b, out = map(Path, sys.argv[1:4]); out.mkdir(parents=True, exist_ok=True)
res = {}
for pal, nome in [('claro', 'Ciclo-Maldito-Livro-de-Regras.pdf'), ('noturno', 'Ciclo-Maldito-Livro-de-Regras-Noturno.pdf')]:
    A, B = pymupdf.open(a/nome), pymupdf.open(b/nome)
    texto, visual = [], []
    for i in range(min(len(A), len(B))):
        ta, tb = A[i].get_text(), B[i].get_text()
        pa = A[i].get_pixmap(dpi=40).samples; pb = B[i].get_pixmap(dpi=40).samples
        if ta != tb: texto.append(i+1)
        elif hashlib.md5(pa).digest() != hashlib.md5(pb).digest(): visual.append(i+1)
    for n in texto + visual:
        for tag, D in (('r67', A), ('r68', B)):
            D[n-1].get_pixmap(dpi=110).save(out/f'{pal}-{tag}-p{n:03d}.png')
    res[pal] = {'paginas_r67': len(A), 'paginas_r68': len(B), 'texto_mudou': texto, 'so_visual_mudou': visual}
(out/'COMPARACAO.json').write_text(json.dumps(res, ensure_ascii=False, indent=1), encoding='utf-8')
print(json.dumps(res, ensure_ascii=False))

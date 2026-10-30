"""Renderizar a prova a 70 dpi e montar folhas de contato de quatro páginas para a inspeção."""
import glob, subprocess, sys
from pathlib import Path
from PIL import Image
d = Path(sys.argv[1])
for f in d.glob('p-*.png'): f.unlink()
subprocess.run(['pdftoppm', '-r', '70', '-png', str(next(d.glob('*.pdf'))), str(d / 'p')], check=True)
fs = sorted(d.glob('p-*.png'))
for k in range(0, len(fs), 4):
    ims = [Image.open(f) for f in fs[k:k + 4]]
    w, h = ims[0].size; sheet = Image.new('RGB', (w * 4 + 30, h), 'white')
    for i, im in enumerate(ims): sheet.paste(im, (i * (w + 10), 0))
    sheet.save(d / f'folha-{k // 4 + 1}.png')
print(len(fs))

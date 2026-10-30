"""Mapas do lote B2-04.

s073: exporta o desenho vetorial existente (MAPAS.py), sem alterá-lo.
s076: mesmo recinto e mesmo estilo, com as posições da tabela do próprio caso.
O desenho do s076 é feito aqui, numa subclasse, para não modificar o arquivo original.
"""
from pathlib import Path
from reportlab.pdfgen.canvas import Canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import white
import json, hashlib, subprocess

A = Path(__file__).resolve().parent
R = A.parents[1]
B = R / '08 - Diagramacao do Guia'
G = {}
src = B / 'MAPAS.py'
exec(compile(src.read_text(), str(src), 'exec'), G)
for name, file in [('Body', 'Spectral-Regular.ttf'), ('Bold', 'Spectral-SemiBold.ttf'), ('Italic', 'Spectral-Italic.ttf'), ('Head', 'BarlowCondensed-SemiBold.ttf')]:
    pdfmetrics.registerFont(TTFont(name, str(B / 'fontes' / file)))
# Mesma família do gerador do livro, para o negrito das legendas.
pdfmetrics.registerFontFamily('Body', normal='Body', bold='Bold', italic='Italic', boldItalic='Bold')

Base = G['Mapa']


class Mapa(Base):
    def __init__(self, key, width):
        if key == 's076':
            super().__init__('s073', width)
            self.key = 's076'
            self.height = 325
        else:
            super().__init__(key, width)

    def s076(self):
        self.label(14, 304, 'REN E SORA · POSIÇÕES INICIAIS', 15, 'Head', 'left')
        c = self.canv
        x, y, sz = 39, 50, 18
        self.grid('ABCDEFGH', 12, x, y, sz, white)
        self.line([(x, y), (x, y + 12 * sz), (x + 8 * sz, y + 12 * sz), (x + 8 * sz, y)], self.ink, 1)
        self.line([(x, y), (x + 2 * sz, y)], self.ink, 2)
        self.line([(x + 6 * sz, y), (x + 8 * sz, y)], self.ink, 2)
        # Ren em D5 (coluna 3, linha 5); Sora em F8 (coluna 5, linha 8), com o estojo.
        for col, row, text in [(3, 5, 'REN'), (5, 8, 'SORA')]:
            c.setFillColor(self.accent)
            c.rect(x + col * sz, y + (row - 1) * sz, sz, sz, stroke=0, fill=1)
            self.label(x + (col + .5) * sz, y + (row - .5) * sz - 3, text, 7.5, 'Head', color=white)
        for col, t in [(2, 'R'), (3, 'M'), (5, 'A')]:
            self.label(x + (col + .5) * sz, y - 17, t, 11, 'Head')
        self.label(x - 9, y - 17, '0', 9.5, 'Body', 'right')
        self.label(x + 4 * sz, 11, 'Porta: C–F · 6 m', 10, 'Body')
        self.note(220, 270, 248, '<b>Recinto: 12 × 18 m.</b><br/>Cada célula mede 1,5 m.<br/>A linha 0 fica no exterior.')
        self.note(220, 203, 248, '<b>Ren:</b> D5.<br/><b>Sora, com o estojo:</b> F8.<br/><b>R · Rina:</b> C0.<br/><b>M · Mei:</b> D0.<br/><b>A · Akira:</b> F0.')
        self.note(220, 99, 248, 'Sem armadilhas, reforços ou cobertura.<br/>Linhas negativas continuam para fora do recinto.')


(A / 'imagens').mkdir(exist_ok=True)
(A / 'tmp/pdfs').mkdir(parents=True, exist_ok=True)
rows = []
for ident, name, origem in [('s073', 'ensaio', 'desenho existente em MAPAS.py, sem alteração'),
                            ('s076', 'confronto', 'novo desenho deste apoio, mesmo estilo e grade do s073, com as posições da tabela do caso')]:
    obj = Mapa(ident, 488)
    pdf = A / f'tmp/pdfs/{name}.pdf'
    c = Canvas(str(pdf), pagesize=(488, obj.height), invariant=1)
    obj.drawOn(c, 0, 0)
    c.showPage()
    c.save()
    svg = A / f'imagens/{name}.svg'
    subprocess.run(['pdftocairo', '-svg', str(pdf), str(svg)], check=True)
    png = A / f'tmp/{name}.png'
    subprocess.run(['pdftoppm', '-png', '-r', '150', '-singlefile', str(pdf), str(png.with_suffix(''))], check=True)
    rows.append({'id': ident, 'figura': str(svg.relative_to(R)), 'sha256': hashlib.sha256(svg.read_bytes()).hexdigest(),
                 'origem': origem, 'codigo': str(src.relative_to(R)) if ident == 's073' else str((A / 'GERAR-MAPAS.py').relative_to(R)),
                 'altura_pontos': obj.height})

data = {
    'registro': 122,
    'mapas': rows,
    'origem_sha256': hashlib.sha256(src.read_bytes()).hexdigest(),
    'criterios': [
        'Conferido o mapa de referência mapa-vetorial-4.png contra o ensaio s073: Rina C0, Mei D0, Akira F0, caixa C6 e Sineiro D6/E6/D7/E7, recinto 12 × 18 m e porta C–F. Corresponde ao texto.',
        'O mapa do s073 foi exportado do desenho vetorial existente, com a altura do próprio desenho, sem a margem da página de referência.',
        'O s076 usa o mesmo recinto, mas outras posições. Não havia desenho para ele. Foi feito um vetor no mesmo estilo e grade, só com as posições da tabela do caso: Ren D5, Sora F8 com o estojo, Rina C0, Mei D0, Akira F0.',
        'Os casos s072 e s075 são fichas sem posições; não recebem mapa.',
    ],
    'limites': 'MAPAS.py não foi alterado. Sem edição de bitmap. O mapa do s076 é figura nova, derivada do texto, sem nova regra ou posição.',
}
(A / 'mapas-selecionados.json').write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')
print('Mapas exportados:', [r['id'] for r in rows])

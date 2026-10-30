"""Mapas do lote B2-05.

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
        if key == 's102':
            super().__init__('s073', width)
            self.key = 's102'
            self.height = 300
        else:
            super().__init__(key, width)

    def sala(self, x, y, sz, titulo, pecas):
        c = self.canv
        self.label(x, y + 14 * sz + 12, titulo, 10.5, 'Head', 'left')
        # linhas 0 e 13: passagem livre, sem parede nas pontas; as letras das colunas ficam na linha 13
        self.grid('ABCDEF', 12, x, y + sz, sz, white)
        self.line([(x, y + sz), (x, y + 13 * sz)], self.ink, 2)
        self.line([(x + 6 * sz, y + sz), (x + 6 * sz, y + 13 * sz)], self.ink, 2)
        self.label(x - 6, y + .5 * sz - 3, '0', 8.5, 'Body', 'right')
        self.label(x - 6, y + 13.5 * sz - 2, '13', 8.5, 'Body', 'right')
        # painel num suporte junto de C12 (linha 12 = topo da grade)
        c.setFillColor(self.ink)
        c.rect(x + 2 * sz + 3, y + 13 * sz - 2.5, sz - 6, 5, stroke=0, fill=1)
        for col, row, t, inimigo in pecas:
            cx, cy = x + col * sz, y + row * sz
            if inimigo:
                c.setFillColor(self.accent)
                c.rect(cx, cy, sz, sz, stroke=0, fill=1)
                self.label(cx + sz / 2, cy + sz / 2 - 3, t, 8.5, 'Head', color=white)
            else:
                self.label(cx + sz / 2, cy + sz / 2 - 3, t, 9, 'Head')

    def s102(self):
        self.label(14, 280, 'ARQUIVO · POSIÇÕES INICIAIS', 15, 'Head', 'left')
        sz = 15
        grupo = [(1, 0, 'Ba', False), (2, 0, 'Em', False), (3, 0, 'Gu', False)]
        self.sala(30, 14, sz, 'Haru sozinho', grupo + [(3, 10, 'H', True)])
        self.sala(150, 14, sz, 'Vigia e Tessa', grupo + [(2, 8, 'V', True), (4, 11, 'T', True)])
        self.note(272, 255, 210, '<b>Sala: 9 × 18 m.</b> Colunas A–F, linhas 1–12; cada célula mede 1,5 m. Linhas 0 e 13 são passagens abertas em todas as colunas.')
        self.note(272, 180, 210, '<b>Grupo:</b> Ba · Bastião B0, Em · Emanador C0, Gu · Guia D0.<br/><b>Haru:</b> D10.<br/><b>Vigia:</b> C8. <b>Tessa:</b> E11.')
        self.note(272, 105, 210, '<b>Painel:</b> barra junto de C12, acessível de B12, C12 ou D12.<br/>Escolha uma das duas versões.')


(A / 'imagens').mkdir(exist_ok=True)
(A / 'tmp/pdfs').mkdir(parents=True, exist_ok=True)
rows = []
for ident, name, origem in [('s079', 'po', 'desenho existente em MAPAS.py, sem alteração'),
                            ('s102', 'arquivo', 'novo desenho deste apoio, mesmo estilo dos mapas do Guia, com as posições da tabela do caso')]:
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
                 'origem': origem, 'codigo': str(src.relative_to(R)) if ident == 's079' else str((A / 'GERAR-MAPAS.py').relative_to(R)),
                 'altura_pontos': obj.height})

data = {
    'registro': 123,
    'mapas': rows,
    'origem_sha256': hashlib.sha256(src.read_bytes()).hexdigest(),
    'criterios': [
        'O desenho s079 de MAPAS.py foi conferido contra o caso: sala 3 × 18 m, faixas A e B, linhas 1–12 com pó, fecho e pino junto de A12, Mei em A0, Akira em B0 e exaustor junto de B0. Corresponde ao texto e substitui, na prova, o esquema em caracteres.',
        'O s102 tinha só uma tabela de posições. Foi feito um vetor no mesmo estilo, com as duas versões lado a lado (Haru sozinho; Vigia e Tessa), porque o texto pede escolher uma antes da sessão. Posições: Bastião B0, Emanador C0, Guia D0, Haru D10, Vigia C8, Tessa E11, painel junto de C12.',
        'O s101 é ficha sem posições; não recebe mapa.',
    ],
    'limites': 'MAPAS.py não foi alterado. Sem edição de bitmap. O mapa do s102 é figura nova, derivada da tabela do caso, sem nova regra ou posição.',
}
(A / 'mapas-selecionados.json').write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')
print('Mapas exportados:', [r['id'] for r in rows])

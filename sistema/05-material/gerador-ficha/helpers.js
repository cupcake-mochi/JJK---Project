// Helpers da FICHA. A paleta e a mesma do manual e do livro (Neve Saturado) de
// proposito: a ficha e o manual vao estar na mesma mesa.
const d = require('docx');
const { Paragraph, TextRun, Table, TableRow, TableCell, WidthType, ShadingType,
        AlignmentType, BorderStyle, VerticalAlign } = d;

const C = {
  // Neve Saturado, v0.200. Os nomes `crimson` e `deep` sao historicos e ficaram
  // para nao quebrar as referencias — hoje `crimson` e o ACENTO e `deep` e o SELO.
  ink:    '251727',
  crimson:'BC2A6E',
  deep:   '2B1B2E',
  grey:   '847B86',
  rule:   'F8C7DC',
  linha:  '9A6F87',   // a linha em que se escreve
  bandBg: 'F7E5EE',
  headBg: '2B1B2E',
  zebra:  'FADDEA',
  boxBg:  'FDF0F6',
  campoBg:'FDF0F6',   // fundo do campo preenchivel
};
const W = 9600;
const NIL = { style: BorderStyle.NIL };
const SEM_BORDA = { top: NIL, bottom: NIL, left: NIL, right: NIL,
                    insideHorizontal: NIL, insideVertical: NIL };

function runs(text, base = {}) {
  const out = [];
  const re = /(\*\*[^*]+\*\*|\*[^*]+\*|`[^`]+`)/g;
  let last = 0, m;
  while ((m = re.exec(text)) !== null) {
    if (m.index > last) out.push(new TextRun({ text: text.slice(last, m.index), ...base }));
    const t = m[0];
    if (t.startsWith('**')) out.push(new TextRun({ text: t.slice(2, -2), bold: true, ...base }));
    else if (t.startsWith('`')) out.push(new TextRun({ text: t.slice(1, -1), font: 'Consolas', size: 17, color: C.deep, ...base }));
    else out.push(new TextRun({ text: t.slice(1, -1), italics: true, ...base }));
    last = m.index + t.length;
  }
  if (last < text.length) out.push(new TextRun({ text: text.slice(last), ...base }));
  return out;
}

const P = (text, o = {}) => new Paragraph({
  children: runs(text, o.run || {}),
  spacing: { before: o.before ?? 0, after: o.after ?? 70, line: o.line ?? 232 },
  alignment: o.align,
});

// titulo de secao da ficha: faixa fina, caixa alta
const FAIXA = (texto) => new Table({
  rows: [new TableRow({ cantSplit: true, children: [new TableCell({
    children: [new Paragraph({ spacing: { before: 30, after: 30 },
      children: [new TextRun({ text: texto.toUpperCase(), bold: true, size: 17,
                               color: 'FFFFFF', font: 'Georgia', characterSpacing: 50 })] })],
    width: { size: W, type: WidthType.DXA },
    shading: { type: ShadingType.CLEAR, fill: C.headBg, color: 'auto' },
    margins: { top: 50, bottom: 50, left: 150, right: 150 },
  })] })],
  columnWidths: [W], width: { size: W, type: WidthType.DXA }, borders: SEM_BORDA,
});

// celula com rotulo pequeno em cima e espaco pra escrever embaixo
function campo(rotulo, valor, o = {}) {
  const kids = [
    new Paragraph({ spacing: { before: 20, after: 10 },
      children: [new TextRun({ text: rotulo.toUpperCase(), bold: true, size: 13,
                               color: C.grey, characterSpacing: 30 })] }),
    new Paragraph({ spacing: { before: 0, after: o.folga ?? 30 },
      children: [new TextRun({ text: valor || '', size: o.size ?? 20,
                               color: C.ink, bold: o.bold })] }),
  ];
  return new TableCell({
    children: kids, width: { size: o.w, type: WidthType.DXA }, columnSpan: o.span,
    shading: { type: ShadingType.CLEAR, fill: o.bg || C.campoBg, color: 'auto' },
    margins: { top: 42, bottom: 42, left: 120, right: 120 },
    verticalAlign: VerticalAlign.TOP,
    borders: { top: NIL, left: NIL, right: NIL,
               bottom: { style: BorderStyle.SINGLE, size: 6, color: C.linha } },
  });
}

// linha de campos
function LINHA(campos, larguras) {
  const total = larguras.reduce((a, b) => a + b, 0);
  const cw = larguras.map(x => Math.round(x * W / total));
  cw[cw.length - 1] = W - cw.slice(0, -1).reduce((a, b) => a + b, 0);
  return new Table({
    rows: [new TableRow({ cantSplit: true,
      children: campos.map((c, i) => campo(c[0], c[1], { w: cw[i], ...(c[2] || {}) })) })],
    columnWidths: cw, width: { size: W, type: WidthType.DXA }, borders: SEM_BORDA,
  });
}

// caixa grande pra escrever, com N linhas de altura
function BLOCO(rotulo, texto, linhas = 3) {
  const kids = [new Paragraph({ spacing: { before: 20, after: 60 },
    children: [new TextRun({ text: rotulo.toUpperCase(), bold: true, size: 13,
                             color: C.grey, characterSpacing: 30 })] })];
  if (texto) {
    kids.push(new Paragraph({ spacing: { after: 60, line: 260 },
      children: runs(texto, { size: 19 }) }));
    for (let i = 0; i < Math.max(0, linhas - 2); i++)
      kids.push(new Paragraph({ text: '', spacing: { after: 108 } }));
  } else {
    for (let i = 0; i < linhas; i++)
      kids.push(new Paragraph({ text: '', spacing: { after: 108 },
        border: { bottom: { style: BorderStyle.SINGLE, size: 4, color: C.rule, space: 2 } } }));
  }
  return new Table({
    rows: [new TableRow({ cantSplit: true, children: [new TableCell({
      children: kids, width: { size: W, type: WidthType.DXA },
      shading: { type: ShadingType.CLEAR, fill: C.campoBg, color: 'auto' },
      margins: { top: 70, bottom: 70, left: 150, right: 150 },
      borders: { left: { style: BorderStyle.SINGLE, size: 12, color: C.crimson },
                 top: NIL, bottom: NIL, right: NIL },
    })] })],
    columnWidths: [W], width: { size: W, type: WidthType.DXA }, borders: SEM_BORDA,
  });
}

// tabela comum
function cell(text, o = {}) {
  return new TableCell({
    children: Array.isArray(text) ? text : [new Paragraph({
      children: runs(String(text), { size: o.size || 17, color: o.color || C.ink, bold: o.bold }),
      alignment: o.align || AlignmentType.LEFT,
      spacing: { before: 18, after: 18, line: 215 } })],
    width: { size: o.w, type: WidthType.DXA }, columnSpan: o.span,
    shading: o.bg ? { type: ShadingType.CLEAR, fill: o.bg, color: 'auto' } : undefined,
    margins: { top: 26, bottom: 26, left: 90, right: 90 },
    verticalAlign: VerticalAlign.CENTER,
  });
}

function TBL(headers, rows, widths, opt = {}) {
  const total = widths.reduce((a, b) => a + b, 0);
  const cw = widths.map(x => Math.round(x * W / total));
  cw[cw.length - 1] = W - cw.slice(0, -1).reduce((a, b) => a + b, 0);
  const trs = [];
  if (headers) trs.push(new TableRow({ tableHeader: true, cantSplit: true,
    children: headers.map((h, i) => cell(h, { w: cw[i], bg: C.headBg, color: 'FFFFFF',
      bold: true, size: 15,
      align: i === 0 ? AlignmentType.LEFT : AlignmentType.CENTER })) }));
  rows.forEach((r, ri) => trs.push(new TableRow({ cantSplit: true,
    children: r.map((c, i) => cell(c, { w: cw[i], bg: ri % 2 ? C.zebra : undefined,
      align: (opt.centerCols || []).includes(i) ? AlignmentType.CENTER : AlignmentType.LEFT,
      bold: (opt.boldCols || []).includes(i) })) })));
  return new Table({ rows: trs, columnWidths: cw, width: { size: W, type: WidthType.DXA },
    borders: {
      top: { style: BorderStyle.SINGLE, size: 4, color: C.rule },
      bottom: { style: BorderStyle.SINGLE, size: 4, color: C.rule },
      left: { style: BorderStyle.SINGLE, size: 4, color: C.rule },
      right: { style: BorderStyle.SINGLE, size: 4, color: C.rule },
      insideHorizontal: { style: BorderStyle.SINGLE, size: 2, color: C.rule },
      insideVertical: { style: BorderStyle.SINGLE, size: 2, color: C.rule } } });
}

// nota de rodape de secao
const NOTA = (t) => new Paragraph({
  spacing: { before: 36, after: 96 },
  children: runs(t, { size: 14, color: C.grey, italics: true }) });

const GAP = (n = 120) => new Paragraph({ text: '', spacing: { after: n } });

// v0.199: o bloco de inimigo reusa estes helpers com OUTRA paleta — a do livro,
// que e a que o jogador ve. Trocar a cor por aqui evita a copia do arquivo
// inteiro, que seria a licao no 9 num arquivo de 164 linhas.
function setPaleta(nova) { Object.assign(C, nova); }

module.exports = { d, C, W, SEM_BORDA, NIL, runs, P, FAIXA, campo, LINHA, BLOCO,
                   cell, TBL, NOTA, GAP, setPaleta };

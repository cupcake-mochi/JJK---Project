const d = require('docx');
const { Paragraph, TextRun, Table, TableRow, TableCell, WidthType, ShadingType,
        AlignmentType, HeadingLevel, BorderStyle, VerticalAlign } = d;

// Paleta Neve Saturado (v0.200). Os nomes 'crimson' e 'deep' são históricos (v1–v3
// usavam vinho); mantidos pra não quebrar as referências nos partX.js.
const C = {
  // Neve Saturado, v0.200. Os nomes `crimson` e `deep` sao historicos e ficaram
  // para nao quebrar as referencias — hoje `crimson` e o ACENTO e `deep` e o SELO.
  ink:    '251727',
  crimson:'BC2A6E',
  deep:   '2B1B2E',
  grey:   '847B86',
  rule:   'F8C7DC',
  bandBg: 'F7E5EE',
  headBg: '2B1B2E',
  zebra:  'FADDEA',
  boxBg:  'FDF0F6',
  warnBg: 'FDEFF5',
};
const W = 9000;

// ---- rich text: **bold**  *italic*  `code` ----
function runs(text, base = {}) {
  const out = [];
  const re = /(\*\*[^*]+\*\*|\*[^*]+\*|`[^`]+`)/g;
  let last = 0, m;
  while ((m = re.exec(text)) !== null) {
    if (m.index > last) out.push(new TextRun({ text: text.slice(last, m.index), ...base }));
    const t = m[0];
    if (t.startsWith('**')) out.push(new TextRun({ text: t.slice(2, -2), bold: true, ...base }));
    else if (t.startsWith('`')) out.push(new TextRun({ text: t.slice(1, -1), font: 'Consolas', size: 18, color: C.deep, ...base }));
    else out.push(new TextRun({ text: t.slice(1, -1), italics: true, ...base }));
    last = m.index + t.length;
  }
  if (last < text.length) out.push(new TextRun({ text: text.slice(last), ...base }));
  return out;
}

const P = (text, opt = {}) => new Paragraph({
  children: runs(text, opt.run || {}),
  spacing: { before: opt.before ?? 0, after: opt.after ?? 140, line: 276 },
  alignment: opt.align, indent: opt.indent, border: opt.border, shading: opt.shading,
});

const H1 = (text) => new Paragraph({
  heading: HeadingLevel.HEADING_1, pageBreakBefore: true,
  spacing: { before: 0, after: 260 },
  border: { bottom: { style: BorderStyle.SINGLE, size: 12, color: C.crimson, space: 6 } },
  children: [new TextRun({ text, bold: true, size: 40, color: C.deep, font: 'Georgia' })],
});
const H1nb = (text) => new Paragraph({
  heading: HeadingLevel.HEADING_1,
  spacing: { before: 400, after: 260 },
  border: { bottom: { style: BorderStyle.SINGLE, size: 12, color: C.crimson, space: 6 } },
  children: [new TextRun({ text, bold: true, size: 40, color: C.deep, font: 'Georgia' })],
});
const H2 = (text) => new Paragraph({
  heading: HeadingLevel.HEADING_2, spacing: { before: 340, after: 160 },
  children: [new TextRun({ text, bold: true, size: 28, color: C.crimson, font: 'Georgia' })],
});
const H3 = (text) => new Paragraph({
  heading: HeadingLevel.HEADING_3, spacing: { before: 240, after: 120 },
  children: [new TextRun({ text, bold: true, size: 23, color: C.ink })],
});

const BUL = (text, lvl = 0) => new Paragraph({
  children: runs(text), numbering: { reference: 'bul', level: lvl },
  spacing: { after: 90, line: 268 },
});
const NUM = (text, inst = 0, lvl = 0) => new Paragraph({
  children: runs(text), numbering: { reference: 'num', level: lvl, instance: inst },
  spacing: { after: 90, line: 268 },
});

function cell(text, o = {}) {
  const kids = Array.isArray(text)
    ? text
    : [new Paragraph({
        children: runs(String(text), { size: o.size || 19, color: o.color || C.ink, bold: o.bold }),
        alignment: o.align || AlignmentType.LEFT,
        spacing: { before: 40, after: 40, line: 240 },
      })];
  return new TableCell({
    children: kids, width: { size: o.w, type: WidthType.DXA },
    shading: o.bg ? { type: ShadingType.CLEAR, fill: o.bg, color: 'auto' } : undefined,
    margins: { top: 60, bottom: 60, left: 110, right: 110 },
    verticalAlign: VerticalAlign.CENTER,
    columnSpan: o.span,
  });
}

function TBL(headers, rows, widths, opt = {}) {
  const total = widths.reduce((a, b) => a + b, 0);
  const scale = W / total;
  const cw = widths.map(x => Math.round(x * scale));
  cw[cw.length - 1] = W - cw.slice(0, -1).reduce((a, b) => a + b, 0);
  const trs = [];
  if (headers) trs.push(new TableRow({
    tableHeader: true, cantSplit: true,
    children: headers.map((h, i) => cell(h, {
      w: cw[i], bg: C.headBg, color: 'FFFFFF', bold: true, size: 18,
      align: i === 0 ? AlignmentType.LEFT : (opt.centerHead === false ? AlignmentType.LEFT : AlignmentType.CENTER),
    })),
  }));
  rows.forEach((r, ri) => {
    trs.push(new TableRow({
      cantSplit: true, // v7: linha inteira nunca quebra entre páginas
      children: r.map((c, i) => cell(c, {
        w: cw[i], bg: ri % 2 ? C.zebra : undefined,
        align: (opt.centerCols || []).includes(i) ? AlignmentType.CENTER : AlignmentType.LEFT,
        bold: (opt.boldCols || []).includes(i),
      })),
    }));
  });
  return new Table({
    rows: trs, columnWidths: cw, width: { size: W, type: WidthType.DXA },
    borders: {
      top:    { style: BorderStyle.SINGLE, size: 4, color: C.rule },
      bottom: { style: BorderStyle.SINGLE, size: 4, color: C.rule },
      left:   { style: BorderStyle.SINGLE, size: 4, color: C.rule },
      right:  { style: BorderStyle.SINGLE, size: 4, color: C.rule },
      insideHorizontal: { style: BorderStyle.SINGLE, size: 2, color: C.rule },
      insideVertical:   { style: BorderStyle.SINGLE, size: 2, color: C.rule },
    },
  });
}

// caixa de destaque
function BOX(title, lines, kind = 'info') {
  const bg = kind === 'warn' ? C.warnBg : C.boxBg;
  const bar = kind === 'warn' ? C.crimson : C.deep;
  const kids = [];
  if (title) kids.push(new Paragraph({
    children: [new TextRun({ text: title.toUpperCase(), bold: true, size: 18, color: bar, font: 'Georgia' })],
    spacing: { before: 20, after: 100 },
  }));
  lines.forEach((l, i) => kids.push(new Paragraph({
    children: runs(l, { size: 20 }),
    spacing: { after: i === lines.length - 1 ? 20 : 110, line: 268 },
  })));
  return new Table({
    rows: [new TableRow({
      cantSplit: true, // v7.1: caixa de destaque nunca racha entre paginas
      children: [new TableCell({
        children: kids, width: { size: W, type: WidthType.DXA },
        shading: { type: ShadingType.CLEAR, fill: bg, color: 'auto' },
        margins: { top: 160, bottom: 160, left: 220, right: 220 },
        borders: {
          left:   { style: BorderStyle.SINGLE, size: 18, color: bar },
          top:    { style: BorderStyle.NIL }, bottom: { style: BorderStyle.NIL }, right: { style: BorderStyle.NIL },
        },
      })],
    })],
    columnWidths: [W], width: { size: W, type: WidthType.DXA },
    borders: { top: { style: BorderStyle.NIL }, bottom: { style: BorderStyle.NIL },
               left: { style: BorderStyle.NIL }, right: { style: BorderStyle.NIL },
               insideHorizontal: { style: BorderStyle.NIL }, insideVertical: { style: BorderStyle.NIL } },
  });
}

const GAP = (n = 160) => new Paragraph({ text: '', spacing: { after: n } });
const RULE = () => new Paragraph({
  text: '', spacing: { before: 120, after: 200 },
  border: { bottom: { style: BorderStyle.SINGLE, size: 6, color: C.rule, space: 2 } },
});

module.exports = { d, C, W, P, H1, H1nb, H2, H3, BUL, NUM, TBL, BOX, GAP, RULE, runs, cell };

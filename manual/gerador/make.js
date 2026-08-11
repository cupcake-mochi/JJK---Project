const d = require('docx');
const fs = require('fs');
const { C } = require('./helpers.js');
const A = require('./partA.js'), B = require('./partB.js'), Cc = require('./partC.js'),
      D = require('./partD.js'), E = require('./partE.js'), F = require('./partF.js');
const { Document, Packer, Paragraph, TextRun, Header, Footer, PageNumber, AlignmentType,
        LevelFormat, convertInchesToTwip, BorderStyle } = d;

const doc = new Document({
  creator: 'Mizuki', title: 'Fundamento', description: 'Sistema de criação de feitiços',
  styles: {
    default: {
      document: { run: { font: 'Calibri', size: 21, color: C.ink }, paragraph: { spacing: { line: 276 } } },
    },
  },
  numbering: {
    config: [
      { reference: 'bul', levels: [
        { level: 0, format: LevelFormat.BULLET, text: '•', alignment: AlignmentType.LEFT,
          style: { paragraph: { indent: { left: convertInchesToTwip(0.28), hanging: convertInchesToTwip(0.18) } } } },
        { level: 1, format: LevelFormat.BULLET, text: '◦', alignment: AlignmentType.LEFT,
          style: { paragraph: { indent: { left: convertInchesToTwip(0.56), hanging: convertInchesToTwip(0.18) } } } },
      ]},
      { reference: 'num', levels: [
        { level: 0, format: LevelFormat.DECIMAL, text: '%1.', alignment: AlignmentType.LEFT,
          style: { paragraph: { indent: { left: convertInchesToTwip(0.32), hanging: convertInchesToTwip(0.22) } } } },
      ]},
    ],
  },
  features: { updateFields: true },
  sections: [
    // capa e sumario, sem cabecalho
    { properties: { page: { margin: { top: 1300, bottom: 1200, left: 1300, right: 1300 } } },
      children: [...A.cover, ...A.toc] },
    // miolo — a ordem das secoes do manual v7:
    //   Comecando -> 1 Fundamento -> 2 Montar -> 3 Melhorias -> 4 Restricoes ->
    //   5 Fora de combate -> 6 Liberacao Maxima -> 7 Tecnica Maxima ->
    //   8 Regras de ouro -> 9 Progressao -> 10 Feiticos prontos -> 11 Mestre -> Apendice
    { properties: {
        page: { margin: { top: 1300, bottom: 1200, left: 1300, right: 1300 },
                pageNumbers: { start: 1 } } },
      headers: { default: new Header({ children: [new Paragraph({
        alignment: AlignmentType.RIGHT,
        border: { bottom: { style: BorderStyle.SINGLE, size: 4, color: C.rule, space: 6 } },
        children: [new TextRun({ text: 'FUNDAMENTO', size: 15, color: C.grey, characterSpacing: 40 })],
      })] }) },
      footers: { default: new Footer({ children: [new Paragraph({
        alignment: AlignmentType.CENTER,
        children: [new TextRun({ children: [PageNumber.CURRENT], size: 17, color: C.grey })],
      })] }) },
      children: [
        ...A.inicio, ...A.numeros,
        ...B.fundamento, ...B.passivas, ...B.exemplosFund,
        ...Cc.montar,
        ...D.melhorias, ...D.restricoes,
        ...E.foraDeCombate, ...E.liberacao, ...E.maxima, ...E.ouro, ...E.progressao,
        ...F.pacotes, ...F.mestre, ...F.apendice,
      ] },
  ],
});

Packer.toBuffer(doc).then(buf => {
  const out = 'Fundamento-MANUAL-v7.docx';
  fs.writeFileSync(out, buf);
  console.log('gerado:', out, (buf.length/1024).toFixed(0) + ' KB');
});

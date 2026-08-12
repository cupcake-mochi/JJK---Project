// Gera as duas fichas: a em branco e a preenchida.
//   node make.js
// Sai ficha-em-branco.docx e ficha-exemplo-kaori.docx, que sao copiados
// para 05-material/. O layout e' UM so' — o que muda e' o objeto que entra.
const d = require('docx');
const fs = require('fs');
const { C } = require('./helpers.js');
const { pagina1, pagina2, pagina3 } = require('./ficha.js');
const { Document, Packer, Paragraph, TextRun, Footer, AlignmentType } = d;

// ---------------------------------------------------------------------------
// A KAORI, da peca 8. Todo valor aqui esta escrito la — nada foi inventado.
// Os feiticos ficam EM BRANCO de proposito: a peca 8 nao lista os dela, e
// invental-os aqui seria escolha de sabor, que e do Mizuki e nao minha.
// ---------------------------------------------------------------------------
const KAORI = {
  nome: 'Kaori', jogador: '', grau: 'Grau 4', nivel: '2', xp: '0',
  caminho: 'Bastião', trilha: 'Muro', origem: 'Descendente',
  atributos: { 'Força': '3', 'Destreza': '2', 'Constituição': '2',
               'Inteligência': '1', 'Essência': '1' },
  numeros: { vida: '23', pe: '8', defesa: '13', iniciativa: 'd20 + 2',
             cac: 'd20 + 3', distancia: 'd20 + 2' },
  trs: ['Físico', 'Vigor'],
  pericias: ['Atletismo', 'Intimidação', 'Sentir Energia', 'Percepção',
             'Sobrevivência', 'Intuição', 'Hierarquia', 'História'],
  oficios: ['Forja', 'Caligrafia', 'Herbalismo'],
  tecnica: {
    regra: 'Tudo que eu prendo entre as minhas mãos fica mais pesado.',
    descricao: '',
    livres: ['Controle', 'Castigo'],
    fechadas: ['Amparo', 'Área', 'Auxiliares'],
    selo: 'As duas mãos precisam se tocar antes.',
    passiva: 'Ela sabe o peso exato de qualquer coisa que encoste nela.',
    classe0: [], feiticos: [],
  },
  lore: {
    aparencia: '', historia: '',
    traco: 'O ramo do clã que perdeu o nome — e ela é dele.',
    legado: 'O Sobrenome — ela consegue audiência em qualquer lugar do meio jujutsu. Ser bem recebida é outra história.',
    legado2: 'Biblioteca — uma vez por cena, refaz um teste de História ou Ocultismo. A casa tinha os livros, e ela foi obrigada a ler.',
    lacos: '', instituicao: '', pacto: '', notas: '',
  },
};

function montar(f, arquivo, rodape) {
  const doc = new Document({
    creator: 'Mizuki', title: 'RPG da Guilda — ficha de personagem',
    description: 'Ficha de nível 2',
    styles: { default: { document: {
      run: { font: 'Calibri', size: 20, color: C.ink },
      paragraph: { spacing: { line: 250 } } } } },
    sections: [1, 2, 3].map(n => ({
      properties: { page: { margin: { top: 680, bottom: 560, left: 780, right: 780 } } },
      footers: { default: new Footer({ children: [new Paragraph({
        alignment: AlignmentType.CENTER,
        children: [new TextRun({ text: rodape + '  ·  ' + n + ' de 3',
                                 size: 14, color: C.grey })] })] }) },
      children: [pagina1, pagina2, pagina3][n - 1](f),
    })),
  });
  return Packer.toBuffer(doc).then(buf => {
    fs.writeFileSync(arquivo, buf);
    console.log('gerado:', arquivo, (buf.length / 1024).toFixed(0) + ' KB');
  });
}

montar(null, 'ficha-em-branco.docx', 'RPG da Guilda · ficha de nível 2')
  .then(() => montar(KAORI, 'ficha-exemplo-kaori.docx',
                     'RPG da Guilda · exemplo preenchido: a Kaori, da peça 8'));

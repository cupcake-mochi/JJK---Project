// Os catalogos e as constantes do BLOCO DE INIMIGO.
//
// NENHUM valor daqui e autoridade. A autoridade e a peca 26 e a tabela
// `Inimigos` do manual, e o conferir-ficha.py compara os dois. Mexeu na peca?
// Mexa aqui e rode o validador.
//
// A tabela do manual publica UMA linha por faixa de Classe, e a faixa e' quem
// manda: a linha do nivel 2 vale do 2 ao 4, a do 5 vale ate o 8, e assim por
// diante. A peca 26 §4 e a dona dessa leitura.
const FAIXAS = [
  // rotulo, de, ate, Classe, grupo/rodada, chefe vida, chefe dano, capanga vida, capanga dano
  ['2 a 4',   2,  4, 1,  38,  138, 6,  null, null],
  ['5 a 8',   5,  8, 2,  90,  330, 15, 40,   8],
  ['9 a 12',  9, 12, 3, 130,  475, 26, 70,   14],
  ['13 a 16',13, 16, 4, 180,  660, 38, 110,  20],
  ['17 a 20',17, 20, 5, 220,  805, 49, 150,  26],
  ['21 a 25',21, 25, 6, 275, 1005, 61, 190,  32],
  ['26 a 30',26, 30, 7, 315, 1155, 72, 220,  38],
];

// As quatro categorias da peca 26 §4. O fator e' personagens/4, e as acoes sao
// personagens menos um com piso 1 — as duas coisas derivam e nao sao escolha.
const CATEGORIAS = [
  ['Ronda',      1, 0.25],
  ['Dupla',      2, 0.50],
  ['Alcateia',   4, 1.00],
  ['Calamidade', 6, 1.50],
];

// Defesa, acerto, CD e refino mudam em MARCO (6, 10, 14, 18, 22, 26) e nao em
// faixa de Classe. As duas escadas nao coincidem, e e por isso que sao duas
// tabelas no bloco em vez de uma. Peca 1 §5 e peca 11 §3.
const DERIVADAS = [
  // rotulo, Defesa, acerto, CD, refino
  ['2 a 5',   14,  4, 12, 1],
  ['6 a 9',   15,  4, 12, 3],
  ['10 a 13', 16,  6, 14, 4],
  ['14 a 17', 17,  6, 14, 6],
  ['18 a 21', 18,  8, 16, 7],
  ['22 a 25', 19,  8, 16, 9],
  ['26 a 30', 20, 10, 18, 10],
];

// A regua de resistencia da peca 26 §6.3, que sai dos pesos da peca 19 §4.
// ⚠ os multiplicadores continuam aqui porque a checagem 8 do conferir-bestiario
// recalcula eles dos pesos da peca 19; o que a FOLHA imprime sao so as duas
// ultimas colunas, o custo em degrau. Multiplicador e derivacao, e a
// REGRA-DE-VOZ manda derivacao pra peca.
const RESISTENCIA = [
  //  grupo        peso   resist.  imunid.  vulner.  resistir custa           ser imune custa
  ['Físicos',    '60%', '1,43×', '2,50×', '0,62×', 'um degrau de categoria', 'mais de um degrau'],
  ['Elementais', '30%', '1,18×', '1,43×', '0,77×', 'meio degrau',            'um degrau'],
  ['Especiais',  '10%', '1,05×', '1,11×', '0,91×', 'nada',                   'nada'],
  ['um tipo só', '20%', '1,11×', '1,25×', '0,83×', 'nada',                   'meio degrau'],
];

// A sub-categoria da peca 26 §4.5: a categoria diz o tamanho e esta diz a forma.
// A fracao sai do CAMBIO — cada capanga vale 1/N de um chefe —, entao ela nao e
// escolha: e 1 menos capangas/N.
const SUBCATEGORIAS = [
  ['sozinho',      0], ['com um apoio', 1], ['com dois', 2], ['bando', 3],
];

const CAMBIO = 4;          // um chefe de Alcateia vale N capangas — peca 26 §5
const REACAO = 1;          // uma por rodada — manual, secao Inimigos

module.exports = { FAIXAS, CATEGORIAS, DERIVADAS, RESISTENCIA, SUBCATEGORIAS,
                   CAMBIO, REACAO };

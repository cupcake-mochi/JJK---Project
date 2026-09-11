// Os catalogos e as constantes do BLOCO DE INIMIGO.
//
// NENHUM valor daqui e autoridade. A autoridade e a peca 26 e a tabela
// `Inimigos` do manual, e o bloco 7 do conferir-ficha.py compara os dois. Mexeu
// na peca? Mexa aqui e rode o validador.
//
// A tabela do manual publica UMA linha por faixa de Classe, e a faixa e' quem
// manda: a linha do nivel 2 vale do 2 ao 4, a do 5 vale ate o 8, e assim por
// diante. A peca 26 §4 e a dona dessa leitura.
//
// v0.221: a coluna do capanga passou a ser a do Capanga da ESCADA — a vida e o
// dano do grupo por rodada dividido por quatro, para baixo, e o dano e um quarto
// do dano do chefe. Ate a v0.220 ela era o capanga da Alcateia (chefe ÷ 4, ÷ 3),
// que morreu com a escada. O manual e a peca 26 §5 sao os donos.
const FAIXAS = [
  // rotulo, de, ate, Classe, grupo/rodada, chefe vida, chefe dano, capanga vida, capanga dano
  ['2 a 4',  2,  4, 1,   38,  114,   17,   9,   4],
  ['5 a 8',  5,  8, 2,   90,  270,   39,  22,  10],
  ['9 a 12',  9, 12, 3,  130,  390,   75,  32,  19],
  ['13 a 16', 13, 16, 4,  180,  540,  111,  45,  28],
  ['17 a 20', 17, 20, 5,  220,  660,  147,  55,  37],
  ['21 a 25', 21, 25, 6,  275,  825,  183,  68,  46],
  ['26 a 30', 26, 30, 7,  315,  945,  219,  78,  55],
];

// As cinco categorias da escada viva, peca 26 §4. As acoes sao DECLARADAS — ate
// a v0.220 elas saiam de "personagens menos um", e foi isso que quebrou a Dupla.
// O Capanga nao tem numero de personagens: a vida dele sai do dano do grupo.
// [nome, personagens, fator, acoes, carrega Intervencao]
const CATEGORIAS = [
  ['Capanga',    null, 0.25, 1, false],
  ['Ameaça',        1, 0.25, 1, false],
  ['Desastre',      4, 1.00, 3, true],
  ['Catástrofe',    6, 1.50, 5, true],
  ['Calamidade',    8, 2.00, 6, true],
];

// Quem carrega Intervencao paga no dano: a Intervencao e acao EXTRA, e o fator
// de dano dele e multiplicado por este numero. Peca 26 §6.5 e a dona.
const FATOR_INTERVENCAO = 0.923;
const INTERVENCOES = 3;          // por luta, de Desastre para cima — peca 26 §6.5

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

// A regua de resistencia da peca 26 §6.3, que sai dos pesos da peca 19 §4. Desde
// a v0.221 a moeda e o FATOR: resistir e ser imune multiplicam o fator da
// categoria, e a vulnerabilidade nao cobra nem devolve. O que a folha imprime sao
// as duas colunas do meio.
const RESISTENCIA = [
  //  grupo        peso   resistir  ser imune  vida efetiva com vulnerabilidade
  ['Físicos',    '60%', '1,43×', '2,50×', '0,62×'],
  ['Elementais', '30%', '1,18×', '1,43×', '0,77×'],
  ['Especiais',  '10%', '1,05×', '1,11×', '0,91×'],
  ['um tipo só', '20%', '1,11×', '1,25×', '0,83×'],
];

// A sub-categoria da peca 26 §4.5: a categoria diz o tamanho e esta diz a forma.
// Desde a v0.221 a fracao do chefe e MEDIDA, e nao sai do cambio: o projeto do
// Bestiario varreu 201 fracoes em 29 niveis atras da que devolve o que o chefe
// sozinho cobra. Com uma casa decimal, porque meio ponto atravessa uma rodada.
// [nome, capangas, o chefe fica com (%), cobra da vida do grupo (%)]
const SUBCATEGORIAS = [
  ['sozinho', 0, 100.0, 67.6], ['com um apoio', 1, 91.5, 67.5],
  ['com dois', 2, 83.0, 67.4], ['bando', 3, 74.5, 67.3],
];

// O tamanho, peca 26 §3.3: o alcance e o lado da grade vezes 1,5 m, e do Grande
// para cima o golpe pega metade num vizinho. Ele nao cobra nada.
// [nome, lado na grade, metade num vizinho]
const TAMANHOS = [
  ['Minúsculo', 1, false], ['Pequeno', 1, false], ['Médio', 1, false],
  ['Grande', 2, true], ['Imenso', 3, true], ['Colossal', 4, true],
];

// A area natural do inimigo, peca 26 §6.5: a cobertura sai do nivel, e a forma e
// o jeito de gastar ela. [de, ate, cobre em quadrados, raio, cone, retangulos]
const AREA_NATURAL = [
  [ 2,  8,  13, '3 m',   '7,5 m',  ['4×3', '6×2', '7×2', '12×1']],
  [ 9, 16,  28, '4,5 m', '10,5 m', ['6×5', '7×4', '9×3', '13×2']],
  [17, 24,  50, '6 m',   '15 m',   ['7×7', '8×6', '9×5', '10×5']],
  [25, 30, 113, '9 m',   '22,5 m', ['11×11', '11×10', '12×9']],
];

// As seis prontas, na escada viva — v0.221. Aqui moram SO as escolhas: nome,
// faixa, categoria, atributos, tamanho e o TEXTO do bloco. Vida, dano, acoes,
// golpe, acerto e CD sao COMPUTADOS pelo make.js a partir de FAIXAS, CATEGORIAS
// e DERIVADAS; onde o texto precisa de numero ele traz um marcador — {acerto},
// {golpe}, {cd}, {alcance}, {vizinho}, {esfera}, {cone}, {retangulo},
// {deslocamento}, {tecnica_dano}, {tecnica_alcance} — que o make.js enche.
//
// O texto veio do livro do Bestiario (capitulo 8, no molde de bloco do 5e), e as
// cinco escolhas que ele pedia foram marteladas pelo Mizuki em 11/09/2026.
// O mapa de faixa e categoria e o do `DECIDIDO-as-seis-prontas.md` do Bestiario:
// Betobeto, Kamaitachi (duas na mesa), Hitotsume e Kitsune sao Ameaca; Tsuchigumo
// e Oni sao Desastre. A Kitsune subiu para 9 a 12 para poder conjurar.
//
// Sao seis porque sao seis: a derivacao antiga (duas faixas vezes as quatro
// categorias, menos a Calamidade) morreu com a escada. A coluna do Capanga fica
// vazia, e isso e o preco declarado da decisao de 10/09 — ficha de esquadrao e
// ficcao do Mizuki. A ficcao sai do folclore japones, escolha dele: maldicao de
// grau baixo e yokai com outro nome.
const PRONTAS = [
  { nome: 'Betobeto', faixa: '2 a 4', categoria: 'Ameaça',
    arranjo: '0 · 3 · 1 · 2 · 3', trs: 'Físico (Destreza) e Espírito',
    tamanho: "Médio", corpos_na_mesa: 1, movimentos: [],
    linha: "Maldição que segue as pessoas no escuro e só se deixa ouvir pelos passos.",
    notas: "No folclore japonês, o Betobeto é um som de passos que acompanha quem anda sozinho à noite, e quem sai do caminho e pede que ele passe na frente fica em paz. Como maldição, ele aparece em corredores, ruas estreitas e escadas sem luz, e ataca quem corre ou se vira para enfrentá-lo. Na luta, bate sempre em quem ele vinha seguindo.",
    tracos: [{"nome": "Passos no Escuro", "texto": "Fora da luta, o Betobeto não pode ser visto. Só se ouvem os passos dele, sempre atrás de quem ele segue, e eles param quando essa pessoa para. Ele fica visível quando a luta começa."}],
    acoes_multiplas: null,
    acoes_nomeadas: [{"nome": "Pisada", "texto": "*Ataque corpo a corpo:* {acerto} para acertar, alcance {alcance}, uma criatura. *Acerto:* {golpe} de dano de Concussão{vizinho}."}],
    intervencoes: [] },
  { nome: 'Kamaitachi', faixa: '2 a 4', categoria: 'Ameaça',
    arranjo: '3 · 3 · 2 · 1 · 0', trs: 'Físico (Destreza) e Vigor',
    tamanho: "Pequeno", corpos_na_mesa: 2, movimentos: [],
    linha: "Par de maldições em forma de doninha, com garras de foice, que chegam montadas no vento.",
    notas: "No folclore japonês, a kamaitachi é um trio de doninhas que corre dentro de um redemoinho: a primeira derruba a pessoa, a segunda corta, e a terceira passa um remédio que fecha o corte antes de doer. Como maldição, elas andam em par e sem o remédio, em campo aberto, pátio e rua onde o vento corre. Na luta, as duas atacam o mesmo alvo, e quando uma cai a outra foge.",
    tracos: [{"nome": "Par", "texto": "As Kamaitachi aparecem sempre em dupla. Ponha duas na mesa: cada uma é uma criatura com este bloco inteiro."}],
    acoes_multiplas: null,
    acoes_nomeadas: [{"nome": "Foice", "texto": "*Ataque corpo a corpo:* {acerto} para acertar, alcance {alcance}, uma criatura. *Acerto:* {golpe} de dano Cortante{vizinho}."}],
    intervencoes: [] },
  { nome: 'Tsuchigumo', faixa: '2 a 4', categoria: 'Desastre',
    arranjo: '3 · 2 · 3 · 1 · 0', trs: 'Físico (Força) e Vigor',
    tamanho: "Grande", corpos_na_mesa: 1, movimentos: ["Escalada"],
    linha: "Aranha gigante que faz ninho em prédios fechados e ataca do teto e das paredes.",
    notas: "No folclore japonês, a Tsuchigumo é a aranha gigante que o guerreiro Minamoto no Raikō matou. Como maldição, ela ocupa prédio abandonado, túnel e porão, e passa a luta presa às paredes e ao teto. Abre com Varrida das Patas quando o grupo entra junto, cobre de Teia a passagem por onde o grupo veio e usa Subir quando fica cercada.",
    tracos: [{"nome": "Escalada de Aranha", "texto": "A Tsuchigumo anda por parede e teto, de cabeça para baixo inclusive, sem fazer teste."}, {"nome": "Andar na Teia", "texto": "A teia dela não é terreno difícil para a Tsuchigumo."}],
    acoes_multiplas: "A Tsuchigumo faz três ataques de Mordida, ou usa Varrida das Patas e faz dois ataques de Mordida.",
    acoes_nomeadas: [{"nome": "Mordida", "texto": "*Ataque corpo a corpo:* {acerto} para acertar, alcance {alcance}, uma criatura. *Acerto:* {golpe} de dano Perfurante{vizinho}."}, {"nome": "Varrida das Patas", "texto": "*Teste de Resistência Físico:* CD {cd}, cada criatura num `Cone` de {cone} a partir dela. *Falha:* {golpe} de dano Cortante. *Sucesso:* metade do dano."}],
    intervencoes: [{"nome": "Mordida", "texto": "A Tsuchigumo faz um ataque de Mordida. Esse ataque não pega o vizinho."}, {"nome": "Teia", "texto": "A Tsuchigumo cobre de teia um `Retângulo` de {retangulo} que encoste nela. A área é terreno difícil até o fim da luta."}, {"nome": "Subir", "texto": "A Tsuchigumo escala até {deslocamento} pela parede ou pelo teto. Esse movimento não provoca ataque de oportunidade."}] },
  { nome: 'Hitotsume', faixa: '5 a 8', categoria: 'Ameaça',
    arranjo: '0 · 2 · 2 · 2 · 3', trs: 'Espírito e Intelecto',
    tamanho: "Médio", corpos_na_mesa: 1, movimentos: [],
    linha: "Maldição com a forma de um menino de um olho só, que aparece parado e cada vez mais perto.",
    notas: "No folclore japonês, o hitotsume-kozō é um menino careca de um olho só que surge no caminho, mostra uma língua comprida e some. Como maldição, ele aparece em escola, hospital e casa antiga: na esquina do corredor, na porta do banheiro, no fim da escada, sempre sozinho. Na luta, ataca quem estiver mais longe do resto do grupo.",
    tracos: [{"nome": "Mais Perto", "texto": "Fora da luta, o Hitotsume só se move quando ninguém está olhando para ele."}],
    acoes_multiplas: null,
    acoes_nomeadas: [{"nome": "Língua", "texto": "*Ataque corpo a corpo:* {acerto} para acertar, alcance {alcance}, uma criatura. *Acerto:* {golpe} de dano de Concussão{vizinho}."}],
    intervencoes: [] },
  { nome: 'Kitsune', faixa: '9 a 12', categoria: 'Ameaça',
    arranjo: '0 · 2 · 1 · 3 · 3', trs: 'Espírito e Intelecto',
    tamanho: "Médio", corpos_na_mesa: 1, movimentos: [],
    linha: "Maldição em forma de raposa que toma a aparência de gente e ataca com fogo à distância.",
    notas: "No folclore japonês, a kitsune é a raposa que aprende a tomar forma humana e acende o kitsunebi, o fogo-de-raposa. Como maldição, ela vive entre pessoas, com rosto humano, em estação, hospital e rua de comércio. Fala com o grupo antes de lutar e tenta separá-lo; na luta, fica longe, usa Fogo-de-Raposa e só morde quem chega ao lado dela.",
    tracos: [{"nome": "Forma Humana", "texto": "Com uma ação, a Kitsune toma a aparência de uma pessoa que ela já viu, ou volta à forma de raposa. Nenhum número do bloco muda."}],
    acoes_multiplas: null,
    acoes_nomeadas: [{"nome": "Mordida", "texto": "*Ataque corpo a corpo:* {acerto} para acertar, alcance {alcance}, uma criatura. *Acerto:* {golpe} de dano Perfurante{vizinho}."}, {"nome": "Fogo-de-Raposa", "texto": "*Ataque de conjuração à distância:* {acerto} para acertar, alcance {tecnica_alcance}, uma criatura. *Acerto:* {tecnica_dano} de dano de Fogo."}],
    intervencoes: [] },
  { nome: 'Oni', faixa: '5 a 8', categoria: 'Desastre',
    arranjo: '3 · 1 · 3 · 1 · 1', trs: 'Físico (Força) e Vigor',
    tamanho: "Grande", corpos_na_mesa: 1, movimentos: [],
    linha: "Maldição de corpo enorme, com chifres e um porrete de ferro, que luta de frente.",
    notas: "No folclore japonês, o oni tem chifres, pele vermelha ou azul, e carrega um kanabō, um porrete de ferro cravejado. Como maldição, ele fica no fim do caminho: no último andar, no fundo do terreno, na sala que o grupo precisa atravessar. Avança sobre quem está mais perto, usa Pancada no Chão quando o grupo o cerca e guarda Arremesso para tirar do lugar quem cuida dos outros.",
    tracos: [{"nome": "Faro", "texto": "O Oni sente cheiro de sangue. Ele sabe onde está cada criatura que perdeu vida nesta luta, se ela estiver no mesmo cômodo que ele, mesmo sem vê-la."}],
    acoes_multiplas: "O Oni faz três ataques de Kanabō, ou usa Pancada no Chão e faz dois ataques de Kanabō.",
    acoes_nomeadas: [{"nome": "Kanabō", "texto": "*Ataque corpo a corpo:* {acerto} para acertar, alcance {alcance}, uma criatura. *Acerto:* {golpe} de dano de Concussão{vizinho}."}, {"nome": "Pancada no Chão", "texto": "*Teste de Resistência Físico:* CD {cd}, cada criatura numa `Esfera` de {esfera} a partir do corpo dele. *Falha:* {golpe} de dano de Concussão. *Sucesso:* metade do dano."}],
    intervencoes: [{"nome": "Kanabō", "texto": "O Oni faz um ataque de Kanabō. Esse ataque não pega o vizinho."}, {"nome": "Arremesso", "texto": "*Teste de Resistência Físico:* CD {cd}, uma criatura a até {alcance} dele. *Falha:* o alvo é jogado num espaço livre a até {deslocamento} do Oni e fica `Derrubado`. O arremesso não causa dano."}, {"nome": "Parede Abaixo", "texto": "O Oni derruba uma parede, pilar ou divisória a até {alcance} dele. Ela para de dar cobertura, e os quadrados onde ela estava viram terreno difícil até o fim da luta."}] },
];

// Quatro Ameaca nao valem um Desastre — peca 26 §4.3, nas sete faixas.
const AMEACA_CONTRA_DESASTRE = [0.75, 0.77];

const CAMBIO = 8;               // um Desastre vale N capangas — peca 26 §5
const TETO_EMPILHAMENTO = 3;    // corpos do mesmo esquadrao no mesmo alvo — peca 26 §5
const REACAO = 1;               // uma por rodada — manual, secao Inimigos
const DESLOCAMENTO = '9 m';     // peca 3 §3, a linha da ficha da peca 26 §3
const ALCANCE_PROJETIL = '18 m'; // o Projetil nas Classes 1 a 5 — manual, partC.js

module.exports = { FAIXAS, CATEGORIAS, FATOR_INTERVENCAO, INTERVENCOES, DERIVADAS, RESISTENCIA,
                   SUBCATEGORIAS, TAMANHOS, AREA_NATURAL, PRONTAS, AMEACA_CONTRA_DESASTRE,
                   CAMBIO, TETO_EMPILHAMENTO, REACAO, DESLOCAMENTO, ALCANCE_PROJETIL };

// Os catalogos e as constantes do BLOCO DE INIMIGO.
//
// NENHUM valor daqui e autoridade. A autoridade e a peca 26, que desde a v0.338 e'
// tambem a dona da tabela `Inimigos` (§3.0; ate la' ela morava no manual do Fundamento
// v7, hoje no arquivo). O bloco 7 do conferir-ficha.py compara os dois. Mexeu na peca?
// Mexa aqui e rode o validador.
//
// A tabela `Inimigos` publica UMA linha por faixa de Classe, e a faixa e' quem
// manda: a linha do nivel 2 vale do 2 ao 4, a do 5 vale ate o 8, e assim por
// diante. A peca 26 §4 e a dona dessa leitura.
//
// v0.282: a coluna do capanga e a do Capanga da GRADE — a vida e o dano do grupo por
// rodada dividido por quatro, para baixo, e o golpe e METADE de um quarto do dano do
// chefe (o esquadrao de 2N corpos com meio golpe, peca 26 §5). A vida do chefe e o
// dano dele nao mudaram: a linha da tabela `Inimigos` e o Desastre x4 da grade.
const FAIXAS = [
  // rotulo, de, ate, Classe, grupo/rodada, chefe vida, chefe dano, capanga vida, capanga dano
  ['2 a 4',  2,  4, 1,   38,  114, 18,   9, 2],
  ['5 a 8',  5,  8, 2,   90,  270, 40,  22, 5],
  ['9 a 12',  9, 12, 3,  130,  390, 77,  32, 10],
  ['13 a 16', 13, 16, 4,  180,  540, 114,  45, 14],
  ['17 a 20', 17, 20, 5,  220,  660, 151,  55, 19],
  ['21 a 25', 21, 25, 6,  275,  825, 189,  68, 24],
  ['26 a 30', 26, 30, 7,  315,  945, 226,  78, 28],
];

// Os cinco degraus da grade, peca 26 §4 (v0.282). A categoria e a DIFICULDADE da luta,
// e a ficha e feita para N pessoas do nivel, de x1 a x6. A vida e rodadas x N x a saida
// de um personagem; o golpe e a pressao x o golpe-base, e a pressao e o orcamento do
// Pathfinder 2e x as rodadas do Desastre ÷ as rodadas do degrau; ele age N vezes.
// [nome, rodadas, orcamento]
const DEGRAUS = [
  ['Capanga',    2,   0.50],
  ['Ameaça',     2.5, 0.75],
  ['Desastre',   3,   1.00],
  ['Catástrofe', 4,   1.50],
  ['Calamidade', 5,   2.00],
];
const N_MAXIMO = 6;              // de x1 a x6 — o teto de seis e do Mizuki, 08/09/2026

// Os seis papeis da peca 26 §3.4. O papel e GERADOR DE BASE: o que ele ganha num
// eixo ele paga no outro, e o produto fecha em 1,000 — ele nao muda o tamanho do
// encontro, muda a forma dele. NENHUM valor aqui e autoridade: a peca 26 §3.4 e a
// dona, e a checagem 7c do conferir-ficha.py compara as duas tabelas.
//
// Os dois primeiros tem fator fixo (a troca do §3.2 com nome). O `Artilheiro` sai do
// degrau (a meia rodada de aproximacao ÷ as rodadas), e os tres de acao saem do N,
// porque o preco deles e UMA acao e o inimigo tem N. O `Capanga` le 2N acoes.
//
// [nome, vida x (fixo, ou null), Defesa +/-, de onde sai o fator variavel]
const PAPEIS = [
  ['Brutamontes', 1.200, -2, null],
  ['Baluarte',    0.800, +2, null],
  ['Artilheiro',   null,  0, 'alcance'],
  ['Emboscador',   null,  0, 'vantagem'],
  ['Controlador',  null,  0, 'acao'],
  ['Reforço',      null,  0, 'acao'],
];

// A vantagem multiplica o dano de UM ataque por isto. Sai de duas regras com dono:
// a peca 19 §2.2 da +25 pontos percentuais, e o inimigo acerta o meio da banda de
// 50% a 55% que a peca 26 §3.1 publica — 77,5 / 52,5.
const MULT_VANTAGEM = 1.476;

// O que o `Artilheiro` poupa: meia rodada, a de quem se aproxima — peca 26 §3.4.
const GANHO_ALCANCE = 0.5;

// O esquadrao do `Capanga`: dois corpos por pessoa, cada um cai num golpe — peca 26 §5.
const CORPOS_POR_PESSOA = 2;

// Quantos dos seis o `Capanga` aceita: os que nao mexem na Defesa dele. A vida do
// corpo e o que um personagem derruba num golpe (peca 26 §5).
const PAPEIS_FORA_DO_CAPANGA = ['Brutamontes', 'Baluarte'];

// A `Intervencao`, peca 26 §6.5: tres por luta, e a porta abre quando N x orcamento
// >= 4. Ela e acao EXTRA — 0,75 de acao por luta — e se paga na vida.
const INTERVENCOES = 3;
const PORTA_INTERVENCAO = 4;
const INTERVENCAO_EXTRA = 0.75;

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
// a v0.282 ela se paga na vida: resistir e ser imune DIVIDEM a vida crua, e a
// vulnerabilidade nao cobra nem devolve. O que a folha imprime sao as duas do meio.
const RESISTENCIA = [
  //  grupo        peso   resistir  ser imune  vida efetiva com vulnerabilidade
  ['Físicos',    '60%', '1,43×', '2,50×', '0,62×'],
  ['Elementais', '30%', '1,18×', '1,43×', '0,77×'],
  ['Especiais',  '10%', '1,05×', '1,11×', '0,91×'],
  ['um tipo só', '20%', '1,00×', '1,25×', '0,83×'],
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

// As seis prontas — v0.221, na grade desde a v0.282. Aqui moram SO as escolhas: nome,
// faixa, categoria, N, atributos, tamanho e o TEXTO do bloco. Vida, dano, acoes,
// golpe, acerto e CD sao COMPUTADOS pelo make.js a partir de FAIXAS, CATEGORIAS
// e DERIVADAS; onde o texto precisa de numero ele traz um marcador — {acerto},
// {golpe}, {cd}, {alcance}, {vizinho}, {esfera}, {cone}, {retangulo},
// {deslocamento}, {tecnica_dano}, {tecnica_alcance} — que o make.js enche.
//
// O texto veio do livro do Bestiario (capitulo 8, no molde de bloco do 5e), e as
// cinco escolhas que ele pedia foram marteladas pelo Mizuki em 11/09/2026.
// O mapa de faixa e categoria e o do `DECIDIDO-as-seis-prontas.md` do Bestiario, levado
// para a grade na v0.282: Betobeto, Kamaitachi (duas na mesa), Hitotsume e Kitsune sao
// `Ameaça x1` — a luta facil para uma pessoa —; Tsuchigumo e Oni sao `Desastre x4`, o
// chefe da linha da tabela `Inimigos`. A Kitsune subiu para 9 a 12 para poder conjurar.
//
// Sao seis porque sao seis: a derivacao antiga (duas faixas vezes as quatro
// categorias, menos a Calamidade) morreu com a escada. A coluna do Capanga fica
// vazia, e isso e o preco declarado da decisao de 10/09 — ficha de esquadrao e
// ficcao do Mizuki. A ficcao sai do folclore japones, escolha dele: maldicao de
// grau baixo e yokai com outro nome.
// v0.235: `ataque` e o atributo que o acerto e a CD leem (peca 26 §3.2), e `marcos` diz, nivel a
// nivel, para onde vai cada ponto de marco — uma lista por marco. A soma e a do §3.2, e a 9.5 do
// conferir-bestiario.py confere.
const PRONTAS = [
  { nome: 'Betobeto', faixa: '2 a 4', categoria: 'Ameaça', n: 1, papel: 'Emboscador',
    arranjo: '0 · 3 · 1 · 2 · 3', ataque: 'Essência', trs: 'Físico (Destreza) e Espírito',
    tamanho: "Médio", corpos_na_mesa: 1, movimentos: [],
    linha: "Maldição que segue as pessoas no escuro e só se deixa ouvir pelos passos.",
    notas: "No folclore japonês, o Betobeto é um som de passos que acompanha quem anda sozinho à noite, e quem sai do caminho e pede que ele passe na frente fica em paz. Como maldição, ele aparece em corredores, ruas estreitas e escadas sem luz, e ataca quem corre ou se vira para enfrentá-lo. Na luta, bate sempre em quem ele vinha seguindo.",
    tracos: [{"nome": "Passos no Escuro", "texto": "Fora da luta, o Betobeto não pode ser visto. Só se ouvem os passos dele, sempre atrás de quem ele segue, e eles param quando essa pessoa para. Ele fica visível quando a luta começa."}],
    acoes_multiplas: null,
    acoes_nomeadas: [{"nome": "Pisada", "texto": "*Ataque corpo a corpo:* {acerto} para acertar, alcance {alcance}, uma criatura. *Acerto:* {golpe} de dano de Concussão{vizinho}."}],
    intervencoes: [] },
  { nome: 'Kamaitachi', faixa: '2 a 4', categoria: 'Ameaça', n: 1, papel: 'Emboscador',
    arranjo: '3 · 3 · 2 · 1 · 0', ataque: 'Destreza', trs: 'Físico (Destreza) e Vigor',
    tamanho: "Pequeno", corpos_na_mesa: 2, movimentos: [],
    linha: "Par de maldições em forma de doninha, com garras de foice, que chegam montadas no vento.",
    notas: "No folclore japonês, a kamaitachi é um trio de doninhas que corre dentro de um redemoinho: a primeira derruba a pessoa, a segunda corta, e a terceira passa um remédio que fecha o corte antes de doer. Como maldição, elas andam em par e sem o remédio, em campo aberto, pátio e rua onde o vento corre. Na luta, as duas atacam o mesmo alvo, e quando uma cai a outra foge.",
    tracos: [{"nome": "Par", "texto": "As Kamaitachi aparecem sempre em dupla. Ponha duas na mesa: cada uma é uma criatura com este bloco inteiro."}],
    acoes_multiplas: null,
    acoes_nomeadas: [{"nome": "Foice", "texto": "*Ataque corpo a corpo:* {acerto} para acertar, alcance {alcance}, uma criatura. *Acerto:* {golpe} de dano Cortante{vizinho}."}],
    intervencoes: [] },
  { nome: 'Tsuchigumo', faixa: '2 a 4', categoria: 'Desastre', n: 4, papel: 'Controlador',
    arranjo: '3 · 3 · 3 · 1 · 0', ataque: 'Força', trs: 'Físico (Força) e Vigor',   // v0.234: o ponto de chefe na Destreza, que a Defesa pedia
    tamanho: "Grande", corpos_na_mesa: 1, movimentos: ["Escalada"],
    linha: "Aranha gigante que faz ninho em prédios fechados e ataca do teto e das paredes.",
    notas: "No folclore japonês, a Tsuchigumo é a aranha gigante que o guerreiro Minamoto no Raikō matou. Como maldição, ela ocupa prédio abandonado, túnel e porão, e passa a luta presa às paredes e ao teto. Abre com Varrida das Patas quando o grupo entra junto, cobre de Teia a passagem por onde o grupo veio e usa Subir quando fica cercada.",
    tracos: [{"nome": "Escalada de Aranha", "texto": "A Tsuchigumo anda por parede e teto, de cabeça para baixo inclusive, sem fazer teste."}, {"nome": "Andar na Teia", "texto": "A teia dela não é terreno difícil para a Tsuchigumo."}],
    acoes_multiplas: "A Tsuchigumo faz quatro ataques de Mordida, ou usa Varrida das Patas e faz três ataques de Mordida.",
    acoes_nomeadas: [{"nome": "Mordida", "texto": "*Ataque corpo a corpo:* {acerto} para acertar, alcance {alcance}, uma criatura. *Acerto:* {golpe} de dano Perfurante{vizinho}."}, {"nome": "Varrida das Patas", "texto": "*Teste de Resistência Físico:* CD {cd}, cada criatura num `Cone` de {cone} a partir dela. *Falha:* {golpe} de dano Cortante. *Sucesso:* metade do dano."}],
    intervencoes: [{"nome": "Mordida", "texto": "A Tsuchigumo faz um ataque de Mordida. Esse ataque não pega o vizinho."}, {"nome": "Teia", "texto": "A Tsuchigumo cobre de teia um `Retângulo` de {retangulo} que encoste nela. A área é terreno difícil até o fim da luta."}, {"nome": "Subir", "texto": "A Tsuchigumo escala até {deslocamento} pela parede ou pelo teto. Esse movimento não provoca ataque de oportunidade."}] },
  { nome: 'Hitotsume', faixa: '5 a 8', categoria: 'Ameaça', n: 1, papel: 'Emboscador',   // v0.235: pega quem está longe do grupo, e não atira
    arranjo: '0 · 3 · 2 · 1 · 3', ataque: 'Essência', marcos: { 6: ['Constituição'] }, trs: 'Espírito e Intelecto',   // v0.234: 1 da Inteligência para a Destreza que a Defesa pede
    tamanho: "Médio", corpos_na_mesa: 1, movimentos: [],
    linha: "Maldição com a forma de um menino de um olho só, que aparece parado e cada vez mais perto.",
    notas: "No folclore japonês, o hitotsume-kozō é um menino careca de um olho só que surge no caminho, mostra uma língua comprida e some. Como maldição, ele aparece em escola, hospital e casa antiga: na esquina do corredor, na porta do banheiro, no fim da escada, sempre sozinho. Na luta, ataca quem estiver mais longe do resto do grupo.",
    tracos: [{"nome": "Mais Perto", "texto": "Fora da luta, o Hitotsume só se move quando ninguém está olhando para ele."}],
    acoes_multiplas: null,
    acoes_nomeadas: [{"nome": "Língua", "texto": "*Ataque corpo a corpo:* {acerto} para acertar, alcance {alcance}, uma criatura. *Acerto:* {golpe} de dano de Concussão{vizinho}."}],
    intervencoes: [] },
  { nome: 'Kitsune', faixa: '9 a 12', categoria: 'Ameaça', n: 1, papel: 'Artilheiro',
    arranjo: '0 · 3 · 1 · 2 · 3', ataque: 'Essência', marcos: { 6: ['Inteligência'], 10: ['Destreza', 'Essência'] }, trs: 'Espírito e Intelecto',   // v0.235: o 10 obriga a Destreza e a Essência
    tamanho: "Médio", corpos_na_mesa: 1, movimentos: [],
    linha: "Maldição em forma de raposa que toma a aparência de gente e ataca com fogo à distância.",
    notas: "No folclore japonês, a kitsune é a raposa que aprende a tomar forma humana e acende o kitsunebi, o fogo-de-raposa. Como maldição, ela vive entre pessoas, com rosto humano, em estação, hospital e rua de comércio. Fala com o grupo antes de lutar e tenta separá-lo; na luta, fica longe, usa Fogo-de-Raposa e só morde quem chega ao lado dela.",
    tracos: [{"nome": "Forma Humana", "texto": "Com uma ação, a Kitsune toma a aparência de uma pessoa que ela já viu, ou volta à forma de raposa. Nenhum número do bloco muda."}],
    acoes_multiplas: null,
    acoes_nomeadas: [{"nome": "Mordida", "texto": "*Ataque corpo a corpo:* {acerto} para acertar, alcance {alcance}, uma criatura. *Acerto:* {golpe} de dano Perfurante{vizinho}."}, {"nome": "Fogo-de-Raposa", "texto": "*Ataque de conjuração à distância:* {acerto} para acertar, alcance {tecnica_alcance}, uma criatura. *Acerto:* {tecnica_dano} de dano de Fogo."}],
    intervencoes: [] },
  { nome: 'Oni', faixa: '5 a 8', categoria: 'Desastre', n: 4, papel: 'Brutamontes',
    arranjo: '3 · 3 · 3 · 0 · 1', ataque: 'Força', marcos: { 6: ['Força'] }, trs: 'Físico (Força) e Vigor',   // v0.234: o −2 do Brutamontes é por fora, e a Destreza é a da tabela; o ponto sai da Inteligência
    tamanho: "Grande", corpos_na_mesa: 1, movimentos: [],
    linha: "Maldição de corpo enorme, com chifres e um porrete de ferro, que luta de frente.",
    notas: "No folclore japonês, o oni tem chifres, pele vermelha ou azul, e carrega um kanabō, um porrete de ferro cravejado. Como maldição, ele fica no fim do caminho: no último andar, no fundo do terreno, na sala que o grupo precisa atravessar. Avança sobre quem está mais perto, usa Pancada no Chão quando o grupo o cerca e guarda Arremesso para tirar do lugar quem cuida dos outros.",
    tracos: [{"nome": "Faro", "texto": "O Oni sente cheiro de sangue. Ele sabe onde está cada criatura que perdeu vida nesta luta, se ela estiver no mesmo cômodo que ele, mesmo sem vê-la."}],
    acoes_multiplas: "O Oni faz quatro ataques de Kanabō, ou usa Pancada no Chão e faz três ataques de Kanabō.",
    acoes_nomeadas: [{"nome": "Kanabō", "texto": "*Ataque corpo a corpo:* {acerto} para acertar, alcance {alcance}, uma criatura. *Acerto:* {golpe} de dano de Concussão{vizinho}."}, {"nome": "Pancada no Chão", "texto": "*Teste de Resistência Físico:* CD {cd}, cada criatura numa `Esfera` de {esfera} a partir do corpo dele. *Falha:* {golpe} de dano de Concussão. *Sucesso:* metade do dano."}],
    intervencoes: [{"nome": "Kanabō", "texto": "O Oni faz um ataque de Kanabō. Esse ataque não pega o vizinho."}, {"nome": "Arremesso", "texto": "*Teste de Resistência Físico:* CD {cd}, uma criatura a até {alcance} dele. *Falha:* o alvo é jogado num espaço livre a até {deslocamento} do Oni e fica `Derrubado`. O arremesso não causa dano."}, {"nome": "Parede Abaixo", "texto": "O Oni derruba uma parede, pilar ou divisória a até {alcance} dele. Ela para de dar cobertura, e os quadrados onde ela estava viram terreno difícil até o fim da luta."}] },
];

// N corpos de x1 nao valem um xN do mesmo degrau — peca 26 §4.3, no nivel 30.
const CORPOS_CONTRA_UM = [0.62, 0.90];

const CAMBIO_POR_PESSOA = 3;    // um Desastre xN vale 3N capangas — peca 26 §5
const TETO_EMPILHAMENTO = 3;    // corpos do mesmo esquadrao no mesmo alvo — peca 26 §5
const REACAO = 1;               // uma por rodada — peca 26 §3.0, a tabela `Inimigos`
const DESLOCAMENTO = '9 m';     // peca 3 §3, a linha da ficha da peca 26 §3
const ALCANCE_PROJETIL = '18 m'; // o Projetil nas Classes 1 a 5 — o livro, Fundamento, tabela `Base por Classe`

module.exports = { FAIXAS, DEGRAUS, N_MAXIMO, PAPEIS, MULT_VANTAGEM, GANHO_ALCANCE,
                   CORPOS_POR_PESSOA, PAPEIS_FORA_DO_CAPANGA,
                   INTERVENCOES, PORTA_INTERVENCAO, INTERVENCAO_EXTRA, DERIVADAS, RESISTENCIA,
                   TAMANHOS, AREA_NATURAL, PRONTAS, CORPOS_CONTRA_UM,
                   CAMBIO_POR_PESSOA, TETO_EMPILHAMENTO, REACAO, DESLOCAMENTO, ALCANCE_PROJETIL };

// partA — capa, sumário e a parte "Começando":
//   O sistema numa página · Os números · Energia · Classe 0 · O dado
// Todo número daqui é conferido por matematica/pac7.py. Mexeu em valor, rode ele.
const { d, C, W, P, H1, H1nb, H2, H3, BUL, NUM, TBL, BOX, GAP } = require('./helpers.js');
const { Paragraph, TextRun, AlignmentType, PageBreak, BorderStyle } = d;

const cover = [
  GAP(2400),
  new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 120 },
    children: [new TextRun({ text: 'CRIAÇÃO DE TÉCNICAS E FEITIÇOS', size: 22, color: C.crimson, bold: true, characterSpacing: 60 })] }),
  new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 60 },
    children: [new TextRun({ text: 'FUNDAMENTO', size: 76, bold: true, color: C.deep, font: 'Georgia' })] }),
  new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 900 },
    children: [new TextRun({ text: 'manual do jogador e do mestre', size: 24, italics: true, color: C.grey })] }),
  new Paragraph({ alignment: AlignmentType.CENTER,
    border: { top: { style: BorderStyle.SINGLE, size: 8, color: C.crimson, space: 14 } },
    children: [new TextRun({ text: 'Níveis 1–20  ·  Faixa lendária 21–30  ·  Versão 7.23', size: 20, color: C.grey })] }),
  new Paragraph({ children: [new PageBreak()] }),
];

const tocPart = (t) => new Paragraph({ spacing: { before: 200, after: 50 },
  children: [new TextRun({ text: t, bold: true, size: 23, color: C.deep, font: 'Georgia' })] });
const tocItem = (t) => new Paragraph({ spacing: { after: 40 }, indent: { left: 340 },
  children: [new TextRun({ text: t, size: 20, color: C.ink })] });

const toc = [
  H1nb('Sumário'),
  tocPart('Começando'),
  tocItem('O sistema numa página  ·  Os números  ·  Energia  ·  Classe 0  ·  O dado'),
  tocPart('1 · Fundamento'),
  tocItem('Descrição  ·  Regra  ·  Famílias  ·  Selo  ·  Passivas  ·  Três Fundamentos prontos'),
  tocPart('2 · Montar um feitiço'),
  tocItem('Os cinco passos  ·  Exemplo guiado  ·  Formas  ·  Ampliar  ·  Cura  ·  Controle'),
  tocPart('3 · Melhorias'),
  tocItem('As nove Famílias  ·  Efeito Próprio'),
  tocPart('4 · Restrições'),
  tocItem('Catálogo  ·  Restrição Própria  ·  O que não empilha'),
  tocPart('5 · Fora de combate'),
  tocItem('Uso Livre  ·  Forma Efeito'),
  tocPart('6 · Liberação Máxima'),
  tocPart('7 · Técnica Máxima'),
  tocPart('8 · Regras de ouro'),
  tocPart('9 · Progressão'),
  tocPart('10 · Feitiços prontos'),
  tocPart('11 · Para o mestre'),
  tocPart('Apêndice'),
  tocItem('Glossário  ·  Ficha de feitiço  ·  Tabela de bolso  ·  Catálogo de temas'),
  new Paragraph({ children: [new PageBreak()] }),
];

const inicio = [
  H1('O sistema numa página'),

  P('Neste sistema, todo personagem nasce com uma única técnica, e ela nunca muda. Essa técnica se chama **Fundamento**, e não é uma lista de poderes pronta: é uma descrição e uma regra, escritas por você na criação do personagem. Tudo de sobrenatural que o personagem faz nasce dela.'),
  P('O que você usa em jogo são os **feitiços**: aplicações concretas da técnica, cada uma com nome próprio. Você mesmo monta os seus feitiços, gastando pontos — e é esse processo de montagem que este manual ensina.'),

  H2('A conta que move tudo'),
  P('Todo feitiço tem uma **Classe**, que mede o tamanho dele. A Classe diz quantos pontos você tem pra gastar na montagem:'),
  BOX(null, ['**Pontos = 3 × Classe.**  Um feitiço de Classe 3 tem 9 pontos.']),
  P('Cada ponto que você não gastar em mais nada vira **1d8 de dano**. Um Classe 3 que põe tudo em dano causa 9d8.'),
  P('Os pontos também compram **Melhorias**: alcance maior, área, derrubar o alvo, conjurar como ação bônus. E, se quiser recuperar pontos, você pode aceitar **Restrições** — desvantagens que devolvem pontos ao orçamento em troca de o feitiço ser mais difícil de usar.'),
  P('Os pontos devolvidos por Restrição só servem pra pagar Melhoria — **Restrição nunca aumenta o dano**. E, contra um alvo só, feitiço comum não passa dos pontos da Classe em dados: quem rompe esse limite é a **Liberação Máxima**, que você ganha no nível 10 (seção 6).'),

  H2('A escala da Classe'),
  P('São oito Classes, e eles não são todos iguais em papel:'),
  TBL(['Classe', 'O que é', 'Quando aparece'],
    [
      ['0', 'O feitiço grátis. Não custa PE, não ocupa espaço na lista e não se monta com pontos.', 'Nível 1'],
      ['1 a 5', 'Os feitiços montados. É onde o jogo acontece, e é o que este manual ensina a construir.', 'Níveis 1 a 20'],
      ['6 e 7', 'A faixa lendária. Mesma montagem, números maiores.', 'Níveis 21 a 30'],
    ],
    [10, 62, 28], { boldCols: [0], centerCols: [0] }
  ),
  GAP(100),
  P('Você não escolhe a Classe livremente: cada feitiço é montado na Classe que o seu nível já liberou, e a tabela de Classes na próxima página mostra quando cada um chega. Daqui pra frente, quando o manual disser só "a Classe", vale pra escala inteira.'),

  H2('Um feitiço em números'),
  BOX('LANÇA NEGRA · CLASSE 2 · PROJÉTIL', [
    'Classe 2 dá **6 pontos**. A Melhoria **Fura** custa 2 e faz o feitiço ignorar até 6 de Redução de Dano. A Restrição **Atrasar** devolve 2, em troca de a conjuração custar a rodada inteira.',
    '6 − 2 + 2 = 6 pontos sobrando.  **Dano: 6d8 (média 27). Custo: 6 de PE.**',
    'A Restrição pagou a Melhoria inteira, e o feitiço saiu com o dano cheio da Classe — é exatamente pra isso que Restrição serve. O que ela nunca faz é passar disso: 6 pontos continuam sendo o máximo de dados de uma Classe 2 contra um alvo.',
  ]),

  H2('As cinco peças da ficha'),
  P('O manual segue a ordem da ficha: o Fundamento e as Passivas na seção 1, os feitiços nas seções 2 a 5, a Liberação Máxima na seção 6 e a Técnica Máxima na seção 7.'),
  TBL(['Peça', 'O que é'],
    [
      ['Fundamento', 'Sua técnica. Uma descrição, uma Regra, Famílias Livres e Fechadas, um Selo e as Passivas.'],
      ['Feitiços', 'As aplicações da técnica. Você monta cada uma. Ganha uma nova a cada dois níveis.'],
      ['Passivas', 'Efeitos que ficam ligados sozinhos. Custam espaços de feitiço.'],
      ['Liberação Máxima', 'O feitiço que rompe o limite de dano num alvo só. Nos níveis 10, 20 e 30.'],
      ['Técnica Máxima', 'O golpe de dano fixo que carrega o nome da técnica. Do nível 17 em diante.'],
    ],
    [20, 80], { boldCols: [0] }
  ),
];

const numeros = [
  H1('Os números'),

  P('Esta página concentra os números que o resto do manual usa. Não precisa decorar nada agora: volte aqui sempre que uma seção citar um valor.'),
  BOX(null, [
    '**Pontos** = 3 × Classe          **Teto de dano** = 4 × Classe em dados',
    '**Devolução máxima** = 2 × Classe      **Liberação Máxima** = + Classe em dados',
    '**Custo em PE** = 3 × Classe (o mesmo número dos pontos)',
    '',
    'Melhoria **Leve** custa metade da Classe · **Média** custa a Classe · **Pesada** custa Classe e meio. Arredonde pra cima.',
  ]),

  TBL(['Classe', 'Nível', 'Pontos e PE', 'Leve', 'Média', 'Pesada', 'Devol. máx', 'Liberação', 'Teto', 'Dano cheio'],
    [
      ['1', '1', '3', '1', '1', '2', '2', '+1', '4', '3d8 = 13'],
      ['2', '5', '6', '1', '2', '3', '4', '+2', '8', '6d8 = 27'],
      ['3', '9', '9', '2', '3', '5', '6', '+3', '12', '9d8 = 40'],
      ['4', '13', '12', '2', '4', '6', '8', '+4', '16', '12d8 = 54'],
      ['5', '17', '15', '3', '5', '8', '10', '+5', '20', '15d8 = 67'],
      ['6', '21', '18', '3', '6', '9', '12', '+6', '24', '18d8 = 81'],
      ['7', '26', '21', '4', '7', '11', '14', '+7', '28', '21d8 = 94'],
    ],
    [7, 7, 13, 8, 8, 9, 12, 9, 8, 19], { centerCols: [0,1,2,3,4,5,6,7,8,9], boldCols: [0] }
  ),
  GAP(100),
  P('A coluna **Nível** é quando aquela Classe abre pra você. **Leve**, **Média** e **Pesada** são os três preços de Melhoria (seção 3), e **Devol. máx** é o total que as Restrições de um feitiço podem devolver (seção 4).'),
  P('A coluna **Teto** é o máximo de dados de dano de um feitiço quando você soma todos os alvos e repetições. Contra um alvo só, o limite é mais baixo: um feitiço comum para nos pontos da Classe. Quem alcança o teto num alvo só é a **Liberação Máxima** (seção 6).'),

  H2('Quantas Melhorias cabem'),
  TBL(['Classe do feitiço', 'Melhorias', 'Restrições'],
    [['1 e 2', '2', '2'], ['3 e 4', '3', '2'], ['5 em diante', '4', '2']],
    [40, 30, 30], { centerCols: [1,2], boldCols: [0] }
  ),
  GAP(100),
  P('A Forma não conta como Melhoria.'),

  H2('Energia'),
  P('Conjurar um feitiço custa **3 × Classe** de PE — o mesmo número dos pontos dele. Classe 0 é grátis.'),
  BUL('**Liberação Máxima** custa 50% a mais que a Classe dela, arredondando pra cima.'),
  BUL('**Técnica Máxima** custa 5 × a sua maior Classe de PE. A regra completa está na seção 7.'),
  GAP(100),
  P('Com um conjurador ganhando 6 PE por nível, isso dá:'),
  TBL(['Nível', 'PE total', 'Maior Classe', 'Custo', 'Quantas vezes você lança o seu melhor feitiço'],
    [
      ['1', '6', '1', '3', '2'],
      ['5', '30', '2', '6', '5'],
      ['9', '54', '3', '9', '6'],
      ['13', '78', '4', '12', '6'],
      ['17', '102', '5', '15', '6'],
      ['20', '120', '5', '15', '8'],
    ],
    [12, 15, 17, 12, 44], { centerCols: [0,1,2,3,4], boldCols: [0] }
  ),
  GAP(100),
  BOX('ESSA ÚLTIMA COLUNA É UM TETO, E NÃO UM DIA', [
    'Ela responde *"quantas vezes cabe se você não fizer mais nada com o seu PE"*. Um dia de verdade tem outras despesas ao mesmo tempo — o sistema em volta tem coisas que cobram **por rodada** enquanto estão ligadas, e a Integridade encarece todo feitiço quando o seu segundo degrau acende.',
    'Na prática, um conjurador gasta PE em cerca de **metade das rodadas de luta do dia** e passa a outra metade no Classe 0, no golpe simples e no que for de graça. Isso não é aperto: é o desenho.',
    'Leia esta coluna como o limite superior. Quem trata ela como orçamento de dia acaba precificando peça nova contra um personagem que só faz uma coisa — e esse erro já custou três versões do sistema em volta.',
  ]),

  H2('Classe 0'),
  P('Feitiços de Classe 0 não gastam PE, não ocupam espaço na lista e não se montam: escolha uma Forma e pronto. São o golpe de todo turno em que o PE precisa ser poupado.'),
  TBL(['Seu nível', '1', '5', '11', '17', '25'],
    [
      ['Quantos você tem', '2', '3', '4', '5', '5'],
      ['Dano', '2d8', '3d8', '4d8', '5d8', '6d8'],
    ],
    [24, 15, 15, 15, 15, 16], { centerCols: [1,2,3,4,5], boldCols: [0] }
  ),
  GAP(100),
  P('Cabe uma Melhoria Leve numa Classe 0, tirando um dado pra pagar. A base de alcance da Classe 0 fica um degrau abaixo da normal; a tabela está na seção 2.'),
  P('**Classe 0 não cura.** As Formas Cura e Onda ficam de fora dela. A tabela de cura da seção 2 começa na Classe 1, e é ela que diz o que uma cura vale — quem quer curar paga uma Classe.'),

  H2('O dado'),
  P('Monte sempre em d8: pontos, Melhorias e Restrições só existem em d8. Se a sua mesa rola outro dado, converta o total final na hora de rolar.'),
  TBL(['d8', 'd6', 'd12', 'd8', 'd6', 'd12', 'd8', 'd6', 'd12'],
    [
      ['1', '1', '1', '11', '14', '8', '21', '27', '15'],
      ['2', '3', '1', '12', '15', '8', '22', '28', '15'],
      ['3', '4', '2', '13', '17', '9', '23', '30', '16'],
      ['4', '5', '3', '14', '18', '10', '24', '31', '17'],
      ['5', '6', '3', '15', '19', '10', '25', '32', '17'],
      ['6', '8', '4', '16', '21', '11', '26', '33', '18'],
      ['7', '9', '5', '17', '22', '12', '27', '35', '19'],
      ['8', '10', '6', '18', '23', '12', '28', '36', '19'],
      ['9', '12', '6', '19', '24', '13', '', '', ''],
      ['10', '13', '7', '20', '26', '14', '', '', ''],
    ],
    [10, 11, 12, 10, 11, 12, 10, 11, 13], { centerCols: [0,1,2,3,4,5,6,7,8], boldCols: [0,3,6] }
  ),
  GAP(100),
  P('A média nunca se afasta mais de 3 pontos da conta em d8.'),
];

module.exports = { cover, toc, inicio, numeros };

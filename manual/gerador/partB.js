// partB — seção 1 (Fundamento, com Passivas) e os Três Fundamentos prontos.
// v7: o Selo não dá mais +1 ponto na Classe 2+. Ele é identidade + a trava da seção 4
// (Restrição que o Selo já obriga não devolve ponto). Nada de bônus universal.
const { d, C, W, P, H1, H2, H3, BUL, NUM, TBL, BOX, GAP } = require('./helpers.js');

const fundamento = [
  H1('1 · Fundamento'),
  P('O Fundamento é a técnica inata do personagem. Ele é escrito uma vez, na criação, junto com o mestre — e não muda depois: o que evolui com os níveis são os feitiços que saem dele. Um Fundamento completo tem cinco partes, e esta seção percorre uma por uma.'),
  BOX('NA CRIAÇÃO, VOCÊ ESCREVE', [
    '**1.** A **Descrição** da técnica, com o tipo de dano dela.',
    '**2.** A **Regra**: a frase que resume o que a técnica faz.',
    '**3.** As **Famílias**: duas Livres e três Fechadas.',
    '**4.** O **Selo**: o que você sempre faz pra conjurar.',
    '**5.** A **Passiva Livre** — e, se a técnica pedir, uma Regra Própria.',
  ]),

  H2('Descrição'),
  P('Escreva a sua técnica como quiser, no tamanho que quiser: de onde ela veio, como aparece, o que as pessoas veem quando ela age. A Descrição não tem efeito mecânico direto, mas é dela que o mestre vai tirar a régua pra aprovar ou recusar os seus feitiços.'),
  P('Anote junto o **tipo de dano** da técnica — um ou dois: corte, fogo, peso, o que a Descrição pedir. Esse tipo vale pra todos os seus feitiços.'),
  BOX('Exemplo', [
    '*Duas relíquias respondem ao chamado dela: um bastão com uma tranca na ponta, outro com uma chave. A tranca segura o instante — o que ela prende para de acontecer e continua parado até ela soltar. A chave abre distância — o que ela destrava deixa de estar onde estava. Ninguém sabe se os bastões são a técnica ou se a técnica só precisa deles pra caber num corpo humano.*',
  ]),

  H2('Regra'),
  P('Depois da Descrição, resuma a técnica numa única frase: a Regra. Ela é o contorno da técnica — todo feitiço que você criar, do primeiro ao último, precisa caber dentro dela.'),
  BUL('*"Prender um instante no lugar, ou abrir a distância entre duas coisas."*'),
  BUL('*"Cortar tudo o que eu enxergo em duas metades."*'),
  BUL('*"Emprestar o meu peso pro que eu encostar."*'),
  GAP(60),
  P('Uma boa Regra exclui coisas. "Controlar fogo" não exclui nada e vira um cheque em branco; "acender o que já passou pela minha mão" exclui bastante, e é exatamente isso que a torna interessante — o limite é o que obriga a criatividade na montagem dos feitiços.'),
  P('Se estiver travado, o **Catálogo de Temas** no apêndice traz 70 pontos de partida.'),

  H2('Famílias'),
  P('As Melhorias — as peças que você compra pros seus feitiços na seção 3 — estão divididas em nove Famílias, cada uma cuidando de um tipo de efeito:'),
  TBL(['Família', 'Do que trata'],
    [
      ['Alcance', 'Chegar longe, se mexer, mexer o inimigo de lugar'],
      ['Área', 'Pegar mais de um alvo, aumentar tamanho, dividir o ataque'],
      ['Mira', 'Acertar, não errar, atravessar defesa'],
      ['Controle', 'Derrubar, prender, calar, barreira, terreno'],
      ['Auxiliares', 'Somar e tirar número: vantagem, defesa, CD, deslocamento'],
      ['Castigo', 'Fazer o dano render mais'],
      ['Tempo', 'Ação bônus, reação, deixar armado, conjurar escondido'],
      ['Marca', 'Preparar o próximo golpe, roubar vida, rastrear'],
      ['Amparo', 'Curar, limpar condição, levantar aliado'],
    ],
    [16, 84], { boldCols: [0] }
  ),
  GAP(120),
  P('Na criação, o seu Fundamento define a relação dele com essas Famílias — e é aqui que duas técnicas com a mesma Regra viram personagens diferentes:'),
  BUL('**Duas Famílias Livres:** as Melhorias delas custam metade da Classe a menos, com mínimo de 1 ponto. É onde a sua técnica é naturalmente boa.'),
  BUL('**Três Famílias Fechadas:** você nunca compra nada delas, em Classe nenhum. É o que a sua técnica simplesmente não faz.'),
  BUL('As outras quatro ficam no preço normal.'),
  GAP(60),
  P('Na prática: uma Melhoria Média num feitiço de Classe 4 custa 4 pontos. Se ela for de uma Família Livre sua, o desconto de metade da Classe (2) derruba o preço pra 2. Se for de uma Família Fechada, ela não está à venda.'),
  P('As Formas — o jeito como o feitiço sai, na seção 2 — também têm Família: Explosão, Cone e Linha são de **Área**; Cura, Apoio e Onda são de **Amparo**. Fechar uma dessas Famílias bloqueia as Formas dela junto. Projétil, Toque e Efeito são de todo mundo.'),

  H2('Selo'),
  P('O Selo é uma coisa que o seu personagem sempre precisa fazer pra conjurar, seja qual for o feitiço: um gesto, um som, uma condição visível. É a assinatura da técnica — o que a mesa vê ou ouve toda vez que ela entra em cena.'),
  BUL('Bater palma. · Dizer o nome do feitiço. · Estar enxergando o alvo. · Ter tocado no alvo nesta cena. · Estar pisando no chão.'),
  GAP(60),
  P('O Selo não mexe em ponto nenhum: não custa, não devolve e não dá bônus. Ele existe pra dar corpo à técnica e pra criar jogo — quem conhece o seu Selo sabe o que procurar quando você se mexe. A única regra mecânica ligada a ele está na seção 4: como o Selo já é uma obrigação sua, **uma Restrição que cobra a mesma coisa que ele não devolve ponto**.'),
  P('O Selo é uma coisa só, e a mesa consegue apontar o momento em que aconteceu. Se você precisa de mais de uma frase pra explicar, não é Selo — é condição de cena ou de alvo, e isso se compra por feitiço, com a Restrição **Condicional**.'),
  TBL(['É Selo', 'Não é Selo, é Condicional'],
    [
      ['Bater palma', 'Bater palma três vezes no ritmo certo'],
      ['Estar enxergando o alvo', 'Enxergar o alvo sem que ele te enxergue'],
      ['Ter tocado no alvo nesta cena', 'Ter tocado no alvo e saber o nome dele'],
      ['Gastar o próprio sangue', 'Gastar sangue de alguém do seu clã'],
    ],
    [50, 50], { }
  ),
  GAP(100),
  P('O Selo pode mudar de forma sem perder a função: se você perde a mão que batia palma, arruma outra coisa que faça o mesmo som.'),
  GAP(60),
  TBL(['Selos de Jujutsu Kaisen', 'O Selo'],
    [
      ['Nobara (Boneco de Palha)', 'Martelo e prego na mão.'],
      ['Nobara (Ressonância)', 'Um pedaço do alvo: sangue, cabelo, um membro.'],
      ['Todo (Boogie Woogie)', 'Bater palma. Depois que perdeu a mão, um vibraslap: o som mudou de fonte, o Selo continuou.'],
      ['Inumaki (Fala Amaldiçoada)', 'Falar o comando, e a garganta cobra o preço.'],
      ['Megumi (Dez Sombras)', 'Um sinal de mão pra cada shikigami.'],
      ['Mahito (Transfiguração Ociosa)', 'Tocar no alvo.'],
      ['Choso (Manipulação de Sangue)', 'Gastar o próprio sangue.'],
      ['Nanami (Proporção)', 'Mirar o ponto 7:3 do corpo do alvo.'],
    ],
    [32, 68], { boldCols: [0] }
  ),
];

const passivas = [
  H2('Passivas'),
  P('Passiva é o que a sua técnica faz sem você mandar: o efeito que fica ligado enquanto você existe. Cada Passiva tem uma Classe, como um feitiço, e é paga com **espaços de feitiço conhecido** — você abre mão de saber mais feitiços pra que a técnica trabalhe sozinha.'),
  TBL(['Classe', 'Custa', 'Libera no nível', 'O que cabe'],
    [
      ['Livre', 'nada', '1', 'Ficção pura. Não rola dado, não muda número, não faz ninguém rolar. Todo personagem tem uma.'],
      ['1', '1 espaço', '1', 'Efeito pequeno, condicional, ou de informação.'],
      ['2', '2 espaços', '7', 'Efeito reativo, com limite de uso por cena ou por descanso.'],
      ['3', '3 espaços', '13', 'Permanente. Muda como você joga.'],
    ],
    [10, 13, 17, 60], { boldCols: [0], centerCols: [0,1,2] }
  ),
  GAP(120),
  P('Máximo de cinco Passivas pagas. A Passiva Livre não conta.'),
  P('**Resistência**, quando alguma coisa aqui usar a palavra, quer dizer sempre a mesma coisa: o dano daquele tipo cai pela metade, antes de qualquer outra conta. Ela é sempre presa a um tipo — não existe resistência a tudo.'),

  H3('Passiva Livre'),
  P('Todo personagem começa com uma Passiva Livre, de graça. Ela não rola dado, não muda número nenhum e não faz ninguém rolar — dentro desses limites, use quando e quanto quiser.'),
  P('Você enxerga emoção como cor. Planta murcha quando você passa. Você nunca se perde. Seu reflexo aparece um segundo atrasado. Metal fica frio na sua mão.'),
  P('Repare que o Livre entrega o dado cru, nunca a leitura pronta: você vê o medo na cor de alguém, mas descobrir o motivo do medo continua sendo trabalho seu.'),

  H3('O que nenhuma Passiva paga pode fazer'),
  BUL('Bônus de dano ou acerto que vale o tempo todo, sem condição.'),
  BUL('Uma ação a mais por rodada.'),
  BUL('Imunidade completa a um tipo de dano ou condição.'),
  BUL('Cura sem limite de uso por descanso.'),
  BUL('Redução de Dano passiva: descontar um número fixo de todo golpe que te acerta. Resistência a um tipo, sim — é o que a Escama faz. Desconto em tudo, não.'),

  H3('Lista'),
  TBL(['Passiva', 'Classe', 'O que faz'],
    [
      ['Leitura', '1', 'Você identifica a Classe e a Forma de qualquer feitiço conjurado a até 18 m.'],
      ['Instinto', '1', 'Você não é pego de surpresa enquanto estiver acordado.'],
      ['Raiz', '1', 'Você não é movido à força nem derrubado contra a sua vontade.'],
      ['Mão Firme', '1', 'Você não perde concentração nem carga por dano de 10 ou menos.'],
      ['Farejador', '1', 'Você sente se alguém conjurou num lugar nas últimas 24 horas, e de que Classe.'],
      ['Aviso', '1', 'Você sabe qual foi o último feitiço que um inimigo à vista usou.'],
      ['Fluxo', '2', 'Ao conjurar Classe 3 ou mais, você ganha 2 × Classe de vida temporária.'],
      ['Recomposição', '2', 'Uma vez por descanso curto, gasta a ação e recupera 5 × a sua maior Classe.'],
      ['Segunda Natureza', '2', 'Uma vez por dia, conjura um feitiço de Classe até metade do seu maior sem gastar PE.'],
      ['Eco', '2', 'Quando você derruba um inimigo com feitiço, o próximo feitiço da cena custa metade.'],
      ['Costura', '2', 'Uma vez por cena, um aliado a até 9 m que cairia a 0 fica com 1.'],
      ['Contramedida', '2', 'Como Reação, quando alguém conjura a até 9 m, gasta PE e sobe em 2 a CD daquele feitiço.'],
      ['Peso da Presença', '2', 'Inimigos fracos que começam o turno a até 6 m fazem TR ou ficam Amedrontados por uma rodada.'],
      ['Escama', '3', 'Escolha um tipo de dano que a sua Regra justifique. Você tem resistência a ele: todo dano daquele tipo cai pela metade.'],
      ['Afinidade', '3', 'Escolha um tema da sua Regra. Feitiços daquele tema ignoram cobertura Parcial e resistência ao seu tipo de dano.'],
      ['Reserva Profunda', '3', 'Seu PE máximo sobe em 3 × a sua maior Classe.'],
      ['Regra Própria', '1 a 3', 'Sua técnica impõe uma regra em vez de produzir efeito. Ver abaixo.'],
      ['Passiva Própria', '1 a 3', 'Qualquer outra coisa, montada com o mestre na escala da tabela acima.'],
    ],
    [20, 8, 72], { boldCols: [0], centerCols: [1] }
  ),

  H3('Regra Própria'),
  P('Algumas técnicas não produzem um efeito: elas impõem uma regra ao mundo — julgamento, aposta, contrato, dívida, sorte. Pra essas existe a Regra Própria, escrita junto com o mestre antes de a campanha começar, obedecendo cinco requisitos:'),
  BUL('Uma frase.'),
  BUL('Verificável: a mesa aponta o momento em que ela disparou.'),
  BUL('Simétrica: vale contra você nas mesmas condições.'),
  BUL('Sem dano direto: gera recurso, condição ou obrigação.'),
  BUL('Com limite por cena.'),
  GAP(80),
  P('A Regra Própria é a única Passiva que pode ser comprada em Classe 1 desde o nível 1. Quando os níveis liberarem as Classes maiores, ela sobe pra Classe 2 e 3 pagando só a diferença de espaços.'),
  P('Exemplos:'),
  BUL('*"Quem me atacar sabendo que eu não revidei acumula uma Dívida. Cobro uma por cena."*'),
  BUL('*"Quando eu aposto e ganho, meu próximo teste na cena tem vantagem. Uma vez por cena."*'),
  BUL('*"Duas coisas que eu tocar na mesma rodada ficam ligadas até o fim da cena."*'),
];

const exemplosFund = [
  H1('Três Fundamentos prontos'),
  P('Três Fundamentos completos, prontos pra usar como estão ou pra servir de régua na hora de escrever o seu. O primeiro deles, a **Régua**, volta na seção 2 pra montar o primeiro feitiço do manual.'),
  P('Os três param onde a criação de personagem para: Descrição, Regra, Famílias, Selo e — quando a técnica pede — a Passiva. Liberação Máxima e Técnica Máxima não aparecem aqui porque só chegam nos níveis 10 e 17, e são escritas na hora.'),

  H2('Régua'),
  TBL(null, [
    ['Descrição', 'Ele não corta com a mão nem com nada que dê pra ver. Ele mede: aponta o dedo, calcula a distância até o alvo e cobra essa distância do corpo do outro. Quanto mais longe, mais fundo o corte. Tipo de dano: corte.'],
    ['Regra', '"Medir a distância entre dois pontos e cobrar por ela."'],
    ['Livres', 'Mira · Alcance'],
    ['Fechadas', 'Área · Amparo · Auxiliares'],
    ['Selo', 'Apontar com o dedo e falar o nome do alvo em voz alta.'],
  ], [16, 84], { boldCols: [0] }),

  H2('Sentença'),
  TBL(null, [
    ['Descrição', 'Ela não decide nada, só registra. Cada coisa que acontece perto dela fica anotada em algum lugar que ninguém vê, e uma hora a conta fecha. Quando fecha, o que ela cobra não é dano — é o que a pessoa devia. Tipo de dano: psíquico.'],
    ['Regra', '"Registrar o que foi feito e cobrar quando fechar a conta."'],
    ['Livres', 'Marca · Castigo'],
    ['Fechadas', 'Área · Alcance · Amparo'],
    ['Selo', 'Ter visto o ato com os próprios olhos.'],
    ['Passiva', 'Regra Própria (Classe 3): "quem ferir alguém desarmado na minha frente acumula uma Dívida. Posso cobrar uma Dívida por cena: o alvo tem desvantagem no próximo teste e eu tenho vantagem contra ele até o fim do meu próximo turno."'],
  ], [16, 84], { boldCols: [0] }),

  H2('Banca'),
  TBL(null, [
    ['Descrição', 'Ele joga. A técnica sai da mão como aposta: moeda no ar, carta virada, um dado rolando em algum lugar que ninguém vê. O golpe em si paga pouco, porque o prêmio de verdade fica guardado com a banca — e a banca fecha a conta quando ele ganha. Tipo de dano: impacto.'],
    ['Regra', '"Apostar contra a sorte e cobrar o prêmio."'],
    ['Livres', 'Auxiliares · Marca'],
    ['Fechadas', 'Área · Alcance · Castigo'],
    ['Selo', 'Falar a aposta em voz alta.'],
    ['Passiva', 'Regra Própria (Classe 1 na criação, subindo com os níveis): "quando eu aposto e ganho, meu próximo teste na cena tem vantagem. Uma vez por cena."'],
  ], [16, 84], { boldCols: [0] }),
  P('O orçamento da Banca mora na Passiva. Os feitiços são fracos de propósito: é uma técnica que guarda o poder pra quando a conta fecha, e a Regra Própria é onde essa conta fecha.'),
];

module.exports = { fundamento, passivas, exemplosFund };

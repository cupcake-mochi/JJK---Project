// partD — seção 3 (catálogo de Melhorias) e seção 4 (catálogo de Restrições).
// Os textos de efeito são regra: se mudar um, confira o impacto em matematica/pac7.py.
const { d, C, W, P, H1, H2, H3, BUL, NUM, TBL, BOX, GAP, RULE } = require('./helpers.js');
const RW = [21, 13, 66];
const CAT = (rows) => TBL(['Melhoria', 'Custo', 'O que faz'], rows, RW, { boldCols: [0], centerCols: [1] });

const melhorias = [
  H1('3 · Melhorias'),
  P('Sessenta e seis Melhorias, em nove Famílias. O preço de cada uma depende da Classe do feitiço em que ela entra: **Leve** custa metade da Classe, **Média** custa a Classe inteiro, **Pesada** custa Classe e meio — sempre arredondando pra cima.'),
  P('Exemplo de leitura: num feitiço de Classe 3, uma Leve custa 2 pontos, uma Média custa 3 e uma Pesada custa 5. Nas suas duas Famílias Livres, tire metade da Classe do preço, com mínimo de 1; nas três Fechadas, não há o que comprar.'),

  H2('Alcance'),
  CAT([
    ['Longe', 'Leve', 'Sobe um degrau na escada de alcance. Pode comprar duas vezes.'],
    ['Muito Longe', 'Média', 'Sobe três degraus de uma vez.'],
    ['Sem Ver', 'Pesada', 'Você conjura contra um alvo fora da sua linha de visão, desde que saiba onde ele está. Alcance normal do feitiço.'],
    ['Passo', 'Leve', 'Você anda até 6 m antes ou depois do feitiço, sem provocar ataque de oportunidade.'],
    ['Empurrão', 'Leve', 'Move o alvo até 6 m na direção que você quiser.'],
    ['Troca', 'Média', 'Você e o alvo trocam de lugar.'],
    ['Perseguir', 'Média', 'Se o alvo sair do alcance antes do feitiço resolver, o feitiço vai atrás.'],
  ]),

  H2('Área'),
  CAT([
    ['Maior', 'Leve', 'Sobe um degrau de tamanho de área. Pode comprar duas vezes.'],
    ['Muito Maior', 'Pesada', 'Sobe três degraus de tamanho de uma vez.'],
    ['Escolher', 'Média', 'Você decide quem, dentro da área, é atingido.'],
    ['Fica', 'Média', 'A área continua ali por 1 minuto. Quem entrar ou começar o turno nela leva metade dos dados. Exige concentração.'],
    ['Mais Um', 'Leve', 'Um alvo a mais. Os dados são divididos entre os alvos. Pode comprar duas vezes.'],
    ['Rajada', 'Leve', 'Divide o feitiço em (Classe + 1) tiros, cada um com sua rolagem de acerto, distribuídos como você quiser.'],
    ['Salto', 'Média', 'Depois do primeiro alvo, pula pro inimigo mais perto a até 9 m com metade dos dados.'],
    ['Contorno', 'Leve', 'A área faz curva. Ignora cobertura e dobra esquinas.'],
  ]),

  H2('Mira'),
  CAT([
    ['Precisão', 'Leve', '+2 na rolagem de acerto, ou +2 na CD do Teste de Resistência.'],
    ['Certeiro', 'Média', 'Sem rolagem de acerto. O alvo ainda faz o Teste de Resistência pra metade.'],
    ['Inescapável', 'Média', 'Sem acerto e sem Teste de Resistência: o dano é automático. Este feitiço não pode ter mais nenhuma peça, nem Melhoria nem Restrição, e não pode ser uma Liberação Máxima.'],
    ['Fura', 'Média', 'Ignora até 3 × Classe de Redução de Dano. O que passar disso continua valendo.'],
    ['Corrói', 'Pesada', 'Resistência ao seu tipo de dano deixa de valer neste feitiço. Só pode ser comprada se Mira for uma das suas Famílias Livres.'],
    ['Sem Cobertura', 'Leve', 'Cobertura leve e meia cobertura não atrapalham.'],
    ['De Novo', 'Média', 'Se você errar, rola de novo. Uma vez por cena.'],
    ['Toca a Alma', 'Leve', 'Só da Classe 3 em diante, e só pra Fundamento cuja Regra encosta em alma, mente ou conceito. Os dados de dano deste feitiço viram dano na alma, e você fica com metade deles, arredondando pra baixo. Não entra numa Liberação Máxima. A régua do dano na alma está na seção 11.'],
  ]),
  BOX('Imunidade', [
    'Nenhuma Melhoria fura imunidade. Quem quiser isso monta uma **Passiva de Regra Própria** com o mestre, com limite de uma vez por cena.',
  ], 'warn'),

  H2('Controle'),
  CAT([
    ['Condição', 'o nível dela', 'Aplica uma das catorze condições. O preço é o nível dela — Leve, Média ou Pesada —, na tabela logo abaixo. Dura uma rodada. As de nível Pesada dão Teste de Resistência no fim de cada turno do alvo, e cabe só uma delas por feitiço.'],
    ['Terreno', 'Leve', 'A área vira terreno difícil, ou fica obscurecida, por uma rodada.'],
    ['Anteparo', 'Média', 'Deixa uma parede ou escudo com 10 × Classe de pontos de vida, por 1 minuto.'],
    ['Prende', 'Média', 'O alvo não sai do lugar até o fim do próximo turno dele. Ele pode gastar a ação pra tentar um Teste de Resistência e se soltar.'],
    ['Cerca', 'Leve', 'O alvo não consegue se aproximar de você até o fim do próximo turno dele.'],
    ['Puxa', 'Média', 'Todo mundo na área é puxado 6 m na direção do centro.'],
    ['Desarma o Feitiço', 'Média', 'Cancela um efeito contínuo ou uma barreira de Classe igual ou menor que o seu.'],
  ]),

  H2('As condições, uma a uma'),
  P('São catorze, e cada uma tem um **nível**: Leve, Média ou Pesada. O nível faz duas coisas ao mesmo tempo — é o **preço** da Melhoria Condição que aplica ela, e é o que custa em energia pra **tirar** ela de alguém (1 ponto por nível). Uma condição dura uma rodada.'),
  P('As três tabelas abaixo são as catorze separadas por nível. Numa Classe 5, por exemplo, aplicar uma Leve custa 3 pontos, uma Média custa 5 e uma Pesada custa 8.'),
  TBL(['Nível Leve', 'O que faz'],
    [
      ['Lento', 'Deslocamento pela metade, e sem Ação Bônus.'],
      ['Incapacitado', 'Você não pode Bloquear, e todo ataque corpo a corpo contra você é crítico.'],
      ['Derrubado', 'No chão. Só se move rastejando, desvantagem nos seus ataques, e quem ataca de até 1,5 m tem vantagem — de longe, desvantagem.'],
      ['Agarrado', 'Deslocamento 0. Acaba se quem agarrou ficar Incapacitado, ou se algo te tirar do alcance dele.'],
      ['Desarmado', 'A sua arma está no chão ou na mão de outro. Você bate desarmado até pegar de volta.'],
      ['Surdo', 'Não ouve. Falha automático em teste que precise de audição, e −2 na iniciativa.'],
    ], [2200, 6800], { boldCols: [0] }),

  TBL(['Nível Média', 'O que faz'],
    [
      ['Calado', 'Você não conjura. Nada que precise de voz, gesto ou Selo sai.'],
      ['Enfeitiçado', 'Você não ataca quem enfeitiçou nem mira efeito nocivo nele, e ele tem vantagem em teste social contra você.'],
    ], [2200, 6800], { boldCols: [0] }),

  TBL(['Nível Pesada', 'O que faz'],
    [
      ['Petrificado', 'Virou pedra. Incapacitado, deslocamento 0, sem perceber o que está em volta, vantagem para quem te ataca — e resistência a todo dano.'],
      ['Impedido', 'Deslocamento 0, desvantagem nos seus ataques e no Teste de Resistência Físico, e vantagem para quem te ataca.'],
      ['Cego', 'Não enxerga. Falha automático em teste que precise de vista, desvantagem nos seus ataques, vantagem para quem te ataca.'],
      ['Amedrontado', 'Desvantagem em ataque e teste enquanto enxergar a fonte do medo, e você não se aproxima dela de vontade própria.'],
      ['Envenenado', 'Desvantagem nos seus ataques e em todo teste de perícia.'],
      ['Atordoado', 'Você perde a Ação Padrão e não usa reação. Quem tem mais de uma Ação Padrão no turno perde UMA, não todas.'],
    ], [2200, 6800], { boldCols: [0] }),

  BOX('Por que as três tabelas não são "menores" e "maiores"', [
    'Até a v7.8 as condições eram vendidas em dois pacotes: Condição Menor por Média e Condição Maior por Pesada. Um preço só, para coisas muito diferentes.',
    'A conta mediu as catorze e o espalhamento dentro de um pacote chegava a dezessete vezes: o Impedido custava o mesmo que o Surdo, e o Incapacitado custava o mesmo que o Petrificado.',
    'Agora cada condição custa o que ela vale. Dez das catorze estavam no degrau errado — três eram baratas demais e sete eram caras demais.',
  ], 'info'),

  BOX('Atordoado e Incapacitado atacam eixos diferentes, e não se empilham', [
    'Atordoado tira PARTE do turno: uma Ação Padrão e a reação. Você continua se defendendo.',
    'Incapacitado não tira turno nenhum — tira a DEFESA. Você age e não se protege.',
    'E eles não custam o mesmo: Atordoado é Pesada e Incapacitado é Leve. Tirar o que o alvo FAZ custa três vezes mais que tirar o que PROTEGE ele — e a conta concorda, porque em dano por rodada um vale pouco mais de três vezes o outro.',
    'O Atordoado cobra uma Ação Padrão só de propósito: um chefe age mais de uma vez por rodada, e apagar o turno dele com uma linha de Controle sairia barato demais.',
  ], 'info'),

  BOX('Três coisas que NÃO são condição aqui', [
    'Inconsciente é cair morrendo, e tem regra própria no sistema em volta — não é efeito de uma rodada.',
    'Exaustão é relógio de descanso, e a Melhoria Condição não alcança ela.',
    'Invisível é benefício: comprar para aplicar num inimigo é pagar para ajudar ele.',
  ], 'warn'),

  H2('Auxiliares'),
  P('Números em cima de alguém. Em feitiço de dano, valem contra o alvo; nas Formas de Amparo, valem no aliado.'),
  CAT([
    ['Impulso', 'Leve', 'O alvo tem vantagem no próximo teste dele, até o fim do próximo turno.'],
    ['Trava', 'Leve', 'O alvo tem desvantagem no próximo ataque dele.'],
    ['Abre Ferida', 'Leve', 'O alvo fica com −2 em Testes de Resistência até o fim do próximo turno dele.'],
    ['Sobrecarga', 'Leve', 'Até o fim do próximo turno do alvo, o feitiço dele custa o dobro de energia e sai com a CD 2 menor.'],
    ['Firmeza', 'Média', 'O alvo tem vantagem no próximo Teste de Resistência dele.'],
    ['Guarda', 'Média', 'Até o fim do próximo turno, o alvo tem +2 de defesa.'],
    ['Pressa', 'Média', 'O alvo ganha +6 m de deslocamento e não provoca ataques de oportunidade até o fim do próximo turno.'],
    ['Enfraquece', 'Média', 'O dano do alvo cai um quarto até o fim do próximo turno dele.'],
    ['Ecoa', 'Média', 'O próximo ataque de um aliado contra o alvo tem vantagem.'],
  ]),

  H2('Castigo'),
  CAT([
    ['Queima', 'Média', 'Metade dos dados de novo, no começo do próximo turno do alvo.'],
    ['Acúmulo', 'Média', '+1 dado por rodada seguida usando este feitiço no mesmo alvo. Para de somar em +3.'],
    ['Remate', 'Média', '+25% de dano contra alvo abaixo de metade da vida. Não entra num feitiço que tenha uma Condicional ligada à vida do alvo.'],
    ['Estilhaço', 'Leve', 'Em crítico, ou quando o alvo erra o Teste de Resistência por 5 ou mais, metade dos dados respinga em quem estiver do lado.'],
    ['Quebra Coisa', 'Leve', 'Dano dobrado contra barreiras, objetos e estruturas.'],
    ['Rasga Escudo', 'Média', 'O dano ignora pontos de vida temporários e barreiras: bate direto na vida.'],
    ['Sem Cura', 'Média', 'O alvo não pode receber cura até o fim do próximo turno dele.'],
  ]),

  H2('Tempo'),
  CAT([
    ['Rápido', 'Pesada', 'Custa Ação Bônus em vez de Ação Padrão. Não entra no mesmo feitiço que Reação.'],
    ['Reação', 'Pesada', 'Você conjura como Reação, a um gatilho que você declara quando monta o feitiço. Não entra no mesmo feitiço que Rápido.'],
    ['Armado', 'Leve', 'Deixa o feitiço pronto e dispara depois, na mesma cena. Disparar ainda gasta ação.'],
    ['Silencioso', 'Leve', 'Sem gesto, sem palavra. Ninguém percebe que você conjurou.'],
    ['Adianta', 'Média', 'Se você conjurar antes de qualquer inimigo agir na rodada, +2 na CD.'],
    ['Segura', 'Leve', 'Você pode adiar o efeito por até uma rodada e disparar no seu próximo turno, de graça.'],
  ]),
  BOX(null, [
    'Se você conjurar um feitiço como Ação Bônus ou Reação, o único outro feitiço que cabe naquele turno é de **Classe 0**.',
  ]),

  H2('Marca'),
  CAT([
    ['Marca', 'Leve', 'O alvo fica marcado até o fim do seu próximo turno. **Você** tem vantagem no seu próximo ataque contra ele. Só você.'],
    ['Rastro', 'Leve', 'Você sabe onde o alvo está por 1 hora, desde que ele esteja no mesmo plano.'],
    ['Sugar', 'Média', 'Você recupera um quarto do dano causado, até no máximo 5 × Classe.'],
    ['Isca', 'Leve', 'Até o fim do próximo turno do alvo, ele tem desvantagem em qualquer ataque que não mire você.'],
    ['Cobrança', 'Média', 'Se o alvo cair nesta cena, o seu próximo feitiço custa metade.'],
    ['Aviso', 'Leve', 'Você sabe qual foi o último feitiço que o alvo usou e de que Classe ele era.'],
  ]),

  H2('Amparo'),
  P('Funcionam com as Formas Cura, Apoio e Onda e, quando fizer sentido, em feitiço de dano que atinja aliados.'),
  CAT([
    ['Limpa', 'Média', 'Remove de um aliado uma condição de nível Leve ou Média.'],
    ['Limpa Fundo', 'Pesada', 'Remove de um aliado uma condição de qualquer nível.'],
    ['Levanta', 'Pesada', 'Um aliado caído em 0 pontos de vida volta com 5 × Classe. Uma vez por cena.'],
    ['Divide', 'Média', 'Um aliado a até 9 m passa a receber metade do dano que você receberia, até o fim do próximo turno. Você escolhe na hora de conjurar.'],
    ['Junto', 'Leve', 'A cura ou o apoio pega um aliado a mais. O efeito é dividido entre eles. Pode comprar duas vezes.'],
    ['Reserva', 'Média', 'A cura fica guardada no aliado e é usada sozinha quando ele cair abaixo da metade da vida. Dura até o fim da cena.'],
    ['Remenda', 'Pesada', 'Devolve 5 × Classe de Integridade a um aliado, e com ela a vida máxima que tinha sido derrubada. Uma vez por cena.'],
  ]),

  H2('Fora de família'),
  CAT([
    ['Efeito Próprio', 'o mestre decide', 'Uma mecânica que não existe em lugar nenhum desta lista. Um deslocamento junto com o dano, um efeito que só funciona em superfície molhada, o que for. Um por feitiço, combinado antes da sessão e nunca no meio dela. Não pertence a nenhuma Família, então Família Fechada não bloqueia.'],
  ]),
  GAP(100),
  P('A Restrição equivalente — a **Restrição Própria** — está no fim da seção 4.'),
];

const restricoes = [
  H1('4 · Restrições'),
  P('Restrição é a desvantagem que você aceita em troca de pontos. Um feitiço carrega no máximo duas, e a devolução total não passa de **2 × Classe**. O que a Restrição devolve serve só pra pagar Melhoria: se devolver mais do que você gastou, o excedente se perde — Restrição nunca vira dano.'),
  P('Uma Restrição devolve **Leve** ou **Média**, nunca Pesada. Duas Médias já batem no teto de devolução da Classe, então o catálogo inteiro cabe dentro do fecho.'),
  TBL(['Restrição', 'Devolve', 'O que muda'],
    [
      ['Corpo a Corpo', 'Média', 'Projétil vira Toque (1,5 m). Explosão vira Aura, centrada em você. Cone e Linha já saem de você, então não podem pegar esta.'],
      ['Lento', 'Média', 'Custa a rodada inteira (Ação Completa): você não se move, não usa ação bônus e não faz mais nada naquele turno.'],
      ['Parado', 'Leve', 'Você não se move no turno em que conjura. A ação bônus continua sua.'],
      ['Gesto', 'Leve', 'Precisa das duas mãos livres e de falar em voz audível.'],
      ['Sangra', 'Média', 'Você toma 2 × Classe de dano que nada reduz.'],
      ['Recuo', 'Leve ou Média', 'Você fica com uma condição até o fim do seu próximo turno. Ela devolve o nível dela: uma condição Leve devolve Leve, uma Média devolve Média. Nível Pesada não entra, porque Restrição nunca devolve Pesada.'],
      ['Carregar', 'Média', 'Você gasta um turno carregando o feitiço antes de disparar. Se tomar dano nesse meio-tempo, faz um Teste de Resistência Espírito (CD 10, ou metade do dano, o que for maior) pra manter. Se falhar, perde o feitiço. Carregar não é concentração: o feitiço ainda não saiu.'],
      ['Tudo ou Nada', 'Leve', 'Quem passa no Teste de Resistência não toma nada, em vez de tomar metade. Só em feitiços de TR.'],
      ['Uma Vez', 'Leve', 'Uma vez por cena.'],
      ['Condicional', 'Leve ou Média', 'Só funciona quando uma condição de cena ou de alvo, escrita na ficha, é verdadeira: no escuro, marcado por você, abaixo de metade da vida, perto de água corrente. Falha em menos de uma cena a cada três: devolve Leve. Falha na maioria das cenas: devolve Média.'],
      ['Fraqueza', 'Leve ou Média', 'Depois de usar, você fica com desvantagem num dos quatro Testes de Resistência, escolhido na montagem, até o fim da cena. Vigor ou Intelecto: Leve. Físico ou Espírito: Média.'],
      ['Frágil', 'Leve', 'Se você tomar dano antes do seu próximo turno, o efeito do feitiço acaba na hora. Só serve em feitiço que deixa algo durando.'],
      ['Barulho', 'Leve', 'Todo mundo num raio de 90 m ouve, e sabe de onde veio.'],
      ['Assinatura', 'Leve', 'O feitiço deixa uma marca visível que dura 1 hora e aponta pra você.'],
      ['Aquecer', 'Leve', 'Não pode ser usado na primeira rodada do combate.'],
      ['Dívida', 'Média', 'Depois de usar, o próximo feitiço que você conjurar nesta cena custa o dobro de energia.'],
      ['Peso Morto', 'Leve', 'Seu deslocamento cai pela metade até o fim do próximo turno.'],
      ['Sem Volta', 'Média', 'Se o feitiço não acertar ninguém, você não conjura nada no seu próximo turno.'],
    ],
    RW, { boldCols: [0], centerCols: [1] }
  ),
  GAP(100),

  H2('Restrição Própria'),
  P('Se a desvantagem que você imaginou não está na lista, escreva ela. A Restrição Própria é o espelho do Efeito Próprio da seção 3: você propõe a dor, o mestre define quanto ela devolve.'),
  TBL(['Restrição', 'Devolve', 'O que muda'],
    [
      ['Restrição Própria', 'Leve ou Média', 'Uma desvantagem que não existe nesta lista. Escrita com o mestre antes da sessão, nunca no meio dela, e vale só pro feitiço onde nasceu. Conta no limite de duas Restrições e obedece as mesmas travas de todas as outras.'],
    ],
    RW, { boldCols: [0], centerCols: [1] }
  ),
  GAP(120),
  P('**Quanto ela devolve.** A pergunta é uma só: em quantas cenas isso vai realmente atrapalhar?'),
  BUL('Atrapalha em menos de uma cena a cada três: **Leve**.'),
  BUL('Atrapalha na metade das cenas ou mais: **Média**.'),
  BUL('Não dá pra imaginar uma cena em que atrapalhe: **não devolve nada**, e não vale como Restrição.'),
  GAP(60),
  P('Nenhuma Restrição do manual devolve Pesada, e a Própria também não. Não é acaso: duas Médias já batem exatamente no teto de devolução da Classe (2 × Classe), então uma Pesada estouraria o fecho do sistema. Se a dor que você escreveu parece valer mais que uma Média, ela provavelmente são duas Restrições disfarçadas de uma — separe.'),
  BOX('NA DÚVIDA, PRA QUE LADO ERRAR', [
    'Efeito Próprio na dúvida é **Pesada**. Restrição Própria na dúvida é **Leve**.',
    'Os dois erram pro mesmo lado: o que não infla o feitiço. Uma Melhoria cara e uma Restrição barata custam ao jogador um pouco de orçamento; o contrário custa o balanço da mesa inteira.',
  ]),
  GAP(100),
  P('As travas valem igual: a Própria precisa ser uma coisa que a mesa consegue apontar acontecendo, não pode cobrar o que a outra Restrição do feitiço já cobra, e não pode repetir o que o seu Selo já obriga. Se ela limita **quando** o feitiço sai, ela conta como Restrição de frequência pra regra abaixo.'),

  H2('O que não empilha'),
  P('Restrição precisa ser uma coisa que a mesa consegue apontar acontecendo — e algumas combinações são proibidas de saída:'),
  BUL('**As suas duas Restrições não podem ser as duas de frequência.** Uma Vez, Condicional, Aquecer, Dívida — e qualquer Restrição Própria que faça a mesma coisa — limitam quando o feitiço sai; escolha no máximo uma delas. Duas juntas devolvem o orçamento inteiro em troca de um feitiço que quase nunca é conjurado — e, quando sai, é sempre o pico.'),
  BUL('**Duas Restrições não podem cobrar a mesma coisa:** dois turnos de preparo, duas condições no seu corpo, dois jeitos de te entregar. Se as duas doem no mesmo momento, a segunda não devolve nada.'),
  BUL('**Restrição que o seu Selo já obriga não devolve ponto.** O Selo é uma obrigação que você já tem; vender a mesma dor duas vezes não vale ponto novo.'),
  GAP(60),
  P('Depois de três sessões, o mestre revisa as Restrições em jogo. As que nunca atrapalharam são trocadas.'),
];

module.exports = { melhorias, restricoes };

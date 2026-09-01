// partF — seção 10 (Feitiços prontos), seção 11 (Para o mestre, com Integridade)
// e o Apêndice. Todos os 35 prontos são conferidos por matematica/pac7.py.
// v7: Fio Preso corrigido (Fica leva a duração pro degrau seguinte: até alguém
// desfazer) e as Técnicas Máximas mostram o gasto do orçamento em vez de "grátis".
const { d, C, W, P, H1, H2, H3, BUL, NUM, TBL, BOX, GAP } = require('./helpers.js');
const PW = [20, 48, 32];
const PT = (rows) => TBL(['Nome', 'Como foi montado', 'Resultado'], rows, PW, { boldCols: [0] });

const pacotes = [
  H1('10 · Feitiços prontos'),
  P('Trinta e cinco feitiços montados e conferidos, pra usar como estão ou como referência de montagem. Na coluna do meio, **−** é o que a peça custou e **+** é o que ela devolveu.'),

  H2('Classe 1 · 3 pontos · 3 PE'),
  PT([
    ['Estalo', 'Projétil', '3d8 = 13'],
    ['Chicote', 'Linha (−1)', '2d8 = 9 numa linha de 18 m'],
    ['Perfurar', 'Projétil · Precisão (−1) · Parado (+1)', '3d8 = 13, +2 no acerto'],
    ['Golpe Cru', 'Toque (Corpo a Corpo +1), sem Melhoria pra pagar', '3d8 = 13 no toque. A devolução some'],
  ]),

  H2('Classe 2 · 6 pontos · 6 PE'),
  PT([
    ['Palma Trovejante', 'Cone (−1) · Derrubado (−1) · Atrasar (+2)', '6d8 = 27 + Derrubado por uma rodada'],
    ['Lança Negra', 'Projétil · Fura (−2) · Atrasar (+2)', '6d8 = 27, fura 6 de RD. O Atrasar pagou a Fura inteira'],
    ['Faísca em Cadeia', 'Projétil · Salto (−2) · Gesto (+1)', '5d8 = 22 e 2d8 = 9 no segundo alvo'],
    ['Sopro', 'Cura (−2)', 'cura 4d8 = 18'],
    ['Vento a Favor', 'Apoio · Impulso (−1) · Pressa (−2)', '9 de vida temporária, vantagem no próximo teste, +6 m sem provocar ataque'],
  ]),

  H2('Classe 3 · 9 pontos · 9 PE'),
  PT([
    ['Marca do Carrasco', 'Projétil · Marca (−2) · Queima (−3) · Uma Vez (+2)', '6d8 = 27 e 3d8 = 13 no turno seguinte'],
    ['Domo de Gelo', 'Explosão (−2) · Terreno (−2) · Maior (−2) · Condicional: no escuro (+2)', '5d8 = 22 num raio de 4,5 m + terreno difícil por uma rodada'],
    ['Passo Cortante', 'Toque (Corpo a Corpo +3) · Passo (−2) · Precisão (−2)', '8d8 = 36 no toque, anda 6 m, +2 no acerto'],
    ['Costura', 'Cura (−3) · Limpa (−3) · Gesto (+2)', 'cura 5d8 = 22 e tira uma condição de nível Leve ou Média'],
    ['Rede', 'Explosão (−2) · Atordoado (−5) · Terreno (−2)', 'zero dano: Atordoado + terreno difícil, CD +2, tudo durando uma rodada a mais'],
    ['Hora Morta', 'Efeito · Longe (−2)', 'um quarteirão em silêncio absoluto por uma hora'],
    ['Fissura', 'Projétil · Toca a Alma (−2)', '7 dados viram 3d8 = 13 na alma'],
  ]),

  H2('Classe 4 · 12 pontos · 12 PE'),
  PT([
    ['Prisão de Sombras', 'Explosão (−2) · Atordoado (−6) · Escolher (−4) · Sangra (+4)', '4d8 = 18 + Atordoado durando uma rodada a mais; você toma 8'],
    ['Julgamento Vertical', 'Linha (−2) · Fura (−4) · Precisão (−2) · Atrasar (+4)', '8d8 = 36, fura 12 de RD, +2 na CD'],
    ['Roubo de Fôlego', 'Projétil · Sugar (−4) · Remate (−4) · Condicional: o alvo te acertou desde o seu último turno (+4)', '8d8 = 36, cura 9, +25% em alvo abaixo de metade'],
    ['Passo do Espelho', 'Toque (Corpo a Corpo +4) · Rápido (−6) · Passo (−2) · Recuo (+4)', '12d8 = 54 como Ação Bônus, no toque'],
    ['Muralha', 'Apoio · Anteparo (−4) · Guarda (−4) · Parado (+2)', 'parede com 40 de vida, aliado com +2 de defesa e 18 de vida temporária'],
    ['Maré Branca', 'Onda (−6)', 'cura 6d8 = 27 em todos os aliados num raio de 3 m'],
    ['Alinhavo', 'Cura (−4) · Remenda (−6) · Gesto (+2)', 'cura 4d8 = 18 e devolve 20 de Integridade, com a vida máxima junto'],
  ]),

  H2('Classe 5 · 15 pontos · 15 PE'),
  PT([
    ['Purga Escarlate', 'Projétil · Inescapável (−5)', '10d8 = 45 automático, sem acerto e sem resistência'],
    ['Chuva de Agulhas', 'Projétil · Rajada (−3) · Precisão (−3) · Parado (+3)', '12d8 = 54 em 6 tiros, +2 cada'],
    ['Vala Comum', 'Explosão (−3) · Maior (−3) · Derrubado (−3) · Atrasar (+5)', '11d8 = 49 num raio de 4,5 m, todos Derrubados por uma rodada'],
    ['Fim de Turno', 'Explosão (−3) · Escolher (−5) · Atrasar (+5)', '12d8 = 54 num raio de 3 m, só em quem você escolher'],
    ['Segunda Vida', 'Cura (−5) · Levanta (−8) · Uma Vez (+3) · Gesto (+3)', 'cura 8d8 = 36, ou levanta um aliado caído com 25'],
    ['Fio Preso', 'Efeito · Fica (−5)', 'um bairro de onde ninguém sai, até alguém desfazer'],
    ['Sete Palmos', 'Toque (Corpo a Corpo +5) · Toca a Alma (−3)', '15 dados viram 7d8 = 31 na alma, no toque'],
  ]),

  H2('Liberações Máximas'),
  P('Escritas antes da sessão, Classe 3 ou mais, fora da lista de feitiços conhecidos. Todas custam a rodada inteira, 50% a mais de PE e o preço escolhido na hora.'),
  P('Repare na **Rachadura**: o Atrasar devolveria 3 pontos, mas a Linha só custou 2 — e devolução nunca passa do que foi gasto em Melhoria, então o terceiro ponto some sem virar dado.'),
  PT([
    ['Golpe do Voto', 'Classe 5 · Projétil (nada mais)', '20d8 = 90, o máximo do nível 20. 23 PE'],
    ['Rachadura', 'Classe 3 · Linha (−2) · Atrasar (+3, só 2 aproveitados)', '12d8 = 54 numa linha de 18 m — o teto da Classe 3. 14 PE'],
    ['Sentença Final', 'Classe 5 · Explosão (−3) · Escolher (−5) · Atrasar (+5)', '17d8 = 76 num raio de 3 m, só em quem você escolher. 23 PE'],
  ]),

  H2('Técnicas Máximas'),
  P('Montadas com o orçamento da seção 7 — na faixa 17–20, 8 pontos nos preços da Classe 5.'),
  PT([
    ['O Fim da Linha', 'Linha (−3) · Muito Longe (−5) — 8 do orçamento', '24d8 = 108 numa linha de 60 m'],
    ['Ponto Final', 'Projétil · Fura (−5) — 5 do orçamento, 3 se perdem', '24d8 = 108 furando 15 de RD'],
  ]),
];

const mestre = [
  H1('11 · Para o mestre'),

  H2('Aprovar'),
  P('Um feitiço novo passa por estas oito perguntas — a versão em checklist das Regras de ouro:'),
  TBL(null, [
    ['☐ 1', 'Cabe na Regra do Fundamento?'],
    ['☐ 2', 'Nenhuma Melhoria nem Forma vem de Família Fechada?'],
    ['☐ 3', 'Melhorias e Restrições dentro do limite da Classe?'],
    ['☐ 4', 'As Restrições devolveram no máximo 2 × Classe, e não mais do que ele gastou em Melhoria?'],
    ['☐ 5', 'Contra um alvo, o dano para nos pontos da Classe? E o total, somando alvos e repetições, cabe em 4 × Classe? (Liberação Máxima pode chegar a 4 × Classe num alvo só.)'],
    ['☐ 6', 'Se é Liberação Máxima: é Classe 3 ou mais, e ele ainda tem essa Liberação disponível pelo nível?'],
    ['☐ 7', 'As duas Restrições são as duas de frequência, ou cobram a mesma coisa? Se sim, refaça.'],
    ['☐ 8', 'Alguma Restrição repete o que o Selo já obriga? Se sim, não devolve nada.'],
  ], [8, 92], { boldCols: [0] }),

  H2('O que depende de você'),
  TBL(['Caso', 'Pergunte', 'Resposta'],
    [
      ['Efeito Próprio · Passiva Própria', 'Em quantas cenas por arco isso vai importar?', 'Uma cena: Leve. Metade: Média. Quase toda: Pesada. Na dúvida, Pesada.'],
      ['Restrição Própria', 'Em quantas cenas isso vai realmente atrapalhar?', 'Menos de uma a cada três: Leve. Metade ou mais: Média. Nunca atrapalha: não devolve nada. Na dúvida, Leve — e nunca Pesada.'],
      ['Condicional', 'Isso vai falhar em quantas cenas?', 'Menos de uma a cada três: Leve. A maioria: Média. Nunca falha: não devolve ponto.'],
      ['Regra Própria', 'Dá pra apontar o momento exato em que dispara?', 'Se dois jogadores discordarem, está mal escrita. Reescreva antes de jogar.'],
      ['Uso Livre', 'Passa nos três testes da seção 5?', 'Rola dado, mexe em número ou passa de coisa de mão: é feitiço.'],
    ],
    [24, 32, 44], { boldCols: [0] }
  ),

  H2('Dizer não'),
  TBL(['Resposta', 'Resolve'],
    [
      ['"Isso é Classe 4, não Classe 2."', '6 de cada 10 casos'],
      ['"Isso precisa de uma Restrição pra pagar."', '2 de cada 10'],
      ['"Isso é Efeito Próprio, resolvemos fora da mesa."', '1 de cada 10'],
      ['"Isso é Família Fechada pra você."', '1 de cada 10'],
    ],
    [50, 50], { boldCols: [0] }
  ),

  H2('Vida'),
  BOX(null, ['**Vida de personagem = 20 + 8 × (nível − 1)**']),
  GAP(100),
  TBL(['Nível', '1', '5', '10', '15', '20', '25', '30'],
    [
      ['Vida', '20', '52', '92', '132', '172', '212', '252'],
      ['Maior dano num alvo, numa rodada', '13', '27', '54', '72', '90', '108', '126'],
      ['Rodadas pra cair sob foco', '1,5', '1,9', '1,7', '1,8', '1,9', '2,0', '2,0'],
    ],
    [23, 11, 11, 11, 11, 11, 11, 11], { centerCols: [1,2,3,4,5,6,7], boldCols: [0] }
  ),
  GAP(100),
  P('A linha do meio é o maior dano que **um alvo** leva numa rodada. Antes do nível 10 não existe Liberação Máxima, então esse pico é o de um feitiço comum: os pontos da Classe. Do 10 em diante o pico é a Liberação — e ela é um recurso contado: no nível 20 são duas escritas na ficha.'),

  H2('Integridade'),
  BOX(null, [
    '**Integridade = vida máxima.** É a vida da alma.',
    'Isso vale para inimigo e para tudo que não seja personagem jogador. **Personagem tem fórmula própria**, com um atributo dentro, e quem é dono dela é o sistema em volta — é o que impede corpo duro de vir com alma dura de graça.',
  ]),
  GAP(100),
  BUL('Cada ponto de dano na alma tira 1 de vida, 1 de Integridade e derruba a sua vida máxima em 1, até o próximo descanso longo. Cura não devolve o que a alma perdeu: só descanso longo, ou a Melhoria **Remenda**.'),
  BUL('Dano na alma entra cheio, sem redução pela metade. Ao receber, faça um **Teste de Resistência de Espírito** contra a CD do atacante: no fracasso, você também avança um estágio na hora, mesmo que a fração ainda não tenha fechado.'),
  BUL('Nenhum feitiço passa de **2 × Classe** em dados na alma.'),
  BUL('Descanso longo devolve toda a Integridade e a vida máxima, e limpa os estágios.'),
  GAP(100),
  TBL(['Integridade perdida', 'Estágio', 'O que pega'],
    [
      ['1/4', '1', 'Desvantagem em testes de perícia.'],
      ['1/2', '2', 'Deslocamento pela metade, e todo feitiço custa +1 PE por Classe.'],
      ['3/4', '3', 'Desvantagem em ataques e Testes de Resistência. Você não conjura acima de metade da sua Classe máximo.'],
      ['Toda', '4', 'Você não é mais você. O que sobra é decisão do mestre.'],
    ],
    [20, 12, 68], { boldCols: [0], centerCols: [0, 1] }
  ),

  H2('Inimigos'),
  TBL(['Nível do grupo', 'Dano do grupo por rodada', 'Chefe sozinho: vida', 'Chefe: dano', 'Capanga: vida', 'Capanga: dano'],
    [
      ['2', '~38', '125 a 150', '6', '—', '—'],
      ['5', '~90', '300 a 360', '15', '40', '8'],
      ['10', '~130', '430 a 520', '26', '70', '14'],
      ['15', '~180', '600 a 720', '38', '110', '20'],
      ['20', '~220', '730 a 880', '49', '150', '26'],
      ['25', '~275', '910 a 1100', '61', '190', '32'],
      ['30', '~315', '1050 a 1260', '72', '220', '38'],
    ],
    [17, 21, 20, 15, 14, 13], { centerCols: [0,1,2,3,4,5], boldCols: [0] }
  ),
  GAP(100),
  P('A conta supõe quatro personagens: um focado em bater, dois medianos, um de apoio.'),
  P('A faixa mais baixa não tem capanga, e isso é decisão: com o corpo que a proporção daria, dois deles cairiam na primeira rodada de um grupo que causa 38 por rodada — aí ele é uma rolagem a mais e não um corpo. Do nível 2 ao 4 o encontro é um inimigo só.'),
  P('Cada linha vale para a faixa de Classe dela, e não só para aquele nível: a do 2 cobre o nível 2 ao 4, a do 5 cobre até o 8, a do 10 até o 12, e assim por diante. Dentro da faixa o grupo ganha vida e o inimigo não, então o encontro afrouxa — se quiser manter o aperto no fim da faixa, acrescente capangas.'),
  P('Chefe sozinho precisa de três a quatro vezes o dano de rodada do grupo, porque ele perde a ação três vezes por rodada. Se não quiser inflar o número, use capangas ou uma barreira que absorva antes da vida.'),
  GAP(100),
  P('E a ficha dele carrega mais duas coisas, que são de marcar e não de calcular:'),
  BUL('**Integridade.** A do inimigo é a que a seção acima escreve: a vida máxima dele, então a coluna de vida serve para as duas barras. Anote as duas assim mesmo — o sistema em volta tem efeito que tira alma sem tirar vida, e é aí que os dois números se separam.'),
  BUL('**Reação.** Uma por rodada, como qualquer personagem, e ela volta no começo do turno dele. Ela paga o ataque de oportunidade, e o sistema em volta pendura outras coisas nela. Marque quando for gasta: guardar ou não é decisão do inimigo do mesmo jeito que é da mesa.'),

  H2('PvP'),
  BOX(null, ['Em duelo entre personagens, o dano de feitiço cai **um terço**.']),
  GAP(100),
  TBL(['Nível', 'Vida', 'Pico normal', 'Rodadas', 'Com o corte', 'Rodadas'],
    [
      ['10', '92', '54', '1,7', '36', '2,6'],
      ['20', '172', '90', '1,9', '60', '2,9'],
      ['30', '252', '126', '2,0', '84', '3,0'],
    ],
    [15, 15, 18, 16, 18, 18], { centerCols: [0,1,2,3,4,5], boldCols: [0] }
  ),

  H2('A curva'),
  TBL(['Nível', 'Classe', 'Rotina', 'Feitiço num alvo', 'Somando alvos', 'Liberação', 'Téc. Máxima'],
    [
      ['1 a 4', '1', '3d8 = 13', '3d8 = 13', '4d8 = 18', '—', '—'],
      ['5 a 8', '2', '6d8 + 1d8 = 31', '6d8 = 27', '8d8 = 36', '—', '—'],
      ['9 a 12', '3', '9d8 + 1d8 = 45', '9d8 = 40', '12d8 = 54', '12d8 = 54', '—'],
      ['13 a 16', '4', '12d8 + 2d8 = 63', '12d8 = 54', '16d8 = 72', '16d8 = 72', '—'],
      ['17 a 20', '5', '15d8 + 2d8 = 76', '15d8 = 67', '20d8 = 90', '20d8 = 90', '24d8 = 108'],
      ['21 a 25', '6', '18d8 + 3d8 = 94', '18d8 = 81', '24d8 = 108', '24d8 = 108', '28d8 = 126'],
      ['26 a 30', '7', '21d8 + 3d8 = 108', '21d8 = 94', '28d8 = 126', '28d8 = 126', '32d8 = 144'],
    ],
    [11, 7, 21, 18, 16, 15, 16], { centerCols: [0,1,2,3,4,5,6], boldCols: [0] }
  ),
  GAP(100),
  P('As colunas saíram de rodar todas as combinações que o sistema permite. **Feitiço num alvo** para nos pontos da Classe. **Somando alvos** é o teto de 4 × Classe, alcançado espalhando o dano com Salto, Rajada, Mais Um ou Queima. **Liberação** entrega o teto inteiro num alvo só, e cada personagem tem no máximo três delas escritas.'),
  P('A única peça que empurra um feitiço comum acima dos pontos da Classe contra um alvo é **Remate**, que soma 25% contra alvo abaixo de metade da vida. No Classe 5 isso leva 15d8 de 67 pra 84, ainda abaixo dos 90 da Liberação, e só contra alvo já ferido.'),
  P('Se a sua mesa tem um tipo de personagem que bate em vez de conjurar, o dano dele por rodada precisa ficar na coluna Rotina, e ele não deve ter Liberação Máxima.'),
];

const apendice = [
  H1('Apêndice'),

  H2('Glossário'),
  TBL(['Termo', 'O que é'],
    [
      ['Fundamento', 'Sua técnica inata. Descrição, Regra, Famílias, Selo e Passivas.'],
      ['Regra', 'A frase que resume a técnica. Todo feitiço precisa caber nela.'],
      ['Família', 'Um dos nove grupos de Melhoria. Duas Livres e três Fechadas, todas na criação.'],
      ['Selo', 'Gesto ou condição obrigatória pra conjurar, igual pra todos os seus feitiços. Não custa nem devolve ponto.'],
      ['Classe', 'O tamanho do feitiço, de 0 a 7. Define pontos, teto, PE e limites.'],
      ['Pontos', 'O orçamento do feitiço. 3 × Classe. Cada ponto que sobra vira 1d8.'],
      ['Teto', 'O máximo de dados de dano do feitiço, somando alvos e repetições. 4 × Classe.'],
      ['Forma', 'Como o feitiço sai: Projétil, Toque, Explosão, Aura, Cone, Linha, Cura, Apoio, Onda, Efeito.'],
      ['Melhoria', 'O que você compra com ponto. Custa Leve, Média ou Pesada.'],
      ['Restrição', 'O que você vende pra recuperar ponto. Paga Melhoria, nunca dano. Devolve Leve ou Média — nunca Pesada.'],
      ['Liberação Máxima', 'Feitiço à parte, escrito antes da sessão, de Classe 3 ou mais. Soma +Classe em dados, custa a rodada inteira, 50% mais PE e um preço escolhido na hora: Vazio, Sangue ou Peso. Uma no nível 10, outra no 20, outra no 30.'],
      ['Ampliar', 'Lançar um feitiço conhecido numa Classe maior, pagando o PE daquela Classe.'],
      ['Passiva', 'Efeito que fica ligado sozinho. Tem Classe de Livre a 3 e custa espaço de feitiço.'],
      ['Uso Livre', 'O que a sua técnica faz de graça fora de combate.'],
      ['Técnica Máxima', 'O golpe de dano fixo do nível 17 em diante. Volta depois do fim do seu terceiro turno seguinte.'],
      ['Integridade', 'A vida da alma. Igual à vida máxima em inimigo; personagem tem fórmula própria, e o dono dela é o sistema em volta. Só volta com descanso longo ou com a Melhoria Remenda.'],
      ['Dano na alma', 'Tira vida, Integridade e vida máxima no mesmo tanto. Entra cheio, e o Teste de Resistência decide o estágio, não o número.'],
    ],
    [20, 80], { boldCols: [0] }
  ),

  H2('Tabela de bolso'),
  TBL(['Classe', 'Pontos e PE', 'Leve', 'Média', 'Pesada', 'Devol.', 'Liberação', 'Teto', 'Melhorias', 'Dano', 'Cura'],
    [
      ['1', '3', '1', '1', '2', '2', '+1', '4', '2', '3d8 = 13', '2d8 = 9'],
      ['2', '6', '1', '2', '3', '4', '+2', '8', '2', '6d8 = 27', '4d8 = 18'],
      ['3', '9', '2', '3', '5', '6', '+3', '12', '3', '9d8 = 40', '6d8 = 27'],
      ['4', '12', '2', '4', '6', '8', '+4', '16', '3', '12d8 = 54', '8d8 = 36'],
      ['5', '15', '3', '5', '8', '10', '+5', '20', '4', '15d8 = 67', '10d8 = 45'],
      ['6', '18', '3', '6', '9', '12', '+6', '24', '4', '18d8 = 81', '12d8 = 54'],
      ['7', '21', '4', '7', '11', '14', '+7', '28', '4', '21d8 = 94', '14d8 = 63'],
    ],
    [6, 11, 6, 7, 8, 8, 8, 6, 11, 15, 14], { centerCols: [0,1,2,3,4,5,6,7,8,9,10], boldCols: [0] }
  ),

  H2('Ficha de feitiço'),
  TBL(null, [
    ['Nome', ''],
    ['Classe / Pontos / Teto / PE', ''],
    ['Forma', 'Projétil · Toque · Explosão · Aura · Cone · Linha · Cura · Apoio · Onda · Efeito'],
    ['Resolve com', 'Acerto · Teste de Resistência · Automático'],
    ['Melhorias', ''],
    ['Restrições', ''],
    ['É Liberação Máxima?', 'Sim ☐   Não ☐        Preço na hora: Vazio · Sangue · Peso'],
    ['Dano ou cura', '____ d8  =  ____'],
    ['Ação', 'Padrão · Bônus · Reação · Rodada inteira'],
    ['Como é', ''],
  ], [26, 74], { boldCols: [0] }),

  H2('Catálogo de temas'),
  P('Setenta pontos de partida pra escrever a sua Regra. Não têm regra nenhuma amarrada, são só ideias.'),
  TBL(['Grupo', 'Temas'],
    [
      ['Corpo e matéria', 'Corte · Impacto · Perfuração · Peso · Elasticidade · Carne · Sangue · Osso · Doença · Crescimento'],
      ['Elementos', 'Fogo · Gelo · Raio · Vento · Água · Terra · Metal · Ácido · Veneno · Fumaça'],
      ['Força e movimento', 'Gravidade · Vetor · Velocidade · Inércia · Rotação'],
      ['Espaço e tempo', 'Distância · Espaço · Tempo · Direção · Reflexo'],
      ['Sentidos', 'Som · Silêncio · Luz · Sombra · Cheiro'],
      ['Mente e alma', 'Medo · Memória · Sono · Ilusão · Voz · Nome · Emoção · Vontade · Instinto · Loucura'],
      ['Conceito', 'Vínculo · Troca · Cópia · Contrato · Dívida · Sorte · Aposta · Julgamento · Regra · Registro · Valor · Verdade · Segredo · Herança · Ausência'],
      ['Criação', 'Invocação · Construção · Marionete · Ferramenta · Selamento · Bloqueio · Semente · Enxame · Máquina · Molde'],
    ],
    [20, 80], { boldCols: [0] }
  ),
  GAP(100),
  P('Os do grupo Conceito quase sempre pedem uma Passiva de Regra Própria pra funcionarem bem.'),

  H2('Regras de ouro'),
  BUL('Restrição paga Melhoria. Nunca vira dano.'),
  BUL('Dano total nunca passa de 4 × Classe. Num alvo só, feitiço comum para nos pontos da Classe.'),
  BUL('Melhorias: 2 nas Classes 1–2, 3 nos 3–4, 4 do 5 em diante. Restrições: até 2.'),
  BUL('Restrição devolve no máximo 2 × Classe.'),
  BUL('Liberação Máxima custa a rodada inteira, é Classe 3 ou mais, e só as que o nível deu.'),
  BUL('Feitiço em Ação Bônus ou Reação só permite mais um de Classe 0.'),
  BUL('Duas Restrições não podem ser as duas de frequência, nem cobrar a mesma coisa.'),
  BUL('Restrição que não atrapalhou em três sessões é trocada.'),
];

module.exports = { pacotes, mestre, apendice };

// partE — seções 5 a 9: Fora de combate · Liberação Máxima · Técnica Máxima ·
// Regras de ouro · Progressão.
// v7: Liberação Máxima ganhou seção própria (saiu de dentro de "Montar"), e a
// Técnica Máxima foi reescrita pra separar os três números dela (dado fixo,
// orçamento de montagem, PE). As montagens são conferidas em matematica/pac7.py.
const { d, C, W, P, H1, H2, H3, BUL, NUM, TBL, BOX, GAP } = require('./helpers.js');

const foraDeCombate = [
  H1('5 · Fora de combate'),
  P('Nem tudo que a sua técnica faz precisa de rolagem ou de montagem. Fora de combate, duas regras cobrem o resto: o Uso Livre, pra coisa pequena, e a Forma Efeito, pra coisa grande.'),

  H2('Uso Livre'),
  P('De graça e sem rolar nada, você faz qualquer coisa que caiba na sua Regra e passe nos três testes:'),
  NUM('Não rola dado e não faz ninguém rolar.', 2),
  NUM('Não tira nem dá vida, não aplica condição, não mexe em rolagem de ninguém e não move nada que resista.', 2),
  NUM('A escala cabe na Classe 0 da tabela de Efeito, logo abaixo: coisa de mão.', 2),
  GAP(80),
  P('Falhou em um dos três, é feitiço — monte e pague. Passou nos três, funciona, mesmo que resolva a cena.'),
  P('A régua geral é essa: **perceber é Livre, interferir é feitiço**. E o que você percebe vem cru — a cor do medo, não o motivo dele.'),
  TBL(['Uso Livre', 'Vira feitiço'],
    [
      ['Aquecer uma xícara', 'Aquecer uma sala inteira'],
      ['Marcar uma parede', 'Marcar uma pessoa'],
      ['Saber de onde vem o vento', 'Saber onde está uma pessoa'],
      ['Iluminar um corredor', 'Cegar quem está no corredor'],
      ['Ver a cor da emoção de alguém', 'Saber o que a pessoa vai fazer'],
      ['Fazer uma folha cair mais devagar', 'Fazer uma pessoa cair mais devagar'],
      ['Abafar o som dos seus passos', 'Abafar o som de uma sala'],
      ['Achar a fechadura no escuro', 'Abrir a fechadura sem chave'],
      ['Saber se mexeram num objeto seu', 'Saber quem mexeu'],
      ['Estabilizar a própria mão', 'Estabilizar a mão de outra pessoa'],
    ],
    [50, 50], { }
  ),

  H2('Forma Efeito'),
  P('Quando a coisa é grande o bastante pra mudar uma cena, monte um feitiço com a **Forma Efeito**. Ele não causa dano e não rola dado: a Classe define sozinho o que o efeito alcança e por quanto tempo dura, pela tabela abaixo.'),
  P('Num feitiço de Efeito, os pontos da Classe servem só pra comprar Melhorias. Ponto que sobrar não vira nada — a escala já está paga pela Classe.'),
  TBL(['Classe', 'O que cabe', 'Quanto dura'],
    [
      ['0', 'Coisa de mão: acender uma vela, trancar uma porta, marcar um objeto.', 'até você desfazer'],
      ['1', 'Uma pessoa, um objeto pequeno, um cômodo apertado.', 'um minuto'],
      ['2', 'Um cômodo grande, uma parede, um carro, meia dúzia de pessoas.', 'dez minutos'],
      ['3', 'Uma casa, um quarteirão, uma dúzia de pessoas.', 'uma hora'],
      ['4', 'Um prédio, uma rua inteira, uma multidão.', 'um dia'],
      ['5', 'Um bairro, uma noite inteira, o clima do lugar. Um prédio dormindo ao mesmo tempo, um rio parando de correr, uma ponte que não deixa ninguém passar.', 'uma semana'],
      ['Máxima', 'Uma cidade, uma coisa que vira notícia. Todo mundo esquecendo um nome, um bairro de onde ninguém sai, uma noite que não amanhece.', 'até alguém desfazer'],
    ],
    [10, 60, 30], { boldCols: [0], centerCols: [0] }
  ),
  GAP(120),
  P('Melhorias funcionam normalmente: **Longe** e **Maior** sobem alcance e escala, **Fica** estende a duração pro degrau seguinte da tabela, **Silencioso** esconde a conjuração.'),
  P('Feitiço de Efeito custa PE igual a qualquer outro e ocupa espaço na sua lista.'),
  BOX('Exemplo', [
    '**Hora Morta** · Classe 3 · Efeito · Longe (−2)',
    'Um quarteirão inteiro para de fazer barulho por uma hora. Portas não rangem, tiro não estala, ninguém grita alto o bastante pra ser ouvido de fora. Custa 9 de PE.',
  ]),
];

const liberacao = [
  H1('6 · Liberação Máxima'),
  P('No nível 10, o personagem aprende a romper o próprio limite. A Liberação Máxima é o único feitiço capaz de passar dos pontos da Classe em dano contra um alvo só — é o pico de dano que a ficha alcança, e por isso ela é contada: você só tem as que os níveis deram.'),
  P('Liberação não se improvisa. Ela é escrita antes da sessão, montada como qualquer feitiço, e fica anotada na ficha com nome próprio.'),
  BOX('LIBERAÇÃO MÁXIMA', [
    'Você ganha uma no **nível 10**, outra no **20** e outra no **30**.',
    'Cada uma é um feitiço de **Classe 3 ou mais**, montado normalmente, que **não ocupa espaço** na sua lista de feitiços conhecidos.',
    '**+Classe em dados de dano** em cima do que a montagem der. Num Classe 5, +5d8.',
    'Custa a rodada inteira e **+50% de PE**, arredondando pra cima.',
    'Escolha o preço na hora de disparar:',
    '**Vazio**: você não conjura nada no seu próximo turno.',
    '**Sangue**: você toma 3 × Classe de dano que nada reduz.',
    '**Peso**: você fica Lento e com desvantagem em Testes de Resistência até o fim do seu próximo turno.',
    'Não serve pra cura, e a Técnica Máxima não é uma Liberação.',
  ], 'warn'),
  GAP(100),
  P('Fora isso, ela é um feitiço como os outros: aceita Melhorias e Restrições dentro dos limites da Classe, obedece a Regra e as Famílias Fechadas, e pode ser Ampliada. Ao subir de nível, você pode reescrevê-la do zero, como qualquer feitiço.'),
  BOX('Exemplo', [
    '**Golpe do Voto** · Liberação Máxima · Classe 5 · Projétil',
    'Sem Melhoria e sem Restrição: os 15 pontos viram 15d8, e a Liberação soma +5d8.',
    '',
    '**20d8 = 90 de dano**, o pico do nível 20. PE: 15 + 50% = 22,5, arredondando pra cima: **23**. Rodada inteira, mais o preço escolhido na hora.',
  ]),
];

const maxima = [
  H1('7 · Técnica Máxima'),
  P('No nível 17, a técnica ganha o golpe que carrega o nome dela. A Técnica Máxima não é montada como um feitiço: o dano dela é **fixo**, definido pela sua faixa de nível, e nenhum ponto compra dado a mais. O que você monta é o resto — a Forma e as Melhorias que vestem esse dano.'),
  TBL(['Nível', 'Dano (fixo)', 'Pontos de montagem', 'PE'],
    [['17 a 20', '24d8 = 108', '8', '25'], ['21 a 25', '28d8 = 126', '8', '30'], ['26 a 30', '32d8 = 144', '12', '35']],
    [24, 30, 32, 14], { centerCols: [0,1,2,3], boldCols: [0] }
  ),
  GAP(120),
  BOX('TRÊS NÚMEROS, TRÊS PAPÉIS', [
    '**O dano é fixo.** Os 24d8 da faixa 17–20 já vêm prontos: você não compra dado, não vende dado, e Restrição não entra aqui.',
    '**Os pontos de montagem compram só a Forma e as Melhorias.** Eles não são os pontos de uma Classe: são um orçamento à parte, gasto nos preços da sua **maior Classe**. Na faixa 17–20, isso significa preços de Classe 5: Leve 3, Média 5, Pesada 8. Ponto de montagem que sobrar se perde — não vira dado.',
    '**O PE tem fórmula própria.** A Técnica Máxima não tem Classe, então não custa 3 × Classe como um feitiço: custa **5 × a sua maior Classe** — 25, 30 e 35 PE por faixa.',
  ]),
  GAP(100),

  H2('Como montar'),
  NUM('Escolha a **Forma**. Projétil e Toque são de graça; as outras custam o preço normal delas, pago do orçamento de montagem.', 3),
  NUM('Gaste o resto do orçamento em **Melhorias**, nos preços da sua maior Classe. Melhoria que escala com Classe — como Fura, que ignora 3 × Classe de RD — também usa a sua maior Classe.', 3),
  NUM('Dê um nome e escreva na ficha. Como a Liberação, a Técnica Máxima não se improvisa na mesa.', 3),
  GAP(120),
  BUL('Custa **a rodada inteira** e 5 × a sua maior Classe de PE.'),
  BUL('Depois de usar, você só usa de novo depois do fim do seu **terceiro turno seguinte**.'),
  BUL('Aceita qualquer Forma. Numa Forma que não causa dano, os dados viram escala pela linha Máxima da tabela de Efeito (seção 5), ou viram cura.'),
  BUL('**Não aceita Restrição**, e não é uma Liberação Máxima: os dados dela já são fixos.'),
  BUL('Quem passa no Teste de Resistência reduz o dano em **um quarto**, não pela metade.'),
  BUL('Famílias Fechadas continuam fechadas.'),
  BUL('Se a sua mesa quiser que pese mais, use uma vez por cena em vez do recarregamento por turnos.'),
  GAP(100),
  BOX('Exemplo: duas Técnicas Máximas da faixa 17–20', [
    '**O Fim da Linha** — Forma Linha (Leve na Classe 5: 3 pontos) + Muito Longe (Média: 5 pontos) = 8 dos 8 pontos de montagem. A linha sobe da base de 18 m até o fim da escada: 60 m.',
    '**24d8 = 108 de dano** em tudo na linha. Rodada inteira, 25 de PE.',
    '',
    '**Ponto Final** — Projétil (grátis) + Fura (Média: 5 pontos) = 5 dos 8; os 3 que sobram se perdem.',
    '**24d8 = 108**, ignorando 15 de Redução de Dano (3 × Classe 5). Rodada inteira, 25 de PE.',
  ]),
  GAP(100),
  P('**Expansão de Domínio não é a Técnica Máxima.** As duas são coisas diferentes: a Técnica Máxima é o topo da sua técnica inata, e o domínio é a mesma técnica estendida sobre o território em volta. Uma técnica feita de domínio continua tendo Técnica Máxima como qualquer outra.'),

  H2('Expansão de Domínio'),
  P('Estender a sua técnica sobre o terreno: por alguns instantes, o lugar em volta deixa de obedecer ao mundo e passa a obedecer a você. É o topo do que um feiticeiro faz, e quase nenhum chega lá.'),
  P('Ela **não é montada com pontos** como um feitiço, e **não é dada pelo nível** como a Técnica Máxima. Ela é **comprada**, com espaços de feitiço conhecido, e só abre quando o seu nível e o seu **refino** alcançam os dois mínimos.'),
  BOX('REFINO, EM UMA LINHA', [
    'O **refino** é o eixo de controle da sua ficha — quanto da sua energia você não desperdiça. Ele não é do Fundamento: ele mora no sistema em volta, sobe com os seus marcos e vai de 1 a 10. Aqui ele é lido em quatro lugares e nada mais: **o requisito**, **o desconto lá dentro**, **quanto tempo o domínio fica de pé** e **quem conquista quando dois domínios se sobrepõem.**',
  ]),
  GAP(100),

  H3('Os dois degraus'),
  TBL(['Degrau', 'Custa', 'Abre em', 'O Acerto dela'],
    [
      ['Incompleta', '2 espaços', 'nível 10 e refino 4', 'resolve por rolagem, como um feitiço'],
      ['Completa', '3 espaços (+1)', 'nível 14 e refino 5', '**acontece.** Sem rolagem e sem Teste de Resistência'],
    ],
    [16, 16, 24, 44], { boldCols: [0] }
  ),
  GAP(120),
  BUL('**A completa exige ter a incompleta**, e paga só a diferença — um espaço a mais, no molde da Regra Própria.'),
  BUL('**Só a completa fecha barreira.** A incompleta é a técnica derramada no terreno, sem parede em volta.'),
  BUL('O teto do feitiço não muda por causa dela, e as duas ficam **fora** da conta de Liberações Máximas.'),
  GAP(100),

  H3('O que você escreve: o Acerto e o Efeito'),
  P('Um domínio tem duas peças, e elas fazem coisas diferentes. Escreva as duas com o mestre antes da campanha, uma frase cada, e as duas precisam caber na **Regra** da sua técnica.'),
  TBL(['Peça', 'A pergunta que ela responde'],
    [
      ['**Acerto**', 'O que o domínio *garante que acontece* com quem está lá dentro.'],
      ['**Efeito**', 'O que o domínio *permite você fazer* lá dentro que você não faria fora.'],
    ],
    [16, 84]
  ),
  GAP(120),
  P('**O Acerto vem em três formas, e a sua é uma delas:** o que a sua técnica já faz passa a acertar · todos no ambiente recebem alguma coisa · ninguém no ambiente pode fazer alguma coisa.'),
  GAP(80),
  BOX('DUAS RÉGUAS PARA O ACERTO, E ELAS JÁ EXISTEM NESTE MANUAL', [
    '**Se o seu Acerto é dano que sempre acerta**, a régua é a Melhoria **Inescapável**: ela custa uma Média e proíbe o feitiço de ter qualquer outra peça. Um Acerto que entrega dano garantido paga o mesmo tipo de preço — ele é o feitiço inteiro, e não sobra orçamento para mais nada em cima.',
    '**Se o seu Acerto é uma regra sobre o ambiente**, a régua são os requisitos da **Regra Própria** (seção 1): uma frase, verificável, sem número solto. O mestre aponta o momento em que ela vale, e ela vale igual para todo mundo lá dentro — inclusive para você.',
    'A diferença entre as duas não é de tamanho. É de que máquina o mestre usa para dizer sim ou não.',
  ]),
  GAP(100),

  H3('Abrir, e o que muda lá dentro'),
  BUL('**Custa a rodada inteira**, e as duas cobram **6 × a sua maior Classe** de PE. O degrau de cima já se pagou no espaço a mais e nos dois gates.'),
  BUL('**O Acerto acontece no momento em que você abre**, e de novo no começo de cada turno seu. O relógio é o seu, e não o de quem está lá dentro.'),
  BUL('**Lá dentro os seus feitiços ficam mais baratos:** −⅓ do refino de PE na incompleta, **−metade do refino** na completa. **Nenhum feitiço custa menos de 1 PE.**'),
  BUL('**Você pode arrastar o domínio.** Se estiver com os pés no chão, gaste o seu deslocamento e a expansão inteira vai junto — e quem está lá dentro não percebe que se mexeu.'),
  BUL('**Dura metade do refino em rodadas**, no mínimo uma.'),
  GAP(100),
  BOX('A EXPANSÃO CONTA COMO FEITIÇO PARA A REGRA DE OURO Nº 6', [
    'Se alguma coisa algum dia baixar o custo de abrir para **Ação Bônus**, a regra nº 6 passa a valer sozinha: *feitiço em Ação Bônus ou Reação só permite mais um de Classe 0 no turno.* Ou seja, quem abrir domínio em Ação Bônus não lança mais nada de peso naquele turno. Não é regra nova; é a que já está lá, e ela existe exatamente para este caso.',
  ]),
  GAP(100),

  H3('A barreira, e o Rescaldo'),
  P('Só a completa levanta barreira. Por dentro ela **não quebra** — quem está lá dentro está lá dentro. Por fora ela tem `50 × metade do refino` de vida, e cair antes da hora é o único jeito de alguém encurtar o seu domínio.'),
  P('*O mestre pode declarar que uma barreira cede fora dessa conta* — uma fraqueza que a ficção já estabeleceu, uma cena que pede. É exceção declarada, e não a régua.'),
  GAP(80),
  BOX('RESCALDO', [
    '**Quando o domínio acaba — de qualquer jeito — a sua técnica queima.** Você desfez por vontade, o tempo correu, ou estilhaçaram a barreira: dá no mesmo. Pelo resto da cena a sua técnica não responde, e você fica com o Classe 0, com o corpo e com o que não for técnica.',
    'Isso é **preço, e não risco** — acontece em todo uso, e você já sabia disso quando abriu. É o que impede o domínio de ser mais uma linha da rotação.',
    'Rescaldo **não é a exaustão do descanso**, e as duas não somam. São escadas diferentes, e esta aqui tem um degrau só.',
  ]),
  GAP(100),

  H3('Nove domínios da obra, lidos nas duas peças'),
  TBL(['Quem', 'Acerto', 'Efeito'],
    [
      ['Megumi *(incompleta)*', 'todas as invocações dele ganham reforço', 'invocar todas elas de uma vez'],
      ['Sukuna', 'clivar e desmantelar acertam', 'alcança todos no ambiente'],
      ['Mahito', 'ninguém desvia do toque dele', 'alcança todos no ambiente'],
      ['Jogo', 'queima todos no ambiente', 'amplifica a técnica'],
      ['Dagon', 'os shikigami dele acertam', 'amplifica a técnica'],
      ['Yuta', 'os feitiços das espadas acertam', 'todas as técnicas copiadas, em forma de espada'],
      ['Gojo', 'a enxurrada de informação', 'tocar em alguém para poupá-lo do Acerto'],
      ['Hakari', 'todos recebem a informação do domínio', 'o pachinko, e a regeneração que ele paga'],
      ['Higuruma', 'ninguém no ambiente pode causar dano', 'o julgamento, e as punições que ele libera'],
    ],
    [22, 38, 40], { boldCols: [0] }
  ),
  GAP(100),
  P('**Repare no que a tabela mostra sobre os dois degraus.** O Megumi é o único incompleto da lista, e o Acerto dele *reforça* em vez de *atingir* — é o que dá para fazer quando o Acerto ainda rola. Os oito completos entregam coisas que não falham, e é isso que o terceiro espaço compra.'),
  P('E repare também que **Efeito quase nunca é dano**. Alcance, repertório, amplificação, uma mecânica nova, controle sobre quem o Acerto pega. O dano, quando existe, mora no Acerto.'),
  GAP(100),

  H3('Dois domínios abertos ao mesmo tempo'),
  P('Só acontece quando as **áreas se sobrepõem**: você está dentro do domínio dele, ou ele abriu dentro do raio do seu. Abrir domínio longe de um que já está de pé não encosta nele.'),
  P('**Enquanto os dois estiverem de pé, nenhum dos dois acerta garantido.** Os dois Acertos ficam desligados, e lá dentro sobra o que não dependia deles: feitiço, corpo, e o Efeito de cada um.'),
  GAP(80),
  P('**Quem conquista sai de três perguntas, nesta ordem.** A primeira que separar decide, e as de baixo nem chegam a ser feitas.'),
  TBL(['', 'A pergunta', 'Quem leva'],
    [
      ['1', 'Quem tem mais **refino**?', 'o mais refinado conquista, e o domínio do outro cai na hora'],
      ['2', 'Refino igual — o Acerto de um dos dois **não causa dano**?', 'esse conquista: um Acerto que não fere se estabelece antes'],
      ['3', 'Iguais nas duas — os dois rolam **1d12**', 'separaram por **4 ou mais**: o maior conquista'],
      ['4', 'O d12 não separou', '**ninguém conquista ainda**, e vale a corrida abaixo'],
    ],
    [7, 45, 48], { centerCols: [0], boldCols: [0] }
  ),
  GAP(120),
  BUL('**A corrida.** Os dois domínios seguem de pé, os dois Acertos seguem desligados, e a luta corre normal. **O primeiro dos dois que perder o domínio — barreira derrubada por fora, ou o tempo acabou — ou chegar a 0 de vida recebe o Acerto do outro na hora.**'),
  BUL('**Quem perde recebe o Acerto do vencedor, e não tem como recusar.** O domínio dele já caiu, e quem cai não abre saída na barreira que continua de pé.'),
  BUL('**Nas duas saídas o Rescaldo dispara**, dos dois lados. O domínio acabou, e ele acaba de qualquer jeito.'),
  GAP(100),
  P('**Um domínio incompleto entra na disputa e não pode vencer.** Ele não fecha barreira, então não tem barreira para conquistar nem para perder. O que ele faz é o que a sobreposição já faz: **desliga o Acerto do completo, e a barreira do completo deixa de prender — quem está lá dentro pode sair** — e o Acerto dele, que rola, continua rolando. É a resposta mais cara que existe a um domínio, e a única que também é um domínio.'),
  GAP(80),
  BOX('A SEGUNDA PERGUNTA É UMA TROCA, E ELA NÃO PAGA ESCREVER ACERTO INÚTIL', [
    'Um Acerto que causa dano rende em **todo** uso do seu domínio — na abertura e no começo de cada turno seu. O desempate da pergunta 2 só rende contra **outro domínio, de refino igual ao seu**.',
    'Quem escreve um Acerto que não fere está comprando o desempate com o que a Melhoria **Inescapável** cobraria, e não ganhando de graça. É a mesma troca que o Hakari e o Higuruma fizeram na tabela acima.',
  ]),
  GAP(100),
  BOX('POR QUE 1d12 E POR QUE 4', [
    'O dado **não leva bônus**, e isso não é economia de regra: **não sobrou nada para somar nele.** Refino já empatou — é o que a pergunta 3 quer dizer. Maestria vem do nível, e os dois estão no mesmo. E o atributo da técnica bate no teto de 6 antes do primeiro clash da campanha, pelas três rotas.',
    'De todas as combinações de dado e margem, **1d12 separando por 4 é a única que cai na metade exata** — 72 dos 144 resultados. Metade das vezes o choque resolve, metade continua e vale a corrida.',
    'Você rola **uma vez**, quando as áreas se sobrepõem, e não a cada rodada. Rolar toda rodada resolveria o choque em 88% até a terceira, e aí quem está de fora batendo na barreira deixaria de decidir o combate.',
  ]),
  GAP(100),

  BOX('TRÊS OU MAIS DOMÍNIOS: CAEM TODOS', [
    'Dois domínios se empurram. **Três ou mais não se acomodam:** as condições que cada barreira exige por dentro e por fora não fecham juntas, e **todas as barreiras caem**.',
    'Ninguém conquista, ninguém recebe Acerto, e o Rescaldo pega todo mundo que abriu.',
  ]),
];

const ouro = [
  H1('8 · Regras de ouro'),
  P('Oito regras seguram o sistema inteiro. Se um feitiço passar por todas, ele é legal; o checklist do mestre na seção 11 segue exatamente esta lista.'),
  TBL(['#', 'Regra'],
    [
      ['1', 'Restrição paga Melhoria. Nunca vira dado de dano. O excedente some.'],
      ['2', 'O dano total, somando alvos e repetições, nunca passa de 4 × Classe em dados. Contra um alvo só, feitiço comum para nos pontos da Classe: 4 × Classe num alvo é coisa de Liberação Máxima.'],
      ['3', 'Melhorias: 2 nas Classes 1–2, 3 nas Classes 3–4, 4 da Classe 5 em diante. Restrições: até 2. A Forma não conta.'],
      ['4', 'Restrição devolve no máximo 2 × Classe.'],
      ['5', 'Liberação Máxima é Classe 3 ou mais, custa a rodada inteira, e você só tem as que o nível deu.'],
      ['6', 'Feitiço em Ação Bônus ou Reação só permite mais um de Classe 0 no turno.'],
      ['7', 'Duas Restrições não podem ser as duas de frequência, nem cobrar a mesma coisa.'],
      ['8', 'Restrição que não atrapalhou em três sessões é trocada.'],
    ],
    [7, 93], { centerCols: [0] }
  ),
  GAP(120),
  P('Duas notas que acompanham as oito: Restrição que o seu Selo já obriga não devolve ponto, e o mestre pode recusar qualquer feitiço, mesmo um que passe em tudo.'),
];

const progressao = [
  H1('9 · Progressão'),
  TBL(['Nível', 'O que ganha'],
    [
      ['1', 'Fundamento com três Famílias Fechadas. Dois feitiços de Classe 0 (grátis). Classe 1. Passiva Livre.'],
      ['5', 'Classe 2. Um feitiço de Classe 0 a mais.'],
      ['7', 'Libera Passiva de Classe 2.'],
      ['9', 'Classe 3.'],
      ['10', '**A primeira Liberação Máxima.**'],
      ['11', 'Um feitiço de Classe 0 a mais.'],
      ['13', 'Classe 4. Libera Passiva de Classe 3.'],
      ['17', 'Classe 5. Técnica Máxima. Um feitiço de Classe 0 a mais.'],
      ['20', '**A segunda Liberação Máxima.**'],
      ['21', 'Classe 6.'],
      ['26', 'Classe 7.'],
      ['30', '**A terceira Liberação Máxima.**'],
    ],
    [16, 84], { boldCols: [0] }
  ),
  GAP(120),
  P('**Quantos feitiços você conhece não é conta deste manual.** O Fundamento manda na Classe, na Liberação Máxima e em quando cada Classe de Passiva abre — a tabela acima é sobre isso. O tamanho da lista vem do sistema em volta, que é quem sabe quantos marcos você já passou, e é lá que ele deve ser consultado.'),
  P('*Até a v7.6 esta seção trazia a própria contagem — dois no nível 1, mais um a cada ímpar, treze no nível 20. Ela era coerente consigo mesma e discordava do sistema em volta em três feitiços no nível 20 e seis no 30, e os dois davam um feitiço extra no nível 10, que somados contavam duas vezes. Uma contagem, um dono.*'),
  P('O que continua valendo aqui: **Passiva é paga com espaços dessa lista**, a **Expansão de Domínio** também, e as **Liberações Máximas ficam de fora** — elas não ocupam espaço.'),
  P('Ao subir de nível você pode reescrever um feitiço que já conhece, do zero. Uma Liberação Máxima conta como feitiço pra isso.'),
  P('Se um feitiço que você conhece deixar de ser legal — por regra nova ou revisão da mesa — você o reescreve de graça na hora, sem gastar a troca de nível.'),

  H2('Faixa lendária'),
  P('Os Classes 6 e 7 existem, mas a recomendação é que o ganho dos níveis 21 a 30 venha de Passivas que quebram regra, e não de dado a mais.'),
];

module.exports = { foraDeCombate, liberacao, maxima, ouro, progressao };

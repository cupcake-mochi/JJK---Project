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
  P('Expansão ainda não tem regra escrita. Quando tiver, ela não sai daqui: vai morar na criação de personagem, presa a um mínimo de **refino** e de nível, e comprada trocando espaços de feitiço conhecido. O teto do feitiço não muda por causa dela.'),
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
      ['5', 'Liberação Máxima custa a rodada inteira, e você só tem as que o nível deu.'],
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
      ['1', 'Fundamento com três Famílias Fechadas. Dois feitiços de Classe 0 (grátis) e dois conhecidos. Classe 1. Passiva Livre.'],
      ['ímpares', 'Mais um feitiço conhecido.'],
      ['5', 'Classe 2. Um feitiço de Classe 0 a mais.'],
      ['7', 'Libera Passiva de Classe 2.'],
      ['9', 'Classe 3.'],
      ['10', 'Um feitiço extra. **A primeira Liberação Máxima.**'],
      ['11', 'Um feitiço de Classe 0 a mais.'],
      ['13', 'Classe 4. Libera Passiva de Classe 3.'],
      ['17', 'Classe 5. Técnica Máxima. Um feitiço de Classe 0 a mais.'],
      ['20', 'Um feitiço extra. **A segunda Liberação Máxima.**'],
      ['21', 'Classe 6.'],
      ['26', 'Classe 7.'],
      ['30', '**A terceira Liberação Máxima.**'],
    ],
    [16, 84], { boldCols: [0] }
  ),
  GAP(120),
  P('A conta fecha em treze feitiços conhecidos no nível 20, menos os espaços que você trocou por Passiva. As Liberações Máximas ficam fora dessa conta.'),
  P('Ao subir de nível você pode reescrever um feitiço que já conhece, do zero. Uma Liberação Máxima conta como feitiço pra isso.'),
  P('Se um feitiço que você conhece deixar de ser legal — por regra nova ou revisão da mesa — você o reescreve de graça na hora, sem gastar a troca de nível.'),

  H2('Faixa lendária'),
  P('Os Classes 6 e 7 existem, mas a recomendação é que o ganho dos níveis 21 a 30 venha de Passivas que quebram regra, e não de dado a mais.'),
];

module.exports = { foraDeCombate, liberacao, maxima, ouro, progressao };

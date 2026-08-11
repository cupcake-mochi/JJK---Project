// partC — seção 2 (Montar um feitiço), com o exemplo guiado do Corte Medido.
// O Corte Medido e a tabela de Ampliar são conferidos por matematica/pac7.py.
const { d, C, W, P, H1, H2, H3, BUL, NUM, TBL, BOX, GAP } = require('./helpers.js');

const montar = [
  H1('2 · Montar um feitiço'),
  P('Com o Fundamento escrito, os feitiços saem dele. Montar um feitiço é uma conta curta: escolher o tamanho, escolher como ele sai, gastar os pontos e dar um nome. Esta seção percorre os passos e depois monta um feitiço completo, do zero, pra você ver a conta acontecendo.'),

  H2('Os cinco passos'),
  NUM('Escolha a **Classe**, até a maior que o seu nível liberou. Ela define os pontos (3 × Classe), o custo em PE (o mesmo número) e quantas Melhorias e Restrições cabem.', 1),
  NUM('Escolha a **Forma**: como o feitiço sai de você. Algumas Formas custam pontos; nenhuma conta no limite de Melhorias.', 1),
  NUM('Compre **Melhorias** (o catálogo é a seção 3) e, se quiser recuperar pontos, venda **Restrições** (seção 4).', 1),
  NUM('O que sobrar de ponto vira dado: **1 ponto = 1d8 de dano**.', 1),
  NUM('Dê um nome e escreva na ficha.', 1),
  GAP(120),
  BOX(null, [
    '**Dados de dano = Pontos − Melhorias + Devolução**',
    'A devolução das Restrições nunca passa do que você gastou em Melhoria: se devolver mais, o excedente some. É por isso que Restrição barateia o feitiço, mas nunca aumenta o dano dele.',
  ]),

  H2('Exemplo guiado: o primeiro feitiço da Régua'),
  P('A **Régua**, apresentada na seção 1, mede distâncias e cobra por elas. As Famílias Livres dela são Mira e Alcance; as Fechadas são Área, Amparo e Auxiliares. O jogador quer o golpe básico da técnica: um corte disparado à distância, que atravesse armadura.'),
  P('**Passo 1 — Classe.** O personagem está no nível 5, então a maior Classe dele é 2. Isso dá **6 pontos**, custo de 6 PE, e os limites da Classe: até 2 Melhorias, até 2 Restrições, devolução máxima de 4.'),
  P('**Passo 2 — Forma.** Projétil: 18 m, um alvo, rolagem de acerto. Não custa ponto.'),
  P('**Passo 3 — Melhorias e Restrições.** **Fura** (Mira, Média) custaria 2 pontos numa Classe 2, mas Mira é Família Livre da Régua: o desconto de metade da Classe (1) derruba o preço pra **1 ponto**. **Precisão** (Mira, Leve) custa 1, e fica em 1 — o desconto nunca leva um preço abaixo de 1. Foram 2 pontos em Melhoria, sobrariam 4. Pra recuperar um, ele vende **Parado** (devolve 1): a Régua precisa dos pés no chão pra medir, então não se move no turno em que conjura. A devolução paga 1 dos 2 pontos gastos.'),
  P('**Passo 4 — Dano.** 6 − 2 + 1 = **5 pontos sobrando: 5d8 de corte**, uma média de 22.'),
  P('**Passo 5 — Nome.** Está pronto, e vai pra ficha assim:'),
  TBL(null, [
    ['Nome', 'Corte Medido'],
    ['Classe / Pontos / PE', '2  ·  6 pontos  ·  6 PE'],
    ['Forma', 'Projétil (18 m, um alvo)'],
    ['Resolve com', 'Rolagem de acerto, com +2 da Precisão'],
    ['Melhorias', 'Fura (−1, Livre) · Precisão (−1, Livre)'],
    ['Restrições', 'Parado (+1)'],
    ['Dano', '5d8 = 22, ignorando até 6 de Redução de Dano (3 × Classe)'],
    ['Ação', 'Padrão'],
    ['Como é', 'Ele para, aponta, diz o nome do alvo — e a distância medida abre no corpo do outro, como um corte de papel do tamanho do caminho.'],
  ], [24, 76], { boldCols: [0] }),
  GAP(100),
  BOX('Erros comuns', [
    '**Vender Restrição sem Melhoria pra pagar.** A devolução some. O **Golpe Cru** (seção 10) faz isso de propósito, pra mostrar que não existe dano de graça.',
    '**Contar que Restrição vira dado.** Nunca vira: contra um alvo só, 6 pontos continuam sendo o máximo de dados de uma Classe 2, com ou sem Restrição.',
    '**Empilhar duas Restrições de frequência** (Uma Vez, Condicional, Aquecer, Dívida). Não pode; a seção 4 explica a trava.',
  ], 'warn'),

  H2('Formas'),
  P('A Forma é o corpo do feitiço: define quem ele atinge e como se resolve. Escolha uma por feitiço.'),
  TBL(['Forma', 'Custa', 'O que é', 'Como resolve'],
    [
      ['Projétil', '—', '18 m, um alvo', 'Rolagem de acerto'],
      ['Toque', '—', '1,5 m, um alvo. Projétil com a Restrição Corpo a Corpo embutida (devolve Média).', 'Rolagem de acerto'],
      ['Explosão', 'Leve', 'Esfera de raio 3 m, num ponto a até 18 m', 'Teste de Resistência, metade no sucesso'],
      ['Aura', 'Leve', 'Esfera de raio 3 m centrada em você. Explosão com Corpo a Corpo embutida (devolve Média).', 'Teste de Resistência, metade no sucesso'],
      ['Cone', 'Leve', '4,5 m saindo de você', 'Teste de Resistência, metade no sucesso'],
      ['Linha', 'Leve', '18 m por 1,5 m', 'Teste de Resistência, metade no sucesso'],
      ['Cura', 'Média', 'Um aliado a até 9 m. Os dados viram cura.', 'Automático'],
      ['Apoio', '—', 'Um aliado a até 9 m. Sem dano. Cada ponto que sobra vira 3 de vida temporária.', 'Automático'],
      ['Onda', 'Pesada', 'Esfera de raio 3 m centrada em você. A cura ou o apoio pega todos os aliados dentro, sem dividir.', 'Automático'],
      ['Efeito', '—', 'Fora de combate. Sem dano. Ver seção 5.', 'Automático'],
    ],
    [12, 9, 44, 35], { boldCols: [0], centerCols: [1] }
  ),
  GAP(120),
  P('Trocar rolagem de acerto por Teste de Resistência, ou o contrário, é de graça.'),
  P('Cada Forma pertence a uma Família: Explosão, Cone e Linha à **Área**; Cura, Apoio e Onda ao **Amparo**. Fundamento com a Família Fechada fica sem essas Formas. Projétil, Toque e Efeito são de todo mundo.'),

  H2('Escadas'),
  P('Alcances e tamanhos crescem por degraus fixos. As Melhorias de Alcance e Área (Longe, Maior e as irmãs) sobem degraus nestas escadas:'),
  TBL(['Escada', 'Degraus'],
    [
      ['Alcance', '1,5 m → 9 m → 18 m → 36 m → 90 m → o que você enxergar'],
      ['Esfera (raio)', '3 m → 4,5 m → 6 m → 9 m → 15 m'],
      ['Cone e Linha', '4,5 m → 9 m → 18 m → 30 m → 60 m'],
    ],
    [24, 76], { boldCols: [0] }
  ),
  GAP(100),
  P('O degrau "o que você enxergar" vale pra olho nu. Câmera, luneta, espelho e visão emprestada não contam.'),
  P('Se uma Melhoria subir mais degraus do que a escada tem, ela para no último degrau.'),

  H3('Base por Classe'),
  TBL(['Forma', 'Classe 0', 'Classes 1–5', 'Classes 6–7'],
    [
      ['Projétil e Toque*', '9 m', '18 m', '36 m'],
      ['Explosão', 'raio 3 m, a 9 m', 'raio 3 m, a 18 m', 'raio 4,5 m, a 36 m'],
      ['Cone', '3 m', '4,5 m', '9 m'],
      ['Linha', '9 × 1,5 m', '18 × 1,5 m', '30 × 1,5 m'],
      ['Cura, Apoio e Onda', '4,5 m', '9 m', '18 m'],
    ],
    [24, 22, 27, 27], { boldCols: [0], centerCols: [1,2,3] }
  ),
  GAP(100),
  P('*Toque fica em 1,5 m em qualquer Classe.'),

  H2('Ampliar'),
  P('Você pode lançar qualquer feitiço que conhece numa Classe maior que o original, até a sua Classe máximo, pagando o PE da Classe novo. Refaça a conta inteira com os números novos: pontos, preços de Melhoria e devoluções de Restrição mudam todos juntos.'),
  TBL(['Palma Trovejante · Classe', 'Pontos', 'Cone (Leve)', 'Derrubado (Média)', 'Lento (devolve)', 'Dano', 'PE'],
    [
      ['Classe 2 (original)', '6', '−1', '−2', '+2', '5d8 = 22', '6'],
      ['Classe 3', '9', '−2', '−3', '+3', '7d8 = 31', '9'],
      ['Classe 5', '15', '−3', '−5', '+5', '12d8 = 54', '15'],
    ],
    [26, 10, 14, 18, 16, 14, 8], { boldCols: [0], centerCols: [1,2,3,4,5,6] }
  ),
  GAP(100),
  P('O dano sobe, a proporção não: em todas as Classes a Palma sai perto de 60% do teto, bem acima do quarto que o bônus de Controle exige. Ampliar aumenta o número, não muda a natureza do feitiço — quem não alcançava o bônus continua sem alcançar (a regra de Controle está no fim desta seção).'),

  H2('Cura'),
  P('A Forma Cura custa Média e transforma em cura os dados que sobrarem, aplicados automaticamente num aliado a até 9 m. Não existe Liberação Máxima de cura: a linha de baixo é o teto por Classe.'),
  P('Pra pegar mais gente: **Junto** (Amparo) soma um aliado dividindo o efeito, e a Forma **Onda** cura em área sem dividir.'),
  TBL(['Classe', '1', '2', '3', '4', '5'],
    [
      ['Cura cheia', '2d8 = 9', '4d8 = 18', '6d8 = 27', '8d8 = 36', '10d8 = 45'],
      ['Onda (área)', '1d8 = 4', '3d8 = 13', '4d8 = 18', '6d8 = 27', '7d8 = 31'],
      ['Dano da mesma Classe', '13', '27', '40', '54', '67'],
    ],
    [24, 15, 15, 15, 15, 16], { centerCols: [1,2,3,4,5], boldCols: [0] }
  ),

  H2('Controle'),
  P('Feitiço que carrega pelo menos uma Melhoria da família **Controle** ganha um bônus quando abre mão de dano de verdade. Comprar a condição e continuar batendo forte não conta: o gatilho é o dano que sobrou no final.'),
  BUL('Dano final até **um quarto do teto** (o teto é 4 × Classe): os efeitos de Controle duram uma rodada a mais.'),
  BUL('**Sem dano nenhum** — o feitiço gastou tudo em Controle: além da rodada extra, a CD contra esses efeitos sobe +2.'),
  GAP(60),
  P('O bônus vale só contra os efeitos de Controle do feitiço. O Teste de Resistência do dano, quando existe, fica como está.'),
  TBL(['Feitiço de Classe 5 · 15 pontos · teto 20 · um quarto = 5', 'Dano final', 'O que ganha'],
    [
      ['15d8 puro, sem Controle', '15d8', 'nada'],
      ['Condição Menor (−5)', '10d8', 'nada: ainda bate como feitiço de dano'],
      ['Condição Maior (−8)', '7d8', 'nada'],
      ['Condição Maior (−8) · Condição Menor (−5)', '2d8', 'dura uma rodada a mais'],
      ['Explosão (−3) · Cond. Menor (−5) · Prende (−5) · Puxa (−5) · Lento (+3)', '0d8', 'uma rodada a mais e CD +2'],
    ],
    [48, 14, 38], { boldCols: [0], centerCols: [1] }
  ),
  GAP(100),
  P('Uma condição sozinha nunca dispara o bônus. Pra chegar no primeiro degrau você compra duas peças de Controle, ou uma condição e alguma outra coisa cara — e pro segundo, o feitiço precisa sair sem um único dado de dano.'),
  GAP(100),
  P('Falta uma peça nesta história: o feitiço que rompe o limite de dano contra um alvo só. Ela chega no nível 10, e tem seção própria — a **Liberação Máxima**, seção 6.'),
];

module.exports = { montar };

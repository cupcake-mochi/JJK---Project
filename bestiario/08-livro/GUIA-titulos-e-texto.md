# Guia de títulos e de texto — o padrão dos livros de 5e

Régua da terceira passada. Sai de quatro livros atuais, lidos em faixa curta de páginas, e das
reclamações do Mizuki sobre a segunda passada. Soma-se à `REGRA-DE-VOZ.md` do Manual da Guilda;
não substitui.

| livro | páginas lidas |
|---|---|
| Livro do Jogador 2024 (PT-BR) | 9 (sumário), 13-20 (capítulo 1) |
| Guia do Mestre 5e (PT-BR) | 1-8 (sumário), 275-277 (*Criando um Monstro*) |
| Caldeirão de Tasha (PT-BR) | 1-6 (sumário e capítulo 1), 86-87 (*Patronos de Grupo*) |
| Dungeon Master's Guide 2024 | 1-8 (sumário), 50-56 (fim do capítulo 2, abertura do 3) |

---

## Títulos

### O que os livros fazem

**Livro do Jogador 2024.** Capítulos: *Jogando o Jogo*, *Criação de Personagens*, *Classes de
Personagem*, *Origens dos Personagens*. Seções: *Dados*, *Testes de D20*, *Salvaguardas*,
*Proficiência*, *Ações Bônus*, *Reações*, *Visão e Luz*, *Riscos*, *Movimento e Posição*,
*Dano e Cura*, *Tipos de Dano*, *Resistência e Vulnerabilidade*, *Condições*, *Avanço de Nível*,
*Multiclasse*, *Componentes de Origem*.

**Guia do Mestre 5e.** Capítulos: *Seu Próprio Mundo*, *Criando Aventuras*, *Entre Aventuras*,
*Tesouros*, *Conduzindo o Jogo*, *Oficina do Mestre*. Seções: *Assentamentos*, *Idiomas e
Dialetos*, *Facções e Organizações*, *Armadilhas*, *Regras da Mesa*, *Doenças*, *Venenos*,
*Loucura*, *Pontos de Experiência*, *Dano Maciço*, *Moral*, *Criando um Monstro*.

**Caldeirão de Tasha.** Capítulos: *Opções de Personagens*, *Patronos de Grupo*. Seções:
*Customizando sua Origem*, *Mudando sua Subclasse*, *Talentos*, *Vantagens*, *Atribuições*,
*Exemplos de Patronos*.

**Dungeon Master's Guide 2024.** Capítulos: *The Basics*, *Running the Game*, *DM's Toolbox*,
*Creating Adventures*, *Creating Campaigns*, *Cosmology*, *Treasure*, *Bastions*. Seções:
*Group Size*, *Resolving Outcomes*, *Improvising Damage*, *Running Combat*, *Tracking Monsters'
Hit Points*, *Chases*, *Traps*, *Hazards*, *Cursed Items*, *Creating a Creature*.

### O padrão

1. **Título é substantivo, ou um substantivo com complemento.** *Tesouros*, *Condições*,
   *Tipos de Dano*, *Regras da Mesa*. Nenhum dos títulos acima é frase com verbo conjugado.
2. **Par de substantivos com "e" é forma comum**, e resolve seção que trata de duas coisas
   vizinhas: *Dano e Cura*, *Visão e Luz*, *Idiomas e Dialetos*, *Resistência e Vulnerabilidade*.
3. **Quando o título é um termo do jogo, ele é o termo, escrito igual.** *Salvaguardas*,
   *Proficiência*, *Reações*. O leitor que procura a palavra acha a seção.
4. **Procedimento vira substantivo de ação.** O Livro do Jogador 2024 escreve *Criação de
   Personagens* e *Avanço de Nível*. O Guia do Mestre 5e e o DMG 2024 ainda usam gerúndio
   (*Criando Aventuras*, *Running Combat*); aqui fica o substantivo, que é o que o livro mais novo
   em português escolheu.
5. **Curto.** Capítulo tem de uma a três palavras de conteúdo. Seção raramente passa de quatro.
6. **Metáfora e sabor ficam fora do título.** O sabor desses livros mora em legenda de arte e em
   caixa lateral. O título diz do que a seção trata.
7. **As exceções existem e são poucas.** O Livro do Jogador tem *Jogador ou Mestre?*, *Os Seis
   Atributos* e *A Ordem de Combate*; o Guia do Mestre tem *O Papel dos Dados* e *Como Usar Este
   Livro*. A `REGRA-DE-VOZ.md` mediu 1,3% de títulos com artigo no Livro do Jogador 2024. A
   exceção não vira licença.
8. **Caixa de sentença.** Os livros traduzidos usam Title Case por herança do inglês; o Projeto-M
   escreve em caixa de sentença (`Dano e cura`, e não `Dano e Cura`), como manda a `REGRA-DE-VOZ.md`.

### A checagem, para o Bestiário

| não pode | exemplo do que saiu | vira |
|---|---|---|
| artigo no começo | *A adjacência* | *Adjacência* |
| "Como…" | *Como a mesa sai* | *Saídas* |
| pergunta | *O que é uma maldição* | *Maldições* |
| frase com verbo | *Morreu do jeito errado* | *Morte sem energia* |
| metáfora | *Morte de mão limpa* | *Morte por ferramenta* |
| contagem | *Os sete tipos* | *Tipos de criatura* |

Vale para os três níveis: título de capítulo (listas `CHAPTERS` e `FRONT` do `build.py`), título
`#` de dentro do arquivo (que no Bestiário é seção, e não capítulo) e `##`/`###`. Vale também para
nome de tabela (`{: .tab-titulo }`), que é citado pelo nome em outros capítulos.

**Cuidado com colisão.** Título não pode ter o mesmo nome de um termo do `07-vocabulario.md` se
tratar de outra coisa. Exemplo: um capítulo sobre os pacotes de regra por natureza da criatura
não pode se chamar *Categorias*, porque `Categoria` já é a coisa do Passo 1 do capítulo 6.

---

## Abertura de capítulo e de seção

### O que os livros fazem

- **DMG 2024, capítulo 3.** Uma frase diz que o capítulo reúne conselhos para quem prepara ou
  conduz a sessão, e uma segunda lista o que tem dentro. Depois disso, a primeira seção.
- **Guia do Mestre 5e, *Criando um Monstro*.** A abertura diz o que o outro livro já cobre e o
  que esta seção acrescenta. A subseção seguinte abre com um roteiro de uso: se você só precisa
  de números rápidos, siga estes passos; se quer o bloco completo, pule para a seção tal.
- **Tasha, capítulo 1.** Uma frase: este capítulo soma opções às do Livro do Jogador.
- **Livro do Jogador 2024, capítulo 1.** Um parágrafo diz o que o jogo é, e a primeira seção de
  regra (*Dados*) já começa definindo.

### O padrão

1. **Uma a três frases**, dizendo o que tem ali e quando o leitor usa.
2. **Quando o capítulo tem dois usos, a abertura roteia.** "Se você quer X, vá à seção Y."
3. **Nenhuma justificativa de desenho.** Por que o número é aquele, contra o que ele foi medido,
   como outro sistema faz: nada disso aparece na abertura, nem no resto da seção.
4. **Nenhum tom de narrador.** A abertura informa. Quem conta história é o texto de ambientação,
   e ele fica fora da regra.

---

## Explicar regra

### O que os livros fazem

- **Guia do Mestre 5e, *Dano Maciço*.** Uma frase diz o que a regra opcional faz. A seguinte
  dá a condição e o efeito ("quando uma criatura sofre…, ela deve…"). A terceira é um exemplo
  com número.
- **Guia do Mestre 5e, *Moral*.** Uma frase diz para que serve a regra; uma lista dá as
  situações que disparam o teste; um parágrafo dá o procedimento; outro diz o que acontece na
  falha.
- **Livro do Jogador 2024, *Notação de Dados*.** Definição, e em seguida "por exemplo".

### O padrão

1. **Condição, depois efeito.** "Quando X, Y." Presente do indicativo.
2. **Exemplo curto logo depois**, com número de verdade.
3. **Segunda pessoa para o que o mestre faz** ("você escolhe", "role"). Terceira pessoa para o
   que a criatura faz.
4. **Uma regra por parágrafo.** Se o parágrafo empilha duas, cada uma ganha nome em negrito.

---

## O que sai do texto

| tipo | teste | exemplo do Mizuki |
|---|---|---|
| **justificativa de desenho** | a frase só interessa a quem decide o número | *"O fator de dano de quem tem Intervenção é multiplicado por 0,923, porque a Intervenção é ação extra e não sai da cota."* |
| **drama** | a frase narra, ou quer impressionar | frase de efeito no fim de parágrafo |
| **enchimento** | tirar a frase não apaga regra, número nem instrução | *"O que assusta nela é aparecer, e aparecer não custa."* · *"Quem não a alcança de longe perde o turno procurando."* |
| **frase vaga que esconde regra** | tem regra ali, mas dita em imagem | *"Procure um feiticeiro que morreu na obra e não voltou como coisa, e a busca explica o mundo inteiro em vez de furar a regra."* |

**O teste da mesa:** um mestre usaria isso no meio de uma sessão, ou montando um inimigo? Se não,
sai. Se a frase vaga guarda uma regra, a regra fica, dita com todas as letras.

**Marcas de texto de IA que também saem:** "além disso", "em suma", antítese de efeito ("não é X,
é Y"), três adjetivos em fila, simetria forçada entre duas frases.

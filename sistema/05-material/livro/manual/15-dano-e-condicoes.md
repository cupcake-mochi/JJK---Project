# Dano, Condições e Cobertura

Este capítulo é de consulta. Você vem aqui quando o dano tem um tipo que importa, quando alguém ficou com uma condição, ou quando tem uma mureta no meio do caminho.

## Os tipos de dano

Todo dano deste sistema tem um tipo, e os catorze tipos se dividem em três grupos. O grupo importa porque várias habilidades resistem a um grupo inteiro em vez de a um tipo só.

> **Catorze tipos, em três grupos.**
>
> | grupo | tipos |
> |---|---|
> | **Físicos** | `Cortante` · `Perfurante` · `Concussão` |
> | **Elementais** | `Fogo` · `Frio` · `Elétrico` · `Ácido` · `Trovejante` · `Veneno` |
> | **Especiais** | `Radiante` · `Necrótico` · `Psíquico` · `Energia Reversa` · `Alma` |

A lista é fechada. Quando uma arma, um feitiço ou uma habilidade disser de que tipo é o dano, ou a que tipo ela resiste, o nome sai daqui.

### O que cada tipo faz num corpo

O número do dano vem da arma ou do feitiço. O tipo diz quem resiste a ele e como a mesa descreve o golpe. Vale ler uma vez, para saber narrar a própria técnica.

#### Físicos

**`Cortante`** — lâmina, fio, borda. Abre o corpo e sangra. É o dano que deixa o rastro mais visível numa cena: chão molhado, uniforme rasgado, alguém segurando o braço.

**`Perfurante`** — ponta, agulha, projétil. Entra fundo num ponto pequeno. Machuca por dentro sem estragar muito por fora, e é o tipo que atravessa uma guarda que estava bem fechada contra um golpe largo.

**`Concussão`** — soco, queda, coisa pesada. Quebra osso e sacode o que está dentro da caixa. Quem toma sai do lugar, perde o ar e demora um segundo a mais para reagir.

#### Elementais

**`Fogo`** — queima, cozinha, pega no que estiver por perto. A cena continua queimando depois do golpe.

**`Frio`** — tira o calor e trava a articulação. O corpo endurece antes de doer, e a mão demora a fechar de novo.

**`Elétrico`** — passa pelo corpo e faz o músculo obedecer a outra pessoa. Contrai tudo de uma vez, arremessa, e cheira a queimado no ponto de entrada.

**`Ácido`** — come. Continua comendo o que encostou, e estraga equipamento junto com pele.

**`Trovejante`** — pressão e som. Bate no ar antes de bater na pessoa: empurra, estoura ouvido, quebra vidro na sala inteira.

**`Veneno`** — entra e trabalha por dentro. É o dano que dá tempo de alguém perceber que está mal antes de cair.

#### Especiais

**`Radiante`** — luz que queima de dentro para fora. Cega antes de ferir, e costuma vir de coisa que se considera com algum direito de julgar.

**`Necrótico`** — apodrece o vivo. O ferimento não fecha direito e a pele em volta escurece.

**`Psíquico`** — não encosta no corpo. Bate direto na cabeça: a dor vem sem ferimento, e a pessoa continua inteira por fora enquanto sangra pelo nariz.

**`Energia Reversa`** — a energia que conserta gente, usada para o contrário. Num corpo comum ela é ferimento em cima do que já existe; é o dano que mais desmonta quem confiava na própria recuperação.

**`Alma`** — passa por couro, armadura e barreira, e bate na coisa que você é. Ele gasta Integridade em vez de vida, tem quatro estágios próprios, e não se resiste com músculo. Quem toma dano de `Alma` continua de pé e volta menos do que era. Os quatro estágios estão logo abaixo.

### Os quatro estágios de dano na alma

**Integridade é a vida da alma**, e a fórmula dela é `20 + 8 × (nível − 1)`, do capítulo 1, *Como Jogar*. Esta seção é o que acontece conforme ela cai.

> **Cada ponto de dano na alma tira 1 de vida, 1 de Integridade, e derruba a sua vida máxima em 1** até o próximo descanso longo.
>
> **Dano na alma entra cheio**, sem redução pela metade.
>
> Ao receber, faça um **Teste de Resistência de Integridade** contra a CD do atacante. Numa falha, você também avança um estágio na hora, mesmo que a fração ainda não tenha fechado.

| Integridade perdida | Estágio | O que pega |
|---|---|---|
| 1/4 | **1** | Desvantagem em testes de perícia. |
| 1/2 | **2** | Deslocamento pela metade, e todo feitiço custa +1 PE por Classe. |
| 3/4 | **3** | Desvantagem em ataques e Testes de Resistência. Você não conjura acima de metade da sua Classe máxima. |
| Toda | **4** | Você não é mais você. O que sobra é decisão do mestre. |

**Cura comum não devolve o que a alma perdeu.** Só descanso longo, ou a Melhoria `Remenda`. O descanso longo devolve toda a Integridade e a vida máxima, e limpa os estágios.

**Nenhum feitiço passa de 2 × Classe em dados na alma.**

#### Nomes que se repetem no manual

Seis desses nomes você já viu em outro lugar, e ali eles querem dizer outra coisa.

| onde o nome aparece | o que ele é ali |
|---|---|
| `Fogo`, `Ácido`, `Veneno` como **Tema** do Fundamento | rótulo de sabor pendurado numa técnica, sem efeito próprio |
| `Cortante`, `Trovejante`, `Alma` dentro de `Passo Cortante`, `Palma Trovejante`, `Toca a Alma` | pedaço do nome de um feitiço pronto |
| os catorze desta seção | o tipo do dano na hora que ele cai |

Um não puxa o outro. Um feitiço com o Tema `Fogo` só causa dano do tipo `Fogo` se o texto dele disser isso.

> **Exemplo.** A Mei tem uma habilidade que dá resistência a `Fogo`. O inimigo acerta ela com `Palma Trovejante`, que causa dano `Trovejante`. Os dois são Elementais, e isso não basta: a resistência dela nomeia um tipo, e `Trovejante` não é `Fogo`. Ela toma o dano inteiro.

## Condições

**Condição** é um estado nomeado que muda o que você consegue fazer enquanto durar. São catorze, e cada uma tem um **nível**: `Leve`, `Média` ou `Pesada`.

> **O nível faz duas coisas, e são as duas contas que a condição pede.**
> É o que ela **custa para comprar** dentro de um feitiço.
> É o que ela **custa para tirar** de alguém, em pontos de energia.

#### Como ler as tabelas

Cada linha diz o nome, o efeito inteiro sem nada implícito, e como aquilo se parece na mesa. O nível de cada bloco está no título da seção. Onde a condição dá vantagem ou desvantagem, a tabela diz a quem.

### As seis de nível `Leve`

| condição | o que faz | na cena |
|---|---|---|
| `Lento` | seu deslocamento cai pela metade e você não usa Ação Bônus | as pernas pesam e o turno rende menos; você chega, só que atrasado |
| `Incapacitado` | você não pode `Bloquear`, e todo ataque corpo a corpo contra você é crítico | a guarda abriu e você não consegue fechar de volta; quem chegar perto acerta onde quiser |
| `Derrubado` | você está no chão. Só se move rastejando, tem desvantagem nos seus ataques, e quem ataca você **a até 1,5 m tem vantagem**; quem ataca de longe tem desvantagem | você está de costas no chão olhando para cima, e a prioridade do turno vira levantar |
| `Agarrado` | seu deslocamento é `0`. Acaba se quem agarrou ficar `Incapacitado`, ou se alguma coisa tirar você do alcance dele | tem uma mão fechada em você; dá para bater, dá para conjurar, e não dá para sair |
| `Desarmado` | a sua arma está no chão ou na mão de outro. Você bate desarmado até pegar de volta | o barulho da lâmina caindo no concreto, e a decisão de gastar o turno pegando |
| `Surdo` | você não ouve. Falha automática em teste que precise de audição, e **`−2` na iniciativa** | zumbido, e tudo que chega por trás chega sem aviso |

### As duas de nível `Média`

| condição | o que faz | na cena |
|---|---|---|
| `Calado` | você não conjura. Nada que precise de voz, gesto ou Selo sai | você tenta e não sai nada; o resto da luta você vira alguém com as mãos e mais nada |
| `Enfeitiçado` | você não ataca quem enfeitiçou nem mira efeito nocivo nele, e ele tem vantagem em teste social contra você | você continua você, e aquela pessoa passou a ter razão sobre tudo |

### As seis de nível `Pesada`

| condição | o que faz | na cena |
|---|---|---|
| `Petrificado` | você virou pedra. `Incapacitado`, deslocamento `0`, sem perceber nada em volta, quem ataca você tem vantagem, e você tem resistência a todo dano | você sai da luta inteiro e sem saber o que aconteceu enquanto isso |
| `Impedido` | seu deslocamento é `0`, você tem desvantagem nos seus ataques e no Teste de Resistência Físico, e quem ataca você tem vantagem | alguma coisa te prendeu no lugar: teia, corrente, o chão fechando em cima do pé |
| `Cego` | você não enxerga. Falha automática em teste que precise de vista, desvantagem nos seus ataques, e quem ataca você tem vantagem | você ataca na direção do barulho, e o grupo passa a te narrar a sala |
| `Amedrontado` | desvantagem em ataque e em teste enquanto você enxergar a fonte do medo, e você não se aproxima dela de vontade própria | você sabe o que precisa ser feito e o corpo não avança |
| `Envenenado` | desvantagem nos seus ataques e em todo teste de perícia | suor frio, mão tremendo, e tudo saindo pela metade |
| `Atordoado` | você perde a Ação Padrão e não usa reação. Quem tem mais de uma Ação Padrão no turno (um chefe, um capanga grande) perde **uma**, e não todas | o mundo demora a voltar; a rodada passa por cima de você |

> **Só as de nível `Pesada` dão Teste de Resistência no fim de cada turno do alvo.**
> **E só cabe uma delas por feitiço.**

> **Exemplo.** A Rina fica `Atordoada`. Ela perde a Ação Padrão daquele turno e não usa reação, então ninguém leva ataque de oportunidade dela. A Defesa continua a mesma: `Atordoado` não abre a guarda de ninguém. No fim do turno dela, como é uma condição `Pesada`, ela faz o Teste de Resistência e pode sair sozinha.

#### `Atordoado` e `Incapacitado` atacam eixos diferentes

Nenhuma das duas contém a outra. Escolher uma para aplicar é escolher o que você quer tirar do alvo:

| | o eixo que ela ataca |
|---|---|
| `Atordoado` | tira **parte do turno**: uma Ação Padrão e a reação. Você continua se defendendo |
| `Incapacitado` | tira a **defesa**: você age e não se protege |

`Paralisado` não existe neste sistema. O que outros jogos chamam assim se chama `Atordoado` aqui, e não há um terceiro degrau que some os dois.

> **Metade do `Incapacitado` só aparece se a sua mesa usa `Bloquear`.** A outra metade — todo ataque corpo a corpo contra você é crítico — vale sempre, com `Bloquear` ligado ou não.

#### Três coisas que não são condição aqui

| não é condição | onde ela está |
|---|---|
| `Inconsciente` | é cair a 0 de vida, com regra própria no capítulo 1, *Como Jogar* |
| `Exaustão` | é relógio de descanso, e mora no capítulo 5, *Descanso e Recuperação* |
| `Invisível` | é benefício, e as condições são compradas para aplicar num alvo |

A `Exaustão` é a que mais engana, porque em outros jogos ela é condição e aqui não. Quem for escrever feitiço que canse alguém não alcança a exaustão pela Melhoria `Condição`.

### Comprar uma condição num feitiço

> **Existe uma Melhoria `Condição`, uma só, e o preço dela é o nível da condição que você escolheu.**
> Escolher `Derrubado` custa `Leve`. Escolher `Petrificado` custa `Pesada`.

Você aponta a condição nas tabelas acima, lê o nível dela, e esse é o preço. Não existe pacote nem grupo de compra.

> **Exemplo.** O Kaito está montando um feitiço de Classe 2 que derruba quem for acertado. Ele compra a Melhoria `Condição` e escolhe `Derrubado`, que é `Leve`. Numa Classe 2 isso custa `1` ponto, e ele fica com o resto do orçamento em dados de dano. Se ele quisesse `Impedido`, que é `Pesada`, o mesmo feitiço pagaria `3` e sairia bem menor.

### Tirar uma condição

> **Tirar uma condição de alguém custa `1` ponto de energia por nível: `1` para `Leve`, `2` para `Média`, `3` para `Pesada`.**

Você só faz isso se tiver uma habilidade que tire condição, e cada habilidade dessas tem um teto de quanta energia ela gasta por uso. O teto é que decide o que você alcança: com teto `2` você limpa `Leve` e `Média`, e a `Pesada` fica fora até o teto subir.

> **Exemplo.** A Mei tem uma habilidade de tirar condição com teto de `2` pontos de energia por uso. O aliado dela está `Calado`, que é `Média`: ela gasta `2` e limpa. No turno seguinte o mesmo aliado fica `Cego`, que é `Pesada`: ela precisaria de `3`, e não consegue até a habilidade dela crescer.

## Cobertura

Cobertura é o que está entre você e quem está atirando. São três degraus, e você lê o que enxerga do alvo para saber em qual deles ele está. A pergunta que o mestre faz é sempre a mesma: daqui, quanto do corpo dele dá para acertar?

| cobertura | o que ela dá | exemplo |
|---|---|---|
| **Parcial** | **`+2` de Defesa e `+2` no Teste de Resistência Físico** | mureta, tronco, uma criatura no caminho |
| **Boa** | **`+5` de Defesa e `+5` no Teste de Resistência Físico** | seteira, olhando por cima de uma parede, metade do corpo atrás de um canto |
| **Total** | **você não pode ser escolhido como alvo, e ponto** | parede inteira, do outro lado da porta |

> **Vale contra o que vem do outro lado da cobertura, e só.** Quem está atrás de uma mureta não ganha nada contra quem já está do lado de cá dela.
>
> **Só a maior conta.** Duas coberturas parciais não viram uma boa.

O Teste de Resistência que a cobertura ajuda é o **Físico**, seja qual for o atributo em que você o travou na criação. Quem travou em Força também se abaixa atrás de uma mureta.

A **Total** tira você da lista de alvos possíveis, e é por isso que ela não tem número. Um efeito que pega área continua alcançando quem está atrás dela, se o efeito não precisar de linha até o alvo.

> **Exemplo.** O Sousuke está agachado atrás do capô de um carro, com meio corpo de fora. Isso é cobertura **Boa**: a Defesa dele sobe `5` contra quem atira do outro lado do estacionamento. Ele decide se jogar inteiro para trás do carro e passa a ter cobertura **Total**, então ninguém do outro lado consegue escolher ele como alvo. Mas um feitiço de área que estoura embaixo do carro não precisa de linha até ele, e alcança do mesmo jeito. Como a **Total** não dá número, o Teste de Resistência Físico dele sai limpo, sem os `5` que ele tinha um segundo antes.

# 19 · Dano e condições

**Fase 4, décima nona peça.** O que uma condição vale, quais são as treze, de que tipo o dano é, e o que cobertura faz.

**Ela é a peça que mais gente estava esperando: vinte e seis lugares em oito documentos citam ela pelo nome.** *E metade dela já estava escrita — em três seções da peça 1 declaradas, no próprio texto, como guarda provisória.*

**O que ela acrescenta é uma coisa só, e é a que faltava: quanto vale uma condição.**

---

## 1. De onde ela veio, e o que é novo

**Três seções mudaram de casa, inteiras.** *As três estavam na peça 1 com o aviso escrito de que o dono natural era esta peça.*

| o que veio | estava em | escrita em |
|---|---|---|
| os catorze tipos de dano, em três grupos | peça 1 §8.1 | v0.74 |
| a cobertura, nos três degraus | peça 1 §8.2 | v0.94 |
| as condições, e o que cada uma faz | peça 1 §8.3 | v0.95 |

**Na peça 1 as três viraram ponteiro**, com o número e o motivo. *É o mesmo trato que o `ESTADO-ATUAL` já fazia com vocabulário que ainda não tinha peça.*

**O que nasce aqui é a seção 2.** Até a v0.102 o projeto escrevia, em três documentos, que *"condição não tem conversão em fatia"* — e escrevia com razão, porque ninguém tinha feito a conta. Ela está feita.

> **⚠⚠ E ela não precisou de régua nova: precisou de ler a tabela de custo do manual.** *É o quarto exemplar do mesmo defeito em vinte versões — o Classe 0 da v0.80, a ação `Mirar` da v0.86, a `Aptidão Própria` da v0.92, e agora esta.* **O manual preça condição em dano desde sempre, e nenhum documento do projeto tinha aberto essa porta.**

---

## 2. A régua — quanto vale uma condição

### 2.1 O teto sai do manual, e ele é plano

**O manual compra condição com ponto de feitiço, e cada ponto que não vira Melhoria vira `1d8` de dano — que são `4,5`.** *Quando esta régua foi feita, na v0.103, o manual vendia condição em dois pacotes: `Condição Menor` custava `Média` e `Condição Maior` custava `Pesada`.* **Então ele sempre disse, em dano, quanto achava que uma condição valia — e é dessa tabela de preço que as bandas saem.**

| Classe | `Leve` | `Média` | `Pesada` | Rotina | `Média` / Rotina | `Pesada` / Rotina |
|---|---|---|---|---|---|---|
| 1 | 1 | 1 | 2 | 3 | 33,3% | 66,7% |
| 2 | 1 | 2 | 3 | 7 | **28,6%** | **42,9%** |
| 3 | 2 | 3 | 5 | 10 | 30,0% | 50,0% |
| 4 | 2 | 4 | 6 | 14 | **28,6%** | **42,9%** |
| 5 | 3 | 5 | 8 | 17 | 29,4% | 47,1% |
| 6 | 3 | 6 | 9 | 21 | **28,6%** | **42,9%** |
| 7 | 4 | 7 | 11 | 24 | 29,2% | 45,8% |

> **Nas Classes pares a razão é exata: `Média` é `2/7` da Rotina e `Pesada` é `3/7`.** *Nas ímpares o arredondamento do manual oscila, e nunca mais que `1,4` ponto percentual — fora a Classe 1, que é pequena demais para arredondar bem.*

**Isso dá as três bandas, e elas são o teto de cada tier:**

> **`Leve` = `1/7` da Rotina · `Média` = `2/7` · `Pesada` = `3/7`.**
> **No nível 30, com a Rotina em `108`: `15,43` · `30,86` · `46,29` de dano por rodada.**

**O teto não é o preço.** Ele diz quanto o manual está disposto a cobrar por um tier; o que cada condição entrega é outra conta, e é a de baixo.

### 2.2 O que cada condição entrega, medido

**Nenhum componente desta conta é escolha.** *Cada um sai de um documento dono, e o `conferir-dano.py` lê os números de lá em vez de guardar cópia.*

| âncora | valor | dono |
|---|---|---|
| a fatia | `5,08` de dano por rodada | `DESENHO-trilhas.md`, a linha de orçamento de Trilha |
| a Rotina no nível 30 | `108` | manual, a tabela de Rotina |
| chefe e capanga no nível 30 | `72` e `38` por rodada | manual, a tabela de inimigo |
| ações do chefe por rodada | `3`, contra um grupo de quatro | manual, citado no `DESENHO-trilhas.md` |
| vantagem e desvantagem | `25` pontos percentuais | peça 11 §8 |
| `1` ponto percentual na rolagem de um aliado | `0,230` | `DESENHO-caminhos.md`, a régua do Guia |
| a ação de atacar de um aliado | `23,00` — dois golpes simples | `DESENHO-caminhos.md` |
| mover `1,5 m` | `0,90`, então `1 m` vale `0,60` | peça 5 §4 |
| `1` ponto de arma | `0,33` por rodada | peça 14 §4 |
| o fundo de uma arma de duas mãos | `5` pontos | peça 14 §5 |
| dano evitado | converte `1` pra `1` | peça 5 §4 |
| o crítico dobra os dados, e só os dados | — | peça 1 §5.2 |

**E duas convenções, as duas lidas de entrega publicada:**

> **Benefício que só o corpo a corpo colhe conta UM aliado.** *É a leitura do `Abalo`, a Manha da Massa.*
> **Benefício que qualquer atacante colhe conta TRÊS.** *É a leitura do `Estampido`, a Manha da Arma de Fogo, que supõe mesa de quatro.*

**As treze, aplicadas num chefe, no nível 30:**

| condição | dano por rodada | fatias | nível |
|---|---|---|---|
| **`Impedido`** | `58,65` | `11,55` | `Pesada` |
| **`Cego`** | `53,25` | `10,48` | `Pesada` |
| **`Amedrontado`** | `41,40` | `8,15` | `Pesada` |
| **`Envenenado`** | `36,00` | `7,09` | `Pesada` |
| **`Atordoado`** | `36,00` | `7,09` | `Pesada` |
| **`Calado`** | `24,00` | `4,72` | `Média` |
| **`Enfeitiçado`** | `24,00` | `4,72` | `Média` |
| **`Lento`** | `14,70` | `2,89` | `Leve` |
| **`Incapacitado`** | `11,00` | `2,17` | `Leve` |
| **`Derrubado`** | `8,45` | `1,66` | `Leve` |
| **`Agarrado`** | `5,40` | `1,06` | `Leve` |
| **`Desarmado`** | `3,45` | `0,68` | `Leve` |
| **`Surdo`** | `0,00` | `0,00` | `Leve` |

**Seis `Leve`, duas `Média`, cinco `Pesada`.**

> **O `Petrificado` saiu na v0.139, e é decisão do Mizuki:** *"ela segue um balanceamento que não planejo ter no sistema"*. **Ele era a mais cara da régua, em `19,73` fatias** — `217%` do teto da `Pesada` —, e o argumento que ele carregava passou para o `Impedido`. *A remoção foi do sistema inteiro: esta peça, o `conferir-dano.py`, o gerador do manual e os cinco lugares do livro.*

### 2.3 O nível de uma condição é o tier dela

***Decisão do Mizuki:*** **o nível de uma condição é `Leve`, `Média` ou `Pesada` — os mesmos três tiers de preço do manual —, e o custo em energia é equivalente a ele.**

> **Tirar uma condição custa `1` ponto de energia por nível: `1` para `Leve`, `2` para `Média`, `3` para `Pesada`.**

**A escada de quem cura cai da própria regra, e ninguém a desenhou:**

| quando | teto por uso | alcança |
|---|---|---|
| `Enxerto` do `Sutura`, no nível 11 | `maestria` = `2` | `Leve` e `Média` |
| maestria `3`, no nível 17 | `3` | e `Pesada` |
| `Cerzido` do `Sutura`, no nível 27 | `maior Classe` = `7` | tudo, com folga para curar junto |

> **E ela bate, degrau por degrau, com a escada de exaustão da peça 10 §4.** *Aquela tem três degraus numerados, e tirar o terceiro custa `3` de energia — então ela só sai a partir da maestria `3`, que é o nível 17.* **Duas escadas construídas separadas, e as duas caem em `1 · 2 · 3` com a mesma virada no mesmo nível.**

> **O `Enxerto` já cobrava *"`1` PE por nível da condição"* desde a v0.84, e nível nenhum existia.** *A entrega dizia que condição sem nível declarado conta como nível `1`* — então, até esta peça, tirar `Impedido` custava o mesmo que tirar `Surdo`.

### 2.4 Quatro coisas que a conta achou, e nenhuma foi procurada

**O `Surdo` valia zero, e por isso ele ganhou uma linha na v0.104.** *Até a v0.103 ele só fazia falhar teste que precise de audição, e não existe teste desses em combate neste sistema — era uma condição com preço de `Média` no manual e entrega nenhuma.* **Hoje ele também dá `−2` na iniciativa**, e a conta disso está no §3.7. *Na régua desta seção ele continua em `0,00`, porque iniciativa não é dano — e isso é sobre a régua, não sobre a condição.*

**O `Incapacitado` é a segunda mais barata das treze, e o manual cobra `Pesada` por ela.** *Metade dela — "você não pode `Bloquear`" — vale praticamente zero, e a peça 23 §5.1 é quem mede.* **A outra metade, o crítico garantido no corpo a corpo, vale `11,00`.** *O que faltava era o tamanho.*

**O `Impedido` engole o `Cego`.** *Ele tem as duas linhas do `Cego` — desvantagem nos ataques do alvo e vantagem para quem o ataca — mais deslocamento zero.* **Até a v0.103 os dois custavam `Média` no manual, e o `Impedido` era a melhor compra da tabela de Controle inteira.** *Hoje os dois custam `Pesada`, e a diferença entre eles caiu para `1,10×` — dominância que o filtro aceita.*

**Duas passam do teto da `Pesada`, e o manual já diz o que fazer com isso.** *O `Cego` fica em `115%` e o `Impedido` em `127%`.* **A regra que o manual dá para a Restrição escrita à mão, virada do avesso, resolve:** *"se a dor que você escreveu parece valer mais que uma Média, ela provavelmente são duas Restrições disfarçadas de uma — separe."* **Uma condição que passa do teto da `Pesada` é mais de uma condição escrita como uma**, e o `Impedido` diz isso no próprio texto: ele é o `Cego` inteiro mais deslocamento zero, que é o que o parágrafo acima já mede em `1,10×`.

> **Eram três até a v0.139, e a terceira era o `Petrificado`, em `217%`.** *Ele era o exemplar mais claro deste argumento — `Incapacitado`, mais deslocamento zero, mais não perceber nada, mais vantagem para quem ataca, tudo vendido como uma condição só.* **Com ele fora, quem carrega o argumento é o `Impedido`, que prova a mesma coisa com metade da força.**

### 2.5 O que a régua reconstrói, e o que ela conserta

**Ela reproduz o `Abalo` exato.** *A Manha da Massa preça `Derrubado` permanente em `8,45` de dano por rodada, com as mesmas duas linhas.* **A régua devolve `8,45`, e com a trava de `60%` devolve a `1,00` fatia publicada.**

**E ela conserta o `Punho`.** *O `Derrubado` do nível 11 estava marcado, no `DESENHO-trilhas.md`, como "não reconstrói de lugar nenhum" — o único número da Trilha sem derivação escrita.*

> **Ele reconstrói: o `8,66` publicado é o `Derrubado` PERMANENTE, a `2,5%` de distância do `8,45`.**
> **Mas o `Encontrão` não é permanente.** O texto dele escreve dois portões: *"um alvo **que você acertou** faz um **Teste de Resistência de Vigor**"*.

| portão | taxa | dono |
|---|---|---|
| você acertou, com dois ataques no nível 30 | `75%` | é o mesmo gate do `Engate`, na mesma Trilha |
| o alvo falhou o Teste de Resistência | `45%` ⚠ | peça 1 §6 — **o dono mudou na v0.117, e a v0.119 mediu: contra o alvo treinado é `35%`** |
| **juntos** | **`33,8%`** | |

**Com os portões o degrau vale `2,85` de dano por rodada, que é `0,56` fatia — e não `1,71`.**

> **⚠⚠ Os dois portões desta tabela deixaram de ter dono na v0.117, e o número não foi refeito.** *O `45%` era a falha de um Teste de Resistência plano de `55%`; hoje o TR **treinado** falha `35%` e o **sem treino** falha `40%` no nível 2 e `55%` no 30.* **E o `75%` é `1 − (1 − 0,50)²`, com o acerto de `50%` que a peça 1 §6 publicava; ele hoje é `55%`, então dois ataques dão `79,75%`.**
>
> *Refazer esta conta muda o `Punho`:* **`0,44` fatia lendo o TR treinado, `0,69` lendo o sem treino, contra os `0,56` publicados.** *As três cabem na banda — o `Punho` fica entre `4,82` e `5,07` de `5,00` —, mas o número parou de ser derivado.* **Não foi mexido aqui de propósito: ele é um de oitenta e nove, e consertar um só produz um catálogo com dois modelos dentro.** *O escopo está registrado no `ESTADO-ATUAL`.*

| o `Punho`, de `5,00` fatias | |
|---|---|
| publicado até a v0.102 | `6,09` — estourava `22%`, aceito por decisão |
| **com o portão que o próprio texto escreve** | **`4,94` — cabe** |

> ***Decisão do Mizuki: corrigir o preço e deixar em `4,94`.*** *As `0,06` fatia de folga são ruído — o projeto já tratou `0,16` como ruído antes, e ela vale `0,30` de dano por rodada.* **Nenhuma linha de texto de mesa se moveu: o que estava errado era a conta, e não o desenho.**

> **⚠ E o estouro declarado sai do documento.** *Ele estava escrito como escolha, com o motivo do Mizuki junto — "a maioria das habilidades são situacionais e de RP".* **A frase fica, marcada como superada, porque o argumento continua valendo para o dia em que outra Trilha estourar.**

---

## 3. As treze condições

*Escritas na v0.95, na peça 1. Mudaram de casa nesta versão, com o nível acrescentado.*

**O manual já cobrava por condição desde sempre e listava os nomes sem dizer o que nenhum deles fazia.** ***Decisão do Mizuki na v0.95: usar as do d20 para tudo que já tem nome lá, e escrever à mão só as que precisam ser diferentes.***

### 3.1 As seis de nível `Leve`

| condição | nível | o que faz |
|---|---|---|
| **`Lento`** | `Leve` | seu deslocamento cai pela metade e você não usa Ação Bônus |
| **`Incapacitado`** | `Leve` | **você não pode `Bloquear`, e todo ataque corpo a corpo contra você é crítico** |
| **`Derrubado`** | `Leve` | você está no chão. Só se move rastejando, tem desvantagem nos seus ataques, e quem ataca você **a até 1,5 m tem vantagem** — quem ataca de longe tem desvantagem |
| **`Agarrado`** | `Leve` | seu deslocamento é `0`. Acaba se quem agarrou ficar `Incapacitado`, ou se alguma coisa tirar você do alcance dele |
| **`Desarmado`** | `Leve` | a sua arma está no chão ou na mão de outro. Você bate desarmado até pegar de volta |

> **⚠ O preço do `Desarmado` ficou devendo desde a v0.122, e o motivo é a peça 3 §3.2.** *Ela fixou que sacar ou guardar UM item não custa nada — então quem carrega arma reserva saca outra de graça, e a condição custa zero para ele.* **Os `3,45` de dano por rodada da §2.2 descrevem hoje só a ficha sem reserva.** *Não foi corrigido lá porque repreçar uma condição mexe na régua das treze e no catálogo de Melhorias do manual.*
| **`Surdo`** | `Leve` | você não ouve. Falha automático em teste que precise de audição, e **`−2` na iniciativa** |

### 3.2 As duas de nível `Média`

| condição | nível | o que faz |
|---|---|---|
| **`Calado`** | `Média` | você não conjura. Nada que precise de voz, gesto ou Selo sai |
| **`Enfeitiçado`** | `Média` | você não ataca quem enfeitiçou nem mira efeito nocivo nele, e ele tem vantagem em teste social contra você |

### 3.3 As cinco de nível `Pesada`

| condição | nível | o que faz |
|---|---|---|
| **`Impedido`** | `Pesada` | seu deslocamento é `0`, você tem desvantagem nos seus ataques e no Teste de Resistência Físico, e quem ataca você tem vantagem |
| **`Cego`** | `Pesada` | você não enxerga. Falha automático em teste que precise de vista, tem desvantagem nos seus ataques, e quem ataca você tem vantagem |
| **`Amedrontado`** | `Pesada` | desvantagem em ataque e teste enquanto enxergar a fonte do medo, e você não se aproxima dela de vontade própria |
| **`Envenenado`** | `Pesada` | desvantagem nos seus ataques e em todo teste de perícia |
| **`Atordoado`** | `Pesada` | **você perde a Ação Padrão e não usa reação.** *Quem tem mais de uma Ação Padrão no turno — um chefe, um capanga grande — perde **uma**, não todas* |

> **Só as de nível `Pesada` dão Teste de Resistência no fim de cada turno do alvo, e só cabe uma delas por feitiço.** *Até a v0.103 essas duas linhas andavam com a `Condição Maior`, que era um pacote de cinco nomes.* **Elas passaram a andar com o degrau de cima porque é ele que precisa de amortecedor** — e as cinco de antes não eram as cinco mais duras: o `Incapacitado` estava lá dentro, e ele é a segunda mais barata das treze.

> **⚠⚠ As duas colunas viraram uma na v0.104, e a que ficou é o nível.** *Até a v0.103 o manual cobrava `Média` por qualquer uma das nove `Menor` e `Pesada` por qualquer uma das cinco `Maior` — um preço só para coisas que valem de `0,00` a `11,55` fatias.* **Hoje o nível faz as duas coisas:** ele é o preço de **comprar** a condição num feitiço e é o custo em energia de **tirar** ela. *A conta que decidiu isso está no §3.6.*

### 3.4 As duas que não seguem o d20, e por quê

***Decisão do Mizuki na v0.95.*** **`Atordoado` e `Incapacitado` atacam eixos diferentes, e não se aninham** — o que no d20 são três linhas que herdam uma da outra, aqui são duas que não se tocam.

| | o eixo que ela ataca |
|---|---|
| **`Atordoado`** | tira **parte do turno** — uma Ação Padrão e a reação. Você continua se defendendo |
| **`Incapacitado`** | não tira turno nenhum: tira a **defesa**. Você age e não se protege |

> **`Paralisado` não existe como condição, e é decisão.** *Ele era o nome da que hoje se chama `Atordoado`.* **Um terceiro degrau que fosse a soma dos dois só teria sentido se custasse mais que `Pesada`, e a escada de preço do manual não tem degrau acima dela.**

> **⚠⚠ E metade do `Incapacitado` vale zero — mas o motivo mudou na v0.143, e o novo é mais forte.** *Até a v0.142 esta seção dizia que a metade do `Bloquear` não contava porque ele era **regra opcional que nem toda mesa liga**.* **O `Bloquear` virou a peça 23 e passou a valer em toda mesa, e a metade continua valendo zero — por outro motivo:**
>
> > **O `Bloquear` é NEUTRO por construção.** *A média de `2d10` é `11`, que é exatamente o que a Defesa parada já supõe.* **Tirar de alguém uma rolagem cuja média é o número que ela substitui não tira nada.**
>
> *O que sobra são os dois extremos de cerca de `1%` — o `Aparar` e a `Brecha` —, e eles quase se cancelam.* **Medido por enumeração completa das `2.000` combinações, a metade vale `+0,02` de dano por rodada**, e o `Incapacitado` iria para `11,02`. *Abaixo da precisão que esta régua carrega: o golpe simples que entra nela varia `3,0` entre o nível 2 e o 30.* **O número publicado no §2.2 fica em `11,00`.**
>
> **Esta peça não precisa saber a geometria do `Bloquear` — ela precisa saber que ele é neutro, e quem prova isso é a checagem 1 do `conferir-bloquear.py`.** *É a única checagem do projeto que existe para sustentar um número de outra peça: se a neutralidade quebrar, o preço desta condição fica errado e ninguém mais estaria olhando.*

> **O `Atordoado` cobra `uma` Ação Padrão de propósito.** *Um chefe do manual age mais de uma vez por rodada; tirar todas com uma condição só faria uma linha de feitiço apagar o turno de um chefe inteiro.* **Tirar uma ação de três é caro sem ser apagar a cena.**

### 3.5 As três que ficaram de fora, com o motivo escrito

| não é condição aqui | por quê |
|---|---|
| **`Inconsciente`** | ***decisão do Mizuki:*** aqui isso é **cair morrendo**, e já tem regra própria — a peça 1 §5.5, com as duas escolhas e a janela de três rodadas. *Uma condição de uma rodada com o mesmo nome faria a mesa confundir o pior estado do jogo com um efeito que passa sozinho.* |
| **`Exaustão`** | já existe, e é da **peça 10**. Ela é relógio de descanso, não efeito de combate |
| **`Invisível`** | é **benefício**, e as Condições do manual são compradas para aplicar num alvo. *Aplicar `Invisível` num inimigo é pagar `Média` para ajudar ele.* |

### 3.6 A Melhoria `Condição`, e por que ela é uma só

***Decisão do Mizuki na v0.104:*** **a `Condição Menor` e a `Condição Maior` viram uma Melhoria só, chamada `Condição`, e o preço dela é o nível da condição que você escolheu.**

**A alternativa estava na mesa e foi medida.** *Ela era manter as duas Melhorias e só promover as três subvendidas — o `Cego`, o `Impedido` e o `Envenenado` — para `Maior`.* **A conta reprovou ela, e não por pouco.**

| | pior espalhamento dentro de um degrau |
|---|---|
| o manual até a v7.8 | **`17,00×`** — o `Impedido` contra o `Desarmado`, os dois por `Média` |
| promover as três, mantendo os dois pacotes | `9,11×` — o `Petrificado` contra o `Incapacitado` *(medido na v0.104, com o `Petrificado` ainda na lista)* |
| **o nível como preço** | **`4,26×`** — o `Lento` contra o `Desarmado` |

> **O filtro de dominância deste projeto reprova a partir de `3,00×`.** *Nenhuma das três passa* — e a razão disso não era a escolha, era a escada: **`4,26×` era o piso de qualquer corte em três degraus.** *Busca exaustiva sobre as catorze, na v0.104; nenhuma outra partição em três fazia melhor.* **O que sobrava de dominância era o preço de a tabela do manual ter três degraus e as condições valerem de `0,00` a `100,25` de dano por rodada.**

> **⚠⚠ A v0.139 tentou refazer o corte depois de o `Petrificado` sair, e a tentativa REPROVOU.** *Com treze condições, uma busca exaustiva sobre o espalhamento acha uma partição de `2,44×` — a que sobe o `Lento` e o `Incapacitado` para `Média`.* **Ela foi aplicada, rodada contra os validadores, e desfeita.**
>
> **O que ela quebrou é a checagem 3, que é o invariante desta peça:** *o valor medido de cada condição tem de cair na **banda** que o nível dela implica, e as bandas saem da tabela de preço do manual — `1/7`, `2/7` e `3/7` da Rotina.* **No nível 30 o teto da `Leve` é `15,43` de dano por rodada. O `Lento` vale `14,70` e o `Incapacitado` `11,00`: os dois cabem em `Leve` pela conta.** *Pôr os dois em `Média` faz o jogador pagar preço de `Média` por coisa que vale `Leve`.*
>
> ***A conclusão, e ela é o oposto do que a busca sugeria:*** **a partição não é escolha livre — a banda a obriga.** *Ela força `6 Leve · 2 Média · 3 Pesada`, mais o `Impedido` e o `Cego` acima do teto, que é exatamente o que está publicado.* **O `4,26×` do degrau `Leve` é o preço de obedecer a banda, e não falta de otimização.**
>
> *Fica registrado como lição nº 8 pelo texto: a busca mediu **espalhamento**, que é livre; a peça mede **banda**, que é derivada. Otimizar o eixo errado produz um resultado que parece melhor e reprova na checagem que importa.*

**O que muda de verdade na mesa:** dez das treze trocam de degrau — três sobem e sete descem.

| sobe | `Cego`, `Impedido` e `Envenenado`, de `Média` para `Pesada` |
|---|---|
| **desce** | `Enfeitiçado` de `Pesada` para `Média`; `Lento`, `Incapacitado`, `Derrubado`, `Agarrado`, `Desarmado` e `Surdo` de `Média` para `Leve` |
| **fica** | `Amedrontado` e `Atordoado` em `Pesada`; `Calado` em `Média` |

> **O `Impedido` deixa de ser a melhor compra da tabela de Controle.** *Ele entregava `11,55` fatias pelo mesmo preço que o `Desarmado`, que entrega `0,68`.* **Era a maior dominância viva do manual, e a régua da seção 2 existia para achar ela.**

**Dois dos trinta e cinco feitiços prontos mudam, e os dois porque o `Derrubado` barateou:**

| feitiço | antes | agora |
|---|---|---|
| `Palma Trovejante`, Classe 2 | `5d8 = 22` | **`6d8 = 27`** |
| `Vala Comum`, Classe 5 | `9d8 = 40` | **`11d8 = 49`** |

*A `Rede` e a `Prisão de Sombras` carregam `Atordoado`, que já era `Pesada` e continua — nenhuma das duas se move.* **A tabela de Ampliar da `Palma Trovejante` refaz junto: `6d8 · 8d8 · 14d8` nas Classes 2, 3 e 5, e a proporção contra o teto sobe de perto de `60%` para perto de `70%`.**

> **⚠ E a arrumação achou um erro vivo na tabela de Controle do manual.** *A última linha dela é um feitiço de Classe 5 que gasta tudo em Controle e sai com `0d8`, e ela publica `Lento (+3)`.* **O `Lento` devolve `Média` desde a v7.3, que na Classe 5 são `5` pontos e não `3`** — com o preço certo aquela linha dá `2d8`, e o exemplo do `CD +2` deixava de existir. *A linha passa a usar o `Parado`, que devolve `Leve` e vale os `3` que a conta pede.* **É o mesmo defeito que a v7.3 já tinha deixado na tabela de Ampliar: mudança de preço que não voltou nos exemplos que citavam o preço velho.**

**Uma coisa que a conta NÃO resolve, e ela virou a seção seguinte:** *o `Surdo` lê `0,00` nesta régua e continua comprável.* **Qualquer degrau que contenha ele tem dominância infinita no papel**, e o `Leve` é onde ele cabe. *A busca exaustiva concorda: a melhor partição possível põe o `Surdo` sozinho num degrau, e degrau para ele o manual não tem.* **O §3.7 conta o que foi feito com ele, e por que o número não se mexe mesmo assim.**

### 3.7 O `Surdo`, e o `−2` na iniciativa

***Decisão do Mizuki na v0.104:*** **o `Surdo` fica comprável, continua `Leve`, e passa a dar `−2` na iniciativa.**

**Isso não é regra caseira: é a regra do d20 de 2003, e é o 5e que largou ela.** *A `Deafened` do SRD 3.5 diz, com todas as letras: `−4` de penalidade em testes de iniciativa, falha automática em `Listen`, e `20%` de falha ao conjurar com componente verbal.* **O 5e de 2014 cortou as duas primeiras e ficou só com a terceira linha**, e é dessa versão encolhida que o `Surdo` deste sistema tinha nascido.

*As outras duas linhas do 3.5 não entram:* **o `Listen` já é a linha de audição que a condição tem**, e a falha de conjuração é o que o `Calado` faz aqui — e ele custa `Média`.

**Quanto custa o `−2`, na moeda que a peça 3 §5 usa.** *A conta é a mesma da tabela do `Adianta`, e ela reproduz aquela tabela nos quatro pontos publicados antes de responder qualquer coisa nova.*

| na iniciativa | você age antes | perde | em pontos de Destreza |
|---|---|---|---|
| normal | `52,50%` | — | — |
| **`−2`, o `Surdo` daqui** | **`42,75%`** | **`9,75` pontos percentuais** | **`2,05`** |
| `−4`, o `Surdo` do 3.5 | `34,00%` | `18,50` pontos percentuais | `3,89` |

> **O `−4` do 3.5 não cabe aqui, e a causa é a escala do atributo.** *Lá o modificador de Destreza vai de `−5` a `+5` e a iniciativa é `d20 + Des`; aqui o atributo é o número cru, e uma ficha de nível 30 anda por volta de `6`.* **`−4` seria tirar quase dois terços do que a Destreza mais alta do jogo compra em iniciativa, por uma condição `Leve`.** *O `−2` custa dois pontos de Destreza, que é uma dor grande e não uma amputação.*

> **⚠ E ele continua valendo `0,00` na régua da seção 2.** *Não é falha do conserto: é a régua.* **A peça 15 §3.1 já rodou o contra-teste, e ele é publicado:** a pergunta *"que fração do meu dano da rodada cai antes de o inimigo agir"* dá **`52,5%` em todas as montagens**, porque iniciativa **reordena** o turno e não tira ação de ninguém. *Aquela peça matou a saída A das Invocações por causa desse eixo, e escreveu que ele existe e que a peça 6 §4 não o preça.* **Então o `Surdo` deixou de não fazer nada na mesa sem deixar de ler zero no papel** — e o `0,00` do §2.2 fica, com este ponteiro do lado.

---

## 4. Os tipos de dano

*Decidido na v0.73, escrito na peça 1 na v0.74, e mudou de casa nesta versão.*

> **Catorze tipos, em três grupos.**
>
> | grupo | tipos | do dano recebido |
> |---|---|---|
> | **Físicos** | `Cortante` · `Perfurante` · `Concussão` | **60%** |
> | **Elementais** | `Fogo` · `Frio` · `Elétrico` · `Ácido` · `Trovejante` · `Veneno` | **30%** |
> | **Especiais** | `Radiante` · `Necrótico` · `Psíquico` · `Energia Reversa` · `Alma` | **10%** |

> **⚠ O `Alma` é o único dos catorze que não bate só na vida, e a máquina dele NÃO é desta peça.** *Ele tira `1` de vida, `1` de Integridade e derruba a vida máxima em `1`, e tem quatro estágios em cima disso.* **Tudo isso é a peça 24**, que fechou na v0.145 — *aqui ele é um tipo de dano como os outros treze, e é só isso que esta peça afirma sobre ele.*

**Os Temas do manual não são taxonomia, e é por isso que esta lista existe.** *Decisão do Mizuki:* eles são **exemplos para quem cria técnica**, não uma classificação fechada do que o dano pode ser. **A colisão entre as duas coisas é aceita e fica declarada** em vez de esquecida:

| o tipo | colide com |
|---|---|
| `Fogo` · `Ácido` · `Veneno` | são **Temas** no manual, com o mesmo nome |
| `Cortante` · `Trovejante` · `Alma` | estão **dentro** de `Passo Cortante`, `Palma Trovejante` e `Toca a Alma` |

> **⚠ O peso dos três grupos é PREVISÃO e não tem dono.** `04-playtest/` está vazia desde a v0.1, e `60/30/10` é palpite calibrado contra o que uma mesa de fantasia costuma jogar em cima do grupo. **É o número que decide quanto vale toda resistência do sistema**, e o primeiro que a mesa vai corrigir.
>
> **O que ele já decide hoje:** o `Alicerce` do `Muro` cobra por tipo, e o palpite do Mizuki reproduziu na conta — ele disse *"diria que ocupa 2,0 de fatia se for só contra físicos"*, e os três Físicos dão `60%` do dano recebido, que são `10,17` de dano por rodada, **`2,00` fatias exatas.**

| quantos tipos você resiste | bate em | vale |
|---|---|---|
| 1 | 20% | 0,67 fatia |
| **2** | 40% | **1,33** |
| 3 — os Físicos inteiros | 60% | 2,00 |
| **4** | 65% | **2,17** |

**Resistir a quatro tipos fura a cerca da peça 5 §4 ao pé da letra, e está aceito.** Aquela cerca autoriza *"resistência a um tipo"*, no singular, e proíbe *"desconto em tudo"*. **Quatro de catorze não é desconto em tudo** — é o que a cerca existe para barrar, e ela continua barrando. *Decisão do Mizuki, registrada com o motivo.*

---

## 5. Cobertura

*Escrita na v0.94, na peça 1, e mudou de casa nesta versão.* **Ela não existia, e treze menções pela pasta já contavam com ela** — inclusive um degrau de nível 27 que promete *"a cobertura para de significar alguma coisa"*, que é uma entrega prometendo apagar uma regra que ninguém tinha escrito.

***Decisão do Mizuki: a métrica é a do d20, igual.*** *Mesmo motivo dos metros das armas na peça 14: cobertura não tem preço neste sistema, então o número não sai de conta daqui — ele só precisa ser o mesmo em sete mesas, e uma tabela que todo mundo já conhece resolve isso de graça.*

| cobertura | o que ela dá | exemplo |
|---|---|---|
| **Parcial** | **`+2` de Defesa e `+2` no Teste de Resistência Físico** | mureta, tronco, uma criatura no caminho |
| **Boa** | **`+5` de Defesa e `+5` no Teste de Resistência Físico** | seteira, olhando por cima de uma parede, metade do corpo atrás de um canto |
| **Total** | **você não pode ser escolhido como alvo, e ponto** | parede inteira, do outro lado da porta |

**Vale contra ataque e contra efeito que venha do outro lado da cobertura, e só.** *Quem está atrás de uma mureta não ganha nada contra quem já está do lado dele.*

**Só a maior conta.** *Duas coberturas parciais não viram uma boa.*

> **O Teste de Resistência é o Físico, e não "o de Destreza".** *A fonte fala em salvaguarda de Destreza; aqui o TR Físico é o que ocupa esse lugar, e ele é travado em Força ou Destreza na criação.* **Quem travou em Força também se abaixa atrás de uma mureta** — trocar isso por "só quem travou em Destreza" criaria uma segunda regra de cobertura para metade das fichas.

> **A `Total` não tem número de propósito.** *Ela é a única das três que não é um bônus: é a ausência de alvo legal.* **Um efeito que pega área continua alcançando quem está atrás dela, se o efeito não precisar de linha de efeito** — e essa parte é do manual, não daqui.

---

## 6. A penalidade de arma — sem treino e sem o requisito

**Três documentos apontavam para cá:** *a peça 14 §8 item 15, a peça 16 §9, e a seção "em aberto" desta peça.* **A peça 14 fecha as 52 armas, a divisão simples/marcial e o requisito de Força, e nenhum dos três dizia o que acontece com quem pega uma arma que não é dele.**

> **Sem treino na categoria, você tem desvantagem na rolagem de ataque com aquela arma.**
> **Sem o requisito de Força da arma, o seu deslocamento cai `3 m` enquanto você a estiver empunhando.**

### A do requisito atravessou inteira; a do treino precisou de tradução

**A regra do requisito é a mesma do d20 de 2024, e nem o número mudou.** *Lá ela é de proteção: "se a tabela mostra um valor de Força na coluna Força, aquela proteção reduz o deslocamento de quem a veste em `10` pés, a menos que ele tenha Força igual ou maior".* **`10` pés são `0,3048 × 10` = `3,05 m`, e esta peça anda em `1,5 m`** — os `3 m` são o mesmo passo, não um arredondamento generoso. *E o requisito de Força de arma desta peça já existe desde a v0.47, na peça 14 §5.5, gateando `d10` e `d12` no corpo a corpo.*

**A do treino não atravessava quando esta seção foi escrita, e passou a atravessar na v0.117.** *No d20, usar arma sem treino tira o bônus de proficiência da rolagem de ataque.* **Naquela época a rolagem daqui não tinha esse termo** — a peça 1 escrevia `Ataque corpo a corpo = d20 + Força`, e a maestria só entrava em perícia e em conjuração.

> ***Decisão do Mizuki na v0.117: as duas valem, e é para doer.*** **Sem treino você não soma a maestria E rola com desvantagem.**
>
> *Medido, as duas cobram coisas diferentes:* **a desvantagem custa `25` pontos percentuais em todo nível; perder a maestria custa `5pp` no nível 2 e `20pp` no 30.** *A primeira é plana e a segunda cresce — juntas, empunhar sem treino fica pior a cada nível, que é exatamente o que se quer de uma porta fechada.*

**O que existe é desvantagem, e ela foi medida antes de ser escolhida:**

| | |
|---|---|
| desvantagem na rolagem | `25` pontos percentuais, lidos da peça 11 §8 |
| sobre um acerto de `50%` | `−50%` do que sai |
| contra a Rotina de `108` | **`54,00` de dano por rodada** |
| no d20, isso é | **exatamente o bônus de proficiência de `+5`** — cada `+1` são `5` pontos percentuais |

> **`+5` é a faixa dos níveis `13` a `16` do d20, e o topo dele é `+6`.** *Então a tradução não é livre: ela cai um passo abaixo do maior valor que a regra original tira, e não em cima de um número inventado.*

### E ela não é preço: é porta fechada

**As duas penalidades somadas custam `33,8` vezes o que a arma inteira entrega.**

| | de dano por rodada |
|---|---|
| desvantagem na rolagem | `54,00` |
| deslocamento `−3 m` | `1,80` — o metro vale `0,60`, na peça 5 §4 |
| **somadas** | **`55,80`** |
| a arma inteira — o fundo de duas mãos, `5` pontos a `0,33` | `1,65` |

> **Ninguém paga trinta e três vezes para usar uma coisa.** *E é isso que o d20 faz também: a penalidade dele não existe para ser paga, existe para você ir buscar o treino.* **Uma penalidade que dá para pagar é preço, e preço abre a porta — o que a peça 14 decidiu sobre acesso vira decoração no dia em que empunhar sem treino for uma escolha de montagem.**

*A conta acima usa a Rotina inteira de propósito.* **Um personagem que vive de arma tem a Rotina em arma**, e é sobre ele que a porta fecha. *Quem só pega a arma do chão numa cena perde muito menos, porque perde só aquela rodada — e isso é o que a regra quer: emprestar arma numa emergência continua sendo uma coisa que acontece na ficção.*

---

## 7. As onze checagens do `conferir-dano.py`

*Escritas antes do validador, que é o método que fez a peça 15 caber numa versão só contra as seis que a peça 14 gastou.*

| # | o que ela confere |
|---|---|
| **1** | **as âncoras existem nos donos.** Cada número que a régua usa aparece no documento que esta peça declara como dono dele. Âncora que sumiu do dono é régua sem chão |
| **2** | **a régua reconstrói as treze.** Cada valor da tabela do §2.2 é recalculado a partir das âncoras e comparado com o publicado. *E, desde a v0.104, ela também reconstrói a razão entre as duas réguas de rolagem — e cobra que ela seja exatamente o dobro da razão das bases* |
| **3** | **o nível de cada condição sai da banda.** O `Leve`/`Média`/`Pesada` publicado bate com `1/7`, `2/7` e `3/7` da Rotina, e as bandas saem da tabela de Classe do manual |
| **4** | **as treze batem com o manual**, nas duas direções: nome e **nível**, tabela por tabela — e o manual vende **uma** Melhoria `Condição`, cobrando o nível. *Lê o `.docx`, então **pula** sem o `python-docx` — e diz que pulou* |
| **5** | **nenhuma condição fica sem nível**, e o nível é um dos três. Guarda de contagem: são treze, seis `Leve`, duas `Média` e cinco `Pesada` |
| **6** | **a escada de quem cura fecha.** O teto de energia por uso em cada faixa de maestria cobre exatamente os tiers que o §2.3 publica, e ela bate com a escada de exaustão da peça 10 |
| **7** | **os catorze tipos de dano**, os três grupos, os pesos `60/30/10` e a tabela de quantos tipos você resiste, recontada em vez de guardada |
| **8** | **a cobertura**: os três degraus, os dois números de cada um, e a `Total` sem número |
| **9** | **as duas entregas publicadas que aplicam condição** — o `Abalo` do `DESENHO-manhas.md` e o `Encontrão` do `DESENHO-trilhas.md` — batem com a régua, com o portão que o texto de cada uma escreve |
| **10** | **nenhum valor de regra escrito dentro do validador.** Todo número vem do documento dono, e a checagem falha se algum ficar guardado no código |
| **11** | **a penalidade de arma da seção 6**: as duas linhas estão escritas, o `3 m` bate com o `10` pés do d20, e a desvantagem reconstrói em `54,00` a partir das âncoras — e a soma das duas contra a entrega da arma inteira |

> **A checagem 9 é a que esta peça existe para ter.** *Ela é a única que sai da pasta, junto com a do `conferir-catalogo.py` — e é ela que pegaria o `Punho` de novo se alguém reescrever o texto da entrega sem mexer no preço, ou o contrário.*

### As vinte e sete perturbações, em cópia isolada

*Com a base conferida verde na cópia antes de cada uma, com o `diff` comparado antes e depois, e com o veredito lido da checagem que estava sendo testada — nunca o código de retorno do programa.* **As quinze de baixo são da v0.104**, e as sete primeiras delas atravessam o `.docx`: perturbar o manual quer dizer mexer no gerador e rodar o `node make.js` de novo.

| checagem | perturbação | esperado | deu |
|---|---|---|---|
| 1 | a âncora do preço de aliado some do dono | acende | acende |
| 2 | o valor publicado de uma condição muda | acende | acende |
| 3 | o nível publicado sai da banda | acende | acende |
| 4 | uma condição some da peça | acende | acende |
| 5 | o nível do texto de mesa diverge da régua | acende | acende |
| 6 | os três degraus de exaustão somem da peça 10 | acende | acende |
| 7 | os pesos dos três grupos param de somar `100%` | acende | acende |
| 7 | a lista de tipos perde o rótulo de **previsão** | acende | acende |
| 8 | a cobertura `Total` ganha número | acende | acende |
| **9** | **o preço do `Derrubado` do `Punho` muda e o texto não** | acende | acende |
| **9** | **o TEXTO da entrega perde o Teste de Resistência e o preço não** | acende | acende |
| **4** | **o `Derrubado` vira `Média` na tabela de mesa da peça** | acende | acende |
| **4** | **o `Cego` muda de tabela dentro do manual, e a peça não** | acende | acende |
| **4** | **uma condição é renomeada na peça** | acende | acende |
| **4** | **a seção `§3.3` muda de título e a extração perde o chão** | acende | acende |
| **4** | **a Melhoria `Condição` volta a cobrar um tier fixo** | acende | acende |
| **4** | **a `Condição Maior` volta a existir no manual** | acende | acende |
| **4** | **o cabeçalho `Nível Pesada` do manual vira `Maior`** | acende | acende |
| **4** | **contra-teste: mexer no texto do `Terreno`, que não é condição** | fica verde | fica verde |
| **4** | **o `−2` do `Surdo` some da tabela de mesa da peça** | acende | acende |
| **4** | **o `−2` do `Surdo` some da peça 3 §5, que é dona da fórmula** | acende | acende |
| **4** | **o `−2` do `Surdo` some do manual** | acende | acende |
| **4** | **o manual troca o `−2` do `Surdo` por `−4`** | acende | acende |
| **4** | **contra-teste: mexer no texto do `Lento`, que não toca iniciativa** | fica verde | fica verde |
| **2** | **a peça publica outra razão entre as duas réguas de rolagem** | acende | acende |
| **2** | **contra-teste: a razão publicada some da peça** | acende | acende |
| 2 | **contra-teste:** mexer em prosa sem mexer em número | verde | verde |
| 9 | **contra-teste:** mexer no texto de outro degrau do `Punho` | verde | verde |

> **⚠⚠ E o arnês achou TRÊS defeitos no validador antes de ele valer, e um deles é a lição nº 8.**
>
> **A checagem 4 comparava o manual contra a lista escrita DENTRO do validador**, e não contra a peça — então renomear uma condição na peça saía **verde**. *Uma checagem que se mede contra a própria constante, pela quarta vez em setenta versões.* **Hoje ela lê os nomes das tabelas do §3.1 e do §3.2.**
>
> **A checagem 6 procurava `três degraus` OU `degrau 3` na peça 10**, e meia porta é porta aberta: apagar uma das duas frases saía verde. *Hoje ela exige as duas.*
>
> **E duas perturbações estavam mal miradas**, trocando uma ocorrência de uma âncora que aparece duas vezes no mesmo arquivo — o que produz um *"não acendeu"* que parece prova. **O arnês ganhou um modo que troca todas as ocorrências**, e é o mesmo defeito que a v0.101 registrou com um `sed` que parou de bater.

---

## 8. Em aberto

- **A `Cicatriz` continua sem mecânica.** *A peça 1 §5.5 registra que ela é permanente, não sai no descanso, e nada mais.* **Esta peça foi escrita com o escopo que o Mizuki fechou — a régua e as três seções que mudaram de casa —, e a `Cicatriz` ficou de fora dele.** *O que precisa ser resolvido continua o mesmo: o que ela faz, se tem teto por ficha, se some algum dia, e se a `Energia Reversa` limpa Sequela.*
- **O `Surdo` lê `0,00` nesta régua mesmo depois do `−2` na iniciativa**, e o motivo é a régua e não a condição — ela mede dano por rodada, e a peça 15 §3.1 já publicou que ordem de iniciativa não move dano. *Enquanto a régua for essa, o degrau que contiver o `Surdo` vai ter dominância infinita no papel.* **O que falta é uma régua para o eixo de iniciativa**, e o projeto já tem duas decisões grandes tomadas nele — a saída A das Invocações e a recusa da iniciativa fixa da peça 3 — as duas sem número em fatia.
- ~~**As condições que impedem `Bloquear`.**~~ **FECHADA na v0.143, e a resposta já estava escrita aqui.** *O rascunho listava surpreendido, caído e agarrado como candidatos e apontava para cá; a peça 23 §5 mediu e concluiu que **só o `Incapacitado`** desliga.* **O §3.4 desta peça já dizia por quê:** *ele é a condição cujo eixo **é** a defesa, e `Atordoado` e `Incapacitado` foram separados em v0.95 justamente para não se aninharem.* **Pôr a linha no `Derrubado` ou no `Agarrado` não seria escrever regra — seria repreçar duas condições que já têm número na régua da seção 2.** *A checagem 5 do `conferir-bloquear.py` lê esta seção e falha se uma segunda condição citar `Bloquear`.*
- **Três vagas de `Desliga` da peça 13 esperam esta peça.** *Elas esperavam um alvo legal que só nascesse aqui.* **A régua da seção 2 cria alvo: o nível de uma condição é número, e a trava do `Desliga` proíbe encostar no que tem preço.** *Vale reler as três com isso na mão.*
- **⚠ As duas réguas de rolagem divergem por `9,4` vezes, e não por `4,7` — e o `4,7` publicado media outra coisa.** *A v0.103 escreveu que `+1` no seu acerto vale `10,80` (que são `10%` da Rotina de `108`), que `1` ponto percentual na rolagem de um aliado vale `0,230` (que é `1%` da ação de atacar de `23,00`), e que **"a diferença é de `4,7` vezes"**.* **O `4,7` é `108 ÷ 23,00`: a razão entre as duas BASES.** *Isso é verdade e responde outra pergunta — quanto o seu escopo é maior que o do aliado.* **Lidas por ponto percentual, que é a única forma de compará-las, elas dão `2,16` contra `0,230`, e a razão é `9,39`.**

  *A causa do fator `2` que separa os dois números é uma escolha de conversão que nunca foi declarada:* **a sua régua é RELATIVA** — a peça 15 §3.3 escreve *"`+1` no acerto = `50%` → `55%` = `+10%` de dano saído"*, então `5` pontos percentuais sobre um acerto de `50%` viram `+10%` do que sai — **e a do aliado é ABSOLUTA**, com `X` pontos percentuais virando `X%` da base. *Pela conversão relativa, `1` pp num aliado valeria `0,460` e não `0,230`.* **`9,4` = `4,7` de escopo × `2` de conversão.**

  > **O contra-teste fecha com o mesmo número, e ele já está publicado noutro documento.** *Lido pela sua régua, o `Ajudar` — que são `25` pontos percentuais — valeria `54,00` de dano por rodada em vez dos `5,75` que o `DESENHO-caminhos` publica.* **`54,00 ÷ 5,75` = `9,4`**, e o `54,00` é exatamente o que o `DESENHO-manhas` já escreve para vantagem. *Mais que uma Trilha inteira, que são `25,40`.*

  **Continua marcado e não consertado, e agora com o tamanho certo:** mexer nisso repreçaria o `Guiar`, o `Estampido` e o `Ajudar` de uma vez.
- **O valor de uma condição depende de em quem ela cai.** *Contra um capanga de `38` de dano por rodada, em vez de um chefe de `72`, seis das treze mudam de nível.* **A tabela publicada é a do chefe, porque é contra ele que as entregas de Trilha foram preçadas** — e o validador confere as duas colunas.
- **O `Impedido` é a maior da lista desde a v0.139, quando o `Petrificado` saiu.** *Ele é o `Cego` inteiro mais deslocamento `0`, e a diferença entre os dois é `1,10×` — dominância que o filtro aceita.*

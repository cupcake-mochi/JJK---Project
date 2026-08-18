# 19 · Dano e condições

**Fase 4, décima nona peça.** O que uma condição vale, quais são as catorze, de que tipo o dano é, e o que cobertura faz.

**Ela é a peça que mais gente estava esperando: vinte e seis lugares em oito documentos citam ela pelo nome.** *E metade dela já estava escrita — em três seções da peça 1 declaradas, no próprio texto, como guarda provisória.*

**O que ela acrescenta é uma coisa só, e é a que faltava: quanto vale uma condição.**

---

## 1. De onde ela veio, e o que é novo

**Três seções mudaram de casa, inteiras.** *As três estavam na peça 1 com o aviso escrito de que o dono natural era esta peça.*

| o que veio | estava em | escrita em |
|---|---|---|
| os catorze tipos de dano, em três grupos | peça 1 §8.1 | v0.74 |
| a cobertura, nos três degraus | peça 1 §8.2 | v0.94 |
| as catorze condições, e o que cada uma faz | peça 1 §8.3 | v0.95 |

**Na peça 1 as três viraram ponteiro**, com o número e o motivo. *É o mesmo trato que o `ESTADO-ATUAL` já fazia com vocabulário que ainda não tinha peça.*

**O que nasce aqui é a seção 2.** Até a v0.102 o projeto escrevia, em três documentos, que *"condição não tem conversão em fatia"* — e escrevia com razão, porque ninguém tinha feito a conta. Ela está feita.

> **⚠⚠ E ela não precisou de régua nova: precisou de ler a tabela de custo do manual.** *É o quarto exemplar do mesmo defeito em vinte versões — o Classe 0 da v0.80, a ação `Mirar` da v0.86, a `Aptidão Própria` da v0.92, e agora esta.* **O manual preça condição em dano desde sempre, e nenhum documento do projeto tinha aberto essa porta.**

---

## 2. A régua — quanto vale uma condição

### 2.1 O teto sai do manual, e ele é plano

**O manual compra condição com ponto de feitiço.** *Uma `Condição Menor` custa `Média` e uma `Condição Maior` custa `Pesada`, e cada ponto que não vira Melhoria vira `1d8` de dano — que são `4,5`.* **Então o manual sempre disse, em dano, quanto ele acha que uma condição vale.**

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

**As catorze, aplicadas num chefe, no nível 30:**

| condição | dano por rodada | fatias | nível |
|---|---|---|---|
| **`Petrificado`** | `100,25` | `19,73` | `Pesada` |
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

**Seis `Leve`, duas `Média`, seis `Pesada`.**

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

> **O `Enxerto` já cobrava *"`1` PE por nível da condição"* desde a v0.84, e nível nenhum existia.** *A entrega dizia que condição sem nível declarado conta como nível `1`* — então, até esta peça, tirar `Petrificado` custava o mesmo que tirar `Surdo`.

### 2.4 Quatro coisas que a conta achou, e nenhuma foi procurada

**O `Surdo` vale zero.** *Ele só faz falhar teste que precise de audição, e não existe teste desses em combate neste sistema.* **É uma condição com preço de `Média` no manual e entrega nenhuma.** *Fica na lista porque ela é a lista do manual, e porque fora de combate ela faz o que promete.*

**O `Incapacitado` é a segunda mais barata das catorze, e o manual cobra `Pesada` por ela.** *Metade dela — "você não pode `Bloquear`" — depende de uma regra opcional que nem toda mesa liga, e a peça 1 já registrava isso.* **A outra metade, o crítico garantido no corpo a corpo, vale `11,00`.** *O que faltava era o tamanho.*

**O `Impedido` engole o `Cego`.** *Ele tem as duas linhas do `Cego` — desvantagem nos ataques do alvo e vantagem para quem o ataca — mais deslocamento zero.* **Os dois custam `Média` no manual, e um domina o outro dentro da mesma lista.**

**Três passam do teto da `Pesada`, e o manual já diz o que fazer com isso.** *O `Cego` fica em `115%`, o `Impedido` em `127%` e o `Petrificado` em `217%`.* **A regra que o manual dá para a Restrição escrita à mão, virada do avesso, resolve:** *"se a dor que você escreveu parece valer mais que uma Média, ela provavelmente são duas Restrições disfarçadas de uma — separe."* **Uma condição que passa do teto da `Pesada` é mais de uma condição escrita como uma**, e o `Petrificado` diz isso no próprio texto: ele é `Incapacitado`, mais deslocamento zero, mais não perceber nada, mais vantagem para quem ataca.

### 2.5 O que a régua reconstrói, e o que ela conserta

**Ela reproduz o `Abalo` exato.** *A Manha da Massa preça `Derrubado` permanente em `8,45` de dano por rodada, com as mesmas duas linhas.* **A régua devolve `8,45`, e com a trava de `60%` devolve a `1,00` fatia publicada.**

**E ela conserta o `Punho`.** *O `Derrubado` do nível 11 estava marcado, no `DESENHO-trilhas.md`, como "não reconstrói de lugar nenhum" — o único número da Trilha sem derivação escrita.*

> **Ele reconstrói: o `8,66` publicado é o `Derrubado` PERMANENTE, a `2,5%` de distância do `8,45`.**
> **Mas o `Encontrão` não é permanente.** O texto dele escreve dois portões: *"um alvo **que você acertou** faz um **Teste de Resistência de Vigor**"*.

| portão | taxa | dono |
|---|---|---|
| você acertou, com dois ataques no nível 30 | `75%` | é o mesmo gate do `Engate`, na mesma Trilha |
| o alvo falhou o Teste de Resistência | `45%` | peça 1 §6 |
| **juntos** | **`33,8%`** | |

**Com os portões o degrau vale `2,85` de dano por rodada, que é `0,56` fatia — e não `1,71`.**

| o `Punho`, de `5,00` fatias | |
|---|---|
| publicado até a v0.102 | `6,09` — estourava `22%`, aceito por decisão |
| **com o portão que o próprio texto escreve** | **`4,94` — cabe** |

> ***Decisão do Mizuki: corrigir o preço e deixar em `4,94`.*** *As `0,06` fatia de folga são ruído — o projeto já tratou `0,16` como ruído antes, e ela vale `0,30` de dano por rodada.* **Nenhuma linha de texto de mesa se moveu: o que estava errado era a conta, e não o desenho.**

> **⚠ E o estouro declarado sai do documento.** *Ele estava escrito como escolha, com o motivo do Mizuki junto — "a maioria das habilidades são situacionais e de RP".* **A frase fica, marcada como superada, porque o argumento continua valendo para o dia em que outra Trilha estourar.**

---

## 3. As catorze condições

*Escritas na v0.95, na peça 1. Mudaram de casa nesta versão, com o nível acrescentado.*

**O manual já cobrava por condição desde sempre e listava os nomes sem dizer o que nenhum deles fazia.** ***Decisão do Mizuki na v0.95: usar as do d20 para tudo que já tem nome lá, e escrever à mão só as que precisam ser diferentes.***

### 3.1 As nove que o manual chama de `Menor`

| condição | nível | o que faz |
|---|---|---|
| **`Derrubado`** | `Leve` | você está no chão. Só se move rastejando, tem desvantagem nos seus ataques, e quem ataca você **a até 1,5 m tem vantagem** — quem ataca de longe tem desvantagem |
| **`Cego`** | `Pesada` | você não enxerga. Falha automático em teste que precise de vista, tem desvantagem nos seus ataques, e quem ataca você tem vantagem |
| **`Surdo`** | `Leve` | você não ouve. Falha automático em teste que precise de audição |
| **`Agarrado`** | `Leve` | seu deslocamento é `0`. Acaba se quem agarrou ficar `Incapacitado`, ou se alguma coisa tirar você do alcance dele |
| **`Impedido`** | `Pesada` | seu deslocamento é `0`, você tem desvantagem nos seus ataques e no Teste de Resistência Físico, e quem ataca você tem vantagem |
| **`Envenenado`** | `Pesada` | desvantagem nos seus ataques e em todo teste de perícia |
| **`Lento`** | `Leve` | seu deslocamento cai pela metade e você não usa Ação Bônus |
| **`Desarmado`** | `Leve` | a sua arma está no chão ou na mão de outro. Você bate desarmado até pegar de volta |
| **`Calado`** | `Média` | você não conjura. Nada que precise de voz, gesto ou Selo sai |

### 3.2 As cinco que o manual chama de `Maior`

| condição | nível | o que faz |
|---|---|---|
| **`Amedrontado`** | `Pesada` | desvantagem em ataque e teste enquanto enxergar a fonte do medo, e você não se aproxima dela de vontade própria |
| **`Enfeitiçado`** | `Média` | você não ataca quem enfeitiçou nem mira efeito nocivo nele, e ele tem vantagem em teste social contra você |
| **`Atordoado`** | `Pesada` | **você perde a Ação Padrão e não usa reação.** *Quem tem mais de uma Ação Padrão no turno — um chefe, um capanga grande — perde **uma**, não todas* |
| **`Incapacitado`** | `Leve` | **você não pode `Bloquear`, e todo ataque corpo a corpo contra você é crítico** |
| **`Petrificado`** | `Pesada` | você virou pedra. `Incapacitado`, deslocamento `0`, sem perceber nada em volta, quem ataca você tem vantagem — e você tem resistência a todo dano |

> **⚠⚠ O `Menor`/`Maior` do manual é PREÇO DE COMPRA e o nível é VALOR, e os dois discordam em dez das catorze.** *O manual cobra `Média` por qualquer uma das nove e `Pesada` por qualquer uma das cinco — um preço só para coisas que valem de `0,00` a `19,73` fatias.* **Enquanto as duas colunas existirem, cada uma serve para uma coisa:** o tier do manual diz o que custa **comprar** a condição num feitiço, e o nível diz o que custa **tirar** ela e quanto ela pesa numa entrega de Trilha.

### 3.3 As duas que não seguem o d20, e por quê

***Decisão do Mizuki na v0.95.*** **`Atordoado` e `Incapacitado` atacam eixos diferentes, e não se aninham** — o que no d20 são três linhas que herdam uma da outra, aqui são duas que não se tocam.

| | o eixo que ela ataca |
|---|---|
| **`Atordoado`** | tira **parte do turno** — uma Ação Padrão e a reação. Você continua se defendendo |
| **`Incapacitado`** | não tira turno nenhum: tira a **defesa**. Você age e não se protege |

> **`Paralisado` não existe como condição, e é decisão.** *Ele era o nome da que hoje se chama `Atordoado`.* **Um terceiro degrau que fosse a soma dos dois só teria sentido se custasse mais que `Pesada`, e a escada de preço do manual não tem degrau acima dela.**

> **⚠ E metade do `Incapacitado` depende de uma regra opcional.** *O `Bloquear` — rolar `2d10` no lugar da Defesa estática — está no `RASCUNHO-bloqueio.md` e nem toda mesa vai usar.* **Onde ele estiver desligado, o `Incapacitado` é só o crítico no corpo a corpo**, que é a metade que sempre vale. *A conta da seção 2 já preça ele assim: as duas metades somadas dão `11,00`, e a do `Bloquear` entra como zero.*

> **O `Atordoado` cobra `uma` Ação Padrão de propósito.** *Um chefe do manual age mais de uma vez por rodada; tirar todas com uma Condição Maior faria uma linha de feitiço apagar o turno de um chefe inteiro.* **Tirar uma ação de três é caro sem ser apagar a cena.**

### 3.4 As três que ficaram de fora, com o motivo escrito

| não é condição aqui | por quê |
|---|---|
| **`Inconsciente`** | ***decisão do Mizuki:*** aqui isso é **cair morrendo**, e já tem regra própria — a peça 1 §5.5, com as duas escolhas e a janela de três rodadas. *Uma condição de uma rodada com o mesmo nome faria a mesa confundir o pior estado do jogo com um efeito que passa sozinho.* |
| **`Exaustão`** | já existe, e é da **peça 10**. Ela é relógio de descanso, não efeito de combate |
| **`Invisível`** | é **benefício**, e as Condições do manual são compradas para aplicar num alvo. *Aplicar `Invisível` num inimigo é pagar `Média` para ajudar ele.* |

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

## 6. As dez checagens do `conferir-dano.py`

*Escritas antes do validador, que é o método que fez a peça 15 caber numa versão só contra as seis que a peça 14 gastou.*

| # | o que ela confere |
|---|---|
| **1** | **as âncoras existem nos donos.** Cada número que a régua usa aparece no documento que esta peça declara como dono dele. Âncora que sumiu do dono é régua sem chão |
| **2** | **a régua reconstrói as catorze.** Cada valor da tabela do §2.2 é recalculado a partir das âncoras e comparado com o publicado |
| **3** | **o nível de cada condição sai da banda.** O `Leve`/`Média`/`Pesada` publicado bate com `1/7`, `2/7` e `3/7` da Rotina, e as bandas saem da tabela de Classe do manual |
| **4** | **as catorze batem com o manual**, nas duas direções: nome, grupo `Menor`/`Maior` e a lista de cada Melhoria. *Lê o `.docx`, então **pula** sem o `python-docx` — e diz que pulou* |
| **5** | **nenhuma condição fica sem nível**, e o nível é um dos três. Guarda de contagem: são catorze, nove no `Menor` e cinco no `Maior` |
| **6** | **a escada de quem cura fecha.** O teto de energia por uso em cada faixa de maestria cobre exatamente os tiers que o §2.3 publica, e ela bate com a escada de exaustão da peça 10 |
| **7** | **os catorze tipos de dano**, os três grupos, os pesos `60/30/10` e a tabela de quantos tipos você resiste, recontada em vez de guardada |
| **8** | **a cobertura**: os três degraus, os dois números de cada um, e a `Total` sem número |
| **9** | **as duas entregas publicadas que aplicam condição** — o `Abalo` do `DESENHO-manhas.md` e o `Encontrão` do `DESENHO-trilhas.md` — batem com a régua, com o portão que o texto de cada uma escreve |
| **10** | **nenhum valor de regra escrito dentro do validador.** Todo número vem do documento dono, e a checagem falha se algum ficar guardado no código |

> **A checagem 9 é a que esta peça existe para ter.** *Ela é a única que sai da pasta, junto com a do `conferir-catalogo.py` — e é ela que pegaria o `Punho` de novo se alguém reescrever o texto da entrega sem mexer no preço, ou o contrário.*

### As treze perturbações, em cópia isolada

*Com a base conferida verde na cópia antes de cada uma, com o `md5` comparado antes e depois, e com o veredito lido da checagem que estava sendo testada — nunca o código de retorno do programa.*

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

## 7. Em aberto

- **⚠⚠ O manual cobra `Média` por dez condições que a conta preça em outro tier**, e seis delas ele subvende. *`Cego`, `Impedido` e `Envenenado` valem `Pesada` e custam `Média`; `Enfeitiçado` e `Incapacitado` valem menos do que a `Pesada` que ele cobra.* **Consertar isso é mexer na tabela de Melhoria do manual e regerar o `.docx`, e é decisão do Mizuki.** *Enquanto não for, o `Impedido` é a melhor compra da tabela de Controle.*
- **A `Cicatriz` continua sem mecânica.** *A peça 1 §5.5 registra que ela é permanente, não sai no descanso, e nada mais.* **Esta peça foi escrita com o escopo que o Mizuki fechou — a régua e as três seções que mudaram de casa —, e a `Cicatriz` ficou de fora dele.** *O que precisa ser resolvido continua o mesmo: o que ela faz, se tem teto por ficha, se some algum dia, e se a `Energia Reversa` limpa Sequela.*
- **A penalidade por empunhar arma sem treino ou sem requisito.** *A peça 14 §8 e a peça 16 §9 apontam para cá.* **A saída óbvia do hobby é desvantagem na rolagem, e este projeto já mede desvantagem em `25` pontos percentuais** — o que dá para fazer com a régua da seção 2 na mão, e não foi feito nesta versão.
- **As condições que impedem `Bloquear`.** *O `RASCUNHO-bloqueio.md` lista surpreendido, caído e agarrado, e aponta para cá.* **Duas das três têm nome agora — `Derrubado` e `Agarrado` —, e a terceira não existe como condição neste sistema.**
- **Três vagas de `Desliga` da peça 13 esperam esta peça.** *Elas esperavam um alvo legal que só nascesse aqui.* **A régua da seção 2 cria alvo: o nível de uma condição é número, e a trava do `Desliga` proíbe encostar no que tem preço.** *Vale reler as três com isso na mão.*
- **A conta usa duas réguas de rolagem que não medem a mesma coisa.** *`+1` no seu acerto vale `10,80`, que são `10%` da Rotina de `108`; `1` ponto percentual na rolagem de um aliado vale `0,230`, que é `1%` da ação de atacar de `23,00`.* **Você é modelado pela Rotina inteira e o aliado por dois golpes simples**, e a diferença é de `4,7` vezes. *Mexer nisso repreçaria o `Guiar`, o `Estampido` e o `Ajudar` de uma vez, então fica marcado em vez de consertado.*
- **O valor de uma condição depende de em quem ela cai.** *Contra um capanga de `38` de dano por rodada, em vez de um chefe de `72`, seis das catorze mudam de nível.* **A tabela publicada é a do chefe, porque é contra ele que as entregas de Trilha foram preçadas** — e o validador confere as duas colunas.
- **`Petrificado` só é a maior da lista porque o grupo pode trocar de alvo.** *A resistência a todo dano dele entra como zero, com o motivo escrito.* **Se o grupo insistir em bater na estátua, ele vira negativo contra um capanga** — e isso é decisão de mesa, não de conta.

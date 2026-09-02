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

**Isso dá o preço de cada tier, em dano:**

> **`Leve` = `1/7` da Rotina · `Média` = `2/7` · `Pesada` = `3/7`.**
> **No nível 30, com a Rotina em `108`: `15,43` · `30,86` · `46,29` de dano por rodada.**

**Esses três números são o PREÇO, e não o teto.** *Eles dizem o que você deixa de causar por ter gasto aqueles pontos numa condição em vez de num dado.*

> ***⚠⚠ Até a v0.200 eles eram também o teste, e isso quebrou na v0.201.*** *A régua comparava o valor da condição com o preço dela e reprovava quem passasse.* **Mas o valor de uma condição é uma fatia da rodada do INIMIGO e o preço é uma fatia da sua** — os dois só empatam enquanto o inimigo e você entregarem a mesma coisa por rodada. *Com o chefe da tabela nova entregando `219` contra uma Rotina de `108`, oito das treze passavam do próprio preço e a `Média` esvaziava.*
>
> ***Decisão do Mizuki: não repreçar, e trocar o que a régua mede.*** *"Tem que considerar que o boss também vai poder aplicar condições."* **A régua passou a ter duas perguntas separadas, e nenhuma delas é "cabe embaixo do preço":**
>
> **1. O NÍVEL da condição é quantas ações da rodada do alvo ela nega** — *meia ação é `Leve`, uma é `Média`, uma e meia é `Pesada`*. **Isso não depende de contra quem ela cai, e é por isso que a mesma tabela serve quando o chefe usa condição num personagem.**
>
> **2. O TESTE é de dominância** — *quanto ela nega, dividido pelo dano que aqueles mesmos pontos de feitiço dariam*, contra o filtro de `3,00×` que o projeto usa em todo catálogo.
>
> **As duas reproduzem os treze níveis publicados sem mover um preço**, e o §2.2 traz as duas colunas.

### 2.2 O que cada condição entrega, medido

**Nenhum componente desta conta é escolha.** *Cada um sai de um documento dono, e o `conferir-dano.py` lê os números de lá em vez de guardar cópia.*

| âncora | valor | dono |
|---|---|---|
| a fatia | `5,08` de dano por rodada | `DESENHO-trilhas.md`, a linha de orçamento de Trilha |
| a Rotina no nível 30 | `108` | manual, a tabela de Rotina |
| chefe e capanga no nível 30 | `219` e `73` por rodada | manual, a tabela de inimigo |
| ações do chefe por rodada | o piso da banda, derivado logo abaixo | **esta peça** — o manual diz o contrário |
| vantagem e desvantagem | `25` pontos percentuais | peça 11 §8 |
| `1` ponto percentual na rolagem de um aliado | `0,230` | `DESENHO-caminhos.md`, a régua do Guia |
| a ação de atacar de um aliado | `23,00` — dois golpes simples | `DESENHO-caminhos.md` |
| mover `1,5 m` | `0,90`, então `1 m` vale `0,60` | peça 5 §4 |
| `1` ponto de arma | `0,33` por rodada | peça 14 §4 |
| o fundo de uma arma de duas mãos | `5` pontos | peça 14 §5 |
| dano evitado | converte `1` pra `1` | peça 5 §4 |
| o `20` natural, e a chance dele | `5%` | peça 1 §5.2 |
| **o escopo do crítico** | dobra **só os dados do que rolou o acerto** | peça 1 §5.2 |
| o dado do soco no teto | `d10`, então `5,5` | peça 14 §5.0.6 |

> **⚠ A linha das ações do chefe mudou de dono na v0.198, porque a antiga citava uma frase que diz o contrário dela.** *Ela publicava `3`, contra um grupo de quatro, com o dono no manual pelo `DESENHO-trilhas.md`.* **O manual escreve que o chefe *"perde a ação três vezes por rodada"*** — ele age uma vez enquanto o grupo de quatro age quatro, e é dessa perda que sai a exigência de `3` a `4×` a vida do grupo que a tabela de inimigo cumpre. *Contagem de ação nunca esteve ali.*

**O chefe age `3` vezes por rodada, e esse número é o piso desta régua.** Quatro das treze condições cobram ação do alvo — o `Lento` cobra meia, o `Calado` e o `Enfeitiçado` uma, o `Atordoado` uma e meia —, e cada ação a menos encarece as quatro na mesma proporção:

*Cada célula é quanto a condição ocupa do teto do tier que a tabela das treze, logo abaixo, publica para ela.*

| ações do chefe | `Lento`, `Leve` | `Calado`, `Média` | `Enfeitiçado`, `Média` | `Atordoado`, `Pesada` |
|---|---|---|---|---|
| `1` | `6,23×` | `6,95×` | `6,95×` | `6,64×` |
| `2` | `3,19×` | `3,48×` | `3,48×` | `3,32×` |
| **`3`** | **`2,18×`** | **`2,32×`** | **`2,32×`** | **`2,21×`** |

**Com `2` as quatro passam do filtro de dominância de `3,00×`.** *Com `3` as quatro cabem, e o `Lento` cabe raspando.* **E ele é piso, não folga escolhida:** se alguém escrever `4`, as quatro continuam cabendo e o número deixa de sair da conta — *a checagem `12` cobra as duas direções, que `3` baste e que `2` não baste.*

> *Esta tabela media `%` do teto até a v0.200 e passou a medir dominância na v0.201, junto com a régua. O piso de `3` não se moveu — o que mudou foi a coluna que o prova.*

**E duas convenções, as duas lidas de entrega publicada:**

> **Benefício que só o corpo a corpo colhe conta UM aliado.** *É a leitura do `Abalo`, a Manha da Massa.*
> **Benefício que qualquer atacante colhe conta TRÊS.** *É a leitura do `Estampido`, a Manha da Arma de Fogo, que supõe mesa de quatro.*

> **⚠ A régua mede a rodada em que a condição está ativa, e a condição dura UMA.** *A Melhoria `Condição` do manual escreve isso na própria célula — "Dura uma rodada" —, e nenhuma das Melhorias que mexem em tempo estende ela.* **Então um `Impedido` vale `132,15` na rodada dele e `44,05` espalhado numa luta de `3` rodadas**, que é `20%` do que um chefe faz.
>
> *Isto entrou na v0.199, e entrou porque a falta dele produziu um erro:* **a régua foi lida como se a condição durasse a luta**, e daí saiu um diagnóstico de que o chefe precisava de proteção contra condição no molde da `Resistência Lendária` do 5e. **Ele não precisa** — *o sistema já resolve pelo relógio, e a duração morava só na célula do manual.*

**As treze, aplicadas num chefe, no nível 30:**

| condição | nega por rodada | ações negadas | pontos | contra o dano deles | nível |
|---|---|---|---|---|---|
| **`Impedido`** | `132,15` | `1,5` + deslocamento + aliados | `11` | `2,67×` | `Pesada` |
| **`Cego`** | `126,75` | `1,5` + aliados | `11` | `2,56×` | `Pesada` |
| **`Amedrontado`** | `114,90` | `1,5` + deslocamento | `11` | `2,32×` | `Pesada` |
| **`Envenenado`** | `109,50` | `1,5` | `11` | `2,21×` | `Pesada` |
| **`Atordoado`** | `109,50` | `1,5` | `11` | `2,21×` | `Pesada` |
| **`Calado`** | `73,00` | `1` | `7` | `2,32×` | `Média` |
| **`Enfeitiçado`** | `73,00` | `1` | `7` | `2,32×` | `Média` |
| **`Lento`** | `39,20` | `0,5` + deslocamento | `4` | `2,18×` | `Leve` |
| **`Derrubado`** | `8,45` | `0` | `4` | `0,47×` | `Leve` |
| **`Agarrado`** | `5,40` | `0` | `4` | `0,30×` | `Leve` |
| **`Incapacitado`** | `4,95` | `0` | `4` | `0,28×` | `Leve` |
| **`Desarmado`** | `3,45` | `0` | `4` | `0,19×` | `Leve` |
| **`Surdo`** | `0,00` | `0` | `4` | `0,00×` | `Leve` |

**Seis `Leve`, duas `Média`, cinco `Pesada` — os mesmos treze níveis de antes da v0.201, e nenhum preço se moveu.**

> **A coluna das ações é quem decide o nível, e ela não olha o alvo.** *Desvantagem nega metade da rodada, e metade de três ações é uma e meia — é por isso que o `Envenenado` cai no mesmo degrau do `Atordoado` sem tirar ação nenhuma.*
>
> **A coluna da direita é o teste, e a pior das treze fica em `2,67×` contra o filtro de `3,00×`.**
>
> ***⚠⚠ E ela destampou o que a régua velha escondia:*** *com o chefe de `72` da v0.200, as treze ficavam entre `0,00×` e `1,18×` —* **comprar condição era o pior negócio da mesa, e o teto não tinha como mostrar isso porque ele media contra um chefe mais fraco que um personagem.** *Hoje as oito que negam ação valem mais que o dano que substituem, e nenhuma domina.*
>
> **⚠ Nenhuma das oito que se moveram é usada por entrega de Trilha nenhuma.** *A única condição do catálogo de entregas é o `Derrubado`, que é feito de vantagem e de metros — os dois absolutos —, e por isso ele não se move com o chefe.* **O `Abalo` e o `Encontrão` continuam com o preço que tinham.**

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

**O `Incapacitado` é a terceira mais barata das treze, e o manual cobrava `Pesada` por ela.** *Metade dela — "você não pode `Bloquear`" — vale praticamente zero, e a peça 23 §5.1 é quem mede.* **A outra metade, o crítico no corpo a corpo, vale `4,95`.** *O que faltava era o tamanho.*

> **⚠⚠ E o `11,00` que ficou publicado da v0.103 à v0.150 não era nenhuma das duas leituras da frase — era metade de uma delas.** *Ele é `2 golpes × 5,5` de dado extra: conta o dado dobrado em **100%** dos golpes, o que só faz sentido se o crítico sempre acertasse, e depois cobra **zero** pelo acerto garantido, que sozinho vale `11,50`.* **Duas metades da mesma leitura, e a peça cobrava uma.** *E a frase "segunda mais barata das treze" era falsa desde a v0.103: com `11,00` ela era a quinta.*

***Decisão do Mizuki na v0.151: a leitura é "todo ataque corpo a corpo QUE ACERTAR você é crítico", que é como a mesa já joga*** — e é a forma da fonte, o `Paralisado` do PHB 2024: *"Qualquer jogada de ataque **que o atinge** é um Acerto Crítico se o atacante estiver a até 1,5 metro"*. **Lá ela vem junto de vantagem para quem ataca; aqui não vem, e é de propósito.**

**A conta, com um aliado corpo a corpo e os dois golpes que o nível 7 dá:**

> **`ganho = 2 golpes × (acerto − chance de 20 natural) × dados dobrados`**
> **`2 × (0,50 − 0,05) × 5,5 = 4,95` de dano por rodada.**

*O crítico não cria acerto: ele troca um golpe normal por um crítico nas vezes em que o golpe já ia acertar, e o `20` natural já entregava isso em `5%` delas.*

> **⚠⚠ E o que decide a banda não é o número — é o ESCOPO do crítico, e ele foi medido antes de a peça 1 fechar a regra.**
>
> | o que o crítico dobra | ganho | do teto da `Leve` |
> |---|---|---|
> | só o dado impresso da arma — soco `d10` | **`4,95`** | **`32%`** |
> | só o dado impresso da arma — arma `d12` | `5,85` | `38%` |
> | \+ o dano na arma do refino `10` (`4d6`) | `17,55` | **`114%`** |
> | o mesmo, com arma `d12` | `18,45` | **`120%`** |
> | \+ um `Classe 0` junto do ataque (a `Fornalha`) | `29,25` | `190%` — vira `Média` |
>
> **Sem a trava de escopo, uma condição `Leve` passa a entregar por ponto mais que uma `Média` e mais que uma `Pesada`.** *Com o feitiço de Toque `Classe 7` dentro do escopo, o `Incapacitado` vai a `2,70×` contra os `2,32×` do `Calado` e os `2,21×` do `Envenenado` — o degrau mais barato da escada entregando mais que os dois de cima.*
>
> *⚠ Esta tabela foi medida contra o TETO até a v0.200, quando o teto ainda era o teste, e as colunas de `%` ficam como estão: elas dizem quanto a condição devolve do que aqueles pontos custaram. **O que mudou é qual linha derruba a trava** — antes eram as duas do meio, hoje é só a última.* *A peça 1 §5.2 passou a dizer "dobra só os dados do que rolou o acerto", e a lista de exclusão virou exemplo em vez de ser a regra.* ***Palavras do Mizuki:*** *"dobrar dado de dano é mt coisa".*
>
> **⚠⚠ As duas linhas do meio eram `14,40` e `15,30` — `93%` e `99%` — até a v0.158, com `3d6`.** *O refino `10` passou a dar `4d6` naquela versão (peça 11 §6.9), e com isso **a trava de escopo deixou de ser folga**: antes o `Incapacitado` só estourava a `Leve` com arma de duas mãos, agora o soco basta.* **A última linha não se move**, porque a trava `Só arma` do dano na arma já proíbe ele de somar por cima de um `Classe 0` que viajou junto do ataque — os dois nunca aparecem na mesma rolagem.
>
> *A conclusão não depende da dívida de acerto do §2.5:* **a `55%` o número vira `5,50` e a banda não se move.**

> **⚠⚠ E o segundo eixo do escopo é QUAL ROLAGEM entra, não só quais dados.** ***Achado do Mizuki:*** *"critar tudo como feitiço e ataques a distância eu não apoio, deixa apenas pros ataques corpo a corpo mesmo."* **Este sistema tem três rolagens de ataque — corpo a corpo, à distância e de conjuração —, e o **feitiço de Toque acontece a `1,5 m` e é de conjuração**.** *"Corpo a corpo" sem essa linha é a palavra que dois mestres leem diferente.*
>
> | o que a condição alcança | ganho | banda |
> |---|---|---|
> | **só ataque corpo a corpo — o publicado** | **`4,95`** | **`Leve`** |
> | \+ ataque à distância, com `2d10` no teto | `9,90` | `Leve` |
> | \+ feitiço de Toque `Classe 3` | `20,25` | `Média` |
> | \+ feitiço de Toque `Classe 5` | `34,43` | `Pesada` |
> | \+ feitiço de Toque `Classe 7` | **`48,60`** | **acima do teto da `Pesada`** |
>
> **Um feitiço de Toque no topo sozinho vale mais que qualquer `Pesada`, e a `Classe 3` já joga a condição para `Média`.** *O `Classe 7` é a Rotina inteira em dados — `24d8` —, e dobrar isso uma vez por turno passa dos `46,29` do teto.* **A linha ficou escrita nas quatro cópias: só o ataque corpo a corpo entra.**

**O `Impedido` engole o `Cego`.** *Ele tem as duas linhas do `Cego` — desvantagem nos ataques do alvo e vantagem para quem o ataca — mais deslocamento zero.* **Até a v0.103 os dois custavam `Média` no manual, e o `Impedido` era a melhor compra da tabela de Controle inteira.** *Hoje os dois custam `Pesada`, e a diferença entre eles caiu para `1,10×` — dominância que o filtro aceita.*

**Duas entregam mais que as outras três `Pesada`, e o manual já diz o que fazer com isso.** *O `Cego` fica em `2,56×` e o `Impedido` em `2,67×`, contra `2,21×` das três que negam uma ação e meia e nada mais.* **A regra que o manual dá para a Restrição escrita à mão, virada do avesso, resolve:** *"se a dor que você escreveu parece valer mais que uma Média, ela provavelmente são duas Restrições disfarçadas de uma — separe."* **Uma condição que passa do teto da `Pesada` é mais de uma condição escrita como uma**, e o `Impedido` diz isso no próprio texto: ele é o `Cego` inteiro mais deslocamento zero, que é o que o parágrafo acima já mede em `1,10×`.

> **Eram três até a v0.139, e a terceira era o `Petrificado`, que na régua daquela versão ficava em `217%` do teto da `Pesada`.** *Ele era o exemplar mais claro deste argumento — `Incapacitado`, mais deslocamento zero, mais não perceber nada, mais vantagem para quem ataca, tudo vendido como uma condição só.* **Com ele fora, quem carrega o argumento é o `Impedido`, que prova a mesma coisa com metade da força.**

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
| **`Incapacitado`** | `Leve` | **você não pode `Bloquear`, e todo ataque corpo a corpo que acertar você é crítico** — *só ele: ataque de conjuração e ataque à distância não, e o feitiço de Toque é de conjuração mesmo encostado em você* |
| **`Derrubado`** | `Leve` | você está no chão. Só se move rastejando, tem desvantagem nos seus ataques, e quem ataca você **a até 1,5 m tem vantagem** — quem ataca de longe tem desvantagem |
| **`Agarrado`** | `Leve` | seu deslocamento é `0`. Acaba se quem agarrou ficar `Incapacitado`, ou se alguma coisa tirar você do alcance dele |
| **`Desarmado`** | `Leve` | a sua arma está no chão ou na mão de outro. Você bate desarmado até pegar de volta |

> **O preço do `Desarmado` descreve a ficha SEM arma reserva, e isso é decisão declarada na v0.188.** *A peça 3 §3.2 dá o primeiro saque do turno de graça, então quem carrega reserva saca outra sem pagar nada e a condição vale `0` para ele.* **As duas metades do `3,45` zeram junto:** *`1,65` são as rodadas socando e `1,80` é a caminhada de `3 m` até a arma — quem tem reserva não faz nenhuma das duas.*
>
> ***Decisão do Mizuki: o número fica, e a régua diz o que ela mede.*** **Ela mede o que a condição TIRA, e não o que o alvo faz a respeito** — nenhuma das treze modela preparação, e criar isso para uma só produz um catálogo com dois modelos dentro. *Carregar reserva é a resposta, e ela é barata de propósito.*
>
> > **⚠ E a dívida dizia que consertar era caro, e para esta condição não é.** *A frase que ela carregava — "repreçar uma condição mexe na régua das treze e no catálogo de Melhorias do manual" — é verdade em geral e falsa aqui.* **A Melhoria `Condição` cobra pelo NÍVEL, e o nível sai da banda:** *no nível 30 a `Leve` vai até `15,43` de dano por rodada, e o `Desarmado` está em `22%` disso.* **Qualquer valor entre `0` e `15,43` continua `Leve`**, então nenhum feitiço do manual e nenhum dos trinta e cinco prontos se moveria. *O `Surdo` lê `0,00` nesta mesma régua e continua comprável e `Leve`.*
> >
> > **O que é de verdade diferente nela, e fica escrito: ela é a única das treze que uma compra feita ANTES da campanha desliga inteira.** *Sair de um `Agarrado` custa ação dentro da luta, e a régua já cobra isso porque a condição tomou a ação; carregar reserva custa dinheiro, uma vez, e nada na luta.* **Se um dia isso pesar na mesa, o molde já existe:** *o `Surdo` lia `0,00` e ganhou `−2` na iniciativa — piso, e não repreço.*
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

> **Só as de nível `Pesada` dão Teste de Resistência no fim de cada turno do alvo, e só cabe uma delas por feitiço.** *Até a v0.103 essas duas linhas andavam com a `Condição Maior`, que era um pacote de cinco nomes.* **Elas passaram a andar com o degrau de cima porque é ele que precisa de amortecedor** — e as cinco de antes não eram as cinco mais duras: o `Incapacitado` estava lá dentro, e ele é a terceira mais barata das treze.

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
> *O que sobra são os dois extremos de cerca de `1%` — o `Aparar` e a `Brecha` —, e eles quase se cancelam.* **Medido por enumeração completa das `2.000` combinações, a metade vale `+0,02` de dano por rodada**, e o `Incapacitado` iria para `4,97`. *Abaixo da precisão que esta régua carrega: o golpe simples que entra nela varia `3,0` entre o nível 2 e o 30.* **O número publicado no §2.2 fica em `4,95`.**
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
> **O que ela quebrou é a checagem 3, que é o invariante desta peça:** *o valor medido de cada condição tem de cair na **banda** que o nível dela implica, e as bandas saem da tabela de preço do manual — `1/7`, `2/7` e `3/7` da Rotina.* **No nível 30 o teto da `Leve` é `15,43` de dano por rodada. O `Lento` vale `14,70` e o `Incapacitado` valia `11,00`: os dois cabiam em `Leve` pela conta.** *Pôr os dois em `Média` faz o jogador pagar preço de `Média` por coisa que vale `Leve`.*
>
> **⚠ E a v0.151 refez o `Incapacitado` para `4,95`, o que só fortalece isto:** *ele passou a caber em `Leve` com `68%` de folga, contra os `29%` que a tentativa da v0.139 disputava.*
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

### 5.1 Quem cita esta escala, e o que ele não pode fazer

**O manual usa esta tabela e não a copia.** *Duas entradas dele compram furar cobertura: a Melhoria `Sem Cobertura` (`Leve`) e a Passiva `Afinidade` (Classe 3), e as duas nomeiam a `Parcial`.* **A checagem 7 do `conferir-manual.py` falha nas duas direções** — se o manual nomear um grau que não está aqui, e se ele repetir os bônus, que são desta seção.

> **⚠ Até a v0.161 as duas citavam graus que este sistema não tem.** *A Melhoria dizia `cobertura leve e meia cobertura` e a Passiva dizia `cobertura leve`.* **Rastreados nos PDFs de referência:** *`cobertura leve` é do **GURPS 4e**, onde nem grau é — lá é um `−2` de tiro —, e `meia cobertura` é o **half cover** do D&D 2014.* **Os dois apontam para obstrução parcial, que aqui é a `Parcial`, e nenhum dos dois é o degrau de `+5`.**

### 5.2 Comprimir a escada foi medido na v0.162, e a conta reprova

***Levantado pelo Mizuki:*** *"como no nosso sistema a rolagem é menor em 1, recomendo as coberturas darem `+1` e `+4` no lugar de `+2` e `+5`, ou `+2` e `+4`."*

**A premissa está certa, e foi conferida.** *No topo, o acerto daqui é `atributo 6 + maestria 4 = +10`; o do d20 é `proficiência +6 + atributo +5 = +11`.* **Um a menos — e por isso o acerto base é `55%` contra `60%`, e a cobertura morde um pouco mais forte aqui.**

**Só que descontar um ponto inteiro passa do alvo.** *Cada ponto de Defesa vale `5` pontos percentuais, e o vão a corrigir é menor que isso:*

| escala | mordida no degrau baixo | no degrau alto | distância somada do d20 |
|---|---|---|---|
| **o d20**, a referência | `−16,7%` | `−41,7%` | — |
| **daqui, hoje `+2 / +5`** | `−18,2%` | `−45,5%` | **`5,3` pp** |
| `+2 / +4` | `−18,2%` | `−36,4%` | `6,8` pp |
| `+1 / +4` | `−9,1%` | `−36,4%` | `12,9` pp |

> **A escala de hoje é a mais próxima das três**, e as duas propostas erram para o outro lado por mais do que ela erra para este. *Não existe conserto inteiro melhor que não mexer: o desvio a corrigir é de `1,5` a `3,8` pontos percentuais, e o menor ajuste possível vale `5`.*
>
> **E o motivo da v0.94 continua de pé, e ele nunca foi matemático:** *o número não sai de conta daqui — ele só precisa ser o mesmo em sete mesas, e uma tabela que todo mundo já conhece resolve isso de graça.* **Comprimir a escada compra pontos percentuais de precisão e vende o reconhecimento, que era o único produto dela.**

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

## 7. As treze checagens do `conferir-dano.py`

*Escritas antes do validador, que é o método que fez a peça 15 caber numa versão só contra as seis que a peça 14 gastou.*

| # | o que ela confere |
|---|---|
| **1** | **as âncoras existem nos donos.** Cada número que a régua usa aparece no documento que esta peça declara como dono dele. Âncora que sumiu do dono é régua sem chão |
| **2** | **a régua reconstrói as treze.** Cada valor da tabela do §2.2 é recalculado a partir das âncoras e comparado com o publicado. *E, desde a v0.104, ela também reconstrói a razão entre as duas réguas de rolagem — e cobra que ela seja exatamente o dobro da razão das bases* |
| **3** | **o nível de cada condição sai das AÇÕES que ela nega**, e não do alvo: meia ação é `Leve`, uma é `Média`, uma e meia é `Pesada`, com desvantagem contando como uma e meia. *E o preço de cada tier continua sendo lido da tabela de Classe do manual, `1/7`, `2/7` e `3/7` da Rotina — ele deixou de ser o teste na v0.201 e continua sendo o preço* |
| **4** | **as treze batem com o manual**, nas duas direções: nome e **nível**, tabela por tabela — e o manual vende **uma** Melhoria `Condição`, cobrando o nível. *Lê o `.docx`, então **pula** sem o `python-docx` — e diz que pulou* |
| **5** | **nenhuma condição fica sem nível**, e o nível é um dos três. Guarda de contagem: são treze, seis `Leve`, duas `Média` e cinco `Pesada` |
| **6** | **a escada de quem cura fecha.** O teto de energia por uso em cada faixa de maestria cobre exatamente os tiers que o §2.3 publica, e ela bate com a escada de exaustão da peça 10 |
| **7** | **os catorze tipos de dano**, os três grupos, os pesos `60/30/10` e a tabela de quantos tipos você resiste, recontada em vez de guardada |
| **8** | **a cobertura**: os três degraus, os dois números de cada um, e a `Total` sem número |
| **9** | **as duas entregas publicadas que aplicam condição** — o `Abalo` do `DESENHO-manhas.md` e o `Encontrão` do `DESENHO-trilhas.md` — batem com a régua, com o portão que o texto de cada uma escreve |
| **10** | **nenhum valor de regra escrito dentro do validador.** Todo número vem do documento dono, e a checagem falha se algum ficar guardado no código |
| **11** | **a penalidade de arma da seção 6**: as duas linhas estão escritas, o `3 m` bate com o `10` pés do d20, e a desvantagem reconstrói em `54,00` a partir das âncoras — e a soma das duas contra a entrega da arma inteira |
| **12** | **as ações do chefe são o piso da dominância.** O número é lido do §2.2, as quatro condições que cobram ação são recalculadas com ele e com um a menos, e a checagem cobra as duas metades: com o publicado as quatro cabem, com um a menos alguma sai. *Assim `4` acende do mesmo jeito que `2`* |
| **13** | **a coluna do capanga.** As treze são recalculadas contra o capanga — `73` por rodada em `1` ação, em vez de `219` em `3` —, e a checagem cobra que **nenhum nível se mova** e que a dominância continue passando dos dois lados. *Ela é a prova de que a régua não depende de contra quem foi escrita, e desde a v0.201 essa promessa deixou de ser retórica: o nível vem das ações negadas, que não olham o alvo* |

> **A checagem 9 é a que esta peça existe para ter.** *Ela é a única que sai da pasta, junto com a do `conferir-catalogo.py` — e é ela que pegaria o `Punho` de novo se alguém reescrever o texto da entrega sem mexer no preço, ou o contrário.*

### As quarenta e quatro perturbações, em cópia isolada

> **⚠ Este título dizia `vinte e sete` e a tabela tinha vinte e oito** — contagem escrita em frase, sem dono, que é a lição nº 9 na forma mais barata que ela tem. *As quatro últimas são da v0.151; a diferença de um é anterior a ela.*

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
| **2** | **o `Incapacitado` volta para o `11,00` da v0.150** | acende | acende |
| **1** | **o escopo do crítico some da peça 1** | acende | acende |
| **1** | **o dado do soco muda na peça 14 e o valor publicado não** | acende | acende |
| **2** | **contra-teste: os DOIS mudam juntos — `d12` e `5,85`** | fica verde | fica verde |
| **12** | **a peça publica `2` ações no lugar de `3`** | acende | acende |
| **12** | **a peça publica `4` — deixa de ser piso** | acende | acende |
| **12** | **uma célula da tabela de ações vira `96%`** | acende | acende |
| **1** | **a frase das ações some da peça** | acende | acende |
| **13** | **a peça volta a dizer `seis`** | acende | acende |
| **13** | **a peça para de declarar que o estouro some contra o capanga** | acende | acende |
| **13** | **o capanga vira `50` no `DESENHO-trilhas.md`** | acende | acende |
| **1.1** | **linha nova na tabela de âncoras da peça** | acende | acende |
| **1.1** | **a linha `dano evitado` sai da tabela** | acende | acende |
| **1.1** | **âncora nova no validador que nenhuma linha reivindica** | acende | acende |
| **1.1** | **contra-teste: linha nova coerente nos três lugares** | fica verde | fica verde |
| **12** | **contra-teste: o `Atordoado` passa a cobrar `2` ações e o piso vai a `4`** | fica verde | fica verde |

> **As doze últimas são da v0.198, e a que prova a checagem `12` é o contra-teste.** *Fazer o `Atordoado` cobrar `2` ações em vez de uma e meia move o piso para `4` sozinho* — **a checagem sai verde com `4` publicado, e é assim que se sabe que ela mede a relação e não a constante `3`.**

> **⚠⚠ E o par de baixo achou um defeito na âncora que a v0.151 tinha acabado de escrever.** *O padrão dela era `` teto é `d10` `` — com o valor dentro.* **Trocar o dado do soco para `d12` na peça 14 fazia a âncora "sumir" e acender a checagem 1 pelo motivo errado**, em vez de a régua reler `6,5` e a checagem 2 comparar. *Uma âncora cujo padrão carrega o valor é a lição nº 8 em miniatura: ela deixa de achar exatamente quando o dono muda, que é quando ela precisa achar.* **Hoje o padrão é `` teto é `d\d+` `` e o valor sai do grupo.**

> **⚠⚠ E o arnês achou TRÊS defeitos no validador antes de ele valer, e um deles é a lição nº 8.**
>
> **A checagem 4 comparava o manual contra a lista escrita DENTRO do validador**, e não contra a peça — então renomear uma condição na peça saía **verde**. *Uma checagem que se mede contra a própria constante, pela quarta vez em setenta versões.* **Hoje ela lê os nomes das tabelas do §3.1 e do §3.2.**
>
> **A checagem 6 procurava `três degraus` OU `degrau 3` na peça 10**, e meia porta é porta aberta: apagar uma das duas frases saía verde. *Hoje ela exige as duas.*
>
> **E duas perturbações estavam mal miradas**, trocando uma ocorrência de uma âncora que aparece duas vezes no mesmo arquivo — o que produz um *"não acendeu"* que parece prova. **O arnês ganhou um modo que troca todas as ocorrências**, e é o mesmo defeito que a v0.101 registrou com um `sed` que parou de bater.

---

## 8. Em aberto

- ~~**A `Cicatriz` continua sem mecânica.**~~ ***FECHADA na v0.171, e não aqui: na peça 1 §5.5.*** *A peça 24 §6.3 já tinha medido o recorte na v0.145 e devolvido ela para lá — a `Cicatriz` é consequência de cair a `0` de vida, e não de condição nem de dano de alma.* **Ela não entra na régua da seção 2 desta peça, e por isso não é entrada de catálogo:** *vantagem em `Intimidação` e desvantagem em `Persuasão`, as duas `Essência`, sem preço em fatia — a troca acontece dentro de um poço só.* **E a segunda pergunta fechou junto: a `Energia Reversa` não limpa Sequela.**
- **O `Surdo` lê `0,00` nesta régua mesmo depois do `−2` na iniciativa**, e o motivo é a régua e não a condição — ela mede dano por rodada, e a peça 15 §3.1 já publicou que ordem de iniciativa não move dano. *Enquanto a régua for essa, o degrau que contiver o `Surdo` vai ter dominância infinita no papel.* **O que falta é uma régua para o eixo de iniciativa**, e o projeto já tem duas decisões grandes tomadas nele — a saída A das Invocações e a recusa da iniciativa fixa da peça 3 — as duas sem número em fatia.
- ~~**As condições que impedem `Bloquear`.**~~ **FECHADA na v0.143, e a resposta já estava escrita aqui.** *O rascunho listava surpreendido, caído e agarrado como candidatos e apontava para cá; a peça 23 §5 mediu e concluiu que **só o `Incapacitado`** desliga.* **O §3.4 desta peça já dizia por quê:** *ele é a condição cujo eixo **é** a defesa, e `Atordoado` e `Incapacitado` foram separados em v0.95 justamente para não se aninharem.* **Pôr a linha no `Derrubado` ou no `Agarrado` não seria escrever regra — seria repreçar duas condições que já têm número na régua da seção 2.** *A checagem 5 do `conferir-bloquear.py` lê esta seção e falha se uma segunda condição citar `Bloquear`.*
- ~~**Três vagas de `Desliga` da peça 13 esperam esta peça.**~~ ***FECHADAS na v0.104***, e a régua da seção 2 é que as destravou: *o nível de uma condição é número, e o `Desliga` passou a poder apagar condição uma vez com o relógio saindo do nível dela.* **As três são o `Revezamento` (`Impedido`), o `Usado` (`Derrubado`) e o `Talhe` (`Agarrado`)**, e as três estão escritas nas tabelas da peça 13.

  > **⚠ Esta linha ficou oitenta e seis versões mandando reler três vagas que não existem mais.** *Achada na v0.191, varrendo as seções "Em aberto" das vinte e cinco peças.* **A peça 13 fechou as cinco destravadas na v0.104 e registrou isso lá; esta peça nunca soube.** *A sub-checagem `11.2` passou a ler a contagem de vagas do lado de lá em vez de confiar nesta frase.*
- **⚠ As duas réguas de rolagem divergem por `9,4` vezes, e não por `4,7` — e o `4,7` publicado media outra coisa.** *A v0.103 escreveu que `+1` no seu acerto vale `10,80` (que são `10%` da Rotina de `108`), que `1` ponto percentual na rolagem de um aliado vale `0,230` (que é `1%` da ação de atacar de `23,00`), e que **"a diferença é de `4,7` vezes"**.* **O `4,7` é `108 ÷ 23,00`: a razão entre as duas BASES.** *Isso é verdade e responde outra pergunta — quanto o seu escopo é maior que o do aliado.* **Lidas por ponto percentual, que é a única forma de compará-las, elas dão `2,16` contra `0,230`, e a razão é `9,39`.**

  ***⚠⚠ E o diagnóstico que estava escrito aqui era errado, refeito na v0.192.*** *Ele dizia que a sua régua é relativa e a do aliado é absoluta, e que consertar isso repreçaria o `Guiar`, o `Estampido` e o `Ajudar`.* **A conta desmente: existe uma régua só, e ela é relativa nos dois lados.**

  **O que estava errado era a BASE do aliado, e não a conversão dele.** *A entrega mexe em UM golpe simples — `11,50` —, e a conta velha usava a **ação inteira**, que são dois golpes.* **Os dois erros se cancelavam exato**, porque `23,00` é `2 × 11,50` e o fator relativo é `1 ÷ 0,50`, que também é `2`. *Foi por isso que o `0,230` sempre foi o número certo com a explicação errada pendurada nele.*

  **Reconstruídas pela relativa em um golpe, as três batem na casa decimal:**

  | entrada | pontos percentuais | conta | publicado |
  |---|---|---|---|
  | `Ajudar` | `25` | `0,50 × 11,50` | **`5,75`** |
  | `Guiar` | `15` | `0,30 × 11,50` | **`3,45`** |
  | `Estampido` | `5`, e conta três aliados | `0,10 × 11,50 × 3` | **`3,45`** |
  | `Vex`, na sua rodada | `25` | `0,50 × 108` | **`54,00`** |

  **E o `9,4` não é defeito nenhum: ele é ESCOPO puro** — a sua rodada de `108` contra um golpe do aliado de `11,50`. *O `4,7` que três documentos publicavam é o mesmo escopo com a base errada do outro lado, `108 ÷ 23,00`.*

  > **O que parecia contra-teste era a mesma troca de base, por outra porta.** *A frase que morava aqui dizia: lido pela sua régua, o `Ajudar` valeria `54,00` em vez de `5,75`, e `54,00 ÷ 5,75` dá `9,4`.* **Aquilo é verdade e não prova nada** — o `54,00` é vantagem medida **na sua rodada inteira**, e o `Ajudar` é a mesma vantagem medida **num golpe do aliado**. *A razão entre os dois é o escopo, que é justamente o `9,4` de que se está falando.*

  ***FECHADO na v0.192, e nenhum número se moveu.*** **O que estava errado era a explicação, e ela ficou setenta e oito versões pendurada num número certo.** *A checagem 2 do `conferir-dano.py` passou a exigir que a razão entre as duas réguas seja **só** o escopo — se um dos dois lados deixar de ser relativo, ela acende.*
- **O valor de uma condição depende de em quem ela cai, e o NÍVEL dela não.** *Contra um capanga de `73` de dano por rodada em `1` ação, em vez de um chefe de `219` em `3`, **nenhuma das treze muda de nível** — o nível sai das ações negadas, e elas não olham o alvo.* **O que muda é a entrega:** *as cinco que negam ação entregam o mesmo dos dois lados, porque a rodada inteira do capanga é o golpe de uma ação do chefe; as quatro que dão desvantagem caem para `0,74×` a `1,19×`.*

  > **⚠ E a ORDEM inverte contra um alvo de uma ação só.** *No chefe o `Envenenado` (`Pesada`) entrega `2,21×` e o `Calado` (`Média`) entrega `2,32×`; no capanga o `Envenenado` cai para `0,74×` e o `Calado` fica.* **Calar quem só tem uma ação é calar a rodada dela inteira**, e é por isso que a régua não promete que o nível ordene a entrega — ela promete que o nível descreva a condição. *A checagem `13` cobra as duas metades.*

  > **⚠ Esta linha dizia `seis`, e dizia que o validador conferia as duas colunas.** *Nenhuma das duas era verdade: a conta dá `cinco` — `Amedrontado`, `Envenenado` e `Atordoado` descem para `Média`, `Calado` e `Enfeitiçado` descem para `Leve` — e o `38` estava escrito dentro do `conferir-dano.py` sem ser usado em lugar nenhum.* **Achado na v0.198, levantando o terreno do `Bestiário`.**
- **O `Impedido` é a maior da lista desde a v0.139, quando o `Petrificado` saiu.** *Ele é o `Cego` inteiro mais deslocamento `0`, e a diferença entre os dois é `1,10×` — dominância que o filtro aceita.*

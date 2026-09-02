# 26 · Bestiário — a máquina de montar inimigo

*Fechada na v0.198. Ela estava no fim da fila desde a v0.36 com uma linha só — "sai da matemática de inimigo que o manual já tem" — e era o único item da fila da mecânica desde a v0.168.*

## 1. O que ela é, e o que ela não é

**Esta peça junta num lugar só os números que montar um inimigo pede.** Até aqui eles moravam em quatro donos — o manual, a peça 1, a peça 19 e o `ESTADO-ATUAL` —, e três dos que a mesa rola toda rodada não tinham dono nenhum: a Defesa do inimigo, o acerto dele e a CD dele.

**Ela é máquina, e não catálogo.** *Decisão do Mizuki na v0.161: o Bestiário sai como máquina mais maldições prontas, e não como recolhimento puro.* **As prontas ficam para a versão seguinte**, e o §8 diz o que falta nelas.

> **A ficha de inimigo é a ficha de personagem sem o Caminho.** *Decisão do Mizuki:* **o inimigo tem refino, tem Passiva, tem aptidão e às vezes tem técnica** — muita coisa que ele enfrenta na obra é feiticeiro, e feiticeiro se monta com as mesmas peças. *O que ele não tem é Caminho, Trilha e poço de PE, e o §6 diz por quê.*

**E a rota que só o inimigo tem é ser maldição.** *O jogador não escolhe isso, em nenhuma das nove rotas de Origem da peça 9.*

## 2. O grau é ficção, e a obra é quem manda nisso

***Decisão do Mizuki: o grau fica na ficha da maldição como rótulo, e não entra em conta nenhuma.*** **A métrica é o nível e a categoria do §4.**

O motivo é a peça 12 §2: *"Grau é reconhecimento; nível é poder"*. Se o grau da maldição parear com o grau do feiticeiro, e o grau do feiticeiro não diz nível, então dois mestres montam o mesmo encontro com fichas de níveis diferentes — que é o filtro que este projeto usa para tudo.

> **⚠ A intuição de parear grau com grau é da obra, e ela está certa lá.** *A escada existe para classificar quatro coisas — feiticeiro, maldição, objeto e ferramenta — e ela nasceu como regra de despacho: manda-se um feiticeiro do grau da maldição.* **O que não atravessa é a metade numérica**, porque aqui o grau é patente e a patente sobe por feito.
>
> **E a obra deixa uma fronteira que a ficha já carrega de graça.** *O que separa uma maldição de grau 2 de uma de semi-grau 1, na classificação da obra, é **saber usar técnica**.* **Isso não é número: é uma linha do §6 desta peça, e ela está na ficha quer o grau exista ou não.** *Então o rótulo tem onde se apoiar sem virar conta.*

## 3. A ficha, e cada linha tem dono

**Dezessete linhas. Nenhum número novo nasce aqui** — o que esta peça faz é dizer de onde cada um sai.

| linha | valor | dono |
|---|---|---|
| nível | o nível do grupo | o mestre declara antes da mesa |
| categoria | `Ronda` · `Dupla` · `Alcateia` · `Calamidade` | o §4 |
| vida | a linha do manual vezes o fator da categoria | manual, a tabela `Inimigos` |
| **Integridade** | igual à vida máxima | manual, a seção `Inimigos` |
| dano por rodada | a linha do manual vezes o fator da categoria | manual, a tabela `Inimigos` |
| ações por rodada | personagens da categoria menos um, piso `1` | o §4.2 |
| **Defesa** | `10 + Destreza + proteção` | peça 1 §5 |
| **acerto** | `atributo + maestria` | peça 1 §5 |
| **CD** | `8 + atributo + maestria` | peça 1 §5 |
| Reação | uma por rodada, volta no começo do turno dele | manual, a seção `Inimigos` |
| refino | a curva do `meio a meio` | peça 11 §3 |
| Testes de Resistência | dois treinados de quatro | peça 7 §6 |
| deslocamento | `9 m` | peça 3 §3 |
| **atributos** | os cinco, no orçamento da peça 2 | peça 2 §3 |
| **características** | Passivas, aptidões e técnica, pelo §6 | peça 11, o mesmo catálogo do jogador |
| **pacto** | opcional, e o teto do permanente é da Essência dele | peça 22 §3 |
| **resistência, vulnerabilidade e imunidade** | custam degrau de categoria, pelo §6.3 | peça 19 §4 |

**As três em negrito não tinham dono em documento nenhum até esta peça**, e as três derivam sem escolha — elas não acrescentam número, elas dão nome ao que a peça 1 §6 e a peça 19 §2.5 já mediam do outro lado da mesa.

### 3.1 As três derivadas, nível a nível

**O inimigo carrega a mesma curva de atributo de quem investe** — `3` no nível 2 subindo a `6` no 26 —, e é isso que põe as três no lugar em que as outras peças já as mediam.

| nível do grupo | 5 | 10 | 15 | 20 | 25 | 30 |
|---|---|---|---|---|---|---|
| Defesa | `14` | `16` | `17` | `18` | `19` | `20` |
| acerto | `+4` | `+6` | `+6` | `+8` | `+8` | `+10` |
| CD | `12` | `14` | `14` | `16` | `16` | `18` |
| refino | `1` | `4` | `6` | `7` | `9` | `10` |

**Contra um personagem que investiu em defesa ele acerta `50%` a `55%`, e o Teste de Resistência treinado dele falha `35%`.** *São os mesmos números que a peça 1 §6 publica do lado do jogador, e é isso que prova a derivação: se ela estivesse errada, os dois lados da mesma rolagem discordariam.*

> **A proteção da Defesa anda junto com o refino, pela peça 11 §6** — `1/3 do refino + 1`. *Isso não é enfeite: sem ela a Defesa do inimigo congela e o acerto do personagem deriva `+15` pontos percentuais na campanha, que é o erro que a v0.117 consertou do lado do jogador.*

### 3.2 Os cinco atributos, no orçamento que a peça 2 já dá

**O inimigo monta os cinco no mesmo orçamento de uma ficha** — nove pontos na criação, teto `3` ali, `+1` por marco e teto `6`. *O precedente é da peça 15 §3.3: a invocação faz exatamente isso desde a v0.180, pelo mesmo motivo, que é ter ficha própria sem inventar economia nova.*

**É daqui que as três derivadas do §3.1 saem.** *A Defesa lê a Destreza, o acerto e a CD leem o atributo que aquele inimigo usa para atacar, e o teto de pacto do §3 lê a Essência.* **Sem os cinco escritos, as três derivadas ficam penduradas numa curva sem ficha por baixo.**

> **⚠ E não existe "atributo do Caminho" aqui.** *A ficha do jogador tem cinco atributos e um Caminho que decide vida e PE; o inimigo tem cinco atributos e a categoria, que decide vida e dano.* **Os nove pontos compram cor, e não tamanho** — um chefe de Força `6` e um de Essência `6` têm a mesma vida e o mesmo dano por rodada, e jogam diferente.

## 4. A categoria — quantos personagens ele exige

***Ideia do Mizuki, e o eixo é o dele:*** *quantos feiticeiros são precisos para enfrentar aquilo.* **A tabela de inimigo do manual já responde isso para um número — ela é calibrada para quatro —, e a categoria é aquela linha reescalada.**

| categoria | personagens | fator sobre a linha do manual | ações |
|---|---|---|---|
| **`Ronda`** | 1 | `× 0,25` | `1` |
| **`Dupla`** | 2 | `× 0,50` | `1` |
| **`Alcateia`** | 4 | `× 1,00` | `3` |
| **`Calamidade`** | 6 | `× 1,50` | `5` |

**A `Alcateia` é a linha do manual sem tocar em nada.** *As outras três saem dela, e nenhuma inventa número.*

### 4.1 A ficha pronta de cada categoria, nos três níveis que a tabela publica

| categoria | nv 10 | nv 20 | nv 30 |
|---|---|---|---|
| `Ronda` | `97` vida · `19` dano | `165` · `37` | `236` · `55` |
| `Dupla` | `195` · `37` | `330` · `73` | `472` · `109` |
| `Alcateia` | `390` · `75` | `660` · `147` | `945` · `219` |
| `Calamidade` | `585` · `112` | `990` · `220` | `1417` · `328` |

> **⚠ O arredondamento é meio para BAIXO, e ele é declarado porque não é cosmético.** *Os fatores são `0,25`, `0,50` e `1,50`, então **vinte e duas das cinquenta e seis células** desta escala caem exatamente em `,5`.* **Três lugares calculam isto — a peça, o validador e o gerador do bloco — e cada linguagem arredonda de um jeito:** *o `Math.round` do JavaScript sobe, o `round` do Python vai para o par.* **Sem a regra escrita, os três divergem em nove células, e o mestre lê o número em voz alta na mesa.**

### 4.2 As ações saem da frase do manual, e não de escolha

**O manual escreve que o chefe *"perde a ação três vezes por rodada"* contra um grupo de quatro** — ele age uma vez enquanto eles agem quatro. **Então a compensação é `personagens − 1`, com piso `1`:** na `Ronda` ele age uma vez porque o outro lado também age uma vez, e na `Alcateia` ele age três.

> **⚠ E a `Alcateia` não pode descer de `3`, e isso não é desta peça.** *A peça 19 §2.2 preça quatro das treze condições dividindo pelas ações do chefe.* **Com `2` as quatro passam do teto do próprio tier**, e o piso está medido lá, com a checagem `12` daquele validador em cima.

### 4.5 A sub-categoria — em quantos corpos o encontro se parte

***Ideia do Mizuki:*** *nem todo combate tem mais de um inimigo, e o mesmo encontro pode vir num corpo só ou repartido.* **A categoria diz o TAMANHO; a sub-categoria diz a FORMA.**

| sub-categoria | o chefe fica com | capangas | cobra do grupo |
|---|---|---|---|
| **`sozinho`** | `100%` | — | `68%` |
| **`com um apoio`** | `75%` | `1` | `58%` |
| **`com dois`** | `50%` | `2` | `56%` |
| **`bando`** | `25%` | `3` | `62%` |

**A fração não foi escolhida: ela sai do câmbio do §5.** *Cada capanga vale um quarto de um chefe de `Alcateia`, então tirar um quarto da vida e do dano dele e pôr um capanga no lugar preserva o tamanho do encontro.*

> **⚠ A coluna da direita depende de em que ordem o grupo abate, e a ordem está declarada: os capangas primeiro.** *É o que a mesa faz sozinha — cada capanga removido corta `73` de dano por `236` de vida gasta, e o chefe corta `73` por `315`.* **Abater na ordem contrária muda a coluna em até `15` pontos percentuais**, e por isso ela não vale sem a ordem escrita ao lado.
>
> **⚠ E partir o encontro sai um pouco mais barato, e não mais caro.** *Do corpo único para qualquer forma repartida a conta cai de `68%` para `56%` a `62%` da vida do grupo.* **É a mesma propriedade que a v0.199 leu ao contrário:** *o dano do inimigo despenca conforme os corpos caem, e um corpo único não despenca nunca.* **Fica declarado — a sub-categoria preserva o TAMANHO, e a forma repartida cobra um pouco menos.**
>
> **⚠ E a primeira tentativa não fechou, o que vale registrar.** *Partir o orçamento pela VIDA — o chefe cede metade da vida e entram capangas até somar aquilo — inflava o encontro.* **O capanga é `glass cannon`: um quarto da vida do chefe e um terço do dano dele**, então trocar vida por capanga acrescenta dano. *Só o câmbio preserva.*

### 4.6 O chefe derruba alguém, e a métrica que mostra isso não é óbvia

**Um chefe de `Alcateia` concentrando os três golpes derruba um personagem na rodada `1,11`.** *No nível 30 ele entrega `657` de dano na luta contra `243` do alvo, e a razão é a mesma em todo nível.* **Numa luta de três rodadas ele derruba `2,70` pessoas se concentrar** — não o grupo inteiro, e mais de uma.

> **⚠ A métrica errada é "quantas rodadas ele leva para derrubar o GRUPO", e até a v0.200 ela dava `14`** — contra uma luta de `3,7`. *Lida assim, a tabela de inimigo parecia fraca demais, e a v0.199 respondeu que ela não estava.* **Estava.** *O que a métrica errada escondia é que ele derrubava exatamente uma pessoa por luta, no último segundo, e a v0.201 mediu isso contra dois sistemas de fora.*
>
> **`2,70` é o número dos dois:** *o d20 de 2014 derruba `2,56` a `2,70` numa luta de três rodadas, e o chefe solo do Pathfinder 2e derruba perto de `2,8`.* **É a métrica que decidiu a tabela nova, e não a que decidiu a antiga.**

### 4.4 O dano se rola em dado, e não em número seco

**O que a tabela do manual publica é o dano por RODADA, e o que o mestre rola é o de uma AÇÃO.** *Divida um pelo outro e você tem o alvo do golpe.*

> **O golpe é `N d8 + fixo`, com metade do alvo em dado:** `N` é o alvo dividido por nove, arredondando, e o fixo é o que sobra. **Abaixo de `5` o golpe fica em número seco** — um `d8` balançaria mais que o próprio golpe, e no nível 2 ao 4 a linha inteira sai assim.

**O precedente é o `Guia do Mestre` de 2014**, que manda traduzir a margem de dano numa expressão de dado e diz que a divisão em ataques é livre. *Aqui a divisão não é livre: ela é o número de ações da categoria.*

| categoria, no nível 26 a 30 | por rodada | ações | o golpe |
|---|---|---|---|
| `Ronda` | `55` | `1` | `6d8 + 28` |
| `Dupla` | `109` | `1` | `12d8 + 55` |
| `Alcateia` | `219` | `3` | `8d8 + 37` |
| `Calamidade` | `328` | `5` | `7d8 + 34` |

> **⚠ O golpe da `Dupla` é o maior da tabela, e isso não é erro.** *Ela entrega metade do que a `Alcateia` entrega, numa ação em vez de três* — **menos ações quer dizer golpe maior, e é a mesma propriedade que faz o capanga bater acima do peso.**
>
> **⚠⚠ E ele custa doze dados numa rolagem só, o que é caro em tempo de mesa.** *A regra do meio em dado foi escrita quando a linha do nível 30 era `72` por rodada; com `219` ela produz punhados de `7d8` a `12d8`.* **Fica declarado como custo, e não consertado aqui:** *quem não quiser rolar doze dados usa o golpe seco — `109` na `Dupla`, `73` na `Alcateia` —, que é a mesma média sem a variação.* **É a saída que a própria regra já dá para a faixa mais baixa.**

### 4.3 ⚠ A categoria não é intercambiável consigo mesma

**Quatro `Ronda` não valem uma `Alcateia`: elas cobram `0,75 ×` a `0,77 ×` o que ela cobra**, e a razão é a mesma nas sete faixas.

*A causa é que eles morrem em fila e a saída deles despenca — quatro corpos de um quarto entregam tudo enquanto estão os quatro de pé, e depois entregam cada vez menos.* **Somar os fatores dá a linha inteira; jogar os quatro não dá o mesmo encontro.**

> **É por isso que o capanga do manual não é uma `Ronda`.** *A `Ronda` é um quarto do chefe nos dois eixos — um quarto da vida e um quarto do dano —, e o capanga é um quarto da vida com um TERÇO do dano.* **É essa diferença de um eixo só que faz o câmbio do §5 fechar em quatro e a `Ronda` parar em `0,76`.**

### 4.7 O que a CURA do grupo faz com o encontro — e ela não faz o que parece

***Pedido do Mizuki na v0.203:*** *"um inimigo tem que ser calculado pra todas as situações, para fazer uma média. Vai ter grupo que vai ter 1 healer, vai ter o grupo que não vai ter healer, vai ter o grupo onde não tem healer mas cada um tem `Circulação` ou pelo menos `Energia Reversa`."*

**A linha do manual foi calibrada contra um grupo que não cura.** *Medindo contra os que curam, o resultado sai ao contrário do esperado.*

| composição, no nível 30 | luta | o chefe entrega | a cura repõe | líquido | do grupo |
|---|---|---|---|---|---|
| sem cura nenhuma | `3,00` | `657` | — | **`657`** | `68%` |
| um suporte, área ou alvo único conforme o turno | `4,00` | `876` | `45` | `832` | `86%` |
| um só com `Energia Reversa` segurando o grupo | `4,00` | `876` | `126` | `750` | `77%` |
| sem suporte, os quatro se curando em rodadas alternadas | `6,00` | `1314` | `135` | **`1179`** | `121%` |

**Toda composição que cura sai PIOR que a que não cura, e o motivo é economia de ação.** *Curar gasta a ação que causaria dano; menos dano faz a luta durar mais; e cada rodada a mais é mais uma rodada do chefe.* **Ele entrega `219` por rodada e nenhuma cura de alvo único do sistema repõe isso** — um atacante que para de bater abre mão de `78,75`.

> **A única que ganha a troca é a cura em ÁREA**, porque ela multiplica por alvo: quatro alvos vezes `45` da `Onda` de Classe 7 passam dos `78,75`. *E ela é a que mais depende de como o chefe bate — contra um chefe que concentra, três quartos dela caem em quem está inteiro.*
>
> **⚠ E é por isso que a linha do manual NÃO desconta cura.** *Descontar deixaria o chefe mais fraco justamente contra os grupos que já sofrem mais.* **A calibragem fica contra o grupo que não cura, e esta tabela existe para o mestre saber o que muda quando ele cura.**

**O molde disso é o do d20, e ele foi lido antes de a tabela ser escrita.** *A `Palavra Curativa` do `Livro do Jogador` de 2024 é Ação Bônus e cura pouco de propósito, e a regra de `0` PV de lá diz que o personagem fica Inconsciente "até recuperar qualquer quantidade de Pontos de Vida".* **Cura ali não existe para deixar ninguém inteiro: ela existe para levantar quem caiu, e é isso que a peça 1 §5.5 já escreve deste lado.**

> ***Decisão do Mizuki:*** *"cura deve ser feita para segurar um pouco de dano, tirar o cara de morrer no próximo tapa — semelhante ao d20, onde cura não é feita pra deixar uma pessoa full."*
>
> **O número que fecha isso:** *levantar alguém de `0` gastando a Ação Padrão é empate exato — você perde a sua rodada e devolve a dele.* **Na Ação Bônus o saldo vira `+51,8`**, e é essa a metade que a aptidão `Circulação` da peça 11 §6 existe para dar.

## 5. O câmbio — um corpo grande vale quatro pequenos

**Dentro de uma categoria o mestre troca o corpo único por vários, e a troca é `1` para `4`.** *O capanga é a coluna que a tabela do manual já publica ao lado da do chefe.*

> **Um chefe de `Alcateia` vale quatro capangas do mesmo nível.**

**Desde a v0.201 o capanga não é medido: ele é derivado, e as duas linhas dele saem do chefe.**

> **Quatro capangas juntos têm a vida do chefe, e cada um bate o golpe dele.**
> **Vida do capanga = a vida do chefe dividida por quatro. Dano do capanga = o dano do chefe dividido por três**, que é o golpe de uma ação dele.

**Com isso o câmbio deixa de sair de simulação e passa a fechar na aritmética: os dois lados entregam NOVE GOLPES.** *O chefe age três vezes por rodada e a luta dura três rodadas — `3 × 3`. Os quatro capangas têm a vida dele, então caem no mesmo ritmo em que ele cairia: quatro golpes na primeira rodada, três na segunda, dois na terceira — `4 + 3 + 2`.*

**No nível 30 os dois cobram `657` de dano em `3` rodadas, e `657` é `68%` da vida do grupo.** *Não é aproximação: é o mesmo número, nas seis faixas que têm capanga.*

> **A simulação continua rodando no validador, e é ela que prova a igualdade.** *Ela não escolhe mais o `4` — ela confere que o `4` derivado é o que ela devolve.*

> **⚠ E o trade-off que sobra não é de tamanho: é de FORMA.** *Os quatro corpos entregam quatro golpes na primeira rodada e dois na última; o chefe entrega três em todas.* **O enxame morde mais cedo e afrouxa no fim, e o corpo único não afrouxa nunca** — é o mesmo fenômeno que o multiplicador de encontro do 5e de 2014 existia para representar, e que a edição de 2024 apagou por imprecisão.
>
> *Até a v0.200 este parágrafo dizia que o enxame era "um pouco mais duro". Com o capanga derivado os dois cobram o mesmo `657`, e o que os separa passou a ser só a distribuição.*

### 5.1 A faixa mais baixa não tem capanga, e isso é o piso

***Decisão do Mizuki na v0.199:*** **a linha da Classe 1 — o nível 2 ao 4 — sai com a coluna de capanga vazia.**

**Do nível 2 ao 4 o encontro é um inimigo só.**

> **⚠⚠ E a razão aritmética que sustentava esta decisão PAROU DE REPRODUZIR na v0.201.** *Ela era: "com o corpo que a proporção daria, `17` de vida, dois deles cairiam na primeira rodada de um grupo que causa `38`".* **Com a tabela nova o corpo tem `29` de vida, e quatro deles duram `3,05` rodadas — a mesma durabilidade das outras seis faixas.** *O capanga do fundo virou um corpo viável, e a conta não pede mais que a coluna fique vazia.*
>
> **A decisão fica de pé, e ela agora se apoia só no levantamento de fora.** *Reabrir a coluna da Classe 1 é escolha do Mizuki, e está no §8.*

> **O levantamento externo diz a mesma coisa por quatro caminhos.** *O `minion` do 4e resolve o fundo da escala tirando a vida do corpo — `1` ponto e dano fixo —, o `mook` do 13th Age junta a vida de todos num poço só, o `Guia do Mestre` de 2014 alarga as faixas do fundo (o `ND 1/8` vai de `7` a `35` de vida), e o Pathfinder 2e põe piso em `PL−4` e não usa criatura abaixo dele.* **Nenhum dos quatro trata o corpo pequeno como corpo grande encolhido.**
>
> **⚠ E a `Ronda` não substitui**, pelo §4.3: quatro delas cobram `0,75 ×` a `0,77 ×` o que a `Alcateia` cobra.

> **⚠⚠ E a conta que parece óbvia mata o grupo.** *Multiplicar vida por dano e dividir dá `12` capangas por chefe.* **Doze capangas no nível 30 cobram `473%` da vida do grupo, em `9` rodadas** — quase cinco vezes o que a categoria promete. *Por isso o câmbio está escrito aqui em vez de deixado para quem quiser derivar.*

## 6. O que ele carrega além dos números

***Decisão do Mizuki:*** **o inimigo se monta com as mesmas peças que um personagem, menos o Caminho.** *Na obra a maior parte do que se enfrenta é feiticeiro, e feiticeiro tem técnica, tem aptidão e tem Passiva — se a ficha de inimigo não alcançar isso, metade dos antagonistas não cabe nela.*

| ele tem | de onde sai |
|---|---|
| refino | a curva do `meio a meio`, peça 11 §3 |
| aptidões e Passivas | o catálogo da peça 11, o mesmo que o jogador usa |
| técnica, com Fundamento | o manual, quando ele é feiticeiro ou maldição de técnica |
| Legado, ferramenta, objeto | as peças 13, 16 e 21, quando a ficção pedir |

| ele não tem | por quê |
|---|---|
| Caminho e Trilha | as duas entregam por marco de campanha, e o inimigo não sobe de nível |
| poço de PE | o §6.1 |
| Origem | a peça 9 é a máquina de criação de quem senta na mesa |

### 6.1 O inimigo não conta PE, e a cota de dano é o orçamento dele

**Tudo que ele faz sai do dano por rodada da ficha.** *Uma técnica que causa dano entrega aquela cota e não mais que ela; uma que não causa dano troca parte da cota por outra coisa.*

**O precedente é do `Guia do Mestre` de 2014, e ele é explícito:** *o que um monstro tem é dano por rodada, e como esse dano se divide em ataques é livre.* **Contar PE de inimigo criaria uma segunda economia que só o mestre opera**, e ela responderia diferente em duas mesas.

> **Isso é a regra de ouro nº 6 pelo outro lado.** *O personagem tem um teto de saída por rodada e paga em PE para chegar nele; o inimigo tem o mesmo teto escrito direto, sem a moeda no meio.*

### 6.2 E existe inimigo sem energia nenhuma

**Ele não tem refino, aptidão nem técnica, e a cota de dano vem do corpo.** *É a forma da Restrição Celestial pelo ramo da Maki, do lado de lá da mesa* — **e a ficha não muda de tamanho por causa disso:** a vida e o dano continuam saindo da categoria, porque a categoria mede o que o encontro custa, e não de onde ele tira força.

> **⚠ E aqui a fronteira da obra encosta na mecânica sem virar número.** *O que separa uma maldição de grau 2 de uma de semi-grau 1, na classificação da obra, é saber usar técnica.* **A ficha carrega essa linha na coluna `técnica`**, e o rótulo do §2 fica legível sem entrar em conta.

### 6.3 Resistência é vida escondida, e ela custa degrau de categoria

**A peça 19 §4 divide os catorze tipos de dano em três grupos e diz quanto cada um pesa no que um alvo recebe** — `Físicos 60%`, `Elementais 30%`, `Especiais 10%`. **Resistir corta pela metade o que entra por aquele grupo, e isso sobe a vida efetiva do inimigo:**

| grupo | peso | resistência | imunidade | vulnerabilidade |
|---|---|---|---|---|
| `Físicos` | `60%` | **`1,43×`** | **`2,50×`** | `0,62×` |
| `Elementais` | `30%` | `1,18×` | `1,43×` | `0,77×` |
| `Especiais` | `10%` | `1,05×` | `1,11×` | `0,91×` |
| um tipo só | `20%` | `1,11×` | `1,25×` | `0,83×` |

**Um chefe de `Alcateia` imune a `Físicos` vira uma luta de `7,50` rodadas que cobra `169%` da vida do grupo**, contra as `3,00` rodadas e `68%` que a categoria promete. *A ficha diz uma coisa e a mesa joga outra, e com a linha da v0.201 a diferença deixou de ser uma luta mais longa e passou a ser uma luta que o grupo não termina de pé.*

**A escada de categoria já é a moeda disso.** *Subir da `Alcateia` para a `Calamidade` vale `1,50×`, e resistir a `Físicos` vale `1,43×`.*

> **Resistência ao grupo `Físicos` custa um degrau de categoria.** *Aos `Elementais`, meio degrau; aos `Especiais`, nada.*
> **Imunidade a `Físicos` custa mais de um degrau, e a escada não tem o que vender acima da `Calamidade`** — então ela só existe num inimigo que já esteja abaixo do topo.
> **Vulnerabilidade devolve na mesma moeda.**

**O mecanismo é o do `Guia do Mestre` de 2014**, que tem uma tabela de `Pontos de Vida Efetivos` fazendo exatamente isso. *Lá o multiplicador encolhe conforme o nível sobe, porque o grupo ganha jeitos de furar; aqui ele não encolhe, porque o `60/30/10` é fixo.*

> **⚠ E toda esta régua está pendurada num palpite, que a peça 19 §4 declara com todas as letras:** *o peso dos três grupos é previsão, `04-playtest/` está vazia, e ele é "o número que decide quanto vale toda resistência do sistema".* **Quando a mesa corrigir o peso, o multiplicador se refaz sozinho** — ele é conta, e não tabela.

### 6.4 A Expansão de Domínio do inimigo — ela DOBRA a categoria

***Decisão do Mizuki: a Expansão do inimigo é a do jogador, escalonada para grupo.*** *A máquina inteira mora no manual, e nada dela é reescrito aqui.*

**Ela não acrescenta dano nenhum, e é isso que faz o preço dela ser fácil de achar.** *Pelo §6.1 tudo que o inimigo faz sai da cota de dano por rodada, e o Acerto de um domínio não é exceção: a cota é a mesma dentro e fora.* **O que muda é quanto dela CHEGA.**

> **Fora do domínio o inimigo acerta `52%` — é a banda de `50%` a `55%` que o §3.1 publica.** *Dentro, o Acerto acontece: sem rolagem e sem Teste de Resistência, como o manual escreve.*
> **Então a Expansão completa multiplica a saída efetiva dele por `1 ÷ 0,52`, que é `1,92 ×`.**

**E a categoria mede exatamente a coisa que esse número move.** *Ela é "quantos personagens ele exige", e o fator dela é `personagens ÷ 4`.* **Como `1,92` arredonda para `2`, a regra sai em uma linha:**

> **Uma Expansão de Domínio completa DOBRA quantos personagens o inimigo exige.**

| categoria | exige | com Expansão completa |
|---|---|---|
| **`Ronda`** | `1` | `2` — vira uma **`Dupla`** |
| **`Dupla`** | `2` | `4` — vira uma **`Alcateia`** |
| **`Alcateia`** | `4` | **`8`** — acima da escada |
| **`Calamidade`** | `6` | **`12`** — acima da escada |

**Duas caem em degraus que a escada já tem, e duas passam do topo.** *A escada sobe `2,00 ×`, `2,00 ×` e `1,50 ×` — o último degrau é menor que a Expansão, então as duas de cima saem dela.* **Isso não é impedimento: a categoria mede pessoas, e o número existe fora da escada do mesmo jeito.**

> **⚠⚠ E é por isso que o chefe da obra com domínio nunca é enfrentado por quatro.** *Uma `Calamidade` com Expansão exige **doze** feiticeiros.* **A régua diz, em número, a coisa que a ficção já dizia: contra isso o grupo não ganha — ele foge, ou traz gente.**
>
> ***⚠ A primeira forma desta seção estava errada, e quem achou foi o Mizuki:*** *"não faz sentido um Sukuna da vida não ter expansão, ele seria Calamidade, não?"* **Ela media só para BAIXO — "com que linha eu monto para o encontro não crescer" — e, não achando degrau abaixo da `Calamidade`, concluía que aquela categoria não podia ter domínio.** *A conclusão não segue.* **O que falta ali não é a permissão: é o número do encontro maior**, e ele existe porque a categoria mede pessoas e não degraus.
>
> *Uma régua que proíbe o chefe mais famoso da obra de fazer a coisa mais famosa dele está errada antes de qualquer conta.*

**O mestre usa a regra dos dois lados, e os dois são a mesma conta:**

> **Quer manter o tamanho?** *Monte com a linha da categoria de baixo* — uma `Alcateia` com domínio construída com os `109` de dano por rodada da `Dupla` entrega os `109` inteiros, contra os `114` efetivos de uma `Alcateia` normal. **Só a `Dupla` e a `Alcateia` têm linha abaixo para isso.**
>
> **Quer o inimigo maior?** *Deixe a linha como está e leia a coluna da direita* — o encontro passou a exigir o dobro de gente, e o mestre monta a mesa sabendo disso.

**A incompleta não custa nada nesta régua.** *O manual diz que o Acerto dela "resolve por rolagem, como um feitiço"* — **sem a garantia não existe o `1,92 ×`**, e o que ela dá é o Efeito, que não é dano. *Qualquer categoria pode ter uma.*

**E abrir não custa rodada ao inimigo, apesar de custar ao jogador.** *O manual cobra a rodada inteira e `6 ×` a maior Classe de PE; o inimigo não conta PE pelo §6.1, e o Acerto acontece no momento em que ele abre.* **A cota daquela rodada sai pelo Acerto em vez de sair pelos golpes, e nada se perde.**

> **A duração cobre a luta inteira, e é por isso que o multiplicador vale o encontro todo.** *O manual põe a duração em metade do refino, e o refino do chefe do nível 30 é `10` — cinco rodadas contra uma luta de `3,00`.*

## 7. O que o `conferir-bestiario.py` confere

| # | o que ela confere |
|---|---|
| **1** | **as âncoras existem nos donos.** Cada número que a ficha usa aparece no documento que esta peça declara como dono, e a tabela do §3 é comparada com a lista do validador nos dois sentidos |
| **2** | **as três derivadas reconstroem.** A Defesa, o acerto e a CD saem das fórmulas da peça 1 §5, com a proteção andando junto do refino — e o resultado tem de bater com os `50%` a `55%` de acerto e os `35%` de falha que a peça 1 §6 publica |
| **3** | **a categoria é cópia com dono.** Vida e dano de cada uma reconstroem da linha do manual vezes o fator, e o fator reconstrói do número de personagens |
| **4** | **as ações saem da frase do manual**, e a `Alcateia` bate com o piso que a peça 19 §2.2 publica. *Se aquele piso mudar, esta acende* |
| **5** | **o câmbio é medido, não guardado.** A simulação de fogo concentrado é rodada aqui dentro, e o `4` publicado tem de ser o que ela devolve. *Desde a v0.201 ela confere mais duas coisas: que o capanga do manual É a vida do chefe dividida por quatro e o dano dele dividido por três, e que os dois lados cobram o mesmo dano na mesma quantidade de rodadas* |
| **5.1** | **a coluna da sub-categoria reconta.** As quatro formas do §4.5 são simuladas com os capangas abatidos primeiro, e as porcentagens publicadas têm de ser o que a simulação devolve. *Ela nasceu na v0.201 porque aquela coluna nunca teve validador e tinha divergido: o publicado subia de `28%` a `35%` e a simulação não reproduzia nem a ordem* |
| **6** | **o grau não vira número.** Nenhuma linha desta peça pode pendurar valor no grau, e o `ESTADO-ATUAL` e a peça 12 continuam dizendo que inimigo não tem grau mecânico |
| **7** | **nenhum valor de regra guardado aqui dentro.** Todo número vem do dono, e a checagem falha se algum sobrar como constante |
| **8** | **resistência é vida escondida.** Os pesos dos três grupos saem da peça 19 §4, os multiplicadores do §6.3 são recalculados de `1 ÷ (1 − o que se poupa)`, e a peça tem de declarar em que moeda a resistência se paga. *Sem essa declaração ela é vida de graça, e a categoria passa a mentir sobre o encontro*

### 7.1 As dezoito perturbações, em cópia isolada

*Com a base conferida verde e com `PULADA` zero antes de cada uma, com o `diff` comparado antes e depois, e com o veredito lido da checagem que estava sendo testada — nunca do código de retorno.*

> **⚠ E uma das seis da v0.199 saiu VERDE pelo motivo errado na primeira rodada.** *A âncora do pacto aparece **três** vezes na peça 22, e a perturbação trocava uma só* — **o validador achava as outras duas e não acusava.** *É o defeito que a peça 19 §7 já registra com estas palavras: perturbação mal mirada produz um "não acendeu" que parece prova.* **Refeita trocando todas as três, ela acende.**

| checagem | perturbação | esperado | deu |
|---|---|---|---|
| **1.1** | linha nova na ficha do §3 | acende | acende |
| **2** | a Defesa do nível 5 vira `15` no §3.1 | acende | acende |
| **2** | a curva do `meio a meio` muda na peça 11 | acende | acende |
| **2** | a peça 1 §6 perde a oscilação declarada | acende | acende |
| **3** | uma célula de vida do §4.1 vira `999` | acende | acende |
| **3** | o fator da `Dupla` vira `0,60` | acende | acende |
| **4** | a `Alcateia` publica `4` ações | acende | acende |
| **4** | a peça 19 baixa o piso das ações para `2` | acende | acende |
| **5** | a peça publica o câmbio em `cinco` | acende | acende |
| **6** | uma linha viva pendura número no grau | acende | acende |
| **2** | **contra-teste:** mexer em prosa sem mexer em número | fica verde | fica verde |
| **3** | **contra-teste:** a `Calamidade` vira `8` personagens, coerente nas duas tabelas | fica verde | fica verde |
| **8** | o multiplicador dos `Físicos` vira `1,60×` | acende | acende |
| **8** | o peso dos `Físicos` muda na peça 19 | acende | acende |
| **8** | a peça para de declarar em que moeda a resistência se paga | acende | acende |
| **1** | o teto de pacto some da peça 22 | acende | acende |
| **1.1** | a linha dos atributos sai da ficha | acende | acende |
| **8** | **contra-teste:** o peso muda na peça 19 **e** no §6.3, coerente | fica verde | fica verde |

> **O contra-teste da `3` é o que prova a checagem.** *Trocar a `Calamidade` para oito personagens muda o fator para `2,00`, as ações para `7` e as três células de ficha — e a checagem sai verde,* **porque ela mede a derivação e não os números publicados.**
>
> **⚠ E a terceira perturbação achou um defeito na checagem `2` antes de ela valer.** *A tabela da peça 1 §6 amostra os níveis de marco, que são os **picos** da curva de acerto — ela publica `55%` em todas as colunas.* **Medir a banda só por ela dava um ponto só, e o inimigo, amostrado em níveis que não são marco, caía fora dela sem nada estar errado.** *O vale não está na tabela: ele está declarado ao lado, como oscilação irredutível de `5pp`.* **Hoje a checagem lê os dois — o pico da tabela e a oscilação declarada — e a banda sai `50%` a `55%`.**

## 8. Em aberto

- ~~**⚠⚠ A pressão do chefe é `3,3 ×` menor que a do d20.**~~ ***FECHADA na v0.201***, com a tabela `Inimigos` refeita e o manual na `v7.23`. **O chefe entrega `90%` da vida de um personagem por rodada e tem `3 ×` o dano de rodada do grupo em vida** — `22,5%` do grupo por rodada, luta de `3` rodadas, e ele derruba `2,70` pessoas se concentrar.

  > **A metade que faltava foi achada onde o livro não diz, mas mostra.** *O `Guia do Mestre` manda tirar a média do dano de um monstro "para as três primeiras rodadas de combate", e essa é a única duração que ele declara.* **Daí sai a saída do grupo: a vida do chefe dividida por três.** *Conferida por um segundo caminho que não conversa com ela — um Guerreiro e um Ladino do Livro do Jogador de 2024, sem magia nenhuma, já entregam metade disso em todo nível.*
  >
  > **⚠ E o `3,3 ×` estava alto.** *Ele saiu de ler o TOPO da faixa de dano do d20 contra o valor único daqui.* **Meio contra meio a diferença era `2,6 ×` a `3,0 ×`**, e a tabela nova é `3,04 ×` no nível 30.
  >
  > **A régua de condição não foi repreçada, e isso é decisão do Mizuki:** *"tem que considerar que o boss também vai poder aplicar condições, troca como a régua mede."* **A peça 19 §2.2 passou a perguntar outra coisa, e as treze passam sem mexer em preço nenhum.**

- **A coluna de capanga da Classe 1, que a v0.199 deixou vazia por uma razão que morreu.** *O §5.1 registra: com a tabela nova o corpo do fundo tem `29` de vida e quatro deles duram `3,05` rodadas, igual às outras seis faixas.* **Encher a coluna é escolha do Mizuki**, e ela custa uma linha na tabela do manual mais o texto do §5.1.

- **As maldições prontas.** *A decisão da v0.161 é máquina mais prontas, e esta versão entrega a máquina.* **Quantas, de que categorias e com que técnicas é escolha do Mizuki**, e o catálogo é a versão seguinte.
- ~~**A Expansão de Domínio de inimigo.**~~ ***FECHADA na v0.204, no §6.4:*** **ela custa um degrau de categoria**, porque o Acerto garantido multiplica a saída efetiva por `1,92 ×` e os dois degraus de baixo da escada valem `2,00 ×`. *Só cabe na `Dupla` e na `Alcateia` — a `Calamidade` não tem degrau de `2 ×` abaixo dela e a `Ronda` não tem degrau nenhum.*
- **O inimigo com Trilha.** *Fica de fora por decisão, e o motivo está no §6* — mas um antagonista recorrente que sobe junto com o grupo é caso de mesa que vai aparecer.
- ~~**A ficha impressa.**~~ ***FECHADA na v0.199:*** **`05-material/bloco-de-inimigo.docx`**, quatro páginas — as tabelas que o mestre copia, o bloco em branco com as dezessete linhas, e um exemplo preenchido. *O gerador é o `gerador-inimigo/`, e o bloco `7` do `conferir-ficha.py` compara o `dados.js` dele com esta peça.*

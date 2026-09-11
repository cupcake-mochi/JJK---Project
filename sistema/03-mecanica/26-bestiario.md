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

**Dezoito linhas. Nenhum número novo nasce aqui** — o que esta peça faz é dizer de onde cada um sai.

| linha | valor | dono |
|---|---|---|
| nível | o nível do grupo | o mestre declara antes da mesa |
| categoria | `Capanga` · `Ameaça` · `Desastre` · `Catástrofe` · `Calamidade` | o §4 |
| vida | a linha do manual vezes o fator da categoria; a do `Capanga` é o dano do grupo dividido por quatro | manual, a tabela `Inimigos` |
| **Integridade** | igual à vida máxima | manual, a seção `Inimigos` |
| dano por rodada | a linha do manual vezes o fator da categoria — e menos em quem carrega `Intervenção`, pelo §6.5 | manual, a tabela `Inimigos` |
| ações por rodada | declaradas pela categoria | o §4.2 |
| **Defesa** | `10 + Destreza + proteção` | peça 1 §5 |
| **acerto** | `atributo + maestria` | peça 1 §5 |
| **CD** | `8 + atributo + maestria` | peça 1 §5 |
| Reação | uma por rodada, volta no começo do turno dele | manual, a seção `Inimigos` |
| refino | a curva do `meio a meio` | peça 11 §3 |
| Testes de Resistência | dois treinados de quatro | peça 7 §6 |
| deslocamento | `9 m` | peça 3 §3 |
| tamanho | o alcance do golpe e onde o corpo cabe — não cobra nada | o §3.3 |
| **atributos** | os cinco, no orçamento da peça 2 | peça 2 §3 |
| **características** | Passivas, aptidões e técnica, pelo §6 | peça 11, o mesmo catálogo do jogador |
| **pacto** | opcional, e o teto do permanente é da Essência dele | peça 22 §3 |
| **resistência, vulnerabilidade e imunidade** | multiplicam o fator da categoria, pelo §6.3 | peça 19 §4 |

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

### 3.3 O tamanho — o alcance, e ele não cobra nada

**O tamanho diz onde o corpo cabe e até onde o golpe alcança.** *Ele não tira Defesa, não mexe na vida e não pede nada em troca:* **o tamanho não cobra nada.**

| tamanho | ocupa na grade | alcance | o golpe pega |
|---|---|---|---|
| `Minúsculo` · `Pequeno` · **`Médio`** | `1×1` *(1,5 × 1,5 m)* | `1,5 m` | só o alvo |
| **`Grande`** | `2×2` *(3 × 3 m)* | `3 m` | o alvo, e metade em `1` vizinho |
| **`Imenso`** | `3×3` *(4,5 × 4,5 m)* | `4,5 m` | o alvo, e metade em `1` vizinho |
| **`Colossal`** | `4×4` *(6 × 6 m)* | `6 m` | o alvo, e metade em `1` vizinho |

**O alcance é o lado da grade vezes o quadrado, e nos alvos o tamanho é um degrau só:** *`Grande`, `Imenso` e `Colossal` pegam o mesmo vizinho a metade.*

> **⚠ E ele põe perto de um quinto de encontro FORA da conta, declarado de propósito.** *Um inimigo de `Grande` para cima entrega isso a mais que um `Médio` da mesma categoria, de graça.* **Medido no projeto do Bestiário em três sistemas:** *a defesa não muda com o tamanho em nenhum deles — `1,000 ×` em `4.791` criaturas do PF2e, `1,016 ×` em `331` do D&D —, os alvos não escalam, e o alcance escala.* **O campo põe o preço do tamanho na organização e no nível; a categoria daqui não sabe do tamanho, e isto está escrito para o mestre contar com a folga.**

## 4. A categoria — quantos personagens ele exige

***Ideia do Mizuki, e o eixo é o dele:*** *quantos feiticeiros são precisos para enfrentar aquilo.* **A tabela de inimigo do manual já responde isso para um número — ela é calibrada para quatro —, e a categoria é aquela linha reescalada.**

| categoria | personagens | fator sobre a linha do manual | ações | `Intervenção` |
|---|---|---|---|---|
| **`Capanga`** | — | `× 0,25` | `1` | não |
| **`Ameaça`** | 1 | `× 0,25` | `1` | não |
| **`Desastre`** | 4 | `× 1,00` | `3` | sim |
| **`Catástrofe`** | 6 | `× 1,50` | `5` | sim |
| **`Calamidade`** | 8 | `× 2,00` | `6` | sim |

**O `Desastre` é a linha do manual sem tocar em nada.** *As outras saem dela, e nenhuma inventa número.* **E o fator e o número de pessoas são a mesma coisa em duas unidades: `personagens = fator × 4`.** *Um inimigo de fator `1,92` exige `7,7` pessoas, e isso se lê sem tabela.*

> **O `Capanga` é a exceção de uma coluna só.** *O fator dele vale para o dano; a vida não sai do fator, sai do dano do grupo dividido por quatro — é o que UM personagem derruba num golpe —, e ele vem em esquadrão de `8` corpos, com a vida num pool só.* **Por isso ele não tem número de personagens: o preço dele é o câmbio do §5.**
>
> **⚠ Esta escada foi refeita no projeto do Bestiário, em 08/09/2026, e substitui a de quatro degraus que esta peça publicou da v0.198 à v0.220.** *`Ronda` virou `Ameaça` e `Alcateia` virou `Desastre`, com os mesmos números; a `Calamidade` de seis pessoas virou `Catástrofe`, e a `Calamidade` de hoje exige oito.* **A `Dupla` morreu:** *ela levava o dobro do orçamento pela mesma porta, e o golpe dela era `1,60 ×` o topo da banda que as outras respeitam.*

### 4.1 A ficha pronta de cada categoria, nos três níveis que a tabela publica

| categoria | nv 10 | nv 20 | nv 30 |
|---|---|---|---|
| `Capanga` | `32` vida · `19` dano | `55` · `37` | `78` · `55` |
| `Ameaça` | `97` vida · `19` dano | `165` · `37` | `236` · `55` |
| `Desastre` | `390` · `75` | `660` · `147` | `945` · `219` |
| `Catástrofe` | `585` · `112` | `990` · `220` | `1417` · `328` |
| `Calamidade` | `780` · `150` | `1320` · `294` | `1890` · `438` |

*A vida do `Capanga` é a de UM corpo; o esquadrão tem oito, num pool.*

> **⚠ O arredondamento é meio para BAIXO, e ele é declarado porque não é cosmético.** *Os fatores `0,25` e `1,50` põem **doze das sessenta e três células** desta escala exatamente em `,5`.* **Três lugares calculam isto — a peça, o validador e o gerador do bloco — e cada linguagem arredonda de um jeito:** *o `Math.round` do JavaScript sobe, o `round` do Python vai para o par.* **Sem a regra escrita, os três divergem, e o mestre lê o número em voz alta na mesa.**
>
> **⚠ E a vida do `Capanga` arredonda PARA BAIXO, por inteiro, que é outra regra.** *Um quarto de ponto de vida põe o esquadrão vivo numa rodada a mais, e a rodada a mais custa `11` pontos percentuais de encontro* — **é o mesmo defeito que o §5.1 registra no chefe do nível 2.**

### 4.2 As ações são declaradas pela categoria

**O `Desastre` age três vezes, e isso sai da frase do manual:** *o chefe "perde a ação três vezes por rodada" contra um grupo de quatro — ele age uma vez enquanto eles agem quatro.* **As outras quatro categorias têm o número delas escrito na tabela do §4**, e ele não sai de fórmula: *`Capanga` e `Ameaça` agem uma vez, a `Catástrofe` cinco e a `Calamidade` seis.*

> **⚠ Até a v0.220 as ações saíam de `personagens − 1`, com piso `1`, e foi isso que quebrou a `Dupla`.** *A razão `pessoas ÷ (pessoas − 1)` explode embaixo — `2 ÷ 1`, `4 ÷ 3`, `6 ÷ 5` —, e a categoria de duas pessoas levava o dobro do orçamento pela mesma porta, numa ação só.* **Declarando, o defeito não tem por onde nascer.**

> **⚠ E o `Desastre` não pode descer de `3`, e isso não é desta peça.** *A peça 19 §2.2 preça quatro das treze condições dividindo pelas ações do chefe.* **Com `2` as quatro passam do teto do próprio tier**, e o piso está medido lá, com a checagem `12` daquele validador em cima.

### 4.5 A sub-categoria — em quantos corpos o encontro se parte

***Ideia do Mizuki:*** *nem todo combate tem mais de um inimigo, e o mesmo encontro pode vir num corpo só ou repartido.* **A categoria diz o TAMANHO; a sub-categoria diz a FORMA.**

| sub-categoria | o chefe fica com | capangas | cobra do grupo |
|---|---|---|---|
| **`sozinho`** | `100%` | — | `67,6%` |
| **`com um apoio`** | `91,5%` | `1` | `67,5%` |
| **`com dois`** | `83,0%` | `2` | `67,4%` |
| **`bando`** | `74,5%` | `3` | `67,3%` |

**A fração não foi escolhida: ela é a que devolve o que o chefe sozinho cobra.** *O projeto do Bestiário varreu `201` frações do chefe em `29` níveis, com o `Capanga` da escada.* **Os três primeiros capangas tomam `8,5%` do chefe cada um — praticamente `1/12`.**

> **⚠ E o câmbio NÃO é linear além de três corpos.** *Do quarto ao sétimo capanga cada corpo passa a tomar de `11%` a `17%` do chefe — `≈ 1/6`* —, **porque um esquadrão cheio cobre os próprios buracos, e cada corpo passa a valer o dobro.** *A tabela para em três de propósito.*
>
> **⚠ As frações saem com uma casa decimal, e isso não é preciosismo.** *Com um capanga, o chefe a `91,5%` cobra `67,5%` da vida do grupo em 3 rodadas, e a `92%` cobra `88,6%` em 4:* **meio ponto percentual atravessa a borda de uma rodada.**
>
> **⚠ A coluna da direita depende de em que ordem o grupo abate, e a ordem está declarada: os capangas primeiro.** *É o que a mesa faz sozinha — o capanga cai num golpe de um personagem.* **E ela é medida no nível 30, contra a vida do grupo da peça 1.**
>
> **⚠ A primeira forma desta tabela era do capanga da `Alcateia`** — *quatro corpos com um quarto da vida do chefe e um terço do dano, e as frações `100%` · `75%` · `50%` · `25%`.* **Aquele capanga morreu com a escada, e o câmbio `1/4` morreu junto.**

### 4.6 O chefe derruba alguém, e a métrica que mostra isso não é óbvia

**Um `Desastre` concentrando os três golpes derruba um personagem na rodada `1,11`.** *No nível 30 ele entrega `657` de dano na luta contra `243` do alvo, e a razão é a mesma em todo nível.* **Numa luta de três rodadas ele derruba `2,70` pessoas se concentrar** — não o grupo inteiro, e mais de uma.

> *Os números desta seção são do modelo sem `Intervenção`. Com ela, a luta de três rodadas entrega o mesmo total — é assim que o fator `0,923` do §6.5 foi calculado —, e as `2,70` pessoas continuam.*

> **⚠ A métrica errada é "quantas rodadas ele leva para derrubar o GRUPO", e até a v0.200 ela dava `14`** — contra uma luta de `3,7`. *Lida assim, a tabela de inimigo parecia fraca demais, e a v0.199 respondeu que ela não estava.* **Estava.** *O que a métrica errada escondia é que ele derrubava exatamente uma pessoa por luta, no último segundo, e a v0.201 mediu isso contra dois sistemas de fora.*
>
> **`2,70` é o número dos dois:** *o d20 de 2014 derruba `2,56` a `2,70` numa luta de três rodadas, e o chefe solo do Pathfinder 2e derruba perto de `2,8`.* **É a métrica que decidiu a tabela nova, e não a que decidiu a antiga.**
>
> **⚠ E o `2,70` é do modelo sem ATRITO, que é o modelo desta peça inteira: quem cai continua contando na saída do grupo.** *Medido com atrito e com o chefe concentrando e ganhando a iniciativa, ele derruba os quatro em cinco rodadas, nos sete níveis* — **porque cada pessoa que cai tira um quarto da saída, a luta estica, e a rodada extra é dele.** ***Decisão do Mizuki na v0.205: fica assim.*** *"Um inimigo focar um único player vai acabar matando mesmo, acho que todo sistema rola isso — o mestre não vai querer normalmente focar também."* **O `Guia do Mestre` tem a mesma simplificação: a conta de nível de desafio dele também é plana.**

### 4.4 O dano se rola em dado, e não em número seco

**O que a tabela do manual publica é o dano por RODADA, e o que o mestre rola é o de uma AÇÃO.** *Divida um pelo outro e você tem o alvo do golpe.*

> **O golpe é `N` dados mais um fixo, com metade do alvo em dado.** *O tamanho do dado se escolhe entre `d4`, `d6`, `d8`, `d10` e `d12` — o que fecha a metade mais limpo, com no máximo **oito** dados na mão.* **Abaixo de `5` o golpe fica em número seco** — um dado balançaria mais que o próprio golpe.

**O precedente é o `Guia do Mestre` de 2014**, que manda traduzir a margem de dano numa expressão de dado e diz que a divisão em ataques é livre. *Aqui a divisão não é livre: ela é o número de ações da categoria.*

| categoria, no nível 26 a 30 | por rodada | ações | o golpe |
|---|---|---|---|
| `Capanga` | `55` | `1` | `6d8 + 28` |
| `Ameaça` | `55` | `1` | `6d8 + 28` |
| `Desastre` | `219` | `3` | `8d8 + 37` |
| `Catástrofe` | `328` | `5` | `6d10 + 33` |
| `Calamidade` | `438` | `6` | `8d8 + 37` |

*O `Capanga` e a `Ameaça` batem o mesmo golpe, e o que separa os dois é a vida. O `Desastre` e a `Calamidade` também: a `Calamidade` tem o dobro do dano em o dobro de ações. Quem carrega `Intervenção` rola este golpe com o fator do §6.5.*

> **Menos ações quer dizer golpe maior**, *e é por isso que a `Catástrofe` bate menos que o `Desastre`: uma vez e meia o dano, em cinco ações em vez de três.*
>
> ~~**⚠⚠ E ele custa doze dados numa rolagem só, o que é caro em tempo de mesa.**~~ ***RESOLVIDO na v0.216, e não por decreto:*** **o dado deixou de ser sempre `d8`.** *Pedido do Mizuki — "não precisa sustentar pra sempre o `d8`, dá pra usar `d6`, `d4`, `d10`, `d12`, para ajudar nos cálculos".* **O maior punhado da tabela caiu de `12d8` para `8d12`** — *o da `Dupla`, que morreu com a escada; o maior de hoje é `8d8`.*
>
> **Medido nas vinte e sete células que rolavam dado na escada de então:** *a metade cai **exata** em `6` delas contra `0` do `d8` fixo, e o desvio médio não se move — `26,4%` para `25,0%`.* **O balanço é o mesmo; o que melhorou foi a aritmética e a mão.**
>
> **⚠ O teto de oito dados não é cosmético.** *Sem ele o otimizador troca `5d8 + 26` por `10d4 + 24`: fecha melhor na conta e é pior na mesa.*

### 4.3 ⚠ A categoria não é intercambiável consigo mesma

**Quatro `Ameaça` não valem um `Desastre`: elas cobram `0,75 ×` a `0,77 ×` o que ele cobra**, e a razão é a mesma nas sete faixas.

*A causa é que elas morrem em fila e a saída delas despenca — quatro corpos de um quarto entregam tudo enquanto estão os quatro de pé, e depois entregam cada vez menos.* **Somar os fatores dá a linha inteira; jogar os quatro não dá o mesmo encontro.** *E vale no degrau de baixo: duas `Ameaça` cobram `25%` a menos que um corpo de fator `0,50`, pela mesma razão.*

> **É por isso que o `Capanga` não é uma `Ameaça`.** *A `Ameaça` é um quarto do chefe nos dois eixos — um quarto da vida e um quarto do dano —, e o `Capanga` é `1/12` da vida com um QUARTO do dano.* **É essa diferença de um eixo só que faz o câmbio do §5 fechar em oito, e a `Ameaça` parar em `0,76`.**
>
> *Os números são os da escada de antes, com o nome novo: a `Ameaça` tem a vida, o dano e as ações que a `Ronda` tinha, e o `Desastre` os da `Alcateia`.* **O modelo do Bestiário refez a conta na escada viva e devolveu o mesmo `0,75 ×` a `0,77 ×`.**

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

## 5. O câmbio — um corpo grande vale oito pequenos

**O `Capanga` é a categoria que vem em bando, e o câmbio diz quantos corpos dele valem um chefe.** *Ele é o da escada: esquadrão de `8` corpos, vida num pool só, uma ação cada.*

> **Um `Desastre` vale oito capangas do mesmo nível.**

**As duas linhas do capanga são derivadas, e nenhuma sai da vida do chefe:**

> **Vida do capanga = o dano do grupo por rodada dividido por quatro, arredondado para baixo.** *É o que UM personagem derruba num golpe.*
> **Dano do capanga = o dano do chefe vezes o fator da categoria** — *o mesmo golpe da `Ameaça`.*

**Com isso o câmbio fecha na aritmética: o esquadrão entrega DOZE golpes de um quarto, e doze quartos são as três rodadas do chefe.** *O grupo derruba quatro corpos por rodada, então o esquadrão bate oito vezes na primeira e quatro na segunda — `8 + 4`. O chefe bate três vezes em cada uma de três rodadas.*

**No nível 30 o chefe cobra `657` de dano em `3` rodadas e o esquadrão cobra `660` em `2`.** *Nas sete faixas os dois ficam a menos de um golpe de capanga de distância.*

> **A simulação roda no validador, e é ela que prova a igualdade.** *Ela não escolhe o `8` — ela confere que o `8` é o número de corpos que devolve o chefe, nível a nível.*

> **⚠ E o trade-off que sobra não é de tamanho: é de FORMA.** *O esquadrão entrega oito golpes na primeira rodada e quatro na segunda; o chefe entrega três em cada uma de três.* **O enxame morde cedo e acaba cedo** — é o mesmo fenômeno que o multiplicador de encontro do 5e de 2014 existia para representar, e que a edição de 2024 apagou por imprecisão.
>
> **E ele precisa de uma trava para não concentrar:** *no máximo `3` corpos do mesmo esquadrão atacam o mesmo alvo por rodada, e do segundo em diante o golpe sai pela metade.* **Sem ela oito corpos entregam mais que a vida inteira de um personagem numa rodada; com ela, menos da metade.** *A trava não encolhe o esquadrão — os oito continuam entregando tudo, só não no mesmo alvo.*

> **⚠ O capanga que esta seção publicou da v0.201 à v0.220 era outro** — *quatro corpos, a vida do chefe dividida por quatro e o dano dividido por três, com a prova dos "nove golpes" (`3 × 3` contra `4 + 3 + 2`).* **Ele era o capanga da `Alcateia`, e morreu com ela.** *Estava certo por dentro; ele só não é o da escada viva. Ficar com um só foi decisão do Mizuki, em 10/09/2026.*

### 5.1 A linha do nível 2 estava um ponto fora, e um ponto era uma rodada

**A seção `Inimigos` do manual escreve a própria regra:** *o chefe sozinho tem cerca de **três vezes** o dano de rodada do grupo em vida, "e é isso que faz a luta contra ele durar três rodadas".* **Seis das sete linhas cumpriam isso exato; a do nível 2 publicava `115` contra os `114` que a regra pede.**

> **⚠⚠ E um ponto de vida custava uma rodada inteira do chefe.** *Com `115` a luta dura `3,03` rodadas, e rodada é inteira na mesa: o chefe age quatro vezes e o encontro cobra `89%` da vida do grupo, contra os `68%` que as outras seis cobram.* **No nível em que o personagem tem `19` de vida.**
>
> *A faixa virou `105 a 123`, com o meio em `114` e o espalhamento em `±7,9%` — dentro dos `±7,4%` a `±9,1%` das outras seis.* **Manual na `v7.25`.** *A checagem `5.2` do validador guarda isso.*

**É o mesmo defeito que a vida do `Capanga` teria sem arredondar para baixo:** *um quarto de ponto de vida põe o esquadrão vivo numa rodada a mais.* **Com o piso, o esquadrão do nível 2 tem `9` de vida por corpo — `38 ÷ 4` dá `9,5`, e fica `9`.**

> **⚠ E a conta que parece óbvia mata o grupo.** *O câmbio não é linear:* **do quarto ao sétimo capanga somado a um chefe inteiro, cada corpo passa a valer o dobro do primeiro**, porque o esquadrão cheio cobre os próprios buracos. *A régua do encontro misturado mora no §4.5 e para em três de propósito.*

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

### 6.3 Resistência é vida escondida, e ela multiplica o fator da categoria

**A peça 19 §4 divide os catorze tipos de dano em três grupos e diz quanto cada um pesa no que um alvo recebe** — `Físicos 60%`, `Elementais 30%`, `Especiais 10%`. **Resistir corta pela metade o que entra por aquele grupo, e isso sobe a vida efetiva do inimigo:**

| grupo | peso | resistência | imunidade | vulnerabilidade |
|---|---|---|---|---|
| `Físicos` | `60%` | **`1,43×`** | **`2,50×`** | `0,62×` |
| `Elementais` | `30%` | `1,18×` | `1,43×` | `0,77×` |
| `Especiais` | `10%` | `1,05×` | `1,11×` | `0,91×` |
| um tipo só | `20%` | `1,11×` | `1,25×` | `0,83×` |

**Um `Desastre` imune a `Físicos` vira uma luta de `7,50` rodadas**, contra as `3,00` que a categoria promete — *a vida efetiva dele é `2,50 ×` a publicada.* *A ficha diz uma coisa e a mesa joga outra, e com a linha da v0.201 a diferença deixou de ser uma luta mais longa e passou a ser uma luta que o grupo não termina de pé.*

**O fator da categoria é a moeda disso, e ele é contínuo.** *`fator novo = fator × o multiplicador da coisa` — e a leitura sai de graça, porque `personagens = fator × 4`.* **Um `Desastre` que resiste a `Físicos` fica em fator `1,43` e exige `5,7` personagens.**

> **Resistência ao grupo `Físicos` multiplica o fator da categoria por `1,43`.** *Aos `Elementais`, por `1,18`; aos `Especiais`, por `1,05`.*
> **Imunidade a `Físicos` multiplica o fator por `2,50`, e o resultado é um número de pessoas, não um nome.** *Aos `Elementais`, por `1,43`; aos `Especiais`, por `1,11`.*
> **A vulnerabilidade é `1,00×`: não cobra e não devolve.** *O dano daquele tipo dobra contra ele, e nada mais na ficha muda — nem o fator, nem a vida.*
> **Ser imune a uma condição que rouba ação do inimigo, ou que dá desvantagem nos ataques dele, multiplica o fator por `1,20`. Qualquer outra condição custa `1,00×`.**

> **⚠ Um `Desastre` imune a `Físicos` exige `10` personagens, não `4`.** *A edição viva do D&D publica isso zero vezes em `331` blocos — se você vender, saiba que está vendendo o item mais caro do livro.* **É aviso, e não trava.**

> **⚠ A coluna `vulnerabilidade` da tabela é conta de vida efetiva, e não preço.** *Ela diz quanto a luta encurta se o grupo inteiro bater naquele tipo, e a ficha não sabe o que o grupo carrega — por isso não cobra nem devolve.* **`4` de `4` sistemas medidos no Bestiário têm vulnerabilidade, e nenhum mexe no custo de encontro por ela.**
>
> *Até a v0.220 esta seção cobrava em "degrau de categoria". Na escada viva o degrau vai de `1,000 ×` a `4,000 ×`, e três dos quatro preços que ela cobrava não cabiam em degrau nenhum. **A moeda passou a ser o fator.***

**O mecanismo é o do `Guia do Mestre` de 2014**, que tem uma tabela de `Pontos de Vida Efetivos` fazendo exatamente isso. *Lá o multiplicador encolhe conforme o nível sobe, porque o grupo ganha jeitos de furar; aqui ele não encolhe, porque o `60/30/10` é fixo.*

> **⚠ E toda esta régua está pendurada num palpite, que a peça 19 §4 declara com todas as letras:** *o peso dos três grupos é previsão, `04-playtest/` está vazia, e ele é "o número que decide quanto vale toda resistência do sistema".* **Quando a mesa corrigir o peso, o multiplicador se refaz sozinho** — ele é conta, e não tabela.

### 6.4 A Expansão de Domínio do inimigo — ela multiplica o fator por `1,92`

***Decisão do Mizuki: a Expansão do inimigo é a do jogador, escalonada para grupo.*** *A máquina inteira mora no manual, e nada dela é reescrito aqui.*

**Ela não acrescenta dano nenhum, e é isso que faz o preço dela ser fácil de achar.** *Pelo §6.1 tudo que o inimigo faz sai da cota de dano por rodada, e o Acerto de um domínio não é exceção: a cota é a mesma dentro e fora.* **O que muda é quanto dela CHEGA.**

> **Fora do domínio o inimigo acerta `52%` — é a banda de `50%` a `55%` que o §3.1 publica.** *Dentro, o Acerto acontece: sem rolagem e sem Teste de Resistência, como o manual escreve.*
> **Então a Expansão completa multiplica a saída efetiva dele por `1 ÷ 0,52`, que é `1,92 ×`.**

**E a categoria mede exatamente a coisa que esse número move.** *Ela é "quantos personagens ele exige", e `personagens = fator × 4`.* **Então a regra sai em uma linha, sem arredondar nada:**

> **Uma Expansão de Domínio completa multiplica o fator do inimigo por `1,92`** — *e, com ele, quantos personagens ele exige.*

| categoria | exige | com Expansão completa |
|---|---|---|
| **`Ameaça`** | `1` | `1,9` |
| **`Desastre`** | `4` | `7,7` |
| **`Catástrofe`** | `6` | `11,5` |
| **`Calamidade`** | `8` | `15,4` |

**Nenhuma cai num degrau da escada, e isso não é impedimento: a categoria mede pessoas, e o número existe fora da escada do mesmo jeito.** *Os cinco nomes são rótulos num contínuo, e não os únicos pontos onde dá para parar.*

> *Até a v0.220 esta seção arredondava o `1,92` para `2` e dizia que a Expansão "dobra a categoria". Na escada viva "dobrar" só pousa numa categoria de verdade em um caso — do `Desastre` para a `Calamidade` —, e os preços em degrau erravam de `13%` a `40%`.* **A moeda passou a ser o fator.**

> **⚠⚠ E é por isso que o chefe da obra com domínio nunca é enfrentado por quatro.** *Uma `Calamidade` com Expansão exige **`15,4`** feiticeiros.* **A régua diz, em número, a coisa que a ficção já dizia: contra isso o grupo não ganha — ele foge, ou traz gente.**
>
> ***⚠ A primeira forma desta seção estava errada, e quem achou foi o Mizuki:*** *"não faz sentido um Sukuna da vida não ter expansão, ele seria Calamidade, não?"* **Ela media só para BAIXO — "com que linha eu monto para o encontro não crescer" — e, não achando degrau abaixo da `Calamidade`, concluía que aquela categoria não podia ter domínio.** *A conclusão não segue.* **O que falta ali não é a permissão: é o número do encontro maior**, e ele existe porque a categoria mede pessoas e não degraus.
>
> *Uma régua que proíbe o chefe mais famoso da obra de fazer a coisa mais famosa dele está errada antes de qualquer conta.*

**O mestre usa a regra dos dois lados, e os dois são a mesma conta:**

> **Quer manter o tamanho?** *Divida o dano por rodada dele por `1,92`* — o domínio devolve o que foi tirado, e o encontro fica o da categoria. **Com o fator contínuo isso vale em qualquer categoria**, e não só nas que tinham degrau embaixo.
>
> **Quer o inimigo maior?** *Deixe a linha como está e leia a coluna da direita* — o encontro passou a exigir o dobro de gente, e o mestre monta a mesa sabendo disso.

**A incompleta não custa nada nesta régua.** *O manual diz que o Acerto dela "resolve por rolagem, como um feitiço"* — **sem a garantia não existe o `1,92 ×`**, e o que ela dá é o Efeito, que não é dano. *Qualquer categoria pode ter uma.*

**E abrir não custa rodada ao inimigo, apesar de custar ao jogador.** *O manual cobra a rodada inteira e `6 ×` a maior Classe de PE; o inimigo não conta PE pelo §6.1, e o Acerto acontece no momento em que ele abre.* **A cota daquela rodada sai pelo Acerto em vez de sair pelos golpes, e nada se perde.**

> **A duração cobre a luta inteira, e é por isso que o multiplicador vale o encontro todo.** *O manual põe a duração em metade do refino, e o refino do chefe do nível 30 é `10` — cinco rodadas contra uma luta de `3,00`.*

### 6.5 O catálogo do jogador na ficha do inimigo

***Decisão do Mizuki:*** *"dá pra deixar ser que nem do sistema pra player, mas rebalancear."* **O inimigo não ganha um catálogo de traços só dele — ele carrega as entradas que o jogador já tem, e o que muda é a moeda em que elas se pagam.**

*O §6 já dizia isso em palavras: refino, aptidão, Passiva e técnica saem do mesmo catálogo.* **O que faltava era o preço, e ele é um câmbio de três portas.**

| o que ele carrega | onde ela se paga |
|---|---|
| **técnica e feitiço** | o **orçamento de feitiço** de uma ação dele, e o Fundamento faz o resto |
| **aptidão e Passiva com custo por rodada** | a **cota de dano por rodada**, nas rodadas em que ela está ligada |
| **o que dá vida efetiva** | **multiplica o fator** da categoria, pelo §6.3 |

**A régua é a do `Guia do Mestre`, e o passo 13 escreve ela entre parênteses:** *as características de um monstro "não mudam realmente as estatísticas" dele — elas mexem na vida efetiva, no dano efetivo ou na CA efetiva.* **E o GURPS 4ed monta bicho assim, com as entradas do jogador:** *o bloco de lá publica "um resumo das metacaracterísticas, vantagens e desvantagens mais importantes" da criatura e deixa a lista cheia no modelo racial, com as secundárias "derivadas dos atributos de acordo com as fórmulas normais"* — **que é o que o §3.1 já faz aqui.**

#### A técnica: o golpe dele é o orçamento do feitiço

***Levantado pelo Mizuki:*** *"se for seguir próximo da criação de ficha normal, um feitiço em área vai ter menos dados para poder comprar condição."* **É exatamente isso, e é por isso que a técnica do inimigo não precisa de preço próprio: o Fundamento já cobra por área, por condição e por Melhoria, em ponto de feitiço.**

**O que a ficha precisa dizer é quantos pontos uma ação dele paga, e isso o §4.4 já publica em dano.** *A conversão é a do manual, que o §2.1 da peça 19 lê: cada ponto que não vira Melhoria vira `1d8`, que são `4,5` de dano.*

> **O orçamento de feitiço de uma ação é o golpe dela dividido por `4,5`.**

| pontos por ação | `Capanga` | `Ameaça` | `Desastre` | `Catástrofe` | `Calamidade` |
|---|---|---|---|---|---|
| nível 2 | seco | seco | seco | seco | seco |
| nível 5 | seco | seco | seco | seco | seco |
| nível 10 | `4,2` | `4,2` | `5,1` | `4,5` | `5,1` |
| nível 15 | `6,2` | `6,2` | `7,6` | `6,9` | `7,6` |
| nível 20 | `8,2` | `8,2` | `10,1` | `9,0` | `10,1` |
| nível 25 | `10,2` | `10,2` | `12,5` | `11,2` | `12,5` |
| nível 30 | `12,2` | `12,2` | `15,0` | `13,5` | `15,0` |

*O golpe entra aqui como a ficha imprime ele — a média do dado do §4.4 —, e quem carrega `Intervenção` entra já com o fator dela.*

**`seco` é o piso, e ele não foi escolhido: o menor feitiço do manual é a `Classe 1` e custa `3` pontos**, que são `13,5` de dano. *Abaixo disso o inimigo não monta feitiço nenhum — ele bate, e o golpe dele sai como o §4.4 manda.*

> **⚠ Este piso não é o mesmo do golpe em dado, e os dois vivem lado a lado.** *O §4.4 põe o número seco abaixo de `5` de dano, porque um `d8` balançaria mais que o próprio golpe; este põe o feitiço abaixo de `13,5`, porque é o que a `Classe 1` custa.* **Existe faixa que rola dado e não conjura** — *uma `Ameaça` de nível 5 bate `2d4 + 5`, dez de média, que é dado e não é feitiço.*

**A maior ação de inimigo do sistema é `15,0` pontos — o `Desastre` e a `Calamidade` do nível 30 —, e o teto do jogador naquele nível é `24`.** *Uma ação de inimigo é `62%` do maior feitiço que um personagem monta no mesmo nível, e ele compensa em quantidade: age três, cinco ou seis vezes por rodada, e o jogador age uma.* **Até a v0.220 o topo era a `Dupla`, com `24,2` pontos numa ação só — o degrau que levava o dobro do orçamento pela mesma porta.**

> **⚠ E é aqui que a condição do inimigo se resolve, sem moeda nova.** *Comprar condição dentro de um feitiço custa ponto, e ponto gasto em condição é dado que não foi comprado.* **A régua da peça 19 §2.2 vale dos dois lados da mesa desde a v0.201, então o preço já está escrito lá.**

#### A aptidão: ela come a cota, e só nas rodadas em que está ligada

**O jogador paga a aptidão em PE por rodada enquanto ela está de pé. O inimigo não conta PE pelo §6.1, então ele paga a mesma coisa na cota — e paga pelas mesmas rodadas.** *O câmbio tem dono: `+1` PE por rodada vale `5,14` de dano por rodada, pela peça 5 §4.*

> **`1` PE por rodada = `5,14` da cota de dano por rodada, contado só nas rodadas em que a aptidão está ligada.**
> **O teto é a cota daquela rodada** — ninguém gasta o que não tem. *Acima dele a aptidão não cabe naquela categoria, e o mestre sobe de categoria ou tira a aptidão.*

**O rebalanceamento que o Mizuki pediu está na razão entre as categorias.** *A mesma aptidão pesa quase quatro vezes mais numa `Ameaça` do que num `Desastre`: a cota da `Ameaça` é um quarto, e a do `Desastre` leva o fator da `Intervenção`.*

| ligada a luta inteira, no nível 30 | da cota de uma `Ameaça` | de um `Desastre` |
|---|---|---|
| `Domínio Simples` e `Pétala` · `1 ×` maior Classe | `65%` | `18%` |
| `Extensão de Domínio` · `1,5 ×` maior Classe | `98%` | `27%` |

**No nível 2 a `Extensão de Domínio` custa `193%` da cota de uma `Ameaça`, e por isso uma maldição daquele nível que a carregue tem de ser pelo menos um `Desastre`** — *lá ela cai para `49%`, e cabe.*

> **⚠ E contar por luta em vez de por rodada ligada estava errado, porque as quatro anti-domínio são pura resposta.** *Elas valem **zero** contra um grupo que não abre domínio.* **O jogador liga quando o domínio abre; o inimigo, cobrado por luta, pagaria pelas rodadas em que ela não fez nada.** *`Domínio Simples` ligado uma rodada de três custa `12,0` de dano, que são `5,9%` da cota de um `Desastre` e `22%` da de uma `Ameaça` — contra os `18%` e `65%` da tabela acima.*

#### A que sai de graça, e o número que prova isso

**Esta não muda a cota — ela muda a FORMA em que ela chega: em que rodada.** *É o mesmo fenômeno que o §4.4 e o §4.5 já medem.*

> **Habilidade guardada, `1 ×` por luta.** *Ela entrega o dobro de uma rodada e deixa as outras menores: no nível 30 são `438` numa e `110` nas outras duas, e o total é `657` — o publicado.*

#### A `Intervenção` — a ação fora do turno, por cima, e o que ela custa

**De `Desastre` para cima o inimigo carrega três `Intervenções` por luta.** *Cada uma é usada uma vez só, no máximo uma por rodada, logo depois do turno de outra criatura.* **A primeira bate — um pouco menos que uma ação normal; a segunda e a terceira mudam o campo em vez de causar dano.** *`Capanga` e `Ameaça` não têm.*

> **Ela é ação EXTRA, por cima das do §4.2, e se paga no dano: o fator de dano de quem carrega `Intervenção` é multiplicado por `0,923`.**

***As duas ideias fixas são do Mizuki:*** *"Inimigo tem ações"* e *"Intervenções são ações extras em meio aos turnos dos alvos. Nenhum sistema come ação do turno para ter essas 'intervenções', e é por um motivo."* **O `0,923` saiu da forma que o campo constrói:** *medidas `9` villain actions em `3` criaturas `Solo` do Draw Steel, a primeira abre com dano e as outras duas mudam o campo — `0,75` de ação extra numa luta de três rodadas.* **Com ele, o total da luta volta ao da tabela, e as `2,70` pessoas do §4.6 continuam.**

> **⚠ Até a v0.220 esta peça dizia o contrário: "as ações fora do turno saem das que ele já tem, nunca por cima".** *A medida daquela versão — `0,94 ×` a `1,07 ×` sobre `81` durações de luta — media a ação fora do turno tirada da cota, e ela continua certa para aquela leitura.* **A leitura mudou, e com ela o preço.**

#### A área — uma ação por rodada, e a `Recarga` não conta

> **No máximo `1` das ações dele por rodada pode ser em área. Ação de `Recarga` não conta nessa cota.** *Vale em toda categoria, e não muda com o nível.*

**Com `1` ação em área, todo mundo leva perto de metade da vida e a luta continua sendo uma luta; com `2`, o alvo termina a luta com `0,3%` de vida.** *E o `2,70` do §4.6 não existe em área: concentrando, a queda é uma curva; em área, é um penhasco — ou ninguém cai, ou a mesa inteira.*

> **A `Recarga (5-6)` é o rótulo do d20: a ação sai uma vez e volta no começo do turno dele com `5` ou `6` no `d6`, e ela ocupa uma das ações dele — não vem por cima.** *Uma área em recarga dispara `1,67 ×` numa luta de três rodadas e vale `0,557` de uma à vontade, então ela já se paga sozinha.* **Cobrar a cota em cima seria cobrar duas vezes.**

*Até a v0.220 esta peça dizia que "área reparte a cota, e não multiplica ela", e que a recarga `5-6` não cabia aqui.* **As duas saíram em 10/09/2026, com a trava acima.**

#### A área natural — a cobertura sai do nível

**Nem todo ataque em área vem de técnica.** *O sopro, o rugido, o chão que cede — são naturais, e não passam pelo Fundamento.* **A cobertura deles sai do nível, e é uma só por faixa; a forma é o jeito de gastar ela:**

| nível | cobre | `Esfera` | `Cone` | `Retângulo` — qualquer `A × B` que dê a cobertura |
|---|---|---|---|---|
| `2`–`8` | `13` quadrados | raio `3 m` | `7,5 m` | `4×3` · `6×2` · `7×2` · `12×1` |
| `9`–`16` | `28` quadrados | raio `4,5 m` | `10,5 m` | `6×5` · `7×4` · `9×3` · `13×2` |
| `17`–`24` | `50` quadrados | raio `6 m` | `15 m` | `7×7` · `8×6` · `9×5` · `10×5` |
| `25`–`30` | `113` quadrados | raio `9 m` | `22,5 m` | `11×11` · `11×10` · `12×9` |

*O quadrado é o da grade do §3.3, e o pior erro de arredondamento nas doze células é `12,5%`.*

> **Ela resolve como a área do Fundamento: Teste de Resistência contra a CD dele, o golpe da ação na falha e metade no sucesso.** *O `Cone` sai sempre do corpo dele, e a largura em qualquer ponto é igual à distância até ele; a `Esfera` e o `Retângulo` saem do corpo dele ou de um ponto no alcance.*

**Ela é de graça, pelo mesmo motivo do tamanho:** *o preço da área já foi fechado supondo que ela pega a mesa inteira, e a trava de uma ação em área por rodada é quem segura ela.* **E a trava conta por ESQUADRÃO:** *oito capangas fazem uma ação em área por rodada juntos, e os outros sete batem normal.*

> *Os raios são os quatro primeiros degraus da escada de esfera do manual, e crescem `9,00 ×` do nível 2 ao 30 — o mesmo crescimento dos dez dragões do D&D 2024, do Jovem ao Ancião. A cobertura, as formas e a resolução por Teste de Resistência saíram do projeto do Bestiário, que mediu cada uma, e a última foi martelada pelo Mizuki em 11/09/2026.*

#### As duas trocas ruins, declaradas e não proibidas

***Decisão do Mizuki:*** *"não tem problema não valer a pena, às vezes o combate tem uma pessoa só."* **As duas ficam medidas e liberadas, no molde do §4.7 — a peça mede, mostra, e o mestre escolhe.**

> **O inimigo que se cura empata em `315`, que é um terço da vida dele.** *Ele gasta a rodada e abre mão de `202` de dano — os `219` da linha com o fator da `Intervenção`; ganha `H` de vida, que alonga a luta em `H ÷ 315` rodadas, e cada rodada a mais entrega `202`.* **Então `H` de cura vale `0,64 × H` de dano**, e curar lasca é o mesmo erro que o grupo comete.
>
> **A condição que o inimigo põe num personagem empata quando `alvos × ações negadas = 4 × ações gastas`.** *A conta não depende do nível: o dano dele cai fora dos dois lados dela.* **Em alvo único nenhuma compensa** — *a `Pesada` precisa de `2,67` alvos, a `Média` precisa de `4` alvos, e a `Leve` precisa de `8` alvos, que a mesa não tem.*

**As duas são a mesma conta virada: gastar a rodada em algo que não é dano rende `0,64 ×` do que aquilo vale.** *A cura não tem como multiplicar — ela cai num corpo só. A condição tem, e é por isso que só ela tem saída.*

## 7. O que o `conferir-bestiario.py` confere

| # | o que ela confere |
|---|---|
| **1** | **as âncoras existem nos donos.** Cada número que a ficha usa aparece no documento que esta peça declara como dono, e a tabela do §3 é comparada com a lista do validador nos dois sentidos |
| **2** | **as três derivadas reconstroem.** A Defesa, o acerto e a CD saem das fórmulas da peça 1 §5, com a proteção andando junto do refino — e o resultado tem de bater com os `50%` a `55%` de acerto e os `35%` de falha que a peça 1 §6 publica |
| **3** | **a categoria é cópia com dono.** Vida e dano de cada uma reconstroem da linha do manual vezes o fator, e o fator reconstrói do número de personagens. *Desde a v0.221 o `Capanga` entra por outra porta: a vida dele é o dano do grupo dividido por quatro, para baixo. E a `3.3` confere o tamanho do §3.3: o alcance é o lado da grade vezes o quadrado* |
| **4** | **as ações são declaradas**, e a categoria de fator `1,00` bate com o piso que a peça 19 §2.2 publica. *Se aquele piso mudar, esta acende* |
| **5** | **o câmbio é medido, não guardado.** A simulação de fogo concentrado é rodada aqui dentro, com o `Capanga` derivado do dano do grupo e do dano do chefe, e o `8` publicado tem de ser o que ela devolve. *E o capanga que a tabela `Inimigos` do manual publica tem de ser esse mesmo — desde a v0.221, quando o capanga da `Alcateia` morreu* |
| **5.2** | **a linha do manual obedece a regra que a própria seção dele escreve.** O multiplicador e a duração saem da prosa da seção `Inimigos`, por extenso — *"cerca de três vezes o dano de rodada do grupo em vida, e é isso que faz a luta contra ele durar três rodadas"* —, e cada linha tem de ter o meio da faixa naquele múltiplo **e** cair naquele número de rodadas inteiras. *Ela nasceu na v0.206, e o que ela teria pego é o que ela pegou: a linha do nível 2 publicava `115` onde a regra pede `114`, e um ponto de vida punha o chefe vivo numa quarta rodada* |
| **5.1** | **a coluna da sub-categoria reconta.** As quatro formas do §4.5 são simuladas com os capangas abatidos primeiro, e as porcentagens publicadas têm de ser o que a simulação devolve — desde a v0.221 com uma casa decimal, e com o `Capanga` da escada. *Ela nasceu na v0.201 porque aquela coluna nunca teve validador e tinha divergido: o publicado subia de `28%` a `35%` e a simulação não reproduzia nem a ordem* |
| **6** | **o grau não vira número.** Nenhuma linha desta peça pode pendurar valor no grau, e o `ESTADO-ATUAL` e a peça 12 continuam dizendo que inimigo não tem grau mecânico |
| **7** | **nenhum valor de regra guardado aqui dentro.** Todo número vem do dono, e a checagem falha se algum sobrar como constante |
| **8** | **resistência é vida escondida.** Os pesos dos três grupos saem da peça 19 §4, os multiplicadores do §6.3 são recalculados de `1 ÷ (1 − o que se poupa)`, e a peça tem de declarar em que moeda a resistência se paga — desde a v0.221 o multiplicador do fator, e o declarado tem de ser o calculado. *Sem essa declaração ela é vida de graça, e a categoria passa a mentir sobre o encontro* |
| **9** | **o câmbio do §6.5, nas três portas.** A `9.1` reconstrói as `35` células do orçamento de feitiço do golpe dividido pelo que um ponto vale, com o fator de quem carrega `Intervenção`, e cobra que o `seco` seja o piso da `Classe 1` do manual; a `9.2` reconstrói a conta da aptidão do custo que a peça 11 §6.5 publica, da maior Classe da peça 18 e do câmbio de PE da peça 5 §4; a `9.3` refaz os dois empates — o da cura e o dos alvos —, com a escada de ações lida da peça 19 e o tamanho do grupo lido da categoria de fator `1,00`; e a `9.4` cobra que cada porta declare a moeda. *Nenhum dos quatro números vive aqui dentro.* **Desde a v0.221, a `9.5` confere as seis prontas do gerador contra a escada, e a `9.6` a área natural contra a escada de esfera do manual** |

### 7.1 As quarenta e duas perturbações, em cópia isolada

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
| **9.1** | uma célula do orçamento do §6.5 vira `99,9` | acende | acende |
| **9.1** | a célula `seco` do nível 5 vira número | acende | acende |
| **9.1** | o ponto de feitiço vira `6,0` na peça 19 | acende | acende |
| **9.1** | o preço da `Classe 1` vira `8` na peça 19 | acende | acende |
| **9.2** | o câmbio de PE vira `7,00` na peça 5 | acende | acende |
| **9.2** | a `Extensão de Domínio` vira `2 ×` na peça 11 | acende | acende |
| **9.2** | uma porcentagem do §6.5 vira `50%` | acende | acende |
| **9.3** | o empate da cura vira `400` | acende | acende |
| **9.3** | a conta de alvos da `Média` vira `6` | acende | acende |
| **9.3** | a escada de ações negadas muda na peça 19 | acende | acende |
| **9.4** | uma porta troca a moeda por *"o mestre decide"* | acende | acende |
| **9.4** | a linha inteira de uma porta é apagada | acende | acende |
| **9.1** | **contra-teste:** mexer em prosa sem mexer em número | fica verde | fica verde |
| **9.1** | **contra-teste:** o piso cai para `2` pontos na peça 19 **e** o nível 5 enche no §6.5 | fica verde | fica verde |
| **9.2** | **contra-teste:** a `Extensão` vai a `2 ×` na peça 11 **e** as duas porcentagens no §6.5 | fica verde | fica verde |
| **9.3** | **contra-teste:** a `Leve` vira uma ação na peça 19 **e** os alvos dela no §6.5 | fica verde | fica verde |
| **5.2** | a vida do nível 2 volta para `105 a 125` no manual | acende | acende |
| **5.2** | a vida do nível 30 vira `870 a 1120` no manual | acende | acende |
| **5.2** | a prosa do manual passa a dizer `quatro vezes` | acende | acende |
| **5.2** | a prosa do manual promete `quatro rodadas` | acende | acende |
| **5** | a peça volta a declarar em PROSA que uma faixa não tem capanga | acende | acende |
| **5** | **contra-teste:** a mesma frase, só dentro de linha de tabela | fica verde | fica verde |
| **5.2** | **contra-teste:** as pontas da faixa do nível 30 mudam e o meio fica `945` | fica verde | fica verde |
| **5.2** | **contra-teste:** as pontas da faixa do nível 2 mudam e o meio fica `114` | fica verde | fica verde |

> **O contra-teste da `3` é o que prova a checagem.** *Trocar a `Calamidade` para oito personagens muda o fator para `2,00`, as ações para `7` e as três células de ficha — e a checagem sai verde,* **porque ela mede a derivação e não os números publicados.**
>
> **⚠ E a guarda da `5` nasceu larga demais, achada pelo próprio arnês.** *Ela procurava a frase no texto inteiro, e a linha do §7.1 que **descreve** a perturbação contém a frase* — **a guarda leu a descrição como se fosse a declaração.** *Hoje ela procura fora de tabela, e o par de testes que prova isso é a mesma frase acendendo em prosa e ficando verde numa célula.*
>
> **⚠ E as duas últimas são as que provam a `5.2`, e a primeira tentativa delas foi mal mirada.** *Eu tinha escrito o contra-teste como "muda a prosa para `quatro vezes` E a tabela junto", e ele não fica verde:* **mexer na vida do chefe no manual acende as checagens `3`, `5`, `5.1` e `9.3` de uma vez**, porque a peça pendura doze células naquele número. *Um contra-teste coerente ali teria de mover uma dúzia de valores, e aí ele não estaria testando a `5.2`.* **O que testa é mexer nas PONTAS da faixa mantendo o meio** — a `5.2` lê o meio, então ela fica verde.
>
> **⚠ E a terceira perturbação achou um defeito na checagem `2` antes de ela valer.** *A tabela da peça 1 §6 amostra os níveis de marco, que são os **picos** da curva de acerto — ela publica `55%` em todas as colunas.* **Medir a banda só por ela dava um ponto só, e o inimigo, amostrado em níveis que não são marco, caía fora dela sem nada estar errado.** *O vale não está na tabela: ele está declarado ao lado, como oscilação irredutível de `5pp`.* **Hoje a checagem lê os dois — o pico da tabela e a oscilação declarada — e a banda sai `50%` a `55%`.**

### 7.2 As dezessete perturbações da v0.221, na escada viva

*Mesmo método: cópia isolada, base conferida antes — com o único vermelho declarado, a checagem `5` acusando o capanga morto na tabela do manual até o manual mudar —, o `diff` conferido, e o veredito lido da checagem que estava sendo testada.*

| checagem | perturbação | esperado | deu |
|---|---|---|---|
| **3** | a vida do `Capanga` no §4.1 vira `33` | acende | acende |
| **3** | o fator da `Calamidade` vira `2,10` | acende | acende |
| **4** | o `Desastre` publica `4` ações | acende | acende |
| **4** | a `Catástrofe` publica `0` ações | acende | acende |
| **5** | a peça publica o câmbio em `sete` | acende | acende |
| **5** | a derivação da vida do capanga some | acende | acende |
| **5.1** | o `com dois` passa a cobrar `67,9%` | acende | acende |
| **5.1** | o chefe do `com um apoio` fica com `92,0%` | acende | acende |
| **7.1** | a `Catástrofe` com Expansão vira `12,0` | acende | acende |
| **8** | resistir aos `Físicos` vira `1,60` | acende | acende |
| **8** | a peça para de declarar a moeda | acende | acende |
| **9.1** | o `Desastre` do nível 20 vira `11,1` | acende | acende |
| **9.1** | o fator da `Intervenção` vira `0,950` | acende | acende |
| **9.2** | **contra-prova:** o `Desastre` volta aos `16%` da cota sem o fator | acende | acende |
| **9.4** | uma porta troca a moeda por *"o mestre decide"* | acende | acende |
| **\*** | **contra-teste:** mexer em prosa sem mexer em número | fica verde | fica verde |
| **\*** | **contra-teste:** a `Calamidade` vira `10` pessoas, coerente nas três tabelas que dependem dela | fica verde | fica verde |

> **A contra-prova da `9.2` é a que prova o fator.** *Com a cota crua, `16%` era o número certo; com a `Intervenção`, ele acende.* **Se a checagem não aplicasse o fator, a perturbação saía verde.**
>
> **⚠ E o último contra-teste saiu VERMELHO na primeira rodada, pelo motivo certo.** *Eu tinha montado a `Calamidade` de dez pessoas com dano `188` no nível 10 — `75 × 2,50` dá `187,5`, e o meio para baixo põe em `187` —, e tinha deixado o nível 5 em `seco`, que com fator `2,50` já monta `3,4` pontos.* **A checagem acusou as quatro células, e o erro era da perturbação.** *Refeita com cada número calculado pela regra da peça, ela fica verde.*

## 8. Em aberto

- ~~**⚠⚠ A pressão do chefe é `3,3 ×` menor que a do d20.**~~ ***FECHADA na v0.201***, com a tabela `Inimigos` refeita e o manual na `v7.23`. **O chefe entrega `90%` da vida de um personagem por rodada e tem `3 ×` o dano de rodada do grupo em vida** — `22,5%` do grupo por rodada, luta de `3` rodadas, e ele derruba `2,70` pessoas se concentrar.

  > **A metade que faltava foi achada onde o livro não diz, mas mostra.** *O `Guia do Mestre` manda tirar a média do dano de um monstro "para as três primeiras rodadas de combate", e essa é a única duração que ele declara.* **Daí sai a saída do grupo: a vida do chefe dividida por três.** *Conferida por um segundo caminho que não conversa com ela — um Guerreiro e um Ladino do Livro do Jogador de 2024, sem magia nenhuma, já entregam metade disso em todo nível.*
  >
  > **⚠ E o `3,3 ×` estava alto.** *Ele saiu de ler o TOPO da faixa de dano do d20 contra o valor único daqui.* **Meio contra meio a diferença era `2,6 ×` a `3,0 ×`**, e a tabela nova é `3,04 ×` no nível 30.
  >
  > **A régua de condição não foi repreçada, e isso é decisão do Mizuki:** *"tem que considerar que o boss também vai poder aplicar condições, troca como a régua mede."* **A peça 19 §2.2 passou a perguntar outra coisa, e as treze passam sem mexer em preço nenhum.**

- ~~**A coluna de capanga da Classe 1, que a v0.199 deixou vazia por uma razão que morreu.**~~ ***FECHADA na v0.206, e o corpo que saiu não é o que este item previa:*** **`28` de vida e `6` de dano, e não os `29` escritos aqui.** *Para abrir a coluna foi preciso consertar a linha do nível 2 antes — ela publicava `115` de vida onde a regra das três vezes da própria seção pede `114`, e um ponto punha o chefe vivo numa quarta rodada.* **Quatro capangas cobram `71%` da vida do grupo contra os `67%` do chefe sozinho.**

  > **⚠ Este item ficou seis versões dizendo `29` depois de a coluna sair com `28`.** *A conta que produziu o `29` foi feita contra a tabela da v0.199; a da v0.201 mudou o chão dela e ninguém voltou aqui.* **É a lição nº 9 dentro da própria lista de pendências — o número de uma previsão não riscada envelhece igual ao de uma regra.**

- ~~**⚠⚠ O CATÁLOGO DE TRAÇOS, e ele é o próximo trabalho desta peça.**~~ ***FECHADO na v0.205, e não virou catálogo:*** **o §6.5 é o câmbio do catálogo do JOGADOR para a ficha do inimigo**, por decisão do Mizuki — *"dá pra deixar ser que nem do sistema pra player, mas rebalancear"*. *Três portas: a técnica paga no orçamento de feitiço da ação, a aptidão paga na cota nas rodadas em que está ligada, e o que dá vida efetiva paga em degrau.* **A ação fora do turno saiu de graça com número — `0,94 ×` a `1,07 ×` sobre `81` durações de luta —, e a condição do inimigo se resolveu sem moeda nova, porque o Fundamento já cobra por ela em ponto de feitiço.**

  ***Levantado pelo Mizuki:*** *"não é bom ele ter justamente PE para ter recursos? Mago inimigo em D&D tem spell slot, técnica máxima como possibilidade, habilidade com recarga. Usar a ficha de D&D como base é o que mais vai ajudar esse sistema de inimigos ficar legal."*

  > **A pesquisa no `Guia do Mestre` responde os dois lados, e o §6.1 sobrevive.** *O passo 13 de "Criando o Bloco de Estatísticas" escreve, entre parênteses: **"as características não mudam realmente as estatísticas do monstro"** — elas mexem na vida efetiva, no dano efetivo ou na CA efetiva, e é assim que entram no Nível de Desafio.* **Espaço de magia num bloco de conjurador é FORMA e não orçamento: o Guia manda contar a magia pelo dano dela.**
  >
  > ***E a escada de categoria desta peça JÁ É essa máquina.*** *O §6.3 converte resistência em degrau e o §6.4 converte a Expansão em dobro de categoria — os dois são o passo 13, com outro nome.* **O que falta não é a máquina: é o CATÁLOGO, e ele tem duas entradas.**
  >
  > **A entrada que o Mizuki está pedindo é a habilidade que não sai toda rodada, e ela é de graça nesta régua.** *Uma habilidade guardada não muda a cota: ela muda a rodada em que o grupo apanha.* **Numa luta de três rodadas, uma habilidade que entrega o dobro de uma rodada deixa as outras duas em `110` cada, e o total continua sendo `657`.** *É o mesmo fenômeno do §4.4 e do §4.5 — mesmo tamanho, forma diferente.*
  >
  > **⚠ A recarga `5-6` do d20 NÃO cabe aqui, e a conta diz por quê:** *numa luta de três rodadas ela dispara `1,67` vezes, e a cota não paga isso.* **Lá ela cabe porque a economia de rodadas é outra.** *O relógio que cabe é `1 ×` por luta, e ele fica para o §6.5 medir junto das outras.*

  > ***E recusar um Teste de Resistência ficou de fora, por decisão do Mizuki na v0.205:*** *"o inimigo não vai ter Resistência Lendária, então ele não anula condições, ele precisa passar no teste."* **É a mesma decisão que a v0.199 já tinha fechado, e a medida nova não a moveu:** *uma recusa vale `1,17 ×` a `1,20 ×` de dano efetivo, contra `1,18 ×` que resistir aos `Elementais` vale — meio degrau.* **O preço existia; a porta é que não.**

- ~~**⚠ O inimigo que se cura, e a conta dele já existe.**~~ ***FECHADO na v0.205, no §6.5***, junto da condição que ele põe num personagem — *as duas são troca ruim, as duas ficam declaradas e liberadas, e as duas só viram lucro em área.* ***Pergunta do Mizuki:*** *"como fica inimigo que quer se curar? Quer usar técnica?"*

  > **É a mesma conta que a v0.203 fez do lado do grupo, virada.** *Ele gasta a rodada e abre mão de `219` de dano; ganha `H` de vida, que alonga a luta em `H ÷ 315` rodadas, e cada rodada a mais entrega `219`.* **Então `H` de cura vale `0,70 × H` de dano, e o empate está em curar `315` — um TERÇO da vida máxima dele.**
  >
  > **Cura de lasca em inimigo é o mesmo erro que o grupo comete.** *Curar `219` — quase um quarto da vida dele — rende `152` contra os `219` que ele largou.* **Só vale se ele repuser um terço de si mesmo numa rodada**, e isso é exatamente o tamanho que a obra dá para a energia reversa de quem é bom nela.
  >
  > *A régua está escrita; o que falta é a entrada do catálogo dizendo em que moeda ela se paga — e isso é o §6.5.*

- ~~**As maldições prontas.**~~ ***FECHADAS na v0.214, e remapeadas na v0.221.*** **Seis, do nível 2 ao 12, na escada viva:** *`Betobeto`, `Kamaitachi` — duas na mesa —, `Hitotsume` e `Kitsune` são `Ameaça`; `Tsuchigumo` e `Oni` são `Desastre`, com três `Intervenções` cada.* **A coluna do `Capanga` ficou vazia, e é o preço declarado da decisão de 10/09:** *a `Kitsune` subiu de faixa para poder conjurar, e a grade de duas faixas por três categorias deixou de fechar. Fichas de esquadrão são ficção do Mizuki, e ficam para quando ele quiser.* **As escolhas moram no `dados.js` e os números são computados**, e o bloco sai no molde de bloco do 5e, igual ao do livro do Bestiário. *A v0.213 tentou publicá-las num `.md` à parte e quatro dos seis golpes saíram errados, por um arredondamento que o gerador faz e a cópia não fazia.*
- ~~**A Expansão de Domínio de inimigo.**~~ ***FECHADA na v0.204, e refeita na v0.221:*** **ela multiplica o fator por `1,92`**, porque o Acerto garantido multiplica a saída efetiva por `1,92 ×`. *A primeira forma cobrava em degrau de categoria e só cabia em duas das quatro categorias da escada de então; a moeda passou a ser o fator, e ela cabe em qualquer uma.*
- **O inimigo com Trilha.** *Fica de fora por decisão, e o motivo está no §6* — mas um antagonista recorrente que sobe junto com o grupo é caso de mesa que vai aparecer.
- ~~**A ficha impressa.**~~ ***FECHADA na v0.199, e três números dela envelheceram até a v0.206:*** *a coluna `cobra do grupo` da sub-categoria ficou nos `28/30/33/35` da v0.199 enquanto esta peça publicava `68/58/56/62` desde a v0.201, a nota ao lado dizia que repartir o encontro o encarece — a v0.201 mediu o contrário —, e a razão de quatro `Ronda` estava em `0,62 ×` contra os `0,75 ×` a `0,77 ×` do §4.3.* **Os três moravam inline no montador do `gerador-inimigo/`, que é o único lugar do subsistema que nenhuma checagem lia** — *o `dados.js` tem validador desde a v0.199 e o montador não tinha.* *Hoje a porcentagem e a razão vivem no `dados.js` e o bloco `7` do `conferir-ficha.py` compara as duas com esta peça, com uma guarda que acende se o montador voltar a guardar inline.* **`05-material/bloco-de-inimigo.docx`**, quatro páginas — as tabelas que o mestre copia, o bloco em branco com as dezessete linhas, e um exemplo preenchido. *O gerador é o `gerador-inimigo/`, e o bloco `7` do `conferir-ficha.py` compara o `dados.js` dele com esta peça.*

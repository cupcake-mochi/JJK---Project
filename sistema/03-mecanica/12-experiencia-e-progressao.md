# EXPERIÊNCIA E PROGRESSÃO

**Fase 4, décima segunda peça.** Como se sobe de nível numa guilda onde sete mestres postam missão e ninguém coordena calendário.

Versão v0.196 — 31/08/2026 · Validador: `conferir-xp.py` · *a curva foi represada na v0.196; o resto é de v0.32*

Esta é a **trava nº 1 de mundo compartilhado** — *"XP tabelado, nunca marco narrativo"* —, e ela ficou aberta por trinta versões. Sem ela, cinco mestres dão progressão diferente, que é exatamente o problema que o sistema existe para resolver.

Ela também é a primeira peça deste projeto escrita a partir de **dado de gente real**: catorze opiniões da Guilda sobre quanto tempo a subida deve levar. O que não muda o fato de tudo aqui continuar sendo previsão até alguém jogar — mas a previsão agora tem de onde sair.

> **O levantamento inteiro está em `01-pesquisa/levantamento-ritmo-de-progressao.md`**, com as catorze respostas como vieram, a mediana medida e o glossário do *gap*. Quando o playtest contradisser algum número daqui, é lá que se confere o que foi perguntado e quem respondeu o quê.

---

## 1. A regra, em cinco linhas

> **Cada nível custa um número inteiro de missões: duas no nível 2, três nos dois seguintes, e daí duas a mais a cada três níveis, até parar em dezessete.**
> **Uma missão padrão paga 100 XP, e paga o mesmo para todo mundo na mesa.**
> **Nenhuma missão faz você subir mais de um nível — o que sobra fica acumulado.**
> **Por semana, as duas primeiras missões pagam cheio; da terceira em diante o valor cai pela metade a cada uma.**
> **Do nível 20 para o 21 o XP não basta: é preciso um feito.**

O resto desta peça é o porquê de cada uma das cinco.

## 2. Por que o XP é fixo, e não escalado pelo desafio

É a decisão que mais separa este sistema de um de campanha fechada, e ela vem de uma propriedade que só uma guilda precisa.

**Numa guilda, mesa aberta junta níveis diferentes.** Um nível 8 e um nível 14 na mesma missão não é exceção: é terça-feira. E aí a pergunta é o que acontece com quem ficou para trás.

Dois personagens começam juntos. Um perde dez sessões — viagem, prova, sumiço. Depois disso jogam tudo junto, e o buraco fica em **1.000 XP para sempre**, porque ninguém mais perde nada.

**A pergunta não é quanto XP falta, e sim quanto esses 1.000 XP VALEM.** *É uma dívida em moeda que se desvaloriza: a mesma quantia compra menos nível a cada faixa que a campanha atravessa.*

| quando quem ficou tem | os 1.000 XP perdidos valem | numa curva plana valeriam |
|---|---|---|
| 2.000 XP | **2,00 níveis** | 0,91 |
| 5.000 XP | **1,24** | 0,91 |
| 9.000 XP | **0,91** | 0,91 |
| 13.000 XP | **0,77** | 0,91 |
| 18.000 XP | **0,67** | 0,91 |
| 23.000 XP | **0,59** | 0,91 |

**A coluna da direita é o contra-teste, e ela é o que prova que quem fecha o abismo é a curva subir.** *Uma curva plana de mesmo custo total deixa a dívida valendo `0,91` nível do começo ao fim* — o atrasado nunca encosta, por mais que a campanha ande. **Nenhuma regra faz esse trabalho, e nenhuma precisa: quem está atrás sobe mais rápido porque o nível dele é mais barato.**

**Com XP escalado pelo nível acontece o contrário, e o buraco CRESCE.** *Quem está atrás ganha menos por missão justamente por estar atrás, então a dívida de `1.000` XP vira `1.188` na missão 60 e `3.238` na 140.* **A distância só fecha quando alguém encosta no teto do nível 30, e até lá ela não se move sozinha.**

E isso tem nome na Guilda: é o **gap** que o Kekka descreveu — *"final da mansão tiveram players literalmente bloqueados de ganhar gap de tão mutantes que eram"*. Um personagem que se descola tanto que não cabe mais em mesa nenhuma.

### O que os jogadores queriam não era isso

A proposta que apareceu no levantamento foi *"inimigo de grau mais alto dá mais XP, como em D&D"*. A intuição está certa — **missão difícil deve valer mais** —, mas endereçada ao alvo errado.

**Missão difícil já vale mais, pelo tamanho dela** (seção 4). O que não pode é o valor depender do *nível de quem recebe*, porque é isso que congela a distância entre as fichas.

### E "Grau dá mais XP" bate numa decisão de arquitetura

O `arquitetura.md` separou os dois eixos de propósito:

> *"Todo personagem começa Grau 4, e a patente sobe por **feito**."*
> *"O Yuta é Grau especial, Nível baixo: a instituição o classificou no topo."*

**Grau é reconhecimento; nível é poder.** Se o Grau passar a dar XP, ele vira nível com outro nome — e pior, vira espiral fechada: sobe de patente, sobe de nível mais rápido, ganha patente por feito, sobe de novo.

O Grau continua valendo muito. Ele só não vale **XP**.

## 3. A curva

> **Um nível custa um número inteiro de missões padrão. A base é três, o número sobe duas a cada três níveis, e ele para em dezessete.**

| níveis | custa | em XP |
|---|---|---|
| **2** | 2 missões | 200 |
| **3 a 4** | 3 missões | 300 |
| **5 a 7** | 5 missões | 500 |
| **8 a 10** | 7 missões | 700 |
| **11 a 13** | 9 missões | 900 |
| **14 a 16** | 11 missões | 1.100 |
| **17 a 19** | 13 missões | 1.300 |
| **20 a 22** | 15 missões | 1.500 |
| **23 a 29** | 17 missões | 1.700 |

**Chegar ao nível 20 custa `143` missões padrão, e ir dali ao 30 custa `164`** — `14.300` e `16.400` de XP, `307` missões na campanha inteira.

### 3.0 De onde sai cada número da curva

*Escrita na v0.196.* **São cinco números, e cada um responde a uma coisa diferente.**

**A base é `3` missões, e ela é o piso do relógio.** *Com base `2` o nível 20 chega em `13,7` meses a duas mesas por semana, e com base `4` em `17,4`.* **Com `3` ele chega em `15,5`**, que é o alvo desta versão.

**O passo é `+2` missões a cada `3` níveis, e esse par é o que segura a razão da faixa lendária.** *Passo de `+1` a cada três põe o nível 20 em `10,7` meses; passo de `+3` põe em `20,1`* — **mas o de `+3` derruba a razão para `0,41`, fora dos `0,45` a `0,61` que o levantamento produziu.** *O de `+2` fica em `0,51`.*

> ***⚠ E o intervalo de três níveis não é decorativo.*** *Com o mesmo passo de `+2` a cada **dois** níveis, a curva vai para `193` missões e `21,0` meses, e a razão despenca para `0,39` — fora da faixa.* **A cada quatro níveis ela cai para `12,7` meses.** *Só o intervalo de três entrega relógio e razão ao mesmo tempo.*

**O teto é `17` e ele continua sendo o único número que não sai de fórmula nenhuma.** *Sem ele o nível 29 custaria `21` missões, e o número cresceria enquanto houvesse nível* — o que tira do jogador a coisa que o custo inteiro existe para dar, que é saber de cabeça quanto falta.

**O que ele compra em número é pouco, e o pouco fica escrito.** *Ele tira `10` missões da faixa lendária — `164` em vez de `174` —, o que move o topo de `8,4` para `7,9` meses e a razão de `0,54` para `0,51`.* **Ele não resgata nada de fora da faixa, porque sem ele já estava dentro.**

**E o nível 2 custa `2` em vez de `3`, que é concessão declarada.** *Ela tira **uma** missão do total e move o nível 20 em `0,11` mês — quase nada.* **O que ela compra é o degrau que decide se alguém fica: com `3`, uma ficha nova joga três mesas antes de a ficha mudar de forma; com `2`, ela sobe na segunda.**

> ***⚠ A curva anterior morreu por medida, e não por gosto.*** *Ela custava `63` missões até o nível 20 e `145` até o 30, e a duas mesas por semana entregava o nível 20 em `6,8` meses.* **A mediana que as catorze respostas pediram é `10,25`, e a resposta mais lenta de todas foi `14`** — então a curva de hoje, sozinha, passa da faixa inteira, em `15,5`.
>
> *O repreço foi medido em duas etapas dentro desta mesma versão: a primeira fechou em `125` missões e `13,6` meses, e o Mizuki esticou de novo depois de ler a tabela por cadência.* **A primeira parava dentro da faixa; esta sai dela de propósito.** *O levantamento que mediu as duas está no `99-arquivo/`, com o cabeçalho de sempre.*
>
> ***E isso é o desenho, não um acidente.*** *Palavras dele:* *"vamos chutar alto, pq assim os servidores que forem usar vão poder compensar esses fatores com outros meios."* **A curva crua é o piso; o §5.3 mede o que cada mecanismo de compensação devolve, e uma única mesa de dobro por mês já traz o nível 20 de volta para `13,9`.**
>
> **O argumento que sustenta a direção é o mesmo das duas vezes:** *uma campanha lenta demais o servidor corrige na semana seguinte, declarando missão maior ou marcando um evento de dobro — as duas coisas são dele, pelo §4 e pelo §5.3. Uma campanha rápida demais deixa fichas de nível 16 na mesa, e ninguém desce de nível.*

**Custo inteiro é a lição do jogo organizado, e não invenção nossa.** Os dois maiores sistemas de campanha compartilhada do mundo convergem nisso:

| | como conta |
|---|---|
| **D&D Adventurers League** (~100 mil membros) | 4 checkpoints por nível até o 4, 8 dali em diante — e 1 checkpoint por hora jogada |
| **Pathfinder Society 2e** | 12 XP por nível, cenário paga 4: **três cenários por nível**, sempre |

O que os dois compram é a mesma coisa: **um jogador sabe de cabeça quanto falta.** *"Estou no nível 12, cada nível são oito missões, joguei duas."* Sem tabela, sem conta.

**Uma versão anterior desta peça usava uma reta** — `100 + 30 × (nível − 2)` —, e ela produzia 1,3 missão no nível 3, 1,6 no 4, 2,8 no 8. Todo nível pedia conta, e nenhum caía redondo.

**Os primeiros níveis continuam passando mais rápido, e agora por pouco.** *Do 2 ao 5 são duas, três e quatro missões; do 24 em diante são catorze.* **A ficha ganha corpo antes de qualquer decisão pesada**, e do 16 para cima cada nível vira coisa de arco.

### E a nossa é MUITO mais achatada que a do D&D, de propósito

**No `Player's Handbook` de 2024 o nível 19 custa `83×` o que custa o nível 2.** *Na nossa ele custa `7×`, e na curva anterior custava `10×`.* **A metade de cima do PHB pesa `3,19×` a de baixo; a nossa pesa `1,98×`.**

**Uma curva íngreme alcança melhor, e a conta diz quanto:** *a mesma dívida de dez missões perdidas encolhe `13,2×` ao longo de uma campanha de PHB e `3,0×` na nossa.* **É a mesma peça que o `DMG` p.92 descreve** — *quem está em nível mais baixo recebe cota igual e sobe mais rápido* —, só que lá ela é bem mais forte.

> **E não dá para copiar a inclinação de lá, porque ela briga com a coisa que esta peça existe para entregar.** *O preço aqui se lê em missões, e é isso que faz sete mestres pagarem igual sem combinar.* **A `83×` do PHB, com base de duas missões, poria o nível 29 em `166` missões** — uma temporada inteira por nível, e ninguém consegue dizer de cabeça quanto falta.
>
> ***O repreço quase não mexeu nisso, e vale registrar:*** *a razão entre topo e base caiu de `10×` para `7×`, e mesmo assim o alcance medido ficou parado* — `2,9×` na curva velha contra `3,0×` na nova. **Encarecer tudo não enfraqueceu o motor que fecha o abismo.**

## 3.1. Nenhuma missão dá mais de um nível

> **Você sobe no máximo um nível por missão. O XP que sobrar fica acumulado e sai na próxima.**

**Este é o defeito que derrubou o XP na maior campanha compartilhada do mundo.** A Adventurers League abandonou experiência na temporada 8, em 2018, e o motivo está escrito: *"uma aventura de quatro horas levava um personagem novo do nível 1 ao 3 — mais rápido do que os designers pretendiam."*

Na curva anterior a pior combinação entregava **três níveis de uma vez**: um final de arco jogado por um personagem de nível 2. Não é injusto — o XP é o XP —, mas é decisão de ficha demais para uma sessão só, e o que a pessoa monta apressada ela joga mal por semanas.

| no nível | curta | padrão | longa | final de arco |
|---|---|---|---|---|
| 2 | +50 | +100 | **1 nível** | 1 nível, +100 |
| 3 e 4 | +50 | +100 | +200 | **1 nível** |
| 5 e acima | +50 | +100 | +200 | +300 |

***⚠ E na curva de hoje o teto DEIXOU DE MORDER, o que é consequência do repreço e fica registrado.*** *Nenhuma combinação de nível e tamanho entrega dois níveis:* **o melhor caso é um final de arco no nível 2, que dá um nível e deixa `100` de troco** — e o nível 3 custa `300`, que é o valor cheio de um final de arco. *Na curva anterior o mesmo caso dava três.*

**Ele fica, e o motivo não é sentimental.** *A regra que está escrita ali é dupla: o teto de um nível, e **o excedente que não some**.* **A segunda metade continua trabalhando toda semana** — quem leva um final de arco no nível 2 entra na missão seguinte com `100` XP no bolso, e esses `100` são um terço do próximo nível.

> **A primeira metade vira rede de segurança, e rede de segurança se mede pelo que ela pega quando alguém cai.** *Um servidor que resolva pagar `600` numa missão de fecho de temporada volta a ter o caso de dois níveis na hora* — e a regra já está no lugar, sem precisar de emenda no meio da campanha.

## 4. O tamanho da missão

Uma curva só, e quem varia é a missão.

| tamanho | paga | o que é |
|---|---|---|
| **curta** | 50 | uma cena, um interrogatório, roleplay puro, uma escolta sem incidente |
| **padrão** | 100 | a missão de uma sessão: sai, resolve, volta |
| **longa** | 200 | duas ou mais sessões, ou uma sessão que virou noite |
| **final de arco** | 300 | o fecho de uma linha de missões, ou o que a mesa vai lembrar por meses |

**Quem declara o tamanho é quem posta a missão, e ele declara antes.** Isso não é detalhe de administração: é o que impede o tamanho de ser decidido depois em função de como a mesa correu.

**Missão de roleplay que qualquer Grau pode entrar é missão curta**, e ela paga. Uma guilda que só dá XP para quem mata perde metade do que faz uma guilda ser guilda.

### 4.1 A mistura de cada faixa, e ela é o número mais perigoso desta peça

*Escrita na v0.196.* **A curva é uma só, e quem varia é a missão — então a missão típica de cada faixa é o que converte preço em relógio.** *Ela nunca esteve derivada aqui, e a §4 chegou a descrever uma mistura que não batia com a que a conta usava.*

> **Missão mundana típica: a cada oito, uma curta e uma longa, e as outras seis padrão.** `(50 + 600 + 200) ÷ 8` = **`106,25` XP**.
>
> **Missão lendária típica: a cada cinco, três longas e dois finais de arco.** `(600 + 600) ÷ 5` = **`240` XP**.

**A curta e a longa quase se anulam, e é isso que põe a mundana perto da padrão.** *Uma curta a menos e uma longa a mais valem `250` contra os `200` de duas padrão* — seis por cento acima, e nada mais.

***⚠ E aqui mora a armadilha que já mordeu duas vezes.*** **A "mesa" da tabela do §3 é a missão PADRÃO, de `100` XP — a unidade de preço.** *A missão típica de `106,25` é a unidade de relógio.* **Dividir `143` mesas pela cadência dá o número errado**, porque `143` já está em moeda de `100` e o relógio corre em moeda de `106,25`.

### E é isso que faz a faixa lendária ser mais rápida em tempo

Do nível 20 em diante a Guilda roda final de arco e side story — missões grandes. A curva continua subindo, mas o pagamento sobe junto:

| faixa | custa | XP total | missão típica | dá em missões |
|---|---|---|---|---|
| 2 → 20 | 143 mesas | 14.300 | `106,25` | ~135 |
| 20 → 30 | 164 mesas | **16.400** | `240` | ~68 |

Dez níveis lendários custam **mais missões padrão** que dezoito mundanos — 164 contra 143 — e mesmo assim levam **metade das missões de verdade**. Foi o que catorze pessoas pediram de jeitos diferentes, e ele sai sem nenhuma regra de exceção.

> ***A faixa lendária não é rápida por causa da curva, e isto precisa ficar escrito.*** *Se o topo rodasse missão mundana, ele levaria `17,8` meses a duas mesas por semana em vez de `7,9`* — **`2,3×` mais devagar do que é hoje, e mais tempo do que os `15,5` da faixa de baixo inteira.** *Em missões dá `154` contra `135`.* **Quem modelar a campanha inteira a `100` XP por missão chega à conclusão contrária, e ela é falsa.**

## 5. As duas primeiras da semana pagam cheio

> **Na sua semana, a primeira e a segunda missão pagam o valor cheio. A terceira paga metade, a quarta metade disso, e assim por diante. A contagem zera na virada da semana.**

| missão da semana | paga |
|---|---|
| 1ª e 2ª | 100% |
| 3ª | 50% |
| 4ª | 25% |
| 5ª | 12% |
| 6ª | 6% |

**Ninguém sai com zero, e isso é a razão de ser retorno decrescente em vez de teto.** Um teto duro produziria a mesa em que você jogou seis horas e não levou nada — e aí a regra vira motivo de briga em vez de ritmo.

**O que ele resolve.** O levantamento trouxe o sintoma pronto, do Mega: *"muita gente só mestra pelo XP e isso vira cúmulo."* Quando a terceira mesa da semana vale metade, moer mesa para de compensar sozinho — sem proibir nada e sem ninguém precisar fiscalizar.

**E ele é o que achata a ponta de cima:**

| você joga | equivale a | chega ao 20 em | e ao 30 em |
|---|---|---|---|
| 1 a cada 15 dias | 0,50 | 62,2 meses | 93,7 |
| 1 por semana | 1,00 | 31,1 | 46,9 |
| **2 por semana** | 2,00 | **15,5** | **23,4** |
| 3 por semana | 2,50 | 12,4 | 18,7 |
| 4 por semana | 2,75 | 11,3 | 17,0 |

**Sem o retorno decrescente, quem joga quatro vezes por semana chegaria ao nível 20 em `7,8` meses em vez de `11,3`** — e aí acontece o que o Zeuk temia: *"30 nego lvl 16 em 4 meses"*. **Repare que dobrar de duas para quatro por semana compra `4,2` meses, e não a metade do tempo.**

### 5.1 O que a Guilda pediu, e onde a curva cai

**As catorze respostas do levantamento desenham uma faixa, e não um ponto:** *`3` meses no mínimo, `10,25` na mediana, `14` no máximo, para ir do nível 2 ao 20.*

**A cadência que essas respostas supunham está escrita lá, e é `1` a `2` mesas por semana.** *É o que o Sui chama de "constância, mas não de forma viciada", e é o que o Mahi descreve como "toda semana, uma vez ou duas".*

***⚠ A curva crua fica FORA dessa faixa, e isso é decisão declarada.*** *Na ponta de cima da cadência ela entrega `15,5` meses contra o teto de `14`, e na ponta de baixo `31,1`.* **É o "chutar alto" do Mizuki**, e o §5.3 é a outra metade da decisão: *uma única mesa de dobro por mês devolve o nível 20 para `13,9`, dentro da faixa.*

> **A regra do sistema é a curva crua; o ritmo que a mesa sente é a curva mais o que o servidor faz com ela.** *Os dois números ficam publicados lado a lado de propósito, porque um servidor que não use mecanismo nenhum precisa saber o que está escolhendo.*

**A mediana de `10,25` fica fora nas duas leituras, e a distância está medida:** *a curva crua erra em `+5,3` meses, e com um dobro por mês em `+3,7`.* *A razão da faixa lendária, que é a única coisa em que as catorze concordaram, passa nas duas.*

### 5.2 O vão entre quem joga uma e quem joga duas, e ele fica SEM regra

***Decisão do Mizuki, na v0.195:*** **nenhum gatilho de recuperação entra na regra.** *Palavras dele:* *"não é ideal o livro obrigar formas de outros players receberem mais XP — apenas auxiliar e sugerir."*

**É a régua de voz do livro aplicada:** *quanto se compensa quem joga menos é economia de guilda, e duas guildas podem responder isso diferente e as duas estarem certas.* **O livro mede, mostra o tamanho e sugere; o servidor decide.**

**A coluna é o mês em que você CHEGA àquele nível, contando do nível 2, e a curva está crua — sem mecanismo nenhum:**

| nível | mesas | 1/15 dias | 1/sem | **2/sem** | 3/sem | 4/sem |
|---|---|---|---|---|---|---|
| **2** | 2 | 0,0 | 0,0 | **0,0** | 0,0 | 0,0 |
| **3** | 3 | 0,9 | 0,4 | **0,2** | 0,2 | 0,2 |
| **4** | 3 | 2,2 | 1,1 | **0,5** | 0,4 | 0,4 |
| **5** | 5 | 3,5 | 1,7 | **0,9** | 0,7 | 0,6 |
| **6** | 5 | 5,7 | 2,8 | **1,4** | 1,1 | 1,0 |
| **7** | 5 | 7,8 | 3,9 | **2,0** | 1,6 | 1,4 |
| **8** | 7 | 10,0 | 5,0 | **2,5** | 2,0 | 1,8 |
| **9** | 7 | 13,0 | 6,5 | **3,3** | 2,6 | 2,4 |
| **10** | 7 | 16,1 | 8,0 | **4,0** | 3,2 | 2,9 |
| **11** | 9 | 19,1 | 9,6 | **4,8** | 3,8 | 3,5 |
| **12** | 9 | 23,0 | 11,5 | **5,8** | 4,6 | 4,2 |
| **13** | 9 | 27,0 | 13,5 | **6,7** | 5,4 | 4,9 |
| **14** | 11 | 30,9 | 15,4 | **7,7** | 6,2 | 5,6 |
| **15** | 11 | 35,6 | 17,8 | **8,9** | 7,1 | 6,5 |
| **16** | 11 | 40,4 | 20,2 | **10,1** | 8,1 | 7,4 |
| **17** | 13 | 45,2 | 22,6 | **11,3** | 9,0 | 8,2 |
| **18** | 13 | 50,9 | 25,4 | **12,7** | 10,2 | 9,2 |
| **19** | 13 | 56,5 | 28,3 | **14,1** | 11,3 | 10,3 |
| **20** | 15 | 62,2 | 31,1 | **15,5** | 12,4 | 11,3 |
| **21** | 15 | 65,1 | 32,5 | **16,3** | 13,0 | 11,8 |
| **22** | 15 | 67,9 | 34,0 | **17,0** | 13,6 | 12,4 |
| **23** | 17 | 70,8 | 35,4 | **17,7** | 14,2 | 12,9 |
| **24** | 17 | 74,1 | 37,0 | **18,5** | 14,8 | 13,5 |
| **25** | 17 | 77,4 | 38,7 | **19,3** | 15,5 | 14,1 |
| **26** | 17 | 80,6 | 40,3 | **20,2** | 16,1 | 14,7 |
| **27** | 17 | 83,9 | 42,0 | **21,0** | 16,8 | 15,3 |
| **28** | 17 | 87,2 | 43,6 | **21,8** | 17,4 | 15,9 |
| **29** | 17 | 90,5 | 45,2 | **22,6** | 18,1 | 16,4 |
| **30** | — | 93,7 | 46,9 | **23,4** | 18,7 | 17,0 |

**O vão medido, sem compensação nenhuma: entre quem joga uma e quem joga duas mesas por semana ele chega a `13` níveis, por volta do mês `23`.** *Ele abre porque quem está na frente cruza o nível 20 e passa a rodar missão de `240` XP enquanto o outro ainda roda missão de `106,25`* — **a faixa lendária acelera quem já chegou nela.**

> **E a curva mais lenta NÃO encolhe o vão — isso foi afirmado aqui e a conta desmentiu.** *As candidatas medidas dão praticamente o mesmo pior vão; o que a curva muda é **quando** ele acontece.* **A curva original entregava o pior por volta do mês `11`, no meio da vida útil de uma temporada; esta empurra para o mês `23`,** que é depois do fim da campanha de um ano que a Guilda planeja.

**O gatilho fica como exemplo trabalhado, e a conta dele mora aqui:**

| gatilho | fator | teto do vão |
|---|---|---|
| 3 níveis atrás | `1,5×` | 9 |
| 3 níveis atrás | `2×` | **6** |
| 3 níveis atrás | `2,5×` | **4** |
| 3 níveis atrás | `3×` | 4 |
| — | — | **`13`** |

***O fator não é sabor: é ele que decide o teto.*** *Dobrar o XP de quem está três níveis atrás corta o vão de `13` para `6`, e `2,5×` chega a `4`* — depois disso ele para de melhorar, porque o limite deixa de ser o XP e passa a ser o teto do nível 30.

> ***⚠ Estes números foram medidos de novo a cada troca de curva, e eles se movem.*** *A primeira conta do rascunho deu `3` para o fator `2×`* — **ela modelou a campanha inteira a uma faixa só, que é exatamente o erro que o §4.1 avisa.**

### 5.3 O que o servidor pode fazer, e quanto cada coisa vale

*Escrita na v0.196, e ela é a outra metade da decisão do §5.1.* **A curva crua é lenta de propósito, para o servidor ter espaço de acelerar do jeito dele em vez de ter de frear.**

> **Nada aqui é regra, e nada aqui é obrigatório.** *Um servidor que não use mecanismo nenhum roda a curva crua e chega ao nível 20 em `15,5` meses a duas mesas por semana. Está certo, e é mais lento do que as catorze respostas pediram.*

**O mecanismo mais forte é a mesa de dobro, e ela é fácil de operar: uma missão declarada como dobro paga duas vezes o tamanho dela.**

| mesas de dobro por mês | nível 20 a 2/sem | nível 30 | o que ela acrescenta |
|---|---|---|---|
| nenhuma | 15,5 meses | 23,4 | — |
| **uma** | **13,9** | **21,0** | `+12%` de XP |
| duas | 12,6 | 19,0 | `+23%` |
| três | 11,5 | 17,4 | `+35%` |

**Uma por mês devolve o ritmo que a curva anterior tinha**, e duas deixam mais rápido do que ele. *A recomendação do projeto é **uma**, porque ela recoloca o nível 20 dentro da faixa que o levantamento desenhou sem gastar o recurso todo.*

***⚠ E a mesa de dobro NÃO alcança quem joga pouco, o que é o limite dela.*** *Ela paga na proporção do que a pessoa já joga, então não dá para dobrar mesa que não foi jogada:* **quem joga a cada 15 dias só joga `2,2` mesas por mês, e o terceiro dobro do mês quase não move a linha dele — de `32,3` para `31,1` meses.** *Quem joga uma vez por semana continua em `18,4` meses até o nível 20 mesmo com três dobros.*

**Por isso o segundo mecanismo não é redundante com o primeiro: ele mira em quem ficou para trás, e não no ritmo geral.**

| mecanismo | o que ele faz | quanto vale |
|---|---|---|
| **mesa de dobro** | acelera o servidor inteiro | `+12%` de XP por mesa/mês; uma por mês vale `1,6` mês no nível 20 |
| **volta de quem sumiu** | dobro para quem está `3` níveis atrás, até alcançar | corta o vão de `13` níveis para `6`; não muda o ritmo de ninguém que esteja em dia |
| **bônus por motivação** | `+10%` na missão em que o personagem age na motivação dele, com aprovação da mesa | aplicado em metade das missões, vale `+5%` de XP |

> **O bônus por motivação não é invenção daqui.** *Ele sai da fonte `kwilkins` catalogada em `01-pesquisa/levantamento-ritmo-fora-do-projeto.md`, que é a única das quatro que escala recompensa por conteúdo em vez de por tempo.* **É a mesma família do `curta · padrão · longa · final de arco` do §4.**

**Os três somam, e o servidor não precisa dos três.** *Uma mesa de dobro por mês mais o bônus por motivação dá `+17%`, que põe o nível 20 em `13,3` meses.*

## 6. Mestrar não dá XP

> **Mestrar não paga XP. Paga na moeda que o sistema já tem separada: patente, contato, favor da instituição, acesso.**

É a decisão mais impopular desta peça e a que tem o argumento mais curto: **se mestrar paga XP, mestrar vira a rota ótima de subir de nível**, e a pessoa que mais dirige o mundo é a que menos joga nele. O Mega descreveu o estado final disso no server de hoje.

**A recompensa existe e ela é grande** — ela só mora no eixo social, que é onde o `arquitetura.md` já pôs o reconhecimento. Um mestre ativo constrói patente e rede, e as duas coisas abrem porta que nível nenhum abre.

*E existe uma conversão pontual depois de muitas mesas mestradas* — **um bônus por marca, não por sessão.** A forma dela ficou em aberto da v0.32 à v0.171, com a trava escrita antes da regra: ela não pode virar pagamento por mesa disfarçado. **Hoje ela é o §6.2.**

## 6.1 O salário — a quarta moeda, e a única com número

*Escrita na v0.171, quando a peça 14 §8 item 11 finalmente pediu ela.* **Das quatro que o §6 lista — patente, contato, favor, acesso —, três continuam discricionárias de propósito. Esta tem tabela.**

> **Feiticeiro recebe salário mensal da instituição, e o valor sai da patente.** *Não é pagamento por missão: é folha.*

| patente | por mês | por ano |
|---|---|---|
| **Grau 4** | `¥150.000` | `¥1,8 milhão` |
| **Grau 3** | `¥300.000` | `¥3,6 milhões` |
| **Grau 2** | `¥600.000` | `¥7,2 milhões` |
| **Grau 1** | `¥1.200.000` | `¥14,4 milhões` |
| **Especial** | `¥2.400.000` | `¥28,8 milhões` |

**O topo é canon e o resto é derivado.** *O Akutami respondeu, em entrevista, que o salário do Gojo é o de um ministro do gabinete japonês — e que feiticeiro recebe **salário mensal**, e não por missão.* **Um ministro ganha `¥29,61 milhões` por ano**, e a escada inteira sai daí: `29,61M ÷ 12 ÷ 2⁴` dá `¥154.219`, arredondado para `¥150.000`. *A única escolha desta tabela é esse arredondamento, e ele custa `−2,7%` no topo.*

> **⚠ O lastro é levantamento secundário, e fica declarado como tal.** *A fala do Akutami chega por reportagem sobre uma entrevista, e não por fonte primária lida.* **Se um dia aparecer o número direto da fonte, é a linha do topo que se move, e a base se recalcula sozinha.**

**E ela cruza com o Japão real sem precisar de conserto.** *Um recém-formado começa entre `¥200.000` e `¥250.000` por mês; um `Grau 4` fica pouco abaixo disso, que é o que ele é — estudante, com moradia da escola.* **Um `Grau 1` em `¥14,4 milhões` por ano é salário de executivo sênior**, e é a faixa que explica a Mei Mei ser rica trabalhando por dinheiro.

### O que ele NÃO é

**Ele não é o quarto eixo de progressão, e a trava é a mesma do §2.** *Se o salário comprasse poder, o Grau viraria nível com outro nome pela porta dos fundos.* **O que o dinheiro compra está na peça 14, e lá ele passa por uma prova: nenhuma compra torna legal uma montagem que já não fosse** — toda entrada de equipamento é travada por atributo e por treino antes de ter preço, e o preço só decide **quando** você a alcança, nunca **se**.

> **A folga é de propósito, e é grande.** *O loadout mundano mais caro que existe — `Revestimento` no topo, arma de assinatura de duas mãos, arma de uma mão e escudo `Torre` — custa `¥1,6 milhão`.* **A renda de uma campanha inteira, subindo de Grau no ritmo normal, é da ordem de `¥10,5 milhões`:** o mundano inteiro cabe em `15%` dela. *Os outros `85%` existem para o que ainda não foi escrito — ferramenta amaldiçoada comprada em vez de recebida, e fabricação.*

## 6.2 A conversão de mestragem — o único lugar em que mestrar vira número

*Escrita na v0.172, e o §6 a deixou em aberto na v0.32.* **A forma estava por escrever; a trava já estava pronta: um bônus por marca, não por sessão, e ela não pode virar pagamento por mesa disfarçado.**

> **A cada vinte mesas mestradas você recebe uma mensalidade extra do seu Grau.** *A marca fecha sozinha na vigésima, e paga na patente que você tinha naquele dia.*

***⚠ ISTO DEIXOU DE SER REGRA na v0.195, por decisão do Mizuki.*** **O livro publica a FORMA e não o valor** — *"a cada `X` mesas mestradas"* —, porque quanto se paga por mesa mestrada é decisão de cada servidor, *e um servidor pode escolher não pagar em dinheiro nenhum.* **Esta linha continua sendo a recomendação do projeto, e ela vale como exemplo trabalhado: é o `X` que a conta abaixo produz.**

**Nenhum dos dois números foi escolhido, e é por isso que a recomendação vale alguma coisa.** *O valor é a linha do §6.1 — a mesma mensalidade, sem moeda nova e sem tabela nova.* **E o `20` é uma divisão com dois donos:** o levantamento mede o mestre ativo em **duas a três mesas por mês**, e o §6.1 mede o catálogo mundano inteiro em **`15%`** da renda de uma campanha. **`3 ÷ 0,15 = 20`.**

> **Quem trocar o `X` fica com a conta na mão.** *Um servidor que ache `20` demorado baixa a marca e sabe o que está comprando: com `10`, o bônus dobra de frequência e o mestre ativo passa a tirar `30%` da renda mundana em vez de `15%`.* **A derivação é o que a peça entrega; o número é do servidor.**

**O que a divisão compra é a trava do §6, e ela sai exata:** *no ritmo mais pesado que a Guilda já relatou, a mestragem acrescenta `15%` à renda — a mesma fatia que o loadout mundano mais caro ocupa.* **Mestrar a campanha inteira paga um loadout completo, e nem um iene a mais.**

### 6.2.1 Por que ela não vira pagamento por mesa, e isso é aritmética

**A fração não depende do tamanho da campanha.** *Ganho e folha correm no mesmo relógio — a mestragem entrega `taxa ÷ 20` da folha, e só isso.* **Mestrar mais não descola a mestragem do salário: ela anda amarrada nele, em qualquer campanha e em qualquer patente.**

| quem mestra | mesas por mês | fecha uma marca em | acrescenta à renda |
|---|---|---|---|
| **pesado** — o teto relatado | `3` | `6,7` meses | **`15%`** |
| **ativo** — a fala do levantamento | `2` | `10` meses | `10%` |
| **ocasional** | `1` | `20` meses | `5%` |

*A coluna da direita é `taxa ÷ 20`, e é ela que responde à trava: a folha continua sendo a renda, e a marca é o bônus em cima.*

> **A marca é rara de propósito, e a régua de raro é a do próprio sistema.** *O §5 mede a cadência real da Guilda — duas mesas por semana — em `15,5` meses até o nível 20; nessa janela um mestre pesado fecha `2,3` marcas, contra os **quatro** marcos que a ficha atravessa nos níveis 6, 10, 14 e 18.* **Menos frequente que o marco, que é a coisa mais rara que uma ficha tem.**
>
> *O repreço da v0.196 encostou os dois:* **na curva anterior eram `1,5` marca contra quatro marcos, e agora são `2,3`.** *A marca continua mais rara, com folga de quase dois para um.*

**Quem mestra pouco não fecha marca nenhuma, e isso não é buraco.** *O §6 já diz onde mora a recompensa de mestrar — patente, contato, favor e acesso —, e nenhuma das quatro tem relógio.* **A marca é a conversão pontual que o §6 prometeu *"depois de muitas mesas mestradas"*, e vinte é muitas.**

### 6.2.2 Contar mesa mestrada não é o relógio que a peça 13 reprovou

**A peça 13 §7 recusou `uma vez por sessão` no catálogo de Legados, e citou justamente esta seção para recusar.** *O argumento continua de pé e não alcança a regra acima.*

**Lá o defeito é que *"uma sessão"* é leitura:** *três mestres leem a mesma palavra de três jeitos, e o spread entre a leitura mais generosa e a mais dura é `3,0×` na mesma ficha.* **Aqui não há o que ler.** *Uma mesa mestrada é uma missão postada e resolvida, e quem postou está no quadro — a contagem sai do registro da Guilda, e não da memória de ninguém.*

> **⚠ E não existe guardar marca.** *Ela fecha na vigésima mesa, no dia em que a vigésima acontece.* **Segurar mesa para fechar a marca depois de subir de patente não funciona, porque não existe o ato de fechar.** *O livro já escreve o mesmo cuidado do outro lado, em "guardar marco não guarda refino".*

## 7. O limiar do nível 20

> **Você chega ao nível 20 por XP. Você passa dele por feito.**

Chegando aos 14.300 de XP acumulado, o personagem para no nível 20 até a mesa reconhecer alguma coisa que ele fez. O XP continua acumulando e nada se perde — ele destrava de uma vez quando o feito acontece.

**De onde isso veio.** Foi pedido no levantamento, e o argumento não é de balanceamento:

> *"Eu colocaria algum tipo de requisito pra quebrar o padrão do lvl 20 e ir pro nível lendário. Seria mais demorado porém com alguma recompensa, pq daí iria tirar a ilusão do 'cheguei no lvl 20 pro 21 em 4 meses de mesa enquanto fulano de tal upou 7 níveis'."*

E ele encaixa numa coisa que o sistema já tinha: **a patente sobe por feito.** O limiar do 20 é o único lugar onde o eixo social e o eixo de poder se tocam — e se tocam uma vez só, na fronteira entre o mundano e o lendário.

**A trava que ele precisa.** *"O mestre decide o que é um feito"* não atravessa sete mesas. A lista precisa ser fechada, no molde do ambiente propício: **entradas escritas, e a palavra final do mestre em cima delas** — nunca do zero.

### 7.1 As oito, e a lista é fechada

*Escrita na v0.172.* **O mestre da mesa tem a palavra final sobre se uma delas aconteceu — e não sobre quais são.**

| | o feito | o que um segundo mestre lê para conferir |
|---|---|---|
| **1** | derrubar um `Chefe` de nível acima do seu | o manual traz `Chefe` e o nível do grupo na tabela de inimigo; o seu nível está na ficha |
| **2** | sair de pé de uma Expansão de Domínio completa | a completa resolve por acerto garantido, pela peça 11; *de pé* é não ter chegado a `0` |
| **3** | fechar um `final de arco` | o tamanho é declarado **antes** da mesa, pela seção 4 desta peça |
| **4** | pôr de pé alguém que estava a `0` de vida | `Aguentar` e `Insistir` são estados escritos, na peça 1 §5.5 |
| **5** | voltar do estágio 4 de dano de alma | os quatro estágios são tabela, na peça 24 §4 |
| **6** | cumprir uma `Promessa` até o fim, pagando a sua metade | os três termos ficam escritos quando ela fecha, na peça 22 §5.1 |
| **7** | trazer para a Guilda uma ferramenta de grau 1 ou especial | a escada de grau da ferramenta é a peça 16 §3, e a ficha registra qual |
| **8** | terminar a missão depois de outro personagem jogador chegar ao estágio 4 | o mesmo estágio da peça 24 §4, lido na ficha do outro e não na sua |

**Um feito basta, e ele destranca uma vez.** *Quem acumulou XP parado no 20 sobe de uma vez até o acumulado acabar, pela regra do §3.1 — o feito abre a porta, e não paga XP.*

### 7.2 O filtro que escolheu as oito já estava escrito, e é da peça 10

**Aquela peça separou lista fechada de lista de exemplo, e o critério dela serve inteiro aqui:** *o `ambiente propício` tem lista fechada porque **"esse lugar tem kit e comida?" é pergunta sobre o mundo** — a mesma resposta serve para qualquer mesa; e `isso foi uma luta?` fica aberto porque **é pergunta sobre a cena que aquele mestre acabou de dirigir**, e ninguém está em melhor posição de responder do que ele.*

**Toda entrada acima é do primeiro tipo.** *Cada uma cita um estado que a ficha ou o registro da missão carrega depois que a mesa acabou* — um nível, um `0` de vida, um estágio, um tamanho declarado antes, um grau escrito na ferramenta. **Nenhuma delas pergunta como a cena foi.**

> **É por isso que *"o mestre decide o que é um feito"* não atravessa sete mesas e esta lista atravessa.** *Sete mestres discordam sobre o que foi impressionante; nenhum deles discorda se o `Chefe` era de nível acima.*

### 7.3 Três das oito trocaram de forma, e vale dizer por quê

**As três reprovavam no filtro do §7.2 do jeito que foram propostas, e as três tinham conserto.**

- **`fechar um incidente que teria vazado` virou `fechar um final de arco`.** *O original é contrafactual — *teria* vazado —, e o sistema não tem Véu: `vazar` não aparece em peça nenhuma nem no livro.* **O tamanho da missão é o gancho mais duro que esta peça tem**, porque a seção 4 obriga a declaração *antes*, exatamente para o tamanho não ser decidido depois em função de como a mesa correu.
- **`escrever um Fundamento inédito` virou `voltar do estágio 4 de dano de alma`.** *Escrever Fundamento é decisão de criação e não feito de mesa — sai do Passo da peça 8, e não da missão.* **E `Inédito` já é o nome de um Legado do Latente**, na peça 13: a entrada colidiria com um termo em uso.
- **`a instituição te dever um favor` virou `trazer para a Guilda uma ferramenta de grau 1 ou especial`.** *`Favor da instituição` é uma das quatro moedas com que o §6 paga a mestragem* — usá-lo como feito fecharia laço entre as duas seções desta peça. **E o favor é estado narrado pelo mestre, sem nada na ficha para um segundo conferir.**

> **⚠ E a primeira entrada trocou `grau` por `nível`, porque não existe grau de maldição hoje.** *A escada `grau 4 a grau 1, mais o especial` existe para **ferramenta e objeto**, na peça 16 §3, e para **patente**, no §6.1 desta.* **Inimigo não tem grau em documento nenhum:** *a tabela do manual é `nível do grupo → vida e dano`, com as colunas `Chefe` e `Capanga`.* **Se o BESTIÁRIO der grau ao inimigo, esta entrada volta para a forma original, e o feito 1 é a linha que o obriga a decidir.**

> **⚠ O feito 7 é o mais frouxo dos oito, e o registro fica.** *Uma ferramenta especial aparecer é decisão do mestre — a peça 16 §3.2 escreve que ela `aparece uma vez por arco, e não duas na mesma mesa`.* **O que a lista exige é que o FATO seja conferível depois, e o grau fica escrito na ficha;** *mas ele é o único dos oito em que a porta é aberta por quem dirige, e não alcançada por quem joga.*

## 8. Falhar

> **Missão falhada paga metade ou nada, e quem decide é o mestre.**

Uma faixa e não um número, porque as duas pontas existem: uma missão perdida por azar de dado não é a mesma coisa que uma abandonada na metade.

**O piso da faixa é metade, e não zero, por um motivo de mesa** — seis horas de sessão que terminam em nada fazem a pessoa não voltar. E o teto é metade, e não cheio, porque senão o sucesso deixa de significar.

*Isto é discricionariedade assumida*, no mesmo molde do *"o mestre declara o que foi uma luta"* da peça 10. Vai para o playtest com a mesma pergunta: **dois mestres pagam parecido pela mesma falha?**

## 9. Como a Guilda opera isto

1. **O mestre posta a missão e declara o tamanho** — curta, padrão, longa, final de arco.
2. **A mesa acontece.**
3. **No fim, o mestre paga o valor declarado**, cheio no sucesso, metade ou nada na falha.
4. **O jogador anota na ficha**, e aplica o desconto da semana se já for a terceira missão.
5. **Chegou ao XP do próximo nível, sobe** — no máximo um nível, e o resto fica acumulado. Não precisa de aprovação, exceto no limiar do 20.

**Uma linha de missões paga por missão, e não no fim.** Quem entra no meio de uma linha recebe pelo que jogou — é o que permite mesa aberta funcionar.

**O desconto semanal é do jogador, não da mesa.** Numa missão com quatro pessoas, uma pode estar na primeira semana dela e outra na quarta. Cada um aplica o seu.

## 10. Em aberto

- ~~**A lista de feitos do limiar do nível 20.**~~ **Fechada na v0.172: são as oito do §7.1**, e o filtro que as escolheu é o da peça 10.
- ~~**A forma da conversão de mestragem** — um bônus por marca, sem virar pagamento por mesa.~~ **Fechada na v0.172: é o §6.2**, uma mensalidade do seu Grau a cada vinte mesas mestradas.
- ~~**A curva é rápida demais para a cadência que a Guilda joga.**~~ **Represada na v0.196: a base foi de `1` para `3` missões e o passo de `+1` a cada três para `+2`**, e o §3.0 tem a derivação dos cinco números.
- **Se dois mestres pagam parecido pela mesma falha.** Marcado para o playtest.
- **Se a semana é o relógio certo** para o retorno decrescente, ou se ele devia acompanhar o descanso longo, como o resto do sistema.
- **Se `15,5` meses até o nível 20 incomoda na prática.** *O §5.1 mede a distância para a mediana do levantamento em `+5,3` meses crus, e `+3,7` com uma mesa de dobro por mês.* **Registrado, não consertado** — a curva é lenta de propósito, e o §5.3 é o que o servidor tem para acelerar.
- **Se o vão de `13` níveis do §5.2 aparece de verdade.** *Ele precisa de vinte meses de campanha e de duas pessoas em cadências opostas o tempo todo.* **É a primeira coisa que o playtest pode desmentir.**
- **Se o teto de um nível por missão volta a morder.** *Hoje ele não morde em combinação nenhuma (§3.1), e um servidor que pague mais de `500` numa missão o traz de volta* — **e a mesa de dobro do §5.3 é exatamente isso: um final de arco dobrado paga `600`.**

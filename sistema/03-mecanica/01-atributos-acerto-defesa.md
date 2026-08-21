# DE ONDE VEM O NÚMERO

**Fase 4, primeira peça.** Atributos, maestria, rolagem de acerto, defesa e Testes de Resistência.
Versão v0.9, ampliada até a v0.19, corrigida na v0.24, com crítico na v0.25, com PE máximo e arredondamento na v0.26, e com a base de acerto refeita na v0.117 — 10/08/2026

> **Três mudanças posteriores vivem aqui.** Os **pontos de vida** ganharam fórmula na v0.17 e passaram a variar por Caminho na v0.19 (seção 5.1) — até então Constituição não tinha número nenhum. E desde a v0.16, **Inteligência sabe e Essência percebe**: Sentir Energia e Percepção mudaram de atributo, o inverso do que a v0.8 tinha decidido.

Todo número aqui foi calculado, não estimado. O validador é `conferir-atributos.py`, na mesma pasta.

---

## 1. A regra que governa tudo

Numa rolagem disputada, **os dois lados precisam crescer no mesmo ritmo**. Não basta os dois crescerem: se um cresce mais rápido, a chance deriva ao longo da campanha, e nenhuma quantidade de valor fixo conserta isso.

Os ritmos deste sistema:

| O que cresce | Quanto cresce numa campanha inteira |
|---|---|
| Um atributo em que o personagem investe | de 3 a 6 — **+3** |
| Maestria, se subisse a cada 4 níveis | de 1 a 8 — **+7** |
| Maestria, subindo a cada 8 níveis | de 1 a 4 — **+3** |

É por isso que **maestria não pode substituir um atributo se crescer duas vezes mais rápido que ele**. Ou ela anda no ritmo do atributo, ou ela não pode aparecer no lugar dele.

## 2. Maestria

> **Maestria** começa em 1 e sobe um ponto a cada oito níveis.

| nível | 2–9 | 10–17 | 18–25 | 26–30 |
|---|---|---|---|---|
| maestria | 1 | 2 | 3 | 4 |

Quatro degraus, no mesmo ritmo de um atributo investido. Cai num marco sim, num marco não da escada de quatro níveis que já governa refino e atributo — então continua sendo um ganho de marco, só que a cada segundo.

**A ficha começa no nível 2**, já com um feitiço. O nível 1 fica como opção de campanha: o personagem antes de ser feiticeiro, o Itadori antes do dedo.

## 3. Cinco atributos

O número **é** o modificador. Escala 0 a 6.

**Força · Destreza · Constituição · Inteligência · Essência**

| Atributo | O que governa |
|---|---|
| **Força** | ataque corpo a corpo, agarrar, quebrar, carregar |
| **Destreza** | ataque à distância, Defesa, iniciativa, furtividade |
| **Constituição** | pontos de vida — e só isso, o que é bastante |
| **Inteligência** | conhecimento, investigação, reconhecer uma técnica pelo catálogo |
| **Essência** | **perceber energia amaldiçoada**, trato social, hierarquia, **negociar Pactos** |

**Essência** funde o que seriam Sabedoria e Carisma. **Inteligência sabe; Essência percebe.**

*Corrigido na v0.16.* Da v0.8 até a v0.15 era o contrário: a percepção morava em Inteligência, para tirar dela o papel de atributo-depósito. A intenção estava certa e o resultado saiu invertido — com o quadro de perícias escrito, Inteligência ficou com 56% do valor de mesa e Essência com 21%. Sentir energia amaldiçoada não é análise, é a sua energia reagindo à de outro; na obra quem sente melhor não é quem estudou mais. Movendo Sentir Energia e Percepção para Essência, o peso ficou 39% e 39%. A conta está na peça 7, seção 3.

Conferido contra o manual: nenhum dos cinco é termo definido lá.

**Dois pontos para acompanhar em playtest.** *Força* é o único candidato a depósito que sobrou — quem escolher Destreza para o TR Físico e não lutar sem técnica pode zerá-la. E vale conferir se a correção acima não passou do ponto: *Essência* agora carrega a perícia mais rolada da mesa, o TR Espírito e os Pactos.

## 4. Quatro Testes de Resistência

| Teste de Resistência | Usa | Serve para |
|---|---|---|
| **Físico** | Força **ou** Destreza — declarado na criação e travado | reagir, esquivar, aguentar impacto |
| **Vigor** | Constituição | veneno, doença, exaustão |
| **Intelecto** | Inteligência | controle mental, ilusão, dissociação |
| **Espírito** | Essência | vontade, determinação, não se dobrar |

Como o TR Físico usa o melhor de dois, ele fica acima dos outros três. O personagem médio **esquiva melhor do que resiste a ter a mente mexida** — para Jujutsu Kaisen é o sabor certo, porque o que apavora na obra não é o soco, é o Mahito.

## 5. As fórmulas

```
Maestria             = 1, +1 a cada 8 níveis

Ataque corpo a corpo = d20 + Força + maestria
Ataque à distância   = d20 + Destreza + maestria
Ataque de conjuração = d20 + atributo da técnica + maestria
Defesa               = 10 + Destreza + proteção
Pontos de vida       = (vida inicial do Caminho + Constituição)
                       + (vida por nível do Caminho + Constituição) × (nível − 1)
Pontos de energia    = PE por nível do Caminho × nível   (sem atributo, sem valor inicial)
Integridade          = 20 + 8 × (nível − 1)      (plana, sem Caminho e sem Constituição)
CD de feitiço        = 8 + atributo da técnica + maestria
Teste de Resistência = d20 + atributo do TR + maestria   (a maestria só entra se treinado)
Perícia              = d20 + atributo + maestria   (a maestria só entra se treinado)
```

**A maestria é a marca do treino, e ela só aparece onde você treinou** — nas três rolagens de acerto, nas perícias, nos ofícios e no Teste de Resistência que a sua ficha treinou. *Ela não está na Defesa, que é passiva.*

> **A técnica declara um atributo, na criação, e ele não muda.** *Qualquer um dos cinco.* **É esse atributo que entra no acerto de conjuração e na CD dos seus feitiços** — o feiticeiro que conjura pela Força existe, e ele é o molde do Todo.

### 5.0 A maestria é a marca do treino, e ela aparece dos dois lados de cada rolagem

*Escrito na v0.117, e ele é o conserto de uma deriva que estava viva e que nenhum validador via.*

**Uma rolagem disputada tem duas fichas, e a maestria entra na de quem treinou — nos dois papéis.**

| | quem rola | contra o quê | o que cresce de cada lado |
|---|---|---|---|
| **acerto** | atacante: `atributo + maestria` | a **Defesa** | Destreza `+3` **e a proteção, que vai de `1` a `4`** |
| **CD** | a sua CD: `8 + atributo + maestria` | o **Teste de Resistência** | atributo `+3` **e a maestria de quem treinou** |

**Os dois lados crescem `+6` nas duas rolagens, e é isso que faz a chance não derivar.**

*Do lado do acerto, o `+6` do alvo é involuntário:* **a proteção de cobrir-se é `1/3 do refino + 1` (peça 11 §6), e o refino sobe sozinho na linha de graça do marco.** *Ninguém escolhe — todo mundo chega lá.*

*Do lado da CD, o `+6` do alvo é comprado:* **a maestria só entra no Teste de Resistência que a ficha treinou**, e cada ficha treina dois de quatro. **Nos outros dois ela cresce `+3` contra uma CD que cresce `+6`, e cai `15` pontos percentuais na campanha.**

> ***Decisão do Mizuki na v0.117: isso é o preço de não treinar, e é para doer.*** *O TR que você treinou fica plano; o que você não treinou vira o lugar por onde um chefe entra, e vira mais a cada nível.*

### O `8` da CD não é escolha de gosto: ele É a chance de quem treinou

**`8 + atributo + maestria` contra `d20 + atributo + maestria` deixa exatamente `8` no dado.** *E `d20 ≥ 8` é `65%`.*

| | nv2 | nv10 | nv18 | nv26 | nv30 | deriva |
|---|---|---|---|---|---|---|
| **treinado** — hoje e antes da v0.117 | 65% | 65% | 65% | 65% | **65%** | **`0`** |
| **sem treino** — era `55%` plano | 60% | 55% | 50% | 45% | **45%** | **`−15pp`** |

**Quem treinou resiste hoje exatamente o que resistia ontem.** *O `+2` fixo entregava `65%` e a maestria entrega `65%`, e a mudança inteira caiu no TR que ninguém treinou.* **Com base `10` o não-treinado terminaria em `35%`; o `8` é o que segura ele em `45%`, que ainda é moeda no ar.**

### Buff plano não deriva, e é por isso que só a proteção puxou a maestria

*O Mizuki levantou que escudo, feitiço e habilidade vão subir a Defesa, e que isso tem de entrar na conta.* **Entra, e a conta diz que eles mudam o nível e não a inclinação:**

| Defesa do alvo difícil | nv2 | nv10 | nv18 | nv30 | deriva |
|---|---|---|---|---|---|
| sem nada por cima | 55% | 55% | 55% | 55% | `0` |
| `+1` de escudo | 50% | 50% | 50% | 50% | `0` |
| `+2` — Manha `+1` e escudo `+1` | 45% | 45% | 45% | 45% | `0` |
| `+4` — escudo 3 e Manha, o topo do que existe | 35% | 35% | 35% | 35% | `0` |

**Um `+1` de escudo vale `+1` no nível 2 e `+1` no 30 — ele não cresce.** *Só a proteção de cobrir-se cresce, e foi por ela que a maestria entrou no acerto.* **Quanto um acerto vale contra um alvo empilhado é escolha de calibragem; a inclinação é o que não pode estar errada.**

### O que a v0.116 achou, e o que a v0.117 fez com isso

> ⚠⚠ **Até a v0.116, esta seção dizia que uma habilidade de Caminho podia "trocar o `2` fixo por um atributo", e que "a troca é neutra em balanço porque os dois crescem igual".** *A frase estava em três documentos — aqui, na peça 6 §6 e no capítulo 9 do livro — desde a v0.9, e ela nunca foi neutra.*

**O que a v0.116 mediu, e que continua sendo o motivo de o `2 + maestria` ter morrido:**

| | nv2 | nv6 | nv10 | nv14 | nv18 | nv22 | nv26 | nv30 |
|---|---|---|---|---|---|---|---|---|
| `2 + maestria` | 3 | 3 | 4 | 4 | 5 | 5 | 6 | 6 |
| o atributo investido | 3 | 3 | 4 | 4 | 5 | 5 | 6 | 6 |

**Eles não "crescem no mesmo ritmo": eram o mesmo número em todo nível.** *Então trocar só o `2` deixava `atributo + maestria` — e a frase media `2 + maestria` (`+3`) contra `atributo` (`+3`) para concluir que a troca era neutra, quando a troca substituía apenas o `2`, que cresce `+0`.* **A outra leitura, trocar o termo inteiro, empatava na melhor das hipóteses e ninguém pegaria.** *Ou quebrava a regra que governa tudo, ou era entrada morta.*

### E a deriva de `−15pp` que ninguém via, porque o validador segurava a proteção em 1

***Achado na v0.117, e ele veio de uma observação de mesa do Mizuki:*** *"a Defesa vai estar chegando em picos de 20-22"*. **Ele está certo, e a seção 6 media contra um alvo de Defesa 17.**

**A peça 14 §3 deriva o teto de Defesa em `20` somando `10` + atributo `6` + os `4` de cobrir-se no refino `10`.** *Este documento media o "caso difícil" contra `10 + Destreza investida + proteção 1` — a proteção do nível 2, congelada.* **Dois documentos descrevendo o mesmo alvo com quatro pontos de diferença, e a peça 14 é quem está certa**, porque a proteção é `1/3 do refino + 1` e o refino sobe sozinho na linha de graça do marco.

| alvo que investe em Destreza e carrega refino | nv2 | nv10 | nv18 | nv26 | nv30 |
|---|---|---|---|---|---|
| Defesa, com a proteção andando junto | 14 | 16 | 18 | 20 | **20** |
| Defesa como a seção 6 media | 14 | 15 | 16 | 17 | 17 |

**Com o alvo certo, o acerto de HOJE derivava `−15pp`:**

| | nv2 | nv10 | nv18 | nv26 | nv30 | deriva |
|---|---|---|---|---|---|---|
| `d20 + atributo` (físico, como estava) | 50% | 45% | 40% | 35% | **35%** | **`−15pp`** |
| `d20 + 2 + maestria` (conjuração, como estava) | 50% | 45% | 40% | 35% | **35%** | **`−15pp`** |
| **`d20 + atributo + maestria`** | 55% | 55% | 55% | 55% | **55%** | **`0`** |

**Os dois lados crescem `+6`, e é por isso que fecha.** *A Defesa ganha `+3` de Destreza e `+3` de proteção; o acerto ganha `+3` de atributo e `+3` de maestria.* **A oscilação que sobra é de `5pp` e é irredutível:** a proteção sobe um ponto a cada quatro níveis e a maestria sobe a cada oito, então as duas escadas ficam meio degrau fora de fase — e meio degrau de d20 é `5pp`. *O validador aceita `5` de tolerância nesta checagem, e só nela, com o motivo escrito no código.*

> **É a lição nº 1 pela terceira vez, e desta vez a própria peça denunciava.** *A seção 7 diz, com todas as letras: "tudo que cresce numa campanha precisa entrar no teste — atributo, **proteção**, equipamento".* **O validador foi corrigido na v0.8 para variar o atributo do defensor, e a proteção ficou para trás no `1`.** *Uma frase certa escrita ao lado de um teste que não a obedece sobrevive muito mais tempo que uma frase errada.*

### O que a mudança cobra, e de quem

**Ela cobra ter um atributo no teto.** *Hoje o `2 + maestria` chega a `6` sozinho, sem a ficha pagar nada; agora quem deixa todos os atributos no meio fica para trás.*

| o feitiço acerta | nv2 | nv10 | nv18 | nv30 |
|---|---|---|---|---|
| atributo da técnica levado ao teto | 55% | 55% | 55% | **55%** |
| atributo parado em `3` desde a criação | 55% | 50% | 45% | **40%** |
| sem treino na arma (a maestria não entra) | 50% | 45% | 40% | **35%** |

**E ela não cobra dos Caminhos físicos, porque o atributo é livre.** *Era essa a objeção da v0.116 — que um Bastião precisaria de Essência 6 — e ela morre com "qualquer atributo":* **o Bastião aponta a técnica para a Força que ele já leva ao teto, e paga zero.** *Cada Caminho aponta para o atributo que já é natural dele, e a única ficha que perde é a que não leva nenhum ao teto.*

> **⚠ Declarado, e vai para o playtest: Constituição é a escolha ótima de quem só conjura.** *Todo Caminho tem um atributo que já faz dois trabalhos — Força bate, Destreza atira e defende, Essência percebe e negocia —, mas o segundo trabalho da Constituição vale para todo mundo.* **Um conjurador puro que aponte a técnica para Constituição paga zero e ainda é o mais duro da mesa.** *Não quebra número nenhum — o acerto continua em `55%` como o de todo mundo —, mas apaga a cor da escolha: "Inteligência sabe, Essência percebe" deixa de significar alguma coisa para a técnica.* **Fica como está, por decisão do Mizuki de que o atributo é livre, e vira pergunta de mesa: *alguém escolheu um atributo de técnica que não fosse o mais alto que já tinha?***


## 5.1 Pontos de vida

> **No nível 1 você recebe a vida inicial do seu Caminho, mais a sua Constituição.**
> **Em cada nível depois, você recebe a vida por nível do seu Caminho, mais a sua Constituição de novo.**

| Caminho | dado | vida no nível 1 | por nível | PE por nível | a troca |
|---|---|---|---|---|---|
| **Bastião** | d12 | 12 | 7 | 4 | menos combustível, mais couro |
| **Vanguarda** | d8 | 8 | 5 | 5 | meio a meio |
| **Guia** | d8 | 8 | 5 | 5 | meio a meio |
| **Evocador** | d6 | 6 | 4 | 6 | combustível cheio, e corpos na frente |
| **Emanador** | d6 | 6 | 4 | 6 | combustível cheio, canhão de vidro |

**A vida inicial é o máximo do dado; a vida por nível é a metade dele arredondando para cima.** Se a sua mesa preferir, role o dado em cada nível em vez de pegar o valor fixo — só saiba que rolar rende meio ponto a menos por nível na média, e é essa a aposta.

**A soma de vida e PE fica praticamente igual nos cinco:** 11 no Bastião e 10 nos outros quatro. É isso que faz a troca "couro contra combustível" ser escolha de sabor em vez de degrau de poder.

### Por que a média dá 5, e não 8

O manual calibra vida de chefe, dano de chefe e dano de capanga em cima de **8 de vida por nível**. A média dos cinco Caminhos aqui é 5 — e é assim que tem que ser.

O 8 do manual é a vida **total** por nível, sem atributo nenhum, porque quando ele foi escrito não existia Constituição na conta. Com Constituição entrando, a comparação certa é:

| | média dos dados | mais a Constituição típica (3) | o manual supõe |
|---|---|---|---|
| dados somando 8 | 8 | **11** | 8 |
| **dados somando 5** | 5 | **8** | 8 |

Uma versão anterior deste documento usava dados que somavam 8 e conferia isso contra o 8 do manual. Estava errado: com Constituição por cima, o grupo ficava com **38% de vida a mais** do que a tabela de encontro supõe, e o combate durava 4,7 rodadas onde o manual promete 3,5.

**A trava certa é: média dos dados + 3 de Constituição ≈ 8.** Com ela, o grupo cai em 2,9 a 3,4 rodadas sob foco — em cima do alvo do manual, sem tocar em nenhuma tabela dele.

Por Caminho, com Constituição 3, rodadas para cair sob foco:

| | nv 2 | nv 10 | nv 20 | nv 30 |
|---|---|---|---|---|
| Bastião | 4,2 | 4,0 | 4,2 | 4,2 |
| Vanguarda · Guia | 3,2 | 3,2 | 3,3 | 3,4 |
| Evocador · Emanador | 2,7 | 2,8 | 2,9 | 2,9 |

A curva é plana do nível 2 ao 30 em todos os cinco, que é o que se quer: o mestre nunca precisa saber o nível para estimar quanto tempo alguém aguenta.

### Vida é a única alavanca que a trava do Caminho deixa aberta

A peça 5 proíbe o Caminho de dar dados de dano, Classe de feitiço, Melhoria de graça ou cura. Sem vida por Caminho, o Bastião — *"o corpo como resposta: aguentar, encarar, prender"* — não teria um número que o fizesse aguentar mais que um Emanador. A única coisa que o tornaria duro seria a Constituição dele, que qualquer conjurador também pode pegar.

Vida é o que transforma "aguentar" em mecânica em vez de sabor. E ela conversa com o PE em sentido contrário: quem tem mais couro tem menos combustível.

**Um aviso sobre o tamanho do efeito.** O que separa o Bastião do Emanador é a **razão** entre os dois números, não o tamanho deles — e a Constituição, que entra igual para os dois, achata essa razão. Com Constituição 3, o 7 contra 4 vira 10 contra 7. Por isso o Bastião aguenta 1,44× o que o Emanador aguenta, e não 1,75×. Se um dia isso parecer pouco, o número a mexer é a **distância** entre o maior e o menor, não o valor de todos.

### Constituição entra cheia

*Escrito na v0.17.* Até aqui, três documentos diziam que Constituição governava pontos de vida e **nenhum dizia quanto**. A única fórmula que existia era a do manual — `20 + 8 × (nível − 1)` —, e ela não tem atributo nenhum. Ou seja: Constituição entregava só o Teste de Resistência Vigor, e o argumento que tirou as perícias dela era um trabalho que ela não tinha.

**O número que decide o tamanho dela não é o do manual** — o manual não tem atributo nenhum na conta de vida, então qualquer valor pareceria demais comparado a ele. A comparação certa é com **Destreza**, o outro atributo que já compra sobrevivência, pela Defesa.

### As três alavancas, e a que ficou grande demais

Todas medidas do valor 1 ao valor 6, que é a faixa que uma ficha real percorre:

| | nível 2 | nível 10 | nível 30 |
|---|---|---|---|
| Caminho, do Evocador ao Bastião | +56% | +46% | +44% |
| **Destreza**, pela Defesa — faz o inimigo errar mais | +62% | +56% | +45% |
| **Constituição**, pela vida — faz você aguentar mais | +67% | **+79%** | **+82%** |

*Corrigida na v0.24.* A linha do Caminho dizia **+36% / +43% / +44%**, e nenhuma fórmula do projeto reproduzia isso: o +36% é o número da **v0.18**, de quando a faixa era "de 6 para 10 de vida por nível", e sobreviveu à revisão da v0.20 que montou esta tabela justamente para acertar as bases. Medida do mesmo jeito que as outras duas — a ficha mais frágil contra a mais dura, com Constituição 3 —, a faixa do Caminho é a de cima.

Do valor **0** ao 6, Constituição chega a **+113%** no nível 10. **Esse número não é comparável aos +56% da Destreza**, que são medidos de 1 a 6. Na mesma base, é **+79% contra +56%** — a Constituição está na frente por **1,4×**, não por 2×. É a diferença entre "um atributo puxou" e "um atributo dominou", e é o número que a pergunta de playtest deveria estar usando.

Repare que as curvas correm em sentidos opostos. **Destreza protege mais cedo e Constituição protege mais tarde**, porque a Defesa não cresce com o nível e a vida cresce. Isso não é defeito — é o motivo de as duas coexistirem sem uma dominar a outra a campanha inteira.

**Mas Constituição passou a Destreza, e isso é novo.** Na versão anterior ela comprava +45% no nível 10, abaixo dos +56% da Destreza. Duas coisas somaram para inverter: a vida por nível ficou menor, então cada ponto de Constituição pesa proporcionalmente mais; e ela passou a entrar **também no nível 1**, multiplicando por *nível* em vez de *(nível − 1)*.

Não quebra nada — as três continuam sendo escolhas, e Destreza ainda compra ataque à distância, iniciativa e quatro perícias de brinde. Mas é o primeiro número do sistema em que um atributo está claramente na frente em sobrevivência. **Se em playtest ninguém aparecer com Constituição 0 ou 1, ela virou obrigatória**, e o conserto é uma linha: ela volta a entrar só a partir do segundo nível.

### O espalhamento é largo de propósito

No nível 30, a ficha mais frágil possível tem **122** de vida e a mais dura tem **395**: **3,2 vezes**. É mais largo que o d20 clássico, onde a distância entre o conjurador frágil e o brutamontes fica perto de 2 vezes.

A causa não é só o Caminho. É a **Constituição entrar já no nível 1** — assim ela multiplica por *nível* em vez de *(nível − 1)*, e no nível 30 com Constituição 6 são 180 de vida somados a uma base de 122 no Emanador.

Traduzido em rodadas sob foco, no nível 30:

| ficha | vida | rodadas |
|---|---|---|
| Emanador de Constituição 0 | 122 | **1,7** |
| Emanador de Constituição 3 | 212 | 2,9 |
| Bastião de Constituição 3 | 305 | 4,2 |
| Bastião de Constituição 6 | 395 | **5,5** |

O extremo de baixo é duro: um Emanador que zerou Constituição cai em menos de duas rodadas de foco. Isso é escolha dele, e a ficção acompanha — conjurador puro que não cuidou do corpo morre rápido em Jujutsu Kaisen. Mas é o número a acompanhar em playtest antes de qualquer outro.

### A Integridade fica de fora das duas

O manual diz *"Integridade = vida máxima"*. Com Caminho e Constituição na vida, essa frase daria de graça a um corpo duro uma **alma dura**, e dano de alma é justamente o que deveria ignorar o corpo — o que o Mahito faz não passa pelo músculo.

> **Integridade = 20 + 8 × (nível − 1).** Plana, igual para todo mundo.

É exatamente a fórmula que o manual já tem, sem nenhum número mexido. Muda uma frase e não muda uma tabela: onde o manual diz *"Integridade = vida máxima"*, leia **"Integridade é a alma, e a alma é igual para todo mundo"**. Os quatro estágios de dano de alma continuam valendo do jeito que estão.

**Com a vida do corpo menor que antes, a alma passou a ser a reserva maior para quase todo mundo.** No nível 30 com Constituição 3, o Emanador tem 212 de corpo contra 252 de alma; só o Bastião inverte, com 305 contra 252.

Isso produz a imagem certa nos dois extremos. O **Emanador** cai pelo corpo antes de a alma acabar — ele morre inteiro. O **Bastião** é o único que sobrevive tempo suficiente para a alma acabar primeiro: ele fica de pé com 53 de vida ainda no medidor, sem ser mais ele. É exatamente o que o Mahito faz com quem é duro demais para morrer de porrada.

**Fica marcado como coisa a acompanhar:** com a alma maior que o corpo em quatro dos cinco Caminhos, o estágio 4 de dano de alma quase nunca dispara — a pessoa cai antes. Isso muda quando a Essência entrar.

**O próximo passo já está decidido, e não aplicado:** a Integridade vai escalar com **Essência**, virando uma segunda vida de verdade em vez de um número plano. Fica para a peça de dano de alma, com o contexto que ela vai trazer. Quando entrar, os dois eixos se cruzam em vez de empilhar — o Emanador de Essência alta fica com alma grossa e corpo fino, o exato oposto do Bastião.

### 5.1.1 Vida temporária

***Decisão do Mizuki na v0.108.*** **Oito efeitos do manual concediam vida temporária e nenhum
documento do projeto dizia como ela funciona** — nem esta peça, nem as outras dezoito, nem o
manual. *`Apoio`, `Fluxo`, `Aprumo`, `Crosta` e quatro feitiços prontos.*

> **A vida temporária é anteparo, e não vida.** Ela **é gasta antes** da vida real, **não
> acumula** — duas fontes, você fica com a maior, nunca com a soma —, **tem teto de metade da
> sua vida máxima**, e **some no fim da cena**.
>
> **O mestre pode deixar ela atravessar para a cena seguinte** quando a preparação foi
> deliberada: quem se cobre antes de entrar no prédio não perde o que gastou porque a cena
> mudou de nome.

**Cada uma das quatro tem razão, e três delas já estavam decididas por outro número:**

**Gasta primeiro** — é o que o `Braseiro` já diz para energia temporária: *"gasta como PE, e
gasta primeiro"*. Uma segunda resposta para a mesma pergunta seria divergência.

**Some no fim da cena** — mesmo relógio da energia temporária do `Braseiro`, e é ele que
sustenta o preço. *A régua do projeto diz que dano evitado converte `1` pra `1` (peça 11 §9),
e um ponto de feitiço vale `1d8` = `4,5` de dano.* **O `Apoio` entrega `3` por ponto, que é
`0,67×`** — um desconto de um terço que só se justifica se a vida temporária for desperdiçada
com frequência. *Fosse ela até o descanso longo, seria quase sempre consumida, e o `Apoio`
estaria subvendido em 50%.* **A duração curta é o que faz o preço fechar.**

**Não acumula** — sem isso, duas fontes viram soma e a régua 1:1 quebra: dois `Apoio` de
Classe 1 entregariam `18` de dano evitado por `6` pontos, contra os `27` de dano que os mesmos
`6` pontos comprariam em `1d8`. *Com o teto, some rápido; sem o teto, empilhar é sempre melhor
que atacar.*

**Teto de metade da vida máxima** — e aqui a conta mostra que ele morde:

| efeito | entrega | cortado pelo teto? |
|---|---|---|
| `Fluxo`, ao conjurar Classe 1 a 7 | `2` a `14` | **nunca** — fica bem abaixo |
| `Apoio` puro, Classe 1 a 7 | `9` a `63` | **sempre**, em toda Classe |

*Um `Apoio` de Classe 1 entrega `9` num Emanador de nível 2, cujo teto é `7`.* **O teto vira o
limite real do `Apoio`, e não a Classe do feitiço.**

> ***Decisão do Mizuki, com o corte à vista:*** **é freio de propósito.** *Vai existir
> habilidade que passa da metade e é cortada, e vai existir habilidade que não chega perto —
> é gestão de recurso, e é a mesma escolha que um jogador de d20 faz ao decidir em que altura
> gasta a cura.* **Um `Apoio` puro no teto ainda é o feitiço que mais entrega valor bruto do
> sistema; o que o teto impede é ele apagar uma luta sozinho.**

**O que isto NÃO faz:** vida temporária não sobe a vida máxima, não conta para `Insistir`, e
não é cura — quem está a `0` de vida e recebe vida temporária continua a `0` e continua
caindo. *Ela previne dano que ainda não veio; não devolve o que já saiu.*

## 5.2 Crítico

*Escrito na v0.25.* O crítico era usado e nunca tinha sido definido: o manual cita *"em crítico"* na Melhoria **Estilhaço** e para por aí, e o projeto não tinha uma linha sobre ele.

> **20 natural numa rolagem de acerto é crítico. Você dobra os dados.**
> Dobra os dados da arma, se for arma; os dados da Classe, se for feitiço ou feitiço de Toque.
> **Nada mais dobra** — nem Força, nem dados que vieram de Melhoria, nem dano fixo.

Três coisas caem dessa frase, e nenhuma delas precisa de regra a mais.

**Só existe crítico onde existe rolagem de acerto.** O manual resolve feitiço de três jeitos — *Acerto · Teste de Resistência · Automático* —, e os dois últimos não têm dado de ataque. Um feitiço de Explosão nunca crita. Um Projétil crita.

**Comprar precisão custa o crítico.** A Melhoria **Certeiro** tira a rolagem de acerto, e a **Inescapável** tira as duas rolagens. Quem paga por elas está trocando 10% de dano médio por não errar nunca — o que é uma escolha boa de montagem, e não um bug.

**Ele vale exatos 10% de dano por rodada.** Contra o alvo difícil, em que se acerta 50%, o crítico transforma `0,50 × dano` em `0,55 × dano`. É o mesmo valor em todo nível, porque a taxa de acerto não deriva.

**O crítico não estoura o teto do manual.** O teto de `4 × Classe em dados` é sobre o que você pode **montar**, não sobre o que o dado pode produzir. Um Classe 7 no teto tem 28 dados; num 20 natural ele rola 56. Isso é variância, não montagem, e o `v7.py` continua valendo como está.

## 5.3 Pontos de energia

*Escrito na v0.26, com o motivo corrigido logo depois.* O PE máximo era usado em três documentos e nunca tinha fórmula. O que existia era a instância do nível 2 na peça 8 — `PE por nível × 2` —, e ela não dá para generalizar sozinha: a vida ao lado dela multiplica por `(nível − 1)` e ainda soma atributo, então as duas leituras óbvias eram plausíveis.

> **Pontos de energia = PE por nível do seu Caminho × o seu nível.**

Sem atributo e sem valor inicial. A parte do atributo é a decisão da seção 9 aplicada: se um atributo somasse PE, ele viraria o atributo obrigatório de todo conjurador pela porta dos fundos. A parte do valor inicial é o que faz esta ser a única reserva do sistema que passa pela origem — e é o que torna a conta de mesa mais curta que a da vida.

**O manual concorda, e vale saber exatamente o quanto isso é argumento.** A tabela dele — *"quantas vezes você lança o seu melhor feitiço"* — é `6 × nível` nos seis pontos que mostra:

| nível | 1 | 5 | 9 | 13 | 17 | 20 |
|---|---|---|---|---|---|---|
| PE total, no manual | 6 | 30 | 54 | 78 | 102 | 120 |
| `6 × nível` | 6 | 30 | 54 | 78 | 102 | 120 |

Uma primeira redação desta seção dizia que *"a fórmula já estava no manual"* e que ela *"não é escolha nossa"*. **Isso dá ao manual uma autoridade que ele não tem.** Os limitadores e exemplos dele foram calibrados quando o sistema em volta era outro, e o Mizuki é explícito sobre isso: servem de base para continuidade, não de verdade. A escolha é nossa; o valor do manual é que ele **não contradiz**, o que significa que a coluna de "quantas vezes você lança" continua dizendo a verdade sobre a ficha sem precisar ser refeita.

**Se um dia o PE por nível de um Caminho mudar, a coluna do manual muda junto** — e é isso, e não uma tabela vencendo a outra, que o `conferir-manual.py` está lá para não deixar passar em silêncio.

**É a única reserva do sistema que é uma linha reta.** A vida tem um valor inicial e soma atributo; a Integridade tem um valor inicial. O PE não tem nem um nem outro — ele é a taxa vezes o nível, e passa pela origem.

Isso tem um efeito pequeno e que vale saber: como a vida perde um nível na parte que escala (`nível − 1`) e o PE não, a razão entre os dois **sobe devagar** ao longo da campanha. Num Emanador de Constituição 3 ela vai de 0,75 no nível 2 a 0,85 no 30; num Bastião, de 0,32 a 0,39. O personagem alto nível tem proporcionalmente mais combustível do que couro do que tinha no começo — pouco, e sempre no mesmo sentido.

*Uma versão desta seção dizia que o PE "cresce mais rápido que a vida". Não cresce: o passo do PE é 4 a 6 por nível e o da vida é 7 a 10 com Constituição típica. O que sobe é a razão, e não o passo — é a lição da v0.19 aparecendo pela quinta vez, com o número certo contra a base errada.*

| | nv 2 | nv 6 | nv 10 | nv 14 | nv 18 | nv 22 | nv 26 | nv 30 |
|---|---|---|---|---|---|---|---|---|
| Bastião | 8 | 24 | 40 | 56 | 72 | 88 | 104 | 120 |
| Vanguarda · Guia | 10 | 30 | 50 | 70 | 90 | 110 | 130 | 150 |
| Evocador · Emanador | 12 | 36 | 60 | 84 | 108 | 132 | 156 | 180 |

## 5.4 Arredondamento

*Escrito na v0.26.* O material fala em "25% do máximo", "metade do máximo" e "metade do dado" em quatro lugares, e nunca disse para que lado arredondar. Cai em fração em boa parte das fichas — no nível 2, a Vanguarda e o Guia já caem na **primeira parada da primeira sessão**, com 2,5 de PE no descanso curto.

> **Arredonde sempre para o lado que não te favorece.**
> O que você **paga** sobe. O que você **ganha** desce. E o que você ganha nunca fica abaixo de 1.

Uma frase, sem exceção e sem tabela. Ela é escolha nossa, e o que faz dela a escolha certa é que o manual **já pensa assim** — a caixa *"na dúvida, para que lado errar"* diz *"os dois erram pro mesmo lado: o que não infla o feitiço"*. Isso é princípio de desenho, não número calibrado, e princípio envelhece bem melhor que tabela. Aplicado a número em vez de a preço, dá exatamente a frase acima.

E ela reconcilia os dois precedentes que estavam brigando. O manual arredonda **para cima** duas vezes — o preço de Melhoria (*"Leve custa metade da Classe… arredonde pra cima"*) e o +50% de PE da Liberação Máxima —, e os dois são coisas que você **paga**. O exemplo da peça 10 arredonda **para baixo**, sem dizer, e é recuperação. Os dois estavam certos; faltava a frase que explica por quê.

**A regra vale para a conta que você faz na mesa, e não para número que já está numa tabela.** A distinção importa por causa de um caso: a **vida por nível do Caminho** é a média do dado arredondada para cima — o d12 vira 7, o d8 vira 5, o d6 vira 4 — e isso é um ganho subindo. Não é exceção à regra; é que aquele número foi decidido na hora de montar a tabela, e desde então ele é só um valor que você copia. A regra existe para quando a conta cai na sua mão.

**O mínimo de 1 é sobre arredondamento, e não sobre regra.** Quando a regra diz que você recupera **nada** — o degrau 3 de exaustão fora de ambiente propício —, ela diz nada. O piso existe para o caso em que a conta produziu 0,4, não para desfazer um zero escrito.

## 5.5 Inconsciente — quando a vida acaba

Esta é a pergunta nº 5 do `pitch-de-design.md`, aberta desde a v0.1: *"como o sistema trata morte? JJK é letal; server de guilda com personagem persistente normalmente não é."*

**Metade dela já estava respondida, e a outra metade não tinha uma linha escrita.** Vale separar as duas, porque o corte decide quem manda em cada uma:

| | quem decide |
|---|---|
| **O registro** — a morte cola nesta mesa? | **o mestre**, na abertura. É a trava 6 do `arquitetura.md`, e ela fica como está |
| **A máquina de estado** — o que acontece a 0 de vida | **o sistema.** Zero ocorrências no projeto e no manual antes desta seção |

O próprio esqueleto justifica a trava 6 dizendo que *"o filtro existe para impedir discricionariedade **nos números**; na ficção é trabalho do mestre"*. **Cair a 0 é número** — muda se você continua com o personagem. Então o registro fica por mesa e a máquina de estado é igual em todas.

### A regra

> **Você chega a 0 de vida. Escolha uma das duas, na hora:**
>
> **Aguentar** — você apaga. Tem uma janela de **3 rodadas**. Qualquer cura de 1 ou mais te põe de pé. A janela acabou sem socorro, você chega ao **estágio 4 de dano de alma**.
>
> **Insistir** — você fica de pé a 0 de vida e age normalmente. Cada rodada custa um pedaço da sua **vida máxima**, e ele dobra: **1/8, depois 1/4, depois 1/2**. Na quarta rodada você desaba.
>
> **Quem desaba pelo Insistir não levanta com um ponto de cura.** Só acorda com uma cura de **metade da sua vida máxima original, de uma vez só**.
>
> **Toda vez que você levanta de uma queda, ganha uma Sequela.** Cada Sequela tira uma rodada da janela da próxima queda. **Na segunda queda você também ganha uma Cicatriz**, que é permanente e não sai no descanso.
>
> **Sequela some no descanso longo. Vida máxima e Integridade voltam junto, como sempre.**

### Por que três rodadas, e não outro número

Um combate dura de 3,4 a 4,0 rodadas (seção 8), e você cai, em média, no meio dele. Uma janela de 1 rodada quase nunca dá tempo de alguém chegar; de 4 em diante o socorro deixa de custar decisão. **Entre 2 e 3 é onde a escolha existe** — dá para socorrer, e custa o turno de quem estava lutando.

### Por que o Insistir cobra fração, e não o dano que entra

A versão óbvia era o dano continuar entrando, só que na vida máxima. Ela quebra, e o motivo é que **vida máxima é justamente o eixo em que os Caminhos divergem 3,2×**:

| perfil | rodadas de pé, se o custo fosse o dano que entra |
|---|---|
| Evocador de Constituição 0 | 3,4 |
| Evocador de Constituição 3 | 5,9 |
| **Bastião de Constituição 6** | **11,0** |

O Bastião ficaria de pé onze rodadas num combate de 3,7 — Insistir viraria *"continue lutando, de graça"* para ele e preço real só para quem é frágil. Usar a máxima como relógio importa o espalhamento inteiro para dentro da regra de morte.

**Cobrando fração da própria máxima, a janela fica em três rodadas para todo mundo, em todo nível, sem tabela nenhuma:**

| perfil, no nível 14 | rodada 1 | rodada 2 | rodada 3 | total |
|---|---|---|---|---|
| Evocador de Constituição 0 | 7 | 14 | 29 | 51 |
| Vanguarda de Constituição 3 | 14 | 29 | 58 | 101 |
| Bastião de Constituição 6 | 23 | 47 | 94 | 164 |

O Bastião paga mais em número absoluto e **a mesma fração de si mesmo**. Ninguém é imune e ninguém é punido por ser frágil. E o total é **7/8**: quem insiste termina a missão com um oitavo do corpo.

*O arredondamento é o da seção 5.4 — o custo sobe.*

### As duas escolhas não se dominam

| | ganha | custa |
|---|---|---|
| **Aguentar** | janela de 3 rodadas, e acorda com 1 de cura | fora da luta desde já, 1 Sequela |
| **Insistir** | 3 rodadas **agindo** | 7/8 da vida máxima, 1 Sequela, e só acorda com metade da máxima original |

Nenhum conjunto contém o outro, pelo teste da peça 3. Com cura sobrando no grupo, Aguentar é melhor — é barato de reverter. Sem cura, Aguentar só adia o fim e Insistir compra três rodadas. Se você é o último de pé, Insistir sempre. Se o chefe está quase caindo, Insistir compra exatamente as rodadas que faltam.

**E a trava do despertar se auto-equilibra:** o Bastião é quem mais lucra com Insistir, porque tem mais corpo para queimar — e é o mais caro de trazer de volta, porque metade dele é muito. Uma cura do topo cobre o frágil em toda a faixa e não cobre o Bastião quase nunca. Ninguém fica trancado: duas curas sempre resolvem, e o descanso longo devolve tudo.

### O estado terminal já estava escrito, e era inalcançável

O manual tem os quatro estágios de dano de alma, e o quarto diz: ***"Você não é mais você. O que sobra é decisão do mestre."***

**Isso é a trava 6 com outras palavras** — morte declarada por mesa —, e ninguém nunca chegou nele. A seção 5.1 explica por quê: a alma é maior que o corpo em quatro dos cinco Caminhos, então *"a pessoa cai antes"*. Ligar o fim da janela ao estágio 4 destrava a máquina que já existia, sem inventar estado novo nem contador novo.

### Duas coisas que a conta recusou

**Teste de morte no d20, no molde de três sucessos contra três falhas.** Simulado: **41% a 68% de morte por queda**, conforme a CD. Num server em que o mesmo personagem atravessa cinco a sete mesas, isso põe no dado a decisão que a trava 6 já deu para o mestre.

**Degrau de exaustão por queda.** Existe como regra caseira popular em outros sistemas, e aqui ela cabia — a peça 10 já tem a escada pronta. Mas o degrau 3 da exaustão é *desvantagem em ataque e Teste de Resistência*, e uma missão de quatro lutas com duas quedas já bate o teto. **Isso é espiral de competência: você cai, levanta pior, erra mais, cai de novo.** É o defeito que a v0.8 consertou e que a peça 10 limitou de propósito.

A Sequela é a outra espécie, e a diferença é a peça inteira:

> **Espiral de competência** — levanta pior, e as suas rolagens pioram. Proibida.
> **Espiral de letalidade** — levanta igual, mas a **próxima** queda está mais perto do fim. Suas rolagens nunca mudam.

É por isso que a Sequela encurta a janela em vez de dar penalidade: ela mata o vaivém de cair e ser levantado sem tirar ninguém do jogo. **O alvo certo não era proibir a cura** — o manual diz *"cura sem limite de uso por descanso"*, e o único freio dela é PE. Era fazer a **queda** custar alguma coisa que a cura não devolve.

### Por que a Cicatriz vem na segunda queda, e não na quarta

Porque na quarta ela nunca aconteceria. Com a vida **não voltando no descanso curto** — decisão da peça 10 —, o dano é cumulativo na missão inteira, e ainda assim:

| perfil | quedas por missão padrão |
|---|---|
| Evocador de Constituição 0, o mais frágil que existe | **1,14** |
| Evocador de Constituição 3 | 0,67 |
| Vanguarda de Constituição 3 | 0,58 |
| Bastião de Constituição 6 | 0,36 |

**A primeira queda é o azar normal de uma missão ruim. A segunda é a missão que deu errado de verdade.** Uma regra cujos dentes só aparecem na quarta queda não morde nunca.

### Em aberto nesta seção

- **O que uma Cicatriz é, mecanicamente.** Hoje ela é o registro de que aconteceu. *O conteúdo dela é da peça 19, que existe desde a v0.103 — e o escopo daquela versão foi a régua de condição e as três seções que mudaram de casa, então a Cicatriz continua aberta lá.*
- **Se a Energia Reversa limpa Sequela antes do descanso longo.** *A aptidão **está escrita desde a v0.78**, na peça 11 §6 — com gate e teto.* **O que continua sem dono é se ela limpa Sequela**, e isso é da peça 19, como a Cicatriz acima.
- **`Incapacitado` é condição nomeada no manual**, e o Legado *Corpo Emprestado* a nega com a qualificação *"só por estar ferido"*. Com esta seção escrita, a leitura fica decidida: **`Inconsciente` não é a condição `Incapacitado`**, e o Legado não alcança o `Inconsciente`.
- **E `Inconsciente` também não é `Derrubado`.** *`Derrubado` é condição de nível `Leve` no manual: quem está `Derrubado` está no chão e continua com vida.* **Quem está `Inconsciente` chegou a zero.** *A Manha `Abalo` aplica o `Derrubado`, e nunca este estado.*

## 6. O que a conta produz

O caso difícil é um alvo que **investiu em Destreza** *e* **carrega refino**, então a proteção de cobrir-se dele anda junto: Defesa `14` no nível 2 e `20` no 30.

| quem ataca | nv2 | nv10 | nv18 | nv26 | nv30 |
|---|---|---|---|---|---|
| corpo a corpo, Força investida e treinado | 55% | 55% | 55% | 55% | 55% |
| à distância, Destreza investida e treinado | 55% | 55% | 55% | 55% | 55% |
| conjuração, atributo da técnica no teto | 55% | 55% | 55% | 55% | 55% |

Deriva: **zero ponta a ponta**, e os três empatados. *A oscilação de `5pp` no meio da tabela é irredutível e o §5 explica: a proteção sobe a cada quatro níveis e a maestria a cada oito.*

> *Este bloco dizia `50%` e media contra proteção `1` — a do nível 2, congelada. **Corrigido na v0.117**, e a correção é o que trouxe a maestria para o acerto.*

### Teste de Resistência

Contra um alvo que investiu no atributo do TR:

| | nv2 | nv10 | nv18 | nv26 | nv30 |
|---|---|---|---|---|---|
| **treinado** | 65% | 65% | 65% | 65% | **65%** |
| **sem treino** | 60% | 55% | 50% | 45% | **45%** |

**O treinado não deriva, e o não-treinado deriva de propósito.** *Toda ficha treina dois Testes de Resistência de quatro (peça 7 §6), então toda ficha carrega dois pontos moles que ficam mais moles.* **É o preço de não treinar, e a §5.0 tem a decisão.**

### Perícias — o único lugar onde crescer é o ponto

A escada oficial está na peça 4, seção 2. Treinado e com o atributo investido:

| dificuldade | nível 2 | nível 30 |
|---|---|---|
| CD 10 (rotina) | 75% | 100% |
| CD 14 (fácil) | 55% | 85% |
| CD 18 (média) | 35% | 65% |
| CD 22 (difícil) | 15% | 45% |
| CD 26 (quase impossível) | 0% | 25% |

Aqui a deriva é desejada. Uma fechadura comum é a mesma fechadura; um feiticeiro de nível 30 deve abri-la sem pensar. Perícia é o lugar onde o personagem sente que cresceu, justamente porque o mundo não cresce junto.

---

## 7. O erro que estava aqui, e como ele apareceu

A versão anterior deste documento dizia que o nível cancelava e o validador confirmava. **Estava errado, e o validador tinha um ponto cego.**

Ele testava se a chance mudava com o nível **mantendo os atributos fixos**. Só que numa campanha o defensor não fica com Destreza 3 para sempre — ele investe, e chega a 6. O ataque de conjuração era um valor fixo de 5 mais maestria, e maestria crescia +7 enquanto o atributo do defensor crescia +3. Resultado real:

| modelo testado | deriva na campanha |
|---|---|
| valor fixo sem maestria | −15 pp (conjurador some) |
| fixo + maestria a cada 4 níveis | +20 pp (conjurador vira infalível) |
| fixo + maestria a cada 8 níveis | **0 pp** |

O valor fixo nunca foi o problema. O problema era o **ritmo**. E o conserto não foi tirar o número fixo — foi fazer a maestria andar na velocidade certa, e depois calibrar o fixo em 2 para o conjurador empatar com o guerreiro em vez de ficar 15 pontos percentuais na frente.

**A lição que fica para o resto do projeto:** verificar invariância contra o nível não basta. Tudo que cresce numa campanha precisa entrar no teste — atributo, proteção, equipamento. O validador foi corrigido para variar os atributos junto com o nível.

> **⚠⚠ E ele aconteceu de novo, na mesma seção, com a palavra do meio — v0.117.** *Esta lição lista três coisas que têm de entrar no teste: **atributo, proteção, equipamento**. O conserto da v0.8 trouxe o atributo e parou ali.* **A proteção ficou congelada em `1` por cento e nove versões**, dentro do validador que esta seção existe para explicar. *Enquanto isso a peça 14 §3 derivava o teto de Defesa somando os `4` de cobrir-se no refino `10` — os dois documentos descrevendo o mesmo alvo com quatro pontos de diferença.*
>
> **O que fez a diferença aparecer não foi validador nenhum: foi o Mizuki olhando a Defesa que a mesa alcança e dizendo que ela chega a `20`.** *A frase certa estava escrita aqui o tempo todo, ao lado de um teste que não a obedecia — e uma frase certa ao lado de um teste que a contradiz sobrevive muito mais que uma frase errada.*

---

## 8. Ritmo de combate

A tabela de letalidade do Fundamento mostra 1,7 a 2,0 rodadas porque supõe que **todo ataque acerta**. Ela mede o pico, e o pico é o número errado para preparar encontro. **O manual precisa passar a mostrar as duas colunas**, com a taxa de acerto real marcada como a de mesa.

*Corrigido na v0.15.* Este parágrafo dizia "3,2 rodadas é o alvo, com 65% de acerto". Os dois números estavam errados e não batiam nem entre si: a taxa que o validador entrega contra um alvo que **também investiu em defesa** é **50%**, e o CHANGELOG da v0.8 registrava 60%. Refazendo a conta:

| taxa de acerto | rodadas |
|---|---|
| 65% | 2,6 – 3,1 |
| 60% | 2,8 – 3,3 |
| **50%** | **3,4 – 4,0** |

**A previsão atual é 3,4 a 4,0 rodadas**, contra alvo bem defendido. Contra inimigo comum é menos. Isso fica como número a medir no playtest, não como alvo fechado — quem decide se o combate está arrastado é a mesa.

## 8.1 · 8.2 · 8.3 — as três foram para a peça 19

*As três seções que moravam aqui mudaram de casa na v0.103, e as três já diziam, no próprio texto, que o dono natural era a **peça de dano e condições**.*

**As três eram guarda provisória**, e a guarda acabou quando a peça existiu. *É o mesmo trato que o `ESTADO-ATUAL` faz com vocabulário que ainda não tem peça: enquanto não tem, mora onde couber e com validador em cima; quando tem, vira ponteiro.*

> **E as checagens foram junto.** *Os tipos de dano e as condições eram as duas últimas checagens do `conferir-atributos.py`, e elas estão hoje no `conferir-dano.py`.* **Com isso este validador parou de abrir o `.docx` do manual**, e ele saiu da lista dos que pulam checagem sem o `python-docx`.

> **O que a peça 19 acrescentou às três: um nível para cada condição.** *O manual cobra `Média` por qualquer uma das nove `Menor` e `Pesada` por qualquer uma das cinco `Maior`, e a conta diz que elas valem de `0,00` a `19,73` fatias.* **O nível é `Leve`, `Média` ou `Pesada`, e é ele que diz quanto custa tirar a condição e quanto ela pesa numa entrega de Trilha.**

### 8.1 Os tipos de dano

**Os catorze tipos, em três grupos, com o peso de cada grupo no dano recebido.** *Escritos aqui na v0.74.* **Hoje eles são a seção 4 da peça 19.**

### 8.2 Cobertura

**Os três degraus — Parcial, Boa e Total.** *Escritos aqui na v0.94.* **Hoje eles são a seção 5 da peça 19.**

### 8.3 As condições

**As catorze, com o que cada uma faz e as três que ficam de fora.** *Escritas aqui na v0.95.* **Hoje elas são a seção 3 da peça 19**, e ganharam lá o nível que faltava.

## 9. Em aberto

- ~~**⚠⚠ A troca do `2` por um atributo não tem versão que funcione.**~~ **FECHADO na v0.117:** *o `2 + maestria` morreu, o atributo da técnica entrou no lugar dele, e a maestria passou a somar no acerto para pagar a proteção que cresce do outro lado.* **O `Estopim` do `Explosivo` ganhou referente de graça** — todo mundo passa a ter um atributo de técnica.
- **Se Constituição vira o atributo de técnica de todo conjurador puro.** *Declarado na seção 5, e é pergunta de mesa e não de conta:* o acerto continua em `55%` seja qual for o atributo, mas o segundo trabalho da Constituição vale para todo mundo e o dos outros quatro não.
- **Se Força precisa de um segundo trabalho.** Ela tem uma perícia só, e a lista de vinte e três não conserta isso.
- **Se Constituição virou obrigatória** (seção 5.1). É a pergunta de playtest número um.
- **Se o extremo frágil é frágil demais**: um Emanador de Constituição 0 cai em 1,7 rodadas no nível 30.

*Resolvidos e tirados daqui:* quantos TRs cada personagem treina — **dois de quatro, um da Origem e um do Caminho** (peça 7). O peso de Inteligência, que foi medido na v0.16 e corrigido movendo a percepção para Essência. E **PE cresce só com nível** — a fórmula está na seção 5.3, e a decisão de não botar atributo nela continua valendo pelo mesmo motivo de sempre: um atributo na conta de PE viraria o atributo obrigatório de todo conjurador pela porta dos fundos.

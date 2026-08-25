# Técnica Marcial

**Fase 4, vigésima peça.** A rota de criação de quem não escreve Fundamento — o que ela é, o que ela herda pronto, e as duas formas que ela tem.

*Fechada na v0.122. Ela estava na fila desde a v0.38, quando o Corpo Amaldiçoado saiu do balde da Restrição Celestial, e destravada desde a v0.48, quando Equipamento fechou. O que a segurava por último era a ferramenta amaldiçoada, que virou a peça 16 na v0.59.*

Três peças escreveram pedaços dela sem que nenhuma soubesse. A peça 16 §2 declarou, com todas as letras, que **o dano por rodada da rota sem energia é desta peça** — *"magnitude, e ela é peça"*. A peça 9 §5 fixou o orçamento dela e disse que só o nome da moeda ficava em aberto. E a peça 11 §6.8 escreveu doze Bênçãos com nome, Classe Passiva e gate, e parou porque o texto de cada uma dependia de saber o que esta rota faz numa rodada.

---

## 1. O que ela é, em três linhas

> **Técnica Marcial é o Fundamento com o corpo no lugar da energia.** Mesma máquina, mesmo orçamento, mesma conta de montagem.
>
> **O que muda é a criação:** onde o Fundamento escreve um Selo, ela escolhe **três grupos de arma** ou **uma ferramenta sob medida**.
>
> **E o equipamento é a técnica.** Sem ele na mão, você é uma pessoa com um plano.

A terceira linha é a que faz esta peça caber sem furar nada. O Fundamento paga a identidade dele com um Selo, que não custa ponto e não pode ser vendido como Restrição. Aqui o Selo virou objeto, e o objeto pode ser tirado de você — mesma função, preço de verdade.

## 2. O que ela não decide — três coisas chegam prontas

Esta peça é a que mais chegou com contrato assinado por outras, e vale listar antes de qualquer coisa, para ninguém tentar reabrir.

| o que | quem decidiu | onde |
|---|---|---|
| **o orçamento** — `4` a `6` de PE por nível, pelo Caminho | v0.116 e v0.120 | peça 9 §5, peça 6 §5 |
| **o nome da moeda** — `PE`, lido como `Pontos de Esforço` na rota sem energia | v0.120 | peça 9 §5 |
| **quem entrega ferir maldição** — a ferramenta, e é binário | v0.59 | peça 16 §2 |
| **quem NÃO tem Expansão de Domínio** — quem não tem energia, nunca. *E o §3.2 estende: nem quem tem* | v0.118 | peça 9 §5 |
| **o tamanho do catálogo de Bênçãos** — catorze: duas grátis e doze pagas | v0.116 e v0.118 | peça 11 §6.8 |

**O tamanho do orçamento é herdado e não escolhido, e o motivo é uma soma.** A peça 6 §5 mantém `vida + PE por nível` em `10` nos quatro Caminhos e `11` no Bastião, e é essa soma parelha que faz escolher Caminho ser sabor em vez de degrau de poder. O `conferir-atributos.py` falha se ela variar mais que `2`.

*Se esta peça inventasse um orçamento próprio, a coluna de PE do Caminho valeria zero para essa Origem e a soma iria para `7 · 5 · 5 · 4 · 4` — espalhamento `3`, e o Bastião passaria a entregar `1,75×` o Emanador na única moeda que ainda paga.* **O argumento inteiro, com as três saídas que reprovaram, está na peça 9 §8.**

## 3. A máquina é o Fundamento, e a lista do que muda cabe numa tabela

**Tudo que o capítulo do Fundamento diz continua valendo aqui**, com três renomes e duas subtrações. Pontos são `3 × Classe`, o custo em PE é o mesmo número, o que sobra de ponto vira `1d8` de dano, Melhorias e Restrições obedecem os mesmos tetos, e a lista de espaços é `2 + (nível ÷ 2)` mais um por marco.

| peça do Fundamento | na Técnica Marcial |
|---|---|
| Descrição, com tipo de dano | **igual** |
| Regra — a frase que contorna a técnica | **igual** |
| duas Famílias Livres, três Fechadas | **igual**, e quem justifica são as armas ou a ferramenta |
| **Selo** | **sai.** No lugar dele, o equipamento — §4.3 |
| **feitiço** | **`Kata`** |
| **Liberação Máxima** | **`Ruptura`** |
| **Técnica Máxima** | **`Ōgi`** |
| Passiva Livre e Passivas pagas | **igual** |
| Classe 0 | **igual** |
| Expansão de Domínio | **não existe nesta peça**, e a negação é dela — §3.2 |
| aptidões e refino | **Bênçãos e Lapidação**, para o ramo sem energia — peça 11 §6.8 |

**Não existe número novo nesta tabela, e isso é o desenho e não economia de trabalho.** A peça 16 §2 mediu o buraco que a rota sem energia tem em dano por rodada: no nível 30 a melhor arma do sistema entrega `12,5` contra uma Rotina de `108`, e fechar essa distância pediria `95` de dano por rodada. *Isso é o Fundamento inteiro.* **Então a resposta certa era dar o Fundamento, não construir um segundo motor ao lado dele.**

### 3.1 Os três renomes, e o que cada um continua sendo

> **`Kata`** (型, a forma que se treina). A aplicação concreta da técnica, montada com pontos. É o feitiço com outro nome: mesma Classe, mesmos pontos, mesmo custo, mesmo teto de Melhoria e de Restrição.
>
> **`Ruptura`**. A única Kata que passa do limite de dano contra um alvo só. Uma no nível 10, uma no 20 e uma no 30. `+Classe` em dados, a rodada inteira, `+50%` de PE, e o preço escolhido na hora — `Vazio`, `Sangue` ou `Peso`.
>
> **`Ōgi`** (奥義, a técnica que a escola guarda). O golpe de dano fixo, do nível 17 em diante. Dano pela faixa de nível, orçamento de montagem à parte, `5 × maior Classe` de PE, e não aceita Restrição.

**Os três nomes passaram na triagem nas duas direções.** *`Assinatura`, que era o candidato natural para o `Ōgi`, saiu **OCUPADO**: já é Restrição no manual — "o feitiço deixa uma marca visível que dura 1 hora e aponta para você".*

> **⚠ E o `Kata` carrega uma colisão ACEITA, declarada aqui em vez de esquecida.** *`Kata` é prefixo de **`Katana`**, que é uma das 52 armas, do grupo `Lâmina Longa` — e a rota de arma empunha exatamente essa.* **Na mesa, em voz alta, uma sílaba separa as duas.**
>
> ***Decisão do Mizuki: fica.*** *"A galera vai gostar da referência, não tem problema a colisão."* **É colisão de som e não de sentido:** uma Kata não **é** uma Katana, e o critério da v0.40 é *"se preocupe quando o nome bate de frente com o nome de algo que é REALMENTE aquilo"*.
>
> **A triagem devolvia `LIVRE` por dois buracos, e os dois foram fechados na mesma versão:** *ela era cega para as **52 armas** da peça 14, e o veredito `DENTRO` só olha termo composto com fronteira de palavra — por isso `Fôlego` morreu dentro de `Roubo de Fôlego` e `Kata` sobreviveu dentro de `Katana`.* **Entrou o veredito `prefixo`, que pega esta classe.**

*`Kata` e `Ōgi` vêm com a tradução entre parênteses, que é a regra que a peça 14 §5.1.2 fixou para `Yumi`, `Hankyū` e `Daikyū`: **quem não conhece o termo não pode ficar travado numa linha de tabela.***

> **Por que renomear em vez de reusar.** *A `Liberação Máxima` e a `Técnica Máxima` são as duas coisas do manual que carregam "a sua técnica" no nome, e uma rota que não tem técnica inata usando as palavras da que tem produz a pergunta errada na mesa.* **Renomear custa zero número e compra a leitura de primeira.** *A Expansão não ganhou substituto porque ela não está sendo renomeada: ela não existe aqui.*

### 3.2 A negação da Expansão é desta peça, e não só da Origem

**Isto precisa estar escrito aqui, porque a decisão da v0.118 sozinha deixa um buraco.** *Ela diz que **quem não tem energia** nunca tem Expansão de Domínio, e ela mora na peça 9 §5.* **O Corpo Amaldiçoado tem energia** — cadáver de mutação abrupta produz a própria, uns três meses depois de acordar —, então aquela frase não alcança ele.

***Decisão do Mizuki: a Técnica Marcial não tem Expansão de Domínio, e ponto.*** *Vale para as duas Origens que a usam, tenham energia ou não.*

**O motivo é o que a Expansão é.** *O manual escreve que ela é "a mesma técnica estendida sobre o território em volta", e a tabela de Acerto e Efeito da peça 11 lista nove exemplares da obra — todos são uma técnica inata fazendo o que ela já faz, num lugar em vez de num alvo.* **A Técnica Marcial não tem técnica inata para estender.** *Não existe versão dela que não fosse dano com outro nome, e o dano já está todo gasto.*

> **E o Panda não tem domínio na obra**, que é a leitura de fora concordando com a de dentro.

### 3.3 As Passivas ficaram sem exemplo, e uma rota de corpo precisa dos próprios

*Achado do Mizuki na v0.134, lendo a criação: **"não [há] exemplos de passivas na criação de técnica de sem energia"**.* **A tabela do §3 dizia que Passiva Livre e Passivas pagas ficam `igual`, e parou ali.** *"Igual" resolve a máquina e não resolve o exemplo — os do capítulo do Fundamento são todos construídos em cima de energia amaldiçoada, e quem escreve uma rota de corpo não tem em que se espelhar.*

**A escada não muda:** Classe Passiva `1`, `2` e `3` custam `1`, `2` e `3` espaços de Kata, e o que cabe em cada altura é o que o manual escreve. *A Passiva Livre continua de graça e continua sem número.*

**O que muda é de onde a ficção sai.** *Onde o Fundamento escreve energia, aqui se escreve corpo, treino e ferramenta.*

| Classe Passiva | exemplo | o que ele é |
|---|---|---|
| **Livre** | `Calo` | a sua mão reconhece pelo peso qualquer arma que você já empunhou uma vez |
| **1** | **`Bocado`** | você guarda no corpo o que carrega. *A entrada inteira está abaixo* |
| **1** | `Raiz` | você não é movido à força nem derrubado contra a sua vontade |
| **1** | `Leitura` | você identifica a Classe e a Forma de qualquer feitiço conjurado a até `18 m` |
| **2** | `Segundo Fôlego` | quando você chega a `0` de vida, uma vez por descanso longo você escolhe `Insistir` sem gastar a rodada |
| **2** | `Contragolpe` | uma vez por cena, quando alguém erra um ataque corpo a corpo contra você, a sua próxima Kata contra ele não pode ser evitada por deslocamento |
| **3** | `Aliança` | a sua arma nunca é desarmada, e ninguém além de você a empunha |

> **⚠ Os dois de Classe Passiva `1` do meio já existiam, e é por isso que eles estão aqui.** *O `Raiz` é a Passiva da `Fisga` e o `Leitura` é a da `Bancada`, as duas Técnicas Marciais prontas do §9.* **Elas estavam publicadas dentro de duas fichas e em lugar nenhum como exemplo** — quem lia a criação não passava por elas.

**Nenhum destes é catálogo, e nenhum tem gate.** *Passiva se escreve na hora, com o mestre, do jeito que o Fundamento sempre fez.* **A lista existe para dar altura, e não para escolher.**

#### `Bocado` — Classe Passiva 1

**Ela é a única desta lista que a peça 9 §5 precisa que exista**, e por isso ela é a única escrita inteira aqui.

> **`Bocado`** — o que você carrega passa a viver dentro de você. Sacar é tirar de si.
>
> **Item amaldiçoado guardado no `Bocado` para de emanar energia.** `Barreira Simples` e `Cortina` deixam de segurar ele, e ele atravessa com você.
>
> **E você saca ou guarda DOIS itens de graça por turno**, em vez de um.

**As duas metades são uma coisa só na ficção**, e cada uma tem dono diferente na regra:

| a metade | de onde ela sai |
|---|---|
| **o saque dobrado** | **peça 3 §3.2**, que já decidiu que *"uma Passiva ou aptidão pode dizer que o segundo saque sai de graça, e ela cabe na Classe Passiva 1"*. **Este é o primeiro exemplar dela** |
| **esconder o que emana** | **peça 9 §5**, que abre o buraco: o corpo do restringido atravessa barreira e o equipamento dele não |

> **A altura não foi escolhida — ela estava escrita.** *A peça 3 §3.2 preçou o saque dobrado em Classe Passiva `1` na v0.122, e a metade de esconder é **acesso e não número**: ela não muda rolagem nenhuma e só existe quando alguém levantou barreira.* **Somadas, continuam em `1`.**
>
> **⚠ E ela não é porta dos fundos para a Expansão.** *O Acerto garantido de uma Expansão completa lê **alvo**, e item nunca foi alvo legível* — o que você carrega já atravessava domínio antes desta Passiva existir. **O `Bocado` não muda nada ali, e o texto diz isso para ninguém ler ganho onde não tem.**

> **Os nomes passaram pela triagem, e ela matou dois — um por colisão que ela pega e outro por colisão que ela NÃO pega.**
>
> **`Segunda Natureza` saiu `OCUPADO`: é Passiva no manual.** *A triagem pegou essa sozinha, e o lugar virou o `Aliança`.*
>
> **`Bolso` saiu `LIVRE` e reprovou mesmo assim, por SENTIDO.** *O projeto usa "bolso" para o orçamento de PE em dez lugares — "o bolso já é apertado" —, e a triagem pega substring e não sentido.* **`Bocado` saiu livre nas duas direções e não aparece uma vez em minúscula na pasta.** *Ficam registrados, também livres:* `Coldre`, `Estojo`, `Ninho`, `Alforje` e `Bornal`.

## 4. As duas rotas

Na criação, depois da Descrição e da Regra, você escolhe uma das duas. **A escolha é uma vez e não muda**, como o Caminho e a Trilha.

### 4.1 Rota de arma — três grupos

> **Escolha três das treze categorias de arma da peça 14 §5.1.2, diferentes entre si.**
> **Você recebe uma arma de cada uma, de grau 4** — pela peça 16 §3, grau 4 fere maldição e não dá `Estigma` nenhum.
> **Você é treinado nas três**, seja qual for o balde de acesso delas.
> **As suas Katas valem com qualquer arma amaldiçoada desses três grupos** — a peça específica é substituível, o grupo não.

É a rota da Maki e do Toji: a pessoa que não tem energia e compete porque a ferramenta carrega a energia por ela.

**O treino não é generosidade — é a conta.** *A peça 19 §6 diz que empunhar sem treino custa desvantagem na rolagem, e a peça 14 §5.4 diz que quem concede treino é o Caminho.* **As duas somadas custam `33,8` vezes o que a arma entrega**, que é porta fechada e não preço. *Sem o treino vindo daqui, a rota inteira depende de o Caminho escolhido cobrir por acaso os três grupos que a ficção pediu.*

**A peça específica é substituível e o grupo não, e isso é copiado de uma regra que já existe.** *A `Escola de Arma` da Vanguarda escreve exatamente isso: "a escola é do tipo de arma, e a peça específica é descartável. Se a sua lâmina quebrou no meio da missão e você pegou outra do chão, a Manha continua."*

#### Três grupos não dão Manha, e a conta é o motivo

**A `Escola de Arma` da Vanguarda também escolhe categoria de arma, e ela dá a `Manha` daquela categoria.** *Um leitor que chega aqui vindo de lá vai perguntar se três grupos dão três Manhas, e dois mestres vão responder diferente se ninguém escrever.*

As treze Manhas estão no `DESENHO-manhas.md`, e a média delas é `0,98` fatia:

| se três grupos dessem Manha | fatias | quanto é isso |
|---|---|---|
| as três mais baratas | 2,10 | 70,0% de um Caminho |
| **três Manhas médias** | **2,93** | **97,6% de um Caminho inteiro** |
| as três mais caras | 3,42 | 114,0% de um Caminho |

**Um Caminho custa `3` fatias na campanha inteira, e uma fatia é `5,08` de dano por rodada.** *Três Manhas de graça na criação é um Caminho inteiro de graça, entregue antes do nível 3 — e uma Vanguarda de Técnica Marcial ficaria com quatro categorias.*

> **Os três grupos entregam arma, treino e o Selo. Manha nenhuma.** *Uma Vanguarda desta rota continua escolhendo **uma** categoria na `Escola de Arma`, e pode escolher uma que não seja das três.*

#### Os três começam em grau 4, e a escada continua sendo da peça 16

**Esta peça entrega o degrau de entrada e nada acima dele.** *A peça 16 §7 já publica o ritmo — grau 4 no nível 2, grau 3 por volta do 10, e assim por diante —, e ele continua sendo o dono de tudo que vem depois.*

**O teto de `Estigma` na ficha não se move, e o motivo é que ele conta pelas mãos e não pela mochila.** *A peça 16 §5 escreve "a arma tem teto pelas mãos; o apoio tem teto de duas", e três armas guardadas com uma empunhada continuam sendo uma.*

### 4.2 Rota de ferramenta — um objeto de apoio

> **Escolha uma ferramenta amaldiçoada sob medida, de grau 4, na forma de objeto de apoio** — a categoria que a peça 16 §1 já abre ao lado das 52 armas.
> **Ela não tem dado de arma**, e não precisa ter: as suas Katas nunca somaram o dado do equipamento.
> **Ela declara na criação se o seu golpe simples atravessa por ela** — §6.
> **As suas Katas valem só com ela.**

É a rota do restringido que não é a Maki. Uma armadura construída por engenharia, uma câmera amaldiçoada, um instrumento — a coisa que a pessoa fez porque não tinha o que o resto do mundo tem.

**Ela é onde os atributos mentais moram**, e isso não é escolha de sabor: é o que o §5 mede. *A rota de arma acerta por Força ou Destreza e não tem terceira opção; a de ferramenta declara qualquer um dos cinco.*

> **Se a ficção for armadura, ela É o seu uniforme.** *Não some com o `Traje` nem com o `Revestimento` da peça 14 §3 — ela é um dos dois, e usa os números publicados lá.* **Zero número novo, e é o mesmo molde da `cobrir-se` portada da peça 11 §6.8**, que é a mesma função com outro nome de recurso.

### 4.3 O Selo virou equipamento, e isso paga duas coisas de graça

**O Fundamento escreve um Selo: uma coisa que você sempre faz para conjurar.** *Bater palma, dizer o nome do alvo, estar pisando no chão.* **O Selo não custa ponto, não devolve ponto e não dá bônus.**

**Aqui ele não se escreve, porque a rota já o fixou:** o Selo é ter o equipamento em uso. Nas três armas, ou na ferramenta.

Isso cobra duas regras do manual sem escrever nenhuma:

> **1 · Nenhuma Restrição pode vender "preciso da minha arma".** *O manual já diz que "Restrição que o seu Selo já obriga não devolve ponto".* **Sem essa linha, toda Kata desta rota nasceria com pontos de graça.**
>
> **2 · A Restrição `Gesto` fica quase invendável.** *Ela pede as duas mãos livres, e uma arma de duas mãos ocupa as duas.* **É consequência e não defeito**, e vale estar escrito em vez de o jogador descobrir na montagem.

**E é o Selo que resolve ferir maldição para a rota inteira** — está no §6.

## 5. O atributo, e por que os grupos ficam presos a ele

A peça 1 fixou na v0.117 que **a técnica declara um atributo na criação, qualquer um dos cinco**, e que ele alimenta os dois lados: `d20 + atributo + maestria` no acerto, e `8 + atributo + maestria` na CD.

**Quando o acerto de uma Kata é a rolagem da arma, isso abre três leituras, e duas quebram metade do kit.** *Medido no caso afiado — a arma pede Força e a ficha declarou Inteligência, com Força no teto porque a arma exige e Inteligência parada em `0`.*

| no nível 30 | o seu acerto | o alvo treinado resiste |
|---|---|---|
| a base do sistema hoje | 60% | **65%** |
| declara um atributo, e o acerto usa ele | **35%** | 90% |
| acerto pela arma, CD pelo declarado | 60% | **90%** |
| **os três grupos acertam pelo atributo declarado** | **60%** | **65%** |

> **Só a terceira mantém as duas metades vivas**, e ela não precisa de regra nova: ela é uma trava na escolha dos grupos.

***Decisão do Mizuki:*** **você declara um atributo, e os três grupos têm de acertar por ele.**

**Na prática isso é menos apertado do que parece**, porque a peça 14 §5.1.2 só tem duas respostas para a pergunta *"que atributo acerta com essa arma?"*:

| o atributo | quantos grupos fecham | quais |
|---|---|---|
| **Força** | **8** | Lâmina Longa · Massa · Porrete · Manopla · Machado · Ceifa · Armas Longas · Flexível |
| **Destreza** | **6** | Lâmina Curta · Lâmina Longa · Arremesso · Yumi · Balestra · Arma de Fogo |

*A `Lâmina Longa` aparece nas duas porque a Rapieira e a Katana carregam `Fineza`, e a `Lâmina Curta` inteira é Destreza pelo mesmo motivo.*

> **⚠ E o que isso fecha, declarado: nenhum grupo de arma acerta por Inteligência, Essência ou Constituição.** *A rota de arma é sempre Força ou Destreza.* **Um restringido de Inteligência alta continua sendo ficha legítima — e ele vai pela rota de ferramenta**, que é exatamente a divisão que a v0.118 abriu quando trocou o nome do ramo de `energia pelo corpo` para `sem energia`.

> **⚠⚠ ABERTO na v0.133, e é achado do Mizuki: a trava fecha uma ficha que devia caber.** *"Se não restringe, seria sempre obrigado a usar um atributo só — e aí não teríamos gente que por exemplo quer usar armas de fogo e armas de força."*
>
> **A `Arma de Fogo` é Destreza e o `Machado` é Força, e as duas listas acima não se cruzam nesses dois.** *Quem quer rifle e machado nos três grupos não tem escolha legal hoje: ou os três são de Força, ou os três são de Destreza.*
>
> **A saída que ele propõe é que a Kata acerte pelo atributo DA ARMA**, e ela já está medida na tabela acima como a terceira linha — *acerto pela arma, CD pelo declarado* —, que reprovou com o alvo resistindo `90%`. **Mas a medida foi feita no caso afiado, com o atributo declarado em `0`:** *lá o declarado era Inteligência e a arma pedia Força.* ***No caso do Mizuki os dois são físicos, e a ficha investe nos dois*** — é outro caso, e ele não foi medido.
>
> **O que precisa ser medido antes de mexer:** o acerto de cada arma pelo atributo dela, com a CD saindo do declarado, numa ficha que reparte pontos entre Força e Destreza em vez de encher um. *Se a CD aguentar, a trava vira "o atributo declarado tem de ser um dos que os seus grupos usam" e a ficha do rifle mais machado passa a caber.* **A checagem 4 do `conferir-marcial.py` é a dona desta amarra e muda junto.**

**A rota de ferramenta declara qualquer um dos cinco, e a justificativa é a ficção da ferramenta** — a mesma régua que o Fundamento já usa para aprovar feitiço contra Descrição. *Uma armadura de engenharia acerta por Inteligência; um instrumento que se toca acerta por Essência.*

## 6. Ferir maldição — quem fere o quê

**Uma arma comum não fere maldição.** *A peça 14 §5 registra a decisão que resolve isso para o feiticeiro: `canalizar energia` — a aptidão grátis do refino `1` — já faz arma comum ferir maldição.* **Quem não tem energia não tem essa aptidão, e a v0.118 registrou a dívida com este nome:** *"o `canalizar` em golpe vai ganhar mecânica quando a Técnica Marcial chegar"*.

Ela ganha, e o mecanismo é o Selo:

> **Toda Kata passa pelo equipamento — é isso que o Selo virou.** *E o equipamento é ferramenta amaldiçoada de grau 4.* **Então toda Kata fere maldição, nas duas rotas, sem regra nova.**

**Sobra o golpe simples**, que não é Kata e sai de graça em todo turno.

| rota | o golpe simples |
|---|---|
| **arma** | sai por uma das três, que são grau 4. **Fere maldição** |
| **ferramenta** | é o soco, e soco não fere maldição. **Depende do objeto** |

***Decisão do Mizuki: depende do objeto, e o objeto declara qual é na criação.*** **Uma linha na ficha, escrita junto da Descrição, no mesmo lugar em que o Fundamento anota o tipo de dano.**

> **Coisa que o golpe atravessa** — armadura, manopla, máscara, coturno. O seu golpe simples fere maldição.
> **Coisa que você só carrega** — câmera, lanterna, maleta, instrumento. O seu golpe simples não fere maldição, e as suas Katas continuam ferindo.

> **⚠ E isto só morde numa das duas Origens que usam esta peça.** *O **Corpo Amaldiçoado tem energia amaldiçoada** — peça 9 §5 —, então ele tem aptidões e refino normais, e com eles o `canalizar energia` de graça no refino `1`.* **O golpe simples dele fere maldição pela aptidão, seja qual for o objeto.**
>
> *Ele continua precisando do equipamento, porque o equipamento é o Selo e sem Selo não sai Kata.* **O que ele não precisa é escolher entre os dois tipos de objeto: para ele os dois valem igual.** *A escolha é da Restrição Celestial pelo ramo sem energia, e é ela que paga por não ter aptidão nenhuma.*

### O tamanho da escolha, medido

**Ela vale mais do que parece, e por isso o texto de mesa precisa avisar em vez de deixar o jogador descobrir no nível 7.**

| nível | golpe simples que morre | ataque extra do nível 7 | somado | em fatias | % da Rotina |
|---|---|---|---|---|---|
| 10 | 6,5 | 10 | 16,5 | **3,25** | 36,7% |
| 18 | 8,5 | 11 | 19,5 | **3,84** | 25,7% |
| **30** | 10,5 | 12 | **22,5** | **4,43** | **20,8%** |

*O ataque extra do nível 7 é um golpe simples que sai na Ação de Atacar — peça 6 §3.1 —, e ele é o degrau que os cinco Caminhos recebem de graça naquele nível.* **Uma Vanguarda que escolha um objeto que o golpe não atravessa perde `4,43` fatias contra maldição no nível 30**, quando uma Trilha inteira vale `5,00`.

> **Fica como armadilha avisada e não como porta fechada, e isso é o jeito da casa.** *O manual faz igual com o atributo da técnica: "apontar para um atributo que você não pretende pagar é a armadilha desta página".* **O aviso: se o seu objeto é do tipo que você só carrega, Bastião e Vanguarda ficam caros — os dois pagam metade do que entregam em golpe simples.**

**E perder o dado de arma, sozinho, custa quase nada.** *Segurando o atributo, a diferença entre o `d12` de uma arma de duas mãos e o soco pela maestria é `1,0` de dano por rodada no nível 30 — `0,20` fatia.* **O soco tem dado próprio, na peça 14 §5.0.6.** *O que custa é a porta, não o dado.*

## 7. O `Desarmado`, que é o preço de tudo isso

**Pôr o Selo num objeto põe a ficha inteira atrás de uma condição de nível `Leve`.** *O `Desarmado` da peça 19 vale `3,45` de dano por rodada — `0,68` fatia — porque ele foi preçado contra uma ficha em que a arma é uma fonte de dano entre outras.*

Contra uma marcial de arma única, ele apagaria a Kata junto:

| nível | maior Classe | Kata cheia | em fatias | contra o preço publicado |
|---|---|---|---|---|
| 2 | 1 | 13 | 2,56 | 3,8× |
| 9 | 3 | 40 | 7,87 | 11,6× |
| **17 a 30** | **5** | **67** | **13,19** | **19,4×** |

> **`19,4×` contra um filtro de dominância que reprova a partir de `3,00×`.** *Uma condição `Leve` valeria mais que qualquer Melhoria `Pesada` do catálogo, e valeria isso contra uma Origem só.*

**O desenho já tem a resposta, e ela é o motivo mecânico de os grupos serem três.**

> **Rota de arma:** a Kata vale com arma de **qualquer um dos três grupos**. O `Desarmado` tira uma; sobram duas, e a ficha não para.
> **Rota de ferramenta:** objeto de apoio não ocupa a mão de arma, e o `Desarmado` não alcança ele.

**Nas duas, o `Desarmado` volta a valer os `0,68` fatia que a peça 19 publica.** *A trava está no §4.1 — "três categorias, diferentes entre si" — e ela não é decorativa: com uma só, esta peça sozinha quebraria a régua de condições.*

> **⚠ O que continua sem preço, e não é desta peça: quanto custa sacar a outra.** *A peça 3 §3.1 lista doze ações e nenhuma delas é sacar arma, e o próprio texto do `Desarmado` já diz "até pegar de volta" sem dizer quanto custa pegar.* **É buraco antigo e uniforme para todo mundo** — o que mudou é que agora existe uma ficha que depende dele. *Marcado no §11.*

## 8. O que ela devolve a três peças que a esperavam

### 8.1 O `Leque` volta, e três documentos dizem que ele não tem onde cair

**A peça 11 §6.8 escreve que a rota sem energia perde um dos três eixos do marco**, porque o `Leque` compra `+1 feitiço e uma Passiva` e as duas coisas são do Fundamento. *Escreve também que a linha de graça perde o `+1 espaço de feitiço`.*

**As duas frases eram verdade quando foram escritas e deixam de ser aqui.** *Esta rota tem lista de Katas, tem Passivas e tem espaços — então o `Leque` tem onde cair e o espaço de graça também.*

> **O marco dela volta a ter três eixos: `Corpo`, `Lapidação` e `Leque`.** *Nenhum número se move — o `10` de picks que a rota pura de Lapidação precisa continua saindo dos sete marcos com os três últimos levando duas, e ele mora no §3 da peça 11.*

*O que se move é a pressão:* **aquela peça registra que "a rota sem energia é empurrada para a Lapidação mais forte do que uma ficha comum é empurrada para o Refino, porque ela não tem um segundo eixo de poder para onde ir".** *Ela tem.*

### 8.2 O argumento da Expansão vira falso, e a decisão continua de pé

**A peça 9 §5 e a peça 11 §6.8 justificam negar a Expansão de Domínio assim:** *"a Expansão é comprada com espaço de feitiço, e esta rota não tem lista de feitiço para gastar — então a negação não custa nada a ela"*.

**Com lista de Katas, negar passa a custar.** *A incompleta custa `2` espaços e a completa `3`, e ela agora teria de onde tirar.*

> ***A decisão não muda, e o motivo é que ela nunca foi de preço.*** *Decisão do Mizuki na v0.118, com a frase registrada:* **"é realmente só algo da obra que infelizmente tem de ser adaptado e vai ser meio fortinho mesmo".**
>
> **O que muda é o argumento embaixo dela, em dois lugares.** *Ele passa a ser: a rota atravessa barreira de energia e não é alcançada pelo Acerto garantido de uma Expansão completa, e o que ela paga por isso é não ter a camada.* **Troca declarada, e não conta que fecha.**

*Fica escrito porque argumento errado envelhece pior que argumento nenhum: daqui a dez versões alguém rederiva a decisão pela frase antiga, acha que ela virou falsa, e reabre.*

### 8.3 As doze Bênçãos podem ganhar texto

**A peça 11 §6.8 fecha dizendo que "o texto das doze" espera esta peça, e o motivo é a magnitude.** *Sete das doze já tinham bloco de regra escrito na v0.118; cinco tinham só a linha da tabela.* **Com esta peça fechada, as cinco ganham texto lá — o dono continua sendo aquela seção, e esta aqui não repete nenhuma.**

## 9. Dois exemplos, um de cada rota

**Eles param onde a criação para** — Descrição, Regra, Famílias, rota e Passiva. *`Ruptura` e `Ōgi` não aparecem porque só chegam nos níveis 10 e 17, e são escritas na hora.*

### Fisga — rota de arma

| | |
|---|---|
| **Descrição** | Ela não aprendeu nada elegante. Aprendeu a segurar peso, a alcançar mais longe do que o braço dela alcança, e a não largar. O que ela faz com uma arma é o que qualquer um faria, feito rápido demais para dar tempo de responder. Tipo de dano: corte. |
| **Regra** | *"Alcançar antes, e não soltar."* |
| **Atributo** | Força |
| **Grupos** | Armas Longas · Ceifa · Flexível |
| **Livres** | Alcance · Controle |
| **Fechadas** | Amparo · Auxiliares · Área |
| **Passiva** | `Raiz` (Classe Passiva 1): você não é movido à força nem derrubado contra a sua vontade |

*Os três grupos fecham em Força, e os três carregam `Alcance` e `Emaranha` — é isso que justifica as duas Famílias Livres.* **Amparo fechada porque nenhuma das três cura ninguém**, e é o caso que o §4.1 descreve: *as armas são a régua que o mestre lê.*

### Bancada — rota de ferramenta

| | |
|---|---|
| **Descrição** | Ele nasceu sem nada e leu tudo. A armadura é dele: fez, refez, e conhece cada solda. Ela não tem energia amaldiçoada nenhuma dentro — o que ela tem é a maldição que ele prendeu no chassi e um sistema que ele entende melhor que o fabricante entenderia. Tipo de dano: impacto. |
| **Regra** | *"Resolver o problema com a peça certa."* |
| **Atributo** | Inteligência |
| **Ferramenta** | uma armadura de corpo inteiro. **Coisa que o golpe atravessa** — os punhos dela são dele |
| **Livres** | Auxiliares · Amparo |
| **Fechadas** | Área · Marca · Castigo |
| **Passiva** | `Leitura` (Classe Passiva 1): você identifica a Classe e a Forma de qualquer feitiço conjurado a até 18 m |

*A armadura é o `Revestimento` da peça 14 §3, com os números publicados lá — não é proteção nova.* **`Amparo` é Livre porque a ficção aguenta**, e é o caso que a rota de ferramenta abre: *uma arma que cura é difícil de justificar, e uma bancada de engenharia não é.*

> **⚠ Os dois nomes passaram na triagem, e o primeiro deles quase entrou errado.** *`Talhe` foi o candidato original da rota de arma, saiu **`LIVRE`**, e **já é Legado do Feto na peça 13** — "uma vez por cena, você não fica `Agarrado`".*
>
> **Medido: `77` de `97` nomes de Legado saem `LIVRE` na triagem.** *Ela lê primeira coluna de tabela do manual e o vocabulário batizado das peças, e o catálogo da peça 13 não entrava em nenhum dos dois.* **É a mesma classe de buraco que a v0.88 achou com as condições do manual, e ele foi fechado nesta versão** — `conferir-nomes.py`, com guarda de contagem.
>
> *`Fisga` foi conferido depois do conserto, e por `grep` também: zero ocorrências nas peças e nos três `DESENHO`.*

## 10. O que o validador confere

O `conferir-marcial.py` roda **treze checagens**, e nenhum valor de regra fica escrito dentro dele: orçamento, fatia, Rotina, condição e escada de grau saem dos documentos donos.

| # | o que ela confere | de onde ela lê | o teste negativo |
|---|---|---|---|
| 1 | o orçamento é o `PE` do Caminho, sem número próprio | peça 6 §5 · peça 9 §5 | inventar uma moeda aqui acende |
| 2 | a soma `vida + PE` continua parelha com esta peça em cima | peça 6 §5 | zerar a coluna acende o espalhamento `3` |
| 3 | três grupos, diferentes entre si, e nenhuma Manha junto | `DESENHO-manhas.md` | dar Manha acende `2,93` fatias contra um Caminho de `3,00` |
| 4 | os grupos acertam pelo atributo declarado | peça 14 §5.1.2 | um grupo fora do atributo acende a queda de acerto ou de CD |
| 5 | nenhum grupo acerta por Inteligência, Essência ou Constituição | peça 14 §5.1.2 | um grupo mental na rota de arma acende |
| 6 | a máquina não tem número próprio nenhum | manual, via peça 11 | um `d8` ou um preço escrito aqui acende |
| 7 | os três renomes existem e o original sumiu desta rota | esta peça §3.1 | `feitiço`, `Liberação Máxima` ou `Técnica Máxima` vivo aqui acende |
| 8 | a Expansão não é alcançável por esta rota | peça 9 §5 | um caminho de compra acende |
| 9 | o `Desarmado` não passa do filtro de dominância | peça 19 · peça 17 | grupos em número menor que dois acende `19,4×` |
| 10 | ferir maldição continua sendo da ferramenta | peça 16 §2 | esta peça entregando a porta sem ferramenta acende |
| 11 | o teto de `Estigma` na ficha não se moveu | peça 16 §5 | contar as três armas como três `Estigma` acende |
| 12 | triagem de todo nome que a peça cria | o manual | nome colidindo acende |
| 13 | o `Bocado` entrega **um saque a mais** que a base, e não um número próprio | **peça 3 §3.2** | mexer num dos dois lados sozinho acende |

> **A checagem 13 mede RELAÇÃO e não constante.** *Ela não guarda o `2` do `Bocado`: ela lê quantos saques a peça 3 §3.2 dá de graça hoje e quantos a Passiva entrega, e exige que a segunda seja a primeira mais um* — que é o que *"o segundo saque sai de graça"* quer dizer. **Mudar os dois lados de forma coerente fica verde de propósito.**

**A checagem 3 e a checagem 9 se medem por eixos opostos, e o par fica declarado.** *A 3 pergunta se a rota recebe demais; a 9 pergunta se ela é frágil demais.* **Uma rota com um grupo só passaria na 3 com folga e reprovaria na 9**, e é por isso que as duas precisam existir juntas.

## 11. O que ela destrava, e o que fica em aberto

| destrava | como |
|---|---|
| **Corpo Amaldiçoado** | PE, aptidões e refino normais, e Técnica Marcial no lugar do Fundamento |
| **Restrição Celestial · sem energia** | Técnica Marcial mais Bênçãos e Lapidação |
| **as rotas de Origem** | **6 de 9 → 8 de 9** |
| **o texto das doze Bênçãos** | a magnitude que a peça 11 §6.8 esperava |
| **1 vaga de `Desliga`** | a da Restrição Celestial, na peça 13 §8 |

**O que ela não destrava: Sem Técnica.** *Decisão do Mizuki: aquela rota tem criação própria e vem depois.* **A peça 9 §6 continua mandando ela para Aptidão ou Estilo da Sombra.**

**Em aberto:**

- **Quanto custa sacar uma arma.** *A peça 3 §3.1 tem doze ações e nenhuma é essa, e o `Desarmado` da peça 19 diz "até pegar de volta" sem preço.* **É buraco daquelas duas peças e não desta**, e ele é uniforme para todo mundo — o que mudou é que a rota de arma depende dele para o §7 funcionar como escrito.
- **A vaga de `Desliga` do Corpo Amaldiçoado.** *Ela é a única que sobrou na peça 13: a outra fechou na v0.132, com o `Conhecido`.* **Esta não espera peça nenhuma desde a v0.122** — ela esperava esta aqui —, e não fechou junto porque alvo de `Desliga` é escopo da peça 13.
- **Nenhuma Kata publicada.** *Esta peça entrega a máquina e dois Fundamentos de exemplo; ela não abre catálogo de Kata pronta, do mesmo jeito que o manual entrega três Fundamentos prontos e não uma lista fechada de feitiços.*
- **O texto de mesa.** *Como toda peça de `03-mecanica/`, esta é nota de design.* **O capítulo do livro sai dela, e é lá que a armadilha do §6 precisa aparecer onde o jogador escolhe** — não numa seção de argumento.

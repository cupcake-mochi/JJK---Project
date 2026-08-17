# 17 · Catálogo de entregas

*Escrita na v0.85. Ela é a décima sétima peça, e a primeira que não escreve regra nenhuma.*

## 1. O que esta peça é, e o que ela não é

Todo degrau que um personagem ganha por **Caminho**, por **Trilha** ou pela **Escola de Arma** mora hoje num dos três `DESENHO-*.md` da raiz. Eles têm o preço em fatias, o argumento de por que o número é aquele, e o texto que o mestre lê na mesa.

O que eles não têm é **quantos são**.

Esta peça é o índice. Ela responde três coisas e só três: **quantas entradas existem, como cada uma se chama, e onde o texto dela mora.**

> **Ela não guarda preço e não guarda texto de mesa.** Os dois continuam sendo dos `DESENHO-*.md`, que são os donos. Copiar qualquer um dos dois para cá seria a lição nº 9 do `README` — um número em dois documentos vai divergir — cometida pelo documento que existe para impedir isso.

**Por que ela existe.** Até a v0.84 nenhum validador alcançava os `DESENHO-*.md`. O preço da falta está medido: o nível 27 da `Estocada` passou três versões com a tabela dizendo *"se o feitiço acertou"* e o bloco de regra dizendo *"carrega **sempre**"* — `1,33` fatia contra `5,31`, quatro vezes o valor, numa Trilha cujo orçamento inteiro é `5,00`. **A mesa lê o bloco.** Com esta peça o `conferir-catalogo.py` ganha porta de entrada nos três arquivos, e aquela contradição vira vermelho.

## 2. A regra de contagem

Ela não estava escrita em lugar nenhum, e é por isso que a contagem publicada divergia da contada. **Uma entrada é uma coisa que o jogador ganha num nível.** As duas bordas:

> **Rota conta separado.** Se a escolha vale a campanha inteira e produz uma ficha diferente, cada rota é uma entrada própria em cada nível.
> **Menu dentro de um degrau não conta separado.** Se a escolha é de uma linha, dentro de um degrau que todo mundo daquele Caminho recebe igual, o degrau é uma entrada só.

**O que cai de cada lado:**

| o caso | conta como | por quê |
|---|---|---|
| as três rotas do `Batedor` | **12** — três rotas × quatro níveis | a rota se escolhe no nível 2 e vale a campanha. **A matriz da Vanguarda já entra com cinco linhas e não três** justamente porque as três são fichas diferentes |
| a `Pegada` do `Executor` | **4** | a lista de estilos é menu de um degrau. Quem escolhe estilo continua sendo um `Executor` |
| a `Sintonia` do Evocador | **4** | mesma forma da `Pegada` — `Presa`, `Casco` e `Voz` são três linhas de um degrau, não três Trilhas |
| a `Escola de Arma` da Vanguarda | **1 degrau + 13 Manhas** | o degrau é um; as Manhas são catálogo próprio, e por isso elas têm seção separada aqui |

*Sem essa regra a contagem não fecha duas vezes seguidas do mesmo jeito, e foi o que aconteceu: a v0.84 publicou `48` entregas com a divisão `Estocada 4 · Batedor 8 · o resto 5`, e recontando dos arquivos sai outra divisão com o mesmo total. **Total que fecha por caminhos diferentes é total que ninguém está conferindo.***

## 3. As 56 entregas de Trilha

Doze Trilhas escritas, e o `Batedor` entra com as três rotas abertas. **As três do Evocador — `Servo`, `Matilha` e `Coro` — não entram**, porque estão paradas desde a v0.82 e não têm entrega escrita; quando voltarem, entram aqui.

Todas moram em **`DESENHO-trilhas.md`**, na seção mecânica da Trilha.

### Bastião — 4 com nome, 8 sem

| Trilha | 2 | 11 | 19 | 27 |
|---|---|---|---|---|
| **`Muro`** | `Alicerce` | — | — | — |
| **`Punho`** | `Engate` | — | `Tropel` | — |
| **`Brasa`** | — | — | — | `Fornalha` |

### Vanguarda — 9 com nome, 11 sem

| Trilha | 2 | 11 | 19 | 27 |
|---|---|---|---|---|
| **`Estocada`** | — | — | — | — |
| **`Batedor` · `Yumi`** | `carregar` | `Mirar` | — | — |
| **`Batedor` · `Besta`** | — | `Mirar` | — | — |
| **`Batedor` · `Arma de Fogo`** | — | `Mirar` | `Quick Draw` | — |
| **`Executor`** | `Pegada` | `Aprumo` | `Revide` | `Retomada` |

> **O `Mirar` aparece em seis destas casas, e até a v0.85 ele não tinha regra em lugar nenhum.** *Este índice foi quem achou: treze menções no desenho, todas concedendo, nenhuma definindo.* **Escrito na v0.86** — Ação Bônus, vantagem no próximo tiro, e só se você não se deslocou nem vai se deslocar. *A regra mora no `DESENHO-trilhas.md`, na seção `A ação Mirar`, antes das três rotas.*
>
> **O nome continua devendo.** *A triagem devolve `Mirar` como `fraco`: ele está a uma letra de `Mira`, que é Família no manual.* **Isso é dívida de nome, e ela é separada da de regra, que fechou.**

### Guia — 12 com nome, 0 sem

| Trilha | 2 | 11 | 19 | 27 |
|---|---|---|---|---|
| **`Elo`** | `Nó` | `Repasse` | `Partilha` | `Trança` |
| **`Sutura`** | `Agulha` | `Enxerto` | `Pulso` | `Cerzido` |
| **`Perímetro`** | `Chão` | `Sentinela` | `Encalço` | `Portão` |

*O único Caminho com as três Trilhas fechadas em nome e em texto de mesa, desde a v0.84.*

### Emanador — 9 com nome, 2 sem, 1 vaga

| Trilha | 2 | 11 | 19 | 27 |
|---|---|---|---|---|
| **`Torrente`** | `acelerar` | — | `Mão Firme` | — |
| **`Explosivo`** | `Pavio` | `Estopim` | `Rompante` | `Ápice` |
| **`Arremate`** | `Empunhadura` | `Rebote` | `Crosta` | **vaga** |

> **A vaga do `Arremate` é a única do sistema, e ela é deliberada.** *Sobram `1,26` fatia ali.* **Nomear degrau vazio seria escrever entrada para fechar contagem, que é exatamente o defeito que a régua da peça 13 §5 nasceu para achar.** *Ela conta como entrada e não conta como nome — as duas coisas ao mesmo tempo, e é por isso que o total tem três colunas em vez de duas.*

## 4. Os 20 degraus de Caminho

Cinco Caminhos, quatro degraus cada, em `2 · 7 · 15 · 30`. Todos com nome. Moram em **`DESENHO-caminhos.md`**.

| Caminho | 2 | 7 | 15 | 30 |
|---|---|---|---|---|
| **Bastião** | `Corpo Duro` | Ataque extra | `Puxar Para Si` | `Segurar` |
| **Vanguarda** | `Escola de Arma` | Ataque extra | `Não Cede` | `Não Acabou` |
| **Guia** | `Guiar` | `Mão na Roda` | `Puxar a Linha` | `Ninguém Cai` |
| **Emanador** | `Sangria` | `Resquício` · `Modelagem` | `Segunda Leitura` | `Fonte` |
| **Evocador** | `Sintonia` | `Coleira` | `Escudo de Osso` | `Segundo Corpo` |

**Duas irregularidades de forma, e as duas ficam declaradas em vez de alisadas.**

O nível 7 do Bastião e o da Vanguarda são **a mesma coisa** — o ataque extra, que a peça 6 §3.1 concede — e não uma entrega própria de cada Caminho. E o nível 7 do Emanador carrega **duas** entregas com nome no mesmo degrau.

*O degrau continua sendo a unidade: são vinte, e não vinte e um nem dezenove.*

## 5. As 13 Manhas

Uma por categoria de arma, todas com nome, todas em **`DESENHO-manhas.md`**, na seção *"O catálogo"*.

`Talho` · `Raspão` · `Abalo` · `Tranco` · `Encaixe` · `Racho` · `Gancho` · `Espeto` · `Laço` · `Palmo` · `Zunido` · `Prego` · `Estampido`

> **Elas são a única das três famílias sem bloco de regra separado.** *O texto de mesa delas é a coluna `o que faz` da própria tabela de preço.* **Então a checagem de "tabela e bloco batem" não tem o que comparar aqui** — e isso é propriedade do formato, não dívida.

## 6. Os totais

| família | entradas | com nome | sem nome | vaga |
|---|---|---|---|---|
| entregas de Trilha | **56** | 34 | **21** | 1 |
| degraus de Caminho | **20** | 20 | 0 | 0 |
| Manhas | **13** | 13 | 0 | 0 |
| **total** | **89** | **67** | **21** | **1** |

**Os 21 nomes que faltam, por dono:**

`Muro` 3 · `Punho` 2 · `Brasa` 3 · `Estocada` 4 · `Batedor`/`Yumi` 2 · `Batedor`/`Besta` 3 · `Batedor`/`Arma de Fogo` 2 · `Torrente` 2

*Todas já têm texto de regra. **É nome e triagem, sem buraco mecânico** — fora o `Mirar`, que é buraco de regra e está marcado acima.*

> **Nenhum destes números fica guardado no validador.** *Ele reconta as três tabelas acima a partir delas mesmas e falha se a soma escrita não bater com a contada — o molde da tabela de totais da peça 13, que já tinha envelhecido duas vezes dentro do próprio arquivo antes de alguém contar.*

## 7. O que o `conferir-catalogo.py` confere

Oito checagens. **Nenhuma guarda valor:** os nomes saem das tabelas desta peça e os textos saem dos `DESENHO-*.md`.

| # | a checagem | o que ela pega |
|---|---|---|
| **1** | os totais publicados na seção 6 batem com o contado das seções 3, 4 e 5 | total copiado que envelheceu na primeira edição |
| **2** | `89 = 56 + 20 + 13`, e `89 = 67 + 21 + 1` | as duas somas fecham por caminhos diferentes |
| **3** | todo nome desta peça aparece no `DESENHO` dono dela | entrada renomeada de um lado só |
| **4** | todo nome em degrau dos `DESENHO` aparece aqui | entrada nova que ninguém indexou |
| **5** | toda entrega de Trilha com nome tem bloco de regra escrito | preço sem texto de mesa — o furo que o Guia tinha até a v0.84 |
| **6** | **bloco de regra não contradiz o gate da linha de preço** | **a `Estocada`**: linha de preço com gate e bloco dizendo `sempre` |
| **7** | a contagem de peças e validadores desta pasta é `17` | peça ou validador novo entrando sem os três documentos subirem |
| **8** | todo documento vivo que cita o total concorda com o contado | **esta peça virando a segunda fonte do próprio número** |

**A oitava nasceu de revisão cética contra esta própria peça.** *Escrevendo o `89` no `README`, no `ESTADO-ATUAL`, no `LEIA-ME` e no README da entrega, ele virou cinco cópias — dentro do documento que a seção 1 abre dizendo que não vai duplicar nada.* **Esta peça é a dona do total; os outros quatro são cópia, e agora existe quem compare.** *O `CHANGELOG` fica de fora de propósito: ele é registro histórico, e a entrada da v0.84 tem de continuar dizendo `81` sem falhar nada.*

**A sexta é a que esta peça existe para ter.** Ela lê, de cada linha de preço, se o degrau é condicional — a palavra de gate, ou a taxa abaixo de `100%` — e reprova se o bloco correspondente afirmar que o efeito é permanente. *É estreita de propósito: ela pega a forma da contradição que aconteceu, e não a intenção do texto.*

> **A quinta e a sexta se medem por eixos diferentes**, e isso é regra do arnês desde a v0.63. A quinta pergunta *"existe bloco?"*; a sexta pergunta *"o bloco diz a mesma coisa que o preço?"*. **Apagar o bloco acende a quinta; reescrever o bloco acende a sexta.** Uma checagem só cobriria metade e sairia verde na metade que custou a `Estocada`.

## 8. Em aberto

- ~~**O `Mirar` não tem regra.**~~ **Escrito na v0.86**, e ele estoura o degrau em `4,25` fatias contra `0,80` — *decisão do Mizuki, com o estouro declarado no desenho, no molde do `Punho` e da `Brasa`.* **O que sobrou é o nome**, que a triagem devolve como `fraco`.
- **`Quick Draw` é o único nome em inglês do sistema.** *Nível 19 da rota `Arma de Fogo`.*
- **Duas entregas têm nome em minúscula** — o `carregar` do `Yumi` e o `acelerar` da `Torrente` —, contra as outras trinta e duas capitalizadas. *Contam como nome; a inconsistência fica registrada.*
- **As três do Evocador ficam de fora enquanto estiverem paradas.** Quando voltarem, o total sai de `89` e a checagem 1 acusa até esta peça subir junto.
- **A checagem 6 não alcança as Manhas**, porque elas não têm bloco separado. *Se elas ganharem texto de mesa próprio um dia, ela passa a valer lá também.*
- **Esta peça não preça nada.** Se uma entrega estiver com o preço errado, quem acha é a matriz de dominância do desenho — não o índice.

# RASCUNHO — Caminho, Trilhas e subtrilhas

**Isto é o método e o plano, não a peça.** Ela é a maior coisa que falta escrever — **quinze Trilhas, e ela toca 100% das fichas** —, e é a única da fila em que errar o formato antes de começar custa a peça inteira. Este documento existe para o formato ser decidido **antes**, e não no meio.

Escrito na **v0.54**, com o Mizuki fora. **Nenhuma Trilha é escrita aqui.** O que está aqui é: o que já está travado, o que a conta já responde, o problema de escala com número, e as perguntas na ordem em que uma trava a outra.

**Na v0.55 a Q1 e a Q4 fecharam** — sem multiclasse, e as entregas de nível alto cruzam Trilhas do mesmo Caminho. **Na v0.60 a Q2 fechou**, junto com o calendário e o fim da palavra `subtrilha`. **Sobram a Q3 e a Q5**, e a Q3 é a que decide se esta peça custa uma versão ou seis.

> **Duas coisas deste documento estavam erradas e foram corrigidas na v0.60. Leia isto antes do §2.**
>
> **1. A tabela de progressão do §2.1 omitiu a escada de Classe.** Uma **Classe nova de feitiço** cai nos níveis **5, 9, 13, 17 e 21** — cinco dos catorze ímpares —, e ela é a maior entrega isolada do sistema. Os níveis que não entregam nada são **nove**, não catorze: `3 · 7 · 11 · 15 · 19 · 23 · 25 · 27 · 29`.
>
> **2. E por isso a recomendação de `2, 10, 18, 26` do §3 caiu pelo próprio argumento dela.** Aqueles são os **quatro níveis mais cheios do sistema**: o nv26 entrega quatro coisas ao mesmo tempo — Classe 7, maestria, dois feitiços e marco —, o nv10 e o nv18 entregam três. O §2.1 cita o D&D 2024 justamente por ele *"não empilhar presente no mesmo nível"*, e a recomendação empilhava em todos.
>
> *A Rotina do §2.2 também mudou: o `126` do nível 30 era leitura da coluna errada do manual, e o valor é `108`. O dono é o manual, e a checagem 4d do `conferir-manual.py` passou a conferir isso.*

---

## 1. O que chega pronto, e não se rediscute

**Os quinze nomes fecharam na v0.24** e o `conferir-nomes.py` falha se algum voltar. **Três por Caminho:**

| Caminho | Trilhas |
|---|---|
| **Bastião** | `Muro` · `Punho` · `Brasa` |
| **Vanguarda** | `Estocada` · `Batedor` · `Executor` |
| **Guia** | `Elo` · `Sutura` · `Perímetro` |
| **Emanador** | `Torrente` · `Repertório` · `Arremate` |
| **Evocador** | `Servo` · `Matilha` · `Coro` |

**E cinco travas duras, cada uma com dono:**

| trava | dono |
|---|---|
| **A Trilha vem no nível 2, e já rende ali.** Ela é identidade, como o Caminho | decisão da v0.27, aplicada na v0.34 |
| **O Caminho não dá dados de dano** — e a Trilha é o Caminho | peça 5 §4, desafiada e confirmada na v0.36 |
| **O que sobra para conceder:** posicionamento, alvo, duração, recuperação, troca do fixo do acerto por atributo, e **exceção estreita e paga na economia de ação** | peça 5 §4 |
| **Você e todas as suas invocações somados entregam uma Rotina** | peça 6 §4 |
| **Ataque extra: Bastião e Vanguarda pelo Caminho no nível 6; `Arremate` e `Coro` pela Trilha; o Guia por nenhuma rota** | peça 6 §3.1 |

**E três das quinze já estão construíveis**, porque o rascunho de Invocações fechou a máquina delas: `Servo` dá um corpo forte, `Matilha` dá os cinco, `Coro` dá a exceção de economia de ação — **e o que a Trilha concede não sai do orçamento da ficha.** *É a metade da Q6 que aquele documento entregou.*

## 2. O que a conta já responde, e não é pergunta

### 2.1 Existe um buraco de progressão, ele tem tamanho, e é onde a Trilha cabe

*O `ESTADO-ATUAL` lista a **tabela de progressão consolidada** como uma das três coisas que não existem — "o que você ganha em cada nível está espalhado por cinco documentos". Montei ela para saber onde a Trilha cabe, e o resultado decide a pergunta sozinho.*

| nível | maestria | feitiços | marco |
|---|---|---|---|
| 2 | 1 | 3 | — |
| 3 | 1 | 3 | — |
| 4 | 1 | **4** | — |
| 6 | 1 | **5** | **marco** · ataque extra do Bastião e da Vanguarda |
| 10 | **2** | **7** | **marco** |
| 14 | 2 | **9** | **marco** |
| 18 | **3** | **11** | **marco** |
| 22 | 3 | **13** | **marco** |
| 26 | **4** | **15** | **marco** |
| 30 | 4 | **17** | **marco** |

> **Catorze dos vinte e nove níveis não entregam absolutamente nada, e são todos os ímpares.** Os feitiços conhecidos (`2 + nível ÷ 2`) cobrem **todo nível par**; a maestria e os marcos caem em cima de níveis pares que já tinham feitiço.

**Isso não é defeito e vira a resposta:** o D&D 2024 padronizou a subclasse em **3, 6, 10 e 14** justamente para não empilhar presente no mesmo nível, e aqui a lacuna é maior e mais regular do que lá. **A Trilha tem onde cair sem competir com nada.**

### 2.2 A entrega TEM de ser escalonada, e não é escolha de densidade

A peça 14 §4 registra a dívida da Trilha da Vanguarda como *"de 6% a 9% da Rotina, e a fração quase não deriva"*. **A fração não deriva; o valor absoluto cresce dez vezes:**

| nível | Rotina | 6% | 9% | em pontos de arma |
|---|---|---|---|---|
| 2 | 13 | 0,8 | 1,2 | 2,4 a 3,5 |
| 10 | 45 | 2,7 | 4,0 | 8,2 a 12,3 |
| **30** | **108** | **6,5** | **9,7** | **19,6 a 29,5** |

> **Uma Trilha que entregue tudo no nível 2 paga a dívida naquele nível e vale `1,1%` da Rotina no nível 30.** É o mesmo formato de falha que o §2.1 do rascunho de ferramenta mediu no ponto de arma: **valor absoluto contra alvo que cresce.**

**Então "quantas entregas por Trilha" não é pergunta de gosto — o mínimo é mais de uma, e a conta é quem diz.** *O que continua sendo escolha é quantas a mais.*

### 2.3 O problema de escala é o maior risco da peça, e ele tem número

Quinze Trilhas multiplicam tudo. **Este é o custo real, medido contra o que este projeto já pagou:**

| entregas por Trilha | níveis | × 15 Trilhas | comparável a |
|---|---|---|---|
| 8 | 2 + os sete marcos | **120** | nada que este projeto já tenha escrito |
| 7 | 2, 8, 12, 16, 20, 24, 28 | **105** | idem |
| **4** | 2, 10, 18, 26 | **60** | peça 13 — 81 entradas, uma versão, com a régua escrita antes |
| 3 | 2, 12, 22 | **45** | entre a peça 11 e a peça 13 |
| 2 | 2, 16 | **30** | peça 11 — 10 entradas, uma versão |

**E o histórico de custo deste projeto, para calibrar:**

| peça | tamanho | custou |
|---|---|---|
| peça 11 — aptidões | 10 entradas compráveis | **uma versão** |
| catálogo de Invocações | 19 entradas | **duas versões** |
| peça 13 — Legados | 81 entradas | **uma versão** — *porque a régua veio primeiro* |
| peça 14 — Equipamento | 52 armas e 12 propriedades | **seis versões**, da v0.42 à v0.48 |

> **A peça 13 e a peça 14 são a lição inteira, e elas discordam de propósito.** Legados escreveu **81 entradas em uma versão** porque a **régua veio antes do catálogo** — e a ordem se pagou na hora: *"os quatro Legados que a régua reprovou eram do catálogo antigo"*. Equipamento gastou **seis versões** porque a régua foi sendo consertada com o catálogo já escrito, e cada conserto envelhecia o que existia.
>
> **Trilhas é maior que as duas.** Escrever entrada antes de a régua fechar é a rota de seis versões, com 60 a 120 entradas em vez de 52.

### 2.4 Duas das três perguntas abertas da peça 6 já têm o conserto nomeado

| pergunta da peça 6 §9 | onde a resposta já está |
|---|---|
| **Como `Torrente` cobra o segundo feitiço da rodada** | *"É o mesmo defeito da seção 4 — mais de uma ação por rodada —, e o conserto que funcionou lá provavelmente serve aqui"*. **E lá ele fechou:** na Q4 de Invocações o teto deixou de ser decreto e passou a **cair da economia de ação**. `Torrente` é a mesma máquina com feitiço no lugar de corpo |
| **O que `Elo`, `Sutura` e `Perímetro` valem contra o golpe por rodada que o Guia não tem** | a v0.36 já respondeu **metade**: *"Guia — **tudo** passa. Auxílio, estender, reposicionar e recuperar são literalmente a lista do permitido"*. O que falta é o **número**, e ele é `6%` a `9%` da Rotina pela peça 14 §4 — a mesma dívida da Vanguarda, no outro Caminho |
| **Quantas Trilhas um personagem acumula, e em que níveis** | **aberta de verdade.** É a Q1 abaixo |

## 3. As perguntas, na ordem em que uma trava a outra

**Q1 — FECHADA na v0.55.** *Decisão do Mizuki:* **Caminhos não se misturam — não existe multiclasse neste sistema.** Uma Trilha por ficha, e a pendência nº 3 do `ESTADO-ATUAL`, aberta desde a v0.22, fecha com ela. **Isso mata as 105 combinações** que eu tinha orçado como o maior risco de matriz da peça.

**Q2 — FECHADA na v0.60.** *Decisão do Mizuki, depois de a conta derrubar a recomendação antiga de `2, 10, 18, 26`.*

> **Entrega de Trilha nos níveis `2 · 11 · 19 · 27`. Entrega de Caminho nos níveis `7 · 15 · 23 · 29`.**
> **80 entradas** — `4 × 15` de Trilha mais `4 × 5` de Caminho — e **405 montagens legais**.

**Os dois degraus não são conceito novo:** a peça 6 §3.1 já escreve *"Bastião e Vanguarda ganham ataque extra no nível 6, **pelo Caminho**; Arremate e Coro ganham **pela Trilha**"*. O que a v0.60 fez foi transformar a distinção existente em calendário.

**E ela resolveu um empate que oito entregas de Trilha não resolviam.** Com seis entregas, todas de Trilha, é impossível ter as duas coisas boas ao mesmo tempo:

| calendário | maior vão da Trilha | pior seca, em missões |
|---|---|---|
| `2, 7, 11, 19, 25, 29` | **8** | 27 |
| `2, 7, 11, 15, 19, 25` | 6 | **37** |
| **misto — T `2,11,19,27` · C `7,15,23,29`** | **5** | **24** |

O misto entrega os dois **e** custa dez entradas a menos, com uma matriz de dominância **nove vezes menor** — porque um degrau de Caminho é igual para as três Trilhas dele e não multiplica nada.

> **A seca foi medida em missão e não em nível**, pela curva da peça 12, porque é a unidade que o jogador sente. Hoje o vão `nv26 → nv30` são **37 missões** sem nada que se escolha, e é o maior da campanha inteira — a seca deste sistema é **no topo**, e não no meio.

*Levantamento externo que decidiu o tamanho do vão:* o problema chama **dead level** no hobby. O D&D 3.5 o remendou com dois artigos de errata em 2007; o Pathfinder 2e o proíbe por princípio declarado; o 4e pagou o oposto, com ficha de nove páginas. **E o 5e de 2014 tinha vãos de 8 entre feitos de subclasse — Paladino `3·7·15·20`, Feiticeiro `1·6·14·18`, Bardo `3·6·14` — que a edição de 2024 tirou todos**, padronizando em `3, 6, 10, 14`.

**Q3 — A régua, e ela vem ANTES do catálogo.** É a lição da peça 13 contra a peça 14, e é a única recomendação deste documento que não é de sabor. A régua de Trilha tem de dizer, antes de qualquer entrada existir:

- **em que formato** uma entrega vem — o projeto tem duas réguas prontas para copiar: as **Classes** da peça 11 (*efeito pequeno · reativo com limite · permanente*) e os **três formatos travados** da peça 13 (`Ajusta` · `Desliga` · `Destranca`)
- **quanto** ela vale, contra os `6%` a `9%` da Rotina
- **o que ela não pode ser** — dado de dano (peça 5 §4), nada que cresça com refino (peça 11 §2), e nenhuma ação a mais por rodada sem pagar na economia de ação (peça 6 §4)

**Q4 — FECHADA na v0.55, e ela devolve metade do que a Q1 tinha economizado.** *Decisão do Mizuki:* **as entregas de nível alto cruzam Trilhas do mesmo Caminho** — o Bastião pega uma do `Muro` e uma do `Punho`, e nunca uma do Guia.

> **A árvore, fechada — e são DUAS camadas, não três:**
> **`Caminho`** (5, exclusivo, escolhido na criação) → **`Trilha`** (3 por Caminho, escolhida no nv2).
> No nível **2** você pega a entrega da **sua** Trilha. Nos níveis **11, 19 e 27** você pega a de **qualquer** Trilha do seu Caminho.

> **A palavra `subtrilha` morreu na v0.60, e a mecânica ficou inteira.** *Decisão do Mizuki, e o motivo foi ele mesmo se perder lendo a árvore — que é o teste que importa.* `Caminho → Trilha → subtrilha` fazia parecer **três andares** quando são **dois com um empréstimo**: a coisa que você pega no nível 11 não é uma camada abaixo da Trilha, é a **mesma camada**, tirada de um vizinho do mesmo Caminho.

**O que isso custa está medido, e é o número que a régua tem de aguentar:** a matriz de dominância deixa de varrer as 15 Trilhas e passa a varrer **as combinações de subtrilha dentro de cada Caminho**. E a pergunta aberta desde a v0.24 muda de forma: *"o Guia contra a Vanguarda"* vira ***"esta combinação de Guia contra aquela combinação de Vanguarda"***. **A régua (Q3) tem de nascer sabendo disso** — ela não está precificando quinze coisas exclusivas, está precificando peças que se somam dentro do Caminho.

*A Q1 tirou as 105 combinações entre Caminhos; a Q4 devolveu as combinações dentro deles. O saldo é bom — cruzamento dentro de um Caminho é escolha de construção, e entre Caminhos era multiclasse —, mas não é zero, e a régua paga a diferença.*

**Q5 — O que cada Trilha entrega, entrada por entrada.** *Última de propósito.* É a passada de conteúdo, e ela só começa depois da Q3.

## 4. A ordem de ataque recomendada

**Não é por Caminho, e o motivo é dependência — o mesmo critério que ordenou a fila na v0.36.**

| # | bloco | por quê aqui |
|---|---|---|
| 1 | **a régua** (Q1 a Q4) | peça 13 contra peça 14: régua antes de catálogo é a diferença entre uma versão e seis |
| 2 | **Evocador** — `Servo` · `Matilha` · `Coro` | **as três já têm máquina**, e o rascunho de Invocações já escreveu o que cada uma concede. São o teste barato da régua contra coisa pronta |
| 3 | **Vanguarda** — `Estocada` · `Batedor` · `Executor` | **é a única com dívida numerada** — `6%` a `9%` da Rotina, peça 14 §4 — e com moeda já aprovada para pagá-la: *"acesso a arma é moeda que ela pode gastar"* (v0.45) |
| 4 | **Guia** — `Elo` · `Sutura` · `Perímetro` | fecha o problema de design nº 2, aberto desde a v0.24. A v0.36 já disse que **tudo passa**; falta o número |
| 5 | **Bastião** — `Muro` · `Punho` · `Brasa` | `Muro` encosta em **cobrir-se de energia** (peça 11 §6) e em escudo (peça 14 §4). *A v0.36 já mandou medir as duas juntas: "ou uma domina a outra, ou são a mesma peça com dois nomes"* |
| 6 | **Emanador** — `Torrente` · `Repertório` · `Arremate` | **`Torrente` é a mais perigosa das quinze** e por isso vai por último: ela é mais de uma ação por rodada, que é a coisa que quebra todo sistema d20. `Repertório` toca a peça 11 e `Arremate` toca a economia de ação |

**E duas coisas para medir antes de escrever, não depois** — as duas já estão registradas no `ESTADO-ATUAL` e nenhuma foi medida:

- **A reação de Redução de Dano do Bastião contra cobrir-se de energia**, que já dá RD de `1,5 × refino` por 2 PE.
- **Os *pontos de feitiço* do Emanador são moeda nova ao lado do PE**, e toda moeda nova passa pelo `conferir-orcamento.py` antes de ter número.

## 5. O que o validador vai precisar ter

- **A matriz de dominância entre as quinze**, e ela roda **por Caminho** e **entre Caminhos** — porque a pergunta do Guia contra a Vanguarda é entre Caminhos.
- **Se a Q1 responder "mais de uma"**, a matriz varre as **105 combinações** de duas.
- **O orçamento de cada Trilha contra os `6%` a `9%` da Rotina**, lido da **peça 14 §4** e nunca de constante.
- **Nenhuma entrega com dado de dano**, e o contra-teste: perturbar a régua da peça 5 §4 tem de acender.
- **Nenhuma entrega que cresça com refino** — peça 11 §2.
- **O teto de uma Rotina somada**, para `Servo`, `Matilha`, `Coro` e `Torrente`, conferido **pela economia de ação** e não por decreto.
- **A tabela de progressão consolidada**, que esta peça vai finalmente poder fechar: o validador confere que **todo nível entrega alguma coisa de algum documento**, ou que os que não entregam sejam lista declarada.
- **Triagem de todo nome** que as quinze criarem — e é onde mais nome novo vai nascer no projeto inteiro.
- **A cota de ataque extra da peça 6 §3.1** conferida contra o catálogo: só `Arremate` e `Coro` o dão por Trilha, e **o Guia por nenhuma rota**.

## 6. O que esta peça destrava, e o que ela fecha

| | |
|---|---|
| **destrava** | nada — **ela é a última dependência da fila.** É a peça que os outros esperam, não a que espera |
| **fecha** | o problema de design **nº 2** (Guia contra Vanguarda, aberto desde a v0.24), a pendência **nº 3** e a **nº 4** do `ESTADO-ATUAL`, as três perguntas do §9 da peça 6, e a dívida de `6%` a `9%` da Rotina que a peça 14 §4 registrou |
| **toca** | **100% das fichas.** Nenhuma outra peça da fila faz isso |

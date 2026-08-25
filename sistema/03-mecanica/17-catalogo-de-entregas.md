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
| a `Escola de Arma` da Vanguarda | **1 degrau + 14 Manhas** | o degrau é um; as Manhas são catálogo próprio, e por isso elas têm seção separada aqui |

*Sem essa regra a contagem não fecha duas vezes seguidas do mesmo jeito, e foi o que aconteceu: a v0.84 publicou `48` entregas com a divisão `Estocada 4 · Batedor 8 · o resto 5`, e recontando dos arquivos sai outra divisão com o mesmo total. **Total que fecha por caminhos diferentes é total que ninguém está conferindo.***

## 3. As 56 entregas de Trilha

Doze Trilhas escritas, e o `Batedor` entra com as três rotas abertas. **As três do Evocador — `Servo`, `Matilha` e `Coro` — não entram**, porque estão paradas desde a v0.82 e não têm entrega escrita; quando voltarem, entram aqui.

Todas moram em **`DESENHO-trilhas.md`**, na seção mecânica da Trilha.

### Bastião — 12 com nome, 0 sem

| Trilha | 2 | 11 | 19 | 27 |
|---|---|---|---|---|
| **`Muro`** | `Alicerce` | `Aterro` | `Escora` | `Cúpula` |
| **`Punho`** | `Engate` | `Encontrão` | `Tropel` | `Arranco` |
| **`Brasa`** | `Fagulha` | `Braseiro` | `Labareda` | `Fornalha` |

### Vanguarda — 20 com nome, 0 sem

| Trilha | 2 | 11 | 19 | 27 |
|---|---|---|---|---|
| **`Estocada`** | `Compasso` | `Traçado` | `Bote` | `Ferrão` |
| **`Batedor` · `Yumi`** | `Disparo Carregado` | `Mirar` | `Pique` | `Dobro` |
| **`Batedor` · `Besta`** | `Manivela` | `Mirar` | `Repuxo` | `Dobro` |
| **`Batedor` · `Arma de Fogo`** | `Ferrolho` | `Mirar` | `Descarga` | `Dobro` |
| **`Executor`** | `Pegada` | `Aprumo` | `Revide` | `Retomada` |

> **O `Mirar` aparece em seis destas casas, e até a v0.85 ele não tinha regra em lugar nenhum.** *Este índice foi quem achou: treze menções no desenho, todas concedendo, nenhuma definindo.* **Escrito na v0.86** — Ação Bônus, vantagem no próximo tiro, e só se você não se deslocou nem vai se deslocar. *A regra mora no `DESENHO-trilhas.md`, na seção `A ação Mirar`, antes das três rotas.*
>
> **O nome fica, e a colisão é aceita e declarada.** *A triagem devolve `Mirar` como `fraco` — ele está a uma letra de `Mira`, que é Família no manual — e a **decisão do Mizuki na v0.87 é manter**, no molde do escudo `Médio` da peça 14, que carrega duas colisões declaradas.*

### Guia — 12 com nome, 0 sem

| Trilha | 2 | 11 | 19 | 27 |
|---|---|---|---|---|
| **`Elo`** | `Nó` | `Repasse` | `Partilha` | `Trança` |
| **`Sutura`** | `Agulha` | `Enxerto` | `Pulso` | `Cerzido` |
| **`Perímetro`** | `Chão` | `Sentinela` | `Encalço` | `Portão` |

*O único Caminho com as três Trilhas fechadas em nome e em texto de mesa, desde a v0.84.*

### Emanador — 11 com nome, 0 sem, 1 vaga

| Trilha | 2 | 11 | 19 | 27 |
|---|---|---|---|---|
| **`Torrente`** | `Acelerar` | `Vazão` | `Cheia` | `Transbordo` |
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

## 5. As 14 Manhas

Treze são uma por categoria de arma; a décima quarta se leva **no lugar** da sua. Todas com nome, todas em **`DESENHO-manhas.md`**, na seção *"O catálogo"*.

`Talho` · `Raspão` · `Abalo` · `Tranco` · `Encaixe` · `Racho` · `Gancho` · `Espeto` · `Laço` · `Palmo` · `Zunido` · `Prego` · `Estampido` · `Versado`

> **A `Versado` entrou na v0.147 e ela não é de categoria nenhuma.** *Ela existe para quem troca de arma no meio da luta, e por isso substitui a Manha da categoria escolhida em vez de somar com ela.* **Conta como entrada própria pela regra da seção 1** — ela tem nome e regra próprios, e não é menu dentro de degrau.

> **Elas são a única das três famílias sem bloco de regra separado.** *O texto de mesa delas é a coluna `o que faz` da própria tabela de preço.* **Então a checagem de "tabela e bloco batem" não tem o que comparar aqui** — e isso é propriedade do formato, não dívida.

## 6. Os totais

| família | entradas | com nome | sem nome | vaga |
|---|---|---|---|---|
| entregas de Trilha | **56** | 55 | **0** | 1 |
| degraus de Caminho | **20** | 20 | 0 | 0 |
| Manhas | **14** | 14 | 0 | 0 |
| **total** | **90** | **89** | **0** | **1** |

**Nenhum nome falta.** *As 21 vagas que existiam na v0.86 fecharam na v0.87 — o Bastião inteiro, a `Estocada`, a `Torrente` e o `Batedor`.* **A única casa sem nome do sistema é a vaga do `Arremate`, e ela é de propósito.**

> **O `Dobro` aparece nas três rotas do `Batedor`, e isso é deliberado.** *O nível 27 das três é a mesma frase — o `Mirar` passa a valer para os dois ataques —, e o próprio `Mirar` já é um nome para as três.* **Nome repetido para regra idêntica é uma palavra a menos para a mesa carregar.**

> **Nenhum destes números fica guardado no validador.** *Ele reconta as três tabelas acima a partir delas mesmas e falha se a soma escrita não bater com a contada — o molde da tabela de totais da peça 13, que já tinha envelhecido duas vezes dentro do próprio arquivo antes de alguém contar.*

## 7. O que o `conferir-catalogo.py` confere

Doze checagens. **Nenhuma guarda valor:** os nomes saem das tabelas desta peça e os textos saem dos `DESENHO-*.md`.

| # | a checagem | o que ela pega |
|---|---|---|
| **1** | os totais publicados na seção 6 batem com o contado das seções 3, 4 e 5 | total copiado que envelheceu na primeira edição |
| **2** | o total fecha por família e por estado, e os dois dão o mesmo número | uma entrada sem estado declarado |
| **3** | todo nome desta peça aparece no `DESENHO` dono dela | entrada renomeada de um lado só |
| **4** | todo nome em degrau dos `DESENHO` aparece aqui | entrada nova que ninguém indexou |
| **5** | toda entrega de Trilha com nome tem bloco de regra escrito | preço sem texto de mesa — o furo que o Guia tinha até a v0.84 |
| **6** | **bloco de regra não contradiz o gate da linha de preço** | **a `Estocada`**: linha de preço com gate e bloco dizendo `sempre` |
| **7** | a contagem de peças e validadores desta pasta é `20` | peça ou validador novo entrando sem os três documentos subirem |
| **8** | todo documento vivo que cita o total concorda com o contado | **esta peça virando a segunda fonte do próprio número** |
| **9** | toda `Classe` que a linha de preço cobra aparece no bloco de regra | **a `Brasa`**: preço de `Classe 3` com o bloco publicando `Classe 2` |

**A DÉCIMA SEGUNDA entrou na v0.131, e o buraco dela não era número divergindo de número: era número que NÃO EXISTIA.** *A linha do nível 2 da `Torrente` publicava `(a base)` na coluna de fatias — texto onde as outras 55 linhas têm número —, e com isso uma entrega de `2,87` fatias ficou cinquenta versões fora do total da Trilha dela.* **O `(a base)` aparecia UMA vez no `DESENHO-trilhas.md` inteiro.**

> **Uma célula que não lê como número é o único jeito de uma entrega escapar do total sem nada acusar:** *somar as quatro linhas e comparar com o cabeçalho sai verde, porque a linha muda não entra em nenhum dos dois lados.* **Por isso ela tem duas metades:** a `12.1` cobra fatia legível em toda linha de preço, e a `12.2` reconta o total do cabeçalho contra o que as linhas somam. **Zero declarado não reprova** — `0,00` é preço, e o nível 27 do `Arremate` está vago com `0,00` de propósito; o que reprova é a ausência.

**A décima entrou na v0.88, e ela é a primeira que não fala de entrega.** *A peça 6 §9 publicou o calendário de Caminho aposentado — `7 · 15 · 23 · 29` — como fato fechado por **dezoito versões**, e nenhum validador alcançava.* **Ela compara toda cópia viva contra o `DESENHO-caminhos.md`, que é o dono, e em dois eixos:** *a primeira metade pergunta se o valor bate; a segunda pergunta se o valor morto sumiu.* **E ela sabe quantas cópias existem** — se achar menos, alguém reescreveu a frase e ela parou de conferir em silêncio.

**A nona entrou na v0.87, e ela é a metade que a sexta não cobre.** *A sexta pega gate contra `sempre`; esta pega **valor contra valor**, que é o que deixou o nível 19 da `Brasa` publicar `Classe 2` enquanto a tabela e o argumento diziam `Classe 3`, e `Classe 4` do nível 21.* **A direção é de mão única de propósito:** comparar os dois lados como conjunto dava **sete** vermelhos falsos, porque o bloco cita `Classe` em exemplo de custo o tempo todo — *"num Classe 7 são 7 PE"* — e exemplo não é promessa.

**A oitava nasceu de revisão cética contra esta própria peça.** *Escrevendo o `89` no `README`, no `ESTADO-ATUAL`, no `LEIA-ME` e no README da entrega, ele virou cinco cópias — dentro do documento que a seção 1 abre dizendo que não vai duplicar nada.* **Esta peça é a dona do total; os outros quatro são cópia, e agora existe quem compare.** *O `CHANGELOG` fica de fora de propósito: ele é registro histórico, e a entrada da v0.84 tem de continuar dizendo `81` sem falhar nada.*

**A sexta é a que esta peça existe para ter.** Ela lê, de cada linha de preço, se o degrau é condicional — a palavra de gate, ou a taxa abaixo de `100%` — e reprova se o bloco correspondente afirmar que o efeito é permanente. *É estreita de propósito: ela pega a forma da contradição que aconteceu, e não a intenção do texto.*

> **A quinta e a sexta se medem por eixos diferentes**, e isso é regra do arnês desde a v0.63. A quinta pergunta *"existe bloco?"*; a sexta pergunta *"o bloco diz a mesma coisa que o preço?"*. **Apagar o bloco acende a quinta; reescrever o bloco acende a sexta.** Uma checagem só cobriria metade e sairia verde na metade que custou a `Estocada`.

## 8. Em aberto

- ~~**O `Mirar` não tem regra.**~~ **Escrito na v0.86**, e ele estoura o degrau em `4,25` fatias contra `0,80` — *decisão do Mizuki, com o estouro declarado no desenho, no molde do `Punho` e da `Brasa`.* **E o nome fica**, com a colisão declarada.
- ~~**Faltam nomes de entrega.**~~ **As 21 vagas fecharam na v0.87.** *A única casa sem nome é a vaga do `Arremate`, e ela é de propósito.*
- ~~**`Quick Draw` é o único nome em inglês do sistema.**~~ **Traduzido na v0.88: virou `Descarga`.** *Decisão do Mizuki entre quatro candidatos que passaram na triagem. **O sistema não tem mais nenhum nome em inglês.***
- ~~**Duas entregas têm nome em minúscula.**~~ **Consertadas na v0.93.** *O `Acelerar` da `Torrente` só precisou da maiúscula. O do `Yumi` precisou de nome novo: `Carregar` sai **OCUPADO** na triagem — é Restrição no manual —, e por isso ele nasceu minúsculo. Virou `Disparo Carregado`.* **Nenhuma das 89 entradas tem mais nome em minúscula.**
- **As três do Evocador ficam de fora enquanto estiverem paradas.** Quando voltarem, o total sai de `89` e a checagem 1 acusa até esta peça subir junto.
- **A checagem 6 não alcança as Manhas**, porque elas não têm bloco separado. *Se elas ganharem texto de mesa próprio um dia, ela passa a valer lá também.*
- **Esta peça não preça nada.** Se uma entrega estiver com o preço errado, quem acha é a matriz de dominância do desenho — não o índice.

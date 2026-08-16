# A lista fechada de gatilhos — proposta para a Q3

*Rascunho de trabalho, não é peça. Toda taxa aqui sai de um documento do projeto e nenhuma foi escolhida por mim. As âncoras estão nomeadas linha a linha, e o critério de reprovação é o que a peça 13 §7 já usa.*

---

## As quatro âncoras, e de onde cada uma vem

| âncora | valor | dono |
|---|---|---|
| a luta dura | **`3,4` a `4,0` rodadas** | **peça 1 §8** |
| taxa de acerto contra alvo que investiu em defesa | **`50%`** | peça 1 |
| `20` natural | **`5%`** | peça 1 |
| o dia tem | **3 a 4 lutas** — três de graça, exaustão na quarta | peça 10 §4 |
| a escada de relógios | `por cena` → `descanso curto` → `por dia` → `descanso longo` | peça 10 §5 |
| o filtro reprova em | **spread de `3,0×`** entre a leitura mais dura e a mais generosa | peça 13 §7 |
| o piso de taxa | **`20%`** — o teto de `-80%` de limitação | GURPS, e é onde a escada de Classe Passiva do §3.1 já parava |

---

## A lista

**Duas travas, e uma entrada precisa passar nas duas:** taxa de pelo menos `20%`, e spread abaixo de `3,0×`.

### A — ancorado em rolagem · a taxa cai do d20 e ninguém arbitra

| gatilho | taxa | spread | |
|---|---|---|---|
| quando você **acerta** um ataque | `50%` | `1,0` | **passa** |
| quando você **erra** um ataque | `50%` | `1,0` | **passa** |
| quando o alvo **falha num TR** que você impôs | `50%` | `1,0` | **passa** |
| quando você **critica** | `5%` | `1,0` | **reprova — abaixo do piso** |

> **Aviso de lição nº 2, e ele foi reescrito na v0.74 porque faltava uma palavra.** *Como estava, ele reprovava a linha de cima desta mesma tabela: ele proibia multiplicar por "quando você acerta", e "quando você acerta" está aprovada a `50%` três linhas acima. **Duas linhas do mesmo documento dizendo o contrário.***
>
> **A regra é sobre a MESMA rolagem, e não sobre rolagem em geral.**
>
> | o gatilho é | multiplicar? | por quê |
> |---|---|---|
> | a **mesma** rolagem que o botão já embute | **não** | *"quando você acerta, o seu golpe causa mais X"* — o valor de X já foi medido contando os 50%. Multiplicar de novo conta o acerto duas vezes |
> | **outra** rolagem, anterior ao botão | **sim** | *"quando você acerta, ganhe um golpe a mais"* — o golpe novo rola o próprio dado. O gate é um dado a mais na frente, e ele restringe de verdade |
>
> **O `Engate` do `Punho` é o segundo caso**, e é por isso que ele é cobrado a `75%`: o acerto que dispara é o da ação de atacar, e o soco de bônus rola sozinho depois. *A taxa é `75%` e não `50%` porque quem tem ataque extra rola dois dados e basta um acertar.*
>
> **E a taxa não é a mesma em todo nível.** Um ataque dá `50%`, dois dão `75%`, três dariam `87,5%`. **Toda entrada que use este gatilho tem de declarar contra quantos ataques ela está medida** — e a fatia mede no nível 30, onde Bastião e Vanguarda têm dois.

*E o crítico reprovando não é a régua nova brigando com o projeto: a escada de Classe Passiva do §3.1 declara que a Classe 1 dispara em `~20%`, e a célula de exemplo dela é `"posicionamento — só quando você critica"`, que dispara em `5%`. **A célula já estava fora da própria escada.***

### B — ancorado em relógio · a escada da peça 10 §5

| gatilho | taxa | spread | |
|---|---|---|---|
| `1×` por **descanso curto** | `30%` | `1,0` | **passa** — o gatilho é *"a luta acabou"*, que dois mestres arbitram igual |
| `1×` por **cena**, gatilho **estreito** | `30%` | — | **passa** — quem limita é o gatilho, não o relógio (peça 13 §7) |
| `1×` por **cena**, gatilho **largo** | `30%` | **`3,0`** | **reprova — multi-mestre** |
| `1×` por **dia** | `9%` | `1,0` | **reprova — abaixo do piso** |
| `1×` por **descanso longo** | `3%` | `1,0` | **reprova — abaixo do piso** |

> **O piso reproduz sozinho uma decisão que o projeto já tinha tomado por levantamento externo.** O §3.6 cita o Stoddard reprovando *"uma vez por dia"* e liberando *"uma vez por descanso curto"*. **A conta chega no mesmo lugar sem citar ninguém** — `9%` contra `30%`, com o corte em `20%` no meio. *Duas rotas independentes na mesma resposta é o que faz uma régua valer.*

**Gatilho estreito** é o que a peça 13 §7 define: uma perícia nomeada, um Teste de Resistência nomeado, até três coisas contáveis. **Largo** é *"combate"* — e combate acontece toda missão, então o relógio vira o único limitador e leva o spread inteiro.

### C — ancorado em estado da ficha · não há o que arbitrar

| gatilho | taxa | |
|---|---|---|
| **permanente** | `100%` | **passa** |
| **enquanto a invocação está de pé** | `100%` | **passa** — a invocação está de pé por padrão, e quanto tempo ela fica não é escolha de quem mestra |
| enquanto você **empunha** / **veste** / **está numa Trilha** | `100%` | **passa** |

### D — ancorado em julgamento · a lista do que não entra

| gatilho | taxa | spread | |
|---|---|---|---|
| `1×` por **sessão** | `6%` | `3,0` | **reprova nos dois eixos** |
| `1×` por **arco** | `2%` | `3,0` | **reprova nos dois eixos** |
| *"quando o mestre julgar…"*, em qualquer forma | — | `3,0` | **reprova** |

*Os dois primeiros a peça 13 §7 já tinha reprovado, com esse mesmo `3,0×`. Aqui eles reprovam também pelo piso, que é rota nova para a mesma conclusão.*

---

## O que a régua passa a reprovar, e é o ponto inteiro

Com o piso aplicado, as oito famílias do permitido deixam de caber todas:

| família | botão | mínimo que ela custa | em fatias | % do orçamento da Trilha | |
|---|---|---|---|---|---|
| **exceção de ação** | `108,00` | `21,60` | **`17,0`** | **426%** | **REPROVA sozinha** |
| troca do fixo por atributo | `21,55` | `4,31` | `3,4` | **85%** | come o orçamento inteiro |
| duração `+1` rodada | `21,60` | `4,32` | `3,4` | **85%** | *já saiu do permitido na v0.68* |
| alvo — golpe pega 2 | `11,50` | `2,30` | `1,8` | 45% | cabe |
| acerto `+1` | `5,40` | `1,08` | `0,9` | 21% | cabe |
| recuperação `+1 PE` | `5,14` | `1,03` | `0,8` | 20% | cabe |
| posicionamento `+3 m` | `1,80` | `0,36` | `0,3` | 7% | cabe |
| posicionamento `+1,5 m` | `0,90` | `0,18` | `0,1` | 4% | cabe |

**A trava da matriz que hoje é escrita à mão — *"a `Matilha` não pode receber ação, o `Servo` não pode receber ação"* — passa a cair da conta.** Nenhuma Trilha pode receber exceção de ação, com nenhum gatilho, porque `17` fatias não cabem em `4`. *Isso não substitui a matriz: ela continua sendo quem mede dominância entre as três. O que mudou é que a régua de preço parou de aprovar o que a matriz proíbe.*

---

## E o `Servo` publicado REPROVA — que é como se sabe que a régua funciona

| nv | a entrega | botão | taxa | sai em |
|---|---|---|---|---|
| 2 | treino | utilidade | — | — |
| 11 | `+1 PE`, `1×` por descanso curto | `5,14` | `30%` | `1,56` |
| 19 | `+3 m` permanente | `1,80` | `100%` | `1,80` |
| 27 | golpe pega 2 alvos | `11,50` | **`20%`** *(era `15%`)* | **`2,30`** |

**Soma `5,66` contra um orçamento de `5,07` — estoura em `12%`.**

### A prova de que os `15%` foram escolhidos para fechar

```
orçamento 5,07 − nv11 (1,56) − nv19 (1,80) = 1,71 sobrando para o nv27
1,71 ÷ 11,50 = 14,9%
```

**O documento publica `15%`.** A conta reconstrói o número inteiro a partir do que sobrou nas outras três entregas — ele nunca saiu de um gatilho, saiu da subtração. *E é por isso que o §6.10 termina dizendo que falta escrever o gatilho: não existe gatilho que produza `15%`, porque o `15%` não veio de nenhum.*

### O que cabe no nível 27 no lugar

Sobram `1,71` de dano por rodada, que são `1,35` fatias:

| em vez do golpe de 2 alvos | taxa que ele pediria | |
|---|---|---|
| golpe pega 2 alvos | `14,9%` | **não cabe** |
| `+1` no seu acerto | `31,7%` | cabe — e `50%` (*"quando você acerta"*) está na lista |
| `+1 PE` por rodada | `33,3%` | cabe |
| `+3 m` outra vez | `95,1%` | cabe, mas repete o nível 19 |

**Ou o golpe de 2 alvos sai do nível 27, ou uma das outras três entregas encolhe para abrir os `0,59` que faltam.** É decisão sua, e as duas são legais.

---

## O achado que só apareceu com a lista fechada

**Fechar os gatilhos fecha as taxas.** Não existe mais `15%` nem `31,7%` — existem `100%`, `50%` e `30%`, e só. Cruzando as cinco famílias do permitido com as taxas legais, **o Evocador tem exatamente 17 entregas possíveis**, e 50 montagens de três fecham dentro de 5% do orçamento. *A régua saiu de "aprova tudo" para "aprova 17 coisas".*

**E aí aparece o que a taxa livre estava escondendo.** Quantas dessas 17 são **permanentes e cabem** em menos de duas fatias?

| entrega permanente | vale | em fatias | |
|---|---|---|---|
| alvo — golpe pega 2 | `11,50` | `9,07` | não cabe |
| acerto `+1` | `5,40` | `4,26` | **come o orçamento inteiro** |
| recuperação `+1 PE` | `5,14` | `4,06` | **come o orçamento inteiro** |
| posicionamento `+3 m` | `1,80` | `1,42` | **cabe** |
| posicionamento `+1,5 m` | `0,90` | `0,71` | **cabe** |

**Só posicionamento.** O §6.4 escolheu para o `Servo` a forma *"três permanentes e um botão"* — **e ela não é construível**, porque três permanentes que caibam seriam três posicionamentos.

> **Isso é a parede do §6.5 numa forma mais dura, e ela não é da moeda nem da régua.** O permitido da peça 5 §4 tem cinco famílias vivas para o Evocador, e **três delas são grandes demais para serem permanentes** dentro de uma Trilha. Não sobra do que montar uma Trilha sempre-ligada.
>
> **A saída já está escrita e é a camada de vínculo do §6.7** — *"o que VOCÊ ganha por ela estar de pé"*. Ela é a única categoria que pode produzir permanente **pequeno**, porque não herda o tamanho dos botões da peça 5 §4. **Ela tem régua e trava desde a v0.68 e nunca teve catálogo** — e o que faltava para escrevê-lo era exatamente esta lista de gatilhos.

*E a forma do `Servo` já estava solta de qualquer jeito: a variância refeita derrubou o §6.4, porque o `Coro` a `90%` cai para `2,13` contra os `2,09` do `Servo`. As três formas precisam ser reescolhidas junto.*

---

## A âncora de rodadas mudou de dono na v0.74

**Este documento ancorava *"a luta dura `3,3` rodadas"* na peça 15 §3.2, e aquela seção não fala de duração de luta.** O `3,3` aparece lá — numa tabela de quantos corpos a `Matilha` derruba —, e foi provavelmente de lá que ele veio. *Número certo lido da coluna errada da tabela certa é o modo de falha que o `conferir-manual.py` já tinha registrado uma vez.*

**A dona é a peça 1 §8: `3,4` a `4,0` rodadas.** As peças 11 e 14 usam `3,5` e `3,7`, todas dentro da faixa.

> **E o `3,3` tem uma segunda origem, que explica melhor por que ele parecia certo.** A tabela de inimigo do manual põe o chefe do nível 30 em `1050 a 1260` de vida contra `~315` de dano do grupo por rodada — e `1050 ÷ 315 = 3,33`. **O `3,3` é o PISO daquela faixa**, lido como se fosse o valor típico. *É piso-lido-como-outra-coisa pela terceira vez na mesma linhagem, e as três vezes o número parecia razoável.*

**Nada quebra, e é bom saber de quanto:** com `3,7`, o `1×` por descanso curto vale `27%` em vez de `30%` — continua acima do piso de `20%`, e o `1×` por dia continua reprovando. **Toda entrada preçada a `30%` está `11%` generosa**, e isso vale para o `Servo` publicado.

## O que ainda falta na lista

- **Gatilhos de posição** — *"quando o alvo está a 1,5 m"*, *"quando você não se moveu"*. Eles não têm spread de mestre (o tabuleiro decide), mas a **taxa só sai da mesa**. Entram marcados como previsão, no molde dos `5%` de posicionamento que a v0.68 já aceitou assim.
- **A taxa de utilidade** — o treino do nível 2 vale `10` pontos percentuais num TR e de `5` a `20` numa perícia. Isso tem conversão e a lista acima não cobre, porque ela é de dano.
- **O validador.** Todos estes números continuam sem rede até a peça fechar, e a especificação do §5 vai precisar de duas linhas novas: *toda entrada cita um gatilho desta lista* e *nenhuma taxa fica abaixo do piso*.

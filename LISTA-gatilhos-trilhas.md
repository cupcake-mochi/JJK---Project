# A lista fechada de gatilhos — proposta para a Q3

*Rascunho de trabalho, não é peça. Toda taxa aqui sai de um documento do projeto e nenhuma foi escolhida por mim. As âncoras estão nomeadas linha a linha, e o critério de reprovação é o que a peça 13 §7 já usa.*

> ## ⚠ Este documento estava na ESCALA VELHA, e a v0.77 converteu
>
> **Ele foi escrito quando quatro fatias valiam `5,07` de dano por rodada — a camada de vínculo do Evocador, fechada na v0.68.** A v0.73 dobrou o orçamento duas vezes: **hoje a fatia é `5,08` e a Trilha leva `5`, que são `25,40` de dano por rodada.** O orçamento é **`5,01×`** maior, e este arquivo continuou medindo pelo antigo mesmo depois de ser revisado na v0.74.
>
> **Ele não dizia em que escala estava, e é assim que se descobre:** ele publica *"exceção de ação = `17,0` fatias"* ao lado de *"mínimo `21,60`"*, e `17,0 × 1,27 = 21,59`. Com a fatia de hoje daria `86`. *Segunda prova, independente:* a seção do `Servo` mede contra um orçamento de `5,07`, que é `4 × 1,27`.
>
> **As taxas não mudam — elas são fração e não valor.** As quatro famílias de gatilho abaixo, o piso de `20%` e o filtro de `3,0×` valem exatamente como estão. **O que muda é toda coluna que diz "em fatias" ou "% do orçamento", e com ela dois vereditos que este documento tinha tomado como fechados.**
>
> *As colunas velhas ficam à vista de propósito, no mesmo molde das linhas de `16` pp do `DESENHO-trilhas.md`: número errado apagado é número que alguém redescobre.*

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

Com o piso aplicado, cada família tem um preço mínimo — o botão dela vezes os `20%`. **A coluna que decide é a última, e ela mede contra os `25,40` de dano por rodada que a Trilha tem hoje.**

| família | botão | mínimo que ela custa | em fatias | % da Trilha | | *(escala velha)* |
|---|---|---|---|---|---|---|
| **exceção de ação** | `108,00` | `21,60` | `4,25` | **85%** | **cabe, e mal** | ~~17,0 · 426% · REPROVA~~ |
| troca do fixo por atributo | `21,55` | `4,31` | `0,85` | 17% | cabe | ~~3,4 · 85%~~ |
| **duração `+1` rodada** | `21,60` | `4,32` | `0,85` | **17%** | **cabe** | ~~3,4 · 85%~~ |
| alvo — golpe pega 2 | `11,50` | `2,30` | `0,45` | 9% | cabe | ~~1,8 · 45%~~ |
| **golpe simples para um ALIADO** | `11,50` | `2,30` | `0,45` | 9% | cabe | *(não estava na lista)* |
| acerto `+1` | `5,40` | `1,08` | `0,21` | 4% | cabe | ~~0,9 · 21%~~ |
| recuperação `+1 PE` | `5,14` | `1,03` | `0,20` | 4% | cabe | ~~0,8 · 20%~~ |
| posicionamento `+3 m` | `1,80` | `0,36` | `0,07` | 1% | cabe | ~~0,3 · 7%~~ |
| posicionamento `+1,5 m` | `0,90` | `0,18` | `0,04` | 1% | cabe | ~~0,1 · 4%~~ |

> **Dois vereditos viraram, e os dois estavam sendo tratados como fechados.**
>
> **1 — `exceção de ação` deixa de reprovar sozinha.** A versão velha desta seção dizia *"nenhuma Trilha pode receber exceção de ação, com nenhum gatilho, porque `17` fatias não cabem em `4`"*. **Na escala de hoje ela cabe em `85%` do orçamento com o gatilho mais frouxo que a lista permite** — apertado, mas dentro. *E a Vanguarda já provava isso sem ninguém cruzar: o nível 19 da `Estocada` é exceção de ação a `100%` e está publicado em `2,46` fatias.*
>
> **A trava do Evocador não cai junto, e isso importa.** *"A `Matilha` não pode receber ação, o `Servo` não pode receber ação"* continua valendo — só que ela volta a ser **regra da matriz**, escrita à mão, e para de cair da conta de preço. **O que a conta dava de graça, agora alguém precisa segurar.**
>
> **2 — `duração` volta ao permitido.** A v0.68 expulsou ela com *"não existe comprimento de efeito que faça `+1 rodada` caber; no melhor caso ela ainda é onze vezes uma entrega"*. **As onze vezes eram onze fatias de `1,27`.** Hoje:
>
> | o efeito dura | `+1` rodada vale | permanente | com gate de acerto | `1×` por descanso curto |
> |---|---|---|---|---|
> | 2 rodadas | `54,0` | 10,63 — **não cabe** | 5,31 — não cabe | 3,19 |
> | 5 rodadas | `21,6` | 4,25 | **2,13** | **1,28** |
> | 8 rodadas | `13,0` | **2,55** | **1,28** | 0,77 |
>
> *(em fatias de `5,08`, contra uma Trilha de `5`)*
>
> **Só o efeito curto continua fora**, e por um motivo que faz sentido sozinho: dobrar a duração de uma coisa que dura duas rodadas é dobrar a coisa. **Do efeito de cinco rodadas para cima, duração cabe** — e ela é o eixo em que a Trilha `Elo` do Guia foi desenhada.

## A família que faltava: golpe simples para um ALIADO

*Ela nunca esteve nesta lista, e existe desde a v0.72 — está no `DESENHO-caminhos.md`, cortada do nível 7 do Guia.*

> **Quando você usa o `Guiar` num aliado, ele pode acrescentar um golpe simples ao turno dele.** Uma vez por rodada.

**O botão já entra descontado, e o motivo é que o golpe é de outra pessoa.** Um golpe simples vale `11,50` de dano, e ele só sai se o aliado acertar — então o botão é `11,50 × 50% = 5,75`. *É exatamente assim que o `DESENHO-caminhos.md` preçou, e o número não se moveu.*

| gatilho | taxa | dano/rodada | fatias | % da Trilha |
|---|---|---|---|---|
| **permanente, `1×` por rodada** | 100% | `5,75` | **1,13** | **23%** |
| quando **você** acerta um ataque | 50% | `2,88` | 0,57 | 11% |
| quando o alvo **falha num TR** que você impôs | 50% | `2,88` | 0,57 | 11% |
| `1×` por descanso curto | 30% | `1,72` | 0,34 | 7% |

**Contra o vão de `7` do Caminho ele valia `82%` e não coube junto do `Ajudar`. Contra os `25,40` de uma Trilha ele é `23%`, permanente.** *E o `DESENHO-caminhos.md` já tinha escrito o destino dele: "a sobra da primeira pode ir para uma entrega de Trilha do Guia depois."*

> **Isso NÃO é a família `exceção de ação`, e a diferença é o que faz caber.** Dar uma **ação** a um aliado custa `29,19` — `115%` da Trilha, permanente. O golpe simples custa `5,75`, que é um quinto disso. *Decisão do Mizuki na v0.77: ação inteira fica fora do Guia; o golpe simples entra e pode ser preçado.*

---

## E o `Servo` publicado REPROVA — que é como se sabe que a régua funciona

> **Esta seção inteira está na escala velha, e ela fica como está.** Todo número dela mede contra um orçamento de `5,07`, que hoje é `25,40`. **Não converti, e é de propósito:** o `Servo` publicado precisa ser **refeito** e não reajustado, e a análise abaixo continua valendo para o que ela existe para mostrar — que os `15%` do nível 27 saíram de subtração e não de gatilho nenhum. *Esse achado é sobre o método, e método não tem escala.*

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

**E aí aparece o que a taxa livre estava escondendo.** Quantas são **permanentes e cabem** em menos de duas fatias?

| entrega permanente | vale | escala velha | **em fatias HOJE** | |
|---|---|---|---|---|
| alvo — golpe pega 2 | `11,50` | 9,06 | `2,26` | não cabe — a única que sobra fora |
| **golpe simples para um aliado** | `5,75` | 4,53 | **`1,13`** | **cabe** |
| acerto `+1` | `5,40` | 4,25 | **`1,06`** | **cabe** |
| recuperação `+1 PE` | `5,14` | 4,05 | **`1,01`** | **cabe** |
| posicionamento `+3 m` | `1,80` | 1,42 | `0,35` | cabe |
| posicionamento `+1,5 m` | `0,90` | 0,71 | `0,18` | cabe |

> ## ⚠ Este achado se inverteu na conversão, e ele era o mais forte do documento
>
> **Ele dizia: *"Só posicionamento."*** E daí saía que a forma *"três permanentes e um botão"* que o §6.4 escolheu para o `Servo` **não era construível**, porque três permanentes que coubessem seriam três posicionamentos.
>
> **Na escala de hoje cabem cinco de seis, e três mudaram de veredito.** A forma *"três permanentes e um botão"* é construível de várias maneiras, e nenhuma delas precisa repetir posicionamento.
>
> **A parede do §6.5 era de escala, não de estrutura.** *O texto dela — "três das cinco famílias são grandes demais para serem permanentes dentro de uma Trilha" — descrevia uma Trilha de `5,07` de dano por rodada. A de hoje tem `25,40`.*
>
> **O que sobrevive, e não é pouco:** a **camada de vínculo** do §6.7 continua sendo a categoria certa para o Evocador, porque ela responde *"o que VOCÊ ganha por ela estar de pé"* — e isso é ficção, não preço. **Ela deixou de ser a única saída e passou a ser a saída escolhida.** *Continua sem catálogo.*
>
> *E as `17` entregas possíveis e as `50` montagens contadas acima são do mesmo cálculo velho. **Não recontei** — o Evocador é a última das três que faltam, e recontar agora seria número velho outra vez quando a vez dele chegar.*

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

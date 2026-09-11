# Agente por ficha, jogando combate — dá pra fazer, e quanto custa

*10/09/2026. **Pergunta do Mizuki:** "É possível ser criado fichas e colocar agentes com cada ficha
para testar combates? Tipo… eles tomam decisões como players e afins. Se sim, o quão caro seria?"*

> ⚠ **Os custos aqui são ESTIMATIVA, não medição.** *A única coisa medida é a linha marcada `MEDIDO`,
> e ela vem desta conversa.* **Dá pra medir de verdade com um combate só — é a última seção.**

---

# `1` · Dá pra fazer. Mas são DUAS coisas diferentes, e uma é quase de graça

| | **`A` — simulação em código** | **`B` — agente por ficha** |
|---|---|---|
| quem decide | uma **política escrita por mim** *("ataque quem tem menos vida")* | o **agente**, lendo a ficha |
| quantos combates | **`10.000`** numa rodada de script | **`1`** por vez |
| custo em token | **zero** | **alto** — a conta está abaixo |
| o que ela responde | *quantas rodadas dura · quantos caem · qual a variância · existe montagem dominante* | *a decisão é interessante? o turno do chefe é chato? alguém acha uma combinação que eu não escrevi?* |
| o que ela NÃO responde | **nada sobre decisão.** Ela só executa a política que eu escrevi — e se eu não pensei numa jogada, ela nunca aparece | **nada sobre número.** `1` combate não é amostra |

> ### O projeto já tem `A` rodando. `simular-a-intervencao.py` é exatamente isso.
> **`B` é a coisa nova, e ela não substitui `A` — ela responde a pergunta que `A` não sabe fazer.**

---

# `2` · Como `B` funciona de verdade, e a parte que as pessoas erram

**O erro clássico é fazer o juiz ser um agente.** *Aí a vida do chefe deriva, alguém "esquece" que
está `Impedido`, e a terceira rodada não bate com a segunda.*

> ### O juiz tem de ser CÓDIGO. Uma máquina de estado em Python que guarda vida, posição, condição, iniciativa e rola os dados.
> **O agente só faz uma coisa: escolhe.** *E o código diz se deu certo.*

**A volta, por turno:**

```
código  →  "você é o Yuji. Vida 96/163. O Sukuna está a 12 m, vida 812/1131.
            A Nobara está Impedida. Suas opções: [Desmembrar não é sua] ..."
agente  →  "Corro 9 m e uso Divergente no Sukuna. Se ele tiver Reação, eu queria
            que a Maki puxasse ela antes."
código  →  rola, aplica, atualiza o estado, passa pro próximo
```

**O que precisa existir antes:** o juiz em código *(uma vez, e ele serve pra sempre)*, as fichas dos
jogadores em formato que o código lê, e a lista de ações legais por ficha. **A ficha de inimigo a gente
já tem — é o `RASCUNHO-5`.**

---

# `3` · O custo — e é aqui que dói na conta Pro

## O que está MEDIDO

> **`MEDIDO`, nesta conversa:** *os dois leques de `2` agentes de pesquisa desta sessão gastaram
> **`332k`** e **um segundo lote ainda rodando**. `2` agentes fazendo pesquisa profunda ≈ `332k` tokens.*

## A estimativa, e as premissas dela na frente

**Um combate contra o Sukuna que a gente acabou de montar:**

| | |
|---|---|
| jogadores | `4` agentes |
| o mestre / o inimigo | `1` agente |
| rodadas | `3` — é o que a escada publica pro `Desastre`; a `Calamidade` contra `4` dura `6` |
| decisões dos jogadores | `4` × `3` = **`12`** |
| decisões do inimigo | `6` ações × `3` rodadas + `3` Intervenções = **`21`** |
| **total de decisões** | **`33`** |

**Por decisão, com o contexto já em cache:** *o estado do campo (~`400`), a ficha dele (~`800`, cacheada),
a regra que ele precisa (~`600`, cacheada), mais o raciocínio e a resposta (~`400` a `1.500` de saída).*

| o quanto o agente pensa | por decisão | **um combate** | quantos combates numa sessão |
|---|---|---|---|
| decide rápido, sem tática | `~500` | **`~17k`** | muitos — `20+` |
| pensa a jogada | `~1.500` | **`~50k`** | **`6` a `8`** |
| pensa e negocia com o grupo | `~4.000` | **`~130k`** | **`2` a `3`** |

> ### ⚠ E é o último que você ia querer, porque é o que testa se a mecânica é interessante.
> **`2` a `3` combates por sessão.** *E `3` combates não dizem nada sobre equilíbrio — dizem sobre
> sensação.*

---

# `4` · As quatro coisas que derrubam esse custo, e elas são grandes

| # | o truque | o que ele economiza |
|---|---|---|
| **1** | **o agente declara um PLANO por RODADA, não uma ação por turno** — e o código executa | corta as decisões do inimigo de `21` pra `3`. **O combate cai de `33` pra `15` decisões: `~2,2×` mais barato** |
| **2** | **Haiku nos jogadores, Opus só no mestre** | a decisão de jogador é simples (*"bato no chefe com a minha melhor coisa"*). **`4` dos `5` agentes ficam ~`10×` mais baratos** |
| **3** | **não jogue o combate inteiro — jogue a RODADA `2`** | *a `1` é aproximação e a `3` é limpeza. A rodada em que a decisão importa é a do meio.* **`3×` mais barato, e mede a mesma coisa** |
| **4** | **o código roda `10.000` combates e o agente só olha os `5` esquisitos** | é o casamento de `A` com `B`: a simulação acha onde o número é estranho, e o agente vai ver o que aconteceria ali |

**Com `1` + `2` + `3` juntos:** *`5` decisões, `4` delas em Haiku.* **`~8k` por combate.**
> ### Aí dá `40` combates numa sessão, e `40` combates começam a dizer alguma coisa.

---

# `5` · E tem um uso de agente que é o MELHOR negócio dos dois, e ele não é combate

> ## `1` agente, `1` disparo: *"aqui está a tua ficha e o livro de regras. Ache a coisa mais quebrada que você consegue fazer."*

**Isso é caça a combinação degenerada, e é a única coisa que a simulação NUNCA acha** — porque a
simulação só faz o que eu escrevi na política dela. *Se eu não pensei na jogada, ela não existe no
sim.*

| | |
|---|---|
| custo | **`~20k` a `40k`** — um agente, uma vez |
| o que ele acha | a montagem que ninguém preçou. *A `balanceamento-simulacao` chama isso de "busca exaustiva de todas as montagens legais" — e o agente faz a parte que a busca não faz: ele **inventa** a montagem* |
| quando usar | **antes de fechar versão**, não durante o desenho |

**E o irmão dele, igualmente barato:** *"leia esta ficha e me diga em que rodada ela fica chata."*
**É o teste do "inimigo de um botão só"**, que é o modo de falha que o campo mais reclama — e o
`ESTADO` já registrou ele como o alerta que vale mais que tudo.

---

# ⟹ A recomendação, em três linhas

| | |
|---|---|
| **pro número** | **simulação em código.** `10.000` combates, zero token. É o que o projeto já faz |
| **pra sensação** | **agente por ficha, com os truques `1` a `3`** — plano por rodada, Haiku nos jogadores, só a rodada `2`. `~8k` por combate |
| **pro que ninguém preçou** | **`1` agente caçando combinação degenerada.** É o melhor retorno por token de tudo aqui |

---

## E como MEDIR isso de verdade, se você quiser

**Um combate só, montado pequeno:** `2` jogadores contra `1` `Ameaça` nv5, `3` rodadas, sem os truques.
**Eu reporto o custo real em token, e a estimativa acima passa a ser medida.**

> **Custo do próprio teste: `~15k`.** *É `4%` do que os dois leques desta sessão gastaram.*
> **Não fiz porque você disse que não queria testar agora** — *"N teste realmente, quero mais é saber
> da possibilidade e o quão cara ela é"*. **Fica na fila.**

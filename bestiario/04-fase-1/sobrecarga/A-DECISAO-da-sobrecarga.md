# A `Sobrecarga` — as opções, com o trade-off calculado

*09/09/2026. A conta está em `MEDIDA-a-metade-morta.md`. As fontes externas estão nos três
`fonte-*.md`. As mexidas que isso exige no repositório estão em `MEXIDAS-no-repositorio.md`.*

> **Texto de hoje:** *"Até o fim do próximo turno do alvo, o feitiço dele custa o dobro de energia e
> sai com a CD `2` menor."*
> **Degrau hoje:** `Leve` no gerador e no `.docx`, **`Pesada`** no livro. *Divergência aberta desde a v0.219.*

---

## A primeira coisa, e ela muda o tamanho do conserto

**Você me pediu pra reescrever a metade que vale `0,00` contra inimigo. Ela também vale quase zero contra jogador.**

| "custa o dobro de energia" | vale |
|---|---|
| contra inimigo | **`0,00`** — ele não conta PE |
| contra jogador, se ele paga | `9,00` |
| contra jogador, no `Classe 0` | `0,00` — *o dobro de zero é zero* |
| **o esperado contra jogador** | **`4,50`** — *porque o manual diz que ele passa metade das rodadas no `Classe 0`* |

**`4,50` é `6,2%` de uma ação de chefe.** *E essa é a frase exata que a v0.217 já tirou da `Dívida`
por dobrar zero — a checagem `5` do `conferir-acao.py` proíbe ela de voltar lá e não olha pra cá.*

> ### Então não é pendurar uma cláusula "contra inimigo". É trocar a metade inteira.
> **Uma linha, não duas. E fecha um buraco que o projeto já fechou uma vez.**

---

## O que o campo diz — cinco sistemas, e eles concordam em duas coisas

### 1 · Negar a **Reação** do inimigo é BARATO. Em cinco sistemas, sem exceção.

| sistema | o efeito | o preço | texto |
|---|---|---|---|
| **D&D 5e 2014** | `Shocking Grasp` | **truque — nível `0`** | *"it can't take reactions until the start of its next turn"* |
| **Weird Wizard** | `Prone`, via `Knockdown` | **opção de ataque universal, custo zero** | `Prone` nega reação |
| **Draw Steel** | `Entropy Ward` | **passiva de nível `1`, de graça** | — |
| **Draw Steel** | `Dazed` | **`3` de recurso, nível `1`, em quatro classes** | — |
| **LANCER** | `JAMMED` — mata reação, ataque e tech | **`1` quick action, licença `LL1`** — o tier mais baixo | — |
| **PF2e** | `Laughing Fit`, rank `2` | **reação no grau `Success`, reação + `slowed 1` no grau `Failure`** | *"Success: It can't use reactions. Failure: The target is slowed 1 and can't use reactions."* |
| **Daggerheart** | `Hypnotic Shimmer` | nível `3`, `Recall 1`, em área | — |

> ### O `Laughing Fit` é a prova mais limpa que existe.
> **A Paizo preçou "nega a reação" e "nega a reação MAIS uma ação" no MESMO feitiço, um grau de
> sucesso de distância.** *Reação é mais barato que uma ação, e a diferença é exatamente um degrau.*

**⚠ E um aviso que vale mais que o resto:** o **D&D 2024 rebaixou** os dois casos mais baratos de
2014. *`Shocking Grasp` e `Open Hand Technique` passaram de "nega toda Reação" para **"nega só
Ataque de Oportunidade"**.* **Não existe mais truque que negue Reação inteira em 2024** — o piso
virou magia de 1º nível.

*Tradução: negar a Reação cabe no degrau mais baixo, mas a edição mais nova de D&D achou que, no
degrau mais baixo, negar a Reação **inteira** era demais.*

### 2 · Encostar na `Intervenção` não é Melhoria. Três sistemas recusam vender isso.

| sistema | o que acontece |
|---|---|
| **D&D, as duas edições** | **nenhuma** opção de jogador tira Ação Lendária. A única porta é `Incapacitated` — *2014: "it can't use them while incapacitated or otherwise unable to take actions"* · *2024: "The monster can't take a Legendary Action if it has the Incapacitated condition"*. E `Incapacitated` nunca é vendido sem duas ou três travas |
| **Draw Steel** | a Villain Action é **inalcançável**: no bloco o campo de ação dela é literalmente `-`, e nenhuma das habilidades que aplicam `Dazed` a toca. **A prova:** ~`10` features de Malice escrevem *"They can use this feature even if they are dazed"* — **quando eles querem furar o `Dazed`, eles escrevem.** A Villain Action não tem cláusula: ela é imune por omissão |
| **Weird Wizard** | `Stunned` diz *"cannot use actions or reactions"* — **e o bloco do dragão AINDA precisou escrever na mão** *"provided [it] is neither stunned nor unconscious"* pros fury tokens. **A regra genérica não alcança a economia especial fora do turno** |
| **Draw Steel, o sinal mais claro** | reduzir Malice está na caixa de **variantes opcionais** do livro — *"You could allow heroes to spend hero tokens to reduce the amount of Malice you have"* — **ao lado de "crítico só no 20 natural"**. A MCDM olhou pra economia do Diretor e decidiu que ela fica fora da escada de preço |

> ### A `Intervenção` morre como alvo, e não pela conta: pelo campo.
> **"A ação fora do turno se governa no bloco do inimigo, não numa Melhoria genérica de feitiço."**
> *E isso é coerente com a decisão que você já tomou — a `Intervenção` não se mexe.*

### 3 · E o campo valida a troca que você está fazendo, com uma frase literal

**O `Counterspell` de 2024 é o efeito mais famoso de "drenar recurso do inimigo" que o D&D tinha. A WotC reescreveu ele pra drenar AÇÃO:**

> *"the action, Bonus Action, or Reaction used to cast it is wasted. **If that spell was cast with a spell slot, the slot isn't expended.**"*

**E o monstro de PF2e TEM poço gastável — spell slots e Focus Points impressos no bloco — e a Paizo
nunca publicou nada que drene isso.** *Só `Counterspell`, troca `1:1`.*

> **Você não está se afastando do campo. Você está indo pra onde ele já foi.**

---

# As três opções

## Opção A — **trava a `Reação`** *(a que eu recomendo)*

> **`Sobrecarga` · `Leve` · *Até o fim do próximo turno do alvo, ele não usa Reação, e o feitiço dele sai com a CD `2` menor.`***

| | |
|---|---|
| **entrega contra chefe nv30** | **`36,50`** de dano por rodada, **invariante** |
| **entrega contra jogador** | `11,50` — *um ataque de oportunidade* |
| **degrau pela regra 1 da peça 19** | **`Leve`** — meia ação negada |
| **dominância em `Leve`** | `2,23×` → `2,64×`, contra o filtro de `3,00×` |
| **irmão publicado no sistema** | o **`Trava`** (`Leve`) entrega `36,50` **ao centavo** — *desvantagem num golpe tira metade dele, e meia ação é metade* |
| **precedente externo** | **o mais forte de tudo:** truque em 2014, custo zero no Weird Wizard, `LL1` no LANCER |
| **fecha a divergência da v0.219?** | **sim** — `Leve` é o lado de `2` dos `3` donos |
| **morde 100% dos blocos?** | **sim.** A `Reação` é constante pra todo inimigo (peça 3). *Zero blocos têm PE; todos têm Reação* |
| **toca na `Intervenção`?** | **não.** *Reação é resposta, Intervenção é iniciativa* — a separação que você já decidiu fica intacta |

**O que custa:** é um **efeito novo** na família `Auxiliar` — hoje nenhuma Melhoria nega reação. E em
`Leve` ela fica em `2,23×`–`2,64×`, **acima do `Trava` (`2,03×`)**, que é o teto atual da família.

---

## Opção B — **`−2` no acerto dele** *(a que faz a Melhoria virar uma ideia só)*

> **`Sobrecarga` · `Leve` · *Até o fim do próximo turno do alvo, todo golpe dele sai com `−2` — na rolagem de acerto, ou na CD, conforme o golpe.`***

**Esta não estava na tua lista. Ela entrou porque é o espelho da metade que FICA.**

| | |
|---|---|
| **entrega contra chefe** | `10,95` a `43,80`, pela mistura do bloco. **No bloco do Sukuna: `21,90`** |
| **degrau pela regra 1** | **`Leve`** — `0,60` ação negada |
| **dominância em `Leve`** | `0,61×` → `2,43×` |
| **irmão publicado** | a **`Precisão`** (`Leve`) vende `+2` em **uma** das duas rolagens. Esta dá `−2` nas **duas** |
| **quantas ideias a Melhoria passa a ter** | **uma.** *"`−2` nas duas rolagens de ataque dele"* — mais curta que o texto de hoje |
| **fecha a divergência?** | **sim**, em `Leve` |

### E ela conserta um buraco que eu não tinha visto: **a metade da CD também é condicional**

**A conta achou uma assimetria que ninguém tinha escrito:**

| os mesmos `−2` num `d20` | negam | por quê |
|---|---|---|
| na **CD** | `5%` daquele golpe | Teste de Resistência bem-sucedido ainda entrega **metade** |
| no **acerto** | **`20%`** daquele golpe | golpe que erra entrega **zero** |

> **A metade da CD, sozinha, só morde ação que pede Teste de Resistência.** *No único bloco
> preenchido que o projeto tem — o Sukuna — ela pega `2` das `3` ações e erra a terceira, que é o
> `Corte`.* **Com o acerto junto, a Melhoria pega o inimigo qualquer que seja a mistura dele.**

**O que custa:** *"Sobrecarga"* é um nome que diz **"ele está sobrecarregado"**, e `−2` na rolagem
não diz isso — diz *"ele erra mais"*. **É a opção mecanicamente mais limpa e a mais fraca de sabor.**

---

## Opção C — **as duas juntas, e a Melhoria sobe pra `Média`**

> **`Sobrecarga` · `Média` · *Até o fim do próximo turno do alvo, ele não usa Reação, e todo golpe dele sai com `−2` — na rolagem de acerto, ou na CD.`***

| `k` *(ações dele que rolam acerto)* | nega | em `Leve` | em **`Média`** |
|---|---|---|---|
| `0` | `47,45` | `2,64×` | `1,51×` |
| **`1`** — *o Sukuna* | **`58,40`** | `3,24×` ⚠ | **`1,85×`** |
| `2` | `69,35` | `3,85×` ⚠ | `2,20×` |
| `3` | `80,30` | `4,46×` ⚠ | `2,55×` |

**`1,10` ação negada, que é `Média` pela regra 1. Em `Média` ela cabe em todo `k`, com teto em `2,55×`.**

**E o precedente externo dessa combinação é exato, em dois sistemas:**

| | |
|---|---|
| **`Tasha's Mind Whip`**, D&D, **2º nível** | nega a reação **e** força o alvo a escolher entre mover, ação ou ação bônus. *Com três freios: salva, `1` rodada de duração, metade do efeito no sucesso* |
| **`Confused`**, 13th Age, **3º nível, Daily, save ends** | *"You can't make opportunity attacks **or use your limited powers**"* — **reação e recurso negados na mesma condição** |
| **`Laughing Fit`**, PF2e | **é exatamente esta escada:** reação no `Success`, reação + ação no `Failure`. *Um degrau de distância* |

**⚠ O que custa:** ela é **`Média`**, e **nenhum** dos três donos escreve `Média` hoje. *O gerador e o
`.docx` dizem `Leve`, o livro diz `Pesada`.* **A divergência da v0.219 não se fecha — ela vira um
terceiro valor**, e aí alguém precisa arbitrar à mão.

---

# O que morre, e por quê

| candidata | morre porque |
|---|---|
| **tranca uma ação** | **é o `Calado` e o `Enfeitiçado`**, publicados em `Média`. Vender por Melhoria uma condição que o catálogo já vende é duplicar entrada |
| **tranca ação + reação** | **é o `Atordoado`**, publicado em `Pesada`, palavra por palavra |
| **"custa o dobro de AÇÃO"** *(o câmbio do §6.1)* | dá no mesmo: `1` ação a menos. **É o `Calado` com outra ficção.** *E contra um inimigo de `1` ação ela tira a rodada inteira* |
| **tranca a `Intervenção`** | **três sistemas recusam vender isso como efeito genérico.** E ela tem duas leituras no teu próprio projeto (ver abaixo) |
| **drena o `refino`** | entrega `3,45` — tamanho de `Desarmado`. **Mas o problema é outro:** cada aptidão lê o refino com teto próprio, então o mesmo `−3` faz coisa diferente em cada bloco. **Falha o filtro dos dois mestres** |
| **"a `Recarga` não recarrega"** | o valor depende de **qual** habilidade aquele bloco pendurou no rótulo. Não tem número único |
| **um medidor que SOBE** *(a saída do LANCER)* | *"medidor que enche, não poço que esvazia"* — **é a porta que o campo aponta, e ela reabre a decisão §8.** O molde Daggerheart foi visto e descartado em 09/09 |

---

# ⚠ Uma coisa que apareceu no caminho e não é desta fila

**A `Intervenção` tem DUAS leituras, e o teu projeto não decidiu qual.**

| leitura | o texto que sustenta | quanto ela ADICIONA por rodada |
|---|---|---|
| **sai da cota** | peça 26 §6.1: *"Tudo que ele faz sai do dano por rodada da ficha"* | `0,00` |
| **é ação extra** | `a-intervencao.md`: ela acontece **fora do turno** — é uma 4ª ação | **`73,00`** |

> **Se a leitura certa é "ação extra", o chefe faz `292` numa rodada em que intervém, e não `219`.**
> *Com uma Intervenção por rodada numa luta de três rodadas, isso é **`+33%`** de dano na luta
> inteira, por fora da escada.*

**As duas frases estão escritas, em documentos diferentes, e ninguém as encostou uma na outra.**
*Vai pra fila — é buraco de bestiário, não de Melhoria.*

---

# O que eu recomendo, e por quê

> ## A **Opção A** — trava a `Reação`.

**Quatro motivos, em ordem de peso:**

| | |
|---|---|
| **1** | **é o único alvo que 100% do bestiário tem e que nenhuma outra peça já vende.** *Zero blocos têm PE; todos têm Reação — e nenhuma das treze condições nem das nove `Auxiliares` nega só a reação* |
| **2** | **o preço já existe publicado no teu próprio sistema, ao centavo.** *O `Trava` é `Leve` e entrega `36,50`. A conta não precisou de número novo* |
| **3** | **é o precedente externo mais forte de tudo** — truque em 2014, custo zero no Weird Wizard, tier mais baixo no LANCER, grau `Success` no PF2e |
| **4** | **fecha a divergência da v0.219 sem ninguém arbitrar**, no lado de `2` dos `3` donos |

**E ela cabe no nome.** *Ele está sobrecarregado: não sobra fôlego pra responder.* **Isso se narra na mesa em quatro palavras.**

**Se o `2,64×` acima do `Trava` te incomodar, o campo dá o freio pronto:** *o D&D 2024 rebaixou
`Shocking Grasp` de "nega toda Reação" pra **"nega só Ataque de Oportunidade"**.* **A versão freada é
"ele não faz ataque de oportunidade"**, que é estritamente mais fraca — e pro bestiário é quase a
mesma coisa, porque o ataque de oportunidade é o que o inimigo faz com a Reação dele.

---

# A pergunta, e ela é tua

1. **Qual opção?** `A` (Reação) · `B` (`−2` no acerto) · `C` (as duas, em `Média`)
2. **Se `A` ou `B`: o degrau é `Leve` ou `Média`?** *As duas passam o filtro. `Leve` fecha a
   divergência; `Média` é fiel ao tamanho do resto da família `Auxiliar`*
3. **Se `A`: Reação inteira, ou só o ataque de oportunidade?** *A segunda é o freio que o D&D 2024 escolheu*

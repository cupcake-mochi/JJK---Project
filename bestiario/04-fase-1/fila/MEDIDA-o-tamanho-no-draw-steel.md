# O `tamanho` validado contra o Draw Steel — item `16`

*10/09/2026. Conta em `medir-o-tamanho-no-draw-steel.py`, saída em `SAIDA-tamanho-draw-steel.txt`.*

> ***Pedido do Mizuki:*** *"Novamente, roubamos esse conceito de Draw Steel, n é bom olhar lá pra
> saber a validação? … **sempre métrica antes de resposta em achismo**."*
>
> ### Ele estava certo, e a medição derrubou a premissa do martelo inteiro.

---

# ⚠ PRIMEIRO: o `Draw Steel Heroes` ESTÁ no dump

**A `MEDIDA-o-tamanho` de 10/09 escreveu:**

> *"A mecânica de `size` do Draw Steel mora no `Draw Steel: Heroes` cap. 10, e **ela não abriu**. O
> `steelcompendium.io` renderiza em JS, o repositório de dados só tem o bestiário, e a busca web caiu
> duas vezes."*

**O `Rules/Draw Steel Heroes.md` está no dump que a gente puxou pra fila da recarga.** *A seção
`Size and Space` abre inteira.* **A frase acima é a única coisa deste projeto que era falsa por falta
de dado, e não por erro de conta.**

---

# `1` · O que o LIVRO diz — `size` é ESPAÇO, e só

> *"A creature's size indicates **how many squares they occupy** during combat, which defines the
> creature's space."*
>
> **Glossário:** *"An indication of a creature's **space** and their overall weight and height
> relative to other creatures."*
>
> *"**There is no limit** to what a creature's size might be."*

**E não existe estatística de defesa pra baixar.** *O Draw Steel resolve ataque com power roll contra
faixas — não tem `AC`, não tem `Defesa`.* **A troca "maior é mais fácil de acertar" não pode existir
lá, porque não há o que descer.**

*As `15` linhas do livro que ligam `size` a `edge`/`bane` são sobre **agarrar, movimento forçado e
mirar objeto** — nenhuma é sobre ser acertado.*

---

# `2` · E o que os `415` statblocks FAZEM — o preço é ZERO

*Normalizado por coorte (mesma organização, mesmo nível), pra tirar nível e organização da conta.*

| `size` | `n` | **Stamina rel.** | **EV rel.** | alcance melee | stability |
|---|---|---|---|---|---|
| `1T` | `8` | `0,900` | **`1,000`** | `1` | `0,0` |
| `1S` | `46` | `1,000` | **`1,000`** | `1` | `0,0` |
| `1M` | `222` | `1,000` | **`1,000`** | `1` | `0,0` |
| `1L` | `36` | `1,000` | **`1,000`** | `1` | `1,5` |
| `2` | `54` | `1,000` | **`1,000`** | **`2`** | `2,0` |
| `3` | `27` | `1,000` | **`1,000`** | **`2`** | `3,0` |
| `4` | `17` | `1,000` | **`1,000`** | **`3`** | `5,0` |
| `5` | `4` | `1,000` | **`1,000`** | **`4`** | `5,5` |

> ### O tamanho dá alcance. Não tira Stamina, não custa EV, e ainda DÁ stability.
> **`size 2+` contra `size 1M ou menor`: Stamina `1,000 ×`, EV `1,000 ×`.** *Exato, nos dois.*

**E as duas linhas do livro em que um herói fica maior:**

> *"While you are in your bear form, **your size is 2 and you gain a +1 bonus to distance with melee
> weapon abilities**."*

**Ganha tamanho E alcance, na mesma frase, sem pagar nada.**

---

# `3` · ⚠ E a pergunta que decide: bicho grande pega MAIS GENTE?

**O nosso `tamanho` dá DUAS coisas:** *alcance **e** "o golpe pega vizinhos a metade".* **A `2` mostrou
que o alcance ele copia do campo. E os vizinhos?**

*Parseando os `328` pares `📏 Melee N` + `🎯 alvo` dos statblocks, **somando as ações** — não a mediana
das linhas:*

| | ações | **pegam `2+` alvos** |
|---|---|---|
| `size 1` — qualquer sub-degrau | `206` | **`22%`** |
| **`size 2` ou maior** | `122` | **`43%`** |

> ### Bicho grande pega `2+` alvos `1,99 ×` mais. **E o preço continua ZERO.**
> *O `Omen Dragon`, `size 5`, tem golpe de corpo a corpo `Melee 4` em **"Two creatures or objects"**.*

---

# `4` · E o ORÇAMENTO DE ATRIBUTO — a `2ª` pergunta do martelo

**A nossa pergunta:** *o `tamanho` devolve `+5` de Destreza no `Colossal` nv20. Isso vira preço?*

**A pergunta equivalente lá:** *a soma dos cinco atributos cresce com o tamanho?*

| `size` | `n` | **Σ rel. à coorte** | Might | Agility |
|---|---|---|---|---|
| `1S` | `46` | `1,000` | `0,0` | `2,0` |
| `1M` | `222` | `1,000` | `1,0` | `2,0` |
| `1L` | `35` | `1,000` | `2,0` | `2,0` |
| `2` | `52` | `1,000` | `2,5` | `1,0` |
| `3` | `26` | `0,865` | `3,0` | **`0,0`** |
| `4` | `15` | `0,947` | `4,0` | `2,0` |
| `5` | `3` | `1,000` | `5,0` | `2,0` |

> ### A soma é a MESMA. O que muda é a FORMA — o Might sobe de `1` a `5`, e a Agility desce.
> **No campo, tamanho não compra orçamento de atributo: ele redistribui o mesmo orçamento.**

⚠ **E aqui a analogia tem limite, e vale dizer:** *lá nenhuma derivada lê um atributo — não há Defesa.*
**A nossa devolução de Destreza é artefato da fórmula `10 + Destreza + proteção`, e o Draw Steel não
tem esse acoplamento pra opinar sobre ele.** *O que ele diz é o mais fraco e ainda assim útil:*
**deixar o tamanho inflar o total de atributo seria coisa que o campo não faz.**

---

# ⟹ O QUE ISSO FAZ COM O MARTELO

## A premissa das cinco saídas era: *"o tamanho tem que ter uma troca"*

***Palavras dele, 10/09:*** *"vira regra, vamos seguir o molde de Draw Steel por enquanto… **mas
lembrando q tamanho tem q ter uma troca**."*

> ### As duas metades dessa frase não vêm do mesmo lugar.
> **"Seguir o molde do Draw Steel" e "ter uma troca" são incompatíveis** — *lá o molde é: **o tamanho
> não tem troca nenhuma**.*

**E a `MEDIDA-o-tamanho` já sabia disso, e escreveu:**

> *"**A troca abaixo é construída com os câmbios do Projeto-M, não copiada do Draw Steel.**"*

## O que a gente copiou, e o que a gente inventou

| | de onde vem |
|---|---|
| a **notação** de tamanho | Draw Steel — confirmado |
| o **alcance** por degrau | Draw Steel — confirmado, `size 2` = `Melee 2`, `size 4` = `Melee 3` |
| **pegar mais alvos** | Draw Steel — confirmado, `43%` contra `22%` |
| **o preço em Defesa** | ⚠ **nosso.** *Lá o preço é ZERO, e não existe defesa pra cobrar* |

> ### ⟹ O `Colossal` não é inconstruível porque a conta errou.
> **Ele é inconstruível porque a gente pôs preço num eixo que o campo entrega de graça — e o preço
> bateu num piso de fórmula.**

## E isso abre uma saída que não estava na lista

| # | a saída | o que ela custa |
|---|---|---|
| **`F`** 🆕 | **o `tamanho` não cobra nada**, como no campo. *Alcance e alvos vêm de graça, e quem preça o inimigo é a **categoria*** | **contradiz a instrução dele** — *"tamanho tem q ter uma troca"*. ⚠ *E o nosso ganho é maior que o deles: eles dão alcance e às vezes `2` alvos; a gente dá alcance **e** metade do dano em até `3` vizinhos, sempre* |

**As outras cinco (`A` a `E`) continuam válidas** — *elas são o desenho do Projeto-M, e o Projeto-M
pode cobrar onde o Draw Steel não cobra.* **Mas agora ele escolhe sabendo que a troca é invenção
nossa, não herança.**

> ⚠ **E se a `F` ganhar, sobra uma pergunta:** *o nosso ganho de tamanho é `1,2153 ×` a `1,65 ×` de
> dano — bem maior que o "às vezes `2` alvos" do campo.* **Dar isso de graça é dar mais do que o campo
> dá.** *A saída honesta da `F` seria encolher o ganho até o tamanho do deles, e aí não cobrar.*

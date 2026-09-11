# DECIDIDO — o item `9`: fica o `Capanga` da ESCADA, e a peça 26 perde três seções

*10/09/2026. **Martelo dele: a saída `B`.** Medição em `MEDIDA-o-encontro-misturado.md`, varredura em
`medir-o-encontro-misturado.py`.*

> ## O projeto tinha dois `Capanga`. Agora tem um.

---

# § 1 · O QUE FICA

> ### O `Capanga` é o da escada: **`8` corpos em pool · vida `= dano do grupo ÷ 4` · fator de dano `0,25` · `1` ação.**
> *`TABELA.md`, `RASCUNHO-5` Passo `1`, e é contra ele que toda a Fase 1 de 10/09 mediu.*

**O outro — `4` corpos, vida `chefe ÷ 4`, dano `chefe ÷ 3` — era o capanga da `Alcateia`, e a
`Alcateia` morreu quando a escada mudou.** *Ele estava certo por dentro; ele só não é mais o daqui.*

| o que o martelo custa | |
|---|---|
| ✅ **não quebra nada de 10/09** | o papel do `Capanga` (`17`), o empilhamento (`19`), a banda `21%`–`28%`, as três fichas de teste |
| ⚠ **quebra três seções da peça 26** | o §4.3, o §4.5 e o §5 — *e as três já vão no mesmo commit dos itens `5`, `6` e `11`* |

---

# § 2 · A TABELA NOVA DO §4.5 — medida, não escolhida

*Varredura de `201` frações do chefe × `29` níveis, procurando a que devolve os `67,5%` que o chefe
sozinho cobra.*

| sub-categoria | **o chefe fica com** | capangas | cobra | erro |
|---|---|---|---|---|
| **`sozinho`** | `100%` | — | `67,5%` | — |
| **`com um apoio`** | **`91,5%`** | `1` | `67,4%` | `−0,1%` |
| **`com dois`** | **`83,0%`** | `2` | `67,3%` | `−0,3%` |
| **`bando`** | **`74,5%`** | `3` | `67,2%` | `−0,4%` |

**O antigo dizia `100%` · `75%` · `50%` · `25%`.** *Aquilo era o câmbio `1/4`, e ele era do outro capanga.*

> ### ⟹ O câmbio do `Capanga` da escada é `8,5%` do chefe por corpo — praticamente `1/12`.
> *E os três primeiros degraus são exatos: `8,5` · `8,5` · `8,5`.*

## ⚠ E o câmbio NÃO é linear além de três corpos

| capangas | o chefe fica com | quanto o corpo tomou |
|---|---|---|
| `1` · `2` · `3` | `91,5%` · `83,0%` · `74,5%` | **`8,5%` cada** — `≈ 1/12` |
| `4` · `5` · `6` · `7` | `63,5%` · `47,0%` · `30,0%` · `13,5%` | **`11%` a `17%` cada** — `≈ 1/6` |
| **`8`** | `0%` | ⚠ **e aí ele cobra `71,6%`, `6,1%` quente** |

> **Um corpo sozinho morre na primeira rodada e não volta. Um esquadrão cheio cobre os próprios
> buracos, e cada corpo passa a valer o dobro.** *Por isso a segunda metade do esquadrão é mais cara
> que a primeira.*

## ⚠⚠ E a tabela é sensível a UM PONTO DE VIDA, o que já tem precedente escrito

*Com `1` capanga: o chefe a **`91,5%`** cobra `67,4%`, e a **`92%`** cobra `80,3%`.* **`0,5` ponto
percentual move o encontro em `13` pontos** — porque o chefe atravessa a borda de uma rodada.

> ***A peça 26 §8 já registrou exatamente isso:*** *"a linha do nível `2` publicava `115` de vida onde
> a regra pede `114`, e **um ponto de vida punha o chefe vivo numa quarta rodada**."*
>
> **⟹ As frações do §4.5 têm de sair com uma casa decimal, e não arredondadas pra "três quartos".**

---

# § 3 · E `1 Desastre + N Capangas` — o encontro que CRESCE, e agora tem preço

*Pela definição da própria peça: "a categoria é quantos personagens ele exige", e `fator = pessoas ÷ 4`.*

| o encontro | exige | fator | a soma ingênua diria | ela erra |
|---|---|---|---|---|
| `1 Desastre` sozinho | `4,00` | `1,000` | `1,00` | — |
| `1 Desastre + 1 Capanga` | `4,33` | `1,083` | `1,25` | `15,4%` |
| `1 Desastre + 2 Capangas` | `4,67` | `1,167` | `1,50` | `28,6%` |
| **`1 Desastre + 4 Capangas`** | **`5,33`** | **`1,333`** | `2,00` | ### **`50,0%`** |
| `1 Desastre + 8 Capangas` | `7,00` | `1,750` | `3,00` | `71,4%` |

> ### A régua, em uma linha:
> **`fator do encontro = fator do chefe + (capangas × `0,083`)`**, e o `0,083` é `1/12`.
> *Ela vale até `4` capangas somados a um chefe inteiro. Acima disso o corpo passa a valer mais, e o
> mestre lê a tabela do §2.*

⚠ **E ela substitui o `0,25` da escada como preço de ENCONTRO.** *O `0,25` continua sendo o fator do
`Capanga` como CATEGORIA — o preço de um esquadrão cheio dividido por oito. **São duas leituras do
mesmo bicho, e a diferença é se ele vem sozinho ou em bando.***

---

# § 4 · AS MEXIDAS NO REPOSITÓRIO — ⚠ e elas somam às do item `5`

*Todas na peça 26. **Com os itens `5`, `6` e `11`, são cinco seções num commit só.***

| # | seção | o que trocar |
|---|---|---|
| **`1`** | **§5** | *"um corpo grande vale **quatro** pequenos"* ⟹ **`oito`**, e a derivação vira `vida = dano do grupo ÷ 4` · `dano = fator 0,25`. ⚠ **A prova dos "nove golpes" cai junto** — o esquadrão novo entrega `8 + 4` em duas rodadas, não `4 + 3 + 2` em três |
| **`2`** | **§4.5** | a tabela inteira: `100%` · **`91,5%`** · **`83,0%`** · **`74,5%`**, e as frações com uma casa decimal |
| **`3`** | **§4.3** | *"o capanga é um quarto da vida com um TERÇO do dano"* ⟹ **`1/12` da vida com um QUARTO do dano** |
| **`4`** | **§4.3** | a comparação com a `Ronda` (`0,75×`–`0,77×`) é da escada morta — **ou sai, ou vira a medição nova** |
| **`5`** | `conferir-bestiario.py` | a checagem **`5`** — *"o câmbio é medido, não guardado… o `4` publicado tem de ser o que ela devolve"* ⟹ **o `8`** |

> ### ⚠ A checagem `5` do validador VAI ACENDER até a peça mudar, e ela está certa em acender.
> *Ela roda a simulação de fogo concentrado e confere que o câmbio publicado é o que ela devolve.*
> **Com o `4` publicado e o `8` implementado, ela é a guarda que pegaria isso — se alguém tivesse
> rodado ela contra a escada nova.**

---

# § 5 · O QUE SOBRA, e é pequeno

> ### 🆕 Item `22` — o esquadrão cheio de `8` cobra `71,6%` contra os `67,5%` do chefe: **`6,1%` quente**.
> *Duas saídas: cortar `6%` da vida do capanga, ou declarar a folga.* **A segunda tem precedente — o
> `tamanho` já põe `≈18%` fora da conta de propósito, declarado no `RASCUNHO-5` Passo `3`.**
>
| custo | 🟢 **BARATO** — a conta está feita, é escolha |
|---|---|

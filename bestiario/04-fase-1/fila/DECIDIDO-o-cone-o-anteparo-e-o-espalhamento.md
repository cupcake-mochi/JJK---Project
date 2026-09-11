# DECIDIDO — os itens `27`, `28` e `29`

*10/09/2026. **Ele:*** *"Valide as soluções de cada e pode bater o martelo no que for o melhor achado,
ideal comparar com outros sistemas q estamos nos baseando."*
**Conta em `medir-o-espalhamento-das-formas.py`, saída em `SAIDA-espalhamento-das-formas.txt`.**

---

# ⚡ `27` · A ABERTURA DO CONE — e o argumento DELE é o motivo de escrever

***Ele:*** *"é padronizado, n? meio q se vc pega um VTT por exemplo, vc n decide largura e alcance de
um cone, so pega o valor em M"*

## ⟹ Ele está certo. E é exatamente por isso que tem de estar escrito.

| o que o VTT faz | |
|---|---|
| **Foundry VTT** | *"os templates de cone vêm com cerca de **`53` graus** por padrão, **mas podem ser mudados nas configurações do template**"* |
| **Roll20** | *"oferece a opção de **inserir ângulos customizados**"* pra montar o cone de 5e |

> ### O VTT não decide o ângulo. Ele LÊ o ângulo de uma configuração.
> **E essa configuração vem do sistema.** *Se o nosso manual não diz, quem monta a mesa no Foundry
> escolhe — e duas mesas do mesmo sistema desenham áreas diferentes.*
>
> **`53` graus é exatamente "a largura é igual à distância"** *(`arctan(0,5) × 2 = 53,13°`)* — **o
> padrão que o Foundry já traz de fábrica.**

## ✅ MARTELO: a abertura é a do D&D — `53` graus, e a frase é uma só

> ### **"A largura do cone em qualquer ponto é igual à distância daquele ponto até você."**
> *A `4` quadrados de você, o cone tem `4` de largura.* **É o padrão de fábrica do Foundry, é a regra
> escrita do D&D 2024, e é a única que se desenha contando quadrado.**

⚠ *O PF2e usa um quarto de círculo (`90°`, `1,57×` mais área) — e a regra deles remete a uma FIGURA do
livro, não a uma frase. Não dá pra "seguir o campo": os dois padrões existem.*

---

# ⚡ `28` · AS DIMENSÕES DO `Anteparo` — ele mandou colocar

***Ele:*** *"Vamos colocar as dimensões"*

**O `partD.js` publica:** *`Anteparo` (`Controle`, `Média`) — "Deixa uma parede ou escudo com
`10 × Classe` de pontos de vida, por `1` minuto."* **Sem comprimento, sem altura, sem colocação.**

## ✅ MARTELO: o `Anteparo` é a `Linha` daquela Classe, DE PÉ — e não entra número novo

> ### **O `Anteparo` ocupa os mesmos quadrados que a `Linha` da Classe dele, arrumados como você quiser, cada quadrado partilhando um LADO com outro. Altura mínima `2` quadrados. Colocado num ponto a até o alcance do feitiço.**

| Classe | a `Linha` cobre | ⟹ o `Anteparo` | em metro |
|---|---|---|---|
| `0` | `6` quadrados | `3 × 2` | `4,5 m` de comprimento × `3 m` de altura |
| **`1`–`5`** | **`12`** | **`6 × 2`** | **`9 m` × `3 m`** |
| `6`–`7` | `20` | `10 × 2` | `15 m` × `3 m` |

**E ele sobe com `Maior` como qualquer área.**

## Por que assim, e não com número novo

| | |
|---|---|
| **"parede OU escudo"** já está no texto | *quadrados contíguos arrumados como você quiser cobre os dois: esticado é parede, compacto é escudo* |
| **é literalmente o `X wall` do Draw Steel** | *"o número `X` é quantos quadrados formam o muro… cada quadrado tem de partilhar pelo menos um **lado** com outro"* |
| **a altura `≥ 2` não é arbitrária** | *`3 m` é o que ninguém passa por cima. Com `1` quadrado não é parede, é degrau* |

> ⚠ **E ela é MENOR que a do D&D, declarado:** *a `Wall of Fire` é `18 × 6 m` = `48` quadrados; a
> nossa na `Classe 1`–`5` é `12`.* **Mas lá ela é um feitiço inteiro de `4º` círculo, e aqui é UMA
> Melhoria `Média` dentro de um feitiço que ainda faz outra coisa.** *Comparar as duas direto seria
> comparar um feitiço com um pedaço de feitiço.*

---

# ⚡ `29` · O ESPALHAMENTO — ⚠⚠ ELE ESTAVA CERTO E EU ESTAVA ERRADO

***Ele:*** *"Mas o da linha pega um alcance maior, ent ta justo, n?"*

## ⟹ Está justo. E o meu `20×` era conta errada.

> ### O erro: eu comparei `Cone` e `Linha` no mesmo ÍNDICE de degrau. **Eles não começam no mesmo degrau.**
> *A escada compartilhada é `4,5 · 9 · 18 · 30 · 60 m`.* **O `Cone` começa no degrau `1` (`4,5 m`) e a
> `Linha` no degrau `3` (`18 m`).** *Uma compra de `Maior` não põe os dois no mesmo lugar.*

## A comparação certa — mesma Classe, mesma compra

**`Classes 1`–`5`:**

| compra | `Esfera` | `Cone` | `Linha` |
|---|---|---|---|
| **base** | `3 m` = `13` q | `4,5 m` = **`4` q** | `18×1,5 m` = `12` q |
| `+1` | `4,5 m` = `28` q | `9 m` = `18` q | `30×1,5 m` = `20` q |
| `+2` | `6 m` = `50` q | `18 m` = `72` q | `60×1,5 m` = `40` q |
| `+3` *(teto)* | `9 m` = `113` q | `30 m` = **`200` q** | `60×1,5 m` = `40` q |

### E o alcance, que é o ponto dele — a `Linha` vai MUITO mais longe

| | o `Cone` alcança | a `Linha` alcança | |
|---|---|---|---|
| **base** | `4,5 m` | `18 m` | ### **`4,00×` mais longe** |
| teto | `30 m` | `60 m` | `2,00×` mais longe |

> ### ⟹ Na base a `Linha` é MAIOR (`12` contra `4` q) **E** alcança `4×` mais longe. O `Cone` é que é a compra ruim ali.
> **A troca que ele descreveu é real, e ela está no sentido certo.**

## E o campo espalha QUANTO entre as formas dele?

| sistema | espalhamento entre as formas | quem contra quem |
|---|---|---|
| D&D 2014 | `1,52×` | cone `19` q contra line `12` q |
| **D&D 2024** | **`2,79×`** | sphere `52` q contra cone `19` q |
| ### **Draw Steel** | ### **`13,44×`** | burst `121` q contra cube `9` q |
| **o NOSSO, na base** | ### **`2,79×`** | ✅ **idêntico ao D&D 2024** |
| o nosso, `Classes 1`–`5` no teto | `5,00×` | dentro dos `13,44×` do Draw Steel |
| ⚠ o nosso, `Classes 6`–`7` no teto | **`20,00×`** | ❌ fora de todos |

> ## ✅ MARTELO: NÃO repreçar. O `29` não é defeito — o campo espalha igual ou mais.
> **O nosso espalhamento na base é `2,79×`, exatamente o do D&D 2024.** *E o filtro de dominância do
> projeto (`3,00×`, peça 19 §3.6) passa na base em todas as três Classes.*

## ⚠ MAS sobrou UM buraco de verdade, e ele é estreito

**Nas `Classes 6`–`7` a `Linha` já nasce no degrau `4` (`30 m`).** *Com `+3` ela sobe UM degrau e bate
no teto da escada; o `Cone` sobe os TRÊS.*

> ### A `Linha` PAGA por três degraus e recebe um. É desperdício, não desequilíbrio.

**A saída, e ela não tem número novo:** *quando o comprimento da `Linha` bate no topo da escada, as
compras seguintes de `Maior` sobem a **LARGURA** — `1,5 → 3 → 4,5 m`.*

**É literalmente o `A × B line` do Draw Steel** *(`241` linhas medidas, larguras `1` a `4`, razão
mediana `5:1`)*. **Com ela, o `Classes 6`–`7` no teto sai de `20,00×` para `6,67×`** — *dentro da banda
do Draw Steel, e a `Linha` passa a receber o que paga.*

---

# ⟹ O QUE VAI PRO REPOSITÓRIO

*⚠ Eu não escrevo lá. Entra na `MEXIDAS-no-repositorio.md`.*

| # | onde | o quê |
|---|---|---|
| **`27`** | `partC.js`, a Forma `Cone` | ➕ *"A largura do cone em qualquer ponto é igual à distância daquele ponto até você."* |
| **`28`** | `partD.js`, a Melhoria `Anteparo` | ➕ as dimensões: os quadrados da `Linha` da Classe, contíguos por lado, altura `≥ 2`, colocado num ponto |
| **`29a`** | — | ❌ **NADA.** *Não repreçar — o campo espalha igual ou mais* |
| **`29b`** | `partC.js`, a escada / a Forma `Linha` | ➕ *"Quando o comprimento da `Linha` chega ao topo da escada, `Maior` passa a subir a largura: `1,5 → 3 → 4,5 m`."* |

> ### ⚠ Os quatro são do lado do JOGADOR, e os quatro são de BAIXO risco:
> **`27` e `28` escrevem número que faltava** *(ninguém montou nada em cima do que não existe)*.
> **`29b` só dá destino a uma compra que hoje é jogada fora.** *Nenhum feitiço pronto encolhe.*
>
> **⟹ Nenhum dos quatro reabre o item `15`.** *O `15` era o `29a`, e o `29a` morreu.*

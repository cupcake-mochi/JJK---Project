# MEDIDA — raio ou diâmetro? *(pergunta dele, 10/09/2026)*

***Pergunta:*** *"ao invés de raio, não seria melhor usar diâmetro pras coisas? Ou não fica mais
entendível?"*

---

# § 1 · O CAMPO É UNÂNIME, e nenhum dos três usa diâmetro

| sistema | como escreve | o número é |
|---|---|---|
| **D&D 2024** | *"20-foot **radius** Sphere"* · *"10-foot Emanation"* | **raio**, em pés |
| **Pathfinder 2e** | *"20-foot **burst**"* — *"spreading in all directions to a specified **radius**"* | **raio**, em pés |
| **Draw Steel** | *"**burst 2**"* — *"the number X is the **radius** of the burst"* | ### **raio, em QUADRADOS** |

> ### `0` de `3` usam diâmetro.

---

# § 2 · MAS O ARGUMENTO PRO DIÂMETRO EXISTE, e é bom

*`deltasdnd.blogspot.com`, "Radius or Diameter?" (2023) — ele levantou a questão e enquetou a
comunidade.*

| a favor do DIÂMETRO | a favor do RAIO |
|---|---|
| **consistência:** *"toda outra forma é expressa pela largura TOTAL — quadrado, linha, cubo, retângulo — e só o círculo é listado por meia-largura"* | *"quando eu jogo de conjurador, eu penso em raio, não em diâmetro"* — você escolhe um ponto e pergunta até onde vai |
| **VTT:** o Roll20 pede largura total, e o raio obriga a converter | convenção matemática |
| **mundo real:** pneu, pizza e poço se medem por diâmetro | mira: quem está dentro, quem está fora |

> **Ele reconheceu as vantagens práticas do diâmetro e ficou com o RAIO** — *"overwhelming preference
> among the classic D&D community"*.

## ⚠ E o argumento da consistência NÃO se aplica ao nosso sistema

**A escada dele quebra porque o D&D tem CUBO e RETÂNGULO, que se medem por lado.**
*A nossa tem `Esfera`, `Cone` e `Linha`.* **E o `Cone` e a `Linha` são medidos DA ORIGEM PRA FORA** —
`4,5 m` de cone é o quanto ele alcança a partir de você.

> ### No nosso sistema é o RAIO que é consistente: as três formas dizem "até onde vai a partir da origem".
> *Trocar a esfera pra diâmetro é que criaria a inconsistência que o Delta reclama.*

---

# § 3 · OS NÚMEROS, lado a lado

| | `d1` | `d2` | `d3` | `d4` | `d5` |
|---|---|---|---|---|---|
| **raio em metros** *(hoje)* | `3 m` | **`4,5 m`** | `6 m` | `9 m` | `15 m` |
| **diâmetro em metros** | `6 m` | `9 m` | `12 m` | `18 m` | `30 m` |
| **raio em quadrados** | `2` | `3` | `4` | `6` | `10` |
| largura em quadrados | `4` | `6` | `8` | `12` | `20` |

| | decimais |
|---|---|
| raio em metros | **`1`** — o `4,5` |
| diâmetro em metros | `0` |
| raio em quadrados | `0` |

> **O diâmetro mata o único decimal da escada. É o argumento concreto mais forte a favor dele.**
> ⚠ *Mas o `4,5 m` não some do sistema — ele é a base do `Cone` e aparece na escada de `Alcance`.*

---

# § 4 · ⚠ E O PROBLEMA DE VERDADE NÃO É RAIO NEM DIÂMETRO. É METRO.

**A comunidade diz o que trava na mesa, e não é a palavra:**

> *"Áreas de efeito são descritas com termos como '20 ft de raio'… **e muitos jogadores não entendem
> conceitos de geometria como o que é raio ou diâmetro**."*
>
> **E a resposta que o campo deu não foi renomear: foi o TEMPLATE.** *"clareza instantânea de alcance"*.

**`raio 3 m` obriga duas contas de cabeça:** *dividir por `1,5` pra saber quantos quadrados, e dobrar
pra imaginar a largura.* **`burst 2` do Draw Steel não obriga nenhuma.**

---

# ⟹ AS TRÊS SAÍDAS, com o custo

| | o que fazer | custa |
|---|---|---|
| **`A`** · fica **raio em metro** | nada | zero. *E é o que os `3` sistemas fazem* |
| **`B`** · vira **diâmetro em metro** | `6 · 9 · 12 · 18 · 30 m` | ⚠ **`89` menções a "raio" no repositório**, e **mexe na ficha do JOGADOR** — é o item `15`, que ele mandou só anotar. *E cria a inconsistência com `Cone` e `Linha`* |
| **`C`** ⭐ · fica raio, **e imprime a grade junto** | *"raio `3 m` — `4` quadrados de largura"* | **zero em regra.** *É só o texto* |

> ## Recomendação: **`C`**.
> **Ela resolve o que trava de verdade — a conversão — sem tocar em regra nenhuma, sem mexer no lado
> do jogador, e sem criar a inconsistência com o `Cone` e a `Linha`.**
>
> *E é literalmente o que o Draw Steel faz: o número que ele imprime é o que você conta na grade.*

⚠ **E se for `B` mesmo assim, ela é BARATA de decidir e CARA de executar** — *as `89` menções são
achado-e-troca, mas cinco delas são feitiços prontos do `partF.js` com o número no meio da frase.*

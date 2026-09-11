# O teto de empilhamento do `Capanga` — item `19`

*10/09/2026. Conta em `medir-o-empilhamento.py`, saída em `SAIDA-o-empilhamento.txt`.*

> **Achado medindo o `Controlador` contra o Draw Steel:** *o nosso `Capanga` não tem trava nenhuma
> pra quantos corpos batem na MESMA pessoa.*

---

# O buraco, com número

**nv20:** *o capanga bate `37` · são `8` corpos · o personagem tem `163` de vida.*

| quantos batem no mesmo alvo | dano | % da vida de `1` PC | mata? |
|---|---|---|---|
| `1` | `37` | `23%` | não |
| `2` | `74` | `45%` | não |
| `3` | `111` | `68%` | não |
| `4` | `148` | `91%` | não |
| **`8`** | **`296`** | **`181%`** | **SIM** |

> ### Bastam `4,4` corpos pra derrubar alguém. Hoje nada na regra impede os `8`.
> **Uma pessoa morre com folga na primeira rodada, e o mestre nem precisa querer.**

---

# `1` · A trava do Draw Steel tem DUAS partes

> *"Each target of a minion's signature ability is affected by only **one instance** of the ability.
> But when **two or three (at maximum)** of a squad's minions attack the same creature simultaneously,
> each additional minion causes the ability to deal extra damage equal to the minion's **free strike
> value**."*
>
> *"Because a minion's free strike value is typically lower than the average damage of their signature
> ability, **it's usually more effective to have each minion target a different hero**."*

| parte | o que ela faz |
|---|---|
| **teto DURO** — `2` ou `3` | impede a alfinetada de `8` |
| **desconto** — free strike no lugar da assinatura | **tira a vontade** de usar o teto |

---

# `2` · O desconto, MEDIDO — `115` minions

*Power roll = `2d10` + bônus, faixas `≤11` / `12-16` / `17+`, e natural `19-20` sempre dá tier `3`.
O dano esperado sai da distribuição inteira, não do meio da faixa.*

| | mediana | média | mín | máx |
|---|---|---|---|---|
| free strike | `2,00` | `2,48` | `1` | `5` |
| assinatura esperada | `4,00` | `4,27` | `1,9` | `8,4` |
| **razão `fs ÷ assinatura`** | **`0,573`** | `0,579` | `0,49` | `1,08` |

> ### O corpo empilhado entrega `57,3%` do que entregaria batendo em outro alvo.
> *A frase do livro — "typically lower" — tem número: **`0,573`**.*

## E o que isso faz com a escolha do mestre

| | empilhar | espalhar | empilhar entrega |
|---|---|---|---|
| `2` corpos | `1,573` assinaturas | `2,000` | **`78,7%`** — perde `21,3%` |
| `3` corpos | `2,146` assinaturas | `3,000` | **`71,5%`** — perde `28,5%` |

> **O teto duro impede o pior caso. O desconto faz o mestre não QUERER chegar nele.**

---

# `3` · A trava traduzida — o que cada forma entrega

*nv20, contra um personagem de `163` de vida.*

| forma | máx num alvo | % da vida do PC | mata? |
|---|---|---|---|
| **sem trava — hoje** | **`296`** | **`181%`** | **SIM** |
| teto `3`, extras a `0,573` *(o do campo)* | `79` | `49%` | não |
| **teto `3`, extras a METADE** *(o `Estilhaço`)* | **`74`** | **`45%`** | não |
| teto `2`, extras a metade | `56` | `34%` | não |
| teto `3`, sem desconto | `111` | `68%` | não |
| teto `2`, sem desconto | `74` | `45%` | não |

> ⚠ **E a trava NÃO encolhe o enxame.** *Com teto `3` e `4` personagens, os `8` corpos ainda entregam
> tudo — eles só não podem CONCENTRAR.* **O dano total não muda enquanto houver alvo pra todo mundo.**
>
> **Então a trava não mexe na razão `1,01 ×` que a escada do `Capanga` publica.** *Ela mexe só no caso
> degenerado.*

---

# `4` · ⚠⚠ E o `tamanho` piorou isso HORAS depois

**A saída `F` do item `16` deu ao `Grande` "o alvo + metade em `1` vizinho", de graça.**

| | alvos atingidos | dano total | vs `1` PC |
|---|---|---|---|
| `8` capangas `Médio`, sem trava | `8` | `296` | `181%` |
| **`8` capangas `Grande`, sem trava** | **`16`** | **`444`** | **`272%`** |
| `8` capangas `Grande`, teto `3` + metade | `6` | `130` | `79%` |

> ### Um `Capanga` `Grande` sem trava é o pior caso do bestiário inteiro.
> **`444` de dano espalhado em `16` alvos, num grupo de `4` pessoas com `163` de vida cada.**

---

# ⟹ A recomendação

> ## Teto `3`, extras a **METADE**.

**Dois motivos, e o segundo é o forte:**

| | |
|---|---|
| **`1`** | `0,50` está a `12,7%` do `0,573` medido — **dentro do ruído da amostra** *(a razão vai de `0,49` a `1,08`)* |
| **`2`** | ### "metade" é a fração que o sistema JÁ publica |

**O `Estilhaço` (`Leve`) diz *"metade dos dados respinga em quem estiver do lado"*, e o `tamanho`
acabou de adotar *"o alvo + metade em `1`"*.**

> **Usar a mesma fração é uma regra a menos pra decorar** — e o Bestiário inteiro passa a ter UMA
> fração de respingo, não duas.

**E o teto `3` em vez de `2`:** *o livro deles escreve "two or three (at maximum)" e não escolhe. O
`3` deixa o mestre montar a jogada de "cercar um" sem que ela mate — `45%` da vida.* **O `2` fecha
demais: `34%` não assusta ninguém.**

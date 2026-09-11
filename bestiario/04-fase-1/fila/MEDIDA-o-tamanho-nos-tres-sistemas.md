# O `tamanho` nos três sistemas — Draw Steel · D&D 2024 · Pathfinder 2e

*10/09/2026. Conta em `medir-o-tamanho-nos-tres-sistemas.py`, saída em
`SAIDA-tamanho-tres-sistemas.txt`.*

> ***Pedido do Mizuki:*** *"Valida com os outros exemplos q temos, Draw Steel, D&D e Pathfinder, deve
> ter auxílios nas versões atualizadas para que sirva como cálculo e média pra gente."*

| sistema | amostra | o que tem |
|---|---|---|
| **Draw Steel** | `416` statblocks | *sem estatística de defesa — ataque é power roll* |
| **D&D 2024 SRD** | `331` monstros | `size` · `CR` · `AC` · `HP` · `6` atributos |
| **Pathfinder 2e** | **`4.791` criaturas** | `size` · nível · `AC` · `HP` · `6` atributos |

*O PF2e foi puxado do AoN em 10/09 — `puxar-pf2e-tamanho.py`. O que já estava em disco era só texto
de habilidade, sem `size`.*

---

# `1` · O tamanho NÃO mexe na defesa. Em nenhum dos três.

*Normalizado por coorte de desafio — `CR` no D&D, nível no PF2e.*

| tamanho | o nosso | **D&D 2024: AC rel.** | `n` | **PF2e: AC rel.** | `n` |
|---|---|---|---|---|---|
| `Tiny` | `Minúsculo` | — | `0` | **`1,000`** | `194` |
| `Small` | `Pequeno` | `1,016` | `84` | **`1,000`** | `491` |
| `Medium` | `Médio` | **`1,000`** | `90` | **`1,000`** | `2238` |
| `Large` | `Grande` | **`1,000`** | `108` | **`1,000`** | `1024` |
| `Huge` | `Imenso` | **`1,000`** | `34` | **`1,000`** | `410` |
| `Gargantuan` | **`Colossal`** | **`1,000`** | `15` | **`1,000`** | `434` |

> ### D&D espalha `1,016 ×`. PF2e espalha `1,000 ×` — exato, em `4.791` criaturas.
> **E o Draw Steel não tem defesa pra espalhar.**

## E o nosso

**O `Colossal` pede Defesa `7` pontos abaixo do `Médio`.** *Num nv20 isso é `18 → 11`.*

> ### `0,611 ×` — contra `1,000 ×` em dois sistemas e "não existe" no terceiro.

---

# `2` · O `Dex`, porque a NOSSA Defesa lê a Destreza

| | Medium | Gargantuan | `n` |
|---|---|---|---|
| **D&D 2024** | `1,000` | `1,000` | `15` — *amostra pequena demais pra afirmar* |
| **PF2e** | `1,000` | **`0,833`** | `434` |

**Só o PF2e mostra bicho gigante com menos Destreza, e por `16,7%`.** *O nosso `Colossal` no nv20 vai
de Destreza `5` pra `0` — `100%`.*

---

# `3` · ⟹ O tamanho NÃO adiciona orçamento de atributo. Nos três.

| tamanho | **D&D 2024** | `n` | **PF2e** | `n` |
|---|---|---|---|---|
| `Small` | `1,029` | `84` | `1,000` | `491` |
| `Medium` | `1,034` | `90` | `1,000` | `2238` |
| `Large` | `1,000` | `108` | `1,000` | `1024` |
| `Huge` | `0,973` | `34` | `1,000` | `410` |
| `Gargantuan` | **`0,992`** | `15` | **`0,964`** | `434` |

**Draw Steel** *(Σ dos cinco, por organização + nível)*: `1S` `1,000` · `1M` `1,000` · `1L` `1,000` ·
`2` `1,000` · `5` `1,000`.

> ### Em três sistemas, o bicho maior tem o MESMO orçamento — ou um pouco MENOS.
> **Nenhum deles deixa o tamanho comprar atributo.** *O que muda é a forma: no Draw Steel o `Might`
> sobe de `1` a `5` e a `Agility` desce.*

---

# `4` · ⚠⚠ E O ACHADO QUE DECIDE A SAÍDA `F`

**A saída `F` é "não cobra, e encolhe o ganho até o tamanho do campo".** *Então: quanto o tamanho
ganha lá?*

*Medido em `327` ações de corpo a corpo do Draw Steel — alvos esperados por ação.*

| `size` | ações | **alvos esperados** | vs `1M` | alcance melee | o nosso |
|---|---|---|---|---|---|
| `1M` | `125` | `1,280` | **`1,000`** | `1` | `Médio` = `1,0000 ×` |
| `1L` | `40` | `1,275` | `0,996` | `1` | — |
| **`2`** | `65` | `1,431` | **`1,118`** | **`2`** | `Grande` = `1,2153 ×` |
| **`3`** | `31` | `1,484` | **`1,159`** | **`2`** | `Imenso` = `1,4321 ×` |
| **`4`** | `20` | `1,450` | **`1,133`** | **`3`** | `Colossal` = `1,6500 ×` |
| **`5`** | `5` | `1,400` | **`1,094`** | **`4`** | — |

> ## O ALCANCE sobe em escada. Os ALVOS não sobem.
> **`1,118` · `1,159` · `1,133` · `1,094`** — *do `size 2` ao `size 5`, o ganho de alvos é PLANO.*

**Juntando:** `size 1` entrega `1,228` alvos por ação · `size 2+` entrega `1,451`.

> ### O ganho de tamanho no campo é `1,181 ×`, e ele é UM DEGRAU, não uma escada.
> **O nosso topo é `1,650 ×` — `1,40 ×` o do campo.** *E o nosso `Grande`, a `1,2153 ×`, já está
> acima do TETO deles.*

---

# ⟹ O QUE ISSO DÁ PRA SAÍDA `F`, com número

***Decisão dele, 10/09:*** *saída `F` — "não cobra, e encolhe o ganho".*

## A forma que o campo publica

| eixo | como o campo faz | o que a gente tem |
|---|---|---|
| **alcance** | **escada** — `size 2` = `Melee 2`, `size 4` = `3`, `size 5` = `4` | ✅ **igual** — `1,5` · `3` · `4,5` · `6 m` |
| **alvos** | **UM degrau**, `≈ 1,18 ×`, plano do `size 2` pra cima | ⚠ **escada** — `1,2153` · `1,4321` · `1,6500` |
| **defesa** | **não mexe** — `1,000 ×` em `4.791` criaturas | ⚠ **`−2` · `−4` · `−7`** |
| **atributo** | **não adiciona** — mesmo orçamento em três sistemas | ⚠ *devolve `+5` no `Colossal` nv20* |

## E a `F` fecha a `2ª` pergunta de graça

**Se o `tamanho` para de cobrar em Defesa, a Defesa para de cair.** *E se a Defesa não cai, a Destreza
obrigada não cai — **não existe ponto devolvido pra preçar**.*

> ### A `2ª` pergunta do martelo some junto com a `1ª`, e some pelo mesmo motivo.
> **E o campo confirma as duas com a mesma medição:** *AC plana e orçamento de atributo plano são a
> mesma decisão de desenho vista de dois lados.*

## ⚠ O que a `F` custa, e tem de ficar declarado

**Um bicho de `Grande` pra cima entrega `≈ 18%` a mais que um `Médio` da mesma categoria, de graça.**

*O campo aceita isso porque o preço deles sai de **organização + nível** e absorve a forma. **O nosso
preço sai da categoria, e ela não sabe do tamanho.***

> **Então a `F` põe `+18%` de encontro fora da conta.** *É pouco, é o que o campo faz, e é o preço de
> seguir o molde — **mas tem de estar escrito**, não descoberto na mesa.*

⚠ **E ela cruza com o item `19`** — *o teto de empilhamento do `Capanga`.* **Oito capangas `Grande`
espalhando a metade em vizinhos é o mesmo problema, multiplicado por oito.**

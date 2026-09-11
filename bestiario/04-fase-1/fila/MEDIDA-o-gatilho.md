# O gatilho da `Chama Divina` — item `13`

*10/09/2026. Conta em `medir-o-gatilho.py`, saída em `SAIDA-o-gatilho.txt`.*

> **A pergunta da fila:** *"só depois de `Desmembrar` e `Clivar`" não é nenhum dos quatro rótulos.*
> **É quinto rótulo, ou texto da ação?**

### ⟹ Nenhum dos dois. **É um EIXO SEPARADO**, e os três sistemas concordam.

---

# `1` · D&D 2024 SRD — dois campos, e o de pré-requisito existe

*`989` ações em `331` monstros.*

| campo | o que ele carrega | quantos |
|---|---|---|
| **`usage_limits`** | **FREQUÊNCIA** — `RECHARGE_ON_ROLL` `73` · `PER_DAY` `27` · `RECHARGE` `13` | `113` *(`11%`)* |
| **`limited_to_form`** | **PRÉ-REQUISITO** | `17` *(`1,7%`)* |

**E o pré-requisito deles é literalmente o nosso caso:**

> `Nightmare Haunting (Requires Soul Bag)`
> `Entangling Rope (Requires Magic Rope)`
> `Bite (Tiger or Hybrid Form Only)`
> `Handaxe (Humanoid or Hybrid Form Only)`

> ### O SRD tem DOIS campos, e o pré-requisito NÃO entra na lista de frequência.
> **E os dois saem impressos no MESMO lugar: parêntese depois do nome.**

⚠ **E o pré-requisito deles é CURTO** — mediana `24` caracteres, de `17` a `28`.
*O nosso — "depois de `Desmembrar` e `Clivar`" — tem `33`.* **Mesma faixa.**

---

# `2` · Draw Steel — `Trigger:` é campo NOMEADO

*`544` blocos de habilidade em `416` statblocks.*

| | quantos | |
|---|---|---|
| com **`Trigger:`** — campo nomeado | `153` | **`28%`** |
| com pré-requisito solto em PROSA | `32` | `6%` |

> **O campo nomeado é `4,8 ×` mais comum que a condição em prosa.** *Lá ele é uma LINHA dentro do
> bloco da habilidade, não um parêntese.*

---

# `3` · Pathfinder 2e — QUATRO campos, e eles são eixos diferentes

*`677` habilidades.*

> ⚠ **AMOSTRA ENVIESADA:** *ela veio de uma busca por RECARGA. **Use a EXISTÊNCIA dos campos, não a
> proporção.***

| campo | | |
|---|---|---|
| `Effect` | `451` | `67%` |
| `Trigger` | `354` | `52%` |
| `Frequency` | `150` | `22%` |
| **`Requirements`** | `144` | `21%` |

> ### O PF2e separa em quatro: `Frequency` (quantas vezes) · `Trigger` (o que dispara) · `Requirements` (o que precisa estar valendo) · `Effect` (o que acontece).
> **`Frequency` e `Requirements` são campos DIFERENTES, e os dois existem.**

---

# ⟹ O VEREDITO

| sistema | frequência | pré-requisito | onde sai impresso |
|---|---|---|---|
| **D&D 2024** | `usage_limits` | **`limited_to_form`** | **parêntese após o nome** |
| **Draw Steel** | palavra-chave | prosa / **`Trigger:`** | linha no bloco |
| **Pathfinder 2e** | `Frequency` | **`Requirements`** | linha no bloco |
| — **o nosso** — | `4` rótulos | ⚠ **NÃO EXISTE** | — |

> ### Nos três, pré-requisito e frequência são EIXOS SEPARADOS.
> **Nenhum dos três enfia pré-requisito na lista de rótulos de frequência.** *Então "quinto rótulo"
> é a resposta errada — não porque não caiba, mas porque mistura dois eixos que o campo inteiro
> mantém separados.*

---

# ⚠ E a gente JÁ TEM a forma pronta, e já usa ela

**O `RASCUNHO-5` escreve, logo abaixo dos quatro rótulos:**

> *"**E um rótulo de CUSTO, que é outro eixo:** `‹ nome ›` **(Ação Bônus).**"*

**O `(Ação Bônus)` é um parêntese que divide o slot visual com os quatro rótulos e NÃO é
frequência.** *É exatamente o desenho do `limited_to_form` do D&D 2024.*

> ### O bloco já tem um eixo não-frequência morando no parêntese. Este é o segundo.

---

# As saídas, com o trade-off

| # | a saída | o que ela custa |
|---|---|---|
| **`A`** | **parêntese de pré-requisito** — `Chama Divina (depois de Desmembrar e Clivar)` | **é o molde do D&D 2024, e a forma que o bloco já usa** no `(Ação Bônus)`. *Custa: parêntese longo fica feio, e o nosso já é `33` caracteres — o topo da faixa deles* |
| **`B`** | **linha nomeada dentro da ação** — `**Exige:** Desmembrar e Clivar já usados` | **é o molde do PF2e e do Draw Steel**, e cabe texto longo. *Custa: o mestre lê a ação inteira antes de descobrir que não pode usar* |
| **`C`** | **texto solto na prosa da ação** | zero regra nova. *Custa: é o que o Draw Steel faz em `6%` dos casos e o campo nomeado em `28%` — **o campo escolheu o contrário*** |
| **`D`** | **quinto rótulo de frequência** | ❌ *mistura dois eixos que os três sistemas mantêm separados* |

> ## Recomendação: `A`.
> **Ela é a única que não inventa forma nova** — o bloco já tem parêntese de eixo-não-frequência
> funcionando, e o D&D 2024 usa exatamente ele pra exatamente isto.
>
> **E ela resolve o problema de ordem que a `B` tem:** *o mestre vê o pré-requisito no nome da ação,
> antes de ler o que ela faz.*

# DECIDIDO — item `22` (o arredondamento) e item `15` (o tamanho da área, lado do inimigo)

*10/09/2026. **Scripts: `medir-o-encontro-misturado.py` e `medir-o-tamanho-da-area.py`.***

---

# § 1 · ITEM `22` — ⚠ não era folga de desenho. Era ARREDONDAMENTO.

**Eu tinha reportado `6,1%` de folga no esquadrão cheio e proposto cortar `6%` da vida do capanga.**
*Errado. A folga inteira mora em `10` níveis, e ela é de um quarto de ponto de vida.*

| nv | a fórmula pede | a `TABELA` publicava | o esquadrão cobrava |
|---|---|---|---|
| `2` a `20` | *(inteiro)* | igual | `63,5%` a `69,2%` — em torno do alvo `67,5%` |
| **`21` a `25`** | `68,75` | **`69`** ⚠ | ### **`79,2%`** |
| **`26` a `30`** | `78,75` | **`79`** ⚠ | ### **`79,1%`** |

> ### Um quarto de ponto de vida põe o esquadrão vivo numa rodada a mais, e a rodada a mais custa `11` pontos percentuais de encontro.

| | média em `29` níveis |
|---|---|
| com a `TABELA` como estava | `71,6%` — **`+6,1%`** |
| **com o piso** | **`67,7%`** — `+0,3%` |

> ## ⟹ A REGRA: **a vida do `Capanga` arredonda PRA BAIXO.** Nunca pro mais perto.
> **✅ Já aplicado na `TABELA.md`** — `10` linhas mudaram: nv`21`–`25` de `69` pra `68` *(pool `552` →
> `544`)* e nv`26`–`30` de `79` pra `78` *(pool `632` → `624`)*. **E a nota do porquê ficou junto.**

> ### ⚠ E é a TERCEIRA vez que este defeito aparece no projeto
> **peça 26 §8:** *"a linha do nível `2` publicava `115` de vida onde a regra pede `114`, e **um ponto
> de vida punha o chefe vivo numa quarta rodada**."*
> **`medir-o-capanga.py`, num comentário:** *"a `TABELA.md` IMPRIME ela arredondada; o sim usa a
> fórmula, senão um resto de `2` pontos inventa uma rodada."*
>
> ***O script já sabia. A tabela é que não tinha sido corrigida.***

---

# § 2 · ITEM `15`, LADO DO INIMIGO — e a medição INVERTE a intuição

***Palavras dele, 10/09:*** *"`3m` é nada KKK"* · *"tem ataques que são NATURAIS do inimigo e são em
área, eu queria olhar de ter métrica pra áreas maiores, talvez baseado no nv."*

## ⚠ PRIMEIRO, a conferência que ele pediu: é RAIO ou DIÂMETRO?

***Pergunta dele:*** *"pera aí que temos uma questão, `3 m` de RAIO não é. No sistema tá escrito
diâmetro, né?"*

> ### É RAIO. Conferido no repositório inteiro: `10` menções dizem `raio`, e **"diâmetro" aparece ZERO vezes** em todo `.md`, `.js` e `.py`.

| onde | o que está escrito |
|---|---|
| `partC.js:52` | *"Explosão · **Esfera de raio `3 m`**, num ponto a até `18 m`"* |
| `partC.js:53` | *"Aura · **Esfera de raio `3 m`** centrada em você"* |
| `partC.js:58` | *"Onda · **Esfera de raio `3 m`** centrada em você"* |
| `partC.js:72` | a escada: *"**Esfera (raio)** · `3 m → 4,5 m → 6 m → 9 m → 15 m`"* |
| `partC.js:85` | *"Explosão · **raio `3 m`**, a `9 m`"* |
| `partF.js` × `5` | os feitiços prontos: *"num **raio** de `4,5 m`"*, *"num **raio** de `3 m`"* … |

**Nenhuma contradição entre documentos. A medição abaixo fica de pé.**

## 🆕 MAS A INTUIÇÃO DELE TEM UMA RAZÃO, e ela tem nome

**O `3 m` de raio é UM QUARTO de uma Bola de Fogo.**

| | raio em quadrados | cobre |
|---|---|---|
| **Bola de Fogo do D&D** *(raio `20 ft`)* | `4` | **`50` quadrados** |
| **a nossa `Explosão` base** *(raio `3 m`)* | `2` | **`13` quadrados** |

> ### É daí que vem o "3m é nada": a régua que a mesa tem na cabeça é a Bola de Fogo, e a nossa base é um quarto dela.
> **As duas coisas são verdade ao mesmo tempo:** *ela é pequena **contra uma Bola de Fogo**, e é grande
> **contra o bicho de nível baixo do campo** (mediana `CR 0–1` = `4,5` quadrados).* **A Bola de Fogo é
> feitiço de JOGADOR de terceiro círculo; não é o sopro de um bicho de `CR 1`.**

### ⟹ E isso dá a âncora que faltava pro teto da escada do inimigo

**O degrau de `6 m` de raio cobre `50` quadrados — que é EXATAMENTE uma Bola de Fogo.**
*É a régua que todo mundo na mesa já conhece, e ela cai no mesmo lugar em que a conta do grupo
espalhado cai.* **Duas derivações independentes, o mesmo teto.**

### O desenho na grade, pra decidir olhando

| raio | quadrados de raio | **largura de ponta a ponta** | cobre |
|---|---|---|---|
| `3 m` | `2` | **`4` quadrados** | `13` |
| `4,5 m` | `3` | **`6` quadrados** | `28` |
| **`6 m`** | `4` | **`8` quadrados** | **`50`** — *uma Bola de Fogo* |
| `9 m` | `6` | `12` quadrados | `113` |
| `15 m` | `10` | `20` quadrados | `314` |

---

## A métrica: ÁREA COBERTA em quadrados, que é a única coisa comparável entre cone, linha e esfera

*`1` quadrado `= 1,5 m = 5 ft`. Cone de `L`: `L² ÷ 2`. Esfera de raio `R`: `π R²`. Linha: `L × W`.*

| corpo | amostra | mediana de área coberta |
|---|---|---|
| **D&D 2024** `CR 0–1` | `14` | `4,5` quadrados |
| D&D 2024 `CR 2–4` | `18` | `4,5` |
| D&D 2024 `CR 5–10` | `23` | `18,0` |
| D&D 2024 `CR 11–16` | `23` | `50,3` |
| D&D 2024 `CR 17+` | `28` | `72,0` |
| **Draw Steel** nv`1–3` · `4–6` · `7+` | `130` | **`9,0` · `10,0` · `15,0`** |

⚠ *`5` ações do D&D ficaram fora por passarem de `500` quadrados — são presença, covil e aura de milha.*

## E a nossa base NÃO é pequena. Ela já está acima do campo de nível baixo.

| | cobre |
|---|---|
| **nossa `Explosão`, raio `3 m`** | ### **`13` quadrados** |
| nosso `Cone`, `4,5 m` | `4,5` quadrados |
| D&D `CR 0–1`, mediana | `4,5` |
| Draw Steel nv`1–3`, mediana | `9,0` |

> ### O `3 m` parece pequeno porque é um RAIO escrito em metro. Em cobertura ele é `13` quadrados — quase o dobro da mediana de nível baixo do D&D, e acima da do Draw Steel.
> **O nosso `Cone` de `4,5 m` bate EXATO na mediana `CR 0–1` do D&D.**

## ⚠⚠ E o que está fora de escala é o TOPO da escada, não a base

| a escada da `Esfera` | `3 m` | `4,5 m` | `6 m` | `9 m` | `15 m` |
|---|---|---|---|---|---|
| **cobre** | `13` | `28` | `50` | ### `113` | ### **`314`** |

| a escada do `Cone` | `4,5 m` | `9 m` | `18 m` | `30 m` | `60 m` |
|---|---|---|---|---|---|
| **cobre** | `4` | `18` | `72` | ### `200` | ### **`800`** |

**A mediana `CR 17+` do D&D 2024 é `72`. O máximo do Draw Steel é `100`.**
*O nosso quarto degrau já passa dos dois, e o quinto passa por `3×` a `8×`.*

---

# ⟹ § 3 · A RÉGUA PRO INIMIGO, e ela sai da nossa própria trava

**O item `11` fechou com `1` ação em área à vontade, e a conta dele foi feita supondo que a área pega
a MESA INTEIRA.** *Então, do ponto de vista do preço, **área maior que "pega o grupo" não faz nada** —
o pior caso já está preçado.*

### ⟹ O teto útil é "pega um grupo espalhado", e ele tem número

*Quatro pessoas num quadrado `2×2`, com espaçamento variável:*

| como o grupo está | vão | raio que pega | cobre |
|---|---|---|---|
| colado | `2` quadrados | `1,5 q` = `2,25 m` | `7` |
| **espaçado normal** *(`2` quadrados entre eles)* | `3 q` | `2,2 q` = **`3,3 m`** | `15` |
| **espalhado** *(`3` quadrados)* | `4 q` | `2,9 q` = **`4,4 m`** | `26` |
| muito espalhado *(`4` quadrados)* | `5 q` | `3,6 q` = **`5,4 m`** | `41` |

> ### O `6 m` de raio cobre `50` quadrados e pega um grupo MUITO espalhado com folga.
> **Acima disso, mais área não pega mais ninguém — ela só pega mais cenário.**

## ⚠⚠ E A PRIMEIRA PROPOSTA ESTAVA ERRADA — ele achou, e o campo deu razão a ele

***Pergunta dele:*** *"mas não fica estranho? Inimigo nv`1` ter a mesma área que nv`30`?"*

**Eu tinha proposto três degraus por CATEGORIA, com o argumento "o grupo não fica maior com o nível".**
*O argumento é verdadeiro e a conclusão não segue — porque o campo cresce a área do mesmo jeito.*

### O teste limpo: os dragões. A MESMA criatura em três idades.

| cor | Jovem | Adulto | Ancião | cresce |
|---|---|---|---|---|
| `Red` · `Gold` · `Green` · `White` · `Silver` | cone `30 ft` = `18 q` | cone `60 ft` = `72 q` | cone `90 ft` = **`162 q`** | **`9,00×`** |
| `Black` | linha `30×5` = `6 q` | `60×5` = `12 q` | `90×10` = `36 q` | `6,00×` |
| `Blue` | `60×5` = `12 q` | `90×5` = `18 q` | `120×10` = `48 q` | `4,00×` |

> ### Mediana de `10` cores: **`9,00×`** do Jovem ao Ancião — e o CR só cresce `3,7×` no mesmo intervalo.
> **O campo escala a área MAIS do que escala o nível.** *E a forma é limpa: o comprimento do cone sobe
> linear (`30 → 60 → 90 ft`) e a cobertura sobe ao quadrado (`18 → 72 → 162`).*

### ⟹ E aqui o crescimento é DE GRAÇA, e isso tem precedente publicado

**O item `11` preçou a área supondo que ela pega a MESA INTEIRA.** *O pior caso já está pago.*
**Então área maior não custa nada — ela só muda a facilidade de acertar todo mundo.**

> **É exatamente a mesma coisa que o item `16` decidiu do `tamanho`:** *"o `tamanho` NÃO COBRA NADA"*,
> porque o ganho dele também já estava dentro do preço. **Dois eixos, o mesmo motivo.**

---

# ⟹ § 3b · A ESCADA POR NÍVEL — e ela usa só degraus JÁ PUBLICADOS

| nível | raio | cobre | contra a mediana do campo |
|---|---|---|---|
| **`2`–`8`** | **`3 m`** | `13` quadrados | `CR 2–8`: `4,5` a `18` ✅ |
| **`9`–`16`** | **`4,5 m`** | `28` quadrados | `CR 9–16`: `18` a `50` ✅ |
| **`17`–`24`** | **`6 m`** | `50` quadrados | `CR 11–16` mediana: **`50,3`** ✅ *exato* |
| **`25`–`30`** | **`9 m`** | `113` quadrados | entre `CR 17+` (`72`) e o Ancião (`162`) ✅ |

> ## E o crescimento total da escada é `9,00×`. O dos dragões do SRD é `9,00×`.
> **Distância: `0,0%`.** *E nenhum número novo entrou — os quatro degraus já estão publicados no
> `partC.js`.*

**E o `15 m` (`314` quadrados) sai da escada do inimigo.** *Ele passa do Ancião por `1,9×`, e continua
existindo pro jogador.*

---

# ⚠⚠ § 3c · E MEDINDO ISSO APARECEU UM BURACO SÉRIO — a trava de área é POR CRIATURA

**O esquadrão do `Capanga` tem OITO criaturas. Oito ações em área por rodada.**

| nv | `8` capangas em área, por alvo por rodada | da vida do PJ |
|---|---|---|
| `7` | `48,0` | **`111%`** |
| `20` | `177,6` | **`109%`** |
| `30` | `264,0` | **`108%`** |

> ### O esquadrão em área derruba OS QUATRO em `0,9` rodada. É `6,0×` o que a trava permite pro chefe.
> *O chefe com `1` ação em área entrega `18%` da vida por alvo por rodada. O esquadrão entrega `109%`.*
> **Na luta inteira: `325%` da vida de CADA personagem.**

## O conserto, e ele já é a leitura publicada do `Capanga`

> ### **A trava de área conta por ESQUADRÃO, não por corpo.**
> *`1` ação em área por rodada no esquadrão inteiro — os outros sete batem normal.*

**Não é regra nova: é a mesma leitura que o item `10` já fechou** — *"quem age é o ESQUADRÃO"*, e o
`Controlador` no esquadrão usa `ações = 8` por isso. **E é a mesma família do teto de empilhamento do
item `19`:** *o enxame entrega tudo, só não CONCENTRA.*

| | por alvo por rodada | na luta |
|---|---|---|
| `8` capangas, trava por corpo | `109%` da vida | ⚠⚠ `325%` |
| **`1` ação de área no esquadrão** | **`14%`** | **`42%`** — *abaixo dos `50%` do chefe* ✅ |

# § 4 · O QUE FALTA — e é uma linha no capítulo, não conta

> #### A área natural do inimigo
>
> **Um inimigo pode ter um ataque em área que não vem de técnica nenhuma** — o sopro, o rugido, o
> corpo que se abre. **O raio dele sai da categoria:** `3 m` no `Capanga` e na `Ameaça`, `4,5 m` no
> `Desastre`, `6 m` na `Catástrofe` e na `Calamidade`.
>
> **Não sobe além disso, e o motivo é que não adianta:** *um raio de `6 m` cobre `50` quadrados e pega
> quatro pessoas espalhadas a três quadrados uma da outra.* **Área maior pega cenário, não gente.**
>
> ⚠ **E ela obedece a trava do §6.5: no máximo `1` ação em área por rodada, e `Recarga` não conta.**

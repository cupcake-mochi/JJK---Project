# A `Recarga` — a `C3` resolvida

*10/09/2026. Conta em `dimensionar-a-recarga.py`, saída em `SAIDA-recarga.txt`.*

***Enquadramento do Mizuki:*** *"o recarga era pra ser **aquela ação pesada da rodada que muda o
combate no turno do inimigo**, normalmente pro lado do dano, igual DnD... **o `5-6` n é regra, era
exemplo**, mas serve bem, seria aí onde entrariam **técnicas máximas, liberações máximas** e afins (o
nome é flavor, n precisa de cálculo à parte)."*

---

## ⚠ E isso DISSOLVE a objeção do §6.5

**O §6.5 dizia:** *"a recarga `5-6` dispara `1,67` vezes numa luta de três rodadas, e **a cota não
paga a fração que sobra**."*

> ### Isso só é problema se a `Recarga` vier POR CIMA das ações dele.
> **No enquadramento do Mizuki ela OCUPA uma ação.** *Então não há fração a **pagar** — há uma fração
> a **DIMENSIONAR**.*

**E a `1× por luta` do §6.5 não morre: ela é o mesmo desenho com `usos = 1`.**

---

## A conta

> **total da luta** = `usos × (k × golpe novo)` + `(slots − usos) × golpe novo`
> **e ele tem de continuar igual a** `slots × golpe de hoje`

*`Desastre` nv30: `3` ações × `3` rodadas = `9` slots, golpe `67,4`, a `Recarga (5-6)` dispara `1,67`.*

| a `Recarga` é | golpe normal | **a `Recarga`** | ela é | e o golpe normal fica |
|---|---|---|---|---|
| `1,5×` uma ação | `61,7` | **`92,5`** | `1,37×` o golpe de hoje | `0,92×` |
| **`2,0×`** | `56,8` | **`113,7`** | `1,69×` | `0,84×` |
| `2,5×` | `52,7` | **`131,8`** | `1,96×` | `0,78×` |
| `3,0×` | `49,1` | **`147,4`** | `2,19×` | `0,73×` |
| `4,0×` | `43,3` | **`173,1`** | `2,57×` | `0,64×` |

> **Quanto maior a `Recarga`, menores os golpes normais. O total não muda.**
> *E `o golpe` que a ficha imprime passa a ser o **normal** — a segunda coluna.*

---

## ✅ O contra-teste: a intuição do Mizuki já era `2,7×`, e ele escreveu isso sem conta nenhuma

**O `RASCUNHO-1` — o Sukuna, escrito em 08/09 antes de qualquer uma destas contas:**

| | |
|---|---|
| `Corte` — a ação normal | **`34`** |
| `Fuga (recarrega no 5–6)` | **`92`** |
| **a razão** | **`2,71×`** |

> **Ele já tinha posto a Recarga em `2,7×` a ação normal, de intuição.**
> *Nessa razão, o golpe normal cai pra `51,2` (`0,76×` o de hoje) e a `Recarga` bate `138,5`.*
> **A conta não corrige a intuição dele — ela só diz o preço: os golpes normais ficam `24%` menores.**

---

## O que fica

| | |
|---|---|
| **a `Recarga` é a ação pesada da rodada** | é onde moram `Técnica Máxima`, `Liberação Máxima` e afins |
| **ela OCUPA uma ação**, não vem por cima | e por isso não estoura a cota |
| **o `5-6` é exemplo, não regra** | *`67` de `83` rótulos do SRD 5.2.1 são `5-6`, então ele serve bem como padrão* |
| **o nome é sabor** | e não pede cálculo à parte — o dimensionamento é o mesmo qualquer que seja o nome |
| **o §6.5 perde a frase** *"e uma não cabe"* | ela media a Recarga como se fosse extra. **Vai junto com o item `6` da fila** |

### ⚠ O que sobra decidir, e é sabor

**Qual `k`?** *A intuição do Sukuna diz `2,7×`. A conta aceita de `1,5×` a `4,0×` — o que muda é
quanto o golpe normal encolhe (`8%` a `36%`).*

> **Quanto maior o `k`, mais a luta vira "espera o golpão".** *Quanto menor, mais ela vira `3` golpes
> iguais — que é o "inimigo de um botão só" que o campo reclama.*

---

# ⚠⚠ O CAMPO CORRIGE O `k` — e a hipótese do Mizuki estava certa

***Ele, 10/09/2026:*** *"salvo engano **recarga come mais de uma ação na rodada do inimigo pra n ser
TPK**, mas posso estar errado."*

**Não estava errado. Fui medir no D&D — `Adult Red Dragon`, fonte `api.open5e.com`:**

| | o texto literal | dano |
|---|---|---|
| **`Multiattack`** | *"The dragon can use its Frightful Presence. It then makes **three attacks**: one with its bite and two with its claws."* | `26,5 + 15,5 + 15,5` = **`57,5`** |
| **`Fire Breath (Recharge 5-6)`** | *"The dragon exhales fire in a 60-foot cone… **63 (18d6)** fire damage"* | **`63`** |

> ### O sopro é uma AÇÃO SEPARADA. Usar ele significa NÃO usar o `Multiattack`.
> **Ele come o turno inteiro — as três ações.**

## E o número desmonta o `2,7×`

**Contra UM alvo, o sopro entrega `63` contra os `57,5` do turno cheio — `1,10×`.**

> **Praticamente o mesmo.** *A `Recarga` do D&D **não é um golpe maior**. Ela é o mesmo turno,
> entregue de outro jeito.*
>
> ### O ganho dela não é tamanho. É ÁREA.

## E o Sukuna do `RASCUNHO-1` já fazia igual — a intuição acertou duas vezes

| | |
|---|---|
| `Ataque Múltiplo` = `3` × `Corte` | `3 × 34` = **`102`** |
| `Fuga (recarrega no 5–6)` | **`92`** |
| **a razão** | **`0,90×`** o turno cheio |

**O Sukuna dá `0,90×` e o dragão dá `1,10×`. A mesma coisa.**

*O `2,71×` que eu calculei antes comparava a `Recarga` com **UMA ação**. O campo compara com o
**TURNO INTEIRO** — e é essa a comparação certa, porque a Recarga come o turno.*

---

# ✅ A `Recarga`, FECHADA

| | |
|---|---|
| **ela come o TURNO INTEIRO** | não uma ação. `Multiattack` e `Recarga` são exclusivos |
| **`k ≈ 1,0×` a `1,1×` do turno cheio** | e não `2,7×` de uma ação. *D&D `1,10` · Sukuna `0,90`* |
| **o ganho é ÁREA**, não tamanho | e o §6.5 já diz o que fazer com isso: *"área reparte a cota, e não multiplica ela"* |
| **e por isso ela não estoura nada** | ela entrega o mesmo turno. **A objeção do §6.5 morre de vez** — não há fração a pagar nem a dimensionar |
| **é onde moram** | `Técnica Máxima`, `Liberação Máxima` e afins. *O nome é sabor* |

> ### ⟹ Num `Desastre` nv30: `o golpe` continua `67,4`, o turno cheio é `202`, e a `Recarga` entrega `~202` — **numa área**.
> **Zero recalibração. O golpe normal NÃO encolhe.** *A tabela de `k` do §1 deste arquivo fica como
> registro do caminho, mas o campo respondeu outra coisa: `k` não se escolhe, ele **é** o turno.*

---

# ⚠ CORREÇÃO — a `Recarga` NÃO come tudo. Come grande parte.

***Ele, 10/09/2026:*** *"essas ações de recarga comem a rodada toda? tenho quase certeza que ele ainda
tem tipo, um ataque em seguida ou algo semelhante, tipo… **ele n come TUDO TUDO, come grande parte**."*

**Certo de novo. Fui conferir o mesmo dragão, e o que eu escrevi acima estava simplificado demais.**

**O `Adult Red Dragon` tem, além das Ações:**

> *"The dragon can take **3 legendary actions**, choosing from the options below."*
> `Detect` · `Tail Attack` · `Wing Attack (Costs 2 Actions)`

**E elas acontecem *"at the end of another creature's turn"* — fora do turno dele.**

> ### ⟹ O `Fire Breath` come a AÇÃO do turno (o `Multiattack`). Ele NÃO come as ações lendárias.
> **Numa rodada de sopro o dragão ainda dá `3` ações lendárias.**

## A tradução exata pro Projeto-M

| a `Recarga` COME | a `Recarga` NÃO come |
|---|---|
| as **`Ações Múltiplas`** daquela rodada | a **`Intervenção`** — *é a ação lendária, e ela é fora do turno* |
| | a **`Ação Bônus`** |
| | a **`Reação`** |

**Então numa rodada de `Recarga`, um `Desastre` entrega:**

> a **`Recarga`** (`~202`, em área) **+** a `Intervenção`, se ele tiver uma disponível **+** a `Ação Bônus` **+** a `Reação`.

*É a rodada mais pesada da luta — e é isso que ela deveria ser. **Mas o corpo dela é o turno, não a
rodada inteira.***

> **A frase certa é a dele: ela não come TUDO. Come a parte grande.**

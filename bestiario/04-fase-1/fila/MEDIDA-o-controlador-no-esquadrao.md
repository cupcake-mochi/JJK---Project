# O `Controlador` no esquadrão — validado contra o Draw Steel

*10/09/2026. Conta em `medir-o-controlador-no-draw-steel.py`, saída em
`SAIDA-controlador-draw-steel.txt`. **`415` statblocks lidos**, do dump em
`dados-recarga-area/data-md-main/`.*

> ***Pedido do Mizuki:*** *"Valide em comparação ao Draw Steel, foi de lá q pegamos a ideia, ent deve
> ter uma métrica q podemos roubar e adaptar provavelmente."*
>
> **Ele estava certo em três frentes. E a métrica que dá pra roubar não é a que eu esperava.**

---

# A PERGUNTA

**A forma `B` do `Controlador` preça assim:** *negar `1` ação do grupo vale `1` ação dele, então ele
ganha `(1 + 1/ações)` e paga `vida × 1/(1 + 1/ações)`.*

**No `Capanga`, `ações` é `1` (por corpo) ou `8` (por esquadrão)?**

| a leitura | ganha | paga vida | razão vs chefe |
|---|---|---|---|
| por CORPO | `2,000×` | `× 0,500` | `0,67` |
| por ESQUADRÃO | `1,125×` | `× 0,889` | `1,01` |

---

# ⟹ A RESPOSTA: **POR ESQUADRÃO**. E as três confirmações são independentes.

## `1` · A regra literal do Draw Steel

> *"When minions act, **each minion in the squad uses their main action** in concert."*
> *"Minion turns are meant to be short. On their shared turn, **each minion** can take only a move
> action and a main action, a move action and a maneuver, or two move actions."*

> ### Cada corpo tem a ação DELE. O esquadrão age junto — mas as ações são `8`, e não `1`.
> *O "age junto" é sobre **iniciativa e rolagem**, não sobre economia de ação.*

## `2` · O preço em Stamina, medido em `415` statblocks

**Cada criatura virou uma razão contra a mediana da coorte dela — mesma organização, mesmo nível.**
*Assim nível e organização saem da conta e sobra o papel.*

| papel do Draw Steel | `n` | Stamina relativa à coorte |
|---|---|---|
| `Artillery` | `50` | `0,833` |
| `Hexer` | `47` | `0,875` |
| **`Controller`** | **`41`** | **`0,917`** |
| `Ambusher` · `Harrier` · `Support` · `Mount` · `Leader` · `Solo` | — | `1,000` |
| `Brute` · `Defender` | `61` · `23` | `1,250` |

### E a nossa forma `B` contra esse número

| a leitura | paga vida | o Draw Steel | **distância** |
|---|---|---|---|
| **por ESQUADRÃO** | `0,889×` | `0,917×` | **`3,1%`** |
| por CORPO | `0,500×` | `0,917×` | **`45,5%`** |

> ### O mais mole dos onze papéis do Draw Steel é o `Artillery`, a `0,833`.
> **Nenhum chega perto de metade.** *O `0,500` não tem apoio nenhum no campo.*

## `3` · E só entre os minions, que é o caso exato do `Capanga`

**Os `6` `Minion Controller`, um a um, contra a mediana de Stamina do nível deles:**

| nome | nv | Stamina | mediana do nv | razão |
|---|---|---|---|---|
| `High Elf Dawn Mage` | `1` | `3` | `4,0` | `0,750` |
| `Orc Glorifier` | `1` | `3` | `4,0` | `0,750` |
| `Human Apprentice Mage` | `2` | `4` | `4,0` | `1,000` |
| `Voiceless Talker Graywarper` | `6` | `9` | `9,0` | `1,000` |
| `Sand Stone Giant` | `8` | `14` | `13,0` | `1,077` |
| `Cyclops` | `10` | `14` | `15,0` | `0,933` |
| | | | **mediana** | **`0,967`** |
| | | | *média* | *`0,918`* |

**Longe do `0,500`. Perto do `0,889`.**

---

# ⚠ E A MÉTRICA QUE DÁ PRA ROUBAR É OUTRA — e ela mexe no desenho, não neste martelo

## O EV do Draw Steel NÃO vê o papel

**Medido: `37` de `39` coortes (organização + nível) com `3` ou mais criaturas têm EV IDÊNTICO.**

*As duas exceções são casos isolados — um `Elite Controller` nv3 com `28` onde o resto tem `20`, e um
`Platoon Hexer` nv1 com `8` onde o resto tem `6`.*

> ### O preço do Draw Steel sai de ORGANIZAÇÃO + NÍVEL. O papel não custa um ponto de EV.
> *E o livro escreve isso: "Roles are **descriptive**, and most don't follow special rules."*

## Mas a Stamina MUDA com o papel — de `0,833` a `1,250`

> ### Então lá o papel remodela o bloco SEM invariante formal.
> **Eles não têm o nosso `produto 1,000`. Eles calibraram no olho, e publicaram.**

**Um `Minion Brute` a `1,125×` de Stamina custa o mesmo EV que um `Minion Artillery` a `0,750×`.**
*Um swing de `50%` que o orçamento deles não cobra.*

## E é por isso que a comparação vale: são duas derivações independentes chegando no mesmo lugar

| papel | **Draw Steel** *(Stamina rel.)* | **o nosso** *(`vida ×`)* | distância |
|---|---|---|---|
| `Controller` → `Controlador` | `0,917` | **`0,889`** | **`3,1%`** ✅ |
| `Artillery` → `Artilheiro` | `0,833` | `0,857` | **`2,9%`** ✅ |
| `Brute` → `Brutamontes` | `1,250` | `1,200` | **`4,0%`** ✅ |
| `Support` → `Apoio` | `1,000` | *paga dano* | — |
| `Ambusher` → `Emboscador` | `1,000` | `0,863` | ⚠ `13,7%` |
| `Defender` → `Guardião` | `1,250` | `0,800` | ⚠ **oposto** |

**Três batem em menos de `4%`.** *E a nossa tabela saiu de uma derivação fechada (`produto 1,000`), a
deles saiu de playtest. **Duas estradas diferentes, mesmo destino.***

### As duas que não batem, e por quê

**O `Guardião` bate no SENTIDO e não no número.** *O `Defender` deles fica duro comprando Stamina; o
nosso fica duro comprando **Defesa `+2`** e pagando `vida × 0,80`.* **Mesma intenção, moeda diferente
— e a nossa tem invariante e a deles não.** *Não é contradição.*

**O `Emboscador` é o único desalinhado de verdade** — o `Ambusher` deles não paga nada, o nosso paga
`0,863`. *E o nosso ganha "vantagem em `1` ataque por rodada, toda rodada", que é mais do que "ataca
primeiro".* **Fica registrado, não vira item: a diferença tem causa escrita.**

---

# ⚠ E APARECEU UMA COISA QUE VIRA ITEM DE FILA

**O Draw Steel põe um TETO em empilhar minion no mesmo alvo, e a gente não tem:**

> *"Each target of a minion's signature ability is affected by only **one instance** of the ability.
> But when **two or three (at maximum)** of a squad's minions attack the same creature simultaneously,
> each additional minion causes the ability to deal extra damage equal to the minion's **free strike
> value**."*
>
> *"Because a minion's free strike value is typically lower than the average damage of their signature
> ability, it's usually **more effective to have each minion target a different hero**."*

**O nosso `Capanga` não tem teto nenhum:** *`8` corpos batem `8` golpes cheios em quem o mestre quiser,
inclusive todos na mesma pessoa.* **No nv20 isso é `8 × 37` = `296` numa cabeça só, contra `163` de
vida.**

> ### Uma pessoa morre duas vezes na primeira rodada, e nada na regra impede.
> **E o Draw Steel resolve isso com a mesma família de argumento que a gente já mediu na área** —
> *"Spread the Damage Around"*, `fila/A-DECISAO-da-area-e-da-recarga.md`.

**⟹ Item novo pra fila: o teto de empilhamento do `Capanga`.**

---

# ⟹ O QUE FECHA

| | |
|---|---|
| **o martelo `C`** | ✅ **por ESQUADRÃO** — `ações = 8`, ganha `1,125×`, paga `vida × 0,889`, razão `1,01` |
| **a confiança** | **três confirmações independentes:** a regra literal, `41` criaturas normalizadas, e os `6` minions um a um |
| **o que não muda** | o EV deles não vê papel. *A gente cobra dentro do bloco e eles não cobram — **e mesmo assim os números bateram.*** |
| **o que sobra** | ⚠ **o teto de empilhamento**, item novo |

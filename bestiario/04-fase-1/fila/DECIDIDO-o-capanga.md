# O `Capanga` — o que o Mizuki bateu

*10/09/2026. Item `17` da fila. A medição está em `MEDIDA-o-capanga.md`, a conta em
`medir-o-capanga.py`.*

> **Dois dos três martelos fecharam. O terceiro ele mandou MEDIR** — *"valide em comparação ao
> Draw Steel, foi de lá q pegamos a ideia, ent deve ter uma métrica q podemos roubar e adaptar"*.
> **Está em `MEDIDA-o-controlador-no-esquadrao.md`.**

---

## 1 · A banda vira **`21%` – `28%`** — FECHADO

***Decisão do Mizuki, 10/09/2026:*** *a saída `1` — o medido, arredondado.*

> ### A banda do `o golpe` vira **`21%`–`28%`**.
> ⚠ *Esta linha é a ÂNCORA. Os scripts leem a banda daqui — não da `DECIDIDO-a-fila-barata`, que
> ficou como registro.*

**O medido, varrido em `29` níveis × `5` categorias:** `21,8%` (`Ameaça` nv2) a `27,7%`
(`Desastre`, todo nível).

| | de | para |
|---|---|---|
| a banda | `20%` – `32%` | **`21%` – `28%`** |

**Por que o `20%` caiu:** *ele existia porque o `Controlador` cortava `1/3` do dano. A forma `B`
tirou o corte do dano e pôs em vida — **`o golpe` não se move mais em papel nenhum**, e o piso ficou
órfão.*

**Por que o `32%` caiu:** *ele **era** o `Capanga` no nv2, calculado com o fator de dano `0,33` da
tabela MORTA da escada. Com o `0,25` que a `TABELA.md` implementa, ele dá `21,8%`.* **Ninguém encosta
em `32%`: sobravam `4,3` pontos de teto que não vigiavam nada.**

> ⚠ **Isso mexe em número publicado, e é a segunda vez em um dia.** *Mas a decisão de `20%`–`32%`
> fechou com a justificativa "o piso passa a ser o `Controlador`" — e a forma `B` matou essa premissa
> dezenove minutos de trabalho depois.* **Não é reabrir decisão viva: é terminar uma cuja premissa
> morreu.**

### ⚠ E a banda nova MATOU a forma `A` do `Controlador` — de graça

*Achado rodando o `dimensionar-o-controlador.py` com a âncora nova.*

**A forma `A` procura, por categoria, a maior fração `1/N` cujo corte ainda cabe na banda.** *Com o
piso em `21%`, o teto de corte da `Ameaça` cai pra `7,1%` — e não existe `1/N` tão pequeno que ainda
seja uma fração útil.*

> **Isso não reabre nada:** *a forma `B` já tinha sido escolhida em 10/09, e ela não corta dano nenhum.*
> ### O que mudou é que agora a `A` é IMPOSSÍVEL, e não só pior.

### Onde isso mexe

| arquivo | o quê |
|---|---|
| `a-escada-com-numero.md` | a linha *"A banda inteira é de `21%` a `32%`"* → **`21%` a `28%`** |
| `fila/DECIDIDO-a-fila-barata.md` §1 | a decisão de `20%`–`32%` fica como registro, **substituída** |
| `medir-o-capanga.py` · `dimensionar-o-controlador.py` | leem a banda por âncora — **não quebram**, mas passam a ler o número novo |

---

## 2 · O `Capanga` toma **só os quatro papéis neutros** — FECHADO

***Decisão do Mizuki:*** *a saída `1`.*

| papel | entra? | por quê |
|---|---|---|
| `Artilheiro` | **sim** | medido `0,0%` de desvio no encontro |
| `Emboscador` | **sim** | medido `0,0%` |
| `Apoio` | **sim** | medido `0,0%` |
| `Controlador` | **sim** | ⚠ *depende do martelo `3` — ver o arquivo do esquadrão* |
| **`Brutamontes`** | **NÃO** | `+25,0%` de encontro — **e ele quebra a trava:** `vida × 1,20` faz o capanga parar de cair num golpe |
| **`Guardião`** | **NÃO** | `−8,3%` de encontro. *O `0,800` cruza a linha de rodada; o `0,857` do `Artilheiro` não* |

### E o motivo do `Brutamontes` não é o número

> ### Um `Capanga` que não cai num golpe **é** uma `Ameaça`.
> *A escada já publica isso — a vida dele é `dano do grupo ÷ 4`, que é exatamente o que UM jogador
> entrega numa rodada.* **A exclusão cai de graça da definição que já está escrita.**

**Quer capanga durão? Sobe pra `Ameaça`.** *Ela custa mais no encontro, e é honesto que custe.*

### A razão de fundo, e ela vale pro projeto inteiro

**A moeda dos seis papéis é VIDA.** *Num corpo único ela é contínua: `20%` a mais de vida é `20%` a
mais de luta.*

> ### Num enxame a vida entra DUAS vezes — uma no corpo, e outra na DURAÇÃO.
> **E duração multiplica tudo o que o enxame entrega.** *Por isso o invariante `produto 1,000` fecha
> no corpo único e não fecha no `Capanga`.*

**E não dá pra trocar a moeda por corpos:** *um corpo a mais é `+12,5%` de corpos e **`+25%` de
encontro**, e os papéis pedem ajustes de `13,7%` a `50%`.* **A moeda é grossa demais, e erra pro
mesmo lado.**

---

## 2b · O TETO DE EMPILHAMENTO — **teto `3`, extras a METADE** — FECHADO

***Decisão do Mizuki, 10/09/2026.*** *Medição em `MEDIDA-o-empilhamento.md`.*

> ### A regra, em uma linha
> **No máximo `3` capangas do mesmo esquadrão atacam o mesmo alvo por rodada, e do segundo em
> diante o golpe sai pela METADE.**

| | nv20 |
|---|---|
| sem trava — como estava | `8 × 37` = **`296`** = **`181%`** da vida de um personagem. *Ele morre* |
| **com a trava** | `37 + 18,5 + 18,5` = **`74`** = **`45%`**. *Ele sente e não cai* |

**Bastavam `4,4` corpos pra derrubar alguém, e nada impedia os `8`.**

### Por que METADE e não o `0,573` do campo

*Medi `115` minions do Draw Steel: o free strike deles é **`0,573`** do dano esperado da assinatura.*

| | |
|---|---|
| `1` | `0,50` está a `12,7%` do medido — **dentro do ruído** *(a razão observada vai de `0,49` a `1,08`)* |
| **`2`** | ### "metade" é a fração que o sistema JÁ publica |

**O `Estilhaço` (`Leve`) diz *"metade dos dados respinga em quem estiver do lado"*, e o `tamanho`
adotou *"o alvo + metade em `1`"* na mesma semana.** *Uma fração de respingo no bestiário inteiro, não
duas.*

### E por que teto `3` e não `2`

**O livro deles escreve *"two or three (at maximum)"* e não escolhe.** *O `3` deixa a jogada de
"cercar um" existir sem matar — `45%` da vida. O `2` fecha demais: `34%` não assusta ninguém.*

### ⚠ E a trava NÃO encolhe o enxame

**Com teto `3` e `4` personagens, os `8` corpos ainda entregam tudo — eles só não podem CONCENTRAR.**

> **A razão `1,01 ×` que a escada do `Capanga` publica não se move.** *A trava mexe só no caso
> degenerado.* **É por isso que ela é barata: ela não re-preça nada.**

### E ela conserta o pior caso do bestiário

**A saída `F` do item `16` deu ao `Grande` "metade em `1` vizinho", de graça.**

| | alvos | dano total | vs `1` PC |
|---|---|---|---|
| `8` capangas `Grande`, **sem trava** | `16` | **`444`** | **`272%`** |
| `8` capangas `Grande`, **com a trava** | `6` | `130` | `79%` |

---

## 3 · O `Controlador` no esquadrão usa **`ações = 8`** — FECHADO por medição

***Palavras dele:*** *"Valide em comparação ao Draw Steel, foi de lá q pegamos a ideia, ent deve ter
uma métrica q podemos roubar e adaptar provavelmente."* **Ele estava certo, e a medição fechou o
martelo sozinha** — `MEDIDA-o-controlador-no-esquadrao.md`.

| | |
|---|---|
| **`ações`** | **`8`** — por esquadrão, não por corpo |
| ganha | `1,125×` |
| **paga** | **`vida × 0,889`** |
| razão vs chefe | `1,01` — o enxame continua do tamanho que a escada vendeu |

### As três confirmações, e elas são independentes

**`1` — a regra literal.** *"When minions act, **each minion in the squad uses their main action** in
concert."* **O "age junto" é sobre iniciativa e rolagem, não sobre economia de ação.**

**`2` — o preço em Stamina, medido em `415` statblocks**, normalizado por nível e organização:

| | paga vida | o `Controller` do Draw Steel | distância |
|---|---|---|---|
| **por ESQUADRÃO** | `0,889×` | `0,917×` *(n=`41`)* | **`3,1%`** |
| por CORPO | `0,500×` | `0,917×` | `45,5%` |

*O papel mais mole dos onze deles é o `Artillery`, a `0,833`.* **Nenhum chega perto de metade.**

**`3` — e só entre os minions:** os `6` `Minion Controller` dão mediana **`0,967×`** (média `0,918×`).

### E de quebra, a tabela dos seis papéis ganhou uma validação externa

*Duas derivações independentes — a nossa fechada em `produto 1,000`, a deles saída de playtest:*

| papel | Draw Steel | o nosso | distância |
|---|---|---|---|
| `Controlador` | `0,917` | `0,889` | **`3,1%`** |
| `Artilheiro` | `0,833` | `0,857` | **`2,9%`** |
| `Brutamontes` | `1,250` | `1,200` | **`4,0%`** |
| `Emboscador` | `1,000` | `0,863` | ⚠ `13,7%` — *o nosso dá mais, e paga* |
| `Guardião` | `1,250` | `0,800` | ⚠ *oposto no número, igual no sentido — ele compra `Defesa`, não vida* |

> ⚠ **E o EV do Draw Steel NÃO vê papel** — `37` de `39` coortes têm EV idêntico. *Lá o papel remodela
> o bloco **sem invariante formal**.* **A gente cobra dentro do bloco e eles não cobram, e mesmo assim
> os números bateram em três de cinco por menos de `4%`.**

---

---

## E os consertos que não eram decisão — FEITOS

| # | o quê | onde |
|---|---|---|
| `1` | caixa de correção no topo da escada: a tabela de fator do topo está **morta** | `a-escada-com-numero.md` |
| `2` | a linha de fatia do `Capanga` (`32/30/30/30`) marcada como errada — o medido é `22/23/23/23` | idem |
| `3` | o item `17` da fila citava o fator morto e concluía o oposto do medido | `A-FILA.md` |
| `4` | ⚠ **nota de método:** em enxame o sim tem de ler a FÓRMULA (`dano do grupo ÷ 4`), nunca a vida IMPRESSA. *`79` em vez de `78,75` inventa uma rodada e erra `17%`* | `MEDIDA-o-capanga.md` |

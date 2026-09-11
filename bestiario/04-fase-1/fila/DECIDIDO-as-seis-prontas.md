# DECIDIDO — o item `30`: para onde vão as seis prontas

*10/09/2026 (noite). **Os dois martelos dele, batidos com a conta na mão.***
**Laudo: `MEDIDA-o-remapeamento-das-seis.md` · conta: `medir-a-dupla.py`** *(o 27º)*.

> ## As seis saem da escada morta. `4` por conferência, `2` por martelo.

---

# § 1 · O MAPA FECHADO — e ele é a ÂNCORA deste item

> ### ⚠ Esta tabela é a fonte. Quem executar no `Claude 2` lê daqui, e o `§10` do script confere.

| ficha | faixa | de | ⟹ **para** | corpos | como fechou |
|---|---|---|---|---|---|
| **`Betobeto`** | `2 a 4` | `Ronda` | **`Ameaça`** | `1` | ✅ conferência — `29`/`29` |
| **`Kamaitachi`** | `2 a 4` | `Dupla` | **`Ameaça`** | ### **`2`** | ⚡ **martelo dele** |
| **`Tsuchigumo`** | `2 a 4` | `Alcateia` | **`Desastre`** | `1` | ✅ conferência — `29`/`29` |
| **`Hitotsume`** | `5 a 8` | `Ronda` | **`Ameaça`** | `1` | ✅ conferência — `29`/`29` |
| **`Kitsune`** | ### **`9 a 12`** | `Dupla` | **`Ameaça`** | `1` | ⚡ **martelo dele — e a FAIXA mudou** |
| **`Oni`** | `5 a 8` | `Alcateia` | **`Desastre`** | `1` | ✅ conferência — `29`/`29` |

---

# § 2 · A `Kitsune` — saída `F`, e ela sobe de faixa em vez de mudar de bicho

***Decisão dele:*** *a `F`.*

**O problema medido:** *`0` de `6` saídas da escada viva deixam ela conjurar no nv`5`–`8` — **nem o
topo**.* *A ficha declara "uma técnica de `Classe 1` no orçamento de `4,2` pontos", e a linha dela é
"a única da faixa que conjura".*

| a `Ameaça`, por faixa | pontos por ação | conjura? |
|---|---|---|
| nv `5 a 8` *(onde ela estava)* | `2,2` | ❌ **seco** |
| ### nv `9 a 12` | ### **`4,2`** | ### ✅ **sim** |

> ### O número não foi ajustado pra bater: `4,2` é o que a `Ameaça` de `9 a 12` já vale, e `4,2` é o
> que a ficha já publica. **Distância `+0,5%`.**
> ⟹ *a característica dela — "no orçamento de `4,2` pontos da ação" — **não muda uma letra**.*

## Por que essa e não "vira bloco seco"

**O piso `seco` foi fechado no item `21` com a conta pronta** — *`25,2%` do D&D `CR 0–1` e `45,7%` dos
minions do Draw Steel têm uma entrada só.* **Ele é regra boa, e ela diz que nv`5` não conjura.**

*Brigar com o piso pra salvar uma ficha reabriria o que já foi medido.* **A `F` respeita o piso E salva
a ficha, e o preço dela é só de COBERTURA — que é escolha de escopo, não defeito de máquina.**

> ### ⚠ E o preço está declarado: as seis deixam de cobrir `nv 2 ao 6`.
> **Passam a cobrir `nv 2 ao 12`**, e o `dados.js` tem um comentário que deriva o número seis da faixa
> antiga. *Ele muda junto — está no `§4` abaixo.*

---

# § 3 · A `Kamaitachi` — duas `Ameaça`, e a ficção não muda uma palavra

***Decisão dele:*** *duas `Ameaça`.*

**A ficção dela JÁ É dois corpos:** *"Duas comadres-de-foice que trabalham juntas: uma derruba, a outra
corta."* **E a característica dela é** *"nenhuma — as duas atacam no mesmo turno, e isso já é a
categoria"*.

| | cobra da mesa padrão | vs a `Dupla` que ela era |
|---|---|---|
| a `Dupla` publicada | `22,5%` | — |
| **duas `Ameaça`** | `16,9%` | ### **`−25,0%`** |

> ### O `−25,0%` não é surpresa nem defeito: é o `0,75×` que o §4.3 já publica.
> ***"Eles morrem em fila e a saída deles despenca."*** *Dois corpos de `0,25` não valem um de `0,50`,
> pela mesma razão que quatro não valem um inteiro.* **É a mesma propriedade, medida no degrau de baixo.**

**E o golpe entra na banda:** *`22,6%`–`22,8%` contra a banda viva `21%`–`28%`.* **A `Dupla` entregava
`45%` num golpe só — `1,60×` o topo.**

## ⚠ O que isso pede do gerador, e é a única sutileza

**O `dados.js` tem UM campo `categoria` por ficha, e o `make.js` monta UM bloco.**

> ### A ficha da `Kamaitachi` é `Ameaça`, e o bloco impresso é UM. A dupla mora na FICÇÃO.
> *O mestre põe duas cópias na mesa.* **É o mesmo jeito que o campo escreve par e minion**, e não pede
> campo novo. ⚠ *Mas a linha dela precisa dizer isso, senão o mestre põe uma só.*

---

# § 4 · A LISTA PRONTA PRO `Claude 2` — `24` linhas varridas por script

> ### ⚠ Nada disto é trabalho deste projeto. Outra conta escreve lá.
> **E nada disto está na `sobrecarga/MEXIDAS-no-repositorio.md`** — *ela cobre a peça 26 e o gerador de
> FEITIÇO. O `gerador-inimigo/` não é nenhum dos dois.*

**Detalhe linha a linha em `MEDIDA-o-remapeamento-das-seis.md` §7.** *O resumo:*

| onde | quantas | o que é |
|---|---|---|
| `gerador-inimigo/dados.js` | **`13`** | as categorias, as seis fichas, o câmbio, a derivação do seis |
| `gerador-inimigo/make.js` | **`11`** | a instrução ao mestre, o exemplo, duas frases já mortas |
| `conferir-ficha.py` bloco `7` | — | acende junto |
| regenerar o `.docx` | — | pelo `make.js` |

## As três que MORDEM

| # | o quê |
|---|---|
| **`1`** | ⚠⚠ **`make.js` `L176`** repete literal a frase que o item `5` matou por medição — *"não existe degrau acima da `Calamidade`"*. **A `MEXIDAS` marcou a cópia da peça 26; ninguém tinha visto a do gerador — e é essa que vai impressa** |
| **`2`** | ⚠⚠ **o nome `Calamidade` não é renomeação.** *A morta (`6` pessoas / `1,50`) vira **`Catástrofe`**, e uma `Calamidade` NOVA (`8` / `2,00`) entra por cima.* **Trocar só as seis e deixar ela quieta é a armadilha** |
| **`3`** | ⚠⚠ **uma mexida é CÓDIGO, não texto.** *O `make.js` computa tudo de `FAIXAS × CATEGORIAS`; o `Capanga` não sai daí — a vida dele é `dano do grupo ÷ 4`* |

## E duas linhas de texto que a decisão de hoje muda

| onde | de | ⟹ para |
|---|---|---|
| `dados.js` `L77` · `make.js` `L281` | *"a faixa do nível `2` ao `6` cruza duas linhas com as QUATRO categorias — oito células"* | **a derivação nova, e a faixa agora vai ao `12`** — *ver o `§5`* |
| `make.js` `L318` | *"A `Calamidade` da faixa fica de fora porque exige seis feiticeiros"* | ⚠ **na escada viva quem exige seis é a `Catástrofe`; a `Calamidade` exige `8`.** *A frase continua verdadeira e passa a apontar pro bicho errado* |

---

# § 5 · ⚠ O QUE A DECISÃO ABRE, e está declarado de propósito

**A grade viva fecha em `6` células** *(`2` faixas × `3` categorias que uma mesa de `4` aguenta)*.
**A decisão de hoje NÃO preenche essa grade** — *ela espalha as seis por três faixas:*

| faixa | `Capanga` | `Ameaça` | `Desastre` |
|---|---|---|---|
| `2 a 4` | ⚠ **vazio** | `Betobeto` · `Kamaitachi` *(×2)* | `Tsuchigumo` |
| `5 a 8` | ⚠ **vazio** | `Hitotsume` | `Oni` |
| `9 a 12` | — | `Kitsune` | — |

> ### Isso não é defeito: é o preço da `F`, e ele foi escolhido de olho aberto.
> **A coluna `Capanga` fica vazia**, e o texto que deriva o número seis deixa de fechar.
>
> ⟹ **Duas saídas, e nenhuma é urgente:** *reescrever a derivação pra "seis porque são seis"*, ou
> **escrever `1` a `2` fichas de `Capanga` novas** *(é ficção, e é dele)*. **Fica anotado, não em fila.**

---

## De onde saiu

**`medir-a-dupla.py` §1–§9** *(a conta)* · **`MEDIDA-o-remapeamento-das-seis.md`** *(o laudo)* ·
**peça 26 §4·§4.1·§4.3·§4.4·§4.5** · **`a-escada-com-numero.md`** *(o registro de que a `Dupla` foi
morta)* · **`A-TABELA-pontos-por-acao.md`** *(o `4,2` e o `24,2`)* · **`DECIDIDO-o-capanga.md` §1**
*(a banda)* · **`gerador-inimigo/dados.js`** *(o dono das seis)*

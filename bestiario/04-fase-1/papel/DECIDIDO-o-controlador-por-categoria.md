# O `Controlador` — o corte vira POR CATEGORIA

*10/09/2026. Conta em `dimensionar-o-controlador.py`, saída em `SAIDA-o-controlador.txt`.*
**Item `10` da fila — o achado `1` do teste de ponta a ponta.**

> ***Decisão do Mizuki, 10/09/2026:*** *"Corte por categoria"* — a saída `C` das quatro que foram
> apresentadas com o trade-off calculado.

---

## O problema, em uma tabela

**O corte único de `1/3` joga `o golpe` abaixo do piso da banda em `4` de `4` categorias, em `3` de `3` níveis medidos.**

| categoria | nv10 | nv20 | nv30 |
|---|---|---|---|
| `Ameaça` | `22,8%` → **`15,2%`** ⚠ | `22,7%` → **`15,1%`** ⚠ | `22,6%` → **`15,1%`** ⚠ |
| `Desastre` | `27,7%` → **`18,5%`** ⚠ | `27,7%` → **`18,5%`** ⚠ | `27,7%` → **`18,5%`** ⚠ |
| `Catástrofe` | `24,4%` → **`16,2%`** ⚠ | `24,9%` → **`16,6%`** ⚠ | `25,0%` → **`16,7%`** ⚠ |
| `Calamidade` | `27,7%` → **`18,5%`** ⚠ | `27,7%` → **`18,5%`** ⚠ | `27,7%` → **`18,5%`** ⚠ |

*Piso da banda: `20%`.*

**E a causa é de ORDEM, não de conta.**

| | quando | o que fez |
|---|---|---|
| `medir-a-fila-barata.py` | **08:09 de 10/09** | mediu o `Controlador` em `48,7` de golpe e calibrou a banda em `20%` |
| `medir-a-intervencao.py` | **08:28 de 10/09** | pôs o fator `× 0,923` no dano de quem tem `Intervenção` |

`73 × 0,667` = `48,7` → **`20,0%`** — a banda foi calibrada nesse número exato.
`73 × 0,923 × 0,667` = `44,9` → **`18,5%`** — o fator entrou dezenove minutos depois.

> ### `32% × 0,923 × 0,667` não foi conta que alguém rodou.

**E a `Ameaça` está fora desde ANTES do fator existir** — `22,7% × 0,667` = `15,1%`, e nenhum `0,923`
encostou nela. *A `MEDIDA-a-fila-barata` mediu o `Controlador` só no `Desastre`.*

---

# ⚠ E RODANDO A DECISÃO, ELA APARECEU EM DUAS FORMAS

**As duas são "corte por categoria". A `B` é melhor, e o motivo já estava publicado.**

## Forma `A` — o corte de dano varia por categoria

*A leitura literal da decisão: cada categoria tem a própria fração de corte, escolhida como a maior
fração `1/N` que ainda cabe na banda.*

| categoria | teto que a banda dá | a fração | corta | **vida ×** | a fatia fica | na banda? |
|---|---|---|---|---|---|---|
| `Ameaça` | `11,5%` | **`1/9`** | `11,1%` | `1,125×` | `20,1%` | sim |
| `Desastre` | `27,8%` | **`1/4`** | `25,0%` | `1,333×` | `20,8%` | sim |
| `Catástrofe` | `17,9%` | **`1/6`** | `16,7%` | `1,200×` | `20,3%` | sim |
| `Calamidade` | `27,8%` | **`1/4`** | `25,0%` | `1,333×` | `20,8%` | sim |

**O invariante fecha em `1,000` nas quatro.** *E as quatro pousam entre `20,1%` e `20,8%` — encostadas
no piso, porque o `Controlador` **é** o piso.*

### ⚠ Mas ela tem um defeito que a conta expôs

**A peça 19 §2.2 preça efeito em AÇÃO NEGADA, `1 pra 1`. E o corte não dá ação inteira em nenhuma:**

| categoria | ações | a fração | = quantas ações dele | e do grupo |
|---|---|---|---|---|
| `Ameaça` | `1` | `1/9` | **`0,11`** | `0,11` |
| `Desastre` | `3` | `1/4` | `0,75` | `0,75` |
| `Catástrofe` | `5` | `1/6` | `0,83` | `0,83` |
| `Calamidade` | `6` | `1/4` | `1,50` | `1,50` |

> **`0,11` de ação negada não é jogável.** *Nem `0,75`, nem `1,50`.* **O papel compraria fração de
> ação, e a régua vende ação inteira.**

---

## ✅ Forma `B` — ele paga em VIDA, e o motivo já estava escrito

**A `A-TABELA-dos-seis-papeis` §4 explica por que o `Artilheiro` e o `Emboscador` pagam em vida:**

> *"Pagar em dano significaria subir o dano de algum outro, e a banda só dá `1,07×` de espaço num
> `Desastre`.* **Pagar em vida não encosta na banda.**"

> ### ⟹ O `Controlador` fura a banda porque ele é o ÚNICO dos seis que paga em DANO.
> **Se ele pagar em vida, `o golpe` não se move e a banda nunca entra no caminho.**

**A conta:** *`1` ação negada do grupo vale `1` ação dele (peça 19 §2.2, `1 pra 1`), e `1` ação dele é
`dano ÷ ações`. Então o ganho multiplica a saída dele por `(1 + 1/ações)`, e ele paga
`vida × 1 ÷ (1 + 1/ações)`.*

| categoria | ações | **ganha** | **paga vida** | produto | `o golpe` | na banda? |
|---|---|---|---|---|---|---|
| `Ameaça` | `1` | `2,000×` | **`× 0,500`** | `1,000×` | `22,7%` | **sim** |
| `Desastre` | `3` | `1,333×` | **`× 0,750`** | `1,000×` | `27,7%` | **sim** |
| `Catástrofe` | `5` | `1,200×` | **`× 0,833`** | `1,000×` | `24,9%` | **sim** |
| `Calamidade` | `6` | `1,167×` | **`× 0,857`** | `1,000×` | `27,7%` | **sim** |

### E a vida que sai na ficha, no nv20

| categoria | vida crua | **com `Controlador`** | ações negadas |
|---|---|---|---|
| `Ameaça` | `165` | **`82`** | **`1` inteira** |
| `Desastre` | `660` | **`495`** | **`1` inteira** |
| `Catástrofe` | `990` | **`825`** | **`1` inteira** |
| `Calamidade` | `1320` | **`1131`** | **`1` inteira** |

> ### As quatro fecham em `1,000`, `o golpe` fica onde estava, e a ação negada é UMA INTEIRA em todas.
> **Inclusive na `Ameaça`, que na forma `A` era o caso sem saída.** *Ela paga metade da vida por negar
> uma ação — caro, e justo: ela tem UMA ação, então negar uma do grupo dobra a saída dela.*

### O que a forma `B` resolve de quebra

| o que estava aberto | como ela fecha |
|---|---|
| **a pendência da `A-TABELA` §5 item `4`** — *"falta decidir o que o `Controlador` faz nas categorias de `1` ação"* | **fecha.** A `Ameaça` paga `× 0,500` de vida e funciona |
| o `Controlador` sendo o piso da banda | **ele deixa de ser o piso.** *E aí a banda pode voltar pra `21%`–`32%`, que era o número publicado da escada — ⚠ **isso é outra decisão**, e ela desfaz o item `1` da `DECIDIDO-a-fila-barata`* |
| o `Controlador` ser o único papel que mexe em `o golpe` | **fecha.** Os seis passam a não mover `o golpe` — que é o que faz a tabela dos papéis ser legal |

### ⚠ O que ela PEDE, e a forma `A` não

**Uma frequência escrita.** *"`1` ação negada" — por luta? por rodada?*

**A conta acima é POR LUTA**, porque o `1 pra 1` da peça 19 §2.2 é sobre a luta. *Isso é uma linha de
texto no capítulo, e é decisão.*

---

# ⟹ A recomendação, e o que falta

> ## Forma `B`.
> **Ela obedece a mesma disciplina dos outros cinco papéis, fecha a pendência da `Ameaça`, e devolve a
> propriedade que a tabela dos seis mais vendia: `o golpe` não se move em nenhum papel.**

**Falta o Mizuki bater o martelo em duas coisas:**

| # | a escolha |
|---|---|
| **1** | **forma `A` ou `B`** — as duas são "corte por categoria", e as duas fecham em `1,000` |
| **2** | *(se `B`)* **a frequência da ação negada** — por luta, ou por rodada. **A conta acima é por luta** |
| **3** | *(se `B`)* **a banda volta pra `21%`–`32%`?** — o piso de `20%` existia só por causa do `Controlador`. **Isso desfaz o item `1` da `DECIDIDO-a-fila-barata.md`**, e é mexida em número publicado da escada |

---

## E o que NÃO foi medido aqui

**O `Capanga`.** *A tabela dele tem outro formato de coluna na `TABELA.md` e o script não lê — e ele
tem fator de dano próprio (`0,33` contra `0,25` de vida), então ele não é uma `Ameaça` com outro nome.*
**Não é "passou": é não medido.**

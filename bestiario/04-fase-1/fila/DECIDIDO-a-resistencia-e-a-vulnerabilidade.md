# DECIDIDO — resistência, imunidade e vulnerabilidade na ficha do inimigo

*10/09/2026. **Os quatro martelos batidos por ele.** Medição em `MEDIDA-a-resistencia-e-a-vulnerabilidade.md`
e `MEDIDA-a-imunidade-a-condicao.md`.*

---

# ⚡ `A` · A VULNERABILIDADE

> # ⟹ A REGRA, e ela é isto e nada mais:
> ## **O dano daquele tipo DOBRA contra ele.**
> ## **Nada mais na ficha muda — nem o fator, nem a vida, nem a categoria.**
>
> *O mestre escreve `Vulnerabilidades: Fogo` e acabou.*
> **De graça pra dar, de graça pra tirar.** *Tudo abaixo é só o porquê.*

---

## O porquê — ela não cobra e não devolve, `1,00×`

***Ele:*** *"Sim, mas é bom medir se outros sistemas abordam dessa forma"*

## ⟹ Mediram. E a medição foi CORRIGIDA por ele no mesmo dia

> ### ⚠⚠ Eu tinha publicado "o D&D 2024 apagou a vulnerabilidade". Errado, e o erro é de DADO.
> *Ele mandou o statblock da **Múmia** do `MM'25` p.`219` — **`Vulnerabilities Fire`**.* **O meu
> `srd-2024.json` traz o campo dela VAZIO; o `srd-2014.json` traz `fire`.** ⟹ *a coleta perdeu a célula.*
> ✅ **Canário instalado** no `medir-resistencia-imunidade.py` §0b pra isso não passar batido de novo.

## E com a correção o resultado fica MAIS forte, não mais fraco

| sistema | tem vulnerabilidade? | mexe no **CUSTO DE ENCONTRO**? | mexe na **VIDA**? |
|---|---|---|---|
| **D&D 2024** | ✅ **sim** — a Múmia, e `9` bichos vulneráveis a fogo no `MM` | ### ❌ **não** — a Múmia é `CR 3` como qualquer outra | ❌ **não** — `58` de vida contra `65` da mediana `CR 3`: **`0,892×`, MENOS** |
| **D&D 2014** | ✅ `15` = `4,6%` no SRD | ### ❌ **não** — o `CR` é o mesmo | ✅ fraca, `1,059×` |
| **Pathfinder 2e** | ✅ | ### ❌ **não** — o nível é o mesmo | ✅ *"if a creature has a weakness… **give it additional HP**"* |
| **Draw Steel** | ✅ `88` = `10,6%` | ### ❌ **não** — `EV` mede `1,000` em `17` coortes | ❌ **não** — `Stamina` mede `1,000` |

> ## ⟹ `4` de `4` sistemas TÊM vulnerabilidade, e `4` de `4` NÃO mexem no custo de encontro.
> **Antes eram `3` de `3` porque eu tinha jogado o D&D 2024 fora por engano.** *Com ele de volta, a
> unanimidade é de quatro — e a conclusão é a mesma.*

**E o campo continua raro:** *"apesar de mais de cem statblocks novos no `MM` de 2024, existe **o mesmo
número** de vulnerabilidades"* — **ela não sumiu, ela ficou parada enquanto o livro cresceu.**

---

# ⚡ `A2` · E A VIDA NÃO SOBE — ele perguntou, e a conta responde

***Ele:*** *"ent como fica questão de vunerabilidade? da mais vida?"*

## ⟹ Não. A vulnerabilidade é `1,00×` no fator **e** `1,00×` na vida.

**Dois dos quatro não compensam nada** *(D&D 2024 e Draw Steel)*, um compensa fraco *(`1,059×`)*, e um
manda compensar no texto *(PF2e)*. **E o argumento decide contra compensar:**

> ### Dar vida de volta tem O MESMO defeito da vulnerabilidade que devolve orçamento — só que invertido.
> *Se o grupo NÃO tem aquele tipo de dano, o bicho ganhou `1,61×` de vida de graça, e o encontro fica
> **mais duro** do que a ficha cobra.* **A ficha não pode conferir o que o grupo carrega — nem pra
> cobrar, nem pra devolver.**

## E quanto ela vale de verdade, medido

| se, dos `4` personagens, batem naquele tipo | a saída do grupo | a luta encurta |
|---|---|---|
| **`1`** | `× 1,25` | **`20%`** |
| `2` | `× 1,50` | `33%` |
| `4` | `× 2,00` | `50%` |

> **É real e é limitado, e ela paga quem se preparou.** *Um grupo que descobre a fraqueza do bicho e
> monta em cima dela ganha `20%` de luta — não a luta inteira.* **Isso é a mecânica funcionando, não
> um furo.**

> ### ⟹ A regra final: **a vulnerabilidade é ficção com retorno. Ela não cobra, não devolve, e não muda a vida.**

---

# ⚡ `B` · A LINHA DO BLOCO DIZ `Vulnerabilidades`

***Ele:*** *"Vunerabilidade, fraqueza normalmente é pra algo mais narrativo, vunerabilidade é o dano"*

**O bloco dizia `Fraquezas`; as peças `19` e `26` dizem `vulnerabilidade`.** *Agora os três dizem a
mesma coisa.*

> ### 🆕 E o argumento dele LIBERA a palavra `fraqueza` — ela não fica órfã, ela muda de lado
> **`vulnerabilidade` = mecânica, e é dano.** **`fraqueza` = narrativa.**
>
> *E o Bestiário tem exatamente onde pôr a segunda:* **o lado de LORE, modelo Volo's Guide**
> *(`DECIDIDO-o-pacote-de-tipo.md` §5)*. **A fraqueza de um bicho — o que ele teme, o que o atrai, o
> que faz ele parar — é entrada de catálogo, não célula de bloco.**

---

# ⚡ `C` · A IMUNIDADE A CONDIÇÃO VAI NA CÉLULA `Imunidades`, JUNTO

***Ele:*** *"N precisa, vai tudo em imunidade, mesma celula"*

**Sem célula nova.** *E o texto se separa sozinho: tipo de dano é substantivo de dano, condição é nome
de condição.*

> **`Imunidades` `Veneno`, `Atordoado`**

## ⟹ E isso PUBLICA a régua do item `25`, que já estava medida

**Toda âncora é publicada** — `9` golpes na luta (peça 26 §5), `±25 pp` (peça 11), o custo em ação de
cada condição (peça 19 §2.2), a duração de `1` rodada (`partD.js`).

| condição | imunidade a ela vale |
|---|---|
| `Atordoado` | **`× 1,20`** |
| `Derrubado` · `Impedido` · `Cego` · `Amedrontado` · `Envenenado` | `× 1,19` |
| `Calado` · `Enfeitiçado` | `× 1,12` |
| `Lento` | `× 1,06` |
| `Incapacitado` · `Agarrado` · `Desarmado` · `Surdo` | **`1,00×`** |

> ### A linha que vai pro §6.3, e ela é UMA:
> **"Ser imune a uma condição que rouba ação do inimigo, ou que dá desvantagem nos ataques dele,
> multiplica o fator por `1,20`. Imunidade a qualquer outra condição custa `1,00×`."**
>
> *O erro de simplificar assim é `+13%` no `Lento` e `+7%` no `Calado`, e ele **sobrecobra** — a mesa ganha.*

---

# ⚡ `D` · O `Físicos` CONTINUA VENDÁVEL — com linha de aviso, não com trava

***Ele:*** *"Sim"*

**A conta está certa e o mecanismo está validado em duas edições** *(`0,889×` no 2024, `0,882×` no
2014, dentro da faixa de CR)*. **O que o campo diz não é "está errado" — é "é raro".**

| | resistência em `Físicos` | imunidade em `Físicos` |
|---|---|---|
| D&D 2014 | `64,5%` das entradas | `26,0%` |
| ### D&D 2024 | ### **`0,0%`** | ### **`0,0%`** |

> ### A linha que vai junto do preço:
> **"Resistir a `Físicos` multiplica o fator por `1,43`; ser imune, por `2,50`. Um `Desastre` imune a
> `Físicos` exige `10` personagens, não `4`. A edição viva do D&D publica isso zero vezes em `331`
> blocos — se você vender, saiba que está vendendo o item mais caro do livro."**

---

# ⟹ O QUE ISSO MANDA MEXER

## No bloco *(`RASCUNHO-5` — ✅ aplicado)*
`1` a linha passa a dizer **`Vulnerabilidades`**
`2` a célula **`Imunidades`** passa a carregar tipo de dano **e** condição

## No repositório *(⚠ eu não escrevo — entra na `MEXIDAS-no-repositorio.md`)*
`3` **§6.3** — *"Vulnerabilidade devolve na mesma moeda"* ⟹ **"a vulnerabilidade é `1,00×`: não cobra,
não devolve e não muda a vida"**, com a nota de que **`4` de `4` sistemas não mexem no custo de encontro**
`4` **§6.3** — as `2` menções à **`Alcateia`** morta
`5` **§6.3** — 🆕 entra a **linha da imunidade a condição** (`1,20×` / `1,00×`)
`6` **§6.3** — 🆕 entra a **linha de aviso do `Físicos`**

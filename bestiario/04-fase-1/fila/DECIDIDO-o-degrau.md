# DECIDIDO — item `5`: "um degrau de categoria" morre como moeda

*10/09/2026. **Conta em `medir-o-degrau.py`.** Toda âncora lida do dono.*

> ## A escada nova não tem degrau de tamanho único, e três seções cobram em degrau.
> **A resposta já estava escrita na peça 26, no §6.4, e nunca chegou nas outras duas.**

---

# § 1 · O TAMANHO DE CADA DEGRAU, e ele espalha `4,00×`

| o degrau | vale |
|---|---|
| `Capanga` → `Ameaça` | **`1,000×`** — *não é degrau nenhum, os dois têm fator `0,25`* |
| `Ameaça` → `Desastre` | ### **`4,000×`** |
| `Desastre` → `Catástrofe` | `1,500×` |
| `Catástrofe` → `Calamidade` | `1,333×` |

**Do menor ao maior: `4,00×` de diferença.** *"Um degrau" pode querer dizer "nada" ou "quadruplicar".*

---

# § 2 · E `3` DOS `4` PREÇOS NÃO CABEM EM DEGRAU NENHUM

| o que a peça cobra | vale | cabe? |
|---|---|---|
| §6.3 · resistir a `Físicos` | `1,430×` | `Desastre → Catástrofe`, errando `4,9%` |
| §6.3 · resistir a `Elementais` | `1,180×` | ⚠ **nenhum** — o mais perto erra `13,0%` |
| §6.4 · a **Expansão de Domínio** | `1,920×` | ⚠ **nenhum** — o mais perto erra `21,9%` |
| §6.3 · ser **IMUNE** a `Físicos` | `2,500×` | ⚠⚠ **nenhum** — o mais perto erra `40,0%` |

## ⚠ E duas frases publicadas são da escada MORTA

| a frase | o problema |
|---|---|
| §6.4 — *"os dois degraus de baixo da escada valem `2,00×`"* | **na escada nova eles valem `1,000×` e `4,000×`** |
| §6.4 — *"a Expansão **dobra a categoria**"* | **"dobrar" pousa numa categoria de verdade em `1` de `5` casos** — só `Desastre → Calamidade` |

---

# § 3 · O CAMPO — nenhuma escada de dificuldade tem degrau de tamanho único

| sistema | quantos degraus | do menor ao maior | espalha |
|---|---|---|---|
| D&D SRD 2024 | `27` | `0,874×` a `3,000×` | `3,43×` |
| D&D SRD 2014 | `27` | `0,728×` a `3,000×` | `4,12×` |
| Pathfinder 2e | `26` | `1,005×` a `1,938×` | `1,93×` |
| Draw Steel | `11` | `0,196×` a `4,764×` | **`24,25×`** |

> ### `0` de `4` têm degrau uniforme. "Um degrau da escada" não é unidade em lugar nenhum do campo.
> **E o campo cobra em MULTIPLICADOR** — *o `Guia do Mestre` de 2014 tem uma tabela de `Pontos de Vida
> Efetivos`, e o próprio §6.3 já cita ela como o mecanismo dele.*

---

# ⟹ § 4 · A DECISÃO: a moeda é o FATOR, e ele é contínuo

> ### O `degrau` some como moeda. Quem cobra é o **fator da categoria**, e ele se multiplica.
>
> **`fator novo = fator × o multiplicador da coisa`** — e a leitura sai de graça, porque a categoria
> já é definida como *"quantos personagens ele exige"*, com **`personagens = fator × 4`**.

## E funciona nos quatro preços, sem número novo

| o bicho | fica em | e isso pede |
|---|---|---|
| `Desastre` resistente a `Físicos` | `1,00 × 1,43` = **`1,43`** | `5,7` personagens |
| `Desastre` com Expansão | `1,00 × 1,92` = **`1,92`** | `7,7` personagens |
| `Calamidade` com Expansão | `2,00 × 1,92` = **`3,84`** | `15,4` personagens |
| `Desastre` **imune** a `Físicos` | `1,00 × 2,50` = **`2,50`** | `10` personagens |

> ### E o "não tem o que vender acima da `Calamidade`" deixa de ser um beco.
> **A `Calamidade` com Expansão não precisa de uma sexta categoria: ela precisa de um NÚMERO, e ele
> existe.** *`3,84` de fator, `15,4` personagens.*

## ⚠⚠ E este argumento JÁ ESTÁ PUBLICADO — no §6.4, e nunca chegou nas outras duas seções

> ***A peça 26 §6.4, palavra por palavra:*** *"**Isso não é impedimento: a categoria mede pessoas, e o
> número existe fora da escada do mesmo jeito.**"*
>
> ***E o parágrafo antes dele registra que o Mizuki já tinha achado o mesmo erro uma vez:*** *"não faz
> sentido um Sukuna da vida não ter expansão, ele seria Calamidade, não?"* — **e a conclusão foi
> exatamente esta: o que falta não é a permissão, é o número do encontro maior.**

**⟹ O item `5` não é régua nova. É propagar pro §6.3 e pro §6.5 a conclusão que o §6.4 já tirou.**

---

# § 5 · AS MEXIDAS — ⚠ e elas são no REPOSITÓRIO, que eu não escrevo

*Vão junto com os itens `6` e `11`, que também mexem no §6.5. **Um commit em vez de três.***

| # | onde | o que trocar |
|---|---|---|
| **`1`** | **§6.3**, a frase do preço | *"Resistência ao grupo `Físicos` custa **um degrau de categoria**"* ⟹ **"multiplica o fator da categoria por `1,43`"** |
| **`2`** | **§6.3**, a frase da imunidade | *"custa mais de um degrau, e **a escada não tem o que vender acima da `Calamidade`**"* ⟹ **"multiplica o fator por `2,50`, e o resultado é um número de pessoas, não um nome"** |
| **`3`** | **§6.4** | tirar *"os dois degraus de baixo da escada valem `2,00×`"* — **é da escada morta** — e trocar *"dobra a categoria"* por **"multiplica o fator por `1,92`"** |
| **`4`** | **§6.5**, a linha do câmbio | *"o que dá vida efetiva \| um **degrau de categoria**, pelo §6.3"* ⟹ **"multiplica o fator, pelo §6.3"** |
| **`5`** | **§3** e o `conferir-bestiario.py` | a linha *"custam degrau de categoria"* e a **checagem `8`**, que hoje confere que *"a peça declara em que moeda a resistência se paga"* — **a moeda passa a ser o fator** |

> ### ⚠ A checagem `8` do validador NÃO quebra, e é bom que não quebre.
> *Ela exige que a peça **declare** a moeda, não que a moeda seja "degrau".* **Trocar a declaração
> mantém ela verde.**

> ### E uma coisa que NÃO muda
> **Os cinco nomes ficam.** *`Capanga` · `Ameaça` · `Desastre` · `Catástrofe` · `Calamidade` continuam
> sendo os cinco degraus que o mestre lê.* **O que muda é que eles passam a ser RÓTULOS num contínuo,
> e não os únicos pontos onde dá pra parar.**

# MEDIDA — resistência, imunidade e vulnerabilidade na ficha do inimigo

***Pergunta dele, 10/09/2026:*** *"como ficou imunidades, resistencias e vunerabilidades para se
colocar nas fichas de inimigo?"*

**Conta em `medir-resistencia-imunidade.py`, saída em `SAIDA-resistencia-imunidade.txt`.**
*Toda âncora lida do dono; o script morre se o dono mudar.*

> # ⚠⚠ CAIXA DE CORREÇÃO — 10/09/2026, ele me pegou com um print
>
> **Eu publiquei "o D&D 2024 apagou a vulnerabilidade — `0` de `331`". ESTÁ ERRADO, e o erro é de DADO.**
>
> *Ele mandou o statblock da **Múmia** do `MM'25` p.`219`: **`Vulnerabilities Fire`**.*
> **A Múmia ESTÁ no meu `srd-2024.json`, e o registro dela vem com o campo VAZIO.** *O `srd-2014.json`
> traz `fire` certinho.* ⟹ **a coleta de 2024 perdeu a célula de vulnerabilidade.**
>
> ### O que muda: toda contagem de vulnerabilidade em `D&D 2024` aqui é PISO, não valor.
> **O que NÃO muda:** *resistência, imunidade e imunidade a condição — a Múmia traz as três
> preenchidas e elas conferem com o statblock publicado.* **E a conclusão do martelo `A` também não
> muda: ela fica mais forte** — *ver o `DECIDIDO`.*
>
> ✅ **Instalei um canário no `medir-resistencia-imunidade.py` §0b:** a Múmia é conferida contra o
> statblock publicado, e o script grita se o dado não bater. *Esse zero não passa batido de novo.*

---

# § 1 · O QUE JÁ EXISTE — e a tabela está CERTA

**A peça 26 §6.3 publica a tabela, e ela não é palpite: é a fórmula da própria seção, rodada.**

| grupo | peso | resistir | imune | vulnerável |
|---|---|---|---|---|
| `Físicos` | `60%` | **`1,43×`** | **`2,50×`** | `0,62×` |
| `Elementais` | `30%` | `1,18×` | `1,43×` | `0,77×` |
| `Especiais` | `10%` | `1,05×` | `1,11×` | `0,91×` |
| um tipo só | `20%` | `1,11×` | `1,25×` | `0,83×` |

**Refiz as doze células a partir do peso `60/30/10` da peça 19 §4:**
`resistir = 1 ÷ (1 − peso/2)` · `imune = 1 ÷ (1 − peso)` · `vulnerável = 1 ÷ (1 + peso)`.

> ### `12` de `12` fecham com menos de `1%` de distância. A tabela é conta, e ela está viva.
> *E o `0,62×` da vulnerabilidade é conta legítima também — ele não foi inventado.*

**E o bloco já tem a linha:** `**Resistências** — · **Imunidades** — · **Fraquezas** — · **Perícias** —`

---

# § 2 · ⚠⚠ MAS O COMMIT DA PEÇA 26 DEIXA DOIS BURACOS NO §6.3

*Achados conferindo a lista do item `5` (`DECIDIDO-o-degrau.md` §5) contra o texto vivo do §6.3.*

**A lista tem `5` trocas. Duas frases do §6.3 ficam de fora, e as duas quebram no dia que ele entrar.**

| # | a frase que fica pra trás | por que ela quebra |
|---|---|---|
| **`6`** | *"**Vulnerabilidade devolve na mesma moeda.**"* | **"a mesma moeda" é o DEGRAU**, e o item `5` mata o degrau como moeda. *As mexidas `1` e `2` trocam a resistência e a imunidade pro fator; a vulnerabilidade fica órfã apontando pra uma moeda que não existe mais* |
| **`7`** | *"Um chefe de **`Alcateia`** imune a `Físicos` vira uma luta de `7,50` rodadas…"* | ⚠ **`Alcateia` é da escada MORTA.** *`2` menções dentro do §6.3. É a **quinta** tabela velha achada — e o `ESTADO` já registra que esse é o padrão do projeto* |

> ### ⟹ As duas viram mexida `6` e `7`, e vão no MESMO commit.
> **A `6` é troca de uma linha:** *"Vulnerabilidade divide o fator: `× 0,62` nos `Físicos`, `× 0,77` nos
> `Elementais`, `× 0,91` nos `Especiais`."*
> **A `7` é trocar `Alcateia` pela categoria viva** — *e o exemplo tem de ser refeito com a vida da
> escada nova, senão ele publica um número morto.*

---

# § 3 · ⚠ E DUAS COISAS QUE A FICHA NÃO TEM

## `1` · O nome não bate

| | chama de |
|---|---|
| **`RASCUNHO-5`**, a linha do bloco | ### **`Fraquezas`** |
| **peça 26 §6.3** e **peça 19 §4** | **`vulnerabilidade`** |

**São a mesma coisa com dois nomes, e um deles é o que o mestre lê na ficha.** *Escolher é de graça —
mas é escolha, não conta.*

## `2` · ⚠⚠ NÃO EXISTE CÉLULA PRA IMUNIDADE A CONDIÇÃO, e ela não é preçada em lugar nenhum

**Varredura nas peças `19` e `26`: `0` menções a imunidade de condição.** *A `19` é a dona das treze
condições e não fala nisso; a `26` só preça tipo de DANO.*

**E o campo imprime, e não é pouco:**

| | quantos blocos têm | mediana de entradas | máximo |
|---|---|---|---|
| **D&D 2024** — `331` blocos | **`75` = `22,7%`** | `2` | `11` |
| **D&D 2014** — `325` blocos | `92` = `28,3%` | `3` | `9` |
| **Draw Steel** | ### **não existe** — nem célula, nem regra | — | — |

> ### O buraco: um inimigo imune a `Atordoado` APAGA o que o jogador comprou, e nada cobra por isso.
> *A peça 19 §2.2 preça o que cada condição ENTREGA, e o §6.5 preça a condição que o inimigo PÕE.*
> **Ninguém preça a condição que o inimigo NEGA.**

---

# § 4 · O CAMPO — e ele apagou exatamente o que a gente cobra mais caro

*`331` blocos do SRD 2024 contra `325` do SRD 2014. **É experimento natural: a mesma linha, revisada.***

## ~~`4a` — a VULNERABILIDADE morreu na revisão~~ ❌ **REFUTADO — ver a caixa de correção no topo**

| | blocos com vulnerabilidade |
|---|---|
| **D&D 2014** | `15` = `4,6%` — *`Fogo` `6`, `Concussão` `5`, `Frio` `2`, `Trovejante` `1`, `Perfurante` `1`, `Radiante` `1`* |
| ~~**D&D 2024**~~ | ~~`0` de `331`~~ ### ⚠ **é `0` da COLETA, não do desenho.** *A Múmia do `MM'25` tem `Vulnerabilities Fire` e o nosso registro dela vem vazio* |

**E em 2014 ela ERA preçada, no sentido que a §6.3 prevê:** *dentro da faixa de CR, quem tinha
vulnerabilidade imprimia `1,059×` a vida de quem não tinha.* **O desconto foi gasto em vida, exato
como o nosso `0,62×` manda.**

> ### ⟹ ~~O campo apagou a mecânica.~~ ❌ **Não apagou: ela ficou RARA.**
> *"Apesar de mais de cem statblocks novos no `MM` de 2024, existe **o mesmo número** de
> vulnerabilidades"* — **ela não cresceu junto com o livro.** *E `9` bichos vulneráveis a fogo é o
> maior número de qualquer tipo.*
>
> **O que a medição do 2014 continua provando, e isso não caiu:** *quem tinha vulnerabilidade imprimia
> `1,059×` a vida — o `CR` não se moveu.* ### **O custo de encontro nunca muda. Essa parte é sólida.**

## `4b` — e a resistência a `Físicos` morreu junto ✅ **e o print DELE confirma isto**

> **A Múmia é a prova viva:** *no SRD 2014 ela tinha `bludgeoning, piercing, and slashing from
> nonmagical attacks`.* **No `MM'25` do print dele a linha `Resistances` NÃO EXISTE.** *Mesma criatura,
> mesmo `CR 3`, mesma vida `58` — e a resistência física sumiu.*

| | entradas de resistência em `Físicos` | em `Elementais` | em `Especiais` |
|---|---|---|---|
| **D&D 2014** — `242` entradas | **`64,5%`** *(`Perfurante` `54`, `Concussão` `52`, `Cortante` `50`)* | `31,8%` | `3,7%` |
| ### **D&D 2024** — `105` entradas | ### **`0,0%`** | `77,1%` | `22,9%` |

**E na imunidade a mesma coisa:** *`26,0%` em `Físicos` no 2014, **`0,0%`** no 2024.*

> ### ⚠⚠ As DUAS células mais caras da nossa tabela — `resistir a Físicos` `1,43×` e `imune a Físicos` `2,50×` — preçam a coisa que a edição viva do campo imprime ZERO vezes.
> *E isso é a **terceira** vez que este mesmo experimento natural aparece no projeto:* a
> `MEDIDA-a-morte-e-a-imunidade.md` já tinha achado os `17` blocos `nonmagical` de 2014 virarem
> **`0` de `331`** em 2024. **Aqui ele aparece no eixo inteiro, não só na trava por propriedade.**

## `4c` — e a resistência que SOBROU é preçada, do jeito que a §6.3 diz

*Comparação feita DENTRO da faixa de CR, senão ela só mede o CR.*

| | vida impressa de quem tem ÷ de quem não tem | o que quer dizer |
|---|---|---|
| **resistência, D&D 2024** | **`0,889`** | ✅ **preçada** — cortaram vida impressa porque a efetiva subiu |
| resistência, D&D 2014 | `0,882` | ✅ preçada, e o valor é o mesmo |
| vulnerabilidade, D&D 2014 | `1,059` | ✅ preçada ao contrário, como manda |
| imunidade, D&D 2024 | `1,066` | ⚠ **de graça** — *e faz sentido: `66` das `169` entradas são `Veneno`* |

> **O mecanismo da §6.3 está validado por duas edições independentes.** *Ela não é invenção nossa —
> é o que o `Guia do Mestre` de 2014 faz, e a §6.3 já cita ele.*

## `4d` — e o Draw Steel resolve por um TERCEIRO caminho: número, não binário

*`828` statblocks lidos.* **Lá as duas células são impressas SEMPRE, com `-` quando vazias.**

| | quantos têm | e o valor é |
|---|---|---|
| **`Immunity`** | `280` = **`33,8%`** | ### **um NÚMERO** — mediana `4`, de `1` a `10`. *É redução fixa de dano daquele tipo, não "não recebe nada"* |
| **`Weakness`** | `88` = **`10,6%`** | **um NÚMERO** — mediana `5`, de `3` a `8`. *É acréscimo fixo, não "dobra"* |

**Onde eles põem:** *imunidade em `corruption` `104`, `poison` `102`, `psychic` `74`, `fire` `66`.
Fraqueza em `holy` `70`, `acid` `12`, `fire` `6`.*

> ### ⚠⚠ E o EV deles NÃO VÊ nenhuma das duas.
> *Medido em `47` coortes de mesmo nível + organização pra imunidade e `17` pra fraqueza:*
> **`1,000` exato nas duas.** *Lá as duas células são **de graça** — o preço sai de nível +
> organização, e a forma some dentro dele.* **É o mesmo desenho que já derrubou o preço do `tamanho`
> (item `16`) e o da área natural (item `15`).**

---

# § 5 · QUANTAS ENTRADAS CABEM NUMA CÉLULA

| | mediana *(nos que têm)* | máximo |
|---|---|---|
| resistência, D&D 2024 | `2` | `5` |
| imunidade, D&D 2024 | `1` | `3` |
| resistência, D&D 2014 | `3` | `8` |
| imunidade a condição, D&D 2024 | `2` | **`11`** |

> **A célula é barata de layout** — *ela não gasta entrada nomeada, e a linha de `6` entradas do
> `RASCUNHO-5` não sente.* **O que é caro é o PREÇO de encontro, não o espaço.**

---

# ⟹ § 6 · OS QUATRO MARTELOS, com a conta pronta

## Martelo `A` — a vulnerabilidade continua devolvendo orçamento?

| # | a saída | o que ela custa |
|---|---|---|
| **`1`** ⭐ | **continua, e vira `fator × 0,62` / `0,77` / `0,91`** — só troca a moeda, como a resistência | **uma linha no commit** *(a mexida `6`)*. ⚠ *Custa o risco de assimetria — ver abaixo* |
| **`2`** | **vira DE GRAÇA** — `1,00×`, declarada e não preçada, como o `tamanho` e a área | *é o desenho do Draw Steel, e ele mede `1,000` exato.* **Custa a simetria com a resistência, que continua cobrando** |
| **`3`** | **some da ficha**, como o D&D 2024 fez | mais honesto com o campo vivo. *Custa uma alavanca de ficção que o `Bestiário` usa bem — o oni que queima* |

> ## ⚠ E existe uma ASSIMETRIA medida, que é o argumento de verdade
> **A resistência erra pro lado SEGURO; a vulnerabilidade erra pro lado PERIGOSO.**
>
> *Se o inimigo resiste a um tipo que o grupo não usa, ele **pagou** `1,43×` por nada — o encontro foi
> cobrado mais caro do que é, e a mesa ganha.*
> *Se ele é vulnerável a um tipo que o grupo não usa, ele **recebeu** `0,62×` de desconto por nada — o
> encontro foi cobrado mais barato do que é, e a mesa perde.*
>
> ### ⟹ E foi exatamente essa a revisão que o campo fez: o D&D 2024 MANTEVE a resistência (`16,0%` dos blocos) e APAGOU a vulnerabilidade (`0` de `331`).
>
> **Recomendação: `2`.** *Ela guarda a ficção — o oni ainda queima — e tira a única porta do sistema
> que barateia o encontro por uma coisa que a ficha não pode conferir.* ⚠ *A `3` também é defensável,
> e é a que o campo fez de verdade; o que não recomendo é a `1`, porque ela paga um desconto sem saber
> se ele vai ser cobrado.*

## Martelo `B` — `Fraquezas` ou `Vulnerabilidades` na linha do bloco?

> **Recomendação: `Vulnerabilidades`.** *É o nome que as peças `19` e `26` usam, e a ficha é a que
> tem menos leitor — mudar o nome nela custa uma linha, mudar nas peças custa duas seções.*
> ⚠ *Se ele preferir `Fraquezas` por gosto, aí a troca é nas peças, e entra no mesmo commit.*

## Martelo `C` — a imunidade a CONDIÇÃO tem célula?

| # | a saída | o que ela custa |
|---|---|---|
| **`1`** ⭐ | **cabe na célula `Imunidades` que já existe** — *"Imunidades: `Veneno`, `Atordoado`"* | zero. *E o texto já separa sozinho: tipo de dano é substantivo de dano, condição é nome de condição* |
| **`2`** | **linha própria**, como o D&D imprime | mais claro. *Custa uma linha em `77%` dos blocos que não vão usar ela* |
| **`3`** | **não existe** — o inimigo nunca é imune a condição | mais simples. *Custa a ficção: a maldição que não dorme, o corpo que não sangra* |

> **Recomendação: `1`.** ⚠ **Mas ela abre a pergunta do preço, e essa não é de graça:** *imunidade a
> condição apaga ponto que o JOGADOR gastou, e o sistema não preça isso em lugar nenhum.*
> **Se for `1` ou `2`, isso vira item de fila próprio.**

## Martelo `D` — o `Físicos` continua vendável?

> **Recomendação: FICA, e ganha uma LINHA de aviso — não uma trava.**
> *A conta está certa e o mecanismo está validado. O que o campo diz não é "está errado", é "é raro":*
> **`0` de `331` blocos da edição viva imprimem resistência a `Físicos`.**
>
> ⟹ *A linha honesta é:* **"resistir a `Físicos` multiplica o fator por `1,43`, e ser imune por
> `2,50`. Um `Desastre` imune a `Físicos` exige `10` personagens, não `4`. O campo publica isso zero
> vezes — se você vender, saiba que está vendendo o item mais caro do livro."*

---

# § 7 · O QUE NÃO PRECISA DE MARTELO

| | por quê |
|---|---|
| **a tabela de `1,43` / `2,50` / `0,62`** | ✅ **é conta, e as `12` células fecham** com a fórmula da própria §6.3 |
| **o mecanismo "vida efetiva"** | ✅ **validado em duas edições** — `0,889` no 2024 e `0,882` no 2014, dentro da faixa de CR |
| **a célula caber no bloco** | ✅ **não gasta entrada nomeada.** Mediana do campo é `2` resistências e `1` imunidade |
| **o pacote de `tipo` na célula `Imunidades`** | ✅ **não entra** — o `maldição` é ponteiro pro capítulo, `DECIDIDO-o-pacote-de-tipo.md`. *A célula é pra imunidade ESPECÍFICA daquele bicho* |

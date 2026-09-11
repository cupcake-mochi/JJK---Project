# O `Capanga` na varredura da banda — item `17`

*10/09/2026. Conta em `medir-o-capanga.py`, saída em `SAIDA-o-capanga.txt`.*
**Ele ficou de fora de três varreduras seguidas. Agora foi medido.**

> **O que a fila dizia:** *"a tabela dele tem outro formato de coluna e o script não lê. **Não é
> 'passou': é não medido.** E ele tem fator de dano próprio (`0,33` contra `0,25` de vida), então não
> é uma `Ameaça` com outro nome. **É meia hora de regex**."*

**Era meia hora de regex. E as duas frases depois dela estavam erradas.**

---

# O que a medição achou — em uma tabela

| # | o achado | tamanho | mexe onde |
|---|---|---|---|
| **`1`** | **a fatia publicada do `Capanga` na escada está errada** — `30%` contra `22,7%` medidos | **grande** | `a-escada-com-numero.md` |
| **`2`** | **o topo `32%` da banda é fantasma** — ele É o `Capanga`, calculado com o fator morto. **Ninguém encosta em `32%`** | **o maior** | a banda, de novo |
| **`3`** | `o golpe` do `Capanga` está **DENTRO** da banda em `4` de `4` níveis. *Ele nunca foi o problema* | — | nada |
| **`4`** | **os papéis que pagam em VIDA não são neutros num enxame** — `Brutamontes` `+25%`, e ele **quebra a trava** | **grande** | a tabela dos seis |
| **`5`** | **o `Controlador` no esquadrão: `ações` de quem?** `1` por corpo ou `8` por esquadrão — `0,67×` contra `1,01×` | médio | `DECIDIDO-o-controlador` |

---

# `1` · A fatia publicada dele está errada, e o fator morto é a causa

**A escada tem DUAS tabelas de fator, e a de cima morreu.**

| onde | fator de vida | fator de dano |
|---|---|---|
| a tabela do **topo** — *"o fator agora é DUPLO"* | `0,25` | **`0,33`** |
| a escada **FECHADA**, embaixo | `dano do grupo ÷ 4` | **`0,25`** |

**A `TABELA.md` implementa o `0,25`.** *O golpe do `Capanga` é igual ao da `Ameaça` em todo nível —
`4d8 + 19` no nv20, nos dois.*

**Mas a linha de fatia da escada ficou na versão morta:**

| nv | golpe de `1` | fatia **recomputada** | fatia **publicada** | bate? |
|---|---|---|---|---|
| `2` | `4,0` | **`21,8%`** | `32%` | **não** |
| `10` | `19,0` | **`22,8%`** | `30%` | **não** |
| `20` | `37,0` | **`22,7%`** | `30%` | **não** |
| `30` | `55,0` | **`22,6%`** | `30%` | **não** |

> ### A razão entre as duas é `1,327`. E `0,33 ÷ 0,25` = `1,320`.
> **Não é aproximação: é a assinatura do fator morto.**

---

# `2` · E por isso o topo `32%` da banda é fantasma

**A banda existe pra vigiar o topo — a própria escada escreve isso.** *"a do bestiário antigo era de
`23%` a `45%`, **e o topo dela era a `Dupla`**".*

**Quem está no topo hoje, nv20, com o fator da `Intervenção` aplicado:**

| categoria | golpe cru | tem `Intervenção`? | golpe efetivo | fatia |
|---|---|---|---|---|
| `Capanga` | `37,0` | não | `37,0` | `22,7%` |
| `Ameaça` | `37,0` | não | `37,0` | `22,7%` |
| **`Desastre`** | `49,0` | **sim** | `45,2` | **`27,7%`** |
| `Catástrofe` | `44,0` | sim | `40,6` | `24,9%` |
| **`Calamidade`** | `49,0` | **sim** | `45,2` | **`27,7%`** |

> **O topo real é `27,7%`. A banda publicada vai até `32%`.**
> ### Sobram `4,3` pontos de teto que ninguém alcança — e um teto que ninguém alcança não vigia nada.

**E o `32%` tinha dono:** *era o `Capanga` no nv2, calculado com o `0,33`. Recomputado com o `0,25`,
ele dá `21,8%`.*

## A banda MEDIDA — `29` níveis × `5` categorias

*A varredura que fechou a banda olhou `3` níveis e `4` categorias. Esta olha todas.*

| categoria | mínimo | onde | máximo | onde |
|---|---|---|---|---|
| `Capanga` | `21,8%` | nv`2` | `23,1%` | nv`8` |
| `Ameaça` | `21,8%` | nv`2` | `23,1%` | nv`8` |
| `Desastre` | `27,7%` | nv`2` | `27,7%` | nv`30` |
| `Catástrofe` | `22,7%` | nv`2` | `25,1%` | nv`16` |
| `Calamidade` | `27,7%` | nv`2` | `27,7%` | nv`30` |
| **TODAS** | **`21,8%`** | `Ameaça` nv`2` | **`27,7%`** | `Desastre` nv`30` |

> ### ⟹ A banda medida é `21,8%` – `27,7%`. Arredondando como a escada faz: **`21%` – `28%`**.
> *A publicada é `20%`–`32%`. Ela sobra `1,8` ponto embaixo e `4,3` em cima.*

**E o piso `20%` ficou órfão.** *Ele existia porque o `Controlador` cortava `1/3` do dano. A forma `B`
tirou o corte do dano e pôs em vida — **`o golpe` não se move mais em papel nenhum.***

---

# `3` · O `Capanga` estava dentro da banda o tempo todo

**`4` de `4` níveis, dentro.** *Ele não era o risco que a fila supunha.* **E ele é o PISO, empatado com
a `Ameaça`** — porque o fator de dano dos dois é o mesmo `0,25`.

> ⚠ **Então a frase do item `17` — *"ele não é uma `Ameaça` com outro nome"* — está errada no eixo do
> DANO.** *Ele é exatamente isso. O que separa os dois é a VIDA: `55` contra `165` no nv20, e oito
> corpos contra um.*

---

# `4` · Os papéis que pagam em vida NÃO são neutros num enxame

## A trava que define o `Capanga`

> ***"o `Capanga` cai num golpe de um jogador"*** — `o-capanga-contra-os-outros-sistemas.md`

**A vida dele não é fator da vida do chefe: é `dano do grupo ÷ 4`, que é exatamente o que UM jogador
entrega numa rodada.** *No nv20 são `55` contra `55`.*

> ### Então `vida × m` com `m > 1,0` quer dizer uma coisa só: ele para de cair num golpe.

| papel | `vida ×` | vida de `1` | golpes pra cair | a trava |
|---|---|---|---|---|
| **`Brutamontes`** | `1,200` | `66,0` | **`1,20`** | ⚠ **QUEBRA** |
| `Guardião` | `0,800` | `44,0` | `0,80` | inteira |
| `Artilheiro` | `0,857` | `47,1` | `0,86` | inteira |
| `Emboscador` | `0,863` | `47,5` | `0,86` | inteira |
| `Controlador` *(forma `B`, por corpo)* | `0,500` | `27,5` | `0,50` | inteira |
| `Apoio` | `1,000` | `55,0` | `1,00` | inteira |

## E a luta inteira, com fogo concentrado

*O modelo reproduz o número publicado em `4` de `4` níveis — razão **e** rodadas.*

| papel | `vida ×` | dano do enxame | razão vs chefe | rodadas | **desvio** |
|---|---|---|---|---|---|
| *— sem papel —* | `1,000` | `444` | `1,01` | `2` | — |
| **`Brutamontes`** | `1,200` | `555` | **`1,26`** | `3` | **`+25,0%`** |
| **`Guardião`** | `0,800` | `407` | `0,92` | `2` | **`−8,3%`** |
| `Artilheiro` | `0,857` | `444` | `1,01` | `2` | `0,0%` |
| `Emboscador` | `0,863` | `444` | `1,01` | `2` | `0,0%` |
| **`Controlador`** *(por corpo)* | `0,500` | `296` | `0,67` | `1` | **`−33,3%`** |
| `Apoio` | `1,000` | `444` | `1,01` | `2` | `0,0%` |

> ### O invariante dos seis é `produto 1,000`. Num corpo único ele fecha. Num enxame de `8`, não.
> **Porque a vida entra DUAS vezes: uma no corpo, e outra na DURAÇÃO.** *E duração multiplica tudo o
> que o enxame entrega.*

**E o desvio não é contínuo, é DEGRAU** — o `Artilheiro` a `0,857` e o `Emboscador` a `0,863` custam
zero, porque o pool ainda dura as mesmas duas rodadas. *O `Guardião` a `0,800` cruza a linha.*

## E pagar em CORPOS não resolve — a moeda é grossa demais

| corpos | vs os `8` | dano do enxame | razão | vs sem papel | rodadas |
|---|---|---|---|---|---|
| `6` | `−25,0%` | `296` | `0,67` | `−33,3%` | `2` |
| `7` | `−12,5%` | `370` | `0,84` | `−16,7%` | `2` |
| **`8`** | `0,0%` | `444` | `1,01` | `0,0%` | `2` |
| `9` | `+12,5%` | `555` | `1,26` | **`+25,0%`** | `3` |
| `10` | `+25,0%` | `666` | `1,51` | `+50,0%` | `3` |

> **UM corpo a mais é `+12,5%` de corpos e `+25,0%` de encontro** — a moeda dobra no caminho, pela
> mesma razão que a vida dobra.
> **E os seis papéis pedem ajustes de `13,7%` a `50,0%`. O menor degrau que corpos sabe fazer é `25,0%`.**

---

# `5` · O `Controlador` no esquadrão — `ações` de quem?

**A forma `B` preça assim:** *negar `1` ação do grupo vale `1` ação DELE, então ele ganha
`(1 + 1/ações)` e paga `vida × 1/(1 + 1/ações)`.*

**A escada publica `ações = 1` pro `Capanga`. Mas isso é por CORPO, e ele vem em `8`.**

| a leitura | `ações` | ganha | paga vida | produto | dano do enxame | razão |
|---|---|---|---|---|---|---|
| **por CORPO** — `ações = 1` | `1` | `2,000×` | `× 0,500` | `1,000` | `296` | **`0,67`** |
| **por ESQUADRÃO** — `8` corpos | `8` | `1,125×` | `× 0,889` | `1,000` | `444` | **`1,01`** |

> **As duas fecham em `1,000` no invariante, e as duas negam a MESMA `1` ação do grupo.**
> ### O que muda é quanto isso vale: `1` de `1`, ou `1` de `8`.

---

# ⚠ E uma nota de método que vale pro projeto inteiro

**A `TABELA.md` imprime a vida do `Capanga` ARREDONDADA** — `79` no nv30, onde a fórmula dá `78,75`.

*Rodando o sim com o número impresso, o nv30 inventa uma TERCEIRA rodada: sobram `2` pontos de pool,
e `2` pontos mantêm um corpo vivo.* **A razão sai `1,17×` em vez de `1,00×` — `17%` de erro vindo de
arredondamento de impressão.**

> ### ⟹ Em enxame, o sim tem de ler a FÓRMULA (`dano do grupo ÷ 4`), nunca o número impresso.
> *Num corpo único isso não morde, porque não existe divisão por vida de corpo.*

---

# O que precisa de MARTELO, e o que é só conserto

## Conserto — não é decisão

| # | o quê |
|---|---|
| `1` | a linha de fatia do `Capanga` na `a-escada-com-numero.md`: `32/30/30/30` → **`22/23/23/23`** |
| `2` | a tabela de fator do TOPO da escada está morta e contradiz a fechada. **Marcar como morta ou apagar** |
| `3` | o item `17` da `A-FILA.md` cita o fator morto (`0,33`) e conclui o oposto do medido |
| `4` | a nota de método do arredondamento, pra quem for rodar sim de enxame |

## Martelo — e os três estão com o número calculado

**Estão na seção final. Custo zero de conta: só falta escolher.**

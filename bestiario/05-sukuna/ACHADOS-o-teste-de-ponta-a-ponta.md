# O que o teste de ponta a ponta achou — `4` contradições

*10/09/2026. Todas saem de `montar-o-sukuna.py`; a saída está em `SAIDA-o-sukuna.txt`.*

> ## ✅ ATUALIZADO em 10/09 — dois destes já fecharam
> **O achado `1` fechou** *(o `Controlador` virou forma `B`, paga em vida, e as CINCO categorias caem
> na banda de `21%`–`28%`)* **e o achado `4` fechou de graça** *(a `Recarga` é sempre em área)*.
> **E o "não medido" do `Capanga` no fim do arquivo foi medido** — `fila/MEDIDA-o-capanga.md`.
>
> ⚠ **O `montar-o-sukuna.py` foi atualizado junto:** *a varredura dele agora inclui o `Capanga`, lê o
> `Controlador` da forma `B`, e a banda vem do dono novo (`fila/DECIDIDO-o-capanga.md` §1).*
> **Os números do Sukuna não mudaram** — vida `1131`, `o golpe` `4d10 + 23`, `6` ações.

> **O item `7` da fila era "refazer o Sukuna, é o teste de que a máquina funciona".**
> **A máquina funciona — ela preencheu o bloco inteiro sem inventar um número.**
> **E ela achou `4` coisas que não fechavam, e nenhuma delas dava pra ver sem rodar as três tabelas
> juntas.** *Duas mexem em número publicado.*

| # | o achado | tamanho | mexe onde |
|---|---|---|---|
| ~~**`1`**~~ | ✅ **FECHADO** — o `Controlador` virou forma `B` e paga em VIDA. **`o golpe` não se move mais em papel nenhum**, e as CINCO categorias caem na banda | — | `papel/DECIDIDO-o-controlador-por-categoria.md` |
| **`2`** | no nv20 as derivadas comem **todos** os marcos de atributo | médio | peça 26 §3.2 — é aviso, não conserto |
| **`3`** | **área a preço fixo não reparte a cota** — `1,62×` | **o maior** | peça 26 §6.5 · `A-FILA.md` |
| **`4`** | o §4.4 não sabe escrever uma `Recarga` em alvo único | médio | peça 26 §4.4 |

---

# `1` · O `Controlador` fura a banda, e o motivo é de ORDEM

## O que a conta diz

| categoria | tem `Intervenção`? | fatia sem papel | **com `Controlador`** | na banda de `20%`–`32%`? |
|---|---|---|---|---|
| `Ameaça` | não | `22,7%` | **`15,1%`** | **NÃO** — `4,9` pontos abaixo |
| `Desastre` | sim | `27,7%` | **`18,5%`** | **NÃO** — `1,5` abaixo |
| `Catástrofe` | sim | `24,9%` | **`16,6%`** | **NÃO** — `3,4` abaixo |
| `Calamidade` | sim | `27,7%` | **`18,5%`** | **NÃO** — `1,5` abaixo |

*Nível 20. O `Capanga` ficou **fora da varredura** — a tabela dele tem outro formato de coluna e o
script não lê. **Não é "passou": é não medido.***

## Por que ninguém viu

**Os dois números foram fechados no mesmo dia, e o segundo nunca voltou pro primeiro.**

| | quando | o que fez |
|---|---|---|
| `medir-a-fila-barata.py` | **08:09 de 10/09** | mediu o `Controlador` em `48,7` de golpe e fechou a banda em `20%` |
| `medir-a-intervencao.py` | **08:28 de 10/09** | pôs o fator `× 0,923` no dano de quem tem `Intervenção` |

**`73 × 0,667` = `48,7` → `20,0%`.** *A banda foi calibrada exatamente nesse número.*
**`73 × 0,923 × 0,667` = `44,9` → `18,5%`.** *O `0,923` entrou dezenove minutos depois.*

> ### `32% × 0,923 × 0,667` não foi conta que alguém rodou.

## E tem uma coisa pior, que o `0,923` não causou

**A `Ameaça` com `Controlador` dá `15,1%`, e ela NÃO tem `Intervenção`** — nenhum `0,923` encostou
nela. *`22,7% × 0,667` = `15,1%`.*

> **A `MEDIDA-a-fila-barata` mediu o `Controlador` SÓ no `Desastre`.** *A `Ameaça` está `4,9` pontos
> abaixo do piso desde antes do fator existir.*

## As saídas, com o trade-off calculado

| # | a saída | o que ela custa |
|---|---|---|
| **A** | **a banda vira `15%`–`32%`** | ela deixa de vigiar o piso. *Mas a banda **foi feita pra vigiar o topo** — a própria escada escreve que "o topo dela era a `Dupla`". O piso nunca foi o trabalho dela* |
| **B** | **o `Controlador` corta menos** — `1/4` em vez de `1/3` | a `MEDIDA-a-fila-barata` já calculou: `o golpe` fica em `22,5%`, dentro. **Mas com o `0,923` isso vira `20,8%`, e a `Ameaça` fica em `17,0%` — ainda fora** |
| **C** | **o corte do `Controlador` sai POR CATEGORIA**, como já é o do `Emboscador` | é a única que fecha nas quatro. *E não custa bookkeeping novo: a escada **já é** uma tabela por categoria* |
| **D** | **o `Controlador` não existe em categoria de `1` ação** | é a `§5` item `4` da `A-TABELA-dos-seis-papeis`, que já registrou essa pendência. **Resolve a `Ameaça`, não resolve as outras três** |

> **Recomendação: `C`.** *O precedente é interno — o `Emboscador` já tem valor por categoria pelo mesmo
> motivo (`1` ataque de `6` é menos que `1` de `3`), e a razão aqui é a mesma: `1` ação negada de `6`
> vale menos que `1` de `3`.*

---

# `2` · No nível 20 as três derivadas comem TODOS os marcos de atributo

## A conta

| | |
|---|---|
| o orçamento no nv20 | **`13`** — `9` na criação (teto `3`) + `4` marcos (nv `6`, `10`, `14`, `18`) |
| a maestria no nv20 | **`3`** — base `1` + os marcos de nv `10` e `18` |
| Defesa `18` = `10 + Destreza + 3` | ⟹ **Destreza `5`** — custa `3` na criação + **`2` marcos** |
| acerto `+8` = `atributo + 3` | ⟹ **atributo da técnica `5`** — custa `3` + **`2` marcos** |

> ### As duas obrigadas comem `10` dos `13` pontos e **`4` dos `4` marcos**.
> **Sobram `3` pontos de criação pra os outros três atributos, e ZERO marco.**

**O §3.2 escreve:** *"Os nove pontos compram cor, e não tamanho."*
**No nv20 eles compram `3` de `13`.** *A frase é verdadeira e pequena.*

## Não é erro — é aperto, e ele tem um jeito honesto de sair

**A peça 1 §6 salva o caso:** *o TR `Físico` usa **Força ou Destreza**, declarado na criação e travado.*
**Então um chefe de Força `1` põe o `Físico` na Destreza `5` que a Defesa já obrigou** — e o `Físico`
sai `+8` em vez de `+1`.

*Sem essa cláusula, todo chefe do sistema teria `+1` no TR mais rolado da mesa.*

## E o que fica de recado

> **Se o mestre quiser um chefe que resista a veneno E a controle mental E seja forte, no nv20 ele não
> tem orçamento.** *Ele escolhe um.*

**Isso não pede conserto — pede uma linha escrita no capítulo**, porque o mestre que montar sozinho vai
bater nisso e achar que errou a conta. *No nv30 folga um marco: `16` de orçamento contra `12` conscritos.*

---

# `3` · ÁREA A PREÇO FIXO NÃO REPARTE A COTA — e é o achado maior

## As duas frases, e elas se contradizem

**A peça 26 §6.5, na lista "as que saem de graça":**

> *"Golpe ou feitiço em área. A cota é o que chega ao GRUPO, e não o que chega a cada um —* **área
> reparte a cota, e não multiplica ela.**"

**E o manual, na abertura das Melhorias (`manual/gerador/partD.js`):**

> *"O preço de cada uma depende da Classe do feitiço em que ela entra:* **Leve custa metade da
> Classe**, *Média custa a Classe inteiro, Pesada custa Classe e meio."*

**E a tabela de Formas (`partC.js`) confirma:** `Explosão`, `Cone` e `Linha` custam **`Leve`** — os
três, o mesmo. *Numa `Classe 3` são `2` pontos.*

> ### `2` pontos de preço fixo não repartem nada.

## A conta, na `Teia de Aranha` do Sukuna

| | |
|---|---|
| o orçamento da ação | `10,0` pontos |
| área (`Leve`) `−2` · `Derrubado` (`Leve`) `−2` | sobram `6` → **`6d8` = `27` por alvo** |
| a área pega | **`2,70` pessoas** — peça 26 §4.6, a mesma leitura que o §6.5 usa |
| **o que chega ao grupo** | `27 × 2,70` = **`73`** |
| a cota de uma ação | **`45`** |
| **a razão** | **`1,62×`** |

**Pra obedecer o §6.5, a ação em área tinha de entregar `17` por alvo — `3,7` pontos.**
**O Fundamento entrega `27`.** *A régua e a máquina discordam por `1,62×`.*

## E isso bate exatamente na pergunta que a fila declarou respondida

**A `A-FILA.md` abre com isto:**

> *Pergunta do Mizuki: "e se for em área?"*
> *Resposta: "**área reparte a cota, e não multiplica ela**" — e o próprio Fundamento já cobra por área
> em ponto de feitiço.*

> ### As duas metades da resposta são as duas metades da contradição.
> **O Fundamento cobra por área — a preço FIXO. O §6.5 manda repartir.** *Cobrar não é repartir.*

## Por que isso não é bug do lado do JOGADOR

**Do lado dele o preço fixo se paga:** *ele age uma vez por rodada, e uma área que pega `2,70` pessoas
é o que compra o turno dele de volta.* **A área é o prêmio de ter uma ação só.**

**Do lado do inimigo não:** *ele já age `3`, `5` ou `6` vezes.* **Preço fixo de área num bloco de `6`
ações multiplica a cota seis vezes, e não uma.**

## As saídas

| # | a saída | o que ela custa |
|---|---|---|
| **A** | **o inimigo divide os dados da ação em área pelos alvos que ela pega** | é o §6.5 ao pé da letra. **Custa uma regra que o jogador não tem** — e o §6.5 já é o lugar onde as duas mesas divergem de propósito |
| **B** | **área custa `Pesada` no inimigo, e não `Leve`** | numa `Classe 3` sobe de `2` pra `5`. *`5d8` = `22,5` por alvo → `61` no grupo → **`1,35×`**. **Melhora e não fecha*** |
| **C** | **a cota do inimigo passa a ser "por alvo" e não "por grupo"** | derruba o §4.6, que é a métrica validada contra o d20 de 2014 e o PF2e. **Caro** |
| **D** | **declarar e liberar**, no molde das "duas trocas ruins" | *"o mestre mede, mostra e escolhe"*. **Mas aqui a troca é BOA — área é o melhor negócio da ficha do inimigo, e declarar isso é declarar um dominante** |

> **Recomendação: `A`.** *É a única que obedece a frase que já está publicada, e o §6.5 existe
> justamente pra dizer onde o inimigo cobra diferente do jogador.*
>
> ⚠ **E ela tem um efeito colateral bom:** *a `Chama Divina` do Sukuna já está montada assim — `271` da
> rodada repartido em `3` alvos dá `90` cada. **Se área reparte, a `Recarga` e a área usam a mesma
> conta**, e o achado `4` se resolve de graça.*

---

# `4` · O §4.4 não sabe escrever uma `Recarga` em alvo único

## A regra

> *"O golpe é `N` dados mais um fixo, **com metade do alvo em dado**. (…) com no máximo **oito** dados
> na mão."* — peça 26 §4.4

## A parede

**A `Recarga` come as `Ações Múltiplas` da rodada e entrega `~1,0×` o turno cheio** — `DECIDIDO-a-recarga.md`.
*No Sukuna o turno cheio é `271`.*

| o alvo | a metade em dado pede | o maior punhado possível | fecha? |
|---|---|---|---|
| `271` — em `1` alvo | `136` em dado | **`8d12` = `52`** | **NÃO.** A melhor montagem é `8d12 + 219`, e só `19%` disso é dado |
| `136` — em `2` alvos | `68` | `52` | não — `8d12 + 84`, `38%` |
| **`90`** — em `3` alvos | `45` | `52` | **sim** — **`8d10 + 46`**, `49%` |
| `68` — em `4` alvos | `34` | `52` | sim — `6d10 + 35`, `49%` |

> ### O teto de `8` dados é o que cria a parede, e ele NÃO é cosmético.
> *O próprio §4.4 explica por que ele existe:* **"sem ele o otimizador troca `5d8 + 26` por `10d4 + 24`:
> fecha melhor na conta e é pior na mesa."**

## E a saída já estava escrita — no canon, não na regra

**O voto vinculante da `Chama Divina`, cap. 259 p.2-5:** *ela é **proibida** de pegar vários oponentes
ao mesmo tempo, a não ser dentro do domínio.*

> **Ou seja: a ficção do Sukuna proíbe exatamente o caso que a regra não sabe escrever.**
> *Fora do domínio ela é alvo único e vira `8d12 + 219`, que é feio. Dentro, ela reparte e vira
> `8d10 + 46`, que fecha.*

**A saída de regra, então, é uma linha:** *a `Recarga` é sempre em ÁREA.* **É o que o campo mede** — o
`Fire Breath` do dragão é um cone, e a `DECIDIDO-a-recarga` já concluiu que **"o ganho dela não é
tamanho, é ÁREA"**. *O que faltava era escrever que isso é obrigatório e não recomendado.*

---

# O que este teste NÃO achou, e é bom saber

| | |
|---|---|
| **o eixo do `tamanho`** | o Sukuna é `Médio`, o único degrau neutro. **`Grande`, `Imenso` e `Colossal` continuam sem bloco de exemplo** |
| ~~**o `Capanga` na varredura da banda**~~ | ✅ **MEDIDO em 10/09** — `fila/MEDIDA-o-capanga.md`. *Ele está DENTRO da banda em `4` de `4` níveis. E ele derrubou o topo `32%` dela, que era ele mesmo com o fator morto* |
| **o `papel` `Apoio`** | precisa de outro bloco pra receber, e este teste tem um bloco só |
| **as duas `Intervenções` que mudam o campo** | elas não têm número, por decisão de 10/09. **Então elas não podem ser conferidas — e isso é o desenho, não uma falha** |

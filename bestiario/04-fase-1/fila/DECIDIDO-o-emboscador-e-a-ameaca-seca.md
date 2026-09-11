# DECIDIDO — os itens `20` e `21`, os dois nascidos de montar as fichas de teste

*10/09/2026. **Conta em `medir-o-bicho-de-nivel-baixo.py` e em `06-playtest/montar-as-tres-fichas.py`.***

> ## Os dois fecharam por medição, e o `20` fechou CORRIGINDO o que eu tinha publicado.

---

# § 1 · ITEM `20` — ⚠ o furo era do meu script. O buraco real é de LEGIBILIDADE

## O que eu publiquei, e está errado

**Eu escrevi que o `Emboscador` num corpo de `1` ação furava o invariante em `27,7%`.** *Não fura.*

**A `papel/A-TABELA-dos-seis-papeis.md` §6 já tinha uma tabela POR CATEGORIA, e ela fecha em todas:**

| categoria | ações | ganho | paga vida | invariante |
|---|---|---|---|---|
| `Ameaça` | `1` | `1,476×` | `0,677×` | **`0,999×`** |
| `Desastre` | `3` | `1,159×` | `0,863×` | `1,000×` |
| `Catástrofe` | `5` | `1,095×` | `0,913×` | `1,000×` |
| `Calamidade` | `6` | `1,079×` | `0,927×` | `1,000×` |

***Eu apliquei o `0,863` do `Desastre` num corpo de uma ação.*** **O erro foi do script, não do desenho.**

## ✅ Mas duas coisas de verdade saíram, e as duas já estão consertadas

| # | o buraco | o conserto |
|---|---|---|
| **`1`** | **a tabela do §6 não tinha linha de `Capanga`** — ela foi escrita antes de o `Capanga` tomar papel *(item `17`, no MESMO dia)* | ✅ **linha adicionada.** *Ele tem `1` ação ⟹ é a linha da `Ameaça`: `1,476×` / `× 0,677`* |
| **`2`** | ⚠ **o resumo do §4 e o `RASCUNHO-5` imprimiam SÓ o `0,863`**, com um *"(varia por categoria)"* em itálico do lado | ✅ **os dois passaram a imprimir as quatro linhas** |

> ### O `Emboscador` é o ÚNICO dos seis cujo pagamento muda por categoria.
> **Publicar um número só dele, com a ressalva em itálico, é o que me derrubou** — e derrubaria
> qualquer mestre montando uma ficha de `Capanga`. *Um número certo no lugar errado engana igual a um
> número errado.*

> ### ⚠ E o valor do `Capanga` importa: a vida do Kama-itachi caiu de `19` pra `15`.
> *`22 × 0,677` e não `22 × 0,863`.* **E em troca ele tem vantagem em TODA rodada, porque `1` ataque de
> `1` é todo ataque dele.** *`06-playtest/FICHAS-teste-nv7-oni.md` já está corrigida.*

---

# § 2 · ITEM `21` — a `Ameaça` seca NÃO é defeito. Falta uma LINHA, não uma mecânica

**O fato:** *`golpe ÷ 4,5` dá menos que os `3` pontos da `Classe 1` do nv`2` ao nv`8` — `7` níveis em
que a `Ameaça` não monta feitiço nenhum.*

## A pergunta certa era: quantos BOTÕES o bicho de nível baixo do campo tem?

| corpo | amostra | mediana de entradas | **com `1` entrada ou menos** |
|---|---|---|---|
| D&D 2024, `CR 0–1` | `135` | `2,0` | **`25,2%`** |
| D&D 2014, `CR 0–1` | `141` | `3,0` | `14,2%` |
| Draw Steel, nv`1–2` | `181` | `2,0` | **`30,4%`** |
| **Draw Steel, os `minions`** | `116` | `2,0` *(média `1,60`)* | ### **`45,7%`** |

> ### Um bicho de nível baixo com UM botão é normal no campo — `14%` a `30%` deles.
> **E entre os `minions`, que são o análogo do `Capanga`, é quase METADE.** *O nosso `Capanga` com uma
> entrada não é defeito nenhum: é o formato.*

## ⚠ Mas a mediana é `2`, e a segunda entrada NÃO é um ataque

*Quebrando as entradas do `CR 0–1` em passivas e ações:*

| | traços passivos | ações |
|---|---|---|
| D&D 2024 `CR 0–1` | mediana **`1,0`** | mediana **`1,0`** |
| D&D 2014 `CR 0–1` | mediana **`1,0`** | mediana **`1,0`** |

**Os traços mais comuns nas duas edições:** *`Pack Tactics` (`14`× nas duas) · `Keen Smell` · `Water
Breathing` · `Amphibious` · `Spider Climb` · `False Appearance` · `Flyby` · `Swarm`.*

> ### NENHUM deles é habilidade de dano. São sentido, movimento, aparência e "eles vêm em grupo".
> **O bicho de `CR 0–1` do campo é `1` ação + `1` traço qualitativo.** *E o nosso bloco já tem as duas
> coisas: o `Deslocamento` carrega o tipo de movimento e a seção `Traços` carrega o resto.*

## ⟹ A DECISÃO: o piso `seco` fica. O que entra é uma linha no capítulo

> ### **A `Ameaça` seca não é um bloco vazio.** Ela é `1` ação + `1` traço qualitativo — que é exatamente o que o campo imprime num bicho desse tamanho, e o traço não custa orçamento nenhum.

| # | o que muda |
|---|---|
| **`1`** | ✅ **o piso `seco` NÃO desce.** *O campo concorda: `1` ação é a mediana no `CR 0–1`* |
| **`2`** | ✅ **entra a linha no capítulo** — *"um bloco `seco` recebe `1` traço qualitativo, e ele é de graça"* |
| **`3`** | ✅ **e o `Capanga` fica como está** — `45,7%` dos minions do campo têm `1` entrada ou menos |
| **`4`** | ⚠ **e o alerta do `ESTADO` continua valendo, só que no OUTRO ponto da escada** — *"inimigo com um botão só"* é problema no CHEFE, não no bicho de nível baixo. *O Arcanaloth reclamado é `CR 12`* |

### O texto da linha

> #### O bloco seco
>
> **Quando `o golpe` de uma ação dividido por `4,5` dá menos que os `3` pontos da `Classe 1`, aquela
> ação não monta feitiço: ela bate, e o dano sai como o §4.4 manda.** *É o caso de toda `Ameaça` do
> nível `2` ao `8`, e de todo `Capanga` até o nível `8`.*
>
> **Isso não deixa o bloco vazio.** *Dê a ele `1` traço qualitativo — um sentido, um jeito de se mover,
> uma aparência que engana, ou o motivo de eles andarem em bando.* **O traço não custa orçamento, e é
> exatamente o que o campo imprime:** *num bicho de `CR 0–1` do D&D a mediana é `1` ação e `1` traço, e
> os mais comuns são `Pack Tactics`, `Keen Smell`, `Amphibious` e `False Appearance`.*
>
> ⚠ **O "inimigo com um botão só" que o campo reclama é o CHEFE, não este.** *A ficha reclamada é de
> `CR 12`.*

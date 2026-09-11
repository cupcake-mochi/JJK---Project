# `Pontos por ação` — a tabela refeita na escada nova

*10/09/2026. Conta em `refazer-pontos-por-acao.py`, saída em `SAIDA-pontos-por-acao.txt`.*
**Item `3` da fila — FEITO.**

> ## ⚠ REFEITA em 11/09/2026, pela rota `B` — e `9` células andaram `0,1`
> *Esta tabela tinha sido calculada pela rota `A`: **média do golpe CRU × `0,923`**.* **A rota
> validada é a `B` — o fator entra no dano de RODADA, antes de escolher o dado, e o que se divide
> por `4,5` é a média do golpe que a ficha IMPRIME.** *Medida em `fila/medir-a-rota-do-orcamento.py`,
> martelo em `fila/DECIDIDO-as-tres-respostas-da-passada.md` §2.*
>
> ### ⟹ A maior ação do sistema é `14,9` pontos, e não `15,0`.
> **E o `refazer-pontos-por-acao.py` agora CONFERE as `35` células contra o §6.5 publicado, e morre
> se divergirem.** *Enquanto ele passar, o Bestiário e a peça 26 contam a mesma coisa.*

> **A regra é do §6.5 e não mudou:** *"o orçamento de feitiço de uma ação é **o golpe dela dividido
> por `4,5`**"*. **O que mudou foi a escada** (as categorias velhas morreram) **e o golpe** (a
> recalibração `× 0,923` de quem tem `Intervenção`).

---

## A tabela

*`seco` = abaixo de `3` pontos. Ali ele **não monta feitiço**: ele bate, e o golpe sai como o §4.4 manda.*

| nível | `Capanga` | `Ameaça` | `Desastre` | `Catástrofe` | `Calamidade` |
|---|---|---|---|---|---|
| `2` | seco | seco | seco | seco | seco |
| `5` | seco | seco | seco | seco | seco |
| `10` | `4,2` | `4,2` | **`5,1`** | `4,6` | **`5,1`** |
| `15` | `6,2` | `6,2` | **`7,6`** | `6,9` | **`7,7`** |
| `20` | `8,2` | `8,2` | **`10,1`** | `9,1` | **`10,1`** |
| `25` | `10,2` | `10,2` | **`12,4`** | `11,3` | **`12,4`** |
| `30` | `12,2` | `12,2` | **`14,9`** | `13,4` | **`14,9`** |

*As colunas em negrito já levam o `× 0,923` da `Intervenção`.*

## O efeito do fator, no `Desastre` nv30

| | dano de rodada | o golpe impresso | pontos |
|---|---|---|---|
| sem o fator | `219` | `8d8 + 37` *(média `73,0`)* | `16,2` |
| **com o fator** | **`202`** | **`6d10 + 34`** *(média `67,0`)* | **`14,9`** |

*O fator entra no dano de RODADA — `⌈219 × 0,923⌉` = `202` —, e o dado se escolhe depois. É essa
ordem que separa a rota `B` da `A`.*

---

## ⚠ O que mudou em relação ao §6.5 publicado — e tem uma coisa grande

**O §6.5, na escada velha, nível 30:** `Ronda 12,2` · **`Dupla 24,2`** · `Alcateia 16,2` · `Calamidade 14,6`

**A escada nova, nível 30:** `Capanga 12,2` · `Ameaça 12,2` · `Desastre 14,9` · `Catástrofe 13,4` · `Calamidade 14,9`

> ### A `Dupla` era o pico — `24,2` pontos, contra o teto de `24` do jogador. Ela MORREU.
> **A escada nova topa em `14,9`.** *Isso é consequência direta de ter matado o degrau que levava o
> dobro do orçamento pela mesma porta — e é a decisão certa. Mas o efeito colateral é real:*
>
> **A maior ação de inimigo do sistema agora é `62%` do maior feitiço que um jogador monta no mesmo nível.**

**Isso não é desequilíbrio** — *o inimigo compensa em QUANTIDADE: ele age `3`, `5` ou `6` vezes por
rodada, e o jogador age uma.* **Mas muda o que cabe numa ação dele.**

### O que isso significa na prática, e é a resposta útil pro mestre

*Numa ação de `14,9` pontos, de um `Desastre` nv30:*

| se ele comprar | custa | sobra pra dado |
|---|---|---|
| uma condição **`Leve`** | `4` pontos | `10,9` → `~10d8` |
| uma condição **`Média`** | `7` | `7,9` |
| uma condição **`Pesada`** | `11` | **`3,9`** |

> **Uma ação de inimigo aguenta uma condição `Pesada`, mas ela vira quase só condição.** *É a mesma
> troca que o jogador faz — e é exatamente o que o Mizuki tinha levantado: **"um feitiço em área vai
> ter menos dados para poder comprar condição"**.*

---

## E fica registrado o que NÃO foi feito aqui

**Esta tabela vive em `Bestiario/`. O §6.5 no repositório continua com a tabela velha.**
*Trocar lá é o item `4` da fila — e ele vai junto com tirar a frase **"nunca por cima"**, que
contradiz a decisão de 10/09 sobre a `Intervenção`.*

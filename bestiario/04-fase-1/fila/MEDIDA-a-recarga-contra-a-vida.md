# A `Recarga` contra a vida de quem ela acerta — MEDIDA

*14/09/2026. Pedido do Mizuki:* *"Sukuna Nv30 está para enfrentar um grupo de nv30, pegue uma média de vida correspondente em relação a valores diferentes de constituição pra cada classe e balanceie esse ataque para uma correspondencia que acerte bem. Sempre pesquisar e validar, antes de responder, se drawn steel tiver resposta para isso, pathing finder, é bom tbm olhar neles".*

**Script:** `medir-a-recarga-contra-a-vida.py` · **saída:** `SAIDA-recarga-contra-a-vida.txt`. *Corpora já baixados: SRD 5.2, Pathfinder 2e (Archives of Nethys) e o repositório do Draw Steel — ver `dados-recarga-area/COMO-RODAR.md`.*

## A régua de cada sistema — dano por alvo na falha ÷ a vida média de um personagem do nível

| sistema | o que foi medido | n | mediana | quartis |
|---|---|---|---|---|
| **D&D 2024** | áreas com `Recharge`, nível de desafio `17+`, contra personagem nível `20` | `14` | **`42%`** | `39%` a `46%` |
| **Pathfinder 2e** | áreas com *"1d4 rounds"*, nível `17+`, contra personagem do mesmo nível | `139` | **`29%`** | `27%` a `30%` |
| **Pathfinder 2e** | as mesmas, com o chefe `2` níveis acima do grupo | `139` | **`32%`** | `30%` a `33%` |
| **Draw Steel** | `Villain Action` em área, resultado `12-16`, nível `8+` | `11` | **`15%`** | `12%` a `15%` |

**Suposições que não saem de documento:** *Constituição `+2`, e `+3` do 8º nível no D&D; Constituição como atributo secundário no Pathfinder (`+2`/`+3`/`+4`); média simples das classes e dos kits.* *O Pathfinder deixou `157` áreas sem ler, porque o dano não vinha na frase "deals XdY"; as `14` do D&D e as `11` do Draw Steel foram conferidas uma a uma.*

## O Projeto-M no nível 30

**Os cinco Caminhos × Constituição `0` a `6`, pela peça 1 §5.1: média `243`, de `122` (Evocador ou Emanador de Constituição `0`) a `395` (Bastião de Constituição `6`).** *É o mesmo `243` que o Bestiário usa como vida de personagem.*

| régua | a `Recarga` por alvo, no nível 30 |
|---|---|
| D&D 2024 | **`101`** (quartis `95` a `112`) |
| Pathfinder 2e, chefe | `78` (`73` a `79`) |
| Pathfinder 2e | `70` (`67` a `73`) |
| Draw Steel | `36` (`29` a `36`) |
| **o turno cheio em cada alvo** *(decisão de 14/09 antes da medida)* | **`402`** — `165%` da vida, `4 ×` a régua do D&D |

## O que o número conversa com o resto

- **`101` é `1,5 ×` o golpe do `Desastre` e da `Calamidade` do nível 30** (`67`) — *o mesmo `1,50 ×` que o Pathfinder dá para área de uso limitado, na `FONTE-a-area-no-campo.md`.*
- **Com o D&D contando a área como `2` alvos numa mesa de `4`, `101 × 2 = 202`, que é o turno cheio do `Desastre`.** *Na `Calamidade`, mesa de `8`, `101 × 4 = 404`, o turno dela.* **A rodada de `Recarga` entrega o mesmo total da rodada comum, e o multiplicador de fator do método do D&D dá `1,00`.**
- **`101` fecha a regra do golpe em dado:** `8d12 + 49`, com `51%` em dado. *O turno cheio (`402`) não fecha: o maior punhado é `8d12`, `13%` de `402`.*

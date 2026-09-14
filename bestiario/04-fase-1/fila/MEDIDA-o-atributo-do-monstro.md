# O atributo do monstro contra o do personagem — MEDIDA

*14/09/2026. Pergunta do Mizuki:* *"Inimigos em DnD normalmente tem mais atributos que player, tem alguma metrica pra isso? vale apena a gente usar? os outros sistemas fazem isso tambem?"*

**Script:** `medir-o-atributo-do-monstro.py` · **saída:** `SAIDA-o-atributo-do-monstro.txt`.

## A régua escrita de cada sistema

| sistema | tem régua de atributo de monstro? | o que ela diz |
|---|---|---|
| **D&D 2024** | **não** | *o Guia do Mestre de 2024 não tem tabela de estatística por nível de desafio, e desaconselha mexer em Força, Destreza e Constituição, porque isso muda ataque, dano, CA e vida* — `01-pesquisa/dmg2024-e-draw-steel.md` |
| **Pathfinder 2e** | **sim** | *a tabela `Attribute Modifier Scales` do GM Core, p. 114: o melhor atributo usa a coluna `High`* — `+4` no nível 1, `+7` no 10, `+10` no 20 · [Archives of Nethys](https://2e.aonprd.com/Rules.aspx?ID=2881) |
| **Draw Steel** | **sim** | *o maior atributo de um monstro é `1 +` o escalão; `Leader` e `Solo` ganham `+1`, com teto `+5`* — `01-pesquisa/dmg2024-e-draw-steel.md` |

## O que as fichas fazem, no mesmo nível do personagem

*O maior atributo, mediana das fichas, contra o maior atributo do personagem pela regra de jogador de cada sistema.*

| sistema | começo | meio | topo |
|---|---|---|---|
| **D&D 2024** *(331 criaturas)* | `−1` | `+1` | **`+3`** *(desafio 17–20: `+8` contra `+5`)* |
| **Pathfinder 2e** *(677 com recarga, amostra de chefe)* | `+0` | `+2` | **`+4`** *(nível 20+: `+10` contra `+6`)* |
| **Draw Steel** *(416 fichas)* | `+0` | `+0` | **`+0`** |

**O personagem de referência:** *D&D 2024 com o conjunto padrão, o antecedente e todo aumento de atributo; Pathfinder 2e com o atributo-chave `+4` e o aumento parcial acima dele; Draw Steel pelas classes do `Heroes`.*

## ⚠ Correção, levantada pelo Mizuki no mesmo dia

*"Mas os outros sistema escalam, defesa, acerto, TR, com esses atributos, olha os inimigos de DnD".* **Ele está certo sobre o D&D:** *na ficha do monstro a CA, o ataque e a CD saem do atributo mais a proficiência, como aqui.* **Quem separa o atributo do resto é só o Pathfinder 2e.**

**O que o atributo maior entrega nas fichas do D&D 2024, contra o personagem do mesmo nível sem item mágico** *(o maior atributo mais a proficiência):*

| nível | ataque do monstro | ataque do personagem | CD do monstro | CD do personagem |
|---|---|---|---|---|
| 1–4 | `+5` | `+6` | `12` | `14` |
| 5–8 | `+7` | `+8` | `14` | `16` |
| 9–12 | `+10` | `+9` | `17` | `17` |
| 13–16 | `+11` | `+10` | `18` | `18` |
| **17–20** | **`+15`** | **`+11`** | **`22`** | **`19`** |

**Até o nível 16 o monstro empata com o personagem.** *O atributo maior só abre distância no topo, e a distância de `+3` a `+4` é o que um personagem de nível 17 a 20 do D&D carrega em item mágico — arma `+3`, foco `+3` —, que o atributo dele não mostra.* **O resultado é a mesma chance dos dois lados.**

**No Projeto-M o personagem não tem esse bônus escondido:** *o acerto é atributo mais maestria (peça 1 §5), e o `+2` a mais — a Melhoria `Precisão` — se compra no feitiço, com o inimigo comprando do mesmo catálogo (peça 26 §6.5).* **Dar ao inimigo o atributo do monstro do D&D seria dar a ele o item que o personagem não tem.**

## ✅ A decisão — v0.233

***Decisão do Mizuki:*** **o chefe começa com dez pontos na criação, e não nove** — *"é um bônus que sim, faz diferença, mas calcular tanto encima dele é trabalho extra demais, é um ponto q pode ir em 5 atributos diferentes"*. **Chefe é quem carrega `Intervenção`**, *o equivalente do `Leader` e do `Solo` do Draw Steel.* **O ponto pode subir Defesa, acerto ou CD, e não entra no fator.** *Está na peça 26 §3.2.*

## Por que os dois primeiros podem, e o Projeto-M decide diferente

**No Pathfinder 2e o ataque, a CD, a CA e os Testes de Resistência da criatura saem de tabelas próprias, e não do atributo.** *O atributo alto não move nenhum deles.* **No D&D o nível de desafio é que manda, e o atributo segue a ficha.**

**No Projeto-M o atributo carrega as derivadas dos dois lados da mesa, pela mesma fórmula** — *a Defesa lê a Destreza, o acerto e a CD leem o atributo da técnica, e o Teste de Resistência é atributo mais maestria* (peça 26 §3.1). **É o desenho do Draw Steel, e é ele que prova a derivação:** *se o inimigo tivesse atributo maior, o acerto de `52%` e a falha de `35%` deixariam de ser os mesmos dos dois lados.*

# O Guia de 2024 e o Draw Steel — a máquina de inimigo dos dois

---

# PARTE 1 · Dungeon Master's Guide 2024

## O que sobrou de "criar criatura": duas páginas, e nenhum número

A seção `Creating a Creature` (capítulo 3, p. 56–57) tem duas partes: **Minor Alterations** e uma lista de traços de sabor. Nada mais.

O que ela deixa você mexer:

| pode mudar | observação |
|---|---|
| tamanho e tipo | livre |
| Inteligência, Sabedoria, Carisma | livre, salvo se for atributo de conjuração |
| Força, Destreza, Constituição | **desaconselhado** — mexe em ataque, dano, CA e PV, e isso muda o ND |
| idiomas, proficiências, perícias, sentidos | livre; sentidos não afetam o ND |
| magias | trocar por outra do mesmo nível; não trocar dano por não-dano |
| ataques | nome, sabor e **tipo** de dano |
| resistências e imunidades | pode dar uma ou duas |
| traços | da lista dele ou de outro bloco |

**E aqui está a frase que fecha o assunto**, sobre importar traços de outro bloco do Manual dos Monstros:

> *desde que você não adicione traços que alterem os Pontos de Vida da criatura, concedam PV temporários, ou mudem a quantidade de dano que ela causa.*

**Ou seja: a seção de criar criatura do Guia de 2024 proíbe explicitamente mexer nos dois números que definem um inimigo.** Não é omissão — é regra.

## Não existe tabela de estatística por ND. Existe uma tabela de armadilha

Varri o livro inteiro. **A única tabela de construção que sobrou no DM's Toolbox é a de armadilhas:**

| níveis | armadilha incômoda: CD / dano | armadilha mortal: ataque / CD / dano |
|---|---|---|
| 1–4 | `10–12` · `5 (1d10)` | `+8` · `13–15` · `11 (2d10)` |
| 5–10 | `12–14` · `11 (2d10)` | `+8` · `15–17` · `22 (4d10)` |
| 11–16 | `14–16` · `22 (4d10)` | `+8` · `17–19` · `55 (10d10)` |
| 17–20 | `16–18` · `55 (10d10)` | `+8` · `19–21` · `99 (18d10)` |

*Uma armadilha ainda tem régua de construção por nível. Um monstro não.*

## O que sobreviveu: a construção de ENCONTRO

O orçamento de encontro continua, e ficou mais simples que o de 2014 — **sem multiplicador de encontro.**

**A calibragem declarada**, que é o equivalente da linha do seu manual:

> Um único monstro é, em geral, um desafio de dificuldade **BAIXA** para um grupo de quatro personagens de nível igual ao ND dele.

### `XP Budget per Character` — multiplique pelo número de personagens

| nível | baixa | moderada | alta |
|---|---|---|---|
| 1 | `50` | `75` | `100` |
| 2 | `100` | `150` | `200` |
| 3 | `150` | `225` | `400` |
| 4 | `250` | `375` | `500` |
| 5 | `500` | `750` | `1.100` |
| 6 | `600` | `1.000` | `1.400` |
| 7 | `750` | `1.300` | `1.700` |
| 8 | `1.000` | `1.700` | `2.100` |
| 9 | `1.300` | `2.000` | `2.600` |
| 10 | `1.600` | `2.300` | `3.100` |
| 11 | `1.900` | `2.900` | `4.100` |
| 12 | `2.200` | `3.700` | `4.700` |
| 13 | `2.600` | `4.200` | `5.400` |
| 14 | `2.900` | `4.900` | `6.200` |
| 15 | `3.300` | `5.400` | `7.800` |
| 16 | `3.800` | `6.100` | `9.800` |
| 17 | `4.500` | `7.200` | `11.700` |
| 18 | `5.000` | `8.700` | `14.200` |
| 19 | `5.500` | `10.700` | `17.200` |
| 20 | `6.400` | `13.200` | `22.000` |

### A nota de solução de problemas, que é um lacaio sem o nome

> Se o encontro tiver **mais de duas criaturas por personagem**, inclua criaturas frágeis que podem ser derrotadas rápido. Especialmente importante nos níveis 1 e 2.

*E: criaturas de ND 0 devem ser usadas com parcimônia — para muitos corpos, use enxames.*

---

# PARTE 2 · Draw Steel — a máquina inteira, em três fórmulas

**O livro publica as fórmulas.** Elas estão na seção `Adjusting Monster Levels`, com um aviso: os blocos não foram feitos para serem modificados, e essas fórmulas existem para você entender como eles funcionam.

> **EV** = `((2 × nível) + 4) × modificador de organização`
> **Stamina** = `((10 × nível) + modificador de papel) × modificador de organização`
> **dano** = `(4 + nível + modificador de dano) × modificador de tier` — dividido por `2` para horda e lacaio; some o maior atributo se for golpe
>
> **Força de encontro de UM herói** = `4 + (2 × nível)`

## Modificador de organização — e ele é DUPLO

| posto | Stamina | EV e dano | razão |
|---|---|---|---|
| `Minion` | `× 0,125` | `× 0,5` | **`4,00 ×`** |
| `Horde` | `× 0,5` | `× 0,5` | `1,00 ×` |
| `Platoon` | `× 1` | `× 1` | `1,00 ×` |
| `Elite` | `× 2` | `× 2` | `1,00 ×` |
| `Leader` | `× 2` | `× 2` | `1,00 ×` |
| `Solo` | `× 5` | `× 6` | **`1,20 ×`** |

## Modificador de papel (entra na Stamina) e de dano

| papel | mod. de papel | mod. de dano |
|---|---|---|
| Brute | `+30` | `+1` |
| Defender | `+30` | `+0` |
| Ambusher | `+20` | `+1` |
| Harrier · Mount · Support | `+20` | `+0` |
| Artillery | `+10` | `+1` |
| Controller · Hexer | `+10` | `+0` |
| **Elite** | — | `+1` |
| **Leader** | `+30` | `+1` |
| **Solo** | `+30` | `+2` |

*O Elite empilha com um papel de `+1`, chegando a `+2`.*

## Modificador de tier — o resultado da rolagem

| tier | modificador |
|---|---|
| 1 (pior resultado) | `× 0,6` |
| 2 (normal) | `× 1,1` |
| 3 (melhor) | `× 1,4` |

## A régua de alvos

| a habilidade acerta | multiplique o dano por |
|---|---|
| um alvo a mais que o esperado | `× 0,8` |
| dois ou mais alvos a mais | `× 0,5` |
| um alvo a menos | `× 1,2` |

*E o esperado não é fixo: habilidades de Elite, Leader e Solo **normalmente já acertam dois alvos**.*

## Outras regras de construção

- O maior atributo de um monstro é `1 + escalão`. Leader e Solo ganham `+1` (teto `+5`), e `+1` nas potências (teto `6`).
- O dano de golpe livre é o dano do tier 1.
- **Golpe livre não rola dado** — é número fixo. Declarado: mantém o jogo rápido e evita crítico fora do turno.

## Lacaio — esquadrão com pool

- Até **oito** com o mesmo nome, agindo na mesma iniciativa.
- **Pool de Stamina = Stamina individual × quantidade.** Oito de `5` = pool de `40`.
- A cada `5` que o pool perde, **um** morre. Aos 35, 30, 25… e assim por diante.
- Um golpe único que tire o equivalente a dois ou mais leva vários de uma vez; **área só mata quem está na área**.
- Não ficam feridos, não curam, não ganham vida temporária.
- **Comprados de quatro em quatro** — o EV de lacaio já representa quatro juntos.

## Villain actions — como o Solo resolve a economia de ação

- **Exatamente três**, cada uma **uma vez por encontro**, no máximo **uma por rodada**.
- Usadas **no fim do turno de outra criatura**.
- A ordem é dramatúrgica: a 1ª é abertura, a 2ª é controle de área quando o grupo já cercou, a 3ª é o ultimate.

## Malice — o recurso do mestre

- No início do combate: Malice = média de Vitórias por herói.
- No início de cada rodada: **Malice = número de heróis + o número da rodada**.
- Cinco heróis com 3 Vitórias começam com `9`; na 2ª rodada ganham `7`, na 3ª `8`, na 4ª `9`.
- **Herói morto para de gerar Malice.**

## Construção de encontro

| passo | como |
|---|---|
| força de encontro do grupo (ES) | soma de `4 + 2 × nível` de cada herói. A cada 2 Vitórias médias, conte um herói a mais |
| orçamento | trivial `< ES − 1 herói` · fácil `< ES` · padrão `ES` a `ES + 1 herói` · difícil até `ES + 3 heróis` · extremo acima |
| teto de nível | criatura no máximo `+2` níveis acima do grupo. **Solo: no máximo `+1`** |
| respiro | de 4 a 6 Vitórias de combate antes de descansar |

### A tabela de força de encontro fecha sozinha

Rodei a fórmula contra o que o livro promete em prosa, no nível 5:

| posto | EV | ES de 1 herói | vale | o livro promete |
|---|---|---|---|---|
| `Minion` | `7` (por 4) | `14` | 8 por herói | 8 por herói |
| `Horde` | `7` | `14` | 2 por herói | 2 por herói |
| `Platoon` | `14` | `14` | 1 herói | 1 por herói |
| `Elite` | `28` | `14` | 2 heróis | 2 heróis |
| `Leader` | `28` | `14` | 2 heróis | 2 ou mais |
| `Solo` | `84` | `14` | 6 heróis | 6 heróis |

**Seis de seis.** A prosa é a fórmula.

---

# PARTE 3 · O achado que responde a `Dupla`

## O dano POR GOLPE quase não muda entre os postos

Papel Brute, tier 2 (resultado normal):

| nível | `Minion` | `Horde` | `Platoon` | `Elite` | `Solo` | `Solo` ÷ `Platoon` |
|---|---|---|---|---|---|---|
| 1 | `3` | `3` | `6` | `7` | `8` | `1,33 ×` |
| 3 | `4` | `4` | `8` | `9` | `10` | `1,25 ×` |
| 5 | `5` | `5` | `10` | `11` | `13` | `1,30 ×` |
| 7 | `7` | `7` | `13` | `14` | `15` | `1,15 ×` |
| 10 | `8` | `8` | `16` | `17` | `18` | `1,12 ×` |

**Um Solo vale SEIS heróis e bate 12% a 33% mais forte que um Platoon, que vale UM.**

## Então de onde vem a força dele

| eixo | `Platoon` nv 5 | `Solo` nv 5 | razão |
|---|---|---|---|
| vida | `80` | `400` | **`5,0 ×`** |
| dano por golpe | `10` | `13` | `1,30 ×` |
| alvos por habilidade | `1` | `2` | `2,0 ×` |
| ações fora do turno | `0` | `3` villain actions | — |
| dano por rodada, em 2 alvos | `10` | `26` | `2,6 ×` |

**A força vem da vida, dos alvos e das villain actions. Não do tamanho do golpe.**

## Lado a lado com o seu sistema

Mesma pergunta — o inimigo passa de exigir 1 pessoa para exigir 2:

| | `Ronda` → `Dupla` (seu) | `Platoon` → `Elite` (Draw Steel) |
|---|---|---|
| personagens exigidos | 1 → 2 | 1 → 2 |
| vida | `× 2,00` | `× 2,00` |
| dano por rodada | `× 2,00` | `× 2,00` |
| **dano por GOLPE** | **`× 2,00`** | **`× 1,10`** |
| por onde o dano extra chega | um golpe maior | mais alvos por habilidade |

---

# PARTE 4 · Como a comunidade recebeu

**`Draw Steel: Monsters` levou 95/100 no GamingTrend.**

| elogiado | criticado |
|---|---|
| lacaio com pool compartilhado — resolve muitos corpos sem fila de turnos | **customizar monstro é ruim**: "escalar para níveis posteriores não é realmente suportado", e ajustar um existente "não é ótimo, fora encher de vida" |
| Solo com turno duplo e villain actions | faltam tipos de criatura (limos, bicho de masmorra) |
| encontro por OBJETIVO, não só eliminação — evita que a luta vire arrastão | a orientação de mestre está no livro de Heróis, não no de Monstros |
| "monstros definidos pelo que fazem, não pela aparência" | tático pesado demais para quem gosta de sistema leve; PDF caro |

**E o próprio livro admite o buraco:** as regras completas de criação de monstro **ainda não foram publicadas**. A seção de fórmulas fecha dizendo que orientação mais robusta virá no futuro.

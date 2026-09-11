# O que estamos descartando, e o que foi medido antes de descartar

*Diagnóstico da peça 26 do repositório, feito em 08/09/2026 antes de decidir refazer.*

## Primeiro: a peça não é grande demais

Essa era a suspeita, e ela está errada.

| peça | linhas |
|---|---|
| `14-equipamento.md` | `1783` |
| `11-aptidoes-e-refino.md` | `1359` |
| `15-invocacoes.md` | `1147` |
| **`26-bestiario.md`** | **`526`** |

**Ela é uma das menores.** O problema é de forma, não de volume.

## O que a medição achou

| achado | número |
|---|---|
| **as subseções estão fora de ordem no próprio arquivo** | 4.1 · 4.2 · **4.5 · 4.6 · 4.4 · 4.3** · 4.7 |
| **duas escadas que quase nunca coincidem** | vida e dano mudam nos níveis 2·5·9·13·17·21·26; Defesa, acerto, CD e refino mudam em 6·10·14·18·22·26. **Coincidem em 2 dos 29 níveis** |
| **documentos que o mestre cruza para montar UMA ficha** | **12 peças mais o manual** |
| **`degrau de categoria` é moeda de três coisas** | resistência · o que dá vida efetiva · a Expansão de Domínio |
| **quanto do texto é história e não máquina** | 43 citações de versão no corpo; 87 de 368 linhas dentro de bloco de citação |
| **um `fator` para dois eixos** | vida e dano escalam pelo mesmo número — é a falha nº 1 do D&D reproduzida aqui |
| **nenhum eixo de papel** | todo inimigo da mesma categoria é mecanicamente idêntico. Os nove pontos de atributo "compram cor, e não tamanho" — e cor não muda como ele joga |
| **uma decisão pendurada** | o inimigo VAI contar PE (decidido na v0.220, não aplicado). Isso derruba o §6.1 e a moeda de metade do §6.5 |

## O diagnóstico

**A peça é três documentos empilhados num arquivo só:**

1. A **máquina** que o mestre usa na hora de montar inimigo.
2. O **argumento** de por que os números são aqueles.
3. O **registro** do que já esteve errado e foi consertado.

Os três são legítimos. Mas quem senta para montar um inimigo quer o primeiro, e tem que atravessar os outros dois para chegar nele.

## O sintoma que abriu tudo

A `Dupla` bate um golpe de `45%` da vida de um personagem, em todo nível, contra `23%` da `Ronda` e `30%` da `Alcateia`.

**A causa:** o dano cresce com o número de pessoas (`fator = pessoas ÷ 4`) e as ações crescem com pessoas **menos um**. A razão `pessoas ÷ (pessoas − 1)` explode embaixo — `2÷1`, `4÷3`, `6÷5`. A `Ronda` só escapa porque o piso de 1 ação a salva de dividir por zero.

**Isso é um sintoma, não a doença.** A doença é o `fator` único.

## O que sobrevive ao descarte

- A linha `Inimigos` do manual (vida e dano por faixa de nível). Ela é do manual, não da peça.
- As fórmulas derivadas das peças 1, 11 e 19 — Defesa, acerto, CD, refino, proteção.
- A regra do dado do §4.4, que traduz dano por rodada em expressão de dado.
- Tudo em `02-referencia/` e `01-pesquisa/`.

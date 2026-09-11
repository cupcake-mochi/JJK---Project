# MEDIDA — a imunidade a CONDIÇÃO, e ela é a irmã do §6.3

*Aberta pelo martelo `C` do `MEDIDA-a-resistencia-e-a-vulnerabilidade.md`.*
**Conta em `medir-a-imunidade-a-condicao.py`, saída em `SAIDA-imunidade-a-condicao.txt`.**
*Toda âncora lida do dono — peça 26, peça 19, peça 11 e o `partD.js`.*

> ## O buraco: o campo imprime imunidade a condição em `22,7%` dos blocos, e o nosso sistema não preça em lugar nenhum.
> *Varredura nas peças `19` e `26`: **zero** menções. A `19` é dona das treze condições e não fala nisso.*

---

# § 1 · A TESE — e ela não é régua nova

| | o que sobe | como se paga |
|---|---|---|
| **§6.3** · resistir a DANO | a vida efetiva | `fator × 1 ÷ (1 − fatia que ele deixa de receber)` |
| ### aqui · imune a CONDIÇÃO | ### a saída efetiva | ### `fator × 1 ÷ (1 − fatia que ele deixa de perder)` |

**É a mesma fórmula, no eixo da AÇÃO em vez do eixo do DANO.**

---

# § 2 · AS ÂNCORAS, e todas já estavam publicadas

| âncora | valor | dono |
|---|---|---|
| ações × rodadas | `3 × 3` = **`9` golpes na luta** | peça 26 §5 — *"o chefe age três vezes por rodada e a luta dura três rodadas"* |
| o acerto do inimigo | `52%` | peça 26 §6.4 |
| vantagem / desvantagem | **`±25` pontos percentuais** | peça 11 |
| quanto cada condição cobra em ação | `Lento` `½` · `Calado` `1` · `Enfeitiçado` `1` · `Atordoado` `1½` | peça 19 §2.2 |
| ### a duração | ### **`1` rodada, todas as treze** | ### `partD.js`, a Melhoria `Condição` |

⚠ **Eu tinha errado a duração na primeira rodagem** — supus que só a `Pesada` acabava cedo. *O
`partD.js` publica **"Dura uma rodada"** pra todas, e a `Pesada` ainda dá TR no fim de cada turno,
então ela pode acabar ANTES de uma rodada, nunca depois.* **Com a duração certa a tabela inteira
encolheu, e a ordem dos níveis voltou a fazer sentido.**

---

# § 3 · A RÉGUA

| condição | nível | apaga | do total | ⟹ imunidade vale | como |
|---|---|---|---|---|---|
| **`Atordoado`** | `Pesada` | `1,50` | `16,7%` | ### **`× 1,20`** | rouba `1½` ação |
| `Derrubado` | ⚠ **`Leve`** | `1,44` | `16,0%` | **`× 1,19`** | desvantagem |
| `Impedido` · `Cego` · `Amedrontado` · `Envenenado` | `Pesada` | `1,44` | `16,0%` | `× 1,19` | desvantagem |
| `Calado` · `Enfeitiçado` | `Média` | `1,00` | `11,1%` | `× 1,12` | rouba `1` ação |
| `Lento` | `Leve` | `0,50` | `5,6%` | `× 1,06` | rouba `½` ação |
| `Incapacitado` · `Agarrado` · `Desarmado` · `Surdo` | `Leve` | — | — | ### **`1,00×`** | não toca ação nem acerto dele |

> ## ⟹ A régua inteira cabe entre `1,00×` e `1,20×`.
> **Imunidade a condição é BARATA** — *compare com `1,43×` de resistir a `Físicos` e `2,50×` de ser
> imune a eles.* **Ela não precisa de tabela: precisa de uma linha.**

## A linha que falta no §6.3, e ela sai pronta

> ### **"Ser imune a uma condição que rouba ação do inimigo, ou que dá desvantagem nos ataques dele, multiplica o fator da categoria por `1,20`. Imunidade a qualquer outra condição custa `1,00×`."**

**O erro de simplificar assim é `+13%` no `Lento` e `+7%` no `Calado`, e ele erra pro lado que
SOBRECOBRA** — *a mesa ganha.*

---

# § 4 · ⚠ O ACHADO DE LADO — o `Derrubado` é `Leve` e nega tanto quanto as `Pesada`

**`Derrubado` mede `1,19×`. `Cego`, que é `Pesada`, mede o mesmo `1,19×`.**

*O motivo: pro INIMIGO o que conta é a desvantagem nos ataques dele, e as duas dão isso. As outras
coisas do `Cego` — falhar teste de vista — não mudam nada num chefe que está em pé no meio da mesa.*

> ### O nível da condição é calibrado no corpo do JOGADOR. O corpo do inimigo é outro.
> **É o mesmo padrão do §6.5:** *o inimigo monta no Fundamento do jogador, mas com a economia de ação
> dele.* ⚠ *Isto **não** reabre a peça 19 — o nível dela está certo pro que ela mede. Só não vale
> transportar direto.*

---

# § 5 · E ELA ERRA PRO LADO SEGURO

**Se ninguém no grupo comprou aquela condição, o inimigo pagou por uma imunidade que não usou** — *o
encontro foi cobrado mais caro do que é.* **A mesa ganha.**

> ⟹ **É o mesmo lado da resistência a dano, e o oposto da vulnerabilidade** *(que devolve orçamento
> por uma coisa que o grupo pode não ter)*. **Isso reforça o martelo `A`.**

## ⚠ E o que NÃO está contado, de propósito

**`1`** a vantagem que `Cego` · `Derrubado` · `Impedido` dão a QUEM ATACA o inimigo — *isso mexe na
vida efetiva, não na saída; contar aqui seria contar duas vezes.*
**`2`** o `Incapacitado`, que transforma acerto corpo a corpo em crítico.

> **Os dois deixam a régua CONSERVADORA. Declarado, não esquecido.**

---

# § 6 · O QUE FALTA

> **Só o martelo `C` do arquivo irmão:** *a imunidade a condição cabe na célula `Imunidades` que já
> existe, ganha linha própria, ou não existe?*
> **A conta do preço, que era o que faltava pra decidir, está aqui.**

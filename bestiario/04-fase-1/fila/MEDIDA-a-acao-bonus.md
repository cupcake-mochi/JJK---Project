# A `Ação Bônus` do inimigo — e o `tipo`

*10/09/2026. Conta em `medir-a-acao-bonus.py`, saída em `SAIDA-acao-bonus.txt`.*

> ***Pergunta do Mizuki:*** *"Compare com os sistemas q andamos nos baseando, falta algo? Eu notei q
> falta, **a gente coloca ação bonus?**"*

---

## 0 · Primeiro: a rodada de 09/09 já tinha feito a comparação campo a campo, e ela NÃO pegou isto

**O `campo-ficha.md` lista `FALTA-1` a `FALTA-8`, comparando o bloco contra D&D 2024, PF2e, Draw Steel
e Daggerheart.** *Nenhuma delas é Ação Bônus.*

| | estado hoje |
|---|---|
| `FALTA-1` o golpe com dano | ✅ aplicado no `RASCUNHO-4` |
| `FALTA-2` rótulo de frequência | ✅ aplicado |
| `FALTA-3` tipo de movimento | ✅ aplicado |
| `FALTA-4` fraqueza | ✅ aplicado |
| `FALTA-5` idiomas | ✅ resolvido pelo `tipo`/`grau` — **não abre campo** |
| `FALTA-6` sentidos | ✅ cabe em `Traços` — **não abre campo** |
| `FALTA-7` preço de encontro misturado | fila — **não é do bloco** |
| `FALTA-8` tamanho carregando regra | ✅ **FECHADO em 10/09** |

> **As oito estão resolvidas. A `Ação Bônus` é buraco novo, e foi o Mizuki que achou.**

---

## 1 · O bloco não declara `Ação Bônus` em lugar nenhum

**A peça 26 §3 lista dezessete linhas. Sobre economia de ação, ela diz duas:**

| | |
|---|---|
| `ações por rodada` | *"personagens da categoria menos um, piso `1`"* |
| `Reação` | *"uma por rodada, volta no começo do turno dele"* |
| **`Ação Bônus`** | ⚠ **não aparece em lugar nenhum** |

**E o jogador tem as quatro** — Ação Padrão · **Ação Bônus** · Reação · movimento (peça 3 §2).

## 2 · E o catálogo do inimigo é o MESMO do jogador

*peça 26 §6: **"refino, aptidão, Passiva e técnica saem do mesmo catálogo"***

**E o catálogo tem coisa que custa Ação Bônus:**

| | onde | o texto |
|---|---|---|
| **`Rápido`** | Melhoria `Pesada` | *"Custa Ação Bônus em vez de Ação Padrão"* |
| **`Ímpeto`** | Classe Passiva `2` | *"Como Ação Bônus, você se move até o seu deslocamento"* |
| **`Campo`** | Classe Passiva `1` | *"A ação `Estudar` custa a sua Ação Bônus"* |
| **`Energia Reversa`** | aptidão | *"você pode usá-la como Ação Bônus"*, com `d4` em vez de `d8` |

> **Então uma aptidão que custa Ação Bônus não tem onde caber na ficha do inimigo.**

---

# 3 · ⚠⚠ A PROVA — o sistema JÁ decidiu, e a decisão está dentro de uma condição publicada

**O texto do `Lento`, no manual:**

> *"**Deslocamento pela metade, e sem Ação Bônus.**"*

**E a peça 19 §2.2 publica o valor dele CONTRA O CHEFE: `39,20` de dano por rodada, `0,5` ações negadas.**

**Reconstruindo das âncoras:**

| | |
|---|---|
| metade do deslocamento | `4,5 m × 0,60` = **`2,70`** |
| **a Ação Bônus** | `0,5 × 73,00` = **`36,50`** |
| **total** | **`39,20`** |

> ### ✅ Fecha exato — `39,20` é o número publicado.
>
> **O `Lento` tira duas coisas, e a metade do deslocamento explica só `2,70` delas. Todo o resto —
> `36,50` — é a Ação Bônus.**

> ### ⟹ O sistema já decidiu que o inimigo TEM Ação Bônus, e já preçou ela em meia ação.
> **Se ele não tivesse, o `Lento` estaria sobrepreçado em `93%` contra inimigo** — e ele é uma das
> treze condições publicadas, com validador em cima.

## 3.1 E é o mesmo tamanho da `Reação` — por duas rotas que não se falam

| | derivada de | vale |
|---|---|---|
| a **`Reação`** | o `Atordoado` — `1,5 − 1,0` | `0,5` ação = **`36,50`** |
| a **`Ação Bônus`** | o `Lento` — a sobra depois do deslocamento | `0,5` ação = **`36,50`** |

> **Duas condições publicadas diferentes, sem se falarem, e o mesmo número.**

---

# 4 · O que falta fazer — e NÃO é recalibrar

**A Ação Bônus do inimigo já está no orçamento: ela foi preçada quando o `Lento` foi preçado.**
*O que falta é o bloco DIZER que ela existe.*

**E ela não muda a cota de dano, pelo mesmo motivo que as `Intervenções` `2` e `3` não mudam:** *o que
se faz com Ação Bônus no catálogo quase nunca é dano.*

| | soma na cota? |
|---|---|
| `Ímpeto` — mover, posicionar | **não** |
| `Campo` — `Estudar` | **não** |
| `Energia Reversa` — curar | **não** |
| `Rápido` — conjurar | **SIM** |

## 4.1 E a forma de escrever segue a decisão que o bloco já tomou

**O `RASCUNHO-4` cortou `Reação 1 por rodada` de todo bloco com o argumento *"é constante pra todo
inimigo"*.** *A `Ação Bônus` é igualmente constante.*

> ### ⟹ Ela NÃO vira célula. Ela vira duas coisas:
> **1.** uma linha no **capítulo de combate**, junto com a `Reação`: *o inimigo tem `1` Ação Bônus e
> `1` Reação por rodada, como todo mundo*
> **2.** um **rótulo de custo** na entrada que a usa: `‹ nome › (Ação Bônus).`

*Assim o bloco não ganha campo, e a aptidão que custa Ação Bônus passa a ter onde caber.*

---

# 5 · O `tipo` — o que ele carrega, pela descrição do Mizuki

***Ele, 10/09/2026:*** *"Sobre o 'tipo', ele só dá sabor basicamente, algumas mecânicas e regras
adicionais que são coisas básicas, pode pôr na fila. **Maldição toma dano pra energia reversa,
restringido passa por barreira, civil n vê maldição sem item (restringido também), sem técnica n tem
técnica**, coisas assim, n falei tudo, dei uma generalizada."*

**Então o `tipo` carrega um pacote pequeno, e ele é qualitativo — não custa orçamento.**

| tipo | o que o pacote carrega *(exemplos dele, não a lista fechada)* |
|---|---|
| **`maldição`** | **toma dano de Energia Reversa** |
| **`restringido`** | **passa por barreira** · **não vê maldição sem item** |
| **`civil`** | **não vê maldição sem item** |
| **`sem técnica`** | **não tem técnica** — e a peça 26 §6.2 já escreve isso: *"ele não tem refino, aptidão nem técnica, e a cota de dano vem do corpo"* |
| **`feiticeiro`** | — *a definir* |

> **E o tamanho do pacote tem teto, e ele já está escrito:** *a §7 das `decisoes-fase-1` diz que
> resistência a `1` ou `2` tipos **custa nada — é sabor**.* **Um pacote maior que isso passa a custar.**
>
> ⚠ **E o "não vê maldição" tem apoio do lado do jogador:** *"quem não tem energia não nasce
> enxergando maldição"* — peça 13, o Legado `Aprendi a Ver`. **A regra já existe; falta o bloco
> herdar ela pelo `tipo`.**

**Fica na fila, e a lista completa é do Mizuki.**

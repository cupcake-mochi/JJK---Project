# RASCUNHO — o repreço do ritmo de XP

**Aberto na v0.195.** *As decisões estão tomadas e os números medidos; nada está aplicado na peça 12, no capítulo 80 nem no `conferir-xp.py`.* **Este arquivo existe para o trabalho não se perder se a conversa acabar antes dele.**

> **Ele é rascunho e não peça** — sem número na frente, e o `conferir-repositorio.py` falha se ele tomar um. *Ele morre quando a peça 12 e o capítulo 80 estiverem escritos.*

---

## A CURVA, decidida

***Decisão do Mizuki:*** **`3` mesas para o primeiro nível, e sobe uma a cada dois níveis — com o nível 2 protegido em `2`.**

| você está no nível | mesas para o próximo | em XP |
|---|---|---|
| **2** | **2** | `200` |
| **3** | 3 | `300` |
| **4 a 5** | 4 | `400` |
| **6 a 7** | 5 | `500` |
| **8 a 9** | 6 | `600` |
| **10 a 11** | 7 | `700` |
| **12 a 13** | 8 | `800` |
| **14 a 15** | 9 | `900` |
| **16 a 17** | 10 | `1.000` |
| **18 a 19** | 11 | `1.100` |
| **20 a 21** | 12 | `1.200` |
| **22 a 23** | 13 | `1.300` |
| **24 a 29** | 14 | `1.400` |

**`125` mesas até o nível 20 e `259` até o 30** — `12.500` e `13.400` de XP. *Hoje são `63` e `145` mesas, `6.300` e `8.200` de XP.*

> **O nível 2 custar `2` em vez de `3` é concessão declarada, e ela custa quase nada:** *uma mesa a menos no total, e o nível 20 se move menos de dois décimos de mês.* **Ela existe para a ficha nova subir de nível na segunda mesa e não na terceira** — é o degrau que decide se alguém fica.
>
> **O teto em `14` é o único número que não sai da fórmula.** *Ele segura a faixa lendária, e sem ele o topo ficaria mais lento do que o levantamento pede.*

---

## Quanto tempo leva, por cadência

**A coluna é o mês em que você CHEGA naquele nível, contando do nível 2.**

| nível | mesas | 1/15 dias | 1/sem | **2/sem** | 3/sem | 4/sem |
|---|---|---|---|---|---|---|
| **2** | 2 | 0,0 | 0,0 | **0,0** | 0,0 | 0,0 |
| **3** | 3 | 0,9 | 0,5 | **0,2** | 0,2 | 0,2 |
| **4** | 4 | 2,3 | 1,2 | **0,7** | 0,5 | 0,5 |
| **5** | 4 | 3,9 | 2,1 | **1,2** | 0,9 | 0,9 |
| **6** | 5 | 5,8 | 3,0 | **1,6** | 1,2 | 1,2 |
| **7** | 5 | 7,8 | 3,9 | **2,1** | 1,6 | 1,6 |
| **8** | 6 | 10,1 | 5,1 | **2,5** | 2,1 | 1,8 |
| **9** | 6 | 12,7 | 6,4 | **3,2** | 2,5 | 2,3 |
| **10** | 7 | 15,2 | 7,6 | **3,9** | 3,2 | 2,8 |
| **11** | 7 | 18,2 | 9,2 | **4,6** | 3,7 | 3,5 |
| **12** | 8 | 21,2 | 10,6 | **5,3** | 4,4 | 3,9 |
| **13** | 8 | 24,6 | 12,4 | **6,2** | 5,1 | 4,6 |
| **14** | 9 | 28,1 | 14,0 | **7,1** | 5,8 | 5,3 |
| **15** | 9 | 32,0 | 16,1 | **8,1** | 6,4 | 6,0 |
| **16** | 10 | 35,9 | 18,0 | **9,0** | 7,4 | 6,7 |
| **17** | 10 | 40,3 | 20,3 | **10,1** | 8,1 | 7,4 |
| **18** | 11 | 44,4 | 22,3 | **11,3** | 9,0 | 8,3 |
| **19** | 11 | 49,3 | 24,6 | **12,4** | 9,9 | 9,0 |
| **20** | 12 | 54,1 | 27,2 | **13,6** | 10,8 | 9,9 |
| **21** | 12 | 56,4 | 28,3 | **14,3** | 11,3 | 10,4 |
| **22** | 13 | 58,7 | 29,5 | **14,7** | 11,7 | 10,8 |
| **23** | 13 | 61,2 | 30,6 | **15,4** | 12,4 | 11,3 |
| **24** | 14 | 63,8 | 32,0 | **16,1** | 12,9 | 11,7 |
| **25** | 14 | 66,3 | 33,4 | **16,8** | 13,3 | 12,2 |
| **26** | 14 | 69,0 | 34,5 | **17,3** | 13,8 | 12,7 |
| **27** | 14 | 71,6 | 35,9 | **18,0** | 14,5 | 13,1 |
| **28** | 14 | 74,3 | 37,3 | **18,6** | 15,0 | 13,6 |
| **29** | 14 | 77,1 | 38,7 | **19,3** | 15,4 | 14,0 |
| **30** | — | 79,6 | 40,0 | **20,0** | 16,1 | 14,7 |

**A duas mesas por semana o nível 20 chega em `13,6` meses e o 30 em `20,0`.** *O alvo do Mizuki era `10`–`12` e depois `+2` meses; a curva entrega `+1,9` sobre a candidata anterior.*

---

## O invariante da faixa lendária continua de pé

**Do nível 20 ao 30 são `134` mesas contra `125` do 2 ao 20 — mais mesas — e mesmo assim `6,4` meses contra `13,6`.**

***A razão é `0,47`.*** *A Guilda pediu entre `0,45` e `0,61`, e o `conferir-xp.py` reprova fora de `0,35`–`0,75`.* **Passa.**

> **⚠ E é aqui que mora a coisa que quase passou.** *O que faz a faixa lendária ser mais rápida NÃO é a curva: é o **tamanho da missão**.* **A peça 12 supõe que do nível 20 em diante a Guilda roda longa e final de arco**, então a missão típica passa a pagar `241` XP em vez de `107`. *Modelar o jogo inteiro a `100` XP por missão dá um resultado errado, e foi o erro que o Mizuki pegou lendo a tabela.*

---

## O VÃO entre cadências, e ele fica SEM regra

***Decisão do Mizuki:*** **nenhum gatilho de catch-up entra na regra.** *"Não é ideal o livro obrigar formas de outros players receberem mais XP — apenas auxiliar e sugerir."*

**É a régua de voz nova aplicada:** *quanto se compensa quem joga menos é economia de guilda, e duas guildas podem responder diferente e as duas estarem certas.* **O livro mede, mostra o tamanho e sugere; o servidor decide.**

**O vão medido, sem gatilho nenhum:** *entre quem joga uma e quem joga duas mesas por semana, ele chega a **`14` níveis**, por volta do mês `20`.*

> **E a curva mais lenta NÃO encolhe o vão — isso eu afirmei e a conta desmentiu.** *As três candidatas medidas dão o mesmo pior vão; o que a curva muda é **quando** ele acontece.* **A de hoje entrega o pior no mês `11`, no meio da vida útil de uma temporada; esta empurra para o mês `20`.**

**A conta que o livro vai sugerir, e a peça guarda:**

| gatilho | fator | teto do vão |
|---|---|---|
| 3 níveis atrás | `2×` | **3** |
| 3 níveis atrás | `1,5×` | `5` ⚠ *dispara e não alcança* |
| — | — | **`14`** |

***O fator não é sabor:*** *é ele que faz o teto ser o número escolhido.*

---

## O que falta fazer

- [x] Validar a curva contra o alvo, e nas cinco cadências.
- [x] Medir o vão sem gatilho, com o tamanho de missão certo.
- [ ] **Escrever na peça 12**, com a derivação de cada número.
- [ ] **Escrever no capítulo 80 do livro**, na voz de lá, com o vão sugerido e não imposto.
- [ ] **Refazer o `conferir-xp.py`** — ele tem checagens penduradas na curva velha.
- [ ] **Regerar os quatro builds do livro**, e mandar o PDF de duas colunas.

> **⚠ O `conferir-xp.py` confere hoje: a soma até o nível 20, o abismo que fecha, os três perfis da Guilda e a razão da faixa lendária.** **Trocar a curva sem refazer essas quatro produz verde que não provou nada.**

---

## De onde saiu cada número

| número | dono |
|---|---|
| a cadência real da Guilda — `1` a `2` mesas por semana | `01-pesquisa/levantamento-ritmo-de-progressao.md` |
| a mediana de `10,25` meses até o nível 20 | o mesmo |
| o tamanho de missão por faixa — `107` e `241` XP | peça 12 §7, a tabela das duas faixas |
| o desconto da semana, e o teto de `2,9` eficazes | peça 12 §5 |
| as quatro posições externas sobre o vão | `01-pesquisa/levantamento-ritmo-fora-do-projeto.md` |

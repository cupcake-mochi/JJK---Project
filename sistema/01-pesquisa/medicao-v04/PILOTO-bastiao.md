# Piloto da medição da coleção v0.4 — o Bastião

**Pedido do Mizuki em 27/09/2026: "2 - A"** — *um piloto com o Bastião, sem agente, que traz o método, os números e as duas pendências que a própria v0.4 deixou; depois ele decide o resto.* **Nada aqui é regra, e nenhum número do sistema se moveu.**

## As respostas do Mizuki — v0.280

- **`Contra a Parede`:** *"Ele n custa PE, o 'metade da sua maior classe' é o feitiço que acompanha (arredondado para baixo), o custo desse 'feitiço que acompanha', é o custo do feitiço mesmo".* **É a linha "para baixo, pagando o PE" da tabela das pendências.** *A ordem veio na volta seguinte: "Depois do primeiro golpe e n crita".*
- **`Oportunista` — "2 - A":** *um ataque do feitiço, ou o primeiro TR de uma criatura contra ele, até o fim do seu próximo turno.*
- **O `Combatente Amaldiçoado` fica como está — "3 - A":** *"N acho q os valores atuais estão corretos, sendo franco, você está calculando cogitando muitas coisas, n precisa tanto."* **É a terceira vez que ele acha a conta inflada**, *depois da `Brasa`, na v0.81, e do `Mirar`, na v0.86.*
- **O resto do item 12 — "2 - B":** *os outros três Caminhos são lidos sem conta, atrás de regra ambígua e de texto que brigue com o resto do sistema.*

**As frases decididas estão no livro e na peça 6 §2, na tabela `Pendências da v0.4 decididas`.** *O que vem abaixo é o piloto como foi medido, antes das respostas: a tabela das Trilhas soma o `Contra a Parede` de graça, e nenhum número publicado saiu daqui.*

## O piloto

A conta está em `conta-bastiao.py`, ao lado deste arquivo. **Ela reproduz antes as linhas da coleção anterior que as entregas novas repetem** — a fatia de `5,08`, o soco a `11,50`, o `Engate` a `1,70`, o `Derrubado` do `Encontrão` a `0,56`, a resistência a dois e a quatro tipos a `1,33` e `2,17`, e o Classe 0 e as Classes 3, 4 e 7 do manual.

## O método

**A régua é a da coleção anterior**: *uma Trilha leva `5,00` fatias, a banda aceita é de `4,50` a `5,00`, e a fatia é `5,08` de dano por rodada no nível 30.* **Acerto e falha de Teste de Resistência são os de hoje** — `55%` e `35%`, que a v0.119 mediu e não aplicou à coleção anterior —, *porque as entregas são novas e não há preço antigo para preservar.*

**O que a régua não tem, o piloto escreve como convenção, em faixa**, *com um valor baixo e um alto:*

| convenção | baixo | alto |
|---|---|---|
| golpes que o Bastião assume por `Olhos Em Mim`, por rodada | `0,5` | `1,0` |
| o atacante ao alcance do contra-golpe | `50%` | `100%` |
| golpes que o Bastião recebe por rodada, para o Bloquear | `1` | `2` |
| rodadas com metade da vida ou menos | `25%` | `50%` |
| rodadas em que o `Guarda-Costas` vale | `50%` | `75%` |
| Testes de Resistência Físicos por rodada | `0,25` | `0,5` |
| rodadas com quatro inimigos na área do `Arrastão` | `0%` | `50%` |

## As três Trilhas

| Trilha | nv 2 | nv 11 | nv 19 | nv 27 | total |
|---|---|---|---|---|---|
| **`Muro`** | `Alicerce` `1,33` | `Guarda-Costas` `0,67`–`1,00` | `Casca Grossa` `1,57`–`3,15` | `Inabalável` `0,84` | **`4,41`–`6,32`** |
| **`Punho`** | `Trocação Franca` `2,37`–`4,07` | `Mão Pesada` `1,00` | `Minha Vez` `0,05`–`0,17` | `Arrastão` `0,00`–`2,26` | **`3,42`–`7,50`** |
| **`Combatente Amaldiçoado`** | `Retaliação` `3,12`–`5,89` | `Embalo` `1,06`–`1,72` | `Oportunista` `0,90`–`1,40` | `Contra a Parede` `1,97`–`3,94` | **`7,06`–`12,95`** |

- **O `Muro` cai na banda no lado baixo e passa no alto**, e quem decide é a `Casca Grossa`: *`16` de dano descontado por golpe assumido, e o preço dela anda junto com quantos golpes o `Olhos Em Mim` transfere.*
- **O `Punho` é a Trilha mais larga**, *porque o golpe extra da `Trocação Franca` e o `Arrastão` dependem da luta — um chefe sozinho não enche a área.* **O `Minha Vez` quase não vale nada:** *os `2` PE custam `10,28` de dano, e o soco dá `11,50`.*
- **O `Combatente Amaldiçoado` passa do orçamento em qualquer leitura**, *e o maior pedaço é a `Retaliação`: um Classe 0 de graça em todo golpe assumido, `27` de dano por uso.* **Só ela vale de `3,12` a `5,89` fatias.**

## As duas pendências da v0.4

**`Contra a Parede`** — *a metade da maior Classe e o custo da conjuração decidem tudo; a ordem entre ataque e feitiço não mexe no número:*

| arredonda | custo | por uso | fatias |
|---|---|---|---|
| para baixo (Classe 3) | de graça | `40` | `1,97`–`3,94` |
| para baixo (Classe 3) | pagando o PE | `−6,3` | negativo |
| para cima (Classe 4) | de graça | `54` | `2,66`–`5,31` |
| para cima (Classe 4) | pagando o PE | `−7,7` | negativo |

*Pagando, ela nunca vale a pena: um Classe 3 rende `4,44` de dano por PE, e o câmbio do sistema é `5,14`.*

**`Oportunista`** — *um alvo contra todos os alvos de um feitiço de área:* `0,90`–`1,40` fatia com um só, `2,71`–`4,20` com três.

## O Caminho base

**A régua antiga dava `3,00` fatias ao Caminho, e ele nunca foi preçado por inteiro — nem na coleção anterior.**

- **`Ainda de Pé`** (nv 7): *`1d8 + 15` de cura, uma vez por cena, numa luta de `3,3` rodadas —* **`1,16` fatia.**
- **`Duro de Matar`** (nv 15): *`2d10 + Constituição 6` no golpe que entrou, uma vez por rodada —* **`1,84` a `2,67` fatias.**
- **As duas juntas já dão de `3,00` a `3,83`**, *sem contar o resto.*
- **Três entregas não têm conversão na régua:** *a transferência de golpe e a Provocação em área do `Olhos Em Mim` (nv 2) e do `Chega Mais` (nv 23), e o `Passa Pra Mim` (nv 30), que é "a queda não aconteceu" — a mesma lacuna do `Ninguém Cai`, registrada no `DESENHO-caminhos.md` desde a v0.77.*
- *O `Ataque Extra` é correção de base, de graça pela peça 6 §3.1, e o `Nem Um Arranhão` depende de quantos efeitos de Teste de Resistência Físico a luta tem.*

## O que o piloto mostrou sobre o resto da medição

**A régua cobre bem o que é dano, acerto, posição e condição**, *e o custo por entrega foi de minutos quando a linha já existia.* **Ela não cobre três famílias que a v0.4 usa muito**: *golpe assumido no lugar de um aliado, Provocação, e queda evitada.* **Sem uma convenção para essas três, qualquer Caminho que as use sai em faixa larga — e o Bastião usa as três no Caminho base.**

# A `Sobrecarga` — onde a mudança encosta no repositório

*09/09/2026. **Nada disto foi mexido.** O repositório `Claude 2` é fonte de leitura aqui; outra conta
mexe nele. Esta é a lista pra quem tem a escrita.*

> **"É uma linha no feitiço" é verdade na regra e falso no disco.** *A linha tem **três** donos e
> **cinco** dependências.*

---

## Os três donos do texto — e um deles discorda dos outros dois

| # | arquivo | linha | o que está escrito hoje |
|---|---|---|---|
| **1** | `manual/gerador/partD.js` | `114` | `['Sobrecarga', 'Leve', 'Até o fim do próximo turno do alvo, o feitiço dele custa o dobro de energia e sai com a CD 2 menor.']` |
| **2** | `sistema/05-material/livro/manual/40-fundamento.md` | `711` | `` | `Sobrecarga` | `Pesada` | Até o fim do próximo turno do alvo, o feitiço dele custa o dobro de energia e sai com a CD 2 menor. | `` |
| **3** | `manual/Fundamento-MANUAL-v7.docx` | — | **gerado** do `partD.js` pelo `make.js`. Não se edita à mão — regenera |

> **O degrau diverge: `Leve` nos donos `1` e `3`, `Pesada` no dono `2`.** *É uma das vinte e cinco
> divergências da v0.219, e **a única que é de preço**.*

---

## As cinco dependências

| # | arquivo | o que acontece |
|---|---|---|
| **4** | `manual/matematica/sobrecarga.py` | **a conta inteira caduca.** Ela mede *"o dobro de energia"* — a seção `METADE 1` do script deixa de existir. E ela lê a string literal `O inimigo não conta PE` da peça 26, que **continua de pé** pela decisão de 09/09: *o script não quebra por esse lado* |
| **5** | `sistema/05-material/livro/ESTADO-revisao.md` | linha `43` da tabela de divergências: `` `Sobrecarga` \| o DEGRAU: `Leve` no manual, `Pesada` no livro. É a única de preço \| sim \| aberta ``. **Ela passa de `aberta` para `fechada na vX.YYY`** — e aí a checagem `12` do `conferir-repositorio.py` passa a **obrigar** os dois lados a dizerem a mesma coisa |
| **6** | `sistema/03-mecanica/conferir-acao.py`, linha `244` | a checagem `5` proíbe a frase `o dobro de energia` de voltar **na `Dívida`** e **não olha para a `Sobrecarga`**. *A v0.219 registrou exatamente isso.* **Se a frase sair da `Sobrecarga`, vale estender a checagem pra ela** — senão o mesmo defeito volta por uma porta que ninguém guarda |
| **7** | `sistema/ESTADO-ATUAL.md`, linhas `1290` e `1304` | **estão desatualizadas, e não por causa desta mudança.** A `1290` diz *"O inimigo **vai** contar energia, com poço semelhante ao do jogador"* e manda *"peça 26 §6.1 cair"*. **A decisão de 09/09 reverteu isso** — o §6.1 fica. A `1304` diz que a `Sobrecarga` *"com o inimigo contando PE passa a ter alvo dos dois lados da mesa"*, e o inimigo não vai contar PE |
| **8** | `logs/CHANGELOG.md` | entrada nova. E a v0.220 precisa ser marcada como **revertida** — ela decidiu dar PE ao inimigo |

---

## A ordem que não gera commit travado

**A v0.220 já ensinou a armadilha:** *registrar uma decisão que ainda não foi aplicada TRAVA o
commit, e a perturbação `fechada` do arnês da v0.219 acende exatamente esse caso — linha marcada
como resolvida com os dois lados ainda discordando.*

| passo | |
|---|---|
| **1** | muda o texto e o degrau nos donos `1` e `2`, **com o mesmo valor nos dois** |
| **2** | regenera o `.docx` (dono `3`) pelo `make.js` |
| **3** | **só então** vira a linha `43` do `ESTADO-revisao.md` de `aberta` para `fechada` |
| **4** | refaz o `sobrecarga.py` — ou aposenta ele e escreve a conta nova |
| **5** | estende a checagem `5` do `conferir-acao.py`, se a frase sair |
| **6** | corrige as duas linhas do `ESTADO-ATUAL.md` e escreve a entrada do CHANGELOG |

> ⚠ **Virar a linha `43` antes do passo `1` reprova a suíte**, porque a checagem `12` passa a cobrar
> igualdade entre dois lados que ainda discordam.

---

## E uma colisão de nome, se a escolha for a candidata `R`

**`Reação` já tem dois significados no sistema:**

| onde | o que quer dizer |
|---|---|
| peça 3 §2 | o **slot de ação** — *"uma, e ela volta no começo do seu turno"* |
| `partD.js` linha `136` e o livro linha `745` | uma **Melhoria** `Pesada` — *"Você conjura como Reação, a um gatilho que você declara"* |

**A colisão é anterior a esta mudança, e não é fatal** — *"o alvo não usa Reação"* lê como o slot, e
um feitiço comprado com a Melhoria `Reação` cai junto, que é coerente.

*Mas a skill `redacao-acessivel-rpg` é explícita: **uma coisa por nome**. Se a `Sobrecarga` passar a
falar de `Reação`, o termo ganha uma terceira aparição e vale amarrar no glossário.*


---

# 🆕 E MAIS TRÊS BLOCOS DE MEXIDA CHEGARAM EM 10/09 — todos no §6.5 e vizinhos

*⚠ **Os três mexem na peça 26. Fazer os três num commit só**, senão são três passadas no mesmo arquivo.*

| item | o quê | onde está escrito |
|---|---|---|
| **`11`** | tirar *"área reparte a cota, e não multiplica ela"* do §6.5, e escrever a trava **`1` ação em área à vontade, `Recarga` não conta** | `fila/DECIDIDO-o-aperto-e-a-area.md` §2 |
| **`6`** | tirar *"nunca por cima"* do §6.5 e corrigir o `0,70×` da cura pra `0,64×` | já estava na fila |
| **`5`** | **`5` trocas** — o `degrau` morre como moeda e vira **fator × multiplicador**, no §3, §6.3, §6.4, §6.5 e na checagem `8` | `fila/DECIDIDO-o-degrau.md` §5 |

> ### ⚠ E o `11` e o `5` se ENCONTRAM no §6.4
> *O `11` tira uma frase do §6.5 que aponta pro §4.6; o `5` reescreve o §6.4 inteiro.* **Fazer o `5`
> primeiro deixa o `11` com uma frase a menos pra consertar.**

---

# 🆕🔴 E MAIS DUAS MEXIDAS NO §6.3 — achadas em 10/09 medindo a resistência

*`fila/MEDIDA-a-resistencia-e-a-vulnerabilidade.md` §2. **As duas são do mesmo commit dos itens
`5`, `6`, `9` e `11`** — é a mesma seção que a mexida `1` e a `2` do item `5` já tocam.*

> ### ⚠ Elas não estavam na lista, e as duas QUEBRAM no dia que o item `5` entrar.
> *A lista do `DECIDIDO-o-degrau.md` §5 troca a resistência e a imunidade pro fator. **Duas frases do
> mesmo §6.3 ficam apontando pra moeda morta.***

| # | a frase, no §6.3 | o que ela vira |
|---|---|---|
| **`6`** | *"**Vulnerabilidade devolve na mesma moeda.**"* — ⚠ *"a mesma moeda" é o **degrau**, e o item `5` mata o degrau* | ✅ **MARTELADO em 10/09** ⟹ **"a vulnerabilidade é `1,00×`: não cobra e não devolve"**, com a nota de que `3` de `3` sistemas que a mantêm não mexem no custo de encontro. *`DECIDIDO-a-resistencia-e-a-vulnerabilidade.md` §A* |
| **`7`** | *"Um chefe de **`Alcateia`** imune a `Físicos` vira uma luta de `7,50` rodadas…"* — ⚠⚠ **`Alcateia` é da escada MORTA**, `2` menções | trocar pela categoria viva **e refazer o exemplo com a vida da escada nova.** *Publicar o número velho é o defeito que o projeto já achou quatro vezes* |

> ## ⟹ O commit passa de `7` mexidas + validador para `9` mexidas + validador.
> **E a `7` é a QUINTA tabela velha achada no projeto** — *o `ESTADO` já registra que esse é o padrão:
> toda vez que a escada mudou, alguma tabela ficou pra trás e ninguém acusou.*


---

# 🆕 E MAIS DUAS LINHAS NOVAS NO §6.3 — dos martelos `C` e `D` de 10/09

*`fila/DECIDIDO-a-resistencia-e-a-vulnerabilidade.md`. **Mesmo commit.***

| # | onde | o que ENTRA (é linha nova, não troca) |
|---|---|---|
| **`8`** | **§6.3** | 🆕 **a imunidade a CONDIÇÃO, que não era preçada em lugar nenhum:** *"Ser imune a uma condição que rouba ação do inimigo, ou que dá desvantagem nos ataques dele, multiplica o fator por `1,20`. Imunidade a qualquer outra condição custa `1,00×`."* **Régua em `fila/MEDIDA-a-imunidade-a-condicao.md`, toda de âncora publicada** |
| **`9`** | **§6.3** | 🆕 **a linha de aviso do `Físicos`:** *"Um `Desastre` imune a `Físicos` exige `10` personagens, não `4`. A edição viva do D&D publica isso zero vezes em `331` blocos — se você vender, saiba que está vendendo o item mais caro do livro."* ⚠ **É aviso, não trava** — o martelo `D` manteve vendável |

> ## ⟹ O commit da peça 26 está em `11` mexidas + o validador.
> **`5` do item `9`** *(§4.3 · §4.5 · §5 · checagem `5`)* · **`5` do item `5`** *(o degrau vira fator)* ·
> **`2` do `6` e do `11`** *(o §6.5)* · **`4` novas do §6.3** *(vulnerabilidade · `Alcateia` ·
> condição · aviso do `Físicos`)*.
>
> ⚠ **Todas na peça 26. Um commit só, senão são quatro passadas no mesmo arquivo.**

---
---

# 🆕 LADO DO JOGADOR — `3` mexidas no `partC.js` e `partD.js`, itens `27` · `28` · `29`

> ### ⚠ Este cabeçalho dizia `4` até 10/09, e estava velho — o `29a` é **NÃO FAZER**.
> *A própria tabela abaixo já dizia "os **três** que sobraram".* **É o mesmo defeito que o projeto já
> pegou seis vezes: a decisão andou e a contagem ficou.**

*`fila/DECIDIDO-o-cone-o-anteparo-e-o-espalhamento.md`, martelado em 10/09.*
**⚠ Estas NÃO são na peça 26 — são no gerador. Commit separado.**

| # | arquivo | o quê | risco |
|---|---|---|---|
| **`27`** | `partC.js`, Forma `Cone` | ➕ *"A largura do cone em qualquer ponto é igual à distância daquele ponto até você."* | 🟢 **nenhum** — escreve o que faltava. *É o padrão de fábrica do Foundry (`53°`)* |
| **`28`** | `partD.js`, Melhoria `Anteparo` | ➕ *"Ocupa os mesmos quadrados que a `Linha` da Classe dele, arrumados como você quiser, cada um partilhando um lado com outro. Altura mínima `2` quadrados. Colocado num ponto a até o alcance do feitiço."* | 🟢 **nenhum** — a Melhoria não tinha dimensão nenhuma |
| **`29b`** | `partC.js`, Forma `Linha` | ➕ *"Quando o comprimento chega ao topo da escada, `Maior` passa a subir a LARGURA: `1,5 → 3 → 4,5 m`."* | 🟢 **baixo** — só dá destino a uma compra que hoje é jogada fora. *Nenhum feitiço pronto encolhe* |
| ~~`29a`~~ | — | ❌ **NÃO FAZER.** *Repreçar as três formas foi REPROVADO pela medição: o nosso espalhamento na base é `2,79×`, idêntico ao do D&D 2024, e o Draw Steel espalha `13,44×`* | — |

> ## ⚠⚠ E ISSO FECHA O ITEM `15` SEM PRECISAR ABRIR ELE.
> **O que fazia o `15` ser caro era o `29a`** — *repreçar área mexeria no que os jogadores já
> construíram.* **A medição matou o `29a`.** *Os três que sobraram só ACRESCENTAM texto onde não havia
> número, e nenhum encolhe feitiço pronto.*

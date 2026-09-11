# A mesa de ND 20 — a primeira evidência de jogo do projeto

*Mesa rodada em 07/09/2026. Relato colhido em 08/09.*

A pasta `04-playtest/` do repositório está vazia desde a v0.1, e todo número do sistema é previsão. **Esta é a primeira vez que alguém rodou combate e contou o que aconteceu.**

## O aviso do próprio mestre

> *"funcionou pq o sistema por parte do players está tão bem estruturado q eu consegui fazer uma média de vida da galera e quanto dano eu queria dar, sou mestre veterano"*

**Isso não é 'deu certo, então está certo'.** O que deu certo foi o motor de combate e a experiência de quem estava mestrando. A camada de construção de inimigo foi contornada, não usada.

## A cena

**Um inimigo só, um "Sukuna" — chefe solo de fim de arco, em DUAS FASES.**

| o que ele fez | de onde tirou |
|---|---|
| **vida** | a linha da `Calamidade`, dividida em duas fases — cerca de `550` por fase, "aumentei só um pouco" |
| **dano** | pegou o golpe da `Dupla` sem querer, achou alto demais, **cortou pela metade**: `4d8 + 16` no alvo único |
| **dano em área** | ajustou para `10` a `15` a menos, ficando por volta de `3d8 + 10` |
| **ajuste durante a luta** | foi subindo e descendo o dano conforme achou necessário |
| **Defesa** | a do sistema — `18` no nível 20 |
| **CD** | a da ficha, sem mexer |
| **pressão** | quando quis apertar, **dobrava os dados e o modificador**, mas **não batia mais vezes na rodada** — no molde da baforada de dragão com recarga |

**Ele não travou em momento nenhum.**

## O que isso confirma, corrige e derruba

### 1. A `Dupla` está errada, e a mesa provou antes da conta

Ele pegou o número da `Dupla` por acidente, achou "alto pra caralho" e cortou pela metade **na hora, no olho.**

O golpe da `Dupla` no nível 20 é `8d8 + 37`. Metade é `4d8 + 18`. Ele usou `4d8 + 16`.

> **A mão dele reproduziu o conserto que a conta apontou depois.** A `Dupla` bate `45%` da vida de um personagem por golpe, contra `23%` da `Ronda` e `30%` da `Alcateia`, e a causa é o `fator` único fazendo vida e dano ao mesmo tempo.

### 2. A CD está validada por jogo. Não mexer

> *"tinha gente q falhava, tinha gente q passava, gente com atributo baixo q tinha CHANCE de passar e passava, mesmo falhando na grande maioria, tudo fluiu mt bem"*

**Essa é a descrição de uma curva de teste de resistência funcionando.** É o único número do bestiário com evidência de mesa a favor.

### 3. A Defesa é o número que o mestre apontou

> *"a galera tinha seus 9 de acerto, ent... ter 18 de defesa n é lá uma média boa pra um inimigo de final de arco"*

**Medido:**

| acerto do grupo | contra Defesa `18` | `19` | `20` | `21` |
|---|---|---|---|---|
| `+9` | **`60%`** | `55%` | `50%` | `45%` |

**E aqui está a comparação que importa:** a peça 1 §6 publica que um personagem acerta um alvo difícil — alguém que investiu em Destreza e carrega refino — em **`55%`**.

> **O chefe de fim de arco é MAIS FÁCIL de acertar que um personagem bem montado.** *Não é erro de conta: a Defesa do inimigo é `10 + atributo + proteção`, a mesma fórmula do jogador. Ele herda a Defesa de um PJ, e um chefe não é um PJ.*

*Se isso deve ser consertado com um número maior, com uma régua própria, ou com outra coisa — é decisão de desenho, e ela está aberta.*

### 4. Ele NÃO quis mais ações. Quis um golpe maior e com trava

**Isso derruba a correção que eu ia propor.**

A saída óbvia para o golpe grande da `Dupla` era dar mais ações ao inimigo, que é o que o D&D e o Pathfinder fazem. **Mas quando o mestre quis apertar, ele fez o contrário:** dobrou os dados e o modificador, e manteve o número de ataques.

> *"ficava fazendo q nem dnd com 'a baforada do dragão' q tem recarga, dá dano pra crl, mas come o turno quase todo"*

**Ele reinventou sozinho o molde da ação de uso limitado.** E ele bate com o que a pesquisa já tinha achado: no D&D, ação de uso limitado entrega cerca de **quatro vezes** o dano de uma ação comum, e a peça 26 §6.5 já mediu que uma habilidade guardada, `1 ×` por luta, **sai de graça** na régua — ela muda em que rodada o grupo apanha, não quanto.

### 5. O chefe de duas fases não existe no sistema

Ele partiu a `Calamidade` em duas metades de vida e tratou como duas fases. **Não há regra nenhuma sobre isso em lugar nenhum do repositório.**

### 6. Metade da máquina antiga não foi exercitada

Categoria, sub-categoria e câmbio existem para responder *"em quantos corpos o encontro se parte"*. **A cena tinha um inimigo.** Essa metade da peça não foi testada nem a favor nem contra.

### 7. Ele ajustou o dano no meio da luta, e isso é requisito

A folha não pode ser uma coisa que trava. Ela tem que suportar o mestre subindo e descendo o número enquanto joga.

## O que ele quer, nas palavras dele

> *"Eu gosto do mesmo feeling que uma ficha de DnD tem (...) ela é funcional, ela tem todo o stat block do inimigo, com TUDO, resistências, rolagens, vida, defesa, TUDO, aí depois vêm as partes únicas, como habilidades, passivas, ações lendárias, magias, que dão o tempero, aí uma ficha de inimigo n passa de uma página de duas colunas, no MÁXIMO duas páginas, o q é fácil de visualizar em um segundo monitor, n tendo de ler PÁGINAS E PÁGINAS pra entender o q um inimigo faz, ou ter uma ficha de planilha imensa"*

**Os requisitos que saem daí:**

| requisito | consequência |
|---|---|
| **uma página de duas colunas, no máximo duas** | é teto rígido, e ele mede o desenho |
| **tudo num lugar só** | vida, Defesa, rolagens, resistências, tudo no bloco. Sem cruzar documento |
| **bloco primeiro, tempero depois** | a parte fixa em cima, as habilidades únicas embaixo |
| **legível em um segundo monitor, num relance** | não é documento de leitura, é painel de consulta |
| **nem planilha, nem páginas e páginas** | os dois extremos que o material atual produziu: o `.docx` é folha de construção, a peça 26 é argumento |

## A conclusão da Fase 0 — FECHADA

***Decisão do Mizuki, 08/09/2026:*** o Bestiário é **duas coisas**, e nas palavras dele:

> *"1 — O bestiário KKK ent tem q ter exemplos lá, bestiários juntam... bestas! é um livro com inimigos. 2 — O como montar elas."*

| parte | o que é |
|---|---|
| **o catálogo** | um livro de inimigos prontos. É o que dá nome ao Bestiário |
| **a máquina** | como montar um novo |

**E as duas se encontram no BLOCO.** O catálogo é uma pilha de blocos preenchidos; a máquina é como preencher um em branco.

> **A referência de formato é o bloco de estatística do D&D**, e ele mandou o do Aboleth de 2024 como alvo. Uma página de duas colunas, no máximo duas.

**O que isso muda em relação à peça 26:** ela era só a máquina, e uma máquina de derivação com doze donos. O catálogo era item de fila que nunca chegou — seis maldições prontas, todas entre os níveis 2 e 8, dentro de um `.docx`.

*O desenho do bloco está em `03-bloco/`.*

# Levantamento — a energia do inimigo

*Colhido em 08 e 09/09/2026 pelo workflow `pe-do-inimigo`: duas frentes lendo o repositório e quatro
de pesquisa de campo externa. As seis fecharam. A fase de cálculo morreu duas vezes no limite de
sessão e foi refeita à mão depois — está em `PRECO-pe-do-inimigo.md`.*

---

> # ⚠ DUAS CORREÇÕES, e leia elas antes do resto
>
> *Achadas em 09/09 pela rodada de refutação (`refutacao/campo-construcao.md`), e consertadas aqui em
> 10/09. **O corpo do levantamento abaixo não foi reescrito** — estas duas linhas o corrigem.*
>
> ### 1 · O Daggerheart DÁ poço ao inimigo. A leitura de "nenhum dá" está errada.
>
> **O certo:** *nenhum dos sistemas medidos dá ao inimigo o poço **de DIA** que o jogador tem.*
> **Mas o Daggerheart dá um poço de ENCONTRO** — o `Stress` do adversário, **média medida `3,48` em
> `129` blocos**, e ele tem dupla função: quando esvazia, a criatura fica `Vulnerable`, e todo mundo
> passa a rolar com vantagem contra ela.
>
> *E o jogador consegue drenar esse poço à força — **"a number of PC features cause adversaries to
> mark Stress"** —, então economizar deixa de ser opção.* **O molde inteiro está medido em
> `decisoes-fase-1.md` §8, e foi visto e DESCARTADO com o porquê escrito.**
>
> ### 2 · A Malice do Draw Steel É poço, alimentado por renda. Não é "renda, e não poço".
>
> **O livro diz *"You can save it up"***, e a sobra **evapora no fim do encontro**. *Então ela é poço
> por encontro com renda por rodada — as duas coisas, e não uma delas.*
>
> *A renda é `número de heróis + número da rodada`, e é ela que a crítica publicada ataca:*
> **"having to track which round of combat it is is actually quite tedious"** — *e essa crítica
> alcança a renda, não o poço.*
>
> ---
>
> **Nenhuma das duas muda a decisão que este levantamento sustentou** — o inimigo não conta PE, e o
> limite é rótulo de frequência (`decisoes-fase-1.md` §8). *As duas mudam o RETRATO do campo, e o
> retrato é o que alguém vai citar depois.*

---

**O achado que enquadra tudo:** nunca existiu, em lugar nenhum do repositório, um número de PE de
inimigo. Nem proposta, nem faixa, nem fórmula. A v0.220 decidiu que ele tem energia e parou ali.

---

## Frente 1

O projeto decidiu DUAS vezes em sentidos opostos, e as duas decisões estão escritas com argumento.

**Contra o PE de inimigo (v0.198, reafirmado na v0.205):** o §6.1 da peça 26 tem quatro pernas, não uma. (a) *Orçamento*: "Tudo que ele faz sai do dano por rodada da ficha" — a cota já É o teto. (b) *Precedente*: o `Guia do Mestre` de 2014 diz que "o que um monstro tem é dano por rodada, e como esse dano se divide em ataques é livre", e o passo 13 escreve que as características "não mudam realmente as estatísticas" do monstro — "espaço de magia num bloco de conjurador é FORMA e não orçamento". (c) *Filtro multi-mestre*: "Contar PE de inimigo criaria uma segunda economia que só o mestre opera, e ela responderia diferente em duas mesas" — o critério que o próprio Mizuki chama de "o que decide quase tudo neste projeto". (d) *A perna que ninguém cita*: a decisão da v0.198 é literalmente "a ficha de inimigo é a ficha de personagem **sem o Caminho**", e o Caminho é quem entrega PE ao jogador. Não há de onde o PE do inimigo sair.

**A favor (v0.220, 07/09/2026):** "Sobrecarga vai ter peso pq ficha de inimigo vai ter energia, vai ser semelhante a de um player." A entrada registra que isso REVERTE o §6.1, que a medida da `Sobrecarga` caduca junto, e que quem for aplicar **precisa responder o filtro multi-mestre**. Nada foi aplicado: a pasta nova do Bestiário ainda lista o PE como item 2 da fila, atrás da técnica, "por decisão dele".

**O que já está preçado e não precisa ser inventado:** o câmbio PE↔dano tem dono e é antigo — `+1` PE por rodada = `5,14` de dano por rodada (peça 5 §4). O orçamento de feitiço do inimigo já é `golpe ÷ 4,5`, com piso na `Classe 1` (`3` pontos = `13,5` de dano), e a `Dupla` do nível 30 já monta `24,2` pontos numa ação contra o teto de `24` do jogador. Do lado do jogador: `3 × Classe` de PE por feitiço, `Classe 0` grátis, `5 × maior Classe` na Técnica Máxima, `6 × maior Classe` + a rodada inteira na Expansão, poço de `120` a `180` PE para `10,5` rodadas de luta por dia.

**A tensão a resolver:** o §6.5 hoje faz a aptidão do inimigo pagar em cota justamente porque ele não tem PE, e o §6.4 dá a ele a Expansão de graça pelo mesmo motivo. Dar PE ao inimigo derruba as duas — o diagnóstico da Fase 0 já escreveu isso: "Isso derruba o §6.1 e a moeda de metade do §6.5". E o §6.2 registra que existe inimigo com energia ZERO por ficção (o ramo da Maki), cuja ficha hoje "não muda de tamanho por causa disso".

### O argumento inteiro do §6.1 — o inimigo não conta PE. Título: "### 6.1 O inimigo não conta PE, e a cota de dano é o orçamento dele". Corpo literal: "**Tudo que ele faz sai do dano por rodada da ficha.

**Números:**
```
nenhum número; três afirmações: (1) tudo sai da cota de dano por rodada, (2) o Guia do Mestre 2014 diz que o monstro tem dano por rodada e a divisão em ataques é livre, (3) contar PE cria uma segunda economia que só o mestre opera e responde diferente em duas mesas
```

*fonte: /media/mizuki/HD Externo II/Claude/Claude 2/.claude/worktrees/projeto-m-manual-revisao-5308c5/sistema/03-mecanica/26-bestiario.md — §6.1 (linhas 253-259)*

### O §6 (o cabeçalho de onde o §6.1 pende) põe o poço de PE numa tabela de "ele não tem", ao lado de Caminho e Origem: "| poço de PE | o §6.1 |". A tabela irmã, de "ele tem", lista refino, aptidões e Pas

**Números:**
```
3 itens em "não tem": Caminho e Trilha, poço de PE, Origem
```

*fonte: /media/mizuki/HD Externo II/Claude/Claude 2/.claude/worktrees/projeto-m-manual-revisao-5308c5/sistema/03-mecanica/26-bestiario.md — §6 (linhas 236-251)*

### A ficha de inimigo do §3 tem DEZESSETE linhas e nenhuma delas é energia. "**Dezessete linhas. Nenhum número novo nasce aqui** — o que esta peça faz é dizer de onde cada um sai." As linhas são: nível, 

**Números:**
```
17 linhas, 0 de energia
```

*fonte: /media/mizuki/HD Externo II/Claude/Claude 2/.claude/worktrees/projeto-m-manual-revisao-5308c5/sistema/03-mecanica/26-bestiario.md — §3 (linhas 25-51)*

### O §6.5 — o câmbio de três portas, literal na tabela: "| **técnica e feitiço** | o **orçamento de feitiço** de uma ação dele, e o Fundamento faz o resto |", "| **aptidão e Passiva com custo por rodada*

**Números:**
```
3 portas; a porta 1 paga em ponto de feitiço, a 2 em dano por rodada, a 3 em degrau de categoria
```

*fonte: /media/mizuki/HD Externo II/Claude/Claude 2/.claude/worktrees/projeto-m-manual-revisao-5308c5/sistema/03-mecanica/26-bestiario.md — §6.5 (linhas 330-342)*

### §6.5, porta 1 — a técnica. "**O orçamento de feitiço de uma ação é o golpe dela dividido por `4,5`.**" A tabela de pontos por ação: nível 10 → Ronda 4,2 · Dupla 8,2 · Alcateia 5,6 · Calamidade 5,0; ní

**Números:**
```
1 ponto de feitiço = 4,5 de dano (peça 19 §2.1); piso Classe 1 = 3 pontos = 13,5 de dano; Dupla nv30 = 24,2 pontos contra teto de jogador 24; 95% / 96% / 101% nos níveis 20, 25 e 30
```

*fonte: /media/mizuki/HD Externo II/Claude/Claude 2/.claude/worktrees/projeto-m-manual-revisao-5308c5/sistema/03-mecanica/26-bestiario.md — §6.5, subseção "A técnica: o golpe dele é o orçamento do feitiço" (linhas 344-370)*

### §6.5, porta 2 — a aptidão, e o câmbio de PE que já tem dono. Literal: "**O jogador paga a aptidão em PE por rodada enquanto ela está de pé. O inimigo não conta PE pelo §6.1, então ele paga a mesma coi

**Números:**
```
1 PE/rodada = 5,14 de dano/rodada; Domínio Simples e Pétala (1× maior Classe) = 65% da cota de uma Ronda e 16% de uma Alcateia; Extensão de Domínio (1,5× maior Classe) = 98% da Ronda e 25% da Alcateia; no nível 2 a Extensão custa 193% da cota de uma Ronda e 96% de uma Dupla; Domínio Simples ligado 1 rodada de 3 custa 12,0 de dano = 5,5% da Alcateia e 22% da Ronda
```

*fonte: /media/mizuki/HD Externo II/Claude/Claude 2/.claude/worktrees/projeto-m-manual-revisao-5308c5/sistema/03-mecanica/26-bestiario.md — §6.5, subseção "A aptidão: ela come a cota" (linhas 372-388); a âncora de 5,14 está em /media/mizuki/HD Externo II/Claude/Claude 2/.claude/worktrees/projeto-m-manual-revisao-5308c5/sistema/03-mecanica/05-caminho-e-combate-sem-feitico.md linha 145: "| | recuperar `+1` PE | permanente | `5,14` | 1,01 | 20% |"*

### §6.5 registra que a primeira versão da conta da aptidão estava ERRADA por cobrar por luta em vez de por rodada ligada: "**⚠ E contar por luta em vez de por rodada ligada estava errado, porque as quatr

**Números:**
```
Domínio Simples ligado 1 rodada de 3 = 12,0 de dano, contra os 65%/16% da conta por luta
```

*fonte: /media/mizuki/HD Externo II/Claude/Claude 2/.claude/worktrees/projeto-m-manual-revisao-5308c5/sistema/03-mecanica/26-bestiario.md — §6.5 (linha 388)*

### §6.4 — a Expansão de Domínio do inimigo e o custo dela em PE. O trecho que trata do custo, literal: "**E abrir não custa rodada ao inimigo, apesar de custar ao jogador.** *O manual cobra a rodada inte

**Números:**
```
custo no manual para o jogador: a rodada inteira + 6 × a maior Classe de PE; acerto fora do domínio 52%; 1 ÷ 0,52 = 1,92×, que arredonda para 2; a tabela: Ronda 1→2, Dupla 2→4, Alcateia 4→8, Calamidade 6→12; duração = metade do refino, refino 10 no nível 30 = 5 rodadas contra uma luta de 3,00; a incompleta custa 0
```

*fonte: /media/mizuki/HD Externo II/Claude/Claude 2/.claude/worktrees/projeto-m-manual-revisao-5308c5/sistema/03-mecanica/26-bestiario.md — §6.4 (linhas 290-328)*

### A entrada da v0.220, item 1, é a decisão de reverter. Literal: "### 1 · A `Sobrecarga` vai ter peso, porque o inimigo VAI contar energia" — "***Decisão do Mizuki:*** *\"Sobrecarga vai ter peso pq fich

**Números:**
```
nenhum — a leva é registro, não conserto. Pedido dele com todas as letras: "N precisa corrigir essas coisas, quero q vc anote elas"
```

*fonte: /media/mizuki/HD Externo II/Claude/Claude 2/.claude/worktrees/projeto-m-manual-revisao-5308c5/logs/CHANGELOG.md — ## [0.220] — 07/09/2026, seções 1 e Decidido (linhas 11-27 e 106)*

### A v0.220 declara o PREÇO da reversão, e ele é um requisito para quem for aplicar: "**O que a reversão custa está escrito no próprio §6.1**, e quem for aplicar precisa responder: *\"contar PE de inimig

**Números:**
```
nenhum
```

*fonte: /media/mizuki/HD Externo II/Claude/Claude 2/.claude/worktrees/projeto-m-manual-revisao-5308c5/logs/CHANGELOG.md — ## [0.220], seção 1 (linhas 23 e 27)*

### A v0.220 declara explicitamente que a medida da Sobrecarga caduca com a reversão: "> **E a medida da `Sobrecarga` da v0.219 CADUCA junto.** *Ela mediu a metade da energia em `0,00` porque o inimigo nã

**Números:**
```
metade da energia da Sobrecarga = 0,00 hoje; −2 na CD = 5% do dano daquele feitiço, invariante
```

*fonte: /media/mizuki/HD Externo II/Claude/Claude 2/.claude/worktrees/projeto-m-manual-revisao-5308c5/logs/CHANGELOG.md — ## [0.220], seção 1 e Achado e não consertado (linhas 25 e 122)*

### A v0.219 mediu a Sobrecarga e a metade da energia deu ZERO por causa do §6.1. Literal: "**A entrega é *\"até o fim do próximo turno do alvo, o feitiço dele custa o dobro de energia e sai com a CD 2 me

**Números:**
```
metade da energia: 0,00 contra o bestiário; do lado do jogador 9,00 de dano por rodada SE ele pagar, 0 se conjurar Classe 0; metade da CD: −2 nega sempre 5% do dano daquele feitiço; degraus: Leve = 4 pontos na Classe 7 = 18,0 de dano; Pesada = 11 pontos = 49,5 de dano; dominância Leve 0,61× no teto e 0,20× no piso; Pesada 0,22× e 0,07×; banda das 13 condições publicadas: Leve de 0,00× (Surdo) a 2,18× (Lento), Pesada de 2,21× a 2,67×; contra-teste: para sentar no pior degrau Pesada ela teria de negar 109,4 de dano por rodada e nega 10,95 no teto — a CD teria de cair 20 pontos num d20
```

*fonte: /media/mizuki/HD Externo II/Claude/Claude 2/.claude/worktrees/projeto-m-manual-revisao-5308c5/logs/CHANGELOG.md — ## [0.219] — 07/09/2026, seções 1 e 2 (linhas 133-152)*

### A v0.205 é a primeira vez que a pergunta do PE de inimigo apareceu, e naquela vez a pesquisa MANTEVE o §6.1. Literal: "***Levantado pelo Mizuki:*** *\"não é bom ele ter justamente PE para ter recursos

**Números:**
```
recarga 5-6 do d20 dispara 1,67 vezes numa luta de 3 rodadas; a habilidade guardada custa 0 na régua (438 numa rodada e 110 nas outras duas, total 657, o publicado)
```

*fonte: /media/mizuki/HD Externo II/Claude/Claude 2/.claude/worktrees/projeto-m-manual-revisao-5308c5/logs/CHANGELOG.md — ## [0.205] — 02/09/2026, seção 5 (linhas 1434-1449); a versão longa do mesmo argumento está no §8 da peça 26 (linhas 500-508)*

### O §8 da peça 26 registra a mesma pesquisa da v0.205 em forma longa, e acrescenta uma decisão vizinha do Mizuki que limita o inimigo: "> ***E recusar um Teste de Resistência ficou de fora, por decisão 

**Números:**
```
recusa de TR = 1,17× a 1,20× de dano efetivo; resistir aos Elementais = 1,18× = meio degrau
```

*fonte: /media/mizuki/HD Externo II/Claude/Claude 2/.claude/worktrees/projeto-m-manual-revisao-5308c5/sistema/03-mecanica/26-bestiario.md — §8, item do catálogo de traços (linha 508)*

### A decisão original — v0.198, a versão em que a peça 26 nasceu. Literal: "***Decisão do Mizuki:*** **a ficha de inimigo é a ficha de personagem sem o Caminho.**" e "**E ele não conta PE: a cota de dano

**Números:**
```
nenhum
```

*fonte: /media/mizuki/HD Externo II/Claude/Claude 2/.claude/worktrees/projeto-m-manual-revisao-5308c5/logs/CHANGELOG.md — ## [0.198] — 31/08/2026, seção 8 e Decidido (linhas 2017-2019 e 2044)*

### A regra de ouro nº 6, que o §6.1 invoca como espelho: "> **Feitiço em Ação Bônus ou Reação só permite mais um de Classe 0 no turno.**" Ela é descrita como "a trava que impede o turno duplo de feitiço 

**Números:**
```
1 exceção em todo o sistema
```

*fonte: /media/mizuki/HD Externo II/Claude/Claude 2/.claude/worktrees/projeto-m-manual-revisao-5308c5/sistema/03-mecanica/03-economia-de-acao-e-iniciativa.md — §6 e §6.1 (linhas 231-247)*

### §6.2 — o projeto já tem inimigo sem energia nenhuma, e a ficha não muda de tamanho por isso: "### 6.2 E existe inimigo sem energia nenhuma" — "**Ele não tem refino, aptidão nem técnica, e a cota de da

**Números:**
```
nenhum
```

*fonte: /media/mizuki/HD Externo II/Claude/Claude 2/.claude/worktrees/projeto-m-manual-revisao-5308c5/sistema/03-mecanica/26-bestiario.md — §6.2 (linhas 261-265)*

### Existe uma dependência de CÓDIGO na frase literal do §6.1. O script lê a string exata do arquivo da peça 26 e falha se ela sumir: `SEM_PE = pega(P26, r'O inimigo não conta PE', 'o inimigo sem PE').gro

**Números:**
```
1 âncora textual; o script também lê 3 × Classe de PE, Classe 0 é grátis, e o câmbio de 5,14 da peça 5
```

*fonte: /media/mizuki/HD Externo II/Claude/Claude 2/.claude/worktrees/projeto-m-manual-revisao-5308c5/manual/matematica/sobrecarga.py — linhas 68 e 88; o desenho está descrito no CHANGELOG linha 167*

### O outro lado da assimetria — os números do orçamento de PE do JOGADOR, que são o chão da pergunta desta rodada. Do manual: "Conjurar um feitiço custa **3 × Classe** de PE, o mesmo número dos pontos de

**Números:**
```
feitiço = 3 × Classe de PE; Classe 0 = 0 PE; Técnica Máxima = 5 × maior Classe = 25/30/35 PE; Expansão = 6 × maior Classe + a rodada inteira; dia = 3 lutas × 3,5 rodadas = 10,5 rodadas; poço no nível 30 = 120 a 180 PE; o jogador conjura em 19% a 76% das rodadas do dia conforme o Caminho
```

*fonte: /media/mizuki/HD Externo II/Claude/Claude 2/.claude/worktrees/projeto-m-manual-revisao-5308c5/sistema/05-material/livro/manual/40-fundamento.md linhas 124, 144 e 961; /media/mizuki/HD Externo II/Claude/Claude 2/.claude/worktrees/projeto-m-manual-revisao-5308c5/sistema/03-mecanica/06-caminhos-e-trilhas.md linha 266; /media/mizuki/HD Externo II/Claude/Claude 2/.claude/worktrees/projeto-m-manual-revisao-5308c5/sistema/03-mecanica/11-aptidoes-e-refino.md linha 497*

### A pasta nova de trabalho já registra a pendência e a POSIÇÃO dela na fila, e ela está atrás da técnica. Do LEIA-ME: "| 1 | **a técnica de inimigo** | **o próximo.** Vem antes do PE, por decisão dele |

**Números:**
```
o PE é o item 2 da fila da Fase 1, atrás da técnica; a Fase 0 registra 2 pendências abertas (o PE e se `tamanho` carrega regra)
```

*fonte: /media/mizuki/HD Externo II/Claude/Claude 2/bestiario/LEIA-ME.md (linhas 82-83); /media/mizuki/HD Externo II/Claude/Claude 2/bestiario/00-fase-0/o-que-descartamos.md (linha 29); /media/mizuki/HD Externo II/Claude/Claude 2/bestiario/03-bloco/RASCUNHO-1-o-bloco.md (linha 102); /media/mizuki/HD Externo II/Claude/Claude 2/bestiario/00-fase-0/decisoes.md (linha 115)*

### O bestiário novo já descartou o desenho que o §6.5 pressupõe, e isso muda o que a reversão custa. A escada nova tem CINCO categorias com fator de vida e fator de dano SEPARADOS (Capanga, Ameaça, Desas

**Números:**
```
5 categorias novas contra 4 velhas; fatores de vida 0,25/0,25/1,00/1,50/2,00 e de dano 0,25/0,25/1,00/1,50/2,00 com o Capanga em vida = dano do grupo ÷ 4; ações 1/1/3/5/6; "degrau de categoria" era moeda de 3 coisas na peça velha
```

*fonte: /media/mizuki/HD Externo II/Claude/Claude 2/bestiario/LEIA-ME.md (a escada e a lista do que morreu); /media/mizuki/HD Externo II/Claude/Claude 2/bestiario/00-fase-0/o-que-descartamos.md (linhas 20-29)*

### ⚠ Não achado

Cinco buracos, e eles importam para a decisão de hoje:

1. **Nunca existiu número de PE de inimigo em lugar nenhum do projeto.** Nem proposta, nem faixa, nem fórmula. A v0.220 decidiu que ele TEM energia e parou ali, com a frase explícita "Nada foi remedido nesta leva, porque a ficha de inimigo com energia ainda não existe — e medir contra uma coisa que não foi desenhada é inventar o resultado". Não há de onde copiar.

2. **A assimetria dia-vs-luta nunca foi escrita como argumento.** As duas metades existem separadas — o lado do jogador (`3` lutas × `3,5` rodadas = `10,5` rodadas por dia, poço de `120` a `180` PE, conjura em `19%` a `76%` das rodadas conforme o Caminho) e o lado do inimigo (luta de `3,00` rodadas, `1` a `6` ações por rodada) — mas nenhum documento as põe lado a lado. A conta "quantas ações de inimigo cabem numa luta contra quantas rodadas de jogador cabem num dia" não está feita em lugar nenhum.

3. **A "segunda tabela de dano só pros feitiços" já existe e ninguém a chamou assim.** A tabela de orçamento de feitiço do §6.5 (`golpe ÷ 4,5`) é isso — só que ela é MENOR que o golpe, não maior, e não tem custo de energia. Não achei nenhuma passagem que tenha considerado a versão "maior, ao custo de energia" que o Mizuki propõe agora. É proposta nova, sem precedente no projeto.

4. **Nada mede o que o inimigo perderia se pagasse PE pelo que hoje é grátis.** O §6.4 dá a ele a Expansão sem os `6 × maior Classe` que o jogador paga, e a Técnica Máxima do manual custa `5 × maior Classe` (`25`/`30`/`35` PE) — ninguém somou esses custos contra um poço hipotético para ver se sobra luta.

5. **Zero evidência de mesa sobre isso.** A pasta `04-playtest/` do repositório está vazia desde a v0.1, e a única mesa registrada (a de ND 20, em `/media/mizuki/HD Externo II/Claude/Claude 2/bestiario/00-fase-0/mesa-nd20.md`) foi mestrada SEM ficha de inimigo, improvisando os dados — ou seja, ela não testa PE de inimigo de jeito nenhum.

Uma observação de método: não escrevi nada no repositório e não abri o `.docx` do manual com python-docx, porque tudo que a tarefa pedia estava no `40-fundamento.md` e nas peças em markdown — e a v0.219 registra que nas Melhorias o `.docx` concorda com o `partD.js`, então para a `Sobrecarga` o `.docx` não traria terceira versão.


---

## Frente 2

A economia de PE do jogador está toda publicada e reproduz. O poço é PE por nível do Caminho × nível, sem atributo e sem valor inicial (4 no Bastião, 5 na Vanguarda e no Guia, 6 no Evocador e no Emanador) — 120 a 180 PE no nível 30. Um feitiço custa 3 × Classe, confirmado nas três cópias do manual; a Liberação Máxima custa ceil(4,5 × Classe), 14 a 32 PE; a Técnica Máxima tem fórmula própria de 5 × a maior Classe, 25/30/35 por faixa; e existe um quarto preço que a pergunta não previa, a Expansão de Domínio, em 6 × a maior Classe.\n\nO número que você procurava existe e é 10,5 rodadas de luta por dia, mas ele não é regra escrita: é 3 lutas (peça 10 §4, a exaustão dispara da quarta) vezes 3,5 rodadas (peça 1 §8, 'o manual promete 3,5'), calculado dentro do conferir-orcamento.py e citado de lá por todo mundo. A frase sobre metade das rodadas é literal e está no manual publicado, dentro de uma caixa chamada 'ESSA ÚLTIMA COLUNA É UM TETO, E NÃO UM DIA': 'Na prática, um conjurador gasta PE em cerca de metade das rodadas de luta do dia e passa a outra metade no Classe 0, no golpe simples e no que for de graça. Isso não é aperto: é o desenho.'\n\nNa prática, o conjurador tem entre 0,76 e 17,14 PE por rodada de luta conforme nível e Caminho — que dá 0,25 a 0,82 feitiço por rodada, e é isso que produz a taxa publicada de 38% a 76%. Numa luta de 3 rodadas isolada, o nível 30 orça 1,9 (Bastião) a 2,9 (Emanador) feitiços.\n\nA Classe 0 muda a conta inteira: ela é grátis e vale 29% a 33% do feitiço pago em quase toda a campanha, então o PE nunca compra o dano — compra o delta. O dano nominal por PE é constante em 4,50, mas o dano MARGINAL sobre a Classe 0 é 3,00 a 3,21 do nível 10 em diante. Uma rodada meia-a-meia entrega 56% a 60% da Rotina.\n\nDois achados que a pergunta não pedia e que mexem na decisão. Primeiro: a peça 10 §6 publica um orçamento de dia de 1,50 × pool para 3 lutas (os dois descansos curtos de 25% cada), e o validador que produz a taxa de 38%-76% ignora isso — com o número da própria peça 10, a taxa vai a 57%-100% e o conjurador de nível 20+ deixa de ser escasso. Segundo: a regra viva hoje é 'O inimigo não conta PE' (peça 26 §6.1), e ela sustenta pelo menos três outras linhas do bestiário e a medição inteira da Melhoria Sobrecarga.

### PE máximo = PE por nível do Caminho × nível. Sem atributo, sem valor inicial — é a única reserva do sistema que é uma linha reta pela origem (a vida soma Constituição e escala em nível−1; a Integridad

**Números:**
```
PE por nível: Bastião 4 · Vanguarda 5 · Guia 5 · Evocador 6 · Emanador 6.
Poço por nível (Bastião / Vanguarda-Guia / Evocador-Emanador):
nv2  8 / 10 / 12
nv5  20 / 25 / 30
nv10 40 / 50 / 60
nv13 52 / 65 / 78
nv17 68 / 85 / 102
nv20 80 / 100 / 120
nv26 104 / 130 / 156
nv30 120 / 150 / 180
```

*fonte: /media/mizuki/HD Externo II/Claude/Claude 2/.claude/worktrees/projeto-m-manual-revisao-5308c5/sistema/05-material/livro/manual/35-caminhos-e-trilhas.md:36-38 (tabela e regra) · sistema/03-mecanica/01-atributos-acerto-defesa.md:82,193,380 (§5.3, a fórmula) · sistema/03-mecanica/06-caminhos-e-trilhas.md:335-336,345*

### O manual publica a linha do conjurador em 6 PE por nível — que é exatamente o Evocador/Emanador. A peça 1 §5.3 diz explicitamente que o manual NÃO é autoridade aqui, só não contradiz.

**Números:**
```
Tabela do manual: nv1=6 · nv5=30 · nv9=54 · nv13=78 · nv17=102 · nv20=120. Coluna 'quantas vezes você lança o seu melhor feitiço': 2 · 5 · 6 · 6 · 6 · 8.
```

*fonte: /media/mizuki/HD Externo II/Claude/Claude 2/.claude/worktrees/projeto-m-manual-revisao-5308c5/sistema/05-material/livro/manual/40-fundamento.md:128-141 · manual/gerador/partA.js:139-150 · manual/Fundamento-MANUAL-v7.docx (tabela 'Nível | PE total | Maior Classe | Custo | Quantas vezes você lança o seu melhor feitiço') · a ressalva em sistema/03-mecanica/01-atributos-acerto-defesa.md:387*

### CONFIRMADO: conjurar custa 3 × Classe de PE, o mesmo número dos pontos. Classe 0 é grátis. A frase está idêntica nas três cópias (livro .md, gerador, .docx).

**Números:**
```
Maior Classe por nível: C1@nv1 · C2@nv5 · C3@nv9 · C4@nv13 · C5@nv17 · C6@nv21 · C7@nv26 (40-fundamento.md:95, coluna Nível).
Custo do feitiço da maior Classe: 3 · 6 · 9 · 12 · 15 · 18 · 21 PE.
```

*fonte: /media/mizuki/HD Externo II/Claude/Claude 2/.claude/worktrees/projeto-m-manual-revisao-5308c5/sistema/05-material/livro/manual/40-fundamento.md:88,124,427 · manual/gerador/partA.js:135 · manual/Fundamento-MANUAL-v7.docx parágrafo 53*

### Liberação Máxima custa 50% a mais que a Classe dela, arredondando para cima — ou seja ceil(4,5 × Classe). O manual dá o exemplo fechado: Classe 5 = 15 + 50% = 22,5 → 23.

**Números:**
```
C3=14 · C4=18 · C5=23 · C6=27 · C7=32 PE.
Come do poço: nv10 Bastião 35% / Emanador 23%; nv20 29% / 19%; nv30 27% / 18%.
Custa a rodada inteira, mais um preço na hora (Vazio, Sangue ou Peso). São 3 no total: nv10, nv20, nv30.
```

*fonte: /media/mizuki/HD Externo II/Claude/Claude 2/.claude/worktrees/projeto-m-manual-revisao-5308c5/sistema/05-material/livro/manual/40-fundamento.md:126,930,942 · manual/gerador/partA.js:136 · manual/Fundamento-MANUAL-v7.docx parágrafo 54*

### Técnica Máxima tem fórmula PRÓPRIA — não é 3 × Classe: custa 5 × a sua maior Classe. Recarrega depois do fim do terceiro turno seguinte.

**Números:**
```
Faixa 17-20: 24d8 = 108 de dano, 8 pontos de montagem, 25 PE.
Faixa 21-25: 28d8 = 126, 8 pontos, 30 PE.
Faixa 26-30: 32d8 = 144, 12 pontos, 35 PE.
Come do poço no nv30: Bastião 29%, Emanador 19%.
```

*fonte: /media/mizuki/HD Externo II/Claude/Claude 2/.claude/worktrees/projeto-m-manual-revisao-5308c5/sistema/05-material/livro/manual/40-fundamento.md:126,952,961,969 · manual/Fundamento-MANUAL-v7.docx parágrafos 55 e 258*

### Existe um quarto preço em PE que a pergunta não cobriu: a Expansão de Domínio custa 6 × a maior Classe, e lá dentro os feitiços ficam mais baratos.

**Números:**
```
6 × maior Classe: C3=18 · C5=30 · C6=36 · C7=42 PE. Custa a rodada inteira. Dentro: −1/3 do refino de PE na incompleta, −metade do refino na completa, e nenhum feitiço custa menos de 1 PE. Dura metade do refino em rodadas, mínimo 1.
Come do poço no nv30: Bastião 35%, Emanador 23%.
```

*fonte: /media/mizuki/HD Externo II/Claude/Claude 2/.claude/worktrees/projeto-m-manual-revisao-5308c5/sistema/05-material/livro/manual/40-fundamento.md:1026-1030 · manual/Fundamento-MANUAL-v7.docx parágrafo 285*

### O NÚMERO PUBLICADO É 10,5 RODADAS DE LUTA POR DIA, e ele é derivado, não escrito: 3 lutas × 3,5 rodadas. As duas metades têm dono separado.

**Números:**
```
LUTAS_DE_GRACA = 3 · RODADAS_POR_LUTA = 3,5 → 10,5.
Literal da peça 10 §4: 'Da quarta luta do dia em diante, cada luta dá um degrau de exaustão. Máximo de três.' e 'As três primeiras lutas do dia são de graça.'
Literal da peça 1: 'o combate durava 4,7 rodadas onde o manual promete 3,5'.
O próprio validador imprime: 'Um dia normal tem 3 lutas de graca (a exaustao dispara da quarta) e cada luta dura ~3.5 rodadas: 10.5 rodadas de luta por dia.'
```

*fonte: /media/mizuki/HD Externo II/Claude/Claude 2/.claude/worktrees/projeto-m-manual-revisao-5308c5/sistema/03-mecanica/conferir-orcamento.py:53-55 e 131-138 (o cálculo) · as 3 lutas em sistema/03-mecanica/10-descanso-e-recuperacao.md:84 · as 3,5 rodadas em sistema/03-mecanica/01-atributos-acerto-defesa.md:216 · republicado em sistema/03-mecanica/06-caminhos-e-trilhas.md:266 e sistema/ESTADO-ATUAL.md:281*

### A FRASE LITERAL sobre gastar PE em metade das rodadas — ela mora numa caixa do manual chamada 'ESSA ÚLTIMA COLUNA É UM TETO, E NÃO UM DIA', e a caixa inteira é um aviso contra usar o poço como orçamen

**Números:**
```
Citação literal, as três linhas da caixa:
1) 'Ela responde "quantas vezes cabe se você não fizer mais nada com o seu PE". Um dia de verdade tem outras despesas ao mesmo tempo — o sistema em volta tem coisas que cobram por rodada enquanto estão ligadas, e a Integridade encarece todo feitiço quando o seu segundo degrau acende.'
2) 'Na prática, um conjurador gasta PE em cerca de metade das rodadas de luta do dia e passa a outra metade no Classe 0, no golpe simples e no que for de graça. Isso não é aperto: é o desenho.'
3) 'Leia esta coluna como o limite superior. Quem trata ela como orçamento de dia acaba precificando peça nova contra um personagem que só faz uma coisa — e esse erro já custou três versões do sistema em volta.'
```

*fonte: /media/mizuki/HD Externo II/Claude/Claude 2/.claude/worktrees/projeto-m-manual-revisao-5308c5/manual/gerador/partA.js:152-156 · a mesma caixa está no manual publicado: manual/Fundamento-MANUAL-v7.docx (célula de tabela) · citada em logs/CHANGELOG.md:139 e 7160*

### A TAXA DE CONJURAÇÃO PUBLICADA (poço nu, sem descanso): o Bastião conjura em 38% a 48% das 10,5 rodadas; Emanador 57% a 76%. É a régua contra a qual todo compromisso novo do sistema é medido.

**Números:**
```
nv / Classe / custo → Bastião | Vanguarda-Guia | Evocador-Emanador
10 / C3 /  9 → 4x=38% | 5x=48% | 6x=57%
14 / C4 / 12 → 4x=38% | 5x=48% | 7x=67%
18 / C5 / 15 → 4x=38% | 6x=57% | 7x=67%
22 / C6 / 18 → 4x=38% | 6x=57% | 7x=67%
26 / C7 / 21 → 4x=38% | 6x=57% | 7x=67%
30 / C7 / 21 → 5x=48% | 7x=67% | 8x=76%
O invariante escrito: falha se cair abaixo de 25% ('o personagem já passa o dia sem poder conjurar') ou passar de 90% ('o PE parou de ser recurso escasso').
```

*fonte: /media/mizuki/HD Externo II/Claude/Claude 2/.claude/worktrees/projeto-m-manual-revisao-5308c5/sistema/03-mecanica/conferir-orcamento.py bloco 1 (rodado agora, saída reproduzida) · republicado em sistema/03-mecanica/06-caminhos-e-trilhas.md:266 e sistema/ESTADO-ATUAL.md:281*

### DIVERGÊNCIA ENCONTRADA: o validador calcula essa taxa contra o poço NU, mas a peça 10 §6 publica um orçamento de dia de 1,50 × poço para 3 lutas (os dois descansos curtos entre elas). Com o número da 

**Números:**
```
Tabela literal da peça 10 §6: 1 luta = o pool · 2 lutas = 1,25 × pool · 3 lutas = 1,50 × pool · 4 lutas = 1,75 × pool, e aqui a exaustão entra.
Refeita a conta com 1,50 × pool sobre 10,5 rodadas:
nv10 → Bastião 57% | Vanguarda-Guia 76% | Evocador-Emanador 95%
nv20 → Bastião 76% | 95% | 100% (12 feitiços cabem em 10,5 rodadas)
nv30 → Bastião 76% | 95% | 100%
PE por rodada de luta no nv30: Bastião 17,1 · Vanguarda-Guia 21,4 · Evocador-Emanador 25,7.
```

*fonte: /media/mizuki/HD Externo II/Claude/Claude 2/.claude/worktrees/projeto-m-manual-revisao-5308c5/sistema/03-mecanica/10-descanso-e-recuperacao.md:~213 (§6, 'O orçamento de missão') · contra sistema/03-mecanica/conferir-orcamento.py:114-116 (a função bolso(), que é só PE_POR_NIVEL × nível)*

### PE SOBRANDO POR RODADA DE LUTA, na prática (poço nu ÷ 10,5). É o número bruto que o inimigo teria que espelhar se você quiser 'gastar energia com peso'.

**Números:**
```
nv / Classe / custo 3C → PE por rodada (Bastião | Vang-Guia | Evoc-Eman), e quanto isso é de feitiço:
2  / C1 /  3 → 0,76 (0,25 feit.) | 0,95 (0,32) | 1,14 (0,38)
10 / C3 /  9 → 3,81 (0,42) | 4,76 (0,53) | 5,71 (0,63)
14 / C4 / 12 → 5,33 (0,44) | 6,67 (0,56) | 8,00 (0,67)
18 / C5 / 15 → 6,86 (0,46) | 8,57 (0,57) | 10,29 (0,69)
22 / C6 / 18 → 8,38 (0,47) | 10,48 (0,58) | 12,57 (0,70)
26 / C7 / 21 → 9,90 (0,47) | 12,38 (0,59) | 14,86 (0,71)
30 / C7 / 21 → 11,43 (0,54) | 14,29 (0,68) | 17,14 (0,82)
A fatia de UMA luta (poço ÷ 3 lutas), nv30: Bastião 40 PE = 1,9 feitiços; Emanador 60 PE = 2,9 feitiços — numa luta de 3 rodadas.
```

*fonte: conta feita agora sobre PE por nível (35-caminhos-e-trilhas.md:36) e 10,5 rodadas (conferir-orcamento.py:138). Script em /tmp/claude-1000/-media-mizuki-HD-Externo-II-Claude-Claude-2--claude-worktrees-projeto-m-manual-revisao-5308c5/24d61e43-2625-4da1-86ad-6a4f1d047250/scratchpad/pe.py*

### O QUE A CLASSE 0 MUDA: ela é o piso grátis, e por isso o PE do jogador nunca compra o dano inteiro — compra só o DELTA sobre o Classe 0. O dano por PE nominal é constante em 4,50 (a média do d8), mas 

**Números:**
```
Classe 0 por nível — quantos você tem / dano: nv1: 2 / 2d8=9 · nv5: 3 / 3d8=13,5 · nv11: 4 / 4d8=18 · nv17: 5 / 5d8=22,5 · nv25: 5 / 6d8=27.
nv / feitiço da maior Classe / Classe 0 / Classe 0 como % do feitiço / DANO MARGINAL POR PE:
2  / 3d8=13,5  / 2d8=9    / 67% / 1,50
5  / 6d8=27    / 3d8=13,5 / 50% / 2,25
10 / 9d8=40,5  / 3d8=13,5 / 33% / 3,00
14 / 12d8=54   / 4d8=18   / 33% / 3,00
20 / 15d8=67,5 / 5d8=22,5 / 33% / 3,00
30 / 21d8=94,5 / 6d8=27   / 29% / 3,21
Rotina do manual para comparar: nv2=13 · nv10=45 · nv20=76 · nv30=108.
Rodada média meia-a-meia (metade feitiço, metade Classe 0): nv2=11,2 · nv10=27,0 · nv20=45,0 · nv30=60,8 — contra Rotinas de 13, 45, 76 e 108.
```

*fonte: /media/mizuki/HD Externo II/Claude/Claude 2/.claude/worktrees/projeto-m-manual-revisao-5308c5/sistema/05-material/livro/manual/40-fundamento.md:142-156 (a seção Classe 0) e :95 (dano do feitiço por Classe) · manual/gerador/partA.js:158-168 · a tabela de Rotina em manual/gerador/partF.js:191-199*

### RECUPERAÇÃO DE PE — descanso curto devolve 25% do máximo, em qualquer lugar; descanso longo devolve tudo em ambiente propício e metade do máximo fora dele. Vida não volta no curto.

**Números:**
```
Descanso curto: PE 25% do máximo · Vida nada · usos 'por descanso curto' recarregam.
Descanso longo, propício: PE cheio, vida cheia, exaustão zera, Integridade cheia. Fora dele: PE metade do MÁXIMO (nunca metade do que sobrou), vida metade do máximo, exaustão não zera.
Frações arredondam para baixo, e o que se recupera nunca fica abaixo de 1 — exceto onde a tabela escreve zero (degrau 3 de exaustão devolve nada).
25% no respiro, nv30: Bastião 30 · Vanguarda-Guia 37 (de 37,5) · Evocador-Emanador 45.
Exaustão corta o curto fora de ambiente propício, degrau a degrau até nada; em ambiente propício os 25% valem em qualquer degrau.
```

*fonte: /media/mizuki/HD Externo II/Claude/Claude 2/.claude/worktrees/projeto-m-manual-revisao-5308c5/sistema/05-material/livro/manual/70-descanso-e-recuperacao.md:33-70 · sistema/03-mecanica/10-descanso-e-recuperacao.md:41-70*

### Existem cinco válvulas publicadas que mexem no poço ou no preço, e vale saber que existem antes de fixar o número do inimigo.

**Números:**
```
Reserva Profunda (Passiva Classe 3): PE máximo sobe em 3 × a maior Classe (+21 no nv30, que é 18% do poço do Bastião).
Segunda Natureza (Passiva Classe 2): 1× por DIA, conjura feitiço de Classe até metade da maior sem gastar PE.
Eco (Passiva Classe 2): ao derrubar um inimigo com feitiço, o próximo feitiço da cena custa metade.
Braseiro (Bastião, nv11): quando o Classe 0 acerta, +2 de energia temporária, teto 2, some no fim da cena.
Integridade no degrau 2: todo feitiço custa +1 PE por Classe (no nv30 isso é 21 → 28 PE, +33%).
Projetar energia: gasta PE ≤ refino, cada 1 PE = +1d6 de dano.
O CÂMBIO PUBLICADO: '+1 PE permanente' vale 5,14 de dano por rodada; '+1 PE 1× por descanso curto' vale 1,54.
```

*fonte: /media/mizuki/HD Externo II/Claude/Claude 2/.claude/worktrees/projeto-m-manual-revisao-5308c5/sistema/05-material/livro/manual/40-fundamento.md:325,326,332 · sistema/05-material/livro/manual/70-descanso-e-recuperacao.md:118 · sistema/05-material/livro/manual/35-caminhos-e-trilhas.md:160 · sistema/05-material/livro/manual/45-aptidoes-e-refino.md:164 · sistema/03-mecanica/05-caminho-e-combate-sem-feitico.md (tabela §4, linha 'recuperação')*

### CONTEXTO DE ATRITO: a regra publicada hoje é que o inimigo NÃO conta PE, e a peça 26 usa isso em pelo menos dois lugares para converter custo em cota de dano.

**Números:**
```
§6.1 'O inimigo não conta PE, e a cota de dano é o orçamento dele'.
:326 — sobre a Expansão: 'abrir não custa rodada ao inimigo, apesar de custar ao jogador... o inimigo não conta PE pelo §6.1... A cota daquela rodada sai pelo Acerto em vez de sair pelos golpes'.
:374 — 'O jogador paga a aptidão em PE por rodada enquanto ela está de pé. O inimigo não conta PE pelo §6.1, então ele paga a mesma coisa na cota'.
E o manual/matematica/sobrecarga.py:76 ancora nisso: a Melhoria Sobrecarga vale ZERO do jogador contra o inimigo, porque 'Não existe alvo no bestiário inteiro'.
```

*fonte: /media/mizuki/HD Externo II/Claude/Claude 2/.claude/worktrees/projeto-m-manual-revisao-5308c5/sistema/03-mecanica/26-bestiario.md:253 (§6.1, o título), :326 e :374*

### ⚠ Não achado

Três coisas.\n\n1. NÃO EXISTE, em lugar nenhum do repositório, um número publicado de 'PE do inimigo' nem uma segunda tabela de dano para feitiço. A decisão da v0.220 que o LEIA-ME cita como 'nunca aplicada' não deixou número nenhum atrás dela — grep por 'PE do inimigo' e por qualquer poço de energia de monstro dá zero. A regra viva é o oposto: peça 26 §6.1, 'O inimigo não conta PE'.\n\n2. A frase '10,5 rodadas de luta do dia' NÃO está escrita no manual nem em nenhuma peça como regra. Ela é sempre CITADA como saída do bloco 1 do conferir-orcamento.py, que a calcula de duas âncoras que moram em peças diferentes (3 lutas na peça 10 §4, 3,5 rodadas na peça 1 §8). Se você quiser que 10,5 seja uma régua do bestiário, ela precisa virar linha escrita em algum lugar, porque hoje ela é um produto de validador.\n\n3. NÃO ACHEI conciliação entre as duas leituras do orçamento de dia. A peça 10 §6 publica 1,50 × pool para 3 lutas; o conferir-orcamento.py mede a taxa contra 1,00 × pool. Nenhum dos dois documentos cita o outro, e nenhum validador cruza os dois. Isso não é erro de conta — é uma escolha de modelo que ninguém declarou, e ela move a taxa de conjuração do Emanador de 76% para 100%. Antes de calibrar o poço do inimigo contra 'a régua do jogador', vale o Mizuki dizer qual das duas é a régua.\n\nBônus de atrito com o bestiário: a Fase 1 fixou a luta padrão em 3 rodadas, e o orçamento de PE do jogador supõe 3,5. Com 3, o dia tem 9 rodadas e toda taxa acima sobe ~17%.


---

## Frente 3

Pesquisa de campo sobre o que faz um recurso ter peso na mesa, com foco no caso do inimigo de UMA luta de 3 rodadas. Três conclusões que atravessam todas as fontes: (1) A literatura de attrition é unânime em dizer que o peso do gasto mora FORA do encontro — na próxima luta, na decisão de avançar ou recuar. O inimigo não tem "fora do encontro". Então, se você der um pool de dia ao inimigo, ele vira formalidade por construção: é a definição literal do "nova problem" ("recurso alimentado por tempo, sem pressão de tempo, é efetivamente de graça" — bankuei). O inimigo está SEMPRE em nova. (2) Os sistemas que resolveram isso não deram pool maior nem menor — trocaram o DENOMINADOR. Draw Steel dá Malice por rodada (heróis + número da rodada), e o custo das habilidades é calibrado contra a renda de UMA rodada, não contra o total da luta: as features de Rival custam 3, 5, 7 e 10, numa renda de 6-7-8-9 por rodada. Ou seja, o inimigo pode pagar mais ou menos uma coisa grande por rodada, e economizar duas rodadas compra a maior. Isso é medida direta e aproveitável. (3) O modo de falha que você teme tem nome e diagnóstico publicado: o chefe que despeja tudo na abertura e depois fica esperando recarga. O Angry GM descreve exatamente isso ("o solo passa a maior parte das rodadas esperando recharge") e a solução convergente de todo mundo — Colville, Sly Flourish, Angry GM, Draw Steel — é a mesma: o pico do inimigo vai no FIM, não no começo, e o recurso é distribuído por relógio de rodada, não por pool livre. Números de fração que dá pra usar: no 5e, o feitiço mais caro que um conjurador pode lançar custa entre 9,8% e 18,5% do pool do DIA (variante de Pontos de Feitiço, DMG p.289), convergindo pra ~12% — que é aproximadamente 1 dos 6-8 encontros do dia. E o que a divulgação descreve como "nova que te deixa racionando" é 55% do pool numa luta só.

### Attrition só vira decisão quando o resultado do cenário não depende de ganhar cada encontro, e sim da EFICIÊNCIA com que o grupo resolve cada um. Cada encontro isolado é quase infalível; o que decide 

**Números:**
```
Sem número. Argumento estrutural.
```

*fonte: The Angry GM — "Maybe You Just Don't GET Attrition": https://theangrygm.com/you-dont-get-attrition/*

### Sem attrition, nunca há razão para evitar um encontro, procurar um atalho ou recuar. O peso do gasto mora nas escolhas ENTRE encontros, não dentro deles.

**Números:**
```
O texto explicitamente NÃO dá percentual nem 'tamanho de mordida' por encontro. Ele recusa a pergunta numérica.
```

*fonte: The Angry GM — "Office Hours: Is Attrition Inertia?": https://theangrygm.com/office-hours-is-attrition-inertia/*

### Custo só produz decisão significativa quando há consideração e trade-off; é o sistema de recurso que sustenta isso. Sem trade-off, o custo é contabilidade.

**Números:**
```
Sem número. (Aviso: o site devolveu 403 na leitura direta; o trecho veio do índice de busca, não do corpo do artigo.)
```

*fonte: Flesh and Blood TCG — "Designer: The Cost of Meaningful Decisions": https://fabtcg.com/articles/designer-cost-meaningful-decisions/*

### Armadilha do acumulador (hoarder trap): se o recurso é caro e limitado, o jogador guarda pra 'quando precisar' e nunca usa. Se é barato e abundante, ele usa. Designers modernos deixam consumível barat

**Números:**
```
Sem número.
```

*fonte: Game Wisdom — "Avoiding the Hoarder Trap in Game Design": https://game-wisdom.com/critical/hoarder-trap-game-design e https://www.gamedeveloper.com/design/avoiding-the-hoarder-trap-in-game-design*

### Nova = despejar recurso limitado numa rodada só para dano/efeito enorme, algo que não pode ser repetido porque consome recurso diário. É definido em oposição a DPR sustentado.

**Números:**
```
Sem número.
```

*fonte: D&D4 Wiki — "Nova": https://dnd4.fandom.com/wiki/Nova*

### O nova problem existe porque a mecânica DEVERIA oferecer a escolha entre usar o poder agora ou guardar pra depois — e quando não há pressão sobre o 'depois', a escolha some. A frase central: recursos 

**Números:**
```
Sem número. As duas saídas propostas: reintroduzir pressão de tempo, ou alimentar o poder com algo que NÃO seja tempo.
```

*fonte: Deeper in the Game (bankuei) — "The Nova Problem / 15 minute adventuring day": https://bankuei.wordpress.com/2014/12/13/the-nova-problem-15-minute-adventuring-day/*

### O 'dia de aventura de cinco minutos' é descansar depois de uma ou duas lutas. Isso elimina virtualmente o aspecto de gestão de recurso do jogo, porque o personagem entra em toda luta podendo usar tudo

**Números:**
```
1 a 2 encontros por descanso longo (contra os 6-8 de projeto).
```

*fonte: M.T. Black Games — "The Five-Minute Adventuring Day": https://www.mtblackgames.com/blog/five-minute*

### O 5e é projetado como jogo de desgaste: 6 a 8 encontros médios/difíceis por descanso longo, e classes com recuperação lenta (Guerreiro, Bruxo) rendem mal quando só há um encontro antes do descanso.

**Números:**
```
6 a 8 encontros por dia. Logo, o orçamento de UM encontro ≈ 1/6 a 1/8 do pool do dia ≈ 12,5% a 16,7%.
```

*fonte: DMG p.84, via The DM Lair — https://thedmlair.com/blogs/news/how-to-use-the-adventuring-day-rules-in-d-d-5e e EN World — https://www.enworld.org/threads/the-adventuring-day-has-nothing-to-do-with-encounter-balance.697146/*

### Na variante oficial de Pontos de Feitiço do 5e (DMG p.289), o feitiço mais caro que um conjurador consegue lançar consome uma fatia surpreendentemente pequena do pool do dia — e a fatia CAI conforme o

**Números:**
```
Nível 5: 27 pontos, feitiço mais caro (3º) = 5 → 18,5% do pool. Nível 9: 57 pontos, 5º = 7 → 12,3%. Nível 11: 73 pontos, 6º = 9 → 12,3%. Nível 17: 107 pontos, 9º = 13 → 12,1%. Nível 20: 133 pontos, 9º = 13 → 9,8%. Faixa: 9,8% a 18,5%, convergindo pra ~12%.
```

*fonte: Tabela completa em D&D 5e Wikidot — https://dnd5e.wikidot.com/spell-points (custos: 1º=2, 2º=3, 3º=5, 4º=6, 5º=7, 6º=9, 7º=10, 8º=11, 9º=13)*

### O que a divulgação de 5e descreve como o gasto que DÓI de verdade é bem maior que o gasto de um feitiço só: gastar três espaços de 3º nível na primeira luta te deixa racionando truques pelas cinco lut

**Números:**
```
3 espaços de 3º = 15 dos 27 pontos de um nível 5 = 55,6% do pool numa luta só. Mago: 15+ espaços/dia. Bruxo: 2-4 espaços/encontro, com recuperação em 1 hora.
```

*fonte: Storyroll — "D&D Spell Slots Explained": https://storyroll.app/blog/spell-slots-explained (frases verificadas no corpo do texto)*

### Draw Steel troca o pool de dia por RENDA por rodada: o Diretor ganha Malice igual ao número de heróis mais o número da rodada, no início de cada rodada, mais uma injeção inicial igual à média de Vitór

**Números:**
```
Exemplo oficial: 5 heróis com 3 Vitórias cada, rodada 1 → começa com 9 Malice (3 de Vitórias + 5 de heróis + 1 da rodada). Na rodada 3 ganha 8, na rodada 4 ganha 9. Numa mesa de 5, a renda pura por rodada é 6, 7, 8, 9…
```

*fonte: Steel Compendium — Monster Basics: https://steelcompendium.io/compendium/main/Bestiary/Monsters/Chapters/Monster%20Basics/*

### Os custos reais em Malice são calibrados contra a renda de UMA rodada, não contra o total da luta. As features de Malice de Rival (nível 1+) custam 3, 5, 7 e 10.

**Números:**
```
Custos: Work as One = 3 · We Just Do It Better = 3 · Check Out Our Loot = 5 · Calling the Shots = 7 · Coordinated Takedown = 10. Contra uma renda de 6/7/8 por rodada numa mesa de 5: a mais barata = ~43% de uma rodada de renda; a mais cara = ~125-140% de uma rodada. Sobre o total de 3 rodadas (21 de renda): 14% a 48%.
```

*fonte: Steel Compendium — Rival Malice (Level 1+ Malice Features): https://steelcompendium.io/v2/Browse/monster/rival/rival-malice-level-1-malice-features/*

### A vantagem declarada do recurso que cresce é que o inimigo continua ameaçador no fim da luta, quando o pool que só encolhe já teria secado — inclusive quando sobrou um goblin só.

**Números:**
```
O review relata começar combate com 7 a 10 de Malice e ganhar mais a cada rodada.
```

*fonte: MCDM / Draw Steel: Monsters, resumido em https://shop.mcdmproductions.com/products/draw-steel-monsters-pdf e review em https://gamingtrend.com/reviews/draw-steel-monsters-review/*

### Em Draw Steel os heróis TAMBÉM ganham recurso por rodada — os dois lados sobem juntos, e a batalha fica mais interessante rodada a rodada em vez de menos.

**Números:**
```
Sem número exato por classe nas fontes que abri.
```

*fonte: Steel Compendium / Draw Steel Heroes, via https://shop.mcdmproductions.com/products/draw-steel-core-rules-bundle-pdf e https://steelcompendium.io/compendium/main/Rules/Chapters/Combat/*

### Villain actions em Draw Steel não são pool: são relógio. Toda criatura solo/líder tem SEMPRE três, cada uma usável uma vez por encontro, no máximo uma por rodada.

**Números:**
```
3 villain actions, 1x cada por encontro, máximo 1 por rodada. Uma criatura solo aguenta seis heróis do mesmo nível.
```

*fonte: Steel Compendium — Monster Basics: https://steelcompendium.io/compendium/main/Bestiary/Monsters/Chapters/Monster%20Basics/*

### Villain actions de Colville são explicitamente amarradas ao número da rodada, e o dimensionamento parte da duração observada do combate. A frase de referência: muitos combates de 5e duram três rodadas

**Números:**
```
3 rodadas → 3 villain actions. O autor, que prefere lutas de 5 rodadas, espaça nas rodadas 1, 3 e 5.
```

*fonte: RJD20 — "My Take on Matthew Colville's 5E Action Oriented Monsters": https://www.rjd20.com/2019/10/my-take-on-matthew-colvilles-5e-action.html (frase verificada no corpo) · vídeo original: https://www.youtube.com/watch?v=Xua9kgK9W1Q*

### A distribuição recomendada do poder do chefe é crescente, não decrescente: rodada 1 posicionar, rodada 2 sair da enrascada, rodada 3 explodir e fazer os personagens se arrependerem.

**Números:**
```
Estrutura de 3 rodadas, uma função por rodada.
```

*fonte: Sly Flourish — "Improvising Colville-style Action Oriented Monsters in D&D": https://slyflourish.com/action_oriented_monsters.html*

### Diagnóstico do chefe que gasta tudo cedo: os dois lados abrem despejando os melhores poderes. O grupo esgota rápido o que tem de bom e passa o resto da luta em ataques básicos; o solo passa a maior pa

**Números:**
```
Comparação de economia de ação: um encontro normal tem pelo menos 5 ações padrão e 5 de movimento por rodada; o solo não chega perto.
```

*fonte: The Angry GM — "The D&D Boss Fight (Part 1)": https://theangrygm.com/the-dd-boss-fight-part-1/*

### Luta contra solo tem só dois marcos de progresso (o monstro fica ensanguentado, o monstro morre), contra vários marcos de um encontro normal. Por isso vira moagem.

**Números:**
```
2 marcos contra ~5 (um por inimigo derrubado).
```

*fonte: EN World — "The 4e Solo Thread": https://www.enworld.org/threads/the-4e-solo-thread.350797/ e "Killing the grind: phased boss fights": https://www.enworld.org/threads/killing-the-grind-phased-boss-fights.265682/*

### A tentativa de consertar solo com mais vida falhou de forma medida: os solos do Monster Manual 2 saíram com cerca de 20% menos pontos de vida que os do MM1, e a matemática de encontro foi refeita de n

**Números:**
```
~20% menos HP no MM2; ~100 pontos de vida a menos em números absolutos; revisão completa da matemática no MM3.
```

*fonte: EN World — "Monster Manual 2 and Elite/Solo design": https://www.enworld.org/threads/monster-manual-2-and-elite-solo-design.256505/*

### Relato de mesa: um mestre subiu o chefe de ~240 para ~2000 pontos de vida pra ele durar, e mesmo assim virou saco de pancada, porque o problema não era durabilidade.

**Números:**
```
240 → 2000 HP (8,3x).
```

*fonte: Handbook of Heroes — "Solo Boss Monster" (comentários): https://www.handbookofheroes.com/archives/comic/solo-boss-monster*

### Estrutura de chefe recomendada quando o problema é o pico na abertura: três estágios, cada um com um terço da vida, cada estágio vivendo de duas a três rodadas, com um poder novo por estágio em vez de

**Números:**
```
3 estágios × 1/3 da vida × 2-3 rodadas cada.
```

*fonte: The Angry GM — "The D&D Boss Fight (Part 4)": https://theangrygm.com/the-dd-boss-fight-part-4/*

### Dado de escalada do 13th Age: começa em 1 na segunda rodada, sobe +1 por rodada até +6, e vale SÓ pros personagens — monstro não soma. Efeito relatado pelos designers: combates mais curtos, mais dramá

**Números:**
```
+1 por rodada, começando na rodada 2, teto +6. Só PCs.
```

*fonte: Pelgrane Press — "13th Sage: Secret Origins of the Escalation Die": https://pelgranepress.com/2015/11/13/13th-sage-secret-origins-of-the-escalation-die/ · regra: https://www.13thagesrd.com/combat-rules/ · adaptação: https://slyflourish.com/escalation.html*

### Heat do Lancer é recurso E risco na mesma variável: o piloto empurra o reator pra ter saída extra, e passar do teto reseta o calor e força rolagem na tabela de Stress; a zero de stress vem o derretime

**Números:**
```
NPC padrão: 1 de stress. Estourar o Heatcap zera o calor e força check.
```

*fonte: LANCER Wiki — Stress: https://lancer.wiki.gg/wiki/Stress · resumo: https://advancedrpgs.com/lancer-rpg-spotlight-tactical-mech-combat-licenses-and-mission-first-campaigns/ · regras: https://lancer-rules.carrd.co/*

### No sistema 2d20 (Conan, Star Trek), o mestre tem um pool próprio — Doom, Threat, Dark Symmetry — que é alimentado em parte pelos PRÓPRIOS jogadores: o jogador pode dar Doom ao mestre pra gerar Momentu

**Números:**
```
Sem valores fixos nas fontes abertas; é pool corrente, não por rodada.
```

*fonte: Starships & Steel — "Conan 2d20 RPG Overview: Doom & Momentum": https://www.starshipsandsteel.com/2018/04/conan-2d20-rpg-overview-doom-momentum.html · Roll20 fórum: https://app.roll20.net/forum/post/10160523/conan-2d20-momentum-and-doom · Age of Ravens: https://www.ageofravensgames.com/blog/2d20-system-guide-for-new-players-part-one*

### Fabula Ultima dá ao vilão um pool fixo por patamar, gasto em efeitos pequenos e frequentes: Menor 5 UP, Maior 10 UP, Supremo 15 UP, com ações de 1 UP (fugir da cena, rerrolar um teste, recuperar de to

**Números:**
```
5 / 10 / 15 UP por patamar de vilão. Gastos típicos de 1 UP. Ou seja, 5 a 15 usos por cena.
```

*fonte: TV Tropes — Fabula Ultima: https://tvtropes.org/pmwiki/pmwiki.php/TabletopGame/FabulaUltima · leitura comentada: https://philgamer.wordpress.com/2024/06/26/lets-study-fabula-ultima-part-2b-conflict-mechanics/*

### ⚠ Não achado

O que NÃO existe na literatura, e é importante você saber antes de esperar uma resposta pronta:

1. NENHUMA fonte dá um percentual publicado de 'fração de pool que as pessoas consideram gasto significativo'. Procurei em escrita de design de RPG, de TCG e de videogame. O Angry GM recusa a pergunta numérica explicitamente. As únicas frações que consegui são DERIVADAS por mim das tabelas oficiais (Pontos de Feitiço do DMG, custos de Malice do Draw Steel, 6-8 encontros do DMG) — são medidas reais, mas ninguém as escreveu como régua de percepção. Trate como referência, não como consenso.

2. Não achei estudo, playtest publicado ou dado medido sobre recurso crescente contra pool decrescente. Você pediu 'quais as vantagens medidas'. Elas não são medidas — são declaradas pelos designers (Colville sobre Malice, Heinsoo e Tweet sobre o dado de escalada) e relatadas por resenhistas. O Sly Flourish é explícito em não ter dado empírico. Não existe playtest público com número nessa área.

3. Não consegui abrir nenhum statblock solo completo do Draw Steel com os custos exatos de Malice por habilidade. O steelcompendium serve navegação em vez do corpo do texto pra WebFetch, e o stawl.app devolveu 403. O que consegui foi a página de Rival Malice (custos 3/5/7/10), que É uma medida real, mas é de grupo de rivais, não de solo. Se você quiser os números de um chefe solo mesmo, vai precisar do PDF do Draw Steel: Monsters.

4. Não achei retrospectiva oficial dos designers de 4e admitindo o fracasso do solo. A evidência é indireta: o corte de ~20% de HP no MM2 e a refeitura da matemática no MM3, mais consenso forte de comunidade. Serve como evidência de comportamento, não como declaração.

5. Não achei relato específico e bem documentado de 'chefe gastou tudo na rodada 1 e virou saco de pancada'. O que existe é a análise do mecanismo (Angry GM parte 1: o solo passa as rodadas esperando recarga) e relatos de saco de pancada por outra causa (excesso de vida). O caso exato que você descreveu é discutido como risco de design, não como incidente registrado.

6. Nada na literatura trata do caso do inimigo com pool próprio numa luta única. Todo o corpo de escrita sobre attrition pressupõe o eixo do dia. Você está num ponto onde a pesquisa se esgota e a decisão passa a ser sua — mas o Draw Steel prova que a saída conhecida é trocar o denominador de LUTA para RODADA, e o custo das habilidades ficar entre meia e uma rodada e meia de renda.


---

## Frente 4

A pergunta do Mizuki já tem resposta pronta no campo, e as duas metades dela ("segunda tabela de dano mais alta" e "custo em energia") são resolvidas por sistemas diferentes, com número.

**Sobre a segunda tabela:** o Pathfinder 2e literalmente tem duas colunas de dano lado a lado — `Unlimited Use` e `Limited Use` — na mesma tabela (Table 2-12: Area Damage). A coluna limitada vale `1,40×` no nível 1, `1,95×` no nível 10 e `2,26×` no nível 24. Não é "um pouco maior": é o dobro. O Level Up (A5E) faz a mesma coisa por câmbio em vez de tabela: *"For every two points of damage that a limited-use ability exceeds the damage per turn budget, reduce the total damage dealt on other turns by one"* — surplus de 2 custa 1, ou seja, a rajada limitada é vendida com 50% de desconto de propósito.

**Sobre a energia:** ninguém no campo dá poço de PE ao monstro no formato do jogador. Quatro respostas apareceram, todas evitando o rastreio de arithmética entre rodadas: (a) **rótulo de frequência sem poço** — "uma vez", "recarga 5-6", `X/dia` (D&D 2024), `once per battle` / `1d3 times per battle` (13th Age); (b) **poço minúsculo dimensionado pra uma luta** — Pontos de Foco do PF2e, `1 a 3`, e o próprio texto admite que com 1 ponto a criatura conjura uma vez só; (c) **poço da MESA, não do monstro, que cresce por rodada e evapora no fim** — a Malícia do Draw Steel; (d) **poço que reseta todo turno** — Ações Lendárias do 5e.

**O achado que mais importa pro projeto dele:** a `Intervenção` que ele já decidiu (3 por luta, cada uma uma vez, no máximo uma por rodada) é, palavra por palavra, a regra de Ação de Vilão do Draw Steel. Ele já reinventou a solução do campo sem saber. E a Malícia do Draw Steel, calibrada pra uma mesa de 4 e uma luta de 3 rodadas, entrega `18` de Malícia no total — que é exatamente o custo somado das três features que o livro manda preparar (`2-3` + `5` + `7-10` = `14 a 18`). O poço não é um orçamento de PE: é um relógio que solta três golpes grandes.

**Sobre a assimetria (pergunta 5):** ninguém escreveu um ensaio dedicado a ela, mas ela está escrita como regra, em fonte primária, em três lugares — e sempre para justificar CORTAR economia do monstro, nunca para dar.

### O PF2e É a resposta direta da pergunta do Mizuki: ele tem DUAS tabelas de dano na máquina de construção de criatura, uma para habilidade ilimitada e outra para habilidade de uso limitado, lado a lado 

**Números:**
```
Razão limitada ÷ ilimitada que eu calculei da tabela: nv 1 = 5 vs 7 (1,40×) · nv 5 = 12 vs 21 (1,75×) · nv 10 = 20 vs 39 (1,95×) · nv 15 = 27 vs 56 (2,07×) · nv 20 = 33 vs 74 (2,24×) · nv 24 = 39 vs 88 (2,26×). A curva sobe de 1,4× e estabiliza em ~2,0× a partir do nível 11. Base declarada: atividade de 2 ações (a maioria das magias de dano); ação única deve dar 'muito menos'.
```

*fonte: https://2e.aonprd.com/Rules.aspx?ID=2874 — GM Core, cap. Building Creatures, seção 'Damage-Dealing Abilities', Table 2–12: Area Damage*

### O Level Up (A5E) resolve a mesma coisa por câmbio explícito em vez de segunda tabela, e o câmbio é favorável à rajada de propósito. Texto literal: 'Abilities that can be used once per day or once per 

**Números:**
```
Câmbio 2:1. Excedente de 2 de dano custa 1 de dano nas outras rodadas. Conta que eu fiz da aplicação numa luta de 3 rodadas: cota D por rodada, rajada de D+X numa rodada, as outras duas somam 2D − X/2. Total da luta = 3D + X/2 — ou seja, o monstro SAI GANHANDO metade do excedente. O desconto é intencional, porque a habilidade limitada pode errar ou a luta pode acabar antes.
```

*fonte: https://a5e.tools/rules/designing-monsters — seção 'Special Attacks' → 'Limited-Use Abilities' (texto verificado no HTML cru)*

### Sim, criatura do PF2e tem espaço de magia, e o número é declarado com precisão — mas o próprio livro manda NÃO preencher, e a razão dada é o tempo de vida da criatura. Texto literal: 'Because creature

**Números:**
```
Círculo máximo = metade do nível arredondado pra cima. 5 truques. Nível ímpar: 2 espaços no círculo mais alto (+3 por círculo abaixo) OU 3 espaços (+4 por círculo abaixo). Nível par: 3 espaços no mais alto (+3 abaixo) OU 4 (+4 abaixo). Preencher de verdade: só os 3 círculos de cima + truques + alguns no 4º de cima pra baixo. Ficha completa só pra inimigo recorrente.
```

*fonte: https://2e.aonprd.com/Rules.aspx?ID=2874 — seção 'Prepared and Spontaneous Spells'*

### Magia inata do PF2e é o modelo de 'frequência escolhida sem poço': o desenhista declara a frequência ao gosto e não existe orçamento por trás. Texto literal: 'Unlike prepared and spontaneous spells, i

**Números:**
```
Três formatos citados como os mais notáveis: (1) círculo máximo, uma vez só; (2) à vontade, temático; (3) constante. O aviso: magia inata acima do círculo normal da criatura deve ser 'typically just one', e serve pra suporte / negação de ação / controle, não pra matar.
```

*fonte: https://2e.aonprd.com/Rules.aspx?ID=2874 — seção 'Innate Spells'*

### O PF2e tem UM caso de poço real na criatura, e ele é minúsculo e explicitamente dimensionado pra uma luta: os Pontos de Foco. Texto literal: 'Simply give the creature the focus spells you like and bet

**Números:**
```
Poço = 1 a 3 pontos. O jogador de PF2e tem a mesma faixa (1 a 3) — mas pro DIA inteiro. A criatura tem a mesma faixa pra UMA luta.
```

*fonte: https://2e.aonprd.com/Rules.aspx?ID=2874 — seção 'Focus Spells'*

### A frase primária que responde a pergunta 2, e ela é REGRA, não fórum. Texto literal do GM Core: 'Most notably, damaging spells drop off in usefulness for a creature that's expected to last only a sing

**Números:**
```
O corte que ela justifica: magia de dano 2 círculos abaixo do máximo 'is still potentially useful, but beyond that, don't bother'. Ou seja: 2 círculos de tolerância, e o resto do espaço de magia é decoração.
```

*fonte: https://2e.aonprd.com/Rules.aspx?ID=2874 — seção 'Spells', parágrafo de seleção de magia*

### O PF2e nomeia o modo de falha que o Mizuki vai encontrar se der buff de PE disfarçado: 'invisible abilities'. Texto literal: 'Avoid abilities that do nothing but change the creature's math, also known

**Números:**
```
—
```

*fonte: https://2e.aonprd.com/Rules.aspx?ID=2874 — seção 'Invisible Abilities'*

### O PF2e nomeia um segundo modo de falha, e ele é sobre orçamento desperdiçado: construir habilidade que a criatura nunca vai ter tempo de usar. Texto literal: 'Understanding a creature's action economy

**Números:**
```
—
```

*fonte: https://2e.aonprd.com/Rules.aspx?ID=2874 — seções 'Action Economy' e 'Design Abilities' (esta última também em https://2e.aonprd.com/Rules.aspx?ID=2903)*

### Terceiro modo de falha nomeado pelo PF2e, e é o único que fala diretamente de 'limitar pra equilibrar'. Texto literal: 'Use 3-action abilities sparingly, as a creature can't use them if it is slowed o

**Números:**
```
—
```

*fonte: https://2e.aonprd.com/Rules.aspx?ID=2874 — seção 'Active Abilities'*

### O Draw Steel é o sistema que DEU recurso ao lado do mestre, e a regra é a mais completa do levantamento. O ponto de desenho: o recurso NÃO é do monstro, é do Diretor, e é da mesa inteira. Texto litera

**Números:**
```
Ganho: no início do combate, Malícia = média de Vitórias por herói. No início de CADA rodada, Malícia = número de heróis + número da rodada. Exemplo do livro: 5 heróis com 3 Vitórias = 9 no começo da rodada 1 (3+5+1); +7 na rodada 2 (5+2); +8 na 3; +9 na 4. Herói que morre para de gerar Malícia. Sobra evapora no fim.
```

*fonte: https://steelcompendium.io/compendium/main/Bestiary/Monsters/Chapters/Monster%20Basics/ — seção 'Malice' (Earning Malice / Spending Malice / Basic Malice Features)*

### O Draw Steel tem uma regra que é IDÊNTICA à Intervenção que o Mizuki já decidiu. Texto literal: 'A creature with villain actions always has three. Each villain action can be used only once per encount

**Números:**
```
Sempre 3. Cada uma 1× por encontro. No máximo 1 por rodada. Só para criaturas 'solo' e 'leader'. Uma criatura solo enfrenta 6 heróis do mesmo nível; um leader enfrenta 2 ou mais.
```

*fonte: https://steelcompendium.io/compendium/main/Bestiary/Monsters/Chapters/Monster%20Basics/ — seção 'Villain Actions'. Versão 5e do mesmo desenho (Flee, Mortals!): https://www.dndbeyond.com/posts/1729-creature-roles-how-flee-mortals-helps-you*

### A calibragem da Malícia do Draw Steel, projetada numa luta de 3 rodadas, dá exatamente o custo das três features que o livro manda preparar. O livro é explícito sobre a preparação: 'You often need to 

**Números:**
```
Conta minha, aplicando a regra a uma mesa de 4 heróis sem Vitórias e uma luta de 3 rodadas: rodada 1 = 4+1 = 5 · rodada 2 = +4+2 = 11 acumulado · rodada 3 = +4+3 = 18 acumulado. Custo das 3 features recomendadas = 2-3 + 5 + 7-10 = 14 a 18. O poço de 3 rodadas cobre as três features preparadas, uma vez cada, e nada mais. E o livro escreve o princípio: 'You won't be able to spend Malice on every single option a given encounter has to offer.'
```

*fonte: https://steelcompendium.io/compendium/main/Bestiary/Monsters/Chapters/Monster%20Basics/ — quadro 'That's So Much Malice!'*

### O 13th Age usa 'por batalha' como unidade nativa de frequência de monstro — não 'por dia'. Texto de regra: 'A few monsters have limited abilities that can be used a certain number of times in a battle

**Números:**
```
'once per battle', '1d3 times per battle', 'first time each battle'. E note a existência de poço COMPARTILHADO por grupo de monstros — o mesmo desenho do Capanga em pool dele.
```

*fonte: https://www.13thagesrd.com/monsters/monster-rules/*

### A racionalização de por que o 4e trocou poder-por-dia por RECARGA no monstro, e ela é exatamente a assimetria da pergunta 5. Argumento do fórum, verificado no fio: não fazia sentido dar poderes diário

**Números:**
```
Recarga típica do 4e/5e: 5–6 num d20... na verdade num d6, 33% por rodada; recarga 6 = 17%.
```

*fonte: https://www.enworld.org/threads/recharge-powers.469834/page-3 (fio 'Recharge powers', EN World)*

### O D&D 2024 tirou espaço de magia do monstro e trocou por rótulo de frequência — e a razão declarada é carga cognitiva. Racionalização registrada no fórum da EN World: 'tracking more than about the top

**Números:**
```
Formato do lich de 2024: magias 'at will' (Detect Magic, Fireball, Lightning Bolt), '2/day' (Animate Dead, Dimension Door, Plane Shift), '1/day' (Chain Lightning, Finger of Death, Power Word Kill). O teto útil citado: 3 a 5 espaços.
```

*fonte: https://www.enworld.org/threads/wizards-have-a-problem-with-spellcasting-stat-blocks.709615/page-5 · https://arcaneeye.com/mechanic-overview/how-spellcasting-monsters-work/ · https://www.dndbeyond.com/forums/d-d-beyond-general/general-discussion/217738-homebrew-monster-spell-slot-design*

### O argumento mais forte contra rastrear recurso de monstro, dito por praticante e não por designer: a luta não dura o suficiente. Citação literal do usuário jl8e: 'Tracking spell slots just isn't worth

**Números:**
```
—
```

*fonte: https://www.dndbeyond.com/forums/d-d-beyond-general/general-discussion/217738-homebrew-monster-spell-slot-design*

### O modo de falha nomeado do lado do JOGADOR, que se aplica ao inimigo com dobro de força: o 'nova' / 'mago de cinco minutos'. O fio da EN World coloca o problema exatamente: se habilidade por-dia é mai

**Números:**
```
—
```

*fonte: https://www.enworld.org/threads/any-inherent-conflict-between-per-encounter-and-per-day-abilities.219305/ · contexto adicional: https://www.enworld.org/threads/a-discussion-in-game-design-the-15-minute-work-day.286349/*

### O contra-argumento moral, e é o filtro multi-mestre dele visto do outro lado. Depoimento de mestre no Gnome Stew: 'It wasn't fair to the players, who weren't allowed to "wing it" with their own charac

**Números:**
```
—
```

*fonte: https://gnomestew.com/npc-stats-full-partial-or-loose/*

### O Angry GM propõe a solução por FASES em vez de poço, e o argumento inclui uma observação sobre o lado do jogador que vale pro caso dele. Sobre habilidades por fase: 'each one only lasts for one third

**Números:**
```
Cada estágio dura ~2 rodadas, possivelmente 3. Cada bloco de componente tem 2 pontos de ação. Fase substitui recarga 5-6 (33%/rodada) em média.
```

*fonte: https://theangrygm.com/the-dd-boss-fight-part-2/*

### A assimetria da pergunta 5 nunca virou ensaio, mas está escrita como REGRA em três fontes primárias, e nas três ela justifica CORTAR economia do monstro, nunca dar. (1) PF2e: 'a creature that's expect

**Números:**
```
Do lado do jogador, a âncora que aparece repetida: 6 a 8 encontros por dia de aventura no 5e como premissa de orçamento. O sistema dele tem a própria âncora: poço de 120 a 180 PE para 10,5 rodadas de luta por dia (peça 5 / levantamento da Fase 1).
```

*fonte: https://2e.aonprd.com/Rules.aspx?ID=2874 · https://steelcompendium.io/compendium/main/Bestiary/Monsters/Chapters/Monster%20Basics/ · https://www.enworld.org/threads/recharge-powers.469834/page-3 · sobre o lado do jogador: https://alphastream.org/index.php/2015/10/17/interlude-extending-the-five-minute-workday/ e https://www.enworld.org/threads/a-discussion-in-game-design-the-15-minute-work-day.286349/ (estes dois eu vi só por resumo de busca, não abri as páginas)*

### ⚠ Não achado

**Não achei ensaio dedicado à assimetria (pergunta 5).** Procurei em várias formulações — "player budgets for the day, monster lives one fight", "asymmetry player resources monster single encounter", "monsters don't have an adventuring day". Ninguém escreveu o ensaio. O que existe é a mesma frase repetida como JUSTIFICATIVA dentro de regras de construção de monstro (PF2e, 4e, Draw Steel), sempre de passagem. A biblioteca gigante sobre o assunto é toda do lado do jogador ("five-minute workday", "adventuring day"), e ela nunca vira o espelho pro monstro. É uma lacuna real do campo — se ele escrever isso no Bestiário, é material novo, não repetição.

**Não achei os modos de falha organizados como lista nomeada.** Eu montei a lista dos achados individuais. Os únicos com NOME próprio publicado são "invisible abilities" (batizado pelo Paizo, no GM Core) e "five-minute workday" / "nova" (do lado do jogador). "Carga cognitiva", "rastreio inútil", "habilidade que nunca sai" e "as duas economias" aparecem descritos com precisão em fórum e em regra, mas sem batismo. Se ele quiser nomes, vai ter que batizar.

**Reddit está bloqueado pro meu buscador** (r/RPGdesign, r/Pathfinder2e, r/DnDBehindTheScreen) — o serviço recusa o domínio. Compensei com EN World, fóruns da D&D Beyond, Paizo e Giant in the Playground, mas a discussão do r/RPGdesign que a tarefa pedia especificamente ficou de fora. Vale um segundo passo com outra ferramenta se ele quiser essa camada.

**Três páginas não abriram:** o fio do Giant in the Playground "Strict per day abilities in RPGs" (403), o artigo do benholder.blog sobre a conjuração do Monster Manual 2024 (429), e o "unified theory of 5e combat design" do Dragna Carta no Substack (redirect não seguido). Do último eu só tenho paráfrase de busca — a afirmação de que o equilíbrio de classe do 5e só emerge num dia com várias lutas de atrito. **Não usei isso como citação em nenhum achado**, só como contexto.

**Não achei o Draw Steel dizendo se a Malícia é visível ao jogador por regra** — o livro deixa explicitamente à escolha do Diretor, e registra que alguns acham que ver a Malícia subir cria tensão. Isso é decisão de mesa, não regra.

**Não confirmei o desenho de NPC do Lancer nem do ICON.** As buscas voltaram só conteúdo de comunidade e itch.io, nada de fonte de regra. Se esses dois importarem como precedente (os dois são sistemas táticos com NPC construído por template e sem economia de recurso, pelo que eu sei de fora), precisam de checagem em fonte primária antes de entrar em qualquer documento.

**Uma coisa que eu calculei e não achei escrita em lugar nenhum:** a razão limitada÷ilimitada da tabela do PF2e (a curva de 1,40× a 2,26×) e o fechamento da Malícia numa luta de 3 rodadas (18 de Malícia contra 14–18 de custo das três features). As duas contas são minhas, feitas em cima do texto de regra literal. O texto de regra está citado; a conta não é deles.


---

## Frente 5

O D&D responde às DUAS perguntas do Mizuki, e as respostas não competem — são camadas diferentes do mesmo bloco.

À pergunta A ("não é só ajustar o custo do feitiço dentro do dano do inimigo?"): é exatamente o que o DMG 2014 faz, e o divisor é a duração da luta. Página 278, texto exato: "If a monster's damage output varies from round to round, calculate its damage output each round for the first three rounds of combat, and take the average." O exemplo do próprio livro é (90 + 37 + 37) ÷ 3 = 54. Uma habilidade de uma-vez-só entra no orçamento diluída por 3. A luta padrão do Mizuki tem 3 rodadas — o divisor já está pronto.

À pergunta B ("segunda tabela de dano maior ao custo de energia"): o D&D 2024 fez uma versão disso e chegou a uma conclusão contraintuitiva. Nos blocos novos existem duas camadas de dano, mas a camada PAGA não é a maior contra alvo único — é a mais LARGA. Arquimago 2025: ataque à vontade = 108 de dano por rodada, de graça; Lightning Bolt de nível 7, que custa uma de duas cargas diárias, dá 42 por alvo e só compensa a partir de 3 alvos. As oito magias à vontade dele têm ZERO dano. O recurso compra área, controle e mobilidade; o número bruto contra um alvo mora na linha gratuita.

Sobre o passo 13 que ele lembrou: existe, chama-se "STEP 13. SPECIAL TRAITS, ACTIONS, AND REACTIONS", e a frase é um parêntese na p. 279 — "(The features don't actually change the monster's statistics.)" O contexto é a tabela de Monster Features, que altera CA/PV/ataque/dano EFETIVOS só para calcular o ND. É o modelo de dois números: um na ficha, outro na conta. E a tabela dá a taxa de câmbio de recurso para estatística: Resistência Lendária vale +10/+20/+30 PV efetivos por uso diário conforme a faixa de ND.

Sobre a energia: nenhum sistema grande de D&D dá pool gastável ao monstro. Em 2014 dava espaço de magia de verdade e isso é a assimetria do Mizuki medida — o Arquimago tinha 20 espaços e usa 3 numa luta de 3 rodadas; 85% do recurso nunca é gasto. Em 2024 os espaços viraram contador: "At Will" e "X/Day Each". O único pool que sobrou é a Ação Lendária, e ela é POR RODADA — 3 pontos que recarregam inteiros todo turno. O número 3 se repete no bloco (Misty Step 3/Day, Protective Magic 3/Day, 3 ações lendárias) e bate com a duração da luta: o recurso flexível é dimensionado para uma por rodada, o recurso grande fica em 1 ou 2.

Recarga 5-6 numa luta de 3 rodadas dá 1,67 usos esperados no total (44% de usar uma vez só, 44% duas, 11% três). É "uma vez por luta com ruído", não pool.

O aviso do 4e: o modo de falha documentado não é o chefe ficar forte demais, é o chefe VIRAR MÁQUINA DE ATAQUE BÁSICO depois que o recurso acaba. Se a Catástrofe age 5 vezes por rodada e o PE seca na rodada 2, a rodada 3 — o clímax — fica vazia. O Draw Steel resolve isso invertendo o sentido: a Malice do Diretor CRESCE por rodada (2 × número de heróis), e escala com o tamanho da mesa, que é justamente o eixo da escada Capanga→Calamidade. As Villain Actions do Colville resolvem de outro jeito: o recurso É o número da rodada, uma por rodada, com arco dramático embutido.

E há uma âncora numérica direta para a assimetria: Mearls documentou que o 5e orça ~20 rodadas de combate entre descansos longos. O inimigo tem 3. Dar ao inimigo o PE de um jogador de mesmo nível entrega ~6,7× o necessário; o fator de correção natural é 3/20 ≈ 0,15.

### A resposta do D&D à pergunta "não é só ajustar o custo do feitiço dentro do dano do inimigo?" é: sim, é exatamente isso, e o divisor é a DURAÇÃO DA LUTA. O DMG 2014 manda calcular o dano de cada uma d

**Números:**
```
Texto exato: "If a monster's damage output varies from round to round, calculate its damage output each round for the first three rounds of combat, and take the average." Exemplo do próprio livro (dragão branco jovem): sopro 90 (dois alvos) na rodada 1, multiataque 37 nas rodadas 2 e 3 → (90 + 37 + 37) ÷ 3 = 54 de dano por rodada para efeito de ND. O sopro vale 90 na conta bruta e ~18 a mais por rodada no orçamento.
```

*fonte: D&D 5e Dungeon Master's Guide (2014), cap. 9, p. 278 — https://online.anyflip.com/tqblu/sfae/files/basic-html/page278.html*

### O passo 13 do DMG 2014 se chama "STEP 13. SPECIAL TRAITS, ACTIONS, AND REACTIONS", e a frase que o Mizuki lembrou existe e é um parêntese — o ponto é que a tabela de features altera a CA/PV/dano EFETI

**Números:**
```
Contexto exato: "The Monster Features table list various features that you can plunder from the Monster Manual. The table notes which features increase a monster's effective Armor Class, hit points, attack bonus, or damage output for the purpose of determining its challenge rating. (The features don't actually change the monster's statistics.)"
```

*fonte: D&D 5e Dungeon Master's Guide (2014), p. 278–279 — https://online.anyflip.com/tqblu/sfae/files/basic-html/page279.html*

### O DMG 2014 diz explicitamente que conjuração só mexe no ND quando o feitiço supera o ataque normal do monstro ou mexe em CA/PV. Feitiço de utilidade é de graça.

**Números:**
```
"Innate Spellcasting and Spellcasting. The impact that the Innate Spellcasting and Spellcasting special traits have on a monster's challenge rating depends on the spells that the monster can cast. Spells that deal more damage than the monster's normal attack routine and spells that increase the monster's AC or hit points need to be accounted for when determining the monster's final challenge rating."
```

*fonte: D&D 5e Dungeon Master's Guide (2014), p. 279 — https://online.anyflip.com/tqblu/sfae/files/basic-html/page279.html*

### O D&D converte recurso por dia em PONTOS DE VIDA EFETIVOS. A tabela de Monster Features do DMG dá a taxa de câmbio explícita para Legendary Resistance.

**Números:**
```
Legendary Resistance: cada uso por dia vale +10 PV efetivos (ND 1–4), +20 (ND 5–10), +30 (ND 11+). Outras linhas: Magic Resistance = +2 CA efetiva; Damage Transfer = dobra os PV efetivos e soma 1/3 dos PV ao dano por rodada; Frightful Presence = +25% de PV efetivos contra personagens de nível 10 ou menos; Regeneration = PV regenerados por rodada × 3; Aggressive = +2 de dano por rodada; Nimble Escape = +4 de CA efetiva E +4 de bônus de ataque efetivo.
```

*fonte: D&D 5e Dungeon Master's Guide (2014), p. 280–281 — https://online.anyflip.com/tqblu/sfae/files/basic-html/page280.html e https://online.anyflip.com/tqblu/sfae/files/basic-html/page281.html*

### No 5e de 2014 o monstro tinha ESPAÇOS DE MAGIA de verdade, iguais aos de um jogador, e em quantidade absurda para uma luta de 3 rodadas.

**Números:**
```
Mago (ND 6, 40 PV): conjurador de 9º nível, 14 espaços (4/3/3/3/1). Arquimago (ND 12, 99 PV): conjurador de 18º nível, 20 espaços (4/3/3/3/3/1/1/1/1), e o ataque físico é uma adaga de 4 de dano. Lich (ND 21, 135 PV): conjurador de 18º nível, 20 espaços, Resistência Lendária 3/dia, 3 ações lendárias.
```

*fonte: Blocos 2014 — Mago: https://www.aidedd.org/dnd/monstres.php?vo=mage · Arquimago: https://www.aidedd.org/dnd/monstres.php?vo=archmage · Lich: https://www.aidedd.org/dnd/monstres.php?vo=lich*

### A mudança de 2024/2025 é real e total: os blocos novos NÃO têm espaço de magia. Trocaram por "At Will" / "X/Day Each", e o texto oficial de regra define as duas notações.

**Números:**
```
Texto oficial de X/Day: "This notation means the stat block part can be used a certain number of times (represented by X) and that a monster must finish a Long Rest to regain expended uses." Texto oficial de Recharge: "...At the start of each of the monster's turns, roll 1d6. If the roll is within the number range given in the notation (represented by X–Y), the monster regains the use of that part, which also recharges when the monster finishes a Short or Long Rest."
```

*fonte: D&D 2024 Basic Rules, "How to Use a Monster" — https://www.dndbeyond.com/sources/dnd/br-2024/how-to-use-a-monster · análise: https://arcaneeye.com/mechanic-overview/how-spellcasting-monsters-work/*

### Bloco concreto 2025 — Mago (ND 6). O ataque livre virou a linha de dano principal, e o recurso limitado virou área e controle. São 6 usos de magia de nível por dia, mais dois blocos de 3/dia.

**Números:**
```
CA 15, 81 PV (era 40), ND 6. Multiattack: 3 × Arcane Burst de 16 (3d8+3) = 48 de dano por rodada, DE GRAÇA. Spellcasting — At Will: Detect Magic, Light, Mage Armor, Mage Hand, Prestidigitation (zero dano). 2/Day Each: Fireball (versão de nível 4), Invisibility. 1/Day Each: Cone of Cold, Fly. Bônus: Misty Step (3/Day). Reação: Protective Magic — Counterspell ou Shield (3/Day). Total de "cargas": 6 de magia + 3 + 3 = 12.
```

*fonte: Mago 2024 — https://www.aidedd.org/monster/mage · https://roll20.net/compendium/dnd5e/Monsters:Mage?expansion=34653*

### Bloco concreto 2025 — Arquimago (ND 12). O padrão se repete e fica mais gritante: TODAS as magias à vontade são de zero dano, e o dano vem do ataque gratuito.

**Números:**
```
CA 17, 170 PV (era 99), ND 12. Multiattack: 4 × Arcane Burst de 27 (4d10+5) = 108 por rodada, de graça (em 2014 era uma adaga de 4). At Will (8 magias, nenhuma de dano): Detect Magic, Detect Thoughts, Disguise Self, Invisibility, Light, Mage Armor, Mage Hand, Prestidigitation. 2/Day Each: Fly, Lightning Bolt (versão nv 7 = 12d6 ≈ 42/alvo). 1/Day Each: Cone of Cold (nv 9 = 12d8 ≈ 54/alvo), Mind Blank, Scrying, Teleport. Misty Step 3/Day. Protective Magic 3/Day. Espaços: 20 → 8 usos limitados.
```

*fonte: Arquimago 2024 — https://www.aidedd.org/monster/archmage · https://www.roll20.net/compendium/dnd5e/Monsters:Archmage?expansion=33335*

### Bloco concreto 2025 — Lich (ND 21). Magias que em 2014 custavam espaço de nível 3 e 5 viraram À VONTADE; só as de efeito de mesa continuam limitadas.

**Números:**
```
CA 20, 315 PV (era 135), ND 21. Multiattack: 3 ataques (Eldritch Burst 31 (4d12+5), ou Paralyzing Touch 15 + paralisia). At Will (8): Detect Magic, Detect Thoughts, Dispel Magic, Fireball (nível 5), Invisibility, Lightning Bolt (nível 5), Mage Hand, Prestidigitation. 2/Day Each: Animate Dead, Dimension Door, Plane Shift. 1/Day Each: Chain Lightning, Finger of Death, Power Word Kill, Scrying. Reação: Counterspell/Shield. 3 ações lendárias (4 no covil). Espaços: 20 → 10 usos limitados.
```

*fonte: Lich 2024 — https://www.aidedd.org/monster/lich · https://arcaneeye.com/mechanic-overview/how-spellcasting-monsters-work/*

### Recarga 5-6 dispara MENOS de uma vez a mais numa luta de 3 rodadas. A conta fecha em 1,67 usos esperados no total.

**Números:**
```
p = 1/3 por rodada. Usada na rodada 1, o monstro rola no início das rodadas 2 e 3 → Binomial(2; 1/3). Usos extras esperados = 0,67; TOTAL esperado em 3 rodadas = 1,67. Distribuição: 1 uso só = 44,4%; 2 usos = 44,4%; 3 usos = 11,1%. Comparação: Recarga 6 (p=1/6) → 1,33 usos totais. Recarga 4-6 (p=1/2) → 2,0 usos totais. (O DungeonSolvers publica "11% de chance de ser usada duas vezes nas 3 primeiras rodadas" — a redação é ambígua; 11,1% é a chance de usar nas TRÊS rodadas.)
```

*fonte: Regra: D&D 2024 Basic Rules, "How to Use a Monster" — https://www.dndbeyond.com/sources/dnd/br-2024/how-to-use-a-monster · Monster Manual 2014 p.11 · análise: https://www.dungeonsolvers.com/a-look-into-the-dd-5e-recharge-mechanic/*

### O D&D usa recarga em vez de pool por dois motivos documentados: incerteza para o jogador e zero escrituração para o mestre. É herança direta do 4e, e foi desenhada contra o modelo do 3e.

**Números:**
```
Citado na discussão: "The reason the mechanic was introduced in 4e was because it was a cool uncertainty mechanic for monsters to have powers that the players weren't quite sure how soon they'd be available again." No 3e o equivalente exigia "rolling a random number of rounds before the power would recharge" — contagem regressiva rodada a rodada. A recarga consolidou tudo em UMA rolagem no início do turno. Texto de regra 4e citado no fórum: "At the start of each of the monster's turns, roll a d6. If the roll is one of the die results shown in the power description, the monster regains the use of that power."
```

*fonte: EN World, "Recharge powers", p.3 — https://www.enworld.org/threads/recharge-powers.469834/page-3 · EN World, "How do Monster Recharge Powers Work?" — https://www.enworld.org/threads/how-do-monster-recharge-powers-work.283747/*

### O 4e deu at-will / encounter / recharge ao monstro, e a razão de o "por encontro" ter perdido espaço para a recarga é que o monstro não vive dois encontros. Poder diário em monstro é orçamento que nun

**Números:**
```
No 4e: poder à vontade = sem limite; poder por encontro = recarrega em descanso curto (5 minutos); poder diário = descanso longo (6h); recarga = chance aleatória a cada rodada. Monstros elite e solo tinham pontos de ação como os PCs, mas — ao contrário dos PCs — podiam gastar mais de um ponto de ação no mesmo encontro. Argumento que circula na comunidade (não consegui atribuir a um post verificável): não fazia sentido dar poder diário e por encontro ao monstro porque você dificilmente enfrenta o mesmo monstro duas vezes no mesmo dia; a recarga ocupou o meio entre a habilidade-estouro e a habilidade à vontade.
```

*fonte: EN World / D&D 4e Recharge — https://www.enworld.org/threads/monster-power-recharge.226665/page-2 · síntese do sistema: https://dungeonsdragons.fandom.com/wiki/Dungeons_%26_Dragons_4th_edition*

### O modo de falha documentado do 4e é o oposto do que o Mizuki teme: não é o chefe ficar sem recurso, é o chefe virar máquina de ataque básico depois que o recurso acaba — luta longa e monótona.

**Números:**
```
Formulação da comunidade: uma vez que o grupo esgota sua cota de diários e por-encontro, o solo "becomes a drone of at-will powers until it finally falls". Reclamação recorrente sobre poderes de uso único no 4e: o combate se arrasta muitas rodadas e a frustração de errar com um poder diário ou por encontro é grande.
```

*fonte: EN World, "Why is 4E so grindy?" — https://www.enworld.org/threads/why-is-4e-so-grindy.273174/ · discussão de recarga: https://www.enworld.org/threads/recharging-encounter-powers.239546/*

### O Monster Manual 3 do 4e é o registro histórico de que a resposta a "o monstro não faz o suficiente" foi mexer no DANO e nos PV, não dar mais recurso.

**Números:**
```
O MM3 refez a matemática ("Monster Manual 3 on a Business Card") e foi "the first book where you wouldn't need to apply any blanket fixes to monster damage". Os blocos passaram a listar habilidade por TIPO DE AÇÃO — traços passivos, padrão, movimento, menor, disparada, nessa ordem. Monstros líder do MM3 passaram a dar bônus de combate em vez de curar.
```

*fonte: Leitura do MM3 4e — https://bira.github.io/octopus-carnival/2022/04/23/mm3-intro.html · Blog of Holding, "5e monster manual on a business card" — https://www.blogofholding.com/?p=7338*

### A ÚNICA coisa parecida com um pool que o D&D dá ao monstro é a Ação Lendária, e ela é POR RODADA, não por luta nem por dia. Recarrega inteira no início de cada turno do monstro.

**Números:**
```
3 ações lendárias por rodada (o Lich 2024 tem 4 no covil). Regra oficial: "A Legendary Action is an action that a monster can take immediately after another creature's turn. Only one of these actions can be taken at a time and only after another creature's turn ends." Mudança de 2024: "Each Legendary Action counts as a single use of a monster's Legendary Actions—none cost multiple actions to use" (em 2014 algumas custavam 2 ou 3).
```

*fonte: D&D 2024 Basic Rules, "How to Use a Monster" — https://www.dndbeyond.com/sources/dnd/br-2024/how-to-use-a-monster · Lich 2024 — https://www.aidedd.org/monster/lich · https://www.dndbeyond.com/posts/1890-preview-the-new-stat-block-design-in-the-2024*

### O número 3 aparece três vezes no bloco 2025 e não é coincidência: 3 usos de Misty Step, 3 de Protective Magic, 3 ações lendárias — exatamente a duração padrão da luta.

**Números:**
```
Mago e Arquimago: Misty Step (3/Day) e Protective Magic (3/Day). Lich: 3 ações lendárias. Abadía: "A battle typically lasts only three to five rounds, so the monster should have no more than five actions and typically three will suffice."
```

*fonte: Mago 2024 — https://www.aidedd.org/monster/mage · Arquimago 2024 — https://www.aidedd.org/monster/archmage · Teos Abadía (designer de aventuras da WotC), "How to Create a Monster for Revised D&D 5E 2024" — https://alphastream.org/index.php/2025/03/26/how-to-create-a-monster-for-revised-dd-5e-2024/*

### A assimetria que o Mizuki descreveu está escrita em texto de terceiros como o motivo mecânico de não dar recurso de jogador ao monstro.

**Números:**
```
"There is no point in memorizing everything a level 20 druid can do when you are only going to use three spell slots and some wildshapes to boost their hit points." O texto também mede o outro lado: um monstro de ND 2 precisa de 40 a 60 PV para durar contra quatro atacantes, contra ~20 de um guerreiro de nível 2 — cerca de duas a três vezes os PV de um PC.
```

*fonte: Dump Stat Adventures, "Don't Give Your Monsters Class Levels" — https://dumpstatadventures.com/the-gm-is-always-right/dont-give-your-monsters-class-levels*

### Mike Mearls documentou o orçamento de recurso do jogador no 5e: cerca de 20 rodadas de combate entre descansos longos, ou seja 6 a 7 encontros de 3 rodadas.

**Números:**
```
~20 rodadas de combate entre descansos longos; ~6 a 7 encontros assumindo média de 3 rodadas por combate. Diagnóstico do Mearls: "a semi-optimized party can vaporize boss monsters in a round or even less" e "a party that unloads with their best powers simply breaks the system" — o problema é a distância entre o jogo suposto (ataque à vontade) e o jogo real (alpha strike). Jonathan Tweet acrescenta que o momento do descanso está fora do controle do designer.
```

*fonte: EN World, "Mike Mearls explains why your boss monsters die too easily" — https://www.enworld.org/threads/mike-mearls-explains-why-your-boss-monsters-die-too-easily.715658/*

### O Pathfinder 2e é o único sistema grande que ainda mantém as duas portas abertas em texto de regra, e diz quando usar cada uma — é a formulação mais limpa do princípio.

**Números:**
```
"Creatures aren't built the same way PCs are. The rules for building them are more flexible, and their statistics are based on benchmark final numbers rather than combining each individual modifier together." Sobre espaços: use espaços de magia para criaturas que devem funcionar como um conjurador de PC, com o nível máximo de magia = metade do nível da criatura arredondado pra cima, e preenchendo só os três níveis mais altos (três quartos das magias escolhidas por tema). Sobre magia inata: pode ser de nível mais alto que metade do nível, "and you can choose how often they're used—they can even be used at will or be constant effects".
```

*fonte: Pathfinder 2e, "Building Creatures" (Archives of Nethys, texto de regra oficial) — https://2e.aonprd.com/Rules.aspx?ID=2874*

### Nenhum sistema grande dá ao monstro um POOL de energia gastável no molde do PE. O mais perto é o Draw Steel, e ele inverte o sentido: o recurso não é do monstro, é do MESTRE, e CRESCE durante a luta e

**Números:**
```
O Diretor gera Villain Power / Malice no topo de cada rodada igual a DUAS VEZES o número de heróis, mais bônus quando a facção joga conforme a tática dela (goblin dá 1 VP ao atacar um inimigo flanqueado sem Bane). Gasta-se no início do turno do monstro para ativar uma feature de Malice. Chefes têm três Villain Actions adicionais. "Malice means you are still challenging your heroes even when there's only one goblin left."
```

*fonte: MCDM / Draw Steel — https://shop.mcdmproductions.com/products/draw-steel-core-rules-bundle-pdf · https://www.youtube.com/watch?v=6hyxZC3YnpE · ficha de encontro oficial: https://files.mcdmproductions.com/DrawSteel/1-EncounterSheet_FormFillable.pdf*

### As Villain Actions do Colville amarram o recurso do chefe à RODADA em vez de a um pool — uma por rodada, cada uma só naquela rodada, com arco dramático embutido.

**Números:**
```
Três villain actions, uma por rodada de uma luta de três rodadas. Rodada 1 "position" (entrar em posição efetiva); rodada 2 "escape" (sair de posição ruim, às vezes mudar o campo de batalha); rodada 3 "explode" — "the boss is about to die so make the characters regret ever tangling with the boss." Justificativa: "boss monsters typically don't have the tools or action economy to deal with a full party of adventurers", e as ações são atreladas "to the rounds of a battle which often mirror the dramatic arc of a story".
```

*fonte: Sly Flourish, "Improvising Colville-style Action Oriented Monsters in D&D" — https://slyflourish.com/action_oriented_monsters.html*

### A prática real da WotC, medida em cima dos livros publicados, é o princípio da causa do Mizuki: os números do bloco variam por história, e as features quase não movem estatística nenhuma.

**Números:**
```
Análise de 2014: "below level 12 – where we have enough data points to do reasonable analysis – there are no significant hit point differences between monsters with high special defenses/resistances/immunities and those without." Dano do MM ficou 10% a 20% abaixo da tabela do DMG; bônus de ataque até 5 pontos acima (+12 previsto contra +17 real no nível 24). Análise de 2024: as ponderações existem mas são "very small and don't make much of a difference"; monstros com Magic Resistance têm ~10 PV a menos entre ND 2 e 6 e o padrão quebra a partir de ND 7; só os casos extremos (fantasma, cloaker, tapete sufocador, com transferência de dano) chegam a ~2/3 dos PV médios. Conclusão do autor: "vary your monster's stats based on their story, with minor variations (up 10%) being common".
```

*fonte: Blog of Holding (Paul Hughes), "the 5e monster creation guidelines are wrong" — https://www.blogofholding.com/?p=7283 · "looking at offensive and defensive adjustments in the 2024 monster manual" — https://www.blogofholding.com/?p=8548*

### ⚠ Não achado

Cinco buracos, e um deles importa para a decisão.\n\n1. NÃO EXISTE texto de designer da WotC dizendo POR QUE tiraram os espaços de magia do monstro em 2024. Os dois posts oficiais (https://www.dndbeyond.com/posts/1890-preview-the-new-stat-block-design-in-the-2024 e https://www.dndbeyond.com/posts/1913-updates-in-the-monster-manual-2025) descrevem O QUE mudou e param aí — o mais perto de uma razão é \"revised with a focus on fun and usability\" e \"Spellcasting monsters now cast spells in ways that are easier to utilize in combat\". Nenhuma entrevista do Jeremy Crawford que consegui alcançar (EN World, ScreenRant, CBR) toca no assunto de espaço de magia. A racionalização circula só em análise de terceiros. Se o parent quiser texto de designer de PRIMEIRA mão sobre isso, provavelmente está em vídeo/podcast, não em texto indexado.\n\n2. O texto primário do 4e me foi bloqueado. A anyflip do Monster Manual 4e devolveu 403 e a wiki dnd4.fandom devolveu 402. Tudo que digo sobre o 4e vem de fórum e de leitura de terceiros, incluindo a frase mais útil — \"não faz sentido dar poder diário e por encontro ao monstro porque você não enfrenta o mesmo monstro duas vezes no mesmo dia\" — que apareceu em resumo de busca mas que eu NÃO consegui atribuir a um post verificável. Tratar como consenso de comunidade, não como citação.\n\n3. Não achei o número oficial de quantos usos limitados um monstro DEVE ter. O \"3 por luta\" que aponto é padrão observado nos blocos (Misty Step 3/Day, Protective Magic 3/Day, 3 ações lendárias), não regra escrita.\n\n4. O \"4× o dano de uma ação não limitada\" para habilidade de uso limitado é análise do Teos Abadía (designer de aventuras da WotC, alphastream.org), NÃO texto do DMG 2024. O número oficial equivalente é o método de média de 3 rodadas do DMG 2014, que é mais conservador.\n\n5. Não fui atrás do 3.5e a fundo — as buscas devolveram quase só 5e. O que ficou confirmado é só o contorno: no 3e/3.5 o monstro era construído com as MESMAS regras do personagem (classe, espaços de magia, habilidades tipo-magia X/dia), e o 4e foi a ruptura explícita com isso. Se o parent quiser o caso 3.5 com texto de regra na mão, é uma segunda rodada de pesquisa.\n\nNão li nenhum arquivo do repositório nem da pasta do Bestiário além do LEIA-ME.md — a tarefa era pesquisa de campo externa. Nada foi escrito em lugar nenhum.


---

## Frente 6

Os três sistemas concordam num ponto que responde direto à pergunta do Mizuki: NENHUM deles dá ao inimigo um orçamento de recurso próprio calculado como o do jogador. Draw Steel põe o recurso na mão do MESTRE (Malice), com renda que cresce por rodada e escala com o número de heróis — 18 Malice numa luta de 3 rodadas com 4 heróis sem Vitórias, 35 numa de 5 rodadas. 13th Age não dá recurso nenhum ao monstro: dá um bônus crescente aos JOGADORES (dado de escalada, +1 a +6) e resolve o poder do monstro com usos-por-batalha fixos. Lancer também não dá pool: dá recarga por dado (1d6, um único rolamento por NPC cobre todos os sistemas) e usos limitados. A escada de preço do Draw Steel é o dado mais aproveitável: as menus de Malice do bestiário são quase sempre 3 / 5 / 7-ou-10, e a renda de UMA rodada (5, 6, 7 nas rodadas 1-2-3 com 4 heróis) compra exatamente um item da faixa alta. A crítica documentada existe e é específica: rastrear a rodada para calcular a renda é chamado de "very book-keepy" e "quite tedious".

### Fórmula exata do Malice (texto oficial, Draw Steel: Monsters, capítulo Monster Basics): "At the start of combat, you gain Malice equal to the average number of Victories per hero. Then at the start of

**Números:**
```
Início = V (média de Vitórias por herói). Rodada R = H + R, onde H = número de heróis. Escala LINEARMENTE com heróis e com o número da rodada, não com o nível nem com a força do monstro.
```

*fonte: https://raw.githubusercontent.com/SteelCompendium/data-bestiary-md/main/Monsters/Chapters/Monster%20Basics.md (linhas 337-339) — espelhado em https://steelcompendium.io/compendium/main/Bestiary/Monsters/Chapters/Monster%20Basics/*

### Somas de Malice numa luta inteira (conta feita com a fórmula oficial). Com 4 heróis e 0 Vitórias: rodada 1 = 5 (acumulado 5), rodada 2 = 6 (11), rodada 3 = 7 (18), rodada 4 = 8 (26), rodada 5 = 9 (35)

**Números:**
```
3 rodadas, 4 heróis, 0 vitórias = 18 Malice no total. 5 rodadas = 35 Malice. Malice por herói por rodada com H=4: 1,25 / 1,50 / 1,75 / 2,00 / 2,25. Com H=6: 1,17 / 1,33 / 1,50 / 1,67 / 1,83 — ou seja, a renda por cabeça CAI quando a mesa cresce.
```

*fonte: cálculo direto da fórmula em https://raw.githubusercontent.com/SteelCompendium/data-bestiary-md/main/Monsters/Chapters/Monster%20Basics.md*

### Malice não tem teto e não sobra: "If a hero dies, they stop generating Malice for you. At the end of an encounter, any unused Malice is lost." O Diretor escolhe se mostra ou não o total aos jogadores.

**Números:**
```
Teto: nenhum. Carry-over entre encontros: zero. Herói morto para de gerar renda.
```

*fonte: https://raw.githubusercontent.com/SteelCompendium/data-bestiary-md/main/Monsters/Chapters/Monster%20Basics.md (linhas 339-341)*

### As duas Basic Malice Features, texto e preço exatos. "Brutal Effectiveness (3 Malice) — The monster digs into the enemy's weak spot. The next ability the monster uses with a potency has that potency i

**Números:**
```
3 Malice = +1 de potência. 5 Malice = +característica de dano; cada Malice extra = +1 de dano, teto em 3x a característica. Com característica 3: 5 Malice → +3; 11 Malice → +9. Com característica 5: 5 → +5; 15 → +15. Trava: não pode em duas rodadas seguidas, NEM por outro monstro.
```

*fonte: https://raw.githubusercontent.com/SteelCompendium/data-bestiary-md/main/Monsters/Chapters/Monster%20Basics.md (linhas 357-367)*

### O livro dá a receita de curadoria (quadro "That's So Much Malice!"): "You often need to prepare only three Malice features for any given encounter, or four if you're running an encounter making use of

**Números:**
```
Três faixas: 2-3 / 5 / 7-10. Três features preparadas por encontro (quatro se houver mistura de tipos).
```

*fonte: https://raw.githubusercontent.com/SteelCompendium/data-bestiary-md/main/Monsters/Chapters/Monster%20Basics.md (linha 372)*

### Verifiquei a escada contra o bestiário inteiro em vez de acreditar no quadro. Nos 63 arquivos de "[Criatura] Malice" (os menus de grupo), o histograma de custos é: 1 Malice = 5 ocorrências, 2 = 2, 3 =

**Números:**
```
217 features de grupo. 84% dos custos caem em 3, 5, 7 ou 10. Custos 4 e 6 são resíduo (7 de 217, ~3%).
```

*fonte: https://github.com/SteelCompendium/data-bestiary-md (63 arquivos */Features/*Malice.md), contados por script*

### Nas habilidades dos stat blocks individuais (não nos menus de grupo) o preço é MUITO mais barato: das 451 entradas com custo em Malice, 79 custam 1, 147 custam 2, 145 custam 3, 10 custam 4, 63 custam 

**Números:**
```
82% dos custos individuais são 1-3. Só 1,5% custam 7 ou mais.
```

*fonte: https://github.com/SteelCompendium/data-bestiary-json — Monsters/statblocks.json (416 stat blocks), contado por script*

### A vazão é limitada, não só o saldo: "At the start of any monster's turn, you can spend Malice to activate one of the following features" — UMA por turno de monstro, e as features de grupo por tipo de 

**Números:**
```
Máximo de 1 ativação de Basic Malice por turno de monstro; features de [Criatura] Malice, 1 por turno.
```

*fonte: https://raw.githubusercontent.com/SteelCompendium/data-bestiary-md/main/Monsters/Chapters/Monster%20Basics.md (linhas 347, 357)*

### As Villain Actions NÃO custam Malice. "A creature with villain actions always has three. Each villain action can be used only once per encounter, and no more than one villain action can be used per ro

**Números:**
```
3 por encontro, cada uma 1 vez, no máximo 1 por rodada, custo em Malice = 0.
```

*fonte: https://raw.githubusercontent.com/SteelCompendium/data-bestiary-md/main/Monsters/Chapters/Monster%20Basics.md (linhas 208-220)*

### Criatura Solo do Draw Steel age duas vezes por rodada e o "agir mais" é comprável: "Solo Turns — The creature can take two turns each round. They can't take turns consecutively." E a receita de conver

**Números:**
```
Solo = 2 turnos/rodada. Conversão: EV x3, Stamina x2,5. Ação principal extra = 5 Malice. Um Solo enfrenta 4 a 6 heróis sozinho.
```

*fonte: https://raw.githubusercontent.com/SteelCompendium/data-bestiary-md/main/Monsters/Chapters/Monster%20Basics.md (linhas 751-776)*

### A justificativa de design está escrita no próprio livro, e é simetria com o herói: "Just as every hero has a Heroic Resource determined by their class, so too do the heroes' foes need their own juice 

**Números:**
```
—
```

*fonte: https://raw.githubusercontent.com/SteelCompendium/data-bestiary-md/main/Monsters/Chapters/Monster%20Basics.md (linhas 31, 333)*

### A justificativa funcional do pool único é ESCASSEZ COMPARTILHADA, que força escolha do mestre: "Malice is the director's resource, a dark mirror to heroic resources... If you spend your entire pool on

**Números:**
```
—
```

*fonte: https://gamingtrend.com/reviews/draw-steel-monsters-review/ e https://thedicesociety.com/tds006-monster-design/*

### A crítica de carga existe e é literal, sobre a fórmula de renda: "The DM gets a metacurrency too! Malice. He gets an amount based on the 'average number of victories per hero' at the start of combat. 

**Números:**
```
—
```

*fonte: https://ponderingtheorb.blogspot.com/2025/08/rpg-review-draw-steel.html*

### Outra crítica, mais ampla, sobre acúmulo de rastreamento no Draw Steel: "there is some burden of bookkeeping in tracking your resource points and surges, triggering actions out of turn, various effect

**Números:**
```
—
```

*fonte: https://medium.com/@pictor_dice_camp/draw-steel-is-a-lot-6843841de2f4 (via resultado de busca; a página bloqueia leitura direta)*

### O próprio Draw Steel trata 3 rodadas como duração típica de encontro cronometrado: "A typical encounter duration is 3 rounds" (aparece duas vezes, para objetivos de defender posição e de completar uma

**Números:**
```
3 rodadas = duração típica. 5+ rodadas = uma categoria de dificuldade acima.
```

*fonte: https://raw.githubusercontent.com/SteelCompendium/data-bestiary-md/main/Monsters/Chapters/Monster%20Basics.md (linhas 1066, 1084, 1185)*

### O esquadrão de minions do Draw Steel bate quase exatamente com o `Capanga` do Mizuki: máximo de OITO por esquadrão, com Stamina em pool compartilhado. "Each squad of minions shares a Stamina pool, wit

**Números:**
```
Máx. 8 minions/esquadrão. Pool = Stamina individual x nº de minions. Exemplo do livro: 8 goblins de 5 Stamina = pool de 40.
```

*fonte: https://raw.githubusercontent.com/SteelCompendium/data-bestiary-md/main/Monsters/Chapters/Monster%20Basics.md (linhas 388, 394, 415, 618)*

### Regra de bolso do custo/benefício do Malice em dano, medida no bestiário. Mediana da característica mais alta e do golpe de assinatura (tier 2 + característica) por nível: nível 3 → caract. 2, golpe 1

**Números:**
```
Malicious Strike a 5 Malice compra +15% a +30% de dano num golpe. No teto (5 + 2x característica de Malice) compra +50% a +90%. Com 4 heróis, a renda inteira da rodada 3 (7 Malice) e característica 3 compra +5 de dano num golpe que já dá ~18 — ou seja, ~+28% por uma rodada inteira de renda.
```

*fonte: https://github.com/SteelCompendium/data-bestiary-json (282 stat blocks com Signature Ability legível), medido por script*

### Regra opcional do próprio livro: os jogadores podem gastar hero tokens para REDUZIR o Malice do Diretor. "You could allow heroes to spend hero tokens to reduce the amount of Malice you have."

**Números:**
```
—
```

*fonte: https://raw.githubusercontent.com/SteelCompendium/data-rules-md/main/Chapters/For%20the%20Director.md (linha 170)*

### 13th Age: o dado de escalada é do JOGADOR, e o monstro não tem recurso equivalente. "At the start of the second round, the GM sets the escalation die at 1." "Each round, the escalation die advances by

**Números:**
```
Começa na rodada 2 em +1, sobe +1 por rodada, teto +6. Rodada 1 = 0.
```

*fonte: https://www.13thagesrd.com/combat-rules/*

### A justificativa de design do 13th Age, do próprio Rob Heinsoo: "the math of 13th Age expects that only the PCs (and dragons!) get the escalation die. Adding the escalation die to all monster attacks w

**Números:**
```
Uma única categoria de exceção (dragões).
```

*fonte: https://pelgranepress.com/2014/08/07/13th-sage-escalation-for-everyone/*

### 13th Age: o que o monstro tem no lugar de recurso é uso limitado, e existe um pool COMPARTILHADO em pequena escala. "A few monsters have limited abilities that can be used a certain number of times in

**Números:**
```
Vida do mook = 1/5 de um monstro normal. Usos por batalha: 1, ou 1d3. Recarga de item mágico: 6+, 11+ ou 16+ em d20, rolada DEPOIS da batalha.
```

*fonte: https://www.13thagesrd.com/monsters/monster-rules/ e https://www.toolkit13.com/srd/monsters*

### Lancer, texto oficial da tag Recharge (repositório da Massif Press): "Once this system or weapon has been used, it can't be used again until it is recharged. At the start of this NPC's turn, roll 1d6:

**Números:**
```
1d6 no início do turno do NPC, alvo tipicamente 4+ ou 5+ (p(4+)=50%, p(5+)=33%). UM rolamento por NPC cobre TODOS os sistemas dele.
```

*fonte: https://github.com/massif-press/lancer-data — lib/tags.json (tg_recharge, tg_limited, tg_unlimited)*

### Lancer NÃO dá pool ao mestre e simplifica o NPC agressivamente: NPCs têm 1 Structure e 1 Stress por padrão, são destruídos sem rolar na tabela ao chegar a 0 HP, ficam Exposed indefinidamente ao estour

**Números:**
```
NPC padrão: 1 Structure, 1 Stress. Elite: x2 Structure/Stress, x2 ativações. Ultra: +3 Structure, +1-2 ativações. Recomendação de encenação: no máximo 1 sistema opcional por inimigo (2 em caso especial), e total de ativações inimigas ~1,5x o número de jogadores.
```

*fonte: https://lancer-faq.netlify.app/ e https://lancer-rules.carrd.co/ e https://owacsender.substack.com/p/the-gms-guide-to-building-lancer*

### ⚠ Não achado

1) Não achei um texto de design assinado pelo Colville explicando em primeira pessoa por que o Malice ficou no Diretor em vez de por monstro. O que existe é (a) a linha do próprio livro sobre simetria com o Heroic Resource, (b) a linha sobre o stat block ser "a moment in time", e (c) um episódio de podcast de 2023 (thedicesociety.com/tds006) em que o recurso ainda se chamava Villain Power e a primeira versão da acumulação já tinha sido descartada. Os vídeos "Designing the Game" do MCDM não são indexáveis por busca de texto e a Patreon exige login.

2) Não achei threads do Reddit sobre a carga do Malice — a ferramenta de busca devolveu lixo (livros e álbuns chamados "Malice") em três tentativas. As duas críticas que reporto são de blogs de resenha, e só uma delas (ponderingtheorb) ataca o Malice diretamente.

3) Não consegui medir a distribuição de valores de Recharge nos NPCs do Lancer: os dados de NPC não estão no repositório aberto da Massif (lancer-data só tem conteúdo de jogador); ficam no LCP proprietário. O lancer.wiki.gg bloqueia leitura automatizada (devolve página "Blocked" e 404 via fetch), então as regras de NPC do Lancer vieram do FAQ/errata da comunidade e do repositório oficial de tags.

4) Não achei número oficial de "quantos turnos de monstro existem por rodada" num encontro padrão de Draw Steel, então não consegui converter a renda de Malice em "Malice por turno de monstro" com base publicada. Dá pra estimar pelo orçamento de EV, mas seria conta minha, não fonte.

5) Não confirmei se a 2ª edição do 13th Age (2025) mudou o dado de escalada ou introduziu algum recurso de monstro — as fontes falam em "monstros revisados" sem detalhar. O que reporto do 13th Age é da 1ª edição, via SRD.

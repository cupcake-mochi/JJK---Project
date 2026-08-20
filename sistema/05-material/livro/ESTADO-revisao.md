# Estado da revisão · Manual da Guilda

Revisão de texto e organização do PDF de mesa. **Nenhum número de regra mudou** em nenhuma
das quatro passadas — verificado por diff de todos os blocos de citação e linhas de tabela
contra o estado inicial.

| | antes | depois |
|---|---|---|
| páginas do PDF | 224 | **225** |
| palavras | 73.858 | **72.943** |
| tabelas | 240 | **221** |
| referências cruzadas quebradas | 43 | **0** |
| termos-chave usados antes de existir | 8 | **0** |
| glossário do livro | não tinha | 66 termos, página 10 |
| índice remissivo | não tinha | 62 termos, página 225 |

---

## O que foi feito, em quatro passadas

### 1 · Referência e navegação

**43 ponteiros cruzados** ganharam número de capítulo e o título exato do sumário. Onze
apontavam para capítulos que não existem com aquele nome — *"capítulo de feitiços"*,
*"de Legados"*, *"de Trilhas"*, *"de energia amaldiçoada"*, *"de objeto amaldiçoado"*.

**Glossário do livro**, 66 termos em 9 blocos, na página 10. Resolve o problema medido: a
palavra `Refino` aparecia 146 vezes e só era explicada no capítulo 10.

**Índice remissivo** no fim, gerado no build por `target-counter` — mesmo mecanismo do
sumário, então não desatualiza.

### 2 · Redundância

- `Regras de ouro` existia **3×** dentro do capítulo 9, com a regra 5 divergindo entre as
  cópias. Sobrou uma, com o fato completo.
- A tabela-mestra de números aparecia **2×** no mesmo capítulo. Sobrou uma, com a coluna
  de cura da outra dobrada dentro.
- O capítulo 10 afirmava que **Classe Passiva 3 não tem nenhuma Passiva**; o capítulo 9
  lista três. Tabela divergente removida, ponteiro para o dono.
- **19 tabelas-prévia** nos Caminhos, que repetiam o texto cinco linhas abaixo.

### 3 · Material de mestre

~2.400 palavras saíram do livro do jogador. O detalhe de cada corte e onde a funcionalidade
precisa voltar a existir está em **`REMOCOES-material-de-mestre.md`**.

Dois pedaços não saíram, porque eram regra de jogador presa na seção errada: os **quatro
estágios de dano na alma** foram para o capítulo 4, e a **tabela de Rotina** para o
capítulo 13.

### 4 · Texto que confundia

- **`Oculta`** era definida por seis negações e por um delta contra um padrão que o livro
  nunca enuncia (*"passa de não rola para rola"*). Reescrita em positivo.
- **`Talha`** aparece em **9 armas** e depende inteiramente do `Bloquear`, que é regra
  **opcional** do apêndice. Nada avisava. O capítulo 4 já avisava o mesmo no `Incapacitado`;
  agora o capítulo 11 avisa também.
- **`Emaranha`** dizia *"dá acesso a agarrar"*; agora diz o que você faz.

---

## Validação contra sistemas atuais

O que a comunidade elogia e reclama em manual de RPG, e onde este fica.

### ✅ O que funciona aqui

| prática elogiada | estado |
|---|---|
| **índice remissivo** — a omissão nº 1 apontada por quem usa livro na mesa | tem, 62 termos |
| **jargão definido antes do uso** | glossário na página 10, e 0 termos-chave descobertos |
| **cada seção declara se é para ler ou consultar** | a introdução declara os 15, um a um |
| **como se rola aparece cedo** — o *Star Trek Adventures 2e* põe isso na página 253 e virou piada | capítulo 1, página 16 |
| **exemplo jogável por conceito** | ~60 blocos de exemplo com nome próprio e conta inteira |
| **regra rápida em cima, exceção embaixo** | as regras vivem em caixa destacada; a exceção vem no corpo |

### ⚠ O risco que este formato corre

**O glossário do D&D 2024 é criticado justamente por ser um glossário.** A crítica tem três
partes: a regra fica partida entre o corpo e o glossário; o leitor precisa adivinhar sob qual
nome a entrada foi arquivada; e há coisas que **só** existem lá, nunca no texto principal.

**Este manual não cai nisso, e foi testado:**

- **Nenhuma das 66 entradas é autoritativa.** Cada uma é uma linha e o número do capítulo
  dono. O cabeçalho diz com todas as letras: *"nada aqui é regra completa"*.
- **Rodei o teste do erro do D&D 2024** — procurar termo que existe no glossário e em lugar
  nenhum mais. Deu **zero**. O teste também pegou dois ponteiros meus apontando para o
  capítulo errado, e os dois foram corrigidos.
- O sumário lista os 66 termos por bloco temático, então não há *"adivinhe o nome da entrada"*.

### ✗ O que este livro não tem, e outros têm

| prática | situação |
|---|---|
| **quick-start jogável de até 20 páginas**, separável para dar aos jogadores | não tem. Foi oferecido e você recusou nesta rodada — a decisão continua aberta |
| **aventura solo que ensina a regra jogando** | não tem. É o padrão-ouro citado em 2026, e é trabalho grande |
| **cartas ou folha de referência de bolso** | a `Tabela de bolso` foi removida como duplicata; uma folha de uma página é outra coisa e não existe |
| **livro do mestre** | não existe, e agora ele tem conteúdo esperando: 2.400 palavras removidas daqui |
| **playtest** | zero sessões. Todo número deste sistema continua sendo previsão |

---

## Um jogador novo se perde?

**Menos do que antes, e dá para dizer onde ainda pode.**

**Resolvido:** ele não encontra mais um termo 146 vezes antes de saber o que é; não é mandado
para capítulos que não existem; não lê a mesma regra em três versões divergentes; e não
escolhe um Caminho sem saber o que ele concede.

**Ainda pode travar em três lugares:**

1. **O capítulo 9 é 15 mil palavras** — um quinto do livro. Ele avisa que é para ler uma vez e
   depois consultar, mas continua sendo o degrau mais alto do manual, e é onde a montagem de
   feitiço acontece.
2. **Buracos declarados aparecem no meio da leitura.** As três Trilhas do Evocador não têm
   entrega escrita, o nível 27 do `Arremate` está vazio, e Pactos não fechou. Está tudo
   declarado com todas as letras, que é o certo — mas quem escolher Evocador vai bater nisso.
3. **Não existe rota de "primeira sessão".** O livro ensina a montar ficha em 8 passos, e não
   ensina a jogar a primeira cena. É o buraco que um quick-start fecharia.

---

## Pendências suas

Nada disto é decisão minha:

- [ ] **Guia no lado conjurador** — pus ele lá porque nenhuma das três Trilhas dele tem
      conteúdo de arma, mas ele é 5/5, meio a meio. Uma linha para trocar se estiver errado.
- [ ] **"Todas as armas" inclui Arma de Fogo** para Bastião e Vanguarda? Foi como eu li. Isso
      faz a rota `Arma de Fogo` do `Batedor` virar especialização, e não acesso.
- [ ] **Onde o `PvP` vai morar** — é a única regra aplicável entre as removidas. Apêndice
      opcional junto do `Bloquear`, ou livro do mestre.
- [ ] **Treino de arma por Caminho existe só aqui**, e este repositório é artefato. Precisa
      voltar para `JJK---Project` com validador, ou some na próxima leva.
- [ ] **Dois bugs do repo-fonte** achados no caminho: a regra 5 das Regras de ouro sem o
      *"Classe 3 ou mais"*, e a tabela de Classe Passiva 3 do capítulo 10 contradizendo o 9.

---

## 5 · Quarta passada: reframe de `Bloquear`, e o quick-start

### `Bloquear` não é regra opcional — é decisão de mesa

Correção sua: `Bloquear` não é "não faz parte do jogo padrão". É uma escolha real do
sistema — Defesa parada ou rolar `2d10` — e as duas são regra completa. A linguagem que
chamava isso de "opcional" foi trocada em **quatro lugares**: a abertura do capítulo 15, a
nota do `Incapacitado` no capítulo 4, a entrada do sumário na introdução, e a nota da
propriedade `Talha` no capítulo 11 (que também parou de soar como alarme — não é mais
"pode não fazer nada, confirme antes de escolher").

### `Oculta` e o padrão de terminar em negativa

`Oculta` tinha seis negações e fechava a frase em *"não faz nada em combate"* — a mesma
última impressão que sobrava era de inutilidade, não da coisa que a propriedade resolve de
verdade (passar por revista e detector). Reescrita para abrir com o que ela **não** muda e
fechar com o que ela **faz**. Mesmo ajuste na nota da `Talha`.

### Quick-start: *Antes da primeira sessão*

Nova peça de frente, entre o vocabulário e o capítulo 1 — **não numerada**, então nenhuma
das 43 referências cruzadas por número de capítulo se move. É o mesmo lugar que o próprio
Ironsworn usa para o dele: o livro abre com a seção de início rápido, e só depois entra na
parte de referência.

**O que tem dentro:**
- resumo de "como jogar" em uma caixa, sem reexplicar o que o capítulo 1 já explica
- a **Kaori**, a mesma ficha de exemplo do capítulo 6, com os mesmos números — não
  diverge, e ganhou gancho de personagem (o clã, a avó, o que ela quer na cena) que o
  exemplo do capítulo 6 não precisava ter
- um feitiço novo dela, `Peso nas Mãos`, montado pelas regras reais do capítulo 9 (Toque
  devolve `Média` = 1 ponto em Classe 1; `Condição` Derrubado custa `Leve` = 1; sobram 3
  pontos = `3d8`) — não é número solto, é conta que fecha
- uma cena de combate guiada, com os dados já rolados e a matemática visível: `Corpo Duro`
  reduzindo 5 de dano a zero, `Peso nas Mãos` derrubando o inimigo com exatamente 14 contra
  14 de vida
- three pontos de decisão sem resposta certa, e um fechamento apontando pros capítulos 1 e 6

**Pesquisado contra a referência do gênero:** o próprio Ironsworn abre com 32 páginas de
início rápido dentro do livro principal — validação direta do formato "dentro do PDF, não
solto". Mothership e a crítica a pregens genéricos apontaram o risco de personagem-exemplo
sem gancho; por isso a Kaori ganhou motivação e segredo, não só números.

**Um bug pego na conferência:** o `build_txt.py` numerou o quick-start como capítulo 1,
empurrando *Como Jogar* pra capítulo 2 — só no `.md` de texto puro, o PDF já tratava certo.
Corrigido antes de fechar.

---

## Para commitar, quando você chegar

**Esta pasta não é um repositório git.** Confirmei: `git rev-parse` falha aqui. O
`JJK---PDF---RPG` está em outro lugar da sua máquina, e este material precisa ser copiado
para lá.

### ⚠ Onde este material vai é decisão sua, e tem uma tensão

O `.gitignore` do `JJK---PDF---RPG` abre com:

> *"Este repositorio e ARTEFATO, nao fonte. Nada aqui e editado a mao."*

E o repositório não tem pasta de livro: só `regra/`, `desenho/`, `manual/` (que é o Fundamento
v7, não o livro) e `ficha/`. **O `manual/*.md` deste projeto e o `build/` são fonte editada à
mão** — pelo contrato escrito do repositório, eles não pertencem a ele.

| o quê | onde faz sentido | por quê |
|---|---|---|
| `Projeto-M-Manual-da-Guilda.pdf` | **`JJK---PDF---RPG`** | é artefato, e o repositório existe para isso |
| `manual/*.md` e `build/` | **`JJK---Project`** | é fonte editada à mão, e a fonte mora lá |
| `REMOCOES-*.md` e `ESTADO-*.md` | **`JJK---Project`** | são registro de decisão, que é o que o CHANGELOG de lá guarda |

### Se você seguir essa divisão

No `JJK---Project` (a fonte), com a pasta copiada para dentro dele:

```bash
git add livro/ REMOCOES-material-de-mestre.md ESTADO-revisao.md && git status
```

E depois:

```bash
git commit -m "livro: revisão de organização e corte de material de mestre

Glossário de 66 termos na frente e índice remissivo no fim, os dois gerados no build.
43 referências cruzadas ganharam número de capítulo; 11 apontavam para capítulo inexistente.

Redundância: Regras de ouro existia 3x com a regra 5 divergindo, tabela-mestra 2x,
19 tabelas-prévia nos Caminhos. A tabela de Classe Passiva do cap.10 contradizia o cap.9.

~2.400 palavras de material de mestre saíram do livro do jogador. Os quatro estágios de
dano na alma e a tabela de Rotina eram regra de jogador na seção errada, e mudaram de
capítulo em vez de sair.

Os cinco Caminhos passam a declarar o que concedem. Treino de arma por Caminho foi
escrito pela primeira vez: não existia neste livro nem em regra/06 e regra/14.

Nenhum número de regra mudou, verificado por diff de blocos de citação e tabelas."
```

No `JJK---PDF---RPG` (o artefato), substituindo o PDF:

```bash
git add manual/ && git commit -m "recorte: Manual da Guilda revisado, 225 páginas" && git push
```

### ⚠ Dois avisos antes de fechar

**1 — O README do artefato estima o livro em 140 páginas.** Ele está em **225**. A conta de
lá (*"as 112 mil palavras que o rascunho publicou viraram 62 páginas… o livro fecha perto de
140"*) não bateu. Vale corrigir aquele parágrafo na mesma leva, senão ele fica mentindo sobre
o próprio material.

**2 — Rode os validadores do `JJK---Project` antes do `subir.sh`**, e confira `PULADA=0`. As
mudanças de treino de arma e de Classe Passiva mexem em coisa que os validadores de lá
conferem.

---

## Arquivos

| arquivo | o que é |
|---|---|
| `Projeto-M-Manual-da-Guilda.pdf` | o livro, 225 páginas |
| `Projeto-M-Manual-da-Guilda-REVISAO.docx` | mesmo conteúdo sem diagramação, para comentar |
| `Projeto-M-Manual-da-Guilda-TEXTO.md` | texto corrido, para diff e Ctrl+F |
| `manual/*.md` | **a fonte.** É aqui que se edita |
| `build/build.py` | markdown → PDF. Gera o índice remissivo |
| `build/build_txt.py` | markdown → texto corrido *(novo nesta revisão)* |
| `REMOCOES-material-de-mestre.md` | o que saiu, por quê, e onde precisa voltar |
| `manual/07-glossario.md` | o glossário *(novo nesta revisão)* |

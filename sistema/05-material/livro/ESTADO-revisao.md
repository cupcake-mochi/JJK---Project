# Estado da revisão · Manual da Guilda

> ## Passada de termos — FASE 1 CONCLUÍDA em 21/08/2026, fases 3 e 4 abertas
>
> **Terceira revisão, sobre o vocabulário.** Nasceu de duas reclamações de playtest: jogador
> novo não se contextualiza, e leitor de leitura dinâmica encontra um termo e não acha a
> definição. A regra que manda nela é a seção *Todo termo tem um destino* da
> `REGRA-DE-VOZ.md`.
>
> ### O diagnóstico, medido contra D&D 2024 e GURPS 4e
>
> Os dois manuais foram lidos inteiros (397 e 576 páginas) e medidos junto com este livro:
>
> | | D&D 2024 | GURPS 4e | este livro |
> |---|---:|---:|---:|
> | palavras por frase (mediana) | 16 | 14 | **13** |
> | palavras por parágrafo (mediana) | 41 | 83 | **35** |
> | frases com mais de 30 palavras | 11,3% | 9,2% | **4,0%** |
> | "você" por mil palavras | 19,65 | 0,43 | **15,65** |
> | "veja"/"consulte" por mil | **1,46** | 0,99 | **0,02** |
> | exemplos por mil palavras | 0,61 | 1,41 | **0,06** |
>
> **O livro não tem problema de prolixidade** — é mais enxuto que os dois em toda medida de
> tamanho. O problema é de **ausência**: remete 73 vezes menos que o D&D, e dá 10 vezes
> menos exemplo. O jogador encontra um termo marcado e não tem para onde ir.
>
> *O caso que criou a regra:* uma leitora travou em `colado` no capítulo 11, com a definição
> seis palavras adiante na mesma frase. Ela não leu como definição porque nada ali dizia que
> era uma. **Ela fez o certo com um livro que estava errado.**
>
> ### Feito nesta passada
>
> **A checagem de termo sem destino entrou no `conferir-voz.py`.** Ela lê os dois lados — os
> termos saem do texto, os destinos saem do glossário e das estreias — e o teto é trava de
> crescimento, não meta. Corte: `5` usos, ou aparecer em `3` capítulos.
>
> **O buraco caiu de 71 para 5 termos**, e a maior parte não foi escrita — foi conserto de
> cinco pontos cegos do próprio validador, cada um testado com perturbação positiva e
> negativa em cópia isolada:
>
> | o que ele não reconhecia como destino | termos que escondia |
> |---|---:|
> | o encaixe `Nível N: `Termo`.` das habilidades de Trilha e Caminho | 4 |
> | título de seção `##` a `######` | 13 |
> | negrito sem crase, `**Termo** —`, do catálogo de Perícias | 5 |
> | definição fora da segunda coluna da tabela | 21 |
> | limiar de tamanho cortando por um caractere, e célula não marcada | 5 |
>
> **O glossário ganhou 49 entradas**, em três seções novas — `Condições`, `Formas, Melhorias
> e Restrições do Fundamento` e `Caminhos e Trilhas` — mais linhas em `Rolagens`, `Números da
> ficha`, `Turno` e `Equipamento`. *Toda definição é texto que já existia numa tabela ou em
> prosa do livro:* nenhuma frase nova, nenhum número novo. O `guard_numeros.py` acusou 26
> diferenças, todas citação de capítulo ou valor copiado de tabela existente, conferidas uma
> a uma contra a fonte.
>
> **O teto está em `0` e daqui em diante ele é ZERO.** Termo novo que passe o corte sem
> entrada no vocabulário nem estreia definida falha o `conferir-voz.py --estrito`.
>
> ### O falso alarme que a leitura das fontes desfez
>
> **`Leve`, `Média` e `Pesada` somam 177 usos, e eu diagnostiquei ambiguidade onde não
> havia.** *A peça 19 §2.3 de `03-mecanica` registra a decisão com todas as letras: o nível de
> uma condição **é** o tier de preço do manual — a mesma escada, de propósito.* E o manual já
> escreve isso em dois lugares, o capítulo 4 e o capítulo 9, na mesma frase: *o nível faz duas
> coisas — é o que a condição custa para comprar, e o que custa para tirar*.
>
> **Não era decisão de design; era falta de entrada no índice**, igual aos outros 44. *Ler a
> peça-fonte antes de propor derrubou um lote inteiro de "cruzamento entre duas peças" para
> redação simples.*
>
> ### O rótulo de família veio do PHB 2024
>
> As três entradas usam **`Leve`** `[Nível]`, com o rótulo entre colchetes. *É o padrão das 41
> entradas ambíguas do Glossário de Regras do PHB — `Cone [Área de Efeito]`, `Surdo
> [Condição]` —, e ele só rotula onde o nome sozinho confunde.* **O GURPS não tem equivalente:
> usa `Leve`/`Média`/`Pesada` como percentual de custo e nunca dá entrada a eles.**
>
> ### E o que a passada ainda nem começou
>
> **Fase 3 — remissões.** Hoje são **8** em 374 seções, e 5 delas num capítulo só. O formato
> `seção *Nome*` já existe e o `conferir-voz.py` já valida se o alvo existe. É escrita, não
> engenharia.
>
> **Fase 4 — reordenação e exemplos.** **22 seções** têm mais de 250 palavras de regra antes
> da primeira tabela. As piores: `Aptidões de barreira` (511), `Regra rápida do turno` (514),
> `Tipos de dano` (549), e as oito Origens com cerca de 350 cada. No capítulo 11, a seção
> `Armas` passa **151 linhas** de regra antes da primeira arma concreta, e depois o catálogo
> se fragmenta em uma tabela por grupo. *O D&D gasta distância parecida, mas as quatro
> tabelas dele ficam coladas e a prosa dos grupos vem depois.*
>
> ### Estado para retomar
>
> **Nada disto foi commitado ainda.** Arquivos tocados: `REGRA-DE-VOZ.md`, `conferir-voz.py`,
> `manual/07-glossario.md`, e este documento.
>
> **Verde em tudo:** `conferir-voz.py --estrito` sai `0`, os 19 validadores de `03-mecanica`
> saem `0` com `PULADA=0`, e o `conferir-repositorio.py` sai verde.
>
> *O glossário do livro não entra no recorte da entrega, então esta passada não mexe em
> `finalizado/`.* **Commit é só do repositório de trabalho.**

> ## Passada de voz — concluída em 20/08/2026
>
> Uma **segunda revisão** passou por todo o livro, sobre a voz do texto. O documento que
> manda nela é a `REGRA-DE-VOZ.md`, nesta mesma pasta. Leia ela antes de escrever qualquer
> coisa nova no manual, e antes desta seção histórica.
>
> **Os 18 arquivos de `manual/` passaram.** O `conferir-voz.py` sai em zero.
>
> | | antes | depois |
> |---|---|---|
> | achados do `conferir-voz.py` | 507 | **0** |
> | tabelas com nome | 1 | **212** |
> | títulos começando com artigo | 131 | **0** |
> | títulos que eram pergunta ou frase | 98 | **0** |
> | o texto falando do próprio livro | 26 | **0** |
> | referências a seção que não resolvem | 0 | **0** |
> | palavras | 74.123 | **72.776** |
> | **números de regra alterados** | — | **0** |
>
> As 1.347 palavras que saíram eram moldura de leitura, justificativa de projeto e
> comparação com outros sistemas. Nenhuma regra, nenhum número, nenhuma exceção.
>
> **O que a passada não fez**, e continua valendo como trabalho futuro: rebaixar título de
> exceção para negrito correndo no parágrafo; criar um segundo estilo de caixa para aviso
> lateral (hoje o `>` serve só para resumo de regra); e quebrar o capítulo 9, que continua
> sendo 15 mil palavras, um quinto do livro.
>
> **Os trechos `TRIAR` foram lidos um a um.** Eram 21; quatro saíram (justificativa de
> projeto: *"e é por isso que ela é um degrau de nível 27"*, dois *"de propósito"* sobre
> balanceamento, e *"isso está escrito de propósito"*). Os **17 que sobraram ficam**: são
> causa dentro da ficção, ou fato de mesa amarrado a número real. O
> `conferir-voz.py --inventario` continua listando eles, e listar não é acusar.
>
> **Uma redundância achada no caminho e não resolvida:** as tabelas de condição do
> capítulo 9 repetem o conteúdo das do capítulo 4. Estão nomeadas de forma parecida de
> propósito, para a duplicação ficar visível no índice remissivo.
>
> **Onde cada coisa mora, porque isto já custou um lote inteiro de trabalho perdido:**
>
> | o quê | onde | repositório |
> |---|---|---|
> | fonte `manual/*.md`, `build/`, validadores | `sistema/05-material/livro/` | `JJK---Project` (`Claude 2/.git`) |
> | PDF e docx prontos | `finalizado/livro/` | `JJK---PDF---RPG` (`Claude 2/finalizado/.git`) |
>
> Existiu uma terceira cópia em `/media/mizuki/HD Externo II/Claude/PDF - Sistema/`, **fora
> de qualquer repositório**. Um lote inteiro foi escrito lá por engano e não entrou em
> commit nenhum. Ela foi renomeada para `PDF - Sistema.OBSOLETO` e não deve ser usada.
>
> **Ferramentas desta passada**, todas nesta pasta:
>
> | ferramenta | o que faz |
> |---|---|
> | `conferir-voz.py` | 7 checagens de título e moldura, mais referências de seção e lista de triagem à mão |
> | `build/guard_numeros.py` | compara dois arquivos e acusa todo número que mudou |
> | `build/extrai_antes.py` | recorta do `Projeto-M-Manual-da-Guilda-TEXTO.md` o "antes" de um capítulo, para alimentar o guard |
>
> **O procedimento por arquivo**, na ordem: extraia o "antes" *antes* de editar; reescreva;
> rode o guard e **explique cada diferença**; rode `conferir-voz.py`; confira as entradas do
> glossário que apontam para aquele capítulo (`conferir-voz.py --so <arquivo>` lista elas).
>
> Estado hoje: **346 achados restantes**, 62 tabelas nomeadas, 0 referências quebradas,
> **0 números de regra alterados**.

Revisão de texto e organização do PDF de mesa, em cinco passadas. **Nenhum número de regra
mudou** em nenhuma delas — verificado por diff de todos os blocos de citação e linhas de
tabela contra o estado inicial, a cada passada.

| | antes | depois |
|---|---|---|
| páginas do PDF | 224 | **230** |
| palavras | 73.858 | **74.123** |
| tabelas | 240 | **214** |
| referências cruzadas quebradas | 43 | **0** |
| termos-chave usados antes de existir | 8 | **0** |
| glossário do livro | não tinha | 66 termos |
| índice remissivo | não tinha | 62 termos |
| quick-start jogável | não tinha | **"Antes da primeira sessão"**, com cena guiada |

O livro cresceu em páginas apesar de ter menos tabelas e menos palavras de mestre: o
glossário, o índice remissivo e o quick-start são texto novo, e pesam mais que o que saiu.

---

## O que foi feito, em cinco passadas

### 1 · Referência e navegação

**43 ponteiros cruzados** ganharam número de capítulo e o título exato do sumário. Onze
apontavam para capítulos que não existem com aquele nome — *"capítulo de feitiços"*,
*"de Legados"*, *"de Trilhas"*, *"de energia amaldiçoada"*, *"de objeto amaldiçoado"*.

**Glossário do livro**, 66 termos em 9 blocos, logo depois da introdução. Resolve o problema
medido: a palavra `Refino` aparecia 146 vezes e só era explicada no capítulo 10.

**Índice remissivo** no fim, gerado no build por `target-counter` — mesmo mecanismo do
sumário, então não desatualiza.

### 2 · Redundância

- `Regras de ouro` existia **3×** dentro do capítulo 9, com a regra 5 divergindo entre as
  cópias. Sobrou uma, com o fato completo.
- A tabela-mestra de números aparecia **2×** no mesmo capítulo. Sobrou uma.
- O capítulo 10 afirmava que **Classe Passiva 3 não tem nenhuma Passiva**; o capítulo 9
  lista três. Tabela divergente removida, ponteiro para o dono.
- **19 tabelas-prévia** nos Caminhos, que repetiam o texto cinco linhas abaixo.
- A moeda de orçamento (`custa` / `devolve`) ficou órfã nas tabelas de propriedade e
  restrição de arma depois que o orçamento saiu do livro do jogador (passada 3). Removida.

### 3 · Material de mestre

~2.400 palavras saíram do livro do jogador. O detalhe de cada corte e onde a funcionalidade
precisa voltar a existir está em `REMOCOES-material-de-mestre.md`.

Dois pedaços não saíram, porque eram regra de jogador presa na seção errada: os **quatro
estágios de dano na alma** foram para o capítulo 4, e a **tabela de Rotina** para o
capítulo 13.

### 4 · Texto que confundia

- **`Oculta`** era definida por seis negações e por um delta contra um padrão que o livro
  nunca enuncia (*"passa de não rola para rola"*). Reescrita em positivo.
- **`Talha`** aparece em **9 armas** e depende do `Bloquear`. Nada avisava. Agora avisa em
  dois lugares — sem soar como alarme de que a arma "pode não fazer nada".
- **`Emaranha`** dizia *"dá acesso a agarrar"*; agora diz o que você faz.
- **`Bloquear` não é regra opcional — é decisão de mesa.** A linguagem que chamava o
  apêndice de "fora do jogo padrão" foi trocada em quatro lugares: a abertura do
  capítulo 15, a nota do `Incapacitado` no capítulo 4, o sumário da introdução, e a nota
  da `Talha` no capítulo 11.

### 5 · Quick-start: *Antes da primeira sessão*

Peça de frente, entre o vocabulário e o capítulo 1 — **não numerada**, então nenhuma das
43 referências cruzadas por número de capítulo se move. Mesmo lugar que o Ironsworn usa
para o dele: o livro abre com início rápido, e só depois entra na parte de referência.

**O que tem dentro:** um resumo de "como jogar" sem reexplicar o capítulo 1; a **Kaori**,
a mesma ficha de exemplo do capítulo 6 (mesmos números, sem divergir), com gancho de
personagem que o exemplo original não precisava ter; um feitiço novo dela, `Peso nas Mãos`,
montado pelas regras reais do capítulo 9 (Toque devolve `Média` = 1 ponto em Classe 1,
`Condição` Derrubado custa `Leve` = 1, sobram 3 pontos = `3d8` — não é número solto, é
conta que fecha); uma cena de combate guiada com a matemática visível; e um fechamento
apontando para os capítulos 1 e 6.

**Isto resolve uma pendência antiga do projeto.** O `README.md` da raiz registra que o
quick-start foi *"abandonado na v0.102, por decisão do Mizuki: 'pode abandonar a ideia do
quick start, eu tô fazendo o PDF direto'"* — a leitura usada aqui foi que a decisão trocou
o **formato** (sem pipeline separado) e não a **existência**: o texto acabou indo direto
para dentro do PDF, que é exatamente onde ele está agora.

---

## Validação contra sistemas atuais

O que a comunidade elogia e reclama em manual de RPG, e onde este fica.

| prática elogiada | estado |
|---|---|
| índice remissivo | tem, 62 termos |
| jargão definido antes do uso | glossário no começo, 0 termos-chave descobertos fora dele |
| cada seção declara se é para ler ou consultar | a introdução declara os 15, um a um |
| como se rola aparece cedo (o *Star Trek Adventures 2e* põe isso na página 253) | capítulo 1, logo no começo |
| exemplo jogável por conceito | ~60 blocos de exemplo com nome próprio e conta inteira |
| quick-start jogável dentro do próprio livro (molde do Ironsworn) | tem, "Antes da primeira sessão" |

**O risco do glossário-estilo-D&D-2024** (regra partida entre corpo e glossário, termo que
só existe lá) foi testado, não só evitado por intenção: rodei uma varredura procurando
termo que existe só no glossário e em lugar nenhum mais. Deu zero — pegou dois ponteiros
meus apontando para capítulo errado, os dois corrigidos.

**O que ainda falta**, comparado com outros sistemas: aventura solo que ensina jogando
(padrão-ouro citado em 2026, trabalho grande); cartas ou folha de referência de bolso; um
livro do mestre — que agora tem conteúdo esperando, as ~2.400 palavras removidas daqui;
e playtest — zero sessões, todo número deste sistema continua sendo previsão.

---

## Um jogador novo se perde?

**Menos do que antes.** Não encontra mais um termo 146 vezes antes de saber o que é; não é
mandado para capítulos que não existem; não lê a mesma regra em três versões divergentes;
não escolhe um Caminho sem saber o que ele concede; e agora tem uma cena pronta para jogar
antes de precisar entender o livro inteiro.

**Ainda pode travar em dois lugares:**

1. **O capítulo 9 é 15 mil palavras** — um quinto do livro. Avisa que é para ler uma vez e
   depois consultar, mas continua sendo o degrau mais alto do manual.
2. **Buracos declarados aparecem no meio da leitura.** As três Trilhas do Evocador não têm
   entrega escrita, o nível 27 do `Arremate` está vazio, e Pactos não fechou. Declarado com
   todas as letras, que é o certo — mas quem escolher Evocador vai bater nisso.

---

## Pendências suas

Nada disto é decisão minha:

- [ ] **Guia no lado conjurador** — pus ele lá porque nenhuma das três Trilhas dele tem
      conteúdo de arma, mas ele é 5/5, meio a meio. Uma linha para trocar se estiver errado.
- [ ] **"Todas as armas" inclui Arma de Fogo** para Bastião e Vanguarda? Foi como eu li.
      Isso faz a rota `Arma de Fogo` do `Batedor` virar especialização, e não acesso.
- [ ] **Onde o `PvP` vai morar** — é a única regra aplicável entre as removidas. Apêndice
      opcional junto do `Bloquear`, ou livro do mestre.
- [ ] **Treino de arma por Caminho existe só aqui** — escrito pela primeira vez nesta
      revisão, e ainda não tem validador nem existe em `sistema/03-mecanica/`.
- [x] ~~**Duas divergências achadas no caminho, bug do sistema e não do livro:** a regra 5
      das Regras de ouro do Fundamento sem o *"Classe 3 ou mais"*, e a tabela de Classe
      Passiva 3 do capítulo de Aptidões contradizendo o Fundamento.~~ **Fechadas na v0.107
      do projeto, as duas do lado da fonte — o livro já estava certo nas duas.** A regra 5
      estava em `manual/gerador/partE.js` e não em `03-mecanica/`, e consertar ela levou o
      manual do Fundamento para a **v7.11**; a tabela de Classe Passiva era a §4 da peça 11,
      errada em **duas** das três linhas (a `2` listava cinco de sete e a `3` dizia `—`), e
      ela ganhou a checagem `4k` do `conferir-manual.py` comparando as três contra o `.docx`.

---

## O que já foi commitado

Localmente, ainda não enviado ao GitHub:

| repositório | commit | conteúdo |
|---|---|---|
| `JJK---Project` (fonte) | `livro: primeiro texto de mesa completo, com quick-start` | esta pasta inteira — fonte, build, PDF, docx, txt, e os dois documentos de decisão |
| `JJK---PDF---RPG` (artefato) | `livro: primeiro recorte do Manual da Guilda completo` | só o PDF e o .docx, na pasta livro/ de lá — sem fonte, sem documento de decisão, seguindo o próprio contrato daquele repositório |

Rodei `conferir-repositorio.py` antes de cada commit; os dois passaram limpos. O commit na
fonte não tocou em nenhum dos arquivos que já estavam modificados e não commitados por
outra sessão (`sistema/03-mecanica/06`, `07`, `08`, entre outros) — só a pasta nova foi
adicionada ao stage.

## Arquivos

| arquivo | o que é |
|---|---|
| `Projeto-M-Manual-da-Guilda.pdf` | o livro, 230 páginas |
| `Projeto-M-Manual-da-Guilda-REVISAO.docx` | mesmo conteúdo sem diagramação, para comentar |
| `Projeto-M-Manual-da-Guilda-TEXTO.md` | texto corrido, para diff e Ctrl+F |
| `manual/*.md` | a fonte, 18 arquivos. É aqui que se edita |
| `manual/07-glossario.md` | o glossário |
| `manual/08-inicio-rapido.md` | o quick-start |
| `build/build.py` | markdown → PDF. Gera o índice remissivo |
| `build/build_docx.py` | markdown → docx de revisão |
| `build/build_txt.py` | markdown → texto corrido |
| `README.md` | o que esta pasta é, e como regerar |
| `REMOCOES-material-de-mestre.md` | o que saiu, por quê, e onde precisa voltar |

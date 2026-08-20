# Estado da revisão · Manual da Guilda

> ## ⚠ Passada de voz em andamento — leia antes de mexer
>
> Desde 20/08/2026 corre uma **segunda revisão**, sobre a voz do texto, e ela está pela
> metade. O documento que manda nela é a `REGRA-DE-VOZ.md`, nesta mesma pasta. Leia ela
> antes desta seção histórica.
>
> **8 dos 18 arquivos de `manual/` já passaram:** `90-apendice-bloquear` (piloto),
> `10-como-jogar`, `11-o-turno`, `12-pericias-e-oficios`, `15-dano-e-condicoes`,
> `20-criacao-de-personagem`, `25-origens`. Faltam 10.
>
> **O PDF e o docx publicados em `finalizado/livro/` estão meio revisados de propósito.**
> Capítulos 1 a 7 com a voz nova e tabela nomeada; do 8 em diante, a voz antiga. Isso não é
> inconsistência de projeto — é uma passada que ainda não terminou. Foi decisão do Mizuki
> publicar no meio, porque o conteúdo já melhorou e nenhum número de regra mudou.
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
- [ ] **Duas divergências achadas no caminho, bug do sistema e não do livro:** a regra 5
      das Regras de ouro do Fundamento sem o *"Classe 3 ou mais"*, e a tabela de Classe
      Passiva 3 do capítulo de Aptidões contradizendo o Fundamento.

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

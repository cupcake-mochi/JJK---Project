# Changelog

Registro do que muda entre uma leva de material e a seguinte. Cada versão fecha quando o material daquela fase é revisado e aprovado.

Formato: `## [versão] — data` com as seções `Adicionado`, `Alterado`, `Removido` e `Decidido` (decisão de design que fecha uma pergunta em aberto).

---

## [0.110] — 21/08/2026

**A versão em que a fila da revisão do livro fechou, e três dos quatro itens dela renderam menos trabalho do que a conta previa — sempre pelo mesmo motivo.**

### Adicionado — três exemplos inline, no formato medido do D&D

*`Controle` no capítulo 9, `Cobrir-se de energia` e `Kokusen` no 10.* **Somam dez no livro, todos entre 15 e 24 palavras, dentro da frase, contra a mediana de `23` do PHB.**

> *Os dois de refino usam `refino 6` porque ele divide exato nas duas fórmulas — `6/3 + 1` e `1,5 × 6` —, então o exemplo não depende do arredondamento, que é regra à parte.*

### Alterado — três habilidades com dois efeitos colados por um "E"

**O `Repuxo` juntava o empurrão e o fim da desvantagem por estar colado; o `Ferrolho` juntava a recarga e a mesma desvantagem; o `Alicerce` juntava benefício, custo, como sair e quando se escolhe.** *Os efeitos independentes ganharam linha própria dentro do bloco.*

**Não foi preciso formato novo:** *o `Corpo Duro` e o `Puxar Para Si` já usam quebra de linha dentro do bloco `>` desde sempre.* **A terceira camada cabe aqui porque a quebra existe — foi por ela não existir que a mesma tentativa falhou na tabela de condições, na v0.108.**

### Achado — o sexto e o sétimo caso do erro de contar proxy

**A fila previa `38` seções sem exemplo e `6` habilidades com três efeitos. Os números reais foram `3` e `3`.**

*Excluindo seção que já tem tabela, as 38 viraram 13; e das 13, dez já se exemplificavam de quatro jeitos que filtro nenhum pega:*

| seção | o que o filtro não via |
|---|---|
| `Passos` | a seção **seguinte** é o *Exemplo guiado: o primeiro feitiço da Régua* |
| `Rolagem de Bloquear` | o apêndice tem uma seção `## Exemplo` inteira, com a Rina |
| `Feitiços por nível` | traz *"São 3 no nível 2, 16 no nível 20 e 24 no nível 30"* |
| `Coro` | traz *"Com uma invocação, cada um entrega metade"* |
| `Técnica Máxima`, `Energia` | tabela com os valores por faixa de nível |

**E das seis habilidades, quatro tinham um efeito com partes, não três efeitos:** *o `Não Acabou` dá Reação, movimento e golpe **do mesmo gatilho**.* **O contador somava palavras-chave distintas.**

> **São sete casos em três versões, e o mecanismo nunca mudou: medir presença de palavra-chave numa população onde boa parte dos itens não precisa daquele elemento.** *O filtro de exemplo foi refinado quatro vezes e errou nas quatro, porque cada versão presumia um formato de exemplificação e o livro usava outro.* **Este livro exemplifica e sinaliza muito mais do que qualquer contagem automática enxerga.**

---

## [0.109] — 21/08/2026

**A versão que leu as 74 habilidades de Trilha e Caminho uma a uma, achou uma lacuna em vez das dezenas que a conta previa, e achou de graça um defeito maior no caminho.**

### Corrigido — `vida temporária` tinha três grafias, e duas ficavam fora da própria regra

**A v0.108 escreveu a regra de `vida temporária` e três efeitos não usavam esse nome.** *O `Aprumo` da Trilha `Executor` e a `Crosta` da Trilha `Arremate` diziam **"PV temporário"**; a Melhoria `Rasga Escudo` dizia **"pontos de vida temporários"**.*

**Ninguém saberia se as três têm o mesmo teto de metade da vida máxima, o mesmo relógio de fim de cena e a mesma regra de não acumular** — que é exatamente o que a regra nova responde para quem escreve `vida temporária`. *Unificadas nas três.*

> *O termo escapou de toda checagem por não estar entre crases até a v0.108, e as três grafias divergentes existiam desde que cada habilidade foi escrita.* **Uma regra nova não alcança o texto que chama a coisa por outro nome.**

### Corrigido — o `Aterro` não dizia se depende do `Alicerce`

**A Trilha `Muro` tem o `Alicerce` no nível 2, que liga e desliga — *"enquanto o `Alicerce` estiver de pé"* — e o `Aterro` no nível 11, que descrevia uma aura de terreno difícil sem dizer se ela precisa do `Alicerce`.** *Dois mestres resolveriam diferente, e é o filtro do projeto reprovando.*

**A fonte já respondia:** *o `DESENHO-trilhas.md` classifica o `Aterro` como `permanente`, e o preço de `0,71` fatias foi calculado assim.* **Era informação perdida na transposição, não decisão nova** — o manual ganhou *"Sempre ligado, e não depende do `Alicerce`"*.

### Achado — a lacuna de gatilho e duração não existia, e foi o quinto caso do mesmo erro

**A medição da v0.108 dizia que estas habilidades têm `45%` de gatilho contra `72%` do PHB, e `5%` de duração contra `21%`.** *Lidas as 74, a lacuna real é uma.*

*As sem gatilho são **permanentes*** — `Estopim`, `Rebote`, `Ferrolho`, `Empunhadura`. *As sem duração são **instantâneas*** — `Corpo Duro`, `Encontrão`, `Sentinela`, `Rompante`. *E as de efeito contínuo dizem:* `Acelerar` traz `2× por cena`, `Ápice` traz `1× por cena`, `Segundo Corpo` traz *uma vez por descanso curto*, `Braseiro` traz *some no fim da cena*.

**O PHB tem mais gatilho porque as habilidades dele são mais longas e condicionais — mediana de `62` palavras contra `26` daqui —, e não porque estas estejam incompletas.**

> **É a quinta conta desta sequência que dá número alto por medir presença de palavra-chave numa população onde a maioria dos itens não precisa daquele elemento.** *As outras quatro estão na entrada da v0.108.* **O padrão está registrado no `sistema/ESTADO-ATUAL.md`, acima das pendências, porque ele vai voltar.**

---

## [0.108] — 21/08/2026

**A versão em que o livro ganhou vocabulário navegável, e a régua para escrever nele saiu de dois manuais medidos em vez de opinião.** *O D&D 2024 e o GURPS 4e foram lidos inteiros — 397 e 576 páginas — e comparados com o Manual da Guilda em sete padrões de escrita.* **E uma regra que oito efeitos usavam desde sempre foi escrita pela primeira vez.**

### Decidido — `vida temporária` tem regra, e ela nasceu de um buraco de oito anos-luz

**Oito efeitos concediam vida temporária e nenhum documento do projeto dizia como ela funciona.** *`Apoio`, `Fluxo`, `Aprumo`, `Crosta` e quatro feitiços prontos.* **Procurado no manual inteiro e nas dezenove peças: nada.**

> ***Decisão do Mizuki:*** **gasta antes da vida real · não acumula, fica a maior e nunca a soma · teto de metade da vida máxima · some no fim da cena.** *O mestre pode deixar atravessar para a cena seguinte quando a preparação foi deliberada.*

**A duração curta é o que sustenta o preço, e isso não foi escolha de sabor.** *A régua do projeto diz que dano evitado converte `1` pra `1`, e um ponto de feitiço vale `1d8` = `4,5` de dano.* **O `Apoio` entrega `3` por ponto — `0,67×` —, e o desconto de um terço só fecha se a vida temporária for desperdiçada com frequência.** *Fosse ela até o descanso longo, como no d20, o `Apoio` estaria subvendido em 50%.*

**O teto morde, e o Mizuki decidiu com o corte à vista:** *o `Fluxo` entrega de `2` a `14` e nunca é cortado; o `Apoio` puro entrega de `9` a `63` e é cortado em **toda** Classe, inclusive na 1.* ***"Vai existir habilidade que passa e habilidade que não chega perto — é gestão de recurso, a mesma escolha de em que altura gastar a cura."***

> **Numerada `§5.1.1` da peça 1, e não `5.2`.** *Numerar como `5.2` empurraria as quatro seções seguintes e quebraria cinco ponteiros vivos — a peça 19 cita `§5.2` e `§5.5`, a 18 cita `§5.3`, a 15 cita `§5.4` duas vezes.* **A renumeração chegou a ser feita e foi revertida antes de fechar.**

*O termo passou a ser escrito entre crases.* **Antes ele escapava de toda checagem por não ser marcado** — a checagem de termo sem destino só enxerga o que tem crase.

### Adicionado — a checagem de termo sem destino, no `conferir-voz.py`

**Termo entre crases é promessa: quem lê entende que aquilo é nome de coisa do sistema e sai procurando a definição.** *Uma leitora do playtest travou em `colado`, com a definição seis palavras adiante na mesma frase — ela não leu como definição porque nada ali dizia que era uma.*

A checagem lê os dois lados: os termos saem do texto, os destinos saem do vocabulário e das estreias. Corte de `5` usos ou `3` capítulos. **O buraco foi de `71` para `0`, e o teto agora é zero permanente.**

> **A maior parte não foi escrita — foi conserto de cinco pontos cegos do próprio validador**, cada um com perturbação positiva e negativa em cópia isolada: o encaixe `Nível N: \`Termo\`.` das habilidades (4 termos), título de seção (13), negrito sem crase do catálogo de Perícias (5), definição fora da segunda coluna da tabela (21), e o limiar de tamanho cortando por um caractere (5).

### Alterado — as catorze condições viraram entradas em prosa

**Formato do PHB: frase de âncora dizendo quando a condição vale, depois um parágrafo por efeito, cada um com nome próprio.** *Vocabulário fechado e reutilizado —* `Deslocamento` · `Seus ataques` · `Contra você` · `Ação` · `Testes` · `Sai quando` *—, nove nomes para catorze condições. A tabela virou `Condições em uma linha`, no fim da seção.*

> **A primeira tentativa reproduziu o defeito que queria consertar, e o Mizuki pegou.** *Os rótulos foram propostos dentro da célula de tabela, e ele leu: o ponto virava vírgula, e o negrito não indicava que a explicação vinha em seguida.* **Fui ver a formatação real do PHB com `pdftotext -layout`: o que separa os efeitos não é o ponto, é a quebra de parágrafo com indentação.** *O rótulo só fecha o nome de um bloco que já está isolado na página.* **Onde não há parágrafo, a forma não funciona.**

### Alterado — o capítulo 11 reordenado, e a divisão do PHB foi rejeitada por medida

**O defeito não era a distância até a tabela; era que a tabela que chegava primeiro não servia para escolher arma.** *O `Índice A–Z` trazia `arma | categoria | treino` — nenhum dado de jogo — e os dados viviam espalhados em treze tabelas de grupo.*

**A divisão do PHB não serve aqui.** *Lá a proficiência é por arma, então ele corta em `simples/marcial × corpo a corpo/distância`.* **Aqui o treino mora na categoria — treinar `Lâmina Longa` libera as oito — e são três listas: simples (26 armas), marcial (19) e de fogo (7).** *Copiar o corte quebraria o vínculo entre categoria e treino, que é regra.*

| | antes | depois |
|---|---:|---:|
| capítulo | 601 linhas | **486** |
| linhas de tabela no catálogo | 132 | **60** |
| tabelas onde uma arma aparece | 14 | **1** |
| armas | 52 | **52** |

### Adicionado — vocabulário, remissões e rótulo de categoria

**O vocabulário ganhou 49 entradas**, em três seções novas — `Condições`, `Formas, Melhorias e Restrições do Fundamento` e `Caminhos e Trilhas`. *Toda definição é texto que já existia em tabela ou prosa: nenhuma frase nova, nenhum número novo.*

**Sete remissões**, achadas por medida e não por atacado: termo cuja primeira aparição no livro é fora do capítulo dono. *Eram 23 casos; 5 eram nome homônimo, 7 já apontavam, 3 são do início rápido que é autocontido de propósito, e 1 já estava coberto.*

**Cinco rótulos de categoria, de 34 candidatos** — *o livro já se anuncia sozinho na maioria: "a **Restrição** `Carregar`", "a **Trilha** `Sutura`".* **O PHB rotula `40` das `767` entradas do glossário dele, 5%: é reserva para o nome que confunde, não prática geral.**

**Sete exemplos inline**, no formato medido do D&D — 15 a 24 palavras, dentro da frase, contra a mediana de `23` dele.

### Registrado — a `REGRA-DE-VOZ.md` ganhou o método, e ele diz que não é lei

**Achado do Mizuki, e ele consertou três frases:** *o que os livros de sistema usam são metodologias, não regras — às vezes aplicam, às vezes não, às vezes trocam de forma no mesmo documento.* **As seções estavam redigidas como lei e induziriam erro.**

*Medida a consistência do PHB: ela é **dentro de cada família**, e cada família tem a sua.* `[Área de Efeito]` 100% e abre com definição · `[Risco]` 100% e abre com descrição · `[Condição]` 86% e abre com âncora de tempo · `[Ação]` 55%. **Não existe "a forma do PHB".**

> **A pergunta certa não é "qual é o padrão do livro", é "de que família é esta coisa, e que forma as irmãs dela já usam".**

*E uma frase contradizia a própria ferramenta:* **"estreia de termo tem uma forma só"** *enquanto o `conferir-voz.py` reconhecia quatro.* Virou a tabela das quatro.

### Achado — quatro diagnósticos meus caíram por medir o proxy, e não o fenômeno

**O padrão se repetiu a versão inteira, e fica registrado porque vai se repetir:**

| o que a conta dizia | o que era |
|---|---|
| *"o livro dá 10× menos exemplo que o D&D"* | o regex procurava `Exemplo:` e o livro escreve `**Exemplo.**` — contou `2` onde havia `36` |
| *"o livro quase não exemplifica"* | contava só o marcador `Por exemplo,`; **o D&D exemplifica sem marcador**, e o Mizuki apontou |
| *"22 seções enterram a tabela"* | o livro sinaliza regra de três formas e a conta só via uma — **o número real é zero** |
| *"24 habilidades sem duração"* | quase todas instantâneas ou permanentes; o defeito real era outro |

> **Quando um número sobre este livro parecer alto demais, o primeiro suspeito é o filtro.**

---

## [0.107] — 20/08/2026

**A versão em que as duas divergências que a revisão do livro registrou e ninguém investigou viraram conserto — e as duas moravam onde o bilhete não dizia.** *O `ESTADO-revisao.md` chamou as duas de "bug do sistema, não do livro" e apontou para `03-mecanica/`. Uma delas está lá; a outra estava no gerador do manual.* **Manual do Fundamento na v7.11.**

### Corrigido — o validador da ficha travava o `subir.sh` desde a v0.105

**A v0.105 tirou a coluna de ofício da tabela de Caminhos da peça 8, e o regex do `conferir-ficha.py` continuou esperando seis colunas.** *Ele não casava com nenhuma linha, `peca_cam` saía vazio, e o validador falhava com `nao consegui ler a tabela de Caminhos da peca 8` — que é a mensagem de "o arquivo mudou de forma", não a de "os números divergem".*

**A checagem 3 ficou duas versões sem conferir nada, com o `subir.sh` travado o tempo todo** — que é a forma mais barulhenta desse defeito e ainda assim a mais fácil de ler errado: a falha acusa a peça, e o defeito estava no leitor.

> **E o campo `oficio` dos `CAMINHOS` do `dados.js` saiu junto.** *Ele guardava `Forja` no Bastião, `Arrombamento` na Vanguarda e mais três — a regra que a v0.105 matou —, e **nada no gerador lia ele**: o `ficha.js` toca em `vida1`, `vidaNv` e `peNv`, e os ofícios impressos na ficha vêm do personagem, não do Caminho.* **Cópia morta de uma regra morta, dentro do arquivo que vira personagem em sete mesas.**

*Sete perturbações conferidas em cópia isolada, com a base passando antes de cada uma e o `diff` conferido: vida, PE, perícia fixa e a tabela sumindo do lado da peça; vida, perícia e Caminho a mais do lado do `dados.js`.* **A contagem de checagens não se moveu — continuam seis, e a comparação de ofício era sub-checagem da terceira.**

### Corrigido — a regra de ouro nº 5, e ela não estava em `03-mecanica/`

**A tabela das Regras de ouro do manual publicava a regra 5 sem o piso de Classe:** *"Liberação Máxima custa a rodada inteira, e você só tem as que o nível deu."*

**O mesmo manual escreve o `Classe 3 ou mais` em outros três lugares** — a seção 6 (*"Escritas antes da sessão, Classe 3 ou mais"*), o item ☐6 do checklist de aprovação, e o resumo do Apêndice. *Só a tabela ficou sem ele, e ela é a lista que a própria seção diz que o checklist do mestre segue **"exatamente"**.* **Quem lesse só a tabela aprovaria uma Liberação Máxima de Classe 1.**

> **⚠ O bilhete dizia `03-mecanica/`, e a regra 5 não mora lá.** *Nenhuma peça de mecânica cita ela; a dona é `manual/gerador/partE.js`.* **O registro da pendência anotou o sintoma — "bug do sistema, não do livro" — e chutou a pasta**, e quem retomasse ia procurar num lugar em que a regra nunca esteve. *Sintoma não diz onde consertar; isso já custou catorze versões à pendência do `carregar`, na v0.93.*

**Manual na v7.11.** *Nenhum número se moveu, nenhum feitiço pronto mudou, e a estrutura fica em 366 parágrafos e 90 tabelas — a correção acontece dentro de uma célula que já existia.* **Ela precisa ser regerada antes do commit:** `node make.js` no gerador e o `soffice` para o `.pdf`, senão o `.docx` publicado fica uma frase atrás e nenhum validador acusa.

### Corrigido — a coluna de Passivas da peça 11, errada em duas das três linhas

**A §4 da peça 11 publica, como prova de que a escada de Classe Passiva foi lida do manual e não inventada aqui, as Passivas do manual em cada altura. Duas das três linhas estavam erradas.**

| Classe Passiva | a peça 11 dizia | o manual lista |
|---|---|---|
| **1** | seis | seis — bate |
| **2** | cinco | **sete** — faltavam `Contramedida` e `Peso da Presença` |
| **3** | **`—`, nenhuma** | **três** — `Escama`, `Afinidade` e `Reserva Profunda` |

**A linha da 3 é a que dói: ela afirmava que o manual não tem nenhuma Passiva permanente, e a `Escama` está lá desde a v0.26** — a mesma que este documento discute na seção de playtest, três telas abaixo. *Uma prova que contradiz o que ela cita prova o contrário do que ela quer provar.*

> **A checagem que faltava é a `4k` do `conferir-manual.py`**, sub-checagem da quarta, no molde exato da `4i` e da `4j`: os dois lados são lidos — as três alturas do `.docx` e as três linhas da peça —, e nenhum valor fica escrito dentro do validador. **A contagem de checagens não se moveu.**
>
> *Ela vem com guarda: a `Regra Própria` e a `Passiva Própria` são `1 a 3` e ficam de fora das três linhas dos dois lados.* **Se o manual der altura fixa a uma delas, a guarda acusa antes de a comparação mudar de forma em silêncio** — e o contra-teste rodado prova que a guarda não é trivialmente verdadeira: renomear a `Passiva Própria` no `.docx` acende ela sozinha, com as três linhas ainda batendo.

*Oito perturbações conferidas em cópia isolada — cinco do lado da peça (o traço voltando na linha 3, um nome faltando na 2, a ordem trocada na 1, um nome trocado na 3, e a tabela mudando de forma) e três do lado do `.docx` (a `Escama` virando Classe 2, a `Regra Própria` ganhando altura fixa, e o cabeçalho da tabela mudando).*

### Registrado — dois `Classe Passiva 2` sem relógio, e o diagnóstico estava errado

**O `Fluxo` e o `Peso da Presença` não trazem limite de uso nenhum**, e a linha que os abriga se define como *"efeito reativo, **com limite de uso por cena ou por descanso**"*. *Isto entrou na peça 11 §4 como frouxidão a registrar — e foi escrito sem ler o que as duas fazem.*

> **Elas já têm freio; ele só não é um relógio.** *O `Fluxo` só dispara ao conjurar **Classe 3 ou mais**, que é caro por si; o `Peso da Presença` só pega inimigo **fraco**, uma vez por turno dele, e ainda passa por TR.* **Decisão do Mizuki: o que a Classe Passiva 2 pede é gatilho, e não contador** — uma Passiva de Classe 1 melhorada, presa a uma condição que já custa caro, cabe na linha inteira.

**O que está estreito é a definição escrita na tabela do manual, e não a lista que ela abriga** — e essa continua sendo pergunta para o dono da lista, que é o manual. *A peça 11 §4 passou a registrar isso, em vez do diagnóstico anterior.*

*É a armadilha de sempre, na direção menos esperada:* **antes de aceitar um preço, veja se o termo que ele usa existe — e o mesmo vale para aceitar que um preço FALTA.** *Duas linhas de tabela lidas teriam evitado o registro errado.*

### Fechado — os três documentos do livro que carregavam as duas como pendência

*O `README.md`, o `ESTADO-revisao.md` e o `REMOCOES-material-de-mestre.md` de `05-material/livro/` descreviam as duas como abertas.* **O texto do livro já estava certo nos dois casos** — a revisão da v0.106 tinha consertado as cópias herdadas e registrado que a fonte continuava errada. *Os três itens fecharam com `~~`, que é a convenção da casa.*

### Corrigido — o `conferir-repositorio.py` lia o worktree do Claude Code como se fosse material

**O Claude Code abre worktree em `sistema/05-material/livro/.claude/worktrees/<nome>/`, e um worktree é uma cópia inteira do repositório dentro do repositório.** *As quatro varreduras recursivas do validador pulavam `.git`, `_backup`, `_to_delete`, `node_modules` e `__pycache__` — e não `.claude`.* **Resultado: cada ponteiro morto e cada nome aposentado aparecia duas vezes, uma pelo arquivo real e outra pelo espelho.** Nesta versão foram oito falsos, todos com `.claude/worktrees/` no caminho.

> **O defeito é intermitente, que é o pior jeito de ele existir.** *Ele só acende enquanto um worktree está vivo, e some sozinho quando a sessão fecha — o `subir.sh` desta versão passou numa rodada e falhou na seguinte sem que nada do material tivesse mudado no meio.* **Um validador que responde diferente para a mesma árvore ensina a desconfiar da árvore.**

*Contra-teste rodado em cópia isolada, com a base passando antes: o mesmo defeito plantado fora de `.claude` acende em quatro linhas de erro, e plantado dentro do worktree fica mudo.* **Nenhuma checagem nova — continuam 188 em 20 validadores.**

### Alterado — a entrega ressincronizada

*Quatro cópias tinham ficado para trás: a peça 11, o `arquitetura.md` e o `.docx`/`.pdf` do manual na v7.11.* O `README.md` da entrega — o único arquivo escrito à mão lá — passou a **v0.107** e **v7.11**, e a nota que manda regerar o Fundamento em vez de reaproveitá-lo ganhou a mudança da regra de ouro nº 5 ao lado dos dois feitiços da v0.104. *Sem isso ela listava pela metade o que mudou desde a `v7.9`.*

---

## [0.106] — 19/08/2026

**A versão em que o PDF ganhou o texto que a v0.103 previu.** *`sistema/05-material/livro/` estava vazia desde a v0.35 — agora tem o Manual da Guilda inteiro, 230 páginas, com o quick-start que "como o PDF carrega essa propriedade é trabalho dele" tinha deixado em aberto.*

### Adicionado — `sistema/05-material/livro/`

A fonte do livro (18 arquivos `manual/*.md`), os três scripts que compilam PDF, docx e texto corrido, e os dois documentos de decisão da revisão: `ESTADO-revisao.md` e `REMOCOES-material-de-mestre.md`.

Um glossário de 66 termos e um índice remissivo de 62, os dois gerados no build. Um quick-start jogável — *"Antes da primeira sessão"* — peça de frente entre o vocabulário e o capítulo 1, com a ficha da Kaori (a mesma do capítulo 6, mesmos números) e uma cena de combate guiada com a matemática visível.

### Alterado — organização e redundância do texto de mesa

43 referências cruzadas por nome de capítulo viraram por número; 11 apontavam para capítulo que não existe com aquele nome. Cortadas 19 tabelas nos Caminhos que repetiam o texto logo abaixo, duas cópias divergentes de "Regras de ouro" e da tabela-mestra de números dentro do Fundamento, e a moeda de orçamento (`custa`/`devolve`) que ficou órfã no catálogo de arma depois que o orçamento saiu do livro do jogador.

~2.400 palavras de material de mestre e argumento de design (aprovar feitiço, letalidade, inimigos, orçamento de arma, projeção de gate) saíram do livro do jogador — detalhe completo de cada corte, e onde a funcionalidade precisa voltar a existir, em `REMOCOES-material-de-mestre.md`.

### Decidido — os cinco Caminhos declaram o que concedem, e o treino de arma ganhou regra pela primeira vez

Cada Caminho ganhou um bloco com vida, PE, atributos, perícias, ofícios, TR e treino de arma — nada disso estava reunido num lugar só antes. **Bastião e Vanguarda treinam as treze categorias de arma; Guia, Emanador e Evocador treinam só Arma de Fogo e Balestra**, e o resto vem pela Trilha, como a `Empunhadura` do `Arremate` já fazia.

**A regra existe só no livro por enquanto.** Não tem validador nem peça em `sistema/03-mecanica/` — precisa voltar para cá numa próxima leva.

---

## [0.105] — 18/08/2026

**A versão em que o Caminho parou de travar ofício.** *Cada um dos cinco fixava um ofício desde a v0.22; agora os dois que o Caminho entrega são livres, e o jogador escolhe os dois.*

### Alterado

**O Caminho dá dois ofícios livres, e nenhum fixo.** Até aqui a tabela era `Forja` no Bastião, `Arrombamento` na Vanguarda, `Herbalismo` no Guia, `Caligrafia` no Emanador e `Entalhador` no Evocador.

**O motivo é variedade de ficha, e ele vem de leitura de mesa.** As duas perícias fixas são a assinatura do Caminho: elas dizem o que qualquer um daquele Caminho sabe fazer numa missão. O ofício não faz esse trabalho. O que um personagem faz com as mãos fora da luta é história dele, e travar isso fazia duas fichas do mesmo Caminho nascerem com a mesma coluna preenchida sem que nenhuma das duas tivesse escolhido aquilo.

**Nenhum número se moveu.** A conta de treino continua a mesma: duas perícias fixas, quatro livres, dois ofícios, mais as duas perícias da Origem e o extra dela. Quem gasta o extra da Origem em ofício fica com oito perícias e três ofícios; quem troca fica com nove e dois. As duas rotas continuam na faixa de 30% a 42% do quadro treinado, que é o que o `conferir-pericias.py` mede.

**Cinco peças e um validador.** As peças 4, 5, 6, 7 e 8 diziam "um ofício fixo e um livre" e passaram a dizer "dois ofícios livres"; a tabela de Caminho da peça 7 e a da peça 8 perderam a coluna de ofício. No `conferir-pericias.py`, `CAM_OF_FIXO, CAM_OF_LIVRE` foi de `1, 1` para `0, 2`, e o mapa de ofício por Caminho saiu junto com a checagem que o conferia contra a lista de onze.

---

## [0.104] — 18/08/2026

**A versão das dez condições no degrau errado, e das três contradições numa tabela que ninguém conferia.** *A Melhoria `Condição` virou uma só e o preço dela é o nível; as cinco vagas de `Desliga` que estavam destravadas desde a v0.59 e a v0.103 fecharam; e a penalidade de arma, que três documentos esperavam, está escrita.* **Manual do Fundamento na v7.10.**

### ⚠⚠ O achado de método: uma tabela de ilustração errada em três das doze entradas

**A tabela dos três formatos da peça 13 — a porta de entrada dela, a primeira coisa que a mesa lê sobre o que `Ajusta`, `Desliga` e `Destranca` fazem — estava errada desde a v0.39.**

| | a tabela dizia | o catálogo diz |
|---|---|---|
| `Corpo Emprestado` | `Desliga` | **`Ajusta`** |
| `Treino de Berço` | `Ajusta` | **`Destranca`** |
| `Não Sou Gente` | `Desliga` | **não está lá** — virou Passiva paga com espaço de feitiço |

**As três foram convertidas pela própria v0.39, que escreveu a régua, mexeu nos Legados que ela reprovava, e não voltou nas tabelas que citavam aqueles Legados como EXEMPLO.**

> **Nenhum validador alcançava ela, e o motivo é que ela é ilustração e não regra.** *A checagem 10 do `conferir-legados.py` entrou nesta versão: ela lê os doze nomes da tabela e cobra cada um contra o formato que o catálogo dá a ele.* **Só uma das três tinha sido achada a olho.**

### Decidido — a Melhoria `Condição` é uma só, e o preço dela é o nível

***Decisão do Mizuki, entre duas formas medidas.*** **A `Condição Menor` e a `Condição Maior` saíram; entrou `Condição`, cobrando `Leve`, `Média` ou `Pesada` conforme a condição escolhida.**

| | pior espalhamento dentro de um degrau |
|---|---|
| o manual até a v7.9 | **`17,00×`** — o `Impedido` contra o `Desarmado`, os dois por `Média` |
| a forma alternativa — promover as três subvendidas | `9,11×` |
| **o nível como preço** | **`4,26×`** |

**A alternativa não movia o pior caso: ela ficava nos mesmos `9,11×`.** *Promover `Cego`, `Impedido` e `Envenenado` para `Maior` joga as três dentro de um degrau que já ia do `Petrificado` ao `Incapacitado`.*

> **E `4,26×` é o PISO, não um resultado.** *A busca exaustiva sobre as catorze diz que nenhum outro corte em três degraus faz melhor.* **O filtro do projeto reprova a partir de `3,00×`, então o que sobra de dominância não é escolha — é a tabela do manual ter três degraus e as condições valerem de `0,00` a `100,25` de dano por rodada.**

**Dez das catorze trocaram de degrau:** `Cego`, `Impedido` e `Envenenado` sobem para `Pesada`; `Enfeitiçado` desce para `Média`; `Lento`, `Incapacitado`, `Derrubado`, `Agarrado`, `Desarmado` e `Surdo` descem para `Leve`.

**Dois feitiços prontos mudaram, os dois porque o `Derrubado` barateou:** a `Palma Trovejante` foi de `5d8 = 22` para `6d8 = 27` e a `Vala Comum` de `9d8 = 40` para `11d8 = 49`. *A `Rede` e a `Prisão de Sombras` carregam `Atordoado`, que já era `Pesada`.*

> **O Teste de Resistência no fim de cada turno, e o limite de uma por feitiço, passaram a valer para o nível `Pesada`.** *Antes valiam para as cinco `Maior`, e aquelas cinco não eram as cinco mais duras — o `Incapacitado` estava lá dentro, e ele é a segunda mais barata das catorze.*

### ⚠ E a arrumação achou um erro vivo na tabela de Controle do manual

**A última linha dela é um feitiço de Classe 5 que gasta tudo em Controle e sai com `0d8`, e ela publicava `Lento (+3)`.** *O `Lento` devolve `Média` desde a v7.3, que na Classe 5 são `5` pontos e não `3`* — com o preço certo aquela linha dá `2d8`, e o exemplo do `CD +2` deixava de existir. **Passou a usar `Parado (+3)`, que devolve `Leve` e vale os `3` que a conta pede.**

*É o mesmo defeito que a v7.3 já tinha deixado na tabela de Ampliar: mudança de preço que não voltou nos exemplos que citavam o preço velho.*

### Decidido — o `Surdo` ganhou `−2` na iniciativa, e ele é a regra do d20 de 2003

***Decisão do Mizuki.*** **Ele fica comprável, continua `Leve`, e passa a dar `−2` na iniciativa.**

**A `Deafened` do SRD 3.5 cobra `−4` em iniciativa, falha automática em ouvir, e `20%` de falha ao conjurar com voz.** *O 5e cortou as duas primeiras e ficou só com a terceira, e é dessa versão encolhida que o `Surdo` deste sistema tinha nascido.* **As outras duas linhas do 3.5 não entram aqui: a de ouvir já é a linha que a condição tem, e a de conjuração é o que o `Calado` faz — e ele custa `Média`.**

| na iniciativa | você age antes | perde | em pontos de Destreza |
|---|---|---|---|
| normal | `52,50%` | — | — |
| **`−2`, o daqui** | **`42,75%`** | **`9,75` pp** | **`2,05`** |
| `−4`, o do 3.5 | `34,00%` | `18,50` pp | `3,89` |

> **⚠ E ele continua lendo `0,00` na régua da peça 19, e isso é sobre a régua.** *A peça 15 §3.1 já publicou o contra-teste: "que fração do meu dano da rodada cai antes de o inimigo agir" dá `52,5%` em todas as montagens, porque iniciativa **reordena** o turno e não tira ação de ninguém.* **Ele deixou de não fazer nada na mesa sem deixar de ler zero no papel.**

### Decidido — a trava do `Desliga` foi relaxada, e as cinco vagas fecharam

***Decisão do Mizuki.*** **Um `Desliga` apaga o que ninguém comprou, e ENFRAQUECE o que alguém comprou. Nunca imunidade.**

*A trava anterior dizia só "apaga o que ninguém comprou", e com ela as cinco vagas destravadas não tinham como nascer: toda condição passou a ter preço nesta mesma versão.* **O relaxamento é escrito em cima do que a régua criou** — o nível é número, então ele escolhe o degrau do relógio em vez de barrar a porta:

> **`Leve` → por cena · `Média` → por dia · `Pesada` → por descanso longo.**

**A fronteira com o `Ajusta` não some, e é ela que segura o relaxamento:** um `Desliga` de condição **apaga aquela vez**; um `Ajusta` de condição **põe um dado no meio**. *O `Corpo Emprestado` e o `Já Morri` continuam `Ajusta`, porque vantagem no Teste de Resistência é mexer num número de uma rolagem.*

**As cinco, com os nomes e os pares escolhidos pelo Mizuki:**

| Origem | Legado | apaga | relógio |
|---|---|---|---|
| **Descendente** | `Cabo` | ficar `Desarmado` | por cena |
| **Restrição Celestial** | `Assinado` | ficar `Cego` | por descanso longo |
| **Receptáculo** | `Revezamento` | ficar `Impedido` | por descanso longo |
| **Feto** | `Talhe` | ficar `Agarrado` | por cena |
| **Reencarnado** | `Usado` | ficar `Derrubado` | por cena |

*Os cinco nomes saíram `LIVRE` na triagem, nas duas direções.* **Sobraram duas vagas, e as duas esperam peça que ainda não existe:** `objeto amaldiçoado` e `Técnica Marcial`.

> **A dívida que a peça 13 marcou desde a v0.24 está paga, e o que a segurava não era trabalho.** *Ela dizia "quando equipamento fechar, a primeira coisa a fazer é voltar aqui", e ninguém voltou nem quando a peça 14 fechou na v0.48 nem quando a 19 fechou na v0.103.* **Era outra decisão: a trava proibia encostar em qualquer coisa com preço, e por isso nenhuma das cinco podia nascer.**

### Adicionado — a penalidade de arma, e ela não é preço

**Três documentos apontavam para cá:** a peça 14 §8 item 15, a peça 16 §9, e a própria peça 19.

> **Sem treino na categoria: desvantagem na rolagem de ataque.**
> **Sem o requisito de Força: o deslocamento cai `3 m` enquanto você a empunhar.**

**A do requisito atravessou inteira do d20 de 2024, e nem o número mudou** — lá ela é de proteção: *"reduz o deslocamento de quem a veste em `10` pés, a menos que ele tenha a Força listada"*, e `10` pés são os `3 m` desta peça.

**A do treino precisou de tradução, e o motivo é estrutural:** no d20 usar arma sem treino tira o bônus de proficiência, e aqui a rolagem de ataque é `d20 + Força`, sem esse termo. *Desvantagem vale `54,00` de dano por rodada, que é exatamente o `+5` do d20 — um passo abaixo do `+6`, que é o topo dele.*

> **E as duas somadas custam `33,8` vezes o que a arma inteira entrega.** *`55,80` contra `1,65`.* **Ninguém paga trinta e três vezes para usar uma coisa: é porta fechada, que é o que o d20 faz também.**

### Corrigido — as duas réguas de rolagem divergem `9,4` vezes, e o `4,7` media outra coisa

**A v0.103 publicava, em três documentos, que a diferença entre a sua régua de rolagem e a do aliado era de `4,7` vezes.** *O `4,7` é `108 ÷ 23,00`: a razão entre as duas BASES.* **Isso é verdade e responde outra pergunta — quanto o seu escopo é maior que o do aliado.**

**Lidas por ponto percentual, que é a única forma de compará-las, elas dão `2,16` contra `0,230`, e a razão é `9,39`.**

| | como ela converte |
|---|---|
| a sua | **relativa** — `+1` são `5` pp sobre `50%`, e isso é `+10%` do que sai (peça 15 §3.3) |
| a do aliado | **absoluta** — `X` pp viram `X%` da base |

> **`9,4` = `4,7` de escopo × `2` de conversão.** *Pela conversão relativa, `1` pp num aliado valeria `0,460`.* **E o contra-teste fecha no mesmo número:** lido pela sua régua, o `Ajudar` valeria `54,00` em vez dos `5,75` publicados, e `54 ÷ 5,75` são `9,4`. *O `54,00` já está publicado no `DESENHO-manhas` para vantagem.*

**Continua marcado e não consertado, e agora com o tamanho certo:** mexer nisso repreçaria o `Guiar`, o `Estampido` e o `Ajudar` de uma vez.

### Decidido — a perícia livre da Origem perdeu a aprovação do mestre

***Decisão do Mizuki, entre três saídas.*** **Ela continua livre, e a trava passou a ser: não pode ser uma das seis que o seu Caminho te deu.**

> **E a trava não é nova.** *A peça 7 §6 publica `8 de 23` perícias treinadas por ficha desde a v0.16, e esse total só fecha se as duas da Origem não repetirem as seis do Caminho — com repetição a ficha teria `7 de 23`, que são `30%` e não os `35%` em que o §7 apoia o argumento inteiro de por que são vinte e três perícias.* **O número supunha a regra; agora ela está escrita.**

**Era o último lugar da criação em que um número dependia de julgamento do mestre.**

### ⚠ E o `de dez` sobreviveu sete versões em dois lugares

**O `Alfaiate` entrou com a peça de equipamento e fez onze ofícios.** *A peça 7 §7 foi corrigida na hora; o §6 da mesma peça e a tabela das duas rotas da peça 8 não foram, e as duas continuaram publicando `de dez`.*

> **O `conferir-criacao.py` lia aquelas linhas e conferia SÓ O NUMERADOR.** *O denominador podia envelhecer à vontade.* **É a checagem medindo pelo eixo errado, de novo — verde exatamente onde importava.** *Hoje ela lê os dois, contando o quadro da peça 7 em vez de guardar o total.*

### Adicionado — o atributo padrão de cada ofício

**Os onze ganharam um, e ele não foi escolhido a gosto: cada ofício herda o atributo da perícia que mora mais perto dele.** *`Arrombamento` puxa `Prestidigitação`, `Forja` puxa `Atletismo`, `Instrumento` puxa `Atuação`.*

**Cinco em Destreza, três em Inteligência, duas em Essência, uma em Força — e nenhuma em Constituição.**

> **A cláusula que importa é a última: o mestre troca quando a ficção pedir, e diz qual ANTES da rolagem.** *Sem ela o padrão não resolve nada — trocar depois de ver o dado é a mesma discricionariedade com um passo a mais.*

### Alterado — a curva de refino mudou de casa, e o `conferir-descanso` perdeu uma contagem

**A curva das três rotas saiu do `02-esqueleto/arquitetura.md` §4.3 para a peça 11 §3.** *Ela era a última fonte de progressão do projeto fora de uma peça de regra, e a peça 18 §7 registrava isso com esse nome.* **O validador não a confere contra cópia: reconstrói da regra** — começa em `1`, `+1` de graça por marco, `+1` opcional, teto `10`. *Os gates da seção 5 daquela peça são esta curva lida em três colunas.*

***Decisão do Mizuki: a contagem de `por cena` da peça 10 saiu.*** *Ela nasceu na v0.62 como prova de que a palavra mais usada do projeto não tinha definição, e a definição está escrita, com checagem própria em cima.* **O total, porém, sobe toda vez que qualquer peça ganha uma entrega: acusou na v0.83, na v0.92, na v0.103 e na v0.104, e nenhuma das quatro achou defeito — achou a própria idade.** *Teste escrito contra número que sobe toda semana mente na semana seguinte.*

### Os validadores

**Onze checagens novas ou reescritas em sete validadores, e quarenta e duas perturbações em cópia isolada — trinta e seis que tinham de acender e seis contra-testes que tinham de ficar verdes.** *Todas acenderam, e todos os seis ficaram verdes.* **Sete perturbações atravessam o `.docx`:** perturbar o manual quer dizer mexer no gerador e rodar o `node make.js` de novo, e sem isso a perturbação não chega no validador.

*Onde elas foram registradas:* **as vinte e sete do `conferir-dano.py` estão na tabela do §7 da peça 19**; as quinze restantes — quatro da tabela dos três formatos, quatro do relógio do `Desliga`, sete do quadro de perícias e ofícios — foram rodadas e não têm tabela própria ainda. *Fica anotado: peça com arnês registrado envelhece melhor que peça com arnês rodado.*

| validador | o que ganhou |
|---|---|
| `conferir-dano.py` | a checagem 4 lê as **três tabelas de nível** do manual e cobra nome **e nível** nos dois sentidos; a 11 é a penalidade de arma; a 2 passou a reconstruir a razão entre as duas réguas de rolagem, e a cobrar que ela seja o dobro da razão das bases |
| `conferir-legados.py` | a checagem 10 confere os doze exemplos da tabela dos três formatos contra o catálogo; a 4 cobra que todo `Desliga` de condição carregue o relógio que o nível dela pede — e o nível vem da peça 19 |
| `conferir-nomes.py` | as catorze condições passaram a ser extraídas das três tabelas de nível; a segunda fonte que existia dentro do `.docx` **mudou de casa** e virou a peça 19, conferida pela checagem 4 do `conferir-dano.py` |
| `conferir-criacao.py` | lê o **denominador** do quadro de perícias e ofícios, contado da peça 7; e cobra a trava da perícia livre nos três donos |
| `conferir-pericias.py` | o atributo padrão dos onze ofícios, a distribuição em prosa contra a tabela, e a exigência de o mestre dizer antes da rolagem |
| `conferir-aptidoes.py` | a curva das três rotas, **reconstruída da regra** e não conferida contra cópia |
| `conferir-descanso.py` | perdeu a contagem de `por cena`, com o motivo escrito no lugar dela |

---

## [0.103] — 2026-08-18

**A peça de dano e condições entrou, e ela é a peça 19.** *Vinte e seis lugares em oito documentos esperavam por ela — a maior dívida estrutural do projeto — e metade dela já estava escrita, em três seções da peça 1 declaradas como guarda provisória.* **A régua que ela existia para ter não precisou ser inventada: ela estava na tabela de custo do manual.** Dezenove peças e dezenove validadores.

### ⚠⚠ O achado: o `Punho` nunca estourou

**Aquela Trilha estava publicada em `6,09` de um orçamento de `5,00`, e o estouro de `22%` estava aceito por decisão do Mizuki** — *"mesmo com esse estouro, não vai quebrar o balanceamento da mesa — a maioria das habilidades são situacionais e de RP"*.

**O próprio desenho já marcava o `Derrubado` do nível 11 como *"não reconstrói de lugar nenhum"*, e era a maior peça da Trilha.**

> **Ele reconstrói: o `8,66` publicado é o `Derrubado` PERMANENTE**, a `2,5%` de distância do `8,45` que a Manha `Abalo` publica com as mesmas duas linhas.
>
> **Mas o `Encontrão` não é permanente.** O texto da entrega escreve dois portões, e o preço não lia nenhum dos dois: *"um alvo **que você acertou** faz um **Teste de Resistência de Vigor**"*.

| portão | taxa | de onde |
|---|---|---|
| acertar, com dois ataques no nível 30 | `75%` | é o mesmo gate que o `Engate` já usa na mesma Trilha |
| o alvo falhar o Teste de Resistência | `45%` | peça 1 §6 |
| **juntos** | **`33,8%`** | |

**O degrau vale `0,56` fatia e não `1,71`, e a Trilha fecha em `4,94`.** ***Decisão do Mizuki: corrigir o preço e deixar assim.*** *As `0,06` fatia de folga são ruído — `0,30` de dano por rodada.* **Nenhuma linha de texto de mesa se moveu: o que estava errado era a conta.**

### ⚠ E quatro decisões de estouro citavam o `Punho` como precedente

*As três rotas do `Batedor`, a `Brasa`, a `Torrente` e o `Explosivo`.* **Nenhum número delas se moveu — o que se moveu foi qual precedente elas citam.**

**O maior estouro aceito do projeto passa a ser a `Brasa`, entre `41%` e `88%`**, e ela foi aceita com a frase dele: *"parece que é forte, mas não é, garanto"*. *As quatro citações foram marcadas como superadas em vez de apagadas, que é a convenção da casa desde a v0.88.*

> **A lição, e ela é de método:** *um número marcado como "não reconstrói" é dívida, e não curiosidade.* **Ele passou da v0.74 até aqui declarado como órfão, e o que ele era não era mistério: era o preço lendo a entrega errada.**

### Adicionado — a régua de condição, e ela sai do manual

**Até a v0.102 três documentos escreviam que *"condição não tem conversão em fatia"*, e escreviam com razão: ninguém tinha feito a conta.**

**O manual preça condição em dano desde sempre.** *Uma `Condição Menor` custa `Média`, uma `Maior` custa `Pesada`, e cada ponto que não vira Melhoria vira `1d8` — que são `4,5`.*

> **Contra a coluna Rotina, as razões são planas: `Média` é `2/7` e `Pesada` é `3/7`, exatas nas Classes pares.** *Nas ímpares o arredondamento do manual oscila no máximo `1,4` ponto percentual.* **Isso dá as três bandas — `1/7`, `2/7` e `3/7` da Rotina —, e elas são o teto de cada tier.**

**É o quarto exemplar do mesmo defeito em vinte versões:** o Classe 0 da v0.80, a ação `Mirar` da v0.86, a `Aptidão Própria` da v0.92, e esta. *O projeto procurando régua que o manual já publicava.*

### As catorze, medidas — e o tier do manual é um preço só para coisas que valem `17` vezes uma da outra

*Contra um chefe, no nível 30. Todo componente sai de documento dono, e o `conferir-dano.py` lê de lá em vez de guardar cópia.*

| condição | tier do manual | dano por rodada | fatias | nível |
|---|---|---|---|---|
| `Petrificado` | Maior | `100,25` | `19,73` | `Pesada` |
| `Impedido` | Menor | `58,65` | `11,55` | `Pesada` |
| `Cego` | Menor | `53,25` | `10,48` | `Pesada` |
| `Amedrontado` | Maior | `41,40` | `8,15` | `Pesada` |
| `Envenenado` | Menor | `36,00` | `7,09` | `Pesada` |
| `Atordoado` | Maior | `36,00` | `7,09` | `Pesada` |
| `Calado` | Menor | `24,00` | `4,72` | `Média` |
| `Enfeitiçado` | Maior | `24,00` | `4,72` | `Média` |
| `Lento` | Menor | `14,70` | `2,89` | `Leve` |
| `Incapacitado` | Maior | `11,00` | `2,17` | `Leve` |
| `Derrubado` | Menor | `8,45` | `1,66` | `Leve` |
| `Agarrado` | Menor | `5,40` | `1,06` | `Leve` |
| `Desarmado` | Menor | `3,45` | `0,68` | `Leve` |
| `Surdo` | Menor | `0,00` | `0,00` | `Leve` |

**Dentro do tier `Menor` o espalhamento é `17` vezes, e o filtro de dominância do projeto reprova a partir de `3,00`.**

**Quatro coisas que a conta achou, e nenhuma foi procurada:**

- **O `Surdo` vale zero.** *Ele só faz falhar teste que precise de audição, e não existe teste desses em combate neste sistema.* **Uma condição com preço de `Média` e entrega nenhuma.**
- **O `Incapacitado` é a segunda mais barata das catorze, e o manual cobra `Pesada`.** *Metade dele depende do `Bloquear`, que é regra opcional — e a peça 1 já registrava isso. O que faltava era o tamanho.*
- **O `Impedido` engole o `Cego`.** *Ele tem as duas linhas do `Cego` mais deslocamento zero, e os dois custam `Média`.*
- **Três passam do teto da `Pesada`**, e o manual já diz o que fazer com isso: a regra da Restrição escrita à mão, virada do avesso — *"se ela parece valer mais que uma Média, ela provavelmente são duas disfarçadas de uma"*. **Condição que passa do teto é mais de uma condição escrita como uma**, e o `Petrificado` diz isso no próprio texto.

### Decidido — o nível de uma condição é o tier dela

***Decisão do Mizuki:*** *"nível é entre ser condição leve, média e pesada, aí o custo de PE fica equivalente a isso"*.

> **Tirar uma condição custa `1` ponto de energia por nível: `1` para `Leve`, `2` para `Média`, `3` para `Pesada`.**

**E isso fecha um buraco que estava vivo embaixo de uma entrega publicada.** *O `Enxerto` do `Sutura` cobra "`1` PE por nível da condição" desde a v0.84, e diz que condição sem nível declarado conta como nível `1`.* **Nível nenhum existia: até aqui, tirar `Petrificado` custava o mesmo que tirar `Surdo`.**

**A escada de quem cura cai da própria regra:** com o teto por uso sendo a maestria, o `Enxerto` alcança `Leve` e `Média` no nível 11 e `Pesada` a partir do 17; o `Cerzido` sobe o teto para a maior Classe e alcança tudo.

> **E ela bate degrau por degrau com a escada de exaustão da peça 10.** *Aquela tem três degraus numerados, e tirar o terceiro custa `3` de energia — então ela só sai a partir da maestria `3`, que é o nível 17.* **Duas escadas construídas separadas caindo em `1 · 2 · 3` com a mesma virada no mesmo nível.**

### Alterado — três seções mudaram de casa, e um validador parou de ler o manual

| o que saiu da peça 1 | escrita em | foi para |
|---|---|---|
| §8.1 os catorze tipos de dano | v0.74 | peça 19 §4 |
| §8.2 a cobertura | v0.94 | peça 19 §5 |
| §8.3 as catorze condições | v0.95 | peça 19 §3 |

**As três eram guarda provisória, e a guarda acabou quando a peça existiu.** *Na peça 1 elas viraram ponteiro, com a data e o destino.*

> **⚠ E as checagens foram junto, o que trocou um nome na lista dos que precisam de `python-docx`.** *Os tipos de dano e as condições eram as duas últimas checagens do `conferir-atributos.py`, e a das condições era a única coisa que abria o `.docx` ali.* **Ele deixou de ler o manual, foi de onze para dez checagens, e o `conferir-dano.py` entrou no lugar dele.**
>
> **Continuam CINCO, e a contagem não se moveu — a lista se moveu.** *É exatamente o tipo de troca que passa despercebida quando o número está certo, e ela foi aplicada nos três documentos que publicam a tabela.*

### Adicionado — o `conferir-dano.py`, com dez checagens

*A especificação foi escrita antes do código, na §6 da peça, que é o método que fez a peça 15 caber numa versão só contra as seis que a peça 14 gastou.*

**A checagem que a peça existe para ter é a nona, e ela sai da pasta:** ela lê os dois `DESENHO` da raiz e bate as duas entregas publicadas que aplicam condição — o `Abalo` e o `Encontrão` — contra a régua, **com o portão que o texto de cada uma escreve**. *É ela que pegaria o `Punho` de novo se alguém reescrevesse a entrega sem mexer no preço, ou o contrário.*

**E a décima guarda a promessa do cabeçalho:** nenhum valor de regra fica escrito dentro do validador, e as três bandas são derivadas de `1/7`, `2/7` e `3/7` da Rotina em vez de constantes.

### As treze perturbações, em cópia isolada

*Base conferida verde antes de cada uma, `md5` comparado antes e depois, e o veredito lido da checagem testada — nunca o código de retorno do programa.* **Onze acendem, dois contra-testes saem verdes.**

> **⚠⚠ E o arnês achou TRÊS defeitos no validador antes de ele valer, e um deles é a lição nº 8 pela quarta vez.**
>
> **A checagem 4 comparava o manual contra a lista escrita DENTRO do validador** e não contra a peça — renomear uma condição na peça saía **verde**. *Hoje ela lê os nomes das tabelas de mesa.*
>
> **A checagem 6 procurava uma frase OU outra na peça 10**, e meia porta é porta aberta. *Hoje ela exige as duas.*
>
> **E duas perturbações estavam mal miradas**, trocando uma ocorrência de uma âncora que aparece duas vezes no mesmo arquivo. **O arnês ganhou um modo que troca todas** — é o mesmo defeito que a v0.101 registrou com um `sed` que parou de bater, por outra porta.

### Decidido — três perguntas saíram da fila

| pergunta | decisão do Mizuki |
|---|---|
| **quem é a próxima peça** | **as três Trilhas do Evocador** — `Servo`, `Matilha` e `Coro`. *O projeto tinha duas respostas escritas: a fila do `ESTADO-ATUAL` dizia Trilhas e a peça 16 dizia Técnica Marcial. A peça 16 foi corrigida.* |
| **se o PDF nasce jogável nas primeiras páginas** | *"vamos finalizando as informações e mandando pro outro repositório o necessário para fazer o PDF, eu já tô no processo de estudo sobre"*. **Como o PDF carrega essa propriedade é trabalho dele, e não pendência do repositório.** *Aplicado no dossiê de metodologia e no `ESTADO-ATUAL`.* |
| **a terceira taxa do `Batedor`** | **sai da fila de perguntas.** *As três taxas ficam declaradas onde moram, com o tamanho escrito. Quem responde é a mesa.* |

### Em aberto

- **⚠⚠ O manual cobra `Média` por dez condições que a conta preça em outro tier, e seis delas ele subvende.** *`Cego`, `Impedido` e `Envenenado` valem `Pesada` e custam `Média`.* **Consertar é mexer na tabela de Melhoria do manual e regerar o `.docx`, e é decisão dele.** *Enquanto não for, o `Impedido` é a melhor compra da tabela de Controle.*
- **A `Cicatriz` continua sem mecânica**, e a pergunta de se a `Energia Reversa` limpa Sequela continua sem dono. *As duas ficaram fora do escopo que ele fechou para esta versão.*
- **A penalidade por empunhar arma sem treino ou sem requisito.** *A peça 14 e a peça 16 apontam para a peça 19, que agora existe, e o item continua aberto lá dentro.*
- **Cinco das sete vagas de `Desliga` da peça 13 estão destravadas e nenhuma foi escrita.** *Três destravaram nesta versão, duas na v0.59.* **Preencher é trabalho, e não conserto de texto.**

> **⚠ E a checagem 6 do `conferir-legados.py` só aceitava UMA resposta, e por isso ela obrigava a vaga a mentir.** *Ela exigia que toda vaga reservada dissesse "espera a peça de X" — então, quando a peça nascia, a vaga continuava dizendo que esperava.* **Agora ela aceita as duas respostas que existem — esperando uma peça, ou destravada e por escrever —, e exige que a segunda nomeie a peça que destravou.** *Ao ganhar o segundo caminho, ela achou na hora as duas vagas que a peça 16 destravou na v0.59 e que estavam há quarenta e quatro versões escritas como esperando.*
- **A conta usa duas réguas de rolagem que não medem a mesma coisa.** *`+1` no seu acerto vale `10,80`, que são `10%` da Rotina de `108`; `1` ponto percentual na rolagem de um aliado vale `0,230`, que é `1%` da ação de atacar de `23,00`.* **Você é modelado pela Rotina inteira e o aliado por dois golpes simples**, e a diferença é de `4,7` vezes. *Mexer nisso repreçaria o `Guiar`, o `Estampido` e o `Ajudar` de uma vez.*
- O resto da lista da v0.102 continua igual.

---

## [0.102] — 2026-08-18

**O quick-start foi abandonado, e o número de checagens de cada validador ganhou dono.** *Duas coisas da mesma família: uma decisão que precisava ser aplicada em oito lugares, e um número que morava em três documentos e no código, com o código sendo o único que não podia mentir.* **Nasceu a checagem 9.** Continuam dezoito peças e dezoito validadores.

### Decidido — o quick-start jogável sai, e o texto de mesa vai direto para o PDF

***Decisão do Mizuki:*** *"pode abandonar a ideia do quick start, eu tô fazendo o PDF direto"*.

**Ele estava decidido na v0.2 como a estrutura do material final, e ficou cem versões escrito como pendência.** *Aplicado em oito lugares: o `README` em dois, o `LEIA-ME` em dois, o `ESTADO-ATUAL` em dois, a peça 14 e a peça 18.*

> **⚠ E uma pergunta ficou aberta junto com a decisão, porque ela não é a mesma coisa.** *O dossiê de metodologia lista, como trava de arquitetura, que o material nasce com quick-start na frente — e o argumento de lá **não é sobre ter dois arquivos**: é sobre alguém conseguir jogar antes de ler tudo.* **Abandonar o formato não responde se o PDF vai carregar essa propriedade.** *Marcado no dossiê, sem reescrever o levantamento: pesquisa é levantamento, não decisão.*

### ⚠⚠ E o `LEIA-ME` tinha a TERCEIRA cópia da contagem do `python-docx`

**A v0.100 corrigiu de três para cinco no `README` e no `ESTADO-ATUAL`, e não achou a terceira cópia.** *Ela estava no `LEIA-ME`, com os mesmos "3 de 5 · 4 de 4 · 1 de 8" e a mesma lista de três nomes.*

> **É a lição nº 9 mordendo o conserto da lição nº 9.** *Achar duas cópias e consertar as duas não prova que eram duas.* **Corrigida, e agora com os cinco e a nota de que ela ficou parada duas versões a mais.**

### Adicionado — a checagem 9, e ela inverte quem é o dono

**Em toda checagem deste projeto o dono do número é um documento e o código é quem confere. Nesta o dono é o CÓDIGO.**

**A definição, e ela precisa ser exata porque a checagem se mede contra ela:** *uma checagem é **um bloco numerado** que o validador imprime.* **Sub-bloco conta para o bloco pai, e o bloco `0` conta** — o `conferir-atributos.py` é o único que tem um.

| o que ela confere | como |
|---|---|
| todo documento que publica "o `conferir-X.py` tem N checagens" bate com o código | conta os blocos numerados, e resolve a quem a frase se refere por três caminhos: o nome do validador na linha, `checagens da peça N`, ou a peça em que a linha mora |
| **nenhum validador tem zero bloco numerado** | zero quer dizer extrator quebrado, e não validador vazio |
| **a numeração não tem buraco** | buraco quer dizer checagem removida sem renumerar, e aí a contagem mente estando "certa" |
| **os documentos continuam escrevendo a contagem** | piso de dez afirmações: se a forma mudar, ela falha em vez de conferir menos em silêncio |

**São 19 validadores e 177 checagens no total**, e 17 afirmações espalhadas por quatro documentos.

> **Linha riscada NÃO é pulada, e isso é decisão.** *O `~~` fecha a pendência, e não a frase ao lado dela* — **e foi exatamente numa linha riscada que a v0.100 achou o `conferir-equipamento.py` publicado como dez tendo onze.** *Linha de história (`>`) é pulada, e essa é a convenção declarada na v0.81.*

### Corrigido — duas contagens que a v0.100 tinha achado na mão

| onde | dizia | é |
|---|---|---|
| `LEIA-ME` | o `conferir-catalogo.py` com **dez** checagens | **onze** |
| peça 17 | *"Nove checagens"* | **onze** |

*O `ESTADO-ATUAL` dizia as duas coisas — "dez" num lugar e "nove" em outro — e a v0.100 já tinha corrigido para onze nos dois.* **Três documentos, três respostas, para um número que o código sempre soube.**

### As oito perturbações, em cópia isolada

| perturbação | esperado | deu |
|---|---|---|
| a contagem publicada erra num documento | acende | acende |
| **a contagem erra numa linha RISCADA** | acende | acende |
| uma checagem sai do validador e deixa buraco na numeração | acende | acende |
| o extrator perde um validador inteiro | acende | acende |
| os documentos param de escrever a contagem | acende | acende |
| **contra-teste:** número errado numa linha de história (`>`) | verde | verde |
| **contra-teste:** afirmar checagem **nova**, que é incremento | verde | verde |
| **contra-teste:** mexer na prosa sem mexer no número | verde | verde |

*O arnês lê o veredito da checagem 9 e não o código de retorno do programa, que é a lição da v0.101.*

### Em aberto

- **A pergunta que sobrou do quick-start:** se o PDF vai carregar a propriedade de "jogável antes de ler tudo", e como. *É decisão dele, e não foi tomada.*
- **A checagem 9 não alcança a docstring do `conferir-repositorio.py`**, que também publica a contagem das próprias checagens. *Ela lê documento, e aquele arquivo é código.*
- O resto da lista da v0.101 continua igual.

---

## [0.101] — 2026-08-18

**Três lugares diziam verde escondendo que não conferiram, e os três foram consertados.** *O `subir.sh` jogava a saída do validador no `/dev/null` e imprimia só `FALHA`; o `conferir-nomes` e o `conferir-pericias` imprimiam `TUDO OK` sem terem aberto o manual uma vez.* **Continuam dezoito peças e dezoito validadores.**

### ⚠ O que provocou: a v0.100 não commitou, e o motivo era uma linha

**O `subir.sh` reprovou, disse `FALHA conferir-repositorio.py`, e parou aí.** *A causa era uma linha só: o prompt de retomada que a v0.99 escreveu citava, entre crases, um caminho que só existe dentro do container do assistente.* **A checagem 2 leu aquilo como referência de arquivo, foi procurar e não achou.**

**O aviso do script mandava rodar o validador sozinho para ver o erro.** *Ele estava certo, e mesmo assim a sessão terminou sem commit — porque o motivo estava a um comando de distância e ninguém deu o comando.*

> **A regra que sai disso: um script que reprova tem de dizer por quê na mesma tela.** *"Rode de novo com mais verbosidade" é a mesma coisa que não dizer.*

### Alterado — o `subir.sh` guarda a saída, e usa ela dos dois lados

**No vermelho, ele imprime as linhas de erro do validador direto na tela.** *As que começam com `!!`, o bloco `>>> N PROBLEMA(S)` e os itens dele.*

**No verde, ele lê a mesma saída atrás de `PULADA`** — e um validador que pulou checagem sai como **`ok*` em amarelo**, com o motivo do lado.

**Pular NÃO trava o commit, e isso é de propósito.** *Biblioteca que falta não é regra quebrada.* **Mas o aviso é amarelo e aparece em toda rodada**, e a linha do `pip install` só aparece quando a pulada foi por causa do `.docx` — ele não chuta a causa.

### ⚠⚠ E a primeira versão disso mostrava o motivo ERRADO

**Um validador que morre de exceção não imprime `!!` nem `>>>`.** *O filtro não casava com nada, e o script mostrava, como motivo da falha, um `>>> TUDO OK` que tinha sobrado de um bloco anterior da mesma saída.*

**É o defeito que esta versão inteira existe para consertar, cometido dentro do conserto.** *Hoje, quando existe `Traceback` na saída — ou quando o filtro volta vazio —, ele mostra o fim da saída, e a linha de sucesso é removida em qualquer caso.*

### Corrigido — os dois rodapés que mentiam, abertos desde a v0.97

| validador | dizia sem `python-docx` | diz agora |
|---|---|---|
| `conferir-nomes` | `TUDO OK` | `OK, mas 3 checagem(ns) PULARAM`, com as três nomeadas |
| `conferir-pericias` | `TUDO OK` | `OK, mas 1 checagem(ns) PULARAM` |

**Quem registra a pulada é cada checagem, no ponto em que ela desiste** — não o `except` do import. *Então a contagem do rodapé é **derivada**, e nenhum número fica escrito dentro do validador.* **É a diferença entre contar sintoma e contar causa, que a v0.38 pagou para aprender.**

> **E o `conferir-pericias` tinha um caminho mudo que ninguém tinha visto.** *A checagem 7 dele é um `if texto_manual:` sem `else`* — sem a biblioteca ela não imprimia nem `PULADA`, ela simplesmente não acontecia. **Agora ela tem o outro lado.**

**Com isso os CINCO que leem o `.docx` avisam quando pulam**, e a tabela do `README` e do `ESTADO-ATUAL` foi atualizada nos dois.

### As perturbações, em cópia isolada

*Com a base conferida verde antes de cada uma.*

| perturbação | esperado | deu |
|---|---|---|
| bloquear o `python-docx` | **5** validadores em `ok*`, zero falha | 5 e zero |
| um número divergente no `README` | falha, **com a linha do erro na tela** | falha, com a linha |
| **exceção não tratada num validador** | falha, **com o `Traceback` na tela** | falha, com o traceback |
| **contra-teste:** mexer em prosa fora do recorte | verde | verde |

> **⚠ E o arnês errou DUAS vezes antes de valer, as duas do jeito que a skill avisa.** *A primeira: o contra-teste mexia numa peça, e mexer numa peça deixa a cópia dela na entrega velha — o que acende a checagem 7. Não era o `subir.sh` errado; era o contra-teste escolhendo um arquivo que o recorte carrega.* **A segunda: depois de a versão subir para `0.101`, o `sed` da perturbação de número continuou procurando `v0.100` e não bateu — e um `sed` que não bate produz um "não acendeu" que parece prova.** *Hoje o arnês compara o md5 antes e depois e recusa a perturbação que não mudou o arquivo.*

> **Três montagens de arnês erradas em duas versões, e nenhuma delas era do código sendo testado.** *A conclusão é a mesma das três: **conferir que a perturbação rodou é parte da perturbação**, e não formalidade.*

### ⚠⚠ E o parágrafo do mount estava dando a saída errada desde a v0.28

**Dois arquivos da raiz viraram fantasma ao serem gravados nesta versão** — `ls` e `stat` com tamanho e inode certos, e `open()` devolvendo ENOENT enquanto os vizinhos da mesma pasta abriam.

**O `README` dizia, desde a v0.28, que *"qualquer escrita nova reconcilia o mount, e uma edição de uma linha basta"*.** *Medido hoje: a escrita nova também sai ENOENT.* **O `cat > arquivo` falha, o `cp` falha, e o arquivo continua fantasma.**

> **O que reconcilia é escrever com OUTRO NOME e depois `mv` por cima.** *O `mv` não precisa abrir o destino.* **Conferido por md5 nos dois lados, nos dois arquivos.**

**É um aviso que dava o motivo errado por setenta e três versões**, e o projeto tem uma regra escrita para isso: *um procedimento com motivo errado envelhece pior que um sem motivo nenhum.* **Corrigido no `README` e na skill.**

### Em aberto

- **A contagem de checagens de cada validador continua sendo número de dois donos, e ninguém confere.** *A v0.100 achou duas erradas de passagem.*
- **Por que o fantasma pega uns arquivos e não outros continua sem explicação.** *Na mesma leva, 23 arquivos foram gravados sem um fantasma e depois 2 de 11 viraram — os dois na raiz, e outros dois da raiz na mesma chamada passaram.*
- O resto da lista da v0.100 continua igual.

---

## [0.100] — 2026-08-18

**As listas "Em aberto" das dezoito peças estavam mentindo, e o tamanho da mentira era onze itens.** *Setenta e duas linhas vivas, e onze delas pediam coisa que já existe — duas dentro da própria peça que já publicava a resposta.* **Nasceu a checagem 8, a primeira que lê seção de pendência.** Continuam dezoito peças e dezoito validadores.

> **O número da versão: `0.100` e não `1.00`.** ***Decisão do Mizuki.*** *`1.0` costuma querer dizer pronto para usar, e `04-playtest/` tem zero sessões, o quick-start não existe e faltam três Trilhas.* **O `1.0` fica reservado para quando alguém tiver jogado.**

### ⚠⚠ O achado: duas peças se contradiziam sozinhas

**A peça 11 §9 pedia as quatro anti-domínio, e a §6.5 dela publica as quatro desde a v0.29** — com Classe, gate, degrau por rota e custo de uso. *A abertura da §6 daquela mesma peça já dizia, com todas as letras, que elas saíram na v0.29.*

**E a peça 13 §10 pedia três consertos na peça 9 que a v0.39 aplicou, e dizia que o `Instinto Bruto` estava metade morto — enquanto a §9 dela mesma publica ele consertado.** *Duas seções do mesmo arquivo, com respostas opostas.*

> **Isso muda o diagnóstico.** *A leitura fácil é "lista velha aponta para fora e envelhece devagar".* **Não é isso: uma delas apontava para dentro, e a peça continha as duas metades da contradição.** *Nenhum validador lia essas seções, então elas não envelheciam — elas paravam.*

### Riscado — onze itens que já tinham fechado

| peça | o item pedia | fechou em |
|---|---|---|
| 5 | quantas Trilhas por Caminho, e em que níveis | v0.55 · v0.60 · v0.65 |
| 5 | a tabela de armas | v0.48 — a peça 14, com as 52 |
| 5 | quanto custa a ferramenta que canaliza sozinha | v0.59 — a peça 16 |
| 8 | a tabela de proteção | v0.48 — a peça 14 |
| 8 | quantas Trilhas um personagem acumula | v0.55 · v0.60 · v0.65 |
| 11 | as quatro anti-domínio, travadas até o manual v7.7 | v0.29, e o manual está na v7.9 |
| 11 | o número da `Barreira Simples` e da `Cortina`, e a régua da `Aptidão Própria` | v0.91 e v0.92 |
| 13 | o validador dos Legados | v0.39 — na mesma versão da peça |
| 13 | o `Instinto Bruto` metade morto | v0.39 — na mesma versão |
| 13 | os três consertos que a peça 9 devia | v0.39 |
| 14 | o validador de Equipamento | v0.48 — onze blocos |

**E cinco lugares fora das peças.** *A fila do `ESTADO-ATUAL` mandava escrever a **Ferramenta amaldiçoada**, que é a peça 16 desde a v0.59, e dizia que faltava o validador dela, que tem dezesseis checagens. A fila mais velha do mesmo arquivo ainda tinha **Invocações** por escrever, e ela é a peça 15 desde a v0.58. A tabela "o que falta para uma ficha de nível 2" ainda listava **aptidões e degraus de refino**, fechados na v0.27 — riscados numa tabela e vivos em outra, no mesmo arquivo.*

> **⚠ E a tabela de progressão consolidada continuava listada como coisa que não existe, no `ESTADO-ATUAL` e no `README`** — uma versão inteira depois de ela virar a peça 18. **O `README` da ENTREGA já estava certo:** ele diz *"existe desde a v0.99: é a `regra/18`"*. *O artefato estava em dia e a fonte não, que é o contrário do que a v0.98 achou.*

### ⚠ Consertado — a contagem do `python-docx` estava errada em dois documentos

**São CINCO validadores que leem o `.docx`, e o `README` e o `ESTADO-ATUAL` diziam três.** *Lido do código e conferido bloqueando o import:*

| validador | pula | de quantas | o rodapé avisa? |
|---|---|---|---|
| `conferir-atributos` | 1 | 11 | sim |
| `conferir-manual` | **4 — todas** | 4 | avisa, e sai antes do rodapé |
| `conferir-nomes` | 3 | 5 | **NÃO — diz `TUDO OK` cego** |
| `conferir-pericias` | 1 | 8 | **NÃO — diz `TUDO OK` cego** |
| `conferir-progressao` | 1 | 8 | sim |

**Eram três até a v0.96.** *O `conferir-atributos` entrou na v0.97 e o `conferir-progressao` na v0.99, e ninguém subiu a contagem nos dois lugares que a publicam.*

> **E o `README` dizia duas coisas diferentes com nove linhas de distância:** *o comentário do `pip install` dizia **dois** e o parágrafo abaixo dizia **três**.* **A lição nº 9 acontecendo dentro do arquivo que a publica.**

### Corrigido — quatro pendências que continuam abertas com o motivo errado

*Elas não mentiam sobre estar abertas. Mentiam sobre por quê, e motivo errado manda procurar o defeito onde ele não está mais.*

| onde | dizia | é |
|---|---|---|
| peça 1, a lista do zero de vida | *"a `Energia Reversa` não foi escrita"* | escrita na v0.78, na peça 11 §6 |
| peça 9 | *"os degraus de refino também não foram escritos"* | escritos na v0.27, na peça 11 |
| peça 9 | Técnica Marcial e Estilo da Sombra são *"a próxima peça"* | cinco peças entraram depois disso |
| peça 15 | *"a corrente ferramenta → Técnica Marcial é a peça seguinte"* | a ferramenta saiu na v0.59; sobra a Técnica Marcial |

**E o `.pdf` do manual estava escrito como v7.8 no `LEIA-ME`**, quatro versões depois de ele passar a sair junto do `.docx`. *A checagem 4 não alcança essa cópia — ela confere a versão do manual e não a do arquivo exportado.*

### Adicionado — a checagem 8 do `conferir-repositorio.py`, com quatro sub-regras

**A regra, em uma frase: um item de pendência não pode ter como assunto — nem esperar, nem pedir validador de — coisa que já existe na pasta.**

| # | o que ela pega | como |
|---|---|---|
| **8a** | o item pede validador que já existe | o dono da peça é **derivado** do nome do arquivo, sem tabela escrita no código |
| **8b** | o item está travado por versão do manual que já passou | lê a versão do dono, o `COMO-USAR.txt` do gerador |
| **8c** | o **assunto** do item é uma peça que já existe | compara o sujeito do item com o slug de cada `NN-*.md` |
| **8d** | o item **espera** uma peça que já existe | pega o que vem depois de *"espera"* |

**O sujeito muda de forma com a forma da linha, e isso é a metade que decide:** *num item de lista é o primeiro negrito, numa tabela é a primeira célula com texto, e em prosa é a frase inteira.* **Ler a linha inteira como sujeito produz falso positivo em toda linha que cita uma peça de passagem.**

**Três exclusões, cada uma com motivo escrito:** *linha com `~~` está fechada e é a convenção da casa; **o corpo de um item riscado morre com ele**, senão a tabela de especificação de um item fechado continua acusando; e linha começando com `>` é história, que a v0.81 declarou.*

> **⚠ E o filtro de "fechado" quase apagou um item vivo.** *A primeira versão pulava qualquer linha que contivesse `fechou`, e o item das sete vagas de Desliga termina em "nenhuma delas abriu quando aquela peça **fechou**".* **O item sumia da checagem inteiro, em silêncio.** *Hoje o filtro só vale em linha de tabela, onde a célula de estado é que declara — em item de lista quem fecha é o `~~`.*

### As nove perturbações, em cópia isolada

*Com a base conferida verde na cópia antes de cada uma, e o `diff` conferido antes de ler o resultado.*

| perturbação | esperado | deu |
|---|---|---|
| o item volta a pedir o validador dos Legados | acende | acende |
| o item volta a travar no manual v7.7 | acende | acende |
| o item volta a dizer que a tabela de proteção não existe | acende | acende |
| a vaga volta a esperar a `ferramenta amaldiçoada` | acende | acende |
| **pendência NOVA citando peça que existe só fora dela** | acende | acende |
| uma peça perde a seção de pendência | acende | acende |
| o extrator perde o cabeçalho | acende | acende |
| **contra-teste:** reescrever a prosa de um item vivo sem nomear peça | verde | verde |
| **contra-teste:** item riscado com tabela de corpo | verde | verde |

> **⚠⚠ E o arnês mentiu na primeira rodada, do jeito que a lição nº 8 avisa.** *Ele lia o código de retorno do script inteiro — e perturbar uma peça também deixa a cópia dela na entrega velha, o que acende a **checagem 7**.* **Duas perturbações da checagem 8 saíam "acende" sem a checagem 8 ter acusado nada.** *Corrigido lendo o veredito da checagem 8 e não o do script; com o veredito certo, duas das quatro sub-regras não acendiam — uma por perturbação mal montada, e a outra pelo filtro de "fechado" acima.*

### Em aberto

- **Duas vagas de `Desliga` destravaram na v0.59 e ninguém voltou.** *Elas esperavam `ferramenta amaldiçoada` — a `Armaria` do Descendente e a Restrição Celestial — e a peça 16 §9 registra que destrava as duas.* **Escrever as duas é trabalho, não conserto de texto**, e a linha de cada uma na peça 13 continua dizendo `espera a peça de ferramenta amaldiçoada`.
- **Quem é a próxima peça está escrito de dois jeitos.** *A fila do `ESTADO-ATUAL` diz `Trilhas`; a peça 16 §9 diz que a `Técnica Marcial` é a peça seguinte.* **As duas leituras cabem, e o projeto não pode ter duas respostas.**
- **Dois dos cinco validadores que leem o `.docx` continuam dizendo `TUDO OK` estando cegos** — o `conferir-nomes` e o `conferir-pericias`. *Item aberto desde a v0.97, e agora com o tamanho medido.*
- **A checagem 8 não alcança a peça 2**, que continua sendo a única peça de regra sem validador dono.
- **A contagem de checagens de cada validador é número de dois donos e ninguém confere.** *Esta versão achou duas erradas — o `conferir-equipamento` publicado como dez sendo onze, e o `conferir-catalogo` publicado como dez num lugar e nove em outro, sendo onze.*
- O resto da lista da v0.99 continua igual.

---

## [0.99] — 2026-08-18

**A tabela de progressão virou a peça 18, e ela não estava espalhada por cinco documentos: eram dez números em seis lugares.** *E um dos dez não tinha dono nenhum.* **Dezoito peças e dezoito validadores.**

### ⚠⚠ O achado: o tamanho da lista de feitiços não era de ninguém

**A fórmula dos espaços de feitiço conhecido — `2 + nível ÷ 2`, mais um por marco — estava escrita à mão dentro de DOIS validadores e em nenhum documento.** *Mesma linha no `conferir-aptidoes.py` e no `conferir-expansao.py`.* **É a regra que este projeto repete desde a v0.14: nada de valor fica escrito dentro do validador.**

**E dá para dizer exatamente quando ela ficou órfã.** *O manual carregava a contagem até a v7.6 e a devolveu na v7.7, com o motivo escrito: ela discordava do sistema em volta em três feitiços no nível 20 e seis no 30.* **O texto de lá hoje diz, com todas as letras:** *"Quantos feitiços você conhece não é conta deste manual. O tamanho da lista vem do sistema em volta."*

> **É o inverso exato do defeito que o projeto viu três vezes.** *Nas v0.80, v0.86 e v0.92 o projeto foi inventar régua que o manual já publicava.* **Aqui o manual passou um número adiante e não tinha ninguém do outro lado.** *A peça 18 pega, e os dois validadores passam a ler a coluna dela.*

### Adicionado — a peça 18, com UMA tabela

***Decisão do Mizuki: uma tabela só,*** *"DnD não divide em múltiplas"*. **Trinta linhas, nove colunas** — nível, XP, maestria, espaços, refino, Classe, Passiva, Classe 0 e o que acontece.

**Dezenove dos trinta níveis entregam alguma coisa.** *Os onze restantes crescem em número e não em regra.*

**Três coisas ficaram de fora, e nenhuma por esquecimento:**

| o que | por quê |
|---|---|
| **vida e PE** | dependem do Caminho, e são duas contas de uma linha — dez colunas a mais para publicar duas fórmulas |
| **a escolha do marco** | são três eixos e quem escolhe é o jogador; o dono é a peça 11 §3 |
| **o que o degrau de Caminho e a entrega de Trilha dão** | são 89 entradas, e o índice delas é a peça 17 |

### Corrigido — a peça 2 publicava a rota de Refino com os números de antes da v0.89

**A tabela *"Três fichas ao longo da campanha"* dizia `5` aptidões no nível 22 e `7` no 30.** *São `6` e `10`.*

**Os números dela são os de antes da decisão da v0.89** — a que diz que, no teto, a escolha de Refino leva duas aptidões em vez de uma. *A peça 11 publica `10` na letra desde então.*

> **Aquela seção já carregava um aviso de que estava desatualizada, e o aviso falava de outra coisa:** *do terceiro eixo do marco, que entrou na v0.26.* **A contagem de aptidão é um segundo erro por baixo do primeiro, e ele passou nove versões.** *Nenhum validador lia aquela tabela — a peça 2 é a única peça de regra sem validador dono.*

### Adicionado — o `conferir-progressao.py`, com oito checagens

**Nenhum valor da tabela está escrito dentro dele.** *As nove colunas são reconstruídas lendo os donos e comparadas linha a linha.*

| # | o que ela confere | dono |
|---|---|---|
| 1 | a tabela tem 30 linhas, do 1 ao 30, sem buraco | — |
| 2 | XP | peça 12 §3 |
| 3 | maestria | peça 1 §2 |
| 4 | marcos e refino passivo | peça 11 §3 |
| 5 | espaços, e a **regressão** contra a tabela da peça 11 | a própria peça 18 §4 |
| 6 | degrau de Caminho e entrega de Trilha | `DESENHO-caminhos.md` |
| 7 | Classe, Passiva, Classe 0, Liberação e Técnica Máxima | manual §9 |
| 8 | a cópia de três fichas da peça 2 | a regra da peça 11 |

**A checagem 5 é a que impede a coluna nova de virar número solto.** *A peça 11 publica quatro valores que saem da mesma fórmula — `12` no nível 14, `16` no 20, `21` no 26 e `24` no 30 —, e o validador exige que a fórmula reproduza os quatro.* **Sem isso, a peça 18 poderia publicar qualquer coisa e sair verde contra ela mesma.**

**A checagem 8 é a que achou o erro da peça 2**, e ela roda a rota em vez de comparar com número guardado.

**E ela PULA sem o `python-docx`, e diz que pulou** — as colunas de Classe, Passiva e Classe 0 são as três que dependem do manual.

### As onze perturbações, em cópia isolada

| perturbação | esperado | deu |
|---|---|---|
| uma célula de XP muda na peça 18 | acende | acende |
| a peça 12 muda uma faixa de XP e a peça 18 não | acende | acende |
| a peça 1 muda um degrau de maestria | acende | acende |
| o calendário de marcos da peça 11 muda | acende | acende |
| **a fórmula dos espaços muda e a tabela da peça 11 não** | acende | acende |
| a peça 2 volta a dizer `7 apt` no nível 30 | acende | acende |
| o `DESENHO-caminhos` muda o calendário de Trilha | acende | acende |
| a tabela da peça 18 perde uma linha | acende | acende |
| **o cabeçalho da tabela da peça 18 muda de forma** | acende | acende |
| **contra-teste:** reescrever a coluna "o que acontece" sem mexer em número | verde | verde |
| sem `python-docx` | **PULA e diz** | PULA e diz |

### Em aberto

- **A curva de refino das três rotas continua no `arquitetura.md` §4.3**, que é documento de projeto e não peça. *É a última fonte da progressão fora de uma peça, e o candidato natural é a peça 11.*
- **A peça 2 continua sendo a única peça de regra sem validador dono.** *A checagem 8 alcança uma tabela dela, e só.*
- **O quick-start vai republicar esta tabela**, e aí ela vira número de dois donos — com a peça 18 sendo a fonte.
- O resto da lista da v0.98 continua igual.

---

## [0.98] — 2026-08-18

**A entrega estava em dia nas cópias e errada em tudo que não é cópia.** *As vinte e cinco cópias batiam byte a byte com a fonte e os dois repositórios estavam no mesmo commit — e mesmo assim ela mandava o leitor abrir dezenove arquivos que não estavam lá, e o README dela afirmava seis números que outra versão já tinha mudado.* **Nasceu a checagem 7, que é a primeira coisa do projeto que atravessa os dois repositórios.** Continuam dezessete peças e dezessete validadores.

### ⚠⚠ O defeito é de EIXO, e a checagem que devia pegar estava do lado errado dele

**A checagem 2 do `conferir-repositorio.py` resolve nome de arquivo contra a árvore INTEIRA.** *Uma peça copiada para `finalizado/` herda os arquivos da fonte, e todo ponteiro dela passa trivialmente.*

**Com o recorte da v0.97 no disco, ela via `472` caminhos e dizia `0 mortos`.** Resolvendo os mesmos ponteiros contra a árvore **da entrega**, `95` não existiam lá, em `29` alvos distintos.

| o que não resolvia | ocorrências | o que é |
|---|---|---|
| nome de validador — `conferir-*.py` | 53 em 15 arquivos | **argumento de design**, e fica na lista branca |
| **`arquitetura.md`** | **17 em 6 peças** | **material de mesa: é o dono da tabela de refino por marco** |
| `RASCUNHO-trilhas.md` | 7 em 5 arquivos | cortado do recorte **por decisão** — carrega o `Servo` |
| **`RASCUNHO-bloqueio.md`** | **2** | **material de mesa: a regra opcional do `Bloquear`** |
| caminho da árvore da fonte, `logs/`, `99-arquivo/`, geradores | 16 | ferramenta e histórico |

> **É a lição nº 8 por uma porta nova.** *Uma checagem que se mede pelo eixo errado sai verde exatamente na perturbação que importa* — e aqui ela nem precisou de perturbação: bastou a entrega existir no disco para ela passar a conferir menos, em silêncio, sem que nenhum número mudasse.

### Adicionado — os dois arquivos de material que a entrega citava e não carregava

**`arquitetura.md` e `RASCUNHO-bloqueio.md` entraram em `finalizado/desenho/`**, com uma caixa no README de lá dizendo por que os dois não são desenho.

- **O `arquitetura.md` está lá por uma seção só: a 4.3**, que publica quanto refino cada rota tem em cada marco, do nv6 ao nv30. **Aquela tabela não existe em peça nenhuma** — ela é uma das cinco fontes da progressão, e a única que ficava fora do recorte. *Sem ela não dá para publicar progressão.*
- **O `RASCUNHO-bloqueio.md` é a regra opcional do `Bloquear`** — rolar `2d10` no lugar da Defesa estática. **Metade da condição `Incapacitado` depende dela**, e a peça 1 mandava abrir um arquivo que não estava ali.

> **O conserto de verdade do primeiro é outro, e fica anotado:** aquela tabela **não devia morar no esqueleto**. Esqueleto é documento de projeto, não peça de regra, e a lição nº 9 diz que um número vivo tem uma peça dona. *Ela sai de lá quando a tabela de progressão consolidada for escrita.*

### Alterado — o README da entrega, seis afirmações e nenhuma delas era opinião

*Ele é o único arquivo daquele repositório que não existe na fonte, e por isso era o único que ninguém comparava com nada.*

| onde | dizia | é |
|---|---|---|
| duas linhas da tabela | *"as quinze condições"* | **catorze** — a v0.96 matou o `Paralisado`, e a §8.3 da peça 1 se chama *"As condições — as catorze"* |
| tabela "O que tem aqui" | `.docx` na **v7.8** | **v7.9**, e a linha 5 do próprio arquivo já dizia |
| o item 2 dos erros conhecidos | *"os dois estão na v7.8"* | **v7.9** nos dois desde a v0.95 |
| o bloco do porquê | `2,2 MB` · `628 KB` · `816 KB` | `4,9 MB` · `732 KB` · `2,0 MB` |
| **as duas Ações Bônus** | *"no FIM do `DESENHO-caminhos.md`"* | **a peça 3 §3.1 é a dona, e isso fechou na v0.83.** *O desenho tem a conta de preço, não a regra* |
| a primeira linha da tabela | iniciativa em `regra/01` e `regra/02` | **peça 3 §5** |

> **A quinta é a que mais custaria.** *Ela manda quem for escrever o PDF procurar a regra no arquivo de argumento em vez de na peça dona* — e o fim do `DESENHO-caminhos.md` diz, em letras, que a casa das duas é a peça 3. **Quinze versões apontando para o lugar errado.**

### Corrigido — e um achado na FONTE, não na entrega

**O problema de design nº 4 do `ESTADO-ATUAL` — *"a escolha de refino no marco paga mal, e três marcos pagam zero"* — estava listado como aberto, e a v0.89 fechou ele.** *Entrou na v0.41, fechou na v0.89 e ficou nove versões escrito como aberto.*

**E ele contradizia a linha de abertura do próprio arquivo**, que desde a v0.89 diz que aquele era *"o único problema de design que tinha sobrado"*. **A decisão está aplicada na peça 11 §3** — no teto a escolha de Refino leva duas aptidões —, e a checagem 5.2 do `conferir-aptidoes.py` mede marco a marco por causa dela.

> *Decisão registrada não é decisão aplicada, aplicado à lista que registra as decisões.*

### Adicionado — a checagem 7, em três partes

**7.1 — toda cópia bate byte a byte.** *As `27` do recorte, com guarda de contagem no piso.* Até aqui, a única forma de saber se a entrega estava velha era rodar `md5sum` na mão.

**7.2 — ponteiro pendurado, resolvido contra a árvore DA ENTREGA.** *Lista branca declarada, com teto: `161` citações, `85` brancas, folga de cinco.* Material de mesa não entra na lista branca — se uma peça manda abrir um arquivo de regra, ele tem que estar lá.

**7.3 — as cinco afirmações de número do README da entrega, cada uma contra o dono dela.** *Versão do recorte contra o topo deste CHANGELOG; versão do manual contra o `COMO-USAR.txt` do gerador; contagem de peças contra o README da fonte; contagem de condições contra o título da §8.3 da peça 1; total de entradas contra a linha de total da peça 17.* **Nenhum valor fica escrito dentro do validador.**

**E ela PULA com voz.** *`finalizado/` é ignorado pelo `.gitignore`, então um clone limpo não tem o recorte.* **O rodapé passou a imprimir `OK, mas N checagem(ns) PULARAM`**, no formato que a v0.97 escreveu para o `conferir-atributos.py` — a lição de que um verde que pulou checagem não é um verde, agora no validador da raiz também.

### As nove perturbações, em cópia isolada

| perturbação | esperado | deu |
|---|---|---|
| uma cópia da entrega muda de conteúdo | acende | acende |
| uma peça some da entrega | acende | acende |
| **a entrega manda abrir um `.md` que só existe na FONTE** | acende | acende |
| o README da entrega volta a dizer "quinze condições" | acende | acende |
| o README da entrega fica no recorte da v0.97 | acende | acende |
| o título da §8.3 da peça 1 muda de forma | acende | acende |
| **contra-teste:** o README cita mais um `conferir-*.py` que existe na fonte | verde | verde |
| **contra-teste:** o README cita uma peça que a entrega já carrega | verde | verde |
| `finalizado/` não existe | **PULA e diz** | PULA e diz |

> **⚠⚠ A terceira é o teste negativo direto do defeito de eixo, e ela vem com a prova junto.** *Com aquela citação no lugar, a checagem 2 imprime `491 caminhos conferidos, 0 mortos` — ela não acusa, porque o arquivo existe na fonte.* **Quem acusa é a 7.2, e ela é a única que olha para o eixo certo.**

> **E os dois contra-testes deram FALSO VERMELHO na primeira montagem, por minha causa e não do validador.** *Eu tinha escrito os dois perturbando uma **peça** da entrega* — **e peça é cópia byte a byte, então qualquer edição nela acende a 7.1 com razão.** *Um contra-teste não pode perturbar para um estado que outra checagem reprova de verdade, senão ele mede a checagem errada.* **Os dois foram para o `README.md` da entrega, que é o único arquivo de lá que não é cópia.**

### Em aberto

- **O `PROMPT-PROXIMA-CONVERSA.md` está escrito contra a v0.92**, seis versões atrás. *Ele carrega remendo de v0.93 e v0.94 e nada da v0.95 em diante.*
- **Não existe script de recorte.** *A entrega é montada à mão, e é por isso que ela pode sair incompleta sem ninguém ver.* **A checagem 7.1 acusa depois; um `recortar.sh` evitaria antes.**
- **A tabela de refino continua morando no esqueleto**, e ela é peça de regra disfarçada de documento de projeto.
- O resto da lista da v0.97 continua igual: a peça de dano e condições, as três Trilhas do Evocador, a terceira taxa do `Batedor`, o quick-start, a tabela de progressão consolidada e o playtest.
- **O Mizuki continua precisando instalar o `python-docx`** — `pip install python-docx --break-system-packages`.

---

## [0.97] — 2026-08-17

**O `subir.sh` falhou na máquina do Mizuki e passava na minha, e o motivo é o defeito nº 1 do projeto acontecendo de verdade: ele NÃO tem `python-docx` instalado.** *A checagem de condições da v0.95 caiu no caminho de pulada e quebrou lá dentro.* Continuam dezessete peças e dezessete validadores.

### ⚠⚠ O bug — `AVISOS` não existe no `conferir-atributos.py`

**Escrevi o caminho de pulada copiando o padrão do `conferir-aptidoes.py`, que tem `ERROS` e `AVISOS`.** *O `conferir-atributos.py` só tem `ERROS`.* **Então o `except ImportError` estourava `NameError` em vez de pular.**

*Ele só dispara em máquina sem `python-docx`* — por isso passou dez vezes seguidas de um lado e falhou do outro, com o mesmo arquivo no mesmo disco.

> **A pulada é o caminho MENOS testado de todo validador que lê o manual**, porque quem escreve a checagem quase sempre tem a biblioteca. *Bloquear o import na hora de escrever custa uma linha e é a única forma de exercitar aquele ramo.*

### ⚠⚠ E o achado que vale mais que o bug: três validadores estão CEGOS na máquina dele

**O `conferir-nomes.py`, o `conferir-manual.py` e o `conferir-pericias.py` saem `ok` sem `python-docx`** — eles pulam as checagens que leem o `.docx` e retornam código `0`. **É o defeito que o `README` documenta desde a v0.28, e ele está acontecendo agora, em produção.**

| validador | do que ele fica cego |
|---|---|
| `conferir-nomes.py` | **3 de 5** — a triagem de nome contra o manual inteiro |
| `conferir-manual.py` | **4 de 4 — todas.** *Ele sai no `except ImportError` antes da primeira checagem* |
| `conferir-pericias.py` | 1 de 8 |

> **A saída do `subir.sh` que ele mandou tem `ok conferir-manual.py`, e aquele `ok` não conferiu absolutamente nada.** *A v0.95 e a v0.96 mexeram no `.docx` — condições novas, `Paralisado` removido, dois feitiços prontos reescritos — e a metade do arnês que confere manual contra projeto não rodou do lado dele em nenhuma das duas.*

**Nada quebrou por causa disso**, porque a comparação rodou aqui e passou. *Mas ela passou por acidente de quem rodou, e não por desenho.*

### Corrigido — três coisas, e nenhuma é o número

1. **`AVISOS` virou `_PULADAS`**, declarada junto de `ERROS` no topo.
2. **O `except` deixou de pegar só `ImportError`.** *Qualquer outra falha de leitura do `.docx` — arquivo sumido, formato trocado, pacote `docx` errado — agora vira **erro** com o tipo da exceção na mensagem, em vez de traceback ou de silêncio.*
3. **O rodapé passou a IMPRIMIR as puladas.** *Antes ele dizia `TUDO OK` do mesmo jeito.* **Agora ele diz `OK, mas N checagem(ns) PULARAM`, e a linha do `[x]` parou de afirmar que a peça bate com o manual quando a comparação não rodou.**

> **A terceira é a que impede o defeito de voltar.** *Um verde que pulou checagem não é um verde; ele só parecia um porque ninguém imprimia a diferença.* **A lição nº 8 por outra porta: a checagem estava se medindo contra o que ela conseguiu fazer, e não contra o que ela devia fazer.**

### Conferido nos dois caminhos, que é o que faltava na v0.95

| | com `python-docx` | sem |
|---|---|---|
| **código de saída** | `0` | `0` |
| **a comparação com o manual** | roda | pula, e **diz que pulou** |
| **o rodapé** | `TUDO OK` | `OK, mas 1 checagem(ns) PULARAM` |

*O caminho sem a biblioteca foi exercitado bloqueando o import no `meta_path`, e não desinstalando nada.*

### Em aberto

- **O Mizuki precisa instalar o `python-docx`** — `pip install python-docx --break-system-packages`. *Enquanto não instalar, os três continuam saindo verdes sem conferir o manual, e isso é dele e não do código.*
- **Vale um `PULADA` visível nos outros três também.** *Hoje eles pulam e imprimem aviso no meio da saída, que o `subir.sh` joga em `/dev/null`.* **O `subir.sh` mostra `ok` e mais nada — ele não tem como saber a diferença.** *Fica anotado como a próxima coisa a arrumar nesse eixo.*
- O resto da lista da v0.96 continua igual.

---

## [0.96] — 2026-08-17

**O `Paralisado` deixou de existir, e o `Incapacitado` ficou com o efeito dele.** *Correção da v0.95, pedida pelo Mizuki: eram para ser **duas** condições nesse lugar e não três, e eu tinha inventado uma escada de três que ninguém pediu.* **São catorze condições — nove Menores e cinco Maiores.** Manual na v7.9, dezessete peças e dezessete validadores.

### ⚠⚠ O que eu errei, e vale escrever porque foi erro de leitura e não de conta

**O Mizuki escreveu duas condições, com efeito cada uma**, e disse depois que o `Atordoado` da fonte era o `Paralisado` dele e que valia mudar o nome.

**Eu li aquilo como pedido de uma escada de TRÊS degraus** — Atordoado, Incapacitado e Paralisado, cada um num eixo —, e o pedido era **renomear uma e ficar com duas.** *A v0.95 publicou uma condição a mais que ninguém tinha pedido, e ela chegou até o `.docx` e o `.pdf`.*

> **O sintoma que eu tinha na mão e não usei: a pergunta que eu fiz oferecia três opções e ele escolheu a que dizia "só troca os nomes de lugar".** *"Troca de lugar" é operação entre **dois**.* **A resposta dele já continha a contagem, e eu li a parte do meio e não a palavra que decidia.**

### Como ficou

| | o eixo que ela ataca |
|---|---|
| **Atordoado** | tira **parte do turno** — uma Ação Padrão e a reação. *Quem tem mais de uma perde **uma**.* Você continua se defendendo |
| **Incapacitado** | não tira turno nenhum: tira a **defesa**. **Sem `Bloquear`, e todo ataque corpo a corpo contra você é crítico** |

**Elas não se empilham, e é isso que as separa.** *No d20 o `Paralisado` é o `Atordoado` mais o crítico no corpo a corpo — um herdando do outro, e o de baixo nunca vira escolha.* **Aqui a Condição Maior custa `Pesada` e você escolhe o eixo: tirar o que ele faz, ou tirar o que protege ele.**

> **E o terceiro degrau não cabia mesmo.** *Uma condição que fosse a soma das duas só teria sentido custando mais que `Pesada`,* **e a escada de preço do manual não tem degrau acima dela.** *A v0.95 criou uma linha que custava o mesmo que as outras duas e valia mais — dominância pura, e nenhum validador do projeto olha para dentro de uma Condição Maior.*

### Alterado — os dois feitiços prontos, e o validador do manual junto

**A `Rede` e a `Prisão de Sombras` aplicavam `Paralisado`.** *Agora aplicam `Atordoado`, no `partF.js` e no `pac7.py`.* **O preço não mudou** — as duas continuam comprando uma Condição Maior por `Pesada` —, e o `pac7.py` passa.

*Elas voltaram a fazer o que faziam antes da v0.95: travar o turno do alvo.* **A v0.95 tinha mudado o efeito delas de lado sem que ninguém pedisse.**

### Alterado — o manual, ainda v7.9

*A versão não subiu porque a v7.9 não chegou a ser commitada com a lista errada.* **`365` parágrafos e `88` tabelas, iguais.** *A tabela de Maiores foi de seis linhas para cinco, a caixa dos eixos foi reescrita para dois, e o `.pdf` saiu junto, em `45` páginas.*

### As seis perturbações, em cópia isolada

| perturbação | esperado | deu |
|---|---|---|
| **o `Paralisado` volta para a lista de Maiores** | acende | acende |
| uma condição some da peça e fica só no manual | acende | acende |
| uma Menor também aparece entre as Maiores | acende | acende |
| uma das que estão fora volta para a lista | acende | acende |
| **contra-teste:** reescrever o efeito sem mexer no nome | verde | verde |
| o título da seção das Maiores muda | acende | acende |

**A primeira é a que importa**, e ela é o teste negativo direto desta versão: se alguém reintroduzir o `Paralisado`, a comparação peça-contra-manual acende nas duas direções.

### Em aberto

- **Nada mudou na lista da v0.95.** *A peça de dano e condições continua devendo a Cicatriz, o clash e as vagas de `Desliga`; as três Trilhas do Evocador e a terceira taxa do `Batedor` continuam fora por decisão.*
- **A força das catorze é previsão**, e vai ser medida no playtest. *`04-playtest/` continua vazia.*
- **O que falta para alguém jogar não é regra, é material:** o **quick-start** e a **tabela de progressão consolidada**.

---

## [0.95] — 2026-08-17

**As condições ganharam efeito, e o manual subiu para a v7.9.** *Eram doze nomes com preço e sem regra — `Condição Menor` custa Média e `Condição Maior` custa Pesada desde sempre, e nenhuma das doze dizia o que fazia.* **Agora são quinze, cada uma com uma linha, no manual e na peça 1.** Continuam dezessete peças e dezessete validadores.

### ⚠⚠ O buraco: doze termos cobrados e indefinidos, em sete mesas

**A linha de `Condição Maior` do manual dizia *"Aplica uma: Atordoado, Paralisado, Amedrontado, Enfeitiçado ou Incapacitado"* e parava aí.** *Um jogador comprava Pesada por `Atordoado` e a mesa decidia na hora o que aquilo significava.*

> **É o formato do buraco do `Mirar` na v0.86 — concedido em treze lugares, definido em nenhum — só que multiplicado por doze e com preço em cima.**

### Decidido — usar as do d20 para tudo que já tinha nome, e escrever à mão só as três que precisam ser diferentes

***Decisão do Mizuki.*** *Mesmo motivo dos metros e da Cobertura: condição não tem conversão em fatia neste sistema, então o número não sai de conta daqui — ele precisa é ser o mesmo em sete mesas.*

**Três condições novas, espalhadas entre os dois tamanhos:** `Impedido` e `Envenenado` entram como Menores, `Petrificado` como Maior. **As Menores vão de sete para nove e as Maiores de cinco para seis.**

### Decidido — os três nomes do meio trocaram de lugar, e cada um atacou um eixo

***O Mizuki viu a colisão sozinho:*** *"atordoado do dnd seria basicamente o paralisado, até recomendo mudar o nome".* **Ele estava certo — a definição que ele tinha escrito para `Paralisado` é o `Atordoado` da fonte, e a que ele tinha escrito para `Incapacitado` é o `Paralisado` de lá.**

***Decisão dele: trocar os nomes de lugar.***

| | o eixo que ela ataca |
|---|---|
| **Atordoado** | tira **parte** do turno — uma Ação Padrão e a reação |
| **Incapacitado** | tira o turno **inteiro** — nem padrão, nem bônus, nem reação, nem `Bloquear` |
| **Paralisado** | não tira turno nenhum: tira a **defesa**. Sem `Bloquear`, e todo ataque corpo a corpo vira crítico |

**O `Paralisado` com o crítico volta a bater com a fonte**, onde o crítico no corpo a corpo é exatamente a linha que separa o `Paralisado` do `Atordoado`.

> **O custo dessa troca está declarado: a `Rede` e a `Prisão de Sombras`, dois feitiços prontos do manual, aplicam `Paralisado` e passam a aplicar uma condição de outro formato** — ela não trava mais o turno do alvo, ela abre a guarda dele. *O `pac7.py` continua passando porque o preço não mudou; o que mudou foi o que o jogador recebe.*

> **O `Atordoado` cobra UMA Ação Padrão de propósito.** *Um chefe age mais de uma vez por rodada.* **Apagar o turno inteiro dele com uma linha de Controle sairia barato demais** — e quem quiser isso tem o `Incapacitado`, que custa a mesma Pesada e é escolha em vez de sorte.

### Decidido — três ficaram de fora, com o motivo escrito

| | por quê |
|---|---|
| **Inconsciente** | ***decisão do Mizuki:*** aqui é **cair morrendo**, e já tem regra própria — a seção 5.5 da peça 1, com as duas escolhas e a janela de três rodadas. *Uma condição de uma rodada com o mesmo nome faria a mesa confundir o pior estado do jogo com um efeito que passa sozinho.* |
| **Exaustão** | já existe e é da **peça 10** — relógio de descanso, não efeito de combate. *É a que mais engana, porque na fonte ela é condição e aqui não.* |
| **Invisível** | é **benefício**. *Comprar Média para aplicar num inimigo é pagar para ajudar ele.* |

### ⚠ E metade do `Paralisado` depende de uma regra opcional

**O `Bloquear` — rolar `2d10` no lugar da Defesa estática — mora no `RASCUNHO-bloqueio.md`, e nem toda mesa vai ligar.** *Onde ele estiver desligado, o `Paralisado` é só o crítico no corpo a corpo, que é a metade que sempre vale.* **Escrito na peça para ninguém achar que a condição está pela metade por engano.**

### Adicionado — a checagem de espalhamento, e só ela

***Decisão do Mizuki: não validar a força, só a distribuição*** — *"vamos testar no sistema depois"*. **É coerente com o que elas são: nenhuma produz número que entre em conta.**

**A checagem entrou no `conferir-atributos.py`**, que é o dono da peça 1, e confere quatro coisas: ninguém em dois tamanhos ao mesmo tempo, nada que está declarado *fora* aparecendo numa das listas, a peça batendo com o manual **nas duas direções**, e a guarda de contagem.

### ⚠ E o extrator do `conferir-nomes.py` passou a bater as DUAS listas do próprio `.docx`

**A guarda de contagem da v0.88 acusou na hora**, porque ela esperava doze condições e o manual passou a devolver quinze. *Ela existe desde que a triagem ficou cega para as condições e deixou a Manha `Abalo` batizar de `Caído` o que o manual já chamava de `Derrubado`.*

**E ela expôs uma coisa nova: o `.docx` agora tem DUAS listas da mesma coisa** — a frase *"Aplica uma: …"* e as tabelas de efeito. *Em vez de escolher uma e torcer, o extrator lê as duas e falha se divergirem.* **Lição nº 9 dentro de um arquivo só.**

### As sete perturbações, em cópia isolada

| perturbação | esperado | deu |
|---|---|---|
| uma condição some da peça e fica só no manual | acende | acende |
| uma condição muda de nome só de um lado | acende | acende |
| **uma das que estão fora volta para a lista de Maiores** | acende | acende |
| **uma Menor também aparece entre as Maiores** | acende | acende |
| **contra-teste:** reescrever o efeito sem mexer no nome | verde | verde |
| o título da seção das Maiores muda | acende | acende |
| a peça perde a seção inteira | acende | acende |

> **⚠ E a primeira tentativa da sexta foi FALSO NEGATIVO meu, não do validador.** *Perturbei `### As seis Maiores` para `### As seis MaioresX` — e o extrator usa `find`, que acha o título como **substring** do perturbado.* **A perturbação mudou o arquivo e não mudou o comportamento.** *É a regra 3 do arnês pegando exatamente o caso que ela existe para pegar: conferir que o `sed` bateu não basta se o que você trocou continua casando.*

### Alterado — o manual, v7.8 para v7.9

**Duas tabelas novas com o efeito de cada condição, mais duas caixas** — a dos três eixos e a das três que ficaram de fora. *`365` parágrafos contra `363`, e `88` tabelas contra `84`.*

**O `pac7.py` e o `v7.py` passam**, e o `.pdf` saiu junto, em `45` páginas. *Segunda versão seguida em que ele não fica atrasado.*

### Em aberto

- **A peça de dano e condições continua não existindo**, e agora ela deve menos: *a lista de condições saiu dela.* **Sobram a Cicatriz, o clash e as vagas de `Desliga`.**
- **As três Trilhas do Evocador**, fora por decisão.
- **A terceira taxa sem medida do `Batedor`.** *Fica para depois, e é pergunta de mesa.*
- **A força de cada condição é previsão**, como todo número deste sistema. *`04-playtest/` continua vazia.*
- **O que falta para alguém jogar não é regra, é material:** o **quick-start** e a **tabela de progressão consolidada**.

---

## [0.94] — 2026-08-17

**O sistema ganhou nome, e as duas últimas regras que faltavam foram escritas.** *`Projeto - M`, os metros de cada arma de projétil, e a Cobertura.* **A pendência do nome estava aberta desde a v0.1 — noventa e três versões.** Continuam dezessete peças e dezessete validadores.

### Decidido — o sistema se chama `Projeto - M`

***Decisão do Mizuki.*** *Passou na triagem: `Projeto`, `M` e o composto saem todos `LIVRE`.*

**Aplicado em seis documentos**, e a pendência saiu das quatro listas que a carregavam — a do `ESTADO-ATUAL`, a do `arquitetura.md`, a do pacote de entrega e a do prompt de retomada.

### ⚠ Achado — a dívida dos metros contava onze armas, e eram DEZENOVE

**A nota da v0.74 dizia *"nenhuma das onze armas de tiro tem metro escrito"*.** *Só que a declaração da própria propriedade, duas seções acima, diz `Longo Alcance` — número em metros para projétil **e arremesso**.*

**As oito de `Arremesso` carregam a propriedade e ficaram de fora da contagem.** *`Punhal`, `Machadinha`, `Kusarigama`, `Lança`, `Kunai`, `Shuriken`, `Tessen` e `Chakram`.*

> **É o segundo exemplar em duas versões seguidas.** *Na v0.93 o `Classe` solto foram treze lugares contra os oito publicados.* **Contagem à mão de uma família de erros pega a amostra que a pessoa estava olhando, e não a família.**

### Decidido — importar os números do d20 em vez de derivar, e a fonte fica declarada

***Decisão do Mizuki.*** **A conversão é `5 pés = 1,5 m`**, a mesma que põe o deslocamento padrão em `9 m`.

**O motivo de importar está escrito na peça, porque ele não é preguiça: alcance de arma não tem preço neste sistema.** *A propriedade `Longo Alcance` custa `1` ponto para toda arma que a tem, e custa por existir — não por quanto.* **Então o número não sai de conta nenhuma daqui.** *Ele precisa ser plausível, consistente entre as armas e igual em sete mesas — e uma tabela publicada que todo mundo já conhece faz as três coisas de graça.*

| | faixa normal | faixa longa |
|---|---|---|
| **Daikyū** — arco longo | `45 m` | 180 m |
| **Besta** — besta pesada | `30 m` | 120 m |
| **Hankyū** · **Rifle** · **Rifle de Precisão** · **Metralhadora Pesada** | `24 m` | 96 · 72 m |
| **Submetralhadora** | `15 m` | 45 m |
| **Revólver** | `12 m` | 36 m |
| **Besta de Uma Mão** · **Pistola** · **Espingarda** | `9 m` | 36 · 27 m |
| **as oito de arremesso, todas** | `6 m` | 18 m |

### ⚠ Alterado — a faixa longa deixou de ser o dobro

**O §5.2.1 dizia *"até o dobro disso"* desde a v0.74, e aquilo era régua provisória** — escrita quando não havia catálogo nenhum para olhar, e a própria seção declarava que os metros ficavam em aberto.

**A fonte usa `4×` para arco e besta e `3×` para arma de fogo e arremesso.** *Importar os números sem importar a proporção seria trazer metade da tabela.*

> **Nada foi reprecificado, e isso é o ponto:** desvantagem continua valendo os mesmos `−25` pontos percentuais, e o `Longo Alcance` continua custando `1` ponto. *A mudança é de alcance, e alcance é a única coisa desta peça que nunca entrou numa conta de preço.*

### Declarado — o empate de três, e a arma sem correspondente

**`Rifle`, `Rifle de Precisão` e `Metralhadora Pesada` empatam em `24 m`, e o empate é da fonte.** *Lá o rifle de caça e o automático têm o mesmo alcance e dados diferentes.* **O `Rifle de Precisão` se separa pelo dado — `2d10` contra `2d8` — e não pela distância.** *Se um dia ele precisar alcançar mais, esse número vai ter de sair de fora da fonte, e aí vira decisão de design em vez de importação.*

**A `Kusarigama` é a única sem correspondente**, porque foice presa a corrente não é arremesso solto. *Ficou com a faixa da família, e a ficção da corrente sugere menos.* **Declarado para quem reler não procurar defeito onde houve escolha.**

### Adicionado — a Cobertura, na peça 1

**Ela não existia, e havia menção pela pasta contando com ela** — inclusive um degrau de nível 27 que promete *"a cobertura para de significar alguma coisa"*. **Uma entrega prometendo apagar uma regra que ninguém tinha escrito.**

***Decisão do Mizuki: a métrica é a mesma do d20, sem adaptação.*** *`+2` na Parcial, `+5` na Boa, e a Total tira você da lista de alvos legais.*

> **A única tradução que precisou de decisão foi o Teste de Resistência.** *A fonte fala em salvaguarda de Destreza; aqui quem ocupa esse lugar é o **TR Físico**, que é travado em Força ou Destreza na criação.* **Quem travou em Força também se abaixa atrás de uma mureta** — amarrar a cobertura em Destreza criaria uma segunda regra para metade das fichas.

**Duas travas que a fonte tem e que ficaram escritas:** vale só contra o que vem do outro lado da cobertura, e **só a maior conta** — duas parciais não viram uma boa.

### Sem validador novo, e por decisão

***Decisão do Mizuki: as duas entram sem checagem.*** **É coerente com o que elas são: nenhuma das duas produz número que entre em conta.** *Alcance nunca foi preçado, e cobertura não tem conversão em fatia — a régua de preço deste projeto não tem o que medir aqui.*

*Os vinte validadores existentes continuam passando, com `PULADA=0`.* **O que fica sem guarda é a cópia**, se algum dia esses números aparecerem em dois documentos.

### Em aberto

- **A peça de dano e condições** — *19 lugares em 7 documentos.* **Decisão do Mizuki: fica de fora por enquanto**, e quando vier pode sair sem a mecânica de condição.
- **As três Trilhas do Evocador**, fora por decisão.
- **A terceira taxa sem medida do `Batedor`** — *em quantas rodadas o atirador fica parado.* **Fica para depois, e não é conta: é pergunta de mesa.**
- **O que falta para alguém jogar não é regra, é material:** o **quick-start**, a **tabela de progressão consolidada** e o **playtest**. *`04-playtest/` continua vazia, e todo número do sistema é previsão.*

---

## [0.93] — 2026-08-17

**Três pendências pequenas fecharam, e uma delas era grande por dentro.** *As duas entregas em minúscula, o `Classe` solto da peça 11, e o `.pdf` do manual — que estava sete versões atrás do `.docx` desde a v7.4.* Continuam dezessete peças e dezessete validadores.

### ⚠⚠ Achado — a minúscula do `carregar` não era descuido, era evasão

**A triagem devolve `Carregar` como `OCUPADO`: é Restrição no manual.** *Alguém baixou a letra para fugir da colisão e ninguém escreveu por quê — então a pendência ficou catorze versões listada como *"inconsistência de capitalização"*, que é o sintoma.*

**As duas entregas tinham causas diferentes e estavam contadas como uma coisa só.** *O `acelerar` não colide com nada — `Acelerar` sai `LIVRE` — e só precisava da maiúscula.*

> **É o mesmo formato do defeito do `Efeito Próprio` na v0.92, virado do avesso.** *Lá o projeto procurava uma régua que já tinha dono; aqui ele descrevia um sintoma sem nunca ter perguntado a causa.* **Uma pendência escrita pelo que se vê não diz o que precisa ser feito.**

### Decidido — `Disparo Carregado`, e o `Acelerar` só ganhou a maiúscula

***Decisões do Mizuki.*** *Os dois passaram na triagem.*

**As três rotas do `Batedor` nomeiam a peça do mecanismo** — `Manivela` na `Besta`, `Ferrolho` na `Arma de Fogo` —, e o `Yumi` era o único com verbo. *Foi oferecido `Corda`, que fecharia o paralelo; ele escolheu `Disparo Carregado`, que guarda a leitura antiga do nome.*

**Duas coisas que a triagem não pega, declaradas:** `Carregado` fica a duas letras da Restrição `Carregar`, no molde do `Mirar` contra `Mira` que a v0.87 já aceitou; e é a **única entrega de Trilha de nível 2 com duas palavras**, contra catorze de uma só. *Nenhuma das duas bloqueia — ficam escritas para a próxima releitura não procurar defeito onde houve escolha.*

**Vinte e um lugares trocados**, e as seis ocorrências em que `carregar` e `acelerar` são palavra comum do português ficaram intactas — *"deixam de carregar `Munição`"*, *"um número a menos para a mesa carregar"*.

### ⚠ Corrigido — o `Classe` solto eram TREZE lugares, e a contagem publicada dizia oito

**Os oito contados eram os quatro títulos das anti-domínio mais as quatro linhas da tabela de degraus.** *Escaparam cinco: a frase que diz "a única Classe 3", os dois da linha que explica o que impede a Classe 3 de comer as outras, a trava da `Aptidão Própria`, e a nota da v0.29.*

> **É a lição da v0.90 outra vez: checagem escrita no braço para UM caso deixa os outros descobertos.** *Aqui nem chegou a virar checagem — virou contagem à mão de uma família de erros, e a família era maior que a amostra.*

**E cinco ocorrências de `Classe N` solto SOBREVIVEM de propósito**, porque são Classe de feitiço: o `Classe 0` da linha do Projetar, o `Classe 7` do `Anteparo`, o `Classe 0` do achado da v0.80, e as duas da seção 4 — que é justamente a seção que existe para explicar a ambiguidade, e onde escrever solto é o exemplo.

### Adicionado — duas checagens, e as duas leem o limite do documento

**A 11ª do `conferir-catalogo.py`:** todo nome batizado do índice começa com maiúscula. *Ela varre as 89 entradas em vez das duas que estavam erradas, e a guarda de contagem compara os nomes extraídos com as células que a peça conta como tendo nome.* **Ela acusa se o extrator passar a ver menos, em vez de conferir menos calada.**

**A do `conferir-aptidoes.py`:** a regra da seção 4 aplicada à peça inteira. *O detalhe que a faz funcionar sem lista de exceção escrita no braço: **a escada de Classe Passiva tem três degraus, e o validador lê quais da tabela da própria seção 4.*** **Então `Classe 0` e `Classe 4` a `7` passam livres por construção** — eles não existem como Passiva —, e só `1`, `2` e `3` precisam das duas palavras.

> **O número que ela guarda é limite de design e está declarado à parte:** `53` ocorrências na forma correta hoje. *Se cair, alguém reescreveu as Passivas e a checagem passou a conferir menos.*

### As oito perturbações, em cópia isolada

| perturbação | esperado | deu |
|---|---|---|
| **uma entrega volta para minúscula** | acende | acende |
| **contra-teste:** renomear mantendo a maiúscula | verde | verde |
| **o extrator de nomes passa a ver menos** | acende | acende |
| um título de anti-domínio volta a `Classe N` solto | acende | acende |
| **a trava da `Aptidão Própria` volta a `Classe N` solto** | acende | acende |
| **contra-teste:** um `Classe 0` novo fora da seção 4 | verde | verde |
| **a tabela da escada da seção 4 muda de formato** | acende | acende |
| a guarda de contagem: some metade das `Classe Passiva` | acende | acende |

### Adicionado — o `.pdf` do manual, e ele parou de ser exportado a mão

**Ele estava na v7.4 contra a v7.8 do `.docx`, atrás desde que a v7.5 renomeou a `Barreira`.** *A causa era o processo: exportação manual pelo Word, que ninguém lembrava de rodar.*

**Sai de `soffice --headless --convert-to pdf`.** *Conferido: `44` páginas nos dois, a capa dizendo `Versão 7.8`, e os termos do manual todos presentes no texto extraído.* **É a única das pendências desta leva que não era texto — era um passo de processo que não tinha dono.**

### ⚠ E o aviso do ponteiro pendurado das skills MORREU, medido

**A v0.66 registrou que as quatro skills com pasta de apoio estavam instaladas só com o `SKILL.md`, apontando para arquivo que não existia.** *Medido de novo nesta versão: os seis arquivos estão lá, e batem byte por byte com os da pasta de trabalho.*

**Corrigido nos dois documentos que carregavam o aviso.** *Aviso que parou de reproduzir é dívida — um procedimento com o motivo errado envelhece pior que um sem motivo nenhum.*

### E a deriva das skills se separou por CAMADA, o que nenhuma versão anterior tinha visto

**A instalada estava na frente só na descrição**, em seis das sete: uma frase de fronteira mandando mesa e lore para a `mizuki-copiloto-do-mestre`. **A pasta estava na frente só no corpo**, em quatro das sete.

*Nenhum dos dois lados estava velho por inteiro — cada um era dono de uma metade do arquivo.* **A regra do merge saiu disso e é mecânica: corpo da pasta, descrição da instalada.** *As sete foram conferidas por script depois: o frontmatter parseia, só a linha de descrição mudou em relação à pasta, e nenhum cabeçalho da instalada sumiu.*

### Em aberto

- **A peça de dano e condições continua sendo a maior dívida** — *19 lugares em 7 documentos de conteúdo esperam por ela.* **Decisão do Mizuki nesta versão: ela pode sair SEM a mecânica de condição**, no molde do que o pacote de entrega já declara.
- **As três Trilhas do Evocador ficam fora por decisão**, e não por falta de tempo.
- **Cobertura não existe como regra** — *uma menção na pasta inteira* — e os **metros das onze armas de projétil** também não. *A régua deles já está escrita desde a v0.74: duas faixas mais o `colado`, com a Forma `Projétil` do manual como âncora em `18 m`. Falta o catálogo.*
- **A terceira taxa sem medida do `Batedor`** — *em quantas rodadas o atirador fica parado.* **Não é conta, é pergunta de mesa.**
- **O que falta para alguém jogar não é regra, é material:** o **quick-start**, a **tabela de progressão consolidada** e o **playtest**. *`04-playtest/` continua vazia.*
- **O nome do sistema**, aberto desde a v0.1.

---

## [0.92] — 2026-08-17

**O catálogo de aptidões fechou de verdade: as catorze entradas têm regra escrita.** *A `Aptidão Própria` era a última, e ela estava listada como "falta a régua" desde a v0.3.* **A régua nunca precisou ser escrita — ela é do manual, está numa tabela, e ninguém tinha aberto.** Continuam dezessete peças e dezessete validadores.

### ⚠⚠ Achado — a régua do `Efeito Próprio` existe, publicada, e a peça 11 passou sessenta versões dizendo que faltava

> **`Efeito Próprio · Passiva Própria` — *Em quantas cenas por arco isso vai importar?*** *Uma cena: **Leve**. Metade: **Média**. Quase toda: **Pesada**. **Na dúvida, Pesada.***

**Ela está na tabela de Melhorias do manual, com as três faixas e o critério de desempate incluído.**

**É o terceiro exemplar do mesmo defeito em doze versões:** *o Classe 0 na v0.80 — tabela própria no manual que nenhum documento abria; a ação `Mirar` na v0.86 — treze menções concedendo e nenhuma definindo; e agora esta.* **O projeto procurando um número que já tinha dono.**

### Adicionado — e as três faixas caem nos três degraus da escada de Classe Passiva

| em quantas cenas por arco | o manual cobra | e a escada da peça 11 §4 diz |
|---|---|---|
| **uma** | Leve | **Classe Passiva 1** — pequeno, condicional, ou de informação |
| **metade** | Média | **Classe Passiva 2** — reativo, com limite por cena ou por descanso |
| **quase toda** | Pesada | **Classe Passiva 3** — permanente. Muda como você joga |

**A escada da peça mede FORMA; a do manual mede FREQUÊNCIA. E as duas caem nos mesmos três degraus.** *Não é coincidência: condicional dispara pouco, reativo com limite dispara em parte, permanente dispara sempre.* **É a mesma escada vista pelos dois lados** — e é por isso que a §4 pôde dizer *"ela não mede quanto, mede o quê"* sem deixar a aptidão sem preço.

> ***E a trava que já estava escrita ganhou número:*** *`Classe Passiva 1 ou 2, nunca 3`* **quer dizer que uma `Aptidão Própria` importa em NO MÁXIMO metade das cenas de um arco.**

### Adicionado — os cinco requisitos, e o que a ficha carrega

**São o molde da `Regra Própria` do manual, com um trocado.**

1. **Uma frase.**
2. **Verificável** — a mesa aponta o momento em que ela disparou.
3. **Não é atalho** — não repete uma das treze do catálogo com outro nome, nem entrega uma que o seu gate ainda não alcança.
4. **Sem dado de dano** — a cerca da peça 5 §4 vale inteira.
5. **Com limite por cena**, se for Classe Passiva 2.

> **O requisito que NÃO veio é a simetria.** *A `Regra Própria` exige "vale contra você nas mesmas condições" porque ela **impõe uma regra ao mundo**, e regra que só pega os outros é a definição de abuso.* **Uma `Aptidão Própria` não impõe regra a ninguém: ela muda o que VOCÊ faz.** *Exigir simetria mataria metade das propostas legítimas por um motivo que não se aplica.*
>
> **No lugar entrou o nº 3, e ele guarda o risco desta camada: a `Aptidão Própria` virar a porta dos fundos do catálogo.** *Sem ele, um jogador escreve a `Energia Reversa` com outro nome e pula o gate de refino 7.*

**E o que faz ela sobreviver a sete mesas é uma linha só: a ficha carrega a RESPOSTA da pergunta de frequência, e não só o texto.** *Um segundo mestre lê "metade das cenas" e sabe o degrau. Lendo só a frase, ele reconstrói a intenção — e sete mestres reconstroem sete intenções.*

**O desempate é o do manual, com o sinal a favor da mesa: na dúvida, Pesada.** *Aqui isso quer dizer Classe Passiva 3, e a `Aptidão Própria` não alcança a 3.* **Então a dúvida REPROVA a proposta.** *É o único lugar do sistema em que "não sei" tem resposta escrita, e ela é "não".*

### E o exemplo que mais ensina é o que foi recusado

| proposta | em quantas cenas | degrau | veredito |
|---|---|---|---|
| *"você sabe se um objeto foi tocado por energia amaldiçoada nas últimas 24 horas"* | uma por arco | Classe Passiva 1 | passa |
| *"1× por cena, um aliado a até 9 m rerrola um Teste de Resistência falhado"* | metade | Classe Passiva 2 | passa |
| **"o seu deslocamento é `+3 m`"** | quase toda | **Classe Passiva 3** | **recusada** |

**`+3 m` sempre vale `0,35` fatia na tabela da peça 5 §4 — é barato, e mesmo assim está fora.** *A trava não é de tamanho: é de forma.* **Uma coisa que está sempre ligada é Classe Passiva 3, e ponto.**

### Adicionado — a checagem 5.4, a 4j do `conferir-manual.py`, e a guarda subiu para catorze

**A 5.4 é diferente das outras porque o conteúdo desta entrada não está no repositório:** ele é escrito na mesa. *Então o que ela confere não é o efeito — é a **cerca**.* **O teto de Classe Passiva, as três faixas na ordem certa, os cinco requisitos, e que a dúvida recusa em vez de aceitar.**

**A 4j fecha a cópia:** as três faixas da peça 11 contra a tabela do `.docx`, com o *"Na dúvida, Pesada"* conferido nos dois lados.

**E a guarda de contagem da checagem de gate subiu de treze para catorze** — as catorze entradas do catálogo agora têm seção própria, e a comparação título-contra-catálogo cobre todas.

### ⚠ E a checagem do `por cena` da peça 10 acusou na primeira edição, pela segunda vez

**Escrever a `Aptidão Própria` acrescentou três usos de `por cena` na pasta**, e a peça 10 publicava `93`. *A checagem reconta da pasta e falhou na hora.* **De `93` para `96`** — *a v0.83 tinha feito o mesmo caminho, de `91` para `93`, com o `Ler o Ambiente`.* **Lição nº 1 fazendo o trabalho dela duas vezes.**

### As sete perturbações, em cópia isolada

| perturbação | esperado | deu |
|---|---|---|
| **o teto de Classe Passiva some da 6.7** | acende | acende |
| **a dúvida passa a APROVAR em vez de recusar** | acende | acende |
| a escada de frequência inverte duas faixas | acende | acende |
| **a cópia da escada diverge do manual** | acende | acende |
| um dos cinco requisitos some | acende | acende |
| **contra-teste:** reescrever um requisito sem mudar a contagem | verde | verde |
| **contra-teste:** um exemplo a mais na tabela dos três | verde | verde |

### Em aberto

- **O catálogo de aptidões não deve mais nada.** *As catorze têm regra, gate e validador.*
- **⚠ E sobra uma inconsistência de vocabulário que esta versão viu e não consertou:** *as quatro anti-domínio da §6.5 escrevem `Classe 1`, `Classe 2` e `Classe 3` soltos, e a §4 desta mesma peça diz **"sempre com as duas palavras, e nunca `Classe` solta"**.* **A `Energia Reversa` e a `Aptidão Própria` escrevem `Classe Passiva`.** *São oito lugares, e é conserto de texto e não de número.*
- **Duas entregas têm nome em minúscula** — o `carregar` do `Yumi` e o `acelerar` da `Torrente`.
- **A peça de dano e condições não existe, e 18 lugares em 8 documentos esperam por ela.** *É a maior dívida estrutural do projeto: a Cicatriz, a lista de condições com nível, o clash e as vagas de `Desliga` moram todos nela.*
- **As três Trilhas do Evocador continuam paradas**, e o `Servo` continua dominado pelas duas irmãs por falta de eixo.
- **Cobertura não existe como regra**, e os metros de cada arma de projétil também não.
- **A terceira taxa sem medida do `Batedor`** — *em quantas rodadas o atirador fica parado* —, e ela não é conta: é pergunta de mesa.
- **O que falta para alguém jogar não é regra, é material:** o **quick-start**, a **tabela de progressão consolidada** e o **playtest**. *`04-playtest/` continua vazia, e todo número do sistema é previsão.*
- As de sempre: o `.pdf` do manual na v7.4 contra a v7.8 do `.docx`, e o **nome do sistema**.

---

## [0.91] — 2026-08-17

**O catálogo de aptidões fechou.** *A `Barreira Simples` e a `Cortina` eram as duas últimas entradas sem número, e estavam assim desde a v0.3.* **As doze que custam marco agora têm regra escrita, e a rota pura de Refino ganhou duas de folga em vez de fechar no talo.** Continuam dezessete peças e dezessete validadores.

### ⚠⚠ Medido — uma barreira com vida, se couber numa luta, vale mais que a Trilha da ficha

***O Mizuki chegou com o problema pelo nome antes de qualquer conta:*** *"se não vira uma vida extra paia"*. **A conta concorda, e ela é pior do que parece.**

> **A régua do projeto diz que dano evitado converte `1` pra `1`.** *Uma barreira que o inimigo precisa quebrar consome nele exatamente a vida dela — então ela **evita a própria vida**.*

| vida no teto | evita | por rodada de luta | em fatias |
|---|---|---|---|
| `50` | 50 de dano | 12,5 | **2,46** |
| `200` | 200 de dano | 50,0 | **9,84** |

**Uma Trilha inteira leva `5,00` fatias. Um marco compra `2,13`.**

### ⚠ E gastar a rodada inteira levantando NÃO gateia

*Era a primeira ideia dele — "talvez necessitar ser ação completa".* **A conta reprova, e por uma margem larga.**

**Uma luta dura `3,3` rodadas.** Gastar uma inteira deixa `2,3` com a barreira de pé, que são `70%` da luta. **E o câmbio fica a favor de quem levanta: uma rodada sua no nível 30 vale `108` de dano, e você a troca por uma barreira que absorve `200`.** *Quase o dobro.*

**O que gateia é levantar custar mais do que a luta inteira dura: `1 minuto`, que são dez rodadas contra `3,3`.**

> **E ele resolve de graça o problema multi-mestre que a alternativa criaria.** *Uma regra do tipo "não dá para levantar em combate" obriga sete mesas a decidirem o que é "estar em combate".* **Dez rodadas contra três e pouco não pede julgamento de ninguém.**
>
> *E o número já tinha casa: `1 minuto` é a duração que o manual usa na Melhoria `Anteparo`.*

### Adicionado — as duas, com número

> **`Barreira Simples` · sem gate.** *Um minuto para levantar.* Um domo de **raio `6 m`**, ancorado no lugar, que **bloqueia passagem e linha de efeito nos dois sentidos**. **`5 × refino` de vida**, e cai quando você fica `Inconsciente`.

> **`Cortina` · exige a `Barreira Simples`.** *Um minuto para levantar.* Cobre **um lugar** — um prédio, uma escola, um quarteirão — e **esconde o que está dentro de quem não é feiticeiro**. **Uma condição sobre quem atravessa.** **`20 × refino` de vida**, e cai quando você fica `Inconsciente`.

**A vida da Barreira fica ABAIXO da maior parede que um feitiço monta, e de propósito.** *O `Anteparo` do manual dá `10 × Classe` — `70` no Classe 7.* **`5 × refino` dá `50` no teto.** *Aquela custa pontos de montagem e sai numa ação; esta custa um marco e um minuto.* **A que sai rápido pode ser maior; a que é permanente na ficha não pode.**

**E o "cai quando você fica `Inconsciente`" é da obra, e encaixa no que a v0.88 acabou de renomear:** *"a barrier can be taken down when the sorcerer who created it is taken out"*.

**A condição da Cortina fala de QUEM ATRAVESSA e de mais nada** — barrar uma pessoa, deixar entrar só quem tem energia amaldiçoada, impedir quem está dentro de sair. *Não pode causar dano, não pode mover a cortina, não pode dar bônus.* **O exemplar da obra é o feiticeiro que levantou uma que deixava outros feiticeiros passarem e barrava só o Gojo.**

> **O tamanho da Cortina não tem metro, e isso é decisão.** *Ela é a única coisa do sistema cujo tamanho **nunca entra numa rolagem**.* **Está escrito na peça justamente para ninguém tentar usá-la como medida de combate.**

### Decidido — o QUINTO formato de gate, e ele foi recusado uma versão antes

***Decisão do Mizuki: a `Cortina` não tem gate de refino nem de nível. O requisito é ter a `Barreira Simples`*** — *"só isso já força a gastar dois marcos aqui"*.

**A v0.90 recusou exatamente este formato para o kokusen, então a diferença precisou ser escrita.**

| | por que |
|---|---|
| **kokusen — recusado** | as três são **alternativas**, cada uma serve sozinha. O requisito obrigaria a comprar a de antes só para chegar na de depois: **pedágio** |
| **`Cortina` — aceito** | ela é a `Barreira Simples` maior. A obra diz isso: barreira é o básico, cortina exige habilidade que muitos feiticeiros poderosos não têm: **escada** |

**A regra ficou escrita: a aptidão exigida tem de ser a mesma coisa em tamanho menor, e tem de servir sozinha.**

> ***E o motivo de escrever em vez de só usar é uma pergunta dele mesmo, da v0.65:*** *"por que não dá para pegar a de baixo em vez da de cima?"* **Aquilo derrubou uma mecânica inteira, e o defeito não era a dependência — era ninguém ter escrito que ela podia existir.**

**E ele é o único dos cinco formatos que cobra MARCO.** *Nível o tempo paga; refino a linha passiva do marco paga sozinha — `refino 4` chega no nível 14 até para quem nunca escolhe Refino; Origem a criação paga uma vez.* **Este gasta um marco antes de a aptidão gateada abrir.**

| rota | a `Barreira Simples` abre | a `Cortina` abre |
|---|---|---|
| sempre Refino | nível 6 | **nível 10** |
| meio a meio | nível 10 | **nível 22** |
| sempre Corpo · sempre Leque | nunca | **nunca** |

*Que quem nunca escolhe Refino duas vezes não levante Cortina também é da obra: as condições delas chegam a ser encomendadas a quem sabe fazer.*

### Adicionado — a checagem 5.3, e a 4i do `conferir-manual.py`

**A 5.3 guarda o relógio:** levantar tem de custar mais do que uma luta dura. *Ela lê as dez rodadas da peça 11 e a duração da luta da peça 1, e imprime o que cada barreira valeria **se coubesse** — que é o limite de design, declarado à parte da regra aplicada.* **E ela confere que a `Barreira Simples` fica abaixo da parede do manual, e que o quinto formato de gate está declarado na seção 5.**

> **⚠ E o extrator de gate tinha um buraco que o formato novo abriu.** *A checagem da v0.90 compara o gate do título com o do catálogo lendo tokens — `refino N`, `nível N`, `Classe N`.* **`exige a Barreira Simples` não produzia token nenhum dos dois lados, então a comparação passava TRIVIALMENTE.** *Um formato de gate inteiro sem ninguém conferindo as duas cópias dele.* **Corrigido, e a guarda de contagem subiu de onze para treze entradas.**

**A 4i fecha a cópia nova:** a peça 11 preça a `Barreira Simples` contra o `Anteparo` do manual, e essa frase virou a segunda cópia do `10 × Classe`. *Agora existe quem compare com o `.docx`.*

### As sete perturbações, em cópia isolada

| perturbação | esperado | deu |
|---|---|---|
| **o gate da `Cortina` diverge entre o título e o catálogo** | acende | acende |
| levantar vira duas rodadas em vez de dez | acende | acende |
| a `Barreira Simples` passa a parede do manual (`15 × refino`) | acende | acende |
| **a declaração do quinto formato some da seção 5** | acende | acende |
| **contra-teste:** a `Cortina` voltando a um gate de refino nos dois lados | verde | verde |
| **o `Anteparo` do manual divergindo da cópia da peça 11** | acende | acende |
| **contra-teste (da v0.89, rodado de novo):** a escada desmembrada | verde | verde |

### Em aberto

- **Sobra UMA aptidão sem número: a `Aptidão Própria`.** *E ela falta por régua e não por conteúdo — o `Efeito Próprio` do manual pergunta "em quantas cenas por arco isso importa?", e o projeto não sabe responder.*
- **Duas entregas têm nome em minúscula** — o `carregar` do `Yumi` e o `acelerar` da `Torrente`.
- **A terceira taxa sem medida do `Batedor`:** em quantas rodadas o atirador fica parado. *Ela sozinha decide `2,12` fatias.*
- **Cobertura não existe como regra**, e os metros de cada arma de projétil também não.
- **As três Trilhas do Evocador continuam paradas.**
- As de sempre: o `.pdf` do manual na v7.4 contra a v7.8 do `.docx`, as vagas de `Desliga`, a Cicatriz, o clash, a tabela de inimigo parada e o **nome do sistema**.

---

## [0.90] — 2026-08-17

**A terceira de kokusen ganhou nome e gate, e virou a `Kokusen Constante`.** *Ela era contada entre as onze fechadas com o gate escrito como **a definir** e sem nome nenhum — a peça a chamava de "(a terceira de kokusen)".* **Fechar ela levou o catálogo de nove entradas escritas com número para dez, que é exatamente o que a rota pura de Refino passou a pedir na v0.89.** Continuam dezessete peças e dezessete validadores.

### ⚠ Achado — ninguém tinha escrito se as três de kokusen empilham

**Procurado nas dezessete peças e nos três desenhos: zero ocorrências.** *É o mesmo formato do buraco do `Mirar` — entrega escrita, interação não —, só que desta vez apareceu antes de alguém sentar na mesa.*

**E a resposta decidia se a entrada existe.** Rodada no refino 10:

| a ficha tem | chance no d100 | dano por rodada |
|---|---|---|
| só o `Kokusen` | 20% | `+1,82%` |
| `Kokusen` + `Melhorado` | 36% | `+3,27%` |
| `Kokusen` + a terceira | 30% | `+2,70%` |
| **as três** | **51%** | **`+4,64%`** |

**Sem empilhar, a terceira é 17% pior que a `Melhorado` pelo mesmo preço de um marco.** *Entrada morta ocupando vaga no catálogo.*

### Decidido — as três empilham, e a ordem está escrita

***Decisão do Mizuki.*** **A `Kokusen Constante` sobe a base para `3 × refino`, e a vantagem da `Kokusen Melhorado` rola em cima dela.**

> **E nenhuma exige a outra.** *Os quatro formatos de gate da peça 11 §5 gateiam por nível, refino, os dois ou Origem — e nenhum deles é "ter pego a de antes".* **Criar esse quinto formato foi recusado:** foi uma pergunta de leitor do próprio Mizuki, na v0.65, que derrubou uma mecânica inteira exatamente por deixar uma entrega depender de outra sem ninguém ter escrito que podia.

**Sozinha, a `Constante` perde para a `Melhorado` em todo refino, e isso fica declarado.** *A conta é de forma:* vantagem numa chance `p` dá `2p − p²`, e isso ganha de `1,5p` enquanto `p` estiver abaixo de `50%`. **O teto do kokusen é `20%`, então a `Melhorado` ganha sempre.**

### Decidido — o gate é `refino 5`, sem gate de nível, e ele é derivado

| gate | especialista | meio a meio | generalista |
|---|---|---|---|
| **`Kokusen Constante`** — refino 5 | **nível 10** | nível 14 | nível 18 |
| `Kokusen Melhorado` — refino 5 **e nível 14** | nível 14 | nível 14 | nível 18 |

**São quatro níveis em que a `Constante` é a única das duas disponíveis, e eles vão inteiros para quem sempre escolhe Refino.** *Sem isso, ela seria uma entrada que nunca compensa escolher: quem pode pegar ela já pode pegar a `Melhorado`, que é melhor.* **É a mesma folga do lado certo que o gate duplo da `Melhorado` tem, virada para a outra ponta da campanha.**

*O nome saiu de três candidatos que passaram na triagem.* **`Pleno` foi recusado FORA dela, tendo saído `LIVRE`:** ele entra no campo de `Liberação Máxima` e `Técnica Máxima`, que já ocupam o *"no máximo"* no manual. *Colisão de sentido continua sendo o que a triagem não pega.*

### ⚠ Corrigido — a trava do kokusen media a ENTRADA, e a peça fala da FICHA

**O contrato 4 exigia que o kokusen ficasse abaixo de um quarto do que um ponto de atributo compra — medindo só a entrada base, em `0,18×`.** *Com as três empilhadas a ficha chega a `+4,64%` de dano por rodada, que é `0,46×`.* **A trava velha não veria.**

**A comparação certa é POR MARCO, e não no total:** a pilha inteira custa **três** marcos, e três marcos de `Corpo` compram `+3` de atributo.

| a ficha tem | dano por rodada | marcos | por marco |
|---|---|---|---|
| só o `Kokusen` | `+1,82%` | 1 | `0,18×` |
| `Kokusen` + `Melhorado` | `+3,27%` | 2 | `0,16×` |
| **as três** | `+4,64%` | **3** | **`0,15×`** |

**Os mesmos três marcos em `Corpo` comprariam `+30%` — `6,5×` mais.** *Continua sendo escolha pelo grito, e não pela planilha, que é o que o texto sempre disse.*

> **Medir a pilha contra UM ponto de atributo seria comparar três marcos com um** — a lição nº 7 por outra porta. *E medir só a entrada é a lição nº 8: a trava se media contra o pedaço que ela mesma escolheu olhar.*

### ⚠ Corrigido — a checagem do gate duplicado só olhava UMA das catorze entradas

**O gate de cada aptidão mora em dois lugares:** o título da seção 6 ou 6.5, e a linha da tabela do catálogo da seção 10. **Catorze entradas, catorze cópias.**

**A checagem que comparava as duas estava escrita no braço, para a `Energia Reversa` e só para ela.** *Perturbando o gate da `Kokusen Constante` no catálogo — `refino 5` virando `refino 7` —, o validador saía **verde**.* **Treze das catorze não tinham ninguém comparando.**

**Generalizada: agora ela varre as onze entradas que têm seção própria.** *A direção é de mão única, no molde da checagem 9 do `conferir-catalogo.py`:* o título é o dono, e a tabela pode dizer **mais** — a `Aptidão Própria` carrega *"uma vez na ficha"*, que não é gate. **Ela não pode dizer menos nem outro.** *E há guarda de contagem: se o número de pares cair de onze, ela acusa em vez de conferir menos em silêncio.*

### As sete perturbações, em cópia isolada

| perturbação | esperado | deu |
|---|---|---|
| **a frase do empilhamento some da peça** | acende | acende |
| a `Constante` sobe a base para `6 ×` em vez de `3 ×` | acende | acende |
| **contra-teste:** `5 ×`, logo abaixo da trava | verde | verde |
| **o gate da `Constante` diverge no catálogo** | acende | acende |
| **a regressão velha: o gate da `Energia Reversa` diverge** | acende | acende |
| **contra-teste:** a tabela dizendo MAIS que o título | verde | verde |
| **contra-teste (da v0.89, rodado de novo):** a escada desmembrada | verde | verde |

> **A terceira encosta na trava de propósito.** *A `5 ×` a pilha rende `2,25%` por marco e passa; a `6 ×` rende `2,52%` e reprova, contra um limite de `2,50%`.* **A linha está entre as duas, e agora existe quem a defenda.**

### Em aberto

- **`Barreira Simples` e `Cortina` continuam sem número.** *Com a `Constante` fechada, o catálogo tem dez entradas escritas e a rota pura de Refino pede exatamente dez — **fecha sem folga nenhuma** até as duas entrarem.* **É a próxima coisa da fila, por escolha do Mizuki.**
- **Duas entregas têm nome em minúscula** — o `carregar` do `Yumi` e o `acelerar` da `Torrente`.
- **A terceira taxa sem medida do `Batedor`:** em quantas rodadas o atirador fica parado. *Ela sozinha decide `2,12` fatias.*
- **Cobertura não existe como regra**, e os metros de cada arma de projétil também não.
- **As três Trilhas do Evocador continuam paradas.**
- As de sempre: o `.pdf` do manual na v7.4 contra a v7.8 do `.docx`, as vagas de `Desliga`, a Cicatriz, o clash, a tabela de inimigo parada e o **nome do sistema**.

---

## [0.89] — 2026-08-17

**A troca do marco fechou, e ela era o único problema de design que tinha sobrado.** *A escolha de `Refino` promete **"mais um de refino, e uma aptidão"** e entregava só a aptidão em três dos sete marcos, porque o teto de refino já tinha sido alcançado.* **Nenhum validador via, e a causa de não ver é a lição nº 3 acontecendo dentro de um deles.** Continuam dezessete peças e dezessete validadores.

### ⚠⚠ Medido — a linha de graça do marco entrega 8 dos 10 de refino, sozinha

**Sete marcos a `+1`, mais o refino 1 com que toda ficha começa.** *Quem **nunca** escolhe `Refino` termina a campanha com refino 8.*

**Então a metade *"mais um de refino"* da escolha só tem `2` pontos de espaço para caber, na campanha inteira** — e quem escolhe `Refino` nos sete marcos pagaria `15` e para em `10`. **Cinco pontos jogados fora.**

| marco | refino antes | depois | o que a ESCOLHA comprou |
|---|---|---|---|
| 6 · 10 · 14 · 18 | 1 → 7 | 3 → 9 | `+1` de refino e uma aptidão |
| **22** | 9 | **10** | o refino da escolha **cai no teto** |
| **26** · **30** | 10 | **10** | idem |

**E os outros dois eixos não desperdiçam nada.** *O `Corpo` ganha `14` pontos contra um teto somado de `30` nos cinco atributos; o teto de Passivas do `Leque` sobe uma vaga por escolha, junto com a rota; feitiço não tem teto.* **O refino era o único dos três cujo teto não acompanha quem o compra.**

### Decidido — no teto, a escolha de `Refino` leva DUAS aptidões

***Decisão do Mizuki:*** *"quando chegar no cap, se escolher aptidão recebe duas. Eu vou aumentar a lista de aptidões futuramente."*

**Não é aptidão de graça: é a segunda metade da escolha trocando de moeda quando a primeira acaba.** *A rota pura passa de `7` para `10` aptidões.*

> **A forma da comparação não muda, e é isso que fecha o argumento.** *Cortando o par aptidão/Passiva dos dois lados — eles vivem na mesma escada de Classe Passiva —, o marco sempre compara `+1` atributo contra **alguma coisa** contra `+1` feitiço.* **Antes do teto essa alguma coisa é `+1` de refino; a partir dele é uma aptidão a mais.** *A escolha nunca fica com uma das mãos vazia.*

> **⚠ E isto NÃO tem régua, declarado.** *"Uma aptidão a mais" não converte em fatia, e foi ela que matou o `Repertório` na v0.81.* **A diferença é quem recebe:** lá a Trilha era vendida para qualquer ficha, e o número tinha de valer para quem nunca pega aptidão nenhuma. **Aqui quem leva a segunda é, por definição, quem já escolheu esse eixo cinco vezes.**

**A rota pura passa a precisar de `10` aptidões, e o catálogo tem `12` que custam marco.** *Cabe, com duas de folga.* **Mas só nove estão escritas com número** — `Barreira Simples`, `Cortina` e a terceira de kokusen continuam *a definir*. *É a primeira coisa que aperta se a lista não crescer, e o Mizuki já declarou que vai crescer.*

### ⚠ As duas alternativas foram medidas e reprovaram, e a conta ficou

**Subir o teto de refino de `10` para `15`** faria a escolha caber inteira. *Reprovou com número: perturbando o teto no validador, **dois contratos acendem na hora** — a proteção de `cobrir-se de energia` passa a crescer `+33` na campanha contra `+3` de um atributo, e o kokusen chega a `9,1%` de dano por rodada, acima de um quinto do que um ponto de atributo compra.* **E há `31` fórmulas usando refino como variável em sete arquivos**, todas calibradas contra o teto `10`.

**Baixar o refino passivo** daria espaço à escolha sem mexer no teto. *Reprovou por efeito colateral: a tabela de gates do §5 é publicada — `Classe Passiva 2` no refino 4, `Classe Passiva 3` no refino 7 —, e ela se move inteira. E a promessa de que `cobrir-se` e `canalizar` crescem sozinhas até 8 cai para 5.*

### Adicionado — a checagem 5.2, e ela é a segunda metade da 5 por outro eixo

**A checagem 5 mede o FIM da campanha.** *Nos totais a rota de `Refino` liderava o eixo do refino com `10` contra `8` e parecia bem — com o meio quebrado o tempo todo.* **A 5.2 mede MARCO A MARCO:** em cada um dos sete, para cada uma das quatro rotas, o que cada opção daria àquele jogador naquele momento.

> **As componentes são QUATRO e não cinco, e a fusão é a afirmação da própria peça 11:** aptidão e Passiva vivem na **mesma** escada de Classe Passiva.
>
> ***Contra-teste que prova que isso é o que segura tudo:*** *rodando a regressão com as duas em componentes SEPARADAS, ela sai **verde**.* **Separadas, `1 aptidão` e `1 Passiva + 1 feitiço` nunca se comparam, e a dominância nunca aparece — que é exatamente por que ninguém viu isto em dezessete versões.**

### ⚠ Corrigido — o Classe 0 fantasma sobreviveu num validador, e sobreviveu por ser só impresso

**O `conferir-aptidoes.py` carregava `CLASSE_0 = 4.5`.** *É o número que a v0.80 matou em todo o resto do projeto: ele não aparece em lugar nenhum do manual.* **Ele sobreviveu nove versões porque só era IMPRESSO, nunca conferido** — a coluna *"Classe 0"* do relatório de `Projetar`.

| nível | a coluna dizia | é |
|---|---|---|
| 2 | `35%` da Rotina | **`69%`** |
| 30 | `4%` | **`25%`** |

**Agora ele é lido da tabela do manual** — `2d8 · 3d8 · 4d8 · 5d8 · 6d8` por faixa —, como cópia vigiada, no mesmo molde da `Rotina`. ***Display errado ensina número errado do mesmo jeito que checagem errada.***

### As seis perturbações, em cópia isolada

**A base passou na cópia antes de cada uma, e o `diff` foi conferido em todas.**

| perturbação | esperado | deu |
|---|---|---|
| **a regressão: no teto, `Refino` volta a dar uma aptidão só** | acende | acende |
| **contra-teste:** no teto ele daria três | verde | verde |
| a regra some da peça 11 | acende | acende |
| **contra-teste:** teto de refino fora de alcance — a 5.2 fica quieta | 0 dominâncias | 0 |
| **contra-teste: a regressão com a escada desmembrada** | **verde** | **verde** |
| teto de refino em `99` | acende (contratos 2 e 4) | acende |

> **A quinta é a que importa, e ela é a prova do método.** *A 5.2 não é uma checagem a mais: ela é a mesma pergunta da 5, feita num eixo em que a resposta muda.* **A sexta rendeu de graça a conta que reprovou a alternativa de subir o teto.**

### Em aberto

- **O catálogo de aptidões precisa crescer.** *A rota pura pede `10` e só `9` estão escritas com número.* **Declarado pelo Mizuki nesta versão.**
- **A escada de Classe Passiva da camada de vínculo continua sem preço** — a grade de `16` células do `RASCUNHO-trilhas.md`, do Evocador parado. *A `§4` da peça 11 é outra coisa: ela declara de propósito que **não mede quanto, mede o quê**.*
- **Duas entregas têm nome em minúscula** — o `carregar` do `Yumi` e o `acelerar` da `Torrente`.
- **A terceira taxa sem medida do `Batedor`:** em quantas rodadas o atirador fica parado. *Ela sozinha decide `2,12` fatias.*
- **Cobertura não existe como regra**, e os metros de cada arma de projétil também não.
- As de sempre: as quatro aptidões abertas, o `.pdf` do manual na v7.4 contra a v7.8 do `.docx`, as vagas de `Desliga`, a Cicatriz, o clash, a tabela de inimigo parada e o **nome do sistema**.

---

## [0.88] — 2026-08-17

**Quatro dívidas antigas fecharam numa versão só, e a mais velha delas não era o que estava escrito.** *A troca de `Caído` por `Inconsciente` estava marcada desde a v0.82 como colisão entre o estado de 0 de vida e a condição de quem foi derrubado — e a condição de derrubado **já tinha nome no manual, e não era `Caído`**.* **Achar isso destampou um buraco de validador que estava aberto desde sempre.** Continuam dezessete peças e dezessete validadores.

### ⚠⚠ Achado — a triagem era cega para as doze condições do manual, e ONZE saíam `LIVRE`

**O manual tem doze condições**, em duas linhas de prosa da tabela de Melhorias: `Derrubado` · `Lento` · `Cego` · `Agarrado` · `Surdo` · `Desarmado` · `Calado` nas Menores, e `Atordoado` · `Paralisado` · `Amedrontado` · `Enfeitiçado` · `Incapacitado` nas Maiores.

**Nenhuma delas entrava no vocabulário do `conferir-nomes.py`.** *A extração lê a primeira coluna de tabelas com cabeçalho conhecido — `Família`, `Forma`, `Melhoria`, `Restrição`, `Passiva` —, e as condições não têm coluna: elas moram dentro da frase `"Aplica uma: …"` de uma célula.*

| candidato | a triagem dizia | é |
|---|---|---|
| `Derrubado` · `Cego` · `Agarrado` · `Surdo` · `Desarmado` · `Calado` | **LIVRE** | Condição Menor |
| `Atordoado` · `Paralisado` · `Amedrontado` · `Enfeitiçado` · `Incapacitado` | **LIVRE** | Condição Maior |
| `Lento` | OCUPADO | **e por acidente** — ele também é Restrição |

> **O exemplar mais constrangedor é o `Incapacitado`:** ele saía `LIVRE` enquanto a peça 1 §5.5 gastava um bullet inteiro explicando que `Incapacitado` **é condição nomeada do manual**. *O projeto sabia, escrito, o que o validador não sabia.*

**Conserto: as doze passam a ser extraídas do `.docx`**, pela frase que as introduz, com guarda de contagem — se a extração devolver diferente de doze, o validador falha em vez de voltar a ficar cego em silêncio. **Nada foi copiado para dentro do validador.**

### ⚠ Corrigido — o `Abalo` das Manhas rebatizava uma condição que o manual já tinha, e isso era REGRESSÃO

**A v0.74 já tinha achado e fechado exatamente essa colisão.** *O `Punho` derrubava alvos com a palavra "cai", e o registro daquela versão diz: **"o manual já tem a condição `Derrubado`, com tier de preço e cinco feitiços prontos usando ela. Trocada a palavra, a colisão sumiu sem custo."***

**Oito versões depois ela voltou por outra porta.** *A v0.82 escreveu o `Abalo` e chamou a mesma condição de `Caído`, que era o nome da máquina de estado de 0 de vida da peça 1 — e marcou a colisão como dívida em vez de perceber que a palavra certa já existia.*

**Agora o `Abalo` aplica o `Derrubado`.** *Uma linha de tabela, uma linha de decisão e a nota da colisão, todas no `DESENHO-manhas.md`.* **Nenhum número se moveu:** a Manha continua valendo `1,00` fatia com trava de `60%`.

> **E o `Punho` estava certo o tempo todo.** *Fui conferir uma por uma as menções a `Caído` antes de trocar qualquer coisa, e o nível 11 do `Punho` já dizia `Derrubado`; o nível 27 do `Muro` diz "caído" em minúscula, em prosa, e não é termo.* **O aviso que dizia "cuidado, nem toda menção é o estado de 0 de vida" descrevia um perigo que não existia mais** — e um aviso com o motivo errado ensina a procurar o defeito no lugar em que ele não está.

### Alterado — o estado de 0 de vida virou `Inconsciente`, três versões depois de decidido

***Decisão do Mizuki, registrada na v0.82 e aplicada só agora.*** **Onze lugares**, e nenhum deles é número:

| onde | o que era |
|---|---|
| **peça 1** | o título da seção 5.5, e a nota que separa o estado da condição `Incapacitado` |
| **peça 13** | a frase do `Corpo Emprestado`, que cita aquela seção |
| **peça 15** | as duas linhas de *"a invocação some no zero, sem estado intermediário"* |
| **`ESTADO-ATUAL`** | a tabela de onde cada coisa mora, e o título da seção histórica |
| **`conferir-atributos.py`** | quatro rótulos da checagem 9 |

**A peça 1 ganhou um bullet a mais, e ele é o motivo de a troca ter existido:** *`Inconsciente` também não é `Derrubado` — quem está `Derrubado` está no chão e continua com vida; quem está `Inconsciente` chegou a zero. A Manha `Abalo` aplica o `Derrubado`, e nunca este estado.*

> **⚠ A ressalva que fica declarada: o `Insistir` não é inconsciente.** *No `Insistir` você fica de pé a 0 de vida e age normalmente, e só desaba na quarta rodada.* **O nome cobre o ramo do `Aguentar` e o fim dos dois, e não cobre o meio do `Insistir`.** *Levado ao Mizuki com a alternativa `Queda`, que é a palavra que a própria regra já usa três vezes; **ele manteve `Inconsciente`.*** *`Caído` entrou na lista de termos mortos e a triagem passa a devolver ele como `MORTO`.*

### Removido — o `Repertório` saiu da peça 6, sete versões depois de morrer

**A peça 6 §2 ainda listava a Trilha do Emanador que a v0.81 abandonou**, e a palavra `Explosivo` não aparecia naquela peça uma vez sequer. *Um leitor que abrisse a peça de Caminhos escolheria uma Trilha que não existe.*

**Ele sobreviveu em sete lugares, e não em três:**

| onde | por que morde |
|---|---|
| **peça 6 §2** | é a peça que o jogador lê |
| **`gerador-ficha/dados.js`** | **é a ficha.** Ela vira personagem em sete mesas ao mesmo tempo |
| `conferir-nomes.py` e `conferir-pericias.py` | as duas listas de Trilha dos validadores |
| `RASCUNHO-trilhas.md` | a tabela dos quinze e a fila de trabalho |
| **peça 5** | a nota histórica que explica um rename **dava o motivo errado**: *"`Repertório` já é a Trilha do Emanador"* |
| `DESENHO-trilhas.md` | **três pendências escritas como abertas** — *"falta o `Repertório`"* — de uma Trilha morta |

> **E a consequência boa aconteceu: o nome ficou `LIVRE` de novo.** *Ele estava na lista `TRILHAS` do `conferir-nomes.py`, então a triagem devolvia `OCUPADO`.* **A ficção dele é boa e pode voltar num Caminho que tenha coluna para ela** — e `Repertório` **não** entrou na lista de mortos, de propósito.

### Corrigido — a peça 6 publicava o calendário de Caminho aposentado como fato fechado

**O degrau de Caminho é `2 · 7 · 15 · 30` desde a v0.70**, e o dono é o `DESENHO-caminhos.md`. **A peça 6 §9 dizia `7 · 15 · 23 · 29`, na linha que abre com *"Fechada na v0.55 e na v0.60"*.** *Dezoito versões.*

**E o segundo lugar não era erro, e por isso não foi apagado.** *O §3.1 conta o que a Q2 de Trilhas decidiu na época, dentro de bloco de citação — aquilo é registro legítimo.* **Ganhou uma linha dizendo que o calendário foi superado na v0.70, e quem é o dono do de hoje.** *Apagar registro histórico é como o projeto perde o porquê.*

### Alterado — `Quick Draw` virou `Descarga`, e o sistema não tem mais nome em inglês

***Decisão do Mizuki entre quatro candidatos que passaram na triagem*** — `Saque`, `Tambor`, `Fuzilada` e `Descarga`. *Dois morreram na triagem antes de chegarem a ele: **`Rajada` é Melhoria no manual** e `Estopim` já é o nível 11 do `Explosivo`.* **E um morreu por sentido depois de sair `LIVRE`: `Pente`, porque a propriedade `Munição` da peça 14 já fala do pente em prosa.**

**Nove ocorrências** — sete no `DESENHO-trilhas.md` e duas na peça 17. *A escada da rota `Arma de Fogo` fica `Ferrolho` · `Mirar` · `Descarga` · `Dobro`.* **Nenhum número se moveu:** continua valendo `1,17` fatia com o Rifle de Precisão e `1,89` com a Metralhadora Pesada.

### Adicionado — a checagem 10 do `conferir-catalogo.py`, em dois eixos

**10a: toda cópia viva do calendário de Caminho bate com o `DESENHO-caminhos.md`.** **10b: o calendário aposentado não aparece fora de nota histórica.**

> **São dois eixos de propósito, e a regra é a mesma da quinta contra a sexta.** *Reescrever a frase sem o número apaga a 10a e deixa a 10b de pé; trocar o número sem mexer na frase acende a 10a.* **E a 10a tem guarda de contagem:** ela sabe que existem três cópias vivas e falha se achar menos, porque uma checagem que para de conferir em silêncio é a lição nº 8 por outra porta.

**A triagem ganhou um veredito novo: `MORTO`.** *Ele não mata o candidato — o projeto reaproveita nome de propósito, e o `Repertório` voltou para a prateleira nesta mesma versão.* **O que ele impede é reaproveitar sem saber que está reaproveitando.**

### As dez perturbações, em cópia isolada

**A base passou na cópia antes de cada uma, e o `diff` foi conferido em todas** — o arnês recusa resultado de `sed` que não bateu.

| perturbação | esperado | deu |
|---|---|---|
| **a regressão da peça 6: o calendário velho de volta** | acende | acende |
| **a regressão da peça 17: o calendário velho de volta** | acende | acende |
| a frase da peça 17 perde o número | acende | acende |
| **contra-teste:** mexer noutro calendário de quatro números (o vão) | verde | verde |
| **contra-teste: mover o calendário NO DONO e nas três cópias** | **verde** | **verde** |
| mover o dono e só duas das três cópias | acende | acende |
| **uma entrega batizada com nome de Condição do manual** | acende | acende |
| **contra-teste:** a mesma entrega com um nome de fato livre | verde | verde |
| **a regressão do `Abalo`: `Caído` de volta na tabela** | acende | acende |
| **contra-teste:** citar `Caído` numa nota que diz quando ele morreu | verde | verde |

> **A quinta é a que importa.** *Mover o calendário no dono e nas três cópias sai **verde** — é a prova de que a 10a lê do `DESENHO-caminhos.md` e não de uma constante escrita dentro dela.* **Sem esse contra-teste, a checagem poderia estar se medindo contra si mesma**, que é o erro que já apareceu três vezes em três versões.

### Medido — o defeito de mount não reproduziu

**Nesta versão a pasta foi alcançada pela ponte do desktop, e todo arquivo abriu** — inclusive a peça 17, que a v0.87 não conseguia ler, e o `.docx` do manual. **Os vinte validadores rodaram de verdade, com `PULADA=0`.**

> *O aviso do `README` sobre o mount **não foi apagado**, porque a via de acesso desta versão pode não ser a mesma que ele descreve.* **Fica marcado para apagar na primeira versão que confirmar o mesmo resultado por outra via** — aviso que parou de reproduzir é dívida, e um que dá o motivo errado envelhece pior que nenhum.

### Em aberto

- **A troca do marco continua sendo o único problema de design em pé.** *Do nível 22 em diante o refino topa em `10` e a escolha "refino e uma aptidão" vira só a aptidão, enquanto Corpo e Leque valem cheio — três marcos com um dos três eixos pela metade.*
- **A escada de Classe Passiva nunca teve os próprios exemplos preçados**, e dois dos sete não sobrevivem.
- **Duas entregas têm nome em minúscula** — o `carregar` do `Yumi` e o `acelerar` da `Torrente`.
- **A terceira taxa sem medida do `Batedor`:** em quantas rodadas o atirador fica parado. *Ela sozinha decide `2,12` fatias.*
- **A lista `NOMES_SEM_CATALOGO` continua com uma entrada, e ela é dívida.**
- **Cobertura não existe como regra**, e os metros de cada arma de projétil também não.
- As de sempre: as quatro aptidões abertas, o `.pdf` do manual na v7.4 contra a v7.8 do `.docx`, as vagas de `Desliga`, a Cicatriz, o clash, a tabela de inimigo parada e o **nome do sistema**.

---

## [0.87] — 2026-08-17

**As 21 entregas sem nome fecharam, e os dois validadores que deixaram passar os últimos defeitos foram consertados.** *De `89` entradas, `88` têm nome — a única sem é a vaga do `Arremate`, que é deliberada.* Continuam dezessete peças e dezessete validadores.

### Adicionado — os 21 nomes, em quatro escadas

| Trilha | 2 | 11 | 19 | 27 |
|---|---|---|---|---|
| **`Estocada`** | `Compasso` | `Traçado` | `Bote` | `Ferrão` |
| **`Muro`** | `Alicerce` | `Aterro` | `Escora` | `Cúpula` |
| **`Punho`** | `Engate` | `Encontrão` | `Tropel` | `Arranco` |
| **`Brasa`** | `Fagulha` | `Braseiro` | `Labareda` | `Fornalha` |
| **`Torrente`** | `acelerar` | `Vazão` | `Cheia` | `Transbordo` |
| **`Batedor` · `Yumi`** | `carregar` | `Mirar` | `Pique` | `Dobro` |
| **`Batedor` · `Besta`** | `Manivela` | `Mirar` | `Repuxo` | `Dobro` |
| **`Batedor` · `Arma de Fogo`** | `Ferrolho` | `Mirar` | `Quick Draw` | `Dobro` |

**Cada escada é um campo semântico fechado, no molde da `Sutura` e do `Explosivo`:** *esgrima na `Estocada`, alvenaria no `Muro`, massa em movimento no `Punho`, fogo crescendo na `Brasa`, água subindo na `Torrente`, e mecanismo de arma no `Batedor`.*

> ***Decisão do Mizuki: o nível 27 das três rotas do `Batedor` leva UM nome só.*** *As três dizem a mesma frase, e o próprio `Mirar` já é um nome para as três.* **Nome repetido para regra idêntica é uma palavra a menos para a mesa carregar.**

**`Ponta` foi recusado FORA da triagem, tendo saído `LIVRE`:** ele aparece `10` vezes na prosa e é eco de `Ponta de Lança`, que era rótulo de rascunho de Caminho. *Colisão de sentido continua sendo o que a triagem não pega.*

### ⚠ Corrigido — o nível 19 da `Brasa` publicava `Classe 2` e cobrava `Classe 3`

| onde | o que dizia |
|---|---|
| a tabela de preço, e o argumento inteiro | `Classe 3` no nível 19, e **`Classe 4` do nível 21** |
| **o bloco de regra** | `Classe 2` |

**A escada de `Classe 3` e `Classe 4` é decisão registrada do Mizuki, com tabela de dano de `40` e `54` logo acima do bloco.** *O bloco nunca foi atualizado.* **É o segundo exemplar do defeito da `Estocada` em duas versões, o que quer dizer que ele não era caso isolado.** *Nenhum número se moveu: o preço de `0,00` a `2,36` já tinha sido calculado com a escada certa.*

### ⚠ Renomeado — `Mão Firme` colidia com uma Passiva do manual

**No manual, `Mão Firme` é Passiva de custo `1`:** *"você não perde concentração nem carga por dano de `10` ou menos"*. **Na `Torrente` ela era rerrolar dado de dano** — duas coisas sem relação nenhuma com o mesmo nome. *Virou `Cheia`.*

> **Ninguém tinha conferido esse nome porque, até esta versão, nenhuma varredura alcançava os `DESENHO-*.md`.** *Achado pelo `conferir-nomes.py` na primeira rodada depois do conserto abaixo.*

### Adicionado — a checagem 9 do `conferir-catalogo.py`

**Toda `Classe` que a linha de preço cobra tem de aparecer no bloco de regra.** *A checagem 6 pega gate contra `sempre`; esta pega VALOR contra valor, que é o que deixou a `Brasa` passar.*

> **A direção é de mão única, e de propósito.** *Comparar os dois lados como conjunto dava **sete** vermelhos falsos: o bloco cita `Classe` em exemplo de custo o tempo todo — "num Classe 7 são 7 PE" — e exemplo não é promessa.* **Preço → bloco pega o defeito e não pega o exemplo.**

### Alterado — o `conferir-nomes.py` passou a enxergar os desenhos

**Ele lê os nomes de entrega da própria peça 17**, então não existe segunda lista: entrada nova no índice entra na triagem na mesma hora. *Passou de `34` para `61` nomes conhecidos, e os `DESENHO-*.md` da raiz entraram na varredura de arquivos vivos.*

**E `Rescaldo` ganhou casa.** *Ele saía `LIVRE` estando batizado — é a queima de técnica quando o domínio acaba, escrita no `ESTADO-ATUAL` e no rascunho de clash.* **Entrou numa lista curta de `NOMES_SEM_CATALOGO`, que é DÍVIDA declarada e não inventário:** cada entrada ali é um nome que vive solto na prosa e devia ter dono.

> **⚠ E o conserto criou um defeito que precisou de conserto: `Nó` batia com a preposição *"no"*.** *A comparação tirava acento dos dois lados, então `Nó` virava `no` e casava com meio repositório — **49 avisos numa rodada só**, quase todos disso.* **Agora nome com acento se compara com acento, e sobraram `18` avisos legítimos.**

**Quatro perturbações conferidas em cópia isolada**, com a base passando antes e o `diff` conferido em cada uma:

| perturbação | esperado | deu |
|---|---|---|
| **a regressão da `Brasa`: `Classe 2` de volta no bloco** | acende | acende |
| **contra-teste:** o bloco citando `Classe 7` num exemplo a mais | verde | verde |
| **a regressão do `Mão Firme`: pôr o nome de volta no índice** | acende | acende |
| **contra-teste:** renomear para um nome livre | verde | verde |

### Decidido — o `Mirar` fica com o nome

***Decisão do Mizuki:*** *"não tem problema com o nome, mantém."* **A triagem devolve ele como `fraco` — está a uma letra de `Mira`, que é Família no manual —, e a colisão fica aceita e declarada**, no molde do escudo `Médio` da peça 14, que carrega duas.

### Em aberto

- **`Quick Draw` continua sendo o único nome em inglês do sistema.**
- **Duas entregas têm nome em minúscula** — o `carregar` do `Yumi` e o `acelerar` da `Torrente`.
- **O `conferir-nomes.py` agora leva `21` segundos**, e o `subir.sh` roda ele em todo commit.
- **A lista `NOMES_SEM_CATALOGO` tem uma entrada, e ela é dívida.** *`Rescaldo` devia ter catálogo, não lista.*
- **Cobertura não existe como regra.**
- As de sempre: as quatro aptidões abertas, a troca do marco, os metros das armas de projétil, `Caído` para `Inconsciente`, o `Repertório` na peça 6 §2, o calendário velho no §9 dela, e o nome do sistema.

---

## [0.86] — 2026-08-17

**A ação `Mirar` existe.** *Ela era entregue em **seis degraus** do `Batedor` desde a v0.74 e não tinha regra escrita em lugar nenhum do repositório — treze menções no desenho, todas concedendo, nenhuma definindo.* **Quem achou foi o `conferir-catalogo.py`, que entrou na versão anterior.** Continuam dezessete peças e dezessete validadores.

### Adicionado — a regra, e ela é do Mizuki

> **`Mirar`.** *Ação Bônus.* Você firma o corpo e alinha o tiro.
> **O seu próximo ataque com arma de projétil nesta rodada é rolado com vantagem.**
> **Você só pode `Mirar` se não tiver se deslocado nesta rodada, e o `Mirar` se perde se você se deslocar.**

***Decisão do Mizuki, e o gate de movimento é dele:*** *"é uma vantagem, ao custo de uma ação bônus… coloca que não pode ter se deslocado na rodada e nem se deslocar."*

**É a forma do `Steady Aim` do Ladino do 5e**, lida na fonte junto com as três do Pathfinder 2e. *As duas formas mais comuns já estavam gastas aqui: a que conserta a penalidade de faixa de alcance é o **nível 2 das três rotas**, e a que mexe em cobertura não tem onde encostar, porque **cobertura não existe como regra** — procurada nas dezessete peças, zero ocorrência.*

### ⚠ Medido — ela estoura o degrau em `5,3×`, e o estouro FICA

***Decisão do Mizuki:*** *"você tá inflando demais essa habilidade, garanto para você, pode passar e manter como está."* **Precedente dele mesmo, com a mesma frase, na `Brasa` da v0.81.**

| a peça | vale |
|---|---|
| vantagem em **um** dos dois ataques | `+27,00` de dano na rodada |
| abrir mão do deslocamento de `9 m` | `−5,40` |
| **líquido** | **`21,60` = `4,25` fatias, num degrau de `0,80`** |

**O gate de movimento corta `20%` do preço.** *Ele não é decorativo — é um quinto —, mas vantagem é o número mais caro do sistema e um quinto não fecha a conta.*

**E a premissa de que a Ação Bônus limita sozinha não se sustenta nos documentos, que dizem o contrário em três lugares:** a peça 3 §7 chama o slot de *"o mais vazio do turno"*, o CHANGELOG da v0.83 fechou com *"duas ações bônus ainda é pouco"*, e o `ESTADO-ATUAL` tem *"alguém usa ação bônus?"* marcado para o playtest. ***O caso mais forte é a `Besta`: o nível 2 dela paga `0,89` fatia exatamente para a recarga parar de comer a Ação Bônus, e o nível 11 volta a cobrar aquele slot.***

**Nenhum número publicado se moveu.** *A discordância fica escrita, no molde do `Punho`.*

### ⚠ Declarado — três dominâncias novas sobre a `Estocada`

**Com o atirador parado em metade das rodadas, as três rotas vão de `4,52`–`4,82` para `5,95`–`6,09` contra um teto de `5,00`** — `+19%` a `+22%`, que é **exatamente o tamanho do `Punho`**, publicado em `6,09` e aceito na v0.74.

| | ação/alvo | defesa | posicionamento | total |
|---|---|---|---|---|
| `Estocada` | 5,02 | 0,00 | 0,00 | 5,02 |
| `Executor` | 2,84 | **1,84** | 0,00 | 4,68 |
| `Yumi` | 5,74 | 0,00 | 0,35 | **6,09** |
| `Besta` | 5,24 | 0,00 | **0,71** | **5,95** |
| `Arma de Fogo` | **6,00** | 0,00 | 0,00 | **6,00** |

**As três dominam a `Estocada` por `1,19×` a `1,21×`** — o mesmo tamanho da dominância `Explosivo` sobre `Torrente` que já está declarada, e dentro do filtro que reprova em `3,00×`.

> **A causa é a de sempre: falta coluna, não sobra número.** *O nível 2 da `Estocada` vale `0,00` em dano e entrega duas coisas que a matriz não tem onde olhar.*
>
> **O que a matriz continua segurando:** ninguém domina o `Executor`, que é o único com coluna de defesa, e as três rotas não se dominam entre si.

### ⚠ E entrou a TERCEIRA taxa sem medida deste bloco

*As outras duas já estavam declaradas: quantas rodadas um atirador passa na faixa longa, e quantas ele passa colado.* **Agora entra *"em quantas rodadas ele fica parado"*, e ela sozinha decide `2,12` fatias.** *A `1,00×` as três rotas vão a `8,07`–`8,21` e a dominância sobe para `1,64×`.* **É a primeira coisa a olhar na mesa, junto com o estouro.**

### Alterado — o `carregar` e o `Mirar` disputam o mesmo slot, e o `Yumi` tem exceção

*O nível 11 do `Yumi` sempre disse que o `Mirar` "pode ser usada junto do `carregar`", e a frase só significa alguma coisa agora que se sabe que os dois são Ação Bônus.* **Escrito: uma mesma Ação Bônus faz os dois, e só o `Yumi` empilha.**

### Em aberto

- **O nome `Mirar` continua devendo.** *A triagem devolve ele como `fraco`: está a uma letra de `Mira`, que é Família no manual.* **A dívida de regra fechou; a de nome não.**
- **Faltam `21` nomes de entrega**, e agora nenhum deles está bloqueado por buraco de regra.
- **`Quick Draw` é o único nome em inglês do sistema.**
- **Cobertura não existe como regra**, e isso apareceu procurando forma para o `Mirar`. *Não é urgente; fica registrado que a lacuna é real.*
- As de sempre: as quatro aptidões abertas, a troca do marco, os metros das armas de projétil, `Caído` para `Inconsciente`, o `Repertório` na peça 6 §2, o calendário velho no §9 dela, e o nome do sistema.

---

## [0.85] — 2026-08-17

**A contagem ganhou dono, e um validador do projeto passou a ler os `DESENHO-*.md` pela primeira vez.** *Aqueles três arquivos estavam fora de alcance de todo validador desde que existem, e o preço disso está medido: o nível 27 da `Estocada` passou três versões cobrando `1,33` fatia na tabela e entregando `5,31` no bloco de regra.* **Passam a ser dezessete peças e dezessete validadores.**

### Adicionado — a peça 17, e ela não escreve regra nenhuma

**Ela é um índice: quantas entradas existem, como cada uma se chama, e onde o texto dela mora.** *Só isso.* **Não guarda preço e não guarda texto de mesa** — os dois continuam sendo dos desenhos, que são os donos.

> ***Decisão do Mizuki: o índice aponta, e o texto fica onde está.*** *A alternativa era copiar o texto de mesa para dentro da peça, e ela reprova sozinha: seria a lição nº 9 cometida pelo documento escrito para impedi-la.*

### Decidido — a regra de contagem, que nunca tinha sido escrita

***Decisão do Mizuki: rota de Trilha conta como entrada própria; menu dentro de um degrau não conta.***

| o caso | conta como | por quê |
|---|---|---|
| as três rotas do `Batedor` | **12** | a rota se escolhe no nível 2 e vale a campanha. **A matriz da Vanguarda já entra com cinco linhas e não três** pelo mesmo motivo |
| a `Pegada` do `Executor` | **4** | menu de um degrau. Quem escolhe estilo continua sendo um `Executor` |
| a `Sintonia` do Evocador | **4** | mesma forma da `Pegada` — e essa a conta fechou sozinha, sem pergunta |

**Com a regra escrita, os números mudaram: `89` entradas e não `81`, e `21` nomes faltando e não `17`.** *As quatro a mais estavam escondidas dentro de uma linha só do `Batedor`.*

> **A divisão que a v0.84 publicou não reproduzia.** *Ela dizia `Estocada 4 · Batedor 8 · o resto 5`, e recontando dos arquivos sai `Muro 3 · Punho 2 · Brasa 3 · Estocada 4 · Batedor 3 · Torrente 2` — mesmo total, outra divisão, e a `Torrente` não estava na lista.* **Total que fecha por caminhos diferentes é total que ninguém está conferindo.** *A causa era a regra de contagem não existir.*

### Adicionado — o `conferir-catalogo.py`, com oito checagens e dez perturbações

**Nada de valor mora dentro dele:** os nomes saem das tabelas da peça, os textos saem dos desenhos, e as contagens saem da própria pasta.

| perturbação | esperado | deu |
|---|---|---|
| trocar o total de Trilha de `56` para `55` | acende | acende |
| quebrar só a soma por estado (`67` → `66`) | acende | acende |
| renomear o `Alicerce` no índice e não no desenho | acende | acende |
| apagar a `Fornalha` do índice | acende | acende |
| apagar o bloco de regra do `Muro` nível 2 | acende | acende |
| **a regressão da `Estocada`: pôr `sempre` de volta no bloco do nível 27** | **acende** | **acende** |
| **contra-teste:** trocar duas linhas do índice de ordem | verde | verde |
| **contra-teste:** reescrever o bloco sem dizer `sempre` | verde | verde |
| o `README` dizendo *"índice das 88 entradas"* | acende | acende |
| **contra-teste:** a entrada da v0.84 continuando a dizer `81` | verde | verde |

> **A quinta e a sexta se medem por eixos diferentes de propósito.** *A quinta pergunta "existe bloco?"; a sexta pergunta "o bloco diz a mesma coisa que o preço?".* **Apagar o bloco acende a quinta; reescrever o bloco acende a sexta.** *Uma checagem só cobriria metade — e sairia verde exatamente na metade que custou a `Estocada`. É a lição nº 8 por outra porta.*

**A base passou na cópia antes de cada perturbação, e o `diff` foi conferido em todas.** *O arnês recusa resultado de `sed` que não bateu, que é a regra 3 dele.*

### ⚠ Achado — a ação `Mirar` não tem regra em lugar nenhum

**Ela é entregue no nível 11 das três rotas do `Batedor` e estendida no 27 das três — seis degraus, valendo entre `1,60` e `2,04` fatias cada.** *Procurada no repositório inteiro: ela aparece só no desenho e neste arquivo.* **Nem a lista de ações da peça 3 §3.1, que fechou na v0.83 com doze, nem o desenho dizem o que ela faz ou que slot ela gasta.**

> **E a triagem devolve o nome como `fraco`:** ele está a uma letra de `Mira`, que é Família no manual. **Mas o buraco é de regra e não de nome** — trocar o nome não escreve o que ela faz.

*O índice lista os seis degraus com o furo à vista, que é exatamente o trabalho dele.*

### ⚠ Achado na revisão cética, contra esta própria versão

**Escrevendo o `89` nos quatro documentos vivos, ele virou cinco cópias — dentro do documento cuja seção 1 abre dizendo que não vai duplicar nada.** *A peça 17 quase cometeu a lição nº 9 no parágrafo em que explica a lição nº 9.*

> **Conserto: a checagem 8.** A peça é a **dona** do total; `README`, `ESTADO-ATUAL`, `LEIA-ME` e o README da entrega são cópia, e agora existe quem compare. **O `CHANGELOG` fica de fora de propósito** — ele é registro histórico, e a entrada da v0.84 tem de continuar dizendo `81` sem falhar nada. *É o contra-teste 10.*

**A frase que ela procura é estreita de propósito:** *"índice das NN entradas"*, e não `NN entradas` solto. *Solto, ela pegava o catálogo de 19 entradas da peça 15 e o de 81 da peça 13 — outros catálogos, outros números, e três vermelhos falsos na primeira rodada.*

### Alterado — o mapa de números por extenso do `conferir-repositorio.py`

**Ele parava em `dezesseis` e a décima sétima peça não teria como ser lida.** *Estendido até `vinte`.* **O número continua sendo lido do `README`, e não guardado no código** — a checagem já saiu de sincronia uma vez, quando o oitavo validador entrou e o `sete` ficou escrito lá dentro.

### Em aberto

- **Faltam `21` nomes**, e não 17: `Muro` 3 · `Punho` 2 · `Brasa` 3 · `Estocada` 4 · `Yumi` 2 · `Besta` 3 · `Arma de Fogo` 2 · `Torrente` 2.
- **O `Mirar` precisa de regra antes de nome.**
- **`Quick Draw` é o único nome em inglês do sistema.** *Nível 19 da rota `Arma de Fogo`.*
- **Duas entregas têm nome em minúscula** — o `carregar` do `Yumi` e o `acelerar` da `Torrente` — contra as outras trinta e duas capitalizadas.
- **A checagem 6 não alcança as Manhas**, porque elas não têm bloco de regra separado — o texto de mesa delas é a própria coluna da tabela. *Propriedade do formato, não dívida.*
- **As três do Evocador ficam fora do índice enquanto estiverem paradas.** Quando voltarem, o total sai de `89` e a checagem 1 acusa até a peça subir junto.
- As de sempre: as quatro aptidões abertas, a troca do marco, os metros das armas de projétil, `Caído` para `Inconsciente`, o `Repertório` abandonado ainda vivo na peça 6 §2, o calendário velho de Caminho no §9 dela, e o nome do sistema.

---

## [0.84] — 2026-08-17

**As doze entregas do Guia saíram de linha de tabela e viraram texto de mesa**, e mais sete degraus do Emanador ganharam nome. *O Guia era o único Caminho sem uma única entrega jogável; virou o único com os três completos.* **E uma Trilha estava entregando quatro vezes o que ela custa.** Continuam dezesseis peças e dezesseis validadores.

### ⚠⚠ Corrigido — a `Estocada` nv27 valia `4×` o preço dela, e só a tabela tinha sido consertada

| onde | o que dizia | vale |
|---|---|---|
| a tabela de preço | o **primeiro** golpe da bônus carrega um Classe 0, **se o feitiço acertou** | `1,33` fatia |
| **o bloco de regra** | o golpe da bônus carrega **sempre** um Classe 0 | **`5,31` fatias** |

**A v0.81 repreçou a entrega e consertou só a tabela. A mesa lê o bloco.** *`5,31` é mais que a Trilha inteira, que leva `5,00`.* **`Torrente`, `Brasa` e `Explosivo` foram conferidas na mesma varredura e as três batem** — o defeito era só ali. ***Decisão registrada não é decisão aplicada***, pela enésima vez.

### Adicionado — as doze do Guia, com nome e sem buraco

| Trilha | 2 | 11 | 19 | 27 |
|---|---|---|---|---|
| **`Elo`** | `Nó` | `Repasse` | `Partilha` | `Trança` |
| **`Sutura`** | `Agulha` | `Enxerto` | `Pulso` | `Cerzido` |
| **`Perímetro`** | `Chão` | `Sentinela` | `Encalço` | `Portão` |

**Os três buracos do `Elo` fecharam, e os três saem do preço e não de gosto.** *Os `2,13` fatias do nível 2 foram calculados como `+1` de acerto **permanente**.* **Então: Ação Bônus para formar, num aliado que você enxerga, e o elo dura até você formar outro e não quebra por distância.** *Se custasse ação todo combate ou quebrasse por distância, o `+1` deixaria de ser permanente e o número publicado estaria errado.* **E o *"que você enxerga"* não é escala nova** — é como o `Guiar` já delimita aliado. *A `Partilha` REPARTE o total e não duplica: duplicar seria cura a mais, e dano evitado converte `1` pra `1`.*

### Decidido — a condição tem preço sem a peça de condições existir

***Decisão do Mizuki:*** *"tá tudo bem não existir, ele só precisa pagar o PE de cada nível de condição mesmo."*

> **O `Enxerto` tira condição por `1` PE por nível dela, e isso sai do mesmo teto da cura.** *Condição sem nível declarado conta como nível 1.*

**A regra preça pelo NÍVEL, então ela não depende da lista** — quando a peça de dano e condições existir e der nível a cada uma, ela já lê de lá sem ser reescrita. *O precedente já estava escrito: a exaustão da peça 10 §4 tem três degraus numerados.*

> **E um gate caiu da conta sem ninguém desenhar:** o teto por uso no nível 11 é `a sua maestria`, que ali vale `2`. **Então a exaustão de degrau 3 só sai a partir da maestria 3, que é o nível 17.**

### Decidido — a duração do `Encalço`, e a escolha não foi de conta

*O Mizuki ofereceu "cena de combate" ou "metade da Essência/Inteligência em rodadas", à minha escolha.* **As duas dão o mesmo preço:** o `−1d6` já é `1×` por rodada, então duração curta não corta o efeito — **ela só cobra a Ação Bônus de novo para repor.** ***Escolhido: até o fim da cena***, porque o que ela compra é um número a menos para a mesa carregar. *É a mesma razão que matou o efeito de crítico na v0.45.* **E `cena` tem definição própria na peça 10 §5.**

### ⚠ Corrigido — `marque` era colisão viva numa Trilha escrita

**O nível 19 do `Perímetro` dizia *"**marque** um alvo"* desde que foi escrito.** *`Marca` é **Família E Melhoria** no manual — a triagem acusa `OCUPADO` nas duas direções.* **Trocado por *"no encalço"*, que é o nome da entrega. Nenhum número se moveu.**

### Adicionado — sete nomes no Emanador

| Trilha | 2 | 11 | 19 | 27 |
|---|---|---|---|---|
| **`Explosivo`** | `Pavio` | `Estopim` | `Rompante` | `Ápice` |
| **`Arremate`** | `Empunhadura` | `Rebote` | `Crosta` | **— vago** |

*Os quatro do `Explosivo` saíram da lista que a v0.81 registrou como livre ao batizar a Trilha, e passaram pela triagem de novo.* **`Pavio` e `Estopim` não são sinônimo:** o pavio é o cordão que você acende, o estopim é o que detona.

> **O nível 27 do `Arremate` é o único degrau sem nome do sistema, e é de propósito: ele está VAGO.** *Nomear degrau vazio seria escrever entrada para fechar contagem — o defeito que a régua da peça 13 nasceu para achar.* **Sobram `1,26` fatia.**

### Onde a contagem de nomes está

**De 48 entregas de Trilha, `11` tinham nome antes desta versão. Agora são `30`.** *E as tabelas das cinco Trilhas mexidas ganharam coluna de nome.*

**Faltam `17`, em quatro Trilhas:** `Estocada` (4), `Batedor` (8), e o resto do `Muro`, do `Punho` e da `Brasa` (5). *Todas já têm texto de regra — é nome e triagem, sem buraco mecânico.*

### Em aberto

- **Faltam 17 nomes**, e depois deles a **peça 17** com as 81 entradas e o décimo sétimo validador.
- **O nível 27 do `Arremate` continua vago**, com `1,26` fatia.
- **Nenhum validador alcança os `DESENHO-*.md`** — foi por isso que a `Estocada` passou três versões com o bloco contradizendo a tabela. *A checagem "tabela e bloco de regra batem" é do validador da peça 17.*
- As de sempre: as quatro aptidões abertas, a troca do marco, os metros das armas de projétil, `Caído` para `Inconsciente`, o nome do sistema.

---

## [0.83] — 2026-08-17

**A lista de ações existe, e ela é a peça 3 §3.1.** *Até aqui esta peça tinha os quatro slots do turno e **nenhuma ação nomeada** — a lista vivia no fim do `DESENHO-caminhos.md`, que não é peça, e o `Ajudar` morava na peça 4 §5 sem custo de ação declarado desde a v0.22.* Continuam dezesseis peças e dezesseis validadores.

### Adicionado — as doze de Ação Padrão, conferidas na fonte

***Decisão do Mizuki: copiar a lista do hobby, e de propósito.*** *"Ninguém precisa aprender lista nova para uma coisa que todo jogador já sabe"* — e o filtro multi-mestre agradece.

**A lista do 5e de 2024 foi lida na fonte e não de memória, e ela tem doze.** *Oito já existiam aqui com outro nome.*

| o que faltava | o que entrou |
|---|---|
| `Influence` | **`Influenciar`** — e ela cabe sem adaptação, porque **Essência é o Carisma deste sistema**: `Persuasão`, `Enganação`, `Intimidação`, `Atuação` e `Provocar` moram todas lá |
| `Ready` | **`Preparar`** — Ação Padrão agora, Reação depois |
| `Search` · `Study` | **`Vasculhar`** e **`Estudar`**, com alvo separado do `Ler o Ambiente` |

### Decidido — o `Ler o Ambiente` se separa por ALVO, e a conta pedia isso

**O `Search` e o `Study` do 5e são os mesmos testes que o `Ler o Ambiente` faria, e custam a Ação Padrão contra a Ação Bônus dele.** *Mesmo teste, slot mais barato: os três não cabiam juntos, e nenhuma redação conserta dominância estrita.*

> ***Decisão do Mizuki:*** *"Ler o ambiente é algo mais de ajuda pro player sobre o ambiente. Study e Search poderiam ser coisas mais no tato e no inimigo, exigindo ação padrão mesmo."*

**`Ler o Ambiente` fala do LUGAR e nunca de criatura; `Vasculhar` e `Estudar` falam da criatura e da coisa.** *Com alvos diferentes elas param de responder à mesma pergunta, e a dominância some sem limite artificial.* **O `1× por cena` fica mesmo assim**, porque a ação obriga o mestre a produzir conteúdo e sem teto ela vira imposto de improviso.

### Alterado — `Agarrar` e `Derrubar` viraram opção do `Atacar`

*Decisão do Mizuki, seguindo o 2024.* **Como ação própria elas ficavam mortas por dominância:** agarrar custaria o turno inteiro, e bater duas vezes rende mais do que segurar alguém. *Com ataque extra dá para agarrar com um golpe e bater com o outro, que é o que um Bastião quer fazer.* **O `Segurar` do Bastião no nível 30 continua valendo palavra por palavra** — ele diz *"tentar `Agarrar` ou `Derrubar`"* e não cita slot.

### Corrigido — o `Ajudar` ganhou custo de ação, sete versões depois

*A peça 4 §5 escreve a regra do "um por teste" desde a v0.22 e **nunca disse em que ação ela acontece**.* **É Ação Padrão**, e está na peça 3 §3.1 com a peça 4 apontando para lá. *E o `Mão na Roda` do Guia passou a ser exceção de uma coisa que existe — antes ele era exceção de uma regra não escrita.*

### Adicionado — cinco checagens no `conferir-acao.py`, com oito perturbações

**Nada de valor mora dentro delas: os nomes são lidos da própria peça.** *O que elas guardam é a estrutura.*

| perturbação | esperado | deu |
|---|---|---|
| apagar o `Preparar` da tabela | acende | acende |
| apagar o `Influenciar` da tabela | acende | acende |
| pôr `Agarrar` de volta como ação própria | acende | acende |
| **apagar a linha *"nunca fala de criatura"*** | acende | acende |
| tirar o teto de uma vez por cena | acende | acende |
| apagar o `Ajudar` da tabela | acende | acende |
| renomear a seção 3.1 | acende | acende |
| **contra-teste:** trocar a ordem de duas linhas | verde | verde |

> **A checagem que mais rende é a da linha de alvo.** *Ela é a única de balanço do conjunto: sem a frase que diz que o `Ler o Ambiente` nunca fala de criatura, uma Ação Bônus volta a dominar duas Ações Padrão — e a matriz não veria, porque as três continuariam existindo.*

### Corrigido — o total de `por cena` da peça 10, e o validador achou sozinho

**Eram `91` e viraram `93`**, e os dois novos são o `Ler o Ambiente`. *O `conferir-descanso.py` reconta da pasta e falhou na primeira edição, que é exatamente o trabalho dele.* **Total guardado à mão envelhece na primeira edição de outro documento.**

### Em aberto

- **`Preparar` é o quinto competidor pela Reação**, e a peça 3 §7 já desconfiava do slot com quatro. *Marcado para o playtest.*
- **O `Ler o Ambiente` não tem preço** — ele entrega informação, e o projeto não tem conversão para isso. *O teto de uma vez por cena é o que segura ele enquanto a régua não existir.*
- **Se o `Ajudar` fora de combate segue a mesma regra** de um por teste.
- **Duas ações bônus ainda é pouco** para o slot mais vazio do turno.
- As 48 entregas de Trilha, os 20 degraus de Caminho e as 13 Manhas **continuam fora de peça numerada** — é a próxima da fila.
- As de sempre: as quatro aptidões abertas, a troca do marco, os metros das armas de projétil, `Caído` para `Inconsciente`, o nome do sistema.

---

## [0.82] — 2026-08-17

**A dívida de linha de base que a v0.81 marcou com `⚠⚠ LIMPAR ANTES DO PDF` NUNCA FOI DÍVIDA.** *Ela era uma frase que ninguém tinha escrito, e a própria peça 6 já tinha registrado a resposta como "anotado, não decidido".* **Zero número se moveu.** E entraram as **treze Manhas** da Vanguarda, que fecham o nível 2 daquele Caminho. Continuam dezesseis peças e dezesseis validadores.

> **⚠ Esta versão subiu em DOIS commits, e o primeiro foi sem esta entrada.** *O commit `7ad1a89` levou as Manhas e o `.gitignore` com a etiqueta v0.82 enquanto o `README`, o `ESTADO-ATUAL` e o `LEIA-ME` ainda diziam v0.81.* **É a mesma falha que a v0.80 registrou, e ela continua sem validador** — a checagem existente só pega quem sobe a versão nos documentos sem escrever a entrada, e não o contrário.

### Fechado — o ataque extra é um golpe SOLTO por rodada

*Achado do Mizuki, e ele veio de uma pergunta e não de uma conta:* ***"já é um ataque extra, é uma mecânica forte, não acho que precisa disso."***

**Ele estava certo, e três mensagens de orçamento tinham sido construídas em cima da premissa errada.** *Eu vinha medindo quanto o nível 7 dos cinco Caminhos perderia e como devolver `1,23` fatia — e a pergunta certa era outra.*

**A peça 6 §3.1 sempre teve a linha `feitiço de Toque + golpe simples` marcada como EXISTENTE na tabela dos três turnos.** *O que faltava era dizer de onde vinha o golpe, e aquela seção já tinha escrito a resposta e a deixado como "anotado, não decidido".*

> **O ataque extra não exige a Ação de Atacar.** Quem tem ataque extra ganha um golpe simples **por rodada**, e ele acontece junto do que a Ação Padrão fez — inclusive quando ela conjurou.

**A reconstrução é a prova, porque ela reproduz uma coisa que não foi posta nela:**

| a rodada, no nível 30 | conjurador | físico | a diferença |
|---|---|---|---|
| gastando PE — o feitiço grande | `94,0` | `105,5` | **`11,5`** |
| poupando PE — um Classe 0 | `27,0` | `38,5` | **`11,5`** |

**A diferença é a mesma nas duas, e é exatamente um golpe simples** — que é o vão `9 · 10 · 11 · 12` que a peça já publicava.

### Medido — a alternativa reprova por DOMINÂNCIA, e não por orçamento

**Com o ataque extra preso à Ação de Atacar, dois golpes rendem `23` no nível 30 e um Classe 0 grátis rende `27`.**

*A habilidade de nível 7 de dois Caminhos perderia para o botão que toda ficha já tem, ninguém usaria a Ação de Atacar nunca, e o físico e o conjurador terminariam idênticos em `60,50` de dano por rodada.* **Uma entrega de Caminho que perde para o botão grátis não é decisão de design.**

> **E a v0.81 registrou no CHANGELOG a frase contrária** — *"o ataque extra sempre exige a Ação de Atacar, como no 5e"*. *Ela contradizia a tabela dos três turnos da mesma peça, que já marcava a linha do físico como existente.* **A peça 6 §3.1 é a dona; o CHANGELOG registra o que se pensou naquele dia.** *A decisão que SOBREVIVE inteira é a outra da v0.81: a Ação de Atacar não inclui o feitiço de Toque. As duas convivem, porque o ataque extra não é parte da Ação de Atacar — ele é um passageiro da rodada.*

### Adicionado — a checagem 4h, e ela guarda a FORMA e não o número

*A peça 6 declarava esta dívida com todas as letras: **"nenhum `conferir-*.py` lê a forma do ataque extra — trocar o slot ou apagar o gate não falha validador nenhum."***

**Ela tem três metades independentes de propósito**, porque uma checagem que só procurasse a frase afirmativa sairia verde se alguém ADICIONASSE a frase contrária sem apagar a primeira: a declaração existe · nenhuma linha viva prende o ataque extra à Ação de Atacar · o gate do golpe do `Arremate` e do `Coro` continua escrito.

**Sete perturbações, em cópia isolada, com a base conferida antes e o `diff` conferido em cada uma:**

| perturbação | esperado | deu |
|---|---|---|
| apagar a declaração do golpe solto | acende | acende |
| trocar o *"não exige"* por *"exige"* | acende | acende |
| linha **viva** prendendo à Ação de Atacar | acende | acende |
| a mesma linha em bloco de citação | verde | verde |
| a mesma linha em nota de itálico | verde | verde |
| apagar o gate do `Arremate` e do `Coro` | acende | acende |
| **contra-teste:** fazer o vão encolher | acende | acende **pela 4f** |

> **A regra 3 do arnês pagou nesta versão.** *O primeiro contra-teste numérico não bateu no formato da tabela e o arquivo não mudou* — e o arnês recusou o resultado em vez de deixar reportar um "acendeu" falso. **O segundo, com o formato certo, acendeu pela `4f`.** *As duas checagens se cobrem por eixos diferentes: a `4h` guarda a forma, a `4f` guarda o número.*

### Adicionado — as treze Manhas da Vanguarda

*O nível 2 da Vanguarda apontava para um catálogo que não existia desde a terceira passada de Caminhos — item 1 do "o que sobrou aberto" daquele desenho, marcado como o maior trabalho que ele criava.*

**A RÉGUA VEIO ANTES DO CATÁLOGO, e ela reprovou sete das oito propriedades de maestria do 5e de 2024.** *A causa é estrutural e não de preço: aqui `+1` no acerto vale `10,80` de dano por rodada, que é `10%` da Rotina, então vantagem vale `54,00` contra um degrau de uma fatia — `10,6` vezes o degrau inteiro.* **Só o `Graze` cabe sozinho.**

**As treze caem entre `0,68` e `1,18` fatia, média `0,98`, dominância `1,74×` contra um filtro que reprova em `3,00×`.** *Calibração: o `Guiar` do Guia vale `0,68` no mesmo degrau e o `Absorver` do Bastião vale `1,60`.*

**Duas decisões do Mizuki destravaram o catálogo.** *Dano de valor **FIXO** é legal — a cerca da peça 5 proibia "dado de dano" e ninguém tinha escrito se fixo entrava junto; isso resolve de graça a mesma pendência na `Presa` do Evocador.* **E derrubar fica, aplicando a condição `Caído`**, com o efeito por extenso até a peça de dano e condições existir.

> **`derrubar` foi DERIVADO das duas réguas que já existem, e não inventado:** vantagem para um aliado corpo a corpo (`25` pp × `0,230` = `5,75`) mais o alvo gastando `4,5 m` para levantar (`2,70`), dando `8,45` por rodada — `1,66` fatia permanente, que a trava de `60%` põe em `1,00`.

**A triagem matou quatro nomes:** `Fio` (dentro de `Fio Preso`), `Volta` (dentro de `Sem Volta`), `Sopro` e `Trava` (feitiço pronto e Melhoria do manual). **E um quinto morreu FORA dela, por colisão de sentido:** `Ajuste` saiu `LIVRE` e foi recusado porque `Ajusta` é formato de Legado e aparece **42 vezes** na peça 13.

### Parado — o Evocador sai da fila, e NÃO por ter morrido

***Decisão do Mizuki:*** *"ninguém vai usar essa classe por enquanto."* **O §6 do `RASCUNHO-trilhas.md` ganhou cabeçalho de parada.** *Ele não foi para `99-arquivo/`, e a diferença importa: aquela pasta é de material morto com o motivo da morte escrito, e nada ali morreu.* **O `Servo` está montado e fecha em `5,07` contra um orçamento de `5,07`** — falta só o gatilho do nível 27.

### Adicionado — o repositório de entrega

**`finalizado/` virou repositório próprio** e entrou no `.gitignore` daqui: ela é **artefato e não fonte**, regerada quando uma versão fecha e nunca editada à mão. *A mesma distinção que o `.gitignore` já fazia com o `.docx` gerado dentro do `manual/gerador/`.*

> **O motivo tem número:** o repositório de trabalho tem `2,2 MB` de texto e `628 KB` disso é este CHANGELOG. **Para escrever texto de mesa isso é ruído que gasta o contexto de quem lê.** A entrega tem `816 KB` e nenhum byte de histórico de decisão.

### Em aberto

- **As 48 entregas de Trilha, os 20 degraus de Caminho e as 13 Manhas continuam fora de peça numerada.** *É a próxima da fila, e é o que faz o `Repertório` abandonado ainda estar vivo na peça 6 §2.*
- **A lista de ações continua fora de peça** — ela mora no fim do `DESENHO-caminhos.md` e nove Trilhas apontam para ela.
- **A troca do marco paga mal do nível 22 em diante**, e o que falta não é a régua impossível de *"uma aptidão a mais"*: no marco a comparação é entre as três opções para o mesmo jogador, e aí a aptidão e a Passiva se cancelam.
- **São QUATRO entradas de aptidão abertas e não três** — `Barreira Simples`, `Cortina`, `Aptidão Própria` e a **terceira de kokusen, que não tem nome e tem o gate "a definir"** enquanto é contada entre as onze fechadas.
- **Os metros de cada arma de projétil não existem**, e a propriedade `Longo Alcance` já custa `1` ponto no orçamento das onze.
- **A troca de `Caído` para `Inconsciente` no estado de 0 de vida continua não aplicada**, e o termo é citado nas peças 1, 13 e 15.
- **Atribuição de versão continua sem validador**, e esta versão é o exemplar novo.
- As de sempre: as vagas de `Desliga`, a Cicatriz, o clash, o nome do sistema, `condição` sem conversão, gastar PE sem preço.

---

## [0.81] — 2026-08-16

**A v0.80 deixou dois avisos pendurados na régua de Trilhas, e os dois foram medidos: o orçamento NÃO se move.** *O vão corrigido não muda o preço de nenhuma das onze Trilhas fechadas, e o teto que morreu não tem substituto — foram testados três candidatos.* **E o Classe 0 fantasma tinha sobrado num lugar que a guarda da v0.80 não alcançava, porque aquela guarda tinha um buraco de uma linha.** Continuam dezesseis peças e dezesseis validadores.

### Medido — a régua não se move com o vão corrigido, e o motivo é que o ponto de chegada é o mesmo

| | conjurador | degrau do nv7 | chega em | físico |
|---|---|---|---|---|
| leitura velha | 99 | `7` | **106** | 106 |
| **leitura nova** | **94** | **`12`** | **106** | 106 |

**O que mudou foi o tamanho do degrau de GRAÇA, e ele nunca saiu das fatias.** *A fatia continua `5,08`, o Caminho continua levando `3` e a Trilha `5`.*

**Conferido por varredura, e não por argumento:** existem três lugares no repositório que usam o vão como base de preço — os dois degraus de nível 7 marcados no `DESENHO-caminhos.md` e o nível 2 do `Arremate` —, e os três já estavam tratados. **Nenhuma entrega de Trilha foi preçada contra o vão.**

### Medido — sem o `+18%`, NADA reprova, e isso foi procurado antes de ser afirmado

As outras quatro travas da v0.72, rodadas de `1×` a `8×`:

| trava | o que ela faz sozinha |
|---|---|
| a magnitude nunca vem de ação a mais por rodada | regra de **mecanismo** — proíbe uma porta, não limita tamanho |
| a camada não deriva como fração da saída | **melhora** quando o orçamento cresce: `3,61×` → `1,81×` |
| continua acima do piso da peça 14 | é **piso**; crescer nunca viola |
| a fatia continua plana | propriedade de construção |

> **Contra-teste rodado, senão isto seria trivialmente verdadeiro:** o `+18%`, vivo, **reprovaria a partir de `3×`**, e reprova o orçamento de hoje em `+35,7%`. **Existia teto, era ele, e era o único.**

**Três candidatos a substituto, e os três caíram:** a coluna *dano do grupo por rodada* e a *duração de combate* têm dono no **playtest**, que está vazio; a razão *chefe = 3 a 4× o dano do grupo* é invariante de **relação** e não teto de nível.

**E o único que reconstrói sem passar pelo playtest nunca morde:** *"a técnica continua sendo a maioria da ficha"* só reprova em **`10,45×`**, que é `2,6` vezes o orçamento de hoje. *Um teto que só acende a dez vezes de onde estamos é a lição nº 8 por outra porta.*

> ***Decisão do Mizuki: o teto é declarado como decisão de design, e não vestido de conta.*** **O orçamento é `4×` — `27,7%` da ficha para a camada, `72,3%` para a técnica** —, com o argumento dele da v0.73 escrito junto. *Âncora externa levantada: no 5e a subclasse carrega de `10%` a `30%` do orçamento de classe mais subclasse. O denominador não é o mesmo, então ela vale como ordem de grandeza e não como trava.*

### Achado — o modelo de combate do manual reconstrói, e ninguém tinha escrito isso

**A coluna *dano do grupo por rodada* da tabela de inimigo é `2,90 ×` a Rotina, nas seis linhas**, com espalhamento de `1,024×`. *Ela não é número solto: é um grupo de quatro em que a saída efetiva é de 2,9 fichas.*

**Com isso o modelo reproduz os dois números que a v0.73 publicou, com zero parâmetro livre:** `3,69` rodadas sem a camada e `2,72` com ela, contra os `3,7` e `2,7` escritos lá.

> **E ele produz a primeira pergunta de mesa deste orçamento com número em cima:** no orçamento de hoje **o chefe deixa de conseguir derrubar a ficha mais frágil concentrando fogo** — a virada acontece entre `2×` e `3×`. *É teto e não valor, porque supõe que as `8` fatias inteiras viram dano, e a matriz do Bastião diz que não viram.*

### Corrigido — o Classe 0 fantasma sobreviveu à v0.80 na peça 6 §5, sem a frase e só com o número

A linha argumentava o PE do Bastião assim: *"o golpe simples dele rende ~10 e o Classe 0 do conjurador rende ~4,5"*.

| nível | Classe 0 | golpe simples | quem rende mais |
|---|---|---|---|
| 2 | `2d8` = 9 | 9 | empate |
| 10 | `3d8` = 13,5 | 10 | Classe 0 |
| 30 | `6d8` = 27 | 12 | **Classe 0, em 2,25×** |

**O argumento não só perdeu o número: ele INVERTE do nível 10 em diante.** *O `~10` batia com o golpe simples e o `~4,5` era o dano de um d8 — a régua de montar feitiço outra vez.*

**O número `4` fica**, e ele passou a se apoiar no que a própria peça já tinha: o Bastião é o único dos cinco com `11` de vida mais energia por nível contra `10` dos outros. *Ele troca combustível por couro e sai um ponto na frente da troca.*

### Corrigido — a guarda da frase morta tinha um buraco, e ele era de uma linha

**Ela tratava qualquer linha começando com `*` como nota histórica — e `**negrito**` começa com `*`.** *Negrito no começo da linha é o estilo dominante da prosa deste projeto, então toda afirmação viva em negrito era lida como história.*

**Agora `>` é história, `*` sozinho é história, e `**` é afirmação viva.**

> **Contra-teste rodado:** com a regra antiga, a frase morta numa linha de negrito sai **verde**. É o buraco medido, e não suposto.

### Adicionado — a checagem 4g, com sete perturbações

**4g — o NÚMERO morto, e não só a frase.** Nenhuma linha viva da peça 6 pode preçar um Classe 0 em `4,50`.

| perturbação | esperado | deu |
|---|---|---|
| `4,50` num Classe 0, em linha viva de negrito | acende | acende |
| `4,50` num Classe 0, em bloco de citação | verde | verde |
| `4,50` num Classe 0, em nota em itálico | verde | verde |
| a frase morta em linha viva de negrito | acende | acende |
| a frase morta em bloco de citação | verde | verde |
| `4,5` longe de Classe 0 (média do d8) | verde | verde |
| devolver o conjurador `99` no nível 30 | acende | acende |

> **A base foi conferida na cópia antes de perturbar, e ela pegou uma cópia suja na primeira tentativa** — todas as perturbações acendiam por causa disso. *É a regra 2 do arnês fazendo exatamente o trabalho dela.*

### Achado — CINCO entregas publicadas foram calculadas a partir do Classe 0 fantasma

**A v0.80 corrigiu a tabela e repreçou só o `Arremate`. As outras foram calculadas *a partir* do `4,50` e nunca refeitas.**

| entrega | publicado | o modelo com o fantasma | refeito |
|---|---|---|---|
| `Brasa` nv2 — Classe 0 na bônus | 1,22 | **1,22** | 4,08 |
| `Brasa` nv19 — o bônus vira Classe 2 | 1,03 | **1,03** | 0,00 a 2,36 |
| `Estocada` nv27 — o golpe carrega um Classe 0 | 0,89 | **0,89** | 1,33 |
| `Torrente` nv11 — o teto vira Classe 3 | 3,78 | **3,77** | 1,38 |
| `Torrente` nv27 — o teto vira Classe 4 | 1,49 | **1,49** | 1,49 |

> **A coluna do meio é a prova de que o achado não é erro de modelo:** ele reproduz o número publicado usando o fantasma, e só depois troca pelo valor do manual. *O nv27 da `Torrente` não se move porque ele é `Classe 4` menos `Classe 3` e o Classe 0 não entra.*

**E a regra que sai daí, que é do sistema e não de uma Trilha:** *um Classe 0 causa `27` no nível 30 e a fatia é `5,08`.* **"Ganha um Classe 0 por rodada" vale `5,31` fatias, e o orçamento de uma Trilha é `5,00`.** *Antes da v0.80 isso custava `0,89` e cabia em qualquer canto.*

> **E um número que explica metade do estrago:** no nível 30 um **Classe 0 causa `27` e um Classe 2 num alvo causa `27`**. São iguais. *Toda entrega que "sobe o Classe 0 para Classe 2" vale zero em dano no nível em que a fatia mede.*

### Fechado — o buraco de texto mais caro da v0.80

*Aquela versão registrou que a peça 6 nunca disse se a Ação de Atacar de um físico inclui o golpe canalizado, e que a frase decidia a `Brasa` por `2,6×`.*

> ***Decisão do Mizuki: não inclui.*** *"Não tem como bater junto de um feitiço — isso é só o efeito da `Fornalha`."* **Canalizar e atacar são ações diferentes e não cabem no mesmo turno.**

**Escrito na peça 6 §3.1, com a tabela dos três turnos e o que ela destrava:** toda entrega pendurada em *"se você usou a ação de atacar"* **não dispara na rodada em que o personagem canaliza** — e é isso que faz o nível 2 da `Brasa` ser preçado por taxa em vez de somado no pico.

*Fica anotado o que ela deixa pendurado: se o golpe simples da linha do físico não vem da Ação de Atacar, ele vem do ataque extra como golpe solto por rodada, e isso não está escrito em lugar nenhum.*

### Alterado — as três Trilhas, repreçadas com o Mizuki

**`Torrente` — `5,37` para `4,65`.** *A premissa dela estava errada: ela existe para furar o teto de `Classe 0` do segundo feitiço, e furar esse teto vale `13` de dano e não `36`.* **O nível 19 velho morreu — ele premiava lançar `Classe 0`, que deixou de ser lixo — e virou o `Mão Firme`:** rerrolar `1`, `2` e `3` nos dados de dano quando o feitiço for o único da rodada.

> **A ideia é dele e o alvo mudou uma vez.** *A proposta era vantagem na rolagem de ataque; ela deu `21,59` de dano — a **quarta** aparição da mesma parede, depois da `Arquearia`, do `+2` no menu do `Elo` e da `Modelagem` como presente.* **O gate sobreviveu inteiro; o botão trocou.**
>
> **E fica declarado que o sistema passou a ter DUAS rerrolagens** — a `Arma Grande` rerrola `1` e `2`, o `Mão Firme` rerrola `1`, `2` e `3`. *A diferença existe para o orçamento fechar e não tem justificativa de design; escrever isso é melhor que inventar um motivo.*

**`Estocada` — `4,58` para `5,02`, e o conserto do nível 27 é dele.** *Três cláusulas:* **só o primeiro golpe da bônus** — que não muda o número mas fecha uma ambiguidade real, porque o nível 19 cria um segundo golpe —, **o feitiço da padrão tem de ter acertado**, e o Classe 0 acompanha o golpe. **Os dois gates dão `25%`, e a entrega cai em `1,33` fatia.**

> **A dominância declarada desde a v0.75 INVERTEU:** era `Arma de Fogo` sobre `Estocada` por `1,03×` e virou `Estocada` sobre `Arma de Fogo` por `1,06×`. *Mesmo tamanho, outro sentido, e continua ruído.*

**`Brasa` — `5,03` para `7,06` a `9,42`, e o estouro fica.** ***Decisão do Mizuki:*** *"Parece que é forte, mas não é, garanto."* **A matriz do Bastião continua limpa nos dois extremos da faixa**, que é o mesmo motivo que segurou o `Punho` em `+22%`.

*O nível 19 ganhou a escada dele — `Classe 3`, e `Classe 4` quando a `Classe 6` libera no nível 21, pagando o PE normal.* **Ele é faixa e não número porque briga com o feitiço grande pela mesma energia:** canalizar rende `2,64` de dano por PE e o `Classe 4` na bônus rende `1,29`, e o poço cobre exatamente as conjurações do dia. *Vale `0,00` se o `Brasa` carrega feitiço grande e `2,36` se ele monta só pequeno — e ninguém escreveu para que lado a Trilha empurra.*

### ⚠⚠ Achado — o "golpe canalizado" NUNCA EXISTIU, e é o terceiro fantasma

*Achado pelo Mizuki: **"não existe golpe canalizado. É uma abreviação que foi feita e tá misturando tudo — é um feitiço de Toque que foi entendido como ataque."***

| termo | ocorrências no manual |
|---|---|
| `golpe canalizado` · `canalizado` · `canaliza` · `Canalizar` · `golpeadora` | **0** |

**E ele aparecia 60 vezes em 12 arquivos do projeto, incluindo a linha de base da peça 6 e uma seção inteira da peça 5.**

> **O padrão dos três fantasmas é o mesmo, e agora dá para nomear:** *o Classe 0 de `4,50` era um **número** inventado lendo a régua errada; o `+18%` era um **teto** que não reconstruía de nada; o golpe canalizado é uma **mecânica** inteira.* **Os três nasceram do projeto ler o manual, criar um intermediário para explicar, e o intermediário virar fonte.**

**A palavra "golpe" é o que fez o estrago:** um feitiço de Forma Toque passou a parecer um ataque, e com isso a economia de ação do projeto inteiro ficou ambígua. *É a raiz do buraco que a v0.80 chamou de "o mais caro que ela deixou aberto".*

### Alterado — o termo limpo em 39 lugares, sem mexer em número

**`golpe canalizado` → `feitiço de Toque`**, em 11 arquivos. **A aptidão `canalizar energia` FICA** — ela é termo da obra, e a peça 11 a lista entre as doze que o material obriga. *O que morreu é o substantivo.*

*A troca quebrou a checagem 13 do `conferir-ferramenta.py`, que procurava a frase literal na peça 9. Ela passou a aceitar as duas formas, e o teste negativo foi rodado: apagar a rota da peça 9 acende.*

### ⚠ E o que a troca NÃO consertou — marcado para antes do PDF

**A linha do físico da peça 6 §3 continua publicando `106` = feitiço de Toque + golpe simples.** *Um feitiço de Toque gasta a Ação Padrão; o golpe simples e o ataque extra exigem a Ação de Atacar.* **Decisão do Mizuki nesta versão: o ataque extra sempre exige a Ação de Atacar, como no 5e.** *Então os dois não cabem no mesmo turno.*

| | publicado | sem o fantasma |
|---|---|---|
| conjurador | 94 | 94 |
| físico | **106** | **94** |
| **o vão** | **12** | **0** |

**Se o vão é zero, o degrau do nível 7 dos cinco Caminhos fica sem o que o pagava** — e com ele o nível 2 do `Arremate`, o `Resquício`, e as duas decisões que a v0.80 marcou. *O ataque extra passaria a valer ~`1,2` fatia, medido pelas rodadas em que o PE acabou.*

> ***Decisão do Mizuki: não refazer agora.*** *"Prefiro finalizar o projeto, testar e trazer o retorno, do que voltar atrás nessas coisas."* **O aviso está no topo do §3 da peça 5, com a conta, e apontado da peça 6.**

### Achado de graça — o manual já tinha a taxa escrita, e eu derivei em vez de ler

> *"Na prática, um conjurador gasta PE em **cerca de metade das rodadas** de luta do dia e passa a outra metade no Classe 0, no golpe simples e no que for de graça."*

**É a mesma taxa que eu vinha derivando do pool de PE a versão inteira — `44%` a `56%`.** *Ela tem dono, e o dono é o manual.* **E a outra frase dele fecha o Classe 0:** *"São o golpe de todo turno em que o PE precisa ser poupado."*

### Adicionado — o `Explosivo`, e o Emanador fechou com três Trilhas

> **`5,57` de `5,00` — `11%` acima, metade do estouro do `Punho`.** *Decisão do Mizuki: fica.*

| nv | a entrega | fatias |
|---|---|---|
| **2** | rerrolar `1` e `2` nos dados de dano, **quando for o seu único feitiço de dano da rodada** | 1,42 |
| **11** | somar o **atributo de conjuração** no dano de todo feitiço | 1,18 |
| **19** | gastar **`a Classe` em PE** para rolar o ataque do feitiço **com vantagem** | 2,25 |
| **27** | `1×` por cena, **+metade da Classe em dados**, pagando `1` PE por dado extra | 0,72 |

**O desenho inteiro é do Mizuki**, e ele corrigiu três coisas minhas no caminho.

### Removido — o `Repertório`, e o motivo é que a régua dele não pode existir

**A ficção era boa e o preço era impossível.** *Ela só se media por "uma aptidão a mais" — e isso vale a Trilha inteira para quem nunca escolhe Refino e um sétimo para quem sempre escolhe.* **E as duas colunas vazias do Caminho não aguentam uma Trilha:** recuperação pediria `3` de PE por rodada devolvidos, posicionamento pediria `26` metros por rodada. *O `Perímetro` do Guia já tinha batido nessa parede.*

> **E a régua que eu disse existir não existia — o Mizuki pegou perguntando "certeza que a `Sutura` adianta a `Energia Reversa`?".** *Eu afirmei que o `0,89` dela preçava "aptidão cedo".* **Ele preça a CURA:** `2` PE de teto × `4,5` por PE = `9` de cura, dano evitado converte `1` pra `1`, vezes `50%` de rodadas curando. **Dá `0,89` exato.** *O "sem gate" torna a aptidão disponível; o número vem do efeito.*

### Corrigido — dois erros meus que o Mizuki achou no preço do `Explosivo`

**1 — a deriva do atributo se mede do nível em que a entrega CHEGA.** *Eu reprovei "somar atributo no dano" lendo a deriva do nível 2: `23,1%` da Rotina lá contra `5,6%` no 30, que é `4,15×`.* **A entrega chega no nível 11, e de lá ao 30 a deriva é `1,60×`** — dentro do filtro. *É por isso que a `Presa` do Evocador reprovou e esta passa: a `Presa` chega no nível **2**.*

**2 — a vantagem por PE compete com conjurar, e eu não tinha modelado isso.** *Eu preçei ela em `9,25` fatias — a quinta aparição da parede dos `21,60`.* **O PE gasto na vantagem é um feitiço a menos depois.** Modelando o dia inteiro como otimização — `180` de PE, `13` rodadas, o jogador escolhendo entre conjurar de novo e comprar vantagem:

| custo | o degrau vale | a Trilha |
|---|---|---|
| `metade da Classe` — 4 PE | 3,98 | 7,30 |
| **`a Classe` — 7 PE** | **2,25** | **5,57** |
| `Classe e meia` — 11 PE | 1,12 | 4,44 |

*Sem a entrega o melhor dia rende `886` de dano; com ela a `7` PE, `1.034`.* ***Decisão do Mizuki: `a Classe`, porque é fórmula com dono e escala sozinha — `10` fixo fecharia na banda e seria número solto.***

### ⚠ Declarado — o `Explosivo` domina a `Torrente` por `1,20×`

As duas são `100%` ação/alvo e nenhuma tem coluna que a outra zere. *Maior que a da `Arma de Fogo` sobre a `Estocada` (`1,06×`), e dentro do filtro que reprova em `3,0×`.* **A causa é a mesma das outras: falta coluna, não sobra número** — o Emanador inteiro tem posicionamento e recuperação vazios nas três.

### Em aberto

- **⚠ A dominância do `Explosivo` sobre a `Torrente` é `1,20×`**, declarada e não consertada.
- **⚠⚠ LIMPAR ANTES DO PDF: a linha de base do físico ainda está em cima do fantasma.** *Peça 5 §3 tem o aviso com a conta.*
- **⚠ O nível 19 da `Brasa` é faixa, e o que decide é o que o jogador monta.** *Primeira coisa a medir na mesa, junto do estouro dela.*
- **A lista de ações continua fora de peça numerada** — ela mora no fim do `DESENHO-caminhos.md` e nove Trilhas fechadas apontam para ela.
- **⚠ O golpe simples da linha do físico não tem casa escrita** — se ele não vem da Ação de Atacar, vem do ataque extra como golpe solto, e isso não está em lugar nenhum.
- **O teto da régua não tem validador, e isso está declarado no §5 do rascunho** como decisão, não esquecimento.
- **⚠ Se o chefe deixa de derrubar a ficha mais frágil é bom ou ruim, ninguém sabe** — é a primeira pergunta de mesa deste orçamento.
- **A tabela de inimigo continua parada**, e o dono dela continua sendo o playtest.
- **O `Repertório`** — a última do Emanador, e ela precisa liderar em posicionamento ou recuperação. *E continua sem régua para converter "uma aptidão a mais" em fatia.*
- **⚠ A peça 6 nunca escreveu se a Ação de Atacar de um físico inclui o golpe canalizado**, e essa frase decide a `Brasa` por um fator de `2,6×`.
- **As duas decisões de nível 7 tomadas contra o vão errado continuam marcadas e não desfeitas** — o Guia e a `Coleira` do Evocador.
- **O nível 27 do `Arremate` está vago**, com `1,26` fatia.
- **A checagem de pasta certa do README estava quebrada** — ela mandava `grep -c "Seis lições"` dar zero, e na pasta certa dá dois, porque o próprio README escreve a frase duas vezes. *Não consertada nesta versão.*
- **A v0.80 foi commitada duas vezes com a mesma etiqueta**, que é a causa conhecida da atribuição de versão divergir. *Vale conferir se algo dela ficou no commit errado.*
- **Atribuição de versão continua sem validador.**
- As de sempre: as vagas de Desliga, a Cicatriz, o clash, o nome do sistema, o refino que paga mal no marco, `condição` sem conversão, gastar PE sem preço.

---

## [0.80] — 2026-08-16

**O projeto estava preçando o Classe 0 num número que não existe no manual, e isso vinha da v0.14.** *Achado indo escrever a permissão do `Arremate`: a frase que sustentava o argumento é que a Rotina "já é feitiço + Classe 0", e ela é falsa.* **O vão que paga o degrau do nível 7 dos cinco Caminhos passou de `7,00` para `12`, a `Voz Grossa` morreu e a permissão do `Arremate` foi aplicada.** Continuam dezesseis peças e dezesseis validadores.

### Achado — o Classe 0 tem tabela no manual, e ninguém neste projeto tinha aberto ela

| seu nível | 1 | 5 | 11 | 17 | 25 |
|---|---|---|---|---|---|
| quantos você tem | 2 | 3 | 4 | 5 | 5 |
| **dano** | 2d8 | 3d8 | 4d8 | 5d8 | **6d8** |

**No nível 30 um Classe 0 causa `27`. O projeto preçava ele em `4,50`, em todo nível, e `4,50` não aparece em lugar nenhum do manual.** *A origem provável é o glossário — "cada ponto que sobra vira `1d8`" —, que é a régua de montar feitiço e não o dano de um Classe 0. É a mesma família do `Fluxo | 2` que a v0.76 registrou: coluna lida errada numa tabela do manual.*

**Nenhum documento do projeto citava essa tabela. Nenhum validador abria ela.** Ela era a **quarta** tabela compartilhada com o manual, e a única sem dono declarado — as outras três são PE (dono: o projeto), Rotina (o manual) e inimigo (o playtest). *Decisão do Mizuki: **o dono é o manual**, e o projeto se corrige.*

### Corrigido — a Rotina nunca foi "feitiço + Classe 0", e agora ela reconstrói

| Classe | num alvo (`3 × C`) | somando alvos (`4 × C`) | o meio | Rotina publicada |
|---|---|---|---|---|
| 1 | 13 | 18 | 13 | 13 |
| 3 | 40 | 54 | 45 | 45 |
| 5 | 67 | 90 | 76 | 76 |
| 7 | 94 | 126 | **108** | **108** |

**A Rotina é `floor(3,5 × Classe)` dados — o meio exato entre bater num alvo e espalhar.** Fecha nas sete Classes, com zero parâmetro livre.

**E um Classe 0 não cabe junto do feitiço grande.** Todo feitiço custa Ação Padrão; a única Melhoria que muda isso é a `Rápido`, que custa o degrau **Pesada**; e o manual escreve que numa Classe 0 só cabe Melhoria do degrau `Leve`. *Pôr `Rápido` no feitiço grande para os dois caberem piora a rodada em todo nível do 10 em diante: no 30 ela sai de `94` para `72`.*

### Alterado — a linha de base da peça 6 §3, e o vão

| nv | Rotina | conjurador antes | **conjurador agora** | físico | vão antes | **vão agora** |
|---|---|---|---|---|---|---|
| 2 | 13 | 18 | **13** | 22 | 4 | **9** |
| 10 | 45 | 45 | **40** | 50 | 5 | **10** |
| 18 | 76 | 72 | **67** | 78 | 6 | **11** |
| 30 | 108 | 99 | **94** | 106 | **7** | **12** |

**O vão publicado era o golpe simples menos `5` em todo nível, e o `5` era o Classe 0 fantasma.** Sem ele, **o vão é exatamente um golpe simples** — que faz sentido, porque o físico *é* o conjurador mais um golpe.

> **E isso conserta uma coisa de graça: os cinco Caminhos passam a receber a MESMA coisa no nível 7.** Bastião e Vanguarda ganhavam um golpe (`11,50`) e os outros três ganhavam um degrau de `7,00` — **uma diferença de `4,50` que ninguém tinha somado.**

**O argumento que aprovava o ataque extra também caiu, e o substituto é mais forte.** Ele era *"a Rotina já é feitiço + Classe 0, então o físico só ganha o espelho"*. Agora é **ninguém está acima da régua**: conjurador `94`, físico `106`, Rotina `108`.

### Adicionado — duas checagens no `conferir-manual.py`, com seis perturbações

**4e — a Rotina reconstrói** como o meio entre as duas colunas vizinhas, lidas do `.docx`. *Com contra-teste: a leitura velha tem de dar diferente da Rotina, senão a checagem aprovaria as duas ao mesmo tempo.* **Ela dá diferente nas sete Classes.**

**4f — a coluna do conjurador da peça 6** contra o feitiço sozinho do manual, mais o vão positivo e crescente. *A regra aplicada e o limite de design ficaram separados de propósito.*

**As seis perturbações, numa cópia isolada, com a base conferida antes e o `diff` conferido em cada uma:**

| perturbação | resultado |
|---|---|
| devolver o conjurador `99` no nível 30 | acendeu |
| fazer o vão encolher | acendeu |
| repor a frase morta numa linha viva | acendeu |
| a mesma frase num bloco de citação | **verde** — nota histórica não pode falhar |
| mexer na contagem de dados da Rotina no `.docx` | acendeu |
| sumir com a tabela do Classe 0 | acendeu |

> **A guarda da frase morta nasceu errada e foi consertada.** A primeira versão varria o arquivo inteiro e acendia na nota histórica que o próprio conserto escreveu. **Hoje ela é por linha: bloco de citação é história, linha normal é afirmação viva.** *Um vermelho pelo motivo errado ensina a procurar o defeito onde ele não está.*

> **E ela achou uma segunda cópia da frase, na §3.1, que eu não tinha visto lendo:** *"o **único** argumento que aprova o ataque extra é que a Rotina já é feitiço + Classe 0"*.

### Aplicado — a permissão do `Arremate`, e o `Coro` herda

*Decidido na v0.79 e não aplicado.* **A frase da peça 6 §3.1 — *"eles não passam a ter três ataques"* — foi reescrita, com o motivo do Mizuki e o número dele:**

> *"o Emanador já tem pouca vida, ele ter dano é o mínimo."*

**Com Constituição 3 no nível 30 o Emanador chega a `212` de vida, contra `243` da Vanguarda e `305` do Bastião — `87%` e `70%`.**

**E a tabela que sustentava a proibição não reconstruía de nada.** A coluna *"somar o golpe"* publicava `21 · 55 · 90 · 127`, e o `127` aparecia **uma vez só no repositório inteiro**, sem script e sem validador. *Terceiro andar do mesmo defeito: a v0.60 achou a coluna errada, a v0.72 achou o piso lido como teto, e a v0.80 achou que o número nunca reconstruiu.*

**⚠ E medindo nível a nível apareceu o que o `DESENHO-trilhas` não tinha visto: o pior nível não é o 30.**

| nv | físico | `Arremate` | acima do físico |
|---|---|---|---|
| **11** | 50 | 60 | **+20%** |
| 18 | 78 | 89 | +14% |
| 30 | 106 | 118 | **+11%** |

*Aquele bloco mediu `+10%` no nível 30 e fechou ali — e o 30 é o mais favorável dos quatro.* **A causa é de escala:** o feitiço cresce `13 → 94` e o golpe simples cresce `9 → 12`. **Declarado e não consertado; o conserto barato é mover o ataque extra do nível 11 para o 19.**

**O `Coro` herda, e nele a permissão custa `0%` em dano** — o teto de uma Rotina somada da seção 4 já segura a saída. *O que ele ganha é uma rolagem a mais, e rolagem a mais é alcance, tipo de dano e alvo, que o teto não mede. É a lição do eixo errado, declarada em vez de consertada.*

### Alterado — o nível 7 do Emanador: a `Voz Grossa` morreu e virou o `Resquício`

> **`Resquício`.** Ao conjurar na Ação Padrão um feitiço **que não causa dano**, você pode lançar um **feitiço de Classe 0 na Ação Bônus**.

**A `Voz Grossa` morreu duas vezes.** *Ela dizia "o seu Classe 0 passa a causar o mesmo que um golpe simples".* **Uma:** no nível 30 isso rebaixa o Classe 0 de `27` para `12`. **Duas, e é pior:** na rodada em que o Emanador lança o feitiço grande **não existe Classe 0 nenhum** para melhorar.

**O `Resquício` não sobe o pico — ele levanta o chão da rodada de controle**, que sai de zero de dano para `27`. *Ele entrega o vão quando o Emanador controla em `44%` das rodadas, e a taxa é número de playtest.*

> **Ele é impossível de abusar por construção:** para usar o botão você abre mão do feitiço de dano, e a rodada de controle faz `27` contra `94`. **O pico do Emanador continua `94` em qualquer montagem.**

**Decisão do Mizuki: o empate do nível 7 se mede na MÉDIA por rodada, e não no pico.** *Preço declarado: o Emanador termina `12` de dano por rodada atrás do físico na melhor rodada dele.* **A alternativa que fechava o pico** — Classe 0 na bônus sempre, causando metade — dava `107,5` contra os `106` do físico, e perdia a metade que recompensa controle.

**O nome passou pela triagem.** `Faísca` morreu (está dentro de `Faísca em Cadeia`), `Sobra` e `Troco` saíram fracos. **E o `Transbordo` saiu `LIVRE` e foi recusado por colisão de sentido:** ele é a mesma figura da `Torrente` com outra palavra.

### Alterado — o `Arremate` repreçado, e o nível 27 dele ficou vago

| nv | fatias antes | **agora** |
|---|---|---|
| 2 | 0,00 | 0,00 *(é o vão, e o vão é `12`)* |
| 11 | 2,26 | **2,36** |
| 19 | 1,38 | 1,38 |
| 27 | 1,38 | **0,00** |
| **total** | **5,02** | **3,74 — abaixo da banda** |

**O nível 27 vale `0,00` e agora dá para provar:** trocar um ataque por um Classe 0 vale `+15` — `27` contra `12` — e fazer o Classe 0 causar o mesmo que um golpe simples vale `−15`. *O texto daquele bloco já dizia "a troca vale `0,00` em dano"; o que faltava era o número dos dois lados.*

**Sobram `1,26` fatia, que são `6,40` de dano por rodada.**

### O raio de alcance — medido errado DUAS vezes, e o Mizuki achou as duas

**A primeira medição somou o Classe 0 novo em cima de cada entrega, uma por vez.** *Lição nº 7: um preço se mede somado, nunca sozinho.*

**A segunda montou a rodada inteira e supôs que a Ação Padrão era conjuração nas três — e ela não é.** *Achado do Mizuki, com o texto das Trilhas na mão: "essas classes são quase todas marciais, a pessoa não vai usar feitiço no turno".* **Ele estava certo em duas de três, e a terceira ele errou para o lado que importa.**

| Trilha | Ação Padrão | Ação Bônus |
|---|---|---|
| `Arremate` | **atacar** com a arma do grupo | conjurar Classe 0 a 7 |
| `Brasa` | **atacar** (socos) | Classe 0 — Classe 2 no nível 19 |
| `Estocada` | **conjurar** | golpe de arma — mais um Classe 0 no nível 27 |

**A `Estocada` é o espelho, e é a única das três que põe um Classe 0 numa rodada que já tem o feitiço grande inteiro.**

### As rodadas de pico, montadas slot a slot no nível 30

| Trilha | a rodada | dano | da Rotina | acima da base do Caminho |
|---|---|---|---|---|
| `Arremate` | 2 golpes `23` + Classe 7 na bônus `94` | **117,00** | +8,3% | **4,53 fatias — dentro da banda** |
| `Estocada` | Classe 7 `94` + golpe `11,5` + Classe 0 `27` | **132,50** | +22,7% | **5,31 fatias — 6% acima** |
| `Brasa` — `Fornalha` | 3 socos `34,5` + 3 Classe 0 `81` | **115,50** | +6,9% | **1,97 fatia — fraca** |

> **Nada quebrou, e o `Arremate` cai exato dentro da banda de `4,50` a `5,00`.** *A `Estocada` estoura `6%`, que é menos de um terço do estouro do `Punho` que já está aceito desde a v0.74.*

> ***Decisão do Mizuki: fica assim, e é esperado e calculado.*** *"O único que realmente sai fraco aqui é a `Brasa`, mas ela está no Caminho que é para ser tank mesmo."* **Ele vai testar e dar retorno.**

### ⚠ O aviso que fica junto, e ele é de texto e não de número

**A peça 6 nunca escreveu se a Ação de Atacar de um físico inclui o golpe canalizado.** Ela publica a linha `canalizado + golpe simples` como a rodada do físico, e nunca disse em que ação isso acontece.

| a `Brasa` no nível 2, se a Ação de Atacar… | a rodada dá |
|---|---|
| …**inclui** o canalizado | `94 + 11,5 + 27` = **132,50** |
| …**não inclui** | `11,5 + 11,5 + 27` = **50,00** |

**Fator de `2,6×` numa entrega publicada, decidido por uma frase que ninguém escreveu.** *É o mesmo buraco que a v0.66 fechou para o `Arremate` e o `Coro` — "esta seção sempre disse 2 ações e nunca disse quais" —, e para o Bastião e a Vanguarda ele continua aberto.*

**Isso é a primeira coisa a olhar no playtest**, e é mais barato de responder na mesa do que na conta.

### Em aberto

- **⚠ A peça 6 nunca escreveu se a Ação de Atacar de um físico inclui o golpe canalizado**, e essa frase decide a `Brasa` por um fator de `2,6×`. *Primeira coisa a olhar no playtest.*
- **A `Estocada` está `6%` acima da banda** e fica, no mesmo molde do estouro do `Punho`.
- **Nenhum validador lê a regra de ouro nº 6**, e ela é a que segura quantos feitiços cabem num turno.
- **⚠ Duas decisões de nível 7 foram tomadas contra o vão errado, e as duas viram.** *Marcadas no `DESENHO-caminhos.md` e não desfeitas.*
  - **Guia:** *"`Ajudar` de bônus mais o golpe preso ao `Guiar` estouram"* — `5,75 + 5,75 = 11,50` contra um vão de `12`. **Cabem, com `0,50` de sobra.**
  - **Evocador:** a `Coleira` foi cortada de `metade da maestria` para `+1` fixo na v0.71, porque `10,80` estourava um vão de `7`. **Contra `12` ela cabe.**
- **⚠ O teto que a régua de Trilhas usa ficou pendurado.** O `RASCUNHO-trilhas.md` §3 mede tudo contra *"o `+18%` sustentado que a peça 6 §3.1 reprovou"*, em quatro lugares — **e a v0.80 mostrou que aquele `+18%` não reconstrói de nada e que a montagem que ele media deixou de ser proibida.** *A régua que preçou as onze Trilhas está medindo contra um teto que não existe mais.*
- **O nível 27 do `Arremate` está vago**, com `1,26` fatia. *A ficção é o capstone do Mahito — dentro do domínio ele deixa de precisar tocar.*
- **A taxa de controle do Emanador** decide o `Resquício` inteiro, e ela é número de playtest.
- **O ataque extra do `Arremate` está em `+20%` sobre o físico no nível 11**, contra `+11%` no 30.
- **Todo número que se mediu contra o vão de `7,00` precisa ser refeito.** *Só o nível 7 do Emanador foi nesta versão. O `DESENHO-caminhos.md` inteiro e o §3.4 do `RASCUNHO-trilhas.md` esperam.*
- **O `Repertório`** — a última do Emanador, e ela precisa liderar em posicionamento ou recuperação.
- **`condição` continua sem conversão** e **gastar PE continua sem preço.**
- **Atribuição de versão continua sem validador.**
- As de sempre: as vagas de Desliga, a Cicatriz, o clash, o nome do sistema, o refino que paga mal no marco, a tabela de inimigo.

---

## [0.79] — 2026-08-16

**O Emanador ganhou o nível 7 do Caminho e duas das três Trilhas** — a `Torrente` fechada em `5,37` e o `Arremate` escrito em `5,02` e **deixado aberto de propósito**, porque ele contradiz uma frase da peça 6. *E três coisas que eu ia afirmar de cabeça estavam erradas: a atribuição da `Energia Reversa` em doze lugares, o alcance da cerca das Melhorias, e a base da sobretaxa de PE.* Continuam dezesseis peças e dezesseis validadores.

### Corrigido — a `Energia Reversa` estava atribuída à v0.77 em DOZE lugares

*Ela fechou na v0.78, e a entrada do topo do CHANGELOG é a dona disso.* **Seis arquivos discordavam dela**, e nenhum validador alcança atribuição de versão.

| arquivo | o que dizia |
|---|---|
| `ESTADO-ATUAL.md` | *"fechou na v0.77"*, *"continua sendo aptidão não escrita"*, *"está na lista de aptidões pendentes"* |
| peça 11 | duas linhas com *"saiu na v0.77"* |
| peça 13 | *"já está na lista de aptidões pendentes"* |
| `CHANGELOG`, entrada da v0.77 | *"Fechada nesta versão, na peça 11"* |
| `DESENHO-trilhas.md` | quatro: *"nunca foi escrita"*, *"aptidão não escrita"*, *"ainda não tem casa"*, *"não tem casa"* |
| `conferir-aptidoes.py` | o rótulo do bloco: `A APTIDAO Energia Reversa — v0.77` |

**A causa tem nome: a v0.77 teve DOIS commits com a mesma etiqueta.** *Lido do `.git/logs/HEAD`, que é texto puro e não precisa rodar git.* A entrada foi reescrita no segundo, e o esboço da aptidão virou *"fechada"* antes de ela ter casa. **O `conferir-repositorio.py` confere o número da versão em onze cópias; ele não confere em que versão cada coisa fechou.**

> **A entrada da v0.77 foi corrigida e não apagada**, com a lista das seis cópias que herdaram o erro escrita nela.

### Feito — a checagem da `Modelagem` contra o Fundamento, pendente desde a v0.71

**A `Modelagem` é a tabelinha do Feiticeiro — metamagia. E o manual já vende metamagia inteira: são as Melhorias.** As tabelas 30 a 40 trazem `Longe` (degrau de alcance), `Mais Um` (um alvo a mais), `Rápido` (Ação Bônus em vez de Padrão), `Reação`, `Silencioso` (sem gesto e sem palavra) e `Rajada`. **Cada uma é um item de metamagia com outro nome, e são `67` no total.**

| a leitura | vale no nv30 | do vão de `7` |
|---|---|---|
| **como PRESENTE** — uma Melhoria **Leve** de graça | **`21,60`** | **`309%`** |
| **como TROCA** — trocar uma Melhoria paga por outra de custo igual ou menor | **`0,00`** | `0%` |

*O `21,60` é a `Precisão`, a Melhoria mais barata que serve para dano.* **É o mesmo `21,60` que reprovou a `Arquearia` na v0.76 e o `+2` de acerto no menu do `Elo` na v0.77 — a mesma parede, por três portas.**

### Decidido — o nível 7 do Emanador, com a `Modelagem` de carona

> **`Voz Grossa`:** o seu Classe 0 passa a causar o mesmo que um golpe simples. `7,00`, o vão exato.
> **`Modelagem`:** ao conjurar um feitiço **de dano ou de condição**, troque uma Melhoria que ele já tem por outra de custo igual ou menor. **A troca não mexe na condição**, e o requisito da Melhoria que entra continua valendo.

**A versão recusada punha um Classe 0 na Ação Bônus, e aquele slot é onde a `Torrente` nasce.** *Com a `Voz Grossa` fechando por magnitude em vez de por slot, a ação bônus ficou livre.*

**As travas da `Modelagem` são duas do Mizuki e uma da conta.** Ele cercou por assunto — *"vai dar dor de cabeça"* —, e ao contar o menu apareceram mais duas que precisavam sair pelo próprio texto: **`11` de `67` ficam fora**, e as duas que a conta pegou são a **`Inescapável`**, que proíbe o feitiço de ter qualquer outra peça, e o **`Efeito Próprio`**, cujo custo é *"o mestre decide"* — **troca livre para Melhoria de custo aberto é o filtro multi-mestre falhando de propósito.** Sobram `54`, que é `81%` do menu.

> **E as duas metades do degrau se separam para o `Arremate`**, que recebe o ataque extra no lugar do degrau do vão e ficaria sem a `Modelagem`. *Como ela vale `0,00`, ela é do Caminho inteiro e só a metade numérica varia.*

### Adicionado — a `Torrente`, `5,37` de `5,00`

| nv | a entrega | fatias |
|---|---|---|
| **2** | **`acelerar`**, `2×` por cena, sobretaxa `Classe e meia` de PE. Teto do outro feitiço: `Classe 0` | *(a base)* |
| **11** | o teto vira **metade da sua maior Classe** | **3,78** |
| **19** | o `acelerar` **não gasta carga** quando você não torra | 0,10 |
| **27** | a metade **arredonda para CIMA** | **1,49** |

**A escada cai da própria regra.** *Cruzando `metade da maior Classe` com a tabela 5 do manual, o teto dá `0 · 1 · 2 · 3` — e o `Classe 3` só existe do nível 21, porque é lá que a Classe 6 libera.* **A sobretaxa também não foi escolhida:** o `Rápido` do manual é Melhoria **Pesada**, e a coluna `Pesada` da tabela 81 dá `11` num Classe 7.

**O nível 27 é uma linha de texto e é o degrau mais caro.** O projeto arredonda sempre para o lado que não te favorece; **inverter isso num lugar só é exceção legível**, e ela não oscila — do nível 27 ao 30 a maior Classe é sempre `7`.

> **Uma rodada de pico custa `44` de PE, e o pool de `180` cobre `1,1` luta.** *Você torra uma luta inteira no dia e entra na segunda com o bolso vazio, que é exatamente a ficção.*

### Achado — o projeto sabe preçar GANHAR PE e não sabe preçar GASTAR PE

**Ganhar tem preço e ele fecha:** o nível 11 da `Brasa` dá `2` de energia temporária e está publicado em `1,01` fatia; o câmbio da peça 5 diz que `1` PE por rodada vale `5,14` de dano, que é `1,01` fatia. **Bate exato.**

**Gastar não tem preço em lugar nenhum** — nenhuma das nove Trilhas fechadas tem entrega cujo custo seja PE. E aplicar o câmbio ao contrário quebra: a `Torrente` ganha `35,50` de dano e gasta `9` PE, o que dá `−10,76` — **um botão que obviamente serve pontuando negativo.**

> **O motivo é de construção:** o câmbio de `5,14` foi derivado dos próprios feitiços, que rendem `4,4` a `4,5` de dano por PE. **"Gastar PE para ter dano" é zero por definição — é o que toda ficha já faz.** *O ganho da `Torrente` não é converter PE em dano; é furar o teto de quanto PE cabe numa rodada.*

### Corrigido — a cerca das Melhorias é do CAMINHO, e eu apliquei ela à Trilha

*Eu afirmei em conversa que toda entrega de Trilha esbarra numa das `67` Melhorias.* **A peça 5 §4 diz literalmente "seis coisas que um CAMINHO nunca dá", e as Trilhas publicadas já dão efeito de Melhoria à vontade:** o `Muro` dá terreno difícil (`Terreno`), o `Perímetro` dá vantagem a aliado (`Ecoa`), a `Pegada` rerrola dado de dano. **A Trilha é limitada pelo orçamento de fatias, não pela cerca.** *A checagem da `Modelagem` continua valendo, porque ali era Caminho mesmo.*

### Adicionado — o `Arremate`, `5,02` de `5,00`, e ele fica ABERTO

**O desenho é do Mizuki, e ele inverteu a Trilha:** em vez de conjurar na padrão e bater na bônus, **bate na padrão e conjura na bônus.**

| nv | a entrega | fatias | coluna |
|---|---|---|---|
| **2** | grupo de arma, treino, atributo mental — e um **feitiço de Classe na bônus** ao atacar com aquela arma | **0,00** | *é o vão* |
| **11** | **ataque extra** | **2,26** | ação/alvo |
| **19** | `maior Classe` de **PV temporário** ao conjurar colado | **1,38** | defesa |
| **27** | trocar um ataque por um **Classe 0**, e o Classe 0 vira do tamanho do golpe | **1,38** | ação/alvo |

**O nível 2 dele já estava escrito na peça 6**, que manda a Trilha de corpo a corpo de um Caminho não-marcial conceder o treino marcial — *"treino de arma não é dado de dano, é acesso"*. **Ele chegou nisso sem ter lido a linha.**

> **⚠ E é por isso que ela não fecha.** A rodada de pico é `Atacar 2×` mais um Classe 7 na bônus: **`117,00`, com três rolagens**, contra os `106,00` do físico — **`+10%` acima do guerreiro.** *E a peça 6 §3.1 proíbe por nome: "eles não passam a ter três ataques."*
>
> ***Decisão do Mizuki: permitir*** — *"o Emanador já tem pouca vida, ele ter dano é o mínimo."* **Falta aplicar**: reescrever aquela frase com o motivo, e decidir se o `Coro` herda. **Decisão registrada não é decisão aplicada.**

**O gate de condição foi testado e reprovado com número.** Um feitiço de condição no Classe 7 ainda causa `45` — a `Condição Maior` come `11` dos `21` pontos —, então a rodada com gate faz `68` contra os `98,50` de um Emanador que só conjura. **`31%` abaixo: ninguém usaria o modo que a Trilha existe para abrir.** *Na `Estocada` o mesmo gate funciona porque lá ele abre um bônus; aqui ele seria a porta do modo principal.*

### Em aberto

- **O `Arremate` contradiz a peça 6 §3.1.** A permissão está decidida e não aplicada, e o `Coro` está no mesmo balde.
- **O `Repertório`** — a última do Emanador, e ela precisa liderar em **posicionamento** ou **recuperação**, que são as duas colunas vazias do Caminho. *E não existe régua para converter "uma aptidão a mais" em fatia.*
- **`condição` continua sem conversão**, e ela travou o `Arremate` duas vezes nesta versão.
- **Gastar PE não tem preço**, e a `Torrente` foi preçada por ritmo para contornar.
- **Atribuição de versão não tem validador**, e ela divergiu em doze lugares nesta versão.
- **`Modelagem` encosta em `montagem`**, que é palavra do manual. *A triagem deu `LIVRE`; ela não pega colisão de sentido.*
- As de sempre: as vagas de Desliga, a Cicatriz, o clash, o nome do sistema, o refino que paga mal no marco, a tabela de inimigo.

---

## [0.78] — 2026-08-16

**A `Energia Reversa` deixou de ser esboço e virou peça.** *Ela estava pendente desde a v0.27 — cinquenta e uma versões — e era a última dependência aberta do Guia: o nível 2 da `Sutura` apontava para uma aptidão que não existia.* Continuam dezesseis peças e dezesseis validadores.

### Adicionado — a aptidão `Energia Reversa` entrou na PEÇA 11, com validador

*Pendente desde a v0.27. Ela era a última dependência aberta do Guia — o nível 2 da `Sutura` apontava para uma aptidão que não existia.*

> **`Energia Reversa` · Classe Passiva 3 · refino 7 e nível 13**
> **Ação padrão. Gaste até `maior Classe` de PE e recupere `1d8` de vida por PE gasto, em você.**

**Nenhum número é escolha minha.** A seção 7 daquela peça já mandava medir contra a Passiva `Recomposição` — `5 × maior Classe`, **`35` no nível 30**. O câmbio de PE existe (*"`+1` PE por rodada `= 5,14` de dano"*), cura é dano evitado e a régua converte `1` pra `1`, então **`1` PE vale cerca de `5` de cura**. E o manual já cura em dado: *"cada ponto que sobra vira `1d8`"*. **No teto são `7d8 = 31,5` contra os `35` da Passiva** — mesma altura, e a diferença é que esta cobra PE e se repete.

**O gate é o mesmo da `Extensão de Domínio` e não foi escolhido por simetria.** No material, energia reversa nasce no cérebro e não no intestino, e o difícil é sustentar dois fluxos ao mesmo tempo. *A Classe Passiva 3 com refino 7 é a altura que a seção 5 reserva para o que quase ninguém alcança: o generalista só chega no nível 26.*

**Ela cura VOCÊ. Quem cura os outros é a `Sutura`, no degrau do 11** — porque curar terceiro é a parte rara do material, e o Gojo não consegue.

**Seis checagens novas no `conferir-aptidoes.py`, com cinco perturbações conferidas e um contra-teste.** Ela confere o gate no título, o gate contra o da `Extensão de Domínio`, a cura no teto contra a `Recomposição`, que o refino não entra na fórmula, que a linha do catálogo da seção 10 repete o gate do título, e que ela saiu da lista das que faltam — que caiu de quatro para três.

> **Uma perturbação acendeu pelo motivo errado e foi consertada.** Enfiar `refino` na fórmula quebrava o regex e disparava *"não consegui ler o dado de cura"* em vez da checagem de refino. **Vermelho pelo motivo errado ensina a procurar o defeito onde ele não está** — é a mesma família do aviso que a v0.38 aposentou.

### Em aberto

- **Se `Energia Reversa` limpa Sequela.** *A peça 1 §5.5 pediu isso quando o `Caído` entrou na v0.37 — "a aptidão não foi escrita; quando for, este é o primeiro lugar que ela encosta".* **Agora ela foi escrita, e a pergunta ficou.** Ela é da peça de dano e condições, junto da Cicatriz.
- **Barreira Simples, Cortina e a régua da Aptidão Própria** — as três que sobraram da lista da seção 7.
- **Emanador e Evocador** — seis Trilhas, e o `Servo` publicado está na escala velha e reprova.
- **O engarrafamento de Reação do Guia**, medido na v0.77 e não resolvido.
- **Faltam nomes** para as doze entregas do Guia, as três do Bastião e o catálogo da `Pegada`.
- As de sempre: as vagas de Desliga, a Cicatriz, o clash, o nome do sistema, o refino que paga mal no marco, a tabela de inimigo.

---

## [0.77] — 2026-08-16

**A matriz da Vanguarda fechou e o Guia inteiro fechou junto** — Caminho preçado e as três Trilhas em `4,78` · `4,51` · `4,74`, com matriz limpa. *E três números que eu ia chutar já existiam escritos: o preço do rerroll em duas peças, a fatia do Teste de Resistência no manual, e a âncora de cura na peça 11.* Continuam dezesseis peças e dezesseis validadores.

### Alterado — a divisão por coluna do `Batedor`, refeita a partir de linha publicada

**Nenhum script gerou os números originais das três rotas.** Eles foram calculados numa passada anterior e só o total de cada entrega ficou escrito — então a divisão por coluna não existia para ser lida. Ela teve de ser reconstruída.

Três peças saem de linha que já estava publicada: o `+3 m` do nível 2 do `Yumi` vale `0,35` pela mesma linha que o `Punho` usa duas vezes, o empurrão da `Besta` vale `0,71` pela linha `+6 m sempre`, e um degrau de margem crítica vale `0,05` — que é o próprio nível 19 do `Yumi`, publicado sozinho. *A escalada entra a zero, no molde do `treino` do `Servo`: utilidade sem preço em dano.*

**Duas saíram por subtração, e é aí que estava o risco:** *"sem desvantagem na faixa longa"* em `1,13` e *"sem desvantagem colado"* em `0,44`.

> **A conferência de fora fecha exata, e ela não é circular.** O nível 19 da `Besta` é empurrão mais colado, e está publicado em `1,15`. As duas parcelas vêm de lugares diferentes — o empurrão da linha `+6 m` e o colado do `1,57` que o documento publica para as duas taxas de previsão — e somam `0,71 + 0,44 = 1,15`. **Nenhuma das duas foi tirada dali.**
>
> *E a terceira bate junto:* o nível 2 do `Fogo` menos o colado deixa `0,10` a `0,15` para *"recarrega só no `1` natural"*, que é o tamanho certo para meia chance de recarga forçada.

### Adicionado — a matriz, com o `Batedor` em três linhas

| | ação/alvo | defesa | posicionamento | recuperação | total |
|---|---|---|---|---|---|
| `Estocada` | **4,58** | 0,00 | 0,00 | 0,00 | 4,58 |
| `Executor` | 2,84 | **1,84** | 0,00 | 0,00 | 4,68 |
| `Batedor` · `Yumi` | 4,46 | 0,00 | 0,35 | 0,00 | 4,81 |
| `Batedor` · `Besta` | 3,82 | 0,00 | **0,71** | 0,00 | 4,53 |
| `Batedor` · `Arma de Fogo` | **4,74** | 0,00 | 0,00 | 0,00 | 4,74 |

**Três linhas e não uma, e isso não é escolha de formato.** A rota se escolhe no nível 2 e vale a campanha inteira, então `Yumi` e `Besta` são duas fichas diferentes — e a dominância pergunta se **uma ficha** ganha da outra em tudo. Uma linha média não responde isso.

Das vinte comparações, uma dispara: `Arma de Fogo` sobre a `Estocada`, por `0,16` fatia e razão `1,03×`. **É a declarada da v0.75.** O `Executor` é o único da Vanguarda com coluna de defesa, e a `Besta` leva posicionamento com folga de `2,0×` sobre o `Yumi`.

### Achado — o `4,74` da `Arma de Fogo` é o PISO da rota, não o valor dela

Duas das quatro entregas dela são faixa e não número: o nível 2 vale `0,54` a `0,59`, e o `Quick Draw` vale `1,17` com o Rifle de Precisão e `1,89` com a Metralhadora Pesada. **O total publicado usa o fundo das duas.**

**No topo das duas a rota soma `5,51` fatias — `10%` acima da banda de `4,50` a `5,00`.**

> **Não cria dominância nova** — a Metralhadora continua sem ganhar do `Yumi`, da `Besta` e do `Executor`, que têm coluna que ela zera. **O que ela enfraquece é o argumento de "ruído"** que sustenta a dominância declarada: contra a `Estocada` a diferença vai de `0,16` para `0,93` fatia, que são `4,72` de dano bruto por rodada — quase **seis vezes** os `0,81` medidos na v0.75.
>
> *A v0.75 mediu o espalhamento do `Quick Draw` entre as armas — `1,6×`, dentro do filtro de `3,0×` — e não o total da rota com ele dentro.* **A decisão de deixar o `X` de balas variar é do Mizuki e continua de pé**; o que faltava era somar o efeito dela na rota inteira.

### Achado — duas somas de `0,01` que não fecham

As quatro entregas do `Yumi` somam `4,81` contra um total publicado de `4,82`; as da `Besta` somam `4,53` contra `4,52`. **É arredondamento das entregas, não erro de conta** — mas é a mesma casa de defeito que o `4,80` contra `4,87` do `Muro`, duas ordens de grandeza menor. A matriz usa a soma das entregas.

### Achado — a `LISTA-gatilhos-trilhas.md` estava na escala VELHA, e dois vereditos dela viram

*Aberto o Guia, a primeira coisa que ele pede é a régua de gatilhos. Ela estava medindo com a fatia de `1,27` contra um orçamento de `5,07` — a camada de vínculo do Evocador, fechada na v0.68.* **A v0.73 dobrou o orçamento duas vezes: hoje a fatia é `5,08` e a Trilha leva `25,40` de dano por rodada, `5,01×` mais.** O documento foi revisado na v0.74 e a escala não foi junto.

**Ele não dizia em que escala estava, e a prova é interna:** ele publica *"exceção de ação = `17,0` fatias"* ao lado de *"mínimo `21,60`"*, e `17,0 × 1,27 = 21,59`. Com a fatia de hoje daria `86`. *Segunda prova, independente: a seção do `Servo` mede contra `5,07`, que é `4 × 1,27`.*

**As taxas não se movem** — elas são fração, não valor. As quatro famílias de gatilho, o piso de `20%` e o filtro de `3,0×` ficam exatamente como estavam. **O que muda é toda coluna em fatias, e com ela dois vereditos que estavam sendo tratados como fechados:**

**1 — `exceção de ação` deixava de caber em qualquer Trilha, e passa a caber.** De `426%` do orçamento para `85%`. *E a Vanguarda já provava isso sem ninguém cruzar: o nível 19 da `Estocada` é exceção de ação a `100%`, publicado em `2,46` fatias desde a v0.75.* **A trava do Evocador não cai junto** — *"a `Matilha` e o `Servo` não podem receber ação"* volta a ser regra da matriz, escrita à mão. **O que a conta segurava de graça, agora alguém precisa segurar.**

**2 — `duração` volta ao permitido, e ela é o eixo em que o `Elo` foi desenhado.** A v0.68 expulsou duração com *"no melhor caso ela ainda é onze vezes uma entrega"* — e as onze vezes eram onze fatias de `1,27`. Hoje, `+1` rodada num efeito de cinco custa `4,25` fatias permanente, `2,13` com gate de acerto e `1,28` uma vez por descanso curto. **Só o efeito de duas rodadas continua fora**, e por motivo próprio: dobrar o que dura duas rodadas é dobrar a coisa.

**E o achado mais forte daquele documento se inverteu inteiro.** Ele dizia que só posicionamento cabia como entrega **permanente**, e daí concluía que a forma *"três permanentes e um botão"* do `Servo` **não era construível**. Na escala de hoje cabem **cinco de seis**, e três mudaram de veredito. *A parede era de escala, não de estrutura.*

> **A seção do `Servo` daquele arquivo NÃO foi convertida, e é de propósito.** O `Servo` publicado precisa ser refeito e não reajustado. O que ela existe para mostrar — que os `15%` do nível 27 saíram de subtração e não de gatilho nenhum — é achado de método, e método não tem escala.

### Adicionado — a família `golpe simples para um ALIADO`

Ela nunca esteve na lista de gatilhos e existe desde a v0.72, cortada do nível 7 do Guia por não caber no vão de `7` daquele degrau.

**O botão já entra descontado porque o golpe é de outra pessoa:** `11,50 × 50%` de o aliado acertar `= 5,75`. *Mesmo número que o `DESENHO-caminhos.md` usou; ele não se moveu.* Contra os `25,40` de uma Trilha ele é **`1,13` fatia, `23%`, permanente** — e `0,57` com gate de acerto.

> **Isso não é a família `exceção de ação`, e a diferença é o que faz caber.** Dar uma **ação** a um aliado custa `29,19`, que é `115%` da Trilha. O golpe simples é um quinto disso.
>
> ***Decisão do Mizuki: ação inteira fica fora do Guia; o golpe simples entra.*** *E ele lembrou certo — o que o Caminho recusou no nível 7 foi o golpe simples, não a ação; a ação já tinha sido recusada numa linha separada.*

### Adicionado — o Caminho do Guia, preçado contra as `3` fatias

*Até aqui só o nível 7 dele tinha preço, e ele nem é das três fatias: é o degrau do **vão**, que a peça 6 §3.1 dá de graça.* **Dois dos outros três passaram a ter.**

**A base sai do próprio `DESENHO-caminhos.md`:** o `Ajudar` de ação bônus está preçado em `5,75` dando `25` pontos percentuais, então **`1` pp numa rolagem de aliado vale `0,230`** de dano por rodada. *E ela fecha sozinha — se `25%` de uma ação de atacar de aliado valem `5,75`, aquela ação vale `23,00`, que é exatamente dois golpes simples de `11,50`. No nível 30 o aliado tem ataque extra. A conta reproduz uma coisa que não foi posta nela.*

| degrau | dano/rodada | fatias | % das `3` |
|---|---|---|---|
| nv2 `Guiar` — `15` pp | `3,45` | **0,68** | 23% |
| nv7 `Mão na Roda` | `5,75` | *1,13* | **fora — pago pelo vão** |
| nv15 `Puxar a Linha` — `9 m` | `5,40` | **1,06** | 35% |
| nv30 `Ninguém Cai` | **?** | **?** | **não reconstrói** |

**O `Ninguém Cai` não tem preço, e não é falta de tentar.** Ele anula o excedente e deixa o aliado com `1` de vida — **o que ele compra não é dano evitado**, é não cair, não pegar Sequela e não virar morte em definitivo. A régua converte `1` pra `1` **pontos de vida**, e aqui o ponto de vida é literalmente um. *Mesmo balde da Cicatriz: é da peça de dano e condições.*

> **Sobram `1,26` fatia, e esse número é TETO e não valor.** Ele é subtração. **Escrever ele como preço seria o `15%` do `Servo` pela terceira vez.**

> **E a dívida não é do Guia: nenhum dos cinco Caminhos foi preçado contra as `3` fatias dele.** O Bastião tem a mesma linha desde a v0.74. **Com dois de três derivados, o Guia virou o mais adiantado dos cinco.**

### Adicionado — a ficção das três Trilhas do Guia, e as âncoras vieram de levantamento

*No método da v0.69: ficção primeiro, sem olhar orçamento, o Mizuki revisa, e só depois o lote é preçado.*

| Trilha | âncora no material | o que ela é |
|---|---|---|
| **`Elo`** | **Utahime Iori**, `Solo Forbidden Area` | amplifica a energia e a saída de quem está no alcance; vira ritual com encantamento, gesto, dança e música, e chega a `120%` |
| **`Sutura`** | **Shoko Ieiri** | Energia Reversa **nos outros**, que é a parte rara — o Gojo cura a si mesmo e não terceiro |
| **`Perímetro`** | **Kirara Hoshi**, `Love Rendezvous` | marca com estrelas do Cruzeiro do Sul; o que tem a mesma estrela se atrai, e chegar em algum lugar passa a exigir a rota que a técnica deixou |

> **A âncora do `Elo` teve CORREÇÃO OFICIAL depois de publicada, e ela muda o desenho.** O capítulo saiu dizendo que a Utahime amplificava **um** feiticeiro; a VIZ publicou correção e o certo é **qualquer feiticeiro no alcance, vários ao mesmo tempo**. *É literalmente o terceiro eixo que a peça 6 dá ao `Elo` — "duração, alcance, **quantos alvos**" — e ele estava errado na primeira leitura da fonte. **Foi a busca por retcon que pegou, não a busca pela técnica.***

**A cerca do Caminho é mais estreita que a dos outros dois, e ela é escrita:** o Guia é o único sem rota para ataque extra, então **Trilha do Guia não dá golpe para você.** E o Caminho já ocupa quatro botões — ajudar rolagem, `Ajudar` de bônus, mover um aliado, impedir a queda —, então as três ficam fora desses quatro. *A separação do `Perímetro` contra o `Puxar a Linha` está escrita: o Caminho move um aliado, a Trilha muda o que o chão cobra. Mesmo eixo, botão diferente.*

### Adicionado — as três do Guia em mecânica, `4,78` · `4,51` · `4,74`, matriz limpa

*A primeira passada foi minha e o Mizuki reprovou quase tudo.* **O que sobreviveu dela foram os números, não as entregas** — as réguas continuaram valendo e foi com elas que a proposta dele foi medida. **Espalhamento de `1,06×` entre as três, o mais apertado de qualquer Caminho até aqui.**

| | ação/alvo | defesa | posicionamento | recuperação | total |
|---|---|---|---|---|---|
| `Elo` | 2,13 | 1,44 | 0,00 | **1,21** | 4,78 |
| `Sutura` | 0,00 | **4,51** | 0,00 | 0,00 | 4,51 |
| `Perímetro` | **4,74** | 0,00 | 0,00 | 0,00 | 4,74 |

### Achado — a fatia do Teste de Resistência saiu do MANUAL, e eu vinha chutando

*Eu usava "um terço", inventado por mim, e ele decidia fatia em três entregas.* **A tabela 24 do manual — a das Formas — tem uma coluna `Como resolve`:** `4` resolvem por Teste de Resistência, `4` são automáticas e `2` por rolagem de acerto.

**São `40%`, e o dono é o manual.** *Toda entrega do Guia que mexe em TR passou a medir por esse número.* **Foi a segunda vez nesta versão que um número que eu ia chutar já existia escrito** — a primeira foi o preço do rerroll.

### Achado — `rerroll` já tinha dono em DUAS peças

A peça 11 §8 escreve que *"rerrolar e dar vantagem valem os mesmos `+25` pontos percentuais"*, e a peça 13 repete. **Rerroll não é mecânica nova — é vantagem, ou desvantagem, com outro nome.**

**E isso derrubou metade da proposta na hora.** *Rerroll de aliado* vale `25` pp `= 5,75`, que é **o número exato do `Ajudar`** do Caminho nível 7 — e o Caminho já tem **dois** ajudadores de rolagem de aliado. ***Decisão do Mizuki: fica, mas só em rolagem que não é ataque.***

### Adicionado — a linha de preço de `alcance`

Alcance a mais poupa, no máximo, o deslocamento que alguém gastaria para chegar lá — então ele **teta em `0,60` de dano por rodada por metro**, a linha `posicionamento +3 m` dividida por três. *Nenhuma das três finais usa, mas ela fecha a lacuna que o bloco do `Batedor` abriu.*

### Registrado — a cascata do menu do `Elo`, e ela parou no segundo degrau

*Pedido do Mizuki: testar `+2` restrito a arma ou a feitiço, cair para `+1` se não coubesse, e só então mudar de ideia.*

| a opção | fatias | |
|---|---|---|
| `+2` de acerto, só **arma** | **4,25** | **reprova — 85% da Trilha** |
| `+2` de acerto, só feitiço | 2,13 | |
| `+1` de acerto, só **arma** | **2,13** | **passa** |
| `+1` de acerto, só feitiço | 1,06 | |

> **Restringir não corta pela metade, e o motivo é estrutural:** *um canalizado é **um** ataque por turno e a arma são **dois** no nível 30.* A rota `arma` vale o dobro da rota `feitiço`, o jogador escolhe arma, e o `+2` continua sendo os `4,25` da `Arquearia` que a v0.76 já reprovou com este número exato.
>
> **E Defesa e TR tiveram de sair do menu** — `3,2×` e `8,0×` atrás do topo. **O menu fecha porque virou menu de uma coisa só.**

### Alterado — a `Sutura` virou uma escada de teto, e isso responde a pergunta dele

*A primeira versão dava a Energia Reversa cheia no nível 2, e ela sozinha valia `67%` da Trilha: uma entrega e três decorações.* **Decisão do Mizuki: cortar** — e a pergunta que veio junto foi *"não sei o que pôr nesse nível 2 que remeta ao `Sutura`"*.

**A resposta é que a Trilha inteira é a resposta.** O teto de PE por uso sobe `2 → 4 → 7`: no nível 2 você costura pouco e só em você, no 27 você costura sete pontos em qualquer um e não erra ponto. **O nome virou a mecânica.**

*E a escada segue a fonte: curar a si mesmo é raro, curar os outros é muito mais raro — o Gojo não consegue. Por isso a parte rara chega no degrau do 11 e não no do 2.*

> **O nível 27 cruza com uma linha publicada.** Rerrolar `1` e `2` no dado de **dano** é a `Arma Grande` da `Pegada`, em `0,33` fatia. No dado de **cura** a mesma mecânica deu `0,52`. *Mesma família, mesma casa.*

### Adicionado — o esboço da aptidão `Energia Reversa`

> **Classe Passiva 3 · refino 7 e nível 13. Ação padrão: gaste até `maior Classe` de PE e cure `1d8` por PE gasto, em você.**

**Cada peça sai de coisa publicada.** A peça 11 §7 mandava medir contra a Passiva `Recomposição` — `5 × maior Classe`, `35` no nível 30. O projeto tem câmbio de PE (*"`+1` PE por rodada `= 5,14` de dano"*), então `1` PE vale ~`5` de cura. E o manual já cura em dado: *"cada ponto que sobra vira `1d8`"*. **No nível 30 são `7d8 = 31,5`, contra os `35` da Recomposição** — mesma altura, e esta se repete cobrando PE.

*O gate é o mesmo da `Extensão de Domínio` e casa com o material: energia reversa nasce no cérebro e não no intestino, e o difícil é sustentar dois fluxos ao mesmo tempo.*

### Decidido — a `Sutura` não causa dano

O material oferecia: **Energia Reversa ofensiva é letal a espírito amaldiçoado**, porque energia positiva destrói construção de energia negativa por dentro. Custaria `1,13` fatia.

> ***"Causar dano com Energia Reversa, se vier de Classe, vai ser difícil de balancear em outras fontes."*** **É o mesmo argumento que tirou o dado de dano do Caminho na peça 5 §4**, aplicado a uma fonte nova antes de ela existir.

### Alterado — a ficção da `Sutura` que eu escrevi contradizia a fonte

Eu tinha posto no nível 27 *"você alcança a alma, o dano que ninguém desfaz você desfaz"*. **Energia Reversa não cura dano de alma** — a única exceção é o Sukuna, e só na própria alma, porque ele conhece a forma dela. *Fica riscado no documento em vez de apagado.*

### Registrado — o `Perímetro` só existe por causa de duas frases do Mizuki

Quatro entregas honestas de posicionamento chegavam a `2,94`, porque **cinco fatias são `42` metros negados por rodada** e posicionamento não enche Trilha sozinho. *O `Muro` já provava: `4,16` de defesa contra `0,71` de posicionamento.*

**A marca tinha de pegar Teste de Resistência e não só perícia** — perícia não converte em dano, e como só perícia o nível 19 valia `0,00`. Pegando TR, vale `1,30`. **E a vantagem na brecha sobe o botão `1,5×`.**

> **Só `1×` por rodada cabe na marca, e a conta fecha sozinha.** Com `2×` o degrau vale `2,59` e a Trilha vai a `6,03`; com `3×`, a `7,33`.
>
> **A saída tem de ser voluntária, e a observação MELHORA o número.** A taxa fica entre `15%` e `30%`, o degrau entre `0,25` e `0,51`, **e a banda absorve os dois.** *Primeira vez nesta peça que não preciso fechar uma previsão para publicar.*

> **Duas coisas ficam declaradas e não consertadas.** A Trilha **não passa** a trava *"nenhuma entrega depende de outra"* — o 19 e o 27 penduram no 2 e no 11 —, e isso é o desenho pedido. **E a Trilha do chão terminou com ZERO em posicionamento:** a área de `9 m` é ficção de posição e mecânica de debuff. *Nenhuma das três do Guia tem uma fatia de posicionamento.*

### Em aberto

- **`Energia Reversa` não tem casa.** O que esta versão escreveu foi o **esboço**, dentro do bloco da `Sutura`. Enquanto ela não entrar no catálogo da peça 11, o nível 2 da `Sutura` aponta para o que não existe. *A peça 1 §5.5 também espera por ela.*

  > **Esta linha dizia *"fechada nesta versão, na peça 11"*, e não era verdade.** A aptidão entrou na peça 11 na **v0.78**, com o validador junto — a entrada daquela versão é a dona disso. *Corrigida depois da v0.78, junto com mais cinco cópias que tinham herdado o `v0.77`: o `ESTADO-ATUAL`, duas linhas da própria peça 11, uma da peça 13 e o rótulo do bloco no `conferir-aptidoes.py`.* **A entrada do topo do CHANGELOG é a dona da versão, e foi ela que sobreviveu à conferência** — as seis cópias é que estavam erradas.
- **O engarrafamento de Reação.** O `Ninguém Cai` do Caminho, o `Elo` nível 11 e o `Perímetro` nível 11 querem a mesma Reação. *Dentro de cada Trilha não colide; entre Trilhas, na mesma mesa, colide.* **É o defeito que matou a primeira versão do `Executor` na v0.75, num slot diferente.**
- **`condição` continua sem conversão.** Só a exaustão tem magnitude escrita, e o nível 11 da `Sutura` carrega o resto quase de graça.
- **Uma previsão segura a `Sutura` inteira:** *"o curandeiro cura em metade das rodadas"*. Ela é multiplicador dos quatro degraus, e não tem dono.
- **Faltam nomes para as doze entregas do Guia.** Nenhuma passou pela triagem.
- **`Espírito` e `Intelecto` são nomes de Teste de Resistência, não de atributo.** *Apareceram na conversa como se fossem; os atributos são Essência e Inteligência.*
- **O nível 2 da `Estocada` continua sem coluna, e agora com tamanho.**
- **O catálogo da `Pegada`**, cinco entradas e duas abaixo do teto de `0,79`. *Junto com as treze `Manhas` de arma.*
- **Faltam nomes** para o empurrão do `Punho`, o espaço do `Muro` e a energia temporária da `Brasa`.
- **Emanador e Evocador** — seis Trilhas, e o `Servo` publicado está na escala velha e reprova.
- **A tabela de inimigo** continua parada até as seis fecharem.
- As de sempre: as vagas de Desliga, a Cicatriz, o clash, o nome do sistema, o refino que paga mal no marco.

---

## [0.76] — 2026-08-16

**O `Executor` fechou, e o que destravou ele foi achar que eu estava cobrando `50%` a mais por PV temporário.** *Três números meus caíram nesta versão, e nos três quem desconfiou primeiro foi o Mizuki.* A Vanguarda está com as três Trilhas escritas. Continuam dezesseis peças e dezesseis validadores.

### Achado — PV temporário vale `1` de dano evitado, e eu cobrava `1,50`

O `1,50` sai de cruzar duas linhas do manual: a Forma `Apoio` diz *"cada ponto que sobra vira 3 de vida temporária"* e o glossário diz *"cada ponto que sobra vira 1d8"*, que é `4,5`.

**Aquela é a moeda de montar feitiço. A moeda da fatia é dano por rodada, e as duas não se convertem uma na outra.**

**Quem prova é o `Alicerce`, publicado desde a v0.73:**

| | evita por rodada | publicado | dano por fatia |
|---|---|---|---|
| 1 tipo | 3,39 | 0,67 | **5,06** |
| 2 tipos | 6,78 | 1,33 | **5,10** |
| 3 tipos | 10,17 | 2,00 | **5,08** |

A fatia é `5,08`. **O projeto converte dano evitado `1` pra `1`, sem multiplicador** — e vale para PV temporário, resistência e redução igualmente.

> **O erro custou uma proposta.** Com `1,50`, a entrega de nível 11 do `Executor` custava `2,75` fatias e eu escrevi ao Mizuki que ela não cabia, oferecendo três jeitos de cortar a fórmula dele. Ele recusou os três e mandou manter. **Com a régua certa ela custa `1,84` e cabe com folga.**
>
> ***"Eu to achando que você encareceu a reação, valide de novo por favor."*** *Foi a terceira vez na mesma passada que ele desconfiou de um número meu, e a terceira em que a conta deu razão a ele.*

> **E uma armadilha de leitura na mesma tabela:** `Fluxo | 2` na lista de Passivas **não** quer dizer *"custa 2 pontos"*. **A coluna é `Classe`** — `Fluxo` é Passiva de Classe 2, que custa dois espaços de feitiço. *Cheguei a escrever que o manual tinha duas réguas de PV temporário. Tem uma só.*

### Achado — Reação de ataque de oportunidade vale `75%`, não `100%`

Eu tinha preçado *"quando alguém bate colado em você"* como permanente. **A tabela de inimigo do manual diz que não é.**

No nível 30 o chefe faz `72` de dano por rodada e o capanga `38`, e o próprio manual escreve que o chefe *"perde a ação três vezes por rodada"* contra um grupo de quatro. Isso dá **`1,0` a `1,5` ataque colado por rodada em você** — e **você só tem uma Reação**, então o que importa é a chance de pelo menos um chegar: entre `63%` e `78%`.

**`75%` é o meio da banda, e por acaso é a mesma taxa do `Engate`.** A entrada caiu de `2,26` para `1,70` fatia.

### Achado — *"contanto que você erre algum ataque"* custa igual a *"quando você acerta"*

Com dois ataques a `50%`, errar pelo menos um dá `75%`. Acertar pelo menos um dá `75%`. **É o mesmo número.** Um gatilho de fracasso parece restrição e não restringe nada — a `LISTA-gatilhos` já mandava declarar contra quantos ataques a entrada está medida, e isso vale para os dois lados da moeda.

### Adicionado — o `Executor`, `4,68` de `5,00` fatias

| nv | a entrega | fatias |
|---|---|---|
| **2** | **`Pegada`** — escolha um estilo da lista | 0,79 *(teto do menu)* |
| **11** | **`Aprumo`** — ação bônus, `1d10 + atributo` de PV temporário, `metade do atributo` usos por descanso curto | **1,84** |
| **19** | **`Revide`** — Reação: ataque de oportunidade em quem bate colado, acertando ou errando | **1,70** |
| **27** | **`Retomada`** — rerrolar uma rolagem de ataque errada, `maestria` vezes por dia | 0,35 |

**A forma inteira é do Mizuki**, e ela chegou nesta conversa como conserto de uma versão que somava `7,25` — *"mover a ação bônus com PVT para o nv11, a reação para o 19 e excluir o efeito do nv19 antigo"*. **O efeito velho do nível 19 dava vantagem se você tivesse gasto a ação bônus**, e sozinho ele custava até `5,24` fatias. Era ele o estouro.

**O relógio da `Retomada` é por dia, e isso não é preferência.** Por descanso curto ela custa `0,85` e **o contador não aperta**: numa luta de `3,7` rodadas você tem erro para rerrolar em `2,8` delas, e tanto `4` usos quanto `3` passam disso. *Só com o relógio longo a escolha entre `maestria` e `metade do atributo` passa a mudar alguma coisa — `0,35` contra `0,26`.*

**Os quatro nomes passaram pela triagem.** `Estilo` saiu **DENTRO** de `Estilo da Sombra` e virou `Pegada`; `Guarda` e `Firmeza` saíram `OCUPADO`, as duas Melhorias do manual. *E `Manejo`, que saiu `LIVRE`, foi recusado por sentido: ele fica ao lado da `Manha` que o Caminho da Vanguarda dá no mesmo nível 2, com o mesmo assunto e o mesmo começo de palavra.*

### Adicionado — a lista da `Pegada`, e uma regra que caiu da conta

| estilo | pede | dá | fatias |
|---|---|---|---|
| `Duelista` | uma arma numa mão, a outra vazia | `+2` de dano em todo golpe | 0,79 |
| `Arremesso` | arma arremessada | `+2` de dano em todo golpe | 0,79 |
| `Desarmado` | punho vazio | `+metade da maestria` no soco | 0,79 |
| `Defesa` | vestindo `Traje` ou `Revestimento` | `+1` de Defesa | 0,67 |
| `Arma Grande` | arma de duas mãos | rerrolar `1` e `2` no dado de dano | 0,33 |

> **Todo estilo tem de pedir alguma coisa.** Um estilo sem porta está disponível para toda ficha e domina qualquer estilo mais barato — o jogador pega o de cima e pronto. *Foi por isso que a `Defesa` ganhou o uniforme como porta: sem ele ela dominava a `Arma Grande` por `2,0×`.*

**E `Arquearia` não existe neste sistema.** O estilo do 5e dá `+2` no acerto, e aqui um ponto de acerto vale `10,80` de dano por rodada — **`4,25` fatias, `85%` de uma Trilha inteira numa linha de menu.** Cortado pela metade ainda custa `2,13`. *É a mesma parede que o `+1` no acerto encontrou quando foi proposto como entrega de nível 2.*

### Alterado — dois erros de conta no `DESENHO-trilhas.md`, achados de passagem

**1. A linha do `Muro` na matriz de dominância não somava.** As colunas davam `4,81` contra um total publicado de `4,87`. A célula de defesa dizia `4,10` e as três entregas defensivas dele somam `4,16`. **As linhas do `Punho` e da `Brasa` fecham exatas.**

**2. A tabela *"Os números que decidiram"* carregava a régua VELHA de resistência.** Ela cobrava `1,67` pelo primeiro tipo e `0,83` pelo segundo — o modelo de `50%` e depois `25%` do dano recebido, de antes de a lista de tipos de dano existir. **O `Alicerce` sempre esteve preçado pela nova**, em `1,33` pelos dois tipos. *Diferença de `1,88×` no mesmo botão, dentro do mesmo arquivo.*

### Em aberto

- **A matriz da Vanguarda não fecha.** A `Estocada` e o `Batedor` foram preçados **sem separar as entregas por coluna** — os totais existem, a divisão não. *O Bastião só ganhou matriz porque as doze entregas dele declararam a família de cada uma.* **As sete entregas daqueles dois precisam de coluna antes de a Vanguarda fechar.**
- **O catálogo da `Pegada`** tem cinco entradas e duas abaixo do teto. *Do mesmo tamanho das treze `Manhas` de arma que o Caminho da Vanguarda deve desde a v0.70.*
- **O `Revide` contra o `Não Acabou`:** o degrau de nível 30 do Caminho **devolve a Reação** ao derrubar um alvo, então contra turba o `Revide` dispara mais de uma vez por rodada. *Não medido — ele só morde no cenário oposto ao que esta Trilha faz.*
- **Falta nome** para o empurrão do `Punho`, o espaço do `Muro` e a energia temporária da `Brasa`.
- **Guia, Emanador e Evocador** — nove Trilhas, e o `Servo` publicado está na escala velha e reprova.
- **A tabela de inimigo** continua parada até as nove fecharem.
- As de sempre: as vagas de Desliga, a Cicatriz, Energia Reversa, o clash, o nome do sistema, o refino que paga mal no marco.

---

## [0.75] — 2026-08-16

**A `Estocada` fechou, e o nível 2 dela — que é a identidade inteira da Trilha — custa zero fatia.** *E uma dominância que eu tinha marcado como defeito virou declaração, porque ela é meio por cento.* Continuam dezesseis peças e dezesseis validadores.

### Adicionado — a `Estocada`, e o nível 2 dela custa ZERO

**`4,58` de `5,00` fatias**, e a identidade inteira da Trilha está num degrau que não custa nada.

> **Conjurar na ação padrão e bater na bônus com o grupo de armas escolhido** — e naquele grupo o acerto e o dano usam **Essência ou Inteligência**, com o requisito de Força continuando de pé.

**Ela não ganha dano: ela muda o ataque de lugar.** A base do físico é `canalizado 94 + golpe 12,5 = 106,5`; a `Estocada` é `feitiço 94 + golpe 12,5 = 106,5`. **O que ela compra é o que a Vanguarda perdia** — quem quer usar a técnica dela perde todos os ataques da rodada, porque Conjurar gasta a ação padrão. *E o que ela paga é a ação bônus.*

**Três propostas caíram no caminho, cada uma contra uma regra que já existia:**

| a proposta | por quê |
|---|---|
| *"conjurar deixa de exigir largar a arma"* | conjurar **não exige mão livre** aqui — quem exige é a Restrição `Gesto`, que é escolhida e **devolve pontos**. Cancelar de graça é `Melhoria de graça` pela porta dos fundos |
| *"ao conjurar, um golpe simples de bônus"* | **é o ataque extra do nível 7 com outras palavras** — a base já é `canalizado + golpe simples` |
| *"o canalizado sai pela arma"* | dado de dano no Caminho. A v0.15 já mediu: `+135%` no nível 2 |

> **E o nível 19 traz uma família de gatilho que a lista não tem.** *"Quando o feitiço da padrão é condicional"* é **o único gatilho do projeto controlado inteiramente pelo jogador** — não é rolagem, relógio, estado da ficha nem julgamento do mestre. **A `LISTA-gatilhos` precisa de uma quinta família.**

### Registrado — a dominância entre `Arma de Fogo` e `Estocada` fica DECLARADA

A rota `Arma de Fogo` sai com `4,74` de ação/alvo contra os `4,58` da `Estocada`, e as duas têm zero nas outras colunas — ela ganha em tudo que a matriz mede.

**Medida antes de tratada, e ela é ruído:** `0,16` fatia, que é `0,81` de dano bruto por rodada e **0,55%** do que o personagem faz. Razão de `1,03×` contra um filtro de `3,0×`, e um terço da largura da própria banda de escrita.

> **A matriz não tem piso, e o defeito é dela.** O teste é binário — *"maior ou igual em todas, maior em uma"* —, então `0,16` dispara exatamente como `3,00`. **O projeto já tem o mecanismo:** o `conferir-equipamento.py` carrega dominâncias **aceitas e declaradas** desde a v0.47, as três da `Versátil`.
>
> ***Achado do Mizuki: "como assim Estocada tá incompleta? tá bão já uai."* Ele estava certo, e eu tinha escrito "precisa de conserto" para uma diferença de meio por cento.**

### Em aberto

- **O `Executor` é a única das três da Vanguarda que não fechou.** Ele soma `7,25` contra `5,00` — estoura em 45% —, e o problema maior nenhum preço pega: **três entregas brigam pela mesma ação bônus.** O nível 2 quer gastá-la em PV temporário, o nível 19 só dá vantagem se você gastou nela, e o nível 27 quer atacar com ela. *Do nível 27 em diante, atacar apaga as outras duas.*
- **A `LISTA-gatilhos` precisa de uma quinta família:** gatilho que o jogador controla inteiramente. *Achado escrevendo o nível 19 da `Estocada`.*
- **`PV temporário` tem conversão no manual e ninguém tinha visto:** a Forma `Apoio` diz *"cada ponto que sobra vira 3 de vida temporária"*. **É a régua que o `Executor` precisa**, e ela já existe.
- **Os metros de cada arma de projétil**, com a âncora nomeada — `Projétil`, 18 m.
- **Duas taxas de posição são previsão** — quantas rodadas na faixa longa e quantas colado. Juntas decidem `1,57` fatia do `Batedor`.
- **A tabela de inimigo**: `+38,3%` e não `36%`, e ela fica parada até as Trilhas que faltam serem preçadas.
- As de sempre: as vagas de Desliga, a Cicatriz, Energia Reversa, o clash, o nome do sistema, o refino que paga mal no marco.

---

## [0.74] — 2026-08-15

**O soco não tinha dado escrito em documento nenhum, e a Trilha inteira do Bastião estava preçada contra uma arma que ninguém estava segurando.** *Três conversões erradas caíram nesta versão, e duas delas vinham se cancelando havia versões.* Continuam dezesseis peças e dezesseis validadores; a peça 14 e a peça 1 ganharam uma checagem cada.

### Achado — o `Engate` era preçado contra `1d10 + Força`, e ele dá um golpe DESARMADO

O `11,50` que a Trilha usava é a linha de comparação da **peça 5 §2**, e ela é *"arma `1d10` + Força"*. **O punho vazio não tinha dado em lugar nenhum.** O `Corpo Duro` dizia *"o seu ataque desarmado conta como arma"* e a única mão do catálogo é a `Manopla`, que é equipamento **vestido** — e o mesmo degrau dizia *"sem empunhar nada"*.

> **Pergunta do Mizuki que achou: "por que caralhos ela bate 6,09? Calculamos pra ser 5, mas mesmo assim não acho que o punho tá forte."** *As duas metades estavam certas.*

### Decidido — o soco sobe com a maestria, e ele é a única entrada sem categoria e sem propriedade

*Ideia do Mizuki: **"minha ideia era ser igual D&D pra monge, mas servindo pra todos os feiticeiros"**. **Peça 14 §5.0.6**, com a checagem 11 do `conferir-equipamento.py` e cinco perturbações conferidas.*

| maestria | níveis | dado | gasta | fundo de uma mão |
|---|---|---|---|---|
| 1 | 2 a 9 | `d4` | 0 | `3` abaixo |
| 2 | 10 a 17 | `d6` | 1 | `2` abaixo |
| 3 | 18 a 25 | `d8` | 2 | `1` abaixo |
| **4** | 26 a 30 | **`d10`** | **3** | **exato** |

**Zero propriedade é o que balanceia, e foi o Mizuki que apontou isso** — *"contando como se fosse de nenhum grupo, tendo nenhuma propriedade, isso q balanceia ele"*. **A régua do §5.0.1 fecha exata em cima disso**: o dado custa `d4 = 0 · d6 = 1 · d8 = 2 · d10 = 3`, o fundo de uma mão é `3`, e zero propriedade custa zero. **O soco nasce dominado e chega à paridade no fim, sem nunca passar dela.**

> **E o `d12` que a ideia original pedia não cabe:** ele custa `4` e só existe em duas mãos, e o soco não tem uma segunda mão para vender. *Nenhuma edição do monge faz `d4` até `d12`: a de 2014 anda `d4·d6·d8·d10` e a de 2024 anda `d6·d8·d10·d12` — as duas andam quatro degraus consecutivos, e `d4` até `d12` são cinco em quatro faixas de maestria.*

**A `Manopla` continua viva, e é isso que prova a régua.** `Soqueira` e `Tekko` são `d4` com `Vestida`·`Oculta`·`Par` e fecham `3/3` iguaizinho — **as duas entradas gastam o mesmo orçamento e compram coisas opostas.** *Sem esta seção elas morriam na maestria 2, porque arma vestida perdendo para não vestir nada é dominância estrita.*

**E o `Corpo Duro` perdeu a primeira linha**, que virou regra de todo feiticeiro. **O Caminho não perdeu nada que fosse dele** — a peça 5 §4 proíbe Caminho de dar dado de dano, e agora ele não precisa: o dado nunca foi dele.

### Achado — a vantagem valia `16` pontos percentuais nos documentos de trabalho, e a peça 11 diz `25`

O `16` é a linearização: `E[maior de 2d20] − E[d20] = 3,325`, vezes `5` pp por ponto de d20. **Ela só vale longe do meio da curva.** Com acerto em `50%`, `1 − (1 − 0,5)² = 75%` e o ganho é **`25` pp** — a peça 11 escreve isso na tabela do Limiar e as peças 13 e 14 repetem. **Erro de 8,4 pp, e ele subestima a vantagem em 56%.**

### Achado — o gatilho *"quando você acerta"* foi cobrado a `50%`, e o Bastião tem ataque extra

A fatia mede no **nível 30**, e lá a ação de atacar tem dois ataques: a chance de pelo menos um acertar é `75%`. **E o mesmo documento já usava dois ataques três linhas abaixo**, ao escrever que a vantagem do nível 27 *"só dispara em um quarto das rodadas — você precisa acertar os dois"*.

> **Os dois erros vinham se cancelando.** O `Engate` publicava `1,13`, que é `11,50 × 0,50`; o certo é `soco × 0,75`. **Dado grande demais vezes gatilho pequeno demais dá um número que parece bom**, e é assim que uma conta errada sobrevive a uma revisão.

**A `Brasa` do nível 19 era a exceção e estava certa:** aquela entrega abre mão do ataque extra, então lá o `50%` é o número certo.

### Alterado — a `LISTA-gatilhos` se contradizia, e faltava uma palavra

Ela aprovava *"quando você acerta"* a `50%` e três linhas depois proibia multiplicar botão por gatilho de rolagem. **A regra é sobre a MESMA rolagem:** gatilho que é o próprio acerto que o botão já embute não multiplica; gatilho que é **outra** rolagem, anterior, multiplica — e o soco de bônus rola o próprio dado depois. **E a taxa não é fixa: um ataque dá `50%`, dois dão `75%`, três dariam `87,5%`.**

**E o `3,3` rodadas dela citava a peça 15 §3.2, que não fala de duração de luta.** A dona é a **peça 1 §8**, com `3,4` a `4,0`. *O `3,3` tem origem: `1050 ÷ 315` na tabela de inimigo do manual, que é o **piso** da faixa de chefe lido como valor típico. Piso-lido-como-outra-coisa pela terceira vez na mesma linhagem.*

### Achado — a subida de `36%` da tabela de inimigo estava errada, e ela NÃO foi aplicada

O `36` é o `+35,8% da Rotina` copiado com a base trocada: a base de antes era `98%` da Rotina, não `100%`. **Com a base certa dá `+38,3%`** — e o modelo reproduz o *"3,7 para 2,7 rodadas"* que a v0.73 escreveu.

**Mas `+38,3%` é teto e não valor.** Ele supõe que as `8` fatias inteiras viram dano, e a matriz do Bastião diz que não viram: o `Muro` põe `0,00` em ação/alvo, e o Caminho do Bastião inteiro é defesa e controle. **Um grupo de `Muro` estica a luta em vez de encurtar.** E a decisão nomeava **duas** colunas quando a tabela tem **três** que se mexem — *"Dano do grupo por rodada"* é a saída dos jogadores e sobe junto.

> **Fica parada até as nove Trilhas que faltam serem preçadas**, porque só aí a média do grupo é computável. O dono declarado daquela tabela é o playtest, e `04-playtest/` continua vazia.

### Achado — a rota que reprovava *"uma ação a mais"* pelo preço deixou de reprovar

A v0.70 fechou o piso de taxa de `20%` com este argumento: *"uma ação a mais passa a custar `17` fatias contra um orçamento de `4` e reprova sozinha — a trava que hoje é escrita à mão cai da conta."*

**A fatia quadruplicou depois disso e o preço em dano por rodada não mudou.** Espremida no piso, a ação a mais sai de **425% para 85%** do orçamento de uma Trilha — **ela cabe agora.** *Ninguém decidiu isso; foi efeito colateral de dobrar a fatia duas vezes em dois dias.* **A decisão não muda** — a peça 6 §3.1 reprova pelo mecanismo — **mas a segunda rota até ela se perdeu, e o texto passa a dizer isso** em vez de continuar prometendo que o preço resolve.

### Adicionado — o que a v0.73 decidiu e não escreveu

| onde | o que entrou |
|---|---|
| `RASCUNHO-trilhas.md` §3 | a fatia de **`5,08`**, `3` fatias de Caminho e `5` de Trilha, e o achado da trava circular |
| `RASCUNHO-trilhas.md` §3.6 | a trava do botão reescrita, com a segunda forma — **condicional que gasta recurso do turno** — e o contra-teste |
| peça 5 §4 | a **terceira forma de exceção estreita**, a tabela de exemplos reconvertida para a escala `5,08`, e o soco em duas linhas |
| **peça 1 §8.1** | os **catorze tipos de dano em três grupos**, em guarda provisória até a peça de dano e condições existir, com a checagem 10 do `conferir-atributos.py` e seis perturbações |

### Alterado — o Bastião reprecado, e o estouro é decisão do Mizuki

| | antes | agora |
|---|---|---|
| `Muro` | 4,87 *(a tabela de travas dizia 4,80)* | **4,87** |
| `Punho` | 4,85 | **6,09 — estoura 22%** |
| `Brasa` | 4,84 | **5,03** |

> **Decisão do Mizuki: fica.** *"Mesmo com esse estouro, não vai quebrar o balanceamento da mesa — a maioria das habilidades são situacionais e de RP."*
>
> **A conta discorda em parte, e a discordância fica escrita:** das cinco peças do `Punho`, **quatro disparam quase toda rodada**, e a única de fato situacional é o `Tropel`, que vale `0,35` fatia. **O que joga a favor:** o estouro é só do `Punho`, a média das três é `5,33`, e **a matriz continua limpa** — cada Trilha lidera numa coluna diferente.
>
> **Uma alteração foi testada e revertida a pedido dele:** o `Engate` exigindo acerto nos dois ataques. Ela passa em todas as travas — taxa de `25%` contra um piso de `20%` — e **corrige demais**: devolve `2,26` fatias quando só `1,09` sobravam, e joga o `Punho` para `3,82`, abaixo do piso da banda.

### Registrado — dois números que não reconstroem de lugar nenhum

**O `Derrubado` do nível 11 do `Punho` vale `1,71` fatia — 28% da Trilha — e não sai de nenhuma linha publicada.** As outras cinco peças daquela Trilha eu refaço do zero. *É o defeito do `15%` do `Servo` outra vez: número que ninguém reproduz é número que saiu da subtração.*

**E o `4,32` do `Ajudar` no `DESENHO-caminhos.md` também não.** *Marcados, não consertados por adivinhação.*

### Adicionado — a regra de alcance, e ela pagou uma dívida escondida à vista

**A peça 14 declarava `Longo Alcance` como *"número em metros"* e nenhuma das onze armas de tiro tinha metro escrito** — e a propriedade **já custava 1 ponto**, porque *"o topo fica um ponto abaixo da `Pesada` porque ele paga o `Longo Alcance`"*. **O catálogo inteiro pagou por uma regra que ninguém tinha escrito.**

> **Peça 14 §5.2.1, no formato do hobby por decisão do Mizuki:** faixa normal até o `Longo Alcance` da arma, **faixa longa até o dobro com desvantagem**, e nada além. **E a terceira faixa é do outro lado:** atacar com projétil **estando adjacente a um inimigo** também é desvantagem.

**As duas pontas são a mesma régua e o mesmo tamanho** — desvantagem vale `−25` pontos percentuais, que é metade do dano, e o número é da peça 11. *Perto demais e longe demais custam igual.*

**Os metros de cada arma ficam de fora, com a âncora nomeada:** a Forma `Projétil` do manual alcança `18 m`, e a peça 15 já lê dela a amarra da invocação. *Onze números seriam catálogo, e catálogo se faz de uma vez com a régua na mão.*

### Adicionado — o `Batedor`, e as três rotas resolvem a posição por portas diferentes

**`Yumi` `4,82` · `Besta` `4,52` · `Arma de Fogo` `4,74`**, de um orçamento de `5,00`. **Espalhamento de `1,08×`** contra um filtro que reprova em `3,0×`.

| rota | como ela resolve a posição |
|---|---|
| **`Yumi`** | ignora a desvantagem da **faixa longa** — atira de onde ninguém alcança |
| **`Arma de Fogo`** | ignora a desvantagem de estar **colado** — atira de dentro do aperto |
| **`Besta`** | não ignora nenhuma: ela **empurra** o inimigo para fora do problema |

### Achado — o golpe canalizado é Forma `Toque`, e o `Batedor` não canaliza

O manual põe `Toque` em **1,5 m** e `Projétil` em `18 m`. **Então a rodada de um atirador é `18,0` a `23,0` de dano bruto no modo Atacar, contra `94,0` do modo Conjurar** — e o modo Conjurar não tem ataque de arma nenhum, porque gasta a ação padrão.

**Toda peça de uma Trilha de arma à distância vive no modo que vale 21% do outro.** *A `Estocada` conserta isso no nível 2 dela; o `Batedor` não conserta em lugar nenhum, e é ele que mais precisa.*

### Achado — o `1` natural da recarga vale, e o tamanho sai do X

*O Mizuki não aceitou o zero que eu tinha escrito, e ele estava certo.*

| X | recargas por rodada com `1–2` | com só o `1` | em fatias |
|---|---|---|---|
| 2 | 1,053 | 1,026 | **0,00** |
| 3 | 0,738 | 0,701 | 0,04 |
| 4 | 0,582 | 0,539 | 0,05 |

**Com `X=2` ele vale zero mesmo** — o teto de X já força recarga toda rodada e o dado nunca chega a ser o primeiro gatilho. **De `X=3` para cima ele existe.**

> **E a peça 14 tinha previsto isto com data marcada:** *"em Ação Bônus a `Munição` custa zero… isso muda no dia em que o slot encher."* **O `Mirar` no nível 11 é esse dia.** A recarga virou preço de verdade sem ninguém mexer em número.

### Decidido — o `Quick Draw` dispara `X`, e a desigualdade entre armas é aceita

*Decisão do Mizuki: **"não tem problema metralhadora ser 4 e as outras serem 3, tem seus altos e baixos usarem cada arma."*** A Metralhadora Pesada leva `2,34` fatias contra `1,17` do Rifle de Precisão, e **o custo da recarga forçada devolve `0,45` só dela** — o espalhamento fecha em `1,6×`. *A arma de X alto paga em ritmo o que ganha na abertura.*

### Removido — a varredura de lixo

| o que | o que foi feito |
|---|---|
| `_to_delete/v0.73-residuo/` **vazia** | os três arquivos que a v0.73 diz ter movido para lá não estão lá. A pasta é resíduo do resíduo |
| **quatro `.gitkeep` vencidos** | `01-pesquisa`, `02-esqueleto`, `03-mecanica` e `05-material` já têm arquivo. *Eram três na v0.69; `01-pesquisa` entrou na conta* |
| `__pycache__` em `sistema/skills/` | criado ao rodar o `conferir-atributos.py`, e o `.gitignore` já segura |
| o `.gitkeep` de `04-playtest` | **fica** — aquela pasta segue vazia desde a v0.1, e ele é o único que ainda trabalha |

### Em aberto

- **Os metros de cada arma de projétil.** A regra das duas faixas existe; os números não.
- **Duas taxas de posição são previsão:** quantas rodadas um atirador passa na faixa longa, e quantas passa colado. Juntas elas decidem `1,57` fatia do `Batedor`.
- **A tabela de inimigo**, agora com o número certo e o motivo de não aplicar ainda.
- **O peso `60/30/10` dos grupos de dano** continua previsão sem dono — agora com validador guardando o rótulo, para ele não virar número fechado sozinho.
- **Os três degraus do Caminho do Bastião nunca foram preçados contra as `3` fatias.** Com o `Absorver` em `1,60`, sobram `1,40` para o `Puxar Para Si` e o `Segurar`.
- **Vanguarda, Guia, Emanador e Evocador** — nove Trilhas, quatro delas problemáticas.
- **Falta nome** para o empurrão do `Punho`, o espaço do `Muro` e a energia temporária da `Brasa`.
- *`Soco` sai **fraco** na triagem — a uma letra de `Sono`, que é Tema. Ele fica como palavra comum em prosa, minúsculo e sem crase de termo, que é como a peça 5 §4 já o usava antes desta versão. **Se um dia virar termo batizado, ele morre na mesma régua que matou `Emenda` e `Postura` na v0.73.***
- As de sempre: as vagas de Desliga, a Cicatriz, Energia Reversa, o clash, o nome do sistema, o refino que paga mal no marco.

---

## [0.73] — 2026-08-15

**O orçamento de Caminho e Trilha dobrou de novo, e o que destravou foi achar que a trava que segurava era circular.** *A v0.72 reprovou `3×` e `4×` medindo contra o `+18%` da peça 6 §3.1 — e foi a própria v0.72 que escreveu que aquele número não é teto de dano.* **As doze entregas do Bastião estão escritas, preçadas e com nome.** Continuam dezesseis peças e dezesseis validadores.

### Achado — a trava que segurava o orçamento media contra ela mesma

A v0.72 listou cinco travas. Rodadas contra `3×` e `4×` o orçamento, **quatro passam**:

| trava | em `4×` |
|---|---|
| a magnitude não vem de ação a mais por rodada | passa |
| a camada não deriva como fração da saída | passa |
| continua acima do piso da peça 14 | passa, com folga maior |
| a fatia continua plana | passa |
| **nível 30 abaixo do `+18%` reprovado** | **reprova — e é a única** |

**O `+18%` é a medida de uma montagem de três ações que a peça 6 recusa pelo mecanismo.** A v0.72 escreveu isso e usou o número como teto na mesma resposta. *Terceira leitura de piso-como-teto na mesma linhagem, e a primeira em que a leitura errada era minha em cima de um achado meu.*

> **Decisão do Mizuki: `4×`, e a fatia vai para `5,08`.** *O argumento dele: "ficar constantemente nessa briga de onde pôr os pontos não vai salvar o projeto, só o limite ao ponto de não conseguirmos construir nada."*

### Decidido — a Trilha leva `5` fatias, e o Caminho fica em `3`

**A camada de Caminho mais Trilha vira `27,7%` da ficha e o físico termina em `+35,8%` da Rotina no nível 30.**

**O teto que não é circular é o pilar 1** — quanto da ficha pode ser Caminho e Trilha antes de a técnica deixar de ser a identidade. *Isso é decisão de design e não conta.*

**O acoplamento que paga: a luta cai de `3,7` para `2,7` rodadas, então a vida de chefe e de capanga sobe `36%`.** É legal porque **o dono declarado daquela tabela é o playtest**, e `04-playtest/` está vazia desde a v0.1. As outras duas tabelas do manual não se movem. **Decidido e NÃO aplicado.**

### Adicionado — a lista de tipos de dano, e ela é do sistema

*Decisão do Mizuki: os Temas do manual são exemplos para quem cria técnica, não uma taxonomia. **Colisão com Tema é aceita e declarada.***

| grupo | tipos | do dano recebido *(previsão)* |
|---|---|---|
| **Físicos** | `Cortante` · `Perfurante` · `Concussão` | 60% |
| **Elementais** | `Fogo` · `Frio` · `Elétrico` · `Ácido` · `Trovejante` · `Veneno` | 30% |
| **Especiais** | `Radiante` · `Necrótico` · `Psíquico` · `Energia Reversa` · `Alma` | 10% |

**Seis colidem e ficam declarados:** `Fogo`, `Ácido` e `Veneno` são Temas; `Cortante`, `Trovejante` e `Alma` estão dentro de `Passo Cortante`, `Palma Trovejante` e `Toca a Alma`.

**E o palpite do Mizuki reproduziu na conta.** Ele disse *"diria que ocupa 2,0 de fatia se for só contra físicos"*; os três Físicos dão `60%` do dano recebido, que são `10,17` de dano por rodada — **`2,00` fatias exatas.**

### Achado — `Aguentar` já era duas máquinas, e ninguém tinha visto

> **`Aguentar`** — a Reação do Bastião que reduz dano, no `DESENHO-caminhos.md`
> **`Aguentar`** — a escolha a 0 de vida em que você apaga, na **peça 1 §5.5**

**A mesma palavra, duas máquinas, e elas acontecem no mesmo momento de jogo.** *A Reação é o que impede de chegar a 0; a outra é o que acontece ao chegar.* **A Reação virou `Absorver`**, que é a palavra que a peça 6 já usa para descrever aquele degrau.

> **E `Resistir`, que era a sugestão, saiu `LIVRE` na triagem e foi recusado por sentido:** ele poria `Resistir`, `resistência` e `Teste de Resistência` na mesma ficha. **A triagem lê nome contra nome, não sentido — está na skill, e desta vez a skill pagou.**

### Achado — `cair` colidia com o `Caído`, e o conserto era de graça

O `Punho` derrubava alvos com a palavra *"cai"*. **`Caído` é a máquina de 0 de vida da peça 1**, com `Absorver`, `Insistir`, `Sequela` e `Cicatriz` penduradas. **O manual já tem a condição `Derrubado`, com tier de preço e cinco feitiços prontos usando ela.** Trocada a palavra, a colisão sumiu sem custo.

### Adicionado — as doze entregas do Bastião, preçadas de uma vez

**`Muro` `4,87` · `Punho` `4,85` · `Brasa` `4,84`**, contra um orçamento de `5,00` fatias. **Matriz de dominância limpa, com dois contra-testes.** *Nove das doze são permanentes ou ativáveis — o miolo é sempre-ligado e o botão é acessório, que é o que o Stoddard descreve e o inverso do que a v0.72 tinha feito.*

**Quatro nomes passaram pela triagem:** `Absorver` · `Alicerce` · `Engate` · `Tropel` · `Fornalha`. **Dois morreram nela** — `Estalo` é feitiço pronto e `Raiz` é Passiva. **E dois saíram `LIVRE` e foram recusados por sentido:** `Couro` e `Calo` entram na família da `Escama` e da `Casca`, e `Âncora` colide com a amarra da peça 15.

### Decidido — o `Absorver` passa a ter usos iguais à Constituição

*Era `1×` por descanso curto.* **Custa `1,60` fatia das `3,00` do Caminho, e ele deriva `1,97×` para cima** — a Constituição cresce enquanto a magnitude do `Absorver` também cresce. **Fica registrado como limite conhecido**; o equivalente sem deriva seriam `6` usos por dia fixos.

> **E o plano B do Mizuki andava para trás, o que só a conta mostrou:** *metade da Constituição, no descanso longo,* dá `3` usos por dia — e o que existia já dava `3` a `4`.

### Decidido — a trava do botão foi reescrita

> **Antes:** *"pelo menos uma das quatro tem de ser Classe Passiva 2."*
> **Agora:** *"pelo menos uma das quatro tem de ser algo que o jogador decide usar — uso limitado por relógio, **ou condicional que ele ativa gastando um recurso do turno**."*

**Contra-teste rodado:** uma Trilha de terreno difícil, Defesa `+1`, resistência permanente e andar `+3 m` **continua reprovando**. *A trava não virou trivialmente verdadeira.*

### Em aberto

### Registrado — três achados da revisão cética foram FECHADOS pelo Mizuki, e ficam com o motivo

*A revisão levantou seis coisas contra a própria proposta. Três viraram decisão na hora, e o motivo de cada uma vale mais que o achado:*

| o achado | a decisão |
|---|---|
| **o capstone da `Brasa` vale zero contra chefe sozinho** — a `Fornalha` exige um alvo por ataque | **não é defeito.** *"Não é intencional o Bastião dar dano."* O capstone é de turba por desenho, e a saída que daria dano em alvo único — ação completa com Classe 2 em dois socos — foi recusada pelo mesmo motivo |
| **o `Alicerce` com quatro tipos fura a cerca da peça 5 ao pé da letra**, que autoriza *"resistência a um tipo"* no singular | **aceito.** Quatro de catorze tipos não é *"desconto em tudo"*, que é o que a cerca existe para barrar |
| **o `Derrubado` do `Punho` foi preçado por conversão de vantagem, e o manual tem preço próprio** | **não precisa cruzar as duas réguas.** Decisão dele |

### Removido — o resíduo dos documentos de trabalho

**Três arquivos da raiz foram para `_to_delete/v0.73-residuo/`**, porque todo número deles está em escala vencida e um chat novo os leria como vivos:

| arquivo | por que sai |
|---|---|
| `AUDITORIA-trilhas-v0.69.md` | **ele mesmo pedia:** *"depois de decidido, o que sobrar disto vira entrada de CHANGELOG e o arquivo sai."* Fatia `1,27`, calendário de Caminho `7·15·23·29` |
| `DECISOES-pendentes-v0.70.md` | abria com *"nada disto está aplicado"*, e quase tudo está — ou foi substituído. Mesmos números vencidos |
| `PENDENCIAS-bastiao.md` | escrito nesta versão e resolvido nesta versão |

> **É a mesma família do `PROMPT-TRILHAS.md` que a v0.69 achou fingindo estar vivo.** *Documento de trabalho que sobrevive à decisão que ele existia para tomar vira instrução velha para quem chega depois.*

### Em aberto

- **A tabela de inimigo sobe `36%`.** Decidido e não aplicado, e é a maior dívida desta versão.
- **O peso dos grupos de dano — `60/30/10` — é previsão sem dono**, e é o número que decide o `Alicerce` inteiro. *Fica para a próxima conversa, por decisão do Mizuki.*
- **Os três degraus do Caminho do Bastião nunca foram preçados contra as `3` fatias.** Com o `Absorver` em `1,60`, sobram `1,40` para o `Puxar Para Si` e o `Segurar`.
- **Todo número escrito antes desta versão está na escala velha** — o `Servo` do §6.10, os cinco Caminhos, a tabela de exemplos da peça 5 §4.
- **A `LISTA-gatilhos` tem duas linhas que se contradizem**, e o `3,3` rodadas dela cita seção que não fala de rodada. **Ela é o único documento de trabalho da raiz que sobreviveu com número vencido dentro**, e sobreviveu porque a régua depende dela.
- **Nenhum validador alcança os documentos de trabalho da raiz.**
- As de sempre: as vagas de Desliga, a Cicatriz, Energia Reversa, o clash, o nome do sistema, o refino que paga mal no marco.

---

## [0.72] — 2026-08-15

**O orçamento de Caminho e Trilha saiu de um piso lido como teto, e ele dobrou.** *O Mizuki leu o Bastião preçado e escreveu "TA MUITO FRACO, tá tudo muito irrelevante" — a conta deu razão a ele, e o defeito estava na base e não nas entregas.* Continuam dezesseis peças e dezesseis validadores; a pendência nº 6, aberta desde a v0.27, fechou.

### Achado — a fatia inteira vem de um piso, e a régua cobrava ele como teto

O `RASCUNHO-trilhas` §3 escreve, com estas palavras: *"a fatia é `1,27`, e ela sai de dividir **o piso** da peça 14 §4 no nível 30 — `10,14 ÷ 8`"*.

**E a lista de armadilhas do projeto diz:** *"Piso não é teto. Um número registrado como o que a peça **deve** é mínimo, e ler ele como máximo reprova a solução certa."* **Quatro versões cobrando um mínimo como se fosse máximo.**

**Pior: o `10,14` nunca foi "quanto uma Trilha vale".** É a conta da peça 14 de *quanto a Trilha da **Vanguarda** precisa entregar para alguém largar o escudo e pegar arma de duas mãos* — um buraco contábil de uma peça só. Ele foi dividido por oito e virou o orçamento **das quinze Trilhas e dos cinco Caminhos**, sem ninguém decidir isso.

### Achado — e o `+18%` também não é teto. Eu li dois pisos como teto na mesma resposta

Trazendo o espaço disponível, escrevi que *"sobram 12,6 pontos até o teto de `+18%` da peça 6 §3.1"*. **Fui conferir de onde ele sai e ele não é teto:**

| nível | Rotina | somar o golpe (3 ações) | trocar o Classe 0 (2 ações) |
|---|---|---|---|
| 30 | 108 | 127 · **+18%** | 106 · **−2%** |

O texto ao lado daquela tabela diz *"contra o `+18%` que a seção abaixo reprova"*. **É a medida de uma montagem de três ações por rodada que a peça recusa** — e ela recusa o **mecanismo**, escrevendo que *"ação a mais por rodada não tem conserto por preço"*. **Não é espaço; é uma parede com aviso.**

> **Duas leituras de piso-como-teto na mesma resposta, e a segunda foi minha em cima da primeira.** *O Mizuki pediu para eu validar antes de aceitar — "valide minha opinião e se refazer o teto vale a pena" — e foi essa pergunta que achou.*

### Decidido — a fatia dobra para `2,54`, e a pendência nº 6 fecha com ela

*Escolha do Mizuki, com tolerância declarada até `20–21` se as habilidades pedirem.*

**A métrica que decidiu não é a fração da Rotina — é quanto a camada vale do que o personagem REALMENTE faz:**

| | com `1,27` | com `2,54` |
|---|---|---|
| nível 2 | 10,4% | **18,8%** |
| nível 18 | 6,1% | **11,5%** |
| nível 30 | 7,7% | **14,4%** |

**Um Caminho inteiro mais uma Trilha inteira valiam menos de um décimo da ficha.** *A fração da Rotina escondia isso porque ela mede contra a régua e não contra o personagem.*

**A pendência nº 6 — *"a curva de dano deve cruzar a Rotina?"*, aberta desde a v0.27 e marcada como decisão não tomada — fecha em `sim`.** O físico terminava `2%` abaixo da Rotina no nível 30 e passa a terminar em **`+14,6%`**. *Ela estava sendo decidida por dentro do orçamento de qualquer jeito; o que mudou é que agora está escrita.*

> **A trava que vem junto, e sem ela a decisão não vale: a magnitude nunca pode vir de uma ação a mais por rodada.** É o que a peça 6 §3.1 reprova, e é a única coisa que o `+18%` de fato prova.

### Adicionado — cinco travas e um contra-teste, todos rodados

| trava | resultado |
|---|---|
| nível 30 abaixo do `+18%` reprovado | **`+14,6%`** — passa com três pontos de folga |
| a magnitude não vem de ação a mais | passa — a §4 da peça 5 só autoriza exceção estreita |
| a camada não deriva como fração da saída | passa — `18,8%` no nível 2 e `14,4%` no 30 |
| continua acima do piso da peça 14 | passa — `16,5%` contra `9,4%` |
| a fatia continua plana, que é a decisão do §6.9 | passa |

**Contra-teste:** `3×` o orçamento dá `+23%` e `4×` dá `+31%` — **as duas reprovam.** *O teto prático é `21` de dano por rodada, que dá `+17,6%` e encosta no limite — exatamente a banda que o Mizuki declarou de intuição, antes de a conta rodar.*

### Achado — a forma estava errada junto com o número, e isso tem fonte

*Crítica do Mizuki: "precisamos fazer novos meios criativos, outros sistemas não entregam só mecânicas simples e duras."*

**O Brandes Stoddard — o mesmo que o §3.6 já cita para reprovar `1× por dia` — escreve que *"um bônus simples numa rolagem de d20 é raso"*, e que se a mudança principal que a subclasse faz no jogo não é passiva ou à vontade, ela tem limite de uso.** **O miolo tem de ser sempre-ligado e o botão é o acessório** — e eu fiz o contrário, pondo o que interessa em `1× por descanso curto` e deixando o passivo em `+1,5 m`.

*E a Apothecary Press fecha o resto: "features que dependem de uma decisão única e depois viram passivas só fingem conter uma escolha."*

### Alterado

| onde | o que mudou |
|---|---|
| **`RASCUNHO-trilhas.md` §3** | a fatia dobra, com o achado do piso, as cinco travas e o contra-teste |
| **`ESTADO-ATUAL`, pendência 6** | fechada em `sim, cruza`, com a trava do mecanismo |
| **peça 6 §3.1** | aviso de que o `+18%` é reprovação de mecanismo e não teto de dano |
| **`DESENHO-trilhas.md`** | aviso no topo do Bastião: a escala está velha, e as doze correções do Mizuki listadas |
| **`DESENHO-caminhos.md`** | `Elo` → **`Guiar`** no Guia, `Vínculo` → **`Sintonia`** no Evocador |

### Achado — três colisões de nome no desenho da v0.70

A triagem devolveu `OCUPADO` em duas, e a terceira eu tinha criado na v0.71:

| nome | colidia com |
|---|---|
| **`Elo`**, degrau do Guia | **a Trilha `Elo`, do próprio Guia** — mesma ficha, duas coisas |
| **`Vínculo`**, degrau do Evocador | **é Tema no manual**, e a peça 15 já registrava `Vínculo — OCUPADO` |
| `repertório`, família que eu escrevi na §4 | **`Repertório` é Trilha do Emanador** |

*E `Amarra`, que eu ia sugerir, saiu LIVRE na triagem e morreu por sentido: "a amarra são 18 metros" é a coleira da invocação na peça 15.* **A triagem não pega colisão de sentido, e isso está na skill.**

### Adicionado — as seis primeiras Trilhas em ficção, e a regra que apareceu escrevendo

**`DESENHO-trilhas.md`**, com Bastião e Vanguarda escritos a partir do material — Panda, Todo, Choso, Yuta, Toji, Nanami — **sem olhar o orçamento**, que é o método do §7 da auditoria.

> **A regra que o Mizuki fixou:** *sobreposição entre Caminho e Trilha não é problema; **duplicação** é.* Nasceu de um exemplo dele — *"se a pessoa escolhe a rota do Nanami, ela vai querer ser meio off-tank"*.

**Ela pegou duas das seis.** O `Muro`, que a peça 6 descreve com dois terços do Caminho do Bastião — *absorve* é o `Corpo Duro` e *redireciona* é o `Puxar Para Si`. E o `Executor`, onde **eu reescrevi o `Não Acabou` sem perceber**. *As duas foram refeitas, e a saída do `Executor` já estava escrita no `DESENHO-caminhos`: aquele degrau é turba, e "foco em alvo único" estava vago.*

### Achado — três famílias não conseguem ser uma entrega média

*Rodado na escala velha, e o formato do achado sobrevive à mudança de escala.* Espremendo cada família no piso de taxa de `20%`:

| família | do orçamento da Trilha inteira |
|---|---|
| defesa `+2` | 27% |
| acerto `+1` — o seu | **43%** |
| alvo, ou golpe extra | **45%** |

**Quem quiser uma delas gasta quase metade numa linha só.** *E foi a primeira vez que a régua reprovou coisa que não é o `Servo` — antes do piso de 20% ela aprovava oito de oito famílias.*

**E o `Punho` reprovou por FORMATO e não por preço:** com as quatro entregas passivas ele fechava em `3,54` e a régua de preço dava verde. Quem barrou foi a trava da v0.65 — *"pelo menos uma das quatro tem de ser algo que o jogador decide usar"*.

### Em aberto

- **Reescrever as doze entregas do Bastião** na escala nova e com o miolo sempre-ligado. **É a primeira coisa do próximo bloco.**
- **Vanguarda, Guia, Emanador e Evocador** — nove Trilhas em ficção, e quatro delas são as problemáticas.
- **O `Batedor` depende de alcance ter preço, e alcance não tem.** A §4 só mede posicionamento em metros do próprio deslocamento.
- **Todo número de entrega escrito antes desta versão está na escala velha** — o `Servo` do §6.10 inclusive.
- **A `LISTA-gatilhos` e a auditoria precisam da passada de conversão** — o `3,3` sem dono, as taxas de 30% e a família `acerto` que não é linha do permitido.
- As de sempre: as vagas de Desliga, a Cicatriz, Energia Reversa, o clash, o nome do sistema, o refino que paga mal no marco.

---

## [0.71] — 2026-08-15

**A peça 5 §4 deixou de ser lista fechada e virou cerca — e o que fez ela mudar não foi gosto: o desenho dos cinco Caminhos usa oito entregas que ela proibia.** *Duas contas publicadas não reproduziram, e as duas erram do mesmo jeito.* Continuam dezesseis peças e dezesseis validadores.

### Achado — a conversão do projeto é RELATIVA, e dois números publicados leram como absoluta

A cadeia está na peça 15 §3.3: *"+1 no acerto = 50% → 55% = **+10% de dano saído**"*. **Um passo de d20 vale 10% da saída, não 5 pontos percentuais dela** — e a `LISTA-gatilhos` avisa a mesma coisa em outra página: *"dano por rodada já embute os 50% de acerto"*.

| onde | o que dizia | o que a conversão do dono dá |
|---|---|---|
| **`Coleira`**, no `DESENHO-caminhos.md` | `5,40` no nível 30 | **`10,80`** — ela dá `metade da maestria`, que é `2` do nível 26 em diante, e foi preçada com o número do `+1` |
| **`Defesa +1`**, no `DECISOES-pendentes` | `1,70` = `1,34` fatia | **`3,39` = `2,67` fatias** — `5 pp × 33,9` conta o acerto duas vezes |

**A segunda derruba uma conclusão inteira.** Aquele documento fecha dizendo que *"Defesa `+1` cai em 1,34 fatia, exatamente o tamanho de uma entrega — o único molde novo que nasce no tamanho certo sem precisar de janela"*. **Ela é o dobro de uma entrega, e precisa de janela como todo o resto.**

### Achado — o calendário de Caminho mudou na v0.70 e ninguém rodou a métrica

O `DESENHO-caminhos.md` põe o Caminho em `2 · 7 · 15 · 30`. **Quatro documentos continuavam em `7 · 15 · 23 · 29`** — o `ESTADO-ATUAL`, o `RASCUNHO-trilhas`, o `DECISOES-pendentes` e a auditoria.

*O modelo reproduz o `vão 5 · seca 24` publicado antes de comparar, que é o que faz a comparação valer:*

| Caminho | vão | seca | empilha em |
|---|---|---|---|
| `7 · 15 · 23 · 29` | **5** | **24 missões** | — |
| `2 · 7 · 15 · 30` | **8** | **31 missões** | níveis 2 e 30 |

**Quem carregava as duas métricas era o degrau do nível 23.** Sem ele abre um vão de oito níveis entre o 19 e o 27, e uma seca de trinta e uma missões entre os marcos 22 e 26. *E `vão 8` é o número que reprovou um dos dois calendários candidatos da Q2* — o que põe a entrada da v0.70 se contradizendo dentro dela mesma, porque ela recusa mudar o calendário com o argumento *"piora vão e seca"* e vinte linhas depois registra um que piora.

> **Decisão do Mizuki: o calendário fica, e o vão é preço aceito.** *"O resto do sistema vai carregar esse vão pelas classes."* O que ele compra é identidade de Caminho no nascimento e capstone no 30 — o formato do Paladino de 2024, que a própria auditoria conferiu em `3 · 7 · 15 · 20`. **Os quatro documentos foram acertados; a auditoria não, porque ela é datada.**

### Achado — a âncora de `3,3` rodadas não sai do documento que ela cita

A `LISTA-gatilhos-trilhas.md` ancora *"a luta dura 3,3 rodadas"* na **peça 15 §3.2**. Aquela seção tem **zero** ocorrências da palavra *rodada*, e o `3,3` não aparece em lugar nenhum daquela peça como duração de luta. **A dona é a peça 1: `3,4` a `4,0`**, e as peças 11 e 14 usam `3,5` e `3,7`.

**Nada quebra:** com `3,7`, o `1× por descanso curto` vale `27%` em vez de `30%` — continua acima do piso de `20%`, e o `1× por dia` continua reprovando. *Mas uma das duas taxas que a auditoria declara "saírem de documento" não sai de nenhum, e toda entrada preçada a 30% está 11% generosa.*

### Achado — as "oito famílias do permitido" não são o permitido

A auditoria e a `LISTA-gatilhos` medem oito famílias e chamam de *"o que a peça 5 §4 autoriza"*. **Elas tiram `treino`, que é linha de verdade e não tem conversão em dano, e põem `acerto`, que não é linha nenhuma** — e a v0.68 já tinha registrado isso como erro meu, com estas palavras: *"a lista tem sete linhas e acerto não é uma"*. Duas versões depois o nível 7 do Evocador concede acerto.

### Decidido — a §4 vira cerca curta com exemplos preçados

*Escolha do Mizuki: **"primeiro mede, depois corta, depois coloca exemplos pra não termos erros de novo."***

> **A cerca são seis proibições. Fora delas quem decide não é a lista — é o preço, e onde não existe preço, o teto de maestria.**

**Duas das seis são novas, e as duas teriam pego erro meu desta sessão:** `Redução de Dano passiva` — a regra do manual que matou a Passiva Casca na v0.26, e que a v0.70 furou desenhando a `Muralha` — e `refino dentro de uma rolagem`, que morava só na peça 11. *A segunda saiu estreitada na revisão cética: refino continua legal em custo, frequência e escopo, e escrever "refino como variável" proibiria o que a peça 11 autoriza.*

**As sete linhas viraram tabela de exemplos com janela e preço**, declarada não exaustiva. *A troca do fixo e a ação a mais ficam nela para serem vistas e não compradas — mesmo no piso de 20% elas custam 85% e 425% do orçamento de uma Trilha.*

### Decidido — o que mexe em rolagem e não tem conversão entra com teto de maestria

*Regra do Mizuki.* `auxílio`, `rerrolação` e `utilidade` são legais e o projeto não sabe preçar — falta a conversão de dano causado por outro, e falta saber quantos Testes de Resistência uma luta tem.

> **Não é preço; é garantia de que a coisa não deriva.** Maestria é o único número que cresce com nível e ela cresce `+3`, o mesmo ritmo de quem está do outro lado da rolagem.

**E `repertório` fica de fora do teto, o que ele mesmo desconfiou:** trocar um feitiço já é o menor tamanho que existe, e teto de maestria ali faria a entrega **crescer**.

### Decidido — `Coleira` vira `+1` fixo, e `Não Cede` vira maestria cheia com um por rodada

**A `Coleira` melhorou trocando `metade da maestria` por `+1`.** Como o sistema segura a taxa de acerto em `50%` em todo nível, `+1` vale `10%` da saída no nível 2 e `10%` no 30 — **não deriva por construção**, que é o argumento da margem crítica da `Presa` e é mais forte que o *"encolhe de leve"* que estava escrito.

**O `Não Cede` ganhou o preço que faltava e um cap que é dele.** Uma rerrolagem vale `25` pontos percentuais no pico, e a entrega dá `12,75` pontos percentuais médios por dia no nível 30. *Eu ofereci três saídas e ele escolheu uma quarta:* **maestria cheia, no máximo uma por rodada.** Sem o cap, `4` usos numa luta de `3,7` rodadas são mais usos do que rodadas e o contador para de limitar; com ele, o teto bate em `100%`, que é onde a escala de taxa do projeto já para.

### Registrado — o validador pegou uma perda de conteúdo minha

Reescrevendo a §4 eu apaguei o *"uma vez por cena"* que **definia o que é uma exceção estreita**. O `conferir-descanso.py` acendeu na hora, porque ele reconta os usos de `por cena` na pasta e compara com o total publicado na peça 10: **91 escrito, 90 contado.** *Ele foi escrito para pegar total guardado a mão envelhecendo, e pegou uma regra sumindo.* **Restaurado, com a definição em negrito desta vez.**

### Registrado — o levantamento, e uma afirmação minha que caiu

**Eu disse que "cerca curta mais exemplos" é o formato do 5e. Não é: o DMG de 2024 traz guia para criar antecedente, criatura e magia, e nenhum para subclasse.** *Casa com o documento da Paizo que a v0.70 já citou, dizendo que não existe sistema concreto para desenhar classe.*

**Quem tem é o Mutants & Masterminds**, e ele roda esta arquitetura há três edições: **quarenta efeitos fechados** em seis tipos — Ataque, Controle, Defesa, Geral, Movimento, Sensorial —, cada um declarando **ação, alcance, duração e custo por grau**, mais Extras e Flaws que mexem no preço. **E os vinte e um "poderes de amostra" não são efeitos novos: são combinações nomeadas dos quarenta, já somadas.** *É a camada de exemplos existindo publicada.*

**As duas coisas que isso trouxe para a §4:** cada exemplo declara janela e preço na própria linha — que é justamente o que faltava para três famílias serem precificáveis —, e **`Defesa` é um tipo de primeira classe lá**, enquanto aqui ela não estava nem no permitido nem no proibido.

### Em aberto

- **As quinze Trilhas.** É o próximo bloco, e o método está decidido na auditoria §7: escrever em ficção a partir do material, o Mizuki revisa a ficção, e só depois eu preço.
- **Abrir a lista não consertou a causa raiz, e isso está medido.** Das seis famílias candidatas, três não têm conversão e a que tem — defesa — precisa de janela como todas. **Saímos de três tipos vivos para quatro.**
- **Três conversões que não existem:** dano causado por outra pessoa, quantos Testes de Resistência uma luta tem, e recuperar condição.
- **A `LISTA-gatilhos` e a auditoria precisam da passada de conversão** — o `3,3`, as taxas de 30% e a família `acerto` que não é linha.
- **As treze Manhas** da Vanguarda, e a **`Modelagem`** do Emanador conferida contra o Fundamento.
- **A lista de ações** — peça nova ou seção da peça 3, e o `Provocar` medido contra os `−25 pp` da peça 11.
- **Duas escolhas de sabor do desenho:** `d6` ou `d8` no `Corpo Duro`, e qual `Voz Grossa`.
- As de sempre: as vagas de Desliga, a Cicatriz, Energia Reversa, o clash, o nome do sistema, o refino que paga mal no marco.

---

## [0.70] — 2026-08-15

**A Q3 de Trilhas não estava travada por falta de número: a régua não conseguia reprovar nada, e o método de Caminho e Trilha foi remodelado por cima disso.** *Três recomendações minhas caíram na segunda validação, e o Mizuki achou quatro coisas que nenhum validador alcança.* Continuam dezesseis peças e dezesseis validadores — o material desta versão mora em quatro documentos de trabalho na raiz, e vira peça quando fechar.

### Achado — a régua da Q3 reprovava zero de oito famílias

A cobrança era `botão × taxa` contra a fatia, e **a taxa é o grau de liberdade**: dado um botão `b` e uma fatia `f`, sempre existe `t = f/b`. **A igualdade não é checagem, é a definição de `t`.** Rodada contra as oito famílias do permitido, **nenhuma reprova** — inclusive `exceção de ação`, que a matriz proíbe por escrito nas três Trilhas do Evocador.

**E o `Servo` do §6.10 prova de dentro:** `5,07 − 1,56 − 1,80 = 1,71`, e `1,71 ÷ 11,50 = 14,9%`. **O documento publica `15%` e diz que falta escrever o gatilho.** A taxa saiu da subtração, não de gatilho nenhum.

### Decidido — piso de taxa de `20%` e lista fechada de gatilhos

*Escolha do Mizuki.* **O número não é inventado: é o teto de `-80%` de limitação do GURPS**, que roda a mesma mecânica há quarenta anos — e é onde a escada de Classe Passiva do §3.1 já parava. **Com ele, `uma ação a mais` passa a custar `17` fatias contra um orçamento de `4` e reprova sozinha** — a trava que hoje é escrita à mão cai da conta. *E o piso reproduz sozinho a rejeição do `1× por dia`, que o §3.6 tinha aceitado por levantamento externo: `9%` contra `30%`, com o corte em `20%` no meio.*

**A lista está em `LISTA-gatilhos-trilhas.md`**, em quatro famílias — rolagem, relógio, estado da ficha e julgamento —, com a taxa de cada uma lida de documento e o spread medido contra os `3,0×` da peça 13 §7.

### Achado — o levantamento do 5e 2024 estava errado, e o Mizuki tinha razão

O CHANGELOG da v0.60 e o §3 do rascunho escrevem que *"a edição de 2024 tirou todos os vãos de 8, padronizando em `3, 6, 10, 14`, com o capstone do Paladino descendo do nível 20 para o 14"*. **Conferido classe a classe no texto de 2024:**

| classe | níveis de subclasse | quantas |
|---|---|---|
| Bárbaro | `3 · 6 · 10 · 14` | 4 |
| Ladino | `3 · 9 · 13 · 17` | 4 |
| **Paladino** | **`3 · 7 · 15 · 20`** — idêntico ao de 2014 | 4 |
| **Feiticeiro** | `3 · 6 · 14 · 18` | 4 |
| **Bardo** | `3 · 6 · 14` | **3** |
| **Clérigo** | `3 · 6 · 17` | **3** |

**Uma de seis está no calendário padrão.** *Das três classes que o projeto citou nominalmente, nenhuma foi corrigida.* **E o mecanismo real está na revisão do Clérigo: a feature do nível 8 saiu da subclasse porque o benefício foi para a classe base.**

### Decidido — o calendário NÃO muda, e a recomendação contrária era minha

*O Mizuki pediu validação antes de aceitar, e ela derrubou a minha proposta.* **Três rotas independentes:** dar três entregas a um Caminho piora vão e seca; os cinco Caminhos já estão empatados por construção, então não há assimetria de base para compensar; e **a v0.61 já testou e desfez isso** ao mover o ataque extra do nível 6 para o 7, *"para os cinco terem quatro degraus de Caminho"*.

*E a "melhoria" que a busca achou também reprova:* `2·11·20·28` corta a seca de `24` para `18` missões, **e empilha três entregas em cima de níveis que já entregam feitiço.** **O calendário de hoje acerta oito de oito.**

### Achado — o permitido da peça 5 §4 é a causa raiz

Duração morreu na v0.68. `Exceção de ação` reprova pelo piso. **`Recuperar ferimento` e `recuperar Integridade` reprovaram nesta versão** — a primeira vale `0,00` para quem não cai, e o Bastião no nível 30 aguenta `11,7` rodadas contra uma luta de `3,7`; a segunda esbarra na regra do manual de que **dano de alma tira das duas barras ao mesmo tempo**, e o corpo acaba antes em três das quatro fichas. `Recuperar condição` depende de peça que não está na fila.

> **Sobravam três tipos de efeito para escrever sessenta entregas.**

### Decidido — remodelar Caminho e Trilha, e a base é levantamento

*Decisão do Mizuki: **"por que não começamos do zero?"***. O documento oficial de design de classes da Paizo abre dizendo que **não existe sistema concreto para desenhar classe** — eles têm um para raças e afirmam que para classe não dá. **A lista fechada de sete linhas da peça 5 é uma coisa que nenhum sistema grande tem.**

**E ele traz três regras que valem aqui inteiras:** primária contra secundária; *"uma classe com progressão completa de magia não recebe feature primária poderosa — a própria magia faz esse papel"*, que é o argumento do Mizuki palavra por palavra num sistema em que **todo personagem é lançador completo**; e *"lançadores completos são exceção ao dead level"*, que **desfaz o critério com que a Q2 mediu seca**.

### Achado — eu tinha superestimado a economia de ação em `9,4×`

Medi *"uma ação padrão a mais"*, que vale uma Rotina — `108`. **O Mizuki propôs um golpe simples a mais, que vale `11,50`.** *Foi por essa conta que declarei a linha morta e cheguei em "sobram três tipos".* **São quatro**, e o quarto é o que os quatro exemplos dele usam. Rodados contra o teto de `+18%` da peça 6 §3.1: **`+2,3%` a `+8,8%`. Todos cabem.**

### Adicionado — o desenho dos cinco Caminhos

**`DESENHO-caminhos.md`**, em três passadas com retorno dele em cada uma. **Calendário `2 · 7 · 15 · 30`**, `3` fatias por Caminho, e o nível 7 de graça porque é correção de base.

**Dois degraus fecham por construção:** o `Voz Grossa` do Emanador — *o seu Classe 0 passa a causar o mesmo que um golpe simples* — vale exatamente o vão, porque **o vão `físico − conjurador` É `golpe simples − Classe 0`**; e o `Vínculo` do Evocador em margem crítica entrega **`5,0%` da Rotina no nível 2 e `5,0%` no 30**, porque crítico é fração e não valor absoluto.

**E três correções vieram dele:**

| o que caiu | por quê |
|---|---|
| `Muralha` — RD passiva para aliados | **é proibida, e a regra está no manual** desde a v0.26: *"Redução de Dano passiva… Resistência a um tipo, sim. Desconto em tudo, não"*. **Eu escrevi exatamente o que matou a Casca** |
| `Presa` com `+atributo` | deriva `4×` — `23,1%` da Rotina no nível 2 contra `5,6%` no 30 |
| `Mão na Roda` com gatilho no acerto do outro | o gatilho tem de ser do **Guia**. Com ele no `Elo`, os níveis 2 e 7 se encadeiam |

### Achado — a lista de ações não existe

*Achada pelo Mizuki indo escrever o gatilho do Guia.* **A peça 3 tem os quatro slots do turno e nenhuma ação nomeada**; `Ajudar` está na peça 4 §5 e **nunca teve custo de ação declarado**. *Ela está rascunhada no fim do `DESENHO-caminhos.md`, com a ação padrão seguindo o padrão do hobby por decisão dele, e duas ações bônus novas — `Provocar` e `Ler o Ambiente` — que ele desenhou.*

### Em aberto

- **As quinze Trilhas.** É o próximo bloco, e agora ele tem régua com piso, lista de gatilhos e o desenho de Caminho por baixo.
- **As treze Manhas** da Vanguarda, uma por categoria de arma.
- **A `Modelagem` do Emanador conferida contra o Fundamento** — o manual já modela feitiço por Melhoria e Restrição.
- ~~O preço do `Provocar`.~~ **Medido, e ele PASSA com a duração de uma rodada** — spread de `1,67×` contra o teto de `3,0×`. *A primeira conta reprovou e estava errada: eu comparei os dois resultados condicionais ao sucesso e esqueci que teste disputado falha metade das vezes, o que dilui os dois lados igual. **Só a `100%` de sucesso ele chegaria no limite.** E a duração curta é o que impede o erro do mestre de empilhar: `25` pontos percentuais por rodada, independentes. *A pergunta que achou isso foi do Mizuki — "e se durar só uma rodada?".***
- **A peça 5 §4 precisa de:** a linha `auxílio`, a frase-trava reescrita (ela lista quatro e a lista tem sete), uma decisão sobre dano fixo, e casa para a `Sangria`.
- **Nenhum validador alcança nada disto.** Os quatro documentos são de trabalho e viram peça quando fecharem.
- As de sempre: as vagas de Desliga, a Cicatriz, Energia Reversa, o clash, o nome do sistema, o refino que paga mal no marco.

---

## [0.69] — 2026-08-15

**Varredura de lixo depois da v0.68, a pedido do Mizuki — e ela achou um terceiro prompt de retomada, escrito catorze versões depois do aviso que proíbe.** Nada de regra mudou: continuam dezesseis peças e dezesseis validadores.

### Achado — o `PROMPT-TRILHAS.md` estava no cemitério fingindo estar vivo

Ele está em `99-arquivo/` **desde a v0.59, sem cabeçalho de morte e sem entrada no `LEIA-ME` da pasta**. Aberto, ele lê como documento vivo: *"copiar o bloco abaixo inteiro"*.

**O agravante é que ele é o terceiro.** O `PROMPT-DE-CONTINUIDADE.md` morreu na v0.14 e o `PROMPT-CHAT-NOVO.md` na v0.45, os dois pelo mesmo defeito. **E o `LEIA-ME` daquela pasta termina com o aviso** — *"dois arquivos, o mesmo motivo, trinta versões de distância — leia o cabeçalho dele antes de escrever um terceiro"*. Este foi escrito **catorze versões depois** dele.

**E envelheceu igual.** Ele manda conferir `head -6 README.md` contra **v0.59**, ler o CHANGELOG **até a v0.50** e afirma **19 de 19 validadores** — e a checagem por número de versão é exatamente a que o `README` documenta como erro, porque *"um teste escrito contra um número que sobe toda semana começa a mentir na semana seguinte"*.

> **Por que isso é lixo de verdade e não arrumação.** As outras coisas que a varredura achou não fazem mal a ninguém. **Este arquivo faria uma conversa nova seguir instruções de dez versões atrás** — e ele mora na pasta que existe para guardar o que *não* deve ser lido.

**Ganhou o cabeçalho no molde dos outros dois e entrada na tabela do `LEIA-ME`.** *O que sobreviveu dele não é conteúdo: é o padrão. Três arquivos, três mortes, o mesmo defeito.*

### Registrado — o que a varredura achou e NÃO mexeu

| o que | por que fica |
|---|---|
| **três `.gitkeep` vencidos** — `02-esqueleto`, `03-mecanica` e `05-material` já têm arquivo | zero byte cada, e tirar custa um commit. *O do `04-playtest` continua fazendo o trabalho dele, porque aquela pasta segue vazia desde a v0.1* |
| **`_to_delete/`** com dois arquivos esperando | é o desenho: o assistente não consegue apagar neste mount, então ele empurra para lá e você apaga a mão. Está no `.gitignore` |
| **o `node_modules` do gerador da ficha é link para o do manual** | pendura num clone novo até alguém rodar `npm install`, e o `COMO-USAR.txt` daquela pasta já avisa |
| **`manual/gerador/Fundamento-MANUAL-v7.docx`** duplica o de `manual/` | é cópia de trabalho do gerador e o `.gitignore` já a segura |

**E o que a varredura NÃO achou, que também é resultado:** zero `__pycache__` ou `.pyc` rastreável, zero temporário de editor, zero pasta vazia, zero arquivo duplicado fora dos que têm motivo, e nenhum `.lock` preso no `.git`.

### Em aberto

Nada novo. A lista das Trilhas é a da v0.68, e ela continua fechada.

---

## [0.68] — 2026-08-15

**A v0.67 escreveu que a peça 15 estava "inteira na escala nova", e ela não estava — quatro linhas ficaram na velha, e uma delas é regra viva.** *Achado indo conferir a moeda antes de escrever as doze entradas do Evocador, que são denominadas nela.* Continuam dezesseis peças e dezesseis validadores, e continuam trinta checagens: o que entrou foram **metades novas dentro das checagens 8, 9 e 10**, que já eram as donas de cada coisa.

### Achado — a venda de deslocamento não foi multiplicada, e nenhuma das três checagens vizinhas olhava para isso

A ficha da invocação pode descer o acerto ou a Defesa dela, e descer **devolve ponto**. Esse ponto ficou em `1` enquanto o catálogo e o orçamento eram multiplicados por quatro.

| devolve | o que a venda de 1 compra sozinha | vendendo 5, entram | × o orçamento do nv2 |
|---|---|---|---|
| **4** | 2× a entrada mais barata (2 pts) | 20 | **2,50** |
| 2 | 1× a entrada mais barata | 10 | 1,25 |
| **1** — como estava | **nada — metade da mais barata** | 5 | 0,62 |

*Antes da v0.67: orçamento do nv2 era `2`, a entrada mais barata custava `1`, e a venda devolvia `1` — ela comprava uma entrada inteira, e vender 5 entravam `2,50×` o orçamento.* **A venda tinha perdido três quartos do poder de compra, e isso não foi decidido em lugar nenhum.**

> **Por que passou verde.** A checagem 8 confere a **forma** da venda — que descer devolve e que subir é proibido —, e ela sai verde com qualquer número. A checagem 30 mede só o que a venda **custa** em vida efetiva. E a busca exaustiva **só enumera compra**: ela nunca modelou venda. *O argumento de segurança da v0.67 — "escala uniforme preserva o conjunto legal exato" — vale para quem compra, e ninguém foi olhar quem vende.*

### Decidido — a devolução vira `4`, que é a escala uniforme

*Escolha do Mizuki entre as três.* **`4` é o que um ponto da escala velha virou**, que é o mesmo motivo pelo qual cada marco passou a dar `4`. Vender 5 volta a entrar `2,50×` o orçamento do nível 2 — exatamente a razão de antes da escala.

### Alterado — as outras três linhas da escala velha

| onde | o que dizia | o que diz |
|---|---|---|
| **§1, o resumo da Q3** | orçamento `2` no nv2, `+1` por marco, `9` no 30 | `8`, `+4`, `36` |
| **§3.6, as duas moedas** | *"o ponto de arma é cerca de quatro vezes menor que o de ficha (ficha tem 2 a 9)"* | a razão medida, e a separação apoiada no **que cada moeda compra** |
| **§3.7, o núcleo do Panda** | *"o orçamento do nível 2 é 2"*, degrau de `3` pontos | `8` e `12` — **o argumento não se moveu**, e é por isso que ele fica |

**A frase das duas moedas era a mais errada das três, e não por causa da escala.** Recalculada dos donos — o ponto de arma da peça 14 e a `Rotina` da peça 6 —, a razão **nunca foi um número só**: ia de `2,0×` no nível 2 a `16,4×` no 30. Depois da divisão por quatro ela vai de **`0,5×` a `4,1×`**, e no nível 2 **o ponto de arma passou a ser o maior dos dois**.

> **Então o motivo escrito para as duas moedas não se misturarem parou de reproduzir.** *"São orçamentos de tamanhos diferentes"* não segura mais nada. A separação continua certa, e ela se apoia no que cada uma **compra**: o ponto de arma compra dado de dano, e o desta ficha é proibido de tocar em dado de dano. **A regra ficou, o motivo mudou** — e um motivo que envelheceu ensina a procurar o defeito onde ele não está mais.

### Adicionado — três metades novas, cada uma dentro da checagem que já era dona

- **Checagem 8** passa a medir o **tamanho** da devolução, em duas afirmações separadas de propósito. **A regra aplicada:** a devolução tem de comprar pelo menos a entrada mais barata do catálogo, senão descer é castigo e não escolha. **O limite de design:** ela bate com o passo do marco, porque as duas *são* um ponto da escala velha. *A mensagem do segundo diz, com todas as letras, que separar os dois é decisão a escrever e não número a ajustar.*
- **Checagem 9** compara o resumo do topo da peça com a tabela dona — base, passo e teto. **Apagar a linha também acende**, senão o conserto barato para uma divergência vira sumir com a cópia.
- **Checagem 10** **recalcula** a razão entre as duas moedas em vez de aceitar a publicada, e ela cai dos donos: o ponto de arma da peça 14, a `Rotina` da peça 6, a fração que um corpo entrega e a própria devolução.

**Nenhuma delas é `conferir-*.py` novo nem checagem numerada nova**, e isso é de propósito: arquivo novo ou trigésima primeira checagem mexeriam na contagem que mora em quatro documentos, para guardar coisa que já tinha dono.

**Arnês, na cópia isolada, com a base conferida verde antes e o `diff` provando cada `sed`:**

| perturbação | acendeu? |
|---|---|
| a devolução volta a `1` | **sim** — nas duas metades, e a primeira nomeia a entrada mais barata |
| a devolução vira `3` | **sim** — e **só no acoplamento com o marco**, que é o que prova que as duas metades são eixos separados |
| acerto devolve `4` e Defesa devolve `2` | **sim**, nomeando os dois valores |
| o resumo do topo volta à escala velha | **sim**, dizendo base, passo e teto dos dois lados |
| o resumo do topo é apagado | **sim** |
| cada marco passa a dar `3` | **sim**, e a tabela do orçamento cai junto |
| a razão publicada `4,1×` vira `6,0×` | **sim** |
| **o dono muda:** o ponto de arma da peça 14 vai de `0,33` para `0,50` | **sim** — acende nos dois níveis, que é a prova de que a razão não é constante escrita |
| **contra-teste:** a prosa do que o `Faro` faz | **não acendeu** |
| **contra-teste:** uma palavra no parágrafo do Panda | **não acendeu** |
| **contra-teste:** a prosa do que o `Vigia` faz | **não acendeu** |

*A segunda linha é a que dá valor à primeira.* Sem ela as duas metades poderiam ser a mesma afirmação escrita duas vezes — que é a lição nº 8 na forma em que ela mais reincide aqui.

### Achado — a tabela do orçamento do `Servo` estava MEIO convertida, e é a sexta linha

*Achada respondendo à pergunta do Mizuki sobre a rota.* A tabela do §3.7 que carrega a concessão inteira da Q6 tinha o **cabeçalho na escala nova e as duas colunas na velha**:

| nv | dizia ficha | dizia `Servo` | deriva ficha | deriva `Servo` |
|---|---|---|---|---|
| 2 | 2 | 3 | **8** | **12** |
| 30 | 9 | 13 | **36** | **54** |

*O `112 pontos` do cabeçalho está certo — o catálogo soma isso mesmo na escala nova —, e as porcentagens de 11%, 21% e 32% também, porque `velho ÷ 28` e `novo ÷ 112` dão o mesmo número.* **A do nível 30 não:** ela vira `48%`.

### Registrado — e o arredondamento do `Servo` virou letra morta sem ninguém decidir

`o orçamento da ficha mais metade, arredondando para baixo` **raspava meio ponto nos níveis 6, 14, 22 e 30**, que eram os de orçamento ímpar. **Na escala nova todo orçamento é múltiplo de `4`, então `mais metade` sempre fecha redondo** — e o `Servo` passou a ficar com `2` pontos a mais nesses quatro níveis.

> **A regra não muda, e o número novo é o certo.** Ela é a regra global da peça 1 §5.4 e continua valendo; o que aconteceu é que ela deixou de ter o que raspar aqui. *Manter o número velho exigiria derivar através de uma escala que não existe mais.* **É a mesma paridade que a v0.67 registrou na busca exaustiva, do outro lado: a moeda fina fecha conta que a grossa arredondava.**

### Adicionado — a tabela do `Servo` passou a ser derivada, dentro da checagem 9

Ela lê a ficha dos marcos, aplica `×1,5` com o arredondamento da peça 1, e **reconta o total do catálogo** em vez de aceitar o publicado.

| perturbação | acendeu? |
|---|---|
| o `Servo` do nv30 volta a `13` | **sim**, dizendo que a regra dá 54 |
| a ficha do nv18 volta a `6` | **sim**, dizendo que os marcos derivam 24 |
| a porcentagem do nv30 volta a `46%` | **sim**, com o recontado |
| o total do catálogo vira `28` | **sim** — ele soma 112 |
| **contra-teste:** a prosa sobre a `Matilha` logo abaixo | **não acendeu** |

### Decidido — a entrega de Trilha do Evocador muda de categoria

*Decisão do Mizuki depois de levantamento externo que ele pediu.* **Ela deixa de ser `+1` ponto de orçamento e passa a ser coisa nomeada da camada de vínculo** — *o que **você** ganha por ela estar de pé.*

**O que derrubou a saída da v0.67 foi contradição interna, e o levantamento foi quem fez ela aparecer.** O §6.4 escreve *"as doze entradas são nomeadas, nunca em branco"* e *"nenhuma entrega move o orçamento"*; o §6.6 escreve *"a entrega é `+1` ponto"*. **Com um ponto por degrau, as doze entradas são a mesma entrada doze vezes** — e a `Matilha`, que a matriz proíbe de receber orçamento, recebe nas quatro dela.

> **A matriz não acusa porque o eixo de orçamento dela é liga-desliga:** ela lê *"mais metade"* e marca `2` ou `1`, e não conta pontos. **Terceira versão seguida em que o defeito é o eixo errado.**

| sistema | o que cada degrau entrega | o que custou |
|---|---|---|
| **Pathfinder 2e** Summoner | features nomeadas — e **quatro das seis são os dois lados ganhando junto** | a customização virou trilha separada, os *evolution feats* |
| **D&D 5e 2024** Beast Master | comando, ataque extra e feitiço compartilhado | é tudo economia de ação, e quase nada disso é legal aqui |
| **Pathfinder 1e** Summoner | **o bolo de pontos cresce com o nível** — a saída da v0.67 | opção-armadilha e a classe mais reclamada da edição |

**As quatro features do 2e que são "os dois lados de uma vez" são literalmente a categoria que o §6.5 tinha achado e chamado de "a que não existe".** *O levantamento não trouxe ideia nova — ele confirmou a que o documento já apontava, e mostrou um sistema grande com a progressão inteira construída ali.*

**A moeda quebrada em quatro fica**, porque ela nunca foi só para caber a entrega: ela é a granularidade do catálogo da peça 15. *O que morre é a frase que fazia dela a entrega.*

### Achado — o §3.3 e o §3.5 mediam com réguas diferentes, e a conta separou

*Apareceu ao preçar a camada de vínculo, e ela decidia o preço das doze entradas.* O §3.3 diz que a entrega é **plana** — `1,27` de dano por rodada em todo nível, com a quantidade crescendo. O §3.5 diz que toda entrega é **fração de coisa que cresce**, e reprova valor absoluto. **As duas não valem para a mesma entrega.**

Rodado contra a dívida da peça 14 §4, que é o alvo em todo nível:

| nv | alvo | plana | fração | por Classe |
|---|---|---|---|---|
| 6 | 1,92 | **−34%** | −81% | −58% |
| 14 | 4,68 | **−19%** | −52% | −36% |
| 22 | 7,41 | **−14%** | −26% | −20% |
| 30 | 10,14 | **+0%** | +0% | +0% |

> **A prova não é a plana ganhar — é ela reproduzir os erros que o §3.3 já publicava.** Aquela seção escreve *"34% abaixo nos níveis 5 e 6"* e *"entre 13% e 19% abaixo no miolo"*, e a conta devolve `−34%`, `−19%` e `−14%`. **Mesmo modelo, mesmos números**, o que valida a leitura antes de valer a comparação. *As três empatam no nível 30 porque é lá que a fatia foi definida; descendo, a fração entrega um quinto.*

**A fatia é plana, e o §3.5 fica com a pergunta errada.** A certa é **"isso cresce depois de chegar?"** — porque o que soma duas vezes com o acúmulo é a entrega que cresce sozinha depois de entrar na ficha.

### Decidido — duração sai do permitido para efeito de Trilha, e posicionamento entra com previsão

**`+1 rodada sempre` custa de `11` a `43` fatias**, conforme o comprimento do efeito. *Não existe efeito curto o bastante para ela caber* — no melhor caso ela ainda é onze vezes uma entrega. *A conta supõe o teto (o efeito vale uma Rotina por rodada), e baixar isso exigiria uma conversão para efeito que não é dano, que o projeto não tem.* **Ela fica registrada com o número, e continua valendo para Caminho e aptidão.**

**Posicionamento fica**, com o número da mesa fixado em **`5%` das rodadas** e marcado como previsão. *Mas ele não tem troco:* o metro exato de uma fatia é **`2,11 m`**, e a escala do projeto é `1,5 · 3 · 6 · 9 · 18 · 21 · 30` — sobra ficar 29% abaixo ou 42% acima. **Terceira família em que a falta de troco aparece**, e a saída é a mesma das outras duas: a janela absorve o que a escala não divide.

### Achado — a parede do Evocador não era da moeda, e a escada de Classe nunca tinha sido preçada

| família | janela | em fatias |
|---|---|---|
| acerto `+1` no seu acerto · PE `+1` por rodada | permanente | 4,3 · 4,1 |
| **acerto `+1` preso no que ela faz** · **PE `+1` por descanso curto** | janela | **0,9 · 1,2** |
| alvo — seu golpe simples pega 2 | permanente | 9,1 |

**Tudo que é permanente e encosta na máquina do Evocador vale quatro fatias ou mais.** *A v0.67 tinha lido isso como problema de moeda e quebrou o ponto em quatro; a moeda era metade da resposta.* **A outra metade é a janela** — e ela casa de graça com o formato do §6.4, porque o `Coro` já puxa pro condicional.

> **E o que fecha: os exemplos da escada de Classe Passiva nunca foram convertidos em fatia.** Ela foi escrita como **forma** — o que separa permanente de reativo de condicional — e as células viraram exemplo sem preço. **Dois dos sete não sobrevivem:** *"+3 m sempre"* está `1,42×` grande e *"+1 rodada sempre"* está `11×`.

### Achado — a auditoria da escada, e a pergunta do Mizuki que a provocou

*Ele perguntou se era impressão dele que cada problema resolvido fazia aparecer outro.* **Não era, e a resposta foi enumerar em vez de tranquilizar.** A escada de Classe Passiva tem **16 células preenchidas**. Preçadas contra a fatia:

| | |
|---|---|
| **cabem** | posicionamento-3 (`1,4`) · recuperação-2 (`1,2`) |
| **grandes** | recuperação-3 `4,1` · alvo-2 `2,7` · alvo-3 `9,1` · duração-3 `10,7` · troca do fixo-3 `17,0` · duração-2 `25,6` · exceção-2 `25,6` |
| **sem preço** | as outras sete |

**Na coluna da Classe 3 — a que o `Servo` precisa três vezes — cabe uma.**

> **A causa é uma só, e ela explica os sete achados da versão:** a escada foi calibrada para **aptidão**, onde o refino carrega a magnitude e o orçamento é de um marco inteiro. Portada para a Trilha, onde o refino é proibido e o orçamento é uma fatia, **ninguém converteu as células**. *Os problemas não estavam se multiplicando — era um só, aparecendo em sete lugares.*

### Decidido — a Q3 foi REFORMULADA, e o que mudou é o método

*Decisão do Mizuki: **"vamos reformular, talvez estejamos usando a metodologia errada"**.* **Ele estava certo.** O método convertia tudo em dano por rodada e cobrava **uma fatia por entrega** — e quase nada do que uma Trilha entrega é dano.

**As duas metades do conserto:**

> **1. O preço mora na Trilha, não na entrega.** As quatro somam o orçamento; nada obriga as quatro a valerem igual.
> **2. Cada entrada declara a taxa de disparo**, e o que se confere é `botão × taxa`.

**A segunda é a que destrava, e a primeira sozinha não bastava.** Os botões que a peça 5 §4 autoriza são **indivisíveis e grandes** — `+1 PE` vale `4,1` fatias, dobrar o golpe simples vale `9,1`, uma ação a mais vale `85,2`. **A escada oferece três taxas fixas — `100%`, `27%`, `20%` — e nenhuma divide `11,50` até `1,7`.** Uma taxa de `15%` divide.

> **É por isso que a escada não estava errada e mesmo assim não servia.** Ela mede **forma**, e diz isso de si mesma: *"ela não mede quanto, mede o quê"*. **As três Classes são três pontos de um dial contínuo**, e a Trilha precisa do dial inteiro. *A escada continua sendo a de aptidão e continua valendo lá.*

**E o degrau do nível 7 deixa de ser exceção.** Ele vale de `3,2` a `5,5` fatias e estava marcado como *"o único diferente dos oito"* porque a régua antiga cobrava uma. Com o preço por Trilha ele é só uma entrega grande. *Uma régua que precisa de exceção para o caso mais importante estava medindo a coisa errada.*

**Sobrevivem intactos:** o calendário da Q2, as travas de forma do §3.6, a banda de orçamento e a fatia como unidade de conta. *A decisão "oito iguais contra a do nv2 maior" deixa de ser pergunta.*

### Adicionado — o `Servo` montado, como prova de que o método constrói

| nv | a entrega | botão | taxa | sai em |
|---|---|---|---|---|
| 2 | treino enquanto ela está de pé | utilidade | — | *sem preço em dano* |
| 11 | `+1 PE`, 1× por descanso curto | `5,14` | `30%` | `1,54` |
| 19 | `+3 m` enquanto ela está de pé | `1,80` | `100%` | `1,80` |
| 27 | o golpe simples pega 2, com gatilho | `11,50` | `15%` | `1,72` |

**Somam `5,07` contra um orçamento de `5,07`.** *A montagem não foi ajustada para fechar — as taxas saem de onde as coisas acontecem.* **Falta o gatilho do nível 27**, que é o que fixa os `15%`.

### Registrado — três recomendações minhas caíram na segunda validação, e o pedido é dele

*Ele escreveu: **"recomendo validar mais de uma vez sempre que me recomendar algo, por eu estar confiando em você"**.* **Na mesma sessão isso pegou três:**

1. Recomendei **escada própria de Trilha**; a segunda passada achou que a escada **mede forma e não magnitude**, então ela porta — e uma escada nova seria a palavra com duas escalas que a v0.64 pagou para consertar.
2. Recomendei **orçamento por Trilha** como suficiente; testado contra o `Servo`, ele **ainda travava** — faltava a taxa declarada.
3. Preçei uma família **`acerto +1`** que **não é linha do permitido**. A lista tem sete linhas e acerto não é uma; o que existe é *trocar o fixo por atributo*, que é outra coisa e custa `17` fatias.

> **As três só apareceram porque alguém mandou olhar de novo.** *Fica como procedimento: recomendação minha passa por uma segunda leitura antes de virar decisão dele.*

### Registrado — o defeito é o mesmo das três últimas versões, numa camada nova

**A v0.63 achou uma checagem que se media pelo eixo errado. A v0.66 achou uma skill que dizia "aplicada nos dois lados" e não estava. Esta achou uma escala declarada uniforme que não era.** *As três têm a mesma forma:* alguém escreveu que a coisa foi feita por inteiro, e nada conferia o "por inteiro".

> **E o que fez esta aparecer foi ir conferir a moeda antes de gastar ela.** As doze entradas do Evocador são precificadas em `+1` ponto da escala nova. **Escrever as doze primeiro teria enterrado o defeito debaixo de doze entradas escritas na moeda errada.**

### Em aberto

**Varredura feita antes de fechar, a pedido do Mizuki. A lista abaixo é o estado inteiro das Trilhas, e ela é fechada — não existe superfície escondida.**

**As seis que esta versão criou e consertou aqui mesmo** — ficam registradas porque a próxima reformulação vai criar as mesmas:

| onde | o que ficou pendurado |
|---|---|
| §3.3 | afirmava a cobrança por entrega como regra viva · **ganhou aviso apontando o §3.4-B** |
| §3.5 | abria com a pergunta que esta versão provou errada · **ganhou a pergunta certa no topo** |
| §5 | dois itens da spec eram do método velho · **o contra-teste do nv7 morreu, e entraram quatro itens novos** |
| §3.1 | publicava três taxas como se fossem as únicas · **ganhou o aviso do dial** |
| §6.9 | escrita sob o enquadramento por entrega · **ganhou o aviso de releitura** |
| `ESTADO-ATUAL` | dizia *"a régua fechou na v0.61"* · **agora diz que ela foi reformulada** |

**O que continua aberto, em ordem de quem trava quem:**

- **O gatilho do nível 27 do `Servo`** — é ele que fixa os `15%`, e sem ele a única Trilha montada não fecha. **Não pode supor corpo a corpo nem dar ação.**
- **O `Coro` precisa da variância refeita.** Os desvios do §6.4 foram medidos tratando toda condicional como `20%`, e o §6.4 exige que a do `Coro` dispare em quase toda rodada. A `90%` ele cai de `3,29` para `2,13` e a ordem das três se inverte. *Decidido: refazer as três quando o bloco do `Coro` começar.*
- **Sete das dezesseis células da escada continuam sem preço.** A lista está no §6.9.
- **Nenhum validador alcança o rascunho.** Todo número do §3, do §6.9 e do §6.10 está sem rede até a peça fechar — e a spec do §5 é o que vai cobrar isso.
- **A regra do slot do golpe do `Arremate` e do `Coro` continua sem validador dono** (peça 6 §3.1). Trocar o slot ou apagar o gate sai verde hoje.
- **As duas dívidas da peça 15:** quando a vida cheia da invocação reinvocada volta, e o que acontece com ela quando o **dono** cai.
- **A `Matilha` e o `Coro` não foram montados.** Só o `Servo`.

- **As doze entradas do Evocador.** O formato fechou na v0.67, a categoria fechou aqui, o conteúdo não. É o resto da Q5.
- **A camada de vínculo tem régua e não tem catálogo.** Sobram cinco famílias — `acerto`, `alvo`, `recuperação`, `posicionamento` e `exceção de ação` —, e a última é ilegal para `Servo` e `Matilha`. **E ela vai precisar de checagem própria**: ela não encosta em nenhum dos cinco eixos, então a matriz sai verde de qualquer jeito.
- **Os exemplos da escada de Classe Passiva continuam sem preço**, fora os dois que esta versão mediu. *A peça 11 §4 é a dona, e ela nunca converteu as células dela em fatia.*
- **O `5%` de posicionamento é previsão e está marcado como tal**, junto de todo o resto — `04-playtest/` continua vazia.
- **As duas dívidas da peça 15**, e as duas continuam sem contra o que ser medidas: **quando a vida cheia da invocação reinvocada volta**, e **o que acontece com a invocação quando o dono cai**.
- **A regra do slot do golpe do `Arremate` e do `Coro` continua sem validador dono.** Trocar o slot ou apagar o gate **sai verde hoje**. Entra com o validador de Trilhas.
- As de sempre: as vagas de Desliga, a Cicatriz, Energia Reversa, o clash, o nome do sistema, o refino que paga mal no marco.

---

## [0.67] — 2026-08-15

**O bloco do Evocador abriu, e a primeira coisa que ele achou foi um vão na peça 6 aberto desde a v0.24: ela sempre disse *"2 ações"* e nunca disse quais.** Continuam dezesseis peças e dezesseis validadores — nada de arquivo novo, porque o formato mora no rascunho até a peça fechar.

### Decidido — o formato das doze entradas do Evocador

*Escolha do Mizuki, uma por Trilha, com a variância na mesa.* A régua da Q3 deixa **38 sequências legais** por Trilha: 81 cai para 54 pela trava do nível 2, e para 38 pela trava do botão. **A média é idêntica nas 38** — `5,08` de dano por rodada no nível 30, por construção da régua. *O que separa uma da outra é variância.*

| Trilha | jeito | desvio | rodada morta | pico |
|---|---|---|---|---|
| `Servo` | sempre-ligado | `2,09` | 0% | `8,51` |
| `Matilha` | meio a meio | `2,95` | 0% | `11,94` |
| `Coro` | **`1 · 2 · 3 · 3`** — condicional no nv2, botão no nv11 | `3,29` | 0% | `13,59` |

**Um permanente sozinho já zera a rodada morta.** A pior sequência legal, `1 · 1 · 1 · 2`, deixa a Trilha sem fazer nada em **37% das rodadas**.

*E nenhum dos três motivos é estético.* O `Servo` é sempre-ligado porque a vida de `5h` da Q6 existe para o corpo não cair — variância de formato em cima de um corpo só recria pelo formato o *"acabou o kit"* que aquela decisão saiu para fechar. A `Matilha` fica no meio porque a variância dela **já mora nos cinco corpos**, e empilhar mais conta a mesma coisa duas vezes. E o `Coro` puxa pro condicional porque o encadeamento é a ficção dele: *"a invocação atacou"* dispara em quase toda rodada, que é o que o §3.6 exige de uma condicional no nível 2.

### Achado — três travas vieram da matriz, e doze verdes não provam nada

Matriz de dominância rodada subindo um eixo de cada vez em cada Trilha, nos cinco eixos: **quinze testes, base limpa.** Três acendem:

| dar… | para | acende |
|---|---|---|
| **ação** | `Matilha` | `Matilha > Coro` |
| **orçamento** | `Matilha` | `Matilha > Servo` |
| **ação** | `Servo` | `Servo > Coro` |

> **Os outros doze saem verdes, e é aí que mora o perigo.** Dar um segundo corpo ao `Servo` **não acende nada** e mesmo assim borra a diferença dele para a `Matilha`. *A matriz não mede ficção* — é a lição do eixo errado da v0.63 reaparecendo na peça em que ela nasceu, quatro versões depois.

### Decidido — o golpe do `Arremate` e do `Coro` é Ação Bônus, com gate na Padrão

*Decisão do Mizuki, e o gate é a parte dele que faz a coisa funcionar:* **o golpe simples só existe se a Ação Padrão daquele turno foi gasta no que a Trilha é** — comandar, no `Coro`; conjurar, no `Arremate`.

> **Eu ia reprovar isso com a conta errada, e o registro fica porque o erro é instrutivo.** Escrevi que mover o golpe para a Ação Bônus é *somar*, que a §3.1 reprova com `+18%` sustentado do nível 18 ao 30. **É falso para o `Coro`:** a seção 4 põe teto de **uma Rotina** no dono mais todas as invocações, e a própria §3.1 escreve que *"as ações se redistribuem, o dano não sobe"*. **Fui ler antes de afirmar, e a leitura derrubou a minha objeção.**

**O gate fecha o vazamento que sobrava.** Sem ele, um `Coro` de Padrão livre conjura, golpeia e comanda no mesmo turno — e o teto de uma Rotina segura o **dano**, não o controle, o alcance nem a condição. *É o eixo errado de novo, na mesma versão.* Com o gate, a escolha volta a ser por rodada: **ou conjura, ou comanda e golpeia.**

**O que sai por rodada não muda; o que muda é que o golpe passa a custar um slot que não custava**, porque ele morava no lugar do Classe 0 e o Classe 0 é grátis. **E esse preço cresce sozinho:** a peça 14 §4 mediu os slots e achou que a Ação Bônus **não cobra nada hoje** — *passivo* e *ação bônus* empatam em `2,01`, e ela chama o slot de *"o mais vazio do turno"*, com o conserto já escrito: *"um preço que cresce sozinho conforme o sistema enche o slot"*. **Esta regra é a primeira coisa a enchê-lo**, e o Bastião socando como Ação Bônus é a segunda.

### Registrado — o levantamento externo que matou a entrega em branco

**O orçamento de invocação cresce `4,5×` contra os `8,31×` da Rotina — razão `0,54`.** Ele cai entre os espaços de feitiço (`0,68`) e a maestria (`0,48`) na tabela do §3.5 do rascunho: **uma entrega escrita nessa moeda vale metade no nível 30 do que valia quando você a pegou.**

*E o hobby já tentou exatamente isso.* O **Pathfinder 1e** monta o eidolon gastando um **bolo de pontos de evolução**, e o guia de referência da comunidade descreve o resultado: opções-armadilha (*"two evolution points for one secondary attack is a very poor investment"*), escolhas óbvias que todo mundo pega (*"flight is crucial, especially at high levels"*), e um **teto externo de número de ataques que precisou existir só para segurar o resto** (*"without this, eidolons would be fairly ridiculous"*). **O Pathfinder 2e trocou o bolo por tipo fixo mais talentos nomeados**, com vida compartilhada e uma ação de agir junto uma vez por rodada — que é quase palavra por palavra o que o `Coro` já é aqui.

**As doze entradas são nomeadas, nunca em branco.** O orçamento continua sendo a concessão fixa do `Servo`, e nenhuma entrega o move.

### Registrado — nenhuma entrega do `Coro` pode supor corpo a corpo

A peça 14 §5 tem a categoria `Arma de Fogo` com sete armas, mais a propriedade `Longo Alcance`. **Uma ficha de `Coro` atirando ao lado de invocações que fecham a distância é legal hoje** — e entrega escrita como *"quando vocês estão adjacentes"* exclui uma montagem que o catálogo já permite.

### Achado — a parede do Evocador: toda moeda dele é maior que uma fatia

*Apareceu tentando escrever as quatro entregas do `Servo`, depois de três tentativas caírem.* **O problema nunca foi qual entrega escolher — é que a máquina de Invocações não tem troco.**

| moeda | % da Rotina | em fatias |
|---|---|---|
| 1 ponto de orçamento | `5,00%` | **4,3** |
| invocar de graça, o dia todo | `9,00%` | 7,7 |
| qualquer coisa presa em *"quando ela cai"* | — | 1,3 a 6,9, **spread `5,2×`** |
| **a fatia** | `1,17%` | 1,0 |

> **O número que fecha:** as **quatro** entregas de Trilha do `Servo` somam `4,69%` da Rotina, e **um** ponto de orçamento vale `5,00%`. *A Trilha inteira do Evocador vale, somada, cerca de um ponto — e um ponto é a menor coisa que a peça 15 sabe vender.*

**E o spread de `5,2×` é o filtro multi-mestre reprovando de novo:** a peça 15 §3.4 mede reinvocações de `0,8` a `4,2` por dia conforme quem mestra, e a peça 13 §7 já tinha reprovado `3,0×` escrevendo que ali o filtro *"está falhando, com número em cima"*.

### Achado — duas dívidas da peça 15, e o Mizuki achou as duas sem querer

*Ele leu uma entrega que eu propus e escreveu: "não entendo o benefício disso".* **Ele estava certo, e é o terceiro achado seguido que vem de ele não entender uma coisa que estava errada.**

1. **Quando a vida cheia da invocação reinvocada volta** — o §3.5 registra a pergunta, diz que o candidato é o descanso longo e que é sabor. Eu propus uma entrega que melhora esse relógio. **Não havia relógio.**
2. **O que acontece com a invocação quando o DONO cai** — a peça fecha o lado vizinho e nunca escreveu este.

> **Não dá para precificar entrega contra linha de base que não existe**, e esta é a versão difícil da armadilha: o termo *parece* existir, porque a pergunta está escrita.

*E uma terceira, menor:* propus *"o `Investir` usa o seu atributo no lugar do fixo"* e **o acerto da invocação nunca teve valor fixo** — ele cresce `+3` junto com a maestria, e o §5 daquela peça tem contra-teste em cima disso.

### Decidido — o ponto de orçamento se quebra em quatro

*Escolha do Mizuki entre as três saídas.* **Toda a peça 15 multiplica por 4.** Escala uniforme preserva o conjunto legal exato, então a busca exaustiva e as trinta checagens passam sem alteração.

**Só escalar não basta:** com o item mais barato em `4`, a entrega de `+1` fica **morta** nos níveis 2, 11 e 19. Então o degrau de 1 ponto se abre em entradas finas — e **a régua para isso já estava escrita**, no eixo que o degrau 2 usa para cobrar `8`: *"encosta em outra criatura ou no tabuleiro"*.

> **`anda 2 · comunica 3 · percebe 5 · espaço 7`**, com o degrau 2 em `8`.

**O teste que decidiu reprovou as três sub-réguas que eu tinha proposto.** As seis entradas do degrau 1 somam `24` na escala nova; as minhas somavam `16` e `17`. **Elas não eram sub-régua — eram um aumento de 30% no orçamento do Evocador, escondido numa tabela.** *Quebrar um degrau chapado só para baixo nunca é neutro.*

*E a ordem não foi escolhida:* o `Miúdo` fica em `7`, **a um passo do `Graúdo` em `8`** — o par que o §3.7 já descreve como separado não por tamanho, mas por *quem sofre*.

**A prova:** contando montagens sobre o catálogo, a entrega abre espaço novo em todo nível — `23→27` no nv2, `188→306` no 11, `798→1.204` no 19, `2.170→3.206` no 27. *Ela vale `1,07` fatia, e a régua fecha.*

### Alterado — a peça 15 inteira, na escala nova

**Ela subiu no mesmo commit da decisão**, que é o único jeito de a lição nº 9 não morder.

| onde | o que mudou |
|---|---|
| **§3.6, tabela do orçamento** | `2·3·4·6·8·9` viram `8·12·16·24·32·36`, com a linha nova que **declara o passo**: *"cada marco dá `4` pontos, e a base no nível 2 é `8`"* |
| **§3.7, catálogo de `Traço`** | o degrau 1 abre em `2 · 3 · 5 · 7`; o degrau 2 inteiro vai para `8` |
| **§3.7, catálogo de `Comando`** | `Investir` fica em 0; o degrau 1 vai para `4` e o 2 para `8` |
| **§3.7, as duas réguas de criar o seu** | os degraus renomeados para a escala nova, com a sub-régua escrita linha a linha |
| **§3.7, os seis shikigami do material** | as somas recalculadas — *e o **nível em que cada um cabe não mudou**, que é a prova de que a escala é uniforme* |
| **`conferir-invocacoes.py`, checagem 9** | o passo do marco deixa de ser implícito e passa a ser **lido do documento**, com a base declarada conferida contra a derivada |

> **A busca exaustiva caiu de `21.502` para `5.429`, e o motivo tem nome: paridade.** Com preços de `1` e `2`, quase todo subconjunto fechava o orçamento exato. Com `2 · 3 · 4 · 5 · 7 · 8` num orçamento par, **um número ímpar de itens de preço ímpar nunca fecha.** *A busca conta gasto exato; o conjunto de montagens **legais** caiu bem menos — medido em `0,78` a `0,90` do que era.* **É propriedade da moeda quebrada, e está escrito na peça em vez de escondido.**

**Arnês, na cópia isolada, com a base conferida verde antes e o `diff` provando cada `sed`:**

| perturbação | acendeu? |
|---|---|
| o passo do marco vira `3` na linha declarada | **sim** |
| a base declarada vira `9` e a tabela fica em `8` | **sim** |
| a linha que declara o passo some | **sim** |
| o `Miúdo` volta a custar `1` | **sim** |
| o orçamento do nv30 vira `35` | **sim** |
| **contra-teste:** muda a prosa do que o `Faro` faz | **não acendeu** |
| **contra-teste:** mexe num número de outra seção | **não acendeu** |

*O primeiro é o que dá valor aos outros quatro: até a v0.66 o passo do marco era `1` e estava **implícito** no código. Um passo implícito não acende quando muda — ele só some.*

### Alterado

| onde | o que mudou |
|---|---|
| **`RASCUNHO-trilhas.md` §6.4** | o formato das três, as travas da matriz, a moeda e a trava do corpo a corpo |
| **`RASCUNHO-trilhas.md` §6.5** | a parede do Evocador, as três tentativas que caíram e as duas dívidas da peça 15 |
| **`RASCUNHO-trilhas.md` §6.6** | a escala nova, a sub-régua do degrau 1 e a prova de que a entrega compra coisa |
| **peça 6 §3.1** | o slot do golpe do `Arremate` e do `Coro`, com o gate e a dívida de validador |

### Em aberto

- **As doze entradas.** O formato fechou, o conteúdo não — é o resto da Q5 para o Evocador.
- **A regra do slot não tem validador dono.** Nenhum `conferir-*.py` lê a forma do ataque extra: trocar o slot ou apagar o gate **sai verde hoje**. Entra com o validador de Trilhas, cuja especificação está no §5 do rascunho.
- As de sempre: as vagas de Desliga, a Cicatriz, Energia Reversa, o clash, o nome do sistema, o refino que paga mal no marco.

---

## [0.66] — 2026-08-15

**As skills instaladas estavam atrás da pasta outra vez — e desta vez o aviso que manda mantê-las em dia já estava escrito nos dois lugares.** *A v0.63 e a v0.64 fecharam as duas dizendo "aplicada nos dois lados dela".* A instalada não tinha nenhuma das duas. Nada de regra mudou aqui: continuam dezesseis peças e dezesseis validadores.

### Achado — a `rpg-da-guilda` instalada estava 39 linhas atrás da pasta

Medido por `diff`, descontando o cabeçalho de frontmatter. O que faltava do lado instalado:

- os dois validadores de `manual/matematica/` no bloco de comando, e a nota de que o `subir.sh` roda os três blocos
- **o caminho de commit de verdade** — `jjk` e `./subir.sh` pelado, com a mensagem deixada em `mensagem-de-commit.txt`
- ler `.git/logs/HEAD` como arquivo para saber em que commit a pasta está sem rodar git
- a lição do **eixo errado** no arnês de perturbação
- **a seção inteira de como FALAR com o Mizuki** — que é exatamente o que a v0.64 saiu para consertar
- a sétima skill na lista, a nota de que o `LEIA-ME` lista as mesmas sete, e o eval que cobre quatro delas
- a armadilha do ponteiro de seção

**É a lição *"decisão registrada não é decisão aplicada"* na camada em que nenhum validador chega.** Duas versões escreveram "nos dois lados"; ninguém conferiu depois.

### Achado — e o pior não era a divergência: as quatro skills com pasta de apoio não têm pasta de apoio instalada

*Isto nunca tinha sido medido.* A `design-mecanicas-rpg` instalada termina com uma seção **"Arquivos de apoio"** mandando ler `references/matematica-de-dado.md` e `references/vocabulario.md`. **Do lado instalado não existe nenhum dos dois.** Nas outras três, igual:

| skill | o que o texto instalado manda ler | está instalado? |
|---|---|---|
| `design-mecanicas-rpg` | `references/` — dois arquivos | **não** |
| `balanceamento-simulacao` | `scripts/dados.py` e `scripts/busca-exaustiva.py` | **não** |
| `playtesting-rpg` | `assets/` — os dois formulários | **não** |
| `redacao-acessivel-rpg` | `references/` — dois arquivos | **não** |

*O contraste que fecha o diagnóstico: as skills de sistema instaladas na mesma conta trazem as pastas delas normalmente.* O que falta é o conteúdo destas quatro, não o suporte a pasta.

> **Ponteiro pendurado dentro da ferramenta é pior que texto desatualizado.** Texto velho dá conselho errado, e dá para desconfiar dele. Ponteiro pendurado manda quem está seguindo a skill abrir um arquivo que não existe — e a conclusão natural é que a skill está quebrada.

**E ele desmente uma frase escrita na v0.3 e repetida desde então:** o `LEIA-ME` diz que *"a versão instalada traz esse conteúdo embutido"*. **Não traz.** O `SKILL.md` instalado é o da pasta, ponteiro e tudo. *A frase nasceu na própria entrada da v0.3 deste arquivo — "com os arquivos de apoio que a versão instalada traz embutidos" —, e aquela entrada fica como está, porque a v0.50 decidiu não reescrever histórico.* **O `LEIA-ME` foi corrigido, e o `ESTADO-ATUAL` ganhou o achado.**

### Alterado — sete lições de v0.60 a v0.65 entraram nas skills

*As de assunto nasceram na v0.3, em 06/08, e a `design-mecanicas-rpg` e a `redacao-acessivel-rpg` não eram escritas desde aquele dia.* Sessenta versões depois, o CHANGELOG tinha lição medida que generaliza para fora deste projeto e nunca tinha sido varrido para isso.

| skill | o que entrou | de onde |
|---|---|---|
| `rpg-da-guilda` | **quando ele diz que não entendeu, procure o defeito antes de reexplicar** — dois seguidos: a palavra com dois sentidos, e a pergunta de leitor que derrubou o empréstimo | v0.64 · v0.65 |
| `design-mecanicas-rpg` | **ou a trilha é fechada, ou cada entrada carrega pré-requisito**, e nenhuma entrega pode depender de outra — com os três modelos publicados e o que cada um cobra | v0.65 |
| `design-mecanicas-rpg` | **pelo menos uma entrada precisa ter botão**, e uso limitado na entrada de abertura é o erro simétrico | v0.65 |
| `design-mecanicas-rpg` | **contador que cresce em cima de magnitude que já cresce conta duas vezes**, e por que *usos = proficiência* funciona no 5e e não aqui | v0.61 |
| `design-mecanicas-rpg` | **dead level** — o nome do vão, as erratas do 3.5, o princípio do PF2e, o preço que o 4e pagou, e medir vão em sessão e não em nível | v0.60 |
| `balanceamento-simulacao` | **a matriz só enxerga os eixos que ela tem coluna** — e quando não existe número que conserte dentro deles, falta uma coluna e não um valor | v0.63 |
| `pesquisa-antes-de-propor` | **ir ao dono não basta: confira que leu a coluna que o dono nomeou** | v0.60 |

**Nenhuma delas carrega número deste projeto.** O filtro foi esse: entra o que continua verdadeiro num sistema que não é este. Preço, teto e calendário ficaram onde já moram.

### Registrado — a deriva tem três sentidos, e esta versão viu os três

A v0.37 achou o repositório atrás da instalada. A v0.40 achou o contrário, nas cinco. **Esta achou as duas coisas ao mesmo tempo:** a `rpg-da-guilda` instalada atrás da pasta, e as de assunto com pasta e instalada empatadas — as duas atrás do CHANGELOG.

> **O que continua não existindo é uma data de última sincronização.** Enquanto ela não existir, a única resposta honesta a *"qual lado está certo?"* é abrir os dois e comparar com o CHANGELOG, que é o dono do que foi decidido.

### Em aberto

- **Uma checagem que conte skill.** Marcada como candidata na v0.38 e de novo na v0.40. Continua sem existir, e esta é a terceira versão que ela teria pego.
- **A varredura de v0.4 a v0.59 não foi feita.** Esta versão leu v0.60 a v0.65 procurando o que generaliza. Sobra uma faixa de cinquenta e poucas versões que ninguém passou o pente.
- **Os arquivos de apoio têm de ir junto toda vez que a skill for reinstalada**, senão o ponteiro pendurado volta.
- As de sempre: as vagas de Desliga, a Cicatriz, Energia Reversa, o clash, o nome do sistema, o refino que paga mal no marco — e **a Q5 de Trilhas**, que é onde o trabalho para.

---

## [0.65] — 2026-08-14

**A Q4 de Trilhas foi reaberta e refeita: a Trilha virou fechada, e no lugar do empréstimo entrou TROCA.** *A pergunta do Mizuki que derrubou a decisão da v0.55 foi de leitor, não de designer* — e é o segundo achado seguido que veio de ele não entender uma coisa que estava errada.

### O que ele perguntou

> *"Não seria melhor poder escolher outras trilhas em qualquer nível? Digamos que eu tô no nível 11 e quero tentar a outra trilha que achei interessante — aí eu pego o nível 2 de outra trilha, em vez do nível 11 de outra trilha."*

E depois, com a conta na mesa: ***"acredito que só remover completamente a mistura das trilhas vai ser melhor... manter a forma de 405 rende em deixar pegar trilhas sem ter a base da trilha e fica estranho."***

### Achado — a trava que faltava, e ela valia nos dois modelos

**Nenhuma entrega pode depender de outra entrega.** *Isso nunca tinha sido escrito em lugar nenhum* — conferido com `grep`, zero ocorrências. E o empréstimo da v0.55 já exigia isso: pegar o degrau de nível 11 do `Punho` sem nunca ter tido o de nível 2 dele já era possível, e nada proibia que o de cima dependesse do de baixo.

### Levantamento externo — existem três modelos e nenhum quarto limpo

| sistema | como resolve |
|---|---|
| **D&D 5e**, 2014 e 2024 | **trilha fechada.** Sem misturar, e **sem regra nenhuma de trocar** — nas duas edições é discricionariedade de mestre |
| **Pathfinder 2e** | **pool com pré-requisito escrito em cada entrada** — *"prerequisites can be a specific class feature, or another feat"* |
| **Pathfinder Society** — personagem entre mestres, o caso mais parecido com este | **rebuild completo, uma vez só, com data para expirar.** Mudar de rumo é evento excepcional e central |

> **Ou cada entrada carrega pré-requisito, ou a trilha é fechada.** A forma de 405 era exatamente o meio-termo que nenhum dos três pratica.

### E o próprio projeto tinha o argumento a favor de fechar

A peça 5 §4: *"se o Caminho desse dano, dois personagens do mesmo Caminho começariam a se parecer, e a coisa que os distingue — **a técnica que cada um escreveu** — perderia espaço."*

**A Trilha nunca foi o motor de variedade — a técnica é**, e cada jogador escreve a dele do zero. *Quinze Trilhas fechadas não é pouco: é a quantidade certa para uma camada que não carrega a individualidade.*

### Decidido — a Trilha é fechada, e a troca é total

> **As quatro entregas de Trilha (`2 · 11 · 19 · 27`) são todas da sua Trilha.**
> **Nos níveis `11`, `19` e `27` você pode trocar de Trilha dentro do Caminho, e a troca é TOTAL** — tudo o que você tinha vira o equivalente da nova. Você é sempre exatamente uma Trilha.

| | antes (v0.55) | agora |
|---|---|---|
| montagens a conferir | **405** | **15** |
| pegar o avançado sem o básico | acontecia, e nada proibia | **impossível** |
| mudar de ideia | não existia | **troca total em 11, 19 ou 27** |
| pré-requisito em cada entrada | seria obrigatório | **desnecessário** |

*A troca parcial foi medida e recusada: guardar o passado e seguir a Trilha nova recria exatamente o defeito que a pergunta apontou.*

### Decidido — o formato voltou a ser livre por Trilha, com duas travas

**A regra da v0.64 — altura fixa por nível — caiu junto com o empréstimo**, porque os dois motivos dela eram o empréstimo e o tamanho da matriz. *Com Trilha fechada, o formato passa a ser o que faz uma Trilha parecer diferente da outra.*

> **1. O nível 2 é sempre `Classe Passiva 1` ou `3`.** Nunca uso limitado.
> **2. Pelo menos uma das quatro tem de ser `Classe Passiva 2`** — algo que o jogador decide usar.

**A primeira é do Mizuki:** *"o nv2 tem que dar a BASE para tudo funcionar, como algo passivo mesmo ou que proca às vezes"*. A conta já proibia condicional-de-baixa-taxa ali; o que faltava era o outro lado — **uso limitado no nível 2 é pior ainda**, porque a única coisa da Trilha vira recurso para administrar antes de existir qualquer outra na ficha.

**A segunda veio de fora, e ela existe porque a preferência dele levada ao extremo tem nome no hobby.** Ele escreveu *"tudo deveria ser entre sempre ligado e às vezes"* — e subclasse **só** de passiva e proc é o **Champion do D&D 5e**:

> *"Most of its features are passive… **this is a subclass that is absolutely desperate for some buttons to push**… this simplicity makes the Champion an ideal character for **new players**, but **veterans will likely find it boring**."*

**A última frase é a resposta inteira: passivo é certo no começo e errado no fim** — que é exatamente o que ele desenhou sem saber.

### Achado — a preocupação com "uma vez por luta" não se confirma, e a peça 10 tem o número

*Ele escreveu: "tem dias que não vai ter mais de uma luta".* **A peça 10 §4 diz que as três primeiras lutas do dia são de graça**, e a exaustão começa na quarta. **O dia esperado tem três a quatro lutas**, então `1× por descanso curto` dispara **três a quatro vezes por dia**, contra uma do `1× por dia`. *E o levantamento externo separa os dois pelo mesmo motivo — o Stoddard reprova o `por dia` e libera o `por descanso curto`.*

### Alterado

| onde | o que mudou |
|---|---|
| **`RASCUNHO-trilhas.md` §3** | a Q4 refeita, o §3.6 reescrito, o §1 e o §5 acompanhando |
| **peça 6 §1** | a linha *"as Trilhas seguintes se acumulam com o nível"* — morta em duas etapas, e agora com a troca escrita no lugar |
| **`ESTADO-ATUAL`, pendência nº 3** | a Trilha fechada e a troca |

### Em aberto

- **A Q5** — as 80 entradas. **O validador de Trilhas ganhou três checagens novas na especificação** e ainda não existe.
- As de sempre: as vagas de Desliga, a Cicatriz, Energia Reversa, o clash, o nome do sistema, o refino que paga mal no marco.

---

## [0.64] — 2026-08-14

**`Classe` era uma palavra fazendo o trabalho de duas, e o dono do sistema não conseguiu ler a própria régua por causa disso.** O Mizuki leu a Q3 de Trilhas inteira e parou em *"como assim Classe? Pra mim Classe é feitiço, não entendi a questão"*. **Ele estava certo, e o defeito é do projeto.** Continuam dezesseis peças e dezesseis validadores.

### Achado — o glossário do manual só tem uma escala, e o eixo de formato vivia de empréstimo

> **`Classe — o tamanho do feitiço, de 0 a 7. Define pontos, teto, PE e limites.`** *(glossário do manual)*

E ele também escreve *"cada Passiva tem uma Classe, **como um feitiço**"*, com a tabela de níveis dizendo *"7 — libera Passiva de Classe 2"*. **Então `Classe 2` já significava duas coisas antes de a peça 11 abrir a boca** — e ela passou a usar `Classe 1/2/3` para o eixo de **formato** (pequeno e condicional · reativo com limite · permanente) sem nunca marcar a diferença.

*O agravante que a palavra escondia:* na Passiva do manual a altura **também cobra** — Classe 3 custa mais espaço de feitiço que a 1. Na aptidão **não cobra nada**: o marco compra uma de qualquer altura que o refino alcance. **A mesma palavra tinha três comportamentos** — mede tamanho no feitiço, mede tamanho e preço na Passiva, mede só formato na aptidão.

### Decidido — `Classe Passiva`, e nunca `Classe` sozinha

*Decisão do Mizuki.* **O conserto é o idioma do próprio manual**, que já escreve *"Passiva de Classe 2"* e *"Classe de Passiva"* quando precisa desambiguar.

**A triagem rodou e cinco candidatos foram RECUSADOS de propósito:** `Feitio`, `Talhe`, `Lavra`, `Feição` e `Formato` saíram **LIVRE** nas duas direções, e `Porte` saiu fraco (a uma letra de `Corte`, que é Tema). *Inventar palavra para o que o manual já sabe dizer cria a segunda fonte que a lição nº 9 existe para evitar* — e um termo que o manual não tem obriga toda leitura futura a traduzir.

### Achado — a escada de formato não foi inventada aqui, e agora a peça prova isso

A seção 4 ganhou a coluna que faltava: **quais Passivas do manual moram em cada altura.**

| Classe Passiva | as Passivas do manual naquela altura |
|---|---|
| **1** | `Leitura` · `Instinto` · `Raiz` · `Mão Firme` · `Farejador` · `Aviso` — todas *"você sabe"* ou *"você não sofre"* |
| **2** | `Fluxo` · `Recomposição` · `Segunda Natureza` · `Eco` · `Costura` — todas *"uma vez por X, acontece"* |

**A escada estava na tabela do manual. O que faltava era alguém escrever o que ela separa** — e é isso que a peça 11 §4 fez na v0.27, sem nome próprio para o que tinha achado.

### Adicionado — a checagem do nome, no `conferir-aptidoes.py`

Ela afirma a **forma** do nome e nunca o conteúdo: o título e o cabeçalho da tabela dizem `Classe Passiva`, a regra *"nunca sozinha"* está escrita, e as três alturas estão lá.

> **E ela precisou da exceção da armadilha nº 4 do projeto** — *a peça que documenta o validador contém o texto que ele procura para reprovar.* A seção 4 **cita o manual** para explicar a ambiguidade, então ela contém `Classe 2` solta duas vezes, legitimamente. A varredura pula a linha que menciona o manual, e só ela. *Sem isso a checagem reprovaria a própria seção que existe para consertar o problema.*

**Arnês, base verde e `diff` por `sed`:**

| perturbação | acendeu? |
|---|---|
| o título volta a ser `As Classes de aptidão` | **sim** |
| a regra *"nunca sozinha"* some | **sim** |
| o cabeçalho da tabela volta a `Classe` | **sim** |
| alguém escreve `Classe 3` solta fora de citação | **sim**, listando as duas |
| **contra-teste:** muda o texto do que cabe na altura 1 | **não acendeu** |
| **contra-teste:** mexe numa linha que cita o manual | **não acendeu** |

### Decidido — a altura é do NÍVEL, e a conta decidiu por dois eixos independentes

**O empréstimo da Q4 exige.** Nos níveis 11, 19 e 27 três entradas do Caminho competem pela mesma vaga. Na média empatam por construção; **na variância não** — a Classe Passiva 1 não faz nada em **44% das lutas** e é a única com desvio (`4,89`). Com alturas misturadas, o empréstimo vira compra de confiabilidade, e a Q4 existe para ele ser de ficção.

**E a matriz confirma pelo outro lado:** altura livre por entrada dá **2.187** combinações, uma-de-cada dá 972, e a altura por nível dá **27** — que mantém as 405 montagens que a Q2 aprovou.

### Decidido — a sequência, e duas pontas a conta fechou sozinha

> **`2 · 11 · 15 · 19 · 23 · 27 · 29` → `3 · 2 · 1 · 3 · 1 · 2 · 3`**

**O nível 2 não pode ser Classe Passiva 1:** são **18 missões** com uma entrega de Trilha só na ficha, e uma altura que falha em 44% das lutas seria a Trilha inteira falhando quase metade do tempo para um personagem novo. **O nível 29 também não**, invertido — ele é carregado por **10 missões**, e coisa que se vê pouco tempo pede formato que aparece sempre.

*As duas condicionais caem nos degraus de Caminho (15 e 23), então a Trilha — a identidade — é sempre confiável, e o tempero mora na camada compartilhada. A Classe Passiva 2 no nv27 é gosto, e está assumida como tal no §3.6.*

### Registrado — o jeito de falar com ele virou procedimento, e o motivo é o mesmo defeito

*Pedido do Mizuki no fim desta versão:* ***"tô começando a me sentir perdido com o que você fala, tem alguma forma de explicar de forma mais leiga?"***

**É o mesmo defeito da seção acima, um nível acima.** A palavra `Classe` significava duas coisas e ele travou; a **conversa inteira** vinha significando duas coisas — texto de referência e explicação — e ele travou de novo. *O dono do projeto se perdeu no próprio projeto porque o chat estava sendo escrito com a densidade de um documento.*

**A skill `rpg-da-guilda` ganhou uma seção 0**, em primeiro lugar de propósito, com o registro separado: uma ideia por parágrafo, nada de `§3.4` no meio da frase, termo do projeto com a tradução colada na primeira vez, número sempre com a unidade por extenso, e **quando ele perguntar "como assim?", a resposta certa é menos detalhe e não mais.** Aplicada nos dois lados dela.

> **E a ironia vale registrar:** o projeto tem uma skill chamada `redacao-acessivel-rpg` — *"escreve texto de regra para quem nunca jogou entender de primeira, define jargão antes de usar"* — e ela nunca tinha sido apontada para a conversa. O defeito que ela descreve aconteceu **no chat**, não no documento.

### Em aberto

- **A Q5** — as 80 entradas, agora com formato, preço, contador e altura por nível fechados.
- **Quando a vida cheia da invocação reinvocada volta** — sabor.
- As de sempre: as vagas de Desliga, a Cicatriz, Energia Reversa, o clash, o nome do sistema, o refino que paga mal no marco.

---

## [0.63] — 2026-08-14

**A Q6 fechou, e com ela a peça 15 inteira — ela não deve mais nada.** Era a única pergunta que Invocações tinha deixado aberta, e ela nunca foi daquela peça: `Servo`, `Matilha` e `Coro` são Trilhas. **O que a destravou não foi um número.** Continuam dezesseis peças e dezesseis validadores.

### Achado — o `Servo` estava dominado por falta de EIXO, não por magnitude

A peça 15 declarava duas dominâncias pendentes, `Matilha > Servo` e `Coro > Servo`, as duas apontando para o mesmo lugar. Rodando a matriz nos três eixos que o validador usava:

| Trilha | saída | corpos | ação |
|---|---|---|---|
| `Servo` | 1 Rotina | 1 | comanda |
| `Matilha` | 1 Rotina | **5** | comanda |
| `Coro` | 1 Rotina | 1 | **ataca e comanda** |

**O `Servo` não estava na frente em nada.** E **não existia número que consertasse dentro dos três** — subir a saída fura o teto da peça 6 §4, dar corpo o transforma na `Matilha`, dar ação o transforma no `Coro`. *A Q6 estava esperando uma **coluna nova na matriz**, e o número vinha depois dela.*

### Decidido — os dois eixos, e o argumento é do Mizuki

> *"Normalmente é a única invocação da pessoa, então ela tem de ser o equivalente de todas as outras, **mas não passar muito delas**. Por ser o mais simples, ela não pode dar um ganho maior que os outros — um exige capturar muitas invocações para valer a pena e o outro exige ir para o combate corporal. Mas ao mesmo tempo ele não pode ser muito abaixo, **já que ao perder a invocação principal, acabou o kit da pessoa**."*

**A trava do fim tem tamanho, e ele é `5×`.** A regra de morte do §3.5 lê a **vida máxima** para decidir morte em definitivo, e com `h` a do `Servo` era um quinto da da `Matilha` — para a **mesma Rotina entregue**:

| nv | vida do corpo (`h`) | pool da `Matilha` (`5h`) | rodadas de chefe concentrando |
|---|---|---|---|
| 2 | 6 | 30 | `Servo` **0,8** · `Matilha` 4,0 |
| 10 | 22 | 110 | 1,7 · 8,5 |
| 30 | 62 | 310 | 1,7 · 8,6 |

> **A concessão:** o corpo do `Servo` tem **`5 × h`** — o pool inteiro da `Matilha` num corpo só — e **o orçamento da ficha mais metade**, arredondando para baixo.

**A vida iguala e o orçamento diferencia.** Com `5h` os dois passam a sair da luta pelo mesmo golpe, e apagar o `Servo` custa as mesmas `1,25` Rotina de área por alvo que o §3.5 já media para apagar a `Matilha` — **nenhuma exceção nova, a regra continua valendo palavra por palavra e o que mudou foi o número que ela lê.** O orçamento vai de `2→3` no nv2 a `9→13` no nv30, que é 46% do que compraria o catálogo inteiro.

**E o *"não passar muito delas"* está medido:** a `Matilha` compra `9` no nv30 e **aplica os nove cinco vezes**, um por corpo. Em largura de utilidade ela continua na frente; o que o `Servo` compra é profundidade num corpo só. *O `Coro` fica com `h`, e essa é a troca dele escrita: ele é o único que ataca e comanda, e o único cujo corpo cair não acaba o kit.*

### Achado — a vida NÃO entra por dominância, e é por isso que ela precisou de checagem própria

**Só o orçamento já zera a matriz.** Medido: com o `Servo` em `orçamento ×1,5` e vida `h`, as seis comparações dão **zero dominância**. Ou seja, **tirar o `5h` sairia verde** e desfaria em silêncio a metade da Q6 que a matriz não mede — a de *"perder o corpo acaba o kit"*.

> *É a lição nº 8 entrando por outra porta.* Ela diz que uma checagem não pode se medir contra a própria constante; este é o primo dela — **uma checagem que se mede pelo eixo errado sai verde exatamente na perturbação que importa.** O conserto foi o mesmo: separar as duas coisas e conferir as duas.

### Alterado — o `conferir-invocacoes.py`

- **`DOMINANCIA_PENDENTE_Q6` foi a conjunto vazio.** Se alguma dominância voltar, a checagem 2 falha em vez de aceitar calada.
- **A matriz ganhou os dois eixos**, lidos da tabela *"O que cada Trilha concede"* do §3.7 — **nunca de constante dentro do arquivo**. Se a tabela sumir ou mudar de formato, ele falha alto dizendo que os dois eixos virariam constante escrita.
- **Uma checagem nova de vida**, separada da matriz, com a mensagem nomeando por quantas vezes o gatilho de morte do `Servo` seria menor.

**Arnês, na cópia isolada, base verde antes e `diff` provando cada `sed`:**

| perturbação | acendeu? |
|---|---|
| o `Servo` perde o orçamento maior | **sim** — `Matilha domina Servo nos três eixos e não está declarada` |
| o `Servo` perde a vida de `5h` | **sim** — e a matriz sai **zero dominâncias**; quem acusa é a checagem de vida |
| a tabela do §3.7 some | **sim**, dizendo que os dois eixos virariam constante |
| **contra-teste:** o `Coro` ganha orçamento maior também | **não acendeu** — ele ganha em ação e perde em vida, e ninguém domina ninguém |

*O segundo é o que dá valor a esta versão inteira: ele é a prova de que a matriz sozinha não bastava.*

### Documentado — o caminho de commit do Mizuki, que nunca tinha sido escrito

*Pedido dele.* A documentação dizia `./subir.sh "o que mudou"`, e o que ele roda de verdade são **duas linhas**:

```bash
jjk               # o atalho que entra na pasta do repositório
./subir.sh        # sem argumento: usa o mensagem-de-commit.txt e apaga depois
```

**Consequência para quem escreve daqui em diante: o último passo é deixar a mensagem em `mensagem-de-commit.txt` e avisar** — não sugerir mensagem por argumento, porque ele roda o script pelado. Está no `README` §*Commitar* e no §7 da skill `rpg-da-guilda`, **nos dois lados dela** (a pasta `sistema/skills/` é cópia de trabalho e não altera a instalada).

> **E a seção de commit do README carregava um número velho.** Ela dizia *"os **dezoito** validadores — os **quinze** de `03-mecanica/`"* quando são dezenove e dezesseis. **Escapou porque o `conferir-repositorio.py` confere a linha de versão do topo e não a prosa.** O conserto não foi atualizar o número: foi **tirar ele** — a frase agora diz *"todos os validadores"* e aponta para a linha do topo, que é a dona. *Lição nº 9 na forma mais barata: a contagem que não é copiada não envelhece.*

**Entrou junto no §5 da skill uma lição desta versão:** *uma checagem que se mede pelo **eixo** errado sai verde exatamente na perturbação que importa* — o primo do "não se meça contra a própria constante", e ele apareceu aqui pela primeira vez.

### Alterado — o resto

| onde | o que mudou |
|---|---|
| **peça 15 §3.7** | a tabela *"O que cada Trilha concede"*, com as duas colunas novas e a conta da vida |
| **peça 15 §1 e §3** | a Q6 marcada como fechada nos três lugares em que ela era citada como aberta |
| **`RASCUNHO-trilhas.md` §6.3** | de pergunta aberta para decisão fechada, com o argumento do Mizuki citado |
| **`ESTADO-ATUAL`** | o bloco de Invocações: a Q6 fechou, e o que sobrou pendurado é uma linha |

### Em aberto

- **A Q5 de Trilhas** — as 80 entradas. O bloco do Evocador é o primeiro, e agora ele tem as três concessões com número.
- **Como as Classes se distribuem nos 8 degraus** — livre com teto, fixa por nível, ou uma de cada mais uma livre. *Ainda não costada.*
- **Quando a vida cheia da invocação reinvocada volta** — o candidato natural é o descanso longo, e é sabor.
- As de sempre: as vagas de Desliga, a Cicatriz, Energia Reversa, o clash, o nome do sistema, o refino que paga mal no marco.

---

## [0.62] — 2026-08-14

**A dívida que a v0.61 anotou virou definição, e a definição desfez a decisão que a criou.** *"Cena" não tinha dono em documento nenhum* — a escada de relógios da peça 10 §5 está no projeto desde a v0.23 e o degrau mais usado dela nunca tinha sido definido. **Definido, ele reprova o contador que a v0.61 escolheu.** Continuam dezesseis peças e dezesseis validadores; o que entrou foi a **checagem 9 do `conferir-descanso.py`**, que é o dono daquela escada.

### Decidido — o que conta como uma cena

*Definição do Mizuki, e ela é do mesmo formato do "o que conta como uma luta" da seção 4:*

> **Quem conta é o mestre.** Uma cena pode ser uma sala, ou um segmento de salas, ou um combate. **Ela acaba quando a pressão daquele pedaço acaba.**

Está na **peça 10 §5**, que é a dona da escada.

### Achado — e é por isso que a v0.61 escolheu o degrau errado

Medido pela metodologia da **peça 13 §7**, que é a única do projeto que já tinha medido relógio contra o filtro multi-mestre:

| como o mestre lê | rolagens no período | usos por combate |
|---|---|---|
| a sala, ou o próprio combate | 4,7 | 1,00 |
| um segmento curto | 9,4 | 0,50 |
| o piso inteiro | 14,1 | 0,33 |

**Spread de `3,0×` — e é exatamente o número com que a peça 13 §7 reprovou *"por sessão"* e *"por arco"***, escrevendo que ali *"o filtro do projeto — dois mestres que nunca conversaram chegam ao mesmo número? — está falhando, com número em cima"*. **O projeto já tinha rejeitado esse spread, com essa conta, num degrau vizinho — e ninguém tinha voltado para olhar o `por cena`.**

### Achado — e mesmo assim os 71 `por cena` do catálogo de Legados continuam certos

A trava daquela peça **mede largura antes de relógio**: *"por cena num gatilho de alcance 1 é seguro por construção, não por generosidade"*. Quando o gatilho é estreito — uma perícia nomeada, um Teste de Resistência nomeado —, quem limita é a frequência do próprio gatilho, e o relógio quase não morde: o `Instinto Bruto` vale +20 pp quando dispara e **1,0 pp médio na ficha, com ou sem relógio.**

> **Então a regra que a peça 10 §5 passou a escrever é sobre quem limita:**
> **gatilho estreito** → `por cena` é seguro, e o catálogo de Legados fica inteiro.
> **o relógio é o único limitador** → desce para `por descanso curto`, cujo gatilho de ficção a peça 10 §1 escolheu porque *"a luta acabou"* dois mestres arbitram igual.

**A Classe 2 de Trilha é o segundo caso** — o gatilho dela é combate, e combate acontece toda missão. *E a troca não move número nenhum:* os dois são degraus vizinhos (`4,7` contra `6,3`, `1,34×`) e os dois dão um uso por luta. A magnitude continua `4,70`. **O que muda é quem decide quando ele volta.**

### Alterado — a régua da Q3, no único ponto em que ela dependia disso

O §3.2 do `RASCUNHO-trilhas.md` trocou `1× por cena` por **`1× por descanso curto`**, com a medição acima escrita. O resto da régua não se moveu.

### Adicionado — a checagem 9 do `conferir-descanso.py`

> **Os quatro degraus da escada saem da tabela da peça 10 §5 e cada um tem de dizer quando recarrega; o degrau `por cena` tem de ter seção própria dizendo o que conta como uma; e os dois totais publicados na peça são RECONTADOS da pasta.**

**PAR DECLARADO com a checagem 2 do `conferir-legados.py`**, que lê a mesma tabela pelo outro lado — lá para reprovar relógio de Legado fora da escada, aqui para exigir que a escada esteja definida.

**E a peça 10 fica de fora da própria contagem**, porque ela é a dona do relógio: a prosa dela sobre `por cena` não é um uso, e o total oscilaria a cada edição da seção. *É a armadilha de a peça que documenta o validador conter o texto que ele procura.*

> **A lição nº 1 cobrou duas vezes na mesma linha antes de o validador existir.** A primeira versão dela dizia **`130`**, que saiu de contar *linhas que continham a palavra cena* — e *"por cena"*, *"a cena anda"*, *"tem cena provando"* e *"fora da cena"* são quatro coisas diferentes. A segunda dizia **`94`**, que era a contagem certa e **envelheceu no mesmo commit**, porque escrever a seção criou ocorrências novas. O número certo é **`91`**, e ele não está mais escrito à mão em lugar nenhum.

**E entrou junto um cruzamento de lição nº 9:** o `4,7` da tabela de leituras é **cópia** da tabela de relógios da peça 13 §7. As duas cópias agora são comparadas, e a mensagem nomeia o dono.

**Arnês, na cópia isolada, base verde antes e `diff` provando cada `sed`:**

| perturbação | acendeu? |
|---|---|
| apagar a seção *"O que conta como uma cena"* | **sim** |
| esvaziar o gatilho do degrau `por dia` | **sim**, nomeando o degrau |
| total publicado `91` → `90` | **sim** |
| total do catálogo `71` → `70` | **sim** |
| peça 10 usa `4,9` e a peça 13 diz `4,7` | **sim**, nomeando o dono |
| **o dono muda:** peça 13 passa a dizer `5,2` | **sim** — acende dos dois lados |
| **contra-teste:** o `4,7` da tabela de leituras, sem tocar no dono | **não acendeu** |
| **contra-teste:** o `por dia` da peça 13, outra linha da mesma tabela | **não acendeu** |

### Achado — o Servo está dominado por falta de EIXO, não por magnitude

*O `RASCUNHO-trilhas.md` ganhou o §6, que é o primeiro bloco da Q5: o Evocador, que o §4 manda atacar primeiro porque as três Trilhas dele já têm máquina pronta na peça 15.* Rodando a matriz nos três eixos que o `conferir-invocacoes.py` usa:

| Trilha | saída | corpos | ação |
|---|---|---|---|
| `Servo` | 1 Rotina | 1 | comanda |
| `Matilha` | 1 Rotina | **5** | comanda |
| `Coro` | 1 Rotina | 1 | **ataca e comanda** |

**O `Servo` não tem nenhum eixo em que esteja na frente**, e é por isso que as duas dominâncias declaradas na peça 15 apontam as duas para ele. **E não existe número que conserte isso dentro dos três:** subir a saída fura o teto da peça 6 §4, dar corpo o transforma na `Matilha`, dar ação o transforma no `Coro`.

> **A Q6 não estava esperando um número — estava esperando uma coluna nova na matriz.** Qualquer quarto eixo em que só o `Servo` esteja na frente mata as duas dominâncias de uma vez. **O número vem depois dele.**

### Achado — e a régua da Q3 tem um limite aqui, que é melhor achar antes do catálogo

Os candidatos de quarto eixo são todos da peça 15, e **a régua não os preça em ponto de Rotina.** A fatia da Q3 é `1,27` ponto de **dano** por rodada; o ponto de orçamento de invocação compra `Traço` e `Comando`, que a peça 15 §3.7 **proíbe de tocar dado de dano**. Aquela peça já tinha escrito o aviso: *"o que não pode acontecer é as duas moedas caírem no mesmo saco"*.

**A régua não muda — o que ela exige é o que sempre exigiu**, que o eixo seja fração de coisa que já cresce. O orçamento de invocação é: ele sai dos sete marcos. *E ele cresce `4,5×` contra os `8,31×` da Rotina, então **deriva `1,8×` para baixo** — a mesma deriva dos espaços de feitiço, que o projeto já aceita. Fica registrado no §6.2 em vez de escondido.*

### Em aberto

- **Qual é o quarto eixo do `Servo`** — orçamento, amarra ou vida. **A conta não separa os três**, e por isso a escolha é de sabor. O §6.3 traz os três com o que cada um custa.
- **A Q5**, que é o resto do catálogo. O bloco do Evocador só começa depois da escolha acima.
- As de sempre: as vagas de Desliga, a Cicatriz, Energia Reversa, o clash, o nome do sistema.

---

## [0.61] — 2026-08-14

**A Q3 de Trilhas fechou: a régua existe, e o catálogo pode começar.** Ela é a última das quatro perguntas de estrutura — Q1 e Q4 na v0.55, Q2 na v0.60, Q3 agora —, e é a que a peça 13 contra a peça 14 diz ser a diferença entre uma versão e seis. Continuam **dezesseis peças e dezesseis validadores**; nada de arquivo novo, porque a régua mora no rascunho até a peça fechar.

### Achado — o calendário da Q2 já tinha resolvido a derivação, e ninguém tinha percebido

O §2.2 do rascunho registra desde a v0.54 que entrega de valor absoluto morre contra alvo que cresce, e cita o ponto de arma da peça 16 como o exemplar. **Vale para uma entrega. O número delas também cresce:**

| nv | entregas | entregas ÷ nv2 | Rotina ÷ nv2 | razão |
|---|---|---|---|---|
| 2 | 1 | 1,00 | 1,00 | 1,00 |
| **5 e 6** | 1 | 1,00 | 2,38 | **0,42** |
| 7 | 2 | 2,00 | 2,38 | 0,84 |
| 23 | 6 | 6,00 | 7,23 | 0,83 |
| **26** | 6 | 6,00 | 8,31 | **0,72** |
| 30 | 8 | 8,00 | 8,31 | 0,96 |

A Rotina cresce **8,31×** e o número de entregas cresce **8,00×**. **Uma entrega de valor plano fica em fração quase constante da Rotina do nível 7 ao 30**, com espalhamento de `1,33×`. Os dois buracos são a Rotina subindo de degrau antes de a entrega seguinte chegar, e são os únicos.

*Isso não estava planejado. A Q2 escolheu `2 · 11 · 19 · 27` e `7 · 15 · 23 · 29` por vão e por seca, sem olhar para derivação nenhuma — e o calendário saiu tracking a escada da Rotina de graça.*

### Decidido — a régua, em quatro linhas

> **Formato:** a escada de Classes da peça 11 §4. A Classe declara a **janela**, e a janela fixa a magnitude.
> **Contador:** plano — `1×` por cena ou por descanso. Nunca um que cresça.
> **Preço:** **sete fatias de `1,27` ponto por rodada**, mais o **degrau do nível 7**, que vale o vão da peça 6 §3 e substitui uma fatia.
> **Denominador:** toda entrega é fração de coisa que já cresce. Número solto deriva `8,3×` e só cabe no nível 2.

**A escada da peça 11 passa no teste que reprovou a da peça 13.** A régua dos três formatos põe **6 das 7 linhas do permitido no `Destranca`** — o `Desliga` é território de Origem e o `Ajusta` tem um morador legal só. A escada de Classes **corta a lista de travessa**: `5 · 5 · 6` moradores, cada linha morando nas três em tamanhos diferentes. E ela porta sem adaptação porque a peça 11 §4 já diz o que ela é — ***"ela não mede quanto, mede o quê"***.

**O que segura a Classe 3 lá é o refino, e ele está proibido aqui.** O substituto sai da definição das três: Classe 3 permanente entrega `1,27` em 100% das rodadas; Classe 2 entrega `4,70` em ~27%; Classe 1 entrega `6,35` em ~20%. **Mesma média, variância diferente** — é o mecanismo do *"Farejador não fica obsoleta"* funcionando sem refino.

### Decidido — o contador é plano, e é a lição nº 2 num lugar novo

A magnitude já é fração, então **ela já cresce 8,31×**. Contador que também cresça conta a mesma coisa duas vezes:

| contador | usos nv2 | usos nv30 | cresce | contra a Rotina |
|---|---|---|---|---|
| `1×` por cena · `1×` por descanso curto | 1,0 | 1,0 | 1,00× | **não deriva** |
| PE, custo `1 × maior Classe` | 12,0 | 25,7 | 2,14× | deriva 2,1× **para cima** |
| PE, custo fixo em pontos | 6,0 | 90,0 | 15,00× | deriva 15,0× para cima |
| usos = maestria, por descanso | 1,0 | 4,0 | 4,00× | deriva 4,0× para cima |

> **E o padrão mais copiado do hobby é o que não serve.** *Usos iguais ao bônus de proficiência* — Tasha's, e depois o 5e de 2024 inteiro — funciona lá porque **a magnitude do feito é plana**, `"cause 1d6 a mais"`, e o contador crescente é o que faz ela acompanhar. Importar os dois aqui soma o que já estava somado.

**A peça 11 §4 já tinha decidido isso e ninguém tinha lido:** a definição de Classe 2 é *"efeito reativo, **com limite de uso por cena ou por descanso**"*. A conta não escolheu nada — ela explicou por que a definição está certa.

**Fica `1×` por cena**, que é o idioma que o projeto já fala: **71 usos na peça 13, 5 na peça 11, 4 na peça 16.** *E vai anotada a dívida que isso destampa: **"cena" não tem definição em documento nenhum.** Divergir por causa disso seria pior — oitenta usos de um lado e um do outro —, mas alguém vai ter de definir, e o candidato é o relógio da escada da peça 10.*

### Decidido — a fatia é plana, e a alternativa perdeu por um critério que não é o erro médio

A fatia sai de dividir o piso da peça 14 §4 no nível 30: `10,14 ÷ 8 = 1,27`. Contra a alternativa de a entrega do nível 2 ser maior:

| | oito iguais (`1,27`) | a do nv2 maior (`1,92` + `1,17`) |
|---|---|---|
| erro médio **pesado por missão** | **12,2%** | 13,2% |
| pior falta | −34% no nv5 | −16% no nv26 |
| pior excesso | +57% no nv2 | **+138% no nv2** |

*O erro foi pesado por missão e não por nível, pela curva da peça 12 — 145 missões do nv2 ao nv30 —, que é o mesmo critério com que a Q2 mediu seca.* Um ponto percentual não decide; **o `+138%` no nível 2 decide.** E o argumento que fecha é do Mizuki: *"no nv2 tem a questão de escolhermos a Trilha pro Caminho"* — **o peso de identidade está na escolha entre as três, não no tamanho do número.**

**O limite fica escrito:** com fatia plana, a Vanguarda fica 34% abaixo do piso do escudo nos níveis 5 e 6 — **4 missões de 145** — e entre 13% e 19% abaixo no miolo.

### Decidido — o ataque extra vai para o nível 7, e ele é o degrau de Caminho e não um degrau a mais

*Decisão do Mizuki, e ela conserta duas coisas de uma vez.* A peça 6 §3.1 punha o ataque extra no **nível 6** com o motivo *"é o primeiro marco, e é onde o resto do sistema já entrega coisa"* — **e esse motivo virou o argumento contrário** quando a Q2 mediu o calendário: o 6 é um dos quatro níveis mais cheios do sistema e o 7 não entrega nada. Pior, com ele no 6, Bastião e Vanguarda ficavam com **cinco degraus de Caminho** e os outros três com quatro.

**E medir o tamanho dele mudou a leitura da peça 6 §3 inteira:**

```
Rotina 108 · conjurador 99 (−8%) · físico 106 (−2%)
```

**Ninguém está acima.** O ataque extra não põe a Vanguarda na frente — ele tira ela de −8% e põe em −2%. **É correção de base, não bônus**, e por isso ele nunca coube como um degrau: ele vale de **3,2 a 5,5 fatias** e chega quando você só tem duas.

> **A regra: o degrau do nível 7 substitui uma fatia e vale exatamente o vão `físico − conjurador`.** Quem já tem rota para ataque extra recebe o ataque extra no lugar dele; quem não tem recebe o degrau grande.

| nv | Rotina | Vanguarda | Guia | `Arremate` | maior distância |
|---|---|---|---|---|---|
| 10 | 45 | 51,3 (+14%) | 51,3 (+14%) | 51,3 (+14%) | **0,0 pp** |
| 18 | 76 | 81,8 (+8%) | 81,8 (+8%) | 81,8 (+8%) | **0,0 pp** |
| 30 | 108 | 114,9 (+6%) | 114,9 (+6%) | 114,9 (+6%) | **0,0 pp** |

**Isso fecha o problema de design nº 2, aberto desde a v0.24**, com o número que a peça 6 §3.1 pediu: *"o que Elo, Sutura e Perímetro entregam que valha um golpe por rodada?"* — **valem o vão**, e o vão chega no nível 7.

*A saída que pagava o ataque extra em fatias foi medida e morreu: custa **6 das 8**, e Bastião e Vanguarda ficariam com seis níveis mortos — o que a Q2 saiu para matar.*

### Achado — os `6%` a `9%` da peça 14 são PISO, e ler eles como teto teria matado a régua certa

O orçamento passa de `9,4%` para `14,7%` da Rotina no nível 30, `1,57×` a âncora. **Isso não é violação.** A peça 14 §4 registra aquele número como o **buraco do escudo** — o que a Trilha **deve** para dar razão de largar o escudo. Estourar ele quer dizer que largar virou decisão fácil, que é literalmente o que aquela seção pediu.

**O teto de verdade é outro, e ele já estava escrito:** o **`+18%` sustentado que a peça 6 §3.1 reprovou** ao rejeitar *somar* o golpe. A régua para em `+6%`, com dez pontos percentuais de folga.

*Lição nº 5 na direção mais barata: eu ia tratar um piso como teto e reprovar a saída certa por causa disso. O texto do dono diz "deve", não "no máximo".*

### Achado — o refino cabe na conta e continua proibido, e é por isso que o contra-teste importa

O refino é o **melhor** denominador que existe numericamente: cresce `8,00×` contra os `8,31×` da Rotina. Uma checagem que só medisse derivação sairia **verde**. O que o reprova é a peça 11 §3 — as três escolhas de marco se equilibram porque **nenhuma compra o que a outra compra**, e a Trilha é bem comum:

| nv | refino de quem escolhe | de quem não | a Trilha ficaria | de graça |
|---|---|---|---|---|
| 14 | 6 | 5 | 20,0% maior | +1,5% da Rotina |
| 30 | 10 | 8 | 25,0% maior | +2,3% |

*E na direção contrária é pior:* quem vai sempre de `Corpo` ou de `Leque` termina com **zero aptidões**, e a Trilha é o único eixo que ainda escala para essas duas rotas.

### Arnês — a régua não tem validador ainda, então o arnês foi contra os donos

*Não entrou `conferir-*.py` nesta versão: a régua mora no rascunho e o validador nasce com a peça (§5 do rascunho é a especificação dele).* O que dá para provar hoje é que **os dois números publicados no §3 saem dos documentos donos e não da minha mão**. Numa cópia isolada, com a base conferida verde antes e o `diff` provando cada `sed`:

| perturbação | fatia | degrau do nv7 | acendeu? |
|---|---|---|---|
| base | `1,27` | `7` | — (reproduz o publicado) |
| peça 14 §4, buraco do nv30 `10,14` → `20,28` | **`2,54`** | 7 | **sim** |
| peça 6 §3, físico do nv30 `106` → `99` | 1,27 | **`0`** | **sim** |
| calendário da Q2 com sete degraus em vez de oito | **`1,45`** | 7 | **sim** |
| **contra-teste:** conjurador do **nv2** `18` → `11` | 1,27 | 7 | **não acendeu**, como tem de ser |

*O contra-teste é o que dá valor aos três primeiros.* Sem ele, os números poderiam estar lendo qualquer célula da tabela certa — que é exatamente como o `81` sobreviveu catorze versões.

### Alterado — o que se moveu, documento por documento

| onde | o que mudou |
|---|---|
| **`RASCUNHO-trilhas.md` §3** | a Q3 fechada, com os cinco sub-blocos: formato, contador, preço, o degrau do nv7 e o denominador |
| **`RASCUNHO-trilhas.md` §5** | seis checagens novas na especificação do validador, e a que dependia da Q1 riscada |
| **peça 6 §3.1** | ataque extra do nível **6** para o **7**, com o motivo antigo registrado como tendo virado o argumento contrário |
| **peça 6 §9** | duas das três perguntas riscadas — a de quantas Trilhas e a de `Elo`/`Sutura`/`Perímetro` |
| **peça 14 §5.2** | as três citações de *"ataque extra no nv6"* — o vazamento do `X=4` agora vaza um nível a mais |

### Em aberto

- **A Q5 — o que cada Trilha entrega, entrada por entrada.** 80 entradas, e agora existe contra o que medi-las. A ordem de ataque do §4 do rascunho não mudou: Evocador, Vanguarda, Guia, Bastião, Emanador.
- **O validador de Trilhas**, que só nasce com a peça. A especificação está no §5 do rascunho e ela tem de ser implementada como está, não reinventada.
- **A palavra "cena" não tem definição**, e ela agora carrega mais peso.
- A discrepância de arredondamento da segunda tabela da peça 6 §3, herdada da v0.60 e não tocada pelo mesmo motivo.
- As de sempre: as vagas de Desliga, a Cicatriz, Energia Reversa, o clash, o nome do sistema.

---

## [0.60] — 2026-08-14

**A coluna Rotina tinha duas versões no repositório, e a errada era a que quase tudo lia.** Achado abrindo o chat de Trilhas, indo ler o dono do número contra o qual a peça inteira ia ser precificada. A peça 6 §3 publicava `81` no nível 18 e `126` no nível 30 — **e nenhum dos dois é a coluna `Rotina` do manual.** Continuam **dezesseis peças e dezesseis validadores**; o que entrou foi uma checagem nova dentro do `conferir-manual.py`, que é o dono dessa fronteira.

### Achado — os dois números existem no manual, na tabela certa e na coluna errada

*É o que fez o defeito sobreviver.* Uma varredura que pergunte *"esse número está no manual?"* aprova os dois:

| nível | Classe | a coluna `Rotina` diz | a peça 6 dizia | de onde o número saiu |
|---|---|---|---|---|
| 2 | 1 | 13 | 13 | — |
| 10 | 3 | 45 | 45 | — |
| **18** | 5 | **76** | **81** | `Feitiço num alvo` da **Classe 6** |
| **30** | 7 | **108** | **126** | `Somando alvos` e `Liberação` da **Classe 7** |

**E o `ESTADO-ATUAL` já dizia quem manda:** *"Rotina — dano por rodada por Classe — **dono: o manual** — ela é a **régua**, não uma medida"*. O `conferir-manual.py` confere essa coluna contra o `.docx` desde a v0.26 **e passava verde**, porque ele nunca abriu a peça 6.

> **Isto desfaz metade da v0.58, e o registro fica porque o erro é instrutivo.** Aquela versão achou três tabelas usando `77` no nível 18 e as corrigiu para `81`, escrevendo que *"o 77 é a interpolação linear entre os 45 do nível 10 e os 126 do nível 30 — conta certa para traçar uma reta, conta errada para uma tabela que já tem dono"*. **O raciocínio estava certo e a tabela consultada era a errada.** O valor certo é `76`, e a interpolação que ela derrubou estava **mais perto** do que a correção que entrou no lugar. *Ir ao dono não basta: é preciso conferir que a coluna lida é a coluna que o dono nomeou.*

### Achado — o conserto fortalece uma decisão que tinha sido tomada com o número fraco

A peça 6 §3.1 rejeita **somar** o golpe (três ações) em favor de **trocar** o Classe 0 (duas ações), e o argumento é que somar vira a terceira ação por rodada. **A tabela que sustentava isso mostrava `+1%` no nível 30** — o número mais fraco possível para aquele argumento, e quem lesse rápido concluiria que somar é inofensivo em campanha alta.

| nível | somar, como estava | somar, com a Rotina certa |
|---|---|---|
| 18 | +11% | **+18%** |
| 30 | **+1%** | **+18%** |

**Somar não afrouxa no topo: ele fica em +18% do nível 18 ao 30.** A decisão estava certa e a conta que a segurava estava lendo a coluna errada.

### Alterado — o que o conserto moveu, documento por documento

| onde | o que mudou |
|---|---|
| **peça 5 §2** | a arma contra a Rotina: `~99`→`76` e `126`→`108`, e a lacuna vira `7,2×` e `9,4×`. A frase *"entre 7% e 65%"* vira **11% e 65%** |
| **peça 6 §3** | as duas tabelas, e o `+9%` do nível 18 vira `+16%` |
| **peça 6 §3.1** | somar/trocar recalculados, com a nota de que a mudança é a favor da decisão |
| **peça 6 §4** | a invocação: `~99`→`76` e `126`→`108`. **Dobrar e quadruplicar não se movem** — o argumento é estrutural, e a horda do nível 30 vai de `504` para `432` |
| **peça 15 §3.3 e §3.6** | o alvo *meia Rotina* no 18 e no 30, e a linha do Evocador que aguenta `2,0` rodadas em vez de `1,7` |
| **peça 16 §2 e §2.1** | dobrar uma arma de duas mãos vale **`1,5%`** da Rotina no nível 30, e o buraco que a ferramenta teria de fechar é **95** e não 113 |
| **`ESTADO-ATUAL`, pendência nº 6** | *"no nível 30, 21% e 16% abaixo"* vira **8% e 2%** |
| **`RASCUNHO-trilhas.md` §2.2** | a dívida da Trilha no nível 30: `6,5` a `9,7` |

### Decidido — a fórmula de vida da invocação NÃO muda, e o motivo é a forma do alvo

O alvo *"meia Rotina"* no nível 30 caiu de `63,0` para `54,0`, e a v0.57 tinha resolvido a fórmula em dois pontos ancorados, um deles ali. Refeita a conta, o por-nível sai **`1,70`** em vez de `2,02` — **e `1,7` não é número de mesa.** Mantendo o `2`, a invocação do nível 30 fica `+15%` acima do alvo.

**Isso parece deriva e não é.** A Rotina é **escada por Classe**, não reta, e uma reta ajustada a uma escada passa por baixo no pé de cada degrau e por cima no topo:

| degrau da Rotina | largura | no pé | no topo |
|---|---|---|---|
| nv5–8 | 4 | −23% | **+16%** |
| nv9–12 | 4 | −11% | **+16%** |
| nv17–20 | 4 | −5% | +11% |
| **nv26–30** | **5** | **+0%** | **+15%** |

**O `+15%` do nível 30 é o topo do degrau mais largo da tabela, e ele é menor que o `+16%` que a peça já aceitava calada no nível 8 e no 12.** O ajuste sempre foi contra uma escada; o que estava errado era o último degrau dela.

### Adicionado — a checagem 4d do `conferir-manual.py`

**Ela existe por um vão que a 4c não cobria:** a 4c confere a coluna `Rotina` do `.docx` contra um dicionário escrito dentro do validador, e **sai verde com a peça 6 publicando qualquer coisa**, porque nunca abre a peça 6.

> **A 4d varre tabela por tabela da peça 6 — só as que declaram `Rotina` no cabeçalho — e bate cada linha contra a coluna do manual, pela faixa de nível lida da própria tabela do `.docx`.** Nenhuma faixa escrita no código: se o manual reagrupar as Classes, ela acompanha. E quando falha, ela **diz de que coluna o número veio**, que é a informação que faltou por catorze versões.

**Arnês, na cópia isolada, com a base conferida verde antes e o `diff` provando cada `sed`:**

| perturbação | acendeu? |
|---|---|
| nv30 `108` → `126` | **sim**, nomeando `Téc. Máxima` da Classe 6 e `Somando alvos` e `Liberação` da Classe 7 |
| nv18 `76` → `81` | **sim**, nomeando `Feitiço num alvo` da Classe 6 |
| **contra-teste:** nv30 `108` → `76` — coluna certa, **linha** errada | **sim** — sem isto a checagem só provaria *"existe no manual"* |
| **contra-teste 2:** mexer na coluna do conjurador e não na Rotina | **não acendeu**, como tem de ser |

*O terceiro é o que dá valor aos dois primeiros.* Uma checagem que aprovasse `76` no nível 30 estaria conferindo presença de número, não correção de leitura — que é exatamente o erro que ela existe para pegar.

### Decidido — Trilhas: a Q2, o calendário e o fim da palavra `subtrilha`

*Decisões do Mizuki, todas com a conta na mesa.* **A tabela de progressão do rascunho tinha omitido a escada de Classe**, e isso movia a resposta: os feitiços conhecidos cobrem todo nível par, mas **cinco dos ímpares entregam uma Classe nova de feitiço** — 5, 9, 13, 17 e 21. São **nove** níveis que não entregam nada, e não catorze: `3 · 7 · 11 · 15 · 19 · 23 · 25 · 27 · 29`.

**E aí a recomendação de `2, 10, 18, 26` cai por terra pelo próprio argumento dela.** Aqueles são os quatro níveis mais cheios do sistema — o nv26 entrega **quatro coisas ao mesmo tempo** (Classe 7, maestria, dois feitiços e marco), o 10 e o 18 entregam três.

> **O calendário fechado: Trilha em `2 · 11 · 19 · 27`, Caminho em `7 · 15 · 23 · 29`.**
> **80 entradas** — 4 × 15 de Trilha e 4 × 5 de Caminho — e **405 montagens legais**.

**Os dois degraus não são conceito novo: a peça 6 §3.1 já os tinha**, em *"Bastião e Vanguarda ganham ataque extra no nível 6, **pelo Caminho**; Arremate e Coro ganham **pela Trilha**"*. Alternar os dois foi o que resolveu um empate que 6 entregas de Trilha não resolviam — com seis, ou o maior vão da Trilha é **8** ou a pior seca é **37 missões**, nunca os dois bons. O misto entrega vão **5** e seca **24**, com **dez entradas a menos** e uma matriz **nove vezes menor**.

*A seca foi medida em **missão** e não em nível, pela curva da peça 12, porque é a unidade que o jogador sente: hoje o vão `nv26 → nv30` são **37 missões** sem nada que se escolha.*

> **`subtrilha` morre como palavra, e a mecânica da Q4 fica inteira.** A árvore `Caminho → Trilha → subtrilha` fazia parecer três andares quando são **dois com um empréstimo**: no nível 2 você pega a entrega da **sua** Trilha, e no 11, 19 e 27 pega a de **qualquer** Trilha do seu Caminho. *Decisão do Mizuki, e o motivo foi ele mesmo se perder na leitura da árvore — o que é o teste que importa.*

### Registrado — o levantamento externo sobre vão entre entregas

*O problema tem nome no hobby: **dead level**.* O D&D 3.5 não o resolveu no livro — a WotC publicou **dois artigos de errata em 2007**, *"3.5 Class Dead Levels"*, só para preencher os níveis vazios de Archivist, Beguiler, Duskblade, Hexblade, Knight, Samurai e Swashbuckler. O **Pathfinder 2e** o resolve por princípio declarado — *"every level should have something, no level should ever be a dead level"* —, e o **4e** pagou o preço oposto: ficha de nove páginas e ferramenta online obrigatória.

**O que decide o nosso caso é o 5e:** a edição de 2014 tinha vãos de **8** entre feitos de subclasse — Paladino `3·7·15·20`, Feiticeiro `1·6·14·18`, Bardo `3·6·14` —, e a de **2024 tirou todos**, padronizando em `3, 6, 10, 14`, com o capstone do Paladino descendo do nível 20 para o 14. **O vão de 8 que o calendário de seis produzia aqui é exatamente o que aquela revisão saiu para matar.**

### Em aberto

- **Trilhas: a Q3 — a régua, e ela vem antes do catálogo.** A conta já fechou duas coisas dela: a régua da **peça 13 não serve** (o `Desliga` é território de Origem, e o `Ajusta` tem um morador legal só — trocar o fixo do acerto por atributo —, o que deixa 6 de 7 no `Destranca`), e **a entrega não precisa crescer**: seis das sete linhas do permitido da peça 5 §4 são fração do que você já faz e não derivam; só o **treino** tem valor absoluto, deriva `8,3×`, e por isso só cabe no nível 2.
- **A tabela de progressão consolidada**, que esta versão montou para responder à Q2 e que continua na lista das três coisas que não existem.
- **Uma discrepância de arredondamento não tocada:** a segunda tabela da peça 6 §3 imprime `+135%` e `+32%` em linhas cujo Rotina não mudou, e a conta dá `+131%` e `+33%`. Não mexi porque não sei se o `30` e o `60` da coluna do meio são exatos ou arredondados — **e chutar qual dos dois lados está errado é como o `81` entrou.**
- As de sempre: as vagas de Desliga, a Cicatriz, Energia Reversa, o clash, o nome do sistema.

---

## [0.59] — 2026-08-14

**Ferramenta amaldiçoada fechou. São dezesseis peças e dezesseis validadores.** O `RASCUNHO-ferramenta-amaldicoada.md` virou `16-ferramenta-amaldicoada.md` e ganhou o `conferir-ferramenta.py`, com as **dezesseis checagens** que o §7 daquele rascunho vinha listando desde a v0.54. **O arnês acendeu cinco perturbações, cada uma numa checagem só.** E a peça só coube numa versão porque uma pergunta que parecia fechada não estava — a escada de grau tinha **duas** respostas no repositório, e as duas estavam escritas.

### Decidido — a escada de grau do §6 é ritmo de entrega, e não gate

*A máquina da v0.55 decidiu o gate no §5.1: grau 2 no **nível 7**, grau 1 e especial no **nível 13**, herdados da peça 11 §6 sem a metade de refino.* Só que o §6 do mesmo rascunho carregava uma segunda escada — `4→2 · 3→10 · 2→18 · 1→26 · especial→30` —, sob o título *"os números que a peça vai precisar, já rodados"*, com **duas formas** e uma inclinação, nunca uma decisão. Ela nunca foi adotada, e nunca foi marcada como aberta.

**Ligar a segunda como gate duro matava duas coisas, e a conta é curta.** Ela é mais alta que o gate herdado em **toda linha**:

| grau | gate herdado (peça 11) | escada do §6 | quem mandaria |
|---|---|---|---|
| 3 | nenhum | 10 | §6 |
| 2 | **7** | 18 | §6 |
| 1 | **13** | 26 | §6 |
| especial | **13** | 30 | §6 |

- **A checagem 3 ficaria trivialmente verdadeira.** O contra-teste que o §7 manda rodar é perturbar a Extensão de Domínio na peça 11 e ver o gate do grau 1 andar junto. Perturbado para `1`, `8` e `18`, o gate do grau 1 fica em **26 nos três casos** — a checagem não consegue mover o número que ela existe para medir. **É a lição nº 8 entrando pela porta dos fundos:** não uma constante escrita no validador, mas um segundo dono no documento que anula o primeiro.
- **O `Desgaste` viraria no-op.** Ele apaga *"o gate de nível do `Estigma`"* — o 7 e o 13. O 18 e o 26 são da ferramenta e continuariam de pé. A Corda Negra deixaria de existir.

**E o §5.3 já tinha respondido sem ninguém ler assim:** *"o que separa grau 1 de especial é **escassez, e não mecânica** (…) isso é **zero número novo**, e o que ele governa é a **mão do mestre**."* Se especial é escassez, o `30` nunca foi gate. **A escada virou o §7 da peça, declarada como ritmo, com a frase *"esta seção não cria requisito"* no topo** — e a checagem 9 falha se ela parar de se declarar.

### Adicionado — o `conferir-ferramenta.py`, com o par 3/9 declarado

**Dezesseis checagens.** O fundo `3/5` sai da **peça 14 §5**; o gate e as Classes da **peça 11 §4 e §6**; os sete marcos da **peça 2 §3**; a Rotina da **peça 6 §3**; a rota sem energia da **peça 9 §5**; as duas vagas de Desliga da **peça 13 §8**; a frase *"Grau é reconhecimento; nível é poder"* da **peça 12 §2**; e o bolso do `conferir-orcamento.py`. A escada, o teto e o catálogo saem da própria peça 16.

**O único bloco com valor na mão é o `LIMITES DE DESIGN`**, declarado à parte da regra aplicada — e é ele que a perturbação 2 do arnês testa: subir o teto de apoio de 2 para 5 acende a checagem 6, e só ela.

> **A checagem 3 e a 9 leem a mesma amarra por dois lados, e o par está escrito no cabeçalho do validador em vez de subentendido.** A 3 confere que o gate vem da peça 11; a 9 confere que a escada de grau vem daqui e **que o §7 continua se declarando ritmo**. Elas não são independentes: se o §7 virasse gate, a 3 morreria calada e a 9 continuaria verde sozinha. *Foi exatamente o cenário que esta versão desarmou, e a checagem existe para ele não voltar.*

**E o catálogo se conta, nunca se guarda.** O validador não sabe que são onze — ele conta as linhas das três tabelas do §6 e compara com o numeral escrito no título da seção.

### Achado — o validador leu a própria especificação como se fosse a regra

*Achado na primeira rodada limpa, e vale registrar porque o erro é de um tipo novo aqui.* Das quatro checagens que falharam de saída, **três eram o validador sendo ingênuo, não a peça estando errada**:

| checagem | o que ela acusou | o que era de verdade |
|---|---|---|
| 4 · SEM-REFINO | *"gate de refino aparece na peça"* | o **§8**, que **descreve as dezesseis checagens**, cita `gate de refino` justamente para dizer que ele não pode existir |
| 10 · PATENTE | *"o texto liga patente a grau: `Grau 2 porta`"* | o **§2.2**, que **cita a ideia refutada** — *"feiticeiro de Grau 2 porta ferramenta de grau 2"* — para derrubá-la com a peça 12 |
| 3 · GATE | *"não achei a tabela de gates na peça 11 §6"* | a peça 11 tem `## 6.` **e** `## 6.5.`, e o recorte ingênuo parava na subseção — perdendo a tabela, que vem **29 linhas depois** dela |

**As duas primeiras são o mesmo erro: confundir o alvo com o tiro.** Uma peça que documenta o próprio validador contém, por construção, o texto que o validador procura para reprovar. *A varredura da checagem 4 hoje lê só as seções de regra — §1 a §7 —, e a 10 exige que a menção venha sem refutação por perto.*

> **A terceira é a lição nº 9 numa camada que ninguém tinha pisado:** `## 6.5.` casa com `^## \d+\.`, então "próxima seção" e "próximo número de seção" não são a mesma coisa. **O recorte agora agrupa por número de seção**, e não pela próxima linha `##`. *Nenhum outro validador do repositório recorta seção assim — os que precisam disso leem tabela por regex direto.*

### Alterado — as contagens, e um rascunho a menos

**Dezesseis peças e dezesseis validadores** no `README`, no `ESTADO-ATUAL` e no `LEIA-ME`. O `conferir-ferramenta.py` entrou nas duas listas de rodar à mão.

**E os rascunhos caíram de quatro para três.** `RASCUNHO-bloqueio.md`, `RASCUNHO-clash-de-expansoes.md` e `RASCUNHO-trilhas.md` — o de ferramenta foi apagado ao virar peça, do mesmo jeito que o de Invocações na v0.58. *Duas versões seguidas fazendo o caminho que um rascunho existe para fazer.*

### O arnês, e os cinco vermelhos que ele produziu

Cópia isolada, base conferida **verde antes** de cada perturbação, `diff` provando que o `sed` bateu, e uma checagem acesa por perturbação:

| perturbação | onde | acendeu |
|---|---|---|
| Extensão de Domínio: nível 13 → 18 | **peça 11** | **checagem 3**, nos *dois* graus de Classe 3 ao mesmo tempo |
| teto de apoio: 2 → 5 | `LIMITES DE DESIGN` | checagem 6 |
| fundo: `3` → `4` | **peça 14** | checagem 1 |
| um `1d6` numa entrada do catálogo | peça 16 §6 | checagem 8 |
| o §7 para de se declarar ritmo | peça 16 §7 | **checagem 9** |

> **A primeira acender nos dois graus ao mesmo tempo é a prova de que o gate é derivado e não copiado** — grau 1 e especial leem a mesma Classe 3, e os dois andaram juntos. Um gate escrito na mão teria movido zero.

### Decidido — os três degraus de escudo ganharam nome

*Pendência aberta desde a v0.42, e o último item de forma que Equipamento devia.* **`Broquel` · `Médio` · `Torre`.**

| degrau | nome | proteção | teto de Destreza | requisito de Força | o que ele é |
|---|---|---|---|---|---|
| 1 | **`Broquel`** | 1 | 5 | — | escudo de punho, **15 a 45 cm**, leve e manobrável |
| 2 | **`Médio`** | 2 | 3 | 3 | o degrau do meio, e o nome diz isso |
| 3 | **`Torre`** | 3 | 1 | **5** | cobre o corpo quase inteiro e **se planta no chão** |

**As duas pontas são objeto e o meio é tamanho, e isso é decisão e não descuido.** *A `Rodela` chegou a ser escrita e caiu por leitura de mesa:* ela é historicamente exata — redonda, de metal, presa ao braço, 50 a 60 cm — e **não diz nada para quem nunca ouviu a palavra.** `Médio` diz. **O critério da peça 14 é que o nome carregue a identidade sem nota de rodapé**, e num degrau que existe para ser o meio, "meio" é a identidade.

> **E ele entra com duas colisões declaradas em vez de escondidas.**
>
> **A que a triagem pega:** `Médio` sai **fraco**, a uma letra de `Medo`, que é **Tema** no manual. Aceita — Tema de feitiço e degrau de escudo não dividem linha de regra.
>
> **A que a triagem NÃO pega, e o §5.4.1 da peça 14 já tinha registrado o ponto cego:** `Leve`, `Média` e `Pesada` são os **tiers de Restrição** da peça 3, e saem `LIVRE` porque **tier de magnitude não está em lista nenhuma do manual**. `Médio` (escudo) e `Média` (Restrição) são a mesma palavra em gêneros diferentes — exatamente como a classe de arma `Pesada` colide com o tier `Pesada` desde que as duas existem. **É a segunda colisão aceita nesta peça, no mesmo eixo**, e por isso ficou escrita na peça: *escudo `Médio` é objeto, Restrição `Média` é preço. Uma se empunha, a outra se paga.*

*Triagem rodada em nove candidatos antes de escrever: `Broquel`, `Torre`, `Rodela`, `Adarga`, `Targa`, `Pavês` e `Escútulo` saíram **LIVRE**; `Médio` e `Medio` saíram **fraco**. E o `conferir-nomes.py` foi rodado com os três já escritos, para o caso de algum virar substring de nome batizado — `Torre` está dentro de `Torrente`, que é Trilha do Emanador: **passa**.* **Mortos na triagem anterior:** `Anteparo` é **Melhoria** e `Bloqueio` é **Tema**.

### Achado — a auditoria antes de Trilhas, e três listas vencidas

*Rodada a pedido do Mizuki, antes de abrir o chat de Trilhas.* **Trilhas não está travada por nada** — a Q1 e a Q4 fecharam na v0.55, as três Trilhas de invocação têm a máquina pronta desde a v0.58, e o `conferir-invocacoes.py` já carrega a guarda que manda tirar a declaração de dominância quando a Q6 der número ao *"corpo forte"* do `Servo`. **O que a auditoria achou não trava; envelhece.**

**A lista *"o que falta"* de Equipamento estava em dois documentos, e dois dos quatro itens já estavam feitos:**

| item | estado real |
|---|---|
| *"o validador da peça"* | **feito na v0.48** — é o `conferir-equipamento.py`, 20 KB |
| *"os dois dados do `Yumi`"* | **corrigido na v0.47**, e o desmentido está **573 linhas abaixo da própria linha**: `Daikyū` para `1d10`, `Hankyū` para `1d8`, os dois fechando exatos em `4 de 4` |
| os nomes dos degraus de escudo | **continua aberto** — hoje são `1`, `2` e `3` |
| a penalidade sem treino ou requisito | **continua aberto**, e é da peça de dano e condições |

> **O §8 item 9 da peça 14 nomeou esse defeito com todas as letras** — *"não uma cópia que diverge, mas uma **conclusão que sobrevive à premissa**"* — e o cabeçalho da mesma peça estava fazendo exatamente isso, com o próprio corpo dela como desmentido. *Foi copiada em vez de apontada, e por isso venceu nos dois lugares ao mesmo tempo.*

### Adicionado — a checagem 6 do `conferir-repositorio.py`: o mapa contra a pasta

**A tabela *"Onde cada coisa está"* do `ESTADO-ATUAL` tinha divergido, e nada acusava.** Faltavam **as peças 13 e 14** — as duas maiores do projeto, 102 KB e 136 KB — e **seis validadores**: `conferir-atributos`, `conferir-acao`, `conferir-pericias`, `conferir-descanso`, `conferir-legados` e `conferir-equipamento`.

**A checagem 1 conta quantas peças existem; ela sai verde com o mapa furado, porque contar e listar são perguntas diferentes.** O mapa é uma **cópia** da listagem da pasta, e a lição nº 9 admite duas saídas para uma cópia — um dono declarado ou um validador que compare as duas. **Ele não tinha nenhuma das duas.**

*E o preço é específico:* quem retoma em conversa nova lê o mapa, não a pasta — que é exatamente o que o chat de Trilhas ia fazer, e as duas peças que faltavam são justo o precedente que aquela peça precisa (**a régua antes do catálogo** é a comparação entre a peça 13, fechada em uma versão, e a peça 14, que gastou seis).

*Contra-teste rodado:* tirar a peça 14 do mapa acende **um problema, o certo**; tirar o `conferir-legados.py` acende **um problema, o certo**. E a base foi conferida verde na cópia antes — na primeira tentativa ela saiu **vermelha**, porque a cópia não levou o `.gitignore` que o README promete, e o arnês recusou o resultado em vez de deixar ler um vermelho que não era prova.

### Alterado — as duas listas vencidas, e o mapa preenchido

As listas de Equipamento no `14-equipamento.md` e no `ESTADO-ATUAL` perderam os dois itens já prontos e ganharam, no lugar, o registro de **quando** cada um foi feito. O mapa recebeu as duas peças e os seis validadores que faltavam: **16 de 16 e 16 de 16**.

### Em aberto

- **Trilhas** é a posição 1 da fila, e o `RASCUNHO-trilhas.md` existe para aquele chat não começar do zero: **30 a 120 entradas**, contra as 81 da peça 13 numa versão e as 52 armas que custaram seis à peça 14. *A recomendação de método daquele documento é uma só: a régua antes do catálogo.*
- **Objeto amaldiçoado** continua por último. Ele fecha **1 vaga de Desliga e mais nada**.
- **Os nomes próprios das ferramentas do material** — a Nuvem Divertida e a Lança Invertida aparecem na peça 16 como exemplar, não como ficha.
- **A penalidade por empunhar sem treino ou sem requisito** continua na peça de dano e condições, que não está na fila. É a mesma pendência que a peça 14 §8 já carrega.

---

## [0.58] — 2026-08-14

**Invocações fechou. São quinze peças e quinze validadores.** O `RASCUNHO-invocacoes.md` virou `15-invocacoes.md` e ganhou o `conferir-invocacoes.py`, com as **trinta checagens** que o §5 daquele documento vinha listando desde a v0.51. **O arnês acendeu as trinta**, e dois contra-testes não acenderam nada. E aconteceu o que a peça 14 já tinha mostrado: **o validador achou três coisas na primeira rodada limpa — e duas eram minhas.**

### Achado — a Rotina do nível 18 tem dois valores no repositório, e o dono é a peça 6

*Achado indo ler o dono antes de conferir a linha do alvo da tabela de vida.* A **peça 6 §3** publica **81** em três tabelas. **Três tabelas de dois rascunhos usavam 77.**

| onde | dizia | é |
|---|---|---|
| peça 15 §3.6, a linha *"alvo — meia Rotina"* | 38,5 | **40,5** |
| `RASCUNHO-ferramenta-amaldicoada.md` §2.1 | 77 · 2,1% | **81 · 2,0%** |
| `RASCUNHO-ferramenta-amaldicoada.md` §2.2 | 77 · 16% · 64,9 | **81 · 15% · 68,5** |

**O 77 é a interpolação linear entre os 45 do nível 10 e os 126 do nível 30** — conta certa para traçar uma reta, conta errada para uma tabela que já tem dono. *E ela passa despercebida justamente porque o nível 18 é o único ponto da curva que ninguém ancorou:* nos níveis 2, 10 e 30 a reta e a tabela dão o mesmo número, então três das quatro células batiam.

**A fórmula de vida não se move.** Ela foi ajustada nos dois pontos ancorados — `h(2) = 6,5` e `h(30) = 63` —, e os dois continuam batendo. O que muda é o alvo contra o qual o tipo do meio é lido no 18, e a diferença é `38` contra `40,5` em vez de `38` contra `38,5`. **Nenhuma decisão vira.**

> *De quebra, o `64,9` da segunda tabela da ferramenta não reproduzia nem com o 77 — com 77 dá `64,5`.* **Número derivado de número emprestado erra duas vezes**, e a segunda ninguém procura.

**A checagem 19 lê a Rotina da peça 6 §3 e nunca de constante.** *Contra-teste rodado:* perturbar o `126` da peça 6 faz a linha do alvo acender inteira — que é a prova de que ela não se mede contra si mesma.

### Adicionado — o `conferir-invocacoes.py`, e ele não guarda um número sequer

**Trinta checagens.** O teto somado e a cota por corpo saem da **peça 6 §4**; a Rotina por nível da **peça 6 §3**; os marcos e os tetos da **peça 2**; a fórmula de vida, o PE por nível e a maestria da **peça 1**; a amarra da **peça 3 §3**, que é o alcance base de Projétil; o ritmo do refino da **peça 11 §2**; o ponto de arma da **peça 14 §5**; e o **PISO do bolso** do `conferir-orcamento.py`, que é quem já sabia medir isso. O catálogo, a régua e o orçamento saem da própria peça 15.

**O único bloco com valor na mão é o `LIMITES DE DESIGN`**, declarado à parte da regra aplicada — que é a lição nº 8, e é ela que a perturbação 2 do arnês testa: tirar um par da declaração acende a matriz, e só ela.

**Ele é o maior dos quinze porque a peça 15 é máquina de construção e não lista**, e por isso faz as quatro naturezas de uma vez: regra, catálogo, instância e busca exaustiva. A busca enumera **21.502 montagens** que gastam o orçamento cheio no nível 30, com a maior usando **9 das 19 entradas — 47%**, e o número estava escrito na peça **antes** de o validador existir.

> **Zero montagens dominadas, e isso não vem de busca: vem de prova.** Toda entrada comprável custa pelo menos 1 e toda montagem gasta o orçamento **exato**, então nenhuma pode ser superconjunto estrito de outra. *A checagem afirma as duas premissas e conclui — comparar 21.502 montagens duas a duas seriam 462 milhões de pares para provar o que a aritmética já garante.*

### Corrigido — dois furos meus, achados pelo arnês e não pela leitura

**Os dois só apareceram porque a perturbação não acendeu o que devia**, e é para isso que ele existe.

| | o que acontecia |
|---|---|
| a régua comia o último nome de cada degrau | a função que limpa a célula tirava a crase das **pontas da célula inteira**, e a última entrada de cada lista ficava sem o par de crases que o `findall` procura. **`Fala`, `Remoto`, `Cavar` e `Chamariz` sumiam da régua** e a checagem 6 saía verde sem conferir os quatro |
| o leitor da cota estourava em vez de acusar | ele só entendia *"um"* e *"cinco"* corpos. Perturbar a peça 6 para *"quatro"* fazia o validador **quebrar com traceback**, e um validador que quebra não é um validador que acusa |

**E duas checagens estavam varrendo a mesma coisa.** A do ritmo também procurava entrada que encostasse em Defesa, que é da checagem 27 — então **uma perturbação acendia duas**, e o arnês deixava de provar que elas eram independentes. A varredura saiu da 18.

> **Três checagens acendem em par ou em trio, e isso ficou declarado em vez de escondido.** Mexer no teto da peça 6 derruba a checagem 1 **e** a 14, porque a tabela de economia de ação fecha a soma no teto. Mexer no alcance de Projétil derruba a 24 **e** a 25, porque a faixa *"no combate"* **é** a amarra. E mexer na quantidade de corpos derruba a 21, a 11 e a 22 — a cota, o pool em que a área entra, e os d20 do crítico. *Quando duas checagens leem o mesmo dono, declarar o par é mais honesto que fingir isolamento.*

### Decidido — a peça se chama Invocações, e isso é decisão escrita

*Decisão do Mizuki.* O §4 tinha deixado o nome em aberto desde a v0.50, com `Invocação` saindo **OCUPADO** na triagem — é **Tema** do manual, no grupo *Criação*.

**O que pesou foi custo de troca contra tamanho da colisão.** Tema não carrega mecânica, então o choque é de vocabulário e não de regra; e o nome já está em **17 citações** no `ESTADO-ATUAL`, **61** no `CHANGELOG` e **13** na peça 6. A v0.50 decidiu por escrito que histórico de CHANGELOG não se reescreve — **trocar deixaria noventa e tantas linhas falando de uma peça com outro nome, para consertar um rótulo que não tem mecânica.** `Coleira` e `Convocação` ficam anotadas no §4, livres.

### Decidido — o quarto formato de gate, e ele foi escrever na peça 11

*Decisão do Mizuki, e ela fecha a última pendência que a v0.57 deixou aberta.* O gate de Origem do `Remoto` — alcance de país exige **Restrição Celestial pelo ramo do corpo limitado** e uma técnica voltada a isso — era o único gate do catálogo inteiro, e a **peça 11 §5** só conhecia três formatos: nenhum, só nível, só refino, ou os dois.

> **Ele foi escrito na peça 11 §5**, que é a dona dos formatos de gate, e a peça 15 aponta para lá em vez de repetir a definição.

**A regra que ele traz é estreita de propósito:** um gate de Origem só é legal quando o efeito **não faz sentido nenhum fora daquela Origem**. Nível e refino se compram, e dois mestres leem os dois igual; **Origem é rótulo**, e se ela virar moeda de preço a criação passa a ser escolhida por quais gates ela destrava. *Aí a Origem deixa de ser ficção e vira árvore de talento.*

**E ele nasceu com trava.** A checagem 26 confere que **nenhuma outra entrada do catálogo tem requisito** — se uma segunda aparecer, quer dizer que a régua de degrau do §3.7 parou de precificar sozinha, e isso tem de ser decisão e não descuido. *Escrever o formato sem o validador ao lado seria criar a quarta porta e não trancar nenhuma.*

### Alterado — o §5 deixou de ser lista de desejo

Ele se chamava *"O que o validador vai precisar ter"* e passou a ser *"O que o validador confere"*. **A lista não mudou de conteúdo: mudou de tempo verbal**, e ganhou, item a item, de qual documento o número é lido e qual perturbação tem de acender aquela checagem.

> *E vale registrar o que essa lista comprou.* Ela foi escrita **antes** do validador, ao longo de sete versões, e o validador coube em **uma**. A peça 14 gastou **seis**, e a diferença que ela mesma registrou é a régua vir antes do catálogo. **Aqui a especificação veio antes do código, e é a mesma economia por outra porta.**

### Corrigido — as duas listas de "rodar os validadores" estavam uma curta desde a v0.48

*Achado na revisão cética, contando as linhas em vez de lendo a frase.* O `README` e o `ESTADO-ATUAL` mandam rodar os validadores um a um, e **o `conferir-equipamento.py` nunca entrou nas duas listas** — ele entrou na pasta na v0.48 e na prosa das duas versões seguintes, mas não no bloco de comandos.

**Ninguém deixou de rodá-lo:** o `subir.sh` varre a pasta por glob. **Quem rodava à mão pelo documento é que rodava um a menos**, e o documento dizia *"os dez primeiros conferem regra"* quando eram onze. *Um comando que falta numa lista não falha nada — ele só ensina errado, e o erro só aparece quando alguém confia na lista em vez do script.*

### Em aberto

- **O validador da ferramenta amaldiçoada** (16 checagens no §7 do rascunho dela). *Ela é a posição 1 da fila agora, e sem ele o catálogo de `Estigma` não vira peça.*
- **Quando a vida cheia da invocação reinvocada volta.** O candidato natural é o descanso longo; é sabor, e não está decidido.
- **As duas dominâncias declaradas da peça 15** — `Matilha > Servo` e `Coro > Servo`, as duas apontando para o Servo, que é a única das três Trilhas cuja concessão não tem número. **Elas caem com a Q6**, na peça de Trilhas, e a checagem 2 acusa se a declaração ficar mentindo depois disso.
- **O tempo de mesa da Matilha** — `2,5×` um personagem de nível 6, escrito antes da sessão. É pergunta de playtest, e `04-playtest/` continua vazia.
- **Trilhas:** a Q3 — a régua antes do catálogo.
- As de sempre: as vagas de Desliga, a Cicatriz, Energia Reversa, o clash, o nome do sistema.

---

## [0.57] — 2026-08-13

**A fórmula de vida da invocação ganhou número, reconseguir fechou, e uma entrada do catálogo de `Estigma` foi arrancada depois de escrita.** Continuam **catorze peças e catorze validadores**.

### Removido — a `Vazadura`, e o motivo é que passar na conta não basta

*Decisão do Mizuki: **ignorar Redução de Dano não entra neste sistema.*** Ela ignorava a RD do alvo, **e tinha passado na conta** — a fração que ela anula anda só `3,3` pontos percentuais em vinte e oito níveis, então ela não derivava.

> **A conta diz o que é legal. Ela não diz o que deve existir.** A RD é o produto que a peça 11 §6 vende por 2 PE, e um item que a apaga é um item que responde a uma escolha de outro jogador com um *"não"*.

**No lugar entrou o `Bojo`** — *uma vez por descanso curto, a ferramenta guarda um feitiço que você lançou e o devolve sem custo de PE*. Sai do **Osso de Dragão** (*"acumula e ejeta energia"*) e cobra em **custo**, que é um dos quatro eixos que a peça 11 §2 autoriza por escrito. *É o único dos onze que só serve a feiticeiro, e isso é aceito: grau 4 é a entrada de quem não tem energia, e o resto da escada não precisa ser neutro.*

### Alterado — o `Cisão` subiu para Classe 3, e a obra é quem manda

*Decisão do Mizuki.* A Katana de Alma Partida não corta a alma uma vez por cena — **ela corta a alma, e é isso que ela é.** Permanente é o formato certo.

**E permanente aqui não é upgrade, o que é o que faz ele caber.** A Integridade é `20 + 8 × (nível − 1)`, sem Caminho e sem Constituição dentro, e a lista de playtest do `ESTADO-ATUAL` já registra que *"a alma é maior que o corpo em quatro dos cinco Caminhos"*. **Trocar dano de vida por dano de alma é pior contra quatro dos cinco e melhor contra um** — é troca, não escada. *É literalmente o que "muda como você joga" quer dizer.*

**O catálogo continua com onze:** 4 de Classe 1, **3** de Classe 2 e **4** de Classe 3.

### Decidido — a fórmula de vida da invocação, com o termo de tipo preenchido

*Ele estava vazio desde que a Q3 fechou, e era o buraco que mais mordia para alguém jogar um Evocador.* **O alvo não era livre:** a Q2 fixou um corpo em **meia Rotina** e a Q5 fixou o pool em `5h`. Resolvendo os dois pontos ancorados — `h(2) = 6,5` e `h(30) = 63` — sai `por nível = 2,02` e `base = 2,46`.

> **`vida = base do tipo + (2 + a Constituição dela) × nível do dono`**

*Ordem decidida pelo Mizuki: talismã e corpo amaldiçoado empatam; a maldição domada tem mais, por ter sido domada; a técnica fica no meio — ela não precisa ser domada, mas quem a perde perde da própria técnica, e não tem substituição.*

| tipo | base | nv2 | nv30 |
|---|---|---|---|
| talismã · corpo amaldiçoado | 1 | 5 | 61 |
| **técnica** | **2** | **6** | **62** |
| maldição domada | 3 | 7 | 63 |
| *alvo — meia Rotina* | | *6,5* | *63,0* |

**Só a base varia; o por-nível é 2 nos quatro.** É a mesma decisão do §3.3 sobre o acerto: **base diferente é deslocamento fixo, e deslocamento fixo não deriva.** Por-nível diferente faria os quatro tipos derivarem um do outro na campanha.

**E o pool continua na faixa que a Q4 mediu, lido na mesma base do §3.4:** no nível 2 os três tipos dão **31% · 38% · 44%** da vida da mesa contra os **40%** registrados lá, e no nível 10 dão **30% · 31% · 33%** contra **32%**. *O tipo do meio cai em cima da referência.*

> **O preço de não derivar é que o tipo encolhe, e o número fica escrito em vez de escondido:** do mais fraco ao mais forte são **1,40×** no nível 2 e **1,03×** no nível 30. **O tipo pesa na criação e vira sabor no fim.** *A alternativa é por-nível diferente, e ela troca "encolhe" por "deriva".*

### Decidido — reconseguir a invocação morta, e a resposta é mais dura do que o rascunho supunha

*Decisão do Mizuki.*

> **Morreu em definitivo, acabou — não se reconsegue.**
> **Chegou só a zero: volta pelo preço da Q4, com metade da vida máxima.**

**A meia vida cai numa conta que a Q5 já tinha:** o corpo vale meia Rotina, então o corpo que volta vale **um quarto**, e o pool da Matilha reinvocado vai de `2,5` para `1,25` Rotinas de presença.

**E ela é a peça que faltava no argumento da Q4.** A conta da *"primeira grátis"* mostrou que o mestre que foca a invocação cobra **420%** do preço nominal, e o conserto foi não ter isenção nenhuma. **A meia vida cobra esse mestre de novo, na direção certa** — ele derruba, o jogador reinvoca por PE e ação, e o corpo que volta cai na metade do tempo. *O preço passa a ser cobrado no recurso **e** na durabilidade.*

*Fica aberto quando a vida cheia volta. O candidato natural é o descanso longo, que é o degrau mais lento da escada da peça 10, mas é sabor e não está decidido.*

### Registrado — Rika e Mahoraga saem da fila desta peça

*Decisão do Mizuki: eles ficam sem base por enquanto, e vão para um guia de Evocador que ele quer escrever.* **Isso não deixa buraco na máquina:** os dois já estavam marcados como **regra própria e não ponto de orçamento**, e nenhuma conta desta peça os usa.

### Corrigido — o mesmo número errado da v0.53, pela terceira vez na semana

*Achado contando antes de citar, ao fechar a versão.* O `ESTADO-ATUAL` dizia **vinte e oito** checagens no §5 do rascunho de Invocações. **São trinta** — a v0.55 acrescentou duas (as faixas de alcance e o gate de Origem) e a frase não se moveu.

> **É a terceira encarnação do mesmo defeito em cinco versões:** a v0.53 achou *"as treze checagens"* quando eram vinte e três, e agora *"vinte e oito"* quando são trinta. **Contagem de uma lista que mora em OUTRO documento envelhece a cada edição daquele documento, e nenhum validador cruza os dois.**
>
> *O conserto de verdade é uma checagem, e ela entra junto com o validador da peça — que é onde essa contagem vai deixar de ser prosa.* Por enquanto o número foi corrigido e ganhou a data de quando foi contado.

### Em aberto

- **O validador de Invocações** (**30** checagens no §5) e **o da ferramenta** (**16** no §7). *Nenhuma das duas vira peça sem ele — o `conferir-repositorio.py` conta peças contra validadores.*
- **Quando a vida cheia da invocação reinvocada volta.**
- **O gate de Origem do `Remoto`** como quarto formato, ao lado dos três da peça 11 §5.
- **Trilhas:** a Q3 — a régua antes do catálogo.
- As de sempre.

---

## [0.56] — 2026-08-13

**O catálogo de `Estigma` foi escrito — onze entradas, com a triagem rodada em cada nome e o degrau derivado da régua em vez de escolhido depois.** Continuam **catorze peças e catorze validadores**; falta o validador para a ferramenta virar peça.

### Adicionado — as onze, distribuídas pelas três Classes da peça 11 §4

**Classe 1 · grau 3** — `Fiel` (volta para a mão, não dá para desarmar) · `Aferido` (ao encostar, você sabe o grau da maldição) · `Presságio` (avisa que há maldição perto) · `Perene` (não quebra, e funciona onde arma comum não funciona).

**Classe 2 · grau 2** — `Quebranto` (Reação: anula um feitiço, uma vez por cena) · `Cisão` (o golpe causa dano de alma no lugar do de vida) · `Avulsa` (Reação: a arma sai da mão e ataca sozinha) · `Vazadura` (o golpe ignora a Redução de Dano do alvo).

**Classe 3 · grau 1 e especial** — `Anátema` (o contato anula técnica amaldiçoada) · `Insondável` (ponta escondida: o alcance dela é *na cena*) · `Contrapeso` (ignora o requisito de Força da arma).

### Registrado — o `Presságio` saiu de um buraco, e não de uma lista de ideias

**A Restrição Celestial pelo ramo da Maki não tem `Sentir Energia`** — está na peça 9, junto com *sem PE* e *sem golpe canalizado*. **É a única perícia do sistema que uma Origem inteira não pode ter**, e a ferramenta é o jeito que a obra dá para ela compensar.

*Vale registrar porque o método é o que sobrevive: a entrada não foi desenhada e depois justificada. Ela saiu de procurar o que a rota que a peça atende não consegue fazer.*

### Achado — a `Vazadura` quase não passou, e o critério que a salvou é da peça 14

Ela anula a Redução de Dano do alvo, e **a única RD do sistema é `1,5 × refino`** (peça 11 §6) — então o valor dela cresce com o refino de quem está do outro lado, e refino é o eixo proibido.

**A conta separou, com o mesmo critério que a peça 14 §4 usa: o que deriva é fração, não valor absoluto.**

| nível | refino | RD anulada | Rotina | % da Rotina |
|---|---|---|---|---|
| 2 | 1 | 1,5 | 13 | 11,5% |
| 18 | 7 | 10,5 | 77 | **13,6%** |
| 30 | 10 | 15,0 | 126 | 11,9% |

**O valor absoluto cresce dez vezes e a fração anda 3,3 pontos percentuais na campanha inteira.** *É o perfil que a peça 14 §4 chama de "um alvo estável, que é o melhor tipo de alvo para passar adiante".*

**E o `Contrapeso` foi medido pelo motivo contrário:** ele vale `+2,0` de dano médio para Força 0 a 2 e **zero** para quem tem Força 3 — o mesmo perfil que a v0.49 mediu no requisito de Força e aceitou como alvo legal do Desliga. **O gate de nível 13 é o que o segura:** 3,5% da Rotina no primeiro nível em que ele existe, 1,6% no nível 30. *Encolhe com o nível, que é o oposto de derivar.*

### Registrado — o `Insondável` não criou metragem própria

Ele usa as três faixas que a v0.55 fixou em Invocações — **no combate · na cena · fora da cena**. *Um número, um dono, e este tem: seria a segunda escala de distância longa do projeto no dia seguinte ao de a primeira ser escrita.*

### Confirmado — o teto de duas é de apoio

*Pergunta que a v0.55 deixou aberta.* **Duas de apoio**, e não duas contando a arma. A ficha topa em **três `Estigmas`** no caso declarado, que é **43%** do orçamento de escolha de marco da campanha.

### Em aberto

- **O validador da ferramenta**, com as checagens do §7 do rascunho. **Sem ele o catálogo não vira peça**, porque o `conferir-repositorio.py` conta peças contra validadores.
- **Invocações continua sendo a posição 1 da fila e continua rascunho** — e o buraco que mais morde para jogar é a **fórmula de vida com o termo de tipo vazio**: `base do tipo + (por nível do tipo + Con dela) × nível do dono`, com os quatro tipos escritos e **nenhum dos dois termos com valor**. *Uma fórmula com termo vazio parece pronta e não é.*
- **Trilhas:** a Q3 — a régua antes do catálogo.
- As de sempre.

---

## [0.55] — 2026-08-13

**A máquina de ferramenta amaldiçoada fechou, e a pergunta que eu tinha marcado como a mais perigosa da peça se resolveu pelo desenho que o Mizuki escolheu.** Fecharam também as duas faixas de alcance do `Remoto` e duas das cinco perguntas de Trilhas. Continuam **catorze peças e catorze validadores** — os três continuam rascunho.

### Decidido — o `Estigma`, uma por ferramenta, e o grau decide o FORMATO

*Decisão do Mizuki: "cada arma ter uma passiva a depender de seu grau, onde obviamente grau 4 só garante ser infundida com energia maldita".* **A segunda metade dessa frase é o achado da v0.54 chegando pela ficção** — a ferramenta entrega **ferir maldição**, que é binário, e o dano fica com a Técnica Marcial.

| grau | `Estigma` | gate | do material |
|---|---|---|---|
| **4** | **nenhum** — ela fere maldição, e é só | nenhum | a katana da Kasumi |
| **3** | **Classe 1** | nenhum | a espada do Toji, o machado da Mei Mei |
| **2** | **Classe 2** | **nível 7** | a Katana de Alma Partida |
| **1** | **Classe 3** | **nível 13** | as forjadas de topo |
| **especial** | **Classe 3**, e **única no mundo** | nível 13 | Nuvem Divertida · Lança Invertida · Corrente de Mil Milhas |

**O grau 4 não é o degrau fraco: é o que faz a peça existir.** As Classes são as da peça 11 §4, sem inventar nada.

### Decidido — o gate cai da peça 11, e a metade de refino fica de fora de propósito

Um `Estigma` de Classe 3 no nível 2 passaria por cima do gate que a peça 11 cobra de uma **aptidão da mesma Classe**. Então o gate é o dela: Cesta Oca (Classe 1) sem gate, Domínio Simples e Pétala (Classe 2) no **nível 7**, Extensão de Domínio (Classe 3) no **nível 13**.

> **Mas a peça 11 cobra *nível E refino*, e o refino não entra.** **Cobrar refino trancaria a peça na cara de quem ela existe para atender** — a Restrição Celestial pelo ramo da Maki não tem refino nenhum, porque não tem energia. *O gate herda o número e recusa o eixo.*

### Decidido — grau 1 contra especial é escassez, e não mecânica

*Decisão do Mizuki, e é o que o material diz.* Os dois dão Classe 3. **Grau 1 se forja; especial é uma só que existe**, com nome próprio. Zero número novo, e o que ele governa é a mão do mestre: uma especial por arco, não duas na mesma mesa.

### Decidido — `Desgaste`, e ele compra o GATE e nunca a Classe

*Decisão do Mizuki: a deterioração entra por balanceamento, porque **"ela é diferente da lança invertida por um motivo"**.* A Corda Negra *"perturba e cancela técnica alheia"* — trabalho de topo — e *"se deteriora com o uso"*, que nenhuma outra faz.

> **`Desgaste` — a ferramenta ignora o gate de nível do `Estigma` dela. Em troca, a cada missão em que o `Estigma` foi usado ela desce um grau. No grau 4 ela é arma comum, e não volta.**

**A máquina é a do §5.0.4 de Equipamento uma camada acima** — *"`Volumosa`, `Embainhada` e `Comprida` devolvem 1 ponto"*. **Restrição de verdade compra acesso.**

**E ele compra o gate e não a Classe de propósito.** Classe é **formato**, e a peça 11 escreve isso com todas as letras; uma restrição que subisse a Classe misturaria formato com magnitude, que é o eixo que este projeto separa desde a v0.30. **O gate é número puro, e número é o que se compra.** Pela curva da peça 12 — um nível custa de 1 a 10 missões —, três missões de uso é perto de um nível inteiro na faixa baixa.

### Medido — a pergunta mais perigosa da peça se fechou sozinha

*O rascunho dizia que "como uma ferramenta entra numa ficha" era **a que decide se a peça funciona**: num server com cinco a sete mestres, quem entrega o item é a maior fonte de divergência que existe.* **Com uma `Estigma` por ferramenta, ela para de ser perigosa.**

| ficha do mesmo nível | `Estigmas` | do orçamento de escolha de marco |
|---|---|---|
| mestre avaro — arma grau 4 | **0** | 0% |
| caso normal | 1 | 14% |
| **teto declarado** — arma + dois apoios | **3** | **43%** |
| extremo — duas armas de uma mão + dois apoios | 4 | 57% |

**A divergência inteira entre o mestre mais avaro e o mais generoso é de um a três `Estigmas`** — as mãos fecham o lado da arma e o teto de dois fecha o outro. *E a moeda é a do projeto: um `Estigma` de Classe 3 é o mesmo formato de uma aptidão de Classe 3, e aptidão se compra com escolha de marco, que são sete na campanha.*

**A tabela do D&D não traduz em volume** — ela entrega ~53 itens de raridade rara ou acima para um **grupo** em vinte níveis, porque lá o item se mede em dano e o grupo divide. **O que traduz é a estrutura**, que este projeto já usa em dois lugares.

### Registrado — `Aspecto` morreu por colisão com o hobby, não no validador

O Mizuki ofereceu **`Estigma` ou `Aspecto`**. Os dois saem **LIVRE** no `conferir-nomes.py` e têm **zero ocorrências no `.docx`**.

> **`Aspecto` é a mecânica central do Fate** — o SRD tem uma página chamada *"Invoking & Compelling Aspects"* —, e quem já jogou vai ler a palavra como aquilo. **É a colisão com o hobby que nenhuma checagem alcança**, e é a segunda desta semana, depois do `Provocar` da v0.53.

**`Estigma` fica**, e para ferramenta *amaldiçoada* ele é melhor de sentido: o grau alto é a marca da maldição sendo mais funda. *E `Passiva` estava OCUPADO — é peça do Fundamento —, que foi o que abriu a pergunta.*

### Decidido — as três faixas de alcance do `Remoto`, e nenhuma é um metro novo

*Buraco que só apareceu quando a entrada precisou de número:* **o projeto não tem nenhuma distância acima de 30 m escrita em lugar nenhum.** A escala inteira é `1,5 · 3 · 6 · 9 · 18 · 21 · 30`.

| faixa | o que é | quem alcança |
|---|---|---|
| **no combate** | os 18 m da amarra | toda invocação |
| **na cena** | *(um quarteirão)* | o `Remoto` |
| **fora da cena** | *(um país)* | o `Remoto`, **com gate** |

**A metragem entre parênteses é referência e não regra** — *decisão do Mizuki*, e é o mesmo formato que a peça 10 usou para não ter relógio de horas: *"gatilho de ficção — a luta acabou, a missão acabou — dois mestres arbitram igual"*. **Medir em metro uma coisa que ninguém vai medir é precisão falsa.**

> **E o gate do país é o primeiro do catálogo inteiro.** *Decisão do Mizuki:* exige **Restrição Celestial pelo ramo do corpo limitado** e uma **técnica voltada a isso** — o Ultimate Mechamaru, sem regra especial. **Nenhum `Traço` ou `Comando` tinha requisito até aqui.** A peça 11 §5 manda cada aptidão declarar o gate dela e permite *nenhum, só nível, só refino, ou os dois*; **este é de Origem, que é um quarto formato**, e fica marcado como decisão a escrever.

### Decidido — duas das cinco perguntas de Trilhas

*Decisão do Mizuki: "Caminhos não podem se misturar, não estou pensando nesse sistema podendo ter multiclasse, no máximo multi subtrilhas, que são do mesmo caminho".*

| | |
|---|---|
| **Q1** | **uma Trilha por ficha, sem multiclasse.** Fecha a pendência nº 3 do `ESTADO-ATUAL`, aberta desde a v0.22, e **mata as 105 combinações** que eram o maior risco de matriz da peça |
| **Q4** | **as subtrilhas existem e cruzam Trilhas do mesmo Caminho** — `Caminho` → `Trilha` → `subtrilha`, e a subtrilha atravessa as três Trilhas do Caminho |

> **A Q4 devolve metade do que a Q1 economizou, e o número importa para a régua.** A matriz deixa de varrer as 15 Trilhas e passa a varrer as **combinações de subtrilha dentro de cada Caminho** — e a pergunta aberta desde a v0.24 muda de forma: *"o Guia contra a Vanguarda"* vira *"esta combinação de Guia contra aquela de Vanguarda"*. **A régua tem de nascer sabendo que precifica peças que se somam.**

### Em aberto

- **Ferramenta:** o **catálogo de `Estigma`** entrada por entrada, e o **validador da peça**. *E uma leitura a confirmar: "no máximo 2" foi lido como duas de apoio (43% do orçamento de marco) e não duas contando a arma (29%).*
- **Trilhas:** a **Q3 — a régua, e ela vem antes do catálogo**, que é o que separa uma versão de seis. Mais a Q2 (quantas entregas) e a Q5 (o conteúdo).
- **Invocações:** o gate de Origem do `Remoto` precisa de decisão escrita como quarto formato de gate; e as de sempre — Rika e Mahoraga, a fórmula de vida por tipo, reconseguir, o validador.
- As de sempre: as vagas de Desliga, a Cicatriz, Energia Reversa, o clash, o nome do sistema.

---

## [0.54] — 2026-08-13

**As posições 2 e 3 da fila ganharam rascunho, e nenhuma regra mudou.** Sessão sem o Mizuki, com permissão para agir: `ferramenta amaldiçoada` e `Trilhas`. **Passam a ser cinco rascunhos**, e continuam **catorze peças e catorze validadores** — o `conferir-repositorio.py` ganhou uma **quinta checagem** e continua sendo o mesmo arquivo. A conta fechou cinco coisas antes de qualquer pergunta, e uma delas derruba o exemplo que abriu a sessão.

### Achado — o cubo que prendeu o Gojo não é ferramenta amaldiçoada

*O pedido nomeou duas categorias: armas de grau, e "ferramentas, artefatos amaldiçoados, como cubo que prendeu Gojo". Fui conferir o segundo antes de escrever.*

> **O Prison Realm é *"a special grade cursed **object**"***, e a regra que separa está escrita na fonte: *"com exceção de ferramentas amaldiçoadas e cadáveres amaldiçoados, itens que contêm energia amaldiçoada são chamados de **objetos amaldiçoados**"*. Ele aparece na lista ao lado dos **dedos do Sukuna** e das **Pinturas de Ventre Amaldiçoado**.

**É a separação que a v0.49 achou, agora do outro lado.** Ferramenta é *feita para* canalizar; objeto **é** a coisa. O Prison Realm é carne viva com um olho no meio, que sela por vontade própria — não é forjado.

**E a categoria 2 não perde nada:** a definição de ferramenta amaldiçoada já é *"**weapons and support items**"*, e os exemplares certos são a **Corrente de Mil Milhas**, a **câmera da Nanako** e o **violão do Gakuganji**. *O que muda é só qual peça é dona do cubo, e é a que a conta pôs em último na v0.50.*

### Achado — grau não pode ser mais ponto de arma, e ele erra nas duas pontas

O ponto de arma tem valor absoluto (`0,33` de dano por rodada, peça 14 §5) e a Rotina cresce:

| nível | Rotina | **+5 pontos** — dobrar uma arma de duas mãos |
|---|---|---|
| 2 | 13 | **12,7%** |
| 10 | 45 | 3,7% |
| **30** | **126** | **1,3%** |

**Contra os `6%` a `9%` que a peça 14 §4 diz que uma Trilha inteira vale.** A Lança Invertida do Céu não pode valer um sétimo de uma Trilha no nível 30 — e no nível 2 os mesmos 5 pontos valem **mais** que uma Trilha. **Grande demais embaixo, invisível em cima: é o formato errado, não um número mal escolhido.**

*E o D&D chegou no mesmo lugar por outro caminho:* lá o item mágico também não escala — um `+3` é `+3` para sempre —, e o que faz um lendário importar no nível 17 **não é o número, é o que ele deixa você fazer.**

### Achado — a ferramenta não é o que faz o sem-energia competir em dano

*Esta muda o desenho da peça, e ela contradiz a leitura fácil da peça 5 §3.* A arma comum **não escala** — o dado é fixo e o atributo topa em 6:

| nível | Rotina | melhor arma (`d12` + Força 6) | % da Rotina | o que falta |
|---|---|---|---|---|
| 2 | 13 | 12,5 | **96%** | 0,5 |
| 10 | 45 | 12,5 | 28% | 32,5 |
| **30** | **126** | **12,5** | **10%** | **113,5** |

> **Uma ferramenta que tivesse de fechar isso precisaria entregar 113 de dano por rodada no nível 30 — o Fundamento inteiro, não um item.**

**Então a divisão cai da conta:** a **ferramenta** entrega **ferir maldição**, que é **binário**; a **Técnica Marcial** entrega o dano. *A peça 5 §3 já dizia isso e ninguém tinha lido assim — "é por isso que um feiticeiro consegue ferir uma maldição e uma pessoa comum não" é frase sobre poder ou não poder, e o resto do parágrafo é sobre dano.*

**E isso desarma sozinho o medo da peça 5 §5** (*"cara o suficiente para não virar o padrão"*): entregando porta e não dano, **ela não pode virar o padrão do feiticeiro**, que já tem a porta de graça pelo golpe canalizado. *Uma pendência aberta desde a peça 5 dissolvendo quando a unidade certa aparece — igual à Q5 de Invocações dissolvendo na Q4.*

### Achado — grau como gate de patente está refutado pela peça 12

A ideia óbvia — *"feiticeiro de Grau 2 porta ferramenta de grau 2"* — bate na frase que a peça 12 escreveu para rejeitar *"Grau dá mais XP"*:

> *"**Grau é reconhecimento; nível é poder.** Se o Grau passar a dar XP, ele vira nível com outro nome — e pior, vira **espiral fechada**."*

**Trocar "XP" por "ferramenta" não muda uma vírgula.** Sobe de patente → ferramenta melhor → mais poder → mais feito → sobe de patente. *A peça 12 já pagou por esse achado; ele só precisava ser lido no eixo novo.*

### Registrado — a colisão de nome é de expectativa, não de palavra

**`Grau` já é a patente** — *"todo personagem começa Grau 4"*, na peça 2, na 8 e na 9, com o Yuta de **Grau especial**. Mesma escala, mesmas cinco casas, outra coisa. E **`Ferramenta` sai OCUPADO na triagem: é Tema no manual**, igual a `Invocação`.

**A recomendação registrada é manter `Grau`**, porque no material os dois **são** a mesma escada de propósito, e um segundo vocabulário conserta uma ambiguidade que o contexto já resolve. **O que precisa estar escrito é a negação da ligação** — *a sua patente não decide que ferramenta você porta, e a ferramenta não mexe na sua patente.* Livres, se ele preferir trocar: `Têmpera` · `Quilate` · `Cunho` · `Lavra` · `Estirpe` · `Relíquia`.

### Achado — catorze dos vinte e nove níveis não entregam nada, e são todos os ímpares

*Montada a **tabela de progressão consolidada** que o `ESTADO-ATUAL` lista como inexistente, para saber onde a entrega da Trilha cabe. Ela respondeu a pergunta sozinha.*

| o que cai onde | |
|---|---|
| feitiços conhecidos (`2 + nível ÷ 2`) | **todo nível par** |
| maestria (nv 10, 18, 26) e os sete marcos | em cima de níveis pares que **já tinham feitiço** |
| **os catorze ímpares** | **nada** |

**O D&D 2024 padronizou a subclasse em 3, 6, 10 e 14 justamente para não empilhar presente no mesmo nível.** Aqui a lacuna é maior e mais regular. **A Trilha tem onde cair sem competir com nada** — e isso é decisão de formato tomada por medição, antes de a peça começar.

### Achado — a entrega da Trilha tem de ser escalonada, e não é gosto de densidade

A peça 14 §4 registra a dívida como *"de 6% a 9% da Rotina, e a fração quase não deriva"*. **A fração não deriva; o valor absoluto cresce dez vezes** — 0,8 a 1,2 no nível 2 contra 7,6 a 11,3 no nível 30.

**Uma Trilha que entregue tudo no nível 2 paga a dívida ali e vale `0,9%` da Rotina no nível 30.** *É o mesmo modo de falha do ponto de arma, dois achados acima: valor absoluto contra alvo que cresce.* **O mínimo é mais de uma entrega, e quem diz é a conta.**

### Medido — o risco real de Trilhas é escala, e ele tem número

| entregas por Trilha | × 15 | comparável a |
|---|---|---|
| 8 — nível 2 mais os sete marcos | **120** | nada que este projeto já tenha escrito |
| **4** — níveis 2, 10, 18, 26 | **60** | peça 13: 81 entradas, **uma versão** |
| 2 — níveis 2 e 16 | 30 | peça 11: 10 entradas, uma versão |

> **A peça 13 e a peça 14 são a lição inteira, e discordam de propósito.** Legados fez **81 entradas em uma versão** porque **a régua veio antes do catálogo** — *"os quatro Legados que a régua reprovou eram do catálogo antigo"*. Equipamento gastou **seis versões** porque a régua foi consertada com o catálogo já escrito, e cada conserto envelhecia o que existia.
>
> **Trilhas é maior que as duas.** Escrever entrada antes de a régua fechar é a rota de seis versões, com 60 a 120 entradas em vez de 52.

### Adicionado — a checagem 5 do `conferir-repositorio.py`: ponteiro de seção

*Escrita na revisão cética desta versão, indo conferir os ponteiros que os dois rascunhos novos criaram. **Ela fecha um buraco que a v0.50 nomeou e não teve como tapar:***

> *"O `conferir-repositorio.py` confere referência **de arquivo** [...] **Referência de seção passa por baixo dele.** Lição nº 9 numa camada mais fina que a de sempre: não é um número com dois donos, é um ponteiro para dentro de um documento que nenhuma checagem resolve."*

**Todo `peça N §M` citado em `.md` tem de apontar para uma seção que existe.** Rodando hoje: **129 ponteiros, e os 129 resolvem.**

> **`logs/` fica de fora de propósito.** As duas citações sobreviventes de *"peça 5 §9"* moram na entrada da v0.49, e a v0.50 decidiu por escrito não reescrever histórico para esconder erro. **Acusá-las seria pedir para desfazer aquela decisão.** *A regra da checagem é a decisão do projeto, escrita no comentário dela.*

**Arnês de perturbação, numa cópia isolada, com a base conferida verde antes** — e as três regras obedecidas:

| perturbação | acendeu? |
|---|---|
| ressuscitar o fantasma: um `peça 5 §3` virando `peça 5 §9` | **sim**, com a mensagem nomeando as cinco seções reais |
| citar `peça 15 §4`, que não existe | **sim** |
| **contra-teste:** trocar por `peça 6 §3.1`, que existe | **não acendeu**, como tem de ser |
| **contra-teste 2:** uma perturbação produz **um** erro | **sim** — as checagens não estão acopladas |

*E o cuidado é herdado: a v0.51 registra um checker meu que acusou **cinco referências boas** por capturar `4.` com o ponto e comparar contra `4`. O `rstrip('.')` desta checagem existe por causa daquele dia, e está comentado no código.*

### Registrado — o levantamento externo

**Cursed Tool** (*"weapons and support items... purposefully imbued with a curse"*, *"categorized from grade one to four based on their power and potency"*, *"even non-sorcerers can use them"*), com o catálogo por grau — Nuvem Divertida e Lança Invertida do Céu como especial, a Corda Negra que *"se deteriora com o uso"*, e a katana da Kasumi como **semi-ferramenta**, que é um degrau abaixo do grau 4 que o material tem e a escada não. **Cursed Object** (a regra de exclusão, e a lista com o Prison Realm dentro). **D&D**: as seis raridades sobre quatro tiers, a **sintonização** — *"no more than three magic items at a time"* — e a metade que serve de graça, *"without becoming attuned... gains only its **nonmagical benefits**"*, que é o que deixa a camada existir **sem furar o fundo de Equipamento**. **D&D 2024**: subclasse padronizada em *"3rd, 6th, 10th, and 14th level"*.

### Registrado — o que NÃO foi decidido, e por quê

*Sessão sem o Mizuki. Escolha de sabor é dele, e nenhuma foi fechada:* quantas entregas por Trilha, uma Trilha ou mais por ficha, se subtrilha existe, o nome do grau, qual o gate de acesso, e quantas ferramentas de apoio se carrega. **Todas estão nos dois rascunhos com as opções e o número de cada uma já calculados.**

### Em aberto

- **Ferramenta:** as sete perguntas do §5 do rascunho — o que o grau compra, se o grau 4 dá algo além da porta, o gate, o teto das que não ocupam mão, **como uma ferramenta entra numa ficha e atravessa sete mesas** (a que decide se a peça funciona), se toda ferramenta canaliza sozinha, e se a deterioração existe.
- **Trilhas:** as cinco perguntas do §3 — quantas Trilhas por ficha, quantas entregas e em que níveis, **a régua antes do catálogo**, se subtrilha existe, e o conteúdo.
- Tudo o que a v0.53 deixou: Rika e Mahoraga, a fórmula de vida por tipo, reconseguir, o alcance do `Remoto`, o validador de Invocações.
- As de sempre: as vagas de Desliga, a Cicatriz, Energia Reversa, o clash, o nome do sistema.

---

## [0.53] — 2026-08-13

**O catálogo de Invocações foi escrito entrada por entrada, e três dos quatro tipos pediram menos do que o tamanho da pergunta.** As catorze entradas da v0.51 e da v0.52 tinham saído todas dos shikigami do Megumi — que é um tipo só. Passados os outros três, o catálogo foi de **13 para 19 compráveis**, e a passada achou um buraco que estava aberto desde a v0.50: **não existia regra de distância entre dono e invocação.** Continuam **catorze peças e catorze validadores** — Invocações continua rascunho até o validador dela existir.

### Achado — não existia amarra, e a Q4 tinha tornado isso urgente sem ninguém ver

Varrido o rascunho inteiro e a peça 6: **zero regra de distância.** A única menção era a nota do PF2e (*"o eidolon tem que ficar a até 30 m do dono"*), marcada de propósito como *"não coisa a importar"*.

**A Q4 é quem cobrou.** Com **comandar custando a ação padrão**, *"dá para comandar daqui?"* virou pergunta de toda rodada, e a resposta era julgamento do mestre — que é o formato que este projeto reprova por definição.

> **A invocação fica a até 18 metros do dono. Além disso ela não pode ser comandada, e não some.**

**O 18 não é número novo:** é o **alcance base de Projétil**, do manual, que a peça 3 §3 já usa como âncora do deslocamento base — *"um turno de movimento fecha metade da distância de um duelo"*. Dois turnos de movimento à frente, e zero parâmetro livre.

**Os 9 m foram medidos e reprovados:** com a amarra no deslocamento base, a Matilha de cinco corpos não abre leque nenhum e o `Traço` de alcance vira compra obrigatória — **propriedade morta**, no vocabulário que Equipamento já tem para isso.

**E não sumir fora da amarra é decisão.** Se sumisse, o inimigo que a empurrasse para além dos 18 m apagaria `1 × maior Classe` de PE e uma ação padrão **com um empurrão**. Parada custa a rodada; sumir custaria o recurso.

### Achado — a maldição domada atravessa a máquina inteira sem pedir nada

*Levantado no texto e não de memória:* **"the user can also extract the curse techniques of semi-grade 1 and above cursed spirits they absorb"** — a maldição domada carrega a técnica dela. E isso se parte em dois, com dono dos dois lados:

| a técnica dela | onde cai |
|---|---|
| causa dano | **ilegal** — o teto de uma Rotina da peça 6 §4 |
| não causa dano | **é exatamente o que `Traço` e `Comando` são** |

O `Maximum: Uzumaki` (*"combines any number of cursed spirits into one and hits the target with a blast"*) cai na primeira linha; e *"a user can only absorb tamed cursed spirits after killing their master"* é **reconseguir**, que a Q5 já tinha mandado para tempo de campanha.

**Um tipo inteiro do material passando pela máquina sem pedir entrada nova é o melhor sinal que ela já deu de que está certa.** *Não é levantamento fraco: é a régua cobrindo o caso antes de ele chegar.*

### Achado — o selar do talismã nomeia uma peça que não existe, e quase virou entrada

A fonte define talismã como *"paper tags with sutras written on them"*, com função principal de **selar**: *"halt the lifestream and preserve the existence of cursed objects while preventing them from doing any further damage"*.

> **O alvo do selo é `objeto amaldiçoado`** — que a **v0.49** descobriu não ter peça dona nenhuma e a **v0.50** pôs em **último** na fila. Escrever a entrada agora é a **vaga de Desliga nomeando a peça errada**, que é o defeito que aquelas duas versões inteiras foram gastas para achar. *Fica marcado com o nome certo em vez de escrito com o alvo errado.*

O que sobrou do talismã é o eixo dos shikigami que **não** são do Megumi — o rato e o pássaro do Dhruv, o Kogane, o Marmalade Boy do Masaki. Todos batedores, e todos **informando o dono**. O `Faro` rastreia e **nada dizia que o dono recebia alguma coisa disso**.

### Decidido — o núcleo do Panda não existe

*Decisão do Mizuki.* O Panda *"has three cores. He can shift the cores in battle"*, e trocar de configuração no meio da luta **não cabe em 1 nem em 2 pontos: ele dobra a montagem inteira.**

| saída | por que não |
|---|---|
| degrau de **3 pontos** | o orçamento do nível 2 é 2 — ele nasce inalcançável até o nível 6, e é degrau com **um morador só**. É escrever entrada para fechar contagem, que é o defeito que a régua de Legados nasceu para achar |
| **concessão de Trilha** | empurra a decisão para a peça de Trilhas, que ainda não existe |

**Corpo amaldiçoado fica sendo fórmula de vida própria e sabor**, como os outros três tipos.

### Decidido — e uma terceira coisa que a criação não compra: agir sozinha

*"Programmed with predetermined commands or act autonomously"* é o que a fonte diz do corpo amaldiçoado. **Aqui isso é ilegal, e o motivo é a Q4 inteira.**

Agir sem o dono gastar a ação padrão **é** a exceção do `Coro`. A Q4 comprou o teto de uma Rotina justamente porque ele passou a **cair da economia de ação** em vez de ser decreto. Virar ponto de orçamento devolve o teto para o decreto — *desfazendo, por 2 pontos, o que uma pergunta inteira foi gasta para conseguir de graça.*

### Adicionado — seis entradas, e cada uma com o degrau derivado da régua

| camada | pts | entrada | de onde veio |
|---|---|---|---|
| `Traço` | 1 | **`Vigia`** — o que ela vê e ouve, você vê e ouve | Kogane · os shikigami de rato e pássaro do Dhruv |
| `Traço` | 1 | **`Fala`** — ela fala, e dá para conversar com ela | Kogane · Marmalade Boy · Panda |
| `Traço` | 2 | **`Graúdo`** — ocupa espaço maior e barra passagem | Elefante Máximo · peça 6 §4 |
| `Traço` | 2 | **`Remoto`** — funciona além dos 18 m | Ultimate Mechamaru |
| `Comando` | 1 | **`Cavar`** — abre buraco, desenterra, revira o terreno | Serpente · Elefante Máximo |
| `Comando` | 2 | **`Chamariz`** — o alvo tem de vir para cima dela | Coelho de Fuga |

**O `Graúdo` é o caso que testa a régua nos dois sentidos.** Ocupar espaço está escrito no degrau de **1** (*"que espaço ocupa"*), e é por isso que o `Miúdo` custa 1: passar por um vão só acontece com ela. **Barrar passagem é o inimigo perdendo movimento** — encosta em outra criatura, degrau de 2. *É a linha `Escalada` contra `Voo`, medida no outro eixo.*

**E o `Chamariz` é a única entrada que existe porque um shikigami do material não fechava sem ela.** A peça 6 §4 vende o produto do invocador como *"corpos que absorvem ataque, flanqueiam e bloqueiam caminho"*, e o Coelho de Fuga é *"muitos corpos que **distraem** para o dono fugir"*. **Absorver e bloquear tinham entrada; distrair não tinha nenhuma.**

### Registrado — um nome morreu por sentido depois de sair LIVRE na triagem

O `Chamariz` ia se chamar **`Provocar`**. Ele **sai LIVRE** no `conferir-nomes.py` — e `Provocar` é **perícia de Essência**, na peça 7. Um `Comando` com nome de perícia manda a mesa procurar uma rolagem que não existe.

*É a colisão de sentido que a triagem não pega, avisada na skill e confirmada aqui pela enésima vez.* **E ela pegou uma segunda:** um `Traço` de corpo duro — *"ela aguenta mais porque é objeto, não carne"* — **compra Defesa com ponto, e Defesa já é a moeda do deslocamento do §3.6.** Dois preços para a mesma coisa, que é a lição nº 2 na forma exata em que ela reincide aqui.

### Medido — o que o catálogo maior comprou, e o que ele não comprou

Enumeradas todas as montagens que gastam o orçamento **exato** (sobrar ponto é dominância estrita, mesmo argumento do fundo de Equipamento §5.0):

| | montagens cheias no nv30 | entradas na maior | % do catálogo consumido |
|---|---|---|---|
| **13 entradas — antes** | 1.126 | 8 | **62%** |
| **19 entradas — agora** | **21.502** | 9 | **47%** |

**Zero montagens dominadas, e as 21.502 têm assinatura distinta.** *A comparação certa é Equipamento, que fechou com 39 assinaturas para 41 armas.*

**E uma coisa que a conta respondeu sozinha, sem pergunta:** vender deslocamento **não precisa de piso**. Mesmo a **−5 de Defesa**, o pool da Matilha ainda põe **20% a 27%** da vida da mesa em campo, contra os **6% a 9%** da Rotina que a peça 14 §4 diz que uma Trilha inteira vale. Ela se limita sozinha no valor.

### Corrigido — o mesmo erro da v0.51, pego pelo hábito que aquela versão criou

**Eu escrevi `1.126 montagens` e `42% do catálogo` na lista do validador — os números de 13 entradas, por cima do catálogo de 19.** São **21.502** e **47%**.

*É exatamente a família das cinco correções da v0.51 — resumo em prosa por cima de tabela que o script já tinha impresso.* **A diferença é que desta vez ela não chegou ao arquivo fechado:** rodei o script antes de fechar em vez de depois, que é a única coisa que aquela versão pediu.

### Corrigido — "as treze checagens" eram vinte e três, e dois documentos repetiam

*Achado indo contar antes de citar.* O §5 do rascunho **nunca teve treze checagens** — ele fechou a v0.51 com **vinte e três**, e o número `treze` está escrito na entrada daquela versão e no `ESTADO-ATUAL`.

| onde | dizia | é |
|---|---|---|
| `CHANGELOG`, v0.51, em aberto | *"as treze checagens que o §5 lista"* | **23** |
| `ESTADO-ATUAL`, "o que separa o rascunho da peça 15" | a mesma frase | **23** |

**O `ESTADO-ATUAL` foi corrigido; a entrada da v0.51 fica como está** — a v0.50 já escreveu por que não se reescreve histórico de CHANGELOG, e o mesmo argumento vale aqui.

> **E o modo de falha tem nome de casa.** O `treze` não saiu de contar errado: **saiu de arrastar o número de peças e validadores para dentro de uma frase que falava de outra coisa.** Treze era a contagem do repositório à época — e ela virou catorze na v0.48 sem que esta frase se movesse. *Lição nº 9 numa forma que nenhum validador alcança: não é uma cópia divergindo do dono, é um número **emprestado do vizinho** e depois abandonado por ele.*

### Registrado — o levantamento externo

Lido em vez de lembrado: **Cursed Corpse** (*"a nonliving object that has been endowed with a curse, allowing it to gain self-control"*, núcleos como coração, Panda com três, *"programmed with predetermined commands or act autonomously"*); **Cursed Spirit Manipulation** (*"extract the curse techniques of semi-grade 1 and above"*, `Maximum: Uzumaki`, *"only absorb tamed cursed spirits after killing their master"*); **Talisman** (*"paper tags with sutras"*, selar como função principal, *"can serve as an intermediary to conjure shikigami"*); e a lista de **Shikigami** fora do Dez Sombras — Kogane, o rato e o pássaro do Dhruv, o Marmalade Boy do Masaki, o Garuda da Yuki, os peixes do Dagon, o Moon Dregs do Junpei.

**O Moon Dregs foi levantado e não virou entrada:** veneno é condição, e a peça de **dano e condições** não existe. *Mesma trava do selar, e as duas ficam marcadas com o nome da peça dona em vez de escritas na base do jeito.*

### Em aberto

- **Rika e Mahoraga**, que agem fora do controle do portador e não são ponto de orçamento.
- **A fórmula de vida com número por tipo.** Os quatro tipos existem, a fórmula tem o termo, **e o termo está vazio.** *Uma fórmula com termo vazio é pior que uma faltando: ela parece pronta.*
- **Reconseguir a invocação morta** — tempo de campanha, da peça de Trilhas ou da passada de material.
- **O validador dono da peça**, agora com **vinte e oito** checagens listadas no §5 do rascunho — as vinte e três de antes, mais a amarra, a contagem do catálogo, a busca exaustiva com número esperado, o piso da venda e a trava de não comprar deslocamento com entrada.
- **O que o `Remoto` alcança.** *Furo meu, marcado na revisão cética:* escrevi a entrada como *"funciona além dos 18 m"* e não pus número no **além**. A conta não decide — ele não compra dano —, e as duas saídas estão medidas no §3.6.
- **O selar do talismã** (espera `objeto amaldiçoado`) e **o veneno** (espera dano e condições).
- **A Q6**, que é da peça de Trilhas e já tem metade da resposta.
- As mesmas de sempre: as vagas de Desliga, a Cicatriz, Energia Reversa, o clash, o nome do sistema.

---

## [0.52] — 2026-08-13

**O jogador passa a poder criar `Traço` e `Comando`, e a régua para isso já estava escrita em duas peças.** Adendo à v0.51, fechado logo depois dela: nenhum número mudou, e o que entrou foi o critério que permite pôr no catálogo uma coisa que não está nele. Continuam **catorze peças e catorze validadores**.

### Decidido — o catálogo é a régua, não a lista

*Pedido do Mizuki: "faltou mencionar no `Traço` e no `Comando` a opção de criar, e aí com a tabela de catálogo o player pode se basear para criar."*

**O projeto já tinha decidido isto para outro caso, e a frase está na peça 12:**

> *"'O mestre decide o que é um feito' **não atravessa sete mesas**. A lista precisa ser fechada, no molde do ambiente propício: **entradas escritas, e a palavra final do mestre em cima delas — nunca do zero**."*

**Então o catálogo de Invocações não é a lista do que existe: é a régua contra a qual o que não existe é medido.** E o critério não precisou ser inventado — ele sai das quatorze entradas que a v0.51 já tinha escrito:

| pontos | `Traço` |
|---|---|
| **1** | **só mexe na própria invocação** — como ela anda, o que ela percebe, que espaço ocupa. `Escalada`, `Nado`, `Faro`, `Miúdo` |
| **2** | **encosta em outra criatura ou no tabuleiro** — carrega, prende, empurra, alcança além do alcance, aparece onde não dava. `Voo`, `Montaria`, `Fisgada`, `Emboscada`, `Jorro` |

| pontos | `Comando` |
|---|---|
| **0** | **o ataque.** `Investir`, que toda invocação tem |
| **1** | **faz uma coisa com um alvo ou um objeto.** `Agarrar`, `Arrastar`, `Buscar` |
| **2** | **protege o dono, ou nega a ação de outro.** `Interpor` |

> **O `Voo` é o caso que prova a régua.** Andar custa 1 e voar custa 2 — **não porque voar seja "melhor"**, mas porque ele deixa de ser uma coisa que a invocação faz consigo mesma e passa a ser uma que ignora o tabuleiro inteiro. *É a mesma linha que separa `Climb` de `Flight` no PF1e, alcançada por outro caminho.* **Um critério que reproduz sozinho a divisão de um sistema publicado é critério, e não gosto arrumado depois.**

### Decidido — três coisas que a criação não compra a preço nenhum

**Elas não são caras: são ilegais**, e cada uma tem dono que já disse por quê.

| não pode | por quê | dono |
|---|---|---|
| **dado de dano** | o teto de uma Rotina já governa a saída. Um `Traço` que dá `+1d6` não custa 3 pontos — ele não existe | peça 6 §4 |
| **qualquer coisa que cresça com refino** | refino cresce `+7` a `+9` contra `+3`, e isso é 70% de acerto no nível 30 | peça 11 §2 |
| **deslocamento positivo** | a invocação não passa do portador | §3.6 do rascunho |

### Medido — quanto a régua economiza no filtro multi-mestre

| quem precifica o que o jogador inventou | divergência possível entre dois mestres |
|---|---|
| o mestre, do zero | **2 pontos — 20%** do que a invocação entrega |
| **a escada por efeito, com a palavra final em cima** | **1 ponto — 10%** |

**Ela corta a divergência pela metade e a põe numa faixa com tamanho já medido** — 1 ponto vale `+10%` do que a invocação entrega, ou `+11%` de vida efetiva. *Não é zero, e não devia ser: a palavra final continua sendo do mestre. O que a régua faz é impedir que ela seja dada do nada.*

### Adicionado — uma checagem que o validador da peça vai precisar

**Toda entrada publicada tem de cair no degrau que a própria régua manda.** *Uma entrada que desobedece ao critério é pior que uma entrada mal precificada:* ela ensina a mesa a ignorar a régua, e aí o `Traço` inventado no meio da sessão passa a ser precificado por imitação de uma exceção.

### Registrado — como isto quase virou reescrita de histórico

*Vale escrever porque o método é o que sobrevive à sessão.* Eu escrevi esta decisão **dentro da entrada da v0.51**, sem saber que ela já tinha sido commitada. **O que denunciou foi o `mensagem-de-commit.txt` sumir da pasta** — o `subir.sh` usa o arquivo e apaga depois, e o `ls` não achar foi o sinal.

**Não é o defeito do mount que este repositório documenta** (aquele é `open()` devolvendo ENOENT enquanto o `ls` mostra o arquivo). **Era o contrário: o arquivo não estava lá porque tinha cumprido a função dele.** A entrada da v0.51 foi restaurada e esta abriu no lugar. *Entrada de CHANGELOG é registro do que se pensou naquele dia, e a v0.50 já tinha escrito por que não se reescreve uma.*

### Em aberto

As mesmas da v0.51 — nenhuma foi tocada. **O catálogo escrito entrada por entrada**, **Rika e Mahoraga**, **reconseguir a invocação morta**, **o validador dono da peça**, e a **Q6**, que é da peça de Trilhas.

---

## [0.51] — 2026-08-13

**Cinco das seis perguntas de Invocações fecharam, e nenhuma peça nova nasceu.** O `RASCUNHO-invocacoes.md` foi de 103 para 751 linhas: iniciativa, o modelo da Matilha, a ficha, o custo e a morte. Continuam **catorze peças e catorze validadores** — ele vira a peça 15 quando o catálogo e o validador existirem.

### Decidido — as cinco perguntas

| | fechou em |
|---|---|
| **Q1** iniciativa | a invocação **compartilha o número do dono** e age logo depois. Não abre casa nova, com um corpo ou cinco |
| **Q2** cinco fichas ou uma | **uma ficha com cinco corpos**, pool de vida com cascata, e a rodada resolvida **em pool** |
| **Q3** a ficha | **derivada do dono mais um deslocamento fixo**; `Traço` e `Comando`; orçamento de **2 a 9** pontos |
| **Q4** o custo | **`1 × maior Classe` de PE e a ação padrão** para invocar; **comandar custa a ação padrão** |
| **Q5** a morte | **some no zero**, vulnerável a área (**dobro**), e **morre em definitivo** nos dois gatilhos |

### Achado — o teto da peça 6 §4 deixou de precisar de decreto

Com comandar custando a ação padrão, o dono e a invocação ficam **mutuamente exclusivos na rodada**:

| | ação da invocação livre | comandar custa a padrão |
|---|---|---|
| dono entrega | 1/5 da Rotina | **0 — ele comandou** |
| invocações entregam | 4/5 | **1 Rotina inteira** |
| **o que segura o teto** | uma frase da peça 6 | **a economia de ação** |

**Uma regra que cai da economia não precisa de ninguém policiando** — é o filtro multi-mestre passando de graça. E o **Coro** vira a exceção que a peça 5 §4 já autoriza com essas palavras: *"exceção estreita e paga na economia de ação"*.

### Achado — iniciativa por corpo morre no teste que a peça 3 §5 já usava

*"Pelo menos um corpo meu age antes do inimigo"*, com a conta da peça 3 §5 (que reproduz a tabela do Adianta exata — 52,5 / 57,2 / 66,0 / 38,2):

| corpos | casa por corpo | casa do dono |
|---|---|---|
| 2 — Servo, Coro | 77,4% | 52,5% |
| 5 — **Matilha** | **97,6%** | 52,5% |

**Escala com o número de corpos e ninguém pagou.** É o teste que a peça 3 §5 usou para rejeitar iniciativa fixa. **E o contra-teste fecha:** a mesma conta no **dano** dá 52,5% nas três saídas — a conta de dano empata, e é a confirmação numérica do buraco que o rascunho tinha achado. **Zero de seis sistemas levantados dão um número de iniciativa por corpo**, nem o `conjure animals` de 2014, que já rolava uma para o bando.

### Achado — a régua do PE era a errada, e o arredondamento colapsa metade da escada

*Decisão do Mizuki: invocação é coisa que **qualquer Caminho** pode usar.* Então o piso é o **Bastião** (4 PE por nível), e não o Evocador — está escrito no comentário do próprio `conferir-orcamento.py`. **Todas as contas da primeira passada mediam 1,5× o bolso certo.**

E pela peça 1 §5.4 o custo arredonda para cima: **no nível 2 a régua da maior Classe só tem dois degraus.** `teto(0,5 × Classe 1) = 1 = 1 × Classe 1` — **meio preço é preço inteiro no nível em que toda ficha nasce.** `1,5×` e `2×` deixam o Bastião de nível 2 com zero feitiços no dia e saem por conta.

O `1×` escolhido cobra **exatamente um feitiço do dia em todo nível**, do 2 ao 30, e cai no mesmo lugar que um feitiço do topo (22% do dia no nv10).

### Achado — "a primeira invocação é grátis" reprova no filtro multi-mestre

| como o mestre joga | reinvocações no dia | preço efetivo |
|---|---|---|
| espalha entre os cinco alvos | 0,8 | 84% |
| **foca na invocação** | **4,2** | **420%** |

**O mesmo personagem, o mesmo dia: o preço varia cinco vezes conforme quem está mestrando.** *Um preço que só é cobrado quando o mestre decide cobrá-lo não é preço — é imposto variável.*

**E as duas alternativas morreram cada uma por um número:** teto de reinvocações por descanso faz o jogador passar **10,2 das 10,5 rodadas do dia sem o Caminho dele**; e *"a primeira de cada luta não custa ação"* devolve **três Rotinas por dia** e cobra o equivalente a **uma** — desconto maior que o preço.

**A metade que sobrevive não precisa de regra nenhuma:** fora de combate a ação não custa nada, então quem invoca antes da luta entra em campo com a invocação de pé. **É o Megumi com o lobo, e já estava lá.**

### Achado — a área apagava a Matilha, e "vulnerável" resolve sem palavra nova

Com pool único e vida de corpo em meia Rotina, **um feitiço de área de rotina levava `5 × 0,5 = 2,5` Rotinas ao pool — o pool inteiro.**

*Decisão do Mizuki: a área causa o dano **uma vez** no pool, com a invocação **vulnerável**.* Com `×2`, um feitiço de área de rotina tira **dois dos cinco corpos**; apagar a Matilha passa a exigir **1,25 Rotina de área por alvo**. **Contra golpe único o mesmo feitiço tiraria um corpo — então a área vale o dobro, que é o que "vulnerável" já quer dizer.**

### Registrado — a morte em definitivo é canon literal

*Decisão do Mizuki, e a fonte confirma com essas palavras:* **"Once destroyed, they cannot be summoned again."**

A invocação morre de vez se o excedente passar de **metade da vida máxima**, ou se **um golpe causar a vida máxima inteira**. **Nenhum golpe de rotina dispara nenhum dos dois** — precisa de área grande ou de Expansão de Domínio, *que são exatamente as coisas que na obra destroem shikigami de vez.* **A régua dispara onde a ficção dispara, e ninguém escreveu isso à mão.**

### Achado — o que a Trilha concede não sai do orçamento

*Achado montando os shikigami do material contra o catálogo.* O Coelho de Fuga é *"muitos corpos"*, e muitos corpos custariam 3 pontos — **impossível no nível 2, que é onde a Trilha é escolhida.**

> **`Servo` dá um corpo forte, `Matilha` dá os cinco, `Coro` dá a exceção de economia de ação. O orçamento compra `Traço` e `Comando` por cima disso.**

**Isso resolve o nível 2 e dá à Q6 a única coisa que ela ainda não tinha** — o que cada Trilha concede que o orçamento não pode comprar. *A pergunta que esperava a peça de Trilhas ganhou metade da resposta aqui.*

### Registrado — a triagem matou quatro nomes antes de qualquer um ser escrito

`Passiva` (peça do Fundamento), `Natureza` (perícia), `Forma` (Feitiço pronto **e** peça do Fundamento), `Molde` (Tema), `Instinto` (Passiva **e** Tema), `Enxame` e `Sombra` (Temas) saem **OCUPADO**; `Toca` sai dentro de *"Toca a Alma"* e `Golpe` dentro de *"Golpe canalizado"*. **`Traço` e `Comando` saíram LIVRE** — e `Comando` é a mesma palavra da regra da Q4, o que é o oposto do defeito da lição nº 6.

### Corrigido — cinco erros meus, todos da mesma família, e três revisões céticas

**Cinco vezes escrevi um resumo em prosa por cima de uma tabela que o script já tinha impresso certo**, e as cinco divergiam: `3,0×` onde era 2,5×, `+7% a +23%` onde era +15% a +46%, `1,4 a 2,1 rodadas` onde era 1,2 a 1,7, `1,1 a 2,5 vezes` onde era 1,5 a 2,0, e `30% a 50%` onde era 30% a 40%. **Cinco do mesmo tipo é padrão, não descuido** — parei de escrever resumo à mão e passei a ler o número do script.

E três achados de ponteiro, que são a família do *"§9 da peça 5"* que a v0.50 arrancou:

| | |
|---|---|
| a regra de arredondamento citada como texto da **peça 1** | a frase copiada era a do bloco de fórmulas do `ESTADO-ATUAL`; **a peça 1 §5.4 é dona da regra, com outras palavras** |
| *"6% a 9% da Rotina"* atribuído ao `ESTADO-ATUAL` | mora na **peça 14 §4** |
| o próprio conserto | deixou a **forma literal do ponteiro morto** dentro do arquivo — reescrito sem ela |

**E uma leitura errada de meia frase**, corrigida quando a Q4 chegou: eu tinha afirmado que *"pool compartilhado de ações morre por texto"*, citando a peça 6 §3.1. **A frase inteira diz o contrário** — *"as ações se redistribuem"* é exatamente pool compartilhado, e é o que a Q4 escolheu.

**Uma correção de conclusão, no meio da Q4:** eu escrevi que *"o mestre que foca a invocação está jogando certo"*. A conta de troca diz que não — derrubar o pool custa **2,5 Rotinas** ao inimigo e nega **1 rodada** ao jogador, e o dano que foi na invocação é dano que não foi num PJ. **O defeito de multi-mestre não é "o mestre esperto cobra mais", é "o mestre inexperiente cobra mais, e ele não sabe".**

**E um checker meu que acusou o que estava certo:** a varredura de ponteiros de seção capturava `4.` com o ponto e comparava contra `4`, marcando **cinco referências boas como inexistentes**. *Foi por pouco que eu não "consertei" as cinco.*

### Registrado — o levantamento externo

**PF2e Summoner** (*"you can use any of your actions for yourself or your eidolon"*, `Act Together`, pool de vida compartilhado), **PF2e companheiro animal** (trait `minion`, *"gains 2 actions during your turn"*, e a fórmula de vida *"ancestry Hit Points from its type, plus 6 plus its Constitution modifier for each level you have"* — **que é a fórmula da peça 1 com outro rótulo**), **PF2e troop** (*"instead of standard Strikes"*, segmentos perdidos em terços), **PF1e Summoner** (evolution pool de 3 a 26 pontos, evoluções de 1 a 4 — a âncora de formato do catálogo), **5e 2014 `conjure animals`** (*"roll initiative for the summoned creatures as a group"*), **5e 2024 `Summon Beast`** (*"shares your Initiative count, but takes its turn immediately after yours"*, `AC 11 + the spell's level`, *"attack bonus equals your spell attack modifier"*), **5e 2024 `conjure animals`** (virou emanação, zero corpos), **5e 2024 Beast Master** e **13th Age mooks** (um mob, um número de iniciativa; um quinto da vida).

### Em aberto

- **O catálogo de `Traço` e `Comando` escrito entrada por entrada**, no molde da peça 11 — e a triagem em cada nome novo.
- **Rika e Mahoraga**, que agem fora do controle do portador e não são ponto de orçamento.
- **Reconseguir a invocação morta** — talismã, corpo, maldição domada. É tempo de campanha, e é da peça de Trilhas ou da passada de material.
- **O validador dono da peça**, com as treze checagens que o §5 do rascunho lista. *Sem escrever o nome do arquivo: o `conferir-repositorio.py` acusa referência morta, e acusou esta mesma linha ao fechar a versão — a checagem funcionando na direção certa.*
- **A Q6**, que é da peça de Trilhas e já tem metade da resposta.
- As mesmas de sempre: as vagas de Desliga, a Cicatriz, Energia Reversa, o clash, o nome do sistema.

---

## [0.50] — 2026-08-13

**A fila foi reordenada, e nenhuma regra mudou.** Sessão de planejamento: as duas peças que a v0.49 destampou — `ferramenta amaldiçoada` e `objeto amaldiçoado` — ganharam posição, e Invocações ganhou o rascunho dela. Continuam **catorze peças e catorze validadores**.

### Decidido — a fila, e três das quatro posições saíram da conta

*Decisão do Mizuki: "Invocações agora, ferramenta entre ela e a Trilha."*

| # | peça | por que aqui |
|---|---|---|
| 1 | **Invocações** | dependência dura de Trilhas: `Servo`, `Matilha` e `Coro` **são** o sistema de invocação visto de dentro |
| 2 | **Ferramenta amaldiçoada** | destrava `Técnica Marcial`, que é o que leva as rotas de Origem de **6/9 para 8/9** |
| 3 | **Trilhas** | fecha com as quinze escrevíveis de uma vez, em vez de doze mais três pendentes |
| 4 | **Objeto amaldiçoado** | por último, e é o que a conta impôs |

**Só a posição 3 contra 2 era escolha; as outras três a conta fechou sozinha.**

> **Objeto amaldiçoado destrava zero ficha, e isso é o contrário do que a v0.49 fazia parecer.** Ele foi o achado brilhante daquela versão — termo cobrindo dois conceitos, duas Origens construídas em cima dele, nenhuma peça dona. **Mas Receptáculo e Reencarnado já rodam hoje**, os dois vão para o Fundamento. Ele fecha **1 das 7 vagas de Desliga** e mais nada.
>
> *Buraco de vocabulário real não é o mesmo que buraco que trava alguém — e o brilho do achado empurra para tratar os dois igual.*

**E ferramenta vem antes de Técnica Marcial por texto já escrito, não por gosto.** A peça 5 §3 diz que a Maki *"só compete porque a **ferramenta amaldiçoada carrega a energia por ela**"*. Escrever Técnica Marcial antes produz uma rota que não consegue ferir maldição, que é o jogo inteiro.

### Achado — "peça 5 §9" não existe, e três documentos apontavam para lá

*Achado na revisão cética desta versão, indo ler a seção antes de citá-la.* **A peça 5 tem cinco seções.** Não existe §9, e nunca existiu.

| quem citava | o que queria dizer | onde a coisa mora |
|---|---|---|
| peça 13, a vaga da Restrição Celestial | *"ferramenta é o único jeito de ferir maldição"* | **§3, Canalizar Energia** |
| peça 14 §8 item 2 | *"a pendência nomeada"* | **§5, Em aberto** |
| `ESTADO-ATUAL`, a definição de ferramenta | *"prometida desde"* | **§5, Em aberto** |

> **Não é um número errado repetido três vezes: as duas coisas citadas como §9 estão em seções diferentes uma da outra.** O argumento da Maki está no §3, junto da frase que explica por que um feiticeiro fere maldição e uma pessoa comum não; a pendência de preço está no §5. **Quem fosse conferir a promessa não acharia nem uma nem outra.**

**E o motivo de ninguém ter pego é estrutural:** o `conferir-repositorio.py` confere referência **de arquivo** — foi ele que pegou, nesta mesma versão, o `15-invocacoes.md` que eu tinha citado no rascunho e que não existe. **Referência de seção passa por baixo dele.** *Lição nº 9 numa camada mais fina que a de sempre: não é um número com dois donos, é um ponteiro para dentro de um documento que nenhuma checagem resolve.*

As três foram corrigidas. A citação dentro da entrada da v0.49, logo abaixo, **fica como está** — entrada de CHANGELOG é registro do que se pensou naquele dia, e reescrever histórico para esconder erro é o contrário do que este arquivo existe para fazer.

### Adicionado — o `RASCUNHO-invocacoes.md`, e ele achou um buraco na peça 6

Levantamento engatilhado, sem número no nome. **Passam a ser três rascunhos** — com o `RASCUNHO-bloqueio.md` e o `RASCUNHO-clash-de-expansoes.md` —, e o `README` foi corrigido, porque ele contava dois pelo nome.

**O achado é do levantamento externo, e ele é de um eixo que a peça 6 não mede.** O `conjure animals` do 5e 2014 é o modo de falha mais documentado do hobby, e ele tem **duas metades**:

| metade | a peça 6 §4 cobre? |
|---|---|
| dano e economia de ação — oito lobos | **sim.** *"Você e todas as suas invocações somados entregam uma Rotina"* |
| **tempo de mesa** — o combate para, e os outros esperam | **não** |

**O 5e 2024 trocou a família inteira por causa da segunda metade**, e o motivo publicado é operacional: ficha de monstro para abrir, miniatura para ter, combate travando. A saída deles foi uma criatura só, que não se divide e **age na iniciativa do dono**. O 13th Age resolve por outro lado — dano contra o bando inteiro, mook com um quinto da vida.

> **A `Matilha` é exatamente a montagem que os dois tiveram que construir máquina especial para segurar** — *"um quinto da Rotina em cada, cinco corpos no campo"*. **Cinco fichas agindo por rodada custam o mesmo tempo de mesa quer cada uma faça 25 de dano ou 5.**
>
> E o eixo **já existe no projeto**: a lista de playtest pergunta *"alguém usa ação bônus?"* com a justificativa *"é a peça mais herdada do turno e a que mais custa tempo de mesa"*. Ninguém tinha apontado ele para cá. *Um preço se mede somado — e tempo de mesa é a parcela que nenhuma conta de dano enxerga.*

### Registrado — o Fundamento não produz invocação, e a suspeita óbvia caiu

*Conferido no `.docx` da v7.8 antes de propor qualquer coisa.* A hipótese era que uma técnica com Regra de invocar já produzisse invocação pelo orçamento do Fundamento — o que seria a lição nº 2, o mesmo poder contado duas vezes.

**Não procede.** `Invocação` aparece **só como Tema**, no grupo *Criação* do catálogo do apêndice, e Tema não tem efeito mecânico. Não existe Forma nem Melhoria que ponha um corpo que age no campo. **Não há duas portas.**

### Registrado — o nome da peça está ocupado, e o `arquitetura.md` nunca soube dela

A triagem: `Invocação`, `Invocacao` e `Vínculo` saem **OCUPADO** (Temas do manual); `Servo`, `Matilha` e `Coro` saem OCUPADO por já serem Trilhas. Livres: `Coleira`, `Convocação`.

**Não é impeditivo — Tema não carrega mecânica —, mas tem de ser decisão escrita e não descuido.** *E de quebra: `invocação` tem **zero ocorrências** no `arquitetura.md`. O documento que é o mapa da ordem de construção nunca mencionou o subsistema, do mesmo jeito que não mencionava `objeto amaldiçoado`.*

### Em aberto

As mesmas da v0.49, menos a posição das duas peças novas. Nenhuma vaga de Desliga foi tocada, nenhum número mudou.

---

## [0.49] — 2026-08-13

**A dívida que a peça 13 devia a Equipamento foi cobrar, e não havia o que cobrar.** As quatro vagas de Desliga que esperavam aquela peça **nomeavam a peça errada, cada uma por um motivo diferente** — e o achado que desfaz três delas veio de uma pergunta do Mizuki sobre canon. Nenhuma vaga foi preenchida, e isso é a decisão. Continuam **catorze peças e catorze validadores**.

### Achado — Equipamento fechou e nenhuma das quatro vagas abriu

*A peça 13 fecha dizendo "quando equipamento fechar, a primeira coisa a fazer é voltar aqui". Voltamos, e a porta estava fechada por dentro.*

| vaga | dizia esperar | espera de verdade |
|---|---|---|
| **Descendente** | equipamento | **ferramenta amaldiçoada** — a peça 14 §8 item 2 declinou o assunto **por decisão** |
| **Restrição Celestial** | equipamento | **ferramenta amaldiçoada** — é a Origem que mais depende dela |
| **Reencarnado** | equipamento | **objeto amaldiçoado** |
| **Corpo Amaldiçoado** | equipamento | **Técnica Marcial** |

**O erro do Corpo Amaldiçoado é o mais instrutivo dos quatro: é dependência de segunda mão.** Técnica Marcial *estava* bloqueada por equipamento, e a vaga **nomeou o bloqueio em vez do dono**. Quando a peça 14 fechou, a vaga parecia destravada e não estava — o que ela esperava continuava sem existir.

> **A regra 1 do §"vaga declarada" tem um modo de falha que só apareceu com a primeira peça pronta na mão.** Ela manda a vaga *nomear a peça de onde o alvo deve sair*, e não manda conferir se a peça nomeada é mesmo a dona. **Uma dívida que nomeia a peça errada é pior que uma dívida sem nome: a sem nome ninguém dá por fechada, e a com nome errado fecha sozinha no dia em que a peça errada fecha.** O conserto está escrito na peça 13: *a vaga nomeia a peça dona do alvo, não a que estava na frente dela na fila.*

### Achado — o projeto usava um nome para duas coisas que o canon separa

*Pergunta do Mizuki, e ela derrubou metade da minha proposta:* **"por que o Corpo Amaldiçoado precisa de ferramenta amaldiçoada exatamente? Acredito que são mais como itens amaldiçoados, não necessitando exatamente ser armas — diferente do restringido, que realmente precisa."**

| | o que é | quem depende dela aqui |
|---|---|---|
| **ferramenta amaldiçoada** (呪具) | **arma forjada** para canalizar energia, com graus. Até quem não é feiticeiro usa | `Armaria` do Descendente · Restrição Celestial |
| **objeto amaldiçoado** (呪物) | **não é item imbuído: é a própria maldição presa em forma de objeto.** Resto de feiticeiro antigo, que encarna num receptáculo compatível | Receptáculo · Reencarnado |

**A diferença é de intenção:** a ferramenta é *feita para* canalizar; o objeto **é** a coisa. *E o `Enterrado` do Reencarnado foi a pista falsa que segurou o erro:* ele diz *"você guardou uma coisa antes de morrer"* — **e uma coisa não é necessariamente uma arma.**

**A peça 9 já escrevia a dependência certa e ninguém tinha ligado os pontos:** o Kashimo *"aceitou virar **objeto amaldiçoado** e encarnar num corpo que o Kenjaku preparou"*.

### Achado — `objeto amaldiçoado` não tem peça dona em lugar nenhum

**Duas Origens inteiras são construídas em cima dele** — Receptáculo é comer um dedo, Reencarnado é *ter virado* um — e ele **não estava na fila, não estava no `arquitetura.md` e não tinha vaga na ordem de construção.** Ele estava escondido dentro da palavra *"ferramenta"*, que tem peça prometida.

*Entrou na lista de peças que faltam, no `ESTADO-ATUAL`.* **É a lição nº 6 numa forma nova:** não é o preço que usa um termo inexistente — é o termo existente **cobrindo dois conceitos**, e um deles não tendo dono.

### Decidido — nenhuma vaga é preenchida, e o motivo é a régua funcionando

*Passados pela trava do Desliga todos os nomes que a peça 14 criou:*

| alvo candidato | quem paga por ele | veredito |
|---|---|---|
| **requisito de Força** | ninguém — é gate, não item | **legal** |
| treino de arma | a Trilha | proibido |
| teto de Destreza do uniforme | vem junto da proteção, um orçamento só | proibido |
| `Volumosa` · `Embainhada` | devolvem 1 ponto ao orçamento | proibido |
| qualquer propriedade de arma | custa 1 ponto | proibido |
| uniforme desliga cobrir-se | apagar dá Defesa 23 | o `conferir-equipamento.py` barra |

> **Equipamento produziu UM alvo legal, e ele não vale a entrada.** O requisito de Força vale `1,0` de dado — um Força 0 sai de `d10` para `d12` — e vale **zero** para quem já tem Força 3, que é o perfil das duas Origens que poderiam pegá-lo.
>
> **A trava do Desliga proíbe encostar no que tem preço, e a peça 14 precificou quase tudo que nomeou.** *A régua funcionando exatamente como desenhada, numa direção que ninguém previu: peça nova cria alvo novo, mas **peça bem precificada cria pouquíssimo**.* Preencher assim mesmo seria escrever entrada para fechar contagem, que é o defeito que essa régua nasceu para achar.

### Adicionado — as duas definições, com dono declarado

*Pedido do Mizuki: "se quiser abordar ferramenta amaldiçoada ou item amaldiçoado no documento, só colocar uma descrição simples do que é."*

**As duas são vocabulário que ainda não tem peça, então a definição mora no `ESTADO-ATUAL`, na lista do que não existe — e isso está escrito lá como provisório.** Quando cada peça for escrita, a definição vai para ela e a linha vira ponteiro. A peça 13 e a peça 14 citam as duas e **apontam** em vez de repetir. *Lição nº 9 obedecida em vez de explicada: duas descrições soltas em quatro peças é como o "ferramenta amaldiçoada" cobrindo dois conceitos começou.*

### Alterado — duas referências mortas dentro das próprias peças

*Achadas varrendo depois de reclassificar, e são o próprio defeito que esta versão documentou.* A peça 13 fechava dizendo *"quatro esperam equipamento, três esperam dano e condições"*, e o §8 item 3 da peça 14 listava as quatro pelo nome. **As duas sobreviveram à reclassificação por estarem longe da tabela que mudou** — e nenhum validador cruza prosa com tabela.

### Em aberto

- **`Objeto amaldiçoado`** — peça nova, sem posição na fila ainda.
- **`Ferramenta amaldiçoada`** — tópico próprio, com graus e forja, prometido desde a peça 5 §9.
- **Técnica Marcial**, destravada na v0.48 e agora com uma vaga de Desliga nomeando ela.
- **As três vagas de dano e condições**, e a Cicatriz, que espera a mesma peça.
- **Os nomes dos degraus de escudo**, as descrições das 52 armas, a penalidade, o barulho na categoria.
- **As três checagens do Bloquear**, no `conferir-atributos.py`.
- **Energia Reversa, o clash, o nome do sistema.**

---

## [0.48] — 2026-08-13

**Equipamento fechou. São catorze peças e catorze validadores.** O `RASCUNHO-equipamento.md` virou `14-equipamento.md` e ganhou o `conferir-equipamento.py`, com dez checagens e dez perturbações conferidas. **E o que destravou a peça não foi escrever o validador: foi derrubar a frase que dizia que ele não podia ser escrito.**

### Achado — o bloqueio do validador era uma conclusão que sobreviveu à premissa

O §5.2 fechava com *"o item 9 do §8 não pode ser escrito antes disto: um validador de dominância por valor total precisa de valor, e sete oitavos do catálogo ainda não têm"*. **A premissa morreu na v0.45**, quando as 52 armas ganharam dado e propriedades; a conclusão sobreviveu **três versões**.

> **Não é a lição nº 9 na forma de sempre.** Não foi uma cópia que divergiu do dono — foi um documento discordando de si mesmo no tempo. A subseção inteira media **classes**, e a classe morreu como preço na v0.44: ela ainda rodava uma matriz de `1 DOMINADA / 15 INCONCLUSIVO` sobre oito classes que não existem, afirmava *"sete das oito propriedades não têm texto"* (são doze, todas têm) e citava um `0,60` que o próprio §8 daquele documento já tinha corrigido para `0,33` na v0.42.

**Refeita, a matriz roda:** 1640 pares no corpo a corpo, 110 no tiro, com o critério certo — *mesma mão, mesmo atributo, dado maior ou igual, propriedades em superconjunto, restrições em subconjunto.*

### Achado — três dominâncias no corpo a corpo, e as três são a mesma

`Espada Longa` passa **Machete** e **Machado**; `Taco` passa **Wakizashi**. **As três são `Versátil` a custo zero** — a dominância que a v0.41 achou entre *classes* e a v0.44 fechou na camada da classe, e que **ninguém conferiu ter descido para a camada da arma.**

Ficam `ACEITA`, com o tamanho que a v0.44 já tinha medido: `0,1` ponto e só no nível 2. **Mas o tamanho não é o achado.** `Versátil` a zero não é barata, é **não precificada**: das 28 armas de uma mão, 4 levam e 24 recusam, e **17 das que recusam têm o mesmo dado de uma que leva.** O orçamento não impede nenhuma; quem impede é a ficção.

> **Decisão do Mizuki, e ela resolve os dois lados:** *"dá pra fazer uma descrição para cada arma, colocando em negrito as propriedades no texto e explicando de forma narrativa."* **A condição de ficção deixa de ser tácita porque vira texto da arma** — e escrever as 52 agora é desperdício, então fica declarado no §5.3 para a passada de material. **Até lá o validador acusa**, que é a metade de graça: as quatro com `Versátil` são lista declarada e uma quinta falha.

### Achado — o fundo da v0.45 nunca chegou nas armas de tiro

*Achado rodando a matriz sobre o tiro logo depois de consertar o `Yumi` — que era o primeiro sintoma disto e não um caso isolado.* **7 das 11 com vaga vazia, e 7 dominâncias estritas.** O `Rifle` sozinho dominava `Besta`, `Espingarda` e `Submetralhadora`.

**E a causa não era desleixo — era falta de resolução na régua:**

| dado | média | gasto pela fórmula do §5.2 |
|---|---|---|
| `1d10` | 5,5 | **0 — grampeado no piso** |
| `2d6` | 7,0 | **0 — grampeado no piso** |
| `2d8` | 9,0 | 0,5 |
| `2d10` | 11,0 | 2,5 |

**A régua não distinguia uma pistola de uma submetralhadora**, e os gastos fracionários faziam propriedade inteira nunca fechar o orçamento exato. *Não é que ninguém preencheu as vagas: é que não havia como preenchê-las por soma.*

**O conserto é o precedente do §5.0.3, um eixo ao lado** — lá está escrito que *"`Duas mãos` não é item de orçamento: é **categoria** de orçamento, com número próprio"*. **O degrau da escada do tiro virou a unidade:** `1d10 · 2d6 · 2d8 · 2d10` = `0 · 1 · 2 · 3`, fundo `2/4`. As sete vagas foram preenchidas com propriedade que já existia — `Oculta` na Besta de Uma Mão, `Rompe` na Besta, Espingarda e Metralhadora, `Talha` no Rifle, `Par`+`Oculta` na Submetralhadora — e **as 7 dominâncias caíram por construção**, não por exceção escrita.

### Decidido — a régua do Mizuki não decide só a fonte do dano, decide o preço

> **A arma que exige alguma coisa do corpo de quem a segura soma atributo. A arma em que você só precisa mirar, não.**

*Decisão dele, e ela **deriva** a tabela do §5.1 em vez de listá-la* — um arco se puxa, um kunai se arremessa, uma besta já está tensionada. **A régua também diz o que fazer com a arma número 53, que a lista não dizia.**

**E ela cobrou o preço na hora de ser escrita:** as duas do `Yumi` **estouravam o orçamento**, porque a escada do tiro foi construída só para armas que não somam nada e desconta `6,0` de atributo de todas. Com o desconto indevido, o `Daikyū 2d8` fazia **15,0** contra os 12,5 de um Força 6 com espadão. **`1d10` fecha exato** e põe o arco em 11,5, que é onde a rota de Destreza já está com a Katana.

*A saída bonita foi testada e reprovada:* dar `Volumosa` ao Daikyū deixaria `1d12` fechar, e `1d12 + Destreza 6 = 12,5` **empata com a Pesada, à distância** — a mesma sentença que o §5.0.1 escreveu contra a `Fineza` no d12. **Empatar de longe é pior que empatar de perto.**

### Decidido — `Silenciosa` foi levantada e o manual já tinha a resposta

*Ideia do Mizuki:* **"uma propriedade que não tira o personagem de furtividade, exigindo um teste novo com penalidade."** A máquina está certa — é a **camada 1 do §6**, a mesma da `Oculta`, um momento adiante. **Não entra, e são quatro motivos independentes:**

| | |
|---|---|
| o nome está ocupado, e não por substring | **`Silencioso` é Melhoria no manual:** *"Sem gesto, sem palavra. Ninguém percebe que você conjurou."* Mesmo efeito, mesmo nome |
| a regra da qual ela isentaria não existe | zero ocorrências de barulho quebrando furtividade nas peças. **É a Passiva Casca de novo** |
| o eixo está errado | pelo §5.0.2, *"propriedade é o que a arma é"* — então toda arma **sem** ela faz barulho, e um tantō passa a ser mais barulhento que um arco longo |
| e os arcos não precisavam | o buraco era da proposta, não do catálogo |

**O quarto é erro meu e fica registrado:** eu movi o `Yumi` para o fundo `5` do corpo a corpo por ele somar atributo. **A régua do §5.1.2 decide quem soma atributo; o §5.0.5 decide qual escada precifica. São perguntas diferentes.** No fundo `2/4` os dois arcos fecham exatos.

> **A metade que sobrevive é uma linha em vez de uma propriedade:** quem revela é a **`Arma de Fogo`**, e categoria é onde este projeto põe *"o que a coisa é"*. Fica no §8 item 19, esperando a peça que tiver furtividade.

### Alterado — o `Yumi` não carrega `Munição`

*Achado do Mizuki:* **"munição elas precisam, mas não precisam recarregar."** A inconsistência já estava no documento: as duas carregavam `Munição` no §5.3 e **nunca receberam X no §5.2** — meia propriedade desde a v0.45. **`Munição` aqui não é *ter munição*: é o ciclo de recarga**, e uma flecha se encaixa como parte do disparo. Sair é de graça, porque ela custa zero.

### Achado — o requisito de Força nunca pega arma de Destreza

*Achado quando o dado do Daikyū desceu dentro desta mesma versão.* O §5.5 contava `6 das 11` no tiro e nomeava *"arco longo"* — verdade enquanto ele era `2d8`, **falso desde que virou `1d10`, três parágrafos antes no mesmo documento.**

**E o conserto mostrou que a régua é mais estreita do que ela dizia:** as oito com `Fineza` param em `d8`, e as duas do `Yumi` ficam no fundo da escada do tiro. **O requisito gateia exatamente quem não depende de Destreza** — o corpo a corpo que soma Força e o tiro que não soma nada. *Ninguém impôs isso em lugar nenhum: caiu do orçamento nas três famílias.* São **dezesseis de 52**, não dezessete.

### Adicionado — o `conferir-equipamento.py`

Dez checagens: **orçamento** (toda arma gasta o fundo exato), **dominância** (a matriz por escada, contra a lista declarada), **propriedade** (toda em uso tem texto), **Força** (o gate é os dois degraus de cima de cada escada e nunca pega Destreza), **teto** (derivado dos três donos, com busca exaustiva de 196 montagens), **baldes**, **Talha**, **Versátil**, **desligamento** e **triagem**.

**Dez perturbações, todas acendendo a checagem certa** — e a nona não acendeu na primeira tentativa porque o `sed` não bateu, o que o arnês pegou antes de eu ler o resultado como "não acendeu". **Dois contra-testes:** uma perturbação produz **um** erro, provando que as checagens não estão acopladas; e perturbar o **teto de atributo na peça 2** faz o teto derivado andar de 20 para 19 e a busca exaustiva acusar — **a checagem 5 não se mede contra a própria constante**, que é a lição nº 8 provada em vez de afirmada.

### Achado — o validador achou duas coisas na primeira rodada limpa

**`Maça` e `Kanabō` dependem só da `Talha`**, e o §5.2 afirmava *"hoje nenhuma fica: as sete que a carregam levam outra propriedade ou um dado que já as separa"* — **são oito, e duas ficam.** A dívida escrita na v0.45 mandava o validador acusar exatamente isso, e ele acusou. *Decisão do Mizuki: as duas ficam declaradas* — a maça e o kanabō **são** as armas anti-guarda, então `Talha` nelas é identidade e não enfeite. **Uma terceira falha.**

**E a tabela do §5.3 escrevia os nomes sem acento** enquanto a prosa escrevia com — `Espadao` contra `Espadão`, `Maca` contra `Maça`. O `conferir-nomes.py` compara literal, então **uma colisão nesses dez nomes passaria batido**. Normalizado, e o validador agora falha se as duas grafias divergirem de novo. *De quebra, isso quebrou o meu próprio validador, que tinha `Versatil` e `Municao` escritos sem acento na mão — consertado comparando sem acento em vez de por grafia.*

### Alterado — as duas dívidas de aplicação nas peças 5 e 6

**Peça 6 §8** nomeava as quatro categorias de treino e não dizia quais armas caem em qual balde; **peça 5 §1** prometia o requisito de Força sem apontar onde ele mora. *As duas decisões existiam desde a v0.47 e nenhuma das duas peças tinha sido tocada* — que é o padrão que custou sete versões na Trilha.

E ao escrever a peça 5 apareceu um contra-teste que aquela frase nunca tinha tido: *"quem luta com Destreza fica nas armas leves"* **se cumpriu sozinha**, porque `Fineza` custa um ponto e o que sobra não paga dado grande. **A promessa e a régua chegaram no mesmo lugar por caminhos diferentes.**

### Em aberto

- **As quatro vagas de Desliga da peça 13**, que esperam desde a v0.39 — e agora nada as bloqueia. *A peça 13 fecha dizendo "quando equipamento fechar, a primeira coisa a fazer é voltar aqui".*
- **Os nomes dos três degraus de escudo**, e quantos são.
- **As descrições das 52 armas**, adiadas por decisão para a passada de material.
- **A penalidade** por empunhar sem treino ou sem requisito — espera dano e condições.
- **O barulho na `Arma de Fogo`** — espera furtividade.
- **A `Comprida` continua sem dono**, e a lista de itens comuns e a moeda continuam abertas.
- **As três checagens do Bloquear**, no `conferir-atributos.py`.
- **A lista de pastas ignoradas mora em dois lugares.** *Achado ao fechar esta versão:* o `conferir-repositorio.py` varria `_to_delete/`, que o `.gitignore` exclui desde que a pasta existe — e uma referência morta lá dentro derrubou o validador por um arquivo que já estava marcado para sumir. Corrigido, **mas o conserto é uma segunda cópia**: as duas listas ainda divergem em `.venv` e `node_modules`. *Lição nº 9 numa camada que nenhum validador olha, porque o validador é ela mesma.*
- **A Cicatriz, Energia Reversa, o clash, o nome do sistema.**

---

## [0.47] — 2026-08-13

**As duas decisões de acesso de Equipamento fecharam, e uma afirmação da v0.45 caiu junto.** A divisão simples/marcial e o requisito de Força — as duas registradas como *"em aberto"* desde a v0.45, as duas resolvendo acesso por eixos diferentes. Continuam **treze peças e treze validadores**; Equipamento continua em rascunho. E a passada achou um estouro de orçamento em duas armas que ninguém tinha medido.

### Achado — "punir é impossível por construção" era propriedade do corte de teste, não da régua

A v0.45 fechou a decisão do treino de arma com uma tabela mostrando os dois baldes chegando ao mesmo teto, e escreveu que **sob a régua com fundo, punir é impossível por construção.** *Rodando a régua sobre todos os cortes em vez de sobre um:*

| | |
|---|---|
| onde mora o `d8` de uma mão | `Lâmina Longa` · `Massa` · `Machado` |
| onde mora o `d12` de duas mãos | **as mesmas três** |

**Qualquer corte que ponha as três no balde marcial deixa o simples `1,0` dado atrás — nas duas economias de mão.** O teste da v0.45 empatava porque tinha `Massa` dentro, e ninguém tinha perguntado se o empate vinha da régua ou do exemplo. *É a lição nº 8 numa forma nova: a checagem não se mediu contra a própria constante, ela se mediu contra um único caso e generalizou.*

### Achado — os dois gates se multiplicam, e nenhum dos dois faz isso sozinho

Sob o requisito de Força, sobram **duas** armas de duas mãos sem requisito no catálogo inteiro: **Kusarigama** (`Ceifa`) e **Corrente** (`Flexível`).

> **Se nenhuma das duas categorias cair no balde simples, o Caminho não-marcial de Força baixa fica com ZERO arma de duas mãos.** O gate de treino sozinho não faz isso; o gate de Força sozinho não faz isso. **Só a interseção faz** — e ela é a ficha do Emanador que quer lutar, que é exatamente quem as duas decisões existem para atender.

*Lição nº 7 num eixo novo: um preço se mede somado, e aqui o que precisava ser somado eram duas restrições em vez de dois custos.*

### Decidido — a divisão simples/marcial

Busca exaustiva dos **1024** cortes das dez categorias de corpo a corpo. **543 passam** nas quatro travas — as duas acima, mais *"cada balde tem arma de uma e de duas mãos"* e *"nenhum balde com menos de 3 categorias"*. Trava demais para decidir sozinha; o que fecha é a âncora de ficção, lida da tabela oficial do 5e 2024 e não de memória.

| | categorias |
|---|---|
| vão para simples sem ambiguidade | `Lâmina Curta` (dagger) · `Porrete` (club, quarterstaff) · `Ceifa` (sickle) · `Arremesso` (dart, javelin) |
| para marcial sem ambiguidade | `Lâmina Longa` (longsword, rapier, greatsword) · `Flexível` (whip) |
| **o 5e corta por dentro** | `Massa` · `Machado` · `Armas Longas` |
| **o 5e não tem** | `Manopla` |

> **A `Manopla` não tem âncora no 5e, e a do PF2e é melhor do que a que faltou.** *Conferido no levantamento, não suposto:* o **gauntlet é arma simples** lá, do grupo `Brawling`, com o traço **`free-hand`** — que é literalmente o texto de regra por trás da `Vestida` deste projeto, já registrado no levantamento da v0.45. **A mesma fonte sustenta a propriedade e o balde.**

**As três que ele corta por dentro são justamente onde mora o teto**, então a trava 2 escolhe entre `Massa` e `Machado` — e o desempate é específico: **o greatclub é arma simples no 5e, e um kanabō é um greatclub**; battleaxe e greataxe são marciais, e o Machado de Guerra é um dos dois. **`Massa` entra.** *E ela ainda deixa o simples com **6** armas de duas mãos contra **4** da rota do `Machado` — medido com o mesmo resto de balde nos dois lados, que é o único jeito de a comparação querer dizer alguma coisa.*

`Armas Longas` fica no marcial por decisão de documento e não de número — a conta é indiferente, porque Naginata e Yari já caem no requisito de Força. **O `ESTADO-ATUAL` diz que a árvore da Vanguarda é *"alcance, reposicionamento forçado, troca de alvo"*, então o alcance bom é o que o treino destrava.** O balde simples não fica sem: Bastão, Bō e Kusarigama carregam `Alcance`.

> **Simples — 24 armas, 6 categorias:** `Lâmina Curta` · `Porrete` · `Ceifa` · `Arremesso` · `Manopla` · `Massa`
> **Marciais — 17, 4 categorias:** `Lâmina Longa` · `Machado` · `Armas Longas` · `Flexível`

**As de projétil.** `Arma de Fogo` é a terceira categoria de treino, sozinha, e ferramenta amaldiçoada fica fora da peça. O 5e corta por dentro de `Yumi` e `Balestra` — arco curto e besta leve simples, arco longo e besta pesada marciais —, e isso não é importável porque aqui a divisão mora na categoria. **`Balestra` é simples e `Yumi` é marcial**, por âncora histórica: a besta mudou a guerra medieval justamente **por não exigir treino**, e o arco japonês é disciplina de anos.

**A repartição de propriedade sai assimétrica de propósito:** o marcial leva o alcance (8 armas contra 3), o simples leva a ocultação, e `Par` e `Vestida` não existem do lado marcial. **A divisão restringe qual identidade, nunca quanto poder** — os dois tetos empatam em `d8` e `d12`.

### Decidido — o requisito de Força reancora no dado, nas duas escadas

*Ele ficou órfão na v0.44, quando a classe saiu do preço, e passou duas versões sem implementação: das 41 armas do §5.3, zero tinham requisito escrito.*

> **`Força 3` para os dois degraus de cima de cada escada.** Corpo a corpo `d10` e `d12` — 11 de 41. Tiro `2d8` e `2d10` — 6 de 11. **Dezessete de 52, com zero parâmetro novo:** é a mesma frase aplicada às duas escadas que o §5.2 já tinha.

**O corte de ficção sai sozinho da régua.** Escapam Hankyū, Submetralhadora, Pistola, Revólver e Besta de Uma Mão — as cinco leves. Pegam arco longo, besta, espingarda, rifle, rifle de precisão e metralhadora pesada. Ninguém escreveu essa lista à mão.

**O tiro entrou por decisão do Mizuki — *"tem arma de longo alcance que vai necessitar de força pra carregar"*— e a conta achou um segundo motivo, maior:**

| ficha | melhor arma sem o requisito | com ele |
|---|---|---|
| Força 0 · Destreza 0 — o conjurador puro | **Rifle de Precisão, 11,0** | Hankyū, 7,0 |

**Um conjurador que não gastou um ponto de atributo fazia 11,0**, contra 6,5 do melhor corpo a corpo dele — e **o requisito no corpo a corpo sozinho não fecha isso**, porque a arma de fogo passa por fora. É o buraco que o §5.2 nomeou (*"não somar atributo não é penalidade, é independência de atributo"*) e não trancou.

### Registrado — o requisito lê o dado impresso, e o vazamento tem tamanho

> **O passo do `Versátil` não conta.** Sem essa frase o requisito pega a **Katana**, que tem `Fineza` — cobraria Força de quem trocou Força por Destreza.

Com ela, três armas alcançam `d10` sem passar pelo gate: Katana, Espada Longa e Taco. **O vazamento vale 1,0 dado**, e o efeito é que **um gate em `d10`+`d12` e um gate só em `d12` devolvem a mesma arma ótima em toda ficha medida.** Eles não são equivalentes, mas o que os separa não é dano:

| para Força < 3 | gate `d10`+`d12` | gate só `d12` |
|---|---|---|
| armas de duas mãos | **2** | 7 |
| com `Talha` de duas mãos | **0 de 6** | 3 |

**Contagem não é valor**, lição nº 3: o gate maior gateia cinco armas a mais e move zero de dano. O que ele move é o que dá para *ser*. **Decisão do Mizuki: o gate maior**, e a `Talha` sumir das duas mãos para quem não tem Força é o desenho.

### Achado — as duas armas do `Yumi` estouram o orçamento

*Achado aplicando o gate de tiro, e ele não estava na pauta desta versão.* A fórmula de preço do tiro desconta `6,0` — *"a Força que o corpo a corpo soma"* —, desconto que só está certo para arma que **não soma nada**. **As nove de `Balestra` e `Arma de Fogo` reproduzem exatas contra a tabela publicada; o `Yumi` soma Destreza (§5.1) e leva o desconto do mesmo jeito.**

| arma | dado | com Destreza 6 | gasta | orçamento |
|---|---|---|---|---|
| Hankyū | `2d6` | 13,0 | 5,5 | 4 — **estoura 1,5** |
| Daikyū | `2d8` | **15,0** | 7,5 | 4 — **estoura 3,5** |

**O Daikyū passa a `Pesada` em 2,5 de dano** — 15,0 contra os 12,5 de um Força 6 com espadão — e a rota de `Fineza`, que é a comparação certa, faz 10,5. *O §5.3 afirma "zero armas estourando o orçamento": vale para as outras cinquenta.* **Registrado com as duas saídas medidas, não consertado** — mexer no dado do arco é decisão de sabor, e ela vai para o §8 item 16.

### Alterado — duas dívidas de documentação, e as duas eram a lição nº 9

| onde | o que estava | o que é |
|---|---|---|
| `RASCUNHO-equipamento` §5.0.2 | a tabela invertida da v0.44 (`0 propriedades → d8`), com o dado como **saída** | o §5.0.1 já dizia o contrário três seções acima, com o fundo `3/5` |
| `ESTADO-ATUAL`, seção de Equipamento | parada na v0.44: listava *"os treze efeitos de crítico"* e *"o dado e as propriedades das 52 armas"* como o que falta | os treze morreram e as 52 fecharam, **na v0.45** |

**A segunda é a que mordia**, e é a mesma família do achado da v0.44 sobre o `Bloquear`: o `ESTADO-ATUAL` é o ponto de retomada declarado, e ele estava duas versões atrás na única peça em andamento. **Quem retomasse por ele retomaria na régua velha, procurando escrever treze efeitos de crítico que já tinham morrido.** *Nenhum validador alcança prosa.*

### Registrado — dois erros meus, os dois pegos antes de fechar

*Ficam escritos porque o método é o que sobrevive à sessão.*

**O primeiro foi no script, e ele mentia para o lado que confirmava a conclusão.** A primeira versão da conta do gate tirava a arma gateada do bolso **mesmo de quem passa no requisito** — então ela mostrava o gate mordendo um personagem de Força 6, o que é impossível. Consertado, a tabela mudou de forma: o gate morde Força 0 a 2 e mais ninguém, que é o desenho.

**O segundo foi uma comparação com bases diferentes.** Escrevi *"a rota do `Machado` deixa o simples com 1 arma de duas mãos contra 6 da `Massa`"* — e o `1` saiu de um balde que não tinha `Ceifa` dentro, enquanto o `6` saiu de um que tinha. **Com o mesmo resto de balde nos dois lados é 6 contra 4.** A conclusão não muda; o número estava errado por comparar duas coisas diferentes. *É a mesma família do `+113% contra +56%` que a v0.24 corrigiu na Constituição — dois números certos, medidos de bases que não batem.*

### Registrado — o levantamento externo

A **tabela oficial de armas do 5e 2024**, lida inteira em vez de citada de memória: as dez simples de corpo a corpo, as dezoito marciais, e — o que decide as de projétil — **arco curto e besta leve como simples contra arco longo, besta de mão e besta pesada como marciais**. Mais os **grupos de arma do PF2e**, que são o análogo mais próximo da "categoria" daqui e onde a `Manopla` acha âncora (`Brawling`). *O corte do 5e passa por dentro de cinco das treze categorias deste projeto, e é por isso que ele serve de âncora e não de resposta.*

### Em aberto

- **O validador da peça**, com a busca exaustiva, as três rotas de proteção e a triagem de todo nome — incluindo a checagem de que nenhuma arma dependa só da `Talha`, e as duas travas novas do §5.4.1.
- **Os dois dados do `Yumi`** — §8 item 16, com as duas saídas medidas.
- **A penalidade por empunhar sem treino ou sem requisito** — §8 item 15. Hoje os dois gates são proibição, não penalidade.
- **Os nomes dos três degraus de escudo**, e quantos são.
- **A `Comprida` continua sem dono.**
- **As quatro vagas de Desliga da peça 13.**
- **As três checagens do Bloquear**, no `conferir-atributos.py`.
- **A Cicatriz, Energia Reversa, o clash, o nome do sistema.**

---

## [0.46] — 2026-08-13

**Um arquivo morreu, e nenhuma regra mudou.** Passada de estrutura, feita logo depois de a v0.45 fechar. Continuam **treze peças e treze validadores**.

### Removido — o `PROMPT-CHAT-NOVO.md`, e ele era a segunda encarnação da mesma ideia

*Achado do Mizuki, no fim da sessão:* **"acredito que ele nem precisa existir — eu sempre peço um prompt novo quando vou finalizar um chat."** Medido antes de decidir, bloco a bloco:

| | |
|---|---|
| blocos que eram **cópia** de outro documento | **15 de 16 — 94%** |
| bloco que era só dele | **1** — o teste da pasta certa, contra o clone parado na v0.27 |
| cópias que ele criava | **32** — a ordem de leitura em 3 lugares, o quanto cada validador pula em 3, o *"não rode git"* em 2, o *"como eu gosto de trabalhar"* em 3 |

**E ele já tinha cobrado o preço duas vezes.** A **v0.40** registra que ele repetiu o *"4, 2 e 1"* errado junto com o `README`, o `ESTADO-ATUAL` e o `LEIA-ME`. E **nesta versão ele descrevia a v0.44** — mandando ler uma tabela do §5.0.1 que tinha mudado e citando treze efeitos de crítico que já estavam mortos.

> **Nenhum validador o alcançava.** Zero menções no `conferir-repositorio.py`, e nenhum arquivo do repositório apontava para ele. **Folha solta, sem dono e sem trava** — que é a lição nº 9 no formato mais puro que ela já apareceu aqui.

**E o padrão já tinha acontecido, o que é o argumento que fecha.** O `PROMPT-DE-CONTINUIDADE.md`, no mesmo `99-arquivo/`, é a primeira encarnação da ideia — morto na **v0.14** com a nota *"o `ESTADO-ATUAL.md` faz esse trabalho melhor hoje"*. **Este é o segundo, morrendo pelo mesmo motivo trinta versões depois.** O cabeçalho do arquivo arquivado diz isso com todas as letras, para o terceiro não ser escrito.

**O que sobreviveu:** o teste da pasta certa virou a seção **"Retomar em conversa nova"** do `README` — dez segundos de `head` e `grep` que já pouparam meia hora uma vez. **E o hábito que tornou os dois arquivos desnecessários:** pedir um prompt de continuidade no fim de cada conversa, escrito na hora contra o estado real. *Um prompt escrito na hora não tem como envelhecer; um arquivo tem.*

### Em aberto

As mesmas da v0.45 — nenhuma foi tocada aqui.

---

## [0.45] — 2026-08-13

**A régua de preço das armas ganhou fundo, o efeito de crítico morreu, e as 52 armas têm dado e propriedades.** A pergunta *"como dar identidade a cada arma?"* foi respondida por uma metade que já estava escrita no §5 e nunca tinha sido implementada: **a arma dá acesso E RESTRIÇÃO.** Continuam **treze peças e treze validadores**; Equipamento continua em rascunho.

### Achado — a `Versátil` a zero não propagou, e ela derrubou três números da v0.44

*Achado rodando a régua como código antes de encostar em arma.* A `Versátil` passou a custar `0` na v0.44, e **três lugares continuaram contando ela como `1`**:

| onde | dizia | é |
|---|---|---|
| a tabela do §5.0.1 | conta propriedade literal, 1 ponto cada | **15 divergências em 54** combinações legais, e todas as 15 têm `Versátil` dentro |
| o `79` do CHANGELOG, na subseção `Corrigido` | espaço legal de corpo a corpo | **94** — o `79` só reproduz com a `Versátil` a 1 |
| *"cinco das seis classes fecham exatas"* | a regressão do §5.0 | **seis de seis.** Sem exceção nenhuma |

**O terceiro é o que vale mais, porque ele conserta para melhor.** A v0.44 apresentou a régua como *"cinco fecham, e a sexta estoura em 1"*; com o preço que ela mesma decidiu, a `Versátil` fecha em `2/2` e **a regressão não tem exceção.** A régua sempre foi melhor do que o documento dizia que ela era.

*Varridas oito hipóteses de contagem para o `79` — dois preços da `Versátil` × quatro conjuntos de filtro — e mais três conjuntos alternativos de "as seis propriedades". Só uma reproduz, e é a régua velha.* **É o mesmo defeito da v0.44 na terceira porta: decisão registrada não é decisão aplicada.**

### Achado — o efeito de crítico é uma regra que não acontece

*Achado pelo Mizuki, e a conta confirmou com folga:* **"ninguém lembra do efeito de crítico na hora de aplicar."**

| | |
|---|---|
| dispara por rodada, por personagem | 3,0% |
| por combate, na **mesa inteira** de quatro | **0,44** |
| um jogador vê o efeito **da arma dele** a cada | **9 combates = 2,3 missões** |

**Num server de personagem persistente, cada jogador encontra a identidade da própria arma uma vez por arco.** E o custo de lembrar é **29 entradas de tabela por disparo**. Não é falha de memória: é frequência. *Um efeito preso a todo acerto dispara 11× mais.*

### Achado — e a causa embaixo era pior: a régua cobrava identidade em dano

| a arma que a ficção põe no teto de dado | vagas de propriedade, na régua da v0.44 |
|---|---|
| uma mão, **d8** — a espada comum | **0** |
| duas mãos, **d12** — o espadão | **0** |

**A arma mais icônica de cada mão era obrigada a não ter identidade nenhuma.** Ter personalidade *era* descer o dado, e na mesa ninguém desce o dado. O efeito de crítico tinha nascido para contornar isso por fora — resolvia o problema certo pelo lado que não dispara.

### Decidido — a régua inverte: o dado é ENTRADA, o número de vagas é SAÍDA

> **Antes:** a ficção diz as propriedades → o dado cai sozinho.
> **Agora:** a ficção diz **o tamanho da arma** (o dado) → o **número de vagas** cai sozinho.

**O fundo vai para `3` numa mão e `5` em duas, e o teto de dado não se move** — `d8` e `d12` continuam sendo o topo, e `d8 + Força 6 = 10,5` e `d12 + Força 6 = 12,5` são os mesmos números da v0.44. **O fundo comprou propriedade, não dado.** Custa `1,1%` da Rotina no nv6 e `0,3%` no nv30.

Como gastar menos que o orçamento continua sendo dominância estrita, **toda arma passa a ser obrigada a encher as vagas**: identidade deixa de ser opcional e vira construção. E o formato tem sentido de ficção sozinho — **quanto menor a arma, mais coisas ela faz.**

**O `+2` (fundo `4/6`) foi levantado, medido e reprovado pela própria conta:** ele deixa **16 de 16** armas com vaga vazia, e com as cinco propriedades de então ele *reduzia* o espaço de assinaturas de 55 para 51. É aritmética de combinação — com 5 propriedades, 4 vagas dão 5 conjuntos e 2 vagas dão 10.

### Decidido — a restrição devolve orçamento, e a máquina já era da casa

> **Uma arma pode carregar um defeito de verdade e comprar uma propriedade com ele.**

**O §5 sempre disse *"a arma dá acesso e restrição"*, e só o acesso estava implementado.** A máquina de restrição-que-devolve é a do Fundamento — `Leve` devolve `teto(Classe/2)`, `Média` devolve `Classe` —, então ela não é importada: é a régua da casa uma camada abaixo.

Três restrições, cada uma devolvendo **1 ponto**: **`Volumosa`** (não esconde e atrapalha em espaço apertado) · **`Embainhada`** (não se saca sozinha) · **`Comprida`** (perde no corpo a corpo colado).

**Não virou resposta padrão: 3 de 41 usam (7%)** — Odachi, Nodachi e Machado de Guerra, que são as três que a ficção carrega de defeito mesmo.

### Decidido — quatro propriedades novas, e o que a triagem matou

| propriedade | custa | o que é | âncora |
|---|---|---|---|
| **`Rompe`** | 1 | vantagem contra objeto e estrutura | *"Força governa agarrar, **quebrar**"* — peça 5 §1 |
| **`Emaranha`** | 1 | dá acesso a agarrar sem largar a arma | *"Força governa **agarrar**"* — peça 5 §1 |
| **`Vestida`** | 1 | não ocupa a mão | o §4 já mede a mão livre, e `Selo`=`Gesto` depende dela |
| **`Talha`** | 1 | a arma é ruim de bloquear — **−1 no `Bloquear` do alvo** | `RASCUNHO-bloqueio.md` §4 |

**Duas morreram na triagem, e uma delas por sentido e não por substring.** `Quebra` saiu `DENTRO` de **Quebra Coisa**, que é Melhoria — e ali a colisão é de sentido: uma Melhoria que quebra coisa faz exatamente o que a propriedade faria. Virou `Rompe`. E `Trava` saiu `OCUPADO`, o que matou a ideia de prender a lâmina do oponente com o Sai — que morreria no mérito de qualquer jeito, porque **`desarmar` tem zero ocorrências no projeto inteiro**.

*E `Enrosca` era a escolha anterior de `Emaranha`; o Mizuki trocou por remeter melhor a agarrar. `Cravo` era `Talha`, e mudou de nome **e de efeito** — ver a subseção abaixo.*

### Decidido — a `Talha` bate no Bloquear e não na proteção, e isso tem uma dívida escrita

*Ideia do Mizuki:* **"uma propriedade que dificulta justamente no bloqueio."**

A versão anterior (`Cravo`) ignorava `1` de proteção do alvo. Bater no **`Bloquear`** é melhor por dois motivos: ele é uma rota **opcional** que o defensor escolhe, então a propriedade cria uma decisão em vez de um desconto; e ela não encosta no teto de Defesa, que é derivado de três donos e não aceita item mexendo nele.

> **A dívida, e ela precisa estar escrita: `Bloquear` é regra opcional.** Numa mesa que não a use, a `Talha` **vale zero** — e a arma pagou 1 ponto por ela. Isso não quebra nada hoje porque o tópico de regras opcionais não existe, mas o validador desta peça tem de acusar se alguma arma ficar dependendo só dela.
>
> **E o invariante do Bloquear continua inteiro.** Ele diz que *o modificador do defensor é o mesmo nos dois lados*; a `Talha` é do **atacante**, e não muda modificador nenhum do defensor.

### Adicionado — as 52 armas com dado e propriedades

**41 de corpo a corpo, no fundo `3/5`, mais as 11 de tiro** — a escada do tiro é a da v0.44 (`2d10 · 2d8 · 2d6 · 1d10`) e não foi tocada.

| | assinaturas | armas com gêmea |
|---|---|---|
| v0.44, só o preço | 14 | 35 de 41 — **85%** |
| v0.44, preço × categoria | 25 | 25 de 41 — 61% |
| **v0.45, a régua com fundo** | **39** | **4 de 41 — 10%** |

**Zero armas estourando o orçamento e zero com vaga vazia.** E as duas gêmeas que sobraram são as certas: `Machete = Machado` e `Soqueira = Tekko` — pares que **são a mesma coisa na ficção**, e tekko é literalmente a soqueira japonesa. A régua acertou ao não separá-las.

**Dominância conferida:** dentro de cada mão todas gastam o orçamento cheio, então **dado maior sempre vem com menos propriedade ou com restrição paga.** Nenhuma arma tem dado maior *e* mais propriedade que outra da mesma mão.

### Registrado — Odachi e Nodachi, e o que a pesquisa NÃO validou

*O Mizuki afirmou que o Odachi é complementar e o Nodachi sempre de duas mãos, e pediu a checagem.* **Três fontes especializadas dizem o contrário, com essas palavras:** *"essencialmente a mesma espada grande, com diferença só de nuance"* e *"não há distinção formal em morfologia de lâmina"* (TOUKENZA); *"documentos históricos mostram que os guerreiros japoneses usavam os dois termos de forma intercambiável"* (Swords of Northshire); *"os dois termos frequentemente se sobrepõem"* (TrueKatana). A diferença registrada é semântica — *nodachi* = espada de campo, *ōdachi* = espada grande.

**Mas as três sustentam outra diferença, e ela é melhor mecanicamente:** as duas eram *"carregadas nas costas, e o samurai tinha um assistente para sacar a arma quando precisava"*. **Uma arma que não se saca sozinha** é fato do objeto e é única no catálogo — virou a `Embainhada` do Odachi.

> **Os dois ficam separados, e fica escrito que isso é DECISÃO DE DESIGN e não canon.** Odachi leva `Alcance · Talha · Embainhada`; Nodachi leva `Alcance · Rompe · Volumosa`. Se alguém reler daqui a dez versões procurando a fonte histórica da distinção, ela não existe — e é por isso que esta linha está aqui.

### Registrado — o levantamento externo

**PF2e**, o sistema de pontos da comunidade (traits em três escalões — 1, 2 e 3 pontos; `Reach` é major lá e vale 1 aqui, e a diferença é de dono e não de erro) e o **`Finesse` como propriedade morta** (*"num personagem de Força ela é uma trait morta que come o orçamento"* — que é o preço conhecido de pôr `Fineza` na Lâmina Curta inteira). O **texto de regra** de `free-hand`, `grapple`, `razing` e `parry`, e a rejeição da `parry` por mexer em Defesa. **5e 2024**, a Weapon Mastery que **dispara em todo acerto e é limitada por classe** — o modelo que mostra que o custo do efeito mora no personagem, não na arma. E o levantamento de arma por arma: sai empunhado em par, tessen oculto **e** de arremesso, tantō de porte discreto, wakizashi de corredor de castelo, kusari-fundo como arma dissimulada, yari de 1 a 6 m contra naginata de 1,5 a 3 m.

### Achado — o requisito de Força ficou órfão quando a classe saiu do preço

*Achado no fim da versão, olhando a tabela do §5.3 recém-escrita.* A peça 5 §1 promete que *"armas de dado maior exigem Força mínima; quem luta com Destreza fica nas armas leves"*, e o §8 item 1 já tinha medido que **o requisito resolve acesso e não preço**, porque nenhuma classe passava de Força 3, que é o teto da criação.

**Só que o requisito morava na CLASSE, e a classe morreu como preço na v0.44.** Das 41 armas do §5.3, **zero têm requisito de Força escrito.** A promessa da peça 5 §1 deixou de ter implementação, e ninguém percebeu porque nenhum validador cruza aquela frase com o catálogo.

O conserto natural é reancorar no **dado**, que é o que a classe media:

| gate | armas com requisito | catálogo aberto a todo mundo |
|---|---|---|
| Força 3 para `d10` e `d12` | 11 | 30 de 41 — 73% |
| Força 3 só para `d12` | 6 | 35 de 41 — 85% |

*Não fechado nesta versão porque é decisão do Mizuki e ela conversa com a pergunta da divisão simples/marcial, que está logo abaixo.* **É a lição nº 9 pela porta de trás: um número perdeu o dono quando o dono foi arquivado.**

### Decidido — o treino de arma existe, e aqui ele não vira castigo

*Decisão do Mizuki, e ela fecha a pergunta que este mesmo CHANGELOG tinha aberto duas seções acima:* **o Emanador com Força 3 não pega um espadão — a menos que a Trilha de corpo a corpo dele conceda o treino.**

**A objeção dele contra a própria ideia estava certa na metade que importa:** *"todas as armas têm valores iguais, já que todas se pagam, então talvez a divisão seja inútil."* **A divisão não pode ser preço** — no PF2e ela é (`Simple +1`, `Martial +4`, `Advanced +6`), e aqui isso cobraria duas vezes.

**E é por isso mesmo que ela funciona aqui.** O modo de falha do 5e é que lá a arma simples é *pior*: o conjurador não é restrito, é punido. Este projeto já rejeitou esse formato quando decidiu que a rota Sem Técnica *"não pode ser os outros menos o Fundamento"*. **Sob a régua com fundo, punir é impossível por construção:**

| | uma mão (28 armas, todas `3/3`) | duas mãos (13 armas, todas `5/5`) |
|---|---|---|
| melhor dado do balde **simples** | `d8` — 4,5 | `d12` — 6,5 |
| melhor dado do balde **marcial** | `d8` — 4,5 | `d12` — 6,5 |

**Os dois baldes chegam ao mesmo teto.** A divisão restringe *qual* identidade, nunca *quanto* poder.

**Ela mora na categoria** — treze nomes e não 52, pela mesma conta que decidiu o eixo de identidade. Testada com `Lâmina Curta · Massa · Porrete · Arremesso` no simples: **19 armas contra 22**, e os dois baldes com arma de uma e de duas mãos. *Qual categoria cai em qual balde é escolha de sabor e fica para a próxima rodada; o critério que a régua impõe é que cada balde tenha as duas economias de mão.*

**E isso destrava a Trilha, que é a peça seguinte na fila.** Treino de arma **não é dado de dano** — é acesso, que está na lista do que a peça 5 §4 permite um Caminho conceder. A Trilha da Vanguarda deve de 6% a 9% da Rotina e não pode pagar em dado; **acesso a arma é moeda que ela pode gastar.**

> **Os dois gates são eixos diferentes e não se substituem:** o requisito de Força separa por **atributo** e o treino separa por **Caminho**. Um Emanador de Força 6 passa no primeiro e para no segundo — que é exatamente o caso que a decisão cobre.

### Em aberto

- **Quais das treze categorias são simples e quais são marciais**, e como as de projétil se encaixam nas quatro categorias de treino que a peça 6 §8 nomeia.
- **O requisito de Força, órfão** — reancorar no dado, e decidir onde o gate cai.
- **Se o catálogo precisa da divisão simples/marcial.** A peça 6 §8 diz *"confirmado que precisa existir"* e lista `simples · marciais · de fogo · ferramentas amaldiçoadas`, com **cada Caminho concedendo as suas**. Ela não pode ser **preço** aqui (no PF2e é: Simple +1, Martial +4, Advanced +6 no orçamento), porque toda arma já fecha no mesmo fundo. Ela só pode ser **acesso** — e aí não substitui o requisito de Força, porque **uma separa por atributo e a outra por Caminho.** A pergunta que decide: *o Emanador com Força 3 pode pegar um espadão?*
- **Os nomes dos três degraus de escudo**, e quantos são.
- **A `Comprida` não foi usada** por arma nenhuma — o Bō virou `d10` e não precisou dela. Ou some, ou acha dono.
- **O validador da peça**, com a busca exaustiva, as três rotas de proteção e a triagem de todo nome — incluindo a checagem de que nenhuma arma dependa só da `Talha`.
- **Se o catálogo precisa da divisão simples/marcial**, e se ela ainda faz sentido agora que toda arma se paga.
- **As quatro vagas de Desliga da peça 13.**
- **As três checagens do Bloquear**, no `conferir-atributos.py`.
- **A Cicatriz, Energia Reversa, o clash, o nome do sistema.**

---

## [0.44] — 2026-08-13

**A régua de preço das armas caiu e foi substituída.** *"O preço mora na classe"* virou *"o preço mora na arma, dentro de um orçamento"* — e a mudança não foi de gosto: **o catálogo já tinha deixado de obedecer à régua velha na v0.42, e ninguém tinha escrito isso.** Continuam **treze peças e treze validadores**; Equipamento continua em rascunho.

### Achado — a classe já tinha parado de ser o preço, e quem a derrubou foi uma decisão nossa

A escada de dados do §5.2 põe **dois dados diferentes dentro da mesma classe**: a Pistola rola `2d8` e a Submetralhadora rola `3d6`, e as duas são `Tiro leve`, que a tabela declara como `d6`.

**Com zero arma nova e zero `Fineza` a mais, o catálogo praticava 9 pacotes de preço para 8 classes.** A pergunta que a `Fineza` abriu — *"o preço mora na classe ou na arma?"* — já estava respondida na prática desde a decisão do `3d10`, e a resposta estava escrita em lugar nenhum.

*E as duas saídas que o rascunho oferecia supunham as duas que a classe ainda era o preço.* Uma delas — *"a classe dá o pacote, e uma arma pode carregar uma propriedade a mais"* — nem alcançava o defeito: **o que estava quebrado era o dado, não uma propriedade.**

### Decidido — o preço mora na arma, e o orçamento saiu por regressão

> **1 ponto = `0,33` por rodada = um passo de dado = uma propriedade.** A unidade não foi escolhida: o §5.2 já tinha medido o passo em `0,33` e o `Par` em `0,32`.

Tratando as seis classes de corpo a corpo publicadas como **dados de uma regressão** em vez de regra, o orçamento cai sozinho: **`2` para uma mão, `4` para duas.** `Oculta` d4+2 propriedades, `Curta` d6+1, `Uma mão` d8+0, `Haste` d10+1, `Pesada` d12+0 — **cinco fecham exatas.**

**A sexta é a `Versátil`, que gasta 3 num orçamento de 2 — e essa é a dominância que a v0.41 achou e registrou como aberta *sem conseguir dizer de que tamanho era*.** A régua reencontrou o defeito de fora e o dimensionou em **1 ponto**. Contra-teste que ninguém armou.

### Decidido — a régua inteira numa tabela, no molde do PF2e

*Pedido do Mizuki: "seguir a lógica do Pathfinder — precificar o que uma arma pode ter."*

| propriedades | uma mão | duas mãos |
|---|---|---|
| 0 | d8 | d12 |
| 1 | d6 | d10 |
| 2 | d4 | d8 |
| 3 | — | d6 |

**No PF2e a lista de tetos é decidida caso a caso; aqui ela *é* o orçamento**, então combinação abusiva fica ilegal por construção em vez de ser pega no teste. **E o teto da `Fineza` cai dela sozinho: d6 numa mão** — exatamente onde o PF2e põe o `Finesse`, por outro caminho. *Conferindo pelo lado oposto: `Fineza` num d12 daria `6,5 + Destreza 6 = 12,5` e **empataria com a `Pesada` nos dois eixos**, dano e Defesa. O orçamento corta três degraus antes.*

### Decidido — o `3d10` da arma de fogo caiu, e a v0.42 mediu contra a pessoa errada

| arma | gasta | orçamento |
|---|---|---|
| `3d10` — Rifle de Precisão, Metralhadora Pesada | **9,0** | 4 |
| `3d8` — Espingarda, Rifle, Besta | 6,0 | 4 |

E os `−5` estão medidos contra **Força 6**, que é o melhor caso para o corpo a corpo. Contra quem de fato pega uma arma que não soma atributo, o `3d10` estourava em **8 pontos com Força 3** e **11 com Força 0 — mais do que os 6% a 9% da Rotina que a Trilha da Vanguarda inteira deve.**

> **A v0.42 mediu `+4,3% da Rotina` e aceitou pelo tamanho, e o número bate exato com o de Força 6. O que faltou foi somar quem segura a arma** — lição nº 7 numa direção nova.

**Ela também tinha matado o argumento *"não soma mod E tem munição"* por dupla contagem, e estava certa nisso.** O que ela não viu é que **não somar atributo não é penalidade: é independência de atributo**, e independência é o que torna a arma boa justamente para quem não investiu.

**Decisão do Mizuki: `2d10` no topo**, escada de dois dados — `2d10 · 2d8 · 2d6 · 1d10`. O topo fica **um ponto abaixo da `Pesada`** porque agora ele paga o `Longo Alcance`; a distância deixou de ser de graça. *Contra-teste: a fórmula reproduz a `Pesada` e a `Haste` em `4,0` de `4`, exatas — é a mesma régua do corpo a corpo, não uma paralela.*

### Achado — o §5.2 trazia as duas regras de recarga ao mesmo tempo

```
"Recarregar custa a sua ação."          <- a regra velha
"Recarregar é Ação Bônus."              <- a decisão do Mizuki
```

E a tabela de `54% / 46% / 14%` ficava **entre as duas, calculada com a primeira.** Eu cheguei a oferecer uma saída inteira montada em cima dela antes de ler as duas frases juntas. *Lição nº 5 na direção mais chata: a tensão de preço era contradição de texto disfarçada, e a conta em cima dela não valia nada.*

### Achado — o `X = 1` da `Munição` apagava o ataque extra

*Achado pelo Mizuki, olhando a faixa `1 · 2 · 3` e dizendo que ela estava baixa demais.* O modelo velho supunha **2,2 ataques por combate** — um golpe simples por rodada. Mas a peça 6 §3.1 dá **ataque extra ao Bastião e à Vanguarda no nv6**, e *"ataque extra é sempre golpe simples"*, que é o que a arma de tiro faz.

| X | ataques que saem, **sem** extra | **com** extra |
|---|---|---|
| **1** | 100% | **64%** |
| 2 | 100% | 97% |

**Com dois golpes você precisa de duas recargas e só tem uma Ação Bônus.** O `X=1` não atrasava o tiro — ele comia o benefício de nível 6 de dois Caminhos inteiros.

**E de 2 para cima a `Munição` custa 1 a 3 pontos percentuais: ela é textura, não preço** — o que quer dizer que nunca poderia ter sido contada como contrapeso do dado, e o §5.2 velho contava.

### Decidido — o X de cada arma, e o vazamento da Metralhadora fica registrado

*Ordenação do Mizuki, por ficção.* **`4`:** Metralhadora Pesada, sozinha. **`3`:** Rifle, Submetralhadora. **`2`:** Pistola, Revólver, Espingarda, Rifle de Precisão e as duas Bestas.

> **A ordenação corta atravessado nos degraus de dado** — Rifle e Espingarda são os dois `2d8` e levam X diferente. **A régua velha não conseguiria escrever essa linha**; a nova consegue porque o preço mora na arma.

O `X=4` é o único que fura o critério dele de *"nenhuma arma atravessa a briga sem recarregar"*: ele deixa **22% dos combates** passarem sem recarga — **mas só para quem não tem ataque extra**, e uma metralhadora de cinta é arma de Vanguarda, que ganha ataque extra no nv6, exatamente onde o vazamento fecha. **O que vaza custa 0,1 a 0,3 ponto. Registrado em vez de consertado** — exceção escrita para 0,3 ponto é contar em vez de medir, lição nº 3.

*As duas Bestas ficam em `2` por falta de lugar melhor: a ficção pediria `1`, e o `1` está proibido. É o único ponto do catálogo em que ficção e régua discordam de frente.*

### Decidido — a `Versátil` custa **zero**, e a dominância de três versões fecha com tamanho

O passo só rende se você largar o escudo — ou a mão livre. E o escudo é uma curva, não um valor: **`0,9` ponto no nv2 e `10,9` no nv30.**

| nv | o passo rende | o escudo vale | vale largar? |
|---|---|---|---|
| 2 | 1,0 | 0,9 | **sim, por 0,1** |
| 6 | 1,0 | 2,7 | não |
| 30 | 1,0 | 10,9 | não |

**Aumentar o passo não conserta** (com três passos, `d6 → d12`, ganha até o nv6 e para) **e baixar o dado só troca o lado da dominância**: com `Versátil` a 1 ponto o dado teria de ser d6, e aí a `Uma mão` d8 ganha em todo nível — **inclusive na rota sem escudo**, porque as duas têm a mão livre e a `Uma mão` tem 1 ponto a mais de dado. **Não existe dado no meio.**

> **A saída veio de um argumento do Mizuki:** *"ter uma mão LIVRE é uma vantagem — permite usar feitiço, pegar item, interagir, coisa que você não pode fazer com espada e escudo, já que vai ter que SOLTAR em vez de guardar."*
>
> **E a versão dura disso já estava escrita no §4:** quem tem `Selo` = `Gesto` e pega um escudo **desliga a técnica inteira**. Para essa gente o escudo nunca esteve no menu.

Com o preço em zero, `Versátil` d8 e `Uma mão` d8 fecham os dois em `2 de 2` e viram **a mesma arma com um texto a mais** — a gêmea de graça que a v0.41 já tinha aprovado. **E a dominância aberta desde então fecha: ela vale `0,1` ponto, e só no nível 2.** *Dominância sem tamanho fica aberta para sempre; com tamanho, ela fecha.*

### Decidido — a categoria ganha efeito de crítico, e o §5.1 foi reaberto com o motivo

A trava era *"a categoria carrega uma coisa só, senão a matriz roda sobre `classe + categoria + propriedade`"*. **Com a classe saindo do preço, esse produto deixou de existir** — sobrou `arma × categoria`, e a arma agora fecha num orçamento em vez de ser comparada par a par. **A objeção era a matriz, e a matriz mudou de forma.**

Um efeito preso ao **20 natural** dispara em **3,0% das rodadas**, e isso muda a escala: **um erro de 3 de dano custa `3,00` pontos se o efeito dispara em todo acerto e `0,27` se ele fica no crítico. O portão divide o erro por onze** — e cabe até **11,0 de valor no disparo**, quase o dado inteiro da `Pesada`, por menos de um passo de dado.

**Treze, na categoria, e não cinquenta e dois, na arma. E não foi balanceamento que decidiu:** calibrando a taxa de erro nas oito Masteries do 5e 2024 — das quais quatro saíram fora da banda —, o espalhamento do melhor ao pior efeito é `0,89` ponto com treze e `1,22` com cinquenta e dois. **A diferença é `0,33`: um passo de dado, a menor unidade do projeto.**

| | treze, na categoria | cinquenta e dois, na arma |
|---|---|---|
| nomes na triagem | 13 | 52 |
| missões até a mesa conhecer o conjunto | **23** | 133 |
| a Vanguarda tem o que especializar | **sim** | não |

**E a escolha se justifica pela própria categoria, não pelo eixo de preço.** *A primeira redação desta entrada dizia o contrário, com "45 assinaturas legais para 52 armas" — número que não existe, e a subseção `Corrigido` logo abaixo mostra de onde ele saiu.* Rodada a régua sobre as 41 armas de corpo a corpo, o eixo de preço dá **14 assinaturas** e deixa 85% do catálogo em par; **com a categoria entrando, sobem para 25 e o par cai para 61%.**

### Corrigido — a conta da `Fineza` estava com o dobro do valor

O §5 dizia *"`1,32` por rodada — 4% da Rotina"*. **As duas colunas da própria tabela dele davam a resposta: `4,12 − 3,47 = 0,65`.** O `1,32` sai de multiplicar a diferença de 2,0 de dano por **`0,66`** em vez de por **`0,33`** — e `0,66` é o número da linha vizinha da mesma peça, *"a arma de duas mãos rende 0,66"*.

**A conclusão sobrevive e fica mais forte:** se 4% já tinha sido aceito como sabor, 2% é sabor com folga, e nada rebalanceia. *É o quarto exemplar do defeito que a v0.43 pagou para aprender — a prosa contradizendo a tabela do próprio documento — e o único jeito de pegar foi refazer a divisão.*

### Corrigido — o "45 assinaturas" contava o dado como eixo livre, e ele não é

*Achado aplicando a régua às armas em vez de contar o espaço dela.*

O número saía de um produto: **5 dados × 9 opções de propriedade** — as oito mais "nenhuma" — dá 45. O `185` da linha vizinha é o mesmo produto com duas propriedades: `C(8,2) + 8 + 1 = 37`, vezes os mesmos 5 dados. E o *"`Lâmina Longa`, 8 armas contra 10 disponíveis"* é o 5 outra vez, dobrado pelas duas classes de mão. **As três frases têm o mesmo fator errado dentro.**

> **O 5 não existe.** A régua do §5.0.1 faz o dado ser **função** de (mãos, nº de propriedades): escolhidos os dois, sobra **um** dado legal, porque gastar menos que o orçamento é dominância estrita. O dado é saída da conta e não entrada — ele não pode variar arma por arma, nem de graça nem caro.

O espaço legal de verdade, com as seis propriedades que servem no corpo a corpo, é **79** combinações. E *"dado × uma propriedade"*, que é o que aquela frase media, são **14** — não 45.

**Mas o espaço nunca foi a pergunta.** Propriedade não é escolha: é o que a arma é. Rodado sobre as 41 de corpo a corpo, com as propriedades que a ficção força:

| eixo | assinaturas | armas com gêmea |
|---|---|---|
| só o preço | 14 | **35 de 41 (85%)** |
| preço × categoria | 25 | **25 de 41 (61%)** |

*É a lição nº 3 numa direção nova — **contar o espaço não é contar o uso** — e a mesma família da regra de método que a v0.43 pagou: conclusão escrita a partir de um número que nunca rodou sobre os dados reais.*

**E o achado reforça a decisão que a entrada acima tomou.** Se o eixo de preço sozinho deixa 85% do catálogo gêmeo, o efeito de crítico na categoria não é o eixo secundário de identidade: é o que faz a identidade existir. **A `Fineza` na `Lâmina Curta` inteira, que parecia sabor, é o que mantém quatro facas distinguíveis de um `Machete`** — e nada dentro da categoria as separa entre si.

### Alterado — três derivas de documentação, e uma delas escondia a v0.43 inteira

| onde | o que estava | o que é |
|---|---|---|
| `ESTADO-ATUAL`, `README`, `LEIA-ME` | **zero menções ao `Bloquear`** | a v0.43 inteira só existia no CHANGELOG |
| `README`, a árvore | *"CHANGELOG, v0.1 a v0.39"* | v0.1 até a versão atual |
| `ESTADO-ATUAL`, cabeçalho | *"Atualizado em 12/08"* na v0.43 | 13/08 |

**A primeira é a que mordia:** o `ESTADO-ATUAL` é o ponto de retomada declarado, e ele não sabia que `RASCUNHO-bloqueio.md` existia. **Quem retomasse sem ler o CHANGELOG retomaria sem a regra.** Ele ganhou uma seção com o achado do `E[d20] = 10,5`, o invariante do modificador único, e **o registro de que o validador do Bloquear não pode ser arquivo novo** — as três checagens dele são sobre a fórmula da Defesa, que é da peça 1, então elas vão para o `conferir-atributos.py`.

### Registrado — o levantamento externo

**PF2e** (orçamento por arma, com o budget mudando por categoria e por mão — 4/9 no Simples, 7/13 no Marcial, 9/15 no Avançado; a reconstrução do sistema de pontos pela comunidade fecha em **mais de 90% das armas oficiais dentro de 0 a 2 pontos**), **as catorze *critical specializations*** (que **não são grátis na arma: são destravadas por característica de classe no nível 5**), **o `Finesse` como propriedade morta** (*"se você é personagem de Força, ela vira uma propriedade morta que come o orçamento"* — a Falchion troca `Finesse` por um dado inteiro mais uma propriedade), **o 5e 2014** como controle negativo (*"um Guerreiro não tem razão real para escolher Machado de Batalha em vez de Martelo de Guerra"*), e **as oito Masteries do 5e 2024**, com o modo de falha medido: Vex forte demais, Sap *"bom demais se não fosse limitado"*, Graze e Slow atrás.

### Em aberto

- **O dado e as propriedades de cada uma das 52 armas**, agora que a régua existe.
- **Os treze efeitos de crítico**, um por categoria — e a armadilha documentada do PF2e: efeito que morre contra alvo comum (sangrar morto-vivo, derrubar quem já está no chão).
- **O validador da peça**, com a busca exaustiva, as três rotas de proteção e a triagem de todo nome.
- **As quatro vagas de Desliga da peça 13**, que esperam desde a v0.39.
- **As três checagens do Bloquear**, no `conferir-atributos.py`.
- **A Cicatriz, Energia Reversa, o clash, o nome do sistema.**

---

## [0.43] — 2026-08-13

**Nenhuma regra em vigor mudou.** Uma sessão de projeto sobre uma ideia do Mizuki — dar ao jogador a chance de rolar para se defender — e ela virou `03-mecanica/RASCUNHO-bloqueio.md`. **Continuam treze peças e treze validadores.** A regra é opcional, vai para o tópico de regras quando ele existir, e não entra em balanceamento até lá.

### Achado — a house rule do hobby tem um bônus escondido, e ninguém nunca notou

A resposta padrão para *"quero rolar minha defesa"* é *"role d20 no lugar dos 10 da CA"*. Ela dá **+2,5 pontos percentuais de graça, em todo ataque, para todo mundo**, porque `E[d20] = 10,5` e a base da Defesa é `10`.

**Oito buscas externas não acharam uma única discussão do problema.** A house rule é praticada há décadas com o viés dentro dela.

### Decidido — `Bloquear`, e o dado da defesa não é d20

> **Role `2d10 + (sua Defesa − 11)` no lugar da sua Defesa.** A média de 2d10 é 11, então na média dá exatamente a sua Defesa.

**Qualquer dado de média 10 é neutro por construção** — `2d10−1`, `2d8+1`, `2d6+3`, `4d4` devolvem 50,0% exatos contra os 47,5% do d20. Escolhido o **2d10−1**, que é o que mais guarda a textura (tráfego 16,5% contra os 25% do d20).

**E a razão de não dar para consertar o d20:** a média de um dado único sempre termina em `,5`, porque é `(N+1)/2`. A base da Defesa é inteira, então o buraco é de **meio ponto** — `d20` dá +2,5pp e `d20−1` dá −2,5pp, sem nada no meio. **2d10 tem média inteira e o `−1` fecha exato.**

*Varridas 11 × 9 = 99 combinações de modificador contra bônus: todas idênticas ao estático.* E o `−1` não aparece na mesa: a ficha imprime `Defesa 17 · Bloquear 2d10+6`.

### Decidido — `Aparar` e `Brecha`, e os dois gastam Reação

*Ideia do Mizuki, vinda do For Honor: recompensar quem apara, punir quem não apara direito.*

| resultado | o que acontece |
|---|---|
| **duplo 10 · Aparar** | o ataque não acerta. Você pode gastar a **Reação** para contra-atacar, com **+3 de dano** |
| **duplo 1 · Brecha** | o ataque acerta. O agressor pode gastar a **Reação dele** para atacar de novo, sem bônus |

**O Aparar não anula um 20 natural**, e a trava saiu de graça: com ela o multiplicador vai de `0,5490` para **`0,5500` exato** — ela **paga** a neutralidade em vez de custar. **E Bloquear não vale em Teste de Resistência.**

**Custo do pacote inteiro: 0,43% do golpe no nv30.** Bloquear puro é 0,00%.

### Achado — o bônus se decidiu sozinho, e `nível` não cabia

A proposta era `+nível` ou `+metade do nível` de dano no contra-ataque. **O golpe simples quase não cresce** — dado fixo e Força travando em 6 —, então ele vai de 9,5 no nv2 a 12,5 no nv14 e para. `+25%` disso é sempre 2,4 a 3,1: **`+3` fixo é literalmente o mesmo número**, sem porcentagem na mesa.

`nível` passa o alvo por **2,3× no nv6 e 9,6× no nv30**, e a distância **cresce** — lição nº 1 na forma mais direta.

**E o teto é +3,9 de dano cru, com o nv22 mandando:** é lá que a Reação vale 9,0 contra os 6,88 do AO, e é o único lugar da mecânica onde existe decisão de verdade. `+3` cabe com 0,9 de margem; **`+4` mata a decisão.**

> **A troca fica registrada porque ela é contraintuitiva:** bônus maior deixa o **líquido** melhor (0,43% → 0,02%, porque compensa o golpe maior do inimigo) **e mata a decisão**. As duas correm em sentidos opostos.

### Decidido — o invariante que segura tudo

> **Bloquear usa exatamente o mesmo modificador da Defesa passiva. Nada pode aumentar um sem aumentar o outro.**

**+1 de diferença vale 2,5pp** — o tamanho do viés que esta regra inteira saiu para consertar. Um único item mal escrito desfaz tudo. **O validador confere que as duas são a mesma expressão**, não dois valores que hoje calham de dar igual — porque valores iguais hoje divergem amanhã, e isso é a lição nº 9.

### Registrado — quatro erros meus, e os quatro pegos por conta rodada

*Ficam escritos porque o método é o que sobrevive à sessão.* Três vezes a **prosa do script contradisse a tabela do próprio script** — *"não existe inimigo contra o qual bloquear seja errado"* com a tabela mostrando −2,7pp ao lado; *"~0,5pp"* quando o valor era 0,05pp; *"de 1,5× a 2,5×"* quando a coluna dizia 5,2×. E uma vez foi aritmética: **`36,0` no lugar de `72` para o golpe do chefe no nv30**, o que inverteu o sinal do líquido do pacote.

**A regra que sai daí: não escrever conclusão dentro do script antes de ler a saída dele.**

### Registrado — o levantamento externo, e o que ele não tinha

**GURPS** (aparar e bloquear uma vez por turno, de graça — e o material admite que *"não existe consideração tática"* quando só vem um golpe), **Mythras** (pontos de ação: defender compete com atacar), **RuneQuest** (−20% cumulativo por aparada extra), **Riddle of Steel** (pool único dividido entre ataque e defesa), **Exalted** (penalidade de onslaught), **rolagem virada para o jogador** (conversão exata, e o engajamento sobe sem a probabilidade mudar).

**Nenhum deles mantém CA estática junto de uma rolagem opcional grátis e neutra.** A combinação não apareceu em busca nenhuma — foi derivada, não encontrada.

### Em aberto

- **As condições que impedem Bloquear** — surpreendido, caído, agarrado. Ficam para quando a peça de **dano e condições** existir.
- **O validador do Bloquear**, com as três checagens do §7.
- **A ficha precisa imprimir a linha** `Defesa 17 · Bloquear 2d10+6`.
- **O inimigo precisa de Reação na ficha dele** para a Brecha funcionar.
- **A classe das doze armas novas** e o validador de Equipamento, que continuam da v0.42.
- **A Cicatriz, Energia Reversa, o clash, o nome do sistema.**

---

## [0.42] — 2026-08-12

**Equipamento andou muito, e três coisas que já estavam escritas caíram.** Nenhuma peça nova; **um ofício novo**, o `Alfaiate`, que subiu os ofícios de dez para onze. O rascunho de Equipamento foi de 487 para 800 linhas, a dívida que a peça 11 e a peça 8 deviam foi **aplicada**, e o `conferir-criacao.py` e o `conferir-pericias.py` mudaram.

### Fechado — o dono do teto de Defesa, e não é nenhuma das duas opções que o §8 oferecia

O `20` é **derivado**: `10` da peça 1 §5, teto de atributo `6` e teto de refino `10` da peça 2 §3, e a fórmula de cobrir-se da peça 11 §5. **Zero parâmetros livres**, então ninguém escreve o número — escrevê-lo seria a lição nº 9, e medir uma checagem contra ele seria a nº 8 pela quarta vez.

> **Equipamento é dona do invariante, não do valor:** *nenhuma montagem de equipamento passa da Defesa que a rota sem equipamento alcança.* O validador deriva o teto dos três donos e roda a busca exaustiva.

**E a frase que sustentava o item caiu junto.** O §3 dizia que as duas rotas topam em 20; equipamento topa em **19**, e a diferença nasceu no §4, quando o escudo ganhou teto de Destreza para não furar o 20. Busca exaustiva de 196 montagens: máximo 20, três montagens chegam, nenhuma passa. **Decisão do Mizuki: fica em 19, agora como decisão e não como sobra.**

### Achado — o Traje era a classe do meio do 5e, contra cobrir-se

Traje não limita Destreza, cobrir-se também não, então os dois se comparam só por proteção — e a escada do Traje (1/2/3) é a mesma que cobrir-se percorre sozinha na linha passiva. **+0 em seis das oito faixas de nível**, e ainda cobrando Força.

O §2 foi para duas classes citando o *"worst-of-both-worlds"* da armadura média do 5e e construiu o Traje exatamente ali — só que contra cobrir-se, que **é a armadura leve deste sistema** e não tinha sido reconhecida como tal.

**Conserto:** a coluna de Força deixou de ser compartilhada (**Traje `— / — / 3`**, **Revestimento `3 / 4 / 6`**; o Força 3 no topo do Traje pousa nos 45% que o §3 já tinha aprovado), e o Traje ganhou benefício **fora da proteção** — vantagem numa situação, com lista fechada e vaga aberta, no molde do Destranca de identidade da peça 13. **O `Alfaiate` entrou para fabricar**, e o canon confirma: existe alfaiate dedicado ao mundo jujutsu e estudante encomenda uniforme sob medida.

### Achado — a peça 6 §3 não tem exceção para arma de tiro

*"Golpe simples = arma + Força"*, e o acerto à distância soma **Destreza** (peça 1 §5). A arma de tiro acertava com um atributo e causava dano com o outro: **2,48 por rodada contra os 4,12 da Pesada**, quando a matriz achava que a distância era 0,33. **Cinco vezes maior que o buraco que as propriedades deviam pagar.**

*Resolvido pela categoria:* `Yumi` soma Destreza, `Balestra` e `Arma de Fogo` não somam atributo e ganham dado maior.

### Achado — o `0,60` do §5 não reproduz com a fórmula do §4

`diferença de dado × 0,55 × 0,60 de uso` dá **0,33** para d10 contra d12. O `0,66` do §4 reproduz exato; o `0,60` só aparece sem o fator de uso. **Duas fórmulas no mesmo documento**, e a segunda foi escrita sem o fator que a primeira acabara de fixar.

### Adicionado — categoria, e as oito propriedades

**Treze categorias, 52 armas.** A categoria carrega **uma coisa só, a fonte do dano** — se carregasse número próprio, o valor viraria `classe + categoria + propriedade` e a matriz teria de rodar sobre o produto dos três, que é a lição nº 7 pela porta de trás. Ela é também o gancho da especialização da Vanguarda.

**E três das sete propriedades sem texto eram a mesma coisa:** `Alcance`, `Distância` e `Arremesso` respondiam *"a que distância?"*, e a resposta é um número. Colapsaram em `Alcance` e `Longo Alcance`, com valor em metros. `Arremesso` sobreviveu como **categoria**.

| propriedade | fecho |
|---|---|
| `Par` | **role dois dados de dano e fique com o melhor** — 0,32 contra um alvo de 0,33 |
| `Versátil` | o dado sobe **um passo**. Vale 0,33 em qualquer degrau |
| `Oculta` | **camada 1 · Permissão** do §6. Zero número em combate |
| `Munição` | recarrega no **1–2 natural** ou a cada **X** ataques. **Recarregar é Ação Bônus** |
| `Fineza` | troca Força por Destreza no acerto e no dano |

**O X da `Munição` não é o pente.** Com 2,2 ataques por combate, **qualquer teto a partir de 4 nunca morde** — o gatilho do dado assume e o número vira enfeite. A faixa útil tem quatro valores: `1`, `2`, `3` e `—`.

### Decidido — `Precisa` voltou como `Fineza`, e metade do argumento que a matou caiu

O argumento era duplo. **A metade que caiu:** *"tira o primeiro trabalho da Força, que tem uma perícia só"* — Força agora compra Traje 3, Revestimento 1/2/3 e escudo 2/3, que é o segundo trabalho que a peça 1 §9 pede desde a v0.24, e que **não existia** quando a decisão foi tomada. **A metade que ficou**, medida: Força 6 com Pesada e escudo faz 4,12 e Defesa 19; Destreza 6 com `Fineza` e cobrir-se faz 3,47 e Defesa 19. **1,32 por rodada, 4% da Rotina.** Vira sabor.

### Decidido — 3d10 no topo da arma de fogo, e o argumento não vale

*O tamanho fecha:* **+32% no golpe simples, +4,3% da Rotina** — o mesmo tamanho da `Fineza`, e abaixo dos 7,5% que a Trilha da Vanguarda deve cobrir.

> **O argumento não fecha, e fica registrado por quê.** Era *"não soma mod E tem munição, duas penalidades"*. A primeira **já está dentro do dado** — `3d10 = 16,5` já é o total sem mod, e o dado grande é o que compensa; contar de novo é a **lição nº 2**. A segunda **vale zero**, porque recarregar em Ação Bônus não tira ataque nenhum. *E o outro lado paga o mesmo:* Força 6 e Destreza 6 custam 3 pontos cada, e as duas carregam `Duas mãos`.

### Aplicado — a dívida que a peça 11 e a peça 8 deviam

**O escudo saiu da lista do que desliga cobrir-se** (ele **soma**), e o preço da Reação virou **agnóstico de fonte** — de *"você fica sem a proteção passiva"* para *"você fica sem proteção"*. Quatro pontos em dois documentos, e **três checagens novas no `conferir-criacao.py`** para a decisão não voltar em silêncio. *Três perturbações conferidas, com contra-teste provando que são checagens separadas.*

### Achado — o `conferir-pericias.py` nunca abriu a peça 7

O docstring prometia *"contagem por atributo bate com o documento"* e a lista estava **escrita dentro do validador**. Eram **três cópias** dos ofícios — a peça, o validador e o `dados.js` — e só duas eram comparadas. **Lição nº 9 dentro de um validador**, e ela só apareceu porque a contagem `!= 10` explodiu por acidente na passada do Alfaiate.

Consertado na raiz: ele **lê a lista da peça 7**, e a contagem declarada sai do **título do §5**, separada da lista aplicada — lição nº 8. O `conferir-ficha.py` deixou de procurar `'## 5. Os dez ofícios'` literal. **Quatro perturbações conferidas**, com contra-teste provando que o regex ficou agnóstico ao número por extenso.

### Registrado — a triagem tem um quarto ponto cego

`Leve`, `Média` e `Pesada` são os **tiers de Restrição** e saem `LIVRE`, porque a triagem compara contra Família, Forma, Melhoria e Tema, e **tier de magnitude não está em lista nenhuma**. A classe de arma `Pesada` colide com o tier `Pesada` desde que as duas existem.

**E o `ARMA DE FOGO` virou régua:** um nome composto que contém termo ocupado **não herda a colisão**, porque *Arma de Fogo* não é o Tema `Fogo`. Grau novo ao lado de `OCUPADO`, `DENTRO` e `fraco`.

### Em aberto

- **A classe das doze armas novas**, e com ela a pergunta que a `Fineza` abriu: **o preço mora na classe ou na arma?** Uma propriedade solta troca *8 classes para conferir* por *52 armas*.
- **O validador da peça** — com as **três** rotas de proteção (cobrir-se · uniforme · **sem energia nenhuma**), o teto derivado dos três donos, e a dominância por valor total.
- **As quatro vagas de Desliga da peça 13.**
- **A Cicatriz não tem mecânica, só nome.**
- **Energia Reversa, Barreira Simples, Cortina** e a régua da Aptidão Própria.
- **Qual modelo de clash vale.**
- **Nome do sistema.**

---

## [0.41] — 2026-08-12

**Equipamento andou, e três coisas que já estavam escritas nela caíram.** Nenhuma peça nova e nenhum validador novo — continuam treze e treze. O que mudou foi o rascunho de Equipamento, de 160 para 487 linhas, e o `conferir-nomes.py`, que estava classificando colisão errado desde sempre.

### Achado — a conta do escudo comparava duas colunas em unidades diferentes

O §4 do rascunho derivou `escudo +1` pondo lado a lado *"+1 de proteção poupa X"* e *"duas mãos rende 2,0"*, e concluiu que a troca empatava no meio da campanha.

**A coluna do escudo estava certa.** `0,05 × CHEFE` é o valor de tirar 5 pontos percentuais da chance do inimigo, e o `CHEFE` do manual é dano **por acerto** — é assim que o `conferir-atributos.py:459` o usa, multiplicando por `0,5`.

**A coluna da arma não.** Os `+2` de dado são o ganho *quando você acerta*, num turno em que usa a arma. Por rodada vale `2,0 × 0,55 × quanto do tempo você dá golpe simples` — o `0,55` da peça 1 §6 mais o crítico da §5.2, e o teto de uso que o `conferir-orcamento.py` já mede. Refeita, a arma rende **0,66** e o escudo passa ela no **nv6**, não no nv16.

> **A unidade de um número se lê do uso, não do nome.** `CHEFE` parece dano por rodada e não é. Quem descobriu foi o validador que já usava o número certo.

### Achado — o escudo desligava cobrir-se, e isso o matava no primeiro marco

O §4 dizia *"o custo do escudo é a mão"*. A peça 11 §5 e §9 e a peça 8 dizem outra coisa, com todas as letras: **"uniforme, armadura e escudo desligam a proteção de energia"**.

| nv | refino | cobrir-se dá | escudo dá | o escudo vale |
|---|---|---|---|---|
| 2 | 1 | 1 | 1 | 0 |
| 6 | 3 | 2 | 1 | **−1** |
| 30 | 10 | 4 | 1 | **−3** |

Do refino 3 em diante pegar escudo **tira** Defesa. Refino 3 chega no nv6 em duas das três rotas. **A derivação inteira mediu contra um escudo que não entraria em ficha nenhuma.**

*É a armadilha de sempre, na direção menos vigiada: o preço usava um termo que existe, e ninguém tinha ido ler a regra pendurada nele.*

### Decidido — o escudo soma, e isso muda três documentos

A alternativa era manter o desligamento, e a conta mostrou que ela mata o item. Então **uniforme e armadura continuam desligando; o escudo passa a somar.**

> **A decisão está tomada e NÃO está aplicada, e isso é de propósito.** A frase mora em três lugares — peça 8 passo 7, peça 11 §5 e peça 11 §9 — e as três só mudam quando Equipamento fechar, junto com a outra dívida que a peça 11 já devia (*"você fica sem a proteção passiva"* virando *"você fica sem proteção"*). Mexer nas duas de uma vez evita tocar duas vezes na mesma peça fechada.
>
> **Fica registrado em quatro lugares porque decisão que termina em "corrigir em três documentos" é exatamente a que o projeto já perdeu sete versões:** aqui, no §7 do rascunho, na seção nova do `ESTADO-ATUAL`, e como checagem obrigatória do validador da peça, no item 9 do §8. *Se a próxima passada fechar a peça sem mexer nos três, o validador tem que falhar.*

**E abriu um buraco que precisou de conserto na mesma passada:** com o escudo somando, `cobrir-se refino 10 + escudo` dá Defesa **21** e fura o teto de 20 que o §3 tinha fixado. Foi a decisão que abriu, e é ela que fecha.

### Decidido — RD foi levantada, medida, e morta pelo critério e não pela conta

A conta apontava para ela: `RD fixa` é a única forma que fica na mesma escala do dado da arma — erra por fator constante (1,5×) em todo nível, contra o fator crescente da proteção (0,5× a 5,5×).

> **Decisão do Mizuki: não.** *"Dar RD nunca é solução, pode acabar vindo a virar mais um cálculo e ninguém quer isso."*

**Fica registrado porque a conta e o critério discordaram, e o critério ganhou.** A conta mede valor por rodada; ela não mede quanto uma subtração a mais custa em tempo de mesa. **Esse eixo não tem validador, e não vai ter.** Sem o registro, alguém reabre a ideia daqui a dez versões achando que ninguém tinha feito a conta.

### Decidido — a escada de escudos, e ela sai de duas linhas que já estavam escritas

A saída estava na própria peça, em dois lugares que ninguém tinha juntado: o §3 fechou dizendo que **as duas rotas topam em Defesa 20**, contando o escudo dentro disso, e o §2 já tinha adotado a régua do 3.x — ***"proteção e teto de Destreza são um orçamento só"***.

**O escudo maior não cresce por cima do teto: ele cresce comendo teto de Destreza**, igual ao Revestimento. E aí vira o prêmio da build de Força sozinho, sem regra nova, porque quem tem Destreza baixa não perde nada com o teto.

| degrau | proteção | teto de Destreza | requer Força | custa marco? |
|---|---|---|---|---|
| 1 | 1 | 5 | — | não |
| 2 | 2 | 3 | 3 | não — cabe na criação |
| 3 | 3 | 1 | **5** | **sim, 2 pontos** |

**O degrau 3 é o primeiro item do catálogo inteiro que cobra ponto de marco** — toda arma pede no máximo Força 3, que é o teto da criação. É o trabalho novo que a peça 1 pedia desde a v0.24, com *"Força tem uma perícia só"*.

Busca exaustiva de uniforme × escudo × Destreza: **nada passa de 20, e 20 é alcançado por duas rotas** — o teto não é decorativo. Nenhum dos três degraus é dominado, e o cruzamento entre o 1 e o 3 cai em **Destreza 3**, o mesmo ponto de Traje contra Revestimento. Uma régua, dois lugares.

### Registrado — e ela não conserta a arma de duas mãos, que é o que motivou tudo

| nv | o degrau 3 poupa | a Pesada rende | razão |
|---|---|---|---|
| 6 | 2,58 | 0,66 | 4× |
| 30 | 10,80 | 0,66 | **16×** |

Proteção escala, dado não. **Isso não tem conserto dentro desta peça, e provavelmente não deveria ter:** a régua do §5 diz que *"a arma dá acesso e restrição; o Caminho dá o que você faz com ela"*. Duas mãos é acesso à árvore que exige duas mãos, e é a Trilha da Vanguarda que dá razão para largar o escudo — por isso ela vem depois na fila da v0.36.

**O alvo fica registrado para quando aquela peça chegar: 6% a 9% da Rotina, e a fração quase não deriva.** Não pode ser pago em dado de dano.

### Achado — o item 1 de Equipamento fechou, e o argumento que ia salvá-lo era desnecessário

*"A Pesada paga dois pontos de Força a mais que a Uma mão pelo mesmo valor líquido"*, e o argumento registrado era que o requisito é **compartilhado com o Revestimento**.

**Ele nem precisa disso: o requisito é grátis.** A Pesada pede Força 3, e 3 é o teto da criação (peça 2 §2). **Nenhuma classe do catálogo custa ponto de atributo** — o requisito de arma resolve acesso, que é o que a peça 5 §1 já tinha concluído.

**E o furo do teste era um nível acima do que a linha dizia.** Não é só que a matriz não somava o total: é que ela roda **uma vez só**. Enquanto o escudo desligava cobrir-se, existiam duas populações com dominâncias opostas — ficha de uniforme e ficha de cobrir-se —, e rodada uma vez ela cancelava as duas e saía verde. O validador precisa rodar **uma vez por rota de proteção**.

### Achado — `Uma mão` está dominada pela `Versátil`, e nenhum par de dados conserta

Mesmo dado, mesma mão livre, uma propriedade a mais, e o ponto de Força a mais não custa nada. O §5 afirmava *"zero classes dominadas"* — verdade com o requisito valendo como custo, falso sem ele.

Testados `d8/d10`, `d8/d12` e `d6/d10` para a Versátil: **em nenhum largar o escudo compensa**, porque o ganho de dado é 0,33 a 0,66 contra os 2,01 do escudo no nv16. O par de dados só vira escolha de sabor depois que a forma do escudo fechar.

### Corrigido — a triagem de nomes classificava três coisas diferentes com a mesma palavra

*Este é o conserto que mais vai render, porque ele estava enviesando decisão de nome desde que a triagem existe.*

O `conferir-nomes.py` marcava `OCUPADO` tanto para colisão exata quanto para **substring dentro de um termo composto**. As duas não são a mesma coisa.

> **Critério do Mizuki:** *"não precisa ligar tanto para nomes conjuntos, como Melhoria 'rasga escudo' a 'lança negra'. Se preocupe mais quando o nome bater de frente com o nome de algo que é **realmente** aquilo."*

A saída agora separa:

| grau | significa | mata? |
|---|---|---|
| `OCUPADO` | o **nome inteiro** já é termo definido | sim |
| `DENTRO` | aparece **dentro de um termo composto** | **não** — vá ler o termo e pergunte se ele *é* aquilo |
| `fraco` | fica a uma letra | não, mas confunde em voz alta |

**O custo de errar isso já tinha sido pago e ninguém percebeu:** `Lança` morreu na triagem por estar dentro de **Lança Negra**, e a arma entrou na classe Haste como **Yari** — que é exatamente uma lança, com o nome em japonês. **O sistema contornou um nome que nunca esteve ocupado.**

Quatro voltaram: `Lança`, `Escudo`, `Faca` e `Lastro`. Continuam mortos, por nome inteiro ou por sentido: `Chicote`, `Guarda`, `Anteparo`, `Bloqueio`, `Proteção`, `Carapaça`. **O catálogo foi de 39 para 41 armas.**

*Três contra-testes:* `Escudo` e `Lança` passaram de `OCUPADO` para `DENTRO`; `Toque`, que é Forma no manual **e** aparece em composto, continua `OCUPADO`, o que prova a prioridade do grau duro; e perturbando a linha que classifica, `Escudo` cai para `LIVRE`, o que prova que é ela que decide.

### Decidido — `Alcance` e `Distância` ficam, com o motivo escrito

As duas saem `OCUPADO` de verdade — `Alcance` é Família **e** Melhoria no manual, `Distância` é Tema — e as duas estão em uso como propriedade de arma.

**A colisão é de camada, não de sentido:** no manual descrevem o que um *feitiço* faz; na tabela descrevem o que um *objeto* é. Nenhuma regra pendura efeito nos dois ao mesmo tempo. Entram no validador da peça como `ACEITA`, no formato que os rótulos de rascunho da peça 6 já usam.

### Adicionado — a seção de itens comuns, em três camadas

*Pedida pelo Mizuki. A moeda ficou de fora de propósito — "provavelmente vai ser com preço e fornecimento".*

**A regra que abre a seção sai da conta: item comum não produz número.** Um item de +1 vale **33% de tudo que um atributo cresce em 28 níveis**, e com 5 a 7 mestres isso compõe — se cada um entregar um por arco, na terceira mesa o jogador ganhou de graça a campanha inteira, sem passar por marco, XP ou validador. **É o filtro multi-mestre falhando pelo lado que ninguém vigia: não é arbitragem divergente, é acúmulo invisível.**

E os quatro eixos óbvios já têm dono: proteção bate no teto de Defesa, cura bate em três decisões, dado de dano bate na Rotina, PE bate no `conferir-orcamento`.

| camada | o que é | o limite, e de onde ele sai |
|---|---|---|
| **1 · Permissão** | move de *não rola* para *rola sem maestria* | passa na lição nº 1 porque não empilha, não deriva (a CD de perícia é fixa) e não entra em rolagem disputada. **Item abre a porta, treino atravessa bem** |
| **2 · Consumível** | gasta e some, então não compõe entre mesas | **um a dois por missão.** De três em diante ele cobre as três lutas de graça da peça 10 e vira a resposta padrão — é o teste do bônus automático aplicado a item |
| **3 · Espaço** | inventário em slots | **desligada**, com gatilho escrito: *se o playtest mostrar que o grupo leva tudo sem escolher, o espaço entra* |

*Levantamento externo por trás disso:* cinco sistemas com o modo de falha de cada um — o *Christmas tree* do 3.5, a lista que ninguém lê do 5e, o `load` discricionário do Blades, o Tetris do Torchbearer e a economia de crafting que o alquímico do PF2e exige por baixo.

**E a ficção ajuda menos do que parecia.** Procurando o que um feiticeiro de JJK carrega além de ferramenta amaldiçoada, **não achei lastro** — a obra tem ferramenta e objeto amaldiçoado, e quase nenhum item mundano com peso de cena. O que tem lastro já está escrito nos ofícios: Herbalismo, Caligrafia, Forja, Entalhador dizem **quem fabrica**; falta dizer **o que sai**.

### Corrigido — o README contava quinze validadores e o `subir.sh` roda dezesseis

Achado na primeira leitura desta sessão, e ele é da mesma família do resto: `quinze` era o número certo com **doze** peças. A v0.39 subiu para treze e essa linha ficou.

```
13 de 03-mecanica/  +  conferir-repositorio.py  +  pac7.py  +  v7.py  =  16
```

**E o `conferir-repositorio.py` não alcança essa frase.** Ele confere as três linhas que contam peças e validadores, e não a prosa que diz quantos o script roda. *Número sem dono, errado desde a v0.39.*

### Em aberto

- **As sete propriedades de arma sem texto** — e essa é a dependência dura: enquanto forem só nome na tabela, 15 dos 16 pares da matriz saem `INCONCLUSIVO`, `Haste` e `Tiro pesado` ficam a 0,60 de estarem dominadas pela `Pesada`, e **o validador da peça não pode ser escrito**.
- **O teto de Defesa 20 não tem dono declarado.** O §3 derivou dele e agora a escada de escudos se apoia nele. Derivação virou invariante sem ninguém decidir — a lição nº 9 entrando pela porta de trás. Ou a peça 1 adota, ou Equipamento declara que é dona.
- **Os nomes dos três degraus de escudo.** Livres: Broquel, Pavês, Rodela, Adarga, Tarja, Couraça, Guarda-Corpo.
- **A lista de itens comuns**, e a moeda.
- **As quatro vagas de Desliga da peça 13** que esperam esta peça.
- **A Cicatriz não tem mecânica, só nome.**
- **Energia Reversa, Barreira Simples, Cortina** e a régua da Aptidão Própria.
- **Qual modelo de clash vale.**
- **Nome do sistema.**

---

## [0.40] — 2026-08-12

**Nenhuma regra e nenhum número de jogo mudaram.** Passada de documentação, feita na migração de conta e antes de abrir a peça de Equipamento. Ela existe porque três coisas que a documentação afirmava tinham deixado de ser verdade — e uma delas ensinava a confiar num verde que não confere nada.

### Achado — o "4, 2 e 1" estava errado, e errado para o lado que engana

A v0.38 mediu quantas checagens cada validador pula sem `python-docx` e registrou **4, 2 e 1**. O `README`, o `ESTADO-ATUAL`, o `LEIA-ME` e o `PROMPT-CHAT-NOVO` repetiram. **Lido do código:**

| validador | documentado | é | de quantas |
|---|---|---|---|
| `conferir-nomes.py` | 4 | **3** (checagens 1, 3 e 4) | 5 |
| `conferir-manual.py` | **2** | **4 — todas** | 4 |
| `conferir-pericias.py` | 1 | 1 ✓ | 8 |

**O `conferir-manual.py` estava escrito como o que pula menos e é o único que não confere absolutamente nada:** ele dá `sys.exit(0)` dentro do `except ImportError`, antes da primeira checagem. Quem lesse "pula 2 de 4" ia supor que sobrou metade da cobertura. Sobra zero.

**A causa é de método, e é o que vale guardar:** o 4 do `conferir-nomes` é a contagem da palavra `PULADA` na saída — ele imprime uma linha de resumo e mais três marcadores inline, e a linha de resumo foi contada como se fosse uma quarta checagem. **O número foi tirado da saída do programa em vez do código.** O do `conferir-manual` não bate com nenhuma das duas leituras.

> **Contar sintoma não é contar causa.** A saída de um validador é feita para ser lida por gente no meio do trabalho, não para ser fonte de número que vai para documento. Quando o número for sobre o comportamento do validador, ele se lê do validador.

*Achado rodando o controle negativo com o import bloqueado — a mesma prática que a v0.28 pagou para aprender e que a v0.33 institucionalizou.* A checagem que ninguém tinha feito era a segunda metade dela: **conferir que o número que a gente escreveu sobre a pulada bate com a pulada.**

### Alterado — o `ESTADO-ATUAL` e o `README` estavam parados na v0.38

A v0.39 subiu as contagens (`treze peças e treze validadores`) e a entrada do CHANGELOG, e o `conferir-repositorio.py` passou — porque ele confere **a contagem escrita contra a pasta**, e ela estava certa. O que ele não confere é se as listas e as seções em prosa acompanharam. Não acompanharam:

| onde | dizia | é |
|---|---|---|
| `ESTADO-ATUAL`, cabeçalho | *"na v0.38"* | v0.40 |
| `ESTADO-ATUAL` e `README`, lista de comandos | doze validadores | **falta o `conferir-legados.py`** nas duas |
| `ESTADO-ATUAL` | *"o décimo primeiro é de outra natureza"* · *"os dois últimos precisam de `python-docx`"* | são **três** naturezas fora da regra, e **três** precisam da biblioteca — e não são os últimos |
| `ESTADO-ATUAL` e `LEIA-ME` | *"as seis skills"* | **sete** |
| `README`, a árvore | doze peças · doze validadores · seis skills | treze · treze · sete |
| `ESTADO-ATUAL`, problema de design nº 1 | o teto de magnitude do Legado, aberto | **fechado na v0.39** |
| `ESTADO-ATUAL`, a fila da v0.36 | Legados na frente, por escrever | fechada, e Equipamento é a próxima |
| `ESTADO-ATUAL`, Corpo Amaldiçoado | *"falta aplicar na peça 9 §5"* | aplicado na v0.39 |

**A peça de Legados ganhou seção nova no `ESTADO-ATUAL`**, no lugar do alerta que pedia a régua: os três formatos, os dois Legados por ficha com Destranca obrigatório, e a tabela do que ficou pendurado — **sete vagas de Desliga, quatro esperando equipamento e três esperando dano e condições**, mais a `Armaria` e o `Enterrado`, que citam ferramenta amaldiçoada e são as primeiras a reler quando a próxima peça sair.

### Alterado — a contagem de versões sem playtest saiu de todos os documentos

*A v0.38 deixou isto anotado em aberto e escreveu o conserto certo: **"é derivável da versão atual e não devia estar escrita à mão em lugar nenhum."*** Estava em cinco lugares com dois valores — `README` 35 e 32, `ESTADO-ATUAL` 35 e 32, `LEIA-ME` 35.

Virou **"zero sessões desde a v0.1"** nos três. É a mesma informação, não envelhece, e ninguém precisa lembrar de somar um a cada versão. O `README` também dizia *"38 versões de argumento"*, pelo mesmo motivo e com o mesmo conserto.

E de passagem: o `README` ainda dizia que **`04-playtest/` e `05-material/` estão as duas vazias.** A ficha saiu na v0.35 e o gerador dela está lá — vazia é só uma.

### Registrado — as cinco skills instaladas estavam todas atrás da pasta

A migração de conta obrigou a reinstalar as sete de `sistema/skills/`. **Duas não estavam instaladas** — `gasto-de-modelo` e `pesquisa-antes-de-propor` — e **as cinco que estavam divergiam da cópia do repositório, todas.**

A pior era a `rpg-da-guilda`: a versão instalada ainda mandava rodar de `03-mecanica/` *"porque de outro lugar eles pulam checagem em silêncio"* — **o aviso que a v0.38 saiu para aposentar.**

> **E a deriva inverteu de direção.** Na v0.37 o repositório é que estava atrás, e a conclusão registrada foi *"migrar pelo repositório levaria o gatilho velho"*. Desta vez foi o contrário, nas cinco. **Não existe lado confiável por natureza** — existe a data da última sincronização, e ela não está escrita em lugar nenhum. Continua sendo a camada que nenhum validador alcança.

### Em aberto

- **Equipamento**, a próxima peça — e a proteção primeiro, porque é a que já tem teto fixado por fora: `1` no nível 2 e `4` no refino 10, e uniforme desliga cobrir-se de energia.
- **As sete vagas de Desliga** e o **Não Sou Gente** virando Passiva.
- **A máquina de criação do Sem Técnica** — Aptidão e Estilo da Sombra.
- **A Cicatriz não tem mecânica, só nome.**
- **Uma checagem que conte skill**, que a v0.38 já tinha marcado como candidata e que esta versão acabou de justificar de novo.
- **Energia Reversa, Barreira Simples, Cortina** e a régua da Aptidão Própria.
- **Qual modelo de clash vale.**
- **Nome do sistema.**

---

## [0.39] — 2026-08-12

**A peça 13 fechou.** Legados sai de rascunho e vira peça numerada, com validador junto — **treze peças e treze validadores**. O catálogo tem **81 entradas** contra as catorze de antes, e as quatro que a régua tinha reprovado saíram todas, cada uma com destino escrito.

### Adicionado — `13-legados.md`, as sete listas de Origem

| Origem | Destranca | Ajusta | Desliga escrito | reservado |
|---|---|---|---|---|
| Latente | 4 | 4 | 2 | — |
| Receptáculo | 4 | 4 | 1 | 1 |
| Descendente | 5 | 4 | 1 | 1 |
| Reencarnado | 4 | 4 | 0 | 2 |
| Corpo Amaldiçoado | 4 | **12** | 1 | 1 |
| Feto | 4 | 4 | 1 | 1 |
| Restrição Celestial | **8** | **8** | 1 | 1 |
| | **33** | **40** | **7** | **7** |

Mais o **`Sem Técnica`**, escrito uma vez e compartilhado pelas cinco Origens que o aceitam. **Oitenta e uma.**

### Decidido — o Desliga virou cota de dois, com vaga declarada

*A régua dizia "até 2, teto e não cota", e o Receptáculo e o Descendente fecharam em um por causa disso.* O Mizuki decidiu o contrário: **toda Origem termina com dois Desliga.**

**A conta não fecha hoje, e é por isso que a vaga existe.** Dois por Origem em sete são catorze; a enumeração de alvos legais tem **sete no sistema inteiro, e o `Ferro Velho` gastou o último**. Então: **o Desliga que tem alvo se escreve, o que não tem vira vaga declarada** — e a vaga **nomeia a peça de onde o alvo deve sair**, aparece na tabela junto dos outros, e o validador confere que ela está marcada em vez de conferir que a lista está cheia.

> **Inventar oito alvos agora seria escrever entrada para fechar contagem — que é exatamente o defeito que esta régua nasceu para achar.** Os três Desliga de condição da v0.37 foram escritos porque a coluna pedia, e cada um apagava Condição Maior, que custa Pesada.

**Sete vagas abertas:** quatro esperam **equipamento**, três esperam **dano e condições**.

### Decidido — dois tipos de Destranca, e o mais velho já estava em uso

A cláusula dizia que **todo** Destranca precisa de gatilho que o jogador puxa. A lista do Corpo Amaldiçoado bateu nisso — as quatro configurações de núcleo são identidade, não ação —, e aí apareceu que **o `Sem Patente` do Latente já era assim desde a primeira lista** e passou sem ninguém reparar.

| tipo | o gatilho é |
|---|---|
| **de ação** | uma coisa que o jogador faz, quando quer |
| **de identidade** | a própria escolha, feita uma vez na criação |

**O que segura o segundo tipo é o teste dos 90%, sozinho:** ninguém deixa em branco a linha que diz o que ele é. E a diferença para o **Irmãos**, que a cláusula existia para pegar: *identidade o jogador escolheu; o Irmãos foi escolhido por ele.*

**E um Destranca de identidade não pendura tarefa.** A primeira leva do Corpo Amaldiçoado foi reprovada pelo Mizuki por isso — *"aponte e diga qual das três teria sabido"*, *"escreva três pessoas que só conhecem ela"*, e a pior: *"quem estuda o assunto vai querer saber como"*, que é **enredo tirado do mestre sem ele ter pedido**.

### Achado — o canon reescreveu duas Origens e matou um Legado

**Corpo Amaldiçoado tem energia amaldiçoada.** O `ESTADO-ATUAL` punha ele no mesmo balde da Maki — *"não têm energia, então não têm aptidão nem refino"*. **Cadáver de mutação abrupta produz a própria energia**, uns três meses depois de acordar; o que falta é **técnica**. Ele é misto: **PE, aptidões e refino normais, e Técnica Marcial no lugar do Fundamento.** As Bênçãos e a Lapidação ficam só com a Maki, que é a única de energia zero.

**E os três núcleos não são sabor: são a receita.** Três almas compatíveis num corpo, obrigadas a se observarem, é o que produz autoconsciência e energia própria. Mas **não é a única configuração possível** — cadáver operado por um feiticeiro e cadáver mantido pelo criador também existem. A lista virou quatro configurações — **Ninhada, Gêmeos, Inteiro, Manutenção** —, três com energia própria e uma dependente, e **cada uma gateia três Ajusta próprios**.

**O `Alcance Impossível` morreu.** *"Aja de um lugar em que o seu corpo não está"* é **técnica** — é o que a Manipulação de Fantoche faz —, e a peça 9 proíbe Origem de conceder técnica. Mesmo diagnóstico do `Núcleos` e do `Não Sou Gente`: **não é Legado, é kit de poder.** O que sobrou dele virou o `Nunca Estive Lá` e o `Do Meu Canto`, que são conhecimento e posição, não alcance.

**E o Mechamaru é o boneco.** A peça 9 atribuía a ele a pele que não aguenta sol e os membros que faltam — isso é do **Kokichi Muta**, a pessoa. Corrigido nos dois documentos.

### Achado — a irmandade do Feto é definida por quem te fez

*O `Irmãos` era o piso do catálogo desde a v0.24: o jogador não conseguia disparar, e o efeito era simétrico.* **O conserto não foi inventar gatilho — foi ler o que a irmandade é.** No material, o reconhecimento de irmão **não depende de o outro ser da mesma fabricação**: o mais velho reconheceu como irmão alguém nascido de gente, porque quem os fez foi o mesmo.

> **O gatilho virou o jogador apontar alguém e dizer que é irmão.**

E isso conserta a premissa da Origem junto: *"nem todo Feto é Pintura da Morte"* estava certo e apoiado em nada — **não existe outra categoria de pessoa meio-humana e meio-maldição.** O que existe com nome parecido é **maldição imatura em estágio de útero**, que não é gente e não vira gente. A Origem é *"alguém te fabricou de propósito"*, e Pintura da Morte é o exemplar famoso.

### Decidido — Sem Técnica entra como ponteiro, e precisa de máquina de criação

**Ela não cabe como entrada de catálogo** — tem construção própria em cima —, **e também não pode ficar invisível na camada onde o jogador escolhe quem é.** Entra como **uma entrada de `Destranca` que aponta para fora**, disponível nas cinco Origens que aceitam a sub-origem, **escrita uma vez e referenciada pelas cinco**. Cinco cópias do mesmo texto seria a lição nº 9 dentro de um catálogo.

**E a rota precisa de máquina de criação própria.** Se for só subtração — os outros menos o Fundamento —, ninguém escolhe por vontade: escolhe por castigo.

*O que ela não precisa é de uma economia nova.* **Energia Reversa não é técnica inata**, é manipulação de energia amaldiçoada — e é por isso que quem não tem técnica consegue usar. E o **Estilo da Sombra é anti-domínio, com a espada sendo o jeito mais comum e não o requisito**: a técnica central dele foi aprendida em um mês por quem não usa espada, e a **seção 6.5 da peça 11 já trata o Domínio Simples como aptidão pura**. *A mecânica do projeto estava certa e a prosa da peça 9 estava mais estreita que ela.*

**De 81 entradas, exatamente uma quebra com Sem Técnica:** o `Inédito`, que fala da *sua* técnica. Virou a checagem 9 do validador.

### Adicionado — `conferir-legados.py`, o décimo terceiro validador

Nove checagens, e **nada de valor escrito dentro dele**: os quatro degraus saem da **peça 10**, as Origens saem da **peça 9**, e as contagens saem da própria pasta. O único bloco na mão é o `LIMITES DE DESIGN`, declarado à parte da regra aplicada — lição nº 8. **Não lê o `.docx` e não precisa de `python-docx`**, então não existe caminho por onde ele saia verde tendo pulado checagem.

A checagem 9 é a que mais vai render: **ela recalcula a tabela de totais da peça e falha se o escrito não bater com o contado.** As contas do rascunho já tinham envelhecido duas vezes dentro do próprio arquivo.

**Nove perturbações conferidas, cada uma acendendo a checagem certa** — numa cópia isolada, com a base conferida verde antes e o `diff` conferido em cada uma. Duas não provaram nada na primeira rodada e as duas foram consertadas: um `sed` que não bateu, e a checagem 8, que **acendeu a checagem errada porque estava frouxa** — ela aceitava a palavra *"especiais"* em qualquer lugar da seção. Agora exige as cinco elegíveis nomeadas **e** as duas especiais excluídas.

**E o contra-teste:** renomear um degrau **dentro da peça 10** acende a checagem 2. É a prova de que ele lê do dono em vez de guardar a escada.

### Alterado — o que a peça 13 obrigou a mexer em volta

| arquivo | o que mudou |
|---|---|
| `09-origens.md` | dois Legados; as sete listas viraram ponteiro para a peça 13; Corpo Amaldiçoado ganhou energia; Kokichi no lugar de Mechamaru; Sem Técnica reescrito; a pendência *"se um Legado é pouco"* fechada |
| `08-criacao-de-personagem.md` | dois Legados nos dois lugares, e a Kaori ganhou o segundo |
| `gerador-ficha/ficha.js` e `make.js` | campo do segundo Legado na página 3 |

> **O `.docx` da ficha ficou para trás do código** e precisa ser regerado com `node make.js`. O `conferir-ficha.py` não acusa porque ele confere as constantes de nível 2, e nenhuma delas mudou.

### Em aberto

- **As sete vagas de Desliga**, quando equipamento e dano-e-condições saírem.
- **A máquina de criação do Sem Técnica** — Aptidão e Estilo da Sombra.
- **A Cicatriz não tem mecânica, só nome.**
- **Energia Reversa, Barreira Simples, Cortina** e a régua da Aptidão Própria.
- **Equipamento**, que é a próxima peça da fila.
- **Qual modelo de clash vale.**
- **Nome do sistema.**

---

## [0.38] — 2026-08-12

**Nenhuma regra e nenhum número mudaram.** Esta versão mexe só na camada de procedimento, e ela existe porque a migração de conta obrigou a reler o que a documentação afirma — e duas coisas que ela afirmava tinham deixado de ser verdade.

### Adicionado — a skill `pesquisa-antes-de-propor`

O Mizuki nomeou o defeito: *"toda vez que vou dar continuidade, a primeira coisa é ir no achismo ou com as informações que temos, e poucas vezes é feita busca real na internet, fóruns e afins, a não ser que eu peça."*

**E a instrução já existia.** A `rpg-da-guilda` diz *"pesquise antes de inventar"* — no item 8, sexto bullet de uma lista de sete. Ela nunca disparou.

> **Lembrete enterrado numa lista não é procedimento. Gatilho é.**

A skill nova troca o bullet por **sete casos em que a busca é obrigatória antes de entregar**: afirmar o que outro sistema faz, atribuir modo de falha documentado, afirmar canon, afirmar comportamento de ferramenta, adotar nome novo, dizer que *"ninguém resolve isso"*, e contornar duas vezes o mesmo defeito de ambiente.

**E ela traz a metade que ninguém escreve — o que *não* se pesquisa fora.** Número que um documento do projeto é dono se lê do dono; buscar fora cria a segunda fonte para o mesmo número, que é a lição nº 9 entrando por outra porta. Conta que dá para rodar se roda. Escolha de sabor é do Mizuki, e nenhuma fonte externa decide por ele.

*Escrita depois de rodar a própria receita:* o levantamento de onde procurar por domínio saiu de busca real, e a hierarquia de canon — obra original, depois material oficial complementar, e wiki de fã como **índice e não autoridade** — é a que a preferência de pesquisa dele já pedia, com a checagem de mudança de status junto.

### Achado — o aviso do diretório parou de reproduzir, e ninguém tinha voltado para olhar

O `README` e o `LEIA-ME` diziam, desde a v0.28, que os três validadores que leem o `.docx` o acham *"por caminho relativo à própria posição"* e que, rodados de outro lugar, **pulam checagem em silêncio**. A v0.33 mediu e registrou: **4, 1 e 1 puladas de `/tmp`.**

**Hoje é zero.** Medido nesta versão:

| | de `03-mecanica/` | de `/tmp` |
|---|---|---|
| `conferir-nomes.py` | 61 linhas, 0 pulada | **61 linhas, 0 pulada** |
| `conferir-manual.py` | 94 linhas, 0 pulada | **94 linhas, 0 pulada** |
| `conferir-pericias.py` | 120 linhas, 0 pulada | **120 linhas, 0 pulada** |

Os quatro validadores que abrem arquivo do manual resolvem por `os.path.dirname(os.path.abspath(__file__))`, e **nenhum `conferir-*.py` tem caminho relativo cru**. O conserto entrou em alguma refatoração e nunca foi registrado — então o aviso sobreviveu à causa dele.

**A instrução fica, o motivo muda.** Rodar de `03-mecanica/` continua sendo o certo, porque é o que o `subir.sh` faz e o que o resto da documentação supõe. O que saiu dos três documentos e da skill é a justificativa errada.

> **Aviso que parou de reproduzir é dívida, e é pior que aviso nenhum:** ele ensina a procurar o defeito no lugar em que ele não está mais. Entrou na lista de armadilhas recorrentes da `rpg-da-guilda`.

### Confirmado — a outra pulada é real, e essa fica

Bloqueando o import de `docx` de propósito, os três saem **verdes, com código 0**, e pulam:

| validador | checagens puladas sem `python-docx` |
|---|---|
| `conferir-nomes.py` | **4** |
| `conferir-manual.py` | **2** |
| `conferir-pericias.py` | **1** |

O `conferir-ficha.py` não entra: ele lê o `.docx` com `zipfile`, da biblioteca padrão, desde a v0.35 — não tem dependência para faltar. **`PULADA=0` continua sendo a checagem que vale antes de confiar num "OK".**

### Alterado — a contagem de skills estava parada em quatro

O `README` e o `LEIA-ME` diziam *"as quatro skills"* enquanto o `ESTADO-ATUAL` dizia cinco, desde que a `rpg-da-guilda` entrou na v0.37. **Três documentos, dois números.** Agora são **seis**, e os três dizem seis — divididas em **duas de procedimento** (`rpg-da-guilda`, `pesquisa-antes-de-propor`) e **quatro de assunto**.

*É a lição nº 9 na camada que o `conferir-repositorio.py` não alcança* — ele confere versão do projeto, versão do manual, peças e validadores, e não conta skill. Fica anotado como candidato a checagem, junto com a divergência entre a pasta e a skill instalada que a v0.37 achou.

### Registrado — três contas do `RASCUNHO-legados-regua.md` envelheceram dentro do próprio arquivo

Nada disso muda a régua, que continua fechada. São as contas de fechamento, que ficaram para trás quando a seção 8 decidiu **dez por Origem** depois das listas já estarem escritas:

| onde | diz | é |
|---|---|---|
| §9, abertura | *"primeira leva, com cinco entradas cada"* | Latente 10, Descendente 10 |
| §9, fecho do Latente | *"quatro Destranca · três Ajusta · três Desliga"* | **4 · 4 · 2** — o `Desconfiado` virou Ajusta e o fecho não acompanhou |
| §9, conta final | *"Ajusta 8 · Desliga 4 · Destranca 8"* | **16 · 4 · 14** |
| §10, primeiro item | *"cinco por Origem"* | dez, pela seção 8 |

**A entrada da v0.37 está certa** — ela registra `Latente (10), Receptáculo (9), Descendente (10) e Reencarnado (5)`, que é o que a pasta tem. Quem derivou foi o rascunho contra si mesmo. **Corrigir junto com a outra metade**, para não mexer duas vezes no mesmo arquivo.

### Em aberto

- **O catálogo dos Legados**, três Origens inteiras — Feto, Corpo Amaldiçoado e Restrição Celestial — e o que falta no Reencarnado, que tem 5 de 10 e um Destranca só. **As quatro contas de fechamento acima entram nesse mesmo passe.**
- **Não Sou Gente** é imunidade a dano e a régua reprova; a saída registrada é virar Passiva paga com espaço de feitiço. **Irmãos** é o piso do catálogo e precisa de gatilho do jogador.
- **O validador dos Legados**, que sai junto com a peça — e sobe peças e validadores de doze para treze nos três documentos de uma vez.
- **A Cicatriz não tem mecânica, só nome** — o conteúdo dela é da peça de dano e condições, que não existe.
- **A mudança de um para dois Legados** ainda não chegou na peça 8, na peça 9, no gerador da ficha nem nos dois validadores da ficha.
- **A contagem de versões sem playtest diverge em três lugares** — o `README` diz 32, o `ESTADO-ATUAL` diz 35 num ponto e 32 em outro, o `LEIA-ME` diz 35. É derivável da versão atual e não devia estar escrita à mão em lugar nenhum.
- **A lista de feitos do limiar do nível 20** e a conversão de mestragem.
- **Energia Reversa, Barreira Simples, Cortina** e a régua da Aptidão Própria.
- **Qual modelo de clash vale.**
- **Nome do sistema.**

---

## [0.37] — 2026-08-12

**A pergunta nº 5 do `pitch-de-design.md` fechou.** Ela estava aberta desde a v0.1: *"como o sistema trata morte? JJK é letal; server de guilda com personagem persistente normalmente não é."* Metade dela já tinha resposta e ninguém tinha reparado que era só metade.

### Decidido — o Caído, e o corte entre o que é do mestre e o que é do sistema

| | quem decide |
|---|---|
| **o registro** — a morte cola nesta mesa? | **o mestre**, na abertura. É a trava 6 do `arquitetura.md`, e ela fica como está |
| **a máquina de estado** — o que acontece a 0 de vida | **o sistema.** Zero ocorrências no projeto e no manual antes desta versão |

O corte não foi inventado: o próprio esqueleto justifica a trava 6 dizendo que *"o filtro existe para impedir discricionariedade **nos números**; na ficção é trabalho do mestre"*. **Cair a 0 é número** — muda se você continua com o personagem —, então o registro fica por mesa e a máquina de estado é igual em todas.

> **A 0 de vida você escolhe:** **Aguentar** (apaga, janela de 3 rodadas, cura de 1 te levanta) ou **Insistir** (fica de pé, e cada rodada custa **1/8, depois 1/4, depois 1/2** da vida máxima).
> **Quem levanta ganha uma Sequela**, que encurta a janela da próxima queda. **Na segunda queda vem uma Cicatriz**, permanente.
> **A janela acabou:** estágio 4 de dano de alma.

### Achado — o estado terminal já estava escrito, e era inalcançável

O manual tem quatro estágios de dano de alma, e o quarto diz ***"você não é mais você; o que sobra é decisão do mestre"***. **Isso é a trava 6 com outras palavras**, e ninguém nunca chegou nele: a peça 1 registra que a alma é maior que o corpo em quatro dos cinco Caminhos, então *"a pessoa cai antes"*. Ligar o fim da janela ao estágio 4 destravou a máquina que já existia, sem estado novo e sem contador novo.

### Por que fração da máxima, e não o dano que entra

A versão óbvia — o dano continuar entrando, só que na vida máxima — quebra, porque **vida máxima é justamente o eixo em que os Caminhos divergem 3,2×**:

| perfil | rodadas de pé, se o custo fosse o dano que entra |
|---|---|
| Evocador de Constituição 0 | 3,4 |
| Evocador de Constituição 3 | 5,9 |
| **Bastião de Constituição 6** | **11,0** |

Onze rodadas num combate de 3,7 é *"continue lutando, de graça"*. Cobrando **fração da própria máxima**, a janela fica em **três rodadas para os cinco Caminhos × três Constituições × oito níveis** — e o Bastião paga mais em número absoluto e a mesma fração de si mesmo. O total é 7/8: quem insiste termina a missão com um oitavo do corpo.

### Duas coisas que a conta recusou

**Teste de morte no d20**, no molde de três sucessos contra três falhas: simulado em **41% a 68% de morte por queda**, conforme a CD. Num server em que o mesmo personagem atravessa cinco a sete mesas, isso põe no dado a decisão que a trava 6 já deu para o mestre.

**Degrau de exaustão por queda** — regra caseira popular em outros sistemas, e aqui cabia, porque a peça 10 já tem a escada. Mas o degrau 3 é *desvantagem em ataque e Teste de Resistência*, e uma missão de quatro lutas com duas quedas bate o teto. **Isso é espiral de competência**, que a v0.8 consertou e a peça 10 limitou de propósito.

A distinção virou parte da peça, porque ela é o desenho inteiro:

> **Espiral de competência** — levanta pior, e as suas rolagens pioram. Proibida.
> **Espiral de letalidade** — levanta igual, mas a **próxima** queda está mais perto do fim.

### Registrado — o levantamento que sustentou o desenho

Seis sistemas, e o defeito que o Mizuki nomeou tem nome e literatura: **o vaivém de cair e ser levantado**. O D&D 5e é a origem — qualquer cura de 1 ponto te põe de pé e **não existe consequência nenhuma**. O conserto canônico é o `wounded` do Pathfinder 2e: cada vez que você levanta, a próxima queda **começa** mais perto da morte. O Draw Steel resolve por outro caminho — você não desmaia, continua agindo e se degrada —, e o Daggerheart e o Cairn cobram **cicatriz permanente**.

A causa apontada pela literatura é *"curar antes de zerar é economia de ação ruim"*. **Aqui é pior que no 5e**, por uma frase do manual: *"Cura sem limite de uso por descanso"*. O alvo certo não era proibir a cura — era fazer a **queda** custar alguma coisa que a cura não devolve.

### Adicionado — seis checagens no `conferir-atributos.py`

Elas foram para o validador **dono da peça 1**, e não para um arquivo novo: `conferir-repositorio.py` conta os `conferir-*.py` da pasta contra o número escrito em três documentos, e validador novo quebraria a contagem.

Nada fica escrito na mão — a janela, a escada de custo e a queda da Cicatriz são **lidas do texto da seção 5.5**, e o ritmo de combate vem da seção 8 da mesma peça. Os limites de design ficam declarados à parte, que é a lição nº 8.

**Oito perturbações conferidas**, e a quinta é a que vale registrar: ela saiu **"não acendeu"** e era mentira — o `sed` não bateu porque a linha começa com `> **Sequela` e o padrão ancorava em início de linha. **Vermelho e verde que não provam nada têm a mesma cara**, e a defesa é conferir o `diff` antes de ler o resultado, do mesmo jeito que a v0.35 aprendeu a conferir que a base passa antes de perturbar.

### Adicionado — a régua de magnitude dos Legados, em rascunho

`03-mecanica/RASCUNHO-legados-regua.md`. **Sem número no nome de propósito:** meia peça não é peça, e um arquivo com dois dígitos na frente quebraria a contagem. Ela vira a peça 13 quando o catálogo fechar.

O defeito registrado na v0.24 era magnitude, não quantidade, e **a máquina que o projeto já tinha passava nos catorze** — zero dominâncias estritas pelo teste da peça 3. Ela mede contenção, e o defeito é distância.

A régua não ranqueia: **três formatos, cada um travado nos próprios termos.** `Ajusta` mexe em número e sempre tem relógio da escada da peça 10, com a largura escolhendo o degrau. `Desliga` só apaga o que ninguém comprou. `Destranca` é zero no dado, e precisa de gatilho do jogador **e** de uma afirmação sobre o mundo que só aquele personagem faz.

### Achado — a lição nº 6 pelo avesso, duas vezes

**A primeira:** a régua ia dizer que Desliga *"não dá para precificar, porque o denominador está no Bestiário e o Bestiário não existe"*. Estava errado — eu não tinha procurado. O manual tem **IMUNIDADE** escrito: *"nenhuma Melhoria fura imunidade; quem quiser isso monta uma Passiva de Regra Própria, com limite de uma vez por cena"*, e tem **resistência** definida como metade do dano, *"sempre presa a um tipo"*, cobrada pela Passiva Escama. **A escada existia e o catálogo nunca foi cruzado com ela.**

**A segunda foi o Mizuki quem pegou**, lendo o Legado *Desconfiado*: apagar uma condição é o mesmo problema. O manual precifica **Condição Menor em Média** e **Condição Maior em Pesada** — o tier mais caro que existe. Eu tinha escrito **três** Desliga de condição em duas Origens, e a trava da época — *"não encosta no dano"* — passou nos três.

A trava virou:

> **Um Desliga só apaga o que ninguém comprou.** Dano não, condição não, nem o que qualquer Melhoria concede. Sobra o que o mundo faz com você fora do feitiço.

Os três viraram **vantagem no Teste de Resistência**: mesmo +25 pp no pico, e agora com um dado no meio, para quem pagou Pesada ter chance.

### Decidido — dois Legados por ficha, e um deles é obrigatoriamente Destranca

**O problema:** quando opção de ficção disputa a mesma vaga que opção mecânica, a mecânica ganha. Não é opinião — os Traços, Ideais, Vínculos e Falhas do D&D 5e ficavam em branco cerca de 90% das vezes, e a edição de 2024 removeu os quatro.

**A regra óbvia não conserta.** *Dois de listas diferentes* deixa pegar `Ajusta + Desliga`: quem otimiza continua sem ficção **e a economia mecânica dobra**. Com o Destranca obrigatório ela não dobra — quem otimiza sai com exatamente um Legado com número, e todo mundo passa a carregar uma afirmação sobre o mundo.

**Isto reabre uma linha da peça 9**, que diz *"o conserto é dar mais opções por Origem, não mais Legados por ficha"*. O teto **de poder** continua em um, porque Destranca é zero no dado — mas a mudança ainda precisa chegar na **peça 8, na peça 9, no `ficha.js` do gerador e nos dois validadores que conferem a ficha**. Enquanto for rascunho, a regra antiga é a que vale.

### Achado — o Desliga é teto e não cota, e o motivo é bom

Enumerados os alvos legais do sistema inteiro depois da trava nova: **são sete, e seis já estão usados.** Três por Origem exigiria vinte e um.

**Um Desliga precisa de coisa nomeada existindo antes dele** — e neste sistema quase tudo que acontece com você ou foi comprado por alguém, e aí tem dono, ou é arbitrado na ficção, e aí não há o que desligar. *O suprimento é estreito porque o resto está bem amarrado.* As peças que faltam — equipamento, invocação e Trilhas — é que vão criar alvo novo.

**Alvo por Origem: 4 Destranca · 4 Ajusta · até 2 Desliga.** Escritas: **Latente (10), Receptáculo (9), Descendente (10) e Reencarnado (5)**.

### Alterado — 24 KB saíram do `ESTADO-ATUAL` para a peça 11, e a mudança pegou um erro de seis versões

O documento tinha **63 KB** e truncava na leitura: a seção que o próprio prompt de retomada mandava ler primeiro caía do lado de fora do corte. **Quase 40% dele era o argumento de projeto da peça 11**, fechada desde a v0.27, numa seção ainda chamada *"a próxima peça"*.

*A primeira hipótese estava errada e foi medida:* só **10%** daquelas frases existiam na peça 11 ou aqui, então não era duplicação — era conteúdo único morando no lugar mais caro de ler. Sete das onze subseções foram para a **seção 10 da peça 11**; as outras quatro, que são da Expansão e do manual, ficaram.

**E aí o `conferir-orcamento.py` acendeu na hora.** O bloco movido dizia *"gastando PE"* sem quantidade, e o preço virou **2 PE na v0.30** — a cópia estava congelada seis versões atrás, e sobreviveu porque **nenhum validador varre o `ESTADO-ATUAL`**. Ela era duplicata da seção 6.1 inteira; virou ponteiro, e a peça 11 ficou 966 B menor do que se o bloco tivesse sido colado cru.

`ESTADO-ATUAL`: **61 KB → 49,8 KB.**

### Adicionado — a skill `rpg-da-guilda`, no repositório

`sistema/skills/rpg-da-guilda/`. Ela guarda **procedimento e nunca conteúdo** — ordem de leitura, de onde rodar os validadores e por quê, o que a triagem de nomes não pega, como escrever arquivo neste mount sem ele sumir, o arnês de perturbação e como fechar versão. **Zero números e zero lições copiadas:** ela aponta para o README, senão criaria a lição nº 9 dentro da ferramenta feita para evitá-la.

### Achado — a lição nº 9 acontecendo fora do repositório

A pasta `sistema/skills/` é cópia de trabalho das skills instaladas na conta, e o `ESTADO-ATUAL` sempre avisou que **editar lá não altera a instalada**. Conferindo as cinco na hora de preparar a migração de conta, **uma tinha divergido**: a descrição do `playtesting-rpg` no repositório era a versão antiga e mais longa, e a instalada tinha sido apertada depois.

**Descrição de skill não é enfeite — é ela que decide quando a skill dispara.** Migrar pelo repositório levaria o gatilho velho. Sincronizado.

*Fica registrado porque é o mesmo defeito de sempre num lugar novo:* duas cópias da mesma coisa, numa camada que o `conferir-repositorio.py` não alcança.

### Em aberto

- **O catálogo dos Legados**, três Origens inteiras — Feto, Corpo Amaldiçoado e Restrição Celestial — e o que falta em Receptáculo, Descendente e Reencarnado.
- **Não Sou Gente** é imunidade a dano e a régua reprova; a saída registrada é virar Passiva paga com espaço de feitiço. **Irmãos** é o piso do catálogo e precisa de gatilho do jogador.
- **O validador dos Legados**, que sai junto com a peça.
- **A Cicatriz não tem mecânica, só nome** — o conteúdo dela é da peça de dano e condições, que não existe.
- **A mudança de um para dois Legados** ainda não chegou na peça 8, na peça 9, no gerador da ficha nem nos dois validadores da ficha.
- **A lista de feitos do limiar do nível 20** e a conversão de mestragem.
- **Energia Reversa, Barreira Simples, Cortina** e a régua da Aptidão Própria.
- **Qual modelo de clash vale.**
- **Nome do sistema.**

---

## [0.36] — 2026-08-11

Sem regra nova e sem número novo: esta versão **fecha uma pergunta e ordena quatro peças**. Ela existe porque a pergunta ia voltar, e porque a ordem que parecia certa estava errada.

### Decidido — o Caminho continua sem dar dados de dano

O Mizuki levantou cinco árvores de habilidade, uma por Caminho, e **três delas pediam dado de dano**: a tabela de desarmado do Bastião no molde do monge, a mecânica por grupo de arma da Vanguarda, e o atributo somado ao dano do feitiço no Emanador.

A peça 5 §4 tem duas listas, e a segunda diz o contrário:

> **O que um Caminho não pode conceder:** dados de dano · aumento de Classe de feitiço · Melhoria de graça · cura

**A regra fica.** O motivo é o pilar 1, e já estava escrito: *"se o Caminho desse dano, dois personagens do mesmo Caminho começariam a se parecer, e a técnica que cada um escreveu perderia espaço."* Um sistema em que a identidade mora na técnica não pode ter o Caminho competindo com ela no eixo mais visível de todos.

**Três saídas foram levantadas e a escolha foi a mais estreita:** manter a regra e desenhar dentro dela, em vez de reabri-la com uma régua nova ou abrir exceção só para o dano físico. As duas alternativas custavam reprecificar as peças 5 e 6 e refazer a **paridade conjurador‑guerreiro** — que está calibrada de propósito em `d20 + 3` nos dois lados desde o nível 2, e que o `conferir-atributos.py` vigia.

**E metade do que o Emanador queria já existia, no eixo certo.** A peça 6 §5 concede *trocar o valor fixo de 2 do ataque de conjuração por Inteligência ou Essência*. Isso é **acerto**, não dano, e é neutro porque os dois lados crescem +3 na campanha. A proposta pedia a metade que não cabe; a que cabe estava escrita desde a v0.14.

### Decidido — a ordem das quatro, e ela mudou por dependência

A ordem levantada foi **Legados → Caminhos → Itens → Invocações**. A peça de Caminhos foi para o fim:

| | peça | destrava | depende de |
|---|---|---|---|
| 1 | **Legados** | — | nada |
| 2 | **Equipamento** | a Vanguarda, e a **Técnica Marcial** — duas das três rotas de Origem que não rodam | — |
| 3 | **Invocações** | o Evocador | — |
| 4 | **Caminho, Trilhas e subtrilhas** | o resto | **2 e 3** |

**Duas das cinco árvores não podem ser escritas antes.** A especialização de arma da Vanguarda precisa que arma exista; o benefício de invocação do Evocador precisa que invocação exista — e essa vem com a trava mais dura do projeto já escrita: *você e todas as suas invocações somados entregam uma Rotina*, porque *mais corpos agindo por rodada é a coisa que quebra todo sistema d20, sem exceção*.

**O Guia é o único que passa inteiro**, e não por sorte: *auxiliar, estender, reposicionar e recuperar* é literalmente a lista do que um Caminho **pode** conceder. Ele também fecha a pergunta aberta desde a v0.24 — *o que Elo, Sutura e Perímetro valem contra um golpe por rodada.*

### Registrado — a peça de Legados tem duas metades, e a ordem entre elas importa

O pedido foi **cinco Legados por Origem**, contra os dois de hoje — de catorze para vinte e cinco.

**O defeito registrado dos Legados não é quantidade, é magnitude.** A faixa entre os catorze vai de **Irmãos** (sente outro Feto por perto, zero em rolagem) a **Não Sou Gente** (imune a veneno, doença e ao que ataca corpo humano). A trava escrita — *"não produz dano e não escala com nível"* — **não pega imunidade**.

> **A régua de magnitude vem antes do catálogo.** Multiplicar a lista por quase três sem ela multiplica o defeito junto.

A expansão em si já estava endossada pela própria peça 9, que fecha com *"se o Legado parecer decoração, o conserto é dar mais opções por Origem, não mais Legados por ficha"*. O que muda é só que ela deixou de ser condicionada ao playtest.

### Registrado — as quatro peças caem onde não há validador

Peças **5, 6 e 9**. São três das quatro que nunca tiveram validador — e a quarta, a peça 8, ganhou o dela na v0.34 **depois** de passar sete versões com a Defesa errada e a Trilha faltando.

Não é coincidência: são as peças de catálogo e de prosa, as que não têm curva para conferir. Fica anotado para que cada uma das quatro saia **com validador junto**, e não sete versões depois.

### Em aberto

- **As quatro peças acima**, nessa ordem.
- **A quick-start de nível 2**, que sai depois delas — o sistema fica testável antes de ela existir, mas ninguém senta na mesa sem ela.
- **Os três feitiços da Kaori**, se o exemplo for para ficar completo.
- **A lista de feitos do limiar do nível 20** e a conversão de mestragem.
- **Energia Reversa, Barreira Simples, Cortina** e a régua da Aptidão Própria.
- **Qual modelo de clash vale.**
- **Nome do sistema.**

---

## [0.35] — 2026-08-11

**A ficha de personagem.** `05-material/` estava vazia desde a v0.1, e ela é o primeiro material deste projeto que não é argumento de design — é coisa que alguém preenche.

Três páginas, geradas por código no mesmo molde do manual, em duas versões: **em branco** e **preenchida com a Kaori**.

### A forma, e por que três páginas

O Mizuki pediu **Ficha · Técnica · Lore/referência**, e a divisão faz mais do que caber:

| página | o que carrega | com que frequência muda |
|---|---|---|
| **1 · Ficha** | identidade, atributos, os números derivados, os 4 TRs, as 23 perícias, os 10 ofícios | toda sessão |
| **2 · A técnica** | a Regra, descrição, Famílias, Selo, Passiva Livre, os 2 Classe 0 e os 3 feitiços | uma vez, na criação |
| **3 · Quem é essa pessoa** | aparência, história, o traço da Origem, o Legado, laços, instituição, pacto | devagar |

**A terceira é a que justifica o projeto inteiro.** O problema que este sistema existe para resolver é *o mesmo personagem passar por sete mesas e continuar sendo o mesmo personagem* — e o que faz alguém ser reconhecido numa mesa em que nunca jogou não é a Defesa: é o traço, o Legado, quem lhe deve favor e o que a instituição sabe. Nada nela rola dado.

*A peça 8 promete que a ficha "cabe numa página".* Não cabe: só perícias e ofícios são 33 linhas. A promessa foi medida e desmentida — as três páginas fecham **exatas**, nas duas versões, e isso foi verificado renderizando o `.docx` em PDF e contando.

### A tira de referência é curta de propósito

A página 3 traz sete linhas de consulta — o turno, arredondamento, crítico, os dois golpes, os dois descansos — e **nada além**. CDs, condições e exaustão ficam de fora e vão para a quick-start.

Não é economia de espaço: é a lição nº 9. Uma tabela de CD impressa na ficha e escrita na quick-start são duas cópias do mesmo número, e a ficha é a que ninguém volta para atualizar.

### Os feitiços da Kaori ficaram em branco

A peça 8 não lista os dela, e inventar três aqui seria **escolha de sabor**, que é do Mizuki. Quando forem escritos, entram no `make.js` e o `pac7.py` confere se a montagem fecha no orçamento da Classe 1.

### Adicionado — `conferir-ficha.py`, o décimo segundo validador

A ficha imprime catálogo: 23 perícias com atributo, 10 ofícios, 5 Caminhos com vida e PE, 15 Trilhas, e nove constantes do nível 2. **Cada um é uma cópia de uma peça**, e este projeto já sabe o que acontece com cópia sem dono — a v0.34 acabou de pagar sete versões por uma.

E aqui é pior que num `.md`: **ficha errada não fica num arquivo que ninguém abre. Ela vira personagem, em sete mesas ao mesmo tempo.**

Seis checagens, e o `gerador-ficha/dados.js` é **cópia declarada** — a autoridade é a peça, e o validador falha quando os dois discordam.

**Nove perturbações conferidas**, todas acendendo a checagem certa: perícia sumindo da ficha, ofício inventado, PE do Bastião mudando só na ficha, Trilha que a peça 6 não tem, refino indo a 4, XP divergindo da peça 12, o `.docx` sumindo, **a peça 7 ganhando perícia e a ficha não acompanhando** — que é o caso real — e o `.docx` publicado ficando para trás do código.

### Corrigido de método — uma checagem que não podia acender, e um arnês que acendeu pelo motivo errado

**Duas armadilhas da casa, nas duas direções, na mesma versão.**

A primeira: a checagem de *"o `.docx` publicado é mais novo que o gerador?"* comparava **mtime**, e ela **não acendeu** na perturbação — este mount carimba data de arquivo de um jeito que não dá para confiar. É a lição nº 8: checagem que não pode acender é pior que checagem nenhuma. Ela foi trocada por uma que lê o **conteúdo** — abre o `.docx` como zip (com `zipfile`, biblioteca padrão, sem dependência para faltar) e confere se o texto traz a proteção, a Integridade e o XP atuais. Assim reformulada, ela acende.

A segunda, pelo lado oposto: o primeiro arnês de perturbação montou a cópia com os diretórios chamados `03` e `05` em vez de `03-mecanica` e `05-material`. **As oito perturbações acenderam — todas porque o validador não achava os arquivos.** Oito vermelhos que não provavam nada, e que pareciam prova. É exatamente o que aconteceu na v0.28 rodando de `/tmp`, e a defesa é sempre a mesma: **conferir que a base passa antes de perturbar.**

### Em aberto

- **A quick-start de nível 2**, enxuta. É a última coisa entre o sistema e uma mesa de verdade.
- **Os três feitiços da Kaori**, se o exemplo for para ficar completo.
- **Um validador para as peças 5 e 9**, que continuam sem nenhum.
- **A lista de feitos do limiar do nível 20** e a conversão de mestragem.
- **Energia Reversa, Barreira Simples, Cortina** e a régua da Aptidão Própria.
- **Qual modelo de clash vale.**
- **Nome do sistema.**

---

## [0.34] — 2026-08-11

A varredura das doze peças, pedida antes de a ficha ser construída. **Dois erros, os dois com sete versões de idade, e os dois na faixa que a ficha ia usar.**

E o achado que vale mais que os dois: **as peças com validador estavam limpas.** Peças 1, 3, 4, 7, 10, 11 e 12, todas certas. Os dois erros estavam nas peças 6 e 8, que não tinham nenhum.

### Achado — a Defesa da ficha de nível 2 estava errada desde a v0.27

A v0.27 deu número a *cobrir-se de energia*: **`1/3 do refino + 1` de proteção**, grátis no refino 1, sem uniforme nem armadura. No refino 1 isso é **proteção 1**, e toda ficha de nível 2 tem.

A peça 8 é da v0.21. Ela dizia proteção **0**, em dois lugares, e a ficha de exemplo fechava `10 + 2 + 0 = 12`.

> **A Defesa de nível 2 é `10 + Destreza + 1`. A ficha da Kaori é 13.**

**E o mais revelador: a matemática de balanço já rodava supondo proteção 1.** A peça 1 mede o caso difícil contra *"alvo que também investiu em Destreza e tem proteção 1"*, e a checagem 1 do `conferir-atributos.py` roda com `protecao 1` desde sempre. Quem estava fora de sincronia era só a peça que publica a ficha — então o conserto é de texto, e nada foi rebalanceado.

*E ela deixa um recado para a peça de equipamento, mais forte do que o que já estava escrito:* como uniforme, armadura e escudo **desligam** a proteção de energia, a tabela de proteção não compete com 0 — ela compete com 1 no nível 2 e com 4 no refino 10.

### Achado — a decisão da Trilha ficou sete versões escrita e não aplicada

O `ESTADO-ATUAL` registra desde a v0.27:

> *"A Trilha é identidade, como o Caminho, e nasce com o personagem. **Corrigir na peça 6, na peça 8 e aqui.**"*

**Nenhum dos três foi corrigido.** A peça 6 continuava dizendo que *"as escolhas de nível compram Trilhas"*, a peça 8 listava *"não afeta o nível 2"* entre as pendências, e o `ESTADO-ATUAL` **se contradizia sozinho** — a seção da decisão dizia uma coisa e duas tabelas mais abaixo diziam a outra.

Aplicado agora nos três. A primeira Trilha vem na criação, junto do Caminho; as seguintes se acumulam com o nível, e quantas e quando continua sendo a peça de Trilhas.

> **E o que ela entrega ainda não tem número, e o texto diz isso.** Escolher a Trilha no nível 2 não custa nada e não tranca nada — ela é o nome e a frase de uma linha até a peça sair.

**A lição que sai daqui é nova, e não é a nº 9:** *decisão registrada não é decisão aplicada*. O CHANGELOG e o `ESTADO-ATUAL` são bons em guardar o **porquê**, e nada no projeto conferia se o **o quê** tinha chegado nos arquivos. Uma decisão que termina em *"corrigir em três lugares"* precisa de alguém conferindo os três.

### Adicionado — `conferir-criacao.py`, o décimo primeiro validador

**Ele confere instância, e os outros dez conferem regra.** Essa é a diferença inteira, e é o buraco por onde os dois erros passaram:

| | pergunta |
|---|---|
| os dez primeiros | *a fórmula deriva certo?* |
| **o décimo primeiro** | ***a ficha publicada obedece à fórmula?*** |

A peça 8 é a única que produz uma ficha inteira com número fechado. Ela soma o que sete outras peças decidiram — e envelhece toda vez que uma delas mexe num número, sem que nada acuse.

Sete checagens: a ficha de exemplo sai das fórmulas; o bloco de fórmulas do passo 7 bate com a peça 1; nenhuma peça afirma proteção 0; a criação entrega Trilha; a contagem de feitiços do nível 2 fecha; as duas rotas de perícia e ofício somam igual; e Caminho, Trilha e Origem citados na criação existem nas peças donas.

**Nenhum valor fica escrito dentro dele** — a proteção é lida da peça 11, a maestria e o refino da peça 8, os Caminhos da tabela do passo 3, o XP da peça 12. E ele não lê o `.docx`, então não tem por onde sair verde tendo pulado checagem.

**Oito perturbações conferidas**, numa cópia isolada, cada uma acendendo a checagem certa: a Defesa voltando para 12, a proteção 0 voltando ao texto, a Trilha saindo da criação, cobrir-se deixando de ser gratuita, os feitiços voltando para dois, os atributos somando 10, e a ficha usando uma Trilha que não existe. **A oitava é a que importa:** mudar a fórmula na **peça dona** — `1/3 do refino + 2` — acende o erro na ficha, o que prova que ele lê do dono em vez de guardar o número.

### Registrado — o sumiço de arquivo tem causa, e ela é acionável

Seis ocorrências em duas versões, e a v0.34 isolou o gatilho:

| quem grava | o bash lê de volta |
|---|---|
| o **bash** | **sempre** |
| a ferramenta de escrita do assistente | às vezes não — ENOENT com `ls` e `stat` certos |

O `conferir-criacao.py` nasceu invisível para o próprio `python3` e precisou ser reescrito pelo bash com `cat > arquivo <<'EOF'`. **Fica como procedimento: código novo se escreve pelo bash.** Para `.md` a ferramenta serve, e uma segunda escrita reconcilia quando o sumiço acontece — o `README.md` e o `LEIA-ME.md` caíram juntos três vezes e voltaram nas três.

O conteúdo nunca esteve em risco em nenhuma das seis.

### Em aberto

- **A ficha de personagem e a quick-start de nível 2**, que é o que esta varredura estava limpando o caminho para.
- **Um validador para as peças 5 e 9**, que continuam sem nenhum.
- **A lista de feitos do limiar do nível 20.**
- **A forma da conversão de mestragem.**
- **Energia Reversa, Barreira Simples, Cortina** e a régua da Aptidão Própria.
- **Qual modelo de clash vale.**
- **Nome do sistema.**

---

## [0.33] — 2026-08-11 · *manual v7.8 regerado*

A passada de validação e polimento que a rota previa depois da XP. **A matemática estava limpa e a prosa não** — e o pior achado não estava em documento interno nenhum: estava na capa do manual.

### Os treze passam, e passam de verdade

Rodados de `sistema/03-mecanica/`, com o controle negativo que a v0.28 pagou para aprender: os três que leem o `.docx` saem com **zero** `PULADA` do lugar certo e com **4, 1 e 1** rodados de `/tmp`. O verde é verde. Nenhum número precisou mudar nesta versão — é a primeira em cinco em que isso acontece.

### Achado — a capa do manual dizia "Versão 7.5"

> **`partA.js` nunca foi atualizado desde a v7.5. O `.docx` que a Guilda abre trazia 7.5 na capa enquanto o projeto inteiro dizia v7.8.**

Três versões do manual (v7.6, v7.7 e v7.8) e **sete versões do projeto** (da v0.26 à v0.32) mexeram no conteúdo e ninguém tocou na string da capa. Nenhum validador olhava para ela.

**E ela é a pior cópia possível para deixar derivar**, porque é a única que sai do repositório. Todo o resto da deriva desta versão é conversa entre quem trabalha no sistema; a capa é o que um jogador vê.

Consertado no gerador e **o manual foi regerado**. O diff é exatamente uma string: 363 parágrafos e 84 tabelas antes e depois. **O `.pdf` continua na v7.4**, como sempre — ele é exportado à mão.

### Achado — a deriva, medida

| documento | afirmava | é |
|---|---|---|
| **capa do `.docx`** (`partA.js`) | **Versão 7.5** | 7.8 |
| `manual/matematica/COMO-USAR.txt` | Fundamento v7.6 | 7.8 |
| `sistema/LEIA-ME.md` | **v0.27** · onze peças · **sete** validadores · manual v7.6 | v0.32 · doze · dez · v7.8 |
| `arquitetura.md` | manual v7.6 | v7.8 |
| `ESTADO-ATUAL` · seção do manual | v7.6, 328 parágrafos, 76 tabelas | v7.8, **363**, **84** |
| `ESTADO-ATUAL` · o material medido | 25.600 palavras em dez peças · 22.000 no CHANGELOG · 2.070 linhas em seis validadores | **34.200** em doze · **32.000** · **3.880** em dez |
| `ESTADO-ATUAL` · o que falta | tabela de XP *"nunca foi escrita"* | peça 12, fechada na v0.31–v0.32 |
| `ESTADO-ATUAL` · a fila | *"nunca foi escrita"* **e** *"fechada na v0.31 e v0.32"* | **o mesmo arquivo, duas respostas** |
| `ESTADO-ATUAL` · dezessete coisas | doze existem, XP entre as que faltam | **treze**, e faltam quatro |
| `ESTADO-ATUAL` · passo 6 de 6 | *"a próxima da lista original"* | fechado desde a v0.23 |
| `ESTADO-ATUAL` · playtest | zero sessões em **26** versões | 32 |
| `ESTADO-ATUAL` · lições | **cinco** | o README tem **nove** |
| `README` · o que não existe | a tabela de XP, trava nº 1 | existe |

**O `LEIA-ME.md` é o caso mais caro**, porque ele é o mapa da pasta: cinco versões parado, anunciando um sistema com onze peças e sete validadores para quem chega agora.

### Corrigido — a lista de lições tinha duas cópias, e elas divergiram

O `ESTADO-ATUAL` guardava a própria lista, parada em **cinco** enquanto o README chegava a **nove**. E a lição nº 2 da cópia ainda listava *"v0.16, v0.17, v0.19, v0.24 e v0.26"* quando o original já contava sete versões.

**É a lição nº 9 acontecendo dentro do documento que existe para avisar sobre ela.** A cópia saiu e virou ponteiro: as lições moram no README, e só lá.

### Adicionado — checagem 4 do `conferir-repositorio.py`

> **Todo número que mora em mais de um documento tem um dono declarado, e cada cópia é conferida contra ele.**

| número | dono | por quê |
|---|---|---|
| **versão do projeto** | a entrada do topo do `CHANGELOG` | é a única que não dá para escrever errado sem querer — ela só existe depois de a versão fechar |
| **versão do manual** | a primeira linha de `manual/gerador/COMO-USAR.txt` | o `.docx` é **saída**. Quando os dois discordam, quem está errado é a capa, e o conserto é regerar |
| **peças e validadores** | a pasta `03-mecanica/` | já era assim para o README desde a v0.28; agora vale para o `ESTADO-ATUAL` e o `LEIA-ME` também |

São **onze cópias** conferidas, e **nenhum dos valores fica escrito dentro do validador** — a armadilha que ele mesmo caiu na v0.28, quando guardava `sete`.

Ele também **não lê o `.docx` e não precisa de `python-docx`**, então não existe caminho por onde ele saia verde tendo pulado checagem. Isso foi de propósito: a checagem que nasceu para pegar a lição 9 não podia nascer com a lição 8 dentro.

**Cinco perturbações conferidas**, cada uma acendendo a checagem certa e nomeando o arquivo culpado: capa voltando para 7.5, `LEIA-ME` voltando para sete validadores, `ESTADO-ATUAL` voltando para onze peças, dono sem valor legível — e o caso que apareceu sozinho enquanto eu escrevia esta entrada: **subir a versão nos três documentos antes de registrar a entrada do CHANGELOG acende três erros.** Essa última é uma trava de graça que ninguém desenhou: não dá mais para anunciar versão que não foi registrada.

*Rodadas numa cópia isolada do repositório, e não nos arquivos reais* — perturbar em cima do original e restaurar depois é como se perde trabalho num mount que já engoliu arquivo quatro vezes.

### Registrado — o mount perdeu dois arquivos, e o README já sabia

Aconteceu **duas vezes** nesta versão: com o `README.md` e o `LEIA-ME.md` juntos, e depois com o próprio `conferir-repositorio.py`, sempre logo depois de uma escrita. Sintoma idêntico ao da v0.28 e da v0.29 — `ls` e `stat` com tamanho e inode certos, `open()` devolvendo **ENOENT**, vizinhos abrindo normalmente.

**Conteúdo íntegro no disco nas três vezes, e uma escrita nova reconciliou nas três.** Fica registrado porque agora são quatro ocorrências em seis versões: não é acidente, é o mount, e o procedimento do README funciona.

### Achado — o mesmo mount quebra o git inteiro, e não só o commit

O README dizia que o assistente não consegue **commitar**. Ele também não consegue **ler**: `git status`, `git log` e `git fsck` saem todos com `fatal: loose object <sha> is corrupt`.

**Não é o repositório.** Medido:

| | conta |
|---|---|
| objetos soltos em `.git/` | 241 |
| que o `ls` mostra com tamanho certo | **241** |
| que o `open()` consegue abrir | 175 |
| que devolvem **ENOENT** | **66** |
| arquivos de trabalho no mesmo estado | 1 (o `mensagem-de-commit.txt`, reconciliado) |

É a mesma falha de sempre, agora medida em escala e dentro do `.git/`. **Fora do sandbox o git funciona normalmente**, e o perigo aqui é de interpretação: quem lê "corrupt" e roda `git gc` para consertar está tentando consertar um repositório que não está quebrado.

**E rodar `git status` daqui cobra um preço:** ele cria um `.git/index.lock` que o mount depois não deixa apagar, e um lock preso trava o `./subir.sh`. Aconteceu nesta versão e foi limpo. Está no README, junto com a conclusão: **não rodar git do sandbox.**

### Em aberto

- **Ficha de personagem e quick-start.** `05-material/` continua vazia, e agora não tem mais nada na frente.
- **A lista de feitos do limiar do nível 20.**
- **A forma da conversão de mestragem.**
- **Energia Reversa, Barreira Simples, Cortina** e a régua da Aptidão Própria.
- **Qual modelo de clash vale.**
- **Nome do sistema.**
- **O `.pdf`, na v7.4.** Quatro versões de manual atrás — e desta vez a capa do `.docx` mudou, então a diferença ficou visível.

---

## [0.32] — 2026-08-11

O Mizuki olhou a curva da v0.31 e disse duas coisas: que ela não fazia **progressão nível a nível**, e que subir três níveis numa missão *"não traz uma metodologia de jogo bom"*. Pediu pesquisa em fórum e em sistema de guilda de verdade.

**Ele estava certo, e o precedente é mais forte do que a intuição dele.**

### Achado — o defeito que derrubou o XP na maior campanha compartilhada do mundo

A **D&D Adventurers League**, com cerca de 100 mil membros, abandonou experiência na temporada 8, em 2018. O motivo documentado é literalmente o caso que o Mizuki descreveu:

> *"Uma aventura de quatro horas levava um personagem novo do nível 1 ao 3 — mais rápido do que os designers pretendiam."*

E o defeito espelho junto: *"jogadores ficavam presos no nível 4 por muito tempo, porque o XP era fixo por faixa e não ajustado ao nível."*

**A nossa curva tinha exatamente o primeiro.** Medido: um final de arco jogado por um personagem de nível 2 entregava **três níveis de uma vez**.

### Achado — os dois grandes sistemas de jogo organizado convergem numa coisa que a nossa curva não tinha

| | como conta |
|---|---|
| **Adventurers League** | 4 checkpoints por nível até o 4, 8 dali em diante · 1 checkpoint por hora |
| **Pathfinder Society 2e** | 12 XP por nível, cenário paga 4 — **três cenários por nível**, sempre |

**Os dois compram a mesma propriedade: o custo de um nível é um número inteiro pequeno de sessões, legível sem tabela.** *"Estou no nível 12, cada nível são quatro missões, joguei duas."*

A reta da v0.31 — `100 + 30 × (nível − 2)` — dava 1,3 missão no nível 3, 1,6 no 4, 2,8 no 8. **Só o nível 2 caía redondo.** Todo o resto pedia conta.

### Decidido — a curva vira degrau, e ele sobe a cada três níveis

> **Um nível custa um número inteiro de missões padrão, e o número sobe uma a cada três níveis.**

| níveis | custa | | níveis | custa |
|---|---|---|---|---|
| 2 a 4 | 1 missão | | 17 a 19 | 6 |
| 5 a 7 | 2 | | 20 a 22 | 7 |
| 8 a 10 | 3 | | 23 a 25 | 8 |
| 11 a 13 | 4 | | 26 a 28 | 9 |
| 14 a 16 | 5 | | 29 | 10 |

**Ela mantém as duas propriedades da v0.31 e ganha a terceira.** Continua crescendo — que é o que fecha o abismo entre quem jogou e quem sumiu, e é a razão do XP ser fixo. E agora é legível de cabeça.

*Por que não a curva plana da Pathfinder Society:* com custo plano **ninguém alcança ninguém**, porque todos sobem no mesmo ritmo para sempre. A PFS resolve isso com faixas de nível por cenário — mesa aberta de guilda não tem esse luxo. Perturbei o validador para plano e ele acende.

### Decidido — nenhuma missão dá mais de um nível

> **Você sobe no máximo um nível por missão. O XP que sobrar fica acumulado e sai na próxima.**

**O excedente não some**, e isso é o que faz o teto não tirar nada de ninguém — ele só espalha. Quem levou um final de arco no nível 2 sobe na hora e entra na missão seguinte com 200 XP no bolso.

**E ele quase não atrasa nada.** Simulado com missão padrão, com teto e sem teto dão o mesmo nível em 10, 20, 40, 60 e 80 missões — porque com missão padrão o teto nunca chega a morder. Ele é rede de segurança para o caso grande.

### Os números novos

| | v0.31 | v0.32 | alvo |
|---|---|---|---|
| 2 → 20 | 6.390 XP · 60 missões | 6.300 XP · 59 | 60 |
| 20 → 30 | 7.750 XP · 32 | **8.200 XP** · 34 | 32 |
| joga pouco | 13,9 meses | 14,5 | 14 |
| mediano | 9,3 | 9,7 | 9 |
| joga muito | 5,1 | 5,3 | 6,5 |

### Corrigido de método — a mesma cegueira pela terceira vez em três versões

A checagem do teto comparava o resultado contra `TETO_NIVEIS_POR_MISSAO` — a **própria constante que ela deveria vigiar**. Subir a constante subia a régua junto, e a perturbação saía verde.

É o terceiro exemplar da mesma espécie em três versões seguidas:

| versão | onde | o que a checagem não via |
|---|---|---|
| v0.28 | dominância das três rotas | o eixo dos feitiços, que era o da pergunta |
| v0.30 | upkeep das anti-domínio | a constante, porque `1.0` estava escrito na mão |
| **v0.32** | teto de níveis por missão | a própria constante, por auto-referência |

**O conserto é sempre o mesmo:** separar *a regra aplicada* do *limite de design*. Agora `MAXIMO_DE_DESIGN = 1` é declarado à parte, e a checagem falha se a regra passar dele **ou** se o resultado passar.

**Nove perturbações conferidas** no `conferir-xp.py`, três delas novas: teto removido, custo deixando de ser inteiro, e curva plana.

### Em aberto

- **A lista de feitos do limiar do nível 20.**
- **A forma da conversão de mestragem.**
- **Energia Reversa, Barreira Simples, Cortina** e a régua da Aptidão Própria.
- **Qual modelo de clash vale.**
- **Nome do sistema.**

---

## [0.31] — 2026-08-11

**A tabela de XP.** A trava nº 1 de mundo compartilhado — *"XP tabelado, nunca marco narrativo"* — ficou aberta por trinta versões, e é a última coisa que separava o sistema de ser jogável de ponta a ponta.

E é a **primeira peça deste projeto escrita a partir de dado de gente real**: catorze opiniões da Guilda sobre quanto tempo a subida deve levar. **Décimo validador**, e ele confere uma coisa que nenhum outro confere — que a regra continua produzindo o *tempo* que as pessoas pediram.

### O levantamento, medido

Mediana de **10,25 meses** para o 2→20 e **4,1** para o 20→30, razão **0,45**. O Mizuki punha o mediano em 9 meses e a razão em 0,61 — um pouco mais rápido que o grupo, com o "joga pouco" dele batendo no teto de quase todo mundo.

**Todas as catorze concordaram numa coisa só:** a faixa lendária é mais curta em tempo, apesar de ter dez níveis contra dezoito.

### Decidido — XP fixo por missão, e a razão é uma propriedade de guilda

> **A missão paga o mesmo para todo mundo na mesa, independente do nível de quem recebe.**

Numa guilda, mesa aberta junta nível 8 com nível 14 — não é exceção, é terça-feira. Simulado: dois personagens começam juntos, um perde dez sessões, depois jogam tudo junto.

| depois de | XP fixo | XP escalado pelo nível |
|---|---|---|
| 20 sessões | 4 níveis | 4 |
| 40 | 2 | **4** |
| 90 | **1** | 0 |

**Com XP fixo a distância só encolhe**, e é aritmética pura: cada nível custa mais que o anterior, então a mesma missão vale uma fatia menor para quem está na frente. Ninguém recebe nada de especial — o atrasado só precisa de menos.

**Com XP escalado ela trava**, e só fecha quando alguém encosta no teto de nível. É o **gap** que o Kekka descreveu: *"tiveram players literalmente bloqueados de ganhar gap de tão mutantes que eram."*

### Decidido — "Grau dá mais XP" bate numa decisão de arquitetura

A proposta que apareceu no levantamento foi a de D&D: inimigo de grau mais alto paga mais. **A intuição está certa e o alvo está errado** — missão difícil já vale mais, pelo tamanho dela.

E se o **Grau** desse XP, ele quebraria uma separação que o `arquitetura.md` fez de propósito: *"todo personagem começa Grau 4, e a patente sobe por **feito**"*, *"o Yuta é Grau especial, Nível baixo"*. Grau é reconhecimento; nível é poder. Juntar os dois vira espiral fechada — sobe de patente, sobe de nível mais rápido, ganha patente por feito.

### A curva, e o tamanho da missão

> **XP para subir = `100 + 30 × (nível − 2)`** — 100 no nível 2, 640 no 20, 910 no 29.

Reta de propósito: um mestre confere de cabeça que *"o próximo custa trinta a mais"*. Exponencial daria o mesmo efeito e uma tabela consultada toda vez.

| missão | paga |
|---|---|
| curta / roleplay | 50 |
| padrão | 100 |
| longa | 200 |
| final de arco | 300 |

**Uma curva só, e quem varia é a missão** — e é isso que faz a faixa lendária ser mais rápida sem nenhuma regra de exceção:

| faixa | XP | missões |
|---|---|---|
| 2 → 20 (18 níveis) | 6.390 | ~60 |
| 20 → 30 (10 níveis) | **7.750** | **~32** |

Dez níveis lendários custam **mais XP** que dezoito mundanos e levam **metade das missões**, porque lá em cima a Guilda roda final de arco.

**E missão de roleplay paga.** Uma guilda que só dá XP para quem mata perde metade do que a faz ser guilda.

### Decidido — retorno decrescente, e não teto

> **As duas primeiras missões da semana pagam cheio. A terceira paga metade, a quarta metade disso, e assim por diante.**

100% · 100% · 50% · 25% · 12% · 6%.

**Ninguém sai com zero, e essa é a razão de ser decrescente.** A escolha entre teto duro e decrescente foi do Mizuki, e o argumento é de mesa e não de planilha: *"por mais que o foco deveria ser jogar e ter história, é garantido que reclamariam de acabar tendo XP zero."* Um teto produziria a sessão de seis horas que termina em nada.

**O que ele resolve** veio pronto do levantamento, do Mega: *"muita gente só mestra pelo XP e isso vira cúmulo."* Quando a terceira mesa da semana vale metade, moer mesa para de compensar sozinho, sem proibição e sem fiscal.

| perfil | mesas/semana | 2 → 20 | o alvo |
|---|---|---|---|
| joga pouco | 1 | 13,9 meses | 14 |
| mediano | 1,5 | 9,3 | 9 |
| joga muito | 4 | **5,1** | 6,5 |

**O terceiro fica um mês e meio na frente, e isso está registrado e não consertado.** Puxá-lo para trás exigiria dar cheio só na primeira missão da semana — e aí quem joga uma vez por semana perde metade, que é exatamente quem não se quer punir. Sem o decrescente ele chegaria em 3,5 meses.

### Decidido — mestrar não dá XP

> **Mestrar paga na moeda que o sistema já tem separada: patente, contato, favor, acesso.**

A decisão mais impopular da peça e a de argumento mais curto: se mestrar paga XP, mestrar vira a rota ótima de subir, e quem mais dirige o mundo é quem menos joga nele.

*Fica em aberto:* uma conversão pontual depois de muitas mesas mestradas — **um bônus por marca, nunca por sessão**.

### Decidido — o limiar do nível 20

> **Você chega ao 20 por XP. Você passa dele por feito.**

Pedido pelo Zeuk e pelo Soler, e o argumento não é de balanceamento: *"tirar a ilusão do 'cheguei no lvl 20 pro 21 em 4 meses enquanto fulano upou 7 níveis'."*

Ele encaixa numa coisa que o sistema já tinha — a patente sobe por feito — e é **o único lugar onde o eixo social e o de poder se tocam**, uma vez só, na fronteira do mundano com o lendário. O XP continua acumulando e nada se perde.

**A lista de feitos fica em aberto**, e ela precisa ser fechada no molde do ambiente propício: entradas escritas, palavra final do mestre em cima delas.

### Decidido — falhar paga metade ou nada, e o mestre escolhe

Faixa e não número, porque azar de dado não é a mesma coisa que abandono. **O piso é metade e não zero** — seis horas que terminam em nada fazem a pessoa não voltar; **o teto é metade e não cheio** — senão o sucesso deixa de significar. Discricionariedade assumida, no molde do *"o mestre declara o que foi uma luta"*.

### Adicionado — `conferir-xp.py`, o décimo validador

Cinco checagens, e uma delas é inédita no projeto: **ele confere que a regra ainda produz o tempo que a Guilda pediu**, com tolerância declarada por perfil. Se alguém mexer na curva ou no tamanho das missões, ele diz de quanto o alvo saiu.

**Seis perturbações conferidas**: curva plana, curva decrescente, decrescente virando teto duro, missão padrão dobrada, faixa lendária ficando mais longa que a mundana, e o decrescente frouxo demais.

**E ele pegou um critério errado meu antes de fechar:** eu exigi distância **zero** entre o atrasado e o líder em 120 sessões, e 120 sessões não alcançam o teto de nível. O invariante certo é a distância **encolher sempre e terminar pequena** — ela zera em 160 sessões, depois do fim de uma campanha, o que na prática quer dizer um nível de folga.

### Em aberto

- **A lista de feitos do limiar do nível 20.**
- **A forma da conversão de mestragem.**
- **Energia Reversa, Barreira Simples, Cortina** e a régua da Aptidão Própria.
- **Qual modelo de clash vale**, e os seis números do push.
- **Nome do sistema.**
- E a fila mudou: com a XP escrita, **o que falta para alguém jogar é ficha e quick-start.**

---

## [0.30] — 2026-08-11 · *manual v7.8*

O Mizuki notou uma coisa e ela derrubou o método de três versões seguidas: **todo cálculo de custo em PE deste projeto mediu uma peça sozinha contra o bolso inteiro.** Uma ficha de verdade gasta tudo ao mesmo tempo.

**Nono validador**, e ele é o primeiro que responde *"cabe tudo junto?"*.

### Achado — o erro não era de conta, era de modelo

Quando a v0.29 escreveu *"1 × Classe por rodada cabe em 3 a 4 lutas"*, o personagem dessa conta segura uma postura defensiva e **não conjura nada**. Isso não é um personagem: é uma estátua. O mesmo vício está nas contas de PE da v0.28 e da v0.27.

**E ele era invisível para os onze validadores**, porque cada um mede uma peça contra a régua dela. Nenhum somava. É a maior das três cegueiras achadas nesta semana — as outras foram a checagem de dominância que não via o eixo dos feitiços e o `1.0` escrito na mão dentro do laço.

### Corrigido de método — e a correção corrigiu a correção

A primeira soma que eu apresentei dizia que segurar uma anti-dominío e conjurar custava **136% do dia** de um Bastião no nível 22, ou seja, era impossível. **Esse número também estava errado**, e pelo lado oposto: ele supunha conjurar **toda rodada**.

> **Conjurar toda rodada nunca coube, com ou sem upkeep.** O bolso só dá para conjurar em **38% a 48%** das rodadas do dia num Bastião, e 57% a 76% num Emanador.

O upkeep é 20% do custo de uma rodada; o feitiço é 80%. Eu culpei o upkeep por um estouro que já existia sem ele. **Segurar durante um domínio inteiro sempre coube: 1 a 1,7 feitiços, 21% a 34% do dia.**

E a economia já pressupõe essa folga de propósito — o resto das rodadas vai para Classe 0, golpe simples e projetar energia, que não custam nada. Isso não é aperto: é o desenho.

### Decidido — o preço das anti-domínio fica como estava

O Mizuki pediu para reduzir o upkeep pela metade e reavaliar. A reavaliação achou uma coisa que ninguém tinha visto: **são duas travas diferentes, e elas puxam para lados opostos.**

| | o que ela faz |
|---|---|
| **custo de ativar** | pune ligar sem precisar — é afundado, some se a luta não vem |
| **upkeep** | limita quanto tempo você segura — **quanto menor, mais tempo ligado** |

Baixar só o upkeep **alarga** a janela de pré-ligamento, que era exatamente o que ele queria fechar: de 2,4 para 4,9 min.

Seis candidatos foram medidos no somatório:

| | um domínio (nv22) | do dia | feitiços que sobram | pré-ligado |
|---|---|---|---|---|
| **A** `0×` ativar · `1×` upkeep | 30 | 34% | 3 | **2,4 min** |
| B `0×` · `0,5×` | 15 | 17% | 4 | 4,9 min |
| C `2×` · `0,5×` | 27 | 31% | 3 | 4,2 min |
| E `2×` · `0,75×` | 37 | 42% | **2** | 3,1 min |
| F `1×` · `1×` | 36 | 41% | **2** | 2,7 min |

**A e C passam nos três invariantes; E e F falham** — deixam dois feitiços para o resto do dia, e aí uma luta de domínio come o dia inteiro. A escolha ficou no **A**: nada muda, porque o somatório absolveu o preço que já estava lá.

### Achado — um preço sem número, desde a v0.27

> **Cobrir-se de energia, a Reação: `1,5 × refino` de Redução de Dano por 2 PE.**

Estava escrito só *"gastando PE"*. É a lição nº 6 pelo avesso: ali o termo existia e o **número** não. O `conferir-orcamento.py` procura essa forma agora, e a busca varreu as onze peças.

**E os 2 são fixos porque o limitador dela não é PE** — é a Reação, uma por rodada, e a proteção perdida por um turno. Medido contra o que um PE compra atacando, só o valor fixo mantém defender não sendo estritamente pior que atacar: `+0,0` no nível 14 e `+0,9` no 30, contra `−2,0` e `−4,1` se ela custasse `1 × Classe`.

### Adicionado — `conferir-orcamento.py`, o nono validador

Cinco checagens, e nenhuma delas existe em outro lugar: a linha de base cabe; um compromisso não pode calar o personagem pelo resto do dia; pré-ligar não pode compensar; o dano de alma empilha por baixo sem falir ninguém numa rodada; e **todo preço em PE tem número**.

**Seis perturbações conferidas**, todas rodadas de `03-mecanica/`: bolso pela metade, upkeep em `3×`, upkeep zerado, upkeep em `0,1×`, Integridade quadruplicada, e o preço sem número voltando para a peça 11.

**E ele deu dois falsos positivos antes de ficar de pé**, os dois registrados no código: `custa Pesada` casava com `custa PE` por falta de um `\b`, e a nota que *explica* o preço antigo citando *"gastando PE"* era acusada como se fosse regra. Citação não é regra.

### Alterado — a coluna de PE do manual ganhou uma caixa (v7.8)

O Mizuki pediu para refazer os cálculos dela agora que existem aptidões. **A conta estava certa** — ela é PE total dividido pelo custo, e bate em todas as seis linhas. O que faltava não era número: era dizer o que ela **não** conta.

Medido: segurar uma anti-domínio durante um domínio inimigo tira **uma** conjuração do dia, duas no nível 20. A tabela não precisou mudar.

> **A caixa nova diz que a coluna é um teto, e não um orçamento de dia** — e diz por quê, porque foi tratar teto como orçamento que produziu esta versão inteira.

### Em aberto

- **Energia Reversa, Barreira Simples, Cortina** e a régua da Aptidão Própria.
- **Qual modelo de clash vale**, e os seis números do push.
- **Tabela de XP**, a próxima da fila.
- **Nome do sistema.**

---

## [0.29] — 2026-08-11

As quatro anti-domínio, destravadas pela v7.7. A pesquisa na obra **inverteu uma decisão** que estava escrita em três documentos, e a inversão mudou quem é a resposta barata do sistema.

### Achado — nenhuma das quatro serve contra a Expansão incompleta, e isso é canon

> **Elas anulam acerto garantido. A incompleta não tem acerto garantido — o Acerto dela rola.**

O wiki da Cesta Oca de Vime é explícito: ela *"não neutraliza a técnica em si, o que a torna ineficaz contra domínios incompletos ou não-letais"*. E tem cena: o **Reggie ativou Cesta Oca dentro do Jardim de Sombras Quimérico do Megumi** — incompleto — e os shikigami tomaram forma e bateram nele do mesmo jeito. O Domínio Simples tem o mesmo limite.

Isso encaixa exato nos dois degraus da v7.7 e **não abre buraco nenhum**: contra a incompleta você se defende com Defesa e Teste de Resistência, como de tudo o mais. E é o que faz o terceiro espaço da completa comprar alguma coisa de verdade — ele troca um Acerto bloqueável por Defesa por um que só estas quatro alcançam.

### Corrigido — a Cesta Oca é a predecessora, e o projeto tinha invertido

O `ESTADO-ATUAL` dizia *"Domínio Simples sem gate — é o que se ensina"*, e punha a **Cesta Oca acima dele**. A obra diz o contrário: a Cesta Oca de Vime é a **técnica antiga que o Domínio Simples melhorou**. O Reggie usa ela porque é feiticeiro do passado, não porque é mais forte. Gatear a versão pior mais alto cobra mais caro pelo produto inferior.

> **Cesta Oca de Vime é Classe 1, sem gate. Domínio Simples subiu para Classe 2.**

**E isso trocou o dono da resposta barata.** O argumento *"o acerto garantido só é jogável porque a resposta é barata"* estava pendurado no Domínio Simples no nível 6. Com ele em Classe 2 (nv10 · 10 · 14), quem chega no nível 6 para as três rotas é a Cesta Oca — **e ela responde menos**, porque anula o Acerto e não o Efeito.

**O argumento continua de pé, e vale escrever por quê:** o que a peça 11 chamou de opressivo foi o acerto que nunca falha, não o Efeito. A resposta barata cobre o que precisava cobrir, e só isso.

### Decidido — o eixo que separa as quatro é liberdade, não força

Os quatro preços vêm da obra, e nenhum foi inventado:

| | protege | e cobra |
|---|---|---|
| **Cesta Oca de Vime** | só você, numa esfera | você segura o símbolo e **não faz mais nada** |
| **Domínio Simples** | um raio em volta | **os pés não saem do chão**, ou quebra |
| **Pétala** | o corpo, e **devolve o golpe** | concentração, e **não para ataque físico** |
| **Extensão de Domínio** | o corpo, e faz o **seu** ataque acertar | **nenhum feitiço enquanto estiver de pé** |

| | Classe · gate | abre em | refino escala | PE/rodada |
|---|---|---|---|---|
| Cesta Oca de Vime | 1 · sem gate | nv 6, três rotas | **nada** | **nenhum** |
| Domínio Simples | 2 · refino 4, nível 7 | nv 10 · 10 · 14 | raio `1,5 m + refino÷2` | `1 ×` Classe |
| Pétala | 2 · refino 4, nível 7 | nv 10 · 10 · 14 | `refino÷2` Acertos devolvidos | `1 ×` Classe |
| Extensão de Domínio | 3 · refino 7, nível 13 | nv 14 · 18 · 26 | duração `refino` rodadas | `1,5 ×` Classe |

### Decidido — o custo por rodada, e a conta escolheu sozinha

Medido no Bastião, que é o menor bolso do sistema, numa luta de 3,5 rodadas:

| custo/rodada | do dia, por luta | lutas que cabem |
|---|---|---|
| metade da Classe | 9% a 18% | 5 a 11 |
| **`1 × Classe`** | **20% a 26%** | **3 a 4** |
| `2 × Classe` | 41% a 52% | 1 a 2 |

**O `1 ×` fica exatamente do tamanho do orçamento de lutas do dia** — a exaustão dispara da quarta, então dá para segurar a defesa em toda luta de um dia normal e terminar seco quando o cansaço chegaria de qualquer jeito. `2 ×` deixa você se defender uma vez e acabou; metade cai para 9% no nível 20 e **evapora**.

**A Cesta Oca é de graça em PE porque já cobra o turno**, que é o recurso mais caro de uma luta. Evitar dois Acertos custa **57% dos seus turnos**: você sobrevive e não contribui. Resposta de sobrevivência, não de vitória — que é o que ela é na obra. Cobrar PE em cima seria cobrar duas vezes pela mesma escolha.

### Escritas, com o que cada número segura

**O raio do Domínio Simples** é `1,5 m + refino ÷ 2` — 2,5 m no refino 2, que é onde o canon está (~2,21 m), e 6,5 m no teto. **Ele nunca passa de um movimento (9 m)**, e essa é a trava: uma defesa que cercasse o inimigo seria outra peça. O Kusakabe puxando gente para dentro fica como coisa da Trilha dele.

**A Pétala devolve `refino ÷ 2` Acertos**, e a completa solta `1 + duração` — 3 a 6. **Sempre sobra um**, em toda faixa de refino. Se ela devolvesse tudo, o terceiro espaço da completa deixaria de comprar alguma coisa.

**A Extensão se auto-limita pelo PE.** Ela dura `refino` rodadas, o dobro de uma Expansão, mas segurar até o fim custa 75% a 92% do dia de um Bastião — e **no nível 26 custa 106%**, ou seja, ele fica sem PE na nona rodada de dez. A duração é teto, não promessa. Some com *"você não lança nada enquanto ela está de pé"*: quem tem feitiço bom paga o dobro por ela.

### Adicionado — checagem 10 no `conferir-expansao.py`

A resposta mais barata alcança as três rotas antes de a Expansão existir; o upkeep cabe no orçamento de lutas do dia sem evaporar; a Pétala nunca anula o Acerto inteiro; o raio nunca vira cerca; e a escada de PE não decresce com a Classe.

**Seis perturbações conferidas**, todas rodadas de `03-mecanica/`: Cesta Oca subindo para Classe 2, upkeep em `2 ×` e em `0,5 ×`, Pétala devolvendo o refino cheio, raio em `1,5 × refino`, e a Extensão ficando mais barata que o Domínio Simples.

### Corrigido de método — a checagem do upkeep não lia a constante

A primeira versão dela tinha `1.0` escrito na mão dentro do laço, em vez de ler o multiplicador da tabela. Uma perturbação na constante **não acendia nada** — o mesmo defeito que a checagem de dominância do `conferir-aptidoes.py` tinha na v0.28, na mesma semana. Agora ela lê da tabela, e a mensagem de erro reporta o valor real em vez de um número fixo.

**É a lição nº 7 pela segunda vez em duas versões:** um número que mora em dois lugares vai divergir — inclusive quando os dois lugares estão no mesmo arquivo.

### Em aberto

- **Energia Reversa, Barreira Simples, Cortina** e a régua da Aptidão Própria.
- **Qual modelo de clash vale**, e os seis números do push.
- **A aptidão que baixa a Expansão para Ação Bônus** — citada, não escrita.
- **Tabela de XP**, que é a próxima da fila.
- **Nome do sistema.**

---

## [0.28] — 2026-08-11 · *manual v7.7*

A Expansão de Domínio, que era a coisa que a v0.27 registrou como bloqueadora de quatro entradas do catálogo. Ela saiu — e o caminho até ela achou **dois documentos que discordavam sobre quantos feitiços um personagem tem**, um validador que guardava um número em vez de lê-lo, e uma checagem de dominância que não enxergava o eixo que ela precisava enxergar.

**Oitavo validador.** E três nomes morreram na triagem, um deles depois de já estar escrito nesta versão.

### Decidido — os gates, e o que a conta separou de verdade

O `ESTADO-ATUAL` registrava nível 10 / refino **3** e nível 14 / refino **5**. O CHANGELOG da v0.27 registrava refino **4** e **6**. Os dois estavam meio certos, e a curva do `arquitetura.md` 4.3 separou:

> **Incompleta: nível 10 e refino 4, por 2 espaços. Completa: nível 14 e refino 5, por 3 no total — e ela exige ter a incompleta.**

**No nível 10 as três rotas estão coladas** — refino 5, 4 e 3, sem buraco entre elas. Então **qualquer gate que barre o generalista pega o meio a meio com folga zero**. Isso não é escolha de número: é o formato da curva, e só dá para escolher quem raspa.

**No nível 14, refino 5 e refino 6 separam exatamente as mesmas rotas.** Os dois barram só o generalista. Eles diferem na direção em que quebram, e o validador mediu: com **5**, a curva caindo um ponto não move ninguém; com 6, ela tira a completa do meio a meio. O 5 é imune para o lado que dói.

**E "barrado" quer dizer atrasado.** O generalista chega à incompleta no 14 e à completa no 18 — quatro níveis atrás nos dois degraus. Ele paga em tempo o que não pagou em marco.

### Corrigido — o preço da completa nunca esteve em aberto

O `ESTADO-ATUAL` dizia *"a definir"*. Mas a própria seção do Leque dizia 3, e **as três tabelas de orçamento da peça 11 só fecham com 3** — conferidas as nove células. `2 + nível÷2 + marcos` dá 12/16/21/24, e as linhas de Passiva batem em 3/7/12/15 e 0/0/3/6.

E um número velho junto: *"dois feitiços são 33% da lista no nível 10"* foi calculado com a fórmula anterior à v0.27. Com nove espaços no nível 10, dois são **22%**.

### Achado — o manual e o projeto tinham calendários de feitiço diferentes

A v0.27 mandou *"o manual corrigir o treze na v7.7"*, tratando como um número. **Não era um número: era um calendário inteiro.**

| nv | manual (tabela 9) | projeto (peça 11) |
|---|---|---|
| 6 | 4 | 6 |
| 14 | 9 | 12 |
| 20 | **13** | **16** |
| 30 | 18 | 24 |

O manual dava 2 no nível 1, +1 em cada **ímpar**, e extras no 10 e no 20. O projeto dá `2 + nível ÷ 2` — que sobe nos **pares** — mais um por marco. **Cada documento era coerente consigo e nenhum era coerente com o outro**, e a distância crescia: +3 no nível 20, +6 no 30.

E os extras **se cruzavam no nível 10**: o manual dava um feitiço ali e o projeto também. Se os dois valessem juntos, o nível 10 contaria duas vezes — a lição nº 2 pela sétima versão seguida.

> **O manual parou de contar feitiço.** A tabela 9 ficou com o que é do Fundamento — Classe por nível, Liberação Máxima, quando cada Classe de Passiva abre — e a contagem tem um dono só. É o mesmo modelo de dono único que a v0.26 escreveu para as três tabelas compartilhadas.

**Efeito colateral achado na varredura:** a peça 8 ainda dizia *"dois feitiços conhecidos"* no nível 2, em três lugares, incluindo a lista de abertura. A fórmula dá **três** desde a v0.27, e ninguém tinha corrigido. A ficha da Kaori não lista feitiços, então foi conserto de texto e não de exemplo.

### Decidido — o que a Expansão custa para usar

| | incompleta | completa |
|---|---|---|
| abrir | `6 × maior Classe` | `8 × maior Classe` |
| desconto lá dentro | `1/3 do refino` | `metade do refino` |
| duração | `metade do refino` em rodadas, mínimo 1 | |
| barreira | não tem | `50 × metade do refino`, só por fora |

**A escada fecha:** feitiço do topo `3×` < Técnica Máxima `5×` < incompleta `6×` < completa `8×`. E a incompleta passar da Máxima responde uma pergunta de design que apareceu no caminho — *"a incompleta não é mais fácil de ter que uma Técnica Máxima?"*. Ela chega sete níveis antes, sim. Mas a Máxima é **dada** no nível 17 para toda ficha, de graça e sem gate, e a incompleta é **comprada**, por dois espaços de lista e um gate de refino que barra uma das três rotas. *"Mais fácil"* está certo no calendário e errado no preço.

**O desconto quase virou lucro, e isso foi por pouco.** A duração é também quantos feitiços saem lá dentro, então desconto × duração compete com o custo de abrir:

| abrir | desconto | nv14 | nv20 | nv30 |
|---|---|---|---|---|
| `6 × Classe` | refino cheio | +3 | **−6** | **−8** |
| `8 × Classe` | metade do refino | +23 | +24 | +31 |

Com `6 ×` e refino cheio, **o saldo fica negativo do nível 20 em diante** — você abre o domínio e termina com mais PE do que começou. As combinações escolhidas ficam entre +18 e +31 em todo nível, e a margem não encolhe.

**E o desconto precisa de piso.** Sem *"nenhum feitiço custa menos de 1 PE"*, o refino 10 zeraria as Classes baixas e o PE deixaria de existir como recurso dentro do domínio.

### Decidido — o Acerto acontece no relógio do portador

Três formatos foram levantados, e dois caem no mesmo problema: pôr o proc no turno dos alvos. **"Começo da rodada dos alvos" não é um momento definido neste sistema** — a iniciativa é `d20 + Destreza` por criatura, então não existe rodada coletiva de inimigos, e dois mestres resolveriam diferente. E "fim do turno dos alvos" deixa todo mundo agir antes de o domínio encostar, o que esvazia o acerto garantido que o terceiro espaço comprou.

> **O Acerto acontece quando você abre, e de novo no começo de cada turno seu.** Um relógio, o do portador.

**E a preocupação com a aptidão que baixa o custo para Ação Bônus já tinha resposta escrita.** A regra de ouro nº 6 — *"feitiço em Ação Bônus ou Reação só permite mais um de Classe 0 no turno"* — resolve sozinha o caso de sair o Acerto garantido mais um feitiço da ação padrão. É a lição do Carregar de novo: **a tensão era lacuna de texto, não de preço.** Bastou escrever que a Expansão conta como feitiço para aquela regra.

### Decidido — o Efeito é escrito com o mestre, e o Acerto tem duas réguas

O Efeito sai no molde da **Regra Própria**, porque nenhum domínio da obra cabe num orçamento de dados — pachinko, julgamento, enxurrada de informação.

E o Acerto ganhou a régua que faltava, sem inventar nada:

- **Acerto que é dano garantido** → a régua é a Melhoria **Inescapável**, que custa uma Média e proíbe o feitiço de ter qualquer outra peça.
- **Acerto que é regra sobre o ambiente** → os requisitos da Regra Própria.

*Uma versão desta análise dizia que o +1 espaço da completa estava subprecificado contra o Inescapável.* Estava mal formulada: comparava as duas como se o Acerto fosse sempre dano. O do Higuruma — *"ninguém no ambiente pode causar dano"* — não é rolagem de dano nenhuma. A comparação só vale para a família que é dano, e é exatamente essa que a régua do Inescapável cobre.

### Adicionado — o Rescaldo, e o nome que morreu depois de escrito

A técnica queima quando o domínio acaba, **de qualquer jeito** — desfeito por vontade, expirado ou estilhaçado. O compêndio não distingue os três, e por isso **isso é preço e não risco**: acontece em todo uso, e quem abriu já sabia.

*Uma versão desta versão propôs tornar o gatilho condicional só à quebra, para preservar a energia reversa no cérebro como resposta a algo que acontece às vezes. A obra decidiu contra, e o texto passou a dizer que é custo fixo.*

**O nome era `Queima de Técnica`, e a triagem matou.** `Queima` já é Melhoria do manual — *"metade dos dados de novo, no começo do próximo turno do alvo"* —, e dois Queimas na mesma mesa com um deles causando dano é a colisão que este projeto mata nome para evitar. `Empurrão` e `Estilhaço`, que apareciam na descrição do clash, **também estão ocupados**. Sobrou **Rescaldo**, que é o que fica depois de algo queimar.

### Adicionado — `conferir-expansao.py`, o oitavo validador

Nove checagens: os gates separam o que dizem, a ordem entre os degraus não inverte, barrado é atrasado e não trancado, o preço fecha com as tabelas publicadas, a resposta anti-domínio chega antes da ameaça, a fragilidade da curva medida nas **duas** direções, o desconto não paga a própria Expansão, o piso segura o custo de feitiço, e a barreira cai dentro da própria duração.

**Oito perturbações conferidas**, cada uma acendendo a checagem certa: gate que para de barrar, gate que barra demais, gate da completa mais frouxo que o da incompleta, preço em 4, preço igual ao da incompleta, incompleta descendo para o nível 6, curva do generalista subindo, e a linha passiva do marco sumindo.

### Corrigido — a checagem de dominância não via o eixo da pergunta

Ao validar se o Leque devia devolver dois feitiços em vez de um, a checagem 5 do `conferir-aptidoes.py` saiu **verde** com a rota pura indo de 31 para 38 espaços. O motivo: ela olhava atributo, aptidões e Passivas, e **não olhava refino nem feitiços** — justamente o eixo em que o Leque lidera.

Agora ela olha os cinco, confere a recíproca (nenhuma rota pode **liderar** em todos), e ganhou duas travas diretas: o Leque devolve exatamente um feitiço por escolha, e a rota de Leque não pode terminar com mais espaços a mais do que existem marcos. **Perturbação conferida:** o `+2` acende as duas.

**E a resposta à pergunta foi não.** A lista não está escassa contra a régua que existe: o manual pretendia treze no nível 20, e a rota de Leque já entrega **20**, +54%. O aperto que se sentia vem da Expansão, e é o preço dela funcionando — sem comprar Expansão a lista nunca fica curta.

### Corrigido — o `conferir-repositorio.py` guardava o número em vez de lê-lo

Ele falhou quando o oitavo validador entrou, porque tinha `sete` escrito no código. Agora ele **lê o número do README** e compara — o mesmo defeito que a checagem 4 do `conferir-manual.py` existe para pegar, dentro do próprio validador que existe para pegar defeitos assim.

Ele também pegou, na hora, o rascunho do clash tomando número de peça. Rascunho não é peça, e o arquivo foi renomeado.

### Corrigido de método — três perturbações minhas eram inválidas

Ao testar o `conferir-manual.py`, rodei as cópias perturbadas de `/tmp`. **De lá ele não acha o `.docx`, avisa e pula as quatro checagens** — então as três primeiras perturbações saíram verdes sem terem conferido nada. É exatamente o alerta que o README dá sobre o `python-docx`, aplicado a mim.

Refeita no lugar certo, a perturbação acendeu. E ela achou um segundo problema: o teste genérico de *"está definido"* aceita qualquer frase com a palavra **é**, e quase toda frase em português tem uma. Para termos importados isso não basta — cada um agora declara o próprio padrão de definição.

### Adicionado — `refino` é termo importado, e o manual tem que defini-lo

A Expansão pôs uma palavra do projeto dentro do manual, que é a direção contrária do problema que a v0.26 consertou. O `conferir-manual.py` ganhou uma lista de **importados do projeto**: cada um entra com o lugar onde o manual o define, e o validador falha se a definição sumir. O manual define refino numa caixa de uma linha e não usa a palavra em mais lugar nenhum.

### Registrado — o clash ficou de fora, e está engatilhado

Um modelo de **push gradual** foi levantado a partir da obra: sobreposição de áreas anula o acerto garantido dos dois lados, e começa um empurrão cuja velocidade vem da diferença de refino, com vantagem para quem tem Acerto inofensivo e para quem está com a barreira aberta.

**Ele substitui uma regra marcada como fechada** — a resolução por `1d10 + aptidões + metade do nível` — e **pede seis números que não existem**. A parte mais interessante dele é a que mais preocupa: *efeito inofensivo empurra melhor* recompensa escrever um Acerto fraco de propósito, e sem número ninguém sabe se compensa.

Foi para `03-mecanica/RASCUNHO-clash-de-expansoes.md`, com os seis números nomeados e a ordem de atacá-los. A v7.7 cita a regra que já estava decidida.

### Registrado de método — o mount perdeu um arquivo que ele mesmo gravou

Fechando a versão, o `conferir-repositorio.py` acusou que o `README.md` não existia. Ele existia: `ls` e `stat` devolviam tamanho e inode certos, e o nome não tinha caractere estranho — mas `open()` devolvia **ENOENT** para o `head`, para o Python e para o `git` igualmente, enquanto **os vizinhos na mesma pasta abriam normalmente**. As ferramentas de arquivo liam o conteúdo certo o tempo todo.

Ou seja: **o arquivo estava íntegro no disco, e quem não o enxergava era o mount FUSE do sandbox.** Nenhuma tentativa de reconciliar resolveu — `sync`, relistar o diretório, caminho absoluto, reentrar na pasta. **Reescrever o arquivo inteiro resolveu**, porque criou um objeto novo.

É primo do problema do `git commit` que o README já documentava, e agora está escrito ao lado dele. Fica registrado porque o sintoma engana: parece arquivo apagado, e é o oposto — o conteúdo nunca esteve em risco.

### Alterado — o README ganhou uma sétima lição

> **Um número que mora em dois documentos vai divergir.** Não é "se", é "quando" — e cada cópia precisa de um dono declarado ou de um validador que compare as duas.

Ela sai desta versão de dois lados ao mesmo tempo: o `conferir-repositorio.py` guardava `sete` no código, e o manual e o projeto contavam feitiço por calendários diferentes desde sempre. As duas são a mesma doença.

E o aviso sobre `python-docx` ganhou um par: **os três validadores que leem o `.docx` também pulam em silêncio se forem rodados de outro diretório.** Foi assim que três perturbações desta versão saíram verdes sem terem conferido nada.

### Em aberto

- **As quatro anti-domínio**, agora destravadas. É a próxima da fila.
- **Energia Reversa, Barreira Simples, Cortina** e a régua da Aptidão Própria.
- **Qual modelo de clash vale**, e os seis números do push.
- **A aptidão que baixa a Expansão para Ação Bônus** — citada, não escrita.
- **Nome do sistema.**

---

## [0.27] — 2026-08-11

A peça de aptidões, que o `arquitetura.md` chama de *"o risco maior da estrutura inteira"*. Ela sai **com quatro das catorze entradas em branco**, e isso é decisão: elas contam o Acerto de uma Expansão de Domínio, e a Expansão só ganha regra na v7.7 do manual.

**Sétimo validador.** E a escolha de marco deixou de ter duas opções.

### Adicionado — `03-mecanica/11-aptidoes-e-refino.md` e `conferir-aptidoes.py`

Sete checagens, e sete perturbações conferidas: aptidão escalando eixo proibido, o divisor de cobrir-se deixando de dar +3, a Reação com saldo negativo, kokusen grande demais para ser só grito, gate de refino que não separa as rotas, Passiva grátis deixando de ocupar vaga, e a linha passiva do marco removida.

### Decidido — o refino é a métrica geral das aptidões, e a trava é outra

Até aqui o refino era um contador. Ele subia nos marcos, tinha teto 10 e destravava aptidão — e **entre um refino 3 e um refino 10, no mesmo nível, com as mesmas aptidões, nada mudava na ficha.** A intenção estava escrita no `arquitetura.md` desde a Fase 3 (*"o refino governa confiabilidade e custo"*) e nunca tinha virado número.

Agora ele é requisito **e** tamanho, e entra no texto de cada aptidão **como variável**, no molde que o manual já usa para `sua maior Classe`. Cada aptidão declara o próprio teto — nem toda uma usa o valor cheio.

**A trava proposta pelo `arquitetura.md` era *"aptidão não produz dano e não escala com nível"*, e ela foi escrita antes de existir régua.** Com a régua das Classes, a que importa é outra, e ela vem da regra que governa o sistema:

> **O refino cresce +7 a +9 numa campanha; atributo e maestria crescem +3.**
> **Então ele não pode aparecer de um lado de uma rolagem em que o outro lado não cresce no ritmo dele.**

Isso proíbe acerto, CD, defesa, Teste de Resistência e dano — os cinco têm do outro lado alguém que cresce +3. **E permite refino contra refino**, que é simétrico: o clash de expansões passa por isso e não deriva.

### Decidido — o marco ganhou um terceiro eixo, o Leque

> **Passivo:** +1 atributo, +1 refino e **+1 espaço de feitiço**.
> **Escolha:** **Corpo** (mais atributo) · **Refino** (mais refino e uma aptidão) · **Leque** (mais um feitiço, que só pode ser feitiço, e uma Passiva).

**O problema que ele resolve é real e era maior do que parecia.** Passiva custa espaço de feitiço, e a Expansão também. Sem rota que devolva espaço, três Passivas de Classe 2 mais a Expansão completa chegavam ao **nível 20 com dois feitiços** — e a montagem cheia que o manual permite, cinco Passivas de Classe 3 mais Expansão, pedia 18 espaços numa ficha que tinha 16. **O teto de "cinco Passivas pagas" do manual já era letra morta:** quem escrevesse cinco Classe 3 descobriria no meio da campanha que não cabia.

Com a linha passiva do marco, a montagem típica sai de dois feitiços no nível 20 para sete, e a mais pesada passa a caber **a partir do nível 22**.

**As três não precisam de trava, e o motivo é bonito.** Passiva e aptidão vivem na **mesma escada de Classe**, então `+1 feitiço e 1 Passiva` empata com `+1 refino e 1 aptidão`. O que sobra dos dois lados é `+1 feitiço` contra `+1 refino` — e **refino não vale nada para quem não tem aptidão**. Quem escolhe Leque não quer refino; quem escolhe refino não quer Passiva. Nenhuma compra o que a outra compra.

**O teto de Passivas sobe, e a grátis traz a própria vaga.** Cada escolha de Leque aumenta o máximo em um, e a Passiva concedida ocupa a vaga nova — então as **pagas continuam sendo cinco**. O teto não cresce; ele abre lugar.

*Uma primeira leitura desta regra somava as duas coisas e chegava a **dezenove** Passivas numa ficha. Estava errada, e é a mesma família da lição nº 2: o teto já incluía o que eu estava somando nele.*

### Corrigido — o manual e a peça 8 discordavam em dois feitiços

O manual: *"a conta fecha em treze feitiços conhecidos no nível 20"* e *"ganha uma nova a cada dois níveis"*. A peça 8: *"no nível 2 você tem dois feitiços conhecidos"*. Dois no nível 2 mais um a cada dois níveis dá **onze** no nível 20.

> **Feitiços conhecidos = `2 + (nível ÷ 2)`, arredondando para baixo — mais um por marco.**

Três no nível 2: dois de toda ficha, mais o do próprio nível 2. **A confusão vinha de a ficha nascer no nível 2** — o nível 1 é quem ainda está entrando no mundo jujutsu, civil ou com a técnica sem despertar. Doze no nível 20, e o manual corrige o treze na v7.7.

### Decidido — a Classe de aptidão mede formato, não tamanho

Se ela medisse tamanho, a escada colapsaria: um marco compra uma aptidão de qualquer Classe destravada, então do nível 13 em diante **toda escolha seria Classe 3** e o especialista terminaria com sete aptidões, cinco delas Classe 3, sem nunca ter olhado para uma Classe 1.

**A Passiva do manual não tem esse problema porque ela tem preço** — Classe 3 custa três espaços, então você troca uma por três Classe 1. A v0.25 herdou metade da régua: o gate e o tamanho do efeito, sem o preço que faz os três degraus competirem.

**O que resolve é o refino.** Com ele escalando o que a aptidão entrega, **uma Classe 1 no refino 10 não é a mesma coisa que no refino 2** — e aí a Classe volta a dizer o que o manual sempre disse que ela dizia: *pequeno e condicional · reativo com limite · permanente*. Não são mais e menos; são formatos.

### Decidido — o gate é por aptidão, e não pode ser só nível

Cada aptidão declara o próprio requisito: nenhum, só nível, só refino, ou os dois.

**Só nível não serve**, e a conta mostra: quem escolhe refino **uma vez, no nível 26**, compraria uma Classe 3 na hora — o mesmo acesso de quem investiu seis vezes. Com gate de refino, a Classe 3 abre no nível 14 para o especialista e no **26** para o generalista. Doze níveis, que é o tamanho que *"quase ninguém consegue"* pede.

**E guardar marco não guarda refino.** A rota que espera — atributo cedo, refino tarde — não domina, porque o refino passivo sobe sozinho: ela chega ao nível 22 com refino 5 e ainda precisa de outro marco para o 7. Troca quatro aptidões por quatro pontos de atributo.

### Escritas — as seis que têm número

**Cobrir-se de energia.** Proteção `1/3 do refino + 1` sem uniforme, e como Reação uma RD de `1,5 × refino` gastando PE, ao custo da proteção por um turno.

O **1/3 não é escolha de gosto: é o único divisor que cabe.** Ele cresce de 0 a 3 na campanha, exatamente como um atributo. Com o refino cheio o atacante cairia de 50% para **5%** de acerto no nível 22 — a deriva da v0.9 pelo lado defensivo.

E o **1,5 ×** é o que impede a Reação de virar armadilha. Com `1 × refino` ela fica **negativa do nível 22 em diante**: o custo de um turno sem proteção cresce com o golpe do chefe enquanto a RD trava no teto. Com 1,5 o saldo fica positivo do começo ao fim e **encolhe** em vez de virar.

*Recado para a peça de equipamento:* no refino 10 ela dá proteção 4, e um Vanguarda que largue o uniforme chega a Defesa 20 contra os 17 dele fardado. **Um uniforme precisa valer mais que 4.**

**Canalizar energia** não é escalada pelo refino — ela vive inteira no orçamento do Fundamento, e é o exemplo mais limpo de teto por aptidão.

**Projetar energia** entrega `dano = refino`, entre **8% e 12% da coluna Rotina** do nível 2 ao 30. É o único lugar do catálogo onde o refino toca dano, e ele **deriva para baixo**, porque a vida do inimigo cresce mais rápido que ele.

**Kokusen** a `2 × refino` no d100, com **+50% no impacto depois de tudo resolvido**. Teto de **1,8%** de dano por rodada no refino 10 — menos de um quinto do que um ponto de atributo compra. **Kokusen Melhorado** dá **vantagem no d100**, que ganha do `3 ×` em todo refino (36% contra 30% no teto), e a terceira sobe a base para `3 ×`.

**E o kokusen tem proteção contra azar.** No refino 1 a espera pelo primeiro seriam **47 sessões**, o que na prática é nunca. Cada d100 falhado empurra o próximo em +2, e o acumulado **zera no descanso longo** — o refino 1 cai para ~9 sessões e o refino 10 quase não se move. *Por cena não serviria:* o acúmulo só começa no segundo crítico da mesma cena, e dois críticos no mesmo combate acontecem em **4,4%** das vezes.

**A cascata mexe só na chance, e nunca na margem.** Dobrar a chance no refino 5 rende +0,9 ponto; fazer a margem cair para 19 rende **+10,9%**, dos quais **9,1 vêm do dado a mais** — a margem carrega o crítico inteiro junto. E sem teto, quatro degraus numa cena levariam o físico a **1,8× o dano base**.

### Adicionado — o Limiar

Vem do dossiê, seção 2: **gatilho de ficção antes da rolagem**, roubado do PbtA e do FitD. Mecânica separada, declarada pelo mestre, e o kokusen é só um dos lugares que a citam. *Faísca* morreu na triagem dentro de *Faísca em Cadeia* e *Impulso* é Melhoria do manual; **Limiar** está livre nos dois lados.

**O cardápio sai sem número, por decisão** — mas o tamanho fica registrado na peça, porque ele não é plano. Contra o alvo difícil, rerrolar e dar vantagem valem os **mesmos +25 pontos percentuais**; "acontece mesmo errando" e "sucesso garantido" valem **o dobro**. E as duas famílias correm em sentidos opostos: a vantagem é auto-regulada e dá 9 pp contra alvo fácil, enquanto o garantido vale **75 pp** contra CD alta — justamente quando alguém vai querer dar.

**Nota de método registrada e não resolvida:** o dossiê defende o gatilho de ficção *contra* a discricionariedade. Aqui a escolha foi a outra, e o `arquitetura.md` sustenta — *"discricionariedade na ficção é o trabalho do mestre e não atravessa mesas"*. Vai para o playtest junto da contagem de lutas, que é a mesma aposta.

### Registrado — o que ficou fora, e por quê

**Quatro das catorze estão bloqueadas.** Domínio Simples, Pétala, Cesta Oca de Vime e Extensão de Domínio contam o **Acerto** de uma Expansão, e a Expansão vai para o manual na v7.7. Escrever o preço delas agora seria precificar contra alvo que não existe — o erro que a v0.24 registrou no ataque extra.

**E o laço entre as duas é o que torna as duas possíveis.** A Expansão completa acerta **garantido**, e é isso que o terceiro espaço compra. Um acerto que nunca falha só é jogável porque a resposta é barata: os quatro anti-domínio são **aptidões de marco**, ao alcance de qualquer ficha que escolha o eixo do controle. Se fossem raros, o garantido seria opressivo. A decisão de pôr os quatro no catálogo foi tomada antes de a Expansão ter forma.

**A Expansão, decidida e não escrita:** incompleta custa **2 espaços**, nível 10 e refino 4; completa custa **+1** (três no total), nível 14 e refino 6, e **exige ter a incompleta** — o molde é o da Regra Própria do manual, que sobe de Classe *"pagando só a diferença de espaços"*. Nos dois gates o **meio a meio passa com folga zero**, e isso pede validador quando a peça existir.

### Registrado — as Bênçãos e a Lapidação

A Restrição Celestial pelo ramo da Maki e o Corpo Amaldiçoado não têm energia — sem PE, sem golpe canalizado, sem Sentir Energia — então não têm aptidão nem refino. Eles ganham **a mesma máquina com outra métrica**: as aptidões viram **Bênçãos** e o refino vira **Lapidação**. Andar em parede e em água, deslocar-se no ar, *fast steps*. Os dois nomes passaram pela triagem.

É a camada de aptidão da **Técnica Marcial**, e ela destrava duas das três rotas de Origem que não rodam hoje.

### Alterado

- `02-economia-de-atributos.md` ganhou aviso na seção 3: a escolha de marco tem três opções desde esta versão, e a análise de auto-equilíbrio dela foi feita com duas.

### Em aberto

- **As quatro anti-domínio**, e a peça da Expansão que as destrava.
- **Energia Reversa, Barreira Simples, Cortina** e a régua da Aptidão Própria.
- **Se alguém escolhe o Leque.** Se ninguém pegar, o aperto que ele resolve continua resolvido pela linha passiva, e aí ele sai.
- **Se doze Passivas pesam na mesa.** O manual escolheu cinco por peso, não por orçamento.
- **Nome do sistema.**

---

## [0.26] — 2026-08-10 · *manual v7.6*

Os quatro buracos de regra que a v0.24 registrou e ninguém tinha escrito. Um deles a conta respondeu sozinha, e ao ir atrás dele apareceram três problemas maiores do que os quatro: um órfão de vocabulário dentro do manual, duas regras que apontavam para Testes de Resistência diferentes sem ninguém ter notado, e a Casca — que morreu por três motivos, e nenhum era o que estava escrito no changelog anterior.

**Seis validadores agora.** O sexto olha a direção que faltava.

### Corrigido dentro da própria versão — o manual não é lei, e eu tinha escrito que era

Duas frases desta versão davam ao manual uma autoridade que ele não tem: *"a fórmula já estava no manual"* e *"não é escolha nossa"*. **Os limitadores, exemplos e tabelas do manual foram calibrados quando o sistema em volta era outro.** Eles servem de base para continuidade — e é bom que estas mudanças estejam acontecendo agora, com estrutura em pé —, mas não valem ao pé da letra.

Isso não muda nenhuma decisão desta versão. Muda o **motivo** de duas delas, e muda o que o validador novo afirma.

Levantando a exposição real, **dez decisões do projeto estão penduradas em três tabelas do manual** — e elas não são iguais entre si:

| tabela | dono | por quê |
|---|---|---|
| **PE** — *"quantas vezes você lança"* | **o projeto** | nada exige que o Emanador tenha 6. O que exige é que a coluna diga a verdade sobre a ficha. Mudou o 6? Regere a coluna |
| **Rotina** — dano por rodada por Classe | **o manual** | ela não é medida, é a **definição** de "quanto é normal". Não há verdade fora dela: o projeto compara tudo contra ela, inclusive ela mesma |
| **Inimigo** — chefe e capanga por nível | **o playtest** | é a única das três que afirma alguma coisa sobre o mundo: que um combate dura ~3,5 rodadas. A trava de vida inteira da peça 1 foi calibrada contra ela, e ninguém é dono dela até alguém jogar |

**Duas das três não correm risco de estar desatualizadas, porque não afirmam nada — elas *são* a régua.** A terceira corre, e é exatamente a que o playtest mede primeiro.

A checagem 4 do `conferir-manual.py` foi reescrita em cima disso. Ela deixou de dizer *"o projeto copiou daqui, então tem que bater"* e passou a dizer **"os dois lados divergiram, e aqui está quem decide"** — a mensagem de erro nomeia o dono e o custo de mexer. Divergência virou pedido de decisão, e não veredito.

### Achado — a fórmula do PE máximo, e o quanto o manual conta como argumento

O buraco dizia: *"o PE máximo nunca teve fórmula escrita — só a instância do nível 2 na peça 8, e não dá para inferir da vida, que usa `(nível − 1)` e soma atributo."*

> **PE máximo = PE por nível do Caminho × nível.** Sem atributo, sem valor inicial.

Sem atributo pelo motivo da peça 1, seção 9: um atributo na conta de PE viraria o atributo obrigatório de todo conjurador pela porta dos fundos. Sem valor inicial porque é o que faz esta ser a única reserva que passa pela origem — a vida tem inicial e soma atributo, a Integridade tem inicial.

**E o manual concorda.** A tabela dele mostra 6, 30, 54, 78, 102 e 120 nos níveis 1, 5, 9, 13, 17 e 20, todos `6 × nível` exatos. Concordar não é mandar, pela seção acima — o que a concordância compra é que **a coluna "quantas vezes você lança" continua dizendo a verdade sobre a ficha sem precisar ser refeita.**

### Decidido — arredondamento, e a frase que reconcilia os precedentes

Cai em fração em quatro lugares, e a **Vanguarda e o Guia caem na primeira parada da primeira sessão**: 25% de uma pool de 10 é 2,5.

> **Arredonde sempre para o lado que não te favorece.** O que você paga sobe, o que você ganha desce, e o que você ganha nunca fica abaixo de 1.

Não é escolha nossa. É o princípio que o manual declara na caixa *"na dúvida, para que lado errar"* — *"os dois erram pro mesmo lado: o que não infla o feitiço"* — aplicado a número em vez de a preço. E ele explica por que os dois precedentes que existiam não estavam brigando: o manual arredonda para cima no preço de Melhoria e no +50% da Liberação, que são coisas que você **paga**; o exemplo da peça 10 arredonda para baixo, e é recuperação.

**O piso de 1 não desfaz um zero escrito.** O degrau 3 de exaustão devolve *nada*, e nada é zero. O piso existe para a conta que produziu 0,4.

**E um caso que parecia exceção e não é.** A vida por nível do Caminho é a média do dado arredondada **para cima** — d12 vira 7, d8 vira 5, d6 vira 4 —, e isso é um ganho subindo. Ela não quebra a regra porque **não é conta de mesa**: é valor de tabela, decidido uma vez no desenho. A regra vale para o número que cai na mão de quem está jogando. O validador agora confere as duas coisas separadamente, para o dia em que alguém tentar "consertar" a tabela aplicando a regra nela.

**Efeito colateral registrado:** com o piso de 1, os degraus 1 e 2 de exaustão devolvem o mesmo PE enquanto a pool é pequena — separam no nível 3 em quatro Caminhos e no 4 no Bastião. Os outros dois eixos do degrau continuam diferentes desde o nível 2, então a escada nunca fica plana de verdade. O validador passou a exigir que a coluna seja **não crescente**, e não estritamente decrescente.

### Decidido — o que conta como uma luta

> **Quem conta é o mestre, e ele conta como em qualquer mesa: foi uma luta se pareceu uma luta.**

Não depende de ter rolado iniciativa, e não é só maldição — feiticeiro contra feiticeiro cansa igual. A peça traz exemplos, e eles são exemplos e não lista fechada.

**Isso é diferente do ambiente propício de propósito, e vale registrar o motivo.** Lá a lista é fechada e o mestre tem a palavra final em cima dela. Aqui não. *"Esse lugar tem kit e comida?"* é pergunta sobre o mundo, e a mesma resposta serve para qualquer mesa; *"isso foi uma luta?"* é pergunta sobre a cena que aquele mestre acabou de dirigir. Fica marcado para o playtest: **medir se dois mestres chegam ao mesmo número de degraus no mesmo tipo de missão.** Se não chegarem, a saída é a do ambiente propício — fechar a lista.

### Corrigido — a exaustão nunca esteve desordenada. O texto é que prometia errado

O achado da v0.24 dizia que *"a exaustão está ordenada por onde dói, não por quanto"*, e que o degrau 1 é maior do que o texto promete. A primeira metade estava certa e a segunda estava mal formulada.

Desvantagem é rolar 2d20 e pegar o menor: a chance `p` vira `p²`, e a perda `p − p²` é máxima exatamente em 50%, onde vale **25 pontos percentuais**. Como o degrau 1 e o degrau 3 são os dois desvantagem, os dois tiram **exatamente os mesmos 25 pp**. Não existe "degrau leve" numa escada em que dois dos três degraus usam a mesma mecânica.

| degrau | eixo | tamanho no pico | a falha custa |
|---|---|---|---|
| 1 | perícia e ofício | −25 pp | a cena anda |
| 2 | deslocamento, 9 m → 6 m | −33% de alcance | posição |
| 3 | ataque e Teste de Resistência | −25 pp | dano, e às vezes a vida |

**A escada é ordenada por consequência, e sempre foi.** Falhar em perícia move a cena, porque a peça 4 proíbe falha que trava; falhar em ataque perde a luta. O conserto não era mexer no número: era o texto parar de vender o degrau 1 como pequeno e passar a dizer que ele é do mesmo tamanho e cai em cima do que não mata. O `conferir-descanso.py` agora confere **magnitude**, e falha se alguém escrever um degrau de desvantagem como se fosse menor.

Para escala: um degrau de exaustão é **maior que treinar um Teste de Resistência** (10 pp), **maior que a maestria de uma campanha inteira** (20 pp) e **maior que sair de atributo 0 para 3** (15 pp).

### Decidido — exaustão e Integridade, pega o pior

As duas escadas nunca tinham sido postas uma do lado da outra. São quase a mesma escada:

| | exaustão (peça 10) | Integridade (manual) |
|---|---|---|
| degrau 1 | desvantagem em perícia e ofício | desvantagem em testes de perícia |
| degrau 2 | deslocamento cai para 6 m | deslocamento pela metade, e +1 PE por Classe |
| degrau 3 | desvantagem em ataque e TR | desvantagem em ataque e TR, e teto de Classe |

> **Quem está nas duas pega o pior, não soma.**

Isso não inventa nada — desvantagem não empilha com desvantagem em mesa nenhuma. A regra existe para escrever o que a mesa já faria, em vez de deixar a pergunta aparecer no meio de uma missão longa. O que só a Integridade tem (o +1 PE por Classe e o teto de Classe) não compete com nada e simplesmente acontece.

**E os 6 m contra os 4,5 m ficam diferentes de propósito:** a Integridade é dano de alma e deve doer mais. Se as duas dessem o mesmo corte, a alma estaria cobrando o preço do cansaço. O validador falha se a Integridade deixar de cortar mais.

### Adicionado — `conferir-manual.py`, o sexto validador, e a direção que faltava

O `conferir-nomes.py` olha **projeto → manual**: *"esse nome que eu batizei já significa alguma coisa lá?"*. Ninguém olhava o contrário. É por isso que o `Bônus de Treinamento` da Passiva Reforço sobreviveu até a v0.25 — e por isso que a Fraqueza sobreviveu até agora.

Quatro checagens: **vocabulário órfão** (palavra de outro sistema, tolerância zero), **teste nomeado pelo atributo** em vez do Teste de Resistência, **termo mecânico usado e nunca definido** (com os aceitos declarados com motivo, no padrão do `conferir-pericias.py`), e — a que ninguém teria escrito à mão — **os números que o projeto importou do manual**. A tabela de PE, a de inimigo e a coluna Rotina estão **copiadas** dentro das peças e dos outros validadores; se o manual for regerado e um deles mudar, o projeto passa a mentir em silêncio. Agora ele grita.

Testado nos dois sentidos: com o manual v7.6 limpo ele sai com código 0, e **seis perturbações** — Sabedoria de volta, teste nomeado pelo atributo, `dano físico` de volta, e um número mexido em cada uma das três tabelas importadas — acenderam cada uma a checagem certa. Somando com as extensões do `conferir-descanso` e do `conferir-atributos`, foram **dezesseis perturbações conferidas** nesta versão.

### Achado — a Restrição Fraqueza carregava dois órfãos numa linha só

> *"Depois de usar, você fica com desvantagem em Testes de Resistência de uma **Habilidade**, escolhida na montagem, até o fim da cena. Habilidade pouco testada na sua mesa: Leve. Constituição, Destreza ou **Sabedoria**: Média."*

**Habilidade** aqui são atributos. **Sabedoria** não existe — ela e o Carisma fundiram em Essência antes de a Fase 4 começar. E o defeito é pior do que vocabulário: o preço citava **atributo**, e os Testes de Resistência daqui são quatro, com o Físico usando Força **ou** Destreza. A tradução não era um para um, e um terço da regra de preço apontava para o nada.

Preço novo: **Vigor ou Intelecto, Leve. Físico ou Espírito, Média.**

### Achado — Concentração e Carregar apontavam para testes diferentes, e um dizia ser o outro

A peça 3 diz que Concentração é **Teste de Resistência Físico**. O manual diz que Carregar é **"teste de Constituição"**. E a peça 3 ainda afirmava, com todas as letras, que *"é a mesma régua que a Restrição Carregar já usa"*. A régua da CD era; o teste não.

Ao abrir os dois, apareceu que **eles não deviam ser a mesma regra**, e a diferença já estava escrita há versões sem ninguém ler: em Concentração *"o efeito cai"* — você tinha, e perdeu. Em Carregar *"perde o feitiço"* — ele ainda não tinha saído. O único fio que os fazia parecer iguais era a palavra **"concentrado"** dentro do texto do Carregar.

| | o que você segura | teste | falhar custa |
|---|---|---|---|
| **Concentração** | o efeito que já está no ar | **Vigor** | o efeito cai |
| **Carregar** | o feitiço que ainda não saiu | **Espírito** | o feitiço, e o que você pagou por ele |

A frequência foi conferida antes de mexer: Concentração é exigida pela Melhoria **Fica**, que **1 dos 35 feitiços prontos** usa, e por Carregar, que **nenhum** usa. Então pôr Concentração em Vigor quase não muda a frequência dele, e o argumento *"o TR Vigor quase não rola"* — que a peça 10 usa e que sustenta o Leve da Fraqueza nova — continua de pé.

A Passiva **Mão Firme** passou a dizer *"não perde concentração **nem carga**"*, explícito, porque com a divisão o nome dela sozinho não alcançava mais o Carregar.

É a terceira vez que a lição do Carregar se paga: **tensão de preço às vezes é lacuna de texto disfarçada.** A v0.11 resolveu o par Lento-contra-Carregar escrevendo uma frase; agora uma palavra dentro do mesmo item resolveu outro problema, e nenhum preço precisou mudar.

### Decidido — a Casca morreu, e por três motivos que não eram o que estava escrito

A v0.25 deixou pendente: *"a Passiva **Casca** cai na mesma regra e não foi mexida"*. Rodando a conta antes de decidir, o motivo escrito era o menos importante dos três:

**`dano físico` aparece uma vez no manual inteiro — dentro da própria Casca.** Não é categoria definida em lugar nenhum, e os tipos de dano do manual são livres (*"corte, fogo, peso, o que a Descrição pedir"*). Dois mestres leem diferente, e um deles dá RD contra tudo que é soco.

**RD corta o mesmo valor de cada golpe, e o manual dá dano por rodada.** Nunca quantos golpes. A Casca valia de **6% a 42%** conforme um número que não existe em lugar nenhum do material.

**E a Melhoria Fura ignora `3 × Classe` de RD.** Um ponto numa Classe 1 já apagava a Casca inteira, em qualquer nível. Contra quem comprou Fura ela era zero.

> A Passiva **Casca** foi deletada. No lugar dela entra a **Escama**: *escolha um tipo de dano que a sua Regra justifique; você tem resistência a ele.*

**A Escama não é uma Casca mais fraca — é outra aposta.** Resistência é metade, então ela vale **5 a 9 vezes mais** que a Casca quando o tipo bate, e **zero** quando não bate. O ponto de virada é **1 luta em 4**: acima disso ela é a melhor Passiva de Classe 3 da lista, abaixo é a pior.

**A trava que impede a otimização é a que estava na escolha desde o começo:** o tipo é preso à Regra, e a Regra é escrita na **criação**, antes de qualquer um saber o que a campanha vai mandar. O jogador aposta; ele não escolhe o tipo que o mestre mais usa, porque ainda não sabe qual é. E o julgamento que a palavra *"justifique"* introduz cai no mesmo momento em que a técnica já é aprovada — a trava nº 3 de mundo compartilhado obriga alguém que não é o dono a ler a Regra —, então ele não atravessa mesas.

O nome passou pelo `conferir-nomes.py --candidatos` junto com onze outros. **Berço** está dentro de *Treino de Berço* e **Familiar** fica a uma letra de *Família*; os dois morreram na triagem antes de entrar em qualquer arquivo.

E ela nasce com **dois counters que já existiam**: a Melhoria **Corrói** cancela resistência ao tipo, e a Passiva **Afinidade** ignora resistência ao tipo. A peça defensiva nova não precisou de contrapeso novo.

**A regra que matou as duas foi escrita onde a próxima pessoa vai procurar** — a lista *"o que nenhuma Passiva paga pode fazer"* do manual ganhou uma quinta linha: *"Redução de Dano passiva… Resistência a um tipo, sim — é o que a Escama faz. Desconto em tudo, não."*

### Decidido — "resistência" ganhou definição

Ela era usada **três vezes** no manual — Afinidade, Corrói, Purga Escarlate — e **nunca explicada**. Mesma família do `dano físico`, e trocar um termo indefinido por outro não seria conserto.

> **Resistência: o dano daquele tipo cai pela metade, antes de qualquer outra conta. Sempre presa a um tipo — não existe resistência a tudo.**

Metade é a única leitura que **não deriva**: sendo proporcional, ela vale o mesmo no nível 13 e no 30. As alternativas de valor fixo encolhem conforme o inimigo cresce, que foi exatamente o que aconteceu com a Casca — **−6,1% no nível 13 e −5,6% no 30**, com o número tendo *dobrado* no meio do caminho.

### Registrado — o Kokusen Melhorado tem preço e requisito

As duas pendências da v0.25 fecharam juntas, porque a segunda responde a primeira:

> **É aptidão, e custa um marco. O requisito é refino 5 e nível 14.**

O requisito deixa de ser sorte. Pelo mesmo motivo, ele deixa de ser a mesma coisa para duas fichas idênticas — o antigo *"ter tirado um kokusen"* travava o jogador por dezenove sessões no refino 1.

Refino 5 cai no nível 10 para quem sempre escolhe refino, no 14 para quem vai meio a meio e no 18 para o generalista; o nível 14 é o que faz as duas primeiras rotas convergirem no mesmo marco. **Um mínimo de nível abaixo de 10 não morderia** — o refino 5 já chega lá.

**E o preço continua ruim de propósito.** A ~2% de dano por rodada, ele vale **0,2× um ponto de atributo**, que compra +10%. Numa campanha com no máximo sete aptidões e mediana perto de três, ninguém que olhe o número escolhe. Escolhe quem escolhe pelo grito — que é exatamente o que a v0.25 registrou que ele é, e o texto dele precisa dizer isso para ninguém montar ficha em cima.

**E o efeito apareceu, no fim da versão:**

> **Kokusen: +50% no impacto, depois de todos os valores resolvidos.**

Ou seja, em cima do crítico que já dobrou os dados — um crítico entrega `2D`, um kokusen entrega `3D`. Com o efeito na mão, a conta da v0.25 sai diferente:

| refino | chance no d100 | dano por rodada | sessões até o primeiro |
|---|---|---|---|
| 1 | 5% | +0,5% | 19,5 |
| 3 | 15% | +1,4% | 6,8 |
| 5 | 25% | +2,3% | 4,3 |
| 10 | 50% | **+4,5%** | 2,4 |

O teto é **4,5%**, e não os *"menos de 4%"* que a v0.25 registrou — aquele número foi calculado antes de o efeito existir. **A conclusão não muda:** continua sendo um quinto do que um ponto de atributo compra, e continua sendo peça de grito e não de planilha. O que muda é que agora dá para escrever validador em cima.

### Corrigido de método — dois erros meus, na revisão cética

O primeiro: uma versão da seção 5.3 dizia que o PE *"cresce mais rápido que a vida"*. Não cresce — o passo do PE é 4 a 6 por nível e o da vida é 7 a 10 com Constituição típica. O que sobe é a **razão** entre os dois, de 0,75 para 0,85 num Emanador, porque a vida perde um nível na parte que escala. **É a lição da v0.19 pela quinta vez: o número certo contra a base errada.**

O segundo achou uma contradição de verdade. A primeira redação da regra de arredondamento citava *"a vida por nível do Caminho"* como precedente do manual de arredondar para cima. Ela não é do manual — é nossa — e, pior, ela é um **ganho subindo**, que é o oposto do que a regra nova manda. A regra só fecha porque vale para **conta de mesa** e não para valor de tabela, e essa frase precisava estar escrita.

### Registrado — a cascata de kokusen é realimentação, e ela precisa de teto antes de existir

A ideia é a da obra: *o segundo kokusen num intervalo curto é mais fácil que o primeiro.* Quatro jeitos de fazer isso foram levantados, e **eles não são da mesma família.** Medidos no refino 5, depois do primeiro kokusen da cena:

| escada | dano por golpe | contra a linha de base |
|---|---|---|
| nada muda (o de hoje) | 0,5625 | +2,3% |
| ajuda no d100, +25 pontos | 0,5750 | +4,5% |
| dobra a chance, 25% → 50% | 0,5750 | +4,5% |
| vantagem no d100 | 0,5719 | +4,0% |
| **margem de crítico cai para 19** | 0,6250 | **+13,6%** |
| **margem cai para 18** | 0,6875 | **+25,0%** |
| **vantagem no ataque** | 0,8719 | **+58,5%** |

**As três primeiras mexem só no kokusen, e o kokusen é pequeno** — dobrar a chance dele rende 2,3 pontos. As duas últimas mexem em coisas que já valem sozinhas: a margem de crítico carrega os 10% do próprio crítico, e **9,1% do +13,6% vêm do dado a mais, antes de o kokusen entrar**; vantagem no ataque sobe o acerto de 50% para 75%, o que já é meio jogo de dano a mais.

**E "mais fácil depois do primeiro" é uma espiral, com o sinal trocado.** É o mesmo desenho que a v0.8 e a v0.23 diagnosticaram na exaustão: kokusen facilita kokusen facilita kokusen. Sem teto, quatro degraus numa cena levam o físico a **1,8× o dano de base** — e a coluna Rotina não tem para onde correr, então a tabela de encontro para de valer no meio da luta.

As três travas que a estrutura já usa e que servem aqui: **teto de degraus** (a exaustão para em três), **relógio curto** (a escada zera quando a cena acaba, no molde do "por cena"), e **uma escada só** — mexer na margem *ou* na chance, nunca nas duas, porque juntas elas se multiplicam.

### Em aberto

- **Nome do sistema.**
- **Qual escada de kokusen, e com que teto e que relógio.** A conta está acima; a escolha é de sabor.
- **Se cinco mestres contam luta parecido.** Aberto de propósito, e é a única coisa da peça 10 sem lista fechada por baixo.
- **A pergunta maior continua aberta:** a peça de aptidões ou a ficha + quick-start jogável. Os quatro buracos saíram da frente, e o número mudou de lado — das dezessete coisas que uma ficha de nível 2 precisa, **doze existem**, e das cinco que faltam **nenhuma morde numa missão de nível 2**: proteção nasce em 0, Pactos é opcional, Trilhas e aptidões só valem do nível 6 em diante, e XP não é preciso para uma missão só. Das dez pendências que só a mesa responde, **as dez são de nível 2**.

---

## [0.25] — 2026-08-10 · *manual v7.5*

Levantamento antes de escrever a peça de aptidões. A conferida contra o manual achou seis colisões e dois defeitos dentro do próprio Fundamento, e as decisões do Mizuki fecharam quatro peças de regra que não existiam. **O manual foi regerado: v7.5.**

### Decidido — as aptidões herdam a régua das Passivas, e não uma nova

O manual já tem a escada que a segunda economia de poder precisava, e ninguém tinha olhado para ela:

| Classe | Custa | Libera no nível | O que cabe |
|---|---|---|---|
| Livre | nada | 1 | ficção pura: não rola dado, não muda número, não faz ninguém rolar |
| 1 | 1 espaço | 1 | efeito pequeno, condicional, ou de informação |
| 2 | 2 espaços | 7 | efeito reativo, com limite por cena ou por descanso |
| 3 | 3 espaços | 13 | permanente, muda como você joga |

Três degraus, com **gate de nível embutido**, já conferidos pelo `pac7.py`. O `arquitetura.md` pedia uma trava para as aptidões — *"não produz dano e não escala com nível"* — porque não tinha régua. Tem.

### Decidido — cura existe nas duas economias, e por isso os nomes tinham que mudar

A Passiva **Reversão** já era Energia Reversa: *"uma vez por descanso curto, gasta a ação e recupera 5 × a sua maior Classe"*. Se a aptidão desse cura de graça, ela mataria a Passiva na hora — a mesma dominância que a peça 4 usou para não deixar feitiço virar ataque de oportunidade.

**As duas ficam, porque são coisas diferentes.** A Passiva é a cura **inata**, que vem da técnica, no molde do toque de cura do paladino. A aptidão é a cura **aprendida**, que gasta PE e se usa com frequência, no molde do conjurador. Duas economias, dois preços, dois nomes:

> A Passiva **Reversão** virou **Recomposição**. A aptidão fica com **Energia Reversa**.

### Corrigido no manual — dois defeitos dentro do Fundamento

**O manual tinha um termo órfão de outro sistema.** A Passiva **Reforço** dizia *"reduz o dano em 3 × Bônus de Treinamento"* — número que não existe aqui, porque o nosso se chama **Maestria**. Uma ocorrência só, e o `pac7.py` não pegava porque ele confere números e não vocabulário. Mesma família do Grau, três versões depois.

**A Passiva foi deletada, e não corrigida**, por decisão de design: *não existe redução de dano passiva neste sistema.* Fica o aviso para a peça de aptidões, que ia querer exatamente isso.

> **Pendente:** a Passiva **Casca** (Classe 3) — *"Redução de Dano 2 contra dano físico, vira 4 no nível 15"* — cai na mesma regra e **não** foi mexida. Decidir antes de fechar a v7.6.

**Técnica Máxima não é Expansão de Domínio.** O manual dizia que *"numa técnica que é feita de domínio, o domínio **é** a sua Técnica Máxima"*. Não é: a Técnica Máxima é o topo da técnica inata, e o domínio é a mesma técnica estendida sobre o território em volta. Uma técnica de domínio continua tendo Técnica Máxima como qualquer outra.

E **Expansão não vai ser aptidão**: ela mora na criação de personagem, presa a um mínimo de refino e de nível, comprada trocando espaços de feitiço conhecido. É a primeira coisa no sistema que o refino destrava fora da lista de aptidões.

### Corrigido no manual — três nomes, porque a obra ganha do manual

As aptidões vêm da obra e não têm para onde fugir. Quem muda é o lado menos entranhado, que é a regra da v0.5 aplicada de novo:

| era | virou | por quê |
|---|---|---|
| **Tema** Barreira | **Bloqueio** | a aptidão **Barreira Simples** é nome da obra |
| **Melhoria** Barreira | **Anteparo** | três coisas mecânicas não podem chamar Barreira |
| **Passiva** Domínio | **Afinidade** | ela escolhe um tema da Regra e fura cobertura leve — não tem nada a ver com domínio, e as aptidões **Domínio Simples** e **Extensão de Domínio** são da obra |

**A prosa em minúscula fica.** *"Dano dobrado contra barreiras"*, *"cancela um efeito contínuo ou uma barreira"*, *"uma barreira que absorva antes da vida"* — essas três agora apontam **certo**, porque barreira passou a ser exatamente a coisa que a aptidão produz. O que saiu foram os dois termos definidos.

Mexeu também no feitiço pronto **Muralha** e em três lugares do `pac7.py`. Os dois validadores passam e a estrutura é 326 parágrafos e 76 tabelas — um parágrafo a mais que a v7.4, porque a linha do domínio virou duas.

**O `.pdf` continua na v7.4.** Ele é exportado à mão; o `.docx` e o `.zip` estão na v7.5.

### Adicionado — o crítico, que era usado e nunca tinha sido escrito

Zero ocorrências no material do projeto. O manual usa a palavra uma vez, na Melhoria **Estilhaço** (*"em crítico, ou quando o alvo erra o Teste de Resistência por 5 ou mais"*), sem definir. E a mecânica de Kokusen pendura inteira nele.

> **20 natural numa rolagem de acerto é crítico, e você dobra os dados** — os da arma se for arma, os da Classe se for feitiço ou golpe canalizado. Nada mais dobra.

Três consequências que caem da frase sem regra a mais: **só existe crítico onde existe rolagem de acerto**, então feitiço que resolve por Teste de Resistência nunca crita; **comprar Certeiro ou Inescapável custa o crítico**, o que vira escolha de montagem em vez de bug; e **o crítico vale exatos 10% de dano por rodada** contra o alvo difícil, em qualquer nível, porque a taxa de acerto não deriva.

O crítico **não estoura** o teto de `4 × Classe em dados`: o teto é sobre o que se monta, não sobre o que o dado produz.

### Registrado — o Kokusen é caça-níquel, e a conta diz o tamanho

A proposta é: crítico no corpo a corpo → role d100, tire `5 × refino` ou menos.

| refino | chance no d100 | por ataque | por combate | combates até o 1º | sessões |
|---|---|---|---|---|---|
| 1 | 5% | 0,25% | 1,7% | 58 | **19** |
| 3 | 15% | 0,75% | 5,1% | 19 | 6 |
| 5 | 25% | 1,25% | 8,4% | 12 | 4 |
| 10 | 50% | 2,50% | 16,2% | 6 | 2 |

**Raro é o ponto**, e isso está decidido. O que a conta acrescenta é o tamanho: mesmo no refino 10 o kokusen soma **menos de 4%** de dano por rodada — 1,5% no nível 6, 3,7% no 30. Ele existe pelo grito na mesa, não pela planilha, e o texto dele precisa dizer isso para ninguém montar ficha em cima.

**Dois problemas ficam abertos**, e os dois são do requisito e não da mecânica: *"ter tirado um kokusen"* trava o jogador por **sorte** — dezenove sessões no refino 1, e duas fichas idênticas com acesso diferente. E **Kokusen Melhorado** paga um marco inteiro por ~2% de dano, competindo com Energia Reversa, que salva vidas.

### Registrado — o curandeiro nasce frágil por construção

Energia Reversa pede Essência 4 e Inteligência 4. Com nove pontos e teto 3 na criação, começar 3 e 3 gasta **seis dos nove** — sobram 1, 1 e 1 para Força, Destreza e **Constituição**, que é a maior alavanca de sobrevivência do sistema. Quem só escolhe refino chega a 4 e 4 no nível 10, e a 5 no nível 14.

Não é defeito: é o custo aparecendo onde deve. Mas é o número a olhar quando alguém reclamar que o curandeiro morre primeiro.

### Em aberto

- **Nome do sistema.**
- **A Passiva Casca**, que é a redução de dano passiva que sobrou.
- **O requisito do Kokusen Melhorado**, que hoje depende de sorte.
- **Se Kokusen Melhorado vale um marco** por ~2% de dano.

---

## [0.24] — 2026-08-08

Revisão cética do material inteiro em três camadas, antes de abrir a peça de aptidões. Os quatro validadores passam. Achou onze erros de texto, três buracos de regra e seis colisões de nome — metade delas nunca vista, porque nenhum validador olhava para lá.

### Adicionado — `conferir-nomes.py`, o quinto validador

O `conferir-pericias.py` já fazia checagem de colisão, **com 33 nomes**: as 23 perícias e os 10 ofícios. O projeto batizou muito mais — 15 Trilhas, 5 Caminhos, 14 Legados, 8 Origens, os termos de sistema. Nada disso passava por lugar nenhum, e foi por isso que três colisões ficaram no material desde a v0.14.

Cinco checagens: colisão para fora (contra o `.docx`), colisão para dentro (contra o próprio projeto), colisão fraca por distância de uma letra, **categoria errada** e termo morto vivo. Mais um modo de triagem, `--candidatos`, para rodar antes de batizar qualquer coisa.

**A quarta é a que ninguém teria escrito à mão.** Ela confere que todo lugar do projeto que cita uma Família, uma Forma, uma Melhoria ou uma Restrição usa um nome que **existe naquela categoria do manual**. Foi ela que pegou a ficha da Kaori, que tem *"Famílias Livres: Peso e Prender"* — e Peso é **Tema**, não Família; Prender não é nada, é uma palavra dentro da descrição de Controle.

**As listas fechadas são extraídas do `.docx` toda vez**, não copiadas: 9 Famílias, 15 Formas, 67 Melhorias, 19 Restrições, 70 Temas, 50 feitiços prontos e os 3 Fundamentos prontos. Quando o manual for regerado, elas se atualizam sozinhas — e o validador falha se a extração devolver um número diferente de nove Famílias, porque aí ele estaria aprovando sem ter lido nada. As perícias e ofícios ele importa do `conferir-pericias.py`, para não existirem duas listas que possam divergir.

Testado nos dois sentidos: numa cópia com os onze problemas consertados ele sai com código 0, e sete perturbações — nome que é Tema exato, nome dentro de feitiço pronto, palavra já batizada, nome dentro de outro nome batizado, Família inexistente, termo morto capitalizado, e o caso de uma letra que deve só avisar — acenderam cada uma a checagem certa.

### Corrigido — três colisões de nome que ninguém tinha visto

| Trilha | com o quê |
|---|---|
| **Sombra** (Evocador) | é **Tema** do manual, grupo Sentidos — e está dentro de **Estilo da Sombra**, o subsistema que ainda vai ser escrito |
| **Enxame** (Evocador) | é **Tema** do manual, grupo Criação |
| **Ofício** (Vanguarda) | é a categoria de **ofício**, com 15 ocorrências só na peça 7 |

A do Ofício é a mais constrangedora: a v0.15 pegou exatamente essa palavra colidindo, resolveu do lado da perícia — *"por isso a lista usa Artesania"* — e deixou a Trilha com o nome.

E duas das três antigas eram piores do que estava registrado. **Régua** não aparece "10x em prosa": ela é **um dos três Fundamentos prontos do manual**, o exemplo que a seção 2 usa para montar o primeiro feitiço. Termo definido, mesma categoria de Herança e Semente. E **Alcance** colide duas vezes — a Família, e o Legado **Alcance Impossível** escrito na v0.22.

### Corrigido de método — a v0.22 errou a categoria do manual

A entrada da v0.22 que rejeita **Herança** diz que ela *"é um dos Selos do manual"*. Não é. A lista *Vínculo · Troca · Cópia · … · Herança · Ausência* é o grupo **Conceito** da tabela de **Temas**. Selo, no manual, é *"um gesto, um som, uma condição visível"* — bater palma, dizer o nome do feitiço. Semente também é Tema, não Selo.

A rejeição estava certa e o motivo estava errado, o que importa porque é o motivo que a próxima checagem vai consultar. É a mesma confusão que produziu "Peso e Prender" como Família: **Tema escrito onde vai Família.** Duas vezes, em versões diferentes, sem ninguém notar — agora o validador não deixa.

### Decidido — os nomes das Trilhas, fechados

Pendência aberta desde a v0.14. Os seis que colidiam saíram; os nove que passaram ficam.

| Caminho | Trilhas |
|---|---|
| **Bastião** | Muro · Punho · Brasa |
| **Vanguarda** | Estocada · **Batedor** · **Executor** |
| **Guia** | Elo · **Sutura** · **Perímetro** |
| **Emanador** | Torrente · Repertório · Arremate |
| **Evocador** | **Servo** · **Matilha** · Coro |

**O Executor mudou de conteúdo junto com o nome.** Ele era *"golpe pesado com arma, ritmo de trabalho, o molde do Nanami"*; virou o corpo a corpo puro. Isso arruma a Vanguarda inteira, que passa a responder a mesma pergunta — *como você alcança o inimigo* — de três jeitos que não se sobrepõem: Estocada com um pé em feitiço, Batedor sem encostar, Executor só encostando. O Nanami vira exemplo, e não molde.

**Sutura ganhou de Respiro por uma frase de regra viva.** A peça 10 diz *"se um respiro devolvesse vida, a coisa mais rara da obra viraria conveniência"* — e a Trilha é justamente a que devolve. O nome brigaria com o texto. Colisão que nenhum validador pega, porque "respiro" ali é prosa.

**Não foi find/replace, pelo mesmo motivo do Grau.** Três dos seis mudam de gênero — *a Régua* → *o Perímetro*, *a Sombra* → *o Servo*, *o Fôlego* → *a Sutura*. E havia duas armadilhas que uma substituição cega destruiria: as ocorrências de "ofício" na peça 7 são **a categoria**, e as de "Sombra" nas peças 8 e 9 são **Estilo da Sombra**. As duas ficam.

Duas sugestões morreram na triagem antes de entrar: **Alento** fica a uma letra de **Lento**, que é Restrição; **Rédea** fica a uma letra de **Rede**, que é feitiço pronto. Nenhuma das duas se pega no olho.

### Decidido — quem ganha ataque extra, e em que nível

**Buraco de regra, não erro de balanço.** Da v0.14 até aqui o ataque extra tinha conta, argumento e correção — e nunca teve dono. O único texto era *"os Caminhos físicos ganham e os meio-arcanos não"*, que é a mesma divisão em duas famílias que a v0.15 registra como tendo deixado o Guia sem número de PE. Ela não cobre os cinco Caminhos.

E o achado nº 2 da v0.20 — *"o Guia pode estar dominado pela Vanguarda"* — dependia inteiro de como essa divisão fosse resolvida. Não era achado fechado; era conclusão apoiada numa classificação que ninguém tinha escrito.

> **Bastião e Vanguarda ganham no nível 6, pelo Caminho.**
> **Arremate e Coro ganham pela Trilha.**
> **O Guia não ganha por nenhuma rota.**

**Num Caminho de técnica, ataque extra é trocar o Classe 0 pelo golpe simples, não somar.** Somando, o conjurador de perto fica com três ações e vai a +61% da Rotina no nível 2 e +22% no 10; trocando, ele cai exatamente na linha do físico, que a peça 6 já aprovou. E somar quebra o único argumento que aprova o ataque extra — *a Rotina já é feitiço mais Classe 0, então o extra do físico é o espelho*.

**O Coro não custa nada a mais**, e isso caiu de graça: a regra da v0.14 diz que o dono e todas as invocações somados entregam **uma** Rotina. É teto de saída, não de número de ações. Os dois golpes do dono e o da invocação continuam saindo do mesmo orçamento — as ações se redistribuem, o dano não sobe. A exceção de economia de ação que estava aberta no Coro já estava paga desde a v0.14, e ninguém tinha percebido.

**O Guia fica coerente ficando de fora.** Ele é o único Caminho que não oferece um segundo golpe; quem quiser lutar de Guia paga pela técnica, no orçamento do Fundamento, como todo mundo. O que era *"pode estar dominado"* vira uma pergunta fechada com número: **o que Elo, Sutura e Perímetro entregam que valha um golpe por rodada?**

### Corrigido — a ficha da Kaori tinha dois nomes que não existem

É a página que todo jogador novo vai copiar, e ela citava **três** categorias erradas de uma vez.

*Famílias Livres: **Peso e Prender***. Peso é **Tema** do manual e preço de Liberação Máxima; Prender não é categoria nenhuma — é uma palavra dentro da descrição de **Controle**. As três Fechadas dela (Amparo, Área, Auxiliares) estavam certas, o que é justamente o que fez ninguém desconfiar da linha. Viraram **Controle e Castigo**: Controle é literalmente *"derrubar, prender, calar, barreira, terreno"*, que é a palavra da Regra dela; Castigo é *"fazer o dano render mais"*, que é o "mais pesado". As duas dizem a mesma coisa que Peso e Prender diziam, com nomes que existem.

E o ofício livre dela era **Artesania**, que virou Entalhador na v0.16. Como é escolha livre, qualquer um dos dez servia; ficou **Caligrafia**, que conversa com ela ser Descendente de um ramo de clã que perdeu o nome.

### Corrigido — a tabela das três alavancas tinha um número da v0.18

A linha do Caminho dizia **+36% / +43% / +44%**, e nenhuma fórmula do projeto reproduzia isso. O **+36%** é o número da v0.18, de quando a faixa era "de 6 para 10 de vida por nível" — e ele sobreviveu à revisão da v0.20, que montou essa tabela **justamente para acertar as bases**. Medido igual às outras duas linhas: **+56% / +46% / +44%**.

**E o par que virou pergunta de playtest mistura bases.** *"Constituição compra +113% contra os +56% da Destreza"* compara Constituição de **0 a 6** com Destreza de **1 a 6**. Na mesma base é **+79% contra +56%** — a Constituição lidera por **1,4×**, não por 2×. A peça 1 já media certo na tabela e citava o 113% à parte; o ESTADO-ATUAL é que juntava os dois como se fossem comparáveis. Não mexemos em nenhum número de regra: só a comparação estava errada, e a diferença é entre "um atributo puxou" e "um atributo dominou".

É a quarta vez que o mesmo tipo de erro aparece — v0.16, contagem não era valor; v0.17, a referência óbvia não era a certa; v0.19, o número certo contra a base errada; agora, dois números certos comparados entre si em bases diferentes.

### Corrigido — nove documentos que tinham ficado para trás

| onde | o quê |
|---|---|
| peça 1 | parágrafo duplicado em "Constituição entra cheia", e o primeiro terminava em *"Indo do valor 1 ao 6:"* sem tabela nenhuma depois |
| peça 3 | *"três peças competem"* pela reação, listando quatro |
| peça 5 | *"Treino em três perícias"* — são duas fixas e quatro livres desde a v0.16 |
| peça 7 | cabeçalho parado na v0.16, com conteúdo da v0.17 e da v0.22 dentro |
| peça 7 | *"Quantos ofícios uma Origem deve dar. Hoje, nenhum"* — a seção 6 do mesmo arquivo dá um |
| peça 8 | *"O catálogo de Origens... a maior lacuna desta peça"*, que existe desde a v0.22 e é apontado duas vezes pela própria peça |
| `arquitetura.md` | dizia "manual v7.3", e o cabeçalho dizia "sincronizada na v0.15" com correção da v0.22 dentro |
| `ESTADO-ATUAL.md` | v7.3 e v7.4 no mesmo arquivo; rabo de tabela morta listando Descanso como pendente; "aplicar Grau → Classe no `.docx`", resolvido na v0.20 |
| `LEIA-ME.md` | parou na v0.20 — "sete peças, três validadores, ainda falta a criação de personagem" |

O *"Quantos ofícios uma Origem dá"* não virou só uma correção: virou pergunta melhor. **O extra da Origem não é escolha de igual para igual** — perícia sem treino você rola, ofício sem treino não. O ofício compra o acesso inteiro a uma coluna fechada; a perícia compra +maestria num teste que você já podia tentar, de +1 no nível 2 a +4 no 30. Medir se alguém escolhe a perícia.

E o **Sentir Energia** saiu da lista de problemas abertos do `ESTADO-ATUAL.md`: a v0.21 fechou como decisão registrada, e ele continuava listado como aberto três versões depois.

### Registrado — três buracos de regra, e um degrau maior do que o texto promete

Nenhum é erro de balanço; são coisas que o material **cita e nunca escreve**, e que dois mestres resolveriam diferente:

- **O PE máximo nunca teve fórmula.** Só a instância do nível 2 na peça 8 (`PE por nível × 2`). Não dá para inferir da vida, que usa `(nível − 1)` e soma atributo.
- **Arredondamento não existe.** "Metade do máximo" e "25% do máximo" caem em fração em cerca de 30% das fichas, e em todo Guia e Vanguarda de nível ímpar. O exemplo da peça 10 arredonda para baixo sem dizer.
- **"Da quarta luta do dia"** nunca define o que conta como luta.

E o **degrau 1 de exaustão** dá desvantagem, que vale **−25 pp no pico** — maior que treinar um Teste de Resistência (+10), maior que a maestria de uma campanha inteira (+20 no nível 30), maior que investir um atributo de 0 a 3 (+15). O texto o vende como o degrau leve. A escada por eixo continua boa; o que falta é o texto dizer o tamanho, e o `conferir-descanso.py` conferir magnitude e não só qual eixo cada degrau toca.

### Achado — o Legado tem teto de quantidade, não de magnitude

Um por ficha, e conferir isso leva um segundo. Mas a faixa entre os catorze é enorme: de **Irmãos** (sente outro Feto por perto, zero em rolagem) a **Não Sou Gente** (imune a veneno, doença e o que ataca corpo humano — apaga uma família de ameaça e boa parte do TR Vigor). A trava escrita, *"não produz dano e não escala com nível"*, não pega imunidade.

Três coisas específicas: **Instinto Bruto está metade morto**, porque "use Sentir Energia no lugar de Percepção" é trocar Essência por Essência desde a v0.16 — o Legado foi escrito na v0.22 pressupondo o quadro anterior. **O relógio não é o mesmo dentro do par** — Latente e Receptáculo oferecem 1×/cena contra 1×/sessão, Reencarnado oferece 1×/arco contra permanente, e pela escada da peça 10 isso é 2× e 5× de diferença numa escolha apresentada como par. E **Treino de Berço** é o único que mexe em número de ficha: ele abre a rota Descendente com **10 perícias, 43%**, fora da faixa de 30–42% que o validador cobra e fora do checklist do mestre, que só conhece "8 e 3 ou 9 e 2".

### Em aberto

- **Nome do sistema.** A última pendência de nome.
- Os quatro achados acima que pedem decisão: o teto de magnitude do Legado, o conserto do Instinto Bruto, as três linhas de regra que faltam, e o texto da exaustão.

---

## [0.23] — 2026-08-07

### Adicionado

- `03-mecanica/10-descanso-e-recuperacao.md` — o manual citava descanso **seis vezes** e nunca definia nenhum dos dois. Sem esta peça ninguém fechava a primeira sessão.
- `03-mecanica/conferir-descanso.py` — quarto validador. Confere que o piso fora da base é estável, que a exaustão não espirala, que nenhum degrau toca a rolagem de luta antes do último, e que os quatro relógios estão ordenados.

### Decidido — a ordem das peças veio de simular uma campanha, não de tamanho

A escolha de escrever descanso antes de Técnica Marcial saiu de perguntar **quando o jogo trava**, e não de qual peça é maior:

| quando | o que travava |
|---|---|
| **fim da sessão 1** | descanso |
| **sessão 2** | equipamento — `Defesa = 10 + Destreza + proteção`, e proteção não tem número |
| **nível 6**, o primeiro marco | aptidões — você escolhe refino e ganha uma, e elas não existem |
| **depois do nível 2** | Trilhas |

E as duas peças de criação que pareciam ser a próxima coisa **estão bloqueadas**: Técnica Marcial depende de **equipamento** (a Maki fere maldição só com ferramenta amaldiçoada, e o preço não existe) e Estilo da Sombra depende das **aptidões** (a rota da Shoko é literalmente "o poder vem de aptidão"). São a quarta e a quinta economia de poder, e a segunda ainda não tem teto escrito.

### Decidido — dois descansos, os dois de ficção

> **Curto — você parou entre uma luta e outra. Longo — a missão acabou.**

**Sem relógio de horas.** Numa Guilda com cinco a sete mestres, *"dá para descansar uma hora aqui?"* é exatamente o tipo de pergunta que cada um responde diferente. Gatilho de ficção, dois mestres arbitram igual.

### Decidido — ambiente propício é o eixo único

Quase tudo na peça depende de uma pergunta só: **o lugar tem recursos?** Talismã, kit, comida, alguém que sabe costurar um corte.

**Lista fechada de exemplos, e o mestre com a palavra final.** É o mesmo padrão dos traços de Origem: a lista existe para ele não decidir do zero, não para amarrá-lo.

| | curto | longo em lugar propício | longo fora |
|---|---|---|---|
| **PE** | 25% do máximo | cheio | **metade do máximo** |
| **Vida** | nada | cheia | **metade do máximo** |
| **Exaustão** | — | zera | não zera |
| **Integridade** | — | cheia | **cheia** |

**A Integridade é a única coisa que o ambiente não toca**, e o motivo é o mesmo da v0.17: a alma não é o corpo. Isso mantém a regra do manual literalmente intacta.

**O descanso curto não devolve vida**, e é decisão: em Jujutsu Kaisen quem conserta gente é a Energia Reversa e a Shoko. Se um respiro devolvesse vida, a coisa mais rara da obra viraria conveniência.

### Achado — "metade" tem uma leitura que colapsa

A regra diz **metade do seu máximo**, e a frase precisa dizer isso com todas as letras. A leitura alternativa — *metade do que você tem* — colapsa:

| Emanador nv10, pool 60, sempre fora da base | dia 1 | dia 2 | dia 3 | dia 4 |
|---|---|---|---|---|
| metade do **máximo** (a regra) | 30 | 30 | 30 | 30 |
| metade do **atual** (a leitura ruim) | 30 | 15 | 7 | 3 |

O validador confere que o piso é estável, e falha se a regra escorregar para a outra leitura.

### Decidido — exaustão, e o teto que impede a espiral

**Não existe no manual** — zero ocorrências de exaustão, cansaço ou fadiga. É peça nova, e ela existe porque **sem ela o descanso curto não tem limite**.

> **Da quarta luta do dia em diante, cada luta dá um degrau. Máximo de três.**

| degrau | o que pega | curto fora de lugar propício |
|---|---|---|
| 1 | desvantagem em perícia e ofício | 15% |
| 2 | deslocamento cai para 6 m | 5% |
| 3 | desvantagem em ataque e Teste de Resistência | nada |

**A ordem não é aleatória: o primeiro degrau pega fora de combate, o segundo pega posicionamento, e só o terceiro pega a rolagem de luta.** Quem está cansado começa a falhar no que não mata antes de falhar no que mata — e o validador **falha** se algum degrau anterior ao último tocar a rolagem.

**O teto de três existe porque a combinação escolhida é uma espiral.** Exaustão que não zera fora da base, somada a degraus crescentes, é o mesmo defeito que a v0.8 diagnosticou: quem está cansado erra mais, apanha mais, luta mais tempo e cansa mais. Sem teto, dez dias de campo dariam vinte degraus.

**E o mestre pode tirar um degrau quando a ficção pedir** — uma noite de sono de verdade, um dia parado. A válvula só anda para o lado do jogador: o mestre nunca adiciona degrau fora da regra.

### Decidido — os quatro relógios, e por que o manual tinha dois nomes

O manual usa **"por cena"**, **"por descanso"** e **"por dia"** sem nunca dizer como se ordenam. Agora dá:

**por cena → por descanso curto → por dia → por descanso longo**, do mais frequente ao menos.

**"Por dia" e "por descanso longo" não são a mesma coisa, e a diferença é o ponto.** Uma missão pode durar cinco dias: quem tem "uma vez por dia" recarrega cinco vezes, quem tem "uma vez por descanso longo" recarrega uma. É por isso que o manual dá "por dia" para a Passiva Segunda Natureza e "descanso longo" para a Integridade — a segunda é muito mais forte, e o relógio mais lento é o preço.

### O orçamento de missão

**PE é o que você tem para a missão inteira.** A coluna do manual — *"quantas vezes você lança o seu melhor feitiço"* — passa a significar **por missão**, e vira o piso em vez do teto:

| lutas no dia | PE acumulado |
|---|---|
| 3 | 1,50 × pool |
| 4 | 1,75 × pool — e a exaustão entra |

É também o que **faz o golpe simples e o Classe 0 existirem**: eles são o que sobra quando o combustível acaba, e num sistema onde o combustível volta cheio a cada respiro eles não teriam razão de ser.

### Em aberto

- **Se três lutas de graça é o número certo.** Se a maioria das sessões tem duas lutas, a exaustão nunca dispara e a peça vira decoração.
- **Se o descanso curto devia devolver alguma vida.** Se o grupo sem curandeiro travar entre lutas, o conserto barato é devolver só em ambiente propício.
- **O que acontece com quem passa semanas em campo.** O teto de três impede a espiral e também diz que dois meses no mato doem igual a três dias.

---

## [0.22] — 2026-08-07

### Adicionado

- `03-mecanica/09-origens.md` — o catálogo. Fecha a maior lacuna da criação de personagem, que era a única coisa no sistema em que um número dependia de julgamento do mestre.
- `conferir-pericias.py` ganhou as listas de Origem e duas checagens: as quatro perícias de cada uma existem no quadro, e nenhuma Origem tem a lista inteira já fixada por um Caminho — se tivesse, a escolha dela morreria.

### Decidido — três camadas, não uma lista

| | |
|---|---|
| **Cinco principais** | Latente · Receptáculo · Descendente · Reencarnado · Feto |
| **Sub-origem** | **Sem Técnica**, que se soma a qualquer uma das cinco |
| **Duas especiais** | **Corpo Amaldiçoado** e **Restrição Celestial** — não aceitam a sub-origem, porque são especiais |

O cruzamento é o que a estrutura compra: **Descendente Sem Técnica** é o caso da Miwa, nome de peso e nenhuma técnica de clã. Uma lista plana de oito perderia isso.

### Corrigido pelo cânone — duas categorias mudaram de nome antes de existirem

A checagem contra a obra pegou uma coisa que teria nascido errada.

**O Junpei tem técnica inata.** Escória da Lua, veneno. O que o Mahito fez foi *modificar o cérebro dele para que ela despertasse antes da hora* — o poder era dele, o acesso veio de fora. Ele estava classificado como "recebeu técnica de fonte externa" e **virou Latente**.

Com ele fora, a categoria mudou de recorte e de nome: **Maculado virou Receptáculo**, e passou a ser *"você carrega alguma coisa, e ela ainda está aí"* — Itadori com o Sukuna, Hana Kurusu com o Anjo.

E **Desperto virou Reencarnado**, o que deixou a fronteira entre as duas nítida. **É a distinção que o próprio mangá faz:** sobre a Hana Kurusu, o texto diz que *"ao contrário da maioria das encarnações, o Anjo vive simbioticamente dentro dela em vez de sobrescrever a consciência"*.

> **Receptáculo é simbiose — os dois estão lá. Reencarnado é sobrescrita — sobrou um.**

O resto do cânone conferiu: **Kashimo** aceitou virar objeto amaldiçoado e encarnar num corpo que o Kenjaku preparou; **Panda** é Cadáver Amaldiçoado de Mutação Abrupta feito pelo Yaga, com três núcleos; **Mechamaru** troca corpo inútil por energia enorme; **Maki e Toji** nasceram sem energia nenhuma e ganharam corpo sobre-humano.

### Decidido — a patente sai da Origem

**Todo personagem começa Grau 4**, venha de onde vier. A patente é eixo social e sobe por feito.

Isso contradizia três documentos, e os três foram corrigidos: a peça 8 dizia que a Origem dava a patente inicial, a peça 2 usava o Yuta como justificativa, e o `arquitetura.md` chamava a Origem de *"o lugar natural da patente inicial"*.

**O caso do Yuta continua existindo na ficção** — a instituição classifica quem ela quiser onde ela quiser. O que sai é a patente ser **produto da Origem na criação**, que criaria a origem que começa na frente. É o mesmo argumento que a v0.10 usou para tirar atributo da Origem.

### Decidido — o Legado, e o teto que ele nasce com

> **O nome saiu de "talento" numa checagem que pegou colisão antes de ela existir.**
>
> A ideia era chamar de **Herança**, para remeter à Origem. **Herança é um dos Selos do manual** — ela está na lista *Vínculo · Troca · Cópia · Contrato · Dívida · Sorte · Aposta · Julgamento · Regra · Registro · Valor · Verdade · Segredo · Herança · Ausência*. Termo definido, mesma armadilha do Grau.
>
> Testadas em seguida: **Marca** (8× no manual), **Sangue** (9×) e **Semente** (também Selo) colidem igual. **Legado** tem zero ocorrência no manual e zero no projeto, e diz a mesma coisa que Herança dizia. Quatro nomes conferidos antes de um entrar no material — foi mais barato que o Grau, que só foi pego depois de 76 tabelas escritas.

A Origem dá **um Legado**, escolhido entre dois. **Um só na ficha inteira: o sistema nunca concede outro.**

Legado é economia de poder nova, e o `arquitetura.md` já chama as aptidões de *"o risco maior da estrutura inteira"* por não terem teto escrito. **Então esta nasce com o teto embutido, e o teto é o menor possível** — toda ficha tem exatamente um, e conferir isso leva um segundo. Legado não produz dano e não escala com nível, pela mesma regra das aptidões.

### Decidido — o resto do que a Origem entrega

**Uma perícia da lista de quatro dela, uma perícia livre, e um extra que o jogador escolhe: um ofício livre ou mais uma perícia.** Mais um Teste de Resistência (qualquer um dos quatro) e um traço, do catálogo dela ou escrito com aprovação.

O extra opcional cria duas rotas, e **as duas cabem na faixa**:

| rota | perícias | ofícios |
|---|---|---|
| Origem pega o ofício | 8 de 23 = **35%** | 3 de 10 = 30% |
| Origem pega a perícia | 9 de 23 = **39%** | 2 de 10 = 20% |

### Registrado — seis das nove rotas já rodam

| rota | jogável |
|---|---|
| as cinco principais | **sim** — vão para o Fundamento, que existe e está validado |
| Restrição Celestial, ramo do Mechamaru | **sim** — Fundamento normal, com o corpo limitado escrito na ficha |
| qualquer uma **+ Sem Técnica** | não — precisa de **Aptidão** ou **Estilo da Sombra** |
| Corpo Amaldiçoado | não — precisa de **Técnica Marcial** |
| Restrição Celestial, ramo da Maki | não — precisa de **Técnica Marcial** |

As três que faltam dependem de um subsistema paralelo ao Fundamento, e ele é a próxima peça. Elas entram no catálogo assim mesmo porque **a Origem é decisão fechada; o que falta é a montagem**.

### Corrigido

- A lista do Reencarnado tinha **Táticas**, que foi removida do quadro na v0.16. Virou Investigação. O validador agora falha se uma Origem oferecer perícia que não existe.

### Decidido — a próxima peça são duas, não uma

**Técnica Marcial** e **Estilo da Sombra** vão ser sistemas separados, porque resolvem problemas diferentes:

| | quem | o problema |
|---|---|---|
| **Técnica Marcial** | Panda, Maki, Toji | **não tem energia amaldiçoada.** Sem PE, sem golpe canalizado, sem Sentir Energia. Paga com o corpo e com ferramenta amaldiçoada |
| **Estilo da Sombra** | Miwa, Kusakabe | **tem energia e não tem técnica.** Tem PE e não tem o que gastar nele. Paga com PE, como todo mundo |

Um motor único acharia os dois: o Panda troca de núcleo e a Miwa saca espada, e forçar isso num orçamento só apagaria a diferença. O custo aceito é balancear duas economias novas em vez de uma.

### Em aberto

- **Técnica Marcial e Estilo da Sombra**, que destravam três rotas.
- **A Aptidão como rota de criação** — a Shoko existe na obra e não na regra, e isso amarra com os degraus de refino, que também não foram escritos.
- **Se a perícia livre da Origem devia ser da lista também.** É o último lugar da criação em que um número depende de julgamento.
- **Se um Legado por ficha é pouco.** Se parecer decoração no playtest, o conserto é mais opções por Origem, não mais Legados por ficha.

---

## [0.21] — 2026-08-07

### Adicionado

- `03-mecanica/08-criacao-de-personagem.md` — **a peça em que tudo se encontra.** Não inventa regra: junta as sete anteriores e o manual do Fundamento na ordem em que a pessoa senta e preenche.
- `99-arquivo/` — pasta de material morto, com `LEIA-ME.md` próprio e três subpastas por assunto.

### Decidido — a ordem dos oito passos, e por que o passo 2 existe

> **Origem → a Regra em uma frase → Caminho → Atributos → a técnica inteira → Perícias e ofícios → os números → Pactos.**

O `arquitetura.md` já tinha levantado a tensão: escrever a técnica inteira leva tempo, mas **escolher o Caminho antes de saber o que a técnica faz ancora o jogador num papel de equipe antes de ele saber o que o personagem é**. Quem escolhe "eu sou o tanque" e só depois escreve a técnica tende a escrever uma técnica de tanque — o oposto do pilar 1.

A saída é partir a técnica em duas: a **Regra sai no passo 2**, em uma frase, e o resto fica para o passo 5. O jogador escolhe o Caminho já sabendo o que a técnica dele é, e ainda não gastou a parte longa.

### Decidido — Sentir Energia fica como está

O achado da v0.20 dizia que ela falha no teste do bônus automático: sendo a mais rolada da mesa, toda ficha eficaz gasta uma das quatro escolhas livres nela, então o Caminho entrega três livres e uma obrigatória.

**Aceito conscientemente, e o argumento é do Mizuki:** sempre vai existir perícia melhor que outra, e as pessoas escolhem por querer ser únicas, não só por eficiência — é para isso que a lista tem vinte e três opções. Deixa de ser problema aberto e passa a ser decisão registrada.

### A ficha de exemplo, conferida

A peça traz uma ficha inteira — a Kaori, Bastião de nível 2 — e cada número dela foi conferido contra as fórmulas: vida 23, Integridade 28, PE 8, Defesa 12, CD 13.

O que ela mostra sem precisar dizer: **ela acerta d20+3 com o soco e d20+3 com o feitiço.** Não é coincidência — é o `2 + maestria` da v0.9 calibrado exatamente para o conjurador empatar com o guerreiro do nível 2 ao 30.

### Registrado — o que a criação ainda contorna

Quatro coisas entram como provisórias, cada uma com a saída escrita no ponto do texto onde ela pesa, e não numa nota no fim:

- **Origens** — escrita livre com aprovação do mestre. É a única em que um número depende de julgamento, e a maior lacuna da peça.
- **Pactos** — só a trava e a promessa.
- **Equipamento** — a ficha nasce com proteção 0. Não trava a criação; trava a segunda sessão.
- **Trilhas** — não afetam o nível 2, afetam a primeira subida.

### Alterado — o arquivo morto saiu do caminho

Material superado espalhado pelas pastas vivas atrapalha busca e ocupa a atenção de quem lê. Agora tem lugar:

| pasta | o que foi para lá |
|---|---|
| `99-arquivo/secoes-substituidas/` | a lista de catorze perícias e o quadro de quatro Caminhos, **extraídos de dentro das peças 4 e 5** |
| `99-arquivo/construcao-das-skills/` | o benchmark das quatro skills, o `feedback.json` e o visualizador — 200 KB que ninguém consulta |
| `99-arquivo/ferramentas-de-decisao/` | o comparador de curvas, que escolheu o d20 na v0.3 e está aposentado desde então |
| `99-arquivo/` | o `PROMPT-DE-CONTINUIDADE.md`, que o `ESTADO-ATUAL.md` faz melhor |

**A mudança de método que vale registrar:** até aqui, seção superada ficava dentro da peça viva com um aviso em cima. Isso não resolve — ela continua aparecendo em busca e continua ocupando quem lê. **Agora ela sai inteira**, e na peça viva fica só um parágrafo com o que sobreviveu e um ponteiro. As peças 4 e 5 encolheram e ficaram mais fáceis de ler.

Cada arquivo arquivado carrega no topo: de onde saiu, o que o substituiu, em que versão, **por que morreu** e o que dele sobreviveu. A última linha é a que não dá para reconstruir depois.

**Aviso para quem ler as entradas antigas deste arquivo:** as versões da v0.2 à v0.4 citam caminhos que não existem mais — `workspace-skills/`, `03-mecanica/comparador-de-curvas.html`, `feedback.json` na raiz. Elas ficam como estão, porque descrevem o que era verdade na época. A tabela acima é o mapa de para onde cada coisa foi.

---

## [0.20] — 2026-08-06

Revisão cética do material inteiro antes de abrir a criação de personagem, em três camadas: automática, textual e de design. Os três validadores passam. Achou quatro erros de texto e três problemas de design que nenhum validador pegaria. E fechou a pendência mais antiga do projeto, aberta desde a v0.3.

### Aplicado — Grau virou Classe no manual do Fundamento

A colisão estava aberta desde a v0.3 e decidida desde a v0.6: **"grau" é o termo da obra para a patente do feiticeiro**, a Guilda fala assim há anos, e o manual usava a mesma palavra para o tamanho do feitiço. Agora o manual está na **v7.4** e usa Classe.

**Não foi find/replace, e essa é a parte que vale registrar.** *Grau* é masculino e *Classe* é feminino. Uma substituição cega produz "do Classe", "um Classe", "o seu maior Classe". Foram **243 linhas alteradas** nos nove arquivos de fonte, e **dez precisaram de concordância que nenhuma regra automática pega**:

- artigo e preposição — *do Grau* → *da Classe*, *num Grau* → *numa Classe*, *pelo Grau* → *pela Classe*
- markdown no meio — `um **Grau**` não casava com a regra de `um Grau`, e escapou na primeira passada
- **pronome** — *"Escolha o Grau… **Ele** define os pontos"* → *"Escolha a Classe… **Ela** define os pontos"*

O método que achou os três últimos foi um linter escrito para o caso: procurar artigo masculino colado em Classe, no texto **renderizado**, não na fonte. Ele acusou oito ocorrências, das quais **cinco eram falso positivo** — *"o mesmo número dos pontos dele"* e *"de que Classe ele era"* têm "ele" se referindo ao feitiço e ao personagem, não à Classe. Só leitura separa esses casos.

**Um efeito colateral que precisou de decisão:** o manual tinha uma frase em prosa — *"se a sua mesa tem uma classe que bate em vez de conjurar"* — que passaria a colidir com o termo novo. Virou *"um tipo de personagem que bate"*.

Conferido depois de gerar: **0 ocorrências de "Grau"** como palavra inteira, 198 de "Classe", `pac7.py` e `v7.py` passando, e a estrutura idêntica — 325 parágrafos e 76 tabelas nos dois. As treze aparições de "grau" que sobram no texto são todas **"degrau"**, palavra diferente.

O `.docx`, o `.pdf` e o `.zip` de fontes foram regenerados e instalados.

### Corrigido — erros de texto

- **Parágrafo duplicado na peça 1.** "Vida é a única alavanca que a trava do Caminho deixa aberta" aparecia duas vezes seguidas, como seção e como parágrafo, dizendo a mesma coisa. Resíduo de edição da v0.18.
- **Dois números contraditórios para a mesma coisa, na mesma seção.** A peça 1 dizia que Constituição compra +45% de sobrevivência no nível 10 numa tabela e **+113%** noutra, dez linhas abaixo. A primeira ficou parada na fórmula da v0.18. Pior: as duas usavam bases diferentes — uma media do valor 1 ao 6, a outra do 0 ao 6. **Agora as três alavancas aparecem numa tabela só, todas medidas de 1 a 6**, com o valor de 0 a 6 citado à parte.
- **A peça 1 ainda usava a escada de perícia CD 12/16/20**, que não existe. A oficial é 10/14/18/22/26, corrigida no validador desde a v0.17 mas não no texto.
- **Listas de "Em aberto" apontando para coisas já resolvidas** em cinco das sete peças — quantos TRs se treina, de onde vem o treino, o quadro de Caminhos, a lista de catorze perícias, se o ataque de oportunidade usa a rolagem comum. Cada uma virou uma linha de "resolvido e tirado daqui", com o ponteiro para onde a resposta mora.

### Achado — Sentir Energia falha no teste do bônus automático

A peça 7 declara: *"Sentir Energia não é fixa de ninguém, e isso é escolha. Livre para todos, ela vira decisão de ficha — e o feiticeiro ruim de sentir energia passa a caber."*

**Não vira.** Ela é a perícia mais rolada da mesa, com o dobro do peso da segunda colocada e o quádruplo das outras dezessete. Com quatro escolhas livres entre vinte e três opções e uma delas valendo por quatro, **toda montagem que se importe com eficácia pega**.

Na prática o Caminho dá **três livres e uma obrigatória**, não quatro livres. E o Itadori ruim de sentir energia só existe se o jogador escolher ser pior de propósito — o que é armadilha, não escolha.

Três saídas, nenhuma aplicada ainda: dar Sentir Energia de graça a todo feiticeiro e assumir que é o piso; fixá-la em alguns Caminhos e aceitar a vantagem; ou aceitar que são três livres e dizer isso no texto em vez de prometer quatro.

### Achado — o Guia pode estar dominado pela Vanguarda

| | vida/nível | PE/nível | ataque extra |
|---|---|---|---|
| Vanguarda | 5 | 5 | **sim** |
| Guia | 5 | 5 | não |

**Números idênticos, e a Vanguarda tem um recurso a mais.** É o único par do sistema em que dois Caminhos custam igual e um leva algo que o outro não leva.

O Guia só escapa se as Trilhas dele entregarem algo que valha um ataque por rodada. Hoje as Trilhas são três linhas de descrição sem número nenhum, então **não dá para saber** — não é erro provado, é buraco de verificação. Fica travado até a peça de Trilhas existir, e é a primeira coisa a conferir quando ela existir.

### Achado — o ofício não passa no filtro do multi-mestre

A regra diz que **o mestre escolhe o atributo que o ofício usa, na hora**. Forjar uma lâmina é Força ou Inteligência? Falsificar é Destreza ou Essência?

Dois mestres que nunca conversaram cobram atributos diferentes pelo mesmo ofício, e a diferença pode ser de cinco pontos na rolagem. É a segunda regra do sistema em que **um número depende de julgamento** — a outra é a Origem dando duas perícias livres, que já está marcada como provisória.

O conserto padrão do projeto se aplica: uma tabela pequena, com o atributo padrão de cada ofício e uma linha dizendo quando o mestre pode trocar.

### Registrado — quatro premissas herdadas que nunca foram marcadas

A peça 3 fez esse exercício para a economia de ação e concluiu, honestamente, *"mantemos por custo de retrabalho, não por mérito"*. Quatro outras nunca passaram por ele:

- **Vida por Caminho.** Entrou na v0.19 com argumento próprio — é a única alavanca que a trava do Caminho deixa aberta —, o que é melhor que herdar cego, mas não está escrito como herança do d20.
- **Vida como reservatório único que esvazia.** Nunca questionado. Em Jujutsu Kaisen o ferimento importa narrativamente, e um medidor só pode não ser o que a obra faz.
- **Nível inteiro subindo de um em um.** O sistema só usa marcos de quatro em quatro; os níveis entre marcos entregam apenas Classe de feitiço. Vale perguntar se o nível precisa existir na granularidade que tem.
- **Rolagem de acerto separada da de dano.** Herdada do Fundamento, que já é d20.

Nenhuma é problema. Mas o projeto tem por método marcar o que é escolha e o que é herança, e essas quatro estavam passando como escolha sem ter sido decididas.

---

## [0.19] — 2026-08-06

### Corrigido — a trava de vida da v0.18 conferia a coisa errada

A v0.18 checava que a **média dos dados de vida** desse 8, igual ao número do manual. Isso parece certo e não é.

**O 8 do manual é a vida total por nível, sem atributo nenhum** — ele foi escrito antes de existir Constituição na conta. Somar Constituição por cima não empata com ele: infla.

| | média dos dados | mais Constituição típica (3) | o manual supõe | desvio |
|---|---|---|---|---|
| v0.18 — 10/9/8/7/6 | 8,0 | 11,0 | 8 | **+38%** |
| v0.19 — 7/5/5/4/4 | 5,0 | **8,0** | 8 | **+0%** |

Na prática, a v0.18 dava ao grupo 38% de vida a mais do que a tabela de encontro supõe, e o combate durava **4,7 rodadas onde o manual promete 3,5**.

**A trava certa é: média dos dados + 3 de Constituição ≈ 8.** O validador foi reescrito para conferir isso, e agora também mede as rodadas para cair sob foco contra a tabela de chefe do manual, em vez de confiar numa média abstrata.

É a terceira vez seguida que o mesmo tipo de erro aparece — v0.16, contagem não era valor; v0.17, a referência óbvia não era a certa; agora, o número certo comparado contra a base errada. **A pergunta que faltou nas três: "esse número já inclui o que eu estou somando nele?"**

### Alterado — a vida por Caminho, com dado

| Caminho | dado | vida no nível 1 | por nível | PE por nível | soma |
|---|---|---|---|---|---|
| **Bastião** | d12 | 12 | 7 | 4 | 11 |
| **Vanguarda** | d8 | 8 | 5 | 5 | 10 |
| **Guia** | d8 | 8 | 5 | 5 | 10 |
| **Evocador** | d6 | 6 | 4 | 6 | 10 |
| **Emanador** | d6 | 6 | 4 | 6 | 10 |

> **No nível 1 você recebe a vida inicial do Caminho + Constituição.**
> **Em cada nível depois, a vida por nível do Caminho + Constituição de novo.**

**A vida inicial é o máximo do dado e a vida por nível é a metade dele arredondando para cima**, então quem quiser pode rolar o dado em vez de pegar o fixo. Uma versão anterior desta proposta tinha 6 por nível para os Caminhos de d8, o que não fecha — d8 dá 5. O validador agora falha se o fixo e o dado deixarem de ser equivalentes.

**A soma vida+PE ficou 11 no Bastião e 10 nos outros quatro.** É o número que faz a troca "couro contra combustível" ser sabor em vez de degrau de poder, e o validador falha se a diferença passar de 2.

### Alterado — PE em três degraus

**6 no Emanador e no Evocador. 5 na Vanguarda e no Guia. 4 no Bastião.**

Os dois do meio vivem entre bater e conjurar: o Guia estende efeito alheio e recupera, a Vanguarda alterna golpe canalizado com golpe simples. O **6 dos dois conjuradores puros não é escolha nossa** — o Fundamento tem uma tabela de "quantas vezes você lança o seu melhor feitiço" calculada em cima dele. O 4 e o 5 são números nossos.

### Resultado

Rodadas para cair sob foco, com Constituição 3, contra a tabela de chefe do manual:

| | nv 2 | nv 10 | nv 20 | nv 30 |
|---|---|---|---|---|
| Bastião | 4,2 | 4,0 | 4,2 | 4,2 |
| Vanguarda · Guia | 3,2 | 3,2 | 3,3 | 3,4 |
| Evocador · Emanador | 2,7 | 2,8 | 2,9 | 2,9 |
| **média do grupo** | 3,2 | 3,2 | 3,3 | 3,4 |

Plana do nível 2 ao 30 nos cinco, e a média em cima das 3,5 do manual. O mestre nunca precisa saber o nível para estimar quanto tempo alguém aguenta.

### Registrado — Constituição virou a maior alavanca de sobrevivência

| no nível 10, do menor valor ao maior | compra |
|---|---|
| Caminho, de 4 para 7 | +46% |
| Destreza, de 1 para 6 | +56% |
| **Constituição, de 0 para 6** | **+113%** |

Na v0.18 ela comprava +59%, na mesma faixa da Destreza. Dobrou por duas razões somadas: a vida por nível ficou menor, então cada ponto de Constituição pesa proporcionalmente mais; e ela passa a entrar **também no nível 1**, multiplicando por *nível* em vez de *(nível − 1)*.

Não quebra nada e as três continuam sendo escolhas, mas é o primeiro número do sistema em que um atributo está claramente na frente. **Pergunta de playtest: apareceu alguém com Constituição 0 ou 1?** Se não apareceu, ela virou obrigatória, e o conserto é uma linha — Constituição volta a entrar só do segundo nível em diante.

Pela mesma causa, o espalhamento subiu para **3,2×**: o Evocador de Constituição 0 tem 122 de vida no nível 30 e cai em 1,7 rodadas, contra 395 e 5,5 rodadas do Bastião de Constituição 6. O teto do validador subiu de 3,0× para 3,5× com o motivo escrito.

### Efeito colateral registrado — a alma virou a reserva maior

Com a vida do corpo menor, a Integridade (`20 + 8 × (nível − 1)`, inalterada) passou a ser **maior que a vida em quatro dos cinco Caminhos**. Quem não é Bastião cai pelo corpo antes de a alma acabar, então o **estágio 4 de dano de alma quase nunca dispara**.

O Bastião é o único que inverte: no nível 30 ele fica de pé com 53 de vida no medidor e a alma acabada. É exatamente o que o Mahito faz com quem é duro demais para morrer de porrada — mas hoje ele é o único que chega lá.

Isso muda quando a **Essência** entrar na Integridade, o que já está decidido e sai junto com a peça de dano de alma.

---

## [0.18] — 2026-08-06

### Decidido — cada Caminho tem a sua vida por nível

> **Pontos de vida = 20 + (a vida do seu Caminho + Constituição) × (nível − 1).**

| | Bastião | Vanguarda | Guia | Evocador | Emanador |
|---|---|---|---|---|---|
| vida por nível | 10 | 9 | 8 | 7 | 6 |
| PE por nível | 4 | 4 | 6 | 6 | 6 |

**O argumento não é "porque o d20 faz assim" — é que sem isso o Bastião não tem como ser tanque.**

A trava do Caminho, escrita na peça 5, proíbe ele de dar dados de dano, Classe de feitiço, Melhoria de graça e cura. Com a v0.17, o Bastião — *"o corpo como resposta: aguentar, encarar, prender"* — ainda não tinha **um único número** que o fizesse aguentar mais que um Emanador. A coisa que o tornaria duro seria a Constituição dele, que qualquer conjurador também pode pegar.

Vida é a única alavanca que a trava deixa aberta, e ela não está na lista do proibido: não é dano, não é Classe, não é Melhoria, não é cura. É o que transforma "aguentar" em mecânica em vez de sabor.

E ela **corre no sentido contrário do PE**, que já era assimétrico desde a v0.14: quem tem mais couro tem menos combustível. As duas assimetrias se pagam em vez de empilhar.

### A trava que a peça precisa: média 8

**A média dos cinco Caminhos tem que dar exatamente 8**, e isso não é estética. O manual calibra vida de chefe, dano de chefe e dano de capanga em cima de 8 por nível. Enquanto a média for 8, a tabela de encontro dele continua valendo para um grupo típico — e ela é a peça que faz cinco mestres prepararem igual. 10 + 9 + 8 + 7 + 6 = 40, sobre cinco, dá 8.

O `conferir-atributos.py` agora **falha** se a média sair de 8, se o espalhamento passar de 3×, ou se uma das três alavancas de sobrevivência dominar as outras duas.

### Os números que fecham

| no nível 10, do menor valor ao maior | compra de sobrevivência | custo |
|---|---|---|
| Caminho, de 6 para 10 | +36% | escolha única, na criação, sem volta |
| Constituição, de 0 para 6 | +59% | pontos de atributo |
| Destreza, de 1 para 6 | +56% | pontos de atributo, e devolve muito mais junto |

Espalhamento no nível 30: de **194** (Emanador de Constituição 0) a **484** (Bastião de Constituição 6), **2,5×**. Um pouco mais largo que o d20 clássico, onde a distância entre o conjurador frágil e o brutamontes fica perto de 2×.

Nenhuma das três domina, e a do Caminho é a única que **não tira ponto de lugar nenhum**.

### Integridade — o rumo agora está decidido, não só registrado

A Integridade continua plana em `20 + 8 × (nível − 1)`, sem Caminho e sem Constituição, e continua sendo exatamente a fórmula do manual — muda uma frase, não muda uma tabela.

**Mas ela não fica assim.** Decidido que a Integridade vai **escalar com Essência**, virando uma segunda vida de verdade em vez de um número plano. Entra junto com a peça de dano de alma, com o contexto que ela vai trazer.

Quando entrar, os dois eixos se cruzam em vez de empilhar: o Emanador de Essência alta fica com **alma grossa e corpo fino**, o exato oposto do Bastião. Hoje já dá para ver o embrião disso — no nível 30, a alma do Bastião acaba com 232 de vida ainda no medidor, e ele fica de pé sem ser mais ele. É a imagem que a obra usa o tempo todo.

### Corrigido de método

A v0.17 tinha escolhido `20 + (8 + Constituição) × (nível − 1)`, com o 8 igual para todo mundo, e **não perguntou se o 8 devia ser igual para todo mundo**. O número veio do manual, e o manual não conhece Caminhos — ele foi escrito antes de eles existirem.

É a mesma lição da v0.17 aplicada um nível acima: lá, a referência óbvia (a tabela do manual) não era a referência certa para o tamanho da Constituição. Aqui, ela também não era a referência certa para **quantas fórmulas de vida deveriam existir**.

---

## [0.17] — 2026-08-06

Revisão geral antes de começar a criação de personagem. Os três validadores passam, todas as fórmulas aparecem iguais em todo lugar, todas as referências cruzadas resolvem e nenhum termo carrega dois significados. Achou um buraco grande e três textos parados.

### Achado — Constituição não fazia nada

Três documentos diziam que Constituição governava pontos de vida. A peça 4 e a peça 7 usavam exatamente isso para justificar por que ela tem **zero perícias**: *"ela já governa vida e o TR Vigor, que é trabalho suficiente"*.

A única fórmula de vida que existia no projeto inteiro estava no manual do Fundamento, e é `20 + 8 × (nível − 1)` — **sem atributo nenhum**. Constituição entregava só o Teste de Resistência Vigor, e o argumento que tirou as perícias dela era um trabalho que ela não tinha.

É o mesmo padrão da v0.11, a tensão que era lacuna de texto disfarçada. Só que desta vez a lacuna estava na linha mais visível da ficha, e teria aparecido na primeira pessoa que fosse criar um personagem.

### Decidido — Constituição entra cheia

> **Pontos de vida = 20 + (8 + Constituição) × (nível − 1).**

**E o número que decide isso não é o do manual.** Comparar Constituição com uma tabela que não tem atributo nenhum faz qualquer valor parecer demais — foi assim que a primeira recomendação saiu "metade", e estava errada.

A comparação certa é com o outro atributo que **já** compra sobrevivência: Destreza, pela Defesa. Indo do valor 1 ao 6:

| nível | Destreza (faz errar mais) | Constituição cheia | razão |
|---|---|---|---|
| 2 | +63% | +17% | 0,72 |
| 10 | +56% | +45% | 0,93 |
| 22 | +50% | +50% | **1,00** |
| 30 | +45% | +52% | 1,04 |

As duas ficam na mesma faixa a campanha inteira, e cruzam por volta do nível 22. **Destreza protege mais cedo e Constituição protege mais tarde** — a Defesa não cresce com o nível, a vida cresce. É por isso que uma não domina a outra.

Pela metade, Constituição ficaria em +29% no nível 10: o atributo que faz uma coisa só, fazendo pior que o atributo que faz cinco. Destreza ainda compra ataque à distância, iniciativa e quatro perícias por cima.

### Decidido — a Integridade não leva Constituição

> **Integridade = 20 + 8 × (nível − 1).**

O manual diz *"Integridade = vida máxima"*. Com Constituição na vida, essa frase daria de graça a um corpo duro uma alma dura — e dano de alma é justamente o que ignora o corpo. O que o Mahito faz não passa pelo músculo.

**A escolha custa zero:** a fórmula acima é exatamente a que o manual já tem. Muda uma frase — *"Integridade = vida máxima"* vira *"a vida que todo mundo tem, antes da Constituição"* — e não muda nenhuma tabela. Os quatro estágios de dano de alma continuam valendo como estão.

Se a alma parecer frágil no playtest, o conserto natural é ela somar **Essência**, que já é o atributo do TR Espírito e o eixo da alma no sistema. Registrado, não aplicado.

### Alterado

- `conferir-atributos.py` ganhou dois invariantes novos: **Constituição compra sobrevivência na mesma faixa que a Destreza** (falha fora de 0,6× a 1,4×) e **Integridade não leva Constituição** (falha se sair da fórmula do manual, porque aí a tabela de estágios teria que ser refeita).

### Corrigido — três textos que tinham ficado para trás

- **A peça 1 ainda dizia "3,2 rodadas é o alvo, com 65% de acerto".** Os dois números estavam errados e não batiam nem entre si: o CHANGELOG da v0.8 registrava 60% e o validador entrega 50%. Virou previsão de **3,4 a 4,0 rodadas**, com a tabela das três taxas do lado, marcada como número a medir e não alvo fechado.
- **A peça 3 citava a regra de ouro nº 6 como "Grau 0"** enquanto o resto do material diz "Classe 0". Citação traduzida, com nota de que o `.docx` ainda não foi regenerado.
- A nota de substituição da peça 4 dizia "vinte perícias" e não avisava que Sentir Energia mudou de atributo na v0.16.

### O que a criação de personagem ainda não tem

Levantado de propósito antes de começar. Só um item travava, e ele foi resolvido acima.

| falta | trava? | por quê |
|---|---|---|
| Lista de Origens | não | a forma existe — patente, traço, duas perícias, um TR. Falta o catálogo, e o mestre aprova na leitura |
| Tabela de proteção | não | `Defesa = 10 + Destreza + proteção`, e dá para criar com proteção 0 |
| Tabela de armas | não | o golpe canalizado nem usa arma |
| Quantas Trilhas e quando | não | a ficha começa no nível 2 e Trilha vem depois |
| Regra de Pactos | não | camada 5, opcional na criação |

### Lição de método

**Quando um número não existe, o erro não é escolher mal — é escolher contra a referência errada.** A primeira recomendação de Constituição saiu conservadora porque comparou com a tabela do manual. A pergunta certa nunca foi "quanto de vida é demais", e sim "quanto de sobrevivência os outros atributos já compram".

Vale como par da lição da v0.16: lá, contagem não era valor; aqui, a referência óbvia não era a referência certa.

---

## [0.16] — 2026-08-06

### Alterado

- `03-mecanica/07-pericias-e-oficios.md` reescrita: **vinte e três perícias**, e o quadro mudou de eixo.
- `03-mecanica/01-atributos-acerto-defesa.md` — a tabela de atributos e o parágrafo da fusão de Essência, que diziam o contrário do que agora vale.
- `03-mecanica/conferir-pericias.py` — checagem nova de peso de mesa, e as colisões aceitas passaram a ser declaradas com motivo dentro do próprio validador.

### Decidido — Inteligência sabe, Essência percebe

**Sentir Energia e Percepção saíram de Inteligência e foram para Essência.** É a maior mudança da versão e ela reverte uma decisão da v0.8.

A v0.8 mandou a percepção para Inteligência com uma intenção boa: tirar de Inteligência o papel de atributo-depósito, dando a ela a coisa que mais importa em Jujutsu Kaisen. Com o quadro de perícias escrito, dá para medir o que aquilo produziu — e produziu o oposto:

| | perícias em Int | peso de mesa (Int / Ess) |
|---|---|---|
| v0.15 | 10 de 20 | **56% / 21%** |
| v0.16 | 11 de 23 | **39% / 39%** |

**Inteligência ficou com mais perícias e vale menos**, porque as duas que saíram são as duas mais roladas da mesa. Foi o que a conta mostrou e o que a contagem crua escondia: pedir "quantas perícias cada atributo tem" responde a pergunta errada. A pergunta certa é quanto do que se rola numa campanha depende dele.

E o argumento de ficção fecha com o número: **Essência não sabe nada, ela sente.** Sentir energia amaldiçoada é a sua energia reagindo à de outro — ressonância, não análise. Na obra quem sente melhor não é quem estudou mais; é o Gojo com os Seis Olhos, é o instinto do Todo.

**Percepção foi junto e essa parte não era opcional.** Com Sentir Energia em Essência e Percepção em Inteligência, a mesa teria dois tipos de perceber em dois atributos, e erraria qual rolar em toda cena de aproximação.

### Decidido — o resto do quadro

- **Táticas deixou de existir.** O trabalho dela já estava coberto duas vezes: **Ocultismo** reconhece o que você vê porque conhece o catálogo, **Sentir Energia** lê como a energia se move sem precisar saber o nome. O Nanami faz a primeira, o Todo faz a segunda.
- **Três perícias partidas em duas:** Ocultismo perdeu o lado sagrado para **Religião**, Sobrevivência perdeu o conhecimento para **Natureza**. Religião é o lado de onde o jujutsu veio antes de virar instituição.
- **Entraram Lidar com Animais e Provocar.** Provocar é o inverso de Intimidação: uma faz recuar, a outra faz avançar.
- **Hierarquia foi para Inteligência.** Saber quem deve o quê a quem é conhecimento, não leitura de sala.
- **Ofícios:** Primeiros Socorros saiu e entrou **Herbalismo**; Artesania virou **Entalhador**; Protocolo virou **Burocracia**.

### Decidido — o Caminho para de escolher o personagem

> **Duas perícias fixas e mais quatro à escolha livre, de qualquer lugar do quadro.**
> **Um ofício fixo e outro livre. A Origem continua dando duas perícias.**

Oito de vinte e três — **35%**, o mesmo alvo de sempre, alcançado por outro caminho. Antes eram cinco escolhidas dentro de uma lista de oito por Caminho.

As duas fixas continuam sendo a assinatura: dois Bastiões dividem Atletismo e Intimidação. As quatro livres são o que impede duas fichas do mesmo Caminho de serem a mesma pessoa.

**Sentir Energia não é fixa de nenhum Caminho, e isso é escolha.** Sendo a mais rolada da mesa, fixá-la em um Caminho daria àquele Caminho uma escolha livre a mais disfarçada. Livre para todos, ela vira decisão de ficha — e o feiticeiro ruim de sentir energia passa a caber, que é o Itadori do começo.

**O Evocador entalha.** O ofício fixo dele é Entalhador, e é o que dá razão de existir para o shikigami de madeira e para a boneca que anda.

### Colisão de "Provocar" — registrada e aceita

O manual usa *"sem provocar ataque de oportunidade"* em três lugares, e a peça 3 chega a perguntar *"provocar o quê?"*. Pela regra de checagem em duas direções, isso é colisão.

**Aceita mesmo assim:** a expressão é comum demais em qualquer mesa de d20 para confundir, e "provocar ataque de oportunidade" e "rolar Provocar" nunca aparecem no mesmo tipo de frase. O que muda é que a decisão fica escrita **dentro do validador**, com o motivo, junto de outras duas fracas — *Natureza* encosta na Passiva **Segunda Natureza**, e *História* aparece uma vez em prosa solta. O validador agora falha se aparecer uma colisão que **não** esteja nessa lista, o que separa "aceito" de "não percebido".

### Achado de método

**Contagem não é valor, e o validador estava medindo a coisa errada.** A versão anterior conferia quantas perícias cada atributo tinha e teria aprovado a v0.16 com Inteligência a 48% — número pior que os 50% da v0.15. Ponderando pela frequência com que cada perícia é rolada, a mesma mudança aparece como 56% caindo para 39%.

Vale para o resto do projeto: **antes de medir uma distribuição, perguntar se cada item pesa igual.** Quase nunca pesa.

### Em aberto

- Nome do sistema.
- Nomes definitivos das Trilhas, com as três colisões conhecidas (Régua, Alcance, Fôlego).
- As listas de perícia de cada Origem.
- **Intuição está em cima do muro.** "Ler a pessoa" tem cara de perceber, e ela ficou em Inteligência como dedução. Se em mesa as pessoas rolarem Percepção no lugar dela, muda de casa.
- **Provocar e Intimidação vão brigar na mesa?** A distinção é clara escrita e vaga em jogo.
- Quantas Trilhas um personagem acumula, e em que níveis.
- Como a Trilha Torrente cobra o segundo feitiço da rodada.
- Se a Trilha Coro deixa dono e invocação agirem no mesmo turno.
- Se a curva de dano deve cruzar a coluna Rotina.

---

## [0.15] — 2026-08-06

### Adicionado

- `03-mecanica/07-pericias-e-oficios.md` — o quadro completo. **Vinte perícias e dez ofícios.** Substitui as seções 3 e 4 da peça 4.
- `03-mecanica/conferir-pericias.py` — validador do quadro: contagem por atributo, nome repetido, tamanho das listas de Caminho, fração treinada, perícia órfã e colisão de termo nas duas direções. Passa.

### Decidido

- **Duas listas, não uma.** Perícia pertence a um atributo fixo; **ofício não pertence a atributo nenhum** — o atributo muda conforme o que você faz com ele. Forjar é Força, falsificar é Destreza, saber qual selo o papel pede é Inteligência, e é o mesmo ofício. É a proficiência de ferramenta do d20, e é o que permitiu recheá-la sem inflar a lista de perícias.
- **Perícia sem treino você tenta; ofício sem treino, não.** Qualquer um escala e falha. Ninguém forja por tentativa.
- **Sabedoria dissolvida dentro de Inteligência, como consequência da v0.8.** Ocultismo come arcano e religioso; Sobrevivência come natureza e rastrear; Percepção, Intuição e Medicina vêm inteiras de Sabedoria. As cinco novas de JJK são Sentir Energia, Tecnologia, Táticas, Hierarquia e Pontaria.
- **O Caminho lista oito perícias e três ofícios; você treina cinco e dois.** A Origem dá mais duas perícias. **Sete de vinte — 35%**, exatamente o alvo que a v0.14 calculou. Com a lista de catorze eram 64%, e "ser treinado" não significava nada.
- **Sentir Energia está nas cinco listas e não é de graça** — ocupa um dos cinco espaços. Um feiticeiro pode ser ruim de sentir energia, e o Itadori do começo é isso.
- **PE do Guia: 6.** A regra da v0.14 dizia "6 nos Caminhos de técnica, 4 nos físicos" e o Guia não era nem um nem outro — ficava sem número. A regra passa a nomear os cinco Caminhos em vez de dividir em duas famílias que não cobriam todos.

### Aceito com pergunta de playtest — Inteligência com metade do quadro

**Dez das vinte perícias moram em Inteligência.** Isso a torna o atributo mais valioso fora de combate por larga margem, e a peça 1 já tinha marcado o risco quando Sabedoria foi fundida nela.

Fica assim de propósito: em Jujutsu Kaisen, perceber e saber *é* metade do jogo, e o contrapeso está dentro do combate — Destreza carrega Defesa e iniciativa, Constituição carrega os pontos de vida, e ninguém zera esses dois. A pergunta de playtest é específica: **apareceu alguma ficha com Inteligência 0 ou 1?** Se em três meses nenhuma apareceu, o conserto é um teto de três perícias do mesmo atributo por Caminho.

**Força continua com uma perícia só, e a lista não conserta isso.** Nenhuma cabia sem enchimento: correr, escalar e carregar já são Atletismo, e aguentar dor e fome é leitura de Constituição em qualquer mesa. O segundo trabalho de Força tem que vir de fora do quadro.

### Corrigido — quinze achados de uma revisão cética do material inteiro

Três contradições diretas, em que duas peças diziam o oposto:

- **O golpe canalizado somava arma e Força na peça 5 e não somava na peça 6.** É a regra central do combatente físico escrita ao contrário em dois arquivos. A peça 6 está certa — somando, o físico fica 131% acima da Rotina no nível 2. Peça 5 corrigida, com a conta apontada.
- **Quantas perícias o Caminho dá:** três na peça 4, sete na peça 6. Resolvido pelo quadro novo.
- **A peça 5 ainda listava os Caminhos de rascunho**, incluindo *Leitura*, eliminada por colisão na v0.14. A peça 6 dizia substituir "a seção 4 da peça anterior", mas a peça 5 não tinha aviso nenhum — quem lesse na ordem saía com os nomes errados.

Números que não fechavam:

- **Peça 1:** *"trocar o 5 fixo por um atributo"* — o valor fixo é **2**. Resquício da v0.8, duas linhas abaixo do lugar onde o próprio documento diz 2.
- **Peça 1:** a fórmula de perícia estava sem a condicional de treino.
- **CHANGELOG v0.10:** *"bate no teto no nível 8 ou 12"* — os marcos são 6/10/14, e não existe nível 8 nem 12. Resquício de quando os marcos eram 4/8/12.
- **`conferir-atributos.py` testava CD 12, 16 e 20**, que não existem na escada oficial de 10/14/18/22/26. Trocado, e a tabela da peça 4 saiu confirmada linha por linha.

O `arquitetura.md`, que é o arquivo apontado para retomar o projeto, tinha ficado quatro versões para trás:

- A tabela de refino usava os marcos **4/8/12/16/20/24/28**, substituídos por 6/10/14/18/22/26/30 na v0.10 — a curva inteira saía errada, junto com "o especialista bate no teto no nível 20" e "desperdiça três escolhas".
- A escada da patente dizia **sete degraus**; a v0.7 decidiu **oito**, com o semi-especial.
- A tabela dos três eixos chamava o tamanho do feitiço de **Escala**, três linhas abaixo do texto que decide **Classe**. Nem *Escala* nem *Potência* sobreviveram.
- O problema 1 da seção 4.3 estava listado como aberto. A v0.10 resolveu, e **não pelo conserto que estava proposto lá** — quem resolveu foi o teto fixo de 6 no atributo, que inverte sozinho o valor relativo dos dois lados no meio da campanha. Os degraus de peso continuam valendo, mas como controle de acesso, não como conserto de balanço.

### Registrado — três coisas que a revisão achou e que ficam para depois

**A taxa de acerto aparece com três valores diferentes no material.** A peça 1 diz 65%, o CHANGELOG da v0.8 diz 60%, e o validador entrega **50%** — contra um alvo que também investiu em defesa, que é o caso difícil. O alvo de "3,2 rodadas" foi calculado em cima de 60%; a 50% a faixa real é **3,4 a 4,0 rodadas**. Fica como previsão a medir em vez de número a consertar: quem decide se o combate está arrastado é a mesa, não a planilha.

**A curva de dano cruza a coluna Rotina, e ninguém tinha comentado.** No nível 2 o conjurador está +38% e o físico +69% acima dela; no nível 30 estão 21% e 16% abaixo. A peça 6 reprovou +135% no nível 2 e aprovou +69% na linha seguinte sem tratar a diferença. Não é necessariamente errado — vida é baixa no nível 2 —, mas é decisão não tomada.

**Três nomes de Trilha colidem com o manual**, pela checagem nas duas direções: **Régua** é um dos três Fundamentos de exemplo do manual, **Alcance** é Família *e* Melhoria com catorze ocorrências, e **Fôlego** aparece no feitiço pronto Roubo de Fôlego. E **Ofício** ia colidir com a perícia de ofício — por isso a lista usa *Artesania*. Como os nomes de Trilha já eram todos provisórios, entra na pendência que já existia.

### Em aberto

- Nome do sistema.
- Nomes definitivos das Trilhas, agora com três colisões conhecidas a resolver.
- As listas de perícia de cada Origem. Hoje a Origem dá duas livres, com aprovação do mestre.
- Quantas Trilhas um personagem acumula, e em que níveis.
- Como a Trilha Torrente cobra o segundo feitiço da rodada, contra a regra de ouro nº 6.
- Se a Trilha Coro deixa dono e invocação agirem no mesmo turno.
- Se a curva de dano deve cruzar a Rotina ou acompanhar ela.

---

## [0.14] — 2026-08-06

### Adicionado

- `03-mecanica/06-caminhos-e-trilhas.md` — o quadro de cinco Caminhos com três Trilhas cada. Revisa e substitui a seção 4 da peça anterior.

### Decidido

- **Cinco Caminhos, com nomes conferidos contra o manual:** Bastião (corpo), Vanguarda (arma), Guia (o outro), Emanador (técnica), Evocador (invocações). Os rótulos de rascunho saíram — *Leitura* em particular já aparecia três vezes no Fundamento.
- **Sem multiclasse.** Um Caminho por personagem; as escolhas de nível compram Trilhas dentro dele. Acumular Trilhas do próprio Caminho é o que permite pegar Energia Reversa antes do refino liberar.
- **O Guia não compete em buff, debuff nem cura** — esses moram na técnica e na Forma de feitiço. Ele **alcança**: faz o efeito de outra pessoa durar mais, pegar mais gente ou chegar mais longe. Era o Caminho que não fechava, e é essa a saída.
- **Treinamento em equipamento** em três categorias: armas, proteção e escudo. Escudo é categoria própria porque ocupa uma mão — e mão ocupada **cancela a Restrição Gesto**, que exige as duas mãos livres. Vira decisão de ficha em vez de bug.

### Ataque extra — aprovado, com correção

A coluna Rotina do Fundamento **já é "feitiço + Classe 0"**: o conjurador sempre teve dois golpes por rodada. Então ataque extra no físico não é privilégio, é o espelho.

Mas o golpe canalizado **não pode somar arma nem Força** — ele *é* o feitiço. Com os dois somados e ataque extra por cima, o físico fica 135% acima da Rotina no nível 2 e 32% no nível 10. A regra em três linhas, espelhando a regra de ouro nº 6: golpe canalizado são os dados da Classe e nada mais; golpe simples é arma + Força; um canalizado por turno, e ataque extra é sempre golpe simples.

### Invocação — reprovada como estava, e o conserto

**Uma invocação que age sozinha dobra o dano por rodada; uma horda de três quadruplica** — 504 por rodada no nível 30 contra uma Rotina de 126. Nenhum preço em PE conserta, porque o problema não é recurso, é economia de ação.

**Conserto: você e todas as suas invocações somados entregam uma Rotina.** Com uma, cada um entrega metade; com três, um quarto. Isso entrega exatamente a fantasia pedida sem regra extra — Sombra tem um corpo forte, Enxame tem cinco fracos, e o invocador troca dano pessoal por presença de tabuleiro. É também a leitura correta da obra: as maldições do Geto individualmente são frágeis, o que assusta é o número.

### Energia — fixa pelo Caminho, sem atributo *(revisado)*

**PE por nível: 6 nos Caminhos de técnica, 4 nos físicos. Espírito não entra.**

Com teto de atributo em 6, não existe faixa útil: qualquer divisor grande o bastante para não criar imposto entrega **um ponto** na ficha inteira. Ou o atributo importa de verdade e vira obrigatório — o que a peça 1 evitou de propósito —, ou não importa e só ocupa espaço na cabeça de quem lê. A análise abaixo continua registrada porque o raciocínio vale para qualquer outra tentação de amarrar atributo a recurso.

### Energia — a análise que levou a isso

Duas objeções à proposta de `4 + Espírito/2` para conjurador:

**Cortar a base de 6 para 4 invalida a tabela de PE do manual**, que tem uma coluna inteira de "quantas vezes você lança o seu melhor feitiço" calculada em cima de 6 por nível.

**Espírito/2 dá +50% de PE entre Espírito 0 e 6** — o dobro de usos do melhor feitiço em vários níveis. É o atributo obrigatório pela porta dos fundos que a peça 1 evitou ao tirar atributo da conta do feitiço.

Proposta: conjurador `6 + Espírito/4`, físico `4 + Espírito/4`. Dá +17%, que é sabor e não imposto. O físico com dois terços do combustível é justo porque o golpe simples dele rende ~10 contra os ~4,5 do Classe 0 do conjurador — menos combustível, melhor motor de reserva.

### Múltiplos atributos por Caminho — aprovado, já estava previsto

O mecanismo já existia: o Caminho pode **trocar o valor fixo de 2 do ataque de conjuração por um atributo**. Emanador conjura com Inteligência ou Essência; Bastião canaliza com Força; Vanguarda com Destreza. A troca é neutra em balanço porque os dois crescem +3 na campanha, e não vira imposto porque é opcional.

### Perícias — a lista precisa crescer

Com catorze perícias e 7 do Caminho mais 2 da Origem, o personagem fica treinado em **64% de tudo que existe** e "ser treinado" para de significar algo. Proposta: expandir para 24 a 28, o que leva a fração a 35% e devolve espaço para o resto do grupo brilhar.

### Em aberto

- Nome do sistema.
- Nomes definitivos das Trilhas.
- O quadro completo de perícias (24 a 28) com o atributo de cada.
- Quantas Trilhas um personagem acumula, e em que níveis.
- Como a Trilha Torrente cobra o segundo feitiço da rodada, contra a regra de ouro nº 6.
- Se a Trilha Coro deixa dono e invocação agirem no mesmo turno.

---

## [0.13] — 2026-08-06

### Adicionado

- `03-mecanica/05-caminho-e-combate-sem-feitico.md` — o trabalho de Força, o Caminho e como alguém luta com o corpo num sistema onde o poder mora na técnica.

### Decidido

- **Força governa** ataque corpo a corpo, agarrar, quebrar, Atletismo, capacidade de carga e requisito de arma e proteção. Armas de dado maior e uniformes pesados exigem Força mínima.
- **Golpe canalizado = feitiço de Forma Toque, sem Melhoria e sem Restrição.** Mesma Classe, mesmo orçamento, mesmo custo em PE, e o golpe ainda soma arma e Força por cima.
- **A trava do Caminho:** ele não dá poder novo, muda o que o poder alcança. Mexe em posicionamento, alvo, duração e recuperação — nunca em dados de dano, Classe de feitiço, Melhoria de graça ou cura.
- **Uma Trilha de Caminho pode abrir exceção estreita e paga** na economia de ação — conjurar na Reação uma vez por cena, ou só com Classe baixa. Como recurso de um caminho específico, não direito universal.
- **Quatro Caminhos como esqueleto:** Linha de Frente (Força), Ponta de Lança (Destreza), Retaguarda (Essência), Leitura (Inteligência). O quadro definitivo é taste call.

### Achado — uma arma sozinha não cabe no jogo

O manual já avisava que o combatente físico precisa ficar na coluna Rotina. Rodando a conta, **uma arma entrega de 7% a 65% do que a coluna pede, e a diferença cresce com o nível** — 1,5× de lacuna no nível 2, 11× no nível 30. Não é escolha de dado: trocar d6 por d12 muda três pontos numa lacuna de cem. Falta uma ordem de grandeza inteira, e nenhum requisito de Força ou tabela de arma conserta isso.

O conserto é Canalizar Energia, e a forma dele caiu da conta em vez de ser inventada: os dados de energia que faltam para o golpe atingir a Rotina batem com os pontos que a Classe do nível concede, faixa por faixa. **O golpe canalizado é o feitiço vazio** — o que sobra de um feitiço quando se tira toda a customização e fica só o orçamento bruto. Por isso é aptidão básica de qualquer feiticeiro, e por isso ter técnica continua sendo melhor: a técnica compra Melhorias, o golpe não.

Isso explica de graça três coisas que estavam soltas: por que **Maki** precisa de ferramenta amaldiçoada (sem energia ela não canaliza, e a arma canaliza por ela); por que **socar é a saída quando o PE acaba** (é o equivalente físico do feitiço de Classe 0); e por que **o combatente físico não tem Liberação Máxima** (ele já vive no teto de dano num alvo o tempo todo).

### Registrado sobre requisito de arma

Requisito de Força resolve **acesso, não balanço**. Um dado maior rende cerca de +2 por golpe, o que empata o valor defensivo de +1 de Destreza por volta do nível 5 e fica para trás depois — sem contar iniciativa e três perícias. É bom que exista e dá a Força um trabalho real, mas não é ele que impede Destreza de dominar. Quem faz isso é o Caminho de Linha de Frente.

### Em aberto

- Nome do sistema.
- O quadro definitivo de Caminhos e quantas Trilhas cada um tem.
- A tabela de armas: dados, requisitos e se arma leve compensa de outra forma.
- Quanto custa uma ferramenta amaldiçoada que canaliza sozinha. Precisa ser cara o bastante para não virar padrão.
- Se o golpe canalizado tem teto próprio ou herda o do Fundamento.

---

## [0.12] — 2026-08-06

### Adicionado

- `03-mecanica/04-pericias-e-testes.md` — perícias, escada de dificuldade, de onde vem o treino, fail-forward e a regra do ataque de oportunidade.

### Decidido

- **Perícia = d20 + atributo + maestria se treinado; sem treino, só atributo.** Maestria é o que marca o treino.
- **Por que treino funciona diferente em perícia e em Teste de Resistência:** a oposição é diferente. A CD de perícia é fixa pela dificuldade e não cresce, então o treino pode crescer. A CD de TR cresce com o conjurador, então o treino tem que ser flat ou o não treinado despenca. É a mesma regra da peça 1 aplicada aos dois casos.
- **Escada de dificuldade em cinco degraus nomeados:** 10 rotina, 14 fácil, 18 média, 22 difícil, 26 quase impossível. CD 10 vira automático no fim da campanha de propósito — feiticeiro experiente não rola para arrombar porta comum.
- **Catorze perícias**, nenhuma amarrada a Constituição. **Sentir Energia** é a mais rolada da mesa e mora em Inteligência.
- **Inteligência não concede perícias extras**, ao contrário do costume d20. Ela já carrega percepção, conhecimento e um TR; dar perícias por Inteligência a empurraria de carregada para obrigatória.
- **Treino:** Origem dá duas perícias e um TR; Caminho dá três perícias e outro TR. Cinco perícias treinadas de catorze, e dois TRs de quatro.
- **Falha nunca é "não acontece nada".** Ela entrega custo, complicação ou informação indesejada. Não é só ritmo: é a norma que faz cinco mestres diferentes falharem do mesmo jeito. Corolário: se o mestre não consegue nomear o custo antes de pedir a rolagem, não pede.
- **Ajudar dá vantagem, um ajudante por teste. Teste de grupo passa com metade do grupo.**

### Resolvido — feitiço como ataque de oportunidade

**Ataque de oportunidade é ataque físico**, rolado como ataque comum e pago com a Reação. Conjurar na Reação continua exigindo a Melhoria Reação.

A razão é aritmética: a Melhoria Reação custa Pesada, o que é **metade do orçamento do feitiço** em toda Classe — 67% na Classe 1, 52% na Classe 7. Se qualquer feitiço pudesse virar ataque de oportunidade de graça, a Melhoria viraria peça morta na hora. Uma trilha de Caminho pode abrir exceção limitada, e aí é recurso pago por um caminho específico em vez de bônus universal.

### Confirmado

- **Ação bônus fica.** Existem técnicas que viram ação bônus e a peça Rápido depende disso. Medir uso real no playtest.
- **Uma reação por rodada.** Revisitar só se a competição entre ataque de oportunidade, Melhoria Reação e as Passivas de reação deixar as Passivas mortas.

### Em aberto

- Nome do sistema.
- Se Força precisa de um segundo trabalho: uma perícia é pouco.
- Se treino em perícia tem graus ou é binário. Binário por ora.
- Quais trilhas de Caminho abrem exceção de conjuração na reação, e sob que condição.

---

## [0.11] — 2026-08-06

### Adicionado

- `03-mecanica/03-economia-de-acao-e-iniciativa.md` — o turno, os recursos que ele contém, iniciativa e a régua de preço das Restrições.
- `03-mecanica/conferir-acao.py` — valida a régua, roda dominância por conjunto de recursos e calcula o valor real da Melhoria Adianta. Passa.

### Decidido

- **O turno tem quatro recursos independentes:** movimento (até 9 m, divisível), ação padrão, ação bônus e reação. "Rodada inteira" não é um quinto — é gastar movimento, padrão e bônus de uma vez.
- **Deslocamento base: 9 metros.** Conversa com as distâncias que o Fundamento já usa: fecha metade de um duelo de 18 m num turno, e sair de uma explosão de raio 3 m custa um terço do movimento.
- **Ataque de oportunidade existe.** Sem ele, sair de um corpo a corpo é grátis e a Melhoria Passo perde a razão de existir.
- **Concentração:** um efeito por vez; ao tomar dano, TR Físico contra CD 10 ou metade do dano, o que for maior. É a mesma régua que a Restrição Carregar já usava.
- **Iniciativa é rolada: d20 + Destreza.** Iniciativa fixa seria mais rápida e mais auditável, mas quebraria a Melhoria Adianta — com ordem fixa, quem tem Destreza alta age antes em 100% das rodadas e Adianta vira +2 permanente. É o teste do bônus automático falhando.
- **A régua de preço das Restrições, derivada dos recursos:** Leve consome um recurso, ou meio recurso por dois turnos. Média consome o turno inteiro, ou um recurso mais um risco real.

### Resolvido — a tensão Carregar × Lento, aberta desde a v7.3

O changelog do Fundamento registrou que Carregar dói mais que Lento pelo mesmo preço e não dava para subir sem estourar o fecho de devolução. Com os recursos definidos, não há dominância: Lento consome três recursos deste turno sem risco; Carregar consome um recurso do turno anterior mais o risco. São conjuntos diferentes.

O que faltava era o texto dizer se **quem carrega pode se mover no turno de carga**. Decidido que sim: só a ação padrão vai embora. É a leitura mais natural do texto atual, é o que torna a peça distinta de Lento, e não muda nenhum dos 35 feitiços prontos porque nenhum usa Carregar.

**A lição:** tensão de preço às vezes é lacuna de texto disfarçada. Antes de mexer no número, conferir se a regra diz o que se acha que ela diz.

### Verificado

As onze Restrições do catálogo cabem na régua, e o teste de dominância por conjunto de recursos não encontra nenhum par em que um contenha o outro. O catálogo estava certo — só não tinha como provar.

### Em aberto

- Nome do sistema.
- **Se ação bônus deve existir mesmo.** É a mais herdada das quatro e a que mais custa em tempo de mesa. Duas peças do Fundamento dependem dela. Medir no playtest quantos turnos usam uma.
- **Quantas reações por rodada.** Uma é o padrão, e quatro coisas competem por ela: ataque de oportunidade, a Melhoria Reação e as Passivas Contramedida e Reforço. Competir é bom, mas se ninguém nunca tiver reação sobrando, as Passivas de reação ficam mortas.
- **O valor de Adianta:** entre 4 e 7 pontos percentuais de efeito médio, abaixo do que uma Média costuma entregar.

---

## [0.10] — 2026-08-06

### Adicionado

- `03-mecanica/02-economia-de-atributos.md` — escala, criação, crescimento e teto dos atributos.

### Decidido

- **Escala 0 a 6, o número é o modificador.** A escada de 1 a 30 com o 10 valendo 0 foi descartada: o sistema inteiro já foi montado sem conversão, conversão custa caro com cinco a sete mestres, e a granularidade extra serve para bônus pequenos que este sistema não tem. O d20 clássico carrega essa escada por razão histórica — os modificadores foram inventados depois dos scores.
- **Criação: nove pontos entre os cinco atributos, nenhum acima de 3.** O arranjo padrão é 3·2·2·1·1. O teto de 3 não é arbitrário: é o que faz o atributo investido crescer exatamente +3 na campanha, o mesmo ritmo da maestria.
- **Crescimento:** a cada quatro níveis, passivo de +1 atributo e +1 refino, mais uma escolha entre outro ponto de atributo ou outro de refino com uma aptidão. Sete marcos, nos níveis **6, 10, 14, 18, 22, 26 e 30** — contados a partir do começo da ficha no nível 2, fechando exato no 30. A maestria sobe em três desses marcos (10, 18 e 26), um sim e um não, então nenhum marco fica vazio e nenhum acumula dois ganhos grandes.
- **Teto do atributo: 6, fixo.** Um teto que crescesse com o nível manteria o ponto de atributo sempre valioso e travaria a escolha em "atributo" a campanha inteira.
- **Origem não dá atributo.** Em JJK a origem é a fonte do poder, não o corpo — ser recipiente não dá Constituição, dá um passageiro. Amarrar número à origem criaria a origem ótima por build, que é empurrar a identidade para a camada errada num sistema cujo pilar é a técnica. A origem dá a patente inicial, um traço não numérico e o gancho de ficção.

### Achado

**A curva se auto-equilibra e a escolha não precisa de trava.** O atributo principal bate no teto no nível 10 ou 14; depois disso o ponto de atributo cai num secundário e vale menos, enquanto uma aptidão nova continua valendo o mesmo. O jogador tende a pegar atributo cedo e refino depois sem que nenhuma regra mande — o valor relativo dos dois lados muda sozinho com o tempo. Era o problema 1 da seção 4.3 do esqueleto, e ele se resolve pelo teto fixo em vez de por degraus de peso.

### Em aberto

- Nome do sistema.
- Quantos pontos de perícia, e se perícia é treinada ou tem graus.
- De onde vem o treino nos Testes de Resistência.
- Se Força precisa de um segundo trabalho.

---

## [0.9] — 2026-08-06

### Corrigido — um erro meu que a pergunta do Mizuki encontrou

**O validador da v0.8 tinha um ponto cego.** Ele testava se a chance mudava com o nível **mantendo os atributos fixos**. Isso verifica se o nível cancela, mas não se a **campanha** cancela: o defensor não fica com Destreza 3 para sempre, ele investe e chega a 6. O ataque de conjuração era um valor fixo mais maestria, e maestria crescia +7 enquanto o atributo do defensor crescia +3. A v0.8 derivava 15 a 20 pontos percentuais e passava no teste assim mesmo.

**A regra que ficou:** numa rolagem disputada, os dois lados precisam crescer no **mesmo ritmo**. Não basta os dois crescerem. Atributo investido cresce +3 numa campanha; maestria a cada 4 níveis crescia +7 — rápido demais para substituir um atributo.

### Alterado

- **Maestria sobe a cada oito níveis**, não quatro. De 1 a 4 ao longo da campanha, o mesmo ritmo de um atributo investido. Continua caindo nos marcos de quatro níveis, só que num sim, num não.
- **Maestria saiu da Defesa e do Teste de Resistência.** Ela fica no ataque de conjuração, na CD e nas perícias. Com isso, nenhum número aparece dos dois lados da mesma rolagem — que era exatamente a objeção levantada.
- **Ataques físicos usam atributo direto:** corpo a corpo soma Força, à distância soma Destreza. Sem maestria, porque o atributo já cresce dos dois lados e se anula sozinho.
- **Ataque de conjuração = 2 + maestria**, e o 2 não é gosto: é o número que faz o conjurador empatar com o guerreiro do nível 2 ao 30. Com 5 ele acertava 15 pontos percentuais a mais a campanha inteira, o que seria de graça — o dano dele já vem do orçamento do feitiço.
- **Habilidade de Caminho pode trocar o 2 fixo por um atributo**, e a troca é neutra em balanço porque os dois crescem igual. É por aí que nasce o feiticeiro que conjura pela Força, no molde do Todo.
- **Perícia = atributo + maestria**, e aqui a deriva para cima é o objetivo: +30 pontos percentuais ao longo da campanha. É o único lugar onde crescer é o ponto, porque o mundo não cresce junto — uma fechadura comum continua sendo uma fechadura comum.

### Resultado

Guerreiro, atirador e conjurador acertam **50%** contra um alvo que também investiu em defesa, em qualquer nível do 2 ao 30. Resistir dá 55% sem treino e 65% treinado, também sem deriva. Deriva medida: **zero** em tudo que não deve derivar.

### Lição de método

Verificar invariância contra o nível não basta. **Tudo que cresce numa campanha precisa entrar no teste** — atributo, proteção, equipamento. O validador foi reescrito para variar os atributos junto com o nível, e ganhou uma checagem nova: nenhum termo pode aparecer dos dois lados da mesma rolagem.

---

## [0.8] — 2026-08-06

### Alterado

- **Cinco atributos, não seis.** Sabedoria e Carisma fundiram em **Essência** — vontade, presença, o que você é por dentro e o que isso projeta. O que Sabedoria fazia de percepção migrou para **Inteligência**, que assim deixa de ser o atributo-depósito clássico e passa a carregar o que mais importa em Jujutsu Kaisen: perceber energia amaldiçoada.
- **"Passo" virou "Maestria".** Conferido: não aparece nenhuma vez no manual.
- **A ficha começa no nível 2**, já com um feitiço. Maestria começa em 1 e sobe a cada quatro níveis a partir do 6, fechando exata em 8 no nível 30. O nível 1 fica como opção de campanha — o personagem antes de ser feiticeiro, o Itadori antes do dedo.
- **CD unificada:** `8 + maestria + atributo relevante`, uma forma só para a ficha inteira. Para feitiço, o atributo dá lugar a um **valor fixo de 5**, que é o que impede o imposto de maximizar a estatística de conjuração.
- **Ritmo de combate: 3,2 rodadas é o alvo**, não um defeito a corrigir. O manual precisa passar a mostrar as duas colunas de letalidade, com a de 60% de acerto marcada como a de mesa.

### Corrigido pela conta, antes de virar regra

- **Maestria só para quem é treinado produzia a espiral do d20.** O não treinado caía de 55% para 20% de sucesso entre o nível 2 e o 30 — salvaguarda sem treino virava sentença, e o mestre passaria a precisar saber nível *e* treino do alvo para estimar qualquer coisa. Conserto: todo mundo soma maestria no TR e treinado ganha **+2 fixo em cima**. Mesma intenção, sem a espiral, e treinar passa a valer exatos 10 pontos percentuais para sempre.
- **Defesa sem maestria quebrava o outro lado.** Com o ataque crescendo contra um número parado, o acerto ia de 65% no nível 2 a **100% no nível 30** — nem o 1 natural erraria. Conserto: a defesa carrega maestria igual ao ataque.

### Resultado

Três números batem no mesmo lugar e não mudam com o nível: acertar alvo de Destreza 3 com proteção 1 dá **60%**, resistir com atributo 2 treinado dá **60%**, sem treino dá **50%**. `conferir-atributos.py` passa em todos os invariantes.

### Em aberto

- Nome do sistema.
- Quantos TRs cada personagem é treinado, e de onde vem esse treino — Origem, Caminho ou os dois.
- Se Força precisa de um segundo trabalho: é o único candidato a depósito que sobrou.
- Quanto Inteligência realmente pesa na mesa. Ficou a mais carregada das cinco.

---

## [0.7] — 2026-08-06

### Adicionado

- `03-mecanica/01-atributos-acerto-defesa.md` — a primeira peça de mecânica com número. Atributos, rolagem de acerto, defesa e Teste de Resistência.
- `03-mecanica/conferir-atributos.py` — validador dessas fórmulas, com contrato de invariantes. Roda antes de fechar qualquer versão que mexa nelas. Passa.

### Decidido

- **O nível entra dos dois lados da conta e se cancela.** Ataque e defesa crescem no mesmo passo; CD e resistência também. O que sobra é a diferença de atributo. Bounded accuracy deixa de ser disciplina a manter e vira consequência da fórmula, e um mestre nunca precisa saber o nível para saber a chance.
- **Passo = nível ÷ 4**, arredondando para baixo. Mesma cadência do refino e do atributo. É a única coisa que cresce com nível.
- **Seis atributos com os nomes clássicos:** Força, Destreza, Constituição, Inteligência, Sabedoria, Carisma. O número é o modificador direto, escala 0 a 6, sem valor separado e sem tabela de conversão. É escolha deliberada e não herança: compra custo de ensino zero, e o custo de seis números não expressarem o personagem não pesa porque a identidade mora na técnica. Todos os seis conferidos contra o manual — nenhum é termo definido lá.
- **Quatro Testes de Resistência, não seis**, para eliminar salvaguarda-depósito: Físico (Força **ou** Destreza, declarado na criação e travado), Vigor (Constituição), Intelecto (Inteligência), Espírito (Sabedoria **ou** Carisma, também travado).
- **Cada atributo tem um serviço fora do TR**, ou o não-escolhido de cada par vira lixo de ficha. Duas amarras são específicas de JJK e resolvem o problema clássico de Sabedoria e Carisma: **Sabedoria percebe energia amaldiçoada** e **Carisma negocia Pactos**.
- **O tipo de dano da técnica decide qual TR o feitiço força**, por padrão. Fogo, corte e peso pedem Físico; veneno pede Vigor; ilusão e voz pedem Intelecto; o que encosta em alma pede Espírito. Uma Melhoria pode trocar.
- **Dano na alma passa a forçar TR de Espírito**, e Integridade volta a ser só reserva.
- **Fórmulas:** bônus de conjuração = 3 + passo · CD = 10 + bônus · defesa = 10 + passo + Destreza + proteção · TR = d20 + atributo do TR + passo.
- **Defesa evita ser acertado; RD reduz o que passou.** Cobrir-se de energia é a fonte natural de RD, e é por isso que ela é aptidão básica de todo feiticeiro.
- **Patente com oito degraus**, incluindo semi-especial: grau 4, 3, semi-2, 2, semi-1, 1, semi-especial, especial. Semi-especial é extensão deliberada — pelo que se sabe não existe no cânone, e é o limbo dramático mais rico da escada.

### Achados sobre o manual existente

**O Fundamento diz "Teste de Resistência" dezoito vezes e especifica de qual apenas uma vez** — no dano de alma. As outras dezessete não dizem contra o quê se resiste. Com quatro TRs, a lacuna vira profundidade em vez de continuar aberta.

**"Teste de Resistência de Integridade" é ambíguo:** o manual manda rolar sem dizer o que se soma, e Integridade é uma reserva, não um modificador. Resolvido acima.

A tabela de letalidade do Fundamento supõe que **todo ataque acerta**: ela divide vida pelo pico de dano. Com taxa real de acerto de 60%, o combate leva de 2,8 a 3,3 rodadas em vez de 1,7 a 2,0. Não é erro de conta — a coluna mede o que diz medir —, é descasamento entre o que a tabela informa e o que o mestre decide com ela. Feitiços que resolvem por Teste de Resistência ficam mais perto da coluna original, porque neles o dano passa mesmo no sucesso do alvo.

### Em aberto

- Nome do sistema.
- O ritmo de combate desejado, à luz do achado acima.
- Se algum atributo deve entrar na conta do feitiço (hoje nenhum entra — é o que faz o nível cancelar).
- Se PE deve receber contribuição de atributo (hoje cresce só com nível).
- Se o generalista deve ter alguma aptidão garantida.
- Os degraus de peso das aptidões, amarrados ao refino atual.

---

## [0.6] — 2026-08-06

### Decidido

- **Tamanho do feitiço passa a se chamar Classe.** "Um feitiço de terceira classe". Soa como classificação burocrática, o que combina com uma sociedade jujutsu que registra e cataloga. Volume e Fluxo ficam registrados como alternativas.
- **O chassi passa a se chamar Caminho**, com Trilhas dentro. Consequência obrigatória da decisão acima: a mesma palavra não pode significar as duas coisas. Vocação e Estilo ficam como alternativas livres.
- **Progressão de Refino fechada:** passivo e escolha ao mesmo tempo, teto 10, começo em 1. A cada quatro níveis o personagem ganha refino e atributo de graça e escolhe onde recebe o bônus extra. Especialista chega ao teto no nível 20; generalista termina em 8 no nível 28.
- **Trava que faz o Refino fechar:** com o refino no teto, escolher refino ainda concede a aptidão. Sem ela, o especialista desperdiça três escolhas depois do nível 20.

### Nota de método

Ao checar colisão de nome contra o manual, separar **termo definido** de **prosa solta**. As palavras *caminho*, *papel*, *função* e *classe* aparecem no Fundamento uma ou duas vezes cada, sempre em frase corrida. Isso não é colisão — vira colisão quando a palavra carrega definição. Livres de qualquer uso: vocação, estilo, postura, trilha, perfil.

### Em aberto

- Nome do sistema.
- Se o generalista deve ter alguma aptidão garantida (hoje termina com zero).
- Os degraus de peso das aptidões, amarrados ao refino atual.
- Onde a Regra da técnica entra na ordem de criação.

---

## [0.5] — 2026-08-06

### Adicionado

- `02-esqueleto/arquitetura.md` — o esqueleto do sistema. Mapeia o que o Fundamento já resolve, os onze buracos em volta ordenados por carga, a estrutura de criação de personagem em cinco camadas e as travas de mundo compartilhado. Sem número nenhum, de propósito.

### Decidido

- **Três eixos separados:** Nível (poder mecânico, da ficha), Grau (patente social, da instituição) e o tamanho do feitiço. É o que permite o Yuta nascer no topo da patente sabendo pouco, e o Itadori ter poder sem reconhecimento.
- **A colisão do Grau se resolve renomeando o tamanho do feitiço, não a patente.** O Grau-tamanho está entranhado no manual; o grau-patente está entranhado na cabeça da Guilda há anos porque é o termo da obra. Dá para vencer um manual, não o vocabulário de uma comunidade. Nome provisório: **Potência**.
- **Patente com sete degraus**, incluindo os semi: Grau 4, 3, semi-2, 2, semi-1, 1, especial. Funciona porque a patente não carrega número mecânico — ela compra acesso, autoridade, obrigação e risco.
- **Estrutura do personagem em cinco camadas:** Origem, Chassi, Técnica, Refino e Aptidões, Pactos.
- **Trava do chassi:** ele não dá poder novo, muda o que o poder alcança. Mexe em posicionamento, alvo, duração e recuperação, nunca em número de dano. Escolhido na criação, com poucas escolhas de trilha depois.
- **Trava das aptidões:** não produzem dano e não escalam com nível. São binárias, e o refino governa confiabilidade e custo, não potência. É o que as mantém fora da economia do Fundamento.
- **Morte no modo não letal não vira regra.** O peso vem de consequência no mundo, arbitrada pelo mestre com apoio de perícia e rolagem mundana. Não fura o filtro do multi-mestre porque o filtro protege os números, não a ficção — consequência narrativa não é portátil entre mesas.

### Em aberto

- Nome do sistema.
- Nome definitivo do tamanho de feitiço (Potência é provisório; Volume e Fluxo são as alternativas registradas).
- Como equilibrar a escolha entre refino e atributo, hoje provavelmente dominada pelo refino.
- Se a escala de refino é 1–7 ou existe outra fonte de refino além do nível.
- Onde a Regra da técnica entra na ordem de criação.

---

## [0.4] — 2026-08-06

### Alterado

- `design-mecanicas-rpg` ganhou a seção **"O nome é parte do design"**: checagem de colisão de termo para fora do sistema (palavra que já significa outra coisa no hobby) e para dentro. Veio do retorno do Mizuki de que "Vulnerável", na maior parte das mesas, significa *tomar mais dano* e não *ficar mais fácil de acertar*.
- `redacao-acessivel-rpg` ganhou **"Presunção sobre o que você não viu"**: quando revisar um trecho exige presumir coisa sobre o resto do material, perguntar antes de reescrever; se tiver que seguir, marcar a presunção no ponto do texto onde ela pesa, não numa nota no fim. Veio do retorno de que declarar a presunção é melhor que escondê-la, mas os dois perdem para perguntar.
- A seção de colisão de termo da `redacao-acessivel-rpg` passou a cobrir também colisão externa.

### Corrigido

- Falso negativo na correção automática do `eval-3`: a asserção "diz quando parar de testar" exigia as expressões "parar de testar" ou "critério de saída", e a resposta dizia "o sinal de parar continua o mesmo de sempre: quando o retorno de uma rodada só repete o da anterior, para". A regex foi corrigida e a execução com skill passou de 6/7 para 7/7. A média com skill subiu de 92,2% para 95,8%.

---

## [0.3] — 2026-08-06

### Adicionado

- Quatro skills de apoio, escritas e instaladas na conta: `design-mecanicas-rpg`, `balanceamento-simulacao`, `playtesting-rpg` e `redacao-acessivel-rpg`. Cópia de trabalho em `skills/`, com os arquivos de apoio que a versão instalada traz embutidos.
- `workspace-skills/iteration-1/` — nove execuções de teste (quatro com skill, quatro linha de base morna, uma linha de base fria), com `eval_metadata.json`, `timing.json` e `grading.json` por execução, mais `benchmark.json`.
- `workspace-skills/revisao-iteracao-1.html` — visualizador de revisão, abre no navegador.
- `workspace-skills/montar-benchmark.py` — o script que gera tudo isso, com as ressalvas de método no cabeçalho.
- `ESTADO-ATUAL.md` — ponto de retomada do projeto.

### Decidido

- Mecânica de resolução: **d20**. O Fundamento já é arquitetura d20 (CD, Teste de Resistência, RD, vantagem) e o teto que o dossiê exigia já existe nele, no orçamento em vez de no dado.
- Recurso central: energia amaldiçoada como pool numérico.
- Progressão numérica contínua, com Nível separado de patente.
- Morte: misto letal / não letal, declarado por mesa.
- Guilda: 5 a 7 mestres ativos, 2 a 3 mesas por semana.

### Auditoria

- Verificado que nada da sessão interrompida ficou truncado: os 21 arquivos criados estão íntegros, os scripts rodam e as oito referências internas das skills resolvem.
- A execução que faltava (`eval-3` sem skill) foi rodada em duas condições distintas, morna e fria, para separar "skill contra Claude que leu o dossiê" de "skill contra nada".

### Em aberto

Nome do sistema. E uma colisão de termo a resolver: **Grau** significa tamanho de feitiço no Fundamento e também patente do feiticeiro em JJK. Renomear a patente antes de a comunidade adotar.

---

## [0.2] — 2026-08-05

### Adicionado

- Comparador de curvas (`03-mecanica/comparador-de-curvas.html`) — ferramenta interativa que calibra seis mecânicas na mesma chance de sucesso e compara o formato da curva de progressão. Abre no navegador, funciona offline exceto pela biblioteca de gráfico.
- Dossiê de metodologia (`01-pesquisa/dossie-de-metodologia.md`) — lentes de decisão, espaço de design, mundo compartilhado multi-mestre, matemática de dado calculada, metodologia de playtest, estrutura de manual e leitura de IP.
- Dez travas de arquitetura que a fase de esqueleto herda (seção 8 do dossiê).

### Alterado

- Pitch: nova pergunta em aberto sobre o tamanho real da Guilda (nº de mestres e jogadores ativos), porque a consistência entre mesas depende disso.

### Decidido

- Ferramenta de probabilidade: `dice-calc` (Python, roda local, compila código do AnyDice). Testado e funcionando.
- Ciclo de playtest: 5 pessoas × 3 rodadas, com correção entre rodadas, em blocos temáticos de duas semanas (formato copiado do playtest público do Pathfinder).
- Estrutura do material final: quick-start jogável na frente do livro, referência atrás — decisão de estrutura, não de diagramação.
- Progressão será tabelada ou por gatilho, nunca discricionária do mestre, e com teto (bounded accuracy) — requisito derivado do personagem persistente entre mestres.

### Revisado

- Dossiê passou por revisão independente: corrigidos um erro de célula na tabela de +1 em 2d6, arredondamento inconsistente na tabela de vantagem, rótulo ambíguo na tabela estilo Blades e a data/premiação do Fabula Ultima.

---

## [0.1] — 2026-08-05

### Adicionado

- Pitch de design (`00-fundacao/pitch-de-design.md`) — visão geral, três pilares, restrições duras e perguntas em aberto.
- Estrutura de pastas do projeto.

### Decidido

- Base ficcional: Jujutsu Kaisen, como material de fã gratuito. Sem venda, sem monetização.
- Contexto de jogo: server de Guilda com múltiplos mestres e mini-campanhas; personagem persistente entre mesas.
- Formato: roleplay por texto entre sessões, rolagem majoritariamente ao vivo.
- Tom shounen de ação; crunch equilibrado.
- Primeiro entregável é esqueleto estrutural, não regra jogável.

### Em aberto

Mecânica de resolução, recurso central, funcionamento do rank no server, molde de técnica inata, tratamento de morte e nome do sistema.

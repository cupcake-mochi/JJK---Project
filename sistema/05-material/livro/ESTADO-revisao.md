# Estado da revisão · Manual da Guilda

## Diagramação — v0.126, 22/08/2026

**Três variantes no disco, e a escolha é do Mizuki.** *Ele leu o PDF e perguntou se não seria melhor em colunas, dando o sumário como exemplo — seis páginas para achar um capítulo.*

| | páginas | sumário | o que ela é |
|---|---|---|---|
| `-A-atual` | 256 | 6 páginas | snapshot do publicado na v0.125, não se regera |
| *(sem sufixo)* | 253 | **3 páginas** | quebras consertadas, sumário em duas colunas |
| `-C-duas-colunas` | **167** | **2 páginas** | corpo em duas colunas a 9,4pt |

### A medida que decidiu

*Três manuais do hobby, lidos com extrator de posição de palavra:*

| livro | duas colunas | corpo |
|---|---|---|
| Guia do Mestre 5e (A4) | 83% | ~9,3pt |
| Caldeirão de Tasha | 92% | ~9,3pt |
| PHB 2024 | 92% | ~9,1pt |

> **A primeira medida deu `66%` de UMA coluna e estava errada.** *Ela procurava faixa vertical vazia no miolo — e título, tabela e abertura atravessam as duas colunas e apagam a faixa.* **O sinal certo é a margem esquerda das linhas.** *Sétimo caso do mesmo erro aqui: medir o marcador em vez do fenômeno.*

**A mancha copiada é a do Guia do Mestre**, o único dos três em A4: colunas de ~245pt, goteira de 20pt, margens externas de 12 a 15mm contra os 26 a 32mm que este livro usava.

### O que precisou ser resolvido no build

> **⚠ O WeasyPrint 69 não implementa `column-span: all`** — medido com caso mínimo: um `h2` e uma `table` marcados com ele continuaram presos na coluna da esquerda.

**A `segmenta_colunas` do `build.py` faz o trabalho:** sequência de elementos estreitos vira `<div class="c2">`, e a tabela larga fica solta entre eles, em largura inteira. *O corte é o **número de colunas** — quatro ou mais, `40` de `211` tabelas.* **Largura em caracteres não serve: célula de prosa quebra bem numa coluna estreita, e é ela que domina a medida.**

**E as duas que enchem uma página sozinha começam numa** — o catálogo de 52 armas e a tabela de progressão. *Sem isso o título ficava no pé da coluna anterior, mesmo virado `<caption>`.*

### As quebras de página, e o diagnóstico que se desmontou

**O defeito real era título + frase de chamada + caixa**, com os dois primeiros no pé de uma página e a caixa na seguinte.

> **`break-before: avoid` em toda caixa reprovou com número:** *são `253` caixas, e a versão com ela ficou com as mesmas oito páginas curtas e **nove páginas a mais**.* **O alvo certo é o par, reconhecido pelo texto — parágrafo terminado em dois-pontos seguido de caixa.** *São oito no livro, e a `cola_chamada` cola os oito.*

| eu contei | era |
|---|---|
| 8 páginas curtas | **2** — seis eram fim de capítulo, e capítulo abre em página nova |
| 7 títulos órfãos | **0** — os sete eram célula de tabela com o mesmo texto de uma seção |

### A quebra dura dentro das caixas

**Ela dependia de onde o autor apertou Enter no `.md`.** *Em coluna larga não aparecia, porque as linhas do fonte têm ~90 caracteres.* **Numa coluna de 236pt a caixa saía picotada no meio da frase.** *Agora a quebra dura só entra em linha de regra — fórmula, nome em negrito na frente, linha curta —, e prosa longa reflui.*

### Revisão de texto

*Varredura mecânica nos 17 capítulos.* **Um achado real:** a linha *"Sem Técnica — texto único, compartilhado pelas cinco Origens principais"*, cinco vezes, uma em cada lista de `Destranca`. **Ela fala do livro e não do jogo**, que é o que a seção *O livro não fala de si mesmo* proíbe. *Trocada pelo que a entrada faz.*

> **O `conferir-voz.py` não pega esta**, porque a `MOLDURA` dele procura "este manual", "este livro" e "este capítulo". **Fica registrado e NÃO virou regex** — expressão feita para casar uma frase só é o aviso que dá o motivo errado.

*O resto da varredura: `224` suspeitas de espaço antes de pontuação, todas a linha `{: .tab-titulo }`; `2` palavras repetidas, as duas corretas (`Mei Mei` é nome, e `quem te fez fez` é sujeito mais verbo); `2` termos com e sem crase, os dois seguindo a convenção de crase na estreia e seco na prosa.*

---

## Sincronização com a fonte — v0.124 e v0.125, 22/08/2026

**O livro estava cinco versões atrás, e não era passada de texto: era conteúdo faltando.** *A v0.123 mediu e registrou a dívida; esta versão paga ela e põe uma checagem em cima para ela não voltar.*

| | antes | depois |
|---|---|---|
| capítulos numerados | 15 | **17** |
| palavras | 74.222 | **79.362** |
| páginas | 237 | **256** |
| Legados publicados | 80 | **85** |

**Dois capítulos entraram, e a posição dos dois é decisão do Mizuki:** `42-tecnica-marcial.md` como o **capítulo 10**, colado no Fundamento, e `47-bencaos-e-lapidacao.md` como o **12**, colado em Aptidões e Refino. *O prefixo dos arquivos-fonte tem folga, então nenhum arquivo foi renumerado — o que desloca é o número impresso, do 10 em diante.*

### O que estava atrás, item por item

| o que faltava no livro | entrou na |
|---|---|
| as catorze Bênçãos e a Lapidação | v0.118 — era capítulo inteiro |
| o ramo `Energia pelo corpo` virar `sem energia` | v0.118 |
| o sexto formato de gate — requisito de atributo | v0.118 |
| `PE` lendo como `Pontos de Esforço` | v0.120 |
| a Técnica Marcial, e os renomes `Kata` · `Ruptura` · `Ōgi` | v0.122 |
| `Ação de Movimento` e a regra de sacar e guardar | v0.123 |
| cinco Legados de `Desliga` | v0.104 |
| a penalidade de arma sem treino e sem requisito | v0.104 |
| a regra de Pactos, que fechou como três formas com dono | v0.116 |

### ⚠⚠ E um achado que não estava na lista: a fórmula de acerto da v0.117

**A lista da v0.123 media termo ausente. Isto é número publicado errado, e são cinco lugares.**

| onde | o livro dizia | a fonte diz |
|---|---|---|
| cap. 1, *Testes de Resistência* | `d20 + atributo, mais 2 se treinado` | `+ maestria`, e só se treinado |
| cap. 1, *Maestria* | *"três lugares"*, e **fora** do Teste de Resistência | toda rolagem de ataque, a CD, e o que você treinou |
| início rápido | `Atacar = d20 + Força` | `d20 + maestria + Força` |
| início rápido | `Teste de Resistência … +2` | a maestria |
| cap. 6, *Números do nível 2* | `CD de feitiço` valendo `13` | `8 + atributo da técnica + maestria` |

> **O `13` é o rastro mais claro: ele é `10 + 2 + maestria`, a CD que a v0.117 aposentou.** *Um número solto onde as linhas vizinhas são fórmula.* **As três linhas de ataque da mesma tabela também tinham perdido o `+ 1` da maestria.**

### A checagem que fecha isso

**Entrou a checagem 10 do `conferir-repositorio.py`.** *A 7 pergunta se o **recorte** da entrega está atualizado, por md5; a 10 pergunta se o **conteúdo** do livro bate com as peças.* **Seis sub-blocos: as três listas de capítulo, os órfãos da pasta, a referência cruzada por número, o vocabulário batizado, o catálogo de Legados, e pendência morta dentro do livro.**

> **A 10.1 nasceu de um defeito real desta versão: `build.py`, `build_docx.py` e `conferir-voz.py` carregam a ordem dos capítulos cada um por conta, e nada comparava os três.** *Capítulo novo entra num e some dos outros dois.*

*Rodada de fechamento, com `--estrito`:* **o `conferir-voz.py` sai com `0` achados, `0` referência quebrada e `0` termo sem destino.** *Ele só sai com código `1` quando recebe `--estrito`, e o `subir.sh` não roda ele — vale saber isso antes de ler um verde dele como prova.*

---

> ## Passada de termos — CONCLUÍDA em 21/08/2026
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
> | exemplo em **bloco** por mil | 0,00 | 0,38 | **0,49** |
> | "Por exemplo," **inline** por mil | 0,58 | 0,58 | **0,08** |
> | **parênteses** por mil | **6,67** | **6,72** | **1,13** |
>
> **O livro não tem problema de prolixidade** — é mais enxuto que os dois em toda medida de
> tamanho, e tem **mais** exemplo em bloco que o GURPS. *O D&D não usa bloco de exemplo
> nenhuma vez em 397 páginas.* **O que falta é remissão — 73 vezes menos que o D&D — e
> parêntese, que ele usa seis vezes mais.**
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
> ### Fase 3 — remissões, feita por medida e não por atacado
>
> **O alvo não foi "espalhar ponteiro", foi achar onde ele falta de verdade:** termo cuja
> **primeira aparição no livro** é fora do capítulo dono, porque aí o leitor encontra a
> palavra antes de ela ter sido apresentada. **Eram 23 casos**, e a triagem derrubou a maior
> parte:
>
> | | quantos | por quê |
> |---|---:|---|
> | falso positivo por nome homônimo | 5 | `Reação`, `Condição` e `Carregar` são Melhorias do capítulo 9, não os conceitos gerais; `Yumi` e `Arma de Fogo` são rotas da Trilha Batedor, não as armas do catálogo |
> | já apontavam | 7 | o livro já remetia onde alguém pensou nisso |
> | não devem apontar | 3 | os três do `08-inicio-rapido`, que é autocontido de propósito — a ficha da Kaori traz o efeito inteiro na hora |
> | já cobertos pela linha seguinte | 1 | `Destranca`, coberto pelo ponteiro logo abaixo da tabela |
> | **remissões escritas** | **7** | `Agarrado`, `Remenda`, `Munição`, `Traje`, `Revestimento`, `Estigma` |
>
> *O total de ponteiros no formato `capítulo N, *Nome*` foi de 42 para 49.* **O
> `guard_numeros.py` acusou 5 diferenças nos quatro arquivos, e todas são o número do capítulo
> recém-escrito.** Nenhum número de regra se moveu.
>
> ### Fase 4 — o capítulo 11 reordenado, e a validação contrariou o modelo
>
> **O defeito não era a distância até a tabela; era que a tabela que chegava primeiro não
> servia para escolher arma.** *O `Índice A–Z` trazia `arma | categoria | treino` — três
> colunas, nenhum dado de jogo — e os dados viviam espalhados em treze tabelas de grupo.*
> **Não existia no capítulo nenhuma tabela que permitisse comparar duas armas.**
>
> **A divisão do PHB não serve aqui, e medir mostrou por quê.** *Lá a proficiência é por arma,
> então ele corta em `simples/marcial × corpo a corpo/distância`.* **Neste sistema o treino
> mora na categoria** — treinar `Lâmina Longa` libera as oito —, **e são três listas, não
> duas: simples (26 armas), marcial (19) e de fogo (7).** Copiar o corte do PHB quebraria o
> vínculo entre categoria e treino, que é regra.
>
> **O que ficou:** uma tabela só, `Catálogo de armas`, com `arma | categoria | mão | dado |
> propriedades | requer Força`, em três blocos por lista de treino e alfabética dentro de cada
> bloco. O `Índice por propriedade` continua. As treze categorias perderam a tabela e
> mantiveram as **70 linhas de prosa** que descrevem cada família.
>
> | | antes | depois |
> |---|---:|---:|
> | capítulo inteiro | 601 linhas | **486** |
> | linhas de tabela no catálogo | 132 | **60** |
> | tabelas onde a arma aparece | 14 | **1** |
> | armas | 52 | **52** |
>
> *Conferido depois da reescrita: nenhuma das 52 armas se perdeu, nenhuma tabela de grupo
> sobrou órfã, e o `guard_numeros.py` acusou 6 diferenças — todas do texto de abertura
> reescrito (`52` armas, `seis` colunas em vez de `cinco`, `treze` categorias, `três` blocos).*
> **Nenhuma notação de dado mudou.**
>
> *Duas frases minhas quebraram a regra `TABELA-VAGA` — diziam "a tabela" sem nome próprio — e
> o `conferir-voz.py` pegou as duas.* **Corrigidas para citar o `Catálogo de armas` pelo nome.**
>

> ### Exemplos: o diagnóstico errou duas vezes, e a segunda foi de método
>
> **Primeiro erro, regex cego.** A conta original procurava `Exemplo:` com dois-pontos, e este
> livro escreve `**Exemplo.**` com ponto: contou `2` onde havia `36`. *O livro tem `0,49`
> exemplo em bloco por mil palavras, contra `0,38` do GURPS — e o D&D não tem nenhum.*
>
> **Segundo erro, e foi o Mizuki que apontou: medir marcador não é medir fenômeno.** *O D&D
> exemplifica sem escrever "por exemplo" — salta direto para o caso concreto depois da
> palavra-chave.* **Contar `Por exemplo,` subestimava ele.**
>
> A medição refeita em sete padrões achou o que realmente separa os três:
>
> | padrão | D&D | GURPS | este livro |
> |---|---:|---:|---:|
> | `Se você …,` | **0,77** | 0,03 | 0,13 |
> | `como o/a/um/uma` | 1,25 | 1,34 | 0,52 |
> | **parênteses** | **6,67** | **6,72** | **1,13** |
> | dois-pontos + caso | 0,20 | 0,61 | **5,43** |
>
> **Este livro usa dois-pontos onde os dois usam parêntese** — escolha de estilo, não falta.
> *Mas parêntese ele usa seis vezes menos, e é aí que mora a diferença.*
>
> ### O que os parênteses do PHB carregam, e é o achado da passada
>
> Classificados os 2.889 do PHB: **58% não são exemplo, são rótulo de categoria no ponto de
> uso** — `(magia)` 391×, `(característica de classe)` 124×, `(talento)` 73×, `(perícia)` 18×.
> **Toda vez que ele cita um termo, diz de que espécie aquilo é, ali na linha.**
>
> *Aqui a crase diz que a palavra é termo do sistema e não diz de que tipo.* **É a metade que
> falta, e é a que fez uma leitora travar no `colado`.**
>
> ### Aplicado: 5 rótulos, de 34 candidatos
>
> *A regra escolhida foi uma por capítulo — o termo de outro capítulo vem rotulado na primeira
> vez que aparece ali.* **Foram 34 candidatos e sobraram 5**, porque o livro já se anuncia
> sozinho na maioria dos casos: *"a **Restrição** `Carregar`"*, *"a **Trilha** `Sutura`"*, ou a
> frase anterior já abriu com *"**Condição** é um estado nomeado…"*.
>
> **Escritos:** `Derrubado` no início rápido e na Trilha Punho, e `Enfeitiçado`,
> `Incapacitado` e `Amedrontado` nos traços de Origem. *Nenhum número mudou em nenhum dos três
> arquivos.*
>
> ### Quatro exemplos inline no capítulo 1
>
> No formato do D&D — dentro da frase, entre 15 e 24 palavras, contra a mediana de `23` dele.
> Em `Teste`, `Maestria`, `Defesa` e `Integridade`. *As 12 diferenças do `guard_numeros.py` são
> todas números derivados de fórmula já publicada, incluindo o `20` do `d20`.*


> ### A terceira camada, aplicada às condições — 21/08/2026
>
> **A primeira tentativa reproduziu o defeito que ela queria consertar, e o Mizuki pegou.**
> *Eu propus os rótulos dentro da célula de tabela: `Seus ataques.` Desvantagem. `Contra
> você.` Vantagem.* **Ele leu e disse que o ponto virava vírgula, e que o negrito não indicava
> que a explicação vinha em seguida — que é exatamente onde a leitora travou no `colado`.**
>
> *Fui ver a formatação real do PHB, com `pdftotext -layout` em vez do texto corrido:*
>
> ```
> Amedrontado [Condição]
> Enquanto tem a condição Amedrontado, você sofre os
> seguintes efeitos.
>   Testes de Atributo e Ataques Afetados. Você tem
> Desvantagem em testes de atributo e jogadas de ataque…
>   Não Pode Se Aproximar. Você não pode se aproximar…
> ```
>
> **O que separa os efeitos não é o ponto — é a quebra de parágrafo, com indentação.** *O
> rótulo só fecha o nome de um bloco que já estava visualmente isolado.* **Rótulo no começo de
> bloco funciona; rótulo no meio de frase corrida vira pontuação decorativa** — e foi por isso
> que o `Atordoado`, que tem um efeito só, ficou bom na primeira tentativa e os outros não.
>
> **Decisão do Mizuki: seguir o PHB de verdade.** As catorze condições saíram da tabela e
> viraram entradas em prosa, cada uma com frase de âncora (*"Enquanto está `X`, você sofre os
> seguintes efeitos"*) e um parágrafo por efeito. **A tabela virou `Condições em uma linha`, no
> fim da seção, para consulta na mesa.**
>
> *O vocabulário de nomes de efeito é fechado e reutilizado, como o do PHB:* `Deslocamento` ·
> `Seus ataques` · `Contra você` · `Ação` · `Testes` · `Sai quando`, mais `Conjuração`,
> `Iniciativa` e `Resistência` onde a condição pede. **São 9 nomes para 14 condições; o PHB usa
> 13 para as 14 dele.**
>
> *Conferido depois: as catorze mantiveram todos os efeitos, verificados um a um por
> palavra-chave contra o texto antigo.* **As 7 diferenças do `guard_numeros.py` são valores que
> agora aparecem duas vezes — na entrada e no sumário.**
>
> ### A varredura pedida: o defeito não era generalizado
>
> *Varrido o livro inteiro atrás de parágrafo de regra com três ou mais efeitos amontoados.*
> **Cinco resultados, e nenhum é o defeito:** um é a entrada de `Atordoado` recém-escrita, dois
> são listas legítimas (*"movimento, Ação Padrão e Ação Bônus de uma vez só"*), e dois —
> `Provocar` e `Puxar a Linha` — são um efeito de duas faces, não efeitos independentes.
>
> **O problema estava concentrado nas condições, e fechou.**


> ### As "21 seções que enterram a tabela" não existem — 21/08/2026
>
> **O diagnóstico era meu e estava errado.** *A conta original mediu "palavras até a primeira
> tabela" e concluiu que 22 seções enterravam o conteúdo principal.* **Refeita contra os três
> formatos que este livro usa para sinalizar regra — subseção própria, bloco `>` e `**Nome**
> —`, o número real é zero.**
>
> Das 26 seções com 150 ou mais palavras de prosa antes da regra:
>
> | o que sinaliza a regra | quantas |
> |---|---:|
> | subseção própria (`Efeito na ficha`, `Características do Bastião`) | 13 |
> | regra direta logo depois da prosa | 9 |
> | nada | 4 |
>
> *E as quatro sem sinalização não são defeito:* `Presença em campo` e `Regra Própria` são
> prosa explicativa; `Combinações inviáveis` **abre** com a regra; e `Lâmina Longa` só aparece
> assim porque a consolidação do catálogo tirou a tabela dela, nesta mesma passada.
>
> **O comparativo com o PHB fica registrado, porque ele vale para escrita nova:** *ele gasta
> mediana de `81` palavras de prosa antes da primeira entrega de nível, com 75% em até `120` e
> um único caso acima de `200`.* **As oito Origens deste livro gastam de `223` a `286`** — mas
> a regra delas vive sob `### Efeito na ficha`, então quem procura acha pelo sumário. *É lore
> densa por decisão, não conteúdo enterrado.*
>
> > **O erro se repetiu quatro vezes nesta passada, sempre igual:** presumir o formato e medir
> > o proxy em vez do fenômeno. *Aconteceu com o regex de `Exemplo:`, com a contagem de
> > `Por exemplo,`, com o classificador de tabela do catálogo de armas, e aqui.* **Quando um
> > número sobre este livro parecer alto demais, o primeiro suspeito é o filtro.**


> ### Metodologia não é lei, e o PHB prova isso — 21/08/2026
>
> **Observação do Mizuki, e ela consertou a `REGRA-DE-VOZ.md`:** *o que os livros de sistema
> usam são metodologias, não regras — às vezes aplicam, às vezes não, às vezes trocam de
> forma dentro do mesmo documento.* **As seções que esta passada escreveu estavam redigidas
> como lei, e isso induziria erro em quem escrevesse depois.**
>
> Medido no PHB, a consistência dele é **dentro de cada família**, e cada família tem a sua:
>
> | família | segue a forma da família | como a forma abre |
> |---|---:|---|
> | `[Área de Efeito]` | 100% | *"Um Cone **é** uma área que…"* — definição |
> | `[Risco]` | 100% | *"Uma criatura **pode**…"* — descrição |
> | `[Condição]` | 86% | *"**Enquanto** tem a condição X…"* — âncora de tempo |
> | `[Ação]` | 55% | *"**Quando** executa a ação X…"* |
>
> **E o rótulo de categoria aparece em `40` das `767` entradas — 5%.** *Não é prática geral: é
> reservado ao nome que sozinho confunde.*
>
> **Três frases foram reescritas:** *"as quatro camadas do PHB"* virou *"a forma da família
> condição"*; *"a regra é uma por capítulo"* virou critério de dúvida, não de posição; e
> *"estreia de termo tem uma forma só"* virou a tabela das **quatro** formas que o livro já
> usa e o `conferir-voz.py` já reconhece — *porque a regra escrita contradizia a própria
> ferramenta, e nenhuma das duas estava errada sozinha.*
>
> > **A pergunta certa não é "qual é o padrão do livro", é "de que família é esta coisa, e que
> > forma as irmãs dela já usam".** Forma nova só quando a família é nova — e aí ela entra na
> > `REGRA-DE-VOZ.md` e no validador junto.

> ### A rota validada para a próxima passada — 21/08/2026
>
> **Duas rotas estavam na mesa, e medir contra o PHB descartou uma e reduziu a outra.**
>
> *Rota B — aplicar as camadas aos 74 blocos de habilidade de Trilha e Caminho:* **descartada
> como frente.** O PHB usa a terceira camada em apenas **15%** das `309` habilidades de nível
> dele, e este livro já usa em `8%` (6 de 74). *A diferença não justifica passada.* **As seis
> entram como trabalho avulso, não como fase.**
>
> *Rota A — exemplo inline:* **mantida, mas com o alvo corrigido.** O PHB escreve
> `Por exemplo,` dentro de habilidade em **2%** dos casos — *ele não exemplifica ali, e
> imitar isso nas Trilhas seria copiar o que a fonte não faz.* **Ele exemplifica nas regras
> gerais.**
>
> Separadas as 74 seções sem exemplo por tipo:
>
> | tipo | quantas | o que o PHB faz |
> |---|---:|---|
> | **regra geral** | **55** | é onde ele exemplifica — `0,58` por mil |
> | habilidade de Trilha/Caminho | 19 | quase não exemplifica — 2% |
>
> **A rota é: exemplo inline nas 55 seções de regra geral, e nenhum nas 19 de habilidade.**
> *Prioridade pela ordem de leitura — `08`, `11`, `12`, `15`, `20` primeiro, que é o que um
> jogador novo encontra antes de qualquer outra coisa.*
>
> > **Um número achado no caminho, e ele é do livro, não do método:** as habilidades daqui têm
> > **mediana de `26` palavras** contra `62` do PHB. *Elas são menos da metade do tamanho.*
> > **Isso não é defeito por si — pode ser densidade boa —, mas é a medida a olhar se algum
> > jogador reclamar que habilidade de Trilha é seca ou difícil de imaginar em jogo.**
>
> ### ⚠ Achado que não é de redação: `vida temporária` não tem regra — 21/08/2026
>
> **Oito efeitos concedem vida temporária e nada no projeto diz como ela funciona.** *`Apoio`
> (Forma), `Fluxo` (Passiva Classe 2), `Aprumo` (Trilha Executor), `Crosta` (Trilha Arremate),
> e mais quatro citações em feitiços prontos.* **Procurado no manual inteiro e nas 19 peças de
> `03-mecanica`: não existe definição em lugar nenhum.**
>
> Quatro perguntas ficam sem resposta, e todas aparecem na primeira mesa que usar `Apoio`:
>
> - **empilha ou substitui**, quando duas fontes dão ao mesmo tempo?
> - **some quando** — fim da cena, descanso curto, descanso longo?
> - **é gasta antes da vida real?** *O `Braseiro` diz isso para energia temporária —* **"gasta
>   como PE, e gasta primeiro"** *—, mas ninguém diz para vida.*
> - **pode passar do máximo de vida?**
>
> *O PHB tem entrada de glossário para isso e remete ao capítulo de dano.* **Aqui o termo
> escapou de toda checagem porque nunca foi escrito entre crases** — a marca que este livro usa
> para dizer "isto é termo do sistema". *A checagem de termo sem destino não alcança palavra
> que não foi marcada.*
>
> **✔ FECHADO na v0.108.** *Decisão do Mizuki, com a conta na mesa:* **gasta antes da vida
> real, não acumula (fica a maior, nunca a soma), teto de metade da vida máxima, e some no fim
> da cena — com o mestre podendo deixar atravessar quando a preparação foi deliberada.**
>
> *A duração curta é o que sustenta o preço:* **o `Apoio` entrega `3` por ponto contra os `4,5`
> que a régua 1:1 pediria, e o desconto de um terço só fecha se a vida temporária for
> desperdiçada com frequência.** Fosse até o descanso longo, ele estaria subvendido em 50%.
>
> **O teto morde, e é de propósito:** *o `Fluxo` (`2` a `14`) nunca é cortado; o `Apoio` puro
> (`9` a `63`) é cortado em toda Classe, inclusive na 1.* ***Decisão do Mizuki:*** *"vai
> existir habilidade que passa e habilidade que não chega perto — é gestão de recurso, a mesma
> escolha de em que altura gastar a cura."*
>
> **Escrito em `03-mecanica/01-atributos-acerto-defesa.md` §5.1.1** — numerada como subseção de
> `5.1 Pontos de vida` **de propósito**: numerar como `5.2` empurraria as quatro seguintes e
> quebraria cinco ponteiros vivos (`19-dano-e-condicoes` §5.2 e §5.5, `18-progressao` §5.3,
> `15-invocacoes` §5.4 duas vezes). *A renumeração chegou a ser feita e foi revertida.*
>
> **E no manual**, capítulo 1, seção `Vida temporária`, mais entrada no vocabulário. *O termo
> passou a ser escrito entre crases — antes ele escapava de toda checagem por não ser marcado.*

> ### A fila, em ordem de quem retoma
>
> **1 · ~~Gatilho e duração nas habilidades~~ — FEITO, e o buraco não existia.**
> *As 74 foram lidas uma a uma, nos cinco Caminhos.* **Uma lacuna real:** o `Aterro` não dizia
> se dependia do `Alicerce` estar de pé — *a fonte respondia (`DESENHO-trilhas.md` classifica
> ele como `permanente`, e o preço de `0,71` fatias foi calculado assim), e a informação se
> perdeu na transposição.* **Corrigido com o texto da fonte, não com decisão nova.**
>
> ⚠ **O `−27` de gatilho e o `−16` de duração eram o mesmo erro de método pela quinta vez.**
> *A conta mediu presença de palavra-chave numa população onde a maioria não precisa do
> elemento:* as sem gatilho são **permanentes** (`Estopim`, `Rebote`, `Ferrolho`,
> `Empunhadura`), as sem duração são **instantâneas** (`Corpo Duro`, `Encontrão`, `Sentinela`,
> `Rompante`), e as de efeito contínuo **dizem** — `Acelerar` traz `2× por cena`, `Ápice` traz
> `1× por cena`, `Segundo Corpo` traz *uma vez por descanso curto*. **O PHB tem mais gatilho
> porque as habilidades dele são mais longas e condicionais, não porque estas estejam
> incompletas.**
>
> **O que a leitura rendeu foi outro achado: `vida temporária` tinha três grafias.**
> *`Aprumo` e `Crosta` diziam "PV temporário"; a Melhoria `Rasga Escudo` dizia "pontos de vida
> temporários".* **As três ficariam fora da regra escrita na v0.108, e ninguém saberia se elas
> têm o mesmo teto e a mesma duração.** *Unificadas.*
>
> **2 · ~~Exemplo inline~~ — FEITO, e o alvo era 13 seções, não 38.**
> *Dez exemplos escritos ao todo:* **capítulo 1** — `Teste`, `Maestria`, `Defesa`,
> `Integridade`; **capítulo 2** — `Limites`; **capítulo 3** — `Rolagem de perícia`;
> **capítulo 4** — `Dano na alma`; **capítulo 9** — `Controle`; **capítulo 10** —
> `Cobrir-se de energia` e `Kokusen`. *Formato: 15 a 24 palavras, dentro da frase, contra a
> mediana de `23` do D&D.*
>
> **O alvo caiu de 38 para 13 ao excluir seção que já tem tabela**, e dos 13 só 3 precisaram de
> texto novo. *O resto já se resolve sozinho, de quatro jeitos que nenhum filtro pega:*
>
> | seção | por que não precisava |
> |---|---|
> | `Passos` | a seção **seguinte** é o *Exemplo guiado: o primeiro feitiço da Régua* |
> | `Rolagem de Bloquear` | o apêndice tem uma seção `## Exemplo` inteira, com a Rina |
> | `Feitiços por nível` | já traz *"São 3 no nível 2, 16 no nível 20 e 24 no nível 30"* |
> | `Coro` | já traz *"Com uma invocação, cada um entrega metade"* |
> | `Técnica Máxima`, `Energia` | tabela com os valores por faixa de nível |
> | `Marco`, `Marcos` | lista de escolhas concretas, não fórmula |
>
> ⚠ **Sexto caso do mesmo erro, e o mais teimoso porque o filtro foi refinado quatro vezes.**
> *Toda versão do filtro presumia um formato de exemplificação e o livro usava outro:* exemplo
> na seção vizinha, exemplo em seção própria de nível `##`, instância concreta sem marcador,
> tabela no lugar de frase. **O livro exemplifica muito mais do que qualquer contagem
> automática consegue enxergar.**
>
> **3 · ~~As seis habilidades com três efeitos~~ — FEITO, e eram três, não seis.**
> *Quatro das seis não tinham três efeitos: tinham **um** efeito com partes.* `Não Acabou` dá
> Reação, movimento e golpe **do mesmo gatilho**; `Puxar a Linha` e `Encalço` são efeito com
> condição; `Acelerar` já traz exemplo próprio. **O contador somava palavras-chave distintas,
> não efeitos independentes — sétimo caso.**
>
> **As que tinham dois efeitos genuinamente separados, colados por um "E", ganharam a segunda
> linha:** `Repuxo` (o empurrão, e o fim da desvantagem por estar colado), `Ferrolho` (a
> recarga, e a mesma desvantagem), e `Alicerce` (o benefício e o custo numa linha, como sair e
> quando se escolhe na outra).
>
> *Não foi preciso formato novo:* **o livro já usa quebra de linha dentro do bloco `>`** — o
> `Corpo Duro` e o `Puxar Para Si` fazem isso desde sempre. *A terceira camada cabe aqui
> porque a quebra existe; foi por não existir que ela falhou na tabela de condições.*
>
> **4 · Herdado da passada de voz — e "quebrar o capítulo 9" não se sustenta.**
>
> ***Medido contra o PHB, a premissa cai:***
>
> | | proporção do livro |
> |---|---:|
> | PHB cap.3, Classes | **36,2%** |
> | PHB cap.7, Magias | **35,6%** |
> | este cap.9, Fundamento | **21,0%** |
>
> **O PHB tem dois capítulos que passam de um terço do livro cada.** *Um capítulo carregar um
> quinto é normal quando ele é o coração do sistema — e o Fundamento é, como Classes e Magias
> são lá.*
>
> **E a estrutura já é a mesma da fonte: regra na frente, catálogo atrás.** *`Melhorias por
> família`, `Restrições`, `Feitiços prontos` e `Fundamentos prontos` somam `5.357` palavras —
> `35%` do capítulo — e são consulta, não leitura.* **Tirando eles, sobram `10.132` palavras de
> leitura corrida, praticamente iguais ao capítulo 7 (`10.213`) e ao 8 (`9.592`).**
>
> *A percepção de "um quinto do livro" estava certa no número e errada na conclusão.*
> **Quebrar por tamanho seria copiar um problema que a fonte não tem.**
>
> **Continuam abertos os outros dois**, e os dois são pequenos: *rebaixar título de exceção
> para negrito correndo* — o `conferir-voz.py` não alcança, é à mão — e *a caixa de aviso
> lateral*, que **pede CSS novo no `build/`** e por isso não é trabalho de texto.
>
> ### Fora do livro
>
> **As três Trilhas do Evocador — `Servo`, `Matilha` e `Coro` — continuam sendo a próxima peça
> de mecânica**, por decisão da v0.103. *Nada nesta passada encostou nelas.* **O dono dessa
> fila é o `sistema/ESTADO-ATUAL.md`, não este documento.**
>
> ### Estado para retomar
>
> **Nada disto foi commitado ainda.** Arquivos tocados: `REGRA-DE-VOZ.md`, `conferir-voz.py`,
> `manual/07-glossario.md`, `manual/12-pericias-e-oficios.md`, `manual/15-dano-e-condicoes.md`,
> `manual/35-caminhos-e-trilhas.md`, `manual/50-equipamento.md` (reordenado inteiro),
> `manual/08-inicio-rapido.md`, `manual/10-como-jogar.md`, `manual/25-origens.md`,
> `manual/15-dano-e-condicoes.md` (as 14 condições reescritas), e este documento.
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

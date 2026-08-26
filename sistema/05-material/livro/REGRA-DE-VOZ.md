# Regra de voz · Manual da Guilda

O manual é documento de sistema. Alguém abre ele no meio de uma sessão, procura uma coisa,
acha, e volta pro jogo. Tudo aqui sai disso.

O `conferir-voz.py` confere as partes mecânicas desta régua. As que ele não alcança estão
marcadas com **(à mão)**.

---

## Mede contra o PHB e o GURPS antes de mudar, e não copia nenhum dos dois

Os dois manuais completos ficam fora do repositório, na pasta de PDFs do Mizuki, e o
`pdftotext` extrai os dois em segundos. **Antes de mudar estrutura, formato ou ordem, veja como cada um resolve o mesmo
problema** — mas a decisão sai da comparação, nunca da imitação.

*Isto rendeu resultados opostos duas vezes na mesma passada, e é por isso que a regra é
medir e não copiar:*

> **O PHB tinha a solução, e ela entrou.** O rótulo de família entre colchetes — `Cone [Área
> de Efeito]` — resolve termo cujo nome sozinho confunde, e ele só usa em 41 das cerca de 760
> entradas do Glossário de Regras. Virou o `[Nível]` do `Leve`, `Média` e `Pesada`.
>
> **O PHB tinha a solução, e ela foi rejeitada.** Ele divide o catálogo de armas em
> `simples/marcial × corpo a corpo/distância` **porque lá a proficiência é por arma**. Aqui o
> treino mora na categoria, e são três listas. Copiar teria quebrado o vínculo entre categoria
> e treino, que é regra. *A divisão saiu por lista de treino.*

**Meça, não folheie.** O que decidiu as duas foi contar — 41 entradas rotuladas de 760, e 52
armas em 13 categorias com 3 listas de treino. Impressão de leitura não separa o caso em que
o modelo serve do caso em que ele mente.

### ⚠ Isto tudo é metodologia, e não lei — o próprio PHB não obedece

**Nenhum livro de sistema segue uma forma única, e medir o PHB mostra isso.** A consistência
dele é **dentro de cada família de coisa**, e cada família tem a sua:

| família | quantas seguem a forma da família | como a forma abre |
|---|---:|---|
| `[Área de Efeito]` | 100% | *"Um Cone **é** uma área que…"* — definição |
| `[Risco]` | 100% | *"Uma criatura **pode**…"* — descrição |
| `[Condição]` | 86% | *"**Enquanto** tem a condição X…"* — âncora de tempo |
| `[Ação]` | 55% | *"**Quando** executa a ação X…"* |

**Não existe "a forma do PHB".** Existe a forma da condição, a forma da ação, a forma da área
— e o mesmo documento carrega todas ao mesmo tempo. *Copiar uma delas para onde ela não
pertence é o erro que a comparação com o modelo mais convida a cometer.*

> **A pergunta certa não é "qual é o padrão", é "de que família é esta coisa, e qual forma as
> irmãs dela já usam".** Forma nova só quando a família é nova.

### As quatro camadas, e elas são OBRIGATÓRIAS em toda entrada de catálogo

*Elas nasceram como "a forma da família condição" e ficaram presas ali por doze versões.* **Decisão do Mizuki na v0.141: entrada de catálogo se escreve nesta forma, e não é escolha de quem está escrevendo.** *Vale para condição, Bênção, aptidão, Passiva, `Estigma`, Legado, entrega de Trilha — qualquer coisa que o leitor procura pelo nome e lê sozinha.*

**O que ela substitui é o parágrafo-parede**, e ele tem sintoma: *a entrada abre com metáfora em vez de dizer quando a regra vale, e depois empilha três regras diferentes sem dar nome a nenhuma.* **Foi assim que o `Bocado` passou da v0.122 à v0.141** — *"o que você carrega passa a viver dentro de você. Sacar é tirar de si"* —, e a regra que o jogador usa toda rodada, o saque a mais, estava no terceiro parágrafo.

> **O teste é de leitura, não de medida, e ele é curto:** *dá para achar a regra que você quer sem ler a entrada inteira?* **Se a resposta depende de ler tudo, os nomes de efeito estão faltando.**

#### A forma, medida no PHB

Não é o "por exemplo" que segura o leitor — o PHB usa pouco, e o `Exemplo:` em bloco ele não
usa **nenhuma vez** em 397 páginas. Nas condições ele monta assim, do geral ao específico:

| camada | o que ela faz | tamanho medido |
|---|---|---|
| `Termo [Tipo]` | diz **de que espécie** é a coisa | 1 a 3 palavras |
| frase de âncora | diz **quando** a regra vale, e nunca o que ela faz | mediana `14` palavras |
| nome do efeito | dá **nome próprio a cada efeito**, em negrito correndo | 4 a 6 palavras |
| a regra | o efeito em si | 15 a 21 palavras |

*Medido nas 450 entradas do Glossário de Regras: 88% das frases de âncora cabem em 20
palavras.* **As catorze condições deste livro foram reescritas nessa forma na v0.108.**

> ⚠ **A terceira camada depende de quebra de parágrafo.** O rótulo em negrito fecha o nome de
> um bloco que **já está isolado na página** — não é ele que separa os efeitos. *Enfiado numa
> célula de tabela, ou no meio de uma frase corrida, o ponto vira vírgula decorativa e o
> leitor não entende que a explicação vem em seguida.* **Foi assim que a primeira tentativa de
> aplicar isto falhou, e é o mesmo defeito que travou uma leitora no `colado`.**
>
> **Onde não há parágrafo, não use esta forma.** A tabela `Condições em uma linha` existe para
> esse caso: consulta rápida, uma linha, sem camadas.

#### O rótulo longo demais TEM CONTAGEM, e ela levou três versões para ter dono

*A v0.141 mediu **nove entradas com doze rótulos**, seis delas no capítulo 12, e publicou o par sem escrever a definição.* **Sem definição escrita, duas versões seguidas tentaram remedir e acharam outra coisa:** *a v0.149 contou o fenômeno errado e foi descartada; a v0.152 achou `209` com um regex que pega toda caixa de regra do livro, parou, e com um recorte próprio chegou a `4`.*

> **O livro carrega `0` rótulos longos demais, em `52` entradas de catálogo.** *Os dois números são o dono, e o `conferir-voz.py` reconta e falha nos dois sentidos.*

**A v0.153 fechou a diferença reconstruindo a definição, em vez de escolher entre os números.** *O par da v0.141 reproduz **exato** — `9` entradas, `12` rótulos, `6` delas no capítulo 12 — se a entrada se qualifica por ter rótulo longo **dentro da caixa de regra** e os rótulos são contados **na seção inteira** dela.* **Ela mede uma metade do par por um recorte e a outra por outro, e é isso que a torna irreproduzível para quem tente adivinhar depois.** *Endireitada — toda entrada, rótulo na seção inteira —, o mesmo texto dá `11` entradas e `14` rótulos, ainda com `6` entradas no capítulo 12.*

*E a v0.138, medida pelas duas, dá o mesmo:* **nada foi consertado de passagem na v0.147 nem na v0.148.**

**A definição publicada é a endireitada:**

| | |
|---|---|
| **entrada de catálogo** | seção-folha `###` ou `####` cujo nome está publicado numa **tabela do próprio capítulo**, e que abre pela camada 1 — `**<o nome dela>** — âncora` dentro da caixa de regra, ou uma âncora em prosa que a nomeia |
| **rótulo longo demais** | negrito **abrindo parágrafo**, com mais de `6` palavras, na seção daquela entrada |

**A lista das entradas não mora no validador: ela mora na tabela que o livro publica** — a `Como ler uma Bênção`, a `Condições em uma linha`, a `Como ler uma aptidão`. *Renomeie uma entrada e a checagem para de achar ela, então a contagem de `52` é guarda: ela falha se subir e se descer.*

**O que NÃO conta, e a fronteira é escrita para não virar discussão:**

- **Caixa de regra fora de entrada.** *O livro tem `253` delas, e o regex que as pega devolve mais de duzentos.* **A camada 3 só vale para entrada de catálogo** — seção de regra escreve como quiser.
- **Rótulo dentro de célula de tabela.** *A própria régua já diz isso acima: sem quebra de parágrafo, o negrito não é camada 3.*
- **`Estigma`, Legado e entrega de Trilha.** *As três famílias se escrevem em **uma linha** dentro de caixa compartilhada — `**`Fiel`** — ela volta para a sua mão`.* **Onde não há parágrafo, a camada 3 não se aplica**, e a obrigação das quatro camadas alcança elas no dia em que virarem seção.

> ***A lição que as três versões custaram:*** *o par "entradas, rótulos" tem uma metade estável e uma instável.* **Os rótulos batem em todo recorte razoável; as entradas mudam de número conforme o que você chama de entrada** — `4`, `6`, `7`, `9`, `32` ou `95`, pela mesma frase lida de seis jeitos. *Por isso a definição vem antes do número, e não depois.*

### As marcas de "isto ainda não existe", e elas TÊM CONTAGEM

*Escrito na v0.144, e ele nasceu de uma contagem que deu errado cinco vezes seguidas.* **O prompt de retomada dizia quatro, o CHANGELOG da v0.136 dizia cinco, a varredura à mão de uma versão disse oito, e o regex acha sete.** *Toda contagem desta família até hoje deu um número diferente, e nenhuma delas tinha validador.*

> **O livro carrega `6` marcas de regra que ainda não existe.** *Esse número é o dono, e o `conferir-voz.py` recontá e falha se ele subir.*

> **Era `7` até a v0.163**, quando a marca do capítulo 15 fechou — *"quando a vida cheia volta ainda está sendo decidido"*. **O validador acusou a queda no mesmo commit em que ela aconteceu**, com as duas leituras na mesma frase: *"ou entrou marca nova, ou uma foi fechada e o número não desceu junto"*. *Ele falha nas duas direções de propósito, e é por isso que fechar uma marca custa uma linha aqui.*

**O que conta como marca, e são três formas:**

| forma | o sintoma |
|---|---|
| **está sendo escrito** | a frase diz que a regra está em produção |
| **pergunte ao mestre** | a frase manda combinar com o mestre, ou diz que é acordo com ele |
| **não tem regra** | a frase diz, com todas as letras, que a regra não existe |

**O que NÃO conta, e a fronteira é escrita para não virar discussão:**

- **A vaga declarada.** *O `Nível 27: vaga` do `Arremate` diz que a casa existe, está vazia e qual é a ficção dela.* **Isso é conteúdo, e não buraco:** o leitor sabe o que tem ali e o que não tem.
- **A variante de mesa.** *"Se a sua mesa preferir, sintonizar pode custar um descanso longo"* **tem padrão escrito e o efeito da variação publicado ao lado.** *A mesa escolhe entre duas coisas que existem — ela não está preenchendo um vazio.*
- **O que mora nas peças e não no livro.** *A vaga reservada do `Desliga` na peça 13, por exemplo.* **Esta contagem é do livro**, porque é o livro que o jogador lê.

***A decisão da v0.129 continua valendo por cima disto:*** *quando a frase de estado carrega uma permissão ou um limite que o jogador precisa, ela fica.* **O que a contagem faz não é mandar cortar — é impedir que uma marca nova entre sem ninguém ver.**

### Rótulo de categoria no ponto de uso

O PHB responde *"que espécie de coisa é essa?"* dentro do texto corrido, entre parênteses, e
faz isso o tempo todo: **58% dos 2.889 parênteses dele são rótulo** — `(magia)`, `(talento)`,
`(perícia)`, `(característica de classe)`.

**Aqui a crase diz que a palavra é termo do sistema, e não diz de que tipo.** É a metade que
falta, e é a que fez uma leitora travar no `colado`.

**Mas ele rotula pouco, e é de propósito: só `40` das `767` entradas do Glossário de Regras
levam rótulo — 5%.** *O rótulo é reservado ao nome que sozinho confunde;* `Cone` precisa
porque cone também é forma de área e palavra comum, `Bardo` não precisa porque ninguém erra.

**O critério é a dúvida, não a posição:** rotule quando o leitor não teria como saber de que
espécie é a coisa — e só a primeira vez em cada capítulo, para quem abre o livro no meio.
*Onde a frase já diz o tipo em português — "a **Restrição** `Carregar`", "a **Trilha**
`Sutura`" —, o rótulo sobra.* **(à mão)**

*Na v0.108 isso deu 5 rótulos escritos de 34 candidatos: 29 caíram porque o livro já se
anunciava sozinho.*

---

## O livro não fala de si mesmo

O teste é a pergunta que a frase responde:

| a frase responde… | destino |
|---|---|
| **onde está?** | fica — *"a regra está no capítulo 6"* |
| **por que o livro é assim?** | sai — *"este capítulo é para ler inteiro"* |

O jogador não precisa saber que o manual usa `Refino` 146 vezes, nem que o capítulo dono
fica na metade. Isso era diagnóstico de revisão e virou texto por engano.

A moldura de leitura vive **uma vez**, na introdução, na seção *Organização do manual*.
Dentro do capítulo, nunca.

### Por que o mundo é assim fica; por que o livro é assim sai

As mesmas palavras servem às duas coisas, e é por isso que o validador não decide sozinho:

> *"Ela escapa do corpo de quem produz, o tempo todo, **e é por isso** que um feiticeiro
> fareja outro a um quarteirão."* → fica. É causa dentro da ficção.
>
> *"Ela não depende da sua técnica, **e é por isso** que mora fora do Fundamento."* → sai.
> É explicação de por que o capítulo está montado daquele jeito.

O `conferir-voz.py` lista os candidatos como `TRIAR` e não conta como achado. Marcadores
que ele procura: *vale reparar*, *repare que*, *de propósito*, *e é por isso*, *na prática*,
*isso quer dizer*, *é a aposta*, *o que importa*, *não à toa*.

### Antes de cortar, veja se a frase é a única dona de um fato

Comentário de efeito às vezes carrega uma regra que não está escrita em mais lugar nenhum.
Cortar direto apaga a regra junto.

O caso que criou esta linha: *"enquanto o gatilho não vem, ninguém sai andando na sua
frente de graça"*, no fim do capítulo 2. Parecia enfeite, e era — mas era o único lugar do
manual que dizia que a Reação **não fica reservada** enquanto uma ação preparada espera. A
frase saiu; a regra foi escrita com todas as letras dentro de *Preparar*.

Ponteiro é curto e sempre na mesma forma: *"veja o capítulo 9, Fundamento"*. Não explica
por que o ponteiro existe.

## Na dúvida, corta

Se eu parei pra decidir se uma frase acrescenta, ela já está condenada. Quem lê uma vez,
na mesa, não vai ter a chance que eu tive de olhar duas vezes.

A exceção é uma só: se cortar apaga um número, uma exceção, ou um caso que nenhuma outra
linha cobre. Aí não é dúvida de estilo, é perda de regra — e aí pergunta.

## Título é o nome da coisa

Serve de entrada de índice remissivo, ou não é título.

- **Sem artigo.** `Linha da ficha`, não `A linha da ficha`. No PHB 2024, 1,3% dos títulos
  começam com artigo; aqui eram 28%.
- **Sem pergunta.** `Testes de Resistência`, não `O que você rola`.
- **Sem frase.** `Aparar e crítico`, não `O Aparar não come crítico`.
- **Sem contagem.** `Perícias`, não `As vinte e três perícias` — entra uma perícia nova e o
  título mente. O número vive na primeira linha do corpo, onde é barato de corrigir.
- **Caixa de sentença**, não Title Case. O `Modificador compartilhado` do D&D-PT é herança
  do inglês e não é convenção em português.

Título de capítulo (`#`) fica fora de tudo isso: 41 referências cruzadas apontam pra ele
pelo nome.

### Quando o nome não é seção — rebaixa

Caso específico e exceção não precisam de título próprio. Viram negrito correndo dentro do
parágrafo, como o PHB faz: **`Dano maciço.`** e o texto segue na mesma linha. Não entra no
sumário, não quebra página, e o degrau `####` deixa de proliferar. **(à mão)**

## Todo termo tem um destino

Termo entre crases é promessa: o leitor entende que aquilo é nome de coisa do sistema, e
sai procurando onde a coisa é explicada. Se não achar, ele para de confiar na crase — e aí
para de procurar até quando teria achado.

Uma leitora do playtest travou em `colado`, no capítulo de equipamento. A definição estava
na mesma frase, seis palavras depois. Ela não leu como definição porque **nada ali dizia
que era uma**: o termo vinha marcado, e texto marcado no livro inteiro significa *isso é
explicado em outro lugar*. Ela fez o certo com um livro que estava errado.

**O que a estreia precisa ter é uma marca de que ali está a definição.** A forma varia com a
família, e o livro já tem quatro que funcionam — todas reconhecidas pelo `conferir-voz.py`:

| forma | onde ela é a certa |
|---|---|
| `### Termo` | a coisa é grande o bastante para ter seção |
| `**`Termo`** — texto` | estreia dentro de prosa |
| `> **Nível N: `Termo`.** …` | habilidade de Trilha ou Caminho — 74 usos |
| linha do vocabulário | termo que vive numa tabela |

*O travessão é a marca da segunda: ele diz **estou definindo isto agora**.* **Não confundir
com o negrito de rebaixar título** — **`Dano maciço.`** com ponto abre um bloco sobre coisa
já conhecida; com travessão, apresenta coisa nova.

> **Forma nova exige motivo.** Se nenhuma das quatro serve, a família é nova — e aí a forma
> entra aqui e no validador junto, não só no texto.

**E todo termo que o livro usa de verdade tem entrada no vocabulário.** O corte é `5` usos,
ou aparecer em `3` capítulos — abaixo disso o termo é local e a estreia no lugar basta.

O `conferir-voz.py` conta os que ficaram sem destino e falha se o número subir. Ele não
exige que o buraco feche de uma vez; exige que ele não cresça.

*O que fica de fora:* nome próprio de item de catálogo — arma, feitiço pronto, Trilha — que
já vive numa tabela com a coluna que o explica. O destino dele é o catálogo, e o índice A–Z
do capítulo é o que leva até lá.

## Os encaixes

Mesma pergunta, mesmo nome, no livro inteiro. O leitor aprende uma vez e reconhece em
qualquer capítulo. É o que o capítulo de Origens já fazia sozinho, com `O que muda`,
`Traços`, `Criação`, `Destranca`, `Ajusta`, `Desliga`.

| encaixe | o que responde |
|---|---|
| `Como ler` | como se lê uma entrada ou tabela deste capítulo |
| `Características de <X>` | o que a coisa concede |
| `Limites` | o que ela não faz, e o que trava ela |
| `Custo` | o que ela cobra |
| `Duração` | quanto tempo dura, e o que a encerra |
| `Alcance` | distância |
| `Teto` | o valor máximo |
| `Catálogo` | a lista longa, para consulta |
| `Exemplo` | a conta inteira, com nome próprio |

`Características` foi conferido: não aparece nenhuma vez no manual hoje, então não colide.
`Traço` já era usado, e por acaso já batia com o D&D.

## Toda tabela tem nome

211 das 212 tabelas do livro não tinham. Sem nome, o texto só consegue apontar por posição
— *"a tabela acima"* —, e isso passa a mentir quando o PDF quebra a página noutro lugar.

Convenção do PHB, que serve aqui: **`<Tipo> de <Nome>`**. *Resultados de Bloquear*,
*Características do Bastião*.

```markdown
**Resultados de Bloquear**
{: .tab-titulo }

| o que acontece | chance |
|---|---|
```

A linha `{: .tab-titulo }` tem que ficar sozinha — na mesma linha do negrito, o
`attr_list` gruda a classe no `<strong>` e a margem não funciona.

Os três builds já entendem: o `build.py` sempre entendeu, o `build_docx.py` ganhou a
extensão, e o `build_txt.py` apaga a linha por regex.

No corpo, chama pelo nome: *"veja a tabela `Resultados de Bloquear`"*.

## O que nunca muda numa passada de texto

Nenhum número de regra. A cada arquivo, antes de aplicar:

```bash
python3 build/guard_numeros.py manual/<antes>.md manual/<depois>.md
```

Ele conta toda notação de dado, porcentagem, inteiro e numeral por extenso dos dois lados e
mostra a diferença. Diferença não é proibida — título perde um `As duas`, prosa cortada
perde um `dois` —, mas **cada uma tem que ser explicada** antes de aplicar. Foi assim que o
piloto passou.

## Fora do alcance do validador

- Rebaixar título pra negrito correndo
- Decidir se uma frase é fato mal-vestido ou enfeite
- Nome de tabela que está lá mas está ruim
- Caixa de aviso lateral, que ainda não existe no CSS

Retomando o **Projeto - M** (sistema de mesa de Jujutsu Kaisen), em
`/media/mizuki/HD Externo II/Claude/Claude 2/`.

## Os dois repositórios

| | |
|---|---|
| **o projeto** — tudo | https://github.com/cupcake-mochi/JJK---Project.git |
| **a entrega do PDF** | https://github.com/cupcake-mochi/JJK---PDF---RPG.git |

**A entrega mora em `finalizado/`, tem git próprio, e precisa do commit dela depois do commit do projeto.** *Ela é recorte e artefato: regerada quando uma versão fecha, e nunca editada a mão.* **O `conferir-repositorio.py` compara o recorte contra a fonte por md5 (checagem 7.1) e lê o git dela (checagem 7.4)** — se você mexer numa peça que está no recorte, copie a peça para `finalizado/regra/` antes de fechar, senão o validador acusa.

> **Se o repositório for lido por um Project do Claude, sincronize depois do push.** *Pular isso é o jeito mais fácil de acabar com duas versões: o Project continua lendo o commit anterior e passa a discutir regra que já mudou.*

---

Leia `README.md` — em especial *"Nove lições que custaram erro"* —, `sistema/ESTADO-ATUAL.md` **inteiro**, e `logs/CHANGELOG.md` de cima. As entradas **v0.129 e v0.130** são o que esta tarefa herda: as duas foram passada de texto no livro, e a v0.130 fechou seis pendências pequenas de uma vez.

Projeto na **v0.130**, **20 peças**, **21 validadores**, **204 checagens**, tudo verde. Livro em **76.664 palavras**, 20 arquivos, 248 páginas em coluna única e 141 em duas colunas.

## Esta conversa é de MECÂNICA, e a ordem é minha

Cinco itens, **nesta ordem**, e ela não é por tamanho:

| # | item | onde ele mora hoje |
|---|---|---|
| 1 | **Torrente** contra a regra de ouro nº 6 | peça 6 §9, e a Trilha no `DESENHO-trilhas.md` |
| 2 | **Objeto amaldiçoado** | não tem peça. A peça 16 §9 declara que é outra coisa |
| 3 | **Pactos** | peça 8, Passo 8 |
| 4 | **Itens menores** | peça 14 §8, régua de três camadas com a terceira desligada |
| 5 | **Trilhas do Evocador** | `RASCUNHO-trilhas.md`, e é a última de propósito |

**Não pule para a 5.** Ela é a maior e a que mais gente espera, e é justamente por isso que ela vem depois — as quatro de cima são menores e destravam vaga que ela não destrava.

### ⚠ Pare no fim de CADA item e me avise. Não emende sozinho.

**Quando um item fechar** — regra escrita na peça, validador com arnês rodado, documentos atualizados e mensagem de commit pronta —, **pare ali e me diga:**

- **o que fechou**, com o que a medida deu;
- **o que ficou aberto** dentro daquele item, se ficou;
- **quanto do seu contexto já foi**, na sua estimativa;
- **se você recomenda seguir para o próximo aqui ou abrir conversa nova.**

**Quem decide sou eu, mas a recomendação é sua e eu quero ela.**

> **O motivo é medido, e ele custou erro na v0.130.** *Aquela conversa fez três passadas de texto no livro inteiro, uma peça nova com validador, e seis pendências — e ficou longa demais.* **Perto do fim, com o contexto já resumido, ela cometeu os dois únicos erros de método da versão:** *um `grep -A9` que atravessava de uma seção do `guard_numeros` para a outra, e uma medida de estilo enviesada que dava `38,6` quando o número certo era `7,1`.* **Nos dois casos ela imprimiu a conclusão antes de ter provado**, e nos dois quem pegou foi ela mesma, conferindo de novo.
>
> **A perda de contexto não avisa.** *O que ela apaga primeiro é justamente o que este projeto pune: qual validador rodou, o que a perturbação acendeu, qual número tinha qual dono.*

**Corte sugerido, se você não tiver opinião melhor:** *a `Torrente` e o objeto amaldiçoado numa conversa; Pactos e itens menores noutra;* **e as Trilhas do Evocador numa só, inteira** — são doze entregas preçadas contra orçamento, e o `RASCUNHO-trilhas.md` avisa que a escala vai de 30 a 120 entradas.

*Este prompt funciona igual nas três: ele diz a ordem, e cada item leva onde mora e o que já está fechado dele.*

---

### 1 · Torrente

**O problema, escrito na peça 6 §9:** *"Como Torrente cobra o segundo feitiço da rodada. É o mesmo defeito da seção 4 — mais de uma ação por rodada —, e o conserto que funcionou lá provavelmente serve aqui: os feitiços que você lança numa rodada, somados, entregam uma Rotina."*

**O que a Trilha entrega hoje**, no capítulo 8 do livro:

- **Nível 2 · `Acelerar`** — `2×` por cena, conjura o feitiço da Ação Padrão como Ação Bônus, pagando `Classe e meia` de PE a mais. Naquele turno o outro feitiço não passa de `Classe 0`.
- **Nível 11 · `Vazão`** — aquele teto vira metade da maior Classe, arredondando para baixo.
- **Nível 27 · `Transbordo`** — aquela metade passa a arredondar **para cima**. É a única exceção à regra global de arredondamento em todo o sistema.

> **⚠ Este é o único dos cinco cujo tamanho eu não consigo prever, e é por isso que ele vem primeiro.** *Ele pode terminar num repreço, e repreço reabre a conta de fatia — que é a v0.73 inteira.* **Meça antes de propor**, e se a conta apontar para mexer no orçamento de Trilha, **pare e pergunte**.

*O conserto de invocação que a peça 6 §4 cita está na peça 15: você e todas as suas invocações somados entregam **uma** Rotina.*

---

### 2 · Objeto amaldiçoado

**Ele não é ferramenta amaldiçoada, e a fonte é explícita:** *"tirando as ferramentas amaldiçoadas e os cadáveres amaldiçoados, todo item que contém energia amaldiçoada é chamado de objeto amaldiçoado"*. **Ferramenta você empunha e ela fere maldição; objeto é a maldição presa numa forma de objeto, e o que está dentro dele age.**

**Duas Origens inteiras são construídas em cima dele** — Receptáculo é comer um dedo, Reencarnado é ter virado um. *O cubo que prendeu o Gojo é objeto, não ferramenta.*

**O que ele destrava:** uma vaga de `Desliga` na peça 13, a do Reencarnado. *A conta o pôs por último na fila antiga justamente porque ele fecha uma vaga e mais nada.*

> **⚠ E tem uma peça velha esperando você.** *A peça 13, na tabela de `Desliga` do **Corpo Amaldiçoado**, ainda diz que a vaga "espera a peça de Técnica Marcial" — e a Técnica Marcial fechou na v0.122, é a peça 20.* **O livro já foi corrigido na v0.124 e diz "alvo ainda não escolhido"; a peça não.** *A peça está velha onde o livro está certo, que é a direção contrária da usual.* **Conserte de passagem, e confira se a nota logo abaixo, que cita a peça 9 dizendo "Técnica Marcial — não existe ainda", não está velha junto.**

---

### 3 · Pactos

**O recorte encolheu para um quarto na v0.116, e isso é a melhor notícia da fila.** *Três das quatro formas já têm dono:*

| o que o jogador quer dizer | onde já se escreve |
|---|---|
| *"a minha técnica fica maior sob uma condição"* | **Restrição**, por feitiço, no manual |
| *"a minha técnica impõe uma regra ao mundo"* | **`Regra Própria`**, por técnica, no manual |
| *"eu troquei uma coisa antes da campanha"* | **Legado**, peça 13 |
| *"eu e mais alguém fechamos um trato, aqui, na mesa"* | **não tem regra** |

**Só a quarta falta**, e ela é a que atravessa mesas — por isso a mais perigosa. **As quatro travas de projeto que qualquer régua futura tem de obedecer já estão escritas na peça 8, Passo 8.** Leia elas antes de propor.

> **⚠ E a trava que estava escrita ali era cópia.** *Os cinco requisitos — "uma frase, verificável, simétrica, sem dano direto, com limite" — são a lista da `Regra Própria` do manual, na ordem, e já tinham divergido em uma palavra.* **A peça 8 passou a apontar em vez de repetir. Não desfaça isso.**

---

### 4 · Itens menores

***Levantado por mim na v0.131.*** **Consumível e afins: o que se compra, se gasta e acaba.** *Talismã pronto, remédio, corda, lanterna, o kit que o ofício `Herbalismo` usa.*

**A peça 14 §8 item 10 já registra:** *"A lista de itens comuns. A régua das três camadas fechou; os itens não. Quantos, quais e como se chamam é escolha de sabor."*

**A régua existe e a terceira camada está desligada.** *Leia ela antes de inventar camada nova.*

> **Escolha de sabor é minha.** *Quantos itens, quais, como se chamam, em que ordem aparecem.* **Traga as opções com o número e o trade-off de cada uma já calculados, em rodadas curtas.**

---

### 5 · Trilhas do Evocador

**`Servo`, `Matilha` e `Coro`.** *Doze entregas de nível — 2, 11, 19 e 27 em cada uma —, e elas fecham as quinze Trilhas.* **Nada mais as trava.**

**O que já está fechado delas** é o ponto de partida da invocação, na tabela do capítulo 8: o `Servo` leva `5 × h` de vida e o orçamento da ficha mais metade; a `Matilha` leva cinco corpos em pool com cascata; o `Coro` ataca e comanda na mesma rodada.

**A máquina inteira de invocação é a peça 15**, com o `conferir-invocacoes.py` e trinta checagens em cima dela.

> **⚠ Duas regras ficaram penduradas na peça 15 e nenhuma entrega de Trilha que mexa nelas tem contra o que ser medida:** *quando a vida cheia da invocação reinvocada volta, e o que acontece com a invocação quando o **dono** cai.* **Feche as duas antes de preçar entrega.**
>
> **⚠ E o risco desta peça é escala:** *quinze Trilhas × quantas entregas dá de 30 a 120 entradas.* **A única recomendação de método que o `RASCUNHO-trilhas.md` faz é: a régua vem antes do catálogo.** *Foi ela que fez a peça 13 fechar em uma versão contra as seis que a peça 14 gastou.*

**Quando elas entrarem, o total de 89 entradas da peça 17 muda e a checagem 1 do `conferir-catalogo.py` acusa.**

---

## Método, e ele não é negociável

- **Rode os validadores antes de mexer em número:** os 20 de `sistema/03-mecanica/`, o `conferir-repositorio.py` da raiz, os dois de `manual/matematica/`, e o `conferir-voz.py --estrito` do livro.
- **Meça o sucesso pelo CÓDIGO DE SAÍDA, nunca casando texto da saída.** *Os validadores reprovam em dois formatos — `>>> N PROBLEMA(S)` e `>>> FALHOU` — e um laço que procura só o primeiro sai verde sem ter conferido.*
- **Confira `PULADA = 0`.** *Sem `python-docx` cinco validadores pulam em vez de falhar.*
- **Todo número novo ganha validador com teste negativo**, em cópia isolada: confira que a base passa antes, que o `diff` entrou, e ponha **contra-teste** — perturbe uma coisa que a checagem NÃO deveria pegar e prove que ela sai verde.
- **Nada de valor fica escrito dentro do validador.** *Leia do documento dono.* **A v0.130 achou a lista de Origem morando dentro do `conferir-pericias.py`, com a mensagem de erro dizendo "e a peca 09 diz quatro" — ele afirmava a regra da peça e guardava o próprio dado.**
- **Cada peça tem um validador dono.** *Checagem nova vai no validador da peça que ela confere, não num arquivo novo — `conferir-*.py` novo quebra a contagem até os três documentos subirem juntos.*
- **Se mexer no livro, `guard_numeros.py antes.md depois.md` a cada arquivo**, e **recorte a seção `NOTAÇÃO E NÚMERO` separado** da de numeral por extenso: um `grep -A9` atravessa de uma para a outra e faz você imprimir "zero diferença" antes de ter provado.
- **Escolha de sabor é minha**, em rodadas curtas, nunca proposta grande pronta.
- **Documento não pode ter cara de saída de IA.** Português informal, nunca de Portugal.
- **Você não commita.** Deixa a mensagem em `mensagem-de-commit.txt` na raiz e em `finalizado/mensagem-de-commit.txt`, e avisa; eu rodo `jjk && ./subir.sh`.

### Duas armadilhas medidas nas últimas versões

> **⚠ Medir o marcador em vez do fenômeno.** *Aconteceu **dez** vezes neste projeto.* **Na v0.130 a medida de "frase de efeito" deu `38,6` e estava torta**, porque o regex pegava uma forma e não a irmã dela. **Quando duas medidas discordarem, vá olhar — não escolha a que te convém.**
>
> **⚠ Decisão registrada não é decisão desregistrada.** *A v0.130 achou o problema de design nº 3 pedindo uma tabela que **já existia** na peça 7 §5, e a peça 13 apontando para uma peça que fechou oito versões antes.* **Antes de trabalhar num item da fila, confira se ele ainda existe.**

## Onde as coisas moram

| | |
|---|---|
| as peças de regra | `sistema/03-mecanica/`, 20 peças e 20 validadores |
| o catálogo de entregas | peça 17, e os três `DESENHO-*.md` da raiz são os donos do preço |
| a fonte do livro | `sistema/05-material/livro/manual/*.md`, 20 arquivos |
| a régua de escrita do livro | `sistema/05-material/livro/REGRA-DE-VOZ.md` |
| o validador do livro | `conferir-voz.py` — **rode com `--estrito`** |
| como regerar o livro | `sistema/05-material/livro/README.md` — são **dois** builds, e os dois se regeram |

**Os dois repositórios estão no topo deste arquivo**, com o que a entrega cobra antes de fechar versão.

## O que NÃO é desta tarefa

**A diagramação está decidida: as duas ficam**, e o `--duas` continua sendo opção do `build.py`. *Não é pendência.*

**O `PvP` vai para o livro do mestre**, decidido na v0.130. **A perícia livre da Origem fica livre**, decidido na v0.130. **A lista de perícia do Corpo Amaldiçoado está escrita** desde a v0.129.

**E o livro acabou de passar por três passadas de texto.** *Se você achar frase de efeito nele, aponte e siga* — **reescrever o livro não é esta tarefa.**

> **O que faz falta de verdade não está nesta lista: `04-playtest/` continua vazia, zero sessões desde a v0.1, e todo número do sistema é previsão.** *A v0.130 recebeu o primeiro retorno de leitura externa — jogadores lendo o capítulo das Bênçãos — e ele achou cinco coisas reais que três passadas minhas não tinham achado.*

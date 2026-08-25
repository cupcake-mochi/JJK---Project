# Retomada — v0.153, e o que sobrou é preço, playtest e dois rascunhos

Pasta: `/media/mizuki/HD Externo II/Claude/Claude 2/`
⚠ Trabalhe na pasta PRINCIPAL, não em worktree. **Você não commita** — deixa a mensagem em
`mensagem-de-commit.txt` e avisa. *A entrega, desde a v0.149, o `subir.sh` copia sozinho.*

Leia primeiro, nesta ordem: `README.md` (a seção *"Nove lições que custaram erro"*),
`sistema/ESTADO-ATUAL.md` **inteiro**, e o `logs/CHANGELOG.md` de cima até a v0.140.

**Projeto na v0.153.** 24 peças · 24 validadores · **255 checagens**. Livro em 17 capítulos,
**70.982 palavras**, **243** páginas em coluna única e **141** em duas. Manual do Fundamento na
**v7.14**. `conferir-voz --estrito` em 0 achados, 0 termos sem destino, 11 triagens, **7 marcas
de "isto ainda não existe" e 0 rótulos longos demais em 52 entradas de catálogo**.

> **Os quatro builds rodaram na v0.153, e a checagem 7.5 está verde.** *Antes de eles valerem,
> o controle da v0.151 foi rodado de novo:* **reconstruindo a partir da fonte de antes das
> edições, a coluna única saiu com `243` páginas e `3.034.652` bytes contra `3.034.648` do build
> anterior** — *quatro bytes, e eles são o carimbo de data do PDF.*

---

## O que as últimas versões fecharam

**A v0.153 fechou a dívida de texto do livro — o item 5 da fila anterior — e ela custou mais
arqueologia do que conserto.** *O par "nove entradas, doze rótulos" era da v0.141 e nunca teve
definição escrita; a v0.149 remediu e foi descartada, e a v0.152 achou `209` e parou.*

**A v0.152 pagou a dívida de preço dos `Estigma`, e ela encolheu antes de fechar** — o corte é
dentro do degrau, e o `Bojo` foi arrancado.

**A v0.151 consertou duas linhas que ele leu e estranhou** — o `Incapacitado` foi de `11,00`
para `4,95` derivado, e o `Cerca` ganhou o portão do `Santuário`.

**A v0.150 tirou a descida de grau do `Desgaste`.** **A v0.149 pôs a cópia da entrega no
`subir.sh`.** **A v0.148 foi a sétima passada de texto, com dezoito achados e nenhum de
validador.** **A v0.147 foi cinco achados dele lendo o PDF, e um reverteu a v0.82.**

---

## ⚠⚠ A lição que a v0.153 acrescentou, e ela é sobre CONTAGEM

**Um número publicado sem a definição escrita ao lado não é medida — é lembrança**, e ele não
sobrevive a quem for reler. *O par da v0.141 atravessou doze versões, três tentativas de
remedição e três resultados diferentes.*

> **E quando ele foi reconstruído, o defeito apareceu: a definição era TORTA.** *A entrada se
> qualificava por um recorte — rótulo dentro da caixa de regra — e os rótulos eram contados por
> outro, a seção inteira.* **Duas metades do mesmo par medidas de jeitos diferentes.** *Com
> isso ela reproduz exato (`9 · 12 · 6`) e não reproduz por nenhum caminho que alguém tente
> adivinhar depois.*
>
> **O conserto é a fronteira escrita ao lado do número**, no molde que a v0.144 já tinha
> inventado para as sete marcas: *o que conta, o que não conta, e por quê.*

**E a checagem nova precisou de DUAS contagens, não uma.** *O número de rótulos é a dívida; o de
entradas é **guarda**.* **Sem a guarda, renomear uma tabela faz o reconhecedor achar zero
entrada, logo zero rótulo, e a checagem passa verde para sempre sem ter conferido nada** — é a
lição nº 8 aplicada ao reconhecedor em vez de ao valor.

> **⚠ E o recorte de seção nasceu com o defeito da v0.151 pela segunda vez:** *fechava a `###`
> só na próxima `###`, e não em `##`.* **O corpo de uma entrada vazava três seções adiante.**
>
> **⚠⚠ E o arnês pegou dois defeitos nas PERTURBAÇÕES, não no código.** *Uma regressão que não
> fechava o `**` — o rótulo sumia em vez de voltar, e ela saía verde pelo motivo errado — e um
> contra-teste que mexia na coluna que é a lista de entradas, acendendo a guarda em vez de
> testar o que ele existia para testar.* **Perturbação que não reproduz o defeito não prova
> nada, e as duas pareciam certas lendo.**

---

## A fila, e nenhuma trava a mesa

### 1 · TRÊS dívidas de preço, e as três são versão própria

| dívida | desde | o que é |
|---|---|---|
| **o vão do nível 7** | v0.147 | o vão `físico − conjurador` foi construído sobre a forma antiga do ataque extra, e é ele que paga o degrau dos cinco Caminhos. A inversão deixou pendurado, de propósito |
| **quatro Manhas** | v0.147 | `Gancho`, `Espeto`, `Laço` e `Prego` foram preçados com trava `—`. Agora têm portão, e os `0,71 · 0,71 · 1,06 · 1,06` valem mais do que a entrega entrega |
| **o dano na arma** | v0.148 | **não tem peça, não tem validador e não tem conta.** Mora só no livro, em `Canalizar energia` e `Estímulo Muscular`. É o único dado do sistema nessa situação |

### 2 · As sete marcas de "isto ainda não existe" — cinco assuntos

*O `conferir-voz.py` conta e falha nas duas direções. Dois são grandes:*

- **As três Trilhas do Evocador** — doze entregas preçadas, e o `RASCUNHO-trilhas.md` é a régua.
- **`Sem Técnica`** — precisa de `Estilo da Sombra` **ou** `Aptidão como rota`, e as duas são
  peça própria. **É a nona rota, a única que não fecha ficha.**

E três médios: o **objeto de apoio** (falta a lista do que conta e o preço), a **invocação que
não obedece**, e as **duas de Invocações** que esperam outra peça.

> **⚠⚠ Existe uma sexta pendência de Invocações que a contagem NÃO enxerga:** *"o que acontece
> com a invocação quando o DONO cai".* **Ela não está escrita em lugar nenhum que alguém vá
> olhar** — nem na peça, nem no livro, nem na seção *Em aberto* do capítulo 15. *E o
> `ESTADO-ATUAL` declara que ela e a "vida cheia" **travam as Trilhas do Evocador**.*

### 3 · Meia versão que fecha duas coisas de uma vez

**O inimigo não tem linha de Integridade na tabela do manual** (peça 24 §9) e **não tem Reação
na ficha** (peça 23 §9). *São o mesmo trabalho: imprimir a coluna.* **As duas fecham juntas.**

### 4 · Os dois rascunhos

| rascunho | estado |
|---|---|
| `RASCUNHO-clash-de-expansoes.md` | **nunca foi triado.** 76 linhas. **Leia antes de propor qualquer coisa** |
| `RASCUNHO-trilhas.md` | 926 linhas, a régua das Trilhas. É de onde as três do Evocador saem |

> **⚠ O de clash aponta quatro vezes para "a peça 12" como quem vai resolver ele, e a peça 12
> hoje é *Experiência e Progressão*.** *Ele é da v0.28, de quando a numeração era outra.* **O
> `conferir-repositorio.py` não pega porque `peça 12` sem `§` não é ponteiro de seção.**

### 5 · ~~Dívida de texto~~ — **FECHADA na v0.153**

**`0` rótulos longos demais em `52` entradas de catálogo, com dono na `REGRA-DE-VOZ.md` e
checagem `ROTULO-LONGO` no `conferir-voz.py`.** *Foram catorze rótulos em onze entradas, em
cinco capítulos.* **A fronteira está escrita ao lado do número, e é ela que impede a próxima
contagem de divergir.**

*Se você abrir um capítulo de catálogo por outro motivo, o validador já cobra a forma sozinho.*

---

## O que NÃO é tarefa

**As peças carregam 94 linhas vivas em *Em aberto*, e a maior parte é pergunta de playtest:**
*se Força precisa de um segundo trabalho, se três lutas de graça é o número certo, se alguém
escolhe o Leque.* **Elas esperam mesa, não conserto.**

> **`04-playtest/` continua vazia. Zero sessões desde a v0.1, e todo número do sistema é
> previsão.** *É o maior item aberto do projeto, e o `README` diz isso na cara.*

---

## Método, e ele não é negociável

- **Rode os validadores ANTES de mexer em número:** os 24 de `sistema/03-mecanica/`, o
  `conferir-repositorio.py` da raiz, os dois de `manual/matematica/`, e o `conferir-voz.py
  --estrito` do livro.
- **Meça o sucesso pelo CÓDIGO DE SAÍDA**, nunca casando texto da saída — eles reprovam em
  dois formatos, `>>> N PROBLEMA(S)` e `>>> FALHOU`.
- **Confira `PULADA = 0`.** *Sem `python-docx` cinco validadores pulam em vez de falhar.*
- **Todo número novo ganha validador com teste negativo**, em cópia isolada: confira que a
  base passa antes, que o `diff` entrou, e ponha **contra-teste**.
  ***E confira que cada checagem tem pelo menos uma perturbação que a acende*** — a que
  nenhuma alcança é a que não pode falhar.
- ***E confira a PERTURBAÇÃO também.*** *A v0.153 escreveu duas que pareciam certas lendo e não
  reproduziam o defeito:* **uma saía verde por sumir com o que ia acender, e a outra acendia
  outra checagem.**
- **Todo número publicado leva a FRONTEIRA escrita ao lado.** *Sem ela, a contagem seguinte
  mede outra coisa — aconteceu três vezes com o mesmo número, da v0.141 à v0.152.*
- **Contra-teste coerente mexe em TUDO que a mudança implica.**
- **Nada de valor fica escrito dentro do validador.** Leia do documento dono.
- **Cada peça tem um validador dono.** Checagem nova vai no validador da peça que ela confere.
- **Antes de batizar qualquer coisa:** `python3 conferir-nomes.py --candidatos Nome Outro`.
  *Ela pega substring e não pega colisão de sentido — essa é sua.*
- **Se mexer no livro:** `guard_numeros.py antes.md depois.md` a cada arquivo, com **cada**
  diferença lida contra a linha que a carregava. E os **quatro** builds.
- **Escolha de sabor é dele**, em rodadas curtas, com o número e o trade-off já calculados.
  **Mas não pergunte o que a conta responde.**
- **Documento não pode ter cara de saída de IA.** Português informal, nunca de Portugal.

### Armadilhas medidas, e as duas primeiras são as que mais mordem

> **⚠⚠ Verde não é fim, e a v0.148 é o exemplar mais caro.** *Ela começou com o
> `conferir-voz --estrito` em `0` achados, os 24 validadores verdes e as 251 checagens
> fechando — e a leitura achou **dezoito** coisas.* **Nenhuma delas tinha marca, regex ou
> checagem que pegasse.**
>
> **⚠⚠ Uma checagem pode se medir contra si mesma sem ninguém ver, por DEZENAS de versões.**
> *No `conferir-atributos.py`, `integridade(nv)` e `vida_manual(nv)` eram a mesma expressão
> literal desde a v0.17.* **Ela nunca pôde falhar.**
>
> **⚠⚠ Um reconhecedor que fica cego passa verde para sempre.** *A checagem da v0.153 conta as
> entradas justamente por isso:* **zero entrada achada dá zero rótulo longo, que é o mesmo
> resultado de estar tudo certo.**
>
> **⚠ Frase morta não volta entre aspas — e frase morta EXIGIDA por um validador não sai
> nunca.** *É a v0.148: a checagem 13 do `conferir-ferramenta` casava o literal que continha o
> `sem PE` aposentado.* **Consertar a peça fazia o validador acender, então ninguém consertou.**
>
> **⚠ Ponteiro em tempo presente vira mentira no ato.**
>
> **⚠⚠ Recorte de seção fecha em QUALQUER cabeçalho de nível igual ou menor.** *Duas versões
> pagaram por isso — a v0.151 no bloco de citação, a v0.153 numa `###` que vazava pela `##`
> seguinte.*
>
> **⚠⚠ Editar por script neste mount tem uma armadilha de uma linha.**
> `open(p,'w').write(open(p).read()...)` **trunca o arquivo**: o Python abre para escrita — e
> zera — antes de avaliar a leitura de dentro. **Leia para uma variável ANTES de abrir para
> escrita.** *E se um `assert` matar o script depois do `replace` e antes do `write`, a
> mudança não foi gravada — aconteceu na v0.150, e o validador pegou.*

## Onde as coisas moram

| | |
|---|---|
| as peças de regra | `sistema/03-mecanica/`, 24 peças e 24 validadores |
| o catálogo de entregas | peça 17; os três `DESENHO-*.md` da raiz são os donos do preço |
| a fonte do livro | `sistema/05-material/livro/manual/`, 20 arquivos |
| os builds | `sistema/05-material/livro/build/` |
| a régua de escrita | `sistema/05-material/livro/REGRA-DE-VOZ.md`, e o `METODO-passada-de-texto.md` ao lado |
| a última passada de texto | `sistema/05-material/livro/PENTE-FINO-v0.147.md`, com os dezoito achados e o que entrou em cada um |
| a entrega | `finalizado/`, git próprio. **O `subir.sh` copia; o commit é à mão** |

**Os dois repositórios:** `JJK---Project` (raiz) e `JJK---PDF---RPG` (`finalizado/`).
*Se o repositório for lido por um Project do Claude, **sincronize depois do push**.*

⚠ **Não rode git do sandbox.** Para ver onde o repositório está, leia `.git/refs/heads/main` e
`.git/refs/remotes/origin/main` — ou `.git/packed-refs`, se os dois não existirem como arquivo.

> **Uma sujeira que não é do projeto, e a v0.153 achou uso para ela:**
> `sistema/05-material/livro/.claude/worktrees/magical-shtern-619941/` é uma **cópia inteira do
> repositório na v0.138**, 11 MB, abandonada. *Ela está no `.gitignore` e o `conferir-repositorio.py`
> já a exclui.* **Todo `grep -rn` cai nela e devolve resultado em dobro — mas foi ela que provou
> que a dívida de texto não tinha sido consertada de passagem**, porque é o único lugar do disco
> com o livro de antes da v0.141. *Apagar continua sendo decisão do Mizuki; se apagar, some junto
> a única máquina do tempo que este repositório tem.*

# Retomada — v0.157, e o que sobrou é preço, playtest e dois rascunhos

Pasta: `/media/mizuki/HD Externo II/Claude/Claude 2/`
⚠ Trabalhe na pasta PRINCIPAL, não em worktree. **Você não commita** — deixa a mensagem em
`mensagem-de-commit.txt` e avisa. *A entrega, desde a v0.149, o `subir.sh` copia sozinho.*

Leia primeiro, nesta ordem: `README.md` (a seção *"Nove lições que custaram erro"*),
`sistema/ESTADO-ATUAL.md` **inteiro**, e o `logs/CHANGELOG.md` de cima até a v0.140.

**Projeto na v0.157.** 24 peças · 24 validadores · **258 checagens**. Livro em 17 capítulos,
**71.086 palavras**, **243** páginas em coluna única e **141** em duas. Manual do Fundamento na
**v7.14**. `conferir-voz --estrito` em 0 achados, 0 termos sem destino, 11 triagens, **7 marcas
de "isto ainda não existe" e 0 rótulos longos demais em 52 entradas de catálogo**.

> **Os quatro builds rodaram na v0.154, e a checagem 7.5 está verde.** *Antes de eles valerem,
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

### 1 · TRÊS dívidas de preço

> **⚠⚠ O vão foi medido na v0.154, e o problema não é o que a dívida dizia.** *A taxa que faltava não era pergunta de playtest — ela sai do bloco 1 do `conferir-orcamento.py`: `10,5` rodadas de luta por dia, e o poço de PE diz quantas cabem.* **Com o dano na arma dentro, a Ação de Atacar rende `1,26×` o Classe 0 grátis e NÃO está dominada** — o ataque extra não virou letra morta.
>
> ***O que quebrou é outra coisa:*** **o vão parou de ser um número.** *Na forma da v0.82 o físico e o conjurador faziam a mesma Ação Padrão e o físico tinha uma coisa a mais — subtração limpa. Na forma da v0.147 o físico **escolhe** entre atacar e conjurar, então "físico − conjurador" virou comparação entre duas decisões, e o resultado muda com o poço de PE do Caminho e com a Manha da ficha.*
>
> **Medido: o degrau do nível 7 vale `0,46` fatia sem Manha e `0,85` com uma que escala, contra `2,36` publicado.** *E a forma inverteu — publicado ele CRESCE com o nível, derivado ele ENCOLHE, porque a rodada sem PE fica mais rara conforme o poço cresce.*
>
> ***A escolha que sobrou é do Mizuki, e são duas:*** **A · repreçar para baixo** — mas aí o degrau vale menos que a menor Manha do catálogo, que é o tamanho que este projeto já chamou de entrada morta duas vezes. **C · trocar o que o nível 7 entrega** a Bastião e Vanguarda — mas aí ele deixa de ser "correção de base", que é o argumento que a peça faz há trinta versões.

| dívida | desde | o que é |
|---|---|---|
| **o vão do nível 7** | v0.147 | o vão `físico − conjurador` foi construído sobre a forma antiga do ataque extra, e é ele que paga o degrau dos cinco Caminhos. **Diagnóstico fechado na v0.154; falta a escolha entre A e C** |
| **as Manhas supõem DOIS ataques** | v0.154 | o `Raspão` publica `6,00`, e `6,00` só fecha com dois (`2 × 50% × 6`). **Do nível 2 ao 6 a Vanguarda tem um**, então `Talho`, `Raspão`, `Racho` e `Zunido` entregam metade por cinco níveis. *Consertar mexe no orçamento da Vanguarda inteira* |
| **a 7.4 mede o rótulo, não o conteúdo** | v0.156 | ela lê a **mensagem** do último commit da entrega e tira o `vN.NN` dali. *Uma entrega sincronizada lê como "duas versões atrás" se a mensagem for copiada da vez passada — aconteceu, e travou o `subir.sh`.* **O conserto é ela ler a linha `Recorte da vX.Y` do `README` da entrega no último commit** |
| **as sete travas que não derivam** | v0.147 | `Espeto`, `Laço` e `Prego` não têm o TR no preço; o `60%` do `Abalo` e o `28%` do `Tranco` não vêm de portão nenhum; e o `75%` do `Talho` e do `Encaixe` é do acerto velho. **Medida e declarada NÃO aplicada na v0.156** — refazer põe a banda em `6,2×` |
| **o dano na arma** | v0.148 | **não tem peça, não tem validador e não tem conta.** Mora só no livro, em `Canalizar energia` e `Estímulo Muscular`. É o único dado do sistema nessa situação. ***Levantado na v0.157, e é o próximo item*** — leia o bloco abaixo antes |

> ### ⚠⚠ O dano na arma é o próximo item, e ele já tem DECISÃO tomada e NÃO ESCRITA
>
> **A v0.157 levantou ele e o Mizuki decidiu duas coisas. Nenhuma das duas está em arquivo nenhum — elas só existem no chat que fechou aquela versão.**
>
> ***1. Ele continua escalando com REFINO, de propósito.*** *"Isso incentiva a galera a querer pegar refino, e isso é bom, dá peso para as outras opções."* **O argumento é de desenho e tem de ser escrito assim na peça** — não como efeito colateral.
>
> ***2. O refino `10` passa a dar `+1` dado.*** *A regra fica: `1d4` a cada `3` de refino; no refino `10` os dados viram `d6` **e** entra um dado a mais.* **Hoje o refino `10` dá `3d6` = `10,5`; passa a dar `4d6` = `14,0`.**
>
> | refino | hoje | decidido |
> |---|---|---|
> | 3 · 6 · 9 | `1d4` · `2d4` · `3d4` | **iguais** |
> | **8** *(passivo)* | `2d4` = 5,0 | **igual** |
> | **10** | `3d6` = 10,5 | **`4d6` = 14,0** |
>
> **⚠ Só o refino `10` se move, e isso é o que salva a v0.155:** *o degrau do nível 7 — `Ainda de Pé` em `1,93` e `Não Pega` em `2,10` — foi todo medido em **refino passivo 8**.* **Como o `8` não muda, aquelas contas continuam valendo inteiras.**
>
> **O que o `4d6` custa, medido e aceito por ele:** *a Ação de Atacar do especialista vai de `1,67×` para `2,0×` o Classe 0 grátis; o ataque extra dele vai de `1,68` para `~1,95` fatia; e o espalhamento dentro do mesmo Caminho abre de `3,2×` para `3,7×`.*
>
> **⚠ E fica um ponto de regra por resolver:** *a peça 11 publica que "refino não pode aparecer de um lado de uma rolagem em que o outro lado não cresce no ritmo dele", e ela **nomeia dano** na lista.* **Mas dano não é rolagem disputada — não tem ninguém do outro lado crescendo `+3`**, então a justificativa da trava não alcança ele do mesmo jeito que alcança acerto, CD, defesa e Teste de Resistência. *Ou a peça 11 declara dano fixo como exceção, com o motivo, ou a trava fica larga demais e mente.*
>
> **O trabalho, na ordem:** *(1)* a conta completa, nível a nível, nas duas rotas de refino; *(2)* a peça que esse dado nunca teve, com o argumento do incentivo escrito; *(3)* a linha da peça 11; *(4)* o validador, com a curva reconstruída dos donos e guarda de que ela não vire rolagem disputada.

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

# Retomada — v0.158, e o que sobrou é preço, playtest e dois rascunhos

Pasta: `/media/mizuki/HD Externo II/Claude/Claude 2/`
⚠ Trabalhe na pasta PRINCIPAL, não em worktree. **Você não commita** — deixa a mensagem em
`mensagem-de-commit.txt` e avisa. *A entrega, desde a v0.149, o `subir.sh` copia sozinho.*

Leia primeiro, nesta ordem: `README.md` (a seção *"Nove lições que custaram erro"*),
`sistema/ESTADO-ATUAL.md` **inteiro**, e o `logs/CHANGELOG.md` de cima até a v0.145.

**Projeto na v0.158.** 24 peças · 24 validadores · **259 checagens**. Livro em 17 capítulos,
**71.167 palavras**, **243** páginas em coluna única e **141** em duas. Manual do Fundamento na
**v7.14**. `conferir-voz --estrito` em 0 achados, 0 termos sem destino, 11 triagens, **7 marcas
de "isto ainda não existe" e 0 rótulos longos demais em 52 entradas de catálogo**.

> **⚠⚠ A entrega está DUAS versões atrás, e a ordem inverte.** *O último commit de
> `finalizado/` é da v0.156; o projeto está na v0.158, e a checagem 7.4 reprova com dois de
> distância.* **Rode o `./subir.sh` PRIMEIRO** — o passo 0 sincroniza e suja a árvore da
> entrega —, **ele para na 7.4, você commita a entrega com `recorte da v0.158`, e roda o
> `subir.sh` de novo.**

---

## O que a v0.158 fechou

**O dano na arma ganhou peça, conta e validador**, e ele estava sem os três desde a v0.147 —
era o único dado do sistema nessa situação. *A peça 11 contradizia o livro em três frases, e
o livro contradizia a si mesmo dentro do mesmo capítulo.* **A trava de dano da §2 ganhou o
motivo que ela nunca teve**, e o refino `10` passou a dar `4d6`.

*Antes dela:* **a v0.157** pôs a lição do rótulo da entrega no `README`; **a v0.156** deu dono
à coluna `trava` das Manhas; **a v0.155** fechou o vão do nível 7; **a v0.154** mexeu em cinco
Manhas por leitura dele.

---

## ⚠⚠ A lição que a v0.158 acrescentou, e ela é sobre CONTAGEM outra vez

**Um bloco de checagem com o rótulo em minúscula é invisível para a contagem, e ele não abre
buraco nenhum.** *A checagem 6 do `conferir-manual.py`, escrita na v0.155, nasceu como
`print('  6. os cinco degraus…')` — o extrator da checagem 9 exige maiúscula depois do número.*
**O projeto publicava `258` e o código tinha `257`, por três versões.**

> **É o irmão do defeito da v0.118, e as duas guardas daquela versão não pegam este caso.**
> *Elas procuram **buraco** e **repetição** na sequência de números.* **Um bloco invisível não
> abre buraco: o `6` some, e o `5` vira o último.**
>
> *Fica anotado como conserto barato para quem passar por ali:* **a guarda que falta é o
> extrator aceitar minúscula, ou o `conferir-repositorio.py` acusar `print('N. ` fora do
> `bloco()`.**

---

## A fila, e nenhuma trava a mesa

### 1 · NENHUMA dívida de preço aberta — as três que sobravam viraram decisão declarada

> **⚠⚠ Este arquivo carregou uma dívida MORTA por três versões, e quem achou foi o Mizuki lendo a fila.** *O **vão do nível 7** fechou na v0.155 — o `CHANGELOG` e o `ESTADO-ATUAL` dizem isso com todas as letras desde então —, e este prompt continuou publicando o texto da v0.154, com o bloco de aviso e a escolha entre A e C.*
>
> **Ele foi copiado de novo na v0.158, para dentro de uma versão que rodou os 24 validadores.** *Nenhum deles alcança este arquivo.* **Lição nº 9 no documento que existe para dizer onde o trabalho parou:** *dívida fechada precisa ser desregistrada, e a linha `→ Continua em` do topo do `CHANGELOG` é quem manda.*

| dívida | desde | o que é |
|---|---|---|
| ~~**as Manhas supõem DOIS ataques**~~ | v0.154 | ***MEDIDA na v0.158, e declarada não aplicada.*** *A descrição estava errada em quatro pontos:* **quem cai pela metade é `Raspão`, `Zunido` e `Gancho`; o `Encaixe` cai um terço pelo portão; o `Talho` SOBE; o `Racho` não se move.** *Banda `0,53`–`1,06` e dominância `2,00×` do nível 2 ao 6 — **a dominância melhora**. O que cai é a média, de `0,94` para `0,80`.* **Sub-checagem `13.1` do `conferir-catalogo.py` em cima** |
| **a 7.4 mede o rótulo, não o conteúdo** | v0.156 | ela lê a **mensagem** do último commit da entrega e tira o `vN.NN` dali. *Uma entrega sincronizada lê como "duas versões atrás" se a mensagem for copiada da vez passada.* **O conserto é ela ler a linha `Recorte da vX.Y` do `README` da entrega no último commit.** *Não é dívida de preço — é de validador* |
| **as sete travas que não derivam** | v0.147 | `Espeto`, `Laço` e `Prego` não têm o TR no preço; o `60%` do `Abalo` e o `28%` do `Tranco` não vêm de portão nenhum; e o `75%` do `Talho` e do `Encaixe` é do acerto velho. **Medida e declarada NÃO aplicada na v0.156** — refazer põe a banda em `6,2×`. *Decisão dele, não trabalho pendente* |
| ~~**o vão do nível 7**~~ | v0.147 | ***FECHADA na v0.155.*** *O nível 7 ganhou uma segunda metade que não anda no ataque —* **`Ainda de Pé` no Bastião e `Não Pega` na Vanguarda**, *totais `1,93` e `2,10` contra `2,36`, com a diferença declarada e a checagem 6 do `conferir-manual.py` em cima* |
| ~~**o dano na arma**~~ | v0.148 | ***FECHADA na v0.158.*** **Peça 11 §6.9**, com a escada, o argumento do incentivo, o invariante medido nos 29 níveis e a checagem 10 do `conferir-aptidoes.py` |

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
  base passa antes **e leia o ESTADO dela**, que o `diff` entrou, e ponha **contra-teste**.
  ***E confira que cada checagem tem pelo menos uma perturbação que a acende*** — a que
  nenhuma alcança é a que não pode falhar. *Aconteceu de novo na v0.158, com a sub-checagem do
  incentivo lendo uma terceira cópia da curva.*
- ***E confira a PERTURBAÇÃO também.*** *A v0.153 escreveu duas que pareciam certas lendo e não
  reproduziam o defeito.*
- **Uma checagem que só sabe ler a decisão de hoje mede a decisão, não a relação.** *A v0.158:
  a primeira versão da checagem 10 lia a exceção do refino 10 pelo literal `e entra um dado a
  mais`, então o contra-teste coerente reprovava em vez de sair verde.*
- **Todo número publicado leva a FRONTEIRA escrita ao lado.** *Sem ela, a contagem seguinte
  mede outra coisa.*
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
> fechando — e a leitura achou **dezoito** coisas.*
>
> **⚠⚠ Decisão escrita SÓ NO LIVRO não chega a peça nenhuma, e ela contradiz a peça em
> silêncio.** *É a v0.158: o dano na arma entrou no capítulo na v0.147 e a peça 11 continuou
> publicando "o refino não a escala" em duas cópias, por onze versões.* **A checagem 10 do
> `conferir-aptidoes.py` compara os dois lados agora; nada comparava antes.**
>
> **⚠⚠ Uma checagem pode se medir contra si mesma sem ninguém ver, por DEZENAS de versões.**
>
> **⚠⚠ Um reconhecedor que fica cego passa verde para sempre.**
>
> **⚠⚠ E uma checagem pode ficar invisível para a CONTAGEM sem ficar cega.** *v0.158: rótulo em
> minúscula, e as guardas de buraco e repetição não alcançam.*
>
> **⚠ Frase morta não volta entre aspas — e frase morta EXIGIDA por um validador não sai
> nunca.**
>
> **⚠ Ponteiro em tempo presente vira mentira no ato.** *A v0.158 tirou cinco `hoje` de uma
> seção recém-escrita, porque no commit seguinte "hoje" já é a outra coluna.*
>
> **⚠⚠ Recorte de seção fecha em QUALQUER cabeçalho de nível igual ou menor.**
>
> **⚠⚠ Editar por script neste mount tem uma armadilha de uma linha.**
> `open(p,'w').write(open(p).read()...)` **trunca o arquivo**. **Leia para uma variável ANTES
> de abrir para escrita**, escreva com outro nome e `mv` por cima.

## Onde as coisas moram

| | |
|---|---|
| as peças de regra | `sistema/03-mecanica/`, 24 peças e 24 validadores |
| o catálogo de entregas | peça 17; os três `DESENHO-*.md` da raiz são os donos do preço |
| a fonte do livro | `sistema/05-material/livro/manual/`, 20 arquivos |
| os builds | `sistema/05-material/livro/build/` |
| a régua de escrita | `sistema/05-material/livro/REGRA-DE-VOZ.md`, e o `METODO-passada-de-texto.md` ao lado |
| a última passada de texto | `sistema/05-material/livro/PENTE-FINO-v0.147.md`, com os dezoito achados |
| a entrega | `finalizado/`, git próprio. **O `subir.sh` copia; o commit é à mão** |

**Os dois repositórios:** `JJK---Project` (raiz) e `JJK---PDF---RPG` (`finalizado/`).
*Se o repositório for lido por um Project do Claude, **sincronize depois do push**.*

⚠ **Não rode git do sandbox.** Para ver onde o repositório está, leia `.git/refs/heads/main` e
`.git/refs/remotes/origin/main` — ou `.git/packed-refs`, se os dois não existirem como arquivo.

> **Uma sujeira que não é do projeto:**
> `sistema/05-material/livro/.claude/worktrees/magical-shtern-619941/` é uma **cópia inteira do
> repositório na v0.138**, 11 MB, abandonada. *Ela está no `.gitignore` e o `conferir-repositorio.py`
> já a exclui.* **Todo `grep -rn` cai nela e devolve resultado em dobro — mas foi ela que provou
> que a dívida de texto não tinha sido consertada de passagem**, porque é o único lugar do disco
> com o livro de antes da v0.141. *Apagar continua sendo decisão do Mizuki.*

# Retomada — v0.150, e o que sobrou é preço, playtest e dois rascunhos

Pasta: `/media/mizuki/HD Externo II/Claude/Claude 2/`
⚠ Trabalhe na pasta PRINCIPAL, não em worktree. **Você não commita** — deixa a mensagem em
`mensagem-de-commit.txt` e avisa. *A entrega, desde a v0.149, o `subir.sh` copia sozinho.*

Leia primeiro, nesta ordem: `README.md` (a seção *"Nove lições que custaram erro"*),
`sistema/ESTADO-ATUAL.md` **inteiro**, e o `logs/CHANGELOG.md` de cima até a v0.140.

**Projeto na v0.150.** 24 peças · 24 validadores · **252 checagens**. Livro em 17 capítulos,
**70.771 palavras**, **243** páginas em coluna única e **141** em duas. Manual do Fundamento na
**v7.13**. `conferir-voz --estrito` em 0 achados, 0 termos sem destino e 11 triagens.

> **⚠ Os quatro builds estão por rodar.** *A v0.150 mexeu no capítulo 14 e os artefatos são da
> v0.148.* **A checagem 7.5 acende até eles rodarem** — é ela fazendo o trabalho para o qual a
> v0.146 escreveu ela.

---

## O que as últimas seis versões fecharam

**A v0.147 foi cinco achados de leitura do Mizuki, e um deles reverteu a v0.82** — o ataque
extra voltou a exigir a Ação de Atacar, porque a forma solta fazia o `Bote` da `Estocada` valer
zero.

**A v0.148 foi a sétima passada de texto: dezoito achados, e nenhum saiu de validador.** *O
`conferir-voz --estrito` estava em `0` quando ela começou.* **Dezessete viraram conserto.**

**A v0.149 pôs a cópia para a entrega dentro do `subir.sh`**, com a lista saindo de
`conferir-repositorio.py --recorte` — a mesma de onde a checagem 7.1 lê.

**A v0.150 tirou a descida de grau do `Desgaste`** e pôs contador de missões no lugar.

---

## ⚠⚠ A lição que estas seis versões custaram, e ela é nova

**QUATRO checagens nasceram sem conseguir acender, ou acendendo no lugar errado**, e o arnês
pegou as quatro. *Nenhuma teria sido pega lendo o código.*

| versão | a checagem | o defeito |
|---|---|---|
| v0.147 | `4h` do `conferir-manual` | passava no próprio título da seção que ela conferia |
| v0.148 | `13` do `conferir-ferramenta` | **exigia** uma frase que a v0.116 tinha aposentado — e por isso a frase morta sobreviveu 31 versões em dois documentos |
| v0.148 | `TABELA-VAGA` do `conferir-voz` | dois furos ao mesmo tempo, e os catorze ponteiros do livro escapavam pelos dois |
| v0.150 | `18.5` do `conferir-ferramenta` | excluía linha de citação para pular história — **e a regra mora numa linha de citação também** |

> **O que separa regra de história neste projeto nem sempre é o `>`.** *Na peça 16 é a **aspa**:
> a regra morta está citada entre aspas, e a regra viva não.* **Confira nos dois sentidos:** a
> perturbação que quebra a regra tem de acender, e a história citada tem de ficar verde.

---

## A fila, e nenhuma trava a mesa

### 1 · Quatro dívidas de preço, e as quatro são versão própria

| dívida | desde | o que é |
|---|---|---|
| **os onze `Estigma`** | v0.144 | nunca foram preçados uns contra os outros. O `Quebranto` sai em `1,28` fatias, `6,0%` da Rotina no nível 30, contra `1,6%` do `Contrapeso`, que é Classe 3 |
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

### 5 · Dívida de texto, e ela não é leva

**Nove entradas do livro ainda estão fora das quatro camadas, com doze rótulos em negrito longos
demais para serem nome de efeito.** *Seis das nove no capítulo 12.* **Medido na v0.141 e não
re-medido desde** — uma tentativa na v0.149 contou a coisa errada e foi descartada.

*Se você abrir um desses capítulos por outro motivo, conserte de passagem.*

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
> **⚠ Frase morta não volta entre aspas — e frase morta EXIGIDA por um validador não sai
> nunca.** *É a v0.148: a checagem 13 do `conferir-ferramenta` casava o literal que continha o
> `sem PE` aposentado.* **Consertar a peça fazia o validador acender, então ninguém consertou.**
>
> **⚠ Ponteiro em tempo presente vira mentira no ato.**
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

> **Uma sujeira que não é do projeto, mas atrapalha quem lê com `grep`:**
> `sistema/05-material/livro/.claude/worktrees/magical-shtern-619941/` é uma **cópia inteira do
> repositório na v0.138**, 11 MB, abandonada. *Ela está no `.gitignore` e o `conferir-repositorio.py`
> já a exclui.* **Mas todo `grep -rn` cai nela e devolve resultado em dobro — e ela tem um link
> quebrado que faz `shutil.copytree` estourar.** *Vale apagar, e é decisão do Mizuki.*

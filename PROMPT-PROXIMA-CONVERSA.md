# Retomada — v0.152, e o que sobrou é preço, playtest e dois rascunhos

Pasta: `/media/mizuki/HD Externo II/Claude/Claude 2/`
⚠ Trabalhe na pasta PRINCIPAL, não em worktree. **Você não commita** — deixa a mensagem em
`mensagem-de-commit.txt` e avisa. *A entrega, desde a v0.149, o `subir.sh` copia sozinho.*

Leia primeiro, nesta ordem: `README.md` (a seção *"Nove lições que custaram erro"*),
`sistema/ESTADO-ATUAL.md` **inteiro**, e o `logs/CHANGELOG.md` de cima até a v0.140.

**Projeto na v0.152.** 24 peças · 24 validadores · **255 checagens**. Livro em 17 capítulos,
**70.977 palavras**, **243** páginas em coluna única e **141** em duas. Manual do Fundamento na
**v7.14**. `conferir-voz --estrito` em 0 achados, 0 termos sem destino e 11 triagens.

> **Os quatro builds e o `.pdf` do manual rodaram na v0.151, e a checagem 7.5 está verde.**
> *Foi conferido que a máquina reproduz a diagramação antes de o build valer:* **reconstruindo a
> partir da fonte de antes das edições, a coluna única saiu com `243` páginas e o mesmo tamanho
> em bytes do build anterior.**

---

## O que as últimas sete versões fecharam

**A v0.147 foi cinco achados de leitura do Mizuki, e um deles reverteu a v0.82** — o ataque
extra voltou a exigir a Ação de Atacar, porque a forma solta fazia o `Bote` da `Estocada` valer
zero.

**A v0.148 foi a sétima passada de texto: dezoito achados, e nenhum saiu de validador.** *O
`conferir-voz --estrito` estava em `0` quando ela começou.* **Dezessete viraram conserto.**

**A v0.149 pôs a cópia para a entrega dentro do `subir.sh`**, com a lista saindo de
`conferir-repositorio.py --recorte` — a mesma de onde a checagem 7.1 lê.

**A v0.150 tirou a descida de grau do `Desgaste`** e pôs contador de missões no lugar.

**A v0.151 consertou duas linhas de regra que ele leu e estranhou.** *O `Incapacitado` era uma
condição `Leve` a um `d12` de estourar a própria banda — o preço publicado, `11,00`, era metade de
uma leitura da frase, e virou `4,95` derivado. E o `Cerca` era a única linha de Controle que
prendia um alvo sem dizer como aquilo acaba; ganhou o portão do `Santuário` do 5e.*

---

## ⚠⚠ A lição que estas seis versões custaram, e ela é nova

**SETE checagens nasceram sem conseguir acender, ou acendendo no lugar errado**, e o arnês
pegou as sete. *Nenhuma teria sido pega lendo o código.*

> **⚠ E a v0.151 acrescentou um modo de falha do próprio arnês:** *a base da cópia ficou poluída
> por um diagnóstico à mão e **passou assim**, porque a poluição era coerente — a peça 14 em `d12`
> e a peça 19 em `5,85` fecham entre si.* **"Confira que a base passa antes" não basta: confira o
> ESTADO da base, linha a linha, e não só o código de saída.**

| versão | a checagem | o defeito |
|---|---|---|
| v0.147 | `4h` do `conferir-manual` | passava no próprio título da seção que ela conferia |
| v0.148 | `13` do `conferir-ferramenta` | **exigia** uma frase que a v0.116 tinha aposentado — e por isso a frase morta sobreviveu 31 versões em dois documentos |
| v0.148 | `TABELA-VAGA` do `conferir-voz` | dois furos ao mesmo tempo, e os catorze ponteiros do livro escapavam pelos dois |
| v0.150 | `18.5` do `conferir-ferramenta` | excluía linha de citação para pular história — **e a regra mora numa linha de citação também** |
| v0.151 | `10` do `conferir-atributos` | recortava "o primeiro bloco de citação da seção", e a seção tem outros — tirar o `>` da primeira linha da regra saía **verde** |
| v0.151 | `2.1` do `conferir-dano` | media a PALAVRA `conjuração`, e a frase a diz duas vezes — tirar a exclusão saía **verde** |
| v0.151 | a âncora do dado do soco | o padrão carregava o valor (`` teto é `d10` ``), então mudar o dono a fazia **sumir** em vez de reler |

> **O que separa regra de história neste projeto nem sempre é o `>`.** *Na peça 16 é a **aspa**:
> a regra morta está citada entre aspas, e a regra viva não.* **Confira nos dois sentidos:** a
> perturbação que quebra a regra tem de acender, e a história citada tem de ficar verde.

---

## A fila, e nenhuma trava a mesa

### 1 · TRÊS dívidas de preço, e as três são versão própria

> **✔ A dos `Estigma` fechou na v0.152, e ela encolheu antes de fechar.** *O escopo "os onze uns contra os outros" pedia uma comparação que a peça 11 §4 proíbe — a escada de Classe **não mede quanto, mede o quê**.* **O corte é dentro do degrau, está na peça 16 §6.1, e a checagem 19 guarda ele.** *O `Bojo` foi arrancado (reprovava em `7,85×`), o `Anátema` ganhou texto, e o `Contrapeso` saiu da tabela de preços por ser condicional à ficha.*

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

### 5 · Dívida de texto, e ela não é leva

**Nove entradas do livro ainda estão fora das quatro camadas, com doze rótulos em negrito longos
demais para serem nome de efeito.** *Seis das nove no capítulo 12.* **Medido na v0.141 e não
re-medido desde** — uma tentativa na v0.149 contou a coisa errada e foi descartada.

> **⚠⚠ E a v0.152 tentou re-medir e PAROU, porque o filtro óbvio dá `209`.** *Um regex que pega
> todo rótulo em negrito abrindo parágrafo devolve `209` em 19 capítulos, contra os `12`
> publicados.* **Ele conta as caixas de regra do livro inteiro, e a camada 3 só vale para
> **entrada de catálogo** — condição, Bênção, aptidão, Passiva, `Estigma`, Legado, entrega de
> Trilha.** *Terceira contagem desta família a dar um número diferente; é a lição de medir o
> marcador em vez do fenômeno, e a `REGRA-DE-VOZ.md` já avisa que a camada 3 depende de quebra
> de parágrafo.*
>
> **O recorte que funciona:** *dentro de cada capítulo de catálogo, corte as seções `###` que
> são **entrada** (as que vêm depois do bloco `Como ler …`), e só nelas conte rótulo em negrito
> abrindo parágrafo com mais de `6` palavras.* **Rodado assim no capítulo 12 dá `4` entradas e
> `6` rótulos, das `14` Bênçãos** — e **não** reproduz os `6` de entradas que a v0.141 publicou.
>
> ***Primeiro trabalho de quem pegar isto: fechar essa diferença antes de consertar uma linha.***
> *Ou a v0.141 contou por outra definição, ou duas entradas foram consertadas de passagem nas
> passadas de texto da v0.147 e da v0.148.* **O número não tem dono e nunca teve validador —
> e essa é a metade da dívida que ninguém escreveu.**

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

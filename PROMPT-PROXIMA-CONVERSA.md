# Retomada — quatro tarefas antes do playtest, e elas foram escolhidas pelo Mizuki

Pasta: `/media/mizuki/HD Externo II/Claude/Claude 2/`
⚠ Trabalhe na pasta PRINCIPAL, não em worktree. **Você não commita** — deixa a mensagem em
`mensagem-de-commit.txt` e em `finalizado/mensagem-de-commit.txt`, e avisa.

Leia primeiro, nesta ordem: `README.md` (a seção *"Nove lições que custaram erro"*),
`sistema/ESTADO-ATUAL.md` **inteiro**, e o `logs/CHANGELOG.md` de cima até a v0.136.

**Projeto na v0.142.** 22 peças · 22 validadores · 232 checagens. Livro em 18 capítulos,
**69.966 palavras**, 237 páginas em coluna única e 139 em duas. Manual do Fundamento na
**v7.12**. `conferir-voz --estrito` em 0 achados e 10 triagens.

---

## O objetivo desta leva, e ele muda a prioridade de tudo

> ***"Vamos para algumas tarefas simples e vou mandar para os jogadores testarem."***

**`04-playtest/` está vazia desde a v0.1, e todo número do sistema é previsão.** *Estas quatro
tarefas foram escolhidas por ele para destravar a primeira mesa de teste, e não por tamanho nem
por dependência.* **O critério de pronto aqui é "um jogador consegue usar isso na mesa sem
perguntar", e não "a peça está elegante".**

---

## 1 · Dano de alma com Essência na Integridade — e ele quer a mecânica de alma INTEIRA validada

***Palavras dele:*** *"Começando por 'dano de alma com essência na integridade' temos de validar
toda mecânica de alma."*

**O que já está decidido e nunca foi aplicado:** a Essência entra na Integridade. *Está na fila
do `ESTADO-ATUAL` como "já decidido, não aplicado" há várias versões — **vá achar onde a decisão
foi registrada no `CHANGELOG` antes de reimplementar do zero**, porque decisão registrada não é
decisão aplicada, e reabrir uma que já fechou custa versão.*

**O escopo NÃO é só aplicar a Essência.** Ele pediu a máquina de alma validada, e ela está
espalhada:

| onde | o que mora lá |
|---|---|
| `Toca a Alma` | a Melhoria que converte dano em dano de alma. Manual do Fundamento, e os feitiços prontos `Fissura` e `Sete Palmos` usam ela |
| a Integridade | o recurso que o dano de alma consome |
| peça 19 | a régua de condição e os catorze tipos de dano — o tipo `Alma` é um deles |
| `Alinhavo` / `Remenda` | devolve `5 × Classe` de Integridade, uma vez por cena |

**Comece medindo o que existe**, com `grep -rn "Integridade\|alma" sistema/03-mecanica/`, e monte
a lista do que tem dono e do que não tem **antes** de propor. *A pergunta que provavelmente decide
a tarefa: **quem é o dono da régua de Integridade hoje?** Se a resposta for "ninguém", essa é a
peça que falta, e ela vem antes de qualquer número.*

---

## 2 · O `Bloquear` LIGA, e ele deixou de ser opcional

***Palavras dele, e elas mudam a natureza da regra:*** *"Bloqueio pode ligar, é uma mecânica que
o jogador pode TOMAR, na hora que for receber um ataque, é uma mecânica real, não uma opcional."*

**Hoje ele é `sistema/03-mecanica/RASCUNHO-bloqueio.md`** — fechado em desenho desde a **v0.43**,
e publicado no livro como **capítulo 18, `Apêndice · Bloquear`**, com a moldura de *"decisão de
mesa: Defesa parada ou rolar `2d10` para se defender"*.

**O que a decisão dele obriga:**

1. **O rascunho vira peça numerada** — a próxima livre é a 23 —, e ela precisa nascer com o validador dono dela junto.
   *Meia peça não é peça: `RASCUNHO-*` não leva número justamente por isso.*
2. **⚠ Peça nova e validador novo QUEBRAM a contagem** até o `README`, o `ESTADO-ATUAL` e o
   `LEIA-ME` subirem juntos — o `conferir-repositorio.py` conta os arquivos de peça e de validador
   na pasta e compara com os três documentos. *Vão para 23 · 23.*
3. **O capítulo 18 deixa de ser apêndice** e a moldura de "decisão de mesa" sai do livro inteiro.
   *Procure com `grep -rn "Bloquear\|apêndice" sistema/05-material/livro/manual/` — a promessa
   de opcionalidade está em mais lugares que o capítulo.*
4. **A peça 19 tem uma dívida presa nisto:** o `Incapacitado` vale `11,00` fatias e **metade
   dele — "você não pode `Bloquear`" — dependia de uma regra opcional que nem toda mesa liga.**
   *Com o `Bloquear` ligado por padrão, essa metade passa a valer sempre, e o preço do
   `Incapacitado` muda.* **Meça isso antes de fechar a peça, e se a conta apontar para repreço,
   pare e pergunte.**

---

## 3 · Os três rascunhos

Depois do `Bloquear`, que já é um deles:

| rascunho | estado |
|---|---|
| `RASCUNHO-bloqueio.md` | **vira peça na tarefa 2** |
| `RASCUNHO-clash-de-expansoes.md` | nunca foi triado. **Leia antes de propor qualquer coisa** |
| `RASCUNHO-trilhas.md` | a régua das Trilhas. É de onde as três do Evocador saem, e a v0.68 reformulou ela |

*Um rascunho que vira peça vai com cabeçalho para `99-arquivo/` dizendo de onde saiu, o que o
substituiu, em que versão e **por que morreu**.*

---

## 4 · As quatro marcas de "está sendo escrito" que o leitor vê

*Ele chamou de "marcas invisíveis" e imaginou que fosse simples. **Duas das quatro são**; as
outras duas não.*

| onde | o que o livro diz hoje | tamanho de verdade |
|---|---|---|
| `25-origens.md:661` | `Sem Técnica` → *"não: está sendo escrita"* | **NÃO é simples.** Precisa de `Estilo da Sombra` **ou** `Aptidão como rota`, e as duas são peça |
| `20-criacao-de-personagem.md:110` | as três Trilhas do Evocador | **NÃO é simples.** É a tarefa de doze entregas preçadas |
| `55-ferramenta-amaldicoada.md:13` | como se sintoniza uma ferramenta — *"acordo com o mestre"* | **simples**, e cabe nesta leva |
| `55-ferramenta-amaldicoada.md:192` | o `Estigma` `Avulsa` — *"o limite de uso dela está sendo escrito"* | **simples.** Um relógio, e a `Classe Passiva 2` do capítulo 10 dá o molde: `maestria`× por cena |

**A decisão da v0.129 continua valendo, e ela não é contradita por esta tarefa:** *quando a frase
de estado carrega uma permissão ou um limite que o jogador precisa, ela fica.* **O que sai é a
frase; o que precisa entrar antes é a regra que ela estava substituindo.**

---

## Uma dívida de texto, medida, que pega qualquer capítulo que você abrir

**A v0.141 tornou as *quatro camadas* obrigatórias em toda entrada de catálogo** — está na
régua de voz do livro e no procedimento de passada de texto, os dois em `sistema/05-material/livro/`. **Nove entradas do livro ainda estão fora,
com doze rótulos em negrito longos demais para serem nome de efeito** *(acima das `4 a 6`
palavras que o PHB entrega)*. **Seis das nove estão no capítulo 12, Bênçãos e Lapidação.**

*Não é tarefa desta leva, mas se você mexer num desses capítulos, conserte de passagem.*

---

## Método, e ele não é negociável

- **Rode os validadores ANTES de mexer em número:** os 22 de `sistema/03-mecanica/`, o
  `conferir-repositorio.py` da raiz, os dois de `manual/matematica/`, e o `conferir-voz.py
  --estrito` do livro.
- **Meça o sucesso pelo CÓDIGO DE SAÍDA**, nunca casando texto da saída — eles reprovam em dois
  formatos, `>>> N PROBLEMA(S)` e `>>> FALHOU`.
- **Confira `PULADA = 0`.** *Sem `python-docx` cinco validadores pulam em vez de falhar.*
- **Todo número novo ganha validador com teste negativo**, em cópia isolada: confira que a base
  passa antes, que o `diff` entrou, e ponha **contra-teste**.
- **Nada de valor fica escrito dentro do validador.** Leia do documento dono.
- **Cada peça tem um validador dono.** Checagem nova vai no validador da peça que ela confere.
- **Antes de batizar qualquer coisa:** `python3 conferir-nomes.py --candidatos Nome Outro`.
  *Ela pega substring e não pega colisão de sentido — essa é sua.*
- **Se mexer no livro:** `guard_numeros.py antes.md depois.md` a cada arquivo, com **cada**
  diferença lida contra a linha que a carregava. E os **quatro** builds: `build.py`,
  `build.py --duas`, `build_docx.py` e `build_txt.py`.
- **Escolha de sabor é dele**, em rodadas curtas, com o número e o trade-off já calculados.
  **Mas não pergunte o que a conta responde** — na v0.141 uma pergunta sobre o `Calo` ia sair e
  a regra da Passiva Livre já respondia ela.
- **Documento não pode ter cara de saída de IA.** Português informal, nunca de Portugal.

### Três armadilhas medidas nas últimas cinco versões

> **⚠ Verde não é fim.** *Na v0.139 os 22 validadores passavam com `PULADA = 0` e treze lugares
> ainda diziam `catorze` para um número que tinha virado treze.* **Contagem escrita em frase não
> tem dono** — a checagem 9 confere contagem de arquivo, não de prosa. **Releia as listas à mão.**
>
> **⚠ Medir o marcador em vez do fenômeno erra para os DOIS lados.** *Na v0.140 a primeira
> varredura de tabela redundante deu nove candidatas e **cinco eram falso positivo** — ela media
> "as palavras voltam", e num capítulo onde o vocabulário satura isso acende sempre.* **Cortar
> pela primeira medida teria apagado três tabelas boas.**
>
> **⚠ Quando um bloco sai ou se move, o que fala dele vai junto.** *Cinco vezes em quatro
> versões.* **E a v0.142 achou uma forma nova:** *não é a frase que sobrevive ao bloco — é o
> **bloco de nota** que sobrevive à entrada que ele comentava.* **Nenhum validador alcança.**

## Onde as coisas moram

| | |
|---|---|
| as peças de regra | `sistema/03-mecanica/`, 22 peças e 22 validadores |
| o catálogo de entregas | peça 17; os três `DESENHO-*.md` da raiz são os donos do preço |
| a fonte do livro | `sistema/05-material/livro/manual/`, 21 arquivos |
| a régua de escrita | `sistema/05-material/livro/REGRA-DE-VOZ.md`, e o procedimento de passada de texto ao lado dela |
| como regerar o livro | o `README.md` de `sistema/05-material/livro/` |
| a entrega | `finalizado/`, git próprio, **precisa do commit dela depois do commit do projeto** |

**Os dois repositórios:** `JJK---Project` (raiz) e `JJK---PDF---RPG` (`finalizado/`).
*Se o repositório for lido por um Project do Claude, **sincronize depois do push**.*

⚠ **Não rode git do sandbox.** Para ver onde o repositório está, leia `.git/refs/heads/main` e
`.git/refs/remotes/origin/main` — ou `.git/packed-refs`, se os dois não existirem como arquivo.

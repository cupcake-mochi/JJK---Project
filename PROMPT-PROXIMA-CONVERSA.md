# Retomada — v0.159, e o que sobrou é um validador, playtest e dois rascunhos

Pasta: `/media/mizuki/HD Externo II/Claude/Claude 2/`
⚠ Trabalhe na pasta PRINCIPAL, não em worktree. **Você não commita** — deixa a mensagem em
`mensagem-de-commit.txt` e avisa. *A entrega, desde a v0.149, o `subir.sh` copia sozinho.*

Leia primeiro, nesta ordem: `README.md` (a seção *"Nove lições que custaram erro"*),
`sistema/ESTADO-ATUAL.md` **inteiro**, e o `logs/CHANGELOG.md` de cima até a v0.145.

**Projeto na v0.159.** 24 peças · 24 validadores · **261 checagens**. Livro em 17 capítulos,
**71.167 palavras**, **243** páginas em coluna única e **141** em duas. Manual do Fundamento na
**v7.15**. `conferir-voz --estrito` em 0 achados, 0 termos sem destino, **10 triagens**, **7
marcas de "isto ainda não existe" e 0 rótulos longos demais em 52 entradas de catálogo**.

> **A entrega está UMA versão atrás, que é o normal — a ordem não inverte.** *O último commit
> de `finalizado/` é `recorte da v0.158`, e a checagem 7.4 aceita uma de distância.* **Rode o
> `./subir.sh` normalmente e commite a entrega depois**, com `recorte da v0.159`.

---

## O que a v0.159 fechou

**O inimigo ganhou as duas linhas que faltavam nele**, e elas eram o mesmo trabalho:
*a peça 24 §8 pedia a Integridade dele desde a v0.145 e a peça 23 §9 pedia a Reação desde a
v0.143, as duas apontando para a mesma seção do manual.* **Nenhum número do sistema se moveu.**

*E de passagem:* **o manual publicava a Integridade errada há treze versões**, a contagem de
checagens escapava por **três** portas e não pela que a v0.158 anotou, e o `11 triagens` era
`10` desde a v0.150.

*Antes dela:* **a v0.158** deu peça, conta e validador ao dano na arma; **a v0.157** pôs a lição
do rótulo da entrega no `README`; **a v0.156** deu dono à coluna `trava` das Manhas; **a v0.155**
fechou o vão do nível 7.

---

## ⚠⚠ A lição que a v0.159 acrescentou, e ela é sobre MAPA DERIVADO

**Um mapa derivado que ninguém imprime é um mapa que ninguém confere.** *O
`conferir-repositorio.py` deriva o validador dono de cada peça do nome do arquivo — e
`24-dano-de-alma.md` começa com `dano`, então a peça 24 caía no `conferir-dano.py`, que é da peça
19.* **O `conferir-alma.py` ficava sem peça nenhuma desde a v0.145.**

> **Ele passou despercebido por coincidência aritmética: os dois tinham ONZE checagens.** *A linha
> do `ESTADO-ATUAL` que publica a contagem da peça 24 estava sendo conferida contra o validador
> errado, e batia.*
>
> **Consertado sem tabela escrita** — *peça que cai num validador já tomado tenta um candidato
> livre do próprio slug* —, **e a checagem 9 passou a imprimir o mapa**: quantas peças ela mapeou
> e quais validadores ficam sem peça de propósito.

---

## A fila, e nenhuma trava a mesa

### 1 · NENHUMA dívida de preço aberta

*As três que existiam viraram decisão declarada, e a última — o dano na arma — virou a §6.9 da
peça 11 na v0.158.* **Fica só a das sete travas das Manhas, medida na v0.156 e declarada NÃO
aplicada:** *`Espeto`, `Laço` e `Prego` não têm o TR no preço; o `60%` do `Abalo` e o `28%` do
`Tranco` não vêm de portão nenhum; e o `75%` do `Talho` e do `Encaixe` é do acerto velho.*
**Refazer põe a banda em `6,2×`, e a decisão dele foi não mexer.**

### 2 · O CONSERTO DA CHECAGEM 7.4 — o mais barato da fila, e sem decisão dele

**Ela lê a MENSAGEM do último commit da entrega — `git log -1 --pretty=%s` — e tira o `vN.NN`
dali, em vez de ler a linha `Recorte da vX.Y` do `README` da entrega dentro daquele commit.**
*Uma entrega perfeitamente sincronizada é lida como "duas versões atrás" se alguém copiar a
mensagem da vez passada.* **Já travou o `subir.sh` duas vezes.**

> **⚠ O arnês desse conserto precisa de um clone descartável em `/tmp`**, com commits rotulados
> errado de propósito — *não dá para fabricar isso na entrega de verdade.* **E o git da entrega
> É legível do sandbox: medido na v0.159**, a própria 7.4 rodou `git -C finalizado` e leu o
> último commit sem deixar lock. *Quem não é legível é o git da RAIZ, e nele não se toca.*

### 3 · Uma coisa pequena que a v0.159 achou e NÃO consertou

**O passo 0 do `subir.sh` acerta a versão do RECORTE no `README` da entrega e não acerta a
versão do MANUAL.** *A checagem 7.3 confere as duas, então ela pega — mas o conserto é à mão, a
cada vez que o manual muda de versão.* **Foi à mão nesta versão, nas quatro ocorrências.**

> *Não virou `sed` no `subir.sh` de propósito:* **as quatro ocorrências estão em negrito e há um
> `` `v7.9` `` histórico entre crases na mesma página.** *Um `sed` cego que acerte as quatro hoje
> apaga história amanhã, e a 7.3 já grita alto.* **Decisão registrada, não dívida.**

### 4 · ⚠ NÃO existe ficha de inimigo, e três documentos falam dela

**O manual não tem bloco de inimigo.** *A seção `Inimigos` é uma tabela de nível → vida e dano mais prosa; o apêndice tem `Ficha de feitiço` e nada equivalente.* **Montar um inimigo pede NOVE números com QUATRO donos** — o manual (vida, dano, e a Integridade e a Reação desde a v0.159), a peça 19 (as `3` ações do chefe e a falha de TR de `35%`), a peça 1 (a Defesa do alvo difícil, que é régua de medida), e o `ESTADO-ATUAL`, que declara na seção do clash que o inimigo carrega refino e aptidões.

> **Juntar os nove é o `Bestiário`**, que está no fim da fila com uma linha só. *Ele é peça, e não meia versão* — e a linha do clash é dono provisório dentro de um documento de retomada, que é o padrão de "vocabulário que ainda não tem peça".

### 5 · As sete marcas de "isto ainda não existe" — cinco assuntos

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

### 6 · Os dois rascunhos

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
  ***E confira que cada checagem tem pelo menos uma perturbação que a acende.***
- ***E confira a PERTURBAÇÃO também.*** *A v0.153 escreveu duas que pareciam certas lendo e não
  reproduziam o defeito.*
- **Uma checagem que só sabe ler a decisão de hoje mede a decisão, não a relação.** *O
  contra-teste que prova o contrário reverte a decisão de forma COERENTE em todos os lugares e
  sai verde.*
- **Contra-teste coerente mexe em TUDO que a mudança implica.** *A v0.159 escreveu um que mexia
  em dois donos quando a mudança implicava quatro, e ele acendeu com razão.*
- **Todo número publicado leva a FRONTEIRA escrita ao lado.**
- **Nada de valor fica escrito dentro do validador.** Leia do documento dono.
- **Cada peça tem um validador dono.** Checagem nova vai no validador da peça que ela confere.
- **Antes de batizar qualquer coisa:** `python3 conferir-nomes.py --candidatos Nome Outro`.
  *Ela pega substring e não pega colisão de sentido — essa é sua.*
- **Se mexer no livro:** `guard_numeros.py antes.md depois.md` a cada arquivo, com **cada**
  diferença lida contra a linha que a carregava. E os **quatro** builds.
- **Se mexer no manual:** `node make.js`, `soffice --headless --convert-to pdf`, e **rode o
  controle antes de o build valer** — reconstrua a versão anterior a partir da fonte e compare
  o XML do documento contra o `.docx` que está na entrega. *Na v0.159 ele saiu idêntico.*
- **Escolha de sabor é dele**, em rodadas curtas, com o número e o trade-off já calculados.
  **Mas não pergunte o que a conta responde.**
- **Documento não pode ter cara de saída de IA.** Português informal, nunca de Portugal.

### Armadilhas medidas, e as duas primeiras são as que mais mordem

> **⚠⚠ Verde não é fim, e a v0.148 é o exemplar mais caro.** *Ela começou com o
> `conferir-voz --estrito` em `0` achados, os 24 validadores verdes e as 251 checagens
> fechando — e a leitura achou **dezoito** coisas.*
>
> **⚠⚠ A pendência muitas vezes descreve o conserto ERRADO, e as duas da v0.159 descreviam o
> mesmo errado.** *As duas pediam "valor sugerido por nível na tabela", e nenhuma das duas tem
> valor por nível.* **Leia o que a dívida pede, depois meça se aquilo existe.**
>
> **⚠⚠ Decisão escrita SÓ NO LIVRO não chega a peça nenhuma, e ela contradiz a peça em
> silêncio.** *E a irmã dela:* **decisão escrita SÓ NA PEÇA não chega ao manual.** *A v0.145
> recolheu a máquina de alma e deixou o manual ensinando a Integridade antiga por treze versões.*
>
> **⚠⚠ Uma checagem pode se medir contra si mesma sem ninguém ver, por DEZENAS de versões.**
>
> **⚠⚠ Um reconhecedor que fica cego passa verde para sempre.**
>
> **⚠⚠ E uma checagem pode ficar invisível para a CONTAGEM sem ficar cega.** *Três portas, e a
> v0.159 fechou as três: rótulo em minúscula, mapa peça→validador errado, e uma exceção de regex
> que lia a linha inteira em vez da janela em volta do número.*
>
> **⚠ Frase morta não volta entre aspas — e frase morta EXIGIDA por um validador não sai
> nunca.**
>
> **⚠ Ponteiro em tempo presente vira mentira no ato.**
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
| o gerador do manual | `manual/gerador/`, e o `COMO-USAR.txt` é o dono da versão dele |
| a entrega | `finalizado/`, git próprio. **O `subir.sh` copia; o commit é à mão** |

**Os dois repositórios:** `JJK---Project` (raiz) e `JJK---PDF---RPG` (`finalizado/`).
*Se o repositório for lido por um Project do Claude, **sincronize depois do push**.*

⚠ **Não rode git do sandbox.** Para ver onde a entrega está sem rodar git, leia
`finalizado/.git/logs/HEAD` como arquivo — é texto puro e não cria lock.

> **Uma sujeira que não é do projeto:**
> `sistema/05-material/livro/.claude/worktrees/magical-shtern-619941/` é uma **cópia inteira do
> repositório na v0.138**, 11 MB, abandonada. *Ela está no `.gitignore` e o `conferir-repositorio.py`
> já a exclui.* **Todo `grep -rn` cai nela e devolve resultado em dobro — e ela é o único lugar do
> disco com o livro de antes da v0.141**, o que já serviu duas vezes: provou que a dívida de texto
> não tinha sido consertada de passagem (v0.153) e datou a queda do `11 triagens` (v0.159).
> *Apagar continua sendo decisão do Mizuki.*

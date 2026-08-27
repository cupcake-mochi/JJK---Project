# Retomada — a v0.171 fechou quatro itens, e **parou no meio de uma pergunta**

Pasta: `/media/mizuki/HD Externo II/Claude/Claude 2/`
⚠ Trabalhe na pasta PRINCIPAL, não em worktree. **Você não commita** — deixa a mensagem em
`mensagem-de-commit.txt` e avisa. *A entrega, desde a v0.149, o `subir.sh` copia sozinho.*

> ## ⚠ Estado no disco: a v0.171 está ESCRITA e NÃO commitada
>
> **Os 25 validadores de `03-mecanica/`, os quatro de `manual/matematica/` e o
> `conferir-voz.py --estrito` saem `0` com `PULADA = 0`.** *O `conferir-repositorio.py` sai com
> **duas** falhas, e as duas são o passo 0 do `subir.sh` que ainda não rodou:* **a 7.1 (a cópia
> da entrega está velha) e a 7.3 (o `README` da entrega ainda diz `v0.170`).**
>
> **`mensagem-de-commit.txt` está pronto.** *Rode `./subir.sh`; ele sincroniza a entrega, para na
> 7.4, e aí você commita a entrega e roda de novo.*

Leia primeiro, nesta ordem: `README.md` (a seção *"Nove lições que custaram erro"*),
`sistema/ESTADO-ATUAL.md` **inteiro**, e o `logs/CHANGELOG.md` de cima até a v0.160.

---

## ⚠⚠ O PRIMEIRO ITEM É UMA PERGUNTA JÁ FEITA, ESPERANDO RESPOSTA

*O Mizuki parou a sessão nela, com estas palavras: **"Vamos parar aqui por hoje, salve oq
fizemos e deixe claro q paramos nessa pergunta, irei continuar amanha."*** **Não refaça o
levantamento — as opções já estão medidas e estão no CHANGELOG da v0.171, na seção *"Onde a
sessão parou"*. Traga as três de cada e pergunte.**

### a · O formato da lista de feitos do limiar do nível 20 — peça 12 §7

**A peça exige lista FECHADA:** *"entradas escritas, e a palavra final do mestre em cima delas —
nunca do zero"*. **Três formatos na mesa:**

| formato | o que é |
|---|---|
| **oito entradas** | maldição de grau acima · sair de pé de uma Expansão completa · fechar um incidente que teria vazado · trazer de volta quem estava a zero · escrever um Fundamento inédito · honrar um Pacto caro · a instituição te dever um favor · perder alguém e continuar |
| **cinco entradas** | as que menos se sobrepõem — saem trazer de volta, o Fundamento inédito e o favor |
| **quatro eixos** | combate · mundo · instituição · pessoa, com dois a três exemplos embaixo de cada |

*Cada entrada precisa ser conferível por um segundo mestre sem julgamento — é o filtro
multi-mestre, e é ele que reprova "o mestre decide o que é um feito".*

### b · A forma da conversão de mestragem — peça 12 §6

**A peça já escreve a trava:** *"um bônus por marca, não por sessão (…) e ela não pode virar
pagamento por mesa disfarçado"*.

| forma | o que pesa a favor, e contra |
|---|---|
| **um feito do limiar a cada N mesas** | é literalmente *"por marca"*, e reusa a lista do item **a**. Não inventa moeda nem número |
| **um degrau de patente, com teto** | ficou **mais caro depois da v0.171**: o salário sai do Grau, então subir patente dobra a renda e a mestragem passa a pagar em iene por via indireta |
| **um pagamento em iene numa marca** | é a única recompensa do sistema que a v0.171 **provou** não comprar poder |

---

## O resto da fila, na ordem

### 2 · `RASCUNHO-clash-de-expansoes.md` — engatilhado, ninguém tocou

**O clash entre duas Expansões de Domínio abertas ao mesmo tempo ficou de fora de propósito.**
*O modelo cogitado — push gradual — pede seis números novos e mexe numa regra já marcada como
fechada.*

### 3 · `BESTIÁRIO` — por último, e é a única peça nova da fila

**Montar um inimigo pede NOVE números com QUATRO donos**, e o levantamento é da v0.159: *o
manual, a peça 19, a peça 1 e o `ESTADO-ATUAL`, que declara na seção do clash que o inimigo
carrega refino e aptidões "na ficha dele".*

> ***Decisão da v0.161, e ela vale:*** **é máquina MAIS maldições prontas**, e não recolhimento
> puro. *O molde é o da peça 15, que é máquina de construção com catálogo em cima.*

**⚠⚠ E NÃO existe ficha de inimigo hoje, apesar de três documentos falarem dela.** *O manual não
tem bloco de inimigo: a seção `Inimigos` é uma tabela de nível → vida e dano, mais prosa.*
**O que a v0.159 já deixou pronto:** *a Integridade do inimigo é a vida máxima dele, e a Reação
dele é o mesmo slot que a peça 3 §3 dá a qualquer ficha.*

> **⚠ E a v0.171 encostou nele sem querer:** *a escada de salário por patente e o gate de `Grau`
> em `Arma de Fogo` e `Revestimento` valem para **feiticeiro**.* **Um inimigo humano armado
> passa a ter de dizer de onde veio a arma dele**, e isso é uma linha da peça nova.

---

## Três achados que a v0.171 deixou anotados e não pagou

- **⚠ A checagem de pasta do `README.md` está QUEBRADA, e ela é o guarda da retomada.** *Ele
  manda rodar `grep -c "Seis lições" README.md # tem que dar 0`, e **dá `2`** — porque as
  palavras `Seis lições` aparecem duas vezes no próprio texto da checagem.* **No clone velho ela
  daria `1`.** *A checagem está invertida, e o conserto é uma linha: use só o `grep -c "^## Nove
  lições"`, que dá `1` aqui e `0` lá.* **Não mexi porque é o guarda da retomada e o Mizuki tinha
  pedido para parar.**
- **A tabela de `quedas por missão padrão` da peça 1 §5.5 não tem validador.** *Ela publica
  `1,14` para o perfil frágil, e o `conferir-atributos.py` recalcula `1,22` no bloco 9.4 sem
  comparar com o escrito.* **Dois números para a mesma coisa, e ninguém compara.**
- **A peça 18 continua genuinamente aberta** — *"quando o PDF sair, a tabela vai aparecer lá"*, e
  a tabela consolidada de progressão de nove colunas ainda não está publicada nele.

## O que fica fora da fila, de propósito

**As perguntas em *"Marcado para o playtest"* do `ESTADO-ATUAL`.** *O próprio projeto marca: não
reabra sem retorno de jogador.* **E `04-playtest/` continua vazia — zero sessões desde a v0.1, e
todo número do sistema é previsão.**

---

## ⚠⚠ Seis lições que as últimas versões pagaram

> **1 · Prosa SOBRE a regra não é a regra.** *Reaparece toda vez que um extrator lê SEÇÃO onde
> devia ler LINHA DE REGRA.* **A v0.171 pagou de novo:** *a checagem da `Cicatriz` lia a seção, e
> a seção DISCUTE as quatro formas reprovadas — uma delas é "penalidade em rolagem de combate".*
>
> **2 · Janela de `N` caracteres morre num ponto final.** *`Cicatriz[^.]{0,160}acerto` não
> alcança a própria linha de regra, porque ela tem um ponto no meio.* **Duas perturbações saíram
> VERDES por isso na v0.171. Leia a linha, não a janela.**
>
> **3 · Total certo esconde dono errado.** *A checagem 6 do `conferir-criacao.py` lia a soma das
> duas rotas de ofício, e ela fecha com a atribuição trocada — sessenta e cinco versões.*
>
> **4 · Guarda de contagem é o que separa "conferiu" de "não achou".** *O extrator de armas da
> checagem 13 lia `45` de `52`, e só a guarda acusou.*
>
> **5 · Pendência cujo assunto não é uma peça não tem quem a alcance.** *Sétimo achado dessa
> família na v0.171 — o livro ainda dizia que `Sem Técnica` não fecha ficha.*
>
> **6 · Não cite nome de arquivo cru entre crases dentro de uma peça.** *A checagem 7.2 lê toda
> citação assim na árvore da ENTREGA e cobra que o arquivo exista lá.*

## Método, e ele não é negociável

- **Rode os validadores ANTES de mexer em número:** os de `sistema/03-mecanica/`, o
  `conferir-repositorio.py` da raiz, os quatro de `manual/matematica/`, e o `conferir-voz.py
  --estrito` do livro. **Meça pelo CÓDIGO DE SAÍDA**, e confira **`PULADA = 0`**.
- **Todo número novo ganha validador com teste negativo**, em cópia isolada. *Confira que a base
  passa na cópia **e que a checagem nova RODOU** antes de perturbar.* **E confira que a
  PERTURBAÇÃO mudou o arquivo.**
  > **⚠ A cópia isolada precisa da ÁRVORE, e não só de `03-mecanica/`.** *Vários validadores leem
  > `../ESTADO-ATUAL.md` e o livro.* **O jeito que funcionou na v0.171: montar a árvore com
  > `symlink` para tudo e cópia de verdade só da pasta que vai ser perturbada.**
- **Uma checagem que só sabe ler a decisão de hoje mede a decisão, não a relação.** *O
  contra-teste que vale reverte a decisão de forma COERENTE em TODOS os donos e sai verde.*
- **Nada de valor fica escrito dentro do validador.** Leia do documento dono. *As exceções são
  `limite de design` (lição nº 8) e **âncora externa** — o `¥29,61M` do ministro, na checagem 13.*
- **⚠ Marca dentro de célula de tabela quebra extrator de OUTRO validador.** Marca vai embaixo.
- **⚠ Tabela dentro de bloco de citação também quebra.**
- **Antes de batizar:** `python3 conferir-nomes.py --candidatos Nome Outro`. *Leva ~21 s.*
- **Pesquise antes de inventar.** *Os PDFs estão em `PDFs - Sistemas Extras/PDF_Sistemas/`, e o
  `pdftotext -layout` já está instalado.* **A v0.171 rendeu duas âncoras boas dali e da web:** o
  `Ferimentos Persistentes` do Guia do Mestre e o salário do ministro.
- **Se mexer no livro:** `guard_numeros.py antes.md depois.md` a cada arquivo, com CADA diferença
  lida contra a linha que a carregava, e os **quatro** builds. *Salve o "antes" ANTES de editar.*
  **E confira se alguma diferença SUMIU** — número que aparece é acréscimo, número que some é
  regra que você apagou sem ver. *Mande o PDF de duas colunas antes de ele commitar.*
- **⚠ Ponteiro de capítulo do livro:** *`Experiência e Progressão` é o **18**, `Fundamento` é o
  **9**, `Criação de Personagem` é o **6**, `Equipamento` é o **14**.* **A checagem 10.3 só
  confere os que trazem o título junto — escreva sempre `capítulo N, *Título*`.**
- **Escolha de sabor é dele**, em rodadas curtas, com o número e o trade-off já calculados.
  **Mas não pergunte o que a conta responde.**
- **Documento não pode ter cara de saída de IA.** Português informal, nunca de Portugal.

## Onde as coisas moram

| | |
|---|---|
| as peças de regra | `sistema/03-mecanica/` — **25 peças e 25 validadores** |
| o catálogo de entregas | peça 17; os três `DESENHO-*.md` da raiz são os donos do preço |
| a moeda | **peça 12 §6.1** é dona do salário; **peça 14 §6.5** é dona do preço |
| a fonte do livro | `sistema/05-material/livro/manual/`, **21 arquivos** — 18 capítulos e 3 de frente |
| a régua de escrita | `sistema/05-material/livro/REGRA-DE-VOZ.md` — **`3` marcas de pendência** |
| a lista branca da 7.2 | base `146`, folga `5`, **teto `151`** |
| o gerador do manual | `manual/gerador/`, e o `COMO-USAR.txt` é o dono da versão dele |
| a entrega | `finalizado/`, git próprio. **O `subir.sh` copia; o commit é à mão** |

⚠ **Não rode git do sandbox.** Para ver onde a entrega está, leia `finalizado/.git/logs/HEAD`
como arquivo.

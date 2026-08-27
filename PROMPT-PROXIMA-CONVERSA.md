# Retomada — a v0.172 fechou a pergunta, e a peça 12 não tem mais item de decisão

Pasta: `/media/mizuki/HD Externo II/Claude/Claude 2/`
⚠ Trabalhe na pasta PRINCIPAL, não em worktree. **Você não commita** — deixa a mensagem em
`mensagem-de-commit.txt` e avisa. *A entrega, desde a v0.149, o `subir.sh` copia sozinho.*

> ## ⚠ Estado no disco: a v0.172 está ESCRITA e NÃO commitada
>
> **Os 25 validadores de `03-mecanica/`, os quatro de `manual/matematica/` e o
> `conferir-voz.py --estrito` saem `0` com `PULADA = 0`.** *O `conferir-repositorio.py` sai com
> **duas** falhas, e as duas são o passo 0 do `subir.sh` que ainda não rodou:* **a 7.1 (a cópia
> da entrega está velha, em três arquivos) e a 7.3 (o `README` da entrega ainda diz `v0.171`).**
>
> **`mensagem-de-commit.txt` está pronto.** *Rode `./subir.sh`; ele sincroniza a entrega, para na
> 7.4, e aí você commita a entrega e roda de novo.* **Os quatro builds do livro já rodaram.**

Leia primeiro, nesta ordem: `README.md` (a seção *"Nove lições que custaram erro"*),
`sistema/ESTADO-ATUAL.md` **inteiro**, e o `logs/CHANGELOG.md` de cima até a v0.160.

---

## A fila, e ela tem dois itens

### 1 · `RASCUNHO-clash-de-expansoes.md` — engatilhado, ninguém tocou

**O clash entre duas Expansões de Domínio abertas ao mesmo tempo ficou de fora de propósito.**
*O modelo cogitado — push gradual — pede seis números novos e mexe numa regra já marcada como
fechada.*

### 2 · `BESTIÁRIO` — a única peça nova da fila

**Montar um inimigo pede NOVE números com QUATRO donos**, e o levantamento é da v0.159: *o
manual, a peça 19, a peça 1 e o `ESTADO-ATUAL`, que declara na seção do clash que o inimigo
carrega refino e aptidões "na ficha dele".*

> ***Decisão da v0.161, e ela vale:*** **é máquina MAIS maldições prontas**, e não recolhimento
> puro. *O molde é o da peça 15, que é máquina de construção com catálogo em cima.*

**⚠⚠ E NÃO existe ficha de inimigo hoje, apesar de três documentos falarem dela.** *O manual não
tem bloco de inimigo: a seção `Inimigos` é uma tabela de `nível do grupo → vida e dano`, com as
colunas `Chefe` e `Capanga`, mais prosa.* **O que a v0.159 já deixou pronto:** *a Integridade do
inimigo é a vida máxima dele, e a Reação dele é o mesmo slot que a peça 3 §3 dá a qualquer ficha.*

> **⚠ A v0.171 encostou nele:** *a escada de salário por patente e o gate de `Grau` em
> `Arma de Fogo` e `Revestimento` valem para **feiticeiro**.* **Um inimigo humano armado passa a
> ter de dizer de onde veio a arma dele.**
>
> **⚠⚠ E a v0.172 acrescentou uma DECISÃO que ele herda: o inimigo ganha `grau`?** *Hoje não
> tem — a escada `grau 4 a grau 1, mais o especial` é de **ferramenta** (peça 16 §3) e de
> **patente** (peça 12 §6.1), e nenhum documento dá grau a maldição.* **O feito 1 do §7.1 da
> peça 12 está escrito em `nível` por causa disso**, e a nota lá diz que ele volta à forma
> original — *"maldição de grau acima"* — se o BESTIÁRIO decidir que sim. *É a linha que obriga
> a decisão a ser tomada em vez de ficar implícita.*

---

## Dois achados anotados e ainda não pagos

- **A tabela de `quedas por missão padrão` da peça 1 §5.5 não tem validador.** *Ela publica
  `1,14` para o perfil frágil, e o `conferir-atributos.py` recalcula `1,22` no bloco 9.4 sem
  comparar com o escrito.* **Dois números para a mesma coisa, e ninguém compara.**
- **A peça 18 continua genuinamente aberta** — *"quando o PDF sair, a tabela vai aparecer lá"*, e
  a tabela consolidada de progressão de nove colunas ainda não está publicada nele.

*O terceiro achado da v0.171 — o guarda de pasta do `README` invertido — **foi pago na v0.172**.*

## O que fica fora da fila, de propósito

**As perguntas em *"Marcado para o playtest"* do `ESTADO-ATUAL`.** *O próprio projeto marca: não
reabra sem retorno de jogador.* **E `04-playtest/` continua vazia — zero sessões desde a v0.1, e
todo número do sistema é previsão.**

---

## ⚠⚠ Sete lições que as últimas versões pagaram

> **1 · Prosa SOBRE a regra não é a regra.** *Reaparece toda vez que um extrator lê SEÇÃO onde
> devia ler LINHA DE REGRA.* **A v0.171 pagou de novo** — a checagem da `Cicatriz` lia a seção, e
> a seção DISCUTE as quatro formas reprovadas.
>
> **2 · Janela de `N` caracteres morre num ponto final.** *`Cicatriz[^.]{0,160}acerto` não
> alcança a própria linha de regra, porque ela tem um ponto no meio.* **Leia a linha, não a
> janela.**
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
>
> **7 · A régua que uma peça escreveu costuma valer para o projeto inteiro, e ninguém vai
> buscar.** *A v0.172 foi escrever a lista de feitos e o filtro dela já estava pronto na peça 10
> desde a v0.26 — **pergunta sobre o mundo fica na lista fechada; pergunta sobre a cena que
> aquele mestre dirigiu, não**.* **Cento e quarenta e seis versões sem sair da peça que o
> escreveu, e ele reprovou três das oito entradas de primeira.** *Antes de inventar critério,
> procure se alguma peça já escreveu um.*

## Método, e ele não é negociável

- **Rode os validadores ANTES de mexer em número:** os de `sistema/03-mecanica/`, o
  `conferir-repositorio.py` da raiz, os quatro de `manual/matematica/`, e o `conferir-voz.py
  --estrito` do livro. **Meça pelo CÓDIGO DE SAÍDA**, e confira **`PULADA = 0`**.
- **Todo número novo ganha validador com teste negativo**, em cópia isolada. *Confira que a base
  passa na cópia **e que a checagem nova RODOU** antes de perturbar.* **E confira que a
  PERTURBAÇÃO mudou o arquivo** — a v0.172 teve um contra-teste recusado pela guarda porque a
  string literal não existia no arquivo.
  > **⚠ A cópia isolada precisa da ÁRVORE, e não só de `03-mecanica/`.** *Vários validadores leem
  > `../ESTADO-ATUAL.md`, o livro e `../01-pesquisa/`.* **O jeito que funciona: montar a árvore com
  > `symlink` para tudo e cópia de verdade só da pasta que vai ser perturbada.**
- **Uma checagem que só sabe ler a decisão de hoje mede a decisão, não a relação.** *O
  contra-teste que vale reverte a decisão de forma COERENTE em TODOS os donos e sai verde.*
- **Nada de valor fica escrito dentro do validador.** Leia do documento dono. *As exceções são
  `limite de design` (lição nº 8) e **âncora externa** — o `¥29,61M` do ministro, na checagem 13.*
- **⚠ Marca dentro de célula de tabela quebra extrator de OUTRO validador.** Marca vai embaixo.
- **⚠ Tabela dentro de bloco de citação também quebra.**
- **Antes de batizar:** `python3 conferir-nomes.py --candidatos Nome Outro`. *Leva ~21 s.*
- **Pesquise antes de inventar.** *Os PDFs estão em `PDFs - Sistemas Extras/PDF_Sistemas/`, e o
  `pdftotext -layout` já está instalado.*
- **Se mexer no livro:** `guard_numeros.py antes.md depois.md` a cada arquivo, com CADA diferença
  lida contra a linha que a carregava, e os **quatro** builds. *Salve o "antes" ANTES de editar.*
  **E confira se alguma diferença SUMIU** — número que aparece é acréscimo, número que some é
  regra que você apagou sem ver. *Na v0.172 sumiu um `15`, e ele era o fim de uma faixa `13 a 15`
  que virou `14 a 16`.* **Mande o PDF de duas colunas antes de ele commitar.**
- **⚠ Ponteiro de capítulo do livro:** *`Experiência e Progressão` é o **18**, `Sem Técnica` é o
  **11**, `Fundamento` é o **9**, `Criação de Personagem` é o **6**, `Equipamento` é o **14**.*
  **A checagem 10.3 só confere os que trazem o título junto — escreva sempre `capítulo N,
  *Título*`.** *A tabela de roteiro da introdução é a quarta cópia da lista, e desde a v0.172 a
  checagem 10.7 a compara com o `build.py`.*
- **Escolha de sabor é dele**, em rodadas curtas, com o número e o trade-off já calculados.
  **Mas não pergunte o que a conta responde.**
- **Documento não pode ter cara de saída de IA.** Português informal, nunca de Portugal.

## Onde as coisas moram

| | |
|---|---|
| as peças de regra | `sistema/03-mecanica/` — **25 peças e 25 validadores** |
| o catálogo de entregas | peça 17; os três `DESENHO-*.md` da raiz são os donos do preço |
| a moeda | **peça 12 §6.1** é dona do salário e o **§6.2** da mestragem; **peça 14 §6.5** é dona do preço |
| a fonte do livro | `sistema/05-material/livro/manual/`, **21 arquivos** — 18 capítulos e 3 de frente |
| a ordem dos capítulos | `build.py`, e ela é a dona — outras três cópias são conferidas contra ela |
| a régua de escrita | `sistema/05-material/livro/REGRA-DE-VOZ.md` — **`3` marcas de pendência** |
| a lista branca da 7.2 | base `146`, folga `5`, **teto `151`** |
| o gerador do manual | `manual/gerador/`, e o `COMO-USAR.txt` é o dono da versão dele |
| a entrega | `finalizado/`, git próprio. **O `subir.sh` copia; o commit é à mão** |

⚠ **Não rode git do sandbox.** Para ver onde a entrega está, leia `finalizado/.git/logs/HEAD`
como arquivo.

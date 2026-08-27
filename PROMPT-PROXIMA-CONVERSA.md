# Retomada — a v0.170 fechou, e o `BESTIÁRIO` é o único item da fila

Pasta: `/media/mizuki/HD Externo II/Claude/Claude 2/`
⚠ Trabalhe na pasta PRINCIPAL, não em worktree. **Você não commita** — deixa a mensagem em
`mensagem-de-commit.txt` e avisa. *A entrega, desde a v0.149, o `subir.sh` copia sozinho.*

> ## Estado no disco
>
> **A v0.170 está fechada e validada, e a `mensagem-de-commit.txt` da raiz é a dela.**
> *Os 25 validadores de `03-mecanica/`, os quatro de `manual/matematica/` e o `conferir-voz.py
> --estrito` saem `0` com `PULADA = 0`.* **O `conferir-repositorio.py` sai `1` só pela ENTREGA**,
> e o passo 0 do `./subir.sh` resolve isso antes de rodar validador.

Leia primeiro, nesta ordem: `README.md` (a seção *"Nove lições que custaram erro"*),
`sistema/ESTADO-ATUAL.md` **inteiro**, e o `logs/CHANGELOG.md` de cima até a v0.160.

---

## A v0.171 — o `BESTIÁRIO`, e ele é a última peça da fila

**Montar um inimigo pede NOVE números com QUATRO donos**, e o levantamento é da v0.159:
*o manual, a peça 19, a peça 1 e o `ESTADO-ATUAL`, que declara na seção do clash que o inimigo
carrega refino e aptidões "na ficha dele".* **Juntar os nove é a peça, e ela é peça e não
recolhimento.**

> ***Decisão da v0.161, e ela vale:*** **é máquina MAIS maldições prontas**, e não recolhimento
> puro. *O molde é o da peça 15, que é máquina de construção com catálogo em cima.*

**⚠⚠ E NÃO existe ficha de inimigo hoje, apesar de três documentos falarem dela.** *O manual não
tem bloco de inimigo: a seção `Inimigos` é uma tabela de nível → vida e dano, mais prosa, e o
apêndice tem `Ficha de feitiço` e nada do outro lado.*

**O que a v0.159 já deixou pronto para ela:** *a Integridade do inimigo é a vida máxima dele —
não tem valor por nível, e a tabela já publica a vida —, e a Reação dele é o mesmo slot que a
peça 3 §3 dá a qualquer ficha.* **O que faltava não era um segundo valor: era um segundo lugar
de marcar.**

## Depois dela

1. **Duas dívidas de argumento, as duas velhas:**
   - **⚠⚠ `08-criacao-de-personagem.md` Passo 1 dá os ofícios ao dono errado.** *Ele diz que a
     **Origem** entrega "dois ofícios livres", e a peça 7 §6 é dona: o **Caminho** dá dois, a
     Origem dá um ou uma perícia. O total `8+3`/`9+2` só fecha pela leitura da 7.*
   - **⚠ A peça 11 §6 justifica *"o refino não escala a `Energia Reversa`"* citando uma §2 que a
     v0.158 substituiu.** *A decisão pode ficar; o argumento caiu há doze versões.* **A peça 25 §6
     já registra isso por escrito, então quem for pagar tem o diagnóstico pronto.**
2. **O texto de mesa das peças que ainda não têm capítulo próprio.** *Hoje o livro cobre bem, e o
   que a v0.170 mostrou é que "o texto de mesa" como item de pendência **não tem quem o alcance**
   — a checagem 8 casa por nome de peça, e aquele assunto não é uma peça.*

> **`04-playtest/` continua vazia. Zero sessões desde a v0.1, e todo número do sistema é
> previsão.** *É o maior item aberto do projeto, e ele não é de regra.*

---

## O que as três últimas versões fecharam

**v0.170 — `Sem Técnica` virou o capítulo 11 do livro**, o `43-sem-tecnica.md`, no molde do
`42-tecnica-marcial.md`. *O Manual da Guilda foi de `17` para `18` capítulos, e a seção daquela
rota no capítulo de Origens virou ponteiro.*

> **⚠⚠ Capítulo no meio desloca todo mundo: `38` referências, em treze arquivos** — os capítulos
> `11` a `17` viraram `12` a `18`. **E a checagem 10.3 só confere metade delas:** *ela lê
> `capítulo N, *Título*`, e as `44` que dizem só `capítulo N` não têm como ser conferidas.*
>
> **⚠⚠ Duas pendências mortas que nenhuma checagem alcançava, e uma tinha quarenta e oito
> versões.** *A peça 20 pedia o texto de mesa desde a v0.122, com o capítulo dela pronto desde a
> v0.124.* ***As duas escapavam pelo mesmo motivo: o assunto delas é "o texto de mesa", e a 8c
> casa por nome de PEÇA.***
>
> **⚠ E a v0.168 tinha deixado o livro contradizendo a peça 13** — o `Inédito` ainda excluía
> `Sem Técnica`, e aquela versão reverteu exatamente isso. *Corrigiu a peça e não desceu ao livro.*

**v0.169 — limpeza.** *A base da lista branca da 7.2 estava a UMA citação de reprovar: o aviso da
v0.162 funcionou e ninguém atendeu ele por seis versões.* **Base `146`, folga `5`, teto `151`**,
com as `146` reclassificadas por família. *E o `README.md` da entrega publicava a contagem de
capítulos duas vezes discordando de si mesma, mais três contagens de página e uma linha de índice
duplicada — a de capítulos ganhou dono e checagem, a de páginas passou a aparecer uma vez só.*

**v0.168 — `Sem Técnica` virou a peça 25**, e a nona rota de Origem fechou. *A máquina é o
Fundamento inteiro; a semente é uma aptidão aberta na criação, em `Classe Passiva 2` ou `3`, e a
banda é DERIVADA da escada de gate da peça 11 §5.*

---

## ⚠⚠ Cinco lições que as três últimas versões pagaram

> **1 · Prosa SOBRE a regra não é a regra.** *A v0.168 pegou isso três vezes dentro do validador
> novo e mais duas em validadores velhos lendo a peça nova.* **Reaparece toda vez que um extrator
> lê SEÇÃO onde devia ler LINHA DE REGRA.**
>
> **2 · Slug de uma palavra casa com o projeto inteiro.** *A `10.6` já sabia disso e escreveu; a
> `8`, no mesmo arquivo, não sabia.* **Guarda que existe num lugar não protege o vizinho.**
>
> **3 · Guarda que aceita o sinal em QUALQUER ponto da frase não separa nada.** *O arnês pegou: a
> perturbação que tirava a identidade saía verde pelo motivo errado.*
>
> **4 · Aviso que ninguém atende é teto sem folga com um passo a mais.** *A v0.162 escreveu o
> aviso justamente para falar na primeira citação nova; ele falou seis versões e a base ficou
> parada até a folga acabar.*
>
> **5 · Pendência cujo assunto não é uma peça não tem quem a alcance.** *A checagem 8 casa por
> nome de peça — "o texto de mesa" atravessou quarenta e oito versões viva.*

## Método, e ele não é negociável

- **Rode os validadores ANTES de mexer em número:** os de `sistema/03-mecanica/`, o
  `conferir-repositorio.py` da raiz, os quatro de `manual/matematica/`, e o `conferir-voz.py
  --estrito` do livro. **Meça pelo CÓDIGO DE SAÍDA**, e confira **`PULADA = 0`**.
- **Todo número novo ganha validador com teste negativo**, em cópia isolada. *Confira que a base
  passa na cópia **e que a checagem nova RODOU** antes de perturbar.* **E confira que a
  PERTURBAÇÃO mudou o arquivo** — `sed` que não bate produz "não acendeu" falso.
- **Uma checagem que só sabe ler a decisão de hoje mede a decisão, não a relação.** *O
  contra-teste que vale reverte a decisão de forma COERENTE em TODOS os donos e sai verde.*
- **Nada de valor fica escrito dentro do validador.** Leia do documento dono. *A exceção é
  `limite de design`, que existe para ser comparado com a regra aplicada — lição nº 8, e o
  `PECAS_ESPERADAS` do `conferir-catalogo.py` é o exemplar.*
- **⚠ Marca dentro de célula de tabela quebra extrator de OUTRO validador.** Marca vai embaixo.
- **⚠ Tabela dentro de bloco de citação também quebra.** *Molde da casa: texto de abertura,
  tabela solta, e o corpo do Legado no `>` depois dela.*
- **Antes de batizar:** `python3 conferir-nomes.py --candidatos Nome Outro`. *Ela leva ~21 s.*
- **Pesquise antes de inventar.** Os PDFs estão em `PDFs - Sistemas Extras/PDF_Sistemas/`.
- **Se mexer no livro:** `guard_numeros.py antes.md depois.md` a cada arquivo, com CADA
  diferença lida contra a linha que a carregava, e os **quatro** builds. *Mande o PDF de duas
  colunas antes de ele commitar.*
- **⚠⚠ Se ACRESCENTAR capítulo:** ele entra nas **três** listas que a 10.1 compara (`build.py`,
  `build_docx.py`, `conferir-voz.py`), **todas as referências cruzadas acima dele deslocam**, e a
  contagem de capítulos sobe nos **três** lugares que a publicam — o `README.md` do projeto, que é
  o dono, e as duas cópias do README da entrega.
- **Se mexer no manual:** `node make.js`, `soffice --headless --convert-to pdf`, e **rode o
  controle antes de o build valer.**
- **Escolha de sabor é dele**, em rodadas curtas, com o número e o trade-off já calculados.
  **Mas não pergunte o que a conta responde.**
- **Documento não pode ter cara de saída de IA.** Português informal, nunca de Portugal.

## Onde as coisas moram

| | |
|---|---|
| as peças de regra | `sistema/03-mecanica/` — **25 peças e 25 validadores** |
| o catálogo de entregas | peça 17; os três `DESENHO-*.md` da raiz são os donos do preço |
| a fonte do livro | `sistema/05-material/livro/manual/`, **21 arquivos** — 18 capítulos e 3 de frente |
| a régua de escrita | `sistema/05-material/livro/REGRA-DE-VOZ.md` — **`3` marcas de pendência** |
| a lista branca da 7.2 | base `146`, folga `5`, **teto `151`** — o comentário dela no `conferir-repositorio.py` é o dono |
| o gerador do manual | `manual/gerador/`, e o `COMO-USAR.txt` é o dono da versão dele |
| a entrega | `finalizado/`, git próprio. **O `subir.sh` copia; o commit é à mão** |

⚠ **Não rode git do sandbox.** Para ver onde a entrega está, leia `finalizado/.git/logs/HEAD`
como arquivo.

# Retomada — v0.165, e a tarefa é a criação de `Sem Técnica`

Pasta: `/media/mizuki/HD Externo II/Claude/Claude 2/`
⚠ Trabalhe na pasta PRINCIPAL, não em worktree. **Você não commita** — deixa a mensagem em
`mensagem-de-commit.txt` e avisa. *A entrega, desde a v0.149, o `subir.sh` copia sozinho.*

Leia primeiro, nesta ordem: `README.md` (a seção *"Nove lições que custaram erro"*),
`sistema/ESTADO-ATUAL.md` **inteiro**, e o `logs/CHANGELOG.md` de cima até a v0.145.

**Projeto na v0.165.** 24 peças · 24 validadores · **266 checagens**. Livro em 17 capítulos,
**72.171 palavras**, **245** páginas em coluna única e **142** em duas. Manual do Fundamento na
**v7.16**. `conferir-voz --estrito` em 0 achados, 0 termos sem destino, **4 marcas de "isto
ainda não existe" e 0 rótulos longos demais em 52 entradas de catálogo**.

> ***A fila da mecânica ficou SEM ITEM na v0.164***, quando as quinze Trilhas fecharam. **O que
> sobra são duas peças, e a de baixo é a que fecha uma rota de ficha:** o `Bestiário` e a
> criação de `Sem Técnica`. *A segunda é a tarefa desta conversa.*

---

## A TAREFA — a máquina de criação de `Sem Técnica`

**Ela é a NONA rota de Origem, e a única que não fecha ficha hoje.** *As outras oito rodam
desde a v0.122.* **Decisão do Mizuki, daquela versão: ela tem criação própria e vem depois** —
e "depois" chegou.

**Leia, além da ordem acima:** a seção *"Sem Técnica precisa de máquina de criação própria, e
ela é menor do que o esqueleto supôs"* do `ESTADO-ATUAL`, a **peça 9** (`09-origens.md`) e a
**peça 20** (`20-tecnica-marcial.md`).

### O que já está pronto, e é a razão de começar por aqui

- **O `arquitetura.md` diz que ela precisa de "um sistema próprio, paralelo ao Fundamento".**
  *A v0.38 mediu e discordou:* **pelo material ela precisa de MENOS do que isso, e por outro
  motivo, de mais.**
- **As duas rotas do material são `Aptidão` e `Estilo da Sombra`, e as duas já têm peça atrás.**
  *As anti-domínio entraram na v0.29 — hoje são **três**, e a `Extensão de Domínio` está ao
  lado delas sem ser da categoria, desde a v0.165.* **A `Energia Reversa` fechou na v0.78**, na
  peça 11 §6, com gate e teto.
- **A peça 11 §6.5 já trata o `Domínio Simples` como aptidão pura, sem lâmina.**
- **A peça 22 §3.5 escreve um CONTRATO em vez de um número** para os estilos do `Estilo da
  Sombra`, porque a peça deles não existe. *Ele é o que a sua peça precisa obedecer, no molde
  do teto de Defesa da peça 14 §3.*

### A trava que decide a peça, e ela já está escrita

> *"A rota não pode ser 'os outros menos o Fundamento'. Se for só subtração, ela fica atrás de
> todo mundo e ninguém escolhe por vontade — escolhe por castigo. Ela precisa de uma máquina de
> construção com a mesma dignidade que o Fundamento tem: quantas aptidões, com que orçamento, e
> o que se paga por elas."*

**E o precedente mais próximo é a peça 20, a Técnica Marcial.** *Ela é o Fundamento com o corpo
no lugar da energia, e **não tem número novo nenhum** — pontos são `3 × Classe`, o PE é o mesmo
número, o que sobra de ponto vira `1d8`. O que muda é a criação.* **Vale medir se `Sem Técnica`
cabe no mesmo molde antes de inventar máquina.**

### Duas coisas presas nisto

**A prosa da peça 9 chama o `Estilo da Sombra` de "técnica de espada e corpo"**, e isso ficou
mais estreito que a própria mecânica do projeto — *a técnica central foi aprendida em um mês
por quem não usa espada.* **Corrigir quando a peça sair.**

**Quando ela entrar, as rotas de Origem vão de `8/9` para `9/9`**, e essa contagem é publicada
no `README` e no `ESTADO-ATUAL`. *E uma das quatro marcas do livro fecha* — a do capítulo 25,
`25-origens.md:408`, que diz *"Sem Técnica não fecha ficha hoje, e ela está sendo escrita"*.
**O dono da contagem é o `REGRA-DE-VOZ.md`, e o `conferir-voz.py` falha nas duas direções**,
então o número desce no mesmo commit.

---

## O que a v0.165 fechou

**Cinco correções pequenas, e três vieram de colegas do Mizuki lendo o material.**

- **A `cobrir-se` das Bênçãos herda a Reação** — pergunta aberta desde a v0.124, e ela não
  inventa número: mesma substituição da proteção, refino por Lapidação.
- **A `Extensão de Domínio` saiu da categoria anti-domínio.** *Ela não **é** uma; ela **serve**
  como uma.* **Nada de mecânico se moveu**, e o argumento de que os anti-domínio serem baratos
  é o que segura o acerto garantido ficou **mais forte** — ela era a única Classe Passiva 3 das
  quatro.
- **E o "anula qualquer técnica" dela ganhou teto:** `1/3 do refino + 1`, que é `3` no gate e
  `4` no teto de refino, contra uma escada de Classe que vai a `7`. *O número reconstrói da
  proteção de `cobrir-se`.* **Checagem 12 do `conferir-aptidoes.py`, sete perturbações.**
- **O Emanador não mexe com aptidão**, e três lugares diziam que sim.
- **O `README` publicava três rascunhos e são dois**, desde a v0.143.

> **⚠⚠ E o arnês da v0.165 pegou dois defeitos antes do commit, os dois de método.** *A base
> falhou na cópia isolada e a checagem nova nem rodou — **todas** as perturbações saíram
> "verdes".* **Verde de checagem que não rodou não prova nada.** *E o conserto destampou o
> segundo: o extrator lia a fórmula da **seção** inteira, e a seção tem prosa citando a mesma
> fórmula para explicar de onde ela vem — apagar a **regra** e deixar o **comentário** saía
> verde.* **Hoje ele lê a linha de regra**, e é a mesma família do recorte que a v0.151
> consertou.
>
> **⚠ E marca dentro de célula de tabela quebra extrator de OUTRO validador.** *Um `— não é da
> categoria` na célula fez o `conferir-ferramenta.py` parar de achar o gate na peça 11.*
> **Marca vai embaixo da tabela.**

## O que a v0.164 fechou

**As doze entregas do Evocador, e com elas as quinze Trilhas.** *`Servo` `7,32` · `Matilha`
`5,05` · `Coro` `7,67`, de `5,00`, com os três estouros declarados.*

> **⚠⚠ O `Servo` que o rascunho publicava como "montado" estava numa escala morta há nove
> versões**, e a `LISTA-gatilhos` já tinha achado isso na v0.77 sem que o achado voltasse para
> o rascunho. **E o segundo defeito não era de escala:** *o `Servo` e a `Matilha` **comandam e
> não atacam**, então as quatro maiores linhas da régua dependem de uma Ação Padrão que duas
> das três Trilhas gastam na porta de entrada.*
>
> **A `Matilha` não lidera coluna nenhuma, e isso é declarado.** *Duas Trilhas monocromáticas
> na mesma coluna sempre dominam uma à outra, e mexer no número só troca quem domina.* **A
> checagem 15 do `conferir-catalogo.py` reconta a matriz das linhas de preço e cobra que a
> declaração nomeie o eixo que resolve o par fora dela.**
>
> **E a triagem era cega para o catálogo de Bênçãos inteiro** — foi assim que `Casco` acabou
> batizado duas vezes. *Consertado; o nome duplicado fica como achado.*

---

---

## O que a v0.163 fechou

**As duas pendências de Invocações que travavam as três Trilhas do Evocador**, e nenhuma das
duas era a decisão que parecia ser.

> ***"O que acontece com a invocação quando o dono cai"* não estava escrito em lugar nenhum**,
> nem na peça, nem no livro, nem na seção `Em aberto` dele — por isso a contagem de marcas não a
> via. *Três quartos da pergunta já estavam respondidos:* **`Insistir` a regra resolve sozinha**
> (quem fica de pé tem Ação Padrão, então comanda), e **a invocação AGIR sozinha é recusada pela
> conta** — sem a Ação Padrão do dono ela agiria de graça, e a §1 da peça mede isso: *dobra o
> dano por rodada*. **Sobrou o `Aguentar`, e a decisão dele foi: ela fica parada.**
>
> *E a v0.162 deixou pronto o que faz isso valer:* **um corpo de pé em cima do dono caído é
> `uma criatura no caminho`, logo cobertura `Parcial`** — `+2` de Defesa pela janela inteira,
> sem regra nova.
>
> **A vida cheia volta no descanso longo, e isso não era sabor:** *a peça 10 §3 já decidiu que
> respiro não devolve vida, e a meia vida da invocação é vida.*
>
> **Entrou a checagem 31**, que LÊ o degrau da linha `Vida` das tabelas da peça 10 em vez de
> guardar a palavra. *Onze perturbações, dez acendendo, e o contra-teste vira a escada nos três
> donos e sai verde.*
>
> **⚠⚠ E o `conferir-repositorio.py` tinha DOIS leitores de numeral** — a checagem 9 tinha o
> próprio mapa, sem compostos, o mesmo defeito que a v0.132 consertou no outro. *`"trinta e uma
> checagens"` era lida como `1`.* **Viraram um.**

## O que a v0.162 fechou

**Duas entradas PREÇADAS do manual compravam furar cobertura contra graus que este sistema não
tem** — `cobertura leve` (que é do **GURPS**, e nem grau é: lá é um `−2` de tiro) e `meia
cobertura` (o *half cover* do **D&D 2014**). *A escada daqui é `Parcial` · `Boa` · `Total`.*
**As duas passaram a citar a `Parcial`, e nenhum preço se moveu — isso é derivado:** ler como
dois degraus entregaria `4,75×`, que não é reescrita de texto, é outra entrada.

> **⚠⚠ E o `INDEFINIDOS_ACEITOS` do `conferir-manual.py` não isentava nada.** *O único ponto que
> consulta a lista é um `elif` dentro do laço do `EXIGEM_DEFINICAO`, e as duas não tinham um
> termo em comum — ramo inalcançável.* **`cobertura leve` saiu, e `inimigo fraco` entrou no
> `EXIGEM_DEFINICAO` para a isenção virar caminho vivo.**
>
> *A escada NÃO foi comprimida, e isso foi medido a pedido dele:* **a premissa está certa — o
> acerto daqui topa em `+10` contra o `+11` do d20 —, mas `+2/+5` é a mais próxima das três**
> (`5,3` pp contra `6,8` do `+2/+4` e `12,9` do `+1/+4`). *A medida virou a §5.2 da peça 19.*
>
> **Entrou a checagem 7**, que falha nas duas direções — grau inexistente e cópia de bônus.
> *Onze perturbações, oito acendendo e três contra-testes. O arnês pegou **duas** perturbações
> minhas que saíam verdes pelo motivo errado.*

## O que a v0.161 fechou

**O `sete` sobreviveu setenta e duas versões à decisão que o aposentou.** *A v0.89 pôs a rota
pura de Refino em `10` aptidões; quatro lugares continuaram publicando `7`, e as duas peças
envolvidas se contradiziam por dentro — tabela contra prosa a poucas linhas de distância.*
**Nada no projeto comparava essa contagem com coisa nenhuma.**

> **⚠⚠ E `meio a meio` nomeava TRÊS rotas** — a curva da peça 11 §3 (`3` escolhas de Refino), a
> tabela do `ESTADO-ATUAL` (`2`) e a linha `ROTAS` do próprio `conferir-aptidoes.py` (`2`). *A
> terceira só aparecia na SAÍDA da checagem 5, imprimindo os totais de outra rota.* **Todas as
> três foram alinhadas à curva da peça, que é de onde o `conferir-atributos.py` deriva a Defesa
> do alvo difícil.**
>
> *Duas frases do clash caíram junto:* **o `+3, que é 72%` mede o marco 22 e não o 26**, e o
> `perdem 12%` **não sai de vantagem nenhuma** — a lista possível é `45·36·28·21·15·10·6·3·1%`.
>
> **Entrou a checagem 11**, com guarda de reconhecedor e 19 perturbações (17 acendendo, 2
> contra-testes). *O arnês achou dois defeitos: um guarda antigo que acusava e **estourava**
> logo depois, e um contra-teste meu que mexia em dois donos quando a mudança implica três.*

## O que a v0.160 fechou

**A checagem 7.4 parou de medir o rótulo do commit da entrega e passou a medir o conteúdo dele.**
*O buraco era dos dois lados: entrega em dia reprovava com mensagem copiada — foi a v0.156, três
rodadas para achar —, e entrega duas versões atrasada passava com mensagem certa por cima.*

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

> ***A posição das Trilhas saiu na v0.164***, e a de `Sem Técnica` virou a TAREFA desta
> conversa — ela está lá em cima. **O que sobra abaixo é o resto da fila.**

### 1 · NENHUMA dívida de preço aberta

*As três que existiam viraram decisão declarada, e a última — o dano na arma — virou a §6.9 da
peça 11 na v0.158.* **Fica só a das sete travas das Manhas, medida na v0.156 e declarada NÃO
aplicada:** *`Espeto`, `Laço` e `Prego` não têm o TR no preço; o `60%` do `Abalo` e o `28%` do
`Tranco` não vêm de portão nenhum; e o `75%` do `Talho` e do `Encaixe` é do acerto velho.*
**Refazer põe a banda em `6,2×`, e a decisão dele foi não mexer.**

### 2 · O `BESTIÁRIO`, e ele deixou de ser uma linha no fim da fila

***NÃO existe ficha de inimigo, e três documentos falam dela.*** *Achado do Mizuki lendo o fecho
da v0.159.* **O manual não tem bloco de inimigo:** a seção `Inimigos` é uma tabela de nível →
vida e dano, mais prosa; o apêndice tem `Ficha de feitiço` e nada equivalente do outro lado.

**Montar um inimigo pede NOVE números, e eles têm QUATRO donos:**

| o número | dono |
|---|---|
| vida e dano por nível, chefe e capanga | **o manual**, a tabela |
| Integridade e Reação | **o manual**, desde a v0.159 |
| as `3` ações do chefe por rodada | peça 19 §2.1 |
| a falha de Teste de Resistência, `35%` contra o alvo treinado | peça 19 §2.5 |
| a Defesa do alvo difícil | peça 1 §6 — *e ela é régua de medida, não número de mesa* |
| refino e aptidões | **o `ESTADO-ATUAL`**, na seção do clash |

> **Nenhum documento junta os nove**, e um dos donos é o `ESTADO-ATUAL` — o padrão de
> *"vocabulário que ainda não tem peça"* de novo.
>
> ***Decisão do Mizuki na v0.161: ela é MÁQUINA MAIS MALDIÇÕES PRONTAS***, e não recolhimento
> puro. *A máquina junta os nove números com os donos que eles já têm; o catálogo é material
> escrito em cima dela.* **Cada bicho escrito tem de reconstruir da tabela do manual**, então o
> validador cresce por entrada e não só por campo — e material sem playtest é previsão em cima
> de previsão. *Com catálogo, o nome `Bestiário` deixa de prometer o que não entrega; ele saiu
> `LIVRE` na triagem.*

> **⚠ A v0.161 acertou dois dos nove antes de a peça começar.** *O refino e as aptidões do
> chefe saem da curva do `meio a meio`, e aquela curva tinha três leituras — a tabela do
> `ESTADO-ATUAL` dava `2` aptidões no nível 30 e a curva da peça 11 dá `3`.* **Na grade da
> tabela de inimigo do manual, que anda de 5 em 5, o chefe fica assim:**
>
> | nível | 5 | 10 | 15 | 20 | 25 | 30 |
> |---|---|---|---|---|---|---|
> | refino | `1` | `4` | `6` | `7` | `9` | `10` |
> | aptidões | `0` | `1` | `2` | `2` | `3` | `3` |
>
> **As duas grades não batem** — a do manual anda de `5` em `5` e os marcos de refino caem em
> `6·10·14·18·22·26·30`. *O `1 / 0` do nível 5 é feio e inofensivo: a Expansão mais cedo que
> existe é nível 10, então aquela linha nunca vê um clash.* **Decidir se a coluna entra nessa
> grade torta ou ganha grade própria é da peça.**

### 3 · Uma coisa pequena que a v0.159 achou e NÃO consertou

**O passo 0 do `subir.sh` acerta a versão do RECORTE no `README` da entrega e não acerta a
versão do MANUAL.** *A checagem 7.3 confere as duas, então ela pega — mas o conserto é à mão, a
cada vez que o manual muda de versão.* **Foi à mão nesta versão, nas quatro ocorrências.**

> *Não virou `sed` no `subir.sh` de propósito:* **as quatro ocorrências estão em negrito e há um
> `` `v7.9` `` histórico entre crases na mesma página.** *Um `sed` cego que acerte as quatro hoje
> apaga história amanhã, e a 7.3 já grita alto.* **Decisão registrada, não dívida.**

### 4 · As sete marcas de "isto ainda não existe" — cinco assuntos

*O `conferir-voz.py` conta e falha nas duas direções. Dois são grandes:*

- **As três Trilhas do Evocador** — doze entregas preçadas, e o `RASCUNHO-trilhas.md` é a régua.
- **`Sem Técnica`** — precisa de `Estilo da Sombra` **ou** `Aptidão como rota`, e as duas são
  peça própria. **É a nona rota, a única que não fecha ficha.**

E dois médios: o **objeto de apoio** (falta a lista do que conta e o preço) e a **invocação que
não obedece**. *A de `selar com talismã` espera a peça de ferramenta, e não é escolha em aberto.*

> **✔ As duas que o `ESTADO-ATUAL` declarava como trava das Trilhas do Evocador FECHARAM na
> v0.163** — *a vida cheia (descanso longo, derivado da peça 10 §3) e a queda do dono.* **A
> segunda era a que a contagem de marcas não enxergava**, porque não estava escrita em lugar
> nenhum. *Com as duas fechadas, nada de Invocações trava mais as três Trilhas.*

### 5 · Os dois rascunhos

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
- **A BASE do arnês também pula.** *A v0.155 montou uma cópia sem o `.docx` e a v0.160 montou uma
  sem o `.git` da entrega — nas duas o validador saiu `0` tendo pulado a checagem que o arnês
  existia para medir.* **Confira que a checagem RODOU, e não só que a base saiu verde.**
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

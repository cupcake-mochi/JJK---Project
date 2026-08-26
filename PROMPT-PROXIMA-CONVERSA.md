# Retomada — a v0.168 está PELA METADE no disco, e fechar ela é a tarefa

Pasta: `/media/mizuki/HD Externo II/Claude/Claude 2/`
⚠ Trabalhe na pasta PRINCIPAL, não em worktree. **Você não commita** — deixa a mensagem em
`mensagem-de-commit.txt` e avisa. *A entrega, desde a v0.149, o `subir.sh` copia sozinho.*

> ## ⚠⚠ LEIA ISTO ANTES DE QUALQUER COISA
>
> **O último commit é a v0.167.** *A `mensagem-de-commit.txt` que está na raiz é a dela, e ela
> já subiu.* **O disco tem trabalho da v0.168 que NÃO está commitado, e ele deixa o
> `conferir-repositorio.py` com 15 problemas** — então `./subir.sh` **recusa**, que é o
> comportamento certo dele.
>
> **Não desfaça nada.** O que está lá é bom e foi validado; o que falta é a aplicação dele no
> resto do repositório. A lista exata está na seção *"O que falta para fechar a v0.168"*.

Leia primeiro, nesta ordem: `README.md` (a seção *"Nove lições que custaram erro"*),
`sistema/ESTADO-ATUAL.md` **inteiro**, o `logs/CHANGELOG.md` de cima até a v0.160, e então a
**peça 25** (`25-sem-tecnica.md`) e a **peça 20** (`20-tecnica-marcial.md`), que é o molde dela.

---

## O que a v0.168 já tem no disco, pronto e validado

| | |
|---|---|
| **`sistema/03-mecanica/25-sem-tecnica.md`** | a peça, 284 linhas, onze seções |
| **`sistema/03-mecanica/conferir-sem-tecnica.py`** | doze checagens, nenhum valor de regra dentro |
| **o arnês** | 11 casos, 0 divergências, 1 contra-teste verde. *O script está em `/tmp/perturba168.py` e some no reboot — se precisar dele de novo, ele se reescreve em dez minutos* |

**A peça sozinha sai verde.** *`python3 conferir-sem-tecnica.py` → código 0, e as doze rodam.*

## O que falta para fechar a v0.168 — e é só isto

*Os 15 problemas do `conferir-repositorio.py` são todos desta lista.*

1. **As contagens vão de `24` para `25` peças e de `24` para `25` validadores**, em quatro
   documentos: `README.md`, `sistema/ESTADO-ATUAL.md`, `sistema/LEIA-ME.md` e a entrada nova do
   `CHANGELOG`. *Os três primeiros escrevem por extenso — `vinte e cinco`.*
2. **O mapa do `ESTADO-ATUAL` precisa citar a peça 25 e o `conferir-sem-tecnica.py`.**
3. **Duas `PENDENCIA MORTA`:** a peça 1 e a peça 9 têm linhas dizendo que esperam a peça de
   `Sem Técnica`, e ela existe agora. *O `conferir-repositorio.py` nomeia as duas.*
4. **A peça 9** — o §4 e a tabela do §6: a rota vai de `8/9` para **`9/9`**, e a linha dela
   deixa de dizer *"não — falta a peça"*.
5. **A peça 13** — a entrada `Sem Técnica` do catálogo deixa de ser ponteiro e vira a escolha
   da semente, no molde do `Destranca` **de identidade** das quatro configurações do Corpo
   Amaldiçoado.
6. **A peça 22** — o §3.5 fecha (*pacto não concede `Manejo`*) e a linha `um estilo` da tabela
   do §3.3 **dissolve** dentro da linha `um espaço de feitiço` que está logo acima.
7. **A dívida do `espada`, em quatro lugares:** `09-origens.md:147`, `13-legados.md:1035`, e o
   livro em `25-origens.md:396` e `:414`.
8. **O `CHANGELOG`, o bloco do `ESTADO-ATUAL` e a `mensagem-de-commit.txt`.**

> **O capítulo do livro NÃO é da v0.168.** *Ele é texto de mesa, passa pela `REGRA-DE-VOZ`, pelo
> `guard_numeros` e pelos quatro builds — e a peça 20 também fechou antes do
> `42-tecnica-marcial.md` existir.* **Ele é a v0.169**, e com ele fecham a marca do
> `25-origens.md:408` e a contagem da `REGRA-DE-VOZ.md`, de `4` para `3`.

---

## As decisões que a peça 25 encapsula, e de onde cada número saiu

**Todas são do Mizuki, tomadas nesta conversa, com a conta rodada antes.**

### A máquina é o Fundamento, e ela não inventa número

**Molde da peça 20.** *Pontos `3 × Classe`, PE o mesmo número, `1d8` no que sobra, espaços
`2 + (nível ÷ 2)` mais um por marco.* **Dois renomes e uma subtração:**

| slot | Fundamento | Técnica Marcial | **Sem Técnica** |
|---|---|---|---|
| a entrada da lista | `feitiço` | `Kata` | **`Manejo`** |
| Técnica Máxima | — | `Ōgi` | **`Auge`** |
| Liberação Máxima | — | `Ruptura` | **igual, e a peça escreve por quê** |
| Selo · Passivas · Classe 0 | — | Selo vira equipamento | **iguais** |
| Expansão de Domínio | — | não existe | **não existe** |

*O motivo de a `Liberação Máxima` não renomear:* **o argumento da peça 20 era *"esta rota não
tem técnica inata"*, e `Sem Técnica` escreve Fundamento — então ele não alcança ela.**

### A semente, e a banda dela é DERIVADA

**Toda ficha `Sem Técnica` começa com uma aptidão aberta, sem os gates, e ela é o assunto do
Fundamento.** *Ela não gasta marco e conta como a primeira aptidão.*

| Classe Passiva | gate padrão | antecipa, na média das três rotas de marco |
|---|---|---|
| 1 | sem gate | `4,0` |
| **2** | refino 4 · nível 7 | **`9,3`** |
| **3** | refino 7 · nível 13 | **`17,3`** |

> **Banda `CP 2` e `3`: espalhamento `1,86×` — passa. Com a `CP 1` junto: `4,33×` — reprova**,
> contra o filtro de `3,00×`. *A escada de gate **é** a escada de Classe Passiva, então o corte
> é derivado e não escolhido.*

**Três portas:** `Domínio Simples` (a Nova Sombra) · `Energia Reversa` (a rota da Shoko) ·
`Aptidão Própria` (a que você escreve, e a peça 11 §6.7 já a trava em `CP 1 ou 2`).
*A `Pétala` cabe na banda e ficou **declarada** como quarta porta não escrita.*

### O vão, medido

| Caminho | conjura | o dia do feiticeiro | o dia dela | vão | fatias |
|---|---|---|---|---|---|
| Bastião | 48% | `71,6` | `51,0` | `20,6` | **`4,06`** |
| Vanguarda | 67% | `79,8` | `51,0` | `28,8` | **`5,67`** |
| Emanador | 76% | `83,7` | `51,0` | `32,7` | **`6,43`** |

*Sem máquina, a rota vive entre `17,7%` e `51,6%` da Rotina.* **E o vão cresce com o PE do
Caminho, o que quer dizer, derivado: a máquina TEM de gastar PE, senão não é neutra entre os
cinco.** *Uma ação que escala com a Classe e gasta PE na taxa cheia **é** o Fundamento.*

### O buff de cura da rota da Shoko

> **Quem tem a semente `Energia Reversa` soma `1/3 do refino` em toda rolagem de cura.**

*`0,30` fatia no refino 10, que é `0,50×` o `Pulso` — a entrega de nível 19 da `Sutura`.*
**O `+ refino` cheio foi medido e recusado: `0,98` fatia, `1,67×` o `Pulso`, de graça.**
*E ele mora na máquina da rota e não na `Sutura`, porque a peça 9 §1 diz que amarrar número à
Origem cria "a origem certa para cada montagem".*

**A `Liberação` — curar OS OUTROS — fica fora da criação.** *Ela é da Trilha `Sutura`, no nível
11 dela, ao preço de uma Trilha inteira. Na obra só três pessoas conseguem, e o Gojo não é uma.*

---

## ⚠⚠ Três lições que esta conversa pagou, e a terceira é a mais cara

> **1 · Prosa SOBRE a regra não é a regra, e o arnês pegou isso TRÊS vezes no mesmo validador.**
> *A checagem 3 acusava a própria tabela de especificação do §10; a 9 procurava `1/3 do refino`
> na peça inteira, e a §6 cita ele para explicar de onde vem; a 4 aceitava uma célula de tabela
> como argumento.* **É a mesma família da v0.165, e ela reaparece toda vez que um validador lê
> SEÇÃO onde devia ler LINHA DE REGRA.**
>
> **2 · Recorte de seção que casa com o PRÓPRIO cabeçalho devolve um caractere.** *Quatro
> checagens acusaram de uma vez, e nenhuma delas era o defeito.* **Procure o fecho DEPOIS da
> linha do cabeçalho.**
>
> **3 · A triagem de nomes matou o meu próprio exemplo, e ela só conseguiu porque tinha sido
> consertada uma versão antes.** *`Ronda` saía `fraco`, a uma letra de `Onda`. Virou `Redoma`.*

---

## O que a v0.167 e a v0.166 fecharam, e vale saber

**v0.167 — a triagem de nomes era cega para duas coisas.** *Ela lia as 52 armas e **não as treze
categorias**, e a lista de vocabulário dela não tinha `Defesa`, `Aptidão`, `Rotina`, `Sequela`,
`Cicatriz` nem `Bloquear` — que é uma peça inteira.* **Hoje ela deriva as categorias do catálogo
e lê o glossário do livro (`136` termos), as duas com guarda de contagem.** *Três dos cinco
`Estilos da Pegada` estavam batizados duas vezes e viraram `Volteio` · `Couraça` · `Mão Nua`,
sem mover preço.*

> **⚠⚠ E o `ocupados` do `--candidatos` era dict comprehension, então a ÚLTIMA fonte vencia.**
> *Acrescentar fonte mudava em silêncio a razão publicada de todo nome que duas fontes
> reivindicam, e a checagem 12 do `conferir-marcial.py` acusou — ela afirma o **motivo** do
> `OCUPADO`.* **Hoje a primeira vence, e a ordem do `UNIVERSO` é ordem de autoridade.**

**v0.166 — o `Classe 0` parou de curar, e não era mudança de regra.** *A tabela `Cura` do manual
sempre começou na Classe 1; quem abria o buraco era a `Base por Classe`, que juntava
`Cura, Apoio e Onda` numa linha só.* **Um `Classe 0` com Forma `Cura` entregava `27` de cura por
rodada, de graça, em aliado — `1,06` Trilha.** *Manual na v7.17, com build de controle.*

---

## A fila, depois da v0.168

1. **v0.169 — o capítulo do livro de `Sem Técnica`**, com a marca do `25-origens.md:408`
   fechando e a `REGRA-DE-VOZ.md` indo de `4` para `3`.
2. **O `BESTIÁRIO`** — os nove números com quatro donos que montar um inimigo pede.
   *Decisão da v0.161: é **máquina mais maldições prontas**, e não recolhimento puro.*
3. **Duas dívidas que esta conversa achou e não consertou:**
   - **⚠⚠ `08-criacao-de-personagem.md` Passo 1 dá os ofícios ao dono errado.** *Ele diz que a
     **Origem** entrega "dois ofícios livres", e a peça 7 §6 é dona: o **Caminho** dá dois, a
     Origem dá um ou uma perícia. O total `8+3`/`9+2` só fecha pela leitura da 7.*
   - **⚠ A peça 11 §6 justifica *"o refino não escala a `Energia Reversa`"* citando uma §2 que a
     v0.158 substituiu.** *A decisão pode ficar; o argumento caiu há dez versões.*
4. **Três documentos parados na contagem de rotas de antes da v0.122:**
   `08-criacao-de-personagem.md:63`, `sistema/LEIA-ME.md:47`, `livro/HANDOFF-ficha-digital.md:158`.

> **`04-playtest/` continua vazia. Zero sessões desde a v0.1, e todo número do sistema é
> previsão.** *É o maior item aberto do projeto.*

---

## Método, e ele não é negociável

- **Rode os validadores ANTES de mexer em número:** os de `sistema/03-mecanica/`, o
  `conferir-repositorio.py` da raiz, os quatro de `manual/matematica/`, e o `conferir-voz.py
  --estrito` do livro. **Meça pelo CÓDIGO DE SAÍDA**, e confira **`PULADA = 0`**.
- **Todo número novo ganha validador com teste negativo**, em cópia isolada. *Confira que a base
  passa na cópia **e que a checagem nova RODOU** antes de perturbar.* **E confira que a
  PERTURBAÇÃO mudou o arquivo** — `sed` que não bate produz "não acendeu" falso.
- **Uma checagem que só sabe ler a decisão de hoje mede a decisão, não a relação.** *O
  contra-teste que vale reverte a decisão de forma COERENTE em TODOS os donos e sai verde.*
- **⚠⚠ Cuidado com extrator que lê a SEÇÃO quando devia ler a LINHA DE REGRA.** *Mordeu na
  v0.151, na v0.165 e três vezes na v0.168.*
- **Nada de valor fica escrito dentro do validador.** Leia do documento dono.
- **⚠ Marca dentro de célula de tabela quebra extrator de OUTRO validador.** Marca vai embaixo.
- **Antes de batizar:** `python3 conferir-nomes.py --candidatos Nome Outro`. *Ela leva ~21 s.*
- **Pesquise antes de inventar.** Os PDFs estão em `PDFs - Sistemas Extras/PDF_Sistemas/`.
- **Se mexer no livro:** `guard_numeros.py antes.md depois.md` a cada arquivo, com CADA
  diferença lida contra a linha que a carregava, e os **quatro** builds. *Mande o PDF de duas
  colunas antes de ele commitar.*
- **Se mexer no manual:** `node make.js`, `soffice --headless --convert-to pdf`, e **rode o
  controle antes de o build valer.**
- **Escolha de sabor é dele**, em rodadas curtas, com o número e o trade-off já calculados.
  **Mas não pergunte o que a conta responde.**
- **Documento não pode ter cara de saída de IA.** Português informal, nunca de Portugal.

## Onde as coisas moram

| | |
|---|---|
| as peças de regra | `sistema/03-mecanica/` — **25 peças e 25 validadores no disco**, e os documentos ainda dizem 24 |
| o catálogo de entregas | peça 17; os três `DESENHO-*.md` da raiz são os donos do preço |
| a fonte do livro | `sistema/05-material/livro/manual/`, 20 arquivos |
| a régua de escrita | `sistema/05-material/livro/REGRA-DE-VOZ.md` |
| o gerador do manual | `manual/gerador/`, e o `COMO-USAR.txt` é o dono da versão dele |
| a entrega | `finalizado/`, git próprio. **O `subir.sh` copia; o commit é à mão** |

⚠ **Não rode git do sandbox.** Para ver onde a entrega está, leia `finalizado/.git/logs/HEAD`
como arquivo.

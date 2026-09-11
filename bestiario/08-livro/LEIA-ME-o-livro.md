# O livro do Bestiário — como ele se gera

*10/09/2026. **O PDF sai daqui, e nenhum número dele é digitado à mão.***

> ## ⚠ Este projeto NÃO escreve no `Claude 2`.
> **O pipeline foi COPIADO de lá** *(`sistema/05-material/livro/build/`)*, e os scripts que leem o
> repositório só leem.

---

# Como rodar

```
cd 08-livro/build
python3 gerar-tabelas.py     # as tabelas de nível, do dono
python3 gerar-atributos.py   # o orçamento de atributo, dos marcos
python3 gerar-exemplo.py     # o exemplo montado, passo a passo
python3 gerar-as-seis.py     # as seis fichas, da escada viva
python3 build.py             # coluna única
python3 build.py --duas      # duas colunas
```

*E as ferramentas de revisão, do `METODO-passada-de-texto.md`:*

```
python3 medir-voz.py                      # mede contra os 4 manuais do hobby
python3 conferir-voz.py --estrito         # o validador de voz
python3 guard_numeros.py <antes> <depois> # nenhum número de regra pode mudar
```

**Os dois primeiros têm de rodar antes do terceiro.** *Eles injetam conteúdo nos capítulos `6` e `8`,
entre as marcas `<!-- TABELAS -->` e `<!-- FICHAS -->`.*

| saída | páginas |
|---|---|
| `Projeto-M-Bestiario.pdf` | `53` — coluna única |
| `Projeto-M-Bestiario-duas-colunas.pdf` | `30` — duas colunas |

---

# De onde sai cada coisa

| o quê | dono |
|---|---|
| a paleta, a tipografia, a capa, o índice de borda | `bestiario.css` — **cópia do `manual.css`** do Manual da Guilda |
| as tabelas de nível do capítulo `6` | **`04-fase-1/TABELA.md`**, por `gerar-tabelas.py` |
| as seis fichas do capítulo `8` | **`fila/DECIDIDO-as-seis-prontas.md`** + **`TABELA.md`** + a ficção do `dados.js`, por `gerar-as-seis.py` |
| o texto dos capítulos `1` a `4` | reescrito de `07-catalogo/`, em voz de livro |
| o texto dos capítulos `5` a `7` | reescrito de `03-bloco/RASCUNHO-5` e da fila |

> ### ⚠ Os dois geradores MORREM se o dono mudar.
> *`gerar-tabelas.py` confere que a escada colapsa em faixa — se ela deixar de colapsar, a tabela
> impressa seria mentira e o script para.* **`gerar-as-seis.py` confere que a faixa de cada ficha é
> constante, e que a categoria dela existe na escada viva.**

---

# A voz

**A régua é a `REGRA-DE-VOZ.md` do Manual da Guilda**, e o Bestiário segue ela. *As linhas que mais
pesaram aqui:*

| a régua | o que ela cortou deste livro |
|---|---|
| **o livro não fala de si mesmo** | data, caixa de correção, "o que este arquivo achou", referência a arquivo interno |
| **por que o NÚMERO é assim também sai** | a justificativa de calibragem. *A medida fica; a conta que produziu ela mora na fila* |
| **título é o nome da coisa** | `17` títulos que eram frase ou pergunta viraram nome |
| **na dúvida, corta** | — |

## ⚠ E uma régua a mais, pedida por ele: escrita em ANTÍTESE

***Palavras dele:*** *"evitando escrita em antítese e outros meios que uma IA escreveram por comum."*

**O documento de trabalho escreve assim de propósito** — *"não é erro de conta, é ficha de livro"* —,
**e o livro não pode.** *Medido com detector largo, nos dois:*

| | palavras | ocorrências | por mil |
|---|---|---|---|
| o catálogo *(documento de trabalho)* | `6.786` | `38` | `5,6` |
| **o livro** | `8.925` | `36` | **`4,0`** |

**E o tique de assinatura — `não é X. É Y` — caiu de `13` para `4`.**

> ⚠ **O detector super-conta, e isso está medido:** *dos `7` casos de `X, e não Y` que sobraram no
> livro, `5` são desambiguação factual* — *"exige dez personagens, e não quatro"*, *"as oito ações do
> esquadrão, e não a de um corpo"*. **Esses ficam: tirar eles apagaria informação.**

---

# O que o livro NÃO tem, e é de propósito

| | por quê |
|---|---|
| **papel nas seis fichas** | o martelo de 10/09 não atribuiu nenhum, e papel multiplica vida |
| **arte de capa** | o `build.py` avisa e sai sem ela. *Ponha um `arte/Capa-v0.1.jpg` e ele usa* |
| **as `Intervenções` escritas** | o capítulo `5` dá o molde das três; escrever cada uma é do mestre |
| **ficha de lugar** | decidido em `fila/DECIDIDO-o-lugar-nao-vira-peca.md` |

---

# ⚠ O que muda quando o `Claude 2` receber os commits

**Nada neste livro.** *Ele já lê a escada VIVA, e o `bloco-de-inimigo.docx` do repositório é que
está na escada morta.*

> ### ⟹ Este PDF supera o `bloco-de-inimigo.docx` enquanto o commit `C` do `PARA-O-CLAUDE-2.md`
> ### não entrar.
> *Depois que entrar, os dois passam a dizer a mesma coisa — e aí vale decidir qual dos dois fica.*

---

# A passada de texto de 10/09 — pelo `METODO-passada-de-texto.md`

**O método é do `Claude 2`** *(`sistema/05-material/livro/METODO-passada-de-texto.md`)*, e as três
ferramentas dele foram copiadas pra `build/`: **`medir-voz.py`** *(mede)*, **`conferir-voz.py`**
*(valida)* e **`guard_numeros.py`** *(guarda os números)*.

> ### O método é explícito: o script MEDE, o documento JULGA.
> *"Número alto NÃO é ordem de corte."* **Antes de cortar numa marca, leia uma amostra dela.**

## O que o validador achou, e o que ficou

| checagem | antes | depois |
|---|---|---|
| **ARTIGO** — título começa com artigo | `30` | ### **`0`** |
| **PERGUNTA** — título é pergunta | `6` | **`0`** |
| **FRASE** — título é frase, não nome | `3` | **`0`** |
| **CONTAGEM** — contagem por extenso no título | `5` | **`0`** |
| **TABELA-VAGA** — cita tabela sem nome próprio | `4` | **`0`** |
| **TABELA-SEM-NOME** | `0` | **`0`** |
| **MOLDURA** — o texto fala do próprio livro | `13` | ⚠ **`3`** |
| **termos sem destino** | `9` | ### **`0`** |
| ### TOTAL | ### `61` | ### **`3`** |

> ### ⚠ Os `3` de `MOLDURA` que ficaram são os AUTORIZADOS, e estão todos na abertura.
> **A `REGRA-DE-VOZ.md` dá à moldura de leitura exatamente um lugar:** *"A moldura de leitura vive
> **uma vez**, na introdução, na seção `Organização do manual`. Dentro do capítulo, nunca."*
> ⟹ *os `10` que estavam DENTRO de capítulo saíram; os `3` da introdução ficam por régua.*

## 🆕 E os `9` termos órfãos abriram um capítulo que faltava

**`FERRAMENTA` · `PADRÃO` · `REGRA` · `Capanga` · `Ameaça` · `Desastre` · `Emboscador` · `Grande` ·
`Cortina`** *passavam o corte de `5` usos ou `3` capítulos e não tinham destino.*

> **É o caso do `colado`** — *uma leitora do playtest travou num termo cuja definição estava seis
> palavras adiante, porque nada ali dizia que aquilo era uma definição.*

**Duas coisas consertaram os nove:**

| | |
|---|---|
| **`1`** | os três pesos trocaram **ponto por travessão** — *`**\`REGRA\`.** A mesa segue` ⟹ `**\`REGRA\`** — a mesa segue`.* **A régua é explícita: com ponto, abre bloco sobre coisa conhecida; com travessão, apresenta coisa nova** |
| **`2`** | 🆕 **entrou o `07-vocabulario.md`** — *`7` tabelas, `35` termos, cada um com o capítulo que o explica* |

⚠ **O validador só lê linha de vocabulário de arquivo que comece com `07-`.** *Foi ele que apontou
que o livro não tinha um.*

## O que a MEDIDA disse, e o que eu NÃO fiz por causa dela

*Medido contra os quatro manuais do hobby — PHB 2024, Tasha, Guia do Mestre, GURPS 4e.*

| marca | a faixa dos quatro | o nosso | o que eu fiz |
|---|---|---|---|
| `não é X, é Y` | `0,0`–`0,1` | ### **`0,0`** | ✅ o tique de assinatura não existe mais |
| **`, e não`** | `0,1`–`1,7` | ⚠ **`11,3`** | ⚠ **`2` enfeites saíram; os `7` de regra ficaram** |
| `em vez de` | `0,1`–`6,9` | `8,0` | ❌ nada — *o método já fechou: "`em vez de` fica"* |
| analogia | `3,7`–`6,2` | ⚠ `1,6` | ➕ `1` onde ela paga o lugar. *Não enchi pra bater número* |
| equação | `1,2`–`4,7` | `6,4` | ❌ nada — *`4` ocorrências cruas, e "corpo pequeno mente"* |
| palavras por frase | `17`–`23` | ⚠ `12` | ➕ juntei a abertura do cap. `6`, que estava picotada |

### ⚠⚠ Por que o `, e não` a `11,3` fica, sendo `6,6×` o topo dos quatro

**O método avisa em seção própria:** *"Ele mede altíssimo e quase nunca é para cortar […]
**Cortar ali apaga regra.**"*

**Li as `9` ocorrências, uma a uma, como ele manda. `7` são regra ou fato:**

| | |
|---|---|
| ❌ enfeite, e saiu | *"serve para conversar sobre o bicho, e não para arquivar ele"* · *"A escola foi o palco dela, e não o berço"* |
| ✅ **regra, e fica** | *"exige dez personagens, e não quatro"* · *"quantas vezes ele age, e não quantas coisas estão escritas nele"* · *"as oito ações do esquadrão, e não a de um corpo"* · *"exige perto de cinco pessoas, e não quatro"* |
| ✅ fato de canon, e fica | *"de grau especial, e não como feiticeiro"* |
| ✅ instrução, e fica | *"Narre junto, e não confunda uma com a outra"* |
| ✅ falso positivo | *"e não confirma nem nega"* |

### E o `12` palavras por frase é ESTRUTURAL, não descuido

**O livro é feito de entrada de catálogo em quatro camadas**, e a régua manda escrever a camada do
efeito em `4` a `6` palavras e a da regra em `15` a `21`. *Os quatro manuais do hobby são mais
narrativos que isso por natureza.* **Varri os trechos com `3` frases curtas seguidas e li os `28`:
`27` são as quatro camadas funcionando.** *O único picotado de verdade era a abertura do `6`.*

## Os números, conferidos

**`guard_numeros.py` rodado nos `9` arquivos mexidos.** *Nenhum número de regra se moveu.*

| a diferença | a explicação |
|---|---|
| `três` · `quatro` · `sete` · `duas` · `dois` **sumiram** | saíram todos de **título**, pela regra `CONTAGEM` — *"entra uma perícia nova e o título mente"*. ⚠ *conferido: o `sete` continua `3×` no corpo do `40`* |
| `uma` oscilou | **artigo**, e o guarda não distingue artigo de numeral |
| `2` e `5` sumiram do `80` | eram **ponteiro por posição** *("a tabela do Passo `2`")*, trocados por ponteiro por **nome**. ✅ *E o `Passo 2` e o `capítulo 5` voltaram como texto, senão o leitor perdia o endereço* |
| `6` apareceu no `80` | o endereço novo — *"no Passo 2 do capítulo 6"* |

> ### ⚠ O snapshot de antes fica em `build/.antes/`.
> *É a linha de base do `guard_numeros.py`.* **Refaça ele antes da próxima passada.**


---

# A segunda passada — "falta algo nesse livro?"

*Rodada logo depois da primeira, e ela achou mais que a primeira.*

## 🔴 O defeito que o livro estava publicando

> ### O capítulo `6` imprimia o golpe CRU e, três seções abaixo, o orçamento COM o fator `0,923`.
> **As duas colunas se desmentiam em `8,3%`.**

*A `TABELA.md` publica o golpe **sem** o fator da `Intervenção` — o Sukuna, que foi o teste de ponta
a ponta, aplica ele por cima (`294 × 0,923 = 271`).* **O livro imprimia a tabela e nunca mandava
aplicar.**

| | golpe que o livro imprimia | golpe de verdade | o orçamento que o livro publicava |
|---|---|---|---|
| `Desastre` nv`30` | `73,0` | **`67,4`** | `15,0` — *que é `67,4 ÷ 4,5`* |

**Um mestre que fizesse `73 ÷ 4,5` achava `16,2`, e a tabela de baixo dizia `15,0`.**

✅ **Consertado:** *aviso na própria tabela de golpe, e o exemplo montado exercita a conta.*

## 🔴 E o que o livro não ensinava

| o buraco | o tamanho |
|---|---|
| ### **atributos e Testes de Resistência** | **`9` células do bloco sem uma linha de instrução.** *E o texto já estava aprovado por ele em 10/09, com a nota "vai pro capítulo do Bestiário como está"* |
| **nenhum exemplo montado** | o checklist pede *"a conta inteira, passo a passo"* e *"com nome próprio"*. **O encaixe `Exemplo` tinha zero usos** |
| **nenhuma referência rápida** | o checklist pede *"uma tabela de referência rápida de uma página"* |
| `personagens = fator × 4` | a identidade que torna o fator legível, e ela não estava escrita |

**Entraram:** *a seção `Atributos` no capítulo `5`* · *o **Ubume**, exemplo montado nv`10` no capítulo
`6`* · *o capítulo `9`, `Referência rápida`*.

> ### ⚠ O `Ubume` exercita de propósito o que as seis prontas NÃO exercitam:
> **um `papel`** *(as seis não têm nenhum)* · **o fator `0,923`** · **um tamanho acima de `Médio`**.
> *E ele fecha em `5,1` pontos, que é exatamente a linha do `Desastre` na tabela de orçamento.*

## A cobertura, medida

**`29` decisões do projeto conferidas contra o livro, uma a uma.** *`24` estavam lá, `2` eram falso
negativo do regex, e `3` faltavam de verdade.*

## E as referências cruzadas

**`20` referências a capítulo, e `0` apontam pra capítulo que não existe.** ⚠ *Uma era falso
positivo — "capítulo `178`" é do mangá, e virou "capítulo `178` do mangá" pra não colidir com a
numeração do livro.*

## ⏳ E sobrou um martelo dele

> ### O `Tsuchigumo` e o `Oni` são `Desastre`, e `Desastre` carrega `Intervenção`.
> **Nenhuma das duas tem as três escritas, e por isso as duas usam o golpe cru.** *O livro declara
> isso no capítulo `8`.*
>
> ⟹ **Ou elas ganham as `Intervenções` e pagam o `0,923`** *(o golpe cai `8,3%`)*, **ou ficam como
> estão e a categoria delas fica sem uma das características.** *É escolha de sabor, e é dele.*

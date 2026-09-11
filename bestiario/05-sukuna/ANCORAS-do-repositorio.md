# Âncoras do repositório — para a ficha do Sukuna

**Lido em:** 2026-09-10
**Repositório lido (só leitura):** `/media/mizuki/HD Externo II/Claude/Claude 2`
Nada foi escrito no repositório de origem.

> ## Divergência entre as duas cópias: NÃO EXISTE
> Comparei os 26 arquivos `.md` de `sistema/03-mecanica/` com os 26 de `finalizado/regra/` byte a byte (`diff -q`, arquivo por arquivo). **Os 26 deram IGUAL.**
> As datas de modificação diferem (o `finalizado/` costuma ser minutos ou horas mais novo), mas o **conteúdo é idêntico**. Então tanto faz qual você abre.
> Neste documento eu cito sempre o caminho de `sistema/03-mecanica/`.

> ## Achado grande: o "Fundamento" é o MANUAL
> Eu procurei uma peça chamada Fundamento e ela não existe em `03-mecanica/`. **O Fundamento é o nome do próprio manual**: `manual/Fundamento-MANUAL-v7.docx` e `.pdf`.
> O `.docx` é **gerado por código**, não escrito à mão. A fonte de verdade é `manual/gerador/*.js` (`partA.js` a `partF.js`), montada por `make.js`.
> Então quando as peças dizem "o manual", o dono literal é um desses `.js`. É de lá que eu tirei tudo o que está marcado como "manual" abaixo.
>
> *(Cuidado com o vocabulário: dentro do manual, "Fundamento" também é o nome da **técnica inata do personagem** — a Regra dele, com três Famílias Fechadas. Os dois sentidos convivem.)*

---

> **⚠ Ordem das seções:** eu fui salvando conforme achava, então os itens **6, 7 e 8 estão DEPOIS dos itens 9 e 10** no arquivo. A ordem de leitura é: 1, 2, 3, 4, 5, 9, 10, 6, 7, 8, e aí os dois bônus e o fecho. Todos os dez estão aqui, nenhum ficou de fora.
>
> **Índice:** 1 ponto→dado · 2 régua de condição · 3 as treze condições · 4 o Fundamento e a área · 5 as Classes e o teto do nível 20 · **9 tabela Inimigos** · **10 Estilhaço** · **6 Pacto** · **7 resistência/imunidade** · **8 Expansão de Domínio** · bônus: categoria e ficha de 17 linhas · fecho: o Sukuna nv 20 · o que NÃO abriu

## Tabela grande — âncora | valor | dono

| âncora | valor | dono (arquivo §seção) |
|---|---|---|
| **ponto de feitiço → dado** | cada ponto que não vira Melhoria vira `1d8` de dano, que são `4,5` | `sistema/03-mecanica/19-dano-e-condicoes.md` §2.1 |
| **preço de tier, em fatia da Rotina** | `Leve` = `1/7` · `Média` = `2/7` · `Pesada` = `3/7` | `19-dano-e-condicoes.md` §2.1 |
| preço de tier em dano/rodada (nível 30) | `15,43` · `30,86` · `46,29` | `19-dano-e-condicoes.md` §2.1 |
| **preço de Melhoria por degrau** | `Leve` = metade da Classe · `Média` = a Classe inteira · `Pesada` = Classe e meio — **sempre arredondando pra cima** | `manual/gerador/partD.js` §3 (Melhorias, texto de abertura) |
| exemplo do manual, Classe 3 | Leve `2` · Média `3` · Pesada `5` | `manual/gerador/partD.js` §3 |
| exemplo do manual, Classe 5 | Leve `3` · Média `5` · Pesada `8` | `manual/gerador/partD.js`, "As condições, uma a uma" |
| **Melhoria `Condição`** | o custo é **o nível da condição** (Leve/Média/Pesada). **Dura uma rodada.** | `manual/gerador/partD.js`, família Controle |
| tirar condição de alguém | `1` ponto de energia **por nível** | `manual/gerador/partD.js`, "As condições, uma a uma" |
| **vantagem / desvantagem** | `25` pontos percentuais | `19-dano-e-condicoes.md` §2.2 (dono citado: peça 11 §8) |
| **dano evitado** | converte `1` pra `1` | `19-dano-e-condicoes.md` §2.2 (dono citado: peça 5 §4) |
| ações do chefe por rodada | `3` — piso da régua | `19-dano-e-condicoes.md` §2.2 — **esta peça é dona**; o manual diz o contrário |
| filtro de dominância do projeto | reprova a partir de `3,00×` | `19-dano-e-condicoes.md` §2.1, §2.2, §3.6 |
| a fatia | `5,08` de dano por rodada | `DESENHO-trilhas.md`, linha de orçamento de Trilha (citado em `19` §2.2) |
| **Classe 1** | `3` pontos · `3` PE — o menor do manual | `manual/gerador/partF.js` §10 e `partA.js` (tabela mestra) |
| **fórmula da Classe** | **`Pontos = 3 × Classe`** · **`Custo em PE = 3 × Classe`** | `manual/gerador/partA.js`, caixa de fórmulas |
| **escada de Classe, completa** | 1→`3` · 2→`6` · 3→`9` · 4→`12` · 5→`15` · 6→`18` · 7→`21` | `manual/gerador/partA.js`, tabela mestra (os sete, literais) |
| **Classe no nível 20** | **Classe 5 = `15` pontos · `15` PE** (a 5 abre no 17; a 6 só no 21) | `partA.js` tabela mestra (coluna Nível) + `partE.js` §9 |
| **teto de dados no nível 20** | `4 × Classe` = **`20` dados** (`20d8 = 90`) | `partA.js` caixa de fórmulas + tabela mestra, coluna Teto |
| dano cheio num alvo, nível 20 | `15d8 = 67` | `partA.js` tabela mestra |
| Técnica Máxima no nível 20 | `24d8 = 108`, custando `5 ×` a maior Classe em PE | `partF.js` "A curva" + `partA.js` "Energia" |
| teto de Melhorias por feitiço | `2` nas Classes 1–2 · `3` nas 3–4 · **`4` da Classe 5 em diante**. Restrições: até `2`. A Forma não conta. | `partA.js` "Quantas Melhorias cabem" + `partE.js` §8 regra 3 |
| teto de devolução de Restrição | `2 × Classe` (nível 20: `10`) | `partA.js` caixa de fórmulas + `partE.js` §8 regra 4 |
| **preço de Forma de área** | **`Cone`, `Linha` e `Explosão` (esfera) custam TODOS `Leve`** — o sistema não separa por formato | `manual/gerador/partC.js`, tabela "Formas" |
| Formas de graça | `Projétil`, `Toque`, `Apoio`, `Efeito` | `partC.js`, tabela "Formas" |
| **categoria do inimigo** | `Ronda` ×0,25 (1 pessoa, 1 ação) · `Dupla` ×0,50 (2, 1) · `Alcateia` ×1,00 (4, 3) · **`Calamidade` ×1,50 (6, 5 ações)** | `sistema/03-mecanica/26-bestiario.md` §4 |
| **`Calamidade` no nível 20** | **`990` vida · `220` dano/rodada · `5` ações** | `26-bestiario.md` §4.1 |
| derivadas no nível 20 | Defesa `18` · acerto `+8` · CD `16` · refino `7` | `26-bestiario.md` §3.1 |
| **pactos permanentes** | metade da Essência, arred. pra baixo (Essência `6` → `3`) | `sistema/03-mecanica/22-pactos.md` §3.1 |
| **teto por pacto** | `0,50` fatia = `2,54` de dano/rodada = `21%` de um golpe simples | `22-pactos.md` §3.2 |
| **resistência custa degrau** | `Físicos` = `1` degrau · `Elementais` = meio · `Especiais` = nada | `26-bestiario.md` §6.3 |
| imunidade a `Físicos` | `2,50×` de vida efetiva — custa **mais de um degrau**, e a escada não vende acima da `Calamidade` | `26-bestiario.md` §6.3 |
| **Expansão de Domínio do inimigo** | **DOBRA quantos personagens ele exige** — o fator é `1 ÷ 0,52 = 1,92×`, que arredonda pra `2` | `26-bestiario.md` §6.4 |
| `Calamidade` com Expansão | exige **`12`** feiticeiros | `26-bestiario.md` §6.4 |
| **tabela "Inimigos", nível 20** | grupo `~220`/rodada · **chefe vida `600 a 720`** · **chefe dano `147`** · capanga vida `165` · capanga dano `49` | `manual/gerador/partF.js` §11 "Para o mestre" › "Inimigos" |
| Integridade do inimigo | igual à vida máxima dele | `partF.js` §11 "Inimigos" |
| **`Estilhaço`** | Melhoria **`Leve`**, família **Castigo** → metade da Classe, arred. cima (Classe 5 = `3` pontos) | `manual/gerador/partD.js`, família Castigo |

*(itens 6, 7, 8 e o preço de Área entram nas seções abaixo)*

---

## 1. PEÇA 19 §2.1 — ponto de feitiço vira dado

**Arquivo:** `/media/mizuki/HD Externo II/Claude/Claude 2/sistema/03-mecanica/19-dano-e-condicoes.md`
**Seção:** `### 2.1 O teto sai do manual, e ele é plano` (título na linha 31; a frase está na linha 33)

A citação, inteira:

> **O manual compra condição com ponto de feitiço, e cada ponto que não vira Melhoria vira `1d8` de dano — que são `4,5`.** *Quando esta régua foi feita, na v0.103, o manual vendia condição em dois pacotes: `Condição Menor` custava `Média` e `Condição Maior` custava `Pesada`.* **Então ele sempre disse, em dano, quanto achava que uma condição valia — e é dessa tabela de preço que as bandas saem.**

### O contexto dela

Logo depois vem a tabela que ela usa. Esta é a tabela de preço da condição por Classe, e ela é do §2.1:

| Classe | `Leve` | `Média` | `Pesada` | Rotina | `Média` / Rotina | `Pesada` / Rotina |
|---|---|---|---|---|---|---|
| 1 | 1 | 1 | 2 | 3 | 33,3% | 66,7% |
| 2 | 1 | 2 | 3 | 7 | **28,6%** | **42,9%** |
| 3 | 2 | 3 | 5 | 10 | 30,0% | 50,0% |
| 4 | 2 | 4 | 6 | 14 | **28,6%** | **42,9%** |
| 5 | 3 | 5 | 8 | 17 | 29,4% | 47,1% |
| 6 | 3 | 6 | 9 | 21 | **28,6%** | **42,9%** |
| 7 | 4 | 7 | 11 | 24 | 29,2% | 45,8% |

E a conclusão que a peça tira dela, literal:

> **Nas Classes pares a razão é exata: `Média` é `2/7` da Rotina e `Pesada` é `3/7`.** *Nas ímpares o arredondamento do manual oscila, e nunca mais que `1,4` ponto percentual — fora a Classe 1, que é pequena demais para arredondar bem.*

> **`Leve` = `1/7` da Rotina · `Média` = `2/7` · `Pesada` = `3/7`.**
> **No nível 30, com a Rotina em `108`: `15,43` · `30,86` · `46,29` de dano por rodada.**

E o aviso que vem colado, que muda o que a régua faz:

> **Esses três números são o PREÇO, e não o teto.** *Eles dizem o que você deixa de causar por ter gasto aqueles pontos numa condição em vez de num dado.*

> ***⚠⚠ Até a v0.200 eles eram também o teste, e isso quebrou na v0.201.*** *A régua comparava o valor da condição com o preço dela e reprovava quem passasse.* **Mas o valor de uma condição é uma fatia da rodada do INIMIGO e o preço é uma fatia da sua** — os dois só empatam enquanto o inimigo e você entregarem a mesma coisa por rodada. *Com o chefe da tabela nova entregando `219` contra uma Rotina de `108`, oito das treze passavam do próprio preço e a `Média` esvaziava.*
>
> ***Decisão do Mizuki: não repreçar, e trocar o que a régua mede.*** *"Tem que considerar que o boss também vai poder aplicar condições."* **A régua passou a ter duas perguntas separadas, e nenhuma delas é "cabe embaixo do preço":**
>
> **1. O NÍVEL da condição é quantas ações da rodada do alvo ela nega** — *meia ação é `Leve`, uma é `Média`, uma e meia é `Pesada`*. **Isso não depende de contra quem ela cai, e é por isso que a mesma tabela serve quando o chefe usa condição num personagem.**
>
> **2. O TESTE é de dominância** — *quanto ela nega, dividido pelo dano que aqueles mesmos pontos de feitiço dariam*, contra o filtro de `3,00×` que o projeto usa em todo catálogo.

**Pro Sukuna isso importa:** a mesma tabela serve quando o chefe joga condição no jogador. Está escrito.

---

## 2. PEÇA 19 §2.2 — a régua de condição

**Arquivo:** `sistema/03-mecanica/19-dano-e-condicoes.md`
**Seção:** `### 2.2 O que cada condição entrega, medido` (linha 64)

### 2a. O preço em ponto de feitiço por degrau

**Cuidado:** a peça 19 §2.1 traz a tabela de preço **em ponto de feitiço, por Classe** (a de sete linhas acima). O manual escreve a mesma coisa como regra, e a regra é mais curta. Do `manual/gerador/partD.js`, abertura da seção 3:

> Sessenta e seis Melhorias, em nove Famílias. O preço de cada uma depende da Classe do feitiço em que ela entra: **Leve** custa metade da Classe, **Média** custa a Classe inteiro, **Pesada** custa Classe e meio — sempre arredondando pra cima.

> Exemplo de leitura: num feitiço de Classe 3, uma Leve custa 2 pontos, uma Média custa 3 e uma Pesada custa 5. Nas suas duas Famílias Livres, tire metade da Classe do preço, com mínimo de 1; nas três Fechadas, não há o que comprar.

E na subseção "As condições, uma a uma", também do `partD.js`:

> São treze, e cada uma tem um **nível**: Leve, Média ou Pesada. O nível faz duas coisas ao mesmo tempo — é o **preço** da Melhoria Condição que aplica ela, e é o que custa em energia pra **tirar** ela de alguém (1 ponto por nível). Uma condição dura uma rodada.

> As três tabelas abaixo são as treze separadas por nível. Numa Classe 5, por exemplo, aplicar uma Leve custa 3 pontos, uma Média custa 5 e uma Pesada custa 8.

**As duas fontes batem.** A tabela da peça 19 §2.1 é o arredondamento explícito dessa mesma regra, Classe por Classe.

### 2b. A tabela de âncoras do §2.2 — colada inteira

É aqui que moram a vantagem e o dano evitado que você pediu. Literal:

> **Nenhum componente desta conta é escolha.** *Cada um sai de um documento dono, e o `conferir-dano.py` lê os números de lá em vez de guardar cópia.*

| âncora | valor | dono |
|---|---|---|
| a fatia | `5,08` de dano por rodada | `DESENHO-trilhas.md`, a linha de orçamento de Trilha |
| a Rotina no nível 30 | `108` | manual, a tabela de Rotina |
| chefe e capanga no nível 30 | `219` e `73` por rodada | manual, a tabela de inimigo |
| ações do chefe por rodada | o piso da banda, derivado logo abaixo | **esta peça** — o manual diz o contrário |
| **vantagem e desvantagem** | **`25` pontos percentuais** | **peça 11 §8** |
| `1` ponto percentual na rolagem de um aliado | `0,230` | `DESENHO-caminhos.md`, a régua do Guia |
| a ação de atacar de um aliado | `23,00` — dois golpes simples | `DESENHO-caminhos.md` |
| mover `1,5 m` | `0,90`, então `1 m` vale `0,60` | peça 5 §4 |
| `1` ponto de arma | `0,33` por rodada | peça 14 §4 |
| o fundo de uma arma de duas mãos | `5` pontos | peça 14 §5 |
| **dano evitado** | **converte `1` pra `1`** | **peça 5 §4** |
| o `20` natural, e a chance dele | `5%` | peça 1 §5.2 |
| **o escopo do crítico** | dobra **só os dados do que rolou o acerto** | peça 1 §5.2 |
| o dado do soco no teto | `d10`, então `5,5` | peça 14 §5.0.6 |

### 2c. As ações do chefe — o `3`

> **⚠ A linha das ações do chefe mudou de dono na v0.198, porque a antiga citava uma frase que diz o contrário dela.** *Ela publicava `3`, contra um grupo de quatro, com o dono no manual pelo `DESENHO-trilhas.md`.* **O manual escreve que o chefe *"perde a ação três vezes por rodada"*** — ele age uma vez enquanto o grupo de quatro age quatro, e é dessa perda que sai a exigência de `3` a `4×` a vida do grupo que a tabela de inimigo cumpre. *Contagem de ação nunca esteve ali.*

> **O chefe age `3` vezes por rodada, e esse número é o piso desta régua.**

Tabela de sensibilidade, literal:

| ações do chefe | `Lento`, `Leve` | `Calado`, `Média` | `Enfeitiçado`, `Média` | `Atordoado`, `Pesada` |
|---|---|---|---|---|
| `1` | `6,23×` | `6,95×` | `6,95×` | `6,64×` |
| `2` | `3,19×` | `3,48×` | `3,48×` | `3,32×` |
| **`3`** | **`2,18×`** | **`2,32×`** | **`2,32×`** | **`2,21×`** |

### 2d. Duração — a condição dura UMA rodada

> **⚠ A régua mede a rodada em que a condição está ativa, e a condição dura UMA.** *A Melhoria `Condição` do manual escreve isso na própria célula — "Dura uma rodada" —, e nenhuma das Melhorias que mexem em tempo estende ela.* **Então um `Impedido` vale `132,15` na rodada dele e `44,05` espalhado numa luta de `3` rodadas**, que é `20%` do que um chefe faz.

E a nota que fecha a porta pra `Resistência Lendária`:

> *Isto entrou na v0.199, e entrou porque a falta dele produziu um erro:* **a régua foi lida como se a condição durasse a luta**, e daí saiu um diagnóstico de que o chefe precisava de proteção contra condição no molde da `Resistência Lendária` do 5e. **Ele não precisa** — *o sistema já resolve pelo relógio, e a duração morava só na célula do manual.*

### 2e. As treze medidas num chefe, nível 30 — a tabela do §2.2

| condição | nega por rodada | ações negadas | pontos | contra o dano deles | nível |
|---|---|---|---|---|---|
| **`Impedido`** | `132,15` | `1,5` + deslocamento + aliados | `11` | `2,67×` | `Pesada` |
| **`Cego`** | `126,75` | `1,5` + aliados | `11` | `2,56×` | `Pesada` |
| **`Amedrontado`** | `114,90` | `1,5` + deslocamento | `11` | `2,32×` | `Pesada` |
| **`Envenenado`** | `109,50` | `1,5` | `11` | `2,21×` | `Pesada` |
| **`Atordoado`** | `109,50` | `1,5` | `11` | `2,21×` | `Pesada` |
| **`Calado`** | `73,00` | `1` | `7` | `2,32×` | `Média` |
| **`Enfeitiçado`** | `73,00` | `1` | `7` | `2,32×` | `Média` |
| **`Lento`** | `39,20` | `0,5` + deslocamento | `4` | `2,18×` | `Leve` |
| **`Derrubado`** | `8,45` | `0` | `4` | `0,47×` | `Leve` |
| **`Agarrado`** | `5,40` | `0` | `4` | `0,30×` | `Leve` |
| **`Incapacitado`** | `4,95` | `0` | `4` | `0,28×` | `Leve` |
| **`Desarmado`** | `3,45` | `0` | `4` | `0,19×` | `Leve` |
| **`Surdo`** | `0,00` | `0` | `4` | `0,00×` | `Leve` |

> **Seis `Leve`, duas `Média`, cinco `Pesada` — os mesmos treze níveis de antes da v0.201, e nenhum preço se moveu.**

> **A coluna das ações é quem decide o nível, e ela não olha o alvo.** *Desvantagem nega metade da rodada, e metade de três ações é uma e meia — é por isso que o `Envenenado` cai no mesmo degrau do `Atordoado` sem tirar ação nenhuma.*

**Isso é útil pro Sukuna:** desvantagem = metade da rodada. Com o chefe em 3 ações, isso é 1,5 ação.

### 2f. Duas convenções de contagem de aliado

> **Benefício que só o corpo a corpo colhe conta UM aliado.** *É a leitura do `Abalo`, a Manha da Massa.*
> **Benefício que qualquer atacante colhe conta TRÊS.** *É a leitura do `Estampido`, a Manha da Arma de Fogo, que supõe mesa de quatro.*

---

## 3. As treze condições, por degrau

Duas fontes, e **elas batem**. A peça 19 §3 é a versão longa; o `manual/gerador/partD.js` é a versão do livro. Cito a peça 19, que é mais completa.

**Dono:** `sistema/03-mecanica/19-dano-e-condicoes.md` §3.1, §3.2, §3.3 (linhas 243–290)
**Espelho:** `manual/gerador/partD.js`, seção "As condições, uma a uma"

### As seis `Leve` (§3.1)

| condição | nível | o que faz |
|---|---|---|
| **`Lento`** | `Leve` | seu deslocamento cai pela metade e você não usa Ação Bônus |
| **`Incapacitado`** | `Leve` | **você não pode `Bloquear`, e todo ataque corpo a corpo que acertar você é crítico** — *só ele: ataque de conjuração e ataque à distância não, e o feitiço de Toque é de conjuração mesmo encostado em você* |
| **`Derrubado`** | `Leve` | você está no chão. Só se move rastejando, tem desvantagem nos seus ataques, e quem ataca você **a até 1,5 m tem vantagem** — quem ataca de longe tem desvantagem |
| **`Agarrado`** | `Leve` | seu deslocamento é `0`. Acaba se quem agarrou ficar `Incapacitado`, ou se alguma coisa tirar você do alcance dele |
| **`Desarmado`** | `Leve` | a sua arma está no chão ou na mão de outro. Você bate desarmado até pegar de volta |
| **`Surdo`** | `Leve` | você não ouve. Falha automático em teste que precise de audição, e **`−2` na iniciativa** |

### As duas `Média` (§3.2)

| condição | nível | o que faz |
|---|---|---|
| **`Calado`** | `Média` | você não conjura. Nada que precise de voz, gesto ou Selo sai |
| **`Enfeitiçado`** | `Média` | você não ataca quem enfeitiçou nem mira efeito nocivo nele, e ele tem vantagem em teste social contra você |

### As cinco `Pesada` (§3.3)

| condição | nível | o que faz |
|---|---|---|
| **`Impedido`** | `Pesada` | seu deslocamento é `0`, você tem desvantagem nos seus ataques e no Teste de Resistência Físico, e quem ataca você tem vantagem |
| **`Cego`** | `Pesada` | você não enxerga. Falha automático em teste que precise de vista, tem desvantagem nos seus ataques, e quem ataca você tem vantagem |
| **`Amedrontado`** | `Pesada` | desvantagem em ataque e teste enquanto enxergar a fonte do medo, e você não se aproxima dela de vontade própria |
| **`Envenenado`** | `Pesada` | desvantagem nos seus ataques e em todo teste de perícia |
| **`Atordoado`** | `Pesada` | **você perde a Ação Padrão e não usa reação.** *Quem tem mais de uma Ação Padrão no turno — um chefe, um capanga grande — perde **uma**, não todas* |

**São treze. Seis + duas + cinco. Lista fechada, não é exemplo.**

### A regra que anda com o degrau `Pesada`

> **Só as de nível `Pesada` dão Teste de Resistência no fim de cada turno do alvo, e só cabe uma delas por feitiço.**

### O `Atordoado` num chefe — a linha que importa pro Sukuna

> **O `Atordoado` cobra `uma` Ação Padrão de propósito.** *Um chefe do manual age mais de uma vez por rodada; tirar todas com uma condição só faria uma linha de feitiço apagar o turno de um chefe inteiro.* **Tirar uma ação de três é caro sem ser apagar a cena.**

### Três que NÃO são condição (§3.5)

| não é condição aqui | por quê |
|---|---|
| **`Inconsciente`** | é **cair morrendo**, e tem regra própria — peça 1 §5.5, com as duas escolhas e a janela de três rodadas |
| **`Exaustão`** | já existe, e é da **peça 10**. É relógio de descanso, não efeito de combate |
| **`Invisível`** | é **benefício**. *Aplicar `Invisível` num inimigo é pagar `Média` para ajudar ele.* |

### Duas removidas, com o motivo

- **`Petrificado`** saiu na v0.139. *"ela segue um balanceamento que não planejo ter no sistema"* — decisão do Mizuki. Ele era a mais cara, em `19,73` fatias, `217%` do teto da `Pesada`. O argumento dele passou pro `Impedido`.
- **`Paralisado`** não existe. Era o nome antigo do que hoje é `Atordoado`.

---

## 4. O FUNDAMENTO — a máquina que monta feitiço

**Onde mora:** no **manual**, `manual/Fundamento-MANUAL-v7.docx`, cuja fonte é `manual/gerador/partA.js` a `partF.js`.

- `partA.js` — Formas
- `partB.js` — o Fundamento do personagem, Famílias, Passivas
- `partC.js` — Formas em detalhe
- `partD.js` — **seção 3, catálogo de Melhorias; seção 4, catálogo de Restrições**
- `partE.js` — **seção 8, Regras de ouro; seção 9, Progressão**
- `partF.js` — **seção 10, feitiços prontos; seção 11, Para o mestre (Inimigos, PvP, A curva); Apêndice**

### Como funciona, passo a passo

*(reconstruído da leitura do gerador — a ordem é minha, os números são do arquivo)*

1. **A Classe diz o orçamento.** Classe N vale `3 × N` pontos, e custa `3 × N` PE pra lançar. `partF.js` escreve os cinco primeiros degraus como título de seção.
2. **A Forma é a base e não conta como Melhoria.** (`partE.js` §8, regra 3: *"A Forma não conta."*)
3. **Cada Melhoria custa por degrau, e o degrau é relativo à Classe:**
   - `Leve` = metade da Classe
   - `Média` = a Classe inteira
   - `Pesada` = Classe e meio
   - **sempre arredondando pra cima**
   - Nas suas **duas Famílias Livres**, tire metade da Classe do preço, com mínimo de `1`. Nas **três Fechadas**, não há o que comprar.
4. **Restrição devolve ponto**, e o ponto devolvido só pode pagar Melhoria.
5. **O que sobrar vira dado.** É a linha do §2.1 da peça 19: cada ponto que não vira Melhoria vira `1d8`, que são `4,5`.

### As oito Regras de ouro (`partE.js` §8) — coladas

| # | regra |
|---|---|
| 1 | Restrição paga Melhoria. Nunca vira dado de dano. O excedente some. |
| 2 | O dano total, somando alvos e repetições, nunca passa de 4 × Classe em dados. Contra um alvo só, feitiço comum para nos pontos da Classe: 4 × Classe num alvo é coisa de Liberação Máxima. |
| 3 | Melhorias: 2 nas Classes 1–2, 3 nas Classes 3–4, 4 da Classe 5 em diante. Restrições: até 2. A Forma não conta. |
| 4 | Restrição devolve no máximo 2 × Classe. |
| 5 | Liberação Máxima é Classe 3 ou mais, custa a rodada inteira, e você só tem as que o nível deu. |
| 6 | Feitiço em Ação Bônus ou Reação só permite mais um de Classe 0 no turno. |
| 7 | Duas Restrições não podem ser as duas de frequência, nem cobrar a mesma coisa. |
| 8 | Restrição que não atrapalhou em três sessões é trocada. |

E as duas notas que acompanham:

> Restrição que o seu Selo já obriga não devolve ponto, e o mestre pode recusar qualquer feitiço, mesmo um que passe em tudo.

### O que se compra com ponto

- **dado de dano** — o resto, `1d8 = 4,5` por ponto
- **condição** — Melhoria `Condição`, preço = o nível dela
- **área** — ver o item de Área logo abaixo
- **alcance** — família Alcance
- **Melhoria** — 66 delas, em 9 Famílias
- **duração** — família Tempo, e a Melhoria `Fica` (família Área)

### ÁREA — o que custa

**Achado importante e você precisa saber disso:** o manual **não vende o formato da área com preço por formato**. **NÃO EXISTE** uma linha "cone custa X, linha custa Y, esfera custa Z" no catálogo de Melhorias.

O que existe é:

**(a) O formato vem da FORMA do feitiço, e a Forma é a base**, não uma Melhoria comprada por degrau. Nos feitiços prontos do `partF.js` os formatos aparecem com número entre parênteses, que é o custo daquela peça naquele feitiço:

| formato | como aparece nos prontos | onde |
|---|---|---|
| `Linha` | `Chicote`: "Linha (−1)" na Classe 1 · `Julgamento Vertical`: "Linha (−2)" na Classe 4 | `partF.js` §10 |
| `Cone` | `Palma Trovejante`: "Cone (−1)" na Classe 2 | `partF.js` §10 |
| `Explosão` (a esfera) | `Domo de Gelo`: "Explosão (−2)" na Classe 3 · `Vala Comum`: "Explosão (−3)" na Classe 5 | `partF.js` §10 |
| `Projétil` | sempre sem número — é o alvo único, a base | `partF.js` §10 |
| `Toque` | **devolve**: "Toque (Corpo a Corpo +1)" na Classe 1, "+3" na Classe 3, "+5" na Classe 5 | `partF.js` §10 |

**(b) A tabela de Formas do `partC.js` é a resposta, e ela CONFIRMA o preço.** Colada inteira:

| Forma | Custa | O que é | Como resolve |
|---|---|---|---|
| `Projétil` | **—** | 18 m, um alvo | Rolagem de acerto |
| `Toque` | **—** | 1,5 m, um alvo. Projétil com a Restrição Corpo a Corpo embutida (devolve Média). | Rolagem de acerto |
| **`Explosão`** (a esfera) | **Leve** | Esfera de raio 3 m, num ponto a até 18 m | Teste de Resistência, metade no sucesso |
| `Aura` | **Leve** | Esfera de raio 3 m centrada em você. Explosão com Corpo a Corpo embutida (devolve Média). | Teste de Resistência, metade no sucesso |
| **`Cone`** | **Leve** | 4,5 m saindo de você | Teste de Resistência, metade no sucesso |
| **`Linha`** | **Leve** | 18 m por 1,5 m | Teste de Resistência, metade no sucesso |
| `Cura` | Média | Um aliado a até 9 m. Os dados viram cura. Pode escolher alvo hostil. | Automático no aliado, acerto no hostil |
| `Apoio` | — | Um aliado a até 9 m. Sem dano. Cada ponto que sobra vira 3 de vida temporária. | Automático |
| `Onda` | Pesada | Esfera de raio 3 m centrada em você. A cura ou o apoio pega todos os aliados dentro, sem dividir. | Automático |
| `Efeito` | — | Fora de combate. Sem dano. Ver seção 5. | Automático |

> ### RESPOSTA DIRETA: o sistema NÃO separa preço por formato
> **Cone, Linha e Explosão (a esfera) custam exatamente a mesma coisa: `Leve`.** Ou seja, metade da Classe, arredondando pra cima. Numa Classe 5 os três custam `3`.
> Está confirmado em três lugares que batem: a tabela de Formas do `partC.js`; os feitiços prontos do `partF.js` (Chicote C1 −1, Palma Trovejante C2 −1, Domo de Gelo C3 −2, Julgamento Vertical C4 −2, Vala Comum C5 −3); e uma frase do `partE.js` linha 114 — *"Forma Linha (Leve na Classe 5: 3 pontos)"*.
> **O que muda entre os três formatos não é o preço, é o tamanho e a escada que eles sobem.**

Regras que andam com a tabela de Formas:

> Trocar rolagem de acerto por Teste de Resistência, ou o contrário, é de graça.

> Cada Forma pertence a uma Família: Explosão, Cone e Linha à **Área**; Cura, Apoio e Onda ao **Amparo**. Fundamento com a Família Fechada fica sem essas Formas. Projétil, Toque e Efeito são de todo mundo.

### As três escadas de tamanho e alcance (`partC.js`, "Escadas")

| Escada | Degraus |
|---|---|
| Alcance | 1,5 m → 9 m → 18 m → 36 m → 90 m → o que você enxergar |
| Esfera (raio) | 3 m → 4,5 m → 6 m → 9 m → 15 m |
| Cone e Linha | 4,5 m → 9 m → 18 m → 30 m → 60 m |

> O degrau "o que você enxergar" vale pra olho nu. Câmera, luneta, espelho e visão emprestada não contam.
> Se uma Melhoria subir mais degraus do que a escada tem, ela para no último degrau.

### Base por Classe (`partC.js`, "Base por Classe")

| Forma | Classe 0 | Classes 1–5 | Classes 6–7 |
|---|---|---|---|
| Projétil e Toque* | 9 m | 18 m | 36 m |
| Explosão | raio 3 m, a 9 m | raio 3 m, a 18 m | raio 4,5 m, a 36 m |
| Cone | 3 m | 4,5 m | 9 m |
| Linha | 9 × 1,5 m | 18 × 1,5 m | 30 × 1,5 m |
| Apoio | 4,5 m | 9 m | 18 m |
| Cura e Onda | — | 9 m | 18 m |

> *Toque fica em 1,5 m em qualquer Classe.*

### As Melhorias de Área (`partD.js`, família Área) — coladas

| Melhoria | Custo | O que faz |
|---|---|---|
| `Maior` | Leve | Sobe um degrau de tamanho de área. Pode comprar duas vezes. |
| `Muito Maior` | Pesada | Sobe três degraus de tamanho de uma vez. |
| `Escolher` | Média | Você decide quem, dentro da área, é atingido. |
| `Fica` | Média | A área continua ali por 1 minuto. Quem entrar ou começar o turno nela leva metade dos dados. Exige concentração. |
| `Mais Um` | Leve | Um alvo a mais. Os dados são divididos entre os alvos. Pode comprar duas vezes. |
| `Rajada` | Leve | Divide o feitiço em (Classe + 1) tiros, cada um com sua rolagem de acerto, distribuídos como você quiser. |
| `Salto` | Média | Depois do primeiro alvo, pula pro inimigo mais perto a até 9 m com metade dos dados. |
| `Contorno` | Leve | A área faz curva. Ignora cobertura e dobra esquinas. |

### As Melhorias de Alcance (`partD.js`, família Alcance)

| Melhoria | Custo | O que faz |
|---|---|---|
| `Longe` | Leve | Sobe um degrau na escada de alcance. Pode comprar duas vezes. |
| `Muito Longe` | Média | Sobe três degraus de uma vez. |
| `Sem Ver` | Pesada | Você conjura contra um alvo fora da sua linha de visão, desde que saiba onde ele está. Alcance normal do feitiço. |
| `Passo` | Leve | Você anda até 6 m antes ou depois do feitiço, sem provocar ataque de oportunidade. |
| `Empurrão` | Leve | Move o alvo até 6 m na direção que você quiser. |
| `Troca` | Média | Você e o alvo trocam de lugar. |
| `Perseguir` | Média | Se o alvo sair do alcance antes do feitiço resolver, o feitiço vai atrás. |

### A Melhoria `Condição` — colada

| Melhoria | Custo | O que faz |
|---|---|---|
| `Condição` | **o nível dela** | Aplica uma das treze condições. O preço é o nível dela — Leve, Média ou Pesada —, na tabela logo abaixo. **Dura uma rodada.** As de nível Pesada dão Teste de Resistência no fim de cada turno do alvo, e cabe só uma delas por feitiço. |

### Imunidade, no catálogo de Melhorias

Caixa de aviso do `partD.js`, literal:

> **Imunidade.** Nenhuma Melhoria fura imunidade. Quem quiser isso monta uma **Passiva de Regra Própria** com o mestre, com limite de uma vez por cena.

---

## 5. As CLASSES de feitiço, e o teto no nível 20

**Dono:** `manual/gerador/partA.js`, a página de números (seção 2, "Tabela de bolso" do começo do manual). **Achei a fórmula escrita e a tabela mestra inteira — nada aqui é extrapolação minha.**

A caixa de fórmulas, colada:

> **Pontos** = 3 × Classe          **Teto de dano** = 4 × Classe em dados
> **Devolução máxima** = 2 × Classe      **Liberação Máxima** = + Classe em dados
> **Custo em PE** = 3 × Classe (o mesmo número dos pontos)
>
> Melhoria **Leve** custa metade da Classe · **Média** custa a Classe · **Pesada** custa Classe e meio. Arredonde pra cima.

E o exemplo que ele dá logo antes: *"**Pontos = 3 × Classe.** Um feitiço de Classe 3 tem 9 pontos."*

### A TABELA MESTRA — `partA.js`, colada inteira

**Esta é a tabela que responde a sua pergunta 5 inteira, e mais.**

| Classe | Nível | Pontos e PE | Leve | Média | Pesada | Devol. máx | Liberação | Teto | Dano cheio |
|---|---|---|---|---|---|---|---|---|---|
| **1** | 1 | **3** | 1 | 1 | 2 | 2 | +1 | 4 | 3d8 = 13 |
| 2 | 5 | 6 | 1 | 2 | 3 | 4 | +2 | 8 | 6d8 = 27 |
| 3 | 9 | 9 | 2 | 3 | 5 | 6 | +3 | 12 | 9d8 = 40 |
| 4 | 13 | 12 | 2 | 4 | 6 | 8 | +4 | 16 | 12d8 = 54 |
| **5** | **17** | **15** | **3** | **5** | **8** | **10** | **+5** | **20** | **15d8 = 67** |
| 6 | 21 | 18 | 3 | 6 | 9 | 12 | +6 | 24 | 18d8 = 81 |
| 7 | 26 | 21 | 4 | 7 | 11 | 14 | +7 | 28 | 21d8 = 94 |

**Confirmado: Classe 6 = `18` pontos, Classe 7 = `21` pontos.** A fórmula `3 × Classe` está escrita e a tabela publica os sete degraus.

**E repare:** as colunas `Leve` / `Média` / `Pesada` desta tabela são **exatamente** as colunas da tabela do §2.1 da peça 19. As duas são a mesma tabela vista de dois documentos. Isso fecha o círculo entre o manual e a régua de condição.

As notas que andam com ela:

> A coluna **Nível** é quando aquela Classe abre pra você. **Leve**, **Média** e **Pesada** são os três preços de Melhoria (seção 3), e **Devol. máx** é o total que as Restrições de um feitiço podem devolver (seção 4).

> A coluna **Teto** é o máximo de dados de dano de um feitiço quando você soma todos os alvos e repetições. Contra um alvo só, o limite é mais baixo: um feitiço comum para nos pontos da Classe. Quem alcança o teto num alvo só é a **Liberação Máxima** (seção 6).

### Quantas Melhorias cabem (`partA.js`)

| Classe do feitiço | Melhorias | Restrições |
|---|---|---|
| 1 e 2 | 2 | 2 |
| 3 e 4 | 3 | 2 |
| **5 em diante** | **4** | **2** |

> A Forma não conta como Melhoria.

### Energia (`partA.js`)

> Conjurar um feitiço custa **3 × Classe** de PE — o mesmo número dos pontos dele. Classe 0 é grátis.
> **Liberação Máxima** custa 50% a mais que a Classe dela, arredondando pra cima.
> **Técnica Máxima** custa 5 × a sua maior Classe de PE.

*(o conjurador ganha `6` PE por nível — `partA.js`)*

### A escada de nível (`manual/gerador/partE.js` §9 Progressão) — colada

| Nível | O que ganha |
|---|---|
| 1 | Fundamento com três Famílias Fechadas. Dois feitiços de Classe 0 (grátis). Classe 1. Passiva Livre. |
| 5 | Classe 2. Um feitiço de Classe 0 a mais. |
| 7 | Libera Passiva de Classe 2. |
| 9 | Classe 3. |
| 10 | **A primeira Liberação Máxima.** |
| 11 | Um feitiço de Classe 0 a mais. |
| 13 | Classe 4. Libera Passiva de Classe 3. |
| 17 | Classe 5. Técnica Máxima. Um feitiço de Classe 0 a mais. |
| **20** | **A segunda Liberação Máxima.** |
| 21 | Classe 6. |
| 26 | Classe 7. |
| 30 | **A terceira Liberação Máxima.** |

### O TETO no nível 20

Cruzando as três fontes:

| o que | valor no nível 20 | dono |
|---|---|---|
| **Classe máxima** | **Classe 5** (abriu no 17; a 6 só no 21) | `partE.js` §9 |
| **pontos por feitiço** | **`15`** | `partF.js` §10, título da Classe 5 |
| **teto de dados, somando alvos e repetições** | `4 × Classe` = **`20` dados** | `partE.js` §8, regra 2 |
| Melhorias por feitiço | `4` (Classe 5 em diante) | `partE.js` §8, regra 3 |
| Restrições por feitiço | até `2`, devolvendo no máximo `2 × Classe` = `10` | `partE.js` §8, regras 3 e 4 |
| Liberações Máximas que ele tem | **duas** (uma no 10, a segunda no 20) | `partE.js` §9 |

E a tabela "A curva" do `partF.js`, que publica o que o nível entrega — a linha do 17 a 20 é a sua:

| Nível | Classe | Rotina | Feitiço num alvo | Somando alvos | Liberação | Téc. Máxima |
|---|---|---|---|---|---|---|
| 1 a 4 | 1 | 3d8 = 13 | 3d8 = 13 | 4d8 = 18 | — | — |
| 5 a 8 | 2 | 6d8 + 1d8 = 31 | 6d8 = 27 | 8d8 = 36 | — | — |
| 9 a 12 | 3 | 9d8 + 1d8 = 45 | 9d8 = 40 | 12d8 = 54 | 12d8 = 54 | — |
| 13 a 16 | 4 | 12d8 + 2d8 = 63 | 12d8 = 54 | 16d8 = 72 | 16d8 = 72 | — |
| **17 a 20** | **5** | **15d8 + 2d8 = 76** | **15d8 = 67** | **20d8 = 90** | **20d8 = 90** | **24d8 = 108** |
| 21 a 25 | 6 | 18d8 + 3d8 = 94 | 18d8 = 81 | 24d8 = 108 | 24d8 = 108 | 28d8 = 126 |
| 26 a 30 | 7 | 21d8 + 3d8 = 108 | 21d8 = 94 | 28d8 = 126 | 28d8 = 126 | 32d8 = 144 |

**No nível 20 o jogador tem `76` de Rotina, `67` de feitiço num alvo, e `108` de Técnica Máxima.**

E a nota da faixa lendária (`partE.js`):

> Os Classes 6 e 7 existem, mas a recomendação é que o ganho dos níveis 21 a 30 venha de Passivas que quebram regra, e não de dado a mais.

### Quantos feitiços — não é conta do manual

> **Quantos feitiços você conhece não é conta deste manual.** O Fundamento manda na Classe, na Liberação Máxima e em quando cada Classe de Passiva abre — a tabela acima é sobre isso. O tamanho da lista vem do sistema em volta.

E o que fica valendo:

> **Passiva é paga com espaços dessa lista**, a **Expansão de Domínio** também, e as **Liberações Máximas ficam de fora** — elas não ocupam espaço.

---

## 9. A tabela "Inimigos" do MANUAL

**Onde mora:** `manual/gerador/partF.js`, seção `11 · Para o mestre`, subseção `H2('Inimigos')` (linha 154).
**No livro:** `manual/Fundamento-MANUAL-v7.docx` / `.pdf`, seção 11.

A tabela, colada inteira:

| Nível do grupo | Dano do grupo por rodada | Chefe sozinho: vida | Chefe: dano | Capanga: vida | Capanga: dano |
|---|---|---|---|---|---|
| 2 | ~38 | 105 a 123 | 17 | 28 | 6 |
| 5 | ~90 | 250 a 290 | 39 | 67 | 13 |
| 10 | ~130 | 360 a 420 | 75 | 97 | 25 |
| 15 | ~180 | 500 a 580 | 111 | 135 | 37 |
| **20** | **~220** | **600 a 720** | **147** | **165** | **49** |
| 25 | ~275 | 760 a 890 | 183 | 206 | 61 |
| 30 | ~315 | 870 a 1020 | 219 | 236 | 73 |

### O que ela publica no NÍVEL 20

- **Dano do grupo por rodada:** `~220`
- **Chefe sozinho, vida:** `600 a 720`
- **Chefe, dano por rodada:** `147`
- **Capanga, vida:** `165`
- **Capanga, dano:** `49`

### As notas que andam com ela — coladas

> A conta supõe quatro personagens: um focado em bater, dois medianos, um de apoio.

> Quatro capangas equivalem a um chefe, e é assim que a coluna se lê: os quatro juntos têm a vida do chefe, e cada um bate o golpe dele. Trocar o corpo único por vários não muda o tamanho do encontro — muda quantas rolagens ele custa e quando o dano do inimigo começa a cair.

> Cada linha vale para a faixa de Classe dela, e não só para aquele nível: a do 2 cobre o nível 2 ao 4, a do 5 cobre até o 8, a do 10 até o 12, e assim por diante. Dentro da faixa o grupo ganha vida e o inimigo não, então o encontro afrouxa — se quiser manter o aperto no fim da faixa, acrescente capangas.

> Chefe sozinho precisa de cerca de três vezes o dano de rodada do grupo em vida, e é isso que faz a luta contra ele durar três rodadas. Se não quiser inflar o número, use capangas ou uma barreira que absorva antes da vida.

> O dano dele por rodada é 90% da vida de um personagem daquele nível — ele não derruba o grupo, mas derruba alguém, e derruba mais de um se concentrar. **Ele perde a ação três vezes por rodada contra um grupo de quatro, e age três vezes enquanto eles agem quatro: o golpe é um terço da linha.**

**Essa última frase é a que a peça 19 §2.2 disse que "diz o contrário" da contagem de ação.** Vale ler as duas juntas: o manual escreve que o chefe age três vezes por rodada, e o `147` do nível 20 é **a linha inteira** — o golpe individual é um terço, `49`.

### As duas coisas que a ficha do inimigo carrega além da tabela

> **Integridade.** A do inimigo é a que a seção acima escreve: a vida máxima dele, então a coluna de vida serve para as duas barras. Anote as duas assim mesmo — o sistema em volta tem efeito que tira alma sem tirar vida, e é aí que os dois números se separam.

> **Reação.** Uma por rodada, como qualquer personagem, e ela volta no começo do turno dele. Ela paga o ataque de oportunidade, e o sistema em volta pendura outras coisas nela. Marque quando for gasta: guardar ou não é decisão do inimigo do mesmo jeito que é da mesa.

**Então, no nível 20, o Sukuna-chefe tem Integridade `600 a 720` também.**

### PvP, de quebra (mesma seção)

> Em duelo entre personagens, o dano de feitiço cai **um terço**.

| Nível | Vida | Pico normal | Rodadas | Com o corte | Rodadas |
|---|---|---|---|---|---|
| 10 | 92 | 54 | 1,7 | 36 | 2,6 |
| **20** | **172** | **90** | **1,9** | **60** | **2,9** |
| 30 | 252 | 126 | 2,0 | 84 | 3,0 |

**A vida de um personagem no nível 20 é `172`.** E `147` (dano do chefe) é `85%` disso — a nota diz "90% da vida de um personagem daquele nível", então bate de perto.

---

## 10. O ESTILHAÇO

**Onde mora:** `manual/gerador/partD.js`, seção `3 · Melhorias`, família **`Castigo`** (linha 127).
**No livro:** `manual/Fundamento-MANUAL-v7.docx`, seção 3, família Castigo.

A linha, colada:

| Melhoria | Custo | O que faz |
|---|---|---|
| **`Estilhaço`** | **Leve** | Em crítico, ou quando o alvo erra o Teste de Resistência por 5 ou mais, **metade dos dados respinga em quem estiver do lado.** |

### O preço

`Estilhaço` é degrau **`Leve`**. Pela regra de abertura da seção 3 do `partD.js`, `Leve` custa **metade da Classe, arredondando pra cima**:

| Classe | preço do `Estilhaço` |
|---|---|
| 1 | 1 |
| 2 | 1 |
| 3 | 2 |
| 4 | 2 |
| **5** | **3** |
| 6 | 3 |
| 7 | 4 |

*(a coluna bate exatamente com a coluna `Leve` da tabela do §2.1 da peça 19 — as duas são a mesma regra)*

**E se Castigo for uma das suas duas Famílias Livres**, tire metade da Classe do preço, com mínimo de `1` — o que na prática zera o desconto num degrau Leve e deixa ele em `1`.

### Um detalhe que vale pro Sukuna

O `Estilhaço` é a única Melhoria do manual que cita "em crítico", e é por causa dela que o crítico precisou ser definido. Está escrito em `sistema/03-mecanica/01-atributos-acerto-defesa.md` linha 352:

> *Escrito na v0.25.* O crítico era usado e nunca tinha sido definido: o manual cita *"em crítico"* na Melhoria **Estilhaço** e para por aí, e o projeto não tinha uma linha sobre ele.

E o escopo do crítico, da tabela de âncoras do §2.2 da peça 19:

> **o escopo do crítico** — dobra **só os dados do que rolou o acerto** — dono: peça 1 §5.2

### A outra família Castigo, colada inteira (útil pra montar o chefe)

| Melhoria | Custo | O que faz |
|---|---|---|
| `Queima` | Média | Metade dos dados de novo, no começo do próximo turno do alvo. |
| `Acúmulo` | Média | +1 dado por rodada seguida usando este feitiço no mesmo alvo. Para de somar em +3. |
| `Remate` | Média | +25% de dano contra alvo abaixo de metade da vida. Não entra num feitiço que tenha uma Condicional ligada à vida do alvo. |
| **`Estilhaço`** | **Leve** | **Em crítico, ou quando o alvo erra o Teste de Resistência por 5 ou mais, metade dos dados respinga em quem estiver do lado.** |
| `Quebra Coisa` | Leve | Dano dobrado contra barreiras, objetos e estruturas. |
| `Rasga Escudo` | Média | O dano ignora pontos de vida temporários e barreiras: bate direto na vida. |
| `Sem Cura` | Média | O alvo não pode receber cura até o fim do próximo turno dele. |

---

## 6. PEÇA 22 §3 — o PACTO

**Arquivo:** `sistema/03-mecanica/22-pactos.md`
**Seção:** `## 3. O pacto permanente` (linha 56), com `§3.1` a `§3.5`

Abertura, literal:

> É o único com número, e todos os números desta peça são dele.

**Existem quatro formas de pacto** (§1), e só a permanente tem número. As outras três: pacto temporário (§4), `Promessa` (§5), pacto de restrição (§6).

### §3.1 — quantos cabem: metade da Essência

> **Você fecha, em toda a campanha, um número de pactos permanentes igual a metade da sua Essência, arredondando para baixo.**

> **Espírito é o Teste de Resistência de Essência** (peça 1 §4), e a escala de atributo vai de `0` a `6` (peça 2 §1).

| Essência | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|---|
| **pactos permanentes** | 0 | 0 | 1 | 1 | 2 | 2 | 3 |

> ***Decisão do Mizuki: zero é zero, sem piso.*** **Quem não investiu em Essência não fecha pacto permanente nenhum.**

> **Este é o único número desta peça que o jogador precisa saber**, e ele cabe numa linha da ficha.

### §3.2 — "o teto do permanente é da Essência dele"

**É isto que a frase quer dizer, e são duas coisas amarradas:**

**(a) A Essência diz QUANTOS pactos.** Metade dela, arredondando pra baixo. Essência `6` (o topo) → `3` pactos.

**(b) O teto de valor de CADA pacto é derivado desse número.** Literal:

> **A fatia é a unidade de orçamento do projeto: `5,08` de dano por rodada no nível 30**, e o dono dela é a régua de Trilhas, no `DESENHO-trilhas.md`.

> ***Decisão do Mizuki na v0.133: a camada de Pacto vale `1,50` fatia.***

> **O teto é POR PACTO, e ele é derivado e não escolhido:**
>
> ```
> teto por pacto = camada ÷ pactos no pior caso
>                = 1,50 ÷ 3
>                = 0,50 fatia
> ```

> *O pior caso é a Essência no teto, que é `6` pela peça 2 §3, e `6/2` dá três pactos.* **Se o teto fosse da camada inteira em vez de por pacto, um Essência `2` levaria num pacto só o que um Essência `6` divide em três** — e aí investir em Essência pagaria *menos*, que é o contrário do que o teto de quantidade quer dizer.

**Então: a Essência é dona das duas pontas.** Ela diz quantos pactos você fecha, e o denominador `3` que produz o `0,50` é o teto da Essência (`6`) dividido por dois. **O permanente inteiro pende da Essência.**

Quanto vale `0,50` fatia, nas moedas em que alguém pergunta:

| o teto de um pacto vale | quanto | de onde sai |
|---|---|---|
| **dano por rodada** | `2,54` | `0,50 × 5,08` |
| **de um golpe simples** | **`21%`** | o golpe simples é `12` no nível 30 |
| de um `Classe 0` | `9%` | o `Classe 0` é `27` no nível 30, no manual |
| de PE por rodada | `0,49` | `1` PE por rodada vale `5,14` de dano, câmbio da peça 5 §4 |

E o motivo do teto, que é a linha que explica o desenho:

> **Ele não existe para preçar pacto. Ele existe para fazer com que preçar pacto em dano não valha a pena.** *Quem gastar um pacto permanente em dano leva um quinto de um soco.* **Quem gastar em coisa que não é número — acesso, permissão, uma regra do mundo — leva o pacto inteiro.**

> *`1,50` é o maior valor que ainda deixa dano ser escolha ruim.* **Abaixo de um quarto de um soco ninguém gasta pacto em dano; a `2,00` fatias isso vira `28%` e passa a ser opção legítima, e aí o teto para de fazer o trabalho que ele existe para fazer.**

### §3.3 — o que o pacto pode entregar

| o que o pacto dá | quem alcança | tem preço em fatia? | quem segura |
|---|---|---|---|
| **PE** | qualquer ficha | **sim** — `1` PE por rodada vale `1,01` fatia (peça 5 §4) | **o teto**: `0,50` fatia é meio PE por rodada |
| **uma aptidão** | quem tem aptidão | **não, e não pode ter** | o mestre, e o teto de quantidade |
| **um espaço de feitiço** | quem escreve Fundamento, e isso inclui `Sem Técnica` | **não tem**, pelo mesmo motivo | o mestre, e o teto de quantidade |

> **Então o teto mede DANO, e só dano.** O que não é dano não passa por ele, e quem aprova é o mestre.

E o aviso de por que "uma aptidão a mais" não tem régua:

> **⚠ A régua de *"uma aptidão a mais"* não existe, e não é descuido — ela não pode existir.** *Ela matou uma Trilha inteira: o `Repertório` do Emanador foi abandonado na v0.81 exatamente por depender dela.* **O motivo está escrito lá: uma aptidão a mais vale a Trilha inteira para quem nunca escolhe Refino, e um sétimo para quem sempre escolhe.** *O valor depende de quantas você já tem, então não existe número.*

### §3.4 — o que ele NUNCA entrega

> **Pacto não mexe em valor numérico de rolagem. Nem acerto, nem Defesa, nem perícia.**

> *Decisão do Mizuki, e ela tem número por trás: `+1` no acerto vale `10,80` de dano por rodada, que é `2,13` fatias — mais de quatro vezes o teto de um pacto inteiro.* **Não é proibição de gosto; é que não cabe.**

> **A Defesa cai junto pela mesma porta.**

> **O que o pacto pode tocar é dano**, e aí o teto do §3.2 faz esse toque ser uma escolha ruim de propósito.

---

## 7. PEÇA 26 §6.3 — resistência e imunidade custam degrau de categoria

**Arquivo:** `sistema/03-mecanica/26-bestiario.md`
**Seção:** `### 6.3 Resistência é vida escondida, e ela custa degrau de categoria` (linha 267)

Abertura, literal:

> **A peça 19 §4 divide os catorze tipos de dano em três grupos e diz quanto cada um pesa no que um alvo recebe** — `Físicos 60%`, `Elementais 30%`, `Especiais 10%`. **Resistir corta pela metade o que entra por aquele grupo, e isso sobe a vida efetiva do inimigo:**

A tabela, colada:

| grupo | peso | resistência | imunidade | vulnerabilidade |
|---|---|---|---|---|
| `Físicos` | `60%` | **`1,43×`** | **`2,50×`** | `0,62×` |
| `Elementais` | `30%` | `1,18×` | `1,43×` | `0,77×` |
| `Especiais` | `10%` | `1,05×` | `1,11×` | `0,91×` |
| **um tipo só** | **`20%`** | **`1,11×`** | **`1,25×`** | `0,83×` |

### A regra exata, colada

> **Resistência ao grupo `Físicos` custa um degrau de categoria.** *Aos `Elementais`, meio degrau; aos `Especiais`, nada.*
> **Imunidade a `Físicos` custa mais de um degrau, e a escada não tem o que vender acima da `Calamidade`** — então ela só existe num inimigo que já esteja abaixo do topo.
> **Vulnerabilidade devolve na mesma moeda.**

E a justificativa do câmbio:

> **A escada de categoria já é a moeda disso.** *Subir da `Alcateia` para a `Calamidade` vale `1,50×`, e resistir a `Físicos` vale `1,43×`.*

### "A partir de quantos tipos começa a custar" — CUIDADO, a pergunta não é essa

> **⚠ A peça NÃO conta tipos. Ela cobra por GRUPO.**
> A régua tem quatro linhas: os três grupos (`Físicos`, `Elementais`, `Especiais`) e a linha `um tipo só`. **Não existe no texto uma frase do tipo "a partir de N tipos começa a custar".**
> O que existe é: **um tipo só** pesa `20%` e resistir a ele vale `1,11×` — **e o texto não diz que isso custa degrau nenhum.** Ele só preça a linha.
> **A cobrança escrita começa nos GRUPOS:** `Especiais` custa **nada**, `Elementais` custa **meio degrau**, `Físicos` custa **um degrau**.
> Então a resposta honesta: **o degrau começa a ser cobrado quando a resistência cobre o grupo `Elementais` (meio degrau) ou o grupo `Físicos` (um degrau). Resistência a `Especiais` e a um tipo avulso não tem preço escrito. NÃO CONFIRMADO que exista um limiar por contagem de tipos.**

### O exemplo que a peça dá, e ele é literalmente um chefe

> **Um chefe de `Alcateia` imune a `Físicos` vira uma luta de `7,50` rodadas que cobra `169%` da vida do grupo**, contra as `3,00` rodadas e `68%` que a categoria promete. *A ficha diz uma coisa e a mesa joga outra, e com a linha da v0.201 a diferença deixou de ser uma luta mais longa e passou a ser uma luta que o grupo não termina de pé.*

### De onde vem o mecanismo, e o aviso que anda com ele

> **O mecanismo é o do `Guia do Mestre` de 2014**, que tem uma tabela de `Pontos de Vida Efetivos` fazendo exatamente isso. *Lá o multiplicador encolhe conforme o nível sobe, porque o grupo ganha jeitos de furar; aqui ele não encolhe, porque o `60/30/10` é fixo.*

> **⚠ E toda esta régua está pendurada num palpite, que a peça 19 §4 declara com todas as letras:** *o peso dos três grupos é previsão, `04-playtest/` está vazia, e ele é "o número que decide quanto vale toda resistência do sistema".* **Quando a mesa corrigir o peso, o multiplicador se refaz sozinho** — ele é conta, e não tabela.

---

## 8. PEÇA 26 §6.4 — a Expansão de Domínio do inimigo DOBRA a categoria

**Arquivo:** `sistema/03-mecanica/26-bestiario.md`
**Seção:** `### 6.4 A Expansão de Domínio do inimigo — ela DOBRA a categoria` (linha 290)

### O número, e de onde ele sai

> ***Decisão do Mizuki: a Expansão do inimigo é a do jogador, escalonada para grupo.*** *A máquina inteira mora no manual, e nada dela é reescrito aqui.*

> **Ela não acrescenta dano nenhum, e é isso que faz o preço dela ser fácil de achar.** *Pelo §6.1 tudo que o inimigo faz sai da cota de dano por rodada, e o Acerto de um domínio não é exceção: a cota é a mesma dentro e fora.* **O que muda é quanto dela CHEGA.**

> **Fora do domínio o inimigo acerta `52%` — é a banda de `50%` a `55%` que o §3.1 publica.** *Dentro, o Acerto acontece: sem rolagem e sem Teste de Resistência, como o manual escreve.*
> **Então a Expansão completa multiplica a saída efetiva dele por `1 ÷ 0,52`, que é `1,92 ×`.**

> **E a categoria mede exatamente a coisa que esse número move.** *Ela é "quantos personagens ele exige", e o fator dela é `personagens ÷ 4`.* **Como `1,92` arredonda para `2`, a regra sai em uma linha:**

> ### **Uma Expansão de Domínio completa DOBRA quantos personagens o inimigo exige.**

### A tabela, colada

| categoria | exige | com Expansão completa |
|---|---|---|
| **`Ronda`** | `1` | `2` — vira uma **`Dupla`** |
| **`Dupla`** | `2` | `4` — vira uma **`Alcateia`** |
| **`Alcateia`** | `4` | **`8`** — acima da escada |
| **`Calamidade`** | `6` | **`12`** — acima da escada |

> **Duas caem em degraus que a escada já tem, e duas passam do topo.** *A escada sobe `2,00 ×`, `2,00 ×` e `1,50 ×` — o último degrau é menor que a Expansão, então as duas de cima saem dela.* **Isso não é impedimento: a categoria mede pessoas, e o número existe fora da escada do mesmo jeito.**

### O bloco que cita o Sukuna pelo nome

> **⚠⚠ E é por isso que o chefe da obra com domínio nunca é enfrentado por quatro.** *Uma `Calamidade` com Expansão exige **doze** feiticeiros.* **A régua diz, em número, a coisa que a ficção já dizia: contra isso o grupo não ganha — ele foge, ou traz gente.**
>
> ***⚠ A primeira forma desta seção estava errada, e quem achou foi o Mizuki:*** *"não faz sentido um Sukuna da vida não ter expansão, ele seria Calamidade, não?"* **Ela media só para BAIXO — "com que linha eu monto para o encontro não crescer" — e, não achando degrau abaixo da `Calamidade`, concluía que aquela categoria não podia ter domínio.** *A conclusão não segue.* **O que falta ali não é a permissão: é o número do encontro maior**, e ele existe porque a categoria mede pessoas e não degraus.
>
> *Uma régua que proíbe o chefe mais famoso da obra de fazer a coisa mais famosa dele está errada antes de qualquer conta.*

**Ou seja: o repositório já decidiu, com o nome dele escrito, que o Sukuna é `Calamidade` COM Expansão, e que isso exige `12` feiticeiros.**

### Os dois lados da regra, pro mestre

> **Quer manter o tamanho?** *Monte com a linha da categoria de baixo* — uma `Alcateia` com domínio construída com os `109` de dano por rodada da `Dupla` entrega os `109` inteiros, contra os `114` efetivos de uma `Alcateia` normal. **Só a `Dupla` e a `Alcateia` têm linha abaixo para isso.**
>
> **Quer o inimigo maior?** *Deixe a linha como está e leia a coluna da direita* — o encontro passou a exigir o dobro de gente, e o mestre monta a mesa sabendo disso.

**Reparo:** a `Calamidade` **não tem** linha de baixo pra usar esse truque. Só `Dupla` e `Alcateia` têm. Então um Sukuna `Calamidade` com Expansão só existe na coluna da direita — encontro de doze.

### A Expansão INCOMPLETA

> **A incompleta não custa nada nesta régua.** *O manual diz que o Acerto dela "resolve por rolagem, como um feitiço"* — **sem a garantia não existe o `1,92 ×`**, e o que ela dá é o Efeito, que não é dano. *Qualquer categoria pode ter uma.*

### Abrir não custa rodada ao inimigo

> **E abrir não custa rodada ao inimigo, apesar de custar ao jogador.** *O manual cobra a rodada inteira e `6 ×` a maior Classe de PE; o inimigo não conta PE pelo §6.1, e o Acerto acontece no momento em que ele abre.* **A cota daquela rodada sai pelo Acerto em vez de sair pelos golpes, e nada se perde.**

### A duração

> **A duração cobre a luta inteira, e é por isso que o multiplicador vale o encontro todo.** *O manual põe a duração em metade do refino, e o refino do chefe do nível 30 é `10` — cinco rodadas contra uma luta de `3,00`.*

---

## BÔNUS que eu achei e você vai precisar — a CATEGORIA (peça 26 §4)

Isto não estava na sua lista, mas é a peça que amarra a tabela "Inimigos" do manual com a ficha do Sukuna. **Sem ela, o `147` do nível 20 não vira ficha.**

**Arquivo:** `sistema/03-mecanica/26-bestiario.md` §4 (linha 74) e §4.1 (linha 87)

> ***Ideia do Mizuki, e o eixo é o dele:*** *quantos feiticeiros são precisos para enfrentar aquilo.* **A tabela de inimigo do manual já responde isso para um número — ela é calibrada para quatro —, e a categoria é aquela linha reescalada.**

| categoria | personagens | fator sobre a linha do manual | ações |
|---|---|---|---|
| **`Ronda`** | 1 | `× 0,25` | `1` |
| **`Dupla`** | 2 | `× 0,50` | `1` |
| **`Alcateia`** | 4 | `× 1,00` | `3` |
| **`Calamidade`** | 6 | `× 1,50` | **`5`** |

> **A `Alcateia` é a linha do manual sem tocar em nada.** *As outras três saem dela, e nenhuma inventa número.*

### §4.1 — a ficha pronta de cada categoria, e a linha do NÍVEL 20

| categoria | nv 10 | **nv 20** | nv 30 |
|---|---|---|---|
| `Ronda` | `97` vida · `19` dano | **`165` · `37`** | `236` · `55` |
| `Dupla` | `195` · `37` | **`330` · `73`** | `472` · `109` |
| `Alcateia` | `390` · `75` | **`660` · `147`** | `945` · `219` |
| **`Calamidade`** | `585` · `112` | **`990` · `220`** | `1417` · `328` |

**Confere com o manual:** a linha do manual no nível 20 é vida `600 a 720` e dano `147`. O meio da banda é `660`, que é exatamente a `Alcateia`. E `Calamidade` = `660 × 1,50 = 990` e `147 × 1,50 = 220,5 → 220`. **Bate.**

> **⚠ O arredondamento é meio para BAIXO, e ele é declarado porque não é cosmético.** *Os fatores são `0,25`, `0,50` e `1,50`, então **vinte e duas das cinquenta e seis células** desta escala caem exatamente em `,5`.* **Três lugares calculam isto — a peça, o validador e o gerador do bloco — e cada linguagem arredonda de um jeito:** *o `Math.round` do JavaScript sobe, o `round` do Python vai para o par.*

### §4.2 — de onde saem as ações

> **O manual escreve que o chefe *"perde a ação três vezes por rodada"* contra um grupo de quatro** — ele age uma vez enquanto eles agem quatro. **Então a compensação é `personagens − 1`, com piso `1`:** na `Ronda` ele age uma vez porque o outro lado também age uma vez, e na `Alcateia` ele age três.

> **⚠ E a `Alcateia` não pode descer de `3`, e isso não é desta peça.** *A peça 19 §2.2 preça quatro das treze condições dividindo pelas ações do chefe.* **Com `2` as quatro passam do teto do próprio tier**, e o piso está medido lá, com a checagem `12` daquele validador em cima.

**Então uma `Calamidade` age `5` vezes por rodada** (`6 − 1`). **Pro Sukuna isso é a linha mais importante da ficha depois da vida.**

---

## BÔNUS 2 — A FICHA do inimigo, as dezessete linhas (peça 26 §3)

**Isto é o molde literal da ficha que você vai preencher.** Não estava na sua lista e é o documento que amarra tudo.

**Arquivo:** `sistema/03-mecanica/26-bestiario.md` §3 (linha 25)

> **Dezessete linhas. Nenhum número novo nasce aqui** — o que esta peça faz é dizer de onde cada um sai.

| linha | valor | dono |
|---|---|---|
| nível | o nível do grupo | o mestre declara antes da mesa |
| categoria | `Ronda` · `Dupla` · `Alcateia` · `Calamidade` | o §4 |
| vida | a linha do manual vezes o fator da categoria | manual, a tabela `Inimigos` |
| **Integridade** | igual à vida máxima | manual, a seção `Inimigos` |
| dano por rodada | a linha do manual vezes o fator da categoria | manual, a tabela `Inimigos` |
| ações por rodada | personagens da categoria menos um, piso `1` | o §4.2 |
| **Defesa** | `10 + Destreza + proteção` | peça 1 §5 |
| **acerto** | `atributo + maestria` | peça 1 §5 |
| **CD** | `8 + atributo + maestria` | peça 1 §5 |
| Reação | uma por rodada, volta no começo do turno dele | manual, a seção `Inimigos` |
| refino | a curva do `meio a meio` | peça 11 §3 |
| Testes de Resistência | dois treinados de quatro | peça 7 §6 |
| deslocamento | `9 m` | peça 3 §3 |
| **atributos** | os cinco, no orçamento da peça 2 | peça 2 §3 |
| **características** | Passivas, aptidões e técnica, pelo §6 | peça 11, o mesmo catálogo do jogador |
| **pacto** | **opcional, e o teto do permanente é da Essência dele** | **peça 22 §3** |
| **resistência, vulnerabilidade e imunidade** | custam degrau de categoria, pelo §6.3 | peça 19 §4 |

**Repare na penúltima linha:** a frase que você me mandou procurar — *"o teto do permanente é da Essência dele"* — **é literalmente uma célula desta tabela.** Ela mora aqui, na peça 26 §3, e aponta pra peça 22 §3, que é onde a conta está. As duas leituras estão nas seções 6 e nesta.

### §3.1 — as três derivadas, nível a nível

> **O inimigo carrega a mesma curva de atributo de quem investe** — `3` no nível 2 subindo a `6` no 26 —, e é isso que põe as três no lugar em que as outras peças já as mediam.

| nível do grupo | 5 | 10 | 15 | **20** | 25 | 30 |
|---|---|---|---|---|---|---|
| Defesa | `14` | `16` | `17` | **`18`** | `19` | `20` |
| acerto | `+4` | `+6` | `+6` | **`+8`** | `+8` | `+10` |
| CD | `12` | `14` | `14` | **`16`** | `16` | `18` |
| refino | `1` | `4` | `6` | **`7`** | `9` | `10` |

> **Contra um personagem que investiu em defesa ele acerta `50%` a `55%`, e o Teste de Resistência treinado dele falha `35%`.** *São os mesmos números que a peça 1 §6 publica do lado do jogador, e é isso que prova a derivação.*

**Esse `52%` é o mesmo que o §6.4 usa pra derivar o `1,92×` da Expansão.** As duas seções conversam.

### §3.2 — os cinco atributos

> **O inimigo monta os cinco no mesmo orçamento de uma ficha** — nove pontos na criação, teto `3` ali, `+1` por marco e teto `6`.

> **É daqui que as três derivadas do §3.1 saem.** *A Defesa lê a Destreza, o acerto e a CD leem o atributo que aquele inimigo usa para atacar, **e o teto de pacto do §3 lê a Essência**.*

---

## Fecho — o Sukuna no nível 20, com tudo cruzado

*Isto é conta minha juntando as âncoras acima, não é citação. Cada número tem o dono do lado.*

| linha da ficha | valor | de onde |
|---|---|---|
| categoria | `Calamidade` | decisão já escrita em `26` §6.4, com o nome dele |
| exige | **`12` feiticeiros** (6 × 2, pela Expansão completa) | `26` §6.4 |
| vida | **`990`** | `26` §4.1, linha `Calamidade` / nv 20 |
| Integridade | **`990`** | `26` §3 — igual à vida máxima |
| dano por rodada | **`220`** | `26` §4.1 |
| ações por rodada | **`5`** (`6 − 1`) | `26` §4 e §4.2 |
| Defesa | **`18`** | `26` §3.1 |
| acerto | **`+8`** | `26` §3.1 |
| CD | **`16`** | `26` §3.1 |
| refino | **`7`** | `26` §3.1 |
| deslocamento | `9 m` | `26` §3 (peça 3 §3) |
| Reação | `1` por rodada | manual, `Inimigos` |
| Testes de Resistência treinados | `2` de `4` | `26` §3 (peça 7 §6) |
| Classe de feitiço do nível 20 | `5` — `15` pontos, `15` PE | `partA.js`, tabela mestra |
| pactos permanentes que ele pode ter | metade da Essência, pra baixo — **`3` se Essência `6`** | peça 22 §3.1 |
| teto de cada pacto | `0,50` fatia | peça 22 §3.2 |

**Duas travas que valem lembrar antes de montar:**

1. **Imunidade a `Físicos` custa mais de um degrau, e a `Calamidade` já é o topo da escada.** Pela peça 26 §6.3, *"ela só existe num inimigo que já esteja abaixo do topo"*. **Então um Sukuna `Calamidade` NÃO pode ter imunidade a Físicos sem estourar a régua.** Resistência a `Físicos` (um degrau) também já não tem pra onde subir. Se você quiser isso nele, tem que montar com a linha da `Alcateia` — e a `Calamidade` não tem linha de baixo pra Expansão, então as duas coisas juntas não cabem.

2. **Condição num chefe de `5` ações.** A régua da peça 19 §2.2 foi medida com o chefe em `3` ações (`Alcateia`). Uma `Calamidade` age `5`. **O `Atordoado` continua tirando UMA ação** — de cinco, agora, não de três. Ele fica proporcionalmente mais barato contra ele. **A peça 19 não recalcula isso, e eu não achei nenhum lugar que recalcule. NÃO CONFIRMADO se a régua vale igual numa `Calamidade`.**

---

## O que NÃO abriu

**Lista honesta. Nada aqui foi arredondado nem inventado.**

### 1. Uma peça chamada "Fundamento" não existe em `03-mecanica/`
O que eu achei foi que **"Fundamento" é o nome do manual** (`manual/Fundamento-MANUAL-v7.docx`), e a máquina de montar feitiço mora no gerador dele (`manual/gerador/partA.js` a `partF.js`). **Se você esperava uma peça numerada com esse nome, ela não está lá.** Confirmei por `grep` no diretório inteiro.

### 2. "AREA com preço por formato" — a pergunta tem resposta, e a resposta é "o sistema não separa"
Eu achei o preço (`Leve` pros três: Cone, Linha, Explosão) e confirmei em três fontes. **Mas se você esperava preços diferentes por formato, eles não existem.** O que difere entre os três é tamanho e escada, não custo.

### 3. A régua de condição numa `Calamidade` de 5 ações
A peça 19 §2.2 mede tudo com o chefe em `3` ações, e diz que `3` é piso. **A `Calamidade` age `5`.** Nenhum documento que eu abri refaz a conta pra `5`. **NÃO CONFIRMADO** que os níveis das treze condições continuem valendo iguais contra ela.

### 4. "A partir de quantos tipos a resistência começa a custar"
**A peça 26 §6.3 não conta tipos, ela cobra por grupo.** Não existe no texto uma frase de limiar por contagem. A linha `um tipo só` (`20%`, `1,11×`) está na tabela **sem preço em degrau declarado**. Se você precisa dessa regra, ela **não está escrita**.

### 5. Os arquivos que eu NÃO abri inteiros
Por tempo, não li linha a linha: `partB.js`, o resto de `partA.js`/`partC.js`/`partE.js`/`partF.js`, e as peças `01`, `02`, `03`, `05`, `07`, `11`, `14`, `15`, `23`, `24`, `25`. **Os donos que a peça 19 §2.2 cita (peça 11 §8 pra vantagem, peça 5 §4 pra dano evitado) eu reportei como a peça 19 os escreve — eu NÃO fui até a peça 11 nem a peça 5 conferir na fonte.** Se esses dois números forem load-bearing pra sua ficha, vale abrir os dois.

### 6. Os `.docx` e o `.pdf`
Não abri `manual/Fundamento-MANUAL-v7.docx` nem o `.pdf`. **Li o gerador, que é a fonte de verdade deles.** Se o `.docx` publicado estiver desatualizado em relação ao gerador, eu não teria como perceber. O `.docx` é de `set 7 01:34` e o `partD.js` é de `set 7 01:34` também, então provavelmente estão em dia — mas **NÃO CONFIRMADO**.

### 7. Os validadores `.py`
Não rodei nenhum. O `conferir-dano.py`, o `conferir-bestiario.py` e o `conferir-manual.py` são quem prova que os números batem. **Eu li as tabelas, não rodei as contas.** Se você quiser os números conferidos e não só lidos, é rodar eles.

### 8. Uma coisa que muda de status e vale saber
A peça 19 §2.1 avisa que **a régua mudou na v0.201** — os três números de tier deixaram de ser o teste e viraram só o preço, e o teste virou dominância contra `3,00×`. **Se você tiver anotação antiga do sistema comparando condição contra teto, ela está velha.** O mesmo vale pro chefe: a v0.200 usava um chefe de `72` no nível 30, e hoje é `219`. Números de antes dessa virada não valem mais.

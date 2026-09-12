# A tabela dos seis papéis — no molde do Draw Steel, com a disciplina do 4e

*10/09/2026. Construída em `construir-os-cambios.py`, saída em `SAIDA-dos-cambios.txt`. A medição que
a sustenta está em `MEDIDA-o-papel.md`.*

> ***Decisão do Mizuki:*** *"Da mesma forma que Draw Steel faz… Se n tiver as conversões nas fichas de
> inimigos, n tem problema, a gente cria."* · *"a questão nunca é 'não tem' é 'não tem AINDA, vale a
> pena fazer?'"*

---

## O invariante, e por que ele não podia ser "dano por rodada"

**Vida é estoque e dano é fluxo. Somar os dois esconde a não-linearidade da Defesa.** *A forma que
fecha é a do invariante:*

> ### o que o encontro custa ∝ **`vida EFETIVA` × `dano`**, com `vida efetiva` = `vida crua ÷ chance de o PC acertar`
> **Um papel é NEUTRO quando o produto dos multiplicadores dele dá `1,000`.**

*O `Desastre` nv30: Defesa `20`, o PC acerta `50%` (peça 1 §5.2), vida crua `945`, **vida efetiva `1890`**.*

---

## 1 · Os câmbios — e cada linha diz se é regra, derivação ou construção

| eixo | multiplica | em que | de onde vem |
|---|---|---|---|
| `Defesa +1` | **`1,111×`** | vida efetiva | derivado — `5` pp num `d20`, peça 1 §5.2 |
| `Defesa +2` | **`1,250×`** | vida efetiva | derivado — idem |
| `Defesa −1` | **`0,909×`** | vida efetiva | derivado — idem |
| `Defesa −2` | **`0,833×`** | vida efetiva | derivado — idem |
| `vida crua ×1,20` | `1,200×` | vida efetiva | a própria célula |
| `vida crua ×0,80` | `0,800×` | vida efetiva | a própria célula |
| `1` ação a menos (de `3`) | `0,667×` | dano | derivado — a escada |
| **ALCANCE** (taxa fixa, `f = 1/3`) | **`1,167×`** | dano | 🔨 **CONSTRUÍDO** — peça 14 §5.2.1 + extensão |
| **vantagem na 1ª rodada** | **`1,159×`** | dano | 🔨 **CONSTRUÍDO** — peça 19 §2.2 + peça 26 §3.1 |
| vantagem a luta inteira | `1,476×` | dano | 🔨 construído — idem |
| `1 m` de deslocamento | `0,60` de dano/rodada | dano | publicado — peça 5 §4 |
| dano negado num aliado | `1 pra 1` | dano | publicado — peça 19 §2.2 |

### ⚠ A não-linearidade, e ela muda como a tabela se usa

> **`Defesa +1` multiplica a vida efetiva por `1,111`; `Defesa −1` por `0,909`.**
> **`1,111 × 0,909 = 1,010`, e não `1,000`.**
>
> *`1/x` é convexo.* **Então `+1` e `−1` de Defesa NÃO são o mesmo degrau**, e um papel que troca
> Defesa tem de usar o multiplicador **do lado em que ele está indo**.

---

## 2 · O câmbio de ALCANCE — construído, e a posição do sistema sobreviveu

**O sistema já tinha posição declarada, e ela é melhor que *"não tem preço"*:**

> *"alcance de arma não tem preço neste sistema. A propriedade `Longo Alcance` custa `1` ponto para
> toda arma que a tem, e **ela custa esse ponto por existir — não por quanto**."* — peça 14 §5.2.2

> ### ⟹ O câmbio é TAXA FIXA por ter alcance, não preço por metro. Um `Artilheiro` de `18 m` e um de `30 m` pagam o mesmo.

**A derivação usa duas regras publicadas e uma extensão declarada:**

| o que a peça 14 §5.2.1 já diz | |
|---|---|
| o de corpo a corpo **fora** do alcance | **não alcança — entrega ZERO** |
| o de projétil **colado** | **desvantagem — entrega METADE** *(`−25` pp contra alvo difícil, que é metade do dano)* |

**A extensão, declarada:** *a regra é escrita pra **arma** de projétil. Estender ela pra **técnica de
inimigo** à distância é o passo que esta construção dá.* **Sem ele não existe câmbio nenhum.**

> **Quem luta de longe perde metade quando está no lugar errado; quem luta de perto perde tudo.**
> ### valor do alcance = `f` × (`100%` − `50%`) × dano por rodada

**E `f` é parâmetro de MESA, não de regra** — é mapa. *Então vai como faixa:*

| `f` | vale | `%` da cota | em vida, na luta | `%` da vida |
|---|---|---|---|---|
| `1/6` — meio turno de aproximação | `18,25` | `8,3%` | `55` | `5,8%` |
| **`1/3` — UMA rodada de três** | **`36,50`** | **`16,7%`** | **`110`** | **`11,6%`** |
| `1/2` — metade da luta | `54,75` | `25,0%` | `164` | `17,4%` |

**O padrão `f = 1/3` sai da própria escada:** *a luta do `Desastre` contra a mesa de quatro dura
`3,0` rodadas, e a primeira é a rodada de aproximação.* **Uma de três.**

### O contra-teste contra o campo

| | cobra pelo alcance |
|---|---|
| o `Artillery` do 4e | **`42%`** da durabilidade |
| **este câmbio** | **`12%`** |
| o câmbio de metro de *deslocamento* (o que eu tinha antes) | `3%` |

> **A construção fechou `4×` da distância que faltava.** *Ainda é `3,6×` mais barato que o 4e — e isso
> é honesto: o 4e cobra por um alcance que funciona num grid de quadrados, e esta conta cobra por
> uma rodada de aproximação numa luta de três.*

---

## 3 · O câmbio de ESCONDER — o eixo do `Emboscador`

**Ele não pode concentrar dano** — `2` ações joga `o golpe` em `45%` da vida de um personagem, que é
**o número que matou a `Dupla`**. *Então o eixo dele é vantagem.*

*O inimigo acerta `50%` a `55%` (peça 26 §3.1), média `52%`. Vantagem dá `+25` pp (peça 19 §2.2) →
`78%`.*

> ### Vantagem multiplica o dano daquele ataque por `1,48` — `+48%`.

| o que o `Emboscador` ganha | vale | `%` da cota | em vida |
|---|---|---|---|
| vantagem no **primeiro ataque** da luta | `11,59` | `5,3%` | `35` |
| **vantagem em toda a primeira RODADA** | **`34,76`** | **`15,9%`** | **`104`** |
| vantagem em todo ataque, a luta inteira | `104,29` | `47,6%` | `313` |

> **A de baixo custaria `33%` da vida dele, e ele só tem `100%`.** *Ela é grande demais pra um papel
> de graça.*

---

# 4 · A TABELA — os seis papéis, montados pra fechar em `1,000`

*Cada linha é o que muda no bloco. O produto dos multiplicadores é `1,000` em todas.*

> ## ⚠ ATUALIZADA na v0.223/v0.224 do `Claude 2` — esta tabela estava DUAS decisões atrás
> **Ela publicava a PRIMEIRA forma do `Controlador`**, a que cortava um terço do dano e tirava uma ação. *Aquela forma morreu porque jogava `o golpe` abaixo do piso da banda em quatro de quatro categorias; a forma `A`, que cortava por categoria, morreu porque comprava fração de ação.* **A viva é a forma `B`: ele nega uma ação inteira e paga em VIDA, e `o golpe` não se move.** *`DECIDIDO-o-controlador-por-categoria.md`.*
>
> **E os nomes fecharam:** *`Guardião` virou **`Baluarte`** (a raiz `Guarda` já é Melhoria no manual) e `Apoio` virou **`Reforço`** (`Apoio` é Forma no manual e entrada do glossário).*
>
> **A tabela viva mora agora na peça 26 §3.4**, com a checagem `10` do `conferir-bestiario.py` em cima dela. *Esta aqui é o registro de como ela foi construída.*

| papel | o que ele GANHA | o que ele PAGA | produto |
|---|---|---|---|
| **`Brutamontes`** | `vida crua × 1,20` *(`1,200×`)* | **`Defesa −2`** *(`0,833×`)* | **`1,000`** |
| **`Baluarte`** | **`Defesa +2`** *(`1,250×`)* | `vida crua × 0,80` *(`0,800×`)* | **`1,000`** |
| **`Artilheiro`** | **alcance**, taxa fixa *(`1,167×`)* | `vida crua × 0,857` *(`0,857×`)* | **`1,000`** |
| **`Emboscador`** | **vantagem em UM ataque por rodada** *(`1,159×` no `Desastre`)* | `vida crua × 0,863` *(`0,863×`)* | **`1,000`** |
| **`Controlador`** | `1` ação negada do grupo *(`1,333×` no `Desastre`)* | **`vida crua × 0,750`** — *forma `B`* | **`1,000`** — *`1 pra 1`, peça 19 §2.2* |
| **`Reforço`** | o mesmo `1 pra 1`, **em outro bloco** | **`vida crua`**, pelo mesmo câmbio do `Controlador` | **`1,000`** |

### O `Desastre` nv30 com cada papel, já preenchido

*A vida de um personagem no nv30 é `243`, derivada de `golpe ÷ fatia`.*

| papel | Defesa | vida crua | dano | ações | `o golpe` | fatia | **fora da ficha** | **invariante** |
|---|---|---|---|---|---|---|---|---|
| ‹ sem papel › | `20` | `945` | `219` | `3` | `73` | `30%` | `1,000×` | **`1,000×`** |
| **`Brutamontes`** | **`18`** | **`1134`** | `219` | `3` | `73` | `30%` | `1,000×` | **`1,000×`** |
| **`Baluarte`** | **`22`** | **`756`** | `219` | `3` | `73` | `30%` | `1,000×` | **`1,000×`** |
| **`Artilheiro`** | `20` | **`810`** | `219` | `3` | `73` | `30%` | **`1,167×`** | **`1,000×`** |
| **`Emboscador`** | `20` | **`816`** | `219` | `3` | `73` | `30%` | **`1,159×`** | **`1,000×`** |
| **`Controlador`** | `20` | **`709`** | `219` | `3` | `73` | `30%` | **`1,333×`** | **`1,000×`** |

> ### Olhe a coluna `o golpe`: ela NÃO SE MOVE em nenhum dos seis.
> **`30%` em todos.** *E é isso que faz a tabela ser legal: a banda de `21%`–`32%` nunca entra no
> caminho, porque **nenhum papel sobe o dano**.*
>
> **E o `invariante` fecha em `1,000×` nos seis.** *O encontro não mudou de tamanho.*

### ⚠⚠ E a coluna `fora da ficha` achou um problema de LEGIBILIDADE, não de equilíbrio

**O `Artilheiro` e o `Emboscador` têm o ganho FORA de célula nenhuma.**

> **O pagamento deles aparece no bloco — vida `810` em vez de `945`. O ganho não aparece.**
> *Quem lê o bloco vê um `Desastre` com `135` de vida faltando e nada explicando.*

> ### E isso confirma, por outro caminho, a decisão de pôr o papel no CABEÇALHO.
> **A palavra `Artilheiro` é a única coisa no bloco que diz pra onde os `135` de vida foram.**
> *Sem ela, o bloco parece um `Desastre` mal montado.*

*O `Brutamontes`, o `Guardião` e o `Controlador` não têm esse problema: as duas metades da troca
deles aparecem em célula.*

### E é por isso que o `Artilheiro` e o `Emboscador` pagam em VIDA, não em dano

**Pagar em dano significaria subir o dano de algum outro**, e a banda só dá `1,07×` de espaço num
`Desastre`. *Pagar em vida não encosta na banda.*

> **Isso responde a tua pergunta sobre o `Artilheiro` convertendo *"vida em dano"*:** **a conversão é
> `vida → alcance`, e não `vida → dano`.** *O alcance faz o dano que ele JÁ TEM chegar mais vezes —
> que é o mesmo efeito, sem tocar na célula que a banda vigia.*

---

## 5 · O que ficou aberto, e é escolha de sabor

| # | a escolha | o trade-off calculado |
|---|---|---|
| **1** | **o tamanho do degrau** | `Defesa ∓2` / `vida ×1,20` é um degrau de `~20%`. `Defesa ∓1` / `vida ×1,10` é metade disso. **Degrau grande = papel que se sente na mesa; degrau pequeno = papel que quase não aparece** |
| **2** | **o `f` do alcance** | `1/3` dá `12%` da vida. `1/6` dá `6%` — *o `Artilheiro` fica quase igual a um bloco sem papel.* `1/2` dá `17%` |
| **3** | **o `Emboscador`** | vantagem na 1ª rodada é o neutro. **Vantagem a luta inteira custaria `33%` da vida dele** — ele ficaria com `633` de vida crua num `Desastre`, que é vidro |
| **4** | **o `Controlador`** | a montagem acima tira `1` ação **das `3`** e devolve `1,50×` de vida. *Num `Capanga` ou numa `Ameaça`, que têm `1` ação, isso não existe — eles ficariam com zero ações.* **Falta decidir o que o `Controlador` faz nas categorias de `1` ação** |

---

# 6 · O `Emboscador` foi CONSERTADO, e a crítica do Mizuki tem nome publicado

***Pergunta dele, 10/09/2026:*** *"vantagem na primeira rodada inteira é bom, mas acredito q ter SO
ISSO o faz meio atrás de todos os outros, já q os outros ainda vão ter o resto do combate
'funcionais'."*

> ### Ele está certo, e o defeito já foi medido e batizado: **"the Lurker Fallacy"**.

*Alphastream, 2015 — https://alphastream.org/index.php/2015/10/15/the-lurker-fallacy/*

| o que o artigo mede | |
|---|---|
| a conta | um `Twig Blight` do 4e **entrega MAIS dano total atacando todo turno** do que esconde-e-golpeia |
| a frase | ***"it does more damage by not being a lurker!"*** |
| os outros defeitos | *custo de oportunidade* (dano agora vale mais que dano depois), *vulnerabilidade a controle* (atordoar ele antes do golpão anula o papel inteiro), e *o fogo que ele não toma, os aliados tomam* |

### E o conserto é do próprio 4e, num livro posterior

**`Monster Vault: Nentir Vale` publicou o `Joplin the Sly`, e o artigo elogia exatamente isto:**

> ***"Attacking every round, bonuses when lurking, cool encounter power, synergies with allies… YES!"***

> ### ⟹ O ganho tem de ser TODA RODADA, não uma abertura só.

### O Draw Steel diz o mesmo, por outro caminho

*O `Ambusher` deles é **"melee warriors who can slip by beefier heroes to reach squishier targets in
the back lines. Ambusher creatures can hide, turn invisible, or otherwise find ways to get the drop
on their enemies."*** **Esconder é UMA ferramenta dele, não o truque único.**

*E uma linha do Draw Steel que vale registrar, porque ela fecha a correção de precedente do §6 da
`MEDIDA`:* **"Roles are descriptive, and most don't follow special rules — they simply help you build
encounters and use creatures effectively in combat."**

---

## A forma corrigida: **vantagem em UM ataque por rodada, toda rodada**

| categoria | ações | o ganho | multiplica o dano | **paga em vida** |
|---|---|---|---|---|
| **`Capanga`** 🆕 | `1` | `+48%` em `1` de `1` | **`1,476×`** | `× 0,677` |
| `Ameaça` | `1` | `+48%` em `1` de `1` | **`1,476×`** | `× 0,677` |
| **`Desastre`** | `3` | `+48%` em `1` de `3` | **`1,159×`** | **`× 0,863`** |
| `Catástrofe` | `5` | `+48%` em `1` de `5` | `1,095×` | `× 0,913` |
| `Calamidade` | `6` | `+48%` em `1` de `6` | `1,079×` | `× 0,927` |

**No `Desastre` o número é IDÊNTICO ao da versão de primeira rodada** — `1,159×` nos dois —, *porque
ali ações e rodadas são os dois `3`.* **O que muda é a distribuição, e é ela que conserta o defeito.**

> ⚠ **O ganho encolhe nas categorias grandes**, porque `1` ataque de `6` é menos que `1` de `3`. *Então
> o pagamento encolhe junto, e a linha do `Emboscador` passa a ter um valor por categoria.*
>
> **E isso não custa bookkeeping novo:** *a escada do bestiário **já é** uma tabela por categoria.*

> ### ⚠⚠ E A LINHA DO `Capanga` FALTAVA — achada em 10/09 montando a ficha do Kama-itachi
> **Esta tabela foi escrita antes de o `Capanga` tomar papel** *(item `17`, `fila/DECIDIDO-o-capanga.md`
> §2, mesmo dia)*. **Ele tem `1` ação, então a linha dele é a da `Ameaça`: ganho `1,476×`, paga
> `× 0,677`.**
>
> ⚠ **E o buraco era real, mas não era o que eu tinha escrito.** *Eu publiquei que o `Emboscador` num
> corpo de `1` ação furava o invariante em `27,7%`.* **Não fura: `1,476 × 0,677 = 0,999`.** *O `1,277`
> saiu de aplicar o `0,863` do `Desastre` num corpo de uma ação — erro do meu script, não do desenho.*
>
> ### ⟹ O perigo de verdade é o `0,863` do resumo do §4 ser lido como se fosse universal.
> **O §4 publica a linha do `Desastre` e o `RASCUNHO-5` copia ela com um *"(varia por categoria)"* em
> itálico.** *Foi exatamente nisso que eu tropecei.* **A correção é o §4 e o `RASCUNHO-5` mandarem pra
> esta tabela em vez de imprimir um número que só vale numa categoria.**

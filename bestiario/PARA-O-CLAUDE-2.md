# PARA O `Claude 2` — tudo que o Bestiário decidiu e não pode escrever

*Fechado em 10/09/2026 (noite). **Este arquivo é a entrega.** Quem tem a escrita no repositório
`Claude 2` lê só ele — o resto do `Bestiario/` é o porquê.*

> ## ⚠ Regra do Bestiário: este projeto NUNCA escreve no `Claude 2`.
> **Ele lê, mede e entrega a conta.** *Toda decisão abaixo já tem laudo, script e âncora do lado de cá.*

---

# § 0 · O MAPA — quatro commits e uma sobra

| # | commit | arquivos | estado |
|---|---|---|---|
| **`A`** | **a peça 26** | `26-bestiario.md` + `conferir-bestiario.py` | `11` mexidas + validador |
| **`B`** | **o gerador de FEITIÇO** | `partC.js` · `partD.js` | `3` mexidas |
| **`C`** | **o gerador de INIMIGO** | `dados.js` · `make.js` · `COMO-USAR.txt` · `conferir-ficha.py` | 🆕 **`18` mexidas** |
| **`D`** | **a peça 15** | `15-invocacoes.md` | 🆕 **`5` mexidas**, e ⚠ **uma tem pergunta de desenho** |
| **`E`** | a `Sobrecarga` | `partD.js` · `40-fundamento.md` + `5` dependências | `3` donos, `6` passos |

> ### ⚠ `A` e `D` são o mesmo assunto e commits DIFERENTES.
> *A peça 15 só quebra **porque** a peça 26 muda.* **Se a `A` entrar sem a `D`, a peça 15 fica publicando
> uma tabela cujo maior número não existe mais** — e nenhum validador acusa, porque não existe checagem
> ligando as duas.

## ⚠⚠ E TRÊS SOBRAS que não são commit de regra, mas ficam erradas se ninguém tocar

| arquivo | linhas | o quê |
|---|---|---|
| `sistema/ESTADO-ATUAL.md` | `6` | a escada morta descrita como viva |
| `sistema/04-playtest/mesa-01-grupo-01.md` | `3` | registro de mesa real com `Ronda`/`Alcateia` |
| `logs/CHANGELOG.md` | — | entrada nova, e marcar a **v0.220 como revertida** |

*E `finalizado/regra/` é **espelho byte a byte** — outro repo git, recortado da fonte, e a **checagem `7`
do `conferir-repositorio.py`** é a dona da comparação. **Não é edição a mais: é um push a mais.***

---
---

# § A · O COMMIT DA PEÇA 26 — `11` mexidas + o validador

*Detalhe em `04-fase-1/sobrecarga/MEXIDAS-no-repositorio.md`. **Todas no mesmo arquivo — um commit só,
senão são quatro passadas na peça.***

| # | seção | o que trocar | de onde vem |
|---|---|---|---|
| `1` | **§5** | *"um corpo grande vale **quatro** pequenos"* ⟹ **`oito`**, e a derivação vira `vida = dano do grupo ÷ 4` · `dano = fator 0,25`. ⚠ **a prova dos "nove golpes" cai junto** | `fila/DECIDIDO-o-capanga-unico.md` |
| `2` | **§4.5** | a tabela inteira: `100%` · **`91,5%`** · **`83,0%`** · **`74,5%`**, com UMA casa decimal | idem |
| `3` | **§4.3** | *"o capanga é um quarto da vida com um TERÇO do dano"* ⟹ **`1/12` da vida com um QUARTO do dano** | idem |
| `4` | **§4.3** | a comparação com a `Ronda` (`0,75×`–`0,77×`) é da escada morta — **sai, ou vira a medição nova** | idem |
| `5` | **§6.3** | *"Resistência a `Físicos` custa um degrau de categoria"* ⟹ **"multiplica o fator por `1,43`"** | `fila/DECIDIDO-o-degrau.md` §5 |
| `6` | **§6.3** | *"custa mais de um degrau, e a escada não tem o que vender acima da `Calamidade`"* ⟹ **"multiplica o fator por `2,50`, e o resultado é um número de pessoas, não um nome"** | idem |
| `7` | **§6.4** | tirar *"os dois degraus de baixo valem `2,00×`"* e trocar *"dobra a categoria"* por **"multiplica o fator por `1,92`"** | idem |
| `8` | **§6.5** | a linha do câmbio: *"um degrau de categoria, pelo §6.3"* ⟹ **"multiplica o fator, pelo §6.3"** | idem |
| `9` | **§6.5** | tirar *"as ações fora do turno saem das que ele já tem, **NUNCA POR CIMA**"* e pôr o **`× 0,923`** | item `6` |
| `10` | **§6.5** | tirar *"área reparte a cota"* e escrever **`1` ação em área à vontade; `Recarga` não conta na cota** | `fila/DECIDIDO-o-aperto-e-a-area.md` §2 |
| `11` | **§6.5** | corrigir o `0,70×` da cura pra **`0,64×`** | item `6` |
| `12` | **§6.3** 🆕 | ➕ **linha nova:** *"Ser imune a uma condição que rouba ação do inimigo, ou que dá desvantagem nos ataques dele, multiplica o fator por `1,20`. Qualquer outra condição custa `1,00×`."* | `fila/MEDIDA-a-imunidade-a-condicao.md` |
| `13` | **§6.3** 🆕 | ➕ **linha nova, de aviso:** *"Um `Desastre` imune a `Físicos` exige `10` personagens, não `4`. A edição viva do D&D publica isso zero vezes em `331` blocos."* ⚠ **aviso, não trava** | `fila/DECIDIDO-a-resistencia-e-a-vulnerabilidade.md` |
| `14` | **§6.3** | *"**Vulnerabilidade devolve na mesma moeda**"* ⟹ **"a vulnerabilidade é `1,00×`: não cobra e não devolve"** | idem |
| `15` | **§6.3** | *"Um chefe de **`Alcateia`** imune a `Físicos` vira uma luta de `7,50` rodadas…"* — **`2` menções à escada morta.** Trocar pela categoria viva **e refazer o exemplo com a vida nova** | idem |

## E o validador

| | |
|---|---|
| **checagem `5`** do `conferir-bestiario.py` | o câmbio publicado `4` ⟹ **`8`**. ⚠ **Ela está VERMELHA hoje, e está CERTA em acender** |
| **checagem `8`** | ela exige que a peça **declare** a moeda, não que a moeda seja "degrau". ✅ **Trocar a declaração mantém ela verde** |

---
---

# § B · O COMMIT DO GERADOR DE FEITIÇO — `3` mexidas

*`fila/DECIDIDO-o-cone-o-anteparo-e-o-espalhamento.md`. **Commit separado: não é a peça 26.***

| # | arquivo | o quê | risco |
|---|---|---|---|
| `27` | `partC.js`, Forma `Cone` | ➕ *"A largura do cone em qualquer ponto é igual à distância daquele ponto até você."* | 🟢 **nenhum** |
| `28` | `partD.js`, Melhoria `Anteparo` | ➕ *"Ocupa os mesmos quadrados que a `Linha` da Classe dele, arrumados como você quiser, cada um partilhando um lado com outro. Altura mínima `2` quadrados."* | 🟢 **nenhum** |
| `29b` | `partC.js`, Forma `Linha` | ➕ *"Quando o comprimento chega ao topo da escada, `Maior` passa a subir a LARGURA: `1,5 → 3 → 4,5 m`."* | 🟢 baixo |

> ### ❌ E o `29a` é **NÃO FAZER**. *Repreçar as três formas foi REPROVADO por medição:* o nosso
> espalhamento na base é `2,79×`, **idêntico ao do D&D 2024**.

---
---

# § C · 🆕 O COMMIT DO GERADOR DE INIMIGO — e ele NÃO estava em lista nenhuma

*`fila/MEDIDA-o-remapeamento-das-seis.md` · `fila/DECIDIDO-as-seis-prontas.md` ·
conta em `fila/medir-a-dupla.py`.*

> ### ⚠ A `MEXIDAS-no-repositorio.md` cobre a peça 26 e o gerador de FEITIÇO.
> **O `gerador-inimigo/` não é nenhum dos dois.** *Quem executar os commits `A` e `B` e der por fechado
> deixa as seis maldições prontas penduradas numa escada que não existe.*

## C.1 · O mapa das seis — **esta tabela é a fonte**

| ficha | faixa | de | ⟹ **para** | corpos | como fechou |
|---|---|---|---|---|---|
| `Betobeto` | `2 a 4` | `Ronda` | **`Ameaça`** | `1` | conferência `29`/`29` |
| `Kamaitachi` | `2 a 4` | `Dupla` | **`Ameaça`** | ### **`2`** | martelo dele |
| `Tsuchigumo` | `2 a 4` | `Alcateia` | **`Desastre`** | `1` | conferência `29`/`29` |
| `Hitotsume` | `5 a 8` | `Ronda` | **`Ameaça`** | `1` | conferência `29`/`29` |
| `Kitsune` | ### **`9 a 12`** | `Dupla` | **`Ameaça`** | `1` | martelo dele — ⚠ **a FAIXA muda** |
| `Oni` | `5 a 8` | `Alcateia` | **`Desastre`** | `1` | conferência `29`/`29` |

> ### ⚠⚠ TRÊS ARMADILHAS, e as três derrubam quem executa de cabeça
>
> **`1` · `Alcateia` NÃO vira `Capanga`.** *Vira `Desastre`.* **`12,00×` de distância em vida.** A peça
> 26 §4.3 já separa os dois: *"o capanga do manual **não é** uma `Ronda`"*.
>
> **`2` · `Calamidade` NÃO é renomeação.** *A morta é `6` pessoas / fator `1,50`; a viva é `8` / `2,00`.*
> **A `Calamidade` morta vira `Catástrofe`, e uma `Calamidade` NOVA entra por cima.**
>
> **`3` · A `Kitsune` muda de FAIXA, não só de categoria.** *`5 a 8` ⟹ `9 a 12`. É a única.*

## C.2 · As mexidas, com linha

### `dados.js` — `13` linhas

| # | linha | o quê |
|---|---|---|
| `1` | `L21` | comentário *"As quatro categorias da peça 26"* ⟹ **cinco** |
| `2` | `L24-27` | `CATEGORIAS`: os quatro degraus ⟹ os cinco vivos — `Capanga` `0,25` · `Ameaça` `0,25` · `Desastre` `1,00` · `Catástrofe` `1,50` · `Calamidade` `2,00` |
| `3` | `L65` | `SUBCATEGORIAS`: `68`/`58`/`56`/`62` ⟹ **`100%` · `91,5%` · `83,0%` · `74,5%`** |
| `4` | `L69` + `L115` | `RONDA_CONTRA_ALCATEIA` `[0.75, 0.77]` é da escada morta — **sai, ou vira a medição nova** |
| `5` | `L77` | a derivação do seis: *"as QUATRO categorias — oito células"* ⟹ **`2` faixas × `3` categorias.** ⚠ *e ver o `C.3`* |
| `6` | `L83` · `L98` | `Betobeto` e `Hitotsume` ⟹ **`Ameaça`** |
| `7` | `L93` · `L108` | `Tsuchigumo` e `Oni` ⟹ **`Desastre`** |
| `8` | `L88` | `Kamaitachi` ⟹ **`Ameaça`**, e a linha dela precisa dizer que são **DOIS corpos** *(ver `C.4`)* |
| `9` | `L103` | `Kitsune` ⟹ **`Ameaça`**, e `faixa: '9 a 12'` |
| `9b` 🆕 | `PRONTAS` | ⚠ **`Tsuchigumo` e `Oni` ganham `3` `Intervenções` cada, e o golpe delas leva `× 0,923`.** *Martelo dele, 10/09 (noite). O texto pronto das três de cada uma está em `08-livro/capitulos/80-seis-maldicoes.md`* |
| `10` | `L117` | `CAMBIO = 4` ⟹ **`8`** *(é a mesma checagem `5` da peça 26)* |

### `make.js` — `11` linhas

| # | linha | o quê |
|---|---|---|
| `11` | `L111` | ⚠ **a instrução ao mestre:** *"`Ronda` é um, `Dupla` é dois, `Alcateia` é quatro, `Calamidade` é seis"* — **é a frase que ENSINA a escada, e as quatro estão mortas** |
| `12` | `L115` · `L260` | o exemplo: *"Isso é uma `Alcateia`: `475` de vida"* ⟹ **`Desastre`** |
| `13` | `L131` · `L133` | *"a `Dupla` bate mais forte que a `Calamidade`"* — **as duas sumiram da frase** |
| `14` | `L150` | *"Um chefe de `Alcateia` vale `${CAMBIO}` capangas […] Quatro `Ronda` não valem uma `Alcateia`"* |
| `15` | `L176` | ⚠⚠ *"Imunidade a `Físicos` custa mais de um degrau, e **não existe degrau acima da `Calamidade`**"* — **é LITERALMENTE a frase que a mexida `6` da peça 26 mata.** *A `MEXIDAS` marcou a cópia da peça; ninguém tinha visto a do gerador — e **é essa que vai impressa**.* |
| `16` | `L281` | a derivação do seis, no texto impresso |
| `17` | `L318` | *"A `Calamidade` da faixa fica de fora porque exige **seis** feiticeiros"* — ⚠ **na escada viva quem exige seis é a `Catástrofe`; a `Calamidade` exige `8`.** *A frase continua verdadeira e passa a apontar pro bicho errado* |
| `18` | `L8` · `L100` | comentários de cabeçalho |

### E o resto

| | |
|---|---|
| `COMO-USAR.txt` `L9` | *"a mesma ficha, com uma `Alcateia` de nivel 10"* ⟹ **`Desastre`** |
| `conferir-ficha.py` bloco `7` | compara o `dados.js` com a peça 26 — **acende junto, e apaga junto** |
| **regenerar** | `bloco-de-inimigo.docx` **e** `bloco-de-inimigo.pdf` pelo `make.js` |

## C.3 · ⚠ O QUE A DECISÃO ABRE, e está declarado de propósito

**A grade viva fecha em `6` células** *(`2` faixas × `3` categorias que uma mesa de `4` aguenta)*.
**A decisão NÃO preenche essa grade** — a `Kitsune` subiu de faixa:

| faixa | `Capanga` | `Ameaça` | `Desastre` |
|---|---|---|---|
| `2 a 4` | ⚠ **vazio** | `Betobeto` · `Kamaitachi` *(×2)* | `Tsuchigumo` |
| `5 a 8` | ⚠ **vazio** | `Hitotsume` | `Oni` |
| `9 a 12` | — | `Kitsune` | — |

> **Duas saídas, e nenhuma é urgente:** *reescrever a derivação pra "seis porque são seis"*, ou
> **escrever `1` a `2` fichas de `Capanga` novas** *(é ficção, e é do Mizuki)*.
> ### É o preço da decisão, escolhido de olho aberto. Não é pendência.

## C.4 · ⚠ A sutileza do `Kamaitachi` — dois corpos, um bloco

**O `dados.js` tem UM campo `categoria` por ficha, e o `make.js` monta UM bloco.**

> ### A ficha dela é `Ameaça`, o bloco impresso é UM, e a dupla mora na FICÇÃO.
> *O mestre põe duas cópias na mesa — é como o campo escreve par e minion, e não pede campo novo.*
> ⚠ **Mas a linha dela tem de dizer isso, senão o mestre põe uma só.**
>
> *Custo medido: **`−25,0%`** de encontro contra a `Dupla` que ela era — que é o mesmo `0,75×` que o
> §4.3 já publica pra corpos repartidos, porque eles morrem em fila.*

---
---

# § D · 🆕🔴 O COMMIT DA PEÇA 15 — e ele tem uma PERGUNTA DE DESENHO dentro

*`fila/MEDIDA-a-peca-15.md` · conta em `fila/medir-a-peca-15.py`.*

> ### A peça 15 §"A morte em definitivo" calibra a morte do shikigami contra a tabela de golpe
> ### da peça 26 — pelo MÁXIMO da rolagem. **O topo da tabela dela é a `Dupla`.**

| | |
|---|---|
| o teto que ela mediu | `8d12 + 57` = **`153`** *(a `Dupla`)* |
| o teto que existe depois do commit `A`/`C` | `8d8 + 37` = **`101`** — **`1,51×` menor** |
| a ÚNICA linha "destrói" da peça | **o crítico da `Dupla`** |

## As mexidas

| # | onde | o quê |
|---|---|---|
| `1` | a tabela da morte | trocar as `5` linhas pela escada viva. ⚠ **a linha "destrói" muda de CONTEÚDO, não só de nome** |
| `2` | a frase de conclusão | *"precisa do crítico da maior categoria"* ⟹ **o crítico vivo (`16d8 + 37` = `165`) destrói o `Coro` (`154`) e NÃO destrói o corpo forte (`185`)** |
| `3` | a tabela do corpo machucado | **`2` de `4` linhas:** `em um quarto` de **`26%`** pra **não** · `a um ponto de cair` de **sempre** pra **`20%`** |
| `4` | a tabela da Constituição | ⚠ os `7%` · `70%` · `4%` · `68%` saíram todos da distribuição da `Dupla`. **Não recomputei: falta a fórmula do corpo por Con, que é do §3.7 da própria peça** |
| `5` | a tabela da morte | *"`Alcateia`, **que é também o capanga**"* — ⚠ **a peça 26 §4.3 diz o contrário com todas as letras** |

> ### ⚡ A guarda que prova que não é leitura minha:
> **as `4` linhas publicadas da tabela do corpo machucado reproduzem EXATO com o `8d12 + 57`.**
> *`26%` recomputa `26%`; `sempre` recomputa `sempre`.* ⟹ **a tabela FOI calibrada contra a `Dupla`.**

## ⚠⚠ E a pergunta de desenho, que é do Mizuki

**A régua ficou mais frouxa sem ninguém decidir isso.** *Antes, um crítico do topo destruía qualquer
corpo. Depois do commit, nenhum golpe destrói o corpo forte, e o gatilho de excedente caiu de
"sempre" pra `20%`.*

> ### ⟹ Ou a peça 15 registra que a morte definitiva virou coisa quase só do gatilho de excedente,
> ### ou o corpo forte encolhe.
> ***Não é pendência do Bestiário.*** *Está escrito aqui porque a conta está aqui.*

---
---

# § E · O COMMIT DA `Sobrecarga` — `3` donos e `5` dependências

*Detalhe completo em `04-fase-1/sobrecarga/MEXIDAS-no-repositorio.md`. **O texto fechado:***

> *"Até o fim do próximo turno do alvo, **ele não usa Reação**, e o feitiço dele sai com a CD `2` menor."*
> **Degrau `Leve`, Reação inteira.** *`decisoes-fase-1.md` §9.*

| | dono / dependência | o quê |
|---|---|---|
| `1` | `manual/gerador/partD.js` `L114` | o texto e o degrau |
| `2` | `sistema/05-material/livro/manual/40-fundamento.md` `L711` | o texto e o degrau — ⚠ **hoje ele diz `Pesada` e o `partD.js` diz `Leve`** |
| `3` | `manual/Fundamento-MANUAL-v7.docx` | **gerado.** Não se edita: regenera |
| `4` | `manual/matematica/sobrecarga.py` | **a conta inteira caduca** — a seção `METADE 1` deixa de existir |
| `5` | `livro/ESTADO-revisao.md` `L43` | a divergência passa de `aberta` pra `fechada na vX.YYY` |
| `6` | `conferir-acao.py` `L244` | a checagem `5` proíbe *"o dobro de energia"* **só na `Dívida`** — vale estender pra `Sobrecarga` |
| `7` | `sistema/ESTADO-ATUAL.md` `L1290` e `L1304` | **desatualizadas** — dizem que o inimigo VAI contar PE, e a decisão de 09/09 reverteu |
| `8` | `logs/CHANGELOG.md` | entrada nova, e **v0.220 marcada como revertida** |

## ⚠ A ordem que não trava o commit

**A v0.220 já ensinou a armadilha:** *registrar uma decisão que ainda não foi aplicada TRAVA o commit,
porque a checagem `12` passa a cobrar igualdade entre dois lados que ainda discordam.*

`1` muda os donos `1` e `2` com o **mesmo valor** · `2` regenera o `.docx` · `3` **só então** vira a
linha `43` · `4` refaz o `sobrecarga.py` · `5` estende a checagem `5` · `6` corrige o `ESTADO-ATUAL`
e escreve o CHANGELOG.

---
---

# § F · O QUE ACENDE E O QUE APAGA

| checagem | hoje | depois |
|---|---|---|
| **`5`** do `conferir-bestiario.py` — o câmbio | 🔴 **VERMELHA, e certa em acender** *(publicado `4`, implementado `8`)* | ✅ apaga com a mexida `A.1` + `C.10` |
| **`8`** do `conferir-bestiario.py` — a moeda | ✅ verde | ✅ **continua verde** — ela cobra que a peça DECLARE a moeda, não que seja "degrau" |
| **bloco `7`** do `conferir-ficha.py` | ✅ verde | ⚠ **acende entre `A` e `C`** — ele compara o `dados.js` com a peça 26 |
| **`12`** do `conferir-repositorio.py` | ✅ verde | ⚠ **acende se a linha `43` virar antes do passo `1`** |
| **`7`** do `conferir-repositorio.py` — o recorte | ✅ verde | ⚠ **acende até o `finalizado/` ser recortado de novo** |

> ### ⚠⚠ E NÃO EXISTE checagem ligando a peça 15 à peça 26.
> *Foi por isso que a tabela da morte do shikigami ficou pendurada num número morto e ninguém acusou.*
> **Se sobrar fôlego no commit `D`, vale escrever ela.**

---

# § G · ONDE ESTÁ CADA CONTA, do lado de cá

| o assunto | o laudo | o script |
|---|---|---|
| as seis prontas, o mapa | `04-fase-1/fila/MEDIDA-o-remapeamento-das-seis.md` | `fila/medir-a-dupla.py` |
| os dois martelos dele | `04-fase-1/fila/DECIDIDO-as-seis-prontas.md` | *(o `§10` do mesmo script confere)* |
| a peça 15 | `04-fase-1/fila/MEDIDA-a-peca-15.md` | `fila/medir-a-peca-15.py` |
| o `Capanga` único | `04-fase-1/fila/DECIDIDO-o-capanga-unico.md` | `fila/medir-o-encontro-misturado.py` |
| o degrau ⟹ fator | `04-fase-1/fila/DECIDIDO-o-degrau.md` | `fila/medir-o-degrau.py` |
| a resistência | `04-fase-1/fila/DECIDIDO-a-resistencia-e-a-vulnerabilidade.md` | `fila/medir-a-imunidade-a-condicao.py` |
| a área e a recarga | `04-fase-1/fila/DECIDIDO-o-aperto-e-a-area.md` | `fila/conferir-o-4-6-contra-area.py` |
| a `Sobrecarga` | `04-fase-1/sobrecarga/DECIDIDO-a-sobrecarga.md` | `sobrecarga/medir-a-metade-morta.py` |
| a escada viva, `29` níveis | `04-fase-1/TABELA.md` | — |
| o bloco em branco | `03-bloco/RASCUNHO-5-o-bloco-em-branco.md` | — |

**`34` scripts rodando, `0` falhando.** *Todos leem âncora de documento dono e morrem se ela mudar —
inclusive os que leem a peça 26 e a peça 15 do `Claude 2`.*

> ### ⟹ Depois que os commits entrarem, RODE os scripts do Bestiário.
> **Os que leem o repositório vão morrer com `ÂNCORA PERDIDA` apontando exatamente a frase que mudou.**
> *É de propósito: eles são a guarda do outro lado.*

# MEDIDA — as seis maldições prontas estão na escada MORTA

*10/09/2026. **Achado respondendo "o que falta?", depois que o catálogo fechou.***
**Conta rodada: `04-fase-1/fila/medir-as-seis-prontas.py`.**

> ## ⚠⚠ CAIXA DE CORREÇÃO — 10/09, mesma noite. O §4 passo `1` deste arquivo está ERRADO.
> **Conta em `fila/medir-a-dupla.py`, laudo em `fila/MEDIDA-o-remapeamento-das-seis.md`.**
>
> *Eu escrevi aqui "`Alcateia` era o esquadrão ⟹ `Capanga`".* ### **Não é.**
> **A `Alcateia` é `4` pessoas · fator `1,00` · `3` ações — e isso é o `Desastre`, exato nos três
> eixos e em `29`/`29` níveis nas quatro colunas.** *O `Capanga` é fator `0,25` e `8` corpos:
> `12,00×` de distância em vida.*
>
> **E a peça 26 §4.3 já separava os dois:** *"É por isso que o capanga do manual **não é** uma
> `Ronda`."* ⟹ *o capanga era eixo SEPARADO da escada, não um degrau dela.*
>
> ### 🆕 E apareceu uma armadilha que este arquivo não viu: o nome `Calamidade`.
> *A morta é `6` pessoas / fator `1,50`; a viva é `8` / `2,00`.* **O herdeiro da `Calamidade` morta é
> a `Catástrofe`.** ⚠ *Nenhuma das seis usa ela — mas o `make.js` imprime a escada INTEIRA no `.docx`.*
>
> ### 🆕 E a `Dupla` não ficou órfã por descuido: ela foi MORTA de propósito, e está escrito.
> *`a-escada-com-numero.md`: "**Foi isso que quebrou a `Dupla`**" · `A-TABELA-pontos-por-acao.md`:
> "A `Dupla` era o pico — `24,2` pontos, contra o teto de `24` do jogador. **Ela MORREU**."*

> ## ⟹ `6` de `6` estão numa escada que o projeto substituiu depois delas.

---

# § 1 · O que existe, e ninguém tinha olhado

**A peça 26 §8 registra `As maldições prontas` como FECHADAS na v0.214.** *Seis bichos do nível `2`
ao `6`, ficção de folclore japonês, dentro do `05-material/bloco-de-inimigo.docx`.*

**Elas existem, estão geradas, e têm validador próprio** *(o bloco `7` do `conferir-ficha.py`)*.
⟹ **O problema não é que faltam. É que a escada mudou depois delas.**

| ficha | nível | categoria | estado |
|---|---|---|---|
| `Betobeto` | `2 a 4` | `Ronda` | ❌ **morta** |
| `Kamaitachi` | `2 a 4` | `Dupla` | ❌ **morta** |
| `Tsuchigumo` | `2 a 4` | `Alcateia` | ❌ **morta** |
| `Hitotsume` | `5 a 8` | `Ronda` | ❌ **morta** |
| `Kitsune` | `5 a 8` | `Dupla` | ❌ **morta** |
| `Oni` | `5 a 8` | `Alcateia` | ❌ **morta** |

| | |
|---|---|
| a escada **de quando elas nasceram** | `Ronda` · `Dupla` · `Alcateia` · `Calamidade` |
| a escada **viva** *(`04-fase-1/TABELA.md`)* | `Capanga` · `Ameaça` · `Desastre` · `Catástrofe` · `Calamidade` |

**Em categoria viva: `0` de `6`.** *E nem o `Calamidade` salva ninguém — nenhuma das seis usa ele.*

---

# § 2 · ⚠ O que ISTO É, e o que NÃO é

| | |
|---|---|
| **não é** | **erro de conta.** *O gerador computa vida, dano, ações e golpe do `dados.js`. Por dentro elas fecham* |
| ### **é** | ### **ficha de LIVRO pendurada em vocabulário que não existe mais** |

> ### ⚠ E o agravante: o `bloco-de-inimigo.docx` é material de livro, não rascunho.
> *É o arquivo que o mestre abre.* **Um mestre que ler `Alcateia` ali e procurar `Alcateia` na peça 26
> nova não acha nada.**

## E o `dados.js` inteiro é da versão de antes

| | |
|---|---|
| `Ronda` | `4×` no arquivo |
| `Dupla` | `3×` |
| `Alcateia` | `5×` |
| o comentário *"As quatro categorias da peça 26"* | **ainda lá** — ⚠ *a escada viva tem **cinco*** |

> ### ⟹ É a SÉTIMA vez que este defeito aparece no projeto, e o padrão é sempre o mesmo:
> **a decisão andou e a tabela ficou.** *Aqui ela ficou num `.docx` publicado.*

---

# § 3 · ⚠⚠ E ISTO NÃO ESTAVA NA LISTA DE MEXIDAS

**A `sobrecarga/MEXIDAS-no-repositorio.md` tem `11` mexidas na peça 26 + o validador, e `3` no
gerador de FEITIÇO** *(`partC.js` / `partD.js`)*.

> ### O `gerador-inimigo/` não é nenhum dos dois. **Ele não está na lista.**
> ⟹ *Quem executar as mexidas de hoje e der o commit por fechado vai deixar as seis prontas pra trás.*

---

# § 4 · O que fazer — e é execução, não decisão

> ### ⚠ Não é trabalho deste projeto: é do `Claude 2`, e outra conta escreve lá.
> **Está registrado aqui pra entrar na lista de quem tem a escrita.**

> ### ⚠⚠ ESTA LISTA FOI SUBSTITUÍDA. A boa está em `MEDIDA-o-remapeamento-das-seis.md` §7,
> **com `24` linhas varridas por script nos dois arquivos do gerador** — não `5` a olho.
> *Fica aqui riscada com o porquê junto, pra ninguém reabrir pelo arquivo errado.*

| passo | o quê |
|---|---|
| **1** | remapear as seis pra escada viva. *`Ronda` era `1` personagem ⟹ `Ameaça`;* ~~*`Alcateia` era o esquadrão ⟹ `Capanga`*~~ ### ❌ **ERRADO — `Alcateia` ⟹ `Desastre`** *(caixa no topo)*; *`Dupla` não tem herdeiro direto* |
| **2** | ⚠ **decidir o que fazer com a `Dupla`** — *`2` das `6` são dela, e a escada nova não tem esse degrau* |
| **3** | trocar o comentário *"As quatro categorias"* por **cinco** |
| **4** | regenerar o `bloco-de-inimigo.docx` pelo `make.js` |
| **5** | conferir o bloco `7` do `conferir-ficha.py` — *ele compara o `dados.js` com a peça 26* |

> ### ⚠ O passo `2` é o único que não é mecânico.
> **A `Dupla` morreu sem herdeiro nomeado**, e duas fichas publicadas dependem dela.
> *Isso é martelo do Mizuki, com a conta a rodar antes.*
>
> ### ✅ A conta ROIDOU, e o martelo mudou de forma — `MEDIDA-o-remapeamento-das-seis.md` §4 e §6.
> **A `Kamaitachi` é barata** *(a ficção dela já é dois corpos)*. **A `Kitsune` não é:** *a linha dela
> é "a única da faixa que conjura", e **`0` de `6` saídas da escada viva conjuram no nv`5`–`8`** — nem
> o topo dela.* ⟹ *o martelo virou "salvar a ficha subindo a FAIXA, ou deixar ela virar bloco `seco`".*

---

## De onde saiu

**`medir-as-seis-prontas.py`** *(este projeto)* · **`sistema/05-material/gerador-inimigo/dados.js`**
*(dono das seis)* · **`sistema/03-mecanica/26-bestiario.md` §8** *(o registro de que fecharam)* ·
**`04-fase-1/TABELA.md`** *(a escada viva)*

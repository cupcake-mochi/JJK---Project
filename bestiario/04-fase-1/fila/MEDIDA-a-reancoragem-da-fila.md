# MEDIDA — as `6` `ÂNCORA PERDIDA` da fila, reancoradas

*11/09/2026, noite. Fecha o item `2` da lista do `PROMPT-proximo-chat.md`.*

> ## ✅ **`43` de `43` scripts passam.** *Eram `35` de `41` com `6` mortos.*
> **Nenhuma âncora foi afrouxada pra passar** — *três eram troca de forma, duas viraram conferência
> nova, e uma precisou de um dono que tinha deixado de existir.*

---

## As `6`, uma a uma

| # | script | o que estava quebrado | o que entrou |
|---|---|---|---|
| `1` | `medir-a-dupla.py` | **a leitura `🟢 só nome` do RETORNO estava OTIMISTA.** *Trocar `Ronda`⟹`Ameaça` destravou a primeira âncora e o script morreu em mais SEIS, uma atrás da outra* | ver o §2 abaixo — **o caso caro** |
| `2` | `medir-o-encontro-misturado.py` | o mesmo `Ronda`/`Alcateia` do §4.3 · **e a tabela do §4.5 passou a sair com UMA CASA** (`91,5%`, `67,6%`), e a regex lia `(\d+)%` | as duas regex com `[\d,]+` e `num()`. **`4` de `4` linhas do §4.5 reproduzem** |
| `3` | `medir-quadrado-e-retangulo.py` | a mexida `29b` emendou a frase da `Linha` no `partC.js`, e a aspa que fechava a string deixou de vir logo depois do `1,5 m` | tirar a aspa do fim da regex |
| `4` | `medir-a-imunidade-a-condicao.py` | a prova dos *"nove golpes"* do §5 **morreu de propósito** na mexida `A.1` | **dois donos melhores, e um deles é NÚMERO:** as ações saem da COLUNA do `Desastre` na tabela do §4, e as rodadas da frase do §4.6. ⚠ **E as três peças passaram a ler a FONTE**, e não a cópia de `finalizado/regra/` |
| `5` | `medir-morte-e-imunidade.py` | o degrau morreu como moeda e o preço virou multiplicador do fator | lê o `1,43` da frase **e COBRA que ele bata com a tabela do §6.3 logo acima** — *dois donos do mesmo número, que é a lição nº 9* |
| `6` | `medir-a-peca-15.py` | a tabela da morte em definitivo foi de `5` linhas pra `4` — ela passou a AGRUPAR categorias de mesmo golpe | **o script parou de PREVER e passou a CONFERIR.** *O número de linhas deixou de ser âncora; o que ele cobra agora é que as expressões publicadas sejam as da escada viva, que o crítico publicado seja o do topo, e que os `4` veredictos reproduzam* |

---

## § 2 · O caso caro — o `medir-a-dupla.py` e a escada que deixou de existir

**Ele não mede a escada: ele mede a TRANSIÇÃO de uma pra outra.** *Para onde cada uma das seis vai, e o
que fazer com a `Dupla`.* **E a escada MORTA ele lia da peça 26 §4 — que a v0.221 reescreveu inteira.**

> ### ⟹ O dono do lado esquerdo da conta sumiu do projeto. Nenhum documento vivo publica
> ### `Ronda` `1p` `× 0,25` `1a` · `Dupla` `2p` `× 0,50` `1a` · `Alcateia` `4p` `× 1,00` `3a`.

**As duas saídas ruins, e por que nenhuma serve:**

| saída | por que não |
|---|---|
| digitar a escada morta dentro do script | ❌ **é número escrito à mão**, que é a regra `2` do projeto |
| aposentar o script | ❌ *ele carrega o `§10`, que confere o `DECIDIDO-as-seis-prontas.md` contra a escada viva — a banda, os pontos da `Kitsune` e o custo do encontro da `Kamaitachi`.* **Isso não está coberto em lugar nenhum** |

### A saída que entrou: uma cópia de MUSEU, com procedência de `git`

**`04-fase-1/museu/a-peca-26.v0.220.md`** — *a peça inteira, byte a byte, do commit `fc1cb79`, que é o
último ANTES do `900da9c` ("a peca 26 passa para a escada viva").* **Dá pra conferir:**

```
cd "/media/mizuki/HD Externo II/Claude/Claude 2"
git show fc1cb79:sistema/03-mecanica/26-bestiario.md
```

> **Não é número à mão: é REGISTRO, com endereço.** *A regra `2` fala de número derivado — o que uma
> fórmula produz tem de sair da fórmula.* **O que um documento dizia numa versão é um fato do
> histórico, e o `git` é o dono dele.**

**Só a escada morta sai do museu** — *o §4, o §4.1, o §4.4 e a frase "o capanga do manual não é uma
`Ronda`".* **A escada VIVA continua saindo dos donos de sempre:** o `RASCUNHO-5` Passo 1, a `TABELA.md`,
o `dados.js` e a peça 26 de hoje.

### E mais três âncoras dele caíram junto, todas do commit `C`

| âncora | o que aconteceu |
|---|---|
| o orçamento da `Kitsune` | o campo `caracteristicas` das `PRONTAS` **morreu** — o feitiço dela passou a ser COMPUTADO (`⌊golpe ÷ 4,5⌋d8`). *O `4,2` mudou de dono: agora sai do `DECIDIDO-as-seis-prontas.md` §2, o martelo que fixou ele* |
| a ficção da `Kamaitachi` | idem. *Passou a ler o traço `Par` **e** o `corpos_na_mesa`, que é número e o gerador imprime* |
| o número `SEIS` | o `dados.js` **parou de derivar** o seis ("a derivação antiga morreu com a escada"). *O §8 deixou de perguntar "ainda dá seis?" e passou a conferir o registro* |

---

## § 3 · O que não era âncora: as `3` que só precisavam de `cwd`

**`classificar-recarga-area.py`, `classificar-recarga-pf2e.py` e `dump-recarga.py`** abrem
`srd-2024.json` e `pf2e-recarga.json` por caminho relativo. **Elas rodam da RAIZ do `Bestiario/`, que é
onde os corpora moram** — não é defeito, é o `cwd`.

---

## § 4 · De quebra: o meio-ponto da `TABELA.md`, fechado

**Achado `1` do agente dos blocos.** *A `TABELA.md` publicava `1d4 + 2` na `Catástrofe` nv `2`–`4` e o
gerador dava `1d4 + 3`.* **A causa é o meio-ponto:** `Math.round` do JS sobe (`2,5` ⟹ `3`) e o `round`
do Python vai pro PAR (`2,5` ⟹ `2`).

**O dono do golpe é o `dado()` do `make.js`, e ele sobe.** *`fila/regerar-o-golpe-da-tabela.py` refaz a
coluna inteira — `116` células — e reescreveu as `3`.* **Sem `--escrever` ele só confere e morre se
divergir**, porque rodar a fila não pode mexer em dono.

> **O `gerar-tabelas.py` parou de acusar o meio-ponto**, e os dois PDFs do livro foram regerados.
> *Nenhum número impresso mudou: no nv `2`–`4` a `Catástrofe` sai `5` seco pelos dois caminhos, porque
> o fator `0,923` derruba ela abaixo do piso do dado.*

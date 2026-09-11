# MEDIDA — a peça 15 calibra a morte do shikigami contra o golpe da `Dupla`

*10/09/2026 (noite). **Achado respondendo "o que falta?" pela segunda vez no dia.***
**Conta rodada: `04-fase-1/fila/medir-a-peca-15.py`** — o 28º.

> ## ⟹ A régua de morte definitiva do shikigami tem `Dupla` embaixo dela. E a `Dupla` morreu hoje.

---

# § 0 · ⚠⚠ E PRIMEIRO: A MINHA VARREDURA DE HOJE ESTAVA INCOMPLETA

**Eu publiquei "`24` linhas" como se fosse o repositório.** *Eram as linhas dos DOIS arquivos que eu
escolhi olhar — `dados.js` e `make.js` —, e a escolha era minha.*

**A varredura de verdade anda os `391` arquivos:**

| arquivo-fonte | linhas | o que é |
|---|---|---|
| `sistema/03-mecanica/26-bestiario.md` | `49` | peça viva — já na `MEXIDAS` |
| `gerador-inimigo/dados.js` | `13` | item `30c` |
| `sistema/03-mecanica/conferir-bestiario.py` | `12` | validador — já na `MEXIDAS` |
| `gerador-inimigo/make.js` | `11` | item `30c` |
| ### `sistema/03-mecanica/15-invocacoes.md` | ### `6` | ### ⚠⚠ **PEÇA VIVA, FORA DE TODA LISTA** |
| `sistema/ESTADO-ATUAL.md` | `6` | ⚠ estado do repo |
| `sistema/03-mecanica/conferir-ficha.py` | `3` | validador — bloco `7` |
| `sistema/04-playtest/mesa-01-grupo-01.md` | `3` | ⚠ registro de mesa real |
| `gerador-inimigo/COMO-USAR.txt` | `1` | ⚠ **eu tinha pulado** |
| ### total | ### **`104`** em **`9`** arquivos | |

*E mais `90` em espelho e histórico, que **não são edição a mais**:* `logs/CHANGELOG.md` *(`35` —
histórico deve falar a morta)* e `finalizado/regra/` *(`55` — **espelho byte a byte** de outro repo
git, e a checagem `7` do `conferir-repositorio.py` é a dona dessa comparação)*.

> ### ⚠ "Linha que cita" NÃO é "mexida".
> **A `MEXIDAS-no-repositorio.md` conta mudança SEMÂNTICA** — *uma tabela inteira trocada é uma mexida
> com dez linhas dentro.* **Este número é a SUPERFÍCIE, e serve pra achar arquivo esquecido, não pra
> estimar trabalho.**

> ### ⟹ E ele achou `4` arquivos que não estavam em lista nenhuma. Um deles é peça de REGRA.

---

# § 1 · O QUE A PEÇA 15 FAZ, e por que ela depende da peça 26

**A peça 15 §"A morte em definitivo" publica a régua do shikigami:**

> *"**A régua da morte é a vida máxima daquele corpo.** Ela morre de vez se **um único golpe** causar
> a régua inteira, ou se o excedente passar de metade da régua."*

**E ela NÃO escolheu esse teto — ela MEDIU contra a tabela de golpe da peça 26**, pelo MÁXIMO da
rolagem, não pela média. *A própria peça escreve por quê:*

> *"o gatilho fala em **um golpe**, e um golpe é uma rolagem […] Medir pela média esconde exatamente
> a cauda que decide isto."*

**⟹ A peça 15 é CONSUMIDORA da escada de categoria.** *Ela não tem escada própria; ela lê a da peça 26.*

---

# § 2 · A TABELA DELA, E O TETO É A `Dupla`

*Nível 30. **Os `5` máximos publicados batem com as expressões** — a tabela é consistente por dentro.*

| a linha, como está publicada | expressão | máximo | `Coro` (`154`) | forte (`185`) |
|---|---|---|---|---|
| `Ronda` | `6d8 + 28` | `76` | cai | cai |
| `Calamidade` | `6d10 + 33` | `93` | cai | cai |
| ⚠ `Alcateia`, *que é também o capanga* | `8d8 + 37` | `101` | cai | cai |
| **`Dupla`**, *o maior golpe da tabela* | `8d12 + 57` | ### **`153`** | cai | cai |
| **crítico de `Dupla`** | `16d12 + 57` | `249` | ### **destrói** | ### **destrói** |

> ### A ÚNICA linha marcada "destrói" na peça inteira é o crítico da `Dupla`.
> *E a `Dupla` foi morta de propósito — `DECIDIDO-as-seis-prontas.md`, hoje.*

## E o teto da escada VIVA, no mesmo nível

| categoria | expressão | máximo |
|---|---|---|
| **`Desastre`** e **`Calamidade`** | `8d8 + 37` | ### **`101`** |
| `Catástrofe` | `6d10 + 33` | `93` |
| `Capanga` e `Ameaça` | `6d8 + 28` | `76` |

> ### ⟹ O teto caiu de `153` para `101` — **`1,51×` menor**.

---

# § 3 · ⚠⚠ A CONCLUSÃO DA PEÇA QUEBRA NA METADE

**A peça 15 conclui, palavra por palavra:**

> *"**Nenhum golpe comum destrói em definitivo**, e a razão vale em todo nível. **Precisa do crítico
> da maior categoria da tabela** — ou de o corpo já estar quase caindo, que é o outro gatilho."*

| a metade | na escada viva |
|---|---|
| **`1` · "nenhum golpe COMUM destrói"** | ### ✅ **continua valendo, e com MAIS folga** — *o maior comum é `101` contra `154` e `185`* |
| **`2` · "precisa do crítico da maior categoria"** | ⚠⚠ **quebra** |

**O crítico do topo vivo é `16d8 + 37` = `165`:**

| contra | `165` alcança? |
|---|---|
| o `Coro` de Con `1` (`154`) | ✅ **destrói** |
| **o corpo forte (`185`)** | ### ❌ **NÃO destrói** |

> ## ⟹ Na escada viva, NADA no jogo destrói um corpo forte com um golpe único.
> **Nem o crítico da maior categoria.** *A peça publica que o crítico da `Dupla` destrói **os dois**, e
> essa é a única linha "destrói" que ela tem.*
>
> ⚠ **O outro gatilho — o excedente, com o corpo já machucado — continua existindo.** *Mas ele também
> se mexeu: `§4`.*

---

# § 4 · A TABELA DO CORPO MACHUCADO — `2` de `4` linhas mudam

*Pro `Coro` de Con `1` no nv30, vida `154`.*

| o corpo | o golpe precisa de | **publicado** *(com a `Dupla`)* | **medido** *(topo vivo)* |
|---|---|---|---|
| cheio | `232` | não | não |
| na metade | `155` | não | não |
| **em um quarto** | `116` | **`26%` das rolagens** | ### ❌ **não** |
| **a um ponto de cair** | `79` | **sempre** | ### ⚠ **`20%` das rolagens** |

> ### ⚡ E a GUARDA fechou: as `4` linhas publicadas reproduzem EXATO com o `8d12 + 57`.
> **`26%` recomputa `26%`. `sempre` recomputa `sempre`.** *⟹ a tabela **foi** calculada contra a
> `Dupla`. Não é coincidência de leitura, e não é interpretação minha.*

**A linha que mais dói é a última.** *"A um ponto de cair — **sempre**" era a promessa de que o gatilho
do excedente sempre pega um corpo quase morto.* **Na escada viva ele pega em `1` de `5` rolagens.**

> ### ⟹ Os dois gatilhos da régua encolheram juntos. O de golpe único perdeu o corpo forte; o do
> ### excedente deixou de ser "sempre" e virou `20%`.

---

# § 5 · ⚠ E A MESMA CONFUSÃO DE HOJE, NUMA PEÇA DE REGRA

**A peça 15 imprime, na própria tabela:** *"`Alcateia`, **que é também o capanga**"*.

**E a peça 26 §4.3 diz o contrário com todas as letras:** *"É por isso que o capanga do manual **não é**
uma `Ronda`."*

*A `Alcateia` é fator `1,00`; o capanga do manual é `chefe ÷ 4` de vida com `chefe ÷ 3` de dano.*

> ### ⟹ É a MESMA troca que a `MEDIDA-o-remapeamento-das-seis.md` corrigiu no `ESTADO` hoje.
> **Só que aqui ela está publicada numa peça de regra, e não num arquivo de estado.** *É a oitava vez
> que "a decisão andou e a tabela ficou" aparece — e a segunda hoje.*

---

# ⟹ § 6 · O QUE ISSO É, E O QUE ELE NÃO É

| | |
|---|---|
| ❌ **não é** | erro de conta da peça 15. *Ela mediu certo, contra a escada que existia* |
| ❌ **não é** | coisa que a mesa sente hoje. *`shikigami` é `tipo` de inimigo, e nenhuma das seis prontas é um* |
| ### ✅ **é** | ### **uma peça de REGRA VIVA cujo número de calibração deixou de existir** |

> ### ⚠ E ele NÃO é do Bestiário resolver.
> **A peça 15 é do repositório, e outra conta escreve lá.** *Este projeto mede e entrega a conta.*

## O que a peça 15 precisa, quando o commit da escada entrar

| # | onde | o quê |
|---|---|---|
| **`1`** | a tabela da morte | trocar as `5` linhas pela escada viva. ⚠ **e a linha "destrói" muda de conteúdo, não só de nome** |
| **`2`** | a frase de conclusão | *"precisa do crítico da maior categoria"* ⟹ **ela só destrói o `Coro`; o corpo forte não cai por golpe único nenhum** |
| **`3`** | a tabela do corpo machucado | `2` de `4` linhas — `em um quarto` de `26%` pra **não**, `a um ponto de cair` de `sempre` pra **`20%`** |
| **`4`** | a tabela da Constituição | ⚠ os `7%` · `70%` · `4%` · `68%` saíram todos da distribuição da `Dupla`. **Não recomputei: falta a fórmula do corpo por Con, que é do §3.7 da própria peça** |
| **`5`** | a frase da tabela | *"`Alcateia`, que é também o capanga"* — **as duas coisas são diferentes, e a peça 26 §4.3 já diz isso** |

> ### ⚠ E tem uma pergunta de DESENHO embaixo do `2`, e ela é dele:
> **A régua ficou mais frouxa sem ninguém decidir isso.** *Antes, um crítico do topo destruía qualquer
> corpo; agora nenhum golpe destrói o corpo forte.* ⟹ **ou a peça 15 registra que a morte definitiva
> virou coisa quase só do gatilho de excedente, ou o corpo forte encolhe.**
>
> ***Não é pendência do Bestiário.*** *Fica escrito aqui porque a conta está aqui.*

---

## De onde saiu

**`medir-a-peca-15.py`** *(este projeto, o 28º)* · **`sistema/03-mecanica/15-invocacoes.md`**
*§"A morte em definitivo"* · **`TABELA.md`** *(a escada viva, nv30)* ·
**`DECIDIDO-as-seis-prontas.md`** *(a `Dupla` saiu hoje)* · **peça 26 §4.3 e §4.4**

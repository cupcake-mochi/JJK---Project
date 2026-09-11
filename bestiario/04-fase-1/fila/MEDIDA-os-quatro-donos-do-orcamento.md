# MEDIDA — a tabela do orçamento tinha `4` donos, e um deles estava velho

*11/09/2026, noite. Saiu da pergunta **"o que falta?"** — a terceira vez que ela acha coisa.*

> ## 🔴 O ACHADO
> **A rota `B` moveu `9` células do orçamento de uma ação. Três lugares foram corrigidos; o quarto não.**
> *E o quarto é o do Bestiário — o `refazer-pontos-por-acao.py` e o laudo dele.*

---

## § 1 · Os quatro donos

| # | onde | rota | estava |
|---|---|---|---|
| `1` | `Claude 2` · peça 26 §6.5, a tabela publicada | `B` | ✅ atual *(patch da `v0.222`)* |
| `2` | `Claude 2` · `conferir-bestiario.py`, a checagem `9.1` | `B` | ✅ atual |
| `3` | `Bestiario` · livro, cap. `6` | `B` | ⚠ **atual, e digitado à mão** |
| `4` | `Bestiario` · `fila/refazer-pontos-por-acao.py` + `A-TABELA-pontos-por-acao.md` | ### `A` | 🔴 **VELHO** |

**A diferença entre as rotas é a ORDEM:**

| rota | a conta |
|---|---|
| `A` | média do golpe **cru** `× 0,923`, e divide por `4,5` |
| ### `B` *(a validada)* | o fator entra no dano de **RODADA**, o dado se escolhe depois, e o que se divide por `4,5` é a média do golpe **IMPRESSO** |

*Exemplo, no `Desastre` nv30:* **rota `A`** dá `219 × 0,923 = 202,1` ⟹ `67,4` ⟹ `15,0` pontos.
**Rota `B`** dá `⌈219 × 0,923⌉ = 202`, `202 ÷ 3 = 67,3` ⟹ dado `6d10 + 34`, média `67,0` ⟹ **`14,9`**.

> ### ⚠ E ele passava na fila. **Passava porque não conferia nada** — ele recomputava por conta
> ### própria e comparava com a escada MORTA, escrita à mão dentro do print.

---

## § 2 · O que entrou

| | |
|---|---|
| `refazer-pontos-por-acao.py` | **passou a fazer a rota `B`**, com o `dado()` portado do `make.js` *(constantes lidas de lá, e o meio-ponto PRA CIMA)* |
| idem | **o `0,923` deixou de ser digitado** — sai do §6.5 da peça 26 |
| idem | **entrou a CONFERÊNCIA:** as `35` células contra a tabela que o §6.5 publica, e ele **morre** se divergirem |
| idem | a comparação com a escada morta *(`Ronda 12,2 · Dupla 24,2 · Alcateia 16,2`)*, que era texto fixo, **saiu** |
| `A-TABELA-pontos-por-acao.md` | refeito na rota `B`, com a caixa dizendo o que mudou e por quê |

> **`✓ as 35 celulas batem com a tabela publicada no §6.5.`**
> *Enquanto este script passar, o Bestiário e a peça 26 contam a mesma coisa.*

---

## § 3 · E o dono `3` deixou de ser digitado à mão

**A `Orçamento de uma ação, por categoria` do capítulo `6` era ESTÁTICA** — *`35` números fora de
qualquer região gerada, mais a `Condição na maior ação`, que depende do maior deles.*

**Virou região:** `<!-- ORCAMENTO -->`, escrita pelo `gerar-tabelas.py` a partir da mesma conta do
golpe impresso. **As âncoras novas:**

| número | dono |
|---|---|
| o `4,5` do ponto de feitiço | peça 26 §6.5, a frase da regra |
| o piso de `3` pontos | peça 26 §6.5, *"o menor feitiço do manual é a `Classe 1`"* |
| `Leve 4` · `Média 7` · `Pesada 11` | peça 19 §3, a coluna `pontos` da tabela das treze |
| a maior ação | **o maior da própria tabela gerada** — ninguém escreve `14,9` |

> ### ⟹ A região gerada saiu IDÊNTICA ao que estava digitado.
> *Isso é a prova de que a conta e o texto concordavam hoje.* **O que muda é que da próxima vez
> ninguém precisa acertar na mão.**

---

## § 4 · ✅ RESOLVIDO na mesma noite — os corpora tinham TRÊS casas, e não duas

**A primeira contagem estava curta.** *Os seis corpora de campo moravam em três lugares:* a raiz do
`Bestiario/`, a `04-fase-1/fila/` e a `fila/dados-recarga-area/`. **`md5` idêntico nos três.**
*E três `classificar-*.py` estavam duplicados junto.*

### A causa estava escrita, e era uma linha de receita

O `dados-recarga-area/COMO-RODAR.md` mandava:

```
cp ../classificar-*.py ../somar-*.py .
```

**Copie os scripts pra cá e rode aqui dentro.** *E os scripts abriam por nome nu — `open('srd-2024.json')` —,
então liam e ESCREVIAM no diretório de quem chamava.* **Cada lugar de onde alguém rodou virou uma casa.**

### O conserto

| | |
|---|---|
| `6` scripts | passaram a resolver o caminho contra o **próprio arquivo** (`os.path.dirname(__file__)`), leitura e escrita. *Os quatro `classificar-*`/`dump` e os dois `puxar-*`, que eram os que criavam cópia* |
| as cópias | apagadas da raiz e da `dados-recarga-area/` — **só depois de conferir `md5` um a um** |
| `3` scripts duplicados | apagados. *O `classificar-va-drawsteel.py` de lá era a versão de `10/09 10:29`, com o glob relativo que devolvia ZERO; a boa, de `19:49`, ficou na `fila/`* |
| `COMO-RODAR.md` | refeito — a linha do `cp` saiu, e a receita agora roda da `fila/` |

> ### ⟹ A prova: a fila roda **`43` de `43` de um `cwd` NEUTRO**, fora do projeto.
> *Antes, `3` scripts só funcionavam se você estivesse na raiz.* **Agora não existe mais "de onde
> você rodou".**

**`47 MB` ⟹ `36 MB`.** *O `ds.tar.gz` fica: ele é o recibo do corpus do Draw Steel, e prova que o
`data-md-main/` não foi editado à mão.*

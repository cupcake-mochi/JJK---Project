# Prompt pra colar no próximo chat

*11/09/2026, fim da tarde. Copie daqui pra baixo.*

---

Estamos no Bestiário do meu RPG (Projeto - M, o de Jujutsu Kaisen). O trabalho mora em
`/media/mizuki/HD Externo II/Claude/Claude 2/bestiario/`, **DENTRO do repositório do sistema**, que é
`/media/mizuki/HD Externo II/Claude/Claude 2/`.

> ⚠ **Mudou em 11/09/2026.** *Até essa noite o Bestiário morava em `Claude/Bestiario/`, fora de
> versionamento.* **Ele entrou no repositório do sistema como pasta à parte, por decisão dele.**
> *Os `PROMPT-*.SUPERADO-*.md` ainda falam do caminho velho, e ficam assim: são registro do que
> valia na data.*

**A entrega do Bestiário já foi executada no `Claude 2`.** A `v0.221` está fechada em `8` commits no ramo
`bestiario-escada-viva`, com a árvore limpa, todos os validadores verdes e **nenhum push** — ele foi autorizado e travou na conta do `gh`.
**E a passada de texto do livro fechou, com os PDFs regerados.**

## Leia estes, nesta ordem, e você está a par de tudo

1. **`RETORNO-do-claude-2.md`** — o estado. Cada commit, o que falta, o que pede meu ok, e a lista das
   `6` `ÂNCORA PERDIDA` da fila com a leitura de cada uma.
2. **`08-livro/PASSADA-3-texto.md`** — a caixa do topo: a passada fechou, e o que ficou marcado pra conferir.
3. **`08-livro/PASSADA-3-blocos.md`** — só o fim: os PEDIDOS pros capítulos `50`, `60` e `70`.

Não me peça pra recontextualizar.

## O que falta, na ordem

| # | o quê | quem decide |
|---|---|---|
| ~~`1`~~ | ~~o push dos dois~~ ✅ **FEITO 11/09, com a conta `cupcake-mochi` ativa.** *`JJK---Project` no `d138193` (ramo `bestiario-escada-viva`) e `JJK---PDF---RPG` no `38e2765 recorte da v0.222`* |
| ~~`2`~~ | ~~reancorar as `6` da fila~~ ✅ **FEITO 11/09 — `43` de `43` passam.** *Laudo em `04-fase-1/fila/MEDIDA-a-reancoragem-da-fila.md`* |
| ~~`3`~~ | ~~a `TABELA.md` com meio-ponto pra cima~~ ✅ **FEITO 11/09.** *`fila/regerar-o-golpe-da-tabela.py` — `3` de `116` células. O `gerar-tabelas.py` parou de acusar* |
| ~~`4`~~ | ~~dois pedidos de desenho do capítulo 5~~ ✅ **FECHADO 11/09, e executado** |
| ~~`5`~~ | ~~a pergunta de conta do capítulo 6~~ ✅ **FECHADA 11/09 — rota B, e executada** |
| ~~`6`~~ | ~~conferir as duas frases contra a obra~~ ✅ **FECHADO 11/09 — uma delas era erro de fato** |
| ~~`7`~~ | ~~o commit da `v0.222`~~ ✅ **FEITO por ele em 11/09** — `d138193`, árvore limpa |

> ## ⟹ ✅ A LISTA INTEIRA FECHOU em 11/09 — e a pergunta **"o que falta?"** achou mais uma.
> ### 🔴 A tabela do orçamento tinha `4` donos, e o do Bestiário estava na rota `A`.
> *`fila/MEDIDA-os-quatro-donos-do-orcamento.md`.* **O `refazer-pontos-por-acao.py` passou a
> fazer a rota `B` e a CONFERIR as `35` células contra o §6.5 — ele morre se divergirem.**
> **E a tabela do capítulo `6`, que era `35` números à mão, virou a região `<!-- ORCAMENTO -->`.**
> *A região saiu idêntica ao que estava digitado.*
>
> ### ✅ E os corpora foram resolvidos na mesma noite — eram **TRÊS** casas, e não duas.
> *A causa era uma linha de receita (`cp ../classificar-*.py .`) somada a `open()` por nome nu.*
> **`6` scripts passaram a resolver contra o próprio arquivo, as cópias foram apagadas depois de
> conferir `md5`, e a fila roda `43` de `43` de um `cwd` NEUTRO.** *`47 MB` ⟹ `36 MB`.*

> ## ⟹ E o resto: **nada está aberto.**
> **`Claude 2` limpo na `v0.222`, `29` validadores verdes, os dois repositórios no ar.**
> **Bestiário: fila `43` de `43`, `conferir-voz.py` em `0`, os dois PDFs regerados.**
>
> ⚠ **O recorte da `v0.222` precisou de commit próprio no `finalizado/`** — o `subir.sh`
> sincroniza a pasta mas NÃO commita ela; a linha `151` dele imprime o comando. *A `v0.221`
> já estava no ar; o que faltava era só a `v0.222`.*

> ## 🆕 O que a sessão da tarde de 11/09 fez, depois que este prompt foi escrito
>
> | | |
> |---|---|
> | **o golpe saiu do cabeçalho** | ele mora no ataque, em `Ações`, com o alcance junto. **`Ações Múltiplas` conta na linha de `6`.** *E o capítulo `5` passou a dizer como se nomeia o ataque — medido em `7` sistemas, e nenhum usa "Ataque de" no nome* |
> | **rota `B` no orçamento** | `9` células do §6.5 andaram `0,1` (e não `3`). **A maior ação do sistema: `15,0` → `14,9` pontos.** *Patch em `ferramentas-claude-2/rota-b-26.py`, que reabre os donos e reescreve os três lugares* |
> | ❌ **erro de fato no capítulo `3`** | *a Maki NÃO matou o Naoya de punho — foi a MÃE dela, com faca de cozinha, cap. `152`.* **Corrigido no livro e no catálogo.** Laudo: `07-catalogo/PESQUISA-03b-o-erro-da-morte-do-naoya.md` |
> | **a `v0.222` está pronta pra commitar** | `29` validadores verdes · `mensagem-de-commit.txt` na raiz do `Claude 2` · **nada commitado, nada empurrado** |
>
> *Os dois PDFs do livro e o `bloco-de-inimigo` foram regerados.*

*Feito em 11/09:* a passada de texto do livro fechou inline — voz em `0`, nenhum número de regra mudou — e os
dois PDFs foram regerados. **Os dois avisos do build já existiam em 10/09:** sem capa de arte, e DejaVu no lugar
do IBM Plex Mono em negrito e itálico dentro de crase, que é a mesma falta de face do Manual.

## ⚠ As regras de trabalho — não negociáveis

**1 — Agente: PERGUNTAR É OBRIGATÓRIO**, mesmo pra `1` só. Diga quantos, o que cada um faz e o custo.
Teto de `2` a `3` por vez, cada um salvando o próprio arquivo antes de retornar. *Se o ultracode mandar
abrir workflow com leque, esta regra vale mais — e me diga isso em uma linha.*
**Régua de custo, medida:** `~R$ 0,13` por `1k` de contexto final de subagente.

| referência medida | contexto final | custo |
|---|---|---|
| a passada de texto anterior — `1` agente, `5` capítulos (e registrou só `3`) | `~277k` | `~R$ 36` |
| os seis blocos — `2` rodadas | `~331k` + `~252k` | `~R$ 76` |

*Use a régua acima pra estimar qualquer trabalho de agente que aparecer.*

**2 — Número vem de conta rodada.** Script que lê cada âncora do documento DONO e morre se ela mudar.
Nunca número digitado à mão.

**3 — Salve conforme for.** Decisão fechada vira arquivo na hora, com o porquê. Conta Pro: a sessão
estoura no meio, e estourou duas vezes em 11/09.

**4 — No `Claude 2`, nada de commit com validador vermelho, e nada de push sem meu ok.** Os `7` `.zip`
em `sistema/skills/` são meus e não entram em commit.

## As ferramentas que já existem

| onde | o quê |
|---|---|
| `ferramentas-claude-2/valida.sh` | roda a suíte inteira do `Claude 2` e mostra só resumo e falha |
| `ferramentas-claude-2/sincroniza-entrega.sh` | o passo 0 do `subir.sh`: sincroniza `finalizado/`, sem commit. **Rode antes do `valida.sh`** |
| `ferramentas-claude-2/arnes-c.py` · `arnes26.py` | arnês de perturbação em cópia isolada — o molde pra checagem nova |
| `ferramentas-claude-2/brancos-diff.py` | itemiza a lista branca da checagem `7.2` entre duas árvores da entrega |
| `08-livro/build/conferir-voz.py` · `guard_numeros.py` | voz dos títulos e do texto · quais números mudaram contra `build/.antes/` |
| `08-livro/build/gerar-*.py` · `build.py` | as regiões geradas dos capítulos `6`, `8` e o exemplo · o PDF |

**Rodar a fila:** `fila/*.py` e `sobrecarga/*.py` de `04-fase-1/`, **menos os `puxar-*`** (baixam `6 MB`).

## Direcionamento das skills

- **`workflow-authoring`** — o ultracode carrega ela e pede workflow. **A regra `1` vale mais.**
- **As skills do próprio projeto moram em `Claude 2/sistema/skills/<nome>/SKILL.md`.** *Se aparecerem na
  lista de skills da sessão, use pelo nome; se não, leia o `SKILL.md` antes da tarefa:*
  - **`rpg-da-guilda`** — antes de mexer no `Claude 2`: ordem de leitura, validadores, arnês, fechar versão
  - **`redacao-acessivel-rpg`** — na passada de texto do livro, junto da `sistema/05-material/livro/REGRA-DE-VOZ.md`
    e da `METODO-passada-de-texto.md` do `Claude 2`
  - **`balanceamento-simulacao`** — pra qualquer número novo, como o meio-ponto da `TABELA.md`
  - **`pesquisa-antes-de-propor`** — antes de propor regra, nome ou afirmação sobre a obra
  - **`design-mecanicas-rpg`** — se a passada abrir decisão de mecânica (aí é pergunta pra mim)
  - **`playtesting-rpg`** — quando o playtest das fichas de nível 7 de `06-playtest/` voltar
- **`docx` e `pdf`: NÃO edite `.docx` nem `.pdf` à mão.** Todo artefato é gerado — o `make.js` do
  `gerador-inimigo`, o `manual/gerador/` e o `build.py` do livro. Mexa na fonte e regenere.

## Como eu gosto de trabalhar

Português informal, frase curta, uma ideia por parágrafo. Sem gíria de RPG na conversa.
Se der pra medir, meça e me traga a resposta em vez da pergunta. Só chega em mim o que é escolha de
sabor — e o que gasta crédito.

# Bestiário — recomeço

**Esta pasta é `bestiario/`, DENTRO do repositório `Claude 2`.** Ela existe porque o Bestiário da peça 26 vai ser refeito em vez de remendado.

> ⚠ **Até 11/09/2026 ela ficava fora do repositório, e nada daqui entrava em commit.** *Nessa noite ela entrou, por decisão dele, como pasta à parte — o trabalho de três dias passou a ter histórico.* **O que continua valendo: este projeto só LÊ o `sistema/`; quem escreve lá é o `subir.sh` do repositório.**

*Aberta em 08/09/2026. Fase 0 fechada no mesmo dia. Fase 1 em andamento.*

---

# ▶ COMO RETOMAR

> ### ⚡ 11/09/2026: a entrega foi EXECUTADA no `Claude 2` (`v0.221`, sem push).
> **Leia `RETORNO-do-claude-2.md` e siga o `PROMPT-proximo-chat.md`.** *O resto desta seção é de antes.*

> ### ⚡ Atalho: se você só vai ler UM arquivo, leia `04-fase-1/ESTADO-onde-paramos.md`.
> Ele tem onde a Fase 1 parou em 09/09, o que está provado, o que está só recomendado, e a fila.

**Leia nesta ordem e você está a par de tudo:**

0. **`04-fase-1/ESTADO-onde-paramos.md`** — **o estado atual.** Comece por aqui.
1. **`00-fase-0/mesa-nd20.md`** — a mesa que fundou o projeto. É o porquê de tudo.
2. **`00-fase-0/decisoes.md`** — as onze decisões da Fase 0.
3. **`03-bloco/o-principio-da-causa.md`** — o princípio que governa o bestiário inteiro.
4. **`03-bloco/RASCUNHO-2-o-bloco-em-branco.md`** — o formato do bloco.
5. **`04-fase-1/decisoes-fase-1.md`** — onde a Fase 1 parou, com a fila do que vem.
6. **`04-fase-1/TABELA.md`** — os números prontos.

**A pergunta do PE está FECHADA, e ela virou o contrário do que a gente estava calculando.** *Em 09/09 o Mizuki parou o preço e concluiu que o inimigo não deveria ter recurso finito — e o campo deu razão: `8` de `9` sistemas medidos limitam o inimigo por rótulo de frequência, não por poço.* **A decisão é a saída `A`, só rótulo** (`decisoes-fase-1.md` §8).

**A `Sobrecarga` e o `papel` do inimigo fecharam em 09–10/09.** *O estado completo, com a fila nova, está em `04-fase-1/ESTADO-onde-paramos.md`.*

> ⚠⚠ **PERGUNTE ANTES DE PUXAR AGENTE. É obrigatório, e vale pra `1` agente só.**
> *Não é pra impedir — é pro Mizuki escolher o momento do gasto; ele quase sempre libera.*
> **A pesquisa de campo de 10/09 foi ótima e custou R$ 100.** *Detalhe em `PROMPT-proximo-chat.md`.*
>
> **E se liberar: `2` a `3` por vez, nunca mais, cada um salvando antes de retornar.**

---

## Por que este projeto existe

O `Bestiário` fechou como peça 26 na v0.198 do repositório. Ele tem validador, quarenta e duas perturbações e os números reproduzem. **Mas o Mizuki não conseguia usar.**

E na véspera de abrir esta pasta, ele mestrou uma mesa de ND 20 **sem ficha de inimigo**, improvisando os dados, usando só a linha de vida do sistema. Rodou bem.

> **Essa mesa é a primeira evidência de jogo do projeto** — a pasta `04-playtest/` do repositório está vazia desde a v0.1. **E ela validou duas coisas:** a CD do sistema funciona, e a linha de dano do grupo prevê a duração da luta com precisão (`1100 ÷ 220 = 5,0` rodadas, ele observou 5 a 6).

## O que está decidido

### O que o Bestiário é
**Duas coisas — o catálogo e a máquina — e as duas se encontram no BLOCO.** O catálogo é uma pilha de blocos preenchidos; a máquina é como preencher um em branco.

**Formato:** stat block no molde do D&D. Uma página de duas colunas, no máximo duas.

### O princípio que governa tudo
> **Nenhum número do bloco se move sozinho. Todo desvio da tabela tem uma causa escrita na ficção.**

*Ele substitui o orçamento do bestiário velho, e passa no filtro de dois mestres sem precisar de tabela.*

### O cabeçalho
`‹ tamanho › ‹ tipo ›, ‹ grau › · ‹ categoria › · nível ‹ N ›`

- **tamanho:** `Minúsculo` · `Pequeno` · `Médio` · `Grande` · `Imenso` · `Colossal` — *ainda não se sabe se carrega regra*
- **tipo:** `maldição` · `feiticeiro` · `restringido` · `civil` · `sem técnica`
- **grau:** rótulo de ficção, não entra em conta
- **categoria:** os cinco degraus abaixo

### A escada
*O nome diz quão ruim é; a tabela diz quantas pessoas precisa. O leitor nunca converte.*

| categoria | quem ela pede | vida | dano | ações | corpos |
|---|---|---|---|---|---|
| `Capanga` | — | `dano do grupo ÷ 4` | `0,25` | `1` | `8`, em pool |
| `Ameaça` | `1` | `0,25` | `0,25` | `1` | `1` |
| `Desastre` | `4` — a mesa padrão | `1,00` | `1,00` | `3` | `1` |
| `Catástrofe` | `6` — a mesa cheia | `1,50` | `1,50` | `5` | `1` |
| `Calamidade` | **mais que `6`** | `2,00` | `2,00` | `6` | `1` |

### O resto
| item | decisão |
|---|---|
| **recurso do inimigo** | **ele NÃO conta PE.** O limite é rótulo de frequência: `à vontade` · `1×/rodada` · `1×/luta` · `Recarga (5-6)`. *`8` de `9` sistemas medidos fazem assim* |
| **`Intervenção`** | a ação fora do turno. `3` por luta, cada uma uma vez, no máximo uma por rodada. Não absorve a Reação. **É o mecanismo que faz o papel do poço** |
| **o golpe do inimigo** | é a **técnica** dele, narrada como tal, sem custo — o `Classe 0` do inimigo. *Para `civil`, `sem técnica` e `restringido` o mesmo número é um soco, uma faca ou uma ferramenta* |
| **Integridade do inimigo** | **metade da vida** |
| **Iniciativa** | é a Destreza dele — `Iniciativa = d20 + Destreza` |
| **traços** | sem orçamento, com teto de quantidade. Não podem ser buff disfarçado |
| **resistências** | cortam pela metade. `1–2` tipos é de graça; um grupo inteiro custa; **imunidade a grupo só com porta de saída** |
| **papel** | ✅ **SEIS papéis, no cabeçalho, e ele REDISTRIBUI o orçamento — nunca adiciona.** `Brutamontes` · `Artilheiro` · `Emboscador` · `Controlador` · `Guardião` · `Apoio`. *O precedente é o 4e, não o Draw Steel.* Ver `04-fase-1/papel/` |
| **fase de chefe** | fora do escopo. Vida partida, ferramenta de mestre, fim do livro |
| **catálogo** | pirâmide — pesado embaixo, fino em cima —, escrito em ondas |
| **onde mora** | híbrido: a máquina vira peça no repositório, o catálogo vira livro gerado |

**O que morreu junto:** `Ronda`, `Dupla`, `Alcateia`; o câmbio de "um chefe vale quatro capangas"; e a sub-categoria.

## A fila

> **⚠ Três linhas desta tabela estavam marcadas como abertas depois de terem fechado, e a v0.223 do `Claude 2` corrigiu as três.** *Quando esta tabela discordar do `04-fase-1/ESTADO-onde-paramos.md` ou do `PROMPT-proximo-chat.md`, os dois vencem: eles são atualizados a cada sessão e esta lista não.*

| # | item | estado |
|---|---|---|
| ~~1~~ | **a `Sobrecarga`** | ✅ **FECHADA em 09/09.** *"ele não usa Reação, e o feitiço dele sai com a CD `2` menor"*, degrau `Leve`. Ver `04-fase-1/sobrecarga/` |
| ~~2~~ | **o `papel` do inimigo** | ✅ **FECHADO em 10/09.** Seis papéis no cabeçalho, tabela de câmbio pronta, os seis montam em `1,000`. Ver `04-fase-1/papel/` |
| ~~3~~ | **a `Intervenção`: sai da cota ou é ação extra?** | ✅ **FECHADA, e as duas respostas valem.** *Ela é ação extra por cima das do §4.2, e se paga no dano: quem carrega `Intervenção` tem o fator multiplicado por `0,923`.* **Publicada na peça 26 §6.5, na v0.221** |
| ~~4~~ | **o piso da banda do `o golpe`** | ✅ **FECHADA em 10/09: a banda virou `21%`–`28%`.** *O piso `20%` era do corte de dano do `Controlador`, que a forma `B` tirou, e o teto `32%` era o `Capanga` com o fator morto.* Ver `04-fase-1/fila/DECIDIDO-o-capanga.md` §1, que é a âncora |
| ~~5~~ | **tamanho carrega regra?** | ✅ **FECHADA: saída `F`, o tamanho não cobra.** *Ele dá alcance e um degrau de vizinho, e os `≈ 18%` que isso põe fora da conta estão declarados na peça 26 §3.3* |
| **1** | **as 4 linhas restantes da ficha** | medidas contra 4 sistemas. Duas já aplicadas no `RASCUNHO-3` |
| **2** | **o teto de traços** | **tem número agora**: `6` entradas nomeadas, `8` no chefe. Mediana `4` do D&D 2024, média `5,4` dos `Solo` do Daggerheart |
| **3** | **o catálogo** | primeira onda, quando o bloco estiver fechado. *Os quatro primeiros capítulos estão em `07-catalogo/`* |

## Onde está o quê

| arquivo | o que tem |
|---|---|
| `00-fase-0/mesa-nd20.md` | a mesa de ND 20, e o que ela provou |
| `00-fase-0/decisoes.md` | as onze decisões da Fase 0, com o porquê |
| `00-fase-0/o-que-descartamos.md` | o diagnóstico medido da peça 26 |
| `03-bloco/o-principio-da-causa.md` | **o princípio que governa o bestiário** |
| `03-bloco/RASCUNHO-4-o-bloco-em-branco.md` | **o bloco em branco atual** (o `RASCUNHO-2` fica pra comparação) |
| `03-bloco/RASCUNHO-1-o-bloco.md` | o bloco preenchido com o Sukuna da mesa |
| `03-bloco/a-intervencao.md` | a ação fora do turno |
| `03-bloco/a-escala-do-inimigo.md` | por que o inimigo NÃO ganha atributo inflado |
| `03-bloco/o-esqueleto-e-o-problema.md` | a virada: os números estavam bons |
| `04-fase-1/TABELA.md` | **os números: 5 categorias, nível 2 a 30** |
| `04-fase-1/decisoes-fase-1.md` | as decisões da Fase 1 e a fila — o §9 é a `Sobrecarga` |
| `04-fase-1/sobrecarga/` | **a `Sobrecarga` fechada** — a medida, as 3 fontes externas, o script e as mexidas que o repositório pede |
| `04-fase-1/papel/` | **o `papel` fechado** — a tabela dos seis, os dois câmbios construídos, e a fonte do 4e |
| `04-fase-1/a-escada-com-numero.md` | a escada, e por que cada fator é aquele |
| `04-fase-1/o-capanga-contra-os-outros-sistemas.md` | o corpo pequeno nos cinco sistemas |
| `01-pesquisa/` | D&D 2014, D&D 2024 e Draw Steel, extraídos dos livros |
| `02-referencia/` | medidas do bestiário antigo — referência, não base |

## Duas coisas importantes

**"Descartar" significou o DESENHO, não as medições.** Os números que continuam verdadeiros ficam em `02-referencia/` e `01-pesquisa/`.

**Nada foi apagado no repositório.** A peça 26, o `conferir-bestiario.py`, o `bloco-de-inimigo.docx` e o `gerador-inimigo/` continuam lá, intactos.

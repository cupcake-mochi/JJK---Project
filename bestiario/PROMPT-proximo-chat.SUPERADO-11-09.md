Estamos refazendo o Bestiário do meu sistema de RPG (Projeto - M, o de Jujutsu Kaisen).

O trabalho mora em /media/mizuki/HD Externo II/Claude/Bestiario/, FORA do repositório.

Leia estes, nesta ordem, e você está a par de tudo:

04-fase-1/ESTADO-onde-paramos.md — o estado.
04-fase-1/A-FILA.md — a fila.
03-bloco/RASCUNHO-5-o-bloco-em-branco.md — o bloco, e a máquina de três passos.
07-catalogo/LEIA-ME-o-catalogo.md — o outro lado do livro, e as regras de escrita dele.
Não me peça pra recontextualizar.

✅ A MÁQUINA ACABOU. ✅ E O CATÁLOGO ACABOU TAMBÉM, em 10/09.
Os quatro capítulos estão escritos: 01 o que é uma maldição · 02 os sete tipos · 03 quando gente vira maldição · 04 os lugares.

# O QUE SOBROU — três coisas, e a terceira é nova

| # | o quê | quem faz |
|---|---|---|
| 1 | **o repositório** — 11 mexidas na peça 26 + o validador (um commit), e 3 no gerador de feitiço (commit separado) | ⚠ você NÃO escreve no Claude 2. Lista pronta em `04-fase-1/sobrecarga/MEXIDAS-no-repositorio.md` |
| 2 | **o playtest** — as 3 fichas nv7 de `06-playtest/` | não rodou. Volta comigo |
| 3 | ### **as 6 maldições PRONTAS estão na escada MORTA** | ### é o próximo trabalho, e tem martelo meu dentro |

⚠ A checagem 5 do `conferir-bestiario.py` está VERMELHA e está CERTA em acender — o câmbio publicado é 4 e o implementado é 8. Ela apaga quando o commit da peça 26 entrar.

# 🔴 O ITEM 3 — leia isto antes de qualquer coisa

**`04-fase-1/fila/MEDIDA-as-seis-prontas.md` · conta em `fila/medir-as-seis-prontas.py`.**

A peça 26 §8 diz que "As maldições prontas" FECHARAM na v0.214 — seis bichos do nv2 ao 6, folclore japonês, dentro do `05-material/bloco-de-inimigo.docx`. **Elas existem e fecham por dentro.** O problema é que a escada mudou depois delas.

as seis usam: `Ronda` · `Dupla` · `Alcateia` — **as três mortas**
a escada viva: `Capanga` · `Ameaça` · `Desastre` · `Catástrofe` · `Calamidade`
**em categoria viva: `0` de `6`.**

⚠⚠ **E isto NÃO está na `MEXIDAS-no-repositorio.md`** — ela cobre a peça 26 e o gerador de FEITIÇO (`partC.js`/`partD.js`). O `gerador-inimigo/` não é nenhum dos dois. Quem executar o commit de hoje e der por fechado deixa as seis pra trás.

⚠ **E tem um martelo meu dentro, não é só execução:** a `Dupla` morreu sem herdeiro nomeado, e 2 das 6 são dela. `Ronda` ⟹ `Ameaça` e `Alcateia` ⟹ `Capanga` saem sozinhos; a `Dupla` não. **Meça antes de me perguntar, e me traga a conta em vez da pergunta.**

# O QUE FECHOU EM 10/09 (noite) — o catálogo 04

**`07-catalogo/04-os-lugares.md`**, escrito com 3 agentes de pesquisa (413.742 tokens ≈ R$55). Os três salvaram: `PESQUISA-04a` (obra) · `-04b` (comunidade/Volo's) · `-04c` (design).

Os quatro achados que mudam a mesa:
- **falta um fator na conta: a emoção precisa CONVERGIR.** Não basta muita emoção ruim — tem que ser a MESMA. ⟹ a pergunta de improviso vira *"todo mundo aqui teme a mesma coisa?"*
- **são DOIS motores:** acúmulo (sem culpado, investiga o lugar) × contaminação (tem culpado e objeto, investiga gente). ⚠ E a obra mostra quase só o segundo.
- **o único caso em que a obra explica a causa pelo lugar é uma ADJACÊNCIA** — cemitério do lado do prédio vazio.
- **DESLIGAR não é RESOLVER.** Exorcizar cala o lugar; a causa fica. A obra não trata disso — o capítulo escolhe e declara que a escolha é nossa.

**E o quarto experimento natural apareceu, MEDIDO:** `0` de `23` blocos do SRD 2014 ganham uso extra em covil; no 2024 são `27` de `32`, e o extra é sempre `+1`. O campo ADICIONOU preço de covil entre as edições. ⚠ O Draw Steel dá ficha ao LUGAR; o D&D 2024 dá `+1` ao MORADOR — os dois concordam que a casa dele é mais cara e discordam de quem carrega a conta.

**✅ E o martelo do lugar já caiu:** o lugar NÃO vira peça de máquina. `fila/DECIDIDO-o-lugar-nao-vira-peca.md`. O argumento veio de casa — a decisão 8 fechou que o inimigo não conta PE, então dar preço ao cenário daria ao lugar uma moeda que o chefe não tem. **A opção ficou desenhada fora do livro, com o gatilho que a reabriria. Não é pendência.**

# O CATÁLOGO — fechado, e ele tem regras próprias

`07-catalogo/`. Modelo Volo's Guide: o que é, como abordar, e o que a mesa encontra sem lutar.

⚠⚠ AS DUAS REGRAS DE ESCRITA DO CATÁLOGO
**1 · Nem tudo é regra. Marque o peso.** `REGRA` (a mesa segue, com dono — no catálogo é RARO e ele só APONTA, nunca cria) · `PADRÃO` (vale se ninguém decidir nada) · `FERRAMENTA` (oferecido, nada quebra se ignorar).
**2 · Canon pede VALIDAÇÃO, não só informação. As quatro perguntas:** o que eu INFERI, eu conferi? · existe CONTRA-EXEMPLO? · o status MUDOU depois? · falta CLASSIFICAÇÃO?

⚠⚠⚠ E A COISA MAIS IMPORTANTE: ele me corrigiu QUATRO vezes em 10/09, todas pela mesma causa — publiquei antes de conferir contra a fonte primária. ("o D&D 2024 apagou a vulnerabilidade" era falha de coleta · "20× entre o Cone e a Linha" era conta errada · "maldições não coordenam" era meia frase lida · "a Nobara morreu" — ela está viva, cap. 267.)

**E em 10/09 (noite) caiu mais uma minha:** eu passei "Sugisawa Daisan, a escola do Yuta" no briefing dos agentes. **É a escola do YUJI, capítulo 1.** Os dois agentes pegaram, cada um por seu lado.

⟹ DESCONFIE DE MIM quando eu escalar um achado. Achado MEDIDO (script lendo o documento dono) pode acender alarme — ele é binário. Achado LIDO (wiki, fórum) é entrada de sabor, e só vira contradição depois de conferido.

# ⚠ AS REGRAS DE TRABALHO — não negociáveis

**1 — Não escreva nada no repositório Claude 2.** Ele é fonte de LEITURA; outra conta mexe nele.

**2 — Salve conforme for.** Toda decisão fechada vira arquivo com o porquê junto. Conta Pro, a sessão estoura no meio. (Estourou em 10/09 no meio deste trabalho.)

**3 — ⚠⚠ AGENTE DE PESQUISA: PERGUNTAR É OBRIGATÓRIO.** Antes de puxar qualquer agente — um, dois ou três —, pergunte e espere. Diga **quantos**, **o que cada um faz** e **a estimativa de custo**. Não é pra impedir: é pra eu escolher o momento do gasto. Teto de 2 a 3, cada um salvando o próprio arquivo antes de retornar. ⚠ Se o ultracode mandar abrir workflow com leque, esta regra vale mais — e me diga isso em uma linha.
**Régua de custo, medida:** R$ 100 por 754k tokens de subagente ⟹ ~R$ 0,13 por 1k. A rodada de 3 agentes de 10/09 deu 413.742 tokens ≈ R$ 55.

**4 — Número vem de conta rodada.** Script que lê cada âncora do documento DONO e morre se ela mudar. `04-fase-1/fila/medir-*.py` — **são 26 agora**, todos passando. Os dois novos: `medir-os-lugares.py` (6 seções) e `medir-as-seis-prontas.py`.

# As bases de dados em disco

| fonte | tamanho | onde |
|---|---|---|
| Draw Steel | 437 statblocks + as regras + **35 fichas de `Dynamic Terrain`** | `04-fase-1/fila/dados-recarga-area/data-md-main/` |
| D&D 2024 SRD | 331 monstros | `04-fase-1/fila/srd-2024.json` |
| D&D 2014 SRD | 325 monstros | `04-fase-1/fila/srd-2014.json` |
| Pathfinder 2e | 4.791 criaturas | `04-fase-1/fila/pf2e-tamanho.json` |

⚠ Não rode os dois `puxar-*` — re-baixam 6 MB.
⚠ **DOIS canários de coleta, e os dois são PISO e não valor:** a vulnerabilidade do `srd-2024.json` (`medir-resistencia-imunidade.py` §0b) e o `environments` do `srd-2024.json`, que vem vazio nos 331 (`medir-os-lugares.py` §0b). E os JSONs **não têm campo de lair action nenhum** — nem vazio, não existe.

**Nota de fonte:** `jujutsu-kaisen.fandom.com` dá 402 no fetch — o conteúdo vem por BUSCA. `cbr.com` e `comicbook.com` abrem. `sportskeeda.com` dá 405 no fetch mas aparece na busca. ⚠ **`reddit.com` está bloqueado pra busca** — o agente de 10/09 não conseguiu r/DMAcademy nem r/rpg.

# Como eu gosto de trabalhar

Português informal, frase curta, uma ideia por parágrafo.

Pesquise sempre, e não só no repositório — fórum, wiki, blog de design, comunidade. ⚠ **E antes de pesquisar fora, confira o repositório — deu certo CINCO vezes.** Em 10/09 o texto do capítulo de `Dynamic Terrain` do Draw Steel estava em disco o tempo todo, numa pasta que ninguém tinha aberto.

Valide contra os três sistemas sempre que der: Draw Steel, D&D 2024 e Pathfinder 2e. "Sempre métrica antes de resposta em achismo."

Se der pra pesquisar e validar, pesquise e me traga a resposta em vez da pergunta. Só chega em mim o que é escolha de sabor. E se achar problema, resolva — não só reporte.

# RETORNO — o que o `Claude 2` fez com a entrega

*10/09/2026 (noite). Sessão que executou o `PARA-O-CLAUDE-2.md`. **Este arquivo é o relatório de volta**:
o plano, o que a entrega não cobria, cada commit com o resultado dos validadores, e a lista de
`ÂNCORA PERDIDA` dos scripts da fila.*

> Mizuki saiu por 20-30 min e deu autonomia total. Os commits estão num ramo próprio,
> **`bestiario-escada-viva`**, e **nenhum push foi feito**. O `main` está intacto.

---

## Retrato ANTES de mexer

| | |
|---|---|
| validadores do `Claude 2` | `26` de `sistema/03-mecanica/` + `conferir-repositorio.py` + `pac7.py` + `v7.py` — **todos verdes, `0` PULADA** |
| scripts da fila do Bestiário | **`41` de análise** (a entrega fala em `34`; a fila cresceu) — **`41` de `41` passam** · os `3` `puxar-*` não rodam (baixam `6 MB`) |

---

## ⚠ O que a entrega NÃO cobria, e eu achei vasculhando

| # | o buraco | por que importa |
|---|---|---|
| **1** | **a escada da peça 26 inteira** — o §3, o §4, o §4.1, o §4.2, o §4.4, o §6.4 e o §6.5 publicam `Ronda`/`Dupla`/`Alcateia`/`Calamidade` em `39` linhas, e as `15` mexidas do § A só trocam `4` delas | as checagens `3`, `4`, `7.1`, `9.1`, `9.2` e `9.5` do `conferir-bestiario.py` e o bloco `7` do `conferir-ficha.py` **leem a tabela do §4**. Sem trocar a escada inteira no commit `A`, o commit `C` não fecha verde nunca |
| **2** | **a tabela `Inimigos` do MANUAL publica o `Capanga` morto** — `manual/gerador/partF.js` L155-169: colunas `Capanga: vida/dano` = `chefe ÷ 4` / `chefe ÷ 3`, e o texto *"Quatro capangas equivalem a um chefe"* | é exatamente o *"outro Capanga"* que o `DECIDIDO-o-capanga-unico.md` matou. A varredura da entrega procurou os NOMES das categorias mortas, e o manual não usa nenhum — por isso passou. E o `dados.js` diz que o manual é a autoridade das colunas de capanga |
| **3** | **o `40-fundamento.md` do livro é o segundo dono das Melhorias** | o commit `B` mexe no `Anteparo` do `partD.js`, e a checagem `12` do `conferir-repositorio.py` compara as duas tabelas. A `v0.217` já fez assim: `partD.js` + `40-fundamento.md` + `.docx` + os quatro artefatos do livro |
| **4** | o `Anteparo` já está declarado `aberta` no `ESTADO-revisao.md` L53 (*"o livro diz que o tamanho depende da Forma; o manual cala"*) | a mexida `28` resolve essa divergência — os dois lados passam a dizer a mesma coisa e a linha fecha |

---

## O plano — ordem dos commits

| ordem | commit | encosta | por que nesta ordem |
|---|---|---|---|
| `1` | **`B`** · o gerador de feitiço | `partC.js` · `partD.js` · `40-fundamento.md` · `ESTADO-revisao.md` (fecha o `Anteparo`) · regera o `.docx` do manual e os quatro do livro | independente, e é o menor |
| `2` | **`E`** · a `Sobrecarga` | `partD.js` · `40-fundamento.md` · `.docx` · `ESTADO-revisao.md` L43 · `sobrecarga.py` · `conferir-acao.py` · `ESTADO-ATUAL.md` | na ordem que a entrega manda (donos → docx → linha 43 → conta → checagem → estado) |
| `3` | **`A`** · a peça 26 | `26-bestiario.md` inteira na escada viva + `conferir-bestiario.py` | antes do `C` e do `D`, que dependem dela |
| `4` | **`D`** · a peça 15 | `15-invocacoes.md` | logo depois do `A`. ⚠ **a pergunta de desenho fica PARA O MIZUKI** — ver abaixo |
| `5` | **`F`** 🆕 · a tabela `Inimigos` do manual | `partF.js` + `.docx` | o buraco `2`. Antes do `C`, porque o `dados.js` copia o manual |
| `6` | **`C`** · o gerador de inimigo | `dados.js` · `make.js` · `COMO-USAR.txt` · `conferir-ficha.py` · regera o bloco | espera os seis blocos novos do livro (ver `08-livro/PASSADA-3-blocos.md`) |
| `7` | **as sobras** | `ESTADO-ATUAL.md` · `mesa-01-grupo-01.md` · `CHANGELOG.md` (entrada `v0.221`, e a `v0.220` marcada revertida) | fecha a versão |

**Uma versão só, a `v0.221`, aberta no último commit.** *A entrega pede UMA entrada de CHANGELOG.*

## A pergunta de desenho da peça 15 — NÃO decidida

Vou aplicar o que é FATO (a tabela da morte na escada viva, a tabela do corpo machucado
recomputada, a frase *"`Alcateia`, que é também o capanga"*). **A escolha entre as duas saídas
fica com o Mizuki:**

> *ou a peça 15 registra que a morte definitiva virou coisa quase só do gatilho de excedente,
> ou o corpo forte encolhe.*

---

## Andamento

*(atualizado a cada commit)* — ramo `bestiario-escada-viva`, nenhum push.

| commit | hash | o quê | validadores depois |
|---|---|---|---|
| **`B`** | `d5b8410` | `Cone`, `Linha`, `Anteparo` nos dois donos; divergência do `Anteparo` fechada | ✅ todos verdes |
| **`E`** | `1476aa3` | a `Sobrecarga` com a Reação, `Leve` nos dois donos; `sobrecarga.py` refeito; checagem `5` do `conferir-acao` estendida | ✅ todos verdes |
| **`A`** | `900da9c` | a peça 26 inteira na escada viva + as `15` mexidas; `conferir-bestiario` reescrito; `17` perturbações (§7.2) | 🔴 `2` declarados: checagem `5` (manual) e bloco `7` do `conferir-ficha` |
| **`F`** 🆕 | `bd40ef7` | a tabela `Inimigos` do manual com o `Capanga` da escada; manual **v7.26** | 🔴 `1` declarado: bloco `7` |
| **`D`** | `4514b4f` | a peça 15 na escada viva; a régua frouxa REGISTRADA; checagem `12f` ligando a peça 15 à 26 | 🔴 `1` declarado: bloco `7` |
| **`C`** | `3ef6809` + `4e42c63` | peça 26 ganha o tamanho (§3.3) e a área natural (§6.5); `dados.js` com as cinco categorias, o `0,923`, o capanga da escada e as seis com o texto do livro; `make.js` imprime as seis no molde 5e; `conferir-bestiario` `3.3`/`9.5`/`9.6`; `conferir-ficha` bloco `7`. **O `4e42c63` fecha:** arnês de `38` perturbações (`38` de `38`) no §7.2 da peça 26, e os dicionários de número ganham `uma`/`duas` — defeito que o arnês achou | ✅ todos verdes, `0` PULADA |
| **sobras** | `4bf52eb` | **`v0.221` fechada:** CHANGELOG (e a `v0.220` marcada revertida), `README`/`LEIA-ME`/`ESTADO-ATUAL` na `v0.221`, as três linhas de regra morta do `ESTADO-ATUAL` marcadas, nota na `mesa-01`, base da lista branca `169 → 171` itemizada pelo diff | ✅ todos verdes, `0` PULADA · `3` avisos que não falham (`7.4` e duas `7.6` do DejaVu) |

## Onde parou — 11/09 (fim da tarde)

**O `Claude 2` está FECHADO na `v0.221`: `8` commits no ramo `bestiario-escada-viva`, árvore limpa, NENHUM push.** *O `main` segue intacto.*

| # | o quê | estado |
|---|---|---|
| `1` | fechar o `C` | ✅ `4e42c63` |
| `2` | sobras e versão | ✅ `4bf52eb` |
| `3` | rodar a fila do Bestiário | ✅ `41` rodados, `6` `ÂNCORA PERDIDA` — tabela abaixo. **Nenhuma reancorada** |
| `4a` | `gerar-as-seis.py` | ✅ lê as `PRONTAS` do `dados.js` pelo `node`, com a âncora nova da conta do golpe e duas guardas de dono duplo (faixa/categoria contra o `DECIDIDO`; `0,923` do `RASCUNHO-5` contra o `dados.js`). **O capítulo 8 saiu idêntico byte a byte.** O `seis-prontas.json` virou `.SUPERADO-11-09` |
| `4b` | `gerar-tabelas.py` · `gerar-exemplo.py` | ✅ rodam limpos, capítulos idênticos |
| `4c` | passada de texto `40`–`90` | ✅ **fechada inline, sem agente** (decisão do Mizuki) — `conferir-voz.py` em `0` achados (eram `51`), `--estrito` sai `0`, nenhum número de regra mudou. Log de cada capítulo no `08-livro/PASSADA-3-texto.md`, inclusive o `20` e o `30` |
| `4d` | `build.py` normal e `--duas` | ✅ **regerados em 11/09** — `61` e `34` páginas. *Os dois avisos já existiam em 10/09: sem capa de arte (a pasta `arte/` não existe no Bestiário), e DejaVu Sans Mono no lugar do IBM Plex Mono em negrito e itálico dentro de crase — a mesma falta de face do Manual, item `4` da fila da `v0.220`* |
| `4e` | `TABELA.md` com meio-ponto pra cima | ⏳ achado `1` do agente dos blocos, lá embaixo |

### ⚠ Pede o ok do Mizuki

| | |
|---|---|
| **push do `Claude 2`** | ✅ **autorizado em 11/09 — e FALHOU com `403`.** O git desta máquina autentica como `Gustavo-MrTs`, e essa conta não tem permissão de push em `cupcake-mochi/JJK---Project`. **O ramo continua só local.** Depois de trocar a conta: `git push -u origin bestiario-escada-viva`. *O merge no `main` é outra decisão* |
| **o recorte da entrega** | ✅ **autorizado — commit feito, push FALHOU com o mesmo `403`** (`cupcake-mochi/JJK---PDF---RPG`). O commit `a7cdfc4 recorte da v0.221` está em `finalizado/`, só local. Depois de trocar a conta: `cd finalizado && git push` |
| **os `.zip` em `sistema/skills/`** | `7` arquivos não rastreados, de 11/09 13:31 — **não são desta execução**, e ficaram fora dos commits |

**Ferramentas desta execução** em `ferramentas-claude-2/`: `valida.sh` (a suíte, só resumo e falha), `sincroniza-entrega.sh` (o passo 0 do `subir.sh`, sem commit), `arnes26.py` (as `17` do commit `A`), **`arnes-c.py`** (as `38` do `C`), **`brancos-diff.py`** (itemiza a lista branca da `7.2` entre duas árvores da entrega).

## O livro — a passada de texto fechou (11/09)

*O log, capítulo a capítulo, está no `08-livro/PASSADA-3-texto.md`.*

**`conferir-voz.py`: `0` achados em todos os capítulos** (eram `51`), `0` referência pendurada, `0` termo sem
destino, e o `--estrito` sai `0`. **Nenhum número de regra mudou** — cada diferença do guard está explicada.
Os três geradores rodaram depois e deixaram os capítulos byte a byte iguais.

| | |
|---|---|
| **três frases que tinham virado mentira, corrigidas** | "Resistir a `Físicos` é a célula mais cara" (cap. `5` e vocabulário — a mais cara é a imunidade, `2,50` contra `1,43`) · "Área reparte a cota" (cap. `6` — a frase que o commit `A` matou na peça 26) · "a `Vida e golpe por faixa` publica o golpe cru" (cap. `9` — ela já traz o `0,923`) |
| **duas regras alinhadas ao dono** | a área natural resolve por Teste de Resistência (`P1`), e a trava de área é "por rodada" (cap. `7` e `9`), como a peça 26 §6.5 |
| ⚠ **pedidos de desenho do cap. `5`, com o Mizuki** | a célula `O golpe` fica no cabeçalho? `Ações Múltiplas` conta como entrada na linha de `6`? |
| ⚠ **pergunta de conta do cap. `6`, pro dono da regra** | o orçamento de uma ação sai com o `0,923` depois da média (peça 26 §6.5, checagem `9.1`) e o golpe impresso sai com ele antes do dado (`make.js`) — `0,1` ponto em `3` células. **O livro segue a peça** |
| ⚠ **conferir contra a obra** | a generalização sobre os feiticeiros que morreram (cap. `3`) e o "dedo deixado" nos quatro lugares (cap. `4`) |

---

## ⚡ As `ÂNCORA PERDIDA` da fila — 11/09, depois de `B` `E` `A` `F` `D` e o `C` de trabalho em andamento

**`41` scripts rodados** (`fila/*.py` + `sobrecarga/*.py`, menos os `3` `puxar-*`). **`35` passam, `6` morrem, e os `6` morrem com `ÂNCORA PERDIDA`.** *Nenhum morre de outra coisa.* Saída de cada um em `…/scratchpad/fila-agora/`.

| # | script | a âncora que morreu | o que o dono diz hoje | commit | leitura |
|---|---|---|---|---|---|
| `1` | `medir-a-dupla.py` L195 | `**Quatro 'Ronda' não valem uma 'Alcateia': elas cobram '0,75 ×' a '0,77 ×'` | `**Quatro 'Ameaça' não valem um 'Desastre': elas cobram '0,75 ×' a '0,77 ×'` — §4.3 | `A` | 🟢 **só nome.** O número ficou, e a peça diz que o modelo do Bestiário refez a conta na escada viva e deu o mesmo |
| `2` | `medir-o-encontro-misturado.py` L53 | a mesma | a mesma | `A` | 🟢 **só nome** |
| `3` | `medir-quadrado-e-retangulo.py` L96 | `\['Linha', '\w+', '([\d,]+) m por ([\d,]+) m'` — a regex exige a aspa logo depois do `1,5 m` | `'18 m por 1,5 m. Quando o comprimento chega ao topo da escada, Maior passa a subir a largura: 1,5 m → 3 m → 4,5 m.'` — `partC.js` L55 | `B` (mexida `29b`) | 🟢 **só forma.** Tirar a aspa do fim da regex |
| `4` | `medir-a-imunidade-a-condicao.py` L59 | `O chefe age três vezes por rodada e a luta dura três rodadas — '3 × 3'` — a prova dos *"nove golpes"* do §5 | **morreu de propósito**, pela mexida `A.1` (*"a prova dos 'nove golpes' cai junto"*). Os dois números vivem em outras frases: §4.2 *"O `Desastre` age três vezes"* e §4.6 *"Numa luta de três rodadas"* | `A` | 🟡 **a premissa vive, a frase morreu.** Reancorar em duas âncoras. ⚠ **E o script lê `finalizado/regra/26-bestiario.md`, a CÓPIA, e não a fonte** |
| `5` | `medir-morte-e-imunidade.py` L44 | `**Resistência ao grupo 'Físicos' custa (um\|meio) degrau` | `**Resistência ao grupo 'Físicos' multiplica o fator da categoria por '1,43'.**` — §6.3 | `A` (mexida `5`) | 🔴 **mudou por decisão** — a moeda virou fator (`DECIDIDO-o-degrau.md`). O script lê o preço em degrau e tem de passar a ler o multiplicador |
| `6` | `medir-a-peca-15.py` L125 | a tabela da morte em definitivo com `5` linhas de golpe | **`4` linhas:** `Capanga` e `Ameaça` · `Catástrofe` · `Desastre` e `Calamidade` · **crítico de `Desastre`** (`16d8 + 37` = `165`, destrói o `Coro` e não o corpo forte) | `D` | 🔴 **mudou por decisão** — a peça passou a publicar a escada viva e a régua frouxa. O §2 do script PREVIA isso; agora ele pode CONFERIR em vez de prever |

*As aspas simples na coluna das âncoras são crases no original (a tabela não aceita crase dentro de crase).*

> ## ✅ AS `6` FORAM REANCORADAS em 11/09, à noite — e **`43` de `43` passam** agora.
> *Laudo em `04-fase-1/fila/MEDIDA-a-reancoragem-da-fila.md`.* **Nenhuma âncora foi afrouxada.**
>
> ⚠ **A leitura `🟢 só nome` da linha `1` estava OTIMISTA.** *Trocar `Ronda`⟹`Ameaça` destravou a
> primeira âncora e o `medir-a-dupla.py` morreu em mais SEIS, uma atrás da outra.* **O fundo do poço:
> ele mede a TRANSIÇÃO de uma escada pra outra, e a escada MORTA deixou de existir em documento
> nenhum quando a peça 26 foi reescrita.**
>
> **Entrou uma cópia de museu com procedência de `git`** — `04-fase-1/museu/a-peca-26.v0.220.md`,
> byte a byte do commit `fc1cb79`. *Registro com endereço não é número à mão.*
>
> **E as `3` que morriam de `FileNotFoundError` não eram âncora:** elas abrem os corpora por caminho
> relativo e rodam da RAIZ do `Bestiario/`.

*O pedido daquela rodada era só trazer a lista.* `1`, `2` e `3` pareciam troca de regex; `4`, `5` e
`6` pediam ler o laudo antes, porque o que o script mede mudou junto — **e a `1` pedia mais que isso**.

---

## As decisões desta execução

### Os martelos do Mizuki nesta sessão (11/09)

| | decisão |
|---|---|
| **peça 15** | **registrar a régua frouxa** — nenhum golpe único destrói o corpo forte; o corpo forte não encolhe |
| **manual** | **commit `F` separado** — o `Capanga` morto sai da tabela `Inimigos` |
| **commit `C`** | **completo**: levar pra peça 26 as regras de **tamanho** e de **área natural** (hoje só no Bestiário), com validador, e o `make.js` imprimir o bloco 5e igual ao do livro |
| **as 5 propostas do agente dos blocos** | ✅ **todas aprovadas** — `P1` área natural por TR (e no máximo uma área por turno) · `P2` a `Intervenção 1` é um ataque do bloco sem o vizinho · `P3` o `Fogo-de-Raposa` da Kitsune (`Projétil` de Classe 1, `4d8` de Fogo, `18 m`) · `P4` os traços inventados · `P5` `Derrubado`, terreno difícil e tirar cobertura de graça nas Intervenções 2 e 3 |
| **agentes** | um por vez. O dos blocos terminou (`253k`); o da prosa entra depois dos commits |

### Achados do agente dos blocos que voltam pro Bestiário

1. **`TABELA.md` × `make.js` numa célula:** `Catástrofe` nv `2-4` — a TABELA publica `1d4 + 2` (o `round` do Python leva `2,5` pro par) e o gerador dá `1d4 + 3` (o `Math.round` sobe). *Regerar a TABELA com o meio-ponto para cima, ou declarar a regra do `fixo` do dado.*
2. **O bloco antigo das seis imprimia a linha de defesa do nível de baixo pra faixa inteira** — errado no Hitotsume e no Oni (nv `6-8`) e na Kitsune (nv `10-12`). Corrigido no livro; o `.docx` corrige no `C`.

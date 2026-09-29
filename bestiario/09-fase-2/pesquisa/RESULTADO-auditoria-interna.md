# Auditoria interna da máquina de inimigo — leva 1

*27/09/2026. Só leitura no repositório `Claude 2/.claude/worktrees/quirky-wiles-46c283` (HEAD `e536020`, v0.274, com mudanças ainda não commitadas no disco: a peça 26 l.388 já cita a peça 19 da v0.277). Li o estado do disco.*
*Notas de trabalho: `NOTAS-auditoria-interna.md`, nesta pasta.*

**Marcas.** `[C]` texto citado do repositório ou da fonte · `[F]` fonte oficial aberta, conferida por mim: o **SRD 5.1** (CC-BY-4.0, `media.wizards.com/2023/downloads/dnd/SRD_CC_v5.1.pdf`; o texto extraído está em `srd51-norm.txt`, nesta pasta) · `[I]` inferência ou conta minha.
**Caminhos.** Tudo relativo à raiz do worktree. "peça 26" é `sistema/03-mecanica/26-bestiario.md`; "livro NN" é `bestiario/08-livro/capitulos/NN-*.md`; "manual" é `manual/gerador/partF.js`, que gera a seção `Inimigos` do `Fundamento-MANUAL-v7.docx`.

---

## 0. O que achei, em doze linhas

1. **A queixa de 27/09 já tinha sido feita e fechada em 08/09.** O Mizuki escreveu *"uma mesa nunca vai ter mais de 6 players e talz, ent n precisa pensar nisso de 7-8 players"*, e a escada fechou com a Calamidade como **"mais que `6`"** (`bestiario/04-fase-1/a-escada-com-numero.md` l.90 e l.100; `decisoes-fase-1.md` l.13) `[C]`. **O `8` não foi decidido: ele é o fator `2,00` passado pela fórmula `personagens = fator × 4`** (peça 26 l.176 e l.178) `[C][I]`.
2. **Nenhum validador trava o encontro em 6 pessoas.** As checagens conferem a derivação, e o contra-teste da checagem 3 prova que uma Calamidade de 8, ou de 10, fica verde (peça 26 l.759 e l.789) `[C]`. A única trava de mesa é a da 9.5: uma **pronta** não pode exigir mais que a mesa padrão de 4 (`conferir-bestiario.py` l.1408 e l.1476-1478) `[C]`.
3. **Existem cinco premissas de chão, e elas se prendem umas nas outras.** A mesa de 4 vem do manual (`manual` l.168). A luta de 3 rodadas também vem do manual (`manual` l.171). As 3 ações do Desastre são o piso da régua de condição da peça 19 (l.87-100). O `0,923` da Intervenção foi medido com 3 ações. A Recarga cobra metade das pessoas da categoria. Mudar qualquer uma delas acende checagens em cadeia, em mais de um validador (§3).
4. **O "duro" tem duas origens, e só uma é o D&D.** O que veio do 5e ao pé da letra é **forma**: a ordem do bloco, `Ações Múltiplas`, `média (dados)`, `Recarga 5-6`, a grade de tamanho e a Ação Lendária virando Intervenção. A rigidez de **número** é do próprio projeto:
   - a ficha do inimigo é a do personagem sem o Caminho (peça 26 l.11), coisa que o D&D **não** faz;
   - um fator só serve para vida e dano;
   - a luta de 3 rodadas está gravada em toda conta;
   - o golpe é igual em toda ação;
   - as três Intervenções seguem um molde fixo.
5. **A melhor prova do "duro" já está medida.** No teste do Sukuna, a vida da máquina bateu em `1,03×` a do Mizuki, e o dano, em `2,66×`. A anotação diz: *"na máquina isso não é montagem legal — os dois fatores da categoria andam juntos"* (`ESTADO-onde-paramos.md` l.843-846) `[C]`.
6. **Da mesa sai uma evidência só**, a de 07/09 (`mesa-nd20.md`). Nela, a CD foi validada, a Defesa do chefe foi apontada como baixa e o dano foi ajustado na mão durante a luta. A camada de montar inimigo foi **contornada**, e não usada (l.11) `[C]`.
7. **O que passa de 6 pessoas** vem da Calamidade de 8, da Expansão `×1,92`, da imunidade a Físicos `×2,50` e do Sukuna de `18,4`. É **aviso, e não trava**, por decisão escrita (peça 26 l.390 e l.430) `[C]`. Mapa completo no §5.
8. **A "sub-categoria por pessoas" da amiga já existe como dado, mas não como regra.** Existe a tabela de rodadas por tamanho de mesa (`a-escada-com-numero.md` l.106-110). E já existe o motivo pelo qual a fase 0 matou a categoria nomeada por número de jogadores: *"Dupla? são dois inimigos? Aaaa são para dois players"* (`00-fase-0/decisoes.md` l.49) `[C]`.
9. **Achei 11 divergências internas** entre donos e cópias (§4.4 deste arquivo). As que mais pesam:
   - o livro ensina o encontro misturado de um jeito que a peça não ensina;
   - o vocabulário do livro diz que o `Controlador` paga em dano;
   - o livro tem duas regras de papel sem dono na peça;
   - a peça 19 guarda o capanga morto de `73`;
   - o `0,923` é aplicado igual nas três categorias, mas foi medido só para a de 3 ações.
10. **A escada tem quatro cópias vivas, cada uma com o próprio leitor:**
    - a peça 26 §4, que é a dona;
    - o `dados.js`, que o `conferir-ficha` bloco 7a vigia;
    - a `bestiario/04-fase-1/TABELA.md`, que é a entrada dos scripts do livro;
    - o `03-bloco/RASCUNHO-5`, de onde o livro lê o `0,923`.
11. **Cerca de 30 scripts de medição leem a peça 26 por regex** (§3.5). Um redesenho que mude a forma das tabelas derruba todos eles com `ÂNCORA PERDIDA`, antes de qualquer número.
12. **Lacuna declarada.** O DMG 2014 é livro fechado, e as origens que o projeto atribui a ele não estão no SRD. São elas: a média das 3 primeiras rodadas, a área contando 2 alvos numa mesa de 4, a tabela de PV efetivos e o passo 13. Registro como citação do projeto `[C]`, **sem conferir**.

---

## 1. O inventário

Cada linha diz onde mora a regra, o que ela faz, quem é o dono do número e a origem dela:

- **D&D literal:** a regra do 5e copiada, com o livro citado.
- **Adaptado:** o molde é do D&D ou de outro sistema, com mudança.
- **Medido:** o número saiu de conta ou simulação do próprio projeto.

### 1.1 A base: a linha do manual e a escada

| # | fórmula / regra | onde mora | o que faz | dono do número | origem |
|---|---|---|---|---|---|
| 1 | **A linha `Inimigos`**, em 7 faixas: grupo por rodada `~38…~315`, vida do chefe `105-123…870-1020`, dano do chefe `17…219`, capanga `9·4…78·55` | `manual` l.155-166. Cópias: `dados.js` l.15-24, `TABELA.md`, `conferir-aptidoes.py` l.86 (`CHEFE`) | É a régua de onde tudo reescala | o manual | **Medido.** A calibragem da v0.201 foi contra o d20 2014 e o PF2e (peça 26 l.1005-1011) `[C]` |
| 2 | **A mesa de 4:** *"A conta supõe quatro personagens: um focado em bater, dois medianos, um de apoio."* | `manual` l.168; peça 26 l.168 e l.178; peça 1 l.207-215 ("8 de vida por nível") | Calibra a linha contra 4 personagens | o manual | **Adaptado.** O ND do D&D supõe *"party of four adventurers"* (SRD 5.1 p.258) `[F]` |
| 3 | **A luta de 3 rodadas:** *"Chefe sozinho precisa de cerca de três vezes o dano de rodada do grupo em vida, e é isso que faz a luta contra ele durar três rodadas."* | `manual` l.171; peça 26 l.327-335; checagem 5.2 (`conferir-bestiario.py` l.678-743) | Vida do chefe = 3 × a saída do grupo | o manual | **Adaptado.** O projeto cita o DMG 2014: *"média das três primeiras rodadas"* (peça 26 l.590 e l.1009; `refutacao/prova-p1-dmg2014.md`) `[C, não conferido — livro fechado]` |
| 4 | **Dano do chefe por rodada = 90% da vida de um personagem do nível**, e o golpe é um terço da linha | `manual` l.172; peça 26 l.1005 | Fixa a pressão | o manual | **Medido.** Derruba `2,70` pessoas em 3 rodadas, contra `2,56-2,70` do d20 2014 e `~2,8` do PF2e (peça 26 l.231-237) `[C]` |
| 5 | **A categoria:** `Capanga — ×0,25` · `Ameaça 1 ×0,25` · `Desastre 4 ×1,00` · `Catástrofe 6 ×1,50` · `Calamidade 8 ×2,00` | peça 26 l.170-176; livro 60 l.17-23; `dados.js` l.30-36; `TABELA.md` | Reescala a linha do manual | peça 26 §4 | **Projeto** (a ideia é do Mizuki, peça 26 l.168), sobre a base de 4 do D&D. O `8` sai da fórmula; a fase 1 escreveu "mais que 6" `[C]` |
| 6 | **`personagens = fator × 4`** e a moeda contínua `fator novo = fator × multiplicador` | peça 26 l.178 e l.381; livro 60 l.11-12; livro 90 l.61 | Converte todo traço em "pessoas" | peça 26 §4 | **Projeto.** O degrau como moeda morreu na v0.221 (`ESTADO` l.562-578) `[C]` |
| 7 | **As ações declaradas `1 · 1 · 3 · 5 · 6`** | peça 26 l.170-176 e l.200-206; `dados.js` l.30-36 | O golpe é a rodada ÷ as ações | peça 26 §4.2 e peça 19 §2.2 (o piso 3) | O `3` do Desastre sai da frase do manual (*"perde a ação três vezes por rodada"*) e é o **piso medido** da peça 19 (l.87-100; `conferir-dano.py` checagem 12). **O `5` e o `6` são declarados, sem fórmula** (peça 26 l.202-203) `[C]`. Não achei medida própria deles `[I]` |
| 8 | **O fator de dano da `Intervenção`, `×0,923`** | peça 26 l.565; livro 60 l.27-28; `dados.js` l.73; `03-bloco/RASCUNHO-5` (lido por `gerar-tabelas.py` l.85-92) | Paga a ação extra | peça 26 §6.5 | **Medido.** São `0,75` ação extra numa luta de 3 rodadas de **3 ações** (`fila/MEDIDA-a-intervencao.md` l.395-445) `[C]` |
| 9 | **O capanga:** vida = grupo ÷ 4, para baixo; dano = chefe × 0,25; 8 corpos em pool; **1 Desastre = 8 capangas** | peça 26 l.180 e l.302-323; `manual` l.169; livro 60 l.159-167 | É o bando | peça 26 §5 e o manual | **Medido** por simulação de fogo concentrado (checagem 5, l.600-617). A forma do Draw Steel foi medida e **inflava** o encontro (`a-escada-com-numero.md` l.64-78) `[C]` |
| 10 | **A trava de empilhamento:** no máximo 3 corpos por alvo, e do 2º em diante pela metade | peça 26 l.321; livro 60 l.30-38; `dados.js` l.211 | Impede o esquadrão de concentrar | peça 26 §5 | **Adaptado** do Draw Steel, que trava em 2 ou 3 corpos por alvo (`ESTADO` l.810-814) `[C]` |
| 11 | **A sub-categoria:** o chefe fica com `100 / 91,5 / 83,0 / 74,5%` com 0 a 3 capangas | peça 26 l.208-227; `dados.js` l.107-110; `make.js` l.444-452 | Reparte o encontro sem mudar o tamanho | peça 26 §4.5 | **Medido:** 201 frações × 29 níveis `[C]` |
| 12 | **O encontro misturado:** `fator = fator do chefe + capangas × 0,083`, "até quatro" | livro 60 l.40-56; livro 90 l.65; `ESTADO` l.607-624 | Soma o chefe **inteiro** com os capangas | ⚠ não está na peça 26 (divergência 1, no §4.4 deste arquivo) | **Medido** (`fila/MEDIDA-o-encontro-misturado.md`) `[C]` |
| 13 | **4 `Ameaça` = `0,75-0,77 ×` 1 Desastre** | peça 26 l.269; `dados.js` l.208 | Mostra que a escada não é linear | peça 26 §4.3 | **Medido** `[C]` |
| 14 | **O arredondamento:** meio para baixo; a vida do capanga para baixo por inteiro; a linha do nv 2 foi de `115` para `114` | peça 26 l.196-198 e l.325-335; `make.js` l.51 | Um ponto de vida vale uma rodada | peça 26 §4.1 e §5.1 | **Medido** `[C]` |

### 1.2 As derivadas: a ficha do inimigo como a do personagem

| # | fórmula / regra | onde mora | o que faz | dono | origem |
|---|---|---|---|---|---|
| 15 | **"A ficha de inimigo é a ficha de personagem sem o Caminho"** | peça 26 l.11 | Toda linha sai da peça dona do lado do jogador | peça 26 §1 | **Projeto, e o oposto do D&D:** monstro do 5e não se monta pela regra do personagem (`03-bloco/a-escala-do-inimigo.md` l.9-46) `[C]` |
| 16 | **`Defesa = 10 + Destreza + proteção`**, com o `±2` do papel por fora | peça 26 l.37 e l.57-66; peça 1 l.79 | Defesa `14…20` | peça 1 §5 | Projeto: é a fórmula do personagem |
| 17 | **`acerto = atributo + maestria`**; **`CD = 8 + atributo + maestria`** | peça 26 l.38-39; peça 1 l.85 e l.102 | Acerto `+4…+10`, CD `12…18` | peça 1 §5 | **Adaptado:** a CD é a fórmula de CD de magia do **personagem** do D&D (SRD 5.1 p.16: *"Spell save DC = 8 + your proficiency bonus + …"*) `[F]` |
| 18 | **A curva "de quem investe":** atributo 3 → 6 e maestria `floor((nv−2)/8)+1` | peça 26 l.55; `conferir-bestiario.py` l.177-185; `make.js` l.121 | O inimigo herda a curva do personagem | peças 1 e 2 | Projeto |
| 19 | **O refino `meio a meio`** e a **proteção `1/3 do refino + 1`** | peça 11 l.136 e l.287; peça 26 l.66 | A Defesa anda junto do refino | peça 11 | Projeto |
| 20 | **A banda:** ele acerta `50-55%` e o TR treinado falha `35%` | peça 26 l.64; peça 1 l.612-632 | Prova a derivação | peça 1 §6 | **Medido** `[C]` |
| 21 | **O orçamento de atributo:** 9 pontos, teto 3 na criação e 6 depois; +1 por marco e as escolhas que o refino não gasta; o chefe começa com 10 | peça 26 l.70-95; peça 2 l.36 e l.49; livro 50 l.76-90 | Os atributos têm de reproduzir a tabela | peças 2 e 11 | Regra do personagem; o `+1` do chefe veio do Draw Steel (peça 26 l.89) `[C]` |
| 22 | **O "orçamento apertado":** no nv 20, a Defesa e o acerto comem 10 de 15 pontos | livro 50 l.97-136 | Sobra pouca "cor" | cap. 5 | É consequência do #15 e do #21 `[C]` |
| 23 | **Integridade = metade da vida**, para baixo | peça 24 l.124; peça 26 l.34; `make.js` l.54 | — | peça 24 §3.3 | Decisão (`decisoes-fase-1.md` l.21-29) |
| 24 | **As constantes:** Reação 1 por rodada, 9 m, dois TR treinados de quatro | peça 26 l.40, l.42 e l.43 | — | peças 3 e 7 e o manual | Regra do personagem |
| 25 | **O tamanho:** grade `1×1 / 2×2 / 3×3 / 4×4`, alcance = lado × 1,5 m, metade num vizinho do `Grande` para cima, **não cobra nada** | peça 26 l.97-110; livro 60 l.112-135 | Espaço e alcance | peça 26 §3.3 | A grade é **D&D literal** (SRD 5.1 p.92: `5×5`, `10×10`, `15×15`, `20×20` ft) `[F]`. "Não cobra" foi **medido** (PF2e 4.791 e D&D 331; `ESTADO` l.697-752) |
| 26 | **O papel:** seis papéis, ganho × pagamento = `1,000`, e três deles pagam conforme as ações | peça 26 l.112-164; livro 60 l.58-110; `dados.js` l.48-69 | Redistribui a base | peça 26 §3.4, peça 1 §5.2, peça 19 §2.2 | **Adaptado e medido.** Contra o Draw Steel ficou a menos de 4% em três papéis (`ESTADO` l.794-806). O `Artilheiro` a 18 m saiu da razão mediana do Draw Steel (peça 26 l.129-133) `[C]` |
| 27 | **O grau é rótulo** | peça 26 l.15-23 | Não entra em conta | peça 26 §2 e peça 12 | Projeto |

### 1.3 O dano, as ações e os traços

| # | fórmula / regra | onde mora | o que faz | dono | origem |
|---|---|---|---|---|---|
| 28 | **O golpe = a rodada ÷ as ações**, em `N dados + fixo`, com metade em dado, `d4…d12`, no máximo 8 dados e número seco abaixo de 5 | peça 26 l.243-265; `make.js` l.65-104 | O que se rola | peça 26 §4.4 | **Adaptado.** O SRD põe a média e a expressão de dado lado a lado (p.259) `[F]`; o projeto cita o DMG 2014 para a tradução em dado `[C, não conferido]` |
| 29 | **O formato `média (dados)`**, com a média arredondada para baixo | `make.js` l.108; `GUIA-bloco-5e.md` §3 | — | o livro | **D&D literal:** *"both the average damage and the die expression are presented"* (SRD 5.1 p.259) `[F]` |
| 30 | **`Ações Múltiplas`**, primeira entrada de `Ações` em quem age mais de uma vez | livro 50 l.299-302; `GUIA` §2 | — | cap. 5 | **D&D literal:** é o *Multiattack* (SRD 5.1 p.259) `[F]` |
| 31 | **A `Intervenção`:** 3 por luta, uma de cada, no máximo uma por rodada, logo depois do turno de outra criatura. A 1ª bate, a 2ª e a 3ª mudam o campo | peça 26 l.561-569; livro 50 l.304-315; `GUIA` §7 | É a ação fora do turno | peça 26 §6.5 | **Adaptado:** a Ação Lendária do SRD, *"outside its turn… only one… at the end of another creature's turn"* (p.260) `[F]`, mais a Villain Action do Draw Steel (`ESTADO` l.834-837) `[C]` |
| 32 | **A `Recarga (5-6)`:** volta com 5 ou 6 no d6, come as ações múltiplas, bate `2,5 ×` o golpe em área, rola em `d12`; fator `×1,14 / 1,37 / 1,28 / 1,37` | peça 26 l.579-608; livro 70 l.117-138 | Jogada grande | peça 26 §6.5 | A regra do d6 é **D&D literal** (SRD 5.1 p.259) `[F]`. O `2,5×` é decisão. O fator segue o *"método do DMG 2014, cap. 9, p. 278"*, com área = 2 alvos numa mesa de 4 (peça 26 l.590) `[C, não conferido]`. O campo foi medido (D&D 2024 42%, PF2e 29-32%, Draw Steel 15%) |
| 33 | **Os rótulos de frequência:** à vontade, `1× por rodada`, `1× por luta`, `Recarga` | livro 70 l.7-18; `decisoes-fase-1.md` §8 | O inimigo não conta PE | cap. 7 | **Adaptado.** O SRD tem *Limited Usage* (X/Day e Recharge, p.259) `[F]`; o campo usa rótulo em 8 de 9 sistemas `[C]` |
| 34 | **O inimigo não conta PE, e a cota de dano é o orçamento** | peça 26 l.354-360 | — | peça 26 §6.1 | **Adaptado.** O projeto cita o DMG 2014 (dano por rodada, divisão livre) `[C, não conferido]` e o campo (`decisoes-fase-1.md` l.105-215) |
| 35 | **A trava de área:** 1 ação em área por rodada, 1 por esquadrão, e a `Recarga` fora da cota | peça 26 l.571-577 e l.625; livro 70 l.102-115 | — | peça 26 §6.5 | **Medido** (com 2 ações em área o alvo fica com `0,3%`) `[C]` |
| 36 | **A área natural por nível:** 13, 28, 50 e 113 quadrados, nas formas Esfera, Cone e Retângulo | peça 26 l.610-627; livro 70 l.34-100; `dados.js` l.122-127 | — | peça 26 §6.5 | **Medido:** cresce `9,00×`, como os dragões do D&D 2024 `[C]` |
| 37 | **O orçamento de feitiço = golpe ÷ 4,5**, e o `seco` abaixo de 3 pontos | peça 26 l.502-529; livro 60 l.231-277; livro 50 l.334-346 | A técnica do inimigo | peça 26 §6.5 e peça 19 §2.1 | Projeto (Fundamento). O "bloco seco" foi **medido** contra D&D e Draw Steel (`ESTADO` l.548-560) |
| 38 | **A aptidão na cota:** `1 PE = 5,14`, e erguer = `maior Classe × 5,14 ÷ 3` | peça 26 l.531-553 | — | peça 5 §4 e peça 11 §6.5 | Projeto |
| 39 | **A habilidade guardada, `1×` por luta, sai de graça** | peça 26 l.555-559 | — | peça 26 §6.5 | **Medido** |
| 40 | **A Expansão `×1,92` (= 1 ÷ 0,52)**; tabela `1,9 / 7,7 / 11,5 / 15,4`; gate nv 14 com refino 5; sem barreiras com refino 10; desvio de refino `×1,11` | peça 26 l.400-486; livro 50 l.185-236 | Aumenta o encontro, e **não se compensa** (v0.229) | peça 26 §6.4 | Projeto e medido |
| 41 | **A resistência:** pesos `60/30/10`; `×1,43 / 1,18 / 1,05 / 1,11`; imunidade `×2,50 / 1,43 / 1,11 / 1,25`; imunidade a condição `×1,20`; vulnerabilidade `×1,00` | peça 26 l.368-398; livro 50 l.146-183; `dados.js` l.94-100 | É vida escondida | peça 19 §4 | **Adaptado.** "Resistência corta metade" é **D&D literal** (SRD 5.1 p.97: *"damage of that type is halved"*) `[F]`. A conversão em vida efetiva cita a tabela de PV efetivos do DMG 2014 (peça 26 l.396) `[C, não conferido]`. **O peso é palpite** (peça 19 l.415) `[C]` |
| 42 | **A cura:** a da `Energia Reversa` = vida ÷ luta ÷ ações; a `Circulação` vira Reação; fator `L ÷ (1 − L·cura ÷ vida)` | peça 26 l.629-646 | — | peça 26 §6.5 | Projeto |
| 43 | **A parte destrutível = vida ÷ luta × 2 ÷ ações** | peça 26 l.648-672; livro 50 l.262-285 | — | peça 26 §6.5 | Projeto e medido |
| 44 | **As trocas ruins:** a cura empata em `315` (1/3 da vida); a condição empata quando `alvos × ações negadas = 4 × ações gastas` | peça 26 l.674-682 | — | peça 26 §6.5 | Projeto |
| 45 | **A cura do grupo:** a linha **não** desconta cura | peça 26 l.277-300 | — | peça 26 §4.7 | **Medido.** O molde de cura curta é o do d20 2024 `[C]` |
| 46 | **`Núcleos (N)`** reparte a vida, com fator `1,00` | livro 50 l.252-260 | — | cap. 5 | Decisão (`ESTADO` l.452-460) |
| 47 | **A linha de entradas nomeadas:** 6, e 8 no chefe de fim de arco | livro 50 l.317-332; livro 90 l.47 | — | cap. 5 | **Adaptado e medido:** D&D 2024 tem mediana de 4 em 234 blocos; Daggerheart, 5,4 (`ESTADO` l.1007) `[C]` |
| 48 | **O pacto:** o teto é a Essência ÷ 2 | peça 26 l.48; livro 50 l.238-246 | — | peça 22 §3 | Projeto |
| 49 | **O bloco:** ordem das linhas, cabeçalho, Traços, Ações, Intervenções, TR com rótulo | livro 50 l.7-39; `GUIA-bloco-5e.md` §1-9; `00-fase-0/decisoes.md` l.13-15; `make.js` l.163-204 | A forma | `GUIA-bloco-5e.md` | **D&D literal, declarado.** É o molde do MM 2014 (PT), do LdJ 2024 Ap. B e do Volo's; o alvo mandado foi o *Aboleth* do MM 2024 `[C]`. O que o SRD tem dele confere (p.259-260) `[F]` |

---

## 2. As dependências das cinco premissas

*Cada linha é algo que muda, ou fica errado, se a premissa mudar. Os validadores estão no §3.*

### 2.1 Premissa (i): `personagens = fator × 4`, e a linha do manual calibrada para 4

**Onde ela nasce.** `manual` l.168 diz *"A conta supõe quatro personagens"*. A peça 26 repete em l.178. A peça 24 l.132 chama a mesa de 4 de *"a premissa de todo preço do sistema"* `[C]`.

| o que depende | onde | como depende |
|---|---|---|
| a vida e o dano de cada categoria | peça 26 l.170-176 e l.184-192; livro 60 l.141-167 | a linha × o fator, e o fator = pessoas ÷ 4 |
| a vida do capanga | peça 26 l.180 e l.310; `manual` l.169 | = dano do grupo ÷ **4** (o que um personagem derruba num golpe) |
| o câmbio de 8 capangas | peça 26 l.302-317 | o grupo de 4 derruba 4 corpos por rodada, e a conta é `8 + 4` golpes |
| a sub-categoria | peça 26 l.208-227 | foi simulada contra a vida de **4** personagens (conferir 5.1 l.676) |
| o encontro misturado (`+0,083` por capanga) | livro 60 l.40-56; livro 90 l.65 | `0,083` = 1/12 do chefe, medido com o grupo de 4 |
| 4 Ameaças = 0,75 Desastre | peça 26 l.269 | a comparação é entre 4 corpos de 1 pessoa e 1 corpo de 4 |
| a derrubada `2,70` | peça 26 l.231-239 | a vida do alvo é a de 1 de 4 |
| a cura do grupo | peça 26 l.277-300 | as composições são de 4 |
| a condição que o inimigo põe | peça 26 l.680 | `alvos × ações negadas = **4** × ações gastas` |
| o preço da `Recarga` | peça 26 l.590-604 | a área pega **metade das pessoas** da categoria |
| a Expansão em pessoas | peça 26 l.409-418 | a tabela é `pessoas × 1,92` |
| a resistência em pessoas | peça 26 l.381 e l.390 | *"Desastre imune a Físicos exige `10`"* = 4 × 2,50 |
| a Circulação | peça 26 l.644 | *"Uma Ameaça com a Circulação exige 1,5 pessoa"* |
| a trava de área | peça 26 l.575 | *"com 2, o alvo termina a luta com 0,3%"*, medido contra 4 |
| o `Cisão` da peça 24 | peça 24 l.132 e l.230 | *"na mesa padrão de quatro a parte de cada um é um quarto"* |
| as convenções da régua de condição | peça 19 l.85 e l.103-104 | "contra um grupo de quatro"; o `Estampido` supõe mesa de quatro |
| as prontas | livro 80 l.232 e l.243; `dados.js` PRONTAS | "cada Desastre exige a mesa padrão de quatro"; a Tsuchigumo com 2 capangas "exige perto de cinco" |
| o texto do gerador | `make.js` l.224, l.411-412, l.419 e l.470 | "quantos personagens", "os quatro precisam", "exige 10 personagens" |
| a vida do grupo no validador | `conferir-bestiario.py` l.551-564 | é a média dos 5 Caminhos da peça 1 §5.1. ⚠ A tabela ainda lista o **Evocador**, que saiu da edição jogável na v0.270 (peça 1 l.197) `[C]` |

### 2.2 Premissa (ii): a escada de cinco, com a Calamidade de 8

| o que depende | onde |
|---|---|
| a tabela dona | peça 26 l.166-182 (a Calamidade de 8 em l.176, e *"a Calamidade de hoje exige oito"* em l.182) |
| as fichas por nível | peça 26 l.184-192; `TABELA.md` (uma seção por categoria, com 29 níveis); livro 60 l.141-182 |
| as tabelas **por categoria** da peça | papel (l.145-151); golpe em dado (l.251-257); orçamento de feitiço (l.511-520); aptidão (l.542-547, com as colunas Ameaça e Desastre); Expansão (l.413-418); Regravação (l.479-482); Recarga (l.599-604); Circulação (l.639-642); parte destrutível (l.662-664) |
| a cópia do gerador | `dados.js` l.30-36; `make.js` l.394-395 (*"a Catástrofe exige seis e a Calamidade exige oito feiticeiros"*) e l.411-412 |
| a cópia de entrada do livro | `bestiario/04-fase-1/TABELA.md`; `gerar-tabelas.py` l.31 (`CATS` fixo) e l.44-46 (morre se faltar seção) |
| o livro | 07 l.21-28; 50 l.193-201 e l.268-273; 60 l.14-23, l.85-94, l.141-154 e l.249-262; 70 l.130-138; 90 l.8-19 |
| o Sukuna | `bestiario/05-sukuna/O-SUKUNA-no-nivel-30.md` l.13 e l.34 (Calamidade); `montar-o-sukuna.py` l.724 |
| a peça 15 (Invocações) | peça 15 l.572-574: o golpe de cada categoria mede a morte do shikigami |
| as notas de história | `sistema/ESTADO-ATUAL.md` l.95 (*"a de oito entrou por cima"*) |
| ⚠ o nome | a Calamidade **morta** era de 6 pessoas e fator 1,50; a **viva** é de 8 e 2,00. Mesmo nome, `1,33×` mais (`ESTADO` l.110-112) `[C]` |

### 2.3 Premissa (iii): a luta de 3 rodadas

**Onde ela nasce.** `manual` l.171 diz que a vida do chefe é três vezes a saída do grupo, e por isso a luta dura três rodadas.
**Dentro da peça 26 ela tem duas âncoras:**
- l.379 (*"contra as `3,00` que a categoria promete"*), que quatro checagens leem;
- l.597 (*"Com a luta de `3` rodadas"*).

| o que depende | onde | conta |
|---|---|---|
| a vida de toda linha | `manual` l.155-166 | vida = 3 × saída (checagem 5.2) |
| o alcance do `Artilheiro` | peça 26 l.162 | *"uma rodada de três é a de aproximação"*, então `1/6` da saída |
| a derrubada `2,70` | peça 26 l.231-239 | 657 em 3 rodadas |
| o câmbio | peça 26 l.313-315 | `8 + 4` contra `3 × 3` |
| a cura do grupo | peça 26 l.283-288 | lutas de 3,00 / 4,00 / 6,00 |
| o `0,923` | peça 26 l.567; `MEDIDA-a-intervencao.md` l.402-404 | `0,75` ação extra numa luta de **3** rodadas |
| o gate da Expansão | peça 26 l.440 | a duração no nível 14 é 3 rodadas, *"contra a luta de `3,00`"* |
| a Regravação espalhada | peça 26 l.482 | *"espalhada na luta de `3,00`"* |
| erguer a anti-domínio | peça 26 l.538 | `maior Classe × 5,14 ÷ 3` |
| a habilidade guardada | peça 26 l.559 | 438 + 110 + 110 = 657 |
| a Recarga | peça 26 l.590-604 | 1,67 disparos em 3 rodadas; fator `[d·r + (L−d)] ÷ L` |
| a cura da Energia Reversa | peça 26 l.631 | vida ÷ **luta** ÷ ações |
| a Circulação | peça 26 l.637 | `L ÷ (1 − L·cura ÷ vida)` |
| a parte destrutível | peça 26 l.652 | vida ÷ **luta** × 2 ÷ ações |
| a cura que empata | peça 26 l.678 | `315` = 1/3 da vida |
| a condição da peça 19 | peça 19 l.106 | *"`44,05` espalhado numa luta de `3` rodadas"* |
| o livro | 50 l.223 (*"o domínio dele já dura a luta inteira"*), 50 l.265-277 (parte), 70 l.17 (*"pouco menos de duas vezes numa luta de três rodadas"*) | — |
| a fase | `a-escada-com-numero.md` l.126-128 | partir a vida dá as **mesmas 3 rodadas**: *"O botão de duração é quantas pessoas aparecem"* `[C]` |

### 2.4 Premissa (iv): as ações `1 · 1 · 3 · 5 · 6`

| o que depende | onde |
|---|---|
| o golpe = a rodada ÷ as ações | peça 26 l.243-265; livro 60 l.141-154; `make.js` l.104 |
| **o piso das 3 ações** (a régua de condição) | peça 19 l.85-100 (com 2 ações, Lento, Calado, Enfeitiçado e Atordoado passam do filtro de `3,00×`); peça 26 l.206 |
| o golpe do chefe em outras peças | `conferir-aptidoes.py` l.86 e l.103-108 (a RD da Reação e o empate da ER se medem contra UM golpe); `conferir-bloquear.py` l.341-350 (golpe = 219 ÷ 3); peça 15 l.567-605 (a morte do shikigami) |
| a banda do golpe, `21-28%` da vida de um personagem | `bestiario/04-fase-1/fila/DECIDIDO-o-capanga.md` §1 (é a dona); lida pela peça 26 l.586, pela peça 1 l.536 e pelo `conferir-atributos.py` l.846-860 |
| o papel | peça 26 l.145-151 e l.160-161; livro 60 l.85-96; `make.js` l.249-250. O ganho é `(N−1+1,476)÷N` ou `1+1÷N` |
| a Intervenção | peça 26 l.561-569: só de Desastre para cima; `×0,923` medido com 3 ações |
| as Ações Múltiplas | livro 50 l.299-302; `make.js` l.322; e o **texto** das prontas: `dados.js` l.175 e l.202, *"faz **três** ataques…"* |
| a parte destrutível | peça 26 l.652 e l.671 (a Ameaça fica de fora por ter 1 ação) |
| a Recarga | peça 26 l.593 (`÷ ações`) |
| o orçamento de feitiço | peça 26 l.508-520 (o golpe ÷ 4,5) |
| a condição posta pelo inimigo | peça 26 l.680 (ações gastas) |
| o esquadrão | peça 26 l.147 (o Capanga lê 8 ações) |
| o livro do jogador | `sistema/05-material/livro/manual/15-dano-e-condicoes.md` l.249: *"um chefe, um capanga grande — perde **uma** das suas ações"* |

### 2.5 Premissa (v): os traços que multiplicam o fator e passam de 6 pessoas

| traço | multiplicador | onde | o que depende |
|---|---|---|---|
| Expansão completa ou sem barreiras | `×1,92` | peça 26 l.400-461; livro 50 l.185-215 | a tabela `7,7 / 11,5 / 15,4`; o gate no nível 14 (iii); o desvio de refino `×1,11`; a decisão *"não se compensa"* (l.430-434) e a guarda contra *"manter o tamanho"* (conferir 7.1b l.952) |
| Recarga | `×1,14 / 1,37 / 1,28 / 1,37` | peça 26 l.590-606; livro 70 l.130-138 | (i), (ii), (iii) e (iv) ao mesmo tempo |
| Resistência e imunidade | `×1,05 … ×2,50` | peça 26 l.368-398; livro 50 l.146-183; `dados.js` l.94-100 | os pesos `60/30/10` da peça 19 §4, que são **palpite** (peça 19 l.415) |
| Imunidade a condição | `×1,20` | peça 26 l.386-388 | o `Calado` da v0.277 (peça 19 §3.2; `conferir-dano.py` l.1444) |
| A cura de Reação da Circulação | `×1,04 … ×1,49` | peça 26 l.637-646 | (iii) |
| A Destreza abaixo da tabela | `×0,833` | só no Sukuna (`O-SUKUNA-no-nivel-30.md` l.19 e l.84: *"A peça 26 não tem essa regra"*) `[C]` | — |
| **O Sukuna** | `8 × 1,92 × 1,37 × 1,049 × 0,833 = 18,4` | `O-SUKUNA-no-nivel-30.md` l.13; `SAIDA-o-sukuna-nv30.txt` l.221-225; `montar-o-sukuna.py` l.724-830 | as cinco premissas juntas. Conferi a conta e dá `18,39` `[I]` |

**O que segura esses multiplicadores hoje é só a palavra.** A peça 26 diz *"É aviso, e não trava"* (l.390; e l.644 para a Circulação). Diz também que *"a categoria mede pessoas, e o número existe fora da escada"* (l.420) `[C]`.

---

## 3. O que encoda cada premissa

### 3.1 Os validadores, checagem por checagem

| validador · checagem | (i) × 4 | (ii) escada | (iii) 3 rodadas | (iv) ações | (v) traços |
|---|---|---|---|---|---|
| `conferir-bestiario` **3** (l.363-450) | ✔ `fator = pessoas/4` (l.432) | ✔ exatamente 5 categorias (l.374), e 1 sem pessoas (l.378) | | | |
| **4** (l.506-529) | ✔ a categoria de fator 1,00 tem de ser 4 (l.520) | | | ✔ as ações dela = o piso da peça 19 (l.523) | |
| **5** (l.600-645) | ✔ capanga = grupo ÷ 4 (l.606-607) | | ✔ a simulação usa a saída do grupo | ✔ | |
| **5.1** (l.648-676) | ✔ grupo = 4 × a vida de um personagem (l.676) | | ✔ | | |
| **5.2** (l.678-743) | | | ✔ **cada linha do manual tem de sair em 3 rodadas inteiras** (l.731-733) | | |
| **7.1** (l.807-860) | ✔ | ✔ a tabela = as pessoas de cada categoria × 1,92 (l.843-856) | | | ✔ |
| **7.1b** (l.874-962) | | | ✔ lê a luta de 3,00 (l.882); o domínio tem de durar a luta (l.915) | | ✔ guarda l.952 |
| **8** (l.968-1040) | | ✔ | | | ✔ |
| **9.1** (l.1102-1194) | | ✔ 7 × 5 = 35 células (l.1192) | | ✔ golpe ÷ ações (l.1174-1177) | |
| **9.2** (l.1196-1283) | | ✔ colunas Ameaça e Desastre | ✔ erguer ÷ `_DUR` (l.1270) | | |
| **9.3** (l.1285-1346) | ✔ `_GRUPO` = 4 (l.1334) | | ✔ a cura = vida ÷ 3 (l.1307) | | |
| **9.5** (l.1372-1580) | ✔ `_MESA` = 4 (l.1408); **uma pronta não passa de 4** (l.1476-1478) | ✔ | | ✔ Ações Múltiplas (l.1479); 3 Intervenções (l.1485) | |
| **9.7** (l.1631-1750) | ✔ pessoas × ½ (l.1707) | ✔ | ✔ L = 3 (l.1686), e confere com a peça (l.1689-1691) | ✔ | ✔ |
| **9.8** (l.1753-1933) | | ✔ | ✔ luta (l.1773, l.1826) e cura `L÷(1−L·c/v)` (l.1896) | | ✔ |
| **9.9** (l.1935-2019) | | ✔ | ✔ luta (l.1945) | ✔ a Ameaça fica de fora por ter 1 ação (l.1973) | |
| **10.2 / 10.3** (l.2021-2215) | | ✔ | | ✔ as ações do §3.4 = as do §4; o Capanga = 8 (l.2206) | |
| `conferir-ficha` **7a** (l.478-501) | ✔ | ✔ `dados.js` == §4, **inclusive o 8** | | ✔ | |
| `conferir-ficha` **7b / 7b-bis** (l.504-567) | ✔ capanga = grupo ÷ 4 | ✔ | | | |
| `conferir-ficha` **7c / 7c-ter** (l.569-776) | | | | ✔ `ACOES_ESQUADRAO`, `MULT_VANTAGEM`, 3 Intervenções, teto 3 | ✔ `RESISTENCIA` |
| `conferir-dano` **12** (l.1234-~1320) | | | | ✔ **o 3 é piso da régua de condição** | |
| `conferir-dano` l.1444 | | | | | ✔ o Calado não paga `1,20` |
| `conferir-aptidoes` l.86-108 | ✔ `CHEFE` copiado do manual | | | ✔ ações lidas da peça 19 | |
| `conferir-bloquear` l.335-350 | | | | ✔ golpe = 219 ÷ 3 | |
| `conferir-alma` **13c** (l.674-700) | ✔ lê `personagens = fator × N` como a mesa padrão do `Cisão` | | | | |
| `conferir-atributos` l.846-860 | | | | ✔ a banda do golpe | |
| `conferir-invocacoes` **12b** (l.1256-1285) | | ✔ lê as tabelas §4.1 e §4 | | ✔ golpe = dano ÷ ações | |

**Nenhum validador põe teto de 6 pessoas.** O contra-teste coerente da checagem 3 (Calamidade 8 → 10) fica verde (peça 26 l.759, l.789 e l.793). A 9.5 é a única que limita, e só as prontas, a 4 `[C]`.

### 3.2 O gerador de inimigo (`sistema/05-material/gerador-inimigo/`)

| parte | premissas | o que quebra |
|---|---|---|
| `dados.js` `CATEGORIAS` (l.30-36) | (i) (ii) (iv) | a cópia da escada; o 7a compara com a peça **célula a célula** |
| `dados.js` `FAIXAS` (l.15-24) | (i) (iii) | a cópia da linha do manual e do capanga (grupo ÷ 4) |
| `dados.js` `SUBCATEGORIAS`, `CAMBIO = 8`, `AMEACA_CONTRA_DESASTRE`, `TETO_EMPILHAMENTO` (l.107-110 e l.208-211) | (i) (iii) | todos são medidos com a mesa de 4 e a luta de 3 |
| `dados.js` `FATOR_INTERVENCAO = 0.923`, `INTERVENCOES = 3` (l.73-74) | (iii) (iv) | — |
| `dados.js` `PRONTAS` (l.150-205) | (ii) (iv) | a `categoria:` de cada pronta tem de existir; o **texto** *"faz três ataques"* (l.175 e l.202) não é conferido contra o número de ações — o `make.js` l.322 e a 9.5 l.1479 só olham se a entrada existe `[I]` |
| `make.js` `danoDaRodada`, `golpe`, `golpeCru` (l.100-106) | (i) (iv) | o golpe e o orçamento |
| `make.js` `fatorPapel` (l.241-252) | (iv) | o papel lê as ações |
| `make.js` `montaPronta` (l.254-329) | (iv) | lança erro se as Ações Múltiplas não baterem ou se as Intervenções ≠ 3 (l.322-327) |
| `make.js` textos (l.224, l.394-395, l.411-412, l.419, l.470) | (i) (ii) (v) | a folha imprime *"Calamidade é oito"* e *"exige 10 personagens"* |

### 3.3 O livro de inimigos (`bestiario/08-livro/`)

| capítulo | premissas | gerado por |
|---|---|---|
| 07 vocabulário | (i) (ii) | à mão |
| 50 o bloco | (i) (ii) (iii) (iv) (v) | a tabela de atributos vem do `gerar-atributos.py` (TABELA.md + peça 26); o resto é à mão |
| 60 a montagem | (i) (ii) (iii) (iv) | tabelas, orçamento e pagamento vêm do `gerar-tabelas.py` (TABELA.md + RASCUNHO-5 + peça 26 §3.4 + `make.js`); o exemplo vem do `gerar-exemplo.py`; o encontro misturado é à mão |
| 70 área e frequência | (ii) (iii) (iv) (v) | à mão |
| 80 as seis maldições | (i) (ii) (iv) | as fichas vêm do `gerar-as-seis.py`, pelo `dados.js` via node |
| 90 referência | (i) (ii) (v) | à mão |
| 05, 10, 20, 30 e 40 | nenhuma premissa numérica | — (só o 10 l.197 fala do esquadrão de oito) |

A 9.5 roda os quatro `gerar-*.py` com `--conferir` (`conferir-bestiario.py` l.1561-1567). O que é gerado acende; **o que foi escrito à mão não acende** `[I]`.

### 3.4 As seis maldições prontas

| pronta | categoria · papel · faixa | (i) × 4 | (ii) escada | (iii) 3 rodadas | (iv) ações | (v) traços |
|---|---|---|---|---|---|---|
| Betobeto | Ameaça · Emboscador · 2-4 | vida `19` = 28 × 0,677 | a categoria tem de existir | via a linha | Emboscador `×0,677` (1 ação) | nenhuma célula preenchida |
| Kamaitachi (×2) | Ameaça · Emboscador · 2-4 | 2 corpos = `−25%`, o `0,75×` do §4.3 (`ESTADO` l.133-134) | idem | idem | idem | — |
| Hitotsume | Ameaça · Emboscador · 5-8 | vida `46` | idem | idem | idem | — |
| Kitsune | Ameaça · Artilheiro · 9-12 | vida `84`; **a técnica `4d8`** sai do golpe da Ameaça (4,2 pontos) | idem | idem | golpe = rodada ÷ 1 | — |
| Tsuchigumo | Desastre · Controlador · 2-4 | vida `85` = 114 × 0,75 | idem | idem | **Controlador `×0,75` = 1÷(1+1/3)**; texto *"três ataques"*; 3 Intervenções; `0,923` | — |
| Oni | Desastre · Brutamontes · 5-8 | vida `324` = 270 × 1,20 | idem | idem | texto *"três ataques"*; 3 Intervenções; `0,923` | — |

**Nenhuma pronta usa Catástrofe, Calamidade, Recarga, Expansão, resistência ou parte destrutível.** O livro diz isso em 80 l.9-15, e o `GUIA-bloco-5e.md` em l.90-91 `[C]`.
**Há um precedente de quebra.** Na troca de escada da v0.221, 0 das 6 prontas ficaram em categoria viva, e ficaram assim num `.docx` publicado (`ESTADO` l.72-93) `[C]`.
**Se a Ameaça virar sub-categoria**, as quatro Ameaças mudam de rótulo e talvez de ações. A Kitsune só conjura porque a Ameaça de 9-12 tem 4,2 pontos (`ESTADO` l.120-134).

### 3.5 Os scripts de medição, fora da bateria

Cerca de 30 arquivos leem a peça 26 com regex:
- os `bestiario/04-fase-1/fila/*.py` (cerca de 25);
- `papel/construir-os-cambios.py`;
- `sobrecarga/medir-a-metade-morta.py`;
- `06-playtest/montar-as-tres-fichas.py`;
- `05-sukuna/montar-o-sukuna.py`;
- os `ferramentas-claude-2/*.py`;
- `manual/matematica/sobrecarga.py` (l.64 lê *"O inimigo não conta PE"*);
- `manual/matematica/casca-sem-barreira.py` (l.70).

A fila tinha 43 âncoras em 11/09 (`ESTADO` l.20-22) `[C]`. Um redesenho que mude a forma das tabelas faz esses scripts morrerem com `ÂNCORA PERDIDA`, que é o comportamento desenhado `[I]`.

---

## 4. O "duro": o que ficou rígido e de onde veio

**Antes da lista, o que a fonte diz.** A queixa não é nova:
- em 08/09 o Mizuki já tinha dito *"tava tudo bom honestamente, mas a montagem n parecia boa, ent acho q o problema é o esqueleto"* (`03-bloco/o-esqueleto-e-o-problema.md` l.5) `[C]`;
- em 27/09 ele inverteu o diagnóstico: *"temos um esqueleto bom, mas não funcional"*, e os valores precisam ser rebalanceados.

A fase 0 fixou os números e mexeu na forma (`00-fase-0/decisoes.md` l.17-21). **Hoje a queixa pega nos dois**, e por isso separei forma de número.

**Sobre as colunas das tabelas abaixo.** A coluna "por que parece duro na mesa" é inferência minha `[I]`, a não ser onde há citação. A coluna "o que foi medido" traz só o que o repositório registra.

### 4.1 Forma: o bloco no molde do 5e

| # | o que está rígido | veio de | por que parece duro na mesa | o que foi medido |
|---|---|---|---|---|
| F1 | **O bloco vertical do 5e carrega a ficha inteira de personagem.** São ~19 linhas derivadas: Defesa, Acerto, CD, Refino com a proteção, Vida e Integridade, 5 atributos, 4 TRs, resistências e o pacto (livro 50 l.9-39) | **D&D literal na forma** (`GUIA-bloco-5e.md`; fase 0 l.13-15, o alvo é o *Aboleth* do MM 2024) `[C]` + **projeto no conteúdo** (peça 26 l.11) | O bloco do 5e é **fachada**: o monstro nasce de uma tabela própria, e o bloco só mostra o resultado. O projeto registra a frase do campo, *"5E Monster stat blocks do not have simulationist transparency with PC abilities"* (`decisoes-fase-1.md` l.213-215) `[C]`. Aqui cada célula da fachada tem dono na regra do jogador. O mestre não mexe numa sem quebrar outra: se a Destreza sai da curva, o `make.js` lança erro (l.286-288) e a 9.5 acende | A moldura vazia gastava 90 a 110 palavras, contra a mediana de 249 do bloco do D&D (`ESTADO` l.1007). O Sukuna tem 9 entradas e passa da linha de 8 (`O-SUKUNA` l.82) |
| F2 | **Um golpe só por categoria, em toda ação.** A área da pronta bate o mesmo número do ataque simples: Varrida das Patas = Mordida, Pancada no Chão = Kanabō, Choro = Garra (livro 80 l.108-110 e l.214-216; livro 60 l.218-220) | `Multiattack` é **D&D literal** (SRD 5.1 p.259) `[F]`. O "golpe único" é **projeto**: *"Aqui a divisão não é livre: ela é o número de ações da categoria"* (peça 26 l.249) `[C]` | Toda ação rola o mesmo dado, e a variedade fica só no texto. No 5e o *Multiattack* mistura ataques de números diferentes (o dragão faz "um com sua mordida e dois com suas garras", `GUIA` l.40-41, citando o MM 2014 p.118) `[C]` | A área por alvo (`0,60×`) cai dentro do campo, que vai de `0,56` a `0,76×` em 7 sistemas (`ESTADO` l.864-866). Na mesa de 07/09, o mestre **dobrou dados e modificador** num golpe especial em vez de bater mais vezes (`mesa-nd20.md` l.61-69) `[C]`. Isso virou a `Recarga` |
| F3 | **Sempre 3 Intervenções, sempre no molde "1ª bate e 2ª e 3ª mudam o campo"**, e a 1ª é *"o ataque sem a metade no vizinho"* (livro 50 l.304-315; livro 80 l.116-120 e l.222-226). A Ameaça não tem nenhuma | **Adaptado:** a Ação Lendária do SRD 5.1 (p.260) `[F]` + a Villain Action do Draw Steel (`ESTADO` l.834-837) `[C]`. **Travado:** o `make.js` l.325-327 e a 9.5 l.1485 exigem exatamente 3 | Um Desastre de nível 2 e o Sukuna têm o mesmo número e o mesmo molde de Intervenção. No SRD o número de Ações Lendárias é do monstro (o Aboleth tem 3), e aqui é da categoria. Um chefe solo de 1 pessoa (Ameaça) não tem ação fora do turno | 9 villain actions de 3 Solos do Draw Steel: 4 de 9 com dano zero (`ESTADO` l.834-837) |
| F4 | **Duas escadas, a faixa de Classe e o marco.** A pronta que cruza marco imprime duas ou três linhas de Defesa e atributos com parêntese — "`3` (`4` do nível 10)" (livro 80 l.132-138, l.162-168 e l.194-200) | **Projeto.** O manual trabalha por faixa, e as derivadas andam por marco (`COMO-USAR.txt` l.58-63) | O bloco de uma faixa de níveis fica parecendo planilha. No 5e cada estatística ocupa uma linha | Até a v0.220 o bloco imprimia a linha errada (`COMO-USAR.txt` l.61-63) `[C]` |
| F5 | **Células vazias sempre impressas:** *"Resistências — · Imunidades — · Vulnerabilidades — · Perícias —"* e os 4 TRs com "—" (livro 80 l.40 e seguintes; `make.js` l.362) | **Desvio declarado do 5e.** O `GUIA` l.31-32 registra que no 5e *"linha que não tem conteúdo some"*, e o livro 80 l.9-10 explica que as células saem vazias porque preencher custa fator `[C]` | O bloco lê como formulário. As células vazias estão ali para mostrar preço, e não conteúdo | — |
| F6 | **O rótulo da categoria no cabeçalho é um número de pessoas** (livro 50 l.49-50) | **Projeto** (a ideia é do Mizuki). A fase 0 escolheu nome de **gravidade** para não obrigar o leitor a converter (`00-fase-0/decisoes.md` l.45-49) `[C]` | O nome diz gravidade e a tabela diz pessoas. Uma Calamidade "exige oito, e nenhuma mesa tem oito" (livro 07 l.28): o rótulo do topo nasce impossível de jogar | Rodadas por tamanho de mesa, no nível 30: a Calamidade dura **6** rodadas contra 4 pessoas e **4** contra 6 (`a-escada-com-numero.md` l.106-110) `[C]` |

### 4.2 Número: as fórmulas

| # | o que está rígido | veio de | por que parece duro na mesa | o que foi medido |
|---|---|---|---|---|
| N1 | **"A ficha de inimigo é a ficha de personagem sem o Caminho"** (peça 26 l.11). As derivadas e o orçamento de atributo obrigam os atributos a reproduzir a tabela. No nível 20, a Defesa e o acerto comem 10 dos 15 pontos (livro 50 l.97-106) | **Projeto, e é o contrário do D&D.** `a-escala-do-inimigo.md` l.9-11: *"O D&D não faz isso, e nunca fez"* `[C]`. Só a CD copia uma fórmula de personagem do D&D (SRD 5.1 p.16) `[F]` | Os pontos *"compram cor, e não tamanho"* (livro 50 l.94). Não dá para fazer um chefe mais preciso ou mais duro pelos atributos. Todo desvio vira traço com causa (`o-esqueleto` l.36) e paga no fator. O Sukuna precisou de exceção: *"Rei das Maldições: +4 pontos"* e Destreza 4 com `×0,833`, *"A peça 26 não tem essa regra"* (`O-SUKUNA` l.18-19 e l.84) `[C]` | **Na mesa de 07/09:** *"a galera tinha seus 9 de acerto, ent... ter 18 de defesa n é lá uma média boa pra um inimigo de final de arco"*, e o chefe ficou **mais fácil de acertar que um PJ bem montado** (`mesa-nd20.md` l.45-59) `[C]`. **Medido contra o MM 2014:** a Defesa não se separa com o ND, e isso levou à decisão de não subir a Defesa (`a-escala` l.30-37; `o-esqueleto` l.11-12). **Para montar uma ficha, o mestre cruza 12 peças mais o manual** (`a-escala` l.44-46) `[C]` |
| N2 | **Um fator só para vida e dano** (peça 26 l.170-176). O papel mexe na vida ou na Defesa e **nunca no dano**: *"Nenhum dos seis sobe o dano por rodada"* (peça 26 l.141) | **Projeto.** O fator duplo, no molde do Draw Steel, foi tentado e morreu (`a-escada-com-numero.md` l.29-39) `[C]` | O "tanque fraco" e o "canhão de vidro" não existem, a não ser pelo papel (±20% de vida ou ±2 de Defesa) | **O teste do Sukuna:** vida `1,03×` e dano `2,66×` a montagem do Mizuki, que *"amarrou a vida na Calamidade e o dano em 0,75× do Desastre, e na máquina isso não é montagem legal"* (`ESTADO` l.843-846) `[C]` |
| N3 | **Luta de 3 rodadas, gravada em toda conta** (§2.3). A 5.2 exige que cada linha do manual saia em 3 rodadas **inteiras**, e 1 PV vale 1 rodada (§5.1) | **Adaptado.** O projeto cita o DMG 2014 (média das 3 primeiras rodadas) `[C, não conferido]` | O único botão de duração é quantas pessoas aparecem (`a-escada` l.128). Chefe em fases dá as mesmas 3 rodadas (l.126-128). O mestre que quer uma luta de 5 rodadas contra 4 pessoas precisa de uma categoria "de 6,7 pessoas" | 2,70 derrubadas contra o d20 2014 e o PF2e (peça 26 l.237); cura do grupo (l.279-300); na mesa, o mestre **ajustou o dano durante a luta**, e isso ficou registrado como requisito (`mesa-nd20.md` l.79-81) `[C]` |
| N4 | **Ações `1·1·3·5·6`, com o golpe = rodada ÷ ações.** O golpe da Calamidade é **igual** ao do Desastre, e o da Catástrofe é **menor**: no nível 26-30, `6d10+34` / `7d8+29` / `6d10+34` (livro 60 l.152) `[C]` | O `3` vem da frase do manual e do **piso medido** da peça 19. O `5` e o `6` são **declarados** (peça 26 l.202-203) `[C]` | Subir de categoria dá **mais ações do mesmo golpe**. A Calamidade é, na conta, dois Desastres num corpo: 2× a vida, 2× as ações e o mesmo golpe `[I]`. A Ameaça, com 1 ação, fica sem Intervenção, sem parte destrutível e paga o Controlador a `×0,5` | Na mesa: *"Ele NÃO quis mais ações. Quis um golpe maior e com trava"* (`mesa-nd20.md` l.61-69) `[C]`. **A escada responde com mais ações** |
| N5 | **O `0,923` é o mesmo nas três categorias com Intervenção** (peça 26 l.565; livro 60 l.27) | Medido **com 3 ações** (`MEDIDA-a-intervencao.md` l.395-445). A própria medida diz que *"O fator não é uniforme"* (l.355-357) `[C]` | Conta minha, pela mesma forma (0,75 ação extra na luta): Catástrofe `15/15,75 = 0,952`; Calamidade `18/18,75 = 0,960`. Com o `0,923` as duas pagam 3 a 4% a mais do que a forma medida pede `[I]` | — |
| N6 | **O piso `seco`:** abaixo de 3 pontos de feitiço a ação não monta técnica. É o caso de toda Ameaça do nível 2 ao 8 e de todo Capanga até o 8 (livro 50 l.334-346) | **Projeto** (a Classe 1 custa 3 pontos, pela peça 19 §2.1) | Num jogo de feiticeiro, o inimigo de nível baixo não tem técnica e vira "um ataque e um traço" | O campo: mediana de 1 ação + 1 traço passivo em 276 blocos de CR 0-1 e 437 do Draw Steel (`ESTADO` l.548-560) `[C]` |
| N7 | **Toda célula de resistência cobra**, até um tipo só (`×1,11`), e a imunidade a Físicos leva a `×2,50`, ou 10 pessoas (peça 26 l.370-390) | Resistência = metade é **D&D literal** (SRD 5.1 p.97) `[F]`. O preço por vida efetiva é **adaptado** do DMG 2014 (peça 26 l.396) `[C, não conferido]`. **Os pesos `60/30/10` são palpite** (peça 19 l.415) `[C]` | As prontas saem todas com as células vazias. O sabor mais comum do monstro de D&D, uma resistência ou uma imunidade, aqui sempre custa | MM 2014: imunidade em 79% a 92% dos blocos de ND 11+; o DMG só cobra a partir de 3 ou mais tipos (`decisoes-fase-1.md` l.75-86) `[C, cita o DMG]` |
| N8 | **A categoria mede pessoas de forma linear** (`fator × 4`), e o próprio projeto mediu que o encontro **não** é linear | **Projeto** | "Somar fator" erra: 4 Ameaças = `0,75×` um Desastre (peça 26 l.269); o capanga toma 1/12 do chefe até 3 corpos e ~1/6 do 4º ao 7º (l.221); a soma ingênua do encontro misturado erra 28,6% a 71,4% (`ESTADO` l.607-611) `[C]` | Tudo isso está medido, mas a unidade de venda continua sendo a pessoa linear |

**O que não é duro, pelo que foi medido.** O tamanho não cobra nada, medido em 4.791 fichas do PF2e e 331 do D&D. O papel fecha em `1,000` e bate com o Draw Steel a menos de 4%. A área natural cresce como os dragões. A CD tem aval de mesa. Esses pontos têm medida a favor e não aparecem em queixa nenhuma `[C]`.

### 4.3 Resumo da origem do "duro"

| camada | veio do D&D ao pé da letra | veio do projeto |
|---|---|---|
| forma | a ordem do bloco, `Ações Múltiplas`, `média (dados)`, a `Recarga 5-6`, a grade de tamanho, o TR com rótulo de 2024, a Ação Lendária virando Intervenção | as 19 linhas derivadas no bloco, o golpe único, as 3 Intervenções fixas, as duas escadas no bloco, as células vazias impressas |
| número | a mesa de 4 do ND, a CD `8 + prof + atributo` do personagem, a resistência pela metade, o d6 da recarga; e, **pela citação do projeto, sem conferir**, as 3 rodadas, a área = 2 alvos e os PV efetivos do DMG 2014 | o inimigo = personagem sem Caminho, o fator único, a luta de 3 como trava de toda conta, as ações declaradas, o 0,923 uniforme, o seco, a cobrança de toda resistência, a pessoa linear |

### 4.4 As divergências internas achadas nesta leitura

| # | o quê | lado A | lado B | marca |
|---|---|---|---|---|
| 1 | **O encontro misturado** | livro 60 l.40-56 e livro 90 l.65: `fator + capangas × 0,083`, "até quatro". A tabela junta *"ele fica com 91,5%"* e *"o encontro exige 4,33"*. O livro 80 l.243 diz que a Tsuchigumo com 2 capangas *"exige perto de cinco"* | peça 26 l.210-222: com o chefe a 91,5%, o encontro com 1 capanga **cobra o mesmo** que o chefe sozinho, e *"A tabela para em três de propósito"*. O `make.js` l.444-452 diz *"As quatro formas cobram o mesmo"* | `[C vs C]` |
| 2 | **O `Controlador`** | livro 07 l.43: *"troca **dano** por uma ação negada"* | peça 26 l.126 e livro 60 l.71: paga em **vida**. A forma que pagava em dano morreu (peça 26 l.141-143) | `[C vs C]` |
| 3 | **Regra de papel sem dono** | livro 60 l.109-110: *"O Emboscador não sobe de Grande. O Baluarte e o Reforço só se pagam com mais de um inimigo"* | a peça 26 não tem nenhuma das duas; o livro diz que nenhuma `REGRA` nasce nele (05 l.15-16) | `[C vs C]` |
| 4 | **O capanga morto na peça 19** | peça 19 l.72: *"chefe e capanga no nível 30 · `219` e `73` · manual"*; repetido em l.542 e l.642 | o manual publica o capanga de **55** (`manual` l.164). O 73 = 219÷3 era o capanga da Alcateia | `[C vs C]` |
| 5 | **O `0,923` uniforme** | peça 26 l.565 | foi medido para 3 ações, e a medida diz que não é uniforme (`MEDIDA-a-intervencao.md` l.355-357) | `[C]` + conta `[I]` |
| 6 | **A Calamidade: "mais que 6" ou 8** | `decisoes-fase-1.md` l.13; `a-escada-com-numero.md` l.90 e l.100 | peça 26 l.176 e l.182; livro 07 l.28; livro 60 l.23; `dados.js` l.35 | `[C vs C]` |
| 7 | **O Evocador na vida do grupo** | peça 1 l.197 lista 5 Caminhos, com o Evocador | o Evocador saiu da edição jogável na v0.270 (commit `ca1e86f`). O `conferir-bestiario` l.551-564 tira a média dos 5 | `[C]`; se isso invalida a vida do grupo é `[I]` |
| 8 | **O golpe sem o `0,923` em três lugares** | peça 26 §4.4 l.251-257 (declara em l.259); `TABELA.md` (`8d8 + 37`); peça 15 l.573 (*"o maior golpe da tabela · `8d8 + 37`"*) | o livro 60 l.152 imprime `6d10 + 34` para o Desastre do 26-30 | `[C]` |
| 9 | **O preço da resistência** | `decisoes-fase-1.md` §7 l.88-95: resistir a 1 ou 2 tipos não custa nada; imunidade a um grupo inteiro só com porta de saída | peça 26 l.370-390: um tipo só custa `×1,11`, e a imunidade a Físicos é *"liberada"*, com aviso | `[C vs C]`. Pode ter sido superada por um `DECIDIDO` que não li `[I]` |
| 10 | **Decisões da fase 0 revertidas sem aviso** | `00-fase-0/decisoes.md` l.73-81 (*"Sem eixo de papel"*) e l.113 (*"a sub-categoria morre"*) | as duas estão vivas: peça 26 §3.4 e §4.5 (`ESTADO` l.617-624 e l.823) | `[C vs C]` |
| 11 | **A ficha do Sukuna no nível 30** | `O-SUKUNA-no-nivel-30.md` l.76: a Extensão *"anulado até Classe 4 … até 10 rodadas"* | a v0.273 reescreveu a Extensão: imune a tudo da Expansão, `1/3 do refino + 1`, `1,5 ×` a maior Classe por rodada (commit `2a2e4b6`) | `[C]`; a ficha está defasada `[I]` |

---

## 5. Toda menção a exigir mais de 6 pessoas

### 5.1 Regra viva e tabela viva

| arquivo:linha | o texto | o número |
|---|---|---|
| peça 26 l.176 | tabela §4: `Calamidade · 8 · × 2,00 · 6` | 8 |
| peça 26 l.178 | *"Um inimigo de fator `1,92` exige `7,7` pessoas"* | 7,7 |
| peça 26 l.182 | *"a `Calamidade` de hoje exige oito"* | 8 |
| peça 26 l.381 e l.384 | resistência e imunidade: *"o resultado é um número de pessoas, não um nome"* | até 10 |
| peça 26 l.390 | *"Um `Desastre` imune a `Físicos` exige `10` personagens, não `4`. […] É aviso, e não trava."* | 10 |
| peça 26 l.416-418 | tabela da Expansão: Desastre `7,7`, Catástrofe `11,5`, Calamidade `15,4` | 7,7 / 11,5 / 15,4 |
| peça 26 l.420 | *"a categoria mede pessoas, e o número existe fora da escada"* | — |
| peça 26 l.424 | *"Uma `Calamidade` com Expansão exige **`15,4`** feiticeiros. […] contra isso o grupo não ganha — ele foge, ou traz gente."* | 15,4 |
| peça 26 l.430-432 | decisão v0.229: a Expansão aumenta o encontro e não se compensa | — |
| peça 26 l.603-604 | tabela da Recarga: Catástrofe `6`, Calamidade `8` pessoas (com Recarga, `×1,37`, dá `11` pessoas pela conta `[I]`) | 8 |
| livro 07 l.28 | *"`Calamidade` · exige oito, e nenhuma mesa tem oito"* | 8 |
| livro 50 l.177-178 | *"Um `Desastre` imune a `Físicos` exige dez personagens, e não quatro."* | 10 |
| livro 50 l.199-201 | tabela da Expansão: `7,7 / 11,5 / 15,4` | — |
| livro 50 l.203-204 | *"Uma `Calamidade` com Expansão exige `15,4` feiticeiros — é por isso que ninguém enfrenta esse chefe com quatro."* | 15,4 |
| livro 60 l.12 | *"Um bicho de fator `1,92` exige `7,7` pessoas."* | 7,7 |
| livro 60 l.23 | tabela de categorias: `Calamidade · 8` | 8 |
| livro 70 l.135-138 | preço da Recarga: Calamidade `×1,37`, implícito sobre as 8 | (11) `[I]` |
| livro 90 l.61 | *"Um bicho de fator `2,50` exige dez pessoas."* | 10 |
| `dados.js` l.35 | `['Calamidade', 8, 2.00, 6, true]` | 8 |
| `make.js` l.394-395 (impresso no `bloco-de-inimigo.docx`) | *"as categorias acima dela ficam de fora das prontas: a Catástrofe exige seis e a Calamidade exige oito feiticeiros. […] se a sua mesa for grande"* | 8 |
| `make.js` l.411-412 (impresso) | *"quantos personagens este inimigo exige? […] `Calamidade` é oito"* | 8 |
| `make.js` l.470 (impresso) | *"Um `Desastre` imune a `Físicos` exige `10` personagens"* | 10 |

### 5.2 Trabalho, histórico e perturbação

| arquivo:linha | o texto | natureza |
|---|---|---|
| `bestiario/05-sukuna/O-SUKUNA-no-nivel-30.md` l.13 | *"o encontro · `8` pessoas · **`18,4` pessoas** · `8 × 1,92 × 1,37 × 1,049 × 0,833`"* | ficha de teste |
| `bestiario/05-sukuna/SAIDA-o-sukuna-nv30.txt` l.225 | `o encontro 8 × 1.92 × 1.37 × 1.049 × 0.833 = 18.4 pessoas` | saída de script |
| `bestiario/05-sukuna/montar-o-sukuna.py` l.724, l.735, l.774, l.824 e l.830 | calcula `ENCONTRO_FINAL` | script |
| `bestiario/04-fase-1/ESTADO-onde-paramos.md` l.110-112 | *"a viva é `8` / `2,00`. Mesmo nome, `1,33×` mais"* | registro |
| `ESTADO-onde-paramos.md` l.607-611 | *"`1 Desastre + 8 Capangas` · `7,00` pessoas"* | medida do encontro misturado |
| `bestiario/04-fase-1/a-escada-com-numero.md` l.39 | tabela "fator duplo" (morta): Calamidade `8` | histórico |
| `a-escada-com-numero.md` l.106-110 | rodadas da Calamidade contra 3, 4, 5 e 6 pessoas (8,0 / 6,0 / 4,8 / 4,0) | medida |
| `bestiario/08-livro/LEIA-ME-o-livro.md` l.87 e l.183 | cita *"exige dez personagens, e não quatro"* como frase de regra que fica | meta do livro |
| `sistema/ESTADO-ATUAL.md` l.95 | *"a `Calamidade` de seis virou `Catástrofe`, a de oito entrou por cima"* | estado |
| `sistema/ESTADO-ATUAL.md` l.145 | *"uma `Calamidade` com Expansão exige **doze** feiticeiros"* (marcado como escada morta) | histórico |
| peça 26 l.759 | contra-teste: *"Trocar a `Calamidade` para oito personagens"* (7 ações) | perturbação |
| peça 26 l.789 e l.793 | contra-teste: *"a `Calamidade` vira `10` pessoas"* | perturbação |

### 5.3 O que *não* passa de 6, mas chega no teto

- a Catástrofe, `6` (*"a mesa cheia"*): peça 26 l.175; livro 07 l.27; livro 60 l.22;
- o Desastre com 3 capangas, `5,00`: livro 60 l.56;
- o Desastre resistente a Físicos, `5,7`: peça 26 l.381.

**A fonte do teto de 6 é o próprio Mizuki, em 08/09** (`a-escada-com-numero.md` l.90) `[C]`.

---

## 6. O que isto implica para o redesenho

*Inferência minha `[I]`, e não recomendação: é o mapa do que a proposta da amiga toca.*

- **A sub-categoria "1×1, 2×1, 4×1, 5×1, 6×1" reabre o eixo da `Dupla`.** A Dupla morreu por dois motivos medidos.
  - O primeiro: as ações saíam de `pessoas − 1`, e a razão `pessoas ÷ (pessoas − 1)` explode em baixo (peça 26 l.204).
  - O segundo: o golpe dela saía `1,60×` o topo da banda de `21-28%` (peça 26 l.182; `ESTADO` l.114-118).

  Qualquer degrau de 2 ou 3 pessoas precisa de ações declaradas e de um golpe dentro dessa banda. **A banda tem dono** (`fila/DECIDIDO-o-capanga.md` §1) e é lida pela peça 1 l.536 e pelo `conferir-atributos` `[C]`.
- **O nome também tem histórico.** A fase 0 escolheu o nome pela gravidade justamente para o leitor não converter pessoas (`00-fase-0/decisoes.md` l.47-49) `[C]`.
- **O dado "por pessoas" já existe.** A tabela de rodadas por tamanho de mesa (`a-escada-com-numero.md` l.106-110) é, em essência, uma categoria lida contra 3, 4, 5 e 6 pessoas.
- **Um teto de 6 pede decidir o que fazer com os multiplicadores.**
  - Mesmo com a escada topando em 6, uma Catástrofe com Expansão dá 11,5, e com imunidade a Físicos dá 15.
  - A alavanca de manter o tamanho dividindo o dano pelo multiplicador foi **retirada por decisão** (v0.229), e a 7.1b l.952 acende se ela voltar.
  - Então o teto é decisão do Mizuki, e não conta.
- **O custo mínimo de mudar a mesa de 4 para outra base** é mexer no manual (l.155-172), na peça 26 §4 e no `dados.js`. Também é regerar a `TABELA.md` e o livro. Além disso, 9 checagens do `conferir-bestiario`, o bloco 7 do `conferir-ficha`, a 13c do `conferir-alma`, a peça 24 §3.3 e a peça 19 §2.2 **leem a mesa de 4 de algum jeito** (§3.1).
- **As 3 ações do Desastre estão presas à régua de condição da peça 19** (checagem 12 do `conferir-dano`). Mudar o Desastre para 2 ações reprecifica quatro condições do jogador (peça 19 l.87-100) `[C]`.

---

## 7. Lacunas

- **O DMG 2014 não foi conferido.** É livro fechado, e o conteúdo não está no SRD 5.1: *"média das três primeiras rodadas"*, *"área conta como 2 alvos numa mesa de 4"* (cap. 9, p. 278, citado pela peça 26 l.590), a tabela de PV efetivos (l.396) e o passo 13 (l.500). Registrei como citação do projeto; a prova do projeto está em `bestiario/04-fase-1/refutacao/prova-p1-dmg2014.md`, que **não li**.
- **Não li os `DECIDIDO-*`/`MEDIDA-*` da `fila/`**, a não ser `MEDIDA-a-intervencao.md` §11-12. Por isso as divergências 5 e 9 podem ter resposta num arquivo que não abri.
- **Não li o `conferir-manual.py`**, que o `conferir-aptidoes` l.85 diz vigiar a cópia `CHEFE`, nem a checagem 7d em diante do `conferir-ficha`. Também não li o 9.6 e o 10.1/10.2 do `conferir-bestiario` linha a linha, só o cabeçalho e as referências.
- **Não abri os `.docx` nem os PDFs** (`bloco-de-inimigo.docx`, `Projeto-M-Bestiario*.pdf`). O que eles imprimem inferi pelo código que os gera.
- **As 5 e 6 ações da Catástrofe e da Calamidade:** não achei medida própria. A peça diz que são declaradas.
- **A origem do número 8 do esquadrão de capanga:** achei a medida (a forma A contra a do Draw Steel), mas não a razão do "8" antes de ele virar câmbio. A peça diz que a simulação **confere** o 8, e não que o escolhe (l.317).
- **Os números da mesa de 07/09** são relato do Mizuki (`mesa-nd20.md`), e não log de jogo.

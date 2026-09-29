# Fase 2 — o redesenho do inimigo

*Aberta em 27/09/2026, pelo item 8 da fila do `sistema/ESTADO-ATUAL.md`. A peça 26, o livro de inimigos e o gerador continuam valendo até o redesenho fechar; nada daqui é regra ainda.*

## 1 · O pedido, nas palavras dele — 27/09/2026

> "Temos de refazer os inimigos, seus status e formulas. O livro foi bem montado e temos um esqueleto bom, mas não funcional
> * 1.1: Acredito que temos de refazer o esqueleto base de inimigos. Uma amiga me sugeriu que dentre as categorias ameaça, desastre, catastrofe e calamidade, teria sub categorias, na qual dividiria para QUANTAS pessoas do nivel daquela criatura iria enfrentar ela. Ent por exemplo, ameaça poderia ter 1x1-2x1-4x1-5x1-6x1. Teriamos de mudar pra que serve as categorias base, mas elas ainda simulariam força de pequena pra grande, além de que... são 4 categorias? lembrava q era 5 ou 6. Só não tenho certeza se é uma boa abordagem, queria validar isso, porque... os inimigos n deveriam passar da necessidade de 6 players, fica impossivel e sem sentido
> * 1.2: As fichas estão boas, mas parecem "duras", usamos de base o DnD como esqueleto, mas levamos muito ao pé da letra, acredito que precisamos refazer a montagem
> * 1.3: Os valores... para encaixarmos o 1x1 - até 6x1, precisamos rebalancear isso direito, atualmente calamidade é pra 8 (e tira essa frase do livro q coloca que, "precisa de 8 mas n tem oito players em mesa", isso é inutil) - Ignorando obviamente invocações por enquanto
>
> Lembrando que o que eu disse n é regra, mas sim tem de ser trabalhado"

## 2 · A primeira leva de pesquisa — 27/09/2026

**Liberada por ele ("1 - A"): dois agentes, a pesquisa externa e a auditoria interna.** *Os resultados estão em `pesquisa/`. O agente da pesquisa morreu no limite de sessão depois de passar pelos sete sistemas; o `RESULTADO-pesquisa-externa.md` foi montado das notas dele, sem fonte nova.*

- **A grade tem precedente direto:** *o Campeão (1) a (6) do Fabula Ultima, o grande e o enorme do 13th Age e o Solo de 6 heróis do Draw Steel. Em todos, o N multiplica a vida e os turnos ou ataques, e não o tamanho de cada golpe.*
- **O teto de 6 já era dele, de 08/09:** *"uma mesa nunca vai ter mais de 6 players e talz, ent n precisa pensar nisso de 7-8 players"* (`04-fase-1/a-escada-com-numero.md`). O `8` da Calamidade entrou depois, pela fórmula `personagens = fator × 4`.
- **O "duro" é mais do projeto que do D&D:** *do D&D veio a forma do bloco; a rigidez dos números vem de o inimigo ser a ficha de personagem sem o Caminho, de um fator só para vida e dano, da luta de 3 rodadas em toda conta, do golpe igual em toda ação e das 3 Intervenções fixas.*

## 3 · As três respostas — 28/09/2026

**1 · O que a categoria vira — "A+B":**
> "Ele é totalmente A, mas faria sim sentido inimigos de categorias acima ter mais recursos, n só numeros. Tipo... n faz sentido uma ameaça ter ação lendaria, mts vezes, no máximo a feita pra 6 pessoas, diferente de um DESASTRE, ele poderia ja ter numa ficha de 4x1, exemplos tá? n precisa levar ao pé da letra"

**A categoria é a dificuldade da luta para aqueles N, e a de cima também ganha recurso fora dos números.**

**2 · O que fazer com os traços que multiplicam o encontro — "B":**
> "Faz mais sentido ser B, entendo a A, mas vc tem q pensar q como fica o inimigo Calamidade? n tem pra aonde subir, dar expansão e essas mecancias deixam o encontro mais letal, mas n necessariamente deixa ele impossivel do grupo ganhar. Semelhante a DnD mesmo, tem inimigo nd10 q n tem habilidade de recarga e nem ação lendaria, ao mesmo tempo que alguns tem"

**A Expansão, a Recarga, a resistência e a cura se pagam por dentro da célula, encolhendo o resto.** *Isso reverte a decisão da v0.229 ("a Expansão aumenta o encontro e não se compensa"), e a guarda da 7.1b do `conferir-bestiario.py` contra "manter o tamanho" cai junto quando o redesenho entrar.*

**3 · A montagem da ficha — "B":**
> "B, mas acredito eu que defesa, acerto, cd, vida podem sir ser aumentados ou diminuidos baseados nos atributos, mas ainda é uma ficha propria semelhante a DnD"

**A ficha é própria, por tabela de nível, e os atributos sobem ou descem a Defesa, o acerto, a CD e a vida em volta do valor da tabela.** *A ficha de personagem sem o Caminho deixa de ser a base.*

## 4 · O corte 1 — 28/09/2026

*A conta está em `conta-esqueleto.py`, que reproduz antes a linha do manual e a escada da peça 26 nas células que o esqueleto novo mantém.*

**O que o corte supõe:** *o N põe a vida e as ações (o inimigo age N vezes, e cada golpe é a pressão de uma pessoa, `22,5%` da vida de um personagem, dentro da banda de `21-28%`); a categoria é a dificuldade, pelo degrau do Pathfinder 2e (`60 · 80 · 120 · 160`, ou `0,75 · 1 · 1,5 · 2`), e mexe na duração; a Intervenção fica liberada quando `N × peso ≥ 4`.*

| categoria | peso | rodadas | vida do grupo que a luta tira | Intervenção a partir de |
|---|---|---|---|---|
| `Ameaça` | `0,75` | `2,25` | `51%` | `×6` |
| `Desastre` | `1,00` | `3,00` | `67,5%` | `×4` |
| `Catástrofe` | `1,50` | `4,50` | `101%` | `×3` |
| `Calamidade` | `2,00` | `6,00` | `135%` | `×2` |

- **Nenhum golpe sai da banda, em nenhuma das 24 células:** *é o que matou a `Dupla`, resolvido pelas ações = N.*
- **Quatro células de hoje sobrevivem:** *o `Desastre ×4` é o `Desastre` de hoje; o `Desastre ×1` é a `Ameaça` de hoje; a `Catástrofe ×4` e a `Calamidade ×4` têm a vida da `Catástrofe` e da `Calamidade` de hoje, mas passam a ser luta severa e extrema para quatro, com o dano por rodada do `Desastre`.*
- **A regra `N × peso ≥ 4` reproduz os dois exemplos dele** *(a `Ameaça` só no `×6`, o `Desastre` já no `×4`).*

**Em aberto, para ele:**
1. *a luta mais difícil é mais longa, mais pesada por rodada, ou as duas coisas — e o que passa de N ações vem de recurso (Intervenção, Recarga), não de golpe maior;*
2. *as células `×1` e `×2` têm menos ações que o piso `3` da régua de condição da peça 19: um inimigo de uma ação morre para `Atordoado`, que é o problema do chefe solo que o D&D resolve com resistência lendária e o Pathfinder 2e com reação.*

## 5 · As duas respostas do corte 1 — 28/09/2026

**1 · Mais longa ou mais pesada — "B", meio a meio:**
> "B, tente usar outros sistemas de base, pode pesquisar aprofundadamente a media de rodadas que eles dão baseado nessas questões. Mas eu penso em ser 2-2.5-3-4-5 rodadas, lembrando q tem a categoria faltando"

**As rodadas dele (`2 · 2,5 · 3 · 4 · 5`) são a hipótese de trabalho, com cinco degraus, como os cinco do Pathfinder 2e (trivial a extrema) e do Draw Steel.** *Com o orçamento do Pathfinder 2e (`40 · 60 · 80 · 120 · 160`), o que sobra do orçamento depois da duração vira pressão por rodada — `0,75 · 0,90 · 1,00 · 1,12 · 1,20` —, e o que passa das N ações vem de recurso: meia ação por rodada na `Catástrofe ×4` e `0,8` na `Calamidade ×4`. A pesquisa das rodadas em outros sistemas é o próximo passo, e ela confirma ou move essas rodadas.*

**2 · O inimigo de uma ou duas ações — "A", só no `×1` e no `×2`:**
> "A, poderia ser uma mecanica apenas para combates 1x1-2x1"

**No `×1` e no `×2`, o inimigo pode encerrar, no fim do turno dele, uma condição que tira ação, pagando com vida.** *Ele continua precisando falhar no teste para ela pegar — a decisão da v0.205 fica ("ele precisa passar no teste").*

## 6 · As duas respostas do corte 2 — 28/09/2026

**1 · A categoria que faltava — o `Capanga`:**
> "Capanga, ele pode sim ser usado contra players em multiplas quantidades ou junto de um chefe"

**O `Capanga` é o degrau de baixo, o de 2 rodadas, e continua entrando em bando contra os players ou junto de um chefe.** *Os cinco degraus ficam `Capanga · Ameaça · Desastre · Catástrofe · Calamidade`. Quanto um `Capanga` tira do orçamento da luta, sozinho, em bando ou ao lado de um chefe, é conta do corte que monta o encontro.*

**2 · A pesquisa das rodadas — "A":**
> "A"

**Dois agentes, com os arquivos em `agentes-2026-09-27/bestiario-leva-2/`:** *o da matemática mede as rodadas de cada dificuldade e de cada N pela conta de cada sistema (Pathfinder 2e, D&D 2024, Draw Steel, 13th Age), e o do que dizem junta o que livros, designers e mesas medidas falam da duração de uma luta, com o teto em que ela vira moedor.*

## 7 · O corte 2, a ficha — 28/09/2026

*Três contas que não dependem das rodadas, no fim de `conta-esqueleto.py`, cada uma com a regressão contra o publicado antes.*

**1 · O ponto de atributo se paga em vida, e a troca é a do papel de hoje.** *A leitura da resposta 3 que ele não contestou: cada ponto acima da tabela na Defesa custa `10%` da vida, e cada ponto no acerto e na CD custa `8,7%`; abaixo, a vida recebe na mesma medida. A conta reproduz o `Brutamontes` (`Defesa −2`, vida `× 1,20`) e o `Baluarte` (`Defesa +2`, vida `× 0,80`) — o papel vira um atalho pronto dessa troca.*

**2 · O `Capanga` no degrau de 2 rodadas.** *O esquadrão de hoje (`2N` corpos de um golpe, o grupo derruba N por rodada) já dura 2 rodadas contra qualquer N, mas cobra `67,5%` da vida do grupo — o custo do `Desastre`, acima da `Ameaça` (`51%`). O degrau de baixo pede `33,8%`. Duas formas chegam lá com as 2 rodadas: os mesmos `2N` corpos com meio golpe (exato em todo N; o golpe cai para `11%` da vida de um personagem, abaixo da banda de `21-28%`), ou N corpos de dois golpes com o golpe inteiro (exato só no N par; o corpo deixa de cair num golpe).* **Em aberto, para ele.**

**3 · Sair da condição no `×1` e no `×2`: o momento e o preço.** *A condição dura uma rodada (a Melhoria `Condição` do manual) e o inimigo age num turno só (as `Ações Múltiplas` do livro de inimigos). Pagar no FIM do turno dele, como a pergunta do corte 1 escreveu, só adianta na condição que dura mais que uma rodada; a que resolve o `Atordoado` do inimigo de uma ação é pagar no COMEÇO do turno. O preço neutro é a fatia da luta que a condição tiraria: o dano de um personagem por rodada, por ação negada — a vida do `Capanga` do mesmo nível (`78` no nível 30), ou `40%` da vida de uma `Ameaça ×1`. O Draw Steel cobra bem menos (`10` de dano no solo instantâneo).* **Em aberto, para ele.**

## 8 · A segunda leva de pesquisa: as rodadas — 28/09/2026

*Dois agentes, `631k` tokens (`323k` + `308k`) contra a estimativa de `850k`. Os arquivos estão em `pesquisa/leva-2/`; o CSV de 2 MB dos combates do FIREBALL ficou só no HD (`agentes-2026-09-27/bestiario-leva-2/`), e o `conta-fireball-rodadas.py` refaz ele do dado aberto. Conferi duas tabelas do Pathfinder 2e na fonte (vida moderada e CA alta nos níveis 3, 10 e 20) e rodei de novo a contagem do FIREBALL: as duas batem.*

- **As rodadas dele se sustentam, e ficam.** *Pela conta dos sistemas, com 4 personagens, a mediana por degrau é `1,5 · 1,8 · 2,7 · 3,3 · 4,7`: o `Desastre` em 3, a `Catástrofe` em 4 e a `Calamidade` em 5 caem dentro do medido. O `Capanga` e a `Ameaça` saem um pouco mais longos que o chefe sozinho dos outros, mas batem com o que se diz e com o que se mediu. O modelo publicado do Tom Dunn para o 5e dá `2,1 · 3,0 · 3,7 · 4,5` do Fácil ao Mortal. O Draw Steel escreve que a luta "typically last 3 or fewer rounds" e que a de 5 é "a long fight". Nos `15.283` combates de 5e do FIREBALL a mediana é 3, e no Critical Role a moda é 3.*
- **O moedor começa em 6 rodadas, e a `Calamidade` fica uma abaixo.** *O Fabula Ultima zera o prêmio na 6ª rodada; os relatos do 4e põem o moedor em 7-8. O risco é a cauda: no FIREBALL, quando a luta típica tem 5 rodadas, 1 em 4 vai a 7-8. Todo sistema que aceita luta longa corta essa cauda com um mecanismo — escalada por rodada, relógio, fase ou fuga do chefe.* **Fechado no fim desta seção: nenhum.**
- **Uma duração por degrau serve de `×1` a `×6`.** *Com a vida e as ações crescendo exatamente com o N, as rodadas não dependem do N; é o que o 13th Age faz, e a conta mostra a razão de `0,93` a `0,97` de uma ponta à outra. Os sistemas de orçamento encurtam a luta com o N, e o FIREBALL mostra o grupo de 5-6 lutando cerca de uma rodada a mais que o de 2 — sinais opostos e fracos; o `×5` e o `×6` ficam para o playtest.*
- **A escada inteira é mais pesada que a dos outros.** *A pressão do `Desastre` de hoje (`67,5%` da vida do grupo) é a da luta severa-a-extrema do Pathfinder 2e e do D&D 2024; a moderada deles tira de `20%` a `48%`. Isso vem da decisão da v0.205 ("fica assim"), e a razão entre os degraus é a deles: a `Calamidade` é o dobro do `Desastre`, como a extrema é o dobro da moderada. Com isso a `Calamidade ×4` tira `135%` da vida do grupo, e conta com a cura para não matar.*

**A luta longa ganha mecanismo para cortar a cauda? — "C":**
> "C, decisão do mestre é melhor aqui"

**Nenhum mecanismo: o 5 da `Calamidade` é média, e o mestre corta a luta quando a vitória estiver clara.** *As rodadas `2 · 2,5 · 3 · 4 · 5` ficam como a duração de cada degrau.*

## 9 · O corte 3, o recurso na grade nova — 28/09/2026

*No fim de `conta-esqueleto.py`, com a regressão contra o `0,923` da `Intervenção` e a tabela da `Recarga` da peça 26 §6.5 antes.*

- **A `Recarga` passa a ter um preço só por degrau, e mais barato.** *Com ações = N, a razão da peça 26 (`2,5 × metade das pessoas ÷ ações`) vira `1,25` em todo N, e o preço depende só da duração: `× 1,15` na `Ameaça`, `× 1,14` no `Desastre`, `× 1,13` na `Catástrofe` e `× 1,12` na `Calamidade` (hoje, `× 1,14` a `× 1,37`).*
- **A `Intervenção` sai cara no N pequeno e barata no grande, sozinha.** *O `0,75` de ação extra por luta pesa sobre as `rodadas × N` ações: `× 1,30` na `Ameaça ×1` e `× 1,03` na `Calamidade ×6`. É a mesma direção dos exemplos dele (a `Ameaça` só no `×6`, o `Desastre` já no `×4`), e a regra `N × peso ≥ 4` fica como a porta.*
- **O golpe sem recurso vai de `20,2%` (`Ameaça`) a `27,0%` (`Calamidade`) da vida de um personagem.** *O piso de `21%` da banda ficou sem motivo desde a forma `B` do `Controlador` (10/09), e a banda é "o medido, arredondado": ela passa a `20%`–`28%` quando a grade entrar.*

**Em aberto, para ele: o recurso se paga no golpe ou na vida.** *No golpe, a luta dura o que o degrau diz e o golpe encolhe (a `Calamidade ×4` com os dois vai de `27,0%` a `23,3%`; o `Desastre` com `Recarga`, de `22,5%` a `19,8%`). Na vida, o golpe fica e a luta encurta (a `Calamidade ×4` com os dois vai de 5 a `4,3` rodadas; o `Desastre` com `Recarga`, de 3 a `2,6`), que é o que a peça 26 faz com o papel ("pagando em vida, a fatia não se move").*

## 10 · As três respostas do corte 3 — 28/09/2026

**1 · A forma do `Capanga` — "B":**
> "B"

**O `Capanga ×N` é um esquadrão de `2N` corpos que caem num golpe, com meio golpe.** *Ele fecha `33,8%` da vida do grupo em 2 rodadas, em todo N; o golpe dele fica abaixo da banda, que passa a vigiar só os chefes.*

**2 · Sair da condição no `×1` e no `×2`:**
> "Meça para balancear, mas acredito que n ser garantido seria melhor. Talvez uma habilidade pra rerolar o TR, rolar no começo do turno dnv ao invés do final, etc. Pq se n a condição fica inutil"

**Não garantido: uma chance de TR, e não um pagamento.** *A medida está no §11.*

**4 · De onde sai o pagamento do recurso:**
> "Olhe os outros sistemas e busque balancear com base nisso, mas acredito que um dragão que tem baforada n tem dano reduzido em comparação a um inimigo que tenha so ataques do mesmo nd, eu acho"

**A leitura dele é que o golpe não encolhe; a medida nos outros sistemas decide.** *Está no §11.*

## 11 · As duas medidas das respostas do corte 3 — 28/09/2026

**1 · O recurso não encolhe o golpe, e se paga na vida.** *Medido nos 331 blocos do SRD 5.2 (`pesquisa/leva-2/conta-recarga-dnd.py`): no mesmo ND, o monstro com `Recarga` tem a rotina de ataque `× 1,05` da do monstro que só ataca, a vida `× 0,94` e a CA `+0,9` — o golpe não paga, e a vida e a CA quase se anulam. O GM Core do Pathfinder 2e dá à área de uso limitado (a baforada) o dano da tabela dela e não manda baixar golpe, vida nem outro número ([Damage-Dealing Abilities](https://2e.aonprd.com/Rules.aspx?ID=2910)). Nos dois, a baforada se paga pela economia de ação — ela toma o turno —, e a `Recarga` daqui já faz isso ("come as ações múltiplas do turno", peça 26 §6.5). O que sobra é o ganho da área, e a resposta "B" manda pagar por dentro: com o golpe parado, sobra a vida.* **O `Desastre` com `Recarga` fica com a vida `÷ 1,14` e dura `2,6` rodadas; a `Calamidade ×4` com `Intervenção` e `Recarga`, `÷ 1,16` e `4,3` rodadas.**

**2 · A condição no `×1` e no `×2`: um TR no começo do turno, não garantido.** *Um TR antes do turno multiplica o que a condição nega pela chance de ele falhar. Pela régua da peça 19 §2.2 (o chefe de 3 ações fica em `2,18×` a `2,32×`, com o filtro em `3,00×`):*

| célula | sem nada | TR no começo do turno, com a maestria | sem a maestria (o TR sem treino) | com desvantagem |
|---|---|---|---|---|
| `×1` | `6,23×` a `6,95×` | **`2,18×` a `2,43×`** | `2,49×` a `3,82×` | — |
| `×2` | `3,19×` a `3,48×` | `1,12×` a `1,22×` | `1,28×` a `1,91×` | **`1,84×` a `2,01×`** |

**A proposta:** *no `×1`, a condição que tira ação dá ao inimigo um TR no começo do turno dele, sempre com a maestria; passou, ela sai antes de ele agir. No `×2`, o mesmo TR, com desvantagem. As duas células voltam à régua do chefe de 3 ações, e a condição continua valendo perto de duas vezes o dano que ela substitui. Sem a maestria, o `×1` passa do filtro do nível 10 em diante; o mesmo TR normal no `×2` deixa a condição a `1,1×`, quase igual ao dano. O reroll que ele citou dá a mesma conta na primeira rodada; o TR no começo do turno é a forma que ele escreveu, e as `Pesadas` já têm o TR, só que no fim do turno.* **Sigo com ela se ele não disser o contrário.**

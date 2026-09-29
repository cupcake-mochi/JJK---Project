# 26 · Bestiário — a máquina de montar inimigo

*Fechada na v0.198. Refeita na v0.282, como a fase 2 do bestiário: a escada que media quantas pessoas o inimigo exigia virou uma grade de dificuldade por tamanho de grupo. A peça de antes está inteira em `sistema/99-arquivo/secoes-substituidas/26-bestiario-a-escada-ate-v0.281.md`, e as decisões e as contas da fase 2, em `bestiario/09-fase-2/`.*

## 1. O que ela é, e o que ela não é

**Esta peça junta num lugar só os números que montar um inimigo pede.** Até a v0.198 eles moravam em quatro donos — o manual, a peça 1, a peça 19 e o `ESTADO-ATUAL` —, e três dos que a mesa rola toda rodada não tinham dono nenhum: a Defesa do inimigo, o acerto dele e a CD dele.

**Ela é máquina, e não catálogo.** *Decisão do Mizuki na v0.161: o Bestiário sai como máquina mais maldições prontas, e não como recolhimento puro.* **As prontas moram no livro do Bestiário e no gerador de inimigo**, e a checagem 9.5 do `conferir-bestiario.py` refaz as seis.

> **A ficha de inimigo é própria, por tabela de nível.** ***Decisão do Mizuki, 28/09/2026:*** *"defesa, acerto, cd, vida podem sim ser aumentados ou diminuídos baseados nos atributos, mas ainda é uma ficha própria semelhante a DnD".* **O inimigo continua tendo refino, Passiva, aptidão e às vezes técnica** — muita coisa que ele enfrenta na obra é feiticeiro, e feiticeiro se monta com as mesmas peças. *O que ele não tem é Caminho, Trilha e poço de PE, e o §6 diz por quê.*

**E a rota que só o inimigo tem é ser maldição.** *O jogador não escolhe isso, em nenhuma das nove rotas de Origem da peça 9.*

## 2. O grau é ficção, e a obra é quem manda nisso

***Decisão do Mizuki: o grau fica na ficha da maldição como rótulo, e não entra em conta nenhuma.*** **A métrica é o nível, a categoria e o N do §4.**

O motivo é a peça 12 §2: *"Grau é reconhecimento; nível é poder"*. Se o grau da maldição parear com o grau do feiticeiro, e o grau do feiticeiro não diz nível, então dois mestres montam o mesmo encontro com fichas de níveis diferentes — que é o filtro que este projeto usa para tudo.

> **⚠ A intuição de parear grau com grau é da obra, e ela está certa lá.** *A escada existe para classificar quatro coisas — feiticeiro, maldição, objeto e ferramenta — e ela nasceu como regra de despacho: manda-se um feiticeiro do grau da maldição.* **O que não atravessa é a metade numérica**, porque aqui o grau é patente e a patente sobe por feito.
>
> **E a obra deixa uma fronteira que a ficha já carrega de graça.** *O que separa uma maldição de grau 2 de uma de semi-grau 1, na classificação da obra, é **saber usar técnica**.* **Isso não é número: é uma linha do §6 desta peça, e ela está na ficha quer o grau exista ou não.**

## 3. A ficha, e cada linha tem dono

**Vinte linhas. Nenhum número novo nasce aqui** — o que esta peça faz é dizer de onde cada um sai.

| linha | valor | dono |
|---|---|---|
| nível | o nível do grupo | o mestre declara antes da mesa |
| categoria | `Capanga` · `Ameaça` · `Desastre` · `Catástrofe` · `Calamidade` — a dificuldade da luta | o §4 |
| N | para quantas pessoas do nível a ficha é feita, de `×1` a `×6` | o mestre declara; o §4 |
| vida | `rodadas × N × a saída de um personagem`; a do `Capanga` é a saída de um personagem, por corpo | manual, a tabela `Inimigos`, e o §4 |
| **Integridade** | metade da vida máxima, arredondando para baixo | peça 24 §3.3 |
| o golpe | `a pressão do degrau × o golpe-base`; o do `Capanga` é metade do golpe-base | manual, a tabela `Inimigos`, e o §4 |
| ações por rodada | `N`; no esquadrão do `Capanga`, uma por corpo | o §4.2 |
| **Defesa** | a da tabela do §3.1, e o desvio pelo §3.2 | o §3.1 |
| **acerto** | o da tabela do §3.1, e o desvio pelo §3.2 | o §3.1 |
| **CD** | a da tabela do §3.1, e o desvio pelo §3.2 | o §3.1 |
| Reação | uma por rodada, volta no começo do turno dele | manual, a seção `Inimigos` |
| refino | a curva do `meio a meio` | peça 11 §3 |
| Testes de Resistência | dois treinados de quatro | peça 7 §6 |
| deslocamento | `9 m` | peça 3 §3 |
| tamanho | o alcance do golpe e onde o corpo cabe — não cobra nada | o §3.3 |
| papel | o que ele ganha num eixo ele paga na vida | o §3.4 |
| **atributos** | os cinco, no orçamento da peça 2 | peça 2 §3 e o §3.2 |
| **características** | Passivas, aptidões e técnica, pelo §6 | peça 11, o mesmo catálogo do jogador |
| **pacto** | opcional, e o teto do permanente é da Essência dele | peça 22 §3 |
| **resistência, vulnerabilidade e imunidade** | cobrança e isenções na vida, pelo §6.3 | peça 19 §4 |

**As três derivadas em negrito — Defesa, acerto e CD — têm a tabela do §3.1 por dona desde a v0.282.** *Até a v0.281 elas saíam das fórmulas da peça 1 aplicadas à ficha de personagem sem o Caminho, e a tabela era o resultado; hoje a tabela é a regra, e as fórmulas são a prova de que ela bate com o outro lado da mesa.*

### 3.1 A tabela por nível — Defesa, acerto e CD

**A Defesa, o acerto e a CD do inimigo de cada nível são os desta tabela.** *Ela é a curva de quem investe — atributo `3` no nível 2 subindo a `6` no 26 —, e é por isso que ela bate com o que a peça 1 §6 publica do lado do jogador.* **A Defesa da tabela é `10 + Destreza + proteção`, o acerto é `atributo + maestria` e a CD é `8 + atributo + maestria`, com o atributo da curva**, pelas fórmulas da peça 1 §5.

| nível do grupo | 5 | 10 | 15 | 20 | 25 | 30 |
|---|---|---|---|---|---|---|
| Defesa | `14` | `16` | `17` | `18` | `19` | `20` |
| acerto | `+4` | `+6` | `+6` | `+8` | `+8` | `+10` |
| CD | `12` | `14` | `14` | `16` | `16` | `18` |
| refino | `1` | `4` | `6` | `7` | `9` | `10` |

**Contra um personagem que investiu em defesa ele acerta `50%` a `55%`, e o Teste de Resistência treinado dele falha `35%`.** *São os mesmos números que a peça 1 §6 publica do lado do jogador, e é isso que prova a tabela: se ela estivesse errada, os dois lados da mesma rolagem discordariam.*

> **A proteção da Defesa anda junto com o refino, pela peça 11 §6** — `1/3 do refino + 1`. *Sem ela a Defesa do inimigo congela e o acerto do personagem deriva `+15` pontos percentuais na campanha, que é o erro que a v0.117 consertou do lado do jogador.*

### 3.2 Os atributos — e o que sai da tabela se paga na vida

**O que sobe ou desce a Defesa, o acerto e a CD em volta da tabela se paga na vida.** *A Defesa lê a Destreza e o papel (§3.4); o acerto e a CD leem o atributo com que ele ataca.* **Um ponto de Defesa acima da tabela custa `10%` da vida, e um ponto de acerto e CD custa `8,7%`; abaixo, a vida recebe na mesma medida.**

| pontos em volta da tabela | a vida, pela Defesa | a vida, pelo acerto e pela CD |
|---|---|---|
| `−2` | `× 1,200` | `× 1,235` |
| `−1` | `× 1,100` | `× 1,105` |
| `+1` | `× 0,900` | `× 0,913` |
| `+2` | `× 0,800` | `× 0,840` |

*A conta é a da peça 1 §5.2: um ponto move `5` pontos percentuais. O personagem acerta o alvo difícil em `50%`, então a Defesa `+k` deixa a vida efetiva em `50 ÷ (50 − 5k)`, e a vida crua paga o inverso; o inimigo acerta o meio da banda do §3.1, `52,5%`, então o acerto `+k` multiplica a saída dele por `(52,5 + 5k) ÷ 52,5`, e a vida paga o inverso.* **O `Brutamontes` e o `Baluarte` do §3.4 são esta troca com nome:** *`Defesa −2` e vida `× 1,20`; `Defesa +2` e vida `× 0,80`.*

**O orçamento de atributo continua o da peça 2, e ele é o que dá os Testes de Resistência, as perícias e a cor da ficha.** **O inimigo monta os cinco com nove pontos na criação, teto `3` ali, e teto `6`.** **Em cada marco ele ganha `+1`, e mais `+1` em cada escolha de marco que o `meio a meio` não gasta em refino.**

***Decisão do Mizuki, v0.232:*** *meio a meio, como o refino.*

| marco | nv 6 | nv 10 | nv 14 | nv 18 | nv 22 | nv 26 | nv 30 |
|---|---|---|---|---|---|---|---|
| refino do `meio a meio` | `3` | `4` | `6` | `7` | `9` | `10` | `10` |
| escolhas gastas em refino, acumuladas | `1` | `1` | `2` | `2` | `3` | `3` | `3` |
| **pontos de atributo** | **`10`** | **`12`** | **`13`** | **`15`** | **`16`** | **`18`** | **`20`** |
| **pontos de atributo do chefe** | **`11`** | **`13`** | **`14`** | **`16`** | **`17`** | **`19`** | **`21`** |

*Antes do nível 6 são os nove da criação, e os dez do chefe. As escolhas gastas em refino saem da peça 11 §3: a curva menos o refino que o marco dá de graça, e uma escolha gasta não volta quando a curva bate no teto.* **A invocação da peça 15 §3.3 continua com o `+1` do marco só, porque o ritmo dela é o do dono.**

> **As escolhas de marco seguem a regra do jogador, pela peça 11 §3.** *A que o `meio a meio` gasta em refino dá `+1` de refino e uma aptidão. Cada uma das outras dá o `+1` de atributo ou uma aptidão, e quem monta escolhe.* **A tabela conta todas como atributo, então ela é o teto:** *cada aptidão tomada numa escolha de atributo tira `1` ponto da linha.* **E o gate de aptidão cobra o marco antes de a gateada abrir, como no jogador.**

***Decisão do Mizuki, v0.242:*** *"ele tem q escolher se pega atributo ou aptidão".*

> **O chefe começa com dez pontos na criação, e não nove.** *Chefe é quem carrega `Intervenção` (§6.5). O teto de `3` na criação e o de `6` continuam.*

***Decisão do Mizuki, v0.233:*** *"vai ser na criação da ficha ao invés de começar com 9 pontos, começa com 10. É um bônus que sim, faz diferença, mas calcular tanto encima dele é trabalho extra demais, é um ponto q pode ir em 5 atributos diferentes".* **O molde é o do Draw Steel, em que o `Leader` e o `Solo` ganham `+1` no maior atributo.**

> **O ponto do chefe é a única coisa acima da tabela que não se paga na vida, e isso é decisão.** *Se ele for para a Destreza, a Defesa sobe `1`; se for para o atributo de ataque, o acerto e a CD sobem `1` — e a vida fica.* **O chefe fica no máximo um ponto acima da tabela**, *na Destreza ou no atributo de ataque (v0.235).*

**⚠ E não existe "atributo do Caminho" aqui.** *A ficha do jogador tem cinco atributos e um Caminho que decide vida e PE; o inimigo tem cinco atributos e a célula do §4, que decide vida e golpe.* **Um chefe de Força `6` e um de Essência `6`, na tabela, têm a mesma vida e o mesmo golpe, e jogam diferente.**

### 3.3 O tamanho — o alcance, e ele não cobra nada

**O tamanho diz onde o corpo cabe e até onde o golpe alcança.** *Ele não tira Defesa, não mexe na vida e não pede nada em troca:* **o tamanho não cobra nada.**

| tamanho | ocupa na grade | alcance | o golpe pega |
|---|---|---|---|
| `Minúsculo` · `Pequeno` · **`Médio`** | `1×1` *(1,5 × 1,5 m)* | `1,5 m` | só o alvo |
| **`Grande`** | `2×2` *(3 × 3 m)* | `3 m` | o alvo, e metade em `1` vizinho |
| **`Imenso`** | `3×3` *(4,5 × 4,5 m)* | `4,5 m` | o alvo, e metade em `1` vizinho |
| **`Colossal`** | `4×4` *(6 × 6 m)* | `6 m` | o alvo, e metade em `1` vizinho |

**O alcance é o lado da grade vezes o quadrado, e nos alvos o tamanho é um degrau só:** *`Grande`, `Imenso` e `Colossal` pegam o mesmo vizinho a metade.*

> **⚠ E ele põe perto de um quinto de encontro FORA da conta, declarado de propósito.** *Um inimigo de `Grande` para cima entrega isso a mais que um `Médio` da mesma célula, de graça.* **Medido no projeto do Bestiário em três sistemas:** *a defesa não muda com o tamanho em nenhum deles — `1,000 ×` em `4.791` criaturas do PF2e, `1,016 ×` em `331` do D&D —, os alvos não escalam, e o alcance escala.* **O campo põe o preço do tamanho na organização e no nível; a célula daqui não sabe do tamanho, e isto está escrito para o mestre contar com a folga.**

### 3.4 O papel — ele redistribui a base, e não acrescenta nada

**O papel é um gerador de base, e não uma coisa que o inimigo faz na mesa.** *Você escolhe a categoria, o N e o papel, e a ficha sai preenchida; as `Ações`, as `Intervenções` e os `Traços` o mestre monta depois disso.* **Por isso ele mora no cabeçalho, ao lado da categoria** — é rótulo do que gerou aquela ficha, e rótulo não gasta entrada nomeada nem pode ser desligado pelo jogador.

> `‹ tamanho › ‹ tipo ›, ‹ grau › · ‹ categoria › ×‹ N › · ‹ papel › · nível ‹ nível ›`

**E ele sai de graça no tamanho do encontro, porque o que ganha num eixo ele paga na vida.** *A regra é uma só e vale nos seis:* **o que ele paga é o inverso do que ele ganha**, e o produto fecha em `1,000`.

| papel | o que ganha | o que paga |
|---|---|---|
| `Brutamontes` | vida crua `× 1,20` | `Defesa −2`, que vale `× 0,833` |
| `Baluarte` | `Defesa +2`, que vale `× 1,250` | vida crua `× 0,80` |
| `Artilheiro` | alcance no ataque, pela tabela por degrau | vida crua, o inverso |
| `Emboscador` | vantagem em um ataque por rodada | vida crua, pela tabela por N |
| `Controlador` | uma ação do grupo negada | vida crua, pela tabela por N |
| `Reforço` | o mesmo câmbio do `Controlador`, gasto em outro bloco | vida crua, pela tabela por N |

> **O ataque do `Artilheiro` alcança `18 m`, em todo nível.** *É o dobro do deslocamento da peça 3, e é o que obriga quem luta de perto a gastar uma rodada para chegar: anda `9 m` e corre mais `9 m`, sem atacar.*

***Decisão do Mizuki, v0.231:*** *"Com base no nível, acho q seria o ideal. N? Se n, mantem semelhante a player, um valor fixo, mesmo".* **Por nível não fecha:** *o deslocamento não cresce com o nível, e o Projétil da Classe da ação cairia em `9 m` enquanto o inimigo não monta feitiço.* **O Draw Steel dá à Artilharia a mesma razão:** *mediana de alcance `10` contra deslocamento `5` do herói, nas `42` fichas, na `bestiario/04-fase-1/papel/MEDIDA-o-alcance-do-artilheiro.md`.*

> **O `±2` de Defesa do papel entra por fora, e a Destreza fica a que a tabela do §3.1 pede.** *O `Brutamontes` do nível 5 tem Destreza `3` e Defesa `12`.* ***Decisão do Mizuki, v0.234:*** *termo à parte.* **A ficha pronta declara com que atributo ataca, e em que atributo entra cada ponto de marco** *(v0.235).*

**O `Artilheiro` varia com o degrau, porque o que ele poupa é a rodada de aproximação, e ela pesa mais na luta curta.** *Uma rodada da luta é a de quem se aproxima, e o alcance poupa meia rodada dela: `1 + 0,5 ÷ rodadas`.*

| categoria | `Capanga` | `Ameaça` | `Desastre` | `Catástrofe` | `Calamidade` |
|---|---|---|---|---|---|
| `Artilheiro` ganha, e a vida paga o inverso | `× 1,250` | `× 1,200` | `× 1,167` | `× 1,125` | `× 1,100` |

**Os três de ação variam com o N, porque o preço deles é UMA ação, e o inimigo tem N.** *Negar uma ação de quem tem uma vale o dobro de negar uma de quem tem seis.* **O esquadrão do `Capanga` se lê por esquadrão: ele tem `2N` ações.**

| papel | `×1` | `×2` | `×3` | `×4` | `×5` | `×6` |
|---|---|---|---|---|---|---|
| `Emboscador` ganha | `× 1,476` | `× 1,238` | `× 1,159` | `× 1,119` | `× 1,095` | `× 1,079` |
| `Controlador` e `Reforço` ganham | `× 2,000` | `× 1,500` | `× 1,333` | `× 1,250` | `× 1,200` | `× 1,167` |
| o esquadrão do `Capanga`, `Emboscador` | `× 1,238` | `× 1,119` | `× 1,079` | `× 1,059` | `× 1,048` | `× 1,040` |
| o esquadrão do `Capanga`, `Controlador` e `Reforço` | `× 1,500` | `× 1,250` | `× 1,167` | `× 1,125` | `× 1,100` | `× 1,083` |

*A vida paga o inverso de cada célula.*

**O `Capanga` toma quatro dos seis:** *`Artilheiro`, `Emboscador`, `Controlador` e `Reforço`.* **`Brutamontes` e `Baluarte` ficam fora:** *a vida do corpo é o que um personagem derruba num golpe (§5), e os dois quebram isso — o `Brutamontes` sobe a vida, e o `Baluarte` faz o golpe errar mais vezes.* **Um corpo que não cai num golpe deixou de ser um `Capanga`.**

**O `Emboscador` não sobe de `Grande`.** *Decisão da fase 1 do Bestiário: um bicho de alcance longo que precisa se esconder é contradição de ficção.* **E o `Reforço` só se paga com mais de um inimigo no encontro**, *porque o câmbio dele é gasto em outro bloco.* *A mesma decisão dizia isso também do `Baluarte`, que na época se chamava `Guardião`; na grade ele troca Defesa pela própria vida, e serve sozinho.*

> *Até a v0.283 as duas frases moravam só no capítulo 6 do livro de inimigos, com o `Baluarte` junto do `Reforço`. A auditoria da fase 2 achou (divergência 3), e a v0.284 trouxe as duas para cá.*

**Nenhum fator acima foi escolhido. Cada um sai de uma regra que já tinha dono:**

| o eixo | a conta | o dono |
|---|---|---|
| `Defesa` ↔ vida | um ponto de Defesa move `5` pontos percentuais, e o personagem acerta alvo difícil em `50%`; então `Defesa −2` deixa ele acertar `60%`, e a vida efetiva cai para `50 ÷ 60` | peça 1 §5.2 |
| vantagem | `+25` pontos percentuais sobre o acerto, e o inimigo acerta o meio da banda que o §3.1 publica. Em um ataque de `N`, o ganho é `(N − 1 + 1,476) ÷ N` | peça 19 §2.2 |
| ação negada | `1 pra 1` — uma ação negada do grupo vale uma ação dele, e uma ação dele é um golpe de `N`. O ganho é `1 + 1 ÷ N` | peça 19 §2.2 |
| alcance | uma rodada da luta é a de aproximação, e o que o alcance poupa nela é meia rodada: `1 + 0,5 ÷ rodadas` | o projeto do Bestiário, em `bestiario/04-fase-1/papel/` |

> **⚠ E o `Artilheiro` e o `Emboscador` têm o ganho fora de célula nenhuma.** *O que eles pagam aparece no bloco — um `Desastre ×4` de nível 30 sai com `810` de vida em vez de `945` —, e o que eles ganham não aparece em lugar nenhum da ficha.* **A palavra no cabeçalho é a única coisa que explica os `135` que faltam**, e é por isso que ela não pode sair de lá.

## 4. A categoria e o N — a grade

***Decisões do Mizuki, 27 e 28/09/2026:*** *"ameaça poderia ter 1x1-2x1-4x1-5x1-6x1 […] os inimigos n deveriam passar da necessidade de 6 players, fica impossivel e sem sentido"* · *"Ele é totalmente A, mas faria sim sentido inimigos de categorias acima ter mais recursos, n só numeros"* · *"eu penso em ser 2-2.5-3-4-5 rodadas, lembrando q tem a categoria faltando"* · *"Capanga, ele pode sim ser usado contra players em multiplas quantidades ou junto de um chefe"*.

**A categoria é a dificuldade da luta, e o N é para quantas pessoas do nível ela é feita, de `×1` a `×6`.** *O teto de seis é dele desde 08/09: "uma mesa nunca vai ter mais de 6 players e talz, ent n precisa pensar nisso de 7-8 players".*

| categoria | rodadas | orçamento | pressão | o golpe, em % da vida de um personagem | `Intervenção` a partir de |
|---|---|---|---|---|---|
| **`Capanga`** | `2` | `0,50` | `—` | `11,2%` | — |
| **`Ameaça`** | `2,5` | `0,75` | `0,900` | `20,2%` | `×6` |
| **`Desastre`** | `3` | `1,00` | `1,000` | `22,5%` | `×4` |
| **`Catástrofe`** | `4` | `1,50` | `1,125` | `25,3%` | `×3` |
| **`Calamidade`** | `5` | `2,00` | `1,200` | `27,0%` | `×2` |

> **A vida é `rodadas × N × a saída de um personagem`**, meio para baixo. *A saída de um personagem é o dano do grupo por rodada da tabela `Inimigos` do manual dividido por quatro, porque a tabela é calibrada para quatro.*
>
> **O golpe é `a pressão × o golpe-base`**, meio para baixo, **e o golpe-base é o dano do chefe da tabela dividido por quatro.** *O orçamento de cada degrau é o do Pathfinder 2e — trivial `40`, baixa `60`, moderada `80`, severa `120`, extrema `160` —, e a pressão é o que a duração não leva dele: `orçamento × 3 ÷ rodadas`, contra o `Desastre`.*
>
> **Ele age `N` vezes por rodada**, e cada golpe é a pressão de uma pessoa. *O `Capanga` é outra forma, e o §5 é dele.*

**O `Desastre ×4` é o chefe da tabela do manual:** *`945` de vida no nível 30, e os `226` por rodada em quatro golpes de `56`, com o arredondamento no golpe.* **E o `Desastre ×1` tem a vida e o golpe da `Ameaça` da escada de antes**, `236` e `56` (a vida antiga foi preservada; o golpe foi recalibrado nesta edição).

**A duração não depende do N.** *A vida e as ações crescem juntas com o N, então o `×1` e o `×6` do mesmo degrau duram o mesmo.* **É o que o 13th Age faz com o monstro grande e o enorme, e o que o Fabula Ultima faz com o Campeão (1) a (6):** *o N multiplica a vida e os turnos, e não o tamanho de cada golpe.*

**As rodadas são dele, e a pesquisa confirmou a ordem e o tamanho.** *Pela matemática de quatro sistemas, com quatro personagens, a mediana por degrau dá `1,5 · 1,8 · 2,7 · 3,3 · 4,7`; o Draw Steel escreve que a luta dura três rodadas ou menos e que a de cinco é longa; e nos `15.283` combates de 5e do FIREBALL a mediana é `3`.* **A luta vira moedor a partir de seis rodadas, e a `Calamidade` fica uma abaixo.** ***Decisão do Mizuki:*** *"C, decisão do mestre é melhor aqui"* — **o `5` é média, e o mestre corta a luta quando a vitória estiver clara.** *A pesquisa está em `bestiario/09-fase-2/pesquisa/leva-2/`.*

> **⚠ A escada de antes media quantas pessoas o inimigo exigia, com `personagens = fator × 4`, e a `Calamidade` exigia oito.** *Ela passava do teto de seis, fazia toda luta durar três rodadas, e deixava a Expansão, a `Recarga`, a resistência e a cura multiplicarem o encontro sem trava.* **Ela morreu na v0.282, e está no arquivo morto.**

### 4.1 A ficha pronta de cada célula, nos três níveis que a tabela publica

*A vida · o golpe. No `Capanga`, os corpos × a vida de um · o golpe.*

**Nível 10**

| categoria | `×1` | `×2` | `×3` | `×4` | `×5` | `×6` |
|---|---|---|---|---|---|---|
| `Capanga` | `2` × `32` · `10` | `4` × `32` · `10` | `6` × `32` · `10` | `8` × `32` · `10` | `10` × `32` · `10` | `12` × `32` · `10` |
| `Ameaça` | `81` · `17` | `162` · `17` | `244` · `17` | `325` · `17` | `406` · `17` | `487` · `17` |
| `Desastre` | `97` · `19` | `195` · `19` | `292` · `19` | `390` · `19` | `487` · `19` | `585` · `19` |
| `Catástrofe` | `130` · `22` | `260` · `22` | `390` · `22` | `520` · `22` | `650` · `22` | `780` · `22` |
| `Calamidade` | `162` · `23` | `325` · `23` | `487` · `23` | `650` · `23` | `812` · `23` | `975` · `23` |

**Nível 20**

| categoria | `×1` | `×2` | `×3` | `×4` | `×5` | `×6` |
|---|---|---|---|---|---|---|
| `Capanga` | `2` × `55` · `19` | `4` × `55` · `19` | `6` × `55` · `19` | `8` × `55` · `19` | `10` × `55` · `19` | `12` × `55` · `19` |
| `Ameaça` | `137` · `34` | `275` · `34` | `412` · `34` | `550` · `34` | `687` · `34` | `825` · `34` |
| `Desastre` | `165` · `38` | `330` · `38` | `495` · `38` | `660` · `38` | `825` · `38` | `990` · `38` |
| `Catástrofe` | `220` · `42` | `440` · `42` | `660` · `42` | `880` · `42` | `1100` · `42` | `1320` · `42` |
| `Calamidade` | `275` · `45` | `550` · `45` | `825` · `45` | `1100` · `45` | `1375` · `45` | `1650` · `45` |

**Nível 30**

| categoria | `×1` | `×2` | `×3` | `×4` | `×5` | `×6` |
|---|---|---|---|---|---|---|
| `Capanga` | `2` × `78` · `28` | `4` × `78` · `28` | `6` × `78` · `28` | `8` × `78` · `28` | `10` × `78` · `28` | `12` × `78` · `28` |
| `Ameaça` | `197` · `51` | `394` · `51` | `591` · `51` | `787` · `51` | `984` · `51` | `1181` · `51` |
| `Desastre` | `236` · `56` | `472` · `56` | `709` · `56` | `945` · `56` | `1181` · `56` | `1417` · `56` |
| `Catástrofe` | `315` · `64` | `630` · `64` | `945` · `64` | `1260` · `64` | `1575` · `64` | `1890` · `64` |
| `Calamidade` | `394` · `68` | `787` · `68` | `1181` · `68` | `1575` · `68` | `1969` · `68` | `2362` · `68` |

> **⚠ O arredondamento é meio para BAIXO, e ele é declarado porque não é cosmético.** *A saída de um personagem e o golpe-base têm fração de quarto, e as rodadas `2,5` põem células exatamente em `,5`.* **Três lugares calculam isto — a peça, o validador e o gerador do bloco — e cada linguagem arredonda de um jeito:** *o `Math.round` do JavaScript sobe, o `round` do Python vai para o par.*
>
> **⚠ E a vida do corpo do `Capanga` arredonda PARA BAIXO, por inteiro, que é outra regra.** *Um quarto de ponto de vida põe o corpo vivo depois do golpe que devia derrubá-lo.*

### 4.2 As ações — e o `×1` e o `×2` contra condição

**Ele age `N` vezes por rodada, num turno só, pelas `Ações Múltiplas` do livro do Bestiário.** *O `Desastre ×4` age quatro vezes; o `×1`, uma.*

**O inimigo de uma ou duas ações perderia a luta inteira para uma condição que tira ação, e a regra do `×1` e do `×2` é o que segura isso.** ***Decisões do Mizuki, 28/09/2026:*** *"A, poderia ser uma mecanica apenas para combates 1x1-2x1"* · *"n ser garantido seria melhor. Talvez uma habilidade pra rerolar o TR, rolar no começo do turno dnv ao invés do final […] Pq se n a condição fica inutil"*.

> **No `×1`, a condição que tira ação dá ao inimigo um Teste de Resistência no começo do turno dele, sempre com a maestria.** *Passou, ela sai antes de ele agir.*
> **No `×2`, o mesmo Teste de Resistência, com desvantagem.**
>
> *Ele continua precisando falhar no teste para a condição pegar — a decisão da v0.205 fica ("ele precisa passar no teste").* **As condições que tiram ação são as quatro da peça 19 §2.2:** *`Lento`, `Calado`, `Enfeitiçado` e `Atordoado`.*

**A regra devolve as duas células à régua da peça 19 §2.2, e a condição continua valendo perto de duas vezes o dano que ela substitui.** *Um Teste de Resistência antes do turno multiplica o que a condição nega pela chance de ele falhar; o chefe de três ações fica em `2,24×` a `2,39×`, e o filtro de dominância é `3,00×`.*

| o que o inimigo tem | `×1` | `×2` |
|---|---|---|
| nada | `6,43×` a `7,17×` | `3,29×` a `3,59×` |
| **a regra** | `2,25×` a `2,51×` | `1,90×` a `2,07×` |
| o Teste de Resistência normal, com a maestria | `2,25×` a `2,51×` | `1,15×` a `1,26×` |
| o Teste de Resistência normal, sem a maestria | `2,57×` a `3,94×` | `1,32×` a `1,97×` |

*Sem a maestria, o `×1` passa do filtro do nível 10 em diante, porque o Teste de Resistência sem treino falha de `40%` a `55%`; com o Teste de Resistência normal no `×2`, a condição fica quase igual ao dano.* **O reroll dá a mesma conta na primeira rodada; o Teste de Resistência no começo do turno é a forma que ele escreveu, e as de nível `Pesada` já têm o teste, só que no fim do turno.**

> **⚠ Até a v0.281 o `Desastre` não podia descer de `3` ações, pelo piso da régua de condição da peça 19 §2.2.** *Na grade o `×1` e o `×2` têm uma e duas, e a regra acima é o que substitui o piso; do `×3` para cima a régua funciona sozinha.*

### 4.3 ⚠ `N` corpos de `×1` não são um `×N`

**Quatro `Desastre ×1` não valem um `Desastre ×4`: eles cobram `0,75 ×` o que ele cobra.** *A causa é que eles morrem em fila e a saída deles despenca — os quatro entregam tudo enquanto estão de pé, e depois cada vez menos.* **Somar as vidas dá a célula inteira; jogar os corpos separados não dá o mesmo encontro.**

| categoria | `×2` | `×4` | `×6` |
|---|---|---|---|
| `Ameaça` | `0,83` | `0,67` | `0,67` |
| `Desastre` | `0,83` | `0,75` | `0,67` |
| `Catástrofe` | `0,75` | `0,62` | `0,67` |
| `Calamidade` | `0,90` | `0,75` | `0,70` |

*O que `N` corpos de `×1` cobram, contra um corpo de `×N` do mesmo degrau, no nível 30, com a ordem de abate do §4.5.*

### 4.4 O dano se rola em dado, e não em número seco

**O que a ficha publica é o golpe, e o que o mestre rola é o dado dele.**

> **O golpe é `N` dados mais um fixo, com metade do alvo em dado.** *O tamanho do dado se escolhe entre `d4`, `d6`, `d8`, `d10` e `d12` — o que fecha a metade mais limpo, com no máximo **oito** dados na mão.* **Abaixo de `5` o golpe fica em número seco** — um dado balançaria mais que o próprio golpe.

**O precedente é o `Guia do Mestre` de 2014**, que manda traduzir a margem de dano numa expressão de dado.

| categoria, no nível 26 a 30 | o golpe | em dado |
|---|---|---|
| `Capanga` | `28` | `4d6 + 14` |
| `Ameaça` | `51` | `4d12 + 25` |
| `Desastre` | `56` | `8d6 + 28` |
| `Catástrofe` | `64` | `6d10 + 31` |
| `Calamidade` | `68` | `6d10 + 35` |

*O golpe não depende do N: um `Desastre ×1` e um `×6` batem o mesmo `8d6 + 28`, e o `×6` bate seis vezes.* **Quem carrega recurso rola este golpe sem mudança nenhuma:** *o recurso se paga na vida (§6).*

> **⚠ O teto de oito dados não é cosmético.** *Sem ele o otimizador troca `5d8 + 26` por `10d4 + 24`: fecha melhor na conta e é pior na mesa.* ***Pedido do Mizuki, v0.216:*** *"não precisa sustentar pra sempre o `d8`, dá pra usar `d6`, `d4`, `d10`, `d12`, para ajudar nos cálculos".*

### 4.5 O chefe com capangas — cada capanga toma `1 ÷ (rodadas × N)` do chefe

***Ideia do Mizuki:*** *nem todo combate tem mais de um inimigo, e o mesmo encontro pode vir num corpo só ou repartido.* ***E a decisão de 28/09:*** *o `Capanga` "pode sim ser usado […] junto de um chefe".*

> **Cada capanga que entra ao lado de um chefe tira `1 ÷ (rodadas × N)` da vida e do golpe do chefe.** *Até metade do grupo em capangas — `1,5 × N` corpos — a conta é essa, e o encontro cobra o que o chefe sozinho cobraria.*

| célula, no nível 30 | `1 ÷ (rodadas × N)` | com 1 capanga, o chefe fica com | com 2 | com 3 |
|---|---|---|---|---|
| `Desastre ×2` | `16,7%` | `83,5%` | `67,1%` | `50,6%` |
| `Desastre ×4` | `8,3%` | `91,7%` | `83,4%` | `75,2%` |
| `Desastre ×6` | `5,6%` | `94,5%` | `89,0%` | `83,5%` |
| `Calamidade ×2` | `10,0%` | `90,1%` | `80,3%` | `70,4%` |
| `Calamidade ×4` | `5,0%` | `95,0%` | `90,0%` | `85,2%` |
| `Calamidade ×6` | `3,3%` | `96,7%` | `93,4%` | `90,1%` |

*A fração não foi escolhida: ela é a que devolve o que o chefe sozinho cobra, pela simulação do `conferir-bestiario.py`.*

> **⚠ A conta depende de em que ordem o grupo abate, e a ordem está declarada: os capangas primeiro.** *É o que a mesa faz sozinha — o capanga cai num golpe de um personagem.* **E o chefe age primeiro em cada rodada**, *que é a leitura que não esconde uma rodada dele.*
>
> **⚠ A `Ameaça` sai da regra, porque as `2,5` rodadas dela dependem de quem age primeiro.** *Com o chefe agindo primeiro ela age três vezes; com o grupo agindo primeiro, duas.* **Para ela, use a fração do `Desastre` do mesmo N.**

### 4.6 Concentrando, ele derruba alguém — e a métrica que mostra isso não é óbvia

*A vida de referência nesta estimativa é o dano publicado do chefe dividido por 90%. Como o dano já foi arredondado, ela aproxima a média exata dos quatro Caminhos; os PV dos personagens continuam sendo calculados por Caminho.*

**Um `Desastre ×4` concentrando os quatro golpes derruba um personagem na rodada `1,12`.** *No nível 30 ele entrega `672` de dano na luta contra `251` do alvo, e a razão é quase a mesma em todo nível.* **Numa luta de três rodadas ele derruba `2,68` pessoas se concentrar** — não o grupo inteiro, e mais de uma.

| categoria, no nível 30 | rodadas | derruba um na rodada (`×4`) | derruba na luta |
|---|---|---|---|
| `Ameaça` | `2,5` | `1,23` | `0,508 × N` |
| `Desastre` | `3,0` | `1,12` | `0,669 × N` |
| `Catástrofe` | `4,0` | `0,98` | `1,019 × N` |
| `Calamidade` | `5,0` | `0,92` | `1,354 × N` |

**A `Catástrofe` e a `Calamidade` derrubam mais gente do que o grupo tem, se ninguém curar e ninguém cair antes.** *São as lutas severa e extrema, e é para isso que elas existem: a `Calamidade ×4` tira `135%` da vida do grupo em cinco rodadas, e conta com a cura (§4.7) para não matar.*

> **⚠ A métrica errada é "quantas rodadas ele leva para derrubar o GRUPO".** *Até a v0.200 ela dava `14` contra uma luta de `3,7`, e escondia que ele derrubava uma pessoa por luta, no último segundo.* **A conta desta edição dá `2,68` pessoas:** *o d20 de 2014 derruba `2,56` a `2,70` numa luta de três rodadas, e o chefe solo do Pathfinder 2e derruba perto de `2,8`.*
>
> **⚠ E é o modelo sem ATRITO, que é o modelo desta peça inteira: quem cai continua contando na saída do grupo.** ***Decisão do Mizuki na v0.205: fica assim.*** *"Um inimigo focar um único player vai acabar matando mesmo, acho que todo sistema rola isso — o mestre não vai querer normalmente focar também."*
>
> **⚠ E a escada inteira é mais pesada que a dos outros sistemas.** *A pressão do `Desastre` (`66,9%` da vida do grupo, no nível 30) é a da luta severa-a-extrema do Pathfinder 2e e do D&D 2024, cuja moderada tira de `20%` a `48%`.* **Isso vem da decisão da v0.205, e a razão entre os degraus é a deles:** *a `Calamidade` é o dobro do `Desastre`, como a extrema é o dobro da moderada.*

### 4.7 O que a CURA do grupo faz com o encontro — e ela não faz o que parece

***Pedido do Mizuki na v0.203:*** *"um inimigo tem que ser calculado pra todas as situações, para fazer uma média. Vai ter grupo que vai ter 1 healer, vai ter o grupo que não vai ter healer, vai ter o grupo onde não tem healer mas cada um tem `Circulação` ou pelo menos `Energia Reversa`."*

> **Registro histórico da medição de cura da v0.203.** A composição com Energia Reversa curando outra pessoa não é permitida na edição jogável atual. Os números abaixo ficam como registro daquela análise e não foram recalibrados como encontros da edição atual.

**A linha do manual foi calibrada contra um grupo que não cura.** *Medindo contra os que curam, o resultado sai ao contrário do esperado. A tabela é a do `Desastre ×4`, que é a linha do manual.*

| composição, no nível 30 | luta | o chefe entrega | a cura repõe | líquido | do grupo |
|---|---|---|---|---|---|
| sem cura nenhuma | `3,00` | `657` | — | **`657`** | `68%` |
| um suporte, área ou alvo único conforme o turno | `4,00` | `876` | `45` | `832` | `86%` |
| um só com `Energia Reversa` segurando o grupo | `4,00` | `876` | `126` | `750` | `77%` |
| sem suporte, os quatro se curando em rodadas alternadas | `6,00` | `1314` | `135` | **`1179`** | `121%` |

**Toda composição que cura sai PIOR que a que não cura, e o motivo é economia de ação.** *Curar gasta a ação que causaria dano; menos dano faz a luta durar mais; e cada rodada a mais é mais uma rodada do chefe.* **Ele entrega `219` por rodada e nenhuma cura de alvo único do sistema repõe isso** — um atacante que para de bater abre mão de `78,75`.

> **A única que ganha a troca é a cura em ÁREA**, porque ela multiplica por alvo: quatro alvos vezes `45` da `Onda` de Classe 7 passam dos `78,75`.
>
> **⚠ E é por isso que a linha do manual NÃO desconta cura.** *Descontar deixaria o chefe mais fraco justamente contra os grupos que já sofrem mais.*

> ***Decisão do Mizuki:*** *"cura deve ser feita para segurar um pouco de dano, tirar o cara de morrer no próximo tapa — semelhante ao d20, onde cura não é feita pra deixar uma pessoa full."* **Levantar alguém de `0` gastando a Ação Padrão é empate exato; na Ação Bônus o saldo vira `+51,8`**, e é essa a metade que a aptidão `Circulação` da peça 11 §6 existe para dar.

## 5. O `Capanga` — o esquadrão de `2N`

***Decisões do Mizuki, 28/09/2026:*** *"Capanga, ele pode sim ser usado contra players em multiplas quantidades ou junto de um chefe"*, e a forma **B** — os `2N` corpos com meio golpe.

**O `Capanga ×N` é um esquadrão de `2N` corpos que caem num golpe cada.** *O grupo de N derruba N corpos por rodada, então o esquadrão dura duas rodadas contra qualquer N.*

> **A vida de um corpo é a saída de um personagem por rodada, para baixo.** *É o que UM personagem derruba num golpe.*
> **O golpe de um corpo é metade do golpe-base**, meio para baixo. *Cada corpo age uma vez por rodada.*

**Com meio golpe o esquadrão cobra `33,5%` da vida do grupo em duas rodadas no nível 30, em todo N, que é o degrau de baixo.** *Com o golpe inteiro, os mesmos corpos cobrariam o que um `Desastre` cobra, e o `Capanga` sairia mais caro que a `Ameaça`.* **O golpe dele fica abaixo da banda de `20%` a `28%`, e a banda vigia só os chefes.**

> **Um `Desastre ×N` vale `3N` capangas do mesmo nível.** *O esquadrão entrega os golpes cedo e acaba cedo; o chefe entrega os mesmos em três rodadas.*

| quantos capangas cobram o que a célula cobra | `×1` | `×2` | `×3` | `×4` | `×5` | `×6` |
|---|---|---|---|---|---|---|
| `Ameaça` | `3` | `5–6` | `8–9` | `11–12` | `13–15` | `16–18` |
| `Desastre` | `3` | `6` | `9–10` | `12` | `14–15` | `17–18` |
| `Catástrofe` | `4` | `7–8` | `11–12` | `15–16` | `18–20` | `22–24` |
| `Calamidade` | `4–5` | `9` | `13` | `17–18` | `21–25` | `26–27` |

*Nas sete faixas da tabela do manual; onde a faixa muda o número, a célula traz os dois.* **A simulação roda no validador, e é ela que prova a igualdade.**

> **E ele precisa de uma trava para não concentrar:** *no máximo `3` corpos do mesmo esquadrão atacam o mesmo alvo por rodada, e do segundo em diante o golpe sai pela metade.* **A trava não encolhe o esquadrão** — *os corpos continuam entregando tudo, só não no mesmo alvo.*

> **⚠ O `Capanga` da escada de antes eram oito corpos com o golpe da `Ameaça`,** *e oito deles valiam um `Desastre`.* **Com o golpe inteiro ele cobrava o orçamento de um chefe, e não o do degrau de baixo.**

### 5.1 A linha do nível 2 estava um ponto fora, e um ponto era uma rodada

**A seção `Inimigos` do manual escreve a própria regra:** *o chefe sozinho tem cerca de **três vezes** o dano de rodada do grupo em vida, "e é isso que faz a luta contra ele durar três rodadas".* **Seis das sete linhas cumpriam isso exato; a do nível 2 publicava `115` contra os `114` que a regra pede.**

> **⚠⚠ E um ponto de vida custava uma rodada inteira do chefe.** *Com `115` a luta dura `3,03` rodadas, e rodada é inteira na mesa: o chefe age quatro vezes e o encontro cobra `89%` da vida do grupo, contra os `68%` que as outras seis cobram.* **A faixa virou `105 a 123`, com o meio em `114`.** *Manual na `v7.25`; a checagem `5.2` do validador guarda isso.*

**É o mesmo defeito que a vida do corpo do `Capanga` teria sem arredondar para baixo.** *Com o piso, o corpo do nível 2 tem `9` de vida — `38 ÷ 4` dá `9,5`, e fica `9`.*

## 6. O que ele carrega além dos números — e se paga na vida

***Decisão do Mizuki:*** **o inimigo se monta com as mesmas peças que um personagem, menos o Caminho.** *Na obra a maior parte do que se enfrenta é feiticeiro, e feiticeiro tem técnica, tem aptidão e tem Passiva.*

| ele tem | de onde sai |
|---|---|
| refino | a curva do `meio a meio`, peça 11 §3 |
| aptidões e Passivas | o catálogo da peça 11, o mesmo que o jogador usa, e uma por escolha de marco, pelo §3.2 |
| técnica, com Fundamento | o manual, quando ele é feiticeiro ou maldição de técnica |
| Legado, ferramenta, objeto | as peças 13, 16 e 21, quando a ficção pedir |

| ele não tem | por quê |
|---|---|
| Caminho e Trilha | as duas entregam por marco de campanha, e o inimigo não sobe de nível |
| poço de PE | o §6.1 |
| Origem | a peça 9 é a máquina de criação de quem senta na mesa |

***Decisões do Mizuki, 28/09/2026:*** *"Faz mais sentido ser B, entendo a A, mas vc tem q pensar q como fica o inimigo Calamidade? n tem pra aonde subir, dar expansão e essas mecancias deixam o encontro mais letal, mas n necessariamente deixa ele impossivel do grupo ganhar"* · *"um dragão que tem baforada n tem dano reduzido em comparação a um inimigo que tenha so ataques do mesmo nd"*.

> **O que o inimigo carrega e muda o encontro se paga na vida: `a vida ÷ o multiplicador`. O golpe não se move.** *A célula fica do tamanho que o §4 diz, e o encontro fica mais letal no pico e mais curto.*

**Os outros sistemas fazem o mesmo com o golpe.** *Nos `331` blocos do SRD 5.2, no mesmo ND, o monstro com `Recarga` tem a rotina de ataque `× 1,05` da do monstro que só ataca, a vida `× 0,94` e a CA `+0,9`; o GM Core do Pathfinder 2e dá à baforada o dano da tabela de área e não manda baixar golpe, vida nem outro número.* **Nos dois a baforada se paga pela economia de ação, e a `Recarga` daqui também: ela come as ações do turno (§6.5).** *O que sobra é o ganho da área, e ele sai da vida. A medida está em `bestiario/09-fase-2/pesquisa/leva-2/conta-recarga-dnd.py`.*

> **⚠ Até a v0.281 o que o inimigo carregava multiplicava o fator, e o encontro crescia.** *"A Expansão aumenta o encontro, e não se compensa", da v0.229, caiu com a resposta de 28/09: a `Calamidade` não tinha para onde subir.*

### 6.1 O inimigo não conta PE, e a cota de dano é o orçamento dele

**Tudo que ele faz sai do golpe da ficha.** *Uma técnica que causa dano entrega aquele golpe e não mais; uma que não causa dano troca parte da cota por outra coisa.* **A cota de uma rodada são os N golpes dele.**

**O precedente é do `Guia do Mestre` de 2014, e ele é explícito:** *o que um monstro tem é dano por rodada, e como esse dano se divide em ataques é livre.* **Contar PE de inimigo criaria uma segunda economia que só o mestre opera**, e ela responderia diferente em duas mesas.

> **Isso é a regra de ouro nº 6 pelo outro lado.** *O personagem tem um teto de saída por rodada e paga em PE para chegar nele; o inimigo tem o mesmo teto escrito direto, sem a moeda no meio.*

### 6.2 E existe inimigo sem energia nenhuma

**Ele não tem refino, aptidão nem técnica, e a cota de dano vem do corpo.** *É a forma da Restrição Celestial pelo ramo da Maki, do lado de lá da mesa* — **e a ficha não muda de tamanho por causa disso:** a vida e o golpe continuam saindo da célula, porque a célula mede o que o encontro custa, e não de onde ele tira força.

> **⚠ E aqui a fronteira da obra encosta na mecânica sem virar número.** *O que separa uma maldição de grau 2 de uma de semi-grau 1, na classificação da obra, é saber usar técnica.* **A ficha carrega essa linha na coluna `técnica`**, e o rótulo do §2 fica legível sem entrar em conta.

### 6.3 Resistência pontual e proteção ampla

**Resistência a até `2` tipos fixos, no total da criatura, não desconta PV.** Um grupo completo continua pago, mesmo quando seus tipos são escritos separadamente. A resistência continua reduzindo à metade o dano daqueles tipos; a isenção é de preço, não de efeito. Imunidade e vulnerabilidade seguem suas regras próprias.

**Pendente:** Três ou mais tipos mistos que não completem um grupo continuam sem preço definido; não aplique a isenção a esse caso.

**A peça 19 §4 divide os catorze tipos de dano em três grupos e diz quanto cada um pesa no que um alvo recebe** — `Físicos 60%`, `Elementais 30%`, `Especiais 10%`. **Resistir corta pela metade o que entra por aquele grupo, e isso sobe a vida efetiva do inimigo.** As colunas de resistência e imunidade são os divisores de PV cobrados. A linha de um tipo usa a isenção aprovada; dois tipos fixos no total também não descontam PV. O peso de 20% permanece hipótese para a imunidade e a vulnerabilidade dessa linha, não uma frequência medida:

| grupo | peso | resistência | imunidade | vulnerabilidade |
|---|---|---|---|---|
| `Físicos` | `60%` | **`1,43×`** | **`2,50×`** | `0,62×` |
| `Elementais` | `30%` | `1,18×` | `1,43×` | `0,77×` |
| `Especiais` | `10%` | `1,05×` | `1,11×` | `0,91×` |
| um tipo só | `20%` | `1,00×` | `1,25×` | `0,83×` |

> **Resistência ao grupo `Físicos` divide a vida crua por `1,43`.** *Aos `Elementais`, por `1,18`; aos `Especiais`, por `1,05`.*
> **Imunidade a `Físicos` divide a vida crua por `2,50`.** *Aos `Elementais`, por `1,43`; aos `Especiais`, por `1,11`.*
> **A vulnerabilidade é `1,00×`: não cobra e não devolve.** *O dano daquele tipo dobra contra ele, e nada mais na ficha muda.*
> **Ser imune a uma condição que rouba ação do inimigo, ou que dá desvantagem nos ataques dele, divide a vida crua por `1,20`. Qualquer outra condição custa `1,00×`.**
>
> **O inimigo que não usa voz não é imune ao `Calado`, e não paga o `1,20`.** *O `Calado` só cala Selo ou habilidade que precise de voz (peça 19 §3.2, v0.277): contra quem não tem nada disso ele não tira ação, então é "qualquer outra condição", a `1,00×`. A imunidade — e o preço dela — só existe para quem usa voz e não se cala.*

**Um `Desastre ×4` imune a `Físicos` sai com `378` de vida no nível 30.** O divisor supõe a distribuição de dano acima. Um grupo que só cause dano Físico não consegue feri-lo por esses ataques; um grupo que use outros tipos enfrenta os PV reduzidos. A conta não garante a mesma duração para toda composição.

**O mesmo `Desastre ×4` resistente apenas a Fogo conserva `945` PV.** Acrescentar um segundo tipo fixo conserva esses PV, desde que o total não forme um grupo completo. A resistência continua podendo prolongar a luta.

> **⚠ A coluna `vulnerabilidade` é conta de vida efetiva, e não preço.** *Ela diz quanto a luta encurta se o grupo inteiro bater naquele tipo, e a ficha não sabe o que o grupo carrega — por isso não cobra nem devolve.* **`4` de `4` sistemas medidos no Bestiário têm vulnerabilidade, e nenhum mexe no custo de encontro por ela.**

**A referência é o cálculo de PV efetivos do `Guia do Mestre` de 2014.** Lá ele estima dificuldade sem alterar os PV reais nessa etapa. Aqui, dividir os PV para conservar uma dificuldade escolhida é adaptação do Projeto M. A isenção pontual foi aprovada pelo Mizuki após a revalidação em `bestiario/09-fase-2/pesquisa/REVALIDACAO-resistencia-2026-09-28.md`.

> **⚠ E toda esta régua está pendurada num palpite, que a peça 19 §4 declara com todas as letras:** *o peso dos três grupos é previsão, `04-playtest/` está vazia, e ele é "o número que decide quanto vale toda resistência do sistema".* **Quando a mesa corrigir o peso, os multiplicadores cobrados devem ser recalculados.** A isenção pontual é decisão autoral, e não resultado dessa fórmula.

### 6.4 A Expansão de Domínio do inimigo — ela divide a vida por `1,92`

***Decisão do Mizuki: a Expansão do inimigo é a do jogador, escalonada para grupo.*** *A máquina inteira mora no manual, e nada dela é reescrito aqui.*

**Ela não acrescenta dano nenhum, e é isso que faz o preço dela ser fácil de achar.** *Pelo §6.1 tudo que o inimigo faz sai da cota, e o Acerto de um domínio não é exceção.* **O que muda é quanto dela CHEGA.**

> **Fora do domínio o inimigo acerta `52%` — é a banda de `50%` a `55%` que o §3.1 publica.** *Dentro, o Acerto acontece: sem rolagem e sem Teste de Resistência, como o manual escreve.*
> **Então a Expansão completa multiplica a saída efetiva dele por `1 ÷ 0,52`, que é `1,92 ×`, e a vida crua dele se divide por `1,92`.**

**Um `Desastre ×4` com Expansão sai com `492` de vida no nível 30, e a luta dura `1,56` rodada.** *No domínio ele acerta tudo o que tenta, e o grupo que não sair dali leva a luta inteira em pouco mais de uma rodada e meia.* **É a leitura dele de 28/09: mais letal, e não impossível.**

| categoria | a luta sem Expansão | com Expansão completa |
|---|---|---|
| **`Ameaça`** | `2,5` | `1,30` |
| **`Desastre`** | `3` | `1,56` |
| **`Catástrofe`** | `4` | `2,08` |
| **`Calamidade`** | `5` | `2,60` |

> *Até a v0.281 ela multiplicava o fator por `1,92`, e uma `Calamidade` com Expansão exigia `15,4` feiticeiros.* **A decisão da v0.229 — "o acerto garantido e a expansão, vão virar pro lado do inimigo […] é esperado o encontro ficar maior nesse caso" — caiu com a resposta de 28/09.**

**A incompleta não custa nada nesta régua.** *O manual diz que o Acerto dela "resolve por rolagem, como um feitiço"* — **sem a garantia não existe o `1,92 ×`**, e o que ela dá é o Efeito, que não é dano. *Qualquer categoria pode ter uma.*

**E abrir não custa rodada ao inimigo, apesar de custar ao jogador.** *O manual cobra a rodada inteira e `6 ×` a maior Classe de PE; o inimigo não conta PE pelo §6.1, e o Acerto acontece no momento em que ele abre.*

***Decisão do Mizuki: os gates são os do jogador.*** **A completa abre no nível `14` com refino `5`, e a Expansão sem Barreiras pede refino `10`**, *como o manual escreve.*

> **É o gate que faz o `1,92` valer a luta toda.** *O manual põe a duração em metade do refino, e na curva do `meio a meio` o nível `14` dá refino `6` e `3` rodadas de domínio, contra a luta mais longa com Expansão, a da `Calamidade`, de `2,60`.* **Dali para cima ela só cresce.**

#### A Expansão sem Barreiras do inimigo — o mesmo `1,92`, e o refino no teto

**Ela divide a vida pelo mesmo `1,92`.** *O preço vem do Acerto garantido, e ele é garantido nos dois modos, com a mesma duração.* **O que muda fica fora do eixo de dano, e por isso fica declarado e não cobrado:**

- **quem não tem energia amaldiçoada** só leva o Acerto se ele alcança o que não tem energia — *contra um grupo com um Restringido ela entrega menos;*
- **não existe casca** para quem está de fora quebrar;
- **contra o domínio de um personagem**, além da disputa de sempre, o Acerto que fere bate na barreira dele por fora;
- **o raio de `200 m`** pega a cena inteira, e a completa pega só quem estava no raio dela.

***Decisão do Mizuki: o gate é o do jogador, e o refino acima da curva é desvio com causa escrita.*** **Pela curva do `meio a meio`, o inimigo só chega a refino `10` no nível `26`.** *Um chefe da obra que abre sem barreira abaixo disso tem a obra como causa.* **A especialização em `Ocultismo` entra no bloco como a perícia `Ocultismo`.**

> **O refino acima da curva se paga na vida, pela Defesa.** *A proteção é `1/3 do refino + 1`, pela peça 11 §6, e o §3.2 diz quanto um ponto de Defesa custa.*

| marco | refino da curva | Defesa ganha subindo a `10` | a vida |
|---|---|---|---|
| nv `14` | `6` | `+1` | `× 0,90` |
| nv `18` | `7` | `+1` | `× 0,90` |
| nv `22` | `9` | `+0` | `× 1,00` |

*O desvio mexe na Defesa, na duração e no raio do domínio, e em nada mais: o refino não entra no acerto, na CD nem no golpe.*

#### O Rescaldo do inimigo, e a `Regravação`

***Decisão do Mizuki, v0.242: o inimigo carrega a corrente inteira do jogador.*** *A `Energia Reversa`, a `Circulação` e a `Regravação` saem do catálogo da peça 11, com os gates e os marcos de lá, e se pagam pelo §6.5.*

**O Rescaldo vale para ele como vale para o jogador:** *quando o domínio acaba, de qualquer jeito, a técnica queima pelo resto da cena.*

> **A cota fica, pelo §6.2, e as ações dele viram golpes de corpo.** *O acerto passa a ler o atributo com que ele bate, e o que era técnica sai junto, inclusive uma `Recarga` de técnica.*

**A corrente fecha no nível `26` para o inimigo:** *a `Energia Reversa` no `18`, a `Circulação` no `22` e a `Regravação` no `26`.* **Ela custa `2` pontos de atributo**, *os das escolhas do `18` e do `26`; a do `22` é de refino, e a aptidão vem com ela.*

> *Sem a regra de marco do §3.2 ela fecharia no `22`, com a `Circulação` e a `Regravação` no mesmo nível.*

**Regravar custa a Ação Bônus e o teto da `Circulação`, na cota da rodada em que ele regrava.** *É a porta da aptidão, com o câmbio de `5,14` por PE.*

| a regravação no nível 30 · `10` PE = `51,4` | `Desastre ×1` | `Desastre ×4` | `Calamidade ×1` | `Calamidade ×4` |
|---|---|---|---|---|
| da cota da rodada | `92%` | `23%` | `76%` | `19%` |
| espalhada na luta | `30,6%` | `7,6%` | `15,1%` | `3,8%` |

**As marcas são as da peça 11, com a Inteligência.** *A tabela mora lá, e o inimigo só alcança a linha do nível 26 ao 30.* **Reabrir não mexe na vida:** *o `1,92` já supõe o domínio de pé a luta inteira.*

### 6.5 O catálogo do jogador na ficha do inimigo

***Decisão do Mizuki:*** *"dá pra deixar ser que nem do sistema pra player, mas rebalancear."* **O inimigo carrega as entradas que o jogador já tem, e o que muda é a moeda em que elas se pagam.**

| o que ele carrega | onde ela se paga |
|---|---|
| **técnica e feitiço** | o **orçamento de feitiço** de uma ação dele, e o Fundamento faz o resto |
| **aptidão e Passiva com custo por rodada** | a **cota de dano por rodada**, nas rodadas em que ela está ligada |
| **o que muda o encontro** — `Intervenção`, `Recarga`, cura de Reação, resistência, Expansão | **a vida**, dividida pelo multiplicador |

**A régua é a do `Guia do Mestre`, e o passo 13 escreve ela entre parênteses:** *as características de um monstro "não mudam realmente as estatísticas" dele — elas mexem na vida efetiva, no dano efetivo ou na CA efetiva.*

#### A técnica: o golpe dele é o orçamento do feitiço

***Levantado pelo Mizuki:*** *"se for seguir próximo da criação de ficha normal, um feitiço em área vai ter menos dados para poder comprar condição."* **É por isso que a técnica do inimigo não precisa de preço próprio: o Fundamento já cobra por área, por condição e por Melhoria, em ponto de feitiço.**

> **O orçamento de feitiço de uma ação é o golpe dela dividido por `4,5`.**
> **E o preço de cada Melhoria usa a maior Classe que cabe nesse orçamento.** *Decisão do Mizuki, v0.230: numa ação de `14,9` pontos a Classe é a `4`, e uma `Leve` custa `2`.*

| pontos por ação | `Capanga` | `Ameaça` | `Desastre` | `Catástrofe` | `Calamidade` |
|---|---|---|---|---|---|
| nível 2 | seco | seco | seco | seco | seco |
| nível 5 | seco | seco | seco | seco | seco |
| nível 10 | seco | `3,8` | `4,2` | `4,9` | `5,1` |
| nível 15 | `3,1` | `5,8` | `6,2` | `7,1` | `7,6` |
| nível 20 | `4,2` | `7,6` | `8,4` | `9,3` | `10,0` |
| nível 25 | `5,3` | `9,6` | `10,4` | `11,8` | `12,7` |
| nível 30 | `6,2` | `11,3` | `12,4` | `14,2` | `15,1` |

*O golpe entra aqui como a ficha imprime ele. Ele não depende do N.*

**`seco` é o piso: o menor feitiço do manual é a `Classe 1` e custa `3` pontos**, que são `13,5` de dano. *Abaixo disso o inimigo não monta feitiço nenhum — ele bate, e o golpe dele sai como o §4.4 manda.*

**A maior ação de inimigo do sistema é `15,1` pontos — a `Calamidade` do nível 30 —, e o teto do jogador naquele nível é `24`.** *Uma ação de inimigo é `63%` do maior feitiço que um personagem monta no mesmo nível, e ele compensa em quantidade: age N vezes por rodada.*

> **⚠ E é aqui que a condição do inimigo se resolve, sem moeda nova.** *Comprar condição dentro de um feitiço custa ponto, e ponto gasto em condição é dado que não foi comprado.* **A régua da peça 19 §2.2 vale dos dois lados da mesa desde a v0.201.**

#### A aptidão: ela come a cota, e só nas rodadas em que está ligada

**O jogador paga a aptidão em PE por rodada enquanto ela está de pé. O inimigo não conta PE pelo §6.1, então ele paga a mesma coisa na cota — e paga pelas mesmas rodadas.** *O câmbio tem dono: `+1` PE por rodada vale `5,14` de dano por rodada, pela peça 5 §4.*

> **`1` PE por rodada = `5,14` da cota de dano por rodada, contado só nas rodadas em que a aptidão está ligada.**
> **O teto é a cota daquela rodada** — ninguém gasta o que não tem. *Acima dele a aptidão não cabe naquela célula, e o mestre sobe o N ou tira a aptidão.*
>
> **Erguer custa a maior Classe em PE, toda vez, desde a v0.272** — *na `Cesta Oca de Vime`, no `Domínio Simples`, na `Pétala` e, desde a v0.273, na `Extensão de Domínio`, pela peça 11 §6.5.* **No inimigo, erguer uma vez por luta entra na cota repartido pelas rodadas dela:** `maior Classe × 5,14 ÷ rodadas` por rodada, somado ao PE de rodada.

**A mesma aptidão pesa N vezes menos num `×N`, porque a cota são os N golpes.**

| ligada a luta inteira, no nível 30 | `Desastre ×1` | `Desastre ×4` | `Calamidade ×1` | `Calamidade ×4` |
|---|---|---|---|---|
| `Cesta Oca de Vime` · só erguer | `21%` | `5%` | `11%` | `3%` |
| `Pétala` · erguer, e `1` PE fixo | `31%` | `8%` | `18%` | `5%` |
| `Domínio Simples` · erguer, e `2` PE fixos | `40%` | `10%` | `26%` | `6%` |
| `Extensão de Domínio` · erguer, e `1,5 ×` maior Classe | `122%` | `31%` | `94%` | `23%` |

**No nível 30 um `Desastre ×1` não carrega a `Extensão de Domínio`: ela custa `122%` da cota dele.** *A partir do `×2` ela cabe.*

> ***O `1,5 ×` arredonda para cima, como tudo o que se paga (peça 1 §5.4), desde a v0.274.*** *É o que a peça 11 cobra do jogador: `2` PE por rodada na Classe 1 e `11` na Classe 7.*

> **⚠ E contar por luta em vez de por rodada ligada estaria errado, porque as quatro anti-domínio são pura resposta.** *Elas valem **zero** contra um grupo que não abre domínio.* **O jogador liga quando o domínio abre; o inimigo, cobrado por luta, pagaria pelas rodadas em que ela não fez nada.**

#### A que sai de graça, e o número que prova isso

**Esta não muda a cota — ela muda a FORMA em que ela chega: em que rodada.**

> **Habilidade guardada, `1 ×` por luta.** *Ela entrega o dobro de uma rodada e deixa as outras menores: num `Desastre ×4` do nível 30 são `440` numa e `110` nas outras duas, e o total é `660`, os três golpes de rodada da célula.*

#### A `Intervenção` — a ação fora do turno, e o que ela custa

**O inimigo com `Intervenção` carrega três por luta.** *Cada uma é usada uma vez só, no máximo uma por rodada, logo depois do turno de outra criatura.* **A primeira bate — um pouco menos que uma ação normal; a segunda e a terceira mudam o campo em vez de causar dano.**

> **Ela abre quando `N × orçamento ≥ 4`:** *a `Ameaça` só no `×6`, o `Desastre` a partir do `×4`, a `Catástrofe` a partir do `×3` e a `Calamidade` a partir do `×2`. O `Capanga` não tem.*
> **Ela é ação EXTRA, por cima das N, e se paga na vida:** `vida ÷ (1 + 0,75 ÷ (rodadas × N))`.

| a vida se divide por | `×1` | `×2` | `×3` | `×4` | `×5` | `×6` |
|---|---|---|---|---|---|---|
| `Ameaça` | — | — | — | — | — | `× 1,050` |
| `Desastre` | — | — | — | `× 1,062` | `× 1,050` | `× 1,042` |
| `Catástrofe` | — | — | `× 1,062` | `× 1,047` | `× 1,038` | `× 1,031` |
| `Calamidade` | — | `× 1,075` | `× 1,050` | `× 1,038` | `× 1,030` | `× 1,025` |

***As duas ideias fixas são do Mizuki:*** *"Inimigo tem ações"* e *"Intervenções são ações extras em meio aos turnos dos alvos. Nenhum sistema come ação do turno para ter essas 'intervenções', e é por um motivo."* ***E os exemplos de 28/09:*** *"n faz sentido uma ameaça ter ação lendaria, mts vezes, no máximo a feita pra 6 pessoas, diferente de um DESASTRE, ele poderia ja ter numa ficha de 4x1"*. **O `0,75` saiu da forma que o campo constrói:** *medidas `9` villain actions em `3` criaturas `Solo` do Draw Steel, a primeira abre com dano e as outras duas mudam o campo — `0,75` de ação extra por luta.*

#### A área — uma ação por rodada, e a `Recarga` não conta

> **No máximo `1` das ações dele por rodada pode ser em área. Ação de `Recarga` não conta nessa cota.** *Vale em toda célula, e não muda com o nível.*

**Com `1` ação em área, todo mundo leva perto de metade da vida e a luta continua sendo uma luta; com `2`, o alvo termina a luta com `0,3%` de vida.** *E o `2,68` do §4.6 não existe em área: concentrando, a queda é uma curva; em área, é um penhasco.*

#### A `Recarga` — ela come o turno, e bate `2,5` golpes em cada alvo

***Decisões do Mizuki, 10/09 e 14/09/2026:*** *"ela consome multiplas ou todas as ações do turno do inimigo para fazer só aquela ação. Porque o inimigo tem sempre de decidir entre, 'fazer o multi ataque' ou 'a baforada', nunca os dois, semelhante a dnd"* · *"2,5 vez o golpe, causar +- uns 60% da vida média"* · *"mestres gostam de ter mais dados, da a sensação de RNG q é positiva"*, em `d12`.

> **A `Recarga (5-6)` sai uma vez e volta no começo do turno dele com `5` ou `6` no `d6`. Ela come as ações múltiplas do turno — não come a `Intervenção`, a Ação Bônus nem a Reação.**
> **Ela é em área, e cada alvo leva `2,5 ×` o golpe na falha do Teste de Resistência e metade no sucesso.** *Ela rola em `d12`, com dois terços do dano em dado e o resto fixo, sem o teto de oito dados do golpe.* **Um golpe de `55` vira `137`, que é `14d12 + 46`.** *Quando dois `d12` já passam de dois terços, ela rola como o golpe do §4.4.*

**O `2,5 ×` se mede na vida de quem leva.** *O golpe fica entre `20%` e `28%` da vida de um personagem do nível, então a `Recarga` tira de `50%` a `70%` dela.* **Medido em três sistemas, na `bestiario/04-fase-1/fila/MEDIDA-a-recarga-contra-a-vida.md`:** *a baforada do D&D 2024 no topo tira `42%`, a área limitada do Pathfinder 2e tira `29%` a `32%`, e a `Villain Action` do Draw Steel tira `15%`.*

**E ela se paga na vida, pelo método do `Guia do Mestre` de 2014** *(capítulo 9, página 278): o dano de um monstro é a média das rodadas da luta, e uma área conta como se pegasse metade das pessoas.* **Aqui a mesa são as N pessoas da célula, então a rodada de `Recarga` vale `2,5 × (N ÷ 2) ÷ N = 1,25` da rodada comum, em todo N:**

```
os disparos = 1 + (rodadas − 1) ÷ 3
o multiplicador = [disparos × 1,25 + (rodadas − disparos)] ÷ rodadas
```

| categoria | `Ameaça` | `Desastre` | `Catástrofe` | `Calamidade` |
|---|---|---|---|---|
| a vida se divide por | `× 1,15` | `× 1,14` | `× 1,12` | `× 1,12` |

*O `Capanga` fica de fora: o esquadrão é a forma dele.* **Os disparos saem do `d6`:** *ela sai na primeira rodada e volta com chance de um terço em cada começo de turno.*

> **A `Recarga` não passa pelo orçamento de feitiço.** *O dano dela sai do golpe, então a forma da área não gasta ponto: técnica usa a Forma do Fundamento, e ataque natural usa a área natural logo abaixo.*

#### A área natural — a cobertura sai do nível

**Nem todo ataque em área vem de técnica.** *O sopro, o rugido, o chão que cede — são naturais, e não passam pelo Fundamento.* **A cobertura deles sai do nível, e é uma só por faixa; a forma é o jeito de gastar ela:**

| nível | cobre | `Esfera` | `Cone` | `Retângulo` — qualquer `A × B` que dê a cobertura |
|---|---|---|---|---|
| `2`–`8` | `13` quadrados | raio `3 m` | `7,5 m` | `4×3` · `6×2` · `7×2` · `12×1` |
| `9`–`16` | `28` quadrados | raio `4,5 m` | `10,5 m` | `6×5` · `7×4` · `9×3` · `13×2` |
| `17`–`24` | `50` quadrados | raio `6 m` | `15 m` | `7×7` · `8×6` · `9×5` · `10×5` |
| `25`–`30` | `113` quadrados | raio `9 m` | `22,5 m` | `11×11` · `11×10` · `12×9` |

*O quadrado é o da grade do §3.3, e o pior erro de arredondamento nas doze células é `12,5%`.*

> **Ela resolve como a área do Fundamento: Teste de Resistência contra a CD dele, o golpe da ação na falha e metade no sucesso.** *O `Cone` sai sempre do corpo dele, e a largura em qualquer ponto é igual à distância até ele; a `Esfera` e o `Retângulo` saem do corpo dele ou de um ponto no alcance.*

**Ela é de graça, pelo mesmo motivo do tamanho:** *o preço da área já foi fechado supondo que ela pega a mesa inteira, e a trava de uma ação em área por rodada é quem segura ela.* **E a trava conta por ESQUADRÃO:** *os corpos de um `Capanga` fazem uma ação em área por rodada juntos, e os outros batem normal.*

> *Os raios são os quatro primeiros degraus da escada de esfera do manual, e crescem `9,00 ×` do nível 2 ao 30 — o mesmo crescimento dos dez dragões do D&D 2024, do Jovem ao Ancião. A resolução por Teste de Resistência foi martelada pelo Mizuki em 11/09/2026.*

#### A `Energia Reversa` e a `Circulação` — as duas curas da corrente

**Para a cura de ação e as partes destrutíveis, use os PV-base da célula, antes dos ajustes de papel, atributos e recursos.** Calcule essa referência por `rodadas × N × a saída de um personagem`. Nessas duas contas, mantenha as frações até arredondar o resultado para baixo; não use os PV já arredondados da ficha. A cura de Reação da Circulação continua seguindo seu próprio dado e teto.

> **No inimigo, a cura de ação da `Energia Reversa` é o empate da troca ruim logo abaixo:** *os PV-base da célula ÷ as rodadas ÷ N, arredondando para baixo, no lugar de uma ação — que é a saída de um personagem por rodada.* **Ela não cobra nada**, *porque curar o empate não ganha nem perde.*

***Decisão do Mizuki, v0.242:*** *"Deixa a cura da ação bônus virar reação, fica como uma mudança em comparação a player."*

> **A cura de Ação Bônus da `Circulação` vira Reação, quando ele sofre dano.** *O dado continua `d4`, e o teto continua o da `Circulação`.* **A Reação que cura não serve para o ataque de oportunidade, o `Bloquear`, o confronto de Expansão nem a anti-domínio.**

**Ela não gasta ação, então a porta é a da vida efetiva, e a vida crua se divide por ela.** *Com uma cura por rodada, a luta de `L` rodadas vira `L ÷ (1 − L × cura ÷ vida)`; como a vida é `L × N ×` a saída de um personagem, o `L` sai da conta, e o multiplicador é o mesmo em todo degrau.*

| a Reação, uma vez por rodada | cura | `×1` | `×2` | `×3` | `×4` | `×5` | `×6` |
|---|---|---|---|---|---|---|---|
| do nível 22 ao 25 · `9d4` | `22,5` | `× 1,49` | `× 1,20` | `× 1,12` | `× 1,09` | `× 1,07` | `× 1,06` |
| do nível 26 ao 30 · `10d4` | `25,0` | `× 1,47` | `× 1,19` | `× 1,12` | `× 1,09` | `× 1,07` | `× 1,06` |

> **O multiplicador não desconta a Reação de que ele abre mão.** *O `Bloquear` é neutro por construção, pela peça 23, e o ataque de oportunidade só acontece se alguém sair do alcance.*

#### A parte destrutível — a vida dela é o empate

***Decisão do Mizuki, v0.244.*** *O braço do Sukuna virou regra, e a conta serve para qualquer inimigo.*

> **A vida de uma parte destrutível é `os PV-base da célula ÷ as rodadas × 2 ÷ N`, arredondando para baixo — duas vezes a saída de um personagem por rodada.** *Ela é alvo com a Defesa do inimigo, e destruí-la tira `1` das ações dele.*

| faixa | nível 2 | nível 5 | nível 10 | nível 15 | nível 20 | nível 25 | nível 30 |
|---|---|---|---|---|---|---|---|
| a vida de uma parte | `19` | `45` | `65` | `90` | `110` | `137` | `157` |

**O `2` são as rodadas pela frente que fazem o empate**, *e é ele que decide se vale a pena quebrar: com mais rodadas pela frente ninguém quebraria parte nenhuma, e com menos ela viraria alvo óbvio em toda rodada.* **O `×1` fica de fora por conta:** *ele tem uma ação só, e uma parte que tire ação o deixaria sem turno.*

**A parte não se paga na vida, e isso é por construção:** *a vida dela é exatamente o que ela devolve em ação perdida.*

> **Quantas partes ele tem, e o que a quebra faz além de tirar a ação, são do mestre.** ***Decisões dele:*** *"Decisão do mestre, é flavor"* e *"o caso do sukuna é exemplo"*. **Dois avisos, medidos e não travados:** *se as partes tirarem todas as ações, o inimigo para de agir; e efeito que não seja a ação perdida não tem preço nesta régua.*

#### As duas trocas ruins, declaradas e não proibidas

***Decisão do Mizuki:*** *"não tem problema não valer a pena, às vezes o combate tem uma pessoa só."*

> **O inimigo que se cura empata em curar `vida ÷ rodadas`** — *a saída do grupo numa rodada.* *Ele gasta a rodada e abre mão dos N golpes; ganha `H` de vida, que alonga a luta em `H ÷ (N × a saída de um personagem)` rodadas, e cada rodada a mais entrega os N golpes.* **Então `H` de cura vale `golpe ÷ a saída de um personagem × H` de dano** — *`0,71 × H` no `Desastre` e `0,86 × H` na `Calamidade`, no nível 30 —, e curar lasca é o mesmo erro que o grupo comete.*
>
> **A condição que o inimigo põe num personagem empata quando `alvos × ações negadas = 3 × ações gastas`.** *A conta não depende do nível nem do N: cada ação do personagem é um terço da rodada dele, e cada ação do inimigo é um golpe de N.* **Em alvo único nenhuma compensa** — *a `Pesada` precisa de `2` alvos, a `Média` precisa de `3` alvos, e a `Leve` precisa de `6` alvos.*

**As duas são a mesma conta virada: gastar a rodada em algo que não é dano rende menos do que aquilo vale, a não ser em área.**

## 7. O que o `conferir-bestiario.py` confere

**As checagens da escada morreram com ela, e as da grade leem cada número desta peça contra o dono dele.** *A lista está no cabeçalho do validador, e o arnês da v0.282 está no CHANGELOG.* **A peça de antes, com as perturbações da v0.221 à v0.281, está no arquivo morto.**

## 8. Em aberto

- **O Sukuna na grade.** *O `bestiario/05-sukuna/` ainda monta ele pela escada — uma `Calamidade` de oito com os multiplicadores empilhados, `18,4` pessoas.* **Na grade ele é uma `Calamidade ×6` com os recursos pagos na vida**, e o documento dele precisa ser refeito.
- **O `×5` e o `×6` no playtest.** *A conta diz que a duração não depende do N, e o FIREBALL mostra o grupo de 5 ou 6 lutando cerca de uma rodada a mais que o de 2* — **sinal fraco, e a mesa decide.**
- **O peso dos três grupos de dano da peça 19 §4 é palpite**, *e toda a régua de resistência do §6.3 se refaz quando a mesa corrigir.*
- **O inimigo com Trilha.** *Fica de fora por decisão, e o motivo está no §6* — mas um antagonista recorrente que sobe junto com o grupo é caso de mesa que vai aparecer.

# ECONOMIA DE AÇÃO E INICIATIVA

**Fase 4, terceira peça.** O turno, os recursos que ele contém, iniciativa e o que o Fundamento vende sem ter definido.
Versão v0.11, corrigida na v0.17 e na v0.26 — 10/08/2026

---

## 1. Esta peça é diferente das outras

As duas anteriores desenhavam do zero. Esta **descobre** — a economia de ação já existe dentro do Fundamento, espalhada por dezesseis peças que vendem pedaços de turno. Ela só nunca foi escrita.

O que o manual já declara, no glossário: `Ação | Padrão · Bônus · Reação · Rodada inteira`. E o que ele usa sem definir:

| Usado por | O que nunca foi definido |
|---|---|
| Passo, Pressa, Peso Morto | **Deslocamento base.** Passo dá 6 m, Pressa dá +6 m, Peso Morto corta pela metade — de quanto? |
| Passo, Pressa | **Ataque de oportunidade.** As duas dizem "sem provocar". Provocar o quê? |
| Adianta | **Iniciativa.** A Melhoria dá +2 na CD se você conjurar antes de qualquer inimigo agir. |
| Fica, Mão Firme | **Concentração.** Uma exige, a outra protege de dano até 10. |
| Parado, Atrasar | **Movimento como recurso separado.** Parado tira o movimento e mantém a ação bônus. |

## 2. O teste da premissa herdada

Esta é a parte mais herdada do sistema inteiro, e vale dizer isso em voz alta em vez de fingir que foi escolha.

Ação padrão, ação bônus, reação, movimento e ataque de oportunidade são o esqueleto de turno do d20 moderno. O Fundamento foi escrito em cima dele, e dezesseis peças já têm preço calibrado nessa premissa — **trocar o esqueleto de turno agora significa reprecificar todas elas e revalidar os 35 feitiços prontos.**

A conclusão honesta: **mantemos, e por custo de retrabalho, não por mérito.** O que dá para fazer é escolher bem os detalhes que ainda estão abertos, e é o que o resto deste documento faz.

Duas premissas que **não** vamos herdar sem checar:

- **Ataque de oportunidade existe?** Sim, e ele passa no teste de finalidade: sem ele, sair de um corpo a corpo é grátis, e a Melhoria Passo perde a razão de existir. E em Jujutsu Kaisen dar as costas para um feiticeiro em alcance de toque *deveria* custar caro.
- **Iniciativa é rolada?** Sim, e por um motivo mecânico específico. Ver seção 5.

## 3. O turno

Um turno contém quatro recursos, e eles são independentes:

| Recurso | Quantos | O que faz |
|---|---|---|
| **Ação de Movimento** | uma, e ela vale até 9 m de deslocamento | pode ser dividida antes, durante e depois da ação |
| **Ação padrão** | uma | atacar, conjurar, a maioria das coisas |
| **Ação bônus** | uma | só o que a regra disser explicitamente que é ação bônus |
| **Reação** | uma, e ela volta no começo do seu turno | responde a um gatilho, e vale fora do seu turno |

> ***O primeiro slot se chamava `Movimento` até a v0.122, e o rename é decisão do Mizuki.*** *Ele virou `Ação de Movimento` quando o §3.2 passou a cobrar dele uma coisa que não é andar — sacar o segundo item do turno.* **A partir do momento em que um slot compra duas coisas diferentes, ele é uma ação e não uma medida**, e é assim que o d20 sempre chamou.
>
> **`Ação de Movimento` é o SLOT; `deslocamento` é a DISTÂNCIA que ele compra, e são coisas diferentes.** *Nada que diga `deslocamento` mudou de sentido — `+3 m`, `metade do deslocamento`, `perde o deslocamento do próximo turno` continuam sendo metros.* **O que ganhou nome foi o lugar do turno em que eles são gastos.**

**Rodada inteira** (o que o Fundamento chama de Ação Completa) não é um quinto recurso: é gastar a Ação de Movimento, a ação padrão e a ação bônus de uma vez.

**Deslocamento base: 9 metros.** O número não é arbitrário — ele conversa com o resto das distâncias do Fundamento. O alcance base de Projétil é 18 m, então um turno de movimento fecha metade da distância de um duelo. A escada de área começa em raio de 3 m, então sair de uma explosão custa um terço do seu movimento. E os +6 m de Passo e Pressa são acréscimos que importam sem dobrar nada.

**Ataque de oportunidade.** Quando alguém sai do seu alcance de corpo a corpo sem tomar cuidado, você pode gastar a sua Reação para atacar. É o que dá sentido a Passo e Pressa dizerem "sem provocar".

**Concentração.** Alguns efeitos exigem que você mantenha a atenção neles — a Melhoria **Fica**, um efeito que dura, uma condição que você segura. Você só concentra em um por vez, e ao tomar dano faz um **Teste de Resistência Vigor** contra **a CD de quem te feriu**. Falhou, o efeito cai. **É um teste por golpe que te acerta**, e não um por rodada. *Este parágrafo dizia "CD 10 ou metade do dano, o que for maior" até a v0.252; a subseção `A CD de quem te feriu`, logo abaixo, tem o que trocou e por quê.*

*Corrigido na v0.26.* Este parágrafo dizia **Físico**, e o manual dizia *"teste de Constituição"* dentro da Restrição Carregar — dois documentos, dois testes, e este aqui ainda afirmava que era *"a mesma régua que Carregar já usa"*. A régua da CD era; o teste não. **Concentração é Vigor**, e o manual v7.6 deixou de nomear teste pelo atributo.

**E Carregar deixou de ser concentração.** Os dois seguram alguma coisa contra o dano, mas a diferença já estava escrita e ninguém tinha lido: em Concentração *"o efeito cai"* — você tinha, e perdeu; em Carregar *"perde o feitiço"* — ele ainda não tinha saído. Um mantém o que está no ar, o outro segura o que está por sair.

| | o que você segura | teste | falhar custa |
|---|---|---|---|
| **Concentração** | o efeito que já está no ar | **Vigor** | o efeito cai |
| **Carregar** | o feitiço que ainda não saiu | **Espírito** | o feitiço, e o que você pagou por ele |

A Passiva **Mão Firme** cobre os dois, e o manual v7.6 diz isso com todas as letras — *"não perde concentração nem carga por dano de 10 ou menos"* —, porque com a divisão o nome dela sozinho não alcançava mais o Carregar.

### A CD de quem te feriu — v0.253

> ***Decisão do Mizuki em 19/09/2026 (v0.253): a CD sai de quem bateu, e não do dano.*** *Até a v0.252 a Concentração rolava contra `10` ou metade do dano, o que fosse maior, sem teto. Ela quebra no dano de chefe, e as tabelas abaixo mostram onde.*

**De quem é a CD.** É a de quem causou o dano, na forma de sempre da peça 1 §5:

- *feitiço:* a CD do feitiço, `8 + atributo da técnica + maestria`;
- *golpe de arma ou desarmado:* `8 + o atributo do ataque + maestria` — Força no corpo a corpo, Destreza à distância. É a mesma forma, e a peça 26 §3 já lê assim a CD do inimigo;
- *inimigo:* a CD da ficha dele, peça 26 §3;
- *invocação:* a CD dos efeitos dela, peça 15 §3.6;
- *dano sem autor* (queda, armadilha, uma zona sem dono): o mestre declara a CD na escada da peça 4 §2.

**Um teste por golpe.** *O jogador raramente enfrenta mais de duas fichas, e o inimigo precisa bater em vários alvos.* Cada golpe que acerta quem concentra pede um teste, e a CD é a de quem bateu. **O `Carregar` usa a mesma CD**, com o teste de Espírito que ele já tinha. **A `Mão Firme` continua igual:** dano de `10` ou menos não pede o teste.

**A corrida de domínios é esta mesma rolagem** *(manual, seção `Dois domínios abertos ao mesmo tempo`; livro, `Domínios sobrepostos`)*: Vigor contra a CD de quem te feriu. **Só a contagem troca:** na corrida as falhas ficam marcadas e o domínio cai quando chegam a metade da Essência, e aqui uma falha derruba o efeito. *Até a v0.252 a CD da corrida era a do dono do outro domínio, decisão de 12/09 (o rascunho da Expansão sem Barreiras, §7.2). O Mizuki alinhou as duas em 19/09.* **Quando o jogador acertou o inimigo de mais de um jeito na rodada, com CDs diferentes, vale a maior.**

**Contra o que a regra se mede.** *O inimigo carrega a mesma curva de atributo de quem investe (peça 26 §3.1), então a CD dele é a de um personagem investido no mesmo nível.* O Teste de Resistência é `d20 + atributo + maestria`, e a maestria só entra em quem treinou (peça 1 §5).

**Chance de passar no teste de Vigor contra a CD do inimigo**

| | nv 5 | nv 10 | nv 15 | nv 20 | nv 25 | nv 30 |
|---|---|---|---|---|---|---|
| **CD do inimigo** | `12` | `14` | `14` | `16` | `16` | `18` |
| Vigor investido e treinado | `65%` | `65%` | `65%` | `65%` | `65%` | `65%` |
| Vigor investido, sem treino | `60%` | `55%` | `55%` | `50%` | `50%` | `45%` |
| Constituição 3, sem treino | `60%` | `50%` | `50%` | `40%` | `40%` | `30%` |

**Quem treinou o Vigor não deriva** (os `65%` são os mesmos da peça 1 §6), **e quem não treinou cai de propósito.** *É a distância que o manual já quer entre quem treinou e quem não treinou, a mesma da §5.0 da peça 1.*

**Quanto tempo uma concentração aguenta.** *O cenário: o chefe faz `2` golpes por rodada, acerta `50%`, e `1` golpe em `4` cai em quem concentra, porque o grupo tem quatro. A concentração aguenta `10` rodadas quando nenhum teste falha.*

**Chance de segurar `10` rodadas**

| | nv 5 | nv 10 | nv 15 | nv 20 | nv 25 | nv 30 |
|---|---|---|---|---|---|---|
| **regra nova** · Vigor investido e treinado | `41%` | `41%` | `41%` | `41%` | `41%` | `41%` |
| regra nova · Constituição 3, sem treino | `36%` | `28%` | `28%` | `21%` | `21%` | `16%` |
| *CD da regra antiga* | `10` | `18` | `27` | `36` | `45` | `54` |
| **regra antiga** · Vigor investido e treinado | `53%` | `24%` | `7%` | `7%` | `7%` | `7%` |

***Por que a regra antiga saiu:*** *o golpe do chefe cresce com o nível e a CD dela cresce junto, sem teto. No nível `10` ela passa a `18` e quem treinou resiste `45%`; do nível `15` em diante nenhum `d20` resiste, e o `7%` que sobra é o chefe errar os golpes, não o teste.* **A regra nova segura `41%` em qualquer nível, porque os dois lados crescem juntos** — é a lição nº 1 do projeto.

**O que a regra nova cobra, e o Mizuki ainda não viu:** *nos níveis baixos ela é mais dura que a antiga para quem concentra — `41%` contra `53%` no nível `5`, porque o golpe de chefe ali ainda é pequeno e a CD `10` era fácil.* **E um golpe pequeno de inimigo forte pede o mesmo teste que um golpe grande:** só a `Mão Firme` livra dos golpes de `10` ou menos.

### A duração: `Concentrada` e `Duradoura` — v0.254

> ***Decisão do Mizuki em 19/09/2026 (v0.254).*** *A duração de efeito de estado em combate vira regra mais duas Melhorias, e não Restrição. A Forma `Efeito` fica como está, com a escada dela por Classe.*

**O buraco que isto fecha.** *Condição e buff só duravam uma rodada ou até o fim do próximo turno, e só a `Fica` e o `Anteparo` chegavam a `1` minuto. Não existia duração para o buff ou a condição fora do `Efeito`.*

**As duas Melhorias**, na Família `Tempo` *(aprovado pelo Mizuki em 19/09/2026: uma técnica com `Tempo` Fechada não compra duração; a alternativa era `Fora de família`)*:

- **`Concentrada`** — *Leve.* Os efeitos de estado do feitiço passam a durar o tempo da tabela de duração, e você concentra neles, pela regra deste parágrafo e da CD de quem te feriu.
- **`Duradoura`** — *Média.* A mesma coisa, sem exigir concentração.

**Escopo: o feitiço inteiro, e só o efeito de ESTADO** *(condição, buff)*. **Não vale para o dano, para a `Fica` nem para o `Anteparo`**, que já têm duração própria. **O feitiço que mistura efeitos de tipos diferentes leva a menor duração entre eles** *(aprovado pelo Mizuki em 19/09/2026)*.

**Quanto custa, em pontos, por Classe** *(o preço de `Leve` e `Média` sai da tabela de Classe do manual)*:

**Preço da duração por Classe**

| | Classe 1 | Classe 2 | Classe 3 | Classe 4 | Classe 5 | Classe 6 | Classe 7 |
|---|---|---|---|---|---|---|---|
| `Concentrada` (`Leve`) | `1` | `1` | `2` | `2` | `3` | `3` | `4` |
| `Duradoura` (`Média`) | `1` | `2` | `3` | `4` | `5` | `6` | `7` |
| a diferença: o que custa não concentrar | `0` | `1` | `1` | `2` | `2` | `3` | `3` |

***Na Classe 1 as duas custam o mesmo.*** *Como a duração do condição e do buff ofensivo é igual nas duas, ali a `Duradoura` é estritamente melhor, e a `Concentrada` só se distingue no buff defensivo. É consequência da tabela de Classe, e o Mizuki escolheu `Duradoura` como `Média` sabendo disso, por não querer exceção escrita.*

**Quanto dura**

| O que o efeito faz | Concentrada | Duradoura |
|---|---|---|
| Condição, buff ofensivo e debuff | 1 minuto | 1 minuto |
| Buff defensivo numérico: um bônus fixo na Defesa ou num Teste de Resistência (a `Guarda`) | 10 minutos | 1 minuto |
| Buff defensivo mecânico: resistência, imunidade, pontos de vida ou dividir dano (a `Divide`) | 10 minutos | Classe 1 e 2: 1 hora · Classe 3: 8 horas · Classe 4 em diante: 24 horas |

**Por que esses tempos** *(D&D no 5e.tools em 19/09/2026, com as `557` magias únicas de todas as fontes menos a `AU`, versão 2024 preferida; medido no site, e não reproduzido pelo validador)*:

- ***Com concentração, o nível da magia não explica a duração*** *(correlação de postos `0,02` em `235` magias)*, **e a duração depende do efeito**: as proteções clássicas, como o `Escudo da Fé` (`+2` na CA, e a `Guarda` é ele), duram `10` minutos, e as mais fortes, de 5º círculo em diante, duram `1`.
- ***Sem concentração, a duração sobe com o nível*** *(`0,36` em `134` magias, `0,64` nas `14` proteções)*: mediana de `1` h nos círculos `1` a `3`, `8` h no `4`, `24` h do `6` ao `8`. **É a escada da `Duradoura`.**
- ***Bônus numérico de `+2` ou mais nunca dura horas:*** *o `Escudo` é `+5` por uma rodada, o `Escudo da Fé` `+2` por `10` minutos; as duas exceções longas são de número pequeno, o `Vínculo de Proteção` (`+1`, `1` h) e o `Auxílio` (`+5` de PV, `8` h).* **Por isso a `Guarda` numérica não sobe pela escada de horas, e o PV entra no lado mecânico.** ***E a Duradoura da `Guarda` dura MENOS que a Concentrada*** *(ideia do Mizuki): o que ela compra é não concentrar, com o buff cobrindo a luta e não as lutas seguintes.*
- ***O mapa de Classe é meu:*** *Classe `c` ≈ círculo `2c − 1`, porque o nível que libera a Classe libera esse círculo. A escada `1` h · `8` h · `24` h é a mediana do D&D sem concentração nesse mapa, e o Mizuki aceitou.*

**O que a regra cobra.** *O preço achatado por degrau de tabela é barato para a condição `Leve` e `Média` que dura a luta inteira, e o Mizuki escolheu assim, pelo motivo de não ter exceção.* **A `Duradoura` cobra `1,5×` a `2,0×` o preço da `Concentrada` nas Classes `2` a `7`.**

### O buff de dano: `Alvo de Caça` — v0.255

> ***Decisão do Mizuki em 19/09/2026 (v0.255).*** *A Melhoria entra na Família `Marca` — dele: "Coloca em marca" —, o gatilho é toda rolagem de acerto que acerta o alvo marcado, e não nasce termo novo: a regra fala de "duas Melhorias escritas como uma", e ele escolheu a opção sem batismo, "A definitivamente".*

**O buraco que isto fecha.** *O catálogo não tinha nenhum buff de dano. A `Marca` dá vantagem, a `Ecoa` dá vantagem ao aliado, e o `Remate`, o `Acúmulo` e a `Queima` somam no próprio golpe — nada somava dano nos seus ataques seguintes. É o `Hex` do D&D, e quem batizou foi o Mizuki.*

**A Melhoria é uma só, de preço `Leve`, e mora na Família `Marca`.** *O alvo fica marcado até o fim do seu próximo turno. Daí em diante, cada ataque seu que acertar ele causa `1d4` a mais, e o feitiço que marcou não ganha o dado — igual à `Marca`, que dá vantagem no *próximo* ataque. Com o `Rápido` no mesmo feitiço, o dado é `1d8`. Um alvo marcado por vez: marcar outro apaga a marca anterior.*

**É o mesmo estado `marcado` da `Marca`**, e não um estado novo: a Restrição `Condicional` que dispara com *"marcado por você"* dispara com as duas. **O dado é fixo, sem escala por Classe** *(decisão da v0.254, quando ele recusou o `X`d4 que eu tinha proposto: "no D&D a gente não tem esse aumento ao longo dos níveis, sinto que isso vai fortificar a possibilidade de só atacar ao invés de usar feitiços")*. **Com a `Concentrada`, a marca dura `1` minuto** — *é buff ofensivo, a primeira linha da tabela `Quanto dura`.*

**Por que a Família `Marca`, e não `Auxiliares`.** *Ela é irmã da `Marca`: a mesma janela, o mesmo alvo, e dano no lugar de vantagem. A palavra `marcado` já mora ali.* **E os três Fundamentos prontos decidem o resto:** *em `Auxiliares`, a `Régua` — que é o pronto de caçador, o que mais quereria esta Melhoria — tem `Auxiliares` como Fechada, e não poderia comprar; em `Marca` nenhum dos três bloqueia, e a `Sentença` e a `Banca` têm a Família como Livre, onde o preço cai para `1` ponto em toda Classe.*

**O gatilho**, decisão dele em 19/09/2026 — *"Qualquer ataque que não seja 'continuo', ent rajada pega, ataque extra, afins (q nem dnd)"*:

- **Conta toda ROLAGEM DE ACERTO sua que acerta o alvo marcado:** *arma, desarmado, feitiço com rolagem de acerto, e cada tiro da `Rajada` conta sozinho.* **É o `Hunter's Mark` do D&D 2024, que cobra a mesma coisa: todo acerto com rolagem de ataque.**
- **Não conta o que não é rolagem de acerto:** *feitiço resolvido por Teste de Resistência não é ataque; o dano que volta em rodadas seguintes, como o da `Queima` e o da `Fica`, também não; e o respingo do `Estilhaço` e o pulo do `Salto` não são ataque.*
- **Só os ataques SEUS:** *a sua invocação não herda a marca.* *(Default meu, para ele vetar.)*

**Quanto custa, em pontos, por Classe** *(o preço `Leve` sai da tabela de Classe do manual, e o desconto de Família Livre da regra "tire metade da Classe do preço, com mínimo de 1"; entre os prontos, quem tem `Marca` como Livre é a `Sentença` e a `Banca`)*:

**Preço do `Alvo de Caça` por Classe**

| | Classe 1 | Classe 2 | Classe 3 | Classe 4 | Classe 5 | Classe 6 | Classe 7 |
|---|---|---|---|---|---|---|---|
| `Alvo de Caça` (`Leve`) | `1` | `1` | `2` | `2` | `3` | `3` | `4` |
| o mesmo, em Família Livre | `1` | `1` | `1` | `1` | `1` | `1` | `1` |

**A régua da conta.** *É a da v0.254, e ela mede os dois lados igual: `1` ponto compra `1d8`, que é `4,5` de dano cheio.* **Os golpes que cabem na janela:** *`2` sem mais nada (o seu próximo turno, com o físico batendo duas vezes por rodada do nível `7` em diante); `5,4` com a `Concentrada`, que é a luta inteira menos a rodada em que você marcou; `4` com o `Rápido`, que marca de Ação Bônus e já ataca no mesmo turno.*

***A luta é de `3,7` rodadas — o meio da banda de `3,4` a `4,0` da seção 8 da peça 1.*** *O `conferir-aptidoes.py` lê o **topo** dessa banda, e está certo no que ele faz: ele testa se uma barreira de `1` minuto cabe dentro da luta, e ali o pior caso é a luta mais longa. Aqui o número responde outra pergunta — quantos golpes a `Concentrada` cobre, em média —, e a resposta média é o meio.*

**Quanto do preço o buff paga**

| | Classe 1 | Classe 2 | Classe 3 | Classe 4 | Classe 5 | Classe 6 | Classe 7 |
|---|---|---|---|---|---|---|---|
| só o buff (`2` golpes) | `111%` | `111%` | `56%` | `56%` | `37%` | `37%` | `28%` |
| com a `Concentrada` (`5,4` golpes) | `150%` | `150%` | `75%` | `75%` | `50%` | `50%` | `38%` |
| com o `Rápido`, em `1d8` (`4` golpes) | `133%` | `100%` | `57%` | `50%` | `36%` | `33%` | `27%` |

***Ele viu estes números antes de escolher, e manteve.*** *Nas Classes `1` e `2` o buff paga mais do que custa, e da `3` em diante ele desbota, que é o que o dado fixo faz.*

**O pior caso é a `Rajada` seguinte**, *que divide o feitiço em `Classe + 1` tiros com rolagem de acerto cada um: contra o alvo marcado, ela soma `(Classe + 1) × 2,5` de dano.*

**A `Rajada` seguinte contra o alvo marcado**

| | Classe 1 | Classe 2 | Classe 3 | Classe 4 | Classe 5 | Classe 6 | Classe 7 |
|---|---|---|---|---|---|---|---|
| `1d4`: o dano que soma | `5,0` | `7,5` | `10,0` | `12,5` | `15,0` | `17,5` | `20,0` |
| `1d4`: quanto é da Rotina | `38,5%` | `24,2%` | `22,2%` | `19,8%` | `19,7%` | `18,6%` | `18,5%` |
| `1d8` com o `Rápido`: o dano | `9,0` | `13,5` | `18,0` | `22,5` | `27,0` | `31,5` | `36,0` |
| `1d8` com o `Rápido`: da Rotina | `69,2%` | `43,5%` | `40,0%` | `35,7%` | `35,5%` | `33,5%` | `33,3%` |

**O que a regra cobra, e o Mizuki aceitou em 19/09/2026.** *A linha da `Rajada` é a mesma curva do `X`d4 que ele recusou — `20,0` de dano na Classe `7`, `18,5%` da Rotina —, só que agora ela é paga duas vezes: a `Rajada` também é `Leve`, e `Alvo de Caça` + `Rajada` + `Concentrada` são três Melhorias, que só cabem da Classe `3`.*

**O limite de Melhorias é o que segura o conjunto.** *`Alvo de Caça` + `Concentrada` + `Rápido` são `3` Melhorias e `9` pontos: só cabe da Classe `3`, e ali ocupa `9` dos `9` pontos. Nas Classes `1` e `2` a ficha escolhe entre `Alvo de Caça` + `Rápido` e `Alvo de Caça` + `Concentrada`.*

**Não existe teto de soma com o `Acúmulo` e o `Remate`, e é por conta:** *o `Alvo de Caça` soma `2,5` fixos no feitiço seguinte contra o alvo marcado (`5,6%` da Rotina na Classe `3`, `2,3%` na `7`) e `5,0` nos dois ataques do físico (`11%` na `3`, `4,6%` na `7`) — pequeno demais para mover o que o `Acúmulo` já faz sozinho.* **O que passa do teto de um alvo ali é o `Acúmulo`, e ele passa antes desta Melhoria existir** — *está registrado como problema de design aberto no `ESTADO-ATUAL.md`.*

**E o invariante da peça 11 segue com folga:** *a rodada de golpe fica abaixo da Rotina. O golpe simples vai de `51,6%` para `58,3%` no nível `7` (`62,5%` com `1d8`) e de `47,2%` para `49,5%` no `30` (`51,3%`).*

## 3.1 A lista de ações

*Escrita na v0.83, e ela é o buraco que o desenho dos Caminhos achou: **esta peça tinha os quatro slots do turno e nenhuma ação nomeada.** `Ajudar` morava na peça 4 §5 sem custo de ação declarado, e nove Trilhas apontavam para uma lista que vivia num documento de desenho.*

> ***Decisão do Mizuki: copiar a lista do hobby, e de propósito.*** **Ninguém precisa aprender lista nova para uma coisa que todo jogador já sabe** — e o filtro multi-mestre agradece, porque dois mestres que vieram de outro sistema chegam ao mesmo lugar sem ler nada.

*A lista do 5e de 2024 tem **doze** ações. Oito já existiam aqui com outro nome; duas faltavam inteiras — `Influence` e `Ready` —, e as outras duas viraram outra coisa por decisão, logo abaixo.*

### As doze de Ação Padrão

| ação | o que ela faz |
|---|---|
| **Atacar** | um ataque com arma ou desarmado. Com ataque extra, os que a regra der. **`Agarrar` e `Derrubar` são opções dela**, e não ações próprias |
| **Conjurar** | um feitiço, pelo Fundamento |
| **Correr** | ganhe deslocamento igual ao seu, pelo resto do turno |
| **Desengajar** | o seu movimento não provoca ataque de oportunidade pelo resto do turno |
| **Esquivar** | ataques contra você têm desvantagem e os seus TR de Destreza têm vantagem, até o começo do seu próximo turno |
| **Esconder** | um teste de `Furtividade` |
| **Ajudar** | dá vantagem ao próximo teste ou ataque de um aliado. **Um por teste** — dois ajudantes não dão vantagem duas vezes (peça 4 §5) |
| **Influenciar** | um teste de **Essência** — `Persuasão`, `Enganação`, `Intimidação` ou `Atuação`, conforme o jeito — para mudar a atitude de alguém |
| **Preparar** | escolha uma ação e um gatilho visível. Quando ele acontecer, você gasta a **Reação** para fazer a ação |
| **Vasculhar** | um teste de `Percepção` ou `Investigação` sobre uma coisa ou uma criatura **ao seu alcance** |
| **Estudar** | um teste de `Sentir Energia`, `Ocultismo`, `Medicina` ou `História` sobre uma criatura ou objeto **que você enxerga** |
| **Usar objeto** | usar um objeto não mágico |

**`Influenciar` cabe sem adaptação porque Essência é o Carisma deste sistema.** *`Persuasão`, `Enganação`, `Intimidação`, `Atuação` e `Provocar` moram todas lá (peça 7).* **A ação do 5e é teste de Carisma; aqui ela é teste de Essência, e nada mais muda.**

**`Preparar` custa duas coisas por uma, e é isso que segura ela.** *Você gasta a Ação Padrão **agora** e a Reação **depois**.* **Se o gatilho não acontecer até o começo do seu próximo turno, a ação se perde.** *Preparar uma conjuração continua exigindo a Melhoria **Reação**, pela mesma regra da seção 3 — o slot não muda o que a Reação permite.*

> **Colisão declarada e aceita:** o manual usa *"dois turnos de **preparo**"* numa regra de Restrição, e ali a palavra é tempo de conjuração. **São coisas diferentes com a mesma raiz**, e o nome fica porque *"preparar uma ação"* é vocabulário que todo jogador já traz de casa.

## 3.2 Sacar e guardar — v0.122

*Escrita porque a peça 20 destampou que ela não existia.* **A lista de doze ações não tem nenhuma que seja sacar arma, e o `Desarmado` da peça 19 diz *"você bate desarmado até pegar de volta"* sem dizer quanto custa pegar.** *Buraco antigo e uniforme para todo mundo, e agora com uma rota inteira dependendo dele.*

***Decisão do Mizuki, e ela é a do d20:***

> **Sacar ou guardar UM item — inclusive arma — não custa nada.** Uma vez por turno.
> **A partir do segundo, sacar ou guardar custa a sua Ação de Movimento inteira.** *Não meia, não `3 m`: a Ação de Movimento do turno.*

**Trocar de arma é sacar e guardar, então é DOIS.** *Guardar a que está na mão é o primeiro e sai de graça; sacar a outra é o segundo e custa a Ação de Movimento.* **Largar no chão não é guardar — largar é de graça e sempre**, e é isso que faz *"solta e saca"* ser mais rápido que *"troca"*, ao preço de deixar a arma no chão.

*Por que a Ação de Movimento e não a Bônus:* **a Bônus já disputa com `Ímpeto` e `Campo`**, duas das doze Bênçãos, e com o que os Caminhos entregam. *A de Movimento é o único dos quatro slots que ninguém compra por habilidade, então cobrar dela não desliga kit de ninguém — ela cobra posição, que é o recurso que o combate deste sistema já usa.*

> **E isso é o degrau que uma Passiva pode comprar.** *Decisão do Mizuki:* **uma Passiva ou aptidão pode dizer que o segundo saque sai de graça, e ela cabe na Classe Passiva 1** — *"efeito pequeno, condicional, ou de informação"*, pela peça 11 §4. *A `Descarga` da Vanguarda e a `Fiel` da peça 16 já vivem nessa vizinhança.*
>
> **✔ E esse degrau ganhou o primeiro exemplar na v0.134: o `Bocado`, na peça 20 §3.3.** *Ele guarda o que você carrega dentro do corpo, e é por isso que o segundo saque sai de graça — a mão não vai à bainha, vai a você.* **Classe Passiva 1, exatamente como esta linha previu.**

### Isso decide contra quem o `Desarmado` foi preçado — fechado na v0.188

**A peça 19 preça o `Desarmado` em `3,45` de dano por rodada — `0,68` fatia — supondo que você bate desarmado até recuperar a arma.** *Com esta regra, quem carrega reserva saca outra **de graça**, porque é o primeiro saque do turno.*

| a ficha | o que o `Desarmado` custa a ela |
|---|---|
| carrega arma reserva | **nada** — o saque da reserva é o primeiro do turno |
| já sacou alguma coisa neste turno | a Ação de Movimento |
| não tem reserva | o que a peça 19 preçou: bater desarmado até recuperar |

**O preço publicado descreve só a terceira linha, e ele fica.** ***Decisão do Mizuki na v0.188:*** *a régua da peça 19 mede o que a condição **tira**, e não o que o alvo faz a respeito — nenhuma das treze modela preparação.* **Carregar reserva é a resposta, e ela é barata de propósito.**

> **⚠ Esta seção dizia que consertar era caro, e para esta condição não era.** *A frase era "repreçar uma condição mexe na régua das treze e no catálogo de Melhorias do manual".* **A Melhoria `Condição` cobra pelo nível, o nível sai da banda, e o `Desarmado` ocupa `22%` do teto da `Leve`** — *qualquer valor até aquele teto continua `Leve`, e nada no manual se moveria.* **A dívida ficou sessenta e seis versões parecendo grande.** *A peça 19 §3.1 é a dona da medida.*

### `Agarrar` e `Derrubar` são opção do ataque, e não ação

*Decisão do Mizuki, seguindo o 2024.* **Quem tem ataque extra pode agarrar com um golpe e bater com o outro** — que é exatamente o que um Bastião quer fazer.

> **Como ação própria elas ficavam mortas por dominância:** agarrar custaria o turno inteiro, e bater duas vezes rende mais do que segurar alguém.

*O `Segurar` do Bastião no nível 30 continua valendo palavra por palavra: ele diz "tentar `Agarrar` ou `Derrubar`" e não cita slot nenhum.*

### As duas de Ação Bônus, e elas são deste sistema

*O slot da Ação Bônus é o mais vazio do turno — a seção 7 desta peça já dizia isso, e a peça 14 §4 mediu: passivo e ação bônus empatam em `2,01`.* **Estas duas existem para o jogador que travou e não sabe o que fazer no turno dele.**

> **`Provocar`** — Ação Bônus. Teste de `Provocar` contra o **Teste de Resistência de Espírito** do alvo. **Numa falha dele:** até o começo do seu próximo turno, ele ataca **com desvantagem qualquer alvo que não seja você**, e **com vantagem contra você**.

> **`Ler o Ambiente`** — Ação Bônus, **uma vez por cena**. Teste de `Percepção` ou `Intuição` contra a dificuldade que o mestre puser. Num sucesso, o mestre te diz **uma coisa daquele lugar que dê para usar** — um objeto, um caminho, uma posição, um risco. **Se não houver nada, ele diz isso e a ação não é gasta.**

**`Ler o Ambiente` NUNCA fala de criatura, e essa linha é a regra e não estilo.** *Quem quer saber do inimigo usa `Estudar`; quem quer revistar alguém usa `Vasculhar`; e os dois custam a Ação Padrão.*

> **Sem essa linha as três se dominavam, e a conta é direta:** o `Search` e o `Study` do 5e são os mesmos testes que o `Ler o Ambiente` faria, **e custam a Ação Padrão contra a Ação Bônus dele**. Mesmo teste, slot mais barato — ninguém usaria os dois caros. ***Decisão do Mizuki: separar por ALVO.*** *O `Ler o Ambiente` é sobre o lugar, o `Vasculhar` e o `Estudar` são sobre a criatura e a coisa.* **Com alvos diferentes elas param de responder a mesma pergunta, e a dominância some sem precisar de limite artificial.** *O `1× por cena` fica mesmo assim, porque a ação obriga o mestre a produzir conteúdo e sem teto ela vira imposto de improviso.*

**O `Provocar` foi medido duas vezes e passa**, e a conta está no `DESENHO-caminhos.md`: ele dá `+25` pontos percentuais quando dispara e `12` pp médios por rodada, contra os `+20` e `1,0` que a peça 13 §7 já aceita no `Instinto Bruto`. *O que faz caber é a duração de uma rodada — ela não muda a razão, muda o que empilha.*

### O que a lista muda em quem já estava escrito

- **O `Ajudar` ganhou custo de ação, e ele nunca tinha tido um.** *A peça 4 §5 escreve a regra do "um por teste" e nunca disse em que slot ela acontece.* **É Ação Padrão.**
- **O `Mão na Roda` do Guia, no nível 7, passa a ser exceção de uma coisa que existe:** ele torna o `Ajudar` uma Ação Bônus para aquele Caminho. *Antes ele era exceção de uma regra não escrita.*
- **`Preparar` é o quinto competidor pela Reação**, e a seção 7 desta peça já desconfiava do slot com quatro. *Fica marcado para o playtest, junto da pergunta que já estava lá.*


## 4. A régua de preço

O Fundamento vende pedaços de turno em onze Restrições, e nunca teve uma régua para justificar quanto cada uma devolve. Com os recursos definidos, ela existe:

> **Leve** — consome **um** recurso, ou meio recurso espalhado por dois turnos.
> **Média** — consome **o turno inteiro**, ou um recurso mais um risco real.

Conferindo o catálogo existente contra essa régua:

| Restrição | preço | o que consome | fecha? |
|---|---|---|---|
| Parado | Leve | movimento | sim |
| Gesto | Leve | mãos e voz | sim |
| Peso Morto | Leve | metade do movimento, dois turnos | sim |
| Frágil | Leve | risco de perder o efeito | sim |
| Tudo ou Nada | Leve | chance de zerar | sim |
| Atrasar | Média | movimento + bônus + padrão | sim |
| Corpo a Corpo | Média | a distância inteira, para sempre | sim |
| Sangra | Média | vida | sim |
| Recuo | Média | condição no corpo até o próximo turno | sim |
| Sem Volta | Média | o próximo turno inteiro, se errar | sim |
| Carregar | Média | ação padrão do turno anterior + risco de perder tudo | ver abaixo |

**Dez das onze fecham.** Rodando o teste de dominância por conjunto de recursos, nenhum par de mesmo preço contém o outro. O catálogo estava certo — só não tinha como provar.

### O caso Carregar, que a v7.3 deixou em aberto

O changelog da v7.3 registrou a tensão: *"Carregar (Média) fica na mesma faixa do Atrasar e dói mais, porque consome dois turnos e ainda arrisca perder o feitiço se você tomar dano."*

Com a régua na mão, a resposta é mais simples do que parecia, e não exige mexer em preço.

**Atrasar** consome três recursos, todos neste turno, sem risco. **Carregar** consome um recurso do turno anterior mais o risco. São conjuntos diferentes, em turnos diferentes — não há dominância de conjunto.

O problema é que **o texto do manual não diz se quem carrega pode se mover no turno de carga.** E é isso que decide:

- Se **pode se mover**, Carregar tem um upside que Atrasar não tem: você fica móvel enquanto prepara. Os dois valem Média por caminhos diferentes, e o par se resolve sozinho.
- Se **não pode**, Carregar vira Atrasar com espera e risco por cima, e aí está dominado de verdade.

**A decisão: quem usa Carregar mantém o movimento e a ação bônus no turno de carga.** Só a ação padrão vai embora. É a leitura mais natural do texto atual, é o que torna a peça distinta de Atrasar, e — o mais importante — **não muda nenhum dos 35 feitiços prontos**, porque nenhum deles usa Carregar.

Um item que estava aberto há duas versões se resolve escrevendo uma frase que já estava implícita. Vale registrar por quê: **tensão de preço às vezes é lacuna de texto disfarçada.** Antes de mexer no número, confira se a regra diz o que você acha que ela diz.

*E na v0.26 a mesma lição pegou o mesmo item de novo.* A Restrição continuava dizendo *"você gasta um turno **concentrado**"*, e era essa palavra — só ela — que fazia Carregar e Concentração parecerem a mesma regra com dois testes diferentes. Ela saiu, e o preço não precisou de nenhum ajuste: o par Atrasar contra Carregar continua fechando pelos conjuntos de recurso, como esta seção já tinha resolvido.

### A Restrição que o momento do feitiço apaga — v0.246

**Uma Restrição que só cobra recurso do turno em que você conjura não cobra nada quando a Melhoria tira a conjuração desse recurso, ou desse turno.** *Duas Melhorias de `Tempo` fazem isso:* **o `Rápido` passa a conjuração para a ação bônus, e a `Reação` tira ela do seu turno.**

| par | por que não cobrava | devolvia |
|---|---|---|
| `Rápido` + `Atrasar` | o `Atrasar` tira a ação bônus, que é onde o `Rápido` conjura | `Média`: um terço do orçamento, em toda Classe |
| `Reação` + `Atrasar` | o `Atrasar` cobra "naquele turno", e a Reação sai no turno de outro, em que você não anda nem age | `Média` |
| `Reação` + `Parado` | "você não se move no turno em que conjura", e no turno de outro você não se move | `Leve` |

***Decisão do Mizuki na v0.246: vetar os três.*** *O `Rápido` e a `Reação` ganharam a trava no texto do manual, no molde do `Armado` com o `Carregar`.* **O primeiro par já era trava da ficha digital, pela decisão A3 de lá**, *e o manual ficava calado: quem montava no papel levava o desconto.* **Os outros dois apareceram testando a mesma leitura nas outras Restrições.**

**O que continua valendo, pela mesma régua:**

- `Rápido` + `Parado` — o movimento é recurso separado da ação bônus, então o `Parado` cobra.
- `Reação` + `Gesto` — mão e voz são usadas na hora em que o feitiço sai, seja de quem for o turno.
- `Reação` + `Carregar` — a carga gasta a ação padrão do seu turno anterior.
- `Armado` com o `Atrasar` ou o `Parado` — você arma no seu turno, e é nele que o custo cai.

**A checagem `6` do `conferir-acao.py` deriva os vetos dos conjuntos de recurso desta seção**, *e cobra que o manual e o livro escrevam esses vetos e nenhum outro.*

## 5. Iniciativa

> **Iniciativa = d20 + Destreza.** Maior age primeiro. Empate se resolve pela maior Destreza; persistindo, o jogador decide antes do inimigo.

> **Uma coisa só mexe nessa conta fora da Destreza, e é a condição `Surdo`: ela dá `−2`.** *Escrita na v0.104, na peça 19 §3.7, com a conta de quanto isso custa — `9,75` pontos percentuais de agir antes, que são `2,05` pontos de Destreza.* **Se aparecer uma segunda coisa que mexa na iniciativa, ela passa por aqui antes**, porque duas fontes de modificador sem ninguém somando é como o `Adianta` viraria bônus automático.

A parte que exige explicação é por que **rolada** e não fixa.

Iniciativa fixa — a ordem simplesmente sendo a Destreza — é tentadora num sistema de cinco a sete mestres: uma rolagem a menos, ordem previsível, ficha auditável. Mas ela quebra uma peça que já existe.

**A Melhoria Adianta** dá +2 na CD se você conjurar antes de qualquer inimigo agir na rodada. Com iniciativa fixa, um conjurador de Destreza alta **sempre** age antes, e Adianta vira +2 permanente por 2 pontos. Isso é exatamente o teste do bônus automático falhando: um bônus que a montagem óbvia sempre alcança não é bônus, é a linha de base com um passo a mais.

Com iniciativa rolada, Adianta é uma aposta: você paga por algo que costuma acontecer e às vezes não. O preço passa a fazer sentido.

**A conta de quanto Adianta vale:**

| sua Destreza | Destreza do inimigo | você age antes | efeito médio de Adianta |
|---|---|---|---|
| 3 | 3 | 52% | 5,2 pp |
| 4 | 3 | 57% | 5,7 pp |
| 6 | 3 | 66% | 6,6 pp |
| 3 | 5 | 38% | 3,8 pp |

O +2 na CD vale 10 pontos percentuais quando dispara, e ele dispara na maioria das rodadas mas não em todas. O efeito médio fica entre 4 e 7 pontos percentuais, por um preço Médio — **abaixo do que uma Média costuma entregar**, e vale acompanhar no playtest. Com iniciativa fixa seriam 10 pp garantidos, e aí o preço estaria errado no outro sentido.

## 6. A regra que fecha o turno

O Fundamento já tem, e ela é a regra de ouro nº 6:

> **Feitiço em Ação Bônus ou Reação só permite mais um de Classe 0 no turno.**

*Desde a v0.20 o manual escreve Classe também — a citação acima é literal.*

É a trava que impede o turno duplo de feitiço grande. Ela só funciona porque ação bônus e ação padrão são recursos separados — o que só agora está escrito.

### 6.1 Ela tem exatamente uma exceção, e é a Trilha `Torrente` — v0.131

> **A `Vazão` e o `Transbordo` sobem o teto do segundo feitiço, de `Classe 0` para metade da sua maior Classe.** *Nada mais no sistema faz isso.*

**Isto fica escrito aqui porque a regra acima é publicada como absoluta em cinco lugares** — nesta seção e em quatro do Manual da Guilda —, **e a exceção mora num sexto que nenhum deles cita.** *Dois mestres lendo o capítulo do turno e o capítulo dos Caminhos chegam a respostas diferentes, que é exatamente o filtro que este projeto usa para decidir.*

**A exceção não é mais de uma ação por rodada.** *A `Torrente` gasta a Ação Padrão e a Ação Bônus, que é a conta normal de qualquer ficha; o que ela fura é o **tamanho** do segundo feitiço, não a quantidade.* **A peça 6 §9 tem a medida, e o preço está no `DESENHO-trilhas.md`.**

> **E o teto dela nunca fica abaixo do `Classe 0` que esta regra já permite.** *Sem essa cláusula, no nível 11 a Trilha entregava um teto de `13` de dano onde a regra de ouro sozinha já dava `18`.*

## 7. O que esta peça deixa em aberto

- **Se ação bônus deve existir mesmo.** Ela é a mais herdada das quatro, e a que mais custa em tempo de mesa: todo turno, todo jogador pergunta "tenho alguma coisa de ação bônus?". Duas peças do Fundamento dependem dela (Rápido e Parado). Vale medir no playtest quantos turnos realmente usam uma.
- **Quantas reações por rodada.** Uma é o padrão, e quatro coisas competem por ela: ataque de oportunidade, a Melhoria Reação e as Passivas Contramedida e Reforço. Competir é bom — vira escolha. Mas se na prática ninguém nunca tiver reação sobrando, as Passivas de reação ficam mortas.
- **O valor real de Adianta** (seção 5). Entre 4 e 7 pontos percentuais de efeito médio, abaixo do que uma Média costuma entregar.

*Resolvido e tirado daqui:* o ataque de oportunidade **é ataque físico, rolado como ataque comum e pago com a Reação** — e um conjurador faz um normalmente, com soco ou arma. Conjurar na Reação continua exigindo a Melhoria Reação. A conta está na peça 4, seção 6.

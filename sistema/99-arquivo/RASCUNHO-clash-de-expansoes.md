> # ARQUIVADO na v0.173
>
> **De onde saiu:** `sistema/03-mecanica/RASCUNHO-clash-de-expansoes.md`, aberto na v0.28.
>
> **O que o substituiu:** a seção **`Dois domínios abertos ao mesmo tempo`** da seção 7 do manual do Fundamento, na **v7.18** — `manual/gerador/partE.js`. *Decisão do Mizuki na v0.173: o clash mora encostado na Expansão que ele governa, e não numa peça.*
>
> **Por que morreu:** ele era levantamento engatilhado, e o §5 dele mandava *"decidir qual modelo vale, e mandar o outro para `99-arquivo/` com o motivo escrito"*. **A decisão foi tomada.** *Mantido vivo ao lado da regra publicada, o §1 e o §2 dele viravam a segunda fonte do clash* — que é a lição nº 9, e é a mesma razão pela qual o rascunho de Pactos saiu na v0.134.
>
> **O modelo de push gradual reprovou como mecanismo de resolução, e a reprovação é medida.** *A velocidade dele é a diferença de refino, e essa diferença é **zero em 59%** dos pareamentos capazes de clash* — concentrada no topo, porque do nível 26 em diante o especialista e o meio a meio estão os dois no teto `10`. **Nenhum limiar conserta uma velocidade que é zero: o melhor caso resolve `41%`**, e o desfecho previsto para o vão zero era o número 4 abaixo, que este mesmo documento marcava como reprovado no filtro multi-mestre.
>
> **O que dele sobreviveu, e onde está agora** — tudo no manual v7.18, e **nenhum dos seis números foi escrito**:
>
> - o **gatilho** (só quando as áreas se sobrepõem) e a **anulação mútua do acerto garantido** → a abertura da seção
> - o **número 4**, *"dano pesado"*, que ele achava ser julgamento puro → virou **a corrida**, amarrada em estado publicado: barreira derrubada, duração vencida ou `0` de vida
> - o **número 2**, a vantagem do Acerto inofensivo → virou **pergunta binária** na cascata, sem número
> - o **número 5**, o buraco na barreira → virou **escolha de quem perde**, e não chance
> - o **número 6**, a curva inversa da barreira → **já estava implementado** no manual desde sempre, como voto vinculante binário: `por dentro não quebra`, `50 × metade do refino` por fora
> - o **número 3**, a vantagem da barreira aberta → **caiu**: não foi achada fonte na obra
> - o **número 1**, a velocidade do push → **morto pela conta acima**
>
> **O levantamento externo da v0.173 confirmou os sete comportamentos deste documento contra a obra**, e é por isso que ele estava certo sobre o mundo e errado sobre o mecanismo. *As fontes e o quadro estão no CHANGELOG da v0.173.*
>
> ---

# CLASH DE EXPANSÕES — rascunho engatilhado

**Não é peça.** É o levantamento do que foi discutido na v0.28, guardado com os números que faltam já identificados, para a peça 12 começar daqui em vez de do zero.

Versão v0.28 — 11/08/2026

> **Isto contradiz uma regra marcada como fechada.** O `ESTADO-ATUAL` registra, sob o título *"O clash de expansões, fechado"*, uma resolução por rolagem única. O modelo abaixo é outro. Nenhum dos dois foi para a mesa, e a decisão de qual vale **não foi tomada** — ela é o primeiro item da peça 12.

---

## 1. O que está decidido hoje, e continua valendo

*Da v0.27, e é o que a v7.7 do manual cita.*

> **Refino contra refino. Empatou, os dois rolam `1d10 + quantidade de aptidões + metade do nível`.**

O que sustenta essa regra, e que qualquer substituta precisa preservar:

- **Ela é simétrica.** O refino cresce +7 a +9 numa campanha, contra os +3 de atributo e maestria — então ele só pode aparecer numa disputa em que o outro lado também é refino. É a única exceção que a trava da peça 11 permite, e o clash é exatamente ela.
- **Do nível 26 em diante o refino para de decidir.** Especialista e meio a meio estão os dois no teto 10, e entre eles cai sempre no d10. Não é defeito; é o que a regra faz, e o texto tem que dizer.
- **Sete aptidões de vantagem ainda perdem `3%` das vezes, e empatam outros `3%`.** O d10 é grande de propósito: a ameaça é calibrada contra o nível do grupo, então os dois lados chegam empatados. *Este número dizia `12%` até a v0.161, e ele não sai de vantagem nenhuma — a lista das possíveis é `45 · 36 · 28 · 21 · 15 · 10 · 6 · 3 · 1%`.*
- **O inimigo carrega refino e aptidões na ficha dele**, no padrão do ambiente propício — valor sugerido pelo nível na tabela, palavra final do mestre em cima.

## 2. O modelo proposto — push gradual

*Levantado pelo Mizuki na v0.28, a partir da obra.*

**Quando dois domínios interagem.** Só quando as áreas **se sobrepõem** — o que exige estar dentro do domínio inimigo, ou dentro do raio de um domínio aberto. Expandir de fora de um domínio já erguido **não gera push**.

**O que a sobreposição faz de imediato:** o **acerto garantido é anulado para os dois lados**.

**E aí começa um push gradual**, cuja velocidade depende da **diferença de refino**. Vence o mais refinado.

**Duas vantagens no push:**

| vantagem | de quem | o motivo |
|---|---|---|
| sai mais rápido e empurra melhor | quem tem **efeito de acerto garantido inofensivo** | um Acerto que não fere se estabelece antes |
| empurra melhor | quem está com a **barreira aberta** | — |

**O que o perdedor leva:** domínio destruído, técnica queimada (o **Rescaldo**), e fica **exposto ao acerto garantido do vencedor**.

**Domínios equivalentes:** o desfecho cai sobre **o primeiro que sofrer dano pesado ou tiver o domínio colapsado**.

**Domínio incompleto na disputa:** não fecha barreira, **não recebe acerto garantido nem morte garantida**, e serve para **anular o acerto garantido alheio e abrir brecha de fuga**.

**Qualquer push pode terminar em buraco na barreira** em vez de conquista.

**A barreira continua sendo alvo físico legítimo**, e é **mais vulnerável por fora quanto mais reforçada estiver por dentro**.

## 3. Os seis números que este modelo pede, e nenhum existe

Esta é a razão de o modelo não ter entrado na v7.7.

| # | o número | contra o que ele precisa ser medido |
|---|---|---|
| 1 | **A velocidade do push** por ponto de diferença de refino | o refino vai de 1 a 10, e a diferença entre duas fichas do mesmo nível raramente passa de 3. Se o push levar mais rodadas que a duração, ele nunca resolve |
| 2 | **O tamanho da vantagem do efeito inofensivo** | é a peça mais interessante do modelo e a mais perigosa: ela **recompensa ter um Acerto fraco**, e sem número ninguém sabe se compensa escrever um Acerto de propósito inútil |
| 3 | **O tamanho da vantagem da barreira aberta** | e se ela empilha com a de cima |
| 4 | **O que é "dano pesado"** | é o desempate de domínios equivalentes, e hoje é julgamento puro — não passa no filtro multi-mestre |
| 5 | **A chance de o push virar buraco** em vez de conquista | uma ramificação a mais na resolução, e ela precisa de peso |
| 6 | **A curva inversa da barreira** — mais reforçada por dentro, mais frágil por fora | é a que mais pode inverter: se reforçar aumenta o risco líquido, ninguém reforça, e a mecânica nasce morta |

**E um sétimo problema, que não é número:** o modelo é uma disputa que dura várias rodadas dentro de uma duração que hoje é de 3 a 5 rodadas. Os dois relógios competem, e o push precisa caber no menor deles.

## 4. O que já foi conferido, e vale para os dois modelos

- **`Empurrão` e `Estilhaço` estão OCUPADOS** — os dois são Melhorias do manual, e nenhum pode batizar peça deste subsistema. `Sobreposição` e `Colapso` voltaram **LIVRES** na triagem.
- **`Queima` também está ocupada** (Melhoria: *"metade dos dados de novo, no começo do próximo turno do alvo"*), e foi por isso que a queima de técnica virou **Rescaldo**.
- **A anulação mútua do acerto garantido é a peça mais barata do modelo** e a que menos depende de número — ela pode entrar antes das outras seis, se a peça 12 demorar.

## 5. Por onde a peça 12 começa

1. **Decidir qual modelo vale**, e mandar o outro para `99-arquivo/` com o motivo escrito.
2. Se for o push: os seis números, na ordem 1 → 4 → 2, porque o 1 diz se ele cabe na duração, o 4 é o que quebra o filtro multi-mestre, e o 2 é o que pode inverter o incentivo.
3. Validador próprio, no molde do `conferir-expansao.py`: o push resolve dentro da duração, a vantagem do inofensivo não paga escrever Acerto inútil, e a curva inversa da barreira não faz reforçar ser burrice.

# Sincronização candidata — catálogo de Fundamento

**Estado:** patches preparados para integração futura, junto do núcleo de Fundamento lote 01. **Não aplicados às fontes publicadas.** A decisão local não equivale a validação integral do catálogo R07.

Fonte principal: `sistema/05-material/livro/manual/40-fundamento.md`.
SHA-256: `8ec6cd54f8fbb0cc7e98874a5242890a3b3392a792ec1cdef959abcec4b70d96`.

Catálogo duplicado: `sistema/05-material/livro/manual/60-invocacoes.md`.
SHA-256: `4df82e672d063b4d4bfe3394d93bb75052ec3e07d44d90b83c0ea32f10439f82`.

Rótulos: **E**, esclarecimento editorial de regra demonstrada; **I**, interpretação necessária de interface; **M**, mudança mecânica. Rótulos combinados indicam que parte da redação fecha uma lacuna com efeito mecânico. Números de linha orientam; conferir âncoras e trechos exatos antes de integrar.

Estes patches preservam os preços e as Famílias das entradas. Restrições da Técnica Máxima pertencem ao quadro próprio no manuscrito: não inferir que uma peça disponível no feitiço comum também pode ser comprada na Máxima.

## CAT-01 — Certeiro

- **Âncora:** ### Mira; linha da Melhoria `Certeiro`; linha 640 da fonte inspecionada.
- **Classificação:** M — redesign da resolução, mantendo preço e Família.
- **Motivo:** A versão antiga apenas trocava ataque por TR, opção que a montagem já permite sem pagar Melhoria. A candidata conserva uma escolha de precisão útil e distinta, com perda de dados pelo preço normal da peça.

**Antes**

```markdown
| `Certeiro` | `Média` | Sem rolagem de acerto. O alvo ainda faz o Teste de Resistência para metade. |
```

**Candidato**

```markdown
| `Certeiro` | `Média` | Só em feitiço com rolagem de ataque. Se o resultado final errar um alvo válido, causa metade dos dados de dano, arredondada para baixo, sem aplicar os outros efeitos. O dano do erro não é crítico. No acerto, a resolução e o crítico seguem as regras normais. |
```

**Conferência:** De Novo, quando disponível, é resolvido antes de conferir o erro final; não acumular metade do erro com o dano da nova tentativa. Não cabe em ficha só de TR, efeito automático, ataque sem alvo válido, sem alcance, sem trajeto ou sem visão exigida. Bloquear substitui a Defesa: se tornar o resultado final um erro, Certeiro resolve sua única parcela de erro. Aparar também causa erro, salvo o 20 natural; se houve acerto, não somar a parcela de erro ao dano normal. Redução de dano que preserve o acerto não ativa Certeiro. Atualizar interpretações antigas que dizem que Certeiro elimina crítico.

## CAT-02 — Fica

- **Âncora:** ### Área; linha da Melhoria `Fica`; linha 624 da fonte inspecionada.
- **Classificação:** M — duração fixa, limite de resolução e posição expressa.
- **Motivo:** A regra antiga dizia um minuto em sistema de rodadas de dez segundos, sem limitar reentradas. O candidato geral passou a seis segundos. Seis janelas globais evitam ampliar a persistência só pela mudança do relógio e fecham múltiplos gatilhos na mesma rodada. Não é alegação de que a regra antiga já tinha máximo de seis aplicações.

**Antes**

```markdown
| `Fica` | `Média` | A área continua ali por 1 minuto. Quem entrar ou começar o turno nela leva metade dos dados. Exige concentração. |
```

**Candidato**

```markdown
| `Fica` | `Média` | A área permanece no local, com concentração, na rodada da conjuração e nas cinco seguintes; termina no fim da última. A resolução inicial ocupa a oportunidade dos alvos afetados naquela rodada. Depois, entrar na área ou começar o turno nela resolve metade dos dados iniciais, arredondada para baixo, pela resolução registrada. Cada criatura recebe no máximo uma resolução do feitiço por rodada, mesmo se o ataque errar ou o TR evitar o dano. Não repete os outros efeitos nem se move com você, mesmo que a Forma inicial seja Aura. |
```

**Conferência:** Entrar e começar turno na mesma rodada produz uma resolução; sair e entrar novamente não produz outra; a resolução inicial seguida de início de turno na mesma rodada não produz outra. Mover a área por alguma capacidade não conta como entrada da criatura. Fica não usa reserva vitalícia de 4 × Classe; Concentrada/Duradoura não ampliam sua duração pela entrada própria dessas peças.

## CAT-03 — Salto

- **Âncora:** ### Área; linha da Melhoria `Salto`; linha 627 da fonte inspecionada.
- **Classificação:** M/I — limite e resolução definidos; preservação da exclusão histórica de gatilhos.
- **Motivo:** O catálogo não esclarecia resistência do segundo alvo nem quantos saltos uma área produz. A nova regra dá uma única aplicação secundária e exige resistência própria. O histórico de Alvo de Caça exclui Salto de seus gatilhos; ganhar uma rolagem para resolver o efeito não deve reabrir essa exclusão.

**Antes**

```markdown
| `Salto` | `Média` | Depois do primeiro alvo, pula para o inimigo mais perto a até 9 m com metade dos dados. |
```

**Candidato**

```markdown
| `Salto` | `Média` | Uma vez por conjuração, depois da resolução inicial, escolha um alvo inicial que tenha sido acertado ou falhado no TR. O dano salta para outro inimigo: o mais próximo dele a até 9 m, por trajeto desimpedido; em empate, você escolhe. O segundo dano usa metade dos dados iniciais, arredondada para baixo. Resolva um ataque com o mesmo bônus ou o TR da ficha contra o segundo alvo. Essa rolagem só resolve o Salto: não causa crítico, não ativa benefícios por realizar ou acertar outro ataque e não reaplica peças do feitiço. O salto não volta a saltar. Se a Forma for Toque, os dois alvos precisam estar a até 1,5 m de você. |
```

**Conferência:** Escolher o alvo inicial válido depois de resolver o disparo é decisão candidata expressa; não cria um salto por vítima da área. Uma falha inicial impede escolher aquele alvo como origem, mesmo que Certeiro cause metade do dano. Um 20 no ataque secundário segue a regra de acerto natural, mas não duplica dados. No TR secundário, sucesso recebe a metade prevista pela ficha, calculada sobre os dados secundários. Não somar melhorias da ficha a esse segundo pacote. A referência de 9 m é medida do alvo inicial; Toque mantém sua exigência adicional.

## CAT-04 — Estilhaço

- **Âncora:** ### Castigo; linha da Melhoria `Estilhaço`; linha 733 da fonte inspecionada.
- **Classificação:** M/I — um disparo secundário, alcance e resolução explicitados.
- **Motivo:** Vários resultados válidos de uma área não devem produzir múltiplos respingos sobrepostos da mesma Melhoria. “Quem estiver do lado” recebe medida de 1,5 m. A fonte não previa novo ataque/TR para o respingo; a candidata preserva essa resolução derivada automática, com gatilho inicial exigente, em vez de inventar um teste novo.

**Antes**

```markdown
| `Estilhaço` | `Leve` | Em crítico, ou quando o alvo falha o Teste de Resistência por 5 ou mais, metade dos dados respinga em quem estiver do lado. |
```

**Candidato**

```markdown
| `Estilhaço` | `Leve` | Uma vez por conjuração, se um alvo inicial sofrer um crítico ou falhar no TR por 5 ou mais, escolha um desses alvos como origem. Metade dos dados iniciais, arredondada para baixo e sem os dados adicionais do crítico, respinga nas outras criaturas a até 1,5 m dele. O respingo não faz novo ataque ou TR, não é crítico, não ativa benefícios por ataque e não aplica as outras peças do feitiço. Não produz outro respingo. |
```

**Conferência:** Um único respingo pode alcançar várias criaturas, como área; não é um respingo por vítima inicial. O pacote de dados conta uma vez no teto, sem multiplicar pelo número de criaturas próximas. Pode atingir aliados e o conjurador se estiverem na área secundária; não herda Escolher nem outras peças. Verificar em R07 o preço Leve, pois o limite novo fecha sobreposição mas não certifica dano esperado final. A escolha de metade dos dados antes do crítico é esclarecimento candidato de uma ambiguidade, registrado como efeito mecânico, não prova de redação antiga inequívoca.

## CAT-05 — Pacote de dano e alvos em área

- **Âncora:** ## Números da montagem; parágrafo após a tabela de Classes; linha 107 da fonte inspecionada.
- **Classificação:** M/E — correção do escopo contraditório do teto e decisões sobre repetições.
- **Motivo:** O teto publicado “somando todos os alvos” não funciona com os exemplos de área que aplicam o mesmo dano a cada criatura. A candidata preserva a operação de áreas e controla os pacotes da montagem. A decisão de Acúmulo aceita pelo usuário na v0.259 não é revogada silenciosamente.

**Antes**

```markdown
A coluna **Teto** é o máximo de dados de dano de um feitiço quando você soma todos os alvos e repetições. Contra um alvo só o limite é mais baixo: um feitiço comum para nos pontos da Classe. Quem alcança o teto num alvo só é a **Liberação Máxima**.
```

**Candidato**

```markdown
A coluna **Teto** limita os dados comprados pela montagem: **4 × Classe**. Um feitiço comum começa com até **3 × Classe**; a Liberação Máxima pode chegar a **4 × Classe** no dano inicial. Comprar peças reduz esse saldo conforme as regras de montagem.

Uma área aplica o dano a cada alvo; não divide os dados pelo número de criaturas. Rajada e Mais Um dividem os dados entre seus tiros ou alvos, antes das rolagens. Junto reparte cura ou benefício de apoio quantitativo compatível, sem copiar bônus ou condições. Um tiro ou alvo sem dados não aplica gratuitamente os efeitos de um acerto.

Some os dados iniciais e os pacotes adicionais de Salto, Queima e Estilhaço ao conferir o limite de **4 × Classe**. Cada pacote secundário é contado uma vez, sem multiplicar pelo número de criaturas que uma área alcança. Um multiplicador comprado, como os 25% de Remate, também entra nessa conferência: 8d8 multiplicados por 1,25 equivalem a 10d8. Reduza os dados iniciais se necessário; descartá-los não concede pontos.

Salto e Estilhaço têm, cada um, no máximo um disparo secundário por conjuração. Repetições não reaplicam automaticamente outras peças, nem criam cadeias recursivas. Fica tem duração e limite próprios, sem uma reserva de 4 × Classe para todos os danos futuros da área. Acúmulo mantém a exceção de usos sucessivos descrita em sua entrada. A Técnica Máxima usa sua tabela e suas compatibilidades próprias.
```

**Conferência:** Não reaplicar o teto de 4 × Classe depois de todo crítico, resistência ou vulnerabilidade: ele é conferido na montagem e nos multiplicadores comprados. Não chamar isso de equilíbrio final de todas as áreas. Atualizar também a síntese “Teto de dano” e a Regra 2 do quadro de revisão, indicadas abaixo; texto antigo não pode ficar concorrendo com o novo.

## CAT-06 — Acúmulo e usos posteriores

- **Âncora:** ### Castigo; linha da Melhoria `Acúmulo`; linha 731 da fonte inspecionada.
- **Classificação:** E/I — preservação da decisão histórica; exclusão de crescimento retroativo.
- **Motivo:** ESTADO-ATUAL.md registra em v0.259 a aceitação pelo usuário de o acúmulo ultrapassar o antigo teto após continuidade contra o mesmo alvo. A correção do teto não deve apagar essa decisão. A tabela de progressão torna claro que o primeiro uso não começa com +1d8.

**Antes**

```markdown
| `Acúmulo` | `Média` | +1 dado por rodada seguida usando este feitiço no mesmo alvo. Para de somar em +3. |
```

**Candidato**

```markdown
| `Acúmulo` | `Média` | Usar este feitiço em rodadas seguidas contra o mesmo alvo acrescenta dados aos usos posteriores: +1d8 no segundo, +2d8 no terceiro e +3d8 no quarto e nos seguintes. O bônus para em +3d8 e é uma exceção ao teto comum de montagem. Ele não causa dano adicional naquele instante nem aumenta retroativamente Queima, Fica, Salto ou Estilhaço de usos anteriores. |
```

**Conferência:** A entrada continua exigindo rodadas seguidas e o mesmo alvo. Não ganha vários degraus por repetir o feitiço na mesma rodada. Interações detalhadas de perda/reinício, vários alvos e Remate permanecem na revisão do catálogo R07; esta sincronização não inventa uma nova cobrança de PE nem altera o máximo histórico +3.

## CAT-07 — Passo, Atrasar e Parado

- **Âncora:** ### Alcance; linha da Melhoria `Passo`; linha 607 da fonte inspecionada.
- **Classificação:** I/E — distinguir custo de ações e proibição de deslocamento.
- **Motivo:** Turnos candidato: Rodada inteira consome Padrão/Bônus/Movimento, preserva Reação. As restrições Atrasar/Parado têm a exigência adicional e expressa de não se mover. Máxima ou Liberação com Ação Completa, sem essas restrições, pode conceder Passo pela própria peça; isso não devolve a Ação de Movimento.

**Antes**

```markdown
| `Passo` | `Leve` | Você anda até 6 m antes ou depois do feitiço, sem provocar ataque de oportunidade. |
```

**Candidato**

```markdown
| `Passo` | `Leve` | Você anda até 6 m antes ou depois da resolução do feitiço, sem provocar ataques de oportunidade. É deslocamento concedido pela peça, sem gastar outra Ação de Movimento; o percurso precisa ser permitido pelo movimento que você possui. Atrasar e Parado impedem usar esse movimento no turno. O custo de Ação Completa, sozinho, não o impede. Condições que reduzem ou impedem movimento também afetam essa distância concedida. |
```

**Conferência:** Não confundir turno inteiro com condição de imobilidade. Fenda de Arrasto da Máxima continua funcional. Passo + Parado/Atrasar não torna funcional um gasto que só serviria para ativar bônus de saldo de Controle. A proibição de reembolso de Atrasar/Parado em Liberação continua valendo como regra expressa candidata.

## Remissões e duplicações a sincronizar na integração

1. **40-fundamento.md, “Números da montagem”:** a linha resumida `> **Teto de dano** = 4 × Classe em dados` deve identificar “teto do pacote da montagem, com exceções próprias”; não repetir “somando todos os alvos”.
2. **40-fundamento.md, quadro Regra 2:** substituir a frase que soma alvos/repetições pelo resumo do CAT-05 e remeter às exceções de Fica/Acúmulo. O antigo resumo contradiz a mudança se ficar isolado.
3. **60-invocacoes.md:** aplicar as entradas CAT-01 a CAT-04 e CAT-06/CAT-07 nos nomes correspondentes. Usar **Classe do efeito**, quando esse for o parâmetro da entidade; não trocar dados reduzidos/PE da entidade pela tabela do jogador. O procedimento de Máxima da entidade segue a sincronização separada `60-INVOCACOES.md`.
4. **Invocações, Salto/Estilhaço:** uma ativação do efeito equivale à conjuração para o limite de um secundário. Não tratar cada alvo inicial ou cada tiro como uma nova ativação.
5. **03-mecanica/01-atributos-acerto-defesa.md:** a explicação histórica de que Certeiro retira o ataque e perde crítico deixa de descrever a candidata. Preservá-la como histórico ou marcar substituição quando integrar; não usar o antigo percentual de precisão como validação do redesign.
6. **03-mecanica/03-economia-de-acao-e-iniciativa.md:** manter a exclusão de Salto/Estilhaço dos gatilhos de Alvo de Caça; a redação deve admitir que Salto ganhou rolagem própria sem se tornar novo ataque para gatilhos.
7. **ESTADO-ATUAL.md, decisão v0.259:** preservar a evidência bruta de Acúmulo e registrar eventual decisão posterior em adendo; não reescrever a fala histórica do usuário.
8. **Concentrada/Duradoura:** não estendem Fica. Revisar em R07 os demais efeitos de um minuto após a passagem de dez para seis segundos por rodada. Não converter todos em seis rodadas automaticamente.

## Conferências mínimas antes de aplicar

- Todas as âncoras “Antes” devem existir uma única vez no arquivo principal. As linhas de peças espelhadas devem aparecer uma única vez em Invocações, mesmo quando seus parâmetros próprios diferirem.
- Registrar os três casos Certeiro: erro final, acerto e acerto crítico; De Novo não permite receber dois resultados de dano.
- Uma área com seis alvos elegíveis gera no máximo um Salto e um Estilhaço, se ambos foram comprados e cabem no pacote; não seis de cada.
- Salto secundário não ativa Alvo de Caça, Marca/Ecoa, Estilhaço ou outro Salto; um 20 não amplia seus dados.
- Fica só resolve uma vez por criatura por rodada e termina no fim da sexta janela global. Entradas repetidas não prolongam nem renovam a cota.
- Acúmulo: usos consecutivos têm bônus 0/1/2/3/3; o bônus de um novo uso não altera efeito antigo que ainda esteja no campo.
- Passo em Máxima sem Atrasar/Parado funciona; Passo com uma dessas restrições não funciona; gastar a Ação Completa não devolve a Ação de Movimento.
- Revalidar preços Leves/Médios/Pesados e cenários de área; uma boa definição operacional não comprova equilíbrio numérico.

## Pendências de R07 conservadas

Preços e condições de Inescapável com Formas pagas; vários multiplicadores simultâneos; reajuste de Estilhaço se a nova resolução exigir; estado de Acúmulo com múltiplos alvos e interrupção de sequência; efeitos próprios equivalentes; Classe 0 com restrições embutidas; todas as demais linhas da matriz ainda marcadas pendentes. Nenhuma dessas pendências está silenciosamente aprovada por este arquivo.

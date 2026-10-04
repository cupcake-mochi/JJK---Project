# Revisão independente — R03

Leitor: **maxima**, distinto do autor. Manuscrito lido integralmente: `15ed0d3535dd08c546cc4d3de9e4385746c73eae15267b6fd14f2db553617908`. Snapshot em `R03-TEXTO-LIDO-MAXIMA.md`. Não alterei o manuscrito nem os donos das habilidades.

## Parecer

A direção resolve falhas reais: Aguentar e Insistir agora compartilham janela e exigência de socorro; custos não abrem uma segunda janela; dano corporal não vira dano de Alma; curas pequenas podem colaborar; a reserva de Integridade finalmente determina o estágio e recuperá-la pode remover penalidades. Não encontrei ciclo de cura/estado que gere ações, recupere os custos ou reinicie a janela.

Os quatro fechamentos operacionais foram incorporados pela raiz durante a revisão e conferidos por nova leitura. Resta confirmar a sincronização da habilidade de resgate. Não identifiquei outro bloqueador concreto do procedimento depois dessas correções; isso não equivale a aprovar o equilíbrio por partidas.

## Achados e resolução

### R03-IM01 — P2-interface

**Local:** Guia — Ainda Há Tempo; R03 Socorro, linha 382 do hash lido.

A regra geral agora impede a habilidade dedicada de emergência de levantar certos aliados com qualquer resultado dos dados, salvo outra cura.

**Caso:** No nível19, Bastião Con3 tem195PV e precisa39. Socorrista com atributo6 cura3d8+6, no máximo30; seu Cuidado comum exige alvo acima de zero e não completa esse tratamento.

**Correção proposta:** Exceção específica de limiar para Ainda Há Tempo, preservando preparo anterior, Reação, custo e uma vez por cena, sem alterar Cuidado comum. Levanta já possui exceção.

**Estado:** raiz concordou em avaliar sincronização; não aplicada pelo revisor.

### R03-IM02 — P2-procedimento

**Local:** Vida a zero / Janela, linha 334 do hash lido.

O marco da janela só é definido quando já existe iniciativa.

**Caso:** Queda ou armadilha reduz personagem a zero fora de combate, sem ordem existente; não é possível localizar três voltas.

**Correção proposta:** Organizar turnos de socorro ao ocorrer a queda e definir o marco inicial antes da primeira ação. Conservar rodadas de6s e nenhuma ação gratuita por iniciar a ordem.

**Estado:** resolvido no texto relido: iniciativa organizada na queda e primeira volta explicitada.

### R03-IM03 — P2-procedimento

**Local:** Recuperação depois da derrota, linha 384 do hash lido.

Não informa se o limiar ainda rege PV após Derrotado nem o destino do tratamento acumulado.

**Caso:** Referência80, tratamento10 e derrota; cura5 posterior. LeituraA: PV0/tratamento15. LeituraB: PV5/tratamento10. Se cura posterior completar20%, também falta deixar evidente quando marcar Sequela sem devolver consciência.

**Correção proposta:** Declarar destino do tratamento e regra de conversão depois da derrota. Conservar vedação de retorno à cena e não cobrar segunda Sequela na mesma queda.

**Estado:** resolvido no texto relido: tratamento vira PV ao ficar Derrotado; cura posterior normal; Sequela ao sair da derrota.

### R03-IM04 — P2-procedimento

**Local:** Derrota e morte / Descanso longo, linha 443 do hash lido.

A saída da inconsciência exige curto com atendimento, mas o longo restaura reservas sem declarar se satisfaz essa saída.

**Caso:** Resgatado chega vivo à base, conclui longo e tem PV/Integridade máximos; a leitura estrita ainda exige outra pausa curta antes de acordar.

**Correção proposta:** Dizer se e em quais condições o longo encerra o estado, preservando morte e consequências permanentes. Não presumir que curto e longo são o mesmo evento.

**Estado:** resolvido no texto relido: longo encerra inconsciência por derrota com ambas reservas positivas.

### R03-IM05 — P3-clareza

**Local:** Estabilizar, linha 394 do hash lido.

Ao alcance é menos preciso que o contato exigido por atendimento manual.

**Caso:** Arma de alcance ou outra habilidade amplia o alcance de ataque, mas não deveria ampliar automaticamente atendimento.

**Correção proposta:** Usar até1,5m, contato possível, uma mão livre e meios adequados. Preservar CD14, ação e Ofício correspondente.

**Estado:** resolvido no texto relido: 1,5m com acesso físico ao alvo.

## Dominância e custo de continuar lutando

Não há dominância estrita. Com referência80 e uma cura imediata de80, Aguentar volta com80; Insistir paga10 e volta no máximo com70. Aguentar também admite estabilização, que mantém o corpo vivo sem consumir PE. Insistir conserva ações, movimento, Bloquear e possibilidade de autocura, mas paga um máximo que persiste até descanso longo.

O custo pode ser pouco perceptível no mesmo confronto: se ambos recebem apenas20 de cura, os dois ficam com20PV; os10 de máximo perdidos só importam numa recuperação maior posterior. Por isso, Insistir continuará atraente para fichas capazes de se proteger ou socorrer. Isso condiz com sua função heroica, mas a matemática não prova que o jogador percebe o preço. Segundo Fôlego pode dispensar o primeiro custo uma vez por descanso longo sem gerar janela ou ações adicionais; é uma exceção concreta, não motivo para alterar toda a escada.

Com três Sequelas, nenhuma escolha permite outro retorno na cena da quarta queda. Trocar de Insistir para Aguentar não renova a janela nem devolve máximo. Nenhuma cura comum remove Sequelas. Esses limites fecham a repetição indefinida de quedas, inclusive com Levanta.

## Cura e escassez

A auditoria independente executou29 verificações,24 perfis de cura e4 comparações de interfaces, com distribuições exatas de d8. A Forma Cura comum sem peças alcança2×Classe d8 por3×Classe PE. Os números abaixo pressupõem fonte disponível, alvo compatível e tempo para usá-la; não estimam a frequência real de curadores na guilda.

| Perfil no nível30 | PV / limiar | Uma Cura14d8 | Duas Curas acumuladas |
|---|---|---|---|
| Bastião Con3 |305 /61 |61,36% |mais de99,999% |
| Emanador Con3 |212 /43 |99,22% |mais de99,999% |
| Bastião Con6 |395 /79 |3,51% |99,997% |
| Emanador Con6 |302 /61 |61,36% |mais de99,999% |

Uma Cura custa21PE; duas custam42PE, além das ações. O acúmulo corrige desperdício e permite resgate em equipe, mas um Bastião com muita Constituição pode exigir dois atendimentos máximos. Em uma janela de uma rodada, isso requer duas fontes ou outra ação permitida. A aptidão Energia Reversa7d8 não pode alcançar79 em um uso; Circulação10d8 quase nunca alcança. É uma redução expressiva da antiga saída de Insistir por1PV, coerente com eliminar a vantagem indevida, mas precisa ser apresentada como mudança de balanço.

Levanta continua valioso pelo resgate abaixo do limiar e por sua limitação própria. **Ainda Há Tempo** merece a exceção nominal de resgate: a reação e a preparação prévia deixariam de cumprir sua função para aliados ordinários no nível em que a habilidade é adquirida. **Ainda de Pé** não precisa receber essa exceção: é uma autocura geral e sua regra já conserva os requisitos de zero. **Passa Pra Mim** impede a queda antes dela, preservando sua função. Reparo do corpo, Cura comum, Reserva, Sugar e Energia Reversa são recuperação geral, não resgates que prometam ignorar limiar. Não encontrei outro resgate dedicado nos seis Caminhos e nas Rotas lidas.

## Dano repetido e tempo

Três ataques positivos contra um alvo já a zero podem consumir a janela inteira na mesma ação. Rajada, armas com múltiplos ataques e Queima por várias aplicações deixam de depender da soma de dano que antes protegia Insistir. Um único golpe de100 consome uma rodada; três de1 consomem três. A assimetria é deliberada na redação e compatível com a retirada do contador de50%, mas deve constar no registro de balanço. Defesas, Bloquear e vida temporária são mais importantes enquanto Insiste; Aguentar não pode Bloquear.

Não recomendo limitar por ação ou rodada nesta revisão: isso acrescentaria outra exceção à proteção e exigiria redesenhar o peso da pressão inimiga. Uma primeira avaliação de mesa deve incluir Rajada contra Insistir e socorro com duas Sequelas. Não foram jogados esses casos.

## Integridade

Concordo com estágios por fração e recálculo após cura. O modelo conferiu limites de Integridade26: perder6 mantém estágio0,7 alcança1,13 alcança2,20 alcança3 e26 alcança4. Curar de12 para17 retira o estágio2. Quatro danos de1 não expulsam o personagem por falhas extras de TR.

Estágio3 ainda concentra penalidades severas: desvantagem em ataque/TR, aumento de PE, movimento reduzido e teto de Classe pela metade. É coerente com uma reserva perto de esgotar, mas não é uma penalidade pequena. Estágio4 não permite recuperar a participação imediatamente com Remenda; exige saída da cena/atendimento, enquanto a reserva positiva remove as penalidades matemáticas. Essa distinção deve continuar explícita. Cura corporal e socorro não reconstroem a alma.

Os limites de Integridade permanecem mais baixos que PV em vários perfis; golpes de Alma ignoram as metades indicadas e atingem duas reservas. Remover TR adicional reduz a loteria punitiva, sem tornar Alma fraca. Não avaliei partidas ou frequência de acesso ao tipo. Não há nova afirmação de cânone nestes procedimentos.

## Alternativa mais simples

A alternativa realmente mais simples é qualquer cura válida encerrar a queda para **ambas** as escolhas, mantendo Sequelas e a janela. Ela elimina o contador de tratamento e o cálculo de20%, mas fortalece curas mínimas, retira parte da função de Levanta e aumenta a eficiência de autocura. O limite de três retornos evita repetição infinita, não impede que a pequena cura seja a decisão mais eficiente. Não recomendo substituir a candidata por essa alternativa agora.

Recomendo manter a regra atual com suas correções e usar uma ficha com **referência, janela, tratamento, Sequelas e máximo perdido**. Não transformar a ficha numa nova mecânica. O ganho de simplicidade já obtido vem de retirar o contador de50% e a janela pós-colapso, além do TR adicional de Integridade.

## Nome da condição

**Guarda Aberta** comunica melhor a perda de Bloquear e a exposição a críticos corpo a corpo. Incapacitado sugere incapacidade de agir, o que a regra expressamente conserva, e induz quem conhece outros RPGs a aplicar outra condição. Não encontrei habilidade aprovada com o nome exato Guarda Aberta que cause colisão.

Recomendo a troca transversal, conservando todos os efeitos e exceções. Revisar a gramática: “fica com a Guarda Aberta”, “contra ficar com a Guarda Aberta”, “enquanto estiver com a Guarda Aberta”. A regra que encerra agarrão quando o mantenedor recebe a condição deve ser preservada como regra expressa, pois o nome novo por si não a explica. Fluidez, Corpo Emprestado, tabelas, criação de Condição e validadores precisam da mesma alteração. Conservar alias histórico apenas no índice e nos registros de revisão, nunca duas condições diferentes.

## Natureza das alterações e limites

Morte não automática como padrão é uma decisão de política mecânica da campanha, mesmo quando resolve discricionariedade anterior. Recomendo classificar DR14 também como mudança de consequência, além de esclarecimento. A mesma cautela vale para cicatrizes sem bônus sociais permanentes: é alteração mecânica, corretamente registrada no lote.

Leitura e modelos foram executados por um agente independente do autor; não representam jogadores. Não inspecionei PDF ou diagramação. O alcance desta revisão é o texto lido, as fórmulas e as interfaces indicadas. Novas versões precisam receber conferência dos trechos alterados e hash atualizado antes de dar os achados como resolvidos.

## Atualização da interface R03-IM01

GUIA-38 aplicada no dono de Ainda Há Tempo, após autorização da raiz. A habilidade passa a encerrar a queda abaixo do limiar apenas enquanto Morrendo, conservando custos, frequência, preparo e valor de cura; não permite voltar depois de Derrotado. O autor deste parecer também é autor do Guia, por isso a revisão independente desse delta cabe à raiz. Este registro não modifica o snapshot R03 lido nem declara o delta já revisado independentemente.

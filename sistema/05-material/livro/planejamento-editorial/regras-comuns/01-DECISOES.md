# Movimento e terreno — decisões e fundamento da minuta

**02/10/2026 · proposta sobre a v0.331.** Documento de trabalho; não é regra publicada. [Texto candidato](01-MOVIMENTO-MINUTA.md).

## O que se quer produzir em jogo

O jogador deve conseguir escolher e calcular um percurso sem interromper a cena para reconstruir regras espalhadas. Um obstáculo perigoso precisa ter consequências compreensíveis antes da tentativa. Os especialistas em movimento devem conseguir fazer algo reconhecível além da travessia comum.

A primeira minuta reúne a base existente e propõe custos para terreno, escalada e natação. Preserva a economia de ações e os 9 m comuns. A intenção é manter as concessões das Trilhas aprovadas; os novos custos e as interpretações de interação continuam sujeitos às decisões registradas. Como os custos gerais ainda não existiam completos, suas consequências sobre as habilidades estão expostas abaixo: **proposta de preenchimento de lacuna também é proposta mecânica**, mesmo que tenha surgido numa revisão textual.

## Decisões da minuta

| ID | Texto candidato | Situação e motivo |
|---|---|---|
| M01 | Base 9 m; dividir movimento; Correr acrescenta metros; Desengajar protege da oportunidade; ação gasta sem andar não é deslocamento | Reunião de regras vigentes, sem reabertura dos números. Fontes: peça 03, manual O turno e histórico v0.11/v0.123/v0.218. |
| M02 | Terreno difícil custa 2 m por metro percorrido, sem repetir pelo número de causas | Proposta nova. Dá significado ao “custo adicional” já referido por habilidades; fácil de calcular por trecho. |
| M03 | Escalada/natação comuns custam 2 m por metro; junto de terreno difícil, 3 m por metro | Proposta nova. Cada dificuldade distinta acrescenta um custo, sem multiplicação sucessiva. Deslocamento específico retira apenas o custo da modalidade. |
| M04 | Movimento Acrobático custa 1 m por metro; terreno difícil ainda pode acrescentar custo; quota mede distância física | Proposta de conciliação. O custo comum de escalada tornaria inviável a aproximação inicial de parede seguida de salto. Não se estende a qualquer personagem nem dispensa testes/apoio. |
| M05 | Salto comum não consome a quota das modalidades acrobáticas; consome movimento disponível | Explicitação candidata, apoiada na distinção já feita em Parkour entre trecho acrobático e regras normais de salto. Não cria distância de salto nem sucesso automático. |
| M06 | Um teste por obstáculo e risco descritos; não repetir só porque mudou o turno | Proposta de procedimento. Evita converter uma travessia em várias chances arbitrárias de falhar. Mudanças concretas podem exigir outro teste. |

A tabela de custos **não resolve a combinação de todas as condições do jogo**. Lento foi conferido no exemplo porque seu efeito é claro. Rastejar/Derrubado, reduções múltiplas e a alteração do deslocamento no meio de um percurso precisam de casos próprios antes da integração. Não trocar “metade” por um custo sem conferir os efeitos dependentes.

**Fixar o Alvo:** a Vanguarda já aceita terreno difícil como requisito específico. A distinção proposta entre custo de percurso e valor de deslocamento não revoga essa permissão. Essa nota precisa acompanhar a integração e a validação, mesmo que não seja repetida na regra básica para jogadores.

## Pesquisa externa dirigida

Leitura das regras indicadas abaixo em 02/10/2026. Três sistemas de estruturas distintas foram cotejados. As conclusões para o Projeto M são escolhas de design nossas, não recomendações atribuídas às editoras. Não houve pesquisa de cânone de JJK nesta rodada nem uso de F&M para escolher mecânicas.

| Referência primária | Procedimento observado | Escolha para esta minuta |
|---|---|---|
| [D&D, Basic Rules 2024 — Rules Glossary](https://www.dndbeyond.com/sources/dnd/br-2024/rules-glossary/), entradas Climbing, Difficult Terrain, Swimming, Long Jump e Falling | Distingue distância e custo; terreno e modalidade onerosa acrescentam movimento. O salto horizontal usa o valor de Força com impulso; há teste separado para algumas aterrissagens. A queda causa dados por altura com teto. | O custo por trecho oferece uma boa referência de consulta. A fórmula de salto não deve ser importada: nossos atributos usam outra escala e Parkour pode substituir a perícia. Queda e aterrissagem exigem avaliação própria. |
| [Pathfinder 2e, Player Core — Basic Actions](https://2e.aonprd.com/Rules.aspx?ID=2343), p. 417; [Long Jump](https://2e.aonprd.com/Actions.aspx?ID=2378) e [High Jump](https://2e.aonprd.com/Actions.aspx?ID=2377), p. 235 | Um salto curto tem procedimento básico; saltos maiores usam Atletismo. No Long Jump consultado, há impulso, CD 15 e distância derivada do resultado no sucesso, limitada pelo deslocamento; falha volta ao salto básico. | Interessa a separação entre travessia simples e esforço maior. Não importar a economia de duas ações, a escala de CDs ou os resultados críticos para um sistema com outra estrutura de turno. |
| [Cairn, primeira edição — SRD](https://cairnrpg.com/first-edition/cairn-srd/), Rules/Saves e Combat/Actions | A descrição da situação e seu risco determinam quando há salvaguarda; o turno combina movimento e uma ação. O procedimento é menos dividido em ações específicas para cada travessia. | Reforça a pergunta “qual risco esta rolagem resolve?”. A menor quantidade de procedimentos funciona como contraste; o Projeto M precisa de mais referências comuns por circular entre mestres. |

O aproveitamento é funcional: ordem de consulta, gatilho de teste, custo e consequência. A redação do candidato foi feita para os termos e habilidades do Projeto M. A presença de um procedimento em outro jogo não prova seu equilíbrio aqui.

## Saltos: direção recomendada para a próxima decisão

**Preferir um salto curto que dispense teste em condições adequadas e testes de perícia para distâncias maiores ou apoios difíceis.** Atletismo continua como perícia comum. Acrobacia substitui apenas quando uma regra permitir, como no Parkour do Assassino.

Evitar vincular toda a distância máxima diretamente à Força: isso pode conservar o nome “Acrobacia” no kit enquanto esvazia sua utilidade para um personagem de Destreza. O investimento em Força já melhora Atletismo; uma distância fixa somada ao mesmo atributo precisa justificar a dupla vantagem.

O procedimento deverá declarar o salto pretendido e a CD antes da rolagem, cobrar movimento suficiente e resolver o mesmo risco uma só vez. “Saltar” e “aterrissar” não devem virar dois testes obrigatórios quando descrevem a mesma dificuldade. Uma aterrissagem que introduza um perigo independente ainda pode exigir tratamento próprio.

**Alternativas ainda em comparação:** distância curta comum + CD por faixas para esforços maiores; ou distância máxima obtida pelo resultado do teste. A primeira permite anunciar a chance antes de tentar; a segunda dá aproveitamento graduado ao resultado, mas exige tratar a posição final quando não se alcança o destino. A recomendação inicial é a primeira. Distância segura, impulso, alcance vertical e consequências de falha continuam por calibrar — não há tabela de metros escondida nos exemplos desta minuta.

**Bordas e mãos:** distinguir altura atingida pelos pés de alcance para se segurar. Não usar a altura do personagem como um novo atributo sem decidir se essa precisão ajuda a mesa. O requisito de pelo menos uma mão ocupada do Assassino já é explícito e precisa sobreviver.

## Quedas: o risco precisa ser escolhido antes do dado

A descida com apoio e a queda livre precisam de procedimentos distintos. Descer 4,5 m controladamente para ativar Parkour não é autorização para ignorar qualquer impacto de 4,5 m, nem exige automaticamente sofrer dano por descer.

Concussão já é o tipo associado a quedas. Faltam dano por altura, mitigação, posição ao terminar e sequência quando uma habilidade empurra ou lança. Definir esses elementos pode acrescentar dano recorrente a Mão Pesada ou Projeção Marcial. Um texto de movimento não deve concedê-lo sem revisão do conjunto.

A escala de Vida mostra a escolha necessária: com Constituição 2, um Incursor tem 14 de Vida no nível 2 e 182 no nível 30; um Bastião tem 23 e 275, respectivamente. Um mesmo impacto de média 14 representa 100% e 7,7% da Vida desses dois Incursores; nos Bastiões, 60,9% e 5,1%. Isso pode ser coerente com personagens cada vez mais resistentes. Não é defeito a corrigir automaticamente escalando a queda pelo nível da vítima.

| Caminho de design | Benefício | Custo ou risco a examinar |
|---|---|---|
| Dano por altura independente do nível | O mesmo lugar continua causando a mesma ameaça física; crescimento de resistência é perceptível | Alturas moderadas perdem peso relativo; um teto muito baixo pode tornar quedas extremas irrelevantes. |
| Faixas de dano ambiental próprias | Facilita adjudicação de perigo e pode cobrir impactos diferentes | Exige uma régua estável; não transformar toda queda em dano arbitrário escolhido depois da ação. |
| Dano proporcional à Vida | Mantém ameaça relativa | Faz a mesma queda causar mais dano absoluto em quem tem mais Vida; reduz o valor da resistência adquirida. Não é a recomendação inicial. |

**Direção inicial:** altura e circunstâncias determinam o perigo; a progressão do personagem determina quanto ele suporta. Comparar opções de mitigação por Acrobacia sem torná-la imunidade geral e sem repetir o teste que já resolveu a aterrissagem. Dados, teto e custo da mitigação permanecem abertos.

## Casos de compatibilidade

| Caso | Resultado desta rodada |
|---|---|
| 9 m: andar 3 m, atacar e andar 6 m | Preservado pela reunião textual. |
| 9 m: chão 3 m + entulho 1,5 m + chão 3 m | Consome 9 m na proposta; percorre 7,5 m. |
| 12 m e Lento; depois 1,5 m em terreno difícil | Movimento disponível 6 m; gasta 3 m; restam 3 m. |
| Escalar 4,5 m normalmente ou 9 m com deslocamento de escalada 9 m | Ambos consomem 9 m; benefício da modalidade preservado. |
| Escalar 3 m de trecho também difícil, sem deslocamento específico | Consome 9 m; com deslocamento específico, consome 6 m. |
| Incursor de 12 m: parede regular de 6 m e salto depois | A parede consome 6 m do movimento e da quota; restam 6 m para o salto. Distância e teste do salto ainda pendentes. |
| Incursor percorre 3 m de parede difícil | Consome 6 m de movimento e 3 m da quota acrobática. |
| Incursor de 12 m usa Correr após chegar à quota | Aumenta movimento disponível, sem reiniciar quota no mesmo turno. Renovação fora do turno ainda aberta. |
| Fixar o Alvo e terreno difícil | Permissão específica preservada; precisa de verificação de integração. |
| Pugilista atravessa água e termina sem apoio | A habilidade não sustenta posição final; natação e consequências devem ser conciliadas. |
| Assassino desce 4,5 m com apoio versus cai 4,5 m | Casos distintos registrados; dano e mitigação não fechados. |
| Mão Pesada eleva alvo / Projeção junto a precipício | Bloqueio de publicação do subsistema de queda até definir direção, trajetória e dano. Não é veto à habilidade atual. |
| Passo Guardado depois de consumir a quota acrobática | Renovação da quota precisa de decisão explícita; não há resposta implícita na minuta. |

Para a lista ampliada, consulte [interações auditadas](EVIDENCIA-INTERACOES.md) e [escala, probabilidades e critérios](EVIDENCIA-ESCALA.md). Estes dois arquivos registram análise independente anterior à minuta; não são aprovação do texto novo.

## Validação editorial e limite da entrega

O texto deve permitir localizar custo, exceção e exemplo sem ler a justificativa do autor. Notas de decisão ficam fora da futura versão para jogadores. A distinção entre proposta e regra vigente deve continuar visível enquanto houver trabalho de design.

Revisão por agentes, conferência de contas e comparação de fontes podem encontrar contradições. Não certificam diversão, naturalidade da voz ou facilidade para jogadores reais. O teste com leitores fica para depois, como pedido pelo Mizuki. O próximo teste de abertura deve manter a cena melhorada e recuperar a apresentação específica do Projeto M, conforme [retorno sobre a r2](../evidencias/abertura-retorno-pos-r2.md).

# Retorno à tarefa de integração — Invocações

**MODELO-DE-RETORNO.md preenchido · consolidação v0.2 · 24/09/2026.**

## 1. Identificação

**Recorte:** ações básicas e especiais, movimento, reações, intenções persistentes, coordenação e autonomia de entidades em campo. A discussão começou com uma invocação e ampliou para duas/três apenas na distribuição de básicas e na coordenação. Não foi desenvolvido o subsistema completo.

**Arquitetura inicial:** candidata B v0.1, com Padrão/Bônus/Movimento compartilhados, atuação conjunta de ataques reduzidos e uma Reação pessoal mais uma coletiva.

**Arquitetura resultante:** atuação básica e Movimento próprios por entidade, uma única Reação coletiva das invocações, Bônus do usuário para redirecionar uma intenção comum e Padrão para comandar uma especial que substitui a básica de uma entidade. Básicas e especiais não podem ser acumuladas pelo mesmo comando nessa rodada.

**Fontes efetivamente consultadas no trabalho registrado:** `LEIA-ME.md`, `PROMPT-PARA-COLAR.md`, `01-CONTEXTO-E-STATUS.md`, arquiteturas e protótipo integrais; capítulos gerais selecionados; trechos pertinentes do Guia v0.4; análise intermediária e decisões da conversa. Na preparação deste retorno foram relidos os dois arquivos de orientação e o modelo, o capítulo 11, as seções de Bloquear/Aparar do capítulo 10, trechos de condições do capítulo 15 e as seções pertinentes do Guia. Não foi relido o projeto inteiro nem presumido acesso ao estado atual do repositório.

O snapshot de referência do pacote é `main` em `ba1e0df6f05dad71659eed2abd06c43d22963834`, conforme seu contexto; não foi verificado que esse continue sendo o estado do work. Usar os arquivos reais disponíveis antes de integrar.

## 2. Decisões explícitas de Mizuki

Os trechos entre aspas são mensagens do usuário nesta conversa, não citações de cânone nem recomendações do assistente.

| Decisão | Evidência textual do usuário | Alcance |
|---|---|---|
| Acesso funcional fora do Evocador | “a invocação ou lutaria lado a lado como rotina basica ou ela lutaria por conta” | Participação não exige a classe; não estabelece acesso gratuito ou números. |
| Autonomia integrada ao investimento do vínculo/entidade | Escolheu “um investimento na própria invocação/vínculo, deixando a rotina disponível enquanto ela estiver manifestada” | Não exige pagamento periódico só para habilitar a rotina; não elimina sustentação particular. |
| Continuidade durante inconsciência | “Eu prefiro que ela continue agindo seja parte da autonomia básica dela.” | Entidade já em campo e funcional; não decide morte ou acesso aos PE do usuário. |
| Movimento independente | “o deslocamento não deva necessitar de ordem nenhuma [...] vindo da invocação de forma independente” | Sem microcomandos e sem ceder Movimento do personagem; não permite movimento ilimitado. |
| Básicas autônomas e especiais ativas comandadas | “ser restrito a uma atividade básica faça mais sentido” | A especial ativa exige intervenção; não obriga a repetir um único ataque. |
| Várias escolhas básicas | “multiplas ações básicas [...] além de atacar, ter as ações básicas do sistema” | Variedade de escolhas, não execuções simultâneas gratuitas. |
| Padrão para comandos especiais | “comandos especiais necessitem sim de uma ação padrão pra executar” | Base escolhida; detalhes de alvo, PE e oportunidade exigem integração. |
| Bônus muda a tarefa | “a ação bônus serviria para trocar a intenção inteira da criatura por uma tarefa diferente” | Não taxa cada básica coerente com a intenção. |
| Proteção reativa autônoma | “poder acontecer de forma autonoma torna mais interessante” | Respostas conforme gatilho/custo da ficha, sem autorização anterior. |
| Uma coletiva para todas as invocações | “ter só uma para todas” | Separada da pessoal; substitui a dúvida anterior sobre uma Reação por corpo. |
| Um comando pode repetir a mesma nova intenção | “a mesma para diversas [...] contanto que não seja diferente para cada uma”; depois: “é uma boa base” | Até X destinatárias, sem fórmula aprovada; tarefas distintas exigem comandos distintos na base. |
| Básicas próprias por entidade | “melhor cada uma ter suas atuações básicas próprias” | Não compartilhar uma única básica entre todos os corpos. |
| Kit com possibilidades de crescimento e ações gerais fora dele | “um kitzinho de ações que poderia vir até a aumentar ao longo dos níveis [...] sem necessariamente consumir esse ‘kit’, como empurrar, agarrar” | Não há progressão, quantidade ou execução gratuita aprovada. A distinção repertório/recurso é explicitada como redação operacional. |
| Especial substitui e não acumula com a básica | “a especial comandada substitua a básica daquela invocação na rodada” | Só a destinatária cede a básica; não elimina a atuação das demais. |
| Básica usada impede especial no mesmo ciclo | “Impedindo até dela poder fazer a ação caso já tenha executado a ação básica da rodada, mesmo como ordem” | O comando não restaura uma oportunidade gasta. |
| Acúmulo por Evocador fica para depois | “vamos deixar para matutar isso depois com o ‘o que o caminho pode ou não pode dar’” | Não criar ou prometer a exceção, nem declarar equilíbrio. |
| Encerrar ao atingir o escopo | “não suponha nada [...] irei para o ‘work’, mas preciso que você me avise quando isso acontecer” | As duas pendências estruturais finais foram resolvidas. A recomendação é retornar agora. |

**Não aprovado:** “Possivelmente executando apenas na proxima rodada” abre a possibilidade de comando diferido; não define uma fila, pagamento antecipado, validade ou execução garantida.

A fala sobre personagens da obra é referência de experiência. Não foi estabelecida uma lei universal de senciência, persistência após desmaio ou custo de comando em JJK. A pesquisa anterior não foi uma leitura integral de todos os capítulos citados.

## 3. Proposta revisada integral

A versão integral está em **`02-PROPOSTA-REVISADA-INTEGRAL.md`**, integrante desta entrega. Ela contém iniciativa, relógio, recursos, kit e básicas gerais, redirecionamento, especiais, Movimento, reserva coletiva, defesa, consciência/condições, Preparar, ações concedidas, Guia, comunicação, exploração e entrada/troca.

**Núcleo escolhido:** personagem e entidades mantêm participação própria; objetivos persistem; Bônus coordena a nova tarefa comum; Padrão mobiliza uma especial no lugar da básica ainda disponível de uma entidade; uma coletiva resolve respostas autônomas. A perda de consciência do usuário não cancela sozinha a atuação de uma criatura sustentada.

**Hipóteses mantidas identificadas:** iniciativa conjunta e renovação no início do turno do invocador; uma básica por ciclo como ensaio; equivalência com Padrão para condições; ausência de Bônus extra por corpo; conversão para básicas originalmente de Bônus; autorização de uma única utilização da especial; procedimento de seleção reativa. Não atribuir aprovação de cada detalhe ao usuário.

## 4. Mudanças em relação ao protótipo v0.1

| Antes | Depois | Motivo | Status |
|---|---|---|---|
| Uma Padrão escolhida entre personagem e entidade | Básicas próprias por entidade, além da Padrão do personagem | Participantes ativos sem empréstimo permanente de ação | Decisão autoral; número/progressão ainda para ensaio |
| Padrão + Bônus autoriza dois golpes reduzidos | Participação básica conjunta não exige essa opção | Não condicionar a rotina lado a lado a uma manobra especial | Direção escolhida; dados antigos não transportados |
| Movimento compartilhado para até dois corpos | Movimento independente por entidade | Dispensa microcomandos e dependência do personagem | Decisão autoral; metros e conversões não fechados |
| Intenção não produzia atividade sem ação compartilhada | Intenção orienta a básica própria | Autonomia mecânica mínima efetiva | Decisão autoral |
| Usuário inconsciente retirava Padrão/Bônus/Movimento compartilhados | Criatura funcional mantém atuação e Movimento próprios | Separar incapacidade do usuário de sustentação | Decisão autoral |
| Comunicação sem novo custo de Bônus especificado para a tarefa | Bônus redireciona uma nova intenção comum a até X | Diferenciar coordenação de escolha interna da básica | Decisão autoral; X pendente |
| Reserva coletiva ainda candidata | Uma coletiva aprovada, separada da pessoal | Limitar respostas sem exigir autorização prévia | Decisão autoral |
| Capacidades especiais e compartilhamento antigo | Padrão do invocador + substituição da básica da destinatária | Especial exige compromisso, sem duplicar atuação | Decisão autoral final |
| Cartões e valores de bancada | Kit customizável e ações gerais sem ocuparem suas escolhas | Não reduzir a criatura ao ataque impresso | Direção escolhida; construção futura |
| Hipótese de eficiência por Bônus | Reservada para avaliação posterior | Evitar desconto universal ou antecipação do Caminho | Adiada, não rejeitada definitivamente |

## 5. Exemplos efetivamente discutidos

Nenhum exemplo abaixo foi uma sessão com jogadores. Rolagens foram escolhidas para explicar o procedimento. Números não foram aprovados como ficha ou orçamento.

### E1 — B v0.1: ataque conjunto e interceptação (histórico, não regra vigente)

Personagem e Guardião alcançam o inimigo por trajetos livres de 4,5 m, terminando adjacentes a ele e entre si. Intenção: acompanhar, enfrentar ameaças e proteger. Uma ação de Movimento compartilhada move ambos; Padrão + Bônus pagam dois golpes de 1d6. Ataques `14+4=18` e `12+4=16` causam 4 e 3. O inimigo ataca o personagem com `13+4=17`; Bloquear `6+6+(15−11)=16` falha. O Guardião gasta a coletiva para receber o acerto e 7 em 2d6, indo de 36 a 29 PV. Resultado: 7 de dano em cada lado; três ataques/3d20, um Bloquear/2d10 e quatro d6 de dano. Reação pessoal não gasta; nenhum TR ou PE no recorte. Manifestação anterior fora do exemplo. Limitação: demonstra a bancada antiga, não valida a autonomia revisada.

### E2 — Uma básica própria enquanto o usuário aciona o mecanismo

Personagem junto do mecanismo; Guardião a 4,5 m do inimigo; caminho livre. Intenção: enfrentar aquele inimigo enquanto a passagem é aberta. Padrão do personagem aciona o mecanismo, sem teste; Guardião usa Movimento próprio de 4,5 m e básica de ataque: `14+4=18`, dano 4 em 1d6. Inimigo responde contra o Guardião: `13+4=17`, 7 em 2d6; defesa fixa, sem Bloquear, Guardião 36→29 PV. Dois ataques/2d20 e três d6; sem TR, Reação ou PE no recorte. Bônus e Movimento do personagem não gastos. Limitação: valores artificiais, sem preço de aquisição/sustentação.

### E3 — Uma entidade escolhe Esquivar em vez de atacar

Personagem junto do mecanismo; Guardião a 4,5 m do inimigo, intenção de guardar a entrada. Personagem gasta Padrão no mecanismo, sem teste. Guardião anda 3 m, termina a 1,5 m e usa a básica em Esquivar. Inimigo escolhe atacá-lo: desvantagem com 16 e 7, `7+4=11`, erra Defesa 15. Uma básica, uma Padrão pessoal e uma inimiga; um ataque/2d20, nenhum dano rolado, Bloquear, TR ou PE. Guardião conserva 36 PV; reservas reativas não usadas. Limitação: Esquivar não obriga a escolha de alvo do inimigo e a parte ambígua do TR de Esquivar não foi aplicada.

### E4 — Duas básicas próprias: guardar e vasculhar

Personagem no mecanismo, Guardião junto da entrada e ao alcance de um inimigo, Batedor diante de recipiente aberto ao alcance. Intenções já dadas: guardar a entrada e procurar a chave. Personagem usa Padrão no mecanismo; Guardião usa sua básica em Esquivar; Batedor usa a dele em Vasculhar, `14+4=18` contra CD 14 e localiza a chave. Inimigo ataca Guardião com desvantagem, 16 e 7: `7+4=11`, erra Defesa 15. Uma busca e um ataque/3d20; nenhum Movimento, Reação, Bloquear, TR, dano rolado ou PE no recorte. Bônus livre: não houve novo objetivo. Limitação: localizar não autoriza todas as interações posteriores, e duas tarefas ativas constituem aumento real de participação.

### E5 — Disputa pela coletiva e decisão final da especial

Foram discutidos, sem rolagens, dois procedimentos. No primeiro, Guardião intercepta e consome a coletiva; uma segunda entidade não pode aproveitar oportunidade posterior com a reserva gasta. No segundo, o usuário compara dedicar sua Padrão a uma especial substitutiva ou conservar a rotina personagem + básica. A decisão final proíbe a especial na mesma rodada após a básica; eventual ordem para a próxima permanece pendente. Não há dano, teste, custo de PE, distância ou êxito demonstrado por esses exemplos procedimentais.

## 6. Verificações realizadas

**Análise textual desta consolidação:** confronto das decisões explícitas com o histórico, leitura do modelo de retorno e conferências pontuais das regras citadas. Não se afirmou leitura completa do repositório atual.

**Histórico de matemática:** a análise intermediária registra enumeração de acerto normal/vantagem/desvantagem e comparação entre ataque básico e Ajudar. Também registra 22 verificações locais em seu modelo então codificado. Esses resultados pertencem àquela versão e estão conservados no ZIP de referência; não foram reexecutados para esta consolidação nem certificam as últimas decisões, a reserva coletiva em todas as combinações ou comandos diferidos.

**B v0.1:** os 243 testes registrados no pacote inicial são históricos. Não foram utilizados como validação da arquitetura resultante.

**Preparação de arquivos nesta etapa:** geração dos documentos novos, cópia intacta das duas referências ZIP, verificação de integridade dos arquivos de entrada disponíveis e conferência do pacote de retorno. Essas checagens são de arquivos, não testes de regras.

**Não realizado:** playtest com pessoas, simulação completa de combate da versão consolidada, auditoria de todos os Caminhos, implementação no work, edição de manual/Caminhos, commit ou push. Não houve nova pesquisa externa nesta preparação final.

## 7. Alternativas recusadas ou adiadas

| Alternativa | Tratamento e autoria |
|---|---|
| Compartilhar uma única básica entre todas as entidades | Não escolhida por Mizuki: preferiu atuação própria de cada uma. |
| Renovar ordens para manter uma tarefa básica | Contrária à direção escolhida de intenção persistente e autonomia. |
| Cobrar Bônus por cada escolha de básica dentro da tarefa | Não adotada; a Bônus foi destinada pelo usuário à mudança de intenção. |
| Dar uma Reação por invocação | Mizuki preferiu uma coletiva para todas. |
| Liberar todas as especiais autonomamente | Mizuki preferiu básicas autônomas e especiais ativas comandadas. |
| Especial adicional à básica por comando comum | Não escolhida na decisão final; há substituição e bloqueio depois de agir. |
| Comando eficiente de Bônus e básica + especial via Evocador | Adiados para discussão do espaço de poder do Caminho, sem compromisso de implementação. |
| Fila para executar comando na rodada seguinte | Possibilidade levantada pelo usuário; não aprovada ou rejeitada. |
| Fórmula metade da Essência | Candidata de capacidade de redirecionamento, não fórmula escolhida. |

## 8. Pendências e impactos

**Não bloqueiam o retorno; exigem definição ou hipótese explícita no work:** relógio de rodada/turno e renovação; comando diferido; conteúdo/custos do kit e ações gerais; primeira ordem; meios/alcance de comunicação e limite X; relação entre redirecionar e comandar uma especial; entrada/troca e saldo de ações do novo corpo; sustentação, duração, PE e acesso quando o usuário cai; limites e manutenção de especiais; condições e concessões externas.

**Não fechar nesta etapa:** construtor, progressão, dano final, vida, capacidade/pesos/Presença, limite de corpos, aquisição, captura, derrota/morte permanente e repertório de reserva. Nem todas essas questões precisam virar perguntas autorais antes de um pequeno ensaio de integração; distinguir escolha de experiência, hipótese testável e dado ausente.

**Riscos a medir:** a básica pode ajudar um aliado forte em vez de atacar; mais corpos ampliam tarefas paralelas, posições, cobertura, percepção e vida acessível; a coletiva limita utilizações reativas, mas mais entidades ampliam seus pontos de origem e opções. Padrão + substituição cobra duas contribuições do conjunto: a especial precisa justificar esse custo, sem supor equivalência automática entre Padrão e Bônus.

**Lacunas de referência preservadas:** resolução completa de Agarrar/Derrubar e Empurrar; “TR de Destreza” em Esquivar versus os quatro TR do projeto; diferença de perícias entre tabela e explicação de Estudar; zero PV versus inconsciência efetiva. O cartão Controlador precisa ser distinguido de uma manobra geral antes de cobrar PE por Derrubado adjacente. Não corrigir silenciosamente o manual.

**Quatro Caminhos:** preservar v0.4, Estocada e a ausência de aumento de PE por atributo no Emanador. A Bônus de redirecionamento disputará recursos de fichas existentes; não alterar essas fichas para acomodá-la. O Guia deve ser conferido na versão v0.4, inclusive suas exceções de nível alto; ataques concedidos não herdam Sequência. Não há autorização para definir habilidades novas do Evocador neste retorno.

## 9. Próximo passo recomendado

**Retornar ao work agora.** As duas escolhas estruturais finais foram resolvidas: básicas individuais e especial substitutiva sem execução após a básica na mesma rodada. Não é necessário prolongar este chat com o tamanho do kit ou a futura classe.

No work, a próxima etapa delimitada é reconciliar esta proposta com os arquivos reais e preparar uma bancada de integração com poucas entidades distintas, incluindo uma utilitária, sem fechar catálogo ou Caminho. Usar ações e capacidades cuja resolução esteja escrita; explicitar qualquer hipótese de relógio ou custo; registrar efeitos da substituição, ajuda, coletiva, redirecionamento e troca. Se uma lacuna bloquear a execução do ensaio, isolá-la antes de inventar uma solução.

**Arquivos entregues:** `00-LEIA-ME-E-PROMPT-WORK.md`, este `01-RETORNO.md`, `02-PROPOSTA-REVISADA-INTEGRAL.md`, manifesto e cópias de referência. Nenhum arquivo original foi editado para preparar esta entrega. Este documento não autoriza modificação do repositório, manual ou Caminhos, nem commit/push.

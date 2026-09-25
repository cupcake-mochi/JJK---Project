# RASCUNHO — integração de ações e autonomia v0.2

**24/09/2026. Conferência documental concluída; ensaio proposto, ainda não executado.**

## 1. O que mudou e já não precisa ser perguntado

A básica e o Movimento pertencem a cada entidade, e o personagem conserva seus recursos. A Bônus redireciona uma intenção comum; a Padrão comanda uma especial que ocupa a básica ainda disponível da destinatária. Se ela já usou a básica, não executa a especial no mesmo ciclo por esse comando. As demais entidades conservam suas atuações. Uma Reação coletiva atende às invocações e fica separada da pessoal. Uma criatura já existente e funcional mantém sua autonomia quando o usuário fica inconsciente.

Isso substitui o empréstimo constante de ações, o Movimento compartilhado e a manobra de dois golpes reduzidos da candidata B v0.1. Também retira a premissa de que a inconsciência do dono impede a atuação básica. Não é um ajuste de números em B: mudou a origem dos recursos de ação.

São decisões explícitas do retorno. Não estão aprovados: quantidade de básicas por ciclo/progressão, iniciativa e relógio exatos, ausência de Bônus próprio, equivalência de básica com Padrão para condições, X, metade da Essência, alcance de ordens, primeira intenção, fila futura, valores de ficha, custos de entrada/troca, acesso aos PE do inconsciente ou capacidade em campo. A direção da substituição foi aprovada; o termo “ciclo” ainda precisa de redação operacional compatível com turno/rodada.

O investimento no vínculo inclui a autonomia; não haverá taxa periódica apenas para repetir a rotina. Isso não declara sustentação gratuita nem acesso gratuito à entidade. O Evocador continua posterior ao subsistema; básica + especial não foi concedida a ele.

Fontes autorais: [retorno, §§2–4 e 7–9](retorno-recebido/01-RETORNO.md) e [proposta integral](retorno-recebido/02-PROPOSTA-REVISADA-INTEGRAL.md). Os textos históricos não reabrem as escolhas resolvidas.

## 2. Estado real dos arquivos

| Item | Verificação desta retomada |
|---|---|
| Projeto principal | `/media/mizuki/HD Externo II/Claude/Claude 2`, branch `main`, commit `ba1e0df6f05dad71659eed2abd06c43d22963834`; sem alterações locais. |
| Pasta RPG -JJK | Branch `main`, commit `dff171d36148c7163fdebfdaf8ec95f343c03503`; contém arquivos não rastreados dos pacotes e do desenvolvimento separado. Foram preservados. |
| Comparação com o pacote levado | Sete arquivos selecionados do repositório, quatro Caminhos Markdown e notas v0.4: todos os 12 idênticos byte a byte. Não houve migração paralela nessas fontes. |
| ZIP de retorno | Sem entrada corrompida; cinco arquivos cobertos pelo manifesto tiveram tamanho e SHA-256 confirmados. Os seis arquivos foram copiados integralmente, incluindo o próprio manifesto. |
| Testes de regras | Nenhum teste novo executado. Os 243 da v0.1 e os 22 relatados na análise intermediária não validam a consolidação atual. |

Registro reproduzível dos resultados de integridade: [verificacao-fontes.json](verificacao-fontes.json). A comparação das 12 fontes não equivale a auditar todo o repositório ou todas as combinações de Caminhos.

Leitura integral nesta retomada: os três documentos principais do retorno e seu manifesto. Conferência dirigida: manual 10/11/15/35/60; economia de ação na peça 03; buscas de manobras no manual e nas peças; trechos de Guia, Bastião, Vanguarda e Emanador v0.4. As referências ZIP foram inspecionadas como histórico; os scripts antigos não foram executados e a análise intermediária não foi usada como autoridade para novas decisões.

## 3. Divergências reais com o projeto

Os caminhos `manual/...` abaixo são relativos a `sistema/05-material/livro/` no projeto principal. Linhas conferidas no estado acima. “Substituir no futuro” identifica trabalho de integração, não uma edição já realizada.

| Tema | Projeto atual | Decisão do retorno e consequência |
|---|---|---|
| Atuação básica | `manual/60-invocacoes.md:9–14`: comandar custa Padrão toda rodada; se o dono age por conta própria, a invocação não atua. | Básica própria e intenção persistente. A regra antiga e seu exemplo precisarão ser substituídos; não são uma restrição da v0.2. |
| Distância | `60:364–378`: além de 18 m, o corpo fica parado; Remoto compra exceções de alcance. | Movimento/autonomia não dependem de microcomando. O retorno admite continuidade da tarefa percebida fora de novas ordens, mantendo comunicação pendente. Não importar 18 m, inércia ou preço de Remoto como solução pronta. Separar alcance para instruir, alcance para perceber e sustentação. |
| Inconsciência | `60:406–415`: mantém corpo e Traços, mas ele não age nem defende sozinho. | A entidade funcional conserva básica, Movimento e respostas elegíveis. Persistência material não basta: o comportamento também mudou. Zero PV ainda não significa inconsciência automática, pois `10:296–304` distingue Insistir e Aguentar. |
| Reação | O turno geral dá uma Reação por personagem (`11:22–31`); o sistema antigo distribui respostas por capacidades do Evocador/Coro (`35:545`, `35:595`), sem escrever a reserva coletiva escolhida. | A reserva coletiva é nova regra do subsistema. Não copiar as respostas antigas junto com ela, emprestar a pessoal nem conceder reação por corpo. Gatilhos/ataques ainda exigem ficha. |
| Taxonomia do catálogo | `60:133–138`: Traço sempre ligado versus Comando pago com Padrão; `60:179–185` vende Agarrar, Buscar e Interpor e atribui Investir a todas. | Agora há ações gerais, kit básico, especiais ativas, reativas e passivas. Não converter todo Comando antigo em especial paga, nem todo Traço em passiva gratuita. Entidade utilitária sem ataque continua válida. |
| Dano e custo de acesso | `60:189–208` deriva Investir da rotina do dono e afirma conservação do dano do conjunto. | O dono conserva sua Padrão e cada corpo atua: não há conservação automática. Tabela antiga não pode ser transplantada para básicas novas. Ajudar, posições e tarefas também compõem o benefício do acesso. |
| Múltiplas | `35:555` entrega cinco corpos numa ficha e barra únicas. | A direção autoral exige entidades distintas, com estado próprio; cinco corpos e barra conjunta não são base aprovada. Definir quantidade e investimento continua posterior. |
| Especial | O Comando antigo substitui essencialmente a Padrão do dono; Coro/Dueto vende uma exceção específica (`35:559`, `35:593`). | A especial v0.2 consome a Padrão do dono e a oportunidade básica da destinatária. O custo de oportunidade mudou. A exceção antiga não migra automaticamente e não antecipa o novo Evocador. |

Os capítulos gerais permanecem referência, mas não definem por si uma “básica de invocação”. Sua aplicação exige uma adaptação declarada. Divergência intencional com o sistema antigo não é erro na decisão nova.

## 4. Lacunas confirmadas e interações preservadas

### Lacunas de regra geral

- **Agarrar/Derrubar:** o capítulo 11, linhas 66 e 80–82, autoriza a opção de ataque; o capítulo 15 descreve consequências. Nas fontes e buscas desta retomada não encontrei um procedimento geral completo de aplicação, oposição/CD, requisitos e escape ativo. O catálogo antigo traz um TR Físico para o Comando comprado Agarrar (`60:210–225`), mas isso não resolve automaticamente a manobra geral. A peça 03, §“Agarrar e Derrubar”, também confirma a troca de ataque sem completar essa resolução. Não usar o Controlador v0.1 para cobrar PE por um Derrubado adjacente antes dessa distinção.
- **Empurrar:** há efeitos particulares e regras de carga; não foi localizado procedimento geral completo de manobra. O empurrão da Trilha Punho, por exemplo, é uma habilidade específica, não permissão universal.
- **Esquivar:** `11:70` fala em vantagem nos TR de Destreza; `10:198–205` lista Físico, Vigor, Intelecto e Espírito, com Físico escolhido entre Força e Destreza. Não substituir silenciosamente um termo pelo outro. O efeito de desvantagem nos ataques está escrito e pode ser isolado no ensaio.
- **Estudar:** `11:76` lista Sentir Energia/Ocultismo/Medicina/História, enquanto `11:106` exemplifica Percepção. Vasculhar pode ser testado com Investigação, presente nas duas descrições; isso não corrige Estudar.

Essas lacunas não obrigam a reiniciar o sistema nem impedem um ensaio restrito. Ficam fora dos resultados quantitativos que dependeriam delas, com registro explícito do motivo.

### Interações que precisam entrar no ensaio

- **Ajudar:** `10:46–52` exige contribuição concreta; `11:72` e `11:84–86` oferecem vantagem na próxima tentativa e proíbem empilhar ajudantes no mesmo teste. Vários corpos ainda podem ajudar tentativas diferentes ou fazer tarefas paralelas. Não basta comparar ataques das criaturas entre si.
- **Bloquear/Aparar/Brecha:** `10:153–187` distingue Bloquear gratuito, contra-ataque de Aparar com Reação e nova investida da Brecha com Reação do agressor. Gastar a coletiva não impede novos Bloquear elegíveis. A entidade utilitária não ganha um ataque por ter reserva disponível.
- **Preparar:** `11:94–100` gasta Padrão e depois Reação; se esta for gasta antes, a preparação se perde. A adaptação proposta básica + coletiva deve verificar múltiplas preparações disputando a mesma reserva, sem criar uma Reação por preparação.
- **Condições:** Atordoado retira uma Padrão e proíbe Reação (`15:242–249`); Incapacitado impede Bloquear e torna críticos os acertos corpo a corpo (`15:134–142`). Usar “básica” para escapar de Atordoado seria uma lacuna nova. Aplicar a equivalência para o ensaio é hipótese declarada, não decisão já aprovada. A condição do usuário não é transmitida à entidade.
- **Guia v0.4:** Abrir Caminho custa Bônus + 1 PE, uma vez por turno (linhas 19–27); Resposta Coordenada gasta a Reação do Guia e a do convidado (55–72). Convidar uma entidade elegível usa a coletiva. O golpe concedido é um ataque comum: não é Ação Atacar, etapa de Sequência ou autorização de especial. Avançar custa Reação fora do turno e não custa dentro (29–35); por isso a definição do turno do conjunto afeta a integração.
- **Dois relógios no Guia:** o limite por rodada do Guia vai do início de seu turno ao próximo (`Guia:72`). A renovação proposta da coletiva vai pelo turno do invocador. Quando forem personagens diferentes, uma renovação pode ocorrer no meio do ciclo do Guia. Testar essa ordem: uma reserva de tamanho um não equivale a um único gasto em todo intervalo definido pelo turno de outra pessoa. No nível 30, a segunda resposta dispensa somente a Reação do Guia (`Guia:104–118`). Sem renovação, a coletiva gasta bloqueia outra resposta; com renovação real entre eventos, o caso precisa ser resolvido pelos dois relógios, não por uma proibição inventada.
- **Disputa real de Bônus:** redirecionar concorre com Abrir Caminho e com Olhos Em Mim/Trocação Franca do Bastião (`Bastião:34–38`, `112–116`). Uma Padrão convertida pode pagar outra Bônus, mas isso custa a Padrão que poderia atacar ou comandar a especial. Comandar uma especial também pode retirar o ataque pessoal que habilitaria Trocação. Manter os textos dos Caminhos.
- **Vanguarda e Emanador:** básica não herda Sequência, Ataque Extra, Estocada ou modificações de feitiços do dono. Ajudar pode favorecer um ataque pessoal elegível sem transferir suas habilidades. O Emanador da coleção conserva 6 PE/nível; não incluir atributo adicional. Interações avançadas exigirão fichas completas numa rodada posterior, não alegação de auditoria integral agora.

## 5. Próximo passo necessário: ensaio de custo de oportunidade e interações

**Recomendação:** preparar uma bancada pequena de três ciclos, com zero, uma, duas e três entidades, partindo da v0.2. O caso zero fornece a comparação do mesmo personagem sem acesso ao subsistema. Uma entidade observa o acesso não especializado; duas/três observam crescimento de participação, sem chamar essas composições de Trilhas nem atribuir a elas preços equivalentes.

A primeira pergunta já não é “elas podem agir?”. É **quanto o acesso às atuações acrescenta e o que torna útil abrir mão de duas contribuições para comandar uma especial**. A outra é se os relógios, condições e respostas se resolvem sem gerar recursos extras por interpretação.

### 5.1 Cartões e escolhas de bancada

Preparar três cartões distintos e pequenos:

1. **Combatente:** ataque básico simples e uma especial de ataque único, sem área/controle/duração. Serve para isolar a substituição e seu custo. A especial não será o Derrubado do Controlador antigo.
2. **Sentinela:** ataque básico, Esquivar e uma interceptação reativa de laboratório com gatilho/custo explícitos. A interceptação não é universal; sua redação deverá limitar a transferência daquele acerto para não criar uma cadeia com Olhos Em Mim. Esse limite seria do cartão experimental, sem reescrever Bastião.
3. **Explorador utilitário:** sem ataque, com sentidos e meios físicos declarados para Vasculhar/Usar objeto e Ajudar quando contribuir de verdade. Sem percepção compartilhada ou voo implícito.

Todos continuam com posição, vida e condições separadas. As demais ações gerais elegíveis continuam acessíveis; listar opções no cartão só organiza os casos testados, não fecha o repertório do personagem futuro.

Na primeira execução, fixar ataque, Defesa, dano, PE e anatomia no cabeçalho de cada caso. **Não reaproveitar silenciosamente 1d6, 36 PV, peso 3, capacidade 6, alcance 18 m ou custo 2 PE.** Eles não foram aprovados. Proponho variar o dano/custo da especial contra uma referência fixa de ataque básico e pessoal, em vez de escolher uma única especial e apresentá-la como preço correto. A grade numérica será instrumento de sensibilidade, não ficha legal de um nível ou construção aprovada. Ainda não há valor de aquisição para comparar personagens com igual investimento.

Para o primeiro corte de dano, comparar alvos e posições idênticos, sem condições ou reações, e depois reintroduzir essas interações. Chamar `U` ao resultado esperado da Padrão pessoal, `B_i` ao da básica da destinatária e `S_i` ao da especial. A rotina tem `U + soma(B)`; o comando tem `S_i + soma(B das demais)`. A diferença é `S_i − U − B_i`, antes de PE e demais consequências. Isso é uma conta de oportunidade sob as mesmas premissas, não uma fórmula universal de preço. Se o comando também impede uma Bônus pessoal dependente de Atacar, registrar essa perda separadamente.

Em seguida comparar a básica atacando com Ajudar: o valor desta última é a mudança da tentativa beneficiada, incluindo sua chance de crítico e eventual vantagem já existente. Não somar vantagens e não conceder vantagem a toda uma sequência por ajudar um único ataque. Contra defesa rolada, examinar separadamente a política de Bloquear e as respostas, em vez de reutilizar a conta contra Defesa fixa como se fosse a mesma situação.

### 5.2 Hipóteses propostas para tornar o ensaio executável

Estas são propostas de bancada, não aprovação nem edição da v0.2:

| ID | Hipótese/recorte | O que fica fora ou precisa ser marcado |
|---|---|---|
| H1 | Uma básica e um Movimento por entidade, na iniciativa do invocador. Renovação no início do turno dele; as atuações são concluídas uma a uma, sem interromper sua resolução. | Progressão de execuções e iniciativa própria. O Guia v0.4 oferece precedente de ciclo pessoal, mas não aprova por si este relógio. |
| H2 | Para durações “até o próximo turno” das ações da entidade, usar a mesma janela do conjunto. Tratar a básica como equivalente à Padrão para Atordoado. | Não criar Bônus pessoal ou árvore completa de conversões das criaturas. Testar a parte escrita de Correr usando a básica; adiar Provocar/Ler o Ambiente por conversão. |
| H3 | Começar com entidades já em campo, funcionais, com intenções registradas e comunicação direta inequívoca. Nos casos de inconsciência, usar básicas sem custo de PE e vínculo que continue sustentado durante o recorte. | Aquisição/manifestação não ficam gratuitas; seus custos não são medidos nesse recorte. Não gastar PE do dono inconsciente nem concluir que isso é universalmente proibido. |
| H4 | No teste de redirecionar o conjunto, usar X = 3 apenas como capacidade instrumental para os três corpos presentes. Três entendem uma intenção comum; duas intenções distintas exigem dois comandos pagos. | Não é teto de corpos, fórmula de atributo ou escolha final de X. Ordens iniciais, comunicação remota e distâncias finais ficam abertas. |
| H5 | Comando autoriza uma execução imediata, paga Padrão e ocupa a básica disponível. O alvo da especial no caso principal já é compatível com a intenção registrada. | Evita resolver silenciosamente se a Padrão inclui mudança de intenção. Especial incompatível com a intenção entra como caso pendente, sem cobrar uma Bônus extra por suposição. |
| H6 | Depois de usar a básica, não executar a especial agora. No ensaio principal, não antecipar pagamento nem criar fila. | Comando diferido continua pendente; “não simulado” não significa rejeição autoral da possibilidade. |
| H7 | Renovar a coletiva somente na fronteira H1; escolher respondente elegível no gatilho. Invocação comunica-se e coopera voluntariamente com Guia no caso testado. | Não declarar toda entidade aliada elegível em qualquer circunstância nem renovar recursos ao manifestar/trocar. |

Nenhuma dessas hipóteses exige reabrir básica individual, Movimento independente, continuidade funcional na inconsciência, reserva coletiva ou substituição da básica. Se um teste mostrar um problema numa hipótese, ajustar a hipótese sem desfazer uma decisão explícita por conveniência.

### 5.3 Matriz mínima proposta

| Caso | Comparação/eventos | O que medir ou conferir |
|---|---|---|
| T1 — rotina e utilidade | Mesmo usuário com 0/1/2/3 entidades; atacar, Esquivar, Vasculhar e Ajudar em variantes separadas. | Ações adicionais, ataques/testes e dados, ganho na tentativa ajudada, tarefas concluídas, posição e exposição ao dano. Não declarar igual investimento entre composições. |
| T2 — especial substitutiva | Especial antes da básica; tentativa depois da básica; tentar básica após especial; repetir com outras duas entidades ativas. | Padrão pessoal e básica da destinatária gastas uma vez; demais básicas preservadas; custo perdido da rotina; nenhum resultado para uma fila não definida. |
| T3 — coordenação e Bônus | Manter intenção; trocar uma comum para três; dar duas intenções diferentes; tentar redirecionar depois de agir. Adicionar separadamente Guia/Bastião nas habilidades citadas. | Bônus concorrentes, conversão da Padrão quando disponível, PE próprios das habilidades de Caminho; mudança de objetivo sem renovar recursos. |
| T4 — defesa e reserva | Interceptação seguida de oportunidade; dois resultados de Aparar; Brecha do agressor; duas preparações competindo; variante Guia 7 e microcaso Guia 30. | Gasto da reserva correta; Bloquear continua possível; preparações perdem a possibilidade quando a coletiva é consumida; não inventar ataque para utilitária; rastrear dois relógios no Guia. |
| T5 — perda de capacidade | Usuário inconsciente; usuário Atordoado; entidade Atordoada/Incapacitada/Lenta; usuário a zero ainda consciente por Insistir. | Autonomia das criaturas aptas; impedimentos individuais; impossibilidade de novo comando consciente do apagado; perda de Padrão não elimina a Bônus por suposição. |
| T6 — relógio e duração | Reordenar quem age dentro do conjunto; atravessar a virada da rodada global; invocador agir antes/depois do Guia; condição aplicada e encerrada nos momentos escritos. | Nenhuma básica/coletiva renovada por mera virada da rodada; prazo de Esquivar/Preparar; Avançar dentro/fora da janela; sem chamar o relógio proposto de aprovado. |
| T7 — entrada/troca, como fronteira | Corpo atua, sai e dá lugar a uma reserva; comparar entrar antes e depois da fronteira de renovação. | Identificar onde uma básica/Movimento novo duplicaria participação e quanto aumenta a vida acessível. Sem resolver preços ou conceder uma troca legal enquanto o procedimento estiver pendente. |

T1–T6 compõem o núcleo de funcionamento proposto. T7 deve começar como traço de eventos com custo marcado **não definido**: não contabilizar como zero PE ou zero ações. Comparar explicitamente duas hipóteses para a entrada — aguardar a próxima renovação para básica/Movimento ou herdar apenas o saldo ainda disponível da vaga substituída. A segunda exigiria definir o que é “vaga”, especialmente se uma entidade for trocada por várias; não adotá-la inadvertidamente. Entrada inicial, acesso imediato à reação coletiva ainda livre, perda e simples retorno do mesmo corpo também precisam de regra. Registrar o ponto em que faltam decisões, sem apresentar esses eventos como uma rotação já permitida.

Para uma primeira bancada executável, recomendo adiar básica/Movimento de corpos que entram à próxima renovação como variante mais simples de medir, **somente no ramo experimental de entrada**. Ainda faltam custo de entrada, primeiro comando, efeitos de chegada e elegibilidade reativa; por isso esse ramo não autoriza publicação de um procedimento. Compará-lo com herança de saldo antes de recomendar uma regra definitiva, se essa diferença se mostrar relevante.

### 5.4 Registro por evento e critério de saída

Registrar, com identificação do ciclo e executor: intenção vigente; fonte da ação; saldos Padrão/Bônus/Movimento do usuário; básica e metros por corpo; Reação pessoal/coletiva; alvo e posição; testes e número de dados; PE por fonte; vida/condições; benefício ou tarefa concluída; fonte da regra e hipótese utilizada. Incluir a ação inimiga e uma variante de escolha de alvo, para não atribuir proteção a Esquivar quando o inimigo simplesmente pode atacar outro corpo.

Critérios procedimentais: especial não acumula com básica da destinatária; condição não é burlada por renomear ação; a coletiva não é multiplicada; ninguém recebe sentidos/habilidades/energia sem fonte; nenhuma lacuna é registrada como zero custo ou permissão. Casos que dependem de regra ausente devem terminar como **indeterminados**, não aprovados ou falhados pelo valor escolhido pelo script.

Critério de utilidade: apresentar o ganho de ações e a comparação básica/ajuda/especial, inclusive posições, reações e custos de oportunidade. Uma especial pode se justificar por alcance, tipo de efeito, timing ou utilidade; não exigir que toda especial supere uma soma de dano. Para efeitos comparáveis de dano, a conta isolada ajuda a localizar opções sistematicamente desvantajosas, sem certificar o preço.

Somente depois desse ensaio podemos recomendar faixas iniciais para o investimento no vínculo/entidade e quais capacidades exigem especial, reagente ou passiva. Limite de corpos, construtor completo e fatias não saem automaticamente desses resultados. Medir tempo real e diversão continua exigindo sessão com pessoas.

## 6. Pendências ordenadas sem repetir escolhas resolvidas

1. **Para executar T1–T6:** declarar a ficha instrumental, H1–H7 e os gatilhos reativos; esses detalhes são hipóteses de ensaio revisáveis, não perguntas autorais já respondidas.
2. **Para fechar o procedimento de jogo:** relógio final; alcance/meios/X e primeira intenção; especial que muda objetivo; comando diferido; entrada/troca e recursos da reserva. O ensaio pode mostrar quais escolhas têm consequência material antes de pedir decisão.
3. **Para precificar e construir:** valor de acesso, kit, distinção básica/especial, sustentação/PE e presença física. Não transportar o orçamento antigo ou o dano da v0.1.
4. **Para integração ampliada posterior:** manobras gerais incompletas, condição/efeito de Esquivar sobre TR, Estudar, fontes de energia, perda e módulos de vínculo; fichas completas dos quatro Caminhos preservados.
5. **Depois da base:** Evocador, e depois suas Trilhas. Sem benefícios antecipados.

Não surgiu nesta conferência motivo para voltar às perguntas sobre compartilhar básicas, exigir microcomando de Movimento, desligar autonomia pelo desmaio do dono ou somar especial à básica. O próximo avanço é medir consequências da estrutura escolhida.

## 7. Escopo efetivamente concluído nesta entrega

Retorno principal lido integralmente; integridade e estado local conferidos; divergências e dependências identificadas; plano de ensaio registrado em pasta separada. Não foram implementadas regras, executados testes de jogo, modificados manual/Caminhos nem realizados commit/push. As propostas de H1–H7, cartões e variante de entrada neste documento não se tornam decisões de Mizuki por terem sido registradas.

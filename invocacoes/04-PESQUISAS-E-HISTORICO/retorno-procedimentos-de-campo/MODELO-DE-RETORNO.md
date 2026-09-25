# Retorno — procedimentos de campo das invocações

**Preenchido a partir da discussão de design por etapas · 24/09/2026**

> Este documento registra decisões e trabalho efetivamente realizados. **Não é aprovação do subsistema inteiro.** A versão de saída é um **rascunho operacional candidato à v0.3**, com status explícito por item. Não deve ser chamada de v0.3 consolidada enquanto as pendências marcadas e as recomendações operacionais ainda não aprovadas não forem resolvidas na integração.

## 1. Identificação

**Recorte.** Procedimento das invocações em campo: comando especial e intenção persistente; comando especial diferido; relógio e renovação; entrada, retorno e substituição; estado e Reação coletiva. Não foram desenvolvidos construtor, catálogo, progressão, orçamento, preço de aquisição, captura, recuperação definitiva, Evocador ou Trilhas.

**Versão de partida.** Decisões autorais da v0.2, preservadas salvo alteração explícita nesta conversa.

**Fontes efetivamente lidas nesta consolidação:**

- `LEIA-ME.md` — integral;
- `01-ESTADO-E-PAUTA.md` — integral;
- `base-v0.2/01-RETORNO.md` — integral;
- `base-v0.2/02-PROPOSTA-REVISADA-INTEGRAL.md` — integral;
- `ensaio/RELATORIO.md` — integral;
- `ensaio/FICHA-DO-ENSAIO.md` — integral.

**Referências consultadas conforme dependência:** capítulos 10, 11 e 15 de `regras-gerais/`; Guia e Bastião v0.4 nas interações pertinentes; Vanguarda/Estocada e Emanador v0.4 preservados como restrições de integração. O código e o JSON completos do ensaio não foram executados nem percorridos nesta conversa.

**Status de saída.** Blocos A, B e C receberam decisões suficientes para uma folha operacional. Alguns detalhes de custo, comunicação e procedimento permanecem explicitamente pendentes. Nenhum arquivo-fonte, Caminho, manual ou repositório foi editado; não houve commit ou push.

## 2. Aprovações explícitas de Mizuki

| Decisão | Confirmação na conversa | Alcance | Pendências preservadas |
|---|---|---|---|
| Especial pode intervir fora da intenção vigente sem Bônus adicional | Preferiu “só a padrão para intervir em B” | A Padrão comanda a especial; a destinatária pode atingir objetivo diferente da tarefa persistente | Requisitos normais da capacidade e comunicação continuam aplicáveis |
| Orientação posterior é escolhida depois do resultado da especial | Exemplo: “Nue ataque raio em alvo X” → resolve → “Nue foque em Y” | Depois da resolução, o usuário pode conservar a intenção anterior ou atribuir uma nova à destinatária, sem Bônus extra | Alcance/meio de comunicação ainda aberto |
| O alvo da nova intenção pode ser diferente do alvo da especial | Mesmo exemplo: raio em X e foco posterior em Y | A Padrão autoriza a intervenção e a orientação posterior; não cria outra básica | Nenhuma ação extra concedida |
| Comando especial diferido é opção tática aprovada | Considerou bom “gastar uma [Padrão] na primeira” e deixar a seguinte livre | A Padrão é paga antes; a especial usa uma básica futura disponível, sem nova Padrão de comando | PE, expiração, cancelamento, troca de alvo e alguns requisitos ainda precisam de redação operacional final |
| Relógio do conjunto aprovado | “pode aprovar esse relógio” | Iniciativa conjunta; ciclo do início de um turno do invocador ao próximo; renovação nessa fronteira; rodada global não renova | Quantidade final de básicas por ciclo continua fora deste recorte numérico |
| Janelas individuais só para início/fim de turno | Aprovadas junto do relógio recomendado | Resolvem condições e efeitos escritos de cada corpo sem criar iniciativa própria | Redação fina na integração |
| Guia 30 não será modificado para esconder a renovação da coletiva | Aprovado junto do relógio | Duas respostas distintas podem ocorrer no ciclo do Guia se a coletiva realmente renovar entre os gatilhos; sem renovação, não | Preservar v0.4 |
| Substituição pode transferir uma básica ainda não gasta | Preferiu que a nova entidade “assuma o que sobrou” | Uma oportunidade básica não gasta pode passar da entidade substituída para uma substituta elegível | Não multiplicar nem fundir oportunidades |
| Em 1→vários, só uma nova entidade recebe o saldo transferido | “uma delas a sua escolha segue com os recursos, as outras não” | Jogador escolhe uma substituta direta | As demais entram sem básica criada pela troca |
| Movimento não é herdado | “movimento sendo algo de cada individualmente” | Cada corpo usa seu próprio Movimento | Metros finais permanecem módulo futuro |
| Entidade nova entra com seu Movimento próprio disponível | “Movimento proprio já disponivel” | Mesmo sem herdar Movimento da substituída, corpo novo pode deslocar-se com seu próprio recurso no ciclo | Mesma criatura não reseta Movimento por sair e voltar |
| Trava anti-rotação de básica | “Concordo plenamente com a trava” | Corpo que já gastou sua básica no ciclo não recebe outra por sair e voltar como substituto | Renovação só pela fronteira normal ou fonte futura explicitamente escrita |
| Primeira intenção sem Bônus apenas em substituição | “Concordo, mas apenas no caso aonde ela esteja substituindo uma em campo” | A entidade substituta recebe a tarefa inicial como parte da troca | Entrada que apenas adiciona corpo não recebe essa gratuidade |

### Decisões v0.2 preservadas

Continuam valendo, entre outras: subsistema geral antes de Evocador; personalização completa inclusive entidades sem ataque; acesso ao vínculo ≠ especialização; atuação básica e Movimento próprios; personagem conserva seus recursos; repertório não implica múltiplas execuções; intenção persiste sem renovação; Bônus muda a tarefa; mesma nova intenção pode alcançar várias entidades dentro de X pendente; Padrão comanda especial substitutiva; básica já usada impede especial naquele ciclo; uma Reação coletiva separada da pessoal; autonomia básica durante inconsciência quando a sustentação permitir; autonomia integra o investimento; preservar Bastião, Vanguarda, Emanador, Guia v0.4, Estocada e Emanador sem acréscimo de atributo aos PE; não conceder básica + especial por Evocador nesta etapa.

## 3. Alterações em relação à v0.2

| Regra/hipótese anterior | Resultado desta discussão | Motivo | Status |
|---|---|---|---|
| Relação especial × intenção estava aberta | Especial pode sair da intenção vigente e, depois do resultado, o usuário decide conservar ou substituir a intenção da destinatária | Maior dinamismo e adaptação ao resultado | **Aprovado** |
| Padrão + Bônus poderia ser exigido para mudar foco durante especial | Bônus não é exigida para a intervenção nem para a orientação posterior da mesma destinatária | Evitar dupla cobrança para uma única ordem especial | **Aprovado** |
| Comando diferido era apenas possibilidade | Existe opção de pagar Padrão agora para a especial ocorrer na próxima oportunidade válida, ocupando básica futura | Deslocamento temporal do custo como escolha tática | **Aprovado em direção; detalhes pendentes** |
| Iniciativa conjunta/ciclo do invocador era hipótese da bancada | Torna-se relógio operacional aprovado | Uma fronteira clara e pouca carga de iniciativa | **Aprovado** |
| Renovação na fronteira do invocador era hipótese | Básica disponível, Movimento próprio e coletiva renovam nessa fronteira; rodada global não renova | Evitar dupla renovação | **Aprovado quanto ao relógio** |
| Guia 30 tinha consequência observada, não escolhida | Consequência é aceita sem alterar Guia | Preservar Caminho v0.4 e relógios reais | **Aprovado** |
| Entrada/troca estava aberta entre esperar e herdar saldo | Substituição pode transferir uma básica não gasta; corpo adicional não cria básica | Fazer a troca ser estratégica sem rotação gratuita | **Aprovado** |
| Movimento poderia ser tratado junto do saldo | Movimento é sempre individual; corpo novo entra com o próprio disponível | Movimento já é propriedade da entidade | **Aprovado** |
| Primeira intenção na entrada era pendente | Substituta recebe primeira intenção dentro da troca; entrada adicional não recebe essa gratuidade | Tornar transição utilitária→combate menos penosa sem liberar ordens gerais | **Aprovado parcialmente** |

## 4. Proposta operacional integral

Entregue separadamente em `PROPOSTA-OPERACIONAL-INTEGRAL.md`. O arquivo reúne as decisões anteriores preservadas, as novas decisões desta conversa, as recomendações ainda não aprovadas e as pendências, sem depender de fragmentos do histórico.

## 5. Exemplos discutidos

### E1 — Especial fora da intenção e orientação posterior

**Antes:** Combatente/Nue tem intenção de enfrentar A e ainda possui uma básica disponível. B/X ameaça um aliado e é alvo válido da especial.

**Procedimento:** o usuário paga Padrão e comanda a especial contra B/X. A destinatária executa a especial no lugar de uma básica disponível e paga os custos próprios da capacidade. Depois de ver o resultado, o usuário pode dizer, por exemplo, “Nue, foque em Y”, atribuindo uma nova intenção sem Bônus adicional; também poderia conservar a intenção anterior.

**Consequência:** não existe básica adicional depois da especial. As demais invocações mantêm suas atuações e intenções.

### E2 — Comando especial diferido

**Antes:** a destinatária já gastou a básica do ciclo. O usuário ainda possui Padrão.

**Procedimento aprovado em direção:** o usuário pode gastar a Padrão agora para deixar uma especial ordenada para a próxima oportunidade válida da destinatária. Quando essa oportunidade chegar, a especial ocupa uma básica futura disponível e não cobra outra Padrão de comando.

**Consequência:** a Padrão do ciclo da execução pode ficar livre para o usuário. Isso é benefício tático intencional por deslocamento temporal do custo, não execução gratuita.

**Ainda pendente:** momento de PE, expiração, cancelamento, alteração de alvo, falha de requisitos e interação fina com inconsciência/troca.

### E3 — Fronteira de renovação e Guia 30

O conjunto renova na abertura do turno do invocador, não na virada da rodada global. Se uma invocação gastar a coletiva numa primeira Resposta Coordenada e o turno do invocador começar antes do segundo gatilho legítimo da cadeia do Guia 30, a coletiva renova e outra invocação pode pagar a segunda resposta. Se não houver renovação entre os gatilhos, a segunda resposta não pode ser paga pela coletiva já gasta. A habilidade do Guia não é alterada.

### E4 — Substituição com saldo

**Antes:** Combatente ainda não gastou a básica. É substituído por Nue.

**Depois:** Nue pode receber aquela básica ainda disponível, recebe sua primeira intenção dentro da substituição e usa seu próprio Movimento. Se o Combatente já tivesse gasto a básica, não haveria saldo para transferir. Se Nue já tivesse gasto uma básica naquele ciclo e retornasse, não poderia receber outra.

### E5 — 1→vários

Combatente sai; entram Nue e outros corpos. O jogador escolhe uma entidade como substituta direta. Somente ela pode receber uma básica não gasta e a primeira intenção incluída na substituição. As demais entram com Movimento próprio, mas sem básica criada pelo evento e sem primeira intenção gratuita por esta regra.

## 6. Pendências e escolhas adiadas

### Resolvidas nesta conversa

- especial fora da intenção vigente;
- escolha da intenção posterior depois de ver o resultado;
- possibilidade tática de comando especial diferido;
- relógio de iniciativa e renovação;
- consequência de Guia 30;
- transferência limitada de básica por substituição;
- 1→vários sem multiplicação;
- Movimento individual na entrada;
- trava anti-rotação;
- primeira intenção gratuita apenas para substituta direta.

### Pendentes por escolha ou módulo futuro

- quantidade final de execuções básicas por ciclo/progressão;
- X de destinatárias por redirecionamento;
- meios e alcance de comunicação;
- custo de manifestação, recolhimento e troca;
- fonte e preço dos PE das especiais;
- detalhes finais do comando diferido: PE, expiração, cancelamento, mudança de alvo, falha de requisitos, troca e inconsciência;
- procedimento/custo da primeira intenção para entidade que entra **sem substituir**;
- persistência de efeitos cuja própria natureza dependa de presença/existência física;
- morte do usuário, perda do vínculo, acesso a PE durante inconsciência;
- valores de PV, dados, alcance, deslocamento, interceptação e demais números da ficha;
- Agarrar/Derrubar/Empurrar e o “TR de Destreza” de Esquivar continuam lacunas de referência quando indispensáveis;
- catálogo, níveis, orçamento, dano final, aquisição, captura, recuperação definitiva, Evocador e Trilhas.

## 7. Verificações realmente realizadas

**Leitura.** Foram lidos integralmente os seis arquivos iniciais listados na seção 1. Foram consultadas as regras gerais e os Caminhos v0.4 apenas nas interações pertinentes.

**Análise lógica.** Foram comparados custos de oportunidade de especial, persistência de intenção, fila/diferimento, renovação, Guia 30, entrada, retorno e substituição.

**Testes nesta conversa.** Nenhum novo código foi executado; nenhuma nova bancada foi rodada; não houve playtest com pessoas. Os **168 checks** pertencem ao ensaio anexado e validaram o modelo executado sob suas hipóteses, não o equilíbrio, a diversão ou esta nova redação.

**Preservação de fontes.** Nenhum arquivo de origem foi alterado. Não houve commit ou push.

## 8. Solicitação para integração

**É hora de voltar à tarefa de integração.** Os três blocos operacionais delimitados foram discutidos até o ponto necessário. A integração deve:

1. reconciliar esta folha com os arquivos reais do projeto, preservando a coleção de Caminhos v0.4;
2. transformar recomendações ainda não aprovadas em campos de decisão ou regras após validação, sem silenciosamente promovê-las a decisão autoral;
3. atualizar a bancada de integração somente depois de fixar o procedimento mínimo do comando diferido e da entrada adicional;
4. testar especialmente concentração de ações com comando diferido, trocas antes/depois da fronteira, 1→vários, Ajudar, Reação coletiva e Guia 30;
5. manter construtor, Evocador e Trilhas fora até essa integração terminar.

**Arquivos desta entrega:** `MODELO-DE-RETORNO.md` e `PROPOSTA-OPERACIONAL-INTEGRAL.md`.

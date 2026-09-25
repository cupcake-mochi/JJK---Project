# RASCUNHO — resultados do ensaio de autonomia v0.2

**24/09/2026. Ensaio autorizado por Mizuki; hipóteses numéricas e operacionais continuam experimentais.**

A bancada foi executada. A autonomia escolhida produz participação adicional efetiva, e o custo da especial precisa ser comparado com a melhor utilização das básicas — incluindo Ajudar. Uma segunda entidade também pode ajudar a especial, mudando novamente essa comparação. A Reação coletiva funciona como uma reserva compartilhada, mas seu relógio pode cruzar o do Guia.

Não apareceu nesta bateria motivo para reabrir as decisões autorais sobre básica individual, Movimento independente, continuidade funcional durante inconsciência, reserva coletiva ou especial substitutiva. Isso não significa que o subsistema esteja equilibrado ou pronto para publicação.

## 1. O que foi executado

- **168 checagens, 168 aprovadas, 0 falhas na execução final.** São verificações do código e das premissas declaradas, não 168 partidas ou provas independentes de equilíbrio.
- **58 cenários/sondas**, com 342 eventos registrados; 55 tentativas recusadas como esperado e 8 registros de questões não resolvidas/modeladas.
- **27 combinações** de Defesa, política de Bloquear e vantagem/desvantagem; **18 comparações** de Ajudar; **63 combinações** de dados e custo de especial; **12 comparações** de composição ofensiva com 1/2/3 entidades; horizonte de PE em três ciclos.
- Traços completos de três ciclos para o mesmo usuário com 0/1/2/3 entidades, mais microcasos de gastos, gatilhos, condições e relógios. Os dados desses traços são escolhidos, não sorteados.
- Os quatro Caminhos v0.4 e as demais 12 referências do registro anterior continuam com os mesmos hashes. Não houve edição no projeto principal.

Leia a [ficha da bancada](FICHA-DO-ENSAIO.md) antes de transportar qualquer número. Ela declara cartões, posições, hipóteses, fontes de PE e limites da simulação. A versão autoral continua sendo a v0.2 recebida; o ensaio não gerou uma v0.3 aprovada.

## 2. Básica e Ajudar: ataque fraco não significa benefício pequeno

Na referência isolada, ataque +5 contra Defesa fixa 16, sem condições, reações ou vantagem anterior:

| Uso das ações | Dano primário esperado |
|---|---:|
| Usuário sozinho, 3d6 + 2 | 6,775 |
| Básica da criatura, 1d6 + 1 | 2,425 |
| Usuário e criatura atacam | 9,200 |
| Criatura ajuda; usuário ataca com vantagem | 10,399 |

Ajudar acrescentou **3,624** à tentativa pessoal; atacar com a criatura acrescentaria **2,425**. O benefício de Ajudar é da tentativa efetivamente favorecida, sem se espalhar para todos os ataques da Ação Atacar ou de uma Sequência.

Com um ataque beneficiado de 6d6 + 2, nas mesmas condições, o ganho da ajuda sobe a **6,748**. Essa é uma sonda de sensibilidade a um ataque mais valioso, não uma ficha de Caminho construída. Com vantagem já existente, o ganho adicional da ajuda é zero. Contribuição física, comunicação e momento da tentativa continuam necessários.

**Consequência de design:** não precificar autonomia apenas pelo dano impresso no ataque da criatura. Uma entidade utilitária ou fraca em combate ainda pode comprar, por sua básica, vantagem para outra tentativa importante. Vários ajudantes não empilham no mesmo teste, mas podem distribuir ajuda a tentativas diferentes.

## 3. Especial: comparação com a rotina e com o grupo

O comando abre mão da Padrão pessoal e da básica da destinatária. Se a especial só causar dano na mesma posição/alvo, a primeira comparação é com as duas contribuições perdidas. Quando Ajudar for melhor que atacar, ela também precisa entrar na referência.

| Com uma entidade | Dano esperado, Defesa fixa 16 |
|---|---:|
| Usuário + básica atacando | 9,200 |
| Usuário ajudado pela criatura | 10,399 |
| Especial 4d6 + 1 | 8,200 |
| Especial 5d6 + 1 | 10,125 |
| Especial 6d6 + 1 | 12,050 |

A especial de 5d6 + 1 supera os dois ataques separados, mas ainda fica abaixo de usar a criatura para Ajudar, antes de cobrar seus PE. Não concluímos que toda especial precise causar 6d6: esses valores só descrevem este ataque, alvo e composição.

### Uma segunda entidade pode ajudar a especial

Enumeramos as escolhas ofensivas disponíveis nos cartões: Combatente/Sentinela atacam ou ajudam; Explorador ajuda ou busca, sem ataque; o usuário ataca ou comanda a especial do Combatente. Cada ajudante ocupa sua própria básica, e o mesmo ataque só recebe uma vantagem. Todas as contribuições e alcances são premissas satisfeitas nessa comparação.

| Entidades | Melhor rotina sem especial entre as opções examinadas | Especial 4d6 + 1 | Especial 5d6 + 1 | Especial 6d6 + 1 |
|---:|---:|---:|---:|---:|
| 1 | 10,399 | 8,200 | 10,125 | 12,050 |
| 2 | 12,824 | 12,615 | 15,581 | 18,547 |
| 3 | 15,249 | 15,040 | 18,006 | 20,973 |

Com duas entidades, a Sentinela pode ceder sua básica para ajudar o ataque especial do Combatente. A especial de 5d6 + 1 chega a **15,581**, contra **12,824** da melhor rotina ofensiva sem especial encontrada nesse conjunto de opções. Com três, o Explorador pode ajudar a especial e a Sentinela volta a atacar. Isso não inclui o valor de Esquivar, investigar, proteger ou conservar PE na função de comparação; maximizar dano primário não é maximizar utilidade total.

O traço `T2-especial-ajudada` confirma a sequência: básica da Sentinela em Ajudar → Padrão do usuário para comandar → básica do Combatente ocupada pela especial, rolando dois d20. Não há execução gratuita: são três contribuições gastas.

**Consequência de design:** não construir um preço de especial que olhe só para uma criatura isolada. O kit precisa ser confrontado com as combinações de básicas do conjunto e com aliados externos. Isso preserva a decisão de substituição; não exige conceder básica + especial ao Evocador.

### PE muda a disponibilidade, não o resultado de um ataque já pago

Na sonda de três ciclos com **4 PE disponíveis**, especial de **6d6 + 1** e retorno à rotina de Ajudar quando falta energia:

| PE por especial | Especiais possíveis | PE restantes | Dano esperado nos três ciclos |
|---:|---:|---:|---:|
| 1 | 3 | 1 | 36,150 |
| 2 | 2 | 0 | 34,499 |
| 3 | 1 | 1 | 32,847 |

Ajudar nos três ciclos, sem especial, renderia **31,196** nesse recorte. Os traços também verificaram que um comando recusado por falta de PE não consome Padrão ou básica; o conjunto consegue então realizar outra opção permitida. Esses custos de 1/2/3 PE são hipóteses de sensibilidade, não preços recomendados. A disponibilidade de energia ao longo de uma missão e o custo de adquirir/manter a entidade ainda não foram modelados.

## 4. Bloquear muda a comparação

Média de Defesa igual não implica mesma distribuição de acertos. No alvo Defesa 16:

| Política do alvo | Usuário + básica atacam | Usuário ajudado | Especial 5d6 + 1 |
|---|---:|---:|---:|
| Defesa fixa | 9,200 | 10,399 | 10,125 |
| Bloquear em todo ataque | 9,209 | 9,883 | 10,134 |
| Bloquear só se acertaria a fixa — hipótese separada | 7,798 | 9,110 | 8,599 |

Contra quem Bloqueia sempre, a especial de 5d6 + 1 passa ligeiramente a opção ajudada em dano primário. Portanto, nem o ordenamento observado contra Defesa fixa é universal. A política de Bloquear só após um acerto conhecido foi explicitamente separada; não foi adotada como interpretação obrigatória de timing.

Essas médias não incluem o valor dos contra-ataques de Aparar/Brecha. Nos traços, dois Aparar podem negar dois ataques, mas só um contra-ataque das entidades foi possível antes da renovação da coletiva. Brecha consumiu a Reação do agressor, não a coletiva. Um 20 natural continuou acertando contra duplo 10. A coletiva gasta não impediu outros Bloquear elegíveis.

## 5. Três ciclos: participação e escolha de alvo

O usuário sempre realiza a mesma sequência pessoal. Combatente ataca; Sentinela Esquiva; Explorador vasculha objetos distintos. Os resultados abaixo são **exemplos com dados fixados**, não estimativas de desempenho médio.

| Entidades | Dano pessoal + criaturas | Buscas bem-sucedidas | d20 se inimigo ataca usuário | d20 se inimigo escolhe Sentinela | PV finais do usuário nessas políticas |
|---:|---:|---:|---:|---:|---|
| 0 | 34 | 0 | 6 | 6 | 13 / 13 |
| 1 | 42 | 0 | 9 | 9 | 13 / 13 |
| 2 | 42 | 0 | 9 | 12 | 13 / 40 |
| 3 | 42 | 2 | 12 | 15 | 13 / 40 |

Nos casos sem Sentinela, a segunda política também ataca o usuário. Quando ela existe, os dados adicionais vêm da desvantagem de Esquivar. A tabela de dados completa, incluindo dano e Bloquear nas outras sondas, está no JSON.

O Explorador realizou buscas enquanto o usuário e o Combatente lutavam. A Sentinela acrescentou uma escolha defensiva, mas Esquivar sozinho **não protegeu o usuário quando o inimigo o escolheu como alvo**: ele terminou com os mesmos 13 PV. Ao atacar a Sentinela, o inimigo errou os três ataques dos dados escolhidos e o usuário manteve 40 PV. Não há provocação implícita em Esquivar ou na intenção de proteger. A interceptação foi verificada separadamente.

As entidades somaram posições e PV distintos. A sonda de cobertura aplicou apenas a maior cobertura pertinente e não a tratou como bloqueio automático de passagem. Não foram precificados corredores, tamanho corporal, sentidos ou toda a geometria do combate. A contagem de dados não mede tempo real de mesa.

## 6. Integrações procedimentais

| Interação | Resultado nos casos executados |
|---|---|
| Básica antes da especial | Comando recusado; Padrão e PE preservados na tentativa não executada. |
| Especial antes da básica | Ocupa a básica da destinatária; outras entidades continuam podendo usar as próprias. |
| Redirecionar após agir | Intenção muda, sem renovar básica, metros ou coletiva. |
| Duas intenções diferentes | Bônus e uma Padrão convertida em Bônus; essa Padrão não fica disponível para especial. |
| Bastião | Olhos Em Mim/Trocação disputam a Bônus. Comandar sem Atacar pessoal não fornece o acerto que habilita Trocação. |
| Usuário inconsciente | Combatente atacou e Sentinela se moveu/interceptou, com sustentação assumida e sem novos comandos do usuário. PE do inconsciente não foi liberado. |
| Usuário Atordoado | Sem Padrão ou uso da Reação; Bônus ainda pôde redirecionar e as entidades aptas atuaram. |
| Entidade Atordoada | Sem básica/especial ou uso da coletiva; outra entidade apta continuou elegível. Encerrar a condição não criou uma básica tardia. |
| Incapacitado | Não removeu a básica; bloqueou Bloquear e tornou crítico um acerto corpo a corpo. |
| Lento, Agarrado e Impedido | Respeitados os metros reduzidos/zerados; Avançar não contornou Impedido. |
| Preparar | Consumiu a básica. Usar a coletiva para uma resposta retirou a possibilidade das preparações restantes. |
| Rodada global | Não renovou básica ou coletiva; o começo do próximo turno do invocador renovou e expirou os efeitos da janela. |
| Sentinela/Bastião | A interceptação experimental encerrou a transferência daquele acerto, sem re-Bloquear ou aplicar Esquivar retroativamente. |

São resultados do procedimento modelado, não auditoria de cada habilidade dos Caminhos. Os traços de Insistir e de condições não simulam todas as suas consequências numa missão completa.

### Guia 7: atuação básica e resposta são recursos diferentes

Uma criatura que já usou a básica pôde aceitar o ataque comum de Resposta Coordenada, pagando a coletiva; o Guia pagou a própria Reação. Isso não renovou sua básica nem autorizou especial depois dela. Quando o próprio invocador era Guia, a sequência gastou Bônus + 1 PE + Reação pessoal + coletiva, mantendo a Padrão pessoal disponível. É um benefício real a considerar no futuro preço do acesso às invocações.

Também se executou especial seguida de resposta comum do Guia: gastaram-se Padrão, básica da destinatária, Bônus, duas Reações e os PE pertinentes. O ataque reativo concedido não é o acúmulo de básica + especial que ficou reservado ao futuro Evocador.

Avançar fora do turno consumiu a coletiva, impedindo outra entidade do conjunto de aceitar uma resposta que exigisse essa mesma reserva. Na janela do conjunto, o trecho de Avançar preservou a coletiva e os metros próprios, conforme a hipótese de turno adotada.

### Guia 30: duas janelas, duas situações distintas

O traço `T6-guia30-com-renovacao` realizou:

1. Guia começa seu ciclo e prepara Resguardar para o Combatente.
2. Antes do turno do invocador, o Combatente usa Resguardar num TR e recebe a primeira Resposta Coordenada: gasta a coletiva; o Guia gasta sua Reação.
3. A cadeia passa Executar para a Sentinela.
4. Começa o turno do invocador: a coletiva renova.
5. A Sentinela usa Executar na básica e aceita a segunda resposta. Ela paga a coletiva renovada; a habilidade de nível 30 dispensa somente a Reação do Guia.

São duas respondentes distintas e dois gastos separados por uma renovação real. Uma terceira resposta foi recusada pelo limite do Guia. No traço sem renovação entre os gatilhos, a segunda entidade não conseguiu pagar a coletiva. **Não é correto resumir essa integração como “no máximo uma resposta das invocações por ciclo do Guia”** enquanto a coletiva renovar pelo invocador. Não se alterou a habilidade do Guia para produzir esses resultados.

## 7. Entrada e troca: comparação ainda parcial

Depois de uma entidade gastar básica e Movimento, ambas as hipóteses examinadas — aguardar a próxima renovação ou herdar saldo — impediram que uma substituta recebesse imediatamente esses recursos. Quando a anterior ainda não agiu, herdar saldo permitiu a atuação, enquanto aguardar a próxima renovação a adiou.

Isso expõe o efeito prático da escolha, mas não define uma troca legal: ação, PE, primeira intenção e elegibilidade reativa continuam sem procedimento fechado. A comparação de herança vale apenas para uma troca de um corpo por outro; não decidiu vagas ou divisão de corpos. A passagem pela fronteira seguinte foi examinada, mas entrada inicial, reentrada do mesmo corpo e uma sequência completa de chegada imediatamente antes/depois da fronteira exigem seus procedimentos reais.

Na sonda, um corpo ferido com 10 PV e a reserva saudável com 18 oferecem **28 PV remanescentes no repertório**, embora só um entre em campo e não haja cura. O acesso a essa reserva é poder adicional, dependente de custos/condições de troca. Não usar um teto de corpos simultâneos como se ele também limitasse automaticamente a vida acessível na cena.

## 8. O que ficou indeterminado ou fora do modelo

Os oito registros indeterminados correspondem a: especial que muda intenção; eventual comando diferido; uso dos PE do inconsciente; quatro variantes de troca sem procedimento completo; e uma sonda de vantagem/desvantagem simultâneas deliberadamente não modelada. O último item é limite da implementação, não declaração de uma lacuna do manual.

Permanecem fora: resolução geral incompleta de Agarrar/Derrubar/Empurrar; interpretação do TR de Esquivar e da perícia de Estudar; preço de aquisição/sustentação; comunicação remota e X definitivo; primeiras ordens; duração de Ajudar além da tentativa do recorte; construções completas de personagens; especiais com controle/área/manutenção; repertório de reserva completo; tamanho e passagem; missões, tempo de mesa e diversão. Ausência de cálculo não foi tratada como custo zero.

## 9. Recomendações que os resultados sustentam

1. **Manter a v0.2 como direção.** As decisões autorais não precisam ser reabertas para explicar os casos examinados. Conservar H1–H7 como hipóteses até a redação operacional ser escolhida.
2. **Separar preço do vínculo, valor da básica e preço da especial.** Acesso a uma criatura já traz uma nova fonte de ações gerais e ajuda; seu ataque isolado não mede esse pacote. A básica também pode aumentar o valor de uma especial de outra entidade.
3. **Não fixar dano mínimo universal para especiais.** Comparar alternativas sob o mesmo alvo, posição, PE e composição. Uma especial de controle/utilidade pode se justificar por efeito/timing, sem competir numa soma de dano.
4. **Escrever os relógios explicitamente.** O ciclo do invocador é uma hipótese operacional consistente nos casos testados; precisa vir acompanhado da consequência observada com o Guia. Não adicionar um segundo limite reativo por silêncio.
5. **Manter entrada/troca como módulo pendente.** Aguardar a próxima renovação é a variante mais simples desta comparação; herdar saldo pode ser mais flexível, mas exige definir a unidade que transmite os recursos. Nenhuma virou regra aprovada.

**Próximo avanço recomendado:** fechar uma folha operacional curta do subsistema com o relógio e os casos de comando/entrada explicitamente resolvidos ou marcados, e então montar um primeiro vínculo com uma criatura de kit reduzido para comparar investimento em fichas completas. Ajudar e as interações com o Guia devem fazer parte dessa avaliação desde o início. O Evocador e suas Trilhas continuam depois da base, sem promessa de exceções.

## 10. Reprodução, evidência e qualidade dos registros

Execute, a partir de qualquer pasta:

```bash
python3 '/home/mizuki/CHAT-GPT/RPG -JJK/desenvolvimento-invocacoes-2026-09-24/integracao-autonomia-v0.2/ensaio-01/bancada.py'
```

O programa usa somente a biblioteca padrão do Python e regrava `resultados.json` e `execucao.txt` ao lado dele. Não executa os validadores antigos e não modifica o projeto principal. O JSON registra os valores exatos como frações, as versões decimais, os resultados esperados/obtidos das checagens, estados antes/depois e hashes das fontes.

Durante a revisão dos registros, uma checagem de integridade detectou compartilhamento indevido de estado mutável nos snapshots de tentativas recusadas. O armazenamento foi corrigido para preservar cópias independentes, e a execução final passou. Foi um defeito da instrumentação, não uma nova regra nem achado de equilíbrio. A versão final também audita que tentativas recusadas/indeterminadas não pagaram recursos e que reservas e básicas não ultrapassaram os limites do modelo.

Arquivos: [ficha e hipóteses](FICHA-DO-ENSAIO.md), [bancada reproduzível](bancada.py), [resultados completos](resultados.json) e [resumo da execução](execucao.txt). O JSON informa o SHA-256 do script executado. Não houve playtest com pessoas, revisão independente por outro agente ou certificação de equilíbrio.

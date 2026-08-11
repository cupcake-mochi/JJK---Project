# Como organizar o teste da primeira versão do sistema de combate

Seu cenário tem uma dificuldade que não é sobre a mecânica de combate em si, mas sobre **como testar qualquer coisa em uma estrutura descentralizada**: 5-7 mestres, sem uma mesa "canônica" única, com personagens que atravessam mesas diferentes carregando estado (HP, recursos, itens, condições). Isso significa que um teste malfeito não fica contido — ele vaza para todas as mesas seguintes que aquele personagem visitar. Então a organização do teste precisa resolver dois problemas ao mesmo tempo: **gerar dados comparáveis apesar de ter várias pessoas rodando a mesma regra de formas diferentes**, e **não deixar a instabilidade de uma v0.1 contaminar a continuidade persistente**.

Abaixo vai uma estrutura para isso, do objetivo até o encerramento do ciclo.

## 1. Defina o que você quer aprender antes de definir logística

"Testar o sistema de combate" é vago demais para gerar feedback útil. Escreva de 3 a 5 perguntas concretas que o teste precisa responder, por exemplo:
- Quanto tempo de mesa um combate médio consome?
- Alguma classe/build está claramente dominante ou inútil?
- A letalidade está no nível certo (mata rápido demais, devagar demais)?
- As regras são claras o suficiente para um mestre resolver sem parar a mesa pra reler o documento?
- Existe alguma interação de regras que quebra ou trava o combate?

Essas perguntas viram o roteiro do que você vai pedir de feedback depois de cada sessão. Sem isso, você recebe só "achei legal" / "achei ruim", que não dá pra agir em cima.

## 2. Trave a variável: só o combate muda, e muda igual pra todo mundo

Durante a janela de teste, o resto do sistema (perícias, progressão, narrativa) continua como está. Só a resolução de combate é a "versão nova". Isso evita misturar, no feedback, problemas que não são do combate.

Mais importante: a matemática do combate (dano, iniciativa, ações, dificuldade) precisa ser **idêntica em todas as mesas**. O que pode variar de mestre pra mestre é a moldura narrativa — que inimigo, que cenário, como descreve — não a mecânica. Se cada um dos 5-7 mestres ajustar a regra "no jeito dele" no meio do teste, você não está testando um sistema, está testando sete variantes dele, e nenhum dado vira conclusão.

## 3. Proteja a continuidade dos personagens persistentes

Esse é o ponto mais arriscado do seu caso específico. Antes de abrir o teste:
- **Backup/snapshot da ficha** de cada personagem que for entrar em combate testado, para poder reverter se algo sair muito errado.
- **Regra de segurança combinada com antecedência**: durante o período de teste, uma morte que claramente resultou de um bug ou de uma regra mal calibrada (não de uma má decisão do jogador) pode ser revertida por consenso entre mestre e jogador, virando nocaute/derrota narrativa em vez de morte definitiva.
- **Ficha como fonte única de verdade, visível a todos os mestres**: como o mesmo personagem pode ir de uma mesa de segunda para uma de quinta com outro mestre, o segundo mestre precisa saber exatamente o que aconteceu na primeira sessão (dano, recursos gastos, condições) antes de começar. Isso já deveria existir independente do teste, mas durante o teste fica crítico, porque o estado muda mais rápido e de formas menos previsíveis.
- **Todos os mestres ativos rodando a mesma versão ao mesmo tempo.** Não dá pra ter adoção gradual por mestre (um usando v0.1, outro ainda no sistema antigo), porque o personagem circula entre eles — isso geraria inconsistência de estado imediata.

## 4. Uma versão, um documento, um árbitro

Distribua o documento da v0.1 para todos os mestres ao mesmo tempo, antes do início da semana de teste, com um número de versão visível (v0.1) e, se possível, um changelog mínimo.

Abra um canal fixo (uma thread ou canal só pra isso) para dúvida de regra durante a semana de teste. Designe uma pessoa — provavelmente você, como autor do sistema — como árbitro final de interpretação. Quando um mestre tiver uma dúvida ambígua em mesa, ele resolve do jeito que fizer sentido naquele momento (a mesa não pode travar esperando resposta), mas registra o caso no canal depois. Isso vira insumo pra próxima versão do documento e evita que a mesma ambiguidade seja resolvida de sete formas diferentes por sete mestres diferentes sem ninguém perceber.

## 5. Rollout em ondas, não simultâneo

Como só 2-3 mesas rodam por semana mesmo, use isso a seu favor em vez de tentar forçar todos os 5-7 mestres a testar ao mesmo tempo:
- **Onda 0 (piloto):** 1-2 mestres voluntários que conhecem bem o sistema (idealmente você e mais um) rodam combates de teste primeiro, de preferência com encontros controlados, pra pegar erros grosseiros e ambiguidades óbvias antes de expor o resto do grupo.
- **Onda 1 em diante:** expande para os outros mestres já com os ajustes do piloto incorporados.

Isso evita que 5-7 mesas batam no mesmo bug óbvio na mesma semana — o que forçaria você a revisar retroativamente decisões tomadas em várias mesas ao mesmo tempo.

## 6. Combates de referência, para poder comparar dados entre mesas diferentes

Combates que surgem organicamente na narrativa de cada mestre são ótimos pra testar em contexto real, mas são difíceis de comparar entre si (cada um tem inimigo, número de personagens e circunstância diferente). Vale preparar 2-4 "encontros de referência" padronizados (por exemplo: um combate 1x1 fácil, uma escaramuça em grupo, um combate mais difícil tipo chefe) que qualquer mestre pode encaixar na própria sessão durante a semana de teste. Isso dá pelo menos alguns pontos de dado comparáveis entre mesas, além dos combates orgânicos de cada história.

## 7. Registro estruturado depois de cada combate testado

Como as mesas acontecem em dias diferentes e você não está em todas, você depende de registro escrito, não de impressão geral relembrada depois. Peça que cada mestre preencha, logo após qualquer combate testado (formulário, planilha ou mensagem estruturada num canal — o formato importa menos que a consistência):
- Personagens envolvidos, nível/build de cada um
- Inimigo(s)/desafio enfrentado
- Número de rounds até resolução
- Tempo real de mesa gasto no combate
- O que travou, quebrou ou pareceu bugado
- O que funcionou bem / foi divertido
- Alguma ação, item ou build que dominou ou pareceu inútil
- Observação livre do mestre (e, se possível, uma linha de algum jogador)

## 8. Sincronização assíncrona entre mesas

Não dá pra reunir os 5-7 mestres ao vivo toda semana, então o ciclo de feedback precisa ser majoritariamente assíncrono: você compila os registros do item 7 ao longo da semana e publica um resumo. Se conseguir emplacar uma call curta de retro no fim de cada semana de teste com quem puder comparecer, melhor — mas o resumo escrito é o que garante que ninguém fica de fora só por ter mesa num dia diferente.

## 9. Dimensione a janela de teste

Uma única semana com 2-3 mesas dá poucos combates e pouca variedade de nível/build de personagem pra tirar qualquer conclusão confiável. Pense em um ciclo de 2-4 semanas antes de considerar a v1 "fechada", cobrindo personagens de níveis diferentes e situações de combate variadas (duelo, grupo vs. grupo, combate contra um único alvo forte, fuga/derrota).

Defina de antemão um critério objetivo de saída do teste — por exemplo: "combate médio resolve dentro de X rounds", "nenhuma build claramente dominante ou inútil nos registros coletados", "nenhuma trava de regra sem solução documentada". Sem critério definido, é fácil ficar em teste indefinidamente ou, no outro extremo, encerrar cedo demais.

## 10. Comunique aos jogadores e deixe uma válvula de escape

Avise explicitamente que aquela semana/período está com o combate em modo de teste, que as regras podem mudar depois, e que mortes serão tratadas com bom senso (item 3). Isso gerencia expectativa e evita frustração de jogador que sentiu o personagem prejudicado por um bug e não por uma escolha ruim.

Dê também ao mestre a permissão explícita de abandonar o sistema novo no meio de uma sessão e resolver no braço (freeform ou pelo método antigo, se houver um) se o combate travar de um jeito que ameace destruir a sessão. É melhor perder um ponto de dado do que perder a mesa inteira daquele dia.

---

## Checklist resumido

1. Escrever 3-5 perguntas que o teste precisa responder.
2. Fechar a v0.1 num documento único, versionado, distribuído a todos os mestres ao mesmo tempo.
3. Backup das fichas + regra de segurança para mortes duvidosas durante o teste.
4. Canal de dúvidas de regra com um árbitro final designado.
5. Rodar primeiro com 1-2 mestres voluntários (piloto) antes de abrir para os demais.
6. Preparar 2-4 encontros de referência padronizados, além dos combates orgânicos.
7. Formulário/registro padrão preenchido após cada combate testado.
8. Resumo semanal compilado por você, já que as mesas não se cruzam ao vivo.
9. Janela de teste de 2-4 semanas, com critério objetivo de saída definido antes de começar.
10. Aviso claro aos jogadores de que é uma versão de teste, com válvula de escape para o mestre abandonar a regra nova em caso de travamento sério.

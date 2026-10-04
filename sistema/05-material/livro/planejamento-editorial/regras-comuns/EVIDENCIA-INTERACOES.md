# Movimento e ambiente: decisões preservadas e interações sensíveis

Auditoria somente de leitura, Projeto M v0.331, 2 de outubro de 2026. Escopo: movimento, terreno, salto, queda, escalada e natação, com as capacidades que dependem deles. Não foram criadas regras, escolhidos custos ou alterados arquivos do projeto. Não foi usado Git.

## Autoridade e limites da busca

Confrontei `logs/CHANGELOG.md`, peças vigentes de `sistema/03-mecanica/`, os capítulos pertinentes do manual e `caminhos/05-Edicao-Integrada/`. Para o Incursor, usei também os registros de consolidação em `sistema/01-pesquisa/integracao-v0.331/`. A peça `06-caminhos-e-trilhas.md` identifica a edição integrada como dona atual das habilidades; seus desenhos anteriores são históricos. A coleção v0.4 e a antiga peça de Invocações não devem fornecer exceções novas por recuperação acidental de um texto abandonado.

O changelog é evidência do motivo e da aprovação de uma decisão, não licença para restabelecer tudo que constava naquela versão. Por exemplo, a entrada v0.11 confirma a base de movimento, mas sua antiga regra de Concentração foi substituída. As notas de consolidação também conservam frases antigas sobre o nome da terceira Trilha; o changelog v0.331 e a edição integrada fixam Malabarista. Usei apenas as decisões pertinentes confirmadas na fonte atual.

Não localizei aprovação anterior de uma fórmula geral de distância de salto, velocidade comum de escalada/natação, custo de terreno difícil ou dano por altura. Há regras de perícia, remissões e exemplos, mas nenhuma fórmula completa foi recuperada para ser simplesmente republicada. A discussão dessas lacunas continua necessária; a base já decidida abaixo não precisa ser reaberta.

## Decisões já tomadas que limitam a nova proposta

| Invariante | Fonte e consequência |
|---|---|
| **Base de 9 m e divisão do movimento no turno** | `logs/CHANGELOG.md`, v0.11, linhas 22737–22739; peça `03-economia-de-acao-e-iniciativa.md`, §3, linhas 41–52; manual `11-o-turno.md`, Deslocamento. O histórico justifica 9 m em relação ao Projétil de 18 m e às áreas. Andar, atacar e continuar andando já é universal; não deve virar uma concessão de Parkour. |
| **Ação de Movimento não é a distância** | Changelog v0.123, linhas 12716–12720; peça 03, §3.2. Sacar/guardar além da franquia pode consumir a ação inteira. Uma nova regra não deve tratar qualquer gasto dessa ação como personagem que se deslocou. |
| **Recarregar com Movimento não é deslocar-se** | Changelog v0.218, linhas 4471 e 4551, afirma isso expressamente. A separação também importa para Estudar a Guarda. Regras de deslocamento voluntário não devem acender porque alguém pagou uma ação para operar um objeto. |
| **Ataque de oportunidade existe e tem exceções expressas** | Changelog v0.11, linha 22740; peça 03, §3; manual `11`, Ataque de oportunidade. Incursor não recebe imunidade universal por ser acrobático. As proteções de Passo Rápido/Guardado, vítima como apoio e nível 30 têm escopos diferentes. A interação universal com empurrão/queda não ficou fechada no recorte encontrado. |
| **Incursor ganha +3 m no nível 2** | Edição integrada `06-Incursor-Caminho-e-Trilhas.md`, Movimento Acrobático, linhas 44–50; consolidação `03-DECISOES-DA-CONSOLIDACAO.md`, Incursor. Um personagem de base 9 m passa a 12 m; o +3 m não é apenas uma permissão de parede. |
| **Movimento Acrobático usa movimento disponível e um limite compartilhado** | Mesma fonte, linhas 48–50. Até metade do deslocamento no nível 2; completo no 23, incluindo modalidades da Trilha (linhas 114–116). Não concede metros gratuitos, sucesso automático, voo ou dispensa geral de oportunidade. |
| **Passo Guardado é movimento adicional, sem reserva** | Edição integrada Incursor, linhas 100–106; notas de integração, Pendências antigas resolvidas. Exige Fluidez presente e capacidade de mover-se após resolver o ataque/TR; não gasta Fluidez nem Reação. Não restabelecer a antiga ideia de reservar parte do movimento. |
| **Retomar gasta a Ação de Movimento inteira** | Incursor, linhas 108–116. Só quando vazio no começo do turno; não transforma metros percorridos em Fluidez. Gastar a ação e receber movimento adicional de outra habilidade são coisas distintas. |
| **Nível 30 dobra deslocamento e antecipa um único turno** | Incursor, Um Passo à Frente, linhas 118–132. Só antes do turno de outra criatura, se ainda não agiu na rodada; substitui o habitual. Mantém ações, custos e apoio final. Não confundir “dobrar o deslocamento” com Correr, que acrescenta movimento. |
| **Quedas pertencem ao dano de Concussão** | Manual `15-dano-e-condicoes.md`, Tipos de dano, linha 25. O tipo já tem referência. A quantidade por altura, prevenção e aterrissagem ainda não foram localizadas como regra geral. |

Há também um precedente útil de redação vigente: Vanguarda/Batedor, **Romper o Contato**, define “metade do deslocamento que sua ficha oferece nessa situação, já considerando as reduções”, distinguindo isso dos metros restantes (`02-Vanguarda-Caminho-e-Trilhas.md`, linha 384). Pode orientar a clareza da regra básica sem presumir que encerrou sozinho todos os cálculos do Incursor.

## Onde a proposta pode mudar habilidades sem querer

### Incursor e a contabilidade do movimento

É necessário distinguir três grandezas na discussão: **valor de deslocamento da ficha**, **distância física percorrida** e **quanto do movimento disponível o percurso consome**. Um custo de terreno pode afetar a terceira sem reduzir diretamente a primeira. O livro usa metade do deslocamento para capacidades e gatilhos; decidir essas grandezas por implicação pode alterar o funcionamento de várias Trilhas.

O limite acrobático é compartilhado, mas sua recomposição ao dividir o percurso entre ações, Passo Rápido, Passo Guardado e turnos alheios não está explicitada com o mesmo relógio usado para Fluidez. A regra nova precisa tornar essa leitura verificável. Não presuma que cada nova ação ou cada interrupção abre outra metade, nem imponha um limite por ciclo que ainda não foi escrito.

Correr dá metros adicionais. Um Passo à Frente dobra o valor de deslocamento. A distinção determina a extensão de “metade”, do limite acrobático e do gatilho de Parkour. Conserve a diferença aprovada antes de medir combinações.

### Assassino: parede, salto, descida e apoio

Fonte: Incursor integrado, **Parkour**, linhas 220–255; **Estudar a Guarda**, linha 166; **Cortar a Fuga**, linha 212.

- Parkour troca Atletismo por Acrobacia nos testes para saltar ou alcançar apoios usados durante Movimento Acrobático. Não apaga dificuldade, consequências ou distância. Uma proposta que passe a resolver todo salto apenas pelo atributo Força precisa tratar explicitamente o valor dessa troca; não basta manter seu nome no texto.
- A aproximação exige percorrer **pelo menos metade do deslocamento por uma parede e depois saltar**, ou **descer pelo menos 4,5 m de posição elevada com apoio**, usando Movimento Acrobático. O primeiro ataque corpo a corpo durante/imediatamente ao fim ganha a oportunidade. Não converter a descida apoiada em qualquer queda livre.
- Com deslocamento 12 m, a primeira aproximação pede 6 m de parede. O limite acrobático inicial também é 6 m. **Se** uma proposta cobrar duas unidades de movimento por cada metro nessa parede, esses 6 m consumiriam todos os 12 m antes do salto. Isso é um teste de compatibilidade, não uma defesa de um custo específico: o pacote aprovado não deve ficar inexequível no nível 2 sem uma decisão expressa.
- Apoios de infiltração autorizam terminar pendurado em borda/superfície capaz de sustentar o personagem, com pelo menos uma mão ocupada. Isso excepciona o apoio normal exigido pelo Caminho; não torna qualquer parede um apoio e não fornece mãos extras para arma/Selo.
- A vítima como apoio não concede ataque extra nem metros: depois de resolver o ataque e seus efeitos, permite um salto com movimento restante, uma vez no próprio turno, sem oportunidade. Definir salto e queda pode viabilizar ou inviabilizar essa saída. Se Cortar a Fuga empurra a vítima antes, não se pode ignorar a ordem já escrita para assumir um apoio ainda ao alcance.
- Estudar a Guarda impede movimento voluntário durante a rodada, incluindo Passos adicionais; movimento forçado permanece. A redação básica precisa preservar a diferença entre deslocamento forçado e um retorno voluntário feito em resposta a ele. Pagar ação de Movimento sem andar também não é o gatilho proibido.

### Pugilista: superfície líquida, retorno e projeção

Fonte: Incursor integrado, **Recuperar a Base**, linhas 366–374; **Movimento sobre líquidos**, linhas 407–411; **Projeção Marcial**, linhas 425–449.

Movimento sobre líquidos acrescenta uma modalidade ao Movimento Acrobático: usa o mesmo orçamento, exige apoio normal ao terminar e não elimina os efeitos de contato com o líquido. Não é flutuação parada, imunidade a ácido/lava nem respiração submersa. O nível 23 amplia também essa modalidade. A natação comum precisa conservar uma utilidade distinta sem transformar a superfície líquida em chão universal.

Recuperar a Base exige **um único empurrão** de pelo menos metade do deslocamento e só então concede retorno de até metade, pago com Fluidez. Dois empurrões menores não são um único efeito. O retorno usa percurso e oportunidades normais e não é um cancelamento retroativo do empurrão. Se o movimento terminar num poço, água ou sem apoio, é preciso saber quando queda/impacto se resolvem antes de concluir se o personagem consegue retornar. Levantar-se com a opção contra Derrubado tampouco cancela automaticamente o dano de queda.

Projeção escolhe espaço livre a até 6 m, com trajetória válida, encerra a contenção na falha, causa dano desarmado e deixa o alvo Derrubado. A colisão com uma segunda criatura tem TR próprio e dano explícito. Uma regra geral de colisão ou queda pode somar dano novo a esse pacote; esse ganho não deve passar despercebido sob o título de esclarecimento editorial. A habilidade não rola ataque, não crita e não gera Fluidez por acerto.

### Batedor e efeitos de terreno

Fonte: Vanguarda integrada, **Soltura Preparada**, linha 220; **Fixar o Alvo**, linha 100; **Romper Fileira**, linha 176; **Ancorar**, linha 182.

Soltura Preparada já concede deslocamento de escalada igual ao normal. Não declara que toda parede dispensa apoio/teste, nem concede o percurso acrobático de criaturas do Incursor. A regra de escalada deve explicar o que muda com um deslocamento específico. Se a regra comum passar a dar o mesmo desempenho sem condição, a concessão perde parte ou todo seu benefício, o que deve ser uma decisão de design consciente.

Fixar o Alvo aceita terreno difícil como a redução prévia necessária. **Mesmo que** a futura regra trate terreno apenas como custo por trecho, essa elegibilidade específica continua escrita. Fechar a Rota, por sua vez, declara não bastar sozinha. Não apagar essa distinção por uma mudança de vocabulário.

Romper Fileira move o alvo por trajeto livre **sobre a superfície que o sustenta**; Ancorar deixa explícito que deslocamento zero não impede movimento forçado ou teleporte. Esses textos são exceções/instruções atuais e ajudam a identificar casos, sem substituir uma regra universal ainda pendente.

### Empurrar e transformar altura em dano

Fonte: Bastião integrado, **Mão Pesada**, linhas 116–118; Vanguarda integrada, **Rasteira**, linha 92, e **Empuxo**, linha 123; Incursor, **Cortar a Fuga** e **Projeção**.

Mão Pesada empurra até 4,5 m na direção escolhida após acerto, uma vez por alvo/rodada; o TR da opção Derrubado/Agarrado é uma parte adicional. Cortar a Fuga e Empuxo especificam afastar; Rasteira combina derrube e empurrão na mesma falha; Projeção possui lançamento e colisão próprios. Uma regra geral não deve acrescentar outro TR a todos por hábito, nem presumir que os textos têm os mesmos limites de direção/tamanho/suporte.

Quando existir dano por altura, testar **empurrão vertical**, **lançamento para espaço sem apoio**, **empurrão por cima de beirada**, **trajeto bloqueado por parede** e **arrastar alguém agarrado para o precipício**. Algumas permissões estão abertas e outras restringem a superfície. Não há aqui autorização para decidir que todos os empurrões são horizontais ou que todos arremessam para cima. O primeiro cenário é especialmente sensível à Mão Pesada: um empurrão que hoje reposiciona pode virar dano adicional recorrente se o texto aceitar elevar e cair.

## Casos-limite para conferir antes de aprovar números

Estes são testes de decisão, não respostas novas:

| Caso | O que precisa ficar verificável |
|---|---|
| Personagem de 9 m anda 3 m, ataca e anda 6 m | A regra preserva a divisão já universal. |
| Incursor de 12 m faz parede e salto no nível 2 | A aproximação de 6 m de parede ainda permite executar o salto e alcançar apoio; o custo e o limite acrobático são contas distinguíveis. |
| Mesmo personagem usa Correr; depois repete sob nível 30 | O texto distingue metros adicionais de deslocamento dobrado, sem abrir novas quotas por silêncio. |
| Passo Guardado ocorre após já percorrer paredes no próprio turno | A mesa sabe que limite acrobático consultar e quando ele renova. |
| Retomar consumiu Movimento; depois há Passo Rápido ou Correr pela Bônus | Não se exige reservar metros já descartados, mas todos os custos próprios continuam pagos. |
| Assassino desce 4,5 m com apoio versus cai 4,5 m sem apoio | O gatilho de aproximação, os testes e o risco têm respostas distintas onde o texto as exige. |
| Ataque acerta, Cortar a Fuga afasta a vítima, personagem quer usá-la de apoio | A ordem de resolução aprovada e a posição real da vítima são respeitadas. |
| Personagem termina pendurado, arma ocupa a outra mão | A próxima ação cumpre seus requisitos; pendurar-se não vira apoio sem mão por omissão. |
| Pugilista cruza água; é parado no meio; cruza líquido nocivo | Apoio final, natação/queda e efeito de contato são compreensíveis sem inventar imunidade. |
| Pugilista de 12 m recebe um empurrão de 6 m; depois dois de 3 m | Um efeito elegível não é confundido com soma de eventos; retorno resolve depois, não desfaz. |
| Lento, Derrubado, dano de alma e terreno atuam juntos | A regra determina qual valor é reduzido, quando e como se combinam custos distintos; não escolher soma/multiplicação incidentalmente no exemplo. |
| Yumi escala no deslocamento normal; outra pessoa escala o mesmo muro | É possível apontar o benefício da concessão sem dispensar todos os testes do Yumi ou impedir a tentativa comum. |
| Fixar o Alvo atinge alguém no terreno difícil | A condição específica continua satisfeita conforme o texto aprovado, mesmo se o novo terreno for descrito em custos. |
| Mão Pesada/Projeção termina junto de parede ou precipício | Colisão e queda não duplicam/retiram dano sem decisão; direção e apoio não são inventados por quem lê. |
| Uma medida resulta em fração fora do padrão usual do mapa | Não se introduz uma grade obrigatória nem se arredonda 4,5 m para outra distância silenciosamente. A política geral de arredondamento existe (peça 01, §5.4), mas sua aplicação à medição espacial precisa ser compatível com os alcances fracionários publicados. |

## Ordem de prioridade sugerida

1. **Fechar o vocabulário operacional e o percurso:** deslocamento, movimento disponível, ação inteira, distância percorrida, trecho, apoio e quando o limite acrobático se recompõe. Preservar divisão e conversões. Essa camada decide o que os números seguintes significam.
2. **Decidir terreno e travessia de parede em conjunto com o Parkour inicial.** Conferir custos, reduções e a concessão do Yumi antes de consolidar tabelas. Não publicar um custo genérico primeiro e descobrir depois que o salto do Assassino deixou de caber.
3. **Fechar salto, descida e queda com os empurrões e lançamentos.** Separar execução apoiada de perda de apoio; explicitar sequência de resolução e consequências. Medir os novos danos possíveis com Mão Pesada e Projeção antes de chamar o ajuste de puramente textual.
4. **Completar natação e a transição superfície/submerso**, preservando o Pugilista. O grau de detalhe pode ser pequeno, desde que responda às cenas efetivamente prometidas pelo livro.
5. **Só então rever exemplos e remissões das Trilhas**, sem redesenhar kits já aprovados. Um exemplo comum, um acrobático e um deslocamento forçado devem produzir a mesma interpretação de ação, metros, apoio e consequência entre leitores.

O dado mais importante da busca é que há autorização clara para preservar a identidade móvel e seus recursos; não há uma tabela antiga fechada capaz de eliminar a atual decisão de design. É possível avançar a regra básica sem reabrir todo o Incursor, desde que seus gatilhos e permissões entrem como casos de compatibilidade antes de escolher números.

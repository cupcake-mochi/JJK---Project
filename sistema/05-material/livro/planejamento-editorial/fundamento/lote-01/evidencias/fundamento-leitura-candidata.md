# Fundamento — leitura crítica da candidata

Auditoria editorial e de compreensão realizada por agente, sem leitores humanos nem playtest. Nenhum texto foi editado.

Fonte: `sistema/05-material/livro/planejamento-editorial/fundamento/lote-01/FUNDAMENTO.md`, 26 páginas lógicas, 800 linhas na leitura inicial. SHA-256 observado ao fim da leitura: `cf8571a7831fdaa39bf6da3419dea196dc22f7b8a89dbe847bdcb1df68b59974`. Como o manuscrito pode estar sendo reorganizado, as âncoras `page:` são a localização principal; linhas referem-se à versão lida.

## Parecer

O texto explica muito melhor a criação comum. Separar descrição e efeito comprado, fixar as decisões na ficha e mostrar cálculos completos resolve problemas concretos. Os títulos são reconhecíveis num livro de RPG; não há títulos “Como ler”, digressões de classe nem passagens de narrativa rebuscada. As 26 páginas têm funções identificáveis, mas ainda podem dar sensação de catálogo antes de jogo se o primeiro exemplo ficar na sexta página.

**Recomendo mover `primeiro` para depois de `tecnica`, tornando-o a terceira página.** Ele contém os números necessários para seguir sem consultar o restante. Na etapa Classe, basta ligar “maior Classe” a `pontos`. Famílias e Selo aparecem na ficha como escolhas de Mei; os detalhes podem vir logo depois. Não mover todas as regras para antes do exemplo.

A candidata não está pronta para ser tratada como substituição completa do Fundamento antigo: remete a catálogos ainda sem destino editorial identificável, e falta uma demonstração convincente de Técnica Máxima sem dano durante combate. Isto deve aparecer como limitação real da entrega, caso não seja resolvido neste lote.

## Achados que merecem correção antes da entrega

### P1 — regra de conjuração enfraquecida na remissão a Turnos

**Local:** `conjurar`, Ação e duração, linha 341.

Texto limita o outro feitiço a Classe 0 se um feitiço usar Bônus ou Reação. A fonte revisada `regras-basicas/lote-01/TESTES-E-TURNOS.md:207` diz que **qualquer** feitiço acima de Classe 0 permite apenas mais um de Classe 0 no turno. A candidata pode ensinar que duas Ações Padrão liberam dois feitiços positivos sem habilidade expressa.

**Substituição recomendada:**

> No seu turno, conjurar um feitiço acima de Classe 0 permite apenas mais um feitiço de Classe 0, salvo permissão expressa. Converter ou receber ações adicionais não remove esse limite. Bônus, Reação e Ação Completa precisam constar da ficha; seus requisitos estão em **Testes e Turnos — Ações Bônus e Reações**.

Conferir o título exato da remissão: no candidato de Turnos existem seções distintas. Preferir dois destinos reais a inventar uma seção conjunta.

### P1 — a apresentação de Máxima ainda não demonstra o caso difícil solicitado

**Locais:** `maxima`, linha 702; `maximadano`, linhas 733–739; `passagem`.

A frase “um ataque, uma cura ou um Efeito sem dano” usa Efeito com maiúscula, que o próprio capítulo define como Forma fora de combate. Isso aparenta excluir Controle ou Apoio sem dano em combate, embora a página seguinte admita Apoio. Além disso, a única Máxima inteiramente sem dano é um portal fora de combate que fecha quando uma luta começa. O combate exemplar continua sendo 24d8 mais duas Melhorias baratas; o texto manda usar um feitiço comum se ele resolver a função por menos PE.

O leitor que reclamava de “Máxima só serve para dano/cura” entende agora a contabilidade, mas ainda não vê **o que faz uma Máxima de controle/proteção valer a escolha**. Acrescentar orçamento não demonstra sozinho esse valor quando todo o resultado de 24–32d8 é descartado.

**Correções exatas recomendadas:**

1. Trocar a frase por “Você registra uma aplicação com dano, com cura ou sem nenhum dos dois. Escolha a Forma adequada ao resultado; Controle e Apoio podem funcionar em combate, enquanto a Forma Efeito segue suas regras fora dele.”
2. Acrescentar uma ficha curta de Máxima sem dano **utilizável em combate**, com ação/PE, quatro ou menos Melhorias, efeito principal mensurável, alcance, duração, reação possível do adversário e comparação com a Classe comum correspondente. Isso pode substituir parte das advertências de `maximadano`, sem criar mais uma página inteira.
3. Se a criação atual não permitir um exemplo que compense, registrar “Máxima de Controle/Apoio em combate ainda requer revisão de design”; não encerrar esse pedido como resolvido apenas com Passagem de Papel.

Não proponho números novos neste relatório: esse ponto exige a decisão e a validação mecânica que os outros revisores estão conduzindo.

### P1 — “o catálogo” não identifica onde o jogador encontra a regra completa

**Locais:** `selo:125`, `restricoes:365`, `controle:418–422`, `aplicacoes:459,467`, `conjurar:343`.

Há referências como “catálogo de Passivas”, “o catálogo traz as demais Restrições”, “quadrados permitidos pela peça” e “pelos prazos das peças”. A ficha de Anteparo fica impossível de usar só com o exemplo: omite comprimento, altura e arranjo da parede. No socorro, as durações de Impulso/Pressa também não estão na ficha.

As referências ao catálogo antigo não são intercambiáveis com o novo procedimento: peças como Fica e incompatibilidades foram revistas. Uma remissão genérica pode fazer o jogador reintroduzir a regra antiga conflitante.

**Correção recomendada:** dar um destino editorial estável a cada referência, como **Catálogo de Melhorias — Controle — Anteparo** e **Catálogo de Passivas — Regra Própria**. Se R07 não está pronto, a documentação da entrega deve deixar isso visível. Nos **exemplos que se dizem fichas**, trazer a informação mínima de execução sem obrigar a procurar: dimensões do Anteparo; fim do benefício de Impulso; fim de Pressa. Não copiar o catálogo inteiro.

### P2 — progressão está espalhada e não responde à atualização da Máxima

**Locais:** `repertorio:142,152`, `classezero:616–618`, `ampliar`, `maxima`.

O leitor aprende que Classe 0 sobe sozinho, Ampliar recalcula e reescrever um feitiço ocupa a revisão. A Técnica Máxima ganha mais dados e orçamento em outras faixas, mas não fica claro quando pode adicionar peças ao orçamento novo, se preserva a ficha automaticamente, nem se uma reescrita da Máxima pode ser a revisão de nível.

**Correção recomendada:** inserir em `maxima` uma frase explícita decidida pelo autor: quais números acompanham a faixa automaticamente e em que ocasião se redistribuem as peças. Se redistribuir usa a revisão comum, declará-lo, como já foi feito para Liberação. Evitar “como qualquer feitiço” sem definir se Máxima entra nesse grupo.

### P2 — detalhes de “Selo e Passivas” chegam antes do primeiro uso

**Locais:** ordem atual de `familias`, `selo`, `repertorio`, `primeiro`.

São decisões obrigatórias e úteis, mas aprender primeiro suas exceções (Família bloqueada, Restrição sobre Selo, Passivas pagas, Domínio) adia a recompensa de completar uma ficha. Mover o exemplo para p.3 resolve a maior parte. Na abertura, acrescentar somente a distinção curta:

> Espaços guardam suas aplicações conhecidas; pontos montam cada aplicação; PE paga cada uso.

Não acrescentar outro glossário extenso.

### P2 — “Travessia por um fio” anuncia uma ação que a ficha não concede

**Local:** `aplicacoes:449–453`.

Prender um fio numa viga e puxar o corpo evoca subir ou atravessar um vão. O resto do exemplo retira justamente escalada, voo e transporte entre apoios. Fica uma promessa narrativa negada por vários parágrafos.

**Substituição recomendada para a primeira frase:**

> Mei prende um fio numa coluna e se puxa por um corredor desimpedido.

Usar o título **Recuo por um fio** ou **Deslocamento por um fio**. Depois basta conservar a medida de 6 m e a exigência de percurso permitido. Guardar a discussão de voo/teleporte para a orientação geral de Efeitos próprios.

### P2 — expressão artificial em Uso Livre

**Local:** `livre:520`, “abafar a aparência sonora de um passo”.

Som não tem “aparência sonora” para o leitor cotidiano; a frase parece tentar negar mecanicamente o que o verbo abafar promete na ficção.

**Substituição recomendada:**

> Mudar o som que acompanha sua técnica não concede vantagem em Furtividade, um teste gratuito de Esconder nem silêncio completo. Esses benefícios precisam de um efeito que os permita.

### P2 — geometria ainda fica abstrata demais para parte dos leitores

**Locais:** `formas`, `alcance`.

Raio, largura de cone e comprimento da linha estão corretos e distinguíveis, mas são seis Formas em tabelas sem nenhuma vista de cima. Uma pequena figura vetorial de grade com origem, raio e linha ajudaria mais que repetir três vezes que alcance e área são diferentes. Isso respeita a proibição de imagem de IA. Não é bloqueador desta entrega se já houver um diagrama no capítulo de movimento, desde que haja remissão explícita.

## Respostas às 16 perguntas de iniciante

Estas respostas usam o manuscrito e os destinos que ele indica; onde a remissão é vaga, essa limitação é anotada.

| # | Pergunta | Resposta que o leitor consegue obter | Resultado |
|---|---|---|---|
| 1 | Nível 2: quantas criações e qual Classe? | Três espaços comuns, dois Classe 0, Classe máxima 1. Passivas/entidades podem ocupar os espaços comuns. `repertorio`, `pontos`, `classezero`. | Respondida. O exemplo adiantado reduz a busca. |
| 2 | Espaço acaba ao usar? Pontos e PE são a mesma reserva? | Espaço permanece; PE é pago a cada uso. Pontos são a conta de montagem. `repertorio`, `primeiro`, `pontos`. | Respondida. Resumo de três moedas na abertura melhora retenção. |
| 3 | Quero entidade: o que deixo de conhecer e onde monto? | Ocupo um espaço em vez de um feitiço; ficha e uso ficam em Invocações. `repertorio`. | Respondida por remissão identificável ao capítulo. |
| 4 | Posso usar espaço do marco, Classe 0 ou Kata? | Marco integra a fórmula normal; Classe 0 não fornece vaga; Kata e Manejo admitem a troca. | Respondida. “Inclusive os recebidos nos marcos” pode eliminar a última inferência, sem nova regra. |
| 5 | Papel protegendo: ganho Defesa pela descrição? | Não. A descrição sustenta a ideia, mas o efeito é comprado, como Anteparo ou peça de Amparo. | Respondida. |
| 6 | Impedir saída de sala: Efeito, parede ou condição? | Parede usa Anteparo e pode ser destruída; prender alguém usa Prende/condição e resolução; escala Efeito não obriga hostis. `controle`, `efeito`. | Respondida no princípio; geometria e escape dependem de catálogo sem destino preciso. |
| 7 | Feitiço sem dano em combate: Forma e sobras? | Formas de ataque podem levar Controle sem dano; pode descartar saldo, sem converter descarte em bônus. Apoio converte seu saldo próprio em vida temporária. | Respondida para comum. Ajustar redação de Máxima para não contradizer. |
| 8 | Toque + Longe? Como reparar? | Não; usar Projétil e retirar a devolução de Corpo a Corpo. `formas`, `combinacoes`. | Respondida com exemplo adequado. |
| 9 | Restrição embutida ou igual ao Selo conta outra vez? | Embutida ocupa uma das duas; não se repete. Selo não devolve pelo mesmo requisito. | Respondida. |
| 10 | Ataque/TR escolhido quando? Qual teste e sucesso? | Na criação, não por alvo. Outra resolução ocupa outra ficha/espaço ou reescrita. Mestre verifica relação com um dos quatro TRs; sucesso normalmente evita efeitos e recebe metade do dano. | Respondida; consultar Testes e Turnos para os quatro atributos. |
| 11 | Alcance é distância ao centro ou tamanho da área? | São medidas distintas; exemplo Explosão + Longe + Maior demonstra os dois. | Respondida. |
| 12 | Duração, interrupção e novo teste? | Uma rodada termina no começo do próximo turno do conjurador; prazo específico prevalece; Pesada testa no fim dos turnos; concentração e escapes seguem peças. | Parcial: os destinos e prazos de peças nos exemplos precisam ficar explícitos. |
| 13 | Ampliar versus nova criação? | Ampliar conserva Forma, peças, TR e resultado; muda números. Trocar peças/resultado requer outro espaço ou reescrita. | Respondida com conta antes/depois. |
| 14 | Máxima de resgate/controle sem frase vaga? | Passagem de Papel define resgate preparado fora de combate com distância, duração, concentração, pontos e encerramento. Não há ficha de resgate/controle sem dano utilizável durante combate. | Parcial no objetivo central do usuário. |
| 15 | Comprar peças diminui dados da Máxima? Requisito pode existir? | Não diminui; dados e pontos são separados. Requisito tem de ser cumprido, mas não devolve pontos. | Respondida de forma clara. |
| 16 | Ao subir de nível, o que muda sozinho e o que reescrevo? | Classe 0 sobe automaticamente; a lista recebe espaços; há uma revisão; Ampliar é uso voluntário. Falta tratar reconstrução/atualização da Máxima e dizer se ela pode ser reescrita. | Parcial; corrigir no dono da Máxima. |

## Suficiência, redundância e títulos

**Conservar:** os títulos Fundamento, Famílias, Conjurar, Controle, Ampliar um feitiço e Ficha de feitiço. São diretos, familiares e localizáveis. Seu primeiro feitiço é instrutivo sem virar “Como ler”. A ficha final contém os campos que faltavam na versão publicada.

**Repetições justificadas:** Toque/Longe aparece na apresentação da Forma, na matriz e no reparo de uma ideia. Cada ocorrência cumpre um uso de consulta diferente. Não cortar todas. O mesmo vale para não converter pontos de Restrição em dano adicional.

**Repetições redutíveis:** “a aparência não dá benefício” aparece em quase todos os exemplos. É necessário no primeiro e em Efeito próprio; nos exemplos posteriores, guardar só a limitação concreta de cada caso. “Aqui a utilidade foi comprada; não veio de chamar o dano de fio” pode sair sem perda, especialmente se seu espaço receber a Máxima não ofensiva de combate.

**Amparo não é repetição de classe:** há menção a rotas apenas para acesso/contabilidade. Isso é pertinente e não reconta habilidades de Caminho. As exceções de dupla aquisição ficaram corretamente no dono.

**Vocabulário:** a maior parte é acessível; “saldo”, “montagem”, “origem”, “restrição” são definidos pelo uso. “Resolução”, “concentração” e “Integridade” pedem destino concreto, não longas explicações repetidas. “Pacote”, em Dano e repetições, pode virar “total de dados da montagem” para reduzir o tom de documento técnico, mas não bloqueia entendimento.

**Volume:** 26 páginas comportam criação, uso, exceções e trunfos; não há motivo para reduzir por uma meta arbitrária. O problema é a ordem e a utilidade de cada consulta. Sem os catálogos referidos, o tamanho não significa completude. Com o primeiro exemplo na terceira página e remissões estáveis, o leitor consegue executar uma tarefa antes de absorver a lista inteira.

## Checagem final recomendada

Após os ajustes, realizar uma leitura sem voltar à fonte antiga: montar o primeiro feitiço, explicar os três recursos, reservar entidade, corrigir Toque/Longe, atualizar para Classe maior e construir uma Máxima sem dano em combate. Pedir que o revisor indique **qual frase** resolve cada decisão. Se precisar supor uma regra ou consultar conversa, registrar lacuna em vez de aprovar por plausibilidade.

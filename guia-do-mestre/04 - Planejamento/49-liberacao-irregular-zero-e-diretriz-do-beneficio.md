# Liberação irregular: resultado zero e direção do benefício

22 de outubro de 2026. **Estrutura escolhida; benefício e distribuição em desenvolvimento.** Este documento atualiza o [planejamento 48](48-liberacao-irregular-estrutura-e-comparacao.md). A numeração pertence ao planejamento; ainda não há seção 49 jogável no manuscrito.

## Escolhas recebidas

Mizuki aceitou o teto total de gasto do começo do próprio turno até o começo do seguinte, incluindo Reações e manutenção, com uma condição: **precisa existir a possibilidade de o limite ser zero**. Dado, frequência de zero e valores positivos continuam abertos.

Sobre ampliar a reserva, respondeu: “A gente tinha trabalhado algo no livro, mas n lembro oq era, ideal é ser criativo nesses casos”. Isso pede recuperação do material e desenvolvimento de um ganho próprio. **Reserva máxima maior não foi escolhida e deixa de ser a recomendação principal.** As perguntas e respostas completas estão no [registro 06](06-registro-das-decisoes.md).

## O que zero significa

**Com limite zero, você conserva a energia guardada, mas não pode fazer novos pagamentos de PE até o limite ser renovado.** PE são os pontos de energia da ficha. O limite mede quanto você pode gastar no intervalo; o saldo mede quanto ainda tem.

Hana começa o turno com 24 PE guardados e sorteia zero. Ela não pode pagar um feitiço de 3 PE nem Amortecer por 2 PE. Pode se mover, interagir e escolher ações que não exijam PE, conforme suas regras. No próximo começo de turno, se o novo limite for 10 e nenhum outro efeito tiver alterado a reserva, terá saldo 24 e poderá gastar até 10 naquele intervalo. O sorteio não acrescentou 10 PE à ficha.

| Situação | Aplicação da estrutura escolhida |
|---|---|
| Reação com custo de PE | Precisa caber no limite restante, mesmo fora do próprio turno. Zero impede o pagamento. |
| Manutenção que vence no intervalo | Precisa caber no limite. Se não couber, aplicar a consequência de falta de pagamento daquela capacidade. |
| Efeito já pago | Continua pelo seu prazo e requisitos. O resultado zero, sozinho, não desfaz o efeito. |
| Proteção ou capacidade sem custo de PE | Continua conforme sua regra. Não retirar a parcela passiva de Cobrir-se de Energia só porque Amortecer ficou indisponível. |
| Energia temporária | Seu gasto também entra no total pago. Ter temporários não contorna o limite zero. |
| Recuperação de energia | Pode mudar o saldo pelos meios permitidos; não aumenta por si o limite de gasto do intervalo. |
| Capacidade que exige esgotar a reserva | Conferir o saldo real. Limite zero com 24 PE guardados não equivale a gastar os últimos PE. |
| Entidade com reserva própria válida | Contar apenas o que sai do portador. A parcela que ele precisa cobrir também está limitada; não conceder reserva própria a uma entidade que não a possui. |

A manutenção de entidades merece atenção: a R53 prevê casos de suspensão até o próximo pagamento previsto, sem dívida. Outras capacidades podem terminar. O Pacto não transforma todas essas consequências em encerramento ou destruição.

O mínimo de 1 usado nas hipóteses antigas **não se aplica ao resultado zero**. O arredondamento dos resultados positivos ainda será definido junto da distribuição.

Antes de publicar o modelo, faltam também o limite inicial anterior ao primeiro turno, a ordem de eventos simultâneos, a cadência fora de iniciativa, mudanças de máximo, combinações com outros Pactos e o encerramento. Os procedimentos sugeridos no documento 48 continuam propostas nesses pontos.

## O que foi recuperado do livro

A R53 estabelece, em **Pacto permanente — Benefícios**, que o ganho é uma mecânica única decidida com o mestre, capaz de modificar um feitiço, a energia, uma aptidão ou um Estilo. O texto pede uma mudança de funcionamento e veda usar o Pacto para bônus numéricos de ataque, Defesa, perícias ou dano. Pactos de energia podem alterar seu funcionamento ou devolver energia; quando existe uma quantidade, ela é expressa como porcentagem do máximo.

Essa diretriz corresponde ao pedido de criatividade, mas não comprova que seja a passagem exata lembrada pelo autor. Nos textos consultados, **não foi localizado um benefício específico já fechado para Liberação irregular**.

| Fonte consultada | Conteúdo encontrado | Uso nesta etapa |
|---|---|---|
| R53, Pactos permanentes e Ideias para desenvolver | Regra geral de mecânica única; Liberação irregular aparece como conceito cujo procedimento precisa ser escrito. | Fonte atual para desenvolver o exemplo. |
| Claude 2, `sistema/03-mecanica/22-pactos.md` | Teto de PE rolado no começo do turno, inclusive com reserva cheia. | Recupera o núcleo da limitação. |
| Claude 2, `sistema/99-arquivo/RASCUNHO-pactos.md` | Ideia de teto por turno rolado. | Histórico do conceito. |
| Claude 2, `sistema/05-material/livro/manual/65-pactos.md` e cópias consultadas no projeto RPG | Formulações anteriores da ideia e regras gerais antigas de benefícios. | Referência histórica; não substitui a R53. |

As regras antigas de benefícios não devem ser importadas em bloco: há permissões anteriores que divergem da R53, inclusive sobre Estilos e ganhos numéricos. A permissão atual de usar porcentagens em Pactos de energia também não torna qualquer acréscimo percentual uma compensação adequada. Por isso, a recomendação anterior de aumentar o máximo precisa ser revista à luz da exigência de alterar o funcionamento da capacidade.

### Capacidades já existentes

**Armado** permite pagar ação e PE antes e liberar o feitiço quando ocorrer um gatilho, sem Reação, respeitando seus limites. **Segura** permite adiar o efeito e dispará-lo no próximo turno sem outra ação. Assim, “pagar quando a energia sai e resolver o efeito depois” já tem aplicações na R53. Apresentar apenas isso como ganho novo repetiria uma possibilidade que a ficha pode obter por sua montagem normal.

Um efeito Armado já pago pode, pela estrutura em desenvolvimento, resolver durante um intervalo de limite zero se cumprir sua própria regra e não exigir novo pagamento. Isso decorre da separação entre pagar e resolver; não é um benefício adicional deste Pacto. O Pacto não concede Armado ou Segura automaticamente.

## Quanto pesa a possibilidade de zero

A frequência ainda não foi escolhida. As contas abaixo mostram por que não basta colocar zero numa tabela e tratar qualquer dado como equivalente.

| Chance de zero em cada sorteio | Pelo menos um zero em 3 sorteios | Pelo menos um zero em 5 sorteios | Zero em dois sorteios consecutivos previamente escolhidos |
|---|---:|---:|---:|
| 1 em 4 — 25% | 57,81% | 76,27% | 6,25% |
| 1 em 6 — aproximadamente 16,67% | 42,13% | 59,81% | 2,78% |
| 1 em 8 — 12,5% | 33,01% | 48,71% | 1,56% |

Premissa: sorteios independentes, sem repetição, proteção contra sequência ruim ou outra interferência. Três e cinco sorteios são janelas de observação; **não representam uma duração de combate presumida**. A última coluna não é a chance de encontrar qualquer dupla de zeros numa sequência maior.

Cálculo: para chance de zero `q`, a chance de pelo menos um zero em `n` sorteios é `1 − (1 − q)^n`; dois sorteios específicos darem zero tem chance `q²`. [Contas completas](apoio-liberacao-irregular/comparacao-zero.json).

Não escolher a frequência só por essa tabela. Uma ficha que depende de manutenção sofre consequências diferentes de outra que conserva ações úteis sem PE. A avaliação precisa considerar o ganho concreto e os custos da ficha.

## Direção do próximo desenvolvimento

O próximo trabalho é escrever uma alteração funcional própria e mostrar a relação dela com a perda de controle da liberação. A explicação precisa responder: **o que esta energia passa a fazer que a capacidade normal não fazia?** Um teto alto apenas permite gastar o que a ficha já poderia gastar; isso não basta como compensação.

Preparar uma comparação curta de benefícios concretos antes de escolher percentuais. Cada candidato deve trazer uma capacidade-base da R53, antes/depois, exemplo durante um intervalo positivo e outro com zero, custos, duração e encerramento. A comparação deve mostrar se o ganho exige nova liberação ou aproveita um efeito já pago, sem criar silenciosamente uma exceção ao limite escolhido.

Investigar como linhas de projeto uma mudança no uso de energia já exteriorizada ou uma propriedade particular das liberações permitidas. São caminhos de pesquisa do assistente, não escolhas do autor nem capacidades recuperadas como prontas. Qualquer quantidade de energia deve seguir a referência percentual da R53. Evitar duplicar Armado/Segura, conceder dano por Pacto ou compensar duas vezes a mesma limitação.

Depois de escolher a troca, comparar frequência de zero e tetos positivos em fichas com custos distintos. O exemplo final continuará experimental até ser avaliado em uso; a redação da pré-1.0 pode avançar sem aguardar esse teste.

## Histórico e referências

A [comparação inicial](apoio-liberacao-irregular/comparacao-hipotetica.json) e a [comparação ampliada de ritmos](apoio-liberacao-irregular/comparacao-de-ritmos.json), reproduzível pelo [script](apoio-liberacao-irregular/comparar-ritmos.py), usaram aumento de reserva e distribuições sem zero. São hipóteses históricas, não a proposta atual. O segundo estudo foi iniciado antes das respostas desta etapa e foi identificado como histórico após recebê-las. Não transportar seus resultados como recomendação da nova distribuição.

Fontes atuais: [R53 — Pacto permanente](</home/mizuki/CHAT-GPT/RPG -JJK/entregas/livro-diagramado-r53/LIVRO-COMPLETO.md#ritual--pacto-permanente>), [Ideias para desenvolver](</home/mizuki/CHAT-GPT/RPG -JJK/entregas/livro-diagramado-r53/LIVRO-COMPLETO.md#ritual--pacto-restricao>), [Armado](</home/mizuki/CHAT-GPT/RPG -JJK/entregas/livro-diagramado-r53/LIVRO-COMPLETO.md#catalogo--melhoria-armado>), [Segura](</home/mizuki/CHAT-GPT/RPG -JJK/entregas/livro-diagramado-r53/LIVRO-COMPLETO.md#catalogo--melhoria-segura>), [energia de entidades](</home/mizuki/CHAT-GPT/RPG -JJK/entregas/livro-diagramado-r53/LIVRO-COMPLETO.md#campo--inv-energia>) e [manutenção](</home/mizuki/CHAT-GPT/RPG -JJK/entregas/livro-diagramado-r53/LIVRO-COMPLETO.md#campo--inv-manutencao>).

Fontes históricas: [Pactos](</media/mizuki/HD Externo II/Claude/Claude 2/sistema/03-mecanica/22-pactos.md>), [rascunho arquivado](</media/mizuki/HD Externo II/Claude/Claude 2/sistema/99-arquivo/RASCUNHO-pactos.md>) e [manual anterior](</media/mizuki/HD Externo II/Claude/Claude 2/sistema/05-material/livro/manual/65-pactos.md>).

Verificação documental e aritmética. Não houve teste de mesa, simulação de combate ou validação de equilíbrio.

**Próxima tarefa:** comparar ganhos funcionais concretos de Liberação irregular, com base na R53 e casos de resultado zero. **GPT-6 Astra, esforço alto**, pela interação entre custo, momento de pagamento e efeito. Depois da escolha, redação e revisão de clareza com GPT-6 Sol, esforço alto.

**Continuação:** [documento 50](50-comparacao-de-beneficios-da-liberacao-irregular.md) apresenta dois benefícios concretos para escolha. A orientação de escrever a comparação foi cumprida; Refluxo foi escolhido como direção de ganho. Percentual, usos e distribuição ainda serão avaliados.

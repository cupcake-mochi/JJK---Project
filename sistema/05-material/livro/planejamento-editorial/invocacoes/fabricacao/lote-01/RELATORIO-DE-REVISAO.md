# Revisão da fabricação de entidades

Manuscrito: 5 páginas. SHA-256: `6b0c6fdc6690e154c064c44ddad58e02593fb3c1a38da3f3ba097e376fc471b0`.

A referência pendente passou a ter procedimento: resultado/ficha, responsável treinado e receita, recursos/prazo definidos, um teste final de ofício, retrabalho informado e entrega em estado inicial. Herança recebeu projeto de alteração do vínculo, com preservação dos estados. A autoria não modificou R11/R12/equipamento nem o manual.

## Regras e localização

§107 pediu teste único de ofício na escada que acompanha, tempo e materiais, fora do capítulo de Invocações. R04 agora fornece o procedimento geral de fabricação; a nova seção é uma aplicação desse procedimento. A pasta de produção está em invocacoes para reunir fontes, mas a publicação deve colocar a seção junto de Fabricação/Ofícios. R12 conserva a ficha e o catálogo; R11 conserva campo, reparo e retorno. As remissões da raiz devem apontar para fab-entidades e fab-conclusao.

Criação sem técnica/slot é decisão autoral §71. Aprender o processo não concede técnica pessoal: materiais preparados e participantes podem atender a parte sobrenatural. A tarefa não produz uma Origem ou alma autônoma por compra. O processo e seus meios permanecem necessários.

O teto do responsável, estados iniciais e transferência são fechamentos candidatos necessários, explicitados em FAB03/08/09/10. O teto de nível também considera o destinatário. Dificuldade é por Classe, mas alguém de nível 13 não produz entidade de nível 16 só por ambos estarem na Classe 4.

## Resultados numéricos

`auditar.py` executou 58 verificações, 27 casos dirigidos, a matriz de 27.000 combinações de níveis e 196 perfis de atributo/Maestria/diferença de Classe. Foram enumerados 164.640 resultados de dados, com e sem vantagem; não houve amostragem aleatória.

A dificuldade preservada dá **65%, 75%, 85%** de sucesso no teste treinado comum, respectivamente Classe igual, uma abaixo e duas ou mais abaixo. Especialização é um bônus do teste, não da CD; ajuda melhora a chance, não remove requisitos. Com vantagem, as três chances são **87,75%, 93,75%, 97,75%**. Isso mostra por que a rolagem não deve ser tratada como principal preço de aquisição.

O exemplo lê valores do próprio manuscrito. Uma falha mais um sucesso gasta ¥36.000 e 20 horas; com um estojo recém-comprado, ¥46.000. Sob a hipótese de 75% constantes, retrabalho sempre disponível e nenhuma mudança de projeto, a média teórica é ¥32.000 e 17⅓ horas por conclusão. A chance de terminar em até três tentativas é98,4375%. Os valores de ferramentas vieram da linha própria do catálogo atual.

Não há nova tabela econômica universal. Dinheiro de campanha, frequência de pausas, ajuda disponível e quantidade de materiais raros ainda determinam o custo real. O preço do exemplo serve para ensinar, não para certificar que toda entidade de nível 9 deve custar ¥30.000. A regra atual R04 já escolheu orçamento por projeto; substituí-la por custo baseado em arma/raridade conflitaria com o dono.

## Funcionalidade e limites

O modelo confirma bloqueios por nível do artesão/receptor, falta de treino/processo/meios, retrabalho incompleto e repetição sobre peça concluída. Na transferência testa furto, ausência do objeto, combate, falha, receptor insuficiente, preservação dePV/carga/usos/queda e recusa a criatura destruída. O modelo não é um motor completo de invocações: controle de corpos, ações/ciclos, equipamentos e alma também foram conferidos por leitura dos donos e invariantes de texto.

A perda anunciada na falha protege a decisão do jogador; a nova tentativa exige a correção material/temporal. Trocar de artesão não produz uma rolagem gratuita na mesma peça. Um corpus de receitas padronizadas, se desejado depois, pode fixar projetos frequentes sem mudar este procedimento. Não se deve anunciar estoque ilimitado barato com base somente no exemplo.

Transferência não reseta nenhum recurso. A carga herdada já foi paga pelo invocador anterior, como §86 determinou. Corpos excedentes permanecem sem controle, conforme R11-48. O avanço futuro do personagem não eleva a criatura criada; a existência de um novo projeto não autoriza uma atualização automática da ficha antiga.

## Texto e comparação

A revisão contextual por página está em REVISAO-EDITORIAL.json. Os títulos são diretos e os exemplos mostram decisão/custo/resultado. Os campos mínimos permitem operar o procedimento; não repetimos o catálogo de habilidades, as ações de comando nem a cura dos corpos.

A ordem de ferramentas, materiais e tempo foi comparada à apresentação do PHB2024 local, p.233 impressa, e à [fonte oficial](https://www.dndbeyond.com/sources/dnd/br-2024/equipment). Mantivemos a ordem didática, sem importar seus descontos ou prazos. A [fabricação de itens mágicos](https://www.dndbeyond.com/sources/dnd/br-2024/magic-items) ajudou a verificar que os requisitos do resultado sobrenatural precisam estar claros. Não houve afirmação factual nova sobre JJK nem uso de F&M como cânone.

O validador editorial automático retornou **zero achados** após o cadastro pela raiz. Isso não substitui a leitura de outra pessoa. A seção Conclusão e transferência é a mais densa e merece atenção no PDF.

## Estado e validação futura

V01–V11 e V15 possuem evidências, com limitações descritas. **V12 (revisão independente),V13 (PDF/navegação) e V14 (inspeção visual) permanecem pendentes.** Não gerei ou inspecionei PDF. Não houve teste com jogadores, nem medição de diversão, tempo real de consulta ou economia de campanha.

A verificação de fontes detectou alteração concorrente de R12 pela raiz: remissões de reparo e troca de “inativos” por “corpos mantidos”. Foi confirmada, relida e registrada em fontes-concorrentes.json, sem fórmula nova. A checagem só aceita esse hash exato; outra mudança exige novo cotejo. Não se apresenta a fonte mutável como se nunca tivesse mudado.

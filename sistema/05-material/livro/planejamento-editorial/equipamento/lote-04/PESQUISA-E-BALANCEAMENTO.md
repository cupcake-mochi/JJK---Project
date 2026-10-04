# Pesquisa e avaliação numérica: armas e munição

03/10/2026. Base publicada v0.331. Esta é avaliação documental com modelos exatos, sem observação de partidas novas e sem entrevista com jogadores. Não chamar este trabalho de pesquisa de campo concluída. Contrato anterior ao modelo em CONTRATO-NUMERICO.md; código reproduzível em validar_numeros.py; resultados completos em evidencias/regras-verificadas.json.

## Referências efetivamente consultadas

| Fonte primária | Observação | Uso nesta revisão e limite |
|---|---|---|
| [D&D Basic Rules 2024, Equipment](https://www.dndbeyond.com/sources/dnd/br-2024/equipment) | Lista peso, preço, propriedades e tipo de dano; 20 flechas pesam 1 lb e a aljava vazia pesa outra libra. | Separar dados de consulta de procedimento. Não converter moedas, quilos ou regra Loading para o Projeto M. |
| [Pathfinder 2e, Player Core, Bulk](https://2e.aonprd.com/Rules.aspx?ID=2143&Redirected=1) e [Arrows](https://2e.aonprd.com/Weapons.aspx?ID=443) | Bulk inclui tamanho e dificuldade de transporte; dez itens L equivalem a 1 Bulk; dez flechas têm L. | Comparação favorável a 20 flechas ocuparem 0,2 em uma escala abstrata. As regras de arredondamento e capacidade são diferentes: não há equivalência integral. |
| [Cairn, primeira edição, SRD](https://cairnrpg.com/first-edition/cairn-srd/) | Dez espaços de inventário, agrupamento de objetos pequenos e custo maior para volumosos. | Contraste: pressão forte sobre o inventário. Importar essa pressão exigiria revisar o catálogo e a capacidade inteira. |
| [GLOCK, ficha técnica G17](https://eu.glock.com/en/products/pistols/g17) | 625 g sem carregador, 705 g com carregador vazio e 915 g carregada; o fabricante ressalva variação conforme a munição. | Diferenças indicam carregador cheio de aproximadamente 290 g, contra 915 g da arma carregada. Um carregador já custar tanto Volume quanto a arma compacta não sugere que ele esteja universalmente leve demais. É um único modelo real, não valida todos os recipientes do jogo. |

As referências sustentam comparações de estrutura e ordem de grandeza. A escolha final é de design do Projeto M. Nenhum texto ou catálogo foi copiado. A capacidade das armas de fogo no jogo mede ataques, não cartuchos físicos; os valores reais não permitem converter um carregador real em ataques do sistema.

## Decisão de carga

Aljava de 20 flechas e estojo de 20 virotes passam de 0,1 para 0,2 Volume na candidata. Preço de ¥3.000 mantido. Demais munições ficam em 0,1; caixa da Metralhadora Pesada fica em 0,2.

| Volume de um recipiente | Recipientes por 1 Volume | Projéteis, se cada um leva 20 | Disparos de pistola, se cada carga permite 2 |
|---|---|---|---|
| 0,1 | 10 | 200 | 20 |
| 0,2 | 5 | 100 | 10 |
| 0,5 | 2 | 40 | 4 |
| 1 | 1 | 20 | 2 |

Esta tabela é sensibilidade, não quatro propostas simultâneas. A mudança corta pela metade a capacidade por Volume para flechas e virotes. Ainda permite muitas reservas: não afirmamos ter criado escassez forte. Para aumentar toda a pressão logística, precisaríamos revisar juntos armas compactas de 0,1, outros itens e o limite de 5 + Força.

O fator de 12 kg por Volume é o recurso do livro para objetos sem valor próprio. Não representa a massa exata de cada item já tabelado. Portanto, 0,1 Volume não significa que todo carregador tenha 1,2 kg.

Cenários simples, sem mochila/ferramentas adicionais: com Força 0, Hankyū (2), Traje 1 (0,1) e aljava (0,2) somam 2,3, deixando 2,7 da capacidade 5. Pistola carregada (0,1), Traje 1 (0,1) e duas reservas (0,2) somam 0,4, deixando 4,6. A diferença vem principalmente das armas; aumentar só a reserva esconderia esse problema. A enumeração inclui Força 0 a 6 e só monta exemplos que cumprem o requisito da arma.

## Preço e disponibilidade

As linhas correntes dão ¥150 por flecha/virote; ¥500 por ataque com pistola, revólver, espingarda, rifle e submetralhadora; ¥1.000 com rifle de precisão e metralhadora pesada. O custo por dano não é uniforme e não precisa ser. O orçamento de exemplo de ¥20.000 compra 40 disparos de pistola, 39 de rifle, ou 20 de precisão, respeitando a venda em conjuntos. Isso não é renda presumida de uma missão.

Com orçamento inicial de ¥150.000, a Pistola de ¥125.000 deixa ¥25.000 e a Espingarda de ¥150.000 não deixa saldo; ambas incluem o estoque inicial definido na candidata. Grau ou autorização continuam exigidos. Esses preços foram preservados; a revisão do kit deverá considerar ferramentas, renda, reposição e acesso. Não adotamos preços de mercado real como medida de equilíbrio.

## Dano e propriedades

Dano abaixo é por acerto, antes de RD, Bloquear, acerto/erro e benefícios de Caminho. Par compara a soma de dois conjuntos completos; críticos dobram o número de dados antes da comparação. Não dobra o resultado final de Par.

| Caso | Média normal | Média no crítico |
|---|---|---|
| d6 sem Par | 3,5 | 7 |
| d6 com Par | 4,4722 | 8,3719 |
| 2d6 com Par | 8,3719 | 15,9334 |
| Soqueira, d4 com Par | 3,125 | 5,8906 |
| Katana, d8 | 4,5 | 9 |

Katana em duas mãos passa a d10, média 5,5 antes do atributo. Os registros incluem o atributo de 0 a 6 onde ele se aplica; bestas e armas de fogo não somam atributo ao dano básico. Par não adiciona ataque nem multiplica Canalizar. Não se pode usar estas médias para concluir que duas Trilhas causam o mesmo dano.

A comparação conservadora exige mesma categoria, tipo, mãos, dado e propriedades, então compara requisito, Volume, preços e alcance. Encontrou Revólver superior à Pistola no alcance normal e longo, sem contrapartida nesses eixos; capacidade e custo da munição também são iguais. É pendência antiga, preservada para revisão própria. Soqueira e Tekko são equivalentes nos números; podem ser variações de aparência, não necessariamente erro. O teste não detecta todas as vantagens possíveis entre categorias ou conjuntos diferentes de propriedades.

## Sequência de ataques e recargas

Modelo com seis turnos, arma inicialmente cheia, reserva suficiente, três oportunidades de ataque por turno que não gastam Ação Bônus, uma Ação Bônus livre por turno e mãos disponíveis. Recarrega quando precisa; se a Bônus sobrar, completa no fim do turno para o próximo. Não troca de arma. Calcula exatamente a distribuição dos gatilhos de 1/2, sem sorteio de amostra. Esta política é explícita, não uma prova de estratégia ótima em qualquer combate.

| Capacidade | Disparos esperados, d20 normal | Com vantagem | Com desvantagem |
|---|---|---|---|
| 1 | 7,000 | 7,000 | 7,000 |
| 2 | 13,300 | 13,930 | 12,670 |
| 3 | 17,671 | 17,998 | 16,767 |
| 4 | 17,866 | 17,999 | 17,325 |

O máximo oferecido no cenário é 18 oportunidades. A besta dispara duas vezes no primeiro turno e uma nos demais, totalizando sete: não existe outra Bônus para rearmá-la. Arcos sem ciclo de recarga não sofrem essa limitação. Ações extras, troca de arma e habilidades que mudem os custos exigem outro cenário. Com reserva finita, o total de disparos também fica limitado pelo estoque: os resultados da tabela não são fornecimento gratuito.

O modelo enumera ainda uma e duas oportunidades por turno. Os 34 casos de conservação e 6.820 estados conferem que recarregar, preparar após 1/2 ou transferir não cria munição. Reduzir a reserva mexe na duração da expedição; mudar recarga mexe também na economia de ações. São decisões diferentes.

## Alcance e tipo de dano: mudanças candidatas

Oito armas já possuíam Alcance, mas o texto publicado só atribuía 3 m à categoria Armas Longas: Bastão, Bō, Kusarigama, Chicote, Corrente, Espadão, Nodachi e Odachi. A candidata faz a propriedade conceder 3 m a todas elas; preserva a propriedade e sincroniza seu dono em Equipamento em jogo. Isso amplia a área de ameaça e possíveis oportunidades. Exige ensaio de combate com corredores, aproximação e recuo; não foi contabilizado como dano adicional por acerto. Diagonais e alcance tridimensional ainda dependem da frente Movimento.

A tabela antiga não tinha coluna de tipo. Os tipos físicos agora explícitos são propostas: lâminas cortam, pontas e projéteis perfuram, armas de impacto e correntes causam Concussão; Tessen usa Concussão como leque de combate. É convenção para o ataque comum, não afirmação histórica nem uma lista completa dos usos de cada objeto. Golpear de outro modo dependerá de armas improvisadas, próxima unidade. Conferir resistências dos inimigos quando a lista estabilizar.

## Ensaios de mesa a realizar

Registrar uma missão curta e outra com vários encontros: reserva inicial, disparos, recargas, Bônus disputadas, recipientes vazios, compras e carga total. Comparar antes/depois da aljava com o mesmo personagem e a mesma rota. Registrar escolhas entre Pistola/Revólver e exemplos de alcance 3 m que mudaram uma decisão. Medir dúvidas de leitura e tempo de consulta, além do dano.

Critério de revisão: identificar reservas que nunca importam, armas escolhidas apenas por superioridade sem custo, gasto de Bônus que impede repetidamente o papel desejado e carga que força abandonar itens essenciais sem decisão interessante. Ainda não há amostra humana nem limiar validado de aceitação. Não inventar porcentagem de equilíbrio a partir dos testes documentais.

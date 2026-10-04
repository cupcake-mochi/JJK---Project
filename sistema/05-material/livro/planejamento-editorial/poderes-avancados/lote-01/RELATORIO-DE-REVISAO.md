# Revisão de Poderes avançados — R08

A candidata contém 15 páginas, com 180–400 palavras por página, e concentra a Expansão de Domínio. Liberação e Técnica Máxima continuam em Fundamento. O texto do jogador não repete o catálogo de aptidões, os Caminhos ou as Trilhas. Foram registradas 33 decisões, distinguindo reorganização, preservação e fechamento mecânico.

## Cobertura e função

A sequência acompanha a tarefa: adquirir e registrar; criar Acerto/Efeito; resolver o Acerto; proteger-se; abrir e manter; romper ou mover; encerrar; usar o modo aberto; disputar; sustentar a disputa; resolver sobreposições e vários domínios. Duas fichas completas e um confronto fecham a leitura.

A revisão contextual por página está em `evidencias/REVISAO-EDITORIAL.json`. Ela examina clareza, suficiência, voz, títulos, vocabulário, repetição, localização, regras, compatibilidade, comparação com RPGs e limite da validação canônica. O bloqueio editorial passou com uma única remissão justificada a Regravação. O falso encontro de “resguardar” com o nome de uma habilidade foi eliminado pela escolha da palavra cotidiana “proteger”.

## Números executados

`python3 auditar.py` executa 154 verificações, 1.818 estados de preço, 3.600 sequências de CDs para o teste único do inimigo, 1.728 tríades de d12 com todas as ordens de pares, 1.001 valores de dano no interior da barreira e 27 perfis de sobrevivência numa corrida.

O script lê a progressão de Classe/Maestria e a curva máxima de refino dos donos atuais. As comparações de desconto não concedem refino 10 aos níveis que ainda não podem alcançá-lo. Os resultados e hashes estão em `evidencias/auditoria-numerica.json`.

| Nível | Liberação: teto sem peças / PE | Máxima: dados / PE | Acerto de domínio / abertura fechada |
|---|---|---|---|
| 17 | 20d8 / 23 | 24d8 / 25 | 10d8 por aplicação / 30 |
| 21 | 24d8 / 27 | 28d8 / 30 | 12d8 por aplicação / 36 |
| 26 | 28d8 / 32 | 32d8 / 35 | 14d8 por aplicação / 42 |

Esses são dados brutos e custos de referência. Não incluem acerto, crítico, defesas, quantidade de alvos ou outras peças. O teto da Liberação não significa que toda combinação alcance esse valor. A Máxima de cura conserva o mesmo total de dados da sua faixa, com o modo de aplicação previsto em R06; dano e cura não foram convertidos numa moeda comum de balanceamento.

A Máxima ainda tem a maior aplicação imediata entre esses valores. Domínio pode superar muito esse total se permanecer: no refino 10, seis Acertos de 14d8 são 84d8 por criatura exposta, média bruta 378. Isso é uma ameaça persistente e exige defesas e formas de encerrar a área. Não seria correto concluir apenas pela diferença entre 32d8 e 14d8 que Domínio é mais fraco.

Com Essência 6 e chance de falha de 35% por dano, a probabilidade de conservar a Expansão até o fim de cinco rodadas é 76,48% recebendo um dano por rodada; 26,16% com dois; 1,21% com quatro. O modelo só mede o teste da corrida e pressupõe danos que efetivamente ocorram. Não inclui morte, barreira, duração encurtada ou decisão de jogadores.

O d12 separa 72 dos 144 pares: 50%. O script também verifica que refino decide antes da natureza do Acerto e que apenas um Acerto sem dano vence esse desempate. Dois sem dano ainda precisam do d12. Não se repetem esses dados a cada rodada.

## Mudanças que precisam continuar visíveis na revisão

- **Raio aberto de 199,5 m:** atende o pedido de distâncias em múltiplos de 1,5 m. Redução de 0,25% no raio e aproximadamente 0,4994% na área, frente aos 200 m antigos.
- **Dano de Acerto explícito:** 2 × maior Classe em d8, derivado dos cálculos históricos de 3C menos Média. Desconto de Família não aumenta esse valor.
- **Vida compartilhada da barreira:** elimina restauração por mudança de face. Quarto do dano no interior é simples, mas o arredondamento não é neutro para impactos muito pequenos. Por exemplo, 1 ponto repetido derruba 100 PV após 100 impactos no novo registro; a antiga representação de 200 PV internos com resistência arredondada precisaria de 200. Em dano múltiplo de quatro, a equivalência é exata.
- **TR único do inimigo:** reutiliza o total do primeiro teste quando a mesma pessoa causa dano com CD maior. Preserva um teste/uma falha por personagem por rodada e resolve o momento que a fonte deixava indefinido.
- **Duração com endpoint:** abertura e metade do refino em turnos seguintes, terminando ao final do último. Preserva os seis Acertos e cinco turnos com desconto da conta histórica de refino 10.
- **Alvos, Incompleta e múltiplos:** agora possuem procedimentos explícitos. São fechamentos mecânicos candidatos, não fatos canônicos nem resultados de playtest.

## Cânone e comparação editorial

A amostra do PHB 2024 foi usada para a organização por alvo, custo, alcance, duração e efeito. O procedimento de concentração de D&D não foi transplantado para a corrida. Esta preserva seus próprios atributos, CDs e assimetria entre jogador e inimigo.

As consultas oficiais de Jujutsu disponíveis trouxeram metadados e sinopse, sem acesso integral às cenas necessárias. Por isso a tabela antiga com explicações dos poderes de personagens foi removida da candidata. Não alegamos que consultar uma página de capítulo verifica todos os painéis. Os exemplos do capítulo são originais e identificados como regras do Projeto - M.

## Limites da entrega

Há auditoria de contas e leitura documental, sem teste humano. Nenhum modelo comprovou que todo Efeito original seja equilibrado, que um grupo iniciante encontre todas as regras ou que a duração seja divertida na mesa. Testes com pessoas devem medir consulta durante uma disputa, compreensão do Acerto sem dano e execução de uma defesa quando a área se sobrepõe a outra.

A revisão independente está em evidencias/REVISAO-INDEPENDENTE.md. Seus três achados foram tratados: metade dos dados no sucesso do TR, primeira entrada na regra contínua e identidade do personagem de exemplo. A inspeção visual cobriu as15 páginas do PDF atual e a conferência automática passou124 verificações. O manuscrito não afirma aprovação mecânica final. Objetos, Integridade e o futuro sistema de morte conservam suas pendências no projeto; o capítulo usa o gatilho vigente de 0 PV e registra a necessidade de consolidar o procedimento de dano a estruturas.


## Correção após leitura independente

Na Incompleta, o sucesso do TR usa metade dos dados, seguindo Fundamento. Para uma regra contínua, cada alvo novo testa na primeira entrada, se ainda não tiver resultado válido, e conserva a resolução até o próximo Acerto ou fim do domínio. O modelo adicional percorre32 estados de entrada e reentrada.

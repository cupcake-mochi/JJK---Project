# Revisão de Vanguarda

## Cobertura e fontes

A edição integrada do Caminho e suas três Trilhas foi lida integralmente. O inventário relaciona as entradas da fonte às seções da candidata. Sequência, Conduções, Conclusões, Escola de Arma, Estocada, as três rotas do Batedor e Executor permanecem disponíveis. A comparação textual completa foi preservada. As fontes e a publicação v0.331 não foram alteradas.

As quinze decisões de revisão têm antes, depois e motivo em ALTERACOES. A principal adaptação funcional envolve o estoque concreto de munição do capítulo de equipamento. Reposições retiram unidades do inventário. A capacidade adicional da Arma de Fogo não cria uma unidade. O Yumi reserva a flecha ao armar e a gasta ao disparar. A Besta já carregada pode disparar sem exigir uma recarga desnecessária.

## Funcionamento e números

A auditoria tem 70 verificações e 34 casos funcionais. O modelo percorre 240 estados de Sequência, 57 perfis de ataque e resistência, 1.638 transições de recarga, 23 transições de virotes e 1.296 pares de dano. A revisão independente acrescentou 20 estados de flechas reservadas e 1.512 perfis de conservação de munição. Esses números representam enumerações dos modelos, não partidas ou personagens completos.

A Sequência cobra recursos na tentativa, conserva o limite de uma Condução ou Conclusão por turno próprio e só renova seu prazo no acerto apropriado. Persistência mantém a Sequência após falha sem transformar a tentativa em acerto. Conclusão Dupla resolve um dano e dois efeitos com requisitos próprios. Trocar de Intenção não produz uma segunda resposta em cadeia. Ferrão explicita sua exceção ao limite de conjuração e a substituição dos dados de Canalizar em Golpe ou Estímulo naquele golpe.

Sob as hipóteses de 65% de acerto e 45% de falha no TR, a opção de Finta eleva a chance de algum efeito de 29,25% para 45,3375%. Isso depende da possibilidade de escolher uma alternativa válida. O custo e o limite da Sequência permanecem. A desvantagem aplicada a uma soma de 2d6 tem média 3.647/648, diferente de aplicar desvantagem separadamente a cada dado, cuja soma tem média 91/18. O texto usa a primeira interpretação. Não se deduz dessas contas equilíbrio global entre Trilhas.

## Escrita e referências

A leitura dirigida dos livros locais, sobretudo PHB 2024 e DMG 2024, está registrada em fundamento/lote-01/REVISAO-DE-VOZ.md. A candidata aplica títulos de consulta, ordem de resolução e exemplos perto das decisões. Não houve cópia de prosa ou arte. As vinte seções foram revistas quanto a suficiência, vocabulário, redundância e localização. Procedimentos gerais de estoque e Energia Temporária ficam nos respectivos donos, conservando aqui as exceções necessárias.

O exemplo final usa nível 10 e Maestria 2 para que os ataques disponíveis sustentem sua sequência. Nenhuma mecânica deste Caminho foi apresentada como regra confirmada do mangá. Não há nova alegação canônica a validar nesta unidade.

## Revisão independente e PDF

O agente compatibilidade leu a fonte e a candidata inteiras e revisou as interfaces com equipamento, Aptidões e Fundamento. Três achados foram resolvidos: mão necessária apenas para recarregar a Besta, duas unidades carregadas para o gasto de Tiro Controlado e concordâncias na contagem de munição. O parecer está vinculado ao texto final.

O agente principal inspecionou as vinte páginas do PDF. Depois dos ajustes, reinspecionou as cinco páginas alteradas e comprovou que as outras quinze mantiveram os mesmos pixels. O PDF organiza as páginas em seis grupos principais recolhidos. Texto, fontes, navegação e evidências são conferidos por conferir.py.

## Dependências e limites

Vida inicial e progressão devem usar a apresentação comum dos Caminhos na consolidação. O capítulo de combate continua responsável por cobertura, condições e economia geral de ações. O estoque continua em equipamento. Nenhuma revisão por agente ou modelo substitui playtest ou teste com leitores humanos. Esta candidata ainda não está integrada ao livro único.

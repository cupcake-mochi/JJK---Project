# Revisão final da reconstrução

## Atualização de 04/10/2026

Depois da entrega de 03/10, a revisão pós-reconstrução (PR #2) mudou a candidata. As 19 correções de interface (C01 a C14), as decisões do Mizuki (D01 a D42) e as retiradas de contas de projetista estão em `../../revisao-interfaces/CORRECOES-APLICADAS.md`, com antes, depois, motivo e efeito na mesa. A pedido do autor, saíram do livro do jogador a tabela de Refino "nunca/sempre", a página Ritmo de campanha, as frases de quem escolhe sempre a mesma opção nos marcos, o total de XP até os níveis 20 e 30, o prazo da marca de mestre, a diferença de probabilidade do Ritual sem treino e três médias de dano em exemplos. Sem Técnica passou a registrar a Expressão da técnica, como a Técnica Marcial.

O livro tem agora 382 páginas e 509 blocos. A conferência estrutural aprovou 3505 verificações e 526 links. O gerador passou a impedir tabela partida com uma linha sozinha e título sozinho no pé da página; a regra está em `DECISOES-DE-MONTAGEM.md`. A inspeção visual encadeia cada página até a prova completa de 03/10 ou até a rodada em que foi aberta; nenhuma ficou sem cobertura. Os 51 achados da revisão de interfaces estão resolvidos; os 18 últimos foram decididos pelo autor na quinta passada (D25 a D41). Em 05/10/2026, a pedido do autor, o nível 7 da Vanguarda ganhou a Execução Preparada (D42); o livro mudou em 11 páginas, todas abertas.

O texto abaixo é o registro da entrega de 03/10 e conserva os números daquele dia.

A rodada de reconstrução foi concluída em 03/10/2026. A entrega é uma candidata editorial completa para revisão do autor, preservando a publicação v0.331. O livro reúne 23 fontes em 5 partes, 21 capítulos e 383 páginas. O painel de navegação tem 32 entradas, com seções acessíveis pelo índice e pelos links internos.

## Resultado

O texto passou por revisão de regras, números, interfaces, nomes, clareza, localização, referências editoriais e cânone nos capítulos pertinentes. A montagem final passou novamente pelos 15 critérios, reaproveitando evidências somente onde o conteúdo permaneceu igual ou o delta foi explicitamente revisado. A conferência estrutural final aprovou 3.492 verificações e 508 links internos. Os 510 blocos das fontes aparecem uma vez, sem omissões detectadas.

A revisão visual cobre as 383 páginas. A comparação de pixels permitiu aproveitar páginas já inspecionadas. As 80 páginas alteradas foram abertas, assim como as páginas complementares da revisão interrompida e as ampliações de tabelas e fichas. Uma última correção afetou apenas duas páginas do Malabarista, ambas reinspecionadas. Fontes e textos permaneceram legíveis, sem cortes ou sobreposições detectados. Espaço branco ao fim de uma unidade completa foi aceito; finais de habilidades isolados e fichas partidas foram corrigidos.

## Escrita e organização

Os títulos passaram a nomear assuntos e ações. A busca final não encontrou títulos do tipo “Como ler” nem títulos iniciados pelos artigos A, O, As ou Os. As regras gerais apresentam procedimentos comuns antes de exceções de personagens. O catálogo serve para consulta, enquanto Fundamento ensina a montar uma aplicação com exemplos. Glossário, índice e fichas atendem tarefas diferentes, evitando repetir explicações extensas.

A organização usa as referências editoriais já examinadas, principalmente D&D: apresentação do jogo, criação, procedimentos, escolhas de personagem, equipamentos e consulta. A redação é própria. Nenhum sistema de terceiros foi tratado como autoridade para o cânone de Jujutsu Kaisen. A apresentação separa acontecimentos da obra, exemplos inventados para ensinar e decisões do Projeto - M.

Os textos estão mais diretos e consultáveis. Essa conclusão vem da revisão por modelos e dos casos registrados, não de uma medição com leitores iniciantes. Também não existe um teste capaz de garantir que uma pessoa nunca perceba uma passagem como artificial. Preferências de voz devem ser confirmadas na próxima leitura do autor.

## Alterações que merecem atenção do autor

- **Dano e recuperação:** Morrendo passa a usar uma janela de 3 rodadas menos as Sequelas já existentes, compartilhada por Aguentar e Insistir. Socorro acumula cura válida até 20% da referência da queda; exceções expressas podem resgatar antes disso. Derrotado encerra a participação na cena e não significa morte automática. Integridade e suas recuperações foram conciliadas com esse estado. Dano de Alma afeta vida e Integridade, com suas proteções específicas. O tipo Força representa energia amaldiçoada pura; impacto físico permanece em Concussão, sem criar um segundo tipo Energético equivalente.
- **Nomes:** Incapacitado tornou-se Guarda Aberta. Passivas pagas são Talentos; Classe Passiva/CP tornou-se Categoria de Efeito/CE. Passiva Livre passou a Expressão da técnica. As duas entradas Aviso foram separadas em Identificar Feitiço e Leitura de Feitiços. O mapa explica os motivos e preserva aliases no índice.
- **Regras comuns:** ações, movimento, salto, furtividade, percepção, objetos e ferramentas têm procedimentos próprios. Furtividade não recebe uma tentativa gratuita só por usar uma arma que não revele a posição. Medidas de jogo seguem a escala prevista pelo sistema.
- **Equipamento:** munição, capacidade, recarga, preço e Volume foram registrados. Oculta não define sozinha peso ou leveza. Trajes escolhem um TR e perícias em quantidade limitada por Maestria. Ferramentas de grau4 não recebem efeito especial; grau3 e superiores incluem opções para armas, roupas, proteções e escudos.
- **Criação:** montagem e compatibilidades foram esclarecidas, com exemplos de utilidade e Técnica Máxima além de dano/cura. Invocação por espaço exige que a técnica, Manejo ou Kata comporte a entidade em seu conceito.
- **Caminhos e Trilhas:** Incursor, Assassino, Pugilista e Malabarista foram consolidados com seus custos e limites. Bastião recebeu as alterações solicitadas. Evocador e os demais Caminhos foram conciliados com regras gerais, condições, repertório e invocações.
- **Invocações:** aquisição, construção, fabricação e atuação em campo estão no mesmo livro, com procedimentos de comandos, reservas, turnos, queda e retorno.
- **Fechamento:** 17 remissões dependentes de página foram substituídas por referências estáveis. Não houve novos ajustes mecânicos nessa última etapa.

Os arquivos ALTERACOES.json de cada unidade registram antes, depois e motivo. A pasta migracao-nomes contém o mapa transversal. AJUSTES-FINAIS-INTEGRACAO.json registra as últimas 17 alterações. Esses registros incluem decisões editoriais e correções de interfaces, portanto sua quantidade não deve ser apresentada como número de novas regras.

## Limites e próxima revisão

Não foram realizados playtests humanos. Os modelos de balanceamento examinam os casos declarados em cada unidade, sem provar todas as combinações do sistema. Na mesa, os pontos prioritários são o ritmo de socorro e queda, o custo em ações das invocações, a frequência de Fluidez e continuações do Malabarista, e a viabilidade dos conjuntos de equipamento. Isso é acompanhamento da candidata, não uma pendência de redação escondida.

Nenhuma imagem de IA foi usada. Esta entrega resolve composição, tabelas, quadros e navegação; um projeto de ilustrações licenciadas pode ser feito separadamente. A publicação antiga não foi substituída automaticamente.

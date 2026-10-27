# L3 — percepção e informação

26 de outubro de 2026. Complemento da auditoria de cobertura: [Perceber, procurar e interpretar sinais](<../06 - Redacao do Guia/83-perceber-procurar-e-interpretar-sinais.md>). A etapa aplica os procedimentos da R53 aos cinco pontos M025–M029 e conecta os casos à investigação, à folha de condução e aos registros existentes.

## Entrega

| Ponto | Demonstração entregue |
|---|---|
| M025 — Esconder, buscar e sentidos alternativos | Uma Furtividade 16 contra observadores com acesso e CDs diferentes; falha, busca posterior, novo observador e Percepção de Contorno. |
| M026 — Ler o Ambiente | Caminho útil com CD, sucesso e falha; caso sem informação que conserva ação e uso. |
| M027 — Estudar, Intuição e lembranças | Comportamento observado, pergunta e resposta limitada; variante em combate; Memória Testemunha com três perguntas, incluindo uma informação inacessível na ocasião. |
| M028 — Busca energética com interferência | Uma rolagem contra a maior CD, fonte com zero PE, fonte bloqueada e ferramenta abandonada. |
| M029 — Pressão, vestígios e assinatura | Pulso distante com informação igual para observadores equivalentes; limite da triangulação; comparação de assinatura com referência confiável. |

Os casos são independentes dos pilotos. As dificuldades locais, os bônus e as posições foram escolhidos para ensino; não são tabelas gerais de ameaça nem fichas completas. Nenhuma nova decisão autoral ou mudança de regra foi atribuída ao pedido de continuar.

## Fontes e diferença de nomenclatura

O Livro do Jogador R53 editável e sua cópia preservada conservaram SHA256 `7311979bdfc61bda1d2fd5113106f072edc7dd5b8a801a02779ada53fd13a81d`. Os [trechos conferidos](apoio-lote3/fontes-conferidas.md) registram as linhas da fonte, não páginas do PDF.

| Trecho da R53 | Uso na redação |
|---|---|
| Testes; Ler o Ambiente | Cálculo, igualdade, dificuldades e diferença entre falha e ausência de informação. |
| Percepção e visibilidade; Esconder; Vasculhar | Acesso sensorial, CDs por observador, Furtividade guardada e busca ativa. |
| Estudar; Intuição | Pergunta concreta, Ação Padrão em combate, resposta sustentada pelos indícios e repetição. |
| Percepção de energia | Alcance, obstáculo, carga, interferência, PE zero, sinais distantes e assinatura. |
| Percepção de Contorno | Visão às cegas a 3 m × Maestria, com limites próprios. |
| Memória Testemunha | Um minuto, uma vez por dia, até três perguntas da mesma cena presenciada, sem teste de lembrança. |
| Tarefas e testes | Tempo anunciado fora do combate, informação evidente, repetição e trabalho conjunto. |

**Diferença encontrada:** M027 do inventário cita “Lembrança Retomada”. A fonte editável atual usa **Memória Testemunha** para o procedimento de revisitar uma cena presenciada. O manuscrito usa esse nome e o texto dessa fonte. Não se afirma uma renomeação autoral ocorrida nesta etapa, nem se cria uma segunda capacidade. O inventário e os registros históricos permanecem preservados; a diferença fica documentada aqui e na cobertura atualizada.

Não houve pesquisa externa: as dúvidas desta entrega eram de aplicação do próprio sistema, resolvidas nos textos locais.

## Casos e contas

| Caso | Conferência |
|---|---|
| Esconder | 11 + 5 = 16; CDs 14, 17 e 13. Nao fica oculto do vigia e da operadora; Sora o localiza. Sem sinal acessível, não há comparação. |
| Modificador passivo | Penumbra visual: 10 + 8 − 5 = 13. Vantagem pertinente, se existente no ramo alternativo: 10 + 4 + 5 = 19. Ouvir normalmente não recebe a penalidade visual. |
| Busca ativa | 12 + 4 = 16 localiza; 11 + 4 = 15 falha. Ação Padrão em ambos. Furtividade não é refeita. |
| Novo observador | CD 16 empata com Furtividade 16 e não localiza; CD 17 localiza. A busca ativa é outro procedimento. |
| Percepção de Contorno | Maestria 2 fornece 6 m; alvo a 4,5 m está no alcance. Furtividade ainda funciona quando seus sinais podem ser ocultados. |
| Ler o Ambiente | 9 + 5 = 14 passa; 8 + 5 = 13 falha. Ambos gastam Bônus e uso. Sem informação a oferecer, conserva ambos, sem dado. |
| Intuição | Inteligência 3 + Maestria 1 = +4; dado 10 chega a 14. Variante em combate com dado 9 chega a 13 e gasta a Padrão. |
| Memória | Um minuto e uso diário ao iniciar; três perguntas da mesma cena. O conteúdo da caixa fechada permanece inacessível. |
| Interferência | Resultado 12 + 6 = 18. Maior entre 18/16 = 18; maior entre 18/19 = 19; ferramenta sem ocultação usa 18. Porta sólida fechada continua impedindo a posição exata. |
| Sem interferência | As duas fontes ocultas voltariam às CDs 16/19; a ferramenta sem ocultação dispensaria dado após gastar a ação. O obstáculo continuaria bloqueando. |
| Pulso distante | 8 + 6 = 14 e 11 + 6 = 17 alcançam CD 14 e entregam a mesma pista do subsolo. |
| Assinatura | 8 + 6 = 14 permite a comparação anunciada com referência; não revela idade do resíduo nem posição atual do portador. |

O [conferidor](apoio-lote3/conferir.py) reproduz as contas e confere a preservação das fontes e a atualização da cobertura. Os [resultados](apoio-lote3/resultados.json) distinguem a comparação passiva de Esconder da busca ativa. Essa conferência documental não é simulação de combate nem teste com leitores.

## Clareza e integração

| Antes | Depois | Motivo |
|---|---|---|
| A investigação distinguia localizar de enxergar, sem uma tentativa completa de Esconder para vários observadores. | Uma tabela acompanha o mesmo total por sentido, dificuldade e resultado; a busca posterior usa o valor guardado. | Mostra quem sabe a posição e por que um sentido acessível muda a resolução. |
| Ler o Ambiente aparecia principalmente na seleção de procedimentos. | Um caminho útil é comparado a falha e ausência de informação. | Evita confundir recurso gasto numa falha com ação que não tinha informação a fornecer. |
| Havia limites gerais de lembranças e interpretação. | O mestre responde a uma pergunta de Intuição e a três perguntas de memória, com o que os sinais permitem. | Torna o limite aplicável sem tratar toda resposta limitada como fracasso. |
| A busca energética existente não tinha interferência. | Uma rolagem atravessa uma tabela de fontes com maior CD, zero PE e obstáculo sólido. | Evita soma de dificuldades, invisibilidade por PE zero e revelação através de portas. |
| Vestígios eram separados de autoria, mas faltava exemplo de consulta. | Pulso distante e referência de assinatura têm resultado e próximo caminho de investigação. | Mantém a pista útil sem convertê-la em localização contínua. |

As seções 05, 10, 12, 26 e 80 receberam lembretes ou remissões. O registro de descobertas continua sendo o formulário principal; não foi criado outro modelo. A navegação, as referências e o planejamento apontam para a nova seção 83.

## Cobertura e continuação

Somente **M025, M026, M027, M028 e M029** passam de P para E, significando base operacional demonstrada no manuscrito. O estado passa de **96 E/33 P/1 L para 101 E/28 P/1 L**. Restam **29 pontos** a complementar, com pesos diferentes; a lacuna L restante continua sendo M066, arma improvisada. A contagem não mede porcentagem de livro pronto.

As 20 competências conservam **16 E/4 P**. A entrega amplia exemplos e consulta sem afirmar aprendizagem observada. A [cobertura atualizada](apoio-lote3/cobertura-atualizada.json) mantém o escopo dos 130 IDs e relocaliza referências de textos integrados. Os retratos da auditoria 80 e do lote L1 continuam preservados. Seus verificadores com hashes antigos não devem ser usados como conferência da revisão atual de arquivos que foram editados depois.

Os 320 arquivos iniciais estavam íntegros. Quinze arquivos recebem integração; suas cópias anteriores ficam em `apoio-lote3/historico/`. O [registro de verificação](apoio-lote3/verificacao.json) delimita o pacote. Para conferir todo o salvamento atual, use `CONFERIR-SALVAMENTO.py` na raiz. O conferidor desta etapa é somente leitura por padrão; `--salvar` escreve apenas seu `resultados.json`.

As decisões autorais, R53, fichas de inimigos, Pactos, projetos e resultados anteriores permanecem preservados. Surpresa/Instinto, treinamentos mecânicos, Bestiário integral e demais adiamentos conservam seus destinos. Salvamento local, sem envio ao GitHub.

**Próxima tarefa:** L2 — espaço, objetos e capacidades do cenário: travessias, saltos com risco, queda sobre criatura, trajetórias, ferramentas, contenção e arma improvisada. **GPT-6 Astra, esforço extra alto**, para regras e exemplos; **GPT-6.1 Sol, esforço alto**, para clareza e integração.
